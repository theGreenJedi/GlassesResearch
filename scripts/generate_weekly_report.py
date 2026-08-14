#!/usr/bin/env python3
import base64, json, os, re, sys
from collections import defaultdict
from datetime import date, datetime, timedelta, timezone
from urllib.parse import quote
import requests
import google.auth.transport.requests
from google.oauth2 import service_account

OUT='weekly-report.md'

def req(name):
    v=os.environ.get(name,'')
    if not v:
        raise RuntimeError(f'{name} is not available')
    return v

def cloudflare():
    token=req('CLOUDFLARE_API_TOKEN'); zone=req('CLOUDFLARE_ZONE_ID')
    query='''query Daily($zoneTag: string, $filter: filter) { viewer { zones(filter:{zoneTag:$zoneTag}) { totals:httpRequestsAdaptiveGroups(limit:1,filter:$filter){count sum{visits edgeResponseBytes}} countries:httpRequestsAdaptiveGroups(limit:20,filter:$filter,orderBy:[count_DESC]){count sum{visits} dimensions{clientCountryName}} paths:httpRequestsAdaptiveGroups(limit:100,filter:$filter,orderBy:[count_DESC]){count sum{visits} dimensions{clientRequestPath}} userAgents:httpRequestsAdaptiveGroups(limit:100,filter:$filter,orderBy:[count_DESC]){count sum{visits} dimensions{userAgent}} } } }'''
    headers={'Authorization':f'Bearer {token}','Content-Type':'application/json'}
    now=datetime.now(timezone.utc)
    total_requests=total_visits=0
    countries=defaultdict(lambda:[0,0]); paths=defaultdict(lambda:[0,0])
    bot=re.compile(r'(bot|crawler|spider|slurp|semrush|seranking|ahrefs|bytespider|applebot|googlebot|bingbot|duckduckbot|baiduspider|yandex|facebookexternalhit|petalbot|mj12bot|dotbot)',re.I)
    bots=human=sample=0
    for days_ago in range(7,0,-1):
        start=now-timedelta(days=days_ago); end=start+timedelta(days=1)
        payload={'query':query,'variables':{'zoneTag':zone,'filter':{'datetime_geq':start.strftime('%Y-%m-%dT%H:%M:%SZ'),'datetime_lt':end.strftime('%Y-%m-%dT%H:%M:%SZ'),'requestSource':'eyeball'}}}
        r=requests.post('https://api.cloudflare.com/client/v4/graphql',headers=headers,json=payload,timeout=30); r.raise_for_status()
        data=r.json()
        if data.get('errors'): raise RuntimeError(str(data['errors']))
        z=data['data']['viewer']['zones'][0]; t=(z.get('totals') or [{}])[0]
        total_requests += t.get('count',0); total_visits += t.get('sum',{}).get('visits',0)
        for row in z.get('countries',[]):
            k=row.get('dimensions',{}).get('clientCountryName') or '(unknown)'; countries[k][0]+=row.get('count',0); countries[k][1]+=row.get('sum',{}).get('visits',0)
        for row in z.get('paths',[]):
            k=row.get('dimensions',{}).get('clientRequestPath') or '/'; paths[k][0]+=row.get('count',0); paths[k][1]+=row.get('sum',{}).get('visits',0)
        for row in z.get('userAgents',[]):
            visits=row.get('sum',{}).get('visits',0); sample+=visits
            ua=row.get('dimensions',{}).get('userAgent') or ''
            if bot.search(ua): bots+=visits
            elif visits and ua: human+=visits
    country_rows=[{'dimensions':{'clientCountryName':k},'count':v[0],'sum':{'visits':v[1]}} for k,v in sorted(countries.items(),key=lambda kv:kv[1][0],reverse=True)]
    path_rows=[{'dimensions':{'clientRequestPath':k},'count':v[0],'sum':{'visits':v[1]}} for k,v in sorted(paths.items(),key=lambda kv:kv[1][0],reverse=True)]
    return {'requests':total_requests,'visits':total_visits,'humanish':human,'bots':bots,'outside_sample':max(total_visits-sample,0),'countries':country_rows,'paths':path_rows}

