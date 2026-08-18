const CADENCES = new Set(['as_verified','daily','weekly','monthly','annually']);
const TOPICS = new Set(['hacks_development','firmware_software','hardware_teardown','privacy_policy','release_availability','research_science','standards_regulation']);
const ID_RE = /^gr-\d{4}-\d{2}-\d{2}-[a-z0-9][a-z0-9-]*$/;
const encoder = new TextEncoder();

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    if (request.method === 'OPTIONS') return cors(new Response(null,{status:204}), env);
    try {
      if (request.method === 'POST' && url.pathname === '/subscribe') return cors(await subscribe(request, env), env);
      if (request.method === 'GET' && url.pathname === '/confirm') return await confirm(url, env);
      if (request.method === 'GET' && url.pathname === '/manage') return await managePage(url, env);
      if (request.method === 'POST' && url.pathname === '/manage') return await updatePreferences(request, env);
      if (request.method === 'POST' && url.pathname === '/unsubscribe') return await unsubscribe(request, env);
      if (request.method === 'POST' && url.pathname === '/published') return await ingestPublished(request, env, ctx);
      if (request.method === 'GET' && url.pathname === '/delivery-proof') return await deliveryProof(request, url, env);
      if (request.method === 'GET' && url.pathname === '/health') return json({ok:true, service:'verified-research-alerts', canary: Boolean(env.CANARY_TO)});
      return new Response('Not found',{status:404});
    } catch (error) {
      console.error(error);
      return cors(json({ok:false,message:'Subscription service is temporarily unavailable.'},500), env);
    }
  },
  async scheduled(_controller, env, ctx) {
    ctx.waitUntil(deliverDigests(env));
  }
};

function cors(response, env) {
  const h = new Headers(response.headers);
  h.set('Access-Control-Allow-Origin', env.SITE_ORIGIN || 'https://glassesresearch.org');
  h.set('Vary','Origin');
  h.set('Access-Control-Allow-Headers','Content-Type, Authorization');
  h.set('Access-Control-Allow-Methods','GET, POST, OPTIONS');
  return new Response(response.body,{status:response.status,statusText:response.statusText,headers:h});
}
function json(value,status=200){return new Response(JSON.stringify(value),{status,headers:{'content-type':'application/json; charset=utf-8'}})}
function html(value,status=200){return new Response(value,{status,headers:{'content-type':'text/html; charset=utf-8','referrer-policy':'no-referrer'}})}
function now(){return new Date().toISOString()}
function esc(s=''){return String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]))}
function normalizeEmail(v){return String(v||'').trim().toLowerCase()}
function normalizeList(v){return Array.isArray(v)?[...new Set(v.map(x=>String(x).trim()).filter(Boolean))].slice(0,50):[]}
function cleanPrefs(p={}){return {models:normalizeList(p.models),brands_lineages:normalizeList(p.brands_lineages),topics:normalizeList(p.topics).filter(x=>TOPICS.has(x))}}
function randomToken(){const a=new Uint8Array(32);crypto.getRandomValues(a);return btoa(String.fromCharCode(...a)).replaceAll('+','-').replaceAll('/','_').replaceAll('=','')}
async function digest(value){const b=await crypto.subtle.digest('SHA-256',encoder.encode(value));return [...new Uint8Array(b)].map(x=>x.toString(16).padStart(2,'0')).join('')}
async function hmacHex(secret, value){
  const keyMaterial=await crypto.subtle.digest('SHA-256',encoder.encode(`glassesresearch-canary-v1\0${secret}`));
  const key=await crypto.subtle.importKey('raw',keyMaterial,{name:'HMAC',hash:'SHA-256'},false,['sign']);
  const sig=await crypto.subtle.sign('HMAC',key,encoder.encode(value));
  return [...new Uint8Array(sig)].map(x=>x.toString(16).padStart(2,'0')).join('');
}
function publisherAuthorized(request,env){
  const auth=request.headers.get('authorization')||'';
  return Boolean(env.PUBLISH_TOKEN) && auth===`Bearer ${env.PUBLISH_TOKEN}`;
}

