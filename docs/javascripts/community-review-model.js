(() => {
  const match = window.location.pathname.match(/\/models\/catalog\/(gls-\d{4})\/?$/i);
  if (!match) return;
  const modelId = match[1].toUpperCase();
  const article = document.querySelector('.md-content__inner');
  const heading = article?.querySelector('h1');
  if (!article || !heading) return;

  const labels = {
    discreetness: 'Discreetness',
    camera: 'Camera',
    visual_ai: 'Visual AI',
    hackability: 'Hackability',
    owner_control: 'Owner Control',
    android_compatibility: 'Android Compatibility',
  };

  const section = document.createElement('section');
  section.className = 'community-review-model-card';
  section.setAttribute('aria-label', 'Independent community hands-on evidence');
  section.innerHTML = `<div class="community-review-model-head"><div><strong>Independent hands-on evidence</strong><p id="community-review-model-summary">Accepted owner reviews are kept separate from the canonical GlassesResearch Report Card.</p></div><a class="md-button md-button--primary" href="/docs/COMMUNITY_REVIEWS/?model=${encodeURIComponent(modelId)}">Own these glasses? Review them</a></div><div id="community-review-model-ratings" hidden></div>`;
  heading.insertAdjacentElement('afterend', section);

  fetch('/data/community-review-summary.json', { cache: 'no-store' })
    .then((response) => response.ok ? response.json() : Promise.reject(new Error('summary unavailable')))
    .then((payload) => {
      const model = payload?.models?.[modelId];
      const summary = document.getElementById('community-review-model-summary');
      const ratings = document.getElementById('community-review-model-ratings');
      if (!model) {
        summary.textContent = 'No accepted independent hands-on reviews yet. A first owner report will remain explicitly labeled as independent community evidence.';
        return;
      }
      const n = Number(model.accepted_review_count || 0);
      const evidenceCount = Number(model.ownership_evidence_count || 0);
      summary.textContent = `${n} accepted independent hands-on review${n === 1 ? '' : 's'} · ${evidenceCount} with ownership evidence supplied. These observations do not overwrite GlassesResearch scores.`;
      const rows = Object.entries(model.ratings || {})
        .filter(([, value]) => Number(value?.n || 0) > 0)
        .map(([key, value]) => `<div class="community-review-mini-score"><span>${labels[key] || key}</span><strong>${value.median}/10</strong><small>median · n=${value.n} · range ${value.min}–${value.max}</small></div>`)
        .join('');
      if (rows) {
        ratings.innerHTML = `<div class="community-review-mini-grid">${rows}</div><p class="community-review-method-note">Community medians expose owner experience without collapsing it into the canonical evidence score. Open individual provenance through contributor histories and source issues as accepted reviews accumulate.</p>`;
        ratings.hidden = false;
      }
    })
    .catch(() => {
      const summary = document.getElementById('community-review-model-summary');
      if (summary) summary.textContent = 'Community review summary is temporarily unavailable. The standardized intake remains available.';
    });
})();
