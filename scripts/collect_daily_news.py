#!/usr/bin/env python3
"""Collect durable wearable-HCI research candidates into the knowledge-flow queue.

Discovery is intentionally high-recall. Every candidate is classified after
collection by relationship, content type, triage priority, and routing target.
Nothing collected here is published automatically.
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
CONFIG = ROOT / "research" / "news-collector-sources.json"
OUTDIR = ROOT / "research" / "news-candidates"
UA = "GlassesResearch-KnowledgeIntake/3.0 (+https://glassesresearch.org/)"


def fetch(url: str, timeout: int = 20) -> bytes:
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": UA,
            "Accept": "application/rss+xml, application/atom+xml, text/html;q=0.9, */*;q=0.5",
        },
    )
    with urllib.request.urlopen(req, timeout=timeout) as response:
        return response.read()


def clean(text: str) -> str:
    text = re.sub(r"<script\b[^>]*>.*?</script>", " ", text, flags=re.I | re.S)
    text = re.sub(r"<style\b[^>]*>.*?</style>", " ", text, flags=re.I | re.S)
    text = re.sub(r"<[^>]+>", " ", text)
    return re.sub(r"\s+", " ", html.unescape(text)).strip()


def score(title: str, summary: str, keywords: list[str]) -> tuple[int, list[str]]:
    hay = f"{title} {summary}"
    hits = term_hits(hay, keywords)
    value = len(hits)
    if term_hits(hay, ("launch", "released", "announced", "preorder", "shipping", "discontinued", "recall")):
        value += 3
    if term_hits(hay, ("sdk", "api", "firmware", "security", "vulnerability", "open source")):
        value += 2
    if term_hits(hay, ("brain-computer", "brain computer", "neural", "emg", "eye tracking", "retinal", "haptic")):
        value += 1
    return value, hits


def item_id(url: str, title: str) -> str:
    return hashlib.sha256(f"{url}\n{title}".encode()).hexdigest()[:16]


def institution_test(title: str, summary: str) -> str:
    hay = f"{title} {summary}"
    durable = (
        "launch", "released", "announced", "sdk", "api", "firmware", "security", "vulnerability",
        "patent", "certification", "research", "study", "acquisition", "partnership", "discontinued",
        "recall", "open source", "brain-computer", "neural", "emg", "eye tracking", "waveguide",
        "microled", "micro-oled", "retinal", "haptic", "accessibility",
    )
    return "likely durable" if term_hits(hay, durable) else "review durability"


def enrich(candidate: dict, source_lane: str, glasses_terms: list[str], *, trusted_direct_source: bool = False) -> dict:
    enrich_candidate(
        candidate,
        source_lane=source_lane,
        extra_direct_terms=glasses_terms,
        trusted_direct_source=trusted_direct_source,
    )
    candidate["institution_test"] = institution_test(candidate["title"], candidate.get("summary", ""))
    return candidate


def parse_feed(
    blob: bytes,
    source: str,
    source_lane: str,
    keywords: list[str],
    glasses_terms: list[str],
    *,
    trusted_direct_source: bool = False,
) -> list[dict]:
    out = []
    try:
        root = ET.fromstring(blob)
    except ET.ParseError:
        return out
    entries = root.findall(".//item")
    atom = False
    if not entries:
        entries = root.findall("{http://www.w3.org/2005/Atom}entry")
        atom = True
    for entry in entries[:50]:
        if atom:
            ns = "{http://www.w3.org/2005/Atom}"
            title = clean(entry.findtext(ns + "title") or "")
            summary = clean(entry.findtext(ns + "summary") or entry.findtext(ns + "content") or "")
            link = ""
            link_element = entry.find(ns + "link")
            if link_element is not None:
                link = link_element.attrib.get("href", "")
            published = entry.findtext(ns + "published") or entry.findtext(ns + "updated") or ""
        else:
            title = clean(entry.findtext("title") or "")
            summary = clean(entry.findtext("description") or "")
            link = (entry.findtext("link") or "").strip()
            published = (entry.findtext("pubDate") or "").strip()
        if not title or not link:
            continue
        materiality, hits = score(title, summary, keywords)
        candidate = {
            "id": item_id(link, title),
            "title": title,
            "url": link,
            "source": source,
            "source_lane": source_lane,
            "published": published,
            "summary": summary[:1000],
            "materiality_score": materiality,
            "keyword_hits": hits,
            "status": "candidate",
        }
        out.append(
            enrich(
                candidate,
                source_lane,
                glasses_terms,
                trusted_direct_source=trusted_direct_source,
            )
        )
    return out


def google_news_url(query: str) -> str:
    encoded = urllib.parse.quote(query)
    return f"https://news.google.com/rss/search?q={encoded}+when:2d&hl=en-US&gl=US&ceid=US:en"


def manufacturer_candidate(url: str, blob: bytes, keywords: list[str], glasses_terms: list[str]) -> dict | None:
    text = blob.decode("utf-8", "ignore")
    title_match = re.search(r"<title[^>]*>(.*?)</title>", text, re.I | re.S)
    title = clean(title_match.group(1)) if title_match else urllib.parse.urlparse(url).netloc
    body = clean(text)[:15000]
    materiality, hits = score(title, body, keywords)
    if materiality == 0:
        return None
    candidate = {
        "id": item_id(url, title),
        "title": f"Manufacturer/source watch: {title}",
        "url": url,
        "source": "manufacturer-watch",
        "source_lane": "research_radar",
        "published": "",
        "summary": body[:1000],
        "materiality_score": max(1, materiality // 2),
        "keyword_hits": hits[:20],
        "status": "candidate",
    }
    return enrich(candidate, "research_radar", glasses_terms)


def prior_ids() -> set[str]:
    seen: set[str] = set()
    if not OUTDIR.exists():
        return seen
    for path in OUTDIR.glob("*.json"):
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
            seen.update(candidate.get("id", "") for candidate in payload.get("candidates", []))
        except Exception:
            continue
    seen.discard("")
    return seen


def main() -> int:
    cfg = json.loads(CONFIG.read_text(encoding="utf-8"))
    keywords = cfg["material_keywords"]
    glasses_terms = cfg["glasses_publication_terms"]
    candidates: list[dict] = []
    errors: list[dict] = []

    feeds: list[tuple[str, str, str, bool]] = []
    feeds += [
        (google_news_url(query), f"Google News: {query}", "core_glasses", False)
        for query in cfg["core_queries"]
    ]
    feeds += [
        (google_news_url(query), f"Google News: {query}", "adjacent_hci", False)
        for query in cfg["adjacent_hci_queries"]
    ]
    feeds += [(url, "direct-feed", "research_radar", True) for url in cfg["direct_feeds"]]

    for url, source, source_lane, trusted_direct_source in feeds:
        try:
            candidates.extend(
                parse_feed(
                    fetch(url),
                    source,
                    source_lane,
                    keywords,
                    glasses_terms,
                    trusted_direct_source=trusted_direct_source,
                )
            )
        except Exception as exc:
            errors.append({"url": url, "error": str(exc)[:300]})

    for url in cfg["manufacturer_pages"]:
        try:
            candidate = manufacturer_candidate(url, fetch(url), keywords, glasses_terms)
            if candidate:
                candidates.append(candidate)
        except Exception as exc:
            errors.append({"url": url, "error": str(exc)[:300]})

    dedup: dict[str, dict] = {}
    for candidate in candidates:
        key = re.sub(r"[?#].*$", "", candidate["url"]).rstrip("/").lower() or candidate["id"]
        if key not in dedup or candidate["materiality_score"] > dedup[key]["materiality_score"]:
            dedup[key] = candidate

    seen = prior_ids()
    new_items = [item for item in dedup.values() if item["id"] not in seen]
    precision_rejected = sum(item["relationship"] == "irrelevant" for item in new_items)
    ranked = [item for item in new_items if item["relationship"] != "irrelevant"]
    ranked.sort(
        key=lambda item: (
            {"high": 0, "normal": 1, "low": 2}[item["triage_priority"]],
            -item["materiality_score"],
            item["title"].lower(),
        )
    )
    ranked = [item for item in ranked if item["materiality_score"] >= 2][:200]

    if not ranked:
        print(
            f"No new intake candidates after classification; "
            f"{precision_rejected} noise results rejected; {len(errors)} source errors"
        )
        return 0

    now = dt.datetime.now(dt.timezone.utc)
    today = now.date().isoformat()
    OUTDIR.mkdir(parents=True, exist_ok=True)

    relationship_counts = {
        relationship: sum(1 for candidate in ranked if candidate["relationship"] == relationship)
        for relationship in RELATIONSHIPS
    }
    type_counts = {
        kind: sum(1 for candidate in ranked if kind in candidate["content_types"])
        for kind in CONTENT_TYPES
    }
    route_counts: dict[str, int] = {}
    for candidate in ranked:
        for route in candidate["routing_targets"]:
            route_counts[route] = route_counts.get(route, 0) + 1

    payload = {
        "schema": 3,
        "discovered_utc": now.isoformat(),
        "candidate_count": len(ranked),
        "precision_rejected_count": precision_rejected,
        "relationship_counts": relationship_counts,
        "type_counts": {key: value for key, value in type_counts.items() if value},
        "routing_counts": dict(sorted(route_counts.items())),
        "publication_policy": "discover broadly, classify, triage, verify, route, then publish; collection never authorizes publication",
        "collector_errors": errors,
        "candidates": ranked,
    }
    (OUTDIR / f"{today}.json").write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    lines = [
        f"# Knowledge intake — {today}",
        "",
        f"Collected **{len(ranked)}** new review candidates after precision filtering; rejected **{precision_rejected}** unrelated search results.",
        "",
        "## Relationship to smart glasses",
        "",
    ]
    for relationship in RELATIONSHIPS:
        if relationship_counts[relationship]:
            lines.append(f"- {relationship}: {relationship_counts[relationship]}")
    lines += ["", "## Content types", ""]
    for kind, count in type_counts.items():
        if count:
            lines.append(f"- {kind}: {count}")
    lines += [
        "",
        "**Flow:** discover → classify → triage → verify → route → publish → deliver.",
        "",
        "**Publishing rule:** collection is not publication. Direct/enabling items can enter editorial verification; speculative items route to Watching; adjacent items remain radar until a concrete glasses relationship exists.",
        "",
    ]
    for candidate in ranked[:80]:
        hits = ", ".join(candidate["keyword_hits"][:8]) or "context match"
        lines += [
            f"## {candidate['title']}",
            "",
            f"- Source: {candidate['url']}",
            f"- Relationship: {candidate['relationship']}",
            f"- Type: {', '.join(candidate['content_types'])}",
            f"- Routes: {', '.join(candidate['routing_targets'])}",
            f"- Triage: {candidate['triage_priority']}",
            f"- Publication eligible after verification: {'yes' if candidate['publication_eligible'] else 'no'}",
            f"- Disposition: {candidate['disposition']}",
            f"- Institution test: {candidate['institution_test']}",
            f"- Materiality score: {candidate['materiality_score']}",
            f"- Signals: {hits}",
            f"- Published by source: {candidate['published'] or 'not supplied by source'}",
            "",
        ]
    if errors:
        lines += ["## Collector warnings", ""] + [f"- {error['url']}: {error['error']}" for error in errors]
    (OUTDIR / f"{today}.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(
        f"Collected {len(ranked)} new candidates; rejected_noise={precision_rejected}; "
        f"relationships={relationship_counts}; routes={route_counts}; {len(errors)} source errors"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
