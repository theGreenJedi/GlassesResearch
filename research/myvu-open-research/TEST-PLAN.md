# MYVU Conformance / Bench Test Plan

Goal: turn community and upstream knowledge into reproducible GlassesResearch evidence without destructive experimentation.

## 0. Identity capture

Before connecting:

- photograph packaging/labels and printed model identifier;
- record marketed name/brand;
- record firmware/build if accessible without changing state;
- record mass and relevant physical identifiers under normal GR bench procedure;
- assign specimen ID.

## 1. Host baseline

Record host phone/computer, OS/version, Bluetooth state, official-app version/region if used, and client/SDK commit/tag. Disconnect competing known centrals during protocol tests.

## 2. Passive Bluetooth inventory

Capture advertised name, address behavior, service UUIDs and other non-destructive advertising data before attempting protocol assumptions.

## 3. GATT inventory

Enumerate services/characteristics and compare raw observations against the documented Air (`0x2020–0x2023`) and V2 (`0x2010–0x2012`) patterns. Preserve unexpected values rather than forcing them into an existing lineage.

## 4. Connection sequence

Test BLE-first behavior, pairing/bond progression, ability authentication, initialization and relay establishment. Record timing and failure point. Confirm whether heartbeat loss produces the documented disconnect behavior.

## 5. Feature conformance

After a stable connection, test one feature at a time:

1. device/status query;
2. clock sync;
3. brightness/volume using reversible settings;
4. notification;
5. teleprompter;
6. trackpad;
7. weather;
8. microphone/AI only after transport is stable.

Record pass/fail/partial and raw evidence.

## 6. Failure-mode reproduction

Where applicable:

- discovery vs MAC-directed connection;
- teleprompter/AI runtime until screen/link/device state changes;
- wear-detection and standby interactions;
- app backgrounding;
- reconnect behavior;
- overhead-light rainbow/artifact observation.

## 7. Compatibility record

Update `COMPATIBILITY.md` only with exact identity and evidence state. A successful test on one specimen/firmware does not establish family-wide compatibility.

## 8. Required evidence output

A test is not complete until one evidence record exists with all applicable fields below. Unknown values are recorded as `UNKNOWN`; they are not omitted or guessed.

```text
Test ID:
Specimen ID:
Operator:
Date/time + timezone:
Hardware marketed name:
Printed/model identifier:
Hardware revision:
Firmware/build:
Host device:
Host OS/version:
Official companion app + version/region/source:
Alternative client/SDK + exact commit/tag:
Test-plan section / procedure:
Preconditions:
Observed BLE advertised identity:
Observed GATT services/characteristics:
RFCOMM/BR-EDR observation (if applicable):
Result: PASS / FAIL / PARTIAL / NOT-TESTED
Failure point or unexpected behavior:
Raw evidence location(s):
Photos/video/log/packet-capture identifiers:
Community/upstream claim being tested:
Evidence state before test:
Evidence state after test:
Notes / confounders:
```

### Raw-evidence rule

For protocol claims, preserve the raw observation needed to audit the normalized conclusion: packet capture, Bluetooth/GATT dump, application log, exact command/response bytes, or equivalent. For physical/optical claims, preserve the documented setup, environmental conditions and photographs/video where useful.

Do not store credentials, API keys, personal message contents, unrelated device identifiers, or other unnecessary private data in public evidence. Redact before commit while preserving the technical signal.

### Evidence-state transitions

- A successful reproduction can support `GR-VERIFIED` only for the identified specimen/firmware/test conditions.
- A failed reproduction does not automatically falsify an upstream/community observation; record the disagreement and investigate changed hardware, firmware, host or procedure.
- A partial reproduction stays `PARTIAL`/qualified and must not be summarized as a pass.
- Protocol agreement between multiple projects that share the same upstream implementation is not independent verification.

## Safety / restraint

Routine conformance testing excludes factory reset, recovery flashing, destructive firmware modification, bypassing hardware protections, or other difficult-to-reverse actions. Such work requires a separate investigation rationale and recovery plan.