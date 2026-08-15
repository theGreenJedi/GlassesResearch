#!/usr/bin/env python3
"""Validate comparison research and build a normalized comparison bundle.

PR #40 establishes infrastructure only. The schema may exist with zero model
comparison records. Future research PRs can add comparisons/data/GLS-####.json
without changing the renderer contract.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SCHEMA = ROOT / "comparisons" / "schema.json"
DEFAULT_DATA_DIR = ROOT / "comparisons" / "data"
GLS_RE = re.compile(r"^GLS-\d{4}$")
ALLOWED_TYPES = {"text", "number", "boolean", "list"}
REQUIRED_EVIDENCE = {"hands-on", "community", "primary", "unresolved", "unknown"}


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def validate_schema(schema: dict[str, Any]) -> tuple[list[str], list[dict[str, Any]]]:
    errors: list[str] = []
    fields: list[dict[str, Any]] = []

    if schema.get("schema_version") != 1:
        errors.append("schema_version must be 1")
    if not schema.get("unknown_label"):
        errors.append("unknown_label is required")

    evidence_states = schema.get("evidence_states")
    if not isinstance(evidence_states, dict):
        errors.append("evidence_states must be an object")
    elif set(evidence_states) != REQUIRED_EVIDENCE:
        errors.append(
            "evidence_states must contain exactly: " + ", ".join(sorted(REQUIRED_EVIDENCE))
        )

    groups = schema.get("groups")
    if not isinstance(groups, list) or not groups:
        errors.append("groups must be a non-empty array")
        return errors, fields

    seen_groups: set[str] = set()
    seen_fields: set[str] = set()
    for group in groups:
        group_id = group.get("id") if isinstance(group, dict) else None
        if not group_id or group_id in seen_groups:
            errors.append(f"invalid or duplicate group id: {group_id!r}")
            continue
        seen_groups.add(group_id)
        if not group.get("label"):
            errors.append(f"group {group_id}: label is required")
        group_fields = group.get("fields")
        if not isinstance(group_fields, list) or not group_fields:
            errors.append(f"group {group_id}: fields must be a non-empty array")
            continue
        for field in group_fields:
            if not isinstance(field, dict):
                errors.append(f"group {group_id}: field must be an object")
                continue
            field_id = field.get("id")
            if not field_id or field_id in seen_fields:
                errors.append(f"invalid or duplicate field id: {field_id!r}")
                continue
            seen_fields.add(field_id)
            field_type = field.get("type")
            if field_type not in ALLOWED_TYPES:
                errors.append(f"field {field_id}: unsupported type {field_type!r}")
            if not field.get("label"):
                errors.append(f"field {field_id}: label is required")
            normalized = dict(field)
            normalized["group"] = group_id
            fields.append(normalized)

    return errors, fields


def validate_value(field: dict[str, Any], value: Any) -> bool:
    field_type = field["type"]
    if field_type == "text":
        return isinstance(value, str) and bool(value.strip())
    if field_type == "number":
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    if field_type == "boolean":
        return isinstance(value, bool)
    if field_type == "list":
        return isinstance(value, list) and all(isinstance(item, str) and item.strip() for item in value)
    return False


def load_records(data_dir: Path, fields: list[dict[str, Any]]) -> tuple[list[str], list[dict[str, Any]]]:
    errors: list[str] = []
    records: list[dict[str, Any]] = []
    field_map = {field["id"]: field for field in fields}

    if not data_dir.exists():
        return errors, records

    for path in sorted(data_dir.glob("*.json")):
        try:
            raw = load_json(path)
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"{path}: invalid JSON: {exc}")
            continue
        if not isinstance(raw, dict):
            errors.append(f"{path}: record must be an object")
            continue
        model_id = raw.get("id")
        if not isinstance(model_id, str) or not GLS_RE.fullmatch(model_id):
            errors.append(f"{path}: id must match GLS-####")
            continue
        if path.stem != model_id:
            errors.append(f"{path}: filename must match record id {model_id}.json")

        raw_fields = raw.get("fields")
        if not isinstance(raw_fields, dict):
            errors.append(f"{path}: fields must be an object")
            continue

        normalized_fields: dict[str, Any] = {}
        for field_id, entry in raw_fields.items():
            if field_id not in field_map:
                errors.append(f"{path}: unknown comparison field {field_id!r}")
                continue
            if not isinstance(entry, dict):
                errors.append(f"{path}: field {field_id} must be an object")
                continue
            evidence = entry.get("evidence")
            if evidence not in REQUIRED_EVIDENCE - {"unknown"}:
                errors.append(
                    f"{path}: field {field_id} evidence must be hands-on, community, primary, or unresolved"
                )
            if "value" not in entry or not validate_value(field_map[field_id], entry.get("value")):
                errors.append(
                    f"{path}: field {field_id} value does not match type {field_map[field_id]['type']}"
                )
            sources = entry.get("sources")
            if not isinstance(sources, list) or not sources or not all(
                isinstance(source, str) and source.strip() for source in sources
            ):
                errors.append(f"{path}: field {field_id} requires at least one source")
            normalized_fields[field_id] = {
                "value": entry.get("value"),
                "evidence": evidence,
                "sources": sources or [],
            }

        records.append({"id": model_id, "fields": normalized_fields})

    ids = [record["id"] for record in records]
    if len(ids) != len(set(ids)):
        errors.append("duplicate comparison record IDs detected")

    return errors, records


def normalize(schema: dict[str, Any], fields: list[dict[str, Any]], records: list[dict[str, Any]]) -> dict[str, Any]:
    unknown = schema["unknown_label"]
    normalized_records: list[dict[str, Any]] = []
    for record in records:
        values: dict[str, Any] = {}
        supplied = record["fields"]
        for field in fields:
            field_id = field["id"]
            if field_id in supplied:
                values[field_id] = supplied[field_id]
            else:
                values[field_id] = {
                    "value": unknown,
                    "evidence": "unknown",
                    "sources": [],
                }
        normalized_records.append({"id": record["id"], "fields": values})

    return {
        "schema_version": schema["schema_version"],
        "unknown_label": unknown,
        "evidence_states": schema["evidence_states"],
        "groups": schema["groups"],
        "record_count": len(normalized_records),
        "records": normalized_records,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--schema", type=Path, default=DEFAULT_SCHEMA)
    parser.add_argument("--data-dir", type=Path, default=DEFAULT_DATA_DIR)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--validate-only", action="store_true")
    args = parser.parse_args()

    try:
        schema = load_json(args.schema)
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: cannot read comparison schema: {exc}", file=sys.stderr)
        return 1
    if not isinstance(schema, dict):
        print("ERROR: comparison schema root must be an object", file=sys.stderr)
        return 1

    errors, fields = validate_schema(schema)
    record_errors, records = load_records(args.data_dir, fields)
    errors.extend(record_errors)
    if errors:
        print("ERROR: comparison engine validation failed:", file=sys.stderr)
        for error in errors:
            print(f"  {error}", file=sys.stderr)
        return 1

    bundle = normalize(schema, fields, records)
    if args.output and not args.validate_only:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(bundle, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"Wrote comparison bundle with {len(records)} researched model records to {args.output}")
    else:
        print(
            f"Validated comparison schema with {len(fields)} fields and "
            f"{len(records)} researched model records"
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
