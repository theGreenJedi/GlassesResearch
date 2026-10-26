# Q-000150 — Pocketed-iPhone smart-glasses capture into Obsidian

Research reviewed: 2026-10-26. Source question observed 2026-10-21 in [r/SmartGlasses](https://www.reddit.com/r/SmartGlasses/comments/1x5b2b0/anyone_actually_using_glasses_for_still_photo/) (canonical registry Q-000150). The question is firsthand demand, **not** proof of an implementation.

**Question:** Anyone actually using glasses for still photo + dictated note → Obsidian/Markdown, with an iPhone staying pocketed?

**Editorial disposition:** Documentary evidence supports components of a possible integration, but **no verified complete, repeatable, phone-locked/pocketed workflow** was established. Do not name a turnkey compatible model or claim end-to-end success. Proposed answer is in `docs/faq/03-use-cases.md`. Keep registry `observed/unresearched` until editorial review, successful build, deployment and live-route verification; then update to `answered/published` with the exact public URL. If published as a bounded research answer, evidence_state should reflect the documentary limits, not an unperformed bench test.

## Claim-level provenance

| Claim | Evidence | Boundaries |
| --- | --- | --- |
| Community demand exists | [Original Reddit question](https://www.reddit.com/r/SmartGlasses/comments/1x5b2b0/anyone_actually_using_glasses_for_still_photo/) — original question URL preserved by discovery | No verified device/app demonstration extracted. |
| Ray-Ban Meta supports hands-free photo capture; media import depends on companion app and setup | [Ray-Ban Meta FAQ](https://www.ray-ban.com/uk/c/frequently-asked-questions-ray-ban-meta-smart-glasses) — manufacturer documentation | Not evidence of an Obsidian integration; automatic import may require glasses in case and connected Wi-Fi. |
| Obsidian can create a Markdown note via URI | [Obsidian URI](https://help.obsidian.md/Extending%2BObsidian/Obsidian%2BURI) — application developer primary documentation | URI text support does not transfer image files or prove locked-phone invocation. |
| iOS Shortcuts offers actions and automation, with permission/background limits | [Apple Shortcuts automations](https://support.apple.com/en-euro/guide/shortcuts/apdfbdbd7123/10.0/ios/27) — OS developer primary documentation | No proof that an arbitrary photo arrival can trigger this exact chain unattended. |
| Supported glasses can be extended through an SDK | [Mentra SDK overview](https://mentrahelp.zendesk.com/hc/en-us/articles/47582365021588-Can-I-access-the-SDK-for-development-or-integration) — vendor documentation | Device capability and iOS restrictions still require testing. |

## Required device verification before asserting end-to-end success

1. Identify exact glasses model, firmware, iOS version, companion app, Shortcuts actions and Obsidian version.
2. Capture still photo and dictate text with iPhone locked/pocketed; inspect image/transcript association, local attachment and Markdown content.
3. Repeat with offline connectivity, suspended apps, low battery and multiple captures; measure failures and duplicate handling.
4. Verify permissions and cloud transfers; distinguish on-device transcription from server processing.
5. Preserve redacted test logs or a reproducible workflow and independent confirmation before upgrading to a tested compatibility claim.

**No bench result, automatic Obsidian photo attachment, iOS background delivery guarantee or third-party user success is claimed.**
