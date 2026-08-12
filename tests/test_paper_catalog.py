from __future__ import annotations

import json
from copy import deepcopy
from pathlib import Path
import tempfile
import unittest

from wbc_handbook.paper_catalog import (
    coverage_report,
    discover_candidates,
    load_json,
    validate_catalog,
    write_candidate_run,
)


PROJECT_ROOT = Path(__file__).resolve().parents[1]


class PaperCatalogTests(unittest.TestCase):
    def setUp(self):
        self.catalog = load_json(PROJECT_ROOT / "content" / "papers" / "catalog.json")
        self.registry = load_json(PROJECT_ROOT / "content" / "papers" / "registry.json")

    def test_repository_catalog_is_consistent(self):
        self.assertEqual(validate_catalog(self.catalog, self.registry), [])
        report = coverage_report(self.catalog)
        self.assertEqual(
            report["counts"]["deep_read"], len(self.registry.get("papers", []))
        )
        self.assertGreater(report["counts"]["queued"], 0)
        self.assertGreater(
            len(self.catalog.get("papers", [])), len(self.registry.get("papers", []))
        )
        self.assertTrue(all(not row["missing_roles"] for row in report["domains"]))

    def test_discovery_deduplicates_known_arxiv_versions(self):
        feed = b'''<?xml version="1.0" encoding="UTF-8"?>
        <feed xmlns="http://www.w3.org/2005/Atom">
          <entry><id>http://arxiv.org/abs/2404.05695v9</id><updated>2026-01-02T00:00:00Z</updated>
            <published>2024-04-01T00:00:00Z</published><title>Known humanoid locomotion</title>
            <summary>humanoid walking</summary><author><name>A</name></author></entry>
          <entry><id>http://arxiv.org/abs/2608.01234v1</id><updated>2026-08-02T00:00:00Z</updated>
            <published>2026-08-01T00:00:00Z</published><title>New humanoid whole-body control</title>
            <summary>humanoid locomotion tracking and recovery</summary><author><name>B</name></author></entry>
        </feed>'''
        candidates = discover_candidates(self.catalog, 2, fetcher=lambda _: feed)
        self.assertEqual([item["paper_id"] for item in candidates], ["arxiv:2608.01234"])
        self.assertGreater(len(candidates[0]["proposed_topics"]), 1)

    def test_catalog_rejects_same_work_under_two_identifiers(self):
        duplicate = deepcopy(self.catalog["papers"][0])
        duplicate["paper_id"] = "openreview:duplicate-work"
        duplicate["analysis_status"] = "queued"
        duplicate.pop("brief_path", None)
        duplicate.pop("brief_path_en", None)
        catalog = deepcopy(self.catalog)
        catalog["papers"].append(duplicate)
        errors = validate_catalog(catalog)
        self.assertTrue(
            any("duplicate paper title across identifiers" in error for error in errors)
        )

    def test_candidate_run_is_explicitly_not_auto_accepted(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = write_candidate_run(Path(tmp) / "candidates.json", [{"paper_id": "x"}])
            payload = json.loads(target.read_text(encoding="utf-8"))
        self.assertEqual(payload["mode"], "manual_on_demand")
        self.assertFalse(payload["auto_accepted"])

    def test_discovery_can_be_limited_to_one_topic(self):
        feed = b'''<?xml version="1.0" encoding="UTF-8"?>
        <feed xmlns="http://www.w3.org/2005/Atom">
          <entry><id>http://arxiv.org/abs/2608.54321v1</id><updated>2026-08-03T00:00:00Z</updated>
            <published>2026-08-03T00:00:00Z</published><title>Humanoid motion generation</title>
            <summary>humanoid motion diffusion control</summary><author><name>A</name></author></entry>
        </feed>'''
        candidates = discover_candidates(
            self.catalog,
            2,
            fetcher=lambda _: feed,
            topics=["motion_generation"],
        )
        self.assertEqual(candidates[0]["proposed_topics"], ["motion_generation"])

    def test_discovery_rejects_unknown_topic(self):
        with self.assertRaisesRegex(ValueError, "unknown topics"):
            discover_candidates(
                self.catalog,
                fetcher=lambda _: b"<feed />",
                topics=["not_a_topic"],
            )


if __name__ == "__main__":
    unittest.main()
