# EV-0043 — W610 battery claims, telemetry and verification boundary

Verified: 2026-08-14
Source classes: OEM/ODM commercial claim; retailer commercial claim; HeyCyan documentation; community SDK repository; project hands-on baseline
Confidence: moderate that 270 mAh is the common W610 specification; unconfirmed for the project's received unit
Scope: W610 / HeyCyan retail variants

## Sources

- Goodway W610 OEM/ODM listing: https://www.goodwaytechs.com/goodway-ai-smart-glasses-with-8mp-camera-real-time-translation-ip65-waterproof-42g-lightweight-w610.html
- TVC-Mall W610 listing: https://m.tvcmall.com/details/w610-heycyan-app-smart-glasses-photo-video-recording-ai-translation-8mp-camera-wifi-bluetooth-compatible-glasses-anti-blue-light-lenses-sku6812002712a.html
- Alibaba W610 listing: https://www.alibaba.com/product-detail/W610-Smart-Glasses-with-Camera-and_1601550648419.html
- HeyCyan feature documentation — low-battery behavior: https://heycyan.net/docs/user-manual/feature-list
- HeyCyan compatible-glasses marketing: https://heycyan.net/pricing
- Community SDK repository: https://github.com/ebowwa/HeyCyanSmartGlassesSDK
- Project hardware baseline: [W610 hardware](../models/W610/hardware/README.md)

## Established findings

| Field | Finding | Evidence class | Confidence |
|---|---|---|---|
| Advertised capacity | 270 mAh | Repeated OEM/retailer commercial claim | Moderate for the W610 specification; not verified on the owned unit |
| Advertised chemistry | High-density polymer lithium / lithium-polymer wording | Commercial claim | Moderate |
| Charging interface | Magnetic contacts/cable | Hands-on observation plus commercial claim | High for interface type |
| Advertised runtime | Up to 12 hours music and 7+ days standby | Retail commercial claim | Low until a controlled workload is tested |
| HeyCyan ecosystem runtime | 8–9 hours active use | App-ecosystem marketing, not proven W610-specific | Low for this exact hardware |
| Low-battery policy | Below 15% disables photo/video/audio recording; below 10% suspends multimedia including music | HeyCyan documentation | Moderate for compatible current firmware; must be reproduced on the exact device |
| Battery telemetry | Community SDK exposes battery percentage and charging state | Community-source code/API claim | Moderate; command and response require independent capture/reproduction |
| Replaceability | No documented owner or manufacturer battery-replacement path located | Negative research result | Unknown, not “non-replaceable” |

## What this does not prove

Repeated 270 mAh listings may share the same upstream specification text. They do not independently confirm the cell installed in the project's unit or every W610-branded revision. Runtime figures are “up to” claims with no disclosed volume, capture rate, Wi-Fi use, AI/app use, temperature, battery age or cutoff criteria. A Bluetooth percentage is controller telemetry, not a capacity measurement.

No teardown photo, cell label, charging trace, measured watt-hours, cycle-life specification, replacement part number, connector type or safe opening procedure has yet been established for the owned device.

## Non-destructive verification protocol

1. Record exact device/revision identifiers, firmware, app/SDK version and ambient temperature.
2. Charge to the device-reported 100%; record input voltage/current with an inline magnetic-cable power meter if electrically compatible.
3. Leave connected for a defined taper period; record total input Wh while explicitly noting conversion loss means input Wh is not cell Wh.
4. Run separate repeatable workloads:
   - powered-on idle;
   - Bluetooth audio at fixed phone and glasses volume;
   - periodic still capture;
   - continuous video at a fixed resolution;
   - media transfer over Wi-Fi.
5. Log battery percentage and charging state at fixed intervals through the preserved protocol/API path.
6. Reproduce the documented 15% and 10% feature cutoffs without deep-discharge cycling.
7. Repeat at least three times; report median runtime and spread rather than a single best run.
8. Stop on swelling, unusual heat, odor, charging instability or enclosure deformation.

## Destructive verification gate

Do not open the temple solely to confirm a marketing capacity. Teardown should occur only after external imaging and fastener/seam mapping, baseline data preservation, a recovery plan, and acceptance that adhesive, flex cables, weather sealing and the cell may be damaged. If opened, photograph the cell label before moving it; record dimensions, markings, polarity, connector or weld method, protection PCB and adhesive placement. Never puncture, bend, short or reuse a visibly damaged lithium-polymer pouch.

## Ownership conclusion

The battery is currently **observable but not serviceable**: software surfaces appear able to report percentage/charge state, while actual capacity and replacement access remain unverified. The common 270 mAh claim is useful as a test hypothesis, not yet a measured fact. This distinction protects future rebrand and revision work from inheriting an unsupported specification.
