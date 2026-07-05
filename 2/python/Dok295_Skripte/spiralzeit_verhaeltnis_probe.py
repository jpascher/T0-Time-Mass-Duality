"""Dok 295 -- Abgleich: traegt HLVs Spiral-Zeit das Verhaeltnis e?
numpy-only. Deterministisch.

Aequiangular-Kriterium (notwendig und hinreichend):
    Eine Windung ist eine log-Spirale mit Verhaeltnis e (je 2pi) genau dann,
    wenn der Defekt je Schritt wie 1/n zerfaellt, D(k)=sum d_n ~ ln(k).
    Konstanter Defekt  -> D(k) linear -> Archimedisch, Verhaeltnis -> 1.

Geprueft werden drei Konstruktionen auf ihren jeweils EIGENEN Definitionen:
  (A) FFGFT:  d_n = 100 xi_n aus xi_{n+1}=xi_n(1-100 xi_n)      -> 1/n-Zerfall -> e   (Orakel)
  (B) Marcel Spiral-Time:  phi_i = q_phi * u_i (linear), chi beschraenkt
        -> konstanter Defekt -> KEIN 1/n-Zerfall -> Verhaeltnis -> 1 (nicht aequiangular)
  (C) phi-Geometrie (tau=phi Cut-and-Project): falls aequiangular gebaut,
        ist der natuerliche Selbstaehnlichkeits-Faktor phi-basiert, NICHT e.
Ergebnis: das e-Kriterium trennt; Marcel (B) ist gar nicht aequiangular,
und die Geometrie, die HLV traegt (C), zeigt phi, nicht e.
"""
import numpy as np

def ratio_from_defect(d, n0):
    """Kumulierter Defekt D=sum d, Radius rho=k+n0, beta=2pi D.
    Fit ln rho = a beta + b; Selbstaehnlichkeit je 2pi = exp(2pi a)."""
    D = np.cumsum(d)
    k = np.arange(1, len(d)+1)
    rho = k + n0
    beta = 2*np.pi*D
    A = np.vstack([beta, np.ones_like(beta)]).T
    (a, b), *_ = np.linalg.lstsq(A, np.log(rho), rcond=None)
    return np.exp(2*np.pi*a), a, D

N = 200000
n = np.arange(1, N+1)

# ---------------------------------------------------------------
# (A) FFGFT: xi-Rekursion -> d_n = 100 xi_n
# ---------------------------------------------------------------
xi0 = 1.0/7500.0
xi = np.empty(N+1); xi[0] = xi0
for i in range(N):
    xi[i+1] = xi[i]*(1 - 100*xi[i])
d_ffgft = 100*xi[1:]                       # Defekt je Schritt
r_ffgft, a_ffgft, D_ffgft = ratio_from_defect(d_ffgft, 75.0)
# 1/n-Test
tail = d_ffgft[99:]*(n[99:]+75)
print("(A) FFGFT  d_n = 100 xi_n")
print(f"    d_n*(n+75) -> 1 :  n=100 {d_ffgft[99]*(100+75):.5f}   n=2e5 {d_ffgft[-1]*(N+75):.5f}")
print(f"    Verhaeltnis je 2pi = {r_ffgft:.5f}   e = {np.e:.5f}   -> traegt e  [OK]")

# ---------------------------------------------------------------
# (B) Marcel Spiral-Time:  phi(t) linear, chi beschraenkt (Fenster)
#     phi_i = q_phi * u_i  mit u_i beschraenkt  -> Defekt je Schritt konstant
#     (kein Skalenlauf in der Konstruktion; siehe Zenodo 20643462, Abschn.12)
# ---------------------------------------------------------------
q_phi = 100*xi0            # gleiche Anfangs-Ganghoehe wie FFGFT, damit Start identisch
d_marcel = np.full(N, q_phi)               # konstanter Defekt (linear phasonisch)
r_marcel, a_marcel, D_marcel = ratio_from_defect(d_marcel, 75.0)
tailm = d_marcel[99:]*(n[99:]+75)
print("\n(B) Marcel Spiral-Time  phi linear, chi beschraenkt")
print(f"    d_n*(n+75) (waechst, KEIN 1/n):  n=100 {d_marcel[99]*(100+75):.5f}   n=2e5 {d_marcel[-1]*(N+75):.2f}")
print(f"    D(k) linear statt log:  D(1e5)={D_marcel[100000]:.2f}  ln(1+k/75)={np.log(1+100000/75):.2f}")
print(f"    Verhaeltnis je 2pi = {r_marcel:.5f}   -> -> 1 (Archimedisch, nicht aequiangular)")
print(f"    -> traegt KEIN e; ist gar keine log-Spirale auf eigenen Definitionen")

# ---------------------------------------------------------------
# (C) phi-Geometrie: falls man aus tau=phi eine aequiangulare Spirale baut,
#     ist der natuerliche Faktor phi-basiert. Goldene Spirale: Faktor phi je 90 Grad,
#     also phi^4 je voller 2pi.  Kontrast zu e.
# ---------------------------------------------------------------
phi = (1+np.sqrt(5))/2
golden_per_2pi = phi**4
print("\n(C) phi-Geometrie (tau=phi Cut-and-Project)")
print(f"    goldene Spirale: Faktor phi je 90deg -> phi^4 je 2pi = {golden_per_2pi:.5f}")
print(f"    phi je 2pi (falls je Umlauf) = {phi:.5f}")
print(f"    e = {np.e:.5f}   -> phi-Konstanten != e; verschiedene Selbstaehnlichkeit")

# ---------------------------------------------------------------
# Bruecken-Bedingung (P35): was HLVs Spiral-Zeit fuer e liefern muesste
# ---------------------------------------------------------------
print("\nBruecken-Bedingung (Kandidat, nicht abgeleitet):")
print("    HLVs Spiral-Zeit traegt e nur, wenn ihr Phasengesetz einen 1/n-Skalenlauf")
print("    (laufende innere Skala) enthaelt. Die vorliegenden Definitionen (lineare")
print("    phasonische Phase, beschraenktes Fenster-Gedaechtnis) enthalten ihn nicht.")
print(f"    Trenn-Zahlen:  FFGFT {r_ffgft:.4f}  |  Marcel {r_marcel:.4f}  |  e {np.e:.4f}  |  phi {phi:.4f}")
