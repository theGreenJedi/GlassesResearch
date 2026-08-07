# Open Hacking Resource Ledger

This ledger collects concrete, public resources that can help owners and researchers understand, repair, interoperate with, or lawfully modify smart-glasses platforms. Inclusion is not an endorsement and does not mean GlassesResearch has reproduced every claim.

## Status key

- **Verified Working** — reproduced by GlassesResearch on an identified device and software environment.
- **Community Confirmed** — multiple independent reports exist, but GlassesResearch has not completed qualifying reproduction.
- **Not Verified Yet** — preserved lead awaiting controlled testing.
- **Disproven** — tested and found not to work under the recorded conditions.
- **Historical** — preserved for research value; not represented as a current working path.

## Active resources

| Platform / model | Resource | Resource type | Status | Why it matters |
|---|---|---|---|---|
| W610 / HeyCyan | [W610 Open-Hacking Dossier](../models/W610/hacking/README.md) | Hands-on research dossier | Verified Working baseline + Not Verified Yet queue | Establishes the current owner-controlled test baseline and the exact promotion rules for future BLE, firmware, recovery, and vendor-app replacement work. |
| W610 / HeyCyan | [W610 Research Portal](../models/W610/resources/RESEARCH_PORTAL.md) | Model-specific research index | Mixed evidence lanes | Canonical intake point for apps, regulatory records, community work, firmware leads, and testing routes. |
| Brilliant Labs Frame family | [Brilliant Labs GitHub organization](https://github.com/brilliantlabsAR) | Source repositories, developer resources, hardware/software projects | Project-primary; Not Verified Yet by GlassesResearch | Provides unusually strong public visibility into an AI-glasses platform and is a priority source for build, firmware, protocol, and hardware research. |
| Mentra-compatible glasses | [MentraOS](https://github.com/Mentra-Community/MentraOS) | Open-source operating system and SDK | Project-primary/community; Not Verified Yet by GlassesResearch | Cross-device application platform with direct relevance to vendor-independent software and portability. |
| Open hardware smart glasses | [Open Source Smart Glasses](https://github.com/Mentra-Community/OpenSourceSmartGlasses) | Mechanical, electrical, firmware, and software project | Project-primary/community; Not Verified Yet by GlassesResearch | Publishes design and implementation material useful for repairability, architecture comparison, and independent builds. |
| Vuzix Z100 | [Vuzix Z100 developer/product entry point](https://www.vuzix.com/products/z100-smart-glasses) | SDK / developer platform lead | Project-primary; Not Verified Yet by GlassesResearch | Candidate for documented APIs, samples, firmware/update research, and host compatibility mapping. |
| Snap Spectacles | [Spectacles developer platform](https://www.spectacles.com/) | SDK and application platform | Project-primary; Not Verified Yet by GlassesResearch | Important standalone AR platform for studying developer access, application portability, update paths, and platform lock-in. |
| XREAL family | [XREAL One](https://www.xreal.com/one/) | Display-platform and compatibility lead | Project-primary; Not Verified Yet by GlassesResearch | Useful for USB-C display behavior, accessories, firmware tooling, and protocol/compatibility research. |
| RayNeo family | [RayNeo AR glasses](https://www.rayneo.com/collections/ar-glasses) | Product-family platform lead | Project-primary; Not Verified Yet by GlassesResearch | Broad device family suitable for mapping host requirements, firmware, accessories, revisions, and possible shared protocols. |
| Rokid family | [Rokid global site](https://global.rokid.com/) | Product and developer ecosystem lead | Project-primary; Not Verified Yet by GlassesResearch | Relevant to Android/XR software, translation, SDKs, firmware tools, and regional application differences. |
| Android XR ecosystem | [Android XR](https://www.android.com/xr/) | Shared OS / SDK layer | Project-primary; Not Verified Yet by GlassesResearch | Potential common software layer across future smart-glasses manufacturers and a key portability target. |

## What to preserve next

Priority order is based on disappearance risk and usefulness to owner control:

1. W610 / HeyCyan APKs, firmware references, BLE captures, flashing notes, recovery procedures, and community repositories.
2. Public source releases, build instructions, hardware files, and licenses from Brilliant Labs and Open Source Smart Glasses.
3. MentraOS releases, compatibility lists, SDK documentation, and example applications.
4. SDKs, firmware tools, manuals, and update/recovery documentation from Vuzix, XREAL, RayNeo, Rokid, and Snap.
5. Regulatory filings, teardowns, PCB imagery, model identifiers, and OEM/rebrand evidence that reveal shared hardware or firmware families.
6. Vendor-cloud dependencies and any lawful, reproducible paths that reduce or eliminate them.

## Verification rule

A resource can be useful without being verified. A **procedure** cannot be called working until it has been reproduced on an identified device with versions, evidence, expected result, and recovery notes recorded.

## Archive-first rule

If a useful public artifact appears fragile or likely to disappear, preserve its metadata immediately: canonical URL, owner, version, retrieval date, license, redistribution status, and hash when a lawful download is made. Organization can follow. Loss cannot be undone.
