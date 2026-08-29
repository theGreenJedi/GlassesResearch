#!/usr/bin/env python3
"""Verify the generated reader-facing newsroom state."""
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

SITE_ORIGIN = "https://glassesresearch.org/"


def stamp(value: str) -> datetime:
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--state", type=Path, required=True)
    args = parser.parse_args()
    state = json.loads(args.state.read_text(encoding="utf-8"))

    if state.get("schema_version") != 1:
        raise SystemExit("Newsroom state schema version must be 1")
    serialized = json.dumps(state)
    if "alert_match" in serialized:
        raise SystemExit("Newsroom state leaked internal alert routing")

    latest = state.get("latest") or []
    if not latest:
        raise SystemExit("Newsroom state must contain latest verified stories")
    dates = [stamp(item["published_at"]) for item in latest]
    if dates != sorted(dates, reverse=True):
        raise SystemExit("Newsroom latest stories are not newest-first")
    if state.get("latest_verified_at") != latest[0]["published_at"]:
        raise SystemExit("Newsroom freshness timestamp drifted from latest story")

    known_ids = {item["event_id"] for item in latest}
    lead = state.get("lead")
    if not lead or lead.get("event_id") not in known_ids:
        raise SystemExit("Newsroom lead is not present in the current latest desk")

    for item in [lead, *latest]:
        url = str(item.get("url", ""))
        if not url.startswith(SITE_ORIGIN):
            raise SystemExit(f"Newsroom story leaves GlassesResearch canonical publication surface: {url}")

    for theme in state.get("convergence") or []:
        story_ids = theme.get("story_ids") or []
        if len(set(story_ids)) < 2:
            raise SystemExit(f"Convergence theme lacks independent story signals: {theme.get('label')}")
        if int(theme.get("independent_source_hosts", 0)) < 2:
            raise SystemExit(f"Convergence theme lacks independent source families: {theme.get('label')}")
        if len(theme.get("stories") or []) < 2:
            raise SystemExit(f"Convergence theme lacks reader-facing supporting stories: {theme.get('label')}")

    print(
        f"Newsroom state verified: lead={lead['event_id']}, latest={len(latest)}, "
        f"convergence={len(state.get('convergence') or [])}, freshness={state['latest_verified_at']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
