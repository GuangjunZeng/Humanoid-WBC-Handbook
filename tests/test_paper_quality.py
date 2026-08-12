from __future__ import annotations

import json
import inspect
from pathlib import Path
import tempfile
import unittest

from wbc_handbook.paper_quality import evaluate_brief


class PaperQualityTests(unittest.TestCase):
    def test_thin_english_first_brief_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            result = evaluate_brief("thin", "# English brief\n\nOnly an abstract.", Path(tmp), "unknown")
        self.assertFalse(result.ok)
        self.assertIn("Chinese must be the main language (ratio < 0.60)", result.errors)
        self.assertIn("fewer than 3 embedded key figures", result.errors)

    def test_manifest_assets_must_all_be_embedded(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            asset_dir = root / "paper"
            asset_dir.mkdir()
            for name in ("a.jpg", "b.jpg", "c.jpg"):
                (asset_dir / name).write_bytes(b"x")
            (asset_dir / "manifest.json").write_text(json.dumps({
                "figures": [{"asset": "a.jpg"}, {"asset": "b.jpg"}, {"asset": "c.jpg"}]
            }), encoding="utf-8")
            text = "## 关键图解\n\n![a](assets/paper/a.jpg)"
            result = evaluate_brief("paper", text, root, "not_public", minimum_cjk=0)
        self.assertTrue(any("manifest figures not embedded" in error for error in result.errors))

    def test_quality_gate_does_not_require_filler_quotas(self):
        source = Path(__file__).parents[1] / "src" / "wbc_handbook" / "paper_quality.py"
        text = source.read_text(encoding="utf-8")
        default = inspect.signature(evaluate_brief).parameters["minimum_cjk"].default
        self.assertIsNone(default)
        self.assertNotIn("evidence-bearing prose paragraphs", text)
        self.assertNotIn("fewer than 2 explanatory analogies", text)

    def test_project_template_demands_pinned_repository_facts(self):
        template = (
            Path(__file__).parents[1] / "templates" / "project-brief.md"
        ).read_text(encoding="utf-8")
        for required in ("官方仓库固定提交", "核心调用链", "论文—代码映射", "静态核验，未运行", "永久链接"):
            self.assertIn(required, template)
        self.assertIn("删除目录罗列", template)

    def test_bans_promotional_ai_filler(self):
        with tempfile.TemporaryDirectory() as tmp:
            result = evaluate_brief(
                "filler",
                "具有重要意义。进一步研究将深入探讨。**金句**这就像打个比方类比成故事，很像：像脚手架。",
                Path(tmp),
                "unknown",
                minimum_cjk=0,
            )
        self.assertIn("banned generic phrase: 具有重要意义", result.errors)
        self.assertIn("banned generic phrase: 进一步研究", result.errors)
        self.assertIn("banned generic phrase: 深入探讨", result.errors)
        self.assertIn("banned generic phrase: **金句**", result.errors)
        self.assertIn("banned generic phrase: 这就像", result.errors)
        self.assertIn("banned generic phrase: 打个比方", result.errors)
        self.assertIn("banned generic phrase: 类比成", result.errors)
        self.assertIn("banned generic phrase: 很像：", result.errors)
        self.assertIn("banned generic phrase: 像脚手架", result.errors)


if __name__ == "__main__":
    unittest.main()
