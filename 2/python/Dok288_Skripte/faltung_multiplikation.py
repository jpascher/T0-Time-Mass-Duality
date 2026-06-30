#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dok 288 -- Hebel 4: Faltung -> Multiplikation auf dem Generationen-Zyklus.

Eine Z3-zyklische Kopplung zwischen den drei Generationen ist eine
zirkulaere Faltung. Der Faltungssatz macht sie im DFT-Bild zu einer
PUNKTWEISEN Multiplikation:
    DFT(a (*) b) = DFT(a) . DFT(b).
Damit wird das Hintereinander zweier Z3-Kopplungen (Matrixprodukt zweier
Zirkulanten) zu drei Skalar-Produkten -- der nachrichtentechnische Kern.

numpy-only, seed 20780458.
"""
import numpy as np
np.random.seed(20780458)

w = np.exp(2j*np.pi/3)
def dft3(x):  return np.array([sum(x[j]*w**(j*k) for j in range(3)) for k in range(3)])
def circ(x):  return np.array([[x[(j-i) % 3] for j in range(3)] for i in range(3)])

# zwei beliebige Z3-Kerne (Massenkern und eine Kopplung)
a = np.array([1.0, (np.sqrt(2)/2)*np.exp(1j*2/9), (np.sqrt(2)/2)*np.exp(-1j*2/9)])
b = np.random.randn(3) + 1j*np.random.randn(3)

# zirkulaere Faltung direkt
conv = np.array([sum(a[m]*b[(n-m) % 3] for m in range(3)) for n in range(3)])

# Faltungssatz: DFT(conv) == DFT(a)*DFT(b)
lhs = dft3(conv)
rhs = dft3(a) * dft3(b)
print("Faltungssatz  max|DFT(a*b) - DFT(a).DFT(b)| =", f"{np.max(np.abs(lhs - rhs)):.2e}")

# Matrixprodukt zweier Zirkulanten == Zirkulant der Faltung
prod_mat = circ(a) @ circ(b)
prod_conv = circ(conv)
print("Zirkulant-Produkt == Zirkulant(Faltung)     :", f"{np.max(np.abs(prod_mat - prod_conv)):.2e}")
print()
print("Hebel: Hintereinanderschalten von Z3-Kopplungen = punktweise Multiplikation")
print("       der drei DFT-Koeffizienten, nicht Matrixmultiplikation.")
