(() => {
  const form = document.getElementById('fw-form');
  const button = document.getElementById('fw-export');
  const status = document.getElementById('fw-status');
  if (!form || !button) return;

  const normalize = (value) => String(value || '').normalize('NFKC').trim().toUpperCase();
  const text = (name) => String(form.elements[name]?.value || '').trim();
  const bool = (name) => Boolean(form.elements[name]?.checked);

  async function fingerprint() {
    const model = text('model');
    const serial = text('serial');
    if (!model || !serial || !crypto?.subtle) return null;
    const source = `${normalize(model)}\u241f${normalize(serial)}`;
    const digest = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(source));
    return [...new Uint8Array(digest)].map((byte) => byte.toString(16).padStart(2, '0')).join('');
  }

  function canonicalId() {
    const match = text('model').match(/\b(GLS-\d{4})\b/i);
    return match ? match[1].toUpperCase() : null;
  }

  function completion() {
    return Math.max(50, Math.min(100, Number(document.getElementById('fw-progress')?.value || 50)));
  }

  function answers() {
    const out = {};
    const forbidden = new Set(['serial', 'model', 'retail_name', 'model_number', 'access_basis', 'attribution_mode', 'display_name', 'attestation_hands_on', 'attestation_observation', 'evidence_links']);
    for (const element of form.elements) {
      if (!element.name || forbidden.has(element.name)) continue;
      if (element.type === 'checkbox') {
        if (element.checked) out[element.name] = true;
      } else {
        const value = String(element.value || '').trim();
        if (value) out[element.name] = value;
      }
    }
    return out;
  }

  function evidenceLinks() {
    return text('evidence_links').split(/\r?\n/).map((line) => line.trim()).filter(Boolean);
  }

  function attribution() {
    const mode = text('attribution_mode') || 'anonymous';
    return {
      mode,
      display_name: mode === 'anonymous' ? null : (text('display_name') || null),
      profile_url: null,
    };
  }

  function submissionId() {
    const id = crypto.randomUUID ? crypto.randomUUID().toUpperCase() : `${Date.now()}-${Math.random().toString(36).slice(2,10).toUpperCase()}`;
    return `GR-FW-${id}`;
  }

  button.addEventListener('click', async (event) => {
    event.preventDefault();
    event.stopImmediatePropagation();

    if (!text('model') || !text('access_basis') || !bool('attestation_hands_on')) {
      status.textContent = 'Complete the exact model, hands-on access basis, and hands-on attestation before exporting.';
      return;
    }

    const payload = {
      schema_version: 1,
      submission_id: submissionId(),
      submitted_at: new Date().toISOString(),
      model: {
        entered_name: text('model'),
        canonical_id: canonicalId(),
        retail_name: text('retail_name') || null,
        model_number: text('model_number') || null,
      },
      access_basis: text('access_basis'),
      device_fingerprint: await fingerprint(),
      attribution: attribution(),
      completion_percent: completion(),
      attestation_hands_on: true,
      attestation_observation: form.elements.attestation_observation ? bool('attestation_observation') : null,
      answers: answers(),
      evidence_links: evidenceLinks(),
    };

    const blob = new Blob([JSON.stringify(payload, null, 2)], {type: 'application/json'});
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `${payload.submission_id.toLowerCase()}.json`;
    document.body.appendChild(a);
    a.click();
    a.remove();
    URL.revokeObjectURL(url);
    status.textContent = 'Schema-valid Fieldwork package exported. The raw serial was not retained.';
  }, true);
})();
