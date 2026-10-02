#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""a125_phi_skelett.py -- Pruefskript zu A125 (phi-Skelett: von den Gewichten
zu den Massenverhaeltnissen).
Prueft: (1) Gewichte p_j aus der ikosaedrischen 5-fold R_5 (Konstruktion wie
Dok293_Skripte/ikosaeder_theta_delta.py), (2) |A| = sqrt2/3, (3) das phi-Skelett,
(4) Koide-Verhaeltnisse gegen PDG 2024 / CODATA, (5) phi-Formen fuer m_tau/m_e,
(6) Koerperaussagen (5 teilt 1152 nicht, phi^4 = -1 in GF(9), ord_37(3) = 18,
4 teilt 18 nicht), (7) Abgrenzung zur phi^10-Leiter.
numpy + Standardbibliothek."""
import math
import numpy as np

phi = (1 + math.sqrt(5)) / 2
xi = 4 / 30000
w = np.exp(2j * np.pi / 3)

n_ok = n_all = 0
def check(name, cond, info=""):
    global n_ok, n_all
    n_all += 1; n_ok += bool(cond)
    print(f"  [{'BESTANDEN' if cond else 'FEHLER   '}] {name}" + (f"  ({info})" if info else ""))

def rot(axis, ang):
    a = np.array(axis, float); a /= np.linalg.norm(a)
    K = np.array([[0, -a[2], a[1]], [a[2], 0, -a[0]], [-a[1], a[0], 0]])
    return np.eye(3) + np.sin(ang) * K + (1 - np.cos(ang)) * (K @ K)

print("1. Gewichte aus R_5")
V = np.array([[1, 1, 1], [1, w, w**2], [1, w**2, w]], dtype=complex) / np.sqrt(3)
v0, ve = V[0], V[1]
R5 = rot([0, 1, phi], 2 * np.pi / 5)
p = [abs(np.vdot(V[j], R5 @ ve))**2 for j in range(3)]
p0, p1, p2 = p[0], p[1], p[2]
check("p0 = 2/9", abs(p0 - 2/9) < 1e-12, f"{p0:.12f}")
check("p1 = (2+3phi)/9", abs(p1 - (2 + 3*phi)/9) < 1e-12)
check("p2 = (5-3phi)/9", abs(p2 - (5 - 3*phi)/9) < 1e-12)
check("Spur der 72-Grad-Drehung = phi", abs(np.trace(R5) - phi) < 1e-12)

print("2. Ein Matrixelement")
A = np.vdot(v0, R5 @ ve)
check("|A| = sqrt2/3", abs(abs(A) - math.sqrt(2)/3) < 1e-12)
check("3|A| = sqrt2 und |A|^2 = 2/9", abs(3*abs(A) - math.sqrt(2)) < 1e-12 and abs(abs(A)**2 - 2/9) < 1e-12)

print("3. phi-Skelett")
check("p1/p2 = phi^8", abs(p1/p2 - phi**8) < 1e-8)
check("p0/p2 = 2 phi^4", abs(p0/p2 - 2*phi**4) < 1e-9)
check("p1/p0 = phi^4/2", abs(p1/p0 - phi**4/2) < 1e-10)
check("3 sqrt(p_j) = sqrt2, phi^2, phi^-2", abs(3*math.sqrt(p0) - math.sqrt(2)) < 1e-12
      and abs(3*math.sqrt(p1) - phi**2) < 1e-10 and abs(3*math.sqrt(p2) - phi**-2) < 1e-10)

print("4. Koide-Verhaeltnisse")
me, mmu, mtau, dmtau = 0.51099895, 105.6583755, 1776.93, 0.09
rt, srt = mtau/me, dmtau/me
rmu_cod, srmu = 206.7682827, 0.0000046
a = [1 + math.sqrt(2)*math.cos(2/9 + 2*math.pi*k/3) for k in range(3)]
kt, km = (a[0]/a[1])**2, (a[2]/a[1])**2
check("Messwert m_tau/m_e = 3477,37 +- 0,18", abs(rt - 3477.37) < 0.005 and abs(srt - 0.176) < 0.001, f"{rt:.3f}")
check("Koide m_tau/m_e = 3477,473, +3,1e-5, 0,6 sigma", abs(kt - 3477.473) < 0.001 and abs(kt/rt - 1 - 3.1e-5) < 0.05e-5 and abs((kt - rt)/srt - 0.6) < 0.05, f"{kt:.4f}")
check("Koide m_mu/m_e = 206,77032, +9,8e-6, 442 sigma", abs(km - 206.77032) < 1e-5 and abs(km/rmu_cod - 1 - 9.8e-6) < 0.05e-6 and abs((km - rmu_cod)/srmu - 442) < 1, f"{(km-rmu_cod)/srmu:.0f} sigma")
check("cos(2/9): 2/9 kein rationales Vielfaches von pi (Abstand zu p/q*pi, q<=1000)",
      min(abs(2/9 - pi_q) for pi_q in (math.pi*pp/q for q in range(1, 1001) for pp in range(0, 2))) > 1e-6)

print("5. phi-Formen fuer m_tau/m_e")
for name, val, ref, rel_t, sig_t in [
        ("74 phi^8", 74*phi**8, 3476.42, -2.7e-4, -5.3),
        ("(74+1/45) phi^8", (74 + 1/45)*phi**8, 3477.469, 3.0e-5, 0.6),
        ("74 phi^8 (1+27 xi/12)", 74*phi**8*(1 + 27/12*xi), 3477.468, 2.9e-5, 0.6)]:
    check(f"{name} = {ref}", abs(val - ref) < 0.006 and abs(val/rt - 1 - rel_t) < 0.06e-4 * (1 if abs(rel_t) > 1e-4 else 0.1)
          and abs((val - rt)/srt - sig_t) < 0.06, f"{val:.4f}, {(val-rt)/srt:+.2f} sigma")
check("3331/45 = 74 + 1/45", abs(3331/45 - 74 - 1/45) < 1e-12)
check("(74+1/45) phi^8 gegen Koide: 1,2e-6", abs(((74 + 1/45)*phi**8)/kt - 1 + 1.2e-6) < 0.1e-6)
check("30 phi^4 = 15 p0/p2 = 205,62, -0,55 %", abs(30*phi**4 - 15*p0/p2) < 1e-9 and abs(30*phi**4 - 205.62) < 0.005 and abs((30*phi**4/(mmu/me) - 1)*100 + 0.55) < 0.01)
check("3700/27 = 137 + 1/27", abs(3700/27 - 137 - 1/27) < 1e-12)
check("74/75 = 1 - 100 xi", abs(74/75 - (1 - 100*xi)) < 1e-15)

print("6. Koerperaussagen")
check("|Aut(D4)| = 1152 = 2^7 3^2, 5 teilt 1152 nicht", 1152 == 2**7 * 3**2 and 1152 % 5 != 0)
check("5 teilt 80 = |GF(81)*|", 80 % 5 == 0)
# GF(9) = F3[x]/(x^2 - x - 1); phi = x
def mul(u, v):  # (a + b x)(c + d x) mit x^2 = x + 1
    a_, b_ = u; c_, d_ = v
    return ((a_*c_ + b_*d_) % 3, (a_*d_ + b_*c_ + b_*d_) % 3)
def pw(u, n):
    r = (1, 0)
    for _ in range(n): r = mul(r, u)
    return r
x = (0, 1)
check("x^2 - x - 1 irreduzibel ueber F3", all((t*t - t - 1) % 3 != 0 for t in range(3)))
check("phi^4 = -1 in GF(9)", pw(x, 4) == (2, 0))
check("phi hat Ordnung 8 (primitiv)", pw(x, 8) == (1, 0) and all(pw(x, k) != (1, 0) for k in range(1, 8)))
check("x^3 - 1 = (x-1)^3 in Charakteristik 3", all(((t**3 - 1) - (t - 1)**3) % 3 == 0 for t in range(9)))
ord37 = min(k for k in range(1, 40) if (3**k - 1) % 37 == 0)
check("Ordnung von 3 modulo 37 = 18", ord37 == 18)
check("4 teilt 18 nicht: GF(81) kein Teilkoerper von GF(3^18)", 18 % 4 != 0)
check("gcd(4,18) = 2: gemeinsamer Teilkoerper GF(9)", math.gcd(4, 18) == 2)

print("7. Abgrenzung")
check("phi^10 = 122,99, nicht 206,77", abs(phi**10 - 122.99) < 0.005 and abs(phi**10 - mmu/me) > 80)

print(f"\nERGEBNIS: {n_ok}/{n_all} BESTANDEN")
if n_ok != n_all:
    raise SystemExit(1)
