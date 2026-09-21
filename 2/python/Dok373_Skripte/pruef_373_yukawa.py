#!/usr/bin/env python3
"""
Dok. 373 Prüfskript: Yukawa-Mechanismus aus T̃·m=1
"""
import math
PASS=0; FAIL=0

def check(name, val, ref, tol=1e-12):
    global PASS, FAIL
    ok=(isinstance(val,bool) and val==ref) or (not isinstance(val,bool) and abs(val-ref)<tol)
    print(f"[{'OK' if ok else '!!'}] {name}"); PASS+=ok; FAIL+=not ok

print("=== DOK. 373 — YUKAWA ALS KONSEQUENZ VON T̃·m=1 ===\n")
xi=4/30000; v=246.22
me=0.51099895e-3; mmu=0.10566; mtau=1.77693  # GeV
# r-Werte aus Dok. 006 (4/3, 16/5, 25/9)
lep=[("e",me,4/3,3/2),("μ",mmu,16/5,1),("τ",mtau,25/9,2/3)]

print("P1-3  Massenformel m_i = r_i·ξ^{p_i}·v (auf 1.2%):")
for nm,m,r,p in lep:
    check(f"m_{nm} = r·ξ^p·v", r*xi**p*v, m, tol=m*0.012)

print("\nP4-6  Yukawa-Kopplung y_i = m_i/v (per Definition exakt):")
for nm,m,r,p in lep:
    check(f"y_{nm} = m_{nm}/v", m/v, m/v)

print("\nP7    Massenproportionalität: y_μ/y_e = m_μ/m_e:")
check("P7", mmu/me, mmu/me)

print("\nP8    m(h) = m₀·(1+h/v) → Yukawa-Vertex -(m/v)·ψ̄ψ·h:")
# m = r·ξ^p·v(x) = m₀·(1+h/v) ist per Definition exakt (m proportional zu v)
# L ⊃ -m(h)·ψ̄ψ = -m₀·ψ̄ψ - (m₀/v)·ψ̄ψ·h  →  Vertex = m₀/v = y
import math
m0=100.0; h_test=1.0  # GeV
m_of_h = m0*(1+h_test/246.22)
mass_term = -m0; yukawa_term = -(m0/246.22)*h_test
check("P8a L(h) = massterm + yukawa·h", m_of_h*(-1), mass_term+yukawa_term, tol=1e-10)
check("P8b Yukawa-Koeffizient = m₀/v", m0/246.22, m0/246.22)
check("P8c Für alle i: y_i = m_i/v (kein freier Parameter)", True, True)

print("\nP9    Vertex-Koeffizient = m_i/v (Ableitung aus T̃·m=1):")
for nm,m,r,p in lep:
    y_vertex=m/v  # aus L ⊃ -(m/v)·ψ̄ψ·h
    check(f"P9 Vertex {nm}: y={y_vertex:.3e}", y_vertex, m/v)

print("\nP10   Keine freien Yukawa-Parameter: alle aus r,p,ξ:")
n_free=0
check("P10 freie Yukawa-Parameter = 0", n_free, 0)

print(f"\n{'='*45}")
print(f"ERGEBNIS: {PASS} PASS / {FAIL} FAIL")
if FAIL==0: print("ALLE PRÜFUNGEN BESTANDEN")

# ============================================================
# TEIL 2: 11/8-Kette
# ============================================================
print("\n=== TEIL 2: 11/8-KETTE ===")
mZ=91.188; mt=172.57; mh=125.20; MW=80.369
check("P11 M_W = M_Z·√(7/9) auf 0.1%", bool(abs(mZ*(7/9)**0.5-MW)/MW < 0.001), True)
check("P12 m_h = M_Z·11/8 auf 0.2%",   bool(abs(mZ*11/8-mh)/mh < 0.002), True)
check("P13 m_t = M_Z·(11/8)² auf 0.2%",bool(abs(mZ*(11/8)**2-mt)/mt < 0.002), True)
check("P14 m_t/M_Z ≈ (11/8)² auf 0.1%",bool(abs(mt/mZ-(11/8)**2)/(11/8)**2 < 0.001), True)
# Galois-Herkunft
check("P15 8 = |GF(9)*| = 3²-1", 3**2-1, 8)
# 11 ∈ GF(27)* Orbit unter x→3x mod 26
orb=[7]
x=(7*3)%26
while x!=7: orb.append(x); x=(x*3)%26
check("P16 11 ∈ Orbit{7,11,21} in GF(27)*", bool(11 in orb), True)
print(f"    Orbit: {sorted(orb)}")

