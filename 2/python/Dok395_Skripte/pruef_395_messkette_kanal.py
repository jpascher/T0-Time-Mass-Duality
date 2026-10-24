"""
pruef_395_messkette_kanal.py -- Dok. 395: Die Messkette als Kanal.
Johann Pascher, ORCID 0009-0000-6518-4064, 24. Oktober 2026

Prüft die Zahlen aus Dok. 395: Kanalschätzung mit Pilot (Verhältnis- und SI-Sektor),
Schranke für einen modenabhängigen Kanalfaktor aus der Koide-Form, Regenerationsgrenze
Q_c = pi/sqrt(6 eps) (Dok. 343) und Shannon-Bilanz einzelner Treffer.
Reines Python, keine Zusatzpakete.
"""
import math

ok = n = 0
def check(name, cond, info=""):
    global ok, n
    n += 1; ok += bool(cond)
    print(f"  [{'OK ' if cond else 'FAIL'}] {name}" + (f"  ({info})" if info else ""))

xi = 4/30000
me, mmu = 0.51099895069, 105.6583755           # CODATA 2022
s_me, s_mmu = 0.00000000016, 0.0000023
mtau, s_tau = 1776.93, 0.09                     # PDG (pdgLive 2026)
ainv, s_a = 137.035999177, 0.000000021          # CODATA 2022
K_rule = 74/75

def koide(th, a):
    s = sorted((1 + a*math.cos(th + 2*math.pi*k/3))**2 for k in range(3))
    return s[1]/s[0], s[2]/s[1]

# ---------------------------------------------------------------------------
print("1. Pilot im Verhältnissektor: Koide (theta = 2/9, d/c = sqrt 2)")
r1m, r2m = mmu/me, mtau/mmu
k1, k2 = koide(2/9, math.sqrt(2))
H1, H2 = r1m/k1, r2m/k2
s1 = math.hypot(s_me/me, s_mmu/mmu); s2 = math.hypot(s_tau/mtau, s_mmu/mmu)
check("Kanalfaktor m_mu/m_e: H - 1 = -0,074 xi (Messfehler 2e-8)", abs((H1-1)/xi + 0.074) < 0.002, f"{(H1-1)/xi:+.4f} xi")
check("Kanalfaktor m_tau/m_mu: H - 1 = -0,16 +- 0,38 xi", abs((H2-1)/xi + 0.158) < 0.01 and abs(s2/xi - 0.38) < 0.01,
      f"{(H2-1)/xi:+.3f} +- {s2/xi:.3f} xi")
check("Verhältnissektor flach: beide Faktoren unter 1 xi, gegen 100 xi des SI-Faktors", abs(H1-1) < xi and abs(H2-1) < xi)

print("\n2. Pilot mit Modellfehler: die Leiter")
l1, l2 = 12/5*xi**-0.5, 125/144*xi**(-1/3)
check("Leiter als Pilot verlangt je Generation eigenen Kanalfaktor: Leiter liegt 39,10 xi und 77,56 xi über der Messung",
      abs((l1/r1m-1)/xi - 39.10) < 0.01 and abs((l2/r2m-1)/xi - 77.56) < 0.02, f"{(l1/r1m-1)/xi:.2f}, {(l2/r2m-1)/xi:.2f}")
check("dieser 'Kanal' ist der Abstand Leiter-Koide (ohne Messwert): 39,02 und 77,40 xi", abs((l1/k1-1)/xi-39.02) < 0.01 and abs((l2/k2-1)/xi-77.40) < 0.01)

print("\n3. Pilot im SI-Sektor: alpha")
K_a = xi*me*mmu*ainv
check("alpha schätzt den SI-Kanal: K = 0,986501 (n = 101,25)", abs(K_a-0.986501) < 1e-6 and abs((1-K_a)/xi-101.246) < 0.001)
check("Schätzung ohne Rauschproblem: Unsicherheit von K unter 3e-8", K_a*math.hypot(s1, s_a/ainv) < 3e-8)
K54 = 54*xi*ainv
check("in der Einheit E_u (m_e m_mu = 54) schätzt alpha K = 0,986659 (n = 100,056)", abs((1-K54)/xi-100.056) < 0.001)

print("\n4. Eigenbasis: Schranke für einen modenabhängigen Kanalfaktor")
b12 = abs(H1-1)/xi + 2*s1/xi
b23 = abs(H2-1)/xi + 2*s2/xi
check("Unterschied Elektron-Myon höchstens 0,074 xi", b12 < 0.075, f"{b12:.4f} xi")
check("Unterschied Myon-Tau höchstens 0,92 xi (2 sigma)", abs(b23-0.92) < 0.01, f"{b23:.3f} xi")
check("modenabhängiger Anteil höchstens rund 1 % des 100-xi-Schritts", b23/100 < 0.01)

