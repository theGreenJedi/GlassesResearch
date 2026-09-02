#!/usr/bin/env python3
"""MkDocs post-build hook for GlassesResearch sitemap completeness."""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

from mkdocs.plugins import event_priority

HOOK_DIR = Path(__file__).resolve().parent
if str(HOOK_DIR) not in sys.path:
    sys.path.insert(0, str(HOOK_DIR))

from reconcile_sitemap import reconcile


@event_priority(-100)
def on_post_build(*, config: Any) -> None:
    """Reconcile only after other hooks have finished generating public pages."""
    site_dir = Path(config.site_dir)
    origin = config.site_url or "https://glassesresearch.org/"
    expected, added, removed = reconcile(site_dir, origin)
    print(
        f"Sitemap post-build reconciliation: {expected} rendered pages, "
        f"{added} added, {removed} stale/duplicate entries removed."
    )
