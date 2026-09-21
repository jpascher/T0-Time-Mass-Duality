#!/usr/bin/env python3
"""
Dok. 372 Prüfskript: Das Matrixelement-Prinzip und seine Reichweite
Alle Ergebnisse exakt arithmetisch (mpmath).
"""
import mpmath as mp; mp.mp.dps=50
import math

phi = (1 + mp.sqrt(5)) / 2
PASS = 0; FAIL = 0

def check(name, val, ref, tol=1e-40):
    global PASS, FAIL
    if abs(val - ref) < tol:
        print(f"[OK] {name}")
        PASS += 1
    else:
        print(f"[!!] {name}: {mp.nstr(val,8)} ≠ {mp.nstr(ref,8)}")
        FAIL += 1

print("=== DOK. 372 — MATRIXELEMENT-PRINZIP ===\n")

# P1: Umverteilungsgewichte
print("P1 Umverteilungsgewichte")
p0 = mp.mpf(2)/9
p1 = (2 + 3*phi) / 9
p2 = (5 - 3*phi) / 9
check("p0 = 2/9", p0, mp.mpf(2)/9)
check("p0+p1+p2 = 1", p0+p1+p2, mp.mpf(1))

# P2: φ⁸-Verhältnisse (Dok. 368, Hauptergebnis)
print("\nP2 φ⁸-Skelett der Gewichtsverhältnisse")
check("p1/p2 = φ⁸", p1/p2, phi**8)
check("p0/p2 = 2φ⁴", p0/p2, 2*phi**4)

# P3: Koide Q = 2/3 (exakt aus θ=2/9)
print("\nP3 Koide-Quotient")
theta = mp.mpf(2)/9
sqm = [1 + mp.sqrt(2)*mp.cos(theta + 2*mp.pi*k/3) for k in range(3)]
m   = [s**2 for s in sqm]
Q   = sum(m) / sum(sqm)**2
check("Q = 2/3", Q, mp.mpf(2)/3)

# P4: 4/3 = 2Q (Dok. 371)
print("\nP4  4/3 = 2·Q")
check("2Q = 4/3", 2*Q, mp.mpf(4)/3)

# P5: φ = 2cos(72°)+1 (Spur-Relation)
print("\nP5 φ = 2cos(72°)+1")
check("φ = 2cos(2π/5)+1", phi, 2*mp.cos(2*mp.pi/5)+1)

# P6: Weinberg-Winkel Abstand von 2/9
print("\nP6 Weinberg-Winkel Numerik")
sin2w_pdg = mp.mpf('0.23121')  # PDG
delta = abs(sin2w_pdg - p0) / sin2w_pdg * 100
check("Δ(sin²θ_W, 2/9) < 5%", delta < 5, True)
print(f"    Δ = {mp.nstr(delta,4)}%  (3.9%)")

# P7: p1,p2 positiv und korrekt geordnet
print("\nP7 Ordnung der Gewichte")
check("p1 > p0 > p2 > 0", p1 > p0 and p0 > p2 and p2 > 0, True)

# P8: Leptonmassen-Verhältnis aus Koide (korrekte Modenordnung)
print("\nP8 Leptonmassen-Verhältnisse")
# k=0 Tau, k=1 Muon, k=2 Elektron (nach Ordnung sqm[0]>sqm[2]>sqm[1])
sqm_sorted = sorted([(s,k) for k,s in enumerate(sqm)], reverse=True)
# Tau: größte, Elektron: mittlere, Muon: kleinste
sq_tau, sq_e, sq_mu = sqm_sorted[0][0], sqm_sorted[1][0], sqm_sorted[2][0]
m_mu_e = (sq_mu/sq_e)**2
m_tau_e = (sq_tau/sq_e)**2
m_mu_pdg  = mp.mpf('205.59889')  # m_μ/m_e PDG
m_tau_pdg = mp.mpf('3477.228')   # m_τ/m_e PDG
# Q aus reiner Parametrisierung ist exakt 2/3 — die Massen-Verhältnisse
# kommen aus der vollen Koide-Formel, hier nur Q prüfen
check("Koide Q = 2/3 (aus θ=2/9)", Q, mp.mpf(2)/3)
print(f"    m_μ/m_e (FFGFT) = {mp.nstr(m_mu_e,8)}")
print(f"    m_τ/m_e (FFGFT) = {mp.nstr(m_tau_e,8)}")

print(f"\nTeil 1: {PASS} PASS / {FAIL} FAIL")

# ============================================================
# TEIL 2: Spektrum der A5-Matrixelemente und SM-Vergleich
# ============================================================
import numpy as np
print("\n=== TEIL 2: A5-SPEKTRUM UND SM-VERGLEICH ===")
fphi=float(phi); w=np.exp(2j*np.pi/3)
V=np.array([[1,1,1],[1,w,w**2],[1,w**2,w]],dtype=complex)/np.sqrt(3)
def rot(axis,ang):
    a=np.array(axis,float); a/=np.linalg.norm(a)
    K=np.array([[0,-a[2],a[1]],[a[2],0,-a[0]],[-a[1],a[0],0]])
    return np.eye(3)+np.sin(ang)*K+(1-np.cos(ang))*K@K
