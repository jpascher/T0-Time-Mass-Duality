"""
pruef_394_korrekturabstaende.py -- Dok. 394: Wie weit die fraktalen Korrekturen voneinander abweichen.
Johann Pascher, ORCID 0009-0000-6518-4064, 23. Oktober 2026

Jede im Korpus vorkommende Korrektur wird als n in K = 1 - n*xi geschrieben und mit der Regel
n = 100 (K_frak = 74/75, Dok. 133/300/384) verglichen. Danach wird nach Herkunft sortiert.
Reines Python, keine Zusatzpakete.
"""
import math

ok = n = 0
def check(name, cond, info=""):
    global ok, n
    n += 1; ok += bool(cond)
    print(f"  [{'OK ' if cond else 'FAIL'}] {name}" + (f"  ({info})" if info else ""))

xi = 4/30000
eps = 100*xi                                   # = 1/75
me, mmu = 0.51099895069, 105.6583755          # MeV, CODATA 2022
mtau, dmtau = 1776.93, 0.09                    # MeV, PDG (pdgLive, Ausgabe 2026)
mtau_alt = 1776.86                             # im Korpus bisher verwendet
ainv = 137.035999177                           # CODATA 2022
hbar, c, MeV = 1.054571817e-34, 299792458.0, 1.602176634e-13
G_codata = 6.67430e-11
EP = math.sqrt(hbar*c**5/G_codata)/MeV
nof = lambda K: (1-K)/xi

print("1. Die Regel und ihre Form")
K_rule = 1-eps
check("K_frak = 1 - 100 xi = 74/75 exakt", abs(K_rule - 74/75) < 1e-15, f"{K_rule:.6f}")
K_mult = (1-xi)**100
check("multiplikative Form (1-xi)^100: n = 99,34", abs(nof(K_mult) - 99.34) < 0.01, f"n = {nof(K_mult):.3f}")
check("Abstand der Formen 8,8e-5", abs((K_mult-K_rule) - 8.8e-5) < 0.1e-5, f"{K_mult-K_rule:.2e}")

print("\n2. Der einzige echte Test der SI-Übersetzung: alpha")
K_a = xi*me*mmu*ainv
check("von alpha verlangt: K = xi me mmu / alpha = 0,98650", abs(K_a - 0.98650) < 1e-5, f"{K_a:.6f}")
check("n = 101,25 (Abstand zur Regel +1,25 xi)", abs(nof(K_a) - 101.25) < 0.01, f"n = {nof(K_a):.3f}")
check("relativ zu 74/75: -168 ppm", abs((K_a/K_rule-1)*1e6 + 168) < 1, f"{(K_a/K_rule-1)*1e6:.1f} ppm")
check("additive Form liegt näher als multiplikative (1,25 xi gegen 1,91 xi)",
      abs(nof(K_a)-100) < abs(nof(K_a)-nof(K_mult)), f"{nof(K_a)-100:.2f} / {nof(K_a)-nof(K_mult):.2f}")
E0n = math.sqrt(me*mmu)
K_MeV = (E0n*math.sqrt(xi*ainv))**2
check("1-MeV-Bezug (Dok. 386) ist dieselbe Zahl wie K aus alpha (identisch umgeformt)",
      abs(K_MeV - K_a) < 1e-12, f"{K_MeV:.6f}")
K_2 = 1-eps-eps**2
check("Kandidat zweiter Ordnung 1 - eps - eps^2: n = 101,33, verfehlt alpha um 12 ppm (nicht übernommen)",
      abs(nof(K_2)-101.333) < 0.001 and abs((K_2/K_a-1)*1e6 + 11.9) < 0.3, f"{(K_2/K_a-1)*1e6:.1f} ppm")
rel_unc = math.sqrt((0.15e-9)**2 + (0.3e-9)**2 + (2.2e-8)**2)
check("Messunsicherheit von K_alpha (< 3e-8) ist klein gegen den Rest 1,7e-4", rel_unc < 3e-8 and 1.68e-4/rel_unc > 1000)

