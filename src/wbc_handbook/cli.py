"""Command-line interface for the offline handbook pipeline."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sqlite3
import sys

from .answer import answer, render_markdown
from .importer import normalize_manual_source
from .index import build_index
from .models import ModelError
from .repository import HandbookRepository, RepositoryError
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
    return parser


def main(argv=None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)
