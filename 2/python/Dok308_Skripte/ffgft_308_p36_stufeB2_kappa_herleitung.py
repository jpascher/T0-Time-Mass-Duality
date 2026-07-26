#!/usr/bin/env python3
# ffgft_308_p36_stufeB2_kappa_herleitung.py  —  Dok. 307, P36 Stufe B (2/2)
# ---------------------------------------------------------------------------
# Auswahlrechnung: welche T^4-Invarianzregel liefert kappa_Raum = 1?
# Vier Kandidaten fuer die raeumliche Mesh-Regel (Kantenmass l(r)).
# ---------------------------------------------------------------------------
# Status: [K] Kernableitung
# Messlatte: alpha = 1.750'' (Sonnenrand), Cassini |gamma-1| < 2.3e-5.
# ---------------------------------------------------------------------------

#
# Ausgangslage: m(r) = m0*(1 + Phi/c^2) = m0*(1 - GM/(r c^2))
#   (duale Lesart der gemessenen Gravitations-Zeitdilatation,
#    Pound-Rebka-verankert; Masse sinkt im Potentialtopf).
# Takt:  T~ = 1/m  ->  n_Zeit = m0/m = 1 + GM/(r c^2)  [kappa_t = 1]
#
# Vier Kandidaten fuer die raeumliche Mesh-Regel (Kantenmass l(r)):
#   K1 KONFORM:      l = lambda_C = hbar/(m c)  (gleiche Quelle wie Takt)
#                    -> n_Raum = m/m0, n_tot = 1: LICHT UNABGELENKT
#   K2 UNIMODULAR:   4-Volumen invariant, L_t*l^3 = const
#                    -> l ~ m^{1/3}, kappa_s = 1/3, gamma = 1/3
#   K3 FLAECHE:      Zeit-Raum-2-Zelle invariant, L_t*l = const
#                    (Dualitaetsform T~*x = const auf das
#                     Zeit-Raum-Paar angewandt; "c = Raum-Zeit-Bruecke")
#                    -> l ~ m, kappa_s = 1, gamma = 1
#   K0 REFERENZ:     nur Takt (kappa_s = 0), das 1911-Halbresultat
#
# FE-Ray-Tracing wie in P36_StufeB_Faktor2_FE.py.
# Messlatten: alpha = 1.750'' (Sonnenrand), Cassini |gamma-1|<2.3e-5.
# ============================================================
import numpy as np

G, c = 6.67430e-11, 2.99792458e8
Msun, Rsun = 1.98892e30, 6.9634e8
eps = G*Msun/(Rsun*c**2)
AS = 206264.806

Nn = 30001
r_nodes = np.exp(np.linspace(np.log(0.95), np.log(6000.0), Nn))

def n_of_rule(kappa_t, kappa_s):
    """n_tot = n_Zeit * n_Raum, erste Ordnung: 1 + (kt+ks)*eps/r."""
    return (1.0 + kappa_t*eps/r_nodes) * (1.0 + kappa_s*eps/r_nodes)

def n_and_grad(x, y, n_nodes):
    r = np.hypot(x, y)
    i = min(max(np.searchsorted(r_nodes, r) - 1, 0), Nn-2)
    r0, r1 = r_nodes[i], r_nodes[i+1]
    n0, n1 = n_nodes[i], n_nodes[i+1]
    w = (r - r0)/(r1 - r0)
    dn = (n1 - n0)/(r1 - r0)
    return n0 + w*(n1 - n0), dn*x/r, dn*y/r

