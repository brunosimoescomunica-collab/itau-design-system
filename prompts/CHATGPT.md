# Usar este sistema no ChatGPT

Leia a primeira seção antes de copiar qualquer coisa. Ela evita meia hora de tentativa errada.

---

## O ChatGPT não baixa o repositório numa pasta

Essa é a parte que confunde todo mundo, então vai direto:

| O que você quer | Dá? | Por quê |
|---|---|---|
| ChatGPT roda `git clone` e guarda numa pasta | **Não** | O ambiente de código do ChatGPT é fechado, **sem internet**. `git clone` e `pip install` falham lá dentro |
| ChatGPT **lê** o repositório | **Sim** | Por navegação na web, ou pelo conector oficial do GitHub |
| ChatGPT **guarda** os arquivos entre conversas | **Sim** | Num **Projeto** do ChatGPT, com os arquivos subidos uma vez |
| Um agente baixa o repo numa pasta de verdade | **Sim** | **Codex**, ou ChatGPT Work no modo Computer Use. Esses têm máquina |

Traduzindo: o "guardar numa pasta" existe, mas o nome dele no ChatGPT é **Projeto**, e quem põe os arquivos lá é você, uma vez. Depois disso toda conversa dentro do Projeto já sabe o sistema.

Escolha o seu caso:

