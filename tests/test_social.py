from __future__ import annotations

from contextlib import redirect_stdout
from datetime import datetime, timezone
import io
import json
from pathlib import Path
import uuid
import unittest

from wbc_handbook.cli import main
from wbc_handbook.social import (
    SocialCollectionError,
    build_collection_plan,
    canonicalize_social_url,
    deduplicate_social_sources,
    normalize_social_capture,
    parse_attention_number,
    queries_from_config,
    render_engineering_qa_markdown,
)
from wbc_handbook.social_x import (
    build_x_api_query,
    build_x_collection_plan,
    collect_x_candidates,
    extract_x_post_id,
)
from wbc_handbook.social_zhihu import (
    build_zhihu_api_query,
    build_zhihu_collection_plan,
    collect_zhihu_candidates,
)
from wbc_handbook.social_xiaohongshu import (
    apply_xhs_review_decisions,
    build_xhs_review_plan,
    build_xhs_review_queue,
)


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def synthetic_capture(**overrides):
    payload = {
        "platform": "xiaohongshu",
        "scope_id": "tracking_and_teleoperation",
        "domain_hints": ["universal_tracking_teleoperation"],
        "query": "G1 全身遥操 延迟 抖动",
        "retrieval_url": (
            "https://www.xiaohongshu.com/explore/0123456789abcdef01234567"
            "?xsec_token=must-not-be-stored"
        ),
        "canonical_url": (
            "https://www.xiaohongshu.com/explore/0123456789abcdef01234567"
        ),
        "captured_at": "2026-08-10T12:00:00+08:00",
        "title": "Synthetic G1 field note",
        "author_display": "Synthetic Author",
        "summary": "Synthetic community capture; not engineering evidence.",
        "wbc_relevance_reason": "Synthetic whole-body teleoperation debugging record.",
        "excerpt": "Synthetic excerpt.",
        "components": ["whole-body tracker"],
        "robot_platforms": ["synthetic humanoid"],
        "engineering_details": {
            "problem_statements": ["Teleoperation command jitters."],
            "environments": ["Synthetic test environment."],
            "symptoms": ["Visible high-frequency arm jitter."],
            "diagnostics": ["Compared command and control-loop timestamps."],
            "attempts": ["Aligned timestamps."],
            "effective_fixes": ["Jitter decreased after alignment."],
            "limits": ["Not verified on hardware."],
        },
        "engineering_qa": [{
            "question_zh": "遥操手臂高频抖动时先检查什么？",
            "answer_zh": "原帖候选解答建议先核对指令与控制循环时间戳。",
            "answer_status": "partial",
            "source_locator": "正文第 2 段",
        }],
        "attention": {"likes": "1.4万", "comments": "1千+"},
        "media_summaries": ["Synthetic image summary."],
        "selected_comments": [{
            "author_display": "Synthetic Commenter",
            "text": "Synthetic comment.",
            "likes": "10+",
        }],
    }
    payload.update(overrides)
    return payload


class SocialPlanTests(unittest.TestCase):
    def test_repository_config_covers_open_engineering_scopes(self):
        config = json.loads(
            (PROJECT_ROOT / "config" / "social-queries.json").read_text(encoding="utf-8")
        )
        queries = queries_from_config(config)
        scopes = {item["scope_id"] for item in queries}
        hinted_domains = {
            domain for item in queries for domain in item["domain_hints"]
        }
        self.assertGreater(len(scopes), 7)
        self.assertEqual(len(hinted_domains), 7)
        self.assertIn("environment_setup_dependencies", scopes)
        self.assertIn("open_ended_wbc_field_notes", scopes)
        self.assertTrue(any(not item["domain_hints"] for item in queries))
        required_cross_cutting = {
            "environment_setup_dependencies",
            "training_instability",
            "compute_performance_memory",
            "state_estimation_calibration",
            "communication_and_realtime",
            "sim_to_sim_and_sim_to_real",
            "hardware_actuator_thermal",
            "deployment_firmware_sdk",
            "safety_fall_recovery",
            "reproducibility_and_debugging",
            "open_ended_wbc_field_notes",
        }
        self.assertTrue(required_cross_cutting.issubset(scopes))

    def test_plan_is_finite_manual_and_url_encoded(self):
        plan = build_collection_plan(
            [{
                "scope_id": "locomotion_contact_terrain",
                "domain_hints": ["locomotion_terrain"],
                "query": "G1 摔倒 调参",
            }],
            platforms=["xiaohongshu", "zhihu"],
            max_results_per_query=3,
            max_comments_per_post=4,
            max_tasks_per_batch=1,
            known_canonical_urls=["https://example.org/known"],
            created_at=datetime(2026, 8, 10, 12, tzinfo=timezone.utc),
        )
        self.assertEqual(plan["trigger"], "manual_on_demand")
        self.assertEqual(len(plan["tasks"]), 2)
        self.assertEqual(len(plan["batches"]), 2)
        self.assertTrue(all(len(batch["task_ids"]) <= 1 for batch in plan["batches"]))
        self.assertEqual(plan["known_canonical_urls"], ["https://example.org/known"])
        self.assertTrue(all(task["max_results"] == 3 for task in plan["tasks"]))
        self.assertTrue(all("G1+%E6%91%94%E5%80%92" in task["search_url"] for task in plan["tasks"]))
        self.assertIn("captcha", plan["execution_rules"]["stop_on"])


