# Display-glasses market gap audit — 2026-09-04

## Trigger

A current Alibaba listing for the CORNMI NeoVista A8 Lite exposed a category question larger than the listing itself: does GlassesResearch adequately cover the host-driven personal-display / cinema-glasses branch, and are there commercially sold display models missing from the purchaser-history ledger?

This investigation therefore treats A8 Lite as the lead, not the scope.

## Method

The audit collision-checked the current canonical ledger and existing research before proposing new identities. Existing XREAL Air/One, VITURE One/Pro/Luma/Beast, TCL NXTWEAR G/G+/S/S+, RayNeo Air-family, Rokid Air/Max and Epson Moverio records were treated as already covered and were not re-created.

Admission followed the existing purchaser-history rule: a distinct model needs an evidence-backed paid acquisition route. Announced, demonstrated or concept-only hardware remains research-only even when the industrial design appears production-ready.

## Result

Eleven missing commercially obtainable display-glasses identities qualify for canonical admission:

| Proposed ID | Maker | Model | Architectural lane | Admission basis |
|---|---|---|---|---|
| GLS-0171 | CORNMI | NeoVista A8 Lite | tethered personal display | direct manufacturer store + OEM marketplace |
| GLS-0172 | CORNMI | NeoVista X7 Lite | tethered personal display | direct manufacturer store |
| GLS-0173 | CORNMI | NeoVista X7 | tethered personal display | direct manufacturer store |
| GLS-0174 | CORNMI | NeoVista X7 Pro | Android-enabled XR display | direct manufacturer store |
| GLS-0175 | ASUS | AirVision M1 | tethered personal display | manufacturer product/sales surface |
| GLS-0176 | Lenovo | Legion Glasses | tethered personal display | historical commercial + manufacturer support |
| GLS-0177 | Lenovo | Legion Glasses Gen 2 | tethered personal display | current manufacturer retail |
| GLS-0178 | Huawei | HUAWEI Vision Glass | tethered personal display | first-party product/support + China sale history |
| GLS-0179 | Meizu / DreamSmart / StarV | StarV View | tethered personal display | current Meizu retail |
| GLS-0180 | OPPO | Air Glass | monocular waveguide assisted reality | documented 2022 preorder/retail release |
| GLS-0181 | TCL / RayNeo | NXTWEAR AIR | tethered personal display | first-party second-generation identity + historical commercial sale |

The companion reconciliation packet is `models/THE_LIST_RECONCILIATION_2026-09-04_DISPLAY_GLASSES.md`.

## Existing coverage that was preserved

The audit confirmed that GlassesResearch already has unusually broad coverage of the major modern personal-display branch:

- XREAL / Nreal Light, Air, Air 2, Air 2 Pro, Air 2 Ultra, One, One Pro and 1S;
- VITURE One, One Lite, Pro, Luma, Luma Pro, Luma Ultra and Beast;
- TCL NXTWEAR G, G+, S and S+;
- RayNeo Air, Air 2, Air 2s, Air 3s, Air 3s Pro and Air 4 Pro;
- Rokid Air, Max and Max 2;
- Epson's Moverio tethered/enterprise display generations.

The purpose of this packet is therefore not to rebuild the category but to close identifiable holes.

## CORNMI: high-value paper investigation, low-priority specimen buy

CORNMI warrants catalog coverage because it is not merely an anonymous marketplace label: the company maintains a current direct store with multiple separately named display-glasses SKUs and an OEM/ODM sales presence. At the same time, its first-party specification record is unusually inconsistent, which makes it a useful GlassesResearch case study in claim provenance.

### A8 Lite contradictions

Current first-party CORNMI material conflicts on several basic facts:

- **Weight:** storefront/editorial material describes roughly 70–79 g, while a CORNMI specification page lists 238 g.
- **Display technology:** one A8 Lite headline says “Micro-LED,” while the specification table on that page identifies Micro OLED; another CORNMI article has described a liquid-crystal waveguide.
- **Resolution / “4K”:** marketplace copy advertises “4K,” while CORNMI product material identifies a 2560×1080-per-eye / 1080P-class native panel configuration. The word “4K” should therefore be treated as an input/marketing claim unless EDID or panel evidence establishes otherwise.
- **PPD and brightness:** different first-party marketing surfaces use different values or contexts and should not be normalized silently.

