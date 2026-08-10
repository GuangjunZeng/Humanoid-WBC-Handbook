#!/usr/bin/env python3
"""Render audited key-figure pages from pinned paper PDFs."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SPEC = ROOT / "research" / "key-figures.json"


def find_pdftoppm(explicit: str = "") -> str:
    if explicit:
        return explicit
    found = shutil.which("pdftoppm")
    if found:
        return found
    candidates = [
        Path.home() / ".cache/codex-runtimes/codex-primary-runtime/dependencies/native/poppler/bin/pdftoppm",
        Path.home() / ".cache/codex-runtimes/codex-primary-runtime/dependencies/native/poppler/poppler/bin/pdftoppm",
    ]
    for candidate in candidates:
        if candidate.is_file():
            return str(candidate)
    raise RuntimeError("pdftoppm not found; install Poppler or pass --pdftoppm")


def digest(path: Path) -> str:
    hasher = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def render_one(pdftoppm: str, pdf: Path, page: int, target: Path, dpi: int) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="wbc-figure-") as tmp:
        prefix = Path(tmp) / "render"
        subprocess.run([
            pdftoppm, "-f", str(page), "-l", str(page), "-singlefile",
            "-jpeg", "-r", str(dpi), "-jpegopt", "quality=88,progressive=y",
            str(pdf), str(prefix),
        ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
        rendered = prefix.with_suffix(".jpg")
        if not rendered.is_file():
            raise RuntimeError(f"render did not create {rendered}")
        shutil.copyfile(rendered, target)


def build_paper(pdftoppm: str, paper: dict, dpi: int, force: bool) -> dict:
    pdf = ROOT / paper["pdf"]
    if not pdf.is_file():
        raise FileNotFoundError(f"missing pinned PDF: {pdf}")
    asset_dir = ROOT / "content" / "papers" / "assets" / paper["slug"]
    asset_dir.mkdir(parents=True, exist_ok=True)
    entries = []
    for figure in paper["figures"]:
        target = asset_dir / figure["file"]
        if force or not target.is_file():
            render_one(pdftoppm, pdf, int(figure["page"]), target, dpi)
        entries.append({
            "asset": figure["file"],
            "source_url": paper["source_url"],
            "pdf_page": int(figure["page"]),
            "source_locator": figure["locator"],
            "caption_zh": figure["caption_zh"],
            "sha256": digest(target),
        })
    manifest = {
        "schema_version": 1,
        "paper_id": paper["paper_id"],
        "source_pdf": paper["source_url"],
        "render_method": f"pdftoppm JPEG at {dpi} DPI; full pinned PDF page retained for context",
        "copyright": "Third-party paper figures remain under their original copyright; reproduced for commentary and technical analysis.",
        "figures": entries,
    }
    (asset_dir / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    return {"slug": paper["slug"], "figures": len(entries)}


def check_paper(paper: dict) -> list[str]:
    errors = []
    asset_dir = ROOT / "content" / "papers" / "assets" / paper["slug"]
    manifest_path = asset_dir / "manifest.json"
    if not manifest_path.is_file():
        return [f"{paper['slug']}: missing manifest.json"]
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if manifest.get("paper_id") != paper["paper_id"]:
        errors.append(f"{paper['slug']}: manifest paper_id mismatch")
    entries = manifest.get("figures", [])
    if len(entries) < 3:
        errors.append(f"{paper['slug']}: fewer than three figures")
    for entry in entries:
        target = asset_dir / entry.get("asset", "")
        if not target.is_file():
            errors.append(f"{paper['slug']}: missing {entry.get('asset')}")
        elif digest(target) != entry.get("sha256"):
            errors.append(f"{paper['slug']}: checksum mismatch {entry.get('asset')}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--spec", default=str(DEFAULT_SPEC))
    parser.add_argument("--paper", action="append", default=[], help="slug; repeatable")
    parser.add_argument("--dpi", type=int, default=150)
    parser.add_argument("--pdftoppm", default="")
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    spec = json.loads(Path(args.spec).read_text(encoding="utf-8"))
    papers = spec["papers"]
    if args.paper:
        requested = set(args.paper)
        papers = [paper for paper in papers if paper["slug"] in requested]
        missing = requested - {paper["slug"] for paper in papers}
        if missing:
            print(f"unknown slugs: {sorted(missing)}", file=sys.stderr)
            return 2

    if args.check:
        errors = [error for paper in papers for error in check_paper(paper)]
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        if not errors:
            print(f"key figures ok: {len(papers)} papers")
        return 1 if errors else 0

    pdftoppm = find_pdftoppm(args.pdftoppm)
    results = [build_paper(pdftoppm, paper, args.dpi, args.force) for paper in papers]
    print(json.dumps({"papers": results}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
