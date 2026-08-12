#!/usr/bin/env python3
"""Extract and audit semantically grounded figure/table crops from pinned PDFs.

The committed JPEGs are commentary excerpts, not arbitrary PDF-page screenshots.  A
figure spec therefore binds every excerpt to the locked PDF digest, one or more
page-local crops, caption anchors that must fall inside those crops, an explicit
claim boundary, and a visual-review fingerprint.
"""

from __future__ import annotations

import argparse
from datetime import date
import hashlib
import json
from pathlib import Path
import re
import shutil
import struct
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SPEC = ROOT / "research" / "key-figures.json"
WORKFLOW_VERSION = "key-figure-audit-v2"
TARGET_WIDTH = 1600
GUTTER = 28
JPEG_QUALITY = 91


def find_poppler_tool(name: str, explicit: str = "") -> str:
    if explicit:
        return explicit
    found = shutil.which(name)
    if found:
        return found
    candidates = [
        Path.home() / f".cache/codex-runtimes/codex-primary-runtime/dependencies/native/poppler/bin/{name}",
        Path.home() / f".cache/codex-runtimes/codex-primary-runtime/dependencies/native/poppler/poppler/bin/{name}",
    ]
    for candidate in candidates:
        if candidate.is_file():
            return str(candidate)
    raise RuntimeError(f"{name} not found; install Poppler or pass its explicit path")


def digest(path: Path) -> str:
    hasher = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def object_digest(value: object) -> str:
    payload = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def compact_text(value: str) -> str:
    return "".join(character for character in value.casefold() if character.isalnum())


def canonical_region(region: dict) -> dict:
    return {
        "pdf_page": int(region["pdf_page"]),
        "crop": [round(float(value), 6) for value in region["crop"]],
        "caption_anchor": region["caption_anchor"],
    }


def canonical_figure(paper: dict, figure: dict) -> dict:
    return {
        "workflow_version": WORKFLOW_VERSION,
        "paper_id": paper["paper_id"],
        "source_url": paper["source_url"],
        "source_pdf_sha256": paper["source_pdf_sha256"],
        "file": figure["file"],
        "locator": figure["locator"],
        "caption_zh": figure["caption_zh"],
        "selection_reason_zh": figure["selection_reason_zh"],
        "supports_zh": figure["supports_zh"],
        "limits_zh": figure["limits_zh"],
        "regions": [canonical_region(region) for region in figure["regions"]],
    }


def review_fingerprint(paper: dict, figure: dict) -> str:
    return object_digest(canonical_figure(paper, figure))


def validate_crop(crop: object, label: str) -> list[float]:
    if not isinstance(crop, list) or len(crop) != 4:
        raise ValueError(f"{label}: crop must be [left, top, right, bottom]")
    values = [float(value) for value in crop]
    left, top, right, bottom = values
    if not (0 <= left < right <= 1 and 0 <= top < bottom <= 1):
        raise ValueError(f"{label}: crop coordinates must be normalized and ordered")
    if (right - left) * (bottom - top) > 0.62:
        raise ValueError(f"{label}: crop retains too much of the PDF page")
    if right - left < 0.18 or bottom - top < 0.08:
        raise ValueError(f"{label}: crop is too small to remain legible")
    return values