The correct GlassesResearch behavior is to preserve the conflicting claims and identify what evidence would resolve them.

### If an A8 Lite ever reaches the bench

NDI should prioritize:

1. physical mass, dimensions and optical-module construction;
2. USB VID/PID, descriptors and power draw;
3. EDID/native timing table, including whether any 4K timing is accepted and how it is scaled;
4. actual refresh modes and per-eye framebuffer geometry;
5. panel / optical-engine identification where non-destructive inspection permits;
6. birdbath versus any waveguide claim;
7. diopter range and mechanical adjustment behavior;
8. brightness and usable FOV under a repeatable test setup.

There is no current reason to buy this specimen ahead of higher-priority GlassesResearch hardware. The paper trail already justifies inclusion and already produces useful research questions.

## CORNMI X7 family boundary

X7 Lite, X7 and X7 Pro are not being treated as color/storage trims.

- X7 Lite is separately sold as the lower-resolution 1080p-per-eye configuration.
- X7 is separately sold as the 2560×1440-per-eye host-driven configuration.
- X7 Pro is separately sold with built-in Android OS, creating a materially different compute/software boundary in addition to the display configuration.

The X7 Pro therefore deserves future software investigation: Android version/build fingerprint, storage, app installation, ADB exposure, update mechanism, bootloader/root state, offline behavior and whether owner-selected software can use sensors/display without a vendor account or cloud path.

## ASUS AirVision M1

AirVision M1 fills a mainstream PC-manufacturer gap. It belongs to the host-driven portable-monitor lineage rather than standalone AI glasses. ASUS's AirVision desktop software and multi-screen behavior are relevant because host software can create proprietary dependence even when the display itself is fundamentally USB-C DisplayPort hardware.

Future research should distinguish what works as generic DisplayPort eyewear from what requires ASUS software.

## Lenovo Legion display lineage

Two canonical generations are warranted:

- original Legion Glasses: roughly 96 g, 38°-class FOV, free-form optics, GY21M72722;
- Legion Glasses Gen 2: roughly 65 g, 43.5°-class FOV, birdbath optics, GY21R10236.

Lenovo Glasses T1 / Yoga Glasses is retained as predecessor/rebrand naming rather than given another GLS row. Lenovo's launch material places T1/Yoga directly in the lineage that became Legion Glasses, and this audit did not establish a materially different commercially sold hardware platform sufficient to justify count inflation.

A future archival comparison of T1/Yoga part numbers, optical geometry and shipping units can revisit that decision if new evidence appears.

## HUAWEI Vision Glass

Vision Glass is a real commercial personal-display product and a useful example of a phone-ecosystem vendor building essentially a wired cinema display. Current Huawei support still documents compatible DP-capable devices, even though broad retail availability is no longer clear.

The research value is less about AI and more about interoperability: generic DP behavior, audio routing, device compatibility lists, firmware/update dependence and whether Huawei-specific software adds functionality beyond standard video output.

## StarV View: orphaned research resolved

The earlier MYVU/StarV investigation already reached the important lineage conclusion: StarV View is a heavier Sony-OLED birdbath/cinema-display product, not the XGA010C / StarV Air waveguide platform. At that time it remained outside the canonical ledger.

The current Meizu store provides a direct acquisition route, so this audit resolves that orphaned identity into canonical purchaser history without changing the optical-lineage conclusion.

## OPPO Air Glass boundary

Only the original Air Glass crosses the purchaser-history threshold in this audit. OPPO published a 4,999-yuan price, preorder information and a March 3, 2022 online/offline sale date.

Do **not** promote the later names just because the designs look mature:

- Air Glass 2 is explicitly described by OPPO as a concept product and not commercially available.
- Air Glass 3 is explicitly described by OPPO as a prototype.

