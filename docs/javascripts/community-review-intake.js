(() => {
  const form = document.getElementById('community-review-intake');
  if (!form) return;

  const dimensions = [
    ['discreetness', 'Discreetness'],
    ['camera', 'Camera'],
    ['visual_ai', 'Visual AI'],
    ['hackability', 'Hackability'],
    ['owner_control', 'Owner Control'],
    ['android_compatibility', 'Android Compatibility'],
  ];
  const modelInput = document.getElementById('cr-model');
  const modelIdInput = document.getElementById('cr-canonical-id');
  const modelResolution = document.getElementById('cr-model-resolution');
  const datalist = document.getElementById('cr-model-options');
  const attribution = document.getElementById('cr-attribution');
  const identityFields = document.getElementById('cr-identity-fields');
  const displayName = document.getElementById('cr-display-name');
  const status = document.getElementById('cr-submit-status');

  for (const select of form.querySelectorAll('.community-review-score')) {
    select.append(new Option('Not evaluated', ''));
    for (let score = 0; score <= 10; score += 1) select.append(new Option(String(score), String(score)));
  }

  const normalize = (value) => String(value || '')
    .normalize('NFKD')
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, ' ')
    .trim();

  let records = [];
  let aliases = [];
  let lookup = new Map();

  function addLookup(key, candidate) {
    const normalized = normalize(key);
    if (!normalized) return;
    const existing = lookup.get(normalized) || [];
    if (!existing.some((item) => item.id === candidate.id)) existing.push(candidate);
    lookup.set(normalized, existing);
  }

  function canonicalCandidate(record) {
    return {
      id: String(record.id || '').toUpperCase(),
      maker: String(record.maker || ''),
      model: String(record.model || ''),
      via: null,
    };
  }

  function rebuildLookup() {
    lookup = new Map();
    datalist.replaceChildren();
    const deviceById = new Map(records.map((record) => [String(record.id || '').toUpperCase(), record]));
    for (const record of records) {
      const candidate = canonicalCandidate(record);
      addLookup(candidate.id, candidate);
      addLookup(`${candidate.maker} ${candidate.model}`, candidate);
      addLookup(`${candidate.id} ${candidate.maker} ${candidate.model}`, candidate);
      addLookup(candidate.model, candidate);
      const option = document.createElement('option');
      option.value = `${candidate.id} — ${candidate.maker} ${candidate.model}`;
      datalist.append(option);
    }
    for (const alias of aliases) {
      const id = String(alias.canonical_id || '').toUpperCase();
      const record = deviceById.get(id);
      if (!record) continue;
      const candidate = canonicalCandidate(record);
      candidate.via = String(alias.alias || '');
      addLookup(alias.alias, candidate);
      const option = document.createElement('option');
      option.value = String(alias.alias || '');
      option.label = `${id} — ${candidate.maker} ${candidate.model}`;
      datalist.append(option);
    }
  }

  function resolveModel() {
    modelIdInput.value = '';
    const raw = modelInput.value.trim();
    if (!raw) {
      modelResolution.textContent = 'Choose the exact model you used. Retail aliases are welcome.';
      modelResolution.dataset.state = '';
      return null;
    }
    let key = normalize(raw);
    const prefixed = raw.match(/^(GLS-\d{4})\b/i);
    if (prefixed) key = normalize(prefixed[1]);
    const matches = lookup.get(key) || [];
    if (matches.length !== 1) {
      modelResolution.textContent = matches.length > 1
        ? 'That name matches more than one canonical model. Choose the GLS-labelled option from the list.'
        : 'Model not resolved yet. Choose a canonical model or known retail alias from the suggestions.';
      modelResolution.dataset.state = 'unresolved';
      return null;
    }
    const match = matches[0];
    modelIdInput.value = match.id;
    modelResolution.textContent = match.via
      ? `${match.via} resolves to ${match.id} — ${match.maker} ${match.model}. Your review will attach to that canonical record.`
      : `Resolved to ${match.id} — ${match.maker} ${match.model}.`;
    modelResolution.dataset.state = 'resolved';
    return match;
  }

  Promise.all([
    fetch('/data/devices.json', { cache: 'no-store' }).then((response) => response.ok ? response.json() : Promise.reject(new Error('device catalog unavailable'))),
    fetch('/data/lineage-aliases.json', { cache: 'no-store' }).then((response) => response.ok ? response.json() : { aliases: [] }),
  ]).then(([deviceDoc, aliasDoc]) => {
    records = Array.isArray(deviceDoc.records) ? deviceDoc.records : [];
    aliases = Array.isArray(aliasDoc.aliases) ? aliasDoc.aliases : [];
    rebuildLookup();
    const requested = new URLSearchParams(window.location.search).get('model');
    if (requested) {
      modelInput.value = requested.toUpperCase();
      resolveModel();
    }
  }).catch(() => {
    modelResolution.textContent = 'The live catalog could not be loaded. You can still use the direct GitHub review form below.';
    modelResolution.dataset.state = 'unresolved';
  });

  modelInput.addEventListener('input', resolveModel);
  modelInput.addEventListener('change', resolveModel);

  function syncIdentity() {
    const identified = attribution.value !== 'anonymous';
    identityFields.hidden = !identified;
    displayName.required = identified;
    if (!identified) displayName.value = '';
  }
  attribution.addEventListener('change', syncIdentity);
  syncIdentity();

  const value = (name) => String(new FormData(form).get(name) || '').trim();
  const lines = (name) => value(name).split(/\r?\n/).map((item) => item.trim()).filter(Boolean);
  const safe = (text) => text || 'Not provided';
  const rating = (dimension) => {
    const raw = value(`score_${dimension}`);
    return raw === '' ? 'Not evaluated' : `${raw}/10`;
  };

  function reviewBody(canonical) {
    const mode = value('attribution_mode');
    const name = mode === 'anonymous' ? 'Anonymous' : safe(value('display_name'));
    const persistent = mode !== 'anonymous' && document.getElementById('cr-persistent-profile').checked ? 'Yes' : 'No';
    const observedClaims = lines('personally_observed_claims');
    const evidenceLinks = lines('evidence_links');
    const scoreRows = dimensions.map(([key, label]) => `| ${label} | ${rating(key)} | ${safe(value(`note_${key}`))} |`).join('\n');
    return `## Canonical device\n\n- Canonical model: **${canonical.id} — ${canonical.maker} ${canonical.model}**\n- Retail name / alias used: ${safe(value('retail_name'))}\n- Access basis: ${safe(value('ownership_basis'))}\n- Approximate hands-on use: ${safe(value('usage_length'))}\n- Hardware revision: ${safe(value('hardware_revision'))}\n- Firmware: ${safe(value('firmware_version'))}\n- Companion app: ${safe(value('companion_app_version'))}\n- Phone / host + OS: ${safe(value('phone_os'))}\n\n## Public attribution\n\n- Attribution mode: ${mode}\n- Display name / handle: ${name}\n- Persistent contributor profile requested: ${persistent}\n- Optional public link: ${safe(value('profile_url'))}\n\nNo private email address is included in this public issue. A persistent contributor ID is assigned only after an accepted review.\n\n## Core Report Card observations\n\n| Dimension | Community score | Personally observed basis |\n|---|---:|---|\n${scoreRows}\n\nCommunity scores are independent evidence and do not overwrite the canonical GlassesResearch Report Card.\n\n## Other hands-on evidence\n\n**Battery life / conditions**\n\n${safe(value('battery_life'))}\n\n**Reliability / failures / quirks**\n\n${safe(value('reliability'))}\n\n**Expected capability that was missing**\n\n${safe(value('expected_but_missing'))}\n\n**Personally observed claims**\n\n${observedClaims.length ? observedClaims.map((item) => `- ${item}`).join('\n') : '- None listed'}\n\n**Public evidence links**\n\n${evidenceLinks.length ? evidenceLinks.map((item) => `- ${item}`).join('\n') : '- None listed yet; files may be attached to this issue before submission.'}\n\n**Additional review notes**\n\n${safe(value('freeform'))}\n\n## Disclosure\n\n${safe(value('disclosure'))}\n\n## Attestation\n\n- [x] I personally used or handled the exact device described above.\n- [x] I separated my observations from things I merely read or heard elsewhere.\n- [x] I have the right to share evidence I attach or link.\n- [x] I understand this submission is public and will be moderated before incorporation.\n\n---\nStructured with the GlassesResearch Community Hands-On Review Intake.\n`;
  }

  form.addEventListener('submit', (event) => {
    event.preventDefault();
    if (!form.reportValidity()) return;
    const canonical = resolveModel();
    if (!canonical) {
      status.textContent = 'Choose a model that resolves to one canonical GLS record before continuing.';
      modelInput.focus();
      return;
    }
    const mode = value('attribution_mode');
    if (mode !== 'anonymous' && !value('display_name')) {
      status.textContent = 'Add the public name or handle you want attached to this review.';
      displayName.focus();
      return;
    }
    const body = reviewBody(canonical);
    const title = `[Community review] ${canonical.id} — ${canonical.maker} ${canonical.model}`;
    const url = `https://github.com/theGreenJedi/GlassesResearch/issues/new?title=${encodeURIComponent(title)}&body=${encodeURIComponent(body)}`;
    if (url.length > 30000) {
      status.textContent = 'This review is too long for the handoff URL. Shorten the free-form fields slightly, then try again; evidence files can be attached on GitHub.';
      return;
    }
    status.textContent = 'Opening the structured GitHub submission. Attach permitted evidence there, review the public text, then submit the issue.';
    window.location.assign(url);
  });
})();
