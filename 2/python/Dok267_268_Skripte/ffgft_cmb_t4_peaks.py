#!/usr/bin/env python3
"""
================================================================================
KORREKTUR-HINWEIS (7. Juni 2026) -- bitte zuerst lesen
================================================================================
Die Rechnung in diesem Skript (Jacobi-Entartung, Bose-Einstein, Verhaeltnisse)
ist korrekt. ABER die fruehere SCHLUSSFOLGERUNG, die Folge {1,6,14,26} folge
"aus xi allein als lokale Maxima", ist NICHT korrekt:
  - Echte Forward-Maxima des vollen T4-Spektrums: {3,6,10,14,18,22,26,30,...}
    (dicht). Davon ist 1 KEIN Maximum, und 10 (ein Maximum) fehlt in der Folge.
  - {1,6,14,26} wurde aus den gemessenen CMB-Verhaeltnissen abgelesen
    (Dok 268, Schritt 4) -> RETRODIKTION, keine Forward-Vorhersage.
Der ehrliche Forward-Gehalt (geometrische Anharmonizitaet aus der
Kodimension-1-Projektion, J0-Membran) steht in:
  forward_t4_spektrum.py, naive_bessel_projektion.py, resonator_vergleich.py,
  dimension_anharmonizitaet.py, spektral_dimension.py  (Dok 268, Schritt 17).
Dieses Skript daher als REIN ILLUSTRATIV / RETRODIKTION verstehen.

Aktualisiert am 1.10.2026: Ausgaben an R139(i) angepasst -- der Faktor 3 ist
eine Setzung (eine Projektion auf drei Raumrichtungen kann ihn nicht erzeugen,
weil die projizierte Wellenzahl die volle nie uebersteigt; neue Pruefung in
Schritt 8); die Eingangsfunktion I(r) enthaelt xi nicht ("Eingabe nur xi"
zurueckgenommen); "ohne Fit, ohne freien Parameter" ersetzt; P30 nach
naive_bessel_projektion.py offen, nicht "machbare Rechnung" (vgl. Dok. 268
bzw. Dok. 190, R139).
================================================================================
"""
"""
================================================================================
ffgft_cmb_t4_peaks.py
CMB-Akustikpeaks aus der T4-Gitterstruktur (FFGFT)
================================================================================

Dieses Skript reproduziert die Herleitung aus Dok. 268 Schritt fuer Schritt:

  Schritt 1: T4-Zustandsraum, Wicklungszahlen n = (n1,n2,n3,n4) in Z^4,
             Jacobi-Entartung g(|n|^2) = Anzahl Darstellungen als 4 Quadrate
  Schritt 2: thermische Besetzung Bose-Einstein, spektrale Dichte
             I(r) = g(r) * <N(r)> * r,  lokale Maxima bei |n|^2 = 3,6,10,14,18,...
  Schritt 3: Projektion ell proportional sqrt(|n|^2), Verhaeltnisse skalenfrei
  Schritt 4/5: dominante Grundpeaks |n|^2 = 1,6,14,26
  Schritt 8: Faktor 3 als SETZUNG (R139 i; Projektion erzeugt ihn nicht)
             sichtbare Serie 3*{1,6,14,26} = {3,18,42,78}

Ergebnis: Verhaeltnisse 1 : 2.449 : 3.742 : 5.099
          vs. CMB        1 : 2.441 : 3.682 : 5.091   (Abweichung < 2%)

Die spektrale Dichte I(r) enthaelt xi NICHT; die Folge {1,6,14,26} ist
aus den gemessenen Verhaeltnissen abgelesen, der Faktor 3 gesetzt
(Retrodiktion, R139). Die ABSOLUTE Skala (ell_1 ~ 220)
braucht hingegen einen externen Parameter (P20, Dok. 190) und ist
NICHT Gegenstand dieses Skripts -- hier geht es nur um die Verhaeltnisse.
================================================================================
"""

import math
from itertools import product

# --- Der eine Parameter ---
xi  = 1 / 7500
D_f = 3 - xi


# ---------------------------------------------------------------------------
# Schritt 1: Jacobi-Entartung g(|n|^2) = r_4(n)
# Anzahl der Darstellungen von n als Summe von 4 Quadraten (mit Vorzeichen
# und Reihenfolge). Jacobi-Formel: r_4(n) = 8 * sum_{d|n, 4 nicht teilt d} d
# ---------------------------------------------------------------------------
def r4(n):
    """Jacobi: Anzahl Darstellungen von n als Summe von 4 Quadraten."""
    if n == 0:
        return 1
    s = 0
    for d in range(1, n + 1):
        if n % d == 0 and d % 4 != 0:
            s += d
    return 8 * s