class SocialNormalizationTests(unittest.TestCase):
    def test_urls_are_canonicalized_without_tracking_parameters(self):
        xhs, xhs_id = canonicalize_social_url(
            "xiaohongshu",
            "https://www.xiaohongshu.com/explore/ABCDEF0123456789ABCDEF01?xsec_token=secret",
        )
        self.assertEqual(
            xhs,
            "https://www.xiaohongshu.com/explore/abcdef0123456789abcdef01",
        )
        self.assertEqual(xhs_id, "abcdef0123456789abcdef01")
        zhihu, zhihu_id = canonicalize_social_url(
            "zhihu",
            "https://www.zhihu.com/question/123/answer/456?utm_source=test",
        )
        self.assertEqual(zhihu, "https://www.zhihu.com/question/123/answer/456")
        self.assertEqual(zhihu_id, "answer.456")

    def test_attention_counter_parser_supports_chinese_units(self):
        self.assertEqual(parse_attention_number("1.4万"), 14000)
        self.assertEqual(parse_attention_number("1千+"), 1000)
        self.assertEqual(parse_attention_number("2,033"), 2033)
        self.assertEqual(parse_attention_number("1.2K"), 1200)
        self.assertEqual(parse_attention_number("3M"), 3_000_000)
        self.assertEqual(parse_attention_number("2.1B"), 2_100_000_000)

    def test_x_status_urls_are_canonicalized_across_aliases(self):
        canonical, post_id = canonicalize_social_url(
            "x", "https://twitter.com/RobotExpert/status/123456/photo/1?ref=test"
        )
        self.assertEqual(canonical, "https://x.com/robotexpert/status/123456")
        self.assertEqual(post_id, "123456")
        self.assertEqual(
            extract_x_post_id("https://x.com/RobotExpert/status/123456/video/1"),
            "123456",
        )

    def test_x_capture_allows_generated_title_and_precise_reply_link(self):
        capture = synthetic_capture(
            platform="x",
            access_mode="public_api",
            retrieval_url="https://x.com/RootAuthor/status/100",
            canonical_url="https://x.com/RootAuthor/status/100",
            title=None,
            author_display="@RootAuthor",
            engineering_qa=[{
                "question_zh": "QP 不可行时作者如何处理？",
                "answer_zh": "作者在回复中建议先检查接触约束。",
                "answer_status": "partial",
                "source_locator": "作者回复",
                "source_url": "https://x.com/RootAuthor/status/101",
            }],
        )
        source = normalize_social_capture(capture)
        self.assertEqual(source.publisher, "X")
        self.assertEqual(source.source_id, "community.x.100")
        self.assertTrue(source.metadata["title_generated"])
        self.assertEqual(
            source.metadata["engineering_qa"][0]["source_url"],
            "https://x.com/rootauthor/status/101",
        )

    def test_capture_becomes_candidate_community_source_without_token(self):
        source = normalize_social_capture(synthetic_capture())
        self.assertEqual(
            source.source_id,
            "community.xiaohongshu.0123456789abcdef01234567",
        )
        self.assertEqual(source.kind.value, "community")
        self.assertEqual(source.attention["likes"], 14000)
        self.assertEqual(source.metadata["review_status"], "candidate")
        self.assertEqual(source.metadata["scope_id"], "tracking_and_teleoperation")
        self.assertEqual(source.metadata["experience_quality"], "rich")
        self.assertNotIn("retrieval_url", source.metadata)
        self.assertNotIn("xsec_token", json.dumps(source.to_dict()))
        self.assertEqual(source.metadata["selected_comments"][0]["likes"], 10)
        qa = source.metadata["engineering_qa"][0]
        self.assertEqual(qa["source_url"], source.canonical_url)
        self.assertEqual(qa["verification_status"], "community_candidate")

    def test_engineering_report_contains_clickable_original_post(self):
        source = normalize_social_capture(synthetic_capture())
        markdown = render_engineering_qa_markdown(
            [source], generated_at=datetime(2026, 8, 10, 12, tzinfo=timezone.utc)
        )
        self.assertIn(f"]({source.canonical_url})", markdown)
        self.assertIn("候选解答", markdown)

    def test_wrong_platform_host_is_rejected(self):
        with self.assertRaises(SocialCollectionError):
            normalize_social_capture(synthetic_capture(
                canonical_url="https://example.org/explore/0123456789abcdef01234567"
            ))

    def test_duplicate_posts_are_removed_within_one_run(self):
        first = normalize_social_capture(synthetic_capture())
        second = normalize_social_capture(synthetic_capture(summary="Second capture."))
        unique, duplicates = deduplicate_social_sources([first, second])
        self.assertEqual(len(unique), 1)
        self.assertEqual(duplicates, [second.source_id])


