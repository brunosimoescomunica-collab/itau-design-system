# Master Slides · Itaú × Africa · contexto e operação

> **Nota do repositório.** Este documento nasceu dentro do workspace da Africa. Os caminhos foram reescritos para a estrutura deste repositório: o que era a pasta de projeto virou `build/scripts/` e `build/src/`, e a pasta de cliente virou `design-system/`. Referências a `Clientes/Africa/` e a `Itaú Fim de Ano/V2/` apontam para material que **não** está aqui: são decks de cliente e a lei da Africa, que ficam no workspace.

**O [`README.md`](README.md) é o guia e a lei. Este arquivo é o cartório.** Lá estão o procedimento de montar um deck e a regra de diagramação. Aqui ficam o porquê, as versões, as decisões e como se mexe nisso sem quebrar nada.

**Versão vigente:** Template de slides **v1.1** (18/09/2026) · 53 slides · derivado de `itau-brand-tokens.json` **v1.1** e do Master Slides da Africa **v4.3** · os componentes de 17/09 são derivação declarada da Africa (nasceram no deck Itaú fim de ano V2), nunca fato do Itaú
**Status:** rebuildado, verificado e entregue em 18/09/2026 com os componentes de 17/09 como opções de catálogo. Segue aguardando o OK do Bruno (fallback tipográfico, Bold na voz, logo do Commons como interino) e o token do logo sobre preto com o brand center.
**Atualizado:** 18/09/2026

---

## 1. O que mora aqui e o que mora fora

```
Clientes/Itaú/
├── Design System/
│   ├── itau-brand-tokens.json          # a fonte de verdade, com a fonte de cada valor
│   ├── itau-design-system.html         # o one-pager do sistema, 9 seções (a 09, Padrões animados, desde 18/09)
│   ├── itau-brand-book-a4.html/.pdf    # brand book de 3 páginas (a terceira, padrões e movimento, desde 18/09)
│   ├── assets/                         # logo (Commons, interino) · pedra · mark da Africa
│   └── fonts/                          # Figtree VF · Miletus Medium · Pangaia Light
│
├── Master Slides/                      # esta pasta
│   ├── README.md                       # guia (Parte I) e lei (Parte II)
│   ├── context.md                      # este arquivo
│   └── itau-slides-template.html       # v1.1 · 53 slides · fontes em base64
│
└── presentations/                      # os decks de verdade, um arquivo por deck
```

O template é auto-contido (fontes em base64, SVGs inline). **Ele é produto de um build**, não se edita à mão: as partes editáveis moram em `build/src/` e o script `scripts/build-itau.py` monta o arquivo entregue. Um deck de verdade, ao contrário, é uma cópia do template editada diretamente.

Desde 18/09 duas peças vivem no P16 e alimentam o template e os decks ao mesmo tempo: `scripts/itau_components.py`, o módulo com a geometria da pedra, a Moldura, a anatomia, as órbitas, o poema, o ecossistema e as tabelas (uma fonte só para forma e movimento), e `src/04-camada.css`, a camada de movimento (prefixo `fa-`), que o build injeta no head do template pelo placeholder `{{CAMADA_CSS}}`. O build do template chama o módulo com texto de exemplo; o build do deck V2 (`Clientes/Itaú/Itaú Fim de Ano/V2/work/build.py`) chama as mesmas funções com a narrativa dele.

---

## 2. Versões

**v1.0 · 15/09/2026** — nasce o template, no método do template da GUT herdado pela Africa v4.3. 42 slides: 3 de abertura (Marca, Tipografia, A regra), 7 seções editáveis com 30 modelos (6 capas, 4 statements, 3 títulos, 4 conteúdos, 2 grades de imagem, 7 dados, mais o especimen), 3 folhas de biblioteca (Marca, Pedra, Paleta) e o fecho obrigatório (Fechamento, Slogan). 250 KB.

