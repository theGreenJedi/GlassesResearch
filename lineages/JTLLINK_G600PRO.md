# Huizhou JTLlink G600Pro smart-glasses hardware lineage

The G600Pro family is tracked as a **confirmed regulatory hardware/OEM lineage**. The FCC test package names Huizhou JTLlink Technology Co., Ltd. as applicant, manufacturer, and factory for the tested smart-glasses platform. A current commercial listing uses the **SENDER** brand for G600Pro. GlassesResearch therefore preserves the regulatory manufacturer and the commercial brand separately rather than assuming the marketplace brand is the factory identity.

**Relationship type:** confirmed hardware lineage + OEM/ODM lineage; retail-brand relationship documented commercially but corporate ownership is unresolved  
**Confidence:** Confirmed for the FCC-listed hardware family; unresolved for downstream brand/rebrand relationships

## Canonical population

| Product / name | GlassesResearch status | Treatment |
|---|---|---|
| Sender G600Pro | `GLS-0250` | Canonical purchasable model; current commercial listing plus regulatory identity |
| G600S | lineage member | Do not count separately without distinct commercial identity/acquisition evidence |
| E06S | lineage member | Do not count separately without distinct commercial identity/acquisition evidence |
| E06 | lineage member | Do not count separately without distinct commercial identity/acquisition evidence |
| S100 | lineage member | Do not count separately without distinct commercial identity/acquisition evidence |
| S200 | lineage member | Do not count separately without distinct commercial identity/acquisition evidence |
| S300 | lineage member | Do not count separately without distinct commercial identity/acquisition evidence |
| S500 | lineage member | Do not count separately without distinct commercial identity/acquisition evidence |
| HS600 | lineage member | Do not count separately without distinct commercial identity/acquisition evidence |

## Regulatory identity

FCC test report **EED32S80475301**, issued May 18, 2026 for **FCC ID 2BEKU-G600PRO**, identifies the product as smart glasses and lists the model references:

`G600Pro, G600S, E06S, E06, S100, S200, S300, S500, HS600`.

The report identifies **Huizhou JTLlink Technology Co., Ltd.** as applicant, manufacturer, and factory. It states that the listed models share the same electrical design, PCB, and layout, while model names and appearance can differ for marketing requirements. G600Pro was the tested model.

That is strong evidence for a shared hardware family. It is **not** evidence that every listed name is an independently sold product, nor that appearance is identical across the family.

## Commercial identity

A current Alibaba supplier listing markets **Sender G600Pro** as AI/camera smart glasses. The listing is useful evidence that G600Pro crossed the project's acquisition threshold, but its specifications remain **commercial claims** unless independently reproduced or corroborated by primary technical documentation.

The marketplace layer and regulatory layer therefore remain distinct:

- **Commercial brand/name:** Sender G600Pro.
- **Regulatory manufacturer:** Huizhou JTLlink Technology Co., Ltd.
- **FCC family:** G600Pro / G600S / E06S / E06 / S100 / S200 / S300 / S500 / HS600.
- **Canonical count:** one admitted model at present, not nine.

## Evidence propagation rule

Regulatory evidence may propagate only what the filing actually establishes across the named family: the shared electrical/PCB/layout relationship and the tested radio platform. It must **not** silently propagate seller-claimed camera specifications, battery capacity, AI features, translation behavior, charging method, app behavior, cloud dependence, frame dimensions, or wearability.

Likewise, a future retail listing for one of the sibling names should not automatically create a new canonical row. GlassesResearch should first determine whether it represents a materially named commercial product/generation, a frame/appearance variant, or a simple rebrand of the same platform.

## Open questions

1. What is the exact commercial/corporate relationship between the Sender-branded seller and Huizhou JTLlink Technology?
2. Which companion application, cloud services, and account requirements are used by G600Pro?
3. Which of G600S, E06S, E06, S100, S200, S300, S500 and HS600 have independently documented retail identities?
4. What mechanical/frame differences correspond to the FCC report's appearance differences?
5. Which marketplace specifications are stable platform properties versus seller-specific configuration claims?
6. Do sibling retail products share firmware and update infrastructure, or only the underlying electrical/PCB platform?

## Sources

- [FCC test report EED32S80475301 / FCC ID 2BEKU-G600PRO](https://device.report/m/c17704d2ba8dd1f6287b235cf907a530475c9791ae9e68700d366468c4c10379.pdf)
- [Huizhou JTLlink FCC filing index](https://fcc.report/company/huizhou-jtllink-technology-co-ltd)
- [Sender G600Pro supplier listing](https://www.alibaba.com/product-detail/2026-New-Sender-AI-Smart-Camera_1601726521408.html)

## Related GlassesResearch layers

- [The List](../models/THE_LIST.md)
- [Model Registry](../models/CATALOG.md)
- [Retail Rebrands & OEM Ecosystems](../models/RETAIL_REBRANDS.md)
- [Technology Lineages](README.md)
