from datetime import datetime, timezone
import json
from types import SimpleNamespace
import unittest

from wbc_handbook.social_inventory import (
    SocialInventoryError,
    build_social_candidate_inventory,
    render_pending_markdown,
)


NOW = datetime(2026, 8, 10, 12, tzinfo=timezone.utc)


class SocialInventoryTests(unittest.TestCase):
    def test_inventory_deduplicates_and_stores_only_minimal_fields(self):
        candidates = [
            {
                "platform": "x",
                "canonical_url": "https://x.com/robot/status/1?utm_source=test",
                "title": "QP solver debugging",
                "scope_id": "optimization_ik_qp_mpc",
                "query": "WBC QP",
                "body_text": "large raw body that must not be committed",
                "selected_comments": [{"text": "raw comment"}],
                "media": [{"url": "https://temporary.invalid/secret"}],
                "cookie": "never-store-me",
            },
            {
                "platform": "x",
                "canonical_url": "https://twitter.com/robot/status/1/photo/1",
                "title": "duplicate",
                "scope_id": "solver_numerics",
                "query": "OSQP failure",
            },
        ]
        inventory = build_social_candidate_inventory(
            [candidates], generated_at=NOW
        )
        self.assertEqual(inventory["stats"]["unique_candidates"], 1)
        self.assertEqual(inventory["stats"]["duplicates_merged"], 1)
        stored = json.dumps(inventory, ensure_ascii=False)
        self.assertNotIn("large raw body", stored)
        self.assertNotIn("raw comment", stored)
        self.assertNotIn("never-store-me", stored)
        self.assertNotIn("temporary.invalid", stored)
        self.assertEqual(
            inventory["candidates"][0]["scope_ids"],
            ["optimization_ik_qp_mpc", "solver_numerics"],
        )

    def test_reviewed_sources_override_pending_and_keep_problem_ids(self):
        source = SimpleNamespace(
            kind=SimpleNamespace(value="community"),
            source_id="community.x.1",
            canonical_url="https://x.com/robot/status/1",
            title="已整理帖子",
            captured_at=NOW,
            metadata={
                "platform": "x",
                "scope_id": "optimization_ik_qp_mpc",
                "query": "WBC QP",
                "engineering_qa": [{"problem_id": "problem.scope.abcdef12"}],
            },
        )
        inventory = build_social_candidate_inventory(
            [[{
                "platform": "x",
                "canonical_url": source.canonical_url,
                "title": source.title,
            }]],
            reviewed_sources=[source],
            generated_at=NOW,
        )
        record = inventory["candidates"][0]
        self.assertEqual(record["triage_status"], "reviewed")
        self.assertEqual(record["related_problem_ids"], ["problem.scope.abcdef12"])

    def test_reviewed_source_with_iso_captured_at_can_seed_inventory(self):
        source = SimpleNamespace(
            kind=SimpleNamespace(value="community"),
            source_id="community.x.2",
            canonical_url="https://x.com/robot/status/2",
            title="新增已整理帖子",
            captured_at="2026-08-10T12:00:00+00:00",
            metadata={
                "platform": "x",
                "scope_id": "communication_realtime_control",
                "query": "WBC latency",
                "engineering_qa": [{"problem_id": "problem.scope.abcdef34"}],
            },
        )
        inventory = build_social_candidate_inventory(
            [], reviewed_sources=[source], generated_at=NOW
        )
        record = inventory["candidates"][0]
        self.assertEqual(record["triage_status"], "reviewed")
        self.assertEqual(record["first_seen_at"], source.captured_at)

    def test_previous_inventory_round_trip_preserves_scopes_and_queries(self):
        first = build_social_candidate_inventory(
            [[{
                "platform": "github_issue",
                "canonical_url": "https://github.com/org/repo/issues/9",
                "title": "WBC timing issue",
                "scope_ids": ["communication_realtime_control", "sim_to_sim_and_sim_to_real"],
                "queries": ["WBC latency", "sim2real timing"],
            }]],
            generated_at=NOW,
        )
        second = build_social_candidate_inventory(
            [], previous_inventory=first, generated_at=NOW
        )
        record = second["candidates"][0]
        self.assertEqual(
            record["scope_ids"],
            ["communication_realtime_control", "sim_to_sim_and_sim_to_real"],
        )
        self.assertEqual(record["queries"], ["WBC latency", "sim2real timing"])

    def test_exclusion_requires_reason_and_pending_pages_have_every_link(self):
        values = [{
            "platform": "github_issue",
            "canonical_url": f"https://github.com/org/repo/issues/{index}",
            "title": f"Issue {index}",
            "scope_id": "open_ended_wbc_field_notes",
            "query": "humanoid WBC",
        } for index in range(1, 251)]
        with self.assertRaises(SocialInventoryError):
            build_social_candidate_inventory(
                [values],
                decisions=[{
                    "platform": "github_issue",
                    "canonical_url": values[0]["canonical_url"],
                    "triage_status": "excluded",
                }],
                generated_at=NOW,
            )
        inventory = build_social_candidate_inventory(
            [values],
            decisions=[{
                "platform": "github_issue",
                "canonical_url": values[0]["canonical_url"],
                "triage_status": "excluded",
                "triage_reason_zh": "广告或与 WBC 工程无关。",
            }],
            generated_at=NOW,
        )
        self.assertEqual(inventory["stats"]["technical_pending"], 249)
        self.assertEqual(inventory["stats"]["excluded"], 1)
        pages = render_pending_markdown(inventory)
        scope_page = pages["open_ended_wbc_field_notes.md"]
        self.assertEqual(scope_page.count("- 原链接："), 249)
        self.assertIn("排除原因分布", pages["index.md"])
        self.assertNotIn(
            f"[{values[0]['canonical_url']}]({values[0]['canonical_url']})",
            scope_page,
        )


if __name__ == "__main__":
    unittest.main()
