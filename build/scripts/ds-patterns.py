#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Os quadros vivos do design system (seção 09, Padrões animados) e os usos novos da pedra (seção 05).

Por que existe: o one-pager mostra os componentes de 17/09 como o próprio slide do catálogo, em
miniatura e animando. Escrever isso à mão duplicaria os SVGs longos e o CSS da camada. Aqui os SVGs
vêm do mesmo módulo que alimenta o template (itau_components.py), os textos de exemplo vêm do
build-itau.py (o catálogo) e o CSS é o do template, escopado a .pat: o subconjunto do CSS de sistema
que os quadros usam (extraído de src/01-head.html) e a camada de movimento inteira (src/04-camada.css,
com o keyframe do morph gerado pelo módulo).

Idempotente: roda de novo, substitui o miolo entre os três pares de marcadores no HTML:
  <!-- DS-PAT-CSS:BEGIN --> ... <!-- DS-PAT-CSS:END -->        o <style> escopado, no head
  <!-- DS-PEDRA-USOS:BEGIN --> ... <!-- DS-PEDRA-USOS:END -->  os três cards da pedra (seção 05)
  <!-- DS-PATTERNS:BEGIN --> ... <!-- DS-PATTERNS:END -->      os oito quadros (seção 09)

Uso: ds-patterns.py   -> reescreve Clientes/Itaú/Design System/itau-design-system.html
"""
import html as H
import importlib.util
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
P16 = os.path.dirname(HERE)
WS = os.path.dirname(os.path.dirname(P16))
SRC = os.path.join(P16, "src")
DS_HTML = os.path.join(WS, "Clientes", "Itaú", "Design System", "itau-design-system.html")

sys.path.insert(0, HERE)
import itau_components as IC  # noqa: E402

_spec = importlib.util.spec_from_file_location("build_itau", os.path.join(HERE, "build-itau.py"))
BI = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(BI)   # só define funções e o catálogo; o main fica atrás do guard


# ================================================================ CSS
def rules(css):
    """Divide um CSS em (seletor, corpo) no nível de cima; blocos @ vêm inteiros como corpo."""
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    out, buf, depth, start = [], "", 0, 0
    i = 0
    while i < len(css):
        c = css[i]
        if c == "{":
            if depth == 0:
                sel, start = buf.strip(), i + 1
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                out.append((sel, css[start:i]))
                buf = ""
        elif depth == 0:
            buf += c
        i += 1
    return out


def scope(css, prefix=".pat "):
    """Prefixa todo seletor com .pat; dentro de @keyframes nada muda; dentro de @media os seletores
    também levam o prefixo. O texto das declarações passa intacto."""
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    out, buf, stack = [], "", []
    for c in css:
        if c == "{":
            sel = buf.strip()
            buf = ""
            if sel.startswith("@keyframes"):
                stack.append("kf")
                out.append(sel + "{")
            elif sel.startswith("@"):
                stack.append("at")
                out.append(sel + "{")
            else:
                stack.append("rule")
                if "kf" in stack:
                    out.append(sel + "{")
                else:
                    out.append(",".join(prefix + p.strip() for p in sel.split(",")) + "{")
        elif c == "}":
            out.append(buf.strip())
            buf = ""
            stack.pop()
            out.append("}\n" if not stack else "}")
        else:
            buf += c
    return "".join(out)


# o que os quadros usam do CSS de sistema do template: slide, quadro, canvas, superfícies, estilos de texto, o grifo, a pedra
SYSTEM_SELECTORS = [
    ".slide", ".frame", ".slide.inv", ".slide.laranja", ".slide.azul",
    ".canvas", ".slide.top .canvas", ".slide.bare .canvas", ".slide.ctr .canvas",
    ".stmt", ".ttl", ".sub", ".body-l", ".body", ".body-s", ".cap", ".med", ".mut",
    ".hl", ".hl::before", ".hl::after", ".slide.visible .hl::before", ".slide.visible .hl::after", ".pd",
]

# os tokens do template que o CSS acima lê (src/01-head.html, :root), na unidade do quadro
PAT_TOKENS = """.pat{container-type:inline-size;position:relative;overflow:hidden;background:var(--bg);color:var(--fg);font-family:var(--text);font-weight:400;line-height:1.5;
  --m:5.2cqw;--col:6cqw;--gutter:1.6cqw;--field:4cqw;--u:.8cqw;--r:.8cqw;--r-s:.4cqw;--r-l:1.25cqw;
  --t-hero:9.4cqw;--t-stmt:8cqw;--t-ttl:5.6cqw;--t-sub:2.6cqw;--t-body-l:2.3cqw;--t-body:1.75cqw;--t-body-s:1.35cqw;--t-cap:1cqw;--t-num:15cqw;--t-num-m:7cqw;
  --e-expo:cubic-bezier(.19,1,.22,1);--e-strong:cubic-bezier(.87,0,.13,1);--e-slow:cubic-bezier(.16,1,.3,1);
  --hair:rgba(0,0,0,.16);--stage:#F1F2F4;--ink:rgba(0,0,0,.06);--acc:#FF6200;--acc-fg:#FFFFFF}
html[data-mode="dark"] .pat{--hair:rgba(255,255,255,.24);--stage:rgba(255,255,255,.06);--ink:rgba(255,255,255,.08)}
"""
# o quadro em miniatura: o slide deixa de ocupar a tela e vira um bloco 16:9 da largura do card
PAT_OVERRIDES = """.pat .slide{height:auto;width:100%;display:block;padding:0;position:relative;overflow:hidden;scroll-snap-align:none;background:var(--bg);color:var(--fg)}
.pat .frame{width:100%;aspect-ratio:16/9}
"""


def system_css():
    head = open(os.path.join(SRC, "01-head.html"), encoding="utf-8").read()
    css = re.search(r"<style>(.*?)</style>", head, re.S).group(1)
    wanted = {s: None for s in SYSTEM_SELECTORS}
    for sel, body in rules(css):
        key = re.sub(r"\s+", " ", sel)
        if key in wanted and wanted[key] is None:
            wanted[key] = body.strip()
    missing = [k for k, v in wanted.items() if v is None]
    if missing:
        sys.exit(f"seletor de sistema não achado em 01-head.html: {missing}")
    return "\n".join(f"{k}{{{v}}}" for k, v in wanted.items())


def pat_css():
    cam = BI.camada_css()   # a camada inteira, com o keyframe do morph gerado pelo módulo
    body = ("/* o CSS de sistema do template, só o que os quadros usam (extraído de src/01-head.html) */\n"
            + scope(system_css())
            + PAT_OVERRIDES
            + "/* a camada de movimento inteira (src/04-camada.css), escopada a .pat */\n"
            + scope(cam))
    return '<style id="pat-css">\n/* gerado por scripts/ds-patterns.py: não editar à mão */\n' + PAT_TOKENS + body + "</style>"


# ================================================================ os quadros da seção 09
def quad(key, classes, inner, title, text):
    return (f'<div class="pat-item">\n<div class="pat" data-pat="{key}"><section class="slide visible {classes}"><div class="frame">{inner}</div></section></div>\n'
            f'<div class="pat-cap"><b>{H.escape(title)}</b><span>{H.escape(text)}</span></div>\n</div>')


def marker():
    return '<svg class="fa-mk fa-pulse" style="--d0:.1s" viewBox="0 0 100 100"><use href="#pedra"/></svg>'


def sep():
    return '<svg class="sep" viewBox="0 0 100 100" aria-hidden="true"><use href="#pedra"/></svg>'


def quads():
    MOV, CAM, SINAIS, ASSUNTOS, TABELA, FIOS, POEMA = BI.MOV, BI.CAM, BI.SINAIS, BI.ASSUNTOS, BI.TABELA, BI.FIOS, BI.POEMA
    q = []
    # 1 · a Moldura em laranja, com o ritmo e o fecho (Statement 05)
    rit = sep().join(f'<span class="it fa-in" style="--d0:{IC.f(1.2 + i * .35)}s">{t}</span>' for i, t in enumerate(["Item um", "Item dois", "Item três", "Item quatro"]))
    q.append(quad("moldura", "ctr laranja",
        IC.resonance(1.0) + '<div class="canvas fa-voz">' + marker()
        + '<p class="stmt fa-in" style="--d0:.1s"><span class="fa-nw">Statement</span><br><span class="fa-nw">lorem ipsum</span><br><span class="fa-nw">sit <span class="hl" data-w="amet" style="--d:1s">amet</span>.</span></p>'
        + '<div class="fa-apoio"><p class="cap fa-rit">' + rit + '</p>'
        + '<p class="body-l fa-fecho fa-in slow" style="--d0:3.1s">O fecho em corpo grande, branco, depois da lista.</p></div></div>',
        "Moldura · Statement 05",
        "Seis contornos da pedra em laranja escuro sobre o laranja, tom sobre tom, respirando em 6s; o marcador acima, a frase com o grifo invertido, o ritmo em legenda com a pedra miúda de separador e o fecho em corpo grande. Funciona nas cinco superfícies."))
    # 2 · a anatomia da capa (Capa 07)
    q.append(quad("anatomia", "bare inv",
        IC.anatomy() + '<div class="canvas fa-capa"><span class="cap mut fa-in" style="--d0:.2s">Setembro 2026 · Africa Creative/™</span>'
        + '<h1 class="stmt fa-in slow" style="--d0:.4s"><span class="fa-nw">Statement</span><br><span class="fa-nw">da <span class="fa-ora">capa</span></span><br><span class="fa-nw">em linhas.</span></h1>'
        + '<p class="body-l fa-in slow" style="--d0:1.1s"><span class="fa-nw">Corpo grande lorem ipsum dolor</span><br><span class="fa-nw">sit amet, em duas linhas fixas.</span></p></div>',
        "Anatomia da capa · Capa 07",
        "O quadrado de quinas redondas vira a pedra (1,5s); quatro contornos entram e respiram em onda a partir do título pousado (1,8s); o logo chega por último (3,8s), em laranja sobre a pedra branca. Slide preto, sem selo; o acento de texto numa palavra. Exceção declarada do logo sobre preto."))
    # 3 · as órbitas (Título 04)
    q.append(quad("orbitas", "",
        '<div class="fa-orb2-tx"><p class="fa-orb2-ttl fa-in" style="--d0:.2s"><span class="fa-nw"><span class="hl" data-w="Título lateral" style="--d:1.1s">Título lateral</span></span><br><span class="fa-nw">em três linhas curtas</span><br><span class="fa-nw">com o <span class="hl" data-w="grifo duplo" style="--d:1.1s">grifo duplo</span>.</span></p>'
        + '<p class="fa-sup left fa-orb2-sup fa-in" style="--d0:1.0s"><span class="fa-nw">Apoio em três linhas fixas,</span><br><span class="fa-nw">corpo pequeno, cinza, alinhado à esquerda,</span><br><span class="fa-nw">na altura do diagrama.</span></p></div>'
        + '<div class="fa-orb2" aria-hidden="true">' + IC.orbita(SINAIS, ASSUNTOS, "ID") + '</div>',
        "Órbitas · Título 04",
        "A pedra-coração bate duas vezes e cada batida solta um contorno que cresce e congela numa faixa: os sinais em laranja na primeira, os assuntos com hastes na segunda. Quando a segunda congela, acabou. Grifo duplo permitido, só aqui."))
    # 4 · o poema em máquina de escrever (Conteúdo 05)
    q.append(quad("poema", "bare",
        '<div class="canvas fa-po">' + IC.poema(**POEMA) + '</div>',
        "Poema em máquina de escrever · Conteúdo 05",
        "Cada linha se escreve em passos de um caractere (22ms), e só depois a próxima, na ordem de leitura: página esquerda, depois direita; o grifo por último. Corpo 1,5cqw, uma tinta só, sem Moldura e sem selo."))
    # 5 · o ecossistema nasce (Sistema 01)
    q.append(quad("eco-nasce", "inv",
        '<div class="fa-eco-tx"><p class="fa-eco-ttl fa-in" style="--d0:.2s"><span class="fa-nw">Título lateral</span><br><span class="fa-nw">em quatro linhas curtas</span><br><span class="fa-nw">com o <span class="hl" data-w="grifo" style="--d:1.1s">grifo</span> na terceira</span><br><span class="fa-nw">e o ponto na última.</span></p>'
        + '<p class="fa-sup left fa-eco-sup fa-in" style="--d0:1.0s"><span class="fa-nw">Apoio em três linhas fixas,</span><br><span class="fa-nw">corpo pequeno, cinza,</span><br><span class="fa-nw">na altura do diagrama.</span></p></div>'
        + '<div class="fa-eco" aria-hidden="true">' + IC.ecossistema("ds-nasce", MOV) + '</div>' + IC.eco_sa(True, CAM),
        "Ecossistema · nasce · Sistema 01",
        "O núcleo bate e cada linha nasce de dentro para fora, com o nome deslizando na curva (passo de 1,1s a partir de 1,8s). Em 8s a legenda da camada entra e brilha três vezes; a cada brilho, uma leva de pontos-cometa nasce em todas as linhas e passa a circular, cada linha na sua velocidade."))
    # 6 · o momento (Sistema 02)
    q.append(quad("eco-momento", "inv",
        '<div class="fa-eco-tx pilar"><p class="cap fa-eco-kk fa-in" style="--d0:.2s">Legenda do momento</p>'
        + '<p class="fa-eco-ttl fa-in" style="--d0:.35s"><span class="fa-nw">Movimento 02</span><br><span class="fa-nw">faz <span class="hl" data-w="isto" style="--d:1.1s">isto</span>.</span></p>'
        + '<p class="body fa-eco-inc one fa-in" style="--d0:.7s">Incipit lorem ipsum dolor sit amet consectetur.</p>'
        + '<p class="fa-def one fa-in" style="--d0:.95s">Definição lorem ipsum dolor sit amet, em corpo pequeno cinza.</p>'
        + IC.rows_html(TABELA, 1.2, .18) + '</div>'
        + '<div class="fa-eco pronto" aria-hidden="true">' + IC.ecossistema("ds-momento", MOV, lit=1) + '</div>' + IC.eco_sa(False, CAM),
        "Ecossistema · momento · Sistema 02",
        "Tudo entra pronto e os pontos já circulam; o núcleo bate uma vez e a faixa do movimento se acende em duas metades a partir do nome, que fica preto sobre o laranja. À esquerda, a legenda, a função como título, o incipit, a definição e a tabela de fios."))
    # 7 · a camada (Sistema 03)
    q.append(quad("eco-camada", "inv",
        '<div class="fa-eco-tx pilar"><p class="cap fa-eco-kk fa-in" style="--d0:.2s">Legenda da camada:</p>'
        + '<p class="fa-eco-ttl fa-in" style="--d0:.35s"><span class="fa-nw">Título lateral</span><br><span class="fa-nw">em três linhas curtas,</span><br><span class="fa-nw">com o <span class="hl" data-w="grifo" style="--d:1.1s">grifo</span>.</span></p>'
        + '<p class="body fa-eco-inc fa-in" style="--d0:.7s"><span class="fa-nw">Subtítulo em corpo regular,</span><br><span class="fa-nw">em três linhas fixas,</span><br><span class="fa-nw">entre o título e a tabela.</span></p>'
        + IC.amb_rows(FIOS) + '</div>'
        + '<div class="fa-eco pronto" aria-hidden="true">' + IC.ecossistema("ds-camada", MOV, lit=len(IC.ECO_R), social=True) + '</div>' + IC.eco_sa(False, CAM),
        "Ecossistema · camada · Sistema 03",
        "Sem faixa, sem brilho, sem batida: só as linhas, os nomes apagados e os pontos de todas as linhas em laranja, circulando. À esquerda, a tabela que se destaca linha a linha."))
    # 8 · a tabela que se destaca, sozinha, sobre branco
    q.append(quad("tabela", "",
        '<div class="fa-eco-tx pilar"><p class="cap fa-eco-kk fa-in" style="--d0:.2s">Legenda da tabela:</p>'
        + '<p class="fa-eco-ttl fa-in" style="--d0:.35s"><span class="fa-nw">Tabela que se destaca</span><br><span class="fa-nw">linha a <span class="hl" data-w="linha" style="--d:1.1s">linha</span>.</span></p>'
        + IC.amb_rows(FIOS) + '</div>',
        "Tabela que se destaca · sobre branco",
        "A cada .45s o fio de cima se desenha da esquerda para a direita, o nome em laranja recebe o facho de luz (o mesmo da legenda do sistema) e o corpo entra em seguida; o fio de baixo fecha a tabela no fim. Coluna dos rótulos de 11cqw, para nomes compostos."))
    return "\n".join(q)


# ================================================================ os usos novos da pedra (seção 05), estáticos
def pedra_usos():
    cards = []
    # a Moldura: seis contornos na caixa, cortados pelo card (só os arcos), a frase no meio
    rings = "".join(f'<path d="{IC.superpath(h, 4.3)}" fill="none" stroke="currentColor" stroke-width=".3" opacity="{o}"/>' for h, o, _ in IC.RES_RINGS)
    cards.append('<div class="gfx"><div class="frame">'
                 f'<svg viewBox="0 0 100 100" preserveAspectRatio="xMidYMid slice" style="position:absolute;inset:0;width:100%;height:100%;color:var(--laranja)" aria-hidden="true">{rings}</svg>'
                 '<p class="ghost-type">A frase.</p></div>'
                 '<div class="cap"><b>Moldura</b><span>Seis contornos atrás da frase, tom sobre tom, respirando. Statement 05 a 07. Viva na seção 09.</span></div></div>')
    # a anatomia: a pedra, os quatro contornos, o logo sobre a pedra branca
    k = 2 * IC.ANA_HALF / IC.LOGO_BOX
    w, x, y = 500 * k, 50 - IC.ANA_HALF - IC.LOGO_OFF[0] * k, 50 - IC.ANA_HALF - IC.LOGO_OFF[1] * k
    ana = "".join(f'<path d="{IC.superpath(IC.ANA_HALF * sc, 4.3)}" fill="none" stroke="var(--laranja)" stroke-width=".34" opacity="{o}"/>' for sc, o, _ in IC.RINGS)
    ana += (f'<path d="{IC.superpath(IC.ANA_HALF, 4.3)}" fill="var(--laranja)"/>'
            f'<path d="{IC.superpath(IC.ANA_HALF - 1.2, 4.3)}" fill="var(--branco)"/>'
            f'<use href="#itau" x="{IC.f(x)}" y="{IC.f(y)}" width="{IC.f(w)}" height="{IC.f(w)}" style="color:var(--laranja)"/>')
    cards.append('<div class="gfx"><div class="frame">'
                 f'<svg viewBox="0 0 100 100" style="width:62%;overflow:visible" aria-hidden="true">{ana}</svg></div>'
                 '<div class="cap"><b>Anatomia</b><span>Do quadrado de quinas redondas à pedra, com quatro contornos em onda; por último o logo sobre a pedra branca. Capa 07.</span></div></div>')
    # o coração: a pedra com o ID, as duas faixas, os sinais e os assuntos
    cx, cy = IC.ORB_C
    orb = "".join(f'<path fill="var(--sup-2)" fill-rule="evenodd" d="{IC.superpath(o, 4.3, cx=cx, cy=cy)} {IC.superpath(i, 4.3, cx=cx, cy=cy)}"/>' for i, o in (IC.ORB_B1, IC.ORB_B2))
    orb += "".join(f'<circle cx="{IC.f(px)}" cy="{IC.f(py)}" r=".36" fill="var(--laranja)"/>' for px, py, _ in IC.arc_points(IC.ORB_B1[1], 4))
    for px, py, a in IC.arc_points(IC.ORB_B2[1], 7):
        x0, y0 = IC.off(px, py, a, IC.ORB_SPOKE[0])
        x1, y1 = IC.off(px, py, a, IC.ORB_SPOKE[1])
        orb += f'<line x1="{IC.f(x0)}" y1="{IC.f(y0)}" x2="{IC.f(x1)}" y2="{IC.f(y1)}" stroke="var(--fg)" stroke-width=".06" opacity=".5"/><circle cx="{IC.f(x1)}" cy="{IC.f(y1)}" r=".4" fill="var(--fg)"/>'
    orb += (f'<path d="{IC.superpath(IC.ORB_PD, 4.3, cx=cx, cy=cy)}" fill="var(--fg)"/>'
            f'<text x="{cx}" y="{cy + .1}" text-anchor="middle" dominant-baseline="middle" fill="var(--bg)" font-family="var(--display)" font-weight="700" font-size="3.6" letter-spacing="-.02em">ID</text>')
    cards.append('<div class="gfx"><div class="frame">'
                 f'<svg viewBox="0 0 {IC.ORB_W} {IC.ORB_H}" style="width:78%;overflow:visible" aria-hidden="true">{orb}</svg></div>'
                 '<div class="cap"><b>Coração</b><span>A pedra com um texto dentro bate e deposita as faixas: os sinais em laranja, os assuntos com hastes. Título 04.</span></div></div>')
    return "\n".join(cards)


# ================================================================ injeção
def inject(s, name, body):
    a, b = f"<!-- {name}:BEGIN -->", f"<!-- {name}:END -->"
    if s.count(a) != 1 or s.count(b) != 1:
        sys.exit(f"marcador {name} ausente ou repetido no design system")
    return re.sub(re.escape(a) + r".*?" + re.escape(b), lambda m: a + "\n" + body + "\n" + b, s, flags=re.S)


def main():
    s = open(DS_HTML, encoding="utf-8").read()
    s = inject(s, "DS-PAT-CSS", pat_css())
    s = inject(s, "DS-PEDRA-USOS", pedra_usos())
    s = inject(s, "DS-PATTERNS", quads())
    if "{{" in s:
        sys.exit("placeholder sem valor no design system")
    open(DS_HTML, "w", encoding="utf-8").write(s)
    n_quads = s.count('class="pat" ')
    print(f"{n_quads} quadros · {len(s)//1024} KB")
    print(DS_HTML)


if __name__ == "__main__":
    main()
