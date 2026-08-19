# Submit an independent hands-on review

GlassesResearch cannot physically inspect every smart-glasses model. Owners, borrowers, developers, repairers, accessibility users, and other hands-on users can help fill that gap through a **standardized independent review**.

Your submission becomes evidence with provenance. It does **not** become a GlassesResearch hands-on finding merely because it was submitted here.

<div class="community-review-principles">
  <strong>Evidence labels:</strong> one accepted owner report is an <em>Independent hands-on review</em>. Compatible findings from multiple unrelated reviewers may become <em>Community confirmed</em>. GlassesResearch uses <em>Verified</em> only when the project evidence standard supports that promotion.
</div>

## What happens to a review

1. You describe the exact device and what you personally observed.
2. The intake resolves retail aliases to the canonical GLS model whenever possible.
3. A maintainer checks the submission for device identity, provenance, disclosure, internal consistency, and usable evidence.
4. Accepted reviews receive a stable review ID such as `GR-CR-0042`.
5. If you choose a persistent public identity, you receive a stable contributor ID such as `GR-C-0017`; future accepted reviews accumulate on the same contributor page.
6. Community scores are summarized separately beside the canonical Report Card. They never silently overwrite GlassesResearch scores.

Persistent contributor history is **provenance, not authority**. Thirty good prior reviews do not make a thirty-first claim automatically true.

## Review intake

