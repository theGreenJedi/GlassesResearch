# W610 Hardware

This section records the physical device baseline, controls, indicators, optics, internal architecture, and component evidence for the received W610-class glasses.

## Owned-device records

- [Physical overview](physical-overview.md) — construction, fit, optics, and mission assessment
- [Controls and indicators](controls-and-indicators.md) — confirmed button behavior, startup response, and open tests

## Current observations

- Electronics are concentrated in the right temple; the left temple is visibly slimmer.
- The right temple has two physical controls. The rear control functions as the power control in current testing.
- An indicator LED is located near the right hinge.
- A power-button press produces an audible tone and a brief LED flash.
- The device includes a camera, microphones, speakers, and magnetic charging contacts.
- The frame is tight on the owner’s larger head, and the supplied tinted lenses do not provide premium sunglass optics.
- Goodway's exact-model supplier page claims removable/customizable prescription lenses only in an OEM/ODM context. [EV-0068](../../../evidence/EV-0068-W610-optical-serviceability-boundary.md) preserves the boundary: no ordinary-optician path, correction range, replacement supply or successful conversion is yet established.
- Retail and OEM sources repeatedly claim an 8 MP camera and 270 mAh lithium-polymer battery. [EV-0043](../../../evidence/EV-0043-W610-battery-evidence-and-verification.md) records the claim cluster, HeyCyan low-power thresholds, community battery telemetry surface and a non-destructive test protocol; capacity and replaceability remain unverified on the owned unit.

## Component leads

- [CMP-0001 — JL7018F](../../../glossary/components/CMP-0001-jl7018f.md)
- [CMP-0002 — Allwinner V821L2](../../../glossary/components/CMP-0002-allwinner-v821l2.md)

Neither component is yet confirmed from PCB markings on the received unit.

## Priority measurements

1. Photograph and measure both temples, controls, charging contacts, lens opening, and hinge geometry.
2. Execute the EV-0043 battery protocol: record charge input, fixed-workload discharge, telemetry, the 15%/10% feature cutoffs, temperature and repeatability.
3. Preserve package, manual, QR-code, and label markings.
4. Identify non-destructive access points before any teardown.
5. Execute the EV-0068 optical protocol: document retention, measure A/B/DBL/effective diameter/curve/thickness/bevel, preserve a trace/template, and obtain a recorded independent-optician assessment before attempting conversion.

## Evidence rules

Record date, device revision, tools, uncertainty, and photographs. Distinguish direct observation from vendor claims and inferred architecture.
