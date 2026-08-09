from __future__ import annotations

from contextlib import redirect_stderr, redirect_stdout
import io
import json
from pathlib import Path
import uuid
import unittest

from wbc_handbook.cli import main


PROJECT_ROOT = Path(__file__).resolve().parents[1]


class CliTests(unittest.TestCase):
    def test_empty_repository_validates(self):
        data_dir = PROJECT_ROOT / "var" / "test-runs" / str(uuid.uuid4()) / "data"
        output = io.StringIO()
        with redirect_stdout(output):
            exit_code = main(["validate", "--data-dir", str(data_dir)])
        report = json.loads(output.getvalue())
        self.assertEqual(exit_code, 0)
        self.assertTrue(report["ok"])
        self.assertEqual(report["counts"]["sources"], 0)

    def test_missing_index_fails_with_diagnostic(self):
        index_path = PROJECT_ROOT / "var" / "test-runs" / str(uuid.uuid4()) / "missing.sqlite"
        output = io.StringIO()
        with redirect_stderr(output):
            exit_code = main(["query", "test question", "--index", str(index_path)])
        self.assertEqual(exit_code, 2)
        self.assertIn("query failed", output.getvalue())


if __name__ == "__main__":
    unittest.main()
