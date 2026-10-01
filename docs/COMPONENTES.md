# Componentes

O índice do sistema. A **forma** de cada componente vive em [`../build/scripts/itau_components.py`](../build/scripts/itau_components.py). O **movimento** vive em [`../build/src/04-camada.css`](../build/src/04-camada.css), com prefixo `fa-`. A **descrição normativa**, com anatomia, tempo, superfícies permitidas, regras e origem, vive no grupo `patterns` de [`../design-system/itau-brand-tokens.json`](../design-system/itau-brand-tokens.json).

Quem muda a forma, muda no módulo Python, roda o build e roda o check. Nunca edite o HTML entregue à mão: ele é produto de build.

---

## Os nove padrões animados

Tudo aqui é **criação da Africa**, nascida no deck Itaú fim de ano V2 em 17/09/2026. É derivação declarada, nunca fato do Itaú.

Cada padrão só corre em `.slide.visible`, por tempo: `--d0` é o instante em que a peça entra, `--dur` a duração, `--n` o número de passos. Todos terminam num estado final que fica. Impressão e movimento reduzido mostram esse estado final.

| Padrão | Papel | Onde aparece no template |
|---|---|---|
| `movimento` | As primitivas da língua do movimento. Quatro verbos, um relógio: entra (`.fa-in`), desenha-se (`.fa-draw`), nasce (`.fa-pop`), pulsa (`.fa-pulse`). | Em todo lugar |
| `tituloCurto` | O degrau entre o Título (5.6cqw) e o Subtítulo (2.6cqw), para quando a linha mais larga passa de 17 caracteres. | Statement 06 e 07 |
| `acentoTexto` | O segundo acento: uma linha inteira ou uma palavra em laranja, sem o bloco do grifo. | Capa 07 e Statement 07 |
| `moldura` | A frase com os contornos da pedra. Uma abertura de palco em volta do texto. | Os slides de Statement |
| `anatomiaCapa` | A capa onde o quadrado de quinas redondas vira a pedra, os contornos respiram e por último chega o logo. | Capa 04 |
| `orbitas` | A pedra-coração que bate e deposita as faixas onde vivem os sinais e os assuntos. | Dados |
| `poemaMaquina` | A página dupla de livro de poesia, escrita à máquina: um caractere por passo, na ordem de leitura. | Conteúdo 05 |
| `ecossistema` | O guia de um sistema com partes que coexistem: o núcleo, cinco órbitas na curva, os pontos-cometa. | Sistema 01, 02 e 03 |
| `tabelas` | Duas tabelas de fio: a que entra linha a linha e a que se destaca linha a linha. | Sistema 02 e 03 |

### As duas regras de movimento que já quebraram um deck

1. **Nunca `vector-effect` junto com `pathLength`.** O Chrome tracejaria a linha.
2. **Animação por tempo, não por `scroll`.** Tudo dispara no observer do template, em `.slide.visible`.

### As curvas

| Nome | Valor | Onde |
|---|---|---|
| `expoOut` | `cubic-bezier(.19,1,.22,1)` | A entrada padrão |
| `slowIn` | `cubic-bezier(.16,1,.3,1)` | Entrada lenta, morph, Moldura |
| `vivid` | `cubic-bezier(.22,1,.36,1)` | As órbitas |

---

## O catálogo de slides do template

As 53 telas de [`../master-slides/itau-slides-template.html`](../master-slides/itau-slides-template.html), na ordem. O número é a ordem de tela. Cada slide carrega o próprio roteiro em `data-notes`: aperte `N` dentro do deck para ler.

