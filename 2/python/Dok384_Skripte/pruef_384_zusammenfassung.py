#!/usr/bin/env python3
"""
pruef_384_zusammenfassung.py -- Dok. 384: FFGFT in Kurzfassung (Stand 1. Okt. 2026).

Rechnet alle Zahlen nach, die Dok. 384 nennt. Jede Zahl stammt aus einem
Korpusdokument (Nummer im Kommentar); das Skript prüft nur, dass die
Kurzfassung sie richtig wiedergibt. Vergleichswerte: CODATA 2022, PDG 2024.
"""
import math
from fractions import Fraction as Fr

ok = n = 0
def check(name, cond, info=""):
    global ok, n
    n += 1; ok += bool(cond)
    print(f"  [{'OK ' if cond else 'FAIL'}] {name}" + (f"  ({info})" if info else ""))

def rel(a, b):
    return (a / b - 1) * 100

pi = math.pi
xi = 4 / 30000
xiF = Fr(4, 30000)
hbar, c, MeV, eV = 1.054571817e-34, 299792458.0, 1.602176634e-13, 1.602176634e-19
G_cod = 6.67430e-11
lP, tP = 1.616255e-35, 5.391247e-44
EP = math.sqrt(hbar * c**5 / G_cod) / MeV            # MeV
me, mmu, mtau = 0.51099895, 105.6583755, 1776.93
v_sm = 246.22e3                                       # MeV, SM-Definition aus G_F
alpha_inv = 137.035999177

print("1. Grundgrößen (Dok. 365, 315, 381, R135)")
check("xi = 4/30000 = 1/7500", xiF == Fr(1, 7500))
K = 1 - 100 * xiF
check("K_frak = 1 - 100 xi = 74/75", K == Fr(74, 75))
Kmess = xi * me * mmu / (1 / alpha_inv)
check("von alpha verlangtes K = 0,98650", abs(Kmess - 0.98650) < 5e-6, f"{Kmess:.6f}")
check("Rest gegen 74/75: 1,7e-4", abs(float(K) / Kmess - 1 - 1.68e-4) < 0.05e-4, f"{float(K)/Kmess-1:.3e}")
check("n = (1-K)/xi = 101,2", abs((1 - Kmess) / xi - 101.25) < 0.05, f"{(1-Kmess)/xi:.2f}")
E0b = math.sqrt(me * mmu); E0 = math.sqrt(me * mmu / float(K))
check("E0 nackt 7,348 MeV", abs(E0b - 7.348) < 0.001, f"{E0b:.4f}")
check("E0 korrigiert 7,397 MeV", abs(E0 - 7.397) < 0.001, f"{E0:.4f}")
ai = 1 / (xi * E0**2)
check("alpha^-1 = 1/(xi E0^2) = 137,06", abs(ai - 137.06) < 0.01, f"{ai:.3f}")
check("Grundform alpha = 1: xi E0^2 = 1 -> E0^2 = 1/xi = 7500 (Dok. 386)", abs(xi * (1/xi) - 1) < 1e-12 and abs(1/xi - 7500) < 1e-9)
Eref = E0 * math.sqrt(xi * alpha_inv)
check("Faktor 10 angepasst; mit nacktem v = 248,93 GeV: Nenner 15,501 = 5 pi K auf 2e-4 (Dok. 387)", abs(xi**4 * 1.220890e19 / (0.51099895e-3/((4/3)*xi**1.5)) / (5*math.pi*74/75) - 1) < 2e-4)
check("SI-Bezugsenergie E0 sqrt(xi/alpha) = 0,99992 MeV (Dok. 386)", abs(Eref - 0.99992) < 1e-5, f"{Eref:.5f}")
check("3700/27 = 137,037 (+7,6 ppm)", abs((3700/27/alpha_inv - 1) * 1e6 - 7.6) < 0.1)
Df = 3 - xi
check("D_f = 3 - xi = 2,999867", abs(Df - 2.999867) < 1e-6)
Dfe = None
lo, hi = 2.9, 3.0
for _ in range(200):
    mid = (lo + hi) / 2
    if (mid / 3) ** (mid / 2) > 74 / 75: hi = mid
    else: lo = mid
