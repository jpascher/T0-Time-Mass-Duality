# FFGFT Changelog — laufend ab v1.3.4

**Grundlage:** Dok. 190 (Korrekturregister)  
**Archiv bis v1.3.3:** [`000_FFGFT_Changelog_De.md`](000_FFGFT_Changelog_De.md)

Neue Einträge werden hier oben eingefügt (neueste zuerst).

---

## 26. August 2026 — v1.3.4: Dok. 328, 330, 332 · Register R93–R96

### Dok. 328 — Kopplungsregime, Resonanz und Synchronisation (DE+EN, je ~12 S.)

Nachrichtentechnische Dreiteilung (unterkritisch / kritisch / überkritisch,
relativ zu Systemdämpfungen) als strukturelles Ordnungsprinzip. Dieselbe
Struktur kehrt in Quantenoptik (strong coupling), Teilchenphysik (Mischung,
avoided crossing) und Synchronisationstheorie (Kuramoto-Schwelle, Arnold-Zungen)
wieder. Für FFGFT: natürliche Sprache für Teilchen als Resonanzzustände.

- **[B]** Wörterbuch Zweikreis ↔ 2×2-Mischung; Ausnahmepunkt g_EP = |γ₁−γ₂|/4
- **[B]** Dualität D²+V²=1 für alle reinen Zeiger; Messübergang κ = d/(2σ)
- **[K]** κ_mix(θ_W) ξ-abgeleitet über Komposition mit Dok. 323; Screening negativ
- **[B]** GST-Textur H₁₂=√(m₁m₂) symbolisch bewiesen (Dok.-041-Formeln)
- **[K]** K_eff = 2πξ ≈ 8,4×10⁻⁴; φ außerhalb aller Arnold-Zungen
- Vier Prüfpunkte in Dok. 041 identifiziert (Autorenentscheidung erforderlich)

**Neu:** Marker **[E]** eingeführt für etablierte externe Formalismen
(Zweikreis, Kuramoto) ohne Korpus-Freigabe als [K]/[B].  
Zehn Prüfskripte.

### Dok. 330 — Drei Operationen von T⁴ zum Beobachtraum (DE+EN, je ~14 S.)

Konsolidiert Typ-I/II/III-Klassifikation (Dok. 270); grenzt FFGFT von diskreten
Emergenzmodellen ab. HLV (Krüger, August 2026) als Fallstudie.

- **Typ I [B]:** S¹_m → ℝ_t via T̃·m=1; informationserhaltend (Pullback p*)
- **Typ II:** D3→D2→D1 geometrische Projektion; verlustbehaftet
- **Typ III [K]/[B]:** T⁴ ↔ H bijektiv, verlustfrei
- **T⁴ flach [K]:** K=0 punktweise via Metrik-Abstieg (R95)
- **D₄-Spezifitätstest [S]:** adversariell gegen angepasste Träger — offen

**R93 [B]:** S_BH(M_coll) = 2π nat = n_thresh(Matzke) in Bit;
Restentropie des Endpunkts (Dok. 325, 329)  
**R94 [B]:** I_Sektor/I_thermisch = log₂3 für alle M;
Strukturkonstante der ℤ₃-Geometrie (Dok. 325)  
**R95:** Zwei Formulierungspräzisierungen nach externem Review (Krüger):
(i) Flachheit K=0 punktweise [B]; (ii) „selbstadjungiert" = beschränkt + symmetrisch;
(iii) Typ-I-Pullback p* [B]; (iv) D₄-Spezifitätstest [S] offen

### Dok. 332 — Zwei Wege vom Diskreten zum Kontinuum (DE+EN, je ~16 S.)

Allgemeiner Vergleichsaufsatz (kein originärer FFGFT-Beweistext).
Referiert Krügers Preprint (Zenodo DOI 10.5281/zenodo.22105698).

Zwei Strategien: (1) Regge/Kettenkomplex — Kategorienfehler blockiert,
Kontinuumslimes via Mosco-Konvergenz *postuliert*. (2) Kanonischer
Funktions-Pullback (FFGFT) — Per_{Rm}(ℝ_t) ≅ L²(S¹_m) [B] (R96).

**R96 [B]/[K]** (zweite Krüger-Rückmeldung, 26. Aug. 2026):
Per_{Rm}(ℝ_t) mit Pro-Periode-Norm ≅ L²(S¹_m), NICHT L²(ℝ_t) —
Pullback ist Darstellungswechsel, kein neuer Sektor [B].
Nash–Kuiper-Zuschreibung in Dok. 330/R95(i) korrigiert:
Existenzsatz für C¹, keine C²-Nichteinbettbarkeitsaussage [K].  
Prüfskript: `pruef_332_krueger_periodizitaet.py`

---

