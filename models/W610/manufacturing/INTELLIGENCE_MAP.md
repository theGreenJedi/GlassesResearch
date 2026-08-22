# W610 Manufacturing Intelligence Map

The commercial name on a listing may identify a reseller rather than the designer, solution house, software operator, or final-assembly factory. Roles below remain deliberately separated.

This model-specific map is now also a case study inside the ecosystem-wide investigation: [Who Actually Makes These Glasses? Mapping the Shenzhen Smart-Glasses Platform Ecosystem](../../../docs/SHENZHEN_SMART_GLASSES_SUPPLY_CHAIN.md).

## Current entity map

| Entity | Observed role | Evidence | Confidence |
|---|---|---|---|
| Shenzhen Qingcheng Future Technology Co., Ltd. (深圳市青橙未来科技有限公司) | HeyCyan app operator/developer | App-store/developer identity, Shenzhen contact information, support records | Confirmed app operator; hardware/design role unknown |
| Shenzhen Qingcheng Wireless Technology Co., Ltd. (深圳市青橙无线科技有限公司) | Upstream V821/V881 smart-glasses solution/design-house lead | Allwinner ecosystem-event coverage describes a V821 complete-glasses solution jointly developed with Allwinner; 2026 event coverage shows a V881 camera/display glasses solution | Strong solution-house evidence; direct W610 design/manufacture still unproven |
| Dongguan Zhiyang Electronic Technology Co., Ltd. | Alibaba supplier marketing W610 as Zhiyang/OEM/ODM | Alibaba company listing and W610 product specification | Confirmed seller/supplier; design and factory ownership unverified |
| Goodway Techs | W610 OEM/ODM solution marketer and customization contact | W610 product page, downloadable specification material, Shenzhen address and sales contacts | Confirmed commercial/OEM lead; exact design/manufacturing role unverified |
| Xinhua Lela Technology Co., Ltd. / Mingdaln | Retail brand/store operator | Mingdaln storefront company disclosure and W610 product page | Confirmed retail-brand lead |
| NJYUAN | Retail/reseller brand | W610 product page with common platform specifications | Confirmed seller identity; corporate role unresolved |
| KLSYQ | Amazon retail brand | W610 manual/listing identity | Confirmed retail name; upstream supplier unresolved |
| Mingtawn | Retail brand | W610 manual/listing identity | Confirmed retail name; upstream supplier unresolved |
| Huaqiangbei Electronics Market seller | Wholesale/reseller channel | W610 wholesale listing with OEM pricing and customization claims | Confirmed reseller channel; upstream factory unresolved |

## New upstream evidence: Qingcheng Wireless + Allwinner

Industry coverage of an Allwinner AI-glasses ecosystem event reports that **Qingcheng Wireless general manager Huang Lianghui released a “V821 Complete Glasses Solution” and described the V821 AI-glasses solution as jointly developed by Qingcheng Wireless and Allwinner**.

References:

- [EEWORLD — Allwinner “Smart Eyes” AI-glasses event](https://en.eeworld.com.cn/mp/XSY/a399875.jspx)
- [Elecfans — corroborating coverage](https://www.elecfans.com/wearable/6653287.html)
- [Allwinner V821 platform documentation](https://docs.aw-ol.com/docs/soc/v821/)

This materially changes the investigation: Qingcheng Wireless is now a **strong upstream solution/design-house lead**, not merely another seller name.

It does **not** establish any of the following without further evidence:

- that Qingcheng Wireless originated the exact W610 PCB;
- that every W610-labelled product descends from its V821 solution;
- that Qingcheng Wireless owns W610 mechanical molds;
- that it performs W610 SMT or final assembly; or
- that Shenzhen Qingcheng Wireless Technology and Shenzhen Qingcheng Future Technology / HeyCyan are the same legal entity.

Those questions remain open.

The lead is current rather than historical. 2026 Allwinner ecosystem-conference coverage reports Qingcheng Wireless demonstrating a new V881 AI camera/display glasses solution:

- [10jqka — 2026 Allwinner ecosystem conference](https://stock.10jqka.com.cn/20260723/c678390516.shtml)
- [Vision Systems China — 2026 conference coverage](https://www.vision-systems-china.com/deinews.asp?id=19928)

Canonical record: [ORG-0004 — Shenzhen Qingcheng Wireless Technology](../../../glossary/organizations/ORG-0004-qingcheng-wireless.md).

## Identity boundary: Qingcheng Future versus Qingcheng Wireless

The repository previously had one Qingcheng lead: [ORG-0001 — Shenzhen Qingcheng Future Technology / HeyCyan](../../../glossary/organizations/ORG-0001-hecyan-qingcheng-future.md), confirmed in the project as the HeyCyan app-operator identity.

The Allwinner solution-house evidence names **Shenzhen Qingcheng Wireless Technology Co., Ltd.** instead.

The similar names are investigatively significant, but GlassesResearch does not currently have sufficient evidence to collapse them into one entity. Until the corporate relationship is resolved, software/app attribution and upstream hardware-solution attribution stay in separate evidence lanes.

## Platform fingerprint shared across suppliers

Multiple commercial sources independently repeat the following W610-style combination:

- Jerry JL7018F main controller
- Allwinner V821L2 coprocessor
- 8 MP camera with 32 MP interpolation claim
- 4 GB / 32 Gbit storage
- roughly 270 mAh polymer battery
- magnetic charging
- HeyCyan companion app
- Wi-Fi media transfer
- dual-microphone ENC
- IP65 claim

This repeated fingerprint strongly suggests a shared reference design, solution-house platform, or supply chain. It does **not** yet establish which company owns the design, firmware, molds, or final assembly.

Allwinner's own V821 developer material is relevant because it shows that the chip ecosystem includes compact reference/development hardware intended to accelerate camera-product and AI-glasses development. A common Allwinner platform can therefore create technical convergence without proving that all resulting products share one factory.

- [Allwinner V821 AI-glasses development board](https://www.aw-ol.com/solutions/57)
- [Allwinner V821 product page](https://www.allwinnertech.com/index.php?c=product&id=136)

## Working relationship model

```text
Allwinner V821/V821L2 silicon + reference-development ecosystem
            |
            +-- strong solution/design-house lead: Qingcheng Wireless
            |       (exact W610 ownership unresolved)
            |
            +-- component vendors: JieLi/Jerry + camera/memory suppliers
            |
            +-- OEM/ODM and wholesale channels: Zhiyang, Goodway, other Shenzhen/Dongguan suppliers
            |
            +-- app/cloud operator record: Shenzhen Qingcheng Future Technology / HeyCyan
            |       (relationship to Qingcheng Wireless unresolved)
            |
            +-- retail rebrands: Mingdaln, NJYUAN, KLSYQ, Mingtawn, unbranded sellers
            |
            +-- physical SMT/final-assembly factory: unresolved
```

This diagram is a research model, not a claim that every branch represents a contractual relationship.

## Questions still open

- Who owns the W610 industrial design and private mold?
- Who designed and owns the W610 PCB layout?
- Who signs or publishes firmware updates?
- Is HeyCyan operated independently from the upstream hardware solution house?
- What is the corporate or operational relationship between Qingcheng Future and Qingcheng Wireless?
- Are Goodway and Zhiyang factories, trading companies, design houses, integrators, or combinations?
- Which entity performs SMT, optical/camera alignment, final assembly, and test?
- Which entity appears on the owned unit's packaging, manuals, labels, QR destinations, certificates, and app traffic?
- Are there distinct W610 hardware revisions sold under the same name?
- Which W610/W630-style commercial products can be tied directly to Qingcheng Wireless's V821 solution rather than only to the same chipset family?

## Next investigation actions

1. Preserve downloadable Goodway specification materials and exact Alibaba seller pages.
2. Inspect packaging and manual legal text from the owned unit.
3. Analyze HeyCyan APK metadata, certificates, domains, privacy policy, firmware delivery, and network endpoints.
4. Search corporate registries, FCC, Bluetooth SIG, patents, trade-show records, and certification databases for both Qingcheng legal names and known sellers.
5. Compare PCB/FPC markings, camera modules, factory/product photography, molds, packaging, and assembly details across W610/W630-style variants.
6. Seek independent teardowns that expose board markings and component provenance.
7. Contact suppliers using a consistent design-authority questionnaire: PCB ownership, firmware authority, mold ownership, camera relocation authority, SMT site, and final-assembly site.
8. Ask Allwinner ecosystem contacts which ODM/solution partners commercialize V821/V881 smart-glasses designs, while treating referrals as leads rather than product-level proof.

## Evidence rule

The company that sells a W610, the company that operates its app, the company that designed its electronics, and the company that assembles it may all be different. GlassesResearch will not collapse those roles until evidence supports the relationship.
