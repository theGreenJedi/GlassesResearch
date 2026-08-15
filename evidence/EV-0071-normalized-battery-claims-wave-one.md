# EV-0071 — normalized battery claim boundaries, wave one

Last verified: 2026-08-15  
Evidence class: vendor-primary claims  
Scope: Even G2, Brilliant Halo, Ray-Ban Meta Gen 2 and Solos AirGo V2

## Purpose

This record normalizes what each manufacturer actually claims before any measured comparison. It does not convert unlike workloads into a ranking and does not treat charging-case energy as continuous on-face runtime.

## Claim matrix

| Model | On-face claim | Stated workload | Capacity / case claim | Boundary |
|---|---|---|---|---|
| Even G2 (GLS-0048) | 2 days | “Typical” or regular use: intermittent information checks, notifications and navigation | Glasses 192 mAh / 0.744 Wh; case 2000 mAh / 7.4 Wh; about 7 full recharges | No daily interaction count, display-on time, brightness, connection state or end-point disclosed. Seven case recharges are not two weeks of continuous on-face runtime. |
| Brilliant Halo (GLS-0052) | 14 hours / all day | Estimated normal use | Capacity not published in the cited product material | Pre-shipping estimate; workload, display duty cycle, AI/audio activity and cutoff undisclosed. Do not present as a measured shipping-product result. |
| Ray-Ban Meta Gen 2 (GLS-0003) | Up to 8 hours moderate use; up to 5 hours continuous audio streaming and voice assistance | Two partly defined workloads | Up to 40 additional hours from fully charged case | The 5-hour continuous workload is more comparable than “moderate use,” but volume, voice-assistant frequency, network state and cutoff remain unspecified. Case claim stays separate. |
| Solos AirGo V2 (GLS-0029) | Product record claims approximately 16 hours of photo shooting and AI enquiries; current Solos landing material also advertises 10 hours music or 7 hours calls | Conflicting/model-page workload descriptions | Capacity not established in this record | Claims must remain workload- and page-specific. Do not collapse photo/AI, music and calling into one battery-life value or borrow generic FAQ figures from another Solos generation. |

## Primary sources

- [Even G2 Battery & Charging](https://support.evenrealities.com/hc/en-us/articles/13499279151375-Battery-Charging)
- [Even G2 specifications](https://support.evenrealities.com/hc/en-us/articles/13499229138959-Specs)
- [Brilliant Halo product page](https://brilliant.xyz/products/halo)
- [Brilliant Labs product overview](https://brilliant.xyz/)
- [Ray-Ban Meta Gen 2 product page](https://www.ray-ban.com/usa/electronics/RW4012ray-ban%20meta%20wayfarer%20-%20gen%202-black/8056262721292)
- [Solos product overview](https://solosglasses.com/)

## Normalized interpretation

No valid endurance ranking can be produced from these claims alone.

- **Idle/connected:** none supplies a complete standardized result.
- **Audio:** Ray-Ban Meta Gen 2 provides up to 5 hours continuous audio plus voice assistance; Solos advertises a separate 10-hour music claim. Volume and connection conditions remain unknown.
- **Camera/AI:** Solos publishes an approximately 16-hour photo/AI-enquiry claim, but the operation frequency is not stated.
- **HUD/display:** Even G2's two-day typical-use claim and Halo's 14-hour estimate do not publish display duty cycle or brightness.
- **Mixed use:** “typical,” “regular,” “moderate,” and “normal” are manufacturer-specific labels, not a shared workload.
- **Case contribution:** Even's approximately seven recharges and Ray-Ban's up-to-40 additional hours are replenishment claims, not continuous glasses runtime.

## Measurement requirements

A measured comparison must use the same workload definition, logging interval, endpoint and reporting method across devices. Record firmware, host, connection/network state, brightness, volume, interaction/capture/query rate, temperature, starting and ending charge, elapsed time and interruptions. Use at least three valid runs and report median plus spread.

Until then, Finder and report-card text should identify these as **manufacturer claims with incomparable workloads**, not performance facts.
