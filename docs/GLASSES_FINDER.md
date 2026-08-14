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

Each surviving candidate should show only the information needed to decide whether to investigate further:

- maker + exact model / GLS ID
- current / discontinued status
- matched shopper requirements
- important unknowns
- current price or price range when verified
- purchase-source buttons
- Compare checkbox/button
- View research

The card should not reproduce the full model article.

## Purchase-source model

Purchase links are separate from research/resource links. Each purchase record should preserve:

- exact GLS model ID
- retailer / marketplace
- source type: manufacturer, Amazon, major retailer, optical retailer, specialist retailer, secondary market
- condition: new, refurbished, used, collector/parts where applicable
- URL
- exact-model confidence
- observed price when practical
- availability state
- last-verified date
- notes such as region, carrier, prescription bundle or accessory requirement

For secondary markets, prefer durable exact-model marketplace searches when individual listings are ephemeral. A current-listing layer may highlight individual listings, but permanent model data should not depend on a listing that will disappear after sale.

## Evidence semantics

Filters must operate from canonical structured data, not prose scraping.

Boolean-like capability fields need at least four states:

- yes
- no
- unknown
- N/A

Unknown must never silently become no. Exact-match filtering may exclude unknowns while near-match mode can surface them as `not yet documented`.

## Data architecture

The Finder should consume the same canonical GLS records used by comparison and research layers. New structured domains should include:

1. `capabilities` — shopper-facing yes/no/unknown/N/A fields.
2. `specs` — weight, camera resolution, storage, RAM, FoV, battery and other range-filterable values.
3. `report_card` — normalized 0–10 dimensions plus N/A/unknown.
4. `purchase_sources` — current and secondary-market acquisition routes.
5. `public` — profile, report card, lineage, evidence and resource links.

This avoids maintaining a second hand-curated shopping database.

## Result behavior

Example:

**Prescription lenses ✓ + Records video ✓ + Used okay ✓ + Under $250 ✓**

The result count should narrow immediately as filters change. Exact matches appear first. Near matches may remain visible only when the user allows them, with the missing or unknown requirement clearly identified.

Selected candidates flow directly into the existing side-by-side comparison engine.

## Mission phases

1. Define canonical Finder/filter and purchase-source schema.
2. Map existing structured comparison fields into shopper capabilities.
3. Populate purchase-source records model-by-model, including secondary markets for discontinued hardware.
4. Upgrade the discovery UI into grouped faceted controls with live candidate counts.
5. Add price/range and Report Card advanced filters.
6. Add candidate purchase buttons and Compare Selected workflow.
7. Add freshness auditing for prices, availability and dead purchase links.

The walls of research remain available downstream. The Finder exists so a shopper can reach the right wall first.