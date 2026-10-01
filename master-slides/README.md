# Master Slides · Itaú × Africa Creative/™

> **Nota do repositório.** Este documento nasceu dentro do workspace da Africa. Os caminhos foram reescritos para a estrutura deste repositório: o que era a pasta de projeto virou `build/scripts/` e `build/src/`, e a pasta de cliente virou `design-system/`. Referências a `Clientes/Africa/` e a `Itaú Fim de Ano/V2/` apontam para material que **não** está aqui: são decks de cliente e a lei da Africa, que ficam no workspace.

**O guia de construção e a lei de diagramação.** Leia antes de montar qualquer deck da Africa para o Itaú.

A ideia em uma linha: **superfície Itaú, assinatura Africa.** O que se vê é do cliente (branco, laranja, a pedra, Itau Display em caixa baixa, quinas de 16px). O que se sente é da agência (grade de 12 colunas, filete de 1px, legenda miúda contra título gigante, dado em Light, selo no canto, fecho em Pangaia).

A **Parte I** é o procedimento: como se sai de um briefing e se chega num deck pronto. A **Parte II** é a lei: o híbrido, a grade, a tipografia, a composição, a cor, o movimento. Onde a lei é a mesma da Africa, este manual diz "herdado" e não repete a justificativa: ela está em `Clientes/Africa/Master Slides/README.md`.

Template: [`itau-slides-template.html`](itau-slides-template.html) · Contexto e operação: [`context.md`](context.md) · Tokens: `../design-system/itau-brand-tokens.json` · Sistema: `../design-system/itau-design-system.html` · Componentes: `build/scripts/itau_components.py` · Camada de movimento: `build/src/04-camada.css`

---
---

# PARTE I · COMO MONTAR UM DECK

## O procedimento, em seis passos

### Passo 0 · Abrir a fonte antes de abrir o editor

Ler três coisas nesta ordem: os **tokens** (`itau-brand-tokens.json`), este README e o **catálogo da seção 7**. Nunca montar slide a partir de uma classe CSS achada no arquivo: a classe é consequência, o modelo é a origem.

Se o deck tem dado de campanha, de mídia ou de negócio, **a fonte vem antes do slide**. A cerca `verification.notVerified` dos tokens vale em todo deck: prêmios, market share, número de clientes ou de agências, cores de segmento e regras do brand book oficial do Itaú não se afirmam sem material fornecido.

### Passo 1 · Escrever o argumento antes do HTML

Uma linha por slide, **cada linha sendo a afirmação que o slide faz**. Não "Awareness", mas "A campanha dobrou a lembrança e a consideração não acompanhou". Se a linha não é uma frase com verbo, o slide ainda não sabe o que quer dizer.

Com a lista pronta, três perguntas: cada linha é uma mensagem só? Qual é o pico? O arco fecha?

### Passo 2 · Escolher o modelo pela mensagem

Cada linha vira um modelo do template. **A mensagem escolhe o modelo, nunca o contrário.** O mapa está abaixo.

### Passo 3 · Montar o esqueleto

1. **Duplicar** `itau-slides-template.html` para `../presentations/<nome-do-deck>.html`. O template nunca é editado, só duplicado.
2. **Apagar tudo o que não vai usar**: os slides de sistema (Tipografia, A regra), os slides de seção do catálogo (Estilos, Capas, Statement…) e as folhas de biblioteca. O **modelo** de seção volta depois, com o nome do seu capítulo.
3. **Reordenar** o que sobrou na ordem do argumento.
4. **Duplicar** o modelo quantas vezes o argumento pedir.

O que **nunca** se toca: o `<style>`, o SVG de `<defs>` (o mark da Africa, o gradiente, a pedra, o clipPath, o logo do Itaú, os anéis do selo), o `<script>`, a UI fixa e os dois últimos slides (fechamento e slogan). É carga estrutural.

### Passo 4 · Preencher

Regra única: **trocar o conteúdo, preservar a estrutura da `<section>`**.

- O texto de exemplo nomeia o estilo que ele carrega. "Statement lorem ipsum" sai e entra o statement de verdade, no mesmo lugar, no mesmo corpo.
- `data-title` recebe o nome do slide. `data-notes` recebe o roteiro de palco: **é onde vive o que se fala, nunca na tela.**
- O grifo (`.hl`) precisa do atributo `data-w` com **o mesmo texto** que está dentro da tag.
- Imagem real entra em base64 no lugar do marcador, teto de 400KB por imagem. Na janela da pedra (Capa 06), a imagem entra dentro do `.img.win`.
- O logo do Itaú do template é o vetor do Commons. **Antes da primeira apresentação, trocar pelo asset oficial** do brand center (o símbolo `#itau` nas `<defs>`).

