#!/usr/bin/env python3
# Bateria de invariantes do sistema Itaú × Africa.
# Lê o PRODUTO FINAL e confere contra os tokens e o dossiê. Não reusa o código
# que gerou os arquivos: o build injeta, o check mede.
#
# Duas zonas no conteúdo, como no verificador da Africa:
#   - zona normativa: tudo que o sistema AFIRMA. Regra dura.
#   - zona cerca (fence): os trechos que existem para dizer "isto é errado" ou
#     "isto não foi verificado". No JSON são chaves nomeadas; no HTML, data-fence="1".
import json, os, re, sys, glob

WS = "/Users/brunosimoes/Desktop/MY WORKSPACE (Claude)"
CL = os.path.join(WS, "Clientes", "Itaú")
DS = os.path.join(CL, "Design System")
MS = os.path.join(CL, "Master Slides")
P16 = os.path.join(WS, "Projetos", "P16-itau-design-system")

MARK_PATH = ("M66.05,62.35l-15.01,19.56h-11.48l-10.34-39.32H9.86L0,19.69,21.3,0l17.69,6.93,"
             "13.78.8,11.69,18.77,10.2,4.71-9.51,19.13.89,12ZM71.21,65.49l-6.58,8.53,6.93,"
             "3.02,3.2-8.62-3.55-2.93Z")

# a paleta do Itaú (tokens_idl/varejo.css) + o gradiente da Africa + cores do logo
WHITELIST = {c.lower() for c in [
    "FF6200", "E55800", "000066", "000D3C", "FFFFFF", "000000", "4C4C4C", "5D636F",
    "ADB8B3", "CFD1D3", "F1F2F4", "E3E5E8", "3B3B3B", "999999",
    "002766", "6E6E6E", "0131FF", "FFBA00", "BD0071", "008717",
    "FFCC00", "CC0000", "001FBD", "0B5B38",
    "348FFE", "8C6BE1", "FF3CB9", "FF7842",
]}
BANNED_IN_HTML = {"ff636b": "coral da Africa", "efefeb": "bone da Africa", "ec7000": "laranja digital antigo"}

JSON_FENCE_KEYS = {"namingRule", "notVerified", "prohibitions", "whatStaysOut", "legacyDigitalOrange",
                   "fallbackDecision", "note", "derivation", "provenance", "verify", "rule", "source",
                   "colorNote", "colorNoteSource", "since_source", "works_source", "meaningSource",
                   "symbolSource", "contrastSource", "itauSpacingNote", "measurement", "why", "status"}

FORBIDDEN = re.compile(
    r"(cannes|le[oõ]es?\b|effie|grand\s*prix|fundad[ao]\s+em|desde\s+19\d\d|"
    r"funcion[aá]rios|colaboradores|market\s*share|[\w.+-]+@[\w-]+\.[\w.]{2,})", re.I)
ACCENT = re.compile(r"[ÁáÀà]fric")
MANIFESTO_FRAG = "para nunca deixar de ser a"

fails, warns, oks = [], [], []
ok, fail, warn = oks.append, fails.append, warns.append


def json_strings(node, key=None, fenced=False):
    if isinstance(node, dict):
        for k, v in node.items():
            yield from json_strings(v, k, fenced or k in JSON_FENCE_KEYS)
    elif isinstance(node, list):
        for v in node:
            yield from json_strings(v, key, fenced)
    elif isinstance(node, str):
        yield node, fenced


def html_zones(src):
    fence = []
    def grab(m):
        fence.append(m.group(0))
        return " "
    tag = r'<(\w+)[^>]*\bdata-fence="1"[^>]*>.*?</\1>'
    return re.sub(tag, grab, src, flags=re.S), "".join(fence)


def textfiles():
    out = []
    for base in [DS, MS]:
        for root, _, names in os.walk(base):
            for n in names:
                if n.lower().endswith((".html", ".json", ".svg", ".css", ".md")):
                    out.append(os.path.join(root, n))
    return sorted(out)


def html_files():
    return sorted(glob.glob(os.path.join(DS, "*.html")) + glob.glob(os.path.join(MS, "*.html")))


def nobase64(s):
    return re.sub(r"data:font/woff2;base64,[A-Za-z0-9+/=]+", "FONT", s)


