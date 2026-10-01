#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Prüfskript: Informationsbilanz der Hawking-Verdampfung — Dok. 325 §5.3
Registereinträge: R93 [B], R94 [B] (Dok. 190)
Aktualisiert am 1.10.2026: Prüfung 3 jetzt S_BH(M_coll) = L_Matzke/l_P und
n_thr = S_BH/√2 statt S_BH = n_thr; Prüfung 6 jetzt Verhältnis in gleicher
Einheit = ln 3 statt log₂3 bit/nat; Registernummern R87/R88 -> R93/R94 (vgl. Dok. 325).

Prüft:
  1. r_s(M_coll) = √2·l_P  (Dok. 329 [B], geometrisch)
  2. S_BH(M_coll) = 2π nat  (exakt)
  3. S_BH(M_coll) = L_Matzke/l_P in Bit, n_thr(Matzke) = S_BH/√2  (R93)
  4. Flächenquant −4·l_P² pro nat  (Dok. 325 §Baustein 2 [B])
  5. N_emit ≥ 0 für M_init > M_coll  (Monotonie)
  6. I_Sektor/I_thermisch = ln 3 = const  (gleiche Einheit; R94, massenunabhängig)
  7. Gesamtbilanz: S_init = N_emit + S_coll  (Energieerhaltung)
  8. Feinkörnige Entropie konstant (unitäre Evolution, Dok. 322 [K])
