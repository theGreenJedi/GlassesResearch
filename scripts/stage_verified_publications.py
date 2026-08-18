#!/usr/bin/env python3
"""Stage dispatch-enabled verified publications at the alerts Worker.

This is intentionally separate from synthetic-canary proof. Real subscriber
mail must not be held behind canary availability; the Worker and deliveries
remain idempotent by publication ID.
"""

from __future__ import annotations

import os
import sys
import time
import urllib.error

from verified_publications import (
    ALERTS_BASE,
    DEFAULT_MANIFEST,
    ValidationError,
    json,
    publication_payload,
    request_json,
    validate,
)


def stage() -> int:
    try:
        manifest = validate(DEFAULT_MANIFEST)
        token = os.environ.get("PUBLISH_TOKEN", "").strip()
        if not token:
            raise ValidationError("PUBLISH_TOKEN is required to stage verified publications")

        endpoint = f"{ALERTS_BASE}/published"
        enabled = [item for item in manifest["publications"] if item["dispatch"]]
        if not enabled:
            print("No dispatch-enabled verified publications.")
            return 0

        for item in enabled:
            payload = publication_payload(item)
            last_error: Exception | None = None
            for attempt in range(1, 6):
                try:
                    result = request_json(endpoint, method="POST", token=token, payload=payload)
                    if result.get("ok") is not True:
                        raise RuntimeError(f"publisher returned non-success response: {result}")
                    print(f"Staged verified alert event: {item['id']}")
                    break
                except (
                    urllib.error.URLError,
                    urllib.error.HTTPError,
                    TimeoutError,
                    RuntimeError,
                    json.JSONDecodeError,
                ) as exc:
                    last_error = exc
                    if attempt == 5:
                        raise RuntimeError(
                            f"Failed staging {item['id']} after 5 attempts: {exc}"
                        ) from exc
                    time.sleep(attempt * 3)
            else:
                raise RuntimeError(f"Failed staging {item['id']}: {last_error}")
    except (ValidationError, RuntimeError, urllib.error.URLError, urllib.error.HTTPError) as exc:
        print(str(exc), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(stage())