# ---------------------------------------------------------------- 1. estrutura
for p in ["itau-brand-tokens.json", "itau-design-system.html", "itau-brand-book-a4.html",
          "itau-brand-book-a4.pdf", "assets/itau-logo-2023-commons.svg", "assets/itau-logo-2023-commons.png",
          "assets/itau-pedra.svg", "assets/africa-mark.svg"]:
    (ok if os.path.exists(os.path.join(DS, p)) else fail)(f"existe: Design System/{p}")
for p in ["itau-slides-template.html", "README.md", "context.md"]:
    (ok if os.path.exists(os.path.join(MS, p)) else fail)(f"existe: Master Slides/{p}")
for p in ["context.md", "session-log.md", "dossie-itau.md", "fontes/itau-tokens-varejo-wayback-2025.css",
          "src/01-head.html", "src/02-body.html", "src/03-tail.html", "scripts/build-itau.py"]:
    (ok if os.path.exists(os.path.join(P16, p)) else fail)(f"existe: P16/{p}")
wf = sorted(os.path.basename(f) for f in glob.glob(os.path.join(DS, "fonts", "*.woff2")))
(ok if wf == ["Figtree-VF-latin-ext.woff2", "Figtree-VF-latin.woff2", "MiletusGrotesk-Medium.woff2", "PPPangaia-Light.woff2"]
 else fail)(f"4 woff2 em fonts/: Figtree VF x2, Miletus Medium, Pangaia Light (achou {wf})")

# ---------------------------------------------------------------- 2. os tokens contra a fonte primária
tok = None
try:
    tok = json.load(open(os.path.join(DS, "itau-brand-tokens.json"), encoding="utf-8"))
    ok("itau-brand-tokens.json parseia")
except Exception as e:
    fail(f"JSON inválido: {e}")
site = os.path.join(P16, "fontes", "itau-tokens-varejo-wayback-2025.css")
if tok and os.path.exists(site):
    css = open(site, encoding="utf-8", errors="ignore").read()
    def site_has(var, val):
        return re.search(re.escape(var) + r"\s*:\s*" + re.escape(val) + r"(?![0-9A-Za-z])", css, re.I) is not None
    pairs = [("--ids_color_bg_brand_primary", tok["colors"]["laranja"]["hex"]),
             ("--ids_color_action_primary_variant", tok["colors"]["laranjaEscuro"]["hex"]),
             ("--ids_color_bg_brand_secondary", tok["colors"]["azul"]["hex"]),
             ("--ids_color_text_body_02", tok["colors"]["cinzaTexto"]["hex"]),
             ("--ids_color_bg_variant_01", tok["colors"]["superficie1"]["hex"]),
             ("--ids_color_bg_variant_02", tok["colors"]["superficie2"]["hex"]),
             ("--ids_color_border_medium", tok["colors"]["cinzaMedio"]["hex"]),
             ("--ids_color_border_soft", tok["colors"]["cinzaSuave"]["hex"])]
    bad = [(v, h) for v, h in pairs if not site_has(v, h)]
    (ok if not bad else fail)(f"todo hex do Itaú nos tokens bate com o CSS oficial do site ({len(pairs)} pares; fora: {bad})")
    (ok if re.search(r'"Itau Display"', css) and re.search(r'"Itau Text"', css) else fail)(
        "o CSS oficial nomeia Itau Display e Itau Text")
    (ok if tok["typography"]["voice"]["family"] == "Itau Display" and tok["typography"]["text"]["family"] == "Itau Text"
     else fail)("tokens: voz = Itau Display, texto = Itau Text")
    (ok if site_has("--ids_motion_easing_effective_decelerate_02", "cubic-bezier(0.19, 1, 0.22, 1)") else fail)(
        "o CSS oficial traz cubic-bezier(0.19,1,0.22,1): a curva da Africa é a do Itaú")
    (ok if tok["colors"]["legacyDigitalOrange"]["hex"] == "#EC7000" else fail)("tokens registram o #EC7000 como legado, não como cor")

# ---------------------------------------------------------------- 3. path do mark da Africa
found = 0
for f in textfiles():
    s = open(f, encoding="utf-8", errors="ignore").read()
    for d in re.findall(r'\bd="(M66[^"]*)"', s) + re.findall(r'"path":\s*"(M66[^"]*)"', s):
        found += 1
        if d != MARK_PATH:
            fail(f"path do mark DIVERGENTE em {os.path.relpath(f, CL)}")
