#!/usr/bin/env python3
"""Install and verify GlassesResearch public-route promises."""

from __future__ import annotations

import argparse
import json
import shutil
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

DEFAULT_CONTRACT = Path("data/public-route-contract.json")


def load_contract(path: Path) -> dict:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if payload.get("schema_version") != 1:
        raise ValueError("public-route contract schema_version must be 1")
    routes = payload.get("routes")
    if not isinstance(routes, list) or not routes:
        raise ValueError("public-route contract requires a non-empty routes list")

    seen_canonical: set[str] = set()
    seen_aliases: set[str] = set()
    for index, route in enumerate(routes, start=1):
        if not isinstance(route, dict):
            raise ValueError(f"route {index} must be an object")
        canonical = route.get("canonical")
        validate_route_path(canonical, f"route {index} canonical")
        if canonical in seen_canonical:
            raise ValueError(f"duplicate canonical route: {canonical}")
        if canonical in seen_aliases:
            raise ValueError(f"canonical route is already registered as an alias: {canonical}")
        seen_canonical.add(canonical)

        aliases = route.get("aliases", [])
        if not isinstance(aliases, list):
            raise ValueError(f"{canonical}: aliases must be a list")
        for alias in aliases:
            validate_route_path(alias, f"{canonical} alias")
            if alias == canonical:
                raise ValueError(f"{canonical}: alias duplicates canonical route")
            if alias in seen_canonical or alias in seen_aliases:
                raise ValueError(f"duplicate public route promise: {alias}")
            seen_aliases.add(alias)

        marker = route.get("contains")
        if marker is not None and (not isinstance(marker, str) or not marker):
            raise ValueError(f"{canonical}: contains must be a non-empty string")

    base_url = payload.get("base_url")
    if not isinstance(base_url, str) or not base_url.startswith(("http://", "https://")):
        raise ValueError("public-route contract requires an http(s) base_url")
    return payload


def validate_route_path(value: object, label: str) -> None:
    if not isinstance(value, str) or not value.startswith("/"):
        raise ValueError(f"{label} must be an absolute site path")
    parsed = urllib.parse.urlsplit(value)
    if parsed.scheme or parsed.netloc or parsed.query or parsed.fragment:
        raise ValueError(f"{label} must not contain scheme, host, query, or fragment: {value}")
    if value != "/" and not value.endswith("/"):
        raise ValueError(f"{label} must be a directory-style route ending in '/': {value}")
    if ".." in Path(parsed.path).parts:
        raise ValueError(f"{label} must not escape the site root: {value}")


def artifact_path(site_root: Path, route: str) -> Path:
    if route == "/":
        candidate = site_root / "index.html"
    else:
        candidate = site_root / route.lstrip("/") / "index.html"
    root = site_root.resolve()
    resolved = candidate.resolve()
    resolved.relative_to(root)
    return resolved


def read_marker(path: Path, marker: str | None, label: str) -> None:
    if marker is None:
        return
    text = path.read_text(encoding="utf-8", errors="replace")
    if marker not in text:
        raise AssertionError(f"{label}: missing expected marker {marker!r}")


def install_aliases(contract: dict, site_root: Path) -> int:
    installed = 0
    for route in contract["routes"]:
        canonical = route["canonical"]
        canonical_path = artifact_path(site_root, canonical)
        if not canonical_path.is_file():
            raise AssertionError(f"{canonical}: canonical built page is missing")
        for alias in route.get("aliases", []):
            alias_path = artifact_path(site_root, alias)
            if alias_path.exists():
                if not alias_path.is_file() or alias_path.read_bytes() != canonical_path.read_bytes():
                    raise AssertionError(
                        f"{alias}: compatibility route collides with a different built artifact"
                    )
                continue
            alias_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(canonical_path, alias_path)
            installed += 1
            print(f"Installed compatibility route {alias} -> {canonical}")
    print(f"Public-route aliases installed: {installed}")
    return installed


def verify_sitemap(contract: dict, site_root: Path) -> None:
    sitemap = site_root / "sitemap.xml"
    if not sitemap.is_file():
        raise AssertionError("sitemap.xml is missing from built site")
    text = sitemap.read_text(encoding="utf-8", errors="replace")
    base = contract["base_url"].rstrip("/")

    for route in contract["routes"]:
        canonical_url = f"{base}{route['canonical']}"
        if canonical_url not in text:
            raise AssertionError(f"sitemap.xml is missing canonical route {canonical_url}")
        for alias in route.get("aliases", []):
            alias_url = f"{base}{alias}"
            if alias_url in text:
                raise AssertionError(
                    f"sitemap.xml must not advertise compatibility alias {alias_url}"
                )