def _bbox_words(pdftotext: str, pdf: Path, page: int) -> tuple[float, float, list[dict]]:
    completed = subprocess.run(
        [pdftotext, "-f", str(page), "-l", str(page), "-bbox-layout", str(pdf), "-"],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    try:
        root = ET.fromstring(completed.stdout)
    except ET.ParseError:
        # A few author PDFs contain malformed metadata/control characters that
        # Poppler reproduces in XHTML.  lxml's recovery parser preserves the
        # word boxes while discarding only the malformed byte sequence.
        try:
            from lxml import etree
        except ImportError as error:  # pragma: no cover - authoring dependency
            raise RuntimeError(
                f"{pdf}: malformed Poppler bbox XHTML; install lxml for recovery"
            ) from error
        root = etree.fromstring(
            completed.stdout.encode("utf-8", errors="replace"),
            parser=etree.XMLParser(recover=True),
        )
    page_node = next((node for node in root.iter() if node.tag.endswith("page")), None)
    if page_node is None:
        raise RuntimeError(f"{pdf}: pdftotext returned no page {page}")
    width = float(page_node.attrib["width"])
    height = float(page_node.attrib["height"])
    words = []
    for block_index, block in enumerate(
        node for node in page_node.iter() if node.tag.endswith("block")
    ):
        block_box = [
            float(block.attrib["xMin"]) / width,
            float(block.attrib["yMin"]) / height,
            float(block.attrib["xMax"]) / width,
            float(block.attrib["yMax"]) / height,
        ]
        for node in block.iter():
            if not node.tag.endswith("word"):
                continue
            text = "".join(node.itertext()).strip()
            normalized = compact_text(text)
            if not normalized:
                continue
            words.append({
                "text": text,
                "normalized": normalized,
                "x0": float(node.attrib["xMin"]),
                "y0": float(node.attrib["yMin"]),
                "x1": float(node.attrib["xMax"]),
                "y1": float(node.attrib["yMax"]),
                "block_index": block_index,
                "block_bbox": block_box,
            })
    return width, height, words


def locate_caption_anchor(
    pdftotext: str,
    pdf: Path,
    page: int,
    crop: list[float],
    anchor: str,
) -> tuple[list[float], list[float], str]:
    needle = compact_text(anchor)
    if len(needle) < 5:
        raise ValueError(f"{pdf}: page {page}: caption_anchor is too weak: {anchor!r}")
    width, height, words = _bbox_words(pdftotext, pdf, page)
    identifier = re.match(r"(?i)\s*((?:fig(?:ure)?\.?|table)\s*[0-9IVX]+[A-Za-z]?)", anchor)
    needles = [needle]
    if identifier:
        short = compact_text(identifier.group(1))
        if short != needle:
            needles.append(short)
    matches = []
    for candidate in needles:
        candidate_matches = []
        for start in range(len(words)):
            combined = ""
            for end in range(start, min(len(words), start + 24)):
                combined += words[end]["normalized"]
                if combined.startswith(candidate):
                    selection = words[start:end + 1]
                    box = [
                        min(word["x0"] for word in selection) / width,
                        min(word["y0"] for word in selection) / height,
                        max(word["x1"] for word in selection) / width,
                        max(word["y1"] for word in selection) / height,
                    ]
                    candidate_matches.append((box, words[start]["block_bbox"]))
                    break
                if not candidate.startswith(combined):
                    break
        if candidate_matches:
            matches = candidate_matches
            break
    if not matches:
        raise ValueError(f"{pdf}: page {page}: caption anchor not found: {anchor!r}")

    left, top, right, bottom = crop
    inside = [
        (box, block_box) for box, block_box in matches
        if box[0] >= left - 0.004 and box[1] >= top - 0.004
        and box[2] <= right + 0.004 and box[3] <= bottom + 0.004
    ]
    if not inside:
        raise ValueError(
            f"{pdf}: page {page}: anchor {anchor!r} exists but falls outside crop {crop}"
        )
    anchor_box, caption_block_box = inside[0]
    if not (
        caption_block_box[0] >= left - 0.004
        and caption_block_box[1] >= top - 0.004
        and caption_block_box[2] <= right + 0.004
        and caption_block_box[3] <= bottom + 0.004
    ):
        raise ValueError(
            f"{pdf}: page {page}: full caption block for {anchor!r} falls outside "
            f"crop {crop}; caption block is {[round(value, 6) for value in caption_block_box]}"
        )
    page_text_hash = hashlib.sha256(
        " ".join(word["normalized"] for word in words).encode("utf-8")
    ).hexdigest()
    return (
        [round(value, 6) for value in anchor_box],
        [round(value, 6) for value in caption_block_box],
        page_text_hash,
    )


def render_page(pdftoppm: str, pdf: Path, page: int, dpi: int, target: Path) -> None:
    prefix = target.with_suffix("")
    subprocess.run(
        [
            pdftoppm,
            "-f", str(page),
            "-l", str(page),
            "-singlefile",
            "-png",
            "-r", str(dpi),
            str(pdf),
            str(prefix),
        ],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.PIPE,
    )
    if not target.is_file():
        raise RuntimeError(f"render did not create {target}")


def render_excerpt(
    pdftoppm: str,
    pdf: Path,
    regions: list[dict],
    target: Path,
    dpi: int,
) -> tuple[int, int]:
    try:
        from PIL import Image
    except ImportError as error:  # pragma: no cover - depends on authoring environment
        raise RuntimeError("Pillow is required to generate cropped figure assets") from error

    target.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="wbc-figure-") as tmp:
        tmp_dir = Path(tmp)
        rendered_pages = {}
        excerpts = []
        for index, region in enumerate(regions):
            page = int(region["pdf_page"])
            if page not in rendered_pages:
                page_file = tmp_dir / f"page-{page}.png"
                render_page(pdftoppm, pdf, page, dpi, page_file)
                rendered_pages[page] = page_file
            with Image.open(rendered_pages[page]) as source:
                source = source.convert("RGB")
                left, top, right, bottom = validate_crop(
                    region["crop"], f"{pdf.name}: region {index + 1}"
                )
                box = (
                    round(left * source.width),
                    round(top * source.height),
                    round(right * source.width),
                    round(bottom * source.height),
                )
                excerpt = source.crop(box)
                scale = TARGET_WIDTH / excerpt.width
                excerpt = excerpt.resize(
                    (TARGET_WIDTH, max(1, round(excerpt.height * scale))),
                    Image.Resampling.LANCZOS,
                )
                excerpts.append(excerpt)

        height = sum(excerpt.height for excerpt in excerpts) + GUTTER * (len(excerpts) + 1)
        canvas = Image.new("RGB", (TARGET_WIDTH + 2 * GUTTER, height), "white")
        y = GUTTER
        for excerpt in excerpts:
            canvas.paste(excerpt, (GUTTER, y))
            y += excerpt.height + GUTTER
        canvas.save(
            target,
            "JPEG",
            quality=JPEG_QUALITY,
            optimize=True,
            progressive=True,
            subsampling=0,
        )
        return canvas.width, canvas.height


