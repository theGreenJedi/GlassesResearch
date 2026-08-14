# Glasses Finder & Compare

Start with what you need, not with a brand name.

<div id="comparison-engine-app">
Loading Glasses Finder data…
</div>

## Shop first

The Finder searches the **full canonical smart-glasses ledger**, not a hand-picked shortlist. Choose practical requirements — prescription lenses, video recording, microphones, speakers, display, AI, translation, SDK/API access, offline operation, price, or where you are willing to buy — and the candidate count narrows immediately.

The primary experience is deliberately shopper-first. Someone who wants **prescription lenses + video recording** should be able to reach a useful shortlist without reading the research corpus first.

Filters are grouped into:

- **Vision** — prescription, progressives, ordinary-optician service, adjustable diopter.
- **Camera** — camera, photos, video recording, live video/streaming.
- **Audio** — speakers, microphones, calls, music.
- **Display** — HUD/display, full color, binocular, or no display.
- **AI & utility** — assistant, visual AI, translation, transcription, navigation.
- **Connectivity & ownership** — Bluetooth/BLE, Wi-Fi, SDK/API, open source, custom AI, offline/local operation, self-hosting.
- **Buying** — available new, price bands, manufacturer, Amazon, major/optical retailers, secondary market, and used hardware.

Each basic filter shows a live count so the shopper can see how much a requirement narrows the catalog before clicking it.

## Candidate cards

Results are compact shopping cards rather than mini-articles. They show the exact model and GLS ID, matched requirements, known non-matches separately from undocumented requirements, verified price observations when available, purchase/acquisition links, research paths, and shortlist controls.

Purchase links are intentionally separate from research links. Current manufacturer routes and durable marketplace searches can coexist with secondary-market links for discontinued hardware. A secondary-market search is an acquisition route, not a claim that a specific listing is currently available.

Every canonical model receives a secondary-market continuation route even when no current first-party purchase page exists. Curated exact-model retailer links remain preferable; generated marketplace searches are visibly treated as discovery fallbacks.

When no exact match exists, turn off **Exact matches only** to surface near-matches and models whose relevant capability is still undocumented. The Finder's canonical capability matrix distinguishes `Yes`, `No`, `Unknown`, and `N/A`; unknown is never silently treated as `No`.

## Shortlist and compare

Check up to **four** promising candidates and use **Compare selected** to send the shortlist directly into the side-by-side comparison engine. You can also choose devices directly in the comparison controls.

The **Differences only** switch removes identical rows so the characteristics that separate the candidates are easier to see. The URL records the selected devices, so a comparison can be shared directly. The print control produces a cleaner printable view. Candidate price observations, purchase links and public research paths remain attached to the selected devices.

## Advanced Report Card filters

Open **Advanced filters · Report Card scores** only when you want the research-heavy controls. Each documented Report Card dimension can be enabled independently with a minimum score from 0–10:

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

A model without a documented score does not pass an enabled minimum. N/A remains distinct from a low score, and unknown remains distinct from both. Scores are not invented merely to make filters look complete.

## Freshness and link maintenance

Purchase URLs are maintained data, not static decorative links. The purchase-link health workflow periodically checks known acquisition routes, records freshness/reachability separately, suppresses confirmed-dead links in the Finder, and queues suspicious or dead routes for replacement without silently rewriting canonical evidence.

Price is also treated as volatile evidence. Dated price observations live separately from durable purchase URLs, and a model with no verified price remains unknown for price filtering rather than being assigned a stale launch price.

The Finder data path is protected by a dedicated consistency workflow that validates the canonical model count, checkbox states, purchase and price records, secondary-market continuation coverage, generated site assets, and Finder JavaScript syntax.

See [Glasses Finder architecture](GLASSES_FINDER.md), [Research Standards](RESEARCH_STANDARDS.md), [Technology Lineages](../lineages/README.md), and the [Model Resource Links](../resources/MODEL_RESOURCE_LINKS.md).