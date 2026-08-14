# W610 Research Backlog

This is the living investigation queue. GitHub issues may later mirror individual work items, but this page provides the model-level overview.

## Priority 0 — Preserve the baseline

- Photograph device, packaging, labels, accessories, manual, and QR materials
- Record advertised name, BLE name, app name, firmware version, and device identifiers with private data redacted
- Preserve APK version and source information where redistribution is lawful
- Record normal behavior before modification

## Priority 1 — Identity and architecture

- Determine whether W610 is a product name, platform name, or reference design
- Identify manufacturer, ODM, brand, importer, app operator, and cloud dependencies
- Establish W610 and W6xx genealogy
- Identify hardware revisions and retail rebrands

## Priority 2 — BLE and software

- Enumerate services and characteristics
- Capture pairing and normal command sequences
- Map commands, notifications, state, and error behavior
- Determine what works without internet or the vendor app
- Identify APK endpoints, permissions, trackers, and device-support tables

## Priority 3 — Hardware and firmware

- Execute the [EV-0043 battery protocol](../../evidence/EV-0043-W610-battery-evidence-and-verification.md): verify installed capacity hypothesis, workload runtime, charge behavior, telemetry and low-power cutoffs
- Identify a battery service path, cell dimensions/markings, protection circuit and connector/weld method only after the nondestructive gate is satisfied
- Identify components, test pads, debug interfaces, and storage
- Acquire and hash firmware or update packages when lawful
- Develop recovery and restore procedures before risky modification

## Priority 4 — User-controlled integrations

- Build a minimal independent BLE client
- Test local-first audio, capture, transcription, translation, and assistant workflows
- Document privacy boundaries and failure modes
- Separate generally reusable W6xx work from W610-specific behavior

## Work-item template

```text
Question:
Why it matters:
Current evidence:
Next experiment:
Required equipment or access:
Risk:
Success criteria:
Owner:
Status:
Related files / issues:
```
