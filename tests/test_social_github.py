from datetime import datetime, timezone
import unittest

from wbc_handbook.social_github import (
    build_github_issue_plan,
    canonicalize_github_issue_url,
    collect_github_issue_candidates,
    merge_github_connector_runs,
    precise_github_issue_locator_url,
)
from wbc_handbook.social import normalize_social_capture, render_engineering_qa_markdown


NOW = datetime(2026, 8, 10, 12, 0, tzinfo=timezone.utc)


def minimal_config():
    return {
        "schema_version": 1,
        "repositories": [
            {"full_name": "org/a", "tags": ["wbc"]},
            {"full_name": "org/b", "tags": ["wbc"]},
            {"full_name": "org/c", "tags": ["simulation"]},
        ],
        "queries": [{
            "scope_id": "optimization_ik_qp_mpc",
            "query": "QP infeasible",
            "repository_tags": ["wbc"],
        }],
        "history_windows": [{
            "window_id": "2025_2026",
            "created": "2025-01-01..2026-12-31",
            "rolling": False,
        }],
    }


class FakeClient:
    def __init__(self):
        self.search_calls = []
        self.comment_calls = []

    def search_issues(self, query, *, page, per_page):
        self.search_calls.append((query, page, per_page))
        if page > 1:
            return {"total_count": 1, "items": []}, {}
        return {
            "total_count": 1,
            "items": [{
                "html_url": "https://github.com/org/a/issues/42?utm_source=test",
                "title": "QP infeasible on floating base",
                "body": "The QP becomes infeasible after contact switching.",
                "number": 42,
                "state": "closed",
                "state_reason": "completed",
                "locked": False,
                "created_at": "2026-08-01T00:00:00Z",
                "updated_at": "2026-08-02T00:00:00Z",
                "closed_at": "2026-08-02T00:00:00Z",
                "comments": 1,
                "comments_url": "https://api.github.com/repos/org/a/issues/42/comments",
                "labels": [{"name": "bug"}],
                "user": {"login": "reporter"},
                "author_association": "NONE",
                "reactions": {"total_count": 3},
            }],
        }, {}

    def list_comments(self, comments_url, *, page, per_page):
        self.comment_calls.append((comments_url, page, per_page))
        if page > 1:
            return [], {}
        return [{
            "id": 99,
            "html_url": "https://github.com/org/a/issues/42#issuecomment-99",
            "body": "Maintainer: normalize the contact Jacobian before rebuilding the QP.",
            "created_at": "2026-08-02T00:00:00Z",
            "updated_at": "2026-08-02T00:00:00Z",
            "user": {"login": "maintainer"},
            "author_association": "MEMBER",
            "reactions": {"+1": 2},
        }], {}


