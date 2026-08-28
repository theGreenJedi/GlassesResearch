# Nimbo X1 — populated research record

Canonical ID: **GLS-0166**  
Primary/project evidence: [EV-0080](../../evidence/EV-0080-Nimbo-X1-open-platform-claims.md).  
Canonical admission: [2026-08-28 reconciliation](../../models/THE_LIST_RECONCILIATION_2026-08-28_NIMBO_X1.md).

## Identity and lifecycle

**Nimbo X1** is a distinct full-color AR smart-glasses product from Nimbo. As checked 2026-08-22, Nimbo exposes public preorder/campaign surfaces and the Nimbo team states that its Kickstarter is funded. The product therefore crosses GlassesResearch's purchaser-history acquisition threshold and is admitted as **GLS-0166**.

Do not confuse **Nimbo X1** with **NIMO Holo-Optical Glasses**. They are separate projects with separate sites, product identities and acquisition states. Similar naming is not lineage evidence.

## Hardware / display claims

Current Nimbo material claims:

- 49 g weight;
- full-color silicon-carbide waveguide display;
- 30° field of view;
- 2000-nit brightness;
- 32 MP camera;
- 2 GB RAM + 32 GB storage in team AMA answers;
- 640×480 physical display resolution in team AMA answers;
- local media storage and Wi-Fi streaming.

An independent hands-on poster reports possessing a unit and measuring approximately 49 g. That is useful corroboration of physical existence/weight, but the display/camera/performance numbers remain manufacturer/team claims until independently reproduced.

## Software and owner-control claims

The Nimbo team makes unusually strong openness claims:

- AOSP-based operating system;
- most AOSP applications supported;
- no general app-installation restriction claimed;
- open SDK;
- system-level signing access;
- low-level hardware interfaces;
- raw sensor access;
- direct camera + IMU access for custom applications;
- independent App Center;
- standard Bluetooth HID-controller compatibility;
- configurable OpenAI-compatible AI API provider/key path.

These claims make X1 a **priority owner-control investigation**, not an automatically high-scoring open platform. GlassesResearch still needs the actual SDK, licenses, developer documentation and owner-side privilege tests.

## Prescription and serviceability boundary

The team states that prescription optics are bonded to the waveguide and cannot be casually swapped by the owner/local optician; replacement requires factory return because incorrect disassembly could damage the SiC component.

This is an important tradeoff: the platform may prove software-open while remaining optically/service mechanically dependent on the manufacturer. Openness, repairability and prescription lifecycle must be scored independently.

## Cloud-independence boundary

The team says the application can accept user-selected API providers/keys using an OpenAI-compatible interface. If delivered as described, this could materially improve AI-provider portability.

It does **not** yet prove:
- complete local/offline AI;
- service survival without Nimbo infrastructure;
- open firmware/recovery images;
- unrestricted bootloader access;
- independence of activation, updates or App Center services.

Cloud Independence remains unscored until those boundaries are tested.

## Comparison / Finder publication boundary

Canonical admission permits Nimbo X1 to appear on model-comparison and Finder surfaces, but only fields supported by preserved evidence should be populated. Project-claimed specifications may be displayed only with their claim provenance intact; unknown capability states must remain unknown rather than being inferred from marketing copy or absence of evidence.

No Report Card score is assigned by the admission. In particular, the project's open-SDK, system-signing, sensor-access and user-selected-AI-endpoint statements are **not** converted into verified Openness, Owner Control, Hackability or Cloud Independence scores until artifacts or owner-side testing substantiate them.

## Research priorities

1. Preserve the SDK, documentation, sample code and license terms as soon as they are publicly obtainable.
2. Verify ordinary-user access to system signing, camera, IMU and raw sensor streams.
3. Determine bootloader/recovery/firmware-update architecture.
4. Test user-selected AI endpoint configuration and behavior when Nimbo services are blocked.
5. Measure display brightness/FOV/color, thermal behavior and realistic battery runtime.
6. Confirm purchase/backer fulfillment and lifecycle state.
7. Verify prescription ranges, factory replacement cost/turnaround and whether any local optical service path exists.
8. Map the claimed in-house optical/manufacturing architecture to actual corporate and supply-chain entities.

## Current scoring rule

No Report Card score is assigned in this record. The evidence is strong enough for canonical admission and comparison-surface discoverability, but not yet strong enough to convert project openness claims into owner-control scores without inspectable artifacts or reproduced behavior.
