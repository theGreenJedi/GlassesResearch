# Research Inbox

The Research Inbox is the maintainer-facing working layer between automated collection and editorial review.

It does **not** replace `research/news-candidates/`; the candidate store remains the raw machine-collected record. The inbox exists to make those candidates easier to survey in coherent batches without turning collection into publication.

> **We strive to be complete in collection, but selective in publication.**

## Workflow

1. The daily collector writes raw candidates to `research/news-candidates/`.
2. A maintainer chooses a useful review window (for example, a week or a month).
3. Relevant candidates are grouped into one inbox survey batch.
4. Each underlying development receives one disposition: `publish`, `watch`, `archive`, `superseded`, or `reject`.
5. `publish` means “worthy of canonical research work,” not “automatically post this article.”
6. For now, only developments materially relevant to smart glasses / AI eyeglasses / eyewear may be promoted to the public site.
7. Adjacent HCI developments remain in the institutional archive until a concrete glasses connection exists or public scope is deliberately broadened.

## Inbox batches

Create dated batches beneath this directory, for example:

```text
research/inbox/
  2026-08/
    SURVEY-2026-08-09.md
```

Use `INBOX_TEMPLATE.md` as the starting point.

## Editorial stamps

Every reviewed development ends with one unambiguous disposition:

- **PUBLISH** — verify and promote into durable canonical research.
- **WATCH** — retain because future developments may make it important.
- **ARCHIVE** — preserve as useful historical evidence; no current action.
- **SUPERSEDED** — retained for provenance but replaced or clarified by newer evidence.
- **REJECT** — not sufficiently relevant, durable, or reliable.

A survey should never delete the underlying raw candidate merely because the editorial decision is `reject`.

## Institution test

For every development worth retaining, ask:

> **Will this still make GlassesResearch more useful one year from now?**

The answer may be “not yet.” That is what `watch` is for.

## Relationship to reviews

Completed editorial records belong in `research/news-reviews/`. The inbox is the workspace; `news-reviews` is the durable decision record.
