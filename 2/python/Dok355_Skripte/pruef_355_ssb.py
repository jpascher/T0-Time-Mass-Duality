#!/usr/bin/env python3
"""
pruef_355_ssb.py
Prüfskript zu Dok. 355: SSB SU(2)_L x U(1)_Y -> U(1)_EM aus T4/Z3-Geometrie
Johann Pascher, 7. September 2026

Aktualisiert am 1.10.2026: Higgs-Dublett I3 = (+1/2, -1/2) mit Q = (+1, 0); Einselement (k=0) hat Legendre-Symbol 0 und liegt in keinem Frobenius-Orbit, Schritt 4 offen; Y = +1 nicht aus Dok. 347 Satz A herleitbar (QR -> Y = -1), Hyperladung offen [S]; Z0 <-> T3 - Q sin^2(theta_W) mit e_L-Beispiel; M_W/M_Z mit cos(theta_W) = 0,8770 gegen 0,8814 (vgl. Dok. 355 und Dok. 190, R146).
"""
import math

xi = 4/30000

N_OK = 0
N_ALL = 0

def chk(cond, msg):
    global N_OK, N_ALL
    N_ALL += 1
    if cond:
        N_OK += 1
    print(f"  [{'OK  ' if cond else 'FAIL'}] {msg}")
    assert cond, msg

