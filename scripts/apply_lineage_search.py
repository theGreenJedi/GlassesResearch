#!/usr/bin/env python3
"""Apply lineage identity context to the staged Finder without adding new visible UI."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

SEARCHABLE_OLD = "const searchable = (r) => [r.id,r.maker,r.model,r.type,r.state].join(' ').toLowerCase();"
SEARCHABLE_NEW = "const searchable = (r) => [r.id,r.maker,r.model,r.type,r.state,...(r.lineage_search_terms || [])].join(' ').toLowerCase();"
QUERY_OLD = "const queryInput = host.querySelector('#discovery-query');"
QUERY_NEW = "const queryInput = host.querySelector('#discovery-query');\n    queryInput.value = params.get('q') || '';"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lineage-index", required=True, type=Path)
    parser.add_argument("--devices", required=True, type=Path)
    parser.add_argument("--finder-js", required=True, type=Path)
    args = parser.parse_args()

    lineage = json.loads(args.lineage_index.read_text(encoding="utf-8"))
    device_doc = json.loads(args.devices.read_text(encoding="utf-8"))
    lineage_models = lineage.get("models", {})
    records = device_doc.get("records", [])
    known = {record.get("id") for record in records}
    if not set(lineage_models).issubset(known):
        raise RuntimeError("lineage search: lineage index contains model IDs outside device database")

    enriched = 0
    for record in records:
        model_id = record.get("id")
        context = lineage_models.get(model_id)
        if not context:
            continue
        record["lineage_family_id"] = context.get("family_id")
        record["lineage_family_label"] = context.get("family_label")
        record["lineage_search_terms"] = list(context.get("search_terms", []))
        enriched += 1
    if enriched != lineage.get("model_count"):
        raise RuntimeError(
            f"lineage search coverage mismatch: index={lineage.get('model_count')} devices={enriched}"
        )
    args.devices.write_text(json.dumps(device_doc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    text = args.finder_js.read_text(encoding="utf-8")
    if text.count(SEARCHABLE_OLD) != 1:
        raise RuntimeError("lineage search: Finder searchable hook changed or already patched")
    if text.count(QUERY_OLD) != 1:
        raise RuntimeError("lineage search: Finder query-input hook changed or already patched")
    text = text.replace(SEARCHABLE_OLD, SEARCHABLE_NEW, 1).replace(QUERY_OLD, QUERY_NEW, 1)
    args.finder_js.write_text(text, encoding="utf-8")

    print(f"Lineage search integrated into Finder for {enriched} canonical models")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
