from __future__ import annotations

import json
from pathlib import Path
import re
import unittest

from wbc_handbook.paper_localization import (
    REQUIRED_HEADINGS,
    load_translations,
    render_paper_translations,
    representative_papers,
)


PROJECT_ROOT = Path(__file__).resolve().parents[1]


class PaperLocalizationTests(unittest.TestCase):
    def setUp(self):
        self.catalog = json.loads(
            (PROJECT_ROOT / "content" / "papers" / "catalog.json").read_text(encoding="utf-8")
        )
        self.registry = json.loads(
            (PROJECT_ROOT / "content" / "papers" / "registry.json").read_text(encoding="utf-8")
        )
        self.slugs = {paper["paper_id"]: paper["slug"] for paper in self.registry["papers"]}

    def test_all_representative_papers_have_current_english_pages(self):
        report = render_paper_translations(PROJECT_ROOT, check=True)
        self.assertEqual(report["papers"], 25)
        self.assertEqual(report["stale"], [])

    def test_english_pages_have_required_structure_and_bilingual_links(self):
        translations = load_translations(PROJECT_ROOT)
        for paper in representative_papers(self.catalog):
            source_path = PROJECT_ROOT / paper["brief_path"]
            target_path = PROJECT_ROOT / "content" / "papers" / "en" / source_path.name
            source = source_path.read_text(encoding="utf-8")
            target = target_path.read_text(encoding="utf-8")
            self.assertIn(f"[English version](en/{source_path.name})", source)
            self.assertIn(f"[中文版](../{source_path.name})", target)
            for heading in REQUIRED_HEADINGS:
                self.assertIn(f"## {heading}", target)
            self.assertEqual(target.count("!["), 3)
            self.assertIn(paper["paper_id"], translations)

            slug = self.slugs[paper["paper_id"]]
            manifest = json.loads(
                (
                    PROJECT_ROOT / "content" / "papers" / "assets" / slug / "manifest.json"
                ).read_text(encoding="utf-8")
            )
            expected_assets = {entry["asset"] for entry in manifest["figures"]}
            chinese_assets = {
                Path(path).name
                for path in re.findall(r"!\[[^\]]*\]\(([^)]+)\)", source)
            }
            english_assets = {
                Path(path).name
                for path in re.findall(r"!\[[^\]]*\]\(([^)]+)\)", target)
            }
            self.assertEqual(chinese_assets, expected_assets)
            self.assertEqual(english_assets, expected_assets)


if __name__ == "__main__":
    unittest.main()
