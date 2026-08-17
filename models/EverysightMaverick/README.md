# Everysight Maverick AI / AI Pro

**Status:** pre-release / still in development as of 2026-08-17  
**Manufacturer:** Everysight  
**Category:** full-color AR + AI smart glasses  
**Canonical GLS IDs:** not assigned yet; the purchaser-history ledger requires acquisition/delivery evidence

## Model distinction

Everysight currently presents two distinct products:

- **Maverick AI** — the base full-color AR + AI glasses.
- **Maverick AI Pro** — adds native eye tracking through Everysight **GazeIntent™**.

The distinction is manufacturer-documented and should not be collapsed into a single SKU during later catalog promotion.

## Current primary specification snapshot

Everysight's current product/support material states:

- 47 g weight.
- Everysight BEAM™ projection engine with a full-color Sony micro-OLED imager.
- 22° field of view.
- Bluetooth 5.2.
- iOS, Android, and Wear OS compatibility.
- IP55.
- 8+ hours claimed continuous operation.
- forward-facing AI camera.
- multi-microphone array and contextual audio speaker.
- inertial / line-of-sight sensing.
- touch controller and on/off button.
- clear, tinted, transition, and prescription lens options.
- single-vision prescription range planned at launch: SPH -3.0 to +3.0; CYL 0 to -1.0. Progressives are not available at launch.
- Maverick AI Pro adds native eye tracking / GazeIntent™.

Because Everysight explicitly says Maverick AI and AI Pro are still in development, all pre-release specifications remain subject to change.

## Developer surface

Everysight publishes a Maverick AI/AI Pro SDK for Android and iOS. Current documentation exposes HUD rendering, line-of-sight/AR, camera, microphone, inertial sensors, display control, and OTA support. The architecture is wirelessly tethered: a host phone/watch application sends control and rendering commands while the glasses embedded OS controls the hardware and display.

The SDK connection path is controlled. Everysight documents a signed glasses-certificate handshake. Certificate generation requires an Everysight-issued developer/runtime API key and periodic server contact when a certificate is missing or expired. The documentation currently describes a 30-day certificate lifetime.

**Research implication:** a public SDK is meaningful openness, but it is not the same thing as unrestricted owner control or cloud independence.

## Evidence conflict to preserve

Current Everysight material specifies a **22° FOV**. Earlier independent material associated with the product has reported **28°**. GlassesResearch treats this as a temporal/revision conflict: the current manufacturer specification is the current snapshot, while the older value remains evidence about an earlier prototype/specification state rather than being silently deleted.

## User-supplied hands-on lead

A user supplied this video for ingestion:

- https://www.youtube.com/watch?v=pYf1E9316iI

The current research environment could not retrieve a reliable transcript or video frames/audio from that endpoint. No hands-on claim is therefore promoted from the URL alone. The source remains preserved as [EV-0076](../../evidence/EV-0076-Maverick-AI-Pro-user-video-lead.md) for later reproducible review.

## Evidence records

- [EV-0074 — primary product evidence](../../evidence/EV-0074-Maverick-AI-primary-product.md)
- [EV-0075 — SDK and owner-control boundary](../../evidence/EV-0075-Maverick-SDK-owner-control.md)
- [EV-0076 — user-supplied video lead](../../evidence/EV-0076-Maverick-AI-Pro-user-video-lead.md)

## Open questions

- first production shipment date and independently confirmed fulfillment.
- production-unit weight/spec changes relative to current pre-release documentation.
- final AI Pro eye-tracking behavior and calibration on production hardware.
- runtime-key approval policy for third-party applications.
- behavior after certificate expiry with Everysight services unreachable.
- whether core non-SDK functions remain useful without an Everysight account or companion-app path.
- firmware recovery/debug access and any bootloader or direct-device development surface.

Until those questions are resolved, unknown stays unknown.
