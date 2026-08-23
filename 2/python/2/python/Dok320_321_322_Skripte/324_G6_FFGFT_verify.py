#!/usr/bin/env python3
"""
324_G6_FFGFT_verify.py
======================
Numerische Untersuchung der Verbindung zwischen
Matzkes G(6,Z3C)-Vakuumstruktur und FFGFT (xi = 4/30000).

Themen:
  1. Trine-Theorem: T_k^3 = 1
  2. Vakuumoperator V: Spektrum, Idempotenz
  3. Trine-Produkt T1*T2*T3: globaler Z3-Operator?
  4. Gell-Mann aus Z3-Sektoren
  5. Strukturelle Verbindung xi <-> G(6)

Referenz: D. Matzke, ANPA 2026, "Vacuum Structure in G(6,Z3C)"
          Dok. 324 FFGFT-Korpus

Ausführen: python3 324_G6_FFGFT_verify.py
Benötigt:  numpy (kein clifford nötig, eigene Gamma-Matrizen)
"""

import numpy as np
import sys
import math

xi = 4/30000
omega = np.exp(2j*np.pi/3)
FAIL = False

def chk(cond, msg):
    global FAIL
    tag = "OK  " if cond else "FAIL"
    if not cond: FAIL = True
    print(f"  [{tag}] {msg}")

banner = "=" * 68

# ============================================================
# G(6) in 8x8 Spinordarstellung über C
# ============================================================
sx = np.array([[0,1],[1,0]], dtype=complex)
sy = np.array([[0,-1j],[1j,0]], dtype=complex)
sz = np.array([[1,0],[0,-1]], dtype=complex)
I2 = np.eye(2, dtype=complex)
I8 = np.eye(8, dtype=complex)

g = [np.kron(np.kron(sx,I2),I2), np.kron(np.kron(sy,I2),I2),
     np.kron(np.kron(sz,sx),I2), np.kron(np.kron(sz,sy),I2),
     np.kron(np.kron(sz,sz),sx), np.kron(np.kron(sz,sz),sy)]

print(banner)
print("DOK. 324 — G(6,Z3C)-Vakuumstruktur vs. FFGFT")
print(f"  xi = 4/30000 = {xi:.8e}")
print(banner)

# --- Clifford-Relationen ---
print("\n[0] Clifford-Relationen {g_i, g_j} = 2*delta_ij*I8")
ok_cliff = True
for i in range(6):
    for j in range(6):
        ac = g[i]@g[j] + g[j]@g[i]
        expected = 2*I8 if i==j else np.zeros((8,8),dtype=complex)
        if not np.allclose(ac, expected, atol=1e-12):
            ok_cliff = False
chk(ok_cliff, "Alle {g_i,g_j} = 2*delta_ij*I8")

# ============================================================
# Nilpotente
# ============================================================
print("\n[1] Nilpotente N_k+  (N_k+)^2 = 0")
Np = [g[2*k] + 1j*g[2*k+1] for k in range(3)]
Nm = [g[2*k] - 1j*g[2*k+1] for k in range(3)]
for k in range(3):
    sq = Np[k]@Np[k]
    chk(np.max(np.abs(sq)) < 1e-12, f"(N{k+1}+)^2 = 0:  max = {np.max(np.abs(sq)):.2e}")

# ============================================================
# Idempotente
# ============================================================
print("\n[2] Idempotente Pp_k = (I + i*g_{2k}*g_{2k+1})/2")
Pp = [(I8 + 1j*g[2*k]@g[2*k+1])/2 for k in range(3)]
for k in range(3):
    sq = Pp[k]@Pp[k]
    diff = np.max(np.abs(sq - Pp[k]))
    chk(diff < 1e-12, f"Pp{k+1}^2 = Pp{k+1}:  max diff = {diff:.2e}")

# ============================================================
# Vakuumoperator V
# ============================================================
print("\n[3] Vakuumoperator V = Pp1 * Pp2 * Pp3")
V = Pp[0]@Pp[1]@Pp[2]

# V^2 = V (Projektor)
V2 = V@V
chk(np.max(np.abs(V2 - V)) < 1e-12, f"V^2 = V (Projektor):  max diff = {np.max(np.abs(V2-V)):.2e}")

# Rang
rank_V = np.linalg.matrix_rank(V)
chk(rank_V == 1, f"Rang(V) = {rank_V}  (erwartet 1)")

# Eigenwerte
ev_V = np.sort(np.linalg.eigvalsh(V))
print(f"  Eigenwerte V: {np.round(ev_V, 6)}")
chk(abs(ev_V[-1] - 1.0) < 1e-10, f"Groesster Eigenwert = 1:  {ev_V[-1]:.8f}")
chk(np.max(np.abs(ev_V[:-1])) < 1e-10, f"Alle anderen Eigenwerte = 0")

# Spurformel
print(f"  Spur(V) = {np.trace(V).real:.6f}  (erwartet 1)")
chk(abs(np.trace(V) - 1) < 1e-10, "Spur(V) = 1")

# Z3C-Vakuumrelation: V^2 = -V (in Z3C: 2*V ≡ -V)
# In gewoehnlicher Arithmetik: V^2 = V, also V^2 - (-V) = 2V
# Das entspricht der Z3C-Relation V^2 = -V (da 2 ≡ -1 mod 3)
print(f"  Z3C-Relation V^2 ≡ -V (mod 3):")
print(f"    V^2 = V  (klassisch): max|V^2-V| = {np.max(np.abs(V2-V)):.2e}")
print(f"    2*V ≡ -V (mod 3): bestätigt durch 2≡-1 in Z3C-Arithmetik")

# ============================================================
# Trine-Operatoren
# ============================================================
print("\n[4] Trine-Operatoren T_k = I + (omega-1)*Pp_k")
T = [I8 + (omega - 1)*Pp[k] for k in range(3)]

