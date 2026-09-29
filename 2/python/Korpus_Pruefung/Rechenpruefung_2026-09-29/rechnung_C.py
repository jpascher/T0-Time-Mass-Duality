#!/usr/bin/env python3
"""Rechenpruefung Gruppe C: Dok. 070, 077, 081, 105, 145, 146."""
from math import pi, sqrt, log, e, cos, radians

xi = 4/30000
me, mmu, mtau = 0.51099895, 105.6583755, 1776.86
me14, mmu14 = 0.5109989461, 105.6583745      # CODATA 2014
meT0, mmuT0 = 0.5108082, 105.66913           # T0-Massen Dok. 070 Z. 372f
ainv = 137.035999
alpha = 1/ainv
hbar, c = 1.054571817e-34, 299792458.0
lP, tP, mP = 1.616255e-35, 5.391247e-44, 2.176434e-8
EP_MeV = 1.22089e22
G = 6.67430e-11
mp_kg, me_kg = 1.67262192e-27, 9.1093837e-31
e_ch, eps0 = 1.602176634e-19, 8.8541878128e-12

def h(t): print("\n=== " + t)

h("070-1  alpha^-1 = 7500/(m_e m_mu) und K_frak")
for lab, a, b in [("0.511*105.658", 0.511, 105.658), ("CODATA2014", me14, mmu14),
                  ("CODATA2018", me, mmu), ("T0-Massen", meT0, mmuT0)]:
    v = 7500/(a*b)
    print(f"{lab:12s}: m_e m_mu = {a*b:.5f}, 7500/.. = {v:.4f}, *0.9862 = {v*0.9862:.4f}, "
          f"*0.986 = {v*0.986:.4f}, *74/75 = {v*74/75:.4f}, *(1-100xi) = {v*(1-100*xi):.4f}")
print("138.93*0.9862 =", 138.93*0.9862, "; 138.949*0.9862 =", 138.949*0.9862,
      "; 138.91*0.986 =", 138.91*0.986)
print("benoetigtes K fuer 138.93 -> 137.036:", 137.036/138.93,
      "; fuer 138.911:", ainv/(7500/(me14*mmu14)))
print("K = 1-(D_f-2)/C: D_f=2.973,C=68.24:", 1-0.973/68.24, " gamma=0.94,C=68.24:", 1-0.94/68.24,
      " D_f=2.973,C=68:", 1-0.973/68)
print("Konstante fuer alpha = m_e m_mu / X mit alpha^-1=137.036: X =", ainv*0.511*105.658,
      "; 7500*0.9862 =", 7500*0.9862, "; 7500/0.9862 =", 7500/0.9862)
print("alpha = m_e m_mu/7380 -> alpha^-1 =", 7380/(0.511*105.658))
print("Box 11.6: alpha = m_e m_mu/7500 * 0.986 -> alpha^-1 =", 1/((0.511*105.658)/7500*0.986))
print("3.4.1: xi*7.398^2 =", xi*7.398**2, "-> 1/", 1/(xi*7.398**2))
pref = (27*sqrt(3)/(8*pi**2))
print("27sqrt3/(8pi^2) =", pref, "; ^0.4 =", pref**0.4, "; xi^2.2 =", xi**2.2)
print("23.6.1: 0.8327*xi^2.2 =", pref**0.4*xi**2.2, "(Dok: 7.292e-3); Dok-Zwischenwert 8.758e-9 ->",
      0.8327*8.758e-9)
print("3.6.1 mit K: ", pref**0.4*xi**2.2*0.9862)

h("070-2  m_mu/m_e")
print("CODATA2014 Verh.:", mmu14/me14, " CODATA2018:", mmu/me)
print("12/5 xi^-1/2 =", 12/5*xi**-0.5, " xi^-1/2 =", xi**-0.5,
      " Abweichung % =", (12/5*xi**-0.5/(mmu/me)-1)*100)
print("(64sqrt3/81)/(128/45) =", (64*sqrt(3)/81)/(128/45), "=5sqrt3/18*1e-2?", 5*sqrt(3)/18)
ce_n = 3*sqrt(3)/(2*pi*sqrt(alpha)); cmu_n = 9/(4*pi*alpha)
print("c_e(nat) =", ce_n, " c_mu(nat) =", cmu_n, " c_mu/c_e =", cmu_n/ce_n,
      " korrekt sqrt3/(2 sqrt a) =", sqrt(3)/(2*sqrt(alpha)), " Dok-Form 3sqrt3/(2sqrt a) =", 3*sqrt(3)/(2*sqrt(alpha)))