**v1.1 · 18/09/2026.** O template incorpora, como opções de catálogo, os componentes que o deck Itaú fim de ano V2 criou em 17/09 e o Bruno aprovou slide a slide. 53 slides, 11 a mais: Capa 07 (a anatomia da pedra), Statement 05 (a Moldura em laranja, ritmo e fecho), 06 (a Moldura em preto), 07 (azul marinho, legenda miúda, o acento de texto), Título 04 (as órbitas), Conteúdo 05 (o poema em máquina de escrever), a oitava seção editável, Sistema, com Sistema 01 (nasce), 02 (momento) e 03 (camada), e a quarta folha de biblioteca, Movimento. Por quê: o deck criou uma língua de movimento e formas que se repetem (a Moldura nas frases, o ecossistema nos slides 10 a 16); deixá-las só no deck faria o próximo deck reinventar. A camada de movimento (`src/04-camada.css`) foi podada regra por regra do CSS do deck e entrou no head; os SVGs passaram a nascer do módulo `scripts/itau_components.py`, importado pelo build do template e pelo build do deck. O deck V2 foi reconstruído sobre o módulo e saiu byte a byte idêntico antes de qualquer mudança de CSS. O verificador ganhou as regras novas (lista fechada de keyframes, loops permitidos, exceções declaradas, 8 seções, 4 folhas). 522 KB.

---

## 3. Decisões e porquês

**A ideia é uma só: superfície Itaú, assinatura Africa.** O pedido era um template "com a cara do Itaú, mas com elementos que mostrem que a agência é a Africa", para o VP da Africa apresentar ao CMO. A resolução: o que se vê (cor, tipo, forma, quina, logo) é do cliente; o que se sente (grade, filete, legenda miúda, dado em Light, selo, fecho) é da agência. Cada slide precisa ter os dois; o slide "A regra" existe para isso ficar visível.

**O laranja é #FF6200, lido dos tokens oficiais do site.** O itau.com.br bloqueia acesso direto; o Wayback Machine (snapshot 2025) devolveu `tokens_idl/varejo.css` com `--ids_color_bg_brand_primary: #FF6200`. O vetor e o PNG do logo 2023 no Commons confirmam. O #EC7000 que aparece em fontes de terceiros é o laranja digital antigo e ficou registrado só para não confundir.

**A voz é Bold.** Todos os estilos de Display dos tokens do site são 700, e o logotipo é caixa baixa. A Africa proíbe Bold em slide, mas aqui a superfície é do cliente. O Light ficou no número: é a assinatura da Africa dentro do dado, e mantém o jogo "gigante contra miúda" com os pesos do cliente.

**O fallback é a Figtree.** Itau Display e Itau Text são proprietárias e não estão nesta máquina nem no workspace. O font stack declara as duas primeiro. A Figtree (OFL, variável 300 a 700, subsets latin e latin-ext) entrou por ser sans humanista, aberta, de caixa baixa amigável, com Light e Bold. **É decisão da Africa, pendente de OK.** Se a agência tiver os arquivos reais, trocar e apagar a Figtree.

**A pedra é derivação declarada, medida no logo.** O Itaú não publica a forma solta; uma fonte de terceiros a descreve como superelipse proprietária. Medi: ajuste por mínimos quadrados ao perfil do PNG do logo dá expoente 4,3 com erro de 1,2%. A pedra existe como contêiner, janela, fantasma e marcador, e nunca recebe o logotipo dentro. É a tradução do mark da Africa (que só existe no selo aqui) e do lápis da GUT (o marcador de seção).

**Seção editável é laranja com a pedra branca.** GUT, lápis; Africa, quadrado coral sobre preto; Itaú, pedra branca sobre laranja. A linhagem fica legível.

**O selo troca de miolo pela cor do fundo.** Sobre branco, o gradiente; sobre laranja, preto e azul, o mark branco chapado. Respeita `mark.fills` dos tokens da Africa e evita o gradiente brigando com o laranja.

**O logo do Itaú só sobre branco.** O vetor do Commons é laranja com as letras vazadas: sobre laranja ou preto não há versão. Nas capas coloridas o nome vai em legenda. O asset oficial do brand center substitui o símbolo `#itau` nas `<defs>` quando chegar.

**Sem coral, sem bone, sem Volume.** O acento é o laranja e a base é o branco do cliente. O 3D de plano cortado da Africa não conversa com a forma orgânica do Itaú; no lugar, as três pedras flutuando (só translação em Y, como o float da Africa).

