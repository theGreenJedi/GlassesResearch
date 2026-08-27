# Retail Rebrands & OEM Ecosystems

Smart glasses are often sold under a retail, marketplace, or house brand that is different from the company providing the underlying hardware, firmware, companion application, or cloud service. This index tracks those relationships when there is concrete evidence for them.

**Searchable market identities do not automatically add to the canonical model count.** If several seller names resolve to one underlying platform, GlassesResearch counts that platform once while preserving every verified name a purchaser may see on a box, retailer page, Bluetooth menu, or manual.

A shared application or software platform is evidence of an ecosystem relationship, **not automatically proof of identical hardware**. Hardware-equivalence claims require stronger evidence such as regulatory filings, board/component identification, firmware compatibility, matching device identifiers, or reproducible hands-on testing.

## Documented retail identities and platform relationships

| Retail brand / model | Underlying identity / house | Count behavior | Evidence / research |
|---|---|---|---|
| BooaBei | W610 / HeyCyan | Alias; does not add a model beyond GLS-0039 | [HeyCyan lineage](../lineages/HEYCYAN.md) |
| Zbna W610 | W610 / HeyCyan | Alias; does not add a model beyond GLS-0039 | Published manual identifies W610 (M02); [HeyCyan lineage](../lineages/HEYCYAN.md) |
| Mingtawn W610 | W610 / HeyCyan | Alias; does not add a model beyond GLS-0039 | Published W610 manuals require HeyCyan; [HeyCyan lineage](../lineages/HEYCYAN.md) |
| ESTG W610 | W610 / HeyCyan | Alias; does not add a model beyond GLS-0039 | Published W610 documentation matches the W610 platform; [HeyCyan lineage](../lineages/HEYCYAN.md) |
| STARK Horizon | Strong W610 market-identity match | No additional count while W610 remains the supported underlying identity | STARK product material calls the underlying glasses `STARK W610`; [HeyCyan population research](../lineages/HEYCYAN_POPULATION.md) |
| Anko Camera Glasses | HeyCyan software ecosystem; hardware equivalence to W610 not established | Already canonical as GLS-0120 because it crossed the acquisition/identity threshold independently | [Anko Camera Glasses](AnkoCameraGlasses/README.md) |
| EarlySincere | W100 / Ear Dance | Retail identity; no separate count | Manuals pair to Bluetooth device `W100`; [W100 / Ear Dance lineage](../lineages/W100_EARDANCE.md) |
| Vital Smart Glasses | W100 / Ear Dance | Retail identity; no separate count | Setup documentation pairs to `W100` and uses Ear Dance; [W100 / Ear Dance lineage](../lineages/W100_EARDANCE.md) |
| Astrum W100 | W100 / Ear Dance | Retail identity; no separate count | Astrum directly names W100 and Ear Dance; [W100 / Ear Dance lineage](../lineages/W100_EARDANCE.md) |
| Tiglon TG-W100 | W100 / Ear Dance | Retail identity; no separate count | Tiglon documents W100/AB5712F/Ear Dance; [W100 / Ear Dance lineage](../lineages/W100_EARDANCE.md) |
| LEEDOAR-associated W100 | W100 / Ear Dance | Retail identity; no separate count | W100 documentation identifies AB5712F + Ear Dance; [W100 / Ear Dance lineage](../lineages/W100_EARDANCE.md) |
| Giinova W630 | W630 / HeyCyan sibling platform | Retail identity of W630; not a W610 alias | Manual identifies W630 + HeyCyan; Goodway separately documents W630 architecture; [HeyCyan population research](../lineages/HEYCYAN_POPULATION.md) |
| GUHUAVMI W630 | W630 / HeyCyan sibling platform | Retail identity of W630; not a W610 alias | Manual identifies W630 + HeyCyan/Bluetooth/Wi-Fi; [HeyCyan population research](../lineages/HEYCYAN_POPULATION.md) |
| VITURE Phantom Beast | VITURE Beast / GLS-0082 | Co-branded derivative alias; does not add a model beyond GLS-0082 | VITURE states that the collector's edition retains Beast's core XR hardware; [VITURE Beast](PROFILES_XR_DISPLAY_02.md#gls-0082-viture-beast); [evidence](../evidence/EV-0086-VITURE-Phantom-Beast-primary-derivative.md) |

The machine-readable resolver used by Finder lives in [`data/lineage-aliases.json`](../data/lineage-aliases.json). It preserves the market name, canonical identity where established, lineage, confidence, sources, and the explanation shown to a visitor.

## How to use this index

If your glasses are sold under a name that is not in the canonical model list, **search the name printed on your box or retailer order anyway**. When a verified relationship exists, GlassesResearch should lead you into the underlying model or lineage research and explain the relationship instead of returning a dead end.

A shared lineage does not mean every seller variant is byte-for-byte identical. Frame construction, lenses, battery, firmware revision, packaging, accessories, regional configuration, and seller-specific software can differ. Those differences remain attached to the market identity when documented.

## HeyCyan ecosystem

The current research distinguishes at least two kinds of relationship inside HeyCyan:

1. **W610 market identities** such as BooaBei, Zbna W610, Mingtawn W610 and ESTG W610, which resolve back to canonical GLS-0039.
2. **Distinct sibling platforms** such as W611 Pro, W620, W630, W640 and W650. These may share HeyCyan and sometimes silicon families with W610, but they are not collapsed into W610 without hardware-equivalence evidence.

That distinction prevents both over-counting seller labels and under-counting genuinely different hardware.

Useful cross-links:

- [W610 / HeyCyan](W610/README.md)
- [HeyCyan lineage](../lineages/HEYCYAN.md)
- [HeyCyan populated research](../lineages/HEYCYAN_POPULATION.md)
- [W100 / Ear Dance lineage](../lineages/W100_EARDANCE.md)
- [HeyCyanSmartGlassesSDK](https://github.com/ebowwa/HeyCyanSmartGlassesSDK)
- [CyanBridge / Alternative HeyCyan App and SDK](https://github.com/FerSaiyan/Alternative-HeyCyan-App-and-SDK)
- [Community & Development](../resources/COMMUNITY_AND_DEVELOPMENT.md)

## Representative sources

- https://manuals.plus/asin/B0FLYTMCKP
- https://www.vital-glasses.com/
- https://astrumworld.com/product/smart-ai-glasses-w100/
- https://manuals.plus/asin/B0F4P785KQ
- https://manuals.plus/asin/B0GFD7H446
- https://www.goodwaytechs.com/ai-camera-glasses-w630.html
- https://www.theguardian.com/australia-news/2026/aug/04/kmart-camera-glasses-anko-meta-smartglasses-australia
