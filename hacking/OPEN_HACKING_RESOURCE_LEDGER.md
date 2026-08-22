---
title: "Smart-Glasses Open Development Resource Ledger"
description: "Direct smart-glasses SDK, API, BLE protocol, firmware, open-hardware, and developer resources with primary/community evidence boundaries."
---

# Open Development Resource Ledger

Last reviewed: **2026-08-21**

This page lists concrete public resources that owners, developers, and researchers can actually use. It does not contain placeholder categories or generic instructions to search elsewhere.

## Evidence lanes

- **Project-primary** — maintained by the manufacturer, platform operator, or project responsible for the interface or code.
- **Community** — independent implementation or reverse engineering. It can establish that public code and documented experiments exist; individual behavior remains community-sourced until separately reproduced.
- **Historical / archived** — preserved because it documents an earlier implementation, compatibility path, or project lineage that may no longer be the active upstream.

A public repository proves that code or documentation was published. It does **not** prove that every feature works on every firmware or hardware revision.

## W610 / HeyCyan

- [HeyCyanSmartGlassesSDK](https://github.com/ebowwa/HeyCyanSmartGlassesSDK) — **Community** — cross-platform community SDK and BLE implementation for HeyCyan-compatible glasses, including W610 references.
- [CyanBridge / Alternative HeyCyan App and SDK](https://github.com/FerSaiyan/Alternative-HeyCyan-App-and-SDK) — **Community** — alternative Android companion stack with published releases and vendor-independent assistant work.
- [CyanBridge releases](https://github.com/FerSaiyan/Alternative-HeyCyan-App-and-SDK/releases) — **Community** — versioned Android release artifacts and release notes.
- [FCC ID 2BNVK-W610](https://fccid.io/2BNVK-W610) — W610 equipment-authorization record with labels and regulatory exhibits.
- [W610 Research Portal](../models/W610/resources/RESEARCH_PORTAL.md) — GlassesResearch index of the concrete W610 sources collected so far.

## Brilliant Labs Frame

- [Frame SDK](https://docs.brilliant.xyz/frame/frame-sdk/) — **Project-primary** — official development documentation covering Python, Flutter, Lua, direct BLE development, and firmware customization.
- [Frame hardware manual](https://docs.brilliant.xyz/frame/hardware/) — **Project-primary** — official block diagrams, schematics, MCU/FPGA details, camera, microphone, battery, mechanical data, prescription clip, and firmware-customization information.
- [Brilliant Labs documentation](https://docs.brilliant.xyz/) — **Project-primary** — official documentation hub for Frame, Halo, Monocle, APIs, firmware and community projects.
- [Brilliant Labs GitHub organization](https://github.com/brilliantlabsAR) — **Project-primary** — public source repositories and SDKs.
- [Frame firmware codebase](https://github.com/brilliantlabsAR/frame-codebase) — **Project-primary** — public Frame firmware/source repository referenced by the official hardware documentation.

## MentraOS and open smart-glasses hardware

- [MentraOS](https://github.com/Mentra-Community/MentraOS) — **Project-primary / community** — MIT-licensed smart-glasses operating system and SDK that handles pairing, hardware access, application runtime, and cross-device compatibility.
- [MentraOS releases](https://github.com/Mentra-Community/MentraOS/releases) — **Project-primary / community** — versioned builds, APKs, release notes, and published checksums.
- [Mentra Community](https://github.com/Mentra-Community) — organization index for MentraOS, example applications, compatibility work, and related open-source projects.
- [Open Source Smart Glasses](https://github.com/Mentra-Community/OpenSourceSmartGlasses) — **Project-primary / community** — MIT-licensed mechanical, electrical, firmware, and software files for an open smart-glasses design.
- [MentraOS Display Example App](https://github.com/Mentra-Community/MentraOS-Display-Example-App) — concrete example application for developing display experiences against MentraOS.

## Even Realities G1 and G2

These projects are **independent community work**, not Even Realities documentation. They are useful because they expose executable or packet-level evidence about what owners can reach over BLE without treating those observations as official API guarantees.

- [`even_glasses`](https://github.com/emingenc/even_glasses) — **Community; G1; GPL-3.0** — Python BLE-control package for Even Realities G1. The public repository identifies scanning/connection and owner-side control as its purpose; use its implementation and examples as community evidence rather than a manufacturer contract.
- [`even-g2-protocol`](https://github.com/i-soxi/even-g2-protocol) — **Community; G2** — active packet/protocol research documenting G2 BLE services, authentication, transport structure, protobuf payloads and working text-display experiments. The project currently reports working BLE connection/authentication and teleprompter/calendar paths, with notifications partial and navigation/AI still under research.
- [MentraOS](https://github.com/Mentra-Community/MentraOS) — **Community / cross-device runtime** — includes Even-device integration in a broader smart-glasses application layer. It is useful as converging implementation evidence but is not independent confirmation merely because it consumes the same upstream community findings.

Forks and mirrors of the same reverse-engineering project are preservation or development branches, **not separate confirmations** of a protocol claim.

## Vuzix Z100

- [Z100 documentation](https://support.vuzix.com/docs/z100-documentation) — **Project-primary** — official Z100 user manual and documentation index.
- [Vuzix Ultralite SDK overview](https://support.vuzix.com/docs/overview-28) — **Project-primary** — official description of display, connection, tap, battery and application-control capabilities exposed to developers.
- [Android SDK](https://support.vuzix.com/docs/sdk-for-android) — **Project-primary** — official Android integration documentation, including requirements and links to Vuzix's SDK library and sample application.
- [Z100 connection guide](https://support.vuzix.com/docs/how-to-connect-to-the-z100) — **Project-primary** — official pairing behavior and Vuzix Connect application requirements.

## Snap Spectacles

- [Spectacles developer documentation](https://developers.snap.com/spectacles/home) — **Project-primary** — official entry point for Spectacles development.
- [Spectacles features overview](https://developers.snap.com/spectacles/about-spectacles-features/overview) — **Project-primary** — official APIs and modules for camera frames, gestures, HTTP access, world queries and controller integration.
- [Spectacles compatibility list](https://developers.snap.com/spectacles/about-spectacles-features/compatibility-list) — **Project-primary** — feature-by-feature API compatibility for Spectacles.
- [Spectacles asset and sample library](https://developers.snap.com/spectacles/about-spectacles-features/asset-library) — **Project-primary** — official packages plus Snap's current public sample repositories.
- [Spectacles samples](https://github.com/specs-devs/samples) — public sample code recommended by Snap's developer documentation.

## XREAL

- [XREAL SDK](https://docs.xreal.com/) — **Project-primary** — official SDK documentation using Unity XR Plugin, XR Interaction Toolkit and AR Foundation.
- [XREAL One specifications](https://tutorials.xreal.com/docs/glasses/one-series/spec/) — **Project-primary** — official display, audio and hardware specifications for the One family.
- [XREAL One connection documentation](https://tutorials.xreal.com/docs/glasses/one-series/first-use/connect-device/) — **Project-primary** — official USB-C DisplayPort/power behavior and host-connection guidance.
- [XREAL One FAQ](https://tutorials.xreal.com/docs/glasses/one-series/faq/) — **Project-primary** — official firmware/update and operational documentation.

## RayNeo

- [OpenClaw for RayNeo X3 Pro](https://github.com/RayNeo-AI-2025/OpenClaw) — public X3 Pro application with source, build instructions, gesture control, speech/LLM integration, and a multi-part RayNeo X3 development guide.
- [OpenClaw development guide](https://github.com/RayNeo-AI-2025/OpenClaw/blob/main/README_EN.md) — documents Mercury SDK integration, dual-eye rendering, temple input, camera APIs, IMU/head tracking, ADB debugging and build requirements.
- [RayNeo Air 3S Pro OpenVR](https://github.com/verncat/RayNeo-Air-3S-Pro-OpenVR) — **Community** — C/C++ work toward host-side interaction and OpenVR support for RayNeo Air glasses.

## Rokid

- [Rokid SDK documentation](https://x-docs.rokid.com/docs/en/terminal-sdk/) — **Project-primary** — official unified SDK index with quick start, glasses-side SDK, phone-side SDK, capability scenarios, samples and API references.
- [Rokid Glasses SDK](https://x-docs.rokid.com/docs/en/terminal-sdk/glasses/) — **Project-primary** — official device-side SDK for media capture, voice, recognition, messaging, device state, Bluetooth and P2P on supported Rokid glasses.

## Project Aria research tooling

Project Aria is a **Meta research platform**, not a Ray-Ban Meta consumer-glasses SDK. Its unusually deep public tooling belongs here, but Aria capabilities must never be transferred to Ray-Ban Meta or other Meta eyewear without model-specific evidence.

- [Project Aria Tools](https://github.com/facebookresearch/projectaria_tools) — **Project-primary / research; Apache-2.0** — open C++/Python tooling for Project Aria data. The current project supports both Aria Gen 1 and Gen 2 data and exposes APIs/utilities for sensor data, calibration, visualization and machine-perception outputs.
- [Project Aria documentation](https://facebookresearch.github.io/projectaria_tools/) — **Project-primary / research** — current documentation, installation paths, tutorials, VRS data access and machine-perception workflows.

This is evidence for the **Aria research ecosystem**, not proof of unrestricted firmware access or an application SDK for unrelated Meta glasses.

## Android XR

- [Android XR developer hub](https://developer.android.com/develop/xr/get-started) — **Project-primary** — official Android XR SDK entry point covering headsets, wired XR glasses, audio glasses and display glasses.
- [Android XR OpenXR development](https://developer.android.com/develop/xr/openxr) — **Project-primary** — official OpenXR 1.1 development path and supported XR capabilities.
- [Android XR virtual glasses devices](https://developer.android.com/develop/xr/jetpack-xr-sdk/run/create-avds/xr-headsets-glasses) — **Project-primary** — official Android Studio emulator support for XR glasses.
- [Android XR application distribution](https://developer.android.com/develop/xr/package-and-distribute) — **Project-primary** — current Google Play distribution rules and device-class distinctions.

## Rule

A public resource belongs here only when we can name it, link it directly, and explain what usable information it contains. Empty categories and “look elsewhere” instructions do not belong on this page.

Official developer documentation is primary evidence for intended interfaces. Independent code and reverse engineering are evidence for observed or implemented access. They answer different questions and are not silently promoted into the same confidence lane.