print("\n5. Koide-Parameter frei angepasst")
def fit(r1, r2):
    th, a = 2/9, math.sqrt(2)
    for _ in range(50):
        f1, f2 = koide(th, a); F = (math.log(f1/r1), math.log(f2/r2))
        h = 1e-7
        a1 = koide(th+h, a); a2 = koide(th, a+h)
        J = [[(math.log(a1[0]/r1)-F[0])/h, (math.log(a2[0]/r1)-F[0])/h],
             [(math.log(a1[1]/r2)-F[1])/h, (math.log(a2[1]/r2)-F[1])/h]]
        det = J[0][0]*J[1][1]-J[0][1]*J[1][0]
        dth = (F[0]*J[1][1]-F[1]*J[0][1])/det; da = (J[0][0]*F[1]-J[1][0]*F[0])/det
        th -= dth; a -= da
    return th, a
th0, a0 = fit(r1m, r2m)
thp, ap = fit(r1m, (mtau+s_tau)/mmu)
sth, sa = abs(thp-th0), abs(ap-a0)
check("angepasstes theta = 2/9 innerhalb der Tau-Unsicherheit", abs(th0-2/9) < 2*sth, f"theta = {th0:.7f}, 2/9 = {2/9:.7f}, sigma {sth:.1e}")
check("angepasste Amplitude = sqrt 2 innerhalb der Tau-Unsicherheit", abs(a0-math.sqrt(2)) < 2*sa, f"a = {a0:.7f}, sigma {sa:.1e}")

print("\n6. Regeneration: Q_c = pi/sqrt(6 eps) (Dok. 343)")
Qc = lambda e: math.pi/math.sqrt(6*e)
check("SI-Korrektur 100 xi (1,33 %): Q_c = 11,1", abs(Qc(100*xi)-11.1) < 0.05)
check("m_tau/m_mu (5,1e-5): Q_c = 180", abs(Qc(s2)-180) < 2, f"{Qc(s2):.0f}")
check("m_mu/m_e (2,2e-8): Q_c = 8700", abs(Qc(s1)-8700) < 100, f"{Qc(s1):.0f}")
check("alpha (1,5e-10): Q_c = 1,0e5", abs(Qc(s_a/ainv)-1.04e5) < 0.03e5, f"{Qc(s_a/ainv):.3g}")
check("Nenner der Grundform (9, 5, 8, 75) bleiben nach der SI-Korrektur nur bis 11 eindeutig: 75 nicht",
      9 < Qc(100*xi) and 75 > Qc(100*xi))

print("\n7. Shannon-Bilanz: Information der Messung gegen Komplexität der Formel")
def info(dev_rel, sig_rel):
    d = max(abs(dev_rel), sig_rel)
    return math.log2(math.log(10)/(2*d))
def bits(p=1, q=1, d=1, k=1, m=0, nn=1, s=0):      # wie Dok. 393
    b = math.log2(p) + math.log2(q)
    if d > 1: b += math.log2(d) + math.log2(k)
    if m: b += 1 + math.log2(abs(m)) + math.log2(nn)
    if s: b += 1
    return b
rows = []
vEP = 246.21965/1.220890e19
rows.append(("v/E_P = xi^4/(5 pi)", info(xi**4/(5*math.pi)/vEP-1, 1e-5), bits(q=5, m=4, s=1)))
rows.append(("M_W/M_Z = sqrt(7/9)", info(math.sqrt(7/9)/(80.3692/91.1876)-1, 1.7e-4), bits(q=3, d=7, k=2)))
rows.append(("alpha^-1 = 3700/27 (frei gesucht)", info(3700/27/ainv-1, s_a/ainv), bits(p=3700, q=27)))
rows.append(("alpha^-1 = 7400/54 (Bestandteile)", info(3700/27/ainv-1, s_a/ainv), bits(q=54)))
rows.append(("m_e m_mu = 54 (nächste ganze Zahl)", math.log2((1/54)/(2*abs(me*mmu/54-1))), 0.0))
rows.append(("Koide theta = 2/9", info(th0/(2/9)-1, sth/(2/9)), bits(p=2, q=9)))
rows.append(("Koide d/c = sqrt 2", info(a0/math.sqrt(2)-1, sa/math.sqrt(2)), bits(d=2, k=2)))
for name, I, C in rows:
    print(f"     {name:36s} I = {I:5.1f} Bit, C = {C:5.1f} Bit, Überschuss {I-C:+5.1f} Bit")
