# EV-0067 — Xiaomi AI Glasses service-survival source boundary

**Status:** Source boundary completed at conservative confidence; hands-on China-region testing required  
**Model:** GLS-0024 Xiaomi AI Glasses  
**Reviewed:** 2026-08-15

## Question

Which functions are demonstrably local to the glasses, and which AI, app, account and regional dependencies remain unresolved?

## Finding

Xiaomi's launch material establishes a self-contained camera/audio platform with Snapdragon AR1, a separate low-power Xiaomi Vela OS chip, onboard storage, physical capture controls, livestreaming, translation, transcription and multimodal AI. That architecture supports a meaningful local residue: camera/audio hardware, onboard storage and low-power device operation exist independently of any claim about cloud AI.

The surviving public primary packet does **not** establish:

- account-free first activation;
- operation without the companion application;
- standard USB or filesystem media access;
- which named AI functions run on-device versus on the phone or Xiaomi services;
- offline translation or transcription;
- regional operation outside the supported China service environment;
- sideloading, public SDK, bootloader or recovery-image access.

GlassesResearch therefore does not label the headline multimodal features local. The device has local capture/storage hardware; the processing and service boundary for recognition, translation, transcription, payments and livestreaming remains connected/unknown unless an exact function is independently demonstrated.

## Function-by-function matrix

| Function | Source-supported state | Evidence boundary |
|---|---|---|
| Photo/video capture | On-device camera and physical controls established | Offline capture is architecturally plausible but still needs endpoint-blocked testing |
| Audio playback/calls | On-device speakers/microphones established | Account-free Bluetooth behavior not documented in current packet |
| Onboard storage | Local storage established | Capacity and owner-visible file-access path require preservation |
| Low-power standby/control | Separate Vela OS low-power chip established | Does not prove AI inference runs locally |
| Multimodal recognition | Advertised | Processing location and endpoint dependency unknown |
| Translation/transcription | Advertised | Offline language packs or local inference not established |
| Livestreaming | Advertised connected function | Necessarily requires network/service destination |
| Companion setup/media management | Dedicated ecosystem implied by product workflow | Exact app, account, region and sign-out behavior not sufficiently preserved |
| Firmware/update/recovery | Vendor-managed architecture | Owner-downloadable firmware/recovery image not located |
| Third-party development | No broad public SDK established | Absence of a located SDK is not proof no private partner interface exists |

## Lifecycle classification

**Connected AI appliance with local capture/storage residue.** This is not a claim that the glasses become useless without Xiaomi services, nor a claim that their defining AI survives. It is the narrowest conclusion supported by the primary packet.

## Scoring effect

Cloud Independence remains 4.5, Owner Control 3.5 and Openness 3.0. Strong hardware and local storage prevent a lower appliance-only score; unresolved activation, processing, media-access and recovery paths prevent a higher ownership score.

## Required hands-on follow-up

Using a supported-region phone/account and a clean second phone, record first activation, account requirement, app package/version, permissions, Bluetooth/Wi-Fi behavior, offline button capture, onboard retention, file export, translation/transcription with endpoints blocked, sign-out, region mismatch, firmware delivery and factory-reset recovery. Preserve the installer and lawful firmware artifacts before testing shutdown scenarios.

## Sources

- [Xiaomi global launch record](https://www.mi.com/global/discover/article?id=5172)
- [Xiaomi HyperAI processing context](https://www.mi.com/global/brand/ai/xiaomi-hyperai)
