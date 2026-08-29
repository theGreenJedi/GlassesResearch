(() => {
  const path = window.location.pathname.replace(/\/+$/, "");
  if (!path.endsWith("/docs/RESEARCH_NEWS")) return;

  const root = document.querySelector(".md-content__inner");
  const title = root?.querySelector("h1");
  if (!root || !title || root.querySelector(".gr-newsroom-hero")) return;

  document.body.classList.add("gr-newsroom-enhanced");

  const intro = title.nextElementSibling;
  const jumpLinks = intro?.nextElementSibling;
  if (intro?.tagName === "P") intro.classList.add("gr-newsroom-enhanced-hide");
  if (jumpLinks?.tagName === "P") jumpLinks.classList.add("gr-newsroom-enhanced-hide");

  const escapeHtml = (value) => String(value ?? "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");

  const displayDate = (value) => {
    const date = new Date(value);
    if (Number.isNaN(date.getTime())) return value || "";
    return new Intl.DateTimeFormat(undefined, { month: "short", day: "numeric", year: "numeric" }).format(date);
  };

  const hero = document.createElement("section");
  hero.className = "gr-newsroom-hero";
  hero.innerHTML = `
    <div class="gr-newsroom-kicker">GlassesResearch Intelligence Desk</div>
    <p class="gr-newsroom-deck">The current smart-glasses beat: verified developments, emerging convergence, research gaps, hands-on evidence, policy, tools and the story threads we are still watching.</p>
    <div class="gr-newsroom-actions" aria-label="Research and News shortcuts">
      <a href="#gr-lead-story">Lead story</a>
      <a href="#gr-current-desk">Latest</a>
      <a href="#gr-convergence-radar">Convergence</a>
      <a href="#watching">Watching</a>
      <a href="#deep-research">Deep research</a>
      <a href="/docs/news/ARCHIVE/">Archive</a>
      <a href="/feed.xml">RSS</a>
    </div>
    <p class="gr-newsroom-freshness" data-newsroom-freshness>Loading verified newsroom state…</p>
  `;
  title.insertAdjacentElement("afterend", hero);

  const lead = document.createElement("section");
  lead.id = "gr-lead-story";
  lead.className = "gr-newsroom-section gr-newsroom-lead";
  lead.hidden = true;
  hero.insertAdjacentElement("afterend", lead);

  const desk = document.createElement("section");
  desk.id = "gr-current-desk";
  desk.className = "gr-newsroom-section";
  desk.innerHTML = `
    <div class="gr-newsroom-section-head">
      <div>
        <div class="gr-newsroom-kicker">Current desk</div>
        <h2>Latest verified</h2>
      </div>
      <p>Verified material changes, newest first. Repetition and syndication do not become separate stories unless they add something substantive.</p>
    </div>
    <div class="gr-newsroom-card-grid" data-newsroom-latest></div>
  `;
  lead.insertAdjacentElement("afterend", desk);

  const convergence = document.createElement("section");
  convergence.id = "gr-convergence-radar";
  convergence.className = "gr-newsroom-section gr-convergence-radar";
  convergence.hidden = true;
  desk.insertAdjacentElement("afterend", convergence);

  const browse = document.createElement("section");
  browse.className = "gr-newsroom-section gr-newsroom-browse";
  browse.innerHTML = `
    <div class="gr-newsroom-section-head">
      <div>
        <div class="gr-newsroom-kicker">Browse the beat</div>
        <h2>Research & News by job</h2>
      </div>
      <p>The same verified event may feed several research surfaces at once.</p>
    </div>
    <div class="gr-newsroom-topic-grid">
      <a class="gr-topic-card" href="#watching"><strong>Releases & models</strong><span>Announcements, availability, model identity and developing launches.</span></a>
      <a class="gr-topic-card" href="#deep-research"><strong>Research & market</strong><span>Papers, market structure, technology shifts and evidence that changes our understanding.</span></a>
      <a class="gr-topic-card" href="#hacks-tools"><strong>Openness & tools</strong><span>SDKs, firmware, alternative apps, owner control and engineering paths.</span></a>
      <a class="gr-topic-card" href="#policy-society"><strong>Policy & society</strong><span>Privacy, workplace rules, accessibility and institutional response.</span></a>
    </div>
  `;
  convergence.insertAdjacentElement("afterend", browse);

  const latestHeading = [...root.querySelectorAll("h2")].find((heading) => heading.textContent?.trim() === "Latest verified");
  const latestTable = latestHeading?.nextElementSibling?.tagName === "TABLE" ? latestHeading.nextElementSibling : null;
  const latestGrid = desk.querySelector("[data-newsroom-latest]");

  const renderTableFallback = () => {
    const rows = latestTable ? [...latestTable.querySelectorAll("tbody tr")].slice(0, 6) : [];
    for (const row of rows) {
      const cells = row.querySelectorAll("td");
      if (cells.length < 3) continue;
      const card = document.createElement("article");
      card.className = "gr-newsroom-card";
      card.innerHTML = `
        <div class="gr-newsroom-date">${cells[0].innerHTML}</div>
        <div class="gr-newsroom-card-copy">${cells[1].innerHTML}</div>
        <div class="gr-newsroom-card-links">${cells[2].innerHTML}</div>
      `;
      latestGrid?.append(card);
    }
  };

  const renderStoryCard = (story) => `
    <article class="gr-newsroom-card">
      <div class="gr-newsroom-date">${escapeHtml(displayDate(story.published_at))}</div>
      <div class="gr-newsroom-card-copy"><strong>${escapeHtml(story.title)}</strong><p>${escapeHtml(story.summary)}</p></div>
      <div class="gr-newsroom-card-links"><a href="${escapeHtml(story.url)}">Read the research →</a></div>
    </article>
  `;

  fetch("/data/newsroom-state.json", { credentials: "same-origin" })
    .then((response) => {
      if (!response.ok) throw new Error(`newsroom state ${response.status}`);
      return response.json();
    })
    .then((state) => {
      if (!state?.lead || !Array.isArray(state.latest)) throw new Error("newsroom state malformed");

      const freshness = hero.querySelector("[data-newsroom-freshness]");
      if (freshness) {
        const latestAt = new Date(state.latest_verified_at);
        const ageHours = Number.isNaN(latestAt.getTime()) ? null : Math.max(0, (Date.now() - latestAt.getTime()) / 36e5);
        const age = ageHours === null ? "" : ageHours < 48 ? ` · ${Math.floor(ageHours)}h ago` : ` · ${Math.floor(ageHours / 24)}d ago`;
        freshness.textContent = `Latest verified ${displayDate(state.latest_verified_at)}${age}`;
        if (ageHours !== null && ageHours > 48) freshness.classList.add("is-stale");
      }

      lead.hidden = false;
      lead.innerHTML = `
        <div class="gr-newsroom-kicker">Lead development</div>
        <a class="gr-newsroom-lead-card" href="${escapeHtml(state.lead.url)}">
          <span class="gr-newsroom-date">${escapeHtml(displayDate(state.lead.published_at))} · ${escapeHtml(state.lead.change_type.replaceAll("_", " "))}</span>
          <strong>${escapeHtml(state.lead.title)}</strong>
          <span>${escapeHtml(state.lead.summary)}</span>
          <em>Go deeper →</em>
        </a>
      `;

      if (latestGrid) latestGrid.innerHTML = state.latest.slice(0, 6).map(renderStoryCard).join("");
      latestHeading?.classList.add("gr-newsroom-enhanced-hide");
      latestTable?.classList.add("gr-newsroom-enhanced-hide");

      if (Array.isArray(state.convergence) && state.convergence.length) {
        convergence.hidden = false;
        const cards = state.convergence.slice(0, 4).map((theme) => {
          const supporting = (theme.stories || []).slice(0, 2).map((story) =>
            `<a href="${escapeHtml(story.url)}">${escapeHtml(story.title)}</a>`
          ).join("<span aria-hidden=\"true\"> · </span>");
          return `
            <article class="gr-convergence-card">
              <div class="gr-signal-row"><span>${escapeHtml(theme.kind)}</span><strong>${escapeHtml(theme.label)}</strong></div>
              <h3>${escapeHtml(theme.story_count)} verified story signals across ${escapeHtml(theme.independent_source_hosts)} source families</h3>
              <p class="gr-convergence-links">${supporting}</p>
            </article>
          `;
        }).join("");
        convergence.innerHTML = `
          <div class="gr-newsroom-section-head">
            <div><div class="gr-newsroom-kicker">Convergence radar</div><h2>Where independent signals are beginning to agree</h2></div>
            <p>Convergence requires multiple verified story signals and multiple source families. Rewrites of one source do not manufacture momentum.</p>
          </div>
          <div class="gr-convergence-grid">${cards}</div>
        `;
      }
    })
    .catch(() => {
      const freshness = hero.querySelector("[data-newsroom-freshness]");
      if (freshness) freshness.textContent = "Verified newsroom state unavailable · showing published-page fallback";
      renderTableFallback();
    });
})();
