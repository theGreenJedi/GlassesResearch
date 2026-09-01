#!/usr/bin/env python3
"""Annotate Core Report Cards with evidence freshness and build a refresh queue.

Freshness is intentionally conservative: rebuilding the site never refreshes a score.
Only a score-specific verification date can establish fresh/aging/stale status. A
model-level comparison review date is retained as context, but it is never promoted
into a score verification date.
"""
from __future__ import annotations

import argparse
import json
from collections import Counter
from datetime import date, datetime, timedelta
from pathlib import Path

FRESHNESS_POLICIES = {
    "discreetness": {
        "max_age_days": 365,
        "reason": "Physical form and social presentation usually change slowly unless the hardware revision changes.",
    },
    "camera": {
        "max_age_days": 365,
        "reason": "Camera hardware is comparatively stable; a new hardware revision or material firmware change should trigger earlier review.",
    },
    "visual_ai": {
        "max_age_days": 90,
        "reason": "Visual-AI behavior, model access, service boundaries, and assistant capabilities can change quickly.",
    },
    "hackability": {
        "max_age_days": 120,
        "reason": "SDKs, APIs, firmware paths, community tooling, and reverse-engineering surfaces evolve over time.",
    },
    "owner_control": {
        "max_age_days": 90,
        "reason": "Accounts, cloud dependencies, custom endpoints, local processing, and vendor restrictions can change quickly.",
    },
    "android_compatibility": {
        "max_age_days": 120,
        "reason": "Companion apps, Android releases, permissions, SDK support, and platform restrictions are moving targets.",
    },
}

RESOLVED = lambda value: isinstance(value, (int, float)) or str(value).lower() == "na"


def load(path: Path | None) -> dict:
    if not path or not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def parse_day(value: object) -> date | None:
    if not value:
        return None
    try:
        return datetime.strptime(str(value), "%Y-%m-%d").date()
    except ValueError:
        return None


def comparison_review_dates(payload: dict) -> dict[str, str]:
    found: dict[str, str] = {}
    for record in payload.get("records", []):
        model_id = str(record.get("id", ""))
        entry = record.get("fields", {}).get("last_reviewed", {})
        reviewed = parse_day(entry.get("value")) if isinstance(entry, dict) else None
        evidence = entry.get("evidence") if isinstance(entry, dict) else None
        if model_id and reviewed and evidence not in {"unknown", "unresolved", None}:
            found[model_id] = reviewed.isoformat()
    return found


def override_score_metadata(payload: dict) -> dict[str, dict[str, dict]]:
    found: dict[str, dict[str, dict]] = {}
    for record in payload.get("records", []):
        model_id = str(record.get("id", ""))
        scores = record.get("scores", {})
        if not model_id or not isinstance(scores, dict):
            continue
        found[model_id] = {
            dimension: value
            for dimension, value in scores.items()
            if isinstance(value, dict)
        }
    return found


def freshness_state(verified: date | None, as_of: date, max_age_days: int) -> tuple[str, int | None, str | None]:
    if not verified:
        return "unknown", None, None
    age = (as_of - verified).days
    if age < 0:
        raise ValueError(f"verification date {verified.isoformat()} is after as-of date {as_of.isoformat()}")
    due = verified + timedelta(days=max_age_days)
    if age > max_age_days:
        state = "stale"
    elif age > int(max_age_days * 0.75):
        state = "aging"
    else:
        state = "fresh"
    return state, age, due.isoformat()


def validate_curated_dates(overrides: dict) -> None:
    errors: list[str] = []
    for record in overrides.get("records", []):
        model_id = str(record.get("id", "unknown"))
        for dimension, value in record.get("scores", {}).items():
            if not isinstance(value, dict):
                errors.append(
                    f"{model_id} {dimension}: curated scores must be objects with score/provenance/confidence/verified_at"
                )
                continue
            score = value.get("score")
            if RESOLVED(score) and not parse_day(value.get("verified_at")):
                errors.append(f"{model_id} {dimension}: resolved curated score requires verified_at YYYY-MM-DD")
    if errors:
        raise RuntimeError("Curated Report Card freshness validation failed:\n  " + "\n  ".join(errors))


