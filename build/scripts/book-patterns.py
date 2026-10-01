#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""A página 3 do brand book, "Padrões e movimento" (v1.1, 18/09/2026): os seis componentes de 17/09 no estado
final, um quadro 16:9 por padrão. Os quadros vêm do módulo itau_components (a mesma fonte do template e dos
decks) e vestem a camada src/04-camada.css reduzida ao estado de impressão: sem keyframes, sem os gatilhos de
.slide.visible, com o bloco @media print valendo como estado normal, tudo escopado em .pat3 (o book é estático).
Os tokens e as classes de sistema que a camada usa (.canvas, .stmt, .cap, .hl...) vêm de src/01-head.html,
copiados aqui com os mesmos valores, também escopados.

Idempotente: reescreve só o que está entre os marcadores /* pat3:css */ ... /* /pat3:css */ (comentários CSS,
no <style id="pat3-css"> do head) e <!-- pat3:frames --> ... <!-- /pat3:frames --> (na página 3). O resto da
página é texto fixo do book. Se um marcador faltar, para sem escrever.

Uso: /usr/bin/python3 scripts/book-patterns.py            (reescreve o book)
     /usr/bin/python3 scripts/book-patterns.py --check    (só confere se o book já está igual ao que geraria)
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import itau_components as IC  # noqa: E402

P16 = os.path.dirname(HERE)
WS = os.path.dirname(os.path.dirname(P16))
BOOK = os.path.join(WS, "Clientes", "Itaú", "Design System", "itau-brand-book-a4.html")
CAMADA = os.path.join(P16, "src", "04-camada.css")


# ================================================================ a camada, reduzida ao estado final
def strip_comments(css):
    return re.sub(r"/\*.*?\*/", "", css, flags=re.S)


def split_blocks(css):
    """Blocos de primeiro nível como (prelúdio, corpo), respeitando chaves aninhadas (@media, @keyframes)."""
    out, i, n = [], 0, len(css)
    while i < n:
        j = css.find("{", i)
        if j < 0:
            break
        prelude = css[i:j].strip()
        depth, k = 1, j + 1
        while k < n and depth:
            if css[k] == "{":
                depth += 1
            elif css[k] == "}":
                depth -= 1
            k += 1
        out.append((prelude, css[j + 1:k - 1]))
        i = k
    return out


def final_rules(css):
    """Da camada viva ao estado final: fora os keyframes e as regras de .slide.visible (só disparam animação);
    o que está em @media print sobe para o nível normal, na mesma ordem em que aparece (é o estado final de
    cada peça, com os !important que já tinha). Toda declaração de animation/transition cai. Cada seletor ganha
    o escopo .pat3 e .slide vira .pfr, o quadro do book."""
    rules = []
    for prelude, body in split_blocks(strip_comments(css)):
        if prelude.startswith("@keyframes"):
            continue
        if prelude.startswith("@media"):
            rules += final_rules(body)
            continue
        sels = [s.strip() for s in prelude.split(",") if s.strip() and ".visible" not in s]
        if not sels:
            continue
        decls = [d.strip() for d in body.split(";") if d.strip() and not d.strip().startswith(("animation", "transition"))]
        if not decls:
            continue
        rules.append((",".join(".pat3 " + s.replace(".slide", ".pfr") for s in sels), ";".join(decls)))
    return rules


