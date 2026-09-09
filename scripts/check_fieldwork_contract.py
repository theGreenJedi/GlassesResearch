#!/usr/bin/env python3
"""Validate Fieldwork questionnaire/submission/privacy/app invariants."""
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

for forbidden in ('"serial"', '"serial_number"', '"raw_serial"'):
    if forbidden in schema.get("properties", {}):
        errors.append(f"Persisted submission schema must not define {forbidden} as a property")

required = set(schema.get("required", []))
for field in ("model", "access_basis", "attestation_hands_on", "completion_percent", "answers"):
    if field not in required:
        errors.append(f"Submission schema must require {field}")

app_path = ROOT / "docs/javascripts/fieldwork-app.js"
export_path = ROOT / "docs/javascripts/fieldwork-export.js"
page_path = ROOT / "docs/FIELDWORK_APP.md"
manifest_path = ROOT / "docs/fieldwork.webmanifest"
service_worker_path = ROOT / "docs/fieldwork-sw.js"
for path in (app_path, export_path, page_path, manifest_path, service_worker_path):
    if not path.exists():
        errors.append(f"Fieldwork app asset missing: {path.relative_to(ROOT)}")

if app_path.exists():
    app_text = app_path.read_text(encoding="utf-8")
    if "question.type === 'serial_private'" not in app_text or "continue;" not in app_text:
        errors.append("Fieldwork draft serialization must explicitly exclude serial_private")
    if "crypto.subtle.digest('SHA-256'" not in app_text:
        errors.append("Fieldwork app must derive the device fingerprint locally with Web Crypto")

if export_path.exists():
    export_text = export_path.read_text(encoding="utf-8")
    if "forbidden = new Set(['serial'" not in export_text:
        errors.append("Fieldwork export must explicitly forbid raw serial fields")
    for required_token in ("submission_id", "submitted_at", "access_basis", "attestation_hands_on", "completion_percent", "answers"):
        if required_token not in export_text:
            errors.append(f"Fieldwork export adapter missing schema field: {required_token}")

if page_path.exists():
    page_text = page_path.read_text(encoding="utf-8")
    for promise in ("Anonymous is welcome.", "Attribution is optional.", "Raw serial numbers are never retained."):
        if promise not in page_text:
            errors.append(f"Fieldwork app page missing privacy promise: {promise}")
    if "Anonymous direct submission is not enabled yet." not in page_text:
        errors.append("Fieldwork must not imply anonymous server submission exists before it does")

if manifest_path.exists():
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if manifest.get("display") != "standalone":
        errors.append("Fieldwork PWA manifest must remain installable/standalone")

if errors:
    print("Fieldwork contract validation failed:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print(f"Fieldwork contract clean: {len(questions)} questions; installable client; anonymous default; raw serial persistence prohibited.")
