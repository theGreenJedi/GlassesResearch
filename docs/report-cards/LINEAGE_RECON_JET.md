# Lineage Research — Recon Jet

**Research date:** 2026-08-12

This packet applies the lineage-first protocol to Recon Instruments' Jet eyewear family. The family is treated as Jet → Jet Pro → Jet Pro+, rather than forcing a fixed-size batch. Recon Snow2/MOD Live are related Recon HUD products but form an earlier snow-goggle/module branch and are not silently merged into the Jet eyewear lineage.

## Lineage finding

Recon Jet clearly crossed the acquisition threshold. Recon's April 2015 launch material states that Jet was available through specialty stores, Amazon.com in the United States, and reconinstruments.com at a US retail price of $699. Contemporaneous trade reporting documents actual shipment beginning in April 2015 and a later US price reduction to $499.

EV-0063 adds a function-by-function post-shutdown boundary: the original manual makes Engage/Uplink first activation mandatory while documenting local camera, gallery, music, compass, maps, GPS and ANT+ functions after activation. Intel's later support record explicitly names three separate products — Recon Jet Smart Eyewear, Recon Jet Pro Smart Eyewear, and Recon Jet Pro+ Smart Eyewear — and directs owners to their place of purchase for warranty/support. That is strong post-acquisition evidence that Pro and Pro+ were real customer products, not merely announced concepts. Generation-specific technical documentation for Pro and especially Pro+ is much thinner than for the original Jet, so this packet does not copy Jet's scores into later variants without evidence.

## Recon Jet — admit

Jet was a sport-focused monocular HUD/computer built around an Android-based operating system. Documented launch features include a dual-core processor, high-contrast display positioned below the right eye, point-of-view camera, smartphone connectivity, ANT+ sensor connectivity, GPS/activity metrics, caller/text display, and Recon Engage web/mobile services. Recon explicitly described the platform as open and published an SDK for third-party applications.

The device's strongest ownership attribute was its application-development surface: this was not merely a mirrored display. Its weakest long-term attribute is cloud/service survivability. Intel later confirmed Recon Engage and the Recon products were discontinued; Intel community support also records that the Engage servers went offline, leaving login/registration-dependent functionality impaired. That materially lowers Cloud Independence on a current ownership ruler even though local sensor/display functions were architecturally capable of running on-device.

### Report card — Recon Jet

| Model | Hardware | Wearability | Visual AI | Software | Openness | Owner Control | Cloud Independence | Hackability | Display/HUD | Value |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Recon Jet | 7.0 | 5.5 | N/A | 7.5 | 7.5 | 8.0 | 4.5 | 7.0 | 6.5 | 7.5 |

- **Hardware 7.0:** substantial self-contained sport-computing capability, camera, GPS/sensors and wireless connectivity, but bulky and dated by the catalog-wide modern ceiling.
- **Wearability 5.5:** sports-eyewear form was purposeful and lighter than industrial headsets, but the electronics pod and asymmetric HUD remain conspicuous and heavier than ordinary glasses.
- **Visual AI N/A:** a camera was present, but the documented system was not a visual-AI platform in the modern catalog sense.
- **Software 7.5:** Android-based software, activity dashboards, phone integration and third-party applications created a meaningful platform; dead services and discontinued support now materially constrain it.
- **Openness 7.5:** Recon publicly promoted an open platform and SDK, well above appliance-style glasses, but firmware/hardware source, schematics and low-level debug access do not approach the Monocle/Frame 10 benchmark.
- **Owner Control 8.0:** owners/developers could run purpose-built applications and use multiple external sensors/services rather than being confined to one assistant workflow.
- **Cloud Independence 4.5:** important local functions existed, but Recon Engage account/server dependence became a real post-shutdown failure mode and prevents a high survivability score.
- **Hackability 7.0:** Android plus an SDK gives a strong experimentation surface, capped by proprietary firmware/hardware and the dead vendor ecosystem.
- **Display/HUD 6.5:** useful glanceable monocular sport HUD, but low-resolution/narrow presentation and asymmetric bulk sit well below current display leaders.
- **Value 7.5:** at the later documented $499 US price, Jet delivered unusually broad wearable-computer capability for its time; launch price was $699.

