#!/usr/bin/env python3
"""Check every deep-read paper against the local paper-daily analysis standard."""

from __future__ import annotations

import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from wbc_handbook.paper_quality import (  # noqa: E402
    evaluate_registry,
    evaluate_registry_english,
)


def main() -> int:
    catalog = json.loads((ROOT / "content" / "papers" / "catalog.json").read_text(encoding="utf-8"))
    registry = json.loads((ROOT / "content" / "papers" / "registry.json").read_text(encoding="utf-8"))
    results = [
        *evaluate_registry(ROOT, catalog, registry),
        *evaluate_registry_english(ROOT, catalog, registry),
    ]
    failed = [result for result in results if not result.ok]
    print(json.dumps({
        "ok": not failed,
        "deep_read_papers": len(registry.get("papers", [])),
        "pages_checked": len(results),
        "failed": len(failed),
        "results": [result.to_dict() for result in results],
    }, ensure_ascii=False, indent=2))
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
