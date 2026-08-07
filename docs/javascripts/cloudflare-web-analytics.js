/*
 * GlassesResearch Cloudflare Web Analytics bootstrap.
 *
 * Cloudflare Web Analytics is privacy-first and does not use cookies or
 * persistent browser storage. Set the site token below after creating the
 * GlassesResearch Web Analytics site in the Cloudflare dashboard.
 *
 * Until a token is configured, this file intentionally does nothing.
 */
(() => {
  const SITE_TOKEN = "";

  if (!SITE_TOKEN) {
    return;
  }

  const beacon = document.createElement("script");
  beacon.type = "module";
  beacon.src = `https://static.cloudflareinsights.com/beacon.min.js?token=${encodeURIComponent(SITE_TOKEN)}`;
  beacon.dataset.glassesresearchAnalytics = "cloudflare-web-analytics";
  document.head.appendChild(beacon);
})();
