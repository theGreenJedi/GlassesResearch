#!/usr/bin/env python3
"""Collect potentially material smart-glasses ecosystem news into a review queue.

The collector is deliberately conservative: it gathers and ranks candidates but does not
promote them into canonical model/lineage claims. Promotion remains a reviewed research step.
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
UA = "GlassesResearch-NewsCollector/1.0 (+https://glassesresearch.org/)"


def fetch(url: str, timeout: int = 20) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/rss+xml, application/atom+xml, text/html;q=0.9, */*;q=0.5"})
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
    return s, hits


def item_id(url: str, title: str) -> str:
    return hashlib.sha256(f"{url}\n{title}".encode()).hexdigest()[:16]


def parse_feed(blob: bytes, source: str, keywords: list[str]) -> list[dict]:
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
        out.append({
            "id": item_id(link, title), "title": title, "url": link, "source": source,
            "published": published, "summary": summary[:1000], "materiality_score": s,
            "keyword_hits": hits, "status": "candidate"
        })
    return out


def google_news_url(query: str) -> str:
    q = urllib.parse.quote(query)
    return f"https://news.google.com/rss/search?q={q}+when:2d&hl=en-US&gl=US&ceid=US:en"


def manufacturer_candidate(url: str, blob: bytes, keywords: list[str]) -> dict | None:
    text = blob.decode("utf-8", "ignore")
    title_match = re.search(r"<title[^>]*>(.*?)</title>", text, re.I | re.S)
    title = clean(title_match.group(1)) if title_match else urllib.parse.urlparse(url).netloc
    body = clean(text)[:15000]
    s, hits = score(title, body, keywords)
    if s == 0:
        return None
    return {
        "id": item_id(url, title), "title": f"Source page changed/contains material terms: {title}",
        "url": url, "source": "manufacturer-watch", "published": "", "summary": body[:1000],
        "materiality_score": max(1, s // 2), "keyword_hits": hits[:20], "status": "candidate"
    }


def main() -> int:
    cfg = json.loads(CONFIG.read_text(encoding="utf-8"))
    keywords = cfg["material_keywords"]
    candidates: list[dict] = []
    errors: list[dict] = []

    feeds = [(google_news_url(q), f"Google News: {q}") for q in cfg["queries"]]
    feeds += [(u, "direct-feed") for u in cfg["direct_feeds"]]
    for url, source in feeds:
        try:
            candidates.extend(parse_feed(fetch(url), source, keywords))
        except Exception as exc:
            errors.append({"url": url, "error": str(exc)[:300]})

    for url in cfg["manufacturer_pages"]:
        try:
            c = manufacturer_candidate(url, fetch(url), keywords)
            if c:
                candidates.append(c)
        except Exception as exc:
            errors.append({"url": url, "error": str(exc)[:300]})

    # Deduplicate by normalized URL/title identity and keep the highest materiality score.
    dedup: dict[str, dict] = {}
    for c in candidates:
        key = re.sub(r"[?#].*$", "", c["url"]).rstrip("/").lower() or c["id"]
        if key not in dedup or c["materiality_score"] > dedup[key]["materiality_score"]:
            dedup[key] = c

    ranked = sorted(dedup.values(), key=lambda x: (-x["materiality_score"], x["title"].lower()))
    # Avoid repository churn from low-signal search results.
    ranked = [x for x in ranked if x["materiality_score"] >= 2][:150]

    today = dt.datetime.now(dt.timezone.utc).date().isoformat()
    OUTDIR.mkdir(parents=True, exist_ok=True)
    payload = {
        "schema": 1,
        "discovered_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "candidate_count": len(ranked),
        "collector_errors": errors,
        "candidates": ranked,
    }
    json_path = OUTDIR / f"{today}.json"
    json_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    lines = [f"# Daily ecosystem candidates — {today}", "", f"Collected **{len(ranked)}** review candidates.", "",
             "This file is an intake queue, not a publication. Candidates become public facts only after verification and promotion into canonical research.", ""]
    for c in ranked[:50]:
        hits = ", ".join(c["keyword_hits"][:8]) or "general ecosystem match"
        lines += [f"## {c['title']}", "", f"- Source: {c['url']}", f"- Materiality score: {c['materiality_score']}",
                  f"- Signals: {hits}", f"- Published: {c['published'] or 'not supplied by source'}", ""]
    if errors:
        lines += ["## Collector warnings", ""] + [f"- {e['url']}: {e['error']}" for e in errors]
    (OUTDIR / f"{today}.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Collected {len(ranked)} candidates; {len(errors)} source errors")
    return 0


if __name__ == "__main__":
    sys.exit(main())
