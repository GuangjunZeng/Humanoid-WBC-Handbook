"""Free, incremental GitHub Issues discovery for WBC engineering evidence.

The collector uses GitHub's documented REST endpoints.  A token is optional;
``GITHUB_TOKEN`` only raises the free rate limit and is never persisted.  Search
tasks are split by repository batches and date windows so large historical
backfills are resumable instead of silently stopping at GitHub's 1,000-result
search cap.
"""

from __future__ import annotations

from datetime import datetime, timedelta, timezone
import hashlib
import json
import os
import re
import time
from typing import Any, Dict, List, Mapping, Optional, Sequence, Tuple
from urllib import error, parse, request


GITHUB_API_BASE = "https://api.github.com"
GITHUB_TOKEN_ENV = "GITHUB_TOKEN"
GITHUB_STATE_SCHEMA_VERSION = 1
GITHUB_PLAN_SCHEMA_VERSION = 1
GITHUB_MAX_PER_PAGE = 100
GITHUB_MAX_SEARCH_PAGES = 10
GITHUB_MAX_COMMENTS_PER_ISSUE = 500
GITHUB_MAX_ISSUES_PER_RUN = 5000


class GithubIssueCollectionError(ValueError):
    """Raised when a GitHub plan, response, or state is invalid."""


def _now(value: Optional[datetime] = None) -> datetime:
    current = value or datetime.now(timezone.utc).astimezone()
    if current.tzinfo is None:
        raise GithubIssueCollectionError("timestamp must include a timezone")
    return current


def _iso(value: Optional[datetime] = None) -> str:
    return _now(value).isoformat(timespec="seconds")


def _parse_iso(value: Any, name: str) -> datetime:
    if not isinstance(value, str) or not value.strip():
        raise GithubIssueCollectionError(f"{name} must be an ISO 8601 string")
    normalized = value[:-1] + "+00:00" if value.endswith("Z") else value
    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError as exc:
        raise GithubIssueCollectionError(f"{name} must be ISO 8601") from exc
    if parsed.tzinfo is None:
        raise GithubIssueCollectionError(f"{name} must include a timezone")
    return parsed


def canonicalize_github_issue_url(url: Any) -> Tuple[str, str, int, str]:
    if not isinstance(url, str) or not url.strip():
        raise GithubIssueCollectionError("GitHub issue URL must be a non-empty string")
    parsed = parse.urlparse(url.strip())
    if parsed.scheme not in {"http", "https"} or parsed.hostname != "github.com":
        raise GithubIssueCollectionError("GitHub issue URL must use github.com")
    match = re.fullmatch(r"/([^/]+)/([^/]+)/issues/(\d+)/?", parsed.path)
    if not match:
        raise GithubIssueCollectionError("GitHub URL must identify /owner/repo/issues/<n>")
    owner, repo, number_text = match.groups()
    canonical = f"https://github.com/{owner}/{repo}/issues/{int(number_text)}"
    stable_id = f"{owner.lower()}.{repo.lower()}.{int(number_text)}"
    return canonical, f"{owner}/{repo}", int(number_text), stable_id


def precise_github_issue_locator_url(url: Any) -> str:
    canonical, _, _, _ = canonicalize_github_issue_url(url)
    fragment = parse.urlparse(str(url)).fragment
    if re.fullmatch(r"issuecomment-\d+", fragment or ""):
        return f"{canonical}#{fragment}"
    return canonical


def _task_signature(scope_id: str, query: str, repositories: Sequence[str], window: str) -> str:
    payload = "\t".join((scope_id, query.casefold(), ",".join(repositories), window))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()[:24]


def empty_github_issue_state(created_at: Optional[datetime] = None) -> Dict[str, Any]:
    created = _iso(created_at)
    return {
        "schema_version": GITHUB_STATE_SCHEMA_VERSION,
        "created_at": created,
        "updated_at": created,
        "tasks": {},
        "known_urls": {},
        "runs": [],
    }


