# GREP — GlassesResearch Evaluation Protocol

Status: design specification

GREP is the GlassesResearch family of repeatable hands-on evaluation instruments. Every GREP form has the same end goal: acquire structured evidence capable of supporting a GlassesResearch Report Card without turning observations into claims they do not justify.

## Forms

- **GREP-42 — NDI / controlled inspection.** For borrowed, return-window, non-destructive, or limited-access specimens. Measurement-heavy and deliberately conservative.
- **GREP-44 — comprehensive owned-device investigation.** For specimens GlassesResearch owns and can revisit. Incorporates the GREP-42 core, deeper technical investigation, and GREP-46 real-world evidence where applicable.
- **GREP-46 — real-world experience and use cases.** For longitudinal wear, usability, functional usefulness, environment, and use-case evidence.

Any one of these may form the evidentiary basis of a Report Card. The form used and its completion depth must be disclosed with the Report Card.

## Core rule

**Tests create evidence. Evidence supports Report Card findings. The examiner does not assign Report Card scores while running the form.**

Every observation records what was tested, conditions, result, and an evidence/artifact identifier where appropriate. Manufacturer claims, hands-on findings, primary documentation, commercial material, community evidence, inference, hypothesis, disproven claims, and unknowns remain distinct evidence lanes.

## Standard result states

Use only states appropriate to the field:

- PASS
- FAIL
- MEASURED
- OBSERVED
- UNKNOWN
- NOT TESTED
- NOT APPLICABLE
- BLOCKED

`UNKNOWN` is a valid result and must never be silently converted to a negative or positive score. `NOT TESTED` means the test was applicable but was not performed. `BLOCKED` requires a reason.

## Stable field namespaces

Fields shared between forms retain the same identifier and semantics. Initial namespaces:

- `ID` identity/provenance
- `HW` physical hardware/metrology
- `PW` power/charging/battery
- `IF` radios/interfaces/connectivity
- `FN` functional behavior
- `VA` visual AI/camera sensing
- `DP` display/optics
- `AU` audio
- `SW` software/companion
- `OP` openness
- `OC` owner control
- `CI` cloud independence
- `HK` hackability
- `PR` privacy/security observations
- `WR` wearability/fit
- `UC` real-world use cases
- `SV` serviceability
- `VL` value/acquisition context

A field such as `OC-04` means the same thing wherever it appears. A GREP-42 result may therefore be reused when a specimen later graduates to GREP-44 rather than being re-entered solely because the form changed.

## Evidence packet

A completed form should identify the specimen, examiner/session, form revision, firmware/software state when observable, equipment used, test conditions, evidence artifacts, applicable capability modules, skipped/blocked tests, and completion status.

Artifacts may include photographs, video, measurements, USB enumeration, Bluetooth captures, RF observations, network observations, logs, screenshots, exported media, audio samples, optical test photographs, notes, and later teardown evidence. Artifact identifiers should be human-readable and specimen-scoped, for example `W610-01-IF-003`.

## Report Card disclosure

A Report Card based on GREP evidence should disclose its evaluation basis, for example:

> Evaluation basis: GREP-42 NDI — partial. Physical examination complete; passive RF/USB inspection complete; companion application not installed; longitudinal wear not evaluated.

or:

> Evaluation basis: GREP-44 comprehensive — bench and functional examination complete; software/control investigation complete; 21-day real-world evaluation; destructive teardown not performed.

Coverage matters independently of score. A high score supported by thin evidence must not appear equivalent to a high score supported by a comprehensive owned-device investigation.

## Capability modules

The common core is supplemented only when applicable: camera/visual AI, display/optics, audio, prescription/fit, standalone compute/OS, sensors, navigation, translation, accessibility, and teardown/serviceability. Absence of a capability does not penalize a device unless the Report Card rubric explicitly evaluates the device against a documented claimed purpose.

## Form lifecycle

These files define the forms before typesetting. First calibrate the field set and Report Card mapping on real specimens, beginning with W610 for GREP-44. After the designs survive bench use, produce printable form revisions. Form revisions must be recorded so historical evaluations remain reproducible.