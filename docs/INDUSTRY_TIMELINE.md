# Smart-Glasses Industry Timeline

The **GlassesResearch Smart-Glasses Industry Timeline** is a living, evidence-backed historical graph of major product, company, technology, open-source, regulatory, research, and GlassesResearch milestones.

The uncluttered default view emphasizes significance **4–5** events. Use the filters to reveal the deeper chronology, GlassesResearch milestones, and automatically discovered primary-source signals.

<div id="industry-timeline-app"></div>

## How to read the graph

Marker size reflects the event's **significance score**. Solid markers are events that occurred. Outlined markers represent announced future milestones. Delayed and cancelled milestones retain their place in history rather than disappearing. Automatically discovered items are shown as a separate **Live signal** state until reviewed and promoted into the canonical historical record.

Every canonical event has a stable `TL-####` identifier. Selecting a marker exposes its sources and a permalink, so a reporter, researcher, or another website can cite a specific milestone rather than linking only to the homepage.

## Significance scale

| Score | Meaning | Main graph behavior |
|---|---|---|
| **5** | Industry-changing | Always prominent |
| **4** | Major | Prominent by default |
| **3** | Important | Visible when the threshold is expanded |
| **2** | Minor but historically useful | Detailed chronology |
| **1** | Routine | Retained only when useful to the historical record |

Significance is not a product rating. It describes how much an event changed the smart-glasses ecosystem or the way the ecosystem is understood.

## A living record, not a frozen poster

The canonical timeline lives in [`timeline/events.json`](../timeline/events.json). A scheduled primary-source watcher checks configured industry feeds and writes newly discovered relevant items into [`timeline/auto-events.json`](../timeline/auto-events.json) as **provisional live signals**.

Automation is deliberately conservative. Discovery is automatic; historical authority is not. A press release can appear quickly as a live signal, but it does not receive a permanent `TL-####` identity until its source, date, relevance, and significance have been reviewed. Future announcements remain distinguishable from events that actually happened, and delays or cancellations are recorded instead of silently rewriting the past.

This design lets the graph keep pace with the industry without lowering the evidence standard that makes the timeline worth citing.

## Historical interpretation

### Consumer form factor became part of the technology

Early head-mounted systems proved many technical concepts, but consumer adoption repeatedly exposed a second engineering problem: people have to be willing to wear the device. Ray-Ban Stories and later Ray-Ban Meta generations made conventional eyewear design, social acceptability, camera signaling, weight, battery placement, and companion-phone integration part of the core smart-glasses problem rather than peripheral styling questions.

### The market split into several different product classes

"Smart glasses" now includes camera-and-audio eyewear, discreet notification displays, tethered private displays, enterprise assisted-reality devices, standalone AR systems, and developer-oriented open platforms. Treating all of them as one interchangeable category obscures the industry's actual evolution. The timeline therefore links milestones back to canonical device identities where possible.

### AI changed expectations faster than optics did

The 2023–2026 period accelerated the shift from capture and notifications toward conversational assistance, translation, visual understanding, and agent-like behavior. Many of those capabilities still depend heavily on a phone or cloud service, which makes privacy, continuity, vendor dependence, and user control historically important alongside camera resolution or display technology.

### Platform competition is re-emerging

Snap OS, Android XR, vendor SDKs, community software, and open-hardware projects show that the future of smart glasses is also a platform contest. The durable historical question is not only which frame sold best, but which hardware and software ecosystems allowed useful capabilities to survive vendor pivots and product discontinuation.

## Citation and reuse

When citing the overall visualization, use:

> **GlassesResearch Smart-Glasses Industry Timeline**, GlassesResearch, https://glassesresearch.org/docs/INDUSTRY_TIMELINE/

For a particular milestone, select it in the graph and use the generated `#TL-####` permalink. Cite the underlying primary source as well when the specific factual claim matters.

The machine-readable canonical record is available at:

`https://glassesresearch.org/timeline/events.json`

The provisional live-signal feed is available at:

`https://glassesresearch.org/timeline/auto-events.json`

## Editorial rules

- Prefer primary, regulatory, repository, and original research sources.
- Preserve disagreement and uncertainty instead of forcing a clean narrative.
- Never convert absence of evidence into evidence of absence.
- Keep announced future events visually and semantically distinct from occurred history.
- Record delays and cancellations rather than deleting inconvenient predictions.
- Deduplicate repeated coverage of the same underlying announcement.
- Give stable IDs only to canonical events.
- Keep routine product news from overwhelming the main graph by using significance thresholds.
- Link device milestones to `GLS-####` records whenever identity is established.

## Coverage backlog

The graph is now a maintained system, but historical depth remains an active research program. High-priority additions include early wearable-computing laboratories, Google Glass editions and enterprise lifecycle, Vuzix and Epson generations, North Focals, RealWear, Bose Frames, Echo Frames, Snap Spectacles generations, XREAL/Nreal, Rokid, VITURE, RayNeo, Brilliant Labs, Even Realities, Solos, Halliday, Mentra, regulatory milestones, major privacy controversies, and well-sourced open-source or reverse-engineering breakthroughs.
