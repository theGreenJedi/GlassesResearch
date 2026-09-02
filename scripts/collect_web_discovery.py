#!/usr/bin/env python3
"""High-recall ordinary-web discovery for GlassesResearch.

This intentionally imitates a curious human searching the wider web: products,
reviews, videos, rumors, developer tools, research, optics, retail, community,
manufacturer catalogs, and adjacent wearables. Classification happens after
discovery, and nothing collected here is published automatically.

The discovery boundary is intentionally permissive: classifier judgments are
retained as metadata and passed downstream to editorial triage rather than used
to erase observations before the desk can inspect them.
"""
from __future__ import annotations

import datetime as dt
import hashlib
import html
import json
import re
import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

from knowledge_flow import CONTENT_TYPES, RELATIONSHIPS, enrich_candidate, term_hits

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "research" / "discovery-sources.json"
OUTDIR = ROOT / "research" / "discovery-candidates"
UA = "GlassesResearch-Discovery/2.1 (+https://glassesresearch.org/)"

EXTRA_DIRECT_TERMS = (
    "maverick", "everysight", "inmo", "dymesty", "latitude52", "latitude 52",
    "halliday", "lucyd", "heycyan", "mentra", "xreal", "rayneo", "rokid",
    "viture", "even realities", "brilliant labs", "vuzix", "solos airgo",
    "project aria",
)
MATERIAL_TERMS = (
    "launch", "released", "announced", "preorder", "shipping", "review",
    "hands-on", "sdk", "api", "firmware", "open source", "github", "teardown",
    "privacy", "lawsuit", "patent", "rumor", "waveguide", "microled",
    "prescription", "oem", "odm", "rebrand", "research", "study",
)


def fetch(url: str, timeout: int = 25) -> bytes:
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": UA,
            "Accept": "application/rss+xml, application/xml, text/html;q=0.9, */*;q=0.5",
        },
    )
    with urllib.request.urlopen(req, timeout=timeout) as response:
        return response.read()


def clean(value: str) -> str:
    value = re.sub(r"<script\b[^>]*>.*?</script>", " ", value, flags=re.I | re.S)
    value = re.sub(r"<style\b[^>]*>.*?</style>", " ", value, flags=re.I | re.S)
    value = re.sub(r"<[^>]+>", " ", value)
    return re.sub(r"\s+", " ", html.unescape(value)).strip()


def normalize_url(url: str) -> str:
    parsed = urllib.parse.urlsplit(url)
    return urllib.parse.urlunsplit(
        (parsed.scheme.lower(), parsed.netloc.lower(), parsed.path.rstrip("/"), "", "")
    )


def candidate_id(url: str, title: str) -> str:
    return hashlib.sha256(f"{normalize_url(url)}\n{title.lower()}".encode()).hexdigest()[:16]


def bing_rss(query: str) -> str:
    encoded = urllib.parse.quote(query)
    return f"https://www.bing.com/search?q={encoded}&format=rss&count=30"


def source_lane(channel: str) -> str:
    if channel == "adjacent":
        return "adjacent_hci"
    if channel == "research":
        return "research"
    return "research_radar"


def materiality(title: str, summary: str, channel: str) -> tuple[int, list[str]]:
    hits = term_hits(f"{title} {summary}", MATERIAL_TERMS)
    base = {
        "broad_web": 2,
        "retail": 2,
        "developer": 3,
        "research": 2,
        "community": 1,
        "adjacent": 1,
        "manufacturer_catalog": 3,
    }.get(channel, 1)
    return base + len(hits), hits


def make_candidate(
    *,
    title: str,
    url: str,
    summary: str,
    channel: str,
    query: str = "",
    source: str = "",
    trusted_direct_source: bool = False,
) -> dict:
    score, hits = materiality(title, summary, channel)
    candidate = {
        "id": candidate_id(url, title),
        "title": title,
        "url": url,
        "summary": summary[:1200],
        "discovery_channel": channel,
        "query": query,
        "source": source or channel,
        "source_lane": source_lane(channel),
        "materiality_score": score,
        "keyword_hits": hits,
        "status": "candidate",
        "disposition": "collected",
    }
    return enrich_candidate(
        candidate,
        source_lane=source_lane(channel),
        extra_direct_terms=EXTRA_DIRECT_TERMS,
        trusted_direct_source=trusted_direct_source,
        channel_hint=channel,
    )