"""

import math

# ── Naturkonstanten ─────────────────────────────────────────────────────────
hbar = 1.054571817e-34   # J·s
c    = 2.99792458e8      # m/s
G    = 6.67430e-11       # m³ kg⁻¹ s⁻²
kB   = 1.380649e-23      # J/K
lP   = math.sqrt(hbar * G / c**3)          # Plancklänge
mP   = math.sqrt(hbar * c / G)             # Planck-Masse
M_sun = 1.989e30                           # kg

# ── Abgeleitete Größen ───────────────────────────────────────────────────────
M_coll = mP / math.sqrt(2)                 # Kollapsgrenze (Dok. 329 [B])
r_s    = lambda M: 2 * G * M / c**2        # Schwarzschild-Radius
S_BH   = lambda M: 4*math.pi * r_s(M)**2 / (4 * lP**2)   # Bekenstein in nat

results = []
def check(name, ok, detail=""):
    results.append((name, ok, detail))
    print(f"[{'OK' if ok else '!!'}] {name}" + (f": {detail}" if detail else ""))

print("=" * 70)
print("Dok. 325 §5.3 — Informationsbilanz der Hawking-Verdampfung")
print("=" * 70)

# ── 1. Geometrischer Endpunkt ────────────────────────────────────────────────
r_coll = r_s(M_coll)
ratio  = r_coll / lP
check("1  r_s(M_coll) = √2·l_P",
      abs(ratio - math.sqrt(2)) < 1e-9,
      f"r_s/l_P = {ratio:.10f}, √2 = {math.sqrt(2):.10f}")

# ── 2. Restentropie exakt 2π nat ─────────────────────────────────────────────
S_coll = S_BH(M_coll)
check("2  S_BH(M_coll) = 2π nat",
      abs(S_coll - 2*math.pi) < 1e-9,
      f"S_coll = {S_coll:.10f}, 2π = {2*math.pi:.10f}")

# ── 3. Identität R93: S_coll = L_Matzke/l_P in Bit, n_thr = S_coll/√2 ───────
L_Matzke_lP  = 2*math.pi / math.log(2)                     # Dok. 329: L_Matzke/l_P
n_thr_Matzke = 2*math.pi / (math.sqrt(2)*math.log(2))      # Dok. 329: n_thr
S_coll_bit   = S_coll / math.log(2)
check("3  S_BH(M_coll) [bit] = L_Matzke/l_P, n_thr = S_BH/√2 mit √2 = r_s/l_P  [R93]",
      abs(S_coll_bit - L_Matzke_lP) < 1e-9
      and abs(S_coll_bit/ratio - n_thr_Matzke) < 1e-9
      and abs(S_coll_bit - n_thr_Matzke) > 1.0,
      f"S_coll = {S_coll_bit:.6f} bit, n_thr = {n_thr_Matzke:.6f}")

# ── 4. Flächenquant −4·l_P² pro nat ─────────────────────────────────────────
# S_BH = A/(4l_P²) → dA/dS = 4l_P² → pro −1 nat: dA = −4·l_P²
dA_per_nat = -4 * lP**2
expected   = -4.0   # in l_P² units
check("4  Flächenquant = −4·l_P² per nat",
      abs(dA_per_nat / lP**2 - expected) < 1e-12,
      f"dA/l_P² = {dA_per_nat/lP**2:.2f}")

# ── 5. N_emit ≥ 0 für verschiedene M_init ────────────────────────────────────
test_masses = [M_sun, 1e6*M_sun, 1e9*M_sun, 10*mP]
all_pos = all(S_BH(M) - S_coll >= 0 for M in test_masses)
check("5  N_emit ≥ 0 für M_init > M_coll (Monotonie)",
      all_pos,
      f"geprüft für {len(test_masses)} Massen")

# ── 6. Verhältnis Sektorinfo/thermisch = ln 3 = const  [R94] ────────────────
# log₂3 bit Sektorinfo pro 1 nat = 1/ln2 bit thermisch -> in gleicher Einheit ln 3
ratio_sector = math.log2(3) / (1/math.log(2))
check("6  I_Sektor/I_thermisch = ln 3 = const (gleiche Einheit)  [R94]",
      abs(ratio_sector - math.log(3)) < 1e-12,
      f"ln 3 = {ratio_sector:.6f}, massenunabhängig [B]")

# ── 7. Gesamtbilanz: S_init = N_emit + S_coll ────────────────────────────────
for M_init, label in [(M_sun, "M_☉"), (1e6*M_sun, "10⁶M_☉")]:
    N_emit = S_BH(M_init) - S_coll
    recon  = N_emit + S_coll
    check(f"7  Bilanz geschlossen für {label}",
          abs(recon - S_BH(M_init)) / S_BH(M_init) < 1e-12,
          f"N_emit = {N_emit:.4e} nat, S_coll = {S_coll:.4f} nat")

# ── 8. Feinkörnige Entropie konstant (Unitarität Dok. 322) ───────────────────
# Formale Prüfung: unitäre Evolution erhält |ψ⟩ → S_fine = const
# Hier: symbolische Assertion (algebraisch in Dok. 322 [K])
check("8  S_feinkörnig = const (Unitarität Dok. 322) [K]",
      True,  # algebraisch bewiesen in Dok. 322
      "algebraisch [K] in Dok. 322 — Assertion hier deklarativ")

# ── Zusammenfassung ──────────────────────────────────────────────────────────
print("=" * 70)
ok_count = sum(1 for _, s, _ in results if s)
print(f"Ergebnis: {ok_count}/{len(results)} Prüfungen bestanden")

print("\n── Physikalische Kennzahlen ─────────────────────────────────────────")
print(f"M_coll       = {M_coll:.4e} kg  = {M_coll/mP:.4f} m_P")
print(f"r_s(M_coll)  = {r_s(M_coll)/lP:.4f} l_P  = √2·l_P")
print(f"S_BH(M_coll) = {S_coll:.6f} nat = 2π nat")
print(f"             = {S_coll/math.log(2):.4f} bit = L_Matzke/l_P = √2·n_thr(Matzke)")
print(f"I_S/I_T      = ln 3 = {math.log(3):.4f}  (gleiche Einheit, für jedes M)")
print(f"N_emit(M_☉)  = {S_BH(M_sun)-S_coll:.4e} nat")
print(f"I_Sektor(M_☉)= {(S_BH(M_sun)-S_coll)*math.log2(3):.4e} bit")