async function subscribe(request, env) {
  const p = await request.json();
  const email = normalizeEmail(p.email);
  if (!/^\S+@\S+\.\S+$/.test(email)) return json({ok:false,message:'Enter a valid email address.'},400);
  if (!CADENCES.has(p.cadence)) return json({ok:false,message:'Choose a valid delivery cadence.'},400);
  const include=cleanPrefs(p.include), exclude=cleanPrefs(p.exclude), token=randomToken(), tokenHash=await digest(token), ts=now();
  const old=await env.DB.prepare('SELECT id,status FROM subscribers WHERE email=?').bind(email).first();
  const id=old?.id || crypto.randomUUID();
  await env.DB.prepare(`INSERT INTO subscribers(id,email,status,cadence,include_json,exclude_json,confirm_token_hash,manage_token_hash,created_at,updated_at)
    VALUES(?,?,?,?,?,?,?,?,?,?) ON CONFLICT(email) DO UPDATE SET status='pending',cadence=excluded.cadence,include_json=excluded.include_json,exclude_json=excluded.exclude_json,confirm_token_hash=excluded.confirm_token_hash,updated_at=excluded.updated_at`)
    .bind(id,email,'pending',p.cadence,JSON.stringify(include),JSON.stringify(exclude),tokenHash,null,ts,ts).run();
  const confirmUrl=`${env.PUBLIC_BASE_URL}/confirm?token=${encodeURIComponent(token)}`;
  await sendMail(env,{to:email,subject:'Confirm your GlassesResearch alerts',text:`Confirm your Verified Research Alerts subscription:\n\n${confirmUrl}\n\nIf you did not request this, ignore this email.`,html:`<p>Confirm your <strong>Verified Research Alerts</strong> subscription.</p><p><a href="${esc(confirmUrl)}">Confirm subscription</a></p><p>If you did not request this, ignore this email.</p>`});
  return json({ok:true,message:'Check your email to confirm your subscription.'});
}

async function confirm(url, env) {
  const token=url.searchParams.get('token')||''; if(!token) return html(page('Invalid confirmation','This confirmation link is invalid.'),400);
  const hash=await digest(token); const row=await env.DB.prepare('SELECT id,email FROM subscribers WHERE confirm_token_hash=? AND status=?').bind(hash,'pending').first();
  if(!row) return html(page('Confirmation unavailable','This confirmation link is invalid or has already been used.'),400);
  const manage=randomToken(), manageHash=await digest(manage), ts=now();
  await env.DB.prepare("UPDATE subscribers SET status='active',confirmed_at=?,updated_at=?,confirm_token_hash=NULL,manage_token_hash=? WHERE id=?").bind(ts,ts,manageHash,row.id).run();
  const manageUrl=`${env.PUBLIC_BASE_URL}/manage?token=${encodeURIComponent(manage)}`;
  await sendMail(env,{to:row.email,subject:'GlassesResearch alerts confirmed',text:`Your subscription is active. Manage or unsubscribe here:\n${manageUrl}`,html:`<p>Your Verified Research Alerts subscription is active.</p><p><a href="${esc(manageUrl)}">Manage subscription or unsubscribe</a></p>`});
  return html(page('Subscription confirmed',`<p>Your Verified Research Alerts subscription is active.</p><p><a href="${esc(manageUrl)}">Manage subscription</a> · <a href="${env.SITE_ORIGIN}">Return to GlassesResearch</a></p>`));
}

