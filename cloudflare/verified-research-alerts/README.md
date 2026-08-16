# Verified Research Alerts backend

This Worker is the production service behind the fail-closed Verified Research Alerts form.

## Architecture

- Cloudflare Worker: public subscription API and management pages.
- Cloudflare D1: subscriber preferences, opaque-token hashes, suppression state, published-item metadata, and delivery receipts.
- Resend: outbound mail transport for the zero-cost starting configuration. The Worker can later switch to Cloudflare Email Sending without changing the public subscription contract.
- `POST /published`: authenticated ingest for verified, publicly published GlassesResearch items only.
- Hourly Cron Trigger: checks due daily, weekly, monthly, and annual digests. If nothing qualifies, nothing is sent.
- `as_verified`: qualifying subscribers are dispatched when a verified publication is ingested.

## Privacy and security behavior

- Double opt-in is required before activation.
- Confirmation and management URLs use random opaque tokens; only SHA-256 token hashes are stored.
- Email addresses never appear in management URLs.
- Exclusion filters always win over Follow filters.
- Unsubscribe changes the record to `suppressed`, clears preference data and management credentials, and retains the address only as the minimum suppression record needed to prevent accidental remailing.
- Published mail content must point to canonical `https://glassesresearch.org/...` URLs.
- The public website remains fail-closed until this Worker is deployed and verified.

## Required Cloudflare resources

1. Create D1 database `glassesresearch-alerts`.
2. Replace `REPLACE_AFTER_D1_CREATION` in `wrangler.jsonc` with its database ID.
3. Apply `schema.sql` to the production D1 database.
4. Deploy the Worker and assign the custom domain `alerts.glassesresearch.org`.
5. Add Worker secrets:
   - `RESEND_API_KEY`
   - `PUBLISH_TOKEN` (random, high-entropy secret used only by the publication pipeline)
6. In Resend, verify `glassesresearch.org` (or a dedicated sending subdomain) using the DNS records Resend supplies through Cloudflare DNS.
7. Confirm `alerts@glassesresearch.org` is an allowed From address.
8. Test `/health`, a subscription confirmation round trip, preference editing, and unsubscribe before enabling the public form endpoint.

## Wrangler commands

From this directory:

```powershell
npx wrangler d1 create glassesresearch-alerts
npx wrangler d1 execute glassesresearch-alerts --remote --file=schema.sql
npx wrangler secret put RESEND_API_KEY
npx wrangler secret put PUBLISH_TOKEN
npx wrangler deploy
```

Do not place either secret in the repository, terminal receipts, documentation, or GitHub Actions logs.

## Publication payload

`POST https://alerts.glassesresearch.org/published` with `Authorization: Bearer <PUBLISH_TOKEN>`:

```json
{
  "id": "stable-publication-id",
  "title": "Verified research title",
  "canonical_url": "https://glassesresearch.org/docs/RESEARCH_NEWS/#example",
  "published_at": "2026-08-16T01:00:00Z",
  "summary": "Short verified summary.",
  "models": ["W620"],
  "brands_lineages": ["HeyCyan"],
  "topics": ["hacks_development"]
}
```

No raw collector candidates or unverified research may be submitted to this endpoint.
