# EV-0035 — Lucyd Lyte generation history

Verified: 2026-08-13
Source class: regulatory/company primary
Confidence: confirmed
Scope: Lucyd Lyte commercial generation naming

## Sources
- Innovative Eyewear SEC filing (2024): https://www.sec.gov/Archives/edgar/data/1808377/000182912624004135/innovativeeyewear_424b5.htm
- Innovative Eyewear SEC filing (2024): https://www.sec.gov/Archives/edgar/data/1808377/000182912624004084/innovativeeye_s1a1.htm
- Lucyd / Innovative Eyewear 2023 year-end review: https://lucyd.co/blogs/blog/innovative-eyewear-inc-2023-year-end-review

## Finding
Innovative Eyewear's SEC disclosures establish this commercial sequence:

1. **Lucyd Lyte / Lyte 1.0** — commercial launch January 2021.
2. **Lucyd Lyte 2.0** — launched February 2023 with 15 styles, four-speaker audio, 12-hour music/call time, improved styling and technical upgrades.
3. **Lucyd Lyte XL** — launched October 2023 as six new styles with flexible hinges, improved speaker/microphone quality, thinner/more ergonomic temples and wider-fit positioning.

The company's filings repeatedly describe the product line in these terms. No primary company or SEC source located in this investigation identifies **Lyte 2.1** or **Lyte 2.3** as separately launched hardware generations.

SEC filings also provide unusually strong optical-serviceability evidence: the company states its frame fronts are designed for easy lens fitting by any optician, and that all frames can be fitted with prescription, sunglass, reading and blue-light lens formats. This is evidence of ordinary independent optical serviceability rather than merely vendor-sold prescription availability.

## Catalog implication
Reconciliation is complete. `GLS-0032 — Lyte 2.1` is retired from the canonical model count because no distinct commercial generation is supported. `GLS-0033` now maps to the defensible October 2023 successor, **Lyte XL**; its former `Lyte 2.3` label is unsupported. Neither row inherits Lyte 2.0 scores.

Both former labels and their disposition are preserved in `models/CATALOG_CORRECTIONS.md`, so the correction is explicit and reversible if new primary acquisition evidence appears.

## Ownership implication
Lucyd's ordinary-optician fitting statement materially strengthens Optical Serviceability / Owner Control for the Lyte family. Core audio remains standard Bluetooth architecture; firmware/system openness remains a separate question.
