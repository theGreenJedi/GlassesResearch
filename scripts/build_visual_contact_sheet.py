#!/usr/bin/env python3
import json,math,pathlib
from PIL import Image,ImageDraw
root=pathlib.Path(".site-image-pilot")
reg=json.loads((root/"data/model-visuals.json").read_text())
ids=[k for k,v in reg["records"].items() if v.get("original_image")]
tw,th,label,cols=320,210,34,4
rows=math.ceil(len(ids)/cols)
sheet=Image.new("RGB",(cols*tw,rows*(th+label)),"white")
draw=ImageDraw.Draw(sheet)
for i,mid in enumerate(ids):
    p=root/"images/models/presentation"/f"{mid.lower()}.png"
    im=Image.open(p).convert("RGBA")
    im.thumbnail((300,190))
    x=(i%cols)*tw+(tw-im.width)//2
    y=(i//cols)*(th+label)+(th-im.height)//2
    bg=Image.new("RGB",im.size,"white"); bg.paste(im,mask=im.getchannel("A"))
    sheet.paste(bg,(x,y))
    draw.text(((i%cols)*tw+8,(i//cols)*(th+label)+th+7),mid,fill="black")
out=pathlib.Path("research/visual-audits"); out.mkdir(parents=True,exist_ok=True)
sheet.save(out/"presentation-contact-sheet.jpg",quality=88,optimize=True)
print(f"Contact sheet: {len(ids)} models")
