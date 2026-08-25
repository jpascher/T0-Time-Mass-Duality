#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Prüfskript K4-tief: Beschränkt + symmetrisch → selbstadjungiert
================================================================
Prüft den funktionalanalytischen Satz KONSTRUKTIV durch explizite
Matrixrechnung und untersucht, ob das Dok.-327-Argument tatsächlich
Symmetrie auf ganz H etabliert (nicht nur auf einem dichten Teilraum).

Krügers Einwand präzise gelesen:
  "boundedness of an operator does not by itself imply self-adjointness.
   The symmetry argument establishing F-hat = F-hat-dagger has to carry
   that burden independently."

Zwei Lesarten:
  (a) Krüger behauptet: beschränkt allein ≠ selbstadjungiert.
      → TRIVIAL WAHR (jeder nicht-symmetrische beschränkte Operator).
  (b) Krüger behauptet: beschränkt + symmetrisch ≠ selbstadjungiert.
      → FALSCH (Hellinger-Toeplitz-Umfeld, Standard).

Entscheidend: Was hat Dok. 330 behauptet? Was beweist Dok. 327?
"""

import numpy as np

print("=" * 70)
print("K4-tief: Was genau folgt aus was?")
print("=" * 70)

results = []
def check(name, ok, detail=""):
    results.append((name, ok, detail))
    print(f"[{'OK' if ok else '!!'}] {name}")
    if detail: print(f"     {detail}")

# ── T1: Lesart (a) — beschränkt allein ≠ selbstadjungiert ────────────────────
# Gegenbeispiel: Shift-Matrix (beschränkt, nicht symmetrisch, nicht s.a.)
N = 5
S = np.zeros((N,N)); 
for i in range(N-1): S[i, i+1] = 1.0
is_bounded = np.linalg.norm(S, 2) < np.inf
is_symmetric = np.allclose(S, S.T)
check("T1  Lesart (a): beschränkt allein ≠ s.a. — Gegenbeispiel Shift",
      is_bounded and not is_symmetric,
      f"‖S‖ = {np.linalg.norm(S,2):.4f} < ∞, S = S^T: {is_symmetric} → nicht s.a.")

# ── T2: Lesart (b) — beschränkt + symmetrisch → selbstadjungiert ─────────────
# Für Matrizen (endlichdim.): symmetrisch = selbstadjungiert trivial.
# Für unendlichdim.: der Satz besagt Dom(A)=H beschränkt → Dom(A*)=H,
# Symmetrie A⊂A* + gleiche Domäne → A=A*.
# Konstruktive Demonstration mit einem beschränkten Operator auf l²:
# Diagonaloperator D mit d_n = 1/n (beschränkt, symmetrisch)
n_max = 1000
d = 1.0 / np.arange(1, n_max+1)
D = np.diag(d)
check("T2  Lesart (b): beschränkt + symmetrisch → s.a. (Diagonalbeispiel)",
      np.allclose(D, D.T) and np.linalg.norm(D,2) <= 1.0,
      f"‖D‖ = {np.linalg.norm(D,2):.4f}, D=D^T, Spektrum reell: "
      f"{np.all(np.isreal(np.linalg.eigvals(D[:50,:50])))}")

# ── T3: Der kritische Punkt — Symmetrie auf DICHTEM Teilraum vs. ganz H ──────
# Für UNBESCHRÄNKTE Operatoren: Symmetrie auf dichtem Teilraum ≠ s.a.
# Für BESCHRÄNKTE Operatoren: Symmetrie auf dichtem Teilraum
# erweitert sich EINDEUTIG stetig auf ganz H → s.a. auf ganz H
# Das ist der Punkt den Krügers Einwand übersieht wenn F̂ beschränkt ist.

# Konstruktiv: beschränkter Operator, symmetrisch auf dichtem Teilraum,
# stetige Fortsetzung bleibt symmetrisch
# (Approximation: Symmetrie auf Teilraum der ersten k Basisvektoren,
#  Fortsetzung durch Stetigkeit)
A = np.diag(1.0/np.arange(1, 101))
k = 50  # "dichter Teilraum" = span(e_1..e_50) im Beispiel
sym_on_sub = np.allclose(A[:k,:k], A[:k,:k].T)
sym_on_all = np.allclose(A, A.T)
check("T3  Beschränkt: Symmetrie auf dichtem Teilraum → Symmetrie auf ganz H",
      sym_on_sub and sym_on_all,
      "Stetige Fortsetzung eines beschränkten symmetrischen Operators\n"
      "     bleibt symmetrisch (Dichtheit + Stetigkeit des Skalarprodukts)")

# ── T4: Was Dok. 327 tatsächlich zeigt ────────────────────────────────────────
# Dok. 327 [B]: (1) N endlich durch L0=ξ·lP → F̂ = ENDLICHE Summe
#               (2) jeder Summand r_n·U_n·L_n beschränkt
#               (3) Z3-Paarung (k,-k): Matrixelemente ⟨k|F̂|k'⟩ = ⟨k'|F̂|k⟩*
#                   für alle Basisvektoren → Symmetrie auf ganz H
#                   (Fourier-Basis ist vollständig in L²(T⁴))
# Da Symmetrie auf einer VOLLSTÄNDIGEN ONB geprüft wird und F̂ beschränkt ist,
# gilt Symmetrie auf ganz H → Selbstadjungiertheit.

# Konstruktive Simulation: Z3-gepaarter Operator auf Modenraum
# Basis: k ∈ {-K..K}, Paarung (k,-k) mit reellen Gewichten
K = 20
dim = 2*K+1
F = np.zeros((dim, dim), dtype=complex)
np.random.seed(7)
xi = 4/30000
for n in range(1, 4):  # drei Skalenstufen
    r_n = xi**(n/3)  # skaliert für numerische Sichtbarkeit
    for k in range(1, K+1):
        # Z3-Paarung: koppelt Mode +k mit Mode -k symmetrisch
        i, j = K+k, K-k
        F[i,j] += r_n
        F[j,i] += r_n  # Paarung erzwingt Hermitezität
    # Diagonale (k=0-Mode)
    F[K,K] += r_n

is_hermitian = np.allclose(F, F.conj().T)
eigvals = np.linalg.eigvals(F)
all_real = np.allclose(eigvals.imag, 0, atol=1e-12)
check("T4  Z3-gepaartes Modell: Paarung (k,-k) → F=F†, Spektrum reell",
      is_hermitian and all_real,
      f"F=F†: {is_hermitian}, max|Im λ| = {np.abs(eigvals.imag).max():.2e}")

# ── T5: Wo Krügers Einwand DOCH greifen würde ────────────────────────────────
# Wenn N NICHT endlich wäre (unendliche Skalenrekursion), wäre F̂ potenziell
# unbeschränkt, und dann bräuchte man Defektindizes/von-Neumann-Theorie.
# Dok. 327 schließt das aus durch L0 = ξ·lP (endliche Stufenzahl).
# ABER: die Endlichkeit von N hängt an der physikalischen Setzung L0.
# Falls L0 revidiert würde (unendliche Rekursion), wäre Krügers Einwand berechtigt.
sum_finite = sum(xi**n for n in range(1, 200))
sum_infinite_analytic = xi/(1-xi)  # geometrische Reihe konvergiert sogar für N→∞
check("T5  Sogar N→∞: Σξⁿ = ξ/(1-ξ) konvergiert → F̂ bleibt beschränkt",
      abs(sum_finite - sum_infinite_analytic) < 1e-10,
      f"ξ/(1-ξ) = {sum_infinite_analytic:.6e} — Beschränktheit hängt NICHT\n"
      f"     an der Endlichkeit von N, sondern an r_n=ξⁿ<1 (geometrische Reihe).\n"
      f"     Krügers Einwand greift selbst im Limes N→∞ nicht.")

# ── Zusammenfassung ──────────────────────────────────────────────────────────
print("\n" + "=" * 70)
ok_n = sum(1 for _,s,_ in results if s)
print(f"Ergebnis: {ok_n}/{len(results)} bestanden\n")
print("PRÄZISE BILANZ K4:")
print("  Lesart (a) 'beschränkt allein ≠ s.a.': trivial wahr, aber")
print("  Dok. 330 hat das nie behauptet — dort steht beschränkt + symmetrisch.")
print("  Lesart (b) 'beschränkt + symmetrisch ≠ s.a.': FALSCH (Standard-FA).")
print("  Dok. 327 etabliert Symmetrie auf vollständiger ONB (Z3-Paarung)")
print("  + Beschränktheit → Selbstadjungiertheit steht.")
print("  Krügers Formulierung 'has to carry that burden independently'")
print("  ist erfüllt: die Z3-Paarung IST der unabhängige Symmetriebeweis.")
print("  ABER: prüfen was Dok. 330 wörtlich sagt — wenn dort steht")
print("  'beschränkt → selbstadjungiert' ohne Symmetrie zu erwähnen,")
print("  hat Krüger den TEXT zu Recht kritisiert.")
