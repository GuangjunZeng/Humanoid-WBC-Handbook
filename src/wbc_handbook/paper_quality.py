"""Quality gates for Chinese, figure-grounded full-paper interpretations."""

from __future__ import annotations

from dataclasses import dataclass, field
import json
from pathlib import Path
import re
from typing import Iterable, List, Mapping


CJK = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff]")
LATIN = re.compile(r"[A-Za-z]")
ENGLISH_WORD = re.compile(r"\b[A-Za-z][A-Za-z0-9'’.-]*\b")
BILINGUAL = re.compile(
    r"(?:[\u3400-\u4dbf\u4e00-\u9fff]{2,}\s*[\(（][A-Za-z][^\)）\n]{1,80}[\)）])"
    r"|(?:[A-Za-z][A-Za-z0-9 -]{1,50}\s*[\(（][\u3400-\u4dbf\u4e00-\u9fff]{2,}[^\)）\n]{0,30}[\)）])"
)
IMAGE = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")
LOCATOR = re.compile(r"\b(?:Figure|Fig\.|Table|Equation)\s*[A-Za-z0-9IVXivx.-]+")
BANNED = ("综上所述", "值得注意的是", "深入探讨", "至关重要")
SECTION_GROUPS = {
    "problem": ("工程痛点", "问题与背景", "研究问题", "故事的起点"),
    "mechanism": ("方法主线", "核心洞察", "方法详解"),
    "figures": ("关键图解", "关键图表怎么读"),
    "experiment": ("最有说服力的实验", "实验证据"),
    "implementation": ("论文—代码映射", "论文-代码映射", "公开实现状态", "论文—实现状态"),
    "limitations": ("适用边界与局限", "局限与安全边界", "局限与工程判断"),
    "takeaway": ("可执行但有边界的结论", "收束", "工程结论"),
    "reproduction": ("复现与验收清单", "复现清单", "验收清单"),
}


