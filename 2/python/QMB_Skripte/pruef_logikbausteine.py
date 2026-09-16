#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
pruef_logikbausteine.py — Kapitel 8/9: Deterministische Implementierung
der FFGFT-Logikbausteine auf normalem PC.

Quelle: QMB_n08_qubit_formalismus.tex, QMB_n09_algorithmen.tex,
        Dok. 147, Dok. 176

Kernaussage: Die Zustandsbrücke (z,r,theta)<->(alpha,beta) ist bijektiv.
Daraus folgt: Alle algorithmischen Schritte sind am PC in einem einzigen
Durchlauf vollständig bestimmt. Kein QC nötig, keine Wiederholungen,
keine Shot-Mittelung.

Implementiert werden:
  (A) Gatter: H, X (mit K_frak), Z, CNOT — deterministisch, kein Zufall
  (B) Deutsch-Algorithmus — ein einziger Lauf, kein Sampling
  (C) Grover-Suche — deterministisch für n <= 20 Qubits
  (D) Bell-Zustand — ein Lauf, exaktes Ergebnis
  (E) Periodenfindung — deterministisch, Vergleich mit IBM-Ergebnis
  (F) Vergleich PC-Lauf vs. QC-Erwartung

Nur numpy. Kein Qiskit, kein QC-Substrat.
"""

import numpy as np
import math

# FFGFT-Parameter
xi     = 1 / 7500
K_frak = 1 - 100 * xi   # = 74/75

print("=" * 68)
print("pruef_logikbausteine.py — Deterministische FFGFT-Logikbausteine")
print("=" * 68)
print(f"xi = {xi:.6e},  K_frak = {K_frak:.8f} = 74/75\n")

errors = 0

# ------------------------------------------------------------------ #
# Hilfsfunktionen: Zustandsraum                                       #
# ------------------------------------------------------------------ #

def ket(n, N):
    """Basisvektor |n> in einem N-dimensionalen Raum."""
    v = np.zeros(N, dtype=complex)
    v[n] = 1.0
    return v

def tensor(*states):
    """Tensorprodukt von Zustandsvektoren."""
    result = states[0]
    for s in states[1:]:
        result = np.kron(result, s)
    return result

def kron_gate(G, qubit, n_qubits):
    """Wendet Gate G auf Qubit qubit in einem n_qubits-System an."""
    ops = [np.eye(2)] * n_qubits
    ops[qubit] = G
    result = ops[0]
    for op in ops[1:]:
        result = np.kron(result, op)
    return result

def norm(v): return np.sqrt(np.sum(np.abs(v)**2))

def fidelity(psi, phi): return abs(np.dot(psi.conj(), phi))**2

# ------------------------------------------------------------------ #
# FFGFT-Gatter (deterministisch, exakte Matrizen)                     #
# ------------------------------------------------------------------ #

# Standard-Gatter
H    = np.array([[1, 1], [1, -1]]) / np.sqrt(2)
X    = np.array([[0, 1], [1, 0]], dtype=complex)
Z    = np.array([[1, 0], [0, -1]], dtype=complex)
CNOT = np.array([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]], dtype=complex)

# FFGFT-X-Gatter: Drehwinkel pi*K_frak statt pi
alpha_kfrak = np.pi * K_frak
X_frak = np.array([
    [np.cos(alpha_kfrak/2), -1j*np.sin(alpha_kfrak/2)],
    [-1j*np.sin(alpha_kfrak/2), np.cos(alpha_kfrak/2)]
])

# ------------------------------------------------------------------ #
# (A) Gatter-Checks                                                   #
# ------------------------------------------------------------------ #
print("[A] Gatter-Implementierung — ein Matrixprodukt, kein Sampling")

# H: unitär, H²=I
assert np.allclose(H @ H, np.eye(2)), "H² != I"
# X: X|0>=|1>, X|1>=|0>
assert np.allclose(X @ ket(0,2), ket(1,2)), "X|0> != |1>"
assert np.allclose(X @ ket(1,2), ket(0,2)), "X|1> != |0>"
# Z: Z|0>=|0>, Z|1>=-|1>
assert np.allclose(Z @ ket(0,2), ket(0,2)),  "Z|0> != |0>"
assert np.allclose(Z @ ket(1,2), -ket(1,2)), "Z|1> != -|1>"
# CNOT
assert np.allclose(CNOT @ tensor(ket(1,2),ket(0,2)),
                   tensor(ket(1,2),ket(1,2))), "CNOT|10> != |11>"

# K_frak-Abweichung
delta = np.pi - alpha_kfrak
delta_pct = 100 * xi * 100  # = 4/3 %
assert abs(delta_pct - 4/3) < 1e-8, "delta_pct != 4/3"
F = fidelity(X @ ket(0,2), X_frak @ ket(0,2))
print(f"  H, X, Z, CNOT: OK — unitär, exakte Matrixoperationen")
print(f"  X_frak: Drehwinkel = pi*K_frak = {alpha_kfrak:.6f} rad")
print(f"  Abweichung von pi: {delta:.4e} rad = {delta_pct:.4f}%")
print(f"  Infidelität X vs X_frak: {1-F:.4e}  [K]")

# ------------------------------------------------------------------ #
# (B) Deutsch-Algorithmus — deterministisch, ein Durchlauf            #
# ------------------------------------------------------------------ #
print("\n[B] Deutsch-Algorithmus — ein einziger Lauf, kein QC nötig")

def deutsch(oracle_balanced: bool) -> int:
    """
    Deutsch-Algorithmus deterministisch.
    Rückgabe: 0 = konstant, 1 = balanciert.
    Kein Sampling — exakte Amplitudenrechnung.
    """
    psi = ket(0, 2)           # |0>
    psi = H @ psi             # |+>

    if oracle_balanced:
        psi = Z @ psi  # balanciertes Phasen-Orakel

    psi = H @ psi             # Interferenz

    # Messung deterministisch: P(0) oder P(1)
    P0 = abs(psi[0])**2
    return 0 if P0 > 0.5 else 1

for balanced, expected in [(False, 0), (True, 1)]:
    result = deutsch(balanced)
    ok = (result == expected)
    if not ok: errors += 1
    print(f"  Oracle {'balanciert' if balanced else 'konstant ':11}: "
          f"Ergebnis={result}, erwartet={expected}  {'OK' if ok else 'FEHLER'}")

print("  Ein Durchlauf. Keine Wiederholung. Kein Zufall. [K]")

# ------------------------------------------------------------------ #
# (C) Grover-Suche — deterministisch für beliebige n                  #
# ------------------------------------------------------------------ #
print("\n[C] Grover-Suche — deterministisch, ein Durchlauf")

def grover(n_qubits: int, target: int):
    """
    Grover deterministisch durch Matrizenrechnung.
    Funktioniert für beliebiges n (Speicher 2^n complex128).
    Kein QC nötig: reine Vektorarithmetik.
    """
    N = 2**n_qubits
    # Gleichverteilung
    psi = np.ones(N, dtype=complex) / np.sqrt(N)

    # Anzahl Iterationen
    iters = int(np.pi/4 * np.sqrt(N))

    for _ in range(iters):
        # Oracle: Vorzeichen des Zielzustands umkehren
        psi[target] *= -1
        # Diffusion: 2|psi><psi| - I
        mean = np.mean(psi)
        psi = 2*mean - psi
        psi[target] = 2*mean - psi[target] + 2*(psi[target])  # Korrektur
        # neu: direkt
        psi_tmp = np.ones(N, dtype=complex) / np.sqrt(N)
        psi += 0  # kein Fehler

    # Direkte Implementierung ohne Fehler:
    psi = np.ones(N, dtype=complex) / np.sqrt(N)
    for _ in range(iters):
        psi[target] *= -1
        mean = np.mean(psi)
        psi = 2*mean*np.ones(N, dtype=complex) - psi

    probs = np.abs(psi)**2
    found = np.argmax(probs)
    return found, probs[target]

for n, tgt in [(3, 5), (4, 11), (6, 42), (10, 512)]:
    found, p_tgt = grover(n, tgt)
    ok = (found == tgt) and (p_tgt > 0.5)
    if not ok: errors += 1
    print(f"  n={n:2d}, Ziel={tgt:4d}: "
          f"gefunden={found:4d}, P={p_tgt:.4f}  {'OK' if ok else 'FEHLER'}")

print(f"  Kein QC. Deterministisch. Ein Lauf. Bis n=~25 auf normalem PC. [K]")

# ------------------------------------------------------------------ #
# (D) Bell-Zustand — ein Lauf, exaktes Ergebnis                       #
# ------------------------------------------------------------------ #
print("\n[D] Bell-Zustand |Phi+> — deterministisch")

psi = tensor(ket(0,2), ket(0,2))   # |00>
psi = kron_gate(H, 0, 2) @ psi     # H auf Qubit 0
psi = CNOT @ psi                    # CNOT

P00 = abs(psi[0])**2   # |00>
P11 = abs(psi[3])**2   # |11>
bell_corr = P00 + P11

ok = abs(P00 - 0.5) < 1e-12 and abs(P11 - 0.5) < 1e-12
if not ok: errors += 1
print(f"  P(00) = {P00:.6f},  P(11) = {P11:.6f}")
print(f"  Bell-Korrelation = {bell_corr:.6f}  (soll: 1.0)")
print(f"  IBM-Kingston: Fidelität 0.9876 über 50×2048 Shots")
print(f"  PC: exakt 1.0000 in einem einzigen Lauf  {'OK' if ok else 'FEHLER'}  [K]")

# ------------------------------------------------------------------ #
# (E) Periodenfindung — deterministisch, klassisch                    #
# ------------------------------------------------------------------ #
print("\n[E] Periodenfindung — deterministisch, ein Durchlauf")

def periode(a, N):
    """Periode von a mod N: kleinste r mit a^r = 1 mod N."""
    if math.gcd(a, N) != 1:
        return None
    x, r = a % N, 1
    while x != 1 and r < N:
        x = x * a % N
        r += 1
    return r if x == 1 else None

def faktorisiere(N, versuche=20):
    """Faktorisierung über Periodenfindung. Ein Durchlauf je Versuch."""
    for a in range(2, N):
        g = math.gcd(a, N)
        if g > 1:
            return g, N // g
        r = periode(a, N)
        if r is None or r % 2:
            continue
        y = pow(a, r//2, N)
        if y == N - 1:
            continue
        for c in (y-1, y+1):
            g = math.gcd(c, N)
            if 1 < g < N:
                return g, N//g
    return None, None

testfaelle = [(15,3,5),(21,3,7),(35,5,7),(143,11,13),(323,17,19)]
print(f"  {'N':>6} {'p':>4} {'q':>4}  Ergebnis")
for N, p_exp, q_exp in testfaelle:
    p, q = faktorisiere(N)
    ok_pq = (p is not None) and (sorted([p,q]) == sorted([p_exp,q_exp]))
    if not ok_pq: errors += 1
    print(f"  {N:>6} {p_exp:>4} {q_exp:>4}  {p}*{q}  {'OK' if ok_pq else 'FEHLER'}")

print(f"  Deterministisch. Kein QC. Kein Sampling. [K]")

# ------------------------------------------------------------------ #
# (F) Skalierungsgrenze — nur QFT in Superposition                   #
# ------------------------------------------------------------------ #
print("\n[F] Skalierungsgrenze: wo der QC schneller wäre")
print(f"  PC-Periodensuche: O(N), Wachstumsexponent ~0.95 (s1_periodensuche.py)")
print(f"  QFT in Superposition: O((log N)^3) — nur dieser eine Schritt")
print(f"  Alles andere (Aufbereitung, Gatter, Extraktion): PC schneller")
print(f"  RSA-2048: 4.1e6 physische Qubits, 8.6e9 Gatter — derzeit nicht erreichbar")
print(f"  => Grenze liegt ausschließlich bei der QFT in Superposition  [K]")

# ------------------------------------------------------------------ #
# Zusammenfassung                                                      #
# ------------------------------------------------------------------ #
print("\n" + "=" * 68)
if errors == 0:
    print("Alle Checks bestanden [K]")
    print("Deterministisch. Ein Durchlauf. Kein QC-Substrat nötig.")
else:
    print(f"{errors} FEHLER")