## Recon Jet Pro — admit, generation-specific scoring held

Intel explicitly recognizes Recon Jet Pro Smart Eyewear as a shipped customer product. Independent teardown evidence records a US-purchased Recon Jet Pro (model RI-JET), measured at 85.3 g, with a recorded retail price of $991.99 and a 2017-era release. That supports ledger admission and enterprise/commercial status.

However, the current evidence package does not yet establish enough primary generation-specific differences in display, processor, camera, battery, SDK policy, environmental rating, or software stack to defensibly score every dimension without inheriting Jet claims. Under the benchmark rules, those fields remain **Not yet graded** pending archival Intel/Recon product sheets or manuals.

| Model | Hardware | Wearability | Visual AI | Software | Openness | Owner Control | Cloud Independence | Hackability | Display/HUD | Value |
|---|---|---|---|---|---|---|---|---|---|---|
| Recon Jet Pro | Not yet graded | Not yet graded | N/A | Not yet graded | Not yet graded | Not yet graded | 4.0 | Not yet graded | Not yet graded | 5.5 |

Cloud Independence receives a provisional 4.0 because Intel's shutdown record applies to the Recon Engage product family and activation/service dependence is directly documented. Value is provisionally 5.5 against the recorded ~$992 acquisition price, pending a stronger primary price sheet.

## Recon Jet Pro+ — admit, scoring held

Intel separately names Recon Jet Pro+ Smart Eyewear as a discontinued Recon product and directs owners to place-of-purchase support. That is sufficient evidence that Pro+ crossed the acquisition threshold. It is not sufficient to infer its hardware from Jet Pro.

| Model | Hardware | Wearability | Visual AI | Software | Openness | Owner Control | Cloud Independence | Hackability | Display/HUD | Value |
|---|---|---|---|---|---|---|---|---|---|---|
| Recon Jet Pro+ | Not yet graded | Not yet graded | N/A | Not yet graded | Not yet graded | Not yet graded | 4.0 | Not yet graded | Not yet graded | Not yet graded |

The correct result is an admitted model with explicit evidence gaps, not a copied scorecard.

## Sources / evidence family

- Recon Instruments launch release (2015), including retail channels, launch price, platform description and SDK: https://www.prnewswire.com/news-releases/recon-instruments-launches-recon-jet-smart-eyewear-for-your-active-lifestyle-300066805.html
- Intel Community support, explicitly naming Recon Jet, Jet Pro and Jet Pro+ as Recon products and confirming Intel no longer supports them: https://community.intel.com/t5/Wireless/How-to-bypass-the-recon-jet-activation-screen/td-p/1379242
- Intel Community support on Recon Engage discontinuation/server loss: https://community.intel.com/t5/Wireless/Recon-Engage-Call-to-all-customers/td-p/1256845
- Bicycle Retailer contemporaneous shipment report (April 2015): https://www.bicycleretailer.com/product-tech/2015/04/16/recon-instruments-begins-shipping-long-awaited-smart-sunglass
- Bicycle Retailer contemporaneous price reduction to $499 (September 2015): https://www.bicycleretailer.com/product-tech/2015/09/15/recon-lowers-price-its-smart-glasses
- TechInsights teardown record for a US-purchased Recon Jet Pro RI-JET, including measured weight and recorded purchase price: https://www.techinsights.com/products/ddt-1804-805

## Service-survival evidence

See [EV-0063](../../evidence/EV-0063-Recon-Jet-service-survival.md). It does not claim that all hardware is dead or that a community bypass universally works: it distinguishes local architecture on activated Jet units from the confirmed activation failure affecting new/reset hardware after Engage/Uplink shutdown.

## Archival follow-up

Recover Intel/Recon manuals and product sheets for Jet Pro and Jet Pro+ before filling their inherited-looking fields. Separately investigate Snow2 and MOD Live as their own earlier HUD lineage rather than treating them as Jet generations.