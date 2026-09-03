"""
pruef_343d_xi_aufloesung.py
Rolle von ξ als Auflösungsboden: Schwellen aus Satz F/G für verschiedene ε.

Auflösungsstufen (aus dem Korpus):
  ε₁ = 1,05 %      fraktale Korrektur bare→gemessen           (Dok. 338)
  ε₂ = 100·ξ       fraktale Dämpfung pro Operation, K_frak=1−100ξ (Dok. 162/034)
  ε₃ = ξ           Linienbreite der Torusmoden, g/ω = ξ       (Dok. 328)
  ε₄ = 1/Q_TFLN    photonische Resonatoren, Q > 10⁶            (Dok. 186)
  ε₅ = ξ²          nächste fraktale Ordnung
Fragen: Wo liegen Q_c, p*, Galois-k_max und Zufallsniveau je Stufe?
"""
import math, random, itertools, bisect
from sympy import factorint, primerange
xi = 4/30000
levels = [("1,05 % (Dok.338)",0.0105),("100·ξ (Dok.162)",100*xi),("ξ (Dok.328)",xi),
          ("1/Q_TFLN=1e-6 (Dok.186)",1e-6),("ξ²",xi*xi)]

def ord3(p):
    k=1
    while pow(3,k,p)!=1: k+=1
    return k
def galois_vals(kmax):
    blocks=set()
    for k in range(1,kmax+1):
        N=3**k-1; blocks.add(N); blocks.add(3**k); blocks.update(factorint(N))
    blocks=sorted(b for b in blocks if b>1)
    vals=set()
    for r in range(1,4):
        for idx in itertools.combinations(range(len(blocks)),r):
            for es in itertools.product((-1,1,2),repeat=r):
                v=1.0
                for i,e in zip(idx,es): v*=blocks[i]**e
                if 10<v<1e4: vals.add(math.log(v))
    return sorted(vals)
spacing={k:(math.log(1e4)-math.log(10))/len(galois_vals(k)) for k in range(2,9)}

print("Vorbemerkung: 1,05 % / (100ξ) =", f"{0.0105/(100*xi):.2f}", "→ die Korrektur aus Dok.338 ist von der Ordnung EINER fraktalen Dämpfungsstufe 100ξ (Dok.162).")
print()
print(f"{'Auflösung ε':>26} {'ε':>9} {'Q_c=π/√6ε':>10} {'p*=ε^-1/2':>10} {'Primen ≤ p*':>12} {'k_max trennscharf':>18} {'Regime bei k=3':>15}")
for name,eps in levels:
    Qc=math.pi/math.sqrt(6*eps); ps=eps**-0.5
    primes_below=[p for p in primerange(2,int(ps)+1)]
    kmax=max([k for k,sp in spacing.items() if sp>2*eps] or [0])
    kmax_s = f"≥{kmax}" if kmax==8 else str(kmax)
    reg = "unterkritisch" if spacing[3]>2*eps else "überkritisch"
    print(f"{name:>26} {eps:>9.2e} {Qc:>10.1f} {ps:>10.1f} {len(primes_below):>12} {kmax_s:>18} {reg:>15}")

print("\nGalois-Raster: mittlerer log-Abstand je k_max (Fenster 10..10⁴):")
for k,sp in spacing.items(): print(f"  k_max={k}: {sp*100:.4f} %   (ξ = {xi*100:.4f} %)")

print("\nEintrittstiefe der bis p* unterscheidbaren Primzahlen bei ε = ξ:")
for p in primerange(5,90):
    print(f"  p={p:2d} k=ord_p(3)={ord3(p):2d}", end="")
print()

print("""
Lesart [B]:
  • Bei ε = 1,05 % (unkorrigierte fraktale Stufe) endet die Galois-Schicht bei k≈3–4 (Satz F).
  • Bei ε = ξ (Linienbreite der Torusmoden) bleibt der Galois-Raster bis k≥8 trennscharf;
    p* ≈ 87: alle Primzahlen bis 83 hätten unterscheidbare Euler-Faktoren.
  • Bei ε = 1/Q der TFLN-Resonatoren (Dok.186) liegt die Auflösung sogar UNTER ξ:
    photonische Hardware könnte den ξ-Boden selbst auflösen.
Folgerung [S]: Die Grenze k≈3–4 ist die Grenze der ersten fraktalen Stufe (100ξ ≈ 1 %).
  Wird diese Stufe analytisch abgezogen (sie ist berechenbar, Dok.338/162), rückt die
  Trennschärfe auf ξ, und die exakte Galois-Schicht reicht bis k≥8. ξ spielt dann die
  Rolle des Auflösungsbodens — nicht des Auswahlkriteriums.
Vorbehalt [S]: Dok.034 stellt fest, dass ξ-Korrekturen (~10⁻⁵) unter dem NISQ-Rauschen
  liegen und mit heutiger Hardware nicht prüfbar sind; Dok.186 gibt Q>10⁶ nur für die
  optische Phase, nicht für Massenverhältnisse. Die Übertragung von 1/Q auf ε ist Analogie.
""")
