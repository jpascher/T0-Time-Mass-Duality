#!/usr/bin/env bash
# Dok. 392 -- alle Prüfskripte (aus diesem Ordner aufrufen)
set -e
cd "$(dirname "$0")"
for s in pruef_392a_schwachfeld.py pruef_392b_mitfuehrung.py pruef_392c_gravitationswellen.py pruef_392d_kosmos.py pruef_392e_massenlesart.py pruef_392f_lichtgrenze.py pruef_392g_abstaende.py pruef_392h_desi_ap.py; do
  echo "=== $s"; python3 "$s" | tail -1
done
