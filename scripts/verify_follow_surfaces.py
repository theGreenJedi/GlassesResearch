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
    script = (ROOT / "docs/javascripts/verified-research-alerts.js").read_text(encoding="utf-8")
    styles = (ROOT / "docs/stylesheets/verified-research-alerts.css").read_text(encoding="utf-8")
    research = (ROOT / "docs/RESEARCH_NEWS.md").read_text(encoding="utf-8")

    require(template, 'rel="alternate" type="application/rss+xml"', "RSS autodiscovery")
    require(template, "/feed.xml", "autodiscovered feed URL")
    require(template, "gr-follow-footer", "global follow footer")
    require(template, "Email alerts", "footer email-alert link")
    require(template, "feedly.com/i/discover/sources/search/feed/", "footer Feedly handoff")

    require(script, 'className = "follow-research"', "Research & News follow card")
    require(script, "#verified-research-alerts", "alert-form handoff")
    require(script, "feedly.com/i/discover/sources/search/feed/", "Feedly reader handoff")
    require(script, "inoreader.com/feed/", "Inoreader reader handoff")
    require(script, "data-copy-feed", "copy-feed control")
    require(script, "navigator.clipboard", "clipboard API")
    require(script, "fallbackCopy", "clipboard fallback")
    require(script, "Watching and unverified discovery items are excluded", "verified-only RSS explanation")

    require(styles, ".follow-research", "follow card styles")
    require(styles, ".gr-follow-footer", "follow footer styles")

    require(research, "data-verified-research-alerts", "existing verified-alert form target")
    require(research, "https://glassesresearch.org/feed.xml", "existing human RSS link")

    print("Follow surface contract valid: email alerts + RSS + Feedly + Inoreader + copy + autodiscovery + footer")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
