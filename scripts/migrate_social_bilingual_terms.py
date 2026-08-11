#!/usr/bin/env python3
"""Backfill and check Chinese-first bilingual terminology on community Q&A cards."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys
from typing import Any, Dict, Iterable, List

from wbc_handbook.importer import normalize_manual_source
from wbc_handbook.language import infer_bilingual_terms, normalize_bilingual_terms


def _context(record: Dict[str, Any]) -> str:
    metadata = record.get("metadata", {})
    details = metadata.get("engineering_details", {})
    detail_items: List[str] = []
    if isinstance(details, dict):
        for values in details.values():
            if isinstance(values, list):
                detail_items.extend(str(value) for value in values)
    components = metadata.get("components", [])
    robots = metadata.get("robot_platforms", [])
    return " ".join([
        str(record.get("title", "")),
        str(record.get("summary", "")),
        str(metadata.get("wbc_relevance_reason", "")),
        *(str(value) for value in components if isinstance(components, list)),
        *(str(value) for value in robots if isinstance(robots, list)),
        *detail_items,
    ])


def migrate_record(record: Dict[str, Any]) -> int:
    """Return the number of Q&A cards changed in one source record."""

    if record.get("kind") != "community":
        return 0
    metadata = record.get("metadata")
    if not isinstance(metadata, dict):
        raise ValueError(f"{record.get('source_id')}: metadata must be an object")
    cards = metadata.get("engineering_qa")
    if not isinstance(cards, list):
        raise ValueError(f"{record.get('source_id')}: engineering_qa must be a list")
    context = _context(record)
    changed = 0
    for index, card in enumerate(cards):
        if not isinstance(card, dict):
            raise ValueError(
                f"{record.get('source_id')}#qa-{index + 1}: card must be an object"
            )
        existing = card.get("bilingual_terms")
        if existing is None:
            terms = infer_bilingual_terms(
                " ".join((
                    str(card.get("question_zh", "")),
                    str(card.get("answer_zh", "")),
                    context,
                ))
            )
            if not terms:
                raise ValueError(
                    f"{record.get('source_id')}#qa-{index + 1}: "
                    "cannot infer bilingual terms; add them manually"
                )
            card["bilingual_terms"] = terms
            changed += 1
        else:
            try:
                card["bilingual_terms"] = normalize_bilingual_terms(existing)
            except ValueError:
                terms = infer_bilingual_terms(
                    " ".join((
                        str(card.get("question_zh", "")),
                        str(card.get("answer_zh", "")),
                        context,
                    ))
                )
                if not terms:
                    raise
                card["bilingual_terms"] = terms
                changed += 1
    return changed


def community_files(data_dir: Path) -> Iterable[Path]:
    return sorted((data_dir / "sources").glob("community.*.json"))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-dir", default="data")
    parser.add_argument(
        "--write", action="store_true",
        help="write inferred terms and recompute source digests",
    )
    args = parser.parse_args()
    files = list(community_files(Path(args.data_dir)))
    changed_files = 0
    changed_cards = 0
    errors: List[str] = []
    for path in files:
        try:
            record = json.loads(path.read_text(encoding="utf-8"))
            changed = migrate_record(record)
            if changed:
                changed_files += 1
                changed_cards += changed
                if args.write:
                    normalized = normalize_manual_source(record).to_dict()
                    temporary = path.with_suffix(path.suffix + ".tmp")
                    temporary.write_text(
                        json.dumps(
                            normalized, ensure_ascii=False, indent=2, sort_keys=True
                        ) + "\n",
                        encoding="utf-8",
                    )
                    temporary.replace(path)
        except (OSError, ValueError, json.JSONDecodeError) as exc:
            errors.append(f"{path}: {exc}")
    report = {
        "ok": not errors and (args.write or changed_cards == 0),
        "mode": "write" if args.write else "check",
        "community_sources": len(files),
        "changed_files": changed_files,
        "changed_cards": changed_cards,
        "errors": errors,
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["ok"] else 2


if __name__ == "__main__":
    sys.exit(main())
