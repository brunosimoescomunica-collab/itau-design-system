# Dossiê · Itaú (identidade 2023) · fontes e o que não foi verificado

> **Nota do repositório.** Este documento nasceu dentro do workspace da Africa. Os caminhos foram reescritos para a estrutura deste repositório: o que era a pasta de projeto virou `build/scripts/` e `build/src/`, e a pasta de cliente virou `design-system/`. Referências a `Clientes/Africa/` e a `Itaú Fim de Ano/V2/` apontam para material que **não** está aqui: são decks de cliente e a lei da Africa, que ficam no workspace.

Pesquisa feita em 15/09/2026 para o P16. Tudo o que o sistema Itaú × Africa afirma sobre o Itaú sai daqui. O que não está aqui, o sistema não afirma.

## 1. O site oficial bloqueou o acesso direto

`itau.com.br` responde 403 a curl e a Chrome headless (proteção anti-bot). O que funcionou foi o **Wayback Machine**: snapshot de 2025 da home (`web.archive.org/web/2025id_/https://www.itau.com.br/`), 135 KB, e a partir dela os CSS ligados, servidos comprimidos em gzip:

| Arquivo | Tamanho | O que trouxe |
|---|---|---|
| `/tokens_idl/varejo.css` | 19 KB | **Os tokens oficiais do design system do varejo**: cores, tipografia, raios, bordas, espaçamento, movimento. Cópia em `fontes/itau-tokens-varejo-wayback-2025.css`. |
| `/libs/styles-idl/main.css` | 276 KB | Componentes. Só referencia os tokens por `var()`. |
| `/modules_idl/header_idl/header_idl.css` | 53 KB | Header. Idem. |

A home arquivada está em `fontes/itau-home-wayback-2025.html`.

## 2. O que os tokens oficiais dizem (fonte primária)

**Cores**
- `--ids_color_bg_brand_primary: #FF6200` · `--ids_color_action_primary_base: #FF6200` · `--ids_color_text_highlight: #FF6200` · `--ids_color_chart_01: #FF6200`
- `--ids_color_action_primary_variant: #E55800` (pressionado)
- `--ids_color_bg_brand_secondary: #000066` · variante `#000D3C` · link `#000066`
- `--ids_color_bg_base: #FFFFFF` · `bg_variant_01: #F1F2F4` · `bg_variant_02: #E3E5E8`
- texto: `body_01 #000000` · `body_02 #4C4C4C` · `heading_01 #000000` · `heading_02 #4C4C4C`
- bordas: `soft #CFD1D3` · `medium #ADB8B3` · `strong #5D636F`
- desabilitado: `#CFD1D3` · `#999999` · neutro de ação `#3B3B3B`
- contraste sobre a marca: `onBrand_primary #FFFFFF` · `onBrand_secondary #FFFFFF` · `onLight #000000` · `onDark #FFFFFF`
- gráfico: `#FF6200 · #002766 · #6E6E6E · #0131FF · #FFBA00 · #999999 · #BD0071 · #008717`
- feedback: alerta `#FFCC00` · erro `#CC0000` · informação `#001FBD` · sucesso `#0B5B38` · neutro `#4C4C4C`

**Tipografia**
- `--ids_textStyle_f01_s16_h24_wbd` até `f01_s64_h100`: **`700 … "Itau Display"`** em todos os tamanhos (16/24, 20/28, 24/32, 32/48, 40/64, 48/80, 64/100). Até os tokens com sufixo `wrg` (regular) resolvem para 700.
- `--ids_textStyle_body_01`: `400 1rem/1.5rem "Itau Text"` e `700`; `body_02`: 14/20; `caption`: 12/18; links em 400, 700 e **900**.
- Não há `@font-face` nos CSS arquivados: as fontes são servidas por outro caminho. **Os arquivos das fontes não estão em mãos.**

**Forma e medida**
- raios: `button .75rem` · `card_01 1rem` · `card_02 .75rem` · `layout_01 1rem` · `layout_02 1.5rem` · `smallButton .5rem` · `tags .25/.5rem` · `tooltip .25rem` · `table .25rem` · `snackbar .25rem`
- bordas: `small .0625rem` (1px) · `medium .125rem` · `large .25rem`
- espaçamento: `1x .25rem` até `14x 3.5rem` (base 4px)
- tamanhos gerais `1x` a `140x` em passos de 4px

**Movimento**
- `--ids_motion_easing_effective_decelerate_02: cubic-bezier(0.19, 1, 0.22, 1)` (idêntico ao expo out da Africa)
- `vivid_decelerate_on: cubic-bezier(0.22, 1, 0.36, 1)` · `standard: cubic-bezier(0.4, 0, 0.6, 1)` · `vivid_standard: cubic-bezier(0.6, 0, 0.2, 1)`
- tempos: fast 100/150/200ms · moderate 250/300/350 · slow 400/450/500 · superslow 600/700/800
- opacidades: soft .10 · medium .50 · strong .80

## 3. O logo

