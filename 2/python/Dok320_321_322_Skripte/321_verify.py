#!/usr/bin/env python3
"""
321_verify.py
=============
Numerische Verifikation aller Zahlenwerte in Dok. 321.
Schwerpunkt: algebraische Konsistenz der Z_3-Projektor-Konstruktion,
Gell-Mann-Matrizen und alpha_s-Formel.

Ausführen:
    python3 321_verify.py

Aktualisiert am 1.10.2026: §6 prüft nicht mehr k = (n1+n2+n3) mod 3, sondern die tau-Invarianz der Summe, Orbit-Eigenzustände psi_{n,k} in H_k und n1=n2=n3 nur in H_0 (vgl. Dok. 321, D44).
"""

import math
import numpy as np
import sys

xi = 4/30000
FAIL = False

def chk(cond, msg):
    global FAIL
    tag = "OK  " if cond else "FAIL"
    if not cond: FAIL = True
    print(f"  [{tag}] {msg}")

banner = "=" * 68

# ===========================================================
print(banner)
print("DOK. 321 — Algebraische Verifikation")
print(f"  xi = 4/30000 = {xi:.8e}")
print(banner)

# -----------------------------------------------------------
print("\n[§1: Z_3 als Zentrum von SU(3)]")
omega = np.exp(2j * math.pi / 3)
chk(abs(omega**3 - 1) < 1e-14,
    f"omega^3 = 1:  omega={omega:.6f}")
chk(abs(1 + omega + omega**2) < 1e-14,
    f"1 + omega + omega^2 = 0  (Summe der 3. Einheitswurzeln)")

# -----------------------------------------------------------
print("\n[§2: Z_3-Projektoren — Orthogonalität und Vollständigkeit]")

# Darstellung von tau als 3x3-Matrix (zyklische Permutation)
tau = np.array([[0,0,1],[1,0,0],[0,1,0]], dtype=complex)
chk(abs(np.linalg.det(tau) - 1) < 1e-14, "det(tau) = 1")
chk(np.allclose(tau @ tau @ tau, np.eye(3)),
    "tau^3 = id")

P = []
for k in range(3):
    Pk = sum(omega**(-j*k) * np.linalg.matrix_power(tau, j)
             for j in range(3)) / 3
    P.append(Pk)

print("  Projektoren P_0, P_1, P_2 konstruiert.")
for k in range(3):
    chk(np.allclose(P[k] @ P[k], P[k]),
        f"P_{k}^2 = P_{k} (Idempotenz)")
for j in range(3):
    for k in range(j+1, 3):
        chk(np.allclose(P[j] @ P[k], np.zeros((3,3))),
            f"P_{j} * P_{k} = 0 (Orthogonalität)")
chk(np.allclose(P[0] + P[1] + P[2], np.eye(3)),
    "P_0 + P_1 + P_2 = id (Vollständigkeit)")

# -----------------------------------------------------------
print("\n[§3: Gell-Mann-Matrizen und SU(3)-Algebra]")

sqrt3 = math.sqrt(3)
lam = [None]  # lam[0] unbenutzt, 1-indiziert

lam.append(np.array([[0,1,0],[1,0,0],[0,0,0]], dtype=complex))
lam.append(np.array([[0,-1j,0],[1j,0,0],[0,0,0]], dtype=complex))
lam.append(np.array([[1,0,0],[0,-1,0],[0,0,0]], dtype=complex))
lam.append(np.array([[0,0,1],[0,0,0],[1,0,0]], dtype=complex))
lam.append(np.array([[0,0,-1j],[0,0,0],[1j,0,0]], dtype=complex))
lam.append(np.array([[0,0,0],[0,0,1],[0,1,0]], dtype=complex))
lam.append(np.array([[0,0,0],[0,0,-1j],[0,1j,0]], dtype=complex))
lam.append(np.array([[1,0,0],[0,1,0],[0,0,-2]], dtype=complex) / sqrt3)

T = [None] + [lam[a]/2 for a in range(1, 9)]

print("  Normierung tr(T_a T_b) = delta_ab / 2:")
for a in range(1, 9):
    for b in range(a, 9):
        val = np.trace(T[a] @ T[b]).real
        expected = 0.5 if a == b else 0.0
        chk(abs(val - expected) < 1e-12,
            f"tr(T_{a} T_{b}) = {val:.6f}  (erwartet {expected})")

# -----------------------------------------------------------
print("\n[§4: Ausgewählte Kommutatoren]")

def comm(A, B): return A @ B - B @ A

