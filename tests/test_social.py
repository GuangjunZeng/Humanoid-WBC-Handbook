from __future__ import annotations

from contextlib import redirect_stdout
from datetime import datetime, timezone
import io
import json
from pathlib import Path
import uuid
import unittest
from urllib import error

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
from wbc_handbook.social_browser import (
    BrowserCollectionError,
    build_browser_collection_plan,
    classify_browser_page,
    normalize_browser_collection_run,
    normalize_browser_page_capture,
)
from wbc_handbook.social_x import (
    XApiClient,
    XCollectionError,
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
        "title": "合成 G1 工程记录",
        "author_display": "Synthetic Author",
        "summary": "这是用于测试中文工程整理与双语术语规则的合成社区记录，不构成工程证据。",
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

    def test_platform_queries_override_generic_queries(self):
        config = {
            "schema_version": 2,
            "scopes": [{
                "scope_id": "optimization_ik_qp_mpc",
                "domain_hints": ["loco_manipulation_wbc"],
                "queries": ["人形机器人 WBC QP 调试"],
                "platform_queries": {
                    "x": ["whole body controller QP"],
                },
            }],
        }
        self.assertEqual(
            queries_from_config(config, platform="x")[0]["query"],
            "whole body controller QP",
        )
        self.assertEqual(
            queries_from_config(config, platform="zhihu")[0]["query"],
            "人形机器人 WBC QP 调试",
        )

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
        xhs_search, xhs_search_id = canonicalize_social_url(
            "xiaohongshu",
            "https://www.xiaohongshu.com/search_result/ABCDEF0123456789ABCDEF01?xsec_token=secret",
        )
        self.assertEqual(xhs_search, xhs)
        self.assertEqual(xhs_search_id, xhs_id)
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
                "answer_zh": "作者在回复中建议先检查接触约束、关节力矩限幅和权重尺度，再根据求解器日志缩小冲突范围。",
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
        self.assertIn(
            "全身遥操作（Whole-Body Teleoperation）", qa["bilingual_terms"]
        )

    def test_engineering_qa_rejects_english_only_content(self):
        with self.assertRaisesRegex(SocialCollectionError, "Chinese-first"):
            normalize_social_capture(synthetic_capture(engineering_qa=[{
                "question_zh": "How should WBC jitter be debugged?",
                "answer_zh": "Check timestamps and the control loop before deployment.",
                "answer_status": "partial",
                "source_locator": "Synthetic body",
                "bilingual_terms": ["全身控制（Whole-Body Control, WBC）"],
            }]))

    def test_engineering_qa_rejects_english_only_term_label(self):
        with self.assertRaisesRegex(SocialCollectionError, "Chinese（English）"):
            normalize_social_capture(synthetic_capture(engineering_qa=[{
                "question_zh": "遥操作出现高频抖动时应该先检查什么？",
                "answer_zh": "先核对指令时间戳与控制循环时间戳，再观察对齐后抖动是否下降。",
                "answer_status": "partial",
                "source_locator": "合成正文",
                "bilingual_terms": ["Whole-Body Teleoperation"],
            }]))

    def test_engineering_report_contains_clickable_original_post(self):
        source = normalize_social_capture(synthetic_capture())
        markdown = render_engineering_qa_markdown(
            [source], generated_at=datetime(2026, 8, 10, 12, tzinfo=timezone.utc)
        )
        self.assertIn(f"]({source.canonical_url})", markdown)
        self.assertIn("候选解答", markdown)
        self.assertIn("`community_candidate`", markdown)
        self.assertIn("环境：Synthetic test environment.", markdown)
        self.assertIn("图片分析：Synthetic image summary.", markdown)
        self.assertIn("关键术语：", markdown)
        self.assertIn("全身遥操作（Whole-Body Teleoperation）", markdown)

    def test_engineering_report_renders_full_scope_coverage_matrix(self):
        source = normalize_social_capture(synthetic_capture())
        markdown = render_engineering_qa_markdown(
            [source],
            scope_definitions=[
                {
                    "scope_id": "tracking_and_teleoperation",
                    "label_zh": "跟踪与遥操作",
                },
                {
                    "scope_id": "compute_performance_memory",
                    "label_zh": "算力、性能与显存",
                },
            ],
        )
        self.assertIn("# WBC 社交平台工程问题查询手册", markdown)
        self.assertIn("| 跟踪与遥操作 | `tracking_and_teleoperation` |", markdown)
        self.assertIn("| 算力、性能与显存 | `compute_performance_memory` | 0 | 0 | 0 | 0 | 0 |", markdown)
        self.assertIn("Scope 覆盖：1/2", markdown)

    def test_engineering_report_keeps_context_attached_to_each_source(self):
        first = normalize_social_capture(synthetic_capture())
        second = normalize_social_capture(synthetic_capture(
            platform="zhihu",
            retrieval_url="https://zhuanlan.zhihu.com/p/123456789",
            canonical_url="https://zhuanlan.zhihu.com/p/123456789",
            title="第二个合成来源",
            engineering_details={
                "problem_statements": ["Second problem."],
                "environments": ["Second-only environment."],
                "symptoms": ["Second-only symptom."],
            },
        ))
        markdown = render_engineering_qa_markdown([first, second])
        first_section = markdown.split("### 遥操手臂高频抖动时先检查什么？", 1)[1]
        first_section = first_section.split("### ", 1)[0]
        self.assertIn("Synthetic test environment.", first_section)
        self.assertNotIn("Second-only environment.", first_section)

    def test_visible_browser_completeness_is_preserved_and_rendered(self):
        capture = synthetic_capture(
            access_mode="authorized_visible_browser",
            collection_completeness={
                "status": "partial_visible",
                "post_text_scope": "visible_dom",
                "reply_scope": "bounded_visible_subset",
                "media_scope": "visible_media_screenshot_queue",
                "visible_replies_captured": 14,
                "reply_limit_requested": 500,
                "reply_expansion_attempts": 2,
                "reply_depth_reached": 1,
                "reply_depth_limit": 10,
                "reply_expansion_strategy": "until_exhausted_or_guardrail",
                "hidden_or_inaccessible_content_included": False,
                "stop_reason": "no_more_visible_reply_controls",
            },
        )
        source = normalize_social_capture(capture)
        completeness = source.metadata["collection_completeness"]
        self.assertEqual(completeness["status"], "partial_visible")
        self.assertEqual(completeness["visible_replies_captured"], 14)
        markdown = render_engineering_qa_markdown([source])
        self.assertIn("`partial_visible`", markdown)
        self.assertIn("可见回复 14", markdown)
        self.assertIn("展开 2 次", markdown)

    def test_visible_browser_capture_cannot_claim_complete_collection(self):
        with self.assertRaises(SocialCollectionError):
            normalize_social_capture(synthetic_capture(
                access_mode="authorized_visible_browser",
                collection_completeness={"status": "complete"},
            ))

    def test_visible_browser_capture_requires_completeness_marker(self):
        with self.assertRaises(SocialCollectionError):
            normalize_social_capture(synthetic_capture(
                access_mode="authorized_visible_browser",
            ))

    def test_wrong_platform_host_is_rejected(self):
        with self.assertRaises(SocialCollectionError):
            normalize_social_capture(synthetic_capture(
                canonical_url="https://example.org/explore/0123456789abcdef01234567"
            ))

    def test_duplicate_posts_are_removed_within_one_run(self):
        first = normalize_social_capture(synthetic_capture())
        second = normalize_social_capture(synthetic_capture(
            summary="这是第二条用于去重测试的中文社区摘要，包含足够的工程上下文。"
        ))
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
        self.assertTrue(plan["recovery"]["pagination_cursor_persisted"])
        self.assertEqual(plan["retry"]["max_retries"], 3)
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

    def test_browser_plan_and_ingest_cli_are_bounded_and_token_free(self):
        run_root = PROJECT_ROOT / "var" / "test-runs" / str(uuid.uuid4())
        plan_path = run_root / "browser-plan.json"
        output = io.StringIO()
        with redirect_stdout(output):
            exit_code = main([
                "social-browser-plan",
                "--platform", "xiaohongshu",
                "--query", "人形机器人 WBC QP 调试",
                "--max-results-per-query", "2",
                "--max-posts-per-run", "2",
                "--output", str(plan_path),
            ])
        self.assertEqual(exit_code, 0)
        plan = json.loads(plan_path.read_text(encoding="utf-8"))
        self.assertEqual(plan["collection_mode"], "visible_browser_assisted")
        self.assertTrue(plan["execution_rules"]["visible_authenticated_browser"])
        self.assertFalse(plan["execution_rules"]["background_schedule"])
        self.assertEqual(plan["limits"]["estimated_max_detail_pages"], 2)

        raw_path = run_root / "browser-raw.json"
        result_path = run_root / "browser-candidates.json"
        raw_path.write_text(json.dumps({"pages": [{
            "platform": "xiaohongshu",
            "url": (
                "https://www.xiaohongshu.com/explore/abcdef0123456789abcdef01"
                "?xsec_token=temporary"
            ),
            "page_state": "ready",
            "scope_id": "optimization_ik_qp_mpc",
            "domain_hints": ["loco_manipulation_wbc"],
            "query": "WBC QP 调试",
            "title": "合成浏览器帖子",
            "body_text": "合成正文。",
        }]}), encoding="utf-8")
        output = io.StringIO()
        with redirect_stdout(output):
            exit_code = main([
                "social-browser-ingest", str(raw_path),
                "--output", str(result_path),
            ])
        self.assertEqual(exit_code, 0)
        stored = result_path.read_text(encoding="utf-8")
        self.assertNotIn("xsec_token", stored)
        self.assertEqual(
            json.loads(stored)["candidates"][0]["access_mode"],
            "authorized_visible_browser",
        )

    def test_x_browser_plan_cli_needs_no_api_token(self):
        run_root = PROJECT_ROOT / "var" / "test-runs" / str(uuid.uuid4())
        plan_path = run_root / "x-browser-plan.json"
        output = io.StringIO()
        with redirect_stdout(output):
            exit_code = main([
                "social-browser-plan",
                "--platform", "x",
                "--post", "https://twitter.com/RobotExpert/status/123456/photo/1",
                "--max-comments-per-post", "12",
                "--output", str(plan_path),
            ])
        self.assertEqual(exit_code, 0)
        plan = json.loads(plan_path.read_text(encoding="utf-8"))
        self.assertEqual(plan["platforms"], ["x"])
        self.assertEqual(
            plan["direct_post_urls"],
            ["https://x.com/robotexpert/status/123456"],
        )
        self.assertEqual(plan["tasks"][0]["task_type"], "detail_and_visible_replies")
        self.assertEqual(plan["completeness_contract"]["status"], "partial_visible")
        self.assertFalse(plan["execution_rules"]["hidden_api_calls"])
        self.assertNotIn("X_BEARER_TOKEN", plan_path.read_text(encoding="utf-8"))


class BrowserCollectionTests(unittest.TestCase):
    def test_plan_respects_platform_specific_query_targets(self):
        plan = build_browser_collection_plan(
            [{
                "scope_id": "optimization_ik_qp_mpc",
                "domain_hints": ["loco_manipulation_wbc"],
                "query": "whole body controller QP",
                "platforms": ["x"],
            }],
            platforms=["x", "zhihu"],
            created_at=datetime(2026, 8, 10, 12, tzinfo=timezone.utc),
        )
        self.assertEqual(len(plan["tasks"]), 1)
        self.assertEqual(plan["tasks"][0]["platform"], "x")

    def test_plan_embeds_machine_readable_recipes_and_stop_rules(self):
        query = {
            "scope_id": "optimization_ik_qp_mpc",
            "domain_hints": ["loco_manipulation_wbc"],
            "query": "humanoid WBC QP infeasible",
        }
        plan = build_browser_collection_plan(
            [query], platforms=["xiaohongshu", "zhihu"],
            max_results_per_query=2, max_comments_per_post=3,
            max_posts_per_run=3,
            created_at=datetime(2026, 8, 10, 12, tzinfo=timezone.utc),
        )
        self.assertEqual(len(plan["tasks"]), 2)
        self.assertIn("a[href*='/search_result/']", plan["recipes"]["xiaohongshu"]["search"]["result_link_selectors"])
        self.assertEqual(
            plan["recipes"]["xiaohongshu"]["search"]["navigation_href"],
            "resolved DOM href property, not raw href attribute",
        )
        self.assertIn(".RichContent-inner", plan["recipes"]["zhihu"]["detail"]["body_selectors"])
        self.assertEqual(
            plan["recipes"]["zhihu"]["search"]["navigation_href"],
            "resolved DOM href property, not raw href attribute",
        )
        self.assertEqual(
            plan["recipes"]["zhihu"]["detail"]["comment_selectors"][0],
            ".CommentContent",
        )
        self.assertEqual(
            plan["recipes"]["zhihu"]["detail"]["comment_container_selectors"],
            [".Comments-container"],
        )
        self.assertIn(
            ".Post-RichTextContainer img",
            plan["recipes"]["zhihu"]["detail"]["image_selectors"],
        )
        self.assertIn(
            "img.origin_image",
            plan["recipes"]["zhihu"]["detail"]["image_selectors"],
        )
        self.assertFalse(plan["execution_rules"]["cookies_or_profile_read"])
        self.assertFalse(plan["execution_rules"]["captcha_bypass"])
        self.assertIn("captcha", plan["execution_rules"]["stop_on"])

    def test_x_recipe_search_and_direct_post_are_bounded_and_partial(self):
        query = {
            "scope_id": "optimization_ik_qp_mpc",
            "domain_hints": ["loco_manipulation_wbc"],
            "query": "humanoid WBC QP infeasible",
        }
        plan = build_browser_collection_plan(
            [query],
            platforms=["x"],
            direct_post_urls=["https://x.com/RobotExpert/status/123456?ref=test"],
            max_results_per_query=2,
            max_comments_per_post=4,
            max_posts_per_run=3,
            created_at=datetime(2026, 8, 10, 12, tzinfo=timezone.utc),
        )
        self.assertEqual(len(plan["tasks"]), 2)
        self.assertIn("x.com/search?q=", plan["tasks"][0]["search_url"])
        self.assertNotIn("f=live", plan["tasks"][0]["search_url"])
        self.assertEqual(
            plan["tasks"][1]["canonical_url"],
            "https://x.com/robotexpert/status/123456",
        )
        self.assertIn(
            "[data-testid='tweetText']",
            plan["recipes"]["x"]["detail"]["body_selectors"],
        )
        self.assertIn(
            "a[href*='/article/']",
            plan["recipes"]["x"]["detail"]["article_route_selectors"],
        )
        self.assertEqual(plan["limits"]["reply_depth_limit"], 10)
        self.assertEqual(plan["limits"]["max_reply_expansions"], 100)
        self.assertEqual(
            plan["completeness_contract"]["reply_expansion_strategy"],
            "until_exhausted_or_guardrail",
        )
        self.assertEqual(plan["completeness_contract"]["status"], "partial_visible")

    def test_login_and_captcha_override_weak_ready_signals(self):
        state = classify_browser_page({
            "platform": "xiaohongshu",
            "url": "https://www.xiaohongshu.com/search_result",
            "visible_text": "登录后查看搜索结果",
            "page_state": "ready",
            "signals": {"real_feed_cards": True},
        })
        self.assertEqual(state["state"], "login_required")
        state = classify_browser_page({
            "platform": "zhihu",
            "url": "https://www.zhihu.com/signin?next=%2F",
            "visible_text": "验证码登录 密码登录",
        })
        self.assertEqual(state["state"], "login_required")
        state = classify_browser_page({
            "platform": "xiaohongshu",
            "url": "https://www.xiaohongshu.com/explore",
            "visible_text": "请拖动滑块完成验证",
        })
        self.assertEqual(state["state"], "captcha")
        state = classify_browser_page({
            "platform": "xiaohongshu",
            "url": "https://www.xiaohongshu.com/explore/abcdef0123456789abcdef01",
            "visible_text": "当前笔记暂时无法浏览",
            "signals": {"detail_body_chars": 999},
        })
        self.assertEqual(state["state"], "unavailable")
        state = classify_browser_page({
            "platform": "x",
            "url": "https://x.com/",
            "visible_text": "Join X today 电子邮箱或用户名 使用 Google 继续",
            "signals": {"real_feed_cards": True},
        })
        self.assertEqual(state["state"], "login_required")

    def test_page_capture_strips_navigation_tokens_and_comment_duplicates(self):
        candidate = normalize_browser_page_capture({
            "platform": "xiaohongshu",
            "url": (
                "https://www.xiaohongshu.com/explore/abcdef0123456789abcdef01"
                "?xsec_token=secret&xsec_source=pc_search"
            ),
            "page_state": "ready",
            "scope_id": "optimization_ik_qp_mpc",
            "domain_hints": ["loco_manipulation_wbc"],
            "query": "WBC QP infeasible",
            "title": "QP 调试失败复盘",
            "author_display": "测试作者",
            "body_text": "接触约束冲突导致求解器不可行。",
            "comments": [
                {"author_display": "作者", "text": "先检查接触约束。"},
                {"author_display": "作者", "text": "先检查接触约束。"},
            ],
            "media": [{
                "kind": "image",
                "url": "https://sns-webpic.example/transient.jpg?token=secret",
                "alt_text": "求解器日志截图",
            }],
            "selector_matches": ["#detail-title", "#detail-desc"],
        }, captured_at=datetime(2026, 8, 10, 12, tzinfo=timezone.utc))
        serialized = json.dumps(candidate, ensure_ascii=False)
        self.assertNotIn("xsec_token", serialized)
        self.assertNotIn("transient.jpg", serialized)
        self.assertEqual(len(candidate["selected_comments"]), 1)
        self.assertTrue(candidate["visual_analysis_pending"])
        self.assertEqual(candidate["review_status"], "pending_analysis")

    def test_x_capture_keeps_reply_links_and_local_media_review_path(self):
        candidate = normalize_browser_page_capture({
            "platform": "x",
            "url": "https://twitter.com/RobotExpert/status/123456/photo/1?ref=test",
            "page_state": "ready",
            "scope_id": "optimization_ik_qp_mpc",
            "domain_hints": ["loco_manipulation_wbc"],
            "query": "humanoid WBC QP infeasible",
            "author_display": "@RobotExpert",
            "body_text": "The QP became infeasible after enabling both contact constraints.",
            "comments": [{
                "author_display": "@RobotExpert",
                "text": "Removing the stale contact fixed it.",
                "source_url": "https://x.com/RobotExpert/status/123457",
                "post_id": "123457",
                "parent_post_id": "123456",
                "conversation_id": "123456",
                "depth": 1,
                "is_author_reply": True,
            }],
            "media": [{
                "kind": "image",
                "alt_text": "QP diagnostic plot",
                "screenshot_path": "var/social-browser/media/123456-1.png",
            }],
            "reply_expansion_attempts": 2,
            "reply_depth_reached": 1,
            "selector_matches": ["[data-testid='tweetText']"],
        }, captured_at=datetime(2026, 8, 10, 12, tzinfo=timezone.utc))
        self.assertEqual(
            candidate["canonical_url"], "https://x.com/robotexpert/status/123456"
        )
        self.assertEqual(candidate["title"], "@RobotExpert 的 X 帖子")
        self.assertFalse(candidate["full_text_available"])
        self.assertEqual(
            candidate["selected_comments"][0]["source_url"],
            "https://x.com/robotexpert/status/123457",
        )
        self.assertEqual(candidate["selected_comments"][0]["depth"], 1)
        self.assertEqual(
            candidate["media"][0]["screenshot_path"],
            "var/social-browser/media/123456-1.png",
        )
        self.assertEqual(
            candidate["collection_completeness"]["status"], "partial_visible"
        )
        self.assertEqual(
            candidate["collection_completeness"]["reply_limit_requested"], 200
        )
        self.assertEqual(
            candidate["collection_completeness"]["reply_expansion_strategy"],
            "until_exhausted_or_guardrail",
        )
        self.assertFalse(candidate["extraction_provenance"]["hidden_api_calls"])

    def test_x_capture_accepts_many_adaptive_reply_expansions(self):
        candidate = normalize_browser_page_capture({
            "platform": "x",
            "url": "https://x.com/RobotExpert/status/223456",
            "page_state": "ready",
            "scope_id": "open_ended_wbc_field_notes",
            "domain_hints": [],
            "query": "humanoid WBC debugging",
            "body_text": "Visible root post.",
            "reply_expansion_attempts": 73,
            "reply_depth_reached": 8,
            "reply_depth_limit": 10,
            "max_comments_per_post": 500,
            "stop_reason": "no_more_visible_reply_controls",
        }, captured_at=datetime(2026, 8, 10, 12, tzinfo=timezone.utc))
        completeness = candidate["collection_completeness"]
        self.assertEqual(completeness["reply_expansion_attempts"], 73)
        self.assertEqual(completeness["reply_depth_reached"], 8)
        self.assertEqual(completeness["reply_limit_requested"], 500)

    def test_run_keeps_blockers_and_merges_duplicate_matches(self):
        base = {
            "platform": "zhihu",
            "url": "https://www.zhihu.com/question/123/answer/456?utm_source=test",
            "page_state": "ready",
            "scope_id": "optimization_ik_qp_mpc",
            "domain_hints": ["loco_manipulation_wbc"],
            "query": "WBC QP 调试",
            "title": "QP 不可行如何排查",
            "body_text": "先检查接触约束。",
        }
        duplicate = dict(base)
        duplicate["scope_id"] = "reproducibility_and_debugging"
        duplicate["query"] = "WBC 调试日志"
        result = normalize_browser_collection_run({"pages": [
            base,
            duplicate,
            {
                "task_id": "browser-zhihu-0003",
                "platform": "zhihu",
                "url": "https://www.zhihu.com/signin?next=%2F",
                "visible_text": "验证码登录 密码登录",
            },
        ]}, captured_at=datetime(2026, 8, 10, 12, tzinfo=timezone.utc))
        self.assertEqual(result["stats"]["ready_pages"], 2)
        self.assertEqual(result["stats"]["unique_candidates"], 1)
        self.assertEqual(result["stats"]["duplicates_merged"], 1)
        self.assertEqual(result["blockers"][0]["state"], "login_required")
        self.assertEqual(len(result["candidates"][0]["matches"]), 2)

    def test_run_deduplicates_repeated_blocker_snapshots(self):
        blocker = {
            "task_id": "browser-xiaohongshu-0001",
            "platform": "xiaohongshu",
            "url": "https://www.xiaohongshu.com/explore/abcdef0123456789abcdef01",
            "visible_text": "当前笔记暂时无法浏览",
        }
        result = normalize_browser_collection_run(
            {"pages": [blocker, dict(blocker)]},
            captured_at=datetime(2026, 8, 10, 12, tzinfo=timezone.utc),
        )
        self.assertEqual(result["stats"]["blocked_pages"], 2)
        self.assertEqual(result["stats"]["unique_blockers"], 1)
        self.assertEqual(len(result["blockers"]), 1)

    def test_run_records_empty_search_as_completed_not_blocked(self):
        empty = {
            "task_id": "browser-x-0001",
            "platform": "x",
            "url": "https://x.com/search?q=OCS2%20WBC",
            "page_state": "empty_results",
            "visible_text": "No results for OCS2 WBC",
        }
        result = normalize_browser_collection_run(
            {"pages": [empty, dict(empty)]},
            captured_at=datetime(2026, 8, 10, 12, tzinfo=timezone.utc),
        )
        self.assertEqual(result["blockers"], [])
        self.assertEqual(result["stats"]["empty_result_pages"], 2)
        self.assertEqual(result["stats"]["unique_completed_searches"], 1)
        self.assertEqual(result["completed_searches"][0]["state"], "empty_results")

    def test_non_ready_page_cannot_be_normalized_as_content(self):
        with self.assertRaises(BrowserCollectionError):
            normalize_browser_page_capture({
                "platform": "zhihu",
                "url": "https://www.zhihu.com/signin",
                "visible_text": "登录/注册",
                "title": "知乎",
                "query": "WBC",
            })


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
                "referenced_tweets": [{"type": "quoted", "id": "199"}],
                "attachments": {"media_keys": ["m1"]},
                "public_metrics": {"like_count": 7, "reply_count": 2},
                "lang": "en",
                "edit_history_tweet_ids": ["200"],
            }],
            "includes": {
                "users": [{
                    "id": "u1", "username": "WBCExpert", "name": "WBC Expert"
                }, {
                    "id": "u2", "username": "QuotedExpert", "name": "Quoted Expert"
                }],
                "media": [{
                    "media_key": "m1", "type": "photo",
                    "url": "https://pbs.twimg.com/media/example.jpg",
                    "alt_text": "QP diagnostic plot",
                }],
                "tweets": [{
                    "id": "199", "text": "Referenced solver context",
                    "author_id": "u2",
                }],
            },
            "meta": {"newest_id": "200", "result_count": 1},
        }


