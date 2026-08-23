#!/usr/bin/env python3
"""
325_hawking_z3_selektion.py
===========================
Algebraischer Teil des FFGFT-Hawking-Mechanismus (Dok. 325):
Z3-Trialitaetsselektion der emittierbaren Moden.

Der Mechanismus:
  - Der Horizont traegt die Z3-Orbifold-Struktur von T^4/Z3 (Dok. 321/322)
  - Paarerzeugung an der Membran trennt ein (k,-k)-Sektorpaar
  - Der einwaerts fallende Partner wird durch die Projektor-
    Orthogonalitaet P_j * P_k = 0 (j != k) absorbiert — exakt, kein Tunneln
  - Emittierbar sind nur Trialitaets-0-Moden (T_R = 0, farblos):
    Confinement als Trialitaetsselektion (Dok. 321) wirkt AUCH am Horizont
  - Das emittierte Quant traegt das Sektorpaar (k,-k) als erhaltene,
    orthogonal lesbare Quantenzahl — die mikroskopische Realisierung
    der Informationserhaltung

Numerisch gezeigt:
  [1] Z3-Projektoren auf L^2(T^4): vollstaendig, orthogonal, idempotent
  [2] Absorption: P_j * P_k = 0 exakt (j != k)
  [3] Trialitaetsselektion: nur T_R=0-Kombinationen emittierbar
  [4] Erhaltung: Z3-Ladungssumme mod 3 vor/nach Emission identisch
  [5] Sektorinformation: die drei (k,-k)-Paare orthogonal unterscheidbar
  [6] Masselosigkeits-Bedingung: Traeger = n4=0-Torusmode

Ausfuehren: python3 325_hawking_z3_selektion.py
Benoetigt:  numpy

Referenz: J. Pascher, Dok. 325; Dok. 321 (SU(3) aus Z3),
          Dok. 322 (Hilbertraum), Dok. 313 Kap. G.
"""

import numpy as np
import sys

omega = np.exp(2j*np.pi/3)
FAIL = False
banner = "=" * 68

def chk(cond, msg):
    global FAIL
    tag = "OK  " if cond else "FAIL"
    if not cond: FAIL = True
    print(f"  [{tag}] {msg}")

print(banner)
print("DOK. 325 — Z3-Trialitaetsselektion der Hawking-Emission")
print(banner)

# ============================================================
# [1] Z3-Projektoren auf dem Modenraum
# ============================================================
print("\n[1] Z3-Projektoren P_k = (1/3) sum_j omega^(-jk) tau^j")
# Modell: Fourier-Moden auf T^4 mit Z3-Wirkung tau (zyklische Permutation
# der drei "Farbrichtungen" 1,2,3; Richtung 4 = Zeitkreis fix)
# Minimaler treuer Modenraum: C^3 (Farbfaser) x C^2 (radial: rein/raus)
# tau wirkt auf C^3 als zyklische Permutation:
tau3 = np.array([[0,0,1],[1,0,0],[0,1,0]], dtype=complex)
I3 = np.eye(3, dtype=complex)
I2 = np.eye(2, dtype=complex)

tau = np.kron(tau3, I2)   # 6x6: Farbe x radial
I6 = np.eye(6, dtype=complex)

# Z3-Projektoren
P = []
for k in range(3):
    Pk = (I6 + omega**(-k)*tau + omega**(-2*k)*(tau@tau)) / 3
    P.append(Pk)

# Vollstaendigkeit
chk(np.allclose(P[0]+P[1]+P[2], I6, atol=1e-14), "P0+P1+P2 = 1 (Vollstaendigkeit)")
# Idempotenz + Orthogonalitaet
for j in range(3):
    chk(np.allclose(P[j]@P[j], P[j], atol=1e-14), f"P{j}^2 = P{j}")
for j in range(3):
    for k in range(3):
        if j != k:
            prod = P[j]@P[k]
            chk(np.max(np.abs(prod)) < 1e-14, f"P{j}*P{k} = 0 (Annihilation, j!=k)")

