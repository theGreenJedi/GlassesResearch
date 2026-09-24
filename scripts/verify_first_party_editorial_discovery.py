#!/usr/bin/env python3
"""Smoke-test automatic discovery of first-party GlassesResearch editorials."""

from __future__ import annotations

import tempfile
from datetime import datetime, timezone
from pathlib import Path

from build_newsroom_state import load_first_party_editorial


def main() -> int:
    now = datetime.now(timezone.utc)
    published = f"{now:%B} {now.day}, {now.year}"

    with tempfile.TemporaryDirectory() as tmp:
        article_dir = Path(tmp)
        article = article_dir / "plumbing-proof.md"
        article.write_text(
            f'''---
description: "Synthetic newsroom plumbing proof."
---

# Plumbing proof

**Published:** {published}  
**Type:** GlassesResearch editorial / test  
''',
            encoding="utf-8",
        )

        lead = load_first_party_editorial(article_dir)
        if lead is None:
            raise SystemExit("First-party editorial auto-discovery returned no lead")
        expected = {
            "lead_mode": "first_party_editorial",
            "source_label": "GlassesResearch",
            "title": "Plumbing proof",
        }
        for key, value in expected.items():
            if lead.get(key) != value:
                raise SystemExit(f"Unexpected {key}: {lead.get(key)!r}")
        if not str(lead.get("url", "")).endswith("/docs/news/articles/plumbing-proof/"):
            raise SystemExit(f"Unexpected editorial URL: {lead.get('url')!r}")

    print("First-party editorial auto-discovery verified.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
