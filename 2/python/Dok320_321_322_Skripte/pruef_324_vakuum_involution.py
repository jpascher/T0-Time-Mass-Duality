#!/usr/bin/env python3
"""
pruef_324_vakuum_involution.py
==============================
Numerische Klärung: Dok. 324 vs. Dougs Einwand (IPI-Mail, 26. Aug. 2026)

Frage: Ist Matzkes Vakuumoperator V eine Involution (V^2 = -V in Z3C)?
       Und was ist das Verhältnis zu V_dok = Pp1*Pp2*Pp3 aus Dok. 324?

ERGEBNIS (vorab):
  V_matzke = ap1*ap2*ap3*an1*an2*an3  = -64 * (Pn1*Pn2*Pn3)
  V_matzke^2 = -64 * V_matzke
  Z3C: -64 ≡ -1 (mod 3)  =>  V^2 ≡ -V  [Involution, Matzke korrekt]

  V_dok = Pp1*Pp2*Pp3  (Dok.-324-Definition)
  V_dok liegt auf einem ANDEREN Strahl als V_matzke.
  V_dok = Pp-Projektor,  V_matzke = -64 * Pn-Projektor.
  Pp und Pn sind komplementäre Idempotente: Pp + Pn = I,  Pp*Pn = 0.

  => Dok. 324 hat Matzkes V mit dem falschen Idempotent berechnet (Pp statt Pn).
  => Die numerischen [B]-Resultate (Rang=1, Trine-Theorem) gelten für V_dok,
     beschreiben aber nicht Matzkes Vakuumzustand.
  => Dougs Korrektur in Punkt 1 ist vollständig berechtigt.

Ausführen: python3 pruef_324_vakuum_involution.py
Benötigt:  numpy
"""

import numpy as np
import sys

FAIL = False

def chk(cond, msg):
    global FAIL
    tag = "OK  " if cond else "FAIL"
    if not cond:
        FAIL = True
    print(f"  [{tag}] {msg}")
    return cond

banner = "=" * 68

# ============================================================
# G(6) in 8x8 Spinor-Darstellung über C
# ============================================================
sx = np.array([[0,1],[1,0]], dtype=complex)
sy = np.array([[0,-1j],[1j,0]], dtype=complex)
sz = np.array([[1,0],[0,-1]], dtype=complex)
I2 = np.eye(2, dtype=complex)
I8 = np.eye(8, dtype=complex)

g = [
    np.kron(np.kron(sx, I2), I2),
    np.kron(np.kron(sy, I2), I2),
    np.kron(np.kron(sz, sx), I2),
    np.kron(np.kron(sz, sy), I2),
    np.kron(np.kron(sz, sz), sx),
    np.kron(np.kron(sz, sz), sy),
]

ap = [g[2*k] + 1j*g[2*k+1] for k in range(3)]   # Aufsteiger
an = [g[2*k] - 1j*g[2*k+1] for k in range(3)]   # Absteiger
Pp = [(I8 + 1j*g[2*k]@g[2*k+1])/2 for k in range(3)]  # Teilchen-Idempotente
Pn = [(I8 - 1j*g[2*k]@g[2*k+1])/2 for k in range(3)]  # Antiteilchen-Idempotente

print(banner)
print("PRUEF_324_VAKUUM_INVOLUTION")
print("Klaerung: Matzkes V (Involution) vs. V_dok (Projektor)")
print(banner)

# --- Clifford ---
print("\n[0] Clifford-Relationen")
ok = all(np.allclose(g[i]@g[j]+g[j]@g[i],
         2*I8 if i==j else np.zeros((8,8),dtype=complex), atol=1e-12)
         for i in range(6) for j in range(6))
chk(ok, "Alle {g_i,g_j} = 2*delta_ij*I8")

# --- Nilpotenz ---
print("\n[1] Nilpotente  (ap_k)^2 = 0")
for k in range(3):
    chk(np.max(np.abs(ap[k]@ap[k])) < 1e-12, f"(ap{k+1})^2 = 0")

