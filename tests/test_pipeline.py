from __future__ import annotations

from datetime import datetime, timezone
import json
from pathlib import Path
import uuid
import unittest

from wbc_handbook.answer import answer, render_markdown
from wbc_handbook.importer import normalize_manual_source
from wbc_handbook.index import build_index
from wbc_handbook.models import EngineeringClaim, SourceRecord
from wbc_handbook.repository import HandbookRepository, RepositoryError
from wbc_handbook.validator import validate_claim


PROJECT_ROOT = Path(__file__).resolve().parents[1]
TEST_RUNS = PROJECT_ROOT / "var" / "test-runs"


def run_directory() -> Path:
    path = TEST_RUNS / str(uuid.uuid4())
    path.mkdir(parents=True, exist_ok=False)
    return path


def primary_source(source_id="paper.synthetic.balance") -> SourceRecord:
    return SourceRecord.from_dict({
        "source_id": source_id,
        "kind": "paper",
        "title": "Synthetic balance-control study",
        "canonical_url": "https://example.org/synthetic-balance-study",
        "captured_at": "2026-08-10T12:00:00+08:00",
        "summary": "Synthetic test evidence, not real engineering guidance.",
        "access_mode": "public_web",
        "content_sha256": "1" * 64,
        "authors": ["Test Author"],
        "license": "Synthetic test data",
        "metadata": {"synthetic": True},
    })


def claim_payload(source_id="paper.synthetic.balance", **overrides):
    payload = {
        "claim_id": "locomotion.synthetic.push-recovery",
        "domain": "locomotion_terrain",
        "question": "How should push recovery be evaluated?",
        "statement": "Evaluate recovery under a declared disturbance envelope and report failures.",
        "status": "reviewed",
        "confidence": 0.8,
        "confidence_rationale": "Synthetic primary evidence exists for the test contract.",
        "applicability": {
            "robots": ["synthetic-biped"],
            "simulators": ["synthetic-sim"],
            "controllers": ["policy-controller"],
            "environments": ["flat-ground"],
            "assumptions": ["state estimation available"]
        },
        "evidence": [{
            "source_id": source_id,
            "role": "support",
            "strength": "primary",
            "locator": "Synthetic Section 4"
        }],
        "safety_level": "caution",
        "reviewed_at": "2026-08-10T12:00:00+08:00",
        "review_due_at": "2030-08-10T12:00:00+08:00",
        "tags": ["push recovery", "disturbance envelope"]
    }
    payload.update(overrides)
    return payload


class ModelAndValidationTests(unittest.TestCase):
    def test_manual_import_derives_stable_digest(self):
        payload = {
            "source_id": "official.synthetic.guide",
            "kind": "official_doc",
            "title": "Synthetic guide",
            "canonical_url": "https://example.org/guide",
            "captured_at": "2026-08-10T12:00:00+08:00",
            "summary": "Synthetic test record.",
            "access_mode": "manual_import",
        }
        first = normalize_manual_source(payload)
        second = normalize_manual_source(payload)
        self.assertEqual(first.content_sha256, second.content_sha256)
        self.assertEqual(len(first.content_sha256), 64)

    def test_community_only_support_is_blocked(self):
        source = SourceRecord.from_dict({
            **primary_source("community.synthetic.post").to_dict(),
            "kind": "community",
        })
        payload = claim_payload("community.synthetic.post")
        payload["evidence"][0]["strength"] = "community"
        claim = EngineeringClaim.from_dict(payload)
        issues = validate_claim(claim, {source.source_id: source})
        self.assertIn("COMMUNITY_ONLY_SUPPORT", {issue.code for issue in issues})

    def test_hardware_critical_claim_requires_complete_safety_case(self):
        source = primary_source()
        claim = EngineeringClaim.from_dict(claim_payload(safety_level="hardware_critical"))
        issues = validate_claim(claim, {source.source_id: source})
        self.assertIn("INCOMPLETE_HARDWARE_SAFETY_CASE", {issue.code for issue in issues})

    def test_review_due_date_must_follow_review_date(self):
        source = primary_source()
        claim = EngineeringClaim.from_dict(claim_payload(
            review_due_at="2025-08-10T12:00:00+08:00"
        ))
        issues = validate_claim(
            claim,
            {source.source_id: source},
            now=datetime(2026, 8, 10, tzinfo=timezone.utc),
        )
        self.assertIn("INVALID_REVIEW_WINDOW", {issue.code for issue in issues})

    def test_complete_hardware_safety_case_passes_gate(self):
        source = primary_source()
        claim = EngineeringClaim.from_dict(claim_payload(
            safety_level="hardware_critical",
            safety_case={
                "simulation_validated": True,
                "command_limits": "Synthetic bounded commands.",
                "emergency_stop": "Synthetic tested E-stop.",
                "protective_controls": "Synthetic exclusion zone.",
                "robot_specific_warning": "Synthetic robot only.",
                "staged_deployment": "Synthetic low-energy stages."
            }
        ))
        issues = validate_claim(claim, {source.source_id: source})
        self.assertNotIn("INCOMPLETE_HARDWARE_SAFETY_CASE", {issue.code for issue in issues})


class RepositoryAndSearchTests(unittest.TestCase):
    def test_repository_rejects_path_traversal_id(self):
        repository = HandbookRepository(run_directory() / "data")
        with self.assertRaises(RepositoryError):
            repository._target(repository.sources_dir, "../escape")

    def test_reviewed_claim_is_retrieved_with_citation(self):
        root = run_directory()
        source = primary_source()
        claim = EngineeringClaim.from_dict(claim_payload())
        index_path = root / "handbook.sqlite"
        counts = build_index(index_path, [source], [claim])
        self.assertEqual(counts["claims"], 1)

        result = answer(index_path, "push recovery disturbance envelope")
        self.assertEqual(result["claims"][0]["claim_id"], claim.claim_id)
        self.assertEqual(
            result["claims"][0]["citations"][0]["canonical_url"],
            source.canonical_url,
        )
        markdown = render_markdown(result)
        self.assertIn(source.canonical_url, markdown)
        self.assertIn("Safety", markdown)

    def test_zero_result_does_not_synthesize_advice(self):
        root = run_directory()
        index_path = root / "handbook.sqlite"
        build_index(index_path, [primary_source()], [EngineeringClaim.from_dict(claim_payload())])
        result = answer(index_path, "unrelated quantum compiler question")
        self.assertEqual(result["claims"], [])
        self.assertIn("No reviewed claim", render_markdown(result))


if __name__ == "__main__":
    unittest.main()
