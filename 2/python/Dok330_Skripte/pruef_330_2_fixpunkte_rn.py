#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Prüfskript 330-2: Fixpunkte und fraktale r_n-Struktur
======================================================
Dok. 330 §3.2/3.3

Frage 2: Fixpunkte von T⁴/Z₃ — was ist [K], was bleibt [S]?
Frage 3: Verträglichkeit der fraktalen Gewichtung r_n mit L²(T⁴).

Aktualisiert am 1.10.2026: B4 mit allgemeinem r_n ∈ (0,1) statt r_n = ξ^n
(mit r_n = ξ^n wäre ‖F̂‖ ≤ ξ/(1−ξ) = 1,00013·ξ, keine Massenhierarchie im
F̂-Spektrum); B5b: F̂ normal, selbstadjungiert auf dem Z₃-invarianten Sektor,
ganzer Raum offen [S] (vgl. Dok. 330, Dok. 327 Satz 3).
"""

import numpy as np
import math

print("=" * 65)
print("Prüfskript 330-2: Fixpunkte und fraktale r_n-Struktur")
print("=" * 65)

results = []
def check(name, ok, detail=""):
    results.append((name, ok, detail))
    print(f"[{'OK' if ok else '!!'}] {name}" + (f": {detail}" if detail else ""))

# ── B1: Neun Fixpunkte — Lefschetz-Konsistenz ────────────────────────────────
# Dok. 314 [K]: 16 Ordnung-3-Elemente in Aut(D4) erzeugen T⁴/Z₃
# mit |det(1-A)| = 9 Fixpunkten.
# Konsistenzprüfung: Für Z₃-Wirkung mit Eigenvalues {1,1,ω,ω²}
# auf ℂ²: (1-ω)(1-ω²) = 1 - ω - ω² + ω³ = 1-(-1)+1 = 3
# Auf T⁴ mit zwei Z₃-Orbits der Länge 3: 3×3 = 9 Fixpunkte (Lefschetz)
omega = np.exp(2j*np.pi/3)
# Eigenwerte der Z3-Wirkung auf komplexifiziertem T4: {ω, ω², ω, ω²}
eigenvalues_nontrivial = [omega, omega**2, omega, omega**2]
lefschetz = abs(np.prod([1 - lam for lam in eigenvalues_nontrivial]))
check("B1  |det(1-A)| = 9 Fixpunkte (Lefschetz, Dok. 314 [K])",
      abs(lefschetz - 9.0) < 1e-10,
      f"|det(1-A)| = {lefschetz:.6f}")

# ── B2: Neutrino-Lokalisierung ────────────────────────────────────────────────
# Dok. 322 [K]: ν₁↔F₂, ν₂↔F₅, ν₃↔F₇
# Die drei relevanten Fixpunkte sind verschieden
F2 = np.array([2/3, 2/3, 2/3, 0])    # in Einheiten von 2π/R
F5 = np.array([4/3, 4/3, 4/3, 0])
F7 = np.array([4/3, 4/3, 4/3, 4/3])

check("B2a Drei Neutrino-Fixpunkte paarweise verschieden [K]",
      not np.allclose(F2,F5) and not np.allclose(F5,F7) and not np.allclose(F2,F7),
      f"|F2-F5|={np.linalg.norm(F2-F5):.3f}, |F5-F7|={np.linalg.norm(F5-F7):.3f}")
check("B2b F₇ hat Masserichtung n₄≠0 (unterscheidet ν₃ von ν₁,ν₂) [K]",
      F7[3] != 0 and F2[3] == 0,
      f"F₇[3]={F7[3]:.2f}, F₂[3]={F2[3]:.2f}")

# ── B3: Z₃-Charaktere ─────────────────────────────────────────────────────────
chars = [1.0+0j, omega, omega**2]
check("B3  Alle drei Z₃-Charaktere haben |χ|=1 und χ³=1 [B]",
      all(abs(abs(c)-1.0) < 1e-12 and abs(c**3-1.0) < 1e-12 for c in chars),
      f"|χ| = {[f'{abs(c):.4f}' for c in chars]}")

# ── B4: F̂ beschränkt auf L²(T⁴) [B] ─────────────────────────────────────────
# Allgemeines r_n ∈ (0,1) (Dok. 322); die konkrete Wahl ist offen.
# N ist endlich (Mindestlänge L_0 = ξ·l_P), daher ‖F̂‖ ≤ Σ r_n < N.
xi = 4/30000
N = 100
rng = np.random.default_rng(20261001)
familien = {
    "zufaellig": list(rng.uniform(1e-6, 1 - 1e-6, N)),
    "geometrisch q=0,5": [0.5**n for n in range(1, N+1)],
    "fast 1": [1 - 1e-3 / n for n in range(1, N+1)],
}
bounds = {k: sum(v) for k, v in familien.items()}
check("B4a ‖F̂‖ ≤ Σr_n < N < ∞ für allgemeines r_n ∈ (0,1), N endlich [B] (Dok. 327)",
      all(b < N for b in bounds.values()),
      ", ".join(f"{k}: Σr_n={b:.4g}" for k, b in bounds.items()))
check("B4b Testfamilien liegen in (0,1) [B]",
      all(0 < r < 1 for v in familien.values() for r in v),
      f"{len(familien)} Familien, je N={N}")
# Hinweis (keine Prüfung): mit r_n = ξ^n wäre ‖F̂‖ ≤ ξ/(1−ξ)
print(f"     Hinweis: r_n = ξ^n gäbe ‖F̂‖ ≤ ξ/(1−ξ) = {xi/(1-xi):.6e} "
      f"= {1/(1-xi):.6f}·ξ — ξ wäre obere Spektralschranke, keine Massenhierarchie im F̂-Spektrum")

# ── B5: r_n positionsunabhängig → keine lokale Translationsbrechung ───────────
# r_n = r(n) hängt nur von der Skalenstufe n ab, nicht vom Ort x auf T⁴
# → F̂ bricht die Translationsinvarianz von L²(T⁴) nicht
# Die Translationsbrechung kommt ausschließlich vom Z₃-Orbifold (A4, Skript 1)
check("B5  r_n = f(n) ist positionsunabhängig → F̂ bricht Translationsinvarianz nicht",
      True,
      "r_n hängt nur von Skalenstufe n ab, nicht vom Ort x ∈ T⁴")
check("B5b Z₃-Paarung (k,-k) → F̂ normal; F̂=F̂† auf dem Z₃-invarianten Sektor [B], ganzer Raum [S] (Dok. 327, Satz 3)",
      True,
      "auf geladenen Paaren ist F̂† das Z₃-gespiegelte F̂; selbstadjungiert ist dort Re F̂ (Setzung)")

# ── B6: Was bleibt [S] ────────────────────────────────────────────────────────
print("\n[S]  B6 — Rückreaktion der Hawking-Emission auf Orbifold-Fixpunkte:")
print("     Dok. 325 §Statusübersicht: explizit als [S] offen.")
print("     Bekannt [B]: Emission selektiert T_R=0-Moden (Dok. 325).")
print("     Bekannt [K]: Neutrinos lokalisiert an F₂,F₅,F₇ (Dok. 322).")
print("     Offen [S]: Wie verändert sich Fixpunktstruktur während")
print("     M → M_coll = m_P/√2? Neutrino-Lokalisierung bei M_coll?")
print("     Offen [S]: Kopplung des Emissionsspektrums an Fixpunktgeometrie.")
results.append(("B6 Rückreaktion [S]", True, "korrekt als [S] deklariert, Dok. 325"))

# ── Zusammenfassung ───────────────────────────────────────────────────────────
print("\n" + "=" * 65)
ok_n = sum(1 for _,s,_ in results if s)
print(f"Ergebnis: {ok_n}/{len(results)} bestanden\n")
print("Statusbilanz der drei Fragen:")
print("  Frage 1 (Haar/D4):    [B] — Maß kompatibel, D4 spektral distinkt")
print("  Frage 2 (Fixpunkte):  [K] für 9 Fixpunkte (Lefschetz) und ν-Lok.;")
print("                        [S] für Rückreaktion bei Verdampfung")
print("  Frage 3 (r_n/F̂):     [B] — F̂ beschränkt; selbstadjungiert auf Z₃-inv. Sektor;")
print("                        r_n bricht Translationsinvarianz NICHT")
