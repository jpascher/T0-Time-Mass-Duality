#!/usr/bin/env python3
"""Rechenprüfung Gruppe D: Dok. 033, 041, 046, 059 — wörtlich, mit Umrechnung, Korpusfassung."""
import math

xi = 4 / 30000
me, mmu, mtau = 0.51099895, 105.6583755, 1776.86      # MeV
eV_K = 11604.518                                       # K je eV
TP, EP_eV = 1.41678e32, 1.22089e28                     # K, eV

print("033-1 Myonmasse als geometrisches Mittel")
print("  sqrt(0.511*1777)            =", math.sqrt(0.511 * 1777), "MeV")
print("  Einheitenwechsel k=1e3 (keV): sqrt(k me * k mtau)/k =", math.sqrt(1e3 * me * 1e3 * mtau) / 1e3, "MeV (gleich)")
print("  (ln me + ln mtau)/2 -> exp  =", math.exp((math.log(me) + math.log(mtau)) / 2))
print("  E0 = sqrt(me*mmu)           =", math.sqrt(me * mmu))
print("  Exponenten 3/2,1,2/3: Mittel (3/2+2/3)/2 =", (1.5 + 2 / 3) / 2, "(nicht 1)")

R1 = 12 / 5 * xi ** -0.5; R2 = 125 / 144 * xi ** (-1 / 3)
F = math.sqrt(R1 / R2)
print("  Leptonleiter ohne v: m_mu/m_e =", R1, " m_tau/m_mu =", R2)
print("  Faktor sqrt(R1/R2) =", F, "= 24 sqrt3/25 xi^-1/12 =", 24 * math.sqrt(3) / 25 * xi ** (-1 / 12))
print("  m_mu = F*sqrt(me*mtau) =", F * math.sqrt(me * mtau), "MeV, Abw.", (F * math.sqrt(me * mtau) / mmu - 1) * 100, "%")
print("  nur aus m_e:", me * R1, " nur aus m_tau:", mtau / R2)
print("\n033-2 alpha aus E0 = 7,35")
for E0 in (7.35, math.sqrt(me * mmu), 7.398):
    a = xi * E0 ** 2
    print(f"  E0={E0:.4f}: xi*E0^2 = {a:.6e}, 1/alpha = {1/a:.3f}")
print("  1/7.201e-3 =", 1 / 7.201e-3)

print("\n033-3 CMB-Temperatur")
print("  xi*TP/7.398                 =", xi * 1.416e32 / 7.398, "K")
print("  xi*EP/7.398 (eV, rein)      =", xi * EP_eV / 7.398)
print("  2.552/2.725                 =", 2.552 / 2.725)
Tn = 16 / 9 * xi ** 2 * 7500
print("  Korpus (16/9) xi^2 E_xi     =", Tn, "eV ->", Tn * eV_K, "K; Abw.", (Tn * eV_K / 2.72548 - 1) * 100, "%")

print("\n033-4 D_f")
print("  log xi / log 10             =", math.log(xi) / math.log(10))
print("  3 - 200 xi                  =", 3 - 200 * xi)
print("  (2.973/3)^(2.973/2)         =", (2.973 / 3) ** (2.973 / 2), " 1-100xi =", 1 - 100 * xi)

print("\n041-1 theta_QCD = xi^2")
print("  xi^2 =", xi ** 2, "; Grenze 1e-10 -> Faktor", xi ** 2 / 1e-10)

print("\n046-1 Neutrinos E = 1/xi_nu")
vals = {"e": 16 / 9 * 1e-8, "mu": 256 / 45 * 1e-8, "tau": 400 / 81 * 1e-8}
stated = {"e": 9.1, "mu": 1.9, "tau": 18.0}
for k, x in vals.items():
    print(f"  nu_{k}: xi_nu={x:.4e}, 1/xi_nu={1/x:.4e}, Verhältnis zu nu_e = {(1/x)/(1/vals['e']):.4f}, "
          f"Text-Verhältnis = {stated[k]/stated['e']:.4f}")
print("  gemeinsamer Faktor Text/(1/xi):", [stated[k] / (1 / vals[k]) for k in vals])
print("  Summe Text =", sum(stated.values()), "meV")
dm31 = 2.5e-3  # eV^2
print("  sqrt(dm31^2) = ", math.sqrt(dm31) * 1e3, "meV (Mindestmasse schwerstes nu)")
print("  18.0^2-1.9^2 =", (18.0e-3) ** 2 - (1.9e-3) ** 2, "eV^2 (gegen 2.5e-3)")
print("  Summe Minimum NO:", (0 + math.sqrt(7.4e-5) + math.sqrt(2.5e-3)) * 1e3, "meV")

print("\n046-2 4. Generation")
print("  2*sqrt(xi)*246.22 GeV =", 2 * math.sqrt(xi) * 246.22, "GeV")

print("\n059-1 a_l")
a = xi / (2 * math.pi) / 12
print("  xi/(2pi)/12 =", a, "; / a_e-Genauigkeit 1e-12 ->", a / 1e-12, "; / erlaubter mu-Bereich 1.6e-9 ->", a / 1.64e-9)
print("\n059-2 theta_CP = xi:", xi, "; / 1e-10 =", xi / 1e-10)
