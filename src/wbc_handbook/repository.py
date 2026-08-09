"""JSON repository with path-traversal protection."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Iterable, List, Mapping, Any

from .models import EngineeringClaim, ID_PATTERN, SourceRecord


class RepositoryError(RuntimeError):
    pass


class HandbookRepository:
    def __init__(self, root: Path) -> None:
        self.root = Path(root).resolve()
        self.sources_dir = self.root / "sources"
        self.claims_dir = self.root / "claims"

    @staticmethod
    def _read_json(path: Path) -> Mapping[str, Any]:
        try:
            value = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            raise RepositoryError(f"cannot read {path}: {exc}") from exc
        if not isinstance(value, dict):
            raise RepositoryError(f"{path} must contain one JSON object")
        return value

    def _paths(self, directory: Path) -> Iterable[Path]:
        if not directory.exists():
            return []
        return sorted(path for path in directory.glob("*.json") if path.is_file())

    def load_sources(self) -> List[SourceRecord]:
        return [SourceRecord.from_dict(self._read_json(path)) for path in self._paths(self.sources_dir)]

    def load_claims(self) -> List[EngineeringClaim]:
        return [EngineeringClaim.from_dict(self._read_json(path)) for path in self._paths(self.claims_dir)]

    @staticmethod
    def _target(directory: Path, record_id: str) -> Path:
        if not ID_PATTERN.fullmatch(record_id):
            raise RepositoryError(f"unsafe record ID: {record_id!r}")
        target = (directory / f"{record_id}.json").resolve()
        if target.parent != directory.resolve():
            raise RepositoryError("record path escapes the repository")
        return target

    @staticmethod
    def _write(path: Path, payload: Mapping[str, Any], overwrite: bool) -> Path:
        path.parent.mkdir(parents=True, exist_ok=True)
        if path.exists() and not overwrite:
            raise RepositoryError(f"record already exists: {path}")
        path.write_text(
            json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        return path

    def save_source(self, source: SourceRecord, overwrite: bool = False) -> Path:
        return self._write(
            self._target(self.sources_dir, source.source_id), source.to_dict(), overwrite
        )

    def save_claim(self, claim: EngineeringClaim, overwrite: bool = False) -> Path:
        return self._write(
            self._target(self.claims_dir, claim.claim_id), claim.to_dict(), overwrite
        )
