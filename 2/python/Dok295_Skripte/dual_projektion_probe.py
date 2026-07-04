"""Dok 295 -- Duale Projektion: Zeit <-> Masse ueber T~ . m = 1.
numpy-only. Deterministisch.

Frage: Wenn die Zeit kontinuierlich gesetzt wird, traegt die Masse/Raum-Seite
die Nichtschliessung. Wandert/spiegelt der Faktor 100?

Aufbau:
  Rekursion xi_{n+1}=xi_n(1-100 xi_n),  xi_0=1/7500.
  Zeit-Seite:  Gatter-Faktor K = 1-100 xi_n,   Defekt je Schritt  d_time = 100 xi_n.
  Masse-Seite (dual, T~.m=1):  Faktor 1/K,      Defekt je Schritt  d_mass = 1/(1-100 xi_n) - 1.
Prueft:
  (1) d_mass/d_time -> 1        (gleicher Faktor 100, gespiegelt: K <-> 1/K)
  (2) beide kumulierten Defekte ~ ln(1+k/75)   (beide log-Spirale)
  (3) beide Spiralen: Verhaeltnis -> e          (projektionsinvariant)
  (4) D_mass - D_time -> beschraenkte Konstante  (Asymmetrie nur hoehere Ordnung)
"""
import numpy as np

xi0 = 1.0/7500.0
N = 200000
xi = np.empty(N+1); xi[0] = xi0
for n in range(N):
    xi[n+1] = xi[n]*(1 - 100*xi[n])
n = np.arange(N+1)

d_time = 100*xi
d_mass = 1.0/(1.0 - 100*xi) - 1.0
D_time = np.cumsum(d_time)
D_mass = np.cumsum(d_mass)

print("(1) d_mass/d_time -> 1  (Faktor 100 gespiegelt, nicht veraendert)")
for k in [1,100,10000,200000]:
    print(f"    n={k:>7}: d_mass/d_time = {d_mass[k]/d_time[k]:.6f}   d_time=100*xi={d_time[k]:.3e}")

print("\n(2) kumulierte Defekte vs ln(1+k/75)")
for k in [100,10000,200000]:
    print(f"    k={k:>7}: D_time={D_time[k]:.5f}  D_mass={D_mass[k]:.5f}  ln={np.log(1+k/75):.5f}")

def spiral(D):
    kk=n[1:]; rho=kk+75.0; beta=2*np.pi*D[1:]
    A=np.vstack([beta,np.ones_like(beta)]).T
    (a,b),*_=np.linalg.lstsq(A,np.log(rho),rcond=None)
    return a, np.exp(2*np.pi*a)

aT,eT = spiral(D_time); aM,eM = spiral(D_mass)
print("\n(3) Spiral-Fit  (rho=k+75):  Verhaeltnis e^(2pi a)")
print(f"    Zeit-Projektion : a={aT:.5f}  e^(2pi a)={eT:.5f}")
print(f"    Masse/Raum-Proj.: a={aM:.5f}  e^(2pi a)={eM:.5f}   (e={np.e:.5f})")

diff = D_mass - D_time
# analytisch: sum (100 xi)^2/(1-100 xi), konvergiert
print("\n(4) Asymmetrie D_mass - D_time (nur hoehere Ordnung, beschraenkt)")
for k in [100,10000,200000]:
    print(f"    k={k:>7}: diff={diff[k]:.6f}")
print(f"    -> konvergiert gegen beschraenkte Konstante ~{diff[-1]:.5f}, waechst NICHT mit ln k")

# Kontrollcheck: waechst diff wirklich nicht log? Vergleich diff[200000]-diff[10000]
print(f"    Zuwachs diff von k=1e4 auf 2e5: {diff[200000]-diff[10000]:.6f}  (ln-Zuwachs waere ~{np.log(200000/10000):.3f})")
