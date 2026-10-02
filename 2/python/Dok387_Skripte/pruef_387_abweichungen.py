#!/usr/bin/env python3
"""
pruef_387_abweichungen.py -- Dok. 387: Die Abweichungen im Überblick.

Rechnet alle Restabweichungen der FFGFT nach, getrennt nach Verhältnissen der
Grundform und Übersetzung in SI, jeweils gegen den Messwert mit seiner
Unsicherheit (CODATA 2022, PDG 2024, NuFIT wie im Korpus). Dazu die drei
Korrekturgrößen beta_T (Higgs), K_frak und den Faktor 10 in v/E_P.
"""
import math

ok = n = 0
def check(name, cond, info=""):
    global ok, n
    n += 1; ok += bool(cond)
    print(f"  [{'OK ' if cond else 'FAIL'}] {name}" + (f"  ({info})" if info else ""))

pi = math.pi; xi = 4 / 30000; K = 74 / 75
me, mmu, mtau, dmtau = 0.51099895000, 105.6583755, 1776.93, 0.09     # MeV
ai = 137.035999177; a = 1 / ai
mh, dmh = 125.20, 0.11; MZ, dMZ = 91.1876, 0.0021; MW, dMW = 80.3692, 0.0133
mt, dmt = 172.57, 0.29; v = 246.21965; EP = 1.220890e19   # GeV
lam, dlam = 0.22501, 0.00068; s13, ds13 = 0.0220, 0.0007
atm, datm = 2.500e-3, 0.028e-3; sol, dsol = 7.53e-5, 0.18e-5

print("1. Verhältnisse der Grundform")
r1 = 12/5 * xi**-0.5
check("m_mu/m_e = 120 sqrt3 = 207,85, +0,52 % (Messfehler 2e-8)", abs(r1 - 207.846) < 0.001 and abs(r1/(mmu/me) - 1 - 0.00521) < 0.0001)
r2 = 125/144 * xi**(-1/3)
check("m_tau/m_mu = 16,99, +1,03 % (Messfehler 5e-5)", abs(r2/(mtau/mmu) - 1 - 0.0103) < 0.0002)
Q = (me+mmu+mtau)/(math.sqrt(me)+math.sqrt(mmu)+math.sqrt(mtau))**2
hh = 1e-6; dQ = ((me+mmu+mtau+hh)/(math.sqrt(me)+math.sqrt(mmu)+math.sqrt(mtau+hh))**2 - Q)/hh*dmtau
check("Koide Q - 2/3 = -0,017 xi, Messfehler 0,038 xi (0,4 sigma)", abs((Q-2/3)/xi + 0.0165) < 0.001 and abs(dQ/xi - 0.038) < 0.002)
vEP = xi**4/(5*pi); vEPm = v/EP
check("v/E_P = xi^4/(5 pi), -0,23 % (Messfehler G: 1e-5)", abs(vEP/vEPm - 1 + 0.00233) < 0.0001)
bT = mh**2/(64*pi**3*v**2)/xi
check("Higgs: beta_T = xi_EFT/xi = 0,977 (-2,3 %), Messfehler m_h 0,18 %", abs(bT - 0.9772) < 0.0002 and abs(2*dmh/mh - 0.00176) < 0.00002)
rq = 120/(11/3)
check("Dm2_atm/Dm2_sol = 32,7 gegen 33,2, -1,4 % (Messfehler 2,6 %)", abs(rq/(atm/sol) - 1 + 0.0143) < 0.001 and abs(math.hypot(datm/atm, dsol/sol) - 0.026) < 0.002)
s13f = (25*xi)**(2/3)
check("sin^2 theta13 = 0,0223, +1,4 % (0,4 sigma)", abs(s13f/s13 - 1 - 0.014) < 0.002 and abs((s13f-s13)/ds13 - 0.44) < 0.05)
MWf = MZ*math.sqrt(7/9)
check("M_W aus 2/9 = 80,42 GeV, 3,8 sigma", abs(MWf - 80.420) < 0.001 and abs((MWf-MW)/math.hypot(dMW, dMZ*math.sqrt(7/9)) - 3.78) < 0.02)
check("m_h = 11/8 M_Z = 125,38 GeV, +0,15 %, 1,7 sigma", abs(11/8*MZ - 125.383) < 0.001 and abs((11/8*MZ - mh)/dmh - 1.66) < 0.02)
check("m_t = (11/8)^2 M_Z = 172,40 GeV, -0,10 %, 0,6 sigma", abs(((11/8)**2*MZ - mt)/dmt + 0.58) < 0.02)
check("lambda_CKM = xi^(1/6) = 0,2260, +0,46 %, 1,5 sigma", abs((xi**(1/6) - lam)/dlam - 1.49) < 0.02)

