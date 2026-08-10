from __future__ import annotations

import json
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


if __name__ == "__main__":
    unittest.main()
