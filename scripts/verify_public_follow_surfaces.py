#!/usr/bin/env python3
"""Smoke-test reader-facing publication surfaces and live research-state agreement."""

from __future__ import annotations

import argparse
import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime

DEFAULT_BASE = "https://glassesresearch.org"
GUIDE_PATHS = (
    "/guides/open-source-smart-glasses/",
    "/guides/offline-smart-glasses/",
    "/guides/visual-ai-smart-glasses/",
)


def fetch(base: str, path: str, cache_bust: str) -> tuple[bytes, str]:
    separator = "&" if "?" in path else "?"
    url = f"{base.rstrip('/')}{path}{separator}{urllib.parse.urlencode({'smoke': cache_bust})}"
    request = urllib.request.Request(
        url,
        headers={
            "Cache-Control": "no-cache",
            "Pragma": "no-cache",
            "User-Agent": "GlassesResearch-public-surface-smoke/1.2",
        },
    )
    with urllib.request.urlopen(request, timeout=20) as response:
        return response.read(), response.headers.get("Content-Type", "")


def require(needle: str, haystack: str, label: str) -> None:
    if needle not in haystack:
        raise AssertionError(f"{label}: missing {needle!r}")


def homepage_stat(home: str, name: str) -> str:
    match = re.search(
        rf'<strong\s+data-site-stat="{re.escape(name)}">\s*([^<]+?)\s*</strong>',
        home,
        flags=re.I,
    )
    if not match:
        raise AssertionError(f"homepage: missing rendered data-site-stat={name!r}")
    return match.group(1).strip()


def display_date(raw_date: str) -> str:
    parsed = datetime.strptime(raw_date, "%Y-%m-%d")
    return f"{parsed.strftime('%b')} {parsed.day}, {parsed.year}"


def rendered_catalog_count(the_list: str) -> int:
    match = re.search(r"\bCount:\s*</?[^>]*>?\s*(\d+)\s+distinct purchasable models", the_list, flags=re.I)
    if not match:
        match = re.search(r"\bCount:\s*(\d+)\s+distinct purchasable models", re.sub(r"<[^>]+>", "", the_list), flags=re.I)
    if not match:
        raise AssertionError("The List: could not resolve rendered canonical Count")
    return int(match.group(1))


def guide_catalog_count(guide: str, label: str) -> int:
    text = re.sub(r"<[^>]+>", " ", guide)
    match = re.search(r"browse all\s+(\d+)\s+canonical models", text, flags=re.I)
    if not match:
        raise AssertionError(f"{label}: missing generated canonical-model footer count")
    return int(match.group(1))


