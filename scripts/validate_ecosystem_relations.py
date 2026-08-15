#!/usr/bin/env python3
"""Validate the evidence-backed ecosystem relationship graph."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data/ecosystem-relations.json"
NODE_TYPES = {"model","lineage","manufacturer","oem_odm","operating_platform","companion_app","sdk_api","firmware_family","protocol_transport","ai_service","community_project"}
RELATIONS = {"member_of","rebrand_of","manufactured_by","uses_platform","compatible_with","requires_app","exposes_sdk","uses_protocol","depends_on_service","community_supports","supersedes"}
CONFIDENCE = {"high","medium","low"}
STATUS = {"established","inferred","unresolved"}


def main() -> int:
    payload = json.loads(DATA.read_text(encoding="utf-8"))
    errors = []
    if payload.get("schema_version") != 1:
        errors.append("schema_version must be 1")
    nodes = payload.get("nodes", [])
    relations = payload.get("relations", [])
    ids = [node.get("id") for node in nodes]
    if len(ids) != len(set(ids)):
        errors.append("node IDs must be unique")
    node_ids = set(ids)
    for node in nodes:
        if node.get("type") not in NODE_TYPES:
            errors.append(f"{node.get('id')}: invalid node type")
        path = node.get("path")
        if path and not (ROOT / path).exists():
            errors.append(f"{node.get('id')}: unresolved path {path}")
        if not path and not node.get("url"):
            errors.append(f"{node.get('id')}: node needs path or url")
    relation_ids = set()
    for relation in relations:
        rid = relation.get("id")
        if rid in relation_ids:
            errors.append(f"duplicate relation ID {rid}")
        relation_ids.add(rid)
        if relation.get("from") not in node_ids or relation.get("to") not in node_ids:
            errors.append(f"{rid}: relation endpoint does not resolve")
        if relation.get("type") not in RELATIONS:
            errors.append(f"{rid}: invalid relation type")
        if relation.get("confidence") not in CONFIDENCE or relation.get("status") not in STATUS:
            errors.append(f"{rid}: invalid confidence/status")
        evidence = relation.get("evidence")
        if not isinstance(evidence, list) or not evidence:
            errors.append(f"{rid}: evidence is required")
            continue
        for item in evidence:
            if not item.get("claim"):
                errors.append(f"{rid}: evidence claim is required")
            path = item.get("path")
            if path and not (ROOT / path).exists():
                errors.append(f"{rid}: unresolved evidence path {path}")
            if not path and not item.get("url"):
                errors.append(f"{rid}: evidence needs path or url")
    if errors:
        print("\n".join(f"ERROR: {error}" for error in errors), file=sys.stderr)
        return 1
    print(f"Validated {len(nodes)} ecosystem nodes and {len(relations)} evidence-backed relations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
