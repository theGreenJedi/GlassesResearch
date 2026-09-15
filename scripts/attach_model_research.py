#!/usr/bin/env python3
"""Attach model-bound research and community-scour indexes to canonical model pages.

Research remains canonical in its own document. Model cards are touchstones:
formal/community research is indexed there, while retained scour findings are
aggregated behind one per-model link so cards remain compact as findings grow.
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

RESEARCH_ROOTS = (
    "research/investigations",
    "research/community-research",
    "research/claims",
    "docs/community-research",
)
SCOUR_ROOTS = (
    "research/community-research",
    "docs/community-research",
)
SCOUR_INDEX_DIR = "research/community-research/by-model"
SCOUR_INDEX_MARKER = "<!-- generated-model-scour-index -->"


def public_url(site_root: Path, path: Path) -> str:
    rel = path.relative_to(site_root).with_suffix("")
    return "/" + rel.as_posix().strip("/") + "/"


def document(path: Path, site_root: Path) -> dict[str, object] | None:
    if path.name.lower() in {"readme.md", "index.md"}:
        return None
    text = path.read_text(encoding="utf-8")
    ids = sorted(set(MODEL_ID_RE.findall(text)))
    if not ids:
        return None
    title_match = TITLE_RE.search(text)
    evidence_match = EVIDENCE_RE.search(text)
    status_match = STATUS_RE.search(text)
    meta = []
    if evidence_match:
        meta.append(evidence_match.group(1).strip())
    if status_match:
        meta.append(status_match.group(1).strip())
    return {
        "ids": ids,
        "title": title_match.group(1).strip() if title_match else path.stem.replace("_", " "),
        "url": public_url(site_root, path),
        "meta": " · ".join(meta),
    }


def collect(site_root: Path, roots: tuple[str, ...]) -> dict[str, list[dict[str, str]]]:
    bindings: dict[str, list[dict[str, str]]] = {}
    seen: set[tuple[str, str]] = set()
    for root_name in roots:
        root = site_root / root_name
        if not root.exists():
            continue
        for path in sorted(root.rglob("*.md")):
            # Never ingest generated per-model indexes as source findings.
            if SCOUR_INDEX_MARKER in path.read_text(encoding="utf-8", errors="replace"):
                continue
            row = document(path, site_root)
            if not row:
                continue
            for model_id in row["ids"]:
                key = (model_id, row["url"])
                if key in seen:
                    continue
                seen.add(key)
                bindings.setdefault(model_id, []).append({
                    "title": str(row["title"]), "url": str(row["url"]), "meta": str(row["meta"])
                })
    return bindings


def build_scour_indexes(site_root: Path, scour: dict[str, list[dict[str, str]]]) -> dict[str, dict[str, object]]:
    out = site_root / SCOUR_INDEX_DIR
    out.mkdir(parents=True, exist_ok=True)
    # Staged builds are disposable; remove stale generated model indexes.
    for path in out.glob("gls-*.md"):
        path.unlink()
    indexes: dict[str, dict[str, object]] = {}
    for model_id, rows in sorted(scour.items()):
        if not rows:
            continue
        ordered = sorted(rows, key=lambda item: (item["title"].lower(), item["url"]))
        lines = [
            f"# Community / Scour Findings — {model_id}", "", SCOUR_INDEX_MARKER, "",
            f"All retained community/scour findings currently bound to **{model_id}**. "
            "These remain attributed community evidence unless separately reproduced by GlassesResearch.", "",
        ]
        for row in ordered:
            suffix = f" — {row['meta']}" if row["meta"] else ""
            lines.append(f"- [{row['title']}]({row['url']}){suffix}")
        path = out / f"{model_id.lower()}.md"
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        indexes[model_id] = {"count": len(ordered), "url": public_url(site_root, path)}
    return indexes


def attach(page: Path, rows: list[dict[str, str]], scour_index: dict[str, object] | None) -> None:
    text = SECTION_RE.sub("", page.read_text(encoding="utf-8"))
    links = []
    # Community/scour source objects are represented by the aggregate link below;
    # avoid reprinting every individual finding on the model card.
    scour_urls = {row["url"] for row in rows if "/community-research/" in row["url"]}
    for row in sorted(rows, key=lambda item: (item["title"].lower(), item["url"])):
        if row["url"] in scour_urls:
            continue
        suffix = f" — {row['meta']}" if row["meta"] else ""
        links.append(f"- [{row['title']}]({row['url']}){suffix}")
    if scour_index:
        count = int(scour_index["count"])
        links.append(f"- [Community / Scour Findings ({count})]({scour_index['url']}) — all retained community findings bound to this model")
    if links:
        body = "\n".join(links)
    else:
        body = "No admitted model-specific research or retained scour finding is currently bound to this model."
    section = (
        "\n## Related Research\n\n"
        "Research is maintained in its canonical source; this card is the touchstone for model-bound material. "
        "Community/scour findings are grouped behind one model-specific index. Evidence state remains attached to each source.\n\n"
        + body + "\n"
    )
    marker = "\n## Sources\n"
    if marker not in text:
        raise ValueError(f"{page}: expected Sources section")
    page.write_text(text.replace(marker, section + marker, 1), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--site-root", type=Path, required=True)
    args = parser.parse_args()
    root = args.site_root
    bindings = collect(root, RESEARCH_ROOTS)
    scour = collect(root, SCOUR_ROOTS)
    scour_indexes = build_scour_indexes(root, scour)
    pages = sorted((root / "models" / "catalog").glob("gls-*.md"))
    if not pages:
        raise SystemExit("No generated canonical model pages found")
    linked_models = linked_objects = 0
    for page in pages:
        model_id = page.stem.upper()
        rows = bindings.get(model_id, [])
        attach(page, rows, scour_indexes.get(model_id))
        if rows:
            linked_models += 1
            linked_objects += len(rows)
    print(
        f"Attached/indexed {linked_objects} research objects across {linked_models} model cards; "
        f"generated {len(scour_indexes)} per-model community/scour indexes ({len(pages)} cards audited)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
