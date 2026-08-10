"""User-triggered discovery through the official Zhihu Data Open Platform.

The current invited-preview search API returns bounded search summaries and
canonical links, not arbitrary full posts or complete comment archives. Raw
candidates remain under ignored ``var/`` until a human selects them for review.
"""

from __future__ import annotations

from datetime import datetime, timezone
import hashlib
import json
import os
import re
import time
from typing import Any, Dict, List, Mapping, Optional, Sequence, Tuple
from urllib import error, parse, request

from .social import SocialCollectionError, canonicalize_social_url


ZHIHU_API_BASE_URL = "https://developer.zhihu.com"
ZHIHU_SEARCH_PATH = "/api/v1/content/zhihu_search"
ZHIHU_DEFAULT_SECRET_ENV = "ZHIHU_ACCESS_SECRET"
ZHIHU_MAX_RESULTS = 10
ZHIHU_MAX_QUERY_LENGTH = 100


class ZhihuCollectionError(ValueError):
    """Raised when a Zhihu API request or response is invalid."""


def _non_empty(value: Any, name: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ZhihuCollectionError(f"{name} must be a non-empty string")
    return value.strip()


def _created_at(value: Optional[datetime] = None) -> str:
    current = value or datetime.now(timezone.utc).astimezone()
    if current.tzinfo is None:
        raise ZhihuCollectionError("created_at must include a timezone")
    return current.isoformat(timespec="seconds")


def build_zhihu_api_query(query: str) -> str:
    """Disambiguate a bare WBC query while preserving user intent."""

    normalized = _non_empty(query, "query")
    lower = normalized.lower()
    markers = (
        "robot", "humanoid", "quadruped", "unitree", "g1",
        "机器人", "人形", "四足", "全身控制", "whole body", "whole-body",
    )
    if re.search(r"\bwbc\b", lower) and not any(marker in lower for marker in markers):
        normalized += " 人形机器人 全身控制"
    if not 2 <= len(normalized) <= ZHIHU_MAX_QUERY_LENGTH:
        raise ZhihuCollectionError(
            f"Zhihu query length must be in [2, {ZHIHU_MAX_QUERY_LENGTH}]"
        )
    return normalized


class ZhihuApiClient:
    """Minimal client for Zhihu's official invited-preview search endpoint."""

    def __init__(
        self,
        access_secret: str,
        *,
        base_url: str = ZHIHU_API_BASE_URL,
        timeout: float = 30.0,
        opener: Any = None,
        clock: Any = None,
    ) -> None:
        self._access_secret = _non_empty(access_secret, "Zhihu access secret")
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self._opener = opener or request.urlopen
        self._clock = clock or time.time

    @classmethod
    def from_environment(
        cls, env_name: str = ZHIHU_DEFAULT_SECRET_ENV, **kwargs: Any
    ) -> "ZhihuApiClient":
        env_name = _non_empty(env_name, "secret environment variable")
        secret = os.environ.get(env_name)
        if not secret:
            raise ZhihuCollectionError(
                f"{env_name} is not set; put the Zhihu Access Secret in that "
                "environment variable, never in the repository or CLI arguments"
            )
        return cls(secret, **kwargs)

    def search(self, query: str, count: int = ZHIHU_MAX_RESULTS) -> Dict[str, Any]:
        if not 1 <= count <= ZHIHU_MAX_RESULTS:
            raise ZhihuCollectionError(
                f"Zhihu Count must be in [1, {ZHIHU_MAX_RESULTS}]"
            )
        params = parse.urlencode({"Query": build_zhihu_api_query(query), "Count": count})
        api_request = request.Request(
            f"{self.base_url}{ZHIHU_SEARCH_PATH}?{params}",
            headers={
                "Authorization": f"Bearer {self._access_secret}",
                "X-Request-Timestamp": str(int(self._clock())),
                "Content-Type": "application/json",
                "Accept": "application/json",
                "User-Agent": "Humanoid-WBC-Handbook/1.0",
            },
            method="GET",
        )
        try:
            with self._opener(api_request, timeout=self.timeout) as response:
                body = response.read()
        except error.HTTPError as exc:
            body = exc.read(8192).decode("utf-8", errors="replace")
            message = body
            try:
                payload = json.loads(body)
                message = payload.get("message") or payload.get("detail") or body
            except json.JSONDecodeError:
                pass
            raise ZhihuCollectionError(
                f"Zhihu API returned HTTP {exc.code}: {str(message)[:500]}"
            ) from exc
        except error.URLError as exc:
            raise ZhihuCollectionError(f"Zhihu API request failed: {exc.reason}") from exc
        try:
            payload = json.loads(body.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            raise ZhihuCollectionError("Zhihu API returned invalid JSON") from exc
        if not isinstance(payload, dict):
            raise ZhihuCollectionError("Zhihu API response must be one JSON object")
        return payload


def _validate_queries(queries: Sequence[Mapping[str, Any]]) -> List[Dict[str, Any]]:
    normalized: List[Dict[str, Any]] = []
    for index, item in enumerate(queries):
        if not isinstance(item, Mapping):
            raise ZhihuCollectionError(f"queries[{index}] must be an object")
        scope_id = _non_empty(item.get("scope_id"), f"queries[{index}].scope_id")
        if not re.fullmatch(r"[a-z0-9][a-z0-9_]{2,63}", scope_id):
            raise ZhihuCollectionError(f"queries[{index}].scope_id has an invalid format")
        domain_hints = item.get("domain_hints", [])
        if not isinstance(domain_hints, list) or not all(
            isinstance(value, str) and value for value in domain_hints
        ):
            raise ZhihuCollectionError(f"queries[{index}].domain_hints must be strings")
        raw_query = _non_empty(item.get("query"), f"queries[{index}].query")
        normalized.append({
            "scope_id": scope_id,
            "domain_hints": list(dict.fromkeys(domain_hints)),
            "query": raw_query,
            "api_query": build_zhihu_api_query(raw_query),
        })
    return normalized


def build_zhihu_collection_plan(
    queries: Sequence[Mapping[str, Any]],
    *,
    count: int = ZHIHU_MAX_RESULTS,
    created_at: Optional[datetime] = None,
) -> Dict[str, Any]:
    """Return a no-network plan for access and query review."""

    normalized = _validate_queries(queries)
    if not 1 <= count <= ZHIHU_MAX_RESULTS:
        raise ZhihuCollectionError(
            f"Zhihu Count must be in [1, {ZHIHU_MAX_RESULTS}]"
        )
    created = _created_at(created_at)
    fingerprint = hashlib.sha256(
        (created + "\n" + "\n".join(item["api_query"] for item in normalized)).encode()
    ).hexdigest()[:12]
    return {
        "schema_version": 1,
        "run_id": f"zhihu-plan-{re.sub(r'[^0-9]', '', created)[:14]}-{fingerprint}",
        "created_at": created,
        "trigger": "manual_on_demand",
        "platform": "zhihu",
        "access_mode": "public_api",
        "endpoint": ZHIHU_API_BASE_URL + ZHIHU_SEARCH_PATH,
        "count_per_query": count,
        "queries": normalized,
        "credential": {
            "source": "environment",
            "default_variable": ZHIHU_DEFAULT_SECRET_ENV,
            "persisted": False,
            "access": "invited_preview",
        },
        "limitations": {
            "full_text": False,
            "complete_comments": False,
            "pagination": False,
            "max_results_per_query": ZHIHU_MAX_RESULTS,
        },
    }


def _ci_get(item: Mapping[str, Any], *names: str) -> Any:
    lower = {str(key).lower(): value for key, value in item.items()}
    for name in names:
        if name in item:
            return item[name]
        if name.lower() in lower:
            return lower[name.lower()]
    return None


def _response_items(payload: Mapping[str, Any]) -> List[Mapping[str, Any]]:
    for name in ("Data", "data", "Results", "results", "Items", "items"):
        value = payload.get(name)
        if isinstance(value, list):
            return [item for item in value if isinstance(item, Mapping)]
        if isinstance(value, Mapping):
            for nested_name in ("Data", "data", "Results", "results", "Items", "items"):
                nested = value.get(nested_name)
                if isinstance(nested, list):
                    return [item for item in nested if isinstance(item, Mapping)]
    return []


def _safe_number(value: Any) -> Optional[float]:
    if isinstance(value, bool) or value is None:
        return None
    try:
        parsed = float(value)
    except (TypeError, ValueError):
        return None
    return parsed if parsed >= 0 else None


def _candidate(item: Mapping[str, Any], match: Mapping[str, Any]) -> Optional[Dict[str, Any]]:
    raw_url = _ci_get(item, "URL", "Url", "url", "ContentURL", "ContentUrl")
    if not isinstance(raw_url, str) or not raw_url.strip():
        return None
    try:
        canonical_url, post_id = canonicalize_social_url("zhihu", raw_url)
    except SocialCollectionError:
        return None
    content_type = _ci_get(item, "ContentType", "Type", "type")
    title = _ci_get(item, "Title", "title")
    summary = _ci_get(
        item, "ContentText", "Summary", "Excerpt", "Description", "content_text"
    )
    if not isinstance(title, str) or not title.strip():
        title = f"知乎{content_type or '内容'} {post_id}"
    if not isinstance(summary, str):
        summary = ""
    author = _ci_get(item, "Author", "AuthorName", "author", "author_name")
    if isinstance(author, Mapping):
        author = _ci_get(author, "Name", "name", "Headline", "headline")
    metrics = {}
    for output_name, aliases in {
        "comments": ("CommentCount", "CommentsCount", "comment_count"),
        "voteups": ("VoteupCount", "VoteCount", "voteup_count"),
        "followers": ("FollowerCount", "follower_count"),
    }.items():
        parsed = _safe_number(_ci_get(item, *aliases))
        if parsed is not None:
            metrics[output_name] = parsed
    selected_comments = _ci_get(item, "SelectedComments", "selected_comments")
    if not isinstance(selected_comments, list):
        selected_comments = []
    return {
        "platform": "zhihu",
        "content_id": str(_ci_get(item, "ContentID", "ID", "id") or post_id),
        "content_type": str(content_type or "unknown"),
        "canonical_url": canonical_url,
        "title": title.strip(),
        "summary": summary.strip(),
        "author_display": author.strip() if isinstance(author, str) else None,
        "published_at": _ci_get(
            item, "CreatedTime", "CreatedAt", "created_time", "created_at"
        ),
        "updated_at": _ci_get(
            item, "UpdatedTime", "UpdatedAt", "updated_time", "updated_at"
        ),
        "attention": metrics,
        "selected_comments": selected_comments[:10],
        "matches": [dict(match)],
        "access_mode": "public_api",
        "review_status": "candidate",
        "full_text_available": False,
    }


def _state_key(api_query: str) -> str:
    return hashlib.sha256(api_query.encode("utf-8")).hexdigest()[:20]


def collect_zhihu_candidates(
    queries: Sequence[Mapping[str, Any]],
    client: ZhihuApiClient,
    *,
    count: int = ZHIHU_MAX_RESULTS,
    previous_state: Optional[Mapping[str, Any]] = None,
    refresh_known: bool = False,
    created_at: Optional[datetime] = None,
) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    """Collect official search summaries and return ``(result, next_state)``."""

    plan = build_zhihu_collection_plan(queries, count=count, created_at=created_at)
    state_before = previous_state if isinstance(previous_state, Mapping) else {}
    old_queries = state_before.get("queries", {})
    if not isinstance(old_queries, Mapping):
        old_queries = {}
    by_url: Dict[str, Dict[str, Any]] = {}
    query_results: List[Dict[str, Any]] = []
    next_query_state: Dict[str, Any] = {}

    for query in plan["queries"]:
        key = _state_key(query["api_query"])
        old_entry = old_queries.get(key, {})
        if not isinstance(old_entry, Mapping) or old_entry.get("api_query") != query["api_query"]:
            old_entry = {}
        seen = {
            str(value) for value in old_entry.get("seen_content_ids", [])
        } if isinstance(old_entry.get("seen_content_ids", []), list) else set()
        payload = client.search(query["api_query"], count=count)
        items = _response_items(payload)
        accepted = 0
        skipped_seen = 0
        unsupported = 0
        returned_ids: List[str] = []
        for item in items:
            candidate = _candidate(item, query)
            if candidate is None:
                unsupported += 1
                continue
            content_id = candidate["content_id"]
            returned_ids.append(content_id)
            if content_id in seen and not refresh_known:
                skipped_seen += 1
                continue
            existing = by_url.get(candidate["canonical_url"])
            if existing is None:
                by_url[candidate["canonical_url"]] = candidate
                accepted += 1
            else:
                existing["matches"].append(dict(query))
        updated_seen = list(dict.fromkeys([*seen, *returned_ids]))[-500:]
        next_query_state[key] = {
            "api_query": query["api_query"],
            "seen_content_ids": updated_seen,
            "last_successful_run": plan["created_at"],
        }
        query_results.append({
            "scope_id": query["scope_id"],
            "query": query["query"],
            "api_query": query["api_query"],
            "returned": len(items),
            "accepted": accepted,
            "skipped_seen": skipped_seen,
            "unsupported_url_or_type": unsupported,
            "has_more": bool(_ci_get(payload, "HasMore", "has_more")),
        })

    result = {
        "schema_version": 1,
        "run_id": plan["run_id"].replace("zhihu-plan-", "zhihu-collect-", 1),
        "created_at": plan["created_at"],
        "trigger": "manual_on_demand",
        "platform": "zhihu",
        "access_mode": "public_api",
        "query_results": query_results,
        "candidates": list(by_url.values()),
        "limitations": plan["limitations"],
        "compliance": {
            "source": "official_zhihu_data_open_platform",
            "web_scraping": False,
            "raw_output_location": "git_ignored_var_only",
            "publish_summaries_and_original_links_only": True,
        },
    }
    next_state = {
        "schema_version": 1,
        "platform": "zhihu",
        "updated_at": plan["created_at"],
        "queries": next_query_state,
    }
    return result, next_state