# [T1, T2] = i*T3
C12 = comm(T[1], T[2])
chk(np.allclose(C12, 1j * T[3]),
    "[T_1, T_2] = i*T_3")

# [T1, T4] = i*(1/2)*T7  (f_147 = 1/2)
C14 = comm(T[1], T[4])
chk(np.allclose(C14, 1j * 0.5 * T[7]),
    "[T_1, T_4] = i*(1/2)*T_7  (f_147 = 1/2)")

# [T3, T8] = 0 (Cartan-Unteralgebra)
C38 = comm(T[3], T[8])
chk(np.allclose(C38, np.zeros((3,3))),
    "[T_3, T_8] = 0  (Cartan-Unteralgebra)")

# [T4, T5] = i*T3/2 + i*sqrt(3)*T8/2  (Strukturkonstante f_458)
# f_458 = sqrt(3)/2 => [T4,T5] = i*(1/2*T3 + sqrt(3)/2*T8)... prüfen
C45 = comm(T[4], T[5])
expected_C45 = 1j * (0.5 * T[3] + (sqrt3/2) * T[8])
chk(np.allclose(C45, expected_C45),
    "[T_4, T_5] = i*(T_3/2 + sqrt(3)*T_8/2)")

# Jacobi-Identität für (T1, T2, T3)
J = comm(T[1], comm(T[2], T[3])) + \
    comm(T[2], comm(T[3], T[1])) + \
    comm(T[3], comm(T[1], T[2]))
chk(np.allclose(J, np.zeros((3,3))),
    "Jacobi-Identität für (T_1, T_2, T_3)")

# -----------------------------------------------------------
print("\n[§5: alpha_s = N_c * xi^{1/(N_c+1)}]")
N_c = 3
alpha_s_calc = N_c * xi**(1/(N_c+1))
alpha_s_pdg  = 0.330   # bei m_tau, PDG
diff = (alpha_s_calc - alpha_s_pdg) / alpha_s_pdg * 100
print(f"  alpha_s = {N_c}*xi^(1/4) = {N_c}*{xi:.6e}^0.25")
print(f"          = {N_c}*{xi**0.25:.6f} = {alpha_s_calc:.5f}")
print(f"  PDG: {alpha_s_pdg}   Abw: {diff:+.2f}%")
chk(abs(alpha_s_calc - 0.322) < 0.001,
    f"alpha_s ~ 0.322 (tex-Wert)")
chk(abs(diff) < 5.0,
    f"Abweichung von PDG < 5%: {diff:+.2f}%")

# -----------------------------------------------------------
print("\n[§6: Trialität der Farbzustände]")
# Korrigierter Stand (Dok. 321, Vermerk zu Gl. tau_fourier):
# tau: (n1,n2,n3,n4) -> (n3,n1,n2,n4). Die Summe n1+n2+n3 ist
# tau-invariant und legt den Sektor NICHT fest. Eigenzustaende sind
# Orbit-Kombinationen psi_{n,k} = sum_j omega^{-jk} tau^j e_n in H_k.
omega = np.exp(2j*np.pi/3)

def tau_n(n):
    n1, n2, n3, n4 = n
    return (n3, n1, n2, n4)

def tau_psi(psi):
    """tau auf Linearkombination {n: Koeffizient} von Fourier-Moden."""
    out = {}
    for n, c in psi.items():
        m = tau_n(n)
        out[m] = out.get(m, 0) + c
    return out

def psi_orbit(n, k):
    psi, m = {}, n
    for j in range(3):
        psi[m] = psi.get(m, 0) + omega**(-j*k)
        m = tau_n(m)
    return psi

def is_eigen(psi, lam):
    t = tau_psi(psi)
    keys = set(t) | set(psi)
    return all(abs(t.get(q, 0) - lam*psi.get(q, 0)) < 1e-12 for q in keys)

def norm2(psi):
    return sum(abs(c)**2 for c in psi.values())

# (a) Summe tau-invariant -> kann omega^k nicht unterscheiden
n0 = (1, 0, 0, 0)
orbit = [n0, tau_n(n0), tau_n(tau_n(n0))]
chk(all(sum(m[:3]) == 1 for m in orbit) and tau_n(orbit[2]) == n0,
    "Orbit von (1,0,0): Summe ueberall 1, tau^3 = id (Summe tau-invariant)")

# (b) Einzelne Fourier-Mode ist nur fuer n1=n2=n3 Eigenvektor (dann H_0)
chk(not any(is_eigen({n0: 1}, omega**k) for k in range(3)),
    "Einzelmode (1,0,0) ist kein tau-Eigenvektor")