def r3(n):
    """Anzahl Darstellungen von n als Summe von 3 Quadraten (Brute Force).
    Dient zur Pruefung des Beobachter-Mechanismus (Schritt 8)."""
    cnt = 0
    lim = int(math.isqrt(n))
    for a in range(-lim, lim + 1):
        for b in range(-lim, lim + 1):
            r = n - a * a - b * b
            if r < 0:
                continue
            c = int(math.isqrt(r))
            if c * c == r:
                cnt += (1 if c == 0 else 2)
    return cnt


# ---------------------------------------------------------------------------
# Schritt 2: spektrale Dichte I(r) = g(r) * <N(r)> * r
# mit Bose-Einstein-Besetzung <N(r)> = 1/(e^r - 1), r = |n| = sqrt(|n|^2)
# ---------------------------------------------------------------------------
def spectral_density(n2):
    r = math.sqrt(n2)
    g = r4(n2)
    N = 1.0 / (math.exp(r) - 1.0)
    return g * N * r


def is_local_max(n2, table):
    """Lokales Maximum, wenn I(n2) groesser als beide Nachbarn."""
    I = table[n2]
    left = table.get(n2 - 1, 0.0)
    right = table.get(n2 + 1, 0.0)
    return I > left and I > right


print("=" * 72)
print("CMB-Akustikpeaks aus der T4-Gitterstruktur (FFGFT)")
print("=" * 72)
print(f"xi = 1/7500 = {xi:.6e}")
print(f"D_f = 3 - xi = {D_f:.8f}")
print()

# ---------------------------------------------------------------------------
# Schritt 1+2: Tabelle der spektralen Dichte, lokale Maxima finden
# ---------------------------------------------------------------------------
NMAX = 90
table = {n2: spectral_density(n2) for n2 in range(1, NMAX + 1)}

print("Schritt 1+2: Spektrale Dichte I(|n|^2) = g * <N> * |n|")
print("-" * 72)
print(f"{'|n|^2':>6} {'|n|':>8} {'g=r4':>6} {'<N>':>9} {'I':>9} {'lok.Max':>8}")
for n2 in range(1, 31):
    r = math.sqrt(n2)
    g = r4(n2)
    N = 1.0 / (math.exp(r) - 1.0)
    I = table[n2]
    mark = "  <--" if is_local_max(n2, table) else ""
    print(f"{n2:>6} {r:>8.4f} {g:>6} {N:>9.4f} {I:>9.3f} {mark:>8}")
print()

peaks = [n2 for n2 in range(1, NMAX + 1) if is_local_max(n2, table)]
print(f"Lokale Maxima (T4-Peaks) bis |n|^2={NMAX}:")
print(f"  {peaks}")
print()

# ---------------------------------------------------------------------------
# Schritt 4/5: dominante Grundpeaks
# ---------------------------------------------------------------------------
grund = [1, 6, 14, 26]
print("Schritt 4/5: dominante T4-Grundpeaks |n|^2 = 1, 6, 14, 26")
print("-" * 72)
for n2 in grund:
    in_peaks = "Peak" if n2 in peaks else "(kein lok. Max, aber Grundmode)"
    print(f"  |n|^2 = {n2:2d}: I = {table[n2]:7.3f}   {in_peaks}")
print()

# ---------------------------------------------------------------------------
# Schritt 8: Faktor 3 -- SETZUNG (R139 i)
# Frueher: "Beobachter in 3D misst k_obs^2 = n1^2+n2^2+n3^2 -> Faktor 3".
# Das traegt nicht: die projizierte Wellenzahl ist nie groesser als die volle,
# k_obs^2 <= |n|^2. Eine Projektion kann |n|^2 = {1,6,14,26} nicht auf
# {3,18,42,78} VERGROESSERN. Der Faktor 3 ist daher eine Setzung.
# ---------------------------------------------------------------------------
print("Schritt 8: Faktor 3 -- Setzung, nicht aus Projektion (R139 i)")
print("-" * 72)
n_sym = (1, 1, 1, 0)
k_obs2 = n_sym[0]**2 + n_sym[1]**2 + n_sym[2]**2
print(f"    n = {n_sym}: |n|^2 = {sum(x*x for x in n_sym)}, k_obs^2 = n1^2+n2^2+n3^2 = {k_obs2}")
# Pruefung: fuer jede Mode mit |n|^2 in {1,6,14,26} gilt k_obs^2 <= |n|^2
for n2g in [1, 6, 14, 26]:
    lim = int(math.isqrt(n2g))
    kmax = 0
    for v in product(range(-lim, lim + 1), repeat=4):
        if sum(x * x for x in v) == n2g:
            kmax = max(kmax, v[0]**2 + v[1]**2 + v[2]**2)
    assert kmax <= n2g < 3 * n2g
    print(f"    |n|^2 = {n2g:2d}: max k_obs^2 ueber alle Moden = {kmax:2d}  (<= |n|^2, nie 3*|n|^2 = {3*n2g})")
