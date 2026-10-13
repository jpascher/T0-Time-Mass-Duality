#!/bin/bash
# Dok. 393 — alle Prüfskripte
cd "$(dirname "$0")"
python3 pruef_393a_nulltest_grammatik.py > pruef_393a_ergebnis.txt 2>&1; a=$?; tail -1 pruef_393a_ergebnis.txt
python3 pruef_393b_zahlen.py | tail -1; b=$?
exit $((a + b))
