from datetime import datetime, timezone
import unittest

from wbc_handbook.social_discovery import (
    empty_discovery_state,
    evolve_query_frontier,
    frontier_queries,
    query_signature,
    render_query_frontier_markdown,
    select_incremental_queries,
    update_discovery_state,
)


NOW = datetime(2026, 8, 10, 12, 0, tzinfo=timezone.utc)


class SocialDiscoveryTests(unittest.TestCase):
    def test_selector_round_robins_scopes_and_deduplicates_signatures(self):
        queries = [
            {"scope_id": "scope_one", "domain_hints": [], "query": "WBC QP", "platforms": ["x"]},
            {"scope_id": "scope_one", "domain_hints": [], "query": "WBC QP", "platforms": ["x"]},
            {"scope_id": "scope_one", "domain_hints": [], "query": "WBC solver", "platforms": ["x"]},
            {"scope_id": "scope_two", "domain_hints": [], "query": "WBC contact", "platforms": ["x"]},
        ]
        selection = select_incremental_queries(
            queries,
            platforms=["x"],
            max_queries_per_platform=2,
            selected_at=NOW,
        )
        self.assertEqual(len(selection["selected"]), 2)
        self.assertEqual(
            {item["scope_id"] for item in selection["selected"]},
            {"scope_one", "scope_two"},
        )
        self.assertTrue(any(
            item["reason"] == "duplicate_query_signature"
            for item in selection["skipped"]
        ))

    def test_zero_yield_query_gets_backoff_and_force_overrides_it(self):
        query = {
            "scope_id": "scope_one",
            "domain_hints": [],
            "query": "WBC no result",
            "platforms": ["x"],
        }
        signature = query_signature("x", "scope_one", "WBC no result")
        state = empty_discovery_state(NOW)
        state["queries"][signature] = {
            "run_count": 2,
            "no_new_streak": 2,
            "last_new_urls": 0,
            "next_eligible_at": "2026-08-12T12:00:00+00:00",
        }
        deferred = select_incremental_queries(
            [query], platforms=["x"], state=state, selected_at=NOW
        )
        self.assertEqual(deferred["selected"], [])
        self.assertEqual(deferred["skipped"][0]["reason"], "backoff_not_elapsed")
        forced = select_incremental_queries(
            [query], platforms=["x"], state=state, force=True, selected_at=NOW
        )
        self.assertEqual(len(forced["selected"]), 1)

    def test_state_tracks_new_and_duplicate_urls_per_query(self):
        plan = {
            "run_id": "plan-1",
            "created_at": "2026-08-10T11:00:00+00:00",
            "tasks": [{
                "task_id": "task-1",
                "task_type": "search_and_enrich",
                "platform": "x",
                "scope_id": "scope_one",
                "query": "WBC QP",
            }],
        }
        result = {
            "run_id": "run-1",
            "candidates": [{
                "canonical_url": "https://x.com/robot/status/1",
                "platform": "x",
                "body_sha256": "a" * 64,
                "matches": [{
                    "task_id": "task-1",
                    "scope_id": "scope_one",
                    "query": "WBC QP",
                }],
            }],
            "blockers": [],
        }
        first = update_discovery_state(plan, result, updated_at=NOW)
        self.assertEqual(first["runs"][-1]["new_urls"], 1)
        second = update_discovery_state(
            plan, result, previous_state=first,
            updated_at=datetime(2026, 8, 11, 12, 0, tzinfo=timezone.utc),
        )
        self.assertEqual(second["runs"][-1]["new_urls"], 0)
        signature = query_signature("x", "scope_one", "WBC QP")
        self.assertEqual(second["queries"][signature]["no_new_streak"], 1)
        self.assertEqual(second["queries"][signature]["total_duplicate_urls"], 1)

    def test_completed_empty_search_increments_zero_yield_backoff(self):
        plan = {
            "run_id": "plan-empty",
            "created_at": "2026-08-10T11:00:00+00:00",
            "tasks": [{
                "task_id": "task-empty",
                "task_type": "search_and_enrich",
                "platform": "x",
                "scope_id": "scope_one",
                "query": "OCS2 WBC no result",
            }],
        }
        result = {
            "run_id": "run-empty",
            "candidates": [],
            "blockers": [],
            "completed_searches": [{
                "task_id": "task-empty",
                "platform": "x",
                "state": "empty_results",
                "evidence": ["explicit page state"],
            }],
        }
        state = update_discovery_state(plan, result, updated_at=NOW)
        signature = query_signature("x", "scope_one", "OCS2 WBC no result")
        history = state["queries"][signature]
        self.assertEqual(history["last_new_urls"], 0)
        self.assertEqual(history["no_new_streak"], 1)
        self.assertEqual(
            history["next_eligible_at"], "2026-08-11T12:00:00+00:00"
        )

    def test_frontier_uses_post_and_comment_evidence_without_runaway_activation(self):
        candidates = [
            {
                "platform": "x",
                "canonical_url": "https://x.com/a/status/1",
                "scope_id": "simulator_physics_numerics",
                "body_text": "Isaac Lab 自定义地形导致结果不可复现，RobotFoo 接触状态异常。",
                "selected_comments": [{
                    "author_display": "dev",
                    "text": "RobotFoo 的 ContactPatchCache 也出现抖动。",
                    "source_url": "https://x.com/dev/status/2",
                }],
            },
            {
                "platform": "zhihu",
                "canonical_url": "https://zhuanlan.zhihu.com/p/3",
                "scope_id": "simulator_physics_numerics",
                "body_text": "另一台机器同样遇到 RobotFoo 与 ContactPatchCache 不一致。",
                "selected_comments": [],
            },
        ]
        frontier = evolve_query_frontier(
            candidates,
            existing_queries=[{
                "scope_id": "simulator_physics_numerics",
                "query": "WBC 接触调试",
            }],
            evolved_at=NOW,
        )
        by_term = {item["term"]: item for item in frontier["topics"]}
        self.assertEqual(by_term["Isaac Lab"]["status"], "ready")
        self.assertEqual(by_term["RobotFoo"]["status"], "ready")
        self.assertGreaterEqual(by_term["RobotFoo"]["independent_source_count"], 2)
        self.assertEqual(by_term["ContactPatchCache"]["status"], "ready")
        self.assertTrue(any(
            evidence["locator"].startswith("评论")
            for evidence in by_term["ContactPatchCache"]["evidence"]
        ))
        dynamic = frontier_queries(frontier, ["x", "github_issue"])
        self.assertTrue(any(item["platforms"] == ["github_issue"] for item in dynamic))

    def test_frontier_never_truncates_topics_or_per_topic_evidence(self):
        candidates = []
        for index in range(205):
            token = f"RobotComponent{index:03d}"
            for source_index in range(21):
                candidates.append({
                    "platform": "x",
                    "canonical_url": (
                        f"https://x.com/robot/status/{index * 100 + source_index}"
                    ),
                    "scope_id": "open_ended_wbc_field_notes",
                    "title": f"{token} WBC debugging record",
                    "body_text": f"{token} failed in a reproducible test.",
                    "selected_comments": [],
                })
        frontier = evolve_query_frontier(
            candidates, existing_queries=[], evolved_at=NOW
        )
        self.assertGreaterEqual(len(frontier["topics"]), 205)
        topic = next(
            item for item in frontier["topics"]
            if item["term"] == "RobotComponent000"
        )
        self.assertGreaterEqual(len(topic["evidence"]), 21)
        selected = frontier_queries(
            frontier, ["x"], topic_ids=[topic["topic_id"]]
        )
        self.assertEqual(len(selected), 1)
        self.assertEqual(selected[0]["frontier_topic_id"], topic["topic_id"])

    def test_frontier_report_collapses_multiline_browser_labels(self):
        frontier = {
            "schema_version": 2,
            "topics": [{
                "topic_id": "topic-multiline-label",
                "term": "contact\n  debugging",
                "status": "needs_more_evidence",
                "scope_id": "simulator_physics_numerics",
                "evidence": [{
                    "platform": "x",
                    "root_url": "https://x.com/robot/status/1",
                    "source_url": "https://x.com/robot/status/2",
                    "locator": "评论 @Robot Lab \n@robotlab\n·\n5月22日",
                }],
            }],
        }

        report = render_query_frontier_markdown(frontier)

        self.assertIn("## 1. contact debugging", report)
        self.assertIn("[评论 @Robot Lab @robotlab · 5月22日]", report)
        self.assertFalse(any(line.endswith(" ") for line in report.splitlines()))

    def test_bounded_rounds_eventually_cover_every_ready_topic(self):
        queries = [{
            "scope_id": f"scope_{index % 5}",
            "domain_hints": [],
            "query": f"WBC component {index}",
            "platforms": ["x"],
            "origin": "frontier",
            "frontier_topic_id": f"topic-{index}",
        } for index in range(53)]
        state = empty_discovery_state(NOW)
        selected_topic_ids = set()
        for _ in range(7):
            selection = select_incremental_queries(
                queries,
                platforms=["x"],
                state=state,
                max_queries_per_platform=8,
                selected_at=NOW,
            )
            for item in selection["selected"]:
                selected_topic_ids.add(item["frontier_topic_id"])
                state["queries"][item["query_signature"]] = {
                    "run_count": 1,
                    "no_new_streak": 1,
                    "last_new_urls": 0,
                    "next_eligible_at": "2026-08-12T12:00:00+00:00",
                }
        self.assertEqual(len(selected_topic_ids), 53)


if __name__ == "__main__":
    unittest.main()
