# Agentic discovery pilot

Separate measurement streams: (1) Bing Webmaster AI Performance citation appearances and cited pages/grounding queries; (2) Google Search Console generative AI link impressions; (3) Cloudflare AI crawler request estimates and explicit referrer requests; (4) browser-side referral lower bounds; (5) blind citation tests. No composite score, no implied organic citations from crawls or experimental answers. No SEO, robots, CDN or site changes.

Sources:
- https://www.bing.com/webmasters/help/?topicid=9f8e7d6c
- https://support.google.com/webmasters/answer/16984139
- https://developers.cloudflare.com/ai-crawl-control/reference/graphql-api/
- https://help.openai.com/en/articles/12627856-publishers-and-developers-faq

No documented dedicated publisher-report API confirmed for Bing or Google. Export the same seven-day date range from the account dashboards; record the report's property-level totals and window in a local JSON file: {"bing_ai":{"start":"YYYY-MM-DD","end":"YYYY-MM-DD","total":0},"google_ai":{"start":"YYYY-MM-DD","end":"YYYY-MM-DD","total":0}}. Use only observed totals; omit unavailable streams. Run python scripts/agentic_discovery.py --exports /path/to/file.json. Retain URL/query breakdowns separately; do not publish private exports without approval.

Blind tests: preselect a fixed panel of representative prompts; never mention this site or constrain source selection. Record model/product/version/date, exact prompt, answer/cited URLs, whether sources support the answer, and whether site was found or actually cited. Distinguish search tool retrieval from a final-answer citation. Run independent products only where access exists; no extrapolation to real-world frequency. Do not use a test click as organic traffic. No independent platform tests executed by this pilot.

Pilot outputs are workflow artifacts, not production data. Review completed query evidence and permissions before adding recurring collection to analytics.
