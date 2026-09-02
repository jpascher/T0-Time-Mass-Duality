#!/usr/bin/env bash
# run_all_342.sh — führt alle Prüfskripte zu Dok. 342 aus und bricht bei Fehler ab
set -e
cd "$(dirname "$0")"
for s in pruef_342_faktorisierung_primzahlen.py pruef_342b_hoehere_harmonien.py pruef_342c_dichte_hoehere_harmonien.py; do
  echo "################ $s ################"
  python3 "$s"
done
echo "Alle Dok.-342-Prüfskripte durchgelaufen."