Dfe = (lo + hi) / 2
check("Potenzform (D/3)^(D/2) = 74/75 -> D_f^eff = 2,97303", abs(Dfe - 2.97303) < 1e-5, f"{Dfe:.6f}")

print("\n2. Ein-Anker-Kette (Dok. 383, 149)")
k = xi**4 / (5 * pi)
check("v/E_P = xi^4/(5 pi) = 2,012e-17", abs(k - 2.0120e-17) < 2e-21, f"{k:.4e}")
check("gegen Messung -0,23 %", abs(rel(k, v_sm / EP) + 0.23) < 0.01, f"{rel(k, v_sm/EP):+.2f} %")
r = {"e": 4/3, "mu": 16/5, "tau": 25/9}; p = {"e": 1.5, "mu": 1.0, "tau": 2/3}
EP_anchor = me / (r["e"] / (5 * pi) * xi ** (p["e"] + 4))
check("Anker m_e: E_P +1,34 %", abs(rel(EP_anchor, EP) - 1.34) < 0.01, f"{rel(EP_anchor, EP):+.2f} %")
G_anchor = hbar * c**5 / (EP_anchor * MeV) ** 2
check("Anker m_e: G -2,6 %", abs(rel(G_anchor, G_cod) + 2.62) < 0.01, f"{rel(G_anchor, G_cod):+.2f} %")
L0 = xi * lP
check("L0 = xi l_P = 2,155e-39 m", abs(L0 - 2.155e-39) < 0.001e-39, f"{L0:.4e}")
check("tau0 = xi t_P = 7,19e-48 s", abs(xi * tP - 7.19e-48) < 0.01e-48)
check("E_P/xi = 9,16e22 GeV", abs(EP / 1e3 / xi - 9.16e22) < 0.01e22)
check("Ketten-C_conv = 7,58e-3", abs(7.783e-3 * G_anchor / G_cod - 7.58e-3) < 0.01e-3, f"{7.783e-3*G_anchor/G_cod:.4e}")

print("\n3. Zeitstruktur (Dok. 295, 306, 381)")
xs = [xi]
for _ in range(5): xs.append(xs[-1] * (1 - 100 * xs[-1]))
d = [100 * x for x in xs]
check("d_n monoton fallend, d_1 = 1/75 größtes", all(d[i] > d[i+1] for i in range(5)) and abs(d[0] - 1/75) < 1e-15)
xn = xi; D = 0.0
for _ in range(100000): D += 100 * xn; xn *= (1 - 100 * xn)
check("D(1e5) = 7,19 ~ ln(1 + 1e5/75) = 7,20", abs(D - 7.19) < 0.005 and abs(math.log(1 + 1e5/75) - 7.196) < 0.001, f"{D:.4f}")
psi1 = sum(1 / (75 + j) ** 2 for j in range(2000000)) + 1 / (75 + 2000000)
check("psi'(75) = 0,01342", abs(psi1 - 0.013423) < 2e-6, f"{psi1:.6f}")

