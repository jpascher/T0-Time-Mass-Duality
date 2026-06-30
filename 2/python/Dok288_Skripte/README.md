# Dok 288 — Skripte (Nachrichtentechnische Rechenwege)

Reproduzierbare numpy-Skripte zu Dok. 288. Jedes prüft einen Rechenhebel der
DFT-/Zirkulant-Darstellung des Z₃-Massenoperators (r=√2, θ=2/9) maschinengenau.
numpy-only, Seed 20780458, keine externen Daten. `python3 <datei>.py`.

- `dft_eigenwerte.py` — Hebel 1: die Lepton-Massenwurzeln √m_k sind die 3-Punkt-DFT
  eines 3-Vektors c=(1, (√2/2)e^{iθ}, (√2/2)e^{-iθ}); Gegenprobe gegen Foot-Koide
  und eigvalsh (Δ ~ 9·10⁻¹⁶). Kein charakteristisches Polynom.
- `parseval_koide.py` — Hebel 2: Koide Q = 2/3 in zwei Parseval-Zeilen
  (Σ√m=3c₀, Σm=3Σ|c_j|²); Q über ganz θ∈[0,2π) konstant 0,666667 → Q hängt nur
  am Betrag r, nicht an der Phase θ.
- `operatorfunktionen.py` — Hebel 3: C=F†ΛF → f(C)=F†f(Λ)F; Potenz C⁵, Inverse C⁻¹,
  Exponential exp(C) als Skalar-Auswertung an drei Eigenwerten; Gegenprobe gegen
  matrix_power / inv / Taylor (Δ ~ 10⁻¹⁴).
- `faltung_multiplikation.py` — Hebel 4: Faltungssatz auf Z₃ — zirkuläre Faltung =
  punktweise DFT-Multiplikation; Matrixprodukt zweier Zirkulanten = drei Skalarprodukte
  (Δ ~ 9·10⁻¹⁶).
- `rekursion_iir.py` — Hebel 5: r(k+1)=r(k)(1−ξ) als IIR-Filter 1. Ordnung, Pol bei
  z=1−ξ=0,99986667, Zeitkonstante k*~1/ξ=7500; drei Regime als Pol-Lagen
  (innen/Kreis/außen).

## Befund
Die parallelen Darstellungen sind nicht nur Einordnung (Dok. 287), sondern Rechenwerkzeug:
weil der Massenoperator ein Z₃-Zirkulant ist, diagonalisiert ihn die DFT, und fünf
Standard-Hebel der Nachrichtentechnik werden anwendbar. Ehrlich: Rechenerleichterung,
keine Herleitung — die Transformation bewegt √2 und θ, sie erzeugt sie nicht (P35);
volle Hebelwirkung am C₃/Z₃-Sektor (3×3).

---
EN: numpy-only reproducibility scripts for Doc. 288. Each verifies one computational
lever of the DFT/circulant representation of the Z₃ mass operator to machine precision:
eigenvalues as a 3-point DFT, Koide Q via Parseval (phase-independent), operator
functions via DFT diagonalisation, the convolution theorem on Z₃, and the ξ-recursion as
a first-order IIR filter. Computational leverage, not derivation (P35).
