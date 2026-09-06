# CyanBridge / Alternative HeyCyan App and SDK

**Community Research project**  
**Primary scope:** HeyCyan-compatible glasses plus experimental multi-vendor interoperability work  
**Project:** [FerSaiyan/Alternative-HeyCyan-App-and-SDK](https://github.com/FerSaiyan/Alternative-HeyCyan-App-and-SDK)  
**Evidence lane:** Community-primary technical research and alternative companion software; device-specific claims require hardware validation

## What the project does

CyanBridge is an alternative smart-glasses companion and interoperability workspace. Its most mature path is the Android companion for HeyCyan-compatible devices, with BLE connection management, media transfer over BLE plus Wi-Fi Direct, local chat history, local-model runtime support, and optional OpenAI-compatible remote inference.

The repository also contains experimental work for additional ecosystems, including MYVU / Star Air, MemoMind / XGIMI, Meta Ray-Ban setup plumbing, and prototype Even / Mentra runtime adapters. The project is explicit that these paths vary in maturity and that physical-device validation remains necessary.

## Why it matters

CyanBridge illustrates the next step after protocol discovery: reusable software that can convert community findings into something owners can actually run. It also shows how open projects can compound one another. CyanBridge explicitly credits Panny777's MYVU client and states that the MYVU BLE, ECDH, RFCOMM relay, heartbeat, and display-transport work informs its native MYVU integration.

That makes CyanBridge an important bridge between reverse-engineering knowledge and practical owner control.

## Evidence boundary

CyanBridge's own documentation distinguishes active, experimental, partial, and prototype paths. GlassesResearch should preserve those boundaries. Inclusion here does not imply that every listed adapter or feature has been independently reproduced by GlassesResearch, nor should experimental support be converted into a verified product capability without separate evidence.

## Related GlassesResearch material

- [W610 research portal](/models/W610/resources/RESEARCH_PORTAL/)
- [W610 open-hacking dossier](/models/W610/hacking/)
- [Panny777 / Meizu-Myvu-Client Community Research profile](panny777-meizu-myvu-client.md)
- [Related editorial: When owners take their glasses back](../news/articles/2026-09-06-when-owners-take-their-glasses-back.md)
