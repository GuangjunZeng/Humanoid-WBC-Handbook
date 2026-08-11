import unittest

from wbc_handbook.social_credibility import (
    HIGH,
    REFERENCE,
    VERIFY,
    SocialCredibilityError,
    aggregate_problem_credibility,
    normalize_card_credibility,
)


def card(status="resolved", credibility=None, verification_refs=None):
    value = {
        "question_zh": "QP 求解器出现不可行时应如何定位？",
        "answer_zh": "先固定接触集合，再检查约束残差与优先级。",
        "answer_status": status,
    }
    if credibility is not None:
        value["credibility"] = credibility
    if verification_refs is not None:
        value["verification_refs"] = verification_refs
    return value


def normalize(value, environment="Ubuntu 22.04 + OSQP 1.0"):
    return normalize_card_credibility(
        value,
        scope_id="optimization_ik_qp_mpc",
        source_id="issue.github.example.repo.1",
        components=["OSQP"],
        engineering_details={
            "environments": [environment] if environment else [],
            "symptoms": ["QP infeasible"],
            "attempts": ["检查约束残差"],
            "outcomes": ["恢复求解"],
        },
    )


class SocialCredibilityTests(unittest.TestCase):
    def test_formal_cross_check_can_reach_high_grade(self):
        normalized = normalize(card(
            credibility={"basis": {
                "source_basis": "primary_cross_checked",
                "reproduction": "steps_and_results_complete",
                "applicability": "environment_version_match",
                "independent_source_ids": [],
                "conflict_present": False,
            }},
            verification_refs=[{
                "relation": "official_documentation",
                "source_url": "https://osqp.org/docs/interfaces/status_values.html",
                "locator": "Solver status: primal infeasible",
            }],
        ))
        self.assertEqual(normalized["credibility"]["computed_grade"], HIGH)
        self.assertEqual(normalized["credibility"]["final_grade"], HIGH)

    def test_complete_engineering_record_is_reference_worthy(self):
        normalized = normalize(card())
        self.assertEqual(normalized["credibility"]["computed_grade"], REFERENCE)

    def test_unresolved_conflict_and_unverified_image_require_validation(self):
        unresolved = normalize(card(status="unresolved"))
        self.assertEqual(unresolved["credibility"]["final_grade"], VERIFY)
        conflicting = normalize(card(
            status="conflicting",
            credibility={"basis": {"conflict_present": True}},
        ))
        self.assertEqual(conflicting["credibility"]["final_grade"], VERIFY)
        visual = normalize(card(credibility={"basis": {
            "visual_evidence_required": True,
            "visual_evidence_verified": False,
        }}))
        self.assertEqual(visual["credibility"]["final_grade"], VERIFY)

    def test_override_requires_reason_and_cannot_bypass_high_gate(self):
        high_input = card(
            credibility={
                "basis": {
                    "source_basis": "primary_cross_checked",
                    "reproduction": "steps_and_results_complete",
                    "applicability": "environment_version_match",
                },
                "final_grade": REFERENCE,
            },
            verification_refs=[{
                "relation": "source_code",
                "source_url": "https://github.com/osqp/osqp/blob/master/include/public/osqp_api_constants.h",
                "locator": "solver status constants",
            }],
        )
        with self.assertRaises(SocialCredibilityError):
            normalize(high_input)
        high_input["credibility"]["override_rationale_zh"] = "目标硬件尚未完成回归测试，审阅者保守降级。"
        normalized = normalize(high_input)
        self.assertEqual(normalized["credibility"]["final_grade"], REFERENCE)

        invalid_upgrade = card(credibility={
            "final_grade": HIGH,
            "override_rationale_zh": "希望直接采用。",
        })
        with self.assertRaises(SocialCredibilityError):
            normalize(invalid_upgrade)

    def test_hardware_safety_note_does_not_replace_independent_verification(self):
        normalized = normalize_card_credibility(
            card(),
            scope_id="safety_faults_limits",
            source_id="community.x.100",
            components=["EtherCAT"],
            engineering_details={
                "environments": ["实机液压人形机器人"],
                "symptoms": ["关节速度突增"],
                "attempts": ["降低增益"],
                "outcomes": ["暂时恢复"],
                "safety_notes": ["需要急停监护"],
            },
        )
        self.assertEqual(normalized["credibility"]["final_grade"], REFERENCE)

    def test_problem_id_does_not_merge_different_robot_environments(self):
        first = normalize(card(), environment="Unitree H1 + Ubuntu 22.04")
        second = normalize(card(), environment="Talos + Ubuntu 20.04")
        self.assertNotEqual(first["problem_id"], second["problem_id"])

    def test_problem_grade_exposes_conflict_instead_of_hiding_sources(self):
        first = normalize(card())
        second = normalize(card(
            status="conflicting",
            credibility={"basis": {"conflict_present": True}},
        ))
        aggregate = aggregate_problem_credibility([first, second])
        self.assertEqual(aggregate["final_grade"], VERIFY)


if __name__ == "__main__":
    unittest.main()
