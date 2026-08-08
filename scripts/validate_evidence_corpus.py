#!/usr/bin/env python3
"""Validate the GlassesResearch evidence corpus."""

from __future__ import annotations

import json
import re
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "evidence" / "resources.json"
ID_RE = re.compile(r"^EV-(\d{4})$")
ALLOWED_STATES = {
    "regulatory-primary",
    "vendor-primary",
    "community-primary",
    "community-report",
    "GlassesResearch-verified",
}


def fail(message: str) -> None:
    raise SystemExit(f"Evidence corpus validation failed: {message}")


def main() -> None:
    data = json.loads(SOURCE.read_text(encoding="utf-8"))
    resources = data.get("resources")
    if not isinstance(resources, list) or not resources:
        fail("resources must be a non-empty list")

    seen_ids: set[str] = set()
    seen_urls: set[str] = set()
    expected = 1
    for item in resources:
        if not isinstance(item, dict):
            fail("every resource must be an object")
        rid = item.get("id")
        match = ID_RE.match(str(rid))
        if not match:
            fail(f"invalid resource id: {rid!r}")
        if int(match.group(1)) != expected:
            fail(f"expected EV-{expected:04d}, found {rid}")
        expected += 1
        if rid in seen_ids:
            fail(f"duplicate id: {rid}")
        seen_ids.add(rid)

        for key in ("title", "type", "url", "evidence_state", "last_verified", "why_it_matters"):
            value = item.get(key)
            if not isinstance(value, str) or not value.strip():
                fail(f"{rid} missing non-empty {key}")

        url = item["url"]
        parsed = urlparse(url)
        if parsed.scheme not in {"http", "https"} or not parsed.netloc:
            fail(f"{rid} has invalid URL: {url}")
        if url in seen_urls:
            fail(f"duplicate URL: {url}")
        seen_urls.add(url)

        if item["evidence_state"] not in ALLOWED_STATES:
            fail(f"{rid} has invalid evidence_state: {item['evidence_state']}")
        if not isinstance(item.get("platforms"), list) or not item["platforms"]:
            fail(f"{rid} must identify at least one platform")
        if not isinstance(item.get("topics"), list) or not item["topics"]:
            fail(f"{rid} must identify at least one topic")
        if not isinstance(item.get("preserve"), bool):
            fail(f"{rid} preserve must be boolean")

    print(f"Evidence corpus valid: {len(resources)} concrete resources")


if __name__ == "__main__":
    main()
