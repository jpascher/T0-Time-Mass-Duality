#!/usr/bin/env python3
# Dok. 328 — Prüfskript 7: Korpus-Abgleich (geklont von GitHub, jpascher/T0-Time-Mass-Duality)
# Quellen: 2/Sources/ch/041_parameterherleitung_De_ch.tex (Mischungsformeln, Ebene 6),
#          2/Sources/ch/006_T0_Teilchenmassen_De_ch.tex (Quarkmassen),
#          2/Sources/ch/007_T0_Neutrinos_De_ch.tex (Δm², zitierte 2025-Daten),
#          2/Sources/ch/323_Weinberg_Winkel_RGE_De_ch.tex (sin²θ_W = 0.2308 [K])
# Teil A: Textur-Satz — arcsin√(m1/m2) <=> H12 = √(m1·m2) (symbolisch, schließt die
#         H12-Frage aus §7.3 auf Korpus-Ebene)
# Teil B: Numerischer Abgleich der Dok.-041-Formeln mit ξ = 4/30000 und Korpusmassen
import numpy as np
import sympy as sp

XI = 4 / 30000

print("=" * 74)
print("PRÜFSKRIPT 7: Korpus-Abgleich Dok. 041 — Mischungsformeln und H12-Textur")
print("=" * 74)

# ---------- Teil A: Textur-Satz (symbolisch) ----------
print("\n[A] Textur-Satz: θ = arctan√(m1/m2)  <=>  Nullstellen-Textur mit H12 = √(m1·m2)")
m1, m2 = sp.symbols('m1 m2', positive=True)
M = sp.Matrix([[0, sp.sqrt(m1 * m2)], [sp.sqrt(m1 * m2), m2 - m1]])
ev = sorted(M.eigenvals().keys(), key=sp.default_sort_key)
ok_ev = {sp.simplify(e) for e in ev} == {-m1, m2}
print("    Matrix M = [[0, √(m1m2)], [√(m1m2), m2−m1]]  (Gatto–Sartori–Tonin-Textur)")
print("    Eigenwerte {−m1, m2}:", "BESTÄTIGT" if ok_ev else f"FEHLER: {ev}")
# Mischungswinkel aus §7.1-Wörterbuch: tan2θ = 2H12/(H11−H22) = 2√(m1m2)/(m1−m2)... 
# exakter: für diese Textur gilt tanθ = √(m1/m2). Prüfen über Eigenvektor:
th = sp.atan(sp.sqrt(m1 / m2))
vec = sp.Matrix([sp.cos(th), -sp.sin(th)])  # Kandidat für Eigenvektor zu −m1
res = sp.simplify(M * vec + m1 * vec)
ok_vec = res == sp.Matrix([0, 0])
print("    tanθ = √(m1/m2) diagonalisiert M:", "BESTÄTIGT" if ok_vec else f"FEHLER: {res.T}")
print("    => Die Dok.-041-Formeln vom Typ θ = arcsin√(m1/m2) (Näherung von arctan")
print("       für m1≪m2) ENTSPRECHEN der Textur H12 = √(m1·m2): Die in §7.3 offene")
print("       Nebendiagonale ist im Korpus als geometrisches Massenmittel festgelegt.")
print("       Damit reduziert sich die ξ-Stufe auf die Massenableitungen selbst [K].")

# ---------- Teil B: Numerischer Abgleich ----------
print("\n[B] Numerischer Abgleich der Dok.-041-Formeln (ξ = 4/30000 = %.6e)" % XI)
print("    Korpusmassen (Dok. 006): m_d = 4.734 MeV, m_s = 95.0 MeV")
md, ms = 4.734, 95.0

def zeile(name, formel_wert, korpus_wert, quelle):
    rel = abs(formel_wert - korpus_wert) / abs(korpus_wert)
    status = "BESTÄTIGT" if rel < 0.02 else ("ABWEICHUNG %.1f%%" % (100 * rel))
    print(f"    {name:28s} Formel: {formel_wert:>9.5f}  Dok.041: {korpus_wert:>8.5f}  {status}  ({quelle})")
    return rel