**A curva é uma só.** `cubic-bezier(.19,1,.22,1)` é o expo out da Africa e o `--ids_motion_easing_effective_decelerate_02` do Itaú. Ficou registrado no slide de paleta e no design system: os dois sistemas se encontram nela.

**O fechamento e o slogan da Africa continuam obrigatórios.** É o lugar onde a agência fala com a própria voz (Pangaia) num deck do Itaú. A linha de co-marca "Itaú × Africa Creative/™ · desde 2002" vem da lista de clientes do site da Africa.

**18/09 · Uma fonte só para forma e movimento.** Os componentes de 17/09 moram em `scripts/itau_components.py` (o módulo) e em `src/04-camada.css` (a camada). O build do template gera o catálogo com texto de exemplo chamando o módulo; o build do deck V2 chama as mesmas funções com a narrativa dele. Quem muda a forma, muda no módulo, e template e deck acompanham no build seguinte. Antes, o deck carregava 941 linhas de build e um CSS próprio; passou a 206 linhas importando o módulo e herda a camada do template. O que motivou: o deck aprovado criou formas que voltam de slide em slide; duplicar o código seria manter duas verdades, e a segunda sempre envelhece.

**18/09 · Tudo é derivação declarada.** Nada dos componentes é fato do Itaú. As referências são as registradas na spec: o filme da Pentagram para a identidade do Itaú (2024) para a anatomia da capa; o One Sheeter do Yummly (Creative Pack 2021) para as órbitas; as prévias do 21st.dev e o duplo diamante do Africa Decoded para o ecossistema; a opção A do burst de 17/09 para a Moldura. Nos tokens entram como `derivedFrom`, nunca como `source`.

**18/09 · A família Sistema.** O ecossistema em órbitas virou seção editável própria (a oitava) porque não é dado nem título: é o guia de uma solução com partes que coexistem, e o mesmo diagrama volta no mesmo lugar em três estágios (nasce, momento, camada). O verificador exige os três.

**18/09 · Dois acentos, um por slide.** O grifo em bloco continua; o texto em laranja sem bloco (`.fa-ora`, `[texto]` na narrativa) entrou como segundo acento para uma linha ou uma palavra, nunca corpo. O grifo duplo só nas órbitas (Título 04).

