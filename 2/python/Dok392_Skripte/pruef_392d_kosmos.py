#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
pruef_392d_kosmos.py -- Dok. 392, Teil D: Kosmologie -- welche statische Lesart der Expansion gleichwertig ist.

Drei statische Lesarten der Rotverschiebung 1+z (Dok. 280, 312, 391):
  W  Wegverlängerung/Energieverlust nur am Photon (dE/dx = -xi E)
  T  wie W, zusätzlich Uhren über T*m = 1 mitgebucht (Zeitdehnung 1+z)
  M  volle Massenlesart: Uhren UND Maßstäbe mitgebucht (Atomlängen ~ 1/m), d. h. die
     Weyl-Umschreibung der Expansion (Wetterich 2013) -- alle dimensionslosen Observablen gleich.
Diskriminatoren (Dok. 312: "bleibt Programm"):
  1. Supernova-Lichtkurven: Dehnung (1+z)^b; [Q] DES (White u.a. 2024, MNRAS 533, 3365): b = 1,003 +- 0,005 (stat) +- 0,010 (sys).
  2. CMB-Temperatur bei z: T(z) = T0 (1+z)^(1-beta); [Q] Noterdaeme u.a. 2011, A&A 526, L7:
     beta = -0,007 +- 0,027 (gemessen über Anregung von CO-Niveaus, also T/m).
  3. Tolman-Flächenhelligkeit SB ~ (1+z)^-k; Expansion k = 4. [Q] Lubin & Sandage 2001, AJ 122, 1084:
     beobachtet k = 2,59 +- 0,17 (R) bzw. 3,37 +- 0,13 (I) vor Entwicklungskorrektur; jüngere Sternpopulationen
     früher heller -> wahres k größer; Ermüdung des Lichts (k = 1) dort mit > 10 sigma verworfen.
Standardbibliothek + sympy.
"""
import sympy as sp

ok = n = 0
def check(name, cond, info=""):
    global ok, n
    n += 1; ok += bool(cond)
    print(f"  [{'OK ' if cond else 'FAIL'}] {name}" + (f"  ({info})" if info else ""))

z, x, D, L = sp.symbols('z x D L', positive=True)
one = 1 + z

def observables(clock, ruler):
    """clock, ruler: ob Uhren bzw. Maßstäbe über T*m = 1 mit (1+z) mitgebucht werden.
    Rückgabe: Lichtkurven-Exponent b, CMB-Exponent (1-beta), Tolman-Exponent k."""
    b = 1 if clock else 0
    # Leuchtkraftentfernung: Energie je Photon (1+z)^-1, Ankunftsrate (1+z)^-1 falls Uhren mitgebucht
    dL2 = x**2*one*(one if clock else 1)
    # Winkeldurchmesser: Objektgröße bei Emission in heutigen Einheiten D*(1+z) falls Maßstäbe mitgebucht
    theta = D*(one if ruler else 1)/x
    SB = (L/dL2)/theta**2
    k = sp.nsimplify(sp.simplify(sp.log(sp.simplify(SB*D**2/L))/sp.log(one)))
    # CMB: Atome bei z messen T/m; mit T*m = 1 sind Uhren und Massen dieselbe Buchung --
    # bei mitgebuchten Massen ist m dort um (1+z) kleiner, T/m also um (1+z) größer
    tcmb = 1 if clock else 0
    return b, tcmb, -k

lesarten = {"W  nur Photon": (False, False), "T  + Uhren": (True, False), "M  + Uhren + Maßstäbe": (True, True)}
res = {}
print("Exponenten (b: Lichtkurven, 1-beta: T(z), k: Tolman)")
for name, (cl, ru) in lesarten.items():
    b, t, k = observables(cl, ru)
    res[name] = (b, t, k)
    print(f"     {name:24s} b = {b}   1-beta = {t}   k = {k}")
check("Expansion (Referenz): b = 1, 1-beta = 1, k = 4 -- die volle Massenlesart M stimmt in allen drei überein",
      res["M  + Uhren + Maßstäbe"] == (1, 1, 4))

print("1. Supernova-Lichtkurven (b = 1,003 +- 0,011 kombiniert)")
bm, be = 1.003, (0.005**2+0.010**2)**0.5
check("Lesart W (b = 0) rund 90 sigma ausgeschlossen", abs(0-bm)/be > 85, f"{abs(0-bm)/be:.0f} sigma")
check("Lesarten T und M (b = 1) verträglich", abs(1-bm)/be < 1)

print("2. CMB-Temperatur T(z) (beta = -0,007 +- 0,027)")
bt, bte = -0.007, 0.027
check("Lesart W (1-beta = 0, also beta = 1) 37 sigma ausgeschlossen", abs(1-bt)/bte > 35)
check("Lesarten T und M (beta = 0) verträglich", abs(0-bt)/bte < 1)

print("3. Tolman-Test (k = 4 bei Expansion; beobachtet 2,59 / 3,37 vor Entwicklungskorrektur)")
kR, kI = 2.59, 3.37
check("Lesart W (k = 1) unter beiden Messwerten", res["W  nur Photon"][2] < min(kR, kI))
check("Lesart T (k = 2) liegt unter beiden Messwerten, obwohl die Entwicklungskorrektur k noch erhöht "
      "-> nicht verträglich ohne eigene Verdunkelung früher Galaxien", res["T  + Uhren"][2] < min(kR, kI))
check("Lesart M (k = 4) verträglich, wenn frühe Galaxien heller waren (Richtung der Sternentwicklung)",
      res["M  + Uhren + Maßstäbe"][2] > max(kR, kI))

print("4. Bilanz")
check("Gleichwertig mit der Expansion ist nur die Lesart, die Uhren UND Maßstäbe über T*m = 1 mitbucht; "
      "reine Wegverlängerung am Photon ist es nicht",
      [nm for nm, r in res.items() if r == (1, 1, 4)] == ["M  + Uhren + Maßstäbe"])

print(f"\n{ok}/{n} Prüfungen bestanden")
raise SystemExit(0 if ok == n else 1)
