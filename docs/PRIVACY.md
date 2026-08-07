# Privacy

GlassesResearch exists to preserve knowledge, not to profile visitors.

## Our public-site promise

The project website is intentionally simple:

- no advertising;
- no tracking cookies;
- no behavioral profiling;
- no sale of visitor data;
- no cross-site visitor identification;
- no attempt to build individual visitor profiles.

We preserve knowledge, not attention.

## Aggregate analytics

GlassesResearch permits one narrowly scoped analytics service: **Cloudflare Web Analytics**.

It is used only to understand aggregate site usage and page performance so the project can learn which research is useful and where the public site needs improvement. The project does not use analytics for advertising, retargeting, user scoring, personalization, or cross-site tracking.

Cloudflare Web Analytics is designed without cookies or persistent browser storage and does not track individual users across Cloudflare customers' sites. If the GlassesResearch Cloudflare site token is not configured, the analytics bootstrap remains inactive and sends nothing.

The analytics configuration is public in the repository so visitors and contributors can inspect exactly what the project loads.

## Community-specific greetings

Links shared in a community may include an explicit parameter such as:

- `https://glassesresearch.org/docs/CONTRIBUTE/?from=reddit`
- `https://glassesresearch.org/docs/CONTRIBUTE/?from=discord`
- `https://glassesresearch.org/docs/CONTRIBUTE/?from=github`

That parameter may produce a one-time greeting such as **Welcome, Redditor!** on the contribution page.

The greeting mechanism:

- reads only the explicit `from` value contained in the link;
- does not inspect the browser referrer;
- does not use cookies or local storage;
- does not fingerprint the device;
- does not retain the community source after the page is left;
- does not alter the rest of the visitor's experience.

Unknown values are ignored. Visitors using ordinary links receive the ordinary contribution page.

## Contributions and attribution

Contributors may choose how they are credited. Available options include:

- real name;
- GitHub username or another public handle;
- project or organization name;
- pseudonym;
- anonymous contribution.

Attribution may appear on the relevant research page, evidence record, commit, pull request, acknowledgment, or a future contributor hall. A contributor hall or hall of fame may be created when the project has a substantial community to recognize; it is not required for contributions to receive credit now.

Contributors should not submit private personal information about themselves or others unless it is necessary, lawful, and intentionally public.

## Services outside the project

The site is hosted through GitHub Pages. Cloudflare Web Analytics may receive the privacy-preserving performance beacon described above. Following links to GitHub, manufacturers, archives, videos, forums, or other outside services means those services apply their own privacy practices. GlassesResearch cannot control external sites.

## Changes to this promise

Any future proposal to add advertising, tracking cookies, persistent visitor identification, profiling, or a materially broader analytics system must be explicit, publicly documented, and reviewed as a project-policy change. The default remains: **no cookies, no profiling, no surveillance.**