**Os componentes vivos** (Capa 07, Statement 05 a 07, Título 04, Conteúdo 05, Sistema 01 a 03) têm duas partes. A camada de movimento (as classes `fa-`) já está no `<style>` do template: nada a instalar. Os SVGs (a Moldura, a anatomia, as órbitas, o ecossistema) e o poema vêm de `build/scripts/itau_components.py`, uma fonte só para forma e movimento. Um deck com build importa o módulo e chama as funções com a própria narrativa, como o Itaú fim de ano V2 faz (`V2/work/build.py`). Um deck montado à mão duplica o slide do catálogo e troca o texto: o SVG que veio com ele já é o do módulo. Quem muda a forma, muda no módulo; o template e os decks acompanham no build seguinte.

### Passo 5 · Verificar antes de mostrar

```
/usr/bin/python3 "build/scripts/check-itau.py"
```

O verificador lê o produto final. Depois dele, **exportar em PDF e olhar** a folha de contato (receita na seção 10).

### Passo 6 · Registrar

Deck de projeto `P##` termina escrevendo no `session-log.md` do projeto.

---

## O mapa: a mensagem escolhe o modelo

| A linha do argumento diz… | Modelo | Por quê |
|---|---|---|
| É o começo. O deck tem um nome. | **Capa 01–06** | Branca com o logo e a pedra sangrando para o padrão; imagem quando há foto com direito; laranja para energia; a pedra preta para peso; azul só para Uniclass e Personnalité; a janela quando a foto é o argumento. |
| A marca é o argumento: a forma, o contorno e o logo. | **Capa 07** | Preta, a anatomia da pedra como no filme da Pentagram: o quadrado vira a pedra, quatro contornos respiram em onda, o logo chega por último. A única capa com o logo sobre preto (exceção declarada). |
| Uma verdade curta que cala a sala. | **Statement 02** | O respiro é a mensagem. |
| Uma verdade curta que precisa de contexto. | **Statement 04** | A frase em cima, o parágrafo pequeno embaixo. |
| Uma verdade curta com peso de marca. | **Statement 01** | A pedra em fantasma nos cantos. Uma vez por deck. |
| Uma verdade curta que fecha uma lista. | **Statement 05** | Laranja. A frase com a Moldura em laranja escuro e o apoio com ritmo: os itens em legenda entram um a um, separados pela pedra miúda, e o fecho vem em corpo grande branco. A lista, depois o ponto. |
| Uma verdade curta que pede palco. | **Statement 06** | A frase com a Moldura: seis contornos da pedra respirando atrás dela, tom sobre tom, e o apoio cinza embaixo. Preto no catálogo; funciona nas quatro superfícies. |
| Uma verdade curta com rótulo, em que uma linha é o pico. | **Statement 07** | Azul marinho. A legenda miúda acima da frase e uma linha inteira em laranja: o segundo acento, texto sem bloco. A superfície escura quando o preto pesa demais. |
| Uma afirmação que abre um assunto. | **Título 01** | Centrado, com subtítulo. |
| Uma afirmação que a imagem prova. | **Título 02** | Imagem na metade esquerda. |
| Uma afirmação que um conceito abstrato sustenta. | **Título 03** | As pedras na metade esquerda. Escolher a composição pelo conceito. |
| Uma ideia que cresce a partir de um centro. | **Título 04** | As órbitas (a Matéria do One Sheeter do Yummly, Creative Pack 2021): a pedra bate duas vezes e cada batida deixa uma faixa; os sinais na primeira, os assuntos na segunda. O único grifo duplo do sistema. |
| Quatro ideias irmãs. | **Conteúdo 01** | Dois por dois. |
| Uma ideia que a imagem acompanha. | **Conteúdo 02** ou **03** | 02 imagem à direita inteira; 03 imagem embaixo. |
| Uma lista que é sequência ou inventário. | **Conteúdo 04** | Filete vertical. Sete itens no máximo. |
| Um texto que se lê inteiro, no ritmo de quem o escreve. | **Conteúdo 05** | O poema em máquina de escrever: página dupla, corpo pequeno, uma tinta só. Sem Moldura e sem selo. |
| Várias imagens, sem hierarquia. | **Imagens 01** ou **02** | Três colunas, ou duas por duas. |
| Dois territórios que se encontram. | **Dados 01** ou **02** | Venn. 01 é filete com intersecção laranja; 02 tem cada bola com cor. |
| Uma proporção entre duas quantidades. | **Dados 03** | Duas bolas, área proporcional ao valor. |
| Duas fatias de um todo. | **Dados 04** | Painéis de largura proporcional. |
| Um número que é o argumento inteiro. | **Dados 05** | Número-herói em Light. No máximo dois por deck. |
| Um ranking ou uma comparação de cinco itens. | **Dados 06** | Barras de filete, a maior em laranja. |
| Quatro medidas que resumem o assunto. | **Dados 07** | Contagens sobre filete. |
| Um sistema com partes que coexistem nasce. | **Sistema 01** | O ecossistema em órbitas (das prévias do 21st.dev lidas quadro a quadro, com o duplo diamante do Africa Decoded como régua de qualidade): o logo no centro, as linhas nascem de dentro para fora, os nomes na curva; os pontos-cometa só depois de a legenda brilhar. |
| Uma parte do sistema, em detalhe. | **Sistema 02** | O mesmo diagrama entra pronto e a faixa da parte se acende; à esquerda, o detalhamento e a tabela de fios. Um slide por parte. |
| A camada que atravessa o sistema inteiro. | **Sistema 03** | Só as linhas e os pontos-cometa em laranja, circulando; à esquerda, a tabela que se destaca linha a linha. |
| Um capítulo novo começa. | **Seção** (`.sec`) | O slide laranja com a pedra branca. |
| É o fim. | **Fechamento + Slogan** | Obrigatórios, nesta ordem, sempre os dois últimos. |

