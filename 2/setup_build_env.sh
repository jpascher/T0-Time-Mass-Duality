#!/usr/bin/env bash
# =============================================================================
# FFGFT / T0 — Setup der LaTeX-Build-Umgebung (LuaLaTeX)
# Bei JEDEM neuen Chat einmal ausführen, dann kompilieren die A4-Standalone-
# Dokumente sauber (0 fehlende Glyphen, 0 csquotes-Fallback).
# Laufzeit ca. 3–6 Min, Download ca. 0,7–1 GB (texlive-fonts-extra ist groß).
# =============================================================================
set -e

echo ">>> [1/3] apt-Pakete installieren ..."
apt-get update -qq
DEBIAN_FRONTEND=noninteractive apt-get install -y -qq --no-install-recommends \
  texlive-luatex \
  texlive-latex-base texlive-latex-recommended texlive-latex-extra \
  texlive-fonts-recommended texlive-fonts-extra \
  texlive-science \
  texlive-pictures \
  texlive-lang-german texlive-lang-english texlive-lang-greek \
  texlive-xetex \
  fonts-inter fonts-jetbrains-mono \
  poppler-utils

echo ">>> [2/3] Schrift- und TeX-Datenbanken aktualisieren ..."
mktexlsr >/dev/null 2>&1 || true
luaotfload-tool --update >/dev/null 2>&1 || true
fc-cache -f >/dev/null 2>&1 || true

echo ">>> [3/3] Verifikation ..."
ok=1
command -v lualatex >/dev/null 2>&1 && echo "  OK  lualatex vorhanden" || { echo "  FEHLT lualatex"; ok=0; }
luaotfload-tool --find="Libertinus Math" 2>/dev/null | grep -q "found" \
  && echo "  OK  Libertinus Math gefunden (korrekte underbrace-Klammern)" \
  || { echo "  FEHLT Libertinus Math"; ok=0; }
kpsewhich ngerman.ldf >/dev/null 2>&1 \
  && echo "  OK  babel ngerman (deutsche Anführungszeichen „…\")" \
  || { echo "  FEHLT babel ngerman"; ok=0; }
for f in unicode-math.sty tcolorbox.sty pifont.sty siunitx.sty physics.sty \
         tikz-feynman.sty quantikz.sty pgfplots.sty longtable.sty csquotes.sty; do
  kpsewhich "$f" >/dev/null 2>&1 || { echo "  FEHLT $f"; ok=0; }
done
fc-list 2>/dev/null | grep -qi "Inter"          && echo "  OK  Inter"          || { echo "  FEHLT Inter";          ok=0; }
fc-list 2>/dev/null | grep -qi "JetBrains Mono"  && echo "  OK  JetBrains Mono"  || { echo "  FEHLT JetBrains Mono";  ok=0; }

[ "$ok" = 1 ] && echo ">>> FERTIG — Umgebung vollständig." \
              || echo ">>> ACHTUNG — es fehlen noch Teile (siehe FEHLT-Zeilen)."

# =============================================================================
# KOMPILIEREN danach (aus Sources/wr_standalone_A4/, damit ../ch und ../pri-end
# stimmen). Zweimal (Dok. 268), dreimal bei \tableofcontents (Dok. 190):
#
#   cd FFGFT_v1_1_2_Komplett/Sources/wr_standalone_A4
#   lualatex -interaction=nonstopmode 268_CMB_Peaks_T4_De.tex   # 2x
#   lualatex -interaction=nonstopmode 190_T0_Korrekturen_De.tex # 3x (TOC)
# =============================================================================
