# MYVU XGA010C technical network and owner-test plan

**Date:** 2026-09-14  
**Subject:** MYVU Air / StarV Air (`XGA010C`)  
**Evidence lane:** Community-primary technical research + GlassesResearch investigation planning  
**Independent GlassesResearch reproduction:** Pending controlled specimen

## Mission

Connect otherwise fragmented public work around XGA010C without collapsing different projects, devices, or evidence states into one claim. Preserve what is inspectable now, identify what can be tested when GlassesResearch obtains a specimen, and quarantine claims that cannot yet be traced to a primary artifact.

## Technical network

### XGA010C hardware identity

The MYVU / Star Air model identity is independently anchored by manufacturer/regulatory material as `XGA010C`. Community projects discussed below target that model explicitly unless otherwise stated.

### Panny777 — replacement client and protocol work

Panny777 publishes two directly inspectable projects:

- `Panny777/Meizu-Myvu-Client` — an unofficial replacement client described by its maintainer as hardware-verified against one pair of XGA010C glasses;
- `Panny777/Meizu-Myvu-SDK` — an unofficial Android SDK plus `PROTOCOL.md`, derived from packet captures and reverse engineering.

The published work documents a two-link architecture: BLE first for wake/session work, then a per-session Classic Bluetooth/RFCOMM relay for application traffic. Published control surfaces include teleprompter output, notifications, brightness/volume, settings, weather, navigation, trackpad actions and microphone/assistant integration.

**Evidence state:** community-primary, hardware-tested by the project author; not yet independently reproduced by GlassesResearch.

### FerSaiyan — CyanBridge / Alternative HeyCyan App and SDK

FerSaiyan's `Alternative-HeyCyan-App-and-SDK` repository is primarily an Android companion and interoperability workspace for HeyCyan-compatible glasses. Its public documentation explicitly credits upstream community work and describes native MYVU interoperability as a separate integration target rather than proof that W610/HeyCyan and XGA010C share identical hardware or firmware.

The useful connection is therefore **knowledge flow**, not automatic lineage:

`XGA010C hardware` → `Panny777 reverse engineering` → `documented protocol/client` → `downstream interoperability work such as CyanBridge`

**Evidence state:** community-primary software project. Any XGA010C behavior attributed to CyanBridge must be traced to a concrete implementation or test before promotion.

## Claims deliberately NOT promoted

During discovery, a firmware/OTA experimentation lead was discussed that was described as involving an XGA010C OTA-bank-sized image of roughly 423 KB and hardware testing by a community developer. GlassesResearch has not yet located a directly inspectable primary artifact sufficient to establish that claim.

Therefore, as of 2026-09-14:

- the ~423 KB figure is **not admitted as evidence**;
- successful firmware replacement is **not established**;
- arbitrary code execution is **not established**;
- root access is **not established**;
- a complete custom-firmware build/flash/recovery chain is **not established**.

If the primary source is located later, it should receive its own provenance record and be evaluated independently. A hardware-tested OTA manipulation would still not, by itself, prove arbitrary code execution or a general custom-firmware path.

## Owner-testing protocol for a GlassesResearch specimen

### Stage 0 — identity and preservation

1. Photograph packaging, model labels, regulatory marks, connectors, lenses and frame details before configuration.
2. Record exact advertised Bluetooth names, firmware version, companion-app version and phone OS/version.
3. Hash and preserve any lawfully obtained application, firmware, update package or protocol artifact before modification.
4. Record all hardware/software revision identifiers that can distinguish this specimen from rebrands or later revisions.

### Stage 1 — non-destructive transport mapping

1. Enumerate BLE advertisements, service UUIDs and characteristics without writing undocumented values.
2. Observe Classic Bluetooth services and whether BLE-first wake/session behavior is reproducible.
3. Confirm whether the device accepts only one central/host at a time.
4. Capture connection timing, disconnect behavior and heartbeat/session requirements.

### Stage 2 — bounded interoperability reproduction

Using the published community client/SDK as the comparison target, attempt only benign reversible functions first:

1. pair/session establishment;
2. one teleprompter/display message;
3. brightness control;
4. one status query;
5. one inbound trackpad/event observation;
6. notification delivery;
7. microphone/audio path only after the transport path is understood.

For each result, preserve packet/log evidence and classify it separately as reproduced, failed, variant-dependent or unresolved.

### Stage 3 — firmware/update reconnaissance

Do not perform destructive writes merely because an update path exists.

1. Identify official update mechanisms and downloadable artifacts.
2. Record filenames, sizes, hashes, headers, manifests, signatures and version metadata.
3. Determine whether update verification/signature behavior can be observed without bypassing it.
4. If a read/dump path exists, make and hash backups before any write experiment.
5. Establish a documented recovery path before testing modified images.
6. Treat UART/JTAG/SWD as conditional hypotheses until physical pads/interfaces are actually identified.

### Stage 4 — modification threshold

Any write that can brick the specimen requires all of the following first:

- specimen identity recorded;
- original firmware/update artifact preserved where lawfully obtainable;
- recovery method documented and, where feasible, tested;
- exact hypothesis stated;
- expected success/failure signal stated;
- rollback path available.

## Evidence-state vocabulary for this investigation

- **Authoritative / primary:** manufacturer, regulatory or directly inspectable project artifact.
- **Community-primary:** original developer's repository, logs, code or hardware-test report.
- **GlassesResearch observed:** directly seen/measured on our specimen.
- **GlassesResearch reproduced:** repeatable result produced under a documented test.
- **Community report:** owner/developer statement without sufficient directly inspectable evidence.
- **Lead / hypothesis:** useful direction not yet admitted as evidence.

Do not convert one state into another through repetition.

## Primary sources currently admitted

- Panny777 — Meizu MYVU Client: https://github.com/Panny777/Meizu-Myvu-Client
- Panny777 — MYVU Android SDK: https://github.com/Panny777/Meizu-Myvu-SDK
- Panny777 — MYVU wire protocol: https://github.com/Panny777/Meizu-Myvu-SDK/blob/main/PROTOCOL.md
- FerSaiyan — Alternative HeyCyan App and SDK / CyanBridge: https://github.com/FerSaiyan/Alternative-HeyCyan-App-and-SDK
- Manufacturer manual for XGA010C: https://fms.res.meizu.com/dms/2025/02/17/7355710f-cfac-46ca-9f6c-857703cac963.pdf

## Investigation queue

1. Acquire/control an XGA010C specimen and execute Stages 0–2 before considering firmware writes.
2. Preserve exact versions/hashes of Panny777 artifacts used for replication.
3. Trace CyanBridge's current MYVU integration to concrete source paths and document which behaviors are inherited, reimplemented or still planned.
4. Locate the primary artifact behind the discussed firmware/OTA lead; until then keep it quarantined as a lead.
5. If a firmware artifact is located, record provenance, hash, format, signature/verification behavior and recovery implications before testing.
6. Promote only successfully reproduced results into GlassesResearch lab evidence and Report Card narratives.

## Disposition

The XGA010C now has a single cross-project technical map and a specimen-ready, preservation-first owner-testing protocol. The strongest present conclusion remains: **third-party application-level interoperability is well supported by community-primary, hardware-tested work; firmware-level owner control remains unproven.**