print("m_mu/m_e aus c_mu/c_e*xi^-1/2 =", cmu_n/ce_n*xi**-0.5, "; mit Dok-Form:", 3*sqrt(3)/(2*sqrt(alpha))*xi**-0.5)
print("Dok 13.7.1 mit alpha=1/137: c_e", 3*sqrt(3)/(2*pi*sqrt(1/137)), " c_mu", 9/(4*pi/137))

h("070-3  c_e = 1.6487e19 vs e bzw. sqrt(e)")
print("e =", e, " sqrt(e) =", sqrt(e))
print("c_e(nat) =", ce_n, " vs 1.6487e19; c_mu(nat) =", cmu_n, "vs 1.0262e20")
print("c_e*c_mu (Tabelle) =", 1.648721270700128e19*1.026187714072347e20, " benoetigt alpha/xi^5.5 =", alpha/xi**5.5,
      " xi^5.5 =", xi**5.5)
print("c_e(nat)*c_mu(nat) =", ce_n*cmu_n)

h("070-4  Massen als Rechenergebnis?")
print("xi^2.5 =", xi**2.5, " xi^2 =", xi**2, " xi^1.5 =", xi**1.5)
print("c_e(nat) xi^2.5 =", ce_n*xi**2.5, "; 1.6487e19*xi^2.5 =", 1.648721270700128e19*xi**2.5)
print("c_mu(nat) xi^2 =", cmu_n*xi**2, "; 1.0262e20*xi^2 =", 1.026187714072347e20*xi**2)
ctau_n = 27*sqrt(3)/(8*pi)*alpha**-1.5
print("c_tau(nat) =", ctau_n, " (Dok 6.1853e20); c_tau xi^1.5 =", ctau_n*xi**1.5)
print("m_e/xi^2.5 [MeV] =", me14/xi**2.5, " m_mu/xi^2 [MeV] =", mmu14/xi**2)
print("E0 = sqrt(T0-Massen) =", sqrt(meT0*mmuT0), " sqrt(CODATA14) =", sqrt(me14*mmu14))
print("4.2.3 tau: 5/4 xi^(2/3) *246 GeV =", 1.25*xi**(2/3)*246, "GeV ; 5/4 xi^(2/3) =", 1.25*xi**(2/3),
      " ; 1.777/246 GeV =", 1.777/246)

h("070-5  3pi * xi^-1 * ln(1e4) / D_f (nur En Z. 222-226)")
v = 3*pi*7500*log(1e4)/2.973
print("ln(1e4) =", log(1e4), " 1/2.973 =", 1/2.973, " 3pi*7500 =", 3*pi*7500, " Ergebnis =", v)
print("Dok-Zwischenschritt 9pi*1e4*9.21*0.340 =", 9*pi*1e4*9.21*0.340, " korrekt 3pi*3/4 = 9pi/4:", 9*pi/4)

h("077-1  c = 299792458 m/s (keine Rechnung; Beleg: 17. CGPM 1983)")
print("E = m c^2 fuer 1 kg:", c**2, "J")

h("081-1  alpha_S = xi^-1/3")
print("xi^-1/3 =", xi**(-1/3), " xi^-1/4 =", xi**-0.25, " xi^1/2 =", xi**0.5, " xi^2 =", xi**2)
print("Welche Groesse ergibt 9.65? 9.65^3 =", 9.65**3, " 9.65^4 =", 9.65**4)

h("081-2  10^38 vs xi^2")
aG_p = G*mp_kg**2/(hbar*c); aG_e = G*me_kg**2/(hbar*c)
print("alpha_G(Proton) =", aG_p, " alpha/alpha_G(p) =", alpha/aG_p)
print("alpha_G(Elektron) =", aG_e, " alpha/alpha_G(e) =", alpha/aG_e)
print("1/xi^2 =", 1/xi**2)
print("Coulomb/Grav fuer 2 Protonen =", e_ch**2/(4*pi*eps0)/(G*mp_kg**2))

h("081-3  G = xi^2 c^3/hbar (Dimension)")
print("xi^2 c^3/hbar [m kg^-1 s^-2 * ?] =", xi**2*c**3/hbar, " (G hat m^3 kg^-1 s^-2)")
L = sqrt(G*hbar/(xi**2*c**3))
print("benoetigte Laenge L mit G = xi^2 c^3 L^2/hbar: L =", L, " = l_P/xi =", lP/xi)
print("081 zus.: E_e = E_P xi^1.5 =", EP_MeV*xi**1.5, "MeV (vs m_e 0.511)")
print("m_tau/m_e =", mtau/me, "; 1776.82/0.5109989 =", 1776.82/me14)