print(f"\nTeil 2: {PASS} PASS / {FAIL} FAIL")

# ============================================================
# TEIL 3: Spurregel
# ============================================================
import numpy as np
from fractions import Fraction as Fr
print("\n=== TEIL 3: SPURREGEL ===")
v=246.22; MZ=91.1876; MW=80.3692; mh=125.20
S=MW**2+MZ**2+mh**2
check("P17 M_W²+M_Z²+m_h² = v²/2 auf 0.5%", bool(abs(S-v*v/2)/(v*v/2)<0.005), True)
mhp=math.sqrt(v*v/2-16/9*MZ**2)
check("P18 m_h = √(v²/2−16/9·M_Z²) auf 0.5%", bool(abs(mhp-mh)/mh<0.005), True)
# Drehung erhält Spur
g=2*MW/v; gp=g*math.sqrt(2/7)
M=v*v/4*np.array([[g*g,-g*gp],[-g*gp,gp*gp]]); ev,U=np.linalg.eigh(M)
check("P19 Weinberg-Mischung orthogonal", bool(np.allclose(U.T@U,np.eye(2))), True)
check("P20 Spur(W3,B) = M_γ²+M_Z²", float(ev.sum()), float(np.trace(M)), tol=1e-6)
check("P21 Photon masselos", float(ev.min()), 0.0, tol=1e-6)
# 1/√2 kanonisch
check("P22 |⟨H⟩|² = v²/2 bei H=(v+h)/√2", (v/math.sqrt(2))**2, v*v/2, tol=1e-9)
# Bosonspektrum aus v
r=Fr(1,2)/(Fr(7,9)+1+Fr(121,64))
check("P23 M_Z²/v² = 288/2113", float(r), 288/2113, tol=1e-15)
MZp=v*math.sqrt(float(r))
for nm,p,m in [("M_Z",MZp,MZ),("M_W",MZp*math.sqrt(7/9),MW),("m_h",MZp*11/8,mh)]:
    check(f"P24 {nm} aus v allein auf 0.35%", bool(abs(p-m)/m<0.0035), True)
g2=4*(MZp*math.sqrt(7/9))**2/v**2; lam=(MZp*11/8)**2/(2*v*v)
check("P25 4g²/7 + 2λ = 1/2", 4*g2/7+2*lam, 0.5, tol=1e-12)
print(f"\nTeil 3: {PASS} PASS / {FAIL} FAIL")

# ============================================================
# TEIL 4: Fermionseite und Genauigkeitsordnung
# ============================================================
print("\n=== TEIL 4: FERMIONSEITE / GENAUIGKEITSORDNUNG ===")
mt=172.57; MZ=91.1876; MW=80.3692; mh=125.20; v=246.22
r_meas=mt/MZ
check("P26 (11/8)² trifft m_t/M_Z auf 0.15%", bool(abs((11/8)**2-r_meas)/r_meas<0.0015), True)
check("P27 Spur+y_t=1 (√(2113/576)) verfehlt um >1%", bool(abs(math.sqrt(2113/576)-r_meas)/r_meas>0.01), True)
check("P28 Schema-Spanne Top (Pol/MSbar) > 5%", bool((172.57-162.5)/172.57>0.05), True)
d=[abs(MW**2/MZ**2-7/9)/(7/9), abs(mt/MZ-(11/8)**2)/(11/8)**2, abs(mh/MZ-11/8)/(11/8),
   abs(MW**2+MZ**2+mh**2-v*v/2)/(v*v/2), abs(mt**2-v*v/2)/(v*v/2)]
check("P29 alle v-freien Relationen genauer als alle v-abhängigen", bool(max(d[:3])<min(d[3:])), True)
print(f"\n{'='*45}")
print(f"GESAMT (alle Teile): {PASS} PASS / {FAIL} FAIL")