class SocialCliTests(unittest.TestCase):
    def test_cli_builds_plan_and_imports_capture(self):
        run_root = PROJECT_ROOT / "var" / "test-runs" / str(uuid.uuid4())
        plan_path = run_root / "social-plan.json"
        output = io.StringIO()
        with redirect_stdout(output):
            exit_code = main([
                "social-plan",
                "--config", str(PROJECT_ROOT / "config" / "social-queries.json"),
                "--platform", "zhihu",
                "--scope", "locomotion_contact_terrain",
                "--max-results-per-query", "1",
                "--output", str(plan_path),
            ])
        self.assertEqual(exit_code, 0)
        self.assertTrue(plan_path.exists())
        plan = json.loads(plan_path.read_text(encoding="utf-8"))
        self.assertTrue(all(task["platform"] == "zhihu" for task in plan["tasks"]))
        self.assertTrue(all(
            task["scope_id"] == "locomotion_contact_terrain" for task in plan["tasks"]
        ))
        self.assertEqual(len(plan["tasks"]), 2)

        capture_path = run_root / "captures.json"
        capture_path.write_text(
            json.dumps({"run_id": "synthetic", "captures": [synthetic_capture()]}),
            encoding="utf-8",
        )
        data_dir = run_root / "data"
        output = io.StringIO()
        with redirect_stdout(output):
            exit_code = main([
                "import-social-captures", str(capture_path), "--data-dir", str(data_dir)
            ])
        self.assertEqual(exit_code, 0)
        report = json.loads(output.getvalue())
        self.assertEqual(len(report["imported"]), 1)
        stored = json.loads(next((data_dir / "sources").glob("*.json")).read_text())
        self.assertNotIn("xsec_token", json.dumps(stored))

        report_path = run_root / "engineering-qa.md"
        output = io.StringIO()
        with redirect_stdout(output):
            exit_code = main([
                "social-report", "--data-dir", str(data_dir),
                "--output", str(report_path),
            ])
        self.assertEqual(exit_code, 0)
        self.assertIn(
            "https://www.xiaohongshu.com/explore/0123456789abcdef01234567",
            report_path.read_text(encoding="utf-8"),
        )

    def test_x_cli_dry_run_needs_no_token_and_writes_official_api_plan(self):
        run_root = PROJECT_ROOT / "var" / "test-runs" / str(uuid.uuid4())
        plan_path = run_root / "x-plan.json"
        output = io.StringIO()
        with redirect_stdout(output):
            exit_code = main([
                "social-collect-x",
                "--query", "humanoid WBC QP infeasible",
                "--dry-run",
                "--output", str(plan_path),
            ])
        self.assertEqual(exit_code, 0)
        plan = json.loads(plan_path.read_text(encoding="utf-8"))
        self.assertEqual(plan["platform"], "x")
        self.assertEqual(plan["access_mode"], "public_api")
        self.assertIn("api.x.com/2/tweets/search/recent", plan["endpoint"])
        self.assertFalse(plan["credential"]["persisted"])
        self.assertNotIn("Authorization", plan_path.read_text(encoding="utf-8"))

    def test_zhihu_cli_dry_run_records_official_api_limitations(self):
        run_root = PROJECT_ROOT / "var" / "test-runs" / str(uuid.uuid4())
        plan_path = run_root / "zhihu-plan.json"
        output = io.StringIO()
        with redirect_stdout(output):
            exit_code = main([
                "social-collect-zhihu",
                "--query", "人形机器人 WBC QP 调试",
                "--dry-run",
                "--output", str(plan_path),
            ])
        self.assertEqual(exit_code, 0)
        plan = json.loads(plan_path.read_text(encoding="utf-8"))
        self.assertIn("developer.zhihu.com/api/v1/content/zhihu_search", plan["endpoint"])
        self.assertFalse(plan["limitations"]["full_text"])
        self.assertFalse(plan["credential"]["persisted"])

    def test_xiaohongshu_cli_builds_no_network_review_queue(self):
        run_root = PROJECT_ROOT / "var" / "test-runs" / str(uuid.uuid4())
        candidate_path = run_root / "xhs-candidates.json"
        queue_path = run_root / "xhs-queue.json"
        candidate_path.parent.mkdir(parents=True, exist_ok=True)
        candidate_path.write_text(json.dumps({"candidates": [{
            "url": (
                "https://www.xiaohongshu.com/explore/abcdef0123456789abcdef01"
                "?xsec_token=temporary"
            ),
            "query": "humanoid WBC 调试",
            "title": "候选帖子",
            "snippet": "站外搜索摘要",
        }]}), encoding="utf-8")
        output = io.StringIO()
        with redirect_stdout(output):
            exit_code = main([
                "social-queue-xiaohongshu",
                "--scope", "open_ended_wbc_field_notes",
                "--candidates", str(candidate_path),
                "--output", str(queue_path),
            ])
        self.assertEqual(exit_code, 0)
        queue = json.loads(queue_path.read_text(encoding="utf-8"))
        self.assertEqual(queue["collection_mode"], "manual_review_queue")
        self.assertFalse(queue["plan"]["automation_boundary"]["browser_dom_extraction"])
        self.assertEqual(
            queue["candidates"][0]["canonical_url"],
            "https://www.xiaohongshu.com/explore/abcdef0123456789abcdef01",
        )
        self.assertNotIn("xsec_token", queue_path.read_text(encoding="utf-8"))


