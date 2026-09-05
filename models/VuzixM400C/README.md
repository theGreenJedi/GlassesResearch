# Vuzix M400-C — Research Hub

**Canonical ID:** `GLS-0212`  
**Lineage:** [Vuzix](../../lineages/VUZIX.md)  
**Audit:** [Manufacturer Completeness Wave 02](../../research/investigations/MANUFACTURER_COMPLETENESS_WAVE_02_2026-09-05.md)

M400-C is a materially distinct host-driven member of Vuzix's M-Series. Vuzix introduced it in January 2022, reported initial shipments, and priced the product at $1,199 with broader availability planned for Q2 2022.

## Why it is not simply M400

M400 runs its own Android application environment. M400-C preserves the eyeglass-mounted camera/display concept while moving application compute to a USB-C host. That changes the system boundary directly relevant to GlassesResearch:

- host ownership and compatibility;
- generic versus Vuzix-specific protocol behavior;
- cloud independence;
- application/developer access;
- failure behavior when vendor software disappears;
- serviceability and upgrade path.

M400 scores therefore do not transfer to M400-C.

## Investigation queue

1. Identify supported USB-C video/data modes and whether operation survives without proprietary host software.
2. Map camera, microphone and sensor exposure to the host.
3. Recover manuals, firmware/update paths and regional model numbers.
4. Compare mechanical/electrical modules against M400 hands-on/teardown evidence.
5. Measure owner-control and cloud-independence boundaries independently.

## Primary source

- [Vuzix M400-C introduction](https://ir.vuzix.com/news-events/press-releases/detail/1937/vuzix-introduces-its-new-m400-c-smart-glasses)
