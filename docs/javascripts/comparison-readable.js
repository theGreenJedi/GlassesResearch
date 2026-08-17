(() => {
  const host = document.getElementById('comparison-engine-app');
  if (!host) return;

  const esc = (v) => String(v ?? '').replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;').replaceAll('"','&quot;').replaceAll("'",'&#039;');
  const known = (e) => e && e.evidence !== 'unknown' && e.value !== 'Unknown' && e.value !== null && e.value !== '';
  const val = (r,f) => known(r.fields?.[f]) ? r.fields[f].value : null;
  const fmt = (v) => Array.isArray(v) ? v.join(', ') : typeof v === 'boolean' ? (v ? 'Yes' : 'No') : (v ?? '—');
  const truth = (r,f) => val(r,f) === true;
  const text = (r,f) => String(val(r,f) ?? '').toLowerCase();

  const category = (r) => {
    const hay = `${r.type || ''} ${text(r,'category')}`.toLowerCase();
    if (/enterprise|industrial/.test(hay)) return 'Enterprise';
    if (/sport/.test(hay)) return 'Sport';
    if (/xr|tether|display glasses/.test(hay)) return 'Tethered XR';
    if (/standalone|ar/.test(hay) && /display/.test(hay)) return 'Standalone AR';
    if (/hud|discreet display|display ai|monocular/.test(hay)) return 'HUD / display';
    if (/camera/.test(hay)) return 'Camera AI';
    if (/audio/.test(hay)) return 'Audio AI';
    return 'Other';
  };

  const quickFields = [
    ['category','Type',(r)=>category(r)], ['price_usd','Price'], ['weight_g','Weight'], ['battery_hours','Battery'],
    ['camera_count','Camera'], ['display_type','Display'], ['prescription_support','Prescription'], ['status','Availability']
  ];
  const deepFields = [
    ['owner_control','Owner control'], ['cloud_independence','Cloud independence'], ['sdk','SDK'], ['api','API'],
    ['adb','ADB'], ['firmware','Firmware access'], ['local_storage','Local storage'], ['offline_operation','Offline/local'],
    ['custom_ai','Custom AI'], ['ble','BLE'], ['subscription','Subscription'], ['account_required','Account required']
  ];
  const categoryFields = {
    'Camera AI': [['camera_resolution','Camera'],['video_resolution','Video'],['storage','Storage'],['microphones','Microphones'],['ip_rating','IP rating'],['visual_ai','Visual AI']],
    'Audio AI': [['microphones','Microphones'],['speakers','Speakers'],['calls','Calls'],['translation','Translation'],['transcription','Transcription'],['assistant','Assistant']],
    'HUD / display': [['display_type','Display'],['fov','FOV'],['brightness','Brightness'],['resolution','Resolution'],['translation','Translation'],['navigation','Navigation']],
    'Standalone AR': [['display_type','Display'],['resolution','Resolution'],['fov','FOV'],['os','OS'],['wifi','Wi-Fi'],['sdk','SDK/API']],
    'Tethered XR': [['resolution','Resolution'],['fov','FOV'],['refresh_rate','Refresh'],['brightness','Brightness'],['dof','Tracking'],['host_requirements','Host']],
    'Enterprise': [['display_type','Display'],['camera_resolution','Camera'],['ip_rating','IP rating'],['sdk','SDK/API'],['os','OS'],['weight_g','Weight']],
    'Sport': [['display_type','Display'],['fov','FOV'],['battery_hours','Battery'],['ip_rating','IP rating'],['weight_g','Weight'],['sdk','SDK/API']]
  };

  Promise.all([
    fetch('../../data/comparisons.json',{cache:'no-store'}).then(r=>r.json()),
    fetch('../../data/devices.json',{cache:'no-store'}).then(r=>r.json())
  ]).then(([bundle,devicesBundle]) => {
    const researched = new Map((bundle.records||[]).map(r=>[r.id,r]));
    const records = (devicesBundle.records||[]).map(d => ({...d, fields:{...(researched.get(d.id)?.fields||{})}}));
    const cats = [...new Set(records.map(category))];
    const counts = new Map(cats.map(c=>[c,records.filter(r=>category(r)===c).length]));

    host.innerHTML = `<section class="gr-compare-intro"><h2>Start broad. Go deep only when you need to.</h2><p>Choose a kind of glasses, scan the essentials, then compare the details that actually matter for that category.</p><div class="gr-market-map"><button class="active" data-cat="All">All <b>${records.length}</b></button>${cats.map(c=>`<button data-cat="${esc(c)}">${esc(c)} <b>${counts.get(c)}</b></button>`).join('')}</div></section><section class="gr-quick"><div class="gr-compare-toolbar"><label>Find a model <input type="search" id="gr-q" placeholder="brand or model"></label><label>Compare <select id="gr-a"></select></label><label>with <select id="gr-b"></select></label></div><div id="gr-quick-results"></div></section><section class="gr-focused"><h2>Focused comparison</h2><p id="gr-focus-note"></p><div id="gr-focus"></div><details><summary>GlassesResearch deep research: ownership, openness & evidence</summary><div id="gr-deep"></div></details></section>`;

    let active='All'; const q=host.querySelector('#gr-q'); const out=host.querySelector('#gr-quick-results');
    const a=host.querySelector('#gr-a'), b=host.querySelector('#gr-b');
    const options=()=>records.map(r=>`<option value="${esc(r.id)}">${esc(r.maker)} ${esc(r.model)}</option>`).join(''); a.innerHTML=options(); b.innerHTML=options(); if(records[1]) b.value=records[1].id;

    const cell=(r,f,derive)=> derive ? derive(r) : fmt(val(r,f));
    const quick=()=>{
      const query=q.value.trim().toLowerCase(); const rows=records.filter(r=>(active==='All'||category(r)===active)&&(!query||`${r.maker} ${r.model}`.toLowerCase().includes(query))).slice(0,50);
      out.innerHTML=`<div class="gr-table-wrap"><table class="gr-quick-table"><thead><tr><th>Model</th>${quickFields.map(x=>`<th>${x[1]}</th>`).join('')}</tr></thead><tbody>${rows.map(r=>`<tr><th>${esc(r.maker)} ${esc(r.model)}<small>${esc(r.id)}</small></th>${quickFields.map(([f,l,d])=>`<td>${esc(cell(r,f,d))}</td>`).join('')}</tr>`).join('')}</tbody></table></div><p class="gr-result-count">Showing ${rows.length} of ${records.filter(r=>active==='All'||category(r)===active).length} in this view.</p>`;
    };
    const table=(selected,fields)=>`<div class="gr-table-wrap"><table><thead><tr><th>What matters</th>${selected.map(r=>`<th>${esc(r.maker)} ${esc(r.model)}</th>`).join('')}</tr></thead><tbody>${fields.map(([f,l])=>`<tr><th>${esc(l)}</th>${selected.map(r=>`<td>${esc(fmt(val(r,f)))}</td>`).join('')}</tr>`).join('')}</tbody></table></div>`;
    const focus=()=>{
      const selected=[a.value,b.value].map(id=>records.find(r=>r.id===id)).filter(Boolean); if(selected.length<2)return;
      const shared=category(selected[0])===category(selected[1])?category(selected[0]):'mixed categories';
      host.querySelector('#gr-focus-note').textContent= shared==='mixed categories' ? 'These models belong to different categories, so the focused table shows universal essentials.' : `Showing fields that matter most for ${shared}.`;
      host.querySelector('#gr-focus').innerHTML=table(selected, shared==='mixed categories'?quickFields.map(x=>[x[0],x[1]]):(categoryFields[shared]||quickFields.map(x=>[x[0],x[1]])));
      host.querySelector('#gr-deep').innerHTML=table(selected,deepFields)+`<p class="gr-evidence-note">Unknown stays unknown. Open a model profile or Report Card for provenance, source links, contradictions, and confidence.</p>`;
    };
    host.querySelectorAll('[data-cat]').forEach(btn=>btn.addEventListener('click',()=>{active=btn.dataset.cat;host.querySelectorAll('[data-cat]').forEach(x=>x.classList.toggle('active',x===btn));quick();}));
    q.addEventListener('input',quick); a.addEventListener('change',focus); b.addEventListener('change',focus); quick(); focus();
  }).catch(err=>{host.innerHTML=`<p>Comparison data could not be loaded: ${esc(err.message)}</p>`;});
})();
