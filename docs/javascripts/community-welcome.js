// Show a transparent, non-persistent welcome banner on the homepage and contribution page.
// Community-specific text is selected only from an explicit ?from= parameter.
// No referrer inspection, cookies, localStorage, fingerprinting, or persistence.

function showCommunityWelcome() {
  const article = document.querySelector("article.md-content__inner");
  if (!article) return;

  const heading = article.querySelector("h1");
  if (!heading) return;

  const normalizedHeading = heading.textContent.trim().toLowerCase();
  const isHomepage = normalizedHeading === "glassesresearch";
  const isContributionPage = normalizedHeading.includes("want to contribute");
  if (!isHomepage && !isContributionPage) return;

  const source = new URLSearchParams(window.location.search).get("from");
  const greetings = {
    reddit: {
      title: "Welcome, Redditor!",
      message: "Useful smart-glasses knowledge should outlive the thread where it first appeared. Search the research or help preserve what your community has learned.",
    },
    discord: {
      title: "Welcome, Discord member!",
      message: "Real-time chats generate valuable discoveries. Explore the research or help preserve the best findings beyond today's conversation.",
    },
    github: {
      title: "Welcome, Developer!",
      message: "Explore models, protocols, firmware, SDKs, reverse engineering, recovery, and vendor-independent development.",
    },
    youtube: {
      title: "Welcome, YouTube viewer!",
      message: "Videos show what is possible. GlassesResearch preserves the supporting details, sources, firmware history, and reproducible steps.",
    },
    forum: {
      title: "Welcome, Forum member!",
      message: "Specialist forums hold years of hard-won knowledge. Explore the collection or help preserve discoveries before links and communities disappear.",
    },
    hackernews: {
      title: "Welcome, Hacker News reader!",
      message: "Start with the evidence: reproducible findings, primary sources, careful attribution, interoperability, and clearly labeled uncertainty.",
    },
    matrix: {
      title: "Welcome, Matrix member!",
      message: "Open communities create valuable technical knowledge. Explore the collection or help turn useful discoveries into durable public documentation.",
    },
  };

  const defaultGreeting = {
    title: "Welcome to GlassesResearch",
    message: "Choose a research collection below: questions, hacking, models, buying guidance, news, history, glossary, or the hands-on W610 investigation.",
  };

  const greeting = source ? greetings[source.toLowerCase()] : defaultGreeting;
  if (!greeting) return;

  const existing = article.querySelector(".glassesresearch-welcome");
  if (existing) existing.remove();

  const box = document.createElement("div");
  box.className = "admonition welcome glassesresearch-welcome";
  box.setAttribute("role", "note");

  const title = document.createElement("p");
  title.className = "admonition-title";
  title.textContent = greeting.title;

  const message = document.createElement("p");
  message.textContent = greeting.message;

  box.append(title, message);

  if (source) {
    const privacy = document.createElement("p");
    privacy.innerHTML = "<small>This greeting came only from the explicit community link you clicked. GlassesResearch does not inspect referrers, set tracking cookies, or remember the source.</small>";
    box.append(privacy);
  }

  heading.insertAdjacentElement("afterend", box);
}

if (typeof document$ !== "undefined") {
  document$.subscribe(showCommunityWelcome);
} else {
  document.addEventListener("DOMContentLoaded", showCommunityWelcome);
}