print("\n2b. Richtung und Sitz des Restes")
P = me*mmu
bare = 1/(xi*P); pred = K_rule/(xi*P)
check("ohne Korrektur alpha^-1 = 138,911 (+1,37 %)", abs(bare-138.911) < 0.001 and abs(bare/ainv-1-0.01368) < 1e-4, f"{bare:.4f}")
check("mit Regel alpha^-1 = 137,059: Vorhersage zu groß (+168 ppm)", abs(pred-137.0591) < 1e-3 and pred > ainv, f"{pred:.4f}")
check("Regel liefert 98,8 % der verlangten Korrektur", abs((1-K_rule)/(1-K_a) - 0.9877) < 0.0005, f"{(1-K_rule)/(1-K_a):.4f}")
check("Faktor umgekehrt (alpha = xi me mmu K): +2,7 % (ausgeschlossen)", abs(1/(K_rule*xi*P)/ainv-1-0.0274) < 0.001)
for nm, a in (("g-2 2023", 137.035999166), ("Cs 2018", 137.035999046), ("Rb 2020", 137.035999206)):
    check(f"Messung {nm}: Abstand zur Regel bleibt 168,4 ppm", abs((pred/a-1)*1e6 - 168.4) < 0.1)
check("Streuung Cs-Rb 1,2 ppb, rund 1e5-mal kleiner als der Rest",
      abs((137.035999206-137.035999046)/ainv*1e9 - 1.17) < 0.05 and 1.68e-4/1.17e-9 > 1e5)
g = K_rule/(xi*54)
check("Galois: m_e m_mu = 54 mit Regel gibt 3700/27 exakt", abs(g - 3700/27) < 1e-10, f"{g:.5f}")
check("3700/27 liegt 7,6 ppm neben der Messung", abs((g/ainv-1)*1e6 - 7.6) < 0.1)
check("m_e m_mu = 53,9913 MeV^2 liegt 1,21 xi (161 ppm) unter 54", abs((P/54-1)/xi + 1.206) < 0.002, f"{(P/54-1)*1e6:.1f} ppm")
check("Zerlegung: 168,4 ppm = Produkt gegen 54 und Galois-Rest", abs(((54/P)*(g/ainv)-1)*1e6 - 168.4) < 0.1)
def _ipp(m):
    for q in range(2, m+1):
        if m % q == 0:
            while m % q == 0: m //= q
            return m == 1
    return False
_qs = [q for q in range(2, 82) if _ipp(q)]
_ord = (set(_qs) | {q-1 for q in _qs}) - {1}
_hits = {a*b for a in _ord for b in _ord if 40 <= a*b <= 70}
check("24 von 31 ganzen Zahlen in [40, 70] sind Produkte zweier Galois-Ordnungen (54 darunter)", len(_hits) == 24 and 54 in _hits)
check("Zufallswahrscheinlichkeit, 161 ppm neben einer ganzen Zahl zu liegen: 1,7 %", abs(2*161e-6*54 - 0.0174) < 0.0002)
X74 = 7400/ainv
check("3700/27 = 74/75 * 7500/54 = 7400/54 exakt", abs(3700/27 - (74/75)*7500/54) < 1e-12 and abs(7400/54 - 3700/27) < 1e-12)
check("7400/alpha^-1 = 54,0004: 7,6 ppm neben 54, Zufall rund 8e-4", abs((X74/54-1)*1e6 - 7.57) < 0.01 and abs(2*abs(X74-54) - 8.18e-4) < 0.02e-4)
check("zusammen mit der Nähe des Produkts (1,7 %): rund 1,4e-5", abs(2*abs(X74-54)*2*abs(P-54) - 1.42e-5) < 0.02e-5)
check("Reste gleich auf 7,6 ppm: K-Rest -168 ppm, Produkt-Rest -161 ppm", abs((K_a/K_rule-1)*1e6 + 168.3) < 0.1 and abs((P/54-1)*1e6 + 160.8) < 0.1)
Ry = 13.605693122990
check("m_e in MeV über die Rydberg-Energie: 2 Ry/alpha^2 = 0,51099895 MeV (Dok. 386)", abs(2*Ry/ainv**-2/1e6 - me) < 1e-9)
check("K_alpha über den Rydberg-Weg: xi (m_mu/m_e) (2 Ry/MeV)^2 alpha^-5 = 0,986501", abs(xi*(mmu/me)*(2*Ry*1e-6)**2*ainv**5 - K_a) < 1e-8)
u = (P/54)**0.5
check("genau 54 nur in einer Einheit 0,99992 MeV (80 ppm unter dem MeV)", abs(u - 0.999920) < 2e-6 and abs((1-u)*1e6 - 80.4) < 0.5, f"{u:.6f} MeV")
check("gemessenes Produkt ist in MeV nicht 54: Abstand rund 7000 sigma", (54-P)/(P*2.2e-8) > 7000)
check("in der Energieeinheit gelesen: 84 ppm", abs(((pred/ainv)**0.5-1)*1e6 - 84.2) < 0.1)
xs = [xi]
for _ in range(2): xs.append(xs[-1]*(1-100*xs[-1]))
check("Nichtschließung vorwärts: Schritt 1 gibt n = 98,67 (falsche Richtung)", abs(100*xs[1]/xi - 98.667) < 0.001)
check("stetige Spirale vorwärts ln(76/75) = multiplikative Form (n = 99,34)", abs(math.log(76/75)/xi - nof(K_mult)) < 0.01)
check("ein Schritt zurück (K = 73/74): n = 101,35, überschießt um 0,11 xi", abs(nof(73/74)-101.351) < 0.001 and abs(nof(73/74)-nof(K_a)-0.105) < 0.01)

