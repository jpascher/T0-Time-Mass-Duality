#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
for s in pruef_343_zeta_galois.py pruef_343b_klassen_symmetrie.py pruef_343c_kopplung_zahlen.py ../Dok344_Skripte/pruef_344_primzahlmuster.py; do
  echo "################ $s ################"
  python3 "$s"
done
echo "Alle Dok.-343-Prüfskripte durchgelaufen."
