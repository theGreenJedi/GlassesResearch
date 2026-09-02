#!/usr/bin/env python3
"""Keep verified-research follow surfaces discoverable and connected."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def require(text: str, needle: str, label: str) -> None:
    if needle not in text:
        raise SystemExit(f"missing {label}: {needle}")


def main() -> int:
    template = (ROOT / "overrides/main.html").read_text(encoding="utf-8")
    alerts_script = (ROOT / "docs/javascripts/verified-research-alerts.js").read_text(encoding="utf-8")
    reader_script = (ROOT / "docs/javascripts/feed-choice.js").read_text(encoding="utf-8")
    feeds = (ROOT / "docs/FEEDS.md").read_text(encoding="utf-8")
    styles = (ROOT / "docs/stylesheets/verified-research-alerts.css").read_text(encoding="utf-8")
    research = (ROOT / "docs/RESEARCH_NEWS.md").read_text(encoding="utf-8")

    require(template, 'rel="alternate" type="application/rss+xml"', "RSS autodiscovery")
    require(template, "/feed.xml", "verified autodiscovered feed URL")
    require(template, "/data/wire-feed.xml", "wire autodiscovered feed URL")
    require(template, "/docs/FEEDS/", "static feeds-page path")
    require(template, "gr-follow-footer", "global follow footer")
    require(template, "Email alerts", "footer email-alert link")
    require(template, "feedly.com/i/subscription/feed%2F", "current footer Feedly handoff")
    require(template, "inoreader.com/feed/", "footer Inoreader handoff")

    require(alerts_script, 'className = "follow-research"', "Research & News follow card")
    require(alerts_script, "#verified-research-alerts", "alert-form handoff")
    require(alerts_script, "inoreader.com/feed/", "Inoreader reader handoff")
    require(alerts_script, "data-copy-feed", "copy-feed control")
    require(alerts_script, "navigator.clipboard", "clipboard API")
    require(alerts_script, "fallbackCopy", "clipboard fallback")
    require(alerts_script, "Watching and unverified discovery items are excluded", "verified-only RSS explanation")

    require(reader_script, "feedly.com/i/subscription/feed%2F", "current Feedly subscription route")
    require(reader_script, "repairReaderLinks", "legacy Feedly-link repair")
    require(reader_script, "Open in Feedly", "direct Feedly button")
    require(reader_script, "Open in Inoreader", "direct Inoreader button")
    require(reader_script, "/docs/FEEDS/#verified-research", "verified reader setup fallback")
    require(reader_script, "/docs/FEEDS/#across-the-wire", "wire reader setup fallback")

    require(feeds, "feedly.com/i/subscription/feed%2Fhttps%3A%2F%2Fglassesresearch.org%2Ffeed.xml", "verified Feedly button")
    require(feeds, "feedly.com/i/subscription/feed%2Fhttps%3A%2F%2Fglassesresearch.org%2Fdata%2Fwire-feed.xml", "wire Feedly button")
    require(feeds, "inoreader.com/feed/https%3A%2F%2Fglassesresearch.org%2Ffeed.xml", "verified Inoreader button")
    require(feeds, "inoreader.com/feed/https%3A%2F%2Fglassesresearch.org%2Fdata%2Fwire-feed.xml", "wire Inoreader button")
    require(feeds, "Copy RSS URL", "reader-independent fallback")

    require(styles, ".follow-research", "follow card styles")
    require(styles, ".gr-follow-footer", "follow footer styles")

    require(research, "data-verified-research-alerts", "existing verified-alert form target")
    require(research, "https://glassesresearch.org/feed.xml", "existing human RSS link")

    print("Follow surface contract valid: two RSS families + Feedly + Inoreader + copy fallback + autodiscovery + footer")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
