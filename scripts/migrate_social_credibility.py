#!/usr/bin/env python3
"""Idempotently add problem identity and credibility to reviewed social cards."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from wbc_handbook.social_credibility import normalize_card_credibility  # noqa: E402


def migrate(data_dir: Path) -> dict[str, int]:
    files_changed = 0
    cards_seen = 0
    cards_changed = 0
    for path in sorted((data_dir / "sources").glob("*.json")):
        payload = json.loads(path.read_text(encoding="utf-8"))
        metadata = payload.get("metadata", {})
        cards = metadata.get("engineering_qa")
        if not isinstance(cards, list):
            continue
        normalized_cards = []
        for card in cards:
            cards_seen += 1
            normalized = normalize_card_credibility(
                card,
                scope_id=str(metadata.get("scope_id", "unclassified")),
                source_id=str(payload.get("source_id", path.stem)),
                components=metadata.get("components", []),
                engineering_details=metadata.get("engineering_details", {}),
                media_summaries=metadata.get("media_summaries", []),
            )
            normalized_cards.append(normalized)
            cards_changed += normalized != card
        if normalized_cards != cards:
            metadata["engineering_qa"] = normalized_cards
            path.write_text(
                json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
            )
            files_changed += 1
    return {
        "files_changed": files_changed,
        "cards_seen": cards_seen,
        "cards_changed": cards_changed,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-dir", default=str(PROJECT_ROOT / "data"))
    args = parser.parse_args()
    print(json.dumps(migrate(Path(args.data_dir)), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
