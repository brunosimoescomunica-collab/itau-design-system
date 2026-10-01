# CLAUDE.md · Itaú × Africa Creative/™

Copie este arquivo para a raiz do projeto onde você vai montar um deck. O Claude Code lê `CLAUDE.md` no começo de cada sessão.

---

## O que é este sistema

**Superfície Itaú, assinatura Africa.** O que se vê é do cliente: branco, laranja `#FF6200`, a pedra, Itau Display em caixa baixa, quinas de 16px. O que se sente é da agência: grade de 12 colunas, filete de 1px, legenda miúda contra título gigante, dado editorial em Light, selo no canto, fecho em Pangaia.

Plateia: CMO do Itaú. Apresentador: o VP da Africa. Assunto: campanhas e estratégia.

## Leia antes de escrever a primeira linha

Nesta ordem, sempre:

1. `design-system/itau-brand-tokens.json` — a fonte de verdade. Cada valor tem a sua origem.
2. `master-slides/README.md` — o manual e a lei de diagramação.
3. `docs/COMPONENTES.md` — o catálogo dos 53 slides e dos nove padrões.

Abra `master-slides/itau-slides-template.html` para ver, não para copiar classe solta.

## As cinco regras duras

### 1. Nada inventado

Todo hex, fonte, raio e curva do Itaú vem de `build/fontes/itau-tokens-varejo-wayback-2025.css`. O que o dossiê não cobre, o sistema não afirma. A chave `verification.notVerified` dos tokens lista o que fica de fora.

Em deck novo, **não afirme sem material fornecido pelo cliente**: prêmios, market share, número de clientes ou de agências, cores de segmento, regras do brand book oficial do Itaú.

Todo dado de campanha, mídia ou negócio entra com fonte. Sem fonte, diga "não tenho fonte para isso" e pare.

### 2. Texto antes de slide

Escreva o argumento inteiro em prosa primeiro. O slide vem depois. Nunca comece pelo HTML.

### 3. O molde antes do layout

Escolha um slide do catálogo e troque o conteúdo. **Nunca monte um slide a partir de uma classe CSS achada no arquivo.** A classe é consequência. O modelo é a origem.

Procure a classe que já existe e está dormente antes de inventar layout novo ou importar de fora.

### 4. A forma vive num módulo

A forma dos componentes está em `build/scripts/itau_components.py`. O movimento está em `build/src/04-camada.css`, prefixo `fa-`. Mudar ali muda o template e os decks. Rebuildar os dois.

**Nunca edite o HTML entregue à mão.** Ele é produto de build.

### 5. O fecho é obrigatório

Dois slides no fim, nesta ordem, sem editar uma palavra:

1. **Fechamento:** "Somos a Africa: a agência que nasce e se desafia todos os dias, para nunca deixar de ser a Africa Creative/™."
2. **Slogan:** "A agência das marcas mais desejadas, admiradas e valiosas do Brasil."

## A régua da tipografia

Quadro 16:9 fixo, `100cqw` por `56.25cqw`. Tudo em `cqw`. `1cqw = 19.2px` num quadro de 1920.

| Papel | cqw | Fonte |
|---|---|---|
| hero (a capa) | 9.4 | Display 700 |
| statement | 8 | Display 700 |
| título | 5.6 | Display 700 |
| título curto | 4.6 | Display 700 |
| número-herói | 15 | Display 300 |
| subtítulo | 2.6 | Text 700 |
| corpo grande | 2.3 | Text 400 |
| corpo | 1.75 | Text 400 |
| corpo pequeno | 1.35 | Text 400 |
| legenda | 1 | Text 700, caixa alta |

**A régua 12/17**, pela linha mais larga da frase: até 12 caracteres, Statement (8cqw). Até 17, Título (5.6). Acima, Título curto (4.6).

Até três linhas. Quatro só num statement sem apoio. **Um acento por slide.** O peso intermediário não faz hierarquia: Display é 700, Text é 400, o Light só aparece no número.

## A cor

| Token | Hex | Uso |
|---|---|---|
| laranja | `#FF6200` | Massa de capa e seção, bloco do grifo, pedra, uma região de diagrama |
| branco | `#FFFFFF` | A base |
| preto | `#000000` | Tinta, filete de 1px, capa preta, modo escuro |
| azul | `#000066` | Só pelo segmento: Uniclass e Personnalité. Nunca ao lado do laranja em massa |
| azul marinho | `#000D3C` | Quando o preto pesa demais |
| cinza de texto | `#4C4C4C` | Apoio, legenda, fonte do dado |

Nada de coral. Nada de bone. Esses são da Africa e ficam fora.

**O laranja é `#FF6200`, não `#EC7000`.**

## A grade

Margem `5.2cqw` nos quatro lados. 12 colunas de `6cqw`, calha de `1.6cqw`. Span de N colunas = `7.6N - 1.6`. Âncoras: selo até `5.3cqw`, início da tela em `10.4cqw`, pé em `51.05cqw`.

## A forma

Quina de 16px (`0.8cqw`) em contêiner de imagem e painel. 8px no bloco do grifo. 24px em contêiner grande.

**A pedra** é a superelipse de expoente **4.3**, medida no vetor do logo 2023. É contêiner, janela, fantasma e marcador de seção. **Nunca com o logotipo dentro.**

**O mark da Africa só existe dentro do selo.** Gradiente sobre branco, branco chapado sobre cor. Nunca solto, nunca em texto, nunca em barra.

## O movimento

Animação **por tempo**, não por scroll. Tudo dispara em `.slide.visible`, pelo observer do template. `--d0` é quando a peça entra, `--dur` a duração, `--n` os passos. Tudo termina num estado final que fica: impressão e movimento reduzido mostram esse estado.

| Curva | Valor |
|---|---|
| expoOut (padrão) | `cubic-bezier(.19,1,.22,1)` |
| slowIn | `cubic-bezier(.16,1,.3,1)` |
| vivid | `cubic-bezier(.22,1,.36,1)` |

**Nunca `vector-effect` junto com `pathLength`.** O Chrome tracejaria a linha.

## Antes de entregar

```bash
/usr/bin/python3 build/scripts/build-itau.py
/usr/bin/python3 build/scripts/check-itau.py   # zero falhas, obrigatório
```

Ajuste a variável `WS` no topo dos scripts para a raiz do seu clone.

Confira **renderizado**, não no código. Nada vaza do slide. Texto sobre fundo movimentado tem que ler limpo.

## A grafia

**"Africa" sem acento.** Regra de marca.
