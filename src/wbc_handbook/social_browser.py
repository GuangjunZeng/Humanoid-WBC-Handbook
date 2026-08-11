"""Contracts for user-triggered collection through a visible signed-in browser.

The browser itself is controlled by the interactive coding agent, not by this
Python package.  This module keeps that execution reproducible: it builds finite
tasks, classifies login/risk-control states, strips transient access parameters,
normalizes extracted pages, and deduplicates them before analysis.

It never reads browser profiles, cookies, local storage, passwords, or tokens.
It never solves CAPTCHAs, bypasses paywalls, schedules background work, or turns
raw community text into reviewed engineering guidance automatically.
"""

from __future__ import annotations

from copy import deepcopy
from datetime import datetime, timezone
import hashlib
import re
from typing import Any, Dict, List, Mapping, Optional, Sequence, Tuple
from urllib.parse import urlparse

from .social import SocialCollectionError, build_search_url, canonicalize_social_url


BROWSER_PLATFORMS = ("xiaohongshu", "zhihu", "x")
BROWSER_PAGE_STATES = (
    "ready",
    "empty_results",
    "login_required",
    "captcha",
    "risk_control",
    "access_denied",
    "unavailable",
)
MAX_BROWSER_RESULTS_PER_QUERY = 10
MAX_BROWSER_COMMENTS = 500
MAX_BROWSER_POSTS_PER_RUN = 30
MAX_BROWSER_BODY_CHARS = 50_000
MAX_BROWSER_COMMENT_CHARS = 1_000
MAX_BROWSER_REPLY_EXPANSIONS = 100
MAX_BROWSER_REPLY_DEPTH = 10
MAX_BROWSER_POST_TIME_BUDGET_SECONDS = 600
MAX_BROWSER_NO_GROWTH_PATIENCE = 5
DEFAULT_BROWSER_COMMENTS = 200
DEFAULT_BROWSER_REPLY_EXPANSIONS = 100
DEFAULT_BROWSER_REPLY_DEPTH = 10
DEFAULT_BROWSER_POST_TIME_BUDGET_SECONDS = 300
DEFAULT_BROWSER_NO_GROWTH_PATIENCE = 3


BROWSER_RECIPES: Dict[str, Dict[str, Any]] = {
    "xiaohongshu": {
        "search": {
            "result_link_selectors": [
                "a[href*='/search_result/']",
                "a[href*='/explore/']",
            ],
            "title_selectors": [".title span", ".note-text", "[class*='title']"],
            "dedupe_key": "canonical_note_url",
            "navigation_href": "resolved DOM href property, not raw href attribute",
        },
        "detail": {
            "title_selectors": ["#detail-title", ".title", "[class*='title']"],
            "body_selectors": ["#detail-desc", ".desc", "[class*='desc']"],
            "author_selectors": [".username", "[class*='author']"],
            "date_selectors": [".date", "[class*='date']"],
            "comment_selectors": [
                ".comment-item",
                ".parent-comment",
                "[class*='comment-inner']",
            ],
            "image_selectors": [
                ".note-slider-img",
                ".swiper-slide img",
                ".note-content img",
            ],
            "expand_comment_text": ["展开更多", "查看更多", "更多回复"],
        },
        "ready_signals": [
            "one or more /explore/<note-id> links on a search page",
            "a non-empty detail title/body on a note page",
            "the signed-in profile link plus real feed cards",
        ],
    },
    "zhihu": {
        "search": {
            "result_link_selectors": [
                "a[href*='/question/'][href*='/answer/']",
                "a[href^='/p/']",
                "a[href*='zhuanlan.zhihu.com/p/']",
            ],
            "title_selectors": ["h2", ".ContentItem-title", "[class*='title']"],
            "dedupe_key": "canonical_answer_or_article_url",
            "navigation_href": "resolved DOM href property, not raw href attribute",
        },
        "detail": {
            "title_selectors": [
                "h1.QuestionHeader-title",
                "h1.Post-Title",
                ".QuestionHeader-title",
            ],
            "body_selectors": [
                ".RichContent-inner",
                ".Post-RichTextContainer",
                ".RichText",
            ],
            "author_selectors": [".AuthorInfo-name", "[class*='AuthorInfo']"],
            "date_selectors": [".ContentItem-time", "[class*='time']"],
            "comment_selectors": [
                ".CommentContent",
                ".CommentItem",
            ],
            "comment_container_selectors": [".Comments-container"],
            "image_selectors": [
                ".Post-RichTextContainer img",
                ".RichContent-inner img",
                "img.origin_image",
                ".RichText img",
            ],
            "expand_comment_text": ["查看全部", "展开其他", "更多回复"],
        },
        "ready_signals": [
            "one or more canonical answer/article links on a search page",
            "a non-empty RichContent-inner answer body",
            "a non-empty Post-RichTextContainer article body",
        ],
    },
    "x": {
        "search": {
            "result_link_selectors": [
                "article[data-testid='tweet'] a[href*='/status/']",
                "article[data-testid='tweet'] time",
            ],
            "title_selectors": [
                "article[data-testid='tweet'] [data-testid='tweetText']",
            ],
            "dedupe_key": "canonical_status_url",
            "navigation_href": "resolved DOM href property, reduced to /<user>/status/<id>",
        },
        "detail": {
            "post_container_selectors": ["article[data-testid='tweet']"],
            "body_selectors": [
                "[data-testid='tweetText']",
                "article[data-testid='tweet']",
            ],
            "article_route_selectors": ["a[href*='/article/']"],
            "author_selectors": ["[data-testid='User-Name']"],
            "date_selectors": ["time"],
            "comment_selectors": ["article[data-testid='tweet']"],
            "comment_body_selectors": ["[data-testid='tweetText']"],
            "comment_permalink_selectors": ["a[href*='/status/'] time"],
            "image_selectors": [
                "div[data-testid='tweetPhoto'] img",
                "a[href*='/photo/'] img",
            ],
            "video_selectors": [
                "div[data-testid='videoPlayer'] video",
                "div[data-testid='videoComponent'] video",
            ],
            "expand_post_text": ["Show more", "显示更多"],
            "expand_comment_text": [
                "Show more replies",
                "Show replies",
                "显示更多回复",
                "显示回复",
            ],
        },
        "ready_signals": [
            "one or more visible article[data-testid=tweet] search cards",
            "a canonical /<username>/status/<id> detail URL plus tweetText, a visible X Article body, or visible media",
        ],
    },
}


