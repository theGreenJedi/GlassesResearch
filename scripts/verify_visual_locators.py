#!/usr/bin/env python3
"""Validate third-party visual locators without allowing them to become publication sources."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
from urllib.parse import urlparse

LOCATOR_HOSTS = {"smartglassesgeek.com", "www.smartglassesgeek.com"}

def host(url: str) -> str:
    return (urlparse(url).hostname or "").lower()

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--registry", required=True)
    ap.add_argument("--locators", required=True)
    args = ap.parse_args()

    registry = json.loads(Path(args.registry).read_text(encoding="utf-8"))
    locators = json.loads(Path(args.locators).read_text(encoding="utf-8"))
    errors: list[str] = []

    for mid, entry in locators.get("records", {}).items():
        if mid not in registry.get("records", {}):
            errors.append(f"{mid}: locator references unknown model")
            continue
        locator_url = entry.get("locator_url", "")
        source_url = entry.get("canonical_source_url", "")
        if host(locator_url) not in LOCATOR_HOSTS:
            errors.append(f"{mid}: locator_url is not Smart Glasses Geek")
        if not source_url or host(source_url) in LOCATOR_HOSTS:
            errors.append(f"{mid}: canonical source must be independent of locator provider")

    for mid, rec in registry.get("records", {}).items():
        for field in ("source_url", "source_asset_url", "primary_image"):
            value = rec.get(field)
            if isinstance(value, str) and host(value) in LOCATOR_HOSTS:
                errors.append(f"{mid}: {field} must not use Smart Glasses Geek as publication provenance")

    if errors:
        raise SystemExit("\n".join(errors))

    print(f"Validated {len(locators.get('records', {}))} visual locators; locator provider is not used as publication provenance")

if __name__ == "__main__":
    main()