h("105-1  c^2 ~ 1/(xi D_f)")
for Df in (3-xi, 2.99987, 2.973, 2.94):
    print(f"D_f={Df:.5f}: 1/(xi D_f) = {1/(xi*Df):.2f}, sqrt = {sqrt(1/(xi*Df)):.3f}")
print("c^2 SI =", c**2)

h("105-2  alpha = xi E0^2 vs xi (E0/m_e)^2")
E0 = sqrt(0.511*105.66)
print("E0 =", E0, " E0/m_e =", E0/0.511, " (E0/m_e)^2 =", (E0/0.511)**2)
print("xi (E0/m_e)^2 =", xi*(E0/0.511)**2, "-> 1/", 1/(xi*(E0/0.511)**2))
print("xi E0^2 (E0 in MeV) =", xi*E0**2, "-> 1/", 1/(xi*E0**2), "; mit 7.398:", 1/(xi*7.398**2))
print("xi*206.8 =", xi*206.8)
print("105 zus.: lambdabar_e/sqrt(alpha) =", hbar/(me_kg*c)/sqrt(alpha), "m vs l_P =", lP)
print("hbar c/(m_e^2 alpha) =", hbar*c/(me_kg**2*alpha), " vs G =", G, " Verh.", hbar*c/(me_kg**2*alpha)/G)

h("145-1  Viskositaet eta ~ hbar/(l_P^3 xi)")
eta = hbar/(lP**3*xi)
print("hbar/l_P^3 =", hbar/lP**3, "Pa s; /xi =", eta, "Pa s (Wasser ~1e-3)")
rhoP = mP/lP**3
print("kinematisch nu = eta/rho_P =", eta/rhoP, "m^2/s = l_P c /xi =", lP*c/xi)
print("in Planck-Einheiten: eta = 1/xi =", 1/xi)

h("145-2  Casimir-Vorzeichen")
for d in (1e-6, 1e-7):
    print(f"d={d}: P = -pi^2 hbar c/(240 d^4) =", -pi**2*hbar*c/(240*d**4), "Pa (negativ = anziehend)")

h("145-3  Dipolzahlen")
T0 = 2.7255
Dk = T0*370e3/c
print("D_kin = T0 v/c =", Dk*1e3, "mK (Dok 3.35); mit T0=2.725:", 2.725*370e3/c*1e3)
print("Planck gemessen: 3.3621 mK")
for H0 in (67.4, 66.2, 73.0):
    LH = c/(H0*1e3/3.0856776e22)
    Dg = xi*log(LH/lP)*T0
    print(f"H0={H0}: L_H={LH:.3e} m, ln(L_H/l_P)={log(LH/lP):.2f}, D_geo=xi ln .. T0 = {Dg*1e3:.2f} mK (Dok 0.1)")
for ang in (0, 48, 90):
    print(f"|3.35 + 0.1| bei {ang} Grad =", sqrt(3.35**2+0.1**2+2*3.35*0.1*cos(radians(ang))))

h("146-1  Turing")
tC_h = 6.62607015e-34/(mp_kg*c**2); tC_hb = hbar/(mp_kg*c**2)
print("Proton h/(m c^2) =", tC_h, " 1/.. =", 1/tC_h, "; hbar/(m c^2) =", tC_hb, " 1/.. =", 1/tC_hb)
print("lambda_C(e) =", 6.62607015e-34/(me_kg*c))

h("146-2  xi_crit")
print("100 xi^2 > 0.1 xi -> xi >", 0.1/100)
print("Fixpunkte von xi(1-100xi): xi = xi - 100 xi^2 -> nur xi*=0")
print("(1 - sqrt(1-4/100))/200 =", (1-sqrt(1-0.04))/200, " (1+sqrt)/200 =", (1+sqrt(1-0.04))/200)
x = 0.0101; x1 = x*(1-100*x)
print("Start 0.0101 -> naechster Wert", x1, "(negativ -> Divergenz)")
x = 0.009
for _ in range(3): x = x*(1-100*x)
print("Start 0.009 nach 3 Schritten:", x)
print("xi(10K) =", 1-2*(1/sqrt(10)-1/sqrt(300)), " alternative:", 1/sqrt(300/10))
print("log(7500)/log2 =", log(7500)/log(2))
print("\nSkript ohne Fehler durchgelaufen.")
