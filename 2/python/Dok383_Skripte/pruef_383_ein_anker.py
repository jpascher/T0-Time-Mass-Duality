#!/usr/bin/env python3
"""
pruef_383_ein_anker.py -- Dok. 383: Massen und Planck-Skala ohne v, eine Kette mit einem Anker.

Beziehung aus Dok. 149: v = E_P / (f^4 (pi/2) 10) = E_P xi^4 / (5 pi), f = 1/xi.
Eingesetzt in die Leptonleiter m_i = r_i xi^p_i v (Dok. 006, 352):
    m_i = r_i/(5 pi) * xi^(p_i + 4) * E_P
Ein Anker (hier m_e) legt E_P, G, l_P, L_0 fest; v wird nicht gebraucht.
"""
import math

ok = n = 0
def check(name, cond, info=""):
    global ok, n
    n += 1; ok += bool(cond)
    print(f"  [{'OK ' if cond else 'FAIL'}] {name}" + (f"  ({info})" if info else ""))

xi = 4 / 30000; f = 1 / xi; pi = math.pi
hbar, c, MeV = 1.054571817e-34, 299792458.0, 1.602176634e-13
G_codata = 6.67430e-11
EP = math.sqrt(hbar * c**5 / G_codata) / MeV          # MeV, gemessen (Komparator)
me, mmu, mtau, v_sm = 0.51099895, 105.6583755, 1776.86, 246.21965e3
lP_codata = 1.616255e-35
r = {"e": 4/3, "mu": 16/5, "tau": 25/9}
p = {"e": 3/2, "mu": 1.0, "tau": 2/3}
mexp = {"e": me, "mu": mmu, "tau": mtau}

print("1. Beziehung v/E_P (Dok. 149)")
k = xi**4 / (5 * pi)
check("E_P/(f^4 (pi/2) 10) = E_P xi^4/(5 pi) (algebraisch)", abs(1/(f**4*(pi/2)*10) - k) < 1e-30)
check("v/E_P = xi^4/(5 pi) = 2,0120e-17", abs(k - 2.0120e-17) < 1e-21, f"{k:.5e}")
d = (k/(v_sm/EP) - 1) * 100
check("gegen v/E_P gemessen: -0,23 %", abs(d + 0.233) < 0.01, f"{d:+.3f} %")
check("mit f = 7500: v = 245,65 GeV", abs(EP*k/1e3 - 245.65) < 0.01, f"{EP*k/1e3:.2f} GeV")
check("Dok. 149 mit f = 7491,91: v = 246,71 GeV", abs(1.220910e22/(7491.91**4*(pi/2)*10)/1e3 - 246.71) < 0.01)
wrong = EP / f**2 / math.sqrt(4*pi) / 1e3
check("Dok. 150 schreibt E_P/(f^2 sqrt(4 pi)): ergibt 6,1e10 GeV, nicht 246,7", abs(wrong/6.12e10 - 1) < 0.01, f"{wrong:.3e} GeV")

print("\n2. Massen ohne v: m_i = r_i/(5 pi) xi^(p_i+4) E_P")
dev = {}
for l in ("e", "mu", "tau"):
    m = r[l] / (5*pi) * xi**(p[l] + 4) * EP
    dev[l] = (m/mexp[l] - 1) * 100
    print(f"     {l:>3}: Koeff {r[l]/(5*pi):.6f}, Exponent {p[l]+4:.4f}, m = {m:.4f} MeV ({dev[l]:+.2f} %)")
check("Elektron: 4/(15 pi) xi^(11/2) E_P, -1,32 %", abs(dev['e'] + 1.318) < 0.01)
check("Myon: 16/(25 pi) xi^5 E_P, -0,80 %", abs(dev['mu'] + 0.803) < 0.01)
check("Tau: 5/(9 pi) xi^(14/3) E_P, +0,23 %", abs(dev['tau'] - 0.226) < 0.01)
check("Massenverhältnisse unabhängig von E_P und 5 pi (= Leiter Dok. 352)",
      abs((r['mu']/r['e'])*xi**(p['mu']-p['e']) - 12/5*xi**-0.5) < 1e-9)

print("\n3. Ein Anker: m_e -> E_P, G, l_P, L_0")
EPa = me / (4/(15*pi) * xi**5.5)
Ga = hbar * c**5 / (EPa*MeV)**2
lPa = math.sqrt(hbar * Ga / c**3)
check("E_P aus m_e: +1,34 %", abs((EPa/EP-1)*100 - 1.335) < 0.01, f"{EPa:.4e} MeV")
check("G = hbar c^5/E_P^2 aus m_e: -2,6 %", abs((Ga/G_codata-1)*100 + 2.62) < 0.05, f"{Ga:.4e}")
check("l_P aus m_e: -1,3 %", abs((lPa/lP_codata-1)*100 + 1.32) < 0.02, f"{lPa:.4e} m")
check("L_0 = xi l_P", abs(xi*lPa - 2.1266e-39) < 1e-42, f"{xi*lPa:.4e} m")
check("G-Abweichung = doppelte E_P-Abweichung (G ~ 1/E_P^2)", abs((Ga/G_codata) - (EP/EPa)**2) < 1e-12)

print("\n4. Anker v statt m_e (Vergleich)")
EPv = v_sm / k
Gv = hbar * c**5 / (EPv*MeV)**2
check("E_P aus v: +0,23 %, G: -0,46 %", abs((Gv/G_codata-1)*100 + 0.465) < 0.01, f"{(Gv/G_codata-1)*100:+.3f} %")
print("     Ankerwahl -> Abweichung von E_P, G, l_P:")
anker = {}
for l in ("e", "mu", "tau"):
    E = mexp[l] / (r[l]/(5*pi) * xi**(p[l]+4))
    anker[l] = (E/EP - 1) * 100
anker["v"] = (EPv/EP - 1) * 100
for a, dE in anker.items():
    dG = ((1 + dE/100)**-2 - 1) * 100
    dl = ((1 + dE/100)**-1 - 1) * 100
    print(f"       Anker {a:>3}: E_P {dE:+.2f} %, G {dG:+.2f} %, l_P {dl:+.2f} %")
check("Anker Myon: E_P +0,81 %", abs(anker['mu'] - 0.81) < 0.01, f"{anker['mu']:+.3f} %")
check("Anker Tau: E_P -0,23 %", abs(anker['tau'] + 0.225) < 0.01, f"{anker['tau']:+.3f} %")
q = 2.0389e-17 / k
check("Weg Dok. 375 (v aus m_e, E_P über C_conv) gegen direkten Weg: Faktor = 1/(1 + Rest Elektron)",
      abs(q - 1/(1 + dev['e']/100)) < 2e-3, f"{q:.4f} gegen {1/(1+dev['e']/100):.4f}")

print("\n5. C_conv als Kurzform")
K = 0.986
Cimp = Ga / (xi**2/(4*me) * K)
check("C_conv aus der Ein-Anker-Kette: 7,58e-3 (Dok. 012: 7,783e-3, Unterschied = Rest der Kette)",
      abs(Cimp - 7.58e-3) < 0.01e-3, f"{Cimp:.4e}")

print("\n" + "=" * 70)
print(f"ERGEBNIS: {ok}/{n} Prüfungen bestanden")
assert ok == n
