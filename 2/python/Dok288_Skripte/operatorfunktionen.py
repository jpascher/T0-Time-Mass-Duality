#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dok 288 -- Hebel 3: jede Operatorfunktion gratis im DFT-Bild.

Der hermitesche Z3-Zirkulant C wird von der unitaeren DFT-Matrix F diagonalisiert:
    C = F^dagger Lambda F,   Lambda = diag(Eigenwerte).
Damit ist JEDE Funktion f(C) = F^dagger f(Lambda) F -- d.h. man wendet f auf
drei Skalare an statt Matrixalgebra zu treiben:
    Potenz C^n  (Rekursion/Fluss), Inverse C^-1, Exponential exp(C) (Zeitentwicklung).

Querprobe numpy-only: matrix_power, inv und eine Taylor-Reihe fuer exp.
seed 20780458.
"""
import numpy as np
np.random.seed(20780458)

r, th = np.sqrt(2), 2/9
c = np.array([1.0, (r/2)*np.exp(1j*th), (r/2)*np.exp(-1j*th)])
C = np.array([[c[(j-i) % 3] for j in range(3)] for i in range(3)])
w = np.exp(2j*np.pi/3)
F = np.array([[w**(-k*j) for j in range(3)] for k in range(3)]) / np.sqrt(3)
Lam = np.diag(F @ C @ F.conj().T).real          # Eigenwerte

print("C hermitesch? max|C - C^dagger| =", f"{np.max(np.abs(C - C.conj().T)):.2e}")
print("Diagonal exakt? off-diag max   =", f"{np.max(np.abs(F@C@F.conj().T - np.diag(Lam))):.2e}")
print()

def f_via_dft(g):
    return F.conj().T @ np.diag(g(Lam)) @ F

# Potenz
C5 = f_via_dft(lambda L: L**5)
print("C^5  via DFT vs matrix_power   =", f"{np.max(np.abs(C5 - np.linalg.matrix_power(C,5))):.2e}")
# Inverse
Ci = f_via_dft(lambda L: 1/L)
print("C^-1 via DFT vs inv            =", f"{np.max(np.abs(Ci - np.linalg.inv(C))):.2e}")
# Exponential -- Querprobe als numpy-Taylor-Reihe (numpy-only)
def expm_taylor(M, N=40):
    S = np.eye(M.shape[0], dtype=complex); term = np.eye(M.shape[0], dtype=complex)
    for n in range(1, N):
        term = term @ M / n
        S = S + term
    return S
Ce = f_via_dft(np.exp)
print("exp(C) via DFT vs Taylor       =", f"{np.max(np.abs(Ce - expm_taylor(C))):.2e}")
print()
print("Hebel: f(C) = drei Skalar-Auswertungen f(Lambda_k); keine Matrixalgebra.")
