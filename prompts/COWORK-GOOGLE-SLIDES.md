# Levar este sistema para o Google Slides

Prompt pronto para um agente montar decks do Itaú × Africa direto no **Google Slides**, em vez de HTML.

---

## Antes de colar: quem é quem

Vale corrigir um nome, porque isso muda qual ferramenta você abre.

| Nome | De quem é | O que é |
|---|---|---|
| **Cowork** | **Anthropic** | Software de escritório com IA, preview em 13/01/2026, app macOS para assinantes Max. Add-ins de Word, Excel e PowerPoint em GA desde maio de 2026 |
| **ChatGPT Work** | **OpenAI** | O equivalente da OpenAI, lançado em 09/07/2026. Um modo dentro do ChatGPT que recebe objetivos e executa projetos de vários passos. Roda em GPT-5.6 com tecnologia do Codex por dentro |
| **Codex** | **OpenAI** | O agente de código. Lê `AGENTS.md` na raiz do repositório |

Não existe "Cowork do GPT". Se você quer o lado da OpenAI, o produto é o **ChatGPT Work**. O prompt abaixo funciona nos três.

## A habilidade do Google Slides

A OpenAI publica uma **agent skill** chamada `google-slides`. Instalação:

```bash
npx skills add https://github.com/openai/plugins --skill google-slides
```

Ela funciona em Codex, Cursor, Windsurf e em outras ferramentas que suportam agent skills.

**O detalhe que decide tudo:** essa skill **não cria apresentação em branco**. Ela segue template, edita deck existente e repara estrutura. Para deck novo sem template de referência, ela encaminha para o plugin `@presentations`.

Tradução prática: o sistema Itaú × Africa não entra como arquivo HTML nem como JSON de tokens. **Ele tem que existir primeiro como um deck nativo do Google Slides**, e a skill lê o design daquele deck. Fazer esse template é um trabalho de uma vez.

---

## Passo 1 · Criar o template nativo, uma vez

Isso você faz à mão (ou com o ChatGPT Work no modo Computer Use). É o investimento que destrava todo o resto.

1. Novo Google Slides. **Arquivo → Configuração da página → Personalizado: 13,333 × 7,5 polegadas.** Isso dá uma página de **960 × 540 pontos** e faz `1cqw = 9,6pt` exatos. Use essa medida: ela é a que menos briga com os mínimos de corpo da skill.
2. No **Editor de temas** (Slide → Editar tema), monte os layouts a partir do catálogo em [`../docs/COMPONENTES.md`](../docs/COMPONENTES.md). Comece por **oito**, que cobrem 80% de qualquer deck:
   - Capa branca · Capa laranja · Capa preta
   - Seção (pedra branca sobre laranja)
   - Statement centrado
   - Título e conteúdo
   - Dado (número-herói)
   - Fechamento e Slogan
3. Cadastre a paleta em **Tema → Cores** com os seis hex da tabela abaixo.
4. Fontes: a Itau Display e a Itau Text são proprietárias. No Google Slides, use **Figtree**, que está no catálogo do Google Fonts, exatamente como o sistema faz no HTML.
5. Para a **pedra** e o **selo da Africa**, suba os SVGs de [`../design-system/assets/`](../design-system/assets/) como imagem em cada layout. O Google Slides não desenha superelipse: a pedra entra como imagem, não como forma.
6. Deixe o deck **compartilhável** e guarde a URL. É ela que você vai dar ao agente.

---

## Passo 2 · O prompt

Cole isto inteiro, trocando o que está entre `<>`:

```
Monte uma apresentação no Google Slides seguindo um template existente.

TEMPLATE DE REFERÊNCIA (não criar deck em branco, seguir este)
<cole aqui a URL do Google Slides do template Itaú × Africa>

Leia esse deck primeiro, monte o catálogo de design dele e use os layouts que já
existem lá. Não invente layout novo. Não mude a tipografia, a proporção da
página nem os elementos estruturais do template.

O ASSUNTO
Tema: <assunto do deck>
Plateia: CMO do Itaú. Quem apresenta: o VP da Africa Creative.
Objetivo: <o que a plateia tem que decidir ou sentir no fim>
Material de origem: <anexe ou cole: briefing, dados, roteiro>

A IDEIA DO SISTEMA, EM UMA LINHA
Superfície Itaú, assinatura Africa. O que se vê é do cliente: branco, laranja
#FF6200, a pedra, títulos em caixa baixa, quinas arredondadas. O que se sente é
da agência: grade de 12 colunas, filete de 1px, legenda miúda contra título
gigante, número grande em peso Light, selo no canto.

A PALETA, FECHADA
#FF6200 laranja, a cor do cliente. Pode ser massa: capa, seção, grifo, pedra,
          uma região de diagrama.
#FFFFFF branco, a base. O deck é claro primeiro.
#000000 preto: tinta, filete de 1px, capa preta.
#000066 azul: só quando o assunto é Uniclass ou Personnalité. Nunca ao lado do
          laranja em massa.
#000D3C azul marinho: o escuro quando o preto pesa demais.
#4C4C4C cinza: texto de apoio, legenda, fonte do dado.
Nada fora desses seis. Nada de coral, nada de bege.
O laranja é #FF6200, não #EC7000.

A TIPOGRAFIA, EM PONTOS (página de 960 × 540 pt)
Capa ................ 90 pt, Bold, caixa baixa
Statement ........... 77 pt, Bold, caixa baixa
Título de slide ..... 54 pt, Bold, caixa baixa
Título curto ........ 44 pt, Bold, caixa baixa
Número-herói ....... 144 pt, Light
Número médio ........ 67 pt, Light
Subtítulo ........... 25 pt, Bold
Corpo grande ........ 22 pt, Regular
Corpo ............... 17 pt, Regular
Legenda ............. 14 pt, Bold, CAIXA ALTA, tracking aberto
Entrelinha fechada no título (0,92 a 1,06). Tracking negativo no título.

A RÉGUA DO TÍTULO, pela linha mais larga da frase
Até 12 caracteres: Statement, 77 pt.
Até 17 caracteres: Título, 54 pt.
Acima de 17: Título curto, 44 pt.
No máximo três linhas. Quatro só num statement sem texto de apoio.

A HIERARQUIA
Bold gigante em caixa baixa contra uma legenda miúda em caixa alta. O peso
intermediário não faz hierarquia: ou é Bold, ou é Regular, e o Light só aparece
no número. Um acento de cor por slide, não dois.

A GRADE
Margem de 50 pt nos quatro lados. 12 colunas de 58 pt com calha de 15 pt.
Selo no canto superior, até 51 pt do alto. O conteúdo começa em 100 pt do alto.
O pé fica em 490 pt.

O QUE EU QUERO QUE VOCÊ IGNORE DO SEU PADRÃO
Este sistema é tipográfico, não ilustrado. Não force dois a quatro visuais por
slide. Muitos slides são só a frase, e isso é a intenção: quando o gráfico dá
spoiler da frase ou quebra a leitura, a frase sozinha ganha. Use imagem quando
a imagem é o argumento, não para encher.
Também não use cartão, pílula, selo de status nem grade de caixinhas. A
composição é uma só, chapada na tela.

DADO E FONTE
Todo número, dado de mercado, benchmark ou citação entra com a fonte escrita no
slide, em cinza #4C4C4C, 14 pt, no pé. Se eu não te der a fonte, não invente o
número: escreva "FONTE PENDENTE" e me avise na lista do fim.
Não afirme nada sobre prêmios, market share, número de clientes ou de agências,
cores de segmento do Itaú ou regras do brand book oficial do Itaú. Nada disso
está verificado.

O FIM DO DECK, OBRIGATÓRIO
Dois slides, nesta ordem, sem editar uma palavra:
Penúltimo: "Somos a Africa: a agência que nasce e se desafia todos os dias,
para nunca deixar de ser a Africa Creative/™."
Último: "A agência das marcas mais desejadas, admiradas e valiosas do Brasil."

GRAFIA
"Africa" sem acento. É regra de marca.
Sem travessão longo no texto do slide. Frase curta e ponto.

A ORDEM DE TRABALHO
1. Escreva o roteiro em prosa corrida primeiro e me mostre. Texto antes de
   slide. Não comece a montar sem meu ok no roteiro.
2. Para cada bloco do roteiro, diga qual layout do template você vai usar.
3. Só então monte, em lotes pequenos, conferindo a miniatura de cada slide que
   você tocar.
4. Ponha o roteiro de fala nas notas do apresentador, não na tela.
5. Nada pode transbordar nem quebrar linha de um jeito que você não escolheu.
   Corrija toda sobreposição antes de me entregar.
6. Entregue o Google Slides editável, não imagem exportada.

NO FIM, ME DIGA
O que ficou pela metade. O que é suposição sua. Que número está sem fonte. Que
regra do template você teve que esticar, e por quê.
```

---

## A tabela de conversão, se você precisar de outro tamanho de página

O sistema é desenhado em `cqw`, que é "por cento da largura do quadro". Para virar ponto, multiplique pelo fator da sua página:

| Página | Medida | Fator (`1cqw` em pt) |
|---|---|---|
| Widescreen grande (**recomendada**) | 13,333 × 7,5 in | **9,6 pt** |
| Padrão 16:9 do Google Slides | 10 × 5,625 in | 7,2 pt |