chk(is_eigen({(2, 2, 2, 1): 1}, 1),
    "Mode mit n1=n2=n3 ist Eigenvektor mit Phase 1 (in H_0)")

# (c) Orbit-Kombinationen psi_{n,k} liegen in H_k, je ein Zustand pro Sektor
for n in [(1, 0, 0, 0), (2, -1, 0, 3)]:
    for k, label in [(0, "farbneutral"), (1, "Quark"), (2, "Antiquark")]:
        p_nk = psi_orbit(n, k)
        chk(norm2(p_nk) > 1e-9 and is_eigen(p_nk, omega**k),
            f"psi_(n={n[:3]},k={k}): tau psi = omega^{k} psi ({label}, H_{k})")

# (d) Fuer n1=n2=n3 ueberlebt nur k=0 (Moden nur in H_0)
nd = (1, 1, 1, 0)
chk(norm2(psi_orbit(nd, 0)) > 1e-9 and
    all(norm2(psi_orbit(nd, k)) < 1e-12 for k in (1, 2)),
    "n1=n2=n3: psi_(n,1)=psi_(n,2)=0, nur H_0 besetzt")

# (e) Trialitaet additiv (Produktzustaende): Phasen multiplizieren sich
for ks, expected_k, label in [
    ((1, 1, 1), 0, "Baryon qqq: 1+1+1=3≡0"),
    ((1, 2), 0, "Meson q qbar: 1+2=3≡0"),
    ((1,), 1, "Einzelquark: 1"),
]:
    phase = np.prod([omega**k for k in ks])
    chk(abs(phase - omega**expected_k) < 1e-12 and sum(ks) % 3 == expected_k,
        f"{label} (Phase omega^{expected_k})")

# -----------------------------------------------------------
print(f"\n{banner}")
if FAIL:
    print("ERGEBNIS: Fehler aufgetreten — siehe oben.")
else:
    print("ERGEBNIS: Alle Assertions bestanden. Dok. 321 algebraisch konsistent.")
print(banner)
# -----------------------------------------------------------
print("\n[§7: SU(2)_L und U(1)_Y — Spurformel Weinberg-Winkel]")
import math as _math

# Fünf Orbifold-Zustände: (d_R,d_G,d_B, e^-, nu_e)
T3_vals = [0, 0, 0, -0.5, +0.5]          # Isospin T_3
Q_vals  = [-1/3, -1/3, -1/3, -1.0, 0.0]  # elektrische Ladung

trT3sq = sum(x**2 for x in T3_vals)
trQsq  = sum(x**2 for x in Q_vals)
sin2_gut = trT3sq / trQsq

print(f"  Tr[T_3^2] = {trT3sq:.6f}  (erwartet 0.5 = 1/2)")
print(f"  Tr[Q^2]   = {trQsq:.6f}  (erwartet 4/3)")
print(f"  sin^2(theta_W)|_GUT = {sin2_gut:.6f}  (erwartet 3/8 = 0.375)")

chk(abs(trT3sq - 0.5) < 1e-12, "Tr[T_3^2] = 1/2")
chk(abs(trQsq  - 4/3) < 1e-12, "Tr[Q^2] = 4/3")
chk(abs(sin2_gut - 3/8) < 1e-12, "sin^2(theta_W)|_GUT = 3/8")

# PDG-Wert und Abweichung
sin2_pdg = 0.2312
delta = sin2_gut - sin2_pdg
print(f"\n  PDG sin^2(theta_W)(M_Z) = {sin2_pdg}")
print(f"  Delta (RG-Lauf)         = {delta:.4f}  [S] offen")
chk(abs(delta - 0.1438) < 0.001,
    f"Delta = 3/8 - PDG = {delta:.4f} ~ 0.1438")

# Hyperladungs-Quantisierung: Y in (1/3)*Z
Y_vals = [2*(Q-T3) for Q,T3 in zip(Q_vals, T3_vals)]
print(f"\n  Hyperladungen Y = {[f'{y:.4f}' for y in Y_vals]}")
for i, y in enumerate(Y_vals):
    chk(abs(3*y - round(3*y)) < 1e-10,
        f"3*Y_{i} = {3*y:.4f} in Z  (Quantisierung)")

print(f"\n{banner}")
if FAIL:
    print("ERGEBNIS: Fehler aufgetreten — siehe oben.")
else:
    print("ERGEBNIS: Alle Assertions bestanden. Dok. 321 vollständig konsistent.")
print(banner)
sys.exit(1 if FAIL else 0)