def validate_snapshot(base: str, expected_sha: str | None, cache_bust: str) -> None:
    deployment_raw, _ = fetch(base, "/deployment.json", cache_bust)
    deployment = json.loads(deployment_raw)
    if expected_sha:
        actual = deployment.get("sha")
        if actual != expected_sha:
            raise AssertionError(f"stale production: expected {expected_sha}, got {actual}")

    home_raw, _ = fetch(base, "/", cache_bust)
    news_raw, _ = fetch(base, "/docs/RESEARCH_NEWS/", cache_bust)
    fieldwork_raw, _ = fetch(base, "/docs/FIELDWORK/", cache_bust)
    the_list_raw, _ = fetch(base, "/models/THE_LIST/", cache_bust)
    status_raw, _ = fetch(base, "/data/site-status.json", cache_bust)
    devices_raw, _ = fetch(base, "/data/devices.json", cache_bust)
    verified_rss_raw, verified_rss_type = fetch(base, "/feed.xml", cache_bust)
    verified_json_raw, verified_json_type = fetch(base, "/feed.json", cache_bust)
    wire_rss_raw, wire_rss_type = fetch(base, "/data/wire-feed.xml", cache_bust)
    wire_json_raw, wire_json_type = fetch(base, "/data/wire-feed.json", cache_bust)

    home = home_raw.decode("utf-8")
    news = news_raw.decode("utf-8")
    fieldwork = fieldwork_raw.decode("utf-8")
    the_list = the_list_raw.decode("utf-8")
    require("Research &amp; News", home, "homepage")
    require("/feed.xml", home, "homepage verified feed entrance")
    require("/data/wire-feed.xml", home, "homepage wire RSS entrance")
    require("/data/wire-feed.json", home, "homepage wire JSON entrance")
    require("Research &amp; News", news, "Research & News page")
    require("/feed.xml", news, "Research & News verified feed entrance")

    # Newly launched contribution flows must not deploy an older pre-launch page.
    require("A functional browser/PWA client now exists", fieldwork, "Fieldwork public route")
    require("Open the Fieldwork app", fieldwork, "Fieldwork public route")
    if "installable Fieldwork client is being built" in fieldwork:
        raise AssertionError("Fieldwork public route still serves pre-launch client copy")

    status = json.loads(status_raw)
    devices = json.loads(devices_raw)
    records = devices.get("records")
    device_count = devices.get("record_count")
    if not isinstance(records, list) or not isinstance(device_count, int) or device_count != len(records):
        raise AssertionError("live devices.json record_count contract failed")

    canonical_count = status.get("canonical_model_count")
    scored_count = status.get("scored_report_card_count")
    catalog_updated = status.get("catalog_updated_at")
    if canonical_count != device_count:
        raise AssertionError(
            f"live research-state drift: site-status has {canonical_count} models, devices.json has {device_count}"
        )
    if not isinstance(scored_count, int) or scored_count < 0:
        raise AssertionError("live site-status scored_report_card_count contract failed")
    if not isinstance(catalog_updated, str):
        raise AssertionError("live site-status catalog_updated_at contract failed")

    rendered_models = homepage_stat(home, "models").replace(",", "")
    rendered_cards = homepage_stat(home, "report-cards").replace(",", "")
    rendered_freshness = homepage_stat(home, "freshness")
    if rendered_models != str(canonical_count):
        raise AssertionError(
            f"homepage model count drift: rendered {rendered_models}, canonical live status {canonical_count}"
        )
    if rendered_cards != str(scored_count):
        raise AssertionError(
            f"homepage Report Card drift: rendered {rendered_cards}, live status {scored_count}"
        )
    expected_freshness = display_date(catalog_updated)
    if rendered_freshness != expected_freshness:
        raise AssertionError(
            f"homepage freshness drift: rendered {rendered_freshness!r}, expected {expected_freshness!r}"
        )

    list_count = rendered_catalog_count(the_list)
    if list_count != canonical_count:
        raise AssertionError(
            f"The List count drift: rendered {list_count}, canonical live status {canonical_count}"
        )

    for guide_path in GUIDE_PATHS:
        guide_raw, _ = fetch(base, guide_path, cache_bust)
        guide_count = guide_catalog_count(guide_raw.decode("utf-8"), guide_path)
        if guide_count != canonical_count:
            raise AssertionError(
                f"{guide_path}: rendered {guide_count} canonical models, live status {canonical_count}"
            )

    verified_rss = ET.fromstring(verified_rss_raw)
    if verified_rss.tag.lower() != "rss":
        raise AssertionError(f"verified RSS: unexpected root {verified_rss.tag!r}")
    verified_channel = verified_rss.find("channel")
    if verified_channel is None or "Research & News" not in (verified_channel.findtext("title") or ""):
        raise AssertionError("verified RSS: channel/title contract failed")

    wire_rss = ET.fromstring(wire_rss_raw)
    if wire_rss.tag.lower() != "rss":
        raise AssertionError(f"wire RSS: unexpected root {wire_rss.tag!r}")
    wire_channel = wire_rss.find("channel")
    if wire_channel is None or "Across the Wire" not in (wire_channel.findtext("title") or ""):
        raise AssertionError("wire RSS: channel/title contract failed")

    verified_json = json.loads(verified_json_raw)
    if not str(verified_json.get("version", "")).startswith("https://jsonfeed.org/version/"):
        raise AssertionError("verified JSON Feed: version contract failed")
    if "Research & News" not in str(verified_json.get("title", "")):
        raise AssertionError("verified JSON Feed: title contract failed")
    if not isinstance(verified_json.get("items"), list):
        raise AssertionError("verified JSON Feed: items must be a list")

    wire_json = json.loads(wire_json_raw)
    if not str(wire_json.get("version", "")).startswith("https://jsonfeed.org/version/"):
        raise AssertionError("wire JSON Feed: version contract failed")
    if "Across the Wire" not in str(wire_json.get("title", "")):
        raise AssertionError("wire JSON Feed: title contract failed")
    if not isinstance(wire_json.get("items"), list):
        raise AssertionError("wire JSON Feed: items must be a list")

    for label, content_type in (
        ("verified RSS", verified_rss_type),
        ("wire RSS", wire_rss_type),
        ("verified JSON Feed", verified_json_type),
        ("wire JSON Feed", wire_json_type),
    ):
        if "text/html" in content_type.lower():
            raise AssertionError(f"{label}: served as HTML ({content_type})")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-url", default=DEFAULT_BASE)
    parser.add_argument("--expected-sha")
    parser.add_argument("--attempts", type=int, default=12)
    parser.add_argument("--sleep-seconds", type=float, default=15)
    args = parser.parse_args()

    last_error: Exception | None = None
    for attempt in range(1, args.attempts + 1):
        cache_bust = f"{args.expected_sha or 'runtime'}-{int(time.time())}-{attempt}"
        try:
            validate_snapshot(args.base_url, args.expected_sha, cache_bust)
            sha_note = f" at {args.expected_sha}" if args.expected_sha else ""
            print(f"Public surfaces and rendered research state verified{sha_note}.")
            return 0
        except (AssertionError, json.JSONDecodeError, ET.ParseError, urllib.error.URLError, ValueError) as exc:
            last_error = exc
            print(f"Attempt {attempt}/{args.attempts} failed: {exc}")
            if attempt < args.attempts:
                time.sleep(args.sleep_seconds)

    raise SystemExit(f"Public-surface smoke test failed: {last_error}")


if __name__ == "__main__":
    raise SystemExit(main())
