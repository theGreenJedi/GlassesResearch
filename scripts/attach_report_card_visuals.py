#!/usr/bin/env python3
"""Attach governed model imagery to staged deep Report Card pages.

Source research files stay untouched. Only staged public pages are enhanced.
"""
from __future__ import annotations
import argparse, html, json, re
from pathlib import Path

GLS_HEADING = re.compile(r"^(#{2,3})\s+(GLS-\d{4})\s+[—-]\s+(.+?)\s*$", re.MULTILINE)

def figure(model_id: str, visual: dict) -> str:
    src = "/" + str(visual["primary_image"]).lstrip("/")
    alt = str(visual.get("alt") or f"{model_id} smart glasses")
    credit = str(visual.get("credit") or "").strip()
    rights = str(visual.get("rights_basis") or "").strip()
    source = str(visual.get("source_url") or "").strip()
    label = " · ".join(x for x in (credit, rights) if x)
    if source and label:
        label = f'<a href="{html.escape(source, quote=True)}" rel="nofollow noopener">{html.escape(label)}</a>'
    elif label:
        label = html.escape(label)
    elif source:
        label = f'<a href="{html.escape(source, quote=True)}" rel="nofollow noopener">Image source</a>'
    caption = f"<figcaption>{label}</figcaption>" if label else ""
    return (
        f'\n\n<figure class="gr-model-hero gr-report-card-hero" data-model-id="{model_id}">\n'
        f'  <img src="{html.escape(src, quote=True)}" alt="{html.escape(alt, quote=True)}" loading="lazy" decoding="async">\n'
        f'  {caption}\n</figure>'
    )

def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--site-root", type=Path, required=True)
    p.add_argument("--visuals", type=Path, required=True)
    a = p.parse_args()
    records = json.loads(a.visuals.read_text(encoding="utf-8")).get("records", {})
    report_dir = a.site_root / "docs" / "report-cards"
    pages = sections = images = 0
    for path in sorted(report_dir.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        touched = False
        def inject(match: re.Match) -> str:
            nonlocal sections, images, touched
            sections += 1
            model_id = match.group(2)
            visual = records.get(model_id, {})
            if visual.get("state") != "published" or not visual.get("primary_image"):
                return match.group(0)
            touched = True
            images += 1
            return match.group(0) + figure(model_id, visual)
        updated = GLS_HEADING.sub(inject, text)
        if touched:
            path.write_text(updated, encoding="utf-8")
            pages += 1
    print(f"Report Card visual pass: {sections} model sections inspected; {images} governed images attached across {pages} pages")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
