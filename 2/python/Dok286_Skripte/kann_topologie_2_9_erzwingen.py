#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
kann_topologie_2_9_erzwingen.py  --  letzter Versuch von unserer Seite
======================================================================
Frage: Erzwingt die T^4/Z_3-Topologie den Koide-Offset theta=2/9 von Grund auf?
Konkret (aus eine_fraktale_quelle.py): ist die relative Phase / der Offset durch
eine FLUSS-Quantisierung (Wilson-Linie, Holonomie einer endlichen Gruppe)
festgelegt, oder ein freier kontinuierlicher Modulus?

Korpus-Konvention bestaetigt (Dok 282 Z.197): sqrt(m_k)=M(1+r cos(theta+2 pi k/3)),
theta steht in RADIANT (gleiche Einheit wie 2 pi k/3). Also theta=2/9 rad ~ 0.2222.

Schluessel-Einsicht (zu pruefen): topologische / fluss-quantisierte Phasen sind
EINHEITSWURZELN e^{2 pi i p/q} (rationale Vielfache von 2 pi). theta=2/9 RAD ist
2 pi * (1/(9 pi)) -- und 1/(9 pi) ist irrational. Nach Lindemann-Weierstrass ist
e^{i*2/9} transzendent (e^{i*alpha} fuer algebraisches alpha!=0), also KEINE
Einheitswurzel. Dann kann keine endliche-Gruppen-/Fluss-Topologie theta=2/9 liefern.

numpy-only, seed=20780458.
"""
import numpy as np
from fractions import Fraction
np.random.seed(20780458)

TWO_PI = 2*np.pi
theta = 2/9.0  # RADIANT (Korpus-Konvention)

print("="*76)
print("KANN T^4/Z_3 DEN OFFSET theta=2/9 ERZWINGEN?  (theta in Radiant)")
print("="*76)

# ---------------------------------------------------------------------------
print("\n[1] Ist theta=2/9 rad ein rationales Vielfaches von 2 pi (= Einheitswurzel)?")
ratio = theta/TWO_PI
print(f"    theta/2pi = (2/9)/(2 pi) = 1/(9 pi) = {ratio:.10f}")
# beste rationale Naeherung p/q an theta/2pi, q bis 100000 -> nie exakt
best = Fraction(ratio).limit_denominator(100000)
approx_theta = float(best)*TWO_PI
print(f"    beste Naeherung p/q (q<=1e5): {best}  ->  Phase {approx_theta:.6f} rad")
print(f"    Fehler gegen 2/9: {abs(approx_theta-theta):.3e} rad  (nie 0 -> irrational)")
print(f"    Grund: 1/(9 pi) enthaelt pi (transzendent) -> theta/2pi NICHT rational.")
print(f"    Lindemann-Weierstrass: e^(i*2/9) ist transzendent -> KEINE Einheitswurzel.")

# ---------------------------------------------------------------------------
print("\n[2] Topologische/fluss-quantisierte Phasen sind Einheitswurzeln. Welche")
print("    Z_3- und Z_9-natuerlichen Werte gibt es, und wie weit ist 2/9 davon?")
def dist_to_set(x, S):
    return min(abs(((x-s+np.pi) % TWO_PI) - np.pi) for s in S)
Z3 = [TWO_PI*k/3 for k in range(3)]          # {0, 2pi/3, 4pi/3}
Z9 = [TWO_PI*n/9 for n in range(9)]          # 9.-Einheitswurzeln
print(f"    Z_3 = {{0, 2pi/3, 4pi/3}} = {[f'{s:.4f}' for s in Z3]}")
print(f"    naechster Z_3-Wert zu 2/9 rad: Abstand {dist_to_set(theta,Z3):.4f} rad")
print(f"    naechster Z_9-Wert zu 2/9 rad: Abstand {dist_to_set(theta,Z9):.4f} rad")
# wenn theta '2/9 einer Umdrehung' GEMEINT waere: 2pi*2/9 -- zur Kontrolle:
alt = TWO_PI*2/9
print(f"    (Kontrolle: WAERE theta='2/9 Umdrehung'=4pi/9={alt:.4f} rad, dann EXAKT")
print(f"     ein 9.-Einheitswurzel-Wert, Z_9-Abstand {dist_to_set(alt,Z9):.1e}. Aber das")
print(f"     ist NICHT die Korpus-Konvention -- dort ist theta=2/9 rad.)")

# ---------------------------------------------------------------------------
print("\n[3] Im Z_3-Zirkulant: theta ist die PHASE der komplexen Kopplung (Peierls).")
print("    Reelle Kopplung -> theta=0. Und Q=2/3 ist VON theta unabhaengig:")
def koide_Q(theta, r=np.sqrt(2)):
    k = np.arange(3)
    s = 1 + r*np.cos(theta + TWO_PI*k/3)     # sqrt(m_k) (Vorzeichen unkritisch fuer Q)
    m = s**2
    return m.sum()/ (s.sum()**2)
for th in [0.0, 2/9, 1.0, 2.0]:
    print(f"    Q(theta={th:.3f}, r=sqrt2) = {koide_Q(th):.6f}")
print("    -> Q haengt nur an r (=sqrt2 gibt 2/3), NICHT an theta. Die Z_3+sqrt2-")
print("       Struktur fixiert den NENNER/Q, der Offset theta bleibt frei.")

# ---------------------------------------------------------------------------
print("\n[4] Ehrliche Abgrenzung: das Mode-Locking-2/9 ist NICHT dasselbe 2/9.")
rho = 2/9.0                                   # Rotationszahl (dimensionslos, Zyklen)
rho_as_phase = TWO_PI*rho                     # als Phase
print(f"    Mode-Locking-Rotationszahl rho=2/9 (dimensionslos) entspricht der Phase")
print(f"    2pi*2/9 = {rho_as_phase:.4f} rad -- das ist 4pi/9, NICHT 2/9 rad={theta:.4f}.")
print(f"    rho=2/9 (Zyklen) und Koide theta=2/9 (Radiant) sind numerisch '2/9', aber")
print(f"    dimensional verschieden. Die Mode-Locking-Arbeit adressiert die")
print(f"    dimensionslose Rationalzahl, nicht direkt den Radiant-Offset.")

print("\n" + "="*76)
print("BEFUND (beweisartig, ehrlich):")
print("="*76)
print(f"""
1. theta=2/9 RAD ist transzendent in Einheiten von 2 pi (= 2pi/(9 pi), pi drin).
   Nach Lindemann-Weierstrass ist e^(i*2/9) KEINE Einheitswurzel.

