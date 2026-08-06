#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FFGFT — Skalenanalyse der Leichtelement-Observablen
====================================================

Frage: Sind die BBN-Observablen "heutige Laborwerte, unbesehen an einen
anderen Ort des Zyklus transportiert" — oder sind sie ortsinvariant?

Befund (Teil A): Y_p haengt ausschliesslich von zwei DIMENSIONSLOSEN
Groessen ab (Q/T_f und t/tau_n). Eine durchgehende Massenskalierung
ist kein anderer Zustand, sondern ein Einheitenwechsel -- es gibt
kein externes Lineal. Y_p ist daher gegen sie trivial invariant.

Befund (Teil B): Was allein zaehlt, ist die Abhaengigkeit von xi.
In einer Ein-Parameter-Theorie ist jede dimensionslose Groesse eine
Funktion von xi allein, also Y_p = Y_p(xi). Bei eingefrorenem xi
(Faelle A/B der Schliessungsgabelung) ist Y_p ortsinvariant, ohne
Zusatzannahme. Nur ein laufendes xi (Fall C) aendert es.

Befund (Teil C, und das ist die eigentliche Antwort): WEDER Y_p NOCH
Li-7 sind belastbare Groessen. Y_p sieht dimensionslos aus, aber T_f
folgt aus dem Modell und t/tau_n ist eine Dauer; Li-7 haengt an eta,
an der Fensterdauer und an Sternatmosphaerenmodellen. Die Rechnung in
Teil A ist daher eine Implikation, keine Pruefflaeche -- BBN taugt
nicht als Test gegen die Kritik an der Rueckwaertsextrapolation,
sondern ist ein Fall dieser Kritik.

Nicht-Befund (ausdruecklich): G und alpha sind KEINE unabhaengigen
Skalen, die gegen die Massen driften koennten -- G = xi^2/(4 m_char)
(Dok. 012) und alpha = xi E_0^2 (Dok. 011) sind aus xi abgeleitet.
Ihre SI-Werte brauchen eine Verankerung; Verankerung ist Umrechnung,
nicht Anpassung (A040-Regel, R72). Sie taugen deshalb nicht als
eigenstaendige Bruchstellen.

