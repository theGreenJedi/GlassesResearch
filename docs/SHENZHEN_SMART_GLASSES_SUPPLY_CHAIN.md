---
title: "Who Actually Makes These Glasses? Mapping the Shenzhen Smart-Glasses Platform Ecosystem"
description: "A living investigation into the silicon vendors, solution houses, ODMs, factories, app operators, brands, and resellers behind recurring smart-glasses platforms and rebrands."
---

# Who Actually Makes These Glasses?

## Mapping the Shenzhen smart-glasses platform ecosystem

Last reviewed: **2026-08-22**

A commercial name on a smart-glasses listing often does not answer the most useful provenance question: **who actually designed, can modify, and manufactures the underlying platform?**

Across Alibaba, Amazon, direct OEM sites, and retail rebrands, apparently different products repeatedly share model numbers, chipsets, camera claims, battery sizes, companion applications, button layouts, firmware behavior, and mechanical details. This research stream maps those relationships without converting resemblance into unsupported manufacturer claims.

The goal is not to expose a single hidden factory. The goal is to distinguish the layers that can all be described loosely as a “manufacturer” in commercial material:

```text
silicon / reference platform
        ↓
solution house / design authority
        ↓
ODM / mechanical integration / tooling
        ↓
SMT / assembly / test factory
        ↓
software / app / cloud operator
        ↓
brand / importer / commercial OEM contact
        ↓
marketplace reseller
```

One company may occupy several layers. Several companies may share one layer. Until evidence establishes a relationship, GlassesResearch keeps the roles separate.

## Why this matters

Knowing the real platform lineage changes how a device should be researched.

- Firmware or protocol work can apply across rebrands that share a platform.
- A seller's “customization” claim does not establish that the seller controls the PCB, firmware, molds, or camera placement.
- The same model number can be sold by unrelated companies without proving a common final-assembly factory.
- The same companion application can span multiple hardware factories.
- A common chipset can produce many unrelated products because chip vendors publish reference designs and development kits.
- Buyers and developers can avoid treating marketing-company names as verified design or manufacturing provenance.

This investigation therefore tracks **design authority, manufacturing responsibility, software control, and retail identity as different facts**.

## Current high-value lead: the Allwinner V821 / V881 ecosystem

### Allwinner — confirmed silicon and reference-platform layer

Allwinner's own V821 documentation identifies the V821 family as a highly integrated low-power vision SoC with camera interfaces, ISP/video processing, Wi-Fi, audio, storage interfaces, and compact 9 mm-class packaging. Allwinner's developer ecosystem also publishes a V821 AI-glasses development board and hardware documentation. These are primary sources for the chip and reference-development environment; they do **not** identify the factory behind any particular retail W610/W630-class product.

Primary references:

