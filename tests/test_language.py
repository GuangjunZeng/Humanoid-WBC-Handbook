from __future__ import annotations

import unittest

from wbc_handbook.importer import normalize_manual_source
from wbc_handbook.language import (
    chinese_first_error,
    infer_bilingual_terms,
    normalize_bilingual_terms,
)
from wbc_handbook.validator import validate_sources


class ChineseFirstLanguageTests(unittest.TestCase):
    def test_infers_canonical_chinese_english_terms(self):
        terms = infer_bilingual_terms(
            "WBC 里的 QP 接触约束与 sim-to-real 迁移需要分别验收。"
        )
        self.assertIn("全身控制（Whole-Body Control, WBC）", terms)
        self.assertIn("二次规划（Quadratic Programming, QP）", terms)
        self.assertIn("仿真到现实（Simulation-to-Real, Sim2Real）", terms)

    def test_chinese_first_requires_substantive_chinese_question_and_answer(self):
        self.assertIsNone(chinese_first_error(
            "全身控制求解失败时先检查什么？",
            "先核对接触约束和关节力矩限幅，再根据求解器日志缩小冲突范围。",
        ))
        self.assertIsNotNone(chinese_first_error(
            "How to debug WBC?",
            "Check the QP solver and contact constraints before deployment.",
        ))

    def test_explicit_terms_must_use_chinese_parenthesized_english(self):
        self.assertEqual(
            normalize_bilingual_terms(["状态估计（State Estimation）"]),
            ["状态估计（State Estimation）"],
        )
        with self.assertRaises(ValueError):
            normalize_bilingual_terms(["State Estimation"])

    def test_repository_validation_requires_bilingual_terms_on_community_cards(self):
        source = normalize_manual_source({
            "source_id": "community.x.123456789",
            "kind": "community",
            "title": "中文社区工程记录",
            "canonical_url": "https://x.com/synthetic/status/123456789",
            "captured_at": "2026-08-10T12:00:00+08:00",
            "summary": "这是一条用于验证中文优先和双语术语数据门槛的合成社区来源摘要。",
            "access_mode": "manual_import",
            "metadata": {
                "engineering_qa": [{
                    "question_zh": "全身控制求解失败时应该先检查什么？",
                    "answer_zh": "先核对接触约束、关节力矩限幅和权重尺度，再根据求解器日志定位冲突。",
                }],
            },
        })
        codes = {issue.code for issue in validate_sources([source])}
        self.assertIn("COMMUNITY_QA_BILINGUAL_TERMS_INVALID", codes)
