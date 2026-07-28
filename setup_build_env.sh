#!/usr/bin/env bash
# =============================================================================
# FFGFT / T0 — Setup der LaTeX-Build-Umgebung (LuaLaTeX)
# Bei JEDEM neuen Chat einmal ausführen, dann kompilieren die A4-Standalone-
# Dokumente sauber (0 fehlende Glyphen, 0 csquotes-Fallback).
#
# NEU (v_fonts): Inter, JetBrains Mono und Libertinus Math liegen jetzt im
# Ordner  fonts/  und werden LOKAL installiert -> KEIN Font-Download mehr.
# Dadurch entfaellt texlive-fonts-extra (~1 GB, war nur wegen Libertinus drin)
# sowie fonts-inter und fonts-jetbrains-mono.
# Es muessen nur noch die TeX-Engine + Paketsammlungen via apt geladen werden
# (lualatex, unicode-math, tcolorbox, tikz-feynman, quantikz, siunitx, physics,
#  pgfplots, csquotes, babel ... — diese lassen sich nicht im ZIP buendeln).
# Laufzeit jetzt ca. 1-3 Min, Download deutlich kleiner.
# =============================================================================
set -e

# Verzeichnis dieses Skripts (damit fonts/ unabhaengig vom Arbeitsverzeichnis stimmt)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
FONT_SRC="$SCRIPT_DIR/fonts"
FONT_DST="/usr/local/share/fonts/ffgft"

echo ">>> [1/4] gebuendelte Schriften lokal installieren (kein Netz) ..."
if [ -d "$FONT_SRC" ]; then
  mkdir -p "$FONT_DST"
  cp -f "$FONT_SRC"/*.ttf "$FONT_SRC"/*.otf "$FONT_DST"/ 2>/dev/null || true
  fc-cache -f "$FONT_DST" >/dev/null 2>&1 || true
  echo "     -> nach $FONT_DST kopiert"
else
  echo "     ACHTUNG: Ordner fonts/ nicht gefunden ($FONT_SRC) — Schriften fehlen evtl.!"
fi

echo ">>> [2/4] apt-Pakete installieren (TeX-Engine + Pakete, OHNE Schriften) ..."

# --- Robustheit: Sandbox-Container bringen oft Fremd-Repos mit (z. B. NodeSource),
#     die hinter der Egress-Proxy-Whitelist mit 403 scheitern und "apt-get update"
#     komplett abbrechen lassen. Wir versuchen erst normal; schlaegt es fehl, werden
#     alle Nicht-Ubuntu-Quellen in sources.list.d beiseitegelegt und erneut versucht.
#     Fuer den TeX-Build ist ausschliesslich das Ubuntu-Archiv noetig.
APT_BACKUP="/tmp/apt_sources_disabled"

disable_third_party_repos() {
  mkdir -p "$APT_BACKUP"
  local moved=0
  shopt -s nullglob
  for f in /etc/apt/sources.list.d/*; do
    case "$(basename "$f")" in
      ubuntu.sources|ubuntu.list|official-package-repositories.list) : ;;   # behalten
      *) mv "$f" "$APT_BACKUP"/ && moved=1 ;;
    esac
  done
  shopt -u nullglob
  [ "$moved" = 1 ] && echo "     Hinweis: Fremd-Repos nach $APT_BACKUP verschoben (nicht erreichbar/unsigniert)."
  return 0
}

if ! apt-get update -qq 2>/dev/null; then
  echo "     apt-get update fehlgeschlagen — deaktiviere Fremd-Repos und versuche erneut ..."
  disable_third_party_repos
  apt-get update -qq
fi

DEBIAN_FRONTEND=noninteractive apt-get install -y -qq --no-install-recommends \
  texlive-luatex \
  texlive-latex-base texlive-latex-recommended texlive-latex-extra \
  texlive-fonts-recommended \
  texlive-science \
  texlive-pictures \
  texlive-lang-german texlive-lang-english texlive-lang-greek \
  texlive-xetex \
  poppler-utils
# Hinweis: texlive-fonts-recommended bleibt (Latin Modern fuer Sandbox-Praeambeln).
# Entfernt ggü. alter Version: texlive-fonts-extra, fonts-inter, fonts-jetbrains-mono.

echo ">>> [3/4] Schrift- und TeX-Datenbanken aktualisieren ..."
mktexlsr >/dev/null 2>&1 || true
fc-cache -f >/dev/null 2>&1 || true
luaotfload-tool --update >/dev/null 2>&1 || true

echo ">>> [4/4] Verifikation ..."
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
#   cd FFGFT_v1_2_3_Komplett/2/Sources/wr_standalone_A4
#   lualatex -interaction=nonstopmode 268_CMB_Peaks_T4_De.tex   # 2x
#   lualatex -interaction=nonstopmode 190_T0_Korrekturen_De.tex # 3x (TOC)
# =============================================================================
