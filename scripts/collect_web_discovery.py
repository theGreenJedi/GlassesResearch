#!/usr/bin/env python3
"""High-recall web discovery for GlassesResearch.

This collector complements the news intake. It deliberately searches the ordinary
web, retail surfaces, developer material, research sources, community sources, and
manufacturer catalogs. Nothing collected here is published automatically.
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
CONFIG = ROOT / "research" / "discovery-sources.json"
OUTDIR = ROOT / "research" / "discovery-candidates"
UA = "GlassesResearch-Discovery/1.0 (+https://glassesresearch.org/)"

GLASSES_TERMS = (
    "smart glasses", "ai glasses", "ar glasses", "smart eyewear", "eyewear",
    "glasses", "spectacles", "maverick", "inmo", "dymesty", "latitude52",
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
    return urllib.parse.urlunsplit((parsed.scheme.lower(), parsed.netloc.lower(), parsed.path.rstrip("/"), "", ""))


def candidate_id(url: str, title: str) -> str:
    return hashlib.sha256(f"{normalize_url(url)}\n{title.lower()}".encode()).hexdigest()[:16]


def bing_rss(query: str) -> str:
    encoded = urllib.parse.quote(query)
    return f"https://www.bing.com/search?q={encoded}&format=rss&count=30"


def classify_scope(channel: str, title: str, summary: str) -> str:
    hay = f"{title} {summary}".lower()
    if channel in {"broad_web", "retail", "developer", "manufacturer_catalog", "community"}:
        return "core_glasses" if any(term in hay for term in GLASSES_TERMS) else "research_radar"
    return "research_radar"


def make_candidate(*, title: str, url: str, summary: str, channel: str, query: str = "", source: str = "") -> dict:
    scope = classify_scope(channel, title, summary)
    return {
        "id": candidate_id(url, title),
        "title": title,
        "url": url,
        "summary": summary[:1200],
        "discovery_channel": channel,
        "query": query,
        "source": source or channel,
        "scope_lane": scope,
        "status": "candidate",
        "publication_eligible": False,
        "publication_gate_reason": "discovery is a lead only; verification and editorial review are required",
        "disposition": "collected",
    }


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
        out.append(make_candidate(title=title, url=url, summary=summary, channel=channel, query=query, source="Bing web RSS"))
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
        hay = f"{anchor} {parsed.path}".lower()
        product_signal = any(term in hay for term in (
            "glass", "eyewear", "spectacle", "maverick", "inmo", "cook", "berlin",
            "product", "collection", "developer", "sdk", "support",
        ))
        if not product_signal:
            continue
        seen.add(normalized)
        title = anchor or parsed.path.rsplit("/", 1)[-1].replace("-", " ") or base.netloc
        out.append(make_candidate(
            title=f"Manufacturer catalog lead: {title}",
            url=url,
            summary=f"Same-domain catalog/developer link discovered from {base_url}",
            channel="manufacturer_catalog",
            source=base_url,
        ))
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
    }
    for channel, queries in lanes.items():
        for query in queries:
            url = bing_rss(query)
            try:
                candidates.extend(parse_rss(fetch(url), channel, query))
            except Exception as exc:
                errors.append({"channel": channel, "query": query, "url": url, "error": str(exc)[:300]})

    for url in cfg.get("manufacturer_catalog_pages", []):
        try:
            blob = fetch(url)
            body = clean(blob.decode("utf-8", "ignore"))[:1200]
            candidates.append(make_candidate(
                title=f"Manufacturer catalog watch: {urllib.parse.urlsplit(url).netloc}",
                url=url,
                summary=body,
                channel="manufacturer_catalog",
                source="configured manufacturer catalog",
            ))
            candidates.extend(same_domain_product_links(url, blob))
        except Exception as exc:
            errors.append({"channel": "manufacturer_catalog", "url": url, "error": str(exc)[:300]})

    dedup: dict[str, dict] = {}
    for item in candidates:
        key = normalize_url(item["url"])
        if key not in dedup:
            dedup[key] = item
        else:
            prior = dedup[key]
            channels = sorted(set(str(prior.get("discovery_channel", "")).split("+")) | {item["discovery_channel"]})
            prior["discovery_channel"] = "+".join(channels)
            if item.get("query") and item["query"] not in str(prior.get("query", "")):
                prior["query"] = "; ".join(x for x in [str(prior.get("query", "")), item["query"]] if x)

    seen = prior_ids()
    ranked = [item for item in dedup.values() if item["id"] not in seen]
    ranked.sort(key=lambda item: (item["discovery_channel"], item["title"].lower()))
    ranked = ranked[:400]

    if not ranked:
        print(f"No new web-discovery candidates; {len(errors)} source errors")
        return 0

    now = dt.datetime.now(dt.timezone.utc)
    day = now.date().isoformat()
    OUTDIR.mkdir(parents=True, exist_ok=True)
    counts: dict[str, int] = {}
    for item in ranked:
        for channel in item["discovery_channel"].split("+"):
            counts[channel] = counts.get(channel, 0) + 1
    payload = {
        "schema": 1,
        "discovered_utc": now.isoformat(),
        "candidate_count": len(ranked),
        "channel_counts": counts,
        "policy": cfg.get("policy", {}),
        "collector_errors": errors,
        "candidates": ranked,
    }
    (OUTDIR / f"{day}.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    lines = [
        f"# Web discovery intake — {day}", "",
        f"Collected **{len(ranked)}** new high-recall discovery leads.", "",
        "**Rule:** discovery is not verification and never publishes automatically.", "",
    ]
    for channel, count in sorted(counts.items()):
        lines.append(f"- {channel}: {count}")
    lines.append("")
    for item in ranked[:120]:
        lines += [
            f"## {item['title']}", "",
            f"- URL: {item['url']}",
            f"- Channel: {item['discovery_channel']}",
            f"- Query/source: {item.get('query') or item.get('source')}",
            f"- Scope: {item['scope_lane']}", "",
        ]
    if errors:
        lines += ["## Collector warnings", ""] + [f"- {e.get('channel')}: {e.get('url')}: {e['error']}" for e in errors]
    (OUTDIR / f"{day}.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Collected {len(ranked)} web-discovery candidates across {counts}; {len(errors)} source errors")
    return 0


if __name__ == "__main__":
    sys.exit(main())
