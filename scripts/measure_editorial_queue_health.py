#!/usr/bin/env python3
"""Measure GlassesResearch editorial-queue aging and verified throughput.

This script is observability only. It reads durable triage state and reports how long
reviewable candidates have been waiting. It never changes editorial disposition,
publication authorization, verification state, or research claims.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import math
import pathlib
import statistics
from collections import Counter

ROOT = pathlib.Path(__file__).resolve().parents[1]
DEFAULT_QUEUE = ROOT / "research/news-reviews/queue.json"
DEFAULT_JSON = ROOT / "research/news-reviews/health.json"
DEFAULT_MARKDOWN = ROOT / "research/news-reviews/health.md"
ACTIONABLE_STATES = {"needs_editorial_verification", "source_review"}


def parse_stamp(value: object) -> dt.datetime | None:
    text = str(value or "").strip()
    if not text:
        return None
    try:
        stamp = dt.datetime.fromisoformat(text.replace("Z", "+00:00"))
    except ValueError:
        return None
    if stamp.tzinfo is None:
        stamp = stamp.replace(tzinfo=dt.timezone.utc)
    return stamp.astimezone(dt.timezone.utc)


def nearest_rank(values: list[float], percentile: float) -> float | None:
    if not values:
        return None
    ordered = sorted(values)
    rank = max(1, math.ceil(percentile * len(ordered)))
    return ordered[rank - 1]


def rounded(value: float | None) -> float | None:
    return None if value is None else round(value, 1)


def age_hours(item: dict, now: dt.datetime) -> float | None:
    stamp = parse_stamp(item.get("first_seen_utc"))
    if stamp is None:
        return None
    return max(0.0, (now - stamp).total_seconds() / 3600.0)


def age_summary(items: list[dict], now: dt.datetime) -> dict:
    ages = [age for item in items if (age := age_hours(item, now)) is not None]
    return {
        "count": len(items),
        "age_known_count": len(ages),
        "median_age_hours": rounded(statistics.median(ages) if ages else None),
        "p90_age_hours": rounded(nearest_rank(ages, 0.90)),
        "max_age_hours": rounded(max(ages) if ages else None),
        "over_24h": sum(age > 24 for age in ages),
        "over_72h": sum(age > 72 for age in ages),
        "over_168h": sum(age > 168 for age in ages),
    }


def resolved_within(items: list[dict], now: dt.datetime, hours: int) -> int:
    cutoff = now - dt.timedelta(hours=hours)
    count = 0
    for item in items:
        if str(item.get("triage_state", "")) != "editorial_published":
            continue
        stamp = parse_stamp(item.get("resolved_utc"))
        if stamp is not None and cutoff <= stamp <= now:
            count += 1
    return count


def build_health(queue: dict) -> dict:
    now = parse_stamp(queue.get("generated_utc")) or dt.datetime.now(dt.timezone.utc)
    candidates = [item for item in queue.get("candidates", []) if isinstance(item, dict)]
    pending = [
        item for item in candidates
        if str(item.get("editorial_disposition", "pending")) == "pending"
        and str(item.get("triage_state", "")) in ACTIONABLE_STATES
    ]
    verification = [item for item in pending if str(item.get("triage_state", "")) == "needs_editorial_verification"]
    high = [item for item in pending if str(item.get("triage_priority", "")) == "high"]
    high_verification = [
        item for item in verification if str(item.get("triage_priority", "")) == "high"
    ]

    published = [item for item in candidates if str(item.get("triage_state", "")) == "editorial_published"]
    oldest_high = sorted(
        (
            {
                "id": str(item.get("id", "")),
                "title": str(item.get("title", "")),
                "url": str(item.get("url", "")),
                "triage_state": str(item.get("triage_state", "")),
                "age_hours": rounded(age_hours(item, now)),
            }
            for item in high
            if age_hours(item, now) is not None
        ),
        key=lambda row: float(row["age_hours"] or 0),
        reverse=True,
    )[:10]

    return {
        "schema": 1,
        "generated_utc": now.isoformat(),
        "source_queue_generated_utc": queue.get("generated_utc"),
        "publication_authority": "none",
        "semantics": "Observability only; age and throughput metrics never authorize publication or strengthen evidence.",
        "state_counts": dict(sorted(Counter(str(x.get("triage_state", "unknown")) for x in candidates).items())),
        "actionable_pending": age_summary(pending, now),
        "needs_editorial_verification": age_summary(verification, now),
        "high_priority_actionable": age_summary(high, now),
        "high_priority_needs_editorial_verification": age_summary(high_verification, now),
        "verified_publication_throughput": {
            "retained_published_total": len(published),
            "resolved_last_24h": resolved_within(candidates, now, 24),
            "resolved_last_7d": resolved_within(candidates, now, 24 * 7),
            "resolved_last_14d": resolved_within(candidates, now, 24 * 14),
        },
        "oldest_high_priority_actionable": oldest_high,
    }


def fmt_hours(value: object) -> str:
    if value is None:
        return "unknown"
    return f"{float(value):.1f} h"


def markdown(health: dict) -> str:
    actionable = health["actionable_pending"]
    verify = health["needs_editorial_verification"]
    high = health["high_priority_actionable"]
    high_verify = health["high_priority_needs_editorial_verification"]
    throughput = health["verified_publication_throughput"]
    lines = [
        "# Editorial queue health — latest",
        "",
        f"Generated: `{health['generated_utc']}`",
        "",
        "> **Observability only.** These metrics do not authorize publication, verification, or evidence promotion.",
        "",
        "## Queue aging",
        "",
        "| Slice | Count | Median age | P90 age | Max age | >24 h | >72 h | >7 d |",
        "|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for label, row in (
        ("All actionable pending", actionable),
        ("Needs editorial verification", verify),
        ("High-priority actionable", high),
        ("High-priority needs verification", high_verify),
    ):
        lines.append(
            f"| {label} | {row['count']} | {fmt_hours(row['median_age_hours'])} | "
            f"{fmt_hours(row['p90_age_hours'])} | {fmt_hours(row['max_age_hours'])} | "
            f"{row['over_24h']} | {row['over_72h']} | {row['over_168h']} |"
        )

    lines += [
        "",
        "## Verified-publication throughput",
        "",
        f"- Retained published total: **{throughput['retained_published_total']}**",
        f"- Resolved/published in last 24 h: **{throughput['resolved_last_24h']}**",
        f"- Resolved/published in last 7 d: **{throughput['resolved_last_7d']}**",
        f"- Resolved/published in last 14 d: **{throughput['resolved_last_14d']}**",
        "",
        "## Oldest high-priority actionable candidates",
        "",
        "| Age | State | Candidate |",
        "|---:|---|---|",
    ]
    for item in health.get("oldest_high_priority_actionable", []):
        title = str(item.get("title", "")).replace("|", "\\|").replace("\n", " ")[:160]
        url = str(item.get("url", ""))
        lines.append(
            f"| {fmt_hours(item.get('age_hours'))} | {item.get('triage_state', '')} | [{title}]({url}) |"
        )
    if not health.get("oldest_high_priority_actionable"):
        lines.append("| — | — | No high-priority actionable candidates with a known first-seen timestamp. |")

    lines += [
        "",
        "The purpose of this report is to expose queue pressure and aging so editorial attention can be prioritized without lowering the verification threshold.",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--queue", type=pathlib.Path, default=DEFAULT_QUEUE)
    parser.add_argument("--json-output", type=pathlib.Path, default=DEFAULT_JSON)
    parser.add_argument("--markdown-output", type=pathlib.Path, default=DEFAULT_MARKDOWN)
    config = parser.parse_args()

    queue = json.loads(config.queue.read_text(encoding="utf-8"))
    health = build_health(queue)
    config.json_output.parent.mkdir(parents=True, exist_ok=True)
    config.json_output.write_text(json.dumps(health, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    config.markdown_output.write_text(markdown(health), encoding="utf-8")
    print(
        "Editorial queue health measured: "
        f"{health['needs_editorial_verification']['count']} need verification; "
        f"{health['high_priority_actionable']['count']} high-priority actionable; "
        f"{health['verified_publication_throughput']['resolved_last_7d']} published/resolved in 7d."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
