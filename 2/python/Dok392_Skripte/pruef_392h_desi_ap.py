#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
pruef_392h_desi_ap.py -- Dok. 392, Teil H: Alcock-Paczynski-Test des exponentiellen Entfernungsgesetzes
gegen DESI DR2.

Das Gesetz 1 + z = exp(H0 x / c) (Dok. 308, logarithmische Entfernungsformel in Dok. 267) entspricht in
der Massenlesart einem FRW-Modell mit a(eta) = exp(H0 (eta - eta0)), also H(z) = H0 (1+z) (392g).
Daraus D_M = (c/H0) ln(1+z), D_H = c/H(z) und

    D_M / D_H = (1+z) ln(1+z).

Das Verhältnis enthält weder H0 noch die Schallhorizontlänge r_d; die Einschränkung P20 (r_d unter
LambdaCDM-Annahmen) entfällt damit. Gemessen [Q]: DESI DR2 Results II, Abdul Karim u.a.,
arXiv:2503.14738, Tabelle IV (D_M/D_H mit Systematik). Die Werte der Bins sind als unabhängig
behandelt (getrennte Rotverschiebungsbereiche). Zum Vergleich flaches LambdaCDM mit dem DESI-Bestwert
Omega_m = 0,2975 (ebd., Abschnitt IX). Nur Standardbibliothek.
"""
import math

ok = n = 0
def check(name, cond, info=""):
    global ok, n
    n += 1; ok += bool(cond)
    print(f"  [{'OK ' if cond else 'FAIL'}] {name}" + (f"  ({info})" if info else ""))

# DESI DR2, Tabelle IV: Tracer, z_eff, D_M/D_H, sigma
desi = [("LRG1", 0.510, 0.622, 0.017), ("LRG2", 0.706, 0.892, 0.021),
        ("LRG3+ELG1", 0.934, 1.223, 0.019), ("ELG2", 1.321, 1.948, 0.045),
        ("QSO", 1.484, 2.386, 0.136), ("Lya", 2.330, 4.518, 0.097)]

def f_exp(z):
    return (1 + z)*math.log(1 + z)

def f_lcdm(z, om=0.2975, N=4000):
    E = lambda x: math.sqrt(om*(1 + x)**3 + 1 - om)
    h = z/N   # Simpson
    s = 1/E(0) + 1/E(z) + sum((4 if i % 2 else 2)/E(i*h) for i in range(1, N))
    return s*h/3*E(z)

print("1. Vorhersage und Messung D_M/D_H")
print(f"     {'Tracer':10s} {'z':>6s} {'DESI':>14s} {'exp. Gesetz':>12s} {'Zug':>6s} {'LCDM':>7s} {'Zug':>6s}")
chi_e = chi_l = 0.0
pulls = {}
for name, z, v, s in desi:
    fe, fl = f_exp(z), f_lcdm(z)
    pe, pl = (fe - v)/s, (fl - v)/s
    chi_e += pe**2; chi_l += pl**2; pulls[name] = pe
    print(f"     {name:10s} {z:6.3f} {v:7.3f}+-{s:5.3f} {fe:12.3f} {pe:+6.1f} {fl:7.3f} {pl:+6.1f}")
print(f"     chi^2 (6 Werte): exponentielles Gesetz {chi_e:.1f}, LambdaCDM {chi_l:.1f}")

check("LambdaCDM-Referenz trifft DESI (chi^2 < 12 für 6 Werte)", chi_l < 12, f"{chi_l:.1f}")
check("Bis z = 1,5 trägt das Gesetz die Daten (|Zug| < 3 in fünf Bins)",
      all(abs(pulls[k]) < 3 for k in ("LRG1", "LRG2", "LRG3+ELG1", "ELG2", "QSO")),
      ", ".join(f"{k} {pulls[k]:+.1f}" for k in ("LRG1", "LRG2", "LRG3+ELG1", "ELG2", "QSO")))
check("Lyman-alpha bei z = 2,33 schließt das Gesetz aus (Zug < -5)", pulls["Lya"] < -5, f"{pulls['Lya']:+.1f}")
check("Gesamt: chi^2 des Gesetzes > 30 bei 6 Werten", chi_e > 30, f"{chi_e:.1f}")

print(f"\n{ok}/{n} Prüfungen bestanden")
