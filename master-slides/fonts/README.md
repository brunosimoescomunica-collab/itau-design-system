# Pasta de fontes do template

O template `itau-slides-template.html` carrega a **Figtree embutida em base64**, então não depende desta pasta para o corpo do deck. Ele busca aqui dentro, por caminho relativo, duas fontes licenciadas da Africa:

- `MiletusGrotesk-Medium.woff2` para o anel do selo e a marca d'água do pé
- `PPPangaia-Light.woff2` para o fechamento e o slogan

As duas não vêm no repositório público, porque são fontes pagas. Sem elas o template abre e funciona. Só esses dois elementos caem no fallback.

Quem é da Africa e tem licença: copie os dois arquivos para cá. Detalhes em [`../../design-system/fonts/README.md`](../../design-system/fonts/README.md).
