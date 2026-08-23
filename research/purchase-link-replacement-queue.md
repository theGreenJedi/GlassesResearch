# Purchase Link Replacement Queue

Generated: 2026-08-23T09:45:18Z

This queue is generated from the purchase-link health checker. Canonical purchase URLs are never silently replaced or deleted by the checker.

`blocked_or_rate_limited` routes stay out of this queue because many retailers intentionally reject bots even when their shopper pages work. Those routes require separate periodic human/browser verification.

| Model | Source | State | HTTP | Current URL | Action |
|---|---|---|---:|---|---|
| GLS-0060 | INMO Air 3 | redirected | 200 | https://www.inmoxr.com/products/inmo-air3-ar-glasses-all-in-one-full-color-waveguide | Verify final page still matches exact model |
