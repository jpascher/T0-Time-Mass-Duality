#!/usr/bin/env python3
"""pruef_369_vier_wege.py — Dok. 369: Vier Wege zu den Leptonmassen, alle Zahlen der Synopse"""
import mpmath as mp
mp.mp.dps = 30
PASS=FAIL=0
def check(label,cond,detail=""):
    global PASS,FAIL
    ok="[PASS]" if cond else "[FAIL]"
    if cond: PASS+=1
    else: FAIL+=1
    print(f"  {ok} {label}"+(f"  ({detail})" if detail else ""))
def dev(a,b): return abs(a/b-1)*100

me,mmu,mtau = mp.mpf('0.51099895'),mp.mpf('105.6583755'),mp.mpf('1776.93')
R_me,R_te = mmu/me, mtau/me
xi=mp.mpf(4)/30000; phi=(1+mp.sqrt(5))/2
print("="*66+"\n  PRUEF 369 — Vier Wege zu den Leptonmassen\n"+"="*66)

print("\n[1] Weg 1: T0-Leiter")
r1_me=mp.mpf(12)/5*xi**(-mp.mpf(1)/2); r1_te=mp.mpf(25)/12*xi**(-mp.mpf(5)/6)
check("m_mu/m_e = 207.846 (Abw. 0.52%)", abs(r1_me-mp.mpf('207.846'))<0.001 and abs(dev(r1_me,R_me)-0.52)<0.01, f"{mp.nstr(dev(r1_me,R_me),3)}%")
check("m_tau/m_e = 3531.6 (Abw. 1.56%)", abs(r1_te-mp.mpf('3531.6'))<0.1 and abs(dev(r1_te,R_te)-1.56)<0.01, f"{mp.nstr(dev(r1_te,R_te),3)}%")
check("Rest m_mu/m_e = 39.1 xi", abs((r1_me/R_me-1)/xi-39.1)<0.2)
check("Rest m_tau/m_e = 117 xi (Dok.352: 117.4 mit PDG-alt m_tau=1776.86)", abs((r1_te/R_te-1)/xi-117.1)<0.3, f"{mp.nstr((r1_te/R_te-1)/xi,5)}")

print("\n[2] Weg 2: Koide theta=2/9")
th=mp.mpf(2)/9; a=[1+mp.sqrt(2)*mp.cos(th+2*mp.pi*k/3) for k in range(3)]
r2_me=(a[2]/a[1])**2; r2_te=(a[0]/a[1])**2
check("m_mu/m_e Abw. < 0.002%", dev(r2_me,R_me)<0.002, f"{mp.nstr(dev(r2_me,R_me),3)}%")
check("m_tau/m_e Abw. < 0.005%", dev(r2_te,R_te)<0.005, f"{mp.nstr(dev(r2_te,R_te),3)}%")
Q=(a[0]**2+a[1]**2+a[2]**2)/(a[0]+a[1]+a[2])**2
check("Q = 2/3 exakt", abs(Q-mp.mpf(2)/3)<1e-25)
s=mp.sqrt(me)+mp.sqrt(mmu); q=me+mmu
x=2*s+mp.sqrt(4*s**2-2*(mp.mpf(3)/2*q-s**2)); mt=x**2
check("m_tau aus Q=2/3: 1776.97 (Abw. < 0.003%)", abs(mt-mp.mpf('1776.97'))<0.01 and dev(mt,mtau)<0.003, f"{mp.nstr(mt,7)}")
check("innerhalb PDG-Unsicherheit tau (0.005%)", dev(r2_te,R_te)<0.005)

print("\n[3] Weg 3: Galois")
check("sqrt(43200) = Weg-1-Wert 207.846", abs(mp.sqrt(43200)-r1_me)<1e-10, "Weg 1 == Weg 3 fuer m_mu/m_e")
check("m_e*m_mu = 54 Abw. 0.016%", abs(dev(54,me*mmu)-0.016)<0.001, f"{mp.nstr(dev(54,me*mmu),3)}%")
check("43200 = 2^6*3^3*5^2", 43200==2**6*3**3*5**2)

print("\n[4] Weg 4: phi-Skelett")
p0=mp.mpf(2)/9; p1=(2+3*phi)/9; p2=(5-3*phi)/9
check("p1/p2 = phi^8", abs(p1/p2-phi**8)<1e-25)
check("p0/p2 = 2phi^4", abs(p0/p2-2*phi**4)<1e-25)
r4=74*phi**8; r4b=74*phi**8*(1+27*xi/12); r4m=30*phi**4
check("74phi^8 Abw. 0.027%", abs(dev(r4,R_te)-0.027)<0.002, f"{mp.nstr(dev(r4,R_te),3)}%")
check("74phi^8(1+27xi/12) Abw. < 0.003%", dev(r4b,R_te)<0.003, f"{mp.nstr(dev(r4b,R_te),3)}%")
check("30phi^4 Abw. 0.55%", abs(dev(r4m,R_me)-0.55)<0.01, f"{mp.nstr(dev(r4m,R_me),3)}%")

print("\n[5] Zwei Genauigkeitsklassen")
check("Klasse A (1,3,4a): alle >0.02%", min(dev(r1_me,R_me),dev(r1_te,R_te),dev(r4,R_te),dev(r4m,R_me))>0.02)
check("Klasse B (2,4b): alle <0.005%", max(dev(r2_me,R_me),dev(r2_te,R_te),dev(r4b,R_te))<0.005)

print("\n[6] Weg 5: M aus T0-Leiter")
v=mp.mpf(246000)
M=(me+mmu+mtau)/6
check("M = Σm/6 = 313.850", abs(M-mp.mpf('313.850'))<0.001, f"{mp.nstr(M,7)}")
check("M = m_tau/a_tau^2 exakt", abs(mtau/a[0]**2/M-1)<1e-5)
mb_e=mp.mpf(4)/3*xi**mp.mpf(1.5)*v; mb_mu=mp.mpf(16)/5*xi*v; mb_tau=mp.mpf(25)/9*xi**(mp.mpf(2)/3)*v
Mb=(mb_e+mb_mu+mb_tau)/6
check("M_bare = 314.82, Abw. 0.31%", abs(Mb-mp.mpf('314.82'))<0.01 and abs(dev(Mb,M)-0.31)<0.01, f"{mp.nstr(dev(Mb,M),3)}%")
check("Korrektur 23.1 xi", abs((Mb/M-1)/xi-23.1)<0.1, f"{mp.nstr((Mb/M-1)/xi,4)}")
check("tau-Anteil an M_bare 94%", abs(mb_tau/(mb_e+mb_mu+mb_tau)*100-94.4)<0.2)
check("Numerologie: 81*sqrt(15) Abw. 0.044% (NICHT im Korpus)", abs(dev(81*mp.sqrt(15),M)-0.044)<0.002)

print("\n"+"="*66+f"\n  ERGEBNIS: {PASS}/{PASS+FAIL} PASS\n"+"="*66)
