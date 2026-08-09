"""Manual evidence import and normalization."""

from __future__ import annotations

import hashlib
import json
from typing import Any, Dict, Mapping

from .models import SourceRecord


def _normalized_digest(payload: Mapping[str, Any]) -> str:
    digest_payload = {key: value for key, value in payload.items() if key != "content_sha256"}
    serialized = json.dumps(
        digest_payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return hashlib.sha256(serialized).hexdigest()


def normalize_manual_source(payload: Mapping[str, Any]) -> SourceRecord:
    """Create a canonical source and derive its integrity digest.

    The caller must supply an explicit access mode. This function performs no network
    access and does not interpret imported text as instructions.
    """

    normalized: Dict[str, Any] = dict(payload)
    normalized["authors"] = list(normalized.get("authors", []))
    normalized["attention"] = dict(normalized.get("attention", {}))
    normalized["metadata"] = dict(normalized.get("metadata", {}))
    normalized["content_sha256"] = _normalized_digest(normalized)
    return SourceRecord.from_dict(normalized)
