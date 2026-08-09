"""Deterministic SQLite index and dependency-free ranker."""

from __future__ import annotations

import json
from pathlib import Path
import re
import sqlite3
from typing import Dict, Iterable, List

from .models import ClaimStatus, EngineeringClaim, SourceRecord
from .validator import has_errors, validate_repository


SCHEMA = """
CREATE TABLE sources (
  source_id TEXT PRIMARY KEY,
  title TEXT NOT NULL,
  canonical_url TEXT NOT NULL,
  kind TEXT NOT NULL,
  summary TEXT NOT NULL
);
CREATE TABLE claims (
  claim_id TEXT PRIMARY KEY,
  domain TEXT NOT NULL,
  question TEXT NOT NULL,
  statement TEXT NOT NULL,
  confidence REAL NOT NULL,
  confidence_rationale TEXT NOT NULL,
  safety_level TEXT NOT NULL,
  applicability_json TEXT NOT NULL,
  tags_json TEXT NOT NULL,
  search_blob TEXT NOT NULL
);
CREATE TABLE evidence (
  claim_id TEXT NOT NULL,
  source_id TEXT NOT NULL,
  role TEXT NOT NULL,
  strength TEXT NOT NULL,
  locator TEXT NOT NULL,
  note TEXT NOT NULL,
  FOREIGN KEY (claim_id) REFERENCES claims(claim_id),
  FOREIGN KEY (source_id) REFERENCES sources(source_id)
);
"""


def build_index(
    index_path: Path,
    sources: Iterable[SourceRecord],
    claims: Iterable[EngineeringClaim],
) -> Dict[str, int]:
    source_list = list(sources)
    claim_list = list(claims)
    issues = validate_repository(source_list, claim_list)
    if has_errors(issues):
        codes = sorted({issue.code for issue in issues if issue.severity == "error"})
        raise ValueError(f"index build blocked by validation errors: {', '.join(codes)}")

    index_path = Path(index_path)
    index_path.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(str(index_path))
    try:
        connection.executescript("DROP TABLE IF EXISTS evidence; DROP TABLE IF EXISTS claims; DROP TABLE IF EXISTS sources;")
        connection.executescript(SCHEMA)
        for source in source_list:
            connection.execute(
                "INSERT INTO sources VALUES (?, ?, ?, ?, ?)",
                (source.source_id, source.title, source.canonical_url, str(source.kind), source.summary),
            )
        indexed_claims = 0
        evidence_count = 0
        for claim in claim_list:
            if claim.status != ClaimStatus.REVIEWED:
                continue
            applicability = json.dumps(claim.applicability.__dict__, ensure_ascii=False, sort_keys=True)
            tags = json.dumps(claim.tags, ensure_ascii=False)
            search_blob = " ".join([
                claim.question, claim.statement, str(claim.domain), " ".join(claim.tags), applicability
            ]).lower()
            connection.execute(
                "INSERT INTO claims VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (
                    claim.claim_id, str(claim.domain), claim.question, claim.statement,
                    claim.confidence, claim.confidence_rationale, str(claim.safety_level),
                    applicability, tags, search_blob,
                ),
            )
            indexed_claims += 1
            for link in claim.evidence:
                connection.execute(
                    "INSERT INTO evidence VALUES (?, ?, ?, ?, ?, ?)",
                    (
                        claim.claim_id, link.source_id, str(link.role), str(link.strength),
                        link.locator, link.note,
                    ),
                )
                evidence_count += 1
        connection.commit()
    finally:
        connection.close()
    return {"sources": len(source_list), "claims": indexed_claims, "evidence": evidence_count}


def _tokens(query: str) -> List[str]:
    lowered = query.lower().strip()
    tokens = re.findall(r"[a-z0-9_.+-]{2,}|[\u4e00-\u9fff]+", lowered)
    expanded: List[str] = []
    for token in tokens:
        if re.fullmatch(r"[\u4e00-\u9fff]+", token) and len(token) > 2:
            expanded.extend(token[index:index + 2] for index in range(len(token) - 1))
        else:
            expanded.append(token)
    return list(dict.fromkeys(expanded))


def search(index_path: Path, query: str, limit: int = 5) -> List[dict]:
    query = query.strip()
    if not query:
        return []
    connection = sqlite3.connect(str(index_path))
    connection.row_factory = sqlite3.Row
    try:
        rows = connection.execute("SELECT * FROM claims").fetchall()
        terms = _tokens(query)
        ranked = []
        for row in rows:
            blob = row["search_blob"]
            score = 12.0 if query.lower() in blob else 0.0
            score += sum(1.0 + min(blob.count(term), 4) for term in terms if term in blob)
            if score <= 0:
                continue
            score *= 0.5 + float(row["confidence"])
            citations = connection.execute(
                """
                SELECT e.role, e.strength, e.locator, e.note,
                       s.source_id, s.title, s.canonical_url, s.kind
                FROM evidence e JOIN sources s ON s.source_id = e.source_id
                WHERE e.claim_id = ? ORDER BY e.role, s.source_id
                """,
                (row["claim_id"],),
            ).fetchall()
            ranked.append({
                "claim_id": row["claim_id"],
                "domain": row["domain"],
                "question": row["question"],
                "statement": row["statement"],
                "confidence": row["confidence"],
                "confidence_rationale": row["confidence_rationale"],
                "safety_level": row["safety_level"],
                "applicability": json.loads(row["applicability_json"]),
                "tags": json.loads(row["tags_json"]),
                "citations": [dict(item) for item in citations],
                "score": round(score, 4),
            })
        ranked.sort(key=lambda item: (-item["score"], -item["confidence"], item["claim_id"]))
        return ranked[:max(0, limit)]
    finally:
        connection.close()
