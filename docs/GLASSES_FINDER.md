# Glasses Finder

GlassesResearch contains deep research, but a shopper should not need to read the research corpus before finding plausible candidates.

The Glasses Finder is the simple front door:

**Choose needs → narrow candidates → shortlist → compare → open model research → follow new evidence.**

## Current capability contract

The live Finder currently supports practical-needs filtering, buying-route filtering, verified price-ceiling filters, Report Card minimum-score filters, exact/near-match discovery, purchase-source routes, shortlist checkboxes, and two-to-four-device comparison.

Price filtering uses only current documented acquisition-price observations. A model without a usable observation remains unknown and does not silently pass a budget filter. Report Card thresholds likewise require a documented numeric score; `N/A` and unknown remain distinct from a low score.

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
- Verified price ceilings: under $100, $250, $500, and $1,000
- Manufacturer purchase
- Amazon
- Major retailer
- Optical retailer
- Specialist retailer
- Secondary market
- New / refurbished / used

## Advanced filters

The Report Card is an advanced filter layer, not a prerequisite for using the Finder. Minimum-score controls are live for the numeric dimensions published in the structured Report Card dataset, including:

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

An enabled minimum requires a documented numeric score. `N/A` remains semantically distinct from a low score, and unknown remains unknown.

## Candidate cards

Each surviving candidate shows only the information needed to decide whether to investigate further:

- maker + exact model / GLS ID
- current / discontinued status
- matched shopper requirements
- important unknowns
- verified current price when one is documented
- purchase-source buttons
- shortlist selection
- research/report-card/lineage links

The card does not reproduce the full model article.

## Continue the research

The Finder is deliberately a route, not a destination. A visitor can move from a filtered candidate into its canonical model page, Report Card, lineage/evidence, purchase routes, and comparison. Canonical model pages then expose the next research paths and a **Follow this model** route into Verified Research Alerts, prefilled with the model being researched.

## Purchase-source model

Purchase links are separate from research/resource links. Each purchase record preserves exact GLS model ID, retailer/marketplace, source type, condition, URL, exact-model confidence, observed price when practical, availability state, last-verified date, and useful notes.

For secondary markets, prefer durable exact-model marketplace searches when individual listings are ephemeral. A current-listing layer may highlight individual listings, but permanent model data should not depend on a listing that disappears after sale.

## Purchase-link health and replacement

Purchase URLs are maintained data rather than permanent assumptions.

A scheduled GitHub Action runs `scripts/check_purchase_links.py` daily and writes `data/purchase-link-health.json`. Each route is classified separately as reachable, redirected, dead, unreachable, temporarily failing, unknown, or blocked/rate-limited by the retailer.

Finder purchase buttons consume that health ledger. Confirmed dead routes are suppressed in the visitor interface and queued for replacement; bot-blocked or temporarily failing routes remain distinct from confirmed dead links because an automated check can fail while the retailer page still works for a shopper.

The health ledger proves reachability/freshness only. Exact-model inventory, price and condition require a higher-level verification pass and retain their own last-verified dates.

## Evidence semantics

Filters operate from canonical structured data, not prose scraping. Boolean-like capability fields use yes / no / unknown / N/A semantics. Unknown never silently becomes no. Exact-match filtering excludes unknowns where a requirement cannot be established; near-match mode surfaces the gap instead.

## Implementation status

### Implemented in Finder v3
- grouped shopper facets for Vision, Camera, Audio, Display, AI/utility, Ownership/connectivity, and Buying;
- normalized capability data across the full canonical model pool;
- live per-filter candidate counts;
- exact-match mode plus near-match mode;
- full canonical model discovery pool;
- model/brand/GLS search with verified alias and rebrand routing;
- compact candidate cards;
- purchase-source buttons on candidate cards;
- manufacturer, Amazon and secondary-market routes where populated;
- verified acquisition-price observations and price-ceiling filters;
- Report Card minimum-score filters;
- shortlist checkboxes with one `Compare selected` action for two-to-four models;
- purchase links retained when candidates move into comparison;
- two-to-four-device comparison, differences-only, shareable URL and print behavior;
- mobile-responsive grouped facets;
- canonical purchase-link health ledger and replacement queue;
- Finder suppression of confirmed dead purchase routes while retaining distinct blocked/temporary states;
- daily scheduled link-health checker.

### Next waves
1. Expand legitimate purchase-source coverage across the full living catalog.
2. Expand current verified price observations so budget filters cover more models without guessing.
3. Add higher-level price/inventory/exact-model verification above simple URL health.
4. Reduce remaining unknown capability fields through source-backed research rather than inference.

The walls of research remain available downstream. The Finder exists so a visitor can reach the right wall first.