# W610 Manufacturing Intelligence Map

The commercial name on a listing may identify a reseller rather than the designer or factory. Roles below remain deliberately separated.

## Current entity map

| Entity | Observed role | Evidence | Confidence |
|---|---|---|---|
| Shenzhen Qingcheng Future Technology Co., Ltd. (深圳市青橙未来科技有限公司) | HeyCyan Android app operator/developer | Google Play developer identity, Shenzhen address, support email and phone | Confirmed app operator; manufacturing role unknown |
| Dongguan Zhiyang Electronic Technology Co., Ltd. | Alibaba supplier marketing W610 as Zhiyang/OEM/ODM | Alibaba company listing and W610 product specification | Confirmed seller/supplier; design and factory ownership unverified |
| Goodway Techs | W610 OEM solution marketer and customization contact | W610 product page, downloadable specification sheet, Shenzhen address and sales contacts | Confirmed commercial/OEM lead; exact manufacturing role unverified |
| Xinhua Lela Technology Co., Ltd. / Mingdaln | Retail brand/store operator | Mingdaln storefront company disclosure and W610 product page | Confirmed retail-brand lead |
| NJYUAN | Retail/reseller brand | W610 product page with common platform specifications | Confirmed seller identity; corporate role unresolved |
| KLSYQ | Amazon retail brand | W610 manual/listing identity | Confirmed retail name; upstream supplier unresolved |
| Mingtawn | Retail brand | W610 manual/listing identity | Confirmed retail name; upstream supplier unresolved |
| Huaqiangbei Electronics Market seller | Wholesale/reseller channel | W610 wholesale listing with OEM pricing and customization claims | Confirmed reseller channel; upstream factory unresolved |

## Platform fingerprint shared across suppliers

Multiple commercial sources independently repeat the following combination:

- Jerry JL7018F main controller
- Allwinner V821L2 coprocessor
- 8 MP camera with 32 MP interpolation claim
- 4 GB / 32 Gbit storage
- 270 mAh polymer battery
- magnetic charging
- HeyCyan companion app
- Wi-Fi media transfer
- dual-microphone ENC
- IP65 claim

This repeated fingerprint strongly suggests a shared reference design or supply chain. It does **not** yet establish which company owns the design, firmware, molds, or final assembly.

## Working relationship model

```text
Unknown platform/reference-design owner
            |
            +-- component vendors: JieLi/Jerry + Allwinner + camera/memory suppliers
            |
            +-- OEM/ODM and wholesale channels: Zhiyang, Goodway, other Shenzhen/Dongguan suppliers
            |
            +-- app/cloud operator: Shenzhen Qingcheng Future Technology / HeyCyan
            |
            +-- retail rebrands: Mingdaln, NJYUAN, KLSYQ, Mingtawn, unbranded sellers
```

## Questions still open

- Who owns the industrial design and private mold?
- Who signs or publishes firmware updates?
- Is HeyCyan operated independently or by the platform owner?
- Are Goodway and Zhiyang factories, trading companies, design houses, or combinations?
- Which entity appears on the owned unit's packaging, manuals, labels, QR destinations, certificates, and app traffic?
- Are there distinct W610 hardware revisions sold under the same name?

## Next investigation actions

1. Preserve downloadable Goodway specification materials and exact Alibaba seller pages.
2. Inspect packaging and manual legal text from the owned unit.
3. Analyze HeyCyan APK metadata, certificates, domains, privacy policy, and network endpoints.
4. Search corporate registries and certification databases for the named companies and addresses.
5. Compare factory/product photography for common molds, packaging, and assembly details.
6. Contact suppliers only after preparing a consistent technical questionnaire.
