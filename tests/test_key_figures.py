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

    def test_all_deep_reads_have_three_to_five_audited_crops(self):
        self.assertEqual(self.spec["schema_version"], 2)
        self.assertEqual(len(self.spec["papers"]), 38)
        for paper in self.spec["papers"]:
            self.assertGreaterEqual(len(paper["figures"]), 3)
            self.assertLessEqual(len(paper["figures"]), 5)
            self.assertEqual(key_figures.validate_paper_spec(paper), [])
            self.assertEqual(key_figures.check_paper(paper), [])
            for figure in paper["figures"]:
                for region in figure["regions"]:
                    self.assertGreaterEqual(len(region["visual_review_note"].strip()), 12)
                    self.assertIn("本体完整", region["visual_review_note"])
                    self.assertIn("无无关正文", region["visual_review_note"])

    def test_manual_caption_bbox_is_inside_crop_and_part_of_review_fingerprint(self):
        paper = next(
            paper for paper in self.spec["papers"]
            if paper["slug"] == "frasa-2410.08655v3"
        )
        region = paper["figures"][1]["regions"][1]
        self.assertIn("caption_bbox", region)
        crop = region["crop"]
        caption_bbox = region["caption_bbox"]
        self.assertGreaterEqual(caption_bbox[0], crop[0])
        self.assertGreaterEqual(caption_bbox[1], crop[1])
        self.assertLessEqual(caption_bbox[2], crop[2])
        self.assertLessEqual(caption_bbox[3], crop[3])
        canonical = key_figures.canonical_region(region)
        self.assertEqual(canonical["caption_bbox"], caption_bbox)

    def test_agile_soccer_keeps_five_reviewed_figures(self):
        paper = next(
            paper for paper in self.spec["papers"]
            if paper["paper_id"] == "arxiv:2304.13653v2"
        )
        self.assertEqual(
            [figure["file"] for figure in paper["figures"]],
            [
                "figure-2-training.jpg",
                "table-1-hardware.jpg",
                "figure-7-ablation.jpg",
                "figure-5-behavior.jpg",
                "figure-s3-table-s5-compute.jpg",
            ],
        )

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
