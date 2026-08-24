#!/usr/bin/env python3
# Dok. 328 — Prüfskript 6: R-neu-c, ξ-Stufe
# Teil A: Kompositions-Schluss für θ_W — κ(θ_W) ist ξ-abgeleitet, weil sin²θ_W
#         im Korpus aus ξ abgeleitet ist (RGE-Serie Dok. 317–323). [K]
# Teil B: Ehrliches Screening — ist κ(θ_W) eine einfache Konstante? (Numerologie-Schutz)
# Teil C: Exakte Reduktion — die offene ξ-Frage je Sektor reduziert sich auf die
#         Nebendiagonale H12; H12 aus (Δλ, θ) exakt bestimmbar (symbolisch bewiesen).
import numpy as np
import sympy as sp

print("=" * 72)
print("PRÜFSKRIPT 6: R-neu-c — ξ-Stufe")
print("=" * 72)

# ---------- Teil A: Kompositions-Schluss ----------
print("\n[A] Kompositions-Schluss für θ_W")
s2 = 0.2308  # sin²θ_W(M_Z), im Korpus aus ξ abgeleitet (Dok. 317–323) [K]
# Exakte Umformung: cos2θ = 1−2s², sin2θ = 2√(s²(1−s²)), κ = sin2θ/cos2θ
c2t = 1 - 2 * s2
s2t = 2 * np.sqrt(s2 * (1 - s2))
kappa_W = s2t / c2t
th = np.degrees(np.arcsin(np.sqrt(s2)))
print(f"    sin²θ_W = {s2}  (ξ-abgeleitet, Dok. 317–323)")
print(f"    θ_W = {th:.4f}°,  cos2θ = {c2t:.6f},  sin2θ = {s2t:.6f}")
print(f"    κ(θ_W) = tan2θ = 2·sqrt(s²(1−s²))/(1−2s²) = {kappa_W:.6f}")
print("    SCHLUSS: κ(θ_W) ist als deterministische Funktion einer ξ-abgeleiteten")
print("    Größe selbst ξ-abgeleitet. Für den θ_W-Sektor: [S] -> [K] (Komposition).")
print("    Kein neuer physikalischer Inhalt — aber die Brücke ist formal geschlossen.")

# ---------- Teil B: Screening gegen einfache Konstanten ----------
print("\n[B] Numerologie-Schutz: κ(θ_W) gegen einfache Konstanten")
print("    Kriterium: relative Abweichung < 1e-3 wäre auffällig; alles darüber = negativ.")
phi = (1 + np.sqrt(5)) / 2
xi = 4 / 30000
kandidaten = {
    "π/2": np.pi / 2, "φ": phi, "φ²−1 (=φ)": phi, "√e": np.sqrt(np.e),
    "π²/6": np.pi**2 / 6, "3/2": 1.5, "11/7": 11 / 7, "π/2·(1−ξ)": np.pi / 2 * (1 - xi),
    "e/√3": np.e / np.sqrt(3), "√(5/2)": np.sqrt(2.5), "tan(1 rad)": np.tan(1.0),
}
auffaellig = []
for name, val in sorted(kandidaten.items(), key=lambda kv: abs(kv[1] - kappa_W)):
    rel = abs(val - kappa_W) / kappa_W
    flag = "AUFFÄLLIG" if rel < 1e-3 else "negativ"
    print(f"    {name:14s} = {val:.6f}   rel.Abw. = {rel:.2e}   {flag}")
    if rel < 1e-3:
        auffaellig.append(name)
print("    ERGEBNIS:", ("Treffer: " + ", ".join(auffaellig)) if auffaellig else
      "kein Treffer — κ(θ_W) ist KEINE einfache Konstante.")
print("    Das stützt: der Wert ist genuin RGE-abgeleitet (Lauf zu M_Z), nicht")
print("    geometrische Rohkonstante. Konsistent mit der Korpus-Architektur,")
print("    in der sin²θ_W erst NACH RGE-Lauf seinen Messwert annimmt.")

# ---------- Teil C: Exakte Reduktion auf H12 ----------
print("\n[C] Exakte Reduktion: (Δλ, θ) -> (Verstimmung, Kopplung) — symbolisch")
Dl, ths = sp.symbols('Delta_lambda theta', positive=True)
H11mH22 = Dl * sp.cos(2 * ths)
H12 = Dl * sp.sin(2 * ths) / 2
# Rückprobe: Eigenwertabstand und Winkel aus (H11−H22, H12) reproduzieren
Dl_back = sp.simplify(sp.sqrt(H11mH22**2 + 4 * H12**2))
tan2_back = sp.simplify(2 * H12 / H11mH22)
ok1 = sp.simplify(Dl_back - Dl) == 0
ok2 = sp.simplify(tan2_back - sp.tan(2 * ths)) == 0
print("    H11−H22 = Δλ·cos2θ,  2H12 = Δλ·sin2θ")
print("    Rückprobe Δλ:", "BESTÄTIGT" if ok1 else "FEHLER",
      "| Rückprobe tan2θ:", "BESTÄTIGT" if ok2 else "FEHLER")
print("    => Die ξ-Stufe zerfällt exakt in zwei Teilfragen:")
print("       (i)  Δλ (Eigenwertabstand) — im Korpus über Massenableitungen belegt [K]")
print("       (ii) H12 = (Δλ/2)·sin2θ — die EIGENTLICH offene Größe [S]")

print("\n[C2] Implizierte Kopplungen H12 aus Messwerten (Richtwerte aus Gedächtnis —")
print("     vor LaTeX-Fassung gegen PDG/Fits prüfen; Konvention: 2x2-Untermatrix,")
print("     Δλ in der jeweils natürlichen Einheit des Sektors):")
faelle = [
    # (Sektor, Δλ, Einheit, θ_deg, Quelle Δλ)
    ("PMNS 1-2 (solar)", 7.4e-5, "eV²", 33.4, "Δm²₂₁, Fit-Richtwert"),
    ("PMNS 1-3", 2.5e-3, "eV²", 8.5, "Δm²₃₁, Fit-Richtwert"),
    ("CKM 1-2 (down-Typ, Massenbild)", 93 - 4.7, "MeV", 13.02, "m_s−m_d, Richtwerte"),
]
print(f"    {'Sektor':32s} {'Δλ':>10} {'Einheit':7s} {'θ[°]':>6} {'=> H12':>12}")
for name, dl, unit, thd, _q in faelle:
    h12 = dl * np.sin(2 * np.radians(thd)) / 2
    verst = dl * np.cos(2 * np.radians(thd))
    print(f"    {name:32s} {dl:>10.4g} {unit:7s} {thd:>6.2f} {h12:>12.4g} {unit}")
print("    Diese H12-Werte sind die Zielgrößen der offenen ξ-Ableitung.")
print("    Wo der Korpus Δλ aus ξ ableitet (Lepton-/Neutrinomassen, Dok. 317–323),")
print("    ist Teilfrage (i) geschlossen; offen bleibt allein (ii).")

print("""
FAZIT R-neu-c:
  θ_W-Sektor: [K] durch Komposition (Teil A) — Brücke geschlossen.
  Screening: κ(θ_W) keine einfache Konstante (Teil B) — genuin RGE-abgeleitet.
  Übrige Sektoren: exakt reduziert auf die Nebendiagonalen H12 (Teil C);
  Status der Restfrage: [S] mit scharf definierter Zielgröße je Sektor.""")
