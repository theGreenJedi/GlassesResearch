(() => {
  const MODEL_PATH = /\/models\/catalog\/(gls-\d{4})\/?$/i;

  function textOfTableValue(label) {
    const rows = Array.from(document.querySelectorAll('.md-content table tr'));
    const row = rows.find((candidate) => candidate.cells?.[0]?.textContent?.trim() === label);
    return row?.cells?.[1]?.textContent?.trim() || '';
  }

  function headingAnchor(label) {
    const heading = Array.from(document.querySelectorAll('.md-content h2')).find(
      (item) => item.textContent.trim().toLowerCase() === label.toLowerCase(),
    );
    return heading?.id ? `#${heading.id}` : '';
  }

  function followHref(id, modelName) {
    const terms = [id, modelName].filter(Boolean).join(', ');
    return `/docs/RESEARCH_NEWS/?model=${encodeURIComponent(terms)}#verified-research-alerts`;
  }

  function link(href, label, primary = false) {
    const a = document.createElement('a');
    a.href = href;
    a.textContent = label;
    a.className = `md-button${primary ? ' md-button--primary' : ''}`;
    return a;
  }

  function hydrate() {
    const match = location.pathname.match(MODEL_PATH);
    if (!match) return;
    const article = document.querySelector('.md-content__inner');
    const h1 = article?.querySelector('h1');
    if (!article || !h1 || article.dataset.knowledgeFlow === 'true') return;
    article.dataset.knowledgeFlow = 'true';

    const id = match[1].toUpperCase();
    const modelName = textOfTableValue('Model');
    const compare = `/docs/COMPARISON_ENGINE/?left=${encodeURIComponent(id)}`;
    const follow = followHref(id, modelName);
    const reportCard = headingAnchor('GlassesResearch Report Card');
    const sources = headingAnchor('Sources');

    const actions = document.createElement('nav');
    actions.className = 'model-flow-actions';
    actions.setAttribute('aria-label', 'Continue from this model');
    if (reportCard) actions.append(link(reportCard, 'Report Card', true));
    actions.append(link(compare, 'Compare'));
    if (sources) actions.append(link(sources, 'Evidence'));
    actions.append(link(follow, 'Follow this model'));
    h1.insertAdjacentElement('afterend', actions);

    const continuation = document.createElement('section');
    continuation.className = 'model-flow-continue';
    continuation.innerHTML = '<h2>Continue researching</h2><p>Keep this model as the reference point while you move through the research.</p>';
    const links = document.createElement('nav');
    links.className = 'model-flow-actions';
    links.setAttribute('aria-label', 'Next research paths');
    links.append(link(compare, 'Compare this model', true));
    const related = headingAnchor('Related models');
    if (related) links.append(link(related, 'Related models'));
    const guides = headingAnchor('Relevant buying and use-case guides');
    if (guides) links.append(link(guides, 'Use-case guides'));
    links.append(link('/docs/RESEARCH_NEWS/', 'Research & News'));
    links.append(link(follow, 'Follow this model'));
    links.append(link('/docs/RESEARCH_CHALLENGES/', 'Challenge or add evidence'));
    continuation.append(links);
    article.append(continuation);
  }

  hydrate();
  document.addEventListener('DOMContentLoaded', hydrate, { once: true });
})();
