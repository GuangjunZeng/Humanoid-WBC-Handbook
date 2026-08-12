"""Quality-gated, on-demand discovery for WBC-related open-source projects."""

from __future__ import annotations

from collections import Counter, defaultdict
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import re
from typing import Callable, Iterable, List, Mapping, Optional
from urllib.parse import urlencode
from urllib.request import Request, urlopen


GITHUB_SEARCH_API = "https://api.github.com/search/repositories"
GITHUB_REPO = re.compile(r"^https://github\.com/([^/]+)/([^/#?]+?)/?$", re.I)
STATUS_VALUES = {"queued", "deep_review"}
RELATION_VALUES = {"project_only", "official_paper_code", "infrastructure"}


def _repo_key(url: str) -> str:
    match = GITHUB_REPO.fullmatch(str(url).strip())
    if not match:
        return ""
    return f"{match.group(1)}/{match.group(2)}".lower()


def validate_project_catalog(
    catalog: Mapping,
    paper_domains: Mapping,
    root: Optional[Path] = None,
    paper_ids: Optional[set[str]] = None,
) -> List[str]:
    """Return deterministic errors for the reviewed project inventory."""

    errors: List[str] = []
    projects = catalog.get("projects")
    if not isinstance(projects, list):
        return ["project catalog.projects must be an array"]
    policy = catalog.get("selection_policy", {})
    minimum = policy.get("default_min_stars", 80)
    conditional = policy.get("conditional_min_stars", 60)
    if not isinstance(minimum, int) or minimum < 1:
        errors.append("selection_policy.default_min_stars must be positive")
        minimum = 80
    if not isinstance(conditional, int) or not 1 <= conditional <= minimum:
        errors.append("selection_policy.conditional_min_stars must be in [1, default]")
        conditional = 60

    seen_ids = set()
    seen_repos = set()
    topic_counts = defaultdict(Counter)
    for index, project in enumerate(projects):
        prefix = f"projects[{index}]"
        if not isinstance(project, dict):
            errors.append(f"{prefix} must be an object")
            continue
        project_id = project.get("project_id")
        if not isinstance(project_id, str) or not project_id.startswith("github:"):
            errors.append(f"{prefix}.project_id must use github:owner/repo")
            continue
        if project_id in seen_ids:
            errors.append(f"duplicate project_id: {project_id}")
        seen_ids.add(project_id)

        repo_url = project.get("repo_url", "")
        repo_key = _repo_key(repo_url)
        if not repo_key:
            errors.append(f"{project_id}: repo_url must be a GitHub repository root")
        elif project_id.lower() != f"github:{repo_key}":
            errors.append(f"{project_id}: project_id does not match repo_url")
        if repo_key in seen_repos:
            errors.append(f"duplicate repository: {repo_key}")
        seen_repos.add(repo_key)

        status = project.get("analysis_status")
        if status not in STATUS_VALUES:
            errors.append(f"{project_id}: invalid analysis_status")
        relation = project.get("relation")
        if relation not in RELATION_VALUES:
            errors.append(f"{project_id}: invalid relation")
        if relation == "project_only" and project.get("related_paper_ids"):
            errors.append(f"{project_id}: project_only cannot list related_paper_ids")
        if relation == "official_paper_code" and not project.get("related_paper_ids"):
            errors.append(f"{project_id}: official_paper_code needs related_paper_ids")
        if paper_ids is not None:
            missing_papers = set(project.get("related_paper_ids", [])) - paper_ids
            if missing_papers:
                errors.append(
                    f"{project_id}: related papers missing from catalog {sorted(missing_papers)}"
                )

        topics = project.get("topics")
        if not isinstance(topics, list) or not topics:
            errors.append(f"{project_id}: topics must be non-empty")
            topics = []
        for topic in topics:
            if topic not in paper_domains:
                errors.append(f"{project_id}: unknown topic {topic}")
            else:
                topic_counts[topic][status] += 1

        stars = project.get("stars")
        exception = project.get("selection_exception")
        if not isinstance(stars, int) or stars < 0:
            errors.append(f"{project_id}: stars must be a non-negative integer")
        elif stars < conditional:
            errors.append(f"{project_id}: stars below conditional floor {conditional}")
        elif stars < minimum:
            if not isinstance(exception, dict) or not exception.get("reason_zh"):
                errors.append(
                    f"{project_id}: {stars} stars needs a written selection_exception"
                )
            elif not project.get("related_paper_ids"):
                errors.append(
                    f"{project_id}: conditional-star exception needs paper evidence"
                )

        snapshot = project.get("star_snapshot_at")
        if not isinstance(snapshot, str) or not snapshot:
            errors.append(f"{project_id}: star_snapshot_at is required")
        if not project.get("default_branch") or not project.get("license"):
            errors.append(f"{project_id}: default_branch and license are required")
        if not project.get("selection_reason_zh"):
            errors.append(f"{project_id}: selection_reason_zh is required")

        if status == "deep_review":
            commit = project.get("reviewed_commit", "")
            if not re.fullmatch(r"[0-9a-f]{40}", str(commit)):
                errors.append(f"{project_id}: deep_review needs a 40-char commit")
            for language in ("zh", "en"):
                field = f"detail_path_{language}"
                value = project.get(field)
                if not value:
                    errors.append(f"{project_id}: deep_review needs {field}")
                elif root is not None and not (root / value).is_file():
                    errors.append(f"{project_id}: missing {value}")

    if root is not None:
        from .project_quality import evaluate_project_catalog_reviews

        for review in evaluate_project_catalog_reviews(catalog, root):
            errors.extend(f"{review.project_id}: {error}" for error in review.errors)

    return errors


