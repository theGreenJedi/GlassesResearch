# Open Hacking and Vendor Independence

GlassesResearch supports lawful owner control, repair, interoperability, preservation, and modification of smart glasses.

This collection documents ways owners and researchers can understand their devices, reduce vendor dependence, preserve abandoned functionality, and build open integrations.

## Start here

- [Open Hacking Resource Ledger](OPEN_HACKING_RESOURCE_LEDGER.md) — populated cross-platform index of concrete public projects, SDKs, open-source platforms, and preservation targets.
- [Ecosystem Resource Catalog](../resources/ECOSYSTEM_RESOURCE_CATALOG.md) — broader intake layer for software, firmware, SDKs, protocols, hardware files, developer documentation, and fragile research leads.
- [Preserved Artifact Ledger](../resources/PRIMARY_ARTIFACT_PRESERVATION_LEDGER.md) — provenance and preservation records for artifacts worth keeping.
- [W610 Open-Hacking Dossier](../models/W610/hacking/README.md) — current hands-on owner-control research, including verified baseline behavior and the active unverified queue.

## Publication rule

> **Only procedures verified working on an identified model, hardware revision, firmware version, and toolchain may be published as working guides.**

A popular post, video, repository, or repeated claim is not automatically a working guide. Reproducibility is the standard.

Unverified material may be preserved only in a clearly marked **Not Verified Yet** research queue. It must not be written as an instruction, recommendation, or established capability.

## Status vocabulary

- **Verified Working** — reproduced successfully with recorded model, revision, versions, date, evidence, and recovery notes.
- **Community Confirmed** — multiple independent reports exist, but GlassesResearch has not completed a qualifying verification. This remains outside the working-guide library.
- **Not Verified Yet** — plausible lead awaiting controlled testing. Never presented as a working procedure.
- **Hypothesis** — proposed technical explanation or experiment without adequate evidence.
- **Disproven** — tested and found not to work under the recorded conditions.
- **Historical** — preserved because it once existed or may aid future research; not represented as currently functional.

## Research lanes

The hacking collection actively tracks:

- alternative companion applications and vendor-app replacement;
- BLE advertising, GATT services, packet captures, and writable controls;
- unofficial APIs, SDKs, libraries, and protocol documentation;
- local-first AI, OCR, speech, and user-selected model integrations;
- firmware acquisition, hashing, lawful preservation, replacement, and modification;
- bootloader, flashing, rollback, and recovery procedures;
- vendor-cloud dependencies and lawful bypass or replacement paths on owned devices;
- UART, JTAG, PCB, teardown, and hardware-revision evidence;
- repair, parts substitution, optics, and hardware modifications;
- FCC/regulatory records that reveal chipsets, radios, internal photos, or model relationships;
- open-source projects, build environments, and cross-device platforms;
- abandoned-device restoration and long-term preservation.

## What does not belong here

- stolen credentials or private keys;
- attacks against services or devices without authorization;
- instructions whose only purpose is bypassing payment, licensing, or access controls unlawfully;
- proprietary files distributed without permission;
- personal data or captured traffic belonging to others;
- untested procedures described as working.

## Required record for every verified guide

```text
Title:
Status: Verified Working
Model:
Hardware revision:
Firmware version:
Companion-app version:
Host OS / phone:
Tools and versions:
Date verified:
Verified by:
Original discoverer / source:
Risk level:
Prerequisites:
Procedure:
Expected result:
Evidence:
Recovery / rollback:
Known limitations:
Last rechecked:
```

## Risk levels

- **Low** — read-only inspection or easily reversible configuration.
- **Moderate** — writes settings or installs software but has a documented rollback.
- **High** — modifies firmware, partitions, boot state, or hardware.
- **Brick Risk** — failure may make the device unusable or require specialized recovery.

Risk labeling does not replace judgment. A procedure without a tested recovery path cannot be called low risk.

## Model-by-model index

| Model or family | Working evidence | Open research | Current state |
|---|---|---|---|
| W610 / HeyCyan variants | [Verified baseline](../models/W610/hacking/README.md#verified-working) | [Active queue](../models/W610/hacking/README.md#not-verified-yet) | Hands-on control baseline established; protocol, firmware, recovery, and assistant-replacement research remains open. |
| Brilliant Labs Frame family | Public source ecosystem indexed in the [resource ledger](OPEN_HACKING_RESOURCE_LEDGER.md) | Build, firmware, protocol, hardware, and portability research | Publicly inspectable platform; GlassesResearch reproduction pending. |
| Mentra-compatible devices | MentraOS and open-hardware projects indexed in the [resource ledger](OPEN_HACKING_RESOURCE_LEDGER.md) | Compatibility, SDK, build, and vendor-independence testing | High-value cross-device open-development target. |
| Vuzix / Snap / XREAL / RayNeo / Rokid | Project-primary developer/platform sources indexed | SDK, firmware, update, recovery, protocol, and host-dependency research | Intake and preservation underway; no GlassesResearch working-guide status implied. |

## Promotion workflow

```text
Not Verified Yet
        |
        +--> controlled test fails --> Disproven
        |
        +--> evidence remains incomplete --> Not Verified Yet
        |
        +--> multiple independent reports --> Community Confirmed
        |
        +--> qualifying reproduction + evidence --> Verified Working
```

A status change must record what changed, who tested it, the date, the exact device and software environment, and the evidence path.

## Archive first, organize second

When firmware, APKs, SDKs, protocol notes, repositories, manuals, packet captures, flashing instructions, recovery procedures, or hardware evidence appear likely to disappear, preserve provenance immediately. Record the canonical source, owner, retrieval date, version, license or redistribution status, and hashes where appropriate. Do not delay preservation merely because the final taxonomy is unfinished.

## Institutional principle

> **Ownership should include the practical ability to understand, maintain, repair, interoperate with, and lawfully modify the device.**

The purpose of this collection is not novelty hacking. It is durable owner control.