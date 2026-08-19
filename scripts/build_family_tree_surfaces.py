#!/usr/bin/env python3
"""Inject optional family-tree triggers into staged model and Report Card pages."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ICON = '''<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 3v5m0 0-5 4m5-4 5 4M7 12v5m10-5v5M4 17h6m4 0h6" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>'''


def button(model_id: str) -> str:
    return (
        f'<button class="family-tree-trigger" type="button" data-family-tree-model="{model_id}" '
        f'aria-label="View family tree for {model_id}" title="View family tree">{ICON}</button>'
    )


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

    devices = json.loads((args.site_root / "data/devices.json").read_text(encoding="utf-8"))
    known = {item["id"] for item in devices.get("records", [])}
    model_to_family: dict[str, str] = {}
    for family in payload.get("families", []):
        ids = []
        for node in family.get("nodes", []):
            model_id = node.get("canonical_id")
            if not model_id:
                continue
            if model_id not in known:
                raise RuntimeError(f"family tree references non-canonical model {model_id}")
            if model_id in model_to_family:
                raise RuntimeError(f"model {model_id} appears in multiple family trees")
            model_to_family[model_id] = family["id"]
            ids.append(model_id)
        if not ids:
            raise RuntimeError(f"family {family.get('id')} has no canonical models")
        nodes = {node["id"] for node in family.get("nodes", [])}
        for edge in family.get("edges", []):
            if edge.get("parent") not in nodes or edge.get("child") not in nodes:
                raise RuntimeError(f"family {family.get('id')} has an edge to a missing node")
            if edge.get("inheritance_allowed") is not False:
                raise RuntimeError(f"family {family.get('id')} edge permits inheritance")
            if not edge.get("evidence"):
                raise RuntimeError(f"family {family.get('id')} edge lacks evidence")

    injected_models = 0
    for model_id in sorted(model_to_family):
        page = args.site_root / "models/catalog" / f"{model_id.lower()}.md"
        if not page.exists():
            raise RuntimeError(f"generated model page missing for {model_id}")
        text = page.read_text(encoding="utf-8")
        if "data-family-tree-model" in text:
            continue
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
        if match and match.group(1) in model_to_family and "data-family-tree-model" not in line:
            model_id = match.group(1)
            line = line.replace("</a>", f"</a> {button(model_id)}", 1)
            injected_rows += 1
        lines.append(line)
    report.write_text("\n".join(lines) + ("\n" if text.endswith("\n") else ""), encoding="utf-8")

    print(f"Family-tree surfaces: {injected_models} model pages, {injected_rows} Report Card rows")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
