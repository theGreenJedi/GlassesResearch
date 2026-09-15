#!/usr/bin/env python3
"""Attach model-bound research links to generated canonical model pages.

Research remains canonical in its own document. Model cards act as an index:
any admitted research document in the configured research roots that explicitly
names a GLS stable ID is automatically linked from that model's canonical card.
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

MODEL_ID_RE = re.compile(r"\bGLS-\d{4}\b")
TITLE_RE = re.compile(r"^#\s+(.+?)\s*$", re.MULTILINE)
EVIDENCE_RE = re.compile(r"^\*\*Evidence lane:\*\*\s*(.+?)\s*$", re.MULTILINE)
STATUS_RE = re.compile(r"^\*\*Status:\*\*\s*(.+?)\s*$", re.MULTILINE)
SECTION_RE = re.compile(r"\n## Related Research\n.*?(?=\n## |\Z)", re.DOTALL)

# Deliberately scoped to admitted model-specific research surfaces. General
# methodology/process documents under research/ are not model evidence merely
# because they happen to mention an example GLS identifier.
RESEARCH_ROOTS = (
    "research/investigations",
    "research/community-research",
    "research/claims",
    "docs/community-research",
)


def public_url(site_root: Path, path: Path) -> str:
    rel = path.relative_to(site_root).with_suffix("")
    return "/" + rel.as_posix().strip("/") + "/"


def collect(site_root: Path) -> dict[str, list[dict[str, str]]]:
    bindings: dict[str, list[dict[str, str]]] = {}
    seen: set[tuple[str, str]] = set()
    for root_name in RESEARCH_ROOTS:
        root = site_root / root_name
        if not root.exists():
            continue
        for path in sorted(root.rglob("*.md")):
            if path.name.lower() in {"readme.md", "index.md"}:
                continue
            text = path.read_text(encoding="utf-8")
            ids = sorted(set(MODEL_ID_RE.findall(text)))
            if not ids:
                continue
            title_match = TITLE_RE.search(text)
            title = title_match.group(1).strip() if title_match else path.stem.replace("_", " ")
            evidence_match = EVIDENCE_RE.search(text)
            status_match = STATUS_RE.search(text)
            meta = []
            if evidence_match:
                meta.append(evidence_match.group(1).strip())
            if status_match:
                meta.append(status_match.group(1).strip())
            url = public_url(site_root, path)
            for model_id in ids:
                key = (model_id, url)
                if key in seen:
                    continue
                seen.add(key)
                bindings.setdefault(model_id, []).append({
                    "title": title,
                    "url": url,
                    "meta": " · ".join(meta),
                })
    return bindings


def attach(page: Path, model_id: str, rows: list[dict[str, str]]) -> None:
    text = page.read_text(encoding="utf-8")
    text = SECTION_RE.sub("", text)
    if rows:
        links = []
        for row in sorted(rows, key=lambda item: (item["title"].lower(), item["url"])):
            suffix = f" — {row['meta']}" if row["meta"] else ""
            links.append(f"- [{row['title']}]({row['url']}){suffix}")
        section = (
            "\n## Related Research\n\n"
            "Research is maintained in its canonical source; this card indexes every admitted "
            "model-bound research object. Evidence state remains attached to the source.\n\n"
            + "\n".join(links)
            + "\n"
        )
    else:
        section = (
            "\n## Related Research\n\n"
            "No admitted model-specific research object is currently bound to this model.\n"
        )
    marker = "\n## Sources\n"
    if marker not in text:
        raise ValueError(f"{page}: expected Sources section")
    text = text.replace(marker, section + marker, 1)
    page.write_text(text, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--site-root", type=Path, required=True)
    args = parser.parse_args()
    root = args.site_root
    bindings = collect(root)
    catalog = root / "models" / "catalog"
    pages = sorted(catalog.glob("gls-*.md"))
    if not pages:
        raise SystemExit("No generated canonical model pages found")
    linked_models = 0
    linked_objects = 0
    for page in pages:
        model_id = page.stem.upper()
        rows = bindings.get(model_id, [])
        attach(page, model_id, rows)
        if rows:
            linked_models += 1
            linked_objects += len(rows)
    print(f"Attached {linked_objects} research links across {linked_models} model cards ({len(pages)} cards audited)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
