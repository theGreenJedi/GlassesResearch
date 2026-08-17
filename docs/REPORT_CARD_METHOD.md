# Report Card Method

GlassesResearch Report Cards are evidence-linked technical evaluations, not sponsored rankings. They are designed to make tradeoffs visible without collapsing unlike products into a single winner.

## Dimensions

A Report Card may evaluate these dimensions when evidence supports a judgment:

- **Hardware** — capability and quality of the physical platform: sensing, compute, connectivity, optics, power, and relevant device architecture.
- **Wearability** — fit, mass, balance, conventional-eyewear practicality, prescription accommodation, endurance, and other evidence-backed factors affecting routine wear.
- **Visual AI** — the device's evidence-backed ability to sense and support computation about the wearer's visual environment. A device with no outward-facing camera may be marked N/A rather than penalized for a capability it was not designed to provide.
- **Software** — quality and breadth of the supported software surface, applications, APIs, tooling, updates, and development environment.
- **Display / HUD** — display usefulness where a display exists: optical architecture, field of view, resolution, brightness, binocular/monocular presentation, and practical limitations. Camera/audio glasses without a display may be N/A.
- **Openness** — documented access to protocols, SDKs, source code, schematics, firmware, APIs, or other interfaces that permit independent development and inspection.
- **Owner Control** — how much meaningful control remains with the owner, including application substitution, direct device access, firmware/platform control where available, and freedom from a single prescribed vendor path.
- **Cloud Independence** — how much useful operation survives without the manufacturer's cloud or hosted services. Local or owner-selected services score more strongly than mandatory vendor-cloud dependence.
- **Hackability** — the practical experimentation surface: documented interfaces, debugging/programming access, replaceable software, accessible hardware, community tooling, and reproducible modification paths.
- **Value** — capability and limitations relative to contemporaneous price and alternatives. Value is left ungraded when current pricing evidence is insufficient.

## Scoring scale

Scores use a 0–10 scale with letter grades as a readable shorthand. The numerical score is the primary value; the grade does not add a second hidden calculation.

A high score means the evidence strongly supports that dimension. A low score means evidence supports meaningful limitations in that dimension. **Unknown is not zero. N/A is not zero.** If evidence is insufficient, the field remains unscored.

## No hidden overall weighting

GlassesResearch does **not** currently calculate a single weighted overall winner score. The dimensions are intentionally shown separately because different users value different properties. A developer may care most about openness and hackability; a daily wearer may care most about wearability; a preservation researcher may care about cloud independence and owner control.

If an overall weighting system is introduced in the future, its weights and calculation must be public on this page before the resulting score is published.

## Evidence before score

Every scored judgment must be defensible from the evidence basis associated with the Report Card. Primary sources, direct measurements, reproducible experiments, manuals, firmware, regulatory records, and other authoritative evidence are preferred. Community and secondary evidence must remain clearly distinguished.

The project-wide [Evidence and Confidence Standard](EVIDENCE_STANDARD.md) governs claim status. In particular, **Personally observed** is distinct from independently reproduced **Verified** evidence, and unresolved facts remain **Unknown**.

## Field observations

First-person observations are useful when GlassesResearch actually has the device or a documented experiment. They must be labeled as field observations or personally observed evidence and identify the device context when relevant. They are never inferred from product copy and are never fabricated for devices that have not been handled.

A field observation can describe practical details that specifications miss—pairing behavior, button placement, balance, unexpected friction, visible indicators, companion-app behavior, or other reproducible quirks. It does not automatically generalize to every hardware or firmware revision.

## Lineage and owner-control emphasis

Lineage/OEM relationships, owner control, and cloud independence are first-class research questions because branding alone does not reveal who controls the hardware/software stack or what remains usable if a vendor service disappears. Where evidence exists, Report Cards should connect those judgments to the relevant lineage and technical research rather than treating each branded product as an isolated object.

## Corrections

Scores can change when stronger evidence arrives. Changes should preserve the evidence trail rather than silently rewriting history. See the [Evidence and Confidence Standard](EVIDENCE_STANDARD.md) and [research challenge process](RESEARCH_CHALLENGES.md).