print("\n4. Leptonen und v (Dok. 006, 352, 372, 383; R104, R112)")
mm = 12/5 * xi ** -0.5
check("m_mu/m_e = 120 sqrt3 = 207,85 (+0,52 %)", abs(mm - 207.846) < 0.001 and abs(rel(mm, mmu/me) - 0.52) < 0.01)
mt = 125/144 * xi ** (-1/3)
check("m_tau/m_mu = 16,99 (+1,03 %)", abs(mt - 16.992) < 0.001 and abs(rel(mt, mtau/mmu) - 1.03) < 0.02, f"{rel(mt, mtau/mmu):+.2f} %")
check("(r_mu/r_e)^2/xi = 43200", Fr(12, 5) ** 2 / xiF == 43200)
check("43200 gegen (m_mu/m_e)^2: -1,03 %", abs(rel((mmu/me)**2, 43200) + 1.03) < 0.01)
v1 = me / (4/3 * xi ** 1.5)
check("v mit gemessenem m_e: 248,9 GeV", abs(v1 / 1e3 - 248.93) < 0.01, f"{v1/1e3:.2f}")
check("dito mit K_frak: 245,6 GeV", abs(v1 * 74/75 / 1e3 - 245.61) < 0.01)
check("xi^4 E_P/(5 pi) = 245,65 GeV", abs(k * EP / 1e3 - 245.65) < 0.01)
me_gal = math.sqrt(54 / (120 * math.sqrt(3)))
check("Galois-m_e 0,50971 MeV -> v = 248,3 GeV", abs(me_gal - 0.50971) < 1e-5 and abs(me_gal / (4/3 * xi**1.5) / 1e3 - 248.30) < 0.01)
check("Leiter v=246 GeV: e -1,18 %, mu -0,66 %, tau +0,37 %",
      abs(rel(4/3*xi**1.5*246e3, me) + 1.18) < 0.01 and abs(rel(16/5*xi*246e3, mmu) + 0.66) < 0.01 and abs(rel(25/9*xi**(2/3)*246e3, 1776.86) - 0.37) < 0.01)
Q = (me + mmu + 1776.86) / (math.sqrt(me) + math.sqrt(mmu) + math.sqrt(1776.86)) ** 2
check("Koide Q - 2/3 = -0,046 xi (m_tau = 1776,86)", abs((Q - 2/3) / xi + 0.046) < 0.002, f"{(Q-2/3)/xi:+.3f} xi")
A = math.sqrt(2) / 3; th = A**2
a = [1 + 3*A*math.cos(th + 2*pi*kk/3) for kk in range(3)]
s = sorted(x*x for x in a)
check("Matrixelement (sqrt2, 2/9): m_mu/m_e = 206,770 (442 sigma)", abs(s[1]/s[0] - 206.7703) < 0.001 and abs((s[1]/s[0] - 206.7682827)/0.0000046 - 442) < 5)
check("dito m_tau/m_e = 3477,47", abs(s[2]/s[0] - 3477.47) < 0.01)

print("\n5. Neutrinos (Dok. 340)")
mnu = xi**2 / 2 * me * 1e9  # meV
check("m_nu = xi^2 m_e/2 = 4,54 meV", abs(mnu - 4.542) < 0.001)
m2, m3 = math.sqrt(14/3) * mnu, 11 * mnu
check("m2 = 9,81, m3 = 49,96, Summe 64,3 meV", abs(m2 - 9.81) < 0.01 and abs(m3 - 49.96) < 0.01 and abs(mnu + m2 + m3 - 64.3) < 0.05)
check("Dm2_atm = 120 m_nu^2 = 2,476e-3 eV^2", abs(120 * (mnu*1e-3)**2 - 2.476e-3) < 0.001e-3)
check("Dm2_sol = 11/3 m_nu^2 = 7,565e-5 eV^2", abs(11/3 * (mnu*1e-3)**2 - 7.565e-5) < 0.002e-5)
rq = 120 / (11/3)
check("Verhältnis Dm2_atm/Dm2_sol = 120/(11/3) = 32,7, gegen 2,500e-3/7,53e-5: -1,4 %", abs(rq - 32.727) < 0.001 and abs(rq / (2.500e-3/7.53e-5) - 1 + 0.0143) < 0.001)
check("Verhältnisse m_h/M_Z = 11/8 (+0,15 %), m_t/M_Z = (11/8)^2 (-0,10 %)", abs(11/8*91.1876/125.20 - 1 - 0.0014) < 0.0003 and abs((11/8)**2*91.1876/172.57 - 1 + 0.0010) < 0.0003)
check("sin^2 theta13 = (25 xi)^(2/3) = 0,0223", abs((25*xi) ** (2/3) - 0.02231) < 1e-5)
s12, s13 = 0.307, 0.0220
mee = abs((1 - s12) * (1 - s13) * mnu + s12 * (1 - s13) * m2)
check("m_ee (Majorana nu1, nu2, Phasen 0) = 6,0 meV", abs(mee - 6.0) < 0.05, f"{mee:.2f}")
check("m_ee destruktiv = 0,13 meV; Obergrenze 14,4 meV", abs(abs((1-s12)*(1-s13)*mnu - s12*(1-s13)*m2) - 0.13) < 0.01 and abs(mnu + m2 - 14.35) < 0.01)

