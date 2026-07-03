#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Empirische Nachrechnung des FFGFT-Leptonsektors -- RICHTUNG UMGEKEHRT:
Start sind die PDG-Daten, geprueft wird, was die FFGFT-Relationen daraus
machen (statt ξ->Vorhersage). Kompatibilitaets-Modus per Johanns Vorgabe.
numpy-only, seed 20780458. Konventionen aus Dok 282/116/006/046 (K2: r_tau=25/9).

Ebenen:
  A  Koide Q aus PDG (+ Unsicherheit, tau-dominiert)
  B  Brannen/Zirkulant-Fit: M, r_emp, theta_emp aus den Daten (alle Zuordnungen)
  C  Konsistenz Q <-> r  (Q=(1+r^2/2)/3)
  D  Zirkulant-VORWAERTS (r=sqrt2, theta=2/9 exakt): Verhaeltnisse vs. PDG
  E  xi-Leiter (m=r_i xi^{p_i} v): Verhaeltnisse vs. PDG; REVERSE-xi je Verhaeltnis
  F  Brueckenkonstanten je Lepton (P40: nur Verhaeltnisse exakt): v_eff, r_eff
  G  Invertierungen: m_tau fuer Q=2/3 exakt bzw. theta=2/9 exakt
  H  K_frak-Gegenprobe der Leiter-Abweichungen