def _state(value: Optional[Mapping[str, Any]], current: datetime) -> Dict[str, Any]:
    if not value:
        return empty_github_issue_state(current)
    if value.get("schema_version") != GITHUB_STATE_SCHEMA_VERSION:
        raise GithubIssueCollectionError("GitHub issue state schema_version is unsupported")
    tasks = value.get("tasks", {})
    known_urls = value.get("known_urls", {})
    runs = value.get("runs", [])
    if not isinstance(tasks, Mapping) or not isinstance(known_urls, Mapping):
        raise GithubIssueCollectionError("GitHub issue state tasks/known_urls must be objects")
    if not isinstance(runs, list):
        raise GithubIssueCollectionError("GitHub issue state runs must be a list")
    normalized = dict(value)
    normalized["tasks"] = {str(key): dict(item) for key, item in tasks.items()}
    normalized["known_urls"] = {
        str(key): dict(item) for key, item in known_urls.items()
    }
    normalized["runs"] = [dict(item) for item in runs if isinstance(item, Mapping)]
    return normalized


def _validated_config(config: Mapping[str, Any]) -> Dict[str, Any]:
    if not isinstance(config, Mapping) or config.get("schema_version") != 1:
        raise GithubIssueCollectionError("GitHub issue config schema_version must be 1")
    repositories_value = config.get("repositories")
    queries_value = config.get("queries")
    windows_value = config.get("history_windows")
    if not isinstance(repositories_value, list) or not repositories_value:
        raise GithubIssueCollectionError("GitHub config repositories must be non-empty")
    if not isinstance(queries_value, list) or not queries_value:
        raise GithubIssueCollectionError("GitHub config queries must be non-empty")
    if not isinstance(windows_value, list) or not windows_value:
        raise GithubIssueCollectionError("GitHub config history_windows must be non-empty")

    repositories = []
    for index, item in enumerate(repositories_value):
        if not isinstance(item, Mapping):
            raise GithubIssueCollectionError(f"repositories[{index}] must be an object")
        full_name = item.get("full_name")
        if not isinstance(full_name, str) or not re.fullmatch(
            r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", full_name
        ):
            raise GithubIssueCollectionError(f"repositories[{index}].full_name is invalid")
        tags = item.get("tags", [])
        if not isinstance(tags, list) or not all(isinstance(tag, str) for tag in tags):
            raise GithubIssueCollectionError(f"repositories[{index}].tags must be strings")
        repositories.append({"full_name": full_name, "tags": list(dict.fromkeys(tags))})

    queries = []
    for index, item in enumerate(queries_value):
        if not isinstance(item, Mapping):
            raise GithubIssueCollectionError(f"queries[{index}] must be an object")
        scope_id = item.get("scope_id")
        query = item.get("query")
        if not isinstance(scope_id, str) or not re.fullmatch(
            r"[a-z0-9][a-z0-9_]{2,63}", scope_id
        ):
            raise GithubIssueCollectionError(f"queries[{index}].scope_id is invalid")
        if not isinstance(query, str) or not query.strip():
            raise GithubIssueCollectionError(f"queries[{index}].query is invalid")
        repository_tags = item.get("repository_tags", [])
        if not isinstance(repository_tags, list) or not all(
            isinstance(tag, str) for tag in repository_tags
        ):
            raise GithubIssueCollectionError(
                f"queries[{index}].repository_tags must be strings"
            )
        queries.append({
            "scope_id": scope_id,
            "query": query.strip(),
            "repository_tags": list(dict.fromkeys(repository_tags)),
        })

    windows = []
    for index, item in enumerate(windows_value):
        if not isinstance(item, Mapping):
            raise GithubIssueCollectionError(f"history_windows[{index}] must be an object")
        window_id = item.get("window_id")
        created = item.get("created")
        if not isinstance(window_id, str) or not re.fullmatch(r"[a-z0-9_-]{2,40}", window_id):
            raise GithubIssueCollectionError(f"history_windows[{index}].window_id is invalid")
        if created is not None and (not isinstance(created, str) or ".." not in created):
            raise GithubIssueCollectionError(f"history_windows[{index}].created is invalid")
        windows.append({
            "window_id": window_id,
            "created": created,
            "rolling": bool(item.get("rolling", False)),
        })
    return {"repositories": repositories, "queries": queries, "history_windows": windows}


