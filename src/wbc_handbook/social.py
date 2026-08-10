"""On-demand manual-review plans and normalized community captures.

This shared module deliberately contains no HTTP client, cookie handling, browser
profile access, or background scheduler. Platform-specific official APIs live in
separate adapters; gated pages enter only through explicit human review/import.
"""

from __future__ import annotations

from datetime import datetime, timezone
import hashlib
import re
from typing import Any, Dict, Iterable, List, Mapping, Optional, Sequence, Tuple
from urllib.parse import quote_plus, urlparse

from .importer import normalize_manual_source
from .models import AccessMode, Domain, SourceRecord, parse_aware_datetime


SUPPORTED_PLATFORMS = ("xiaohongshu", "zhihu", "x")
MANUAL_REVIEW_PLATFORMS = ("xiaohongshu", "zhihu")
MAX_SELECTED_COMMENTS = 50
MAX_MEDIA_SUMMARIES = 20
MAX_ENGINEERING_ITEMS_PER_FIELD = 10
ENGINEERING_DETAIL_FIELDS = (
    "problem_statements",
    "environments",
    "symptoms",
    "diagnostics",
    "suspected_causes",
    "attempts",
    "effective_fixes",
    "outcomes",
    "limits",
    "safety_notes",
)
ENGINEERING_ANSWER_STATUSES = ("resolved", "partial", "unresolved", "conflicting")


class SocialCollectionError(ValueError):
    """Raised when a social collection plan or capture violates the contract."""


