#!/usr/bin/env python3
"""Write a compact machine-readable receipt for an Across the Wire workflow run."""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path("data/wire-run-receipt.json"))
    parser.add_argument("--phase", choices=("started", "completed"), required=True)
    parser.add_argument("--changed", choices=("true", "false", "unknown"), default="unknown")
    parser.add_argument("--status", default="running")
    args = parser.parse_args()

    now = dt.datetime.now(dt.timezone.utc).isoformat().replace("+00:00", "Z")
    receipt: dict = {}
    if args.output.exists():
        try:
            receipt = json.loads(args.output.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            receipt = {}

    if args.phase == "started":
        receipt = {
            "schema_version": 1,
            "run_id": os.environ.get("GITHUB_RUN_ID", "local"),
            "run_attempt": os.environ.get("GITHUB_RUN_ATTEMPT", "1"),
            "event": os.environ.get("GITHUB_EVENT_NAME", "local"),
            "started_at": now,
            "completed_at": None,
            "status": "running",
            "visible_wire_changed": None,
        }
    else:
        receipt["completed_at"] = now
        receipt["status"] = args.status
        receipt["visible_wire_changed"] = None if args.changed == "unknown" else args.changed == "true"

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    print(f"Wire run receipt: {args.phase} status={receipt.get('status')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
