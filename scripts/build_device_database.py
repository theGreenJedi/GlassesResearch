#!/usr/bin/env python3
"""Build and validate the machine-readable GlassesResearch device database.

The human-maintained source of truth remains models/THE_LIST.md. This script
parses every GLS record, validates the stable-ID ledger, and can emit a JSON
representation for the website and downstream research tools.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE = ROOT / "models" / "THE_LIST.md"
COUNT_RE = re.compile(r"\*\*Count:\*\*\s*(\d+)")
ID_RE = re.compile(r"^GLS-(\d{4})$")
LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
MARKDOWN_RE = re.compile(r"[`*_~]")


def clean(value: str) -> str:
    value = value.strip()
    value = LINK_RE.sub(lambda m: m.group(1), value)
    return MARKDOWN_RE.sub("", value).strip()


def links(value: str) -> list[dict[str, str]]:
    found: list[dict[str, str]] = []
    for label, target in LINK_RE.findall(value):
        target = target.strip()
        kind = "external" if urlparse(target).scheme in {"http", "https"} else "internal"
        found.append({"label": clean(label), "url": target, "kind": kind})
    return found


def parse(source: Path) -> tuple[int, list[dict[str, object]]]:
    text = source.read_text(encoding="utf-8")
    count_match = COUNT_RE.search(text)
    if not count_match:
        raise ValueError("THE_LIST.md is missing its declared Count")
    declared_count = int(count_match.group(1))

    records: list[dict[str, object]] = []
    for line_number, line in enumerate(text.splitlines(), start=1):
        if not line.startswith("| GLS-"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) != 8:
            raise ValueError(f"line {line_number}: expected 8 model columns, found {len(cells)}")
        stable_id, maker, model, era, state, device_type, access, evidence = cells
        if not ID_RE.match(stable_id):
            raise ValueError(f"line {line_number}: malformed stable ID {stable_id!r}")
        records.append(
            {
                "id": stable_id,
                "maker": clean(maker),
                "model": clean(model),
                "era": clean(era),
                "state": clean(state),
                "type": clean(device_type),
                "access": clean(access),
                "evidence": clean(evidence.split(";", 1)[0]),
                "links": links(evidence),
                "ledger_line": line_number,
            }
        )

    return declared_count, records


def validate(declared_count: int, records: list[dict[str, object]]) -> None:
    errors: list[str] = []
    ids = [str(record["id"]) for record in records]
    if len(records) != declared_count:
        errors.append(f"declared Count is {declared_count}, parsed {len(records)} records")
    if len(ids) != len(set(ids)):
        errors.append("duplicate GLS stable IDs detected")

    expected = [f"GLS-{number:04d}" for number in range(1, declared_count + 1)]
    if ids != expected:
        missing = sorted(set(expected) - set(ids))
        unexpected = sorted(set(ids) - set(expected))
        if missing:
            errors.append("missing stable IDs: " + ", ".join(missing[:20]))
        if unexpected:
            errors.append("unexpected stable IDs: " + ", ".join(unexpected[:20]))
        if not missing and not unexpected:
            errors.append("stable IDs are not in canonical numeric order")

    for record in records:
        if not record["maker"] or not record["model"]:
            errors.append(f"{record['id']}: maker/model must not be empty")
        if not record["evidence"]:
            errors.append(f"{record['id']}: evidence classification must not be empty")
        if not record["links"]:
            errors.append(f"{record['id']}: at least one research/source link is required")

    if errors:
        raise ValueError("device database validation failed:\n  " + "\n  ".join(errors))


def payload(records: list[dict[str, object]]) -> dict[str, object]:
    return {
        "schema_version": 1,
        "canonical_source": "models/THE_LIST.md",
        "record_count": len(records),
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--validate-only", action="store_true")
    args = parser.parse_args()

    try:
        declared_count, records = parse(args.source)
        validate(declared_count, records)
    except (OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    if args.output and not args.validate_only:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(payload(records), indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"Wrote {len(records)} canonical device records to {args.output}")
    else:
        print(f"Validated {len(records)} canonical device records from {args.source}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
