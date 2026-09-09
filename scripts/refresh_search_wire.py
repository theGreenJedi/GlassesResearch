#!/usr/bin/env python3
"""Refresh the public developing-news wire from commodity search wheels.

GlassesResearch does not need to own web crawling. This collector deliberately uses
commodity discovery surfaces (Google News RSS, Bing News RSS, and Bing Web RSS), plus
small benchmark-sentinel checks, performs only the minimum normalization/deduplication
needed for the public developing wire, and leaves verification/editorial judgment to
GlassesResearch.

Across the Wire is a recall-oriented discovery surface. Ordinary web/news search is
the benchmark: retrieval should cast a broad net across generic, company, product,
policy, research, accessibility, market, and relevant international-language terms,
while downstream editorial stages decide importance and verification.

Benchmark sentinels are gap detectors only. They are never treated as authorities: a
sentinel can surface an outbound publisher link for review, but it cannot verify or
promote the underlying claim.
"""
from __future__ import annotations

import argparse
import datetime as dt
import email.utils
import hashlib
import html
import json
import re
import statistics
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path

# Fast news queries run against both Google News and Bing News. Keep this set focused
# enough that a 15-minute discovery clock remains practical while covering the makers,
# platforms, policy, optics, software, and business developments most likely to move.
NEWS_QUERIES = (
    '"smart glasses"', '"AI glasses"', '"AR glasses"',
    '"Ray-Ban Meta"', '"Meta glasses"', '"Android XR" glasses',
    'Samsung smart glasses', 'Google smart glasses', 'Apple smart glasses',
    '"Snap Specs"', '"Lens Studio" Spectacles', 'RayNeo glasses', 'XREAL glasses',
    'Rokid glasses', 'VITURE glasses', '"Even Realities" glasses', 'Vuzix glasses',
    'INMO glasses', 'smart glasses waveguide', 'smart glasses SDK',
    'smart glasses firmware', 'smart glasses privacy', 'smart glasses regulation',
    'smart glasses accessibility', 'smart glasses funding partnership acquisition',
)

# Ordinary web search remains useful for developer/open-source and teardown material,
# but it changes less quickly than news. Restricting Bing Web to a small subset keeps
# per-run request volume roughly flat even though the public wire now scans twice as
# often.
WEB_QUERIES = (
    '"smart glasses"', '"AI glasses"', '"AR glasses"', 'smart glasses SDK',
    'smart glasses open source', 'smart glasses teardown', 'smart glasses waveguide',
)

# Discovery-only locale wheels. These increase recall for regions with meaningful
# eyewear, optics, electronics, XR, or manufacturing ecosystems without changing
# any downstream verification or editorial promotion rule.
INTERNATIONAL_GOOGLE = (
    ("pt-BR", "BR", "BR:pt-419", ('"óculos inteligentes"', '"óculos de realidade aumentada"', 'óculos AR')),
    ("es-419", "MX", "MX:es-419", ('"gafas inteligentes"', '"gafas de realidad aumentada"', 'gafas AR')),
    ("ru", "RU", "RU:ru", ('"умные очки"', '"очки дополненной реальности"', 'AR очки')),
    ("ja", "JP", "JP:ja", ('スマートグラス', 'ARグラス', 'AIグラス')),
    ("ko", "KR", "KR:ko", ('스마트 안경', 'AR 글래스', 'AI 안경')),
    ("zh-CN", "CN", "CN:zh-Hans", ('智能眼镜', 'AR眼镜', 'AI眼镜')),
)

# A sentinel is a discovery benchmark, not an evidence source. Only outbound links to
# the original publisher are admitted to the wire, with the item still marked Reported.
SENTINELS = (
    ("smartglasses.today", "https://www.smartglasses.today/articles"),
)

RELEVANCE_TERMS = (
    "smart glasses", "smartglasses", "ai glasses", "ar glasses", "augmented reality glasses",
    "ray-ban meta", "meta glasses", "oakley meta", "rayneo", "xreal", "rokid", "viture",
    "even realities", "vuzix", "snap specs", "snap smart glasses", "spectacles",
    "samsung smart glasses", "google smart glasses", "apple smart glasses", "inmo",
    "brilliant labs", "solos airgo", "halliday", "waveguide",
    "óculos inteligentes", "óculos de realidade aumentada", "óculos ar",
    "gafas inteligentes", "gafas de realidad aumentada", "gafas ar",
    "умные очки", "очки дополненной реальности", "ar очки",
    "スマートグラス", "arグラス", "aiグラス",
    "스마트 안경", "ar 글래스", "ai 안경",
    "智能眼镜", "ar眼镜", "ai眼镜",
)
TECH_HOST_HINTS = (
    "theverge.com", "techcrunch.com", "arstechnica.com", "tomsguide.com",
    "androidcentral.com", "androidauthority.com", "engadget.com", "cnet.com", "wired.com",
    "9to5google.com", "9to5mac.com", "roadtovr.com", "uploadvr.com", "auganix.org",
    "kguttag.com", "visionmonday.com", "sammobile.com", "petapixel.com",
)
PRIMARY_HOST_HINTS = (
    "about.fb.com", "meta.com", "engineering.fb.com", "snap.com", "newsroom.snap.com",
    "developers.snap.com", "googleblog.com", "blog.google", "developer.android.com",
    "android-developers.googleblog.com", "apple.com", "samsung.com", "rayneo.com", "xreal.com",
    "rokid.com", "viture.com", "evenrealities.com", "vuzix.com",
)
UA = "GlassesResearch-Wire/1.3 (+https://glassesresearch.org/)"
MIN_TIME = dt.datetime.min.replace(tzinfo=dt.timezone.utc)


