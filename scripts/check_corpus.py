#!/usr/bin/env python3
"""Deterministically verify the paper catalog and deep-read corpus offline."""

from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from wbc_handbook.paper_catalog import validate_catalog  # noqa: E402
from wbc_handbook.paper_quality import (  # noqa: E402
    evaluate_registry,
    evaluate_registry_english,
)


CATALOG = ROOT / "content" / "papers" / "catalog.json"
REGISTRY = ROOT / "content" / "papers" / "registry.json"
SOURCES = ROOT / "data" / "sources"
CLAIMS = ROOT / "data" / "claims"
DOMAINS = {
    "training_data_retargeting": "training-data-retargeting.md",
    "universal_tracking_teleoperation": "universal-tracking-teleoperation.md",
    "locomotion_terrain": "locomotion-terrain.md",
    "loco_manipulation_wbc": "loco-manipulation-wbc.md",
    "sports": "sports-athletic-skills.md",
    "motion_generation": "motion-generation.md",
    "recovery_safety_force": "recovery-safety-force.md",
}


def load_json(path: Path):
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def main() -> int:
    errors: list[str] = []
    catalog = load_json(CATALOG)
    registry = load_json(REGISTRY)
    papers = registry.get("papers", [])
    catalog_papers = catalog.get("papers", [])

    errors.extend(validate_catalog(catalog, registry))
    if not papers:
        errors.append("registry must contain at least one deep-read paper")
    if any(paper.get("status") != "complete" for paper in papers):
        errors.append("every registry entry must be complete")

    paper_domains = Counter(paper.get("primary_domain") for paper in papers)
    unknown_domains = set(paper_domains) - set(DOMAINS)
    if unknown_domains:
        errors.append(f"registry contains unknown primary domains: {sorted(unknown_domains)}")
    empty_domains = [domain for domain in DOMAINS if not paper_domains[domain]]
    if empty_domains:
        errors.append(f"registry domains need at least one deep read: {empty_domains}")

    for result in evaluate_registry(ROOT, catalog, registry):
        for error in result.errors:
            errors.append(f"{result.slug}: {error}")
    for result in evaluate_registry_english(ROOT, catalog, registry):
        for error in result.errors:
            errors.append(f"{result.slug} [en]: {error}")

    domain_root = ROOT / "content" / "papers" / "domains"
    paper_readme = (ROOT / "content" / "papers" / "README.md").read_text(
        encoding="utf-8"
    )
    for domain, filename in DOMAINS.items():
        path = domain_root / filename
        if not path.is_file():
            errors.append(f"missing domain index: {filename}")
            continue
        text = path.read_text(encoding="utf-8")
        if "<!-- BEGIN GENERATED PAPER CATALOG -->" not in text:
            errors.append(f"domain index lacks generated catalog section: {filename}")
        for paper in catalog_papers:
            if domain in paper.get("topics", []) and paper.get("title") not in text:
                errors.append(f"domain index omits catalog paper {paper.get('paper_id')}: {filename}")
        selected = [
            paper for paper in catalog_papers if domain in paper.get("topics", [])
        ]
        expected_readme_row = (
            f"| [{catalog['domains'][domain]['title_zh']}](domains/{filename}) | "
            f"{len(selected)} | "
            f"{sum(paper.get('analysis_status') == 'deep_read' for paper in selected)} | "
            f"{sum(paper.get('analysis_status') == 'queued' for paper in selected)} | "
            f"{sum(paper.get('code', {}).get('status') == 'verified_official' for paper in selected)} |"
        )
        if expected_readme_row not in paper_readme:
            errors.append(f"paper README has stale coverage row: {domain}")

    source_records = [load_json(path) for path in sorted(SOURCES.glob("*.json"))]
    paper_sources = [source for source in source_records if source.get("kind") == "paper"]
    if len(paper_sources) != len(papers):
        errors.append(
            f"expected one paper source per deep read ({len(papers)}), found {len(paper_sources)}"
        )
    source_titles = Counter(source.get("title") for source in paper_sources)
    for paper in papers:
        if source_titles[paper.get("title")] != 1:
            errors.append(f"paper title does not map to exactly one paper source: {paper.get('title')}")

    claims = [load_json(path) for path in sorted(CLAIMS.glob("*.json"))]
    if len(claims) != len(papers):
        errors.append(f"expected one claim per deep read ({len(papers)}), found {len(claims)}")
    claim_domains = Counter(claim.get("domain") for claim in claims)
    if claim_domains != paper_domains:
        errors.append(
            "claim primary-domain counts must match the deep-read registry: "
            f"claims={dict(claim_domains)}, papers={dict(paper_domains)}"
        )
    for claim in claims:
        evidence = claim.get("evidence", [])
        if not any(item.get("source_id", "").startswith("paper.") for item in evidence):
            errors.append(f"claim lacks paper evidence: {claim.get('claim_id')}")
        if claim.get("safety_level") == "hardware_critical" and not claim.get("safety_case"):
            errors.append(f"hardware-critical claim lacks safety case: {claim.get('claim_id')}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    queued = sum(paper.get("analysis_status") == "queued" for paper in catalog_papers)
    print(
        "corpus ok: "
        f"{len(catalog_papers)} catalog papers, {len(papers)} deep reads, {queued} queued, "
        f"{len(DOMAINS)} domains, {len(source_records)} sources, {len(claims)} claims"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
