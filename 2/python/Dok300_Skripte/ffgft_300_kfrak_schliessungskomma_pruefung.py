#!/usr/bin/env python3
# ffgft_300_kfrak_schliessungskomma_pruefung.py
# ---------------------------------------------------------------------------
# PRÜFSKRIPT (kein Beweis): hängt der kleine, bei der Projektion vernachlässigte
# Faktor -- das Schließungs-"Komma" der aufgerollten Rekursion -- mit K_frak
# zusammen?
#
# Kontext (aus dem Gespräch, ehrlich protokolliert):
#   * Die aufgerollte Rekursion schließt sich erst nach N=75 gleichen Teilstücken
#     (nicht nach einer Umdrehung). N = 1/(100*xi), xi = 4/30000.
#   * "Nach einer Umdrehung deckt sich der Ausschnitt" ist eine NÄHERUNG:
#     jedes Teilstück ist eine um einen kleinen Faktor eps verkürzte Umdrehung;
#     75 solche Verkürzungen summieren sich zur exakten Schließung.
#   * Marcel PROJIZIERT (cut-and-project). Eine Projektion MUSS dieses Defizit
#     nicht tragen -- sie kann es verschlucken; sein Objekt kann sauber
#     geschlossen erscheinen, obwohl das Original ein Defizit hat.
#   * Johann korrigiert den aufgerollten Faktor als K_frak (SI-Umrechnung,
#     in die Brückenkonstanten absorbiert). Die zu prüfende Frage ist daher
#     NICHT "gleiche Zahl auf einer Ebene", sondern ob der von der Projektion
#     verschluckte Faktor MIT K_frak zusammenhängt.
#
# WAS DAS SKRIPT TUT (und was nicht):
#   * Es rechnet die xi-Seite (eps aus der Schließung) exakt aus -- das ist die
#     einzige Seite, die aus dem Korpus vorliegt.
#   * K_frak ist EINGABE. Der Wert wird NICHT erfunden. Ohne ihn meldet das
#     Skript nur die xi-Seite und fordert den Wert an.
#   * Es behauptet KEINE Gleichheit. Es meldet das Verhältnis und ob es "sauber"
#     ist (nahe 1, 2π, φ, einfacher Bruch) -- als KANDIDAT, nicht als Fund.
#   * ZIRKULARITÄTS-WÄCHTER: ist K_frak selbst über 75 oder xi definiert, dann
#     ist das Verhältnis per Definition fest -> das Skript warnt, dass ein
#     "Zusammenhang" dann definitorisch und kein empirischer Befund ist.
# ---------------------------------------------------------------------------

import math
from fractions import Fraction

# HINWEIS: Der Korpuswert ist K_frak = 1 - 100*xi = 74/75 = 0.9867
# (subtraktiv; Dok. 133/231/032/285). eps = 100*xi ist das Schliessungs-
# Komma; K_frak = 1 - eps. Beide sind 100*xi; der Anker ist Dok. 133
# (Faktor 100 aus RG-Lauf; K_frak durch m_e/m_mu-Konsistenz fixiert),
# nicht die 75. Das Skript listet beide Vorzeichen als Kandidaten.
# ============================ xi-Seite (Korpus) ============================
XI = Fraction(4, 30000)                 # 4/30000 = 1/7500
N  = 1 / (100 * XI)                      # = 75, Schließungszahl (1/(100 xi))
assert N == 75, "N sollte 75 sein (= 1/(100 xi))"
N = int(N)

# Herleitung des Schließungs-Kommas eps:
# 75 gleiche Teilstücke, jedes eine um eps verkürzte Umdrehung, schließen exakt.
# 75*(1 - eps) = 74  (75 leicht zu kurze Umdrehungen = 74 volle -> Schließung)
#   => 75*eps = 1  => eps = 1/75 = 100*xi   (dimensionslos, "das Komma")
eps_dimlos = Fraction(1, N)             # = 100*xi
assert eps_dimlos == 100 * XI

# alternative, ebenso legitime Lesarten des kleinen Faktors:
candidates = {
    "eps_dimlos (1/75 = 100*xi)"     : float(eps_dimlos),
    "eps_winkel (2*pi/75, rad/Umdr.)": 2 * math.pi / N,
    "eps_komplement (1 - 1/75)"      : float(1 - eps_dimlos),
    "eps_grad (360/75)"              : 360.0 / N,
}

