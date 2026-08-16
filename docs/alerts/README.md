# Verified Research Alerts

Verified Research Alerts is the subscription layer for verified, publicly published GlassesResearch work.

The public preference interface supports:

- Follow filters for models, brands/lineages, and research topics;
- Exclude filters for models, brands/lineages, and research topics;
- delivery as verified, daily, weekly, monthly, or annually;
- exclusion precedence: excluded material is never delivered even when it also matches a Follow filter.

The preference contract is defined in [SUBSCRIPTION_SPEC.md](SUBSCRIPTION_SPEC.md).

Subscriptions use double opt-in. A new address is not activated until its confirmation link is used. Every delivered alert links directly to the corresponding published GlassesResearch work and includes a signed Manage subscription / unsubscribe path. Subscribers can change cadence and Follow/Exclude preferences or unsubscribe completely.

GlassesResearch retains subscriber email addresses only to operate the requested alert service. Subscriber addresses are not sold or used for advertising.

[Choose your alerts on Research & News](../RESEARCH_NEWS.md#verified-research-alerts).