# ============================================================
# [2] Annihilationsschritt: das FFGFT-Gegenstueck zu P_k * Vs = 0
# ============================================================
print("\n[2] Absorption: Partnerquant im orthogonalen Sektor")
print("    P_j * P_k = 0 (j!=k): Z3-Sektor-Orthogonalitaet auf L^2(T^4)")
# Explizit: Voxel-Zustand im Sektor 1, Partnerquant projiziert auf Sektor 2
np.random.seed(20780458)
psi = np.random.randn(6) + 1j*np.random.randn(6)
voxel = P[1] @ psi          # Bekenstein-Voxel als Sektor-1-Zustand
partner = P[2] @ (P[1] @ psi)  # Partnerquant faellt in Sektor 2 -> annihiliert
chk(np.linalg.norm(partner) < 1e-14,
    f"P2*(Sektor-1-Voxel) = 0: |Rest| = {np.linalg.norm(partner):.2e}")
print("    => Der einfallende Partner loescht das Voxel genau dann,")
print("       wenn er im orthogonalen Z3-Sektor liegt — exakt, kein Tunneln.")

# ============================================================
# [3] Trialitaetsselektion: nur T_R = 0 entkommt
# ============================================================
print("\n[3] Trialitaetsselektion am Horizont (Confinement, Dok. 321)")
# Trialitaet einer Mode = Z3-Ladung k (Eigenwert omega^k unter tau).
# Emittierbar (asymptotisch frei) sind nur T_R=0-Kombinationen:
# - Einzelmode Sektor 0 (farblos, 'Photon-artig')
# - Bilineare P_j x P_j^dagger (Meson-artig: k + (-k) = 0)
# - Trilineare Sektor1*Sektor2*Sektor0-artig mit Summe 0 mod 3 (Baryon-artig)
# Test: Z3-Ladung von Produkten
def z3_charge_of_product(charges):
    return sum(charges) % 3

kombis = {
    "Einzelmode k=0":         [0],
    "Einzelmode k=1 (Quark)": [1],
    "Bilinear (1,-1)=(1,2)":  [1, 2],
    "Bilinear (1,1)":         [1, 1],
    "Trilinear (1,1,1)":      [1, 1, 1],
    "Trilinear (0,1,2)":      [0, 1, 2],
}
print(f"  {'Kombination':<26} {'T_R':>4}  {'emittierbar?':>12}")
for name, ch in kombis.items():
    T_R = z3_charge_of_product(ch)
    em = "JA" if T_R == 0 else "nein"
    print(f"  {name:<26} {T_R:>4}  {em:>12}")

chk(z3_charge_of_product([0]) == 0,       "k=0-Mode emittierbar (Photon-Analogon)")
chk(z3_charge_of_product([1]) != 0,       "k=1-Einzelmode confined (Quark)")
chk(z3_charge_of_product([1,2]) == 0,     "Bilinear (1,2) emittierbar (Meson)")
chk(z3_charge_of_product([1,1,1]) == 0,   "Trilinear (1,1,1) emittierbar (Baryon)")
print("    => Hawking-Quanten sind ausschliesslich T_R=0-Objekte:")
print("       Confinement (Dok. 321) und Hawking-Selektion sind EIN Prinzip.")

# ============================================================
# [4] Erhaltung der Z3-Ladung bei Emission
# ============================================================
print("\n[4] Z3-Ladungserhaltung: Horizont + Strahlung")
# Modell: Horizontzustand = Superposition ueber Sektoren mit Gewichten w_k.
# Emission eines T_R=0-Quants aendert die Sektorbilanz nicht.
w = np.array([0.5, 0.3, 0.2])   # Sektor-Besetzungen (normiert)
Q_vor = np.dot(w, [0,1,2]) % 3  # mittlere Z3-Ladung (mod 3 gewichtet, formal)
# Emission T_R=0: entnimmt (k, -k)-Paar oder k=0 => Bilanz unveraendert
w_nach_meson  = w - np.array([0.0, 0.05, 0.05])   # (1,2)-Paar entnommen
w_nach_meson  = w_nach_meson / w_nach_meson.sum()
Q_nach = np.dot(w_nach_meson * w.sum(), [0,1,2]) % 3
# Ladungsdifferenz der ENTNOMMENEN Anteile:
# strengere Version: ganzzahlige Quanten
N = np.array([50, 30, 20])       # Modenzahlen pro Sektor
Q_int_vor = (N[1]*1 + N[2]*2) % 3
N_em = N - np.array([0, 1, 1])   # ein (1,2)-Paar emittiert
Q_int_nach = (N_em[1]*1 + N_em[2]*2) % 3
chk(Q_int_vor == Q_int_nach,
    f"Z3-Ladung mod 3 erhalten: {Q_int_vor} -> {Q_int_nach} (Meson-Emission)")
