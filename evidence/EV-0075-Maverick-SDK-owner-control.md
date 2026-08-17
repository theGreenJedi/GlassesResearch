# EV-0075 — Maverick SDK and owner-control boundary

**Evidence state:** vendor-primary  
**Last verified:** 2026-08-17  
**Platforms:** Everysight Maverick AI; Everysight Maverick AI Pro

## Sources

- Developer overview: https://www.everysight.com/pages/developer
- SDK getting started: https://everysight.github.io/maverick-ai-docs/getting-started/start-development/
- API keys and certificates: https://everysight.github.io/maverick-ai-docs/getting-started/api-key/

## Supported claims

Everysight publishes an Android/iOS SDK for Maverick AI/AI Pro. Current documentation exposes HUD rendering, line-of-sight/AR, camera, microphone, inertial sensors, display control, and OTA functionality, with additional capabilities listed on the roadmap. Everysight describes the glasses as wirelessly tethered to a smartphone or watch: the host application sends control/rendering commands while the glasses embedded OS controls hardware and display behavior.

SDK connectivity is not unrestricted. Everysight documents a certificate handshake in which a signed glasses certificate must validate before an application can connect. Certificate generation requires an Everysight-issued developer or runtime API key and contacts an Everysight server when a new certificate is required. The generated certificate is persisted and currently has a 30-day expiration according to the documentation.

## Research consequence

The public SDK is strong evidence of a supported developer surface. It is not evidence of full cloud independence or unrestricted owner control. Those dimensions must remain separate in GlassesResearch evaluations.
