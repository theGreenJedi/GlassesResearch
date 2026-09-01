(() => {
  const root = document.querySelector('[data-second-life-root]');
  if (!root) return;

  const status = root.querySelector('[data-second-life-status]');
  const container = root.querySelector('[data-second-life-listings]');

  const escapeHtml = (value) => String(value ?? '')
    .replaceAll('&', '&amp;')
    .replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;')
    .replaceAll('"', '&quot;')
    .replaceAll("'", '&#039;');

  const fresh = (listing, now) => {
    const verified = Date.parse(listing.last_verified_at || listing.verified_at || '');
    const ttlHours = Number(listing.fresh_for_hours || 0);
    return Number.isFinite(verified)
      && verified <= now
      && ttlHours > 0
      && now - verified <= ttlHours * 3600000;
  };

  const safeUrl = (value) => {
    try {
      const url = new URL(String(value || ''), window.location.origin);
      return url.protocol === 'https:' ? url.href : null;
    } catch (_) {
      return null;
    }
  };

  fetch('/data/second-life.json', { cache: 'no-store' })
    .then((response) => {
      if (!response.ok) throw new Error(`HTTP ${response.status}`);
      return response.json();
    })
    .then((data) => {
      const now = Date.now();
      const listings = (data.listings || []).filter((item) => item.status === 'active' && fresh(item, now));

      if (!listings.length) {
        status.textContent = 'No recently verified listings right now.';
        return;
      }

      status.remove();
      container.innerHTML = listings.map((item) => {
        const verifiedAt = item.last_verified_at || item.verified_at;
        const url = safeUrl(item.url);
        const link = url
          ? `<p><a href="${escapeHtml(url)}" rel="nofollow noopener noreferrer">View listing</a></p>`
          : '';
        return `
        <article class="second-life-listing">
          <h2>${escapeHtml(item.model)}</h2>
          <p><strong>${escapeHtml(item.condition)}</strong>${item.price ? ` · ${escapeHtml(item.price)}` : ''}</p>
          <p>Verified ${escapeHtml(verifiedAt)} · ${escapeHtml(item.source)}</p>
          ${link}
        </article>`;
      }).join('');
    })
    .catch(() => {
      status.textContent = 'Current listings are temporarily unavailable.';
    });
})();
