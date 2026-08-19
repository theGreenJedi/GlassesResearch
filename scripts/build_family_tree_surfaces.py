#!/usr/bin/env python3
"""Validate family-tree data and inject optional triggers into staged public pages."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ICON = '''<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 3v5m0 0-5 4m5-4 5 4M7 12v5m10-5v5M4 17h6m4 0h6" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>'''
ALLOWED_NODE_TYPES = {"family", "branch", "origin", "model", "alias"}
ALLOWED_STATUS = {"established", "inferred", "unresolved"}
ALLOWED_CONFIDENCE = {"high", "medium", "low"}


def button(model_id: str) -> str:
    return (
        f'<button class="family-tree-trigger" type="button" data-family-tree-model="{model_id}" '
        f'aria-label="View family tree for {model_id}" title="View family tree">{ICON}</button>'
    )


def validate_family(family: dict, known: set[str], repo_root: Path, model_to_family: dict[str, str]) -> None:
    family_id = str(family.get("id") or "")
    if not family_id:
        raise RuntimeError("family tree has a family without an id")
    nodes = family.get("nodes", [])
    edges = family.get("edges", [])
    node_map = {node.get("id"): node for node in nodes}
    if None in node_map or len(node_map) != len(nodes):
        raise RuntimeError(f"family {family_id} has missing or duplicate node ids")
    root_id = family.get("root_id")
    if root_id not in node_map:
        raise RuntimeError(f"family {family_id} root is missing")

    canonical_count = 0
    for node_id, node in node_map.items():
        if node.get("type") not in ALLOWED_NODE_TYPES:
            raise RuntimeError(f"family {family_id} node {node_id} has invalid type")
        if node.get("status") not in ALLOWED_STATUS:
            raise RuntimeError(f"family {family_id} node {node_id} has invalid status")
        model_id = node.get("canonical_id")
        if not model_id:
            continue
        canonical_count += 1
        if node.get("type") != "model":
            raise RuntimeError(f"family {family_id} non-model node {node_id} carries a canonical id")
        if model_id not in known:
            raise RuntimeError(f"family tree references non-canonical model {model_id}")
        if model_id in model_to_family:
            raise RuntimeError(f"model {model_id} appears in multiple family trees")
        model_to_family[model_id] = family_id
    if not canonical_count:
        raise RuntimeError(f"family {family_id} has no canonical models")

    incoming = {node_id: 0 for node_id in node_map}
    children = {node_id: [] for node_id in node_map}
    edge_keys: set[tuple[str, str, str]] = set()
    for edge in edges:
        parent, child = edge.get("parent"), edge.get("child")
        key = (parent, child, str(edge.get("relationship")))
        if key in edge_keys:
            raise RuntimeError(f"family {family_id} contains duplicate edge {key}")
        edge_keys.add(key)
        if parent not in node_map or child not in node_map:
            raise RuntimeError(f"family {family_id} has an edge to a missing node")
        if parent == child:
            raise RuntimeError(f"family {family_id} has a self edge on {parent}")
        if edge.get("status") not in ALLOWED_STATUS:
            raise RuntimeError(f"family {family_id} edge {parent}->{child} has invalid status")
        if edge.get("confidence") not in ALLOWED_CONFIDENCE:
            raise RuntimeError(f"family {family_id} edge {parent}->{child} has invalid confidence")
        if edge.get("inheritance_allowed") is not False:
            raise RuntimeError(f"family {family_id} edge {parent}->{child} permits inheritance")
        evidence = edge.get("evidence", [])
        if not evidence:
            raise RuntimeError(f"family {family_id} edge {parent}->{child} lacks evidence")
        for relative in evidence:
            if not (repo_root / relative).exists():
                raise RuntimeError(f"family {family_id} evidence path does not exist: {relative}")
        incoming[child] += 1
        children[parent].append(child)

    for node_id, count in incoming.items():
        expected = 0 if node_id == root_id else 1
        if count != expected:
            raise RuntimeError(f"family {family_id} node {node_id} has {count} parents; expected {expected}")

    visiting: set[str] = set()
    visited: set[str] = set()
    def walk(node_id: str) -> None:
        if node_id in visiting:
            raise RuntimeError(f"family {family_id} contains a cycle at {node_id}")
        if node_id in visited:
            return
        visiting.add(node_id)
        for child_id in children[node_id]:
            walk(child_id)
        visiting.remove(node_id)
        visited.add(node_id)
    walk(root_id)
    if visited != set(node_map):
        raise RuntimeError(f"family {family_id} has unreachable nodes: {sorted(set(node_map) - visited)}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--site-root", type=Path, required=True)
    parser.add_argument("--families", type=Path, required=True)
    args = parser.parse_args()

    payload = json.loads(args.families.read_text(encoding="utf-8"))
    if payload.get("schema_version") != 1:
        raise RuntimeError("family tree schema_version must be 1")
    rules = payload.get("rules", {})
    if rules.get("score_inheritance") is not False or rules.get("relationship_inheritance") is not False:
        raise RuntimeError("family tree data must explicitly forbid score and relationship inheritance")
    if rules.get("unknown_relationships_remain_unknown") is not True:
        raise RuntimeError("family tree data must preserve unknown relationships as unknown")

    devices = json.loads((args.site_root / "data/devices.json").read_text(encoding="utf-8"))
    known = {item["id"] for item in devices.get("records", [])}
    repo_root = args.families.resolve().parents[1]
    model_to_family: dict[str, str] = {}
    family_ids: set[str] = set()
    for family in payload.get("families", []):
        family_id = str(family.get("id") or "")
        if family_id in family_ids:
            raise RuntimeError(f"duplicate family id {family_id}")
        family_ids.add(family_id)
        validate_family(family, known, repo_root, model_to_family)
    if not model_to_family:
        raise RuntimeError("family tree data contains no canonical models")

    injected_models = 0
    for model_id in sorted(model_to_family):
        page = args.site_root / "models/catalog" / f"{model_id.lower()}.md"
        if not page.exists():
            raise RuntimeError(f"generated model page missing for {model_id}")
        text = page.read_text(encoding="utf-8")
        if "data-family-tree-model" in text:
            raise RuntimeError(f"model page already contains a family-tree trigger: {model_id}")
        match = re.search(r"^(# .+)$", text, re.MULTILINE)
        if not match:
            raise RuntimeError(f"model page has no H1: {page}")
        trigger = f'\n\n<span class="family-tree-model-trigger">{button(model_id)}</span>'
        text = text[:match.end()] + trigger + text[match.end():]
        page.write_text(text, encoding="utf-8")
        injected_models += 1

    report = args.site_root / "docs/REPORT_CARD.md"
    text = report.read_text(encoding="utf-8")
    injected_rows = 0
    lines = []
    for line in text.splitlines():
        match = re.search(r"<td><code>(GLS-\d{4})</code></td>", line)
        if match and match.group(1) in model_to_family:
            if "data-family-tree-model" in line:
                raise RuntimeError(f"Report Card row already contains a family-tree trigger: {match.group(1)}")
            model_id = match.group(1)
            line = line.replace("</a>", f"</a> {button(model_id)}", 1)
            injected_rows += 1
        lines.append(line)
    report.write_text("\n".join(lines) + ("\n" if text.endswith("\n") else ""), encoding="utf-8")

    expected = len(model_to_family)
    if injected_models != expected or injected_rows != expected:
        raise RuntimeError(
            f"family-tree trigger coverage mismatch: expected {expected}, "
            f"model_pages={injected_models}, report_rows={injected_rows}"
        )
    print(f"Family-tree surfaces validated: {len(family_ids)} families, {expected} canonical models")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
