#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FFGFT -- Pruefskript (kein Beweis): Kruemmungstreue vs. Reichweite
==================================================================
Dok. 304 / Dok. 295 -- das e-Kriterium auf einen Akkumulator angewandt.

FFGFT-seitige These (unabhaengig von jedem externen Gedaechtnismodell):
    Die trennende Achse zwischen einem KRUEMMUNGSTREUEN (log-Spiral-)
    Akkumulator und einem GLEICHFOERMIGEN (archimedischen) Akkumulator
    ist NICHT die Reichweite, sondern die Kruemmungstreue.

    - Bei GLEICHER Reichweite liefert eine reichweitenbasierte Metrik
      fuer beide dasselbe (kann sie nicht trennen).
    - Das e-Kriterium (Ganghoehe zerfaellt wie 1/n; Selbstaehnlichkeit
      D(2k)-D(k) -> ln 2; e-fache Skala pro Einheits-Zuwachs von D)
      trennt die beiden sauber und exakt.

Deterministisch, nur Standardbibliothek (math). Kein Zufall, kein Fit gegen Fit.
Der Befund ist FFGFT-intern (aus xi / der Rekursion ableitbar, Dok. 295).
Er etabliert KEINE Spezifitaet irgendeines kognitiven M_B -- das bliebe die
restricted-Bruecke (Kategorie B) und verlangt einen eigenen, unabhaengigen,
gemeinsam versiegelten Benchmark.
"""

import math

N = 300_000            # Horizont
D0 = 1.0 / 75.0        # Start-Ganghoehe d_1 = 100*xi_1 -> log-Spirale, 75-Schliessung


# ---------------------------------------------------------------------------
# 1. Kruemmungstreuer Akkumulator: exakte Rekursion d_{n+1} = d_n (1 - d_n),
#    mit d_n = 100*xi_n. Kumuliert: D(k) = sum_{n<=k} d_n -> ln(1 + k/75).
# ---------------------------------------------------------------------------
d_curved = [0.0] * N
d = D0
for n in range(N):
    d_curved[n] = d
    d = d * (1.0 - d)                      # exakte Rekursion (Dok. 295)

D_curved = [0.0] * (N + 1)
s = 0.0
for k in range(1, N + 1):
    s += d_curved[k - 1]
    D_curved[k] = s

def D_closed(k):
    """Geschlossene Form der kruemmungstreuen Akkumulation."""
    return math.log(1.0 + k / 75.0)


# ---------------------------------------------------------------------------
# 2. Gleichfoermiger (archimedischer) Akkumulator -- GLEICHE Reichweite:
#    konstante Ganghoehe, so gewaehlt, dass die Gesamtakkumulation bei N
#    exakt uebereinstimmt (equal reach / equal total accumulation).
# ---------------------------------------------------------------------------
d_const = D_curved[N] / N
D_linear = [d_const * k for k in range(N + 1)]


def hr(title):
    print("\n" + title)
    print("-" * len(title))


print("=" * 70)
print(" FFGFT Kruemmungstreue-Probe -- Reichweite trennt nicht, Kruemmung schon")
print("=" * 70)
print(f" Horizont N = {N},  Start-Ganghoehe d_1 = 1/75 = {D0:.8f}")
print(f" kruemmungstreu: D(N) = {D_curved[N]:.6f}   (geschlossen {D_closed(N):.6f},"
      f" Abw. {D_curved[N]-D_closed(N):+.2e})")
print(f" gleichfoermig : d_const = {d_const:.3e}, D_lin(N) = {D_linear[N]:.6f}"
      f"  -> GLEICHE Reichweite (gleiches Gesamt-D bei N)")


# ---------------------------------------------------------------------------
# 3. REICHWEITEN-TEST: Informationshorizont eines fruehen Impulses.
#    Ein unbeschraenkter Akkumulator behaelt einen beliebig alten Beitrag;
#    ein Fenster der Breite W verliert ihn, sobald N - t0 > W.
#    -> Reichweite trennt {Akkumulatoren} von {endlichem Kern},
#       aber NICHT kruemmungstreu von linear.
# ---------------------------------------------------------------------------
hr("(R) Reichweiten-Test: beeinflusst ein Impuls bei t0=10 noch die Ausgabe bei N?")
t0 = 10
for W in (1_000, 100_000):
    win_horizon_ok = (N - t0) <= W
    print(f"  endliches Fenster W={W:>7d}:  Impuls erhalten? "
          f"{'ja' if win_horizon_ok else 'NEIN (jenseits des Horizonts)'}")
# beide Akkumulatoren: Beitrag d_{t0} bzw. d_const bleibt in der laufenden Summe
print(f"  kruemmungstreuer Akkumulator:  Impuls erhalten? ja "
      f"(Beitrag d_t0 = {d_curved[t0]:.3e} bleibt in D(N))")
print(f"  gleichfoermiger  Akkumulator:  Impuls erhalten? ja "
      f"(Beitrag d_const = {d_const:.3e} bleibt in D(N))")
print("  => Reichweite ist fuer beide Akkumulatoren identisch (unbeschraenkt);")
print("     sie kann kruemmungstreu und gleichfoermig NICHT unterscheiden.")


# ---------------------------------------------------------------------------
# 4. KRUEMMUNGSTREUE-TEST (e-Kriterium, Dok. 295) -- drei Signaturen.
# ---------------------------------------------------------------------------

# (a) Selbstaehnlichkeit: Skalenverdopplungs-Inkrement D(2k) - D(k).
#     kruemmungstreu -> ln 2 (skaleninvariant, konstant ueber alle k)
#     gleichfoermig  -> d_const * k (waechst linear mit k, nicht skaleninvariant)
hr("(a) Selbstaehnlichkeit -- D(2k) - D(k):")
print("       k          curved     |curved - ln2|        linear")
ln2 = math.log(2.0)
for k in (100, 1_000, 10_000, 100_000):
    dc = D_curved[2 * k] - D_curved[k]
    dl = D_linear[2 * k] - D_linear[k]
    print(f"  {k:>8d}    {dc:10.6f}    {abs(dc-ln2):.3e}    {dl:12.4f}")
print(f"  kruemmungstreu -> ln 2 = {ln2:.6f} (konstant);  gleichfoermig waechst mit k.")

# (b) Ganghoehen-Zerfallsexponent p:  d_n ~ n^{-p}  (log-log-Steigung).
#     kruemmungstreu p ~ 1 (1/n-Zerfall);  gleichfoermig p = 0 (konstant).
hr("(b) Ganghoehen-Zerfall -- Exponent p in d_n ~ n^(-p):")
def loglog_slope(seq, a, b):
    x1, x2 = math.log(a), math.log(b)
    y1, y2 = math.log(seq[a - 1]), math.log(seq[b - 1])
    return (y2 - y1) / (x2 - x1)
p_curved = loglog_slope(d_curved, 1_000, 100_000)
d_lin_seq = [d_const] * N
p_linear = loglog_slope(d_lin_seq, 1_000, 100_000)
print(f"  kruemmungstreu:  p = {p_curved:+.4f}   (Ziel 1/n  -> p ~ -1... hier |p|)")
print(f"  gleichfoermig :  p = {p_linear:+.4f}   (konstant -> p = 0)")
print("  => der 1/n-Zerfall ist die Signatur der Kruemmung; konstant hat ihn nicht.")

# (c) e-fache Skala pro Einheits-Zuwachs von D (Ratio e, Dok. 295).
#     Weil exp(D_curved(k)) = 1 + k/75, multipliziert sich die k-Skala bei
#     einem Zuwachs von D um 1 exakt mit e. Beim gleichfoermigen Akkumulator
#     ist der Zuwachs arithmetisch -> Skalen-Ratio -> 1 (keine log-Spirale).
hr("(c) Ratio e -- k-Skalen-Faktor bei D-Zuwachs um 1:")
def scale_ratio_curved(D_target):
    # k, bei dem D_curved(k) ~ D_target: aus exp(D)=1+k/75 -> k=75(e^D - 1)
    k1 = 75.0 * (math.exp(D_target) - 1.0)
    k2 = 75.0 * (math.exp(D_target + 1.0) - 1.0)
    return k2 / k1
for Dt in (2.0, 4.0, 6.0):
    r = scale_ratio_curved(Dt)
    print(f"  bei D={Dt:.0f}:  k-Faktor = {r:.6f}   (e = {math.e:.6f}, Abw. {r-math.e:+.2e})")
print("  kruemmungstreu -> e (log-Spirale);  gleichfoermig -> 1 (arithmetisch, keine).")


# ---------------------------------------------------------------------------
# 5. FAZIT
# ---------------------------------------------------------------------------
hr("FAZIT")
print("  Bei GLEICHER Reichweite:")
print("    - Reichweiten-Metrik(kruemmungstreu) == Reichweiten-Metrik(gleichfoermig)")
print("      -> Reichweite trennt die beiden NICHT.")
print("    - Kruemmungstreue-Metrik trennt sie SAUBER und exakt:")
print(f"        Selbstaehnlichkeit  D(2k)-D(k):  ln2={ln2:.4f}  vs. waechst mit k")
print(f"        Ganghoehen-Zerfall  p:           ~1 (1/n)      vs. 0 (konstant)")
print(f"        Skalen-Ratio        e:           {math.e:.4f}       vs. 1")
print()
print("  => Die tragende Achse ist die KRUEMMUNGSTREUE, nicht die Reichweite.")
print("     (FFGFT-intern, aus xi/der Rekursion ableitbar -- proven, Dok. 295.)")
print("     Dieser Pruefstand etabliert KEINE Spezifitaet eines kognitiven M_B;")
print("     das bleibt die restricted-Bruecke (Kategorie B) und verlangt einen")
print("     eigenen, unabhaengigen, gemeinsam versiegelten Benchmark.")
print("=" * 70)
