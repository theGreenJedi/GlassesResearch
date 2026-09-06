(() => {
  const root = document.getElementById('gr-evaluate-app');
  if (!root) return;

  const PROTOCOL = 'GR-EVAL-0.1';
  const STORAGE_KEY = 'glassesresearch-evaluate-draft-v1';
  const dimensions = [
    ['discreetness', 'Discreetness', 'How closely do these present and function as ordinary eyewear in routine public use?'],
    ['camera', 'Camera', 'How useful is the outward-facing camera for wearer-perspective capture?'],
    ['visual_ai', 'Visual AI', 'How well can the system understand what the wearer is looking at and turn it into useful machine understanding?'],
    ['hackability', 'Hackability', 'What practical experimentation surface exists: BLE, wired access, SDK/API, firmware paths, sideloading, reverse engineering, or community tooling?'],
    ['owner_control', 'Owner Control', 'How much meaningful control remains with the owner rather than a prescribed vendor path?'],
    ['android_compatibility', 'Android Compatibility', 'How deep and reliable is Android support, from companion-app compatibility through direct device access?'],
  ];

  const freshState = () => ({
    taskIndex: 0,
    startedAt: new Date().toISOString(),
    answers: {},
    tools: {
      camera: true,
      ruler: false,
      caliper: false,
      scale: false,
      usb_meter: false,
      debug: false,
    },
    attest: {},
  });

  let state = freshState();
  try {
    const saved = JSON.parse(localStorage.getItem(STORAGE_KEY) || 'null');
    if (saved && typeof saved === 'object') {
      state = {
        ...freshState(),
        ...saved,
        answers: { ...freshState().answers, ...(saved.answers || {}) },
        tools: { ...freshState().tools, ...(saved.tools || {}) },
        attest: { ...(saved.attest || {}) },
      };
    }
  } catch (_) {
    state = freshState();
  }

  const requestedModel = new URLSearchParams(window.location.search).get('model');
  if (requestedModel && !state.answers.model) state.answers.model = requestedModel.toUpperCase();

  let catalogRecords = [];
  let aliases = [];
  let lookup = new Map();
  let catalogReady = false;
  let evidenceFiles = [];
  let installPromptEvent = null;

  const save = () => {
    try { localStorage.setItem(STORAGE_KEY, JSON.stringify(state)); } catch (_) { /* local draft is best effort */ }
  };

  const escapeHtml = (value) => String(value ?? '')
    .replaceAll('&', '&amp;')
    .replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;')
    .replaceAll('"', '&quot;')
    .replaceAll("'", '&#039;');

  const normalize = (value) => String(value || '')
    .normalize('NFKD')
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, ' ')
    .trim();

  const answer = (name) => String(state.answers[name] ?? '');
  const checked = (value) => value ? ' checked' : '';
  const selected = (actual, expected) => String(actual) === String(expected) ? ' selected' : '';
  const splitLines = (value) => String(value || '').split(/\r?\n/).map((item) => item.trim()).filter(Boolean);

  function addLookup(key, candidate) {
    const normalized = normalize(key);
    if (!normalized) return;
    const existing = lookup.get(normalized) || [];
    if (!existing.some((item) => item.id === candidate.id)) existing.push(candidate);
    lookup.set(normalized, existing);
  }

  function rebuildLookup() {
    lookup = new Map();
    const byId = new Map();
    for (const record of catalogRecords) {
      const candidate = {
        id: String(record.id || '').toUpperCase(),
        maker: String(record.maker || ''),
        model: String(record.model || ''),
        via: null,
      };
      byId.set(candidate.id, candidate);
      addLookup(candidate.id, candidate);
      addLookup(candidate.model, candidate);
      addLookup(`${candidate.maker} ${candidate.model}`, candidate);
      addLookup(`${candidate.id} ${candidate.maker} ${candidate.model}`, candidate);
    }
    for (const alias of aliases) {
      const candidate = byId.get(String(alias.canonical_id || '').toUpperCase());
      if (!candidate) continue;
      addLookup(alias.alias, { ...candidate, via: String(alias.alias || '') });
    }
  }

  function resolveModel(raw = answer('model')) {
    const value = String(raw || '').trim();
    if (!value) return null;
    const prefixed = value.match(/^(GLS-\d{4})\b/i);
    const key = normalize(prefixed ? prefixed[1] : value);
    const matches = lookup.get(key) || [];
    return matches.length === 1 ? matches[0] : null;
  }

  function modelOptions() {
    const canonical = catalogRecords.map((record) => {
      const id = String(record.id || '').toUpperCase();
      return `<option value="${escapeHtml(`${id} — ${record.maker || ''} ${record.model || ''}`)}"></option>`;
    });
    const aliasOptions = aliases.slice(0, 1200).map((item) => `<option value="${escapeHtml(item.alias || '')}"></option>`);
    return canonical.concat(aliasOptions).join('');
  }

  function textInput(name, label, placeholder = '', options = {}) {
    const type = options.type || 'text';
    const inputMode = options.inputmode ? ` inputmode="${options.inputmode}"` : '';
    const required = options.required ? ' required' : '';
    const suffix = options.suffix ? `<span class="gr-evaluate-unit">${escapeHtml(options.suffix)}</span>` : '';
    return `<label class="gr-evaluate-field"><span>${escapeHtml(label)}${options.required ? ' *' : ''}</span><div class="gr-evaluate-input-wrap"><input type="${type}" data-answer="${escapeHtml(name)}" value="${escapeHtml(answer(name))}" placeholder="${escapeHtml(placeholder)}"${inputMode}${required}>${suffix}</div>${options.hint ? `<small>${escapeHtml(options.hint)}</small>` : ''}</label>`;
  }

  function textArea(name, label, placeholder = '', rows = 5, hint = '') {
    return `<label class="gr-evaluate-field"><span>${escapeHtml(label)}</span><textarea data-answer="${escapeHtml(name)}" rows="${rows}" placeholder="${escapeHtml(placeholder)}">${escapeHtml(answer(name))}</textarea>${hint ? `<small>${escapeHtml(hint)}</small>` : ''}</label>`;
  }

  function selectInput(name, label, options, required = false) {
    return `<label class="gr-evaluate-field"><span>${escapeHtml(label)}${required ? ' *' : ''}</span><select data-answer="${escapeHtml(name)}"${required ? ' required' : ''}>${options.map(([value, text]) => `<option value="${escapeHtml(value)}"${selected(answer(name), value)}>${escapeHtml(text)}</option>`).join('')}</select></label>`;
  }

  function scoreSelect(key) {
    const options = [['', 'Not evaluated']];
    for (let score = 0; score <= 10; score += 1) options.push([String(score), `${score} / 10`]);
    return selectInput(`score_${key}`, 'Community score', options, false);
  }

  function taskList() {
    const tasks = [
      { id: 'model', kicker: 'Specimen 1', title: 'Which glasses are in front of you?', help: 'Resolve the exact specimen before recording observations.' },
      { id: 'context', kicker: 'Specimen 2', title: 'How did you get access to them?', help: 'Usage context and software versions make later observations reproducible.' },
      { id: 'tools', kicker: 'Setup', title: 'What can you examine today?', help: 'Choose only what you actually have. Evaluate will skip optional work you cannot do.' },
      { id: 'evidence', kicker: 'Evidence', title: 'Capture the specimen before testing it.', help: 'Photographs and visible markings anchor identity and physical observations.' },
    ];

    if (state.tools.ruler || state.tools.caliper || state.tools.scale || state.tools.usb_meter) {
      tasks.push({ id: 'measurements', kicker: 'Physical', title: 'Record only the measurements your tools support.', help: 'Unknown is better than an estimate. Leave anything you did not actually measure blank.' });
    }

    for (const [key, label, help] of dimensions) {
      tasks.push({ id: `dimension_${key}`, kicker: 'Report Card observation', title: label, help });
    }

    tasks.push(
      { id: 'behavior', kicker: 'Use', title: 'What happened during real use?', help: 'Failures, battery behavior, and missing capabilities are often more useful than a generic rating.' },
      { id: 'claims', kicker: 'Claims', title: 'Separate what you observed from what you read.', help: 'One observation per line makes later corroboration and dispute handling much easier.' },
      { id: 'attribution', kicker: 'Provenance', title: 'How should this contribution be attributed?', help: 'Anonymous evidence remains valid. Identity history is provenance, never automatic authority.' },
      { id: 'review', kicker: 'Submit', title: 'Review the evidence package.', help: 'Nothing becomes GlassesResearch-verified merely because it is submitted.' },
    );
    return tasks;
  }

  function modelResolutionMarkup() {
    if (!answer('model')) return '<p id="gr-model-resolution" class="gr-evaluate-resolution">Start typing a GLS number, manufacturer + model, or retail alias.</p>';
    if (!catalogReady) return '<p id="gr-model-resolution" class="gr-evaluate-resolution" data-state="pending">Catalog is loading. You can keep entering specimen details.</p>';
    const match = resolveModel();
    if (match) {
      const via = match.via ? ` via the alias “${escapeHtml(match.via)}”` : '';
      return `<p id="gr-model-resolution" class="gr-evaluate-resolution" data-state="resolved">Resolved${via} to <strong>${escapeHtml(match.id)} — ${escapeHtml(match.maker)} ${escapeHtml(match.model)}</strong>.</p>`;
    }
    return `<p id="gr-model-resolution" class="gr-evaluate-resolution" data-state="unresolved">No single canonical model resolves from that name yet. If this is genuinely the exact device, mark it as unresolved and continue.</p>
      <label class="gr-evaluate-check"><input type="checkbox" data-answer-check="unresolved_ack"${checked(Boolean(state.answers.unresolved_ack))}> This exact model is not in the catalog or I cannot resolve it confidently.</label>`;
  }

  function taskMarkup(task) {
    if (task.id === 'model') {
      return `<label class="gr-evaluate-field"><span>Model, GLS number, or retail alias *</span><input id="gr-evaluate-model" data-answer="model" list="gr-evaluate-model-options" value="${escapeHtml(answer('model'))}" autocomplete="off" placeholder="GLS-0039, W610, Ray-Ban Meta…" required><datalist id="gr-evaluate-model-options">${modelOptions()}</datalist></label>
        ${modelResolutionMarkup()}
        ${textInput('retail_name', 'Name printed on the box or listing, if different', 'Retail brand, alias, regional name…')}`;
    }

    if (task.id === 'context') {
      return `${selectInput('ownership_basis', 'How did you access this exact device?', [
          ['', 'Choose…'],
          ['purchased', 'Purchased / personally owned'],
          ['borrowed', 'Borrowed'],
          ['review_sample', 'Review sample / loaner'],
          ['employer_provided', 'Employer / organization provided'],
          ['retailer_demo', 'Retailer / event demo'],
          ['other', 'Other hands-on access'],
        ], true)}
        ${textInput('usage_length', 'Approximate hands-on use', '3 months daily, 2-hour demo…')}
        <div class="gr-evaluate-grid">${textInput('hardware_revision', 'Hardware revision', 'If known')}${textInput('firmware_version', 'Firmware version', 'If known')}${textInput('companion_app_version', 'Companion app + version', 'If used')}${textInput('phone_os', 'Phone / host + OS', 'Pixel 9 Pro XL / Android 16…')}</div>`;
    }

    if (task.id === 'tools') {
      const tools = [
        ['camera', 'Phone or camera', 'Photograph markings, ports, packaging, and physical details.'],
        ['ruler', 'Ruler / measuring tape', 'Useful for coarse frame and temple measurements.'],
        ['caliper', 'Caliper', 'Preferred for repeatable physical dimensions.'],
        ['scale', 'Digital scale', 'Record specimen mass rather than a manufacturer claim.'],
        ['usb_meter', 'USB power meter', 'Observe charging voltage/current when safe and applicable.'],
        ['debug', 'Developer / debug access', 'ADB, BLE tools, SDKs, USB enumeration, logs, or equivalent access.'],
      ];
      return `<div class="gr-evaluate-tool-list">${tools.map(([key, label, hint]) => `<label class="gr-evaluate-tool"><input type="checkbox" data-tool="${key}"${checked(Boolean(state.tools[key]))}><span><strong>${escapeHtml(label)}</strong><small>${escapeHtml(hint)}</small></span></label>`).join('')}</div><p class="gr-evaluate-note">No special equipment is required. Evaluate changes the optional work rather than treating missing tools as missing evidence.</p>`;
    }

    if (task.id === 'evidence') {
      const fileList = evidenceFiles.length
        ? `<ul class="gr-evaluate-file-list">${evidenceFiles.map((file, index) => `<li><span>${escapeHtml(file.name)} <small>${Math.max(1, Math.round(file.size / 1024))} KB</small></span><button type="button" data-action="remove-file" data-file-index="${index}" aria-label="Remove ${escapeHtml(file.name)}">Remove</button></li>`).join('')}</ul>`
        : '<p class="gr-evaluate-empty">No local evidence files selected yet.</p>';
      const camera = state.tools.camera
        ? `<label class="gr-evaluate-capture"><span>Photograph or choose specimen evidence</span><input id="gr-evaluate-photo-input" type="file" accept="image/*" capture="environment" multiple><small>Good first images: front, both temples, interior markings, charging interface, packaging/model label. Files stay on this device until you attach them during submission.</small></label>${fileList}`
        : '<p class="gr-evaluate-note">Camera capture is skipped because you said a camera is not available.</p>';
      return `${camera}${textArea('physical_markings', 'Visible markings, labels, ports, controls, and unusual physical details', 'Example: FCC ID on left temple; two buttons on right arm; USB-C on case…', 5)}`;
    }

    if (task.id === 'measurements') {
      const fields = [];
      if (state.tools.ruler || state.tools.caliper) {
        fields.push(textInput('frame_width_mm', 'Overall frame width', '', { inputmode: 'decimal', suffix: 'mm' }));
        fields.push(textInput('temple_length_mm', 'Temple length', '', { inputmode: 'decimal', suffix: 'mm' }));
        fields.push(textInput('lens_width_mm', 'Lens width', '', { inputmode: 'decimal', suffix: 'mm' }));
        fields.push(textInput('bridge_width_mm', 'Bridge width', '', { inputmode: 'decimal', suffix: 'mm' }));
      }
      if (state.tools.scale) fields.push(textInput('mass_g', 'Specimen mass', '', { inputmode: 'decimal', suffix: 'g', hint: 'Say in notes if this includes prescription lenses or accessories.' }));
      if (state.tools.usb_meter) {
        fields.push(textInput('charge_voltage_v', 'Observed charging voltage', '', { inputmode: 'decimal', suffix: 'V' }));
        fields.push(textInput('charge_current_a', 'Observed charging current', '', { inputmode: 'decimal', suffix: 'A' }));
      }
      return `<div class="gr-evaluate-grid">${fields.join('')}</div>${textArea('measurement_notes', 'Measurement conditions / exceptions', 'Tool used, whether lenses were installed, charging state, repeat measurements…', 4)}`;
    }

    if (task.id.startsWith('dimension_')) {
      const key = task.id.replace('dimension_', '');
      return `<div class="gr-evaluate-dimension-prompt"><p>${escapeHtml(task.help)}</p></div>${scoreSelect(key)}${textArea(`note_${key}`, 'What did you personally observe?', 'Describe the behavior or test that supports the score. Leave the score Not evaluated if you do not have enough evidence.', 6)}`;
    }

    if (task.id === 'behavior') {
      return `${textArea('battery_life', 'Observed battery life and test conditions', '4h 20m with camera off, audio streaming ~50%, Android phone connected…', 4)}${textArea('reliability', 'Reliability, failures, pairing problems, heat, crashes, resets, or quirks', '', 5)}${textArea('expected_but_missing', 'What did you reasonably expect these glasses to do that they cannot do?', '', 4)}`;
    }

    if (task.id === 'claims') {
      const debug = state.tools.debug ? textArea('debug_notes', 'Developer / debug observations', 'BLE names/services, USB enumeration, SDK behavior, ADB, logs, endpoints, firmware access…', 5) : '';
      return `${textArea('personally_observed_claims', 'Personally observed claims — one per line', 'Rear button powers the glasses on/off\nBLE advertises as …\nVideo clips stop after …', 7)}${debug}${textArea('evidence_links', 'Public evidence links — one per line', 'Photos already hosted publicly, screenshots, logs, documents, video, test notes…', 5)}${textArea('freeform', 'Anything else worth preserving?', '', 4)}`;
    }

    if (task.id === 'attribution') {
      const mode = answer('attribution_mode') || 'anonymous';
      const identity = mode === 'anonymous' ? '' : `<div class="gr-evaluate-grid">${textInput('display_name', 'Public display name or handle', 'Bob, cyberglass42…', { required: true })}${textInput('profile_url', 'Optional public profile/project link', 'https://…', { type: 'url' })}</div><label class="gr-evaluate-check"><input type="checkbox" data-answer-check="persistent_profile"${checked(state.answers.persistent_profile !== false)}> Keep this identity attached to future accepted contributions so I can build a public contributor history.</label>`;
      return `${selectInput('attribution_mode', 'Public attribution', [['anonymous', 'Anonymous'], ['pseudonym', 'Persistent handle / pseudonym'], ['identified', 'Public name']], true)}${identity}${textArea('disclosure', 'Conflicts or relationships', 'Free review unit, vendor employee, affiliate relationship, none, etc.', 4)}`;
    }

    if (task.id === 'review') {
      const pkg = buildPackage();
      const model = pkg.specimen.canonical_id ? `${pkg.specimen.canonical_id} — ${pkg.specimen.canonical_name}` : `Unresolved — ${pkg.specimen.entered_model || 'model not entered'}`;
      return `<div class="gr-evaluate-review-summary"><dl><div><dt>Specimen</dt><dd>${escapeHtml(model)}</dd></div><div><dt>Protocol</dt><dd>${PROTOCOL}</dd></div><div><dt>Evidence files queued</dt><dd>${evidenceFiles.length}</dd></div><div><dt>Scored dimensions</dt><dd>${dimensions.filter(([key]) => answer(`score_${key}`) !== '').length} / ${dimensions.length}</dd></div></dl></div>
        <div class="gr-evaluate-attest">
          <label class="gr-evaluate-check"><input type="checkbox" data-attest="hands_on"${checked(Boolean(state.attest.hands_on))}> I personally used or handled the exact device described above.</label>
          <label class="gr-evaluate-check"><input type="checkbox" data-attest="observation_boundary"${checked(Boolean(state.attest.observation_boundary))}> I separated my own observations from things I merely read or heard elsewhere.</label>
          <label class="gr-evaluate-check"><input type="checkbox" data-attest="rights"${checked(Boolean(state.attest.rights))}> I have the right to share any evidence I attach or link.</label>
          <label class="gr-evaluate-check"><input type="checkbox" data-attest="public"${checked(Boolean(state.attest.public))}> I understand the first-stage submission opens a public GitHub issue for moderation.</label>
        </div>
        <p class="gr-evaluate-note">The GitHub handoff opens in a new tab so this session and its local evidence queue remain available while you attach permitted photographs or screenshots.</p>`;
    }

    return '';
  }

  function buildPackage() {
    const canonical = resolveModel();
    const reportCard = {};
    for (const [key, label] of dimensions) {
      reportCard[key] = {
        label,
        score: answer(`score_${key}`) === '' ? null : Number(answer(`score_${key}`)),
        observation: answer(`note_${key}`) || null,
      };
    }
    return {
      schema_version: 1,
      protocol: PROTOCOL,
      evidence_class: 'independent_hands_on',
      started_at: state.startedAt,
      packaged_at: new Date().toISOString(),
      specimen: {
        canonical_id: canonical?.id || null,
        canonical_name: canonical ? `${canonical.maker} ${canonical.model}`.trim() : null,
        entered_model: answer('model') || null,
        retail_name: answer('retail_name') || null,
        unresolved_acknowledged: !canonical ? Boolean(state.answers.unresolved_ack) : false,
        ownership_basis: answer('ownership_basis') || null,
        usage_length: answer('usage_length') || null,
        hardware_revision: answer('hardware_revision') || null,
        firmware_version: answer('firmware_version') || null,
        companion_app_version: answer('companion_app_version') || null,
        phone_os: answer('phone_os') || null,
      },
      tools: { ...state.tools },
      physical: {
        markings: answer('physical_markings') || null,
        frame_width_mm: numberOrNull(answer('frame_width_mm')),
        temple_length_mm: numberOrNull(answer('temple_length_mm')),
        lens_width_mm: numberOrNull(answer('lens_width_mm')),
        bridge_width_mm: numberOrNull(answer('bridge_width_mm')),
        mass_g: numberOrNull(answer('mass_g')),
        charge_voltage_v: numberOrNull(answer('charge_voltage_v')),
        charge_current_a: numberOrNull(answer('charge_current_a')),
        notes: answer('measurement_notes') || null,
      },
      observations: {
        report_card: reportCard,
        battery_life: answer('battery_life') || null,
        reliability: answer('reliability') || null,
        expected_but_missing: answer('expected_but_missing') || null,
        personally_observed_claims: splitLines(answer('personally_observed_claims')),
        debug_notes: answer('debug_notes') || null,
        additional_notes: answer('freeform') || null,
      },
      evidence: {
        local_files_selected: evidenceFiles.map((file) => ({ name: file.name, type: file.type || null, size: file.size, last_modified: file.lastModified || null })),
        public_links: splitLines(answer('evidence_links')),
      },
      contributor: {
        attribution_mode: answer('attribution_mode') || 'anonymous',
        display_name: (answer('attribution_mode') || 'anonymous') === 'anonymous' ? null : (answer('display_name') || null),
        profile_url: answer('profile_url') || null,
        persistent_profile: Boolean(state.answers.persistent_profile),
        disclosure: answer('disclosure') || null,
      },
      attestations: { ...state.attest },
    };
  }

  function numberOrNull(value) {
    if (String(value).trim() === '') return null;
    const parsed = Number(value);
    return Number.isFinite(parsed) ? parsed : null;
  }

  function mdCell(value) {
    return String(value || 'Not provided').replace(/\r?\n/g, ' ').replaceAll('|', '\\|');
  }

  function issueBody(pkg) {
    const canonical = pkg.specimen.canonical_id
      ? `**${pkg.specimen.canonical_id} — ${pkg.specimen.canonical_name}**`
      : `**Unresolved catalog identity — ${pkg.specimen.entered_model || 'Not provided'}**`;
    const scoreRows = dimensions.map(([key, label]) => {
      const item = pkg.observations.report_card[key];
      return `| ${label} | ${item.score === null ? 'Not evaluated' : `${item.score}/10`} | ${mdCell(item.observation)} |`;
    }).join('\n');
    const claims = pkg.observations.personally_observed_claims.length ? pkg.observations.personally_observed_claims.map((item) => `- ${item}`).join('\n') : '- None listed';
    const links = pkg.evidence.public_links.length ? pkg.evidence.public_links.map((item) => `- ${item}`).join('\n') : '- None listed';
    const files = pkg.evidence.local_files_selected.length ? pkg.evidence.local_files_selected.map((item) => `- ${item.name} (${Math.max(1, Math.round(item.size / 1024))} KB)`).join('\n') : '- None selected';
    const machine = JSON.stringify(pkg, null, 2);
    return `## Evidence classification\n\n- Evidence class: **Independent hands-on review**\n- Guided protocol: **${PROTOCOL}**\n- Packaged: ${pkg.packaged_at}\n- Canonical device: ${canonical}\n- Retail name / alias used: ${pkg.specimen.retail_name || 'Not provided'}\n\nThis submission is contributor evidence. It does not become a GlassesResearch verified lab finding merely because it was submitted.\n\n## Specimen context\n\n- Access basis: ${pkg.specimen.ownership_basis || 'Not provided'}\n- Approximate hands-on use: ${pkg.specimen.usage_length || 'Not provided'}\n- Hardware revision: ${pkg.specimen.hardware_revision || 'Not provided'}\n- Firmware: ${pkg.specimen.firmware_version || 'Not provided'}\n- Companion app: ${pkg.specimen.companion_app_version || 'Not provided'}\n- Phone / host + OS: ${pkg.specimen.phone_os || 'Not provided'}\n\n## Physical evidence\n\n**Visible markings / controls / ports**\n\n${pkg.physical.markings || 'Not provided'}\n\n| Measurement | Observed value |\n|---|---:|\n| Overall frame width | ${pkg.physical.frame_width_mm ?? 'Not measured'} mm |\n| Temple length | ${pkg.physical.temple_length_mm ?? 'Not measured'} mm |\n| Lens width | ${pkg.physical.lens_width_mm ?? 'Not measured'} mm |\n| Bridge width | ${pkg.physical.bridge_width_mm ?? 'Not measured'} mm |\n| Specimen mass | ${pkg.physical.mass_g ?? 'Not measured'} g |\n| Charging voltage | ${pkg.physical.charge_voltage_v ?? 'Not measured'} V |\n| Charging current | ${pkg.physical.charge_current_a ?? 'Not measured'} A |\n\nMeasurement notes: ${pkg.physical.notes || 'None'}\n\n## Core Report Card observations\n\n| Dimension | Community score | Personally observed basis |\n|---|---:|---|\n${scoreRows}\n\n## Real-use observations\n\n**Battery life / conditions**\n\n${pkg.observations.battery_life || 'Not provided'}\n\n**Reliability / failures / quirks**\n\n${pkg.observations.reliability || 'Not provided'}\n\n**Expected capability that was missing**\n\n${pkg.observations.expected_but_missing || 'Not provided'}\n\n**Personally observed claims**\n\n${claims}\n\n**Developer / debug observations**\n\n${pkg.observations.debug_notes || 'Not evaluated'}\n\n**Additional notes**\n\n${pkg.observations.additional_notes || 'None'}\n\n## Evidence handoff\n\nFiles selected locally in Evaluate (attach permitted files to this issue before submitting):\n\n${files}\n\nPublic evidence links:\n\n${links}\n\n## Public attribution and disclosure\n\n- Attribution mode: ${pkg.contributor.attribution_mode}\n- Display name / handle: ${pkg.contributor.display_name || 'Anonymous'}\n- Persistent contributor profile requested: ${pkg.contributor.persistent_profile ? 'Yes' : 'No'}\n- Optional public link: ${pkg.contributor.profile_url || 'Not provided'}\n\nDisclosure: ${pkg.contributor.disclosure || 'Not provided'}\n\n## Attestation\n\n- [x] I personally used or handled the exact device described above.\n- [x] I separated my observations from things I merely read or heard elsewhere.\n- [x] I have the right to share evidence I attach or link.\n- [x] I understand this submission is public and will be moderated before incorporation.\n\n<details><summary>Machine-readable evidence package</summary>\n\n\`\`\`json\n${machine}\n\`\`\`\n\n</details>\n\n---\nPrepared with GlassesResearch Evaluate ${PROTOCOL}.\n`;
  }

  function validateTask(task) {
    const error = (message, selector) => {
      const box = root.querySelector('#gr-evaluate-error');
      if (box) box.textContent = message;
      const target = selector ? root.querySelector(selector) : null;
      if (target) target.focus();
      return false;
    };
    if (task.id === 'model') {
      if (!answer('model').trim()) return error('Enter the exact model, GLS number, or retail alias.', '#gr-evaluate-model');
      if (catalogReady && !resolveModel() && !state.answers.unresolved_ack) return error('Resolve the model from the catalog, or confirm that the exact model remains unresolved.', '[data-answer-check="unresolved_ack"]');
    }
    if (task.id === 'context' && !answer('ownership_basis')) return error('Choose how you accessed this exact device.', '[data-answer="ownership_basis"]');
    if (task.id === 'attribution') {
      const mode = answer('attribution_mode') || 'anonymous';
      if (mode !== 'anonymous' && !answer('display_name').trim()) return error('Add the public name or handle you want attached to this contribution.', '[data-answer="display_name"]');
    }
    return true;
  }

  function validateSubmission() {
    if (!answer('model').trim()) return 'The specimen model is missing.';
    if (catalogReady && !resolveModel() && !state.answers.unresolved_ack) return 'The model is unresolved and has not been acknowledged as such.';
    if (!answer('ownership_basis')) return 'The specimen access basis is missing.';
    const mode = answer('attribution_mode') || 'anonymous';
    if (mode !== 'anonymous' && !answer('display_name').trim()) return 'Public attribution requires a display name or handle.';
    const missing = ['hands_on', 'observation_boundary', 'rights', 'public'].filter((key) => !state.attest[key]);
    if (missing.length) return 'Complete all four attestations before submitting.';
    return '';
  }

  function render() {
    const tasks = taskList();
    state.taskIndex = Math.max(0, Math.min(state.taskIndex, tasks.length - 1));
    const task = tasks[state.taskIndex];
    const percent = Math.round(((state.taskIndex + 1) / tasks.length) * 100);
    const installButton = installPromptEvent ? '<button type="button" class="gr-evaluate-quiet" data-action="install">Install app</button>' : '';
    const isReview = task.id === 'review';
    root.innerHTML = `<section class="gr-evaluate-shell" aria-labelledby="gr-evaluate-task-title">
      <div class="gr-evaluate-topline">
        <div><span class="gr-evaluate-brand">GlassesResearch Evaluate</span><small>${PROTOCOL} · draft saved locally</small></div>
        <div class="gr-evaluate-top-actions">${installButton}<button type="button" class="gr-evaluate-quiet" data-action="new-session">New session</button></div>
      </div>
      <div class="gr-evaluate-progress" aria-label="Evaluation progress"><span style="width:${percent}%"></span></div>
      <div class="gr-evaluate-progress-copy">Task ${state.taskIndex + 1} of ${tasks.length}</div>
      <article class="gr-evaluate-task">
        <p class="gr-evaluate-kicker">${escapeHtml(task.kicker)}</p>
        <h2 id="gr-evaluate-task-title">${escapeHtml(task.title)}</h2>
        <p class="gr-evaluate-help">${escapeHtml(task.help)}</p>
        <div class="gr-evaluate-task-body">${taskMarkup(task)}</div>
        <p id="gr-evaluate-error" class="gr-evaluate-error" aria-live="polite"></p>
      </article>
      <div class="gr-evaluate-nav">
        <button type="button" data-action="back"${state.taskIndex === 0 ? ' disabled' : ''}>Back</button>
        <div class="gr-evaluate-nav-right">${isReview ? '<button type="button" class="gr-evaluate-secondary" data-action="download">Download evidence package</button><button type="button" class="gr-evaluate-primary" data-action="submit">Continue to moderated submission</button>' : '<button type="button" class="gr-evaluate-primary" data-action="next">Next</button>'}</div>
      </div>
    </section>`;
    save();
    if (task.id === 'model') syncModelResolution();
  }

  function syncModelResolution() {
    const box = root.querySelector('#gr-model-resolution');
    if (!box) return;
    const modelValue = answer('model').trim();
    if (!modelValue) {
      box.dataset.state = '';
      box.textContent = 'Start typing a GLS number, manufacturer + model, or retail alias.';
      return;
    }
    if (!catalogReady) {
      box.dataset.state = 'pending';
      box.textContent = 'Catalog is loading. You can keep entering specimen details.';
      return;
    }
    const match = resolveModel(modelValue);
    if (match) {
      box.dataset.state = 'resolved';
      box.textContent = `${match.via ? `${match.via} resolves to ` : 'Resolved to '}${match.id} — ${match.maker} ${match.model}.`;
      state.answers.unresolved_ack = false;
      save();
      const ack = root.querySelector('[data-answer-check="unresolved_ack"]');
      if (ack) ack.closest('label')?.remove();
      return;
    }
    box.dataset.state = 'unresolved';
    box.textContent = 'No single canonical model resolves from that name yet. If this is genuinely the exact device, mark it as unresolved and continue.';
    if (!root.querySelector('[data-answer-check="unresolved_ack"]')) {
      box.insertAdjacentHTML('afterend', `<label class="gr-evaluate-check"><input type="checkbox" data-answer-check="unresolved_ack"${checked(Boolean(state.answers.unresolved_ack))}> This exact model is not in the catalog or I cannot resolve it confidently.</label>`);
    }
  }

  root.addEventListener('input', (event) => {
    const target = event.target;
    if (target.matches('[data-answer]')) {
      state.answers[target.dataset.answer] = target.value;
      save();
      if (target.dataset.answer === 'model') syncModelResolution();
    }
  });

  root.addEventListener('change', (event) => {
    const target = event.target;
    if (target.matches('[data-answer]')) {
      state.answers[target.dataset.answer] = target.value;
      save();
      if (target.dataset.answer === 'attribution_mode') render();
      if (target.dataset.answer === 'model') syncModelResolution();
    }
    if (target.matches('[data-answer-check]')) {
      state.answers[target.dataset.answerCheck] = target.checked;
      save();
    }
    if (target.matches('[data-tool]')) {
      state.tools[target.dataset.tool] = target.checked;
      save();
    }
    if (target.matches('[data-attest]')) {
      state.attest[target.dataset.attest] = target.checked;
      save();
    }
    if (target.id === 'gr-evaluate-photo-input') {
      for (const file of Array.from(target.files || [])) {
        if (!evidenceFiles.some((item) => item.name === file.name && item.size === file.size && item.lastModified === file.lastModified)) evidenceFiles.push(file);
      }
      render();
    }
  });

  root.addEventListener('click', async (event) => {
    const button = event.target.closest('[data-action]');
    if (!button) return;
    const action = button.dataset.action;
    const tasks = taskList();
    const task = tasks[Math.max(0, Math.min(state.taskIndex, tasks.length - 1))];

    if (action === 'back') {
      state.taskIndex = Math.max(0, state.taskIndex - 1);
      render();
      root.scrollIntoView({ behavior: 'smooth', block: 'start' });
      return;
    }
    if (action === 'next') {
      if (!validateTask(task)) return;
      state.taskIndex = Math.min(taskList().length - 1, state.taskIndex + 1);
      render();
      root.scrollIntoView({ behavior: 'smooth', block: 'start' });
      return;
    }
    if (action === 'remove-file') {
      evidenceFiles.splice(Number(button.dataset.fileIndex), 1);
      render();
      return;
    }
    if (action === 'new-session') {
      if (!window.confirm('Clear this local draft and start a new evaluation?')) return;
      state = freshState();
      evidenceFiles = [];
      save();
      render();
      return;
    }
    if (action === 'download') {
      const pkg = buildPackage();
      const blob = new Blob([JSON.stringify(pkg, null, 2)], { type: 'application/json' });
      const link = document.createElement('a');
      link.href = URL.createObjectURL(blob);
      link.download = `${pkg.specimen.canonical_id || 'unresolved'}-${PROTOCOL}-evidence.json`;
      document.body.append(link);
      link.click();
      link.remove();
      setTimeout(() => URL.revokeObjectURL(link.href), 1000);
      return;
    }
    if (action === 'submit') {
      const problem = validateSubmission();
      const error = root.querySelector('#gr-evaluate-error');
      if (problem) {
        if (error) error.textContent = problem;
        return;
      }
      const pkg = buildPackage();
      const body = issueBody(pkg);
      const titleModel = pkg.specimen.canonical_id ? `${pkg.specimen.canonical_id} — ${pkg.specimen.canonical_name}` : `Unresolved — ${pkg.specimen.entered_model}`;
      const title = `[Community evaluation] ${titleModel}`;
      const url = `https://github.com/theGreenJedi/GlassesResearch/issues/new?title=${encodeURIComponent(title)}&body=${encodeURIComponent(body)}`;
      if (url.length > 30000) {
        if (error) error.textContent = 'This package is too large for the GitHub handoff URL. Download the evidence package, shorten long free-form notes slightly, then submit again.';
        return;
      }
      const opened = window.open(url, '_blank', 'noopener');
      if (!opened) window.location.assign(url);
      if (error) error.textContent = 'Submission opened. Attach the permitted local evidence files listed in this session before you submit the GitHub issue.';
      return;
    }
    if (action === 'install' && installPromptEvent) {
      installPromptEvent.prompt();
      await installPromptEvent.userChoice.catch(() => null);
      installPromptEvent = null;
      render();
    }
  });

  window.addEventListener('beforeinstallprompt', (event) => {
    event.preventDefault();
    installPromptEvent = event;
    render();
  });

  function enablePwa() {
    if (!document.querySelector('link[rel="manifest"][data-gr-evaluate]')) {
      const manifest = document.createElement('link');
      manifest.rel = 'manifest';
      manifest.href = '/docs/evaluate.webmanifest';
      manifest.dataset.grEvaluate = 'true';
      document.head.append(manifest);
    }
    if ('serviceWorker' in navigator) {
      navigator.serviceWorker.register('/docs/evaluate-sw.js', { scope: '/docs/' }).catch(() => null);
    }
  }

  Promise.all([
    fetch('/data/devices.json', { cache: 'no-store' }).then((response) => response.ok ? response.json() : Promise.reject(new Error('device catalog unavailable'))),
    fetch('/data/lineage-aliases.json', { cache: 'no-store' }).then((response) => response.ok ? response.json() : { aliases: [] }),
  ]).then(([deviceDoc, aliasDoc]) => {
    catalogRecords = Array.isArray(deviceDoc.records) ? deviceDoc.records : [];
    aliases = Array.isArray(aliasDoc.aliases) ? aliasDoc.aliases : [];
    rebuildLookup();
    catalogReady = true;
    if (taskList()[state.taskIndex]?.id === 'model') render();
  }).catch(() => {
    catalogReady = true;
    if (taskList()[state.taskIndex]?.id === 'model') render();
  });

  enablePwa();
  render();
})();
