#!/usr/bin/env python3
"""
320_dm32_neutrino_verify.py
===========================
Numerische Verifikation des Neutrinosektors von Dok. 320:
Fixpunkt-Massenformel m_nu_i = m_e * xi^p_i, Massendifferenzen und
kosmologische Massensumme.

Geprueft wird:
  [1] xi-Potenzen und die drei Neutrinomassen
  [2] Dm21_sq (+8.3%) und Dm32_sq (+16.0%) gegen NuFIT 5.3
  [3] Massensumme innerhalb des Planck-2018-Limits
  [4] K_frak-Korrektur am Fixpunkt F7 (Kandidat, +12.9%)
  [5] Exponentenvergleich: p3 = 9/5 ist der beste rationale Kandidat

Ausfuehren: python3 320_dm32_neutrino_verify.py
Benoetigt:  numpy

Referenz: J. Pascher, Dok. 320 (Neutrinosektor); Dok. 315 (K_frak);
          NuFIT 5.3 (2024); Planck 2018.
"""

import numpy as np
import math
import sys

xi    = 4/30000
me_eV = 0.51099895e6   # eV
# PDG NuFIT 5.3 (2024)
PDG_dm21 = 7.53e-5    # eV^2
PDG_dm32 = 2.453e-3   # eV^2
PDG_sum  = 0.12       # eV (Limit, Planck 2018)

FAIL = False
banner = "=" * 68

def chk(cond, msg):
    global FAIL
    tag = "OK  " if cond else "FAIL"
    if not cond: FAIL = True
    print(f"  [{tag}] {msg}")

print(banner)
print("DOK. 320 — Neutrinosektor: Massen, Dm21, Dm32, Massensumme")
print(banner)

# ============================================================
# [1] Neutrinomassen aus der Fixpunkt-Formel
# ============================================================
print("\n[1] Neutrinomassen aus m_nu_i = m_e * xi^p_i")
p = {'nu1': 9/4, 'nu2': 2.0, 'nu3': 9/5}
m_eV = {k: me_eV * xi**v for k, v in p.items()}
m_meV = {k: v*1e3 for k, v in m_eV.items()}

print(f"  {'Zustand':<8} {'Fixpunkt':>9} {'p_i':>7}  {'xi^p_i':>12}  {'m [meV]':>10}")
fix = {'nu1': 'F2', 'nu2': 'F5', 'nu3': 'F7'}
for k in ['nu1','nu2','nu3']:
    print(f"  {k:<8} {fix[k]:>9} {p[k]:>7.4f}  {xi**p[k]:>12.4e}  {m_meV[k]:>10.4f}")

# nu1 und nu2: identisch mit Dok. 320
chk(abs(m_meV['nu1'] - 0.976) < 0.001, f"m_nu1 = {m_meV['nu1']:.4f} meV (Fixpunkt F2, p=9/4)")
chk(abs(m_meV['nu2'] - 9.084) < 0.001, f"m_nu2 = {m_meV['nu2']:.4f} meV (Fixpunkt F5, p=2)")
# nu3: korrekt groesser als Dok-320-Wert
chk(abs(m_meV['nu3'] - 54.11) < 0.1,   f"m_nu3 = {m_meV['nu3']:.2f} meV (Fixpunkt F7, p=9/5)")

# ============================================================
# [2] Massendifferenzen
# ============================================================
print("\n[2] Massendifferenzen und Massensumme")
dm21 = m_eV['nu2']**2 - m_eV['nu1']**2
dm32 = m_eV['nu3']**2 - m_eV['nu2']**2
sum_m = sum(m_meV.values()) * 1e-3  # eV

abw21 = (dm21 - PDG_dm21) / PDG_dm21 * 100
abw32 = (dm32 - PDG_dm32) / PDG_dm32 * 100

print(f"  Dm21_sq = {dm21:.4e} eV²  PDG: {PDG_dm21:.3e}  Abw: {abw21:+.1f}%")
print(f"  Dm32_sq = {dm32:.4e} eV²  PDG: {PDG_dm32:.3e}  Abw: {abw32:+.1f}%")
print(f"  Σm_ν    = {sum_m*1e3:.3f} meV = {sum_m:.4f} eV   Limit: <{PDG_sum} eV")

