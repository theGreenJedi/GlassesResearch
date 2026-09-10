# Identity Forensics — Wave 03

**Date:** 2026-09-10  
**Trigger:** fresh competitor/reference sweep against the current GlassesResearch corpus  
**Baseline:** 239 active canonical smart-glasses records; highest allocated smart-glasses ID `GLS-0240`

This pass rechecks externally surfaced names against first-party or transaction evidence before changing the canonical ledger. Competitor catalogs are discovery aids only. A name is admitted only when GlassesResearch independently establishes product identity, a qualifying acquisition route, and the correct form-factor shelf.

## Finding 1 — Thunderbird / RayNeo Air 1S is a missing sold generation

**Final disposition: admit as `GLS-0241`.**

RayNeo's own October 20, 2022 announcement calls **Thunderbird Air 1S** a *new generation* of consumer XR glasses, gives a list price of CNY 2,499, and states that presales opened on JD and Tmall. The same first-party announcement distinguishes it from the original Air through a new Sony MicroOLED generation, upgraded audio, revised industrial design, volume/brightness controls, a 2D/3D switch, and a detachable magnetic cable.

Primary evidence:

- RayNeo launch record: https://www.rayneo.cn/xinwen/352.html
- RayNeo's current firmware-upgrade service independently lists **RayNeo Air 1s** as a supported model, separately from Air Plus, Air 2, Air 2s, Air 3, Air 3s and later products: https://ota.rayneo.com/

### Identity boundary

Air 1S is not merely a regional spelling or color of `GLS-0087` RayNeo Air. The manufacturer explicitly presents it as a new generation and documents multiple hardware/interface changes. The paid preorder route satisfies the purchaser-history threshold even though the model is no longer a current flagship.

**Canonical action:** `GLS-0241` — RayNeo / Thunderbird Air 1S — 2022 — legacy/support — tethered XR display glasses — China preorder/retail.

## Finding 2 — Thunderbird / RayNeo Air Plus is another missing sold generation

**Final disposition: admit as `GLS-0242`.**

A surviving first-party RayNeo product page names **Air Plus**, exposes a `Buy Now` route to JD, and documents a 49° FOV, up to 120 Hz refresh, 600 nit eye brightness claim, prescription-lens attachment and host connectivity across phones, computers and consoles. RayNeo's current firmware updater lists Air Plus separately from Air 1S and Air 2.

Primary and corporate evidence:

- Preserved RayNeo Air Plus product page with purchase route: https://test.rayneo.cn/airplus/
- Current RayNeo OTA supported-model list: https://ota.rayneo.com/
- TCL Electronics' 2023 interim report states that the Group launched the upgraded XR smart glasses **Air Plus** in the PRC during the first half of 2023: https://www1.hkexnews.hk/listedco/listconews/sehk/2023/0825/2023082500287.pdf

Contemporaneous launch reporting independently records a May 18, 2023 launch and CNY 2,499 pricing, but it is supporting evidence rather than the admission authority: https://www.ithome.com/0/693/486.htm

### Identity boundary

Air Plus is not a bundle name for Air 1S plus RayNeo Pocket. The manufacturer preserves an Air Plus eyewear product page and the current firmware service recognizes Air Plus as its own device identity. RayNeo Pocket remains an accessory/host.

**Canonical action:** `GLS-0242` — RayNeo / Thunderbird Air Plus — 2023 — legacy/support — tethered XR display glasses — China retail.

## Finding 3 — MAD Gaze GLOW and GLOW Plus both crossed purchaser history

**Final disposition: admit two distinct marketed eyewear identities as `GLS-0243` and `GLS-0244`.**

The previous AR Compare intake correctly refused to admit GLOW Plus on an external catalog listing alone. The missing transaction history has now been reconstructed.

MAD Gaze's Kickstarter campaign raised HKD 1,641,790 from 399 backers. Its surviving FAQ explicitly refers to **GLOW and GLOW Plus**, promises shipment beginning in November 2019, states that both carry a one-year warranty, and describes the SDK/sensor access. The later Japanese CAMPFIRE campaign provides especially clean product-specific transaction evidence: separate paid reward tiers for **GLOW** and **GLOW PLUS**, with distinct prices, backer counts and delivery windows.

