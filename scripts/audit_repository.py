#!/usr/bin/env python3
"""Audit GlassesResearch Markdown links and evidence-oriented records.

Uses only the Python standard library. The script checks repository-relative
and site-root Markdown links, reports external links for later archival review,
and flags preservation-ledger rows that do not contain a recognizable PA ID.
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote, urlparse

LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
PA_ID_RE = re.compile(r"\bPA-\d{4}\b")
SKIP_DIRS = {".git", ".venv", ".site-src", "site", "node_modules", "__pycache__"}


@dataclass(frozen=True)
class Finding:
    path: Path
    line: int
    message: str


def markdown_files(root: Path) -> list[Path]:
    return sorted(
        path
        for path in root.rglob("*.md")
        if not any(part in SKIP_DIRS for part in path.parts)
    )


def clean_target(raw: str) -> str:
    target = raw.strip()
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1]
    if " \"" in target:
        target = target.split(" \"", 1)[0]
    # Preserve percent-encoding for external URLs. Decoding an external target
    # here turns valid %20/%7C escapes back into whitespace/reserved characters
    # and can corrupt the newline-delimited URL inventory consumed by lychee.
    return target


def site_root_candidate(root: Path, relative: str) -> Path:
    """Map a clean site URL such as /docs/BLE/ back to repository Markdown."""
    clean = relative.lstrip("/").rstrip("/")
    candidate = root / clean
    if candidate.is_dir():
        return candidate / "README.md"
    if candidate.exists():
        return candidate
    markdown_candidate = root / f"{clean}.md"
    if markdown_candidate.exists():
        return markdown_candidate
    return candidate


def audit_markdown(root: Path) -> tuple[list[Finding], set[str]]:
    findings: list[Finding] = []
    external: set[str] = set()

    for path in markdown_files(root):
        text = path.read_text(encoding="utf-8")
        for line_number, line in enumerate(text.splitlines(), start=1):
            for match in LINK_RE.finditer(line):
                target = clean_target(match.group(1))
                if not target or target.startswith("#"):
                    continue

                parsed = urlparse(target)
                if parsed.scheme in {"http", "https"}:
                    external.add(target)
                    continue
                if parsed.scheme in {"mailto", "tel", "data"}:
                    continue

                # Repository paths need filesystem-safe decoded text, but
                # external URLs above must retain their encoded representation.
                relative = unquote(parsed.path)
                if not relative:
                    continue
                if relative.startswith("/"):
                    candidate = site_root_candidate(root, relative)
                else:
                    candidate = (path.parent / relative).resolve()
                    try:
                        candidate.relative_to(root.resolve())
                    except ValueError:
                        findings.append(Finding(path, line_number, f"link escapes repository: {target}"))
                        continue
                    if candidate.is_dir():
                        candidate = candidate / "README.md"

                if not candidate.exists():
                    findings.append(Finding(path, line_number, f"missing local target: {target}"))

    return findings, external


def audit_preservation_ledger(root: Path) -> list[Finding]:
    ledger = root / "resources" / "PRIMARY_ARTIFACT_PRESERVATION_LEDGER.md"
    if not ledger.exists():
        return [Finding(ledger, 0, "preservation ledger is missing")]

    findings: list[Finding] = []
    for line_number, line in enumerate(ledger.read_text(encoding="utf-8").splitlines(), 1):
        if line.startswith("|") and "PA-" in line and not PA_ID_RE.search(line):
            findings.append(Finding(ledger, line_number, "malformed preservation record ID"))
    return findings


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--external-output", type=Path, help="Write sorted external URLs for archival/link-check workflows.")
    args = parser.parse_args()
    root = args.root.resolve()

    findings, external = audit_markdown(root)
    findings.extend(audit_preservation_ledger(root))

    if args.external_output:
        output = args.external_output
        if not output.is_absolute():
            output = root / output
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text("\n".join(sorted(external)) + "\n", encoding="utf-8")

    print(f"Audited {len(markdown_files(root))} Markdown files.")
    print(f"Recorded {len(external)} unique external links.")
    if findings:
        for finding in findings:
            try:
                shown = finding.path.relative_to(root)
            except ValueError:
                shown = finding.path
            print(f"ERROR {shown}:{finding.line}: {finding.message}")
            if os.getenv("GITHUB_ACTIONS") == "true":
                safe = finding.message.replace("%", "%25").replace("\r", "%0D").replace("\n", "%0A")
                print(f"::error file={shown},line={max(finding.line, 1)}::{safe}")
        return 1

    print("Repository audit passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