def _repo_batches(repositories: Sequence[str], batch_size: int) -> List[List[str]]:
    return [list(repositories[index:index + batch_size]) for index in range(0, len(repositories), batch_size)]


def build_github_issue_plan(
    config: Mapping[str, Any],
    *,
    previous_state: Optional[Mapping[str, Any]] = None,
    frontier_queries: Sequence[Mapping[str, Any]] = (),
    frontier_only: bool = False,
    max_tasks_per_run: int = 40,
    repositories_per_task: int = 5,
    max_pages_per_task: int = GITHUB_MAX_SEARCH_PAGES,
    per_page: int = GITHUB_MAX_PER_PAGE,
    created_at: Optional[datetime] = None,
) -> Dict[str, Any]:
    """Build a resumable historical/rolling Issue search plan."""

    if not 1 <= max_tasks_per_run <= 500:
        raise GithubIssueCollectionError("max_tasks_per_run must be in [1, 500]")
    if not 1 <= repositories_per_task <= 10:
        raise GithubIssueCollectionError("repositories_per_task must be in [1, 10]")
    if not 1 <= max_pages_per_task <= GITHUB_MAX_SEARCH_PAGES:
        raise GithubIssueCollectionError("max_pages_per_task must be in [1, 10]")
    if not 1 <= per_page <= GITHUB_MAX_PER_PAGE:
        raise GithubIssueCollectionError("per_page must be in [1, 100]")
    current = _now(created_at)
    normalized = _validated_config(config)
    state = _state(previous_state, current)
    queries = [] if frontier_only else list(normalized["queries"])
    for item in frontier_queries:
        if not isinstance(item, Mapping) or item.get("platforms") != ["github_issue"]:
            continue
        queries.append({
            "scope_id": item.get("scope_id", "open_ended_wbc_field_notes"),
            "query": item.get("query"),
            "repository_tags": [],
            "origin": "frontier",
            "frontier_topic_id": item.get("frontier_topic_id"),
        })

    all_tasks: List[Dict[str, Any]] = []
    for query_item in queries:
        required_tags = set(query_item.get("repository_tags", []))
        selected_repos = [
            item["full_name"] for item in normalized["repositories"]
            if not required_tags or required_tags.intersection(item["tags"])
        ]
        for batch in _repo_batches(selected_repos, repositories_per_task):
            for window in normalized["history_windows"]:
                signature = _task_signature(
                    query_item["scope_id"], query_item["query"], batch, window["window_id"]
                )
                history = state["tasks"].get(signature, {})
                if history.get("complete") and not window["rolling"]:
                    continue
                next_eligible = history.get("next_eligible_at")
                if next_eligible and _parse_iso(next_eligible, "next_eligible_at") > current:
                    continue
                task = {
                    "task_signature": signature,
                    "scope_id": query_item["scope_id"],
                    "query": query_item["query"],
                    "repositories": batch,
                    "window_id": window["window_id"],
                    "created": window["created"],
                    "rolling": window["rolling"],
                    "resume_page": int(history.get("next_page", 1) or 1),
                    "run_count": int(history.get("run_count", 0) or 0),
                    "origin": query_item.get("origin", "configured"),
                }
                if query_item.get("frontier_topic_id"):
                    task["frontier_topic_id"] = query_item["frontier_topic_id"]
                all_tasks.append(task)

    all_tasks.sort(key=lambda item: (
        0 if item["run_count"] == 0 else 1,
        0 if item["origin"] == "frontier" else 1,
        item["run_count"],
        item["scope_id"],
        item["window_id"],
        item["task_signature"],
    ))
    selected = all_tasks[:max_tasks_per_run]
    for index, task in enumerate(selected, 1):
        task["task_id"] = f"github-issue-{index:04d}"
        qualifiers = ["is:issue", task["query"]]
        qualifiers.extend(f"repo:{repo}" for repo in task["repositories"])
        if task["created"]:
            qualifiers.append(f"created:{task['created']}")
        task["search_query"] = " ".join(qualifiers)
        task["search_url"] = (
            "https://github.com/search?type=issues&q="
            + parse.quote_plus(task["search_query"])
        )
    fingerprint = hashlib.sha256(
        ("\n".join(task["task_signature"] for task in selected) + _iso(current)).encode()
    ).hexdigest()[:12]
    return {
        "schema_version": GITHUB_PLAN_SCHEMA_VERSION,
        "run_id": f"github-issues-{current.strftime('%Y%m%d%H%M%S')}-{fingerprint}",
        "created_at": _iso(current),
        "trigger": "manual_on_demand",
        "access_mode": "public_api",
        "tasks": selected,
        "limits": {
            "max_tasks_per_run": max_tasks_per_run,
            "repositories_per_task": repositories_per_task,
            "max_pages_per_task": max_pages_per_task,
            "per_page": per_page,
            "search_api_result_cap_per_task": 1000,
        },
        "coverage": {
            "repositories": len(normalized["repositories"]),
            "queries": len(queries),
            "history_windows": len(normalized["history_windows"]),
            "eligible_tasks": len(all_tasks),
            "selected_tasks": len(selected),
        },
        "credential": {
            "optional_environment_variable": GITHUB_TOKEN_ENV,
            "required_for_paid_access": False,
            "persisted": False,
        },
        "deduplication": {
            "primary_key": "canonical_issue_url",
            "refresh_key": "issue_updated_at + content_sha256",
        },
    }


