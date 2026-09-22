#!/usr/bin/env python3
import json,pathlib,statistics
from PIL import Image,ImageChops
root=pathlib.Path(".site-image-pilot")
reg=json.loads((root/"data/model-visuals.json").read_text())
rows=[]
for mid,rec in reg["records"].items():
    if not rec.get("original_image"): continue
    p=root/"images/models/presentation"/f"{mid.lower()}.png"
    im=Image.open(p).convert("RGBA")
    a=im.getchannel("A"); ab=a.getbbox()
    rgb=Image.new("RGB",im.size,"white"); rgb.paste(im,mask=a)
    diff=ImageChops.difference(rgb,Image.new("RGB",im.size,"white")).convert("L")
    wb=diff.point(lambda x: 255 if x>18 else 0).getbbox()
    b=ab or wb
    if b:
        w=b[2]-b[0]; h=b[3]-b[1]; occ=(w*h)/(im.width*im.height)
        edge=min(b[0],b[1],im.width-b[2],im.height-b[3])
    else: w=h=0; occ=0; edge=0
    rows.append((mid,w,h,occ,edge,rec.get("state","")))
out=pathlib.Path("research/visual-audits/presentation-geometry-audit.md"); out.parent.mkdir(parents=True,exist_ok=True)
occs=[r[3] for r in rows]
lines=["# Presentation geometry audit","",f"Models measured: **{len(rows)}**.",f"Median occupied canvas area: **{statistics.median(occs):.1%}**.","","| Model | bbox px | area | min edge px | state |","|---|---:|---:|---:|---|"]
for mid,w,h,occ,edge,state in rows: lines.append(f"| {mid} | {w}×{h} | {occ:.1%} | {edge} | {state} |")
out.write_text("\n".join(lines)+"\n")
print(f"Geometry audit: {len(rows)} models")
