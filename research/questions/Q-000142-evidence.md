# Q-000142 — Recording indicator on camera smart glasses

**Original observed question:** [I want smart glasses with no recording indicator. What do I buy?](https://www.reddit.com/r/SmartGlasses/comments/1x96b62/i_want_smart_glasses_with_no_recording_indicator/), preserved as Q-000142. **Reviewed:** 2026-10-26. Reddit thread content was not retrievable in this research pass; the original question wording was preserved by the existing discovery registry, not invented.

## Claim-level provenance

| Claim | Evidence | Boundary |
| --- | --- | --- |
| Meta AI camera glasses use a blinking white capture LED for gallery photos/videos | [Meta's 2026 capture-indicator FAQ](https://about.fb.com/news/2026/07/metas-ai-glasses-your-questions-answered/) | Manufacturer statement, not independently verified on every generation |
| Meta states camera is disabled if LED is blocked or tampered with on supported models | [Meta's FAQ](https://about.fb.com/news/2026/07/metas-ai-glasses-your-questions-answered/) | Product/firmware behavior can change; do not propose circumvention |
| Camera-free display glasses are a different category; Even explicitly confirms G2 has no camera and its specs list four microphones | [Even manufacturer no-camera explanation](https://www.evenrealities.com/en-HR/blogs/even-insider/asking-for-less), [Even G2 specifications](https://support.evenrealities.com/hc/en-us/articles/13499229138959-Specs) | Manufacturer statements, not a claim that all data collection is absent |
| Visible capture indicators do not replace permission/consent in restricted settings | [Existing GlassesResearch privacy FAQ](../../docs/faq/07-privacy-security.md) | Editorial guidance; legal rules differ by place |

## Verification and publication gate

No claim is made that every camera-equipped model has a mandatory light or that an indicator alone ensures consent. The safe answer is to choose a **camera-free** design if visible capture indication is unacceptable, rather than defeating safety signals. **State: published after exact live FAQ and directory proof.** Proposed anchor: `docs/faq/07-privacy-security.md#can-i-buy-camera-smart-glasses-without-a-recording-indicator`.

## Publication proof — 2026-10-26

[PR #698](https://github.com/theGreenJedi/GlassesResearch/pull/698) merged as revision `2262054aaa16529f36e768925535be576f9a17b6` after documentation, editorial, link/fragment, deploy and Lighthouse checks passed. [Production content proof #40396645760](https://github.com/theGreenJedi/GlassesResearch/actions/runs/40396645760) succeeded: fetched the complete public FAQ `/docs/faq/07-privacy-security/` (digest `bb42bbbd03b7`), Practical Answers directory `/docs/faq/` (digest `3f42fb3fe4bc`), and this evidence page (digest `999bfa7220dc`) matching the deployed build. The directory links to the exact built-page anchor [published answer](https://glassesresearch.org/docs/faq/07-privacy-security/#can-i-buy-camera-smart-glasses-without-a-recording-indicator), validated by strict internal fragment checks. This proves content publication, **not** a device or SDK bench test. Registry Q-000142 was credited only after this proof; original observations and uncertainty remain intact.