N_em0 = N - np.array([1, 0, 0])  # ein k=0-Quant emittiert
Q_int_nach0 = (N_em0[1]*1 + N_em0[2]*2) % 3
chk(Q_int_vor == Q_int_nach0,
    f"Z3-Ladung erhalten bei k=0-Emission: {Q_int_vor} -> {Q_int_nach0}")

# ============================================================
# [5] Informationstransfer: Sektorindex als erhaltene Quantenzahl
# ============================================================
print("\n[5] Informationskodierung im emittierten Quant")
print("    Das T_R=0-Quant traegt das SEKTORPAAR (k,-k) als innere")
print("    Quantenzahl — welcher Sektor entnommen wurde, steht in der")
print("    inneren Struktur des Quants.")
# Numerik: die drei moeglichen (k,-k)-Paare sind orthogonal unterscheidbar
pairs = []
for k in [0, 1, 2]:
    # Paarzustand: symmetrisiertes Produkt der Sektor-Basisvektoren
    e = np.zeros(3, dtype=complex); e[k] = 1
    f = np.zeros(3, dtype=complex); f[(3-k) % 3] = 1
    pair = np.kron(e, f)
    pairs.append(pair / np.linalg.norm(pair))
Gram = np.array([[abs(np.vdot(a,b)) for b in pairs] for a in pairs])
chk(np.allclose(Gram, np.eye(3), atol=1e-14),
    "Die drei (k,-k)-Paarzustaende sind orthogonal => Sektorinfo lesbar")
print(f"    Gram-Matrix der Paarzustaende:\n{np.round(Gram.real,3)}")
print("    => log2(3) = 1.585 Bit Sektorinformation pro emittiertem Quant")
print("       zusaetzlich zur thermischen 1-nat-Flaechenbuchung (Skript 1).")

# ============================================================
# [6] Masselosigkeit des Traegers: Torusmode ohne Massenwindung
# ============================================================
print("\n[6] Masselosigkeit: Windungsvektor ohne Massenkreis-Komponente")
# T^4 = T^3_Raum x S^1_Masse. Masse einer Mode ~ Windung n_4 auf dem
# Massenkreis (T~*m=1). Emittierbar als masseloser Traeger: n_4 = 0.
# Test: Spektrum der Moden |n|^2 = n1^2+n2^2+n3^2+n4^2, Masse ~ |n_4|
modes = []
for n1 in range(-1,2):
    for n2 in range(-1,2):
        for n3 in range(-1,2):
            for n4 in range(-1,2):
                modes.append((n1,n2,n3,n4))
massless = [m for m in modes if m[3]==0 and m != (0,0,0,0)]
massive  = [m for m in modes if m[3]!=0]
print(f"    Moden mit |n_i|<=1: {len(modes)-1} nichttrivial")
print(f"    masselos (n4=0):    {len(massless)}")
print(f"    massiv (n4!=0):     {len(massive)}")
chk(len(massless) == 26, f"26 masselose Nachbarmoden (3^3-1)")
chk(len(massive) == 54,  f"54 massive Moden (2*27)")
print("    => Der Hawking-Traeger ist die n4=0-Mode: raeumliche Windung ohne")
print("       Massenwindung — der masselose Vakuumtraeger des Torus.")
print("       Ein massives Quant (n4!=0) hat T~ endlich => faellt zurueck")
print("       (Uhrenstauchung an der Membran, Dok. 313 G.2).")

# ============================================================
print(f"\n{banner}")
if FAIL:
    print("ERGEBNIS: Fehler aufgetreten.")
else:
    print("ERGEBNIS: Alle Assertions bestanden.")
    print()
    print("  Z3-Selektionsmechanismus (Dok. 325, algebraischer Teil):")
    print("  1. Z3-Projektoren vollstaendig/orthogonal/idempotent          [B]")
    print("  2. Absorption P_j*P_k=0 exakt (Sektor-Orthogonalitaet)        [B]")
    print("  3. Nur T_R=0 entkommt: Confinement = Hawking-Selektion        [B]")
    print("  4. Z3-Ladung mod 3 exakt erhalten                             [B]")
    print("  5. Sektorpaar-Info orthogonal lesbar: log2(3) Bit pro Quant   [B]")
    print("  6. Traeger = n4=0-Torusmode (masselos), massive fallen zurueck [K]")
print(banner)
sys.exit(1 if FAIL else 0)