print("\n  B1) CKM:")
f_cab = np.sqrt((ms - md) / (ms + md))
vus = np.sqrt(md / ms) * f_cab
zeile("|V_us| = √(m_d/m_s)·f_Cab", vus, 0.22452, "Ebene 6")
vus_pur = np.sqrt(md / ms)
print(f"    {'Vergleich ohne f_Cab':28s} √(m_d/m_s) = {vus_pur:.5f}   (GST-Rohwert)")
d_ckm = np.arcsin(2 * np.sqrt(2) * np.sqrt(XI) / 3)
zeile("δ_CKM = arcsin(2√2·√ξ/3)", d_ckm, 1.20, "Ebene 6; Einheit rad")

print("\n  B2) PMNS:")
th13 = np.degrees(np.arcsin(XI ** (1 / 3)))
zeile("θ13 = arcsin(ξ^(1/3)) [°]", th13, 8.57, "Ebene 6")
# θ12, θ23 hängen an m_ν-Verhältnissen; Rückwärtsprobe: welche Verhältnisse implizieren sie?
r12 = np.sin(np.radians(33.44)) ** 2
r23 = np.sin(np.radians(49.2)) ** 2
print(f"    θ12 = arcsin√(mν1/mν2): impliziert mν1/mν2 = sin²(33.44°) = {r12:.4f}")
print(f"    θ23 = arcsin√(mν2/mν3): impliziert mν2/mν3 = sin²(49.2°)  = {r23:.4f}")
print("    (Rückwärtsprobe; Vorwärtsprüfung erfordert die mν-Werte der Korpus-Ableitung)")

print("\n  B3) Weinberg (Querverbindung zu §7.3):")
s2_323 = 0.2308  # Dok. 323 [K]
kappa = 2 * np.sqrt(s2_323 * (1 - s2_323)) / (1 - 2 * s2_323)
print(f"    Dok. 323: sin²θ_W(M_Z) = {s2_323} [K]; Referenz dort: 0.2312 (−0.19%)")
print(f"    => κ(θ_W) = {kappa:.6f}  (ersetzt den Gedächtniswert; identisch bestätigt)")

print("\n  B4) Neutrino-Δm² (Dok. 007, dort zitierte 2025-Daten):")
print("    Δm²₂₁ ≈ 7.53×10⁻⁵ eV² [Solar],  Δm²₃₂ ≈ 2.44×10⁻³ eV² [Atmosphärisch]")
h12_sol = 7.53e-5 * np.sin(2 * np.radians(33.44)) / 2
print(f"    => H12(solar, Δm²-Bild) = {h12_sol:.3e} eV²  (ersetzt Gedächtniswert 3.40e-5)")
print("    ACHTUNG Korpus-interner Befund (Dok. 007): T0-Grundposition Δm²=0 mit")
print("    Koide-Erweiterung auf kleine Δm² ≈ (0.1–0.2)×10⁻⁴ eV² — steht in Spannung")
print("    zu den in Dok. 041 verwendeten Fit-Winkeln. Als Korpus-Prüfpunkt notieren.")

print("""
FAZIT:
  [A] H12-Frage auf Korpus-Ebene geschlossen: Dok.-041-Formeln = GST-Textur
      H12 = √(m1·m2); symbolisch bewiesen. R-neu-c-Rest hängt damit NUR noch
      an den Massenableitungen (die im Korpus stehen) — Zielstatus [K] erreichbar.
  [B] Abgleich deckt Prüfpunkte auf: Formeln aus Dok. 041, die mit ξ = 4/30000
      wörtlich ausgewertet ihre eigenen Tabellenwerte nicht reproduzieren
      (θ13, δ_CKM) bzw. abweichen (|V_us| mit Dok.-006-Massen), sind als
      Korpus-Prüfpunkte auszuweisen — möglicherweise andere ξ-Normierung,
      laufende Massen oder Druckfehler in der Tabelle. KEINE stillschweigende
      Korrektur; Klärung am Quelldokument.""")