- **Wikimedia Commons**, `File:Itaú Unibanco logo 2023.svg` (500×500, 11 KB, licença PD-textlogo, marca registrada). Dois paths, ambos `fill:#FF6200`: a pedra com as letras vazadas e o miolo do **a**. Conferido renderizado: é o "itaú" em caixa baixa dentro da pedra laranja.
- `File:2023 Itaú Unibanco Logo.png` (1233×1233): amostragem de 32.860 pixels laranja, todos `#FF6200`. Bate com os tokens do site.
- **Curvatura da pedra**: perfil da borda esquerda do PNG ajustado a uma superelipse |x|^n + |y|^n = 1. Melhor `n = 4.3`, erro quadrático médio de 14px em 1233 (1,2%). 26% da borda é reta.

## 4. O rebrand de 2023 (imprensa e estúdio)

| Fato | Fonte |
|---|---|
| Lançamento em 06/12/2023, conceito "Feito de Futuro" | [GKPB](https://gkpb.com.br/160737/novo-logo-itau/) · [Janela](https://janela.com.br/2023/12/07/com-nova-marca-itau-lanca-campanha-com-o-conceito-feito-de-futuro/) |
| Itaú = pedra preta em tupi-guarani; o símbolo é a pedra, agora "mais orgânica e fluida" | GKPB · [Design Conceitual](https://designconceitual.com.br/2023/12/07/itau-atualiza-marca-e-adota-slogan-feito-de-futuro/) |
| 22 meses, mais de 70 estudos de cor, cerca de 100 estudos tipográficos | GKPB · Janela |
| Pentagram (Michael Bierut) na consultoria; Fabio Haag no refinamento tipográfico | GKPB · Janela · [Fabio Haag Type](https://fabiohaagtype.com/en/itau/) |
| Africa Creative e Galeria no posicionamento | GKPB · Janela · Design Conceitual |
| Laranja ganha protagonismo; azuis vibrantes para Uniclass e Personnalité; tons escuros para BBA e Private | GKPB · Design Conceitual |
| Logotipo em caixa baixa como gesto de humanização; acento do ú horizontal e ascendente; sans humanista com influência caligráfica e contraste sutil; equipe Fabio Haag, Henrique Beier, Ana Laydner, Eduilson Coan; Pentagram NY com Michael Bierut e Robin Haueter | Fabio Haag Type |
| Eduardo Tracanella, CMO, liderou o projeto; de "Feito com você" para "Feito de Futuro"; laranja na paleta desde 1992 | [Brazil Journal](https://braziljournal.com/play/por-que-o-itau-decidiu-mudar-a-marca-e-assumir-o-laranja/) |
| Clayton Caetano, superintendente de design; linhagem Aloízio Magalhães (anos 1960), Francesc Petit (1970), Alexandre Wollner (1980) | Janela · Design Conceitual |
| Personalidades da campanha: Madonna, Jorge Ben Jor, Ronaldo, Fernanda Montenegro, Ingrid Silva, Marta | Janela |
| Itaú Typeface (Dalton Maag): Itaú Display com 6 pesos, Itaú Text com 4; "proximidade, leveza, simplicidade"; 43% mais leve que a Myriad; 10 meses, testada com 1.200 clientes | [Behance · Amanda Carvalho](https://www.behance.net/gallery/94801085/Itau-Typeface) · [Janela 2018](https://janela.com.br/2018/05/16/itau-ganha-nova-fonte-criada-com-designers-da-inglesa-dalton-maag/) |

## 5. Fontes de terceiros (registradas, não usadas como verdade)

- [designmd.app/brands/itau](https://designmd.app/brands/itau): descreve um "Voxel Design System" com laranja `#EC7000`, azul `#003399`, neutros `#F7F7F7 / #EDEDED / #1A1A1A`, raios 4/8/12px, "Pedra: superelipse orgânica proprietária", princípios "simples, confiável, relevante, memorável". É extração automática de terceiros e **diverge dos tokens oficiais** (#FF6200, #000066, #F1F2F4). Serve só como pista da pedra como contêiner.
- Fontes de download pirata de "Itau Display" apareceram na busca. **Não foram usadas.** As famílias são proprietárias.

## 6. O que NÃO foi verificado (a cerca)

- O brand book oficial 2023 (área de proteção, versões monocromáticas, logo sobre laranja e sobre preto, fotografia, grafismos).
- Os arquivos da Itau Display e da Itau Text. O template declara as famílias e cai no fallback Figtree (decisão da Africa, pendente de OK).
- As cores oficiais de cada segmento.
- Prêmios, market share, número de clientes ou agências.
- O Pentagram: a página do case (`pentagram.com/work/itau`) dá 404; o item de arquivo 40967 não tem texto.

## 7. O que ficou registrado no workspace

```
build/fontes/
├── itau-tokens-varejo-wayback-2025.css   # os tokens oficiais, decodificados
└── itau-home-wayback-2025.html           # a home arquivada
design-system/assets/
├── itau-logo-2023-commons.svg / .png     # o logo, do Commons
├── itau-pedra.svg                         # a superelipse n=4.3, gerada
└── africa-mark.svg                        # o mark da Africa, cópia
```
