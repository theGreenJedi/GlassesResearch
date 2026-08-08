#!/usr/bin/env python3
"""MkDocs hooks that derive accurate search metadata from visible page content."""

from __future__ import annotations

import html
import json
import re
from typing import Any

FAQ_HEADING = re.compile(r"^##\s+(?:\d+\.\s+)?(.+\?)\s*$", re.MULTILINE)
LINK = re.compile(r"!?\[([^\]]+)\]\([^\)]+\)")
HTML_TAG = re.compile(r"<[^>]+>")
MARKDOWN_MARKS = re.compile(r"[`*_~]+")
WHITESPACE = re.compile(r"\s+")


def _plain_text(markdown: str) -> str:
    """Reduce a Markdown fragment to plain text without inventing content."""
    text = LINK.sub(r"\1", markdown)
    text = re.sub(r"^\s{0,3}#{1,6}\s+", "", text, flags=re.MULTILINE)
    text = re.sub(r"^\s*>\s?", "", text, flags=re.MULTILINE)
    text = re.sub(r"^\s*[-*+]\s+", "", text, flags=re.MULTILINE)
    text = re.sub(r"^\s*\d+[.)]\s+", "", text, flags=re.MULTILINE)
    text = HTML_TAG.sub(" ", text)
    text = MARKDOWN_MARKS.sub("", text)
    return WHITESPACE.sub(" ", html.unescape(text)).strip()


def _first_description(markdown: str, page_title: str) -> str:
    """Use the first substantive prose paragraph as the page description."""
    blocks = re.split(r"\n\s*\n", markdown)
    for block in blocks:
        stripped = block.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if stripped.startswith(("```", "---", "!!!", "???")):
            continue
        text = _plain_text(stripped)
        if len(text) >= 40:
            if len(text) > 220:
                text = text[:217].rsplit(" ", 1)[0] + "..."
            return text
    return f"{page_title}: evidence-based smart-glasses research and documentation from GlassesResearch."


def _faq_schema(markdown: str, canonical_url: str) -> str | None:
    """Build FAQPage JSON-LD only when visible H2 question/answer pairs exist."""
    matches = list(FAQ_HEADING.finditer(markdown))
    if len(matches) < 2:
        return None

    entities: list[dict[str, Any]] = []
    for index, match in enumerate(matches):
        answer_start = match.end()
        answer_end = matches[index + 1].start() if index + 1 < len(matches) else len(markdown)
        answer_markdown = markdown[answer_start:answer_end].strip()
        answer = _plain_text(answer_markdown)
        question = _plain_text(match.group(1))
        if not question or not answer:
            continue
        entities.append(
            {
                "@type": "Question",
                "name": question,
                "acceptedAnswer": {"@type": "Answer", "text": answer},
            }
        )

    if len(entities) < 2:
        return None

    return json.dumps(
        {
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "@id": f"{canonical_url}#faq",
            "mainEntity": entities,
        },
        ensure_ascii=False,
        separators=(",", ":"),
    )


def on_page_markdown(markdown: str, page: Any, config: Any, files: Any) -> str:
    """Populate per-page metadata before Material renders the page."""
    page_title = page.title or config.site_name
    if not page.meta.get("description"):
        page.meta["description"] = _first_description(markdown, page_title)

    canonical_url = config.site_url.rstrip("/") + "/" + page.url
    faq_json = _faq_schema(markdown, canonical_url)
    if faq_json:
        page.meta["seo_faq_json"] = faq_json

    return markdown
