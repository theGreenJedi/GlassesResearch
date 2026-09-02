#!/usr/bin/env python3
"""Refresh the public developing-news wire from existing search/news wheels.

GlassesResearch does not need to own web crawling. This collector deliberately uses
commodity discovery surfaces (Google News RSS and Bing News RSS), performs only the
minimum normalization/deduplication needed for the public developing wire, and
leaves verification/editorial judgment to GlassesResearch.

Across the Wire is a recall-oriented discovery surface. Ordinary web/news search is
the benchmark: retrieval should cast a broad net across generic, company, product,
policy, research, accessibility, and market terms, while downstream editorial stages
decide importance and verification.
"""
from __future__ import annotations

import argparse
import datetime as dt
import email.utils
import hashlib
import html
import json
import re
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

QUERIES = (
    '"smart glasses"',
    '"AI glasses"',
    '"AR glasses"',
    '"augmented reality glasses"',
    '"Ray-Ban Meta"',
    '"Meta glasses"',
    'RayNeo glasses',
    'XREAL glasses',
    'Rokid glasses',
    'VITURE glasses',
    '"Even Realities" glasses',
    'Vuzix glasses',
    '"Snap Specs"',
    'Snap smart glasses',
    'Samsung smart glasses',
    'Google smart glasses',
    'Apple smart glasses',
    'smart glasses privacy',
    'smart glasses regulation',
    'smart glasses accessibility',
    'smart glasses research',
)
RELEVANCE_TERMS = (
    "smart glasses",
    "smartglasses",
    "ai glasses",
    "ar glasses",
    "augmented reality glasses",
    "ray-ban meta",
    "meta glasses",
    "rayneo",
    "xreal",
    "rokid",
    "viture",
    "even realities",
    "vuzix",
    "snap specs",
    "snap smart glasses",
    "samsung smart glasses",
    "google smart glasses",
    "apple smart glasses",
)
TECH_HOST_HINTS = (
    "theverge.com",
    "techcrunch.com",
    "arstechnica.com",
    "tomsguide.com",
    "androidcentral.com",
    "engadget.com",
    "cnet.com",
    "wired.com",
)
PRIMARY_HOST_HINTS = (
    "about.fb.com",
    "meta.com",
    "snap.com",
    "newsroom.snap.com",
    "googleblog.com",
    "blog.google",
    "apple.com",
    "samsung.com",
    "rayneo.com",
    "xreal.com",
    "rokid.com",
    "viture.com",
    "evenrealities.com",
    "vuzix.com",
)
UA = "GlassesResearch-Wire/1.0 (+https://glassesresearch.org/)"


def fetch(url: str, timeout: int = 25) -> bytes:
    req = urllib.request.Request(
        url,
        headers={"User-Agent": UA, "Accept": "application/rss+xml, application/xml;q=0.9, */*;q=0.5"},
    )
    with urllib.request.urlopen(req, timeout=timeout) as response:
        return response.read()


def clean(value: str) -> str:
    value = re.sub(r"<[^>]+>", " ", value or "")
    return re.sub(r"\s+", " ", html.unescape(value)).strip()


def iso_date(value: str) -> str:
    value = (value or "").strip()
    if not value:
        return ""
    try:
        parsed = email.utils.parsedate_to_datetime(value)
        if parsed.tzinfo is None:
            parsed = parsed.replace(tzinfo=dt.timezone.utc)
        return parsed.astimezone(dt.timezone.utc).isoformat().replace("+00:00", "Z")
    except (TypeError, ValueError, OverflowError):
        return value


def hostname(url: str) -> str:
    host = urllib.parse.urlsplit(url).netloc.lower()
    return host.removeprefix("www.")


def source_class(url: str) -> str:
    host = hostname(url)
    if any(host == hint or host.endswith(f".{hint}") for hint in PRIMARY_HOST_HINTS):
        return "primary"
    if any(host == hint or host.endswith(f".{hint}") for hint in TECH_HOST_HINTS):
        return "technical_reporting"
    return "reputable_secondary"


def discovery_id(title: str, url: str) -> str:
    key = f"{title.casefold()}\n{url}".encode("utf-8")
    return hashlib.sha256(key).hexdigest()[:16]


def google_news_url(query: str) -> str:
    q = urllib.parse.quote(f"{query} when:3d")
    return f"https://news.google.com/rss/search?q={q}&hl=en-US&gl=US&ceid=US:en"


