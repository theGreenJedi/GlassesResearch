# SEO & Discoverability

GlassesResearch is designed to be easy to find without profiling visitors or using invasive tracking.

## Current status

As of 2026-08-07:

- `glassesresearch.org` is verified in Google Search Console as a **Domain property** using DNS TXT verification.
- Google URL Inspection reports `https://glassesresearch.org/` as **indexed** and served over HTTPS.
- `https://glassesresearch.org/robots.txt` is publicly reachable and allows crawling.
- `https://glassesresearch.org/sitemap.xml` is publicly reachable and contains canonical `glassesresearch.org` URLs.
- Search Console sitemap submission remains an external follow-up item because the newly created property returned an "Invalid sitemap address" UI error even though the sitemap itself is reachable and valid.

Do not remove the Google verification TXT record from DNS; Search Console uses it to retain ownership verification.

## Published search signals

Every rendered page publishes:

- a canonical `https://glassesresearch.org/...` URL;
- a page-specific HTML description derived from its visible source content unless an explicit description is supplied;
- Open Graph title, description, site name, type, and canonical URL;
- Twitter/X summary-card metadata;
- Schema.org `Organization`, `WebSite`, `WebPage`, and `BreadcrumbList` structured data;
- Schema.org `FAQPage` structured data when a page actually contains multiple visible question-and-answer sections.

Site-wide discovery endpoints:

- Canonical site: `https://glassesresearch.org/`
- Sitemap: `https://glassesresearch.org/sitemap.xml`
- Robots policy: `https://glassesresearch.org/robots.txt`
- Human-readable project marker: `https://glassesresearch.org/humans.txt`

## Automated SEO audit

Every pull request and production deployment builds the real MkDocs site and runs `scripts/verify_discoverability.py`.

The audit fails the build when it detects regressions in:

- required `robots.txt`, `sitemap.xml`, or `CNAME` artifacts;
- sitemap XML validity, duplicate entries, wrong-domain URLs, or rendered pages omitted from the sitemap;
- missing, duplicated, or incorrect canonical URLs;
- missing HTML titles or page descriptions;
- duplicate page descriptions;
- missing or mismatched Open Graph and Twitter/X metadata;
- invalid JSON-LD;
- missing `Organization`, `WebSite`, `WebPage`, or `BreadcrumbList` schema;
- FAQ collections whose visible question-and-answer content is missing `FAQPage` schema.

Repository link integrity and preservation records are separately checked by `scripts/audit_repository.py` in the same Pages workflow, so internal-link regressions remain deployment-blocking rather than becoming silent SEO failures.

After a production deployment, the workflow also checks the live `https://glassesresearch.org/robots.txt` and `https://glassesresearch.org/sitemap.xml` endpoints with retries so DNS or Pages propagation problems become visible instead of silently persisting.

## Google Search Console follow-up

Search Console contains live Google-side indexing data that repository CI cannot reproduce. The current operating checklist is:

1. Keep the DNS TXT ownership-verification record in place.
2. Retry submission of `https://glassesresearch.org/sitemap.xml` in **Sitemaps** after the new Domain property has had time to initialize.
3. Use **URL Inspection** for important entry pages after substantial changes, beginning with the homepage and `https://glassesresearch.org/models/THE_LIST/`.
4. Review **Pages** for crawl, canonical, redirect, duplicate-content, or robots exclusions.
5. Review **Core Web Vitals** as sufficient field data becomes available.
6. Recheck sitemap status after large catalog, FAQ, or news expansions.

## Structured-data policy

Structured data must describe content that is actually visible on the page. GlassesResearch does not add schema merely to chase rich-result features. In particular, FAQ schema is generated only from explicit visible question headings and their corresponding answers; pages without that structure remain ordinary `WebPage` records.

## Philosophy

Discoverability is a usability feature. The project does not need behavioral advertising, fingerprinting, or cross-site visitor tracking to be findable. Search metadata should describe the research accurately, preserve canonical identity, and help people reach useful evidence quickly.