def search_console():
    info=json.loads(req('GOOGLE_SEARCH_CONSOLE_CREDENTIALS')); site=req('GOOGLE_SEARCH_CONSOLE_SITE_URL')
    creds=service_account.Credentials.from_service_account_info(info,scopes=['https://www.googleapis.com/auth/webmasters.readonly']); creds.refresh(google.auth.transport.requests.Request())
    end=date.today()-timedelta(days=2); start=end-timedelta(days=6)
    endpoint='https://searchconsole.googleapis.com/webmasters/v3/sites/'+quote(site,safe='')+'/searchAnalytics/query'
    headers={'Authorization':f'Bearer {creds.token}','Content-Type':'application/json'}
    def query(dimensions,row_limit=50):
        r=requests.post(endpoint,headers=headers,json={'startDate':start.isoformat(),'endDate':end.isoformat(),'dimensions':dimensions,'rowLimit':row_limit,'dataState':'final'},timeout=30); r.raise_for_status(); return r.json().get('rows',[])
    queries=query(['query'],50); pages=query(['page'],25); totals=query([],1); total=totals[0] if totals else {}
    return {'start':start,'end':end,'queries':queries,'pages':pages,'clicks':total.get('clicks',0),'impressions':total.get('impressions',0),'ctr':total.get('ctr',0),'position':total.get('position',0)}

def candidate_key(c):
    if c.get('id'):
        return 'id:'+str(c['id'])
    if c.get('url'):
        return 'url:'+str(c['url']).strip().lower().rstrip('/')
    return 'title:'+re.sub(r'\s+',' ',str(c.get('title','')).strip().lower())

def lane_rank(lane):
    return {'core_glasses':0,'adjacent_hci':1,'research_radar':2}.get(lane,3)

def github_pages(url,headers,params=None,max_pages=10):
    """Read bounded GitHub list pagination instead of silently trusting page one."""
    items=[]; base=dict(params or {})
    per_page=int(base.pop('per_page',100))
    for page in range(1,max_pages+1):
        query={**base,'per_page':per_page,'page':page}
        r=requests.get(url,headers=headers,params=query,timeout=30)
        if not r.ok:
            r.raise_for_status()
        batch=r.json()
        if not isinstance(batch,list):
            raise RuntimeError(f'Expected a GitHub list response from {url}')
        items.extend(batch)
        if len(batch)<per_page:
            break
    return items

