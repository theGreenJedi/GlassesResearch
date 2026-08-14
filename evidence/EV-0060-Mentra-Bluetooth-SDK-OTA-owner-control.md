# EV-0060 — Mentra Bluetooth SDK, durable OTA manifests, and direct host control

- **Evidence ID:** EV-0060
- **Platform:** MentraOS / Mentra Live
- **Evidence class:** community primary source and vendor primary source
- **Reviewed:** 2026-08-14
- **Status:** source-verified; no GlassesResearch hands-on reproduction
- **Canonical model:** [GLS-0038 — Mentra Live](../models/catalog/gls-0038.md)

## Finding

Mentra publishes a cross-platform Bluetooth SDK that lets an owner-written Android or iOS host application connect directly to supported glasses. For Mentra Live, the documented surface includes camera, microphones, speakers, buttons, touch input, battery and connectivity state, Wi-Fi configuration, capture, streaming, and over-the-air update control.

This is stronger evidence of recoverability than a generic “open SDK” claim because the public repository documents both the host API and the glasses-side command path. The glasses-side `asg_client` command reference states that BLE commands and Android debug intents converge on the same command processor.

## Durable release path

The SDK derives its default Mentra Live OTA manifest from the SDK version:

`https://github.com/Mentra-Community/MentraOS/releases/download/bluetooth-sdk-ota/bluetooth-sdk-<sdkVersion>-version.json`

Mentra's release documentation says each published SDK version points to a durable ASG client APK and firmware manifest built for that SDK release. The release workflow treats an existing asset with different bytes as an error and requires a new SDK version for a different compatibility target.

That version-to-manifest mapping materially improves preservation and rollback analysis. It does **not** prove that every firmware component is reproducibly buildable, that every historical manifest will remain hosted forever, or that an owner can bypass all bootloader and signing controls.

## Owner-control implications

The documented SDK supports:

- direct BLE discovery and connection from React Native/Expo, native Android, and native iOS applications;
- explicit control and event handling for capture, microphone state, buttons, touch input, battery, Wi-Fi and streaming features exposed by the connected model;
- owner-supplied webhook destinations for photo and video workflows;
- SDK-driven OTA availability checks and user-approved installation;
- a public glasses-side JSON command reference for Mentra Live;
- deployment without requiring Mentra-hosted cloud infrastructure for the direct host-to-glasses path.

The MentraOS repository is MIT-licensed and describes self-hosting, modification, and cross-device application support. Those platform claims remain distinct from the proprietary hardware, firmware signing, mobile operating-system permissions, and third-party services an individual application may still use.

## Telemetry caveat

The public SDK README documents three PostHog usage events enabled by default. Recorded fields can include the SDK/app version, application identifier, operating-system information, glasses model, and a manufacturing serial used as `glasses_device_id`. The documentation also provides opt-out controls for Expo/React Native, native Android, and native iOS builds.

This means the direct SDK path is not automatically telemetry-free. Owner control is materially strengthened by the documented ability to disable these events, but privacy-sensitive deployments must make that choice explicitly and verify the built application configuration.

## Claim limits

This record verifies published architecture, source, release policy, and vendor statements. It does not independently verify:

- radio reliability, transfer speed, camera quality, battery life, or update success;
- that all supported-glasses features work equally across Android and iOS;
- completeness of source for every binary delivered through the OTA chain;
- continued availability of GitHub-hosted release assets;
- the security of owner-supplied endpoints or third-party applications.

## Primary sources

1. [Mentra Bluetooth SDK README](https://github.com/Mentra-Community/MentraOS/blob/dev/mobile/modules/bluetooth-sdk/README.md)
2. [Bluetooth SDK release and OTA policy](https://github.com/Mentra-Community/MentraOS/blob/dev/mobile/modules/bluetooth-sdk/RELEASING_CI.md)
3. [Mentra Live ASG command API](https://github.com/Mentra-Community/MentraOS/blob/dev/asg_client/docs/ASG_CLIENT_API.md)
4. [Persistent Bluetooth SDK OTA release](https://github.com/Mentra-Community/MentraOS/releases/tag/bluetooth-sdk-ota)
5. [MentraOS repository](https://github.com/Mentra-Community/MentraOS)
6. [Mentra Live product and SDK statements](https://mentraglass.com/live)