async function getManagedSubscriber(token, env){if(!token)return null;return env.DB.prepare("SELECT * FROM subscribers WHERE manage_token_hash=? AND status='active'").bind(await digest(token)).first()}
async function managePage(url, env){const token=url.searchParams.get('token')||'';const s=await getManagedSubscriber(token,env);if(!s)return html(page('Management link unavailable','This management link is invalid or no longer active.'),404);const inc=JSON.parse(s.include_json||'{}'),exc=JSON.parse(s.exclude_json||'{}');return html(page('Manage Verified Research Alerts',manageForm(token,s,inc,exc)))}
function topicBoxes(name, values=[]){return [...TOPICS].map(t=>`<label><input type="checkbox" name="${name}" value="${t}" ${values.includes(t)?'checked':''}> ${esc(t.replaceAll('_',' / '))}</label>`).join('')}
function manageForm(token,s,inc,exc){return `<p><strong>${esc(s.email)}</strong></p><form method="post" action="/manage"><input type="hidden" name="token" value="${esc(token)}"><label>Cadence <select name="cadence">${[...CADENCES].map(c=>`<option value="${c}" ${s.cadence===c?'selected':''}>${esc(c.replaceAll('_',' '))}</option>`).join('')}</select></label><fieldset><legend>Follow</legend><label>Models <input name="include_models" value="${esc((inc.models||[]).join(', '))}"></label><label>Brands / lineages <input name="include_brands" value="${esc((inc.brands_lineages||[]).join(', '))}"></label>${topicBoxes('include_topics',inc.topics)}</fieldset><fieldset><legend>Exclude</legend><label>Models <input name="exclude_models" value="${esc((exc.models||[]).join(', '))}"></label><label>Brands / lineages <input name="exclude_brands" value="${esc((exc.brands_lineages||[]).join(', '))}"></label>${topicBoxes('exclude_topics',exc.topics)}</fieldset><button>Save preferences</button></form><form method="post" action="/unsubscribe" style="margin-top:2rem"><input type="hidden" name="token" value="${esc(token)}"><button>Unsubscribe completely</button></form>`}
async function readForm(request){const f=await request.formData();return f}
async function updatePreferences(request,env){const f=await readForm(request),token=String(f.get('token')||''),s=await getManagedSubscriber(token,env);if(!s)return html(page('Management link unavailable','This management link is invalid or no longer active.'),404);const cadence=String(f.get('cadence')||'');if(!CADENCES.has(cadence))return html(page('Invalid cadence','Choose a valid cadence.'),400);const split=v=>String(v||'').split(',').map(x=>x.trim()).filter(Boolean).slice(0,50);const include={models:split(f.get('include_models')),brands_lineages:split(f.get('include_brands')),topics:f.getAll('include_topics').filter(x=>TOPICS.has(x))};const exclude={models:split(f.get('exclude_models')),brands_lineages:split(f.get('exclude_brands')),topics:f.getAll('exclude_topics').filter(x=>TOPICS.has(x))};await env.DB.prepare('UPDATE subscribers SET cadence=?,include_json=?,exclude_json=?,updated_at=? WHERE id=?').bind(cadence,JSON.stringify(include),JSON.stringify(exclude),now(),s.id).run();return html(page('Preferences saved',`<p>Your subscription preferences were updated.</p><p><a href="/manage?token=${encodeURIComponent(token)}">Return to management</a></p>`))}
async function unsubscribe(request,env){const f=await readForm(request),token=String(f.get('token')||''),s=await getManagedSubscriber(token,env);if(!s)return html(page('Already unsubscribed','This subscription is already inactive or the link is invalid.'));await env.DB.prepare("UPDATE subscribers SET status='suppressed',include_json='{}',exclude_json='{}',manage_token_hash=NULL,updated_at=? WHERE id=?").bind(now(),s.id).run();return html(page('Unsubscribed','Your address has been suppressed from future GlassesResearch alert mailings.'))}

async function ingestPublished(request,env,ctx){
  if(!publisherAuthorized(request,env)) return json({ok:false},401);
  const p=await request.json();
  if(!p.id||!ID_RE.test(String(p.id))||!p.title||!p.canonical_url||!String(p.canonical_url).startsWith(env.SITE_ORIGIN)) return json({ok:false,message:'Invalid publication payload.'},400);
  const item={id:String(p.id),title:String(p.title),canonical_url:String(p.canonical_url),summary:String(p.summary||''),models:normalizeList(p.models),brands:normalizeList(p.brands_lineages||p.brands),topics:normalizeList(p.topics).filter(x=>TOPICS.has(x)),published_at:p.published_at||now()};
  await env.DB.prepare(`INSERT INTO published_items(id,title,canonical_url,summary,models_json,brands_json,topics_json,published_at,created_at) VALUES(?,?,?,?,?,?,?,?,?) ON CONFLICT(id) DO UPDATE SET title=excluded.title,canonical_url=excluded.canonical_url,summary=excluded.summary,models_json=excluded.models_json,brands_json=excluded.brands_json,topics_json=excluded.topics_json,published_at=excluded.published_at`).bind(item.id,item.title,item.canonical_url,item.summary,JSON.stringify(item.models),JSON.stringify(item.brands),JSON.stringify(item.topics),item.published_at,now()).run();
  ctx.waitUntil(Promise.allSettled([deliverAsVerified(item,env),deliverCanary(item,env)]));
  return json({ok:true});
}