class FakeXClient:
    def __init__(self):
        self.calls = []

    def get_json(self, path, params):
        self.calls.append((path, dict(params)))
        return {
            "data": [{
                "id": "200",
                "text": "truncated",
                "note_tweet": {"text": "Full long-form WBC debugging note"},
                "author_id": "u1",
                "created_at": "2026-08-10T04:00:00Z",
                "conversation_id": "200",
                "attachments": {"media_keys": ["m1"]},
                "public_metrics": {"like_count": 7, "reply_count": 2},
                "lang": "en",
                "edit_history_tweet_ids": ["200"],
            }],
            "includes": {
                "users": [{
                    "id": "u1", "username": "WBCExpert", "name": "WBC Expert"
                }],
                "media": [{
                    "media_key": "m1", "type": "photo",
                    "url": "https://pbs.twimg.com/media/example.jpg",
                    "alt_text": "QP diagnostic plot",
                }],
            },
            "meta": {"newest_id": "200", "result_count": 1},
        }


class XOfficialApiTests(unittest.TestCase):
    def test_query_guard_and_collection_preserve_long_text_media_and_state(self):
        query = {
            "scope_id": "optimization_ik_qp_mpc",
            "domain_hints": ["loco_manipulation_wbc"],
            "query": "WBC QP infeasible",
        }
        guarded = build_x_api_query(query["query"])
        self.assertIn("robot OR robotics", guarded)
        self.assertIn("-is:retweet", guarded)
        plan = build_x_collection_plan(
            [query], max_posts_per_query=3,
            created_at=datetime(2026, 8, 10, 12, tzinfo=timezone.utc),
        )
        self.assertEqual(plan["estimated_post_read_upper_bound"], 3)

        client = FakeXClient()
        result, state = collect_x_candidates(
            [query], client, max_posts_per_query=3,
            created_at=datetime(2026, 8, 10, 12, tzinfo=timezone.utc),
        )
        candidate = result["candidates"][0]
        self.assertEqual(
            candidate["canonical_url"], "https://x.com/WBCExpert/status/200"
        )
        self.assertEqual(candidate["text"], "Full long-form WBC debugging note")
        self.assertEqual(candidate["media"][0]["alt_text"], "QP diagnostic plot")
        self.assertNotIn("X_BEARER_TOKEN", json.dumps(result))

        second_client = FakeXClient()
        collect_x_candidates(
            [query], second_client, previous_state=state, max_posts_per_query=3,
            created_at=datetime(2026, 8, 10, 13, tzinfo=timezone.utc),
        )
        self.assertEqual(second_client.calls[0][1]["since_id"], "200")