<form id="community-review-intake" class="community-review-form">
  <fieldset>
    <legend>1. Identify the glasses</legend>
    <label for="cr-model">Model, GLS number, or retail alias <span aria-hidden="true">*</span></label>
    <input id="cr-model" name="model" list="cr-model-options" autocomplete="off" required maxlength="180" placeholder="GLS-0039, W610, BooaBei…">
    <datalist id="cr-model-options"></datalist>
    <p id="cr-model-resolution" class="community-review-resolution" aria-live="polite">Choose the exact model you used. Retail aliases are welcome.</p>
    <input id="cr-canonical-id" name="canonical_id" type="hidden">

    <label for="cr-retail-name">Name printed on your box/listing, if different</label>
    <input id="cr-retail-name" name="retail_name" maxlength="160" placeholder="Retail brand, alias, regional name…">

    <div class="community-review-grid">
      <label>How did you access this device?
        <select id="cr-ownership" name="ownership_basis" required>
          <option value="">Choose…</option>
          <option value="purchased">Purchased / personally owned</option>
          <option value="borrowed">Borrowed</option>
          <option value="review_sample">Review sample / loaner</option>
          <option value="employer_provided">Employer / organization provided</option>
          <option value="retailer_demo">Retailer / event demo</option>
          <option value="other">Other hands-on access</option>
        </select>
      </label>
      <label>Approximate hands-on use
        <input id="cr-usage-length" name="usage_length" maxlength="120" placeholder="3 months daily, 2-hour demo…">
      </label>
      <label>Hardware revision
        <input id="cr-hardware" name="hardware_revision" maxlength="120" placeholder="If known">
      </label>
      <label>Firmware version
        <input id="cr-firmware" name="firmware_version" maxlength="120" placeholder="If known">
      </label>
      <label>Companion app + version
        <input id="cr-app" name="companion_app_version" maxlength="120" placeholder="If used">
      </label>
      <label>Phone / host device + OS
        <input id="cr-host" name="phone_os" maxlength="180" placeholder="Pixel 9 Pro XL / Android 16…">
      </label>
    </div>
  </fieldset>

  <fieldset>
    <legend>2. How should this review be attributed?</legend>
    <label for="cr-attribution">Public attribution</label>
    <select id="cr-attribution" name="attribution_mode" required>
      <option value="anonymous">Anonymous</option>
      <option value="pseudonym">Persistent handle / pseudonym</option>
      <option value="identified">Public name</option>
    </select>

    <div id="cr-identity-fields" hidden>
      <label for="cr-display-name">Public display name or handle</label>
      <input id="cr-display-name" name="display_name" maxlength="120" placeholder="Bob, cyberglass42…">
      <label for="cr-profile-url">Optional public profile/project link</label>
      <input id="cr-profile-url" name="profile_url" type="url" maxlength="300" placeholder="https://…">
      <label class="community-review-check"><input id="cr-persistent-profile" name="persistent_profile" type="checkbox" checked> Keep this identity attached to future accepted reviews so I can build a public contributor history.</label>
    </div>

    <p>No legal name is required. Anonymous submissions remain valid evidence. Persistent identities receive a stable internal contributor ID after the first accepted review, so changing a display name later does not break contribution history.</p>
  </fieldset>

  <fieldset>
    <legend>3. Core Report Card observations</legend>
    <p>Use the same six dimensions as every canonical GlassesResearch Core Report Card. Choose <strong>Not evaluated</strong> when you do not have enough hands-on evidence. Unknown is not zero.</p>
    <div id="cr-dimensions" class="community-review-dimensions">
      <div class="community-review-dimension" data-dimension="discreetness"><h3>Discreetness</h3><p>How closely do these present and function as ordinary eyewear in routine public use?</p><label>Score <select name="score_discreetness" class="community-review-score"></select></label><label>What did you personally observe?<textarea name="note_discreetness" maxlength="900" rows="4"></textarea></label></div>
      <div class="community-review-dimension" data-dimension="camera"><h3>Camera</h3><p>How useful is the outward-facing camera for wearer-perspective capture?</p><label>Score <select name="score_camera" class="community-review-score"></select></label><label>What did you personally observe?<textarea name="note_camera" maxlength="900" rows="4"></textarea></label></div>
      <div class="community-review-dimension" data-dimension="visual_ai"><h3>Visual AI</h3><p>How well can the system understand what the wearer is looking at and turn it into useful machine understanding?</p><label>Score <select name="score_visual_ai" class="community-review-score"></select></label><label>What did you personally observe?<textarea name="note_visual_ai" maxlength="900" rows="4"></textarea></label></div>
      <div class="community-review-dimension" data-dimension="hackability"><h3>Hackability</h3><p>What practical experimentation surface exists: BLE, wired access, SDK/API, firmware paths, sideloading, reverse engineering, or community tooling?</p><label>Score <select name="score_hackability" class="community-review-score"></select></label><label>What did you personally observe?<textarea name="note_hackability" maxlength="900" rows="4"></textarea></label></div>
      <div class="community-review-dimension" data-dimension="owner_control"><h3>Owner Control</h3><p>How much meaningful control remains with the owner: direct access, replaceable AI, local processing, custom endpoints, sideloading, and independence from one prescribed vendor path?</p><label>Score <select name="score_owner_control" class="community-review-score"></select></label><label>What did you personally observe?<textarea name="note_owner_control" maxlength="900" rows="4"></textarea></label></div>
      <div class="community-review-dimension" data-dimension="android_compatibility"><h3>Android Compatibility</h3><p>How deep and reliable is Android support, from companion-app compatibility through direct SDK/device access and owner-controlled integration?</p><label>Score <select name="score_android_compatibility" class="community-review-score"></select></label><label>What did you personally observe?<textarea name="note_android_compatibility" maxlength="900" rows="4"></textarea></label></div>
    </div>
  </fieldset>

  <fieldset>
    <legend>4. Other hands-on evidence</legend>
    <label for="cr-battery">Observed battery life and test conditions</label>
    <textarea id="cr-battery" name="battery_life" maxlength="1200" rows="3" placeholder="Example: 4h 20m with camera off, audio streaming ~50%, Android phone connected…"></textarea>
    <label for="cr-reliability">Reliability, failures, pairing problems, heat, crashes, resets, or quirks</label>
    <textarea id="cr-reliability" name="reliability" maxlength="1200" rows="3"></textarea>
    <label for="cr-missing">What did you reasonably expect these glasses to do that they cannot do?</label>
    <textarea id="cr-missing" name="expected_but_missing" maxlength="1200" rows="3"></textarea>
    <label for="cr-claims">Personally observed claims — one per line</label>
    <textarea id="cr-claims" name="personally_observed_claims" maxlength="3000" rows="5" placeholder="Rear button powers the glasses on/off&#10;BLE advertises as …&#10;Video clips stop after …"></textarea>
    <label for="cr-evidence">Public evidence links — one per line</label>
    <textarea id="cr-evidence" name="evidence_links" maxlength="3000" rows="4" placeholder="Photos, screenshots, logs, public documents, videos, test notes…"></textarea>
    <p>You can attach photographs, screenshots, and other permitted files after the GitHub submission page opens. Please obscure serial numbers, addresses, faces, account identifiers, and other unnecessary personal information.</p>
    <label for="cr-freeform">Anything else?</label>
    <textarea id="cr-freeform" name="freeform" maxlength="1800" rows="5"></textarea>
  </fieldset>

  <fieldset>
    <legend>5. Disclosure and attestation</legend>
    <label for="cr-disclosure">Conflicts or relationships</label>
    <textarea id="cr-disclosure" name="disclosure" maxlength="1200" rows="3" placeholder="Free review unit, vendor employee, affiliate relationship, none, etc."></textarea>
    <label class="community-review-check"><input id="cr-hands-on" type="checkbox" required> I personally used or handled the exact device described above.</label>
    <label class="community-review-check"><input id="cr-observation-attest" type="checkbox" required> I have separated my own observations from things I merely read or heard elsewhere.</label>
    <label class="community-review-check"><input id="cr-rights" type="checkbox" required> I have the right to share any evidence I attach or link.</label>
    <label class="community-review-check"><input id="cr-public" type="checkbox" required> I understand this first-stage submission opens a public GitHub issue for moderation.</label>
  </fieldset>

  <div class="community-review-submit">
    <button type="submit">Continue to GitHub and submit review</button>
    <p id="cr-submit-status" aria-live="polite"></p>
  </div>
</form>

## Prefer to start directly on GitHub?

Use the [Community hands-on review issue form](https://github.com/theGreenJedi/GlassesResearch/issues/new?template=community-review.yml). It asks for the same evidence categories.

## How accepted reviews affect model information

Accepted owner reports remain a distinct community evidence layer. A model page can show the number of accepted independent reviews, ownership-evidence count, individual review provenance, and the **median + sample size + distribution** for each of the six community scores.

Those numbers do not replace the canonical GlassesResearch Report Card. Objective claims are not averaged at all: they remain claim records that can be corroborated, disputed, superseded, or promoted under the [Evidence and Confidence Standard](EVIDENCE_STANDARD.md).

[Browse persistent community contributor histories](/docs/COMMUNITY_REVIEWERS/) · [Read the Report Card Method](REPORT_CARD_METHOD.md) · [Read the Evidence Standard](EVIDENCE_STANDARD.md)
