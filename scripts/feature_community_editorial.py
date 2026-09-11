#!/usr/bin/env python3
"""Promote the current editorial feature without changing verified-news ordering."""
from __future__ import annotations

import argparse
from pathlib import Path

FEATURE = '''<section class="gr-section gr-community-feature" aria-labelledby="gr-community-feature-title" data-home-community-feature>
  <a class="gr-community-feature-card" href="/docs/news/articles/2026-09-06-when-owners-take-their-glasses-back/">
    <div class="gr-community-feature-copy">
      <p class="gr-kicker">Community Research · Featured editorial</p>
      <h2 id="gr-community-feature-title">When owners take their glasses back.</h2>
      <p>Three community repositories show how careful interoperability research, evidence discipline, and reusable software can give owners more practical authority over hardware they already possess.</p>
      <p class="gr-community-feature-meta">Published Sep. 6, 2026 · attributed repository evidence · community findings remain distinct from GlassesResearch laboratory verification</p>
    </div>
    <div class="gr-evidence-route" aria-label="Evidence path from community research to owner agency">
      <div class="gr-evidence-node"><strong>Panny777 / MYVU</strong><span>interoperability research</span></div>
      <div class="gr-evidence-node"><strong>aimindseye / Rokid</strong><span>evidence mapping</span></div>
      <div class="gr-evidence-node"><strong>CyanBridge</strong><span>cross-device integration</span></div>
      <div class="gr-evidence-outcome">Community evidence → practical owner agency</div>
    </div>
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

    newsroom_marker = '<div class="gr-news-pair" aria-label="GlassesResearch newsroom">'
    legacy_verified_marker = '<section class="gr-section" aria-labelledby="gr-now-title" data-home-verified-stream>'
    if newsroom_marker in text:
        marker = newsroom_marker
    elif legacy_verified_marker in text:
        marker = legacy_verified_marker
    else:
        raise SystemExit("Homepage newsroom/verified stream marker missing")

    text = text.replace(marker, FEATURE + "\n\n" + marker, 1)
    path.write_text(text, encoding="utf-8")
    print("Featured Community Research editorial on homepage once; newsroom chronology unchanged")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
