(() => {
  const root = document.getElementById('fieldwork-app');
  if (!root) return;

  const form = document.getElementById('fw-form');
  const mount = document.getElementById('fw-questionnaire');
  const nav = document.getElementById('fw-section-nav');
  const scoreEl = document.getElementById('fw-score');
  const progressEl = document.getElementById('fw-progress');
  const statusEl = document.getElementById('fw-status');
  const saveButton = document.getElementById('fw-save');
  const exportButton = document.getElementById('fw-export');
  const storageKey = 'glassesresearch.fieldwork.v1.draft';

  let instrument = null;
  let modelRecords = [];
  let deviceFingerprint = '';
  let fingerprintSource = '';

  const esc = (value) => String(value ?? '').replace(/[&<>"']/g, (c) => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const slug = (value) => String(value || '').replace(/[^a-z0-9_-]/gi, '-');
  const normalize = (value) => String(value || '').normalize('NFKC').trim().toUpperCase();

  function optionMarkup(options = []) {
    return options.map((option) => `<option value="${esc(option)}">${esc(option.replaceAll('_', ' '))}</option>`).join('');
  }

  function fieldMarkup(question) {
    const id = `fw-${slug(question.id)}`;
    const required = question.required ? ' required' : '';
    const common = `id="${id}" name="${esc(question.id)}" data-question-id="${esc(question.id)}"${required}`;
    const unknown = '<option value="">Choose…</option>';
    switch (question.type) {
      case 'textarea':
      case 'long_textarea':
      case 'links':
        return `<textarea ${common} rows="${question.type === 'long_textarea' ? 8 : 4}"></textarea>`;
      case 'choice':
        return `<select ${common}>${unknown}${optionMarkup(question.options)}</select>`;
      case 'choice_with_note':
        return `<select ${common}>${unknown}${optionMarkup(question.options)}</select><textarea name="${esc(question.id)}__note" data-question-id="${esc(question.id)}__note" rows="2" placeholder="Optional context"></textarea>`;
      case 'yes_no_unknown':
        return `<select ${common}>${unknown}<option value="yes">Yes</option><option value="no">No</option><option value="unknown">I don't know / not tested</option></select>`;
      case 'checkbox':
        return `<label class="fieldwork-check"><input type="checkbox" ${common}> ${esc(question.prompt)}</label>`;
      case 'rating_with_note':
        return `<select ${common}>${unknown}<option value="not_tested">I don't know / not tested</option>${Array.from({length:11},(_,i)=>`<option value="${i}">${i}/10</option>`).join('')}</select><textarea name="${esc(question.id)}__note" data-question-id="${esc(question.id)}__note" rows="2" placeholder="Optional context"></textarea>`;
      case 'money':
        return `<input ${common} type="text" inputmode="decimal" placeholder="Example: 299 USD">`;
      case 'month_or_date':
        return `<input ${common} type="text" placeholder="YYYY-MM or YYYY-MM-DD">`;
      case 'serial_private':
        return `<input ${common} type="text" autocomplete="off" spellcheck="false" aria-describedby="${id}-privacy"><small id="${id}-privacy">Used only in this browser to derive a one-way duplicate-device fingerprint. Raw serial is excluded from saves and exports.</small>`;
      case 'model_lookup':
        return `<input ${common} type="text" list="fw-models" autocomplete="off"><datalist id="fw-models"></datalist>`;
      default:
        return `<input ${common} type="text">`;
    }
  }

  function render() {
    mount.innerHTML = instrument.sections.map((section, index) => {
      const questions = section.questions.map((question) => {
        const checkbox = question.type === 'checkbox';
        return `<div class="fieldwork-question" data-question="${esc(question.id)}">
          ${checkbox ? '' : `<label for="fw-${slug(question.id)}">${esc(question.prompt)}${question.required ? ' <span aria-label="required">*</span>' : ''}</label>`}
          ${fieldMarkup(question)}
        </div>`;
      }).join('');
      return `<section class="fieldwork-section" id="fw-section-${esc(section.id)}" data-section-index="${index}">
        <details ${index < 2 ? 'open' : ''}>
          <summary><span>${index + 1}</span> ${esc(section.title)} <em class="fw-section-count"></em></summary>
          <div class="fieldwork-section__body">${questions}</div>
        </details>
      </section>`;
    }).join('');

    nav.innerHTML = instrument.sections.map((section, index) => `<a href="#fw-section-${esc(section.id)}">${index + 1}. ${esc(section.title)}</a>`).join('');
    const datalist = document.getElementById('fw-models');
    if (datalist) datalist.innerHTML = modelRecords.map((record) => `<option value="${esc(`${record.id} — ${record.maker} ${record.model}`)}"></option>`).join('');

    const attribution = form.elements.attribution_mode;
    if (attribution) attribution.value = instrument.privacy.default_attribution || 'anonymous';
    syncConditionalFields();
    restoreDraft();
    updateProgress();
  }

  function fieldValue(element) {
    if (!element) return '';
    if (element.type === 'checkbox') return element.checked;
    return String(element.value || '').trim();
  }

  function answered(question) {
    if (question.type === 'serial_private') return Boolean(deviceFingerprint);
    const element = form.elements[question.id];
    if (!element) return false;
    if (question.type === 'checkbox') return element.checked;
    return Boolean(String(element.value || '').trim());
  }

  function requiredValid() {
    return instrument.completion.minimum_fields.every((id) => {
      if (id === 'serial') return true;
      const el = form.elements[id];
      return el && (el.type === 'checkbox' ? el.checked : String(el.value || '').trim());
    });
  }

  function updateProgress() {
    const questions = instrument.sections.flatMap((section) => section.questions);
    const optional = questions.filter((q) => !q.required);
    const optionalAnswered = optional.filter(answered).length;
    const score = Math.min(100, Math.round(50 + (optional.length ? (optionalAnswered / optional.length) * 50 : 50)));
    scoreEl.textContent = `${score}%`;
    progressEl.value = score;
    progressEl.textContent = `${score}%`;
    statusEl.textContent = requiredValid()
      ? `Valid hands-on contribution. ${optionalAnswered} of ${optional.length} optional questions answered.`
      : 'Answer the exact model, hands-on access basis, and hands-on attestation to create a valid contribution.';

    for (const section of instrument.sections) {
      const node = document.getElementById(`fw-section-${section.id}`);
      const count = node?.querySelector('.fw-section-count');
      if (!count) continue;
      const done = section.questions.filter(answered).length;
      count.textContent = `${done}/${section.questions.length}`;
    }
  }

  async function hashSerialIfReady() {
    const serial = String(form.elements.serial?.value || '').trim();
    const model = String(form.elements.model?.value || '').trim();
    if (!serial || !model || !crypto?.subtle) {
      deviceFingerprint = '';
      fingerprintSource = '';
      return;
    }
    const source = `${normalize(model)}\u241f${normalize(serial)}`;
    if (source === fingerprintSource && deviceFingerprint) return;
    const digest = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(source));
    deviceFingerprint = [...new Uint8Array(digest)].map((byte) => byte.toString(16).padStart(2, '0')).join('');
    fingerprintSource = source;
  }

  function serialize() {
    const answers = {};
    for (const section of instrument.sections) {
      for (const question of section.questions) {
        if (question.type === 'serial_private') continue;
        const el = form.elements[question.id];
        if (!el) continue;
        const value = fieldValue(el);
        if (value !== '' && value !== false) answers[question.id] = value;
        const note = form.elements[`${question.id}__note`];
        if (note && String(note.value || '').trim()) answers[`${question.id}__note`] = String(note.value).trim();
      }
    }
    return {
      schema_version: instrument.schema_version,
      product: 'Fieldwork',
      created_at: new Date().toISOString(),
      completion_percent: Number(progressEl.value),
      device_fingerprint: deviceFingerprint || null,
      raw_serial_retained: false,
      attribution_mode: answers.attribution_mode || 'anonymous',
      answers,
    };
  }

  function saveDraft() {
    const payload = serialize();
    localStorage.setItem(storageKey, JSON.stringify(payload));
    statusEl.textContent = 'Draft saved only on this device. Raw serial was not saved.';
  }

  function restoreDraft() {
    let payload;
    try { payload = JSON.parse(localStorage.getItem(storageKey) || 'null'); } catch { return; }
    if (!payload?.answers) return;
    for (const [key, value] of Object.entries(payload.answers)) {
      const el = form.elements[key];
      if (!el) continue;
      if (el.type === 'checkbox') el.checked = Boolean(value);
      else el.value = String(value);
    }
    deviceFingerprint = String(payload.device_fingerprint || '');
    fingerprintSource = '';
    syncConditionalFields();
  }

  function syncConditionalFields() {
    const mode = String(form.elements.attribution_mode?.value || 'anonymous');
    const display = form.elements.display_name?.closest('.fieldwork-question');
    if (display) display.hidden = mode === 'anonymous';
  }

  function downloadExport() {
    if (!requiredValid()) {
      statusEl.textContent = 'Complete the three required hands-on fields before exporting.';
      return;
    }
    const payload = serialize();
    const blob = new Blob([JSON.stringify(payload, null, 2)], {type: 'application/json'});
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `fieldwork-${new Date().toISOString().slice(0,10)}.json`;
    document.body.appendChild(a);
    a.click();
    a.remove();
    URL.revokeObjectURL(url);
    statusEl.textContent = 'Contribution package exported. It contains the fingerprint, never the raw serial.';
  }

  form.addEventListener('input', async (event) => {
    if (event.target.name === 'serial' || event.target.name === 'model') await hashSerialIfReady();
    if (event.target.name === 'attribution_mode') syncConditionalFields();
    updateProgress();
  });
  form.addEventListener('change', async () => { await hashSerialIfReady(); updateProgress(); });
  form.addEventListener('reset', () => {
    setTimeout(() => {
      localStorage.removeItem(storageKey);
      deviceFingerprint = '';
      fingerprintSource = '';
      syncConditionalFields();
      updateProgress();
      statusEl.textContent = 'Draft cleared from this device.';
    }, 0);
  });
  saveButton.addEventListener('click', async () => { await hashSerialIfReady(); saveDraft(); });
  exportButton.addEventListener('click', async () => { await hashSerialIfReady(); downloadExport(); });

  Promise.all([
    fetch('/data/fieldwork-questionnaire.v1.json', {cache: 'no-store'}).then((r) => { if (!r.ok) throw new Error('questionnaire unavailable'); return r.json(); }),
    fetch('/data/devices.json', {cache: 'no-store'}).then((r) => r.ok ? r.json() : {records: []}),
  ]).then(([questionnaire, devices]) => {
    instrument = questionnaire;
    modelRecords = Array.isArray(devices.records) ? devices.records : [];
    render();
  }).catch((error) => {
    mount.innerHTML = `<p role="alert">Fieldwork could not load its research instrument. ${esc(error.message)}</p>`;
    statusEl.textContent = 'App unavailable.';
  });
})();
