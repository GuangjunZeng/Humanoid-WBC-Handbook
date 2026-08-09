"""Canonical, dependency-free domain models."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import datetime
from enum import Enum
import re
from typing import Any, Dict, List, Mapping, Optional
from urllib.parse import urlparse


ID_PATTERN = re.compile(r"^[a-z0-9][a-z0-9._-]{2,127}$")


class ModelError(ValueError):
    """Raised when a canonical record violates the data contract."""


class StringEnum(str, Enum):
    def __str__(self) -> str:
        return self.value


class SourceKind(StringEnum):
    PAPER = "paper"
    OFFICIAL_DOC = "official_doc"
    SOURCE_CODE = "source_code"
    ISSUE = "issue"
    RELEASE = "release"
    PROJECT_PAGE = "project_page"
    VIDEO = "video"
    COMMUNITY = "community"


class AccessMode(StringEnum):
    PUBLIC_WEB = "public_web"
    PUBLIC_API = "public_api"
    MANUAL_IMPORT = "manual_import"
    AUTHORIZED_VISIBLE_BROWSER = "authorized_visible_browser"


class EvidenceRole(StringEnum):
    SUPPORT = "support"
    CONFLICT = "conflict"
    SUPERSEDE = "supersede"
    CONTEXT = "context"


class EvidenceStrength(StringEnum):
    PRIMARY = "primary"
    SECONDARY = "secondary"
    COMMUNITY = "community"


class ClaimStatus(StringEnum):
    DRAFT = "draft"
    REVIEWED = "reviewed"


class SafetyLevel(StringEnum):
    INFORMATIONAL = "informational"
    CAUTION = "caution"
    HARDWARE_CRITICAL = "hardware_critical"


class Domain(StringEnum):
    TRAINING_DATA_RETARGETING = "training_data_retargeting"
    UNIVERSAL_TRACKING_TELEOPERATION = "universal_tracking_teleoperation"
    LOCOMOTION_TERRAIN = "locomotion_terrain"
    LOCO_MANIPULATION_WBC = "loco_manipulation_wbc"
    SPORTS = "sports"
    MOTION_GENERATION = "motion_generation"
    RECOVERY_SAFETY_FORCE = "recovery_safety_force"


def _require_keys(data: Mapping[str, Any], allowed: set, required: set, name: str) -> None:
    missing = required - set(data)
    unknown = set(data) - allowed
    if missing:
        raise ModelError(f"{name} missing fields: {', '.join(sorted(missing))}")
    if unknown:
        raise ModelError(f"{name} unknown fields: {', '.join(sorted(unknown))}")


def _validate_id(value: str, name: str) -> None:
    if not isinstance(value, str) or not ID_PATTERN.fullmatch(value):
        raise ModelError(f"{name} must match {ID_PATTERN.pattern}")


def _validate_url(value: str) -> None:
    parsed = urlparse(value)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        raise ModelError("canonical_url must be an absolute HTTP(S) URL")


def parse_aware_datetime(value: str, name: str) -> datetime:
    if not isinstance(value, str):
        raise ModelError(f"{name} must be an ISO 8601 string")
    normalized = value[:-1] + "+00:00" if value.endswith("Z") else value
    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError as exc:
        raise ModelError(f"{name} must be ISO 8601: {value}") from exc
    if parsed.tzinfo is None:
        raise ModelError(f"{name} must include a timezone")
    return parsed


@dataclass(frozen=True)
class SourceRecord:
    source_id: str
    kind: SourceKind
    title: str
    canonical_url: str
    captured_at: str
    summary: str
    access_mode: AccessMode
    content_sha256: str
    authors: List[str] = field(default_factory=list)
    publisher: Optional[str] = None
    published_at: Optional[str] = None
    version: Optional[str] = None
    license: Optional[str] = None
    excerpt: Optional[str] = None
    attention: Dict[str, float] = field(default_factory=dict)
    metadata: Dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        _validate_id(self.source_id, "source_id")
        _validate_url(self.canonical_url)
        parse_aware_datetime(self.captured_at, "captured_at")
        if self.published_at:
            parse_aware_datetime(self.published_at, "published_at")
        if not self.title.strip() or not self.summary.strip():
            raise ModelError("title and summary must be non-empty")
        if not re.fullmatch(r"[0-9a-f]{64}", self.content_sha256):
            raise ModelError("content_sha256 must be a lowercase SHA-256 hex digest")
        if self.excerpt and len(self.excerpt) > 1000:
            raise ModelError("excerpt exceeds the 1000-character storage limit")
        if any(not isinstance(value, (int, float)) for value in self.attention.values()):
            raise ModelError("attention values must be numeric")
        if any(value < 0 for value in self.attention.values()):
            raise ModelError("attention values cannot be negative")

    @classmethod
    def from_dict(cls, data: Mapping[str, Any]) -> "SourceRecord":
        allowed = {
            "source_id", "kind", "title", "canonical_url", "captured_at", "summary",
            "access_mode", "content_sha256", "authors", "publisher", "published_at",
            "version", "license", "excerpt", "attention", "metadata",
        }
        required = {
            "source_id", "kind", "title", "canonical_url", "captured_at", "summary",
            "access_mode", "content_sha256",
        }
        _require_keys(data, allowed, required, "SourceRecord")
        payload = dict(data)
        payload["kind"] = SourceKind(payload["kind"])
        payload["access_mode"] = AccessMode(payload["access_mode"])
        return cls(**payload)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class EvidenceLink:
    source_id: str
    role: EvidenceRole
    strength: EvidenceStrength
    locator: str
    note: str = ""

    def __post_init__(self) -> None:
        _validate_id(self.source_id, "evidence.source_id")
        if not self.locator.strip():
            raise ModelError("evidence locator must be non-empty")

    @classmethod
    def from_dict(cls, data: Mapping[str, Any]) -> "EvidenceLink":
        allowed = {"source_id", "role", "strength", "locator", "note"}
        required = {"source_id", "role", "strength", "locator"}
        _require_keys(data, allowed, required, "EvidenceLink")
        payload = dict(data)
        payload["role"] = EvidenceRole(payload["role"])
        payload["strength"] = EvidenceStrength(payload["strength"])
        return cls(**payload)


@dataclass(frozen=True)
class Applicability:
    robots: List[str] = field(default_factory=list)
    simulators: List[str] = field(default_factory=list)
    controllers: List[str] = field(default_factory=list)
    environments: List[str] = field(default_factory=list)
    assumptions: List[str] = field(default_factory=list)

    @classmethod
    def from_dict(cls, data: Mapping[str, Any]) -> "Applicability":
        allowed = {"robots", "simulators", "controllers", "environments", "assumptions"}
        _require_keys(data, allowed, set(), "Applicability")
        return cls(**dict(data))


@dataclass(frozen=True)
class SafetyCase:
    simulation_validated: bool
    command_limits: str
    emergency_stop: str
    protective_controls: str
    robot_specific_warning: str
    staged_deployment: str

    @classmethod
    def from_dict(cls, data: Mapping[str, Any]) -> "SafetyCase":
        required = {
            "simulation_validated", "command_limits", "emergency_stop",
            "protective_controls", "robot_specific_warning", "staged_deployment",
        }
        _require_keys(data, required, required, "SafetyCase")
        return cls(**dict(data))

    def complete(self) -> bool:
        return self.simulation_validated and all(
            value.strip()
            for value in (
                self.command_limits,
                self.emergency_stop,
                self.protective_controls,
                self.robot_specific_warning,
                self.staged_deployment,
            )
        )


@dataclass(frozen=True)
class EngineeringClaim:
    claim_id: str
    domain: Domain
    question: str
    statement: str
    status: ClaimStatus
    confidence: float
    confidence_rationale: str
    applicability: Applicability
    evidence: List[EvidenceLink]
    safety_level: SafetyLevel
    reviewed_at: str
    review_due_at: str
    safety_case: Optional[SafetyCase] = None
    tags: List[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        _validate_id(self.claim_id, "claim_id")
        if not self.question.strip() or not self.statement.strip():
            raise ModelError("question and statement must be non-empty")
        if not 0.0 <= self.confidence <= 1.0:
            raise ModelError("confidence must be in [0, 1]")
        if not self.confidence_rationale.strip():
            raise ModelError("confidence_rationale must be non-empty")
        parse_aware_datetime(self.reviewed_at, "reviewed_at")
        parse_aware_datetime(self.review_due_at, "review_due_at")
        if not self.evidence:
            raise ModelError("at least one evidence link is required")

    @classmethod
    def from_dict(cls, data: Mapping[str, Any]) -> "EngineeringClaim":
        allowed = {
            "claim_id", "domain", "question", "statement", "status", "confidence",
            "confidence_rationale", "applicability", "evidence", "safety_level",
            "reviewed_at", "review_due_at", "safety_case", "tags",
        }
        required = allowed - {"safety_case", "tags"}
        _require_keys(data, allowed, required, "EngineeringClaim")
        payload = dict(data)
        payload["domain"] = Domain(payload["domain"])
        payload["status"] = ClaimStatus(payload["status"])
        payload["applicability"] = Applicability.from_dict(payload["applicability"])
        payload["evidence"] = [EvidenceLink.from_dict(item) for item in payload["evidence"]]
        payload["safety_level"] = SafetyLevel(payload["safety_level"])
        if payload.get("safety_case") is not None:
            payload["safety_case"] = SafetyCase.from_dict(payload["safety_case"])
        return cls(**payload)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)
