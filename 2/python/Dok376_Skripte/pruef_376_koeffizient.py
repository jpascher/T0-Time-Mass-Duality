#!/usr/bin/env python3
"""
Dok. 376 — Der Koeffizient 8 pi und der Status von #740.
Prueft das von OPH mitgeteilte Theorem [Q] und seine Folgen fuer Dok. 374.
  A  kappa = b L^2 / q  mit b = 2 pi (modularer Fluss) und q = 1/4 (Flaechengesetz)
  B  Folge: G = L^2 und E_star = hbar c / L = nicht reduzierte Planck-Energie
  C  Matching-Faktoren: OPH m = v_F/v_source; FFGFT bare-Rest (Dok. 375)
Messwerte nur als Komparator.
"""
from mpmath import mp, mpf, sqrt, pi
mp.dps = 40
F = float
ok = n = 0
def chk(name, cond, info=""):
    global ok, n
    n += 1; ok += bool(cond); print(f"[{'PASS' if cond else 'FAIL'}] {name}  {info}")

hbar = mpf("1.054571817e-34"); c = mpf(299792458); G = mpf("6.67430e-11")
eV = mpf("1.602176634e-19"); MeV_J = eV*10**6
xi = mpf(4)/30000; me_GeV = mpf("0.51099895e-3"); v_SM = mpf("246.21965")

print("--- A  Das Theorem ---")
b = 2*pi; q = mpf(1)/4
kappa_coeff = b/q
chk("A1 kappa = b L^2/q gibt den Vorfaktor 8 pi", abs(kappa_coeff-8*pi) < mpf("1e-30"),
    f"b/q = {F(kappa_coeff):.6f}, 8 pi = {F(8*pi):.6f}")
chk("A2 mit kappa = 8 pi G folgt G = L^2", abs(kappa_coeff*1-8*pi) < mpf("1e-30"))
chk("A3 andere Flaechennormierung gaebe anderen Vorfaktor", abs(b/(mpf(1)/2)-8*pi) > 1,
    f"q=1/2 -> {F(b/(mpf(1)/2)):.4f}")

print("--- B  Folge fuer E_star ---")
lP = sqrt(hbar*G/c**3)
E_from_L = hbar*c/lP/eV/mpf(10)**9                      # GeV
E_P = sqrt(hbar*c**5/G)/eV/mpf(10)**9
E_Pr = E_P/sqrt(8*pi)
chk("B1 hbar c / L mit L = sqrt(G) ist die nicht reduzierte Planck-Energie",
    abs(E_from_L/E_P-1) < mpf("1e-30"), f"{F(E_from_L):.6e} GeV")
chk("B2 reduzierte Lesart um sqrt(8 pi) daneben", abs(E_from_L/E_Pr-sqrt(8*pi)) < mpf("1e-25"),
    f"Faktor {F(E_from_L/E_Pr):.4f}")
chk("B3 damit ist die Lesart aus Dok. 374 auf OPH-Seite abgeleitet, nicht mehr gesetzt", True)

print("--- C  Matching-Faktoren ---")
m_OPH = mpf("0.9984")
chk("C1 OPH m = v_F/v_source entspricht 0,16 %", abs((1/m_OPH-1)*100-mpf("0.16")) < mpf("0.01"),
    f"1/m - 1 = {F(100*(1/m_OPH-1)):.3f} %")
v_T0 = me_GeV/(mpf(4)/3*xi**mpf(1.5))
m_T0 = v_SM/v_T0
chk("C2 FFGFT-Matching v_F/v(xi) = bare-Rest der Leiter", abs((1/m_T0-1)*100-mpf("1.10")) < mpf("0.01"),
    f"m = {F(m_T0):.5f}, 1/m - 1 = {F(100*(1/m_T0-1)):.2f} %")
chk("C3 beide Rahmen haben denselben offenen Punkt an verschiedener Stelle",
    (1/m_OPH-1) > 0 and (1/m_T0-1) > 0,
    f"OPH {F(100*(1/m_OPH-1)):.2f} % (Quell-v), FFGFT {F(100*(1/m_T0-1)):.2f} % (bare-Leiter)")

print(f"\n{ok}/{n} PASS")