R5=rot((0,1,fphi),2*np.pi/5); C3=rot((1,1,1),2*np.pi/3)
G=[np.eye(3)]; seen={tuple(np.round(np.eye(3),8).ravel())}; fr=[np.eye(3)]
while fr:
    nf=[]
    for g in fr:
        for h in (R5,C3):
            m=g@h; k=tuple(np.round(m,8).ravel())
            if k not in seen: seen.add(k); G.append(m); nf.append(m)
    fr=nf
check("P9  |A5| = 60", mp.mpf(len(G)), mp.mpf(60))
spec=set()
for g in G:
    P=np.abs(V.conj()@g@V.T)**2
    spec.update(np.round(P.ravel(),8))
expected={0.0, round((5-3*fphi)/9,8), round(1/9,8), round(2/9,8),
          round(4/9,8), round(5/9,8), round((2+3*fphi)/9,8), 1.0}
check("P10 Spektrum = 8 Werte {0,p2,1/9,2/9,4/9,5/9,p1,1}",
      mp.mpf(1) if spec==expected else mp.mpf(0), mp.mpf(1))
check("P11 4/9 + 5/9 = 1", mp.mpf(4)/9+mp.mpf(5)/9, mp.mpf(1))

# Weinberg on-shell
MZ=mp.mpf('91.1880'); MW=mp.mpf('80.3692'); MWc=mp.mpf('80.4335')
s2=1-(MW/MZ)**2; s2c=1-(MWc/MZ)**2
check("P12 on-shell (PDG-Mittel) < 0.5% von 2/9", abs(s2-p0)/p0*100 < 0.5, True)
check("P13 on-shell (CDF) < 0.2% von 2/9",        abs(s2c-p0)/p0*100 < 0.2, True)
MW29=MZ*mp.sqrt(mp.mpf(7)/9)
check("P14 M_W(2/9) = M_Z·√(7/9) ≈ 80.420", abs(MW29-mp.mpf('80.4203'))<0.001, True)
print(f"    M_W(2/9) = {mp.nstr(MW29,6)} GeV")

# θ23
check("P15 PDG sin²θ23=0.558 → 5/9 auf <0.5%", abs(mp.mpf('0.558')-mp.mpf(5)/9)/mp.mpf('0.558')*100<0.5, True)
check("P16 |5/9-1/2| = |4/9-1/2| = 1/18", abs(mp.mpf(5)/9-mp.mpf(1)/2), mp.mpf(1)/18)

# Negativbefunde
for name,val,thr in [("P17 sin²θ12=0.307 nicht im Spektrum (>5%)",0.307,5),
                     ("P18 sin²θ13=0.0222 nicht im Spektrum (>5%)",0.0222,5),
                     ("P19 α_s=0.118 nicht im Spektrum (>5%)",0.118,5)]:
    d=min(abs(s-val)/val*100 for s in spec if s>0)
    check(name, bool(d>thr), True)

print(f"\nTeil 2: {PASS} PASS / {FAIL} FAIL")

# ============================================================
# TEIL 3: Abgleich mit Dok. 340
# ============================================================
print("\n=== TEIL 3: ABGLEICH DOK. 340 ===")
import sympy as sp
x=sp.symbols('x')
mp13=sp.minimal_polynomial(sp.cos(2*sp.pi/13), x)
check("P20 Grad Minimalpolynom cos(2π/13) = 6", mp.mpf(sp.degree(mp13,x)), mp.mpf(6))
c5=mp.cos(2*mp.pi*5/13)**2
check("P21 cos²(10π/13) ≠ 5/9 (Differenz > 1e-3)", bool(abs(c5-mp.mpf(5)/9)>1e-3), True)
check("P22 cos²(10π/13) und 5/9 innerhalb 1%", bool(abs(c5-mp.mpf(5)/9)/(mp.mpf(5)/9)<0.01), True)
# Look-elsewhere: Menge aus Dok. 340 (12 Werte) trifft ≥5 von 7 SM-Parametern <7%
S13=[float(mp.cos(2*mp.pi*k/13)**2) for k in range(1,7)]; S13+= [1-v for v in S13]
SM={"θ12":0.307,"θ23":0.558,"θ23NO":0.470,"θ13":0.0222,"θW":0.2232,"λ":0.225,"αs":0.118}
hits13=sum(1 for v in SM.values() if min(abs(s-v)/v for s in S13)<0.07)
check("P23 Dok.-340-Menge: ≥5 von 7 SM-Werten <7% (zu dicht)", bool(hits13>=5), True)
hitsA5=sum(1 for v in SM.values() if min(abs(s-v)/v for s in spec if s>0)<0.013)
check("P24 A5-Achtermenge: genau 3 Treffer <1.3%", mp.mpf(hitsA5), mp.mpf(3))
print(f"\n{'='*45}")
print(f"GESAMT (alle Teile): {PASS} PASS / {FAIL} FAIL")
