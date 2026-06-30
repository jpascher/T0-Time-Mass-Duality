#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dok 288 -- Hebel 1: die Lepton-Massenwurzeln sind eine 3-Punkt-DFT.
Kein charakteristisches Polynom, kein 3x3-Eigensolver.

Der Massenoperator ist ein Z3-Zirkulant C mit erster Zeile
    c = (1, (r/2) e^{i theta}, (r/2) e^{-i theta}),  r = sqrt(2), theta = 2/9.
Seine Eigenwerte sind die DFT von c und gleich der Foot-Koide-Form
    sqrt(m_k) = 1 + sqrt(2) cos(theta + 2*pi*k/3).

numpy-only, seed 20780458.
"""
import numpy as np
np.random.seed(20780458)

r, th = np.sqrt(2), 2/9
w = np.exp(2j*np.pi/3)
c = np.array([1.0, (r/2)*np.exp(1j*th), (r/2)*np.exp(-1j*th)])

# Eigenwerte als 3-Punkt-DFT von c
lam_dft = np.array([sum(c[j]*w**(j*k) for j in range(3)) for k in range(3)]).real

# Gegenprobe 1: geschlossene Foot-Koide-Form
lam_closed = np.array([1 + r*np.cos(th + 2*np.pi*k/3) for k in range(3)])

# Gegenprobe 2: echter hermitescher Eigensolver am 3x3-Zirkulant
C = np.array([[c[(j-i) % 3] for j in range(3)] for i in range(3)])
lam_eig = np.linalg.eigvalsh(C)

print("Massenwurzeln sqrt(m_k) (via DFT):", np.round(np.sort(lam_dft), 6))
print("max|DFT - Foot-Koide|           :", f"{np.max(np.abs(np.sort(lam_dft)-np.sort(lam_closed))):.2e}")
print("max|DFT - eigvalsh(C)|          :", f"{np.max(np.abs(np.sort(lam_dft)-np.sort(lam_eig))):.2e}")
print()
print("Hebel: ein 3x3-Eigenwertproblem wird eine 3-Punkt-DFT eines 3-Vektors.")
