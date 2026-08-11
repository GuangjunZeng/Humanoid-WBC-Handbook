"""Deterministic publication and safety validation."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Dict, Iterable, List, Mapping

from .language import (
    chinese_first_error,
    cjk_character_count,
    normalize_bilingual_terms,
)

from .models import (
    ClaimStatus,
    EngineeringClaim,
    EvidenceRole,
    EvidenceStrength,
    SafetyLevel,
    SourceRecord,
    parse_aware_datetime,
)
from .social_credibility import SocialCredibilityError, normalize_card_credibility


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
        if source.kind.value == "community" or (
            source.kind.value == "issue" and source.metadata.get("platform") == "github_issue"
        ):
            if cjk_character_count(source.title) < 2:
                issues.append(ValidationIssue(
                    "error", "COMMUNITY_TITLE_NOT_CHINESE_FIRST", source.source_id,
                    "community source title must be Chinese-first",
                ))
            if cjk_character_count(source.summary) < 20:
                issues.append(ValidationIssue(
                    "error", "COMMUNITY_SUMMARY_NOT_CHINESE_FIRST", source.source_id,
                    "community source summary must be Chinese-first",
                ))
            cards = source.metadata.get("engineering_qa", [])
            if not isinstance(cards, list):
                issues.append(ValidationIssue(
                    "error", "COMMUNITY_QA_INVALID", source.source_id,
                    "community engineering_qa must be a list",
                ))
                continue
            for index, card in enumerate(cards):
                card_id = f"{source.source_id}#qa-{index + 1}"
                if not isinstance(card, Mapping):
                    issues.append(ValidationIssue(
                        "error", "COMMUNITY_QA_INVALID", card_id,
                        "community engineering Q&A card must be an object",
                    ))
                    continue
                language_error = chinese_first_error(
                    card.get("question_zh"), card.get("answer_zh")
                )
                if language_error:
                    issues.append(ValidationIssue(
                        "error", "COMMUNITY_QA_NOT_CHINESE_FIRST", card_id,
                        language_error,
                    ))
                try:
                    normalize_bilingual_terms(
                        card.get("bilingual_terms"), "bilingual_terms"
                    )
                except ValueError as exc:
                    issues.append(ValidationIssue(
                        "error", "COMMUNITY_QA_BILINGUAL_TERMS_INVALID", card_id,
                        str(exc),
                    ))
                required_credibility_fields = {
                    "problem_id", "problem_title_zh", "credibility", "verification_refs"
                }
                missing = required_credibility_fields - set(card)
                if missing:
                    issues.append(ValidationIssue(
                        "error", "COMMUNITY_CREDIBILITY_MISSING", card_id,
                        "social card lacks canonical credibility fields: "
                        + ", ".join(sorted(missing)),
                    ))
                    continue
                try:
                    normalize_card_credibility(
                        card,
                        scope_id=str(source.metadata.get("scope_id", "unclassified")),
                        source_id=source.source_id,
                        components=source.metadata.get("components", []),
                        engineering_details=source.metadata.get("engineering_details", {}),
                        media_summaries=source.metadata.get("media_summaries", []),
                    )
                except SocialCredibilityError as exc:
                    issues.append(ValidationIssue(
                        "error", "COMMUNITY_CREDIBILITY_INVALID", card_id, str(exc)
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
    for source in source_list:
        cards = source.metadata.get("engineering_qa", [])
        if not isinstance(cards, list):
            continue
        for index, card in enumerate(cards):
            if not isinstance(card, Mapping):
                continue
            for ref in card.get("verification_refs", []):
                if (
                    isinstance(ref, Mapping)
                    and ref.get("source_id")
                    and ref["source_id"] not in source_map
                ):
                    issues.append(ValidationIssue(
                        "error", "UNKNOWN_SOCIAL_VERIFICATION_SOURCE",
                        f"{source.source_id}#qa-{index + 1}",
                        f"verification_refs references unknown source {ref['source_id']}",
                    ))
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
