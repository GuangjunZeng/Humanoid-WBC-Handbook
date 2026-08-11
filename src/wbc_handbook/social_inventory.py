"""Minimal, reviewable inventory for every discovered technical candidate."""

from __future__ import annotations

from datetime import datetime, timezone
import hashlib
from typing import Any, Dict, Iterable, Mapping, Optional, Sequence
from urllib.parse import urlparse

from .models import SourceRecord
from .social import SUPPORTED_PLATFORMS, canonicalize_social_url


INVENTORY_SCHEMA_VERSION = 1
TRIAGE_STATUSES = ("reviewed", "technical_pending", "excluded")


class SocialInventoryError(ValueError):
    """Raised when an inventory candidate or review decision is invalid."""


def _iso(value: Optional[datetime] = None) -> str:
    current = value or datetime.now(timezone.utc).astimezone()
    if current.tzinfo is None:
        raise SocialInventoryError("inventory timestamp must include a timezone")
    return current.isoformat(timespec="seconds")


def _text(value: Any, name: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise SocialInventoryError(f"{name} must be a non-empty string")
    return value.strip()


def _infer_platform(item: Mapping[str, Any], url: str) -> str:
    raw = item.get("platform")
    if isinstance(raw, str):
        normalized = raw.strip().lower()
        aliases = {"github": "github_issue", "twitter": "x"}
        normalized = aliases.get(normalized, normalized)
        if normalized in SUPPORTED_PLATFORMS:
            return normalized
    host = (urlparse(url).hostname or "").lower()
    if host == "github.com":
        return "github_issue"
    if host.endswith("xiaohongshu.com"):
        return "xiaohongshu"
    if host.endswith("zhihu.com"):
        return "zhihu"
    if host in {"x.com", "www.x.com", "twitter.com", "www.twitter.com"}:
        return "x"
    raise SocialInventoryError(f"cannot infer a supported platform for {url}")


def _canonical(item: Mapping[str, Any]) -> tuple[str, str]:
    raw_url = item.get("canonical_url") or item.get("url") or item.get("source_url")
    url = _text(raw_url, "candidate canonical_url")
    platform = _infer_platform(item, url)
    try:
        canonical, _ = canonicalize_social_url(platform, url)
    except ValueError as exc:
        raise SocialInventoryError(str(exc)) from exc
    return platform, canonical


def _string_values(values: Iterable[Any]) -> list[str]:
    return list(dict.fromkeys(
        value.strip() for value in values if isinstance(value, str) and value.strip()
    ))


def _candidate_fields(item: Mapping[str, Any], observed_at: str) -> Dict[str, Any]:
    platform, canonical_url = _canonical(item)
    scopes = []
    queries = []
    if item.get("scope_id"):
        scopes.append(item.get("scope_id"))
    if isinstance(item.get("scope_ids"), list):
        scopes.extend(item.get("scope_ids", []))
    if item.get("query"):
        queries.append(item.get("query"))
    if isinstance(item.get("queries"), list):
        queries.extend(item.get("queries", []))
    matches = item.get("matches", [])
    if isinstance(matches, list):
        for match in matches:
            if isinstance(match, Mapping):
                scopes.append(match.get("scope_id"))
                queries.append(match.get("query"))
    scopes = _string_values(scopes) or ["open_ended_wbc_field_notes"]
    queries = _string_values(queries)
    title = item.get("title")
    if not isinstance(title, str) or not title.strip():
        title = f"{platform} 技术候选 {canonical_url.rsplit('/', 1)[-1]}"
    digest = hashlib.sha256(f"{platform}\t{canonical_url}".encode("utf-8")).hexdigest()[:20]
    first_seen = item.get("first_seen_at") or item.get("captured_at") or observed_at
    last_seen = item.get("last_seen_at") or item.get("captured_at") or observed_at
    return {
        "candidate_id": f"candidate.{digest}",
        "canonical_url": canonical_url,
        "title": title.strip(),
        "platform": platform,
        "scope_ids": scopes,
        "queries": queries,
        "first_seen_at": str(first_seen),
        "last_seen_at": str(last_seen),
        "triage_status": "technical_pending",
        "triage_reason_zh": "技术相关性待结构化审阅，保守保留。",
        "related_problem_ids": [],
    }


def _merge_record(existing: Dict[str, Any], incoming: Mapping[str, Any]) -> Dict[str, Any]:
    merged = dict(existing)
    merged["title"] = merged.get("title") or incoming.get("title")
    merged["scope_ids"] = _string_values([
        *merged.get("scope_ids", []), *incoming.get("scope_ids", [])
    ])
    merged["queries"] = _string_values([
        *merged.get("queries", []), *incoming.get("queries", [])
    ])
    merged["related_problem_ids"] = _string_values([
        *merged.get("related_problem_ids", []),
        *incoming.get("related_problem_ids", []),
    ])
    merged["first_seen_at"] = min(
        str(merged.get("first_seen_at", incoming["first_seen_at"])),
        str(incoming["first_seen_at"]),
    )
    merged["last_seen_at"] = max(
        str(merged.get("last_seen_at", incoming["last_seen_at"])),
        str(incoming["last_seen_at"]),
    )
    return merged


def _minimal_existing(item: Mapping[str, Any], observed_at: str) -> Dict[str, Any]:
    base = _candidate_fields(item, observed_at)
    status = item.get("triage_status", "technical_pending")
    if status not in TRIAGE_STATUSES:
        raise SocialInventoryError(f"unknown triage_status {status!r}")
    base["triage_status"] = status
    reason = item.get("triage_reason_zh")
    if status == "excluded" and (not isinstance(reason, str) or not reason.strip()):
        raise SocialInventoryError("excluded candidate requires triage_reason_zh")
    if isinstance(reason, str) and reason.strip():
        base["triage_reason_zh"] = reason.strip()
    base["related_problem_ids"] = _string_values(item.get("related_problem_ids", []))
    return base


def build_social_candidate_inventory(
    candidate_groups: Sequence[Sequence[Mapping[str, Any]]],
    *,
    reviewed_sources: Sequence[SourceRecord] = (),
    previous_inventory: Optional[Mapping[str, Any]] = None,
    decisions: Sequence[Mapping[str, Any]] = (),
    generated_at: Optional[datetime] = None,
) -> Dict[str, Any]:
    """Merge and deduplicate candidates without retaining bodies or media."""

    observed_at = _iso(generated_at)
    by_url: Dict[str, Dict[str, Any]] = {}
    if previous_inventory:
        if previous_inventory.get("schema_version") != INVENTORY_SCHEMA_VERSION:
            raise SocialInventoryError("inventory schema_version is unsupported")
        values = previous_inventory.get("candidates", [])
        if not isinstance(values, list):
            raise SocialInventoryError("inventory candidates must be a list")
        for item in values:
            if isinstance(item, Mapping):
                normalized = _minimal_existing(item, observed_at)
                by_url[normalized["canonical_url"]] = normalized

    input_count = 0
    for group in candidate_groups:
        for item in group:
            if not isinstance(item, Mapping):
                raise SocialInventoryError("candidate items must be objects")
            input_count += 1
            incoming = _candidate_fields(item, observed_at)
            url = incoming["canonical_url"]
            by_url[url] = (
                _merge_record(by_url[url], incoming) if url in by_url else incoming
            )

    reviewed_by_url: Dict[str, tuple[SourceRecord, list[str]]] = {}
    for source in reviewed_sources:
        if source.kind.value not in {"community", "issue"}:
            continue
        platform = source.metadata.get("platform")
        try:
            _, canonical = _canonical({
                "platform": platform,
                "canonical_url": source.canonical_url,
            })
        except SocialInventoryError:
            continue
        cards = source.metadata.get("engineering_qa", [])
        problem_ids = _string_values(
            card.get("problem_id") for card in cards if isinstance(card, Mapping)
        ) if isinstance(cards, list) else []
        reviewed_by_url[canonical] = (source, problem_ids)
        if canonical not in by_url:
            captured_at = source.captured_at
            if not isinstance(captured_at, str):
                captured_at = captured_at.isoformat()
            by_url[canonical] = _candidate_fields({
                "platform": platform,
                "canonical_url": source.canonical_url,
                "title": source.title,
                "scope_id": source.metadata.get("scope_id"),
                "query": source.metadata.get("query"),
                "captured_at": captured_at,
            }, observed_at)
    for url, (_source, problem_ids) in reviewed_by_url.items():
        by_url[url]["triage_status"] = "reviewed"
        by_url[url]["triage_reason_zh"] = "已结构化进入工程问题手册。"
        by_url[url]["related_problem_ids"] = problem_ids

    decision_count = 0
    for decision in decisions:
        if not isinstance(decision, Mapping):
            raise SocialInventoryError("review decisions must be objects")
        platform, url = _canonical(decision)
        if url not in by_url:
            by_url[url] = _candidate_fields({
                **decision, "platform": platform, "canonical_url": url
            }, observed_at)
        status = decision.get("triage_status")
        if status not in TRIAGE_STATUSES:
            raise SocialInventoryError(
                "decision triage_status must be reviewed, technical_pending, or excluded"
            )
        if status == "reviewed" and url not in reviewed_by_url:
            raise SocialInventoryError(
                "reviewed status requires a matching canonical source in data/sources"
            )
        if url in reviewed_by_url and status != "reviewed":
            raise SocialInventoryError(
                "a candidate already present in the handbook must remain reviewed"
            )
        reason = decision.get("triage_reason_zh")
        if status == "excluded" and (not isinstance(reason, str) or not reason.strip()):
            raise SocialInventoryError("excluded decision requires a Chinese reason")
        if status != by_url[url]["triage_status"] or reason:
            decision_count += 1
        by_url[url]["triage_status"] = status
        by_url[url]["triage_reason_zh"] = (
            reason.strip() if isinstance(reason, str) and reason.strip()
            else {
                "reviewed": "已结构化进入工程问题手册。",
                "technical_pending": "技术相关性待结构化审阅，保守保留。",
            }[status]
        )
        if decision.get("related_problem_ids") is not None:
            by_url[url]["related_problem_ids"] = _string_values(
                decision.get("related_problem_ids", [])
            )

    candidates = sorted(by_url.values(), key=lambda value: (
        value["triage_status"], value["platform"], value["canonical_url"]
    ))
    statuses = {status: 0 for status in TRIAGE_STATUSES}
    exclusion_reasons: Dict[str, int] = {}
    for item in candidates:
        statuses[item["triage_status"]] += 1
        if item["triage_status"] == "excluded":
            reason = item["triage_reason_zh"]
            exclusion_reasons[reason] = exclusion_reasons.get(reason, 0) + 1
    return {
        "schema_version": INVENTORY_SCHEMA_VERSION,
        "generated_at": observed_at,
        "candidates": candidates,
        "stats": {
            "input_candidates": input_count,
            "unique_candidates": len(candidates),
            "duplicates_merged": max(0, input_count - len({
                _canonical(item)[1] for group in candidate_groups for item in group
            })),
            "decisions_applied": decision_count,
            **statuses,
            "exclusion_reasons": exclusion_reasons,
        },
    }


def render_pending_markdown(
    inventory: Mapping[str, Any],
    *,
    scope_definitions: Sequence[Mapping[str, Any]] = (),
) -> Dict[str, str]:
    """Return index.md and one complete technical-pending page per scope."""

    if inventory.get("schema_version") != INVENTORY_SCHEMA_VERSION:
        raise SocialInventoryError("inventory schema_version is unsupported")
    candidates = inventory.get("candidates", [])
    if not isinstance(candidates, list):
        raise SocialInventoryError("inventory candidates must be a list")
    labels = {
        str(value.get("scope_id")): str(value.get("label_zh", value.get("scope_id")))
        for value in scope_definitions
        if isinstance(value, Mapping) and value.get("scope_id")
    }
    pending = [
        value for value in candidates
        if isinstance(value, Mapping) and value.get("triage_status") == "technical_pending"
    ]
    excluded = [
        value for value in candidates
        if isinstance(value, Mapping) and value.get("triage_status") == "excluded"
    ]
    scopes = sorted({
        scope for item in pending for scope in item.get("scope_ids", [])
        if isinstance(scope, str)
    })
    stats = inventory.get("stats", {})
    index_lines = [
        "# WBC 工程经验待整理清单", "",
        "> 本附录完整暴露尚未完成结构化整理的技术候选；每轮搜索有预算，但展示没有数量截断。",
        "", f"- 唯一候选：{stats.get('unique_candidates', len(candidates))}",
        f"- 已进入问题手册：{stats.get('reviewed', 0)}",
        f"- 技术待整理：{len(pending)}",
        f"- 排除记录：{len(excluded)}", "",
        "## 按 scope 查看", "",
    ]
    for scope in scopes:
        count = sum(scope in item.get("scope_ids", []) for item in pending)
        index_lines.append(
            f"- [{labels.get(scope, scope)} (`{scope}`)]({scope}.md)：{count} 条"
        )
    index_lines.extend(["", "## 排除原因分布", ""])
    reasons: Dict[str, int] = {}
    for item in excluded:
        reason = str(item.get("triage_reason_zh", "未记录原因"))
        reasons[reason] = reasons.get(reason, 0) + 1
    if reasons:
        for reason, count in sorted(reasons.items(), key=lambda value: (-value[1], value[0])):
            index_lines.append(f"- {reason}：{count}")
    else:
        index_lines.append("- 当前没有排除记录。")
    index_lines.extend([
        "", "排除项不进入主手册；其 URL 与中文原因仍保留在 `data/social-candidate-index.json`。", ""
    ])
    pages = {"index.md": "\n".join(index_lines)}
    for scope in scopes:
        rows = [item for item in pending if scope in item.get("scope_ids", [])]
        lines = [
            f"# {labels.get(scope, scope)}：技术待整理", "",
            f"> `scope_id`: `{scope}`；共 {len(rows)} 条，未做用户可见截断。", "",
        ]
        for index, item in enumerate(rows, start=1):
            queries = "；".join(str(value) for value in item.get("queries", [])) or "未记录"
            lines.extend([
                f"## {index}. {item.get('title', '未命名候选')}", "",
                f"- 平台：`{item.get('platform', 'unknown')}`",
                f"- 原链接：[{item.get('canonical_url')}]({item.get('canonical_url')})",
                f"- 查询来源：{queries}",
                f"- 首次/最近发现：{item.get('first_seen_at')} / {item.get('last_seen_at')}",
                f"- 审阅状态：`technical_pending` — {item.get('triage_reason_zh')}", "",
            ])
        pages[f"{scope}.md"] = "\n".join(lines)
    return pages