def bing_news_url(query: str) -> str:
    q = urllib.parse.quote(query)
    return f"https://www.bing.com/news/search?q={q}&format=RSS"


def parse_feed(blob: bytes, wheel: str, query: str) -> list[dict]:
    root = ET.fromstring(blob)
    out: list[dict] = []
    for item in root.findall(".//item")[:40]:
        title = clean(item.findtext("title") or "")
        url = (item.findtext("link") or "").strip()
        description = clean(item.findtext("description") or "")
        published_at = iso_date(item.findtext("pubDate") or item.findtext("published") or "")
        if not title or not url:
            continue
        haystack = f"{title} {description}".casefold()
        if not any(term in haystack for term in RELEVANCE_TERMS):
            continue
        source = item.find("source")
        publisher = clean(source.text if source is not None and source.text else "") or hostname(url)
        out.append(
            {
                "discovery_id": discovery_id(title, url),
                "title": title,
                "url": url,
                "publisher": publisher,
                "source_class": source_class(url),
                "published_at": published_at,
                "discovered_at": "",
                "status": "reported",
                "_wheel": wheel,
                "_query": query,
            }
        )
    return out


def title_key(title: str) -> str:
    value = re.sub(r"\s+-\s+[^-]{2,80}$", "", title.casefold())
    value = re.sub(r"[^a-z0-9]+", " ", value)
    return re.sub(r"\s+", " ", value).strip()


def parse_time(value: str) -> dt.datetime:
    if not value:
        return dt.datetime.min.replace(tzinfo=dt.timezone.utc)
    try:
        return dt.datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(dt.timezone.utc)
    except ValueError:
        return dt.datetime.min.replace(tzinfo=dt.timezone.utc)


def load_previous(path: Path) -> tuple[dict, dict[str, str]]:
    if not path.exists():
        return {}, {}
    try:
        state = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}, {}
    discovered = {
        str(item.get("discovery_id")): str(item.get("discovered_at") or "")
        for item in state.get("items", [])
        if isinstance(item, dict) and item.get("discovery_id")
    }
    return state, discovered


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path("data/wire-state.json"))
    parser.add_argument("--max-items", type=int, default=72)
    args = parser.parse_args()

    now = dt.datetime.now(dt.timezone.utc)
    previous, previous_discovered = load_previous(args.output)
    candidates: list[dict] = []
    errors: list[str] = []

    wheels = (
        ("Google News", google_news_url),
        ("Bing News", bing_news_url),
    )
    for wheel, builder in wheels:
        for query in QUERIES:
            url = builder(query)
            try:
                candidates.extend(parse_feed(fetch(url), wheel, query))
            except Exception as exc:  # external feeds should fail independently
                errors.append(f"{wheel} {query}: {exc}")

    dedup: dict[str, dict] = {}
    for item in candidates:
        key = title_key(item["title"]) or item["discovery_id"]
        prior = dedup.get(key)
        if prior is None or parse_time(item["published_at"]) > parse_time(prior["published_at"]):
            dedup[key] = item

    cutoff = now - dt.timedelta(days=3)
    ranked = [
        item for item in dedup.values()
        if not item["published_at"] or parse_time(item["published_at"]) >= cutoff
    ]
    ranked.sort(key=lambda item: (parse_time(item["published_at"]), item["title"].casefold()), reverse=True)
    ranked = ranked[: max(1, args.max_items)]

    for item in ranked:
        item["discovered_at"] = previous_discovered.get(item["discovery_id"]) or now.isoformat().replace("+00:00", "Z")
        item.pop("_wheel", None)
        item.pop("_query", None)

    previous_items = previous.get("items") if isinstance(previous.get("items"), list) else []
    if ranked == previous_items:
        print(f"Search wire unchanged: items={len(ranked)}; feed_errors={len(errors)}")
        return 0

    state = {
        "schema_version": 1,
        "semantics": "Discovery-only wire from commodity search/news feeds. Items are source reports under review, not verified GlassesResearch claims.",
        "generated_at": now.isoformat().replace("+00:00", "Z"),
        "items": ranked,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(state, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Search wire refreshed: items={len(ranked)}; feed_errors={len(errors)}")
    for error in errors:
        print(f"warning: {error}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
