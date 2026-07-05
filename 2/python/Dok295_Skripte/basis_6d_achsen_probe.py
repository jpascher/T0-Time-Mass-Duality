"""Dok 295/294 -- Sind die 6 Dimensionen gleich? Achsenspektrum des 6D-Cut-and-Project.
numpy-only. Deterministisch.

Frage: decken sich FFGFTs geteiltes Objekt (tau=phi ikosaedrischer Projektor, Dok 294)
und ein natives 6D-Cut-and-Project (Marcel, Z^6 -> 3+3)?

Konstruktion: das tau-Ikosaeder hat 12 Ecken = zyklische Permutationen von (0,+-1,+-tau).
Seine 6 fuenfzaehligen Achsen (antipodale Ecken-Paare) sind die 6 projizierten Achsen des
6D->3D Cut-and-Project. Geprueft wird das Spektrum der 15 paarweisen Achsenwinkel.

Erwartung (Dok 294):
  tau=phi   -> alle 15 Winkel gleich arccos(1/sqrt5)=63.435 Grad  (aequiangular)
  tau=sqrt2 -> zweiwertig 61.87/70.53 Grad                        (nicht aequiangular)
Damit: die 6D-Basen decken sich GENAU auf der goldenen (ikosaedrischen) Projektion --
das ist das geteilte Objekt; ein generisches 6D-Split tut es nicht.
"""
import numpy as np
import itertools

def sechs_achsen(tau):
    """6 fuenfzaehlige Achsen aus dem tau-Ikosaeder (12 Ecken, antipodale Paare)."""
    ecken = []
    base = [(0, a, b) for a in (1,-1) for b in (tau,-tau)]
    for (x,y,z) in base:
        ecken += [(x,y,z), (z,x,y), (y,z,x)]     # 3 zyklische Shifts -> 12 Ecken
    ecken = np.array(ecken, float)
    ecken /= np.linalg.norm(ecken, axis=1, keepdims=True)
    # antipodale Paare zusammenfassen -> 6 Achsen (Vorzeichen normieren)
    achsen = []
    for v in ecken:
        v = v * np.sign(v[np.argmax(np.abs(v))])   # kanonisches Vorzeichen
        if not any(np.allclose(v, a, atol=1e-9) for a in achsen):
            achsen.append(v)
    return np.array(achsen)

def winkelspektrum(achsen):
    """alle 15 paarweisen spitzen Winkel (Grad)."""
    w = []
    for i,j in itertools.combinations(range(len(achsen)), 2):
        c = abs(np.dot(achsen[i], achsen[j]))      # Achsen = ungerichtete Linien
        w.append(np.degrees(np.arccos(np.clip(c,0,1))))
    return np.sort(np.round(w, 4))

phi   = (1+np.sqrt(5))/2
silber= 1+np.sqrt(2)   # tau des Silbernen Schnitts (Dok 294 nennt sqrt2-Konstruktion)

for name, tau in [("phi (golden)", phi), ("sqrt2", np.sqrt(2)), ("1+sqrt2 (silber)", silber)]:
    A = sechs_achsen(tau)
    spek = winkelspektrum(A)
    werte = np.unique(np.round(spek, 3))
    print(f"tau = {name:16s} ({tau:.5f}):  {len(A)} Achsen")
    print(f"    Winkelwerte (Grad): {werte}")
    print(f"    aequiangular? {'JA' if len(werte)==1 else 'nein'}   "
          f"(Referenz arccos(1/sqrt5)={np.degrees(np.arccos(1/np.sqrt(5))):.3f})")
print()
print("Fazit zur Dimensionsfrage:")
print("  Die 6 projizierten Achsen decken sich mit FFGFTs geteiltem Objekt GENAU bei tau=phi")
print("  (aequiangular, 63.435 Grad). Ein generisches 6D-Split (sqrt2/silber) ergibt ein")
print("  anderes, zweiwertiges Spektrum. Die Sechs ist also nicht per se gleich -- gleich ist")
print("  allein die golden-ikosaedrische Projektion. Das ist das geteilte Objekt, einseitig")
print("  verifiziert (FFGFT->HLV, Dok 294) und filtrations-empfindlich.")
