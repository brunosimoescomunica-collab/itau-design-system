#!/usr/bin/env python3
"""Monta o template de slides Itaú × Africa a partir das partes editáveis.

Por que existe: o template entregue carrega as fontes em base64 (um deck viaja
por e-mail e muda de pasta) e dois SVGs longos (a pedra e o logo do Itaú). Editar
isso à mão é penoso. As partes moram em src/, o script injeta os SVGs, escreve a
cópia leve (fontes por caminho relativo) e a cópia entregue (fontes embutidas).

Uso: build-itau.py            -> escreve src/itau-slides-template.light.html
                                 e Clientes/Itaú/Master Slides/itau-slides-template.html
"""
import base64, json, math, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import itau_components as IC  # noqa: E402  os componentes vivos (a Moldura, a anatomia, as órbitas, o poema, o ecossistema)

HERE = os.path.dirname(os.path.abspath(__file__))
P16 = os.path.dirname(HERE)
WS = os.path.dirname(os.path.dirname(P16))
SRC = os.path.join(P16, "src")
DS = os.path.join(WS, "Clientes", "Itaú", "Design System")
MS = os.path.join(WS, "Clientes", "Itaú", "Master Slides")
FONTS = os.path.join(DS, "fonts")

N = 4.3  # expoente da superelipse, medido no vetor do logo (rmse 14px em 1233)


def superellipse(scale, npts=360, prec=3):
    pts = []
    for i in range(npts):
        t = 2 * math.pi * i / npts
        c, s = math.cos(t), math.sin(t)
        x = scale / 2 + (scale / 2) * math.copysign(abs(c) ** (2 / N), c)
        y = scale / 2 + (scale / 2) * math.copysign(abs(s) ** (2 / N), s)
        p = (round(x, prec), round(y, prec))
        if not pts or pts[-1] != p:
            pts.append(p)
    return "M" + " L".join(f"{x:g},{y:g}" for x, y in pts) + "Z"


def itau_symbol():
    svg = open(os.path.join(DS, "assets", "itau-logo-2023-commons.svg"), encoding="utf-8").read()
    paths = re.findall(r'<path[^>]*d="([^"]+)"', svg)
    if len(paths) != 2:
        sys.exit(f"logo: esperava 2 paths, achou {len(paths)}")
    return ('<symbol id="itau" viewBox="0 0 500 500">'
            + "".join(f'<path fill="currentColor" d="{d}"/>' for d in paths)
            + "</symbol>")


def inline_fonts(html):
    def rep(m):
        ref = m.group(1)
        path = os.path.join(FONTS, os.path.basename(ref))
        if not os.path.exists(path):
            sys.exit(f"FALTA fonte: {path}")
        b64 = base64.b64encode(open(path, "rb").read()).decode("ascii")
        return f'url("data:font/woff2;base64,{b64}")'
    return re.sub(r'url\("(fonts/[^"]+\.woff2)"\)', rep, html)


# o catálogo dos componentes de 17/09: texto de exemplo que nomeia o estilo (o método da GUT), forma do módulo
MOV = [("Movimento 01", "Função curta."), ("Movimento 02", "Função curta."), ("Movimento 03", "Função curta."),
       ("Movimento 04", "Função um pouco mais longa."), ("Movimento 05", "Função curta.")]
CAM = ("Camada transversal", "Legenda da camada, em uma linha.")
SINAIS = ["sinal um", "sinal dois", "sinal três", "sinal quatro"]
ASSUNTOS = ["tema um", "tema dois", "tema três", "tema quatro", "tema cinco", "tema seis", "tema sete"]
TABELA = [("Legenda", "Corpo pequeno lorem ipsum."), ("Legenda", "Corpo pequeno lorem ipsum dolor."),
          ("Legenda", "Corpo pequeno lorem ipsum dolor sit."), ("Legenda", "Corpo pequeno lorem ipsum.")]
FIOS = [("Canal um", "Faz lorem."), ("Canal dois", "Faz ipsum."), ("Canal três", "Faz dolor."),
        ("Canal quatro e cinco", "Fazem sit amet."), ("Canal seis", "Faz consectetur elit.")]
