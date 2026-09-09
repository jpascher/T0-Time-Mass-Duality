#!/usr/bin/env bash
# Buildskript FFGFT Narrativ-Buch (De + En)
# Aufruf: bash build_narrativ.sh
set -e
cd "$(dirname "$0")"
for lang in De En; do
    echo ">>> Kompiliere FFGFT_Narrativ_${lang}.tex ..."
    lualatex -interaction=nonstopmode FFGFT_Narrativ_${lang}.tex
    lualatex -interaction=nonstopmode FFGFT_Narrativ_${lang}.tex
    cp FFGFT_Narrativ_${lang}.pdf ../../pdf/
    cp FFGFT_Narrativ_${lang}.pdf pdf/
    echo "    -> ../../pdf/FFGFT_Narrativ_${lang}.pdf"
done
echo ">>> Fertig."
