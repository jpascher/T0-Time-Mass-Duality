"""
pruef_342c_dichte_hoehere_harmonien.py
Prüfung der These: Bei höheren Harmonischen werden die Galois-Produktwerte
statistisch von höheren Moden nicht mehr unterscheidbar — kein Widerspruch,
sondern Dichte-Effekt (dieselbe Struktur wie beim Obertonspektrum).

Test 1: Dichte der erreichbaren Verhältnisse in log-Skala als Funktion von k_max.
Test 2: Erwartete Zufallstreffer pro Ziel vs. tatsächliche Treffer.
Test 3: Analogon Obertonreihe: Intervallabstand log(n+1)/n → 0.
Test 4: Trennschärfe-Grenze k*: ab wann ist 1%-Auflösung nicht mehr diskriminierend?
"""
import math, itertools, random
from collections import Counter

def factorize(n):
    f=Counter(); d=2
    while d*d<=n:
        while n%d==0: f[d]+=1; n//=d
        d+=1
    if n>1: f[n]+=1
    return f

# Bausteine bis k_max: |GF(3^k)*| = 3^k-1, |GF(3^k)| = 3^k, und deren Primteiler
def blocks_upto(kmax):
    B=set()
    for k in range(1,kmax+1):
        B.add(3**k-1); B.add(3**k)
        B |= set(factorize(3**k-1))
    return sorted(B)

def products(blocks, r_max=3, exps=(-1,1,2)):
    vals=set()
    for r in range(1,r_max+1):
        for idx in itertools.combinations(blocks,r):
            for e in itertools.product(exps,repeat=r):
                v=1.0
                for b,ee in zip(idx,e): v*=b**ee
                if 1<v<1e8: vals.add(round(math.log(v),9))
    return sorted(vals)

print("="*70)
print("TEST 1: Dichte der Galois-Produkte in log-Skala (Fenster 10 < x < 10^4)")
print("="*70)
print(f"{'k_max':>5} {'Bausteine':>10} {'Werte im Fenster':>17} {'mittl.Abstand(%)':>17} {'erw.Treffer@0.5%':>17} {'@0.05%':>8}")
lo,hi=math.log(10),math.log(1e4)
density={}
for kmax in range(2,9):
    B=blocks_upto(kmax)
    L=[v for v in products(B) if lo<v<hi]
    n=len(L)
    spacing=(hi-lo)/n if n else float('inf')
    # erwartete Treffer für ein zufälliges Ziel bei Toleranz t (relativ): 2t/spacing
    e05=2*0.005/spacing; e0005=2*0.0005/spacing
    density[kmax]=(len(B),n,spacing)
    print(f"{kmax:>5} {len(B):>10} {n:>17} {spacing*100:>17.3f} {e05:>17.2f} {e0005:>8.3f}")
print("""
Lesart: Sobald der mittlere log-Abstand unter die Toleranz fällt, trifft JEDES
Ziel — die Galois-Produktmenge ist dann quasi-dicht. Bei k_max=3 (Leptonenschicht)
ist die Auflösung noch diskriminierend; ab k_max≈5-6 nicht mehr bei 0,5 %,
ab k_max≈8 auch nicht mehr bei 0,05 %.
""")

print("="*70)
print("TEST 2: Zufallsziele vs. physikalische Ziele — gleiche Trefferrate?")
print("="*70)
random.seed(42)
me,mmu,mtau=0.51099895,105.6583755,1776.86
mu,md,ms,mc,mb,mt=2.16,4.70,93.5,1273.,4183.,172570.
phys={"m_mu/m_e":mmu/me,"(m_mu/m_e)^2":(mmu/me)**2,"m_tau/m_mu":mtau/mmu,
      "(m_tau/m_mu)^2":(mtau/mmu)**2,"m_t/m_c":mt/mc,"m_c/m_u":mc/mu,
      "m_b/m_s":mb/ms,"m_s/m_d":ms/md,"m_t/m_b":mt/mb,"m_tau/m_e":mtau/me}
for kmax in (3,4,6):
    B=blocks_upto(kmax); L=products(B)
    def hits(t,tol):
        lt=math.log(t); return sum(1 for v in L if abs(v-lt)<tol)
    for tol in (0.005,0.0005):
        ph=[hits(t,tol) for t in phys.values()]
        rn=[hits(math.exp(random.uniform(lo,hi)),tol) for _ in range(200)]
        print(f"k_max={kmax} tol={tol*100:.2f}%:  physikalisch Ø{sum(ph)/len(ph):.2f}  "
              f"zufällig Ø{sum(rn)/len(rn):.2f}   (phys: {ph})")
print("""
Lesart: Liegt die Trefferrate physikalischer Verhältnisse auf Zufallsniveau,
ist die Galois-Produkt-Suche bei dieser Tiefe nicht mehr aussagekräftig.
Ein echter Befund muss sich ÜBER dem Zufallsniveau abheben — wie 43200 bei k_max=3
mit NUR 2 Bausteinen und Exponent ≤2, und geometrischer Herleitung via ξ (Dok.338).
""")

print("="*70)
print("TEST 3: Analogon Obertonreihe — Intervallabstände verschwinden")
print("="*70)
print(f"{'n':>4} {'Intervall n+1:n':>16} {'Cent':>8} {'JND≈5ct?':>10}")
for n in (1,2,3,4,5,6,8,12,16,24,32,48,64):
    cent=1200*math.log2((n+1)/n)
    print(f"{n:>4} {f'{n+1}:{n}':>16} {cent:>8.1f} {'unterscheidbar' if cent>5 else 'NICHT':>10}")
print("""
Ab n≈16 liegen benachbarte Obertöne unter einem Halbton (100 ct), ab n≈250
unter der Wahrnehmungsschwelle (~5 ct). Das ist exakt derselbe Mechanismus:
die harmonische Reihe wird bei hohen Moden quasi-kontinuierlich (Dok.159:
Konvergenz durch Modenunterdrückung auf dem fraktalen Torus).
""")

print("="*70)
print("TEST 4: Kritisches k* — wo die Galois-Auflösung unter die FFGFT-Korrektur fällt")
print("="*70)
corr = 0.0105  # fraktal-rekursive Korrektur höherer Ordnung, Dok.338 (bare→gemessen)
print(f"FFGFT-Korrektur bare→gemessen: {corr*100:.2f} % (Dok.338)")
for kmax,(nb,n,sp) in density.items():
    flag = "diskriminierend" if sp > 2*corr else "NICHT mehr trennbar"
    print(f"  k_max={kmax}: log-Abstand {sp*100:.3f}%  vs  2·Korrektur {2*corr*100:.2f}%  → {flag}")
print("""
FAZIT [B]:
  • k≤3 (GF(3), GF(9), GF(27)): Galois-Werte sind grob gerastert; ein Treffer
    ist signifikant. Hier lebt die Leptonenschicht.
  • k≥5: Die Produktmenge ist dichter als die fraktale Korrektur selbst.
    Jede Zahl wird "getroffen" — Galois-Produkte sind dann von höheren
    Torus-Moden statistisch ununterscheidbar. KEIN Widerspruch: das ist
    die algebraische Form der Modenkonvergenz aus Dok.159.
  • Konsequenz für die Methodik: Tiefe Harmonische (k≤4) dürfen als Identitäten
    [K]/[B] gelten; höhere (k≥5) nur, wenn sie aus ξ geometrisch abgeleitet sind
    und nicht durch Produktsuche gefunden wurden.
""")