@dataclass
class BriefQuality:
    slug: str
    cjk_chars: int
    chinese_ratio: float
    paragraphs: int
    bilingual_terms: int
    images: int
    locators: int
    errors: List[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.errors

    def to_dict(self) -> dict:
        return {
            "slug": self.slug,
            "ok": self.ok,
            "cjk_chars": self.cjk_chars,
            "chinese_ratio": round(self.chinese_ratio, 3),
            "paragraphs": self.paragraphs,
            "bilingual_terms": self.bilingual_terms,
            "images": self.images,
            "locators": self.locators,
            "errors": self.errors,
        }


@dataclass
class EnglishBriefQuality:
    slug: str
    words: int
    paragraphs: int
    images: int
    locators: int
    errors: List[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.errors

    def to_dict(self) -> dict:
        return {
            "slug": self.slug,
            "language": "en",
            "ok": self.ok,
            "words": self.words,
            "paragraphs": self.paragraphs,
            "images": self.images,
            "locators": self.locators,
            "errors": self.errors,
        }


def _paragraphs(text: str) -> int:
    blocks = re.split(r"\n\s*\n", text)
    return sum(
        bool(block.strip())
        and not block.lstrip().startswith(("#", "|", "```", "![", "- "))
        for block in blocks
    )


def evaluate_brief(
    slug: str,
    text: str,
    asset_root: Path,
    code_status: str,
    minimum_cjk: int = 3000,
) -> BriefQuality:
    cjk_chars = len(CJK.findall(text))
    latin_chars = len(LATIN.findall(text))
    ratio = cjk_chars / max(1, cjk_chars + latin_chars)
    image_paths = IMAGE.findall(text)
    bilingual_terms = len(BILINGUAL.findall(text))
    result = BriefQuality(
        slug=slug,
        cjk_chars=cjk_chars,
        chinese_ratio=ratio,
        paragraphs=_paragraphs(text),
        bilingual_terms=bilingual_terms,
        images=len(image_paths),
        locators=len(LOCATOR.findall(text)),
    )

    if cjk_chars < minimum_cjk:
        result.errors.append(f"Chinese depth below {minimum_cjk} CJK characters")
    if ratio < 0.6:
        result.errors.append("Chinese must be the main language (ratio < 0.60)")
    if result.paragraphs < 15:
        result.errors.append("fewer than 15 prose paragraphs")
    if bilingual_terms < 6:
        result.errors.append("fewer than 6 Chinese-English term pairs")
    if len(image_paths) < 3:
        result.errors.append("fewer than 3 embedded key figures")
    if result.locators < 3:
        result.errors.append("fewer than 3 Figure/Table/Equation locators")
    for group, headings in SECTION_GROUPS.items():
        if not any(f"## {heading}" in text for heading in headings):
            result.errors.append(f"missing required section: {group}")
    if "作者" not in text or "独立" not in text:
        result.errors.append("author-stated and independent limitations must be separated")
    if len(re.findall(r"像|好比|可以把.{0,24}理解为|类比", text)) < 2:
        result.errors.append("fewer than 2 explanatory analogies")
    for phrase in BANNED:
        if phrase in text:
            result.errors.append(f"banned generic phrase: {phrase}")

    manifest_path = asset_root / slug / "manifest.json"
    if not manifest_path.is_file():
        result.errors.append("missing figure manifest")
    else:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        required_assets = {entry.get("asset") for entry in manifest.get("figures", [])}
        referenced = {Path(path).name for path in image_paths}
        missing_refs = required_assets - referenced
        if missing_refs:
            result.errors.append(f"manifest figures not embedded: {sorted(missing_refs)}")
        for asset in required_assets:
            if asset and not (asset_root / slug / asset).is_file():
                result.errors.append(f"missing figure asset: {asset}")

    implementation_text = text[text.find("## 论文"):] if "## 论文" in text else text
    if code_status == "verified_official" and len(re.findall(r"`[^`\n]+`", implementation_text)) < 2:
        result.errors.append("official-code paper needs at least two concrete code symbols")
    if code_status in {"not_public", "unknown", "announced"} and not re.search(
        r"未公开|无法核验|尚未公开|Coming Soon", implementation_text
    ):
        result.errors.append("non-verified code status must be stated explicitly")
    return result


def evaluate_english_brief(
    slug: str,
    text: str,
    asset_root: Path,
    code_status: str,
    minimum_words: int = 900,
) -> EnglishBriefQuality:
    """Check a complete English companion without weakening the evidence gate."""

    image_paths = IMAGE.findall(text)
    result = EnglishBriefQuality(
        slug=slug,
        words=len(ENGLISH_WORD.findall(text)),
        paragraphs=_paragraphs(text),
        images=len(image_paths),
        locators=len(LOCATOR.findall(text)),
    )
    if result.words < minimum_words:
        result.errors.append(f"English depth below {minimum_words} words")
    if result.paragraphs < 15:
        result.errors.append("fewer than 15 English prose paragraphs")
    if result.images < 3:
        result.errors.append("fewer than 3 embedded key figures in English page")
    if result.locators < 3:
        result.errors.append("fewer than 3 Figure/Table/Equation locators in English page")
    required_headings = (
        "Engineering problem",
        "Core insight",
        "Method",
        "How to read the key figures",
        "Strongest experiment",
        "Limitations and safety boundary",
        "Bounded engineering takeaway",
        "Reproduction and acceptance checklist",
    )
    headings = re.findall(r"^##\s+(.+)$", text, flags=re.M)
    lower_text = text.lower()
    for required in required_headings:
        if not any(heading.startswith(required) for heading in headings):
            result.errors.append(f"missing English required section: {required}")
    if f"[中文版](../{slug}.md)" not in text:
        result.errors.append("missing exact Chinese companion link")
    if "author-stated" not in lower_text and "authors explicitly" not in lower_text:
        result.errors.append("author-stated limitations are not identified")
    if "independent" not in lower_text:
        result.errors.append("independent engineering limitations are not identified")

    manifest_path = asset_root / slug / "manifest.json"
    if not manifest_path.is_file():
        result.errors.append("missing figure manifest")
    else:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        required_assets = {entry.get("asset") for entry in manifest.get("figures", [])}
        referenced = {Path(path).name for path in image_paths}
        missing_refs = required_assets - referenced
        if missing_refs:
            result.errors.append(
                f"manifest figures not embedded in English page: {sorted(missing_refs)}"
            )
        for asset in required_assets:
            if asset and not (asset_root / slug / asset).is_file():
                result.errors.append(f"missing figure asset: {asset}")

    mapping_start = max(text.find("## Paper-to-code mapping"), text.find("## Paper-to-implementation status"))
    mapping_text = text[mapping_start:] if mapping_start >= 0 else text
    if code_status == "verified_official" and len(re.findall(r"`[^`\n]+`", mapping_text)) < 2:
        result.errors.append("official-code English page needs at least two code symbols")
    if code_status in {"not_public", "unknown", "announced"} and not re.search(
        r"no (?:unique |uniquely )?(?:auditable |verifiable )?official code|"
        r"no uniquely verifiable official code|Coming Soon|no public code",
        mapping_text,
        flags=re.I,
    ):
        result.errors.append("non-verified code status must be explicit in English page")
    return result


def evaluate_registry(root: Path, catalog: Mapping, registry: Mapping) -> List[BriefQuality]:
    by_id = {paper["paper_id"]: paper for paper in catalog.get("papers", [])}
    results = []
    for paper in registry.get("papers", []):
        path = root / paper["brief_path"]
        catalog_entry = by_id[paper["paper_id"]]
        results.append(evaluate_brief(
            paper["slug"],
            path.read_text(encoding="utf-8"),
            root / "content" / "papers" / "assets",
            catalog_entry.get("code", {}).get("status", "unknown"),
        ))
    return results


def evaluate_registry_english(
    root: Path, catalog: Mapping, registry: Mapping
) -> List[EnglishBriefQuality]:
    by_id = {paper["paper_id"]: paper for paper in catalog.get("papers", [])}
    results = []
    for paper in registry.get("papers", []):
        path_value = paper.get("brief_path_en")
        if not path_value:
            results.append(EnglishBriefQuality(
                slug=paper.get("slug", "unknown"),
                words=0,
                paragraphs=0,
                images=0,
                locators=0,
                errors=["registry entry is missing brief_path_en"],
            ))
            continue
        path = root / path_value
        if not path.is_file():
            results.append(EnglishBriefQuality(
                slug=paper.get("slug", "unknown"),
                words=0,
                paragraphs=0,
                images=0,
                locators=0,
                errors=[f"missing English brief: {path_value}"],
            ))
            continue
        catalog_entry = by_id[paper["paper_id"]]
        results.append(evaluate_english_brief(
            paper["slug"],
            path.read_text(encoding="utf-8"),
            root / "content" / "papers" / "assets",
            catalog_entry.get("code", {}).get("status", "unknown"),
        ))
    return results
