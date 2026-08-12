# Report Card Benchmark Anchors

GlassesResearch uses **one ruler across the entire catalog**. Scores are not normalized within a product category, generation, price class, or manufacturer. A score of 8 in Openness means the same standard whether the device is consumer eyewear, enterprise hardware, a developer kit, or a discontinued historical model.

## Core rule

A **10/10 is a catalog-wide benchmark**, not shorthand for “excellent for this kind of product.” Once a device establishes a defensible 10-level bar, later models must meet or exceed that capability to receive the same score. A later device may raise the bar; if it does, earlier cards must be eligible for recalibration.

Scores describe the evidence available about the device, not manufacturer intent or reputation.

## Common numeric anchors

These anchors apply to every dimension; the dimension-specific definition determines what capability is being measured.

| Score | Meaning |
|---:|---|
| **10** | Benchmark-level: among the strongest documented implementations in the entire catalog, with essentially no material deficiency in the measured dimension. |
| **9** | Exceptional: approaches the benchmark but gives up one meaningful capability, quality, or freedom. |
| **8** | Strong: clearly above the catalog middle and broadly capable, with identifiable limitations. |
| **7** | Good: useful and competent but with several meaningful compromises. |
| **6** | Above weak but mixed: worthwhile capability alongside substantial constraints. |
| **5** | Middle / mixed: neither notably strong nor notably poor on the catalog-wide ruler. |
| **4** | Constrained: important limitations materially reduce usefulness or freedom. |
| **3** | Poor: only limited capability in the dimension. |
| **2** | Very poor: capability exists mostly nominally or through severe restrictions. |
| **1** | Minimal: almost no meaningful capability or owner benefit in the dimension. |
| **0** | Effectively absent despite the dimension being applicable. |

`N/A` means the dimension genuinely does not apply. `Not yet graded` means it applies but the evidence is insufficient. Neither is a numerical score.

## Dimension-specific 10/10 anchors

### Hardware — 10
Best-in-catalog wearable hardware integration for its intended smart-eyewear role: sensing/vision, audio, compute, battery/thermal behavior, controls, connectivity and build are collectively exceptional. A device does not receive 10 merely by maximizing one specification.

### Wearability — 10
Essentially ordinary-eyewear wearability while retaining its smart functions: excellent comfort and balance, low mass/bulk, socially discreet design, practical all-day use, and strong prescription/fit accommodation where relevant.

### Visual AI — 10
Best-in-catalog ability to understand and act on what the wearer sees, combining strong visual sensing with useful contextual processing and access. Native vendor AI is not automatically superior to an owner-controlled vision pipeline; capability and practical usefulness are what matter.

### Software — 10
Exceptional software quality and capability: stable, mature, well-supported, feature-rich, well-documented and broadly integrable, with development tooling where appropriate. Software polish alone cannot substitute for missing capability.

### Display / HUD — 10
Best-in-catalog wearable visual-output experience for the device's role, considering readability, resolution, field of view, brightness, color, refresh, optical quality, latency, binocular/monocular design and practical usefulness. A display-first XR device and discreet HUD are judged on the same capability ruler, not separate category curves.

### Openness — 10
The owner/developer receives unusually complete documented access to the platform. The current benchmark is the **Brilliant Labs Monocle / Frame class**: public firmware/source where applicable, documented protocols/interfaces, schematics/hardware documentation, supported SDK or direct development paths, and low-level programming/debug access. Merely publishing an SDK does not earn 10.

### Owner Control — 10
The owner can meaningfully choose or replace the software and intelligence stack, control device I/O and data paths, deploy their own applications/endpoints, and operate without being confined to a vendor-selected assistant or companion-app workflow. Root-like freedom is more valuable than cosmetic settings.

### Cloud Independence — 10
All core smart-eyewear functions can operate locally or through owner-chosen local/host compute without mandatory manufacturer cloud services. Optional cloud use does not reduce the score; unavoidable vendor-cloud dependence does.

### Hackability — 10
Best-in-catalog practical ability to inspect, modify, experiment with and repurpose the device. The current benchmark is the **Brilliant Labs Monocle / Frame class**: source/firmware access, documented protocols, schematics, low-level debug/programming paths and supported developer tooling. Reverse engineering alone can demonstrate hackability, but supported low-level access is stronger evidence.

### Value — 10
Exceptional capability and ownership utility for the contemporaneous acquisition cost compared with the entire relevant smart-eyewear market. Value is explicitly time-sensitive and must record the price/date basis. Historical MSRP alone is not enough for a current Value score.

## Calibration rules

1. **Cross-category consistency:** never award a score because a device is “good for audio glasses,” “good for enterprise,” or “good for its era.” Historical context belongs in prose; the numerical ruler remains catalog-wide.
2. **Evidence before score:** a high score requires evidence proportional to the claim. Missing evidence produces `Not yet graded`, not optimism.
3. **Benchmark challenge:** when research uncovers a device that clearly exceeds a current 10-point anchor, record the new benchmark and audit existing scores in that dimension.
4. **No ceiling inflation:** several devices may legitimately share a 10 when they meet the same benchmark. A 10 is not reserved for one winner.
5. **No forced curve:** scores describe capability, not rank. The catalog does not need a predetermined number of 10s, 5s or 1s.
6. **Generation specificity:** do not transfer scores between generations unless evidence shows the relevant capability is materially identical.
7. **Source/time specificity:** especially for Value, Software and cloud-dependent features, record when the evidence was checked because these dimensions can change after launch.

## Current benchmark notes

- **Openness:** Brilliant Labs Monocle and Frame currently establish the 10-level reference through unusually deep documented owner/developer access. Brilliant publishes Monocle schematics under CERN-OHL-P Rev 2, reinforcing that this is hardware-level openness rather than an SDK-only claim.
- **Hackability:** Monocle and Frame currently establish the 10-level reference because supported experimentation extends from application code down through firmware/hardware debug paths.

Other dimension benchmarks should be named only after enough catalog-wide research exists to defend them. Until then, use the explicit 10-point definition above rather than prematurely crowning a device.
