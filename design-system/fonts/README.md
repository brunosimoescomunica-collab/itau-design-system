# Fontes

## O que está aqui

| Arquivo | Família | Peso | Licença |
|---|---|---|---|
| `Figtree-VF-latin.woff2` | Figtree (variável) | 300 a 700 | SIL OFL 1.1. Ver `Figtree-OFL.txt` |
| `Figtree-VF-latin-ext.woff2` | Figtree (variável) | 300 a 700 | SIL OFL 1.1. Ver `Figtree-OFL.txt` |

Figtree é o **fallback** do sistema, não a fonte do Itaú. O font stack declara `Itau Display` e `Itau Text` primeiro. Na máquina que tiver as proprietárias instaladas, o deck renderiza com elas. Onde não tiver, cai na Figtree, escolhida por ser sans humanista de caixa baixa amigável, com Light e Bold, e livre para embutir.

Origem: <https://github.com/google/fonts/tree/main/ofl/figtree>

## O que NÃO está aqui, de propósito

Duas fontes licenciadas da Africa foram removidas deste repositório público. Publicá-las seria redistribuir fonte paga.

| Arquivo que falta | Família | Onde ela aparece | Fornecedor |
|---|---|---|---|
| `MiletusGrotesk-Medium.woff2` | Miletus Grotesk | só o anel do selo e a marca d'água do pé | licença da Africa |
| `PPPangaia-Light.woff2` | PP Pangaia | só o fechamento e o slogan | Pangram Pangram |

**Efeito prático:** o sistema inteiro renderiza certo. Só o selo e o slogan de fecho caem no fallback.

## Como restaurar, para quem é da Africa e tem licença

Copie os dois `.woff2` para **duas** pastas, a partir da raiz do repositório:

```bash
cp MiletusGrotesk-Medium.woff2 PPPangaia-Light.woff2 design-system/fonts/
cp MiletusGrotesk-Medium.woff2 PPPangaia-Light.woff2 master-slides/fonts/
```

Depois disso tudo renderiza completo, sem mais nenhum passo.

Para voltar a embutir as fontes dentro do HTML do template, que é o que faz um deck sobreviver a viajar por e-mail:

```bash
/usr/bin/python3 build/scripts/inline-fonts.py master-slides/itau-slides-template.html master-slides/fonts
```

Não comite os dois arquivos de volta enquanto este repositório for público.
