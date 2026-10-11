#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
pruef_392g_abstaende.py -- Dok. 392, Teil G: Winkeldurchmesser-Entfernung und Alcock-Paczynski-Test
in der Massenlesart.

Gerechnet wird im flachen Minkowski-Raum mit zeitabhängigen Massen m(t) = m0 a(t). Atomare Längen und
Takte laufen mit 1/m (lambda_4 m = 2 pi, Dok. 314), die Photonenzahl bleibt erhalten, die
Koordinatenfrequenz eines Photons ist im flachen Raum fest. Daraus werden d_A, d_L und das
Alcock-Paczynski-Verhältnis Delta z / Delta theta durch direkte Buchung bestimmt und mit den
FRW-Formeln (d_A = a_e chi, d_L = chi / a_e, Delta z / Delta theta = (1+z) H d_A, H = a'/a^2 in
konformer Zeit) verglichen. Die Rechnung in der Massenlesart benutzt die FRW-Formeln nicht.

  1. Lesart M (Uhren und Maßstäbe mitgebucht): d_A, d_L und AP stimmen mit FRW überein,
     d_L / d_A = (1+z)^2 (Etherington).
  2. Hinweis (nicht gezählt): Lesarten W und T aus 392d haben d_L / d_A = (1+z)^(1/2) bzw. (1+z).
     Flächenhelligkeit ~ (d_A/d_L)^2, also ist der Tolman-Exponent k = 4 dieselbe Aussage wie
     d_A = d_L/(1+z)^2.
  3. Hinweis (nicht gezählt): Das Gesetz 1 + z = exp(H0 x) entspricht in M einem FRW-Modell mit
     H(z) = H0 (1+z); sein AP-Verhältnis D_M H / c = (1+z) ln(1+z) ist die Vorhersage, die gegen
     gemessene D_M/D_H zu prüfen bleibt.
Nur Standardbibliothek.
"""
import math

ok = n = 0
def check(name, cond, info=""):
    global ok, n
    n += 1; ok += bool(cond)
    print(f"  [{'OK ' if cond else 'FAIL'}] {name}" + (f"  ({info})" if info else ""))

T0 = 1.0          # Beobachtungszeitpunkt (Koordinatenzeit = konforme Zeit)
M0 = 1.0          # heutige Masse, setzt die Einheiten des Beobachters

def buchung_M(a, chi, N=1e-7, eps=1.0, ndot=1.0):
    """Lesart M im flachen Raum: Masse m(t) = M0 a(t)."""
    te = T0 - chi
    me = M0*a(te)
    z = M0/me - 1.0
    # Winkel: Objekt aus N atomaren Längen hat Koordinatengröße N/me
    theta = (N/me)/chi
    L_obs = N/M0                      # Eigengröße in heutigen Einheiten
    dA = (L_obs/theta)*M0             # in Beobachtereinheiten (Koordinate * M0)
    # Fluss: ndot Photonen je Eigentakt des Senders (Takt = 1/me Koordinatenzeit),
    # Energie eps in Sendereinheiten, Koordinatenfrequenz ~ me bleibt unterwegs fest
    rate_koord = ndot*me              # Photonen je Koordinatenzeit
    rate_obs = rate_koord/M0          # je Beobachtertakt
    E_obs = eps*me/M0                 # Energie je Photon in Beobachtereinheiten
    area_obs = 4*math.pi*chi**2*M0**2
    F = rate_obs*E_obs/area_obs
    dL = math.sqrt(ndot*eps/(4*math.pi*F))
    # AP: radiale Ausdehnung N atomare Längen -> Koordinatenausdehnung N/me
    dchi = N/me
    z2 = M0/(M0*a(T0 - chi - dchi)) - 1.0
    ap = (z2 - z)/theta
    return z, dA, dL, ap

def frw(a, chi, h=1e-6):
    te = T0 - chi
    ae = a(te)
    z = 1/ae - 1
    H = (a(te + h) - a(te - h))/(2*h)/ae**2
    dA = ae*chi
    return z, dA, chi/ae, (1 + z)*H*dA

modelle = {
    "Materie a ~ t^2": lambda t: (t/T0)**2,
    "exponentiell a = exp(t-T0)": lambda t: math.exp(t - T0),
}
chis = [0.05, 0.2, 0.4, 0.6]

print("1. Lesart M gegen FRW (direkte Buchung, ohne FRW-Formeln)")
for name, a in modelle.items():
    rel_A = rel_L = rel_AP = rel_E = 0.0
    for chi in chis:
        zM, dAM, dLM, apM = buchung_M(a, chi)
        zF, dAF, dLF, apF = frw(a, chi)
        rel_A = max(rel_A, abs(dAM/dAF - 1))
        rel_L = max(rel_L, abs(dLM/dLF - 1))
        rel_AP = max(rel_AP, abs(apM/apF - 1))
        rel_E = max(rel_E, abs(dLM/dAM/(1 + zM)**2 - 1))
    check(f"{name}: d_A wie FRW", rel_A < 1e-9, f"max. Abw. {rel_A:.1e}")
    check(f"{name}: d_L wie FRW", rel_L < 1e-9, f"max. Abw. {rel_L:.1e}")
    check(f"{name}: d_L/d_A = (1+z)^2", rel_E < 1e-9, f"max. Abw. {rel_E:.1e}")
    check(f"{name}: Alcock-Paczynski wie FRW", rel_AP < 1e-4, f"max. Abw. {rel_AP:.1e}")

print("2. Hinweis: Reziprozität nur in Lesart M (Exponenten aus 392d, nicht gezählt)")
# W: nur Photonenenergie ~ 1/(1+z); T: zusätzlich Ankunftsrate; M: zusätzlich Maßstäbe ~ 1/m.
# Flächenhelligkeit ~ (d_A/d_L)^2 = (1+z)^(-k), also d_L/d_A = (1+z)^(k/2).
for k_name, k in (("W", 1), ("T", 2), ("M", 4)):
    print(f"     {k_name}: Tolman k = {k}  ->  d_L/d_A = (1+z)^{k/2:g}")

print("3. Hinweis: exponentielles Gesetz 1+z = exp(H0 x) in Lesart M (nicht gezählt)")
for zz in (0.51, 0.71, 0.93, 1.32, 2.33):
    print(f"     z = {zz:4.2f}:  D_M H/c = (1+z) ln(1+z) = {(1 + zz)*math.log(1 + zz):.3f}")

print(f"\n{ok}/{n} Prüfungen bestanden")