# --- Pp Idempotent ---
print("\n[2] Pp_k^2 = Pp_k,  Pn_k^2 = Pn_k,  Pp_k*Pn_k = 0,  Pp_k+Pn_k = I")
for k in range(3):
    chk(np.max(np.abs(Pp[k]@Pp[k] - Pp[k])) < 1e-12, f"Pp{k+1}^2 = Pp{k+1}")
    chk(np.max(np.abs(Pn[k]@Pn[k] - Pn[k])) < 1e-12, f"Pn{k+1}^2 = Pn{k+1}")
    chk(np.max(np.abs(Pp[k]@Pn[k])) < 1e-12,          f"Pp{k+1}*Pn{k+1} = 0  (komplementär)")
    chk(np.max(np.abs(Pp[k]+Pn[k] - I8)) < 1e-12,     f"Pp{k+1}+Pn{k+1} = I")

# ============================================================
# Abschnitt A: V_matzke
# ============================================================
print("\n[A] V_matzke = ap1*ap2*ap3*an1*an2*an3  (Matzkes Definition)")
V_m = ap[0]@ap[1]@ap[2]@an[0]@an[1]@an[2]
V_pn = Pn[0]@Pn[1]@Pn[2]

chk(abs(np.trace(V_m).real + 64.0) < 1e-8,
    f"Spur(V_matzke) = {np.trace(V_m).real:.1f}  (erwartet -64)")
chk(np.linalg.matrix_rank(V_m) == 1,
    f"Rang(V_matzke) = {np.linalg.matrix_rank(V_m)}")

# V^2 = k*V
V_m2 = V_m@V_m
k_found = None
for i in range(8):
    for j in range(8):
        if abs(V_m[i,j]) > 1.0:
            k_found = (V_m2[i,j] / V_m[i,j]).real
            break
    if k_found is not None:
        break
chk(k_found is not None and np.max(np.abs(V_m2 - k_found*V_m)) < 1e-6,
    f"V_matzke^2 = {k_found:.0f}*V_matzke  (in C-Arithmetik)")

mod3 = int(-64) % 3
chk(mod3 == int(-1) % 3,
    f"-64 mod 3 = {mod3} = (-1 mod 3)  =>  V^2 ≡ -V in Z3C  [Matzke korrekt]")

# V_matzke = -64 * Pn-Produkt
chk(np.max(np.abs(V_m - (-64)*V_pn)) < 1e-8,
    f"V_matzke = -64 * (Pn1*Pn2*Pn3):  max|diff| = {np.max(np.abs(V_m-(-64)*V_pn)):.2e}")

# ============================================================
# Abschnitt B: V_dok aus Dok. 324
# ============================================================
print("\n[B] V_dok = Pp1*Pp2*Pp3  (Dok.-324-Definition)")
V_dok = Pp[0]@Pp[1]@Pp[2]

chk(np.max(np.abs(V_dok@V_dok - V_dok)) < 1e-12,
    f"V_dok^2 = V_dok  (Idempotent in C)")
chk(np.linalg.matrix_rank(V_dok) == 1,
    f"Rang(V_dok) = {np.linalg.matrix_rank(V_dok)}")
ev_dok = np.sort(np.linalg.eigvalsh(V_dok))
chk(abs(ev_dok[-1] - 1.0) < 1e-10,
    f"Groesster EW = {ev_dok[-1]:.6f}  (erwartet 1)")

# V_dok ≠ V_pn
chk(np.max(np.abs(V_dok - V_pn)) > 0.5,
    f"V_dok ≠ Pn1*Pn2*Pn3  (verschiedene Objekte): max|diff| = {np.max(np.abs(V_dok-V_pn)):.4f}")

