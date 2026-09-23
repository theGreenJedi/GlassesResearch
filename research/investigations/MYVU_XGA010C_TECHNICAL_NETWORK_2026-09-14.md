# MYVU XGA010C technical network and owner-test plan

**Date:** 2026-09-14  
**Subject:** MYVU Air / StarV Air (`XGA010C`)  
**Evidence lane:** Community-primary technical research + GlassesResearch investigation planning  
**Independent GlassesResearch reproduction:** Pending controlled specimen  
**Substantive update:** 2026-09-23 — BimaPDev firmware evidence expanded with post-flash iOS/ANCS bond failure mode

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

## BimaPDev — firmware modification and bounded native execution

The previously quarantined XGA010C firmware/OTA lead is now traceable to a directly inspectable public primary project: `BimaPDev/SmartGlasses`. The project documents firmware analysis and patching, hardware-visible modified firmware, execution of hand-written Thumb from PSRAM, and subsequent hardware-confirmed execution of compiled C from PSRAM with calls back into vendor firmware.

Follow-up hardware testing used multiple callback detours and visible rendering behavior as positive controls. This advances the old firmware lead from **unresolved** to **community-primary, hardware-tested**.

The evidence does **not** establish root access, unrestricted native applications, a complete replacement firmware, or a general custom-firmware build/flash/recovery chain. Published payload work still records explicit limits around payload-owned data/BSS/string-literal/literal-pool use.

BimaPDev also documented that assumptions about firmware regions and offsets can vary by build. Addresses, patch offsets and resource boundaries must therefore remain firmware-version-specific unless separately demonstrated.

**Primary sources:**
- https://github.com/BimaPDev/SmartGlasses
- https://github.com/BimaPDev/SmartGlasses/commit/8f5c6b71a23de9d7453bb9d5df7f6a2993dbaae9
- https://github.com/BimaPDev/SmartGlasses/commit/d2aa057a7de6dc7aa3cce0d4de68bc9e9ac99757

### Filesystem and transfer boundary

The same project documents a LittleFS-backed storage path plus a protobuf ShareMessage BLE transfer family with named chunked transfers, MD5 verification, acknowledgements and pull-by-known-filename behavior. Its negative tests report no filesystem-list operation in the examined transfer family, while the examined LittleFS adapter reports writes as unsupported and loads its partition from flash into PSRAM at boot.

This is useful interoperability evidence but not evidence of arbitrary filesystem enumeration or a simple replacement-file path.

**Primary source:** https://github.com/BimaPDev/SmartGlasses/commit/01a374068fba8730b4b497a82bacfda730412428

### Boot versus shutdown assets

A hardware-visible rebrand showed modified BIMA branding at power-off while boot still displayed MYVU. After correcting an earlier incomplete resource search, the project reported the shutdown asset inside the OTA-carried image but no boot/splash asset there.

The empirical distinction is useful. The exact boot asset location remains unresolved.

**Primary source:** https://github.com/BimaPDev/SmartGlasses/commit/b9bbe7dbe87660736c5016baef0fee36ab270cf4


### Post-flash iOS / ANCS bond state

BimaPDev reports that flashing firmware clears the glasses' LE bond database while iOS may retain its prior bond record. Because the proprietary MYVU application session uses a separate application-layer ECDH exchange, that path can continue to appear functional while ANCS notifications fail for lack of the expected encrypted BLE bond. The reported recovery is to forget the glasses in iOS and pair again.

**Evidence state:** community-primary, hardware-tested by the project author; not yet reproduced by GlassesResearch.

**Primary source:** https://github.com/BimaPDev/SmartGlasses/commit/2702c70247af7d3458c9cc4ea2881f36d21bfd09

**Test implication:** after any firmware flash, explicitly reset/re-establish the phone bond before using ANCS failure as evidence of a firmware or notification regression.

## Claims still deliberately NOT promoted

Even with the stronger BimaPDev evidence, GlassesResearch does not presently claim:

- root access;
- unrestricted arbitrary native execution;
- a complete owner-buildable replacement firmware;
- a universal flash/recovery chain across XGA010C firmware versions;
- the exact physical location of the boot asset;
- GlassesResearch-independent reproduction of BimaPDev's firmware results.

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
4. Preserve the exact BimaPDev commits, firmware-build identifiers and tooling used for any reproduction; do not transplant offsets across builds.
5. Reproduce one deliberately benign, hardware-visible firmware modification only after recovery prerequisites are satisfied, then separately test the bounded PSRAM execution path.
6. After any firmware flash, forget/re-pair the specimen on iOS before ANCS validation and record bond state as part of the test evidence.
7. Record provenance, hashes, format, signature/verification behavior and recovery implications before any GlassesResearch write experiment.
8. Promote only successfully reproduced results into GlassesResearch lab evidence and Report Card narratives.

## Disposition

The XGA010C now has a cross-project technical map spanning Panny777 application/protocol interoperability, CyanBridge knowledge flow, and BimaPDev firmware work. The evidence now supports a stronger but bounded conclusion: **third-party application-level interoperability and a firmware-level owner-controlled execution path are supported by community-primary, hardware-tested work. GlassesResearch has not independently reproduced either result, and complete custom firmware/root/general native execution remain unproven.**
