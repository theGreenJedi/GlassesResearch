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
    "community": "community_discovery_queries",
    "manufacturer_catalog": "manufacturer_catalog_pages",
}
WATCH_CHANNELS = {"research_watch", "community_watch", "retail_watch"}


def norm_text(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", value.lower()).strip()


def norm_url(value: str) -> str:
    parsed = urllib.parse.urlsplit(value)
    return urllib.parse.urlunsplit((parsed.scheme.lower(), parsed.netloc.lower(), parsed.path.rstrip("/"), "", ""))


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def corpus_text(*, include_watches: bool) -> str:
    parts: list[str] = []
    if DISCOVERY_DIR.exists():
        for path in DISCOVERY_DIR.glob("*.json"):
            try:
                payload = load_json(path)
            except Exception:
                continue
            for item in payload.get("candidates", []):
                channels = set(str(item.get("discovery_channel", "")).split("+"))
                if not include_watches and channels & WATCH_CHANNELS:
                    continue
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


def matches(targets: list[dict], hay: str) -> list[str]:
    return [str(target["id"]) for target in targets if target_match(target, hay)]


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

    independent = corpus_text(include_watches=False)
    retained = corpus_text(include_watches=True)
    known = known_text()
    independent_hits = matches(targets, independent)
    retained_hits = matches(targets, retained)
    known_hits = matches(targets, known)
    independent_missing = [str(target["id"]) for target in targets if str(target["id"]) not in independent_hits]
    retained_missing = [str(target["id"]) for target in targets if str(target["id"]) not in retained_hits]
    known_missing = [str(target["id"]) for target in targets if str(target["id"]) not in known_hits]

    # Product/model discovery is the critical regression this mission is meant to fix.
    model_targets = [target for target in targets if target.get("kind") in {"model", "family", "commercial_lead"}]
    independent_model_hits = matches(model_targets, independent)
    independent_model_missing = [str(target["id"]) for target in model_targets if str(target["id"]) not in independent_model_hits]

    if independent_missing:
        warnings.append(
            f"broad-query discovery has not independently rediscovered {len(independent_missing)}/{len(targets)} benchmark target(s)"
        )
    if retained_missing:
        errors.append(
            f"durable discovery coverage is missing {len(retained_missing)}/{len(targets)} benchmark target(s): {', '.join(retained_missing)}"
        )
    if independent_model_missing:
        warnings.append(
            f"independent product/model recall is {len(independent_model_hits)}/{len(model_targets)}; missing: {', '.join(independent_model_missing)}"
        )
    if known_missing:
        warnings.append(
            f"{len(known_missing)}/{len(targets)} benchmark target(s) are not yet represented in catalog/list/candidate-ledger text"
        )

    def pct(hit_count: int, total: int) -> float:
        return round((100.0 * hit_count / total), 1) if total else 0.0

    metrics = {
        "benchmark_targets": len(targets),
        "active_channels": sorted(active_channels),
        "configuration_coverage_pct": 100.0 if not missing_channels and not direct_watch_missing else 0.0,
        "independent_recall_count": len(independent_hits),
        "independent_recall_pct": pct(len(independent_hits), len(targets)),
        "independent_missing": independent_missing,
        "independent_model_targets": len(model_targets),
        "independent_model_recall_count": len(independent_model_hits),
        "independent_model_recall_pct": pct(len(independent_model_hits), len(model_targets)),
        "independent_model_missing": independent_model_missing,
        "retained_coverage_count": len(retained_hits),
        "retained_coverage_pct": pct(len(retained_hits), len(targets)),
        "retained_missing": retained_missing,
        "known_coverage_count": len(known_hits),
        "known_coverage_pct": pct(len(known_hits), len(targets)),
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
        f"Independent broad-query recall: **{metrics['independent_recall_count']}/{metrics['benchmark_targets']} ({metrics['independent_recall_pct']}%)**",
        f"Independent product/model recall: **{metrics['independent_model_recall_count']}/{metrics['independent_model_targets']} ({metrics['independent_model_recall_pct']}%)**",
        f"Retained benchmark coverage (including durable watches): **{metrics['retained_coverage_count']}/{metrics['benchmark_targets']} ({metrics['retained_coverage_pct']}%)**",
        f"Known catalog/ledger coverage: **{metrics['known_coverage_count']}/{metrics['benchmark_targets']} ({metrics['known_coverage_pct']}%)**",
        "",
        "Independent recall excludes durable watch entries; retained coverage includes them. This prevents known-source watches from inflating broad-search recall.",
        "",
    ]
    if errors:
        lines += ["### Blocking discovery errors", *[f"- {item}" for item in errors], ""]
    if warnings:
        lines += ["### Recall warnings", *[f"- {item}" for item in warnings], ""]
    if metrics.get("independent_missing"):
        lines += ["### Not yet independently rediscovered", *[f"- {item}" for item in metrics["independent_missing"]], ""]
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
