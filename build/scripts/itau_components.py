#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Os componentes vivos do sistema Itaú × Africa (17/09/2026): a geometria da pedra, a Moldura, a anatomia da
capa, as órbitas, o poema em máquina de escrever, o ecossistema em órbitas, as tabelas. Nasceram no deck
"Itaú fim de ano V2" e daqui alimentam o template (build-itau.py monta o catálogo com texto de exemplo) e os
decks (o build de cada deck chama as mesmas funções com a sua narrativa). Uma fonte só: quem muda a forma,
muda aqui. O CSS correspondente (prefixo fa-) mora em src/01-head.html, bloco "A CAMADA DE MOVIMENTO".

Convenções: toda geometria em cqw dentro de um viewBox em cqw; a pedra é a superelipse de expoente 4,3 com
360 pontos (a mesma contagem em todo path, para o CSS interpolar d: path()); --d0 é o instante em que a
peça entra, --dur a duração; a animação só corre em .slide.visible e termina num estado final que fica.
"""
import html as H
import math
import re

PEDRA = '<svg %s viewBox="0 0 100 100"><use href="#pedra"/></svg>'


def f(x, p=2):
    return f"{x:.{p}f}".rstrip("0").rstrip(".") if isinstance(x, float) else str(x)


def acc(text, d="1.6s"):
    """{palavra} vira o grifo do sistema: bloco laranja com a palavra em branco (inverte sobre laranja).
    [texto] vira texto em laranja, sem bloco (o Main KPI, 17/09)."""
    def rep(m):
        w = m.group(1)
        return f'<span class="hl" data-w="{H.escape(w, quote=True)}" style="--d:{d}">{H.escape(w)}</span>'
    out = re.sub(r"\{([^}]+)\}", rep, H.escape(text))
    return re.sub(r"\[([^\]]+)\]", lambda m: f'<span class="fa-ora">{m.group(1)}</span>', out)


def lines(parts, d="1.6s", nw=True):
    if not nw:
        return " ".join(acc(p, d) for p in parts)
    return "<br>".join(f'<span class="fa-nw">{acc(p, d)}</span>' for p in parts)


def esc(t):
    return H.escape(t, quote=True)


def body_size(parts):
    """O corpo pela linha mais larga, para a frase morar dentro da Moldura com folga (17/09): a abertura
    tem 70cqw e a frase fica em até 46. Medido no deck, a Figtree 700 rende cerca de 0,47em por
    caractere; daí os tetos: Statement (8cqw) até 12 caracteres na linha, Título (5,6cqw) até 17,
    Título curto (4,6cqw) acima disso."""
    w = max(len(plain(p)) for p in parts)
    return "stmt" if w <= 12 else "ttl" if w <= 17 else "ttl-s"


def marker(d0=".1s"):
    return PEDRA % f'class="fa-mk fa-pulse" style="--d0:{d0}"'


ANA_HALF = 30      # meia largura da pedra na caixa 0..100 da anatomia
ANA_N_SQ = 9       # o quadrado de quinas redondas (o ícone de app, o logo de antes): de onde a pedra saiu
LOGO_BOX = 479.8   # a pedra do vetor do Commons mede 479,8 dos 500, a partir de (10.2, 10.0): medido nos subpaths
LOGO_OFF = (10.2, 10.0)


def superpath(half, n, npts=360, cx=50, cy=50):
    """Superelipse |x|^n + |y|^n = 1 como polilinha de npts pontos, sempre com a mesma estrutura: é o
    que deixa o CSS interpolar de um expoente a outro (d: path()) no morph do quadrado à pedra."""
    pts = []
    for i in range(npts):
        t = 2 * math.pi * i / npts
        c, s = math.cos(t), math.sin(t)
        pts.append(f"{cx + half * math.copysign(abs(c) ** (2 / n), c):.2f},{cy + half * math.copysign(abs(s) ** (2 / n), s):.2f}")
    return "M" + " L".join(pts) + "Z"


RINGS = [(1.12, .80, 0.0), (1.26, .60, 0.3), (1.42, .44, 0.6), (1.60, .30, 0.9)]   # escala, opacidade, atraso da onda
WAVE_T0 = 1.8   # quando o título pousa (.4s + 1.4s): a primeira onda parte daí


def anatomy():
    """Forma, contorno e o logo, como no filme da Pentagram para o Itaú (2024), mas o contorno vira
    ressonância: quatro contornos concêntricos da pedra, tom sobre tom, que expandem e retraem em
    onda, em loop (o trecho 6,1s a 7,0s do sizzle, em que os contornos em relevo respiram). A pedra
    pulsa no centro como fonte da onda; a primeira onda parte quando o título pousa. As guias
    tracejadas de prancheta saíram a pedido do Bruno (17/09): poluíam. As letras são vazadas no
    vetor do Commons, então o logo em laranja vai por cima de uma pedra branca um pouco menor."""
    k = 2 * ANA_HALF / LOGO_BOX
    w, x, y = 500 * k, 50 - ANA_HALF - LOGO_OFF[0] * k, 50 - ANA_HALF - LOGO_OFF[1] * k
    rings = "".join(f'<path class="fa-ana-ring" style="--o:{o};--d0:{WAVE_T0 + d:.1f}s" d="{superpath(ANA_HALF * sc, 4.3)}"/>'
                    for sc, o, d in RINGS)
    return ('<svg class="fa-ana" viewBox="0 0 100 100" aria-hidden="true">'
            + rings
            + '<g class="fa-ana-core">'
            + f'<path class="fa-ana-pd" d="{superpath(ANA_HALF, 4.3)}"/>'
            + f'<g class="fa-ana-logo"><path fill="var(--branco)" d="{superpath(ANA_HALF - 1.2, 4.3)}"/>'
            + f'<use href="#itau" x="{f(x)}" y="{f(y)}" width="{f(w)}" height="{f(w)}"/></g>'
            + '</g></svg>')


def anatomy_css():
    return ('@keyframes faAnaForm{from{d:path("' + superpath(ANA_HALF, ANA_N_SQ) + '")}to{d:path("' + superpath(ANA_HALF, 4.3) + '")}}\n')


RES_RINGS = [(29, .95, 0.0), (31.6, .80, .25), (34.2, .65, .5), (36.8, .50, .75), (39.4, .36, 1.0), (42, .24, 1.25)]   # meia largura na caixa 0..100 (x1,2 = cqw), opacidade, atraso; o interno a 34,8cqw deixa 5cqw para a linha mais larga de Statement


BODY_CQW = {"stmt": 8, "ttl": 5.6, "ttl-s": 4.6}   # o corpo de cada classe, em cqw


def resonance(rs=1.0, br=1.06):
    """A Moldura (opção A do burst de 17/09, escolhida pelo Bruno): a ressonância da capa centralizada
    e grande, seis contornos da pedra em laranja escuro, tom sobre tom, em degradê de opacidade,
    respirando devagar. A caixa mede 120cqw, maior que o slide, então o que aparece são os arcos
    laterais, uma abertura de palco em volta da frase. O anel interno tem meia largura de 32,4cqw e
    o bloco de texto vai até 22cqw do centro: nada cruza letra, nem no pico da respiração."""
    return (f'<svg class="fa-res" style="--rs:{f(rs)};--br:{f(br)}" viewBox="0 0 100 100" aria-hidden="true">'
            + "".join(f'<path class="fa-res-ring" style="--o:{o};--d0:{.2 + d:.2f}s" d="{superpath(h, 4.3)}"/>' for h, o, d in RES_RINGS)
            + '</svg>')


TW_CHAR, TW_LINE, TW_STANZA = .022, .18, .5   # a máquina de escrever: por caractere, entre linhas, entre estrofes


def poema(screen, estrofes, litania, veredito, prosa, t0=.4):
    """A página dupla do poema (17/09), escrita à máquina: cada linha se escreve da esquerda para a direita
    em passos de um caractere, e só depois a próxima, na ordem de leitura (página esquerda, depois direita);
    o grifo por último. À esquerda o título modesto e as estrofes; à direita a litania, o veredito e a linha
    fina. Devolve a grade (fa-po-grid); o slide é bare, sem Moldura."""
    t = [t0]   # o relógio, compartilhado pelas linhas

    def tw(text, grifo_d=None):
        n = len(plain(text))
        dur = max(.25, n * TW_CHAR)
        html = (f'<span class="fa-tw" style="--d0:{f(t[0])}s;--dur:{f(dur)}s;--n:{n}">'
                + (acc(text, grifo_d) if grifo_d else H.escape(text)) + '</span>')
        t[0] += dur + TW_LINE
        return html

    def stanza(cls, parts, grifo_last=False):
        out = []
        for k, p in enumerate(parts):
            last = grifo_last and k == len(parts) - 1
            out.append(tw(p, f(t[0] + max(.25, len(plain(p)) * TW_CHAR) + .5) + "s" if last or "{" in p else None))
        t[0] += TW_STANZA
        return f'<p class="{cls}">' + "".join(out) + '</p>'

    esq = [stanza("sub fa-po-ttl", screen)] + [stanza("fa-po-est", e) for e in estrofes]
    dir_ = [stanza("fa-po-est fa-po-lit", litania), stanza("fa-po-est", veredito), stanza("fa-po-est", prosa)]
    return ('<div class="fa-po-grid"><div class="fa-po-col fa-po-esq">' + "".join(esq) + '</div>'
            '<div class="fa-po-col fa-po-dir">' + "".join(dir_) + '</div></div>')


def plain(t):
    """Sem as marcas de acento: {grifo em bloco} e [texto em laranja]."""
    return t.replace("{", "").replace("}", "").replace("[", "").replace("]", "")


def rows_html(rows, t0, step, cls=""):
    # linha da tabela numa linha só até 68 caracteres (cabe na coluna de 43,6cqw); acima disso a tabela alarga para 56cqw (wide)
    # e a linha continua única (o Eco, 74 caracteres, a pedido de 17/09); embaixo, o anel de fora já curvou para longe
    wide = any(len(plain(b)) > 68 for _, b in rows)
    if wide:
        cls += " wide"
    return f'<div class="fa-rows{cls}">' + "".join(
        f'<div class="row fa-in" style="--d0:{f(t0 + i * step)}s"><span class="cap">{H.escape(plain(a))}</span><span class="body-s{" one" if wide or len(plain(b)) <= 68 else ""}">{H.escape(plain(b))}</span></div>'
        for i, (a, b) in enumerate(rows)) + "</div>"


# ================================================================ as órbitas
# o diagrama do slide 4: a caixa em cqw (o viewBox é em cqw), o centro, a pedra, as duas faixas
ORB_W, ORB_H = 64, 46
ORB_C = (32, 23)
ORB_LEFT = 52                                # onde a caixa começa no quadro. Atenção: o cqw deste template mede a área de conteúdo; o quadro inteiro tem 111,6cqw
ORB_PD = 5.3
ORB_B1, ORB_B2 = (7.5, 9.4), (15.3, 16.9)   # faixa interna e externa: (borda de dentro, borda de fora)
ORB_GAP = 1.2                                # a distância constante do ponto ao rótulo
ORB_SPOKE = (.3, 1.2)                        # a haste dos assuntos: começa e termina a esta distância da faixa
ORB_T = (.6, 2.0)                            # as duas pulsações
ORB_ARRIVE = (1.4, 2.8)                      # quando cada uma chega na sua faixa e congela
# na ordem em que aparecem ao redor, a partir do topo, em sentido horário; a posição é por perímetro igual


def arc_points(half, n, start_deg=270):
    """n pontos igualmente espaçados pelo perímetro da superelipse (e não por ângulo, que nas quinas fica
    irregular), a partir do topo, em sentido horário. Devolve (x, y, ângulo radial em graus)."""
    cx, cy = ORB_C
    N = 1440
    pts = []
    for i in range(N + 1):
        a = math.radians(start_deg) + 2 * math.pi * i / N
        c, s = math.cos(a), math.sin(a)
        pts.append((cx + half * math.copysign(abs(c) ** (2 / 4.3), c), cy + half * math.copysign(abs(s) ** (2 / 4.3), s)))
    cum = [0.0]
    for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
        cum.append(cum[-1] + math.hypot(x1 - x0, y1 - y0))
    total = cum[-1]
    out = []
    for k in range(n):
        target = total * k / n
        i = min(range(len(cum)), key=lambda j: abs(cum[j] - target))
        x, y = pts[i]
        out.append((x, y, math.degrees(math.atan2(y - cy, x - cx))))
    return out


def off(x, y, ang, d):
    t = math.radians(ang)
    return x + d * math.cos(t), y + d * math.sin(t)


def orb_label(word, x, y, ang, d0, cls="", flip=1.4):
    """O rótulo se ancora pelo lado: à direita começa no ponto, à esquerda termina nele, em cima e embaixo
    centra. Se à direita ele fosse vazar do quadro (o diagrama mora perto da borda), vai para cima ou para
    baixo do ponto, centrado, a flip cqw dele."""
    c, sn = math.cos(math.radians(ang)), math.sin(math.radians(ang))
    lb = 10 / ORB_W * 100
    if c > .3 and ORB_LEFT + x + .55 * len(word) + .6 > 104:   # 104cqw = 93% do quadro
        y = y + (flip if sn > 0 else -flip)
        pos = f"left:{f((x - .6) / ORB_W * 100 - lb / 2)}%;text-align:center"
    elif c > .3:
        pos = f"left:{f(x / ORB_W * 100)}%;text-align:left"
    elif c < -.3:
        pos = f"left:{f(x / ORB_W * 100 - lb)}%;text-align:right"
    else:
        pos = f"left:{f(x / ORB_W * 100 - lb / 2)}%;text-align:center"
    return f'<span class="cap fa-orb2-lb {cls} fa-in" style="{pos};width:{f(lb)}%;top:{f((y - .55) / ORB_H * 100)}%;--d0:{f(d0)}s">{H.escape(word)}</span>'


def orbita(signals, subjects, id_text="ID"):
    """A pedra com o ID é o coração. Bate duas vezes; cada batida solta um contorno dela mesma que cresce
    e congela numa faixa cheia, tom sobre tom (a Matéria, como o One Sheeter do Yummly). Na primeira faixa
    os sinais solitários que o algoritmo lê (em laranja); na segunda, com hastes, o que chega. Quando a
    segunda congela, acabou: nada fica em loop. Pontos por perímetro igual; rótulos HTML a uma distância
    constante, ancorados pelo lado."""
    cx, cy = ORB_C
    pedra = (f'<svg class="fa-orb2-pd" style="width:{f(2 * ORB_PD / ORB_W * 100)}%" viewBox="0 0 100 100"><g class="fa-orb2-heart"><use href="#pedra"/>'
             f'<text class="fa-orb2-id" x="50" y="52" text-anchor="middle" dominant-baseline="middle">{H.escape(id_text)}</text></g></svg>')
    out = [f'<svg class="fa-orb2-svg" viewBox="0 0 {ORB_W} {ORB_H}" aria-hidden="true">']
    for k, (inner, outer) in enumerate((ORB_B1, ORB_B2)):   # as faixas, depositadas quando o pulso chega
        out.append(f'<path class="fa-orb2-band" style="--d0:{f(ORB_ARRIVE[k])}s" fill-rule="evenodd" d="{superpath(outer, 4.3, cx=cx, cy=cy)} {superpath(inner, 4.3, cx=cx, cy=cy)}"/>')
    for k, (inner, outer) in enumerate((ORB_B1, ORB_B2)):   # os pulsos: partem da pedra e congelam na faixa
        out.append(f'<path class="fa-orb2-pulse" style="--d0:{f(ORB_T[k])}s;--to:{f(outer / ORB_PD)}" d="{superpath(ORB_PD, 4.3, cx=cx, cy=cy)}"/>')
    labels = []
    for i, ((x, y, a), w) in enumerate(zip(arc_points(ORB_B1[1], len(signals)), signals)):
        d0 = ORB_ARRIVE[0] + .12 + i * .12
        out.append(f'<g class="fa-pop" style="--d0:{f(d0)}s"><circle cx="{f(x)}" cy="{f(y)}" r=".36" fill="var(--laranja)"/></g>')
        ax, ay = off(x, y, a, ORB_GAP)
        labels.append(orb_label(w, ax, ay, a, d0 + .2, "fa-orb2-sig"))
    for i, ((x, y, a), w) in enumerate(zip(arc_points(ORB_B2[1], len(subjects)), subjects)):
        d0 = ORB_ARRIVE[1] + .12 + i * .12
        x0, y0 = off(x, y, a, ORB_SPOKE[0])
        x1, y1 = off(x, y, a, ORB_SPOKE[1])
        out.append(f'<line class="fa-draw fa-orb2-spoke" style="--d0:{f(d0)}s;--dur:.5s" x1="{f(x0)}" y1="{f(y0)}" x2="{f(x1)}" y2="{f(y1)}" pathLength="1"/>')
        out.append(f'<g class="fa-pop" style="--d0:{f(d0 + .3)}s"><circle cx="{f(x1)}" cy="{f(y1)}" r=".4" fill="var(--fg)"/></g>')
        ax, ay = off(x1, y1, a, ORB_GAP)
        labels.append(orb_label(w, ax, ay, a, d0 + .25))
    out.append("</svg>")
    return pedra + "".join(out) + "".join(labels)



# ================================================================ o ecossistema (a arquitetura e os movimentos, 17/09)
ECO_BOX = 50                              # a caixa do svg em cqw (viewBox 0..50); o centro em (25, 25)
ECO_C = 25
ECO_LEFT, ECO_TOP = 59, 6.4               # a caixa no quadro: o centro cai em 84cqw (75% do quadro, como as órbitas) e 31,4 (o meio)
ECO_CORE = 4.6                            # meia largura da pedra do logo
ECO_CLEAR = 6.0                           # a quina da pedra chega a 5,54 (4,6 × 2^(-1/4,3) × √2); a primeira faixa começa logo depois
ECO_R = [9.2, 12.3, 15.4, 18.5, 21.6]     # as cinco linhas, de dentro para fora: cada uma fecha a faixa de um movimento (2,2cqw cada)
ECO_OVER = 3                              # graus além do fundo em cada metade da faixa acesa: as duas se sobrepõem e não fica emenda
ECO_INSET = 0                             # a faixa ocupa o entrelinhas inteiro, de linha a linha (pedido de 17/09)
ECO_LAP = [16, 22, 29, 37, 46]            # segundos por volta: quanto mais fora, mais devagar
ECO_DOTS = [3, 4, 5, 6, 7]                # Social Activations por linha
ECO_TAIL = [(.30, .6), (.23, .38), (.16, .2), (.10, .08)]   # a cauda do cometa, do ponto para trás: (largura, opacidade) de cada trecho
ECO_TAIL_LEN = 6.5                        # comprimento da cauda em cqw (em graus, depende do raio da linha; no máximo 40°)
ECO_HALO = 1.05                           # o raio do halo que brilha em volta do ponto
ECO_T0, ECO_STEP = 1.8, 1.1               # na arquitetura: a primeira batida do núcleo e o passo entre elas
ECO_SA = 8.0                              # a legenda de Social Activations entra...
ECO_SHINE0, ECO_SHINE_T, ECO_SHINES = 8.7, 1.4, 3   # ...e brilha três vezes; a cada brilho, uma leva de pontos
ECO_WAVE_LAG = .6                         # a leva chega logo depois do brilho
ECO_LIT = (.5, .8)                        # no movimento: a batida do núcleo, e a faixa que começa a se acender
SOC_ROW0, SOC_STEP = 1.2, .45              # em Social Activations: os canais à esquerda se destacam um a um


def low(t):
    """"Faz sentir." vira "faz sentir": a função lida na curva, sem ponto final."""
    t = t.rstrip(".")
    return t[0].lower() + t[1:]


def eco_pt(r, ang):
    a = math.radians(ang)
    return ECO_C + r * math.cos(a), ECO_C + r * math.sin(a)


def eco_band(i):
    """A faixa do movimento i: da linha de dentro (ou da quina da pedra) até a própria linha, com o recuo."""
    a = (ECO_R[i - 1] if i else ECO_CLEAR) + ECO_INSET
    b = ECO_R[i] - ECO_INSET
    return a, b


def ecossistema(sid, movimentos, lit=None, social=False):
    """O núcleo é o logo do Itaú (a pedra branca um pouco menor por baixo, como na capa), com um brilho
    radial que respira. Cada movimento é uma faixa entre linhas, de dentro para fora, e o nome (legenda)
    com a função (cinza) vive na curva da faixa, no alto.
    Na arquitetura (lit=None) tudo nasce: o núcleo bate, a batida cresce e deposita a linha, e o nome chega
    deslizando na curva; depois das cinco, a legenda de Social Activations entra embaixo e brilha; a cada
    brilho, uma leva de pontos laranja com rastro nasce em todas as linhas e passa a circular, cada linha na
    sua velocidade. Só isso e a respiração do brilho ficam em loop.
    No slide do movimento k (lit=k) tudo entra pronto e os pontos já circulam; as faixas dos movimentos
    anteriores ficam em laranja claro; e a faixa k se acende: o núcleo bate e a faixa se desenha a partir do
    nome, para os dois lados, até fechar embaixo; o nome fica preto sobre o laranja.
    Em Social Activations (social=True, lit=5) não há faixa, brilho nem batida: só as linhas, os nomes apagados e os
    pontos de todas as linhas em laranja, circulando (a única animação laranja, a pedido de 17/09).
    pontos de todas as linhas em laranja, circulando (a única animação laranja, a pedido de 17/09)."""
    C = ECO_C
    nasce = lit is None
    born = " born" if nasce else ""
    out = [f'<svg class="fa-eco-svg" viewBox="0 0 {ECO_BOX} {ECO_BOX}" aria-hidden="true"><defs>'
           f'<radialGradient id="fa-eco-{sid}-glow"><stop offset="0" stop-color="#FF6200" stop-opacity=".6"/>'
           '<stop offset=".4" stop-color="#FF6200" stop-opacity=".22"/><stop offset="1" stop-color="#FF6200" stop-opacity="0"/></radialGradient>'
           f'<radialGradient id="fa-eco-{sid}-dg"><stop offset="0" stop-color="#FF6200" stop-opacity=".75"/>'
           '<stop offset=".45" stop-color="#FF6200" stop-opacity=".25"/><stop offset="1" stop-color="#FF6200" stop-opacity="0"/></radialGradient>']
    # os caminhos dos nomes, no meio de cada faixa: o círculo começa embaixo e gira no sentido horário, então o alto fica em 50%
    for i in range(len(ECO_R)):
        a, b = eco_band(i)
        tp = (a + b) / 2 - .15   # o nome um pouco acima do meio da faixa: os pontos da linha de dentro passam longe da cedilha
        out.append(f'<path id="fa-eco-{sid}-tp{i}" d="M{C},{f(C + tp)} A{tp},{tp} 0 1 1 {C},{f(C - tp)} A{tp},{tp} 0 1 1 {C},{f(C + tp)}"/>')
    out.append('</defs>')
    if not social:   # em Social Activations não há brilho: laranja só nos pontos (pedido de 17/09)
        out.append(f'<circle class="fa-eco-glow{born}" style="--d0:.4s" cx="{C}" cy="{C}" r="11" fill="url(#fa-eco-{sid}-glow)"/>')
    # as faixas: dos movimentos já vistos, em laranja claro; a do movimento da vez se acende em duas metades, a partir do nome
    if not nasce and not social:   # em Social Activations nenhuma faixa: só as linhas, os nomes apagados e os pontos
        for i in range(min(lit + 1, len(ECO_R))):
            a, b = eco_band(i)
            R, w = (a + b) / 2, b - a
            if i < lit:   # já vista: um anel cheio, em laranja claro
                out.append(f'<circle class="fa-eco-rb done" style="--w:{f(w)}" cx="{C}" cy="{C}" r="{f(R)}"/>')
                continue
            for sweep in (1, 0):   # a da vez: duas metades que se desenham do nome (no alto) até o fundo, cada uma passando um pouco do fundo
                x1, y1 = eco_pt(R, 90 + ECO_OVER if sweep else 90 - ECO_OVER)
                out.append(f'<path class="fa-eco-rb now" style="--w:{f(w)};--d0:{f(ECO_LIT[1])}s" pathLength="1" d="M{C},{f(C - R)} A{R},{R} 0 1 {sweep} {f(x1)},{f(y1)}"/>')
    p0 = ECO_CORE * .92   # a batida nasce escondida atrás do logo (a pedra tem meia largura 4,6 nos lados)
    for i, r in enumerate(ECO_R):
        if nasce:
            d0 = ECO_T0 + i * ECO_STEP
            out.append(f'<circle class="fa-eco-pulse" style="--d0:{f(d0)}s;--to:{f(r / p0)}" cx="{C}" cy="{C}" r="{f(p0)}"/>')
            out.append(f'<circle class="fa-eco-ring born" style="--d0:{f(d0)}s;--s0:{f(ECO_CORE / r)}" cx="{C}" cy="{C}" r="{r}"/>')
        else:   # pronto: a linha do movimento inteira; as dos outros, apagadas (pedido de 17/09)
            out.append(f'<circle class="fa-eco-ring{"" if i == lit else " dim"}" cx="{C}" cy="{C}" r="{r}"/>')
    if social:   # nenhuma batida: a única animação laranja é a circulação dos pontos (pedido de 17/09)
        pass
    elif not nasce:
        out.append(f'<circle class="fa-eco-pulse" style="--d0:{f(ECO_LIT[0])}s;--to:{f(eco_band(lit)[1] / p0)}" cx="{C}" cy="{C}" r="{f(p0)}"/>')
    for i, (nome, fn) in enumerate(movimentos):
        if nasce:
            cls, d0 = "fa-eco-lbg born", ECO_T0 + i * ECO_STEP + .5
        else:
            cls, d0 = "fa-eco-lbg " + ("now" if i == lit else "done" if i < lit else "next"), (ECO_LIT[1] + .2 if i == lit else 0)
        out.append(f'<g class="{cls}" style="--d0:{f(d0)}s"><text class="fa-eco-lb"><textPath href="#fa-eco-{sid}-tp{i}" startOffset="50%">'
                   f'<tspan class="fa-eco-nm">{H.escape(nome.upper())}</tspan><tspan class="fa-eco-fn" dx=".7">{H.escape(low(fn))}</tspan></textPath></text></g>')
    # Social Activations: as levas de pontos, em todas as linhas, cada linha girando na sua velocidade
    for i, r in enumerate(ECO_R):
        dots = []
        for k in range(ECO_DOTS[i]):
            ang = 90 + i * 37 + 360 * k / ECO_DOTS[i]
            wave = k % ECO_SHINES
            d0 = ECO_SHINE0 + wave * ECO_SHINE_T + ECO_WAVE_LAG + (k // ECO_SHINES) * .1 + i * .06
            x, y = eco_pt(r, ang)
            # a cauda: trechos de arco atrás do ponto, cada um mais fino e mais transparente que o anterior
            deg = min(40, ECO_TAIL_LEN / r * 180 / math.pi)
            tail = ""
            for j, (w, o) in enumerate(ECO_TAIL):
                x1, y1 = eco_pt(r, ang - deg * j / len(ECO_TAIL))
                x0, y0 = eco_pt(r, ang - deg * (j + 1) / len(ECO_TAIL))
                tail += f'<path d="M{f(x0)},{f(y0)} A{r},{r} 0 0 1 {f(x1)},{f(y1)}" style="stroke-width:{w};opacity:{o}"/>'
            halo = f'<circle class="fa-eco-halo" style="--i:{i * 7 + k};fill:url(#fa-eco-{sid}-dg)" cx="{f(x)}" cy="{f(y)}" r="{ECO_HALO}"/>'
            dots.append(f'<g class="fa-eco-dot{born}"' + (f' style="--d0:{f(d0)}s"' if nasce else "") + f'>{tail}{halo}<circle cx="{f(x)}" cy="{f(y)}" r=".38"/></g>')
        spin_d0 = f(ECO_SHINE0 + ECO_WAVE_LAG) if nasce else f(-ECO_LAP[i] * (.13 + .2 * i))   # pronto: já no meio da volta
        st = "" if nasce else (" on" if (i == lit or social) else " off")   # no movimento, só os pontos da linha dele ficam laranja; em Social Activations, todos
        out.append(f'<g class="fa-eco-spin{st}" style="--T:{ECO_LAP[i]}s;--d0:{spin_d0}s">' + "".join(dots) + '</g>')
    # o núcleo: o logo, como na capa (as letras são vazadas no vetor, a pedra branca por baixo as pinta)
    k = 2 * ECO_CORE / LOGO_BOX
    w, x, y = 500 * k, C - ECO_CORE - LOGO_OFF[0] * k, C - ECO_CORE - LOGO_OFF[1] * k
    out.append(f'<g class="fa-eco-core{born}" style="--d0:.5s"><path fill="var(--branco)" d="{superpath(ECO_CORE - .18, 4.3, cx=C, cy=C)}"/>'
               f'<use href="#itau" x="{f(x)}" y="{f(y)}" width="{f(w)}" height="{f(w)}"/></g>')
    out.append('</svg>')
    return "".join(out)


def eco_sa(shine, cam, t_in=ECO_SA, t_shine=ECO_SHINE0):
    """A legenda de Social Activations embaixo do diagrama; na arquitetura e no slide dela, brilha três vezes."""
    cls = "fa-eco-sa shine" if shine else "fa-eco-sa"
    st = f"--d0:{f(t_in)}s;--d1:{f(t_shine)}s" if shine else "--d0:.05s"
    return (f'<div class="{cls}" style="{st}"><span class="cap fa-eco-sa-nm">{H.escape(cam[0])}</span>'
            f'<span class="body-s fa-eco-sa-fn">{H.escape(low(cam[1]))}</span></div>')




def amb_rows(rows, t0=None, step=None):
    """Os canais, um a um (0,45s entre eles): o fio de cima se desenha da esquerda para a direita, o nome em laranja
    recebe um facho de luz, e a função entra logo depois. A coluna dos rótulos é mais larga ("Stories e DM")."""
    t0 = SOC_ROW0 if t0 is None else t0
    step = SOC_STEP if step is None else step
    out = ['<div class="fa-rows amb">']
    for i, (a, b) in enumerate(rows):
        d0 = t0 + i * step
        out.append(f'<div class="row" style="--d0:{f(d0)}s"><span class="cap fa-amb-nm">{H.escape(plain(a))}</span>'
                   f'<span class="body-s one fa-in" style="--d0:{f(d0 + .35)}s">{H.escape(plain(b))}</span></div>')
    out.append('</div>')
    return "".join(out)