class GithubIssueApiClient:
    """Small documented REST client with optional free authentication."""

    def __init__(
        self,
        token: Optional[str] = None,
        *,
        base_url: str = GITHUB_API_BASE,
        timeout: float = 30.0,
        opener: Any = None,
        retries: int = 2,
    ) -> None:
        self.token = token.strip() if isinstance(token, str) and token.strip() else None
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self._opener = opener or request.urlopen
        self.retries = retries

    @classmethod
    def from_environment(cls, env_name: str = GITHUB_TOKEN_ENV, **kwargs: Any) -> "GithubIssueApiClient":
        return cls(os.environ.get(env_name), **kwargs)

    def _get(self, url: str) -> Tuple[Dict[str, Any] | List[Any], Dict[str, str]]:
        headers = {
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "Humanoid-WBC-Handbook/1.0",
        }
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        last_error: Optional[BaseException] = None
        for attempt in range(self.retries + 1):
            api_request = request.Request(url, headers=headers, method="GET")
            try:
                with self._opener(api_request, timeout=self.timeout) as response:
                    body = response.read()
                    response_headers = {key.lower(): value for key, value in response.headers.items()}
                payload = json.loads(body.decode("utf-8"))
                if not isinstance(payload, (dict, list)):
                    raise GithubIssueCollectionError("GitHub API returned invalid JSON shape")
                return payload, response_headers
            except error.HTTPError as exc:
                body = exc.read(8192).decode("utf-8", errors="replace")
                last_error = GithubIssueCollectionError(
                    f"GitHub API returned HTTP {exc.code}: {body[:500]}"
                )
                if exc.code not in {429, 500, 502, 503, 504} or attempt >= self.retries:
                    raise last_error from exc
            except (error.URLError, TimeoutError) as exc:
                last_error = exc
                if attempt >= self.retries:
                    raise GithubIssueCollectionError(f"GitHub API request failed: {exc}") from exc
            time.sleep(min(2 ** attempt, 4))
        raise GithubIssueCollectionError(f"GitHub API request failed: {last_error}")

    def search_issues(self, query: str, *, page: int, per_page: int) -> Tuple[Dict[str, Any], Dict[str, str]]:
        params = parse.urlencode({
            "q": query,
            "sort": "updated",
            "order": "desc",
            "page": page,
            "per_page": per_page,
        })
        payload, headers = self._get(f"{self.base_url}/search/issues?{params}")
        if not isinstance(payload, dict):
            raise GithubIssueCollectionError("GitHub issue search response must be an object")
        return payload, headers

    def list_comments(self, comments_url: str, *, page: int, per_page: int) -> Tuple[List[Any], Dict[str, str]]:
        separator = "&" if "?" in comments_url else "?"
        payload, headers = self._get(
            f"{comments_url}{separator}{parse.urlencode({'page': page, 'per_page': per_page})}"
        )
        if not isinstance(payload, list):
            raise GithubIssueCollectionError("GitHub issue comments response must be a list")
        return payload, headers