def collector():
    repo=os.environ.get('GITHUB_REPOSITORY','')
    headers={'Authorization':f"Bearer {os.environ.get('GH_TOKEN','')}",'Accept':'application/vnd.github+json'}
    cutoff=datetime.now(timezone.utc)-timedelta(days=7)
    prs=[]; branches=[]; raw_candidates=0
    raw_scope_counts=defaultdict(int); source_errors=0
    if not repo:
        return {'prs':prs,'branches':branches,'raw_count':0,'unique_count':0,'repeat_observations':0,'repeated_candidates':0,'raw_scope_counts':{},'unique_scope_counts':{},'source_errors':0,'latest_new':0,'latest_repeat':0,'ranked_candidates':[]}

    r=requests.get(f'https://api.github.com/repos/{repo}/pulls',headers=headers,params={'state':'all','per_page':100,'sort':'updated','direction':'desc'},timeout=30)
    if r.ok:
        for p in r.json():
            updated=datetime.fromisoformat(p['updated_at'].replace('Z','+00:00')); title=p.get('title','')
            if updated>=cutoff and ('Institutional knowledge intake' in title or p.get('head',{}).get('ref','').startswith('knowledge-intake-')):
                prs.append({'number':p['number'],'title':title,'state':p['state'],'branch':p.get('head',{}).get('ref','')})

    try:
        all_branches=github_pages(f'https://api.github.com/repos/{repo}/branches',headers,{'per_page':100})
    except requests.RequestException:
        all_branches=[]
    if all_branches:
        for b in all_branches:
            name=b.get('name','')
            m=re.match(r'^knowledge-intake-(\d{4}-\d{2}-\d{2})-',name)
            if not m: continue
            try:
                intake_date=date.fromisoformat(m.group(1))
            except ValueError:
                continue
            if intake_date < (date.today()-timedelta(days=7)): continue
            branch={'name':name,'date':m.group(1),'candidate_count':None,'scope_counts':{},'source_errors':None,'candidates':[],'new_count':0,'repeat_count':0}
            file_url=f'https://api.github.com/repos/{repo}/contents/research/news-candidates/{m.group(1)}.json'
            fr=requests.get(file_url,headers=headers,params={'ref':name},timeout=30)
            if fr.ok:
                payload=fr.json()
                try:
                    data=json.loads(base64.b64decode(payload.get('content','')).decode('utf-8'))
                    branch['candidate_count']=int(data.get('candidate_count',0))
                    branch['scope_counts']=data.get('scope_counts',{}) or {}
                    branch['source_errors']=len(data.get('collector_errors',[]) or [])
                    branch['candidates']=data.get('candidates',[]) or []
                    raw_candidates += branch['candidate_count']
                    source_errors += branch['source_errors']
                    for k,v in branch['scope_counts'].items(): raw_scope_counts[k]+=int(v)
                except Exception:
                    pass
            branches.append(branch)

    branches.sort(key=lambda b:(b['date'],b['name']))
    latest_name=branches[-1]['name'] if branches else None
    seen=set(); occurrence_counts=defaultdict(int); unique_scope_counts=defaultdict(int); records={}
    for b in branches:
        for c in b['candidates']:
            key=candidate_key(c)
            occurrence_counts[key]+=1
            if key in seen:
                b['repeat_count']+=1
            else:
                seen.add(key); b['new_count']+=1
                lane=c.get('scope_lane') or c.get('source_lane') or 'unknown'
                unique_scope_counts[lane]+=1
            score=int(c.get('materiality_score',0) or 0)
            lane=c.get('scope_lane') or c.get('source_lane') or 'unknown'
            rec=records.get(key)
            if rec is None:
                records[key]={
                    'key':key,'title':c.get('title') or '(untitled)','url':c.get('url') or '',
                    'source':c.get('source') or 'unknown','lane':lane,'materiality_score':score,
                    'publication_eligible':bool(c.get('publication_eligible')),'first_seen':b['name'],
                    'last_seen':b['name'],'occurrences':1,'seen_latest':b['name']==latest_name,
                    'new_latest':b['name']==latest_name
                }
            else:
                rec['last_seen']=b['name']; rec['occurrences']+=1; rec['seen_latest']=rec['seen_latest'] or b['name']==latest_name
                if score>rec['materiality_score']:
                    rec['materiality_score']=score
                if lane_rank(lane)<lane_rank(rec['lane']):
                    rec['lane']=lane
                rec['publication_eligible']=rec['publication_eligible'] or bool(c.get('publication_eligible'))
                if not rec['url'] and c.get('url'): rec['url']=c['url']
                if rec['source']=='unknown' and c.get('source'): rec['source']=c['source']

    ranked=list(records.values())
    ranked.sort(key=lambda c:(-c['materiality_score'],lane_rank(c['lane']),0 if c['new_latest'] else 1,-c['occurrences'],c['title'].lower()))
    unique_count=len(seen)
    repeat_observations=max(raw_candidates-unique_count,0)
    repeated_candidates=sum(1 for n in occurrence_counts.values() if n>1)
    latest=branches[-1] if branches else None
    return {
        'prs':prs,'branches':branches,'raw_count':raw_candidates,'unique_count':unique_count,
        'repeat_observations':repeat_observations,'repeated_candidates':repeated_candidates,
        'raw_scope_counts':dict(raw_scope_counts),'unique_scope_counts':dict(unique_scope_counts),
        'source_errors':source_errors,'latest_new':latest['new_count'] if latest else 0,
        'latest_repeat':latest['repeat_count'] if latest else 0,'latest_name':latest_name,
        'ranked_candidates':ranked
    }

