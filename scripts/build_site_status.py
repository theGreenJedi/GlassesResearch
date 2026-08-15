#!/usr/bin/env python3
"""Build generated homepage research-status metrics."""
from __future__ import annotations

import argparse
import json
import os
from datetime import UTC, datetime
from pathlib import Path


def load(path: str) -> dict:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def generated_at() -> str:
    epoch = os.environ.get("SOURCE_DATE_EPOCH")
    moment = datetime.fromtimestamp(int(epoch), UTC) if epoch else datetime.now(UTC)
    return moment.replace(microsecond=0).isoformat().replace("+00:00", "Z")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--devices", required=True)
    parser.add_argument("--report-cards", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    devices = load(args.devices)
    report_cards = load(args.report_cards)
    model_count = devices.get("record_count")
    if not isinstance(model_count, int):
        model_count = len(devices.get("records", []))

    scored = 0
    for record in report_cards.get("records", []):
        scores = record.get("scores", {})
        if any(isinstance(value, (int, float)) for value in scores.values()):
            scored += 1

    payload = {
        "schema_version": 1,
        "canonical_model_count": model_count,
        "scored_report_card_count": scored,
        "generated_at": generated_at(),
    }
    target = Path(args.output)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(f"Built site status for {model_count} canonical models and {scored} scored Report Cards")


if __name__ == "__main__":
    main()
