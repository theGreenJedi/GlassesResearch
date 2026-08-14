# Purchase Link Replacement Queue

Generated: 2026-08-14T10:18:52Z

This queue is generated from the purchase-link health checker. Canonical purchase URLs are never silently replaced or deleted by the checker.

`blocked_or_rate_limited` routes stay out of this queue because many retailers intentionally reject bots even when their shopper pages work. Those routes require separate periodic human/browser verification.

| Model | Source | State | HTTP | Current URL | Action |
|---|---|---|---:|---|---|
| GLS-0018 | Amazon search | temporary_failure | 503 | https://www.amazon.com/s?k=Razer+Anzu+smart+glasses | Retry later |
| GLS-0021 | Huawei Eyewear 2 | dead | 404 | https://consumer.huawei.com/en/wearables/huawei-eyewear-2/ | Find replacement or durable marketplace search |
| GLS-0039 | Amazon search | temporary_failure | 503 | https://www.amazon.com/s?k=HeyCyan+W610+smart+glasses | Retry later |
| GLS-0051 | Frame | redirected | 200 | https://brilliant.xyz/products/frame | Verify final page still matches exact model |
| GLS-0056 | Vuzix Z100 | redirected | 200 | https://www.vuzix.com/products/z100-smart-glasses | Verify final page still matches exact model |
| GLS-0060 | INMO Air 3 | redirected | 200 | https://www.inmoglass.com/ | Verify final page still matches exact model |
| GLS-0074 | XREAL One | dead | 404 | https://www.xreal.com/one/ | Find replacement or durable marketplace search |
