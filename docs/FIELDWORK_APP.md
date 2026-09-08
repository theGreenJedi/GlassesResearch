# Fieldwork App

<div class="fieldwork-app" id="fieldwork-app">
  <header class="fieldwork-app__header">
    <p class="fieldwork-app__eyebrow">GlassesResearch community field research</p>
    <h1>Fieldwork</h1>
    <p>Contribute what you know about the smart glasses in your hands. Five minutes helps. Go deeper only if you want to.</p>
    <div class="fieldwork-privacy-promise" role="note" aria-label="Fieldwork privacy promise">
      <strong>Anonymous is welcome.</strong><br>
      <strong>Attribution is optional.</strong><br>
      <strong>Raw serial numbers are never retained.</strong>
    </div>
    <button type="button" id="fw-install" hidden>Install Fieldwork</button>
  </header>

  <section class="fieldwork-app__status" aria-live="polite">
    <div><strong>Completion</strong> <span id="fw-score">50%</span></div>
    <progress id="fw-progress" value="50" max="100">50%</progress>
    <p id="fw-status">Answer the three required hands-on fields to create a valid contribution.</p>
  </section>

  <nav class="fieldwork-app__sections" id="fw-section-nav" aria-label="Fieldwork sections"></nav>

  <form id="fw-form" novalidate>
    <div id="fw-questionnaire"></div>

    <section class="fieldwork-app__actions">
      <button type="button" id="fw-save">Save on this device</button>
      <button type="button" id="fw-export">Export contribution package</button>
      <button type="reset" id="fw-clear">Clear draft</button>
    </section>
  </form>

  <section class="fieldwork-app__handoff">
    <h2>Submission status</h2>
    <p><strong>Anonymous direct submission is not enabled yet.</strong> The app is functional for data collection, local drafts, privacy-preserving serial fingerprinting, and structured export. GlassesResearch will not advertise Fieldwork publicly until the anonymous submission endpoint is live.</p>
  </section>
</div>

<script src="../javascripts/fieldwork-app.js"></script>
<script src="../javascripts/fieldwork-pwa.js"></script>