Abhaengigkeiten: mpmath. Deterministisch.
Stand: 5. August 2026
"""
from mpmath import mp, mpf, exp, log, power

mp.dps = 15

# Heutige Laborwerte (Referenzpunkt, NICHT als ortsunabhaengig unterstellt)
Q_LAB   = mpf('1.293')    # MeV, m_n - m_p
TF_LAB  = mpf('0.8')      # MeV, Ausfriertemperatur
TAU_LAB = mpf('879.4')    # s, Neutronenlebensdauer
TD_LAB  = mpf('250')      # s, Verzoegerung bis zur Deuteriumbildung


def Yp(QT, t_over_tau):
    """Helium-4-Massenanteil aus zwei dimensionslosen Groessen.
    QT          = Q / T_f       (Ausfrierverhaeltnis)
    t_over_tau  = t_D / tau_n   (Zerfallsanteil)
    Toy-Modell: reproduziert die Struktur, nicht die Praezision."""
    r = exp(-QT) * exp(-t_over_tau)      # n/p nach Ausfrieren und Zerfall
    return 2 * r / (1 + r)


# ============================================================
# TEIL A — Skalenexponenten unter m -> lambda * m
# ============================================================
# Annahme: ALLE Massenskalen skalieren gemeinsam (Q, v, M_Pl).
#   Q     ~ lam^1     (Massendifferenz)
#   G_F   ~ 1/v^2     -> lam^-2
#   M_Pl  ~ lam^1
# Ausfrieren aus Ratengleichheit  G_F^2 T^5 = T^2 / M_Pl:
#   T_f^3 = 1/(G_F^2 M_Pl)
# Neutronenlebensdauer  tau_n ~ 1/(G_F^2 Q^5)
# Hubble-Zeit           t     ~ M_Pl / T^2
e_Q, e_v, e_MPl = 1, 1, 1
e_GF   = -2 * e_v
e_Tf   = -(2 * e_GF + e_MPl) / 3
e_taun = -(2 * e_GF + 5 * e_Q)
e_t    = e_MPl - 2 * e_Tf

assert e_Tf == 1,   e_Tf          # T_f skaliert wie die Massen
assert e_taun == -1, e_taun
assert e_t == -1,    e_t
assert e_Q - e_Tf == 0            # Q/T_f invariant
assert e_t - e_taun == 0          # t/tau_n invariant

print("TEIL A - Skalenexponenten unter m -> lam*m (Einheitenwechsel)")
print(f"  Q ~ lam^{e_Q}   G_F ~ lam^{e_GF}   M_Pl ~ lam^{e_MPl}")
print(f"  T_f ~ lam^{e_Tf:.0f}   tau_n ~ lam^{e_taun:.0f}   t ~ lam^{e_t:.0f}")
print(f"  => Q/T_f ~ lam^0 und t/tau_n ~ lam^0  -> Y_p INVARIANT")

QT0 = Q_LAB / TF_LAB
TT0 = TD_LAB / TAU_LAB
print(f"  Referenz: Q/T_f = {float(QT0):.4f}, t/tau = {float(TT0):.4f}"
      f"  ->  Y_p = {float(Yp(QT0, TT0)):.4f}   (beobachtet ~0.245)\n")

# ============================================================
# TEIL B — Diskriminator: ungleichfoermige Skalierung
# ============================================================
# Faellt T_f mit Exponent a != 1 aus, gilt Q/T_f ~ lam^(1-a).
print("TEIL B0 - Kontrollrechnung: a != 1 waere kein Ortseffekt,")
print("          sondern ein inkonsistenter Einheitenwechsel")
print(f"{'lam':>7} {'a=1.0':>9} {'a=0.9':>9} {'a=1.1':>9} {'a=0.5':>9}")
for lam in [mpf('1'), mpf('0.5'), mpf('0.1'), mpf('0.01')]:
    vals = []
    for a in [mpf(1), mpf('0.9'), mpf('1.1'), mpf('0.5')]:
        vals.append(float(Yp(QT0 * power(lam, 1 - a), TT0)))
    print(f"{float(lam):>7} " + " ".join(f"{v:>9.4f}" for v in vals))
# Kontrolle: bei a = 1 ist Y_p exakt konstant
for lam in [mpf('0.5'), mpf('0.01')]:
    assert abs(Yp(QT0 * power(lam, 0), TT0) - Yp(QT0, TT0)) < mpf('1e-12')

h = mpf('1e-6')
sens = (log(Yp(QT0 + h, TT0)) - log(Yp(QT0 - h, TT0))) / (2 * h) * QT0
print(f"  Empfindlichkeit d lnY_p / d ln(Q/T_f) = {float(sens):.3f}")
print(f"  -> Y_p auf 1% gemessen legt Q/T_f auf "
      f"{1/abs(float(sens)):.1f}% fest\n")

# ============================================================
# TEIL C — Warum Li-7 anders liegt als Y_p
# ============================================================
# Y_p:  bestimmt durch VERHAELTNISSE (Q/T_f, t/tau) -> invariant.
# D/H und Li/H: bestimmt durch eta = n_B/n_gamma und durch die DAUER
#   des Fensters. eta ist ein Verhaeltnis zweier Teilchenzahlen, also
#   nicht durch Massenskalierung fixiert; die Fensterdauer erst recht
#   nicht. Beide fallen daher NICHT unter das Invarianzargument.
print("TEIL C - Einordnung der drei Observablen")
tab = [
    ("Y_p  (He-4)", "Q/T_f, t/tau_n", "gemischt", "NICHT belastbar"),
    ("D/H",         "eta, Fensterlage", "Zahl + Modell", "nicht belastbar"),
    ("Li-7/H",      "eta, Fensterdauer", "Zahl + Dauer", "nicht belastbar"),
]
print(f"  {'Observable':<13} {'haengt ab von':<20} {'Typ':<17} Status")
for n, d_, ty, st in tab:
    print(f"  {n:<13} {d_:<20} {ty:<17} {st}")
print("""
  WICHTIGE EINSCHRAENKUNG (Korrektur an der naheliegenden Lesart):
  Y_p ist zwar ein dimensionsloses ERGEBNIS, aber seine Zutaten sind
  es nicht durchgehend:
    - T_f ist NICHT gemessen, sondern folgt aus einer Ratengleichung
      mit H, also aus dem kosmologischen Modell.
    - t/tau_n enthaelt eine DAUER (Fensterlage).
  Y_p ist damit ein Gemisch aus Struktur- und Modellgroessen, kein
  reines Verhaeltnis gleicher Ebene wie m_mu/m_e oder alpha.

  Folgerung: Das Invarianzargument aus Teil A ist eine IMPLIKATION
  ("faellt das Modell so aus, kuerzt sich das Verhaeltnis heraus"),
  KEINE Pruefflaeche. Y_p ist keine Ausnahme von der Kritik an der
  Rueckwaertsextrapolation, sondern ein Fall davon.

  Li-7 erst recht: eta (Zahl), Fensterdauer (Dauer) und zusaetzlich
  Sternatmosphaerenmodelle bei der Messung -- drei Modellschichten
  uebereinander. Die Faktor-3-Diskrepanz zeigt darum, dass irgendwo
  in der Kette etwas nicht stimmt, aber nicht wo. Die Korpusposition
  (Dok. 025/063: Nukleosynthese ohne feste Zeitschranke) setzt an
  der Fensterdauer an; eine quantitative Li-7-Vorhersage folgt
  daraus NICHT.

  Belastbar im strengen Sinn bleiben nur Groessen ohne Skalenbruecke
  und ohne Dauer: Zaehlungen (1152, 24, 9) und reine Verhaeltnisse
  gleicher Ebene (alpha, m_mu/m_e, Koide Q). BBN-Observable gehoeren
  NICHT dazu.""")



# ============================================================
# TEIL D — Die einzige verbleibende Bruchstelle: laufendes xi
# ============================================================
# In einer Ein-Parameter-Theorie ist jede dimensionslose Groesse
# Funktion von xi allein.  Also  Y_p = Y_p(xi).
#   Faelle A/B (xi eingefroren): Y_p ortsinvariant.  Ende.
#   Fall C (xi laeuft):          Y_p aendert sich -- und zwar
#                                berechenbar, sobald der Exponent
#                                p = dln(Q/T_f)/dln(xi) bekannt ist.
# p ist aus dem hier verwendeten Material NICHT ableitbar und wird
# darum parametrisiert (Status: offen, nicht behauptet).

print("\n" + "=" * 62)
print("TEIL D - Einzige Bruchstelle: laufendes xi (Fall C)")
print("=" * 62)

XI0 = mpf(1) / 7500
SENS = -mpf('1.40607')          # dlnY_p/dln(Q/T_f), Teil B

def xi_n(n):
    """Rekursion aus Dok. 295: xi_n ~ 1/(100(n+75))."""
    return mpf(1) / (100 * (n + 75))

assert abs(xi_n(0) - XI0) < mpf('1e-18')
assert abs(xi_n(75) / XI0 - mpf('0.5')) < mpf('1e-15')

print("\nxi-Drift laengs der Rekursion (Fall C):")
print(f"  {'n':>4} {'xi_n/xi_0':>11} {'ln(xi_n/xi_0)':>15}")
for n in [0, 1, 5, 25, 75]:
    r = xi_n(n) / XI0
    print(f"  {n:>4} {float(r):>11.5f} {float(log(r)):>15.5f}")

print("\nY_p-Drift, parametrisiert nach p = dln(Q/T_f)/dln(xi):")
print(f"  {'n':>4} " + " ".join(f"{'p='+str(pp):>10}" for pp in
                                ['0', '0.25', '1', '2']))
for n in [1, 5, 25, 75]:
    dlnxi = log(xi_n(n) / XI0)
    row = []
    for pp in [mpf(0), mpf('0.25'), mpf(1), mpf(2)]:
        row.append(float(Yp(QT0 * exp(pp * dlnxi), TT0)))
    print(f"  {n:>4} " + " ".join(f"{v:>10.4f}" for v in row))
print("  -> p = 0: nichts passiert. Jedes p != 0 laesst Y_p driften.")

# Wieviel Drift erlaubt die Beobachtung?
#   Y_p ist auf ~1% gemessen -> |dlnY_p| < 0.01
#   |dln(Q/T_f)| < 0.01/|SENS|
print("\nSchranke aus der Beobachtung (Y_p auf 1% gemessen):")
tol = mpf('0.01') / abs(SENS)
print(f"  |dln(Q/T_f)| < {float(tol):.5f}")
print(f"  {'n':>4} {'|dln xi|':>10} {'|p| <':>10}")
for n in [1, 5, 25, 75]:
    d = abs(log(xi_n(n) / XI0))
    print(f"  {n:>4} {float(d):>10.5f} {float(tol / d):>10.4f}")
assert tol / abs(log(xi_n(75) / XI0)) < mpf('0.02')
print("""
  Lesart: Traefe Fall C zu und lieferte die beobachtete Epoche
  n ~ 75 Praezessionsrunden, so waere |p| < 0.011 erzwungen --
  d.h. Q/T_f muesste nahezu xi-unabhaengig sein. Das ist eine
  harte, pruefbare Forderung an Fall C; sie faellt in den Faellen
  A/B ersatzlos weg.

  Status: p ist hier NICHT bestimmt. Die Rechnung zeigt nur, dass
  die gesamte Frage auf diesen einen Exponenten zusammenschnurrt --
  und dass G und alpha als Bruchstellen ausscheiden, weil sie aus
  xi abgeleitet sind und nicht unabhaengig driften koennen.""")

print("\nAlle Kontrollen bestanden.")
