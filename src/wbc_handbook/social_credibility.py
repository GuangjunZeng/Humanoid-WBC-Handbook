"""Rule-based, non-numeric credibility grades for community experience.

These grades describe how much verification an experience has received.  They
never promote a community card into the formal ``EngineeringClaim`` corpus.
"""

from __future__ import annotations

import hashlib
import json
import re
from typing import Any, Dict, Mapping, Optional, Sequence
from urllib.parse import urlparse


HIGH = "可信度很高"
REFERENCE = "值得参考"
VERIFY = "需要实际验证"
CREDIBILITY_GRADES = (HIGH, REFERENCE, VERIFY)

SOURCE_BASES = (
    "primary_cross_checked",
    "maintainer_or_author_confirmed",
    "engineering_practice_record",
    "problem_signal_only",
)
REPRODUCTION_BASES = (
    "independent_reproduction",
    "original_thread_confirmation",
    "steps_and_results_complete",
    "not_reproduced",
)
APPLICABILITY_BASES = (
    "environment_version_match",
    "environment_clear",
    "partially_clear",
    "environment_unknown",
)
VERIFICATION_RELATIONS = (
    "paper",
    "official_documentation",
    "source_code",
    "pull_request",
    "issue",
    "maintainer_confirmation",
    "independent_reproduction",
    "conflict",
)
FORMAL_OR_INDEPENDENT_RELATIONS = {
    "paper",
    "official_documentation",
    "source_code",
    "pull_request",
    "independent_reproduction",
}


class SocialCredibilityError(ValueError):
    """Raised when a social credibility record violates the contract."""


