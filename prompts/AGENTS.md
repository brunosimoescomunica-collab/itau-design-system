# AGENTS.md · Itaú × Africa Creative/™

Contrato para agentes de código. O **Codex** da OpenAI lê `AGENTS.md` na raiz do repositório. Cursor, Windsurf, Gemini CLI e Copilot Agent também leem, ou leem um arquivo equivalente que aponta para este.

Copie este arquivo para a raiz do projeto onde você vai montar um deck. É o mesmo contrato de [`CLAUDE.md`](CLAUDE.md), escrito no formato que o Codex procura.

---

## Project overview

Design system híbrido para apresentações da **Africa Creative** ao **Itaú**. Entrega em HTML de arquivo único: slides em `scroll-snap`, quadro 16:9 fixo, tipografia de papel, gráficos isométricos e cinematográficos, animação por tempo.

A ideia em uma linha: **superfície Itaú, assinatura Africa.**

Não é o brand book do Itaú. É o sistema da relação agência-cliente.

## Setup

Nenhuma dependência de pacote. Python 3 do sistema e um navegador.

```bash
git clone <este repo> && cd itau-design-system
/usr/bin/python3 -m http.server 8017
# http://localhost:8017/master-slides/itau-slides-template.html
```

Para rodar o build, ajuste a variável `WS` no topo de `build/scripts/build-itau.py` e `build/scripts/check-itau.py` para a raiz do clone.

## Build and test

```bash
/usr/bin/python3 build/scripts/build-itau.py    # monta o template a partir de build/src/
/usr/bin/python3 build/scripts/check-itau.py    # bateria de invariantes
```

`check-itau.py` é o teste. **Zero falhas é condição de entrega.** Ele lê o produto final e mede contra os tokens e o dossiê. Não reusa o código que gerou os arquivos: o build injeta, o check mede. Não "conserte" o check para ele passar.

O build exige duas fontes licenciadas da Africa em `design-system/fonts/`, que não vêm no repositório público. Sem elas ele para com `FALTA fonte`. Ver `design-system/fonts/README.md`.

## Code layout

| Caminho | O que é |
|---|---|
| `build/src/01-head.html` | CSS de sistema e `defs` do SVG |
| `build/src/02-body.html` | Os slides |
| `build/src/03-tail.html` | Interface fixa e JavaScript |
| `build/src/04-camada.css` | Camada de movimento, prefixo `fa-`, injetada pelo placeholder `{{CAMADA_CSS}}` |
| `build/scripts/itau_components.py` | **A forma dos componentes.** Fonte única |
| `design-system/itau-brand-tokens.json` | **A fonte de verdade dos valores de marca** |
| `master-slides/itau-slides-template.html` | Produto de build. Nunca editar à mão |
| `master-slides/README.md` | O manual e a lei de diagramação |
| `docs/COMPONENTES.md` | Catálogo dos 53 slides e dos nove padrões |

## Conventions

- Tudo dimensionado em `cqw`. Quadro `100cqw` por `56.25cqw`. `1cqw = 19.2px` em 1920.
- Classes do movimento levam prefixo `fa-`. Não colida com as do sistema.
- Prosa e comentários em **português do Brasil**.
- Comentário só explica o **porquê** do que não é óbvio. Não descreva o que o código faz.
- Sem em-dash no texto de slide, em nenhuma língua. Frase curta e ponto.
- **"Africa" sem acento.** Regra de marca.

## Hard rules

### Nada inventado

Todo valor de marca do Itaú vem de `build/fontes/itau-tokens-varejo-wayback-2025.css`, o snapshot dos tokens oficiais do site. O logo vem do Wikimedia Commons. Não introduza hex, fonte, raio ou curva que não esteja nos tokens.

`verification.notVerified` nos tokens lista o que o sistema **não** afirma. Em deck novo, não afirme sem material fornecido: prêmios, market share, número de clientes ou de agências, cores de segmento, regras do brand book oficial do Itaú.

Dado de campanha, mídia ou negócio entra com fonte. Sem fonte, não entra.

### A ordem de trabalho

1. Ler os tokens, o manual e o catálogo. Nesta ordem.
2. Escrever o argumento em prosa. Texto antes de slide.
3. Escolher um molde do catálogo. **Nunca montar slide a partir de uma classe CSS achada no arquivo.**
4. Procurar a classe que já existe e está dormente antes de inventar layout novo.
5. Build, check, conferir renderizado.

### A paleta fechada

`#FF6200` laranja · `#FFFFFF` branco · `#000000` preto · `#000066` azul (só Uniclass e Personnalité, nunca ao lado do laranja em massa) · `#000D3C` azul marinho · `#4C4C4C` cinza de texto.

Nada de coral, nada de bone: esses são da Africa e ficam fora. O laranja é `#FF6200`, **não** `#EC7000`.

### A régua 12/17

Pela linha mais larga da frase: até 12 caracteres, Statement (`8cqw`). Até 17, Título (`5.6cqw`). Acima, Título curto (`4.6cqw`). Até três linhas; quatro só em statement sem apoio. **Um acento por slide.**

O peso intermediário não faz hierarquia: Display é 700, Text é 400, Light só no número.

### A pedra

Superelipse de expoente **4.3**, medida no vetor do logo 2023. Contêiner, janela, fantasma, marcador de seção. **Nunca com o logotipo dentro.**

### O mark da Africa

Só existe dentro do selo. Gradiente sobre branco, branco chapado sobre cor. Nunca solto, nunca em texto, nunca em barra.

### O movimento

Por **tempo**, nunca por scroll. Dispara em `.slide.visible`. `--d0` entrada, `--dur` duração, `--n` passos. Termina num estado final que fica.

**Nunca `vector-effect` junto com `pathLength`:** o Chrome tracejaria a linha.

### O fecho

Dois slides no fim, nesta ordem, sem editar uma palavra:

1. "Somos a Africa: a agência que nasce e se desafia todos os dias, para nunca deixar de ser a Africa Creative/™."
2. "A agência das marcas mais desejadas, admiradas e valiosas do Brasil."

## Do not

- Não edite `master-slides/itau-slides-template.html` à mão.
- Não remova CSS por bloco. Remova regra por regra e feche com auditoria de classe usada contra classe definida.
- Não adicione dependência de pacote. O entregável é arquivo único que viaja por e-mail.
- Não publique as fontes `MiletusGrotesk-Medium.woff2` e `PPPangaia-Light.woff2` neste repositório: são fontes pagas.
- Não toque em `Clientes/Africa/` nem em `Clientes/GUT/` do workspace de origem. Só leitura.
