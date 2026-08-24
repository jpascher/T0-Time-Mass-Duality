#!/usr/bin/env python3
# Dok. 328 — Prüfskript 1: Wörterbuch Zweikreis <-> 2x2-Mischung (Ziel R-neu-b, [B])
# Symbolischer Nachweis (sympy), dass beide Formalismen identische Eigenstruktur haben.
import sympy as sp

print("=" * 70)
print("PRÜFSKRIPT 1: Zweikreis <-> 2x2-Mischung — symbolische Identität")
print("=" * 70)

# --- Seite A: 2x2-Mischungsmatrix (reell-symmetrisch) ---
H11, H22, H12, th = sp.symbols('H11 H22 H12 theta', real=True)
H = sp.Matrix([[H11, H12], [H12, H22]])
ev = sorted(H.eigenvals().keys(), key=sp.default_sort_key)

# Eigenwerte
S = (H11 + H22) / 2
D = (H11 - H22) / 2
lam_erw = [S - sp.sqrt(D**2 + H12**2), S + sp.sqrt(D**2 + H12**2)]
ok_ev = all(sp.simplify(a - b) == 0 for a, b in zip(ev, lam_erw)) or \
        all(sp.simplify(a - b) == 0 for a, b in zip(ev, lam_erw[::-1]))
print("\n[A1] Eigenwerte lambda± = (H11+H22)/2 ± sqrt(((H11-H22)/2)^2 + H12^2):",
      "BESTÄTIGT" if ok_ev else "FEHLER")

# Aufspaltung
dlam = sp.simplify(lam_erw[1] - lam_erw[0])
print("[A2] Aufspaltung Δλ = 2·sqrt(D^2 + H12^2) =", dlam)

# Mischungswinkel: Rotation R(theta) diagonalisiert H  <=>  tan(2θ)=2H12/(H11-H22)
R = sp.Matrix([[sp.cos(th), sp.sin(th)], [-sp.sin(th), sp.cos(th)]])
Hd = sp.simplify(R * H * R.T)
offdiag = sp.expand_trig(sp.simplify(Hd[0, 1]))
# Bedingung Nebendiagonale = 0:
cond = sp.simplify(offdiag - (H12 * sp.cos(2 * th) - (H11 - H22) / 2 * sp.sin(2 * th)))
print("[A3] Nebendiagonale nach Rotation = H12·cos2θ − ((H11−H22)/2)·sin2θ:",
      "BESTÄTIGT" if cond == 0 else "FEHLER")
print("     => Diagonalisierung genau bei tan(2θ) = 2·H12/(H11−H22)")

# --- Seite B: zwei gekoppelte Schwingkreise (verlustfrei, reaktiv gekoppelt) ---
# Bewegungsgleichungen: x1'' + w1^2 x1 + g x2 = 0 ; x2'' + w2^2 x2 + g x1 = 0
# Ansatz e^{iωt} => Eigenwertproblem für ω^2 mit Matrix M:
w1, w2, g = sp.symbols('omega1 omega2 g', positive=True)
M = sp.Matrix([[w1**2, g], [g, w2**2]])
evM = sorted(M.eigenvals().keys(), key=sp.default_sort_key)
SM = (w1**2 + w2**2) / 2
DM = (w1**2 - w2**2) / 2
evM_erw = [SM - sp.sqrt(DM**2 + g**2), SM + sp.sqrt(DM**2 + g**2)]
okM = all(sp.simplify(a - b) == 0 for a, b in zip(evM, evM_erw)) or \
      all(sp.simplify(a - b) == 0 for a, b in zip(evM, evM_erw[::-1]))
print("\n[B1] Zweikreis-Eigenfrequenzen ω±² = (ω1²+ω2²)/2 ± sqrt(((ω1²−ω2²)/2)² + g²):",
      "BESTÄTIGT" if okM else "FEHLER")

print("\n[B2] WÖRTERBUCH (strukturidentisch, Substitution H11→ω1², H22→ω2², H12→g):")
print("     Verstimmung        H11−H22   <->  ω1²−ω2²")
print("     Kopplung           H12       <->  g  (= k·ω0² beim Bandfilter)")
print("     Eigenwert-Abstand  Δλ        <->  ω+² − ω−²  (Höckerabstand)")
print("     Mischungswinkel    tan2θ = 2H12/(H11−H22)  <->  tan2θ = 2g/(ω1²−ω2²)")

# --- Entartungsfall: maximale Mischung ---
H12p = sp.symbols('H12p', positive=True)
theta_ent = sp.limit(sp.atan(2 * H12p / (H11 - H22)) / 2, H11, H22, '+')
print("\n[A4] Entartungsgrenze H11→H22: θ →", theta_ent, "(= 45°, maximale Mischung)")
print("     Zweikreis-Entsprechung: ω1=ω2 => symmetrische Aufspaltung, 50/50-Hybride")

print("\nFAZIT: Wörterbuch algebraisch bewiesen. Status R-neu-b: [S] -> [B].")