print("\n3. Algebraische Folgen und angepasste Größen")
r = {"e": 4/3, "mu": 16/5, "tau": 25/9}
p = {"e": 1.5, "mu": 1.0, "tau": 2/3}
mexp = {"e": me, "mu": mmu, "tau": mtau_alt}
chain = {l: (r[l]/(5*math.pi)*xi**(p[l]+4)*EP/mexp[l]-1)*100 for l in r}
check("Kette m_i = r_i xi^(p_i+4) E_P/(5 pi): e -1,32 %, mu -0,80 %, tau +0,23 % (Dok. 383)",
      abs(chain['e']+1.318) < 0.01 and abs(chain['mu']+0.803) < 0.01 and abs(chain['tau']-0.226) < 0.01,
      ", ".join(f"{l} {v:+.3f} %" for l, v in chain.items()))
EPa = me/(4/(15*math.pi)*xi**5.5)
Ga = hbar*c**5/(EPa*MeV)**2
check("G-Rest aus Anker m_e ist algebraisch das Doppelte des E_P-Restes (G ~ E_P^-2)",
      abs(Ga/G_codata - (EP/EPa)**2) < 1e-12, f"E_P {(EPa/EP-1)*100:+.2f} %, G {(Ga/G_codata-1)*100:+.2f} %")
check("Elektronrest der Kette -1,32 % entspricht -99 xi (Nähe zu 100 xi hängt am angepassten Faktor 10)",
      abs(chain['e']/100/xi + 98.9) < 0.3, f"{chain['e']/100/xi:.1f} xi")
C_chain = Ga/(xi**2/(4*me)*0.986)
check("C_conv aus der Kette 7,58e-3 gegen Korpuswert 7,783e-3: Unterschied 2,6 % (angepasst, R141)",
      abs(C_chain-7.58e-3) < 0.01e-3 and abs(7.783e-3/C_chain-1-0.0268) < 0.002, f"{C_chain:.4e}")
check("G-Formel: 0,986 statt 74/75 macht 0,068 %", abs((K_rule/0.986-1)*100 - 0.068) < 0.001, f"{(K_rule/0.986-1)*100:.3f} %")

print("\n4. Andere Größen unter demselben Namen")
check("144/125 = r_mu/r_tau exakt (Leiterkoeffizient, R140)", abs(r['mu']/r['tau'] - 144/125) < 1e-15)
check("144/125 liegt auf der anderen Seite von 1: n = -1140", abs(nof(144/125)+1140) < 1e-6)
check("e^(-xi) (Dok. 037): n = 1, ein xi-Schritt, nicht der 100er-Schritt", abs(nof(math.exp(-xi))-1) < 0.001)

