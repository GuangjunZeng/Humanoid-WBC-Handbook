import json
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]


class SocialCorpusAcceptanceTests(unittest.TestCase):
    def test_all_reviewed_experiences_have_grade_reason_and_original_link(self):
        cards = []
        for path in sorted((ROOT / "data" / "sources").glob("*.json")):
            payload = json.loads(path.read_text(encoding="utf-8"))
            cards.extend(payload.get("metadata", {}).get("engineering_qa", []))
        self.assertGreaterEqual(len(cards), 64)
        for card in cards:
            self.assertTrue(card["problem_id"].startswith("problem."))
            self.assertTrue(card["problem_title_zh"])
            self.assertIn(
                card["credibility"]["final_grade"],
                {"可信度很高", "值得参考", "需要实际验证"},
            )
            self.assertTrue(card["credibility"]["rationale_zh"])
            self.assertTrue(card["source_url"].startswith("https://"))
        report = (ROOT / "content" / "social-engineering-candidates.md").read_text(
            encoding="utf-8"
        )
        self.assertEqual(report.count("**经验 "), len(cards))
        self.assertEqual(report.count("- 原帖/精确回复："), len(cards))

    def test_minimal_inventory_is_complete_and_pending_links_are_exposed(self):
        inventory = json.loads(
            (ROOT / "data" / "social-candidate-index.json").read_text(encoding="utf-8")
        )
        stats = inventory["stats"]
        self.assertEqual(
            stats["reviewed"] + stats["technical_pending"] + stats["excluded"],
            stats["unique_candidates"],
        )
        allowed = {
            "candidate_id", "canonical_url", "title", "platform", "scope_ids",
            "queries", "first_seen_at", "last_seen_at", "triage_status",
            "triage_reason_zh", "related_problem_ids",
        }
        for item in inventory["candidates"]:
            self.assertEqual(set(item), allowed)
            if item["triage_status"] == "excluded":
                self.assertTrue(item["triage_reason_zh"])
        pending_text = "\n".join(
            path.read_text(encoding="utf-8")
            for path in (ROOT / "content" / "social-engineering-pending").glob("*.md")
        )
        for item in inventory["candidates"]:
            if item["triage_status"] == "technical_pending":
                self.assertIn(item["canonical_url"], pending_text)
        github_candidates = sum(
            item["platform"] == "github_issue" for item in inventory["candidates"]
        )
        self.assertEqual(github_candidates, 1067)

    def test_generated_frontier_exposes_every_migrated_topic(self):
        report = (ROOT / "content" / "social-query-frontier.md").read_text(
            encoding="utf-8"
        )
        total_match = re.search(r"^- 主题总数：(\d+)$", report, re.MULTILINE)
        self.assertIsNotNone(total_match)
        expected = int(total_match.group(1))
        self.assertGreaterEqual(expected, 3568)
        topic_headings = sum(
            line.startswith("## ") and line[3:4].isdigit()
            for line in report.splitlines()
        )
        self.assertEqual(topic_headings, expected)

    def test_user_visible_social_docs_use_only_constructive_grade_names(self):
        paths = [
            ROOT / "content" / "social-engineering-candidates.md",
            ROOT / "docs" / "social-collection.md",
            ROOT / "docs" / "social-discovery-evolution.md",
            ROOT / "docs" / "social-credibility-and-inventory.md",
        ]
        text = "\n".join(path.read_text(encoding="utf-8") for path in paths)
        self.assertNotIn("可信度很低", text)
        self.assertNotIn("低可信", text)


if __name__ == "__main__":
    unittest.main()
