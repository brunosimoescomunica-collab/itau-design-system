#!/usr/bin/env python3
"""Recorta um PNG por faixa vertical. sips ancora o crop no CENTRO, nao no topo —
este helper usa fitz e recorta pelas coordenadas que a gente pede de verdade."""
import fitz, sys

src, out, y0, y1 = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
scale = float(sys.argv[5]) if len(sys.argv) > 5 else 1.0
d = fitz.open(src)
p = d[0]
r = p.rect
clip = fitz.Rect(0, y0, r.width, min(y1, r.height))
p.get_pixmap(clip=clip, matrix=fitz.Matrix(scale, scale)).save(out)
print(f"{out}: {clip.width:.0f}x{clip.height:.0f} @ {scale} -> {int(clip.width*scale)}x{int(clip.height*scale)}")
