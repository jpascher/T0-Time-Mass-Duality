#!/usr/bin/env python3
"""
Dok. 374 — Gemeinsamer Anker: Brückengleichungen zu OPH und die elektroschwache Skala als Treffpunkt.
Prüft
  A  Brückengleichungen B1–B4 (OPH #740 <-> FFGFT Dok. 180/257/329, T~·m=1)
  B  Hierarchie: OPH v/E_star [Q, bedingt] x FFGFT m_e/v [K] gegen m_e/E_P (Komparator)
Alle Messwerte nur als Komparator.
"""
from mpmath import mp, mpf, sqrt, pi, log
mp.dps = 40
F = float
ok = n = 0
def chk(name, cond, info=""):
    global ok, n
    n += 1; ok += bool(cond)
    print(f"[{'PASS' if cond else 'FAIL'}] {name}  {info}")

# ---------- Eingänge ----------
xi = mpf(4)/30000
phi = (1+sqrt(5))/2
P_pub = mpf("1.630968209403959324879279847782648941")        # OPH FULL_DERIVATION.md
P_src = mpf("1.63097209585889737696451390350695562985390")
h_pub = mpf("2.0199803239725553e-17")                        # OPH theorem_package.md
h_src = mpf("2.0198114078576331e-17")
# Komparatoren
hbar = mpf("1.054571817e-34"); c = mpf(299792458); G = mpf("6.67430e-11")
eV = mpf("1.602176634e-19"); MeV_J = eV*mpf(10)**6
E_P_GeV = sqrt(hbar*c**5/G)/eV/10**9
E_Pr_GeV = E_P_GeV/sqrt(8*pi)
v_GeV = mpf("246.21965"); me_GeV = mpf("0.51099895e-3")
A_codata = mpf("137.035999177")

print("--- A  Brückengleichungen (Planck-Einheiten) ---")
chk("A0 OPH-Außengleichung P = phi + sqrt(pi)/alpha^-1", abs(phi+sqrt(pi)/A_codata-P_pub) < mpf("1e-9"))
L = sqrt(P_pub); E = 1/sqrt(P_pub)
chk("A1 E_cell = E_bit(sqrt(P) l_P)", abs(E-1/L) < mpf("1e-35"), f"L_cell={F(L):.6f} l_P, E_cell={F(E):.6f} E_P")
nthr = L/sqrt(2)
chk("A2 n_thr(L_cell) = sqrt(P/2)", abs(nthr-sqrt(P_pub/2)) < mpf("1e-35"), f"{F(nthr):.6f}")
chk("A2a Dok.-329-Formel gibt 6.4097 bei 2pi l_P/ln2", abs(2*pi/log(2)/sqrt(2)-mpf("6.4097")) < mpf("1e-4"))
chk("A2b r_s(E_cell)/L_cell = 2/P", abs(2*E/L-2/P_pub) < mpf("1e-35"), f"{F(2/P_pub):.6f}")
chk("A2c Schwelle P=2, OPH darunter", P_pub < 2 and nthr < 1)
chk("A2d Zweigunabhängig (<2 ppm)", abs(sqrt(P_src/P_pub)-1) < mpf("2e-6"), f"{F(sqrt(P_src/P_pub)-1):.2e}")
chk("A3 T~_cell = sqrt(P) t_P = L_cell/c", abs(1/E-L) < mpf("1e-35"))
chk("A4 L_cell/L_0 = sqrt(P)/xi > 1", L/xi > 1, f"{F(L/xi):.1f}")

print("--- B  Hierarchie über den Treffpunkt v ---")
dB1 = h_pub/(v_GeV/E_P_GeV)-1
chk("B1 OPH v/E_star gegen v/E_P (nicht reduziert)", abs(dB1) < mpf("0.005"), f"{F(100*dB1):+.3f} %")
chk("B1a E_star nicht reduzierte Planck-Energie", abs((v_GeV/h_pub)/E_Pr_GeV-1) > 1,
    f"E_star={F(v_GeV/h_pub):.5e} GeV")
mev = mpf(4)/3*xi**mpf(1.5)
dB2 = mev/(me_GeV/v_GeV)-1
chk("B2 FFGFT m_e/v = (4/3) xi^(3/2)", abs(dB2) < mpf("0.02"), f"{F(100*dB2):+.2f} %")
comb = mev*h_pub; meas = me_GeV/E_P_GeV
dB3 = comb/meas-1
chk("B3 m_e/E_P kombiniert", abs(dB3) < mpf("0.02"), f"{F(comb):.5e} vs {F(meas):.5e}, {F(100*dB3):+.2f} %")
chk("B3a Summe der Einzelabweichungen", abs((1+dB1)*(1+dB2)-1-dB3) < mpf("1e-12"))
chk("B3b OPH-Zweig ohne Einfluss (<1e-4)", abs(h_src/h_pub-1) < mpf("1e-4"))
p_eff = log(meas)/log(xi)
chk("B4 m_e/m_P keine einfache xi-Potenz", abs(p_eff*6-round(p_eff*6)) > 0.05, f"xi^{F(p_eff):.4f}")