# os tokens e as classes de sistema que a camada pressupõe, com os valores de src/01-head.html (o quadro .pfr faz o
# papel de .slide + .frame: container em cqw, 16:9, padding --m). O grifo já no estado final (bloco aberto, palavra pintada).
BASE_CSS = """
.pat3 .pfr{--m:5.2cqw;--r:.8cqw;--r-s:.4cqw;--r-l:1.25cqw;--bg:#FFFFFF;--fg:#000000;--line:#000000;--muted:#4C4C4C;--hair:rgba(0,0,0,.16);--stage:#F1F2F4;--ink:rgba(0,0,0,.06);--acc:#FF6200;--acc-fg:#FFFFFF;--azul-d:#000D3C;--e-expo:cubic-bezier(.19,1,.22,1);--e-strong:cubic-bezier(.87,0,.13,1);--e-slow:cubic-bezier(.16,1,.3,1);--t-hero:9.4cqw;--t-stmt:8cqw;--t-ttl:5.6cqw;--t-sub:2.6cqw;--t-body-l:2.3cqw;--t-body:1.75cqw;--t-body-s:1.35cqw;--t-cap:1cqw;container-type:inline-size;width:100%;aspect-ratio:16/9;position:relative;overflow:hidden;padding:var(--m);display:flex;flex-direction:column;background:var(--bg);color:var(--fg);font-family:var(--text);font-weight:400}
.pat3 .pfr.inv{background:var(--preto);--fg:#ffffff;--line:#ffffff;--muted:#ADB8B3;--hair:rgba(255,255,255,.24);--stage:rgba(255,255,255,.06);--ink:rgba(255,255,255,.1);color:var(--branco)}
.pat3 .pfr.laranja{background:var(--laranja);--fg:#ffffff;--line:#ffffff;--muted:rgba(255,255,255,.82);--hair:rgba(255,255,255,.32);--stage:rgba(255,255,255,.14);--ink:rgba(255,255,255,.16);--acc:#FFFFFF;--acc-fg:#FF6200;color:var(--branco)}
.pat3 .pfr.azul{background:var(--azul);--fg:#ffffff;--line:#ffffff;--muted:rgba(255,255,255,.72);--hair:rgba(255,255,255,.26);--stage:rgba(255,255,255,.08);--ink:rgba(255,255,255,.1);color:var(--branco)}
.pat3 .canvas{position:relative;z-index:2;flex:1;display:flex;flex-direction:column;justify-content:center;padding:5.2cqw 0 0;gap:2.4cqw}
.pat3 .pfr.bare .canvas{padding:0}
.pat3 .pfr.ctr .canvas{align-items:center;text-align:center}
.pat3 .stmt{font-family:var(--display);font-weight:700;font-size:var(--t-stmt);line-height:.96;letter-spacing:-.03em}
.pat3 .ttl{font-family:var(--display);font-weight:700;font-size:var(--t-ttl);line-height:1;letter-spacing:-.025em}
.pat3 .sub{font-size:var(--t-sub);font-weight:700;line-height:1.1;letter-spacing:-.01em}
.pat3 .body-l{font-size:var(--t-body-l);font-weight:400;line-height:1.3;letter-spacing:-.01em}
.pat3 .body{font-size:var(--t-body);font-weight:400;line-height:1.5}
.pat3 .body-s{font-size:var(--t-body-s);font-weight:400;line-height:1.55}
.pat3 .cap{font-size:var(--t-cap);font-weight:700;text-transform:uppercase;letter-spacing:.14em;line-height:1}
.pat3 .mut{color:var(--muted)}
.pat3 .hl{position:relative;display:inline-block;white-space:nowrap}
.pat3 .hl::before{content:"";position:absolute;left:-.12em;right:-.12em;top:-.02em;bottom:-.04em;background:var(--acc);border-radius:var(--r-s)}
.pat3 .hl::after{content:attr(data-w);position:absolute;left:0;top:0;color:var(--acc-fg);white-space:nowrap}
""".strip()


def scoped_css():
    css = open(CAMADA, encoding="utf-8").read().replace("{{ANATOMIA_CSS}}", "")
    body = "\n".join(f"{sel}{{{decl}}}" for sel, decl in final_rules(css))
    return ("/* gerado por scripts/book-patterns.py a partir de src/01-head.html (tokens e classes de sistema) e\n"
            "   src/04-camada.css (a camada de movimento no estado final de impressão); não editar à mão */\n"
            + BASE_CSS + "\n" + body)


