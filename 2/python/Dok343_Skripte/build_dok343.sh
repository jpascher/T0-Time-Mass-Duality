#!/usr/bin/env bash
set -e
REPO="$(cd "$(dirname "$0")/../../.." && pwd)"
cd "$REPO/2/Sources/wr_standalone_A4"
for L in De En; do
  lualatex -interaction=nonstopmode -halt-on-error 343_Zeta_Galois_FFGFT_$L.tex >/dev/null
  lualatex -interaction=nonstopmode -halt-on-error 343_Zeta_Galois_FFGFT_$L.tex >/dev/null
  mv 343_Zeta_Galois_FFGFT_$L.pdf "$REPO/2/pdf/"
  rm -f 343_Zeta_Galois_FFGFT_$L.{aux,log,toc,out}
done
echo "PDFs: $REPO/2/pdf/343_Zeta_Galois_FFGFT_{De,En}.pdf"
