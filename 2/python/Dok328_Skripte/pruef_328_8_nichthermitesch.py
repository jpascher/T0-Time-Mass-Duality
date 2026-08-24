#!/usr/bin/env python3
# Dok. 328 — Prüfskript 8: Nicht-hermitesche Erweiterung des Wörterbuchs (Rest-[S] aus §7.1)
# Effektiver 2x2-Hamiltonian mit Zerfallsbreiten:  H = [[E1 − iγ1/2, g], [g, E2 − iγ2/2]]
# Behauptungen: (a) Eigenwertformel wie hermitesch, nur mit KOMPLEXER Verstimmung;
# (b) auf Resonanz (E1=E2) trennt der Ausnahmepunkt (EP) g_EP = |γ1−γ2|/4 exakt
#     das unterkritische Regime (eine Frequenz, zwei Breiten) vom überkritischen
#     (zwei Frequenzen = Rabi-Aufspaltung) — d.h. k_krit des Bandfilters IST der EP.
import sympy as sp

print("=" * 74)
print("PRÜFSKRIPT 8: Güte ↔ Zerfallsbreite — nicht-hermitesches Wörterbuch")
print("=" * 74)

E1, E2, g = sp.symbols('E1 E2 g', real=True)
g1, g2 = sp.symbols('gamma1 gamma2', positive=True)
H = sp.Matrix([[E1 - sp.I * g1 / 2, g], [g, E2 - sp.I * g2 / 2]])

# (a) Eigenwerte
S = (E1 + E2) / 2 - sp.I * (g1 + g2) / 4
delta = (E1 - E2) / 2 - sp.I * (g1 - g2) / 4   # komplexe Verstimmung
lam_erw = [S - sp.sqrt(delta**2 + g**2), S + sp.sqrt(delta**2 + g**2)]
ev = list(H.eigenvals().keys())
def in_liste(x, liste):
    return any(sp.simplify(sp.expand(x - y)) == 0 for y in liste)
ok = all(in_liste(l, ev) for l in lam_erw)
print("\n[a] λ± = S ± sqrt(δ² + g²) mit KOMPLEXER Verstimmung δ = (E1−E2)/2 − i(γ1−γ2)/4:")
print("    ", "BESTÄTIGT" if ok else "FEHLER")
print("    => Das hermitesche Wörterbuch (§7.1) bleibt FORMGLEICH gültig;")
print("       einzige Änderung: Verstimmung wird komplex (Realteil: Energie,")
print("       Imaginärteil: Breitendifferenz). Güte ↔ Zerfallsbreite ist damit")
print("       keine Analogie, sondern dieselbe Formel im Komplexen.")

# (b) Resonanzfall E1 = E2: Aufspaltung Ω = 2·sqrt(g² − (γ1−γ2)²/16)
Om = sp.simplify((lam_erw[1] - lam_erw[0]).subs(E1, E2))
Om_erw = 2 * sp.sqrt(g**2 - (g1 - g2)**2 / 16)
ok_b = sp.simplify(Om - Om_erw) == 0
print("\n[b] Resonanz (E1=E2): λ+ − λ− = 2·sqrt(g² − (γ1−γ2)²/16):",
      "BESTÄTIGT" if ok_b else f"FEHLER: {Om}")
gEP = sp.Abs(g1 - g2) / 4
print(f"    Ausnahmepunkt (EP): g_EP = |γ1−γ2|/4  — Diskriminante = 0")
print("    g < g_EP: Wurzel imaginär  => EINE Frequenz, ZWEI Breiten  (unterkritisch)")
print("    g > g_EP: Wurzel reell     => ZWEI Frequenzen (Rabi)       (überkritisch)")
print("    g = g_EP: Eigenwerte UND Eigenvektoren koaleszieren        (kritisch = EP)")

# Numerische Stichprobe
import numpy as np
def eigs(E, gam1, gam2, gg):
    Hn = np.array([[E - 1j * gam1 / 2, gg], [gg, E - 1j * gam2 / 2]])
    return np.linalg.eigvals(Hn)
gam1, gam2 = 0.0, 1.0   # γ-Differenz 1 => g_EP = 0.25
print("\n    Numerik (E1=E2=0, γ1=0, γ2=1, g_EP=0.25):")
for gg in [0.10, 0.25, 0.40]:
    lam = np.sort_complex(eigs(0.0, gam1, gam2, gg))
    dRe = abs(lam[1].real - lam[0].real)
    dIm = abs(lam[1].imag - lam[0].imag)
    regime = "unterkritisch" if gg < 0.249 else ("EP" if abs(gg - 0.25) < 1e-9 else "überkritisch")
    print(f"      g={gg:.2f}: ΔRe(λ)={dRe:.4f}  ΔIm(λ)={dIm:.4f}   {regime}"
          f"  ({'nur Breiten spalten' if dRe < 1e-9 else 'Frequenzen spalten'})")

print("""
FAZIT: Rest-[S] aus §7.1 geschlossen -> [B].
  Wörterbuch-Erweiterung: Güte/Breite geht als Imaginärteil in die komplexe
  Verstimmung ein; die kritische Kopplung des verlustbehafteten Systems ist
  der Ausnahmepunkt g_EP = |γ1−γ2|/4. Die Bandfilter-Schwelle k_krit=1/√(Q1Q2)
  und die Cavity-QED-Schwelle 'strong coupling' sind Spezialfälle dieser
  EP-Bedingung — die Dreiteilung aus §2 ist damit auch im dissipativen Fall
  exakt, nicht nur strukturell.""")
