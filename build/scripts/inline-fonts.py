#!/usr/bin/env python3
"""Troca url("fonts/X.woff2") por data URI base64 dentro de um HTML.

Por que: um deck viaja. Sai por e-mail, muda de pasta, abre em máquina que não
tem a pasta fonts/ ao lado. Path relativo quebra e o deck cai no fallback.
Fontes embutidas custam ~264 KB e resolvem isso de uma vez.

Uso: inline-fonts.py <arquivo.html> [pasta-das-fontes]
Idempotente: se já estiver embutido, não faz nada.
"""
import base64, os, re, sys

html = sys.argv[1]
fonts = sys.argv[2] if len(sys.argv) > 2 else os.path.join(os.path.dirname(html), "fonts")
src = open(html, encoding="utf-8").read()

if "data:font/woff2" in src:
    print("já embutido, nada a fazer")
    sys.exit(0)

refs = re.findall(r'url\("(fonts/[^"]+\.woff2)"\)', src)
if not refs:
    print("nenhuma referência relativa a woff2 encontrada")
    sys.exit(1)

antes = len(src)
for ref in sorted(set(refs)):
    path = os.path.join(os.path.dirname(html), ref)
    if not os.path.exists(path):
        print(f"FALTA: {path}")
        sys.exit(1)
    b64 = base64.b64encode(open(path, "rb").read()).decode("ascii")
    src = src.replace(f'url("{ref}")', f'url("data:font/woff2;base64,{b64}")')

open(html, "w", encoding="utf-8").write(src)
print(f"{len(set(refs))} fontes embutidas · {antes//1024} KB -> {len(src)//1024} KB")
