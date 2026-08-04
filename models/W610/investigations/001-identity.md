# Investigation 001 — W610 Identity

## Objective

Determine whether `W610` identifies a single branded product, a shared hardware platform, or a family of loosely related products, and identify the most useful organizations and communities for further research.

## Status

**Initial public-source pass complete. Device-level verification remains open.**

## Findings

1. `W610` is sold under multiple retail names, including Goodway, Mingdaln, NJYUAN, KLSYQ, Mingtawn, Zhiyang/OEM/ODM, and unbranded marketplace listings.
2. Multiple apparently independent sellers repeat a distinctive technical fingerprint: JL7018F main controller, Allwinner V821L2 coprocessor, 8 MP camera with interpolated-resolution claims, approximately 270 mAh battery, magnetic charging, Wi-Fi media transfer, dual-microphone ENC, IP65 marketing, and the HeyCyan app.
3. This repeated fingerprint is strong evidence for a shared reference platform or supply chain, but it does not yet identify the platform owner or final manufacturer.
4. The Google Play listing identifies Shenzhen Qingcheng Future Technology Co., Ltd. as the HeyCyan app operator. This is not yet evidence that it manufactures the glasses.
5. Dongguan Zhiyang Electronic Technology and Goodway Techs are strong OEM/ODM leads. Their exact roles—factory, design house, trading company, or mixed operation—remain unresolved.
6. Public community discovery is still weak. The most productive current knowledge sources are commercial/OEM pages, app-store records, manual mirrors, and the owned device itself rather than a mature W610 reverse-engineering community.

## Source set reviewed

- Goodway Techs W610 OEM product page and specification material
- Dongguan Zhiyang Electronic Technology Alibaba W610 listing
- Huaqiangbei Electronics Market W610 wholesale listing
- HeyCyan Google Play developer listing and user reviews
- Mingdaln and NJYUAN W610 retail pages
- KLSYQ and Mingtawn W610 manual mirrors
- Generic marketplace listings using the W610 designation

## Repository areas updated

- `COMMUNITY_MAP.md`
- `GENEALOGY.md`
- `manufacturing/INTELLIGENCE_MAP.md`

## Cautions

Commercial pages frequently copy one another and may contain incorrect specifications. Repetition strengthens a lead but does not replace physical evidence. Claims about operating systems, Bluetooth versions, weights, camera resolution, and battery capacity conflict across listings and require device-level testing.

## Next actions

1. Record every identifier from the owned W610 package, manual, device labels, QR codes, Bluetooth advertisements, and app prompts.
2. Photograph control layout and compare it against each known retail variant.
3. Acquire and statically inspect the HeyCyan APK without granting unnecessary permissions.
4. Capture BLE services and device-information values.
5. Locate firmware/update endpoints and app-supported model lists.
6. Search regulatory databases using confirmed company names, addresses, radio identifiers, and chipset leads.
7. Archive the strongest public sources before they disappear.