async function deliveryProof(request,url,env){
  if(!publisherAuthorized(request,env)) return json({ok:false},401);
  const id=String(url.searchParams.get('publication_id')||'');
  if(!ID_RE.test(id)) return json({ok:false,message:'Invalid publication ID.'},400);
  const dispatch=await env.DB.prepare('SELECT attempted_at,provider_accepted_at,provider_message_id,last_error FROM canary_dispatches WHERE publication_id=?').bind(id).first();
  const receipt=await env.DB.prepare('SELECT received_at,received_message_id FROM canary_receipts WHERE publication_id=?').bind(id).first();
  return json({
    ok:true,
    publication_id:id,
    dispatch_attempted:Boolean(dispatch?.attempted_at),
    provider_accepted:Boolean(dispatch?.provider_accepted_at),
    provider_message_id:dispatch?.provider_message_id||null,
    received:Boolean(receipt?.received_at),
    received_at:receipt?.received_at||null,
    received_message_id:receipt?.received_message_id||null,
    last_error:dispatch?.last_error||null
  });
}

function lowerSet(v=[]){return new Set(v.map(x=>String(x).toLowerCase()))}
function intersects(a,b){for(const x of a)if(b.has(x))return true;return false}
function eligible(s,item){const inc=JSON.parse(s.include_json||'{}'),exc=JSON.parse(s.exclude_json||'{}');const im=lowerSet(item.models),ib=lowerSet(item.brands),it=lowerSet(item.topics);if(intersects(lowerSet(exc.models),im)||intersects(lowerSet(exc.brands_lineages),ib)||intersects(lowerSet(exc.topics),it))return false;const hasInclude=(inc.models?.length||0)+(inc.brands_lineages?.length||0)+(inc.topics?.length||0)>0;if(!hasInclude)return true;return intersects(lowerSet(inc.models),im)||intersects(lowerSet(inc.brands_lineages),ib)||intersects(lowerSet(inc.topics),it)}
async function activeByCadence(env,cadence){return (await env.DB.prepare("SELECT * FROM subscribers WHERE status='active' AND cadence=?").bind(cadence).all()).results||[]}
async function deliverAsVerified(item,env){for(const s of await activeByCadence(env,'as_verified')){if(!eligible(s,item))continue;const sent=await env.DB.prepare('SELECT 1 FROM deliveries WHERE subscriber_id=? AND publication_id=?').bind(s.id,item.id).first();if(sent)continue;await sendResearch(env,s,[item]);await recordDelivery(env,s,[item]);}}
function due(cadence,last){if(!last)return true;const age=Date.now()-Date.parse(last);return age>=({daily:864e5,weekly:7*864e5,monthly:28*864e5,annually:365*864e5}[cadence]||Infinity)}
async function deliverDigests(env){const all=(await env.DB.prepare("SELECT * FROM subscribers WHERE status='active' AND cadence!='as_verified'").all()).results||[];for(const s of all){if(!due(s.cadence,s.last_sent_at))continue;const since=s.last_sent_at||s.confirmed_at||s.created_at;const rows=(await env.DB.prepare('SELECT * FROM published_items WHERE published_at>? ORDER BY published_at ASC').bind(since).all()).results||[];const items=rows.map(r=>({...r,models:JSON.parse(r.models_json||'[]'),brands:JSON.parse(r.brands_json||'[]'),topics:JSON.parse(r.topics_json||'[]')})).filter(i=>eligible(s,i));if(!items.length)continue;await sendResearch(env,s,items);await recordDelivery(env,s,items)}}
async function recordDelivery(env,s,items){const ts=now();for(const i of items)await env.DB.prepare('INSERT OR IGNORE INTO deliveries(subscriber_id,publication_id,delivered_at) VALUES(?,?,?)').bind(s.id,i.id,ts).run();await env.DB.prepare('UPDATE subscribers SET last_sent_at=?,updated_at=? WHERE id=?').bind(ts,ts,s.id).run()}
async function sendResearch(env,s,items){const manage=randomToken(),manageHash=await digest(manage);await env.DB.prepare('UPDATE subscribers SET manage_token_hash=?,updated_at=? WHERE id=?').bind(manageHash,now(),s.id).run();const manageUrl=`${env.PUBLIC_BASE_URL}/manage?token=${encodeURIComponent(manage)}`;const subject=items.length===1?`GlassesResearch: ${items[0].title}`:`GlassesResearch: ${items.length} verified updates`;const lines=items.map(i=>`${i.title}\n${i.summary}\n${i.canonical_url}`).join('\n\n');const cards=items.map(i=>`<h3><a href="${esc(i.canonical_url)}">${esc(i.title)}</a></h3><p>${esc(i.summary)}</p>`).join('');await sendMail(env,{to:s.email,subject,text:`${lines}\n\nManage subscription / unsubscribe: ${manageUrl}`,html:`${cards}<hr><p><a href="${esc(manageUrl)}">Manage subscription / unsubscribe</a></p>`,headers:{'List-Unsubscribe':`<${manageUrl}>`}})}

