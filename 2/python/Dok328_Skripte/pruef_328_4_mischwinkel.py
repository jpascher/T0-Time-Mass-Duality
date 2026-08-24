#!/usr/bin/env python3
# Dok. 328 — Prüfskript 4: Mischungswinkel als Kopplungsgrade (Ziel R-neu-c, Strukturstufe)
# Liest bekannte Mischungswinkel über das bewiesene Wörterbuch (Skript 1) als
# normierte Kopplung κ_mix = 2H12/(H11−H22) = tan(2θ) und klassifiziert die Regime.
# KEINE ξ-Ableitung — reine Strukturübersetzung. Die ξ-Stufe bleibt offen ([S]).
import numpy as np

print("=" * 72)
print("PRÜFSKRIPT 4: Mischungswinkel als Kopplungsgrade — Strukturübersetzung")
print("=" * 72)
print("""
Übersetzung (aus Skript 1, [B]):  tan(2θ) = 2·H12/(H11−H22) ≡ κ_mix
  κ_mix << 1 : unterkritisch-analog (Kopplung klein gegen Verstimmung; schwache Mischung)
  κ_mix ≈ 1 : Übergangsbereich (Kopplung ≈ Verstimmung)
  κ_mix >> 1 : überkritisch-analog (nahe Entartung; Mischung → maximal, θ → 45°)
Hinweis: Die Bandfilter-Schwelle k_krit=1/√(Q1Q2) vergleicht Kopplung mit DÄMPFUNG;
κ_mix vergleicht Kopplung mit VERSTIMMUNG. Beide Lesarten sind im Dokument getrennt
ausgewiesen (§7); hier wird die Verstimmungs-Lesart geprüft.
""")

winkel = [
    # (Name, θ in Grad, Quelle der Zahl)
    ("Weinberg θ_W (FFGFT: sin²θ_W=0.2308)", np.degrees(np.arcsin(np.sqrt(0.2308))), "FFGFT Dok. 317–323"),
    ("Cabibbo θ_C (CKM 1-2)", 13.02, "PDG-Richtwert"),
    ("CKM θ_23", 2.35, "PDG-Richtwert"),
    ("CKM θ_13", 0.20, "PDG-Richtwert"),
    ("PMNS θ_12 (solar)", 33.4, "globale Fits, Richtwert"),
    ("PMNS θ_23 (atmosph.)", 49.0, "globale Fits, Richtwert"),
    ("PMNS θ_13 (Reaktor)", 8.5, "globale Fits, Richtwert"),
]

print(f"{'Winkel':38s} {'θ[°]':>7} {'sin²θ':>7} {'κ_mix=tan2θ':>12}  Regime-Lesart")
print("-" * 72)
for name, th_deg, _src in winkel:
    th = np.radians(th_deg)
    kappa = np.tan(2 * th)
    s2 = np.sin(th) ** 2
    if th_deg > 45:  # jenseits maximaler Mischung: Vorzeichenwechsel der Verstimmung
        lesart = f"|κ|={abs(kappa):.2f}, jenseits Entartung (Verstimmung wechselt Vorzeichen)"
    elif abs(kappa) > 3:
        lesart = "überkritisch-analog (nahe Entartung)"
    elif abs(kappa) > 0.5:
        lesart = "Übergangsbereich"
    else:
        lesart = "unterkritisch-analog (verstimmungsdominiert)"
    print(f"{name:38s} {th_deg:>7.2f} {s2:>7.4f} {kappa:>12.4f}  {lesart}")

print("""
BEFUND (Strukturstufe):
1. Die Quark-Mischung ist durchgängig unterkritisch-analog (κ_C≈0.49 an der
   Grenze, θ_23/θ_13 tief unterkritisch): verstimmungsdominierte Sektoren —
   konsistent mit stark hierarchischen Quarkmassen (große 'Verstimmung').
2. Die Lepton-Mischung (PMNS θ12, θ23) liegt im Übergangs- bis überkritischen
   Bereich; θ23≈49° sitzt praktisch AUF der Entartung (κ→∞ bei 45°) —
   konsistent mit quasi-entarteten Strukturen im Neutrinosektor.
3. θ_W (κ≈1.57) liegt im Übergangsbereich — weder verstimmungs- noch
   kopplungsdominiert.
OFFEN ([S], ξ-Stufe): ob die Verhältnisse H12/(H11−H22) je Sektor aus ξ folgen.
Das Wörterbuch selbst ist bewiesen [B]; die Regime-Zuordnung oben ist exakte
Umformung, keine neue Physik.""")
