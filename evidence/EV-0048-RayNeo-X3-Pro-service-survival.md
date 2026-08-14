# EV-0048 — RayNeo X3 Pro local/developer and service-survival boundary

**Verified:** 2026-08-14  
**Evidence class:** Current first-party RayNeo product, launch and technical explanation pages  
**Scope:** RayNeo X3 Pro; Air-series host displays are architecturally separate

## Architecture

X3 Pro is a standalone Android-based AI+AR platform with Snapdragon AR1 Gen 1, 4 GB RAM, 32 GB storage, Wi-Fi, Bluetooth, cameras, sensors, battery and RayNeo AIOS. RayNeo states that a phone is useful for setup, hotspot access and companion features, but does not need to remain connected for all operation.

That makes X3 Pro more locally capable than a phone-only peripheral, but its defining Gemini experience remains a hybrid local/cloud system.

## Function matrix

| Function | Local/device evidence | Service dependency | Survival assessment |
|---|---|---|---|
| Core UI and controls | RayNeo AIOS, local menu/UI rendering, voice wake-up and temple controls | Firmware remains vendor-controlled | Local residue |
| Camera and storage | 12 MP camera, spatial camera and 32 GB storage | Exact export/account restrictions not documented | Strong hardware residue |
| Selected Android apps | Android-based virtual environment; some apps may be manually installed or use developer tools | App compatibility, accounts and online services vary | Recoverable application value |
| Creator Mode | Unity ARDK / Android ARDK with 6DoF and SLAM | SDK/tool availability and privilege limits remain | Meaningful supported local-development path |
| Teleprompter/music/camera tools | Built-in tools are documented | Content/provider dependencies vary | Plausible local value |
| Voice wake and basic scene detection | RayNeo states these are local | Delivered model/firmware boundary is not fully enumerated | Local |
| Gemini Live / complex visual AI | Local chip captures, parses and renders, then sends compressed voice/scene data to cloud models when needed | Google Gemini and network service | Cloud-dependent reasoning |
| Translation | Fourteen-language real-time translation is advertised | Current product material associates it with AI services; no offline pack is documented | Treat as service-dependent |
| Navigation, news and meeting summaries | Integrated through AIOS | Maps, current data, ASR/LLM and service providers | Service-dependent |

## Creator Mode does not equal open system ownership

Creator Mode materially improves survival because developers can build spatial applications against documented Unity/Android ARDK surfaces and deploy selected applications. It does not establish:

- open-source RayNeo AIOS or firmware;
- bootloader unlock;
- unrestricted camera/sensor privileges;
- owner-replaceable Gemini endpoints;
- account-free first activation;
- offline installation/update of the ARDK stack; or
- recovery images and rollback.

## Correct label

**Substantial standalone/local application residue with a supported developer path; defining Gemini reasoning and connected services remain cloud-dependent.**

This is a stronger survival posture than closed companion-only AI glasses, but weaker than an open firmware/hardware platform.

## Required validation

1. Complete setup, then operate with phone Bluetooth disabled and no network.
2. Inventory built-in tools, camera/export, UI, settings and stored applications.
3. Build a minimal Creator Mode application using only local assets.
4. Install and launch it with RayNeo services blocked.
5. Test manual APK installation and document signing/permission limits.
6. Test camera, spatial camera, microphone, SLAM and storage access from Creator Mode.
7. Identify which voice wake, scene detection and translation functions continue offline.
8. Preserve SDK, ARDK, application, firmware and recovery artifacts where licensing permits.

## Primary sources

- [RayNeo X3 Pro product page](https://www.rayneo.com/products/x3-pro-ai-display-glasses)
- [RayNeo X3 Pro launch page](https://www.rayneo.com/pages/x3-pro-launch)
- [RayNeo explanation of local edge processing and Gemini hybrid AI](https://www.rayneo.com/blogs/news/how-smart-glasses-ai-assists-your-daily-life)
- [RayNeo developer portal](https://open.rayneo.com/)

## Confidence

High for standalone hardware, Android-based environment, Creator Mode, Unity/Android ARDK support, local voice wake/basic scene detection and Gemini cloud reasoning. Medium for exact offline built-in-tool survival and developer privilege boundaries until physical and SDK-level tests are completed.