async function deliverCanary(item,env){
  if(!env.CANARY_TO) throw new Error('CANARY_TO is not configured');
  if(!env.PUBLISH_TOKEN) throw new Error('PUBLISH_TOKEN is not configured for canary signing');
  const existing=await env.DB.prepare('SELECT received_at FROM canary_receipts WHERE publication_id=?').bind(item.id).first();
  if(existing?.received_at) return;
  const sentAt=now();
  const signature=await hmacHex(env.PUBLISH_TOKEN,`${item.id}\n${sentAt}`);
  await env.DB.prepare(`INSERT INTO canary_dispatches(publication_id,attempted_at,provider_accepted_at,provider_message_id,last_error)
    VALUES(?,?,?,?,?) ON CONFLICT(publication_id) DO UPDATE SET attempted_at=excluded.attempted_at,last_error=NULL`)
    .bind(item.id,sentAt,null,null,null).run();
  try{
    const result=await sendMail(env,{
      to:env.CANARY_TO,
      subject:`GlassesResearch canary: ${item.id}`,
      text:`Synthetic delivery witness for ${item.id}.\n${item.canonical_url}`,
      html:`<p>Synthetic delivery witness for <strong>${esc(item.id)}</strong>.</p><p><a href="${esc(item.canonical_url)}">Canonical publication</a></p>`,
      headers:{
        'X-GlassesResearch-Publication-Id':item.id,
        'X-GlassesResearch-Canary-Sent-At':sentAt,
        'X-GlassesResearch-Canary-Signature':signature
      }
    });
    await env.DB.prepare('UPDATE canary_dispatches SET provider_accepted_at=?,provider_message_id=?,last_error=NULL WHERE publication_id=?')
      .bind(now(),String(result?.id||''),item.id).run();
  }catch(error){
    const message=String(error?.message||error).slice(0,500);
    await env.DB.prepare('UPDATE canary_dispatches SET last_error=? WHERE publication_id=?').bind(message,item.id).run();
    throw error;
  }
}

async function sendMail(env,message){
  if(!env.RESEND_API_KEY)throw new Error('RESEND_API_KEY is not configured');
  const body={from:env.MAIL_FROM,to:[message.to],subject:message.subject,text:message.text,html:message.html,headers:message.headers||{}};
  const r=await fetch('https://api.resend.com/emails',{method:'POST',headers:{authorization:`Bearer ${env.RESEND_API_KEY}`,'content-type':'application/json'},body:JSON.stringify(body)});
  const raw=await r.text();
  if(!r.ok)throw new Error(`Mail provider returned ${r.status}: ${raw}`);
  try{return JSON.parse(raw||'{}')}catch{return {}}
}
function page(title,body){return `<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>${esc(title)} · GlassesResearch</title><style>body{font:16px/1.55 system-ui;margin:0;background:#f6f8f7;color:#10211f}main{max-width:46rem;margin:8vh auto;padding:1.5rem}form,fieldset{display:grid;gap:.65rem}fieldset{margin:1rem 0;padding:1rem;border:1px solid #ccd7d3;border-radius:.7rem}input,select,button{font:inherit;padding:.65rem}button{cursor:pointer}a{color:#236e64}</style></head><body><main><h1>${esc(title)}</h1>${body}</main></body></html>`}