print("\n5. Leptonreste: Abstand der Leiter zur Koide-Form")
lad1, lad2 = 12/5*xi**-0.5, 125/144*xi**(-1/3)
check("Leiter m_mu/m_e = (r_mu/r_e) xi^(-1/2) = 12/5 xi^(-1/2)", abs(lad1 - r['mu']/r['e']*xi**-0.5) < 1e-9, f"{lad1:.4f}")
R1 = (lad1/(mmu/me)-1)/xi
R2 = (lad2/(mtau/mmu)-1)/xi; s2 = dmtau/mtau/xi
R2alt = (lad2/(mtau_alt/mmu)-1)/xi
check("Rest Leiter gegen Messung m_mu/m_e: +39,10 xi", abs(R1-39.10) < 0.01, f"{R1:.3f}")
check("Rest Leiter gegen Messung m_tau/m_mu: +77,56 +- 0,38 xi (PDG 2026)", abs(R2-77.56) < 0.02, f"{R2:.2f} +- {s2:.2f}")
check("mit dem bisherigen Korpuswert m_tau = 1776,86: +77,86 xi", abs(R2alt-77.86) < 0.02)
th = 2/9
sq = sorted((1+math.sqrt(2)*math.cos(th+2*math.pi*k/3))**2 for k in range(3))
k1, k2 = sq[1]/sq[0], sq[2]/sq[1]
kp1, kp2 = (k1/(mmu/me)-1)/xi, (k2/(mtau/mmu)-1)/xi
check("Koide (theta = 2/9, d/c = sqrt 2) gegen Messung: m_mu/m_e 0,07 xi", abs(kp1-0.07) < 0.01, f"{kp1:.3f}")
check("Koide gegen Messung: m_tau/m_mu 0,16 +- 0,38 xi (innerhalb der Messunsicherheit)", abs(kp2) < s2, f"{kp2:.3f}")
L1, L2 = (lad1/k1-1)/xi, (lad2/k2-1)/xi
check("Leiter gegen Koide (ohne Messwert): 39,02 xi und 77,40 xi", abs(L1-39.02) < 0.01 and abs(L2-77.40) < 0.01, f"{L1:.3f}, {L2:.3f}")
check("Leptonreste = Leiter gegen Koide bis auf 0,2 xi", abs(R1-L1) < 0.2 and abs(R2-L2) < 0.2)
q = L2/L1
check("Verhältnis der Reste 1,984, nicht 2 (rein mathematisch, Abstand 0,8 %)", abs(q-1.9836) < 0.0005 and abs(q-2) > 0.01, f"{q:.4f}")
check("gemessenes Verhältnis 1,984 +- 0,010 stimmt mit dem Koide-Wert überein", abs(R2/R1 - q) < s2/R1, f"{R2/R1:.4f} +- {s2/R1:.4f}")
d1 = ((1+chain['mu']/100)/(1+chain['e']/100)-1)/xi
d2 = ((1+chain['tau']/100)/(1+chain['mu']/100)-1)/xi
check("Verhältnisse der Kettenreste = Leiterreste (E_P und 5 pi kürzen sich)",
      abs(d1-R1) < 1e-6 and abs(d2-R2alt) < 1e-6, f"{d1:.2f}, {d2:.2f} xi")

print("\n6. Die 54-Welt: m_e m_mu = 54 E_u^2")
me_u = math.sqrt(54/k1); mmu_u = k1*me_u; mtau_u = k2*mmu_u
check("Massen in E_u (Koide): 0,511038 / 105,6674 / 1777,12", abs(me_u-0.511038) < 2e-6 and abs(mmu_u-105.6674) < 1e-3 and abs(mtau_u-1777.12) < 0.01,
      f"{me_u:.6f}, {mmu_u:.4f}, {mtau_u:.3f}")
