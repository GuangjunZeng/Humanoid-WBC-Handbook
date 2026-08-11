"""Command-line interface for the offline handbook pipeline."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sqlite3
import sys
from typing import Any, Mapping

from .answer import answer, render_markdown
from .importer import normalize_manual_source
from .index import build_index
from .models import Domain, ModelError
from .paper_catalog import (
    coverage_report,
    discover_candidates,
    load_json,
    validate_catalog,
    write_candidate_run,
)
from .repository import HandbookRepository, RepositoryError
from .social import (
    MANUAL_REVIEW_PLATFORMS,
    SocialCollectionError,
    build_collection_plan,
    deduplicate_social_sources,
    normalize_social_capture,
    queries_from_config,
    render_engineering_qa_markdown,
)
from .social_browser import (
    BROWSER_PLATFORMS,
    BrowserCollectionError,
    build_browser_collection_plan,
    normalize_browser_collection_run,
)
from .social_discovery import (
    SocialDiscoveryError,
    evolve_query_frontier,
    frontier_queries,
    frontier_topic_ids,
    render_query_frontier_markdown,
    select_incremental_queries,
    update_discovery_state,
)
from .social_github import (
    GithubIssueApiClient,
    GithubIssueCollectionError,
    build_github_issue_plan,
    collect_github_issue_candidates,
    merge_github_connector_runs,
)
from .social_inventory import (
    SocialInventoryError,
    build_social_candidate_inventory,
    render_pending_markdown,
)
from .social_x import (
    XApiClient,
    XCollectionError,
    build_x_collection_plan,
    collect_x_candidates,
    extract_x_post_id,
)
from .social_zhihu import (
    ZhihuApiClient,
    ZhihuCollectionError,
    build_zhihu_collection_plan,
    collect_zhihu_candidates,
)
from .social_xiaohongshu import (
    XiaohongshuQueueError,
    apply_xhs_review_decisions,
    build_xhs_review_plan,
    build_xhs_review_queue,
)
from .validator import has_errors, validate_repository
from .web_search import (
    DEFAULT_BRANCH,
    DEFAULT_REPOSITORY_URL,
    DEFAULT_TRANSLATIONS_DIR,
    WebSearchError,
    build_web_index,
    collect_web_problems,
    render_problem_pages,
)


def _repository(path: str) -> HandbookRepository:
    return HandbookRepository(Path(path))


def command_validate(args: argparse.Namespace) -> int:
    repository = _repository(args.data_dir)
    try:
        sources = repository.load_sources()
        claims = repository.load_claims()
    except (RepositoryError, ModelError, ValueError) as exc:
        print(json.dumps({"ok": False, "error": str(exc)}, ensure_ascii=False, indent=2))
        return 2
    issues = validate_repository(sources, claims)
    report = {
        "ok": not has_errors(issues),
        "counts": {"sources": len(sources), "claims": len(claims), "issues": len(issues)},
        "issues": [issue.to_dict() for issue in issues],
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["ok"] else 2


def command_import_source(args: argparse.Namespace) -> int:
    try:
        raw = json.loads(Path(args.input).read_text(encoding="utf-8"))
        if not isinstance(raw, dict):
            raise ModelError("manual source input must be one JSON object")
        source = normalize_manual_source(raw)
        target = _repository(args.data_dir).save_source(source, overwrite=args.overwrite)
    except (OSError, json.JSONDecodeError, ModelError, RepositoryError, ValueError) as exc:
        print(f"import failed: {exc}", file=sys.stderr)
        return 2
    print(json.dumps({"source_id": source.source_id, "path": str(target)}, ensure_ascii=False))
    return 0


def _read_json(path: str) -> Any:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def _filter_social_queries(
    queries: list, scopes: Any = None, domains: Any = None
) -> list:
    if scopes:
        selected_scopes = set(scopes)
        queries = [item for item in queries if item["scope_id"] in selected_scopes]
    if domains:
        selected_domains = set(domains)
        queries = [
            item for item in queries
            if selected_domains.intersection(item["domain_hints"])
        ]
    return queries


def command_social_plan(args: argparse.Namespace) -> int:
    """Create a finite manual link-review list without network access."""

    try:
        raw = _read_json(args.config)
        if not isinstance(raw, Mapping):
            raise SocialCollectionError("social query config must be one JSON object")
        queries = queries_from_config(raw)
        queries = _filter_social_queries(queries, args.scope, args.domain)
        configured_platforms = [
            platform for platform in raw.get("platforms", MANUAL_REVIEW_PLATFORMS)
            if platform in MANUAL_REVIEW_PLATFORMS
        ]
        platforms = args.platform or configured_platforms
        limits = raw.get("limits", {})
        if not isinstance(limits, Mapping):
            raise SocialCollectionError("social query config limits must be an object")
        max_results = (
            args.max_results_per_query
            if args.max_results_per_query is not None
            else limits.get("max_results_per_query", 5)
        )
        max_comments = (
            args.max_comments_per_post
            if args.max_comments_per_post is not None
            else limits.get("max_comments_per_post", 10)
        )
        max_tasks_per_batch = (
            args.max_tasks_per_batch
            if args.max_tasks_per_batch is not None
            else limits.get("max_tasks_per_batch", 12)
        )
        known_urls = []
        if not args.refresh_known:
            known_urls = [
                source.canonical_url
                for source in _repository(args.data_dir).load_sources()
                if source.kind.value == "community"
            ]
        plan = build_collection_plan(
            queries,
            platforms=platforms,
            max_results_per_query=max_results,
            max_comments_per_post=max_comments,
            max_tasks_per_batch=max_tasks_per_batch,
            known_canonical_urls=known_urls,
        )
        target = Path(args.output)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(
            json.dumps(plan, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    except (
        OSError,
        json.JSONDecodeError,
        ModelError,
        RepositoryError,
        SocialCollectionError,
        ValueError,
    ) as exc:
        print(f"social plan failed: {exc}", file=sys.stderr)
        return 2
    print(json.dumps({
        "run_id": plan["run_id"],
        "path": str(target),
        "tasks": len(plan["tasks"]),
        "batches": len(plan["batches"]),
        "scopes": len({task["scope_id"] for task in plan["tasks"]}),
        "known_urls": len(plan["known_canonical_urls"]),
        "trigger": plan["trigger"],
    }, ensure_ascii=False, indent=2))
    return 0


def command_social_collect_x(args: argparse.Namespace) -> int:
    """Run one bounded, user-triggered collection through official X API v2."""

    try:
        raw = _read_json(args.config)
        if not isinstance(raw, Mapping):
            raise XCollectionError("social query config must be one JSON object")
        configured_queries = _filter_social_queries(
            queries_from_config(raw, platform="x"), args.scope, args.domain
        )
        ad_hoc = bool(args.query or args.post or args.conversation)
        queries = configured_queries if (not ad_hoc or args.include_config_queries) else []
        for query in args.query or []:
            queries.append({
                "scope_id": "open_ended_wbc_field_notes",
                "domain_hints": [],
                "query": query,
            })

        direct_post_ids = [extract_x_post_id(value) for value in args.post or []]
        for value in args.conversation or []:
            conversation_id = extract_x_post_id(value)
            direct_post_ids.append(conversation_id)
            queries.append({
                "scope_id": "open_ended_wbc_field_notes",
                "domain_hints": [],
                "query": f"conversation_id:{conversation_id}",
            })
        direct_post_ids = list(dict.fromkeys(direct_post_ids))
        if not queries and not direct_post_ids:
            raise XCollectionError("select at least one config query, --query, or --post")
        if not 0 <= args.max_retries <= 10:
            raise XCollectionError("--max-retries must be in [0, 10]")
        if not 0 <= args.max_retry_wait_seconds <= 60:
            raise XCollectionError(
                "--max-retry-wait-seconds must be in [0, 60]"
            )

        target = Path(args.output)
        target.parent.mkdir(parents=True, exist_ok=True)
        if args.dry_run:
            result = build_x_collection_plan(
                queries,
                mode=args.mode,
                max_posts_per_query=args.max_posts_per_query,
                max_pages=args.max_pages,
                direct_post_ids=direct_post_ids,
            )
            result["start_time"] = args.start_time
            result["end_time"] = args.end_time
            result["sort_order"] = args.sort_order
            result["retry"] = {
                "max_retries": args.max_retries,
                "max_retry_wait_seconds": args.max_retry_wait_seconds,
            }
            next_state = None
        else:
            previous_state = {}
            state_path = Path(args.state)
            if not args.no_state and state_path.exists():
                previous_state = _read_json(str(state_path))
                if not isinstance(previous_state, Mapping):
                    raise XCollectionError("X state file must be one JSON object")
            client = XApiClient.from_environment(
                args.token_env,
                max_retries=args.max_retries,
                max_retry_wait_seconds=args.max_retry_wait_seconds,
            )
            result, next_state = collect_x_candidates(
                queries,
                client,
                mode=args.mode,
                max_posts_per_query=args.max_posts_per_query,
                max_pages=args.max_pages,
                direct_post_ids=direct_post_ids,
                previous_state=previous_state,
                use_state=not args.no_state,
                start_time=args.start_time,
                end_time=args.end_time,
                sort_order=args.sort_order,
            )
            if not args.no_state:
                state_path.parent.mkdir(parents=True, exist_ok=True)
                state_path.write_text(
                    json.dumps(next_state, ensure_ascii=False, indent=2, sort_keys=True)
                    + "\n",
                    encoding="utf-8",
                )
        if args.conversation and args.mode == "recent":
            result.setdefault("warnings", []).append(
                "conversation search uses the recent endpoint and only covers "
                "replies available in its current recent window; use --mode all "
                "with sufficient entitlement for full-archive thread recovery"
            )
        target.write_text(
            json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    except (
        OSError,
        json.JSONDecodeError,
        ModelError,
        SocialCollectionError,
        XCollectionError,
        ValueError,
    ) as exc:
        print(f"X collection failed: {exc}", file=sys.stderr)
        return 2

    print(json.dumps({
        "run_id": result["run_id"],
        "dry_run": args.dry_run,
        "mode": args.mode,
        "sort_order": args.sort_order,
        "path": str(target),
        "queries": len(result["queries"]) if args.dry_run else len(result["query_results"]),
        "candidates": 0 if args.dry_run else len(result["candidates"]),
        "estimated_post_read_upper_bound": result.get(
            "estimated_post_read_upper_bound"
        ),
        "state": None if args.dry_run or args.no_state else str(Path(args.state)),
        "queries_complete": None if args.dry_run else result["stats"]["queries_complete"],
        "queries_resume_pending": (
            None if args.dry_run else result["stats"]["queries_resume_pending"]
        ),
        "api_errors": None if args.dry_run else result["stats"]["api_errors"],
        "request_failures": (
            None if args.dry_run else result["stats"]["request_failures"]
        ),
    }, ensure_ascii=False, indent=2))
    if not args.dry_run and result["stats"]["request_failures"]:
        return 3
    return 0


def command_social_collect_zhihu(args: argparse.Namespace) -> int:
    """Run one bounded discovery pass through Zhihu's official search API."""

    try:
        raw = _read_json(args.config)
        if not isinstance(raw, Mapping):
            raise ZhihuCollectionError("social query config must be one JSON object")
        configured_queries = _filter_social_queries(
            queries_from_config(raw, platform="zhihu"), args.scope, args.domain
        )
        queries = configured_queries if not args.query or args.include_config_queries else []
        for query in args.query or []:
            queries.append({
                "scope_id": "open_ended_wbc_field_notes",
                "domain_hints": [],
                "query": query,
            })
        if not queries:
            raise ZhihuCollectionError("select at least one config query or --query")

        target = Path(args.output)
        target.parent.mkdir(parents=True, exist_ok=True)
        if args.dry_run:
            result = build_zhihu_collection_plan(queries, count=args.count)
        else:
            previous_state = {}
            state_path = Path(args.state)
            if not args.no_state and state_path.exists():
                previous_state = _read_json(str(state_path))
                if not isinstance(previous_state, Mapping):
                    raise ZhihuCollectionError("Zhihu state file must be one JSON object")
            client = ZhihuApiClient.from_environment(args.secret_env)
            result, next_state = collect_zhihu_candidates(
                queries,
                client,
                count=args.count,
                previous_state=previous_state,
                refresh_known=args.refresh_known,
            )
            if not args.no_state:
                state_path.parent.mkdir(parents=True, exist_ok=True)
                state_path.write_text(
                    json.dumps(next_state, ensure_ascii=False, indent=2, sort_keys=True)
                    + "\n",
                    encoding="utf-8",
                )
        target.write_text(
            json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    except (
        OSError,
        json.JSONDecodeError,
        ModelError,
        SocialCollectionError,
        ZhihuCollectionError,
        ValueError,
    ) as exc:
        print(f"Zhihu collection failed: {exc}", file=sys.stderr)
        return 2

    print(json.dumps({
        "run_id": result["run_id"],
        "dry_run": args.dry_run,
        "path": str(target),
        "queries": len(result["queries"]) if args.dry_run else len(result["query_results"]),
        "candidates": 0 if args.dry_run else len(result["candidates"]),
        "state": None if args.dry_run or args.no_state else str(Path(args.state)),
        "full_text_available": False,
    }, ensure_ascii=False, indent=2))
    return 0


def command_social_browser_plan(args: argparse.Namespace) -> int:
    """Build a finite task file for a user-triggered visible-browser run."""

    try:
        raw = _read_json(args.config)
        if not isinstance(raw, Mapping):
            raise BrowserCollectionError("social query config must be one JSON object")
        direct_posts = args.post or []
        if direct_posts and args.platform and "x" not in args.platform:
            raise BrowserCollectionError("--post requires --platform x")
        platforms = args.platform or (["x"] if direct_posts else BROWSER_PLATFORMS)
        configured_queries = []
        for query_platform in platforms:
            platform_queries = _filter_social_queries(
                queries_from_config(raw, platform=query_platform),
                args.scope,
                args.domain,
            )
            for item in platform_queries:
                configured_queries.append({**item, "platforms": [query_platform]})
        frontier = None
        dynamic_queries = []
        frontier_path = Path(args.frontier)
        if frontier_path.exists():
            frontier = _read_json(str(frontier_path))
            if args.topic:
                missing = sorted(set(args.topic) - frontier_topic_ids(frontier))
                if missing:
                    raise BrowserCollectionError(
                        "unknown frontier topic_id: " + ", ".join(missing)
                    )
            dynamic_queries = frontier_queries(
                frontier, platforms, topic_ids=args.topic
            )
        elif args.topic:
            raise BrowserCollectionError("--topic requires an existing query frontier")
        ad_hoc = bool(args.query or args.post or args.topic)
        queries = (
            list(configured_queries)
            if (not ad_hoc or args.include_config_queries)
            else []
        )
        if not ad_hoc or args.include_config_queries or args.topic:
            queries.extend(dynamic_queries)
        for query in args.query or []:
            queries.append({
                "scope_id": "open_ended_wbc_field_notes",
                "domain_hints": [],
                "query": query,
            })
        if not queries and not direct_posts:
            raise BrowserCollectionError(
                "select at least one config query, --query, or X --post"
            )
        discovery_state = None
        discovery_state_path = Path(args.state)
        if discovery_state_path.exists():
            discovery_state = _read_json(str(discovery_state_path))
        selection = select_incremental_queries(
            queries,
            platforms=platforms,
            state=discovery_state,
            max_queries_per_platform=args.max_queries_per_platform,
            min_repeat_hours=args.min_query_repeat_hours,
            force=args.refresh_queries or ad_hoc,
        )
        queries = selection["selected"]
        if not queries and not direct_posts:
            raise BrowserCollectionError(
                "no query is currently eligible; use --refresh-queries to override "
                "the low-repeat ledger"
            )
        known_urls = []
        if not args.refresh_known:
            known_urls = [
                source.canonical_url
                for source in _repository(args.data_dir).load_sources()
                if source.kind.value == "community"
            ]
            if isinstance(discovery_state, Mapping):
                state_urls = discovery_state.get("known_urls", {})
                if isinstance(state_urls, Mapping):
                    known_urls.extend(str(value) for value in state_urls)
        plan = build_browser_collection_plan(
            queries,
            platforms=platforms,
            max_results_per_query=args.max_results_per_query,
            max_comments_per_post=args.max_comments_per_post,
            max_posts_per_run=args.max_posts_per_run,
            max_reply_expansions=args.max_reply_expansions,
            reply_depth_limit=args.reply_depth_limit,
            post_time_budget_seconds=args.post_time_budget_seconds,
            reply_no_growth_patience=args.reply_no_growth_patience,
            direct_post_urls=direct_posts,
            known_canonical_urls=known_urls,
        )
        plan["query_selection"] = selection
        plan["discovery_state_path"] = str(discovery_state_path)
        plan["query_frontier_path"] = str(frontier_path)
        target = Path(args.output)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(
            json.dumps(plan, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    except (
        OSError,
        json.JSONDecodeError,
        ModelError,
        RepositoryError,
        SocialCollectionError,
        BrowserCollectionError,
        ValueError,
    ) as exc:
        print(f"browser collection plan failed: {exc}", file=sys.stderr)
        return 2
    print(json.dumps({
        "run_id": plan["run_id"],
        "path": str(target),
        "platforms": plan["platforms"],
        "tasks": len(plan["tasks"]),
        "queries_selected": selection["counts"]["selected"],
        "queries_deferred": selection["counts"]["skipped"],
        "estimated_max_detail_pages": plan["limits"]["estimated_max_detail_pages"],
        "trigger": plan["trigger"],
        "requires_visible_browser": True,
    }, ensure_ascii=False, indent=2))
    return 0


def command_social_browser_ingest(args: argparse.Namespace) -> int:
    """Normalize pages extracted by the visible-browser agent."""

    try:
        raw = _read_json(args.input)
        if not isinstance(raw, Mapping):
            raise BrowserCollectionError("browser input must be one JSON object")
        result = normalize_browser_collection_run(raw)
        target = Path(args.output)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(
            json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        ledger_summary = None
        frontier_summary = None
        plan_path = Path(args.plan)
        if not args.no_state and plan_path.exists():
            plan = _read_json(str(plan_path))
            if not isinstance(plan, Mapping):
                raise BrowserCollectionError("browser plan must be one JSON object")
            state_path = Path(args.state)
            previous_state = _read_json(str(state_path)) if state_path.exists() else None
            next_state = update_discovery_state(
                plan,
                result,
                previous_state=previous_state,
                min_repeat_hours=args.min_query_repeat_hours,
            )
            state_path.parent.mkdir(parents=True, exist_ok=True)
            state_path.write_text(
                json.dumps(next_state, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
                encoding="utf-8",
            )
            ledger_summary = next_state["runs"][-1]
        if not args.no_evolve:
            config = _read_json(args.config)
            if not isinstance(config, Mapping):
                raise SocialDiscoveryError("social query config must be one object")
            existing_queries = []
            for platform in BROWSER_PLATFORMS:
                for item in queries_from_config(config, platform=platform):
                    existing_queries.append({**item, "platforms": [platform]})
            frontier_path = Path(args.frontier)
            previous_frontier = (
                _read_json(str(frontier_path)) if frontier_path.exists() else None
            )
            next_frontier = evolve_query_frontier(
                result["candidates"],
                existing_queries=existing_queries,
                previous_frontier=previous_frontier,
            )
            frontier_path.parent.mkdir(parents=True, exist_ok=True)
            frontier_path.write_text(
                json.dumps(next_frontier, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
                encoding="utf-8",
            )
            frontier_summary = next_frontier["counts"]
    except (
        OSError,
        json.JSONDecodeError,
        BrowserCollectionError,
        SocialCollectionError,
        ValueError,
    ) as exc:
        print(f"browser collection ingest failed: {exc}", file=sys.stderr)
        return 2
    state_counts = {}
    for blocker in result["blockers"]:
        state = blocker["state"]
        state_counts[state] = state_counts.get(state, 0) + 1
    print(json.dumps({
        "run_id": result["run_id"],
        "path": str(target),
        "pages_received": result["pages_received"],
        "candidates": len(result["candidates"]),
        "duplicates_merged": result["stats"]["duplicates_merged"],
        "empty_searches": result["stats"].get("unique_completed_searches", 0),
        "blockers": state_counts,
        "ledger": ledger_summary,
        "query_frontier": frontier_summary,
        "auto_published": False,
    }, ensure_ascii=False, indent=2))
    return 0


def command_social_evolve_queries(args: argparse.Namespace) -> int:
    """Mine evidence-linked technical entities from candidate files."""

    try:
        candidates = []
        for input_path in args.input:
            raw = _read_json(input_path)
            if isinstance(raw, Mapping):
                values = raw.get(
                    "candidates", raw.get("pages", raw.get("captures"))
                )
            else:
                values = raw
            if not isinstance(values, list):
                raise SocialDiscoveryError(
                    f"{input_path} must be a list or contain "
                    "candidates/pages/captures[]"
                )
            candidates.extend(values)
        config = _read_json(args.config)
        if not isinstance(config, Mapping):
            raise SocialDiscoveryError("social query config must be one object")
        existing_queries = []
        for platform in BROWSER_PLATFORMS:
            for item in queries_from_config(config, platform=platform):
                existing_queries.append({**item, "platforms": [platform]})
        output_path = Path(args.output)
        previous = _read_json(str(output_path)) if output_path.exists() else None
        frontier = evolve_query_frontier(
            candidates,
            existing_queries=existing_queries,
            previous_frontier=previous,
        )
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(
            json.dumps(frontier, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    except (OSError, json.JSONDecodeError, SocialDiscoveryError, SocialCollectionError) as exc:
        print(f"query frontier update failed: {exc}", file=sys.stderr)
        return 2
    print(json.dumps({
        "path": str(output_path),
        "topics": len(frontier["topics"]),
        "counts": frontier["counts"],
    }, ensure_ascii=False, indent=2))
    return 0


def command_social_frontier_report(args: argparse.Namespace) -> int:
    """Render every frontier topic, evidence link, and scheduling state."""

    try:
        frontier = _read_json(args.frontier)
        if not isinstance(frontier, Mapping):
            raise SocialDiscoveryError("query frontier must be one object")
        state_path = Path(args.state)
        state = _read_json(str(state_path)) if state_path.exists() else None
        if state is not None and not isinstance(state, Mapping):
            raise SocialDiscoveryError("discovery state must be one object")
        markdown = render_query_frontier_markdown(
            frontier, discovery_state=state
        )
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(markdown, encoding="utf-8")
    except (OSError, json.JSONDecodeError, SocialDiscoveryError) as exc:
        print(f"query frontier report failed: {exc}", file=sys.stderr)
        return 2
    print(json.dumps({
        "path": str(output_path),
        "topics": len(frontier.get("topics", [])),
        "complete_catalogue": True,
    }, ensure_ascii=False, indent=2))
    return 0


def command_github_issue_plan(args: argparse.Namespace) -> int:
    """Build a bounded, resumable GitHub Issues backfill plan."""

    try:
        config = _read_json(args.config)
        if not isinstance(config, Mapping):
            raise GithubIssueCollectionError("GitHub issue config must be one object")
        state_path = Path(args.state)
        previous_state = _read_json(str(state_path)) if state_path.exists() else None
        frontier_path = Path(args.frontier)
        frontier = _read_json(str(frontier_path)) if frontier_path.exists() else None
        if args.topic:
            if frontier is None:
                raise GithubIssueCollectionError(
                    "--topic requires an existing query frontier"
                )
            missing = sorted(set(args.topic) - frontier_topic_ids(frontier))
            if missing:
                raise GithubIssueCollectionError(
                    "unknown frontier topic_id: " + ", ".join(missing)
                )
        dynamic_queries = frontier_queries(
            frontier, ["github_issue"], topic_ids=args.topic
        )
        plan = build_github_issue_plan(
            config,
            previous_state=previous_state,
            frontier_queries=dynamic_queries,
            frontier_only=bool(args.topic),
            max_tasks_per_run=args.max_tasks_per_run,
            repositories_per_task=args.repositories_per_task,
            max_pages_per_task=args.max_pages_per_task,
            per_page=args.per_page,
        )
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(
            json.dumps(plan, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    except (OSError, json.JSONDecodeError, GithubIssueCollectionError, SocialDiscoveryError) as exc:
        print(f"GitHub issue plan failed: {exc}", file=sys.stderr)
        return 2
    print(json.dumps({
        "run_id": plan["run_id"],
        "path": str(output_path),
        "repositories": plan["coverage"]["repositories"],
        "queries": plan["coverage"]["queries"],
        "eligible_tasks": plan["coverage"]["eligible_tasks"],
        "selected_tasks": plan["coverage"]["selected_tasks"],
        "free_api": True,
    }, ensure_ascii=False, indent=2))
    return 0


def command_github_issue_collect(args: argparse.Namespace) -> int:
    """Execute a GitHub Issues plan through documented free REST endpoints."""

    try:
        plan = _read_json(args.plan)
        if not isinstance(plan, Mapping):
            raise GithubIssueCollectionError("GitHub issue plan must be one object")
        state_path = Path(args.state)
        previous_state = _read_json(str(state_path)) if state_path.exists() else None
        client = GithubIssueApiClient.from_environment()
        result, next_state = collect_github_issue_candidates(
            plan,
            client,
            previous_state=previous_state,
            max_issues_per_run=args.max_issues_per_run,
            max_comments_per_issue=args.max_comments_per_issue,
            enrich_comments=not args.no_comments,
            refresh_known=args.refresh_known,
        )
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(
            json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        state_path.parent.mkdir(parents=True, exist_ok=True)
        state_path.write_text(
            json.dumps(next_state, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    except (OSError, json.JSONDecodeError, GithubIssueCollectionError) as exc:
        print(f"GitHub issue collection failed: {exc}", file=sys.stderr)
        return 2
    print(json.dumps({
        "run_id": result["run_id"],
        "path": str(output_path),
        "state": str(state_path),
        "candidates": len(result["candidates"]),
        "requests_made": result["stats"]["requests_made"],
        "request_failures": len(result["request_failures"]),
        "free_api": True,
    }, ensure_ascii=False, indent=2))
    return 3 if result["request_failures"] else 0


def command_github_issue_ingest_connector(args: argparse.Namespace) -> int:
    """Merge connected-app candidate/comment exports deterministically."""

    try:
        candidate_runs = []
        for path in args.input:
            value = _read_json(path)
            if not isinstance(value, Mapping):
                raise GithubIssueCollectionError(f"candidate input is not an object: {path}")
            candidate_runs.append(value)
        comment_runs = []
        for path in args.comments or []:
            value = _read_json(path)
            if not isinstance(value, Mapping):
                raise GithubIssueCollectionError(f"comment input is not an object: {path}")
            comment_runs.append(value)
        result = merge_github_connector_runs(
            candidate_runs, comment_runs=comment_runs
        )
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(
            json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    except (OSError, json.JSONDecodeError, GithubIssueCollectionError) as exc:
        print(f"GitHub connector ingest failed: {exc}", file=sys.stderr)
        return 2
    print(json.dumps({
        "run_id": result["run_id"],
        "path": str(output_path),
        **result["stats"],
    }, ensure_ascii=False, indent=2))
    return 0


def command_social_queue_xiaohongshu(args: argparse.Namespace) -> int:
    """Build/update a no-network Xiaohongshu manual-review queue."""

    try:
        raw = _read_json(args.config)
        if not isinstance(raw, Mapping):
            raise XiaohongshuQueueError("social query config must be one JSON object")
        queries = _filter_social_queries(
            queries_from_config(raw, platform="xiaohongshu"),
            args.scope,
            args.domain,
        )
        if not queries:
            raise XiaohongshuQueueError("select at least one configured query")
        plan = build_xhs_review_plan(
            queries, max_candidates_per_query=args.max_candidates_per_query
        )
        target = Path(args.output)
        existing = None
        if not args.fresh and target.exists():
            existing = _read_json(str(target))
            if not isinstance(existing, Mapping):
                raise XiaohongshuQueueError("existing queue must be one JSON object")

        candidates = []
        if args.candidates:
            candidate_input = _read_json(args.candidates)
            if isinstance(candidate_input, Mapping):
                candidate_input = candidate_input.get("candidates")
            if not isinstance(candidate_input, list):
                raise XiaohongshuQueueError(
                    "candidate input must be a list or an object with candidates[]"
                )
            candidates = candidate_input
        queue = build_xhs_review_queue(
            plan, candidates, existing_queue=existing
        )

        if args.decisions:
            decision_input = _read_json(args.decisions)
            if isinstance(decision_input, Mapping):
                decision_input = decision_input.get("decisions")
            if not isinstance(decision_input, list):
                raise XiaohongshuQueueError(
                    "decision input must be a list or an object with decisions[]"
                )
            queue = apply_xhs_review_decisions(queue, decision_input)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(
            json.dumps(queue, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    except (
        OSError,
        json.JSONDecodeError,
        ModelError,
        SocialCollectionError,
        XiaohongshuQueueError,
        ValueError,
    ) as exc:
        print(f"Xiaohongshu queue failed: {exc}", file=sys.stderr)
        return 2

    status_counts = {}
    for candidate in queue["candidates"]:
        status = candidate.get("review_status", "unknown")
        status_counts[status] = status_counts.get(status, 0) + 1
    print(json.dumps({
        "run_id": plan["run_id"],
        "path": str(target),
        "tasks": len(plan["tasks"]),
        "added": queue["added"],
        "candidates": len(queue["candidates"]),
        "status_counts": status_counts,
        "network_access": False,
        "browser_dom_extraction": False,
    }, ensure_ascii=False, indent=2))
    return 0


def command_import_social_captures(args: argparse.Namespace) -> int:
    """Normalize, deduplicate, and store reviewed social analysis."""

    try:
        raw = _read_json(args.input)
        if isinstance(raw, Mapping):
            captures = raw.get("captures")
            run_id = raw.get("run_id")
        else:
            captures = raw
            run_id = None
        if not isinstance(captures, list):
            raise SocialCollectionError(
                "social capture input must be a list or an object with captures[]"
            )
        normalized = [normalize_social_capture(item) for item in captures]
        unique, in_run_duplicates = deduplicate_social_sources(normalized)
        repository = _repository(args.data_dir)
        existing_sources = repository.load_sources()
        existing_by_url = {source.canonical_url: source for source in existing_sources}
        existing_by_id = {source.source_id: source for source in existing_sources}

        imported = []
        skipped = []
        for source in unique:
            same_url = existing_by_url.get(source.canonical_url)
            same_id = existing_by_id.get(source.source_id)
            existing = same_url or same_id
            if existing is not None and not args.overwrite:
                skipped.append({
                    "source_id": source.source_id,
                    "reason": "already_exists",
                    "existing_source_id": existing.source_id,
                })
                continue
            if same_url is not None and same_url.source_id != source.source_id:
                skipped.append({
                    "source_id": source.source_id,
                    "reason": "canonical_url_owned_by_other_source",
                    "existing_source_id": same_url.source_id,
                })
                continue
            target = repository.sources_dir / f"{source.source_id}.json"
            if not args.dry_run:
                target = repository.save_source(source, overwrite=existing is not None)
            imported.append({"source_id": source.source_id, "path": str(target)})
    except (
        OSError,
        json.JSONDecodeError,
        ModelError,
        RepositoryError,
        SocialCollectionError,
        ValueError,
    ) as exc:
        print(f"social import failed: {exc}", file=sys.stderr)
        return 2

    report = {
        "run_id": run_id,
        "dry_run": args.dry_run,
        "captures": len(captures),
        "engineering_qa_cards": sum(
            len(source.metadata.get("engineering_qa", [])) for source in unique
        ),
        "imported": imported,
        "skipped": skipped,
        "in_run_duplicates": in_run_duplicates,
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


def command_social_report(args: argparse.Namespace) -> int:
    """Render candidate engineering questions with mandatory original links."""

    try:
        sources = _repository(args.data_dir).load_sources()
        config = _read_json(args.config)
        if not isinstance(config, Mapping) or not isinstance(config.get("scopes"), list):
            raise ValueError("social report config must contain a scopes list")
        markdown = render_engineering_qa_markdown(
            sources, scope_definitions=config["scopes"]
        )
        target = Path(args.output)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(markdown, encoding="utf-8")
        pending_files = 0
        inventory_stats = None
        inventory_path = Path(args.inventory)
        if inventory_path.exists():
            inventory = _read_json(str(inventory_path))
            if not isinstance(inventory, Mapping):
                raise SocialInventoryError("social inventory must be one object")
            pages = render_pending_markdown(
                inventory, scope_definitions=config["scopes"]
            )
            pending_root = Path(args.pending_output)
            pending_root.mkdir(parents=True, exist_ok=True)
            for relative_name, content in pages.items():
                (pending_root / relative_name).write_text(content, encoding="utf-8")
            pending_files = len(pages)
            inventory_stats = inventory.get("stats")
        card_count = sum(
            len(source.metadata.get("engineering_qa", []))
            for source in sources
            if source.kind.value in {"community", "issue"}
            and isinstance(source.metadata.get("engineering_qa", []), list)
        )
    except (
        OSError, json.JSONDecodeError, ModelError, RepositoryError,
        SocialCollectionError, SocialInventoryError, ValueError,
    ) as exc:
        print(f"social report failed: {exc}", file=sys.stderr)
        return 2
    print(json.dumps({
        "path": str(target),
        "engineering_qa_cards": card_count,
        "pending_files": pending_files,
        "inventory": inventory_stats,
    }, ensure_ascii=False, indent=2))
    return 0


def _inventory_candidates(raw: Any, path: str) -> list[Mapping[str, Any]]:
    if isinstance(raw, list):
        values = raw
    elif isinstance(raw, Mapping):
        values = raw.get(
            "candidates", raw.get("pages", raw.get("items", raw.get("decisions")))
        )
    else:
        values = None
    if not isinstance(values, list):
        raise SocialInventoryError(
            f"{path} must be a list or contain candidates/pages/items[]"
        )
    if not all(isinstance(value, Mapping) for value in values):
        raise SocialInventoryError(f"{path} candidate items must be objects")
    return values


def command_social_inventory(args: argparse.Namespace) -> int:
    """Merge every candidate into the minimal triage inventory."""

    try:
        groups = [
            _inventory_candidates(_read_json(path), path) for path in args.input
        ]
        output_path = Path(args.output)
        previous = (
            _read_json(str(output_path))
            if output_path.exists() and not args.fresh else None
        )
        if previous is not None and not isinstance(previous, Mapping):
            raise SocialInventoryError("existing inventory must be one object")
        decisions = []
        if args.decisions:
            decisions = _inventory_candidates(
                _read_json(args.decisions), args.decisions
            )
        sources = _repository(args.data_dir).load_sources()
        inventory = build_social_candidate_inventory(
            groups,
            reviewed_sources=sources,
            previous_inventory=previous,
            decisions=decisions,
        )
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(
            json.dumps(inventory, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    except (
        OSError, json.JSONDecodeError, ModelError, RepositoryError,
        SocialInventoryError, ValueError,
    ) as exc:
        print(f"social inventory failed: {exc}", file=sys.stderr)
        return 2
    print(json.dumps({
        "path": str(output_path),
        **inventory["stats"],
    }, ensure_ascii=False, indent=2))
    return 0


def command_build_index(args: argparse.Namespace) -> int:
    repository = _repository(args.data_dir)
    try:
        counts = build_index(
            Path(args.index), repository.load_sources(), repository.load_claims()
        )
    except (RepositoryError, ModelError, ValueError, OSError, sqlite3.Error) as exc:
        print(f"index build failed: {exc}", file=sys.stderr)
        return 2
    print(json.dumps({"index": args.index, **counts}, ensure_ascii=False, indent=2))
    return 0


def _collect_web_problems(args: argparse.Namespace):
    repository = _repository(args.data_dir)
    return collect_web_problems(
        repository.load_sources(),
        repository.load_claims(),
        repository_url=args.repository_url,
        branch=args.branch,
        translations_dir=Path(args.translations_dir),
    )


def command_render_problems(args: argparse.Namespace) -> int:
    """Render or check every static engineering-problem detail page."""

    try:
        problems = _collect_web_problems(args)
        report = render_problem_pages(
            problems, Path(args.output_dir), check=args.check
        )
    except (
        OSError, ModelError, RepositoryError, ValueError, WebSearchError,
    ) as exc:
        print(f"problem-page render failed: {exc}", file=sys.stderr)
        return 2
    print(json.dumps({"path": args.output_dir, **report}, ensure_ascii=False, indent=2))
    return 0


def command_build_web_index(args: argparse.Namespace) -> int:
    """Build the metadata-free bilingual index used by the static search UI."""

    try:
        problems = _collect_web_problems(args)
        report = build_web_index(
            problems, Path(args.problems_dir), Path(args.output)
        )
    except (
        OSError, ModelError, RepositoryError, ValueError, WebSearchError,
    ) as exc:
        print(f"web index build failed: {exc}", file=sys.stderr)
        return 2
    print(json.dumps({"path": args.output, **report}, ensure_ascii=False, indent=2))
    return 0


def command_query(args: argparse.Namespace) -> int:
    try:
        result = answer(Path(args.index), args.question, limit=args.limit)
    except (OSError, ValueError, sqlite3.Error) as exc:
        print(f"query failed: {exc}", file=sys.stderr)
        return 2
    if args.format == "json":
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(render_markdown(result))
    return 0


def command_papers_status(args: argparse.Namespace) -> int:
    try:
        catalog = load_json(Path(args.catalog))
        registry = load_json(Path(args.registry))
        errors = validate_catalog(catalog, registry)
        report = coverage_report(catalog)
        report["ok"] = not errors
        report["errors"] = errors
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"paper status failed: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(report, ensure_ascii=False, indent=2, default=dict))
    return 0 if report["ok"] else 2


def command_papers_discover(args: argparse.Namespace) -> int:
    try:
        catalog = load_json(Path(args.catalog))
        errors = validate_catalog(catalog)
        if errors:
            raise ValueError("; ".join(errors))
        candidates = discover_candidates(
            catalog,
            max_per_topic=args.max_per_topic,
            topics=args.topic,
        )
        target = write_candidate_run(Path(args.out), candidates)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"paper discovery failed: {exc}", file=sys.stderr)
        return 2
    print(json.dumps({
        "mode": "manual_on_demand",
        "candidates": len(candidates),
        "output": str(target),
        "auto_accepted": False,
    }, ensure_ascii=False, indent=2))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="wbc-handbook")
    subparsers = parser.add_subparsers(dest="command", required=True)

    validate = subparsers.add_parser("validate", help="validate source and claim records")
    validate.add_argument("--data-dir", default="data")
    validate.set_defaults(func=command_validate)

    importer = subparsers.add_parser("import-source", help="normalize one manual source JSON")
    importer.add_argument("input")
    importer.add_argument("--data-dir", default="data")
    importer.add_argument("--overwrite", action="store_true")
    importer.set_defaults(func=command_import_source)

    social_plan = subparsers.add_parser(
        "social-plan",
        help="build a finite Xiaohongshu/Zhihu manual link-review plan",
    )
    social_plan.add_argument("--config", default="config/social-queries.json")
    social_plan.add_argument(
        "--platform", action="append", choices=MANUAL_REVIEW_PLATFORMS,
        help="limit the assisted plan to Xiaohongshu or Zhihu; repeat for both",
    )
    social_plan.add_argument(
        "--scope", action="append",
        help="limit the plan to one engineering scope_id; repeat for multiple scopes",
    )
    social_plan.add_argument(
        "--domain", action="append", choices=[item.value for item in Domain],
        help="limit the plan to one WBC domain; repeat to select multiple domains",
    )
    social_plan.add_argument("--max-results-per-query", type=int)
    social_plan.add_argument("--max-comments-per-post", type=int)
    social_plan.add_argument("--max-tasks-per-batch", type=int)
    social_plan.add_argument("--data-dir", default="data")
    social_plan.add_argument(
        "--refresh-known", action="store_true",
        help="include already imported canonical posts in the review run",
    )
    social_plan.add_argument("--output", default="var/social-collection-plan.json")
    social_plan.set_defaults(func=command_social_plan)

    social_x = subparsers.add_parser(
        "social-collect-x",
        help="collect public X posts through the official X API v2",
    )
    social_x.add_argument("--config", default="config/social-queries.json")
    social_x.add_argument(
        "--scope", action="append",
        help="limit configured searches to one engineering scope_id; repeat as needed",
    )
    social_x.add_argument(
        "--domain", action="append", choices=[item.value for item in Domain],
        help="limit configured searches to domain hints; cross-domain scopes may be omitted",
    )
    social_x.add_argument(
        "--query", action="append",
        help="run one ad-hoc WBC query; repeat for more queries",
    )
    social_x.add_argument(
        "--post", action="append",
        help="look up one exact X post ID or status URL; repeat for more posts",
    )
    social_x.add_argument(
        "--conversation", action="append",
        help=(
            "look up a root post and search its conversation_id replies; recent "
            "mode covers only the recent window, while --mode all needs entitlement"
        ),
    )
    social_x.add_argument(
        "--include-config-queries", action="store_true",
        help="also run configured queries when --query/--post/--conversation is used",
    )
    social_x.add_argument("--mode", choices=("recent", "all"), default="recent")
    social_x.add_argument("--max-posts-per-query", type=int, default=10)
    social_x.add_argument("--max-pages", type=int, default=1)
    social_x.add_argument("--start-time")
    social_x.add_argument("--end-time")
    social_x.add_argument(
        "--sort-order", choices=("recency", "relevancy"), default="recency"
    )
    social_x.add_argument("--token-env", default="X_BEARER_TOKEN")
    social_x.add_argument("--max-retries", type=int, default=3)
    social_x.add_argument("--max-retry-wait-seconds", type=float, default=30.0)
    social_x.add_argument("--state", default="var/social-state/x.json")
    social_x.add_argument(
        "--no-state", action="store_true",
        help="do not read or write incremental since_id state",
    )
    social_x.add_argument(
        "--dry-run", action="store_true",
        help="write the request/cost plan without network access or credentials",
    )
    social_x.add_argument("--output", default="var/social-candidates/x.json")
    social_x.set_defaults(func=command_social_collect_x)

    social_zhihu = subparsers.add_parser(
        "social-collect-zhihu",
        help="discover Zhihu candidates through the official invited-preview API",
    )
    social_zhihu.add_argument("--config", default="config/social-queries.json")
    social_zhihu.add_argument("--scope", action="append")
    social_zhihu.add_argument(
        "--domain", action="append", choices=[item.value for item in Domain]
    )
    social_zhihu.add_argument("--query", action="append")
    social_zhihu.add_argument(
        "--include-config-queries", action="store_true",
        help="also run configured queries when an ad-hoc --query is used",
    )
    social_zhihu.add_argument("--count", type=int, default=10)
    social_zhihu.add_argument("--secret-env", default="ZHIHU_ACCESS_SECRET")
    social_zhihu.add_argument("--state", default="var/social-state/zhihu.json")
    social_zhihu.add_argument("--no-state", action="store_true")
    social_zhihu.add_argument(
        "--refresh-known", action="store_true",
        help="include candidates already seen in prior on-demand runs",
    )
    social_zhihu.add_argument(
        "--dry-run", action="store_true",
        help="write the API plan without network access or credentials",
    )
    social_zhihu.add_argument("--output", default="var/social-candidates/zhihu.json")
    social_zhihu.set_defaults(func=command_social_collect_zhihu)

    social_browser_plan = subparsers.add_parser(
        "social-browser-plan",
        help="build finite Xiaohongshu/Zhihu/X tasks for a signed-in visible browser",
    )
    social_browser_plan.add_argument("--config", default="config/social-queries.json")
    social_browser_plan.add_argument(
        "--platform", action="append", choices=BROWSER_PLATFORMS,
        help="limit the plan to Xiaohongshu, Zhihu, or X; repeat as needed",
    )
    social_browser_plan.add_argument("--scope", action="append")
    social_browser_plan.add_argument(
        "--domain", action="append", choices=[item.value for item in Domain]
    )
    social_browser_plan.add_argument("--query", action="append")
    social_browser_plan.add_argument(
        "--topic", action="append",
        help="run one stable topic_id from the complete frontier; repeat as needed",
    )
    social_browser_plan.add_argument(
        "--post", action="append",
        help="open one exact X status URL and collect bounded visible replies",
    )
    social_browser_plan.add_argument(
        "--include-config-queries", action="store_true",
        help="also include configured searches with an ad-hoc --query, --topic, or --post",
    )
    social_browser_plan.add_argument("--max-results-per-query", type=int, default=3)
    social_browser_plan.add_argument("--max-comments-per-post", type=int, default=200)
    social_browser_plan.add_argument("--max-reply-expansions", type=int, default=100)
    social_browser_plan.add_argument("--reply-depth-limit", type=int, default=10)
    social_browser_plan.add_argument("--post-time-budget-seconds", type=int, default=300)
    social_browser_plan.add_argument("--reply-no-growth-patience", type=int, default=3)
    social_browser_plan.add_argument("--max-posts-per-run", type=int, default=15)
    social_browser_plan.add_argument("--data-dir", default="data")
    social_browser_plan.add_argument("--refresh-known", action="store_true")
    social_browser_plan.add_argument(
        "--state", default="var/social-state/discovery.json",
        help="persistent query-yield and canonical-URL ledger",
    )
    social_browser_plan.add_argument(
        "--frontier", default="var/social-state/query-frontier.json",
        help="evidence-linked technical topics discovered from prior posts/comments",
    )
    social_browser_plan.add_argument(
        "--max-queries-per-platform", type=int, default=8,
        help="round-robin query budget per platform for this on-demand run",
    )
    social_browser_plan.add_argument(
        "--min-query-repeat-hours", type=int, default=24,
        help="base cooldown; repeated zero-yield queries back off exponentially",
    )
    social_browser_plan.add_argument(
        "--refresh-queries", action="store_true",
        help="explicitly override the query cooldown for this run",
    )
    social_browser_plan.add_argument(
        "--output", default="var/social-browser/plan.json"
    )
    social_browser_plan.set_defaults(func=command_social_browser_plan)

    social_browser_ingest = subparsers.add_parser(
        "social-browser-ingest",
        help="normalize pages extracted by a visible-browser collection run",
    )
    social_browser_ingest.add_argument("input")
    social_browser_ingest.add_argument(
        "--output", default="var/social-browser/candidates.json"
    )
    social_browser_ingest.add_argument(
        "--plan", default="var/social-browser/plan.json",
        help="plan used for per-query yield accounting",
    )
    social_browser_ingest.add_argument(
        "--config", default="config/social-queries.json"
    )
    social_browser_ingest.add_argument(
        "--state", default="var/social-state/discovery.json"
    )
    social_browser_ingest.add_argument(
        "--frontier", default="var/social-state/query-frontier.json"
    )
    social_browser_ingest.add_argument("--min-query-repeat-hours", type=int, default=24)
    social_browser_ingest.add_argument("--no-state", action="store_true")
    social_browser_ingest.add_argument("--no-evolve", action="store_true")
    social_browser_ingest.set_defaults(func=command_social_browser_ingest)

    social_evolve = subparsers.add_parser(
        "social-evolve-queries",
        help="mine evidence-linked WBC subtopics from post bodies and comments",
    )
    social_evolve.add_argument("input", nargs="+")
    social_evolve.add_argument("--config", default="config/social-queries.json")
    social_evolve.add_argument(
        "--output", default="var/social-state/query-frontier.json"
    )
    social_evolve.set_defaults(func=command_social_evolve_queries)

    social_frontier_report = subparsers.add_parser(
        "social-frontier-report",
        help="render the complete WBC social-query frontier without display caps",
    )
    social_frontier_report.add_argument(
        "--frontier", default="var/social-state/query-frontier.json"
    )
    social_frontier_report.add_argument(
        "--state", default="var/social-state/discovery.json"
    )
    social_frontier_report.add_argument(
        "--output", default="content/social-query-frontier.md"
    )
    social_frontier_report.set_defaults(func=command_social_frontier_report)

    github_plan = subparsers.add_parser(
        "github-issue-plan",
        help="build a large, resumable WBC GitHub Issues search plan",
    )
    github_plan.add_argument("--config", default="config/github-issue-search.json")
    github_plan.add_argument("--state", default="var/social-state/github-issues.json")
    github_plan.add_argument(
        "--frontier", default="var/social-state/query-frontier.json"
    )
    github_plan.add_argument(
        "--topic", action="append",
        help="run one stable topic_id from the complete frontier; repeat as needed",
    )
    github_plan.add_argument("--max-tasks-per-run", type=int, default=40)
    github_plan.add_argument("--repositories-per-task", type=int, default=5)
    github_plan.add_argument("--max-pages-per-task", type=int, default=10)
    github_plan.add_argument("--per-page", type=int, default=100)
    github_plan.add_argument(
        "--output", default="var/github-issues/plan.json"
    )
    github_plan.set_defaults(func=command_github_issue_plan)

    github_collect = subparsers.add_parser(
        "github-issue-collect",
        help="collect GitHub Issue bodies/comments via the documented free REST API",
    )
    github_collect.add_argument("--plan", default="var/github-issues/plan.json")
    github_collect.add_argument("--state", default="var/social-state/github-issues.json")
    github_collect.add_argument("--max-issues-per-run", type=int, default=1000)
    github_collect.add_argument("--max-comments-per-issue", type=int, default=100)
    github_collect.add_argument("--no-comments", action="store_true")
    github_collect.add_argument("--refresh-known", action="store_true")
    github_collect.add_argument(
        "--output", default="var/github-issues/candidates.json"
    )
    github_collect.set_defaults(func=command_github_issue_collect)

    github_connector = subparsers.add_parser(
        "github-issue-ingest-connector",
        help="merge GitHub connected-app search and comment exports by original URL",
    )
    github_connector.add_argument("input", nargs="+")
    github_connector.add_argument("--comments", action="append")
    github_connector.add_argument(
        "--output", default="var/github-issues/candidates.json"
    )
    github_connector.set_defaults(func=command_github_issue_ingest_connector)

    social_xhs = subparsers.add_parser(
        "social-queue-xiaohongshu",
        help="build/update a no-network Xiaohongshu manual-review queue",
    )
    social_xhs.add_argument("--config", default="config/social-queries.json")
    social_xhs.add_argument("--scope", action="append")
    social_xhs.add_argument(
        "--domain", action="append", choices=[item.value for item in Domain]
    )
    social_xhs.add_argument("--max-candidates-per-query", type=int, default=5)
    social_xhs.add_argument(
        "--candidates",
        help="JSON list/object of links and search snippets from an allowed source",
    )
    social_xhs.add_argument(
        "--decisions",
        help="JSON list/object of explicit human review decisions",
    )
    social_xhs.add_argument(
        "--fresh", action="store_true",
        help="ignore an existing output queue instead of merging it",
    )
    social_xhs.add_argument(
        "--output", default="var/social-review/xiaohongshu.json"
    )
    social_xhs.set_defaults(func=command_social_queue_xiaohongshu)

    social_import = subparsers.add_parser(
        "import-social-captures",
        help="normalize and deduplicate reviewed social analysis captures",
    )
    social_import.add_argument("input")
    social_import.add_argument("--data-dir", default="data")
    social_import.add_argument("--dry-run", action="store_true")
    social_import.add_argument("--overwrite", action="store_true")
    social_import.set_defaults(func=command_import_social_captures)

    social_report = subparsers.add_parser(
        "social-report",
        help="render engineering Q&A candidates with original post links",
    )
    social_report.add_argument("--data-dir", default="data")
    social_report.add_argument("--output", default="var/social-engineering-qa.md")
    social_report.add_argument(
        "--config", default="config/social-queries.json",
        help="scope catalog used for the coverage matrix",
    )
    social_report.add_argument(
        "--inventory", default="data/social-candidate-index.json",
        help="minimal all-candidate inventory used for the pending appendix",
    )
    social_report.add_argument(
        "--pending-output", default="content/social-engineering-pending",
        help="directory for the complete technical-pending index and scope pages",
    )
    social_report.set_defaults(func=command_social_report)

    social_inventory = subparsers.add_parser(
        "social-inventory",
        help="merge and triage all social/Issue candidates without storing raw bodies",
    )
    social_inventory.add_argument("input", nargs="*")
    social_inventory.add_argument("--data-dir", default="data")
    social_inventory.add_argument(
        "--decisions", help="review decisions list or object with candidates/items[]"
    )
    social_inventory.add_argument(
        "--output", default="data/social-candidate-index.json"
    )
    social_inventory.add_argument(
        "--fresh", action="store_true", help="rebuild instead of merging the prior index"
    )
    social_inventory.set_defaults(func=command_social_inventory)

    render_problems = subparsers.add_parser(
        "render-problems",
        help="render or check every static engineering-problem detail page",
    )
    render_problems.add_argument("--data-dir", default="data")
    render_problems.add_argument("--translations-dir", default=str(DEFAULT_TRANSLATIONS_DIR))
    render_problems.add_argument("--output-dir", default="content/problems")
    render_problems.add_argument(
        "--repository-url", default=DEFAULT_REPOSITORY_URL
    )
    render_problems.add_argument("--branch", default=DEFAULT_BRANCH)
    render_problems.add_argument("--check", action="store_true")
    render_problems.set_defaults(func=command_render_problems)

    web_index = subparsers.add_parser(
        "build-web-index",
        help="build the static Chinese/English engineering-problem search index",
    )
    web_index.add_argument("--data-dir", default="data")
    web_index.add_argument("--translations-dir", default=str(DEFAULT_TRANSLATIONS_DIR))
    web_index.add_argument("--problems-dir", default="content/problems")
    web_index.add_argument("--output", default="site/search-index.json")
    web_index.add_argument("--repository-url", default=DEFAULT_REPOSITORY_URL)
    web_index.add_argument("--branch", default=DEFAULT_BRANCH)
    web_index.set_defaults(func=command_build_web_index)

    builder = subparsers.add_parser("build-index", help="rebuild the local SQLite index")
    builder.add_argument("--data-dir", default="data")
    builder.add_argument("--index", default="var/handbook.sqlite")
    builder.set_defaults(func=command_build_index)

    query = subparsers.add_parser("query", help="query reviewed claims with citations")
    query.add_argument("question")
    query.add_argument("--index", default="var/handbook.sqlite")
    query.add_argument("--limit", type=int, default=5)
    query.add_argument("--format", choices=("markdown", "json"), default="markdown")
    query.set_defaults(func=command_query)

    paper_status = subparsers.add_parser(
        "papers-status", help="report classic/open-source/deep-read coverage"
    )
    paper_status.add_argument("--catalog", default="content/papers/catalog.json")
    paper_status.add_argument("--registry", default="content/papers/registry.json")
    paper_status.set_defaults(func=command_papers_status)

    paper_discover = subparsers.add_parser(
        "papers-discover", help="manually discover unseen arXiv candidates"
    )
    paper_discover.add_argument("--catalog", default="content/papers/catalog.json")
    paper_discover.add_argument(
        "--topic", action="append",
        help="limit discovery to one catalog topic key; repeat for multiple topics",
    )
    paper_discover.add_argument("--max-per-topic", type=int, default=8)
    paper_discover.add_argument("--out", default="var/paper-update/candidates.json")
    paper_discover.set_defaults(func=command_papers_discover)
    return parser


def main(argv=None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)
