from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import unittest


PROJECT_ROOT = Path(__file__).resolve().parents[1]
MODULE_SPEC = importlib.util.spec_from_file_location(
    "extract_key_figures", PROJECT_ROOT / "scripts" / "extract_key_figures.py"
)
assert MODULE_SPEC and MODULE_SPEC.loader
key_figures = importlib.util.module_from_spec(MODULE_SPEC)
MODULE_SPEC.loader.exec_module(key_figures)


class KeyFigureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.spec = json.loads(
            (PROJECT_ROOT / "research" / "key-figures.json").read_text(encoding="utf-8")
        )

    def test_all_deep_reads_have_three_audited_crops(self):
        self.assertEqual(self.spec["schema_version"], 2)
        self.assertEqual(len(self.spec["papers"]), 25)
        self.assertEqual(sum(len(paper["figures"]) for paper in self.spec["papers"]), 75)
        for paper in self.spec["papers"]:
            self.assertEqual(key_figures.validate_paper_spec(paper), [])
            self.assertEqual(key_figures.check_paper(paper), [])

    def test_full_page_or_stale_review_is_rejected(self):
        paper = json.loads(json.dumps(self.spec["papers"][0]))
        figure = paper["figures"][0]
        figure["regions"][0]["crop"] = [0.0, 0.0, 1.0, 1.0]
        errors = key_figures.validate_paper_spec(paper)
        self.assertTrue(any("retains too much" in error for error in errors))

        paper = json.loads(json.dumps(self.spec["papers"][0]))
        paper["figures"][0]["review"]["fingerprint"] = "0" * 64
        errors = key_figures.check_paper(paper)
        self.assertTrue(any("stale visual-review fingerprint" in error for error in errors))

    def test_ci_runs_key_figure_gate_without_auto_approval(self):
        for name in ("ci.yml", "pages.yml"):
            workflow = (
                PROJECT_ROOT / ".github" / "workflows" / name
            ).read_text(encoding="utf-8")
            self.assertIn("scripts/extract_key_figures.py --check", workflow)
            self.assertNotIn("--record-visual-review", workflow)


if __name__ == "__main__":
    unittest.main()
