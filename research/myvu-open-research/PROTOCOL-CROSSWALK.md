# MYVU Protocol Crosswalk

This is a normalized research index, not a replacement for upstream protocol documentation.

| Layer | Panny777 Client | Panny777 SDK | CyanBridge | GR status |
|---|---|---|---|---|
| Hardware target | MYVU / Star Air XGA010C | MYVU / Star Air XGA010C | Native MYVU integration credits Panny upstream | Upstream-documented; GR reproduction pending |
| BLE wake/setup | Implemented | Detailed | Uses Panny BLE work | Cross-source agreement |
| GATT generation distinction | Client supports protocol implementation | Air `2020–2023`; V2 `2010–2012` documented | Downstream integration | Critical compatibility investigation |
| ECDH bond | Implemented | P-256/AES exchange documented | Uses Panny ECDH work | Cross-source agreement |
| Heartbeat | Implemented | 3 s urgent-characteristic heartbeat documented | Uses Panny heartbeat work | Cross-source agreement |
| Ability/session auth | Implemented | AUTH + AUTH_SUCCESS documented | Downstream integration | Reproduction pending |
| Init sequence | Implemented | captured init burst/replay behavior documented | Downstream integration | Determine minimum required sequence experimentally |
| RFCOMM relay | Implemented | per-session UUID synced via BLE; framing documented | Uses Panny RFCOMM work | Cross-source agreement |
| Display/app actions | Implemented | actions/features documented | Uses Panny display transport | Build feature-by-feature conformance tests |
| Microphone/AI | Implemented | Opus + session sequencing documented | broader local-AI architecture exists | Reproduce on GR specimen |
| Weather | Supported | wire shape + metric behavior documented | not required for crosswalk yet | Useful protocol conformance target |
| Recovery/reset | not routine | deliberately not implemented | not normalized | Keep outside safe baseline |

## Best-practice interpretation

Where CyanBridge says it uses Panny777's MYVU transport, that is **downstream adoption**, not independent protocol discovery. It increases confidence that the implementation is reusable, but GlassesResearch should reserve **GR-VERIFIED** for our own reproduction on identified hardware.

The Air-vs-V2 characteristic distinction is currently one of the most important clues for explaining apparent compatibility failures across MYVU-branded or related hardware. It should be captured before attempting higher-level feature debugging.