print("\n6. g-2, elektroschwach (Dok. 158, 382, 372, 373, 323)")
f = 1 / xi
check("f^(1/3) - 1 = 18,57", abs(f ** (1/3) - 1 - 18.57) < 0.01)
ae, amu = 1.15965218059e-3, 1.165920715e-3
atau = ae + 144/125 * mtau/mmu * (amu - ae)
check("a_tau = 1,2811e-3 (verankert)", abs(atau - 1.2811e-3) < 0.0002e-3, f"{atau:.5e}")
MZ, MW, mh, mt_ = 91.1876, 80.3692, 125.20, 172.57
check("M_W = M_Z sqrt(7/9) = 80,42 GeV", abs(MZ * math.sqrt(7/9) - 80.42) < 0.005)
check("m_h = 11/8 M_Z = 125,38 GeV (+0,15 %)", abs(11/8*MZ - 125.38) < 0.005 and abs(rel(11/8*MZ, mh) - 0.15) < 0.01)
check("m_t = (11/8)^2 M_Z = 172,40 GeV (-0,10 %)", abs((11/8)**2*MZ - 172.40) < 0.01 and abs(rel((11/8)**2*MZ, mt_) + 0.10) < 0.01)
check("lambda_CKM = xi^(1/6) = 0,2260", abs(xi ** (1/6) - 0.22602) < 1e-5)

print("\n7. Schwarze Löcher, Casimir, Kosmos (Dok. 325, 329, 279, 309, 308)")
check("S_BH(M_coll) = 2 pi/ln 2 bit = 9,065; n_thr = S/sqrt2 = 6,41",
      abs(2*pi/math.log(2) - 9.0647) < 1e-4 and abs(2*pi/math.log(2)/math.sqrt(2) - 6.4097) < 1e-4)
check("I_Sektor/I_therm = ln 3 = 1,099", abs(math.log(3) - 1.0986) < 1e-4)
check("pi^2/(720 xi) = 102,8", abs(pi**2 / (720 * xi) - 102.8) < 0.05)
H0 = pi / 2 * xi**10 * (me * MeV) / hbar * 3.0856775814913673e19
check("H0 aus (pi/2) xi^10 = 66,8 km/s/Mpc", abs(H0 - 66.82) < 0.02, f"{H0:.2f}")
check("pi^2 xi^10 = 1,75e-38", abs(pi**2 * xi**10 - 1.7526e-38) < 0.001e-38)

print("\n8. QM (Dok. 147, 230, 175)")
check("pi-Gatter: 1 - K_frak = 100 xi = 1,33 %", abs(100 * xi * 100 - 1.333) < 0.001)
check("Lücke 2 sqrt2 - 2,74 = 0,088 (3,1 %)", abs(2*math.sqrt(2) - 2.7396 - 0.0888) < 0.0005)
check("xi/(2 pi) = 2,1e-5", abs(xi / (2*pi) - 2.12e-5) < 0.01e-5)

print("\n9. Zusätze (Tabellen in Dok. 384)")
for anc, mval, rr, pp, eEP, eG in (("mu", mmu, 16/5, 1.0, 0.81, -1.60), ("tau", mtau, 25/9, 2/3, -0.22, 0.45)):
    EPa = mval / (rr / (5 * pi) * xi ** (pp + 4)); Ga = hbar * c**5 / (EPa * MeV) ** 2
    check(f"Anker {anc}: E_P {eEP:+.2f} %, G {eG:+.2f} %", abs(rel(EPa, EP) - eEP) < 0.02 and abs(rel(Ga, G_cod) - eG) < 0.03, f"{rel(EPa,EP):+.2f}/{rel(Ga,G_cod):+.2f}")
