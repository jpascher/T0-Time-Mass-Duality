#!/usr/bin/env python3
"""Prüfskript zu Dok. 390 — Lose Puzzleteile.

Teil A sichert jede Korpusangabe von Dok. 390 durch eine Textprüfung in der
genannten Kapiteldatei ab (Fundstelle muss wörtlich vorhanden sein).
Teil B rechnet die wenigen Zahlenwerte nach, die Dok. 390 nennt.

Aufruf aus der Repo-Wurzel:  python3 2/python/Dok390_Skripte/pruef_390_puzzleteile.py
"""
from fractions import Fraction as F
from pathlib import Path
import math, sys

ROOT = Path(__file__).resolve().parents[2]          # .../2
CH = ROOT / "Sources" / "ch"

ok = fail = 0
def check(name, cond, info=""):
    global ok, fail
    if cond:
        ok += 1; print(f"  PASS  {name}")
    else:
        fail += 1; print(f"  FAIL  {name}  {info}")

def has(dok_prefix, phrase):
    files = sorted(CH.glob(f"{dok_prefix}_*De_ch.tex"))
    files = [f for f in files if "Archiv" not in f.name] or sorted(CH.glob(f"{dok_prefix}_*De_ch.tex"))
    for f in files:
        if phrase in f.read_text(encoding="utf-8"):
            return True
    return False

print("Teil A — Fundstellen im Korpus")
belege = [
    # Kaluza-Klein
    ("330", "Kaluza-Klein-Relation der", "T·m=1 als KK-Relation der vierten Torusrichtung"),
    ("330", "Massedimension $S^1_m$", "Massendimension S^1_m"),
    ("270", "ist damit strukturell die Kaluza-Klein-Relation f\\\"ur die Massedimension", "Dok. 270 Proposition"),
    ("307", "gilt hier für die eingerollte Zeit", "Zeit statt Raumrichtung"),
    ("307", "mit der Masse in der Rolle des Modenindex", "Masse als Modenindex"),
    ("231", "Die Extra-Dimension ist \\emph{zeitlich}, nicht räumlich", "Dok. 231 zeitliche Extra-Dimension"),
    ("311", "Skala ohne Modul", "Skala ohne Modul"),
    ("311", "Man hat eine Skala gewonnen und einen Parameter dazugekauft", "freier Radius"),
    ("318", "Radius $R$ ist freier Modul", "Dok. 318 drei Wege"),
    ("307", "es gibt keinen zusätzlichen Kaluza-Klein-Turm", "kein zusätzlicher Turm"),
    ("312", "Lorentz-Invarianz \\emph{lokal}", "Lorentz lokal"),
    # de Broglie / Compton
    ("312", "Warum Einstein $\\tilde T \\cdot m = 1$ nicht sah", "Kapitel Einstein"),
    ("312", "de~Broglie 1924", "de Broglie 1924"),
    ("312", "Compton-Uhr-Experiment (Lan, Müller et al., Berkeley)", "Compton-Uhr 2013"),
    ("314", "de-Broglie-Relation", "lambda_4 m = 2pi als de-Broglie-Relation"),
    ("312", "Statuswechsel", "Statuswechsel der Formel"),
    ("312", "Konstanten-Fixierung umstellte", "SI-Reform 2019"),
    # Pauli
    ("307", "Paulis Einwand die eingerollte Sicht nicht trifft", "Pauli trifft kompakte Zeit nicht (307)"),
    ("334", "die Pauli-Bedingung ist nicht erfüllt", "Pauli-Bedingung (334)"),
    # relationale Zeit
    ("307", "Page--Wootters", "Page-Wootters"),
    ("307", "Bars", "Zwei-Zeit-Physik Bars"),
    ("307", "kompakte geometrische Zeit statt relationaler oder thermischer Zeit", "Abgrenzung 307"),
    # Wigner
    ("307", "Masse ist eine Casimir-Invariante", "Wigner in 307"),
    ("339", "Wigner (1939) klassifiziert", "Wigner in 339"),
    # Casimir SU(3)
    ("324", "\\xi = \\frac{C_2(SU(3)_{\\text{fund}})}{N_{\\text{Fourier}}}", "xi = C2/N_Fourier"),
    ("324", "\\textbf{[B]} Diese Formel ist exakt", "Formel [B]"),
    ("324", "\\textbf{[K]} Die Fourier-Modenzahl", "N_Fourier [K]"),
    # Heaviside-Lorentz
    ("365", "Heaviside-Lorentz-Einheiten", "HL in 365"),
    ("365", "ist dabei keine Setzung im Sinn von R56, sondern eine \\emph{Einheitenwahl}", "alpha=1 Einheitenwahl"),
    ("338", "des Ankers $E_0^2 = 54\\;\\text{MeV}^2$, keine unabhängige Vorhersage", "alpha am Anker E0"),
    # Orbifold
    ("311", "Bedingung 2 ist vorbildlich erfüllt", "311 Stringtheorie"),
    ("190_T0_Korrekturen", "die neun Fixpunkte im Ortsraum", "R131 neun Fixpunkte"),
    ("365", "$D_4$ als dichtestes Gitter", "D4 Setzung"),
    ("365", "$\\mathbb{Z}_3$ als sparsamste Identifikation mit drei Generationen", "Z3 Setzung"),
    # Galois / Frobenius
    ("336", "Frobenius-Automorphismus", "Frobenius in 336"),
    ("346", "Ladungsquantisierung aus dem Legendre-Symbol", "Legendre 346"),
    ("348", "entsprechen den drei Generationen", "Generationen 348"),
    ("338", "43200", "43200 in 338"),
    ("190_T0_Korrekturen", "Hyperladung der geladenen Leptonen folgt damit nicht", "R146"),
    # Koide
    ("369", "Das exakte Paar $(\\sqrt2,\\,2/9)$ ist für", "Paar ausgeschlossen (369)"),
    ("369", "$\\theta = 2/9$ \\BM", "theta [B] (369)"),
    ("353", "nur mit der unbegründeten", "Amplitude [S] (353)"),
    ("367", "p_0 = \\frac{2}{9}", "p0 = 2/9 (367)"),
    ("353", "Foot", "Foot-Lesart in 353"),
    ("353", "Gleichverteilung zwischen symmetrischer und nicht-trivialer Mode", "Gleichverteilung 353"),
    ("190_T0_Korrekturen", "R150 &", "R150"),
    ("367", "Der\nFaktor~$3$ ist hier gesetzt", "3|A| gesetzt (367)"),
    # Rauschgrenze
    ("343", "Auflösungsboden", "xi als Auflösungsboden (343)"),
]
for dok, phrase, name in belege:
    check(f"Dok. {dok}: {name}", has(dok, phrase), f"[fehlt: {phrase!r}]")

