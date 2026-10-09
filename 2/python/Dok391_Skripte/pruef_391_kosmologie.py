#!/usr/bin/env python3
"""Prüfskript zu Dok. 391 — Lose Puzzleteile II: Kosmologie.

Teil A sichert jede Korpusangabe von Dok. 391 durch eine Textprüfung in der
genannten Kapiteldatei ab (Fundstelle muss wörtlich vorhanden sein).
Teil B rechnet die Zahlenwerte nach, die Dok. 391 nennt oder voraussetzt.
Der kosmische Sektor ist kalibriert (P39, P20): Teil B prüft Konsistenz der
Formeln, keine Vorhersage von H0.

Aufruf aus der Repo-Wurzel:  python3 2/python/Dok391_Skripte/pruef_391_kosmologie.py
"""
from pathlib import Path
import math, sys

ROOT = Path(__file__).resolve().parents[2]
CH = ROOT / "Sources" / "ch"
ok = fail = 0

def check(name, cond, info=""):
    global ok, fail
    if cond:
        ok += 1; print(f"  PASS  {name}")
    else:
        fail += 1; print(f"  FAIL  {name}  {info}")

def has(prefix, phrase):
    files = [f for f in sorted(CH.glob(f"{prefix}_*De_ch.tex")) if "Archiv" not in f.name]
    return any(phrase in f.read_text(encoding="utf-8") for f in files)

print("Teil A — Fundstellen im Korpus")
R190 = "190_T0_Korrekturen"
belege = [
    (R190, "P39 &", "P39 vorhanden"),
    (R190, "von \\emph{keinem} Rahmen aus ersten Prinzipien hergeleitet", "P39: kein Rahmen leitet R_H/l_P her"),
    (R190, "P20 &", "P20 vorhanden"),
    (R190, "dimensionsloses $\\xi$-Verhältnis ($R_H/\\ell_P$)", "P20: Form als xi-Verhältnis"),
    ("365", "Der Exponent~10 in $H_0\\propto\\xi^{10}$ ist Setzung", "Exponent 10 Setzung (365)"),
    ("365", "Der kosmische Sektor ($H_0$, $\\Lambda$) wird ausgeklammert", "kosmischer Sektor ausgeklammert (365)"),
    (R190, "Achromasie bleibt, die Skala der Wegverlängerung ist über $H_0$ kalibriert", "K6/R137: Skala kalibriert"),
    (R190, "Keine Abweichung der Supernova-Zeitdehnung von $(1+z)$", "R128 Zeitdehnung"),
    (R190, "Uhrentakt gemeinsam gebucht", "R128 gemeinsame Buchung"),
    ("312", "nur die Photonseite ändert", "Tired Light scheitert (312)"),
    ("312", "Wetterich 2013", "Wetterich in 312"),
    ("312", "Expansion vs.\\ Massenlauf rahmenäquivalent (Wetterich) & [K]", "Äquivalenz [K] (312)"),
    ("312", "\\emph{möglich} und beobachtungsgleich ist -- nicht, dass sie", "ehrliche Grenze (312)"),
    ("267", "\\emph{entartet}", "Entartung (267)"),
    ("312", "$\\partial\\text{T}^4 = \\emptyset$", "Träger ohne Rand (312)"),
    ("313", "einen Halbzyklus", "Halbzyklus (313)"),
    ("313", "der \\enquote{Anfang} ist der Antipode des Zeitzyklus", "Anfang = Antipode (313)"),
    ("313", "K$|$P20", "Status K|P20 (313)"),
    ("313", "als\n        Randbedingung gesetzt werden", "Periodizität als Randbedingung (313)"),
    ("182", "Hubble-Länge: die obere Skala des kosmologischen Sektors", "Hubble-Länge Maximalskala (182)"),
    ("365", "Hubble-Länge als geometrische Maximalskala (nicht als Expansionshorizont)", "Maximalskala (365)"),
    ("365", "$a_0=cH_0/(2\\pi)$ \\KM", "a0 = cH0/2pi [K] (365)"),
    ("309", "Querverankerung", "Querverankerung (309)"),
    ("309", "$a_0$ (MOND-Skala", "a0 in 309"),
    ("308", "a = \\sqrt{a_N^2 + a_N\\,a_0}", "Interpolationsformel (308)"),
    ("308", "a_0 = 2\\,a_\\text{bg}", "a0 = 2 a_bg (308)"),
    ("308", "Unruh", "Unruh-Kopplung (308)"),
    ("308", "Lesart-Artefakt", "Lambda Lesart-Artefakt (308)"),
    (R190, "Casimir--CMB-Verbindung: Identität, kein Messbeleg", "R136"),
    (R190, "Die $\\Lambda$-Formeln in Dok.~028, 143 und 149 treffen den beobachteten Wert nicht", "R137 Lambda [X]"),
    (R190, "Die Relation $T(z)$ in Dok.~039 ist durch Messungen ausgeschlossen", "R137 T(z) [X]"),
    (R190, "einheitenabhängige Übereinstimmung", "R137 CMB-Temperatur"),
    (R190, "Der Faktor ist eine Setzung", "R139 Faktor 3"),
    (R190, "R70 &", "R70 vorhanden"),
    ("388", "\\frac{T_{\\mathrm{CMB}}}{m_e}=(8\\pi)^{1/4}\\,\\xi^{5/2}", "CMB-Kandidat (388)"),
    ("388", "ein Zufall ist nicht ausgeschlossen", "Zufallsprüfung (388)"),
    ("388", "T_{\\mathrm{CMB}}^4=16\\,H_0\\,m_e^3}\\qquad\\BM", "T^4 = 16 H0 me^3 [B] (388)"),
]
for pre, phrase, name in belege:
    check(f"{pre}: {name}", has(pre, phrase), f"[fehlt: {phrase!r}]")