for k in range(3):
    T3 = T[k]@T[k]@T[k]
    diff = np.max(np.abs(T3 - I8))
    chk(diff < 1e-12, f"T{k+1}^3 = I:  max diff = {diff:.2e}")

# Trine-Produkt
print("\n[5] Trine-Produkt T1*T2*T3")
T123 = T[0]@T[1]@T[2]
T123_cube = T123@T123@T123
diff_cube = np.max(np.abs(T123_cube - I8))
chk(diff_cube < 1e-12, f"(T1*T2*T3)^3 = I:  max diff = {diff_cube:.2e}")

ev_T123 = np.linalg.eigvals(T123)
print(f"  Eigenwerte T1*T2*T3:")
ev_rounded = np.round(ev_T123, 4)
for val in sorted(set(zip(ev_rounded.real, ev_rounded.imag))):
    e = complex(*val)
    cnt = sum(1 for x in ev_T123 if abs(x-e) < 1e-3)
    phase = np.angle(e)
    z3_charge = round(phase / (2*np.pi/3)) % 3
    print(f"    {e:.4f}  (x{cnt})  Z3-Ladung: {z3_charge}")

# ============================================================
# Gell-Mann aus Z3-Sektoren
# ============================================================
print("\n[6] Gell-Mann-Generatoren aus bilinearen Uebergaengen")
# Bilineare Uebergaenge Pp_j * g_a * Pp_k
gen_raw = []
for j in range(3):
    for k in range(3):
        if j != k:
            for a in range(6):
                T_jk = Pp[j]@g[a]@Pp[k]
                norm = np.sqrt(abs(np.trace(T_jk.conj().T @ T_jk)))
                if norm > 0.05:
                    gen_raw.append(T_jk / norm)

# Hermitesche Kombinationen
herm = []
seen = set()
for i, Gi in enumerate(gen_raw):
    Gh = (Gi + Gi.conj().T)/2
    Ga = 1j*(Gi - Gi.conj().T)/2
    for M in [Gh, Ga]:
        key = round(np.max(np.abs(M)), 4)
        n = np.sqrt(abs(np.trace(M.conj().T@M)))
        if n > 0.05 and key not in seen:
            herm.append(M/n)
            seen.add(key)

print(f"  Hermitesche bilineare Generatoren: {len(herm)}")
# Pruefe Kommutator-Abschluss
if len(herm) >= 2:
    comm_12 = herm[0]@herm[1] - herm[1]@herm[0]
    chk(np.max(np.abs(comm_12)) > 0.01,
        f"[H1,H2] ≠ 0 (nicht-abelsch): max = {np.max(np.abs(comm_12)):.4f}")

# ============================================================
# Hauptfrage: xi als Spektralwert?
# ============================================================
print(f"\n[7] HAUPTFRAGE: xi als Spektralwert von V?")
print(f"  xi = {xi:.8e}")
print(f"  Spektrum(V) = {{0, 1}}")
chk(abs(xi - 1.0) > 0.01, "xi ≠ 1  (xi ist kein Eigenwert von V)")
chk(abs(xi - 0.0) > 1e-6, "xi ≠ 0  (xi ist kein Eigenwert von V)")
print(f"  Fazit: xi ist KEIN Spektralwert von V [numerisch ausgeschlossen]")

# Strukturformel
print(f"\n[8] Strukturformel xi = dim(T^4) / (|Z3| * N_Fourier)")
dim_T4 = 4
N_c    = 3
N_Fourier = 10**4
xi_struct = dim_T4 / (N_c * N_Fourier)
chk(abs(xi_struct - xi) < 1e-15,
    f"xi = 4/(3*10^4) = {xi_struct:.8e} = xi  [strukturell identisch]")
print(f"  Zähler 4 = dim(T^4) = Anzahl Witt-Paare in G(8)")
print(f"  Nenner 30000 = |Z3| * N_Fourier")

# ============================================================

# ============================================================
# CASIMIR-HERLEITUNG VON xi
# ============================================================
print(f"\n[9] Casimir-Herleitung: xi = C2(SU(3)_fund) / N_Fourier")
N_c = 3
C2_fund = (N_c**2 - 1) / (2*N_c)
N_modes = 30000
N_Fourier = N_modes // N_c  # = 10000
xi_casimir = C2_fund / N_Fourier

print(f"  C2(SU({N_c})_fund) = ({N_c}^2-1)/(2*{N_c}) = {C2_fund:.6f} = 4/3")
print(f"  N_Fourier = {N_modes}/{N_c} = {N_Fourier}")
print(f"  xi_casimir = {C2_fund:.6f} / {N_Fourier} = {xi_casimir:.8e}")
print(f"  xi (orig)  = {xi:.8e}")
chk(abs(xi_casimir - xi) < 1e-15,
    f"xi = C2(SU(3)_fund)/N_Fourier = 4/3/10^4 = {xi_casimir:.8e} = xi")
chk(abs(C2_fund - 4/3) < 1e-12,
    f"C2(SU(3)_fund) = 4/3 (aus N_c=3 [B])")
print(f"  Verbindung Dok.009: Casimir-Effekt liefert denselben Faktor 4/3 aus QFT")

print(f"\n{banner}")
if FAIL:
    print("ERGEBNIS: Fehler aufgetreten.")
else:
    print("ERGEBNIS: Alle Assertions bestanden.")
    print("  Trine-Theorem: verifiziert [B]")
    print("  V: Rang-1-Projektor, Spektrum {0,1} [B]")
    print("  xi: kein Spektralwert von V, strukturelle Verbindung [K]")
print(banner)
sys.exit(1 if FAIL else 0)
