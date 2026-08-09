#!/usr/bin/env python3
"""Collect durable wearable-HCI research candidates into a review queue.

The collector observes broadly and publishes nothing automatically. Glasses-related
items may be considered for promotion after review; adjacent HCI items are retained
as research radar until a concrete glasses connection exists.
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

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "research" / "news-collector-sources.json"
OUTDIR = ROOT / "research" / "news-candidates"
UA = "GlassesResearch-KnowledgeIntake/2.0 (+https://glassesresearch.org/)"


def fetch(url: str, timeout: int = 20) -> bytes:
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": UA,
            "Accept": "application/rss+xml, application/atom+xml, text/html;q=0.9, */*;q=0.5",
        },
    )
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def clean(text: str) -> str:
    text = re.sub(r"<script\b[^>]*>.*?</script>", " ", text, flags=re.I | re.S)
    text = re.sub(r"<style\b[^>]*>.*?</style>", " ", text, flags=re.I | re.S)
    text = re.sub(r"<[^>]+>", " ", text)
    return re.sub(r"\s+", " ", html.unescape(text)).strip()


def score(title: str, summary: str, keywords: list[str]) -> tuple[int, list[str]]:
    hay = f"{title} {summary}".lower()
    hits = sorted({k for k in keywords if k.lower() in hay})
    s = len(hits)
    if any(k in hay for k in ("launch", "released", "announced", "preorder", "shipping", "discontinued", "recall")):
        s += 3
    if any(k in hay for k in ("sdk", "api", "firmware", "security", "vulnerability", "open source")):
        s += 2
    if any(k in hay for k in ("brain-computer", "brain computer", "neural", "emg", "eye tracking", "retinal", "haptic")):
        s += 1
    return s, hits


def item_id(url: str, title: str) -> str:
    return hashlib.sha256(f"{url}\n{title}".encode()).hexdigest()[:16]


def classify_scope(title: str, summary: str, source_lane: str, glasses_terms: list[str]) -> tuple[str, bool, str]:
    hay = f"{title} {summary}".lower()
    direct_glasses = any(term.lower() in hay for term in glasses_terms)
    if direct_glasses or source_lane == "core_glasses":
        return "core_glasses", True, "direct smart-glasses or eyewear relevance"
    if source_lane == "adjacent_hci":
        return "adjacent_hci", False, "wearable-HCI relevance without a concrete glasses connection yet"
    return "research_radar", False, "potential ecosystem relevance retained for later review"


def institution_test(title: str, summary: str) -> str:
    hay = f"{title} {summary}".lower()
    durable = (
        "launch", "released", "announced", "sdk", "api", "firmware", "security", "vulnerability",
        "patent", "certification", "research", "study", "acquisition", "partnership", "discontinued",
        "recall", "open source", "brain-computer", "neural", "emg", "eye tracking", "waveguide",
        "microled", "micro-oled", "retinal", "haptic", "accessibility",
    )
    return "likely durable" if any(term in hay for term in durable) else "review durability"


def enrich(candidate: dict, source_lane: str, glasses_terms: list[str]) -> dict:
    scope, publication_eligible, reason = classify_scope(
        candidate["title"], candidate.get("summary", ""), source_lane, glasses_terms
    )
    candidate.update(
        {
            "scope_lane": scope,
            "publication_eligible": publication_eligible,
            "publication_gate_reason": reason,
            "disposition": "collected",
            "site_action": "none_pending_editorial_review",
            "institution_test": institution_test(candidate["title"], candidate.get("summary", "")),
        }
    )
    return candidate


def parse_feed(blob: bytes, source: str, source_lane: str, keywords: list[str], glasses_terms: list[str]) -> list[dict]:
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
    for e in entries[:50]:
        if atom:
            ns = "{http://www.w3.org/2005/Atom}"
            title = clean((e.findtext(ns + "title") or ""))
            summary = clean((e.findtext(ns + "summary") or e.findtext(ns + "content") or ""))
            link = ""
            le = e.find(ns + "link")
            if le is not None:
                link = le.attrib.get("href", "")
            published = e.findtext(ns + "published") or e.findtext(ns + "updated") or ""
        else:
            title = clean(e.findtext("title") or "")
            summary = clean(e.findtext("description") or "")
            link = (e.findtext("link") or "").strip()
            published = (e.findtext("pubDate") or "").strip()
        if not title or not link:
            continue
        s, hits = score(title, summary, keywords)
        candidate = {
            "id": item_id(link, title),
            "title": title,
            "url": link,
            "source": source,
            "source_lane": source_lane,
            "published": published,
            "summary": summary[:1000],
            "materiality_score": s,
            "keyword_hits": hits,
            "status": "candidate",
        }
        out.append(enrich(candidate, source_lane, glasses_terms))
    return out


def google_news_url(query: str) -> str:
    q = urllib.parse.quote(query)
    return f"https://news.google.com/rss/search?q={q}+when:2d&hl=en-US&gl=US&ceid=US:en"


def manufacturer_candidate(url: str, blob: bytes, keywords: list[str], glasses_terms: list[str]) -> dict | None:
    text = blob.decode("utf-8", "ignore")
    title_match = re.search(r"<title[^>]*>(.*?)</title>", text, re.I | re.S)
    title = clean(title_match.group(1)) if title_match else urllib.parse.urlparse(url).netloc
    body = clean(text)[:15000]
    s, hits = score(title, body, keywords)
    if s == 0:
        return None
    candidate = {
        "id": item_id(url, title),
        "title": f"Manufacturer/source watch: {title}",
        "url": url,
        "source": "manufacturer-watch",
        "source_lane": "research_radar",
        "published": "",
        "summary": body[:1000],
        "materiality_score": max(1, s // 2),
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
            seen.update(c.get("id", "") for c in payload.get("candidates", []))
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

    feeds: list[tuple[str, str, str]] = []
    feeds += [(google_news_url(q), f"Google News: {q}", "core_glasses") for q in cfg["core_queries"]]
    feeds += [(google_news_url(q), f"Google News: {q}", "adjacent_hci") for q in cfg["adjacent_hci_queries"]]
    feeds += [(u, "direct-feed", "research_radar") for u in cfg["direct_feeds"]]

    for url, source, source_lane in feeds:
        try:
            candidates.extend(parse_feed(fetch(url), source, source_lane, keywords, glasses_terms))
        except Exception as exc:
            errors.append({"url": url, "error": str(exc)[:300]})

    for url in cfg["manufacturer_pages"]:
        try:
            c = manufacturer_candidate(url, fetch(url), keywords, glasses_terms)
            if c:
                candidates.append(c)
        except Exception as exc:
            errors.append({"url": url, "error": str(exc)[:300]})

    dedup: dict[str, dict] = {}
    for c in candidates:
        key = re.sub(r"[?#].*$", "", c["url"]).rstrip("/").lower() or c["id"]
        if key not in dedup or c["materiality_score"] > dedup[key]["materiality_score"]:
            dedup[key] = c

    seen = prior_ids()
    ranked = sorted(dedup.values(), key=lambda x: (-x["materiality_score"], x["title"].lower()))
    ranked = [x for x in ranked if x["materiality_score"] >= 2 and x["id"] not in seen][:200]

    if not ranked:
        print(f"No new intake candidates; {len(errors)} source errors")
        return 0

    today = dt.datetime.now(dt.timezone.utc).date().isoformat()
    OUTDIR.mkdir(parents=True, exist_ok=True)
    counts = {
        lane: sum(1 for c in ranked if c["scope_lane"] == lane)
        for lane in ("core_glasses", "adjacent_hci", "research_radar")
    }
    payload = {
        "schema": 2,
        "discovered_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "candidate_count": len(ranked),
        "scope_counts": counts,
        "publication_policy": "collect broadly; only glasses-relevant items are eligible for site promotion after editorial review",
        "collector_errors": errors,
        "candidates": ranked,
    }
    (OUTDIR / f"{today}.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    lines = [
        f"# Institutional knowledge intake — {today}",
        "",
        f"Collected **{len(ranked)}** new review candidates.",
        "",
        f"- Core glasses: {counts['core_glasses']}",
        f"- Adjacent HCI radar: {counts['adjacent_hci']}",
        f"- General research radar: {counts['research_radar']}",
        "",
        "**Publishing rule:** collection is not publication. Only items with a concrete smart-glasses/eyewear connection are eligible for promotion to the public site, and even those require editorial review.",
        "",
        "Default disposition for every new item is **collected**. Later editorial dispositions are: watch, archived, published, superseded, or rejected.",
        "",
    ]
    for c in ranked[:80]:
        hits = ", ".join(c["keyword_hits"][:8]) or "general ecosystem match"
        lines += [
            f"## {c['title']}",
            "",
            f"- Source: {c['url']}",
            f"- Scope: {c['scope_lane']}",
            f"- Publication eligible now: {'yes' if c['publication_eligible'] else 'no'}",
            f"- Disposition: {c['disposition']}",
            f"- Institution test: {c['institution_test']}",
            f"- Materiality score: {c['materiality_score']}",
            f"- Signals: {hits}",
            f"- Published by source: {c['published'] or 'not supplied by source'}",
            "",
        ]
    if errors:
        lines += ["## Collector warnings", ""] + [f"- {e['url']}: {e['error']}" for e in errors]
    (OUTDIR / f"{today}.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Collected {len(ranked)} new candidates; {counts}; {len(errors)} source errors")
    return 0


if __name__ == "__main__":
    sys.exit(main())
