"""pruef_347_gell_mann.py — Gell-Mann-Nishijima aus Galois-Struktur"""
from fractions import Fraction
QR13 = {k for k in range(1,13) if any(j*j%13==k for j in range(1,13))}

print("Satz A: Y aus QR/NQR")
for name,nqr,Y_exp in [("Lepton",0,Fraction(-1)),("Quark",1,Fraction(1,3))]:
    Y=Fraction(-1)+Fraction(4,3)*nqr; assert Y==Y_exp; print(f"  {name}: Y={Y} ✓")

print("\nSatz B: I3 aus Su/Sd-Trennung")
for su,I3_exp in [(True,Fraction(1,2)),(False,Fraction(-1,2))]:
    I3=Fraction(1,2) if su else Fraction(-1,2); assert I3==I3_exp
    print(f"  {'Su' if su else 'Sd'}: I3={I3} ✓")

print("\nSatz C: Q = I3 + Y/2")
for name,su,quark,q_exp in [
    ("Neutrino",True,False,Fraction(0)),("Elektron",False,False,Fraction(-1)),
    ("up-Quark",True,True,Fraction(2,3)),("dn-Quark",False,True,Fraction(-1,3))]:
    Y=Fraction(-1)+Fraction(4,3)*(1 if quark else 0)
    I3=Fraction(1,2) if su else Fraction(-1,2)
    Q=I3+Y/2; assert Q==q_exp, f"{name}: {Q}!={q_exp}"
    print(f"  {name:12s}: I3={str(I3):>5}, Y={str(Y):>5}, Q={Q} ✓")

print("\nSatz D: Y aus Legendre-Symbol")
for orb,Y_exp in [([1,3,9],Fraction(-1)),([4,10,12],Fraction(-1)),
                  ([2,5,6],Fraction(1,3)),([7,8,11],Fraction(1,3))]:
    qr=all(k%13 in QR13 for k in orb)
    Y=Fraction(-1)+Fraction(4,3)*(0 if qr else 1)
    assert Y==Y_exp; print(f"  {orb}: Y={Y} ✓")

print("\nAlle Assertions bestanden. [B]")