Modelo que não está no mapa não existe. Se a mensagem não encaixa em nenhum, **o problema é a mensagem**.

---

## O esqueleto padrão

Um deck para o CMO tem **12 a 20 slides**. Ponto de partida, 16:

| # | Slide | Modelo |
|---|---|---|
| 01 | A capa | Capa 01 |
| 02 | A tese, em uma frase | Statement 02 |
| 03 | Abre o primeiro capítulo | Seção |
| 04 | O contexto | Título 01 |
| 05 | O que os dados mostram | Dados 06 |
| 06 | A consequência | Conteúdo 01 |
| 07 | O respiro | Statement 03 |
| 08 | Abre o segundo capítulo | Seção |
| 09 | A proposta | Título 02 |
| 10 | Como funciona | Conteúdo 04 |
| 11 | A prova | Dados 05 (o pico) |
| 12 | O que muda | Conteúdo 02 |
| 13 | Abre o fecho | Seção |
| 14 | O pedido | Título 01 |
| 15 | **Fechamento** | obrigatório |
| 16 | **Slogan** | fecha |

Nesse esqueleto, três slides laranja em dezesseis: dentro do orçamento de 15 a 20%.

---

## Checklist antes de entregar

- [ ] Todo título é afirmação com verbo, nunca tópico
- [ ] Uma mensagem por slide, uma coisa saltando por slide
- [ ] Todo número tem fonte declarada em legenda
- [ ] Nada afirmado fora do que a fonte diz (a cerca dos tokens)
- [ ] "Africa" sem acento em todo o deck
- [ ] O logo do Itaú só sobre branco (salvo a Capa 07 e o Sistema 01 a 03, exceções declaradas), e é o asset oficial
- [ ] Um acento por slide: o grifo com `data-w` idêntico ao texto da tag, até três palavras, ou a linha em laranja; o grifo duplo só nas órbitas
- [ ] Nada em loop fora da lista fechada da seção 8; toda animação termina num estado final
- [ ] Nunca dois slides laranja adjacentes
- [ ] Fechamento é o penúltimo, slogan é o último, nenhum dos dois editado
- [ ] Roteiro em `data-notes`, nada de fala na tela
- [ ] Verificador rodado, zero falha
- [ ] PDF exportado e olhado, página por página, na folha de contato

---
---

# PARTE II · A LEI

## 1. O híbrido: o que é de quem

O template segue o método do template da GUT, herdado pela Africa: o deck ensina mostrando. Cada modelo é um slide pronto e o texto de exemplo nomeia o próprio estilo. As seções editáveis são laranja e marcadas pela pedra branca. As famílias vêm em variações lado a lado. Quatro folhas de biblioteca fecham: marca, pedra, paleta, movimento.

**O que se vê é do Itaú.** Branco de base e laranja em massa. Itau Display Bold em caixa baixa na voz, Itau Text no texto. A pedra como contêiner, janela, fantasma e marcador de seção. Quinas de 16px em imagem e painel, 8px no bloco do grifo. O logo, só sobre branco (as exceções declaradas estão na seção 9).

