#!/usr/bin/env python3
"""Smoke-test the reader-facing publication and feed surfaces on production."""

from __future__ import annotations

import argparse
import json
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET


DEFAULT_BASE = "https://glassesresearch.org"


def fetch(base: str, path: str, cache_bust: str) -> tuple[bytes, str]:
    separator = "&" if "?" in path else "?"
    url = f"{base.rstrip('/')}{path}{separator}{urllib.parse.urlencode({'smoke': cache_bust})}"
    request = urllib.request.Request(
        url,
        headers={
            "Cache-Control": "no-cache",
            "Pragma": "no-cache",
            "User-Agent": "GlassesResearch-public-surface-smoke/1.0",
        },
    )
    with urllib.request.urlopen(request, timeout=20) as response:
        return response.read(), response.headers.get("Content-Type", "")


def require(needle: str, haystack: str, label: str) -> None:
    if needle not in haystack:
        raise AssertionError(f"{label}: missing {needle!r}")


def validate_snapshot(base: str, expected_sha: str | None, cache_bust: str) -> None:
    deployment_raw, _ = fetch(base, "/deployment.json", cache_bust)
    deployment = json.loads(deployment_raw)
    if expected_sha:
        actual = deployment.get("sha")
        if actual != expected_sha:
            raise AssertionError(f"stale production: expected {expected_sha}, got {actual}")

    home_raw, _ = fetch(base, "/", cache_bust)
    news_raw, _ = fetch(base, "/docs/RESEARCH_NEWS/", cache_bust)
    verified_rss_raw, verified_rss_type = fetch(base, "/feed.xml", cache_bust)
    verified_json_raw, verified_json_type = fetch(base, "/feed.json", cache_bust)
    wire_rss_raw, wire_rss_type = fetch(base, "/data/wire-feed.xml", cache_bust)
    wire_json_raw, wire_json_type = fetch(base, "/data/wire-feed.json", cache_bust)

    home = home_raw.decode("utf-8")
    news = news_raw.decode("utf-8")
    require("Research &amp; News", home, "homepage")
    require("/feed.xml", home, "homepage verified feed entrance")
    require("/data/wire-feed.xml", home, "homepage wire RSS entrance")
    require("/data/wire-feed.json", home, "homepage wire JSON entrance")
    require("Research &amp; News", news, "Research & News page")
    require("/feed.xml", news, "Research & News verified feed entrance")

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

    # Content-Type is advisory on GitHub Pages, but obvious HTML responses for feed URLs are failures.
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
            print(f"Public follow surfaces verified{sha_note}.")
            return 0
        except (AssertionError, json.JSONDecodeError, ET.ParseError, urllib.error.URLError) as exc:
            last_error = exc
            print(f"Attempt {attempt}/{args.attempts} failed: {exc}")
            if attempt < args.attempts:
                time.sleep(args.sleep_seconds)

    raise SystemExit(f"Public follow-surface smoke test failed: {last_error}")


if __name__ == "__main__":
    raise SystemExit(main())
