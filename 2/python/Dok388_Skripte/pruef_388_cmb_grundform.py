#!/usr/bin/env python3
"""
pruef_388_cmb_grundform.py -- Dok. 388: CMB-Temperatur und H0 in der Grundform.

Stellt die Wege zur CMB-Temperatur gegenüber: die eV-Relation (16/9) xi eV mit
Korrektur zweiter Ordnung (P11), ihre Einheitenabhängigkeit, die Form der
Grundform T/m_e = K xi^(5/2) mit dem Kandidaten K = (8 pi)^(1/4), die
Folgerungen (T^4 = 16 H0 m_e^3, Omega_gamma, L_xi) und den Vergleich der
H0-Formen mit Exponent 10 und 41/4. Messwerte: FIRAS (Fixsen 2009), CODATA 2022.
"""
import math
from fractions import Fraction as Fr

ok = n = 0
def check(name, cond, info=""):
    global ok, n
    n += 1; ok += bool(cond)
    print(f"  [{'OK ' if cond else 'FAIL'}] {name}" + (f"  ({info})" if info else ""))

pi = math.pi; xi = 4 / 30000
me = 0.51099895000e6; mmu = 105.6583755e6            # eV
kB = 8.617333262e-5; T = 2.72548; sT = 0.00057        # eV/K, K
e = 1.602176634e-19; kBJ = 1.380649e-23; a = 1 / 137.035999177
hbar = 6.582119569e-16; Mpc = 3.0856775814913673e22  # eV s, m
lamC = 3.8615926796e-13                               # reduzierte Compton-Länge (m)
EP = 1.220890e28                                      # eV (1/sqrt G)
kT = kB * T; t = kT / me; rT = sT / T
kmsMpc = lambda H: H / hbar * Mpc / 1e3

print("1. Die eV-Relation (P11)")
f1 = 16/9 * xi; f2 = f1 * (1 - 275/4 * xi)
check("(16/9) xi eV = 2,7507 K, +0,93 %", abs(f1*e/kBJ - 2.7507) < 1e-4 and abs(f1/kT - 1 - 0.00925) < 1e-4)
check("2. Ordnung (1 - 275 xi/4): +0,0002 %, 1/100 der FIRAS-Unsicherheit",
      abs(f2/kT - 1 - 2.14e-6) < 1e-7 and abs((f2/kT - 1)/rT) < 0.011)
kn = (1 - kT/f1) / xi
check("verlangter Koeffizient 68,766 statt 275/4 = 68,75", abs(kn - 68.766) < 0.001)
check("Raster n/4: Schritt 0,25 xi (16/9)-relativ = 3,3e-5 in T", abs(0.25*xi - 3.33e-5) < 1e-7)
check("in meV, K oder m_e stimmt (16/9) xi nicht (Faktoren 1e3, 1e4, 5e5)",
      abs(f1/(kT*1e3) - 1) > 0.9 and abs(f1/T - 1) > 0.9 and abs(f1/t - 1) > 0.9)
check("als Verhältnis: T/m_e = (16/9) xi / 510999 = 4,639e-10 gegen 4,596e-10",
      abs(f1/me - 4.639e-10) < 1e-12 and abs(t - 4.596e-10) < 1e-12)
check("alpha = 1: e_geo/e_hist = 1/sqrt(alpha) = 11,706; Energien unverändert", abs(1/math.sqrt(a) - 11.706) < 1e-3)

print("2. Andere Bezugsenergien")
u = math.sqrt(xi * me * mmu)
check("u = sqrt(xi m_e m_mu) = 84,85 keV, T/u = 2,768e-9 = 0,0876 (16/9) xi^2",
      abs(u/1e3 - 84.85) < 0.01 and abs(kT/u - 2.768e-9) < 1e-12 and abs(kT/u/(16/9*xi**2) - 0.0876) < 1e-4)
check("Hartree: T/(alpha^2 m_e) = 0,0647 xi", abs(kT/(a**2*me)/xi - 0.0647) < 1e-4)
check("eV/m_e = 1,271 xi^(3/2), 4/pi um 0,17 % daneben", abs(1/me/xi**1.5 - 1.2711) < 1e-4 and abs(1/me/xi**1.5/(4/pi) - 1 + 0.0017) < 1e-4)

print("3. Grundform: T/m_e = K xi^(5/2)")
K = t / xi**2.5
check("K gemessen = 2,23897", abs(K - 2.23897) < 1e-5)
for name, v in (("sqrt 5", math.sqrt(5)), ("9/4", 9/4), ("64/(9 pi)", 64/(9*pi))):
    check(f"Kandidat {name}: außerhalb FIRAS", abs(v/K - 1) > 3*rT, f"{(v/K-1)*100:+.2f} %")