print("Teil B — Zahlenwerte")
N = 3
C2 = F(N*N - 1, 2*N)
check("C2(SU(3)_fund) = 4/3", C2 == F(4, 3))
xi = C2 / 10**4
check("xi = (4/3)/10^4 = 4/30000", xi == F(4, 30000))
check("43200 = |GF(9)*|^2 * 5^2 * |GF(27)|", (9-1)**2 * 25 * 27 == 43200)
check("(r_mu/r_e)^2/xi = 43200 mit r_mu/r_e = 12/5", F(12, 5)**2 / xi == 43200)
# Koide mit PDG 2024 (MeV)
me, mmu, mtau = 0.51099895000, 105.6583755, 1776.93
Q = (me + mmu + mtau) / (math.sqrt(me) + math.sqrt(mmu) + math.sqrt(mtau))**2
check(f"Koide Q = {Q:.7f} nahe 2/3 (|dQ| < 1e-4)", abs(Q - 2/3) < 1e-4)
check("p0 = (sqrt2/3)^2 = 2/9", abs((math.sqrt(2)/3)**2 - 2/9) < 1e-15)
# Compton-Zeit und Zitterbewegungsfrequenz des Elektrons (SI, nur Plausibilität)
hbar, c, m_e = 1.054571817e-34, 299792458.0, 9.1093837015e-31
tC = hbar / (m_e * c**2)
check(f"Compton-Zeit Elektron = {tC:.3e} s", 1.28e-21 < tC < 1.30e-21)
wZ = 2 * m_e * c**2 / hbar
check(f"Zitterbewegung 2mc^2/hbar = {wZ:.3e} rad/s = 2/t_C", abs(wZ * tC - 2) < 1e-12)
c0=1.0; d0=math.sqrt(2)
check("Gleichverteilung: 3c^2 = (3/2)d^2 bei d = sqrt2*c", abs(3*c0**2-1.5*d0**2)<1e-12)
v=[c0+d0*math.cos(0.4+2*math.pi*k/3) for k in range(3)]
cphi=sum(v)/(math.sqrt(3)*math.sqrt(sum(x*x for x in v)))
check("Foot: Winkel (sqrt m) zu (1,1,1) = 45 Grad", abs(math.degrees(math.acos(cphi))-45)<1e-9)
# Kaluza-Klein: m_n = n/R in natürlichen Einheiten; T·m = 1 pro Mode
R = 7.3
check("KK-Turm: T_n * m_n = 2*pi*R/n * n/R = 2*pi (Periode mal Masse konstant)",
      all(abs((2*math.pi*R/n) * (n/R) - 2*math.pi) < 1e-12 for n in range(1, 10)))

print(f"\nErgebnis: {ok}/{ok+fail} bestanden")
sys.exit(0 if fail == 0 else 1)
