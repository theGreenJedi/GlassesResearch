# Canonical reconciliation — VRcompare batch 02

Date: 2026-08-31

This packet adjudicates four smart-glasses products surfaced during the VRcompare comparison. VRcompare is discovery-only. Admission evidence is independently sourced in [EV-0089](../evidence/EV-0089-VRcompare-reconciliation-batch-02-primary-acquisition.md).

This is a **stacked reconciliation** on top of batch 01. The proposed IDs below assume `GLS-0167` and `GLS-0168` from batch 01 are accepted first; if that prerequisite changes, these IDs must be reallocated before merge rather than creating collisions.

## Admit to canonical purchaser-history ledger

| Proposed ID | Maker | Model | Era | State | Type | Access | Evidence |
|---|---|---|---:|---|---|---|---|
| GLS-0169 | Rokid | Max Pro (RA202) | 2023/2024 | current/enterprise | XR/AR display | B2B/store | primary + contemporaneous secondary | 
| GLS-0170 | Huawei | Vision Glass | 2022 | legacy/current unclear, region-limited | XR display | retail/China | primary product + contemporaneous secondary sale record |
| GLS-0171 | Lenovo | Glasses T1 (AR-6561Y; Yoga Glasses in China) | 2022 | legacy/current unclear, region-limited | XR display | regional/direct sales | primary |
| GLS-0172 | DigiLens | ARGO | 2022 | current/enterprise | standalone enterprise AR | enterprise/integrator | primary + commercial |

## Identity decisions

### GLS-0169 — Rokid Max Pro
Max Pro is not Rokid Max or Max 2. Rokid assigns model **RA202** and names it as the glasses component of Rokid AR Studio. Commercial sale as part of an AR Studio package is sufficient purchaser-history evidence; the ledger does not require that every component be sold standalone in every market.

### GLS-0170 — HUAWEI Vision Glass
Vision Glass is distinct from Huawei's audio-eyewear line. It is a host-connected dual-display viewing-glasses product. The maintained manufacturer page establishes identity; contemporaneous December 2022 reporting establishes actual Vmall sale after the original storefront became difficult to retrieve.

### GLS-0171 — Lenovo Glasses T1
Lenovo's own material identifies **Lenovo Yoga Glasses** as the China-market name of Glasses T1. Treat Yoga Glasses as an alias unless evidence establishes materially different hardware. The support identity **AR-6561Y** anchors the shipped product.

### GLS-0172 — DigiLens ARGO
ARGO is eyewear, not a helmet/headset form requiring adjacent-catalog routing. DigiLens describes and contracts for sale of the ARGO headset/smartglasses, and a current integrator exposes a concrete procurement route.

## Evidence boundary

Admission records purchaser history and product identity. It does **not** promote manufacturer specifications into measured performance, nor does it infer Report Card values for wearability, openness, owner control, cloud independence, hackability, repairability or value. Existing lineage scores must not be copied onto these products merely because they share a maker or broad architecture.

## Catalog propagation

If batch 01 and this packet are both approved, the active canonical count would move from **165 to 171**. Synchronization should update `models/THE_LIST.md`, derived count statements, Finder/comparison surfaces, model-resource links and any catalog-dependent tests mechanically. Do not hand-maintain a public count independent of the canonical ledger.

## Source packet

- `evidence/EV-0089-VRcompare-reconciliation-batch-02-primary-acquisition.md`
- https://global.rokid.com/pages/security-center
- https://arstudio.rokid.com/
- https://de.rokid.com/fr/products/rokid-ar-studio-pour-b2b
- https://consumer.huawei.com/cn/wearables/vision-glass/
- https://www.ithome.com/0/663/477.htm
- https://news.lenovo.com/pressroom/press-releases/glasses-t1-wearable-display-for-gaming-streaming-privacy-on-the-go/
- https://news.lenovo.com/wp-content/uploads/2022/08/Lenovo-T1-Glasses-DS.pdf
- https://www.digilens.com/argo/
- https://www.digilens.com/argo/terms-of-use/
- https://magicgate.com/digilens-argo/