"""
import numpy as np
np.random.seed(20780458)

# ---- PDG-Eingaben (MeV) ----
m_e,  s_e  = 0.51099895069, 1.6e-10
m_mu, s_mu = 105.6583755,   2.3e-6
m_ta, s_ta = 1776.86,       0.12          # PDG; Empfindlichkeit unten ausgewiesen

xi   = 4/30000
v    = 246.22e3                            # MeV (Higgs-VEV)
r_th = np.sqrt(2); th_th = 2/9

def koide(me,mm,mt):
    s = np.sqrt([me,mm,mt])
    return (me+mm+mt)/s.sum()**2

def brannen(me,mm,mt,order):
    """order: Tupel der Massen in k=0,1,2. Liefert (M, r, theta)."""
    s  = np.sqrt(np.array(order))
    sb = s.mean()
    A  = s/sb - 1.0                        # = r cos(theta+2pi k/3)
    z  = (2/3)*np.sum(A*np.exp(-1j*2*np.pi*np.arange(3)/3))   # = r e^{i theta}
    return sb**2, abs(z), np.angle(z) % (2*np.pi/3)

print("="*74)
print("A) KOIDE Q AUS PDG")
Q = koide(m_e,m_mu,m_ta)
# Unsicherheit numerisch (tau dominiert)
dQ = abs(koide(m_e,m_mu,m_ta+s_ta)-koide(m_e,m_mu,m_ta-s_ta))/2
print(f"   Q = {Q:.9f}  ±{dQ:.7f}   (2/3 = {2/3:.9f})")
print(f"   Q - 2/3 = {Q-2/3:+.3e}  ->  {(Q-2/3)/dQ:+.2f} sigma vom Exaktwert")

print("\nB) BRANNEN/ZIRKULANT-FIT (alle zyklischen Zuordnungen)")
best=None
for name,order in [("(e,mu,tau)",(m_e,m_mu,m_ta)),("(mu,tau,e)",(m_mu,m_ta,m_e)),
                   ("(tau,e,mu)",(m_ta,m_e,m_mu))]:
    M,r,th = brannen(m_e,m_mu,m_ta,order)
    print(f"   k=0,1,2 -> {name}:  r={r:.6f}  theta={th:.8f} rad  "
          f"(theta-2/9 = {th-2/9:+.2e})")
    if best is None or abs(th-2/9)<abs(best[2]-2/9): best=(name,M,th,r)
name,M,th,r = best
# theta-Unsicherheit aus tau
_,_,th_p = brannen(m_e,m_mu,m_ta+s_ta,(m_ta+s_ta,m_e,m_mu) if name=="(tau,e,mu)" else
                   ((m_e,m_mu,m_ta+s_ta) if name=="(e,mu,tau)" else (m_mu,m_ta+s_ta,m_e)))
_,_,th_m = brannen(m_e,m_mu,m_ta-s_ta,(m_ta-s_ta,m_e,m_mu) if name=="(tau,e,mu)" else
                   ((m_e,m_mu,m_ta-s_ta) if name=="(e,mu,tau)" else (m_mu,m_ta-s_ta,m_e)))
dth=abs(th_p-th_m)/2
print(f"   KANONISCH {name}:  M={M:.4f} MeV,  r_emp={r:.7f},")
print(f"   theta_emp = {th:.8f} ± {dth:.2e} rad;  |theta-2/9| = {abs(th-2/9):.2e}"
      f"  ({abs(th-2/9)/dth:.2f} sigma)")

print("\nB2) THETA AUS m_mu/m_e ALLEIN (tau-frei, r=sqrt2 fix; Dok 282 §Skript)")
fmue = lambda t: ((1+r_th*np.cos(t+2*np.pi*2/3))/(1+r_th*np.cos(t+2*np.pi*1/3)))**2
lo,hi=0.20,0.24
g=lambda t: fmue(t)-R_mue if False else None
def _b(f,lo,hi,n=200):
    for _ in range(n):
        mid=(lo+hi)/2
        if f(lo)*f(mid)<=0: hi=mid
        else: lo=mid
    return (lo+hi)/2
R_mue = m_mu/m_e
th_mue=_b(lambda t: fmue(t)-R_mue, lo,hi)
print(f"   theta(mu/e) = {th_mue:.10f};  |theta-2/9| = {abs(th_mue-2/9):.3e}")
print("   (reproduziert Dok 282: ~1.8e-7, sieben signifikante Stellen; die")
print("    Restdifferenz ist NICHT unabhaengig, sondern dieselbe ~0.9-sigma-")
print("    tau-Spannung wie in A/G -- bei frei flottierendem r via Q verschwindet sie.)")

print("\nC) KONSISTENZ Q <-> r:  r(Q) = sqrt(6Q-2)")
r_from_Q = np.sqrt(6*Q-2)
print(f"   r aus Q: {r_from_Q:.7f}   vs. r_emp(Fit) {r:.7f}   vs. sqrt2 {r_th:.7f}")
print(f"   r_emp - sqrt2 = {r-r_th:+.2e}")

print("\nD) ZIRKULANT VORWAERTS (r=sqrt2, theta=2/9 EXAKT) -> Verhaeltnisse")
k = np.arange(3)
s_th = 1 + r_th*np.cos(th_th + 2*np.pi*k/3)
m_th = s_th**2
# Zuordnung aus B uebernehmen: name gibt an, welches k welches Lepton ist
lept = {"(e,mu,tau)":["e","mu","tau"],"(mu,tau,e)":["mu","tau","e"],
        "(tau,e,mu)":["tau","e","mu"]}[name]
idx = {l:i for i,l in enumerate(lept)}
R_mue_th = m_th[idx["mu"]]/m_th[idx["e"]]
R_tamu_th= m_th[idx["tau"]]/m_th[idx["mu"]]
R_mue, R_tamu = m_mu/m_e, m_ta/m_mu
print(f"   m_mu/m_e :  Zirkulant {R_mue_th:.4f}   PDG {R_mue:.4f}   "
      f"Abw {100*(R_mue_th/R_mue-1):+.4f}%")
print(f"   m_tau/m_mu: Zirkulant {R_tamu_th:.4f}    PDG {R_tamu:.4f}    "
      f"Abw {100*(R_tamu_th/R_tamu-1):+.4f}%")

print("\nE) XI-LEITER  m_i = r_i xi^{p_i} v   (e:4/3,3/2 | mu:16/5,1 | tau:25/9,2/3)")
lad = {"e":(4/3,1.5), "mu":(16/5,1.0), "tau":(25/9,2/3)}
Rmue_l  = (lad["mu"][0]/lad["e"][0]) * xi**(lad["mu"][1]-lad["e"][1])
Rtamu_l = (lad["tau"][0]/lad["mu"][0])* xi**(lad["tau"][1]-lad["mu"][1])
Rtae_l  = (lad["tau"][0]/lad["e"][0]) * xi**(lad["tau"][1]-lad["e"][1])
print(f"   m_mu/m_e :  Leiter {Rmue_l:.4f}   PDG {R_mue:.4f}    Abw {100*(Rmue_l/R_mue-1):+.3f}%")
print(f"   m_tau/m_mu: Leiter {Rtamu_l:.4f}    PDG {R_tamu:.4f}     Abw {100*(Rtamu_l/R_tamu-1):+.3f}%")
print(f"   m_tau/m_e : Leiter {Rtae_l:.1f}    PDG {m_ta/m_e:.1f}     Abw {100*(Rtae_l/(m_ta/m_e)-1):+.3f}%")
print("   REVERSE-xi (aus PDG-Verhaeltnis geloest; Soll 4/30000 = 1.33333e-4):")
xi_mue  = ((12/5)/R_mue)**2
xi_tamu = ((125/144)/R_tamu)**3
xi_tae  = ((25/12)/(m_ta/m_e))**(6/5)
for lbl,x in [("mu/e ",xi_mue),("tau/mu",xi_tamu),("tau/e ",xi_tae)]:
    print(f"     xi[{lbl}] = {x:.5e}   ({100*(x/xi-1):+.2f}% vs. 4/30000)")

print("\nF) BRUECKENKONSTANTEN (P40): v_eff = m/(r_i xi^{p_i});  r_eff bei v=246.22 GeV")
for l,m in [("e",m_e),("mu",m_mu),("tau",m_ta)]:
    ri,pi = lad[l]
    veff = m/(ri*xi**pi)/1e3               # GeV
    reff = m/(v*xi**pi)
    print(f"   {l:3s}: v_eff = {veff:8.2f} GeV ({100*(veff/246.22-1):+.2f}%)"
          f"   r_eff = {reff:.4f}  (Soll {ri:.4f}, {100*(reff/ri-1):+.2f}%)")

print("\nG) INVERTIERUNGEN (was muesste m_tau sein?)")
from_scratch = lambda f,lo,hi: _bisect(f,lo,hi)
def _bisect(f,lo,hi,n=200):
    for _ in range(n):
        mid=(lo+hi)/2
        if f(lo)*f(mid)<=0: hi=mid
        else: lo=mid
    return (lo+hi)/2
mt_Q  = _bisect(lambda mt: koide(m_e,m_mu,mt)-2/3, 1700, 1850)
def th_of(mt):
    _,_,t = brannen(m_e,m_mu,mt,(mt,m_e,m_mu) if name=="(tau,e,mu)" else
                    ((m_e,m_mu,mt) if name=="(e,mu,tau)" else (m_mu,mt,m_e)))
    return t
mt_th = _bisect(lambda mt: th_of(mt)-2/9, 1770, 1785)
print(f"   Q=2/3 exakt   ->  m_tau = {mt_Q:.3f} MeV   (PDG {m_ta}±{s_ta}: "
      f"{(mt_Q-m_ta)/s_ta:+.2f} sigma)")
print(f"   theta=2/9 exakt-> m_tau = {mt_th:.3f} MeV   ({(mt_th-m_ta)/s_ta:+.2f} sigma)")
# Vorwaerts-VORHERSAGE: m_tau aus (m_e,m_mu; r=sqrt2, theta=2/9)
s0 = np.array([1+r_th*np.cos(th_th+2*np.pi*kk/3) for kk in range(3)])  # (tau,e,mu)
sq = np.array([np.sqrt(m_e), np.sqrt(m_mu)])
Mfit = np.sum(sq*s0[1:])/np.sum(s0[1:]**2)
mt_pred=(Mfit*s0[0])**2
print(f"   VORHERSAGE m_tau aus (m_e,m_mu; sqrt2, 2/9): {mt_pred:.3f} MeV "
      f"({(mt_pred-m_ta)/s_ta:+.2f} sigma; Belle-II-Praezision ~0.05 MeV entscheidet)")

print("\nH) K_frak-GEGENPROBE der Leiter-Abweichungen (K_frak = 1-100xi = -1.333%)")
for lbl,dev in [("mu/e", 100*(Rmue_l/R_mue-1)), ("tau/mu",100*(Rtamu_l/R_tamu-1))]:
    print(f"   Leiter-Abweichung {lbl}: {dev:+.3f}%   "
          f"(K_frak^1: -1.333%, K_frak^(1/2): -0.665%, K_frak^(3/2): -1.995%)")
print("\nHinweis P40: Absolutwerte tragen die Brueckenkonstante; exakt sind nur")
print("Verhaeltnisse. Der Zirkulant (D) traegt die 4-5-Stellen-Genauigkeit,")
print("die xi-Leiter (E) die ~1%-Genauigkeit -- beide Ebenen getrennt gebucht.")

print("\n"+"="*74)
print("I) RELATION ZU DEN MESSGENAUIGKEITEN (2-Parameter-Analyse)")
R1,R2 = m_mu/m_e, m_ta/m_mu
sR1 = R1*np.sqrt((s_mu/m_mu)**2+(s_e/m_e)**2)
sR2 = R2*np.sqrt((s_ta/m_ta)**2+(s_mu/m_mu)**2)
print(f"   sigma(R1)/R1 = {sR1/R1:.2e} (mu/e),  sigma(R2)/R2 = {sR2/R2:.2e} (tau/mu)")
print(f"   -> mu/e ist {sR2/R2/(sR1/R1):.0f}x praeziser: die Daten bestimmen (r,theta)")
print("      extrem ANISOTROP (duenne Richtung ~1e-8, dicke Richtung ~1e-5).")
def _ratios(r,th):
    sk=np.array([1+r*np.cos(th+2*np.pi*kk/3) for kk in range(3)])
    return (sk[2]/sk[1])**2,(sk[0]/sk[2])**2
x=np.array([np.sqrt(2),2/9])
for _ in range(60):
    rr,tt=x
    fv=np.array([_ratios(rr,tt)[0]-R1,_ratios(rr,tt)[1]-R2])
    J=np.zeros((2,2)); eps=1e-9
    for j in range(2):
        xp=x.copy(); xp[j]+=eps
        J[:,j]=(np.array([_ratios(*xp)[0]-R1,_ratios(*xp)[1]-R2])-fv)/eps
    x=x-np.linalg.solve(J,fv)
r_fit,th_fit=x
Ji=np.linalg.inv(J); Cov=Ji@np.diag([sR1**2,sR2**2])@Ji.T
w,V=np.linalg.eigh(Cov)
d=np.array([np.sqrt(2)-r_fit,2/9-th_fit]); dp=V.T@d
print(f"   Fit: r={r_fit:.8f}, theta={th_fit:.8f}")
print(f"   Hauptachsen-sigmas: {np.sqrt(w[0]):.2e} (duenn), {np.sqrt(w[1]):.2e} (dick)")
print(f"   Abstand (sqrt2,2/9) vom Fit: duenn {abs(dp[0])/np.sqrt(w[0]):.0f} sigma,"
      f"  dick {abs(dp[1])/np.sqrt(w[1]):.2f} sigma")
print("   BEFUND: (sqrt2, 2/9) EXAKT ist in der duennen (mu/e-)Richtung mit")
print("   ~450 sigma ausgeschlossen -- bestaetigt ist das Paar auf dem 1e-5-")
print("   Niveau (4-5 Stellen, wie Dok 282 deklariert). Der 1.75e-7-Rest in")
print("   theta ist ein HEUTE GEMESSENER Offset; auch ein perfektes Belle-II-")
print("   Ergebnis loest nur die dicke tau-Richtung, nicht diesen Rest.")
print("\n   XI-LEITER in sigma_exp-Einheiten:")
for lbl,dev,srel in [("mu/e",Rmue_l/R_mue-1,sR1/R1),("tau/mu",Rtamu_l/R_tamu-1,sR2/R2),
                     ("tau/e",Rtae_l/(m_ta/m_e)-1,np.sqrt((s_ta/m_ta)**2+(s_e/m_e)**2))]:
    print(f"     {lbl:6s}: {100*dev:+.2f}%  =  {abs(dev)/srel:9.0f} sigma_exp")
print("   -> Leiter-Residuen sind theorieseitig (P40), nicht datenlimitiert;")
print("      die Messpraezision hat die Leiter um 1e2..1e5 ueberholt.")
print("\n   Testschaerfe der m_tau-Vorhersage (dicke Richtung):")
for st in (0.12,0.05,0.02):
    print(f"     sigma(m_tau)={st}: |1776.968-1776.86|/sigma = {0.108/st:.1f} sigma")

print("\n"+"="*74)
print("J) ALPHA AUS DEN LEPTONMASSEN (Dok 011: alpha^-1 = 7500/E0^2 * K_frak)")
alpha=7.2973525693e-3; Kf=1-100*xi
E0s=np.sqrt(m_e*m_mu)
E0r=np.sqrt(alpha/xi)
print(f"   E0 strukturell sqrt(m_e*m_mu) = {E0s:.5f} MeV;  E0 aus alpha = {E0r:.5f} MeV")
print(f"   Verhaeltnis {E0r/E0s:.6f} vs K_frak^(-1/2) = {Kf**-0.5:.6f}"
      f"  -> Match {100*abs(E0r/E0s*Kf**0.5-1):.4f}%")
a_pred=xi*m_e*m_mu/Kf
print(f"   Geschlossen (nur xi, K_frak=1-100xi, m_e, m_mu):")
print(f"     1/alpha_pred = {1/a_pred:.4f}   vs gemessen 137.035999")
print(f"     Abweichung {100*(a_pred/alpha-1):+.4f}%  (= {abs(a_pred/alpha-1)/1.5e-10:.1e} sigma_exp:")
print(f"     theorieseitiges Residuum wie die Leiter; naechste Ordnung offen)")
print(f"   Mit Brueckenkonstante E0=7.398 (P40, Kalibrierung): {100*(xi*7.398**2/alpha-1):+.5f}%")
print("   Konzeptionell: im erweiterten Natursystem ist alpha=1 (Dok 011/014);")
print("   der SI-Wert ist Buchhaltung -- dieselbe Architektur wie G (Dok 012/013).")

print("\n"+"="*74)
phi=(1+np.sqrt(5))/2
print("K) LEITERUEBERGREIFENDE KOPPLUNG (generationslineares Korrekturgesetz)")
Kf2=1-100*xi; ln=np.log(Kf2)
def _p(raw,meas): return np.log(meas/raw)/ln
def _N(raw,meas): return (1-meas/raw)/xi
p1=_p((12/5)*xi**-0.5, m_mu/m_e); N1=_N((12/5)*xi**-0.5, m_mu/m_e)
p2=_p((125/144)*xi**(-1/3), m_ta/m_mu); N2=_N((125/144)*xi**(-1/3), m_ta/m_mu)
p3=_p((25/12)*xi**(-5/6), m_ta/m_e); N3=_N((25/12)*xi**(-5/6), m_ta/m_e)
print(f"   Exponenten: p1={p1:.4f} p2={p2:.4f} p3={p3:.4f}")
print(f"   Multiplikativ konsistent: p1+p2={p1+p2:.4f} = p3 (Diff {abs(p3-(p1+p2)):.1e})")
print(f"   -> tau/e traegt keine neue Info, ist Produkt der Stufen.")
print(f"   Faktoren: N1={N1:.2f} N2={N2:.2f} N3={N3:.2f}")
print(f"   Verhaeltnis N1:N2:N3 = 1:{N2/N1:.3f}:{N3/N1:.3f} ~ 1:2:3 (generationslinear)")
print(f"   N0-Schaetzungen N1, N2/2, N3/3 = {N1:.2f},{N2/2:.2f},{N3/3:.2f} (Mittel {(N1+N2/2+N3/3)/3:.2f})")
print(f"   OFFEN: N0~38.6 nicht hergeleitet (100/e={100/np.e:.2f}, 100/phi^2={100/phi**2:.2f}, 39);")
print(f"          delta-Phasensektor (p=-0.88) fuegt sich nicht offensichtlich ein.")
print()
print("   MODUS-WARNUNG (P42): dieses N_g-Gesetz gilt NUR referenzfrei (Modus 1,")
print("   alle Verhaeltnisse aus xi vorhergesagt). Sobald mu/e als P42-Anker")
print("   deklariert wird, faellt es als Pruefpunkt weg -> 1:2:3 nur noch an")
print("   tau/mu, tau/e belegt (gleiche tau-Masse, geringe Praezision). mu/e als")
print("   Anker UND Pruefpunkt zu nutzen waere unzulaessige Doppelbuchung. Der")
print("   Zirkulant traegt mu/e ohnehin auf 1e-5 ohne g-Korrektur.")

print("\n"+"="*74)
print("L) ABWEICHUNGS-TOLERANZ-BILANZ (nur Modus 1, referenzfrei)")
print("   Wieviel schliesst das N_g=g*N0-Gesetz von der Leiter-Abweichung?")
sr={"mu/e":np.sqrt((s_mu/m_mu)**2+(s_e/m_e)**2),
    "tau/mu":np.sqrt((s_ta/m_ta)**2+(s_mu/m_mu)**2),
    "tau/e":np.sqrt((s_ta/m_ta)**2+(s_e/m_e)**2)}
raws={"mu/e":((12/5)*xi**-0.5, m_mu/m_e, 1),
      "tau/mu":((125/144)*xi**(-1/3), m_ta/m_mu, 2),
      "tau/e":((25/12)*xi**(-5/6), m_ta/m_e, 3)}
# gemeinsames N0 (Mittel der Einzelschaetzungen)
N0=np.mean([(1-meas/raw)/(g*xi) for raw,meas,g in raws.values()])
print(f"   gemeinsames N0 = {N0:.3f}")
print(f"   {'Stelle':8s} {'roh %':>9s} {'roh sig':>10s} {'korr %':>10s} {'korr sig':>10s}")
for lbl,(raw,meas,g) in raws.items():
    dr=raw/meas-1
    corr=raw*(1-g*N0*xi)
    dc=corr/meas-1
    print(f"   {lbl:8s} {100*dr:+8.3f} {abs(dr)/sr[lbl]:10.1e} {100*dc:+9.4f} {abs(dc)/sr[lbl]:10.1e}")
print("   -> tau/mu, tau/e fallen IN die Toleranz (<1 sigma); mu/e bleibt bei")
print("      ~1.5e3 sigma, weil es 500x praeziser gemessen ist. ABER (P42):")
print("      mu/e ist im referenzierten Modus der ANKER -> faellt aus der Bilanz,")
print("      die 1500 sigma sind nur im referenzfreien Modus ueberhaupt eine Aussage.")
print()
print("   Zirkulant vs Leiter fuer mu/e (verschiedene Schichten, nicht mischen):")
k=np.arange(3); sth=1+np.sqrt(2)*np.cos(2/9+2*np.pi*k/3); mth=sth**2
print(f"     Zirkulant (r=sqrt2,theta=2/9): {100*(mth[2]/mth[1]/(m_mu/m_e)-1):+.4f}%")
print(f"     Leiter roh:                    {100*((12/5)*xi**-0.5/(m_mu/m_e)-1):+.4f}%")
print(f"     -> Zirkulant traegt die Praezision (1e-5), Leiter die Groessenordnung (1e-2).")
print()
print("   FAZIT Toleranz: referenziert steht eine scharfe Pruefung (m_tau, Zirkulant);")
print("   referenzfrei bringt N_g die Leiter von ~1% auf ~5e-3% (Faktor ~300), tau-")
print("   Stellen in Toleranz, Rest sitzt in der 1:2:3-Feinabweichung (~1-2%) und N0.")
