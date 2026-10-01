# Build

Esta pasta é o **registro de como o sistema foi feito**, e a ferramenta para refazê-lo. Você não precisa dela para usar o design system ou o template: os dois são arquivos prontos.

## O princípio

O HTML entregue é **produto de build**. Nunca edite `master-slides/itau-slides-template.html` à mão. Edite a parte em `src/`, rode o build, rode o check.

## As partes

| Arquivo | O que é |
|---|---|
| `src/01-head.html` | CSS de sistema e as `defs` do SVG |
| `src/02-body.html` | Os slides |
| `src/03-tail.html` | A interface fixa e o JavaScript (navegação, roteiro, grade) |
| `src/04-camada.css` | A camada de movimento, prefixo `fa-`, injetada no head pelo placeholder `{{CAMADA_CSS}}` |

| Script | O que faz |
|---|---|
| `scripts/build-itau.py` | Monta o template: injeta a pedra e o logo, a camada de movimento e os SVGs dos componentes, embute as fontes |
| `scripts/itau_components.py` | **A forma dos componentes.** Uma fonte só: a Moldura, a anatomia da capa, as órbitas, o poema, o ecossistema, as tabelas |
| `scripts/check-itau.py` | A bateria de invariantes. Lê o produto final e confere contra os tokens e o dossiê. **Não reusa o código que gerou os arquivos:** o build injeta, o check mede |
| `scripts/ds-patterns.py` | Gera a seção de padrões do design system |
| `scripts/book-patterns.py` | Gera a terceira página do brand book |
| `scripts/inline-fonts.py` | Troca `url("fonts/X.woff2")` por data URI base64. Idempotente |
| `scripts/strip-fonts.py` | O inverso, para voltar a editar o HTML leve |
| `scripts/render-itau.sh` · `contact-sheet.py` · `crop.py` | Provas de render em PNG e a folha de contato |

| Pasta | O que é |
|---|---|
| `fontes/itau-tokens-varejo-wayback-2025.css` | **A fonte de verdade da marca do Itaú.** Os tokens oficiais do site, snapshot do Wayback de 2025 |
| `fontes/itau-home-wayback-2025.html` | A home arquivada, de onde os tokens foram lidos |

## Rodar

```bash
/usr/bin/python3 build/scripts/build-itau.py
/usr/bin/python3 build/scripts/check-itau.py
```

**Atenção:** os scripts foram escritos para o workspace de origem e têm o caminho absoluto dele no topo (`WS = "/Users/brunosimoes/Desktop/MY WORKSPACE (Claude)"`). Num clone, eles não rodam sem você ajustar esse caminho. Isso é de propósito: eles entram aqui como **registro do método**, não como ferramenta portátil. Se você for mexer na forma, ajuste `WS` para a raiz do seu clone.

O build também exige as duas fontes licenciadas da Africa em `design-system/fonts/`. Sem elas, ele para com `FALTA fonte`. Ver [`../design-system/fonts/README.md`](../design-system/fonts/README.md).

## A ordem que não se inverte

1. Editar `src/` ou `scripts/itau_components.py`
2. Rodar o build
3. Rodar o check: **zero falhas** antes de qualquer entrega
4. Conferir **renderizado**, não no código

A forma dos componentes vive num módulo só. Mudar ali muda o template **e** os decks que importam o módulo. Rebuildar os dois.