def fetch(url: str, timeout: int = 25) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/rss+xml, application/xml;q=0.9, text/html;q=0.8, */*;q=0.5"})
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
    return urllib.parse.urlsplit(url).netloc.lower().removeprefix("www.")


def source_class(url: str) -> str:
    host = hostname(url)
    if any(host == hint or host.endswith(f".{hint}") for hint in PRIMARY_HOST_HINTS):
        return "primary"
    if any(host == hint or host.endswith(f".{hint}") for hint in TECH_HOST_HINTS):
        return "technical_reporting"
    return "reputable_secondary"


def discovery_id(title: str, url: str) -> str:
    return hashlib.sha256(f"{title.casefold()}\n{url}".encode("utf-8")).hexdigest()[:16]


def google_news_url(query: str, hl: str = "en-US", gl: str = "US", ceid: str = "US:en") -> str:
    q = urllib.parse.quote(f"{query} when:3d")
    return f"https://news.google.com/rss/search?q={q}&hl={urllib.parse.quote(hl)}&gl={urllib.parse.quote(gl)}&ceid={urllib.parse.quote(ceid)}"


def bing_news_url(query: str) -> str:
    return f"https://www.bing.com/news/search?q={urllib.parse.quote(query)}&format=RSS"


def bing_web_url(query: str) -> str:
    return f"https://www.bing.com/search?q={urllib.parse.quote(query)}&format=rss"


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
        if not any(term.casefold() in haystack for term in RELEVANCE_TERMS):
            continue
        source = item.find("source")
        publisher = clean(source.text if source is not None and source.text else "") or hostname(url)
        out.append({
            "discovery_id": discovery_id(title, url), "title": title, "url": url,
            "publisher": publisher, "source_class": source_class(url), "published_at": published_at,
            "discovered_at": "", "status": "reported", "_wheel": wheel, "_query": query,
        })
    return out


class SentinelLinkParser(HTMLParser):
    """Collect outbound anchor text without copying article bodies or summaries."""

    def __init__(self, base_url: str) -> None:
        super().__init__(convert_charrefs=True)
        self.base_url = base_url
        self.links: list[tuple[str, str]] = []
        self._href = ""
        self._parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() != "a" or self._href:
            return
        href = dict(attrs).get("href") or ""
        self._href = urllib.parse.urljoin(self.base_url, href)
        self._parts = []

    def handle_data(self, data: str) -> None:
        if self._href:
            self._parts.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() != "a" or not self._href:
            return
        title = clean(" ".join(self._parts))
        if title:
            self.links.append((self._href, title))
        self._href = ""
        self._parts = []


def parse_sentinel(blob: bytes, label: str, page_url: str) -> list[dict]:
    parser = SentinelLinkParser(page_url)
    parser.feed(blob.decode("utf-8", "ignore"))
    sentinel_host = hostname(page_url)
    out: list[dict] = []
    seen: set[str] = set()
    for url, title in parser.links:
        parsed = urllib.parse.urlsplit(url)
        if parsed.scheme not in {"http", "https"} or not parsed.netloc:
            continue
        host = hostname(url)
        if host == sentinel_host or host.endswith(f".{sentinel_host}"):
            continue
        if url in seen or len(title) < 12:
            continue
        haystack = title.casefold()
        if not any(term.casefold() in haystack for term in RELEVANCE_TERMS):
            continue
        seen.add(url)
        out.append({
            "discovery_id": discovery_id(title, url), "title": title, "url": url,
            "publisher": host, "source_class": source_class(url), "published_at": "",
            "discovered_at": "", "status": "reported", "_wheel": f"Sentinel {label}",
            "_query": "benchmark gap detector",
        })
    return out


def title_key(title: str) -> str:
    value = re.sub(r"\s+-\s+[^-]{2,80}$", "", title.casefold())
    value = re.sub(r"[^\w]+", " ", value, flags=re.UNICODE)
    return re.sub(r"\s+", " ", value).strip()


def parse_time(value: str) -> dt.datetime:
    if not value:
        return MIN_TIME
    try:
        return dt.datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(dt.timezone.utc)
    except ValueError:
        return MIN_TIME


def load_previous(path: Path) -> tuple[dict, dict[str, str]]:
    if not path.exists():
        return {}, {}
    try:
        state = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}, {}
    discovered = {str(item.get("discovery_id")): str(item.get("discovered_at") or "") for item in state.get("items", []) if isinstance(item, dict) and item.get("discovery_id")}
    return state, discovered


def ranking_time(item: dict, previous_discovered: dict[str, str], now: dt.datetime) -> dt.datetime:
    published = parse_time(str(item.get("published_at") or ""))
    if published != MIN_TIME:
        return published
    prior = parse_time(previous_discovered.get(str(item.get("discovery_id") or ""), ""))
    return prior if prior != MIN_TIME else now


def percentile(values: list[float], fraction: float) -> float | None:
    if not values:
        return None
    ordered = sorted(values)
    index = round((len(ordered) - 1) * fraction)
    return ordered[index]


def velocity_summary(items: list[dict], now: dt.datetime) -> dict:
    delays: list[float] = []
    published_last_24h = 0
    discovered_last_24h = 0
    day_ago = now - dt.timedelta(hours=24)
    for item in items:
        published = parse_time(str(item.get("published_at") or ""))
        discovered = parse_time(str(item.get("discovered_at") or ""))
        if published != MIN_TIME:
            if published >= day_ago:
                published_last_24h += 1
            if discovered != MIN_TIME:
                delays.append(max(0.0, (discovered - published).total_seconds() / 60.0))
        if discovered != MIN_TIME and discovered >= day_ago:
            discovered_last_24h += 1

    median_delay = statistics.median(delays) if delays else None
    p90_delay = percentile(delays, 0.90)
    within_target = (100.0 * sum(delay <= 120 for delay in delays) / len(delays)) if delays else None
    return {
        "target_discovery_minutes": 120,
        "items_in_window": len(items),
        "items_published_last_24h": published_last_24h,
        "items_discovered_last_24h": discovered_last_24h,
        "median_discovery_delay_minutes": round(median_delay, 1) if median_delay is not None else None,
        "p90_discovery_delay_minutes": round(p90_delay, 1) if p90_delay is not None else None,
        "within_target_percent": round(within_target, 1) if within_target is not None else None,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path("data/wire-state.json"))
    parser.add_argument("--max-items", type=int, default=120)
    args = parser.parse_args()
    now = dt.datetime.now(dt.timezone.utc)
    previous, previous_discovered = load_previous(args.output)
    candidates: list[dict] = []
    errors: list[str] = []

    news_wheels = (("Google News", google_news_url), ("Bing News", bing_news_url))
    for wheel, builder in news_wheels:
        for query in NEWS_QUERIES:
            try:
                candidates.extend(parse_feed(fetch(builder(query)), wheel, query))
            except Exception as exc:
                errors.append(f"{wheel} {query}: {exc}")

    for query in WEB_QUERIES:
        try:
            candidates.extend(parse_feed(fetch(bing_web_url(query)), "Bing Web", query))
        except Exception as exc:
            errors.append(f"Bing Web {query}: {exc}")

    for hl, gl, ceid, queries in INTERNATIONAL_GOOGLE:
        for query in queries:
            wheel = f"Google News {gl}"
            try:
                candidates.extend(parse_feed(fetch(google_news_url(query, hl=hl, gl=gl, ceid=ceid)), wheel, query))
            except Exception as exc:
                errors.append(f"{wheel} {query}: {exc}")

    for label, page_url in SENTINELS:
        try:
            candidates.extend(parse_sentinel(fetch(page_url), label, page_url))
        except Exception as exc:
            errors.append(f"Sentinel {label}: {exc}")

    dedup: dict[str, dict] = {}
    for item in candidates:
        key = title_key(item["title"]) or item["discovery_id"]
        prior = dedup.get(key)
        if prior is None or ranking_time(item, previous_discovered, now) > ranking_time(prior, previous_discovered, now):
            dedup[key] = item

    cutoff = now - dt.timedelta(days=3)
    ranked = [
        item for item in dedup.values()
        if not item["published_at"] or parse_time(item["published_at"]) >= cutoff
    ]
    ranked.sort(
        key=lambda item: (ranking_time(item, previous_discovered, now), item["title"].casefold()),
        reverse=True,
    )
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
        "semantics": "Discovery-only wire from commodity web/news search and benchmark gap detectors, including locale-aware international recall. Items are source reports under review, not verified GlassesResearch claims.",
        "generated_at": now.isoformat().replace("+00:00", "Z"),
        "velocity": velocity_summary(ranked, now),
        "items": ranked,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(state, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    metrics = state["velocity"]
    print(
        "Search wire refreshed: "
        f"items={len(ranked)}; feed_errors={len(errors)}; "
        f"median_delay_min={metrics['median_discovery_delay_minutes']}; "
        f"within_120m={metrics['within_target_percent']}%"
    )
    for error in errors:
        print(f"warning: {error}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
