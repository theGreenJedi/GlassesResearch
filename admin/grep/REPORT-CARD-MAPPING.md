# GREP → GlassesResearch Report Card mapping

Status: design specification

This document prevents the forms from becoming disconnected laboratory paperwork. Every GREP instrument is designed to produce evidence for the existing GlassesResearch Report Card while preserving evidence depth and uncertainty.

## Governing rule

A GREP answer is not automatically a score. A field supplies evidence to one or more Report Card categories. Scoring rules consume the evidence later and must account for provenance, repeatability, contradictions, recency/configuration, and coverage.

## Category mapping

### Hardware
Primary GREP inputs: `ID`, `HW`, `PW`, `IF`, applicable `VA/DP/AU`, `SV`.
Questions answered: what hardware is physically present; measured size/mass; controls/connectors; power behavior; radio/interface capabilities; physical quality observations; capability implementation; reliability evidence.

### Wearability
Primary inputs: `HW`, `WR`, `PW`, `DP`, `AU`.
Questions answered: mass/geometry; pressure/slippage/balance; thermal behavior; prescription/fit; prolonged wear; visual comfort; interference with ordinary activities.

### Visual AI
Primary inputs: `VA`, `UC`, `SW`, `CI`.
Questions answered: camera/input capability; actual visual-AI tasks; accuracy evidence where controlled; latency; usefulness; processing/dependency boundaries. Devices without visual AI should be N/A rather than automatically poor unless the rubric explicitly defines otherwise.

### Software
Primary inputs: `SW`, `FN`, `UC`, `PR`.
Questions answered: setup burden; stability; permissions; recovery; feature behavior; updates; usability; reliability over time.

### Openness
Primary inputs: `IF`, `OP`, `SW`, `HK`.
Questions answered: documented interfaces; SDK/API; protocol accessibility; standards versus proprietary paths; ability for independent software to interact. Community reverse engineering is valuable evidence but is not equivalent to manufacturer-supported openness.

### Owner Control
Primary inputs: `OC`, `IF`, `SW`, `SV`.
Questions answered: can the owner access created media/data; choose software; invoke core functions; reset/recover; export; maintain/use the hardware without unnecessary vendor gatekeeping.

### Cloud Independence
Primary inputs: `CI`, `OC`, `SW`, `UC`.
Questions answered function-by-function: what continues offline; what needs internet; what needs vendor infrastructure; what can be performed locally or through alternative owner-controlled paths. Avoid one binary cloud/no-cloud label when capabilities differ.

### Hackability
Primary inputs: `HK`, `IF`, `OP`, `SV`.
Questions answered: observable interfaces; alternative clients; firmware availability; development/debug paths; documented hardware/service access; practical modifiability. Do not reward insecure design as if vulnerability were openness.

### Value
Primary inputs: `VL`, plus outcomes from every other category and `UC`.
Questions answered: acquisition price/route; included accessories; recurring costs; demonstrated usefulness; reliability; service/support context; capability relative to cost. Price must be dated and regionalized where relevant.

## Evidence depth labels

Each Report Card category should be able to expose a coverage/evidence label independent of its score. Proposed levels for later calibration:

- **E0 — Unknown:** no meaningful evidence.
- **E1 — Documentary:** primary/commercial/community evidence but no hands-on support for the category.
- **E2 — Hands-on limited:** GREP-42 or similarly bounded direct evidence supports some material claims.
- **E3 — Hands-on substantial:** multiple direct tests and/or GREP-46 longitudinal evidence cover most material questions.
- **E4 — Comprehensive:** GREP-44 evidence substantially covers applicable technical and real-world questions with unresolved gaps disclosed.

These labels are provisional until calibrated against real devices. They must not become a mechanism for inflating the product score; they describe confidence/coverage, not quality.

## Contradictions

When GREP evidence contradicts manufacturer, commercial, community or earlier hands-on evidence, preserve both records and flag the contradiction. Prefer the most directly relevant reproducible evidence for the tested specimen/configuration, but do not universalize one specimen result without justification.

## Configuration and recency

Firmware, app and cloud services can change. Evidence should retain configuration/date. A later GREP result may supersede an earlier behavioral result for current-state scoring while the earlier observation remains part of the historical evidence trail.

## Report Card generation handoff

When a completed form or photographs/scans of it are ingested:

1. identify specimen, GREP form and revision;
2. transcribe stable field IDs and results;
3. attach/resolve evidence artifact IDs;
4. preserve evidence lane and test conditions;
5. map fields to categories using this document;
6. identify contradictions and unresolved questions;
7. calculate category coverage separately from product performance;
8. apply the Report Card rubric only after evidence ingestion;
9. publish the GREP basis/coverage disclosure with the Report Card;
10. never convert blank, illegible, NOT TESTED or UNKNOWN fields into assumptions.

## Why multiple GREP forms can support a Report Card

GREP-42 can produce a useful conservative Report Card because direct measurements and bounded functional evidence are better than pretending unavailable evidence exists. GREP-46 can produce a useful experience-heavy Report Card because longitudinal behavior answers questions a bench inspection cannot. GREP-44 combines both and adds deep technical evidence, making it the preferred basis for GlassesResearch-owned long-term specimens.

The difference is evidence coverage and confidence, not whether the result is permitted to become a Report Card.