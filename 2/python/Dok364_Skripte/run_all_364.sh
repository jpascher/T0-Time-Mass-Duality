#!/bin/bash
# Führt alle Prüfskripte zu Dok. 364 aus.
# Optional: Pfad zur native_trace.json des OPH-Pakets als erstes Argument.
cd "$(dirname "$0")"
TRACE="${1:-native_trace.json}"
python3 spectrum_icosahedral_carrier.py "$TRACE" && \
python3 galois_z3_icosahedral_carrier.py "$TRACE" && \
python3 zphi_mod3_a5.py && \
python3 a5_vs_d4.py && \
python3 phasen_einheitswurzeln.py
