"""Citation-preserving answer rendering."""

from __future__ import annotations

import json
from pathlib import Path
from typing import List

from .index import search


def answer(index_path: Path, question: str, limit: int = 5) -> dict:
    return {"question": question, "claims": search(index_path, question, limit=limit)}


def render_markdown(result: dict) -> str:
    lines: List[str] = [f"# {result['question']}", ""]
    claims = result["claims"]
    if not claims:
        return "\n".join(lines + [
            "No reviewed claim in the local evidence index answers this question.",
            "", "Add or review evidence instead of inferring an unsupported answer.",
        ])
    for index, claim in enumerate(claims, 1):
        lines.extend([
            f"## {index}. {claim['statement']}", "",
            f"- Domain: `{claim['domain']}`",
            f"- Confidence: {claim['confidence']:.2f} — {claim['confidence_rationale']}",
            f"- Safety: `{claim['safety_level']}`",
            "- Applicability: " + json.dumps(claim["applicability"], ensure_ascii=False),
            "- Evidence:",
        ])
        for citation in claim["citations"]:
            lines.append(
                "  - "
                f"[{citation['title']}]({citation['canonical_url']}) — "
                f"{citation['role']}/{citation['strength']}, {citation['locator']}"
            )
        lines.append("")
    lines.extend([
        "> Hardware-critical content remains subject to the complete safety case and human authorization.",
        "",
    ])
    return "\n".join(lines)
