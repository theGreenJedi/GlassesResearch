#!/usr/bin/env python3
"""Stage dispatch-enabled verified publications at the alerts Worker.

Real subscriber mail must not be held behind synthetic-canary availability, but
it also must not outrun the public site deployment. Each alert is staged only
after its GlassesResearch article URL is reachable. Worker ingestion and
subscriber deliveries remain idempotent by publication ID.
"""

from __future__ import annotations

import os
import sys
import time
import urllib.error
import urllib.request

from verified_publications import (
    ALERTS_BASE,
    DEFAULT_MANIFEST,
    ValidationError,
    json,
    publication_payload,
    request_json,
    validate,
)


def wait_until_article_live(item: dict, *, timeout_seconds: int = 300) -> None:
    url = str(item["canonical_url"])
    deadline = time.monotonic() + timeout_seconds
    last_error: Exception | None = None
    while time.monotonic() < deadline:
        try:
            request = urllib.request.Request(
                url,
                headers={"User-Agent": "GlassesResearch-alert-publication-gate/1.0"},
            )
            with urllib.request.urlopen(request, timeout=20) as response:
                if 200 <= response.status < 300:
                    print(f"Public article reachable: {item['id']} {url}")
                    return
                last_error = RuntimeError(f"unexpected HTTP status {response.status}")
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as exc:
            last_error = exc
        time.sleep(10)
    raise RuntimeError(
        f"Refusing to stage {item['id']} before its public article is reachable: {url}; "
        f"last error: {last_error}"
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
            wait_until_article_live(item)
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
