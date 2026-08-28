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

  const hero = document.createElement("section");
  hero.className = "gr-newsroom-hero";
  hero.innerHTML = `
    <div class="gr-newsroom-kicker">GlassesResearch Intelligence Desk</div>
    <p class="gr-newsroom-deck">The current smart-glasses beat: verified developments, emerging convergence, research gaps, hands-on evidence, policy, tools and the story threads we are still watching.</p>
    <div class="gr-newsroom-actions" aria-label="Research and News shortcuts">
      <a href="#gr-current-desk">Latest</a>
      <a href="#gr-convergence-radar">Convergence radar</a>
      <a href="#watching">Watching</a>
      <a href="#deep-research">Deep research</a>
      <a href="news/ARCHIVE/">Archive</a>
      <a href="https://glassesresearch.org/feed.xml">RSS</a>
    </div>
  `;
  title.insertAdjacentElement("afterend", hero);

  const latestHeading = [...root.querySelectorAll("h2")].find((heading) => heading.textContent?.trim() === "Latest verified");
  const latestTable = latestHeading?.nextElementSibling?.tagName === "TABLE" ? latestHeading.nextElementSibling : null;

  const desk = document.createElement("section");
  desk.id = "gr-current-desk";
  desk.className = "gr-newsroom-section";
  desk.innerHTML = `
    <div class="gr-newsroom-section-head">
      <div>
        <div class="gr-newsroom-kicker">Current desk</div>
        <h2>What changed</h2>
      </div>
      <p>Verified material changes first. Repetition and syndication do not become separate stories unless they add something substantive.</p>
    </div>
    <div class="gr-newsroom-card-grid" data-newsroom-latest></div>
  `;
  hero.insertAdjacentElement("afterend", desk);

  const latestGrid = desk.querySelector("[data-newsroom-latest]");
  const rows = latestTable ? [...latestTable.querySelectorAll("tbody tr")].slice(0, 6) : [];
  if (latestGrid && rows.length) {
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
      latestGrid.append(card);
    }
    latestHeading?.classList.add("gr-newsroom-enhanced-hide");
    latestTable?.classList.add("gr-newsroom-enhanced-hide");
  }

  const convergence = document.createElement("section");
  convergence.id = "gr-convergence-radar";
  convergence.className = "gr-newsroom-section gr-convergence-radar";
  convergence.innerHTML = `
    <div class="gr-newsroom-section-head">
      <div>
        <div class="gr-newsroom-kicker">Convergence radar</div>
        <h2>Where independent signals are beginning to agree</h2>
      </div>
      <p>This is not a trending chart. Convergence gets stronger when different evidence families point toward the same entity, technology or market shift. Ten rewrites of one press release still count as roughly one signal.</p>
    </div>
    <div class="gr-convergence-grid">
      <article class="gr-convergence-card">
        <div class="gr-signal-row"><span>Entity</span><strong>RayNeo ecosystem</strong></div>
        <h3>Product cadence + market presence + technical follow-through</h3>
        <p>RayNeo keeps appearing across product launches, market-share evidence and deeper technical investigation. The newsroom should treat those independent paths as a research assignment, not just repeated brand mentions.</p>
        <div class="gr-research-gap"><strong>Research gaps:</strong> owner control, SDK/API boundaries, cloud dependence, battery behavior and final retail state for newly announced models.</div>
        <p><a href="news/articles/2026-08-21-rayneo-io-gt-series/">Follow the current RayNeo story →</a></p>
      </article>
      <article class="gr-convergence-card">
        <div class="gr-signal-row"><span>Market</span><strong>Smart-glasses acceleration</strong></div>
        <h3>Display-less and display eyewear are both scaling</h3>
        <p>IDC reports 167% year-over-year growth for display-less smart glasses and 86% growth for display eyewear in Q1 2026. The useful signal is not one forecast: it is the market shift when shipment data, product activity and platform investment start reinforcing one another.</p>
        <div class="gr-research-gap"><strong>Research gaps:</strong> category definitions, regional mix, sell-through versus shipments, and whether platform openness improves as volume rises.</div>
        <p><a href="https://www.idc.com/resource-center/blog/smart-glasses-surge-the-xr-market-is-rewriting-its-own-rules/" rel="noopener">Read the IDC analysis →</a></p>
      </article>
    </div>
    <p class="gr-newsroom-method-note"><strong>Implementation note:</strong> the autonomous newsroom now computes convergence from story, entity, source and claim state. The public radar will move from these editorial seed cards to that structured feed after the Cloudflare integration boundary is crossed.</p>
  `;
  desk.insertAdjacentElement("afterend", convergence);

  const sourceRadar = document.createElement("section");
  sourceRadar.className = "gr-newsroom-section";
  sourceRadar.innerHTML = `
    <div class="gr-newsroom-section-head">
      <div>
        <div class="gr-newsroom-kicker">Source radar</div>
        <h2>Follow beats and people, not just websites</h2>
      </div>
      <p>Different sources play different roles. Authority, hands-on evidence and early discovery are recorded separately instead of being flattened into one generic source score.</p>
    </div>
    <div class="gr-source-grid">
      <article class="gr-source-card">
        <span class="gr-source-role">Market intelligence</span>
        <h3>Jitesh Ubrani · IDC</h3>
        <p>Recurring smart-glasses/XR market analysis makes the analyst himself a useful beat signal. New eyewear work from a repeatedly relevant analyst deserves elevated discovery attention while each claim still keeps its own provenance.</p>
        <a href="https://www.idc.com/resource-center/blog/smart-glasses-surge-the-xr-market-is-rewriting-its-own-rules/" rel="noopener">Current IDC smart-glasses analysis →</a>
      </article>
      <article class="gr-source-card">
        <span class="gr-source-role">Reader surface</span>
        <h3>PCMag · Smart Glasses</h3>
        <p>A dedicated living topic page makes the beat discoverable without forcing readers through a generic technology stream. That newsroom pattern is the presentation reference for this page.</p>
        <a href="https://www.pcmag.com/news/categories/smart-glasses" rel="noopener">PCMag Smart Glasses →</a>
      </article>
      <article class="gr-source-card">
        <span class="gr-source-role">Discovery sensor</span>
        <h3>Geeky Gadgets</h3>
        <p>Broad product roundups can surface obscure models and technologies early. They are useful lead generators, but commercial or affiliate-oriented claims remain candidates until stronger evidence corroborates them.</p>
        <a href="https://www.geeky-gadgets.com/smart-glasses-wearable-vr-and-ar/" rel="noopener">Example roundup →</a>
      </article>
    </div>
  `;
  convergence.insertAdjacentElement("afterend", sourceRadar);

  const browse = document.createElement("section");
  browse.className = "gr-newsroom-section gr-newsroom-browse";
  browse.innerHTML = `
    <div class="gr-newsroom-section-head">
      <div>
        <div class="gr-newsroom-kicker">Browse the beat</div>
        <h2>Research & News by job</h2>
      </div>
      <p>The same verified event may feed several of these surfaces at once.</p>
    </div>
    <div class="gr-newsroom-topic-grid">
      <a class="gr-topic-card" href="#watching"><strong>Releases & models</strong><span>Announcements, availability, model identity and developing launches.</span></a>
      <a class="gr-topic-card" href="#deep-research"><strong>Research & market</strong><span>Papers, market structure, technology shifts and evidence that changes our understanding.</span></a>
      <a class="gr-topic-card" href="#hacks-tools"><strong>Openness & tools</strong><span>SDKs, firmware, alternative apps, owner control and engineering paths.</span></a>
      <a class="gr-topic-card" href="#policy-society"><strong>Policy & society</strong><span>Privacy, workplace rules, accessibility and institutional response.</span></a>
    </div>
  `;
  sourceRadar.insertAdjacentElement("afterend", browse);
})();
