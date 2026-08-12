#!/usr/bin/env python3
"""Fail CI when canonical model/lineage surfaces drift out of sync."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
errors = []

the_list = (ROOT / "models/THE_LIST.md").read_text(encoding="utf-8")
model_readme = (ROOT / "models/README.md").read_text(encoding="utf-8")
root_readme = (ROOT / "README.md").read_text(encoding="utf-8")
lineage_index = (ROOT / "lineages/README.md").read_text(encoding="utf-8")
mkdocs = (ROOT / "mkdocs.yml").read_text(encoding="utf-8")

ids = re.findall(r"^\| (GLS-\d{4}) \|", the_list, flags=re.M)
unique_ids = set(ids)
count_match = re.search(r"\*\*Count:\*\* (\d+)", the_list)
if not count_match:
    errors.append("The List has no canonical Count field")
else:
    declared = int(count_match.group(1))
    if declared != len(unique_ids):
        errors.append(f"The List declares {declared} models but contains {len(unique_ids)} unique GLS IDs")

for label, text in (("models/README.md", model_readme), ("README.md", root_readme)):
    counts = [int(x) for x in re.findall(r"\b(\d+) (?:purchasable smart-glasses models|models and generations)", text)]
    for count in counts:
        if count != len(unique_ids):
            errors.append(f"{label} says {count} models; canonical ledger has {len(unique_ids)}")

chapter_ids = set(re.findall(r"GLS-\d{4}", model_readme))
missing_ids = sorted(chapter_ids - unique_ids)
if missing_ids:
    errors.append("Model research references IDs absent from The List: " + ", ".join(missing_ids))

lineage_files = sorted(p for p in (ROOT / "lineages").glob("*.md") if p.name != "README.md")
for path in lineage_files:
    rel = f"lineages/{path.name}"
    if f"({path.name})" not in lineage_index:
        errors.append(f"{rel} exists but is absent from lineage index")
    if rel not in mkdocs:
        errors.append(f"{rel} exists but is absent from MkDocs lineage navigation")

if errors:
    print("Catalog consistency check FAILED:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print(f"Catalog consistency check passed: {len(unique_ids)} canonical models; {len(lineage_files)} lineage chapters.")