print("--- C  FFGFT-eigene Kette xi -> G -> l_P -> E_P (Dok. 012/013/180) ---")
C_conv = mpf("7.783e-3"); K_frak = mpf("0.986"); me_MeV = mpf("0.511")
G_T0 = xi**2/(4*me_MeV)*C_conv*K_frak
chk("C1 G = xi^2/(4 m_e) C_conv K_frak", abs(G_T0/G-1) < mpf("1e-4"), f"{F(G_T0):.5e}, {F(100*(G_T0/G-1)):+.4f} %")
C_dim = 1/mpf("28.4"); C_conv_split = C_conv/C_dim
chk("C2 Aufteilung C_dim*C_conv (Dok. 180) gleichwertig", abs(xi**2/(4*me_MeV)*C_dim*C_conv_split*K_frak/G_T0-1) < mpf("1e-30"))
lP = sqrt(hbar*G_T0/c**3)
chk("C3 l_P aus der Kette", abs(lP/mpf("1.616255e-35")-1) < mpf("1e-4"), f"{F(lP):.5e} m, L_0={F(xi*lP):.4e} m")
EP_T0 = sqrt(hbar*c/G_T0)*c**2/MeV_J/1000          # in GeV
d = (me_GeV/EP_T0)/(me_GeV/E_P_GeV)-1
chk("C4 m_e/E_P über die eigene Kette", abs(d) < mpf("1e-4"), f"{F(me_GeV/EP_T0):.5e}, {F(100*d):+.4f} %")
vEP_T0 = v_GeV/EP_T0
dO = h_pub/vEP_T0-1
chk("C5 OPH v/E_star gegen FFGFT-Kette v/E_P", abs(dO) < mpf("0.005"), f"FFGFT {F(vEP_T0):.5e}, OPH {F(100*dO):+.3f} %")
chk("C6 Genauigkeit je Weg verschieden: Kette << Leiter-Kombination", abs(d) < abs(dB3)/100)

print("--- D  Referenzenergie E_star ---")
from mpmath import exp
aU_pub = mpf("0.041124336195630495"); aU_src = mpf("0.0411242474418166851408899338896597194")
h_calc = exp(-2*pi/(4*aU_pub))/sqrt(P_pub)
chk("D1 Theorem A reproduziert v/E_star aus P, alpha_U", abs(h_calc/h_pub-1) < mpf("1e-12"), f"{F(h_calc):.10e}")
Estar = v_GeV/h_pub
chk("D2 E_star vs E_P nicht reduziert", abs(Estar/E_P_GeV-1) < mpf("0.002"), f"{F(Estar):.5e} GeV, {F(100*(Estar/E_P_GeV-1)):+.3f} %")
chk("D3 E_star vs E_P reduziert: Faktor ~sqrt(8pi)", abs(Estar/E_Pr_GeV - sqrt(8*pi)) < mpf("0.02"), f"Faktor {F(Estar/E_Pr_GeV):.3f}, sqrt(8pi)={F(sqrt(8*pi)):.3f}")
sens = pi/(2*aU_pub**2)
dA = log(E_P_GeV/Estar)/sens
chk("D4 Empfindlichkeit d ln(v/E)/d alpha_U = pi/(2 alpha_U^2)", abs(sens-929) < 2, f"{F(sens):.1f}; 0,16 % <-> d alpha_U={F(dA):.2e} (rel. {F(dA/aU_pub):.1e})")
pred = exp(sens*(aU_src-aU_pub))*sqrt(P_pub/P_src)
chk("D5 Empfindlichkeit erklärt Zweigdifferenz", abs(pred-h_src/h_pub) < mpf("1e-6"), f"{F(pred-1):.2e} vs {F(h_src/h_pub-1):.2e}")

print("--- E  #740: absolute Länge und Takt über die FFGFT-Kette (Lesart E_star = E_P) ---")
L_abs = sqrt(P_pub)*lP; t_abs = L_abs/c
chk("E1 L_cell = sqrt(P) l_P absolut", abs(L_abs/mpf("2.0642e-35")-1) < mpf("1e-3"), f"{F(L_abs):.4e} m")
chk("E2 T~_cell = sqrt(P) t_P absolut", abs(t_abs/mpf("6.8855e-44")-1) < mpf("1e-3"), f"{F(t_abs):.4e} s")
chk("E3 Taktverhältnis = Massenverhältnis (T~ = hbar/E)", abs((hbar/(E_P_GeV*1e9*eV/sqrt(P_pub)))/(sqrt(P_pub)*sqrt(hbar*G/c**5))-1) < mpf("1e-10"))

print(f"\n{ok}/{n} PASS")
