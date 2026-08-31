#!/usr/bin/env python3
"""MkDocs post-build hook for GlassesResearch sitemap completeness."""
from __future__ import annotations

from pathlib import Path
from typing import Any

from scripts.reconcile_sitemap import reconcile


def on_post_build(*, config: Any) -> None:
    site_dir = Path(config.site_dir)
    origin = config.site_url or "https://glassesresearch.org/"
    expected, added, removed = reconcile(site_dir, origin)
    print(
        f"Sitemap post-build reconciliation: {expected} rendered pages, "
        f"{added} added, {removed} stale/duplicate entries removed."
    )