# ============================ K_frak (EINGABE) =============================
# Johann trägt hier den selbst gerechneten Wert ein. Solange None, prüft das
# Skript nur die xi-Seite und fordert den Wert an. NICHT erfinden.
K_FRAK_VALUE = None          # z.B. 1.0013333...  (dimensionslos) ODER SI-Wert
K_FRAK_UNIT  = ""            # "" = dimensionslos, sonst z.B. "SI" / "J*s" ...
# Definierender Ausdruck von K_frak, als Text -- für den Zirkularitäts-Wächter:
K_FRAK_EXPR  = ""            # z.B. "1 + 1/75", "f(xi)", "aus calc_De Brückenkonst."

# ============================ Marcel-Seite (EINGABE) =======================
# Der Faktor, den SEINE Projektion verschluckt (falls/ sobald bekannt).
MARCEL_PROJECTION_FACTOR = None   # NICHT erfinden; kommt aus seinem Material.

# ================================ Auswertung ===============================
def is_clean(x, tol=1e-3):
    """nahe an einer 'sauberen' Konstante? -> (name, wert) oder None"""
    if x is None or x <= 0: return None
    refs = {"1": 1.0, "2*pi": 2*math.pi, "pi": math.pi, "phi": (1+5**0.5)/2,
            "1/phi": 2/(1+5**0.5), "e": math.e}
    for name, v in refs.items():
        if abs(x - v) < tol: return (name, v)
    fr = Fraction(x).limit_denominator(1000)
    if abs(float(fr) - x) < tol and fr.denominator <= 100:
        return (f"{fr.numerator}/{fr.denominator}", float(fr))
    return None

def circularity_flag(expr):
    e = (expr or "").lower()
    hit = [t for t in ("75", "xi", "ξ", "1/(100", "100*xi", "1/7500") if t in e]
    return hit

print("="*68)
print("PRÜFUNG: Schließungs-Komma (xi-Seite)  <->  K_frak")
print("="*68)
print(f"xi                     = {XI} = {float(XI):.8g}")
print(f"Schließungszahl N      = {N}   (= 1/(100*xi))")
print("kleiner Faktor eps, Kandidaten aus der Schließung:")
for k, v in candidates.items():
    print(f"   {k:32s} = {v:.10g}")
print()

if K_FRAK_VALUE is None:
    print(">> K_frak ist NICHT eingetragen.")
    print(">> Trage K_FRAK_VALUE (dein selbst gerechneter Wert) und K_FRAK_EXPR")
    print(">> (die Definition) oben ein, dann vergleicht das Skript.")
    print(">> Bis dahin steht nur die xi-Seite fest; nichts wird behauptet.")
else:
    print(f"K_frak                 = {K_FRAK_VALUE}  [{K_FRAK_UNIT or 'dimensionslos'}]")
    print(f"K_frak-Definition      = {K_FRAK_EXPR!r}")
    cflag = circularity_flag(K_FRAK_EXPR)
    if cflag:
        print()
        print("!! ZIRKULARITÄTS-WARNUNG: K_frak ist über " + ", ".join(cflag) +
              " definiert.")
        print("!! Dann ist ein Zusammenhang mit eps DEFINITORISCH, kein Befund.")
        print("!! Ein sauberes Verhältnis zählt nur, wenn K_frak UNABHÄNGIG von")
        print("!! 75/xi bestimmt ist (z.B. rein aus SI-Messgrößen).")
    print()
    print("Verhältnisse eps / K_frak (dimensionslos nur sinnvoll, wenn Einheiten passen):")
    for k, v in candidates.items():
        r = v / K_FRAK_VALUE
        c = is_clean(r) or is_clean(1/r)
        tag = f"  <- sauber: {c[0]}" if c else ""
        print(f"   {k:32s}: eps/K_frak = {r:.8g}{tag}")
    if not cflag:
        print()
        print(">> Lesart: ein 'sauberes' Verhältnis (1, 2π, φ, einfacher Bruch) bei")
        print(">> UNABHÄNGIG bestimmtem K_frak ist ein KANDIDAT für den Zusammenhang,")
        print(">> kein Beweis. Provenienz von K_frak entscheidet.")

print()
if MARCEL_PROJECTION_FACTOR is None:
    print("Marcel-Projektionsfaktor: nicht eingetragen (kommt aus seinem Material,")
    print("nicht zu erfinden). Er MUSS kein Defizit tragen -- die Projektion kann es")
    print("verschlucken; genau dann ist K_frak die Umrechnung, die es wieder einträgt.")
else:
    print(f"Marcel-Projektionsfaktor = {MARCEL_PROJECTION_FACTOR}")
    for k, v in candidates.items():
        r = v / MARCEL_PROJECTION_FACTOR
        print(f"   {k:32s}: eps/proj = {r:.8g}")

print()
print("STATUS: xi-Seite fest, K_frak offen (deine Rechnung). Das Skript stellt die")
print("Frage scharf und verhindert einen definitorischen Scheintreffer -- mehr nicht.")
