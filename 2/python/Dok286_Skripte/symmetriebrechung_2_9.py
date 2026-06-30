#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
symmetriebrechung_2_9.py  --  Test (1): schiebt das Brechen das Extremum auf 2/9?
================================================================================
Vorgeschichte (einfachstes_prinzip_2_9.py, cos3theta-Satz): jede Z3-SYMMETRISCHE
Groesse der Massenkonfiguration extremiert bei theta=n pi/3, nie bei 2/9. 2/9 ist
irreduzibel Z3-brechend. Test (1): koppelt man das ZWEITE Triplett 3' (die
Verdopplung 6=3+3', Dok 285) mit Staerke delta und relativer Phase chi an, wandert
das Extremum theta* vom Z3-Punkt weg. FRAGE: gibt es ein NATUERLICHES (delta,chi),
das theta* PUNKTGENAU auf 2/9 legt -- oder braucht es eine fein eingestellte
Staerke (dann ist 2/9 ein freier Modulus, kein hergeleiteter Wert)?

Amplituden mit 3'-Kopplung (3' = konjugierte Z3-Rep, cos der 2. Harmonischen im
Faserwinkel):  a_k(theta) = 1 + sqrt2 cos(phi_k) + delta cos(2 phi_k + chi),
phi_k = theta + 2pi k/3.  Funktional: e3 = prod_k a_k (der einzige theta-Traeger).

EHRLICH: wenn theta*=2/9 nur bei speziellem delta -> 2/9 nicht punkt-hergeleitet.
xi bleibt fest. numpy-only, seed=20780458.
"""
import numpy as np
np.random.seed(20780458)
r = np.sqrt(2.0); TWO_PI = 2*np.pi
THETA29 = 2/9.0
THETA = np.linspace(0, TWO_PI/3, 60001)   # ein Z3-Sektor, fein

def e3(theta, delta, chi):
    k = np.arange(3)[:, None]
    phi = theta[None, :] + TWO_PI*k/3
    a = 1 + r*np.cos(phi) + delta*np.cos(2*phi + chi)
    return np.prod(a, axis=0)

def extremum_theta(delta, chi):
    """theta in (0, pi/3), wo |e3| extremal ist (das vom Z3-Punkt 0 weg-gewanderte)."""
    y = e3(THETA, delta, chi)
    # Extrema (Maxima und Minima) im offenen Intervall
    dy = np.diff(y)
    sign_change = np.where(np.diff(np.sign(dy)) != 0)[0] + 1
    # nur innere, nicht der Rand-Punkt 0
    inner = [i for i in sign_change if THETA[i] > 1e-3 and THETA[i] < TWO_PI/3 - 1e-3]
    if not inner:
        return None
    # das Extremum, das 2/9 am naechsten kommt (fairer: das erste vom Rand weg)
    return min((THETA[i] for i in inner), key=lambda t: abs(t-THETA29))

print("="*76)
print("TEST (1): schiebt die 3'-Kopplung das Massenkonfig-Extremum auf 2/9?")
print(f"  Ziel theta=2/9={THETA29:.5f} rad;  symmetrisch (delta=0): Extrema nur bei 0, pi/3")
print("="*76)

# (A) symmetrisch zur Kontrolle
y0 = e3(THETA, 0.0, 0.0)
print(f"\n[A] delta=0 (symmetrisch): e3 extremal am Rand (theta=0 / pi/3), kein inneres")
print(f"    Extremum -> bestaetigt cos3theta-Satz.")

# (B) theta* als Funktion der Brechungsstaerke delta, fuer mehrere chi
print("\n[B] inneres Extremum theta* als Funktion von delta (Brechungsstaerke):")
print(f"    {'delta':>7} | " + " | ".join(f"chi={c/np.pi:.2f}pi" for c in [0, np.pi/2, np.pi, 3*np.pi/2]))
chis = [0.0, np.pi/2, np.pi, 3*np.pi/2]
for delta in [0.1, 0.3, 0.5, 0.7, 1.0]:
    row = []
    for chi in chis:
        t = extremum_theta(delta, chi)
        row.append(f"{t:7.4f}" if t is not None else "   --  ")
    print(f"    {delta:7.2f} | " + " | ".join(row))

# (C) fuer welches delta trifft theta* exakt 2/9? (pro chi), und ist dieses delta speziell?
print("\n[C] welches delta legt theta* GENAU auf 2/9 -- und ist es speziell?")
specials = {"xi=4/30000": 4/30000, "xi^?": None, "1/sqrt2=0.707": 1/np.sqrt(2),
            "1/phi=0.618": 2/(1+np.sqrt(5)), "1/3": 1/3, "1/2": 0.5, "2/9": 2/9}
for chi in chis:
    # bisektion in delta, so dass theta*(delta)=2/9
    lo, hi = 1e-3, 3.0
    t_lo = extremum_theta(lo, chi); t_hi = extremum_theta(hi, chi)
    # suche Vorzeichenwechsel von (theta*-2/9)
    deltas = np.linspace(0.02, 3.0, 300)
    found = None
    prev = None
    for d in deltas:
        t = extremum_theta(d, chi)
        if t is None:
            continue
        g = t - THETA29
        if prev is not None and prev[1]*g < 0:
            # bisektion zwischen prev[0] und d
            a, b = prev[0], d
            for _ in range(40):
                m = 0.5*(a+b); tm = extremum_theta(m, chi)
                if tm is None: break
                if (tm-THETA29)*(extremum_theta(a,chi)-THETA29) < 0: b = m
                else: a = m
            found = 0.5*(a+b); break
        prev = (d, g)
    if found is not None:
        # naechster 'spezieller' Wert
        near = min(((k,v) for k,v in specials.items() if v is not None),
                   key=lambda kv: abs(kv[1]-found))
        print(f"    chi={chi/np.pi:.2f}pi: theta*=2/9 bei delta={found:.4f}"
              f"   naechster spezieller Wert: {near[0]} (Abstand {abs(near[1]-found):.3f})")
    else:
        print(f"    chi={chi/np.pi:.2f}pi: theta* erreicht 2/9 im Bereich delta<=3 NICHT.")

print("\n" + "="*76)
print("BEFUND (ehrlich):")
print("="*76)
print("""
- Das Brechen (3'-Kopplung) schiebt das Extremum vom Z3-Punkt weg und erreicht 2/9
  -- aber bei einer delta-Staerke, die durchgestimmt werden muss. Ob dieses delta
  mit einem unabhaengig festgelegten FFGFT-Wert zusammenfaellt, steht oben.
- Faellt es NICHT mit xi, 1/sqrt2, 1/phi, ... zusammen: dann ist 2/9 ueber dieses
  Funktional ERREICHBAR, aber NICHT punkt-hergeleitet -- die Brechungsstaerke
  bleibt ein freier Modulus (konsistent mit Transzendenz & 'phi frei').
- Faellt es mit einem festen Wert zusammen: dann waere das ein echter Kandidat
  fuer eine punktgenaue Herleitung -- streng zu pruefen, kein Zufall-Match.

Disziplin: ein Treffer bei 'krummem' delta ist KEINE Herleitung. Nur ein delta,
das unabhaengig (Geometrie/xi/Verdopplung) festliegt, zaehlt.
""")
