#!/usr/bin/env python3
"""Keep verified-research follow surfaces discoverable, truthful, and connected."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FEEDLY_HOME = "https://feedly.com/"
FEEDLY_UNSUPPORTED_PREFIX = "https://feedly.com/i/discover/sources/search/feed/"
INOREADER_PREFIX = "https://www.inoreader.com/feed/"


def require(text: str, needle: str, label: str) -> None:
    if needle not in text:
        raise SystemExit(f"missing {label}: {needle}")


def forbid(text: str, needle: str, label: str) -> None:
    if needle in text:
        raise SystemExit(f"forbidden {label}: {needle}")


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
    require(template, FEEDLY_HOME, "footer Feedly entry point")
    require(template, INOREADER_PREFIX, "footer Inoreader feed handoff")
    forbid(template, FEEDLY_UNSUPPORTED_PREFIX, "unsupported footer Feedly deep link")

    require(alerts_script, 'className = "follow-research"', "Research & News follow card")
    require(alerts_script, "#verified-research-alerts", "alert-form handoff")
    require(alerts_script, "data-copy-feed", "copy-feed control")
    require(alerts_script, "navigator.clipboard", "clipboard API")
    require(alerts_script, "fallbackCopy", "clipboard fallback")
    require(alerts_script, "Watching and unverified discovery items are excluded", "verified-only RSS explanation")

    require(reader_script, f'const FEEDLY_HOME = "{FEEDLY_HOME}";', "stable Feedly entry point")
    require(reader_script, f'const FEEDLY_UNSUPPORTED_PREFIX = "{FEEDLY_UNSUPPORTED_PREFIX}";', "legacy Feedly route rewrite target")
    require(reader_script, "normalizeReaderLinks", "dynamic reader-link normalization")
    require(reader_script, "inoreaderUrl(VERIFIED)", "verified Inoreader handoff")
    require(reader_script, "inoreaderUrl(WIRE)", "wire Inoreader handoff")
    require(reader_script, "Copy RSS URL", "reader-independent fallback")
    require(reader_script, "/docs/FEEDS/#verified-research", "verified reader setup fallback")
    require(reader_script, "/docs/FEEDS/#across-the-wire", "wire reader setup fallback")

    require(feeds, FEEDLY_HOME, "Feedly setup entry point")
    require(feeds, "https://www.inoreader.com/feed/https%3A%2F%2Fglassesresearch.org%2Ffeed.xml", "verified Inoreader handoff")
    require(feeds, "https://www.inoreader.com/feed/https%3A%2F%2Fglassesresearch.org%2Fdata%2Fwire-feed.xml", "wire Inoreader handoff")
    require(feeds, "Copy RSS URL", "reader-independent fallback")
    require(feeds, "does not automate tests against third-party reader interfaces", "third-party testing boundary")
    forbid(feeds, FEEDLY_UNSUPPORTED_PREFIX, "unsupported Feedly deep link on feeds page")

    require(styles, ".follow-research", "follow card styles")
    require(styles, ".gr-follow-footer", "follow footer styles")

    require(research, "data-verified-research-alerts", "existing verified-alert form target")
    require(research, "https://glassesresearch.org/feed.xml", "existing human RSS link")

    print("Follow surface contract valid: canonical feeds + copy fallback + truthful reader entry points + autodiscovery + footer")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
