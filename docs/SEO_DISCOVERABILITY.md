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

## Search Console checklist

1. Add `glassesresearch.org` as a Google Search Console domain property.
2. Complete DNS ownership verification at the DNS provider.
3. Submit `https://glassesresearch.org/sitemap.xml`.
4. Inspect the homepage URL and request indexing after major structural changes.
5. Review Coverage / Pages reports for crawl or canonical errors.
6. Recheck the sitemap after large catalog, FAQ, or news expansions.

## Deployment checks

After a production deployment, verify that:

- the custom domain resolves over HTTPS;
- `/robots.txt` returns an allow-all policy and the canonical sitemap URL;
- `/sitemap.xml` exists and uses `https://glassesresearch.org/` URLs;
- rendered pages contain a canonical link;
- rendered pages contain Open Graph metadata;
- rendered pages contain the GlassesResearch structured-data block;
- GitHub Pages completes successfully.

## Philosophy

Discoverability is a usability feature. The project does not need behavioral advertising, fingerprinting, or cross-site visitor tracking to be findable. Search metadata should describe the research accurately and help people reach useful evidence quickly.