(ok if found else fail)(f"path do mark da Africa idêntico em {found} ocorrência(s)")

# ---------------------------------------------------------------- 4. grafia e afirmações
if tok:
    acc = [t[:60] for t, fen in json_strings(tok) if not fen and ACCENT.search(t)]
    (ok if not acc else fail)(f"JSON zona normativa sem 'África' (achou {acc})")
    inv = [(t[:60], FORBIDDEN.search(t).group(0)) for t, fen in json_strings(tok) if not fen and FORBIDDEN.search(t)]
    (ok if not inv else fail)(f"JSON zona normativa sem afirmação não verificada (achou {inv})")
for f in html_files():
    rel = os.path.basename(f)
    norm, _ = html_zones(nobase64(open(f, encoding="utf-8").read()))
    a = ACCENT.findall(norm)
    (ok if not a else fail)(f"{rel}: zona normativa sem 'África' (achou {len(a)})")
    i = FORBIDDEN.findall(norm)
    (ok if not i else fail)(f"{rel}: zona normativa sem afirmação não verificada ({i[:5]})")
    p = [m for m in re.findall(r"[^.]{0,300}premiad[^.]{0,300}\.", norm, re.I)]
    (ok if not p else fail)(f"{rel}: sem 'premiad*' ({[x[:50] for x in p]})")

# ---------------------------------------------------------------- 5. paleta
# só a zona normativa conta: a cerca (data-fence no HTML, chaves nomeadas no JSON) cita coral,
# bone e o laranja antigo justamente para dizer que não entram. Os .md são prosa e fazem o mesmo.
bad = {}
for f in textfiles():
    if f.endswith(".md"):
        continue
    if f.endswith(".json") and tok:
        s = "\n".join(t for t, fen in json_strings(tok) if not fen)
    elif f.endswith(".html"):
        s, _ = html_zones(nobase64(open(f, encoding="utf-8").read()))
    else:
        s = open(f, encoding="utf-8", errors="ignore").read()
    for h in re.findall(r"#([0-9a-fA-F]{6})\b", s):
        if h.lower() not in WHITELIST:
            bad.setdefault(os.path.relpath(f, CL), set()).add("#" + h)
(ok if not bad else fail)(f"todo hex da zona normativa pertence à paleta ({ {k: sorted(v) for k, v in bad.items()} })")
for f in html_files():
    s, _ = html_zones(nobase64(open(f, encoding="utf-8").read()))
    s = s.lower()
    hits = [n for h, n in BANNED_IN_HTML.items() if h in s]
    (ok if not hits else fail)(f"{os.path.basename(f)}: zona normativa sem coral, bone ou laranja antigo ({hits})")

# ---------------------------------------------------------------- 6. gradiente na ordem
for f in textfiles():
    s = nobase64(open(f, encoding="utf-8", errors="ignore").read()).upper()
    if "348FFE" not in s:
        continue
    seq = "".join(h for h in re.findall(r"#([0-9A-F]{6})", s) if h in {"348FFE", "8C6BE1", "FF3CB9", "FF7842"})
    n = seq.count("348FFE8C6BE1FF3CB9FF7842")
    (ok if n else fail)(f"{os.path.relpath(f, CL)}: {n} gradiente(s) na ordem azul>violeta>magenta>coral")

# ---------------------------------------------------------------- 7. autonomia dos HTML
for f in html_files():
    s = open(f, encoding="utf-8").read()
    rel = os.path.basename(f)
    ext = re.findall(r'(?:href|src)="(https?://[^"]+)"', s)
    (ok if not ext else fail)(f"{rel}: zero recurso externo ({ext[:3]})")
    miss = [p for p in re.findall(r'url\((?:"|\')?([^"\')]+\.woff2)', s)
            if not os.path.exists(os.path.join(os.path.dirname(f), p))]
    (ok if not miss else fail)(f"{rel}: todo woff2 referenciado existe (faltam {miss})")
    for pat, nome in [(r"<canvas", "canvas"), (r"\bthree\b", "three.js"), (r"importmap", "importmap"),
                      (r"mix-blend-mode", "mix-blend-mode")]:
        n = len(re.findall(pat, nobase64(s), re.I))
        (ok if n == 0 else fail)(f"{rel}: sem {nome} (achou {n})")
    # sombra difusa: só o halo do brilho da legenda do sistema (faEcoGlow), exceção declarada em 17/09
    sem_glow = re.sub(r"@keyframes faEcoGlow\{[^}]*\}[^}]*\}", "", nobase64(s))
    n = len(re.findall(r"text-shadow|drop-shadow", sem_glow, re.I))
    (ok if n == 0 else fail)(f"{rel}: sem sombra difusa fora do brilho da legenda do sistema (achou {n})")

