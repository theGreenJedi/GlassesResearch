(() => {
  const root = document.querySelector('[data-ecosystem-constellation]');
  if (!root) return;

  const canvas = root.querySelector('[data-ecosystem-canvas]');
  const inspector = root.querySelector('[data-ecosystem-inspector]');
  const filters = [...root.querySelectorAll('[data-ecosystem-filter]')];
  if (!canvas || !inspector) return;

  const endpoint = '/data/ecosystem-relations.json';
  const typeLabels = {
    model: 'Glasses',
    lineage: 'Lineage',
    operating_platform: 'Platform',
    companion_app: 'Companion app',
    sdk_api: 'SDK / API',
    protocol_transport: 'Transport',
    ai_service: 'AI / cloud service',
    community_project: 'Community project'
  };
  const relationLabels = {
    member_of: 'Member of',
    rebrand_of: 'Rebrand of',
    manufactured_by: 'Manufactured by',
    uses_platform: 'Uses platform',
    compatible_with: 'Compatible with',
    requires_app: 'Requires app',
    exposes_sdk: 'Exposes SDK',
    uses_protocol: 'Uses protocol',
    depends_on_service: 'Depends on service',
    community_supports: 'Community supports',
    supersedes: 'Supersedes'
  };

  const esc = (value) => String(value ?? '')
    .replaceAll('&', '&amp;')
    .replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;')
    .replaceAll('"', '&quot;')
    .replaceAll("'", '&#039;');

  const slug = (value) => String(value || '').replace(/_/g, ' ');
  const labelType = (value) => typeLabels[value] || slug(value);
  const labelRelation = (value) => relationLabels[value] || slug(value);

  const renderInspectorIntro = (data) => {
    inspector.innerHTML = `
      <p class="gr-inspector-eyebrow">Trace the stack</p>
      <h3>${data.nodes.length} mapped nodes.<br>${data.relations.length} evidence-backed links.</h3>
      <p>Select any bubble to isolate its immediate ecosystem. The rest fades back so the relationship is readable instead of merely impressive.</p>
      <div class="gr-ecosystem-relations">
        <span class="gr-ecosystem-relation"><strong>Glasses stay at the center.</strong><span>Platforms, apps, SDKs, transports, services and community projects orbit the hardware they affect.</span></span>
      </div>`;
  };

  const render = (data) => {
    const width = 980;
    const height = 720;
    const center = { x: width * .49, y: height * .5 };
    const nodes = data.nodes.map((node, index) => ({ ...node, index }));
    const nodeById = new Map(nodes.map((node) => [node.id, node]));
    const relations = data.relations
      .map((rel) => ({ ...rel, source: nodeById.get(rel.from), target: nodeById.get(rel.to) }))
      .filter((rel) => rel.source && rel.target);

    const modelNodes = nodes.filter((node) => node.type === 'model');
    const otherNodes = nodes.filter((node) => node.type !== 'model');

    modelNodes.forEach((node, i) => {
      const angle = (Math.PI * 2 * i) / Math.max(1, modelNodes.length) - Math.PI / 2;
      const radius = Math.min(width, height) * .24;
      node.x = center.x + Math.cos(angle) * radius;
      node.y = center.y + Math.sin(angle) * radius;
      node.anchorX = node.x;
      node.anchorY = node.y;
    });

    otherNodes.forEach((node, i) => {
      const neighbors = relations
        .filter((rel) => rel.source.id === node.id || rel.target.id === node.id)
        .map((rel) => rel.source.id === node.id ? rel.target : rel.source)
        .filter((neighbor) => neighbor.type === 'model');
      if (neighbors.length) {
        const ax = neighbors.reduce((sum, n) => sum + n.x, 0) / neighbors.length;
        const ay = neighbors.reduce((sum, n) => sum + n.y, 0) / neighbors.length;
        const angle = (i * 2.399963229728653) % (Math.PI * 2);
        node.x = ax + Math.cos(angle) * (92 + (i % 3) * 26);
        node.y = ay + Math.sin(angle) * (82 + (i % 4) * 20);
      } else {
        const angle = (Math.PI * 2 * i) / Math.max(1, otherNodes.length);
        node.x = center.x + Math.cos(angle) * 260;
        node.y = center.y + Math.sin(angle) * 230;
      }
      node.anchorX = node.x;
      node.anchorY = node.y;
    });

    const radiusFor = (node) => {
      const degree = relations.filter((rel) => rel.source.id === node.id || rel.target.id === node.id).length;
      if (node.type === 'model') return 44 + Math.min(degree * 2, 10);
      if (node.type === 'operating_platform') return 40 + Math.min(degree * 2, 8);
      return 31 + Math.min(degree * 1.6, 8);
    };

    // A small deterministic relaxation pass keeps the network organic without an external graph library.
    for (let pass = 0; pass < 110; pass += 1) {
      for (let i = 0; i < nodes.length; i += 1) {
        const a = nodes[i];
        let dx = (a.anchorX - a.x) * .014;
        let dy = (a.anchorY - a.y) * .014;
        for (let j = 0; j < nodes.length; j += 1) {
          if (i === j) continue;
          const b = nodes[j];
          const vx = a.x - b.x;
          const vy = a.y - b.y;
          const distance2 = Math.max(36, vx * vx + vy * vy);
          const distance = Math.sqrt(distance2);
          const minDistance = radiusFor(a) + radiusFor(b) + 20;
          if (distance < minDistance) {
            const push = (minDistance - distance) * .038;
            dx += (vx / distance) * push;
            dy += (vy / distance) * push;
          }
        }
        a.x += dx;
        a.y += dy;
        a.x = Math.max(radiusFor(a) + 20, Math.min(width - radiusFor(a) - 20, a.x));
        a.y = Math.max(radiusFor(a) + 20, Math.min(height - radiusFor(a) - 20, a.y));
      }
    }

    const svgNS = 'http://www.w3.org/2000/svg';
    const svg = document.createElementNS(svgNS, 'svg');
    svg.classList.add('gr-ecosystem-svg');
    svg.setAttribute('viewBox', `0 0 ${width} ${height}`);
    svg.setAttribute('role', 'img');
    svg.setAttribute('aria-label', 'Interactive map of smart-glasses ecosystem relationships');

    const edgeLayer = document.createElementNS(svgNS, 'g');
    const nodeLayer = document.createElementNS(svgNS, 'g');
    svg.append(edgeLayer, nodeLayer);

    relations.forEach((rel) => {
      const line = document.createElementNS(svgNS, 'line');
      line.classList.add('gr-ecosystem-edge');
      line.dataset.from = rel.from;
      line.dataset.to = rel.to;
      line.dataset.status = rel.status || 'established';
      line.setAttribute('x1', rel.source.x);
      line.setAttribute('y1', rel.source.y);
      line.setAttribute('x2', rel.target.x);
      line.setAttribute('y2', rel.target.y);
      edgeLayer.appendChild(line);
      rel.element = line;
    });

    nodes.forEach((node) => {
      const group = document.createElementNS(svgNS, 'g');
      group.classList.add('gr-ecosystem-node');
      group.dataset.id = node.id;
      group.dataset.type = node.type;
      group.setAttribute('transform', `translate(${node.x} ${node.y})`);
      group.setAttribute('tabindex', '0');
      group.setAttribute('role', 'button');
      group.setAttribute('aria-label', `${node.label}, ${labelType(node.type)}`);

      const circle = document.createElementNS(svgNS, 'circle');
      circle.setAttribute('r', radiusFor(node));
      group.appendChild(circle);

      const name = document.createElementNS(svgNS, 'text');
      name.classList.add('gr-node-name');
      name.setAttribute('y', '-4');
      const words = String(node.label || '').split(/\s+/);
      const line1 = words.length > 2 ? words.slice(0, Math.ceil(words.length / 2)).join(' ') : node.label;
      const line2 = words.length > 2 ? words.slice(Math.ceil(words.length / 2)).join(' ') : '';
      const t1 = document.createElementNS(svgNS, 'tspan');
      t1.setAttribute('x', '0');
      t1.textContent = line1;
      name.appendChild(t1);
      if (line2) {
        const t2 = document.createElementNS(svgNS, 'tspan');
        t2.setAttribute('x', '0');
        t2.setAttribute('dy', '13');
        t2.textContent = line2;
        name.appendChild(t2);
      }
      group.appendChild(name);

      const type = document.createElementNS(svgNS, 'text');
      type.classList.add('gr-node-type');
      type.setAttribute('y', line2 ? '23' : '14');
      type.textContent = labelType(node.type);
      group.appendChild(type);

      node.element = group;
      nodeLayer.appendChild(group);
    });

    canvas.replaceChildren(svg);
    renderInspectorIntro(data);

    const clearSelection = () => {
      nodes.forEach((node) => node.element.classList.remove('is-muted', 'is-active'));
      relations.forEach((rel) => rel.element.classList.remove('is-muted', 'is-active'));
    };

    const selectNode = (node) => {
      const attached = relations.filter((rel) => rel.source.id === node.id || rel.target.id === node.id);
      const neighborIds = new Set([node.id]);
      attached.forEach((rel) => {
        neighborIds.add(rel.source.id);
        neighborIds.add(rel.target.id);
      });

      nodes.forEach((candidate) => {
        candidate.element.classList.toggle('is-active', candidate.id === node.id);
        candidate.element.classList.toggle('is-muted', !neighborIds.has(candidate.id));
      });
      relations.forEach((rel) => {
        const active = rel.source.id === node.id || rel.target.id === node.id;
        rel.element.classList.toggle('is-active', active);
        rel.element.classList.toggle('is-muted', !active);
      });

      const relationCards = attached.map((rel) => {
        const outbound = rel.source.id === node.id;
        const other = outbound ? rel.target : rel.source;
        const direction = outbound ? labelRelation(rel.type) : `Linked by ${labelRelation(rel.type).toLowerCase()}`;
        const status = rel.status || 'established';
        const confidence = rel.confidence || 'unknown confidence';
        return `<span class="gr-ecosystem-relation"><strong>${esc(direction)} → ${esc(other.label)}</strong><span>${esc(status)} · ${esc(confidence)} · ${esc(rel.provenance || 'provenance unknown')}</span></span>`;
      }).join('');

      const target = node.path ? `/${node.path.replace(/README\.md$/, '').replace(/\.md$/, '/').replace(/^\//, '')}` : node.url;
      const visit = target ? `<p><a href="${esc(target)}">Open the underlying research →</a></p>` : '';
      inspector.innerHTML = `
        <p class="gr-inspector-eyebrow">${esc(labelType(node.type))}</p>
        <h3>${esc(node.label)}</h3>
        <p>${attached.length ? `${attached.length} mapped relationship${attached.length === 1 ? '' : 's'} touch this node.` : 'No mapped relationships yet.'}</p>
        <div class="gr-ecosystem-relations">${relationCards || '<span class="gr-ecosystem-relation"><strong>Research gap</strong><span>This node is present, but no durable edge has been mapped yet.</span></span>'}</div>
        ${visit}`;
    };

    nodes.forEach((node) => {
      node.element.addEventListener('click', () => selectNode(node));
      node.element.addEventListener('keydown', (event) => {
        if (event.key === 'Enter' || event.key === ' ') {
          event.preventDefault();
          selectNode(node);
        }
      });
    });

    filters.forEach((button) => {
      button.addEventListener('click', () => {
        const mode = button.dataset.ecosystemFilter;
        filters.forEach((candidate) => candidate.setAttribute('aria-pressed', String(candidate === button)));
        clearSelection();
        renderInspectorIntro(data);
        if (mode === 'all') return;
        const keepTypes = mode === 'hardware'
          ? new Set(['model', 'lineage'])
          : mode === 'platforms'
            ? new Set(['model', 'operating_platform', 'companion_app', 'sdk_api', 'protocol_transport'])
            : new Set(['model', 'operating_platform', 'sdk_api', 'community_project', 'ai_service']);
        const visibleIds = new Set(nodes.filter((node) => keepTypes.has(node.type)).map((node) => node.id));
        nodes.forEach((node) => node.element.classList.toggle('is-muted', !visibleIds.has(node.id)));
        relations.forEach((rel) => rel.element.classList.toggle('is-muted', !(visibleIds.has(rel.from) && visibleIds.has(rel.to))));
      });
    });
  };

  fetch(endpoint, { credentials: 'same-origin', cache: 'no-store' })
    .then((response) => {
      if (!response.ok) throw new Error(`HTTP ${response.status}`);
      return response.json();
    })
    .then((data) => {
      if (!data || !Array.isArray(data.nodes) || !Array.isArray(data.relations)) throw new Error('Invalid ecosystem graph');
      render(data);
    })
    .catch(() => {
      canvas.innerHTML = '<p class="gr-ecosystem-noscript">The interactive map could not load. The evidence-backed relationship table remains available below.</p>';
      inspector.innerHTML = '<p class="gr-inspector-eyebrow">Map unavailable</p><h3>The research is still here.</h3><p>Use the seeded ecosystem links below while the interactive layer is unavailable.</p>';
    });
})();