def jpeg_dimensions(path: Path) -> tuple[int, int]:
    with path.open("rb") as handle:
        if handle.read(2) != b"\xff\xd8":
            raise ValueError(f"not a JPEG: {path}")
        while True:
            marker_start = handle.read(1)
            if not marker_start:
                break
            if marker_start != b"\xff":
                continue
            marker = handle.read(1)
            while marker == b"\xff":
                marker = handle.read(1)
            if marker in {bytes([value]) for value in range(0xC0, 0xC4)} | {
                bytes([value]) for value in range(0xC5, 0xC8)
            } | {bytes([value]) for value in range(0xC9, 0xCC)} | {
                bytes([value]) for value in range(0xCD, 0xD0)
            }:
                length = struct.unpack(">H", handle.read(2))[0]
                data = handle.read(length - 2)
                height, width = struct.unpack(">HH", data[1:5])
                return width, height
            if marker in {b"\xd8", b"\xd9"}:
                continue
            length_data = handle.read(2)
            if len(length_data) != 2:
                break
            length = struct.unpack(">H", length_data)[0]
            handle.seek(length - 2, 1)
    raise ValueError(f"JPEG dimensions not found: {path}")


def validate_paper_spec(paper: dict) -> list[str]:
    errors = []
    slug = paper.get("slug", "<missing-slug>")
    source_hash = paper.get("source_pdf_sha256", "")
    if not re.fullmatch(r"[0-9a-f]{64}", source_hash):
        errors.append(f"{slug}: invalid or missing source_pdf_sha256")
    figures = paper.get("figures", [])
    if len(figures) != 3:
        errors.append(f"{slug}: expected exactly three key-figure assets")
    names = [figure.get("file") for figure in figures]
    if len(names) != len(set(names)):
        errors.append(f"{slug}: duplicate figure asset names")
    for figure in figures:
        label = f"{slug}/{figure.get('file', '<missing-file>')}"
        for field in (
            "locator", "caption_zh", "selection_reason_zh", "supports_zh", "limits_zh"
        ):
            minimum = 5 if field == "locator" else 8
            if len(str(figure.get(field, "")).strip()) < minimum:
                errors.append(f"{label}: missing substantive {field}")
        regions = figure.get("regions")
        if not isinstance(regions, list) or not regions:
            errors.append(f"{label}: missing regions")
            continue
        for index, region in enumerate(regions, 1):
            try:
                if int(region.get("pdf_page", 0)) < 1:
                    raise ValueError("pdf_page must be >= 1")
                validate_crop(region.get("crop"), f"{label}: region {index}")
                if len(compact_text(str(region.get("caption_anchor", "")))) < 5:
                    raise ValueError("caption_anchor is too weak")
            except (TypeError, ValueError) as error:
                errors.append(f"{label}: region {index}: {error}")
    return errors


