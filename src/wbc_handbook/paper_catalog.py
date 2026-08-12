"""On-demand paper coverage reporting and arXiv candidate discovery."""

from __future__ import annotations

from collections import Counter, defaultdict
from datetime import datetime, timezone
import json
from pathlib import Path
import re
from typing import Callable, Dict, Iterable, List, Mapping, Optional
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import xml.etree.ElementTree as ET


ARXIV_API = "https://export.arxiv.org/api/query"
ATOM = {"atom": "http://www.w3.org/2005/Atom"}
ARXIV_ID = re.compile(r"arxiv:(\d{4}\.\d{4,5})(?:v\d+)?$")


def load_json(path: Path) -> dict:
    with path.open(encoding="utf-8") as handle:
        payload = json.load(handle)
    if not isinstance(payload, dict):
        raise ValueError(f"{path} must contain one JSON object")
    return payload


def base_arxiv_id(paper_id: str) -> str:
    match = ARXIV_ID.fullmatch(paper_id)
    return match.group(1) if match else ""


def validate_catalog(catalog: Mapping, registry: Optional[Mapping] = None) -> List[str]:
    """Return deterministic catalog errors; an empty list means publishable."""

    errors: List[str] = []
    domains = catalog.get("domains")
    papers = catalog.get("papers")
    if not isinstance(domains, dict) or not domains:
        return ["catalog.domains must be a non-empty object"]
    if not isinstance(papers, list):
        return ["catalog.papers must be an array"]

    seen = set()
    base_ids = set()
    allowed_statuses = set(catalog.get("status_values", []))
    allowed_code_statuses = set(catalog.get("code_status_values", []))
    roles_by_domain: Dict[str, set] = defaultdict(set)
    deep_ids = set()

    for index, paper in enumerate(papers):
        prefix = f"papers[{index}]"
        if not isinstance(paper, dict):
            errors.append(f"{prefix} must be an object")
            continue
        paper_id = paper.get("paper_id", "")
        if not isinstance(paper_id, str) or not paper_id:
            errors.append(f"{prefix}.paper_id must be non-empty")
            continue
        if paper_id in seen:
            errors.append(f"duplicate paper_id: {paper_id}")
        seen.add(paper_id)
        base_id = base_arxiv_id(paper_id)
        if base_id and base_id in base_ids:
            errors.append(f"duplicate arXiv work across versions: {base_id}")
        if base_id:
            base_ids.add(base_id)

        if paper.get("analysis_status") not in allowed_statuses:
            errors.append(f"{paper_id}: invalid analysis_status")
        topics = paper.get("topics")
        if not isinstance(topics, list) or not topics:
            errors.append(f"{paper_id}: topics must be non-empty")
            topics = []
        for topic in topics:
            if topic not in domains:
                errors.append(f"{paper_id}: unknown topic {topic}")
            else:
                roles_by_domain[topic].update(paper.get("coverage_roles", []))

        code = paper.get("code", {})
        if code.get("status") not in allowed_code_statuses:
            errors.append(f"{paper_id}: invalid code.status")
        if code.get("status") == "verified_official" and not code.get("url"):
            errors.append(f"{paper_id}: verified official code needs a URL")

        if paper.get("analysis_status") == "deep_read":
            deep_ids.add(paper_id)
            if not paper.get("brief_path"):
                errors.append(f"{paper_id}: deep_read entry needs brief_path")
            if not paper.get("brief_path_en"):
                errors.append(f"{paper_id}: deep_read entry needs brief_path_en")

    for domain, config in domains.items():
        missing = set(config.get("required_roles", [])) - roles_by_domain.get(domain, set())
        if missing:
            errors.append(f"{domain}: missing coverage roles {sorted(missing)}")
        if not config.get("discovery_query") or not config.get("keywords"):
            errors.append(f"{domain}: discovery_query and keywords are required")

    if registry is not None:
        registry_by_id = {
            paper.get("paper_id"): paper for paper in registry.get("papers", [])
        }
        registry_ids = set(registry_by_id)
        if deep_ids != registry_ids:
            errors.append(
                "deep_read catalog entries must exactly match registry papers; "
                f"catalog_only={sorted(deep_ids - registry_ids)}, "
                f"registry_only={sorted(registry_ids - deep_ids)}"
            )
        catalog_by_id = {
            paper.get("paper_id"): paper for paper in papers
            if paper.get("analysis_status") == "deep_read"
        }
        for paper_id in sorted(deep_ids & registry_ids):
            for field in ("brief_path", "brief_path_en"):
                if catalog_by_id[paper_id].get(field) != registry_by_id[paper_id].get(field):
                    errors.append(
                        f"{paper_id}: catalog and registry disagree on {field}"
                    )
    return errors


