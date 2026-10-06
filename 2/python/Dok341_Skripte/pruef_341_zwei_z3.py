#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
pruef_341_zwei_z3.py -- Dok. 336, 341, 358 (Vermerke vom 6. Okt. 2026): zwei verschiedene Z3.

Prüft, dass die additive Ladung N mod 3 (Trialität) und die Eigenphase der zyklischen
Vertauschung (Sektoren H_k aus Dok. 321) verschiedene Größen sind:
  (1) Fock-Spektrum von N = B1+B2+B3 mit B_k^2 = +1: {-3,-1,+1,+3}, mod 3 {0,+1,-1}
      mit Multiplizitäten {2,3,3} (wie Dok. 341);
  (2) die zyklische Vertauschung sigma: B1 -> B2 -> B3 lässt N unverändert;
  (3) in den Eigenräumen N = +1 und N = -1 (je 3-dimensional) treten alle drei
      Eigenphasen 1, omega, omega^2 von sigma auf: N mod 3 legt k nicht fest;
  (4) Dok. 321: der Orbit der Mode (1,0,0) hat überall Windungssumme 1 und liefert
      dennoch Zustände in H_0, H_1, H_2;
  (5) beide Größen sind verträglich: sigma und N vertauschen.
numpy + Standardbibliothek.
"""
import itertools
import numpy as np

ok = n = 0
def check(name, cond, info=""):
    global ok, n
    n += 1; ok += bool(cond)
    print(f"  [{'OK ' if cond else 'FAIL'}] {name}" + (f"  ({info})" if info else ""))

w = np.exp(2j * np.pi / 3)

# Fock-Basis: Eigenwerte (b1,b2,b3) der vertauschenden B_k mit B_k^2 = +1
basis = list(itertools.product([1, -1], repeat=3))
idx = {b: i for i, b in enumerate(basis)}
N = np.diag([sum(b) for b in basis]).astype(complex)
S = np.zeros((8, 8), complex)               # sigma: B1 -> B2 -> B3 -> B1
for b in basis:
    S[idx[(b[2], b[0], b[1])], idx[b]] = 1

print("1. Spektrum von N")
ev = sorted(np.diag(N).real.astype(int))
mod = [e % 3 for e in ev]
check("N hat Eigenwerte {-3,-1,+1,+3} mit Multiplizitäten {1,3,3,1}",
      sorted(set(ev)) == [-3, -1, 1, 3] and [ev.count(x) for x in (-3, -1, 1, 3)] == [1, 3, 3, 1])
check("N mod 3: Werte {0, +1, -1} mit Multiplizitäten {2, 3, 3}",
      mod.count(0) == 2 and mod.count(1) == 3 and mod.count(2) == 3)

print("2. sigma lässt N unverändert")
check("S N S^-1 = N (die Summe B1+B2+B3 ist unter der zyklischen Vertauschung invariant)",
      np.allclose(S @ N @ np.linalg.inv(S), N))
check("S^3 = 1, sigma ist eine Z3-Wirkung", np.allclose(np.linalg.matrix_power(S, 3), np.eye(8)))

print("3. N mod 3 legt die sigma-Eigenphase nicht fest")
for val in (1, -1):
    P = [i for i, b in enumerate(basis) if sum(b) == val]
    Ssub = S[np.ix_(P, P)]
    phases = np.linalg.eigvals(Ssub)
    ks = sorted(int(round((np.angle(p) / (2*np.pi/3)))) % 3 for p in phases)
    check(f"Eigenraum N = {val:+d} (N mod 3 = {val % 3}): sigma-Eigenphasen 1, omega, omega^2 alle vorhanden",
          ks == [0, 1, 2], f"k = {ks}")
fixed = [b for b in basis if (b[2], b[0], b[1]) == b]
check("Fixpunkte von sigma: (+,+,+) und (-,-,-), also N = +3 und -3 (beide N mod 3 = 0)",
      sorted(fixed) == [(-1, -1, -1), (1, 1, 1)])

print("4. Dok. 321: Orbit der Mode (1,0,0)")
orbit = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
sums = {sum(m) for m in orbit}
# tau-Eigenzustände psi_k = sum_j w^(-jk) tau^j |m>; tau |m_j> = |m_{j+1}>
T = np.roll(np.eye(3), 1, axis=0)
ks = []
for k in range(3):
    psi = np.array([w**(-j*k) for j in range(3)])
    lam = (T @ psi) @ np.conj(psi) / (psi @ np.conj(psi))
    ks.append(int(round(np.angle(lam) / (2*np.pi/3))) % 3)
check("Windungssumme überall 1, die Orbit-Kombinationen liegen dennoch in H_0, H_1, H_2",
      sums == {1} and sorted(ks) == [0, 1, 2], f"k = {sorted(ks)}")

print("5. Verträglichkeit")
check("[S, N] = 0: ein Zustand kann Trialität und Sektor-Index zugleich tragen", np.allclose(S @ N, N @ S))

print(f"\nErgebnis: {ok}/{n}")
raise SystemExit(0 if ok == n else 1)