**18/09 · O azul marinho como superfície escura.** `.slide.azul.marinho` usa o `--azul-d` (#000D3C, `colors.azulEscuro` dos tokens) quando o preto pesa demais (Statement 07). O azul (#000066) segue reservado a Uniclass e Personnalité.

**18/09 · As exceções declaradas, escritas como regra.** O logo do Itaú sobre preto só na Capa 07 e no Sistema 01 a 03 (token pendente com o brand center); a sombra difusa só no halo do brilho da legenda do sistema (`faEcoGlow`); o grifo duplo só no Título 04; os loops só na lista fechada de seis (`faResBreath`, `faAnaPulse`, `faAnaRes`, `faEcoBreath`, `faEcoSpin`, `faEcoTwinkle`); a pedra sólida continua sem sombra, volume ou giro (a Moldura usa desfoque leve nos contornos, veludo, não sombra; o que gira são os pontos nas órbitas e o nome que desliza 6° na curva ao entrar). O verificador confere cada uma.

---

- **17/09 (deck Itaú fim de ano, V2, capa) — exceção pedida: o logo do Itaú sobre preto.** A regra deste manual é logo só sobre branco, porque o vetor do Commons não tem versão sobre cor. Na capa da V2 o Bruno pediu a anatomia da pedra (forma, contorno e o logo, como no filme da Pentagram), e o logo é o último batimento: laranja com letras brancas, sobre a pedra preta. Tecnicamente ele nasce do mesmo símbolo `#itau`, em laranja, por cima de uma pedra branca um fio menor (as letras são vazadas no vetor). A regra segue valendo para todo o resto; o `check.py` do deck isenta só a capa. **Pendência de token:** confirmar no brand center do Itaú se o logo laranja sobre fundo escuro é uso permitido e qual é a área de proteção. Em 18/09 a exceção entrou no template (Capa 07 e o núcleo do ecossistema, Sistema 01 a 03) e passou ao `check-itau.py`, que exige exatamente essas quatro. A pendência continua.

## 4. Regras de operação

**Antes de entregar qualquer deck, rode o verificador.**
```
/usr/bin/python3 "build/scripts/check-itau.py"
```
Ele lê o produto final e cobre as duas pastas. Para o template checa, entre outras coisas: os hex dos tokens contra o CSS oficial do site, o path do mark da Africa, a grafia "Africa", a paleta fechada (sem coral, bone ou #EC7000), o gradiente na ordem, as 4 fontes embutidas, a grade e os spans, as quinas, a voz em Display 700 e o número em Display 300, a Pangaia só no fecho, as 8 seções editáveis (a oitava é Sistema, com os três estágios), as 4 folhas (a quarta é Movimento), o logo só sobre branco salvo as quatro exceções declaradas (e que as quatro existam), a lista fechada de 28 keyframes, os 6 loops permitidos, nada girando além do selo e das órbitas, a sombra difusa só no `faEcoGlow`, o grifo duplo só no Título 04, toda classe `fa-` definida usada por algum slide, o acento de texto, o azul marinho e o Título curto presentes na camada, o mark só no selo, o selo com os dois miolos, a UI que lê o fundo, o grifo com `data-w` idêntico, nunca dois laranjas adjacentes, o fechamento penúltimo e o slogan fechando, e que `Clientes/Africa` e `Clientes/GUT` continuam intocadas.

**Mexer no template.** Editar `src/01-head.html` (CSS de sistema, defs), `src/02-body.html` (slides), `src/03-tail.html` (UI, JS) ou `src/04-camada.css` (a camada de movimento) no P16, rodar `build-itau.py`, rodar `check-itau.py`, exportar e olhar. Nunca editar o HTML entregue. A forma e o movimento dos componentes vivem em `scripts/itau_components.py`: mudar ali muda o template e o deck V2, então rebuildar os dois e rodar os dois verificadores.

**Render nesta máquina.** `render-itau.sh slides` exporta o PDF; `contact-sheet.py` monta a folha de contato. Chrome headless não encerra sozinho: o script mata só os processos do perfil de scratchpad.

**Método.** Lab focado, verificar, OK do Bruno, propagar, calibrar. **Nada commitado sem o OK dele.**

---

## 5. Relacionados

- **[[P16-itau-design-system]]** — o projeto. Contexto, dossiê com as fontes, build e verificador.
- **[[P13-africa-design-system]]** — a matriz. Grade, escala, cadência e método vêm de lá.
- **`Clientes/Africa/Master Slides/README.md`** — a lei da Africa, onde este manual diz "herdado".
- **`Clientes/Itaú/Itaú Fim de Ano/V2/`**: o deck onde os componentes nasceram (17/09); `work/build.py` importa o módulo e herda a camada do template.
- **skill `master-slides`** — ainda sem bloco "Itaú × Africa". Entra com o OK do Bruno.

---

## 6. Perguntas em aberto

1. **Fallback tipográfico.** Figtree fica, ou a Africa tem a Itau Display e a Itau Text?
2. **Bold na voz.** Confirmar que o CMO deve ver títulos em Bold (a regra do site) e não em Light (a regra da Africa).
3. **Logo oficial.** Trocar o vetor do Commons pelo asset do brand center; conferir área de proteção e versões sobre cor. **O token do logo sobre preto segue pendente:** a Capa 07 e o Sistema 01 a 03 usam o logo sobre preto como exceção declarada; confirmar com o brand center se é uso permitido.
4. **Azul na Capa 05.** Manter só para Uniclass e Personnalité, ou tirar?
5. **Logo em todo slide?** Hoje só na capa branca, na de imagem e na janela; o selo da Africa está em todo slide de conteúdo.
6. **Master template (bento de componentes)** como o da Africa: fazer ou o template de slides basta?
7. **Bloco "Itaú × Africa" na skill `master-slides`** e commit na raiz. Esperam a palavra do Bruno.
8. **A régua do corpo com as fontes reais.** Os tetos de caractere (12 para o Statement, 17 para o Título) foram medidos na Figtree 700, cerca de 0,47em por caractere. Com a Itau Display, remedir e conferir a Moldura contra o texto.