S = {r[0]: r[1]-r[2] for r in rows}
check("3700/27 als frei gesuchter Bruch: kein Überschuss (so rechnet Dok. 393, p = 0,47)", S["alpha^-1 = 3700/27 (frei gesucht)"] < 1)
check("3700/27 nach Bestandteilen 7500*(74/75)/54: Überschuss über 11 Bit", S["alpha^-1 = 7400/54 (Bestandteile)"] > 11, f"{S['alpha^-1 = 7400/54 (Bestandteile)']:.1f}")
X = 7400/ainv
check("7400/alpha^-1 = 54,0004 liegt 7,6 ppm neben 54: Zufall rund 8e-4", abs(X-54.0004) < 1e-4 and abs(2*abs(X-54) - 8.2e-4) < 0.1e-4)
check("54: Überschuss rund 5,9 Bit (Zufall rund 1,7 %)", abs(S["m_e m_mu = 54 (nächste ganze Zahl)"]-5.85) < 0.1)
check("Koide theta = 2/9: Überschuss über 10 Bit", S["Koide theta = 2/9"] > 10, f"{S['Koide theta = 2/9']:.1f}")
check("Koide d/c = sqrt 2: Überschuss über 10 Bit", S["Koide d/c = sqrt 2"] > 10, f"{S['Koide d/c = sqrt 2']:.1f}")
check("v/E_P und M_W/M_Z: positiver, aber kleiner Überschuss (unter 7 Bit)",
      0 < S["v/E_P = xi^4/(5 pi)"] < 7 and 0 < S["M_W/M_Z = sqrt(7/9)"] < 7)

print("\n8. Was sich lösen lässt")
v = 246219.65
vm = 5/(16*xi)
check("tau_mu prüft v/m_mu: Leiter 5/(16 xi) = 2343,75 gegen 2330,34", abs(vm-2343.75) < 1e-9 and abs(v/mmu-2330.34) < 0.01)
r0 = (vm/(v/mmu)-1)/xi; rK = (vm/K_rule/(v/mmu)-1)/xi
check("Rest ohne K +43 xi, mit K +145 xi: ohne K 3,4-mal näher", abs(r0-43.2) < 0.1 and abs(rK-145.1) < 0.2 and abs(rK/r0-3.36) < 0.02,
      f"{r0:.1f}, {rK:.1f}")
lad = {"e": (4/3, 1.5, me), "mu": (16/5, 1.0, mmu), "tau": (25/9, 2/3, mtau)}
res = {k: ((1/(r*xi**p_))/(v/m)-1)/xi for k, (r, p_, m) in lad.items()}
check("Leiter auf v bezogen: e +82,5, mu +43,2, tau -34,0 xi", abs(res["e"]-82.5) < 0.2 and abs(res["mu"]-43.2) < 0.1 and abs(res["tau"]+34.0) < 0.2)
check("Differenzen 39 und 77 xi = Muster Leiter gegen Koide", abs(res["e"]-res["mu"]-39.3) < 0.5 and abs(res["mu"]-res["tau"]-77.2) < 0.5)
h = 1e-7; k0 = koide(2/9, math.sqrt(2))
va = [(math.log(koide(2/9, math.sqrt(2)+h)[i])-math.log(k0[i]))/h for i in range(2)]
vt = [(math.log(koide(2/9+h, math.sqrt(2))[i])-math.log(k0[i]))/h for i in range(2)]
check("Amplitude verschiebt fast nur m_mu/m_e: 32,6 gegen 1,8", abs(va[0]-32.6) < 0.1 and abs(va[1]-1.84) < 0.05)
Rr = (math.log(r1m/k1), math.log(r2m/k2))
def bound(vv):
    u = (vv[1], -vv[0]); nu = math.hypot(*u); u = (u[0]/nu, u[1]/nu)
    return (abs(u[0]*Rr[0]+u[1]*Rr[1]) + 2*math.hypot(u[0]*s1, u[1]*s2))/xi, u
bt, ut = bound(va); ba, ua = bound(vt)
check("nur theta = 2/9 exakt: gebundene Kombination fast nur Tau-Myon, <= 0,91 xi", abs(ut[1]) > 0.99 and abs(bt-0.91) < 0.01, f"{bt:.3f}")
check("nur d/c = sqrt 2 exakt: <= 0,92 xi", abs(ua[1]) > 0.99 and abs(ba-0.92) < 0.01, f"{ba:.3f}")

print("\n" + "="*70)
print(f"ERGEBNIS: {ok}/{n} Prüfungen bestanden")
assert ok == n
