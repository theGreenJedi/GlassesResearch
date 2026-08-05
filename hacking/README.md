# Open Hacking and Vendor Independence

GlassesResearch supports lawful owner control, repair, interoperability, preservation, and modification of smart glasses.

This collection documents ways owners and researchers can understand their devices, reduce vendor dependence, preserve abandoned functionality, and build open integrations.

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

## What belongs here

- alternative companion applications
- documented or reverse-engineered BLE control
- unofficial APIs and open libraries
- local-first AI integrations
- firmware acquisition and lawful preservation
- firmware replacement or modification
- bootloader and recovery research
- vendor-cloud bypasses on owned devices
- privacy hardening
- repair, parts substitution, and hardware modifications
- protocol captures and repeatable experiments
- abandoned-device restoration

## What does not belong here

- stolen credentials or private keys
- attacks against services or devices without authorization
- instructions whose only purpose is bypassing payment, licensing, or access controls unlawfully
- proprietary files distributed without permission
- personal data or captured traffic belonging to others
- untested procedures described as working

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

| Model or family | Verified working guides | Not Verified Yet queue | Current state |
|---|---:|---:|---|
| W610 / HeyCyan variants | [Open-hacking dossier](../models/W610/hacking/README.md) | Included in dossier | Initial verified device-control baseline; modification claims remain unverified |
| Other models | Added only when a model dossier contains evidence | Leads may be cataloged without instructions | Research intake |

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

## Institutional principle

> **Ownership should include the practical ability to understand, maintain, repair, interoperate with, and lawfully modify the device.**

The purpose of this collection is not novelty hacking. It is durable owner control.