Evidence:

- MAD Gaze Kickstarter campaign: https://www.kickstarter.com/projects/madgaze/mad-gaze-glow-lightweight-and-stylish-mr-glasses-for-you
- MAD Gaze Kickstarter FAQ naming GLOW / GLOW Plus, shipping and warranty: https://www.kickstarter.com/projects/madgaze/mad-gaze-glow-lightweight-and-stylish-mr-glasses-for-you/faqs
- CAMPFIRE paid reward tiers for GLOW and GLOW PLUS: https://camp-fire.jp/projects/248361/view
- Follow-on CAMPFIRE campaign with additional GLOW PLUS reward transactions: https://camp-fire.jp/projects/281919/view
- MAD Gaze Japan support note preserving separate GLOW and GLOW PLUS manuals and model differences: https://note.com/madgaze_japan/n/n664d9a804036

### Hardware boundary

The two names are not cosmetic tiers. Preserved product/support material distinguishes the optical/display architectures and capabilities: GLOW supports 3D content, while GLOW Plus does not; the Plus uses a different optical design, is brighter and more power-efficient, and provides a larger field of view. Contemporary product documentation further distinguishes 720p / roughly 45° GLOW from 1080p / roughly 53° GLOW Plus. Both are phone/host-powered eyewear rather than standalone compute devices.

**Canonical actions:**

- `GLS-0243` — MAD Gaze GLOW — 2019 — legacy — tethered AR/MR smart glasses — crowdfunding/retail.
- `GLS-0244` — MAD Gaze GLOW Plus — 2019/2020 — legacy — tethered AR/MR smart glasses — crowdfunding/retail.

The catalog split records two separately marketed hardware configurations. It does not imply that every subsystem differs.

## Finding 4 — RealMax Qian is real and acquired, but belongs on the adjacent shelf

**Final disposition: admit as `ADJ-0017`, not a `GLS-` row.**

RealMax Qian clearly crossed an acquisition threshold. Its Kickstarter offered paid Qian Light and Standard reward tiers, and the manufacturer's surviving storefront still names Qian, calls it a standalone AR headset, and exposes an order surface. Independent owners documented delivered units in 2020–2021.

Evidence:

- RealMax Qian Kickstarter FAQ and reward/version description: https://www.kickstarter.com/projects/realmax100/realmax-qian-the-1008-fov-ar-glasses-for-a-more-immersive/faqs
- Manufacturer storefront/product route: https://realmax.myshoplaza.com/products/realmax-qian-immersive-ar-glasses-with-ultra-large-fov
- Independent delivered-unit report: https://discussions.unity.com/t/realmax-qian-the-ar-glasses-with-immersive-119-3-fov-unedited-video-filmed-via-phone/806225
- Independent hands-on review of delivered hardware: https://skarredghost.com/2021/02/11/realmax-qian-review-wide-fov-ar/

### Form-factor boundary

The site's taxonomy puts devices fundamentally worn as glasses in `GLS-`, while headsets/goggles belong in the adjacent wearable-HCI catalog. RealMax itself repeatedly calls Qian a **standalone AR headset**; its bulky integrated compute/optical assembly can fit over ordinary prescription glasses and can be converted toward VR with a front shield. Independent hands-on sources likewise describe it as a headset rather than ordinary eyeglass-frame eyewear.

Qian Light and Qian Standard do **not** receive separate adjacent IDs. RealMax's own FAQ says the Standard tier primarily adds accessories — including the magnetic VR cover, power adapter, Leap Motion holder and cable — rather than establishing a second core headset generation.

**Adjacent action:** `ADJ-0017` — RealMax Qian — 2020 — legacy — standalone AR/VR headset — crowdfunding/retail.

## Finding 5 — RayNeo X2 Lite should be preserved, not counted

**Final disposition: research/lineage prototype only; no `GLS-` ID.**