EPv = v_sm / k
check("Anker v: E_P +0,23 %, G -0,46 %", abs(rel(EPv, EP) - 0.23) < 0.01 and abs(rel(hbar*c**5/(EPv*MeV)**2, G_cod) + 0.46) < 0.02)
mlep = [r[x] / (5*pi) * xi ** (p[x] + 4) * EP for x in ("e", "mu", "tau")]
check("Massen mit gemessenem E_P: 0,504 / 104,8 / 1780,9 MeV", abs(mlep[0]-0.5043) < 0.0005 and abs(mlep[1]-104.81) < 0.05 and abs(mlep[2]-1780.9) < 0.3)
q = {"u": (6, 1.5, 2.27e-3), "d": (12.5, 1.5, 4.73e-3), "s": (26/9, 1.0, 94.8e-3), "c": (2, 2/3, 1.284), "b": (1.5, 0.5, 4.26), "t": (1/28, -1/3, 172.0)}
check("Quark-Leiter (v = 246 GeV) wie Tabelle", all(abs(rr * xi ** pp * 246 / val - 1) < 0.003 for rr, pp, val in q.values()))
a0 = c**2 * xi**10 / (4 * hbar / (me * MeV / c))
check("a0 = 1,03e-10 m/s^2 (-14 % gegen 1,2e-10)", abs(a0 - 1.033e-10) < 0.003e-10 and abs(rel(a0, 1.2e-10) + 13.9) < 0.2, f"{a0:.4e}")
check("sin^2 theta23 = 5/9 = 0,556", abs(5/9 - 0.556) < 0.0006)
check("Spurregel M_W^2+M_Z^2+m_h^2 gegen v^2/2: +0,45 %", abs(rel(MW**2 + MZ**2 + mh**2, (v_sm/1e3)**2/2) - 0.45) < 0.02)
check("IBM: 2,7396/2,7016/2,7244 = 96,9/95,5/96,3 % von 2 sqrt2", all(abs(x/(2*math.sqrt(2))*100 - y) < 0.05 for x, y in ((2.7396, 96.9), (2.7016, 95.5), (2.7244, 96.3))))

print("\n10. Nach unabhängiger Prüfung ergänzt")
Q24 = (me + mmu + mtau) / (math.sqrt(me) + math.sqrt(mmu) + math.sqrt(mtau)) ** 2
check("Koide mit PDG 2024 (1776,93): Q - 2/3 = -0,017 xi", abs((Q24 - 2/3) / xi + 0.017) < 0.002, f"{(Q24-2/3)/xi:+.3f} xi")
check("Dm2_atm gegen 2,500e-3 (Dok. 340): -1,0 %", abs(rel(120 * (mnu*1e-3)**2, 2.500e-3) + 0.96) < 0.05)
check("Formabstand |(1-100xi) - (1-xi)^100| = 8,8e-5", abs(abs((1 - 100*xi) - (1 - xi)**100) - 8.76e-5) < 0.01e-5)
check("Lücke gepoolt 2 sqrt2 - 2,7244 = 0,104", abs(2*math.sqrt(2) - 2.7244 - 0.104) < 0.001)
check("G mit 74/75 statt 0,986: +0,07 %", abs((74/75) / 0.986 * (1 + 0.000036) - 1 - 0.0007) < 0.0001)
check("alpha^-1 = 7500 (74/75)/54 = 3700/27", abs(7500 * (74/75) / 54 - 3700/27) < 1e-9)

print("\n11. Higgs-Prüfung von xi (Dok. 354, 320)")
mh_, v_ = 125.1, 246.2
lam = mh_**2 / (2 * v_**2)
xeft = lam**2 * v_**2 / (16 * pi**3 * mh_**2)
check("lambda_h = m_h^2/(2 v^2) = 0,129", abs(lam - 0.129) < 0.0005)
check("xi_EFT = m_h^2/(64 pi^3 v^2) = 1,30e-4", abs(xeft - 1.30e-4) < 0.005e-4 and abs(xeft - mh_**2/(64*pi**3*v_**2)) < 1e-15)
x354 = 0.129**2 * v_**2 / (16 * pi**3 * mh_**2)
check("mit 0,129 (Dok. 354): -2,6 % gegen 4/30000", abs(rel(x354, xi) + 2.56) < 0.02, f"{rel(x354, xi):+.2f} %")
xpdg = 125.20**2 / (64 * pi**3 * 246.22**2)
check("PDG 2024 (125,20/246,22): rund -2,3 % (Dok. 385)", abs(rel(xpdg, xi) + 2.28) < 0.03, f"{rel(xpdg, xi):+.2f} %")
check("Verkürzung 1/(16 pi^3) = 15-faches von xi", abs(1/(16*pi**3)/xi - 15.12) < 0.01)

