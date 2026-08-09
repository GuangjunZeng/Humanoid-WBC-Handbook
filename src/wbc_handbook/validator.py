"""Deterministic publication and safety validation."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Dict, Iterable, List

from .models import (
    ClaimStatus,
    EngineeringClaim,
    EvidenceRole,
    EvidenceStrength,
    SafetyLevel,
    SourceRecord,
    parse_aware_datetime,
)


@dataclass(frozen=True)
class ValidationIssue:
    severity: str
    code: str
    record_id: str
    message: str

    def to_dict(self) -> dict:
        return {
            "severity": self.severity,
            "code": self.code,
            "record_id": self.record_id,
            "message": self.message,
        }


def validate_sources(sources: Iterable[SourceRecord]) -> List[ValidationIssue]:
    issues: List[ValidationIssue] = []
    seen = set()
    for source in sources:
        if source.source_id in seen:
            issues.append(ValidationIssue(
                "error", "DUPLICATE_SOURCE_ID", source.source_id, "source ID is duplicated"
            ))
        seen.add(source.source_id)
        if source.excerpt and not source.license:
            issues.append(ValidationIssue(
                "warning", "EXCERPT_LICENSE_UNKNOWN", source.source_id,
                "stored excerpt has no recorded source license; review quotation rights",
            ))
    return issues


def validate_claim(
    claim: EngineeringClaim,
    sources: Dict[str, SourceRecord],
    now: datetime = None,
) -> List[ValidationIssue]:
    issues: List[ValidationIssue] = []
    now = now or datetime.now(timezone.utc)
    support = []

    for link in claim.evidence:
        if link.source_id not in sources:
            issues.append(ValidationIssue(
                "error", "UNKNOWN_EVIDENCE_SOURCE", claim.claim_id,
                f"evidence references unknown source {link.source_id}",
            ))
        if link.role == EvidenceRole.SUPPORT:
            support.append(link)

    if not support:
        issues.append(ValidationIssue(
            "error", "NO_SUPPORTING_EVIDENCE", claim.claim_id,
            "claim has no evidence with role=support",
        ))
    elif all(link.strength == EvidenceStrength.COMMUNITY for link in support):
        issues.append(ValidationIssue(
            "error", "COMMUNITY_ONLY_SUPPORT", claim.claim_id,
            "community evidence requires independent primary or secondary support",
        ))

    if claim.status == ClaimStatus.REVIEWED and claim.confidence < 0.2:
        issues.append(ValidationIssue(
            "warning", "LOW_CONFIDENCE_REVIEWED", claim.claim_id,
            "reviewed claim has very low confidence; consider draft status",
        ))

    reviewed_at = parse_aware_datetime(claim.reviewed_at, "reviewed_at")
    review_due_at = parse_aware_datetime(claim.review_due_at, "review_due_at")
    if review_due_at <= reviewed_at:
        issues.append(ValidationIssue(
            "error", "INVALID_REVIEW_WINDOW", claim.claim_id,
            "review_due_at must be later than reviewed_at",
        ))
    if review_due_at < now:
        issues.append(ValidationIssue(
            "warning", "REVIEW_OVERDUE", claim.claim_id, "claim review date has passed"
        ))

    if claim.safety_level == SafetyLevel.HARDWARE_CRITICAL:
        if claim.safety_case is None or not claim.safety_case.complete():
            issues.append(ValidationIssue(
                "error", "INCOMPLETE_HARDWARE_SAFETY_CASE", claim.claim_id,
                "hardware-critical claim lacks a complete simulation-first safety case",
            ))
    elif claim.safety_case is not None:
        issues.append(ValidationIssue(
            "warning", "UNEXPECTED_SAFETY_CASE", claim.claim_id,
            "safety case is present but safety_level is not hardware_critical",
        ))

    return issues


def validate_repository(
    sources: Iterable[SourceRecord], claims: Iterable[EngineeringClaim]
) -> List[ValidationIssue]:
    source_list = list(sources)
    claim_list = list(claims)
    issues = validate_sources(source_list)
    source_map = {source.source_id: source for source in source_list}
    seen_claims = set()
    for claim in claim_list:
        if claim.claim_id in seen_claims:
            issues.append(ValidationIssue(
                "error", "DUPLICATE_CLAIM_ID", claim.claim_id, "claim ID is duplicated"
            ))
        seen_claims.add(claim.claim_id)
        issues.extend(validate_claim(claim, source_map))
    return issues


def has_errors(issues: Iterable[ValidationIssue]) -> bool:
    return any(issue.severity == "error" for issue in issues)
