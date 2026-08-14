# Glasses Finder & Compare

Start with what you need, not with a brand name.

<div id="comparison-engine-app">
Loading Glasses Finder data…
</div>

## Shop first

The Finder searches the **full canonical smart-glasses ledger**, not a hand-picked shortlist. Choose practical requirements — prescription lenses, video recording, microphones, speakers, display, AI, translation, SDK/API access, offline operation, or where you are willing to buy — and the candidate count narrows immediately.

The primary experience is deliberately shopper-first. Someone who wants **prescription lenses + video recording** should be able to reach a useful shortlist without reading the research corpus first.

Filters are grouped into:

- **Vision** — prescription, progressives, ordinary-optician service, adjustable diopter.
- **Camera** — camera, photos, video recording, live video/streaming.
- **Audio** — speakers, microphones, calls, music.
- **Display** — HUD/display, full color, binocular, or no display.
- **AI & utility** — assistant, visual AI, translation, transcription, navigation.
- **Connectivity & ownership** — Bluetooth/BLE, Wi-Fi, SDK/API, open source, custom AI, offline/local operation, self-hosting.
- **Buying** — available new, manufacturer, Amazon, major/optical retailers, secondary market, and used hardware.

Each filter shows a live count so the shopper can see how much a requirement narrows the catalog before clicking it.

## Candidate cards

Results are compact shopping cards rather than mini-articles. They show the exact model and GLS ID, matched requirements, important missing/undocumented requirements, purchase/acquisition links where populated, a path into the research, and an **Add to comparison** action.

Purchase links are intentionally separate from research links. Current manufacturer routes and durable marketplace searches can coexist with secondary-market links for discontinued hardware. A secondary-market search is an acquisition route, not a claim that a specific listing is currently available.

When no exact match exists, turn off **Exact matches only** to surface near-matches and models whose relevant capability is still undocumented. Unknown is never silently treated as `No` in the research data.

## Then compare

Add promising candidates to the comparison table or choose them directly. Compare **two to four devices** side by side. The **Differences only** switch removes identical rows so the characteristics that separate the candidates are easier to see.

The URL records the selected devices, so a comparison can be shared directly. The print control produces a cleaner printable view. Candidate purchase links and public research paths remain attached above the comparison table.

## Advanced research filters

GlassesResearch also uses a ten-dimension [Report Card](REPORT_CARD.md): **Hardware, Wearability, Visual AI, Software, Display / HUD, Openness, Owner Control, Cloud Independence, Hackability, and Value**.

These belong in the Finder as an advanced layer rather than forcing ordinary shoppers to understand them before searching. Future Finder waves will expose minimum-score controls for the dimensions that have responsibly assigned scores.

N/A remains distinct from a failing score, and unknown remains distinct from both. Missing information is not treated as failure and scores are not invented merely to fill a table.

See [Glasses Finder architecture](GLASSES_FINDER.md), [Research Standards](RESEARCH_STANDARDS.md), [Technology Lineages](../lineages/README.md), and the [Model Resource Links](../resources/MODEL_RESOURCE_LINKS.md).
