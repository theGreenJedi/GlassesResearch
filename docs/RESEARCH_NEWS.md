# Research & News

[Who owns the record?](discussions/WHO_OWNS_THE_RECORD.md) examines why independent,
durable documentation matters when products, services, and vendor pages disappear.

<div class="verified-alerts" data-verified-research-alerts markdown>

## Verified Research Alerts

Receive only verified, published GlassesResearch work. Choose what you follow, what you never want, and how often we write. [How Verified Research Alerts work](alerts/README.md).

<form data-verified-research-alerts data-endpoint="https://alerts.glassesresearch.org/subscribe">
  <label for="alerts-email"><strong>Email address</strong></label>
  <input id="alerts-email" name="email" type="email" autocomplete="email" required placeholder="you@example.com">

  <fieldset>
    <legend>Delivery cadence</legend>
    <select name="cadence" required>
      <option value="as_verified">As verified</option>
      <option value="daily">Daily</option>
      <option value="weekly">Weekly</option>
      <option value="monthly">Monthly</option>
      <option value="annually">Annually</option>
    </select>
  </fieldset>

  <div class="alert-grid">
    <fieldset>
      <legend>Follow</legend>
      <label>Models <input name="include_models" type="text" placeholder="W620, Vuzix Z100"></label>
      <label>Brands / lineages <input name="include_brands" type="text" placeholder="HeyCyan, Even Realities"></label>
      <div class="alert-checks">
        <label><input type="checkbox" name="include_topics" value="hacks_development"> Hacks / Development</label>
        <label><input type="checkbox" name="include_topics" value="firmware_software"> Firmware / Software</label>
        <label><input type="checkbox" name="include_topics" value="hardware_teardown"> Hardware / Teardown</label>
        <label><input type="checkbox" name="include_topics" value="privacy_policy"> Privacy / Policy</label>
        <label><input type="checkbox" name="include_topics" value="release_availability"> Releases / Availability</label>
        <label><input type="checkbox" name="include_topics" value="research_science"> Research / Science</label>
        <label><input type="checkbox" name="include_topics" value="standards_regulation"> Standards / Regulation</label>
      </div>
    </fieldset>

    <fieldset>
      <legend>Exclude</legend>
      <label>Models <input name="exclude_models" type="text" placeholder="Ray-Ban Meta"></label>
      <label>Brands / lineages <input name="exclude_brands" type="text" placeholder="Meta"></label>
      <div class="alert-checks">
        <label><input type="checkbox" name="exclude_topics" value="hacks_development"> Hacks / Development</label>
        <label><input type="checkbox" name="exclude_topics" value="firmware_software"> Firmware / Software</label>
        <label><input type="checkbox" name="exclude_topics" value="hardware_teardown"> Hardware / Teardown</label>
        <label><input type="checkbox" name="exclude_topics" value="privacy_policy"> Privacy / Policy</label>
        <label><input type="checkbox" name="exclude_topics" value="release_availability"> Releases / Availability</label>
        <label><input type="checkbox" name="exclude_topics" value="research_science"> Research / Science</label>
        <label><input type="checkbox" name="exclude_topics" value="standards_regulation"> Standards / Regulation</label>
      </div>
    </fieldset>
  </div>

  <p class="alert-note">Exclusions always win. Leave Follow empty to receive all verified research except anything you exclude. Every email links directly to the corresponding published GlassesResearch work and includes Manage subscription / unsubscribe.</p>
  <button type="submit" class="md-button md-button--primary">Subscribe to verified research</button>
  <p class="alert-status" data-alert-status aria-live="polite"></p>
</form>

</div>

## August 11, 2026 — Courts in England and Wales prohibit Meta smart glasses

His Majesty's Courts and Tribunals Service (HMCTS) confirmed that Meta smart glasses are prohibited in court and tribunal buildings because of restrictions on unauthorized recording. According to reporting by *The Guardian*, people entering with the glasses will have them held on entry and returned when they leave.

**Why it matters:** smart glasses are beginning to receive device-specific institutional rules rather than simply inheriting smartphone policy. That matters for social acceptance, privacy, wearability in public institutions, and the practical limits of camera-equipped eyewear.

