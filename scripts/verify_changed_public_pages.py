#!/usr/bin/env python3
"""Prove that changed public Markdown pages are the exact HTML served in production.

Run after the Pages deployment. The repository is built at the deployed SHA, then
changed public Markdown files are mapped to their MkDocs output. Each production
URL is fetched with cache-busting headers and its body must byte-match the built
artifact. A deployment is not considered proven merely because its SHA is live.
"""
from __future__ import annotations

import argparse
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

PUBLIC_ROOTS = {
    "artifacts", "buyers", "changes", "comparisons", "data", "dataset", "docs",
    "evidence", "glossary", "guides", "hacking", "images", "lineages", "models",
    "research", "resources", "timeline",
}
EXCLUDED = {
    "comparisons/README.md", "data/family-trees-bounded.json", "data/family-trees-researched.json",
    "data/family-tree-audit-overrides.json", "data/verified-changes.json", "docs/AI610-Notes.md",
    "docs/CONTENT_GAPS_WAVE_TWO.md", "docs/HOMEPAGE_DESIGN_NOTES.md", "docs/KISS_WORKING_NOTES.md",
    "docs/LEGACY_STRUCTURE_AUDIT.md", "docs/RESEARCH_AGENDA.md", "docs/research/issue-381-validation.md",
    "docs/ROADMAP_V1.md", "docs/SEO_DISCOVERABILITY.md", "docs/WEBSITE.md", "docs/START_HERE.md",
    "docs/news/WORKFLOW.md", "docs/report-cards/PROFILE_AUDIT_03_06.md", "docs/report-cards/SOURCES_01.md",
    "resources/CHANGE_SCOPE.md", "resources/PR_NOTES.md", "resources/VALIDATION.md", "timeline/README.md",
}


def changed_files(base: str, head: str) -> list[str]:
    out = subprocess.check_output(["git", "diff", "--name-only", "--diff-filter=ACMR", base, head], text=True)
    return [line.strip() for line in out.splitlines() if line.strip()]


def public_output(source: str, site: Path) -> tuple[Path, str] | None:
    if source == "README.md":
        return site / "index.html", "/"
    p = Path(source)
    if p.suffix.lower() != ".md" or source in EXCLUDED or not p.parts or p.parts[0] not in PUBLIC_ROOTS:
        return None
    rel = p.with_suffix("")
    # MkDocs directory URLs: foo/index.md -> foo/, foo/bar.md -> foo/bar/
    if rel.name == "index":
        rel = rel.parent
    output = site / rel / "index.html"
    url = "/" + rel.as_posix().strip("/") + "/"
    return output, url


def fetch(url: str, sha: str, attempt: int) -> bytes:
    sep = "&" if "?" in url else "?"
    req = urllib.request.Request(
        f"{url}{sep}deploy-proof={sha}-{attempt}",
        headers={"Cache-Control": "no-cache", "Pragma": "no-cache", "User-Agent": "GlassesResearch-deployment-proof/1"},
    )
    with urllib.request.urlopen(req, timeout=25) as response:
        if response.status != 200:
            raise RuntimeError(f"HTTP {response.status}")
        return response.read()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", required=True)
    ap.add_argument("--head", required=True)
    ap.add_argument("--site-root", default="site")
    ap.add_argument("--origin", default="https://glassesresearch.org")
    ap.add_argument("--attempts", type=int, default=12)
    ap.add_argument("--delay", type=int, default=15)
    args = ap.parse_args()

    site = Path(args.site_root)
    targets: list[tuple[str, Path, str]] = []
    for source in changed_files(args.base, args.head):
        mapped = public_output(source, site)
        if mapped:
            output, url = mapped
            if not output.is_file():
                print(f"ERROR: changed public source {source} has no built output {output}", file=sys.stderr)
                return 1
            targets.append((source, output, url))

    if not targets:
        print("No directly changed public Markdown pages require production body proof.")
        return 0

    print("Production content proof targets:")
    for source, _, url in targets:
        print(f"  {source} -> {url}")

    pending = targets[:]
    for attempt in range(1, args.attempts + 1):
        still_pending = []
        for source, output, path in pending:
            expected = output.read_bytes()
            try:
                actual = fetch(args.origin.rstrip("/") + path, args.head, attempt)
            except (urllib.error.URLError, TimeoutError, RuntimeError) as exc:
                print(f"Attempt {attempt}: {path} unavailable: {exc}")
                still_pending.append((source, output, path))
                continue
            if actual != expected:
                print(f"Attempt {attempt}: {path} does not byte-match deployed artifact yet.")
                still_pending.append((source, output, path))
            else:
                print(f"PROVED: {source} is exactly served at {path}")
        if not still_pending:
            print(f"Production content verified for {len(targets)} changed public page(s).")
            return 0
        pending = still_pending
        if attempt < args.attempts:
            time.sleep(args.delay)

    print("ERROR: production did not serve the exact built content for:", file=sys.stderr)
    for source, _, path in pending:
        print(f"  {source} -> {path}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