This is a useful catalog-governance example: industrial-design maturity is not acquisition evidence.

## TCL / RayNeo NXTWEAR AIR boundary

NXTWEAR AIR is documented by TCL as the second NXTWEAR generation after NXTWEAR G and before the later S branch. It was independently marketed and sold, so it warrants its own historical identity.

There is an unresolved naming/lineage question around China-market Thunderbird/RayNeo “Air” naming and the existing canonical GLS-0087 RayNeo Air. That should be solved with model numbers, manuals, certification identifiers and hardware photos rather than by deleting or merging identities from marketing names alone.

## Explicit non-admissions / unresolved leads

| Lead | Disposition | Reason |
|---|---|---|
| OPPO Air Glass 2 | research-only | concept; not commercially available per OPPO |
| OPPO Air Glass 3 | research-only | prototype per OPPO |
| Lenovo Glasses T1 / Yoga Glasses | lineage alias/predecessor | insufficient evidence for a distinct sold hardware generation beyond first Legion lineage |
| HUAWEI Vision Glass 2 | unresolved | no sufficiently authoritative commercial identity located in this audit |
| Existing XREAL/VITURE/RayNeo/Rokid/TCL rows | no action | collision check succeeded; already canonical |

## Category lesson for GlassesResearch

“Display glasses” should remain a first-class architectural lane rather than being treated as failed AI glasses. Host-driven eyewear often scores very differently from autonomous AI eyewear: it can be closed firmware yet highly owner-controlled in practice because the user supplies the phone/PC/console, local applications and content source. Conversely, proprietary host utilities, undocumented IMU protocols and accessory boxes can reintroduce dependence.

That distinction is exactly why this branch belongs in GlassesResearch even when a particular model is not personally compelling.

## Primary source set

### CORNMI
- https://www.cornmi.com/A8Lite-ARglasses
- https://shop.cornmi.com/products/cornmi-neovista-a8-lite-arglasses
- https://shop.cornmi.com/products/cornmi-neovista-x7-lite
- https://shop.cornmi.com/products/neovista-x7
- https://shop.cornmi.com/products/neovista-x7-pro
- https://www.cornmi.com/Product/NeoVista-X7-Lite.html
- https://www.cornmi.com/Product/NeoVista-X7-Pro.html
- discovery listing: https://www.alibaba.com/product-detail/2026-Ar-Glasses-4K-OEM-ODM_1601875780506.html

### ASUS
- https://www.asus.com/us/displays-desktops/glasses/airvision/asus-airvision-m1/
- https://www.asus.com/us/support/faq/1054069/

### Lenovo
- https://support.lenovo.com/us/en/accessories/lenovo_legion_glasses
- https://www.lenovo.com/us/en/p/accessories-and-software/vr-headsets/vr-headsets_smart-glasses/gy21r10236
- https://news.lenovo.com/pressroom/press-releases/glasses-t1-wearable-display-for-gaming-streaming-privacy-on-the-go/
- https://news.lenovo.com/pressroom/press-releases/legion-gaming-devices-ai-tablets-software-best-in-customer-choice/

### Huawei
- https://consumer.huawei.com/cn/wearables/vision-glass/
- https://consumer.huawei.com/cn/wearables/vision-glass/specs/

### Meizu / DreamSmart / StarV
- https://www.meizu.com/global/product/starv-view/specs
- https://detail.meizu.com/item/StarVView.html
- existing lineage investigation: `research/investigations/MYVU_STARV_LINEAGE_2026-09-02.md`

### OPPO
- https://www.oppo.com/cn/newsroom/press/480/
- https://www.oppo.com/cn/events/innoday2022/
- https://www.oppo.com/en/newsroom/press/oppo-unveils-new-oppo-air-glass-3/

### TCL / RayNeo
- https://www.tcl.com/global/en/news/tcl-unveils-portable-lightweight-and-personal-nxtwear-air-wearable-display-glass-at-ces-2022
- https://www.tcl.com/eu/en/glasses/tcl-nxtwear-air/specifications
