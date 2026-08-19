(() => {
  const triggers = [...document.querySelectorAll('.family-tree-trigger[data-family-tree-model]')];
  if (!triggers.length) return;

  let payloadPromise;
  let activeModel = null;
  const narrow = matchMedia('(max-width: 600px)');

  function loadData() {
    if (!payloadPromise) {
      payloadPromise = fetch('/data/family-trees.json', { credentials: 'same-origin' }).then((response) => {
        if (!response.ok) throw new Error(`Family tree data unavailable (${response.status})`);
        return response.json();
      });
    }
    return payloadPromise;
  }

  function familyFor(payload, modelId) {
    return payload.families.find((family) => family.nodes.some((node) => node.canonical_id === modelId));
  }

  function incomingFor(family, nodeId) {
    return family.edges.find((edge) => edge.child === nodeId) || null;
  }

  function nodeType(node) {
    return ({ model: 'GLS model', branch: 'Branch', alias: 'Alias / rebrand', origin: 'Technology origin', family: 'Family' })[node.type] || node.type;
  }

  function makeDialog() {
    const dialog = document.createElement('dialog');
    dialog.className = 'family-tree-dialog';
    dialog.innerHTML = `
      <div class="family-tree-dialog-shell">
        <div class="family-tree-dialog-head">
          <div><div class="family-tree-eyebrow">Family tree</div><h2 data-ft-title></h2></div>
          <button type="button" class="family-tree-close" aria-label="Close family tree">×</button>
        </div>
        <p class="family-tree-summary" data-ft-summary></p>
        <div class="family-tree-controls">
          <label><input type="checkbox" data-ft-aliases checked> Retail identities / aliases</label>
          <label><input type="checkbox" data-ft-inferred checked> Inferred relationships</label>
        </div>
        <div class="family-tree-stage-wrap" data-ft-wrap>
          <div class="family-tree-stage" data-ft-stage>
            <svg class="family-tree-links" data-ft-links aria-hidden="true"></svg>
            <div class="family-tree-levels" data-ft-levels></div>
            <div class="family-tree-mobile" data-ft-mobile></div>
          </div>
        </div>
        <div class="family-tree-detail" data-ft-detail></div>
      </div>`;
    document.body.append(dialog);
    dialog.querySelector('.family-tree-close').addEventListener('click', () => dialog.close());
    dialog.addEventListener('click', (event) => {
      if (event.target === dialog) dialog.close();
    });
    dialog.querySelector('[data-ft-aliases]').addEventListener('change', () => renderCurrent(dialog));
    dialog.querySelector('[data-ft-inferred]').addEventListener('change', () => renderCurrent(dialog));
    narrow.addEventListener?.('change', () => {
      if (dialog.open) renderCurrent(dialog);
    });
    return dialog;
  }

  const dialog = makeDialog();
  let activePayload = null;
  let activeFamily = null;
  let selectedNode = null;

  function filteredGraph(family) {
    const showAliases = dialog.querySelector('[data-ft-aliases]').checked;
    const showInferred = dialog.querySelector('[data-ft-inferred]').checked;
    const byId = new Map(family.nodes.map((node) => [node.id, node]));
    const allowedNode = (node) => node && (showAliases || node.type !== 'alias') && (showInferred || node.status !== 'inferred');
    const edges = family.edges.filter((edge) => {
      if (!showInferred && edge.status === 'inferred') return false;
      return allowedNode(byId.get(edge.parent)) && allowedNode(byId.get(edge.child));
    });
    const reachable = new Set([family.root_id]);
    let changed = true;
    while (changed) {
      changed = false;
      for (const edge of edges) {
        if (reachable.has(edge.parent) && !reachable.has(edge.child)) {
          reachable.add(edge.child);
          changed = true;
        }
      }
    }
    return {
      byId,
      nodes: family.nodes.filter((node) => reachable.has(node.id) && allowedNode(node)),
      edges: edges.filter((edge) => reachable.has(edge.parent) && reachable.has(edge.child)),
    };
  }

  function showDetail(family, graph, nodeId) {
    const node = graph.byId.get(nodeId);
    if (!node) return;
    selectedNode = nodeId;
    const incoming = graph.edges.find((edge) => edge.child === nodeId);
    const parent = incoming ? graph.byId.get(incoming.parent) : null;
    const detail = dialog.querySelector('[data-ft-detail]');
    detail.replaceChildren();
    const h = document.createElement('h3');
    h.textContent = node.label;
    detail.append(h);
    const dl = document.createElement('dl');
    const rows = [
      ['Node', nodeType(node)],
      ...(node.canonical_id ? [['Canonical ID', node.canonical_id]] : []),
      ...(parent ? [['Parent', parent.label]] : []),
      ['Relationship', incoming ? incoming.label : 'family root'],
      ['Status', incoming ? incoming.status : node.status],
      ['Confidence', incoming ? incoming.confidence : '—'],
    ];
    for (const [key, value] of rows) {
      const dt = document.createElement('dt');
      const dd = document.createElement('dd');
      dt.textContent = key;
      dd.textContent = value;
      dl.append(dt, dd);
    }
    detail.append(dl);
    if (incoming?.evidence?.length) {
      const label = document.createElement('strong');
      label.textContent = 'Evidence';
      const ul = document.createElement('ul');
      for (const evidence of incoming.evidence) {
        const li = document.createElement('li');
        li.textContent = evidence;
        ul.append(li);
      }
      detail.append(label, ul);
    }
    const boundary = document.createElement('p');
    boundary.className = 'family-tree-boundary';
    boundary.textContent = 'Family position does not inherit specifications, firmware behavior, evidence, or Report Card scores.';
    detail.append(boundary);
    if (node.href && node.canonical_id) {
      const link = document.createElement('a');
      link.href = node.href;
      link.textContent = `Open ${node.canonical_id} model page →`;
      detail.append(link);
    }
    dialog.querySelectorAll('[data-ft-node]').forEach((button) => {
      button.setAttribute('aria-pressed', button.dataset.ftNode === nodeId ? 'true' : 'false');
    });
  }

  function depthMap(family, graph) {
    const depths = new Map([[family.root_id, 0]]);
    let changed = true;
    while (changed) {
      changed = false;
      for (const edge of graph.edges) {
        if (depths.has(edge.parent) && !depths.has(edge.child)) {
          depths.set(edge.child, depths.get(edge.parent) + 1);
          changed = true;
        }
      }
    }
    return depths;
  }

  function nodeButton(node, family, graph) {
    const incoming = graph.edges.find((edge) => edge.child === node.id);
    const parent = incoming ? graph.byId.get(incoming.parent) : null;
    const button = document.createElement('button');
    button.type = 'button';
    button.className = 'family-tree-node';
    button.dataset.ftNode = node.id;
    button.dataset.type = node.type;
    button.dataset.status = incoming ? incoming.status : node.status;
    if (node.canonical_id === activeModel) button.classList.add('is-current');
    button.setAttribute('aria-pressed', node.id === selectedNode ? 'true' : 'false');
    const type = document.createElement('span');
    type.className = 'family-tree-node-type';
    type.textContent = nodeType(node);
    const label = document.createElement('span');
    label.className = 'family-tree-node-label';
    label.textContent = node.label;
    button.append(type, label);
    if (node.canonical_id) {
      const id = document.createElement('span');
      id.className = 'family-tree-node-id';
      id.textContent = node.canonical_id === activeModel ? `${node.canonical_id} · current` : node.canonical_id;
      button.append(id);
    }
    if (incoming && parent) {
      const relation = document.createElement('span');
      relation.className = 'family-tree-node-relation';
      relation.textContent = `↳ ${parent.label} · ${incoming.label}`;
      button.append(relation);
    }
    button.addEventListener('click', () => showDetail(family, graph, node.id));
    return button;
  }

  function drawLinks(graph) {
    const stage = dialog.querySelector('[data-ft-stage]');
    const svg = dialog.querySelector('[data-ft-links]');
    svg.replaceChildren();
    if (narrow.matches) return;
    const stageBox = stage.getBoundingClientRect();
    const width = stage.clientWidth;
    const height = stage.scrollHeight;
    svg.setAttribute('viewBox', `0 0 ${width} ${height}`);
    svg.setAttribute('width', width);
    svg.setAttribute('height', height);
    for (const edge of graph.edges) {
      const parent = dialog.querySelector(`[data-ft-node="${edge.parent}"]`);
      const child = dialog.querySelector(`[data-ft-node="${edge.child}"]`);
      if (!parent || !child) continue;
      const p = parent.getBoundingClientRect();
      const c = child.getBoundingClientRect();
      const x1 = p.left + p.width / 2 - stageBox.left;
      const y1 = p.bottom - stageBox.top;
      const x2 = c.left + c.width / 2 - stageBox.left;
      const y2 = c.top - stageBox.top;
      const bend = Math.max(20, (y2 - y1) / 2);
      const path = document.createElementNS('http://www.w3.org/2000/svg', 'path');
      path.classList.add('family-tree-link');
      if (edge.status === 'inferred') path.classList.add('is-inferred');
      path.setAttribute('d', `M ${x1} ${y1} C ${x1} ${y1 + bend}, ${x2} ${y2 - bend}, ${x2} ${y2}`);
      svg.append(path);
    }
  }

  function renderDesktop(family, graph) {
    const levels = dialog.querySelector('[data-ft-levels]');
    const mobile = dialog.querySelector('[data-ft-mobile]');
    mobile.replaceChildren();
    levels.replaceChildren();
    levels.hidden = false;
    mobile.hidden = true;
    const depths = depthMap(family, graph);
    const maxDepth = Math.max(...depths.values());
    for (let depth = 0; depth <= maxDepth; depth += 1) {
      const level = document.createElement('div');
      level.className = 'family-tree-level';
      level.dataset.levelLabel = depth === 0 ? 'Origin / family' : `Generation / layer ${depth}`;
      for (const node of graph.nodes.filter((candidate) => depths.get(candidate.id) === depth)) {
        level.append(nodeButton(node, family, graph));
      }
      levels.append(level);
    }
    requestAnimationFrame(() => requestAnimationFrame(() => drawLinks(graph)));
  }

  function renderMobile(family, graph) {
    const levels = dialog.querySelector('[data-ft-levels]');
    const mobile = dialog.querySelector('[data-ft-mobile]');
    const svg = dialog.querySelector('[data-ft-links]');
    levels.replaceChildren();
    svg.replaceChildren();
    levels.hidden = true;
    mobile.hidden = false;
    mobile.replaceChildren();

    const children = new Map();
    for (const edge of graph.edges) {
      if (!children.has(edge.parent)) children.set(edge.parent, []);
      children.get(edge.parent).push(edge.child);
    }

    function branch(nodeId, depth = 0) {
      const node = graph.byId.get(nodeId);
      if (!node || node.type === 'alias') return null;
      const wrap = document.createElement('div');
      wrap.className = 'family-tree-mobile-branch';
      wrap.style.setProperty('--family-depth', depth);
      wrap.append(nodeButton(node, family, graph));
      const childIds = children.get(nodeId) || [];
      const aliases = childIds.map((id) => graph.byId.get(id)).filter((child) => child?.type === 'alias');
      const structural = childIds.map((id) => graph.byId.get(id)).filter((child) => child && child.type !== 'alias');
      if (aliases.length) {
        const details = document.createElement('details');
        details.className = 'family-tree-alias-group';
        const summary = document.createElement('summary');
        summary.textContent = `${aliases.length} retail ${aliases.length === 1 ? 'identity / alias' : 'identities / aliases'}`;
        details.append(summary);
        const list = document.createElement('div');
        list.className = 'family-tree-alias-list';
        for (const alias of aliases) list.append(nodeButton(alias, family, graph));
        details.append(list);
        wrap.append(details);
      }
      for (const child of structural) {
        const childBranch = branch(child.id, depth + 1);
        if (childBranch) wrap.append(childBranch);
      }
      return wrap;
    }
    const root = branch(family.root_id, 0);
    if (root) mobile.append(root);
  }

  function renderCurrent() {
    if (!activeFamily) return;
    const graph = filteredGraph(activeFamily);
    if (!graph.nodes.some((node) => node.id === selectedNode)) {
      selectedNode = graph.nodes.find((node) => node.canonical_id === activeModel)?.id || activeFamily.root_id;
    }
    dialog.querySelector('[data-ft-title]').textContent = activeFamily.label;
    dialog.querySelector('[data-ft-summary]').textContent = activeFamily.summary;
    if (narrow.matches) renderMobile(activeFamily, graph);
    else renderDesktop(activeFamily, graph);
    showDetail(activeFamily, graph, selectedNode);
  }

  async function openFor(modelId, source) {
    try {
      activePayload = await loadData();
      activeFamily = familyFor(activePayload, modelId);
      if (!activeFamily) return;
      activeModel = modelId;
      selectedNode = activeFamily.nodes.find((node) => node.canonical_id === modelId)?.id || activeFamily.root_id;
      renderCurrent();
      dialog.showModal();
      dialog.querySelector('.family-tree-close').focus();
    } catch (error) {
      console.error(error);
      source.setAttribute('title', 'Family tree unavailable');
    }
  }

  for (const trigger of triggers) {
    trigger.addEventListener('click', () => openFor(trigger.dataset.familyTreeModel, trigger));
  }
})();
