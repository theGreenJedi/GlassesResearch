"""Server-render curated model-hub navigation into canonical GLS pages."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "data" / "model-hubs.json"
MODEL_PATH = re.compile(r"^models/catalog/(gls-\d{4})\.md$")


def _load() -> dict:
    if not CONFIG.exists():
        return {}
    payload = json.loads(CONFIG.read_text(encoding="utf-8"))
    return payload.get("models") or {}


def _safe(item: object) -> str | None:
    if not isinstance(item, dict):
        return None
    url = item.get("url")
    if not isinstance(url, str) or not url.startswith("/") or url.startswith("//"):
        return None
    label = str(item.get("label") or url)
    note = str(item.get("note") or "").strip()
    return f"- [{label}]({url})" + (f" — {note}" if note else "")


def _hub_markdown(hub: dict) -> str:
    lines = [
        "## Research hub",
        "",
        "Everything GlassesResearch has attached to this model, with research leads kept distinct from verified product claims.",
    ]
    research = [*(hub.get("research") or []), *(hub.get("evidence") or [])]
    rendered = [line for item in research if (line := _safe(item))]
    if rendered:
        lines += ["", "### Go deeper", "", *rendered]

    grep_items = [line for item in (hub.get("grep") or []) if (line := _safe(item))]
    if grep_items:
        lines += ["", "### GREP examinations", "", *grep_items]

    questions = [hub.get("open_questions"), hub.get("research_backlog")]
    rendered_questions = [line for item in questions if (line := _safe(item))]
    if rendered_questions:
        lines += ["", "### What we still need to learn", "", *rendered_questions]
    return "\n".join(lines) + "\n\n"


def _neighbors_markdown(hub: dict) -> str | None:
    rendered = [line for item in (hub.get("neighbors") or []) if (line := _safe(item))]
    if not rendered:
        return None
    return (
        "## Lineage and ecosystem neighbors\n\n"
        "Curated identity, lineage, or ecosystem relationships take precedence over generic capability similarity. "
        "A relationship here does not imply identical hardware.\n\n"
        + "\n".join(rendered)
        + "\n\n"
    )


def _replace_related(markdown: str, replacement: str) -> str:
    pattern = re.compile(r"## Related models\n.*?(?=\n## |\Z)", re.DOTALL)
    return pattern.sub(replacement.rstrip(), markdown, count=1)


def on_page_markdown(markdown: str, page, config, files):
    src = getattr(getattr(page, "file", None), "src_uri", "")
    match = MODEL_PATH.match(src)
    if not match:
        return markdown

    model_id = match.group(1).upper()
    hub = _load().get(model_id)
    if not isinstance(hub, dict):
        return markdown

    marker = "## At a glance\n"
    if marker in markdown and "## Research hub\n" not in markdown:
        markdown = markdown.replace(marker, _hub_markdown(hub) + marker, 1)

    neighbors = _neighbors_markdown(hub)
    if neighbors:
        markdown = _replace_related(markdown, neighbors)
    return markdown