def trace(n_nodes, b=1.0, X=3000.0, want_path=False):
    x, y, tx, ty = -X, b, 1.0, 0.0
    extra = 0.0
    while x < X:
        r = np.hypot(x, y)
        ds = 0.02*max(1.0, r/10.0)
        def deriv(x, y, tx, ty):
            n, gx, gy = n_and_grad(x, y, n_nodes)
            tg = tx*gx + ty*gy
            return tx, ty, (gx - tg*tx)/n, (gy - tg*ty)/n
        k1 = deriv(x, y, tx, ty)
        k2 = deriv(x+0.5*ds*k1[0], y+0.5*ds*k1[1], tx+0.5*ds*k1[2], ty+0.5*ds*k1[3])
        k3 = deriv(x+0.5*ds*k2[0], y+0.5*ds*k2[1], tx+0.5*ds*k2[2], ty+0.5*ds*k2[3])
        k4 = deriv(x+ds*k3[0], y+ds*k3[1], tx+ds*k3[2], ty+ds*k3[3])
        if want_path:
            nmid,_,_ = n_and_grad(x, y, n_nodes)
            extra += (nmid-1.0)*ds
        x  += ds*(k1[0]+2*k2[0]+2*k3[0]+k4[0])/6
        y  += ds*(k1[1]+2*k2[1]+2*k3[1]+k4[1])/6
        tx += ds*(k1[2]+2*k2[2]+2*k3[2]+k4[2])/6
        ty += ds*(k1[3]+2*k2[3]+2*k3[3]+k4[3])/6
        nrm = np.hypot(tx, ty); tx, ty = tx/nrm, ty/nrm
    a = abs(np.arctan2(ty, tx))
    return (a, extra) if want_path else a

print("="*68)
print(" AUSWAHLRECHNUNG: vier Regeln, eine Messlatte (1.750'')")
print("="*68)
rules = [("K1 KONFORM  (l=lambda_C, gleiche Quelle)", 1.0, -1.0),
         ("K2 UNIMODULAR (4-Volumen invariant)",      1.0,  1/3),
         ("K3 FLAECHE  (Zeit-Raum-2-Zelle invariant)",1.0,  1.0),
         ("K0 nur Takt (Referenz 1911)",              1.0,  0.0)]
for label, kt, ks in rules:
    a = trace(n_of_rule(kt, ks))
    gamma = ks/kt
    verdict = ("BESTANDEN" if abs(a*AS-1.75)<0.01 else "ausgeschlossen")
    print(f"{label:44s} gamma={gamma:+.4f}  alpha={a*AS:.4f}''  {verdict}")

print(f"\nCassini: |gamma-1| < 2.3e-5")
print(f"  K1: |(-1)-1| = 2         -> ausgeschlossen (Faktor ~1e5 ueber Schranke)")
print(f"  K2: |1/3-1|  = 0.667     -> ausgeschlossen (Faktor ~3e4 ueber Schranke)")
print(f"  K3: |1-1|    = 0 exakt   -> besteht mit unendlichem Spielraum")

# Shapiro-Konsistenz fuer K3
print("\nShapiro-Konsistenz (K3), b = 1 R_sun, X = 3000 R_sun:")
a, extra = trace(n_of_rule(1.0, 1.0), want_path=True)
X, b = 3000.0, 1.0
analytic = 2*2*eps*np.arcsinh(X/b)   # int (2 eps/r) ds, Gerade
print(f"  numerisch:  Delta_Weg = {extra:.6e} R_sun = {extra*Rsun:.1f} m")
print(f"  analytisch: {analytic:.6e} R_sun = {analytic*Rsun:.1f} m  "
      f"(rel. Abw. {abs(extra-analytic)/analytic:.2e})")
print(f"  Laufzeit: {extra*Rsun/c*1e6:.1f} mikros (Groessenordnung Shapiro ~ 100 mikros ok)")

print("""
BEFUND:
  Der naive Weg (Kante = Kohaerenzlaenge desselben Knotens) ist die
  KONFORME FALLE: Takt und Massstab skalieren gleich, Licht sieht
  nichts, alpha = 0. Haerter ausgeschlossen als das Halbresultat.
  Von den T^4-Invarianzregeln besteht genau eine: die
  Flaechen-Invarianz der Zeit-Raum-2-Zelle, L_t * l = const --
  formal dieselbe Reziprozitaetsform wie T~*m = 1, angewandt auf
  das Zeit-Raum-Paar. gamma = 1 folgt dann EXAKT, nicht gefittet.
""")
