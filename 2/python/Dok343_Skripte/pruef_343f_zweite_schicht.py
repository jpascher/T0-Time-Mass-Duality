"""
pruef_343f_zweite_schicht.py — Quantenzahlen der zweiten GF(27)*-Schicht {f₁, f₄}
Frage: Welche Quantenzahlen hätten Teilchen in der Schicht {f₁,f₄}, wenn {f₂,f₃} die Leptonen sind?
Methode: Alle Quantenzahlen aus der Galois-Algebra ableiten (Frobenius-Orbit, Z₂-Parität,
Sektorpaarung, Selbstinversion), ohne physikalische Annahme; dann interpretieren.
"""
import itertools
# Alle Aussagen leben im Exponentenraum Z₂₆ ≅ GF(27)* (Erzeuger g, Ordnung 26).
print('GF(27)* ≅ Z₂₆; Klassen nach Polynomtabelle Dok. 342\n')
# Elemente als Exponenten k ∈ Z₂₆ ; Frobenius: k → 3k ; Negation: k → k+13 ; Inversion: k → -k
frob=lambda k:(3*k)%26; neg=lambda k:(k+13)%26; inv=lambda k:(-k)%26
# Primitive Klassen = Frobenius-Orbits von Exponenten mit ggT(k,26)=1
from math import gcd
# Nummerierung nach Polynomtabelle Dok. 342: f1=x³+2x+1 {1,3,9}, f2=x³+2x²+1 {17,23,25},
# f3=x³+2x²+x+1 {5,15,19}, f4=x³+x²+2x+1 {7,11,21}
orbits=[]; names={}
for i,k in enumerate((1,17,5,7)):
    o=sorted({k,frob(k),frob(frob(k))}); orbits.append(o); names[tuple(o)]=f"f{i+1}"
print("Primitive Klassen (Frobenius-Orbits in Z₂₆*, Ordnung 26):")
for o in orbits: print(f"  {names[tuple(o)]} = {o}")
# Ordnung-13-Klassen
# g_i = Negationspartner von f_i (Polynomtabelle Dok. 342): g1=x³+2x+2, g2=x³+x²+2, g3=x³+x²+x+2, g4=x³+2x²+2x+2
orb13=[]
for i,k in enumerate((14,4,2,8)):
    o=sorted({k,frob(k),frob(frob(k))}); orb13.append(o); names[tuple(o)]=f"g{i+1}"
print("Ordnung-13-Klassen:")
for o in orb13: print(f"  {names[tuple(o)]} = {o}")

def cls(k):
    for o in orbits+orb13:
        if k in o: return names[tuple(o)]
    return "fix"
print("\nAbbildungen zwischen Klassen:")
print(f"{'Klasse':>7} {'Inversion k→−k':>16} {'Negation k→k+13':>17} {'Z₁₃-Orbit (k mod 13)':>22} {'Z₂-Parität (k mod 2)':>20}")
z13orb={1:"O1{1,3,9}",3:"O1{1,3,9}",9:"O1{1,3,9}",2:"O2{2,5,6}",5:"O2{2,5,6}",6:"O2{2,5,6}",4:"O3{4,10,12}",10:"O3{4,10,12}",12:"O3{4,10,12}",7:"O4{7,8,11}",8:"O4{7,8,11}",11:"O4{7,8,11}",0:"fix"}
for o in orbits:
    k=o[0]
    print(f"{cls(k):>7} {cls(inv(k)):>16} {cls(neg(k)):>17} {z13orb[k%13]:>22} {k%2:>20}")
print()
for o in orb13:
    k=o[0]
    print(f"{cls(k):>7} {cls(inv(k)):>16} {cls(neg(k)):>17} {z13orb[k%13]:>22} {k%2:>20}")

print("""
Ablesung [B]:
  Sektorpaarung (Inversion):  f1↔f2, f3↔f4 — zwei Paare (Dok. 343 D').
  Negation:                   f_i ↔ g_i — Ordnung 26 ↔ 13 (Dok. 343 D'').
  Z₂-Parität: alle f_i ungerade (k ungerade) → nicht im Frobenius-Fixkörper GF(3)*, aber
              im Z₂-Sektor 'Parität 1' — massiver Sektor nach Dok. 339 (Fixpunkte ±1 = Z₂).
  Z₁₃-Orbit:  f-Klassen verteilen sich auf die Z₁₃-Orbits O1..O4.
""")
# Welche Z13-Orbits tragen die beiden Schichten?
def z13set(o): return sorted({k%13 for k in o})
L=[o for o in orbits if cls(o[0]) in("f3","f4")]; S=[o for o in orbits if cls(o[0]) in("f1","f2")]
print("Schicht {f3,f4}: Z₁₃-Orbits", [z13orb[z13set(o)[0]] for o in L])
print("Schicht {f1,f2}: Z₁₃-Orbits", [z13orb[z13set(o)[0]] for o in S])
print()
# Involutionen: Sektorpaarung k→−k (GF(27)*-Inversion) und k→k⁻¹ mod 13 (Dok. 340, Majorana-Kriterium)
orbs={"O1":[1,3,9],"O2":[2,5,6],"O3":[4,10,12],"O4":[7,8,11]}
def which(k): return next(n for n,o in orbs.items() if k%13 in o)
print("Z₁₃-Orbits unter beiden Involutionen:")
for n,o in orbs.items():
    neg=sorted({(-k)%13 for k in o}); mi=sorted({pow(k,-1,13) for k in o})
    print(f"  {n} {o}: k→−k → {which(neg[0])};   k→k⁻¹ → {which(mi[0])} {'SELBSTINVERS → Majorana' if mi==o else '→ Dirac'}")
assert sorted({pow(k,-1,13) for k in orbs["O1"]})==orbs["O1"]
assert sorted({pow(k,-1,13) for k in orbs["O3"]})==orbs["O3"]
assert sorted({pow(k,-1,13) for k in orbs["O2"]})==orbs["O4"]
print("  Kuriosität [S]: (max O1)²−1 =", 9*9-1, "= |GF(81)*|;  (max O4)²−1 =", 11*11-1, "= Δm²_atm/m_ν² (Dok. 340)")
print("""
Quantenzahlen aus der Algebra [B]:
  Schicht {f3,f4} ≙ Z₁₃-Orbits O2,O4 (zueinander invers)  → Dirac-Profil: Teilchen ≠ Antiteilchen
  Schicht {f1,f2} ≙ Z₁₃-Orbits O1,O3 (selbstinvers)       → Majorana-Profil
  Beide Schichten: Z₂-Parität 1 (massiver Sektor, Dok. 339), keine Farbe, drei Zustände je Klasse.
  Sektorpaarung k→−k: f1↔f2 (O1↔O3), f3↔f4 (O2↔O4); Negation f_i↔g_i.
Deutung [S]:
  {f3,f4} = geladene Leptonen (Dirac).  {f1,f2} = Neutrinosektor (Majorana); Dok. 340 setzt die
  aktiven Neutrinos in O3 = f2.  Offen bleibt f1 = O1 {1,3,9}: Majorana, drei Generationen,
  Sektorpartner der aktiven Neutrinos → Profil steriler (rechtshändiger) Neutrinos; die Paarung
  O1↔O3 unter k→−k ist algebraisch die Seesaw-Paarung aktiv↔steril. Dok. 340: m_min = 4 m_ν.
Korrektur: Dok. 341 legt für Leptonen nur Ordnung 26 fest, keine Klasse.
""")
print("Alle Assertions bestanden.")
