# Brain-dump investigation — 2026-08-17

This note records the disposition of the user-supplied `braindump.txt` intake tracked by issue #295. Inclusion in the original dump was a discovery lead, not verification. Findings below distinguish repository reconciliation from newly checked external primary sources.

## Model reconciliation

### Everysight Maverick Sport — canonical addition warranted

Primary Everysight product/store/support material establishes Maverick Sport as a distinct, currently purchasable product, separate from Maverick AI / AI Pro. The store lists it at $399 and documents a 43 g frame, 22-degree 640×400 monocular full-color Sony micro-OLED display, Bluetooth 5.2, IP55, approximately 10 hours of operation, iOS/Android compatibility, and an SDK/developer portal.

Starting sources:
- https://www.everysight.com/pages/maverick-sport
- https://www.everysight.com/products/maverick
- https://support.everysight.com/hc/en-us/sections/27996728837404-Using-your-Maverick-Sport

Disposition: add to `THE_LIST.md` and registry; do not conflate with Maverick AI or AI Pro.

### Dymesty — three named products, not one

Dymesty's own catalog enumerates three eyewear products:
- Dymesty AI Glasses Cook Edge
- Dymesty AI Glasses Jobs Circle
- Dymesty AI Sunglasses Moore Vision

Primary catalog/product pages establish direct retail purchase routes. The three names should therefore be represented as separate marketed models rather than leaving Cook Edge as a family placeholder.

Starting sources:
- https://dymesty.com/collections/catalog-sales
- https://dymesty.com/products/dymesty-ai-glasses-cook-edge
- https://dymesty.com/products/dymesty-ai-glasses-jobs-circle
- https://dymesty.com/products/dymesty-ai-sunglasses

Disposition: add all three to the purchaser-history ledger and registry. Treat detailed performance/AI claims as manufacturer claims until independently tested.

### L'Atitude 52°N — Berlin and Milan require different treatment

The manufacturer explicitly presents Berlin and Milan as two distinct frame designs sharing the same electronics platform. Berlin currently exposes a purchase route at $449 on the manufacturer page. Milan is explicitly marked `COMING SOON` / `Notify me` and therefore does not yet meet this repository's purchaser-history threshold.

Starting sources:
- https://www.latitude52n.com/products/berlin-smart-glasses
- https://www.latitude52n.com/products/milan-smart-glasses
- https://www.latitude52n.com/

Disposition: add Berlin to `THE_LIST.md`; add Berlin and Milan to the research registry, with Milan marked pre-release/not-yet-canonical. Preserve the shared-platform relationship rather than pretending the two frames are unrelated architectures.

### INMO — existing catalog was partly right and partly stale

The brain dump did **not** uncover an entirely absent INMO family: `THE_LIST.md` already contains Air, Air 2, GO and Air 3. The useful audit finding is that the current INMO lineup has advanced beyond that ledger.

Primary current INMO material establishes:
- INMO GO2: current support/manual/development documentation; the downloads page explicitly lists GO and GO2 as compatible with the INMO GO app.
- INMO GO3: current manufacturer product page with a direct `Order Now` / $599 route and model IMG301.
- INMO Air3: current manufacturer product page and Android 14/developer SDK material.
- INMO Air2: retained manufacturer product/support material, including an ADB developer-mode path for third-party APK installation.

Starting sources:
- https://www.inmoxr.com/pages/manuals-downloads
- https://support.inmoxr.com/go2/
- https://www.inmoxr.com/pages/inmo-go3-ai-glasses
- https://www.inmoxr.com/pages/inmo-air3
- https://support.inmoxr.com/air2/guides/developer-mode/

Disposition: preserve existing Air/Air2/GO/Air3 identities, add GO2 and GO3 to the purchaser-history ledger, and promote INMO into the research registry with explicit owner-control/developer research signals. Separately update stale `inmoglass.com` starting links toward current `inmoxr.com` material when touched.

### Walmart titanium AI glasses — unresolved OEM/rebrand lead

The marketplace title is insufficient to establish a canonical identity. Keep the lead in `data/model-candidates.json` as commercial/OEM investigation material until seller, brand/model number, upstream OEM/ODM, and possible rebrand relationships are resolved.

Disposition: no GLS ID yet.

### `rokkid`

The bare term remains insufficient evidence of a distinct entity. Given the already-cataloged Rokid family, treat this as an unresolved likely typo until the original context establishes otherwise. Do not create a model or organization from the string alone.

## Research/source intake disposition

The rest of the brain dump is valuable even where it does not create model rows. Preserve the source classes below as investigation inputs:

### Academic / institutional
ScienceDirect S2949678023000223; MIT Media Lab Smart Eyewear; Project Aria; MDPI Sensors 24(20):6515; Stanford smart-glasses/VR research; Duke Medicine environmental/health smart-glasses work.

Use for: HCI history, sensing architecture, health/environmental implications, privacy, interface design, and research lineage. These sources should support research chapters/evidence records, not commercial specifications unless the paper itself measures the device/claim.

### Industry / market / investigative
Citi; Bank of America Institute; IEEE Spectrum `Two Visions for Smart Glasses`; CBC; Grand View Research; Ambiq; Slashdot lead.

Use for: market history, competing architectural visions, adoption narratives, edge-compute trends, and identifying primary sources. Do not let market reports override manufacturer/regulatory/developer evidence for model specifications.

### User experience / comparative / community
Reddit r/SmartGlasses nine-glasses comparison; owner-use discussion; continuing r/SmartGlasses monitoring; PCMag; TechRadar; Treeview Studio; All About Vision; supplied YouTube IDs; Instagram reel.

Use for: attributed real-world observations, usability/battery/wearability failure modes, and discovery of claims requiring verification. Classify hands-on testing separately from commentary, affiliate content, and marketing.

### Retail discovery surfaces
Target Optical, Vision Express, Amazon smart-glasses category, and Walmart marketplace.

Use for: product/availability/rebrand discovery only. Retail presence can establish a commercial acquisition route when identity is clear, but seller copy is not automatically technical truth.

## Process finding

The most consequential finding from this intake was discovery recall: a casual generic web search surfaced multiple named products/families that the news-centric collector had missed. PR #296 repaired that infrastructure defect by separating ordinary-web, manufacturer, retail, developer, research, community, and durable-watch discovery lanes and retaining the brain dump as a regression benchmark.

Issue #295 remains responsible for converting the actual leads into verified catalog/research content. This note is the evidence-backed disposition record for that work.