def coverage_report(catalog: Mapping) -> dict:
    """Build the user-facing per-topic status report."""

    rows = []
    papers = catalog.get("papers", [])
    for domain, config in catalog.get("domains", {}).items():
        topic_papers = [paper for paper in papers if domain in paper.get("topics", [])]
        roles = set()
        for paper in topic_papers:
            roles.update(paper.get("coverage_roles", []))
        rows.append({
            "domain": domain,
            "title_zh": config.get("title_zh", domain),
            "total": len(topic_papers),
            "deep_read": sum(paper.get("analysis_status") == "deep_read" for paper in topic_papers),
            "queued": sum(paper.get("analysis_status") == "queued" for paper in topic_papers),
            "official_code": sum(
                paper.get("code", {}).get("status") == "verified_official"
                for paper in topic_papers
            ),
            "coverage_roles": sorted(roles),
            "missing_roles": sorted(set(config.get("required_roles", [])) - roles),
        })
    return {
        "updated_at": catalog.get("updated_at"),
        "counts": Counter(paper.get("analysis_status") for paper in papers),
        "domains": rows,
    }


def _arxiv_query(query: str) -> str:
    terms = [term.strip() for term in re.split(r"\s+AND\s+", query, flags=re.I)]
    encoded = []
    for term in terms:
        if term.startswith("(") and term.endswith(")"):
            alternatives = [item.strip() for item in re.split(r"\s+OR\s+", term[1:-1], flags=re.I)]
            encoded.append("(" + " OR ".join(f'all:"{item}"' for item in alternatives) + ")")
        else:
            encoded.append(f'all:"{term}"')
    return " AND ".join(encoded)


def parse_arxiv_feed(xml_data: bytes) -> List[dict]:
    root = ET.fromstring(xml_data)
    results = []
    for entry in root.findall("atom:entry", ATOM):
        raw_id = (entry.findtext("atom:id", default="", namespaces=ATOM).rstrip("/").split("/")[-1])
        base_id = re.sub(r"v\d+$", "", raw_id)
        title = " ".join(entry.findtext("atom:title", default="", namespaces=ATOM).split())
        summary = " ".join(entry.findtext("atom:summary", default="", namespaces=ATOM).split())
        authors = [
            node.findtext("atom:name", default="", namespaces=ATOM)
            for node in entry.findall("atom:author", ATOM)
        ]
        results.append({
            "paper_id": f"arxiv:{base_id}",
            "title": title,
            "summary": summary,
            "authors": authors,
            "published_at": entry.findtext("atom:published", default="", namespaces=ATOM),
            "updated_at": entry.findtext("atom:updated", default="", namespaces=ATOM),
            "paper_url": f"https://arxiv.org/abs/{base_id}",
        })
    return results


def discover_candidates(
    catalog: Mapping,
    max_per_topic: int = 10,
    fetcher: Optional[Callable[[str], bytes]] = None,
    topics: Optional[Iterable[str]] = None,
) -> List[dict]:
    """Discover and rank unseen arXiv records without mutating the catalog."""

    if max_per_topic < 1:
        raise ValueError("max_per_topic must be positive")
    known = {base_arxiv_id(paper.get("paper_id", "")) for paper in catalog.get("papers", [])}
    known.discard("")
    available_topics = set(catalog.get("domains", {}))
    selected_topics = available_topics if topics is None else set(topics)
    unknown_topics = selected_topics - available_topics
    if unknown_topics:
        raise ValueError(f"unknown topics: {sorted(unknown_topics)}")
    if not selected_topics:
        raise ValueError("at least one topic is required")
    if fetcher is None:
        def fetcher(url: str) -> bytes:
            request = Request(url, headers={"User-Agent": "humanoid-wbc-handbook/0.2"})
            with urlopen(request, timeout=45) as response:
                return response.read()

    merged: Dict[str, dict] = {}
    for domain, config in catalog.get("domains", {}).items():
        if domain not in selected_topics:
            continue
        params = urlencode({
            "search_query": _arxiv_query(config["discovery_query"]),
            "start": 0,
            "max_results": max(20, max_per_topic * 3),
            "sortBy": "lastUpdatedDate",
            "sortOrder": "descending",
        })
        for candidate in parse_arxiv_feed(fetcher(f"{ARXIV_API}?{params}")):
            base_id = base_arxiv_id(candidate["paper_id"])
            if base_id in known:
                continue
            text = f"{candidate['title']} {candidate['summary']}".lower()
            score = sum(3 if keyword.lower() in candidate["title"].lower() else 1
                        for keyword in config.get("keywords", []) if keyword.lower() in text)
            record = merged.setdefault(base_id, {**candidate, "proposed_topics": [], "scores": {}})
            record["proposed_topics"].append(domain)
            record["scores"][domain] = score

    ranked = sorted(
        merged.values(),
        key=lambda item: (max(item["scores"].values()), item.get("updated_at", "")),
        reverse=True,
    )
    per_topic = Counter()
    selected = []
    for item in ranked:
        available = [topic for topic in item["proposed_topics"] if per_topic[topic] < max_per_topic]
        if not available:
            continue
        item["proposed_topics"] = available
        selected.append(item)
        for topic in available:
            per_topic[topic] += 1
    return selected


def write_candidate_run(path: Path, candidates: Iterable[Mapping]) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "mode": "manual_on_demand",
        "auto_accepted": False,
        "candidates": list(candidates),
    }
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return path
