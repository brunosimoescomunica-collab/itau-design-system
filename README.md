# Itaú × Africa Creative/™ · Design System e Master Slides

**Superfície Itaú, assinatura Africa.** O que se vê é do cliente: branco, laranja, a pedra, a Itau Display em caixa baixa, as quinas de 16px. O que se sente é da agência: a grade de 12 colunas, o filete de 1px, a legenda miúda contra o título gigante, o dado editorial em Light, o selo no canto e o fecho em Pangaia.

Este repositório é o sistema de marca que a Africa usa para apresentar ao Itaú. Não é o brand book do Itaú. É o sistema híbrido da relação agência-cliente: campanhas e estratégia, plateia CMO, apresentado pelo VP da Africa.

**Versão 1.1 · 18/09/2026**

---

## Baixar

```bash
git clone https://github.com/brunosimoescomunica-collab/itau-design-system.git
cd itau-design-system
```

Depois disso, abra dois arquivos no navegador e você já viu o sistema inteiro:

| Arquivo | O que é |
|---|---|
[`design-system/itau-design-system.html`](design-system/itau-design-system.html) | O design system vivo, em uma página, com interruptor claro e escuro |
[`master-slides/itau-slides-template.html`](master-slides/itau-slides-template.html) | O deck-mãe: 53 slides que ensinam mostrando |

Para o template, não abra por duplo clique se o navegador bloquear os arquivos locais. Sirva por HTTP:

```bash
/usr/bin/python3 -m http.server 8017
# depois abra http://localhost:8017/master-slides/itau-slides-template.html
```

Teclas dentro do deck: setas, espaço, `j` e `k` navegam. `N` mostra o roteiro. `B` troca claro e escuro. `G` liga a grade.

---

## O que tem dentro

```
itau-design-system/
├── design-system/
│   ├── itau-brand-tokens.json        A fonte de verdade. Cada valor com a sua origem.
│   ├── itau-design-system.html       O sistema vivo em uma página, 9 seções
│   ├── itau-brand-book-a4.html/.pdf  O brand book, 3 páginas A4, para imprimir
│   ├── assets/                       Logo do Itaú 2023, a pedra, o mark da Africa
│   └── fonts/                        Figtree (OFL) e o aviso das duas fontes pagas
├── master-slides/
│   ├── README.md                     O manual: como montar um deck e a lei de diagramação
│   ├── context.md                    Contexto e operação
│   ├── itau-slides-template.html     O deck-mãe, 53 slides
│   └── fonts/                        Onde vão as duas fontes pagas da Africa
├── build/
│   ├── src/                          As partes editáveis do template
│   ├── scripts/                      O build, os componentes e a bateria de invariantes
│   └── fontes/                       Os tokens oficiais do site do Itaú (snapshot Wayback 2025)
├── docs/
│   ├── dossie-itau.md                A pesquisa, com fonte por fato
│   └── COMPONENTES.md                O índice dos componentes
├── prompts/
│   ├── CHATGPT.md                    Como pôr o sistema no ChatGPT, com os prompts prontos
│   ├── CLAUDE.md                     Para Claude e Claude Code
│   ├── AGENTS.md                     Para Codex e agentes que leem AGENTS.md
│   └── COWORK-GOOGLE-SLIDES.md       Para montar isto no Google Slides
├── NOTICE.md                         O que você pode e o que não pode reusar
└── CHANGELOG.md
```

---

## A regra em uma página

### Cor

| Token | Hex | Papel |
|---|---|---|
| `laranja` | `#FF6200` | A cor do cliente. Pode ser massa: capa, seção, bloco do grifo, pedra, uma região de diagrama. |
| `branco` | `#FFFFFF` | A base. O Itaú é claro primeiro, como a Africa. |
| `preto` | `#000000` | Tinta, filete de 1px, capa preta, modo escuro. Itaú é pedra preta. |
| `azul` | `#000066` | Só entra pelo segmento: Uniclass e Personnalité. Nunca ao lado do laranja em massa. |
| `azulEscuro` | `#000D3C` | A superfície azul marinho, quando o preto pesa demais. |
| `cinzaTexto` | `#4C4C4C` | Texto de apoio, legenda, fonte do dado. |

Nada de coral. Nada de bone. Esses são da Africa e ficam fora.

**O laranja é `#FF6200`, não `#EC7000`.** O segundo é o laranja digital antigo, citado por fonte de terceiros. Os tokens oficiais de 2025 e o logo 2023 dizem o primeiro.

### Tipografia

| Papel | Família | Peso | Fallback |
|---|---|---|---|
| A voz: capa, statement, título | Itau Display | 700 | Figtree 700 |
| O texto: parágrafo, lista, nota | Itau Text | 400 e 700 | Figtree 400 e 700 |
| O número-herói | Itau Display | 300 | Figtree 300 |
| O anel do selo | Miletus Grotesk | 500 | fonte da Africa |
| O fechamento e o slogan | PP Pangaia | 300 | fonte da Africa |

