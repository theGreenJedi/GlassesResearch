#!/usr/bin/env python3
"""Prove changed and representative public pages are served from the deployed build.

The production edge may legitimately transform HTML bytes, so raw byte identity is
not a reliable deployment invariant. Each built page carries a deterministic digest
of its source URI plus the Markdown passed into the SEO hook. Production must expose
the exact expected digest and canonical URL for every changed public Markdown page
plus permanent regression canaries.
"""
from __future__ import annotations

import argparse
import subprocess
import sys
import time
import urllib.error
import urllib.request
from html.parser import HTMLParser
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

# These three surfaces exposed the first non-vacuous failure of the original
# byte-identity proof on 2026-09-23. Keep them as cross-surface regression
# canaries: Research & News, model research, and durable research plumbing.
REGRESSION_CANARIES = (
    "docs/news/articles/2026-09-23-state-of-the-state-smart-glasses-are-no-longer-becoming-one-thing.md",
    "models/PROFILES_2026_09_23_NUANCE_AUDIO.md",
    "research/HARDWARE_LINEAGE_ODM.md",
)


class ProofSignals(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.content_digest = ""
        self.canonical = ""

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {key: value or "" for key, value in attrs}
        if tag == "meta" and values.get("name") == "gr-content-sha256":
            self.content_digest = values.get("content", "").strip()
        elif tag == "link" and "canonical" in values.get("rel", "").split():
            self.canonical = values.get("href", "").strip()


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


def signals(body: bytes) -> ProofSignals:
    parser = ProofSignals()
    parser.feed(body.decode("utf-8", errors="replace"))
    return parser


def fetch(url: str, sha: str, attempt: int) -> bytes:
    sep = "&" if "?" in url else "?"
    req = urllib.request.Request(
        f"{url}{sep}deploy-proof={sha}-{attempt}",
        headers={
            "Cache-Control": "no-cache",
            "Pragma": "no-cache",
            "User-Agent": "GlassesResearch-deployment-proof/2",
        },
    )
    with urllib.request.urlopen(req, timeout=25) as response:
        if response.status != 200:
            raise RuntimeError(f"HTTP {response.status}")
        return response.read()


def short(value: str) -> str:
    return value[:12] if value else "<missing>"


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
    candidates = list(dict.fromkeys(changed_files(args.base, args.head) + list(REGRESSION_CANARIES)))
    targets: list[tuple[str, Path, str, str, str]] = []

    for source in candidates:
        mapped = public_output(source, site)
        if not mapped:
            continue
        output, url = mapped
        if not output.is_file():
            print(f"ERROR: public proof source {source} has no built output {output}", file=sys.stderr)
            return 1
        expected = signals(output.read_bytes())
        if not expected.content_digest:
            print(f"ERROR: built page {output} is missing gr-content-sha256", file=sys.stderr)
            return 1
        if not expected.canonical:
            print(f"ERROR: built page {output} is missing canonical URL", file=sys.stderr)
            return 1
        targets.append((source, output, url, expected.content_digest, expected.canonical))

    if not targets:
        print("No public pages are available for production content proof.")
        return 1

    print("Production content proof targets:")
    for source, _, url, digest, _ in targets:
        kind = "changed" if source in changed_files(args.base, args.head) else "canary"
        print(f"  [{kind}] {source} -> {url} digest={short(digest)}")

    pending = targets[:]
    for attempt in range(1, args.attempts + 1):
        still_pending = []
        for source, output, path, expected_digest, expected_canonical in pending:
            try:
                actual = signals(fetch(args.origin.rstrip("/") + path, args.head, attempt))
            except (urllib.error.URLError, TimeoutError, RuntimeError) as exc:
                print(f"Attempt {attempt}: {path} unavailable: {exc}")
                still_pending.append((source, output, path, expected_digest, expected_canonical))
                continue

            if actual.content_digest != expected_digest:
                print(
                    f"Attempt {attempt}: {path} content digest mismatch "
                    f"(expected {short(expected_digest)}, got {short(actual.content_digest)})."
                )
                still_pending.append((source, output, path, expected_digest, expected_canonical))
                continue
            if actual.canonical != expected_canonical:
                print(
                    f"Attempt {attempt}: {path} canonical mismatch "
                    f"(expected {expected_canonical!r}, got {actual.canonical!r})."
                )
                still_pending.append((source, output, path, expected_digest, expected_canonical))
                continue

            print(f"PROVED: {source} is served at {path} with build digest {short(expected_digest)}")

        if not still_pending:
            print(f"Production content verified for {len(targets)} changed/canary public page(s).")
            return 0
        pending = still_pending
        if attempt < args.attempts:
            time.sleep(args.delay)

    print("ERROR: production did not prove the expected build content for:", file=sys.stderr)
    for source, _, path, expected_digest, _ in pending:
        print(f"  {source} -> {path} (expected digest {short(expected_digest)})", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
