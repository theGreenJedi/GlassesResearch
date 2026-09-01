#!/usr/bin/env python3
"""Compile news.update_story packages through the proven canonical news actuator.

The core news actuator deliberately began with exact ``news.publish`` scope. This
wrapper extends it only to packages whose complete approved route set is a non-empty
subset of ``news.publish`` / ``news.update_story`` and includes ``news.update_story``.
The resulting update is a new dated verified change/article, never an in-place rewrite
of historical newsroom prose.
"""
from __future__ import annotations

import argparse
from pathlib import Path

import newsroom_news_actuator as core

ROOT = Path(__file__).resolve().parents[1]
PACKAGES = ROOT / "research" / "newsroom-packages"
NEWS_ROUTES = {"news.publish", "news.update_story"}


def eligible(route_set: set[str]) -> bool:
    return bool(route_set) and "news.update_story" in route_set and route_set.issubset(NEWS_ROUTES)


def process(path: Path, root: Path = ROOT) -> tuple[str, str]:
    package_id, package = core.load_envelope(path)
    route_set = core.destinations(package)
    if not eligible(route_set):
        return package_id, "not_story_update_scope"
    previous = core.SAFE_ROUTES
    try:
        core.SAFE_ROUTES = set(route_set)
        return core.apply_package(root, path)
    finally:
        core.SAFE_ROUTES = previous


def process_all(package_dir: Path = PACKAGES, root: Path = ROOT) -> dict[str, int]:
    outcomes: dict[str, int] = {}
    for path in sorted(package_dir.glob("GRNP-*.json")):
        package_id, package = core.load_envelope(path)
        route_set = core.destinations(package)
        if not eligible(route_set):
            continue
        _pid, outcome = process(path, root)
        assert _pid == package_id
        outcomes[outcome] = outcomes.get(outcome, 0) + 1
    return outcomes


def self_test() -> None:
    assert eligible({"news.update_story"})
    assert eligible({"news.publish", "news.update_story"})
    assert not eligible({"news.publish"})
    assert not eligible({"news.update_story", "catalog.update"})
    assert not eligible(set())
    print("Newsroom story-update actuator scope self-test passed.")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--package", type=Path)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return 0
    if args.package:
        package_id, outcome = process(args.package)
        print(f"{package_id}: {outcome}")
        return 0
    if args.all:
        outcomes = process_all()
        summary = ", ".join(f"{key}={value}" for key, value in sorted(outcomes.items())) or "none"
        print(f"Story-update actuator outcomes: {summary}.")
        return 0
    parser.error("use --all, --package, or --self-test")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