class GithubIssueTests(unittest.TestCase):
    def test_issue_and_comment_urls_keep_stable_original_links(self):
        canonical, repository, number, stable_id = canonicalize_github_issue_url(
            "https://github.com/Org/Repo/issues/42?utm_source=test#issuecomment-9"
        )
        self.assertEqual(canonical, "https://github.com/Org/Repo/issues/42")
        self.assertEqual(repository, "Org/Repo")
        self.assertEqual(number, 42)
        self.assertEqual(stable_id, "org.repo.42")
        self.assertEqual(
            precise_github_issue_locator_url(
                "https://github.com/Org/Repo/issues/42#issuecomment-9"
            ),
            "https://github.com/Org/Repo/issues/42#issuecomment-9",
        )

    def test_plan_batches_repositories_and_date_windows(self):
        plan = build_github_issue_plan(
            minimal_config(), repositories_per_task=1, max_tasks_per_run=10,
            created_at=NOW,
        )
        self.assertEqual(plan["coverage"]["repositories"], 3)
        self.assertEqual(plan["coverage"]["eligible_tasks"], 2)
        self.assertEqual(len(plan["tasks"]), 2)
        self.assertTrue(all("is:issue" in task["search_query"] for task in plan["tasks"]))
        self.assertTrue(all("created:2025-01-01..2026-12-31" in task["search_query"] for task in plan["tasks"]))

    def test_collection_is_resumable_and_skips_unchanged_known_issue(self):
        plan = build_github_issue_plan(
            minimal_config(), repositories_per_task=2, max_tasks_per_run=1,
            per_page=100, created_at=NOW,
        )
        client = FakeClient()
        first, state = collect_github_issue_candidates(
            plan, client, max_issues_per_run=10, max_comments_per_issue=10,
            collected_at=NOW,
        )
        self.assertEqual(len(first["candidates"]), 1)
        candidate = first["candidates"][0]
        self.assertEqual(candidate["canonical_url"], "https://github.com/org/a/issues/42")
        self.assertEqual(
            candidate["selected_comments"][0]["source_url"],
            "https://github.com/org/a/issues/42#issuecomment-99",
        )
        self.assertTrue(candidate["comments_complete"])
        self.assertIn(candidate["canonical_url"], state["known_urls"])

        # Rebuild with an explicit rolling-like refresh of the same task.  The
        # unchanged updated_at/body digest is observed but not emitted again.
        repeated_plan = dict(plan)
        repeated_plan["tasks"] = [dict(plan["tasks"][0])]
        repeated_plan["tasks"][0]["rolling"] = True
        repeated_plan["tasks"][0]["resume_page"] = 1
        second, _ = collect_github_issue_candidates(
            repeated_plan, FakeClient(), previous_state=state,
            max_issues_per_run=10, max_comments_per_issue=10,
            collected_at=datetime(2026, 8, 11, 12, 0, tzinfo=timezone.utc),
        )
        self.assertEqual(second["candidates"], [])

    def test_reviewed_issue_capture_is_issue_evidence_with_exact_comment_link(self):
        source = normalize_social_capture({
            "platform": "github_issue",
            "canonical_url": "https://github.com/org/a/issues/42",
            "query": "QP infeasible",
            "scope_id": "optimization_ik_qp_mpc",
            "domain_hints": ["loco_manipulation_wbc"],
            "title": "浮动基座切换接触后 QP 不可行",
            "summary": "该 Issue 记录了浮动基座机器人在接触切换后求解器不可行，并由维护者回复给出雅可比归一化的排查办法。",
            "wbc_relevance_reason": "直接涉及全身控制求解与接触约束。",
            "captured_at": "2026-08-10T12:00:00+00:00",
            "access_mode": "public_api",
            "author_display": "reporter",
            "engineering_details": {
                "problem_statements": ["接触切换后 QP 不可行。"],
                "environments": ["浮动基座全身控制器。"],
                "symptoms": ["求解器返回 infeasible。"],
                "diagnostics": ["维护者要求检查接触雅可比。"],
                "suspected_causes": ["接触雅可比尺度不一致。"],
                "attempts": [],
                "effective_fixes": ["归一化接触雅可比后重建 QP。"],
                "outcomes": ["原作者确认问题解决。"],
                "limits": ["只验证于该仓库版本。"],
                "safety_notes": [],
            },
            "engineering_qa": [{
                "question_zh": "接触切换后 QP 不可行时如何排查？",
                "answer_zh": "先检查并归一化接触雅可比，再重建二次规划约束。",
                "answer_status": "resolved",
                "source_locator": "维护者评论 @maintainer",
                "source_url": "https://github.com/org/a/issues/42#issuecomment-99",
                "bilingual_terms": [
                    "二次规划（Quadratic Programming, QP）",
                    "雅可比矩阵（Jacobian Matrix）"
                ],
            }],
            "components": ["QP solver"],
            "robot_platforms": [],
        })
        self.assertEqual(source.kind.value, "issue")
        self.assertEqual(source.source_id, "issue.github.org.a.42")
        card = source.metadata["engineering_qa"][0]
        self.assertEqual(card["verification_status"], "issue_candidate")
        self.assertEqual(
            card["source_url"],
            "https://github.com/org/a/issues/42#issuecomment-99",
        )
        report = render_engineering_qa_markdown([source], generated_at=NOW)
        self.assertIn("GitHub Issues", report)
        self.assertIn("#issuecomment-99", report)

    def test_connector_runs_merge_cross_query_duplicates_and_comments(self):
        base = {
            "platform": "github_issue",
            "canonical_url": "https://github.com/org/a/issues/42?x=1",
            "body_text": "QP failure",
            "body_characters": 10,
            "matches": [{"task_signature": "one"}],
            "selected_comments": [],
        }
        other = {
            **base,
            "canonical_url": "https://github.com/org/a/issues/42",
            "body_text": "Longer QP failure report",
            "body_characters": 24,
            "matches": [{"task_signature": "two"}],
        }
        merged = merge_github_connector_runs(
            [{"candidates": [base]}, {"candidates": [other]}],
            comment_runs=[{"issues": [{
                "canonical_url": "https://github.com/org/a/issues/42",
                "comments": [{
                    "comment_id": 99,
                    "text": "Maintainer answer",
                    "source_url": "https://github.com/org/a/issues/42#issuecomment-99",
                }],
            }]}],
            merged_at=NOW,
        )
        self.assertEqual(merged["stats"]["unique_candidates"], 1)
        candidate = merged["candidates"][0]
        self.assertEqual(len(candidate["matches"]), 2)
        self.assertEqual(candidate["body_text"], "Longer QP failure report")
        self.assertEqual(
            candidate["selected_comments"][0]["source_url"],
            "https://github.com/org/a/issues/42#issuecomment-99",
        )


if __name__ == "__main__":
    unittest.main()
