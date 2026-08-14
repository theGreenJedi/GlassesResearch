# Device Serviceability Framework

Long-term ownership depends on whether a product can be maintained after normal wear or component failure.

For each model, record documented construction methods, battery service path, replaceable modules, lens service path, charging-interface design, internal component documentation, spare-part availability, donor-part compatibility when demonstrated, repair documentation, and whether reassembly requires manufacturer-specific calibration or software.

Prefer evidence-backed descriptions over a single serviceability score when information is sparse. Distinguish ordinary service, specialist service, manufacturer-only service, community-demonstrated service, and unknown.

Do not assume that visually similar lineage members use interchangeable parts. Demonstrated compatibility and suspected common design are separate claims.

Serviceability findings should inform Owner Control, Hardware, Value, and discontinued-device survivability.

## Evidence-backed serviceability records

| Model | Optical service | Battery service | Other repair path | Current classification | Evidence |
|---|---|---|---|---|---|
| HTC VIVE Eagle | Qualified eye-care professional may replace lenses; HTC states -8D to +4D support | Unknown | Spare magnetic charging cable is regionally advertised; internal parts and repair documentation remain unverified | **Specialist-serviceable optics; remainder unknown** | [EV-0042](../evidence/EV-0042-HTC-VIVE-Eagle-optical-serviceability.md) |
| W610 / HeyCyan variants | Removable/prescription-compatible claims exist but require exact-variant verification | Common 270 mAh Li-poly specification and software telemetry are documented as claims; installed cell and replacement path unverified | Magnetic charging observed; internal parts, sealing and repair instructions unknown | **Battery observable; service path unknown** | [EV-0043](../evidence/EV-0043-W610-battery-evidence-and-verification.md) |

A positive result in one column must not be generalized to the whole device. VIVE Eagle's documented lens path, for example, improves optical durability but does not establish replaceable batteries or owner-serviceable electronics.