RayNeo publicly demonstrated **X2 Lite** at CES 2024, but the first-party release described the demonstration and future crowdfunding intent rather than a completed acquisition route. Contemporary hands-on coverage likewise identified it as prototype hardware. It should be retained in RayNeo lineage history and discovery monitoring without inflating the purchaser-history count.

Primary evidence:

- RayNeo CES 2024 release: https://www.prnewswire.com/news-releases/rayneo-demos-ultralight-x2-lite-ar-glasses-for-the-first-time-announcing-crowdfund-campaign-for-the-rayneo-x2-ar-glasses-at-ces-2024-302028818.html

Current historical overview also preserves 2024 X2 Lite as a development milestone: https://www.quanchu.com.cn/content/dam/sitebuilder/rxch/quanchu/2025/9/16/%E8%89%BE%E7%91%9E%E5%92%A8%E8%AF%A2-2025%E5%B9%B4%E4%B8%AD%E5%9B%BDAI%E7%9C%BC%E9%95%9C%E8%A1%8C%E4%B8%9A%E7%A0%94%E7%A9%B6%E6%8A%A5%E5%91%8A.pdf.coredownload.579939865.pdf

## Competition-derived site audit correction

The same sweep exposed three apparent feature gaps that were already partly solved inside GlassesResearch:

1. **Host compatibility already exists.** `docs/HOST_COMPATIBILITY.md` and `data/host-compatibility.json` already define an evidence-backed host/glasses compatibility model. The real gap is population: the structured dataset currently contains only an initial XREAL One-family transport seed rather than broad named-host coverage.
2. **Prescription guidance already exists.** The generated guide system includes a prescription-compatible guide and the Finder exposes prescription filtering. The real gap is field depth: a binary `prescription_support` capability cannot yet express direct glazing vs insert vs over-glasses, sphere/cylinder limits, IPD/PD constraints, progressives/bifocals, or evidence confidence.
3. **`CITATION.cff` already exists.** The prior competition note saying it appeared absent was a search miss. The remaining scholarly-publishing opportunity is DOI/version archiving (for example Zenodo), not creation of a citation file from scratch.

These corrections matter because competitor review should improve GlassesResearch without erasing work already completed.

## Wave 03 disposition summary

| Identity / opportunity | Result | Reason |
|---|---|---|
| RayNeo / Thunderbird Air 1S | **Admit — GLS-0241** | First-party new-generation launch + paid preorder + current firmware identity. |
| RayNeo / Thunderbird Air Plus | **Admit — GLS-0242** | First-party product/purchase surface + corporate launch record + current firmware identity. |
| MAD Gaze GLOW | **Admit — GLS-0243** | Paid crowdfunding transaction history and distinct product identity. |
| MAD Gaze GLOW Plus | **Admit — GLS-0244** | Paid crowdfunding transaction history + materially distinct optical/display configuration. |
| RealMax Qian | **Adjacent — ADJ-0017** | Acquired product, but physically a standalone AR/VR headset rather than eyeglass-frame smart glasses. |
| RayNeo X2 Lite | **Registry/lineage only** | Demonstrated prototype; no qualifying acquisition route established. |
| Host Compatibility Center | **Already exists; deepen** | Framework is present; named-host population is thin. |
| Prescription & Fit | **Already exists; deepen** | Guide/filter exists; schema is too binary for optical-fit decisions. |
| CITATION.cff | **Already exists** | DOI/version-archive integration remains the useful next step. |

## Count impact

If the accompanying canonical reconciliation is merged and mechanically synchronized, the active smart-glasses population advances from **239 to 243**. Stable IDs extend through `GLS-0244`. The adjacent wearable-HCI catalog gains one entry, `ADJ-0017`, without affecting the smart-glasses count.

## Evidence boundary

This wave establishes identity, acquisition history, and catalog shelf. It does not independently validate manufacturer display, brightness, FOV, comfort, durability, software, privacy, SDK, compatibility, optical-safety, or owner-control claims. Manufacturer specifications are retained as provenance-bound claims until independently tested.