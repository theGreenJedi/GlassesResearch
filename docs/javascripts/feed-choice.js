(() => {
  const VERIFIED = "https://glassesresearch.org/feed.xml";
  const WIRE = "https://glassesresearch.org/data/wire-feed.xml";

  const copyFeed = async (button) => {
    const url = button.dataset.feedUrl;
    if (!url) return;
    const scope = button.closest("section, .md-content__inner, .follow-research__option") || document;
    const status = scope.querySelector("[data-feed-copy-status], [data-copy-feed-status]");
    try {
      await navigator.clipboard.writeText(url);
      if (status) status.textContent = "Feed URL copied. Paste it into Feedly, Inoreader, or another RSS reader.";
      button.textContent = "Copied";
      window.setTimeout(() => {
        button.textContent = button.dataset.feedLabel || "Copy RSS URL";
      }, 1800);
    } catch {
      if (status) status.textContent = `Copy this feed URL: ${url}`;
    }
  };

  document.addEventListener("click", (event) => {
    const button = event.target.closest("[data-feed-copy]");
    if (!button) return;
    event.preventDefault();
    copyFeed(button);
  });

  const verifiedPanel = document.querySelector("[data-follow-research]");
  if (verifiedPanel) {
    const heading = verifiedPanel.querySelector("#home-follow-research-title");
    if (heading) heading.textContent = "Follow verified research";
    const rssOption = verifiedPanel.querySelector("[aria-labelledby='home-follow-rss-title']");
    if (rssOption) {
      const title = rssOption.querySelector("#home-follow-rss-title");
      if (title) title.textContent = "Verified Research feeds";
      const description = rssOption.querySelector("p");
      if (description) description.textContent = "Only verified, published GlassesResearch updates. Across the Wire is a separate feed.";
      const actions = rssOption.querySelector(".follow-research__actions");
      if (actions) actions.innerHTML = `
        <a class="md-button md-button--primary" href="/docs/FEEDS/#verified-research">Choose reader</a>
        <button class="md-button" type="button" data-feed-copy data-feed-url="${VERIFIED}" data-feed-label="Copy RSS URL">Copy RSS URL</button>
        <a class="md-button" href="${VERIFIED}">Raw RSS</a>
      `;
      const status = rssOption.querySelector("[data-copy-feed-status]");
      if (status) status.setAttribute("data-feed-copy-status", "");
    }
  }

  const wireSection = document.querySelector("[data-home-wire]");
  if (wireSection) {
    const old = wireSection.querySelector(".gr-wire-feed-links");
    if (old) {
      old.innerHTML = `<strong>Across the Wire feeds:</strong> <a href="/docs/FEEDS/#across-the-wire">Choose reader</a> · <button class="gr-link-button" type="button" data-feed-copy data-feed-url="${WIRE}" data-feed-label="Copy RSS URL">Copy RSS URL</button> · <a href="${WIRE}">Raw RSS</a> · <a href="/data/wire-feed.json">JSON Feed</a><span data-feed-copy-status role="status" aria-live="polite"></span>`;
    }
  }

  const newsroomActions = document.querySelector(".gr-newsroom-actions");
  if (newsroomActions) {
    const rss = [...newsroomActions.querySelectorAll("a")].find((link) => link.getAttribute("href") === "/feed.xml");
    if (rss) {
      rss.href = "/docs/FEEDS/";
      rss.textContent = "Feeds";
    }
  }
})();