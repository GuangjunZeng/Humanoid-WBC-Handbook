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
X_USER_FIELDS = "id,username,name,verified,description"
X_MEDIA_FIELDS = (
    "media_key,type,url,preview_image_url,alt_text,width,height,duration_ms"
)
X_QUERY_LIMITS = {"recent": 512, "all": 1024}
X_PAGE_LIMITS = {"recent": 100, "all": 500}
X_DEFAULT_TOKEN_ENV = "X_BEARER_TOKEN"


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
    ) -> None:
        self._bearer_token = _non_empty(bearer_token, "X bearer token")
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self._opener = opener or request.urlopen

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
        try:
            with self._opener(api_request, timeout=self.timeout) as response:
                body = response.read()
        except error.HTTPError as exc:
            body = exc.read(8192).decode("utf-8", errors="replace")
            message = body
            try:
                payload = json.loads(body)
                message = payload.get("detail") or payload.get("title") or body
            except json.JSONDecodeError:
                pass
            raise XCollectionError(
                f"X API returned HTTP {exc.code}: {str(message)[:500]}"
            ) from exc
        except error.URLError as exc:
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
        "schema_version": 1,
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
        "estimated_post_read_upper_bound": (
            len(normalized) * max_posts_per_query + len(post_ids)
        ),
    }


def _included_maps(payload: Mapping[str, Any]) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    includes = payload.get("includes", {})
    if not isinstance(includes, Mapping):
        includes = {}
    users = includes.get("users", [])
    media = includes.get("media", [])
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
    return user_map, media_map


def _safe_media(item: Mapping[str, Any]) -> Dict[str, Any]:
    allowed = {
        "media_key", "type", "url", "preview_image_url", "alt_text",
        "width", "height", "duration_ms",
    }
    return {key: item[key] for key in allowed if item.get(key) is not None}


def _post_candidate(
    post: Mapping[str, Any],
    users: Mapping[str, Any],
    media: Mapping[str, Any],
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

    note_tweet = post.get("note_tweet")
    text = post.get("text", "")
    if isinstance(note_tweet, Mapping) and isinstance(note_tweet.get("text"), str):
        text = note_tweet["text"]
    text = _non_empty(text, f"X post {post_id} text")

    attachments = post.get("attachments", {})
    media_keys = attachments.get("media_keys", []) if isinstance(
        attachments, Mapping
    ) else []
    attached_media = [
        _safe_media(media[str(key)])
        for key in media_keys
        if str(key) in media and isinstance(media[str(key)], Mapping)
    ] if isinstance(media_keys, list) else []

    referenced = post.get("referenced_tweets", [])
    if not isinstance(referenced, list):
        referenced = []
    referenced = [
        {"type": item.get("type"), "id": str(item.get("id"))}
        for item in referenced
        if isinstance(item, Mapping) and item.get("id") is not None
    ]
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
            for key in ("id", "username", "name", "verified", "description")
            if author_raw.get(key) is not None
        },
        "published_at": post.get("created_at"),
        "conversation_id": str(post.get("conversation_id") or post_id),
        "in_reply_to_user_id": post.get("in_reply_to_user_id"),
        "referenced_tweets": referenced,
        "lang": post.get("lang"),
        "entities": post.get("entities", {}),
        "media": attached_media,
        "public_metrics": dict(public_metrics),
        "possibly_sensitive": bool(post.get("possibly_sensitive", False)),
        "withheld": post.get("withheld"),
        "article": post.get("article"),
        "edit_history_tweet_ids": post.get("edit_history_tweet_ids", [post_id]),
        "matches": [dict(match)],
        "access_mode": "public_api",
        "review_status": "candidate",
    }
    return {key: value for key, value in candidate.items() if value is not None}


def _state_key(api_query: str) -> str:
    return hashlib.sha256(api_query.encode("utf-8")).hexdigest()[:20]


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
    state_before = previous_state if isinstance(previous_state, Mapping) else {}
    old_queries = state_before.get("queries", {})
    if not isinstance(old_queries, Mapping):
        old_queries = {}

    by_id: Dict[str, Dict[str, Any]] = {}
    query_results: List[Dict[str, Any]] = []
    next_query_state: Dict[str, Any] = {}

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
        payload = client.get_json("/tweets", params)
        users, media = _included_maps(payload)
        returned = 0
        for post in payload.get("data", []):
            if not isinstance(post, Mapping):
                continue
            merge(_post_candidate(post, users, media, {
                "scope_id": "open_ended_wbc_field_notes",
                "domain_hints": [],
                "query": f"post_id:{post.get('id')}",
                "api_query": "direct_lookup",
            }))
            returned += 1
        query_results.append({
            "kind": "direct_lookup",
            "requested": len(batch),
            "returned": returned,
        })

    for item in plan["queries"]:
        query_key = _state_key(item["api_query"])
        old_entry = old_queries.get(query_key, {})
        if not isinstance(old_entry, Mapping) or old_entry.get("api_query") != item["api_query"]:
            old_entry = {}
        params: Dict[str, Any] = {
            **_request_fields(),
            "query": item["api_query"],
            "max_results": min(
                X_PAGE_LIMITS[mode], max(10, max_posts_per_query)
            ),
            "start_time": start_time,
            "end_time": end_time,
        }
        if mode == "recent" and use_state and not start_time and old_entry.get("newest_id"):
            params["since_id"] = old_entry["newest_id"]

        received_ids: List[str] = []
        page_count = 0
        next_token: Optional[str] = None
        while page_count < max_pages and len(received_ids) < max_posts_per_query:
            page_params = dict(params)
            if next_token:
                page_params["next_token"] = next_token
            payload = client.get_json(X_SEARCH_PATHS[mode], page_params)
            users, media = _included_maps(payload)
            remaining = max_posts_per_query - len(received_ids)
            data = payload.get("data", [])
            if not isinstance(data, list):
                data = []
            for post in data[:remaining]:
                if not isinstance(post, Mapping):
                    continue
                candidate = _post_candidate(post, users, media, item)
                received_ids.append(candidate["post_id"])
                merge(candidate)
            page_count += 1
            meta = payload.get("meta", {})
            next_token = meta.get("next_token") if isinstance(meta, Mapping) else None
            if not next_token or not data:
                break

        newest_id = _numeric_max([
            old_entry.get("newest_id"), *received_ids
        ])
        next_query_state[query_key] = {
            "api_query": item["api_query"],
            "newest_id": newest_id,
            "last_successful_run": plan["created_at"],
        }
        query_results.append({
            "kind": "search",
            "scope_id": item["scope_id"],
            "query": item["query"],
            "api_query": item["api_query"],
            "pages": page_count,
            "returned": len(received_ids),
            "incremental_since_id": params.get("since_id"),
            "newest_id": newest_id,
        })

    result = {
        "schema_version": 1,
        "run_id": plan["run_id"].replace("x-plan-", "x-collect-", 1),
        "created_at": plan["created_at"],
        "trigger": "manual_on_demand",
        "platform": "x",
        "access_mode": "public_api",
        "mode": mode,
        "query_results": query_results,
        "candidates": list(by_id.values()),
        "compliance": {
            "source": "official_x_api_v2",
            "web_scraping": False,
            "raw_output_location": "git_ignored_var_only",
            "publish_summaries_and_post_links_only": True,
        },
    }
    next_state = {
        "schema_version": 1,
        "platform": "x",
        "updated_at": plan["created_at"],
        "queries": next_query_state,
    }
    return result, next_state
