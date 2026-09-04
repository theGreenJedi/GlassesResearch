#!/usr/bin/env python3
"""Fail CI when canonical model/lineage surfaces drift out of sync."""
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
errors = []

the_list = (ROOT / "models/THE_LIST.md").read_text(encoding="utf-8")
model_readme = (ROOT / "models/README.md").read_text(encoding="utf-8")
root_readme = (ROOT / "README.md").read_text(encoding="utf-8")
lineage_index = (ROOT / "lineages/README.md").read_text(encoding="utf-8")
corrections_path = ROOT / "models/CATALOG_CORRECTIONS.md"
corrections = corrections_path.read_text(encoding="utf-8") if corrections_path.exists() else ""
candidates_path = ROOT / "data/model-candidates.json"

ids = re.findall(r"^\| (GLS-\d{4}) \|", the_list, flags=re.M)
unique_ids = set(ids)
canonical_count = len(unique_ids)
count_match = re.search(r"\*\*Count:\*\* (\d+)", the_list)
if not count_match:
    errors.append("The List has no canonical Count field")
else:
    declared = int(count_match.group(1))
    if declared != canonical_count:
        errors.append(f"The List declares {declared} models but contains {canonical_count} unique GLS IDs")

for label, text in (("models/README.md", model_readme), ("README.md", root_readme)):
    counts = [int(x) for x in re.findall(r"\b(\d+) (?:purchasable smart-glasses models|models and generations)", text)]
    for count in counts:
        if count != canonical_count:
            errors.append(f"{label} says {count} models; canonical ledger has {canonical_count}")

# Historical milestones are allowed to remain in prose. These patterns are reserved
# for statements that explicitly claim to describe the *current* canonical total.
current_count_patterns = (
    ("active canonical count is now", r"active canonical count is now \*\*(\d+)\*\*"),
    ("returns the active canonical count to", r"returns the active canonical count to \*\*(\d+)\*\*"),
    ("every active canonical record", r"\*\*every one of the (\d+) active canonical smart-glasses records\*\*"),
)
for label, pattern in current_count_patterns:
    for match in re.finditer(pattern, model_readme):
        count = int(match.group(1))
        if count != canonical_count:
            errors.append(
                f"models/README.md current-count statement ({label}) says {count}; canonical ledger has {canonical_count}"
            )

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
missing_ids = sorted(chapter_ids - unique_ids - retired_ids)
if missing_ids:
    errors.append("Model research references IDs absent from The List: " + ", ".join(missing_ids))

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

print(f"Catalog consistency check passed: {canonical_count} canonical models; {len(lineage_files)} lineage chapters.")