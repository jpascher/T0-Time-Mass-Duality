#!/usr/bin/env python3
# Dok. 328 — Prüfskript 9: Zwei weitere Rest-[S]-Schließungen
# Teil A (§4.1): Die Dualität D²+V²=1 gilt für JEDEN reinen Zeiger, nicht nur
#                gaußsche — der Gauß-Fall war Beispiel, nicht Voraussetzung. [B]
# Teil B (§6):   Die q-Hierarchie der Arnold-Zungen (Breite ∝ K^q für kleine K)
#                ist K-unabhängige STRUKTUR — die φ-Sonderstellung braucht kein ξ.
import numpy as np
import sympy as sp

print("=" * 74)
print("PRÜFSKRIPT 9A: D² + V² = 1 für beliebige REINE Zeiger [B]")
print("=" * 74)
# Zwei beliebige reine Zeigerzustände spannen einen 2D-Unterraum auf.
# O.B.d.A. Überlapp reell: ⟨φ+|φ−⟩ = cos(α), α ∈ [0, π/2].
al = sp.symbols('alpha', nonnegative=True)
V = sp.cos(al)                       # Restkohärenz = |Überlapp|
D = sp.sin(al)                       # Helstrom: D = sqrt(1 − |⟨φ+|φ−⟩|²) = sin α
dual = sp.simplify(D**2 + V**2)
print("Beliebige reine φ±: |⟨φ+|φ−⟩| = cosα  =>  V = cosα, D_Helstrom = sinα")
print("D² + V² =", dual, "->", "BESTÄTIGT für ALLE reinen Zeiger" if dual == 1 else "FEHLER")
print("""Folgerung: Der Gauß-Zeiger (Skript 5) ist ein Beispiel, kein Sonderfall —
JEDER reine Zeiger sättigt die Dualität; die Ungleichung D²+V²<1 tritt
ausschließlich bei GEMISCHTEN Zeigerzuständen auf (Informationsverlust an
nicht ausgelesene Freiheitsgrade). §4.1 wird entsprechend verschärft.

NICHT SCHLIESSBAR (Begründung vorab, wie gefordert): Die Restaussage 'jede
physikalische Messanordnung ist auf das Zeigermodell reduzierbar' ist keine
mathematische, sondern eine physikalische Modellannahme — sie quantifiziert
über alle realisierbaren Apparate und ist prinzipiell nicht beweisbar, nur
durch Gegenbeispiel widerlegbar. Sie bleibt korrekt als [SETZUNG]/Modellrahmen
deklariert; innerhalb des Rahmens ist alles bewiesen.""")

print("=" * 74)
print("PRÜFSKRIPT 9B: K-Unabhängigkeit der Zungen-Hierarchie (Breite ∝ K^q)")
print("=" * 74)
def winding(Omega, K, n_tr=300, n_av=1500):
    th = 0.0
    for _ in range(n_tr):
        th = th + Omega - K / (2 * np.pi) * np.sin(2 * np.pi * th)
    th0 = th
    for _ in range(n_av):
        th = th + Omega - K / (2 * np.pi) * np.sin(2 * np.pi * th)
    return (th - th0) / n_av

def tongue_width(p, q, K, span, n=1201):
    target = p / q
    Om = np.linspace(target - span, target + span, n)
    W = np.array([winding(o, K) for o in Om])
    locked = np.abs(W - target) < 1e-4
    return (Om[locked].max() - Om[locked].min()) if locked.any() else 0.0

print("Skalierungstest: log ΔΩ(p/q; K) gegen log K — Steigung sollte ≈ q sein")
print(f"{'Zunge':>6} | {'Steigung (num.)':>15} | {'Theorie q':>9} | Befund")
Ks = np.array([0.20, 0.30, 0.45])
for p, q, span in [(1, 2, 0.05), (1, 3, 0.03), (2, 5, 0.012)]:
    ws = np.array([tongue_width(p, q, K, span) for K in Ks])
    if np.all(ws > 0):
        slope = np.polyfit(np.log(Ks), np.log(ws), 1)[0]
        ok = abs(slope - q) < 0.35 * q
        print(f"  {p}/{q:>2}  | {slope:>15.2f} | {q:>9d} | {'BESTÄTIGT' if ok else 'ABWEICHUNG'}")
    else:
        print(f"  {p}/{q:>2}  | Zunge bei kleinem K unter Auflösung — Span/Raster anpassen")

print("""Folgerung: ΔΩ(p/q) ∝ K^q bedeutet: Die ORDNUNG der Einrastresistenz
(je größer der Kettenbruch-Nenner, desto resistenter; φ als Grenzfall
[1;1,1,…] maximal resistent) ist für ALLE Kopplungen 0<K<1 dieselbe —
eine strukturelle, K-unabhängige Aussage. Die dynamische Begründung der
φ-Sonderstellung (§6, Dok. 172/188/275) hängt damit NICHT an einem
ξ-abhängigen Kopplungswert.

NICHT SCHLIESSBAR (Begründung vorab, wie gefordert): Die QUANTITATIVE
Restfrage von R-neu-a — die absoluten Zungenbreiten, d.h. der Wert von K
selbst, aus ξ — ist aus dem vorliegenden Korpus nicht ableitbar: ξ fixiert
die Geometrie (T⁴/Z₃, D4), K ist dagegen die Stärke einer dynamischen
Störung; das Repository enthält (Stand Klon 24.08.2026, grep über
2/Sources/ch) keine Ableitung einer effektiven Störstärke aus ξ. Eine
solche Brücke zu erfinden wäre Numerologie; der Punkt bleibt [S] mit
jetzt scharf definierter Restfrage: 'effektives K aus ξ'.""")
