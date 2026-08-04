# APP-0001 — HeyCyan

## Identity

- **Type:** Android companion application and cloud-service client
- **Observed device relationship:** The received unit advertises as `HeyCyan Glasses`
- **Reported package:** `com.glasssutdio.wear` (spelling requires verification from an acquired APK)
- **Operator:** [ORG-0001 — Shenzhen Qingcheng Future Technology](../organizations/ORG-0001-hecyan-qingcheng-future.md)
- **Confidence:** Application relationship strongly supported; package and supported-model details require direct APK preservation
- **Last checked:** 2026-08-03

## Why it matters

The app may reveal pairing procedures, BLE UUIDs, Wi-Fi transfer behavior, cloud endpoints, supported-device identifiers, firmware-update mechanisms, privacy practices, and feature gating. The project intentionally avoided installing it during the earliest baseline tests so original device behavior could be documented first.

## Useful links

- [Google Play search for HeyCyan](https://play.google.com/store/search?q=HeyCyan&c=apps) — current Android listing and developer information.
- [Google search for HeyCyan APK](https://www.google.com/search?q=HeyCyan+APK) — APK mirrors and historical versions; treat third-party downloads as untrusted until hashed and scanned.
- [GitHub search for HeyCyan](https://github.com/search?q=HeyCyan&type=code) — integrations, strings, package references, and reverse-engineering leads.

## Research cautions

Do not install unknown APK mirrors on a trusted phone. Preserve package name, version, signing certificate, hashes, permissions, domains, and extracted resources before analysis.

## Related

- [W610 software section](../../models/W610/software/README.md)
- [INV-0001 — W610 Identity](../../models/W610/investigations/001-identity.md)
