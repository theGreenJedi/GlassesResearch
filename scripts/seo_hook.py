#!/usr/bin/env python3
"""MkDocs hooks that derive accurate search metadata from visible page content."""

from __future__ import annotations

import html
import json
import re
from datetime import datetime
from typing import Any

FAQ_HEADING = re.compile(r"^##\s+(?:\d+\.\s+)?(.+\?)\s*$", re.MULTILINE)
PUBLISHED = re.compile(r"^\*\*Published:\*\*\s+(.+?)\s*$", re.MULTILINE)
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


def _core_schema(page_title: str, description: str, canonical_url: str, site_url: str) -> str:
    """Describe the project, site, current page, and a minimal visible breadcrumb trail."""
    root = site_url.rstrip("/") + "/"
    breadcrumbs = [
        {"@type": "ListItem", "position": 1, "name": "GlassesResearch", "item": root}
    ]
    if canonical_url != root:
        breadcrumbs.append(
            {"@type": "ListItem", "position": 2, "name": page_title, "item": canonical_url}
        )

    payload = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "Organization",
                "@id": f"{root}#organization",
                "name": "GlassesResearch",
                "url": root,
                "sameAs": ["https://github.com/theGreenJedi/GlassesResearch"],
            },
            {
                "@type": "WebSite",
                "@id": f"{root}#website",
                "name": "GlassesResearch",
                "url": root,
                "description": "Evidence-based research into AI eyeglasses, smart eyewear, and open user-controlled ecosystems.",
                "publisher": {"@id": f"{root}#organization"},
            },
            {
                "@type": "WebPage",
                "@id": f"{canonical_url}#webpage",
                "name": page_title,
                "url": canonical_url,
                "description": description,
                "isPartOf": {"@id": f"{root}#website"},
                "about": {"@id": f"{root}#organization"},
                "breadcrumb": {"@id": f"{canonical_url}#breadcrumb"},
            },
            {
                "@type": "BreadcrumbList",
                "@id": f"{canonical_url}#breadcrumb",
                "itemListElement": breadcrumbs,
            },
        ],
    }
    return json.dumps(payload, ensure_ascii=False, separators=(",", ":"))


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


def _model_schema(meta: dict[str, Any], description: str, canonical_url: str) -> str | None:
    """Describe canonical model subjects without inventing offers or ratings."""
    if not meta.get("model_id"):
        return None
    return json.dumps(
        {
            "@context": "https://schema.org",
            "@type": "Product",
            "@id": f"{canonical_url}#product",
            "name": meta.get("model_name"),
            "model": meta.get("model_id"),
            "brand": {"@type": "Brand", "name": meta.get("model_maker")},
            "category": meta.get("model_category"),
            "description": description,
            "url": canonical_url,
        },
        ensure_ascii=False,
        separators=(",", ":"),
    )


def _dataset_schema(meta: dict[str, Any], description: str, canonical_url: str, site_url: str) -> str | None:
    """Describe the generated open dataset only when the visible dataset page opts in."""
    if meta.get("dataset_schema") is not True:
        return None
    root = site_url.rstrip("/")
    payload: dict[str, Any] = {
        "@context": "https://schema.org",
        "@type": "Dataset",
        "@id": f"{canonical_url}#dataset",
        "name": meta.get("dataset_name") or "GlassesResearch Open Smart-Glasses Dataset",
        "description": description,
        "url": canonical_url,
        "version": meta.get("dataset_version"),
        "license": "https://opensource.org/license/mit",
        "creator": {"@type": "Organization", "name": "GlassesResearch", "url": root + "/"},
        "isAccessibleForFree": True,
        "keywords": ["smart glasses", "AI eyewear", "augmented reality", "wearable computing", "open dataset"],
        "distribution": [
            {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": root + "/data/public/models.json"},
            {"@type": "DataDownload", "encodingFormat": "text/csv", "contentUrl": root + "/data/public/models.csv"},
            {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": root + "/data/public/lineages.json"},
            {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": root + "/data/public/relationships.json"},
        ],
    }
    if meta.get("dataset_date_modified") and meta.get("dataset_date_modified") != "unknown":
        payload["dateModified"] = meta["dataset_date_modified"]
    if meta.get("dataset_record_count") is not None:
        payload["size"] = str(meta["dataset_record_count"]) + " canonical model records"
    return json.dumps(payload, ensure_ascii=False, separators=(",", ":"))


def _article_schema(
    markdown: str,
    page_title: str,
    description: str,
    canonical_url: str,
    site_url: str,
    source_uri: str,
) -> str | None:
    """Describe standalone verified Research & News articles from visible publication data."""
    if not source_uri.startswith("docs/news/articles/") or "**Status:** Verified" not in markdown:
        return None
    published = PUBLISHED.search(markdown)
    if not published:
        return None
    raw_date = published.group(1).strip()
    try:
        date_published = datetime.strptime(raw_date, "%B %d, %Y").date().isoformat()
    except ValueError:
        try:
            date_published = datetime.fromisoformat(raw_date.replace("Z", "+00:00")).date().isoformat()
        except ValueError:
            return None

    root = site_url.rstrip("/") + "/"
    return json.dumps(
        {
            "@context": "https://schema.org",
            "@type": "Article",
            "@id": f"{canonical_url}#article",
            "headline": page_title,
            "description": description,
            "url": canonical_url,
            "datePublished": date_published,
            "author": {"@id": f"{root}#organization"},
            "publisher": {"@id": f"{root}#organization"},
            "mainEntityOfPage": {"@id": f"{canonical_url}#webpage"},
            "isPartOf": {"@id": f"{root}#website"},
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
    page.meta["seo_core_json"] = _core_schema(
        page_title,
        page.meta["description"],
        canonical_url,
        config.site_url,
    )

    faq_json = _faq_schema(markdown, canonical_url)
    if faq_json:
        page.meta["seo_faq_json"] = faq_json

    model_json = _model_schema(page.meta, page.meta["description"], canonical_url)
    if model_json:
        page.meta["seo_model_json"] = model_json

    dataset_json = _dataset_schema(page.meta, page.meta["description"], canonical_url, config.site_url)
    if dataset_json:
        page.meta["seo_dataset_json"] = dataset_json

    source_uri = getattr(getattr(page, "file", None), "src_uri", "") or ""
    article_json = _article_schema(
        markdown,
        page_title,
        page.meta["description"],
        canonical_url,
        config.site_url,
        source_uri,
    )
    if article_json:
        page.meta["seo_article_json"] = article_json

    return markdown
