#!/usr/bin/env python3
"""Render per-topic paper tables from the canonical coverage catalog."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "content" / "papers" / "catalog.json"
DOMAIN_ROOT = ROOT / "content" / "papers" / "domains"
BEGIN = "<!-- BEGIN GENERATED PAPER CATALOG -->"
END = "<!-- END GENERATED PAPER CATALOG -->"

DOMAIN_FILES = {
    "training_data_retargeting": "training-data-retargeting.md",
    "universal_tracking_teleoperation": "universal-tracking-teleoperation.md",
    "locomotion_terrain": "locomotion-terrain.md",
    "loco_manipulation_wbc": "loco-manipulation-wbc.md",
    "sports": "sports-athletic-skills.md",
    "motion_generation": "motion-generation.md",
    "recovery_safety_force": "recovery-safety-force.md",
}

ROLE_ZH = {
    "classical_control": "经典控制（classical control）",
    "field_anchor": "领域锚点（field anchor）",
    "hardware_evidence": "实机证据（hardware evidence）",
    "latent_skill": "潜技能（latent skill）",
    "learning": "学习控制（learning）",
    "learning_anchor": "学习基线（learning anchor）",
    "multi_mode": "多模式（multi-mode）",
    "open_source": "开源实现（open source）",
    "optimization": "优化控制（optimization）",
    "protective_fall": "保护性跌倒（protective fall）",
    "recovery": "恢复（recovery）",
    "robot_data_quality": "机器人数据质量（robot data quality）",
    "robot_deployment": "机器人部署（robot deployment）",
    "sim_to_real": "仿真到现实（sim-to-real）",
    "sparse_command": "稀疏命令（sparse command）",
    "task_interaction": "任务交互（task interaction）",
    "terrain": "地形（terrain）",
}


def _paper_link(paper: dict) -> str:
    title = str(paper["title"]).replace("|", "\\|")
    if paper.get("analysis_status") == "deep_read":
        brief = Path(paper["brief_path"]).name
        return f"[{title}](../{brief})"
    return f"[{title}]({paper['paper_url']})"


def _code_link(paper: dict) -> str:
    code = paper.get("code", {})
    status = code.get("status")
    url = code.get("url")
    if status == "verified_official" and url:
        return f"[官方代码]({url})"
    if status == "announced" and url:
        return f"[公开计划，待核验]({url})"
    if status == "not_public":
        return "未发现官方公开代码"
    return "待核验"


def _generated_section(domain: str, catalog: dict) -> str:
    config = catalog["domains"][domain]
    papers = [paper for paper in catalog["papers"] if domain in paper.get("topics", [])]
    papers.sort(key=lambda paper: (
        0 if paper.get("analysis_status") == "deep_read" else 1,
        int(paper.get("year", 0)),
        paper.get("title", "").lower(),
    ))
    deep = sum(paper.get("analysis_status") == "deep_read" for paper in papers)
    official = sum(paper.get("code", {}).get("status") == "verified_official" for paper in papers)
    required = "、".join(ROLE_ZH.get(role, role) for role in config.get("required_roles", []))
    lines = [
        BEGIN,
        "## 扩展论文目录",
        "",
        "下表由 [`catalog.json`](../catalog.json) 生成。“深度解读”已通过中文全文分析与关键图质量门；“待深读”已经过主记录、去重、经典性/开源性与板块缺口审查，但不冒充完整解读。",
        "",
        f"- 当前收录：{len(papers)} 篇，其中深度解读 {deep} 篇，有可核验官方代码 {official} 篇。",
        f"- 必要覆盖角色：{required}。",
        "",
        "| 状态 | 论文 | 年份 | 收录角色 | 代码 | 为什么收录 |",
        "|---|---|---:|---|---|---|",
    ]
    for paper in papers:
        status = "深度解读" if paper.get("analysis_status") == "deep_read" else "待深读"
        roles = "、".join(ROLE_ZH.get(role, role) for role in paper.get("coverage_roles", []))
        why = str(paper.get("why_zh", "")).replace("|", "\\|").replace("\n", " ")
        lines.append(
            f"| {status} | {_paper_link(paper)} | {paper.get('year', '')} | "
            f"{roles} | {_code_link(paper)} | {why} |"
        )
    lines.extend([
        "",
        "更新不在后台定时运行。当用户明确要求更新该板块时，按 [论文库按需更新流程](../../../docs/on-demand-paper-update.md) 执行。",
        END,
        "",
    ])
    return "\n".join(lines)


def render_page(path: Path, domain: str, catalog: dict) -> str:
    current = path.read_text(encoding="utf-8").rstrip() + "\n"
    section = _generated_section(domain, catalog)
    if BEGIN in current:
        prefix, remainder = current.split(BEGIN, 1)
        if END not in remainder:
            raise ValueError(f"{path}: generated section has no end marker")
        _, suffix = remainder.split(END, 1)
        return prefix.rstrip() + "\n\n" + section + suffix.lstrip("\n")
    return current.rstrip() + "\n\n" + section


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--catalog", type=Path, default=CATALOG)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    catalog = json.loads(args.catalog.read_text(encoding="utf-8"))
    stale = []
    for domain, filename in DOMAIN_FILES.items():
        path = DOMAIN_ROOT / filename
        rendered = render_page(path, domain, catalog)
        current = path.read_text(encoding="utf-8")
        if current != rendered:
            stale.append(path)
            if not args.check:
                path.write_text(rendered, encoding="utf-8")
    if stale and args.check:
        for path in stale:
            print(f"stale topic page: {path.relative_to(ROOT)}", file=sys.stderr)
        return 1
    action = "checked" if args.check else "rendered"
    print(f"{action} {len(DOMAIN_FILES)} topic pages")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