def _comment(item: Mapping[str, Any], root_url: str) -> Optional[Dict[str, Any]]:
    body = item.get("body")
    if not isinstance(body, str) or not body.strip():
        return None
    user = item.get("user") if isinstance(item.get("user"), Mapping) else {}
    html_url = item.get("html_url")
    try:
        source_url = precise_github_issue_locator_url(html_url or root_url)
    except GithubIssueCollectionError:
        source_url = root_url
    reactions = item.get("reactions") if isinstance(item.get("reactions"), Mapping) else {}
    return {
        "comment_id": item.get("id"),
        "author_display": user.get("login"),
        "author_association": item.get("author_association"),
        "text": body[:5000],
        "text_truncated": len(body) > 5000,
        "published_display": item.get("created_at"),
        "updated_at": item.get("updated_at"),
        "likes": reactions.get("+1", 0),
        "source_url": source_url,
    }


def _issue_candidate(item: Mapping[str, Any], task: Mapping[str, Any]) -> Optional[Dict[str, Any]]:
    if "pull_request" in item:
        return None
    try:
        canonical_url, repository, issue_number, stable_id = canonicalize_github_issue_url(
            item.get("html_url")
        )
    except GithubIssueCollectionError:
        return None
    body = item.get("body") if isinstance(item.get("body"), str) else ""
    title = item.get("title") if isinstance(item.get("title"), str) else f"Issue #{issue_number}"
    user = item.get("user") if isinstance(item.get("user"), Mapping) else {}
    reactions = item.get("reactions") if isinstance(item.get("reactions"), Mapping) else {}
    match = {
        "task_id": task.get("task_id"),
        "task_signature": task.get("task_signature"),
        "scope_id": task.get("scope_id"),
        "query": task.get("query"),
        "repositories": task.get("repositories"),
        "window_id": task.get("window_id"),
        "origin": task.get("origin"),
    }
    return {
        "schema_version": 1,
        "platform": "github_issue",
        "post_id": stable_id,
        "canonical_url": canonical_url,
        "repository": repository,
        "issue_number": issue_number,
        "scope_id": task.get("scope_id"),
        "query": task.get("query"),
        "matches": [match],
        "title": title[:500],
        "author_display": user.get("login"),
        "author_association": item.get("author_association"),
        "published_at": item.get("created_at"),
        "updated_at": item.get("updated_at"),
        "closed_at": item.get("closed_at"),
        "issue_state": item.get("state"),
        "state_reason": item.get("state_reason"),
        "locked": bool(item.get("locked", False)),
        "body_text": body[:50_000],
        "body_characters": len(body),
        "body_truncated": len(body) > 50_000,
        "body_sha256": hashlib.sha256(body.encode("utf-8")).hexdigest(),
        "comments_url": item.get("comments_url"),
        "comments_reported": int(item.get("comments", 0) or 0),
        "selected_comments": [],
        "comments_complete": False,
        "labels": [
            value.get("name") for value in item.get("labels", [])
            if isinstance(value, Mapping) and isinstance(value.get("name"), str)
        ],
        "attention": {
            "comments": int(item.get("comments", 0) or 0),
            "reactions": int(reactions.get("total_count", 0) or 0),
        },
        "access_mode": "public_api",
        "content_collected": True,
        "review_status": "pending_analysis",
        "captured_at": None,
        "extraction_provenance": {
            "method": "github_documented_rest_api",
            "credential_persisted": False,
            "auto_published": False,
        },
    }


def _merge_candidate(existing: Dict[str, Any], incoming: Dict[str, Any]) -> None:
    known = {value.get("task_signature") for value in existing["matches"]}
    for match in incoming["matches"]:
        if match.get("task_signature") not in known:
            existing["matches"].append(match)