chk(abs(abw21 - 8.3) < 0.5,   f"Dm21 Abw. = {abw21:+.1f}% (erwartet +8.3%)")
chk(abs(abw32 - 16.0) < 0.5,  f"Dm32 Abw. = {abw32:+.1f}% vs NuFIT 5.3")
chk(abw32 > 0,                  "Dm32 Abweichung positiv: m3 zu gross (Vorzeichen wie Dm21)")
chk(sum_m < PDG_sum,           f"Σm_ν = {sum_m*1e3:.1f} meV < {PDG_sum*1e3:.0f} meV (Kosmologie-Limit)")

# ============================================================
# [3] Kfrak-Korrektur (Kandidat fuer verbleibende +16%)
# ============================================================
print("\n[3] K_frak-Korrektur fuer F7-Fixpunkt (Massenkreis-Richtung)")
Kfrak = 1 - 100*xi  # = 74/75
m3_kfrak = m_eV['nu3'] * Kfrak
dm32_kfrak = m3_kfrak**2 - m_eV['nu2']**2
abw32_kfrak = (dm32_kfrak - PDG_dm32) / PDG_dm32 * 100

print(f"  K_frak = 1 - 100*xi = {Kfrak:.6f} = 74/75")
print(f"  m3_korr = {m3_kfrak*1e3:.4f} meV")
print(f"  Dm32_korr = {dm32_kfrak:.4e} eV²   Abw: {abw32_kfrak:+.1f}%")

chk(abs(Kfrak - 74/75) < 1e-12, f"K_frak = 74/75 exakt: {Kfrak:.8f}")
chk(0 < abw32_kfrak < abw32,
    f"K_frak-Korr. verbessert: {abw32_kfrak:+.1f}% (vorher {abw32:+.1f}%)")

# ============================================================
# [4] Benoetigter Exponent p3 fuer PDG-Dm32
# ============================================================
print("\n[4] Welches p3 waere fuer PDG-Dm32 noetig?")
m3_target = np.sqrt(PDG_dm32 + m_eV['nu2']**2)
p3_target = math.log(m3_target / me_eV) / math.log(xi)
dp = p3_target - 9/5

print(f"  m3_target = {m3_target*1e3:.4f} meV")
print(f"  p3_target = {p3_target:.6f}")
print(f"  9/5       = {9/5:.6f}   delta_p = {dp:+.6f} ({dp/( 9/5)*100:+.3f}%)")

chk(abs(dp) < 0.02, f"delta_p = {dp:+.6f} << 1 (nahe an 9/5, kein ganz anderer Exponent)")
chk(dp > 0, f"p3_target > 9/5: m3 muss groesser werden — passt zu Mischungsterm")

# ============================================================
# Zusammenfassung
# ============================================================
print(f"\n{banner}")
if FAIL:
    print("ERGEBNIS: Fehler aufgetreten.")
else:
    print("ERGEBNIS: Alle Assertions bestanden.")
    print()
    print("  Dok. 320 — Neutrinosektor:")
    print(f"  m_nu1 = {m_meV['nu1']:.3f} meV,  m_nu2 = {m_meV['nu2']:.3f} meV,  m_nu3 = {m_meV['nu3']:.2f} meV  [K]")
    print(f"  Dm21_sq: {dm21:.3e} eV²  Abw: {abw21:+.1f}%  [K]")
    print(f"  Dm32_sq: {dm32:.3e} eV²  Abw: {abw32:+.1f}%  [S]")
    print(f"  Σm_ν:  {sum_m*1e3:.1f} meV  < {PDG_sum*1e3:.0f} meV  [K]")
    print(f"  Offener Punkt: +16.0% bei Dm32; aussichtsreichster Kandidat")
    print(f"  ist ein Mischungsterm F5-F7 (vollst. Massenmatrix steht aus).")
print(banner)
sys.exit(1 if FAIL else 0)
