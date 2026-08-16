# Verified Research Alerts

Verified Research Alerts is the subscription layer for verified, publicly published GlassesResearch work.

The public preference interface supports:

- Follow filters for models, brands/lineages, and research topics;
- Exclude filters for models, brands/lineages, and research topics;
- delivery as verified, daily, weekly, monthly, or annually;
- exclusion precedence: excluded material is never delivered even when it also matches a Follow filter.

The preference contract is defined in [SUBSCRIPTION_SPEC.md](SUBSCRIPTION_SPEC.md).

The repository-side interface is intentionally fail-closed until a production subscription API endpoint is provisioned. In that state, the form collects and transmits no email address. Activating delivery requires the backend to provide double opt-in, signed management links, direct canonical research links, preference editing, suppression handling, and unsubscribe support required by the project privacy policy.
