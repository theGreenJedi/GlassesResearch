#!/usr/bin/env python3
"""Build the canonical public GlassesResearch data export.

This joins the existing validated catalog, comparison, Finder, report-card,
evidence, and ecosystem graph outputs without strengthening any claim. Missing
confidence or verification timestamps remain null rather than being inferred.
"""
from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path
from typing import Any

MODEL_NODE_RE = re.compile(r"^model:(gls-\d{4})$")


def load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def by_id(payload: dict[str, Any], key: str = "records") -> dict[str, dict[str, Any]]:
    return {str(item.get("id")): item for item in payload.get(key, []) if item.get("id")}


def compact_claim(field_id: str, entry: dict[str, Any]) -> dict[str, Any]:
    return {
        "field": field_id,
        "value": entry.get("value"),
        "evidence_state": entry.get("evidence", "unknown"),
        "sources": entry.get("sources", []),
        "confidence": None,
        "verified_at": None,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--devices", type=Path, required=True)
    ap.add_argument("--comparisons", type=Path, required=True)
    ap.add_argument("--capabilities", type=Path, required=True)
    ap.add_argument("--report-cards", type=Path, required=True)
    ap.add_argument("--ecosystem", type=Path, required=True)
    ap.add_argument("--evidence", type=Path, required=True)
    ap.add_argument("--schema", type=Path, required=True)
    ap.add_argument("--output-dir", type=Path, required=True)
    args = ap.parse_args()

    devices = load(args.devices)
    comparisons = by_id(load(args.comparisons))
    capabilities = by_id(load(args.capabilities))
    report_cards = by_id(load(args.report_cards))
    ecosystem = load(args.ecosystem)
    evidence = load(args.evidence)
    valid_model_ids = {str(record.get("id")) for record in devices.get("records", [])}

    nodes = {str(n.get("id")): n for n in ecosystem.get("nodes", []) if n.get("id")}
    relations_by_model: dict[str, list[dict[str, Any]]] = {}
    for rel in ecosystem.get("relations", []):
        endpoints = (str(rel.get("from", "")), str(rel.get("to", "")))
        for endpoint in endpoints:
            node = nodes.get(endpoint, {})
            if node.get("type") != "model":
                continue
            match = MODEL_NODE_RE.fullmatch(str(node.get("id", "")))
            if not match:
                continue
            model_id = match.group(1).upper()
            if model_id in valid_model_ids:
                relations_by_model.setdefault(model_id, []).append(rel)

    evidence_resources = evidence.get("resources", [])
    records: list[dict[str, Any]] = []
    for device in devices.get("records", []):
        model_id = str(device["id"])
        comparison = comparisons.get(model_id, {})
        cap = capabilities.get(model_id, {})
        claims = [compact_claim(fid, entry) for fid, entry in comparison.get("fields", {}).items()]
        record = {
            "schema_version": 1,
            "id": model_id,
            "identity": {
                "maker": device.get("maker"),
                "model": device.get("model"),
                "era": device.get("era"),
                "state": device.get("state"),
                "type": device.get("type"),
                "access": device.get("access"),
            },
            "public": device.get("public", {}),
            "catalog_evidence": device.get("evidence"),
            "catalog_links": device.get("links", []),
            "claims": claims,
            "finder_capabilities": cap.get("capabilities", {}),
            "report_card": report_cards.get(model_id),
            "ecosystem_relations": relations_by_model.get(model_id, []),
        }
        records.append(record)

    out = args.output_dir
    model_dir = out / "models"
    model_dir.mkdir(parents=True, exist_ok=True)
    (out / "schema.json").write_text(args.schema.read_text(encoding="utf-8"), encoding="utf-8")
    (out / "evidence-resources.json").write_text(json.dumps({"schema_version": evidence.get("schema_version"), "resources": evidence_resources}, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (out / "ecosystem-relations.json").write_text(json.dumps(ecosystem, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    aggregate = {
        "schema_version": 1,
        "record_count": len(records),
        "records": records,
    }
    (out / "models.json").write_text(json.dumps(aggregate, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    for record in records:
        (model_dir / f"{record['id'].lower()}.json").write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    with (out / "models.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["id", "maker", "model", "era", "state", "type", "access", "model_page", "profile", "report_card", "lineage"])
        writer.writeheader()
        for record in records:
            public = record.get("public", {})
            identity = record["identity"]
            writer.writerow({
                "id": record["id"],
                "maker": identity.get("maker"),
                "model": identity.get("model"),
                "era": identity.get("era"),
                "state": identity.get("state"),
                "type": identity.get("type"),
                "access": identity.get("access"),
                "model_page": public.get("model_page", ""),
                "profile": public.get("profile", ""),
                "report_card": public.get("report_card", ""),
                "lineage": public.get("lineage", ""),
            })

    print(f"Wrote canonical public dataset for {len(records)} models to {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
