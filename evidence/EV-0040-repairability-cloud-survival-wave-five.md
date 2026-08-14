# EV-0040 — repairability and cloud-survival wave five

Verified: 2026-08-13

## Mentra Live / MentraOS
Primary sources: Mentra Live product/FAQ, MentraOS local-development/cloud documentation.

- Mentra Live says owners can swap in their own lenses through any optician; checkout prescription options are not yet required for optical service.
- Mentra documents offline calls, music and phone audio.
- MentraOS cloud is open source and the official development guide documents running the cloud locally with Docker/local databases and configuring the mobile app's Cloud URL to the developer-operated instance.
- Production-style MiniApps still depend on the MentraOS architecture, authentication and app/cloud plumbing unless the owner substitutes/runs those services.

Interpretation: Mentra Live has unusually strong ordinary-optician serviceability and unusually strong service-survival potential because the cloud control plane itself can be self-hosted. This is stronger evidence than simple SDK openness, but not proof that every bundled first-party function survives a vendor shutdown without configuration work.

## Brilliant Labs Frame
Primary source: Brilliant Frame hardware manual.

- Frame documents two built-in 105 mAh lithium-ion cells (210 mAh total) and a 140 mAh charging-cradle cell.
- Hardware schematics, mechanical files, firmware customization and debug access are public.
- Battery charging/monitoring is documented, but the battery is built in and safety documentation warns against removal.

Interpretation: preservation/documentation access is benchmark-level; battery replacement is not owner-supported. Repairability must be decomposed by component.

## Oakley Meta HSTN
Primary source: Oakley Meta FAQ/product documentation.

- Oakley explicitly states the embedded battery in the glasses and charging case is not replaceable.
- The battery cannot be removed by the end user.
- Oakley lists replacement lenses and prescription configurations, so optical consumables are materially more serviceable than the electronics.
- Oakley documents that normal operation requires a compatible smartphone, wireless internet access, a valid Meta account and the Meta AI app; features can change or be withdrawn.

Interpretation: Oakley Meta combines good lens-level service with poor battery/electronics repairability and high platform/account dependence. This is a useful closed-consumer control against Brilliant/Mentra.

## Repairability subfields reinforced
Track independently:
1. documentation/schematics;
2. firmware/debug access;
3. optical/lens replacement;
4. battery replacement;
5. electronics/module replacement;
6. replacement-parts availability;
7. destructive/non-destructive disassembly;
8. software/cloud survivability.

A product can be excellent in one and poor in another.