# ================================================================ os seis quadros
# placeholder que nomeia o estilo (o método do template), sem dado: os nomes seguem o catálogo do build-itau.py
MOV = [("Movimento 01", "Função curta."), ("Movimento 02", "Função curta."), ("Movimento 03", "Função curta."),
       ("Movimento 04", "Função um pouco mais longa."), ("Movimento 05", "Função curta.")]
CAM = ("Camada transversal", "Legenda da camada, em uma linha.")
SINAIS = ["sinal um", "sinal dois", "sinal três", "sinal quatro"]
ASSUNTOS = ["tema um", "tema dois", "tema três", "tema quatro", "tema cinco", "tema seis", "tema sete"]
TABELA = [("Legenda", "Corpo pequeno numa linha."), ("Legenda", "Corpo pequeno numa linha, um pouco maior."),
          ("Legenda", "Corpo pequeno numa linha."), ("Legenda", "Corpo pequeno numa linha.")]
FIOS = [("Canal um", "Faz isto."), ("Canal dois", "Faz aquilo."), ("Canal três", "Faz outra coisa."),
        ("Canal quatro e cinco", "Fazem juntos."), ("Canal seis", "Fecha a lista.")]
POEMA = dict(screen=["Título do poema", "em duas linhas"],
             estrofes=[["Estrofe em três linhas,", "escrita à máquina,", "um caractere por vez."], ["Segunda estrofe,", "em duas linhas."]],
             litania=["Linha!", "Linha", "Linha!", "Linha!", "Linha (“aparte”)", "Linha!", "Linha!", "Linha", "Linha!", "Linha!"],
             veredito=["Veredito em uma linha.", "E outra."],
             prosa=["{Linha fina com o grifo}.", "Linha fina em corpo pequeno."])


def pfr(cls, inner):
    return f'<div class="pfr{(" " + cls) if cls else ""}">{inner}</div>'


def moldura():
    """Statement 06 do template: a frase centrada com o marcador, a Moldura atrás, o apoio cinza. O corpo e a
    abertura seguem a régua do módulo (0,47em por caractere; abre 12% acima de 60cqw, 20% acima de 78)."""
    parts = ["A frase centrada,", "a Moldura em volta,", "nada cruza {letra}."]
    cls = IC.body_size(parts)
    est = max(len(IC.plain(p)) for p in parts) * .47 * IC.BODY_CQW[cls]
    rs = 1.2 if est > 78 else 1.12 if est > 60 else 1.0
    br = 1.03 if rs > 1 else 1.06
    return pfr("ctr inv", IC.resonance(rs, br) + '<div class="canvas fa-voz">' + IC.marker()
               + f'<p class="{cls}">{IC.lines(parts, "1s")}</p>'
               + '<p class="fa-sup">Apoio em corpo regular cinza, mais estreito que a frase.</p></div>')


def anatomia():
    """Capa 07: título à esquerda (Statement, o acento de texto numa palavra), a anatomia à direita, slide preto e bare."""
    return pfr("bare inv", IC.anatomy() + '<div class="canvas fa-capa"><span class="cap mut">Legenda da capa · Africa Creative/™</span>'
               + f'<p class="stmt">{IC.lines(["Statement", "da [capa]", "em linhas."])}</p>'
               + f'<p class="body-l">{IC.lines(["Corpo grande em peso regular,", "em duas linhas fixas."])}</p></div>')


def orbitas():
    """Título 04: título lateral com o grifo duplo, apoio em três linhas, as órbitas à direita."""
    return pfr("", '<div class="fa-orb2-tx">'
               + f'<p class="fa-orb2-ttl">{IC.lines(["{Título lateral}", "em três linhas curtas", "com o {grifo duplo}."], "1.1s")}</p>'
               + f'<p class="fa-sup left fa-orb2-sup">{IC.lines(["Apoio em três linhas fixas,", "corpo pequeno, cinza, alinhado à esquerda,", "na altura do diagrama."])}</p></div>'
               + f'<div class="fa-orb2" aria-hidden="true">{IC.orbita(SINAIS, ASSUNTOS, "ID")}</div>')