def merge_github_connector_runs(
    candidate_runs: Sequence[Mapping[str, Any]],
    *,
    comment_runs: Sequence[Mapping[str, Any]] = (),
    merged_at: Optional[datetime] = None,
) -> Dict[str, Any]:
    """Merge connected-app exports by canonical Issue/comment URL.

    The connected app is useful when a Codex session already has GitHub access;
    the result contract remains identical to the documented REST collector and
    never stores connector credentials.
    """

    current = _now(merged_at)
    by_url: Dict[str, Dict[str, Any]] = {}
    raw_candidates = 0
    for run_index, run in enumerate(candidate_runs):
        if not isinstance(run, Mapping):
            raise GithubIssueCollectionError(f"candidate_runs[{run_index}] must be an object")
        candidates = run.get("candidates", [])
        if not isinstance(candidates, list):
            raise GithubIssueCollectionError(
                f"candidate_runs[{run_index}].candidates must be a list"
            )
        for candidate in candidates:
            if not isinstance(candidate, Mapping):
                continue
            raw_candidates += 1
            try:
                canonical, repository, issue_number, stable_id = canonicalize_github_issue_url(
                    candidate.get("canonical_url")
                )
            except GithubIssueCollectionError:
                continue
            normalized = dict(candidate)
            normalized.update({
                "platform": "github_issue",
                "post_id": stable_id,
                "canonical_url": canonical,
                "repository": repository,
                "issue_number": issue_number,
                "captured_at": candidate.get("captured_at") or _iso(current),
            })
            normalized.setdefault("matches", [])
            normalized.setdefault("selected_comments", [])
            existing = by_url.get(canonical)
            if existing is None:
                by_url[canonical] = normalized
                continue
            _merge_candidate(existing, normalized)
            if int(normalized.get("body_characters", 0) or 0) > int(
                existing.get("body_characters", 0) or 0
            ):
                for field in (
                    "title", "body_text", "body_characters", "body_sha256",
                    "body_truncated", "author_display", "published_at", "updated_at",
                    "closed_at", "issue_state", "state_reason", "labels",
                ):
                    if field in normalized:
                        existing[field] = normalized[field]

    comment_issue_count = 0
    raw_comments = 0
    for run_index, run in enumerate(comment_runs):
        if not isinstance(run, Mapping):
            raise GithubIssueCollectionError(f"comment_runs[{run_index}] must be an object")
        issues = run.get("issues", [])
        if not isinstance(issues, list):
            raise GithubIssueCollectionError(
                f"comment_runs[{run_index}].issues must be a list"
            )
        for issue in issues:
            if not isinstance(issue, Mapping):
                continue
            try:
                canonical, _, _, _ = canonicalize_github_issue_url(
                    issue.get("canonical_url")
                )
            except GithubIssueCollectionError:
                continue
            candidate = by_url.get(canonical)
            if candidate is None:
                continue
            comments = issue.get("comments", [])
            if not isinstance(comments, list):
                continue
            comment_issue_count += 1
            existing_keys = {
                (value.get("comment_id"), value.get("source_url"))
                for value in candidate.get("selected_comments", [])
                if isinstance(value, Mapping)
            }
            for comment in comments:
                if not isinstance(comment, Mapping) or not isinstance(comment.get("text"), str):
                    continue
                raw_comments += 1
                source_url = precise_github_issue_locator_url(
                    comment.get("source_url") or canonical
                )
                normalized_comment = dict(comment)
                normalized_comment["source_url"] = source_url
                key = (normalized_comment.get("comment_id"), source_url)
                if key not in existing_keys:
                    candidate.setdefault("selected_comments", []).append(normalized_comment)
                    existing_keys.add(key)
            reported = candidate.get("comments_reported")
            candidate["comments_complete"] = (
                isinstance(reported, int)
                and len(candidate.get("selected_comments", [])) >= reported
            )

    fingerprint = hashlib.sha256(
        "\n".join(sorted(by_url)).encode("utf-8")
    ).hexdigest()[:12]
    return {
        "schema_version": 1,
        "run_id": f"github-connector-merged-{current.strftime('%Y%m%d%H%M%S')}-{fingerprint}",
        "created_at": _iso(current),
        "trigger": "manual_on_demand",
        "platform": "github_issue",
        "access_mode": "public_api",
        "candidates": list(by_url.values()),
        "stats": {
            "candidate_runs": len(candidate_runs),
            "raw_candidates": raw_candidates,
            "unique_candidates": len(by_url),
            "duplicates_merged": raw_candidates - len(by_url),
            "comment_runs": len(comment_runs),
            "comment_issues_matched": comment_issue_count,
            "comments_merged": raw_comments,
        },
        "auto_published": False,
    }


