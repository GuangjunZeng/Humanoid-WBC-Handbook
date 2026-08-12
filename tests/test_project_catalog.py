from __future__ import annotations

import json
from pathlib import Path
import tempfile
import unittest
from urllib.parse import parse_qs, urlparse

from wbc_handbook.paper_catalog import load_json
from wbc_handbook.project_catalog import (
    discover_github_projects,
    project_coverage_report,
    validate_project_catalog,
    write_project_candidate_run,
)


PROJECT_ROOT = Path(__file__).resolve().parents[1]


class ProjectCatalogTests(unittest.TestCase):
    def setUp(self):
        self.paper_catalog = load_json(
            PROJECT_ROOT / "content" / "papers" / "catalog.json"
        )
        self.project_catalog_path = (
            PROJECT_ROOT / "content" / "papers" / "project-catalog.json"
        )

    def test_repository_project_catalog_is_consistent(self):
        catalog = load_json(self.project_catalog_path)
        self.assertEqual(
            validate_project_catalog(
                catalog,
                self.paper_catalog["domains"],
                root=PROJECT_ROOT,
                paper_ids={paper["paper_id"] for paper in self.paper_catalog["papers"]},
                paper_records=self.paper_catalog["papers"],
            ),
            [],
        )
        report = project_coverage_report(catalog, self.paper_catalog["domains"])
        self.assertEqual(
            {row["domain"] for row in report["domains"]},
            set(self.paper_catalog["domains"]),
        )
        self.assertTrue(all(row["total"] > 0 for row in report["domains"]))

    def test_star_floor_requires_a_paper_backed_exception(self):
        catalog = {
            "selection_policy": {
                "default_min_stars": 80,
                "conditional_min_stars": 60,
            },
            "projects": [{
                "project_id": "github:owner/repo",
                "name": "repo",
                "repo_url": "https://github.com/owner/repo",
                "topics": ["locomotion_terrain"],
                "relation": "project_only",
                "related_paper_ids": [],
                "analysis_status": "queued",
                "stars": 70,
                "star_snapshot_at": "2026-08-12",
                "default_branch": "main",
                "license": "MIT",
                "selection_reason_zh": "test",
            }],
        }
        errors = validate_project_catalog(catalog, self.paper_catalog["domains"])
        self.assertTrue(any("selection_exception" in error for error in errors))

    def test_official_project_repository_must_match_paper_code(self):
        catalog = {
            "selection_policy": {
                "default_min_stars": 80,
                "conditional_min_stars": 60,
            },
            "projects": [{
                "project_id": "github:owner/wrong-repo",
                "name": "wrong-repo",
                "repo_url": "https://github.com/owner/wrong-repo",
                "topics": ["locomotion_terrain"],
                "relation": "official_paper_code",
                "related_paper_ids": ["arxiv:test"],
                "analysis_status": "queued",
                "stars": 100,
                "star_snapshot_at": "2026-08-12",
                "default_branch": "main",
                "license": "MIT",
                "selection_reason_zh": "test",
            }],
        }
        paper_records = [{
            "paper_id": "arxiv:test",
            "code": {
                "status": "verified_official",
                "url": "https://github.com/owner/canonical-repo",
            },
        }]
        errors = validate_project_catalog(
            catalog,
            self.paper_catalog["domains"],
            paper_ids={"arxiv:test"},
            paper_records=paper_records,
        )
        self.assertTrue(any("does not match official code" in error for error in errors))

    def test_discovery_uses_official_records_and_never_auto_accepts(self):
        observed = []

        def fetcher(url, headers):
            observed.append((url, headers))
            return json.dumps({"items": [{
                "full_name": "Owner/NewRepo",
                "name": "NewRepo",
                "html_url": "https://github.com/Owner/NewRepo",
                "description": "humanoid whole-body control",
                "stargazers_count": 123,
                "forks_count": 7,
                "default_branch": "main",
                "license": {"spdx_id": "MIT"},
                "pushed_at": "2026-08-01T00:00:00Z",
                "fork": False,
                "archived": False,
            }]}) .encode("utf-8")

        candidates = discover_github_projects(
            ["humanoid whole-body control"],
            {"projects": []},
            fetcher=fetcher,
        )
        self.assertEqual(candidates[0]["project_id"], "github:Owner/NewRepo")
        query = parse_qs(urlparse(observed[0][0]).query)["q"][0]
        self.assertIn("stars:>=80", query)
        with tempfile.TemporaryDirectory() as tmp:
            path = write_project_candidate_run(
                Path(tmp) / "candidates.json", candidates
            )
            payload = json.loads(path.read_text(encoding="utf-8"))
        self.assertFalse(payload["auto_accepted"])
        self.assertEqual(payload["source"], "github_official_search_api")

    def test_rejected_aggregation_identifiers_cannot_enter_catalogs(self):
        audit = load_json(
            PROJECT_ROOT / "content" / "papers" / "discovery-audit.json"
        )
        corrections = audit["identifier_corrections"]
        rejected_ids = {item["rejected_paper_id"] for item in corrections}
        accepted_ids = {item["accepted_paper_id"] for item in corrections}
        paper_ids = {paper["paper_id"] for paper in self.paper_catalog["papers"]}
        project_paper_ids = {
            paper_id
            for project in load_json(self.project_catalog_path)["projects"]
            for paper_id in project.get("related_paper_ids", [])
        }
        self.assertTrue(accepted_ids <= paper_ids)
        self.assertTrue(accepted_ids <= project_paper_ids)
        self.assertTrue(rejected_ids.isdisjoint(paper_ids))
        self.assertTrue(rejected_ids.isdisjoint(project_paper_ids))
        self.assertTrue(all(
            item["decision"] == "rejected_identifier_corrected"
            and item["rejected_primary_url"].endswith(
                item["rejected_paper_id"].removeprefix("arxiv:")
            )
            and item["accepted_primary_url"].endswith(
                item["accepted_paper_id"].removeprefix("arxiv:")
            )
            for item in corrections
        ))
        selected_project_ids = {
            project["project_id"] for project in load_json(self.project_catalog_path)["projects"]
        }
        project_rejections = audit["project_rejections"]
        self.assertTrue(all(
            item["project_id"] not in selected_project_ids
            and item["stars_at_review"] < 60
            and item["decision"] == "rejected_below_conditional_star_floor"
            for item in project_rejections
        ))


if __name__ == "__main__":
    unittest.main()