class PagingXClient:
    def __init__(self, pages):
        self.calls = []
        self.pages = list(pages)

    def get_json(self, path, params):
        self.calls.append((path, dict(params)))
        return self.pages.pop(0)


class FailingXClient:
    def __init__(self, message="synthetic temporary failure"):
        self.calls = []
        self.message = message

    def get_json(self, path, params):
        self.calls.append((path, dict(params)))
        raise XCollectionError(self.message)


def synthetic_x_page(ids, *, newest_id=None, next_token=None):
    payload = {
        "data": [{
            "id": str(post_id),
            "text": f"Synthetic WBC post {post_id}",
            "author_id": "u1",
            "created_at": "2026-08-10T04:00:00Z",
            "conversation_id": str(post_id),
        } for post_id in ids],
        "includes": {"users": [{
            "id": "u1", "username": "WBCExpert", "name": "WBC Expert"
        }]},
        "meta": {"result_count": len(ids)},
    }
    if newest_id is not None:
        payload["meta"]["newest_id"] = str(newest_id)
    if next_token is not None:
        payload["meta"]["next_token"] = next_token
    return payload


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
        self.assertEqual(plan["estimated_post_read_upper_bound"], 10)
        self.assertTrue(
            plan["recovery"]["advance_since_id_only_after_window_complete"]
        )

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
        self.assertTrue(candidate["visual_analysis_pending"])
        self.assertTrue(candidate["full_text_available"])
        self.assertEqual(
            candidate["referenced_posts"][0]["canonical_url"],
            "https://x.com/QuotedExpert/status/199",
        )
        self.assertEqual(
            candidate["referenced_posts"][0]["text"],
            "Referenced solver context",
        )
        self.assertNotIn("X_BEARER_TOKEN", json.dumps(result))

        second_client = FakeXClient()
        collect_x_candidates(
            [query], second_client, previous_state=state, max_posts_per_query=3,
            created_at=datetime(2026, 8, 10, 13, tzinfo=timezone.utc),
        )
        self.assertEqual(second_client.calls[0][1]["since_id"], "200")

    def test_incomplete_page_window_resumes_before_advancing_since_id(self):
        query = {
            "scope_id": "optimization_ik_qp_mpc",
            "domain_hints": ["loco_manipulation_wbc"],
            "query": "humanoid WBC QP infeasible",
        }
        first_client = PagingXClient([
            synthetic_x_page([300, 299], newest_id=300, next_token="page-2")
        ])
        first, first_state = collect_x_candidates(
            [query], first_client, max_posts_per_query=1, max_pages=1,
            created_at=datetime(2026, 8, 10, 12, tzinfo=timezone.utc),
        )
        self.assertEqual(first["query_results"][0]["returned"], 2)
        self.assertTrue(first["query_results"][0]["resume_pending"])
        state_entry = next(iter(first_state["queries"].values()))
        self.assertIsNone(state_entry["newest_id"])
        self.assertEqual(state_entry["pending"]["next_token"], "page-2")

        second_client = PagingXClient([
            synthetic_x_page([298], newest_id=298)
        ])
        second, second_state = collect_x_candidates(
            [query], second_client, previous_state=first_state,
            max_posts_per_query=10, max_pages=1,
            created_at=datetime(2026, 8, 10, 13, tzinfo=timezone.utc),
        )
        self.assertEqual(second_client.calls[0][1]["next_token"], "page-2")
        self.assertTrue(second["query_results"][0]["resumed"])
        self.assertTrue(second["query_results"][0]["complete"])
        completed_state = next(iter(second_state["queries"].values()))
        self.assertEqual(completed_state["newest_id"], "300")
        self.assertNotIn("pending", completed_state)

        third_client = PagingXClient([synthetic_x_page([])])
        collect_x_candidates(
            [query], third_client, previous_state=second_state,
            max_posts_per_query=10,
            created_at=datetime(2026, 8, 10, 14, tzinfo=timezone.utc),
        )
        self.assertEqual(third_client.calls[0][1]["since_id"], "300")

    def test_api_client_retries_rate_limit_without_exposing_token(self):
        calls = []
        sleeps = []

        class FakeResponse:
            def __enter__(self):
                return self

            def __exit__(self, exc_type, exc, traceback):
                return False

            def read(self):
                return b'{"data": []}'

        def opener(api_request, timeout):
            calls.append((api_request, timeout))
            if len(calls) == 1:
                raise error.HTTPError(
                    api_request.full_url, 429, "rate limited",
                    {"Retry-After": "0"}, io.BytesIO(b'{"detail":"slow down"}'),
                )
            return FakeResponse()

        client = XApiClient(
            "synthetic-secret", opener=opener, max_retries=1,
            sleeper=sleeps.append,
        )
        payload = client.get_json("/tweets", {"ids": "1"})
        self.assertEqual(payload, {"data": []})
        self.assertEqual(len(calls), 2)
        self.assertEqual(sleeps, [0.0])
        self.assertNotIn("synthetic-secret", calls[0][0].full_url)

    def test_request_failure_is_recorded_and_pending_cursor_survives(self):
        query = {
            "scope_id": "optimization_ik_qp_mpc",
            "domain_hints": ["loco_manipulation_wbc"],
            "query": "humanoid WBC QP infeasible",
        }
        first_client = PagingXClient([
            synthetic_x_page([300], newest_id=300, next_token="page-2")
        ])
        _, first_state = collect_x_candidates(
            [query], first_client, max_posts_per_query=1, max_pages=1,
            created_at=datetime(2026, 8, 10, 12, tzinfo=timezone.utc),
        )
        failing = FailingXClient()
        result, next_state = collect_x_candidates(
            [query], failing, previous_state=first_state,
            max_posts_per_query=10, max_pages=1,
            created_at=datetime(2026, 8, 10, 13, tzinfo=timezone.utc),
        )
        self.assertEqual(result["stats"]["request_failures"], 1)
        self.assertTrue(result["query_results"][0]["retry_required"])
        state_entry = next(iter(next_state["queries"].values()))
        self.assertEqual(state_entry["pending"]["next_token"], "page-2")
        self.assertIsNone(state_entry["newest_id"])

    def test_completed_historical_window_is_not_billed_twice(self):
        query = {
            "scope_id": "optimization_ik_qp_mpc",
            "domain_hints": ["loco_manipulation_wbc"],
            "query": "humanoid WBC QP infeasible",
        }
        start_time = "2025-01-01T00:00:00Z"
        end_time = "2026-01-01T00:00:00Z"
        client = PagingXClient([synthetic_x_page([200], newest_id=200)])
        _, state = collect_x_candidates(
            [query], client, mode="all", start_time=start_time,
            end_time=end_time,
            created_at=datetime(2026, 8, 10, 12, tzinfo=timezone.utc),
        )
        entry = next(iter(state["queries"].values()))
        self.assertTrue(entry["window_complete"])

        second_client = FailingXClient("must not be called")
        second, _ = collect_x_candidates(
            [query], second_client, mode="all", previous_state=state,
            start_time=start_time, end_time=end_time,
            created_at=datetime(2026, 8, 10, 13, tzinfo=timezone.utc),
        )
        self.assertEqual(second_client.calls, [])
        self.assertTrue(
            second["query_results"][0]["skipped_completed_window"]
        )

    def test_scoped_run_preserves_unselected_query_state(self):
        query = {
            "scope_id": "optimization_ik_qp_mpc",
            "domain_hints": ["loco_manipulation_wbc"],
            "query": "humanoid WBC QP infeasible",
        }
        previous_state = {
            "schema_version": 1,
            "platform": "x",
            "queries": {
                "unselected-query": {
                    "api_query": "G1 sim2real -is:retweet",
                    "newest_id": "123",
                }
            },
        }
        client = PagingXClient([synthetic_x_page([200], newest_id=200)])
        _, state = collect_x_candidates(
            [query], client, previous_state=previous_state,
            created_at=datetime(2026, 8, 10, 12, tzinfo=timezone.utc),
        )
        self.assertIn("unselected-query", state["queries"])
        self.assertEqual(
            state["queries"]["unselected-query"]["newest_id"], "123"
        )


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