def collect_github_issue_candidates(
    plan: Mapping[str, Any],
    client: GithubIssueApiClient,
    *,
    previous_state: Optional[Mapping[str, Any]] = None,
    max_issues_per_run: int = 1000,
    max_comments_per_issue: int = 100,
    enrich_comments: bool = True,
    refresh_known: bool = False,
    collected_at: Optional[datetime] = None,
) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    """Execute selected tasks while preserving unfinished pages and exact URLs."""

    if plan.get("schema_version") != GITHUB_PLAN_SCHEMA_VERSION:
        raise GithubIssueCollectionError("GitHub issue plan schema_version is unsupported")
    if not 1 <= max_issues_per_run <= GITHUB_MAX_ISSUES_PER_RUN:
        raise GithubIssueCollectionError("max_issues_per_run must be in [1, 5000]")
    if not 0 <= max_comments_per_issue <= GITHUB_MAX_COMMENTS_PER_ISSUE:
        raise GithubIssueCollectionError("max_comments_per_issue must be in [0, 500]")
    current = _now(collected_at)
    state = _state(previous_state, current)
    limits = plan.get("limits", {})
    max_pages = int(limits.get("max_pages_per_task", GITHUB_MAX_SEARCH_PAGES))
    per_page = int(limits.get("per_page", GITHUB_MAX_PER_PAGE))
    by_url: Dict[str, Dict[str, Any]] = {}
    failures: List[Dict[str, Any]] = []
    requests_made = 0
    known_unchanged_skipped = 0
    task_results = []
    remaining_budget = max_issues_per_run
    known_before = dict(state["known_urls"])

    for task in plan.get("tasks", []):
        if remaining_budget <= 0:
            break
        signature = task["task_signature"]
        history = dict(state["tasks"].get(signature, {}))
        page = int(history.get("next_page", task.get("resume_page", 1)) or 1)
        pages_read = 0
        observed_urls: List[str] = []
        newest_updated_at = history.get("newest_updated_at")
        search_query = task["search_query"]
        if task.get("rolling") and newest_updated_at:
            search_query += f" updated:>{newest_updated_at}"
        task_complete = False
        total_count = None
        try:
            while pages_read < max_pages and remaining_budget > 0:
                payload, _headers = client.search_issues(
                    search_query, page=page, per_page=per_page
                )
                requests_made += 1
                items = payload.get("items", [])
                if not isinstance(items, list):
                    raise GithubIssueCollectionError("GitHub search items must be a list")
                total_count = int(payload.get("total_count", 0) or 0)
                page_fully_scanned = True
                for item in items:
                    if remaining_budget <= 0:
                        page_fully_scanned = False
                        break
                    if not isinstance(item, Mapping):
                        continue
                    candidate = _issue_candidate(item, task)
                    if candidate is None:
                        continue
                    url = candidate["canonical_url"]
                    observed_urls.append(url)
                    known = known_before.get(url, {})
                    changed = (
                        not known
                        or known.get("issue_updated_at") != candidate.get("updated_at")
                        or known.get("body_sha256") != candidate.get("body_sha256")
                    )
                    if not refresh_known and not changed:
                        known_unchanged_skipped += 1
                        continue
                    if candidate.get("updated_at") and (
                        newest_updated_at is None
                        or candidate["updated_at"] > newest_updated_at
                    ):
                        newest_updated_at = candidate["updated_at"]
                    existing = by_url.get(url)
                    if existing is None:
                        candidate["captured_at"] = _iso(current)
                        by_url[url] = candidate
                        remaining_budget -= 1
                    else:
                        _merge_candidate(existing, candidate)
                if not page_fully_scanned:
                    # Resume the same API page.  Already stored canonical URLs
                    # will be skipped, so exhausting the global budget cannot
                    # discard the unprocessed tail of a page.
                    break
                pages_read += 1
                page += 1
                if len(items) < per_page or page > GITHUB_MAX_SEARCH_PAGES:
                    task_complete = True
                    break
        except GithubIssueCollectionError as exc:
            failures.append({
                "task_id": task.get("task_id"),
                "task_signature": signature,
                "page": page,
                "error": str(exc),
            })

        next_page = None if task_complete else page
        run_count = int(history.get("run_count", 0) or 0) + 1
        if task_complete and task.get("rolling"):
            next_eligible = current + timedelta(hours=24)
            state_complete = False
            next_page = 1
        else:
            next_eligible = current
            state_complete = task_complete
        history.update({
            "scope_id": task.get("scope_id"),
            "query": task.get("query"),
            "repositories": task.get("repositories"),
            "window_id": task.get("window_id"),
            "rolling": bool(task.get("rolling")),
            "run_count": run_count,
            "complete": state_complete,
            "next_page": next_page,
            "newest_updated_at": newest_updated_at,
            "last_run_at": _iso(current),
            "last_observed_urls": len(set(observed_urls)),
            "last_new_or_changed": len(
                [url for url in set(observed_urls) if url not in known_before]
            ),
            "next_eligible_at": _iso(next_eligible),
            "total_count_reported": total_count,
        })
        state["tasks"][signature] = history
        task_results.append({
            "task_id": task.get("task_id"),
            "task_signature": signature,
            "pages_read": pages_read,
            "observed_urls": len(set(observed_urls)),
            "complete": state_complete,
            "next_page": next_page,
            "total_count_reported": total_count,
        })

    if enrich_comments and max_comments_per_issue:
        for candidate in by_url.values():
            comments_url = candidate.get("comments_url")
            if not isinstance(comments_url, str) or not comments_url:
                candidate["comments_complete"] = candidate["comments_reported"] == 0
                continue
            comments: List[Dict[str, Any]] = []
            page = 1
            try:
                while len(comments) < max_comments_per_issue:
                    requested = min(100, max_comments_per_issue - len(comments))
                    values, _headers = client.list_comments(
                        comments_url, page=page, per_page=requested
                    )
                    requests_made += 1
                    for value in values:
                        if isinstance(value, Mapping):
                            normalized = _comment(value, candidate["canonical_url"])
                            if normalized:
                                comments.append(normalized)
                    if len(values) < requested:
                        break
                    page += 1
            except GithubIssueCollectionError as exc:
                failures.append({
                    "stage": "comments",
                    "canonical_url": candidate["canonical_url"],
                    "page": page,
                    "error": str(exc),
                })
            candidate["selected_comments"] = comments[:max_comments_per_issue]
            candidate["comments_complete"] = (
                len(comments) >= candidate["comments_reported"]
                and candidate["comments_reported"] <= max_comments_per_issue
            )

    for url, candidate in by_url.items():
        known = dict(state["known_urls"].get(url, {}))
        known.update({
            "repository": candidate.get("repository"),
            "issue_number": candidate.get("issue_number"),
            "first_seen_at": known.get("first_seen_at", _iso(current)),
            "last_seen_at": _iso(current),
            "issue_updated_at": candidate.get("updated_at"),
            "body_sha256": candidate.get("body_sha256"),
            "comments_reported": candidate.get("comments_reported"),
        })
        state["known_urls"][url] = known

    run_summary = {
        "run_id": plan.get("run_id"),
        "completed_at": _iso(current),
        "selected_tasks": len(plan.get("tasks", [])),
        "task_results": len(task_results),
        "candidates": len(by_url),
        "failures": len(failures),
        "requests_made": requests_made,
    }
    state["runs"].append(run_summary)
    state["runs"] = state["runs"][-100:]
    state["updated_at"] = _iso(current)
    result = {
        "schema_version": 1,
        "run_id": plan.get("run_id"),
        "created_at": _iso(current),
        "trigger": "manual_on_demand",
        "platform": "github_issue",
        "access_mode": "public_api",
        "candidates": list(by_url.values()),
        "task_results": task_results,
        "request_failures": failures,
        "stats": {
            "unique_candidates": len(by_url),
            "known_unchanged_skipped": known_unchanged_skipped,
            "requests_made": requests_made,
        },
        "auto_published": False,
    }
    return result, state
