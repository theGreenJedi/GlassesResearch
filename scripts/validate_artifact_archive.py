#!/usr/bin/env python3
"""Validate GlassesResearch artifact preservation records and stored files."""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ROOT / "artifacts"
SCHEMA_PATH = ARTIFACTS / "manifest.schema.json"
RECORDS = ARTIFACTS / "records"
FILES = ARTIFACTS / "files"
ID_RE = re.compile(r"^PA-\d{4}$")
SHA_RE = re.compile(r"^[0-9a-f]{64}$")


def load(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    errors: list[str] = []
    try:
        schema = load(SCHEMA_PATH)
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: cannot load artifact schema: {exc}", file=sys.stderr)
        return 1

    required = set(schema.get("required", []))
    allowed_types = set(schema.get("artifact_types", []))
    allowed_redistribution = set(schema.get("redistribution_values", []))
    allowed_states = set(schema.get("preservation_states", []))

    seen_ids: set[str] = set()
    local_paths: set[str] = set()
    record_count = 0

    for path in sorted(RECORDS.glob("*.json")):
        record_count += 1
        try:
            record = load(path)
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"{path}: invalid JSON: {exc}")
            continue
        if not isinstance(record, dict):
            errors.append(f"{path}: record root must be an object")
            continue

        missing = sorted(required - set(record))
        if missing:
            errors.append(f"{path}: missing required fields: {', '.join(missing)}")

        record_id = record.get("record_id")
        if not isinstance(record_id, str) or not ID_RE.fullmatch(record_id):
            errors.append(f"{path}: record_id must match PA-####")
        else:
            if path.stem != record_id:
                errors.append(f"{path}: filename must match {record_id}.json")
            if record_id in seen_ids:
                errors.append(f"{path}: duplicate record_id {record_id}")
            seen_ids.add(record_id)

        platforms = record.get("platforms")
        if not isinstance(platforms, list) or not platforms or not all(isinstance(x, str) and x.strip() for x in platforms):
            errors.append(f"{path}: platforms must be a non-empty string array")

        if record.get("artifact_type") not in allowed_types:
            errors.append(f"{path}: unsupported artifact_type {record.get('artifact_type')!r}")
        if record.get("redistribution") not in allowed_redistribution:
            errors.append(f"{path}: invalid redistribution value")
        if record.get("preservation_status") not in allowed_states:
            errors.append(f"{path}: invalid preservation_status")

        url = record.get("canonical_url")
        parsed = urlparse(url) if isinstance(url, str) else None
        if not parsed or parsed.scheme not in {"http", "https"} or not parsed.netloc:
            errors.append(f"{path}: canonical_url must be an absolute HTTP(S) URL")

        status = record.get("preservation_status")
        local_path = record.get("local_path")
        expected_hash = record.get("sha256")
        if status == "artifact-preserved":
            if not isinstance(local_path, str) or not local_path.startswith("artifacts/files/"):
                errors.append(f"{path}: artifact-preserved record requires local_path under artifacts/files/")
            if not isinstance(expected_hash, str) or not SHA_RE.fullmatch(expected_hash):
                errors.append(f"{path}: artifact-preserved record requires lowercase SHA-256")

        if isinstance(local_path, str):
            if not local_path.startswith("artifacts/files/"):
                errors.append(f"{path}: local_path must be under artifacts/files/")
            else:
                candidate = ROOT / local_path
                if not candidate.is_file():
                    errors.append(f"{path}: local file does not exist: {local_path}")
                else:
                    local_paths.add(local_path)
                    if isinstance(expected_hash, str) and SHA_RE.fullmatch(expected_hash):
                        actual = sha256(candidate)
                        if actual != expected_hash:
                            errors.append(f"{path}: SHA-256 mismatch for {local_path}")

    if FILES.exists():
        for path in FILES.rglob("*"):
            if path.is_file() and path.name != ".gitkeep":
                relative = path.relative_to(ROOT).as_posix()
                if relative not in local_paths:
                    errors.append(f"unregistered preserved file: {relative}")

    print(f"Validated {record_count} artifact preservation records.")
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("Artifact archive validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
