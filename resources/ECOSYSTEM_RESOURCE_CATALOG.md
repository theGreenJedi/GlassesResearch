# Smart-Glasses Ecosystem Resource Catalog

This catalog is the cross-model intake layer for software, firmware, SDKs, protocols, hardware files, developer documentation, community projects, and fragile research leads.

It is deliberately broader than the current W610 hands-on work. Inclusion means that a resource is relevant enough to preserve and investigate; it does **not** mean that GlassesResearch has tested it, endorses it, or has verified every claim it contains.

## Evidence and preservation labels

- `project-primary` — maintained by the project or manufacturer responsible for the platform.
- `community` — maintained by an identifiable third party or community.
- `commercial` — seller, marketplace, or marketing source.
- `hands-on` — independently exercised by this repository's maintainers.
- `linked` — canonical URL recorded, but no local preservation copy exists.
- `metadata-preserved` — provenance, retrieval date, license, and hash information recorded.
- `artifact-preserved` — a lawful redistributable copy is stored or attached to a durable release.
- `restricted` — redistribution is not currently justified; preserve metadata and acquisition route only.

## Active resource catalog

| Ecosystem / models | Resource | Type | Evidence lane | Preservation state | Why it matters | Next action |
|---|---|---|---|---|---|---|
| W610 / HeyCyan ecosystem | [W610 Research Portal](../models/W610/resources/RESEARCH_PORTAL.md) | Annotated research index | hands-on + mixed sourced leads | Repository-native | Canonical entry point for W610 apps, regulatory records, community work, firmware leads, and testing routes | Continue converting external links into provenance-rich records |
| Brilliant Labs Frame and related devices | [Brilliant Labs GitHub organization](https://github.com/brilliantlabsAR) | Public source repositories | project-primary | linked | Hardware and software repositories provide unusually strong visibility into an AI-glasses platform | Inventory repositories, licenses, releases, hardware files, and protocol documentation |
| Mentra-compatible glasses | [MentraOS](https://github.com/Mentra-Community/MentraOS) | Open-source operating system and SDK | project-primary/community | linked | Cross-device application platform and SDK with compatibility implications beyond one glasses model | Record supported devices, build instructions, API boundaries, releases, and license |
| Open hardware smart glasses | [Open Source Smart Glasses](https://github.com/Mentra-Community/OpenSourceSmartGlasses) | Mechanical, electrical, and software project | project-primary/community | linked | Publishes design files and implementation details that can inform repairability, architecture comparison, and independent builds | Preserve release metadata, BOM, CAD, PCB, firmware, and license details |
| Vuzix Z100 | [Vuzix Z100 product and developer entry point](https://www.vuzix.com/products/z100-smart-glasses) | Product and developer documentation lead | project-primary | linked | Monocular display platform with SDK and cross-platform compatibility research value | Locate canonical SDK docs, sample code, firmware/update procedure, and supported-host matrix |
| Snap Spectacles | [Spectacles developer platform](https://www.spectacles.com/) | Device and developer platform | project-primary | linked | Standalone AR platform with a distinct OS, SDK, interaction model, and developer ecosystem | Map SDK, emulator, publishing path, hardware generations, and archival availability |
| XREAL One and related display glasses | [XREAL One](https://www.xreal.com/one/) | Product/platform source | project-primary | linked | Important tethered-display family for USB-C video, accessories, tracking, and compatibility research | Locate developer docs, firmware tools, USB behavior, accessory protocols, and revision history |
| RayNeo Air family | [RayNeo AR glasses collection](https://www.rayneo.com/collections/ar-glasses) | Product-family source | project-primary | linked | Large tethered-display family useful for cross-model compatibility and naming/revision analysis | Split family into canonical models and record firmware, accessories, and host requirements |
| RayNeo X3 Pro | [RayNeo platform](https://www.rayneo.com/) | Standalone AI/AR platform lead | project-primary | linked | Android-derived standalone architecture warrants software, developer, and update-path investigation | Identify SDK, OS lineage, application model, regional variants, and recovery path |
| Meta / Ray-Ban Meta / Oakley Meta | [Meta AI glasses](https://www.meta.com/ai-glasses/) | Product and platform source | project-primary | linked | Widely deployed camera/audio ecosystem; valuable baseline for privacy, update, app, and capability comparison | Map generations, companion app, firmware/update behavior, public APIs, and regulatory filings |
| Even Realities G1 / G2 | [Even Realities](https://www.evenrealities.com/) | Product/platform source | project-primary | linked | Display-first architecture and third-party platform compatibility create a useful contrast with camera/audio glasses | Locate developer interfaces, firmware/update mechanisms, optical architecture sources, and compatibility evidence |
| Solos AirGo family | [Solos](https://solosglasses.com/) | Product-family and integration source | project-primary | linked | Multi-assistant and modular product-family claims make it relevant to vendor-independence research | Separate generations, identify app/API surfaces, and verify replaceable-module claims |
| Rokid glasses ecosystem | [Rokid global site](https://global.rokid.com/) | Product and developer ecosystem lead | project-primary | linked | Translation, display, Android/XR, and SDK workflows span several relevant smart-glasses categories | Inventory models, SDKs, firmware tools, regional applications, and host dependencies |
| Android XR partner ecosystem | [Android XR](https://www.android.com/xr/) | Operating-system and partner-platform source | project-primary | linked | Shared platform layer may connect multiple future manufacturers and models | Track SDK releases, supported device classes, partner hardware, and application portability |
| Amazon Echo Frames | [Echo Frames](https://www.amazon.com/echo-frames/) | Product/history source | project-primary/commercial | linked | Useful historical audio-glasses case study involving cloud assistant dependence, generations, and discontinuation risk | Preserve generation history, app requirements, update status, manuals, and end-of-life evidence |

## Artifact-preservation record

Before storing or mirroring an external artifact, add a record containing:

```yaml
resource_id: stable-kebab-case-id
models:
  - canonical-model-id
resource_type: firmware | apk | sdk | source | packet-capture | manual | cad | pcb | tool | procedure | community-post | other
source_url: https://example.invalid/resource
source_owner: person-or-organization
retrieved_utc: 2026-08-05T00:00:00Z
version_or_revision: unknown
sha256: unknown
license: unknown
redistribution: allowed | restricted | unknown
preservation_state: linked | metadata-preserved | artifact-preserved | restricted
claim_lane: hands-on | project-primary | community | commercial | inference
notes: >-
  Explain what the artifact is, why it matters, and any uncertainty.
```

## Intake rules

1. Preserve the canonical source URL even when an artifact is mirrored.
2. Never treat a repository fork, marketplace listing, or repost as independent confirmation of an upstream claim.
3. Record hashes for downloaded files before analysis or modification.
4. Keep originals immutable; store derived or patched files separately with explicit provenance.
5. Do not redistribute files merely because they are downloadable. Record license and redistribution status first.
6. Promote model-specific findings into `models/<canonical-model-id>/` when enough substantive evidence exists.
7. Record dead links and replacements rather than silently deleting historical routes.
8. Prefer real resource entries over empty category pages.

## Priority preservation queue

1. W610/HeyCyan APKs, firmware, protocol notes, flashing/recovery procedures, and community repositories.
2. Public hardware and software releases from Brilliant Labs and the Open Source Smart Glasses project.
3. MentraOS releases, device compatibility records, SDK documentation, and examples.
4. SDKs, firmware tools, manuals, and compatibility documentation for Vuzix, XREAL, RayNeo, Rokid, and Snap.
5. Manuals, app requirements, regulatory filings, and end-of-life records for discontinued or cloud-dependent glasses.
6. OEM/rebrand evidence connecting low-cost camera glasses to shared hardware, applications, firmware, or BLE behavior.

## Relationship to model chapters

This catalog answers **where useful ecosystem resources are and what must be preserved**. Model chapters answer **what those resources establish about a particular device**. A resource may appear here before a dedicated model chapter exists; that is intentional and allows the repository to scale without creating empty scaffolding.
