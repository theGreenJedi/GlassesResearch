# Brain-dump investigation — 2026-08-17

This note records the disposition of the user-supplied `braindump.txt` intake tracked by issue #295. Inclusion in the original dump was a discovery lead, not verification. Findings below distinguish repository reconciliation from newly checked external primary sources.

## Model reconciliation

### Everysight Maverick Sport — canonical addition warranted

Primary Everysight product/store/support material establishes Maverick Sport as a distinct, currently purchasable product, separate from Maverick AI / AI Pro. The store lists it at $399 and documents a 43 g frame, 22-degree 640×400 monocular full-color Sony micro-OLED display, Bluetooth 5.2, IP55, approximately 10 hours of operation, iOS/Android compatibility, and an SDK/developer portal.

Starting sources:
- https://www.everysight.com/pages/maverick-sport
- https://www.everysight.com/products/maverick
- https://support.everysight.com/hc/en-us/sections/27996728837404-Using-your-Maverick-Sport

Disposition: cataloged as GLS-0147; do not conflate with Maverick AI or AI Pro.

### Dymesty — three named camera-free products, not one

Dymesty's own catalog enumerates three eyewear products:
- Dymesty AI Glasses Cook Edge
- Dymesty AI Glasses Jobs Circle
- Dymesty AI Sunglasses Moore Vision

Primary catalog/product pages establish direct retail purchase routes and describe the family as camera-free, display-free titanium audio/AI eyewear. The three names should therefore be represented as separate marketed models rather than leaving Cook Edge as a family placeholder. Marketplace copy using phrases such as “recording glasses” refers to audio/meeting recording and must not be interpreted as evidence of an onboard camera.

Starting sources:
- https://dymesty.com/collections/catalog-sales
- https://dymesty.com/products/dymesty-ai-glasses-cook-edge
- https://dymesty.com/products/dymesty-ai-glasses-jobs-circle
- https://dymesty.com/products/dymesty-ai-sunglasses
- https://dymesty.com/pages/titanium-smart-ai-glasses

Disposition: cataloged as GLS-0148 through GLS-0150. Treat detailed performance/AI claims as manufacturer claims until independently tested.

### L'Atitude 52°N — Berlin and Milan require different treatment

The manufacturer explicitly presents Berlin and Milan as two distinct frame designs sharing the same electronics platform. Berlin exposes a purchase route in supported regions. Milan was rechecked on 2026-08-17 and remains explicitly marked `COMING SOON` / `Notify me`; it therefore does not meet this repository's purchaser-history threshold.

Starting sources:
- https://www.latitude52n.com/products/berlin-smart-glasses
- https://www.latitude52n.com/products/milan-smart-glasses
- https://www.latitude52n.com/

Disposition: Berlin cataloged as GLS-0151. Milan remains a distinct pre-release registry entry with no GLS row until an acquisition route exists. This is a completed disposition, not an unresolved issue-295 task.

### INMO — existing catalog was partly right and partly stale

The brain dump did **not** uncover an entirely absent INMO family: `THE_LIST.md` already contains Air, Air 2, GO and Air 3. The useful audit finding is that the current INMO lineup had advanced beyond that ledger.

Primary current INMO material establishes:
- INMO GO2: current support/manual/development documentation; the downloads page explicitly lists GO and GO2 as compatible with the INMO GO app.
- INMO GO3: current manufacturer product page with a direct `Order Now` route and model IMG301.
- INMO Air3: current manufacturer product page and Android/developer SDK material.
- INMO Air2: retained manufacturer product/support material, including an ADB developer-mode path for third-party APK installation.

Starting sources:
- https://www.inmoxr.com/pages/manuals-downloads
- https://support.inmoxr.com/go2/
- https://www.inmoxr.com/pages/inmo-go3-ai-glasses
- https://www.inmoxr.com/pages/inmo-air3
- https://support.inmoxr.com/air2/guides/developer-mode/

Disposition: existing Air/Air2/GO/Air3 identities retained; GO2 and GO3 cataloged as GLS-0152 and GLS-0153; INMO promoted into the research registry with owner-control/developer research signals.

