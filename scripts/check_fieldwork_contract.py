#!/usr/bin/env python3
"""Validate Fieldwork questionnaire/submission privacy invariants."""
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
questionnaire = json.loads((ROOT / "data/fieldwork-questionnaire.v1.json").read_text(encoding="utf-8"))
schema = json.loads((ROOT / "data/fieldwork-submission.schema.json").read_text(encoding="utf-8"))
errors = []

sections = questionnaire.get("sections", [])
questions = [q for section in sections for q in section.get("questions", [])]
ids = [q.get("id") for q in questions]

if len(questions) < 60:
    errors.append(f"Fieldwork v1 unexpectedly shrank below 60 questions ({len(questions)})")
if len(ids) != len(set(ids)):
    errors.append("Fieldwork question IDs must be unique")
if questionnaire.get("completion", {}).get("minimum_valid_submission_percent") != 50:
    errors.append("Minimum valid Fieldwork Completion must remain 50%")
if questionnaire.get("completion", {}).get("maximum_percent") != 100:
    errors.append("Maximum Fieldwork Completion must remain 100%")
if questionnaire.get("privacy", {}).get("default_attribution") != "anonymous":
    errors.append("Fieldwork must remain anonymous-by-default")
if questionnaire.get("privacy", {}).get("raw_serial_persisted") is not False:
    errors.append("Raw serial persistence must remain prohibited")

serial_questions = [q for q in questions if q.get("id") == "serial"]
if len(serial_questions) != 1 or serial_questions[0].get("type") != "serial_private":
    errors.append("Serial intake must use the serial_private control")

schema_text = json.dumps(schema).lower()
for forbidden in ('"serial"', '"serial_number"', '"raw_serial"'):
    # The only permitted appearances are in explicit prohibitions/descriptions.
    if forbidden in schema.get("properties", {}):
        errors.append(f"Persisted submission schema must not define {forbidden} as a property")

required = set(schema.get("required", []))
for field in ("model", "access_basis", "attestation_hands_on", "completion_percent", "answers"):
    if field not in required:
        errors.append(f"Submission schema must require {field}")

if errors:
    print("Fieldwork contract validation failed:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print(f"Fieldwork contract clean: {len(questions)} questions; anonymous default; raw serial persistence prohibited.")
