# EV-0041 — HTC VIVE Eagle function-level service survival

Verified: 2026-08-14
Source class: vendor product/support primary
Confidence: confirmed for documented functions; shutdown behavior remains prospective
Scope: GLS-0025 — HTC VIVE Eagle

## Sources
- Product overview: https://www.vive.com/us/product/vive-eagle/overview/
- Product specifications: https://www.vive.com/us/product/vive-eagle/spec/
- VIVE launch explanation: https://blog.vive.com/us/introducing-vive-eagle-smart-glasses-built-for-everyday-life/
- Support — use without VIVE Connect: https://www.vive.com/sea/support/vive-eagle/category_howto/can-i-use-vive-eagle-without-vive-connect.html
- Support — VIVE Connect role: https://www.vive.com/hk/support/vive-eagle-en/category_howto/about-vive-connect-app.html
- Support — media storage: https://www.vive.com/hk/support/vive-eagle-en/category_howto/where-is-my-media-saved.html

## Function-by-function result

| Function | Phone/app required? | Internet/cloud required? | Survival finding |
|---|---|---|---|
| Button photo/video capture | No during capture | No | Works without opening VIVE Connect. |
| On-glasses media storage | No | No | Photos/videos remain in 32 GB onboard storage until import. |
| Media import/export | Yes, VIVE Connect | No cloud requirement stated | App is the documented bridge to phone; owners should export to the phone photo library because app deletion/cache clearing deletes its gallery copy. |
| Basic device commands | Not for the documented local commands | No | HTC says VIVE AI can take a photo, play music, or launch an app completely offline. |
| Advanced VIVE AI | Yes, glasses connected to VIVE Connect | Yes, phone internet | HTC support explicitly requires both the companion connection and internet for VIVE AI tasks. |
| Third-party reasoning | Yes | Yes | Gemini and OpenAI GPT are selectable service providers; provider choice is not local model execution. |
| Notes files | App-managed | Service-dependent for transcription/summaries | Files are described as AES-256 encrypted and locally stored, but AI Notes processing/allowance remains a service layer. |
| Setup / button behavior / chat and memo management | Yes | Feature-dependent | VIVE Connect is the supported setup and management control plane. |

## Interpretation

VIVE Eagle is **partially durable**, not cloud-independent. Its camera and local-storage appliance survives loss of internet and can capture without the app open. A narrower set of commands is documented as offline. The defining generative-AI experience, however, requires VIVE Connect plus an internet-connected phone and third-party/VIVE services.

Local encrypted storage is a privacy and capture-survival advantage, but it does not remove companion-app risk: documented media import and management still depend on VIVE Connect. Owners seeking preservation should export media to the phone's ordinary photo library and preserve compatible app installers.

This evidence supports a split assessment:
- capture/storage: Survival level **A/B**;
- basic offline commands/audio: **B**;
- advanced assistant, translation, transcription and summaries: **C/D**;
- whole-device usefulness after service loss: **B/C**, because camera/audio utility survives while advertised AI capability degrades substantially.

## Remaining tests

First-run setup and account requirements, Bluetooth audio behavior after app sign-out, whether local files can be accessed over a standard filesystem/USB path, exact offline-command list, regional AI-provider restrictions, firmware-update delivery, and behavior with a preserved app after backend shutdown.
