#!/usr/bin/env python3
"""
pruef_340b_spirale_breitband.py
Ergänzung zu Dok. 340 (31. Aug. 2026)

Prüft:
  1. Nichtschließung der Winkelstruktur Z_13 x Z_24 (Frobenius-Orbits x D4-Kissing)
  2. Phasenspirale phi ~ 1/E über das DUNE-Spektrum (nicht periodisch)
  3. Breitband-Verschwindung (clamped Normalverteilung) vs. monochromatisch
  4. K_frak = 1-100*xi darf NICHT auf das Verhältnis dm2/m_nu^2 angewendet werden

Alle Werte aus xi = 1/7500 und der GF(27)*-Struktur; keine freien Parameter.
"""
import numpy as np
from math import gcd

# ---------------------------------------------------------------- Basis
xi     = 1/7500
m_e    = 510998.95            # eV
m_nu   = xi**2/2*m_e          # eV
dm2    = 120*m_nu**2          # eV^2  (Dok. 340)
hbar_c = 197.3e-9             # eV*m
L_DUNE = 1285e3               # m

def phi(E, dm2_eff=dm2):
    return dm2_eff*L_DUNE/(4*hbar_c*E)

ok = 0
print("="*65)
print("PRÜFSKRIPT 340b: Spirale / Nichtschließung / Breitband")
print("="*65)

# ---------------------------------------------------------------- 1
print("\nASSERTION 1: Z_13 x Z_24 teilerfremd -> kgV = 312 [B]")
g = gcd(13, 24); kgv = 13*24//g
assert g == 1 and kgv == 312
print(f"  gcd(13,24) = {g}, kgV = {kgv}  [OK]")
print(f"  13 = |Z_13| (Frobenius-Orbitphasen 2*pi*k/13)")
print(f"  24 = Kissing(D4) (SICC-Richtungsquantisierung)")
print(f"  -> kombinierte Winkelstruktur schliesst erst nach 312 Schritten")
ok += 1

# ---------------------------------------------------------------- 2
print("\nASSERTION 2: Phase am 0.5-GeV-Clamp ~ 8 rad [K]")
p05 = phi(0.5e9)
assert abs(p05 - 8.06) < 0.05, p05
print(f"  phi(0.5 GeV) = {p05:.3f} rad = {p05/np.pi:.3f} pi  [OK]")
ok += 1

# ---------------------------------------------------------------- 3
print("\nASSERTION 3: Nichtschließung der Spirale über [0.5, 5] GeV [B]")
dphi = phi(0.5e9) - phi(5.0e9)
rest = dphi % (2*np.pi)
assert rest > 0.1 and abs(rest - 2*np.pi) > 0.1, rest
print(f"  phi(0.5) - phi(5.0) = {dphi:.4f} rad = {dphi/(2*np.pi):.3f} Umläufe")
print(f"  Rest mod 2pi = {rest:.4f} rad = {np.degrees(rest):.1f} deg  (≠ 0)  [OK]")
print(f"  -> phi ~ 1/E ist nicht periodisch in E: die Kurve schliesst nicht")
ok += 1

# ---------------------------------------------------------------- 4
print("\nASSERTION 4: Monochromatisch 2.5 GeV -> ~99.8 % Verschwindung [K]")
P_mono = np.sin(phi(2.5e9))**2
assert abs(P_mono - 0.998) < 0.002, P_mono
print(f"  phi(2.5 GeV) = {phi(2.5e9):.4f} rad, sin^2 = {P_mono*100:.2f} %  [OK]")
ok += 1

# ---------------------------------------------------------------- 5
print("\nASSERTION 5: Breitband (clamped Normal 2.5±1.0 GeV, [0.5,5]) -> ~76 % [K]")
rng = np.random.default_rng(2026)
N = 5_000_000
E = np.clip(rng.normal(2.5e9, 1.0e9, N), 0.5e9, 5.0e9)
P_broad = np.mean(np.sin(phi(E))**2)
frac_clamp = np.mean(rng.normal(2.5e9, 1.0e9, N) < 0.5e9)
assert 0.74 < P_broad < 0.79, P_broad
print(f"  <sin^2 phi> = {P_broad*100:.2f} %  (SICC V3: 76.16 %)  [OK]")
print(f"  Anteil auf 0.5-GeV-Spike: {frac_clamp*100:.1f} %")
print(f"  -> Spektrumsform bestimmt die Observable; reale LBNF-Flusstabelle nötig")
ok += 1

# ---------------------------------------------------------------- 6
print("\nASSERTION 6: K_frak nicht auf Verhältnis anwendbar [K]")
K_frak = 1 - 100*xi
dm2_frak = dm2*K_frak
dev_base = abs(dm2      - 2.5e-3)/2.5e-3
dev_frak = abs(dm2_frak - 2.5e-3)/2.5e-3
assert dev_frak > dev_base
P_frak = np.mean(np.sin(phi(E, dm2_frak))**2)
assert abs(P_frak - P_broad) < 0.005
print(f"  K_frak = 1-100*xi = {K_frak:.6f}")
print(f"  dm2 Abw. ohne K_frak: {dev_base*100:.2f} %, mit: {dev_frak*100:.2f} %  (schlechter)")
print(f"  Breitband-Effekt: {abs(P_frak-P_broad)*100:.2f} Prozentpunkte (unter Auflösung)")
print(f"  -> K_frak betrifft absolute Skala (Dok. 011/133), nicht Verhältnisse (Dok. 306)  [OK]")
ok += 1

print("\n" + "="*65)
print(f"ALLE {ok}/6 ASSERTIONS BESTANDEN")
print("="*65)
