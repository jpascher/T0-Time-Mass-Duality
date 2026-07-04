"""Dok 295 -- Zeit-Windung als logarithmische Spirale (laufendes xi).
numpy-only. Deterministisch.

Rekursion xi_{n+1} = xi_n (1 - 100 xi_n),  xi_0 = 1/7500.
Zeigt:
  (1) xi_n ~ 1/(100(n+75))            algebraischer 1/n-Zerfall
  (2) D(k)=sum 100 xi_n ~ ln(1+k/75)  kumulierter Defekt logarithmisch
  (3) mit rho = k+75, beta = 2pi D:   log-Spirale rho = 75 e^{beta/2pi}
      Fit-Steigung a -> 1/(2pi),  e^{2pi a} -> e
  (4) lokales Selbstaehnlichkeits-Verhaeltnis je Praezessionsrunde -> e
  (5) kontinuierliche (nicht diskret log-periodische) Skaleninvarianz
Das Verhaeltnis e ist NICHT angesetzt; es folgt aus dem 1/n-Zerfall
(harmonische Summe -> natuerlicher Logarithmus -> Basis e).
"""
import numpy as np

xi0 = 1.0/7500.0
N = 200000
xi = np.empty(N+1); xi[0] = xi0
for n in range(N):
    xi[n+1] = xi[n]*(1 - 100*xi[n])
n = np.arange(N+1)

# (1) 1/n-Zerfall
approx = 1.0/(100*(n+75))
print("(1) xi_n * 100(n+75) -> 1")
for k in [1,100,10000,200000]:
    print(f"    n={k:>7}: {xi[k]*100*(k+75):.6f}")

# (2) D(k) vs ln(1+k/75)
D = np.cumsum(100*xi)
print("\n(2) D(k) vs ln(1+k/75)")
for k in [100,10000,200000]:
    print(f"    k={k:>7}: D={D[k]:.5f}  ln={np.log(1+k/75):.5f}  diff={D[k]-np.log(1+k/75):+.5f}")

# (3) Fit  rho=k+75
kk = n[1:]
rho = kk + 75.0
beta = 2*np.pi*D[1:]
A = np.vstack([beta, np.ones_like(beta)]).T
(a,b),*_ = np.linalg.lstsq(A, np.log(rho), rcond=None)
print("\n(3) Fit ln(rho)=a*beta+b   (rho=k+75)")
print(f"    a        = {a:.5f}   1/(2pi) = {1/(2*np.pi):.5f}")
print(f"    e^(2pi a)= {np.exp(2*np.pi*a):.5f}   e = {np.e:.5f}")

# (4) lokales Verhaeltnis je Praezessionsrunde (Delta D = 1)
print("\n(4) rho(D=m+1)/rho(D=m) -> e")
seq=[]
for m in range(1,8):
    k_lo = int(np.searchsorted(D, m)); k_hi = int(np.searchsorted(D, m+1))
    if k_hi < len(rho):
        r=(k_hi+75)/(k_lo+75); seq.append(r)
print("    " + " ".join(f"{r:.4f}" for r in seq) + f"   -> e={np.e:.5f}")

# (5) diskrete Skaleninvarianz?  Residuum D-ln, Amplitude/Periodizitaet
res = D[1:] - np.log(1+kk/75)
print("\n(5) kontinuierliche Skaleninvarianz")
print(f"    max|Residuum| (k>=100) = {np.max(np.abs(res[99:])):.5f}")
print(f"    std  Residuum (k>=100) = {np.std(res[99:]):.6f}   (nahe 0, keine log-Periodizitaet)")
