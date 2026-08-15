# EV-0065 — Bose Frames post-Bose-AR service-survival matrix

**Status:** Source boundary completed; regional app and hands-on testing remain  
**Models:** GLS-0013 Alto; GLS-0014 Rondo; GLS-0015 Tempo; GLS-0016 Tenor; GLS-0017 Soprano  
**Reviewed:** 2026-08-15

## Question

What remains useful after Bose ended the Bose AR platform, and which functions still depend on Bose applications or networked phone services?

## Finding

Bose Frames are Bluetooth audio glasses with a separable historical AR software layer. Bose no longer sells the lineage on Bose.com, but its current support surfaces still list:

- Alto and Rondo under Bose Connect compatibility; and
- Tempo, Tenor and Soprano under the Bose app compatibility list.

The original Alto/Rondo architecture used open-ear Bluetooth audio plus a nine-axis head-motion sensor. Bose AR combined that head orientation with the paired phone's location and applications. Its loss removes the location/motion-driven application ecosystem; it does not erase ordinary Bluetooth playback and calling.

The later Tempo/Tenor/Soprano generation was sold primarily as finished Bluetooth audio eyewear. Its core playback, calls, physical/touch controls and phone voice-assistant invocation are separable from Bose AR.

## Function-by-function matrix

| Function | Alto / Rondo | Tempo / Tenor / Soprano | Evidence boundary |
|---|---|---|---|
| Bluetooth music playback | Local Bluetooth path documented | Local Bluetooth path documented | Manufacturer product/app material; no cloud inference required |
| Calls / microphones | Phone Bluetooth path documented | Phone Bluetooth path documented | Host phone/cellular service may be needed for calls, not Bose cloud |
| Physical controls | Documented | Documented | On-device control path |
| Bose AR experiences | Historical platform; no current supported ecosystem established | Not a defining current-generation function | Loss is software-layer loss, not total device failure |
| Head-motion sensing | Nine-axis sensor documented | No equivalent open developer path established | Do not transfer first-generation AR capability forward |
| Companion configuration | Bose Connect remains listed | Bose app remains listed | Current listing proves support surface, not every region/device combination |
| Firmware updates | App-mediated history; current per-model availability not verified | App-mediated history; current per-model availability not verified | Remains unknown pending paired-device test |
| Voice assistant | Invokes the paired phone's assistant | Invokes the paired phone's assistant | Depends on host assistant/network, not a Bose Frames cloud |
| Operation after Bose account/app loss | Basic Bluetooth audio is architecturally separable | Basic Bluetooth audio is architecturally separable | Pairing/reset behavior must still be tested hands-on |
| Replacement lenses / batteries / repair | Not resolved by this pass | Not resolved by this pass | Separate repairability workstream |

## Lifecycle classification

All five models are **discontinued-functional / supported-owner** as of this review. That classification is dated and source-bounded:

- sales ended;
- current Bose compatibility/support pages remain;
- basic Bluetooth audio survives independently of Bose AR;
- app-dependent settings and firmware longevity remain unverified.

## Scoring effect

The existing Cloud Independence anchors remain appropriate: 7.5 for Alto/Rondo and 8.0 for Tempo/Tenor/Soprano. First-generation scores stay slightly lower because part of their advertised differentiation was the discontinued Bose AR layer. Openness/Hackability are not raised merely because the discontinued SDK once existed.

## Required hands-on follow-up

For one factory-reset example from each generation, record pairing without account sign-in, audio/calls, controls, assistant invocation, app discovery, firmware status, retained settings after app removal and behavior with Bose endpoints blocked. Record phone OS, app version, region and firmware.

## Sources

- [Bose Frames support](https://www.bose.com/c/support/smart_glasses_support.html)
- [Bose Connect compatibility](https://www.bose.com/apps/bose-connect)
- [Bose app compatibility](https://www.bose.com/apps/bose-app)
- [Original Bose Frames architecture and Bose AR announcement](https://www.bose.com/pressroom/bose-announces-frames-a-revolutionary)
- [Tempo, Tenor and Soprano generation announcement](https://www.bose.com/pressroom/new-bose-frames)
