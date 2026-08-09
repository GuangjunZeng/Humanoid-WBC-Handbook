#!/usr/bin/env python3
"""Deterministically verify the frozen paper corpus without network access."""

from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
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
    registry = load_json(REGISTRY)
    papers = registry.get("papers", [])

    if len(papers) != 14:
        errors.append(f"registry must contain 14 papers, found {len(papers)}")
    if any(paper.get("status") != "complete" for paper in papers):
        errors.append("every registry entry must be complete")

    paper_domains = Counter(paper.get("primary_domain") for paper in papers)
    expected_domains = Counter({domain: 2 for domain in DOMAINS})
    if paper_domains != expected_domains:
        errors.append(f"registry domain counts differ: {dict(paper_domains)}")

    for paper in papers:
        brief = ROOT / paper.get("brief_path", "")
        if not brief.is_file():
            errors.append(f"missing brief: {brief.relative_to(ROOT)}")
            continue
        text = brief.read_text(encoding="utf-8")
        if len(re.findall(r"Figure|Figures|Table|Tables|Equation|Equations|Fig\.", text)) < 3:
            errors.append(f"brief needs at least three figure/table/equation locators: {brief.name}")
        if not re.search(r"代码|实现", text):
            errors.append(f"brief lacks implementation/code status: {brief.name}")
        if not re.search(r"局限|边界", text):
            errors.append(f"brief lacks limitations/boundary section: {brief.name}")

    for filename in DOMAINS.values():
        path = ROOT / "content" / "papers" / "domains" / filename
        if not path.is_file():
            errors.append(f"missing domain index: {filename}")

    source_records = [load_json(path) for path in sorted(SOURCES.glob("*.json"))]
    paper_sources = [source for source in source_records if source.get("kind") == "paper"]
    if len(paper_sources) != 14:
        errors.append(f"expected 14 paper source records, found {len(paper_sources)}")
    source_titles = Counter(source.get("title") for source in paper_sources)
    for paper in papers:
        if source_titles[paper.get("title")] != 1:
            errors.append(f"paper title does not map to exactly one paper source: {paper.get('title')}")

    claims = [load_json(path) for path in sorted(CLAIMS.glob("*.json"))]
    if len(claims) != 14:
        errors.append(f"expected 14 claims, found {len(claims)}")
    claim_domains = Counter(claim.get("domain") for claim in claims)
    if claim_domains != expected_domains:
        errors.append(f"claim domain counts differ: {dict(claim_domains)}")
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

    print("corpus ok: 14 papers, 7 domains, 14 briefs, 28 sources, 14 claims")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