2. Jede topologische / fluss-quantisierte / endliche-Gruppen-Holonomie ist eine
   EINHEITSWURZEL (rationales Vielfaches von 2 pi). Also kann KEINE solche
   Topologie -- auch nicht T^4/Z_3 -- den Offset theta=2/9 rad liefern. Die
   Topologie erzwingt die SPACING 2pi/3 (Z_3, der Nenner), NICHT den Offset.

3. Im Zirkulant ist theta die Phase der komplexen Kopplung; Q=2/3 ist von theta
   unabhaengig (nur r=sqrt2). Nenner/Q topologisch fest, Offset frei -- konsistent
   mit Dok 282/285.

4. Der Offset ist also strukturell ein KONTINUIERLICHER Modulus, kein
   topologischer Invariant. Determiniert wird er nicht durch Fluss-Quantisierung,
   sondern DYNAMISCH -- genau der selbstkonsistente Lepton-Fixpunkt (Dok 203),
   keine endliche Gruppe.

ANTWORT auf 'erzwingt T^4/Z_3 das theta=2/9': NEIN -- und beweisartig nicht, weil
2/9 rad die falsche ART Zahl ist (transzendent in 2 pi, keine Einheitswurzel).
Das erklaert, warum es der topologischen Herleitung widersteht. Von UNSERER Seite
ist die Frage damit beantwortet: der Offset ist dynamisch (Fixpunkt), nicht
topologisch; die externe Route bleibt HLVs dynamische Spiral-Phase R (BD17A),
die genau eine dynamische, keine quantisierte Phase ist (Dok 283).

CAVEAT (Punkt 4 oben): das Mode-Locking-2/9 (Rotationszahl, dimensionslos) ist
nicht dimensionsgleich mit dem Koide-2/9 (Radiant); die Identifikation ist offen.
""")
