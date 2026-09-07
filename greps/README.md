# GREPs — GlassesResearch Evaluation Protocol forms

This folder is the working home for printable GlassesResearch bench forms.

## Current printable forms

- [GREP-42 — Controlled NDI / Limited-Access Inspection](GREP-42.html)
- [GREP-44 — Comprehensive Owned-Device Investigation](GREP-44.html)
- [GREP-46 — Real-World Experience and Use Cases](GREP-46.html)

Open an HTML form in a browser and print at 100% / Actual Size. The stylesheet targets US Letter paper with single-sided pages. Never print these forms duplex. Metric/SI values are canonical; imperial conversions may be added only as secondary convenience notes.

## Header and notation canon

Every printable form must:

1. show the GREP number prominently at the top;
2. spell out **GlassesResearch Evaluation Protocol** directly beneath it;
3. state the specific examination/form name;
4. provide specimen, examiner, date/configuration and evidence/provenance fields;
5. use stable field namespaces when a field is shared between GREPs;
6. provide explicit room for examiner impressions, subjective observations and explanations;
7. distinguish **NT — Not Tested** from **NP — Not Present / Not Applicable**;
8. preserve UNKNOWN as a valid research state instead of forcing a yes/no answer;
9. keep measurements metric/SI-first and authoritative;
10. record evidence/artifact identifiers wherever an observation may support a Report Card.

The forms collect evidence. They do **not** assign Report Card scores during examination.

## The three progenitors

The current printable generation descends from the earlier GREP design work:

- **GREP-42** — measurement-heavy, conservative controlled inspection for borrowed, return-window or otherwise limited-access specimens;
- **GREP-44** — the deepest repeatable owned-device investigation, incorporating valid GREP-42 evidence plus deeper power, protocol, software/dependency, owner-control and capability testing;
- **GREP-46** — repeated real-world wear, reliability, battery and use-case evidence over time.

GREP-44 does not redefine shared tests. A valid GREP-42 observation can carry forward with its original date and evidence ID; GREP-46 sessions can attach to GREP-44 when longitudinal evidence exists.

## Original design specifications

The pre-typesetting design specifications are preserved in [`original-designs/`](original-designs/) so future form revisions can be compared against the design intent rather than relying on memory.

## Result vocabulary

Use only the state appropriate to the field:

- PASS
- FAIL
- MEASURED
- OBSERVED
- UNKNOWN
- NT — Not Tested
- NP — Not Present / Not Applicable
- BLOCKED

A blank field is not evidence. `NT` means the test was applicable but was not performed. `NP` means the capability or test truly is not present/applicable. `BLOCKED` requires a reason.

## Evidence lanes

Keep manufacturer claims, hands-on observations, primary documentation, commercial seller material, community evidence, inference/hypothesis, disproven claims and unknowns distinct. A supplier claim does not become a bench result because it appears on a form.

## Revision rule

Printable forms carry explicit revisions. Do not silently alter historical meaning. If a stable shared field changes semantics, mint a new field/revision and preserve the prior form for reproducibility.