def render_page(payload: dict, labels: dict[str, str]) -> str:
    summary = payload["summary"]
    queue = payload["refresh_queue"]
    policies = payload["policies"]
    policy_rows = "\n".join(
        f"| **{labels.get(dim, dim.replace('_', ' ').title())}** | {policy['max_age_days']} days | {policy['reason']} |"
        for dim, policy in policies.items()
    )
    queue_rows = []
    for item in queue:
        verified = item.get("verified_at") or "Unknown"
        due = item.get("next_review_due") or "—"
        queue_rows.append(
            f"| [{item['id']}](/models/catalog/{item['id'].lower()}/) | {labels.get(item['dimension'], item['dimension'].replace('_', ' ').title())} | {item['score']} | **{item['freshness'].title()}** | {verified} | {due} | {item['reason']} |"
        )
    queue_table = "\n".join(queue_rows) if queue_rows else "| — | — | — | — | — | — | No scored dimensions currently require refresh. |"
    return f'''---
title: "Report Card Freshness"
description: "Evidence-verification freshness, aging rules, and the refresh queue for GlassesResearch Core Report Cards."
---

# Report Card Freshness

**As of {payload['as_of']}.** Freshness belongs to the evidence supporting a score, not to the page that displays it. Rebuilding or redeploying GlassesResearch never makes an old score fresh.

## Research health

| State | Core subjects |
|---|---:|
| **Fresh** | {summary['fresh']} |
| **Aging** | {summary['aging']} |
| **Stale** | {summary['stale']} |
| **Unknown freshness** | {summary['unknown']} |
| **Unscored subjects** | {summary['unscored']} |

**{summary['cards_with_resolved_scores']} of {summary['card_count']} Core Report Cards currently contain at least one numeric score or N/A judgment.** Of {summary['resolved_dimensions']} resolved Core subjects, {summary['known_freshness_dimensions']} have an explicit score-specific verification date and {summary['unknown']} still need one.

A model-level comparison review date may appear in machine-readable metadata as `context_reviewed_at`. It is useful context, but it **does not** certify that a particular Report Card score was re-verified on that date.

## Freshness policy

A resolved score is **Fresh** through the first 75% of its review interval, **Aging** for the final 25%, and **Stale** after the interval expires. `Unknown freshness` means the score exists but no score-specific verification date has yet been recorded.

| Core subject | Review interval | Why |
|---|---:|---|
{policy_rows}

These are maximum routine review intervals, not promises that a score cannot change sooner. A material product, firmware, service, SDK, app, policy, or ownership change should trigger immediate re-verification of the affected dimensions.

## Refresh queue

Priority is **Stale → Unknown freshness → Aging**. Unscored subjects remain research gaps rather than freshness failures and are not allowed to overwhelm this queue.

| Model | Subject | Score | Freshness | Last verified | Review due | Why queued |
|---|---|---:|---|---|---|---|
{queue_table}

## How a score becomes fresh

A re-review must check the evidence that supports the specific score. When the judgment is still defensible, record `verified_at` for that subject. If the evidence changed, update the score, provenance, confidence, and `verified_at` together. A new site build, catalog update, or unrelated model review is never sufficient by itself.

[Read the Report Card method](/docs/REPORT_CARD_METHOD/) · [Browse all Report Cards](/docs/REPORT_CARD/) · [Submit stronger evidence](/docs/RESEARCH_CHALLENGES/)
'''


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--scores", type=Path, required=True)
    parser.add_argument("--comparisons", type=Path, required=True)
    parser.add_argument("--overrides", type=Path)
    parser.add_argument("--output-scores", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--page-output", type=Path, required=True)
    parser.add_argument("--as-of")
    args = parser.parse_args()

    as_of = parse_day(args.as_of) if args.as_of else date.today()
    if not as_of:
        raise RuntimeError("--as-of must be YYYY-MM-DD")

    scores = load(args.scores)
    comparisons = load(args.comparisons)
    overrides = load(args.overrides)
    validate_curated_dates(overrides)

    dimensions = scores.get("dimensions", [])
    dimension_ids = [item["id"] for item in dimensions]
    labels = {item["id"]: item["label"] for item in dimensions}
    if set(dimension_ids) != set(FRESHNESS_POLICIES):
        raise RuntimeError(f"Freshness policy/Core dimension mismatch: {dimension_ids}")

    context_dates = comparison_review_dates(comparisons)
    curated = override_score_metadata(overrides)
    counts = Counter()
    queue: list[dict] = []
    cards_with_resolved = 0

    for record in scores.get("records", []):
        model_id = record["id"]
        record_meta = record.setdefault("score_meta", {})
        resolved_on_card = 0
        per_card = Counter()
        for dimension in dimension_ids:
            value = record.get("scores", {}).get(dimension, "unknown")
            meta = record_meta.setdefault(dimension, {})
            policy = FRESHNESS_POLICIES[dimension]
            explicit = curated.get(model_id, {}).get(dimension, {})
            verified = parse_day(explicit.get("verified_at"))
            context_reviewed = context_dates.get(model_id)

            if not RESOLVED(value):
                counts["unscored"] += 1
                per_card["unscored"] += 1
                meta.update({
                    "verified_at": None,
                    "freshness": "unknown",
                    "freshness_basis": "unscored",
                    "context_reviewed_at": context_reviewed,
                    "max_age_days": policy["max_age_days"],
                    "age_days": None,
                    "next_review_due": None,
                })
                continue

            resolved_on_card += 1
            state, age, due = freshness_state(verified, as_of, policy["max_age_days"])
            counts[state] += 1
            per_card[state] += 1
            meta.update({
                "verified_at": verified.isoformat() if verified else None,
                "freshness": state,
                "freshness_basis": "score-specific-verification" if verified else "missing-score-specific-verification",
                "context_reviewed_at": context_reviewed,
                "max_age_days": policy["max_age_days"],
                "age_days": age,
                "next_review_due": due,
            })
            if state in {"stale", "unknown", "aging"}:
                if state == "stale":
                    reason = "Routine review interval has expired."
                    priority = 1
                elif state == "unknown":
                    reason = "Resolved score lacks a score-specific verification date."
                    priority = 2
                else:
                    reason = "Score is approaching its routine review deadline."
                    priority = 3
                queue.append({
                    "priority": priority,
                    "id": model_id,
                    "dimension": dimension,
                    "score": value,
                    "freshness": state,
                    "verified_at": verified.isoformat() if verified else None,
                    "context_reviewed_at": context_reviewed,
                    "age_days": age,
                    "next_review_due": due,
                    "max_age_days": policy["max_age_days"],
                    "provenance": meta.get("provenance", "unresolved"),
                    "confidence": meta.get("confidence", "unknown"),
                    "reason": reason,
                })

        if resolved_on_card:
            cards_with_resolved += 1
        record["freshness_summary"] = {
            "resolved_dimensions": resolved_on_card,
            "fresh": per_card["fresh"],
            "aging": per_card["aging"],
            "stale": per_card["stale"],
            "unknown": per_card["unknown"],
            "unscored": per_card["unscored"],
        }

    queue.sort(key=lambda item: (item["priority"], item["next_review_due"] or "9999-12-31", item["id"], item["dimension"]))
    resolved_dimensions = counts["fresh"] + counts["aging"] + counts["stale"] + counts["unknown"]
    known_freshness = counts["fresh"] + counts["aging"] + counts["stale"]
    summary = {
        "card_count": len(scores.get("records", [])),
        "cards_with_resolved_scores": cards_with_resolved,
        "resolved_dimensions": resolved_dimensions,
        "known_freshness_dimensions": known_freshness,
        "fresh": counts["fresh"],
        "aging": counts["aging"],
        "stale": counts["stale"],
        "unknown": counts["unknown"],
        "unscored": counts["unscored"],
        "queue_count": len(queue),
    }

    scores["schema_version"] = max(int(scores.get("schema_version", 2)), 3)
    scores["freshness_as_of"] = as_of.isoformat()
    scores["freshness_semantics"] = "A page rebuild never refreshes evidence. Freshness requires a score-specific verified_at date."
    scores["freshness_policies"] = FRESHNESS_POLICIES
    scores["freshness_summary"] = summary

    freshness = {
        "schema_version": 1,
        "as_of": as_of.isoformat(),
        "semantics": scores["freshness_semantics"],
        "policies": FRESHNESS_POLICIES,
        "summary": summary,
        "refresh_queue": queue,
    }

    args.output_scores.parent.mkdir(parents=True, exist_ok=True)
    args.output_scores.write_text(json.dumps(scores, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(freshness, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    args.page_output.parent.mkdir(parents=True, exist_ok=True)
    args.page_output.write_text(render_page(freshness, labels), encoding="utf-8")

    print(
        f"Report Card freshness: {summary['fresh']} fresh, {summary['aging']} aging, "
        f"{summary['stale']} stale, {summary['unknown']} unknown freshness; "
        f"refresh queue={summary['queue_count']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
