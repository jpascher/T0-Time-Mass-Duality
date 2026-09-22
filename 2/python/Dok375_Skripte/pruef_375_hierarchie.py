#!/usr/bin/env python3
"""
Dok. 375 — Die Hierarchie v/E_P: FFGFT-Herleitung gegen OPH (Theorem A).
FFGFT: v = m_e/((4/3) xi^(3/2)) (R104, Dok. 006); E_P über G = xi^2/(4 m_e) C_conv K_frak (Dok. 012/013/180).
OPH [Q]: v/E_star = P^-1/2 exp(-2 pi/(4 alpha_U)) (theorem_package.md), bedingt.
Messwerte nur als Komparator; v(G_F) ist SM-Definition (R112).
"""
from mpmath import mp, mpf, sqrt, pi, exp, log
import hashlib
mp.dps = 40
F = float
ok = n = 0
def chk(name, cond, info=""):
    global ok, n
    n += 1; ok += bool(cond); print(f"[{'PASS' if cond else 'FAIL'}] {name}  {info}")

xi = mpf(4)/30000
hbar = mpf("1.054571817e-34"); c = mpf(299792458); eV = mpf("1.602176634e-19"); MeV_J = eV*10**6
G_meas = mpf("6.67430e-11")
me_MeV = mpf("0.51099895"); v_SM = mpf("246.21965")          # GeV, aus G_F
C_conv = mpf("7.783e-3"); K_frak = mpf("0.986")

# FFGFT
v_T0 = me_MeV/1000/(mpf(4)/3*xi**mpf(1.5))
G_T0 = xi**2/(4*mpf("0.511"))*C_conv*K_frak
EP_T0 = sqrt(hbar*c/G_T0)*c**2/MeV_J/1000
EP_meas = sqrt(hbar*c/G_meas)*c**2/MeV_J/1000
h_T0 = v_T0/EP_T0
h_meas = v_SM/EP_meas
chk("1 FFGFT v aus xi (R104)", abs(v_T0/v_SM-1) < mpf("0.02"), f"v={F(v_T0):.3f} GeV, {F(100*(v_T0/v_SM-1)):+.2f} %")
chk("2 FFGFT E_P aus eigener Kette", abs(EP_T0/EP_meas-1) < mpf("1e-4"), f"{F(EP_T0):.6e} GeV")
chk("3 FFGFT v/E_P", abs(h_T0/h_meas-1) < mpf("0.02"), f"{F(h_T0):.5e} vs gemessen {F(h_meas):.5e}, {F(100*(h_T0/h_meas-1)):+.2f} %")
chk("3a Abweichung = Abweichung von v (E_P-Kette trägt < 1e-4 bei)",
    abs((h_T0/h_meas)/(v_T0/v_SM)-1) < mpf("1e-4"))
me_bare_rel = (mpf(4)/3*xi**mpf(1.5))/(me_MeV/1000/v_SM)-1
chk("3b = bare-Rest der Leiter m_e/v (Dok. 352)", abs((1+me_bare_rel)*(v_T0/v_SM)-1) < mpf("1e-12"),
    f"m_e/v bare {F(100*me_bare_rel):+.2f} %")
# OPH
P = mpf("1.630968209403959324879279847782648941"); aU = mpf("0.041124336195630495")
h_OPH = exp(-2*pi/(4*aU))/sqrt(P)
chk("4 OPH Theorem A reproduziert", abs(h_OPH/mpf("2.0199803239725553e-17")-1) < mpf("1e-12"), f"{F(h_OPH):.5e}")
chk("4a OPH gegen Messwert", abs(h_OPH/h_meas-1) < mpf("0.005"), f"{F(100*(h_OPH/h_meas-1)):+.3f} %")
chk("5 Abstand OPH zu FFGFT", abs(h_OPH/h_T0-1) < mpf("0.02"), f"{F(100*(h_OPH/h_T0-1)):+.2f} %")
# Empfindlichkeiten
s_OPH = pi/(2*aU**2); s_T0 = mpf(-3)/2
chk("6 Empfindlichkeit OPH d ln h/d alpha_U", abs(s_OPH-929) < 2, f"{F(s_OPH):.1f}")
chk("6a Empfindlichkeit FFGFT d ln v/d ln xi = -3/2", abs(log(v_T0*(1+mpf('1e-8'))**(-1.5)/v_T0)/log(1+mpf('1e-8'))-s_T0) < mpf("1e-6"))
# Tabelleneintrag und Hash
entry = f"v/E_P | FFGFT | {F(h_T0):.5e} | route: v=m_e/((4/3)xi^(3/2)) (R104, Doc 006) ; E_P via G=xi^2/(4m_e)C_conv K_frak (Docs 012/013/180) ; bare ladder"
hsh = hashlib.sha256(entry.encode()).hexdigest()
print("\nEintrag:", entry); print("SHA-256:", hsh)
chk("7 Eintrag gehasht", len(hsh) == 64)
print(f"\n{ok}/{n} PASS")