- [Allwinner V821 product page](https://www.allwinnertech.com/index.php?c=product&id=136)
- [Allwinner V821 developer documentation](https://docs.aw-ol.com/docs/soc/v821/)
- [Allwinner V821 AI-glasses development board](https://www.aw-ol.com/solutions/57)
- [Allwinner V821 series mass-production announcement](https://www.aw-ol.com/news/162)

### Shenzhen Qingcheng Wireless Technology — strong solution-house / design-authority lead

Industry coverage of an Allwinner AI-glasses ecosystem event reports that **Qingcheng Wireless general manager Huang Lianghui presented a “V821 Complete Glasses Solution” developed jointly by Qingcheng Wireless and Allwinner**. This materially advances Qingcheng Wireless beyond a generic marketplace-seller lead: it is direct evidence that the company participates in complete smart-glasses solution development around V821.

The evidence still does **not** prove that Qingcheng Wireless designed or manufactures every W610, W630, or HeyCyan-compatible device using a V821-family chip.

Event references:

- [EEWORLD coverage of the Allwinner “Smart Eyes” AI-glasses event](https://en.eeworld.com.cn/mp/XSY/a399875.jspx)
- [Electronic Enthusiast / Elecfans coverage of the same event](https://www.elecfans.com/wearable/6653287.html)

The lead remains current. Coverage of Allwinner's **2026 “Smart Vision” ecosystem conference** reports that Qingcheng Wireless demonstrated a new-generation V881 AI camera/display glasses solution. Separate conference coverage describes a V881 + F101 waveguide display reference product with camera capture, display overlays, and limited on-device detection. This is strong evidence that Qingcheng Wireless remains active in smart-glasses solution engineering in 2026.

2026 references:

- [2026 Allwinner ecosystem conference coverage — 10jqka](https://stock.10jqka.com.cn/20260723/c678390516.shtml)
- [2026 Allwinner ecosystem conference coverage — Vision Systems China](https://www.vision-systems-china.com/deinews.asp?id=19928)
- [2026 conference technical summary — Electronic Innovation](https://static.eetrend.com/content/2026-07/85558821-9d5a-46df-9bdb-92b6a2657ebc-100602761.html)

Canonical organization record: [ORG-0004 — Shenzhen Qingcheng Wireless Technology](../glossary/organizations/ORG-0004-qingcheng-wireless.md)

### Do not silently merge “Qingcheng Wireless” and “Qingcheng Future”

GlassesResearch already tracks **Shenzhen Qingcheng Future Technology Co., Ltd.** as the organization identity previously tied to the HeyCyan companion application. The Allwinner conference evidence instead names **Shenzhen Qingcheng Wireless Technology Co., Ltd.**

The names are similar and may have an operational, corporate, personnel, or software relationship. That relationship is **not yet established strongly enough to treat the two legal names as aliases**.

Until stronger evidence resolves the identity:

- [ORG-0001 — Shenzhen Qingcheng Future Technology / HeyCyan](../glossary/organizations/ORG-0001-hecyan-qingcheng-future.md) remains the existing app-operator record.
- [ORG-0004 — Shenzhen Qingcheng Wireless Technology](../glossary/organizations/ORG-0004-qingcheng-wireless.md) records the V821/V881 solution-house evidence.
- Cross-links record the investigation rather than collapsing the entities.

### Magic Treasure Era — ODM/manufacturing lead, not yet factory proof for W610/W630

At the same Allwinner ecosystem event, **Magic Treasure Era** was presented from the perspective of a veteran ODM discussing how AI-glasses technology moves into design and production. This makes it a worthwhile manufacturing/integration lead in the Allwinner ecosystem.

That evidence establishes relevance to smart-glasses ODM work; it does **not** establish that Magic Treasure Era is the final-assembly factory for any specific W610/W630 listing without device-level or contractual evidence.

Reference:

- [EEWORLD event coverage](https://en.eeworld.com.cn/mp/XSY/a399875.jspx)

## Case study: recurring W610 / W630-style platform fingerprints

The existing [W610 Manufacturing Intelligence Map](../models/W610/manufacturing/INTELLIGENCE_MAP.md) documents a repeated W610 fingerprint across commercial sources, including the JL7018F + Allwinner V821L2-class architecture, camera and storage claims, Wi-Fi media transfer, magnetic charging, dual-microphone audio, and HeyCyan integration.

Repeated fingerprints support a **shared reference-platform, solution-house, or supply-chain hypothesis**. They do not by themselves tell us which entity:

- designed the PCB;
- owns the firmware source and signing process;
- owns the mechanical molds;
- performs SMT;
- performs final assembly and test;
- owns the camera module design;
- controls the companion application or cloud services; or
- has authority to relocate components for an ODM customer.

W630 and other V821-family listings extend the same research problem. The next step is platform fingerprinting and provenance, not counting every reseller page as a new manufacturer.

## Alibaba and marketplace evidence: useful but fragile

Marketplace listings are valuable for discovering aliases, model numbers, seller entities, claimed customization, recurring photographs, BOM clues, and price/MOQ patterns. They are not reliable enough by themselves to settle design ownership or factory identity.

Current investigation examples include:

- W630-class camera-glasses listings from multiple unrelated commercial sellers;
- F20 audio/translation glasses appearing under multiple seller identities;
- repeated V821/JL7018-class combinations across camera glasses;
- identical or near-identical frames marketed with different brand names and capability headlines.

Marketing titles can also blur distinctions such as native camera resolution versus interpolation, remote phone-camera control versus an onboard camera, app/cloud AI versus on-device inference, or still-image resolution versus video resolution. Model records must preserve the underlying evidence rather than normalize the headline.

**Preservation status:** exact marketplace URLs should be archived when lawful and practical because seller pages frequently mutate or disappear. This page records the research method and durable upstream sources; individual fragile listings remain evidence leads until archived or promoted into model-specific evidence records.

## Provenance tests

When two products appear related, GlassesResearch should look for converging evidence across several independent surfaces.

### Hardware fingerprints

- SoC and coprocessor combination
- camera sensor and module markings
- flash / NAND parts
- battery capacity and cell markings
- PCB dimensions, silk-screen IDs, and connector layout
- FPC part numbers
- microphones, amplifiers, speakers, and touch controllers
- antenna placement
- charging geometry
- physical button and hinge layout
- mold marks and internal part numbers

### Firmware and software fingerprints

- Bluetooth advertising names and UUIDs
- Wi-Fi transfer behavior
- companion-app package names
- OTA endpoints
- firmware filenames and version conventions
- signing certificates / update metadata
- protocol packet structure
- device identifiers exposed to the app
- cloud endpoints and privacy-policy entities

### Corporate and regulatory fingerprints

- FCC grantee / equipment records
- Bluetooth SIG declarations
- certification reports and test-lab applicants
- patents and industrial-design registrations
- trademark filings
- trade-show exhibitor records
- legal company names and addresses
- factory audit material
- import/export records when available and lawfully accessible

### Commercial fingerprints

- identical MOQ tiers
- identical specification errors
- identical product photography
- identical packaging/manuals/QR codes
- identical customization menus
- shared sales contacts or domains

No single fingerprint automatically proves common manufacture.

## Supplier qualification questions

A serious provenance inquiry should ask a candidate supplier questions that a reseller cannot answer convincingly with marketing language alone:

1. Did your company design the PCB for this platform?
2. Who owns the schematic and PCB layout files?
3. Can your engineers change PCB outline and component placement directly?
4. Who owns the mechanical tooling and molds?
5. Can your engineers relocate the camera or change its FPC/module?
6. Who maintains the firmware source and signs production firmware?
7. Can you provide or customize the phone communication protocol / SDK?
8. Where are SMT, final assembly, optical alignment, and final test physically performed?
9. Which operations are subcontracted?
10. Which company is the original design manufacturer for the platform?
11. Why is the same model number sold by unrelated suppliers, and what is your relationship to them?

These answers remain commercial claims until corroborated, but the specificity of the response can identify where deeper verification should focus.

## Confidence model for manufacturing attribution

### Confirmed

Use only when evidence directly identifies the role for the relevant product or platform: e.g. factory documentation, regulatory applicant records that match the production entity, contractual/source documentation, direct teardown markings tied to a legal entity, or a primary engineering source.

### Strong lead

Multiple credible sources place the organization in the relevant design/solution/manufacturing role, but the exact product-level responsibility is not yet proven.

### Commercial claim

The organization describes itself as manufacturer/OEM/ODM or offers customization, but independent evidence of design or factory authority is incomplete.

### Inferred

Technical fingerprints support a shared platform or relationship, but no source directly establishes the entity connection.

### Unknown

The evidence does not yet identify the responsible organization.

## Current working map

| Layer | Entity / family | Current evidence state | What is still unresolved |
|---|---|---|---|
| Vision silicon / reference development | Allwinner V821 / V881 | **Confirmed** primary chip and development ecosystem | Which exact retail products descend from which reference design/revision |
| Smart-glasses solution/design lead | Shenzhen Qingcheng Wireless Technology | **Strong lead** — V821 complete solution jointly presented with Allwinner; V881 glasses solution shown in 2026 | Exact W610/W630 design ownership; factory responsibility; relationship to Qingcheng Future |
| App/software identity | Shenzhen Qingcheng Future Technology / HeyCyan | **Existing confirmed app-operator record** in GlassesResearch | Corporate/operational relationship to Qingcheng Wireless; hardware authority |
| ODM / design-for-manufacture lead | Magic Treasure Era | **Strong ecosystem lead** from Allwinner event coverage | Exact products, factory operations, tooling ownership |
| Commercial OEM/supplier lead | Goodway Techs | **Confirmed commercial source; manufacturing role unresolved** | PCB/firmware/mold ownership; SMT/final assembly authority |
| Commercial OEM/supplier lead | Dongguan Zhiyang | **Confirmed seller/supplier; manufacturing role unresolved** | Same questions as above |
| Retail/rebrand layer | Multiple marketplace brands and sellers | **Confirmed commercial identities** | Upstream platform and factory relationships |

This table is deliberately conservative. A “strong lead” is not silently promoted to “manufacturer.”

## Open research questions

- Who originated the recurring JL7018F + V821/V821L2 smart-glasses board families?
- Which organizations hold source-level firmware authority for the common V821 camera-glasses platforms?
- Which molds and PCB layouts are shared across W610/W630 and other repeated commercial variants?
- What is the relationship, if any, between Shenzhen Qingcheng Wireless Technology and Shenzhen Qingcheng Future Technology?
- Which companies in the Allwinner ecosystem perform actual SMT and final assembly for export products?
- Do W610/W630-labelled products represent one hardware lineage, several revisions of one reference platform, or multiple implementations sharing only a chipset/application stack?
- Which marketplace “AI” capabilities execute on-glasses, on a companion phone, or in cloud services?

## Research rule

**The logo on the glasses, the company selling the glasses, the company operating the app, the company that designed the electronics, and the company assembling the product may all be different entities.**

GlassesResearch records those roles separately until evidence says otherwise.

## Related research

- [Ecosystem relationship map](ECOSYSTEM_MAP.md)
- [W610 Manufacturing Intelligence](../models/W610/manufacturing/README.md)
- [W610 Manufacturing Intelligence Map](../models/W610/manufacturing/INTELLIGENCE_MAP.md)
- [W610 identity investigation](../models/W610/investigations/001-identity.md)
- [HeyCyan lineage](../lineages/HEYCYAN.md)
- [Companion App Database](COMPANION_APP_DATABASE.md)
- [Research Standards](RESEARCH_STANDARDS.md)
