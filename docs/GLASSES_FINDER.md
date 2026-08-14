# Glasses Finder

GlassesResearch contains deep research, but a shopper should not need to read the research corpus before finding plausible candidates.

The Glasses Finder is the simple front door:

**Choose needs → narrow candidates → see where to buy → shortlist → compare → open deep research.**

## Shopper-first filters

### Vision
- Prescription lenses
- Progressive lenses
- Ordinary optician compatible
- Adjustable diopter

### Camera
- Camera
- Takes photos
- Records video
- Live video / streaming

### Audio
- Speakers
- Microphones
- Phone calls
- Music

### Display
- HUD / display
- Full-color display
- Binocular display
- No display

### AI / utility
- AI assistant
- Visual AI
- Translation
- Transcription
- Navigation

### Connectivity / ownership
- Bluetooth
- BLE
- Wi-Fi
- SDK / API
- Open source
- Custom / replaceable AI
- Local or offline operation
- Self-hostable

### Buying
- Available new now
- Under $100 / $250 / $500 / $1,000
- Manufacturer purchase
- Amazon
- Major retailer
- Optical retailer
- Secondary market
- Used hardware

## Advanced filters

The Report Card is an advanced filter layer, not a prerequisite for using the Finder. Each dimension can be independently enabled with a 0–10 minimum threshold:

- Hardware
- Wearability
- Visual AI
- Software
- Display / HUD
- Openness
- Owner Control
- Cloud Independence
- Hackability
- Value

N/A remains semantically distinct from a low score, and unknown remains unknown. A model without a documented Report Card score does not satisfy an enabled minimum.

## Canonical capability matrix

Every one of the 145 canonical `GLS-####` models receives every shopper-facing capability field with one of four states:

- `yes`
- `no`
- `unknown`
- `na`

The Finder consumes this matrix directly. Explicit `yes`, `no`, and `N/A` are authoritative. Only unresolved `unknown` values may fall back to conservative compatibility inference while research continues.

Category-derived negatives are allowed only where the canonical type itself proves them. For example, a device classified as audio-only can safely be treated as no-camera/no-video/no-display; a generic AR/display classification is never assumed camera-less merely because the short type name omits a camera.

## Candidate cards and shortlisting

Each surviving candidate shows only the information needed to decide whether to investigate further:

- maker + exact model / GLS ID
- current / discontinued status
- matched shopper requirements
- known non-matches separately from undocumented requirements
- verified current price observation when available
- purchase-source buttons
- research/report-card/lineage links
- shortlist checkbox

A shopper can shortlist up to four candidates and use one **Compare selected** action to send them into the existing side-by-side comparison engine.

The card does not reproduce the full model article.

## Purchase-source model

Purchase links are separate from research/resource links. Curated purchase records preserve exact GLS model ID, retailer/marketplace, source type, condition, URL, exact-model confidence, availability state, last-verified date, and useful notes.

Current manufacturer/retailer routes remain preferable to marketplace discovery. For secondary markets, durable exact-model marketplace searches are preferred over ephemeral individual listings.

Every canonical model also receives a generated secondary-market continuation route when a curated one does not exist. Generated searches are explicitly discovery fallbacks, not inventory claims, and the shopper is told to verify the exact model before buying.

## Purchase-link health and replacement

Purchase URLs are maintained data rather than permanent assumptions.

A scheduled GitHub Action runs `scripts/check_purchase_links.py` daily and writes `data/purchase-link-health.json`. Each curated route is classified separately as reachable, redirected, dead, unreachable, temporarily failing, unknown, or blocked/rate-limited by the retailer.

The public Finder consumes this ledger. Confirmed-dead purchase buttons are suppressed; bot-blocked, redirected, and temporary-failure routes remain distinct rather than being falsely declared dead. Suspicious routes are written to `research/purchase-link-replacement-queue.md` so an exact-model replacement can be verified before canonical data changes.

The checker deliberately does **not** silently delete or replace canonical purchase URLs.

## Price semantics

Price is volatile evidence, not a permanent model specification.

`data/price-observations.json` contains only currently obtainable, dated acquisition-price observations and drives shopper budget filters. Sold-out, unavailable, or historical observations are preserved separately in `data/price-history.json`; they never satisfy **Under $100 / $250 / $500 / $1,000** filters.

A model with no verified current price remains unknown for price filtering rather than being assigned a stale launch price.

## Comparison

Two to four devices can be compared side by side. **Differences only** removes identical rows, the selected devices are encoded in the URL for sharing, and print mode produces a cleaner comparison view. Price observations, purchase routes and research paths stay attached to selected candidates.

## Validation

The Finder has a dedicated CI gate. It validates:

- exactly 145 canonical GLS IDs;
- Finder schema fields against the generated capability matrix;
- four-state override validity;
- purchase-source IDs, source types, conditions and HTTPS URLs;
- live-price versus price-history semantics;
- secondary-market continuation for every canonical model;
- successful generation of all Finder site data;
- JavaScript syntax for the Finder and its shortlist, purchase-fallback and link-health adapters.

The normal documentation build and catalog-consistency workflows continue to run alongside it.

## Implementation status

### Shopper feature layer — implemented
- grouped Vision, Camera, Audio, Display, AI/utility, Connectivity/ownership and Buying facets;
- live per-filter candidate counts;
- exact-match and near-match modes;
- full 145-model discovery pool;
- canonical `yes / no / unknown / N/A` capability matrix;
- price-band filters backed by dated current observations;
- compact candidate cards with known-vs-unknown mismatch language;
- current manufacturer/retailer purchase buttons where curated;
- secondary-market continuation for all models;
- automated purchase-link health, dead-link suppression and replacement queue;
- shortlist up to four + **Compare selected**;
- two-to-four-device comparison, differences-only, shareable URL and print behavior;
- advanced 0–10 Report Card minimum-score filters;
- mobile-responsive grouped facets;
- dedicated Finder CI gate;
- homepage and navigation promotion so the Finder is a front door rather than a buried research tool.

### Ongoing research/data enrichment
The remaining work is not missing Finder functionality. It is continuous evidence improvement:

1. Resolve more `unknown` capability cells with primary or preserved evidence, especially for older and less documented models.
2. Replace generated marketplace fallbacks with stronger exact manufacturer/retailer routes when legitimate sources are found.
3. Expand dated current-price coverage without importing stale launch prices.
4. Improve inventory/model-match verification beyond URL reachability where retailer behavior permits it.
5. Continue adding new models to the same schema as the ecosystem evolves.

The walls of research remain available downstream. The Finder exists so a shopper can reach the right wall first.