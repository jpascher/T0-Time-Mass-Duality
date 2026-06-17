# Dok271_HICE_Holonomie_Skripte — FFGFT↔HLV Holonomie-/HICE-Audit

Der **Holonomie-Zweig** des FFGFT↔HLV-Vergleichs (Dok. 271), ergänzend zum
*Spektral*-Diskriminator in `Dok271_274_Skripte/`. Diese Skripte spiegeln Marcel
Krügers HICE-/Hybrid-HLV-Programm und José De Jesus' W_psi-Audit auf dem
FFGFT-T⁴-Träger und prüfen sie in Krügers Zulässigkeits-Sprache (Gate-Sets,
Claim-State-Ledger). Konservativer Maximal-Status: „candidate carrier", **nicht**
Validierung, **nicht** Verbindung zu HLV. numpy (einige scipy/sklearn/matplotlib).

## Der HICE-Zeugen-Faden (#1 → #7)
- **ffgft_t4_holonomy_witness.py** — FFGFT-T⁴-Holonomie-Zeuge (W = kleinster
  Eigenwert des Verbindungs-Laplacians), durch das HICE-Gate-Set (gauge-null →
  benign → destruktiv → matched null). Anker: ξ als irreduzible Minimal-Torsion
  (Dok. 172), H₁(T⁴)=Z⁴ (Dok. 230/189).
- **ffgft_t4_context_content_witness.py** — De Jesus' Kontext/Inhalt-Split
  (W_psi = λ_low[ctx+content] − λ_low[ctx]) auf der C³-ICE-Faser. Ergebnis:
  Channel-Swap NEGATIV (Z₃-symmetrische Achsen), Korridor monoton — gleicher
  Claim-State wie der HLV-Träger.
- **ffgft_t4_dynamical_u3.py** — dynamischer, zeit-indizierter U3(t)-Speicher
  (Krüger Sec. 13.5): bricht ein magnitude-gematchtes Speichergesetz die
  Z₃-Kanal-Symmetrie? (fairer L2-Vergleich Snapshot vs. Speicher).
- **ffgft_t4_coherence_observables.py** — kohärenz-auflösende Observablen (#7,
  Krügers HICE-MEM0-Frage): IPR, Low-Band-Streuung, Loop-Holonomie-Dispersion vs.
  das blinde λ_low.

## HLV-Falsifikation und Audit
- **ffgft_hlv_homology_check_v3.py** — Falsifikations-Prototyp für die
  HLV-Vortex/Randmoden-Behauptung (H₁-Persistenz, b₁(ε)-Kurvenform,
  Permutationstest, N-Skalierung). Entspricht dem HLV-Homologie-Test (vgl. Dok. 276):
  HLV trennt scharf von kristallinen Kontrollen, nur schwach von generischem
  √2-Cut-and-Project. numpy+scipy (gudhi/matplotlib optional).
- **hice_pilot.py** — unabhängige Implementierung von Krügers Hybrid-HLV-Zelle
  (HICE7): nativer Z⁶-Cut-and-Project-Backbone, U(1)-Faser, Gates HICE1–4 mit λ₂.
  Ergebnis: Benign-Stabilität FAIL → reproduziert Krügers „precondition not
  satisfied". Erzeugt `hice_pilot.png`.
- **ffgft_phi3_pairwise_audit.py** — symmetrischer all-vs-all-Audit von Krügers
  Run PHI3 (Zenodo 10.5281/zenodo.20692350): zeigt, dass φ **kein** Ausreißer ist
  (jede Irrationale trennt von jeder anderen) ⇒ φ-Spezifität ist ein Artefakt des
  asymmetrischen Tests. Stützt Dok. 281 (φ ohne Sonderstatus) und Dok. 275.
  Eingabe `feature_table.csv` **liegt bei** (Krügers Run-PHI3-NATIVE6D-Output,
  320 Zeilen, 8 Ensembles; Zenodo 10.5281/zenodo.20692350). Lauf:
  `python3 ffgft_phi3_pairwise_audit.py feature_table.csv` — reproduziert AUC-Matrix
  durchweg 1,0, φ kein Ausreißer ⇒ φ-Spezifität nicht belegt.
  numpy+pandas+sklearn+matplotlib.

Lauf: `python3 <skript>.py`.
