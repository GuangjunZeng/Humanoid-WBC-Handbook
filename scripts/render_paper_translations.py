#!/usr/bin/env python3
"""Render or check reviewed English paper pages."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from wbc_handbook.paper_localization import (  # noqa: E402
    PaperLocalizationError,
    render_paper_translations,
)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    try:
        report = render_paper_translations(ROOT, check=args.check)
    except (OSError, json.JSONDecodeError, PaperLocalizationError) as exc:
        print(f"paper localization failed: {exc}", file=sys.stderr)
        return 1
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