### Walmart titanium AI glasses — resolved as Dymesty retail presentation

The original marketplace lead was preserved because its generic title did not itself establish identity. A fresh marketplace recheck on 2026-08-17 resolves the important part of that ambiguity: Walmart identifies the matching titanium/48-hour AI-glasses listing as **Dymesty**, sold by Dymesty. The listing's 35 g / 1.23 oz titanium frame, Dymesty app, 48-hour battery claim, translation/meeting-recording functions, and prescription-lens path correspond directly to Dymesty's documented titanium family.

This evidence does **not** establish a fourth named Dymesty model. Dymesty's own primary catalog still enumerates Cook Edge, Jobs Circle, and Moore Vision as the named products. The marketplace listing is therefore best treated as a retail/distribution presentation or ambiguous family-level listing, not a new canonical identity.

Disposition: mark the marketplace candidate `duplicate-rebrand`; link it to the Dymesty family; no new GLS ID.

### `rokkid` — resolved as typo/alias noise

A web recheck finds `rokkid` used informally as a misspelling of **Rokid**, including references to Rokid Air. No evidence was found for a distinct smart-glasses company, product family, or model named Rokkid.

Disposition: typo/alias noise for Rokid; no candidate and no GLS row.

## Research/source intake disposition

The remaining brain-dump links were triaged as source classes rather than model identities. Their role is explicit below, so they no longer constitute open issue-295 work merely because they are not all promoted into standalone pages.

### Academic / institutional
ScienceDirect S2949678023000223; MIT Media Lab Smart Eyewear; Project Aria; MDPI Sensors 24(20):6515; Stanford smart-glasses/VR research; Duke Medicine environmental/health smart-glasses work.

Disposition/use: HCI history, sensing architecture, health/environmental implications, privacy, interface design, and research lineage. These are research/evidence inputs, not commercial-specification authorities unless a paper directly measures the device or claim.

### Industry / market / investigative
Citi; Bank of America Institute; IEEE Spectrum `Two Visions for Smart Glasses`; CBC; Grand View Research; Ambiq; Slashdot lead.

Disposition/use: market history, competing architectural visions, adoption narratives, edge-compute trends, and leads to primary evidence. Market and commentary sources do not override manufacturer/regulatory/developer evidence for model specifications.

### User experience / comparative / community
Reddit r/SmartGlasses nine-glasses comparison; owner-use discussion; continuing r/SmartGlasses monitoring; PCMag; TechRadar; Treeview Studio; All About Vision; supplied YouTube IDs; Instagram reel.

Disposition/use: attributed real-world observations, usability/battery/wearability failure modes, and discovery of claims requiring verification. Hands-on testing remains distinguished from commentary, affiliate content, and marketing.

### Retail discovery surfaces
Target Optical, Vision Express, Amazon smart-glasses category, and Walmart marketplace.

Disposition/use: product/availability/rebrand discovery only. Retail presence can establish an acquisition route when identity is clear, but seller copy is not automatically technical truth.

## Process finding and closeout

The most consequential infrastructure finding from this intake was discovery recall: a casual generic web search surfaced multiple named products/families that the news-centric collector had missed. PR #296 repaired that defect by separating ordinary-web, manufacturer, retail, developer, research, community, and durable-watch discovery lanes and retaining the brain dump as a regression benchmark.

PR #297 performed the model/source reconciliation and assigned the seven warranted canonical IDs. Subsequent catalog synchronization inserted those rows into `THE_LIST.md`, derived the actual total automatically, and added CI preventing a `cataloged` candidate from existing without its canonical row.

With the Walmart identity resolved to the existing Dymesty family, Milan explicitly disposed as pre-release, `rokkid` disposed as Rokid typo noise, and every source class assigned a defined research role, issue #295 has no remaining untriaged research obligation. Future changes in Milan availability or newly identified Dymesty/OEM evidence are new discoveries handled by the normal collector/ledger process rather than reasons to keep this intake issue open.