def build_paper(
    pdftoppm: str,
    pdftotext: str,
    paper: dict,
    dpi: int,
    force: bool,
) -> dict:
    spec_errors = validate_paper_spec(paper)
    if spec_errors:
        raise ValueError("\n".join(spec_errors))
    pdf = ROOT / paper["pdf"]
    if not pdf.is_file():
        raise FileNotFoundError(f"missing pinned PDF: {pdf}")
    actual_pdf_digest = digest(pdf)
    if actual_pdf_digest != paper["source_pdf_sha256"]:
        raise ValueError(
            f"{paper['slug']}: pinned PDF checksum mismatch; expected "
            f"{paper['source_pdf_sha256']}, got {actual_pdf_digest}"
        )
    asset_dir = ROOT / "content" / "papers" / "assets" / paper["slug"]
    asset_dir.mkdir(parents=True, exist_ok=True)
    entries = []
    for figure in paper["figures"]:
        target = asset_dir / figure["file"]
        audited_regions = []
        for region in figure["regions"]:
            canonical = canonical_region(region)
            anchor_box, caption_block_box, page_text_hash = locate_caption_anchor(
                pdftotext,
                pdf,
                canonical["pdf_page"],
                canonical["crop"],
                canonical["caption_anchor"],
            )
            audited_regions.append({
                **canonical,
                "caption_anchor_bbox": anchor_box,
                "caption_block_bbox": caption_block_box,
                "page_text_sha256": page_text_hash,
            })
        if force or not target.is_file():
            width, height = render_excerpt(pdftoppm, pdf, figure["regions"], target, dpi)
        else:
            width, height = jpeg_dimensions(target)
        fingerprint = review_fingerprint(paper, figure)
        entries.append({
            "asset": figure["file"],
            "source_url": paper["source_url"],
            "source_locator": figure["locator"],
            "caption_zh": figure["caption_zh"],
            "selection_reason_zh": figure["selection_reason_zh"],
            "supports_zh": figure["supports_zh"],
            "limits_zh": figure["limits_zh"],
            "regions": audited_regions,
            "pixel_width": width,
            "pixel_height": height,
            "sha256": digest(target),
            "review": figure.get("review", {"status": "pending"}),
            "review_fingerprint": fingerprint,
        })
    manifest = {
        "schema_version": 2,
        "workflow_version": WORKFLOW_VERSION,
        "paper_id": paper["paper_id"],
        "source_pdf": paper["source_url"],
        "source_pdf_sha256": actual_pdf_digest,
        "render_method": (
            f"Poppler page render at {dpi} DPI; normalized audited crops; "
            f"Pillow Lanczos composition at {TARGET_WIDTH}px content width"
        ),
        "copyright": (
            "Third-party paper figures remain under their original copyright; "
            "cropped excerpts are reproduced for commentary and technical analysis."
        ),
        "figures": entries,
    }
    (asset_dir / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    return {"slug": paper["slug"], "figures": len(entries)}


def _canonical_manifest_regions(entry: dict) -> list[dict]:
    return [canonical_region(region) for region in entry.get("regions", [])]


def check_paper(paper: dict) -> list[str]:
    errors = validate_paper_spec(paper)
    slug = paper.get("slug", "<missing-slug>")
    asset_dir = ROOT / "content" / "papers" / "assets" / slug
    manifest_path = asset_dir / "manifest.json"
    if not manifest_path.is_file():
        return errors + [f"{slug}: missing manifest.json"]
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if manifest.get("schema_version") != 2:
        errors.append(f"{slug}: manifest schema_version must be 2")
    if manifest.get("workflow_version") != WORKFLOW_VERSION:
        errors.append(f"{slug}: stale workflow_version")
    if manifest.get("paper_id") != paper.get("paper_id"):
        errors.append(f"{slug}: manifest paper_id mismatch")
    if manifest.get("source_pdf") != paper.get("source_url"):
        errors.append(f"{slug}: manifest source URL mismatch")
    if manifest.get("source_pdf_sha256") != paper.get("source_pdf_sha256"):
        errors.append(f"{slug}: manifest source PDF checksum mismatch")

    spec_figures = paper.get("figures", [])
    entries = manifest.get("figures", [])
    if len(entries) != len(spec_figures):
        errors.append(f"{slug}: manifest/spec figure count mismatch")
    by_name = {entry.get("asset"): entry for entry in entries}
    expected_names = {figure.get("file") for figure in spec_figures}
    actual_jpegs = {path.name for path in asset_dir.glob("*.jpg")}
    if actual_jpegs != expected_names:
        errors.append(
            f"{slug}: JPEG inventory mismatch; expected {sorted(expected_names)}, "
            f"found {sorted(actual_jpegs)}"
        )
    for figure in spec_figures:
        name = figure.get("file")
        entry = by_name.get(name)
        if entry is None:
            errors.append(f"{slug}: missing manifest entry for {name}")
            continue
        expected = canonical_figure(paper, figure)
        comparisons = {
            "source_url": entry.get("source_url"),
            "source_locator": entry.get("source_locator"),
            "caption_zh": entry.get("caption_zh"),
            "selection_reason_zh": entry.get("selection_reason_zh"),
            "supports_zh": entry.get("supports_zh"),
            "limits_zh": entry.get("limits_zh"),
            "regions": _canonical_manifest_regions(entry),
        }
        expected_values = {
            "source_url": expected["source_url"],
            "source_locator": expected["locator"],
            "caption_zh": expected["caption_zh"],
            "selection_reason_zh": expected["selection_reason_zh"],
            "supports_zh": expected["supports_zh"],
            "limits_zh": expected["limits_zh"],
            "regions": expected["regions"],
        }
        if comparisons != expected_values:
            errors.append(f"{slug}: stale manifest metadata for {name}")
        target = asset_dir / str(name)
        if not target.is_file():
            errors.append(f"{slug}: missing {name}")
        else:
            if digest(target) != entry.get("sha256"):
                errors.append(f"{slug}: checksum mismatch {name}")
            try:
                dimensions = jpeg_dimensions(target)
                if dimensions != (entry.get("pixel_width"), entry.get("pixel_height")):
                    errors.append(f"{slug}: pixel dimensions mismatch {name}")
                if dimensions[0] < 1200:
                    errors.append(f"{slug}: figure too narrow for readable review {name}")
            except ValueError as error:
                errors.append(f"{slug}: {error}")

        fingerprint = review_fingerprint(paper, figure)
        review = figure.get("review", {})
        if review.get("status") != "approved":
            errors.append(f"{slug}: figure has no approved visual review: {name}")
        if review.get("fingerprint") != fingerprint:
            errors.append(f"{slug}: stale visual-review fingerprint: {name}")
        if entry.get("review_fingerprint") != fingerprint:
            errors.append(f"{slug}: stale manifest review fingerprint: {name}")
        if entry.get("review") != review:
            errors.append(f"{slug}: manifest/spec review mismatch: {name}")
        for region in entry.get("regions", []):
            box = region.get("caption_anchor_bbox")
            caption_block = region.get("caption_block_bbox")
            crop = region.get("crop")
            if not isinstance(box, list) or len(box) != 4:
                errors.append(f"{slug}: missing caption anchor bbox: {name}")
            elif not (
                box[0] >= crop[0] - 0.004 and box[1] >= crop[1] - 0.004
                and box[2] <= crop[2] + 0.004 and box[3] <= crop[3] + 0.004
            ):
                errors.append(f"{slug}: caption anchor outside crop: {name}")
            if not isinstance(caption_block, list) or len(caption_block) != 4:
                errors.append(f"{slug}: missing caption block bbox: {name}")
            elif not (
                caption_block[0] >= crop[0] - 0.004
                and caption_block[1] >= crop[1] - 0.004
                and caption_block[2] <= crop[2] + 0.004
                and caption_block[3] <= crop[3] + 0.004
            ):
                errors.append(f"{slug}: full caption block outside crop: {name}")
            if not re.fullmatch(r"[0-9a-f]{64}", str(region.get("page_text_sha256", ""))):
                errors.append(f"{slug}: missing page text fingerprint: {name}")
    return errors


def write_audit_sheet(papers: list[dict], output: Path) -> None:
    try:
        from PIL import Image, ImageDraw, ImageFont
    except ImportError as error:  # pragma: no cover - depends on authoring environment
        raise RuntimeError("Pillow is required to create the visual audit sheet") from error
    font = ImageFont.load_default(size=20)
    files = [
        (paper["slug"], figure["locator"], ROOT / "content" / "papers" / "assets" / paper["slug"] / figure["file"])
        for paper in papers for figure in paper["figures"]
    ]
    columns = 3
    cell_width, cell_height = 540, 500
    rows = (len(files) + columns - 1) // columns
    sheet = Image.new("RGB", (cell_width * columns, cell_height * rows), "white")
    draw = ImageDraw.Draw(sheet)
    for index, (slug, locator, path) in enumerate(files):
        with Image.open(path) as source:
            source = source.convert("RGB")
            source.thumbnail((cell_width - 30, cell_height - 90))
            x0 = (index % columns) * cell_width
            y0 = (index // columns) * cell_height
            x = x0 + (cell_width - source.width) // 2
            y = y0 + 72 + (cell_height - 82 - source.height) // 2
            sheet.paste(source, (x, y))
        draw.multiline_text(
            (x0 + 12, y0 + 10),
            f"{index + 1:02d} {slug}\n{locator}",
            fill="black",
            font=font,
            spacing=3,
        )
    output.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(output, quality=90, optimize=True)


def record_visual_reviews(spec_path: Path, spec: dict, papers: list[dict], reviewer: str) -> int:
    reviewer = reviewer.strip()
    if len(reviewer) < 3:
        raise ValueError("visual-review recorder requires a meaningful reviewer identifier")
    approved = 0
    selected_slugs = {paper["slug"] for paper in papers}
    for paper in spec["papers"]:
        if paper["slug"] not in selected_slugs:
            continue
        for figure in paper.get("figures", []):
            figure["review"] = {
                "status": "approved",
                "reviewer": reviewer,
                "reviewed_on": date.today().isoformat(),
                "fingerprint": review_fingerprint(paper, figure),
            }
            approved += 1
    spec_path.write_text(
        json.dumps(spec, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    return approved


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--spec", default=str(DEFAULT_SPEC))
    parser.add_argument("--paper", action="append", default=[], help="slug; repeatable")
    parser.add_argument("--dpi", type=int, default=220)
    parser.add_argument("--pdftoppm", default="")
    parser.add_argument("--pdftotext", default="")
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--audit-sheet", default="", help="write a visual contact sheet")
    parser.add_argument(
        "--print-review-fingerprints",
        action="store_true",
        help="print fingerprints that must be copied only after visual review",
    )
    parser.add_argument(
        "--record-visual-review",
        metavar="REVIEWER",
        default="",
        help=(
            "after inspecting the full-resolution audit sheet, record approved "
            "fingerprints; never run this in CI or before human visual review"
        ),
    )
    args = parser.parse_args()

    spec_path = Path(args.spec)
    spec = json.loads(spec_path.read_text(encoding="utf-8"))
    if spec.get("schema_version") != 2:
        print("ERROR: key-figures.json schema_version must be 2", file=sys.stderr)
        return 1
    papers = spec["papers"]
    if args.paper:
        requested = set(args.paper)
        papers = [paper for paper in papers if paper["slug"] in requested]
        missing = requested - {paper["slug"] for paper in papers}
        if missing:
            print(f"unknown slugs: {sorted(missing)}", file=sys.stderr)
            return 2

    if args.print_review_fingerprints:
        payload = {
            paper["slug"]: {
                figure["file"]: review_fingerprint(paper, figure)
                for figure in paper.get("figures", [])
            }
            for paper in papers
        }
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return 0

    if args.record_visual_review:
        if args.check or args.force or args.audit_sheet:
            print(
                "ERROR: --record-visual-review cannot be combined with build/check options",
                file=sys.stderr,
            )
            return 2
        try:
            approved = record_visual_reviews(
                spec_path, spec, papers, args.record_visual_review
            )
        except ValueError as error:
            print(f"ERROR: {error}", file=sys.stderr)
            return 2
        print(f"recorded visual review: {approved} assets by {args.record_visual_review}")
        return 0

    if args.check:
        errors = [error for paper in papers for error in check_paper(paper)]
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        if not errors:
            print(f"key figures ok: {len(papers)} papers / {sum(len(p['figures']) for p in papers)} assets")
        return 1 if errors else 0

    pdftoppm = find_poppler_tool("pdftoppm", args.pdftoppm)
    pdftotext = find_poppler_tool("pdftotext", args.pdftotext)
    results = []
    build_errors = []
    for paper in papers:
        try:
            results.append(build_paper(pdftoppm, pdftotext, paper, args.dpi, args.force))
        except (FileNotFoundError, RuntimeError, ValueError) as error:
            build_errors.append(f"{paper.get('slug', '<missing-slug>')}: {error}")
    if build_errors:
        for error in build_errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    if args.audit_sheet:
        write_audit_sheet(papers, Path(args.audit_sheet))
    print(json.dumps({"papers": results}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
