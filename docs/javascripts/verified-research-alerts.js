(() => {
  const CADENCES = ["as_verified", "daily", "weekly", "monthly", "annually"];
  const PANEL_SELECTOR = ".verified-alerts";
  const ENDPOINT = "https://alerts.glassesresearch.org/subscribe";

  function normalizeList(value) {
    return String(value || "").split(",").map((item) => item.trim()).filter(Boolean).slice(0, 50);
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

  function cleanupPanel(root) {
    const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT);
    const nodes = [];
    while (walker.nextNode()) nodes.push(walker.currentNode);
    for (const node of nodes) {
      if (node.nodeValue?.includes("</fieldset>")) {
        node.nodeValue = node.nodeValue.replaceAll("</fieldset>", "");
      }
    }
  }

  function resetPanel(root) {
    root.querySelectorAll('input[type="email"], input[type="text"]').forEach((input) => { input.value = ""; });
    root.querySelectorAll('input[type="checkbox"]').forEach((input) => { input.checked = false; });
    const cadence = root.querySelector('[name="cadence"]');
    if (cadence) cadence.value = "as_verified";
  }

  async function submitPanel(root, button) {
    const status = root.querySelector("[data-alert-status]");
    if (!status || !button || button.dataset.submitting === "true") return;

    cleanupPanel(root);
    status.textContent = "";

    let payload;
    try {
      payload = payloadFrom(root);
      if (!payload.email || !payload.email.includes("@")) throw new Error("Enter a valid email address.");
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
      if (!response.ok || result.ok === false) {
        throw new Error(result.message || "Subscription service is temporarily unavailable.");
      }
      status.textContent = result.message || "Check your email to confirm your subscription.";
      resetPanel(root);
    } catch (error) {
      status.textContent = error instanceof Error ? error.message : "Subscription service is temporarily unavailable.";
    } finally {
      delete button.dataset.submitting;
      button.disabled = false;
    }
  }

  document.addEventListener("click", (event) => {
    const button = event.target instanceof Element ? event.target.closest(`${PANEL_SELECTOR} button[type="submit"]`) : null;
    if (!button) return;
    const root = button.closest(PANEL_SELECTOR);
    if (!root) return;
    event.preventDefault();
    submitPanel(root, button);
  });

  document.addEventListener("submit", (event) => {
    const form = event.target instanceof HTMLFormElement ? event.target : null;
    const root = form?.closest(PANEL_SELECTOR);
    if (!root) return;
    event.preventDefault();
    const button = root.querySelector('button[type="submit"]');
    if (button) submitPanel(root, button);
  });

  function cleanAll() {
    document.querySelectorAll(PANEL_SELECTOR).forEach(cleanupPanel);
  }

  cleanAll();
  new MutationObserver(cleanAll).observe(document.documentElement, { childList: true, subtree: true });
})();
