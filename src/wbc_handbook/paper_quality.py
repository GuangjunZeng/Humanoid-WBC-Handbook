"""Quality gates for Chinese, figure-grounded full-paper interpretations."""

from __future__ import annotations

from dataclasses import dataclass, field
import json
from pathlib import Path
import re
from typing import Iterable, List, Mapping


CJK = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff]")
LATIN = re.compile(r"[A-Za-z]")
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