def parse_rss(blob: bytes, channel: str, query: str) -> list[dict]:
    try:
        root = ET.fromstring(blob)
    except ET.ParseError:
        return []
    out: list[dict] = []
    for item in root.findall(".//item")[:30]:
        title = clean(item.findtext("title") or "")
        url = (item.findtext("link") or "").strip()
        summary = clean(item.findtext("description") or "")
        if not title or not url:
            continue
        out.append(
            make_candidate(
                title=title,
                url=url,
                summary=summary,
                channel=channel,
                query=query,
                source="Bing web RSS",
            )
        )
    return out


def same_domain_product_links(base_url: str, blob: bytes) -> list[dict]:
    text = blob.decode("utf-8", "ignore")
    base = urllib.parse.urlsplit(base_url)
    seen: set[str] = set()
    out: list[dict] = []
    link_re = re.compile(r"<a\b[^>]*href=[\"']([^\"']+)[\"'][^>]*>(.*?)</a>", re.I | re.S)
    for href, anchor_html in link_re.findall(text):
        url = urllib.parse.urljoin(base_url, html.unescape(href))
        parsed = urllib.parse.urlsplit(url)
        if parsed.scheme not in {"http", "https"} or parsed.netloc.lower() != base.netloc.lower():
            continue
        normalized = normalize_url(url)
        if normalized in seen:
            continue
        anchor = clean(anchor_html)
        hay = f"{anchor} {parsed.path}"
        product_signal = bool(
            term_hits(
                hay,
                (
                    "glass", "glasses", "eyewear", "spectacle", "maverick", "inmo",
                    "cook", "berlin", "milan", "product", "collection", "developer",
                    "sdk", "support",
                ),
            )
        )
        if not product_signal:
            continue
        seen.add(normalized)
        title = anchor or parsed.path.rsplit("/", 1)[-1].replace("-", " ") or base.netloc
        out.append(
            make_candidate(
                title=f"Manufacturer catalog lead: {title}",
                url=url,
                summary=f"Same-domain catalog/developer link discovered from {base_url}",
                channel="manufacturer_catalog",
                source=base_url,
                trusted_direct_source=True,
            )
        )
        if len(out) >= 100:
            break
    return out


def prior_ids() -> set[str]:
    seen: set[str] = set()
    if not OUTDIR.exists():
        return seen
    for path in OUTDIR.glob("*.json"):
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
            seen.update(str(item.get("id", "")) for item in payload.get("candidates", []))
        except Exception:
            continue
    seen.discard("")
    return seen


