# Watch and Crack: smart-glasses video password-inference study — October 31, 2026

<!-- news_promotion_schema: 1 -->

**Review date:** 2026-10-31  
**Study first posted:** September 2026; **new secondary coverage:** October 30, 2026  
**Scope:** `core_glasses`, wearable-camera bystander privacy and smartphone password-entry risk  
**Disposition:** `review` for existing Across the Wire editorial research; not a new October 31 discovery or independently reproduced exploit.

## Sources and provenance

- [Orenbach and Wool, *Watch and Crack: Password Inference from Smart-Glasses Video*, arXiv:2609.06539](https://arxiv.org/abs/2609.06539) — **researcher-primary preprint** (September 2026); the authors describe video-based probabilistic inference of alphanumeric smartphone QWERTY passwords from Meta Ray-Ban footage.
- [ACM CCS 2026 official accepted-paper list](https://www.sigsac.org/ccs/CCS2026/program/accepted-papers.html) — **independent confirmation** that the paper by Yoav Orenbach and Avishai Wool is accepted, **not** independent reproduction.
- [Avishai Wool's university publication list](https://www.avishaiwool.sites.tau.ac.il/publication/refereed-conference-papers) — author-primary listing of the paper as forthcoming at CCS 2026.
- [ITmedia Innovative Tech coverage, October 30](https://www.itmedia.co.jp/news/article/2610/30/2000002684/) — **secondary media surfacing**, not a new study release. The Japanese article discusses filming fingertip motion across a cafe and potential ineffectiveness of screen privacy filters against this *different* observation channel.

## What the authors report (not universal capabilities)

The research reports a camera-side-channel pipeline for filmed smartphone password entry. It estimates key probabilities and combines them with password-distribution priors, rather than reading a password directly from a hidden screen. The preprint reports experiments with Meta Ray-Ban capture up to **1.8 m**, multiple phone models and viewing postures, and significant reduction in password-guessing search space in its controlled study. Statements about crack times assume the authors' offline-guessing methodology and compute, not instant remote account compromise. Distinguish **alphanumeric passwords** from numeric-only PINs; do not retitle this as a universally demonstrated PIN unlock. No device is claimed hacked by wearing glasses.

## Editorial / safety boundary

The finding is about **bystander privacy and threat modeling**, not an instruction to reproduce credential theft. Practical consumer implication: concealing the display alone may not conceal hand/finger motion from nearby cameras; avoid entering sensitive credentials where fingers are easily filmed, use phishing-resistant authentication where available. Exact mitigation effectiveness is not measured here. No GlassesResearch replication, independent hardware test, or generalized prevalence estimate.

The actual public [Across the Wire feed](https://glassesresearch.org/data/wire-feed.json) was inspected October 31. It contains a Japanese-language secondary headline about smart-glasses filming finger motion and phone passcodes (dated 2026-10-30T23:48:04Z), marked **Reported / unverified**. That is **existing attributed discovery coverage**, not verification or an unpublished/broken state. No duplicate feed item or generated-feed edit. The older September paper and October 30 reporting should remain dated separately.

**Follow-up:** Check study sample, devices, threat model and defenses directly before translating findings into Practical Answers; verify any later public publication against the deployed feed/page.
