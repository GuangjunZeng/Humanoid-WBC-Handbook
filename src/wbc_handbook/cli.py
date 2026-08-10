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
            queries_from_config(raw), args.scope, args.domain
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
            next_state = None
        else:
            previous_state = {}
            state_path = Path(args.state)
            if not args.no_state and state_path.exists():
                previous_state = _read_json(str(state_path))
                if not isinstance(previous_state, Mapping):
                    raise XCollectionError("X state file must be one JSON object")
            client = XApiClient.from_environment(args.token_env)
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
        XCollectionError,
        ValueError,
    ) as exc:
        print(f"X collection failed: {exc}", file=sys.stderr)
        return 2

    print(json.dumps({
        "run_id": result["run_id"],
        "dry_run": args.dry_run,
        "mode": args.mode,
        "path": str(target),
        "queries": len(result["queries"]) if args.dry_run else len(result["query_results"]),
        "candidates": 0 if args.dry_run else len(result["candidates"]),
        "estimated_post_read_upper_bound": result.get(
            "estimated_post_read_upper_bound"
        ),
        "state": None if args.dry_run or args.no_state else str(Path(args.state)),
    }, ensure_ascii=False, indent=2))
    return 0


def command_social_collect_zhihu(args: argparse.Namespace) -> int:
    """Run one bounded discovery pass through Zhihu's official search API."""

    try:
        raw = _read_json(args.config)
        if not isinstance(raw, Mapping):
            raise ZhihuCollectionError("social query config must be one JSON object")
        configured_queries = _filter_social_queries(
            queries_from_config(raw), args.scope, args.domain
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


def command_social_queue_xiaohongshu(args: argparse.Namespace) -> int:
    """Build/update a no-network Xiaohongshu manual-review queue."""

    try:
        raw = _read_json(args.config)
        if not isinstance(raw, Mapping):
            raise XiaohongshuQueueError("social query config must be one JSON object")
        queries = _filter_social_queries(
            queries_from_config(raw), args.scope, args.domain
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
        markdown = render_engineering_qa_markdown(sources)
        target = Path(args.output)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(markdown, encoding="utf-8")
        card_count = sum(
            len(source.metadata.get("engineering_qa", []))
            for source in sources
            if source.kind.value == "community"
            and isinstance(source.metadata.get("engineering_qa", []), list)
        )
    except (OSError, ModelError, RepositoryError, ValueError) as exc:
        print(f"social report failed: {exc}", file=sys.stderr)
        return 2
    print(json.dumps({
        "path": str(target),
        "engineering_qa_cards": card_count,
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
        help="look up a root post and search its conversation_id reply thread",
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
    social_x.add_argument("--token-env", default="X_BEARER_TOKEN")
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
    social_report.set_defaults(func=command_social_report)

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