def project_coverage_report(catalog: Mapping, paper_domains: Mapping) -> dict:
    projects = catalog.get("projects", [])
    domains = []
    for topic, config in paper_domains.items():
        selected = [project for project in projects if topic in project.get("topics", [])]
        domains.append({
            "domain": topic,
            "title_zh": config.get("title_zh", topic),
            "total": len(selected),
            "deep_review": sum(
                project.get("analysis_status") == "deep_review" for project in selected
            ),
            "project_only": sum(
                project.get("relation") == "project_only" for project in selected
            ),
        })
    return {
        "updated_at": catalog.get("updated_at"),
        "counts": Counter(project.get("analysis_status") for project in projects),
        "domains": domains,
    }


def _github_headers(token_env: str = "GITHUB_TOKEN") -> dict:
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "humanoid-wbc-handbook/0.3",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    token = os.environ.get(token_env, "").strip()
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers


def discover_github_projects(
    queries: Iterable[str],
    known_catalog: Mapping,
    min_stars: int = 80,
    max_results_per_query: int = 30,
    token_env: str = "GITHUB_TOKEN",
    fetcher: Optional[Callable[[str, Mapping[str, str]], bytes]] = None,
) -> List[dict]:
    """Search official GitHub repository records without accepting candidates."""

    if min_stars < 1:
        raise ValueError("min_stars must be positive")
    if not 1 <= max_results_per_query <= 100:
        raise ValueError("max_results_per_query must be in [1, 100]")
    normalized_queries = list(dict.fromkeys(str(item).strip() for item in queries))
    if not normalized_queries or any(not item for item in normalized_queries):
        raise ValueError("at least one non-empty query is required")
    known = {
        _repo_key(project.get("repo_url", ""))
        for project in known_catalog.get("projects", [])
    }
    known.discard("")
    if fetcher is None:
        def fetcher(url: str, headers: Mapping[str, str]) -> bytes:
            with urlopen(Request(url, headers=dict(headers)), timeout=45) as response:
                return response.read()

    merged = {}
    for query in normalized_queries:
        qualified = f"{query} stars:>={min_stars}"
        params = urlencode({
            "q": qualified,
            "sort": "stars",
            "order": "desc",
            "per_page": max_results_per_query,
        })
        payload = json.loads(fetcher(
            f"{GITHUB_SEARCH_API}?{params}", _github_headers(token_env)
        ).decode("utf-8"))
        for item in payload.get("items", []):
            repo_key = str(item.get("full_name", "")).lower()
            if not repo_key or repo_key in known or item.get("fork") or item.get("archived"):
                continue
            candidate = merged.setdefault(repo_key, {
                "project_id": f"github:{item['full_name']}",
                "name": item.get("name", ""),
                "repo_url": item.get("html_url", ""),
                "description": item.get("description") or "",
                "stars": int(item.get("stargazers_count", 0)),
                "forks": int(item.get("forks_count", 0)),
                "default_branch": item.get("default_branch", ""),
                "license": (item.get("license") or {}).get("spdx_id") or "NOASSERTION",
                "pushed_at": item.get("pushed_at", ""),
                "matched_queries": [],
            })
            candidate["matched_queries"].append(query)
    return sorted(
        merged.values(),
        key=lambda item: (-item["stars"], item["project_id"].lower()),
    )


def write_project_candidate_run(path: Path, candidates: Iterable[Mapping]) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "mode": "manual_on_demand",
        "source": "github_official_search_api",
        "auto_accepted": False,
        "candidates": list(candidates),
    }
    path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return path
