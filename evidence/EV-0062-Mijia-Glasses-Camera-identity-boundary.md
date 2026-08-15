# EV-0062 — Mijia Glasses Camera identity and evidence boundary

**Status:** Model identity resolved for catalog/report-card use; manufacturer manual and direct Bluetooth exhibit still sought  
**Model:** Xiaomi Mijia Glasses Camera  
**Candidate model number:** `MJSV01FC`  
**Launch period:** August 2022  
**Reviewed:** 2026-08-14

## Question

Can GLS-0023 be separated cleanly from Xiaomi's audio-glasses branches and tied to a model-specific identity without treating marketplace specifications as manufacturer-verified facts?

## Finding

A Beijing municipal-government new-product list directly names **Beijing Fengchao Century Technology Co., Ltd.**, product **Glasses Camera**, and model **MJSV01FC**. That primary identity record converges with the surviving Xiaomi route at `https://www.mi.com/mjglass`, Xiaomi-hosted product-trial coverage, contemporaneous launch reporting, a Bluetooth-certification index, commercial records, and peer-reviewed use records.

This is not the 2023 Mijia Smart Audio Glasses. The 2022 device has cameras and a near-eye AR display; the audio branch is ordinary-form open-ear Bluetooth eyewear without that camera/display architecture.

## Evidence lanes

### Xiaomi-hosted evidence

A Xiaomi community/product-trial page describes a dual-camera product with a Sony Micro OLED and external free-form AR optical engine. Because this is hosted by Xiaomi but written as a trial/review account, GlassesResearch records it as **Xiaomi-hosted community evidence**, not a formal specification sheet.

### Primary identity record

The Beijing Municipal Science and Technology Commission's 2023 second-batch new-product list records Beijing Fengchao Century Technology Co., Ltd., the product name 眼镜相机 (Glasses Camera), and model `MJSV01FC`. This is direct government-hosted evidence for the company/product/model mapping, though it is not a technical datasheet.

### Independent identity corroboration

- A Bluetooth Launch Studio certificate index records the Chinese and English product names with model `MJSV01FC` and a 2022-08-02 date.
- A 2025 peer-reviewed medical-training study identifies the eyeglass camera used in its protocol as `MJSV01FC`.
- Multiple period commercial records use the same model number for the Mijia Glasses Camera and its dedicated charging accessory.

Together with the government list, these records close the catalog identity question. The direct Bluetooth certificate and manufacturer manual remain preferable technical preservation targets.

## Conservatively supported characteristics

The current evidence supports the following as source-bounded findings:

- distinct camera/display architecture;
- dual cameras;
- near-eye Micro OLED/free-form AR optical display;
- documented first-person capture use;
- association with the `MJSV01FC` model string;
- a dedicated companion/software workflow;
- China-focused launch and acquisition route.

Period reporting and commercial records additionally describe 32 GB storage, Snapdragon compute, wide and telephoto cameras, hybrid zoom, Wi-Fi/Bluetooth, and a 1,020 mAh battery. These remain **secondary/commercial specifications** until recovered from a manufacturer manual, archived product sheet, or direct regulatory exhibit.

## Not established

- A complete manufacturer specification sheet preserved by GlassesResearch.
- Direct regulatory exhibits or the original user manual.
- Exact processor SKU.
- Current server, account, app, firmware-update, offline or sideloading behavior.
- Standard file access, developer APIs, bootloader state or recovery images.
- Independent optical serviceability or prescription support.
- Hands-on performance, battery endurance, thermal behavior or capture quality.

## Catalog and Report Card effect

GLS-0023 is a valid separate canonical model and now has a conservative card in [`LINEAGE_XIAOMI_MIJIA_CAMERA.md`](../docs/report-cards/LINEAGE_XIAOMI_MIJIA_CAMERA.md). Hardware/display strengths are graded from the established architecture; Software, Openness, Owner Control, Cloud Independence and Hackability remain deliberately low-confidence and conservative because present-day service and owner-access behavior is untested.

## Sources

- [Beijing municipal-government new-product list (PDF)](https://kw.beijing.gov.cn/zwgk/tzgg/202312/P020240919619054378012.pdf)
- [Surviving Xiaomi product route](https://www.mi.com/mjglass)
- [Xiaomi-hosted product-trial account](https://web.vip.miui.com/page/info/mio/mio/detail?app_version=dev.20051&postId=38575976)
- [Contemporaneous August 2022 launch report](https://mashdigi.com/xiaomi-launched-the-mijia-glasses-camera-allowing-users-eyes-to-learn-to-zoom-and-record-the-first-10-seconds-of-the-momentary-picture/)
- [Bluetooth certificate index record](https://t.me/s/XiaomiCertificationTracker?before=3166)
- [Peer-reviewed study identifying MJSV01FC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12449284/)

## Preservation note

The dead-or-JavaScript-dependent manufacturer route and the indexed certificate are fragile. Preserve a lawful manufacturer manual or direct certificate record when recovered. Marketplace pages are leads, not substitutes for primary specifications.