POEMA = dict(screen=["Título do poema", "em duas linhas"],
             estrofes=[["Estrofe lorem ipsum", "dolor sit amet,", "consectetur elit."], ["Segunda estrofe,", "em duas linhas."]],
             litania=["Linha!", "Linha", "Linha!", "Linha!", "Linha (“aparte”)", "Linha!", "Linha!", "Linha", "Linha!", "Linha!"],
             veredito=["Zero de lorem.", "Zero de ipsum."],
             prosa=["{Linha fina com o grifo}.", "Linha fina lorem ipsum dolor."])


def camada_css():
    css = open(os.path.join(SRC, "04-camada.css"), encoding="utf-8").read()
    return css.replace("{{ANATOMIA_CSS}}", IC.anatomy_css().strip())


def catalogo():
    return {
        "ANATOMIA": IC.anatomy(),
        "MOLDURA": IC.resonance(1.0),
        "MOLDURA_ABERTA": IC.resonance(1.12),
        "ORBITAS": IC.orbita(SINAIS, ASSUNTOS, "ID"),
        "POEMA": IC.poema(**POEMA),
        "ECO_NASCE": IC.ecossistema("cat-nasce", MOV),
        "ECO_MOMENTO": IC.ecossistema("cat-momento", MOV, lit=1),
        "ECO_CAMADA": IC.ecossistema("cat-camada", MOV, lit=len(IC.ECO_R), social=True),
        "ECO_SA_BRILHA": IC.eco_sa(True, CAM),
        "ECO_SA": IC.eco_sa(False, CAM),
        "TABELA": IC.rows_html(TABELA, 1.2, .18),
        "TABELA_FIOS": IC.amb_rows(FIOS),
    }


def main():
    parts = [open(os.path.join(SRC, f), encoding="utf-8").read()
             for f in ["01-head.html", "02-body.html", "03-tail.html"]]
    html = "".join(parts)
    html = html.replace("{{PEDRA_100}}", superellipse(100, 360, 2))
    html = html.replace("{{PEDRA_UNIT}}", superellipse(1, 360, 4))
    html = html.replace("{{ITAU_SYMBOL}}", itau_symbol())
    n_slides = len(re.findall(r'<section class="slide', parts[1]))
    html = html.replace("{{TOTAL}}", f"{n_slides:02d}")
    html = html.replace("{{CAMADA_CSS}}", camada_css())
    for k, v in catalogo().items():
        html = html.replace("{{" + k + "}}", v)
    left = re.findall(r"\{\{[A-Z_]+\}\}", html)
    if left:
        sys.exit(f"placeholder sem valor: {left}")

    light = os.path.join(SRC, "itau-slides-template.light.html")
    open(light, "w", encoding="utf-8").write(html)
    full = inline_fonts(html)
    os.makedirs(MS, exist_ok=True)
    out = os.path.join(MS, "itau-slides-template.html")
    open(out, "w", encoding="utf-8").write(full)
    print(f"{n_slides} slides · leve {len(html)//1024} KB · entregue {len(full)//1024} KB")
    print(out)

    # o design system e o brand book carregam os mesmos SVGs longos; a injeção
    # acontece no lugar, uma vez só (sem placeholder, nada muda)
    for name in ["itau-design-system.html", "itau-brand-book-a4.html"]:
        p = os.path.join(DS, name)
        if not os.path.exists(p):
            continue
        s = open(p, encoding="utf-8").read()
        if "{{" not in s:
            continue
        s = (s.replace("{{PEDRA_100}}", superellipse(100, 360, 2))
              .replace("{{PEDRA_UNIT}}", superellipse(1, 360, 4))
              .replace("{{ITAU_SYMBOL}}", itau_symbol()))
        open(p, "w", encoding="utf-8").write(s)
        print(f"{name}: pedra e logo injetados · {len(s)//1024} KB")


if __name__ == "__main__":
    main()
