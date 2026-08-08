# Developer Resources and Vendor Independence

Concrete resources for developing, repairing, understanding, and extending smart-glasses platforms.

## Start with the resources

- [Open Development Resource Ledger](OPEN_HACKING_RESOURCE_LEDGER.md) — direct SDKs, source repositories, developer documentation, protocol resources, samples, and open-hardware projects across W610/HeyCyan, Brilliant Labs, MentraOS, Vuzix, Snap, XREAL, RayNeo, Rokid, and Android XR.
- [W610 Research Portal](../models/W610/resources/RESEARCH_PORTAL.md) — direct W610/HeyCyan SDK, alternative-app, FCC, rebrand, and supplier sources.
- [Research Library](../evidence/README.md) — machine-readable evidence records with stable identifiers.
- [Manuals, Firmware & Technical Files](../artifacts/README.md) — identified technical artifacts and preservation records.

## Platforms with usable public development material

### W610 / HeyCyan

Community developers have published a [HeyCyanSmartGlassesSDK](https://github.com/ebowwa/HeyCyanSmartGlassesSDK) and the [CyanBridge alternative companion stack](https://github.com/FerSaiyan/Alternative-HeyCyan-App-and-SDK). The [W610 FCC record](https://fccid.io/2BNVK-W610) adds regulatory identity and hardware exhibits. GlassesResearch also maintains hands-on observations in the [W610 dossier](../models/W610/hacking/README.md).

### Brilliant Labs Frame

Brilliant Labs publishes an unusually open development stack. The [Frame SDK](https://docs.brilliant.xyz/frame/frame-sdk/) covers Python, Flutter, Lua, direct BLE development, and firmware customization. The [hardware manual](https://docs.brilliant.xyz/frame/hardware/) publishes architecture, schematics, camera, microphone, battery, FPGA/MCU and mechanical information. Public source is available through the [Brilliant Labs GitHub organization](https://github.com/brilliantlabsAR) and [Frame firmware codebase](https://github.com/brilliantlabsAR/frame-codebase).

### MentraOS and open hardware

[MentraOS](https://github.com/Mentra-Community/MentraOS) is an MIT-licensed smart-glasses operating system and SDK with application runtime, pairing, hardware access and cross-device compatibility. Versioned builds and checksums are published in [MentraOS releases](https://github.com/Mentra-Community/MentraOS/releases). The same community publishes [Open Source Smart Glasses](https://github.com/Mentra-Community/OpenSourceSmartGlasses), including mechanical, electrical, firmware and software material.

### Vuzix Z100

Vuzix publishes [Z100 documentation](https://support.vuzix.com/docs/z100-documentation), an [Ultralite SDK overview](https://support.vuzix.com/docs/overview-28), and an [Android SDK route](https://support.vuzix.com/docs/sdk-for-android). The SDK exposes connection state, display content, power/display state, tap events, battery and charger state.

### Snap Spectacles

Snap publishes a full [Spectacles developer portal](https://developers.snap.com/spectacles/home), a [feature/API overview](https://developers.snap.com/spectacles/about-spectacles-features/overview), [compatibility list](https://developers.snap.com/spectacles/about-spectacles-features/compatibility-list), [asset library](https://developers.snap.com/spectacles/about-spectacles-features/asset-library), and public [sample code](https://github.com/specs-devs/samples).

### XREAL

XREAL publishes its [SDK documentation](https://docs.xreal.com/) along with [One-family specifications](https://tutorials.xreal.com/docs/glasses/one-series/spec/), [host connection documentation](https://tutorials.xreal.com/docs/glasses/one-series/first-use/connect-device/), and [firmware/operation FAQ](https://tutorials.xreal.com/docs/glasses/one-series/faq/).

### RayNeo

RayNeo's public [OpenClaw project for X3 Pro](https://github.com/RayNeo-AI-2025/OpenClaw) includes source, build instructions, gesture control, speech/LLM integration, and a detailed X3 development guide. Community work also includes [RayNeo Air 3S Pro OpenVR](https://github.com/verncat/RayNeo-Air-3S-Pro-OpenVR).

### Rokid

Rokid publishes a unified [terminal SDK](https://x-docs.rokid.com/docs/en/terminal-sdk/) and a specific [glasses-side SDK](https://x-docs.rokid.com/docs/en/terminal-sdk/glasses/) covering media capture, voice, recognition, messaging, device state, Bluetooth and P2P on supported models.

### Solos AirGo

Solos publishes a [developer SDK program](https://solosglasses.com/pages/developers) for AirGo V 1/2 camera models and AirGo 3/A5 audio models. The vendor documents BLE control, Wi-Fi data on V2, microphones, sensors, touch, camera access, webhooks/RTMP endpoints, and iOS/Android application wrappers.

### Android XR

Google's [Android XR developer hub](https://developer.android.com/develop/xr/get-started) covers headsets, wired XR glasses, audio glasses and display glasses. Google also publishes [OpenXR guidance](https://developer.android.com/develop/xr/openxr), [virtual XR-glasses devices for Android Studio](https://developer.android.com/develop/xr/jetpack-xr-sdk/run/create-avds/xr-headsets-glasses), and [distribution guidance](https://developer.android.com/develop/xr/package-and-distribute).

## Safety boundary

Research only devices and services you own or are authorized to inspect. Do not publish credentials, private user traffic, unlawfully distributed proprietary files, or instructions intended to compromise another person's device or account.

## Publication rule

A procedure is presented as working only when the evidence supports that specific procedure on an identified device/software environment. Public resource pages themselves should contain useful resources, not queues of things we hope to find later.