def poema():
    """Conteúdo 05: a página dupla, bare, sem Moldura."""
    return pfr("bare", '<div class="canvas fa-po">' + IC.poema(**POEMA) + '</div>')


def momento():
    """Sistema 02: o detalhamento à esquerda e o ecossistema pronto com a faixa do movimento acesa."""
    return pfr("inv", '<div class="fa-eco-tx pilar"><p class="cap fa-eco-kk">Legenda do momento</p>'
               + f'<p class="fa-eco-ttl">{IC.lines(["Movimento 02", "faz {isto}."], "1.1s")}</p>'
               + '<p class="body fa-eco-inc one">Incipit em corpo regular, numa linha só.</p>'
               + '<p class="fa-def one">Definição em corpo pequeno cinza, numa linha só.</p>'
               + IC.rows_html(TABELA, 1.2, .18) + '</div>'
               + f'<div class="fa-eco pronto" aria-hidden="true">{IC.ecossistema("bk-momento", MOV, lit=1)}</div>'
               + IC.eco_sa(False, CAM))


def tabela():
    """Sistema 03: a tabela que se destaca linha a linha à esquerda; à direita a camada (só linhas e pontos laranja)."""
    return pfr("inv", '<div class="fa-eco-tx pilar"><p class="cap fa-eco-kk">Legenda da camada:</p>'
               + f'<p class="fa-eco-ttl">{IC.lines(["Título lateral", "em três linhas curtas,", "com o {grifo}."], "1.1s")}</p>'
               + f'<p class="body fa-eco-inc">{IC.lines(["Subtítulo em corpo regular,", "em três linhas fixas,", "entre o título e a tabela."])}</p>'
               + IC.amb_rows(FIOS) + '</div>'
               + f'<div class="fa-eco pronto" aria-hidden="true">{IC.ecossistema("bk-camada", MOV, lit=len(IC.ECO_R), social=True)}</div>'
               + IC.eco_sa(False, CAM))


# legenda de cada quadro: nome, o que faz numa linha, o loop e a curva, a origem (criação da Africa, 17/09/2026,
# com a referência real da especificação; onde não há referência externa, diz que não há)
CELLS = [
    (moldura, "A Moldura",
     "Seis contornos da pedra, tom sobre tom, abrem um palco em volta da frase. Nada cruza letra.",
     "faResBreath, 6s, escala 1 a 1,06 (3% quando aberta). Entra com faResIn, 1,6s, na entrada lenta cubic-bezier(.16,1,.3,1).",
     "Criação da Africa, 17/09/2026. Derivada da opção A do burst de 17/09: a ressonância da capa levada às frases."),
    (anatomia, "A anatomia da capa",
     "O quadrado de quinas redondas vira a pedra, quatro contornos respiram em onda e, por último, o logo chega.",
     "faAnaRes, 3,6s, escala 1,10 em onda; faAnaPulse, 3,6s, 3%. O morph faAnaForm dura 1,5s na entrada lenta cubic-bezier(.16,1,.3,1).",
     "Criação da Africa, 17/09/2026. Derivada do filme da Pentagram para a identidade do Itaú (2024), pentagram.com/work/banco-itau, trecho 6,1s a 7,0s do sizzle."),
    (orbitas, "As órbitas",
     "A pedra-coração bate duas vezes. Cada batida congela numa faixa de Matéria: os sinais na primeira, os assuntos na segunda.",
     "Nenhum. Quando a segunda faixa congela, acabou. faHeart 1,4s ease-out; faOrbFreeze 0,8s na curva vivid cubic-bezier(.22,1,.36,1).",
     "Criação da Africa, 17/09/2026. Derivada do One Sheeter do Yummly (Creative Pack 2021, p. 145 a 151): faixas de matéria depositadas."),
    (poema, "O poema em máquina de escrever",
     "Página dupla. Cada linha se escreve em passos de um caractere, na ordem de leitura. O grifo por último.",
     "Nenhum. faTw em steps(n): 22ms por caractere (mínimo 0,25s), 0,18s entre linhas, 0,5s entre estrofes.",
     "Criação da Africa, 17/09/2026, no slide 6 do deck Itaú fim de ano V2. Sem referência externa."),
    (momento, "O ecossistema, no momento",
     "O diagrama entra pronto, o núcleo bate uma vez e a faixa do movimento se acende a partir do nome. Só os pontos da linha ficam laranja.",
     "faEcoSpin (16, 22, 29, 37 e 46s por volta), faEcoTwinkle 1,9s, faEcoBreath 5s. A batida faEcoPulse 1,2s na curva vivid; a faixa em faDraw 1,3s no expo out cubic-bezier(.19,1,.22,1).",
     "Criação da Africa, 17/09/2026. Derivada das prévias do 21st.dev (o chronos engine), lidas quadro a quadro, com o duplo diamante do Africa Decoded como régua."),
    (tabela, "A tabela que se destaca",
     "Linha a linha, a cada 0,45s: o fio se desenha, o nome em laranja recebe o facho, o corpo entra. Ao lado, a camada: só linhas e pontos laranja.",
     "Na tabela, nenhum; no diagrama, faEcoSpin e faEcoTwinkle. faAmbLine 0,8s no expo out cubic-bezier(.19,1,.22,1); faEcoShine 1,3s ease-in-out.",
     "Criação da Africa, 17/09/2026, com o ecossistema no deck Itaú fim de ano V2 (Sistema 03 do template). Sem referência externa."),
]


