"""Quality gates for bilingual, commit-pinned open-source project reviews."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
import re
from typing import List, Mapping


CJK = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff]")
WORD = re.compile(r"\b[A-Za-z][A-Za-z0-9'-]*\b")
COMMIT_URL = re.compile(r"https://github\.com/[^/]+/[^/]+/(?:tree|blob)/[0-9a-f]{40}/")
CODE_LINK = re.compile(r"https://github\.com/[^/]+/[^/]+/blob/[0-9a-f]{40}/[^)\s#]+(?:#[^)\s]+)?")

ZH_SECTIONS = (
    "## 为什么收录",
    "## 它解决什么问题",
    "## 架构与数据流",
    "## 代码定位",
    "## 最小复现路径",
    "## 能力边界",
    "## 工程判断与风险",
    "## 一手来源",
)
EN_SECTIONS = (
    "## Why it is included",
    "## Problem addressed",
    "## Architecture and data flow",
    "## Code map",
    "## Minimal reproduction path",
    "## Capability boundaries",
    "## Engineering assessment and risks",
    "## Primary sources",
)


@dataclass
class ProjectReviewQuality:
    project_id: str
    cjk_chars: int
    english_words: int
    zh_code_links: int
    en_code_links: int
    errors: List[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.errors


def evaluate_project_review(project: Mapping, root: Path) -> ProjectReviewQuality:
    """Evaluate one deep-review project and return deterministic errors."""

    project_id = str(project.get("project_id", "unknown"))
    zh_path = root / str(project.get("detail_path_zh", ""))
    en_path = root / str(project.get("detail_path_en", ""))
    zh = zh_path.read_text(encoding="utf-8") if zh_path.is_file() else ""
    en = en_path.read_text(encoding="utf-8") if en_path.is_file() else ""
    quality = ProjectReviewQuality(
        project_id=project_id,
        cjk_chars=len(CJK.findall(zh)),
        english_words=len(WORD.findall(en)),
        zh_code_links=len(CODE_LINK.findall(zh)),
        en_code_links=len(CODE_LINK.findall(en)),
    )
    if not zh:
        quality.errors.append("missing Chinese project review")
    if not en:
        quality.errors.append("missing English project review")
    if quality.cjk_chars < 900:
        quality.errors.append("Chinese review is below 900 CJK characters")
    if quality.english_words < 600:
        quality.errors.append("English review is below 600 words")
    for section in ZH_SECTIONS:
        if section not in zh:
            quality.errors.append(f"Chinese review missing section: {section}")
    for section in EN_SECTIONS:
        if section not in en:
            quality.errors.append(f"English review missing section: {section}")
    if quality.zh_code_links < 2 or quality.en_code_links < 2:
        quality.errors.append("each language needs at least two commit-pinned code links")
    commit = str(project.get("reviewed_commit", ""))
    for language, text in (("Chinese", zh), ("English", en)):
        if commit and commit not in text:
            quality.errors.append(f"{language} review does not pin reviewed_commit")
        if text and not COMMIT_URL.search(text):
            quality.errors.append(f"{language} review has no commit-pinned repository URL")
    zh_cross = f"[English version](en/{zh_path.name})" if zh_path.name else ""
    en_cross = f"[中文版](../{en_path.name})" if en_path.name else ""
    if zh_cross and zh_cross not in zh:
        quality.errors.append("Chinese review has no exact English cross-link")
    if en_cross and en_cross not in en:
        quality.errors.append("English review has no exact Chinese cross-link")
    for text, language in ((zh, "Chinese"), (en, "English")):
        if "star" not in text.lower():
            quality.errors.append(f"{language} review must state that stars are not confidence")
        if "安全" not in text and language == "Chinese":
            quality.errors.append("Chinese review must state a hardware safety boundary")
        if "safety" not in text.lower() and language == "English":
            quality.errors.append("English review must state a hardware safety boundary")
    return quality


def evaluate_project_catalog_reviews(catalog: Mapping, root: Path) -> List[ProjectReviewQuality]:
    return [
        evaluate_project_review(project, root)
        for project in catalog.get("projects", [])
        if project.get("analysis_status") == "deep_review"
    ]
