# SDK / API Compatibility Matrix

This matrix tracks what smart-glasses manufacturers and projects expose to developers. A product having an SDK is not enough; the useful question is which device capabilities are documented, which host platforms are supported, how much the interface depends on a vendor service, and whether a portability layer is official or community-maintained.

## Official and vendor-exposed device SDKs

| Device / family | Official SDK / API | Host platforms | Display | Camera | Audio | Sensors | Transport | Custom AI integration | Assessment |
|---|---|---|---|---|---|---|---|---|---|
| Brilliant Labs Frame | Published developer documentation and project repositories | Official tooling plus developer-defined workflows | Supported | Supported | Product/workflow dependent | Broad developer-oriented hardware surface | Documented development path | High | Strong reference platform for owner-directed development. |
| Brilliant Labs Halo | Vendor describes SDK and open-source development path | Verify current release tooling | Supported by product design | Product-defined optical sensing | Product-defined | Product-defined | Developer-oriented; verify current docs | High in principle | Score delivered and documented capability rather than announcement language. |
| Vuzix Z100 | Official Android and iOS SDKs | Android, iOS | Supported for text, images and animations | N/A: no camera listed | Host-phone dependent | Device interaction through supported SDK | Documented BLE peripheral architecture | High on host side | Strong example of a documented display peripheral. |
| Solos AirGo family | Official developer material for supported generations | Android / iOS, generation-dependent | Model-dependent | Supported on camera-equipped AirGo V models, generation-dependent | Supported on audio models | Generation-dependent | BLE and generation-dependent Wi-Fi paths | Moderate to high | Exact generation must be recorded because capabilities differ. |
| XREAL One family | Developer ecosystem exists | Host/platform dependent | Core capability | Accessory/model dependent | Host/model dependent | Spatial features model-dependent | Host/display pathways plus vendor tooling | Moderate | Basic display usefulness can be more durable than proprietary spatial features. |
| Ray-Ban Meta / Meta AI glasses | Consumer platform; not a general-purpose hardware SDK comparable to open development platforms | Meta consumer ecosystem | No HUD in current camera/audio category | Consumer feature access | Consumer feature access | Limited third-party hardware surface | Vendor-controlled | Low | Strong consumer product, limited general hardware programmability. |
| [Even Realities G2](https://hub.evenrealities.com/) | Even Hub is a live first-party app platform with official SDK/documentation, developer console, local testing workflow, and publishing path | Web-oriented app development through the Even platform; exact runtime/host boundaries should be recorded per SDK release | Supported through Even Hub APIs | N/A for G2 outward-facing camera | Device/platform dependent; do not infer speaker output | Platform-exposed inputs only | Vendor-mediated through Even App / Even Hub | Moderate to high within published API surface | Third-party development is now established for G2. Keep G1 separate unless Even explicitly documents Hub support there. |
| Even Realities G1 | Public integrations exist | Mobile ecosystem | Supported | Generation-dependent | Generation-dependent | Product-dependent | Vendor-controlled unless documented otherwise | Moderate / uncertain | Do not inherit G2 Even Hub support onto G1 without generation-specific evidence. |
| W610 / HeyCyan variants | Community CyanBridge project plus bundled vendor SDK artifacts; not an independently open official SDK | Android is the active community path; iOS vendor-demo shell also present | No confirmed HUD on hands-on W610 | Community path exposes camera/media commands through vendor library; direct independent control pending | Audio/recording transfer documented; full direct developer access pending | Device information and battery surfaces claimed by community code; hands-on inventory pending | BLE control plus Wi-Fi Direct/local HTTP media transfer documented by community source | Moderate potential, unscored pending owned-unit validation | EV-0044 establishes a concrete owner-directed companion path, but it presently retains vendor-binary dependencies and uncertain licensing. |

## Community and cross-vendor portability layers

These projects are tracked separately from manufacturer SDKs. Their existence can materially improve developer portability, but a community adapter does **not** prove that every underlying device capability is open, vendor-independent, or hardware-validated.

| Project | Scope | Current documented support | Host/tooling | Dependency boundary | Evidence lane / assessment |
|---|---|---|---|---|---|
| [xg.glass](https://github.com/hkust-spark/xg-glass-sdk) | Community universal smart-glasses API intended to reduce per-vendor integration work | Project documentation currently lists adapters/workflows for Rokid, Meta Ray-Ban, Brilliant Labs Frame, RayNeo, Even Realities G1, INMO, Omi, plus a simulator; per-device validation status varies | Android, iOS, CLI; current project docs specify Android minSdk 28, minSdk 29 for Meta and the RayNeo host, iOS 16+, and Python CLI tooling | Some adapters still depend on vendor components; RayNeo support, for example, requires vendor AARs obtained from RayNeo developer resources | **Community software evidence.** High-interest portability layer, but capability claims must remain device-specific and should not be promoted to official SDK status. |
| MentraOS-compatible glasses | Open-source cross-device application platform | Depends on current MentraOS compatibility list | Platform-dependent | Cross-device abstraction may still depend on device/vendor interfaces underneath | **Project/open-source evidence.** Useful portability layer across compatible hardware; verify each device generation independently. |

## Access levels

GlassesResearch uses four labels when documenting a capability:

1. **Documented direct control** — the SDK explicitly allows an application to use the capability.
2. **Documented structured feature** — the SDK exposes a defined operation with meaningful but bounded control.
3. **Vendor feature only** — the manufacturer's own application can use the capability, but third-party access is not documented.
4. **Not verified** — the hardware may exist, but a developer path has not been established.

This prevents common category mistakes such as assuming that a camera automatically implies third-party camera access, or that an AI feature automatically implies user-selectable AI.

## Minimum evidence record

For each SDK/API claim, record the exact device and hardware revision, SDK version, documentation source, supported host operating systems, sample application where available, account requirements, license, registration or approval requirements, offline behavior, and the exact documented capabilities.

For cross-vendor layers, also record which adapter implementation was inspected, whether real hardware was tested, and which vendor binaries, accounts, app stores, AARs/frameworks, cloud services, or proprietary transports remain underneath the abstraction.

## Report-card relationship

This matrix supports the **Openness**, **Owner Control**, **Cloud Independence**, and **Hackability** grades. Grades should change when stronger documentation or hands-on evidence changes the underlying facts. Community portability is useful evidence about practical development paths, but it does not by itself change a manufacturer's openness or owner-control grade.

For the W610 boundary, see [EV-0044 — community protocol and owner-access surface](../evidence/EV-0044-W610-community-protocol-and-owner-access.md).