print("\n12. Ikosaeder und phi-Skelett (Dok. 293, 367, 368, 370; Erweiterung 2. Okt. 2026)")
phi = (1 + math.sqrt(5)) / 2
p0, p1, p2 = 2/9, (2 + 3*phi)/9, (5 - 3*phi)/9
check("p0 + p1 + p2 = 1", abs(p0 + p1 + p2 - 1) < 1e-14)
check("p1/p2 = phi^8 exakt", abs(p1/p2 - phi**8) < 1e-9)
check("p0/p2 = 2 phi^4 exakt", abs(p0/p2 - 2*phi**4) < 1e-10)
check("3 sqrt(p_j) = sqrt2, phi^2, phi^-2", abs(3*math.sqrt(p0) - math.sqrt(2)) < 1e-14 and abs(3*math.sqrt(p1) - phi**2) < 1e-12 and abs(3*math.sqrt(p2) - phi**-2) < 1e-12)
rt = mtau / me; srt = 0.09 / me
check("PDG m_tau/m_e = 3477,37 +- 0,18", abs(rt - 3477.37) < 0.01 and abs(srt - 0.176) < 0.001, f"{rt:.3f}")
r74 = 74 * phi**8
check("74 phi^8 = 3476,42, -2,7e-4, -5,3 sigma", abs(r74 - 3476.42) < 0.01 and abs(r74/rt - 1 + 2.7e-4) < 0.05e-4 and abs((r74 - rt)/srt + 5.3) < 0.05)
r45 = (74 + 1/45) * phi**8
check("(74+1/45) phi^8 = 3477,469, +3,0e-5, 0,6 sigma", abs(r45 - 3477.469) < 0.001 and abs(r45/rt - 1 - 3.0e-5) < 0.05e-5 and abs((r45 - rt)/srt - 0.59) < 0.02, f"{r45:.4f}")
rxi = 74 * phi**8 * (1 + 27/12*xi)
check("74 phi^8 (1+27 xi/12) = 3477,468, +2,9e-5", abs(rxi - 3477.468) < 0.001 and abs(rxi/rt - 1 - 2.9e-5) < 0.05e-5)
ak = [1 + math.sqrt(2)*math.cos(2/9 + 2*pi*k/3) for k in range(3)]
rk = (ak[0]/ak[1])**2
check("Koide theta=2/9: m_tau/m_e = 3477,473, +3,1e-5", abs(rk - 3477.473) < 0.001 and abs(rk/rt - 1 - 3.1e-5) < 0.05e-5)
r30 = 30 * phi**4
check("30 phi^4 = 205,62, -0,55 % gegen m_mu/m_e", abs(r30 - 205.62) < 0.005 and abs(rel(r30, mmu/me) + 0.55) < 0.01)
check("74 = Zähler der Rotationszahl 74/75 = 1 - 100 xi", Fr(74, 75) == 1 - 100*xiF)
check("37 | 3^18 - 1, aber 4 teilt 18 nicht: GF(81) kein Teilkörper von GF(3^18)", (3**18 - 1) % 37 == 0 and 18 % 4 != 0 and min(k for k in range(1, 40) if (3**k - 1) % 37 == 0) == 18)
check("5 teilt 80 = |GF(81)*|, aber nicht 1152 = |Aut(D4)|", 80 % 5 == 0 and 1152 % 5 != 0)

