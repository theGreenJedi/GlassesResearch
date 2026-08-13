# Chipset and Silicon Genealogy Framework

Smart-glasses products that look unrelated may share processors, display controllers, sensor hubs, radios, or reference designs. GlassesResearch should map these technical relationships without assuming that shared silicon proves shared firmware, OEM ancestry, or equivalent capabilities.

## What to capture

For each device or lineage, record when evidence permits:

- main SoC or application processor;
- companion processor, MCU, DSP, NPU, or sensor hub;
- Bluetooth/Wi-Fi radio or combo chip;
- display controller and display-engine silicon;
- camera-processing components;
- storage and memory architecture when documented;
- power-management components where they materially affect ownership or repair;
- GNSS/cellular silicon where present;
- known reference platforms or development kits;
- firmware/OS family associated with the silicon;
- source evidence and verification date.

## Relationship classes

Keep the following relationships distinct:

- Same exact silicon: the same documented chip or chipset appears in multiple devices.
- Same silicon family: related chips from one vendor family are used, but not necessarily the same part.
- Same reference platform: evidence ties products to the same vendor reference design or development platform.
- Similar architecture: products use comparable architectural patterns, but direct lineage is not established.
- Suspected relationship: circumstantial evidence exists but is not strong enough for a firm connection.

## Evidence rules

Regulatory filings, teardowns, schematics, board photographs, official developer documentation, supplier documentation, and GlassesResearch hands-on inspection can all contribute. Retailer specification sheets alone should not establish a chipset relationship unless independently corroborated.

Do not infer an OEM relationship solely because two products share a common Qualcomm, MediaTek, BES, Actions, JL, Nordic, or other chip. Commodity silicon crosses many unrelated manufacturers.

## Why this matters

Silicon genealogy can explain recurring capabilities and limitations across the ecosystem: camera pipelines, Bluetooth behavior, local AI feasibility, firmware architecture, battery characteristics, display limits, driver reuse, and software portability.

It can also reveal where apparent product diversity is superficial and where similar-looking devices are actually architecturally distinct.

## Output

The eventual silicon map should allow traversal in both directions: device to component and component to devices. Each relationship should carry evidence confidence and source IDs rather than appear as an unsupported graph edge.
