#!/usr/bin/env python3
"""Promote the current editorial feature without changing the verified-news ordering."""
from __future__ import annotations

import argparse
from pathlib import Path

FEATURE = '''<section class="gr-section gr-community-feature" aria-labelledby="gr-community-feature-title" data-home-community-feature>
  <div class="gr-section-heading gr-heading-compact">
    <div>
      <p class="gr-kicker">Community Research · Featured editorial</p>
      <h2 id="gr-community-feature-title">When owners take their glasses back.</h2>
    </div>
    <a class="gr-text-link" href="/docs/news/articles/2026-09-06-when-owners-take-their-glasses-back/">Read the editorial <span aria-hidden="true">→</span></a>
  </div>

  <a class="gr-feature-story" href="/docs/news/articles/2026-09-06-when-owners-take-their-glasses-back/">
    <span class="gr-story-art" aria-hidden="true"></span>
    <span class="gr-story-tag">Community Research · Sep. 6</span>
    <strong>When owners take their glasses back</strong>
    <span>Three community repositories — Panny777's MYVU client, the Rokid AI Glasses research wiki, and CyanBridge — show how reverse engineering, evidence discipline, and reusable software can give owners more practical authority over hardware they already possess.</span>
    <em>Meet the community →</em>
  </a>
</section>'''


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--site-root", type=Path, required=True)
    args = parser.parse_args()
    path = args.site_root / "index.md"
    text = path.read_text(encoding="utf-8")
    if "data-home-community-feature" in text:
        raise SystemExit("Homepage community feature already present")
    marker = '<section class="gr-section" aria-labelledby="gr-now-title" data-home-verified-stream>'
    if marker not in text:
        raise SystemExit("Homepage verified stream marker missing")
    text = text.replace(marker, FEATURE + "\n\n" + marker, 1)
    path.write_text(text, encoding="utf-8")
    print("Featured Community Research editorial on homepage; verified-news chronology unchanged")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
