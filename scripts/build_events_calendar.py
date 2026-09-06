#!/usr/bin/env python3
from __future__ import annotations
import argparse,json
from datetime import datetime,timedelta
from pathlib import Path

def esc(s:str)->str:
    return str(s).replace('\\','\\\\').replace(';','\\;').replace(',','\\,').replace('\n','\\n')

def date_ics(s:str)->str:
    return datetime.strptime(s,'%Y-%m-%d').strftime('%Y%m%d')

def main()->int:
    ap=argparse.ArgumentParser()
    ap.add_argument('--input',type=Path,default=Path('data/events.json'))
    ap.add_argument('--output',type=Path,default=Path('docs/events.ics'))
    args=ap.parse_args()
    doc=json.loads(args.input.read_text(encoding='utf-8'))
    events=doc.get('events',[])
    required={'id','title','type','start_date','end_date','source_url','verified_on'}
    seen=set()
    lines=['BEGIN:VCALENDAR','VERSION:2.0','PRODID:-//GlassesResearch//Events//EN','CALSCALE:GREGORIAN','METHOD:PUBLISH','X-WR-CALNAME:GlassesResearch Events','X-WR-CALDESC:Verified smart-glasses launches, conferences, research and developer events.']
    for e in events:
        missing=required-set(e)
        if missing: raise SystemExit(f"{e.get('id','event')}: missing {sorted(missing)}")
        if e['id'] in seen: raise SystemExit(f"duplicate event id: {e['id']}")
        seen.add(e['id'])
        start=datetime.strptime(e['start_date'],'%Y-%m-%d')
        end=datetime.strptime(e['end_date'],'%Y-%m-%d')
        if end<start: raise SystemExit(f"{e['id']}: end before start")
        desc=e.get('why_it_matters','')
        if e.get('source_url'): desc=(desc+' Source: '+e['source_url']).strip()
        lines += ['BEGIN:VEVENT',f"UID:{esc(e['id'])}@glassesresearch.org",f"DTSTAMP:{date_ics(e['verified_on'])}T000000Z",f"DTSTART;VALUE=DATE:{date_ics(e['start_date'])}",f"DTEND;VALUE=DATE:{(end+timedelta(days=1)).strftime('%Y%m%d')}",f"SUMMARY:{esc(e['title'])}",f"DESCRIPTION:{esc(desc)}",f"LOCATION:{esc(e.get('location','Online'))}",f"URL:{e['source_url']}",f"CATEGORIES:{esc(e['type'].upper())}",'END:VEVENT']
    lines.append('END:VCALENDAR')
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text('\r\n'.join(lines)+'\r\n',encoding='utf-8')
    print(f"Built {len(events)} events -> {args.output}")
    return 0

if __name__=='__main__': raise SystemExit(main())
