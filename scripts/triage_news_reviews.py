#!/usr/bin/env python3
"""Persist automated triage for the GlassesResearch knowledge-intake conveyor.

This script deliberately stops before factual publication. It turns durable intake
snapshots into a durable triage queue, checks source reachability when requested,
and records which candidates need editorial verification versus Watching/radar.
Existing explicit editorial decisions are preserved across runs.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import pathlib
import re
import urllib.error
import urllib.request
from collections import Counter
from zoneinfo import ZoneInfo

ROOT = pathlib.Path(__file__).resolve().parents[1]
INTAKE_DIRS = (ROOT / "research/news-candidates", ROOT / "research/discovery-candidates")
REVIEWS_DIR = ROOT / "research/news-reviews"
QUEUE_PATH = REVIEWS_DIR / "queue.json"
LATEST_PATH = REVIEWS_DIR / "latest.md"
FINAL_DISPOSITIONS = {"published", "watch", "archived", "superseded", "rejected"}
PRIORITY_ORDER = {"high": 0, "normal": 1, "low": 2}
STATE_ORDER = {
    "needs_editorial_verification": 0,
    "source_review": 1,
    "watching": 2,
    "adjacent_radar": 3,
    "rejected_noise": 4,
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lookback-days", type=int, default=14)
    parser.add_argument("--verify-reachability", action="store_true")
    parser.add_argument("--timeout", type=float, default=12.0)
    return parser.parse_args()


def utc_now() -> dt.datetime:
    return dt.datetime.now(dt.timezone.utc)


def parse_stamp(value: str) -> dt.datetime | None:
    if not value:
        return None
    try:
        stamp = dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
        if stamp.tzinfo is None:
            stamp = stamp.replace(tzinfo=dt.timezone.utc)
        return stamp.astimezone(dt.timezone.utc)
    except ValueError:
        return None


def fallback_stamp(path: pathlib.Path) -> dt.datetime | None:
    match = re.match(r"(\d{4}-\d{2}-\d{2})", path.name)
    if not match:
        return None
    try:
        return dt.datetime.fromisoformat(match.group(1)).replace(tzinfo=dt.timezone.utc)
    except ValueError:
        return None


def candidate_key(item: dict) -> str:
    existing = str(item.get("id", "")).strip()
    if existing:
        return existing
    url = str(item.get("url", "")).strip()
    return hashlib.sha256(url.encode("utf-8")).hexdigest()[:16]


def load_existing_queue() -> dict[str, dict]:
    if not QUEUE_PATH.exists():
        return {}
    try:
        payload = json.loads(QUEUE_PATH.read_text(encoding="utf-8"))
    except Exception:
        return {}
    return {
        str(item.get("id")): item
        for item in payload.get("candidates", [])
        if isinstance(item, dict) and item.get("id")
    }


def collect_candidates(cutoff: dt.datetime) -> tuple[dict[str, dict], list[str]]:
    dedup: dict[str, dict] = {}
    files_seen: list[str] = []
    for directory in INTAKE_DIRS:
        if not directory.exists():
            continue
        for path in sorted(directory.glob("*.json")):
            try:
                payload = json.loads(path.read_text(encoding="utf-8"))
            except Exception:
                continue
            stamp = parse_stamp(str(payload.get("discovered_utc", ""))) or fallback_stamp(path)
            if stamp is not None and stamp < cutoff:
                continue
            files_seen.append(str(path.relative_to(ROOT)))
            for item in payload.get("candidates", []):
                if not isinstance(item, dict):
                    continue
                url = str(item.get("url", "")).strip()
                if not url:
                    continue
                key = candidate_key(item)
                record = dict(item)
                record["id"] = key
                record["intake_file"] = str(path.relative_to(ROOT))
                record["intake_discovered_utc"] = stamp.isoformat() if stamp else ""
                prior = dedup.get(key)
                if prior is None:
                    dedup[key] = record
                    continue
                old_stamp = parse_stamp(str(prior.get("intake_discovered_utc", "")))
                if stamp and (old_stamp is None or stamp >= old_stamp):
                    dedup[key] = record
    return dedup, files_seen


def source_status(url: str, timeout: float) -> dict:
    result = {"status": "not_checked", "result": ""}
    try:
        req = urllib.request.Request(
            url,
            headers={"User-Agent": "GlassesResearch-editorial-triage/1.0"},
        )
        with urllib.request.urlopen(req, timeout=timeout) as response:
            result["result"] = str(response.status)
            result["status"] = "reachable" if 200 <= response.status < 400 else "review"
    except urllib.error.HTTPError as exc:
        result["status"] = "review"
        result["result"] = str(exc.code)
    except Exception as exc:
        result["status"] = "unreachable"
        result["result"] = type(exc).__name__
    return result


def automated_state(item: dict, source: dict) -> str:
    relationship = str(item.get("relationship", ""))
    types = set(item.get("content_types", []) or [])
    if relationship == "irrelevant":
        return "rejected_noise"
    if relationship == "speculative" or "rumor" in types:
        return "watching"
    if relationship == "adjacent":
        return "adjacent_radar"
    if relationship in {"direct", "enabling"}:
        if source.get("status") in {"review", "unreachable"}:
            return "source_review"
        return "needs_editorial_verification"
    return "source_review"


def preserve_editorial_fields(record: dict, prior: dict | None) -> None:
    if not prior:
        record.setdefault("editorial_disposition", "pending")
        record.setdefault("editorial_notes", "")
        record.setdefault("publication_authorized", False)
        return
    for field in (
        "first_seen_utc",
        "editorial_disposition",
        "editorial_notes",
        "publication_authorized",
        "resolved_utc",
        "canonical_destinations",
    ):
        if field in prior:
            record[field] = prior[field]


def build_queue(args: argparse.Namespace) -> dict:
    now = utc_now()
    cutoff = now - dt.timedelta(days=args.lookback_days)
    incoming, files_seen = collect_candidates(cutoff)
    existing = load_existing_queue()
    records: list[dict] = []

    for key, item in incoming.items():
        prior = existing.get(key)
        record = dict(item)
        preserve_editorial_fields(record, prior)
        record.setdefault("first_seen_utc", record.get("intake_discovered_utc") or now.isoformat())
        record["last_seen_utc"] = record.get("intake_discovered_utc") or now.isoformat()
        source = (
            source_status(str(record.get("url", "")), args.timeout)
            if args.verify_reachability
            else dict((prior or {}).get("source_check", {"status": "not_checked", "result": ""}))
        )
        source["checked_utc"] = now.isoformat() if args.verify_reachability else str(source.get("checked_utc", ""))
        record["source_check"] = source

        disposition = str(record.get("editorial_disposition", "pending"))
        if disposition in FINAL_DISPOSITIONS:
            record["triage_state"] = f"editorial_{disposition}"
        else:
            record["triage_state"] = automated_state(record, source)
            record["editorial_disposition"] = "pending"
            record["publication_authorized"] = False

        record["publication_gate"] = (
            "authorized"
            if bool(record.get("publication_authorized")) and disposition == "published"
            else "blocked_pending_editorial_verification"
            if record["triage_state"] in {"needs_editorial_verification", "source_review"}
            else "not_publication_eligible"
        )
        records.append(record)

    incoming_ids = set(incoming)
    for key, prior in existing.items():
        if key in incoming_ids:
            continue
        if str(prior.get("editorial_disposition", "pending")) in FINAL_DISPOSITIONS:
            records.append(prior)

    records.sort(
        key=lambda item: (
            0 if str(item.get("editorial_disposition", "pending")) == "pending" else 1,
            STATE_ORDER.get(str(item.get("triage_state", "")), 9),
            PRIORITY_ORDER.get(str(item.get("triage_priority", "low")), 9),
            -int(item.get("materiality_score", 0) or 0),
            str(item.get("title", "")).lower(),
        )
    )
    state_counts = Counter(str(item.get("triage_state", "unknown")) for item in records)
    priority_counts = Counter(str(item.get("triage_priority", "unknown")) for item in records)
    return {
        "schema": 1,
        "generated_utc": now.isoformat(),
        "lookback_days": args.lookback_days,
        "intake_files_inspected": len(files_seen),
        "candidate_count": len(records),
        "state_counts": dict(sorted(state_counts.items())),
        "priority_counts": dict(sorted(priority_counts.items())),
        "publication_rule": "Automated triage never authorizes publication; factual publication requires explicit editorial verification.",
        "candidates": records,
    }


def esc(value: object) -> str:
    return str(value).replace("|", "\\|").replace("\n", " ").strip()


def render_markdown(queue: dict) -> str:
    lines = [
        "# Automated editorial triage — latest",
        "",
        f"Generated: `{queue['generated_utc']}`",
        "",
        f"- Intake files inspected: **{queue['intake_files_inspected']}**",
        f"- Candidates retained in this review window/history: **{queue['candidate_count']}**",
        "- **Publication authority: none.** This file is triage state, not factual verification or publication approval.",
        "",
        "## Queue state",
        "",
    ]
    for state, count in queue.get("state_counts", {}).items():
        lines.append(f"- `{state}`: {count}")
    lines += [
        "",
        "## Action queue",
        "",
        "| Priority | State | Relationship | Candidate | Source check | Routes |",
        "|---|---|---|---|---|---|",
    ]
    pending = [
        item
        for item in queue.get("candidates", [])
        if str(item.get("editorial_disposition", "pending")) == "pending"
    ]
    for item in pending[:250]:
        source = item.get("source_check", {}) or {}
        source_text = source.get("status", "not_checked")
        if source.get("result"):
            source_text += f" ({source['result']})"
        lines.append(
            "| {priority} | {state} | {relationship} | [{title}]({url}) | {source} | {routes} |".format(
                priority=esc(item.get("triage_priority", "low")),
                state=esc(item.get("triage_state", "")),
                relationship=esc(item.get("relationship", "")),
                title=esc(item.get("title", ""))[:140],
                url=str(item.get("url", "")),
                source=esc(source_text),
                routes=esc(", ".join(item.get("routing_targets", []) or [])),
            )
        )
    lines += [
        "",
        "## Meaning of states",
        "",
        "- `needs_editorial_verification` — direct/enabling glasses material with a usable source; verify the underlying claim and canonical destinations.",
        "- `source_review` — potentially relevant, but the source could not be cleanly validated automatically.",
        "- `watching` — rumor/speculation; retain without public promotion.",
        "- `adjacent_radar` — neighboring wearable/HCI material without a concrete glasses publication gate.",
        "- `rejected_noise` — irrelevant material that should not advance.",
        "",
        "The next boundary is explicit editorial verification. Only an explicitly published/authorized record may feed canonical site publication and Verified Research Alerts.",
        "",
    ]
    return "\n".join(lines)


def write_outputs(queue: dict) -> None:
    REVIEWS_DIR.mkdir(parents=True, exist_ok=True)
    QUEUE_PATH.write_text(json.dumps(queue, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    markdown = render_markdown(queue)
    LATEST_PATH.write_text(markdown, encoding="utf-8")
    day = dt.datetime.fromisoformat(queue["generated_utc"]).astimezone(ZoneInfo("America/New_York")).date().isoformat()
    (REVIEWS_DIR / f"{day}-auto-triage.md").write_text(markdown, encoding="utf-8")


def main() -> int:
    args = parse_args()
    if args.lookback_days < 1:
        raise SystemExit("--lookback-days must be >= 1")
    queue = build_queue(args)
    write_outputs(queue)
    print(json.dumps({"candidate_count": queue["candidate_count"], "state_counts": queue["state_counts"]}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