| # | Slide | Superfície e variante | O que é |
|---|---|---|---|
| 1 | Marca | `bare ctr` | O momento de marca. |
| 2 | Tipografia | base | Duas famílias do Itaú, três papéis. |
| 3 | A regra | `top` | O que é de quem. |
| 4 | Seção · Estilos | `sec bare laranja` | A pedra branca sobre laranja marca seção editável: é o lápis da GUT e o quadrado coral da Africa, traduzidos. |
| 5 | Estilos · especimen | `top` | Como o Styles da GUT: cada estilo nomeado pelo próprio texto. |
| 6 | Seção · Capas | `sec bare laranja` | Seis fundos para a mesma capa: branco, imagem, laranja, a pedra preta, azul e a janela. |
| 7 | Capa 01 | `bare` | Branca. |
| 8 | Capa 02 | `bare` | Como a capa Annual Reports da GUT: imagem na metade esquerda, título na direita, o logo do Itaú no pé da coluna de texto. |
| 9 | Capa 03 | `bare laranja` | Laranja. |
| 10 | Capa 04 | `bare inv` | A pedra preta. |
| 11 | Capa 05 | `bare ctr azul` | Azul, composição centrada, a pedra pequena em branco flutuando sobre o título. |
| 12 | Capa 06 | `bare` | A janela: a imagem recortada pela pedra, na metade direita, e o título à esquerda. |
| 13 | Capa 07 | `bare inv` | Preta, com a anatomia da pedra: forma, contorno e o logo, como no filme da Pentagram para o Itaú (2024). |
| 14 | Seção · Statement | `sec bare laranja` | Uma frase por tela, duas ou três linhas, em Display Bold. |
| 15 | Statement 01 | `ctr` | Centrado, com a pedra em fantasma nos cantos. |
| 16 | Statement 02 | `ctr` | Centrado e limpo. |
| 17 | Statement 03 | base | À esquerda, sem mais nada. |
| 18 | Statement 04 | `top` | Statement à esquerda com corpo pequeno embaixo. |
| 19 | Statement 05 | `ctr laranja` | A frase com a Moldura em laranja (os contornos em laranja escuro, tom sobre tom) e o apoio com ritmo: uma legenda em caixa alta com itens que entram um a um, separados pela pedra miúda, e o fecho embaixo, em corpo grande e branco. |
| 20 | Statement 06 | `ctr inv` | A frase com a Moldura: seis contornos da pedra, tom sobre tom, em degradê de opacidade e com um desfoque leve, respirando devagar atrás da frase (6s, 6%). |
| 21 | Statement 07 | `ctr azul marinho` | A frase com a Moldura em azul marinho (o tom escuro do azul, --azul-d), com a legenda miúda acima da frase e a segunda linha inteira em laranja: o segundo acento do sistema, texto laranja sem bloco, para uma linha, nunca para corpo. |
| 22 | Seção · Título | `sec bare laranja` | O título é afirmação, nunca tópico. |
| 23 | Título 01 | `ctr` | Centrado, com o bloco na palavra, e o subtítulo embaixo. |
| 24 | Título 02 | `bare` | Imagem na metade esquerda, título e corpo à direita. |
| 25 | Título 03 | `bare` | As pedras na metade esquerda, no lugar da textura da GUT e do Volume da Africa: laranja, preta e cinza, flutuando só em Y. |
| 26 | Título 04 | base | Título à esquerda (4cqw, três linhas curtas, o grifo pode ser duplo), o apoio em três linhas fixas embaixo, o bloco centrado na altura do diagrama; à direita, grande, as órbitas: a pedra com um texto dentro bate duas vezes e cada batida solta um contorno dela mesma que cresce e congela numa faixa cheia, tom sobre tom (a Matéria, como o One Sheeter do Yummly). |
| 27 | Seção · Conteúdo | `sec bare laranja` | Teto de sete objetos por slide. |
| 28 | Conteúdo 01 | `top` | Título e quatro blocos em duas colunas. |
| 29 | Conteúdo 02 | `top` | Título e corpo à esquerda, imagem ocupando a direita inteira. |
| 30 | Conteúdo 03 | `top` | Título à esquerda, corpo à direita, imagem embaixo à esquerda. |
| 31 | Conteúdo 04 | `top` | Título à esquerda, lista com filete vertical à direita. |
| 32 | Conteúdo 05 | `bare` | O poema como página de livro, escrito à máquina: cada linha se escreve da esquerda para a direita em passos de um caractere (22ms cada), e só depois a próxima, na ordem de leitura (página esquerda, depois direita); o grifo por último. |
| 33 | Seção · Imagens | `sec bare laranja` | Duas grades. |
| 34 | Imagens 01 | base | Três colunas em proporção crescente, a primeira dividida em duas. |
| 35 | Imagens 02 | base | Quatro imagens, duas por duas. |
| 36 | Seção · Dados | `sec bare laranja` | Editorial, não dashboard. |
| 37 | Dados 01 | `top` | O Venn de filete com a intersecção em laranja. |
| 38 | Dados 02 | `top` | Cada bola com cor: preto, cinza do Itaú e a intersecção em laranja. |
| 39 | Dados 03 | `top` | Duas bolas proporcionais entre si, pela área. |
| 40 | Dados 04 | base | Painéis de largura proporcional ao valor, com o número ao lado e o título em cima. |
| 41 | Dados 05 | `top` | O número-herói: título em cima, filete, e no pé o número em Display Light gigante com subtítulo, corpo e fonte ao lado. |
| 42 | Dados 06 | `top` | Barras de filete: título, rótulo, trilho de 1px, preenchimento proporcional ao valor, número à direita. |
| 43 | Dados 07 | base | Contagens: quatro números em Light médio sobre filete, rótulo em legenda, fonte no pé. |
| 44 | Seção · Sistema | `sec bare laranja` | O ecossistema em órbitas, o guia gráfico de uma solução com partes que coexistem: o logo do Itaú no centro, cada movimento como uma faixa entre linhas com o nome na curva, e os pontos-cometa que circulam em todas as linhas. |
| 45 | Sistema 01 | `inv` | O ecossistema nasce. |
| 46 | Sistema 02 | `inv` | O momento. |
| 47 | Sistema 03 | `inv` | A camada. |
| 48 | Biblioteca · Marca | `top` | Os dois logos e a regra de cada um. |
| 49 | Biblioteca · Pedra | `top` | A forma do cliente, solta. |
| 50 | Biblioteca · Paleta | `top` | Os hex do Itaú, lidos dos tokens oficiais do site. |
| 51 | Biblioteca · Movimento | `top` | A língua do movimento (17/09): quatro verbos de entrada, o tempo por variável, os loops permitidos e a regra que fecha tudo: toda animação termina num estado final que fica na tela, e a impressão mostra esse estado. |
| 52 | Fechamento | `bare ctr s-closing` | Obrigatório em todo deck da Africa, mesmo no do Itaú. |
| 53 | Slogan | `bare ctr` | A última tela é a promessa da casa, em Pangaia. |

Total: 53 slides.

---

## As variantes de superfície, nas classes

| Classe | Superfície |
|---|---|
| (nenhuma) | branca |
| `laranja` | laranja `#FF6200` |
| `inv` | preta |
| `azul` | azul `#000066` |
| `azul marinho` | azul marinho `#000D3C` |

| Classe | Composição |
|---|---|
| `top` | Conteúdo ancorado no alto |
| `ctr` | Conteúdo centrado |
| `bare` | Sem o selo da Africa no canto |
| `sec` | Slide de seção |
| `s-closing` | O fechamento obrigatório |
