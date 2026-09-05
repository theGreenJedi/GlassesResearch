# Rokid Air Pro — GLS-0182

Rokid Air Pro is the camera-equipped enterprise/cultural-tourism sibling of Rokid Air, released as a separately named product in 2021.

**Technology lineage:** [Rokid](../../lineages/ROKID.md)  
**Catalog state:** canonical — `GLS-0182`  
**Evidence state:** first-party chronology + first-party developer documentation + surviving commercial/enterprise availability; hands-on verification pending

## Why Air Pro is a separate model

Rokid's corporate history names **Rokid Air** and **Rokid Air Pro** as separate 2021 releases. More importantly, Rokid's developer forum documents a material hardware boundary:

- Air Pro includes cameras; Air does not.
- Air supports adjustable myopia correction that Air Pro does not.
- Rokid's UXR SDK explicitly supports both Air and Air Pro as separate targets.

Those differences alter sensing, privacy, AR capability, optical serviceability, and owner-control questions. Air Pro must therefore not inherit the Air report card or be treated as an Air accessory package.

## Architecture

Air Pro remains fundamentally host-connected eyewear rather than the standalone all-in-one architecture of Rokid Glass / Glass 2. Surviving product material describes a binocular Micro-OLED display, USB-C host connection, IMU/sensing, directional audio and wearer-view camera capability.

Generation-specific specifications still need primary-manual recovery before being promoted to canonical facts. Surviving distributor pages may preserve useful leads, but GlassesResearch should not silently elevate reseller copy to first-party evidence.

## Investigation queue

1. Recover the original first-party Air Pro product page/manual and regulatory model number.
2. Separate camera, display, IMU and microphone capabilities from ordinary Air.
3. Map UXR SDK APIs that depend on the Air Pro camera.
4. Test whether camera access is local/host-controlled or mediated by Rokid software.
5. Establish exact host compatibility, USB transport, firmware/update path and service-loss behavior.
6. Build a generation-specific report card rather than inheriting GLS-0092 scores.

## Primary sources

- [Rokid corporate milestones](https://www.rokid.com/en-US/about)
- [Rokid developer forum — UXR / Air versus Air Pro](https://forum.rokid.com/post/detail/365)

## Related GlassesResearch resources

- [Rokid lineage](../../lineages/ROKID.md)
- [Rokid historical audit](../../research/investigations/ROKID_HISTORICAL_AUDIT_2026-09-05.md)
- [Rokid populated research record](../../research/populated/ROKID.md)
