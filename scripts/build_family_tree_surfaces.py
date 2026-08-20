#!/usr/bin/env python3
"""Validate family-tree data, apply audited corrections, build lineage context, and inject optional public triggers."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

ICON = '''<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 3v5m0 0-5 4m5-4 5 4M7 12v5m10-5v5M4 17h6m4 0h6" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>'''
ALLOWED_NODE_TYPES = {"family", "branch", "origin", "model", "alias"}
ALLOWED_STATUS = {"established", "inferred", "unresolved"}
ALLOWED_CONFIDENCE = {"high", "medium", "low"}
ALLOWED_RELATIONSHIPS = {"member_of", "product_branch", "successor", "derived_from", "alias_of", "rebrand_of"}
REQUIRED_RULES = {
    "score_inheritance": False,
    "relationship_inheritance": False,
    "unknown_relationships_remain_unknown": True,
}
FORBIDDEN_INDEX_KEYS = {"score", "scores", "capability", "capabilities", "rating", "ratings"}


def button(model_id: str) -> str:
    return (
        f'<button class="family-tree-trigger" type="button" data-family-tree-model="{model_id}" '
        f'aria-label="View family tree for {model_id}" title="View family tree">{ICON}</button>'
    )


def load_source(path: Path) -> dict:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if payload.get("schema_version") != 1:
        raise RuntimeError(f"family tree schema_version must be 1: {path}")
    rules = payload.get("rules", {})
    for key, expected in REQUIRED_RULES.items():
        if rules.get(key) is not expected:
            raise RuntimeError(f"family tree source {path} violates required rule {key}={expected}")
    if not isinstance(payload.get("families"), list):
        raise RuntimeError(f"family tree source {path} must contain a families list")
    return payload


def relation_type_check(family_id: str, edge: dict, node_map: dict[str, dict]) -> None:
    relationship = str(edge.get("relationship") or "")
    if relationship not in ALLOWED_RELATIONSHIPS:
        raise RuntimeError(f"family {family_id} uses unsupported relationship {relationship!r}")
    parent_type = node_map[edge["parent"]].get("type")
    child_type = node_map[edge["child"]].get("type")
    if relationship in {"alias_of", "rebrand_of"}:
        if parent_type != "model" or child_type != "alias":
            raise RuntimeError(f"family {family_id} {relationship} must be model -> alias")
    elif relationship == "member_of":
        if parent_type not in {"family", "branch"} or child_type != "model":
            raise RuntimeError(f"family {family_id} member_of must be family/branch -> model")
    elif relationship == "product_branch":
        if parent_type not in {"family", "branch", "model"} or child_type != "branch":
            raise RuntimeError(f"family {family_id} product_branch must end at a branch node")
    elif relationship == "successor":
        if parent_type not in {"model", "branch"} or child_type not in {"model", "branch"}:
            raise RuntimeError(f"family {family_id} successor must connect model/branch nodes")
    elif relationship == "derived_from":
        if parent_type != "origin" or child_type not in {"family", "branch"}:
            raise RuntimeError(f"family {family_id} derived_from must be origin -> family/branch")


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
            raise RuntimeError(
                f"model {model_id} appears in multiple family trees: "
                f"{model_to_family[model_id]} and {family_id}"
            )
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
        relation_type_check(family_id, edge, node_map)
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


def load_corrections(path: Path | None) -> list[dict]:
    if path is None:
        return []
    payload = json.loads(path.read_text(encoding="utf-8"))
    if payload.get("schema_version") != 1 or not isinstance(payload.get("corrections"), list):
        raise RuntimeError(f"invalid family-tree audit corrections: {path}")
    return payload["corrections"]


def edge_matches(edge: dict, spec: dict) -> bool:
    return all(edge.get(key) == value for key, value in spec.items())


def apply_corrections(families: list[dict], corrections: list[dict], repo_root: Path) -> None:
    family_map = {str(family.get("id")): family for family in families}
    seen_ids: set[str] = set()
    for correction in corrections:
        correction_id = str(correction.get("id") or "")
        if not correction_id or correction_id in seen_ids:
            raise RuntimeError(f"invalid or duplicate audit correction id {correction_id!r}")
        seen_ids.add(correction_id)
        family_id = str(correction.get("family_id") or "")
        family = family_map.get(family_id)
        if family is None:
            raise RuntimeError(f"audit correction {correction_id} references unknown family {family_id}")
        if not str(correction.get("reason") or "").strip():
            raise RuntimeError(f"audit correction {correction_id} lacks a reason")
        evidence = correction.get("evidence", [])
        if not evidence:
            raise RuntimeError(f"audit correction {correction_id} lacks evidence")
        for relative in evidence:
            if not (repo_root / relative).exists():
                raise RuntimeError(f"audit correction {correction_id} evidence path does not exist: {relative}")

        edges = family.setdefault("edges", [])
        for spec in correction.get("remove_edges", []):
            matches = [index for index, edge in enumerate(edges) if edge_matches(edge, spec)]
            if len(matches) != 1:
                raise RuntimeError(
                    f"audit correction {correction_id} expected exactly one edge matching {spec}; found {len(matches)}"
                )
            edges.pop(matches[0])
        for edge in correction.get("add_edges", []):
            if any(edge_matches(existing, {"parent": edge.get("parent"), "child": edge.get("child"), "relationship": edge.get("relationship")}) for existing in edges):
                raise RuntimeError(f"audit correction {correction_id} would duplicate edge {edge}")
            edge = dict(edge)
            edge["audit_correction_id"] = correction_id
            edges.append(edge)


def relationship_id(family_id: str, edge: dict) -> str:
    stable = f"{family_id}|{edge.get('parent')}|{edge.get('relationship')}|{edge.get('child')}"
    return "GLR-" + hashlib.sha1(stable.encode("utf-8")).hexdigest()[:12].upper()


def ancestry(node_id: str, parent_of: dict[str, str], node_map: dict[str, dict]) -> list[dict]:
    path: list[dict] = []
    current = node_id
    seen: set[str] = set()
    while current in parent_of:
        current = parent_of[current]
        if current in seen:
            break
        seen.add(current)
        path.append(node_map[current])
    path.reverse()
    return path


def build_lineage_index(families: list[dict]) -> dict:
    models: dict[str, dict] = {}
    relationships: list[dict] = []
    relationship_ids: set[str] = set()

    for family in families:
        family_id = str(family["id"])
        family_label = str(family.get("label") or family_id)
        node_map = {node["id"]: node for node in family.get("nodes", [])}
        parent_of = {edge["child"]: edge["parent"] for edge in family.get("edges", [])}
        canonical_nodes = [node for node in family.get("nodes", []) if node.get("canonical_id")]
        related_ids = sorted(str(node["canonical_id"]) for node in canonical_nodes)

        incident: dict[str, list[str]] = {node_id: [] for node_id in node_map}
        predecessor: dict[str, set[str]] = {model_id: set() for model_id in related_ids}
        successor: dict[str, set[str]] = {model_id: set() for model_id in related_ids}
        aliases: dict[str, list[dict]] = {model_id: [] for model_id in related_ids}

        for edge in family.get("edges", []):
            rid = relationship_id(family_id, edge)
            if rid in relationship_ids:
                raise RuntimeError(f"duplicate stable relationship id {rid}")
            relationship_ids.add(rid)
            parent_node = node_map[edge["parent"]]
            child_node = node_map[edge["child"]]
            parent_model = parent_node.get("canonical_id")
            child_model = child_node.get("canonical_id")
            record = {
                "id": rid,
                "family_id": family_id,
                "parent_node_id": edge["parent"],
                "child_node_id": edge["child"],
                "parent_canonical_id": parent_model,
                "child_canonical_id": child_model,
                "relationship": edge["relationship"],
                "label": edge.get("label"),
                "confidence": edge.get("confidence"),
                "status": edge.get("status"),
                "evidence": list(edge.get("evidence", [])),
            }
            if edge.get("audit_correction_id"):
                record["audit_correction_id"] = edge["audit_correction_id"]
            relationships.append(record)
            incident[edge["parent"]].append(rid)
            incident[edge["child"]].append(rid)
            if edge["relationship"] == "successor" and parent_model and child_model:
                successor[parent_model].add(child_model)
                predecessor[child_model].add(parent_model)
            if edge["relationship"] in {"alias_of", "rebrand_of"} and parent_model and child_node.get("type") == "alias":
                aliases[parent_model].append({
                    "label": child_node.get("label"),
                    "relationship": edge["relationship"],
                    "status": edge.get("status"),
                    "confidence": edge.get("confidence"),
                    "relationship_id": rid,
                })

        for node in canonical_nodes:
            model_id = str(node["canonical_id"])
            ancestors = ancestry(node["id"], parent_of, node_map)
            branch_path = [
                {"node_id": item["id"], "type": item["type"], "label": item.get("label")}
                for item in ancestors
                if item.get("type") in {"origin", "family", "branch"}
            ]
            terms = {model_id, str(node.get("label") or ""), family_label}
            terms.update(str(item.get("label") or "") for item in ancestors)
            terms.update(str(alias.get("label") or "") for alias in aliases[model_id])
            models[model_id] = {
                "family_id": family_id,
                "family_label": family_label,
                "model_label": node.get("label"),
                "branch_path": branch_path,
                "aliases": sorted(aliases[model_id], key=lambda item: str(item.get("label") or "").casefold()),
                "predecessor_ids": sorted(predecessor[model_id]),
                "successor_ids": sorted(successor[model_id]),
                "related_model_ids": [value for value in related_ids if value != model_id],
                "relationship_ids": sorted(incident[node["id"]]),
                "search_terms": sorted(term for term in terms if term),
            }

    payload = {
        "schema_version": 1,
        "semantics": "Identity and relationship context only. No specification, capability, evidence claim, community rating, or Report Card score inherits through lineage.",
        "model_count": len(models),
        "relationship_count": len(relationships),
        "models": models,
        "relationships": sorted(relationships, key=lambda item: item["id"]),
    }
    encoded = json.dumps(payload, sort_keys=True).lower()
    for forbidden in FORBIDDEN_INDEX_KEYS:
        if re.search(rf'"{re.escape(forbidden)}"\s*:', encoded):
            raise RuntimeError(f"lineage index unexpectedly contains forbidden key {forbidden!r}")
    return payload


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--site-root", type=Path, required=True)
    parser.add_argument("--families", type=Path, required=True)
    parser.add_argument("--additional-families", type=Path, action="append", default=[])
    parser.add_argument("--corrections", type=Path)
    parser.add_argument("--index-output", type=Path)
    args = parser.parse_args()

    source_paths = [args.families, *args.additional_families]
    payloads = [load_source(path) for path in source_paths]
    merged_payload = {
        "schema_version": 1,
        "rules": dict(REQUIRED_RULES),
        "source_sets": [
            {
                "source_class": payload.get("source_class", "maintained_lineages"),
                "family_count": len(payload.get("families", [])),
            }
            for payload in payloads
        ],
        "families": [family for payload in payloads for family in payload.get("families", [])],
    }

    devices = json.loads((args.site_root / "data/devices.json").read_text(encoding="utf-8"))
    known = {item["id"] for item in devices.get("records", [])}
    repo_root = args.families.resolve().parents[1]
    corrections = load_corrections(args.corrections)
    apply_corrections(merged_payload["families"], corrections, repo_root)

    model_to_family: dict[str, str] = {}
    family_ids: set[str] = set()
    for family in merged_payload["families"]:
        family_id = str(family.get("id") or "")
        if family_id in family_ids:
            raise RuntimeError(f"duplicate family id {family_id}")
        family_ids.add(family_id)
        validate_family(family, known, repo_root, model_to_family)
    if not model_to_family:
        raise RuntimeError("family tree data contains no canonical models")

    lineage_index = build_lineage_index(merged_payload["families"])
    if set(lineage_index["models"]) != set(model_to_family):
        raise RuntimeError("lineage index model coverage drifted from validated family-tree membership")

    public_payload = args.site_root / "data/family-trees.json"
    public_payload.write_text(json.dumps(merged_payload, indent=2) + "\n", encoding="utf-8")
    index_output = args.index_output or (args.site_root / "data/lineage-index.json")
    index_output.parent.mkdir(parents=True, exist_ok=True)
    index_output.write_text(json.dumps(lineage_index, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

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
    print(
        f"Family-tree surfaces validated: {len(family_ids)} families, {expected} canonical models, "
        f"{lineage_index['relationship_count']} relationships from {len(source_paths)} source sets; "
        f"audit_corrections={len(corrections)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
