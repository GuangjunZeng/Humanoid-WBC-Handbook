"""User-triggered collection from the official X API v2.

The collector never automates x.com pages and never accepts a bearer token on
the command line. Raw API candidates belong under ignored ``var/``; only later
human-reviewed summaries and stable post links may enter the evidence store.
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

from .models import parse_aware_datetime


X_API_BASE_URL = "https://api.x.com/2"
X_SEARCH_PATHS = {
    "recent": "/tweets/search/recent",
    "all": "/tweets/search/all",
}
X_POST_FIELDS = (
    "id,text,author_id,created_at,conversation_id,in_reply_to_user_id,"
    "referenced_tweets,entities,attachments,public_metrics,lang,note_tweet,"
    "article,edit_history_tweet_ids,reply_settings,possibly_sensitive,withheld"
)
X_EXPANSIONS = (
    "author_id,referenced_tweets.id,referenced_tweets.id.author_id,"
    "attachments.media_keys"
)
X_USER_FIELDS = (
    "id,username,name,verified,verified_type,description,protected,public_metrics"
)
X_MEDIA_FIELDS = (
    "media_key,type,url,preview_image_url,alt_text,width,height,duration_ms,"
    "public_metrics,variants"
)
X_QUERY_LIMITS = {"recent": 512, "all": 1024}
X_PAGE_LIMITS = {"recent": 100, "all": 500}
X_DEFAULT_TOKEN_ENV = "X_BEARER_TOKEN"
X_RETRYABLE_HTTP_STATUS = frozenset({429, 500, 502, 503, 504})
X_DEFAULT_MAX_RETRIES = 3
X_DEFAULT_MAX_RETRY_WAIT_SECONDS = 30.0
X_MIN_REQUEST_INTERVAL_SECONDS = {"/tweets/search/all": 1.0}


class XCollectionError(ValueError):
    """Raised when an X collection request or response is invalid."""


def _non_empty(value: Any, name: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise XCollectionError(f"{name} must be a non-empty string")
    return value.strip()


def _created_at(value: Optional[datetime] = None) -> str:
    current = value or datetime.now(timezone.utc).astimezone()
    if current.tzinfo is None:
        raise XCollectionError("created_at must include a timezone")
    return current.isoformat(timespec="seconds")


def extract_x_post_id(value: str) -> str:
    """Accept a numeric post ID or one x.com/twitter.com status URL."""

    raw = _non_empty(value, "X post ID or URL")
    if re.fullmatch(r"\d+", raw):
        return raw
    parsed = parse.urlparse(raw)
    host = (parsed.hostname or "").lower()
    if host not in {"x.com", "www.x.com", "twitter.com", "www.twitter.com"}:
        raise XCollectionError("X post URL must use x.com or twitter.com")
    match = re.fullmatch(
        r"/(?:[A-Za-z0-9_]{1,15}/status|i/web/status)/(\d+)"
        r"(?:/(?:photo|video)/\d+)?/?",
        parsed.path,
    )
    if not match:
        raise XCollectionError("X URL must identify one /<username>/status/<id> post")
    return match.group(1)


def build_x_api_query(query: str, mode: str = "recent") -> str:
    """Build a high-precision X query without confusing WBC with blood cells."""

    if mode not in X_SEARCH_PATHS:
        raise XCollectionError("X search mode must be recent or all")
    normalized = _non_empty(query, "query")
    lower = normalized.lower()
    robot_markers = (
        "robot", "robotics", "humanoid", "quadruped", "unitree", "g1",
        "机器人", "人形", "四足", "全身控制", "whole body", "whole-body",
    )
    if re.search(r"\bwbc\b", lower) and not any(
        marker in lower for marker in robot_markers
    ):
        normalized = (
            f"({normalized}) "
            "(robot OR robotics OR humanoid OR quadruped OR Unitree)"
        )
    if "is:retweet" not in lower:
        normalized += " -is:retweet"
    if len(normalized) > X_QUERY_LIMITS[mode]:
        raise XCollectionError(
            f"X {mode} query exceeds the {X_QUERY_LIMITS[mode]}-character limit"
        )
    return normalized


def _request_fields() -> Dict[str, str]:
    return {
        "tweet.fields": X_POST_FIELDS,
        "expansions": X_EXPANSIONS,
        "user.fields": X_USER_FIELDS,
        "media.fields": X_MEDIA_FIELDS,
    }


class XApiClient:
    """Minimal dependency-free client for official X API v2 read endpoints."""

    def __init__(
        self,
        bearer_token: str,
        *,
        base_url: str = X_API_BASE_URL,
        timeout: float = 30.0,
        opener: Any = None,
        max_retries: int = X_DEFAULT_MAX_RETRIES,
        max_retry_wait_seconds: float = X_DEFAULT_MAX_RETRY_WAIT_SECONDS,
        sleeper: Any = None,
        clock: Any = None,
    ) -> None:
        self._bearer_token = _non_empty(bearer_token, "X bearer token")
        self.base_url = base_url.rstrip("/")
        if timeout <= 0:
            raise XCollectionError("X API timeout must be positive")
        if not 0 <= max_retries <= 10:
            raise XCollectionError("X API max_retries must be in [0, 10]")
        if not 0 <= max_retry_wait_seconds <= 60:
            raise XCollectionError(
                "X API max_retry_wait_seconds must be in [0, 60]"
            )
        self.timeout = timeout
        self.max_retries = max_retries
        self.max_retry_wait_seconds = max_retry_wait_seconds
        self._opener = opener or request.urlopen
        self._sleep = sleeper or time.sleep
        self._clock = clock or time.time
        self._last_request_at: Dict[str, float] = {}

    @classmethod
    def from_environment(
        cls, env_name: str = X_DEFAULT_TOKEN_ENV, **kwargs: Any
    ) -> "XApiClient":
        env_name = _non_empty(env_name, "token environment variable")
        token = os.environ.get(env_name)
        if not token:
            raise XCollectionError(
                f"{env_name} is not set; put the X API bearer token in that "
                "environment variable, never in the repository or CLI arguments"
            )
        return cls(token, **kwargs)

    def _retry_delay(self, headers: Any, attempt: int) -> float:
        retry_after = headers.get("Retry-After") if headers is not None else None
        if retry_after is not None:
            try:
                return min(
                    self.max_retry_wait_seconds,
                    max(0.0, float(retry_after)),
                )
            except (TypeError, ValueError):
                pass
        reset = headers.get("x-rate-limit-reset") if headers is not None else None
        if reset is not None:
            try:
                return min(
                    self.max_retry_wait_seconds,
                    max(0.0, float(reset) - float(self._clock()) + 1.0),
                )
            except (TypeError, ValueError):
                pass
        return min(self.max_retry_wait_seconds, float(2 ** attempt))

    @staticmethod
    def _http_error_message(exc: error.HTTPError) -> str:
        body = exc.read(8192).decode("utf-8", errors="replace")
        message = body
        try:
            payload = json.loads(body)
            if isinstance(payload, Mapping):
                message = payload.get("detail") or payload.get("title") or body
        except json.JSONDecodeError:
            pass
        return str(message)[:500]

    def _throttle(self, path: str) -> None:
        interval = X_MIN_REQUEST_INTERVAL_SECONDS.get(path, 0.0)
        last_request = self._last_request_at.get(path)
        now = float(self._clock())
        if last_request is not None and now - last_request < interval:
            self._sleep(interval - (now - last_request))
            now = float(self._clock())
        self._last_request_at[path] = now

    def get_json(self, path: str, params: Mapping[str, Any]) -> Dict[str, Any]:
        encoded = parse.urlencode(
            [(key, value) for key, value in params.items() if value is not None]
        )
        url = f"{self.base_url}{path}"
        if encoded:
            url += "?" + encoded
        api_request = request.Request(
            url,
            headers={
                "Authorization": f"Bearer {self._bearer_token}",
                "Accept": "application/json",
                "User-Agent": "Humanoid-WBC-Handbook/1.0",
            },
            method="GET",
        )
        body: bytes = b""
        for attempt in range(self.max_retries + 1):
            self._throttle(path)
            try:
                with self._opener(api_request, timeout=self.timeout) as response:
                    body = response.read()
                break
            except error.HTTPError as exc:
                message = self._http_error_message(exc)
                if (
                    exc.code in X_RETRYABLE_HTTP_STATUS
                    and attempt < self.max_retries
                ):
                    self._sleep(self._retry_delay(exc.headers, attempt))
                    continue
                raise XCollectionError(
                    f"X API returned HTTP {exc.code}: {message}"
                ) from exc
            except error.URLError as exc:
                if attempt < self.max_retries:
                    self._sleep(self._retry_delay(None, attempt))
                    continue
                raise XCollectionError(f"X API request failed: {exc.reason}") from exc
        try:
            payload = json.loads(body.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            raise XCollectionError("X API returned invalid JSON") from exc
        if not isinstance(payload, dict):
            raise XCollectionError("X API response must be one JSON object")
        if payload.get("errors") and not payload.get("data"):
            raise XCollectionError(
                "X API response contained errors: "
                + json.dumps(payload["errors"], ensure_ascii=False)[:1000]
            )
        return payload


def _validate_query_records(
    queries: Sequence[Mapping[str, Any]], mode: str
) -> List[Dict[str, Any]]:
    if mode not in X_SEARCH_PATHS:
        raise XCollectionError("X search mode must be recent or all")
    normalized: List[Dict[str, Any]] = []
    for index, item in enumerate(queries):
        if not isinstance(item, Mapping):
            raise XCollectionError(f"queries[{index}] must be an object")
        scope_id = _non_empty(item.get("scope_id"), f"queries[{index}].scope_id")
        if not re.fullmatch(r"[a-z0-9][a-z0-9_]{2,63}", scope_id):
            raise XCollectionError(f"queries[{index}].scope_id has an invalid format")
        domain_hints = item.get("domain_hints", [])
        if not isinstance(domain_hints, list) or not all(
            isinstance(value, str) and value for value in domain_hints
        ):
            raise XCollectionError(f"queries[{index}].domain_hints must be strings")
        raw_query = _non_empty(item.get("query"), f"queries[{index}].query")
        normalized.append({
            "scope_id": scope_id,
            "domain_hints": list(dict.fromkeys(domain_hints)),
            "query": raw_query,
            "api_query": build_x_api_query(raw_query, mode),
        })
    return normalized


def build_x_collection_plan(
    queries: Sequence[Mapping[str, Any]],
    *,
    mode: str = "recent",
    max_posts_per_query: int = 10,
    max_pages: int = 1,
    direct_post_ids: Sequence[str] = (),
    created_at: Optional[datetime] = None,
) -> Dict[str, Any]:
    """Return a no-network plan suitable for cost and query review."""

    normalized = _validate_query_records(queries, mode)
    if not 1 <= max_posts_per_query <= 5000:
        raise XCollectionError("max_posts_per_query must be in [1, 5000]")
    if not 1 <= max_pages <= 50:
        raise XCollectionError("max_pages must be in [1, 50]")
    post_ids = list(dict.fromkeys(extract_x_post_id(value) for value in direct_post_ids))
    created = _created_at(created_at)
    fingerprint = hashlib.sha256(
        (created + "\n" + "\n".join(item["api_query"] for item in normalized)).encode()
    ).hexdigest()[:12]
    return {
        "schema_version": 2,
        "run_id": f"x-plan-{re.sub(r'[^0-9]', '', created)[:14]}-{fingerprint}",
        "created_at": created,
        "trigger": "manual_on_demand",
        "platform": "x",
        "access_mode": "public_api",
        "mode": mode,
        "endpoint": X_API_BASE_URL + X_SEARCH_PATHS[mode],
        "max_posts_per_query": max_posts_per_query,
        "max_pages": max_pages,
        "direct_post_ids": post_ids,
        "queries": normalized,
        "credential": {
            "source": "environment",
            "default_variable": X_DEFAULT_TOKEN_ENV,
            "persisted": False,
        },
        "recovery": {
            "retryable_http_status": sorted(X_RETRYABLE_HTTP_STATUS),
            "pagination_cursor_persisted": True,
            "advance_since_id_only_after_window_complete": True,
            "full_archive_min_request_interval_seconds": 1.0,
        },
        "estimated_post_read_upper_bound": (
            len(normalized) * max(10, max_posts_per_query) + len(post_ids)
        ),
    }


def _included_maps(
    payload: Mapping[str, Any]
) -> Tuple[Dict[str, Any], Dict[str, Any], Dict[str, Any]]:
    includes = payload.get("includes", {})
    if not isinstance(includes, Mapping):
        includes = {}
    users = includes.get("users", [])
    media = includes.get("media", [])
    posts = includes.get("tweets", includes.get("posts", []))
    user_map = {
        str(item["id"]): item
        for item in users
        if isinstance(item, Mapping) and item.get("id") is not None
    } if isinstance(users, list) else {}
    media_map = {
        str(item["media_key"]): item
        for item in media
        if isinstance(item, Mapping) and item.get("media_key") is not None
    } if isinstance(media, list) else {}
    post_map = {
        str(item["id"]): item
        for item in posts
        if isinstance(item, Mapping) and item.get("id") is not None
    } if isinstance(posts, list) else {}
    return user_map, media_map, post_map


def _safe_media(item: Mapping[str, Any]) -> Dict[str, Any]:
    allowed = {
        "media_key", "type", "url", "preview_image_url", "alt_text",
        "width", "height", "duration_ms", "public_metrics", "variants",
    }
    return {key: item[key] for key in allowed if item.get(key) is not None}


def _post_text(post: Mapping[str, Any], post_id: str) -> str:
    note = post.get("note_tweet", post.get("note_post"))
    text = post.get("text", "")
    if isinstance(note, Mapping) and isinstance(note.get("text"), str):
        text = note["text"]
    return _non_empty(text, f"X post {post_id} text")


def _safe_api_errors(payload: Mapping[str, Any]) -> List[Dict[str, Any]]:
    errors = payload.get("errors", [])
    if not isinstance(errors, list):
        return []
    allowed = (
        "resource_id", "resource_type", "title", "detail", "type",
        "status", "parameter", "value",
    )
    return [
        {key: item[key] for key in allowed if item.get(key) is not None}
        for item in errors
        if isinstance(item, Mapping)
    ]


def _safe_referenced_posts(
    references: Sequence[Mapping[str, Any]],
    posts: Mapping[str, Any],
    users: Mapping[str, Any],
) -> List[Dict[str, Any]]:
    normalized: List[Dict[str, Any]] = []
    for reference in references:
        post_id = str(reference.get("id", ""))
        included = posts.get(post_id, {})
        if not isinstance(included, Mapping):
            included = {}
        author = users.get(str(included.get("author_id", "")), {})
        if not isinstance(author, Mapping):
            author = {}
        username = author.get("username")
        canonical_url = f"https://x.com/i/web/status/{post_id}"
        if isinstance(username, str) and re.fullmatch(
            r"[A-Za-z0-9_]{1,15}", username
        ):
            canonical_url = f"https://x.com/{username}/status/{post_id}"
        item: Dict[str, Any] = {
            "type": reference.get("type"),
            "id": post_id,
            "canonical_url": canonical_url,
        }
        if included:
            try:
                item["text"] = _post_text(included, post_id)
            except XCollectionError:
                pass
            if author:
                item["author"] = {
                    key: author[key]
                    for key in ("id", "username", "name")
                    if author.get(key) is not None
                }
        normalized.append(item)
    return normalized


def _post_candidate(
    post: Mapping[str, Any],
    users: Mapping[str, Any],
    media: Mapping[str, Any],
    included_posts: Mapping[str, Any],
    match: Mapping[str, Any],
) -> Dict[str, Any]:
    post_id = _non_empty(str(post.get("id", "")), "X post id")
    author_id = str(post.get("author_id", ""))
    author_raw = users.get(author_id, {})
    if not isinstance(author_raw, Mapping):
        author_raw = {}
    username = author_raw.get("username")
    if isinstance(username, str) and re.fullmatch(r"[A-Za-z0-9_]{1,15}", username):
        canonical_url = f"https://x.com/{username}/status/{post_id}"
    else:
        canonical_url = f"https://x.com/i/web/status/{post_id}"

    text = _post_text(post, post_id)

    attachments = post.get("attachments", {})
    media_keys = attachments.get("media_keys", []) if isinstance(
        attachments, Mapping
    ) else []
    attached_media = [
        _safe_media(media[str(key)])
        for key in media_keys
        if str(key) in media and isinstance(media[str(key)], Mapping)
    ] if isinstance(media_keys, list) else []

    referenced = post.get("referenced_tweets", post.get("referenced_posts", []))
    if not isinstance(referenced, list):
        referenced = []
    referenced = [
        {"type": item.get("type"), "id": str(item.get("id"))}
        for item in referenced
        if isinstance(item, Mapping) and item.get("id") is not None
    ]
    referenced_posts = _safe_referenced_posts(
        referenced, included_posts, users
    )
    public_metrics = post.get("public_metrics", {})
    if not isinstance(public_metrics, Mapping):
        public_metrics = {}

    candidate: Dict[str, Any] = {
        "platform": "x",
        "post_id": post_id,
        "canonical_url": canonical_url,
        "text": text,
        "author": {
            key: author_raw[key]
            for key in (
                "id", "username", "name", "verified", "verified_type",
                "description", "protected", "public_metrics",
            )
            if author_raw.get(key) is not None
        },
        "published_at": post.get("created_at"),
        "conversation_id": str(post.get("conversation_id") or post_id),
        "in_reply_to_user_id": post.get("in_reply_to_user_id"),
        "referenced_tweets": referenced,
        "referenced_posts": referenced_posts,
        "lang": post.get("lang"),
        "entities": post.get("entities", {}),
        "media": attached_media,
        "visual_analysis_pending": bool(attached_media),
        "public_metrics": dict(public_metrics),
        "possibly_sensitive": bool(post.get("possibly_sensitive", False)),
        "withheld": post.get("withheld"),
        "article": post.get("article"),
        "edit_history_tweet_ids": post.get(
            "edit_history_tweet_ids",
            post.get("edit_history_post_ids", [post_id]),
        ),
        "matches": [dict(match)],
        "content_collected": True,
        "full_text_available": True,
        "access_mode": "public_api",
        "review_status": "candidate",
    }
    return {key: value for key, value in candidate.items() if value is not None}


def _legacy_state_key(api_query: str) -> str:
    return hashlib.sha256(api_query.encode("utf-8")).hexdigest()[:20]


def _state_key(
    api_query: str,
    mode: str,
    start_time: Optional[str],
    end_time: Optional[str],
    sort_order: str,
) -> str:
    signature = json.dumps({
        "api_query": api_query,
        "mode": mode,
        "start_time": start_time,
        "end_time": end_time,
        "sort_order": sort_order,
    }, sort_keys=True)
    return hashlib.sha256(signature.encode("utf-8")).hexdigest()[:20]


def _numeric_max(values: Sequence[Optional[str]]) -> Optional[str]:
    usable = [value for value in values if value and str(value).isdigit()]
    return max((str(value) for value in usable), key=int) if usable else None


def collect_x_candidates(
    queries: Sequence[Mapping[str, Any]],
    client: XApiClient,
    *,
    mode: str = "recent",
    max_posts_per_query: int = 10,
    max_pages: int = 1,
    direct_post_ids: Sequence[str] = (),
    previous_state: Optional[Mapping[str, Any]] = None,
    use_state: bool = True,
    start_time: Optional[str] = None,
    end_time: Optional[str] = None,
    sort_order: str = "recency",
    created_at: Optional[datetime] = None,
) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    """Collect bounded X candidates and return ``(result, next_state)``."""

    plan = build_x_collection_plan(
        queries,
        mode=mode,
        max_posts_per_query=max_posts_per_query,
        max_pages=max_pages,
        direct_post_ids=direct_post_ids,
        created_at=created_at,
    )
    for name, value in (("start_time", start_time), ("end_time", end_time)):
        if value is not None:
            parse_aware_datetime(value, name)
    if sort_order not in {"recency", "relevancy"}:
        raise XCollectionError("X sort_order must be recency or relevancy")
    state_before = previous_state if isinstance(previous_state, Mapping) else {}
    old_queries = state_before.get("queries", {})
    if not isinstance(old_queries, Mapping):
        old_queries = {}

    by_id: Dict[str, Dict[str, Any]] = {}
    query_results: List[Dict[str, Any]] = []
    next_query_state: Dict[str, Any] = {
        str(key): dict(value)
        for key, value in old_queries.items()
        if isinstance(value, Mapping)
    }

    def merge(candidate: Dict[str, Any]) -> None:
        existing = by_id.get(candidate["post_id"])
        if existing is None:
            by_id[candidate["post_id"]] = candidate
            return
        known = {
            json.dumps(item, ensure_ascii=False, sort_keys=True)
            for item in existing["matches"]
        }
        for item in candidate["matches"]:
            marker = json.dumps(item, ensure_ascii=False, sort_keys=True)
            if marker not in known:
                existing["matches"].append(item)
                known.add(marker)

    post_ids = plan["direct_post_ids"]
    for start in range(0, len(post_ids), 100):
        batch = post_ids[start:start + 100]
        params = {**_request_fields(), "ids": ",".join(batch)}
        try:
            payload = client.get_json("/tweets", params)
        except XCollectionError as exc:
            query_results.append({
                "kind": "direct_lookup",
                "requested": len(batch),
                "returned": 0,
                "missing_ids": batch,
                "api_errors": [],
                "complete": False,
                "request_error": str(exc),
                "retry_required": True,
            })
            continue
        users, media, included_posts = _included_maps(payload)
        returned = 0
        returned_ids = []
        direct_data = payload.get("data", [])
        if not isinstance(direct_data, list):
            direct_data = []
        for post in direct_data:
            if not isinstance(post, Mapping):
                continue
            merge(_post_candidate(post, users, media, included_posts, {
                "scope_id": "open_ended_wbc_field_notes",
                "domain_hints": [],
                "query": f"post_id:{post.get('id')}",
                "api_query": "direct_lookup",
            }))
            returned += 1
            returned_ids.append(str(post.get("id")))
        query_results.append({
            "kind": "direct_lookup",
            "requested": len(batch),
            "returned": returned,
            "missing_ids": [value for value in batch if value not in returned_ids],
            "api_errors": _safe_api_errors(payload),
            "complete": True,
        })

    for item in plan["queries"]:
        query_key = _state_key(
            item["api_query"], mode, start_time, end_time, sort_order
        )
        old_entry = old_queries.get(query_key, {})
        if (
            not old_entry
            and mode == "recent"
            and start_time is None
            and end_time is None
            and sort_order == "recency"
        ):
            legacy_key = _legacy_state_key(item["api_query"])
            old_entry = old_queries.get(legacy_key, {})
            if old_entry:
                next_query_state.pop(legacy_key, None)
        if (
            not isinstance(old_entry, Mapping)
            or old_entry.get("api_query") != item["api_query"]
        ):
            old_entry = {}

        if (
            use_state
            and start_time is not None
            and end_time is not None
            and old_entry.get("window_complete") is True
        ):
            next_query_state[query_key] = dict(old_entry)
            query_results.append({
                "kind": "search",
                "scope_id": item["scope_id"],
                "query": item["query"],
                "api_query": item["api_query"],
                "pages": 0,
                "returned": 0,
                "newest_id": old_entry.get("newest_id"),
                "resumed": False,
                "complete": True,
                "resume_pending": False,
                "skipped_completed_window": True,
                "api_errors": [],
                "request_error": None,
                "retry_required": False,
            })
            continue

        pending = old_entry.get("pending", {}) if use_state else {}
        if not isinstance(pending, Mapping):
            pending = {}
        resumed = bool(pending.get("next_token"))
        next_token: Optional[str] = (
            str(pending["next_token"]) if resumed else None
        )
        window_newest_id = (
            str(pending["window_newest_id"])
            if pending.get("window_newest_id") is not None
            else None
        )
        params: Dict[str, Any] = {
            **_request_fields(),
            "query": item["api_query"],
            "start_time": start_time,
            "end_time": end_time,
            "sort_order": sort_order,
        }
        if mode == "recent" and use_state and not start_time:
            if pending.get("since_id"):
                params["since_id"] = pending["since_id"]
            elif old_entry.get("newest_id"):
                params["since_id"] = old_entry["newest_id"]

        received_ids: List[str] = []
        page_count = 0
        api_errors: List[Dict[str, Any]] = []
        request_error: Optional[str] = None
        while page_count < max_pages and len(received_ids) < max_posts_per_query:
            remaining = max_posts_per_query - len(received_ids)
            page_params = dict(params)
            page_params["max_results"] = min(
                X_PAGE_LIMITS[mode], max(10, remaining)
            )
            if next_token:
                page_params["next_token"] = next_token
            try:
                payload = client.get_json(X_SEARCH_PATHS[mode], page_params)
            except XCollectionError as exc:
                request_error = str(exc)
                break
            users, media, included_posts = _included_maps(payload)
            data = payload.get("data", [])
            if not isinstance(data, list):
                data = []
            for post in data:
                if not isinstance(post, Mapping):
                    continue
                candidate = _post_candidate(
                    post, users, media, included_posts, item
                )
                received_ids.append(candidate["post_id"])
                merge(candidate)
            api_errors.extend(_safe_api_errors(payload))
            page_count += 1
            meta = payload.get("meta", {})
            if not isinstance(meta, Mapping):
                meta = {}
            if window_newest_id is None:
                window_newest_id = _numeric_max([
                    str(meta.get("newest_id") or ""), *received_ids
                ])
            next_value = meta.get("next_token")
            next_token = str(next_value) if next_value else None
            if not next_token or not data:
                if not data:
                    next_token = None
                break

        complete = request_error is None and next_token is None
        if complete:
            newest_id = _numeric_max([
                old_entry.get("newest_id"), window_newest_id, *received_ids
            ])
            pending_state = None
        elif next_token is not None:
            newest_id = old_entry.get("newest_id")
            pending_state = {
                "next_token": next_token,
                "since_id": params.get("since_id"),
                "window_newest_id": window_newest_id,
                "saved_at": plan["created_at"],
            }
        else:
            newest_id = old_entry.get("newest_id")
            old_pending = old_entry.get("pending")
            pending_state = (
                dict(old_pending) if isinstance(old_pending, Mapping) else None
            )
        state_entry: Dict[str, Any] = {
            "api_query": item["api_query"],
            "mode": mode,
            "start_time": start_time,
            "end_time": end_time,
            "sort_order": sort_order,
            "newest_id": newest_id,
            "last_attempted_run": plan["created_at"],
        }
        if complete:
            state_entry["last_successful_run"] = plan["created_at"]
            if start_time is not None and end_time is not None:
                state_entry["window_complete"] = True
        elif old_entry.get("last_successful_run"):
            state_entry["last_successful_run"] = old_entry["last_successful_run"]
        if pending_state is not None:
            state_entry["pending"] = pending_state
        next_query_state[query_key] = state_entry
        query_results.append({
            "kind": "search",
            "scope_id": item["scope_id"],
            "query": item["query"],
            "api_query": item["api_query"],
            "pages": page_count,
            "returned": len(received_ids),
            "incremental_since_id": params.get("since_id"),
            "newest_id": newest_id,
            "window_newest_id": window_newest_id,
            "resumed": resumed,
            "complete": complete,
            "resume_pending": pending_state is not None,
            "api_errors": api_errors,
            "request_error": request_error,
            "retry_required": request_error is not None,
        })

    result = {
        "schema_version": 2,
        "run_id": plan["run_id"].replace("x-plan-", "x-collect-", 1),
        "created_at": plan["created_at"],
        "trigger": "manual_on_demand",
        "platform": "x",
        "access_mode": "public_api",
        "mode": mode,
        "sort_order": sort_order,
        "query_results": query_results,
        "candidates": list(by_id.values()),
        "stats": {
            "queries_complete": sum(
                1 for item in query_results if item.get("complete") is True
            ),
            "queries_resume_pending": sum(
                1 for item in query_results if item.get("resume_pending") is True
            ),
            "api_errors": sum(
                len(item.get("api_errors", [])) for item in query_results
            ),
            "request_failures": sum(
                1 for item in query_results if item.get("request_error")
            ),
        },
        "compliance": {
            "source": "official_x_api_v2",
            "web_scraping": False,
            "raw_output_location": "git_ignored_var_only",
            "publish_summaries_and_post_links_only": True,
        },
    }
    next_state = {
        "schema_version": 2,
        "platform": "x",
        "updated_at": plan["created_at"],
        "queries": next_query_state,
    }
    return result, next_state
