#!/usr/bin/env python3
"""Apply explicit editorial decisions to the generated durable triage queue."""
from __future__ import annotations

import datetime as dt
import json
from collections import Counter

from triage_news_reviews import LATEST_PATH, QUEUE_PATH, REVIEWS_DIR, markdown, review_key

DECISIONS_PATH = REVIEWS_DIR / "editorial-decisions.json"
FINAL_DISPOSITIONS = {"published", "watch", "archived", "superseded", "rejected"}


def decision_map(payload: dict) -> dict[str, dict]:
    mapped: dict[str, dict] = {}
    for decision in payload.get("decisions", []):
        if not isinstance(decision, dict):
            continue
        source_url = str(decision.get("source_url", "")).strip()
        disposition = str(decision.get("disposition", "")).strip()
        if not source_url or disposition not in FINAL_DISPOSITIONS:
            continue
        mapped[review_key({"url": source_url})] = decision
    return mapped


def apply_decision(item: dict, decision: dict) -> dict:
    record = dict(item)
    disposition = str(decision["disposition"])
    authorized = bool(decision.get("publication_authorized", False))
    if disposition != "published":
        authorized = False
    record["editorial_disposition"] = disposition
    record["editorial_notes"] = str(decision.get("editorial_notes", ""))
    record["publication_authorized"] = authorized
    record["resolved_utc"] = str(decision.get("decided_utc", ""))
    record["canonical_destinations"] = list(decision.get("canonical_destinations", []) or [])
    if decision.get("verified_publication_id"):
        record["verified_publication_id"] = str(decision["verified_publication_id"])
    record["triage_state"] = f"editorial_{disposition}"
    record["publication_gate"] = "authorized" if authorized else "not_publication_eligible"
    return record


def apply_payload(queue: dict, decisions_payload: dict) -> dict:
    decisions = decision_map(decisions_payload)
    records = []
    for item in queue.get("candidates", []):
        decision = decisions.get(review_key(item))
        records.append(apply_decision(item, decision) if decision else item)
    queue = dict(queue)
    queue["candidates"] = records
    queue["state_counts"] = dict(sorted(Counter(str(x.get("triage_state", "unknown")) for x in records).items()))
    queue["editorial_decisions_applied"] = sum(1 for item in records if str(item.get("editorial_disposition", "pending")) != "pending")
    return queue


def write_outputs(queue: dict) -> None:
    QUEUE_PATH.write_text(json.dumps(queue, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    text = markdown(queue)
    LATEST_PATH.write_text(text, encoding="utf-8")
    generated = dt.datetime.fromisoformat(str(queue["generated_utc"]).replace("Z", "+00:00"))
    day = generated.astimezone().date().isoformat()
    # The triage generator already created the dated snapshot. Rewrite every matching
    # dated snapshot for this generated day so the human-readable state stays aligned.
    for path in REVIEWS_DIR.glob(f"{day}-auto-triage.md"):
        path.write_text(text, encoding="utf-8")


def main() -> int:
    if not QUEUE_PATH.exists() or not DECISIONS_PATH.exists():
        print("No queue or editorial decision ledger to apply.")
        return 0
    queue = json.loads(QUEUE_PATH.read_text(encoding="utf-8"))
    decisions_payload = json.loads(DECISIONS_PATH.read_text(encoding="utf-8"))
    updated = apply_payload(queue, decisions_payload)
    write_outputs(updated)
    print(json.dumps({"editorial_decisions_applied": updated.get("editorial_decisions_applied", 0), "state_counts": updated.get("state_counts", {})}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
