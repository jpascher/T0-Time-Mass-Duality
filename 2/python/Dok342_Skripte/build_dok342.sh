#!/usr/bin/env bash
# build_dok342.sh — kompiliert Dok. 342 De+En mit lualatex und legt PDFs in 2/pdf ab
set -e
REPO="$(cd "$(dirname "$0")/../../.." && pwd)"
cd "$REPO/2/Sources/wr_standalone_A4"
for L in De En; do
  lualatex -interaction=nonstopmode -halt-on-error 342_Faktorisierung_Harmonik_$L.tex >/dev/null
  lualatex -interaction=nonstopmode -halt-on-error 342_Faktorisierung_Harmonik_$L.tex >/dev/null
  mv 342_Faktorisierung_Harmonik_$L.pdf "$REPO/2/pdf/"
  rm -f 342_Faktorisierung_Harmonik_$L.{aux,log,toc,out}
done
echo "PDFs: $REPO/2/pdf/342_Faktorisierung_Harmonik_{De,En}.pdf"
