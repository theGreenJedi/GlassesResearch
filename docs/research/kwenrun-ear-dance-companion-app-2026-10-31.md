# KWENRUN / Ear Dance companion-app investigation

**Research date:** 2026-10-31  
**Status:** Preliminary research; app not installed or instrumented on the test phone.  
**Test hardware:** Approx. US$26 KWENRUN-branded Bluetooth audio glasses, Amazon ASIN [B0H714BBSP](https://www.amazon.com/dp/B0H714BBSP); advertising/model lineage unresolved; Bluetooth advertising name `eyewear SE`.

## Ecosystem contributor

- **Shenzhen Watch Fun Internet Technology Co., Ltd.** (深圳市沃奇互娱科技有限公司) — developer/publisher attributed to the **Ear Dance** companion application, Android package `com.watchfun.classicpublic`; company/developer site [watchfun.cn](https://watchfun.cn/).
- **Role classification:** software / companion-app ecosystem contributor, **not** a confirmed original equipment manufacturer for this pair of glasses.
- [Google Play package entry](https://play.google.com/store/apps/details?id=com.watchfun.classicpublic). Developer and package attribution should be rechecked periodically because listings change.

## Preliminary application and privacy review

The app is marketed for Bluetooth-glasses services including AI conversations, speech translation and recording/transcription. These are **advertised/documented features**; they have *not* been tested on the user's physical unit.

An independent Android app index reports requested capabilities including Bluetooth access, microphone and foreground microphone service, camera, file/media access, media controls and overlay. **Manifest-requested permissions are not the same as user-granted permissions or evidence of active collection.** Reconcile these against the actual Play Store build and runtime dialogs before publication of any exact manifest-level claims.

The Android Play Store's self-reported data-safety disclosures and the separate iOS App Store privacy disclosures appear materially different (Android reports no collection/sharing; iOS indicates some identifiers/contact/diagnostic categories may be collected). Different platforms and developer declarations may explain the difference; do not infer wrongdoing or prove zero collection from either declaration. [Developer-linked privacy policy](https://earjoy-dance.com/app-about-h5?code=privacy_policy) has not yet been independently read and validated; policy details remain **unknown**.

## Cloud / AI dependency questions — unresolved

- Which underlying LLM/API powers Ear Dance AI conversations? **Unknown.** Marketing references to “ChatGPT” do not establish an OpenAI API integration.
- Which vendors operate automatic speech recognition, translation, text-to-speech and storage? **Unknown.**
- Whether audio, transcripts, identifiers, contacts or device telemetry leave the phone; processing regions; retention/deletion and opt-out controls: **Unknown** until documented or tested.
- Some third-party product documentation describes internet-dependent translation; do not assume offline service, and do not attribute its workflow to this hardware without a demonstrated match.

## “Free lifetime access” claim

Seller marketing for this KWENRUN listing describes **free lifetime access to Ear Dance**. Record as a **seller claim only**, not a verified entitlement to unlimited cloud services. No confirmed agreement establishes unlimited AI turns, translation minutes, model access, an indefinite no-fee commitment or any service-availability guarantee. Reports of “no in-app purchases” do not answer usage quotas, backend funding or shutdown risk.

**Required follow-up:** capture the exact offer language and version/date, terms of service, in-app usage meters or quotas, whether advanced features require a login, and a written developer response specifying what “lifetime” means (app access, device lifetime, company/service lifetime, free basic tier, or unlimited inference).

## Actual tested hardware vs. companion app

The user has already independently verified direct Bluetooth music, two-way phone calling and a conversation in ChatGPT Voice using the Pixel as host, **without installing Ear Dance**. That establishes a useful baseline and does not verify Ear Dance's AI features. The underlying hardware model remains **unconfirmed**: an earlier KO/FCC-ID theory based on the generic `eyewear SE` pairing name is insufficient, especially in view of differences in frame construction and the user's report of “KI” in an Amazon listing. Avoid assigning FCC ID `2A4ZQ-KO` to this physical unit without evidence.

## Next research / test sequence

1. Preserve package/version, developer identity, APK signature and permissions from official distribution before installation.
2. Read the full privacy policy and service terms, including retention and cross-border processing provisions.
3. Test pairing, app-account requirements and feature discovery with minimal permissions; deny optional contacts/camera/storage access initially.
4. Record whether translation/AI features function offline and, if online, inspect observable network endpoints without assuming endpoints prove the downstream AI provider.
5. Test usage limits against the seller's “lifetime” wording and obtain developer clarification.
6. Publish conclusions only after the evidence is checked; preserve “unknown” where verification is unavailable.

**Evidence hierarchy:** firsthand test > directly examined application/terms > publisher's platform disclosures > seller listing > third-party manual/index. This note is a research annotation, not a completed security audit or a recommendation to install.