Source: [The Guardian — Meta glasses banned from courts in England and Wales](https://www.theguardian.com/technology/2026/aug/11/meta-glasses-banned-from-courts-in-england-and-wales)

---

## August 10, 2026 — Meta releases Muse Glimmer for local agent workflows

Meta AI Research released **Muse Glimmer**, a 30-billion-parameter open-weight model optimized for always-on local agent workflows. Meta says the model is designed to run on a Mac or PC with a single consumer GPU, supports interleaved text-and-image input, tool use, multi-step reasoning, failure recovery, and long-context agentic workflows, and is released under the Apache 2.0 license.

For smart glasses, the important point is architectural rather than brand-specific: increasingly capable perception and agent logic can live on hardware controlled by the wearer instead of inside the glasses or exclusively in a vendor cloud.

**Why it matters:** local multimodal agents may allow smart glasses to act primarily as sensors and interfaces while a phone, laptop, or nearby owner-controlled computer provides perception, reasoning, memory, and tool use. That design can materially affect owner control, cloud independence, privacy, hackability, and the useful lifetime of glasses hardware.

Read the GlassesResearch development note: [Local AI Agents and Smart Glasses](../hacking/LOCAL_AI_AGENTS.md).

Primary source: [Meta AI Research — Introducing Muse Glimmer: An Open Agentic Model That Runs on Your Device](https://research.meta.ai/blog/introducing-muse-glimmer-open-agentic-model)

---

## August 6, 2026 — UK venues tighten rules around recording with Meta smart glasses

Restaurants, private clubs, pubs, and theatres in the UK have begun clarifying or enforcing restrictions on recording with smart glasses. *The Guardian* reported that Wetherspoons applies its existing rule against filming customers or employees without permission to Meta glasses; ATG Theatres similarly treats them under its no-filming rules, while other venues have taken stricter approaches.

**Why it matters:** the distinction between banning a device and banning a behavior is important. Smart-glasses adoption will depend not only on technical privacy indicators but also on whether institutions and bystanders can understand and trust what a wearer is doing.

Source: [The Guardian — Restaurants, pubs and theatres ban Meta's 'spy glasses' over privacy fears](https://www.theguardian.com/technology/2026/aug/06/restaurants-pubs-and-theatres-ban-metas-spy-glasses-over-privacy-fears)

---

## December 13, 2025 — Mentra pushes an open, cross-compatible smart-glasses OS

Hackaday highlighted Mentra's open-source smart-glasses operating system and its cross-device compatibility approach. At the time of the report, the compatibility list included Mentra Live, Mentra Mach 1, Vuzix Z100, and Even Realities G1.

**Why it matters:** cross-compatible software directly affects Openness, Owner Control, Cloud Independence, and Hackability. A shared application layer across multiple glasses models reduces the degree to which useful software must remain tied to one manufacturer's hardware or cloud.

Source: [Hackaday — Mentra Brings Open Smart Glasses OS With Cross-Compat](https://hackaday.com/2025/12/13/mentra-brings-open-smart-glasses-os-with-cross-compat/)

---

## October 9, 2025 — Meta Ray-Ban Display teardown exposes repairability limits and waveguide design

Hackaday summarized an iFixit teardown of Meta's Ray-Ban Display glasses. The teardown found that the arms can be opened with heat and expose the battery and internal PCBs, but spare-part availability remains a significant barrier to meaningful repair. The teardown also documents the glasses' geometric reflective waveguide architecture.

**Why it matters:** teardown evidence helps separate theoretical owner control from practical owner control. A device may be physically openable while still being difficult to repair because parts, documentation, firmware access, or calibration tooling are unavailable.

Source: [Hackaday — The Fascinating Waveguide Technology Inside Meta's Ray-Ban Display Glasses](https://hackaday.com/2025/10/09/the-fascinating-waveguide-technology-inside-metas-ray-ban-display-glasses/)

---

## April 1, 2025 — Vuzix receives $500K Augmex smart-glasses reorder

Vuzix announced a $500,000 reorder from Augmex for smart glasses used with Augmex software in warehouse, logistics, field-service, healthcare, and hospital deployments in the UK and Europe. The order followed an earlier six-figure order in December 2024.

**Why it matters:** consumer AI glasses receive most public attention, but enterprise deployments provide a separate measure of whether smart glasses are becoming durable working infrastructure. Repeat orders are particularly useful evidence because they suggest continued operational use rather than a one-off pilot.

Primary source: [Vuzix — $500K Smart Glasses Reorder from Augmex](https://ir.vuzix.com/news-events/press-releases/detail/2121/vuzix-receives-500k-smart-glasses-reorder-from-augmex-to)