- **Você só quer usar o sistema para fazer deck** → [Caminho A](#caminho-a--projeto-do-chatgpt-recomendado). É o recomendado.
- **Você quer o ChatGPT lendo o repo ao vivo** → [Caminho B](#caminho-b--conector-do-github)
- **Você mexe em código e quer o repo no seu computador** → [Caminho C](#caminho-c--codex)

---

## Caminho A · Projeto do ChatGPT (recomendado)

Funciona em qualquer plano que tenha Projetos. Não precisa de terminal, nem de conector, nem de permissão de ninguém.

### 1. Baixe o kit

Abra este link. O navegador baixa um ZIP de 1,1 MB:

**<https://github.com/brunosimoescomunica-collab/itau-design-system/archive/refs/heads/main.zip>**

Descompacte.

### 2. Crie um Projeto no ChatGPT

Na barra da esquerda, **Projetos → novo projeto**. Chame de `Itaú × Africa`.

### 3. Suba estes seis arquivos no Projeto

Só esses seis. São o que ensina o sistema, cerca de 100 KB de texto no total:

| Arquivo | O que ensina |
|---|---|
| `prompts/AGENTS.md` | O contrato: as regras duras, em formato curto |
| `design-system/itau-brand-tokens.json` | A fonte de verdade: todo hex, corpo, raio e curva, com a origem de cada um |
| `master-slides/README.md` | A lei de diagramação e o procedimento de montar um deck |
| `docs/COMPONENTES.md` | O catálogo das 53 telas e dos nove padrões |
| `prompts/COWORK-GOOGLE-SLIDES.md` | O caminho para montar no Google Slides |
| `NOTICE.md` | O que pode e o que não pode reusar |

**Não suba** `master-slides/itau-slides-template.html`. Ele tem 392 KB e quase tudo é fonte codificada. Ele é para você **abrir no navegador** e ver, não para o ChatGPT ler.

### 4. Cole isto nas instruções do Projeto

Em **Instruções do projeto**, cole o bloco inteiro:

```
Você é o assistente de apresentações do time da Africa Creative para a conta Itaú.

OS ARQUIVOS DESTE PROJETO SÃO A SUA FONTE DE VERDADE
Antes de responder qualquer coisa sobre marca, cor, corpo de texto, grade,
layout ou componente, leia o arquivo e cite o valor que está lá. Nunca invente
um valor de marca. Se o valor não estiver nos arquivos, diga "isso não está no
sistema" em vez de preencher o buraco.

A ORDEM DE LEITURA, SEMPRE
1. itau-brand-tokens.json  — a fonte de verdade dos valores
2. master-slides/README.md — a lei de diagramação e o procedimento
3. COMPONENTES.md          — o catálogo das telas e dos padrões

A IDEIA DO SISTEMA, EM UMA LINHA
Superfície Itaú, assinatura Africa. O que se vê é do cliente: branco, laranja
#FF6200, a pedra, títulos em caixa baixa, quinas arredondadas. O que se sente é
da agência: grade de 12 colunas, filete de 1px, legenda miúda contra título
gigante, número grande em peso Light, selo no canto.
Plateia: CMO do Itaú. Quem apresenta: o VP da Africa.

AS REGRAS QUE VOCÊ NÃO NEGOCIA
- Nada inventado. Dado de campanha, mídia, mercado ou benchmark entra com fonte
  escrita. Sem fonte, escreva "FONTE PENDENTE" e me avise. Não afirme nada sobre
  prêmios, market share, número de clientes ou de agências, cores de segmento do
  Itaú ou regras do brand book oficial do Itaú: nada disso está verificado.
- A paleta é fechada: #FF6200 laranja, #FFFFFF branco, #000000 preto, #000066
  azul (só Uniclass e Personnalité, nunca ao lado do laranja em massa), #000D3C
  azul marinho, #4C4C4C cinza de texto. Nada de coral, nada de bege.
  O laranja é #FF6200, NÃO #EC7000.
- Texto antes de slide. Escreva o argumento em prosa corrida e me mostre antes
  de montar qualquer tela.
- O molde antes do layout. Escolha uma tela do catálogo e troque o conteúdo.
  Não invente layout novo.
- A régua do título, pela linha mais larga da frase: até 12 caracteres é
  Statement; até 17 é Título; acima de 17 é Título curto. No máximo três linhas.
  Um acento de cor por slide, não dois.
- A hierarquia é Bold gigante em caixa baixa contra legenda miúda em caixa alta.
  O peso intermediário não faz hierarquia. O Light só aparece no número.
- A pedra nunca tem o logotipo dentro.
- O mark da Africa só existe dentro do selo.
- Todo deck termina com dois slides, nesta ordem, sem editar uma palavra:
  penúltimo "Somos a Africa: a agência que nasce e se desafia todos os dias,
  para nunca deixar de ser a Africa Creative/™." e último "A agência das marcas
  mais desejadas, admiradas e valiosas do Brasil."
- "Africa" sem acento. É regra de marca.
- Sem travessão longo no texto de slide, em nenhuma língua. Frase curta e ponto.

COMO VOCÊ ME RESPONDE
Direto, com a lógica por trás quando o assunto é estratégia, e curto quando é
execução. Sem encher de bullet. Sem emoji.
No fim de todo entregável, me diga: o que ficou pela metade, o que é suposição
sua, e que número está sem fonte.
```

### 5. Comece a trabalhar

Primeira mensagem dentro do Projeto, para checar se ele aprendeu:

```
Leia os arquivos do projeto e me devolva, em meia página:
1. A ideia do sistema em uma frase.
2. Os seis hex da paleta e o que cada um faz.
3. A régua do título, com os três cortes.
4. As três coisas que o sistema proíbe.
5. Duas coisas que você NÃO encontrou nos arquivos e que teria que me perguntar.

Cite o arquivo de onde tirou cada resposta. Se chutar algum número, me diga que
chutou.
```

Se as respostas baterem com os arquivos, ele está pronto. O item 5 é o teste que importa: um assistente que não acha nenhum buraco está inventando.

---

## Caminho B · Conector do GitHub

Serve quando você quer o ChatGPT lendo o repositório ao vivo, sem subir arquivo.

1. No ChatGPT, conecte o **GitHub** nos conectores e autorize este repositório.
2. Depois use a pesquisa profunda (deep research) apontando para o repo.

**Limites conhecidos:** o conector é **somente leitura**, e a busca é por **nome de repositório**, não por nome de arquivo dentro dele. Ele serve para entender e perguntar, não para guardar o sistema.

Para trabalho do dia a dia, o Caminho A é melhor: os arquivos ficam parados no Projeto e ele não precisa buscar nada.

### Se o seu ChatGPT tem navegação e você quer só uma conversa rápida

Cole isto. Ele lê os arquivos direto pelas URLs públicas:

```
Leia estes seis arquivos antes de me responder qualquer coisa. Eles são o design
system de apresentações da Africa Creative para o Itaú, e são a sua única fonte
de verdade sobre marca.

https://raw.githubusercontent.com/brunosimoescomunica-collab/itau-design-system/main/prompts/AGENTS.md
https://raw.githubusercontent.com/brunosimoescomunica-collab/itau-design-system/main/design-system/itau-brand-tokens.json
https://raw.githubusercontent.com/brunosimoescomunica-collab/itau-design-system/main/master-slides/README.md
https://raw.githubusercontent.com/brunosimoescomunica-collab/itau-design-system/main/docs/COMPONENTES.md
https://raw.githubusercontent.com/brunosimoescomunica-collab/itau-design-system/main/prompts/COWORK-GOOGLE-SLIDES.md
https://raw.githubusercontent.com/brunosimoescomunica-collab/itau-design-system/main/NOTICE.md

Depois de ler, me diga em meia página: a ideia do sistema em uma frase, os seis
hex da paleta e o papel de cada um, a régua do título com os três cortes, e duas
coisas que você não encontrou nos arquivos.

Cite o arquivo de onde tirou cada resposta. Nunca invente valor de marca: se não
estiver nos arquivos, diga que não está.
```

Isso vale para **uma conversa**. Fechou a aba, ele esquece. É por isso que o Caminho A existe.

---

## Caminho C · Codex

Esse sim baixa de verdade, numa pasta sua, e pode mexer nos arquivos.

```bash
git clone https://github.com/brunosimoescomunica-collab/itau-design-system.git
cd itau-design-system
cp prompts/AGENTS.md ./AGENTS.md
```

A terceira linha é a que importa: o **Codex lê `AGENTS.md` na raiz do repositório**, automaticamente, em toda sessão. Copiando o arquivo para a raiz, o contrato entra sozinho. Não precisa colar prompt nenhum.

Depois, abra o Codex nessa pasta e peça o trabalho em linguagem normal:

```
Leia o AGENTS.md, os tokens em design-system/itau-brand-tokens.json e o catálogo
em docs/COMPONENTES.md. Depois me escreva, em prosa corrida, o roteiro de um
deck sobre <assunto>, para o CMO do Itaú. Texto antes de slide: não monte nada
até eu aprovar o roteiro.
```

Para montar no Google Slides em vez de HTML, siga [`COWORK-GOOGLE-SLIDES.md`](COWORK-GOOGLE-SLIDES.md).

---

## Para ver o deck, nada disso é necessário

O template é um arquivo HTML que abre no navegador. Depois de descompactar o ZIP:

```bash
cd itau-design-system
python3 -m http.server 8017
```

Abra <http://localhost:8017/master-slides/itau-slides-template.html>.

Teclas: setas, espaço, `j` e `k` navegam. `N` mostra o roteiro de cada tela. `B` troca claro e escuro. `G` liga a grade.

O design system em uma página abre por duplo clique: `design-system/itau-design-system.html`.

---

## Fontes

- [O ambiente de código do ChatGPT não tem internet](https://learn.chatgpt.com/docs/sandboxing)
- [Conectar o GitHub ao ChatGPT](https://help.openai.com/en/articles/11145903-connecting-github-to-chatgpt)
- [O que a integração com o GitHub faz e não faz](https://www.usecarly.com/blog/chatgpt-github-integration/)
