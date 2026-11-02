---
title: "Smart-Glasses Open Development Resource Ledger"
description: "Direct smart-glasses SDK, API, BLE protocol, firmware, open-hardware, and developer resources with primary/community evidence boundaries."
---

# Open Development Resource Ledger

Last reviewed: **2026-09-25**

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

## Brilliant Labs Frame and Halo

- [Frame SDK](https://docs.brilliant.xyz/frame/frame-sdk/) — **Project-primary** — official development documentation covering Python, Flutter, Lua, direct BLE development, and firmware customization.
- [Frame hardware manual](https://docs.brilliant.xyz/frame/hardware/) — **Project-primary** — official block diagrams, schematics, MCU/FPGA details, camera, microphone, battery, mechanical data, prescription clip, and firmware-customization information.
- [Brilliant Labs documentation](https://docs.brilliant.xyz/) — **Project-primary** — official documentation hub for Frame, Halo, Monocle, APIs, firmware and community projects.
- [Brilliant Labs GitHub organization](https://github.com/brilliantlabsAR) — **Project-primary** — public source repositories and SDKs.
- [Frame firmware codebase](https://github.com/brilliantlabsAR/frame-codebase) — **Project-primary** — public Frame firmware/source repository referenced by the official hardware documentation.
- [Halo firmware](https://github.com/brilliantlabsAR/halo-firmware) — **Project-primary; mixed licenses** — Brilliant Labs' public Zephyr-based Halo firmware, including a Lua on-device runtime, BLE protocol documentation, [build/OTA flashing guide](https://github.com/brilliantlabsAR/halo-firmware/blob/main/applications/halo/FLASHING.md), and MCUboot test-boot/auto-revert behavior. [Firmware release 0.8.23](https://github.com/brilliantlabsAR/halo-firmware/releases/tag/0.8.23) was published **2026-10-27**. The maintainer documents owner-built OTA firmware as supported; GlassesResearch has not independently flashed Halo. **License boundary:** Halo-specific code is generally Apache-2.0, but Alif SDK and vendored components have separate terms; the entire repository is **not** uniformly Apache-2.0.

## MentraOS and open smart-glasses hardware

- [MentraOS](https://github.com/Mentra-Community/MentraOS) — **Project-primary / community** — MIT-licensed smart-glasses operating system and SDK that handles pairing, hardware access, application runtime, and cross-device compatibility.
- [MentraOS releases](https://github.com/Mentra-Community/MentraOS/releases) — **Project-primary / community** — versioned builds, APKs, release notes, and published checksums.
- [Mentra Community](https://github.com/Mentra-Community) — organization index for MentraOS, example applications, compatibility work, and related open-source projects.
- [Open Source Smart Glasses](https://github.com/Mentra-Community/OpenSourceSmartGlasses) — **Project-primary / community** — MIT-licensed mechanical, electrical, firmware, and software files for an open smart-glasses design.
- [MentraOS Display Example App](https://github.com/Mentra-Community/MentraOS-Display-Example-App) — concrete example application for developing display experiences against MentraOS.

## Independent local-first and Linux research platforms

- [OpenSQZ Glass / OpenGlass](https://github.com/OpenSQZ/OpenGlass) — **Research-project primary; prototype** — ESP32-S3 wearable camera/microphone sensing with nearby-host local multimodal inference; includes editable frame CAD, BOM, build guide, firmware, and experimental Rokid capture adapter. The [ACL 2026 demonstration paper](https://aclanthology.org/2026.acl-demo.82/) documents the research architecture. This is **not** evidence of on-glasses inference or a ready-to-buy product. [Source snapshot, 2026-09-30](https://github.com/OpenSQZ/OpenGlass/tree/e0221443ef9547b8402251d8be0ea492ec964734).
- [OpenSource-Ai-Glasses / OSAIG](https://github.com/Iam5tillLearning/OpenSource-Ai-Glasses) — **Project-primary; early-stage** — Apache-2.0 RV1106B embedded-Linux glasses software, SDK, host-build guides, camera/RTSP, BLE text and optional display integration; [v0.7.0 release](https://github.com/Iam5tillLearning/OpenSource-Ai-Glasses/releases/tag/v0.7.0) dates to 2026-05-08. The maintainer says the open scope is **primarily system software and application stack**, not a guarantee that every hardware element is open. Firmware v0.6.x/v0.7.x is restricted to reference hardware made after 2026-01-01; older hardware needs an older image. No GlassesResearch hardware reproduction. [Source snapshot, 2026-10-22](https://github.com/Iam5tillLearning/OpenSource-Ai-Glasses/tree/758d4d1ebf59927bae267dc6a98919844126a76b).

## Raven Prism / RavenOS

- [Raven Framework](https://github.com/RavenResonance/raven-framework) — **Manufacturer-primary; source-available, proprietary (NOT open source)** — Python/PySide6 gaze-first UI/API framework and desktop simulator for Raven Prism. Its [LICENSE](https://github.com/RavenResonance/raven-framework/blob/main/LICENSE) explicitly permits installing/running the **unmodified** framework and building apps against public APIs, but forbids modification, redistribution, sublicensing and derivative works without written permission. Do not conflate public source, Linux/SSH device access or a permissive application ecosystem with an open-source framework. [2026-10-30 v1.0.7 license clarification](https://github.com/RavenResonance/raven-framework/commit/b0efac742ed0ec6c9e76e1c52868ebd39afd531f).
- [Raven Starter Project](https://github.com/RavenResonance/raven-starter-project) — **Manufacturer-primary; SDK preview** — runnable starter examples, Python 3.10+ setup and simulator instructions; mouse input simulates gaze and clicks simulate blink/dwell. A successful desktop simulation does not establish physical-device performance or app deployment.
- [DOOMed Prism](https://github.com/RBraga01/DOOMed-Prism) — **Community implementation; partial external device report** — gaze/IPC and shared-memory Qt compositor proof-of-concept. Maintainer reports passing Windows simulator and ARM64 CI tests; physical-Prism operation is **reported by Raven staff**, not independently reproduced by the project maintainer or GlassesResearch. On-device headless-engine display behavior and full input validation remain open. [Public developer discussion](https://www.reddit.com/r/augmentedreality/comments/1wgyxow/doom_running_on_actual_raven_prism_smart_glasses/).
- [Raven Prism October 29 preorder announcement](https://www.prnewswire.com/news-releases/raven-resonance-announces-raven-prism-the-worlds-first-ambient-computer-is-officially-available-for-pre-orders-302923690.html) — **Manufacturer announcement; not delivery verification** — $49 refundable deposit and *expected* January 2027 first shipments, with Linux-based standalone ARM64 processing, gaze control, waveguide display and hot-swappable Raven Wings claimed. [Avegant partner announcement](https://avegant.com/raven-prism-launch/) independently establishes Avegant's participation as a display supplier, not finished-device battery life, shipping, or privacy performance.

## Even Realities G1 and G2

These projects are **independent community work**, not Even Realities documentation. They are useful because they expose executable or packet-level evidence about what owners can reach over BLE without treating those observations as official API guarantees.

- [`even_glasses`](https://github.com/emingenc/even_glasses) — **Community; G1; GPL-3.0** — Python BLE-control package for Even Realities G1. The public repository identifies scanning/connection and owner-side control as its purpose; use its implementation and examples as community evidence rather than a manufacturer contract.
- [`even-g2-protocol`](https://github.com/i-soxi/even-g2-protocol) — **Community; G2** — active packet/protocol research documenting G2 BLE services, authentication, transport structure, protobuf payloads and working text-display experiments. The project currently reports working BLE connection/authentication and teleprompter/calendar paths, with notifications partial and navigation/AI still under research.
- [Even Realities WebFlasher](https://github.com/AM-Guru/evenRealities-webflasher) — **Community; G2/R1; MIT** — browser-based case/temple inspection, local backups, and guarded **official-firmware** update/reinstall paths; [public owner/developer discussion](https://www.reddit.com/r/EvenRealities/comments/1vmz7gs/were_open_sourcing_part_of_our_even_realities/). The project's own README explicitly says **no dead-temple recovery**, and that experimental charging-case write/bank activation has **not** been physically validated on sacrificial hardware. Do not present this as an official Even tool, a universally safe recovery route, or proof of hardware repairability. [Source snapshot, 2026-10-09](https://github.com/AM-Guru/evenRealities-webflasher/tree/2fcdb888facfe9c56672cbe2a3da741b44033c44).
- [MentraOS](https://github.com/Mentra-Community/MentraOS) — **Community / cross-device runtime** — includes Even-device integration in a broader smart-glasses application layer. It is useful as converging implementation evidence but is not independent confirmation merely because it consumes the same upstream community findings.

Forks and mirrors of the same reverse-engineering project are preservation or development branches, **not separate confirmations** of a protocol claim.

## Meizu MYVU / Star Air (XGA010C)

- [Meizu MYVU Android SDK](https://github.com/Panny777/Meizu-Myvu-SDK) — **Community; unofficial; MIT** — reverse-engineered XGA010C Android SDK for pairing, lens UI, teleprompter, notifications, navigation and assistant integration; includes [packet-level protocol documentation](https://github.com/Panny777/Meizu-Myvu-SDK/blob/main/PROTOCOL.md) describing BLE-first bonding and a session-specific classic-Bluetooth RFCOMM relay. These are author-reported implementation findings, **not** a manufacturer API or independent GlassesResearch reproduction.
- [Meizu MYVU Client](https://github.com/Panny777/Meizu-Myvu-Client) — **Community; unofficial** — Android client plus Python research reference for the same XGA010C family. Both repositories derive from the same research effort and **must not be counted as independent confirmations**. See the [existing GlassesResearch evidence note](../research/investigations/COMMUNITY_MYVU_XGA010C_PANNY777_2026-09-06.md) for attribution, limitations and replication plan.

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
- [Rokid Nexus](https://github.com/Anezium/Rokid-Nexus) — **Community** — owner/developer hub for display-equipped Rokid Glasses. Its architecture keeps a persistent glasses-side hub while extending capabilities through ordinary Android APK plugins on the phone; the public project exposes HUD, camera-question, speech/AI, notification and calendar integrations and supports selectable AI providers/self-hosted endpoints. Treat compatibility and behavior as community evidence until independently reproduced.
- [Rokid Live Studio](https://github.com/Anezium/Rokid-Live-Studio) — **Community** — phone-hosted live-media project demonstrating glasses camera/microphone transport over Wi-Fi Direct while preview, encoding and streaming remain on the phone. Useful for transport and host-boundary investigation; not independent confirmation of every Nexus claim merely because the projects share an author.
- [aimindseye / rokid-ai-glasses](https://github.com/aimindseye/rokid-ai-glasses) — **Community research** — evidence-labeled investigation of the display-free RV203/Style family. Public work reports qualified RSA-protected USB ADB access with Developer Mode enabled, maps phone/cloud/glasses responsibilities, and investigates AI/media paths. Findings remain community-attributed until GlassesResearch reproduction.
- [GlassesResearch: aimindseye Community Research profile](../docs/community-research/aimindseye-rokid-ai-glasses.md) — GR evidence-boundary summary and investigation link.

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
