#!/usr/bin/env python3
"""Render curated model-hub associations into staged canonical model pages.

Hub associations are navigation metadata, not evidence. This script only links to
existing GlassesResearch material and never upgrades a research lead into a
product claim.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def internal_url(value: object) -> bool:
    return isinstance(value, str) and value.startswith("/") and not value.startswith("//")


def item_line(item: dict) -> str | None:
    url = item.get("url")
    if not internal_url(url):
        return None
    label = str(item.get("label") or url)
    note = str(item.get("note") or "").strip()
    suffix = f" — {note}" if note else ""
    return f"- [{label}]({url}){suffix}"


def render_hub(hub: dict) -> str:
    lines = [
        "## Research hub",
        "",
        "Everything GlassesResearch has attached to this model, with research leads kept distinct from verified product claims.",
    ]

    research = [*(hub.get("research") or []), *(hub.get("evidence") or [])]
    rendered = [line for item in research if isinstance(item, dict) for line in [item_line(item)] if line]
    if rendered:
        lines += ["", "### Go deeper", "", *rendered]

    grep_items = [item for item in (hub.get("grep") or []) if isinstance(item, dict)]
    rendered_grep = [line for item in grep_items for line in [item_line(item)] if line]
    if rendered_grep:
        lines += ["", "### GREP examinations", "", *rendered_grep]

    questions = [hub.get("open_questions"), hub.get("research_backlog")]
    rendered_questions = [line for item in questions if isinstance(item, dict) for line in [item_line(item)] if line]
    if rendered_questions:
        lines += ["", "### What we still need to learn", "", *rendered_questions]

    return "\n".join(lines) + "\n\n"


def render_neighbors(hub: dict) -> str | None:
    neighbors = [item for item in (hub.get("neighbors") or []) if isinstance(item, dict)]
    rendered = [line for item in neighbors for line in [item_line(item)] if line]
    if not rendered:
        return None
    return (
        "## Lineage and ecosystem neighbors\n\n"
        "Curated identity, lineage, or ecosystem relationships take precedence over generic capability similarity. "
        "A relationship here does not imply identical hardware.\n\n"
        + "\n".join(rendered)
        + "\n\n"
    )


def replace_related_section(text: str, replacement: str) -> str:
    start = text.find("## Related models\n")
    if start < 0:
        return text
    next_heading = text.find("\n## ", start + len("## Related models\n"))
    if next_heading < 0:
        return text[:start] + replacement.rstrip() + "\n"
    return text[:start] + replacement.rstrip() + "\n" + text[next_heading:]


def apply(site_root: Path, config: Path) -> int:
    payload = load(config)
    models = payload.get("models") or {}
    changed = 0
    for model_id, hub in models.items():
        if not isinstance(hub, dict):
            continue
        page = site_root / "models" / "catalog" / f"{model_id.lower()}.md"
        if not page.exists():
            raise FileNotFoundError(f"Hub target does not exist: {page}")
        text = page.read_text(encoding="utf-8")
        marker = "## At a glance\n"
        if marker not in text:
            raise ValueError(f"Canonical model page lacks expected At a glance section: {page}")
        if "## Research hub\n" not in text:
            text = text.replace(marker, render_hub(hub) + marker, 1)
        neighbors = render_neighbors(hub)
        if neighbors:
            text = replace_related_section(text, neighbors)
        page.write_text(text, encoding="utf-8")
        changed += 1
    return changed


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--site-root", type=Path, required=True)
    parser.add_argument("--config", type=Path, required=True)
    args = parser.parse_args()
    count = apply(args.site_root, args.config)
    print(f"Rendered curated research hubs into {count} canonical model page(s)")


if __name__ == "__main__":
    main()
