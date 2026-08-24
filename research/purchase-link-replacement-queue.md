# Purchase Link Replacement Queue

Generated: 2026-08-24T10:07:11Z

This queue is generated from the purchase-link health checker. Canonical purchase URLs are never silently replaced or deleted by the checker.

`blocked_or_rate_limited` routes stay out of this queue because many retailers intentionally reject bots even when their shopper pages work. Those routes require separate periodic human/browser verification.

| Model | Source | State | HTTP | Current URL | Action |
|---|---|---|---:|---|---|
| GLS-0060 | INMO Air 3 | redirected | 200 | https://www.inmoxr.com/products/inmo-air3-ar-glasses-all-in-one-full-color-waveguide | Verify final page still matches exact model |
| GLS-0164 | Nautica Smart Eyewear Powered by Lucyd — Corsair | unreachable |  | https://www.bestbuy.com/product/nautica-smart-eyewear-powered-by-lucyd-corsair/J3R8ZC6LGC/sku/6589919 | Retry, then search replacement if persistent |
| GLS-0165 | Meta Adventurer AI Glasses | unreachable |  | https://www.bestbuy.com/product/meta-adventurer-ai-glasses-smart-features-like-12mp-camera-live-translate-8-hour-battery-range-of-sizes-brown-lenses-classic-tortoise/J3LHRV8436/sku/6677832 | Retry, then search replacement if persistent |