# Eigenvektoren auf verschiedenen Strahlen
_, vec_dok = np.linalg.eigh(V_dok)
ev_m_vals, vec_m = np.linalg.eig(V_m)
idx_m = np.argmax(np.abs(ev_m_vals))
vac_m = vec_m[:, idx_m] / np.linalg.norm(vec_m[:, idx_m])
vac_d = vec_dok[:, -1]
overlap = abs(np.dot(vac_m.conj(), vac_d))
chk(overlap < 0.01,
    f"|<vac_matzke|vac_dok>| = {overlap:.6f}  (verschiedene Strahlen, Ueberlapp ~ 0)")

# ============================================================
# Abschnitt C: Trine-Theorem (bleibt korrekt)
# ============================================================
print("\n[C] Trine-Theorem T_k^3 = I  [B] aus Dok. 324 — unverändert korrekt")
omega = np.exp(2j*np.pi/3)
T = [I8 + (omega-1)*Pp[k] for k in range(3)]
for k in range(3):
    diff = np.max(np.abs(T[k]@T[k]@T[k] - I8))
    chk(diff < 1e-12, f"T{k+1}^3 = I:  max|diff| = {diff:.2e}")

T123 = T[0]@T[1]@T[2]
chk(np.max(np.abs(T123@T123@T123 - I8)) < 1e-12,
    f"(T1*T2*T3)^3 = I")

# Dougs Trine-Produkt (Z3C, nicht C)
prod = (I8+ap[0])@(I8+ap[1])@(I8+ap[2])
np3  = (-I8+prod)@(-I8+prod)@(-I8+prod)
chk(np.max(np.abs(np3)) < 1e-10,
    f"(-I+(I+ap1)(I+ap2)(I+ap3))^3 = 0  [Matzkes 3-Nilpotent, Z3C]")

# ============================================================
# Abschnitt D: Zusammenfassung
# ============================================================
print(f"\n{banner}")
print("ZUSAMMENFASSUNG UND FOLGERUNG")
print(banner)
print("""
V_matzke = ap1*ap2*ap3*an1*an2*an3 = -64 * (Pn1*Pn2*Pn3)
  Rang:        1
  Eigenwert:  -64
  V^2 = -64*V;  in Z3C: V^2 ≡ -V  (mod 3)  →  Involution  [Matzke: korrekt]

V_dok = Pp1*Pp2*Pp3             (Dok.-324-Definition)
  Rang:        1
  Eigenwert:  +1
  V^2 = V  →  Idempotent (Rang-1-Projektor in C)

Pp_k = (I + i*g_{2k}*g_{2k+1})/2  [Teilchen-Sektor]
Pn_k = (I - i*g_{2k}*g_{2k+1})/2  [Antiteilchen-Sektor]
Pp_k * Pn_k = 0,  Pp_k + Pn_k = I  (komplementär)

FEHLER in Dok. 324:
  V_dok = Pp1*Pp2*Pp3 wurde als Matzkes Vakuumoperator behandelt.
  Matzkes V ist proportional zu Pn1*Pn2*Pn3, nicht zu Pp1*Pp2*Pp3.
  Die Objekte liegen auf verschiedenen Strahlen (Ueberlapp = 0).

WAS IN DOK. 324 KORREKT BLEIBT [B]:
  - Trine-Theorem T_k^3 = I  (Pp-basiert, gilt unabhängig)
  - Rang-1-Struktur von Pp1*Pp2*Pp3  (aber für das falsche Objekt)
  - xi kein Spektralwert von V_dok

KORREKTURBEDARF IN DOK. 324:
  Abschnitt 2: V_dok durch V_matzke-Analyse ersetzen.
  Befund: V_matzke = -64*(Pn1*Pn2*Pn3), Rang 1, Involution in Z3C.
  Der Rang-1-Projektortest muss für Pn-Produkt wiederholt werden.
""")

print(banner)
if FAIL:
    print("ERGEBNIS: Fehler aufgetreten — Details oben.")
    sys.exit(1)
else:
    print("ERGEBNIS: Alle Assertions bestanden.")
    sys.exit(0)
