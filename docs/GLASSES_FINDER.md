# Glasses Finder

GlassesResearch contains deep research, but a shopper should not need to read the research corpus before finding plausible candidates.

The Glasses Finder is the simple front door:

**Choose needs → narrow candidates → see where to buy → compare → open deep research.**

## Shopper-first filters

### Vision
- Prescription lenses
- Progressive lenses
- Ordinary optician compatible
- Adjustable diopter

### Camera
- Takes photos
- Records video
- Live video / streaming
- First-person camera

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
- Manufacturer purchase
- Amazon
- Major retailer
- Optical retailer
- Specialist retailer
- Secondary market
- New / refurbished / used
- Price bands

## Advanced filters

The Report Card is an advanced filter layer, not a prerequisite for using the Finder:

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

Each numeric dimension can eventually be constrained by minimum score. N/A remains semantically distinct from a low score, and unknown remains unknown.

## Candidate cards

Each surviving candidate shows only the information needed to decide whether to investigate further:

- maker + exact model / GLS ID
- current / discontinued status
- matched shopper requirements
- important unknowns
- purchase-source buttons
- Add to comparison
- research/report-card/lineage links

The card does not reproduce the full model article.

## Purchase-source model

Purchase links are separate from research/resource links. Each purchase record preserves exact GLS model ID, retailer/marketplace, source type, condition, URL, exact-model confidence, observed price when practical, availability state, last-verified date, and useful notes.

For secondary markets, prefer durable exact-model marketplace searches when individual listings are ephemeral. A current-listing layer may highlight individual listings, but permanent model data should not depend on a listing that disappears after sale.

## Purchase-link health and replacement

Purchase URLs are maintained data rather than permanent assumptions.

A scheduled GitHub Action runs `scripts/check_purchase_links.py` daily and writes `data/purchase-link-health.json`. Each route is classified separately as reachable, redirected, dead, unreachable, temporarily failing, unknown, or blocked/rate-limited by the retailer.

The checker deliberately does **not** silently delete or replace canonical purchase URLs. Suspicious routes are written to `research/purchase-link-replacement-queue.md` so an exact-model replacement can be verified before the canonical dataset changes. Retailers that block automated requests remain distinct from confirmed dead links because a bot-blocked page may still work perfectly for a shopper.

The health ledger proves reachability/freshness only. Exact-model inventory, price and condition require a higher-level verification pass and should retain their own last-verified dates.

## Evidence semantics

Filters operate from canonical structured data, not prose scraping. Boolean-like capability fields use yes / no / unknown / N/A semantics. Unknown never silently becomes no. Exact-match filtering excludes unknowns where a requirement cannot be established; near-match mode surfaces the gap instead.

## Implementation status

### Implemented in Finder v3
- grouped shopper facets for Vision, Camera, Audio, Display, AI/utility, Ownership/connectivity, and Buying;
- live per-filter candidate counts;
- exact-match mode plus near-match mode;
- full canonical model discovery pool;
- compact candidate cards;
- purchase-source buttons on candidate cards;
- manufacturer, Amazon and secondary-market seed routes;
- purchase links retained when candidates move into comparison;
- two-to-four-device comparison, differences-only, shareable URL and print behavior;
- mobile-responsive grouped facets;
- canonical purchase-link health ledger and replacement queue;
- daily scheduled link-health checker that preserves bot-blocked versus actually dead links.

### Next waves
1. Expand purchase-source coverage from the seed set to all 145 models where legitimate acquisition routes exist.
2. Normalize capability fields so fewer filters rely on compatibility aliases/heuristics.
3. Make Finder candidate buttons consume the health ledger, suppressing confirmed dead routes while displaying freshness state for checked links.
4. Add price fields and price-band/range controls.
5. Add Report Card minimum-score controls under Advanced filters.
6. Add selection checkboxes and one `Compare selected` action for shortlist workflows.
7. Add higher-level price/inventory/model-match verification above simple URL health.

The walls of research remain available downstream. The Finder exists so a shopper can reach the right wall first.