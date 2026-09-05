#!/bin/bash
# Alle Prüfskripte Dok. 351 ausführen
cd "$(dirname "$0")"
echo "=== Dok. 351 Prüfskripte ==="
python3 pruef_351_rationale_vergleiche.py
echo ""
echo "=== Fertig ==="
