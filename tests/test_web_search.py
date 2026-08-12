from __future__ import annotations

import json
from dataclasses import replace
from pathlib import Path
import re
import shutil
import tempfile
import unittest

from wbc_handbook.repository import HandbookRepository
from wbc_handbook.models import ClaimStatus
from wbc_handbook.web_search import (
    FORBIDDEN_SEARCH_FIELDS,
    WebSearchError,
    build_web_index,
    collect_web_problems,
    normalize_search_text,
    render_problem_pages,
)


PROJECT_ROOT = Path(__file__).resolve().parents[1]
TRANSLATIONS_DIR = PROJECT_ROOT / "data/locales/en/problems"
EXPECTED_BASELINE_PROBLEMS = 346


class WebSearchTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        repository = HandbookRepository(PROJECT_ROOT / "data")
        cls.sources = repository.load_sources()
        cls.claims = repository.load_claims()
        cls.problems = collect_web_problems(
            cls.sources, cls.claims, translations_dir=TRANSLATIONS_DIR
        )

    def test_every_claim_and_engineering_qa_is_searchable(self):
        qa_count = sum(
            len(source.metadata.get("engineering_qa", []))
            for source in self.sources
            if isinstance(source.metadata.get("engineering_qa", []), list)
        )
        self.assertEqual(len(self.problems), len(self.claims) + qa_count)
        self.assertEqual(len(self.problems), EXPECTED_BASELINE_PROBLEMS)
        self.assertEqual(
            len({problem.problem_id for problem in self.problems}),
            len(self.problems),
        )

    def test_all_answer_statuses_are_preserved_on_detail_pages(self):
        statuses = {
            card["answer_status"]
            for source in self.sources
            for card in source.metadata.get("engineering_qa", [])
        }
        self.assertEqual(
            statuses, {"resolved", "partial", "unresolved", "conflicting"}
        )
        markdown = "\n".join(problem.markdown for problem in self.problems)
        for status in statuses:
            self.assertIn(f"`{status}`", markdown)

    def test_future_draft_claim_is_searchable_at_l1(self):
        draft = replace(self.claims[0], status=ClaimStatus.DRAFT)
        problems = collect_web_problems(self.sources, [draft])
        page = next(problem for problem in problems if problem.problem_id == draft.claim_id)
        self.assertIn("L1 草稿或部分经验", page.markdown)
        self.assertEqual(page.problem_id, draft.claim_id)
        self.assertFalse(page.has_english)

    def test_search_items_do_not_leak_credibility_fields(self):
        for problem in self.problems:
            item = problem.search_item()
            self.assertFalse(FORBIDDEN_SEARCH_FIELDS.intersection(item))
            self.assertEqual(
                set(item),
                {"id", "title", "summary", "keywords", "aliases", "search_text", "url"},
            )
            visible_card_text = json.dumps(
                {"title": item["title"], "summary": item["summary"]},
                ensure_ascii=False,
            ).casefold()
            indexed_text = json.dumps(
                {key: value for key, value in item.items() if key != "url"},
                ensure_ascii=False,
            ).casefold()
            for label in ("可信度", "置信度", "证据状态", "问题状态"):
                self.assertNotIn(label, visible_card_text)
                self.assertNotIn(label, indexed_text)

    def test_chinese_and_english_aliases_share_the_index(self):
        searchable = " ".join(
            " ".join([
                problem.title,
                problem.summary,
                *problem.keywords,
                *problem.aliases,
                problem.search_text,
            ])
            for problem in self.problems
        ).casefold()
        for term in (
            "真机", "实机", "real robot", "hardware",
            "足端打滑", "foot slip",
            "不可行", "infeasible",
            "状态估计漂移", "state estimation drift",
            "observation scale", "action scaling",
        ):
            self.assertIn(term.casefold(), searchable)

    def test_discovery_queries_support_bilingual_problem_phrases(self):
        qp_weight_pages = [
            problem for problem in self.problems
            if "floating_base_weight" in problem.title or "mpc_alpha" in problem.title
        ]
        self.assertTrue(qp_weight_pages)
        for page in qp_weight_pages:
            text = " ".join([*page.aliases, page.search_text]).casefold()
            self.assertIn("qp", text)
            self.assertIn("infeasible", text)
            self.assertIn("不可行", text)

    def test_generic_object_slip_is_not_labeled_as_foot_slip(self):
        object_slip_page = next(
            problem for problem in self.problems
            if "noslip_iterations" in problem.title
        )
        aliases = {normalize_search_text(value) for value in object_slip_page.aliases}
        self.assertNotIn("foot slip", aliases)
        self.assertNotIn("足端打滑", aliases)

    def test_detail_pages_are_chinese_first_and_bilingual(self):
        qa_page = next(
            problem for problem in self.problems
            if problem.problem_id.startswith("community.x.")
        )
        self.assertIn("## 关键术语", qa_page.markdown)
        self.assertRegex(qa_page.markdown, r"[\u4e00-\u9fff]+（[A-Za-z]")
        self.assertIn("## 原始来源", qa_page.markdown)
        self.assertIn("## 可信度与证据状态", qa_page.markdown)
        self.assertIn("[English version]", qa_page.markdown)
        self.assertIn("[中文版]", qa_page.markdown_en)
        self.assertIn("## Credibility and evidence status", qa_page.markdown_en)
        self.assertIn("## Original source", qa_page.markdown_en)
        self.assertRegex(qa_page.markdown_en, r"[A-Za-z]+.*[（(].*[\u4e00-\u9fff]")

    def test_every_translation_is_current_and_both_urls_are_stable(self):
        self.assertEqual(
            len(list(TRANSLATIONS_DIR.glob("*.json"))), len(self.problems)
        )
        for problem in self.problems:
            self.assertTrue(problem.has_english, problem.problem_id)
            self.assertIn("/content/problems/", problem.url)
            self.assertIn("/content/problems/en/", problem.url_en)
            zh_evidence = {
                url for url in re.findall(r"https://[^)>]+", problem.markdown)
                if "/blob/main/content/problems/" not in url
            }
            en_evidence = {
                url for url in re.findall(r"https://[^)>]+", problem.markdown_en)
                if "/blob/main/content/problems/" not in url
            }
            self.assertEqual(zh_evidence, en_evidence, problem.problem_id)

    def test_stale_translation_fingerprint_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            translations = Path(directory) / "translations"
            shutil.copytree(TRANSLATIONS_DIR, translations)
            path = translations / f"{self.problems[0].problem_id}.json"
            record = json.loads(path.read_text(encoding="utf-8"))
            record["source_fingerprint"] = "0" * 64
            path.write_text(
                json.dumps(record, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
                encoding="utf-8",
            )
            with self.assertRaisesRegex(WebSearchError, "is stale"):
                collect_web_problems(
                    self.sources, self.claims, translations_dir=translations
                )

    def test_detail_pages_expose_required_engineering_sections(self):
        for problem in self.problems:
            for marker in (
                "> **当前答案：**",
                "## 关键术语",
                "## 结果",
                "## 限制",
                "## 安全提示",
            ):
                self.assertIn(marker, problem.markdown, problem.problem_id)
            if "## 原始来源" in problem.markdown:
                for marker in (
                    "## 环境",
                    "## 优先排查",
                    "## 图片与图文证据",
                ):
                    self.assertIn(marker, problem.markdown, problem.problem_id)
            else:
                self.assertIn("## 排查与验证", problem.markdown)
                self.assertIn("## 证据", problem.markdown)

    def test_render_and_index_are_deterministic_and_checked(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            pages = root / "problems"
            index = root / "search-index.json"
            first = render_problem_pages(self.problems, pages)
            self.assertEqual(first["written"], len(self.problems) * 2)
            self.assertEqual(first["pages"], len(self.problems) * 2)
            second = render_problem_pages(self.problems, pages)
            self.assertEqual(second["written"], 0)
            render_problem_pages(self.problems, pages, check=True)
            report = build_web_index(self.problems, pages, index)
            self.assertEqual(report["items"], len(self.problems))
            payload = json.loads(index.read_text(encoding="utf-8"))
            self.assertEqual(payload["schema_version"], 2)
            self.assertEqual(
                [item["id"] for item in payload["items"]],
                sorted(item["id"] for item in payload["items"]),
            )
            first_page = pages / Path(self.problems[0].relative_path).name
            first_page.write_text("stale\n", encoding="utf-8")
            with self.assertRaises(WebSearchError):
                render_problem_pages(self.problems, pages, check=True)

    def test_search_index_has_localized_display_fields(self):
        item = self.problems[0].search_item()
        self.assertEqual(set(item["title"]), {"zh", "en"})
        self.assertEqual(set(item["summary"]), {"zh", "en"})
        self.assertEqual(set(item["url"]), {"zh", "en"})
        self.assertIn(normalize_search_text(item["title"]["zh"]), item["search_text"])
        self.assertIn(normalize_search_text(item["title"]["en"]), item["search_text"])

    def test_missing_detail_page_blocks_index_build(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            pages = root / "problems"
            render_problem_pages(self.problems, pages)
            missing = pages / Path(self.problems[0].relative_path).name
            missing.unlink()
            with self.assertRaises(WebSearchError):
                build_web_index(self.problems, pages, root / "search-index.json")

    def test_missing_english_detail_page_blocks_index_build(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            pages = root / "problems"
            render_problem_pages(self.problems, pages)
            missing = pages / "en" / Path(self.problems[0].relative_path_en).name
            missing.unlink()
            with self.assertRaises(WebSearchError):
                build_web_index(self.problems, pages, root / "search-index.json")

    def test_duplicate_problem_id_is_rejected(self):
        with self.assertRaises(WebSearchError):
            collect_web_problems(self.sources, [self.claims[0], self.claims[0]])

    def test_non_github_detail_url_is_rejected(self):
        with self.assertRaises(WebSearchError):
            collect_web_problems(
                self.sources,
                self.claims,
                repository_url="https://example.com/not-github",
            )

    def test_normalization_is_nfkc_and_case_insensitive(self):
        self.assertEqual(normalize_search_text("ＱＰ  InFeasible"), "qp infeasible")


if __name__ == "__main__":
    unittest.main()
