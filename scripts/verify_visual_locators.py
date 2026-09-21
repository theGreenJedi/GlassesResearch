#!/usr/bin/env python3
"""Validate the curated visual-locator network without allowing locator sites to become publication provenance."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
from urllib.parse import urlparse

ALLOWED_CLASSES = {"locator-primary", "locator-router", "locator-secondary"}

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

    providers = locators.get("providers", {})
    locator_hosts: set[str] = set()
    for name, provider in providers.items():
        pclass = provider.get("class")
        domains = provider.get("domains", [])
        if pclass not in ALLOWED_CLASSES:
            errors.append(f"{name}: unsupported locator class {pclass!r}")
        if not domains:
            errors.append(f"{name}: provider has no domains")
        for domain in domains:
            locator_hosts.add(domain.lower())

    locator_count = 0
    for mid, entry in locators.get("records", {}).items():
        if mid not in registry.get("records", {}):
            errors.append(f"{mid}: locator references unknown model")
            continue
        source_url = entry.get("canonical_source_url", "")
        if not source_url or host(source_url) in locator_hosts:
            errors.append(f"{mid}: canonical source must be independent of locator network")

        refs = entry.get("locators", [])
        if not refs:
            errors.append(f"{mid}: record has no locator references")
        for ref in refs:
            locator_count += 1
            provider_name = ref.get("provider", "")
            provider = providers.get(provider_name)
            if provider is None:
                errors.append(f"{mid}: unknown provider {provider_name!r}")
                continue
            if host(ref.get("url", "")) not in {d.lower() for d in provider.get("domains", [])}:
                errors.append(f"{mid}: locator URL does not match provider {provider_name}")

    for mid, rec in registry.get("records", {}).items():
        for field in ("source_url", "source_asset_url", "primary_image"):
            value = rec.get(field)
            if isinstance(value, str) and host(value) in locator_hosts:
                errors.append(f"{mid}: {field} must not use locator-network domains as publication provenance")

    if errors:
        raise SystemExit("\n".join(errors))

    print(
        f"Validated {len(providers)} locator providers and {locator_count} model references; "
        "locator network is excluded from publication provenance"
    )

if __name__ == "__main__":
    main()
