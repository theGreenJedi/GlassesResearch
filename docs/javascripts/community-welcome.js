// Show one transparent, opt-in greeting on the contribution page.
// The greeting is selected only from an explicit ?from= parameter in the link.
// No referrer inspection, cookies, localStorage, fingerprinting, or persistence.

function showCommunityWelcome() {
  const article = document.querySelector("article.md-content__inner");
  if (!article) return;

  const heading = article.querySelector("h1");
  if (!heading || !heading.textContent.toLowerCase().includes("want to contribute")) return;

  const source = new URLSearchParams(window.location.search).get("from");
  if (!source) return;

  const greetings = {
    reddit: {
      title: "Welcome, Redditor!",
      message:
        "Great discussions can disappear into old threads. Help us preserve useful smart-glasses knowledge as a permanent, searchable reference.",
    },
    discord: {
      title: "Welcome, Discord member!",
      message:
        "Real-time chats generate valuable discoveries. Help us preserve the best findings beyond today's conversation.",
    },
    github: {
      title: "Welcome, Developer!",
      message:
        "Code, testing, documentation, reverse engineering, issue reports, and one-line corrections are all valuable contributions.",
    },
    youtube: {
      title: "Welcome, YouTube viewer!",
      message:
        "Videos demonstrate what is possible. Help us preserve the supporting details, sources, firmware history, and reproducible steps.",
    },
    forum: {
      title: "Welcome, Forum member!",
      message:
        "Specialist forums hold years of hard-won knowledge. Help us preserve and properly credit discoveries before links and communities disappear.",
    },
    hackernews: {
      title: "Welcome, Hacker News reader!",
      message:
        "We value reproducible findings, primary sources, careful attribution, interoperability, and clearly labeled uncertainty.",
    },
    matrix: {
      title: "Welcome, Matrix member!",
      message:
        "Open communities create valuable technical knowledge. Help us turn useful discoveries into durable public documentation.",
    },
  };

  const greeting = greetings[source.toLowerCase()];
  if (!greeting) return;

  const box = document.createElement("div");
  box.className = "admonition welcome";
  box.setAttribute("role", "note");

  const title = document.createElement("p");
  title.className = "admonition-title";
  title.textContent = greeting.title;

  const message = document.createElement("p");
  message.textContent = greeting.message;

  const privacy = document.createElement("p");
  privacy.innerHTML =
    "<small>This greeting came from the explicit community link you clicked. GlassesResearch does not inspect your browsing history, set tracking cookies, or remember the source after this page.</small>";

  box.append(title, message, privacy);
  heading.insertAdjacentElement("afterend", box);
}

if (typeof document$ !== "undefined") {
  document$.subscribe(showCommunityWelcome);
} else {
  document.addEventListener("DOMContentLoaded", showCommunityWelcome);
}