Itau Display e Itau Text são proprietárias e não estão aqui. O font stack as declara primeiro: na máquina que as tiver instaladas, o deck renderiza com elas. Onde não tiver, cai na Figtree.

### Grade

Quadro 16:9 fixo, `100cqw` por `56.25cqw`. Tudo em `cqw`. Margem de `5.2cqw` nos quatro lados. 12 colunas de `6cqw` com calha de `1.6cqw`. Span de N colunas = `7.6N - 1.6`. Herdado do Master Slides da Africa v4.3, sem alteração: é a assinatura estrutural da agência.

### Forma

A quina é do Itaú. Contêiner de imagem e painel levam 16px (`0.8cqw`). O bloco do grifo leva 8px. Contêiner grande leva 24px.

**A pedra** é a superelipse de expoente **4.3**, medida no vetor do logo 2023. Ela é contêiner, janela, fantasma e marcador de seção. **Nunca com o logotipo dentro.**

### O fecho é obrigatório

Todo deck termina com dois slides, nesta ordem e sem editar uma palavra:

1. **Fechamento:** "Somos a Africa: a agência que nasce e se desafia todos os dias, para nunca deixar de ser a Africa Creative/™."
2. **Slogan:** "A agência das marcas mais desejadas, admiradas e valiosas do Brasil."

É onde a Africa fala com a própria voz, em Pangaia, dentro de um deck do Itaú.

---

## A lei que não se negocia

**Nada inventado.** Todo hex, fonte, raio e curva do Itaú vem de `tokens_idl/varejo.css` do itau.com.br, no snapshot do Wayback de 2025, que está em [`build/fontes/`](build/fontes/). O logo vem do Wikimedia Commons. O que o dossiê não cobre, o sistema não afirma: a chave `verification.notVerified` dos tokens lista o que fica de fora.

Em deck novo, isso significa: prêmios, market share, número de clientes ou de agências, cores de segmento e regras do brand book oficial do Itaú **não se afirmam** sem material fornecido.

**"Africa" sem acento.** Regra de marca.

**O mark da Africa só existe dentro do selo.** Gradiente sobre branco, branco chapado sobre cor. Nunca solto, nunca em texto, nunca em barra.

---

## Como montar um deck

O manual completo é [`master-slides/README.md`](master-slides/README.md). O resumo em seis passos:

0. **Abrir a fonte antes do editor.** Ler os tokens, o manual e o catálogo de componentes, nessa ordem.
1. **Escrever o argumento antes do HTML.** Texto primeiro, slide depois.
2. **Escolher o molde** no catálogo do template, não inventar layout.
3. **Montar** copiando o slide do template e trocando o conteúdo.
4. **Conferir renderizado**, não no código.
5. **Fechar** com os dois slides obrigatórios.

Nunca monte um slide a partir de uma classe CSS achada no arquivo. A classe é consequência. O modelo é a origem.

---

## Usar com agente de IA

A pasta [`prompts/`](prompts/) tem quatro arquivos, um por ferramenta:

| Arquivo | Para quem | O que faz |
|---|---|---|
[`prompts/CHATGPT.md`](prompts/CHATGPT.md) | **Comece por aqui se você usa ChatGPT** | Como pôr o sistema dentro do ChatGPT e os prompts prontos. Explica por que o ChatGPT não consegue clonar o repositório, e o que fazer em vez disso. |
[`prompts/CLAUDE.md`](prompts/CLAUDE.md) | Claude e Claude Code | Carrega o sistema e as regras duras. Copie para a raiz do seu projeto. |
[`prompts/AGENTS.md`](prompts/AGENTS.md) | Codex e qualquer agente que leia `AGENTS.md` | O mesmo contrato, no formato que o Codex procura. Copie para a raiz do repositório e ele entra sozinho. |
[`prompts/COWORK-GOOGLE-SLIDES.md`](prompts/COWORK-GOOGLE-SLIDES.md) | Cowork, ChatGPT Work e Codex | Prompt pronto para montar este sistema direto no Google Slides, com a conversão de medidas. |

---

## Licença e reuso

Leia [`NOTICE.md`](NOTICE.md) antes de reusar qualquer coisa. Em resumo:

- **Marca do Itaú:** propriedade do Itaú Unibanco. Uso restrito ao trabalho da Africa para o Itaú.
- **Marca da Africa:** propriedade da Africa Creative.
- **Figtree:** SIL OFL 1.1, livre. Licença em [`design-system/fonts/Figtree-OFL.txt`](design-system/fonts/Figtree-OFL.txt).
- **Miletus Grotesk e PP Pangaia:** fontes pagas, **removidas** deste repositório. Ver [`design-system/fonts/README.md`](design-system/fonts/README.md).
- **O sistema, o código e os componentes:** criação da Africa Creative.

---

Mantido por Bruno Simões · VP de Creative Effectiveness, Africa Creative/™