def main():
    cf=cloudflare(); sc=search_console(); co=collector()
    lines=['# GlassesResearch — Weekly Friday Report','',f'Generated: {datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")}','','## 1. Traffic — Cloudflare','',f'- Raw visits, rolling 7 days: **{cf["visits"]}**',f'- Requests: **{cf["requests"]}**',f'- Human-like visits in sampled user agents: **{cf["humanish"]}**',f'- Known crawler visits in sampled user agents: **{cf["bots"]}**',f'- Visits outside sampled UA groups: **{cf["outside_sample"]}**','', '> “Human-like” is a traffic heuristic, not a unique-person count. No client-side identity tracking is added by this report.','','### Top countries','']
    for r in cf['countries'][:10]: lines.append(f'- {r["dimensions"]["clientCountryName"]}: {r["count"]} requests / {r["sum"]["visits"]} visits')
    lines += ['','### Top paths','']
    for r in cf['paths'][:15]: lines.append(f'- `{r["dimensions"]["clientRequestPath"]}` — {r["count"]} requests / {r["sum"]["visits"]} visits')
    lines += ['','## 2. Google Search Console','',f'Final-data window: **{sc["start"]} through {sc["end"]}**',f'- Clicks: **{sc["clicks"]:g}**',f'- Impressions: **{sc["impressions"]:g}**',f'- CTR: **{sc["ctr"]*100:.2f}%**',f'- Average position: **{sc["position"]:.2f}**','','### Search queries','']
    if not sc['queries']: lines.append('- No finalized query rows yet.')
    for r in sc['queries'][:25]: lines.append(f'- **{(r.get("keys") or ["(unknown)"])[0]}** — {r.get("clicks",0):g} clicks, {r.get("impressions",0):g} impressions, {r.get("ctr",0)*100:.2f}% CTR, position {r.get("position",0):.2f}')
    lines += ['','### Search-result pages','']
    if not sc['pages']: lines.append('- No finalized page rows yet.')
    for r in sc['pages'][:15]: lines.append(f'- `{(r.get("keys") or ["(unknown)"])[0]}` — {r.get("clicks",0):g} clicks, {r.get("impressions",0):g} impressions, position {r.get("position",0):.2f}')
    lines += ['','## 3. Research collector — last 7 days','',f'- Intake PRs touched: **{len(co["prs"])}**',f'- Preserved intake branches: **{len(co["branches"])}**',f'- Raw candidate observations: **{co["raw_count"]}**',f'- Unique candidates: **{co["unique_count"]}**',f'- Repeat observations: **{co["repeat_observations"]}**',f'- Candidates seen in more than one intake: **{co["repeated_candidates"]}**']
    if co['latest_name']:
        lines.append(f'- Latest intake: **{co["latest_new"]} new / {co["latest_repeat"]} previously seen** (`{co["latest_name"]}`)')
    if co['raw_scope_counts']:
        lines.append('- Raw scope mix: ' + ', '.join(f'**{k} {v}**' for k,v in sorted(co['raw_scope_counts'].items())))
    if co['unique_scope_counts']:
        lines.append('- Unique scope mix: ' + ', '.join(f'**{k} {v}**' for k,v in sorted(co['unique_scope_counts'].items())))
    lines.append(f'- Collector source errors recorded: **{co["source_errors"]}**')
    lines += ['', '> Candidate identity uses the collector’s stable candidate ID, with normalized URL/title fallbacks. A repeat observation is useful corroboration, not automatically a duplicate to discard.','']
    for p in co['prs'][:20]: lines.append(f'- PR #{p["number"]}: {p["title"]} — {p["state"]}')
    for b in co['branches'][:20]:
        count='unknown' if b['candidate_count'] is None else b['candidate_count']
        mix=', '.join(f'{k}={v}' for k,v in sorted(b['scope_counts'].items())) or 'scope mix unavailable'
        lines.append(f'- `{b["name"]}` — {count} observations; {b["new_count"]} new / {b["repeat_count"]} previously seen ({mix})')

    lines += ['','### Ranked candidate survey — all unique candidates','',
              '> Nothing is hidden from the survey. Ranking uses the collector’s existing materiality score as the primary signal; ties favor core-glasses relevance, then candidates first seen in the latest intake, then repeated sightings as corroboration.','']
    if not co['ranked_candidates']:
        lines.append('- No candidates available.')
    for i,c in enumerate(co['ranked_candidates'],1):
        status='NEW' if c['new_latest'] else ('SEEN AGAIN' if c['occurrences']>1 else 'EARLIER')
        title=str(c['title']).replace('[','\\[').replace(']','\\]')
        linked=f'[{title}]({c["url"]})' if c['url'] else title
        eligibility='public-review eligible' if c['publication_eligible'] else 'research inbox'
        lines.append(f'{i}. **{linked}** — interest **{c["materiality_score"]}** · `{c["lane"]}` · **{status}** · seen {c["occurrences"]}x · {eligibility} · source `{c["source"]}`')

    lines += ['','## 4. Friday review checklist','','- Survey the full ranked candidate list; do not discard lower-ranked items solely because of rank.','- Investigate surprising or high-position search queries.','- Review collector candidates and promote only source-backed material.','- Prioritize new candidates while treating repeat sightings as possible corroboration.','- Note pages gaining impressions but not clicks.','- Check traffic for obvious crawler/scanner inflation before interpreting growth.','- Turn genuine ecosystem gaps into model, lineage, development, timeline, or research work.','']
    open(OUT,'w',encoding='utf-8').write('\n'.join(lines)); print(open(OUT,encoding='utf-8').read())

if __name__=='__main__':
    try: main()
    except Exception as e:
        print(f'Weekly report failed: {e}',file=sys.stderr); raise
