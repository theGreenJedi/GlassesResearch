# Rokid Max Pro — GLS-0183

Rokid Max Pro is the eyewear component of Rokid AR Studio. It is a distinct 6DoF-capable glasses model, not merely a Rokid Max sold with Station Pro.

**Technology lineage:** [Rokid](../../lineages/ROKID.md)  
**Catalog state:** canonical — `GLS-0183`  
**Evidence state:** current first-party developer/product material + launch/procurement evidence; hands-on verification pending

## Identity boundary

Rokid's AR Studio material explicitly identifies two separate hardware components:

- **Rokid Max Pro** glasses;
- **Rokid Station Pro** compute host.

Contemporaneous launch reporting also priced those two components separately. Max Pro therefore earns its own eyewear identity while AR Studio remains a system/bundle identity.

Rokid's current security-support table lists Max Pro separately with hardware model **RA202**.

## Manufacturer-documented hardware

Rokid's AR Studio developer site currently documents Max Pro-specific behavior including:

- approximately 76 g eyewear weight;
- Sony Micro-OLED display architecture;
- approximately 50° field of view;
- 1920 × 1200 display specification;
- up to 120 Hz display capability, with 90 Hz stated when connected to Station Pro;
- approximately 500-nit default eye brightness and up to 600-nit peak claim;
- 108% sRGB claim;
- 100,000:1 contrast claim;
- 6DoF head-controlled spatial interaction;
- camera-assisted spatial positioning / single-camera spatial interaction described by Rokid.

These claims must remain attached to Max Pro and not be copied onto Max or Max 2.

## Software / ownership boundary

The spatial-computing behavior of AR Studio depends materially on Station Pro and YodaOS-Master. The glasses and host therefore need separate evidence records even when they are evaluated together as a system. Max Pro should be tested both as eyewear hardware and as one half of AR Studio.

## Investigation queue

1. Preserve Max Pro manual, firmware identifiers, USB behavior and regulatory model evidence.
2. Separate on-glasses sensors from Station Pro sensors/cameras.
3. Verify whether Max Pro can function as a conventional DP display without Station Pro and what modes survive.
4. Map 6DoF camera/IMU processing boundaries and data flow.
5. Investigate developer access, ADB/sideloading, firmware/update path and recoverability.
6. Build a generation-specific report card; do not inherit Max or Max 2 scores.

## Primary sources

- [Rokid AR Studio](https://arstudio.rokid.com/)
- [Rokid AR Studio developer site](https://studio-dev.rokid.com/)
- [Rokid security center](https://global.rokid.com/pages/security-center)

## Related GlassesResearch resources

- [Rokid lineage](../../lineages/ROKID.md)
- [Rokid historical audit](../../research/investigations/ROKID_HISTORICAL_AUDIT_2026-09-05.md)
- [Rokid populated research record](../../research/populated/ROKID.md)