def _text(value: Any, name: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise SocialCredibilityError(f"{name} must be a non-empty string")
    return value.strip()


def _enum(value: Any, allowed: Sequence[str], name: str) -> str:
    normalized = _text(value, name)
    if normalized not in allowed:
        raise SocialCredibilityError(
            f"{name} must be one of {tuple(allowed)}"
        )
    return normalized


def stable_problem_id(
    scope_id: str,
    problem_title_zh: str,
    *,
    components: Sequence[str] = (),
    symptoms: Sequence[str] = (),
    environments: Sequence[str] = (),
) -> str:
    """Create a conservative ID that will not merge unlike environments."""

    signature = {
        "scope_id": scope_id.strip().casefold(),
        "problem_title_zh": re.sub(r"\s+", "", problem_title_zh).casefold(),
        "components": sorted({str(value).strip().casefold() for value in components}),
        "symptoms": sorted({str(value).strip().casefold() for value in symptoms}),
        "environments": sorted({str(value).strip().casefold() for value in environments}),
    }
    digest = hashlib.sha256(
        json.dumps(signature, ensure_ascii=False, sort_keys=True).encode("utf-8")
    ).hexdigest()[:16]
    safe_scope = re.sub(r"[^a-z0-9_]+", "_", scope_id.casefold()).strip("_")
    return f"problem.{safe_scope or 'unclassified'}.{digest}"


def _verification_refs(value: Any) -> list[Dict[str, str]]:
    if value is None:
        return []
    if not isinstance(value, list):
        raise SocialCredibilityError("verification_refs must be a list")
    refs: list[Dict[str, str]] = []
    for index, item in enumerate(value):
        if not isinstance(item, Mapping):
            raise SocialCredibilityError(
                f"verification_refs[{index}] must be an object"
            )
        relation = _enum(
            item.get("relation"), VERIFICATION_RELATIONS,
            f"verification_refs[{index}].relation",
        )
        locator = _text(
            item.get("locator"), f"verification_refs[{index}].locator"
        )
        source_id = item.get("source_id")
        source_url = item.get("source_url")
        if bool(source_id) == bool(source_url):
            raise SocialCredibilityError(
                f"verification_refs[{index}] needs exactly one of source_id/source_url"
            )
        ref = {"relation": relation, "locator": locator}
        if source_id:
            ref["source_id"] = _text(
                source_id, f"verification_refs[{index}].source_id"
            )
        else:
            normalized_url = _text(
                source_url, f"verification_refs[{index}].source_url"
            )
            parsed = urlparse(normalized_url)
            if parsed.scheme not in {"http", "https"} or not parsed.netloc:
                raise SocialCredibilityError(
                    f"verification_refs[{index}].source_url must be absolute HTTP(S)"
                )
            ref["source_url"] = normalized_url
        refs.append(ref)
    return refs


def _high_gate(
    *,
    status: str,
    basis: Mapping[str, Any],
    verification_refs: Sequence[Mapping[str, Any]],
) -> bool:
    if status != "resolved" or basis["conflict_present"]:
        return False
    if basis["applicability"] not in {
        "environment_version_match", "environment_clear"
    }:
        return False
    if basis["visual_evidence_required"] and not basis["visual_evidence_verified"]:
        return False
    relations = {str(value.get("relation")) for value in verification_refs}
    has_exact_support = bool(relations & FORMAL_OR_INDEPENDENT_RELATIONS)
    independently_reproduced = (
        basis["reproduction"] == "independent_reproduction"
        and bool(basis["independent_source_ids"])
    )
    formally_cross_checked = (
        basis["source_basis"] == "primary_cross_checked" and has_exact_support
    )
    return has_exact_support and (independently_reproduced or formally_cross_checked)


def compute_grade(
    *,
    status: str,
    basis: Mapping[str, Any],
    verification_refs: Sequence[Mapping[str, Any]],
) -> tuple[str, str]:
    """Return a deterministic grade and a concise Chinese explanation."""

    if _high_gate(status=status, basis=basis, verification_refs=verification_refs):
        return HIGH, "问题已闭环、环境明确且无冲突，并有正式资料或独立复现的精确引用。"
    reasons = []
    if status in {"unresolved", "conflicting"}:
        reasons.append("解答尚未闭环或存在冲突")
    if basis["conflict_present"]:
        reasons.append("来源结论存在未解决冲突")
    if basis["source_basis"] == "problem_signal_only":
        reasons.append("当前仅形成问题线索")
    if basis["reproduction"] == "not_reproduced":
        reasons.append("尚未形成可核对的复现记录")
    if basis["applicability"] == "environment_unknown":
        reasons.append("适用环境未知")
    if basis["visual_evidence_required"] and not basis["visual_evidence_verified"]:
        reasons.append("关键图片尚未完成分析")
    if reasons:
        return VERIFY, "；".join(dict.fromkeys(reasons)) + "。"
    reference_ready = (
        status in {"resolved", "partial"}
        and basis["source_basis"] != "problem_signal_only"
        and basis["reproduction"] != "not_reproduced"
        and basis["applicability"] != "environment_unknown"
    )
    if reference_ready:
        return REFERENCE, "环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。"
    return VERIFY, "现有记录可作为排查入口，使用前仍需在目标环境中核对。"


def normalize_card_credibility(
    card: Mapping[str, Any],
    *,
    scope_id: str,
    source_id: str,
    components: Sequence[str] = (),
    engineering_details: Optional[Mapping[str, Any]] = None,
    media_summaries: Sequence[str] = (),
) -> Dict[str, Any]:
    """Fill and validate problem identity plus experience credibility fields."""

    normalized = dict(card)
    title = _text(
        normalized.get("problem_title_zh", normalized.get("question_zh")),
        "problem_title_zh",
    )
    details = engineering_details or {}
    problem_id = normalized.get("problem_id")
    if problem_id is None:
        problem_id = stable_problem_id(
            scope_id,
            title,
            components=components,
            symptoms=details.get("symptoms", []),
            environments=details.get("environments", []),
        )
    problem_id = _text(problem_id, "problem_id")
    if not re.fullmatch(r"problem\.[a-z0-9_]+\.[a-z0-9][a-z0-9_.-]{5,80}", problem_id):
        raise SocialCredibilityError("problem_id has an invalid format")

    credibility_value = normalized.get("credibility", {})
    if not isinstance(credibility_value, Mapping):
        raise SocialCredibilityError("credibility must be an object")
    basis_value = credibility_value.get("basis", {})
    if not isinstance(basis_value, Mapping):
        raise SocialCredibilityError("credibility.basis must be an object")
    status = str(normalized.get("answer_status", "unresolved"))
    has_steps_and_result = bool(details.get("attempts")) and bool(
        details.get("effective_fixes") or details.get("outcomes")
    )
    default_source_basis = (
        "problem_signal_only" if status in {"unresolved", "conflicting"}
        else "engineering_practice_record"
    )
    default_reproduction = (
        "steps_and_results_complete" if has_steps_and_result
        else "not_reproduced"
    )
    default_applicability = (
        "environment_clear" if details.get("environments")
        else "partially_clear" if normalized.get("applicability")
        else "environment_unknown"
    )
    independent_ids_value = basis_value.get("independent_source_ids", [])
    if not isinstance(independent_ids_value, list):
        raise SocialCredibilityError(
            "credibility.basis.independent_source_ids must be a list"
        )
    independent_ids = list(dict.fromkeys(
        _text(value, "credibility.basis.independent_source_ids[]")
        for value in independent_ids_value
        if value != source_id
    ))
    conflict = basis_value.get("conflict_present", status == "conflicting")
    if not isinstance(conflict, bool):
        raise SocialCredibilityError("credibility.basis.conflict_present must be boolean")
    visual_required = basis_value.get("visual_evidence_required", False)
    visual_verified = basis_value.get(
        "visual_evidence_verified", bool(media_summaries)
    )
    if not isinstance(visual_required, bool) or not isinstance(visual_verified, bool):
        raise SocialCredibilityError(
            "credibility.basis visual evidence flags must be boolean"
        )
    basis = {
        "source_basis": _enum(
            basis_value.get("source_basis", default_source_basis),
            SOURCE_BASES,
            "credibility.basis.source_basis",
        ),
        "reproduction": _enum(
            basis_value.get("reproduction", default_reproduction),
            REPRODUCTION_BASES,
            "credibility.basis.reproduction",
        ),
        "applicability": _enum(
            basis_value.get("applicability", default_applicability),
            APPLICABILITY_BASES,
            "credibility.basis.applicability",
        ),
        "independent_source_ids": independent_ids,
        "conflict_present": conflict,
        "visual_evidence_required": visual_required,
        "visual_evidence_verified": visual_verified,
    }
    refs = _verification_refs(normalized.get("verification_refs"))
    computed, default_rationale = compute_grade(
        status=status, basis=basis, verification_refs=refs
    )
    supplied_computed = credibility_value.get("computed_grade")
    if supplied_computed is not None and supplied_computed != computed:
        raise SocialCredibilityError(
            "credibility.computed_grade does not match the rule result"
        )
    final = _enum(
        credibility_value.get("final_grade", computed),
        CREDIBILITY_GRADES,
        "credibility.final_grade",
    )
    override = credibility_value.get("override_rationale_zh")
    if final != computed:
        override = _text(override, "credibility.override_rationale_zh")
    elif override is not None:
        override = _text(override, "credibility.override_rationale_zh")
    if final == HIGH and not _high_gate(
        status=status, basis=basis, verification_refs=refs
    ):
        raise SocialCredibilityError(
            "可信度很高 requires exact formal verification or independent reproduction"
        )
    rationale = _text(
        credibility_value.get("rationale_zh", default_rationale),
        "credibility.rationale_zh",
    )
    credibility = {
        "computed_grade": computed,
        "final_grade": final,
        "rationale_zh": rationale,
        "basis": basis,
    }
    if override is not None:
        credibility["override_rationale_zh"] = override
    normalized.update({
        "problem_id": problem_id,
        "problem_title_zh": title,
        "credibility": credibility,
        "verification_refs": refs,
    })
    return normalized


def aggregate_problem_credibility(
    cards: Sequence[Mapping[str, Any]],
) -> Dict[str, str]:
    """Compute the visible problem-level grade from all experience cards."""

    conflicts = any(
        card.get("answer_status") == "conflicting"
        or bool(card.get("credibility", {}).get("basis", {}).get("conflict_present"))
        for card in cards
    )
    grades = [
        card.get("credibility", {}).get("final_grade", VERIFY) for card in cards
    ]
    if conflicts:
        return {
            "final_grade": VERIFY,
            "rationale_zh": "不同来源存在尚未解决的冲突，全部经验继续展示并等待目标环境验证。",
        }
    if HIGH in grades:
        return {
            "final_grade": HIGH,
            "rationale_zh": "至少一条经验已有正式资料或独立复现支持，且当前没有未解决冲突。",
        }
    if REFERENCE in grades:
        return {
            "final_grade": REFERENCE,
            "rationale_zh": "至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。",
        }
    return {
        "final_grade": VERIFY,
        "rationale_zh": "现有来源主要提供问题线索或待复现经验，建议在目标系统中逐项核对。",
    }
