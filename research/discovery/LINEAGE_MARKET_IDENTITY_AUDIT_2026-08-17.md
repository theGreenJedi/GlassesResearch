# Market identity and lineage discovery audit — 2026-08-17

## Question

If a purchaser knows only the name printed on the box, can GlassesResearch lead that person to the underlying hardware/platform research without inflating the canonical model count for simple rebrands?

## Result

Yes for the first verified clusters. The search exposed two large commodity lineage houses plus several distinct sibling platforms that must not be collapsed merely because they share an app or chipset family.

## House 1 — W610 / HeyCyan camera lineage

### Verified market identities that should not add another canonical model count

- **BooaBei** → W610 / HeyCyan lineage.
- **Zbna W610** → W610. Published manual identifies `W610 (M02)` and documents JL7018F + Allwinner V821L2, 270 mAh battery, Wi-Fi transfer and HeyCyan voice behavior.
- **Mingtawn W610** → W610. Multiple manuals identify model W610 and direct owners to HeyCyan.
- **ESTG W610** → W610. Published manual identifies W610 with the same JL7018F + V821L2 / 270 mAh architecture.
- **STARK Horizon** → strong W610 market identity. STARK's own product copy describes the underlying glasses as `STARK W610`. Seller-specific frame, firmware or package differences remain possible and should be preserved.

Canonical count effect: **zero additional models** beyond GLS-0039 for these names.

### Distinct HeyCyan sibling platforms — do not collapse into W610

Current supplier/manufacturer evidence separately names and offers:

- W611 Pro
- W620
- W630
- W640
- W650
- W300 and several N-series products in the broader supplier ecosystem

W640 is independently documented with a 290 mAh battery, IP66 sport chassis and JL7018F + V821-family architecture. W650 is documented with a 220 mAh battery and materially different power/chassis characteristics. These are evidence of a **shared technology/software house**, not proof of one identical model.

These siblings require individual canonical-admission and duplicate checks.

## House 2 — W100 / Ear Dance audio-translation lineage

### Verified market identities

- **EarlySincere** → W100 / Ear Dance. Manuals instruct pairing to a Bluetooth device named W100 and installing Ear Dance.
- **Astrum W100** → W100 / Ear Dance. Astrum directly names W100 and documents Ear Dance plus dual 85 mAh cells.
- **Tiglon TG-W100** → W100 / Ear Dance. Tiglon documents AB5712F + Ear Dance.
- **LEEDOAR-associated W100** → W100 / Ear Dance. Published W100 documentation shows AB5712F, dual 85 mAh cells and Ear Dance.
- **Generic/OEM W100** listings → same platform fingerprint where AB5712F + roughly 170 mAh total + Ear Dance is documented.

Canonical count effect: these retail identities should **not each become separate models**. The underlying W100 platform itself still requires a canonical admission decision if it is not already represented in THE_LIST.

## Platform fingerprint is not identity proof

A shared app, processor or model-number family is evidence for genealogy, not enough by itself to declare identical products. The resolver therefore stores:

1. market identity / alias;
2. canonical model when established;
3. lineage house;
4. confidence;
5. evidence URLs;
6. a human explanation of the relationship.

## Visitor behavior

Expected user path:

`name on box / retailer listing` → `recognized market identity` → `canonical model when established` → `lineage research` → `setup, troubleshooting, development, evidence and related identities`

A visitor searching **BooaBei** should see W610. A visitor searching **EarlySincere** should be told that the product resolves to the W100 / Ear Dance house even before a final canonical GLS identity is established.

## Discovery sources

- https://manuals.plus/ae/1005009589949659
- https://manuals.plus/asin/B0FKG7X84V
- https://manuals.plus/asin/B0GH796VGZ
- https://manuals.plus/ae/1005009590124259
- https://www.starkglasses.com/en/products/horizon_ai-smart-glasses
- https://manuals.plus/asin/B0F4P785KQ
- https://manuals.plus/asin/B0F4P2CZY8
- https://astrumworld.com/product/smart-ai-glasses-w100/
- https://www.tiglonele.com/es/product-page/ai-smart-glasses-tg-w100
- https://manuals.plus/ae/1005008605776017
- https://www.goodwaytechs.com/goodway-w100-ai-bluetooth-smart-glasses-for-translation-audio-calls.html
- https://aiglasses.synteker.com/
- https://www.goodwaytechs.com/goodway-ai-smart-glasses-8mp-sony-cam-ai-translation-hd-video-w640.html
- https://www.goodwaytechs.com/goodway-ai-camera-glasses-hands-free-1080p-video-recording-eyewear-with-ai-assistant-w650.html
- https://manuals.plus/asin/B0GHQ7PQP2

## Follow-on admission queue

Investigate W100, W611 Pro, W620, W630, W640 and W650 as **underlying model candidates**. Their retail aliases should remain separate from model count decisions.