print("Teil B — Zahlenwerte (Konsistenz, keine Vorhersage)")
xi = 4/30000
c = 299792458.0
lam_e = 3.8615926796e-13          # reduzierte Compton-Wellenlänge Elektron [m]
Mpc = 3.0856775814913673e22
# Dok. 308/279: H0/c = (pi/2) xi^10 / lam_e  (Exponent 10 gesetzt, P20)
H0 = c * (math.pi/2) * xi**10 / lam_e
H0_kms = H0 * Mpc / 1000
check(f"H0 aus gesetztem Exponenten = {H0_kms:.2f} km/s/Mpc (nahe den Messwerten 67–74; Exponent gesetzt)", 66 < H0_kms < 75)
R_H = c / H0
check(f"R_H = c/H0 = {R_H:.3e} m (Dok. 182 mit gemessenem H0: 1,398e26 m)", abs(R_H/1.398e26 - 1) < 0.02)
tau_c = 2*math.pi/H0 / (3.15576e16)
check(f"Zeitzyklus tau_c = 2pi/H0 = {tau_c:.1f} Gyr (Dok. 313: 91,9)", abs(tau_c - 91.9) < 0.5)
a0_1 = c*H0/(2*math.pi)
a0_2 = c**2 * xi**10 / (4*lam_e)
check(f"a0 = cH0/2pi = {a0_1:.4e} = c^2 xi^10/(4 lam_e) = {a0_2:.4e}", abs(a0_1/a0_2 - 1) < 1e-12)
check(f"a0 in der Größenordnung von Milgroms 1,2e-10 m/s^2 (Faktor {1.2e-10/a0_1:.2f})", 0.5 < a0_1/1.2e-10 < 2)
# Dirac: elektrische/gravitative Kraft Elektron-Proton
e = 1.602176634e-19; eps0 = 8.8541878128e-12; G = 6.67430e-11
me, mp = 9.1093837015e-31, 1.67262192369e-27
dirac = e**2/(4*math.pi*eps0*G*me*mp)
check(f"Dirac-Verhältnis = {dirac:.3e} (~1e39)", 1e39 < dirac < 1e40)
lP = 1.616255e-35
check(f"R_H/l_P = {R_H/lP:.3e} (~1e61)", 1e60 < R_H/lP < 1e62)
# Zeitdehnung: Wellenlänge und Takt gleich gebucht
for z in (0.5, 2.0, 5.0):
    x = math.log(1+z)/xi       # 1+z = exp(xi x)
    stretch_lambda = math.exp(xi*x); stretch_clock = math.exp(xi*x)
    check(f"z={z}: Wellenlänge und Uhrentakt gedehnt um {stretch_clock:.3f} = 1+z", abs(stretch_clock-(1+z))<1e-12 and stretch_lambda==stretch_clock)
# Dok. 388: T/me = (8pi)^(1/4) xi^(5/2); T^4 = 16 H0 me^3 (natürliche Einheiten)
me_eV = 0.51099895e6; kB = 8.617333262e-5
T_eV = (8*math.pi)**0.25 * xi**2.5 * me_eV
T_K = T_eV / kB
check(f"T_CMB-Kandidat = {T_K:.4f} K (FIRAS 2,7255 K)", abs(T_K/2.7255 - 1) < 1e-4)
H0_nat = (math.pi/2) * xi**10 * me_eV
check("T^4 = 16 H0 me^3 aus beiden Formen (xi kürzt sich)", abs(T_eV**4 / (16*H0_nat*me_eV**3) - 1) < 1e-12)
# Interpolationsformel: Grenzfälle
a0 = a0_1
for aN, lim in ((1e3*a0, "Newton"), (1e-4*a0, "tief-MOND")):
    a = math.sqrt(aN**2 + aN*a0)
    ref = aN if lim == "Newton" else math.sqrt(aN*a0)
    check(f"a = sqrt(aN^2 + aN a0) im Grenzfall {lim}", abs(a/ref - 1) < 1e-3)

print(f"\nErgebnis: {ok}/{ok+fail} bestanden")
sys.exit(0 if fail == 0 else 1)