def frames_html():
    cells = []
    for fn, nome, faz, loop, origem in CELLS:
        cells.append(f'<div class="pcell">{fn()}<p class="pcap"><b>{nome}</b>{faz}'
                     f'<span><span class="k">Loop e curva</span> {loop}</span>'
                     f'<span><span class="k">Origem</span> {origem}</span></p></div>')
    return '<div class="pgrid pat3">' + "".join(cells) + '</div>'


# ================================================================ a injeção
MARK = {"css": ("/* pat3:css */", "/* /pat3:css */"),            # dentro do <style>: comentário CSS (um comentário HTML ali
        "frames": ("<!-- pat3:frames -->", "<!-- /pat3:frames -->")}   # deixa o texto do marcador solto e engole a regra seguinte)


def inject(html, tag, content):
    a, b = MARK[tag]
    if html.count(a) != 1 or html.count(b) != 1:
        sys.exit(f"marcador pat3:{tag} ausente ou duplicado no book: nada escrito")
    i, j = html.index(a) + len(a), html.index(b)
    return html[:i] + "\n" + content + "\n" + html[j:]


def main():
    html = open(BOOK, encoding="utf-8").read()
    out = inject(inject(html, "css", scoped_css()), "frames", frames_html())
    # conferências antes de tocar no arquivo
    for bad, why in [("{{", "placeholder de build"), ("—", "travessão"), ("–", "meia-risca"),
                     ("drop-shadow", "sombra difusa"), ("text-shadow", "sombra de texto"), ("@keyframes", "keyframe na página estática")]:
        gen = out[out.index(MARK["css"][0]):out.index(MARK["css"][1])] + out[out.index(MARK["frames"][0]):out.index(MARK["frames"][1])]
        if bad in gen:
            sys.exit(f"o trecho gerado contém {why} ({bad!r}): nada escrito")
    if len(re.findall(r'<div class="page"', out)) != 3:
        sys.exit("o book não tem 3 páginas: nada escrito")
    if "--check" in sys.argv:
        print("book igual ao gerado" if out == html else "book DIFERENTE do gerado")
        sys.exit(0 if out == html else 1)
    if out == html:
        print("book já estava igual ao gerado (nada a escrever)")
    else:
        open(BOOK, "w", encoding="utf-8").write(out)
        print(f"book reescrito · {len(out)//1024} KB")
    print(f"{len(CELLS)} quadros · {len(final_rules(open(CAMADA, encoding='utf-8').read().replace('{{ANATOMIA_CSS}}', '')))} regras da camada no estado final")
    print(BOOK)


if __name__ == "__main__":
    main()
