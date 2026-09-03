# Ecosystem

Smart glasses are rarely isolated products. They sit inside a stack of platforms, apps, SDKs, transports, services, lineages, and community projects. This surface lets you see that stack as a living system instead of a table of links.

<div class="gr-ecosystem-shell" data-ecosystem-constellation>
  <header class="gr-ecosystem-head">
    <p class="gr-kicker">Ecosystem map</p>
    <h2>See what your glasses depend on.</h2>
    <p class="gr-ecosystem-dek">Select a node to trace the immediate ecosystem around it. Established evidence stays solid; unresolved or inferred relationships remain visually distinct rather than being promoted to fact.</p>
  </header>
  <div class="gr-ecosystem-controls" aria-label="Filter ecosystem map">
    <button type="button" data-ecosystem-filter="all" aria-pressed="true">Everything</button>
    <button type="button" data-ecosystem-filter="hardware" aria-pressed="false">Glasses &amp; lineages</button>
    <button type="button" data-ecosystem-filter="platforms" aria-pressed="false">Platforms &amp; control</button>
  </div>
  <div class="gr-ecosystem-stage">
    <div class="gr-ecosystem-canvas" data-ecosystem-canvas aria-live="polite">
      <p class="gr-ecosystem-noscript">Loading the evidence-backed ecosystem constellation…</p>
    </div>
    <aside class="gr-ecosystem-inspector" data-ecosystem-inspector aria-live="polite">
      <p class="gr-inspector-eyebrow">Trace a relationship</p>
      <h3>Loading relationships…</h3>
      <p>The graph is built directly from the GlassesResearch relationship dataset.</p>
    </aside>
  </div>
  <div class="gr-ecosystem-legend" aria-label="Node legend">
    <span class="model">Glasses</span>
    <span class="platform">Platform</span>
    <span class="developer">SDK / API</span>
    <span class="app">Companion app</span>
    <span class="service">Service</span>
    <span class="community">Community</span>
  </div>
</div>

## Seeded ecosystems

| Ecosystem | Hardware starting points | Connected layers | Research path |
|---|---|---|---|
| HeyCyan | Anko Camera Glasses; W610 | lineage, software platform, companion app, CyanBridge community project | [HeyCyan lineage](../lineages/HEYCYAN.md) |
| Shenzhen reference-platform / manufacturing provenance | W610 and recurring V821/V821L2 camera-glasses families | silicon, solution houses, ODM/factory leads, app operators, commercial suppliers, rebrands | [Supply-chain investigation](SHENZHEN_SMART_GLASSES_SUPPLY_CHAIN.md) |
| Solos | AirGo V2 | AirGo lineage, Solos SDK, BLE control | [Solos lineage](../lineages/SOLOS.md) |
| Even Realities | G2 | Even companion application, cloud AI and translation services | [G2 model research](../models/EvenG2/README.md) |
| Mentra | Mentra Live | MentraOS, SDK, BLE transport, Mentra Community | [Mentra Live in the canonical ledger](../models/THE_LIST.md) |

## Evidence rules

**Established** means cited evidence directly supports the edge. **Inferred** means multiple clues support it but direct confirmation is incomplete. **Unresolved** records a material hypothesis without presenting it as fact. Confidence expresses the strength of the current support independently of whether the source is primary, independent, community-produced, or hands-on.

The map intentionally distinguishes a device that **uses a platform** from one that is merely **compatible with** a project, and a vendor SDK from a community project that supports the same ecosystem.

Manufacturing and design provenance need an additional evidence layer because a seller, app operator, solution house, ODM, tooling owner, and final-assembly factory may all be different organizations. That work lives in [Who Actually Makes These Glasses? Mapping the Shenzhen Smart-Glasses Platform Ecosystem](SHENZHEN_SMART_GLASSES_SUPPLY_CHAIN.md). Manufacturing relationships are not added to the machine graph until evidence supports a specific durable edge.

## Relationship vocabulary

`member_of`, `rebrand_of`, `manufactured_by`, `uses_platform`, `compatible_with`, `requires_app`, `exposes_sdk`, `uses_protocol`, `depends_on_service`, `community_supports`, and `supersedes`.

This layer does not replace the canonical model ledger, comparison data, lineage research, manufacturing-provenance research, or evidence corpus. It indexes relationships among those sources. New nodes and edges must resolve to durable repository research or a direct external resource, and every edge must state its evidence and uncertainty.