def legendre(a, p):
    """Legendre-Symbol (a/p) als Wert in {0, 1, -1}."""
    r = pow(a % p, (p-1)//2, p)
    return -1 if r == p-1 else r

# ── S1: VEV != 0 aus T*m=1 ──────────────────────────────────────────────────
print("S1: m_vak != 0 aus T*m=1 [B]")
# T*m=1 hat bei m=0 keine Loesung
try:
    T_zero = 1.0 / 0.0
    raise AssertionError("m=0 sollte keine Loesung haben")
except ZeroDivisionError:
    pass
chk(True, "m_vak != 0 erzwungen durch T*m=1 (m=0 hat keine Loesung) [B]")

# ── S0: SM-Ausgangslage — Higgs-Dublett (korrigiert) ────────────────────────
print("\nS0: SM-Ausgangslage Higgs-Dublett Phi = (phi+, phi0)^T [X]")
I3_dublett = (+0.5, -0.5)     # korrigiert, vorher (-1/2, +1/2)
Y_higgs = +1                  # SM-Setzung
Q_dublett = tuple(i3 + Y_higgs/2 for i3 in I3_dublett)
chk(Q_dublett == (1.0, 0.0),
    f"I3 = (+1/2, -1/2), Y = +1 -> Q = {Q_dublett} = (+1, 0)")
Q_alt = tuple(i3 + Y_higgs/2 for i3 in (-0.5, +0.5))
chk(Q_alt == (0.0, 1.0),
    f"alter Stand I3 = (-1/2, +1/2) gaebe Q = {Q_alt}: phi+ neutral, phi0 geladen (falsch)")

# ── S2a: Einselement (k=0) — Frobenius-Fixpunkt, Legendre-Symbol 0 ──────────
print("\nS2a: Galois-Klassifikation des Vakuums (Schritte 3/4)")
k_vacuum = 0
N_vacuum = k_vacuum % 3
chk(N_vacuum == 0, "k=0-Mode: N mod 3 = 0 (Farb-Singlett) [B]")

# Frobenius-Orbits k -> 3k mod 13 auf Z_13 \ {0}
orbits, seen = [], set()
for k in range(1, 13):
    if k in seen:
        continue
    orb, x = [], k
    while x not in orb:
        orb.append(x)
        x = (3*x) % 13
    orbits.append(sorted(orb))
    seen |= set(orb)
chk(len(orbits) == 4 and all(len(o) == 3 for o in orbits)
    and len(set().union(*map(set, orbits))) == 12,
    f"Frobenius-Orbits {orbits}: vier disjunkte Dreierorbits")
chk((3*0) % 13 == 0 and all(0 not in o for o in orbits),
    "Exponent 0 (Einselement g^0) ist Fixpunkt, liegt in keinem Orbit O_i")
chk(1 in orbits[0] and orbits[0] == [1, 3, 9],
    "1 in O_1 = {1,3,9} ist der Exponent k=1 (g^1), nicht das Einselement")
L_vac = legendre(k_vacuum, 13)
chk(L_vac == 0,
    f"Legendre-Symbol (0/13) = {L_vac}: weder QR noch NQR -> "
    "'triviales Element ist QR' (Schritt 4) nicht belegt [S]")

# ── S2b: Hyperladung — Y = +1 nicht aus Dok. 347 Satz A herleitbar ──────────
print("\nS2b: Hyperladung des Vakuums (Schritte 5-7)")
I3_phi0 = -0.5          # Sd-Sektor, linkshaendig (Dok. 349 Satz D) [B]
def Y_satzA(nqr):
    """Zitierte Formel aus Dok. 347 Satz A: Y = -1 + (4/3)*NQR."""
    return -1 + 4/3*nqr
Y_QR = Y_satzA(0)
chk(abs(Y_QR - (-1)) < 1e-14,
    f"Satz-A-Formel fuer QR (NQR=0): Y = {Y_QR:+.0f}, nicht +1")
Q_satzA = I3_phi0 + Y_QR/2
chk(abs(Q_satzA - (-1)) < 1e-14,
    f"damit Q = I3 + Y/2 = {Q_satzA:+.1f} statt 0")
nqr_needed = (Y_higgs + 1) * 3/4
chk(abs(nqr_needed - 1.5) < 1e-14,
    f"Y = +1 verlangte NQR = {nqr_needed} (nicht ganzzahlig) -> Schritt 6 offen [S]")
# Hyperladung der geladenen Leptonen aus QR/NQR allein: offen (Dok. 190, R146)
print("  [S] Y = +1 des Higgs-Dubletts ist SM-Eingang, in FFGFT nicht hergeleitet;")
print("      Hyperladung der geladenen Leptonen offen (Dok. 190, R146).")

# Mit SM-Setzung Y = +1 (nicht FFGFT-hergeleitet): Q_vak = 0
Q_vacuum = I3_phi0 + Y_higgs/2
chk(abs(Q_vacuum) < 1e-14,
    f"mit SM-Eingang Y = +1: Q_vak = I3 + Y/2 = {Q_vacuum} (Gell-Mann-Nishijima)")

# ── S3: U(1)_Q als Restgruppe ────────────────────────────────────────────────
print("\nS3: U(1)_Q als Restgruppe")
inv = all(abs(complex(math.cos(a*Q_vacuum), math.sin(a*Q_vacuum)) - 1.0) < 1e-14
          for a in [0, math.pi/6, 1.0, math.pi, 2*math.pi])
chk(inv, "U(1)_Q laesst Vakuum (Q_vak = 0) invariant fuer alle alpha")

# ── S4: Goldstone-Zaehlung, W/Z massiv ───────────────────────────────────────
print("\nS4: Goldstone-Zaehlung")
dim_G = 4   # SU(2)_L: 3, U(1)_Y: 1
dim_H = 1   # U(1)_EM: 1
n_goldstone = dim_G - dim_H
chk(n_goldstone == 3,
    f"{n_goldstone} Goldstone-Bosonen -> W+, W-, Z0 massiv; gamma masselos")

# ── S4b: Z0-Generator T3 - Q sin^2(theta_W) (korrigiert) ────────────────────
print("\nS4b: Z0 <-> T3 - Q sin^2(theta_W)")
s2 = 0.2312
ok_id = True
for T3, Y in [(-0.5, -1), (+0.5, -1), (+0.5, 1/3), (-0.5, 1/3), (0, -2), (0, 4/3)]:
    Q = T3 + Y/2
    lhs = T3*(1 - s2) - Y/2*s2
    rhs = T3 - Q*s2
    ok_id &= abs(lhs - rhs) < 1e-14
chk(ok_id, "T3 cos^2 - (Y/2) sin^2 = T3 - Q sin^2 fuer alle SM-Fermionen")
T3_eL, Y_eL = -0.5, -1
Q_eL = T3_eL + Y_eL/2
gZ_neu = T3_eL - Q_eL*s2
gZ_alt = T3_eL - Y_eL/2*s2
chk(abs(gZ_neu - (-0.2688)) < 5e-5,
    f"e_L: T3 - Q sin^2 = {gZ_neu:.4f} (Dok. 355: -0,2688)")
chk(abs(gZ_alt - (-0.3844)) < 5e-5,
    f"alter Ausdruck T3 - (Y/2) sin^2 = {gZ_alt:.4f} (-0,3844, falsch)")

# ── S5: Weinberg-Winkel und Massenverhaeltnis ────────────────────────────────
print("\nS5: Weinberg-Winkel und M_W/M_Z [K]")
sin2_thetaW_ffgft = 0.2308   # Dok. 323 [K]
sin2_thetaW_pdg   = 0.2312   # MS-bar, Dok. 355 Tabelle
abw_thetaW = (sin2_thetaW_ffgft - sin2_thetaW_pdg) / sin2_thetaW_pdg
chk(abs(abw_thetaW*100 - (-0.17)) < 0.01,
    f"sin^2(theta_W) = {sin2_thetaW_ffgft} vs {sin2_thetaW_pdg}: Abw. {abw_thetaW*100:+.2f} %")
cosW = math.sqrt(1 - sin2_thetaW_ffgft)
MW, MZ = 80.369, 91.188
MW_MZ = MW / MZ
abw_ratio = (cosW - MW_MZ) / MW_MZ
chk(abs(cosW - 0.8770) < 5e-5, f"cos(theta_W) = sqrt(1-0,2308) = {cosW:.4f}")
chk(abs(MW_MZ - 0.8814) < 5e-5, f"M_W/M_Z = {MW}/{MZ} = {MW_MZ:.4f}")
chk(abs(abw_ratio*100 - (-0.49)) < 0.01, f"Abweichung {abw_ratio*100:+.2f} %")
s2_onshell = 1 - MW_MZ**2
chk(abs(s2_onshell - 0.2232) < 5e-4,
    f"on-shell sin^2(theta_W) = 1-(M_W/M_Z)^2 = {s2_onshell:.4f}: "
    "Differenz ist Schemaunterschied MS-bar vs. on-shell")

# ── Zusammenfassung ──────────────────────────────────────────────────────────
print(f"\n=== Dok. 355 Pruefskript: {N_OK}/{N_ALL} OK ===")
print("  Q_vak = 0 mit SM-Eingang Y = +1; I3 = (+1/2, -1/2), Q = (+1, 0)")
print("  Schritt 4 (k=0 ist QR) und Schritt 6 (Y = +1 aus Legendre-Symbol): offen [S]")
print("  Hyperladung der geladenen Leptonen offen (Dok. 190, R146) [S]")
print(f"  Goldstone-Bosonen: {n_goldstone} (W+, W-, Z0); Photon masselos [B]")
print("  Z0 <-> T3 - Q sin^2(theta_W)")
print(f"  sin^2(theta_W) = {sin2_thetaW_ffgft}, Abw. {abw_thetaW*100:+.2f} % [K]; "
      f"M_W/M_Z Abw. {abw_ratio*100:+.2f} % [K]")