check("M_W/M_Z = sqrt(7/9): +0,06 % bei Messfehler 1,7e-4", abs(MZ*math.sqrt(7/9)/MW - 1 - 0.00063) < 0.00003)
check("beta_T-Rest 13-mal größer als Messfehler; K^sqrt3 = 0,9770", abs((1-bT)/(2*dmh/mh) - 12.9) < 0.3 and abs(K**math.sqrt(3) - 0.9770) < 0.0001)
print("\n2. Übersetzung in SI")
check("alpha^-1 = K/(xi m_e m_mu) = 137,059, +1,7e-4 (Messfehler 1,5e-10)", abs(K/(xi*me*mmu)/ai - 1 - 1.68e-4) < 0.02e-4)
check("Galois 3700/27 = 137,037, +7,6 ppm", abs(3700/27/ai - 1 - 7.6e-6) < 0.1e-6)
check("m_e m_mu = 53,991 MeV^2, -1,6e-4 gegen 54", abs(me*mmu/54 - 1 + 1.61e-4) < 0.02e-4)
chain = [r*xi**(p+4)*EP*1e3/(5*pi)/m - 1 for r, p, m in ((4/3, 1.5, me), (16/5, 1, mmu), (25/9, 2/3, mtau))]
check("Kette mit E_P: e -1,32 %, mu -0,80 %, tau +0,22 %", abs(chain[0]+0.01318) < 0.00005 and abs(chain[1]+0.00804) < 0.00005 and abs(chain[2]-0.00222) < 0.00005)
check("Elektronrest der Kette = K - 1 bis auf 1,6e-4", abs((1+chain[0])/K - 1 - 1.57e-4) < 0.05e-4)
vl = me*1e-3/((4/3)*xi**1.5)
check("v aus der Leiter mit m_e: 248,93 GeV (+1,10 %); mit K: 245,61 GeV (-0,25 %)", abs(vl - 248.928) < 0.005 and abs(vl*K/v - 1 + 0.00248) < 0.0001)
mnu = xi**2/2*me*1e6          # eV
A, S = 120*mnu**2, 11/3*mnu**2
check("Dm2_atm = 2,476e-3: -1,0 % (-0,9 sigma); Dm2_sol = 7,565e-5: +0,46 % (0,2 sigma)", abs(A/atm-1+0.0096) < 0.0005 and abs((A-atm)/datm+0.86) < 0.03 and abs(S/sol-1-0.0046) < 0.0005 and abs((S-sol)/dsol-0.19) < 0.03)

print("\n3. Korrekturgrößen")
for name, vv, target in (("v gemessen", v, 0.9772), ("v Leiter nackt", vl, 0.9561), ("v Kette xi^4 E_P/(5pi)", xi**4*EP/(5*pi), 0.9818)):
    b = mh**2/(64*pi**3*vv**2)/xi
    check(f"beta_T mit {name} = {target}", abs(b - target) < 0.0002, f"{b:.4f}")
def psi1(x):
    s = 0
    while x < 50: s += 1/x**2; x += 1
    return s + 1/x + 1/(2*x**2) + 1/(6*x**3) - 1/(30*x**5) + 1/(42*x**7)
Ka = xi*me*mmu*ai
check("K_alpha = 0,98650; 74/75 +1,7e-4, (1-xi)^100 +2,6e-4, 1-psi'(75) +7,8e-5", abs(Ka-0.986501) < 1e-6 and abs(K/Ka-1-1.68e-4) < 0.02e-4 and abs((1-xi)**100/Ka-1-2.57e-4) < 0.02e-4 and abs((1-psi1(75))/Ka-1-7.8e-5) < 0.2e-5)
need = xi**4*EP/v
check("Faktor 10: benötigter Nenner mit v gemessen 15,671 (5 pi = 15,708)", abs(need - 15.671) < 0.001)
needl = xi**4*EP/vl
check("mit v nackt aus der Leiter 15,501: 5 pi K = 15,4985, pi^3/2 = 15,5031", abs(needl - 15.501) < 0.001 and abs(5*pi*K/needl - 1) < 2e-4 and abs(pi**3/2/needl - 1) < 2e-4)
r = EP/(7491.8**4*pi/2)
check("Herkunft: m_P/(f^4 pi/2) mit f = 7491,8 = 2467 GeV, Lücke 10,02", abs(r - 2467) < 1 and abs(r/v - 10.02) < 0.01)

print(f"\nErgebnis: {ok}/{n} OK")
raise SystemExit(0 if ok == n else 1)
