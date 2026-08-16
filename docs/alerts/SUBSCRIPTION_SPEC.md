# Verified Research Alerts — Subscription Contract

Verified Research Alerts delivers only verified, publicly published GlassesResearch material. Raw retrievals, candidate records, and internal review artifacts are never eligible for subscriber mail.

## Subscriber choices

A subscription has three independent preference layers:

1. **Follow** — models, brands/lineages, and topics the subscriber wants.
2. **Exclude** — models, brands/lineages, and topics the subscriber does not want.
3. **Cadence** — `as_verified`, `daily`, `weekly`, `monthly`, or `annually`.

Exclusions always win. A verified item that matches an included interest is still suppressed when it also matches any subscriber exclusion.

An empty Follow section means "all verified GlassesResearch research". An empty Exclude section means "exclude nothing".

## Topic vocabulary

Initial public topics:

- `hacks_development`
- `firmware_software`
- `hardware_teardown`
- `privacy_policy`
- `release_availability`
- `research_science`
- `standards_regulation`

The vocabulary may expand, but existing identifiers must remain stable for stored subscriber preferences.

## Example

A subscriber who wants recent W620 development work but no Meta material can store:

```json
{
  "cadence": "daily",
  "include": {
    "models": ["W620"],
    "brands_lineages": [],
    "topics": ["hacks_development"]
  },
  "exclude": {
    "models": [],
    "brands_lineages": ["Meta"],
    "topics": []
  }
}
```

A W620 hack is eligible. A Meta article is not. A W620 item that is also explicitly tagged Meta is suppressed because exclusion wins.

## Published-item metadata

Every mail-eligible published item should expose normalized metadata:

- stable publication ID;
- title;
- canonical `https://glassesresearch.org/...` URL;
- publication / verification timestamp;
- affected models;
- affected brands / lineages;
- topic tags;
- short verified summary.

The mailer matches preferences against this metadata rather than keyword-searching prose at send time.

## Delivery behavior

- **As verified:** send after a qualifying verified item is published.
- **Daily / Weekly / Monthly / Annually:** bundle qualifying items published since that subscriber's prior successful delivery window.
- If no qualifying items exist, send nothing.
- Every item links directly to its canonical public GlassesResearch destination.
- Every message contains a visible **Manage subscription** link and standards-based one-click unsubscribe where supported.

## Preference management

The management endpoint must allow subscribers to alter Follow, Exclude, and Cadence settings or unsubscribe completely without creating an account. Management URLs must use signed, non-guessable tokens and must not expose the email address in plaintext query parameters.

## Privacy

Email addresses and preferences exist only to provide the requested subscription. They are not advertising data, are not sold or traded, and are not used to build commercial or behavioral profiles. After unsubscribe, retain only the minimum suppression record needed to honor the opt-out.
