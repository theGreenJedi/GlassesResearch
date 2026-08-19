(() => {
  const shell = document.querySelector('[data-family-tree-beta]');
  const source = document.getElementById('family-tree-beta-data');
  if (!shell || !source) return;
  const data = JSON.parse(source.textContent);
  if (data.beta_only !== true || data.rules.public_site_enabled !== false) return;

  const familySelect = shell.querySelector('[data-ft-family]');
  const aliasToggle = shell.querySelector('[data-ft-aliases]');
  const inferredToggle = shell.querySelector('[data-ft-inferred]');
  const summary = shell.querySelector('[data-ft-summary]');
  const stage = shell.querySelector('[data-ft-stage]');
  const levels = shell.querySelector('[data-ft-levels]');
  const links = shell.querySelector('[data-ft-links]');
  const detail = shell.querySelector('[data-ft-detail]');
  const mobileQuery = matchMedia('(max-width: 600px)');
  let selectedFamily = data.families[0].id;
  let selectedNode = null;

  for (const family of data.families) {
    const option = document.createElement('option');
    option.value = family.id;
    option.textContent = family.label;
    familySelect.append(option);
  }

  function family() {
    return data.families.find((item) => item.id === selectedFamily);
  }

  function graph(item) {
    const byId = new Map(item.nodes.map((node) => [node.id, node]));
    const allowed = (node) => {
      if (!node) return false;
      if (!aliasToggle.checked && node.type === 'alias') return false;
      if (!inferredToggle.checked && node.status === 'inferred') return false;
      return true;
    };
    const possibleEdges = item.edges.filter((edge) => {
      if (!inferredToggle.checked && edge.status === 'inferred') return false;
      return allowed(byId.get(edge.parent)) && allowed(byId.get(edge.child));
    });
    const reachable = new Set([item.root_id]);
    let changed = true;
    while (changed) {
      changed = false;
      for (const edge of possibleEdges) {
        if (reachable.has(edge.parent) && !reachable.has(edge.child)) {
          reachable.add(edge.child);
          changed = true;
        }
      }
    }
    return {
      byId,
      nodes: item.nodes.filter((node) => reachable.has(node.id) && allowed(node)),
      edges: possibleEdges.filter((edge) => reachable.has(edge.parent) && reachable.has(edge.child)),
    };
  }

  function depthMap(item, current) {
    const depths = new Map([[item.root_id, 0]]);
    let changed = true;
    while (changed) {
      changed = false;
      for (const edge of current.edges) {
        if (depths.has(edge.parent) && !depths.has(edge.child)) {
          depths.set(edge.child, depths.get(edge.parent) + 1);
          changed = true;
        }
      }
    }
    return depths;
  }

  function typeName(node) {
    return ({model: 'GLS model', branch: 'Branch', alias: 'Alias / rebrand', origin: 'Technology origin', family: 'Family'})[node.type] || node.type;
  }

  function incomingEdge(current, nodeId) {
    return current.edges.find((edge) => edge.child === nodeId);
  }

  function nodeButton(item, current, node) {
    const incoming = incomingEdge(current, node.id);
    const parent = incoming ? current.byId.get(incoming.parent) : null;
    const button = document.createElement('button');
    button.type = 'button';
    button.className = 'ft-node';
    button.dataset.nodeId = node.id;
    button.dataset.nodeType = node.type;
    button.dataset.status = incoming ? incoming.status : node.status;
    button.setAttribute('aria-pressed', 'false');

    const type = document.createElement('span');
    type.className = 'ft-node-type';
    type.textContent = typeName(node);
    const label = document.createElement('span');
    label.className = 'ft-node-label';
    label.textContent = node.label;
    button.append(type, label);

    if (node.canonical_id) {
      const id = document.createElement('span');
      id.className = 'ft-node-id';
      id.textContent = node.canonical_id;
      button.append(id);
    }
    if (incoming) {
      const relation = document.createElement('span');
      relation.className = 'ft-node-relation';
      relation.textContent = `↳ ${parent ? parent.label : incoming.parent} · ${incoming.label}`;
      button.append(relation);
    }
    button.addEventListener('click', () => showDetail(item, current, node.id));
    return button;
  }

  function showDetail(item, current, nodeId) {
    const node = current.byId.get(nodeId);
    if (!node) return;
    selectedNode = nodeId;
    detail.replaceChildren();
    const title = document.createElement('h2');
    title.textContent = node.label;
    detail.append(title);
    const facts = document.createElement('dl');
    const incoming = incomingEdge(current, nodeId);
    const parent = incoming ? current.byId.get(incoming.parent) : null;
    const rows = [
      ['Node', typeName(node)],
      ...(node.canonical_id ? [['Canonical ID', node.canonical_id]] : []),
      ['Parent', parent ? parent.label : '—'],
      ['Relationship', incoming ? incoming.label : 'family root'],
      ['Status', incoming ? incoming.status : node.status],
      ['Confidence', incoming ? incoming.confidence : '—'],
    ];
    for (const [key, value] of rows) {
      const dt = document.createElement('dt');
      const dd = document.createElement('dd');
      dt.textContent = key;
      dd.textContent = value;
      facts.append(dt, dd);
    }
    detail.append(facts);
    if (incoming && incoming.evidence.length) {
      const strong = document.createElement('strong');
      strong.textContent = 'Evidence paths';
      const list = document.createElement('ul');
      for (const itemPath of incoming.evidence) {
        const li = document.createElement('li');
        li.textContent = itemPath;
        list.append(li);
      }
      detail.append(strong, list);
    }
    const boundary = document.createElement('div');
    boundary.className = 'ft-boundary';
    boundary.textContent = 'No evidence inheritance. Family position never copies specifications, firmware behavior, ownership claims, or Report Card scores into this node.';
    detail.append(boundary);
    if (node.href && node.canonical_id) {
      const link = document.createElement('a');
      link.className = 'ft-model-link';
      link.href = node.href;
      link.textContent = `Open ${node.canonical_id} model page →`;
      detail.append(link);
    }
    for (const button of shell.querySelectorAll('.ft-node')) {
      button.setAttribute('aria-pressed', button.dataset.nodeId === nodeId ? 'true' : 'false');
    }
  }

  function draw(current) {
    links.replaceChildren();
    if (mobileQuery.matches) return;
    const stageBox = stage.getBoundingClientRect();
    const width = Math.max(stage.scrollWidth, stage.clientWidth);
    const height = Math.max(stage.scrollHeight, stage.clientHeight);
    links.setAttribute('viewBox', `0 0 ${width} ${height}`);
    links.setAttribute('width', width);
    links.setAttribute('height', height);
    for (const edge of current.edges) {
      const parent = shell.querySelector(`[data-node-id="${edge.parent}"]`);
      const child = shell.querySelector(`[data-node-id="${edge.child}"]`);
      if (!parent || !child) continue;
      const p = parent.getBoundingClientRect();
      const c = child.getBoundingClientRect();
      const x1 = p.left + p.width / 2 - stageBox.left;
      const y1 = p.bottom - stageBox.top;
      const x2 = c.left + c.width / 2 - stageBox.left;
      const y2 = c.top - stageBox.top;
      const bend = Math.max(24, (y2 - y1) / 2);
      const path = document.createElementNS('http://www.w3.org/2000/svg', 'path');
      path.setAttribute('class', 'ft-link');
      path.dataset.status = edge.status;
      path.setAttribute('d', `M ${x1} ${y1} C ${x1} ${y1 + bend}, ${x2} ${y2 - bend}, ${x2} ${y2}`);
      links.append(path);
    }
  }

  function renderDesktop(item, current) {
    const depths = depthMap(item, current);
    const maxDepth = Math.max(...depths.values());
    levels.className = 'ft-levels';
    levels.replaceChildren();
    for (let level = 0; level <= maxDepth; level += 1) {
      const column = document.createElement('div');
      column.className = 'ft-level';
      column.dataset.levelLabel = level === 0 ? 'Origin / family' : `Generation / layer ${level}`;
      for (const node of current.nodes.filter((candidate) => depths.get(candidate.id) === level)) {
        column.append(nodeButton(item, current, node));
      }
      levels.append(column);
    }
  }

  function renderMobile(item, current) {
    levels.className = 'ft-mobile-tree';
    levels.replaceChildren();
    const children = new Map(current.nodes.map((node) => [node.id, []]));
    for (const edge of current.edges) {
      children.get(edge.parent)?.push(edge.child);
    }

    const walk = (nodeId) => {
      const node = current.byId.get(nodeId);
      const subtree = document.createElement('div');
      subtree.className = 'ft-mobile-subtree';
      subtree.append(nodeButton(item, current, node));

      const childIds = children.get(nodeId) || [];
      const aliases = childIds.map((id) => current.byId.get(id)).filter((child) => child.type === 'alias');
      const structural = childIds.map((id) => current.byId.get(id)).filter((child) => child.type !== 'alias');

      if (structural.length) {
        const branch = document.createElement('div');
        branch.className = 'ft-mobile-children';
        for (const child of structural) branch.append(walk(child.id));
        subtree.append(branch);
      }

      if (aliases.length) {
        const group = document.createElement('details');
        group.className = 'ft-alias-group';
        const groupLabel = document.createElement('summary');
        const noun = aliases.length === 1 ? 'retail identity / alias' : 'retail identities / aliases';
        groupLabel.textContent = `${aliases.length} ${noun} for ${node.label}`;
        group.append(groupLabel);
        const aliasList = document.createElement('div');
        aliasList.className = 'ft-alias-list';
        for (const alias of aliases) aliasList.append(nodeButton(item, current, alias));
        group.append(aliasList);
        subtree.append(group);
      }
      return subtree;
    };

    levels.append(walk(item.root_id));
  }

  function render() {
    const item = family();
    const current = graph(item);
    summary.textContent = `${item.label} — ${item.summary} (${current.nodes.length} total nodes)`;
    if (mobileQuery.matches) renderMobile(item, current);
    else renderDesktop(item, current);

    if (!current.nodes.some((node) => node.id === selectedNode)) selectedNode = item.root_id;
    showDetail(item, current, selectedNode);
    requestAnimationFrame(() => requestAnimationFrame(() => draw(current)));
  }

  familySelect.addEventListener('change', () => {
    selectedFamily = familySelect.value;
    selectedNode = null;
    render();
  });
  aliasToggle.addEventListener('change', render);
  inferredToggle.addEventListener('change', render);
  mobileQuery.addEventListener('change', render);
  addEventListener('resize', () => {
    if (!mobileQuery.matches) requestAnimationFrame(() => draw(graph(family())));
  });
  familySelect.value = selectedFamily;
  render();
})();
