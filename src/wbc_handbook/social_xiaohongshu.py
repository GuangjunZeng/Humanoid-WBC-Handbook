"""Manual fallback queue for Xiaohongshu discovery.

Xiaohongshu does not expose a public general-purpose note reader API. This
module remains the fallback when visible-browser collection is blocked. It
automates only query planning, canonical-link validation, deduplication, and
review-state management. The separate ``social_browser`` adapter defines the
finite, user-triggered DOM-extraction contract. Neither module reads cookies,
stores credentials, bypasses access controls, or performs scheduled collection.
"""

from __future__ import annotations

from datetime import datetime, timezone
import hashlib
import re
from typing import Any, Dict, List, Mapping, Optional, Sequence

from .social import SocialCollectionError, build_search_url, canonicalize_social_url


XHS_REVIEW_STATUSES = (
    "pending_manual_review",
    "approved_for_analysis",
    "rejected_irrelevant",
    "unavailable",
)
XHS_DISCOVERY_SOURCES = ("external_search", "manual_share", "manual_platform_search")


class XiaohongshuQueueError(ValueError):
    """Raised when an XHS discovery queue violates the review contract."""


def _non_empty(value: Any, name: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise XiaohongshuQueueError(f"{name} must be a non-empty string")
    return value.strip()


def _created_at(value: Optional[datetime] = None) -> str:
    current = value or datetime.now(timezone.utc).astimezone()
    if current.tzinfo is None:
        raise XiaohongshuQueueError("timestamp must include a timezone")
    return current.isoformat(timespec="seconds")


def _validate_queries(queries: Sequence[Mapping[str, Any]]) -> List[Dict[str, Any]]:
    normalized: List[Dict[str, Any]] = []
    for index, item in enumerate(queries):
        if not isinstance(item, Mapping):
            raise XiaohongshuQueueError(f"queries[{index}] must be an object")
        scope_id = _non_empty(item.get("scope_id"), f"queries[{index}].scope_id")
        if not re.fullmatch(r"[a-z0-9][a-z0-9_]{2,63}", scope_id):
            raise XiaohongshuQueueError(f"queries[{index}].scope_id has an invalid format")
        domain_hints = item.get("domain_hints", [])
        if not isinstance(domain_hints, list) or not all(
            isinstance(value, str) and value for value in domain_hints
        ):
            raise XiaohongshuQueueError(f"queries[{index}].domain_hints must be strings")
        query = _non_empty(item.get("query"), f"queries[{index}].query")
        normalized.append({
            "scope_id": scope_id,
            "domain_hints": list(dict.fromkeys(domain_hints)),
            "query": query,
            "manual_platform_search_url": build_search_url("xiaohongshu", query),
            "external_discovery_query": f"site:xiaohongshu.com/explore {query}",
        })
    return normalized


def build_xhs_review_plan(
    queries: Sequence[Mapping[str, Any]],
    *,
    max_candidates_per_query: int = 5,
    created_at: Optional[datetime] = None,
) -> Dict[str, Any]:
    """Build a finite no-network discovery and manual-review plan."""

    normalized = _validate_queries(queries)
    if not 1 <= max_candidates_per_query <= 20:
        raise XiaohongshuQueueError("max_candidates_per_query must be in [1, 20]")
    created = _created_at(created_at)
    fingerprint = hashlib.sha256(
        (created + "\n" + "\n".join(item["query"] for item in normalized)).encode()
    ).hexdigest()[:12]
    tasks = []
    for index, item in enumerate(normalized, 1):
        tasks.append({
            "task_id": f"xhs-review-{index:04d}",
            **item,
            "max_candidates": max_candidates_per_query,
        })
    return {
        "schema_version": 1,
        "run_id": f"xhs-plan-{re.sub(r'[^0-9]', '', created)[:14]}-{fingerprint}",
        "created_at": created,
        "trigger": "manual_on_demand",
        "platform": "xiaohongshu",
        "collection_mode": "manual_review_queue",
        "tasks": tasks,
        "automation_boundary": {
            "query_generation": True,
            "candidate_link_normalization": True,
            "deduplication": True,
            "review_state_management": True,
            "platform_login": False,
            "browser_dom_extraction": False,
            "full_text_collection": False,
            "comment_collection": False,
        },
        "stop_on": ["login_required", "captcha", "risk_control", "access_denied"],
    }


def _optional_short(value: Any, name: str, maximum: int) -> Optional[str]:
    if value is None:
        return None
    text = _non_empty(value, name)
    if len(text) > maximum:
        raise XiaohongshuQueueError(f"{name} exceeds {maximum} characters")
    return text


def normalize_xhs_discovery_candidate(
    item: Mapping[str, Any], *, captured_at: Optional[datetime] = None
) -> Dict[str, Any]:
    """Normalize one link/snippet candidate without opening the platform page."""

    if not isinstance(item, Mapping):
        raise XiaohongshuQueueError("Xiaohongshu candidate must be an object")
    raw_url = item.get("canonical_url", item.get("url"))
    try:
        canonical_url, note_id = canonicalize_social_url(
            "xiaohongshu", _non_empty(raw_url, "candidate.url")
        )
    except SocialCollectionError as exc:
        raise XiaohongshuQueueError(str(exc)) from exc
    scope_id = _non_empty(
        item.get("scope_id", "open_ended_wbc_field_notes"), "candidate.scope_id"
    )
    if not re.fullmatch(r"[a-z0-9][a-z0-9_]{2,63}", scope_id):
        raise XiaohongshuQueueError("candidate.scope_id has an invalid format")
    domain_hints = item.get("domain_hints", [])
    if not isinstance(domain_hints, list) or not all(
        isinstance(value, str) and value for value in domain_hints
    ):
        raise XiaohongshuQueueError("candidate.domain_hints must be strings")
    discovery_source = item.get("discovery_source", "external_search")
    if discovery_source not in XHS_DISCOVERY_SOURCES:
        raise XiaohongshuQueueError(
            f"candidate.discovery_source must be one of {XHS_DISCOVERY_SOURCES}"
        )
    candidate = {
        "platform": "xiaohongshu",
        "note_id": note_id,
        "canonical_url": canonical_url,
        "scope_id": scope_id,
        "domain_hints": list(dict.fromkeys(domain_hints)),
        "query": _non_empty(item.get("query"), "candidate.query"),
        "title": _optional_short(item.get("title"), "candidate.title", 300),
        "search_snippet": _optional_short(
            item.get("search_snippet", item.get("snippet")),
            "candidate.search_snippet",
            500,
        ),
        "author_display": _optional_short(
            item.get("author_display"), "candidate.author_display", 100
        ),
        "discovery_source": discovery_source,
        "discovered_at": _created_at(captured_at),
        "review_status": "pending_manual_review",
        "review_note": None,
        "reviewed_at": None,
        "content_collected": False,
    }
    return candidate


def build_xhs_review_queue(
    plan: Mapping[str, Any],
    candidates: Sequence[Mapping[str, Any]] = (),
    *,
    existing_queue: Optional[Mapping[str, Any]] = None,
    created_at: Optional[datetime] = None,
) -> Dict[str, Any]:
    """Merge candidates into a stable queue while preserving prior decisions."""

    if not isinstance(plan, Mapping) or plan.get("platform") != "xiaohongshu":
        raise XiaohongshuQueueError("plan must be one Xiaohongshu review plan")
    existing_items = []
    if existing_queue is not None:
        if not isinstance(existing_queue, Mapping):
            raise XiaohongshuQueueError("existing_queue must be an object")
        existing_items = existing_queue.get("candidates", [])
        if not isinstance(existing_items, list):
            raise XiaohongshuQueueError("existing_queue.candidates must be a list")
    by_url = {
        item["canonical_url"]: dict(item)
        for item in existing_items
        if isinstance(item, Mapping) and isinstance(item.get("canonical_url"), str)
    }
    added = 0
    for item in candidates:
        normalized = normalize_xhs_discovery_candidate(item, captured_at=created_at)
        if normalized["canonical_url"] in by_url:
            continue
        by_url[normalized["canonical_url"]] = normalized
        added += 1
    updated = _created_at(created_at)
    return {
        "schema_version": 1,
        "platform": "xiaohongshu",
        "collection_mode": "manual_review_queue",
        "plan_run_id": plan.get("run_id"),
        "plan": dict(plan),
        "updated_at": updated,
        "added": added,
        "candidates": list(by_url.values()),
    }


def apply_xhs_review_decisions(
    queue: Mapping[str, Any], decisions: Sequence[Mapping[str, Any]],
    *, reviewed_at: Optional[datetime] = None,
) -> Dict[str, Any]:
    """Apply explicit human decisions without fetching any post content."""

    if not isinstance(queue, Mapping) or queue.get("platform") != "xiaohongshu":
        raise XiaohongshuQueueError("queue must be one Xiaohongshu review queue")
    items = queue.get("candidates", [])
    if not isinstance(items, list):
        raise XiaohongshuQueueError("queue.candidates must be a list")
    by_url = {
        item["canonical_url"]: dict(item)
        for item in items
        if isinstance(item, Mapping) and isinstance(item.get("canonical_url"), str)
    }
    timestamp = _created_at(reviewed_at)
    for index, decision in enumerate(decisions):
        if not isinstance(decision, Mapping):
            raise XiaohongshuQueueError(f"decisions[{index}] must be an object")
        try:
            canonical_url, _ = canonicalize_social_url(
                "xiaohongshu", _non_empty(decision.get("canonical_url"), "decision.url")
            )
        except SocialCollectionError as exc:
            raise XiaohongshuQueueError(str(exc)) from exc
        if canonical_url not in by_url:
            raise XiaohongshuQueueError(f"decision URL is not present in queue: {canonical_url}")
        status = _non_empty(decision.get("review_status"), "decision.review_status")
        if status not in XHS_REVIEW_STATUSES:
            raise XiaohongshuQueueError(
                f"decision.review_status must be one of {XHS_REVIEW_STATUSES}"
            )
        if status == "pending_manual_review":
            raise XiaohongshuQueueError("a decision cannot reset an item to pending")
        by_url[canonical_url]["review_status"] = status
        by_url[canonical_url]["review_note"] = _optional_short(
            decision.get("review_note"), "decision.review_note", 500
        )
        by_url[canonical_url]["reviewed_at"] = timestamp
    updated = dict(queue)
    updated["updated_at"] = timestamp
    updated["candidates"] = list(by_url.values())
    return updated
