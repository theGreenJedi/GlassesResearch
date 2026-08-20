#!/usr/bin/env python3
"""Publish and prove Verified Research Alerts derived from canonical GRE events.

The GRE ledger is the editorial authorization boundary between verified public
research and subscriber mail. Discovery candidates and Watching items are
outside this path. Existing gr-YYYY-MM-DD-* publication IDs remain the delivery
idempotency key so no subscriber history is reset by this migration.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

from verified_changes import (
    DEFAULT_CHANGES,
    ValidationError,
    publication_manifest,
    validate as validate_changes,
)

DEFAULT_MANIFEST = DEFAULT_CHANGES
ALERTS_BASE = "https://alerts.glassesresearch.org"


def validate(path: Path = DEFAULT_MANIFEST) -> dict:
    """Validate the GRE ledger and return the backward-compatible publication view."""
    return publication_manifest(validate_changes(path))


def request_json(
    url: str,
    *,
    method: str = "GET",
    token: str | None = None,
    payload: dict | None = None,
    timeout: int = 25,
) -> dict:
    headers = {"User-Agent": "GlassesResearch-verified-publication-bridge/3.0"}
    data = None
    if token:
        headers["Authorization"] = f"Bearer {token}"
    if payload is not None:
        headers["Content-Type"] = "application/json"
        data = json.dumps(payload, separators=(",", ":")).encode("utf-8")
    request = urllib.request.Request(url, data=data, headers=headers, method=method)
    with urllib.request.urlopen(request, timeout=timeout) as response:
        body = response.read().decode("utf-8")
        return json.loads(body or "{}")


def publication_payload(item: dict) -> dict:
    return {
        key: item[key]
        for key in (
            "id",
            "event_id",
            "title",
            "canonical_url",
            "summary",
            "models",
            "brands_lineages",
            "topics",
            "published_at",
        )
    }


def wait_for_canary(item: dict, endpoint: str, token: str, *, timeout_seconds: int = 360) -> dict:
    publication_id = item["id"]
    base = endpoint.rsplit("/", 1)[0]
    proof_url = f"{base}/delivery-proof?{urllib.parse.urlencode({'publication_id': publication_id})}"
    deadline = time.monotonic() + timeout_seconds
    next_replay = 0.0
    last_proof: dict = {}
    last_error: Exception | None = None

    while time.monotonic() < deadline:
        now_mono = time.monotonic()
        if now_mono >= next_replay:
            try:
                replay = request_json(endpoint, method="POST", token=token, payload=publication_payload(item))
                if replay.get("ok") is not True:
                    raise RuntimeError(f"publisher replay returned non-success response: {replay}")
            except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, RuntimeError, json.JSONDecodeError) as exc:
                last_error = exc
            next_replay = now_mono + 45

        try:
            proof = request_json(proof_url, token=token)
            last_proof = proof
            if proof.get("ok") is True and proof.get("provider_accepted") is True and proof.get("received") is True:
                print(
                    "End-to-end canary delivery proven: "
                    f"{publication_id} event={item['event_id']} "
                    f"provider_message_id={proof.get('provider_message_id') or 'unavailable'} "
                    f"received_at={proof.get('received_at')}"
                )
                return proof
            if proof.get("last_error"):
                print(f"Canary delivery pending for {publication_id}: {proof['last_error']}", file=sys.stderr)
        except urllib.error.HTTPError as exc:
            last_error = exc
        except (urllib.error.URLError, TimeoutError, RuntimeError, json.JSONDecodeError) as exc:
            last_error = exc
        time.sleep(10)

    safe = {
        "dispatch_attempted": last_proof.get("dispatch_attempted"),
        "provider_accepted": last_proof.get("provider_accepted"),
        "received": last_proof.get("received"),
        "received_at": last_proof.get("received_at"),
        "last_error": last_proof.get("last_error"),
    }
    detail = f"; last request error: {last_error}" if last_error else ""
    raise RuntimeError(f"End-to-end canary delivery was not proven for {publication_id}: {safe}{detail}")


def publish(manifest: dict, endpoint: str, token: str) -> None:
    enabled = [item for item in manifest["publications"] if item["dispatch"]]
    if not enabled:
        print("No dispatch-enabled verified publications.")
        return

    for item in enabled:
        payload = publication_payload(item)
        last_error: Exception | None = None
        for attempt in range(1, 6):
            try:
                result = request_json(endpoint, method="POST", token=token, payload=payload)
                if result.get("ok") is not True:
                    raise RuntimeError(f"publisher returned non-success response: {result}")
                print(f"Published alert event accepted: {item['event_id']} via {item['id']}")
                break
            except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, RuntimeError, json.JSONDecodeError) as exc:
                last_error = exc
                if attempt == 5:
                    raise RuntimeError(f"Failed publishing {item['id']} after 5 attempts: {exc}") from exc
                time.sleep(attempt * 3)
        else:
            raise RuntimeError(f"Failed publishing {item['id']}: {last_error}")
        wait_for_canary(item, endpoint, token)


def wait_for_canary_capable_worker(*, timeout_seconds: int = 300) -> None:
    deadline = time.monotonic() + timeout_seconds
    last: object = None
    while time.monotonic() < deadline:
        try:
            health = request_json(f"{ALERTS_BASE}/health")
            last = health
            if health.get("ok") is True and health.get("service") == "verified-research-alerts" and health.get("canary") is True:
                print("Verified Research Alerts Worker health check passed with canary support.")
                return
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, json.JSONDecodeError) as exc:
            last = exc
        time.sleep(10)
    raise ValidationError(f"Canary-capable Verified Research Alerts Worker did not become healthy: {last}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST, help="Canonical GRE verified-change ledger")
    parser.add_argument("--publish", action="store_true", help="POST dispatch-enabled entries and prove canary receipt")
    parser.add_argument("--endpoint", default=f"{ALERTS_BASE}/published")
    args = parser.parse_args()

    try:
        manifest = validate(args.manifest)
        if args.publish:
            token = os.environ.get("PUBLISH_TOKEN", "").strip()
            if not token:
                raise ValidationError("PUBLISH_TOKEN is required for --publish")
            wait_for_canary_capable_worker()
            publish(manifest, args.endpoint, token)
    except (ValidationError, RuntimeError, urllib.error.URLError, urllib.error.HTTPError) as exc:
        print(str(exc), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
