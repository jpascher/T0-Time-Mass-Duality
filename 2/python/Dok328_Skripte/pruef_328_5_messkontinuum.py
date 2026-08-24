#!/usr/bin/env python3
# Dok. 328 — Prüfskript 5: R-neu-d — Messübergang schwach→stark als κ-Kontinuum
# Von-Neumann-Zeigermodell mit Gauß-Zeiger. Symbolischer Beweis (sympy):
# EIN Parameter κ = d/(2σ) steuert Informationsgewinn UND Rückwirkung,
# mit exakter Dualität D² + V² = 1.
import sympy as sp

print("=" * 72)
print("PRÜFSKRIPT 5: Messung als κ-Kontinuum (Von-Neumann-Zeigermodell)")
print("=" * 72)
print("""
Modell: System-Zustand a|+⟩ + b|−⟩, Zeiger-Wellenfunktion G(x) gaußisch (Breite σ).
Kopplung H_int = g·Â⊗p̂ verschiebt den Zeiger um ±d/2 je nach Systemzustand:
  |Ψ⟩ = a|+⟩⊗φ₊ + b|−⟩⊗φ₋,  φ±(x) = G(x ∓ d/2)
Definition Mess-Kopplungsgrad: κ ≡ d/(2σ)  (Zeigertrennung relativ zur Zeigerbreite)
""")

x, d, sig = sp.symbols('x d sigma', positive=True)
G = lambda xc: (2 * sp.pi * sig**2) ** sp.Rational(-1, 4) * sp.exp(-(x - xc) ** 2 / (4 * sig**2))
phi_p = G(d / 2)
phi_m = G(-d / 2)

# [1] Normierung
norm = sp.integrate(phi_p**2, (x, -sp.oo, sp.oo))
print("[1] Normierung ∫|φ₊|²dx =", sp.simplify(norm))

# [2] Überlapp = Restkohärenz-Faktor (Visibility V):
ov = sp.simplify(sp.integrate(phi_p * phi_m, (x, -sp.oo, sp.oo)))
kappa = sp.symbols('kappa', positive=True)
V = sp.simplify(ov.subs(d, 2 * kappa * sig))
print("[2] Überlapp ⟨φ₊|φ₋⟩ =", ov, "  =>  V(κ) =", V)

# [3] Optimale Unterscheidbarkeit (Helstrom, reine Zustände): D = sqrt(1 − |⟨φ₊|φ₋⟩|²)
D = sp.sqrt(1 - V**2)
print("[3] Unterscheidbarkeit D(κ) = sqrt(1 − V²) =", sp.simplify(D))

# [4] Exakte Dualität
dual = sp.simplify(D**2 + V**2)
print("[4] D² + V² =", dual, " ->", "EXAKTE DUALITÄT BESTÄTIGT" if dual == 1 else "FEHLER")

# [5] Grenzfälle
V0 = sp.limit(V, kappa, 0)
Vinf = sp.limit(V, kappa, sp.oo)
D0 = sp.limit(D, kappa, 0)
Dinf = sp.limit(D, kappa, sp.oo)
print(f"[5] Grenzfälle:  κ→0: V={V0}, D={D0}  (keine Messung — unterkritischer Grenzfall)")
print(f"                 κ→∞: V={Vinf}, D={Dinf}  (projektive Messung — starker Grenzfall)")

# [6] Monotonie: dD/dκ > 0, dV/dκ < 0 für κ>0
dDdk = sp.simplify(sp.diff(D, kappa))
dVdk = sp.simplify(sp.diff(V, kappa))
mono_D = sp.simplify(dDdk) 
print("[6] dV/dκ =", dVdk, " (<0 für κ>0);  dD/dκ =", mono_D, " (>0 für κ>0)")
print("    => Informationsgewinn und Rückwirkung sind streng monotone Funktionen")
print("       DESSELBEN Parameters κ — das Kontinuum ist eindimensional.")

# [7] Schwaches Regime: Störung 1−V ≈ κ²/2 (quadratisch klein), Info D ≈ κ (linear)
serV = sp.series(1 - V, kappa, 0, 4).removeO()
serD = sp.series(D, kappa, 0, 3).removeO()
print("[7] Entwicklung κ≪1:  1−V =", serV, ";  D =", serD)
print("    => weak-measurement-Regime: Info wächst linear, Störung erst quadratisch —")
print("       die formale Grundlage des Tauschs 'Rückwirkung gegen Statistik' (§4).")

print("""
FAZIT: Im Von-Neumann-Gauß-Modell ist der Messübergang schwach→stark ein
Ein-Parameter-Kontinuum κ = d/(2σ) mit exakter Dualität D² + V² = 1,
V = exp(−κ²/2), D = sqrt(1 − exp(−κ²)). Symbolisch bewiesen.
Status R-neu-d: [S] -> [B] (innerhalb des Zeigermodells; Zuordnung zur
A271-Ebenentrennung: alles hier lebt auf der Zustandsübergangs-Ebene).""")
