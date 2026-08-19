#!/usr/bin/env python3
# =============================================================================
# Euler-Spirale im 7-Limit: exakte Suche nach Beinahe-Schluessen
# -----------------------------------------------------------------------------
# Frage: nach welchen Kombinationen von Quinten (3), Terzen (5) und
# Naturseptimen (7) kommt die Spirale der Oktave (2) am naechsten?
#
# Methode: exakte Bruchrechnung (fractions.Fraction). Fuer jedes Tripel
# (b, c, d) von Exponenten zu 3, 5, 7 wird der Oktav-Exponent a so gewaehlt,
# dass 2^a * 3^b * 5^c * 7^d moeglichst nahe an 1 liegt. Der Rest ist das
# Komma; Groesse in Cent = 1200 * log2(Komma).
#
# Exakter Schluss 2^a 3^b 5^c 7^d = 1 mit (a,b,c,d) != 0 ist unmoeglich
# (Eindeutigkeit der Primfaktorzerlegung) -- das Skript prueft das mit.
# =============================================================================

from fractions import Fraction
from math import log2

LIMIT_B = 12   # Quinten-Exponent |b| <= 12
LIMIT_C = 6    # Terzen-Exponent  |c| <= 6
LIMIT_D = 4    # Septimen-Exponent|d| <= 4
CENT_MAX = 30  # nur Kommas unter 30 Cent auflisten

def komma(b, c, d):
    """Exaktes Komma 2^a 3^b 5^c 7^d >= 1 mit optimalem a; liefert (Fraction, a, cents)."""
    if (b, c, d) == (0, 0, 0):
        return None
    x = log2(3) * b + log2(5) * c + log2(7) * d
    a = -round(x)                       # Oktavreduktion: naechstes ganzes a
    frac = Fraction(3) ** b * Fraction(5) ** c * Fraction(7) ** d * Fraction(2) ** a
    if frac < 1:
        frac = 1 / frac                 # Komma stets als Verhaeltnis > 1 notieren
    cents = 1200 * log2(frac)
    return frac, a, cents

results = []
for b in range(-LIMIT_B, LIMIT_B + 1):
    for c in range(-LIMIT_C, LIMIT_C + 1):
        for d in range(-LIMIT_D, LIMIT_D + 1):
            r = komma(b, c, d)
            if r is None:
                continue
            frac, a, cents = r
            assert frac != 1, "Exakter Schluss gefunden -- unmoeglich!"
            if cents <= CENT_MAX:
                results.append((cents, b, c, d, a, frac))

results.sort()

# Duplikate durch Vielfache herausfiltern (z. B. 2*(b,c,d) ist doppeltes Komma)
from math import gcd
seen = set()
unique = []
for cents, b, c, d, a, frac in results:
    g = gcd(gcd(abs(b), abs(c)), abs(d))
    key = (b // g, c // g, d // g) if g else (b, c, d)
    if key in seen and g > 1:
        continue
    seen.add(key)
    unique.append((cents, b, c, d, a, frac))

NAMEN = {
    Fraction(4375, 4374):   "Ragisma",
    Fraction(2401, 2400):   "Breedsma",
    Fraction(32805, 32768): "Schisma (5-Limit)",
    Fraction(225, 224):     "Septimales Kleisma / Marvel-Komma",
    Fraction(1029, 1024):   "Gamelisma",
    Fraction(5120, 5103):   "Hemifamity / Beta-5-Komma",
    Fraction(81, 80):       "Syntonisches Komma (5-Limit)",
    Fraction(64, 63):       "Archytas-Komma / septimales Komma",
    Fraction(531441, 524288): "Pythagoreisches Komma (3-Limit)",
    Fraction(126, 125):     "Kleine septimale Diesis / Starling",
    Fraction(3125, 3087):   "Gariboh",
    Fraction(50, 49):       "Jubilisma / Tritonus-Diesis",
    Fraction(49, 48):       "Slendro-Diesis",
    Fraction(245, 243):     "Sensamagic / kleines Porkupinkomma",
    Fraction(6144, 6125):   "Porwell",
    Fraction(65625, 65536): "Horwell",
    Fraction(703125, 702464): "Meter (7-Limit)",
    Fraction(420175, 419904): "Wizma",
    Fraction(250047, 250000): "Landscape-Komma",
    Fraction(15625, 15552): "Kleisma (5-Limit)",
    Fraction(128, 125):     "Kleine Diesis (5-Limit)",
    Fraction(3136, 3125):   "Hemimean",
    Fraction(875, 864):     "Keema",
    Fraction(686, 675):     "Senga",
}

print(f"{'Cent':>8}  {'Komma':>18}  {'2^a':>5} {'3^b':>4} {'5^c':>4} {'7^d':>4}  Name")
print("-" * 90)
for cents, b, c, d, a, frac in unique[:40]:
    name = NAMEN.get(frac, "")
    tag7 = "" if d == 0 else "  [7-Limit]"
    print(f"{cents:8.3f}  {frac.numerator:>9}/{frac.denominator:<8}"
          f"  {a:>5} {b:>4} {c:>4} {d:>4}  {name}{tag7}")

print()
print("Suchraum: |b|<=%d Quinten, |c|<=%d Terzen, |d|<=%d Septimen, Kommas <= %d Cent"
      % (LIMIT_B, LIMIT_C, LIMIT_D, CENT_MAX))
print("Kein exakter Schluss gefunden (Assertion nie ausgeloest) -- wie bewiesen.")