print("    -> Die Projektion kann den Faktor 3 NICHT erzeugen; Faktor 3 = SETZUNG.")
print()

sichtbar = [3 * g for g in grund]
print(f"  Sichtbare Serie: 3 * {grund} = {sichtbar}")
print()

# Pruefung: sind die sichtbaren Werte echte T4-Peaks?
print("  Sind |n|^2 = 3,18,42,78 echte lokale Maxima?")
for n2 in sichtbar:
    mark = "JA" if is_local_max(n2, table) else "nein"
    print(f"    |n|^2 = {n2:2d}: I = {table[n2]:7.3f}, lokales Maximum: {mark}")
print()

# ---------------------------------------------------------------------------
# Schritt 3+5: Verhaeltnisse ell proportional sqrt(|n|^2)
# ---------------------------------------------------------------------------
print("Schritt 3+5: Peak-Verhaeltnisse ell proportional sqrt(|n|^2)")
print("-" * 72)
ref = math.sqrt(sichtbar[0])
ratios = [math.sqrt(n2) / ref for n2 in sichtbar]
cmb = [220.0, 537.0, 810.0, 1120.0]
cmb_ratios = [x / cmb[0] for x in cmb]

print(f"{'Peak':>5} {'|n|^2':>6} {'sqrt':>8} {'Verh.':>8} {'CMB-Verh.':>10} {'Abw.':>8}")
for i, n2 in enumerate(sichtbar):
    dev = (ratios[i] - cmb_ratios[i]) / cmb_ratios[i] * 100
    print(f"{i+1:>5} {n2:>6} {math.sqrt(n2):>8.4f} "
          f"{ratios[i]:>8.4f} {cmb_ratios[i]:>10.4f} {dev:>+7.2f}%")
print()

ratio_str = " : ".join(f"{x:.3f}" for x in ratios)
cmb_str = " : ".join(f"{x:.3f}" for x in cmb_ratios)
print(f"  FFGFT (T4): {ratio_str}")
print(f"  CMB:        {cmb_str}")
maxdev = max(abs((ratios[i] - cmb_ratios[i]) / cmb_ratios[i] * 100)
             for i in range(4))
print(f"  Maximale Abweichung: {maxdev:.2f} %  (Folge abgelesen, Faktor 3 gesetzt -- Retrodiktion)")
print()

# ---------------------------------------------------------------------------
# Befund
# ---------------------------------------------------------------------------
print("=" * 72)
print("BEFUND")
print("=" * 72)
print(f"""
1. Die spektrale Dichte I(r) = g * <N> * r (Jacobi-Entartung, Bose-
   Einstein) enthaelt xi NICHT. Ihre lokalen Maxima sind dicht
   ({{3,6,10,14,...}}); die Folge {{1,6,14,26}} ist aus den gemessenen
   CMB-Verhaeltnissen abgelesen (Retrodiktion). Die Peak-Selektion ist offen.

2. Der Faktor 3 ist eine SETZUNG (R139 i): eine Projektion auf drei
   Raumrichtungen liefert k_obs^2 <= |n|^2 und kann {{1,6,14,26}} nicht auf
   {{3,18,42,78}} vergroessern.

3. Die Verhaeltnisse 1 : {ratios[1]:.3f} : {ratios[2]:.3f} : {ratios[3]:.3f}
   stimmen mit den CMB-Peaks 1 : {cmb_ratios[1]:.3f} : {cmb_ratios[2]:.3f} : {cmb_ratios[3]:.3f}
   auf < {math.ceil(maxdev)}% ueberein -- als Retrodiktion mit abgelesener Folge
   und gesetztem Faktor 3, kein parameterfreier Beleg.

4. Gegenstand sind nur die Verhaeltnisse (s. 1-3). Die absolute Position
   (ell_1 ~ 220) braucht einen externen Parameter (P20, Dok. 190);
   sie ist nicht Gegenstand dieses Skripts.

5. Offen (P30): die strenge sphaerische Projektion der T4-Moden auf das
   Winkelleistungsspektrum C_ell mit sphaerischen Bessel-Funktionen.
   Die naive Bessel-Projektion (naive_bessel_projektion.py) reproduziert
   die Peaks nicht; P30 bleibt offen.

Bezug: Dok. 268 (CMB-Peaks aus T4), Dok. 267 (kosmologische Entartung),
       Dok. 190 (P14, P20, P29, P30), Dok. 025 (T_CMB aus xi).
""")