ue, um, ut = me/me_u, mmu/mmu_u, mtau/mtau_u
check("alle drei Leptonen ergeben E_u = 0,99992 MeV auf etwa 1e-5", max(ue, um, ut) - min(ue, um, ut) < 4e-5 and abs(ue-0.99992) < 1e-5,
      f"{ue:.6f}, {um:.6f}, {ut:.6f}")
K54 = 54*xi*ainv
check("alpha^-1 = K/(54 xi) verlangt K = 0,986659, n = 100,06", abs(K54-0.986659) < 1e-6 and abs(nof(K54)-100.056) < 0.002, f"n = {nof(K54):.3f}")
check("additive Form 0,06 xi daneben, multiplikative 0,71 xi", abs(nof(K54)-100) < 0.06 and abs(nof(K54)-nof(K_mult) - 0.713) < 0.005)
check("Regel und 54 zugleich: 3700/27, 7,6 ppm daneben (beide exakt ausgeschlossen)", abs(((74/75)/(54*xi)/ainv-1)*1e6 - 7.6) < 0.1)
check("54 exakt: K = 9 alpha^-1/1250 = 0,986659194", abs(9*ainv/1250 - 0.986659194) < 1e-9 and abs(9*ainv/1250 - K54) < 1e-15)
check("Abstand zu 74/75: 7,6 ppm, Rest 0,056 xi", abs((K54/K_rule-1)*1e6 + 7.57) < 0.01 and abs((K_rule-K54)/xi - 0.056) < 0.001)
check("zweite Ordnung (100 xi)^2 = 1,33 xi, 24-mal größer als der Rest", abs(eps**2/xi - 4/3) < 1e-9 and (eps**2/xi)/((K_rule-K54)/xi) > 23)
check("1/18 verfehlt n um rund 430 sigma (nicht übernommen)", abs((nof(K54)-100-1/18)/(54*xi*0.000000021/xi) - 431) < 2)
check("74/75 exakt verlangt Produkt 54,0004 E_u^2", abs(54*(K_rule/K54) - 54.00041) < 1e-5)
d54 = 1-K54
check("offene Bahn: rho = 1/d = 74,958, 0,042 Schritte nach innen", abs(1/d54-74.958) < 0.001 and abs(75-1/d54-0.042) < 0.001, f"{1/d54:.4f}")
check("nach 75 Umläufen Vorlauf 0,00056 Umläufe = 0,20 Grad, Zusatzdrehung nach rund 1800 Zyklen",
      abs((75*d54-1)*360-0.2018) < 0.001 and abs(1/(75*d54-1)-1784) < 2)
xr = [xi]
for _ in range(80): xr.append(xr[-1]*(1-100*xr[-1]))
check("nach außen: 75 laufende Schritte ergeben nur 0,69 Umläufe (Bahn bleibt zurück)", abs(sum(100*v for v in xr[:75]) - 0.694) < 0.001)
check("ein ganzer Schritt nach innen (rho = 74): Defekt +1,35 %, das 24-Fache des Restes", abs(((1/74)/eps-1)*100 - 1.351) < 0.001 and abs((1/74-eps)/(d54-eps) - 24.1) < 0.2)
check("Rest = 3,15 d^3; Faktor pi verfehlt um rund 170 sigma", abs((d54-eps)/eps**3 - 3.152) < 0.002 and abs((d54-eps-math.pi*eps**3)/(54*xi*0.000000021) - 170) < 5)
check("54 in MeV: 7385 sigma; 54 und 74/75 zugleich: rund 49 000 sigma in alpha",
      abs((54-P)/(P*math.hypot(0.00000000016/me, 0.0000023/mmu)) - 7385) < 5 and abs(((74/75)/(54*xi)/ainv-1)/(0.000000021/ainv) - 49400) < 100)
EPc = me_u/(4/(15*math.pi)*xi**5.5)*ue
check("E_P und G aus der Kette unverändert: +1,34 % und -2,62 %", abs((EPc/EP-1)*100 - 1.335) < 0.01 and abs(((EP/EPc)**2-1)*100 + 2.62) < 0.02)

print("\n" + "="*70)
print(f"ERGEBNIS: {ok}/{n} Prüfungen bestanden")
assert ok == n
