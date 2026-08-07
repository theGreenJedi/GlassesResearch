# SEO & Discoverability

GlassesResearch is designed to be easy to find without profiling visitors or using invasive tracking.

## Published search signals

- Canonical site: `https://glassesresearch.org/`
- Sitemap: `https://glassesresearch.org/sitemap.xml`
- Robots policy: `https://glassesresearch.org/robots.txt`
- Human-readable project marker: `https://glassesresearch.org/humans.txt`
- Canonical URL metadata on rendered pages
- Open Graph and Twitter summary metadata
- Schema.org `WebSite` / `Organization` structured data

## Automated verification

Every pull request and production deployment now validates the built site's discoverability signals. CI fails if the build is missing `robots.txt`, `sitemap.xml`, the `CNAME` custom-domain marker, canonical URLs, Open Graph URLs, or JSON-LD structured data.

After a production deployment, the workflow also checks the live `https://glassesresearch.org/robots.txt` and `https://glassesresearch.org/sitemap.xml` endpoints with retries so DNS or Pages propagation problems become visible instead of silently persisting.

## Google Search Console checklist

Search Console ownership and indexing data live in the site owner's Google account and cannot be proven from repository code alone. Complete these one-time external steps:

1. Add `glassesresearch.org` as a Google Search Console **Domain property**.
2. Complete DNS ownership verification at the DNS provider using the TXT record Google supplies.
3. Submit `https://glassesresearch.org/sitemap.xml` in **Sitemaps**.
4. Use **URL Inspection** on `https://glassesresearch.org/` and request indexing.
5. Repeat URL Inspection for `https://glassesresearch.org/models/THE_LIST/` after deployment.
6. Review **Pages** / indexing reports for crawl, canonical, redirect, or robots errors.
7. Recheck the sitemap after large catalog, FAQ, or news expansions.

## Deployment checks

A successful production workflow verifies that:

- the custom domain resolves over HTTPS;
- `/robots.txt` returns an allow-all policy and the canonical sitemap URL;
- `/sitemap.xml` exists and uses `https://glassesresearch.org/` URLs;
- rendered pages contain canonical links;
- rendered pages contain Open Graph URL metadata;
- rendered pages contain the GlassesResearch structured-data block;
- the custom-domain `CNAME` is included in the built site;
- GitHub Pages completes successfully.

## Philosophy

Discoverability is a usability feature. The project does not need behavioral advertising, fingerprinting, or cross-site visitor tracking to be findable. Search metadata should describe the research accurately and help people reach useful evidence quickly.
