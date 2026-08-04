# W610 Firmware

This section tracks firmware identity, update mechanisms, package metadata, hashes, recovery options, and analysis findings.

## Current state

- No firmware image has yet been acquired from the received device.
- No firmware version has yet been independently recorded.
- The HeyCyan application is the leading place to investigate supported-device identifiers and update endpoints.
- Commercial chipset claims point toward [CMP-0001 — JL7018F](../../../glossary/components/CMP-0001-jl7018f.md) and [CMP-0002 — Allwinner V821L2](../../../glossary/components/CMP-0002-allwinner-v821l2.md), but firmware architecture must not be inferred from listings alone.

## Acquisition priorities

1. Record any version strings exposed over Bluetooth, USB, app screens, logs, or update traffic.
2. Preserve APK versions and signing-certificate details before examining update behavior.
3. Capture update URLs, headers, filenames, hashes, and manifests without installing unknown packages.
4. Document recovery and rollback evidence before attempting modification.

## Publication boundary

Hashes, metadata, extraction procedures, and lawful source links may be published even when redistribution rights for binaries are unclear. Proprietary firmware should not be uploaded without permission.
