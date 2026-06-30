#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dok 288 -- Hebel 5: die xi-Rekursion ist ein IIR-Filter 1. Ordnung.

r(k+1) = r(k) (1 - xi)  hat die z-Transfer-Funktion
    H(z) = 1 / (1 - (1-xi) z^-1),  ein Pol bei z = 1 - xi.
|Pol| < 1  ->  stabil/kontrahierend (Gegenkopplung); der Pol-Abstand zum
Einheitskreis (= xi) setzt die Zeitkonstante. Die drei Regime aus Dok 285/286
sind Pol-Lagen: innen (kontrahiert), auf dem Kreis (Barkhausen), aussen (Weglauf).

numpy-only, seed 20780458.
"""
import numpy as np
np.random.seed(20780458)

xi = 4/30000
pole = 1 - xi
print(f"xi          = {xi:.6e}")
print(f"Pol z       = {pole:.8f}   |Pol| < 1 -> stabil/kontrahierend")
print(f"Zeitkonst.  k* ~ 1/xi = {1/xi:.1f} Schritte (Abstand Pol<->Einheitskreis = xi)")
print()

# Impulsantwort des Filters == direkte Rekursion (Querprobe)
N = 20000
h = pole**np.arange(N)                      # geschlossene IIR-Impulsantwort
rec = np.empty(N); rec[0] = 1.0
for k in range(1, N):
    rec[k] = rec[k-1]*pole                  # direkte Iteration
print("Impulsantwort H(z) vs direkte Rekursion  max|Delta| =", f"{np.max(np.abs(h - rec)):.2e}")
print()

# drei Regime als Pol-Lagen
for name, p in [("innen  (Gegenkopplung)", 1-xi),
                ("Kreis  (Barkhausen)   ", 1.0),
                ("aussen (Mitkopplung)  ", 1/(1-xi))]:
    tag = "kontrahiert" if p < 1 else ("Grenzfall" if abs(p-1) < 1e-12 else "laeuft weg")
    print(f"  Pol {name}: |z|={p:.6f}  -> {tag}")
print()
print("Hebel: Rekursion, Log-Periodizitaet und die drei Regime sind Pol-Rechnungen,")
print("       kein eigener Formalismus -- Standard-Filtertheorie.")