def _non_empty_string(value: Any, name: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise SocialCollectionError(f"{name} must be a non-empty string")
    return value.strip()


def _platform(value: Any) -> str:
    platform = _non_empty_string(value, "platform").lower()
    if platform not in SUPPORTED_PLATFORMS:
        raise SocialCollectionError(
            f"unsupported platform {platform!r}; expected one of {SUPPORTED_PLATFORMS}"
        )
    return platform


def _host_matches(host: str, expected: str) -> bool:
    return host == expected or host.endswith("." + expected)


def canonicalize_social_url(platform: str, url: str) -> Tuple[str, str]:
    """Return ``(canonical_url, stable_post_id)`` for a supported post URL.

    Tracking parameters and Xiaohongshu access tokens remain in ``retrieval_url``
    metadata, never in the canonical citation URL.
    """

    platform = _platform(platform)
    raw_url = _non_empty_string(url, "canonical_url")
    parsed = urlparse(raw_url)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        raise SocialCollectionError("social URL must be an absolute HTTP(S) URL")
    host = (parsed.hostname or "").lower()
    path = parsed.path.rstrip("/")

    if platform == "xiaohongshu":
        if not _host_matches(host, "xiaohongshu.com"):
            raise SocialCollectionError("Xiaohongshu capture must use xiaohongshu.com")
        match = re.fullmatch(r"/(?:explore|discovery/item)/([0-9a-fA-F]{24})", path)
        if not match:
            raise SocialCollectionError(
                "Xiaohongshu URL must identify one /explore/<24-hex-note-id> post"
            )
        post_id = match.group(1).lower()
        return f"https://www.xiaohongshu.com/explore/{post_id}", post_id

    if platform == "x":
        if host not in {"x.com", "www.x.com", "twitter.com", "www.twitter.com"}:
            raise SocialCollectionError("X capture must use x.com or twitter.com")
        status = re.fullmatch(
            r"/([A-Za-z0-9_]{1,15})/status/(\d+)"
            r"(?:/(?:photo|video)/\d+)?",
            path,
        )
        if status:
            username, post_id = status.groups()
            return f"https://x.com/{username.lower()}/status/{post_id}", post_id
        web_status = re.fullmatch(r"/i/web/status/(\d+)", path)
        if web_status:
            post_id = web_status.group(1)
            return f"https://x.com/i/web/status/{post_id}", post_id
        raise SocialCollectionError("X URL must identify one /<username>/status/<id> post")

    if not _host_matches(host, "zhihu.com"):
        raise SocialCollectionError("Zhihu capture must use zhihu.com")

    answer = re.fullmatch(r"/question/(\d+)/answer/(\d+)", path)
    if answer:
        question_id, answer_id = answer.groups()
        return (
            f"https://www.zhihu.com/question/{question_id}/answer/{answer_id}",
            f"answer.{answer_id}",
        )
    article = re.fullmatch(r"/p/(\d+)", path)
    if article and (host == "zhuanlan.zhihu.com" or host == "www.zhihu.com"):
        article_id = article.group(1)
        return f"https://zhuanlan.zhihu.com/p/{article_id}", f"article.{article_id}"
    question = re.fullmatch(r"/question/(\d+)", path)
    if question:
        question_id = question.group(1)
        return f"https://www.zhihu.com/question/{question_id}", f"question.{question_id}"
    pin = re.fullmatch(r"/pin/(\d+)", path)
    if pin:
        pin_id = pin.group(1)
        return f"https://www.zhihu.com/pin/{pin_id}", f"pin.{pin_id}"
    raise SocialCollectionError(
        "Zhihu URL must identify one question, answer, article, or pin"
    )


def build_search_url(platform: str, query: str) -> str:
    platform = _platform(platform)
    if platform not in MANUAL_REVIEW_PLATFORMS:
        raise SocialCollectionError(
            "X discovery must use the official API through social-collect-x"
        )
    encoded = quote_plus(_non_empty_string(query, "query"))
    if platform == "xiaohongshu":
        return (
            "https://www.xiaohongshu.com/search_result"
            f"?keyword={encoded}&source=web_search_result_notes"
        )
    return f"https://www.zhihu.com/search?type=content&q={encoded}"


def _aware_now() -> datetime:
    return datetime.now(timezone.utc).astimezone()


def _iso_datetime(value: Optional[datetime]) -> str:
    current = value or _aware_now()
    if current.tzinfo is None:
        raise SocialCollectionError("plan timestamp must include a timezone")
    return current.isoformat(timespec="seconds")


def build_collection_plan(
    queries: Sequence[Mapping[str, Any]],
    platforms: Sequence[str] = MANUAL_REVIEW_PLATFORMS,
    max_results_per_query: int = 5,
    max_comments_per_post: int = 10,
    max_tasks_per_batch: int = 12,
    known_canonical_urls: Sequence[str] = (),
    created_at: Optional[datetime] = None,
) -> Dict[str, Any]:
    """Build a finite, manually triggered link-review plan."""

    if not 1 <= max_results_per_query <= 20:
        raise SocialCollectionError("max_results_per_query must be in [1, 20]")
    if not 0 <= max_comments_per_post <= MAX_SELECTED_COMMENTS:
        raise SocialCollectionError(
            f"max_comments_per_post must be in [0, {MAX_SELECTED_COMMENTS}]"
        )
    if not 1 <= max_tasks_per_batch <= 50:
        raise SocialCollectionError("max_tasks_per_batch must be in [1, 50]")
    normalized_platforms = list(dict.fromkeys(_platform(item) for item in platforms))
    invalid_manual_platforms = set(normalized_platforms) - set(MANUAL_REVIEW_PLATFORMS)
    if invalid_manual_platforms:
        raise SocialCollectionError(
            "manual-review plans support only Xiaohongshu/Zhihu; "
            "use social-collect-x for X"
        )
    if not normalized_platforms:
        raise SocialCollectionError("at least one platform is required")
    if not queries:
        raise SocialCollectionError("at least one social query is required")

    normalized_queries: List[Dict[str, Any]] = []
    for index, item in enumerate(queries):
        if not isinstance(item, Mapping):
            raise SocialCollectionError(f"queries[{index}] must be an object")
        query = _non_empty_string(item.get("query"), f"queries[{index}].query")
        scope_id = _non_empty_string(
            item.get("scope_id", item.get("domain")), f"queries[{index}].scope_id"
        )
        if not re.fullmatch(r"[a-z0-9][a-z0-9_]{2,63}", scope_id):
            raise SocialCollectionError(
                f"queries[{index}].scope_id must use lowercase letters, digits, underscores"
            )
        domain_hints = item.get("domain_hints")
        if domain_hints is None:
            legacy_domain = item.get("domain")
            domain_hints = [] if legacy_domain is None else [legacy_domain]
        if not isinstance(domain_hints, list):
            raise SocialCollectionError(f"queries[{index}].domain_hints must be a list")
        valid_domains = {domain.value for domain in Domain}
        normalized_hints = []
        for domain_index, domain in enumerate(domain_hints):
            normalized_domain = _non_empty_string(
                domain, f"queries[{index}].domain_hints[{domain_index}]"
            )
            if normalized_domain not in valid_domains:
                raise SocialCollectionError(f"unknown handbook domain {normalized_domain!r}")
            normalized_hints.append(normalized_domain)
        normalized_queries.append({
            "scope_id": scope_id,
            "domain_hints": list(dict.fromkeys(normalized_hints)),
            "query": query,
        })

    created = _iso_datetime(created_at)
    fingerprint_payload = "\n".join(
        [created, *normalized_platforms]
        + [f"{item['scope_id']}\t{item['query']}" for item in normalized_queries]
    )
    fingerprint = hashlib.sha256(fingerprint_payload.encode("utf-8")).hexdigest()[:12]
    compact_time = re.sub(r"[^0-9]", "", created)[:14]
    tasks = []
    for item in normalized_queries:
        for platform in normalized_platforms:
            task_index = len(tasks) + 1
            tasks.append({
                "task_id": f"task-{task_index:04d}",
                "platform": platform,
                "scope_id": item["scope_id"],
                "domain_hints": item["domain_hints"],
                "query": item["query"],
                "search_url": build_search_url(platform, item["query"]),
                "max_results": max_results_per_query,
                "max_selected_comments_per_post": max_comments_per_post,
            })

    batches = []
    for start in range(0, len(tasks), max_tasks_per_batch):
        batch_tasks = tasks[start:start + max_tasks_per_batch]
        batch_id = f"batch-{len(batches) + 1:03d}"
        for task in batch_tasks:
            task["batch_id"] = batch_id
        batches.append({
            "batch_id": batch_id,
            "task_ids": [task["task_id"] for task in batch_tasks],
        })

    normalized_known_urls = []
    for index, url in enumerate(known_canonical_urls):
        normalized_known_urls.append(
            _non_empty_string(url, f"known_canonical_urls[{index}]")
        )

    return {
        "schema_version": 2,
        "run_id": f"social-{compact_time}-{fingerprint}",
        "created_at": created,
        "trigger": "manual_on_demand",
        "access_mode": AccessMode.MANUAL_IMPORT.value,
        "tasks": tasks,
        "batches": batches,
        "known_canonical_urls": list(dict.fromkeys(normalized_known_urls)),
        "execution_rules": {
            "manual_navigation_only": True,
            "automated_dom_collection": False,
            "finite_result_limit": True,
            "expand_full_text": False,
            "inspect_visible_media": False,
            "skip_known_canonical_urls": True,
            "store_full_post_or_bulk_comments": False,
            "stop_on": ["login_required", "captcha", "risk_control", "access_denied"],
        },
    }


def queries_from_config(config: Mapping[str, Any]) -> List[Dict[str, Any]]:
    """Flatten an open engineering-scope config into query records.

    Schema v2 uses independent ``scope_id`` values and optional WBC domain hints.
    Schema v1 remains accepted so existing local configurations do not break.
    """

    if not isinstance(config, Mapping):
        raise SocialCollectionError("social query config must be an object")
    schema_version = config.get("schema_version")
    if schema_version not in {1, 2}:
        raise SocialCollectionError("social query config schema_version must be 1 or 2")
    groups_key = "topics" if schema_version == 1 else "scopes"
    topics = config.get(groups_key)
    if not isinstance(topics, list) or not topics:
        raise SocialCollectionError(
            f"social query config {groups_key} must be a non-empty list"
        )
    valid_domains = {item.value for item in Domain}
    queries: List[Dict[str, Any]] = []
    for topic_index, topic in enumerate(topics):
        if not isinstance(topic, Mapping):
            raise SocialCollectionError(f"topics[{topic_index}] must be an object")
        if schema_version == 1:
            domain = _non_empty_string(
                topic.get("domain"), f"topics[{topic_index}].domain"
            )
            if domain not in valid_domains:
                raise SocialCollectionError(f"unknown handbook domain {domain!r}")
            scope_id = domain
            domain_hints = [domain]
        else:
            scope_id = _non_empty_string(
                topic.get("scope_id"), f"scopes[{topic_index}].scope_id"
            )
            if not re.fullmatch(r"[a-z0-9][a-z0-9_]{2,63}", scope_id):
                raise SocialCollectionError(
                    f"scopes[{topic_index}].scope_id has an invalid format"
                )
            domain_hints = topic.get("domain_hints", [])
            if not isinstance(domain_hints, list):
                raise SocialCollectionError(
                    f"scopes[{topic_index}].domain_hints must be a list"
                )
            for domain in domain_hints:
                if domain not in valid_domains:
                    raise SocialCollectionError(f"unknown handbook domain {domain!r}")
        topic_queries = topic.get("queries")
        if not isinstance(topic_queries, list) or not topic_queries:
            raise SocialCollectionError(
                f"topics[{topic_index}].queries must be a non-empty list"
            )
        for query_index, query in enumerate(topic_queries):
            queries.append({
                "scope_id": scope_id,
                "domain_hints": list(dict.fromkeys(domain_hints)),
                "query": _non_empty_string(
                    query, f"topics[{topic_index}].queries[{query_index}]"
                ),
            })
    return queries


_ATTENTION_MULTIPLIERS = {
    "\u4e07": 10_000.0,
    "\u5343": 1_000.0,
    "\u4ebf": 100_000_000.0,
    "k": 1_000.0,
    "m": 1_000_000.0,
    "b": 1_000_000_000.0,
}


def parse_attention_number(value: Any, name: str = "attention") -> float:
    """Parse visible counters such as ``1.4\u4e07`` and ``1\u5343+``."""

    if isinstance(value, bool):
        raise SocialCollectionError(f"{name} must be numeric")
    if isinstance(value, (int, float)):
        if value < 0:
            raise SocialCollectionError(f"{name} cannot be negative")
        return float(value)
    text = _non_empty_string(value, name).replace(",", "").replace("+", "")
    multiplier = 1.0
    unit = text[-1:].lower()
    if unit in _ATTENTION_MULTIPLIERS:
        multiplier = _ATTENTION_MULTIPLIERS[unit]
        text = text[:-1]
    try:
        parsed = float(text) * multiplier
    except ValueError as exc:
        raise SocialCollectionError(f"{name} must be a visible numeric counter") from exc
    if parsed < 0:
        raise SocialCollectionError(f"{name} cannot be negative")
    return parsed


def _selected_comments(value: Any) -> List[Dict[str, Any]]:
    if value is None:
        return []
    if not isinstance(value, list):
        raise SocialCollectionError("selected_comments must be a list")
    if len(value) > MAX_SELECTED_COMMENTS:
        raise SocialCollectionError(
            f"selected_comments exceeds the {MAX_SELECTED_COMMENTS}-comment limit"
        )
    comments: List[Dict[str, Any]] = []
    for index, item in enumerate(value):
        if not isinstance(item, Mapping):
            raise SocialCollectionError(f"selected_comments[{index}] must be an object")
        text = _non_empty_string(item.get("text"), f"selected_comments[{index}].text")
        if len(text) > 500:
            raise SocialCollectionError(
                f"selected_comments[{index}].text exceeds 500 characters"
            )
        comment: Dict[str, Any] = {"text": text}
        for key in ("author_display", "published_display", "reply_context"):
            if item.get(key) is not None:
                comment[key] = _non_empty_string(
                    item[key], f"selected_comments[{index}].{key}"
                )
        if item.get("likes") is not None:
            comment["likes"] = parse_attention_number(
                item["likes"], f"selected_comments[{index}].likes"
            )
        comments.append(comment)
    return comments


def _media_summaries(value: Any) -> List[str]:
    if value is None:
        return []
    if not isinstance(value, list):
        raise SocialCollectionError("media_summaries must be a list")
    if len(value) > MAX_MEDIA_SUMMARIES:
        raise SocialCollectionError(
            f"media_summaries exceeds the {MAX_MEDIA_SUMMARIES}-item limit"
        )
    summaries = []
    for index, item in enumerate(value):
        summary = _non_empty_string(item, f"media_summaries[{index}]")
        if len(summary) > 500:
            raise SocialCollectionError(
                f"media_summaries[{index}] exceeds 500 characters"
            )
        summaries.append(summary)
    return summaries


def _string_list(value: Any, name: str, maximum: int = 20) -> List[str]:
    if value is None:
        return []
    raw_items = [value] if isinstance(value, str) else value
    if not isinstance(raw_items, list):
        raise SocialCollectionError(f"{name} must be a string or a list")
    if len(raw_items) > maximum:
        raise SocialCollectionError(f"{name} exceeds the {maximum}-item limit")
    items = []
    for index, item in enumerate(raw_items):
        normalized = _non_empty_string(item, f"{name}[{index}]")
        if len(normalized) > 500:
            raise SocialCollectionError(f"{name}[{index}] exceeds 500 characters")
        items.append(normalized)
    return items


def _engineering_details(value: Any) -> Tuple[Dict[str, List[str]], int, str]:
    if not isinstance(value, Mapping):
        raise SocialCollectionError("engineering_details must be an object")
    unknown = set(value) - set(ENGINEERING_DETAIL_FIELDS)
    if unknown:
        raise SocialCollectionError(
            "engineering_details has unknown fields: " + ", ".join(sorted(unknown))
        )
    details = {
        field: _string_list(
            value.get(field),
            f"engineering_details.{field}",
            MAX_ENGINEERING_ITEMS_PER_FIELD,
        )
        for field in ENGINEERING_DETAIL_FIELDS
    }
    if not details["problem_statements"] and not details["symptoms"]:
        raise SocialCollectionError(
            "engineering_details needs at least one problem_statement or symptom"
        )
    signal_groups = (
        details["problem_statements"] or details["symptoms"],
        details["environments"],
        details["diagnostics"] or details["suspected_causes"],
        details["attempts"],
        details["effective_fixes"] or details["outcomes"],
        details["limits"] or details["safety_notes"],
    )
    signal_count = sum(bool(group) for group in signal_groups)
    quality = "rich" if signal_count >= 5 else "useful" if signal_count >= 3 else "sparse"
    return details, signal_count, quality


def _engineering_qa(
    value: Any, canonical_url: str, platform: str
) -> List[Dict[str, str]]:
    if not isinstance(value, list) or not value:
        raise SocialCollectionError("engineering_qa must be a non-empty list")
    if len(value) > 20:
        raise SocialCollectionError("engineering_qa exceeds the 20-card limit")
    cards = []
    for index, item in enumerate(value):
        if not isinstance(item, Mapping):
            raise SocialCollectionError(f"engineering_qa[{index}] must be an object")
        question = _non_empty_string(
            item.get("question_zh"), f"engineering_qa[{index}].question_zh"
        )
        status = _non_empty_string(
            item.get("answer_status"), f"engineering_qa[{index}].answer_status"
        )
        if status not in ENGINEERING_ANSWER_STATUSES:
            raise SocialCollectionError(
                f"engineering_qa[{index}].answer_status must be one of "
                f"{ENGINEERING_ANSWER_STATUSES}"
            )
        answer = item.get("answer_zh")
        if status == "unresolved" and answer is None:
            answer = "原帖未给出可验证的解答。"
        answer = _non_empty_string(answer, f"engineering_qa[{index}].answer_zh")
        locator = _non_empty_string(
            item.get("source_locator"), f"engineering_qa[{index}].source_locator"
        )
        source_url = canonical_url
        if item.get("source_url") is not None:
            source_url, _ = canonicalize_social_url(
                platform,
                _non_empty_string(
                    item["source_url"], f"engineering_qa[{index}].source_url"
                ),
            )
        card = {
            "question_zh": question,
            "answer_zh": answer,
            "answer_status": status,
            "source_locator": locator,
            "source_url": source_url,
            "verification_status": "community_candidate",
        }
        if item.get("applicability") is not None:
            card["applicability"] = _non_empty_string(
                item["applicability"], f"engineering_qa[{index}].applicability"
            )
        cards.append(card)
    return cards


def normalize_social_capture(payload: Mapping[str, Any]) -> SourceRecord:
    """Validate reviewed analysis and convert it to a community SourceRecord."""

    if not isinstance(payload, Mapping):
        raise SocialCollectionError("social capture must be an object")
    platform = _platform(payload.get("platform"))
    retrieval_url = _non_empty_string(
        payload.get("retrieval_url", payload.get("canonical_url")), "retrieval_url"
    )
    canonical_url, post_id = canonicalize_social_url(
        platform, payload.get("canonical_url", retrieval_url)
    )
    query = _non_empty_string(payload.get("query"), "query")
    scope_id = _non_empty_string(
        payload.get("scope_id", payload.get("domain")), "scope_id"
    )
    if not re.fullmatch(r"[a-z0-9][a-z0-9_]{2,63}", scope_id):
        raise SocialCollectionError("scope_id has an invalid format")
    title_generated = False
    title_value = payload.get("title")
    if platform == "x" and (not isinstance(title_value, str) or not title_value.strip()):
        author_hint = payload.get("author_display") or post_id
        title_value = f"{author_hint} 的 X 帖子"
        title_generated = True
    title = _non_empty_string(title_value, "title")
    summary = _non_empty_string(payload.get("summary"), "summary")
    relevance_reason = _non_empty_string(
        payload.get("wbc_relevance_reason"), "wbc_relevance_reason"
    )
    if len(summary) > 3000:
        raise SocialCollectionError("summary exceeds the 3000-character storage limit")
    captured_at = _non_empty_string(payload.get("captured_at"), "captured_at")
    parse_aware_datetime(captured_at, "captured_at")

    access_mode = payload.get("access_mode", AccessMode.MANUAL_IMPORT.value)
    if access_mode not in {
        AccessMode.AUTHORIZED_VISIBLE_BROWSER.value,
        AccessMode.MANUAL_IMPORT.value,
        AccessMode.PUBLIC_API.value,
    }:
        raise SocialCollectionError(
            "social capture access_mode must be authorized_visible_browser, "
            "manual_import, or public_api"
        )

    published_at = payload.get("published_at")
    if published_at is not None:
        published_at = _non_empty_string(published_at, "published_at")
        parse_aware_datetime(published_at, "published_at")
    excerpt = payload.get("excerpt")
    if excerpt is not None:
        excerpt = _non_empty_string(excerpt, "excerpt")
        if len(excerpt) > 1000:
            raise SocialCollectionError("excerpt exceeds the 1000-character storage limit")

    attention_input = payload.get("attention", {})
    if not isinstance(attention_input, Mapping):
        raise SocialCollectionError("attention must be an object")
    attention = {
        _non_empty_string(key, "attention key"): parse_attention_number(
            value, f"attention.{key}"
        )
        for key, value in attention_input.items()
    }

    engineering_details, signal_count, experience_quality = _engineering_details(
        payload.get("engineering_details")
    )
    domain_hints = payload.get("domain_hints")
    if domain_hints is None:
        legacy_domain = payload.get("domain")
        domain_hints = [] if legacy_domain is None else [legacy_domain]
    if not isinstance(domain_hints, list):
        raise SocialCollectionError("domain_hints must be a list")
    valid_domains = {domain.value for domain in Domain}
    normalized_domain_hints = []
    for index, domain in enumerate(domain_hints):
        normalized_domain = _non_empty_string(domain, f"domain_hints[{index}]")
        if normalized_domain not in valid_domains:
            raise SocialCollectionError(f"unknown handbook domain {normalized_domain!r}")
        normalized_domain_hints.append(normalized_domain)

    metadata: Dict[str, Any] = {
        "schema_version": 2,
        "platform": platform,
        "post_id": post_id,
        "scope_id": scope_id,
        "domain_hints": list(dict.fromkeys(normalized_domain_hints)),
        "query": query,
        "wbc_relevance_reason": relevance_reason,
        "review_status": "candidate",
        "experience_quality": experience_quality,
        "experience_signal_count": signal_count,
        "engineering_details": engineering_details,
        "engineering_qa": _engineering_qa(
            payload.get("engineering_qa"), canonical_url, platform
        ),
        "components": _string_list(payload.get("components"), "components"),
        "robot_platforms": _string_list(
            payload.get("robot_platforms"), "robot_platforms"
        ),
        "selected_comments": _selected_comments(payload.get("selected_comments")),
        "media_summaries": _media_summaries(payload.get("media_summaries")),
    }
    if retrieval_url != canonical_url:
        # Retrieval URLs can contain short-lived access parameters such as
        # Xiaohongshu xsec_token.  The raw capture belongs under ignored var/;
        # canonical repository records retain only this non-secret audit flag.
        metadata["retrieval_url_was_canonicalized"] = True
    if title_generated:
        metadata["title_generated"] = True
    for key in ("published_display", "collector_note"):
        if payload.get(key) is not None:
            metadata[key] = _non_empty_string(payload[key], key)

    author = payload.get("author_display")
    authors = [] if author is None else [_non_empty_string(author, "author_display")]
    publisher = {
        "xiaohongshu": "Xiaohongshu",
        "zhihu": "Zhihu",
        "x": "X",
    }[platform]
    source_id = f"community.{platform}.{post_id}"
    source_payload: Dict[str, Any] = {
        "source_id": source_id,
        "kind": "community",
        "title": title,
        "canonical_url": canonical_url,
        "captured_at": captured_at,
        "summary": summary,
        "access_mode": access_mode,
        "authors": authors,
        "publisher": publisher,
        "attention": attention,
        "metadata": metadata,
    }
    if published_at is not None:
        source_payload["published_at"] = published_at
    if excerpt is not None:
        source_payload["excerpt"] = excerpt
    return normalize_manual_source(source_payload)


def deduplicate_social_sources(
    sources: Iterable[SourceRecord],
) -> Tuple[List[SourceRecord], List[str]]:
    """Keep the first canonical post in a run and report duplicate source IDs."""

    unique: List[SourceRecord] = []
    duplicates: List[str] = []
    seen_urls = set()
    seen_ids = set()
    for source in sources:
        if source.canonical_url in seen_urls or source.source_id in seen_ids:
            duplicates.append(source.source_id)
            continue
        seen_urls.add(source.canonical_url)
        seen_ids.add(source.source_id)
        unique.append(source)
    return unique, duplicates


def _markdown_text(value: Any) -> str:
    """Render untrusted source text as one Markdown-safe line."""

    return (
        str(value)
        .replace("\r", " ")
        .replace("\n", " ")
        .replace("[", "\\[")
        .replace("]", "\\]")
    )


def render_engineering_qa_markdown(
    sources: Iterable[SourceRecord], generated_at: Optional[datetime] = None
) -> str:
    """Render candidate engineering Q&A cards with mandatory original-post links."""

    generated = _iso_datetime(generated_at)
    rows = []
    for source in sources:
        if source.kind.value != "community":
            continue
        metadata = source.metadata
        cards = metadata.get("engineering_qa", [])
        if not isinstance(cards, list):
            continue
        for card in cards:
            if not isinstance(card, Mapping):
                continue
            rows.append((
                str(metadata.get("scope_id", "unclassified")),
                source,
                card,
            ))
    rows.sort(key=lambda item: (item[0], item[1].captured_at, item[1].source_id))

    lines = [
        "# WBC 社交平台工程问题候选清单",
        "",
        f"> 生成时间：{generated}。以下解答均是社区候选信息，需要论文/官方文档/源码/Issue 独立验证。",
        "",
    ]
    if not rows:
        lines.extend(["当前没有已入库的工程问题卡片。", ""])
        return "\n".join(lines)

    current_scope = None
    for scope_id, source, card in rows:
        if scope_id != current_scope:
            lines.extend([f"## `{_markdown_text(scope_id)}`", ""])
            current_scope = scope_id
        title = _markdown_text(source.title)
        question = _markdown_text(card.get("question_zh", ""))
        answer = _markdown_text(card.get("answer_zh", ""))
        status = _markdown_text(card.get("answer_status", "unresolved"))
        locator = _markdown_text(card.get("source_locator", "未标注"))
        source_url = card.get("source_url") or source.canonical_url
        author = _markdown_text(source.authors[0]) if source.authors else "未显示"
        lines.extend([
            f"### {question}",
            "",
            f"- 候选解答（`{status}`）：{answer}",
            f"- 来源定位：{locator}",
            f"- 原帖：[{title}]({source_url})",
            f"- 平台/作者：{_markdown_text(source.publisher or '')} / {author}",
        ])
        if card.get("applicability"):
            lines.append(f"- 适用边界：{_markdown_text(card['applicability'])}")
        lines.append("")
    return "\n".join(lines)