def main() -> int:
    cfg = json.loads(CONFIG.read_text(encoding="utf-8"))
    candidates: list[dict] = []
    errors: list[dict] = []

    lanes = {
        "broad_web": cfg.get("broad_web_queries", []),
        "retail": cfg.get("retail_discovery_queries", []),
        "developer": cfg.get("developer_discovery_queries", []),
        "research": cfg.get("research_discovery_queries", []),
        "community": cfg.get("community_discovery_queries", []),
        "adjacent": cfg.get("adjacent_discovery_queries", []),
    }
    for channel, queries in lanes.items():
        for query in queries:
            url = bing_rss(query)
            try:
                candidates.extend(parse_rss(fetch(url), channel, query))
            except Exception as exc:
                errors.append(
                    {"channel": channel, "query": query, "url": url, "error": str(exc)[:300]}
                )

    for url in cfg.get("manufacturer_catalog_pages", []):
        try:
            blob = fetch(url)
            body = clean(blob.decode("utf-8", "ignore"))[:1200]
            candidates.append(
                make_candidate(
                    title=f"Manufacturer catalog watch: {urllib.parse.urlsplit(url).netloc}",
                    url=url,
                    summary=body,
                    channel="manufacturer_catalog",
                    source="configured manufacturer catalog",
                    trusted_direct_source=True,
                )
            )
            candidates.extend(same_domain_product_links(url, blob))
        except Exception as exc:
            errors.append(
                {"channel": "manufacturer_catalog", "url": url, "error": str(exc)[:300]}
            )

    dedup: dict[str, dict] = {}
    for item in candidates:
        key = normalize_url(item["url"])
        if key not in dedup:
            dedup[key] = item
        else:
            prior = dedup[key]
            channels = sorted(
                set(str(prior.get("discovery_channel", "")).split("+"))
                | {item["discovery_channel"]}
            )
            prior["discovery_channel"] = "+".join(channels)
            if item.get("query") and item["query"] not in str(prior.get("query", "")):
                prior["query"] = "; ".join(
                    value for value in [str(prior.get("query", "")), item["query"]] if value
                )
            if item["triage_priority"] == "high" and prior["triage_priority"] != "high":
                dedup[key] = item

    seen = prior_ids()
    new_items = [item for item in dedup.values() if item["id"] not in seen]
    classifier_irrelevant = sum(item["relationship"] == "irrelevant" for item in new_items)
    ranked = list(new_items)
    ranked.sort(
        key=lambda item: (
            item["relationship"] == "irrelevant",
            {"high": 0, "normal": 1, "low": 2}[item["triage_priority"]],
            -item["materiality_score"],
            item["title"].lower(),
        )
    )
    ranked = ranked[:800]

    if not ranked:
        print(f"No new web-discovery observations; {len(errors)} source errors")
        return 0

    now = dt.datetime.now(dt.timezone.utc)
    day = now.date().isoformat()
    OUTDIR.mkdir(parents=True, exist_ok=True)

    channel_counts: dict[str, int] = {}
    relationship_counts = {
        relationship: sum(1 for item in ranked if item["relationship"] == relationship)
        for relationship in RELATIONSHIPS
    }
    type_counts = {
        kind: sum(1 for item in ranked if kind in item["content_types"])
        for kind in CONTENT_TYPES
    }
    route_counts: dict[str, int] = {}
    for item in ranked:
        for channel in item["discovery_channel"].split("+"):
            channel_counts[channel] = channel_counts.get(channel, 0) + 1
        for route in item["routing_targets"]:
            route_counts[route] = route_counts.get(route, 0) + 1

    payload = {
        "schema": 3,
        "discovered_utc": now.isoformat(),
        "candidate_count": len(ranked),
        "classifier_irrelevant_count": classifier_irrelevant,
        "precision_rejected_count": 0,
        "channel_counts": dict(sorted(channel_counts.items())),
        "relationship_counts": relationship_counts,
        "type_counts": {key: value for key, value in type_counts.items() if value},
        "routing_counts": dict(sorted(route_counts.items())),
        "policy": cfg.get("policy", {}),
        "collector_errors": errors,
        "candidates": ranked,
    }
    (OUTDIR / f"{day}.json").write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    lines = [
        f"# Web discovery intake — {day}",
        "",
        f"Retained **{len(ranked)}** deduplicated search observations for downstream triage; the classifier marked **{classifier_irrelevant}** as likely irrelevant, but discovery did not erase them.",
        "",
        "**Flow:** discover → retain → classify → triage → verify → route → publish → deliver.",
        "",
        "**Rule:** discovery is not verification. Classifier judgments prioritize downstream review; they do not authorize publication and they do not delete an observation at the discovery boundary.",
        "",
        "## Search surfaces",
        "",
    ]
    for channel, count in sorted(channel_counts.items()):
        lines.append(f"- {channel}: {count}")
    lines += ["", "## Relationship", ""]
    for relationship in RELATIONSHIPS:
        if relationship_counts[relationship]:
            lines.append(f"- {relationship}: {relationship_counts[relationship]}")
    lines.append("")
    for item in ranked[:120]:
        lines += [
            f"## {item['title']}",
            "",
            f"- URL: {item['url']}",
            f"- Search surface: {item['discovery_channel']}",
            f"- Query/source: {item.get('query') or item.get('source')}",
            f"- Relationship: {item['relationship']}",
            f"- Type: {', '.join(item['content_types'])}",
            f"- Routes: {', '.join(item['routing_targets'])}",
            f"- Triage: {item['triage_priority']}",
            "",
        ]
    if errors:
        lines += ["## Collector warnings", ""] + [
            f"- {error.get('channel')}: {error.get('url')}: {error['error']}"
            for error in errors
        ]
    (OUTDIR / f"{day}.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(
        f"Retained {len(ranked)} web-discovery observations; "
        f"classifier_irrelevant={classifier_irrelevant}; relationships={relationship_counts}; "
        f"routes={route_counts}; {len(errors)} source errors"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