class FakeZhihuClient:
    def __init__(self):
        self.calls = []

    def search(self, query, count=10):
        self.calls.append((query, count))
        return {
            "Data": [{
                "ContentType": "answer",
                "ContentID": "456",
                "Title": "人形机器人 QP 不可行如何排查？",
                "ContentText": "先检查接触约束和权重尺度。",
                "URL": "https://www.zhihu.com/question/123/answer/456?utm_source=test",
                "AuthorName": "测试作者",
                "CommentCount": 3,
                "VoteupCount": 12,
                "CreatedTime": "2026-08-10T04:00:00Z",
                "SelectedComments": [{"text": "补充检查求解器状态。"}],
            }, {
                "ContentType": "user",
                "ContentID": "user-1",
                "Title": "不应入库的用户结果",
                "ContentText": "",
                "URL": "https://www.zhihu.com/people/example",
            }],
            "HasMore": False,
        }


class ZhihuOfficialApiTests(unittest.TestCase):
    def test_official_summary_collection_is_bounded_and_stateful(self):
        query = {
            "scope_id": "optimization_ik_qp_mpc",
            "domain_hints": ["loco_manipulation_wbc"],
            "query": "WBC QP infeasible",
        }
        self.assertIn("人形机器人", build_zhihu_api_query(query["query"]))
        plan = build_zhihu_collection_plan(
            [query], count=10,
            created_at=datetime(2026, 8, 10, 12, tzinfo=timezone.utc),
        )
        self.assertEqual(plan["count_per_query"], 10)
        self.assertFalse(plan["limitations"]["pagination"])

        client = FakeZhihuClient()
        result, state = collect_zhihu_candidates(
            [query], client,
            created_at=datetime(2026, 8, 10, 12, tzinfo=timezone.utc),
        )
        self.assertEqual(len(result["candidates"]), 1)
        candidate = result["candidates"][0]
        self.assertEqual(
            candidate["canonical_url"],
            "https://www.zhihu.com/question/123/answer/456",
        )
        self.assertEqual(candidate["summary"], "先检查接触约束和权重尺度。")
        self.assertEqual(candidate["attention"]["voteups"], 12)
        self.assertFalse(candidate["full_text_available"])
        self.assertEqual(result["query_results"][0]["unsupported_url_or_type"], 1)

        second, _ = collect_zhihu_candidates(
            [query], FakeZhihuClient(), previous_state=state,
            created_at=datetime(2026, 8, 10, 13, tzinfo=timezone.utc),
        )
        self.assertEqual(second["candidates"], [])
        self.assertEqual(second["query_results"][0]["skipped_seen"], 1)


class XiaohongshuReviewQueueTests(unittest.TestCase):
    def test_plan_queue_dedup_and_human_decision_preserve_original_link(self):
        queries = [{
            "scope_id": "open_ended_wbc_field_notes",
            "domain_hints": [],
            "query": "人形机器人 WBC 工程问题",
        }]
        now = datetime(2026, 8, 10, 12, tzinfo=timezone.utc)
        plan = build_xhs_review_plan(queries, created_at=now)
        self.assertFalse(plan["automation_boundary"]["platform_login"])
        self.assertFalse(plan["automation_boundary"]["full_text_collection"])
        raw = {
            "url": "https://www.xiaohongshu.com/explore/abcdef0123456789abcdef01",
            "query": "人形机器人 WBC 工程问题",
            "title": "WBC 调试记录",
            "snippet": "公开搜索结果摘要",
        }
        queue = build_xhs_review_queue(plan, [raw, raw], created_at=now)
        self.assertEqual(queue["added"], 1)
        self.assertEqual(len(queue["candidates"]), 1)
        url = queue["candidates"][0]["canonical_url"]
        reviewed = apply_xhs_review_decisions(queue, [{
            "canonical_url": url,
            "review_status": "approved_for_analysis",
            "review_note": "人工确认与 WBC 工程调试相关。",
        }], reviewed_at=now)
        self.assertEqual(
            reviewed["candidates"][0]["review_status"],
            "approved_for_analysis",
        )
        self.assertEqual(reviewed["candidates"][0]["canonical_url"], url)
        self.assertFalse(reviewed["candidates"][0]["content_collected"])


if __name__ == "__main__":
    unittest.main()
