#!/usr/bin/env python3
"""Validate and stage the non-public GlassesResearch family-tree beta.

This experiment is intentionally isolated from the production site. It only enters
an MkDocs build when this script is invoked with --stage after prepare_site.py.
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
DATA_PATH = HERE / "family-trees.json"
GLS = re.compile(r"^GLS-\d{4}$")
ALLOWED_NODE_TYPES = {"family", "branch", "origin", "model", "alias"}
ALLOWED_RELATIONSHIPS = {
    "product_branch",
    "member_of",
    "successor",
    "derived_from",
    "alias_of",
    "rebrand_of",
    "variant_of",
    "unresolved",
}
ALLOWED_STATUS = {"established", "inferred", "unresolved"}
ALLOWED_CONFIDENCE = {"high", "medium", "low"}


def canonical_ids() -> set[str]:
    text = (ROOT / "models" / "THE_LIST.md").read_text(encoding="utf-8")
    return set(re.findall(r"\bGLS-\d{4}\b", text))


def validate(payload: dict) -> None:
    errors: list[str] = []
    if payload.get("schema_version") != 1:
        errors.append("schema_version must be 1")
    if payload.get("beta_only") is not True:
        errors.append("beta_only must be true")
    rules = payload.get("rules", {})
    if rules.get("public_site_enabled") is not False:
        errors.append("public_site_enabled must remain false in beta")
    if rules.get("score_inheritance") is not False:
        errors.append("score_inheritance must remain false")
    if rules.get("relationship_inheritance") is not False:
        errors.append("relationship_inheritance must remain false")

    known_gls = canonical_ids()
    family_ids: set[str] = set()
    for family in payload.get("families", []):
        fid = family.get("id")
        if not fid or fid in family_ids:
            errors.append(f"duplicate or missing family id: {fid!r}")
            continue
        family_ids.add(fid)
        nodes = family.get("nodes", [])
        edges = family.get("edges", [])
        node_map = {node.get("id"): node for node in nodes}
        if len(node_map) != len(nodes) or None in node_map:
            errors.append(f"{fid}: node ids must be unique and non-empty")
        root_id = family.get("root_id")
        if root_id not in node_map:
            errors.append(f"{fid}: root_id {root_id!r} is missing")

        for node in nodes:
            nid = node.get("id")
            if node.get("type") not in ALLOWED_NODE_TYPES:
                errors.append(f"{fid}/{nid}: invalid node type {node.get('type')!r}")
            if node.get("status") not in ALLOWED_STATUS:
                errors.append(f"{fid}/{nid}: invalid node status")
            canonical_id = node.get("canonical_id")
            if canonical_id:
                if not GLS.match(canonical_id):
                    errors.append(f"{fid}/{nid}: malformed canonical id {canonical_id}")
                elif canonical_id not in known_gls:
                    errors.append(f"{fid}/{nid}: canonical id {canonical_id} is not in THE_LIST")
                if node.get("type") != "model":
                    errors.append(f"{fid}/{nid}: only model nodes may carry canonical_id")

        incoming: dict[str, int] = {node_id: 0 for node_id in node_map}
        children: dict[str, list[str]] = {node_id: [] for node_id in node_map}
        edge_keys: set[tuple[str, str, str]] = set()
        for edge in edges:
            parent, child = edge.get("parent"), edge.get("child")
            key = (parent, child, edge.get("relationship"))
            if key in edge_keys:
                errors.append(f"{fid}: duplicate edge {key}")
            edge_keys.add(key)
            if parent not in node_map or child not in node_map:
                errors.append(f"{fid}: edge references missing node {parent!r}->{child!r}")
                continue
            if parent == child:
                errors.append(f"{fid}: self edge on {parent}")
            if edge.get("relationship") not in ALLOWED_RELATIONSHIPS:
                errors.append(f"{fid}: invalid relationship {edge.get('relationship')!r}")
            if edge.get("status") not in ALLOWED_STATUS:
                errors.append(f"{fid}: invalid edge status")
            if edge.get("confidence") not in ALLOWED_CONFIDENCE:
                errors.append(f"{fid}: invalid edge confidence")
            if edge.get("inheritance_allowed") is not False:
                errors.append(f"{fid}: edge {parent}->{child} must explicitly forbid evidence/score inheritance")
            evidence = edge.get("evidence", [])
            if not evidence:
                errors.append(f"{fid}: edge {parent}->{child} has no evidence path")
            for rel in evidence:
                path = ROOT / rel
                if not path.exists():
                    errors.append(f"{fid}: evidence path does not exist: {rel}")
            incoming[child] += 1
            children[parent].append(child)

        for node_id, count in incoming.items():
            if node_id == root_id and count != 0:
                errors.append(f"{fid}: root {root_id} must have no parent")
            elif node_id != root_id and count != 1:
                errors.append(f"{fid}: node {node_id} must have exactly one parent, found {count}")

        visiting: set[str] = set()
        visited: set[str] = set()
        def walk(node_id: str) -> None:
            if node_id in visiting:
                errors.append(f"{fid}: cycle detected at {node_id}")
                return
            if node_id in visited:
                return
            visiting.add(node_id)
            for child_id in children.get(node_id, []):
                walk(child_id)
            visiting.remove(node_id)
            visited.add(node_id)
        if root_id in node_map:
            walk(root_id)
        unreachable = set(node_map) - visited
        if unreachable:
            errors.append(f"{fid}: unreachable nodes from root: {sorted(unreachable)}")

    if errors:
        raise SystemExit("Family-tree beta validation failed:\n- " + "\n- ".join(errors))
    print(f"Family-tree beta validated: {len(family_ids)} representative families")


def build_markdown(payload: dict) -> str:
    encoded = json.dumps(payload, ensure_ascii=False).replace("</", "<\\/")
    return f'''# Family Tree Beta

!!! warning "Private build experiment"
    This page is generated only by the **family-tree beta workflow**. It is not part of the public GlassesResearch build or navigation. No lineage relationship shown here permits automatic inheritance of specifications, evidence, or Report Card scores.

The beta is testing three graph shapes: a branched corporate family (**Lucyd**), a technology-origin/brand/alias chain (**MemoMind**), and a dense OEM/rebrand family (**HeyCyan**).

<div class="family-tree-beta" data-family-tree-beta>
  <div class="ft-toolbar">
    <label>Family
      <select data-ft-family></select>
    </label>
    <label class="ft-check"><input type="checkbox" data-ft-aliases checked> Show retail aliases / rebrands</label>
    <label class="ft-check"><input type="checkbox" data-ft-inferred checked> Show inferred relationships</label>
  </div>
  <div class="ft-family-summary" data-ft-summary aria-live="polite"></div>
  <div class="ft-key" aria-label="Family tree legend">
    <span><b>GLS</b> canonical model</span>
    <span><b>Branch</b> product/platform branch</span>
    <span><b>Alias</b> retail or historical identity</span>
    <span><b>Dashed</b> inferred relationship</span>
  </div>
  <div class="ft-layout">
    <div class="ft-stage-scroll">
      <div class="ft-stage" data-ft-stage>
        <svg class="ft-links" data-ft-links aria-hidden="true"></svg>
        <div class="ft-levels" data-ft-levels></div>
      </div>
    </div>
    <aside class="ft-detail" data-ft-detail aria-live="polite">
      <h2>Inspect a node</h2>
      <p>Select a family member to see relationship type, evidence source, confidence, and the no-inheritance boundary.</p>
    </aside>
  </div>
</div>

<script id="family-tree-beta-data" type="application/json">{encoded}</script>
'''


def stage(payload: dict) -> None:
    staged = ROOT / ".site-src"
    if not staged.is_dir():
        raise SystemExit(".site-src is missing; run scripts/prepare_site.py before --stage")
    page_dir = staged / "__beta"
    page_dir.mkdir(parents=True, exist_ok=True)
    (page_dir / "FAMILY_TREE.md").write_text(build_markdown(payload), encoding="utf-8")

    css_target = staged / "docs" / "stylesheets" / "family-tree-beta.css"
    js_target = staged / "docs" / "javascripts" / "family-tree-beta.js"
    css_target.parent.mkdir(parents=True, exist_ok=True)
    js_target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(HERE / "family-tree-beta.css", css_target)
    shutil.copy2(HERE / "family-tree-beta.js", js_target)

    base = (ROOT / "mkdocs.yml").read_text(encoding="utf-8")
    css_anchor = "  - docs/stylesheets/community-review.css\n"
    js_anchor = "  - docs/javascripts/community-review-model.js\n"
    if css_anchor not in base or js_anchor not in base:
        raise SystemExit("mkdocs.yml asset anchors changed; beta refuses to guess")
    beta_config = base.replace(
        css_anchor,
        css_anchor + "  - docs/stylesheets/family-tree-beta.css\n",
    ).replace(
        js_anchor,
        js_anchor + "  - docs/javascripts/family-tree-beta.js\n",
    )
    beta_config = beta_config.replace(
        "site_url: https://glassesresearch.org/",
        "site_url: http://127.0.0.1:4173/",
    )
    (ROOT / "mkdocs.family-tree-beta.yml").write_text(beta_config, encoding="utf-8")
    print("Staged private family-tree beta at /__beta/FAMILY_TREE/")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--stage", action="store_true")
    args = parser.parse_args()
    payload = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    validate(payload)
    if args.stage:
        stage(payload)


if __name__ == "__main__":
    main()
