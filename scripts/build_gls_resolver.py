#!/usr/bin/env python3
"""Build first-class public resolution surfaces for stable GLS identifiers."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ID_RE = re.compile(r"^GLS-\d{4}$")


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--devices", type=Path, required=True)
    parser.add_argument("--output-root", type=Path, required=True)
    args = parser.parse_args()

    payload = load(args.devices)
    records = payload.get("records", [])
    expected = payload.get("record_count")
    if not isinstance(expected, int) or expected != len(records):
        raise SystemExit("device database record_count does not match records")

    ids = [str(record.get("id", "")) for record in records]
    if any(not ID_RE.fullmatch(model_id) for model_id in ids):
        raise SystemExit("every canonical device must have a GLS-#### identifier")
    if len(ids) != len(set(ids)):
        raise SystemExit("canonical GLS identifiers must be unique")

    resolver_dir = args.output_root / "gls"
    resolver_dir.mkdir(parents=True, exist_ok=True)
    index_records: list[dict] = []
    index_rows: list[str] = []

    for record in records:
        model_id = record["id"]
        slug = model_id.lower()
        public = record.get("public", {})
        model_page = public.get("model_page") or f"/models/catalog/{slug}/"
        json_url = f"/data/public/models/{slug}.json"
        resolver_url = f"/gls/{slug}/"
        report_card = public.get("report_card")

        entry = {
            "id": model_id,
            "maker": record.get("maker"),
            "model": record.get("model"),
            "state": record.get("state"),
            "type": record.get("type"),
            "resolver": resolver_url,
            "model_page": model_page,
            "json": json_url,
            "report_card": report_card,
        }
        index_records.append(entry)
        index_rows.append(
            f"| [{model_id}]({resolver_url}) | {record.get('maker')} | {record.get('model')} | [{model_page}]({model_page}) |"
        )

        report_line = f"- Report Card: [{report_card}]({report_card})\n" if report_card else "- Report Card: included on the canonical model page when scored\n"
        page = f'''---
title: "{model_id} — {str(record.get('maker', '')).replace('"', '\\"')} {str(record.get('model', '')).replace('"', '\\"')}"
description: "Resolve stable GlassesResearch identifier {model_id} to its canonical model record and machine-readable data."
---

# {model_id}

**{model_id} resolves to {record.get('maker')} {record.get('model')}.**

This is a stable identifier resolver. Product research lives on the canonical model page; machine consumers can use the JSON record.

- Canonical model page: [{model_page}]({model_page})
- Machine-readable JSON: [{json_url}]({json_url})
{report_line}- Canonical ledger: [/models/THE_LIST/](/models/THE_LIST/)

Identifier: `{model_id}`  
Lifecycle state: {record.get('state')}  
Device type: {record.get('type')}
'''
        (resolver_dir / f"{slug}.md").write_text(page, encoding="utf-8")

    resolver_index = {
        "schema_version": 1,
        "record_count": len(index_records),
        "id_format": "GLS-####",
        "resolver_url_template": "/gls/gls-####/",
        "model_json_url_template": "/data/public/models/gls-####.json",
        "records": index_records,
    }
    data_path = args.output_root / "data" / "gls-index.json"
    data_path.parent.mkdir(parents=True, exist_ok=True)
    data_path.write_text(json.dumps(resolver_index, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    (resolver_dir / "index.md").write_text(
        f"# GLS identifier resolver\n\n"
        f"Every canonical GlassesResearch identifier resolves through the same deterministic pattern. "
        f"For example, `GLS-0038` is `/gls/gls-0038/`, and its machine record is "
        f"`/data/public/models/gls-0038.json`. The complete machine-readable resolver is "
        f"[`/data/gls-index.json`](/data/gls-index.json).\n\n"
        f"| GLS ID | Maker | Model | Canonical research page |\n"
        f"|---|---|---|---|\n" + "\n".join(index_rows) + "\n",
        encoding="utf-8",
    )

    # Acceptance test: every row must point to a generated resolver and the
    # public-data convention used by build_public_dataset.py.
    for entry in index_records:
        slug = entry["id"].lower()
        if not (resolver_dir / f"{slug}.md").is_file():
            raise SystemExit(f"missing resolver page for {entry['id']}")
        if entry["json"] != f"/data/public/models/{slug}.json":
            raise SystemExit(f"non-deterministic JSON path for {entry['id']}")

    print(f"Generated deterministic GLS resolvers for {len(index_records)} models")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
