# GlassesResearch Control Room

This directory is the maintainer-facing operational control room for GlassesResearch. It is repository infrastructure, not public research content, and is not intended for the website navigation.

> **OPSEC policy:** Document architecture and procedures, not provider-specific identifiers. Assigned nameservers, zone/account IDs, API tokens, recovery codes, private dashboard screenshots, billing data, and account-specific recovery details are intentionally omitted from the public repository.

## Current architecture

- Public site: https://glassesresearch.org/
- Source repository: `theGreenJedi/GlassesResearch`
- Hosting: GitHub Pages
- DNS / CDN / edge security: Cloudflare
- Registrar: Namecheap
- Search indexing: Google Search Console
- Privacy analytics: Cloudflare Web Analytics / RUM
- Automated research intake: daily ecosystem news collector at **12:01 AM Eastern (`America/New_York`)**

## Research inbox

The daily collector writes raw intake to `research/news-candidates/`. The maintainer working layer is `research/inbox/`, and completed editorial decisions are preserved in `research/news-reviews/`.

Maintainer path:

**Control Room → Raw Collection (`research/news-candidates/`) → Research Inbox (`research/inbox/`) → Durable Review (`research/news-reviews/`) → Promote selected glasses-relevant findings into canonical research.**

The collector is deliberately broader than the public site. Adjacent wearable-HCI developments may be retained for future reference, but for now only concrete smart-glasses / AI-eyeglasses / eyewear developments are eligible for public promotion.

## Service health

Track these systems as independent layers so failures can be isolated quickly.

| Layer | Expected state | Where to check | Notes |
|---|---|---|---|
| Domain registration | Active | Namecheap | `glassesresearch.org` |
| Authoritative DNS | Cloudflare active | Cloudflare Overview / DNS | Provider assignment details intentionally omitted |
| DNSSEC | Off during migration; enable later through Cloudflare if desired | Cloudflare DNS / Namecheap | Do not leave stale registrar-side DS records |
| Origin hosting | GitHub Pages healthy | GitHub Actions / Pages | Custom domain configured in repository |
| TLS | Full | Cloudflare SSL/TLS | HTTPS should terminate at Cloudflare and remain encrypted to GitHub Pages |
| Site deployment | Green | GitHub Actions | Pages workflow validates built endpoints and live deployment |
| Search indexing | Verified | Google Search Console | Sitemap and robots.txt should remain reachable |
| Web analytics | Enabled globally | Cloudflare Web Analytics | Privacy-first RUM enabled globally |
| Daily news collector | **12:01 AM Eastern daily** | GitHub Actions | Uses `America/New_York` DST-aware gating; raw candidates are review-only, never canonical automatically |
| Research surveys | Periodic | `research/inbox/` → `research/news-reviews/` | Record dispositions and canonical follow-ups |

## Collector schedule implementation

GitHub Actions cron uses UTC and does not provide an `America/New_York` timezone setting. The collector therefore schedules both UTC equivalents of 12:01 AM Eastern—04:01 UTC for EDT and 05:01 UTC for EST—and checks the current Eastern UTC offset before doing any collection. The inactive DST counterpart exits without collecting. Manual workflow dispatch remains available and bypasses the schedule gate.

The institutional rule remains simple: **collection is automatic; review and publication are human editorial decisions.**

## Operational metrics

Record snapshots periodically rather than turning the public site into an internal dashboard.

### Traffic

- Unique visitors
- Page views
- Top pages
- Referrers
- Countries
- Browser/device mix
- Core Web Vitals / RUM

### Search

- Indexed pages
- Search impressions
- Search clicks
- Top queries
- Sitemap errors
- Crawl/indexing warnings

### Research corpus

- Canonical models tracked
- Technology lineages documented
- Model research chapters
- Community/development resources
- SDKs / developer projects cataloged
- Manuals / firmware / technical artifacts preserved
- Timeline events
- Open research candidates
- Last research-inbox survey date
- Watch/archive/publish dispositions awaiting follow-up

### Automation

- Pages deployment status
- Daily collector last successful run
- Candidate PRs awaiting review
- Broken-link or validation failures
- Comparison-engine record count
- Device-database record count

## Incident checklist

If the public site fails:

1. Confirm `glassesresearch.org` resolves.
2. Check Cloudflare zone status and DNS records.
3. Check Cloudflare SSL/TLS mode and certificate health.
4. Check the latest GitHub Pages workflow run.
5. Check GitHub Pages custom-domain configuration and `CNAME`.
6. Verify the expected GitHub Pages apex records remain present in Cloudflare without publishing provider-specific assignment details here.
7. Confirm no recent DNS, caching, redirect, or SSL change caused the failure.
8. Use Cloudflare Development Mode only temporarily when diagnosing stale cache behavior.

If analytics stops:

1. Confirm Cloudflare remains authoritative.
2. Confirm Web Analytics / RUM is enabled globally.
3. Confirm requests are actually traversing Cloudflare.
4. Check whether the analytics beacon or Cloudflare injection is present on the live site.
5. Compare HTTP Traffic against Web Analytics to distinguish traffic loss from analytics failure.

If search indexing falls:

1. Verify `robots.txt`.
2. Verify `sitemap.xml`.
3. Check Google Search Console coverage/indexing warnings.
4. Confirm canonical domain and HTTPS redirects are stable.
5. Verify recent site builds did not remove or rename major pages without redirects.

## Sensitive operational data

Keep the following outside the public repository:

- provider-assigned nameservers when there is no documentation need to publish them;
- Cloudflare zone IDs, account IDs, API tokens, and scoped credentials;
- registrar account identifiers and recovery details;
- private dashboard screenshots that expose account metadata;
- billing information;
- MFA recovery codes or backup credentials;
- private email addresses or phone numbers used for service recovery.

A local `operations-private/` directory may be used for non-secret maintainer notes and is excluded by `.gitignore`, but credentials and recovery secrets should live in a proper password manager or secrets store rather than plaintext files.

## Change log discipline

Operational changes should be recorded in git with a short explanation of what changed and why. Major infrastructure changes should also update this control room so recovery does not depend on chat history.

## Privacy posture

GlassesResearch should continue to favor privacy-preserving operational tooling. Cloudflare Web Analytics / RUM is preferred over cookie-heavy visitor tracking. Search crawlers and AI answer agents may access public research, while AI training crawlers are blocked by policy unless that decision is deliberately changed later.
