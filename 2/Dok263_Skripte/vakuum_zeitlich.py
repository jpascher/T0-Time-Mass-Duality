import numpy as np

# ============================================================================
# Vakuum-Energie kommt aus der ZEITLICHEN Komponente -- keine eigenstaendige
# (statische) Energie.  RECHNERISCHER Nachweis aus der FFGFT-Lagrangedichte.
#
# Grundlage (Dok 010, BELEGT):
#   Lagrangedichte:  L = xi (d_mu E)(d^mu E)        -- NUR Ableitungsterm
#   Feldgleichung:   box E = 0                       -- MASSELOS (kein m^2 E^2)
#   KEIN Potentialterm V(E), KEIN Massenterm -> KEINE statische Eigenenergie.
#
# Aus L folgt der Energie-Impuls-Tensor (Standard-Feldtheorie):
#   T_{mu nu} = 2 xi [ (d_mu E)(d_nu E) - (1/2) g_{mu nu} (d_alpha E)(d^alpha E) ]
# Energiedichte = T_{00}. Mit Metrik (+,-,-,-) und (d_alpha E)(d^alpha E)
#   = (d_t E)^2 - (grad E)^2  (in nat. Einheiten c=1):
#
#   T_00 = 2 xi [ (d_t E)^2 - (1/2)( (d_t E)^2 - (grad E)^2 ) ]
#        = xi [ (d_t E)^2 + (grad E)^2 ]
#
# DAS ist der Kern: T_00 haengt NUR von Ableitungen ab. Es gibt KEINEN
# konstanten/feldwert-abhaengigen Term (kein V(E), kein m^2 E^2). Ohne
# Zeit- UND Raum-Variation ist die Energiedichte exakt NULL.
# ============================================================================

xi = 4/30000.0
print("="*70)
print("Vakuum-Energie aus der zeitlichen Komponente (Dok 010: L = xi (dE)^2)")
print("="*70)
print("""Energiedichte aus dem Energie-Impuls-Tensor:
   T_00 = xi [ (d_t E)^2 + (grad E)^2 ]
Kein V(E), kein m^2 E^2 -> KEINE eigenstaendige statische Energie.
""")

# --- numerische Demonstration an einem konkreten Feld ---
# Feld als Welle: E(x,t) = A cos(k x - w t). Masselos: w = |k| (aus box E=0).
A   = 1.0
k   = 2*np.pi/1.0      # Wellenzahl (1/Laenge, nat. Einh.)
w   = abs(k)          # Dispersion masselos: w = k  (box E = 0)

# Ableitungen
# d_t E = A w sin(kx - wt),  d_x E = -A k sin(kx - wt)
# Zeitmittel von sin^2 = 1/2
mean_sin2 = 0.5
dtE2_mean   = (A*w)**2 * mean_sin2
gradE2_mean = (A*k)**2 * mean_sin2

T00_full = xi*(dtE2_mean + gradE2_mean)
print("FALL 1: dynamisches Feld E = A cos(kx - wt), masselos w=k")
print(f"   <(d_t E)^2>  = {dtE2_mean:.4f}")
print(f"   <(grad E)^2> = {gradE2_mean:.4f}")
print(f"   T_00 = xi[<(d_t E)^2>+<(grad E)^2>] = {T00_full:.6e}   (>0: Energie da)")

# --- FALL 2: zeitliche Komponente ABGESCHALTET (statisch, d_t E = 0) ---
# Ein rein statisches Feld muss box E=0 erfuellen: d.h. grad^2 E = 0.
# Loesung im freien Vakuum mit endlicher Energie: E = const -> grad E = 0.
# (Ein statisches E mit grad E != 0 ist keine quellenfreie Vakuumloesung;
#  jede lokalisierte statische Stoerung braucht eine Quelle -> nicht Vakuum.)
dtE2_static   = 0.0
gradE2_static = 0.0   # quellenfreies statisches Vakuum: E=const
T00_static = xi*(dtE2_static + gradE2_static)
print("\nFALL 2: zeitliche Komponente AUS (d_t E = 0), quellenfreies Vakuum")
print("   box E = 0 + statisch  =>  grad^2 E = 0  =>  E = const  =>  grad E = 0")
print(f"   T_00 = xi[0 + 0] = {T00_static:.1f}")
print("   -> OHNE zeitliche Entwicklung ist die Vakuum-Energiedichte EXAKT NULL.")

# --- der Punkt ---
print("\n" + "-"*70)
print("ERGEBNIS (rechnerisch):")
print("-"*70)
print("""  Die Energiedichte T_00 = xi[(d_t E)^2 + (grad E)^2] enthaelt KEINEN
  statischen Term. Es gibt keine 'eigenstaendige' Vakuumenergie, die auch
  bei eingefrorenem Feld bliebe. Schaltet man die zeitliche Komponente ab
  (d_t E = 0) und fordert eine quellenfreie Vakuumloesung (box E = 0), folgt
  E = const und T_00 = 0.

  -> Die Vakuum-Energie ist VOLLSTAENDIG an die zeitliche (und raeumliche)
     VARIATION des Feldes gebunden. Sie ist kein statischer Eigenwert,
     sondern Ausdruck der Dynamik. Das ist die rechnerische Form von:
     'keine eigenstaendige Energie -- sie kommt aus der zeitlichen Komponente'.

  Konsistent mit:
   - Dok 010: L = xi(dE)^2, box E = 0 (masselos, kein Potentialterm).
   - kompaktifiziert=dekompaktifiziert vorhanden (vakuum_emergenz.py): die
     STRUKTUR (Feld + seine Dynamik) ist dieselbe; T_00 ist nur ihre
     dimensionsbehaftete Projektion. Hier wird zusaetzlich gezeigt, dass
     selbst diese Struktur KEINEN statischen Energie-Sockel hat.
""")

# --- ehrliche Grenzen ---
print("="*70)
print("EHRLICHE GRENZEN:")
print("="*70)
print("""  1. T_{mu nu} aus L=xi(dE)^2 ist Standard-Feldtheorie (kanonischer
     Energie-Impuls-Tensor) -- die FFGFT-Aussage ist, dass GENAU dieser
     potentialfreie Lagrangian der richtige ist (Dok 010/019).
  2. 'grad E=0 im statischen Vakuum' gilt fuer die quellenfreie Loesung mit
     endlicher Energie. Mit Randbedingungen (Casimir-Platten!) ist grad E != 0
     moeglich -> dann gibt es eine statische RAUM-Komponente. D.h. die
     Aussage 'rein zeitlich' gilt fuers FREIE Vakuum; eingeschraenktes Vakuum
     (Casimir) hat einen Raumanteil (konsistent mit Dok 091: freies vs.
     eingeschraenktes Vakuum).
  3. Reduktionsschicht: zeigt die STRUKTUR (kein statischer Sockel), nicht
     einen kosmologischen Zahlenwert.
""")