# ---------------------------------------------------------------- 8. design system e brand book
ds_html = os.path.join(DS, "itau-design-system.html")
if os.path.exists(ds_html):
    s = open(ds_html, encoding="utf-8").read()
    secs = sorted(set(re.findall(r">0([1-9])\s*—", s)))
    (ok if len(secs) == 9 else fail)(f"DS: 9 seções numeradas 01–09 (a 09, Padrões animados, desde 18/09) (achou {secs})")
    for e in ["cubic-bezier(.19,1,.22,1)", "cubic-bezier(.87,0,.13,1)", "cubic-bezier(.16,1,.3,1)"]:
        (ok if e in s.replace(" ", "") else fail)(f"DS: easing {e} presente")
    (ok if 'data-mode="light"' in s and 'id="bw"' in s else fail)("DS: os dois modos e o toggle P/B")
    (ok if "#FF6200" in s and "Itau Display" in s and "Figtree" in s else fail)("DS: laranja oficial, Itau Display e o fallback declarados")
    (ok if len(re.findall(r'data-fence="1"', s)) >= 2 else fail)("DS: ao menos 2 blocos de cerca (o que não fazer, o que não foi verificado)")
bb_html = os.path.join(DS, "itau-brand-book-a4.html")
if os.path.exists(bb_html):
    s = open(bb_html, encoding="utf-8").read()
    (ok if len(re.findall(r'<div class="page"', s)) == 3 else fail)("book: 3 páginas A4 (a terceira, padrões e movimento, desde 18/09)")
    (ok if "@page{size:A4" in s.replace(" ", "") else fail)("book: @page A4")
bb_pdf = os.path.join(DS, "itau-brand-book-a4.pdf")
if os.path.exists(bb_pdf):
    try:
        import fitz
        d = fitz.open(bb_pdf)
        (ok if len(d) == 3 else fail)(f"book PDF: 3 páginas (achou {len(d)})")
        w, h = d[0].rect.width, d[0].rect.height
        (ok if abs(w - 595.3) < 2 and abs(h - 841.9) < 2 else fail)(f"book PDF: página A4 ({w:.0f}x{h:.0f}pt)")
    except ImportError:
        warn("pymupdf ausente: PDF do book não conferido (rodar com /usr/bin/python3)")