K8 = (8*pi)**0.25; d = K8/K - 1
check("Kandidat (8 pi)^(1/4) = 2,23903: +0,0025 %, 0,12 sigma", abs(d - 2.5e-5) < 1e-6 and abs(d/rT - 0.12) < 0.01)
hits = []; tot = 0; tot10 = 0
for nn in (1, 2, 3, 4):
    for k in range(-3, 4):
        for p in range(1, 31):
            for q in range(1, 31):
                if math.gcd(p, q) != 1: continue
                v = (p/q * pi**k)**(1/nn)
                if 1.5 < v < 3.5:
                    tot += 1; tot10 += (p <= 10 and q <= 10)
                    if abs(v/K - 1) < rT: hits.append((p, q, k, nn))
exp_all = tot * 2*rT*K / 2.0; exp10 = tot10 * 2*rT*K / 2.0
check("Suche (p/q pi^k)^(1/n): 3370 Ausdrücke, 3 Treffer, zufällig 1,6 erwartet",
      tot == 3370 and len(hits) == 3 and abs(exp_all - 1.58) < 0.02, str(hits))
check("davon p, q <= 10: einziger Treffer (8 pi)^(1/4), zufällig 0,2 erwartet",
      [h for h in hits if h[0] <= 10 and h[1] <= 10] == [(8, 1, 1, 4)] and exp10 < 0.25, f"{tot10} Ausdrücke, {exp10:.2f}")

print("4. Folgerungen")
H10 = pi/2 * xi**10 * me
check("mit H0 = (pi/2) xi^10 m_e: T^4 = 8 pi xi^10 m_e^4 = 16 H0 m_e^3 (algebraisch)",
      abs(8*pi*xi**10*me**4 / (16*H10*me**3) - 1) < 1e-12)
HT = kT**4 / (16*me**3)
check("H0 aus T_CMB: 66,81 +- 0,06 km/s/Mpc", abs(kmsMpc(HT) - 66.81) < 0.01 and abs(4*rT*kmsMpc(HT) - 0.056) < 0.002)
check("gegen Planck 67,4 +- 0,5: 1,2 sigma", abs((67.4 - kmsMpc(HT))/0.5 - 1.17) < 0.02)
re = 4/3; MP = me * 5*pi/re * xi**-5.5
Om = Fr(4096, 10125)
Omx = (pi**2/15*(K8*xi**2.5*me)**4) / (3*H10**2*MP**2/(8*pi)) / xi
check("Omega_gamma = (4096/10125) xi = 0,4045 xi (T0-H0, T0-E_P)", abs(Omx - float(Om)) < 1e-12)
Omm = (pi**2/15*kT**4) / (3*H10**2*EP**2/(8*pi)) / xi
check("mit gemessenem E_P: 0,4154 xi", abs(Omm - 0.4154) < 1e-4)
Lx = (15/(8*pi**3))**0.25 * xi**-2.25 * lamC
Ldef = (15*xi/pi**2)**0.25 / kT * hbar * 299792458
check("L_xi = (15/8 pi^3)^(1/4) xi^(-9/4) lambda_e = 100,24 um, ohne T_CMB", abs(Lx*1e6 - 100.24) < 0.01 and abs(Lx/Ldef - 1) < 1e-4)

print("5. H0-Formen gegen T_CMB")
Tf = lambda H: (16*H*me**3)**0.25 / kB
for name, H, tv, sg in (("(pi/2) xi^10 m_e", H10, 66.821, 0.1),
                        ("E0 xi^(41/4), E0 = 7,398 MeV", 7.398e6*xi**10.25, 66.179, -11.4),
                        ("E0 xi^(41/4), E0 = sqrt(m_e m_mu)", math.sqrt(me*mmu)*xi**10.25, 65.731, -19.5)):
    s = (Tf(H)/T - 1)/rT
    check(f"{name}: H0 = {tv}, T-Abweichung {sg} sigma", abs(kmsMpc(H) - tv) < 0.002 and abs(s - sg) < 0.1, f"T = {Tf(H):.5f} K")
check("E0 xi^(1/4) = 0,9904 (pi/2) m_e", abs(7.398e6*xi**0.25/(pi/2*me) - 0.9904) < 1e-4)

print(f"\nErgebnis: {ok}/{n}")
