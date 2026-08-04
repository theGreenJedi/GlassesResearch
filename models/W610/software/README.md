# W610 Software, Apps, and SDKs

This section covers companion applications, permissions, network behavior, SDKs, APIs, integrations, and local-control experiments.

## Current state

- The received device advertises as `HeyCyan Glasses`.
- Multiple W610 commercial sources direct users to the HeyCyan companion app.
- The project initially avoided installing the vendor app in order to preserve an unmodified device baseline.
- [APP-0001 — HeyCyan](../../../glossary/applications/APP-0001-hecyan.md) is the canonical application record.
- [ORG-0001 — Shenzhen Qingcheng Future Technology](../../../glossary/organizations/ORG-0001-hecyan-qingcheng-future.md) is confirmed as the app operator; its hardware role remains unresolved.

## Investigation priorities

1. Acquire the official APK from a trustworthy source.
2. Record package name, version, signing certificate, permissions, SDK targets, domains, and supported-device strings.
3. Compare behavior with and without the vendor app.
4. Identify BLE and Wi-Fi responsibilities, firmware-update logic, and cloud dependencies.
5. Evaluate a local-first replacement path using documented protocols.

Third-party APK mirrors are leads, not trusted software. Analyze in an isolated environment before installation.