# ---------------------------------------------------------------- 9. template de slides
ST = os.path.join(MS, "itau-slides-template.html")
if os.path.exists(ST):
    s = open(ST, encoding="utf-8").read()
    nb = len(re.findall(r"data:font/woff2;base64,", s))
    (ok if nb == 4 else fail)(f"slides: 4 fontes embutidas em base64 (achou {nb})")
    rel = re.findall(r'url\((?:"|\')?(fonts/[^"\')]+)', s)
    (ok if not rel else fail)(f"slides: zero fonte por caminho relativo (achou {rel})")
    st_css = "\n".join(re.findall(r"<style>(.*?)</style>", s, re.S))
    body = re.sub(r"<style>.*?</style>", "", s, flags=re.S)
    js = "\n".join(re.findall(r"<script>(.*?)</script>", s, re.S))
    (ok if "{{" not in body else fail)("slides: nenhum placeholder de build sobrou")

    sl = re.findall(r'<section class="slide([^"]*)"([^>]*)>', body)
    (ok if len(sl) >= 40 else fail)(f"slides: ao menos 40 slides (achou {len(sl)})")
    semt = [i for i, (c, a) in enumerate(sl) if 'data-title="' not in a]
    semn = [i for i, (c, a) in enumerate(sl) if 'data-notes="' not in a]
    (ok if not semt else fail)(f"slides: todo slide tem data-title (falta em {semt})")
    (ok if not semn else fail)(f"slides: todo slide tem data-notes, o roteiro fora da tela (falta em {semn})")
    (ok if sl and 'data-title="Marca"' in sl[0][1] else fail)("slides: o primeiro slide é a marca (os dois logos)")
    (ok if len(sl) > 1 and "s-closing" in sl[-2][0] else fail)("slides: o fechamento obrigatório é o penúltimo")
    (ok if sl and 'data-title="Slogan"' in sl[-1][1] else fail)("slides: o slogan fecha o deck")
    (ok if MANIFESTO_FRAG in s else fail)("slides: o fechamento traz a frase oficial do manifesto da Africa")
    (ok if "A agência das marcas" in body else fail)("slides: o slogan da Africa está no último slide")

    for pat, nome in [(r"cubic-bezier\(\.19,1,\.22,1\)", "expo out / decelerate_02"),
                      (r"cubic-bezier\(\.87,0,\.13,1\)", "in out forte"),
                      (r"cubic-bezier\(\.16,1,\.3,1\)", "entrada lenta")]:
        (ok if re.search(pat, st_css) else fail)(f"slides: easing {nome} presente")
    for pat, nome in [(r'data-mode="light"', "os dois modos"), (r"@media print", "bloco de impressão"),
                      (r"scroll-snap-type", "scroll-snap"), (r"container-type:\s*inline-size", "escala por cqw"),
                      (r"classList\.remove\('visible'\)", "observer que re-anima na revisita")]:
        (ok if re.search(pat, s) else fail)(f"slides: {nome}")

    kf = dict(re.findall(r"@keyframes\s+([A-Za-z0-9_-]+)\s*\{((?:[^{}]|\{[^{}]*\})*)\}", st_css))
    fl = kf.get("afFloat")
    (ok if fl and not re.search(r"rotate|scale|skew", fl) else fail)(f"slides: afFloat só translada (corpo: {fl})")
    # a lista fechada de keyframes (17/09): os dois do sistema e os da camada de movimento, cada um com um dono
    KF = {"afFloat", "spin",
          "faIn", "faShow", "faDraw", "faPop", "faPulse",                                   # a língua do movimento
          "faAnaForm", "faAnaPulse", "faAnaRingIn", "faAnaRes",                             # a anatomia da capa
          "faResIn", "faResBreath",                                                         # a Moldura
          "faTw",                                                                            # a máquina de escrever
          "faOrbIn", "faHeart", "faOrbFreeze",                                               # as órbitas
          "faEcoIn", "faEcoBreath", "faEcoPulse", "faEcoRing", "faEcoLb", "faEcoSpin",     # o ecossistema
          "faEcoTwinkle", "faEcoGlow", "faEcoShine", "faEcoNmOn", "faAmbLine"}
    (ok if set(kf) == KF else fail)(f"slides: a lista fechada de keyframes (sobrando {sorted(set(kf) - KF)}, faltando {sorted(KF - set(kf))})")
    loops = {re.search(r"\b(fa\w+)\b", a).group(1) for decl in re.findall(r"animation:([^;}]+)", st_css) for a in decl.split(",") if "infinite" in a and re.search(r"\b(fa\w+)\b", a)}
    (ok if loops <= {"faAnaPulse", "faAnaRes", "faResBreath", "faEcoBreath", "faEcoSpin", "faEcoTwinkle"} else fail)(f"slides: em loop só o que a biblioteca de movimento permite ({sorted(loops)})")
    gira = [k for k, v in kf.items() if "rotate" in v and k not in ("spin", "faEcoSpin", "faEcoLb")]
    (ok if not gira else fail)(f"slides: nada gira além do selo e das órbitas dos pontos ({gira})")

    # a grade da Africa, herdada sem alteração
    for tk, val in [("--col", "6cqw"), ("--gutter", "1.6cqw"), ("--field", "4cqw"), ("--u", ".8cqw"), ("--m", "5.2cqw")]:
        (ok if re.search(re.escape(tk) + r"\s*:\s*" + re.escape(val), st_css) else fail)(f"slides: token de grade {tk} = {val}")
    spans = {int(n): float(w) for n, w in re.findall(r"\.sp(\d+)\{width:([\d.]+)cqw\}", st_css)}
    ruins = {n: w for n, w in spans.items() if abs(w - (7.6 * n - 1.6)) > .001}
    (ok if spans and not ruins else fail)(f"slides: todo span obedece w(n)=7.6n-1.6 ({len(spans)} spans, fora: {ruins})")
    # as quinas do Itaú
    for tk, val in [("--r", ".8cqw"), ("--r-s", ".4cqw"), ("--r-l", "1.25cqw")]:
        (ok if re.search(re.escape(tk) + r"\s*:\s*" + re.escape(val) + r"\s*;", st_css) else fail)(f"slides: token de quina {tk} = {val}")
    (ok if re.search(r"\.img\{[^}]*border-radius:var\(--r\)", st_css) else fail)("slides: o marcador de imagem leva a quina do Itaú")
    (ok if re.search(r"\.bars \.tr\{[^}]*\}", st_css) and "border-radius" not in re.search(r"\.bars \.tr\{[^}]*\}", st_css).group(0) else fail)(
        "slides: a barra de dado fica reta (regra da Africa)")

    # tipografia: a voz é Display 700, o número é Display 300, o texto é Text 400
    for sel in [".stmt", ".ttl", ".hero"]:
        (ok if re.search(re.escape(sel) + r"\{font-family:var\(--display\);font-weight:700", st_css) else fail)(
            f"slides: {sel} usa Itau Display Bold")
    (ok if re.search(r"\.num\{font-family:var\(--display\);[^}]*font-weight:300", st_css) else fail)("slides: .num usa Display Light")
    (ok if re.search(r"body\{[^}]*font-family:var\(--text\);font-weight:400", st_css) else fail)("slides: o corpo usa Itau Text Regular")
    (ok if re.search(r'--display:"Itau Display","Figtree"', st_css) and re.search(r'--text:"Itau Text","Figtree"', st_css) else fail)(
        "slides: font stack declara as famílias do Itaú primeiro e a Figtree depois")
    (ok if re.search(r"\.cap\{[^}]*font-weight:700;text-transform:uppercase", st_css) else fail)("slides: legenda em Bold miúdo caixa alta")
    (ok if re.search(r"\.pg\{font-family:var\(--pangaia\)", st_css) and "class=\"pg" in body else fail)("slides: a Pangaia existe e só entra pelo .pg")
    pg_where = [t for c, a in sl for t in re.findall(r'data-title="([^"]+)"', a)]
    pg_secs = re.findall(r'<section class="slide[^"]*"[^>]*data-title="([^"]+)"[^>]*>(.*?)</section>', body, re.S)
    uses_pg = [t for t, b in pg_secs if 'class="pg' in b]
    (ok if set(uses_pg) == {"Fechamento", "Slogan"} else fail)(f"slides: Pangaia só no fechamento e no slogan (achou {uses_pg})")
    (ok if "v3-" not in s and "preserve-3d" not in st_css else fail)("slides: sem peça de Volume da Africa (nada de .v3-, nada de 3D)")

    # catálogo · o método da GUT
    titles = re.findall(r'data-title="([^"]+)"', body)
    secoes = {t.split(" · ")[1] for t in titles if t.startswith("Seção · ")}
    SECOES = {"Estilos", "Capas", "Statement", "Título", "Conteúdo", "Imagens", "Dados", "Sistema"}
    (ok if secoes == SECOES else fail)(f"slides: as 8 seções editáveis presentes (faltam {SECOES - secoes})")
    variantes = {}
    for t in titles:
        m = re.match(r"(Capa|Statement|Título|Conteúdo|Imagens|Dados|Sistema) 0(\d)$", t)
        if m:
            variantes[m.group(1)] = variantes.get(m.group(1), 0) + 1
    fracas = {k: v for k, v in variantes.items() if v < 2}
    (ok if len(variantes) == 7 and not fracas else fail)(f"slides: toda família editável tem ao menos 2 variações ({variantes})")
    (ok if variantes.get("Sistema", 0) == 3 else fail)(f"slides: o sistema tem os três estágios, nasce, momento e camada (achou {variantes.get('Sistema', 0)})")
    (ok if variantes.get("Capa", 0) >= 6 else fail)(f"slides: ao menos 6 capas (achou {variantes.get('Capa', 0)})")
    (ok if variantes.get("Dados", 0) >= 7 else fail)(f"slides: ao menos 7 modelos de dados (achou {variantes.get('Dados', 0)})")
    biblio = {t.split(" · ")[1] for t in titles if t.startswith("Biblioteca · ")}
    (ok if biblio == {"Marca", "Pedra", "Paleta", "Movimento"} else fail)(f"slides: as 4 folhas de biblioteca: marca, pedra, paleta, movimento ({biblio})")
    for nome in ["Marca", "Tipografia", "A regra", "Estilos · especimen"]:
        (ok if nome in titles else fail)(f"slides: slide do sistema '{nome}' presente")
    for estilo in ["Statement lorem ipsum", "Título 02 lorem", "Corpo regular", "Corpo pequeno", "Corpo grande", "Subtítulo", "Legenda"]:
        (ok if estilo in body else fail)(f"slides: placeholder que nomeia o estilo: '{estilo}'")
    for cls in ["laranja", "inv", "azul"]:
        (ok if re.search(r'<section class="slide[^"]*\b' + cls + r'\b[^"]*"[^>]*data-title="Capa', body) else fail)(f"slides: capa com fundo {cls}")
    (ok if re.search(r'<section class="slide[^"]*"[^>]*data-title="Capa 06"[^>]*>(?:(?!</section>).)*class="img win', body, re.S) else fail)(
        "slides: a capa 06 usa a janela da pedra")

    # seção editável = laranja, sem cabeçalho, marcada pela pedra branca
    secs = [(c, a) for c, a in sl if 'data-title="Seção' in a]
    (ok if secs and all("sec" in c and "bare" in c and "laranja" in c for c, a in secs) else fail)(
        "slides: toda seção editável é laranja, sem cabeçalho, com a pedra branca")
    (ok if len(re.findall(r'class="pedra-sq', body)) == len(secs) else fail)("slides: uma pedra branca por seção")
    laranjas = [i for i, (c, a) in enumerate(sl) if "laranja" in c]
    adj = [i for i in laranjas if i + 1 in laranjas]
    (ok if not adj else fail)(f"slides: nunca dois slides laranja adjacentes no template (adjacentes em {adj})")

    # a pedra e o logo
    (ok if 'id="pedra"' in s and 'id="pedra-clip"' in s and 'clipPathUnits="objectBoundingBox"' in s else fail)(
        "slides: a pedra existe como símbolo e como clipPath escalável")
    n_itau_paths = len(re.findall(r'<symbol id="itau"[^>]*>(?:(?!</symbol>).)*</symbol>', s, re.S))
    sym = re.search(r'<symbol id="itau"[^>]*>(.*?)</symbol>', s, re.S)
    (ok if sym and len(re.findall(r"<path", sym.group(1))) == 2 else fail)("slides: o logo do Itaú é o símbolo com os 2 paths do vetor")
    logo_on_color = [t for t, b in pg_secs if 'href="#itau"' in b and t in {
        t2 for c2, a2 in sl for t2 in re.findall(r'data-title="([^"]+)"', a2) if re.search(r"\b(laranja|inv|azul)\b", c2)}]
    # exceções declaradas (17/09): a anatomia da capa (Capa 07) e o núcleo do ecossistema (Sistema 01 a 03) levam o logo sobre preto
    EXC_LOGO = {"Capa 07", "Sistema 01", "Sistema 02", "Sistema 03"}
    fora = [t for t in logo_on_color if t not in EXC_LOGO]
    (ok if not fora else fail)(f"slides: o logo do Itaú só sobre branco, salvo as exceções declaradas (achou sobre cor em {fora})")
    (ok if set(logo_on_color) == EXC_LOGO else fail)(f"slides: as quatro exceções do logo sobre preto estão no catálogo ({sorted(logo_on_color)})")
    mark_loose = [t for t, b in pg_secs if re.search(r'href="#mark(-g)?"', b) and t not in {"Marca", "Biblioteca · Marca", "Fechamento"}]
    (ok if not mark_loose else fail)(f"slides: o mark da Africa só dentro do selo (solto em {mark_loose})")
    (ok if "mkp" not in body and 'class="bullet' not in body and ".bullet" not in st_css else fail)("slides: nenhum mark como marcador")

    # o cabeçalho e a UI fixa
    (ok if "hseal" in js and "ring-hd" in js and 'class="mg"' in js and 'class="mf"' in js else fail)(
        "slides: o cabeçalho injetado é o selo com os dois miolos (gradiente e chapado)")
    (ok if re.search(r"\.slide\.laranja \.hseal \.mf[^{]*\{display:block\}", st_css) else fail)("slides: sobre laranja o selo mostra o mark chapado")
    (ok if re.search(r"\.hd\{[^}]*left:1\.6cqw;[^}]*top:\.9cqw", st_css) else fail)("slides: o selo no canto superior esquerdo, na linha dos botões")
    (ok if re.search(r"\.hseal text\{[^}]*fill:var\(--fg\)", st_css) else fail)("slides: o anel do selo segue a cor do texto do slide")
    (ok if 'class="pg"' not in st_css and "Pág." not in s and "data-cap" not in body else fail)("slides: cabeçalho sem legenda e sem página")
    (ok if "uiFor(" in js and re.search(r'html\[data-ui="dark"\]\{--ui-fg:#ffffff', st_css) else fail)("slides: a UI fixa lê o fundo do slide corrente")
    (ok if re.search(r'<div class="wm"><b>itaú</b> <span>× @africa creative/™</span></div>', s) and re.search(r"\.wm\{[^}]*white-space:nowrap", st_css) else fail)(
        "slides: a marca d'água traz os dois nomes numa linha")
    (ok if re.search(r"\.prog\{[^}]*background:var\(--laranja\)", st_css) else fail)("slides: a barra de progresso é laranja")
    (ok if "gridlay" in s and "data-grid" in s else fail)("slides: overlay da grade na tecla G")
    # grifo: tinta laranja, palavra branca, quina pequena; inverte sobre laranja
    (ok if re.search(r"\.hl::before\{[^}]*background:var\(--acc\);border-radius:var\(--r-s\)", st_css) and
     re.search(r"\.slide\.laranja\{[^}]*--acc:#FFFFFF;--acc-fg:#FF6200", st_css) else fail)("slides: o grifo é laranja com quina pequena e inverte sobre laranja")
    hls = re.findall(r'<span class="hl" data-w="([^"]+)"[^>]*>([^<]+)</span>', body)
    badhl = [(w, t) for w, t in hls if w != t]
    (ok if hls and not badhl else fail)(f"slides: todo grifo tem data-w idêntico ao texto ({len(hls)} grifos, fora: {badhl})")
    per_slide = {t: len(re.findall(r'class="hl"', b)) for t, b in pg_secs}
    dois = {t: n for t, n in per_slide.items() if n > 1}
    (ok if set(dois) <= {"Título 04"} and per_slide.get("Título 04", 0) == 2 else fail)(f"slides: no máximo um grifo por slide, salvo o grifo duplo das órbitas (Título 04) ({dois})")
    # a camada de movimento: toda classe fa- definida é usada por algum slide (nada morto no template)
    defined = set(re.findall(r"\.(fa-[\w-]+)", st_css))
    used = set(re.findall(r'class="([^"]+)"', body))
    used = {c for cs in used for c in cs.split()}
    mortas = sorted(defined - used)
    (ok if not mortas else fail)(f"slides: toda classe fa- definida é usada (mortas: {mortas})")
    (ok if ".fa-ora{color:var(--laranja)}" in st_css and ".slide.azul.marinho{background:var(--azul-d)}" in st_css and ".ttl-s{" in st_css else fail)("slides: o acento de texto, o azul marinho e o Título curto existem na camada")

# ---------------------------------------------------------------- 10. Africa e GUT intocadas
cut = os.path.getctime(CL) - 60
touched = []
for base in ["Africa", "GUT"]:
    for root, _, names in os.walk(os.path.join(WS, "Clientes", base)):
        for n in names:
            p = os.path.join(root, n)
            try:
                if os.path.getmtime(p) > cut and not n.startswith(".DS_Store"):
                    touched.append(os.path.relpath(p, WS))
            except OSError:
                pass
(ok if not touched else fail)(f"Clientes/Africa e Clientes/GUT sem arquivo tocado desde a criação de Clientes/Itaú ({touched[:5]})")

# ---------------------------------------------------------------- saída
print("\n".join(f"  ok    {m}" for m in oks))
if warns: print("\n".join(f"  AVISO {m}" for m in warns))
if fails: print("\n".join(f"  FALHA {m}" for m in fails))
print(f"\n{len(oks)} ok · {len(warns)} avisos · {len(fails)} falhas")
sys.exit(1 if fails else 0)
