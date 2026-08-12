"""Reviewed English localizations for representative paper deep reads."""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
import json
from pathlib import Path
import re
from typing import Iterable, Mapping


REQUIRED_HEADINGS = (
    "Engineering problem",
    "Method",
    "Key figures",
    "Decisive evidence",
    "Paper-to-implementation mapping",
    "Limits and evidence boundary",
    "Bounded engineering takeaway",
    "Reproduction checklist",
)
URL_PATTERN = re.compile(r"https?://[^)\s]+")


class PaperLocalizationError(ValueError):
    """Raised when a reviewed paper translation is missing or stale."""


@dataclass(frozen=True)
class PaperTranslation:
    paper_id: str
    source_fingerprint: str
    title: str
    content_markdown: str
    path: Path


def source_fingerprint(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def representative_papers(catalog: Mapping) -> list[Mapping]:
    by_id = {paper["paper_id"]: paper for paper in catalog.get("papers", [])}
    ordered: list[Mapping] = []
    seen: set[str] = set()
    for domain in catalog.get("domains", {}).values():
        for route in domain.get("readme_routes", []):
            paper_id = route["paper_id"]
            if paper_id in seen:
                continue
            paper = by_id.get(paper_id)
            if paper is None:
                raise PaperLocalizationError(f"route references unknown paper: {paper_id}")
            if paper.get("analysis_status") != "deep_read" or not paper.get("brief_path"):
                raise PaperLocalizationError(f"route is not a deep read: {paper_id}")
            ordered.append(paper)
            seen.add(paper_id)
    return ordered


def load_translations(root: Path) -> dict[str, PaperTranslation]:
    translations: dict[str, PaperTranslation] = {}
    for path in sorted((root / "data" / "locales" / "en" / "papers").glob("*.json")):
        raw = json.loads(path.read_text(encoding="utf-8"))
        required = {"schema_version", "paper_id", "source_fingerprint", "title", "content_lines"}
        missing = required - set(raw)
        if missing:
            raise PaperLocalizationError(f"{path}: missing fields {sorted(missing)}")
        if raw["schema_version"] != 1:
            raise PaperLocalizationError(f"{path}: unsupported schema_version")
        paper_id = raw["paper_id"]
        if paper_id in translations:
            raise PaperLocalizationError(f"duplicate paper translation: {paper_id}")
        if not isinstance(raw["content_lines"], list) or not all(
            isinstance(line, str) for line in raw["content_lines"]
        ):
            raise PaperLocalizationError(f"{path}: content_lines must be a string list")
        content = "\n".join(raw["content_lines"]).strip()
        for heading in REQUIRED_HEADINGS:
            if f"## {heading}" not in content:
                raise PaperLocalizationError(f"{path}: missing heading: {heading}")
        if len(URL_PATTERN.findall(content)) < 1:
            raise PaperLocalizationError(f"{path}: translation has no evidence URL")
        translations[paper_id] = PaperTranslation(
            paper_id=paper_id,
            source_fingerprint=raw["source_fingerprint"],
            title=raw["title"].strip(),
            content_markdown=content,
            path=path,
        )
    return translations


def _render_one(source_path: Path, translation: PaperTranslation) -> str:
    return (
        f"# {translation.title}\n\n"
        f"[中文版](../{source_path.name})\n\n"
        f"{translation.content_markdown.rstrip()}\n"
    )


def render_paper_translations(root: Path, *, check: bool = False) -> dict:
    catalog = json.loads((root / "content" / "papers" / "catalog.json").read_text(encoding="utf-8"))
    papers = representative_papers(catalog)
    translations = load_translations(root)
    expected_ids = {paper["paper_id"] for paper in papers}
    actual_ids = set(translations)
    missing = sorted(expected_ids - actual_ids)
    orphaned = sorted(actual_ids - expected_ids)
    if missing or orphaned:
        raise PaperLocalizationError(
            f"translation coverage mismatch; missing={missing}, orphaned={orphaned}"
        )

    output_root = root / "content" / "papers" / "en"
    stale: list[str] = []
    for paper in papers:
        source_path = root / paper["brief_path"]
        source = source_path.read_text(encoding="utf-8")
        translation = translations[paper["paper_id"]]
        actual_fingerprint = source_fingerprint(source)
        if translation.source_fingerprint != actual_fingerprint:
            raise PaperLocalizationError(
                f"{translation.path}: stale fingerprint for {paper['paper_id']}; "
                f"expected {actual_fingerprint}"
            )
        expected_switch = f"[English version](en/{source_path.name})"
        if expected_switch not in source:
            raise PaperLocalizationError(f"{source_path}: missing English switch link")

        external_source_urls = set(URL_PATTERN.findall(source))
        external_translation_urls = set(URL_PATTERN.findall(translation.content_markdown))
        invented = sorted(external_translation_urls - external_source_urls)
        if invented:
            raise PaperLocalizationError(
                f"{translation.path}: URLs absent from Chinese evidence page: {invented}"
            )

        target = output_root / source_path.name
        rendered = _render_one(source_path, translation)
        current = target.read_text(encoding="utf-8") if target.exists() else None
        if current != rendered:
            stale.append(str(target.relative_to(root)))
            if not check:
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(rendered, encoding="utf-8")

    unexpected_outputs = sorted(
        path.name for path in output_root.glob("*.md")
        if path.name not in {Path(paper["brief_path"]).name for paper in papers}
    ) if output_root.exists() else []
    if unexpected_outputs:
        raise PaperLocalizationError(f"orphaned English pages: {unexpected_outputs}")
    if check and stale:
        raise PaperLocalizationError(f"stale English paper pages: {stale}")
    return {"papers": len(papers), "written": 0 if check else len(stale), "stale": stale}