**O que se sente é da Africa.** A grade de 12 colunas, a margem de 5.2cqw, o filete de 1px. A legenda miúda em caixa alta contra o título gigante. O dado editorial: número em Light, proporção estrita, uma cor por diagrama. O selo girando no canto de todo slide de conteúdo. O fechamento e o slogan em Pangaia.

**O que fica de fora.** O coral e o bone da Africa. As peças de Volume. A Pangaia como voz. O gradiente fora do selo. Se um slide parece só Itaú, faltou a Africa; se parece só Africa, o cliente não se reconhece.

---

## 2. A grade (herdada)

O quadro é 16:9 fixo: **100cqw por 56.25cqw**. Margem `--m` de 5.2cqw nos quatro lados. **12 colunas de 6cqw com 11 calhas de 1.6cqw = 89.6cqw**, e um span de N colunas mede **7.6N − 1.6**:

| span | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 12 |
|---|---|---|---|---|---|---|---|---|
| cqw | 21.2 | 28.8 | 36.4 | 44.0 | 51.6 | 59.2 | 66.8 | 89.6 |

Duas calhas, e só duas: a de grade (1.6cqw) e a de campo (4cqw). A unidade de respiro é 0.8cqw; todo gap vertical é múltiplo dela. Âncoras verticais: o canto do selo (até 5.3cqw), o início do canvas (10.4cqw), o pé (51.05cqw). Tecla **G** mostra a grade.