| Papel | cqw | pt em 960 | pt em 720 |
|---|---|---|---|
| Capa (hero) | 9,4 | 90,2 | 67,7 |
| Statement | 8 | 76,8 | 57,6 |
| Título | 5,6 | 53,8 | 40,3 |
| Título curto | 4,6 | 44,2 | 33,1 |
| Número-herói | 15 | 144,0 | 108,0 |
| Número médio | 7 | 67,2 | 50,4 |
| Subtítulo | 2,6 | 25,0 | 18,7 |
| Corpo grande | 2,3 | 22,1 | 16,6 |
| Corpo | 1,75 | 16,8 | 12,6 |
| Corpo pequeno | 1,35 | 13,0 | 9,7 |
| Legenda | 1 | 9,6 | 7,2 |

| Medida de grade | cqw | pt em 960 |
|---|---|---|
| Margem | 5,2 | 49,9 |
| Coluna | 6 | 57,6 |
| Calha | 1,6 | 15,4 |
| Campo | 4 | 38,4 |
| Unidade de respiro | 0,8 | 7,7 |
| Âncora do selo | 5,3 | 50,9 |
| Início do conteúdo | 10,4 | 99,8 |
| Pé | 51,05 | 490,1 |

---

## Os quatro conflitos que você vai encontrar

São reais e é melhor saber antes.

### 1. O corpo mínimo da skill

A skill da OpenAI impõe piso de corpo de texto. As descrições públicas divergem: uma fala em 12 pt de narrativa mínima, outra em 42 pt para título, 32 pt para título de slide e 17 pt para corpo. **Confira na skill instalada**, não nesta página.

Pelo piso mais exigente, numa página de 960 pt o sistema bate assim:

| Papel | pt do sistema | Piso de 17 pt | O que fazer |
|---|---|---|---|
| Corpo | 16,8 | quase passa | Arredonde para 17 |
| Corpo pequeno | 13,0 | **abaixo** | Suba para 17 ou corte texto |
| Legenda | 9,6 | **abaixo** | Suba para 14 e aceite a exceção |

O prompt acima já usa 17 pt no corpo e 14 pt na legenda. É uma **exceção declarada ao token**, não um erro. A legenda do sistema é miúda de propósito: é ela que faz o contraste com o título gigante. Subir para 14 pt achata um pouco essa tensão. Em HTML, continue usando `1cqw`.

### 2. A skill quer imagem, o sistema quer tipografia

A skill pede "dois a quatro ativos visuais por slide" e desencoraja slide de texto. **Este sistema é o contrário:** a hierarquia é o Bold gigante contra a legenda miúda, e vários slides são só a frase. O prompt já diz isso em voz alta, na seção "o que eu quero que você ignore do seu padrão". Se o agente insistir em encher o slide, repita a instrução.

### 3. Os nove padrões animados não atravessam

A Moldura, a anatomia da capa, as órbitas, o poema em máquina de escrever, o ecossistema e as tabelas que se destacam são SVG com animação por tempo. **O Google Slides não reproduz isso.** Três caminhos:

- **Estado final como imagem.** Abra o slide no HTML, espere a animação terminar, exporte em PNG ou PDF e suba a imagem. É o caminho mais fiel e o mais rápido.
- **Reconstruir como forma nativa.** Dá um resultado editável, mas perde a precisão da superelipse e o movimento.
- **Manter em HTML.** Se o padrão animado é o argumento do slide, o Google Slides é o veículo errado para aquele slide.

A skill proíbe desenhar imagem com Python. Então: exporte do HTML e suba como arquivo. Não tente gerar o SVG dentro do fluxo dela.

### 4. A pedra não é uma forma do Google Slides

A pedra é superelipse de expoente 4,3. O Google Slides só tem retângulo de quina redonda, que é outra curva. Suba `../design-system/assets/itau-pedra.svg` como imagem. **E a regra do sistema vale igual: nunca com o logotipo dentro.**

---

## Ressalvas honestas

- **O template nativo não existe ainda.** O Passo 1 é trabalho a fazer. Sem ele, a skill não tem o que seguir.
- **Os mínimos de corpo da skill estão citados de descrições públicas de terceiros**, e elas divergem entre si. Confira na skill que você instalar.
- **Figtree é fallback, não a fonte do Itaú.** Itau Display e Itau Text são proprietárias. Se a Africa tiver os arquivos, suba as duas para o Google Fonts da organização e troque no tema.
- **O HTML continua sendo o entregável de maior fidelidade.** Google Slides é o caminho quando o deck precisa ser editado por outras pessoas, dentro do Workspace, sem passar por build.

## Fontes

- [OpenAI `google-slides` agent skill](https://mcpservers.org/agent-skills/openai/google-slides)
- [A skill, em detalhe](https://skills.lc/openai/plugins/openai-plugins-plugins-google-drive-skills-google-slides-skill-md)
- [ChatGPT Work, a resposta da OpenAI ao Cowork](https://www.leadwithai.co/article/chatgpt-work-is-here-openais-answer-to-claude-cowork)
- [Cowork, da Anthropic](https://baike.baidu.com/en/item/Cowork/1416125)
- [Criar apresentações com o Claude Cowork](https://slidespeak.co/blog/how-to-create-presentations-claude-cowork)