def verify_built(contract: dict, site_root: Path) -> None:
    checked = 0
    for route in contract["routes"]:
        canonical = route["canonical"]
        canonical_path = artifact_path(site_root, canonical)
        if not canonical_path.is_file():
            raise AssertionError(f"{canonical}: canonical built page is missing")
        read_marker(canonical_path, route.get("contains"), canonical)
        canonical_bytes = canonical_path.read_bytes()
        checked += 1

        for alias in route.get("aliases", []):
            alias_path = artifact_path(site_root, alias)
            if not alias_path.is_file():
                raise AssertionError(f"{alias}: compatibility route is missing")
            if alias_path.read_bytes() != canonical_bytes:
                raise AssertionError(f"{alias}: compatibility artifact differs from {canonical}")
            read_marker(alias_path, route.get("contains"), alias)
            checked += 1

    verify_sitemap(contract, site_root)
    print(f"Built public-route contract verified: {checked} promised routes.")


def fetch(base_url: str, route: str, cache_bust: str) -> bytes:
    separator = "&" if "?" in route else "?"
    url = (
        f"{base_url.rstrip('/')}{route}"
        f"{separator}{urllib.parse.urlencode({'route_contract': cache_bust})}"
    )
    request = urllib.request.Request(
        url,
        headers={
            "Cache-Control": "no-cache",
            "Pragma": "no-cache",
            "User-Agent": "GlassesResearch-public-route-contract/1.0",
        },
    )
    with urllib.request.urlopen(request, timeout=20) as response:
        if response.status != 200:
            raise AssertionError(f"{route}: expected HTTP 200, got {response.status}")
        return response.read()


def verify_live_once(contract: dict, base_url: str, cache_bust: str) -> None:
    checked = 0
    for route in contract["routes"]:
        canonical = route["canonical"]
        canonical_bytes = fetch(base_url, canonical, cache_bust)
        marker = route.get("contains")
        if marker and marker not in canonical_bytes.decode("utf-8", errors="replace"):
            raise AssertionError(f"{canonical}: live page missing expected marker {marker!r}")
        checked += 1

        for alias in route.get("aliases", []):
            alias_bytes = fetch(base_url, alias, cache_bust)
            if alias_bytes != canonical_bytes:
                raise AssertionError(f"{alias}: live compatibility route differs from {canonical}")
            if marker and marker not in alias_bytes.decode("utf-8", errors="replace"):
                raise AssertionError(f"{alias}: live page missing expected marker {marker!r}")
            checked += 1

    sitemap = fetch(base_url, "/sitemap.xml", cache_bust).decode("utf-8", errors="replace")
    for route in contract["routes"]:
        for alias in route.get("aliases", []):
            alias_url = f"{base_url.rstrip('/')}{alias}"
            if alias_url in sitemap:
                raise AssertionError(f"live sitemap advertises compatibility alias {alias_url}")

    print(f"Live public-route contract verified: {checked} promised routes.")


def verify_live(
    contract: dict,
    base_url: str,
    attempts: int,
    sleep_seconds: float,
) -> None:
    last_error: Exception | None = None
    for attempt in range(1, attempts + 1):
        cache_bust = f"{int(time.time())}-{attempt}"
        try:
            verify_live_once(contract, base_url, cache_bust)
            return
        except (
            AssertionError,
            urllib.error.URLError,
            urllib.error.HTTPError,
            UnicodeError,
        ) as exc:
            last_error = exc
            print(f"Attempt {attempt}/{attempts} failed: {exc}", file=sys.stderr)
            if attempt < attempts:
                time.sleep(sleep_seconds)
    raise SystemExit(f"public-route contract failed: {last_error}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--contract", type=Path, default=DEFAULT_CONTRACT)
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("validate")

    install = subparsers.add_parser("install")
    install.add_argument("--site-root", type=Path, default=Path("site"))

    built = subparsers.add_parser("verify-built")
    built.add_argument("--site-root", type=Path, default=Path("site"))

    live = subparsers.add_parser("verify-live")
    live.add_argument("--base-url")
    live.add_argument("--attempts", type=int, default=3)
    live.add_argument("--sleep-seconds", type=float, default=10)

    args = parser.parse_args()
    contract = load_contract(args.contract)

    if args.command == "validate":
        route_count = len(contract["routes"])
        alias_count = sum(len(route.get("aliases", [])) for route in contract["routes"])
        print(f"Public-route contract valid: {route_count} canonical routes, {alias_count} aliases.")
        return 0

    if args.command == "install":
        install_aliases(contract, args.site_root)
        return 0

    if args.command == "verify-built":
        verify_built(contract, args.site_root)
        return 0

    if args.command == "verify-live":
        base_url = args.base_url or contract["base_url"]
        verify_live(contract, base_url, args.attempts, args.sleep_seconds)
        return 0

    raise AssertionError("unreachable")


if __name__ == "__main__":
    raise SystemExit(main())
