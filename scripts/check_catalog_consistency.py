#!/usr/bin/env python3
"""Fail CI when canonical model/lineage surfaces drift out of sync.

Reconciliation packets may approve a GLS admission before the mechanical catalog
synchronizer inserts the row into THE_LIST. Research/profile links for those
approved-pending IDs are valid during the pull request that approves them.
"""
from pathlib import Path
import json
import re
import sys

from catalog_metadata import canonical_model_count, canonical_model_ids

ROOT = Path(__file__).resolve().parents[1]
MODELS = ROOT / "models"
errors = []

the_list = (MODELS / "THE_LIST.md").read_text(encoding="utf-8")
model_readme = (MODELS / "README.md").read_text(encoding="utf-8")
root_readme = (ROOT / "README.md").read_text(encoding="utf-8")
lineage_index = (ROOT / "lineages/README.md").read_text(encoding="utf-8")
corrections_path = MODELS / "CATALOG_CORRECTIONS.md"
corrections = corrections_path.read_text(encoding="utf-8") if corrections_path.exists() else ""
candidates_path = ROOT / "data/model-candidates.json"


def approved_pending_ids() -> set[str]:
    """Collect explicitly approved GLS rows awaiting mechanical synchronization."""
    approved: set[str] = set()
    for path in MODELS.glob("THE_LIST_RECONCILIATION_*.md"):
        text = path.read_text(encoding="utf-8")
        match = re.search(
            r"## Admit to canonical purchaser-history ledger\n(.*?)(?=\n## |\Z)",
            text,
            flags=re.S,
        )
        if not match:
            continue
        approved.update(re.findall(r"^\| (GLS-\d{4}) \|", match.group(1), flags=re.M))
    return approved


unique_ids = set(canonical_model_ids(ROOT, the_list))
pending_ids = approved_pending_ids() - unique_ids
canonical_count = canonical_model_count(ROOT, the_list)
count_match = re.search(r"\*\*Count:\*\* (\d+)", the_list)
if not count_match:
    errors.append("The List has no generated Count field")
else:
    declared = int(count_match.group(1))
    if declared != canonical_count:
        errors.append(f"The List displays {declared} models but canonical rows total {canonical_count}")

# Public prose may display the current total, but it is a generated derivative.
# Any current-count phrase must agree with the one authoritative ledger-derived count.
for label, text in (("models/README.md", model_readme), ("README.md", root_readme)):
    patterns = (
        r"\b(\d+) purchasable smart-glasses models",
        r"\b(\d+) models and generations",
        r"every one of the (\d+) active canonical smart-glasses records",
        r"active canonical count is now \*\*(\d+)\*\*",
        r"returns the active canonical count to \*\*(\d+)\*\*",
    )
    for pattern in patterns:
        for raw in re.findall(pattern, text):
            count = int(raw)
            if count != canonical_count:
                errors.append(f"{label} says {count} models; canonical ledger has {canonical_count}")

if candidates_path.exists():
    payload = json.loads(candidates_path.read_text(encoding="utf-8"))
    cataloged_ids = []
    for candidate in payload.get("candidates", []):
        if candidate.get("status") != "cataloged":
            continue
        canonical_id = candidate.get("canonical_id")
        candidate_id = candidate.get("candidate_id", "<unknown-candidate>")
        if not canonical_id:
            errors.append(f"Cataloged candidate {candidate_id} has no canonical_id")
            continue
        cataloged_ids.append(canonical_id)
        if canonical_id not in unique_ids:
            errors.append(
                f"Cataloged candidate {candidate_id} points to {canonical_id}, but that GLS row is absent from The List"
            )
    duplicated_catalog_ids = sorted({gid for gid in cataloged_ids if cataloged_ids.count(gid) > 1})
    if duplicated_catalog_ids:
        errors.append(
            "Multiple cataloged candidates claim the same canonical GLS ID: " + ", ".join(duplicated_catalog_ids)
        )

chapter_ids = set(re.findall(r"GLS-\d{4}", model_readme))
retired_ids = set(re.findall(r"\| (GLS-\d{4}) \|[^\n]*\*\*Retired", corrections))
missing_ids = sorted(chapter_ids - unique_ids - pending_ids - retired_ids)
if missing_ids:
    errors.append("Model research references IDs absent from The List or approved-pending admissions: " + ", ".join(missing_ids))

lineage_files = sorted(p for p in (ROOT / "lineages").glob("*.md") if p.name != "README.md")
for path in lineage_files:
    rel = f"lineages/{path.name}"
    if f"({path.name})" not in lineage_index:
        errors.append(f"{rel} exists but is absent from lineage index")

if errors:
    print("Catalog consistency check FAILED:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print(
    f"Catalog consistency check passed: {canonical_count} canonical models; "
    f"{len(pending_ids)} approved pending; {len(lineage_files)} lineage chapters."
)
