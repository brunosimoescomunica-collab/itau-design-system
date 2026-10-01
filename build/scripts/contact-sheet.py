#!/usr/bin/env python3
"""Folha de contato de um PDF: todas as páginas numa imagem só, para ler de uma vez.

Uso: /usr/bin/python3 contact-sheet.py <pdf> <png> [colunas] [largura_celula]
Página suspeita vira uma segunda montagem maior: contact-sheet.py <pdf> <png> 2 700 3,7,12
"""
import sys, fitz

pdf, out = sys.argv[1], sys.argv[2]
cols = int(sys.argv[3]) if len(sys.argv) > 3 else 6
cw = int(sys.argv[4]) if len(sys.argv) > 4 else 300
only = [int(x) - 1 for x in sys.argv[5].split(",")] if len(sys.argv) > 5 else None

src = fitz.open(pdf)
pages = only if only else list(range(len(src)))
p0 = src[0]
ratio = p0.rect.height / p0.rect.width
ch = int(cw * ratio)
gap = 6
rows = (len(pages) + cols - 1) // cols
W = cols * cw + (cols + 1) * gap
H = rows * (ch + 14) + (rows + 1) * gap
doc = fitz.open()
page = doc.new_page(width=W, height=H)
page.draw_rect(page.rect, color=None, fill=(.55, .55, .55))
for k, i in enumerate(pages):
    r, c = divmod(k, cols)
    x = gap + c * (cw + gap)
    y = gap + r * (ch + 14 + gap)
    pix = src[i].get_pixmap(matrix=fitz.Matrix(cw / p0.rect.width, cw / p0.rect.width), alpha=False)
    page.insert_image(fitz.Rect(x, y, x + cw, y + ch), pixmap=pix)
    page.insert_text((x + 2, y + ch + 11), f"{i + 1:02d}", fontsize=9, color=(1, 1, 1))
page.get_pixmap(matrix=fitz.Matrix(1, 1), alpha=False).save(out)
print(f"{len(pages)} páginas · {W}x{H} · {out}")