**O cabeçalho é o selo da Africa**, no canto superior esquerdo, 4.4cqw, fora da margem, na linha dos botões B e N. Injetado por JS em todo slide que não é `bare`. O miolo é o gradiente sobre branco e o mark branco chapado sobre laranja, preto e azul; o anel segue a cor do texto do slide. Sem legenda, sem número de página. A UI fixa (número, marca d'água `itaú × @africa creative/™`, setas) lê o fundo do slide corrente e troca de cor sozinha.

---

## 3. A escala de tipo

### Duas famílias do Itaú, três papéis; duas da Africa, dois lugares

| Papel | Fonte | Quando | Como |
|---|---|---|---|
| **A voz** | Itau Display Bold | Capa, título de slide e statement. | Sempre Bold, sempre caixa baixa, entrelinha fechada, tracking negativo. A palavra que importa vai no bloco laranja. |
| **O texto** | Itau Text Regular | Parágrafo, lista, nota. | Regular no corpo. Bold só no subtítulo e na palavra em destaque. Nada de Black em slide. |
| **A legenda** | Itau Text Bold, caixa alta | Rótulo, fonte do dado, data, índice, nome de seção. | Miúda, caixa alta, tracking aberto. Nunca uma frase inteira em caixa alta. |
| **O número** | Itau Display Light | Número-herói, número médio, valor de barra e de contagem. | Gigante e apertado. É o único Light do sistema: a Africa dentro do dado. |
| **O selo** | Miletus Grotesk Medium | O anel do selo e a marca d'água. | Só ali. |
| **O fecho** | PP Pangaia Light | Fechamento e slogan. | Só ali. A Africa fala uma vez, no fim. |

**Fallback.** Itau Display e Itau Text são proprietárias. O font stack declara as duas primeiro; onde estiverem instaladas, o deck usa. Embutida vai a Figtree (OFL, variável 300 a 700). É decisão da Africa, pendente de OK; se os arquivos reais chegarem, entram no lugar.

### A tabela

1cqw = 19.2px num quadro de 1920.

| Estilo | cqw | px @1920 | Fonte e peso | Entrelinha | Tracking |
|---|---|---|---|---|---|
| Hero | 9.4 | 180 | Display 700 | .92 | −.03em |
| **Statement** | 8 | 154 | Display 700 | .96 | −.03em |
| **Título** | 5.6 | 108 | Display 700 | 1 | −.025em |
| **Título curto** | 4.6 | 88 | Display 700 | 1.06 | −.025em |
| Número-herói | 15 | 288 | Display 300 | .8 | −.05em |
| Número médio | 7 | 134 | Display 300 | .88 | −.03em |
| **Subtítulo** | 2.6 | 50 | Text 700 | 1.1 | −.01em |
| **Corpo grande** | 2.3 | 44 | Text 400 | 1.3 | −.01em |
| **Corpo regular** | 1.75 | 34 | Text 400 | 1.5 | 0 |
| **Corpo pequeno** | 1.35 | 26 | Text 400 | 1.55 | 0 |
| **Legenda** | 1 | 19 | Text 700 caixa alta | 1 | .14em |

O slide de seção tem escala própria: o statement em 9cqw e a linha de doutrina em corpo pequeno Bold, ancorada no pé.

**A régua do corpo (17/09), para a frase morar dentro da Moldura.** Pela linha mais larga da frase: até 12 caracteres, Statement; até 17, Título; acima, Título curto (o degrau entre o Título e o Subtítulo). Até três linhas, quatro num statement sem apoio. A narrativa pode declarar o corpo em cqw quando a frase pede (o Main KPI da V2 usa 4,8, entrelinha 1,16, caixa de 92cqw). A régua foi medida na Figtree 700, cerca de 0,47em por caractere: com a Itau Display, remedir.

**A regra que rege a tabela:** a hierarquia é o Bold gigante em caixa baixa contra uma legenda miúda em caixa alta. O peso intermediário não faz hierarquia: Display é 700, Text é 400, o Light só aparece no número.

**O grifo.** A mecânica da Africa com a tinta do Itaú: bloco laranja varrendo a palavra, texto em branco, quina de 8px. Sobre laranja inverte: bloco branco, palavra laranja. Uma por slide, até três palavras. É a única ênfase dentro de uma frase.

**O segundo acento (17/09).** Uma linha inteira ou uma palavra em laranja, sem bloco (`.fa-ora`; na narrativa, `[texto]`). Nunca corpo de texto. Convive com o grifo, mas a regra é a mesma: um acento por slide. O grifo duplo só existe nas órbitas (Título 04).

---

## 4. As regras de composição

1. **Uma mensagem por slide.** Se a frase de resumo precisa de "e", são dois slides.
2. **Título é afirmação, não tópico.** O tópico vai na legenda.
3. **Exatamente uma coisa salta.** O número, a pedra, a palavra em bloco, a imagem.
4. **Teto de 7 objetos por slide.**
5. **Tetos de caractere.** Statement 90 · corpo grande 220 · corpo regular 340 · célula de grade 60 · item de lista 60.
6. **A margem é moldura.** 5.2cqw intocáveis. Sangria só declarada: a pedra que vaza, a imagem em meia tela, o painel de dado. O selo do cabeçalho é a única coisa que mora fora da margem.
7. **Todo número tem fonte declarada**, em legenda.
8. **O gráfico domina e o texto encolhe.** Círculo, painel ou barra ocupa ao menos 60% da área viva. Proporcional ao valor, filete de 1px, preto chapado, cinza do Itaú ou laranja numa região só. Nunca gradiente, sombra ou volume em gráfico. Título, corpo e fonte nunca encostam na circunferência.
9. **Imagem entra em base64**, teto de 400KB. Texto sobre imagem só com véu.
10. **A quina é do Itaú, o dado é da Africa.** Imagem, painel e célula levam 16px; barra, filete e painel de dado ficam retos. Tipo nunca leva contêiner arredondado, exceto o bloco do grifo.
11. **A pedra nunca leva o logotipo dentro.** Isso é o logo, e o logo é asset. A pedra é contêiner, janela, fantasma ou marcador. Só translada em Y; nunca gira.
12. **O logo do Itaú só sobre branco.** Nas capas coloridas o nome vai em legenda até o asset oficial entrar. As exceções declaradas (Capa 07, Sistema 01 a 03) estão na seção 9.
13. **O mark da Africa só dentro do selo.** Nunca solto num slide do Itaú, nunca como marcador, nunca sangrando.
14. **O roteiro vive em `data-notes`.** Slide não é documento.

---

## 5. O ritmo do deck

- **Respiro a cada 4 ou 5 slides de conteúdo:** um statement, sem dado e sem grade.
- **Capítulo abre com o slide de seção** (laranja, pedra branca). De 3 a 6 slides por capítulo.
- **Nunca dois slides laranja adjacentes.** Nem capa laranja seguida de seção.
- **Número-herói: no máximo 2 por deck**, nunca adjacentes.
- **Composição de pedras (Título 03): no máximo 2 por deck**, com pelo menos 3 slides entre uma e outra.
- **Nunca em sequência:** grade depois de grade, herói depois de herói, dois slides coloridos.
- **Um pico por deck.**
- **O fechamento é obrigatório e é sempre o penúltimo. O slogan fecha.**

---

## 6. A cor no slide

**Branco é a base.** Laranja é a seção e no máximo um momento de ênfase; preto é a capa da pedra preta e o modo escuro; azul só para Uniclass e Personnalité. Num deck de verdade, superfícies coloridas somam 15 a 20%. Nunca duas adjacentes.

**Laranja é a cor, e pode ser massa:** capa, seção, bloco do grifo, pedra, região de destaque num diagrama (a intersecção do Venn, a bola maior, a maior barra, o painel de cima), barra de progresso da UI. Nunca em texto corrido; em texto, só o segundo acento, uma linha ou uma palavra (seção 3).

**Preto é tinta e pedra.** Tipografia, filete de 1px, a pedra preta da composição, o fundo da Capa 04.

**O azul marinho (`--azul-d`, #000D3C) é a superfície escura do sistema** quando o preto pesa demais (Statement 07, o Main KPI da V2). O azul (#000066) segue reservado a Uniclass e Personnalité.

**Os cinzas do Itaú fazem apoio:** #4C4C4C no texto de apoio e na legenda, #E3E5E8 na segunda bola e na terceira pedra, #F1F2F4 no palco de imagem.

**O gradiente da Africa só existe dentro do mark, no centro do selo**, e só sobre branco. Sobre laranja, preto e azul o mark vai branco chapado. Nunca solto, nunca em texto, nunca em barra.

**O coral e o bone da Africa não entram.** O laranja digital antigo do Itaú (#EC7000) também não: os tokens oficiais de 2025 dizem #FF6200.

---

## 7. O que tem no template

53 slides, na ordem em que aparecem. Os de 17/09 nasceram no deck Itaú fim de ano V2 e entraram como opções de catálogo em 18/09.

### Abertura
**Marca** · o logo do Itaú, o × e o selo da Africa, no mesmo tamanho.
**Tipografia** · duas famílias do Itaú, três papéis; Miletus e Pangaia em dois lugares.
**A regra** · o que se vê é do Itaú, o que se sente é da Africa.

### Modelos editáveis
**Estilos** · o especimen.
**Capas** · 01 branca com o logo e a pedra sangrando · 02 imagem na metade esquerda · 03 laranja com a pedra branca em fantasma · 04 a pedra preta: preto com a pedra laranja no alto · 05 azul, centrada, para Uniclass e Personnalité · 06 a janela: imagem recortada pela pedra · 07 a anatomia: preta, o quadrado vira a pedra, quatro contornos respiram em onda, o logo chega por último (ensina a única capa com o logo sobre preto, o Statement em três linhas e o acento de texto).
**Statement** · 01 centrado com as pedras em fantasma · 02 centrado limpo · 03 à esquerda · 04 à esquerda com corpo pequeno · 05 a frase com a Moldura em laranja e o apoio com ritmo: itens em legenda que entram um a um, separados pela pedra miúda, e o fecho em corpo grande (ensina o grifo invertido e a lista que termina num ponto) · 06 a frase com a Moldura em preto e o apoio cinza (ensina a Moldura, o marcador de pedra e a régua do corpo pela linha mais larga) · 07 a frase com a Moldura em azul marinho, a legenda miúda acima e uma linha em laranja (ensina a superfície escura, a legenda que rotula e o segundo acento).
**Título** · 01 centrado com subtítulo · 02 imagem à esquerda · 03 as pedras à esquerda (laranja, preta, cinza, flutuando) · 04 as órbitas: a pedra com um texto dentro bate duas vezes e deixa duas faixas, os sinais na primeira e os assuntos com hastes na segunda (ensina o diagrama que acaba, sem loop, os rótulos que viram para dentro e o único grifo duplo).
**Conteúdo** · 01 quatro blocos · 02 imagem à direita · 03 corpo à direita e imagem embaixo · 04 lista com filete · 05 o poema em máquina de escrever: página dupla, corpo pequeno, uma tinta só, cada linha se escrevendo na ordem de leitura (ensina o slide sem Moldura e sem selo, e o texto que se lê inteiro).
**Imagens** · 01 três colunas · 02 duas por duas. Quina de 16px.
**Dados** · 01 Venn de filete com a intersecção laranja · 02 Venn com cada bola em cor (preto, cinza, laranja) · 03 duas bolas proporcionais, a grande laranja · 04 painéis proporcionais, o de cima laranja · 05 número-herói em Light · 06 barras de filete, a maior laranja · 07 contagens sobre filete.
**Sistema** · o ecossistema em órbitas, o guia de uma solução com partes que coexistem: o mesmo diagrama, no mesmo lugar, em três estágios · 01 nasce: o núcleo (o logo sobre a pedra branca) bate, cada linha nasce de dentro para fora e o nome chega deslizando na curva; a legenda da camada brilha três vezes e a cada brilho uma leva de pontos-cometa passa a circular (ensina a ordem das entradas, o brilho como única sombra difusa e o logo sobre preto como exceção) · 02 momento: entra pronto, o núcleo bate uma vez e a faixa da parte se acende a partir do nome; à esquerda a legenda, a função como título, o incipit, a definição e a tabela de fios (ensina o detalhamento de uma parte e a tabela de fios) · 03 camada: sem faixa, sem brilho, sem batida, só as linhas e os pontos em laranja circulando; à esquerda a tabela que se destaca linha a linha (ensina a camada transversal e a tabela com o fio que se desenha).

### Biblioteca
**Marca** · o logo do Itaú sobre branco, o mark da Africa nos dois preenchimentos, o selo.
**Pedra** · laranja, preta, branca sobre laranja, a janela.
**Paleta** · os seis hex do Itaú e a fita do gradiente da Africa.
**Movimento** · a língua do movimento: os quatro verbos de entrada, o tempo por variável, os loops permitidos e a regra do estado final.

### Fecho
**Fechamento** · o selo, a frase final do manifesto da Africa em Pangaia, a linha de co-marca. Obrigatório.
**Slogan** · a promessa da casa, em Pangaia.

---

## 8. Movimento

| Curva | Valor | Duração | Onde |
|---|---|---|---|
| Expo out · decelerate_02 | `cubic-bezier(.19,1,.22,1)` | .5s | A principal. É a curva da Africa e o token de movimento do Itaú: os dois sistemas se encontram nela. |
| In out forte | `cubic-bezier(.87,0,.13,1)` | .6s | Painel, float das pedras. |
| Entrada lenta | `cubic-bezier(.16,1,.3,1)` | 1.4s | Hero e statement entrando. |
| Vivid | `cubic-bezier(.22,1,.36,1)` | .8s a 1.2s | As batidas: a faixa que congela nas órbitas (`faOrbFreeze`) e o pulso do núcleo do ecossistema (`faEcoPulse`). Estava reservada nos tokens; em uso desde 17/09. |
| Micro hover | `ease` | .2s | Interface. |

O reveal escalonado usa `--d` no `style` de cada elemento, de .06s a .1s entre irmãos. Os loops do sistema são o `spin` de 12s do selo e o `afFloat` de 3s da pedra, que só translada em Y. **O observer põe `.visible` ao entrar e tira ao sair**: tudo re-anima na revisita. Nenhum slide é 100% estático.

### A língua do movimento (17/09)

Quatro verbos de entrada, na camada `fa-` do head:

| Verbo | Classe | O que faz |
|---|---|---|
| Entra | `.fa-in` | Opacidade 0 a 1 e sobe 1cqw (`faIn`, .9s, expo out). `.slow`: 1.4cqw em 1.4s, na curva lenta. |
| Desenha-se | `.fa-draw` | O traço corre o caminho inteiro (`faDraw`, `stroke-dasharray:1` com `pathLength="1"`). Sem `vector-effect`: o Chrome tracejaria. |
| Nasce | `.fa-pop` | Escala 0 a 1 (`faPop`, .7s, expo out). |
| Pulsa | `.fa-pulse` | 0 a 1.16 a 1 (`faPulse`, 1s): a batida. |

O tempo é por variável: `--d0` é o instante em que a peça entra, `--dur` a duração, `--n` o número de passos. Tudo dispara em `.slide.visible` e **termina num estado final que fica na tela**; `@media print` e `prefers-reduced-motion` mostram esse estado.

**A lista fechada dos loops.** Além do `spin` do selo e do `afFloat` da pedra, só seis animações da camada podem ser `infinite`, e o verificador confere:

| Loop | Onde | Ritmo |
|---|---|---|
| `faResBreath` | A Moldura respira | 6s, escala 1 a 1.06 (3% quando aberta) |
| `faAnaPulse` | A pedra da anatomia pulsa | 3.6s, 3% |
| `faAnaRes` | Os contornos da anatomia respiram em onda | 3.6s, escala 1.10 |
| `faEcoBreath` | O núcleo do ecossistema respira | 5s |
| `faEcoSpin` | Os pontos circulam nas órbitas | 16, 22, 29, 37, 46s por volta, de dentro para fora |
| `faEcoTwinkle` | O halo dos pontos brilha | 1.9s, cada ponto no seu tempo |

Tudo o mais corre uma vez e para: a máquina de escrever anda em passos de um caractere e para; as órbitas acabam quando a segunda faixa congela; a faixa do momento se acende e fica. **Nada gira além do selo e das órbitas dos pontos**; o nome que desliza 6° na curva ao entrar (`faEcoLb`) é a única outra rotação. Os 28 keyframes do template são uma lista fechada, cada um com dono: o verificador acusa qualquer keyframe a mais ou a menos.

---

## 9. O que nunca fazer

- Pôr o logotipo dentro da pedra solta, ou a pedra no lugar do logo
- Logo do Itaú sobre laranja, preto ou azul, fora das exceções declaradas abaixo (não há versão neste sistema)
- Redesenhar, recolorir ou esticar o logo do Itaú
- Rotacionar, espelhar, distorcer ou sombrear o mark da Africa; usá-lo solto fora do selo
- Gradiente fora do mark do selo
- Coral, bone ou #EC7000 em qualquer lugar
- Laranja em texto corrido; dois slides laranja adjacentes
- Escrever "África" com acento
- Número sem fonte declarada
- Parafrasear o manifesto da Africa
- Black em slide; Light fora do número
- Pangaia fora do fecho; Miletus fora do selo
- Quina arredondada em barra, filete ou tipo; quina reta em imagem e painel
- Peça de Volume da Africa num slide do Itaú
- Slide 100% estático
- Cortar o fechamento ou o slogan
- Encolher o corpo para caber mais texto
- Afirmar o que a cerca `verification.notVerified` proíbe
- Loop fora da lista fechada da seção 8; animação sem estado final
- Sombra difusa (`text-shadow`, `drop-shadow`) fora do brilho da legenda do sistema
- Grifo duplo fora das órbitas

### As exceções declaradas (17/09)

Nasceram no deck Itaú fim de ano V2, aprovadas slide a slide, e entraram no template como regra escrita, não como brecha. O verificador confere cada uma.

- **O logo do Itaú sobre preto**, só na anatomia da capa (Capa 07) e no núcleo do ecossistema (Sistema 01 a 03). Nasce do mesmo símbolo `#itau`, em laranja, sobre uma pedra branca 4% menor (as letras do vetor são vazadas). Token pendente: confirmar no brand center se o logo sobre fundo escuro é uso permitido e qual é a área de proteção.
- **Sombra difusa**, só o halo do brilho da legenda do sistema (`faEcoGlow`). É a única do sistema.
- **Grifo duplo**, só nas órbitas (Título 04).
- **Loops**, só a lista fechada da seção 8. A pedra continua sem girar: o que gira são os pontos nas órbitas, e o nome desliza 6° na curva ao entrar.
- **A pedra sem sombra ou volume** continua valendo para a pedra sólida. A Moldura usa um desfoque leve nos contornos (veludo, não linha); não é sombra.

---

## 10. Verificar e exportar

**Verificar:**
```
/usr/bin/python3 "build/scripts/check-itau.py"
```

**Montar o template** (só quando o próprio template muda, nunca para um deck):
```
python3 "build/scripts/build-itau.py"
```
O build importa `scripts/itau_components.py` (os SVGs do catálogo e o keyframe do morph da capa) e injeta `src/04-camada.css` no head, no placeholder `{{CAMADA_CSS}}`. Mudar a forma ou o movimento de um componente é mudar no módulo, e o deck V2 acompanha no build dele.

**Exportar em PDF 16:9 e olhar:**
```
zsh "build/scripts/render-itau.sh" slides
/usr/bin/python3 "build/scripts/contact-sheet.py" <pdf> <png> 6 300
```
Chrome headless nesta máquina escreve o arquivo e não encerra; o script roda em background, espera o PDF e mata só os processos do perfil de scratchpad. A folha de contato lê o deck inteiro numa imagem; detalhe suspeito vira uma segunda montagem, maior, só das páginas em questão (`contact-sheet.py <pdf> <png> 2 760 3,12,21`).

**Atalhos:** setas, espaço, PgUp/PgDn, j/k, Home/End · **N** roteiro · **B** modo · **G** grade · `#s7` abre no slide 7 · `?mode=dark`.

---

*Itaú × Africa Creative/™ · Master Slides v1.1 · 18/09/2026 · derivado de `itau-brand-tokens.json` v1.1 e do Master Slides da Africa v4.3 · os componentes de 17/09 são derivação declarada da Africa, nascidos no deck Itaú fim de ano V2*
