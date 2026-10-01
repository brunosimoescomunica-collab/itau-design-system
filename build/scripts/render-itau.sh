#!/bin/zsh
# Monta o template, exporta o PDF 16:9 pelo Chrome headless e monta a folha de contato.
# Chrome nesta máquina escreve o PDF e não encerra: roda em background, espera o
# arquivo, mata só os processos do perfil de scratchpad (nunca o Chrome do Bruno).
set -u
WS="/Users/brunosimoes/Desktop/MY WORKSPACE (Claude)"
P16="$WS/Projetos/P16-itau-design-system"
SC="/private/tmp/claude-501/-Users-brunosimoes-Desktop-MY-WORKSPACE--Claude-/dd5e63d2-79ae-4d2c-b425-83db115a819b/scratchpad"
CH="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
TARGET="${1:-slides}"

cd "$P16" || exit 1
python3 scripts/build-itau.py || exit 1

if [ "$TARGET" = "slides" ]; then
  SRC="$WS/Clientes/Itaú/Master Slides/itau-slides-template.html"
  PDF="$SC/itau-slides.pdf"
  PROF="$SC/prof-itau-slides"
else
  SRC="$WS/Clientes/Itaú/Design System/itau-brand-book-a4.html"
  PDF="$WS/Clientes/Itaú/Design System/itau-brand-book-a4.pdf"
  PROF="$SC/prof-itau-book"
fi
rm -f "$PDF"
rm -rf "$PROF"
"$CH" --headless=new --disable-gpu --no-sandbox --hide-scrollbars \
  --user-data-dir="$PROF" --virtual-time-budget=9000 \
  --no-pdf-header-footer --print-to-pdf="$PDF" "file://$SRC" 2>/dev/null &
PID=$!
n=0
until [ -s "$PDF" ] || [ $n -ge 150 ]; do sleep 1; n=$((n+1)); done
sleep 3
kill $PID 2>/dev/null
pkill -f "user-data-dir=$PROF" 2>/dev/null
sleep 1
echo "pdf: $PDF ($(stat -f %z "$PDF" 2>/dev/null || echo 0) bytes, ${n}s)"
echo "chrome órfãos do scratchpad: $(pgrep -f 'user-data-dir=/private/tmp/claude-501' | wc -l | tr -d ' ')"