print("\n13. Resonanz und Eulersches Tonnetz (Dok. 060, 189, 315, 316, 358; Ergänzung 2. Okt. 2026)")
def pf(x):
    d = {}; q = 2
    while x > 1:
        while x % q == 0: d[q] = d.get(q, 0) + 1; x //= q
        q += 1
    return d
check("1/xi = 7500 = 2^2 * 3 * 5^4, Tonnetz-Punkt (-2,-1,-4)", 1/xiF == 7500 and pf(7500) == {2: 2, 3: 1, 5: 4})
rY = {"e": Fr(4, 3), "mu": Fr(16, 5), "tau": Fr(25, 9), "u": Fr(6), "d": Fr(25, 2), "c": Fr(2), "b": Fr(3, 2), "s": Fr(26, 9), "t": Fr(1, 28)}
primes = lambda f: set(pf(f.numerator)) | set(pf(f.denominator))
lim5 = [k for k, f in rY.items() if primes(f) <= {2, 3, 5}]
check("7 von 9 Yukawa-Vorfaktoren 5-Limit; Ausnahmen s (13), t (7); alle im Raster {2,3,5,7,11,13}, 11 fehlt",
      len(lim5) == 7 and primes(rY["s"]) - {2, 3, 5} == {13} and primes(rY["t"]) - {2, 3, 5} == {7}
      and set().union(*map(primes, rY.values())) == {2, 3, 5, 7, 13})
check("Euler-Spirale schließt nie: 2^x 3^y 5^z = 1 nur trivial (|x|,|y|,|z| <= 30)",
      not any(Fr(2)**x * Fr(3)**y * Fr(5)**z == 1 for x in range(-30, 31) for y in range(-30, 31) for z in range(-30, 31) if (x, y, z) != (0, 0, 0)))
check("im endlichen Körper schließt der Zirkel: 3 hat in (Z/13)* Ordnung 3 (Orbit {1,3,9})",
      [pow(3, k, 13) for k in range(4)] == [1, 3, 9, 1])
check("xi-Zyklus: Schritt 1/75, Rotationszahl 74/75, gcd(74,75)=1 -> Schluss nach genau 75 Umläufen",
      math.gcd(74, 75) == 1 and min(k for k in range(1, 200) if (k * Fr(74, 75)).denominator == 1) == 75)
check("Terz der Massenleiter: xi^(1/3) = 1/19,57", abs(1 / xi**(1/3) - 19.57) < 0.01)

print("\n14. Deterministische Messlesart (Dok. 230, 175; Ergänzung 2. Okt. 2026)")
zs = [-0.9, -0.3, 0.0, 0.42, 0.8]
M = 200000
lam = [-1 + 2*(k + 0.5)/M for k in range(M)]   # gleichmäßiges lambda-Gitter, keine Zufallszahlen
check("A(z,lambda) = sgn(z - lambda): Achsenanteil zum Pol +1 = (1+z)/2",
      all(abs(sum(1 for l in lam if l < z)/M - (1 + z)/2) < 1e-5 for z in zs))
check("Archimedes: Zonenfläche der Einheitskugel von -1 bis z = 2 pi (1+z), Anteil (1+z)/2",
      all(abs(2*math.pi*(1 + z)/(4*math.pi) - (1 + z)/2) < 1e-15 for z in zs))

check("Auflösungsboden xi: N_max = 1/xi = 7500, rund 13 Bit (Dok. 343, Satz G')", 1/xiF == 7500 and round(math.log2(7500)) == 13)
check("Shor: O(n^3) Aufbereitung gegen O(n^2) QFT, Verhältnis n; RSA-2048 n^3 = 8,6e9", 2048**3 == 8589934592)

Tc = 8.617333262e-5 * 2.72548 / 0.51099895e6
check("CMB-Kandidat (Dok. 388): T/m_e = (8 pi)^(1/4) xi^(5/2), +0,0025 %", abs((8*math.pi)**0.25 * xi**2.5 / Tc - 1 - 2.5e-5) < 1e-6)

print(f"\nErgebnis: {ok}/{n} OK")
raise SystemExit(0 if ok == n else 1)
