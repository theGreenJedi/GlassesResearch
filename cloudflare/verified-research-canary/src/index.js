const encoder = new TextEncoder();
const ID_RE = /^gr-\d{4}-\d{2}-\d{2}-[a-z0-9][a-z0-9-]*$/;

export default {
  async email(message, env) {
    if (!env.PUBLISH_TOKEN) throw new Error('PUBLISH_TOKEN is not configured');
    if (!env.CANARY_ADDRESS) throw new Error('CANARY_ADDRESS is not configured');
    if (String(message.to||'').toLowerCase() !== env.CANARY_ADDRESS.toLowerCase()) {
      message.setReject('Unknown canary recipient');
      return;
    }

    const id=String(message.headers.get('X-GlassesResearch-Publication-Id')||'');
    const sentAt=String(message.headers.get('X-GlassesResearch-Canary-Sent-At')||'');
    const supplied=String(message.headers.get('X-GlassesResearch-Canary-Signature')||'').toLowerCase();
    if(!ID_RE.test(id) || !sentAt || !/^[a-f0-9]{64}$/.test(supplied)) {
      message.setReject('Invalid canary envelope');
      return;
    }

    const sentMillis=Date.parse(sentAt);
    if(!Number.isFinite(sentMillis) || sentMillis > Date.now()+10*60*1000 || sentMillis < Date.now()-48*60*60*1000) {
      message.setReject('Stale canary envelope');
      return;
    }

    const expected=await hmacHex(env.PUBLISH_TOKEN,`${id}\n${sentAt}`);
    if(!constantTimeEqual(expected,supplied)) {
      message.setReject('Invalid canary signature');
      return;
    }

    const receivedAt=new Date().toISOString();
    const messageId=String(message.headers.get('Message-ID')||'').slice(0,255);
    await env.DB.prepare(`INSERT INTO canary_receipts(publication_id,received_at,received_message_id)
      VALUES(?,?,?) ON CONFLICT(publication_id) DO UPDATE SET received_at=excluded.received_at,received_message_id=excluded.received_message_id`)
      .bind(id,receivedAt,messageId).run();
    console.log(`Verified alert canary receipt: ${id}`);
  }
};

async function hmacHex(secret, value){
  const keyMaterial=await crypto.subtle.digest('SHA-256',encoder.encode(`glassesresearch-canary-v1\0${secret}`));
  const key=await crypto.subtle.importKey('raw',keyMaterial,{name:'HMAC',hash:'SHA-256'},false,['sign']);
  const sig=await crypto.subtle.sign('HMAC',key,encoder.encode(value));
  return [...new Uint8Array(sig)].map(x=>x.toString(16).padStart(2,'0')).join('');
}

function constantTimeEqual(a,b){
  if(a.length!==b.length)return false;
  let diff=0;
  for(let i=0;i<a.length;i++)diff|=a.charCodeAt(i)^b.charCodeAt(i);
  return diff===0;
}
