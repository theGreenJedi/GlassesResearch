#!/usr/bin/env python3
"""Build normalized publication derivatives for governed model imagery."""
from __future__ import annotations
import argparse, json
from pathlib import Path
from PIL import ImageChops
CANVAS=(1600,900)
MAX_BOX=(1320,650)
NORMALIZATION="centered-object-1600x900-v3"
def main():
    p=argparse.ArgumentParser()
    p.add_argument("--registry",type=Path,required=True)
    p.add_argument("--root",type=Path,required=True)
    p.add_argument("--output-root",type=Path)
    p.add_argument("--write-registry",action="store_true")
    a=p.parse_args()
    try:
        from PIL import Image
    except ImportError as exc:
        raise SystemExit("Pillow is required to normalize model imagery") from exc
    data=json.loads(a.registry.read_text(encoding="utf-8"))
    made=0
    for model_id,record in data.get("records",{}).items():
        original=str(record.get("original_image","")).strip()
        if not original:
            continue
        src=a.root/original.lstrip("/")
        if not src.exists():
            raise SystemExit(f"{model_id}: original_image missing: {original}")
        out_rel=f"images/models/presentation/{model_id.lower()}.png"
        output_root=a.output_root or a.root
        out=output_root/out_rel
        out.parent.mkdir(parents=True,exist_ok=True)
        with Image.open(src) as im:
            im=im.convert("RGBA")
            alpha=im.getchannel("A")
            bbox=alpha.getbbox()
            if bbox:
                im=im.crop(bbox)
            rgb=Image.new("RGB",im.size,"white")
            rgb.paste(im,mask=im.getchannel("A"))
            corners=[rgb.getpixel((0,0)),rgb.getpixel((rgb.width-1,0)),rgb.getpixel((0,rgb.height-1)),rgb.getpixel((rgb.width-1,rgb.height-1))]
            if all(min(c)>235 for c in corners):
                diff=ImageChops.difference(rgb,Image.new("RGB",rgb.size,"white")).convert("L")
                fg=diff.point(lambda x: 255 if x>18 else 0).getbbox()
                if fg:
                    pad=max(8,int(max(rgb.size)*0.02))
                    fg=(max(0,fg[0]-pad),max(0,fg[1]-pad),min(im.width,fg[2]+pad),min(im.height,fg[3]+pad))
                    im=im.crop(fg)
            scale=min(MAX_BOX[0]/im.width,MAX_BOX[1]/im.height)
            size=(max(1,round(im.width*scale)),max(1,round(im.height*scale)))
            if size != im.size:
                im=im.resize(size,Image.Resampling.LANCZOS)
            canvas=Image.new("RGBA",CANVAS,(0,0,0,0))
            x=(CANVAS[0]-im.width)//2
            y=(CANVAS[1]-im.height)//2
            canvas.alpha_composite(im,(x,y))
            canvas.save(out,optimize=True)
        record["primary_image"]="/"+out_rel
        record["normalization"]=NORMALIZATION
        made+=1
    if a.write_registry and made:
        a.registry.write_text(json.dumps(data,indent=2)+"\n",encoding="utf-8")
    if a.output_root and made:
        staged=a.output_root/"data/model-visuals.json"
        staged.parent.mkdir(parents=True,exist_ok=True)
        staged.write_text(json.dumps(data,indent=2)+"\n",encoding="utf-8")
    print(f"Normalized {made} model presentation images")
if __name__=="__main__":
    main()