class BrowserCollectionError(ValueError):
    """Raised when a browser plan or extracted page violates the contract."""


def _non_empty(value: Any, name: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise BrowserCollectionError(f"{name} must be a non-empty string")
    return value.strip()


def _platform(value: Any) -> str:
    platform = _non_empty(value, "platform").lower()
    if platform not in BROWSER_PLATFORMS:
        raise BrowserCollectionError(
            f"browser collection platform must be one of {BROWSER_PLATFORMS}"
        )
    return platform


def _created_at(value: Optional[datetime] = None) -> str:
    current = value or datetime.now(timezone.utc).astimezone()
    if current.tzinfo is None:
        raise BrowserCollectionError("timestamp must include a timezone")
    return current.isoformat(timespec="seconds")


def browser_recipe(platform: str) -> Dict[str, Any]:
    """Return a copy so a caller cannot mutate the canonical recipe."""

    return deepcopy(BROWSER_RECIPES[_platform(platform)])


def _validate_queries(queries: Sequence[Mapping[str, Any]]) -> List[Dict[str, Any]]:
    normalized: List[Dict[str, Any]] = []
    for index, item in enumerate(queries):
        if not isinstance(item, Mapping):
            raise BrowserCollectionError(f"queries[{index}] must be an object")
        scope_id = _non_empty(item.get("scope_id"), f"queries[{index}].scope_id")
        if not re.fullmatch(r"[a-z0-9][a-z0-9_]{2,63}", scope_id):
            raise BrowserCollectionError(f"queries[{index}].scope_id has an invalid format")
        query = _non_empty(item.get("query"), f"queries[{index}].query")
        domain_hints = item.get("domain_hints", [])
        if not isinstance(domain_hints, list) or not all(
            isinstance(value, str) and value for value in domain_hints
        ):
            raise BrowserCollectionError(f"queries[{index}].domain_hints must be strings")
        query_platforms = item.get("platforms")
        if query_platforms is not None:
            if not isinstance(query_platforms, list) or not query_platforms:
                raise BrowserCollectionError(
                    f"queries[{index}].platforms must be a non-empty list"
                )
            query_platforms = list(dict.fromkeys(
                _platform(value) for value in query_platforms
            ))
        record = {
            "scope_id": scope_id,
            "domain_hints": list(dict.fromkeys(domain_hints)),
            "query": query,
        }
        for field in (
            "query_signature",
            "origin",
            "frontier_topic_id",
            "frontier_term",
            "selection_history",
        ):
            if item.get(field) is not None:
                record[field] = deepcopy(item[field])
        if query_platforms is not None:
            record["platforms"] = query_platforms
        normalized.append(record)
    if not normalized:
        raise BrowserCollectionError("at least one browser query is required")
    return normalized


def build_browser_collection_plan(
    queries: Sequence[Mapping[str, Any]],
    *,
    platforms: Sequence[str] = BROWSER_PLATFORMS,
    max_results_per_query: int = 3,
    max_comments_per_post: int = DEFAULT_BROWSER_COMMENTS,
    max_posts_per_run: int = 15,
    max_reply_expansions: int = DEFAULT_BROWSER_REPLY_EXPANSIONS,
    reply_depth_limit: int = DEFAULT_BROWSER_REPLY_DEPTH,
    post_time_budget_seconds: int = DEFAULT_BROWSER_POST_TIME_BUDGET_SECONDS,
    reply_no_growth_patience: int = DEFAULT_BROWSER_NO_GROWTH_PATIENCE,
    direct_post_urls: Sequence[str] = (),
    known_canonical_urls: Sequence[str] = (),
    created_at: Optional[datetime] = None,
) -> Dict[str, Any]:
    """Build a finite plan for an agent controlling a visible browser."""

    normalized_queries = _validate_queries(queries) if queries else []
    normalized_platforms = list(dict.fromkeys(_platform(value) for value in platforms))
    if not normalized_platforms:
        raise BrowserCollectionError("at least one browser platform is required")
    normalized_direct_posts: List[Tuple[str, str]] = []
    for index, value in enumerate(direct_post_urls):
        try:
            canonical_url, post_id = canonicalize_social_url("x", value)
        except SocialCollectionError as exc:
            raise BrowserCollectionError(
                f"direct_post_urls[{index}] must be an X status URL: {exc}"
            ) from exc
        normalized_direct_posts.append((canonical_url, post_id))
    normalized_direct_posts = list(dict.fromkeys(normalized_direct_posts))
    if normalized_direct_posts and "x" not in normalized_platforms:
        raise BrowserCollectionError("direct X posts require platform x")
    if not normalized_queries and not normalized_direct_posts:
        raise BrowserCollectionError("at least one browser query or direct X post is required")
    if not 1 <= max_results_per_query <= MAX_BROWSER_RESULTS_PER_QUERY:
        raise BrowserCollectionError(
            f"max_results_per_query must be in [1, {MAX_BROWSER_RESULTS_PER_QUERY}]"
        )
    if not 0 <= max_comments_per_post <= MAX_BROWSER_COMMENTS:
        raise BrowserCollectionError(
            f"max_comments_per_post must be in [0, {MAX_BROWSER_COMMENTS}]"
        )
    if not 1 <= max_posts_per_run <= MAX_BROWSER_POSTS_PER_RUN:
        raise BrowserCollectionError(
            f"max_posts_per_run must be in [1, {MAX_BROWSER_POSTS_PER_RUN}]"
        )
    if not 1 <= max_reply_expansions <= MAX_BROWSER_REPLY_EXPANSIONS:
        raise BrowserCollectionError(
            f"max_reply_expansions must be in [1, {MAX_BROWSER_REPLY_EXPANSIONS}]"
        )
    if not 1 <= reply_depth_limit <= MAX_BROWSER_REPLY_DEPTH:
        raise BrowserCollectionError(
            f"reply_depth_limit must be in [1, {MAX_BROWSER_REPLY_DEPTH}]"
        )
    if not 30 <= post_time_budget_seconds <= MAX_BROWSER_POST_TIME_BUDGET_SECONDS:
        raise BrowserCollectionError(
            "post_time_budget_seconds must be in "
            f"[30, {MAX_BROWSER_POST_TIME_BUDGET_SECONDS}]"
        )
    if not 1 <= reply_no_growth_patience <= MAX_BROWSER_NO_GROWTH_PATIENCE:
        raise BrowserCollectionError(
            "reply_no_growth_patience must be in "
            f"[1, {MAX_BROWSER_NO_GROWTH_PATIENCE}]"
        )

    created = _created_at(created_at)
    fingerprint_input = [created, *normalized_platforms]
    fingerprint_input.extend(item["query"] for item in normalized_queries)
    fingerprint_input.extend(item[0] for item in normalized_direct_posts)
    fingerprint = hashlib.sha256("\n".join(fingerprint_input).encode()).hexdigest()[:12]
    tasks: List[Dict[str, Any]] = []
    for platform in normalized_platforms:
        for item in normalized_queries:
            query_platforms = item.get("platforms")
            if query_platforms is not None and platform not in query_platforms:
                continue
            task_query = {
                key: value for key, value in item.items() if key != "platforms"
            }
            tasks.append({
                "task_id": f"browser-{platform}-{len(tasks) + 1:04d}",
                "task_type": "search_and_enrich",
                "platform": platform,
                **task_query,
                "search_url": build_search_url(platform, item["query"]),
                "max_results": max_results_per_query,
                "max_comments_per_post": max_comments_per_post,
                "max_reply_expansions": max_reply_expansions,
                "reply_depth_limit": reply_depth_limit,
                "post_time_budget_seconds": post_time_budget_seconds,
                "reply_no_growth_patience": reply_no_growth_patience,
                "reply_expansion_strategy": "until_exhausted_or_guardrail",
            })
    for canonical_url, post_id in normalized_direct_posts:
        tasks.append({
            "task_id": f"browser-x-{len(tasks) + 1:04d}",
            "task_type": "detail_and_visible_replies",
            "platform": "x",
            "scope_id": "open_ended_wbc_field_notes",
            "domain_hints": [],
            "query": f"direct X post {post_id}",
            "canonical_url": canonical_url,
            "max_results": 1,
            "max_comments_per_post": max_comments_per_post,
            "max_reply_expansions": max_reply_expansions,
            "reply_depth_limit": reply_depth_limit,
            "post_time_budget_seconds": post_time_budget_seconds,
            "reply_no_growth_patience": reply_no_growth_patience,
            "reply_expansion_strategy": "until_exhausted_or_guardrail",
        })

    search_tasks = sum(task["task_type"] == "search_and_enrich" for task in tasks)
    estimated = min(
        search_tasks * max_results_per_query + len(normalized_direct_posts),
        max_posts_per_run,
    )
    return {
        "schema_version": 1,
        "run_id": f"browser-plan-{re.sub(r'[^0-9]', '', created)[:14]}-{fingerprint}",
        "created_at": created,
        "trigger": "manual_on_demand",
        "collection_mode": "visible_browser_assisted",
        "platforms": normalized_platforms,
        "tasks": tasks,
        "recipes": {platform: browser_recipe(platform) for platform in normalized_platforms},
        "known_canonical_urls": list(dict.fromkeys(known_canonical_urls)),
        "direct_post_urls": [item[0] for item in normalized_direct_posts],
        "limits": {
            "max_results_per_query": max_results_per_query,
            "max_comments_per_post": max_comments_per_post,
            "max_posts_per_run": max_posts_per_run,
            "estimated_max_detail_pages": estimated,
            "max_reply_expansions": max_reply_expansions,
            "reply_depth_limit": reply_depth_limit,
            "post_time_budget_seconds": post_time_budget_seconds,
            "reply_no_growth_patience": reply_no_growth_patience,
        },
        "completeness_contract": {
            "status": "partial_visible",
            "reply_expansion_strategy": "until_exhausted_or_guardrail",
            "captures": [
                "post text currently rendered in the signed-in visible browser",
                "bounded replies reached by visible controls",
                "visible image/video frames queued for screenshot analysis",
            ],
            "does_not_claim": [
                "all platform posts",
                "all replies or complete reply depth",
                "deleted, protected, withheld, collapsed, or inaccessible content",
            ],
        },
        "automated_actions": [
            "login_state_check",
            "platform_search",
            "result_link_extraction",
            "detail_navigation",
            "body_comment_metadata_extraction",
            "image_screenshot_queue",
            "canonicalization",
            "deduplication",
            "analysis_queue_generation",
        ],
        "manual_actions": [
            "initial_or_expired_login",
            "captcha_confirmation_and_completion",
            "paywall_or_access_decision",
        ],
        "execution_rules": {
            "visible_authenticated_browser": True,
            "read_only_navigation": True,
            "cookies_or_profile_read": False,
            "credential_storage": False,
            "captcha_bypass": False,
            "paywall_bypass": False,
            "background_schedule": False,
            "auto_publish": False,
            "hidden_api_calls": False,
            "completeness_claim": "partial_visible",
            "reply_expansion_strategy": "until_exhausted_or_guardrail",
            "stop_on": [
                "login_required",
                "captcha",
                "risk_control",
                "access_denied",
            ],
        },
    }


def _state_markers(platform: str) -> Dict[str, Tuple[str, ...]]:
    common = {
        "captcha": ("安全验证", "人机验证", "拖动滑块", "完成验证", "captcha"),
        "risk_control": ("访问异常", "操作频繁", "请求过于频繁", "风险提示"),
        "access_denied": ("内容不存在", "页面不存在", "内容已删除", "暂无权限查看"),
        "unavailable": ("当前笔记暂时无法浏览", "页面走丢了", "回答已删除", "文章已删除"),
    }
    if platform == "xiaohongshu":
        common["login_required"] = (
            "登录后查看搜索结果",
            "登录后推荐更懂你的笔记",
            "请先登录",
            "扫码登录",
        )
    elif platform == "zhihu":
        common["login_required"] = (
            "验证码登录",
            "密码登录",
            "登录/注册",
            "请登录知乎",
        )
        common["access_denied"] += ("购买后阅读", "仅限盐选会员阅读全文")
    else:
        common["login_required"] = (
            "sign in to x",
            "join x today",
            "电子邮箱或用户名",
            "使用 google 继续",
            "登录 x",
        )
        common["captcha"] += ("authenticate your account", "arkose challenge")
        common["risk_control"] += (
            "rate limit exceeded",
            "something went wrong. try reloading",
            "出现错误。请尝试重新加载",
        )
        common["access_denied"] += (
            "these posts are protected",
            "this account's posts are protected",
            "you're unable to view this post",
            "你无法查看此帖子",
        )
        common["unavailable"] += (
            "this post is unavailable",
            "hmm...this page doesn’t exist",
            "这个帖子不可用",
            "此帖子已被删除",
        )
    return common


def classify_browser_page(payload: Mapping[str, Any]) -> Dict[str, Any]:
    """Classify a visible page using content signals, not a single avatar selector."""

    if not isinstance(payload, Mapping):
        raise BrowserCollectionError("browser page must be an object")
    platform = _platform(payload.get("platform"))
    url = str(payload.get("url", payload.get("canonical_url", ""))).strip()
    title = str(payload.get("title", "")).strip()
    visible_text = str(payload.get("visible_text", "")).strip()
    combined = "\n".join((url, title, visible_text)).lower()
    evidence: List[str] = []

    markers = _state_markers(platform)
    for state in (
        "captcha",
        "risk_control",
        "access_denied",
        "login_required",
        "unavailable",
    ):
        matched = [marker for marker in markers[state] if marker.lower() in combined]
        if matched:
            return {"state": state, "evidence": matched[:3]}

    parsed = urlparse(url) if url else None
    if parsed and any(part in parsed.path.lower() for part in ("/signin", "/login")):
        return {"state": "login_required", "evidence": ["login URL"]}

    explicit = payload.get("page_state")
    if explicit is not None:
        explicit = _non_empty(explicit, "page_state")
        if explicit not in BROWSER_PAGE_STATES:
            raise BrowserCollectionError(
                f"page_state must be one of {BROWSER_PAGE_STATES}"
            )
        if explicit != "ready":
            return {"state": explicit, "evidence": ["explicit page state"]}

    signals = payload.get("signals", {})
    if not isinstance(signals, Mapping):
        raise BrowserCollectionError("signals must be an object")
    post_links = signals.get("post_links", 0)
    body_chars = signals.get("detail_body_chars", 0)
    if isinstance(post_links, int) and post_links > 0:
        evidence.append(f"post_links={post_links}")
    if isinstance(body_chars, int) and body_chars > 0:
        evidence.append(f"detail_body_chars={body_chars}")
    if signals.get("real_feed_cards") is True:
        evidence.append("real_feed_cards")
    if payload.get("body_text") or payload.get("content_text"):
        evidence.append("extracted_body_text")
    if explicit == "ready":
        evidence.append("explicit ready state")
    if evidence:
        return {"state": "ready", "evidence": evidence}
    return {"state": "unavailable", "evidence": ["no reliable ready signal"]}


def _optional_text(value: Any, name: str, maximum: int) -> Optional[str]:
    if value is None:
        return None
    text = _non_empty(value, name)
    if len(text) > maximum:
        return text[:maximum]
    return text


def _normalize_comments(
    platform: str, comments: Any, canonical_url: str
) -> List[Dict[str, Any]]:
    if comments is None:
        return []
    if not isinstance(comments, list):
        raise BrowserCollectionError("selected_comments must be a list")
    normalized: List[Dict[str, Any]] = []
    seen = set()
    for index, comment in enumerate(comments[:MAX_BROWSER_COMMENTS]):
        if not isinstance(comment, Mapping):
            raise BrowserCollectionError(f"selected_comments[{index}] must be an object")
        text = _non_empty(comment.get("text"), f"selected_comments[{index}].text")
        author = _optional_text(
            comment.get("author_display"),
            f"selected_comments[{index}].author_display",
            100,
        )
        key = ((author or "").lower(), text[:80])
        if key in seen:
            continue
        seen.add(key)
        source_url = canonical_url
        if comment.get("source_url"):
            try:
                source_url, _ = canonicalize_social_url(platform, comment["source_url"])
            except SocialCollectionError:
                source_url = canonical_url
        normalized_comment = {
            "author_display": author,
            "text": text[:MAX_BROWSER_COMMENT_CHARS],
            "text_truncated": len(text) > MAX_BROWSER_COMMENT_CHARS,
            "published_display": _optional_text(
                comment.get("published_display"),
                f"selected_comments[{index}].published_display",
                100,
            ),
            "likes": comment.get("likes"),
            "source_url": source_url,
        }
        for field in ("post_id", "parent_post_id", "conversation_id"):
            if comment.get(field) is not None:
                normalized_comment[field] = _optional_text(
                    str(comment[field]), f"selected_comments[{index}].{field}", 100
                )
        depth = comment.get("depth")
        if depth is not None:
            if not isinstance(depth, int) or not 0 <= depth <= MAX_BROWSER_REPLY_DEPTH:
                raise BrowserCollectionError(
                    "selected_comments"
                    f"[{index}].depth must be in [0, {MAX_BROWSER_REPLY_DEPTH}]"
                )
            normalized_comment["depth"] = depth
        if comment.get("is_author_reply") is not None:
            normalized_comment["is_author_reply"] = bool(comment["is_author_reply"])
        normalized.append(normalized_comment)
    return normalized


def _normalize_media(media: Any) -> List[Dict[str, Any]]:
    if media is None:
        return []
    if not isinstance(media, list):
        raise BrowserCollectionError("media must be a list")
    normalized = []
    for index, item in enumerate(media[:20]):
        if not isinstance(item, Mapping):
            raise BrowserCollectionError(f"media[{index}] must be an object")
        summary = _optional_text(item.get("summary"), f"media[{index}].summary", 1000)
        normalized_item = {
            "index": item.get("index", index + 1),
            "kind": str(item.get("kind", "image"))[:30],
            "alt_text": _optional_text(item.get("alt_text"), f"media[{index}].alt_text", 500),
            "summary": summary,
            "requires_visual_analysis": bool(
                item.get("requires_visual_analysis", summary is None)
            ),
        }
        screenshot_path = item.get("screenshot_path")
        if screenshot_path is not None:
            screenshot_path = _non_empty(
                screenshot_path, f"media[{index}].screenshot_path"
            ).replace("\\", "/")
            if (
                screenshot_path.startswith("/")
                or ".." in screenshot_path.split("/")
                or not screenshot_path.startswith("var/social-browser/media/")
            ):
                raise BrowserCollectionError(
                    "media screenshot_path must stay under var/social-browser/media/"
                )
            normalized_item["screenshot_path"] = screenshot_path
        normalized.append(normalized_item)
    return normalized


def normalize_browser_page_capture(
    payload: Mapping[str, Any], *, captured_at: Optional[datetime] = None
) -> Dict[str, Any]:
    """Normalize one ready detail page while dropping transient navigation data."""

    state = classify_browser_page(payload)
    if state["state"] != "ready":
        raise BrowserCollectionError(
            f"browser page is not ready: {state['state']} ({', '.join(state['evidence'])})"
        )
    platform = _platform(payload.get("platform"))
    raw_url = _non_empty(
        payload.get("canonical_url", payload.get("url")), "browser page URL"
    )
    try:
        canonical_url, post_id = canonicalize_social_url(platform, raw_url)
    except SocialCollectionError as exc:
        raise BrowserCollectionError(str(exc)) from exc
    scope_id = _non_empty(
        payload.get("scope_id", "open_ended_wbc_field_notes"), "scope_id"
    )
    if not re.fullmatch(r"[a-z0-9][a-z0-9_]{2,63}", scope_id):
        raise BrowserCollectionError("scope_id has an invalid format")
    domain_hints = payload.get("domain_hints", [])
    if not isinstance(domain_hints, list) or not all(
        isinstance(value, str) and value for value in domain_hints
    ):
        raise BrowserCollectionError("domain_hints must be strings")

    body = str(payload.get("body_text", payload.get("content_text", ""))).strip()
    title_value = payload.get("title")
    if platform == "x" and (not isinstance(title_value, str) or not title_value.strip()):
        author_hint = payload.get("author_display") or post_id
        title_value = f"{author_hint} 的 X 帖子"
    title = _non_empty(title_value, "title")
    media = _normalize_media(payload.get("media"))
    if not body and not media:
        raise BrowserCollectionError("a ready detail page needs body text or visual media")
    comments = _normalize_comments(
        platform,
        payload.get("selected_comments", payload.get("comments")),
        canonical_url,
    )
    captured = _created_at(captured_at)
    selector_matches = payload.get("selector_matches", [])
    if not isinstance(selector_matches, list) or not all(
        isinstance(value, str) for value in selector_matches
    ):
        raise BrowserCollectionError("selector_matches must be a list of strings")
    attention = payload.get("attention", {})
    if not isinstance(attention, Mapping):
        raise BrowserCollectionError("attention must be an object")

    body_stored = body[:MAX_BROWSER_BODY_CHARS]
    expansion_attempts = payload.get("reply_expansion_attempts", 0)
    if (
        not isinstance(expansion_attempts, int)
        or not 0 <= expansion_attempts <= MAX_BROWSER_REPLY_EXPANSIONS
    ):
        raise BrowserCollectionError(
            "reply_expansion_attempts must be in "
            f"[0, {MAX_BROWSER_REPLY_EXPANSIONS}]"
        )
    reply_depth_reached = payload.get("reply_depth_reached", 0)
    if (
        not isinstance(reply_depth_reached, int)
        or not 0 <= reply_depth_reached <= MAX_BROWSER_REPLY_DEPTH
    ):
        raise BrowserCollectionError(
            f"reply_depth_reached must be in [0, {MAX_BROWSER_REPLY_DEPTH}]"
        )
    reply_depth_limit = payload.get("reply_depth_limit", DEFAULT_BROWSER_REPLY_DEPTH)
    if (
        not isinstance(reply_depth_limit, int)
        or not 1 <= reply_depth_limit <= MAX_BROWSER_REPLY_DEPTH
    ):
        raise BrowserCollectionError(
            f"reply_depth_limit must be in [1, {MAX_BROWSER_REPLY_DEPTH}]"
        )
    reply_limit_requested = payload.get(
        "max_comments_per_post", DEFAULT_BROWSER_COMMENTS
    )
    if (
        not isinstance(reply_limit_requested, int)
        or not 0 <= reply_limit_requested <= MAX_BROWSER_COMMENTS
    ):
        raise BrowserCollectionError(
            f"max_comments_per_post must be in [0, {MAX_BROWSER_COMMENTS}]"
        )
    match = {
        "scope_id": scope_id,
        "domain_hints": list(dict.fromkeys(domain_hints)),
        "query": _non_empty(payload.get("query"), "query"),
        "task_id": payload.get("task_id"),
    }
    for field in ("query_signature", "origin", "frontier_topic_id", "frontier_term"):
        if payload.get(field) is not None:
            match[field] = payload[field]
    return {
        "schema_version": 1,
        "platform": platform,
        "post_id": post_id,
        "canonical_url": canonical_url,
        "scope_id": scope_id,
        "domain_hints": match["domain_hints"],
        "query": match["query"],
        "matches": [match],
        "title": title[:500],
        "author_display": _optional_text(payload.get("author_display"), "author_display", 200),
        "published_display": _optional_text(
            payload.get("published_display"), "published_display", 200
        ),
        "body_text": body_stored,
        "body_characters": len(body),
        "body_truncated": len(body) > MAX_BROWSER_BODY_CHARS,
        "body_sha256": hashlib.sha256(body.encode()).hexdigest(),
        "full_text_available": bool(
            payload.get("full_text_available", bool(body) if platform != "x" else False)
        ),
        "selected_comments": comments,
        "attention": dict(attention),
        "media": media,
        "media_summaries": [item["summary"] for item in media if item["summary"]],
        "visual_analysis_pending": any(
            item["requires_visual_analysis"] for item in media
        ),
        "collection_completeness": {
            "status": "partial_visible",
            "post_text_scope": "visible_dom",
            "reply_scope": "bounded_visible_subset",
            "media_scope": "visible_media_screenshot_queue",
            "visible_replies_captured": len(comments),
            "reply_limit_requested": reply_limit_requested,
            "reply_expansion_attempts": expansion_attempts,
            "reply_depth_reached": reply_depth_reached,
            "reply_depth_limit": reply_depth_limit,
            "reply_expansion_strategy": "until_exhausted_or_guardrail",
            "hidden_or_inaccessible_content_included": False,
            "stop_reason": str(payload.get("stop_reason", "bounded_run"))[:100],
        },
        "content_collected": True,
        "review_status": "pending_analysis",
        "access_mode": "authorized_visible_browser",
        "captured_at": captured,
        "extraction_provenance": {
            "method": "visible_browser_dom",
            "user_session": True,
            "selector_matches": selector_matches,
            "cookies_or_profile_read": False,
            "credentials_persisted": False,
            "captcha_bypassed": False,
            "hidden_api_calls": False,
            "auto_published": False,
        },
    }


def _merge_candidates(existing: Dict[str, Any], incoming: Dict[str, Any]) -> None:
    known_matches = {
        (item.get("scope_id"), item.get("query")) for item in existing["matches"]
    }
    for match in incoming["matches"]:
        if (match.get("scope_id"), match.get("query")) not in known_matches:
            existing["matches"].append(match)
    if incoming["body_characters"] > existing["body_characters"]:
        for key in (
            "body_text", "body_characters", "body_truncated", "body_sha256",
            "full_text_available", "title", "author_display", "published_display",
        ):
            existing[key] = incoming[key]
    comment_keys = {
        ((item.get("author_display") or "").lower(), item.get("text"))
        for item in existing["selected_comments"]
    }
    for comment in incoming["selected_comments"]:
        key = ((comment.get("author_display") or "").lower(), comment.get("text"))
        if key not in comment_keys and len(existing["selected_comments"]) < MAX_BROWSER_COMMENTS:
            existing["selected_comments"].append(comment)
            comment_keys.add(key)
    existing["collection_completeness"]["visible_replies_captured"] = len(
        existing["selected_comments"]
    )
    existing["collection_completeness"]["reply_expansion_attempts"] = max(
        existing["collection_completeness"]["reply_expansion_attempts"],
        incoming["collection_completeness"]["reply_expansion_attempts"],
    )
    existing["collection_completeness"]["reply_depth_reached"] = max(
        existing["collection_completeness"]["reply_depth_reached"],
        incoming["collection_completeness"]["reply_depth_reached"],
    )
    existing["collection_completeness"]["reply_depth_limit"] = max(
        existing["collection_completeness"]["reply_depth_limit"],
        incoming["collection_completeness"]["reply_depth_limit"],
    )
    existing["collection_completeness"]["reply_limit_requested"] = max(
        existing["collection_completeness"]["reply_limit_requested"],
        incoming["collection_completeness"]["reply_limit_requested"],
    )
    if len(incoming["media"]) > len(existing["media"]):
        existing["media"] = incoming["media"]
        existing["media_summaries"] = incoming["media_summaries"]
        existing["visual_analysis_pending"] = incoming["visual_analysis_pending"]


def normalize_browser_collection_run(
    raw: Mapping[str, Any], *, captured_at: Optional[datetime] = None
) -> Dict[str, Any]:
    """Normalize ready pages and retain blockers without persisting page DOM."""

    if not isinstance(raw, Mapping):
        raise BrowserCollectionError("browser run must be an object")
    pages = raw.get("pages", raw.get("captures"))
    if not isinstance(pages, list):
        raise BrowserCollectionError("browser run must contain pages[]")
    by_url: Dict[str, Dict[str, Any]] = {}
    blockers: List[Dict[str, Any]] = []
    blocker_keys = set()
    completed_searches: List[Dict[str, Any]] = []
    completed_search_keys = set()
    ready_pages = 0
    blocked_pages = 0
    empty_result_pages = 0
    for index, page in enumerate(pages):
        if not isinstance(page, Mapping):
            raise BrowserCollectionError(f"pages[{index}] must be an object")
        state = classify_browser_page(page)
        if state["state"] == "empty_results":
            empty_result_pages += 1
            receipt = {
                "task_id": page.get("task_id"),
                "platform": page.get("platform"),
                "state": "empty_results",
                "evidence": state["evidence"],
            }
            receipt_key = (
                receipt["task_id"],
                receipt["platform"],
                receipt["state"],
            )
            if receipt_key not in completed_search_keys:
                completed_search_keys.add(receipt_key)
                completed_searches.append(receipt)
            continue
        if state["state"] != "ready":
            blocked_pages += 1
            blocker = {
                "task_id": page.get("task_id"),
                "platform": page.get("platform"),
                "state": state["state"],
                "evidence": state["evidence"],
            }
            blocker_key = (
                blocker["task_id"],
                blocker["platform"],
                blocker["state"],
                tuple(blocker["evidence"]),
            )
            if blocker_key not in blocker_keys:
                blocker_keys.add(blocker_key)
                blockers.append(blocker)
            continue
        ready_pages += 1
        candidate = normalize_browser_page_capture(page, captured_at=captured_at)
        existing = by_url.get(candidate["canonical_url"])
        if existing is None:
            by_url[candidate["canonical_url"]] = candidate
        else:
            _merge_candidates(existing, candidate)

    created = _created_at(captured_at)
    run_id = raw.get("run_id")
    if not isinstance(run_id, str) or not run_id.strip():
        digest = hashlib.sha256(
            (created + "\n" + "\n".join(sorted(by_url))).encode()
        ).hexdigest()[:12]
        run_id = f"browser-run-{re.sub(r'[^0-9]', '', created)[:14]}-{digest}"
    return {
        "schema_version": 1,
        "run_id": run_id,
        "plan_run_id": raw.get("plan_run_id"),
        "created_at": created,
        "trigger": "manual_on_demand",
        "collection_mode": "visible_browser_assisted",
        "access_mode": "authorized_visible_browser",
        "pages_received": len(pages),
        "candidates": list(by_url.values()),
        "completed_searches": completed_searches,
        "blockers": blockers,
        "stats": {
            "ready_pages": ready_pages,
            "unique_candidates": len(by_url),
            "duplicates_merged": ready_pages - len(by_url),
            "blocked_pages": blocked_pages,
            "unique_blockers": len(blockers),
            "empty_result_pages": empty_result_pages,
            "unique_completed_searches": len(completed_searches),
        },
        "auto_published": False,
    }
