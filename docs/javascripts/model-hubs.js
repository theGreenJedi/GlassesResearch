/* Progressive model-hub navigation.
 * Associations come from /data/model-hubs.json; this script makes no research
 * claims and leaves pages unchanged when no curated hub record exists.
 */
(() => {
  const modelIdFromPage = () => {
    const heading = document.querySelector('main h1, article h1');
    const match = heading?.textContent?.match(/\bGLS-\d{4}\b/i);
    return match ? match[0].toUpperCase() : null;
  };

  const safeInternal = (url) => typeof url === 'string' && url.startsWith('/') && !url.startsWith('//');

  const makeLink = (item) => {
    if (!item || !safeInternal(item.url)) return null;
    const li = document.createElement('li');
    const a = document.createElement('a');
    a.href = item.url;
    a.textContent = item.label || item.url;
    li.append(a);
    if (item.note) {
      const note = document.createElement('span');
      note.className = 'gr-model-hub__note';
      note.textContent = ` — ${item.note}`;
      li.append(note);
    }
    return li;
  };

  const replaceGenericRelatedModels = (article, hub) => {
    const curated = (hub.related_models || []).filter((item) => safeInternal(item?.url));
    if (!curated.length) return;

    const heading = [...article.querySelectorAll('h2')]
      .find((node) => node.textContent?.trim().toLowerCase() === 'related models');
    if (!heading) return;

    let node = heading.nextElementSibling;
    while (node && !/^H[12]$/.test(node.tagName)) {
      const next = node.nextElementSibling;
      node.remove();
      node = next;
    }

    heading.textContent = 'Lineage and ecosystem neighbors';
    const intro = document.createElement('p');
    intro.textContent = 'Curated relationships are shown before generic capability similarity. Shared software or ecosystem membership does not imply identical hardware.';
    heading.after(intro);

    const ul = document.createElement('ul');
    curated.map(makeLink).filter(Boolean).forEach((li) => ul.append(li));
    intro.after(ul);
  };

  const render = (hub) => {
    const article = document.querySelector('article.md-content__inner, main .md-content__inner, main article');
    if (!article || article.querySelector('[data-gr-model-hub]')) return;

    const section = document.createElement('section');
    section.dataset.grModelHub = 'true';
    section.className = 'gr-model-hub';

    const h2 = document.createElement('h2');
    h2.textContent = 'Research hub';
    section.append(h2);

    const intro = document.createElement('p');
    intro.textContent = 'Everything GlassesResearch has attached to this model, without turning research leads into verified product claims.';
    section.append(intro);

    const research = [...(hub.research || []), ...(hub.evidence || [])];
    if (research.length) {
      const h3 = document.createElement('h3');
      h3.textContent = 'Go deeper';
      section.append(h3);
      const ul = document.createElement('ul');
      research.map(makeLink).filter(Boolean).forEach((li) => ul.append(li));
      if (ul.children.length) section.append(ul);
    }

    const questions = [hub.open_questions, hub.research_backlog].filter(Boolean);
    if (questions.length) {
      const h3 = document.createElement('h3');
      h3.textContent = 'What we still need to learn';
      section.append(h3);
      const ul = document.createElement('ul');
      questions.map(makeLink).filter(Boolean).forEach((li) => ul.append(li));
      if (ul.children.length) section.append(ul);
    }

    const firstSection = article.querySelector('h2');
    if (firstSection) firstSection.before(section);
    else article.append(section);

    replaceGenericRelatedModels(article, hub);
  };

  const run = async () => {
    const id = modelIdFromPage();
    if (!id) return;
    try {
      const response = await fetch('/data/model-hubs.json', { credentials: 'same-origin' });
      if (!response.ok) return;
      const payload = await response.json();
      const hub = payload?.models?.[id];
      if (hub) render(hub);
    } catch (_) {
      // Progressive enhancement: canonical model page remains fully usable.
    }
  };

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', run, { once: true });
  else run();
})();
