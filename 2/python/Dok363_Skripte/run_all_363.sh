#!/bin/bash
# Führt alle Prüfskripte zu Dok. 363 aus
cd "$(dirname "$0")"
python3 pruef_363_hodge_t4z3.py && python3 pruef_363b_luecken.py
