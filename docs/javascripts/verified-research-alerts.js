(() => {
  const CADENCES = ["as_verified", "daily", "weekly", "monthly", "annually"];
  const PANEL_SELECTOR = ".verified-alerts";
  const ENDPOINT = "https://alerts.glassesresearch.org/subscribe";
  const FEED_URL = "https://glassesresearch.org/feed.xml";
  const FEEDLY_URL = "https://feedly.com/i/discover/sources/search/feed/https%3A%2F%2Fglassesresearch.org%2Ffeed.xml";
  const INOREADER_URL = "https://www.inoreader.com/feed/https%3A%2F%2Fglassesresearch.org%2Ffeed.xml";
  const TOPICS = [
    ["hacks_development", "Hacks / Development"],
    ["firmware_software", "Firmware / Software"],
    ["hardware_teardown", "Hardware / Teardown"],
    ["privacy_policy", "Privacy / Policy"],
    ["release_availability", "Releases / Availability"],
    ["research_science", "Research / Science"],
    ["standards_regulation", "Standards / Regulation"],
  ];

  function normalizeList(value) {
    return String(value || "").split(",").map((item) => item.trim()).filter(Boolean).slice(0, 50);
  }

  function topicChecks(name) {
    return TOPICS.map(([value, label]) => `<label><input type="checkbox" name="${name}" value="${value}"> ${label}</label>`).join("");
  }

  function contextFromUrl() {
    const params = new URLSearchParams(window.location.search);
    return {
      model: params.get("model") || "",
      brand: params.get("brand") || "",
      topic: params.get("topic") || "",
      cadence: params.get("cadence") || "",
    };
  }

  function applyContext(root) {
    const context = contextFromUrl();
    const model = root.querySelector('[name="include_models"]');
    const brand = root.querySelector('[name="include_brands"]');
    const cadence = root.querySelector('[name="cadence"]');
    if (model && context.model) model.value = context.model;
    if (brand && context.brand) brand.value = context.brand;
    if (cadence && CADENCES.includes(context.cadence)) cadence.value = context.cadence;
    if (context.topic && TOPICS.some(([value]) => value === context.topic)) {
      const topic = root.querySelector(`input[name="include_topics"][value="${context.topic}"]`);
      if (topic) topic.checked = true;
    }
    const contextual = Boolean(context.model || context.brand || context.topic);
    if (contextual) {
      const note = root.querySelector("[data-alert-context]");
      if (note) note.hidden = false;
    }
  }

  function renderFollowPanel() {
    const path = window.location.pathname.replace(/\/+$/, "");
    if (path !== "/docs/RESEARCH_NEWS") return;
    const article = document.querySelector(".md-content__inner");
    if (!article || article.querySelector("[data-follow-research]")) return;

    const panel = document.createElement("section");
    panel.className = "follow-research";
    panel.dataset.followResearch = "true";
    panel.setAttribute("aria-labelledby", "follow-research-title");
    panel.innerHTML = `
      <div class="follow-research__heading">
        <p class="follow-research__eyebrow">Follow GlassesResearch</p>
        <h2 id="follow-research-title">Follow verified research</h2>
        <p>Choose tailored email alerts or follow the same verified-change stream in your own RSS reader.</p>
      </div>
      <div class="follow-research__grid">
        <section class="follow-research__option" aria-labelledby="follow-email-title">
          <h3 id="follow-email-title">Email alerts</h3>
          <p>Follow models, brands/lineages, or topics; exclude what you do not want; choose as-verified, daily, weekly, monthly, or annual delivery.</p>
          <a class="md-button md-button--primary" href="#verified-research-alerts">Set up alerts</a>
        </section>
        <section class="follow-research__option" aria-labelledby="follow-rss-title">
          <h3 id="follow-rss-title">RSS — no email required</h3>
          <p>Receive every verified GRE change in the reader you already use. Watching and unverified discovery items are excluded.</p>
          <div class="follow-research__actions">
            <a class="md-button" href="${FEED_URL}">RSS feed</a>
            <a class="md-button" href="${FEEDLY_URL}" target="_blank" rel="noopener noreferrer">Feedly</a>
            <a class="md-button" href="${INOREADER_URL}" target="_blank" rel="noopener noreferrer">Inoreader</a>
            <button class="md-button" type="button" data-copy-feed>Copy feed</button>
          </div>
          <p class="follow-research__status" data-copy-feed-status role="status" aria-live="polite"></p>
        </section>
      </div>`;

    const intro = article.querySelector("h1 + p");
    if (intro) {
      intro.insertAdjacentElement("afterend", panel);
    } else {
      const heading = article.querySelector("h1");
      if (heading) heading.insertAdjacentElement("afterend", panel);
      else article.prepend(panel);
    }
  }

  function renderPanel(root) {
    if (root.dataset.alertsHydrated === "true") return;
    root.dataset.alertsHydrated = "true";
    root.innerHTML = `
      <p data-alert-context hidden>This form has been prefilled from the model or topic you were researching. Adjust anything before subscribing.</p>
      <form data-verified-research-alerts>
        <label for="alerts-email"><strong>Email address</strong></label>
        <input id="alerts-email" name="email" type="email" autocomplete="email" required placeholder="you@example.com">
        <fieldset>
          <legend>Delivery cadence</legend>
          <select name="cadence" required>
            <option value="as_verified">As verified</option>
            <option value="daily">Daily</option>
            <option value="weekly">Weekly</option>
            <option value="monthly">Monthly</option>
            <option value="annually">Annually</option>
          </select>
        </fieldset>
        <div class="alert-grid">
          <fieldset>
            <legend>Follow</legend>
            <label>Models <input name="include_models" type="text" placeholder="W620, Vuzix Z100"></label>
            <label>Brands / lineages <input name="include_brands" type="text" placeholder="HeyCyan, Even Realities"></label>
            <div class="alert-checks">${topicChecks("include_topics")}</div>
          </fieldset>
          <fieldset>
            <legend>Exclude</legend>
            <label>Models <input name="exclude_models" type="text" placeholder="Ray-Ban Meta"></label>
            <label>Brands / lineages <input name="exclude_brands" type="text" placeholder="Meta"></label>
            <div class="alert-checks">${topicChecks("exclude_topics")}</div>
          </fieldset>
        </div>
        <p class="alert-note">Exclusions always win. Leave Follow empty to receive all verified research except anything you exclude. Every email links directly to the corresponding published GlassesResearch work and includes Manage subscription / unsubscribe.</p>
        <button type="button" class="md-button md-button--primary" data-alert-submit>Subscribe to verified research</button>
        <p class="alert-status" data-alert-status aria-live="polite"></p>
      </form>`;
    applyContext(root);
  }

  function value(root, name) {
    return root.querySelector(`[name="${name}"]`)?.value || "";
  }

  function payloadFrom(root) {
    const cadence = value(root, "cadence");
    if (!CADENCES.includes(cadence)) throw new Error("Choose a valid delivery cadence.");
    return {
      schema: 1,
      email: value(root, "email").trim(),
      cadence,
      include: {
        models: normalizeList(value(root, "include_models")),
        brands_lineages: normalizeList(value(root, "include_brands")),
        topics: Array.from(root.querySelectorAll('input[name="include_topics"]:checked')).map((el) => el.value),
      },
      exclude: {
        models: normalizeList(value(root, "exclude_models")),
        brands_lineages: normalizeList(value(root, "exclude_brands")),
        topics: Array.from(root.querySelectorAll('input[name="exclude_topics"]:checked')).map((el) => el.value),
      },
      source: "research_news",
    };
  }

  function resetPanel(root) {
    root.querySelector("form")?.reset();
  }

  async function submitPanel(root, button) {
    const status = root.querySelector("[data-alert-status]");
    if (!status || button.dataset.submitting === "true") return;

    let payload;
    try {
      payload = payloadFrom(root);
      if (!/^\S+@\S+\.\S+$/.test(payload.email)) throw new Error("Enter a valid email address.");
    } catch (error) {
      status.textContent = error instanceof Error ? error.message : "Check the subscription form and try again.";
      return;
    }

    button.dataset.submitting = "true";
    button.disabled = true;
    status.textContent = "Submitting…";

    try {
      const response = await fetch(ENDPOINT, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
      });
      const result = await response.json().catch(() => ({}));
      if (!response.ok || result.ok === false) throw new Error(result.message || "Subscription service is temporarily unavailable.");
      status.textContent = result.message || "Check your email to confirm your subscription.";
      resetPanel(root);
    } catch (error) {
      status.textContent = error instanceof Error ? error.message : "Subscription service is temporarily unavailable.";
    } finally {
      delete button.dataset.submitting;
      button.disabled = false;
    }
  }

  function fallbackCopy(text) {
    const area = document.createElement("textarea");
    area.value = text;
    area.setAttribute("readonly", "");
    area.style.position = "fixed";
    area.style.opacity = "0";
    document.body.appendChild(area);
    area.select();
    const copied = document.execCommand("copy");
    area.remove();
    return copied;
  }

  async function copyFeed(button) {
    const panel = button.closest("[data-follow-research]");
    const status = panel?.querySelector("[data-copy-feed-status]");
    try {
      if (navigator.clipboard?.writeText) await navigator.clipboard.writeText(FEED_URL);
      else if (!fallbackCopy(FEED_URL)) throw new Error("copy failed");
      if (status) status.textContent = "Feed URL copied.";
    } catch (_error) {
      if (status) status.textContent = `Feed URL: ${FEED_URL}`;
    }
  }

  document.addEventListener("click", (event) => {
    const target = event.target instanceof Element ? event.target : null;
    if (!target) return;

    const copyButton = target.closest("[data-copy-feed]");
    if (copyButton) {
      event.preventDefault();
      copyFeed(copyButton);
      return;
    }

    const button = target.closest("[data-alert-submit]");
    if (!button) return;
    const root = button.closest(PANEL_SELECTOR);
    if (!root) return;
    event.preventDefault();
    submitPanel(root, button);
  });

  function renderAll() {
    renderFollowPanel();
    document.querySelectorAll(PANEL_SELECTOR).forEach(renderPanel);
  }

  renderAll();
  new MutationObserver(renderAll).observe(document.documentElement, { childList: true, subtree: true });
})();