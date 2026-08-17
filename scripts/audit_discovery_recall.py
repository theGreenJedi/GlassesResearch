#!/usr/bin/env python3
"""Audit discovery-system recall against a human-search regression corpus."""
from __future__ import annotations

import argparse
import json
import os
import re
import urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BENCHMARK = ROOT / "research" / "discovery-benchmark.json"
CONFIG = ROOT / "research" / "discovery-sources.json"
DISCOVERY_DIR = ROOT / "research" / "discovery-candidates"
LEDGER = ROOT / "data" / "model-candidates.json"
CATALOG = ROOT / "models" / "CATALOG.md"
THE_LIST = ROOT / "models" / "THE_LIST.md"

CHANNEL_KEYS = {
    "broad_web": "broad_web_queries",
    "retail": "retail_discovery_queries",
    "developer": "developer_discovery_queries",
    "research": "research_discovery_queries",
    "manufacturer_catalog": "manufacturer_catalog_pages",
}


def norm_text(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", value.lower()).strip()


def norm_url(value: str) -> str:
    parsed = urllib.parse.urlsplit(value)
    return urllib.parse.urlunsplit((parsed.scheme.lower(), parsed.netloc.lower(), parsed.path.rstrip("/"), "", ""))


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def corpus_text() -> str:
    parts: list[str] = []
    if DISCOVERY_DIR.exists():
        for path in DISCOVERY_DIR.glob("*.json"):
            try:
                payload = load_json(path)
            except Exception:
                continue
            for item in payload.get("candidates", []):
                parts.extend(str(item.get(field, "")) for field in ("title", "url", "summary", "query", "source"))
    return norm_text("\n".join(parts))


def known_text() -> str:
    parts = [
        CATALOG.read_text(encoding="utf-8") if CATALOG.exists() else "",
        THE_LIST.read_text(encoding="utf-8") if THE_LIST.exists() else "",
        LEDGER.read_text(encoding="utf-8") if LEDGER.exists() else "",
    ]
    return norm_text("\n".join(parts))


def target_match(target: dict, hay: str) -> bool:
    terms = [target.get("label", ""), *target.get("aliases", [])]
    source = target.get("source_url", "")
    if source and norm_text(norm_url(source)) in hay:
        return True
    for term in terms:
        normalized = norm_text(str(term))
        if normalized and normalized in hay:
            return True
    return False


def audit() -> tuple[list[str], list[str], dict]:
    cfg = load_json(CONFIG)
    benchmark = load_json(BENCHMARK)
    errors: list[str] = []
    warnings: list[str] = []

    if benchmark.get("schema_version") != 1:
        errors.append("discovery benchmark schema_version must be 1")
    targets = benchmark.get("targets", [])
    if not isinstance(targets, list) or not targets:
        errors.append("discovery benchmark must contain targets")
        targets = []

    active_channels = {channel for channel, key in CHANNEL_KEYS.items() if cfg.get(key)}
    missing_channels: dict[str, list[str]] = {}
    for target in targets:
        expected = target.get("expected_channels", [])
        missing = sorted(set(expected) - active_channels)
        if missing:
            missing_channels[str(target.get("id"))] = missing
            errors.append(f"{target.get('id')}: expected discovery channel(s) not configured: {', '.join(missing)}")

    # Manufacturer-backed benchmark products should have their source domain watched
    # directly, not merely depend on a generic search query.
    watched_domains = {
        urllib.parse.urlsplit(url).netloc.lower().removeprefix("www.")
        for url in cfg.get("manufacturer_catalog_pages", [])
    }
    direct_watch_missing: list[str] = []
    for target in targets:
        if "manufacturer_catalog" not in target.get("expected_channels", []):
            continue
        domain = urllib.parse.urlsplit(target.get("source_url", "")).netloc.lower().removeprefix("www.")
        if domain and domain not in watched_domains:
            direct_watch_missing.append(str(target.get("id")))
            errors.append(f"{target.get('id')}: manufacturer domain {domain} is not directly watched")

    observed = corpus_text()
    known = known_text()
    observed_hits = [target["id"] for target in targets if target_match(target, observed)]
    known_hits = [target["id"] for target in targets if target_match(target, known)]
    observed_missing = [target["id"] for target in targets if target["id"] not in observed_hits]
    known_missing = [target["id"] for target in targets if target["id"] not in known_hits]

    if observed_missing:
        warnings.append(
            f"live web-discovery corpus has not yet independently rediscovered {len(observed_missing)}/{len(targets)} benchmark target(s)"
        )
    if known_missing:
        warnings.append(
            f"{len(known_missing)}/{len(targets)} benchmark target(s) are not yet represented in catalog/list/candidate-ledger text"
        )

    metrics = {
        "benchmark_targets": len(targets),
        "active_channels": sorted(active_channels),
        "configuration_coverage_pct": 100.0 if not missing_channels and not direct_watch_missing else 0.0,
        "observed_recall_count": len(observed_hits),
        "observed_recall_pct": round((100.0 * len(observed_hits) / len(targets)), 1) if targets else 0.0,
        "observed_missing": observed_missing,
        "known_coverage_count": len(known_hits),
        "known_coverage_pct": round((100.0 * len(known_hits) / len(targets)), 1) if targets else 0.0,
        "known_missing": known_missing,
    }
    return errors, warnings, metrics


def markdown(errors: list[str], warnings: list[str], metrics: dict) -> str:
    lines = [
        "## Discovery recall benchmark",
        "",
        f"Benchmark targets: **{metrics['benchmark_targets']}**",
        f"Configured discovery lanes: **{', '.join(metrics['active_channels'])}**",
        f"Configuration coverage: **{metrics['configuration_coverage_pct']}%**",
        f"Observed independent rediscovery: **{metrics['observed_recall_count']}/{metrics['benchmark_targets']} ({metrics['observed_recall_pct']}%)**",
        f"Known catalog/ledger coverage: **{metrics['known_coverage_count']}/{metrics['benchmark_targets']} ({metrics['known_coverage_pct']}%)**",
        "",
    ]
    if errors:
        lines += ["### Blocking configuration errors", *[f"- {item}" for item in errors], ""]
    if warnings:
        lines += ["### Recall warnings", *[f"- {item}" for item in warnings], ""]
    if metrics.get("observed_missing"):
        lines += ["### Not yet independently rediscovered", *[f"- {item}" for item in metrics["observed_missing"]], ""]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--github-summary", action="store_true")
    args = parser.parse_args()
    errors, warnings, metrics = audit()
    for error in errors:
        print(f"ERROR: {error}")
    for warning in warnings:
        print(f"WARNING: {warning}")
    print(json.dumps(metrics, indent=2))
    if args.github_summary and os.environ.get("GITHUB_STEP_SUMMARY"):
        summary = Path(os.environ["GITHUB_STEP_SUMMARY"])
        with summary.open("a", encoding="utf-8") as handle:
            handle.write(markdown(errors, warnings, metrics) + "\n")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
