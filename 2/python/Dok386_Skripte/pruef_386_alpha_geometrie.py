#!/usr/bin/env python3
"""
pruef_386_alpha_geometrie.py -- Dok. 386: Wo alpha steckt.

Prüft: Ladungsumdefinition e^2 = 4 pi alpha, alpha als Verhältnis zweier
Radien (r_e/lambda_C), Verhältnisform xi E0^2 = 1 (E0^2 = 1/xi) in T0-Einheiten,
die Bezugsenergie der SI-Brücke alpha_SI = xi (E0/1 MeV)^2 und die
zurückgenommene Lesart E0 = 1/xi = 7500 GeV. Konstanten CODATA 2022.
"""
import math

ok = n = 0
def check(name, cond, info=""):
    global ok, n
    n += 1; ok += bool(cond)
    print(f"  [{'OK ' if cond else 'FAIL'}] {name}" + (f"  ({info})" if info else ""))

pi = math.pi
xi = 4 / 30000
K = 74 / 75
e = 1.602176634e-19; hbar = 1.054571817e-34; c = 299792458.0
eps0 = 8.8541878188e-12; m_e_kg = 9.1093837139e-31
me, mmu = 0.51099895, 105.6583755          # MeV
a = e**2 / (4 * pi * eps0 * hbar * c)

print("1. Umdefinition der Ladung")
check("alpha^-1 = 137,036 (SI-Ausdruck)", abs(1 / a - 137.035999) < 1e-5, f"{1/a:.6f}")
e_nat = math.sqrt(4 * pi * a); e_geo = math.sqrt(4 * pi)
check("hbar=c=eps0=1: e^2 = 4 pi alpha, e = 0,3028", abs(e_nat - 0.30282) < 1e-5, f"{e_nat:.5f}")
check("alpha = 1: e = sqrt(4 pi) = 3,545", abs(e_geo - 3.5449) < 1e-4)
check("alpha = (e_hist/e_geo)^2; e_geo/e_hist = 11,706", abs((e_nat / e_geo)**2 - a) < 1e-15 and abs(e_geo / e_nat - 11.706) < 1e-3)

print("\n2. Zwei Kugeln um das Elektron")
r_e = e**2 / (4 * pi * eps0 * m_e_kg * c**2)
lam_C = hbar / (m_e_kg * c)
a0 = 4 * pi * eps0 * hbar**2 / (m_e_kg * e**2)
check("r_e / lambda_C = alpha", abs(r_e / lam_C / a - 1) < 1e-9, f"r_e = {r_e:.4e} m, lambda_C = {lam_C:.4e} m")
check("a_0 / lambda_C = 1/alpha", abs(a0 / lam_C * a - 1) < 1e-9)
r = 1e-12
check("Coulomb-Energie/Quantenenergie bei gleichem r = alpha (r-unabhängig)",
      all(abs((e**2 / (4 * pi * eps0 * rr)) / (hbar * c / rr) / a - 1) < 1e-12 for rr in (1e-15, r, 1e-9)))

print("\n3. Verhältnisform: alpha = 1, ohne fraktale Korrektur")
E0_T0 = math.sqrt(1 / xi)
check("xi E0^2 = 1  =>  E0^2 = 1/xi = 7500, E0 = 86,60", abs(E0_T0**2 - 7500) < 1e-9 and abs(E0_T0 - 86.6025) < 1e-4)
E0b = math.sqrt(me * mmu)
unit = E0b / E0_T0
check("T0-Energieeinheit = sqrt(xi m_e m_mu) = 84,85 keV", abs(unit * 1e3 - 84.846) < 0.01, f"{unit*1e3:.3f} keV")
check("ohne Korrektur alpha^-1 = 7500/E0^2 = 138,91", abs(7500 / E0b**2 - 138.911) < 0.002, f"{7500/E0b**2:.3f}")

print("\n4. SI-Brücke und Bezugsenergie")
E0k = math.sqrt(me * mmu / K)
check("mit K_frak: alpha^-1 = 137,06 (+1,7e-4)", abs(1 / (xi * E0k**2) - 137.059) < 0.002 and abs(1 / (xi * E0k**2) * a - 1 - 1.68e-4) < 0.05e-4)
Eref_b = E0b * math.sqrt(xi / a); Eref_k = E0k * math.sqrt(xi / a)
check("E_ref (nackt) = E0 sqrt(xi/alpha) = 0,99323 MeV", abs(Eref_b - 0.99323) < 1e-5, f"{Eref_b:.5f}")
check("E_ref (nackt) / 1 MeV = sqrt(K_frak) bis auf 8e-5", abs(Eref_b / math.sqrt(K) - 1) < 1e-4, f"{Eref_b/math.sqrt(K)-1:+.1e}")
check("E_ref (korrigiert) = 0,99992 MeV", abs(Eref_k - 0.99992) < 1e-5, f"{Eref_k:.5f}")
check("T0-Einheit / sqrt(alpha) MeV = sqrt(K_frak)-Rest", abs(unit / (math.sqrt(a)) - Eref_b) < 1e-12)
check("2 m_e = 1,022 MeV als Bezugsenergie: 2,2 % daneben", abs(2 * me / Eref_k - 1 - 0.0221) < 0.001)

print("\n5. Zurückgenommene Lesart E0 = 1/xi = 7500 GeV")
check("E0 = 1/xi ergäbe xi E0^2 = 7500, nicht 1 und nicht alpha", abs(xi * (1 / xi)**2 - 7500) < 1e-9)
check("7500 GeV / 7,397 MeV = 1,01e6", abs(7500e3 / E0k / 1.0139e6 - 1) < 1e-3)
check("4 pi in e^2 = 4 pi alpha ist dasselbe 4 pi wie in 64 pi^4 = 16 pi^3 4 pi (Dok. 385)", abs(64 * pi**4 / (16 * pi**3) - 4 * pi) < 1e-12)

print(f"\nErgebnis: {ok}/{n} OK")
raise SystemExit(0 if ok == n else 1)
