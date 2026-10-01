#!/usr/bin/env python3
"""Inverso do inline-fonts.py: troca as data URIs por url("fonts/X.woff2") pra editar o HTML leve."""
import re, sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding="utf-8").read()
MAP = {("Miletus Grotesk",300):"MiletusGrotesk-Light.woff2",("Miletus Grotesk",400):"MiletusGrotesk-Regular.woff2",
       ("Miletus Grotesk",500):"MiletusGrotesk-Medium.woff2",("Miletus Grotesk",700):"MiletusGrotesk-Bold.woff2",
       ("Miletus Grotesk",900):"MiletusGrotesk-Black.woff2",("PP Pangaia",300):"PPPangaia-Light.woff2"}
def rep(m):
    blk = m.group(0)
    fam = re.search(r'font-family:"([^"]+)"', blk).group(1)
    w = int(re.search(r'font-weight:(\d+)', blk).group(1))
    return re.sub(r'url\("data:font/woff2;base64,[A-Za-z0-9+/=]+"\)', f'url("fonts/{MAP[(fam,w)]}")', blk)
out = re.sub(r'@font-face\{.*?\}', rep, s, flags=re.S)
open(dst, "w", encoding="utf-8").write(out)
print(len(s)//1024, "KB ->", len(out)//1024, "KB")
