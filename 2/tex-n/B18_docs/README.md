# B18 Erklaerungsdokumente (DE)

Dieses Verzeichnis enthaelt alle neu erstellten deutschsprachigen B18-Erklaerungsdokumente zu den Python-Skripten unter `2\python`.

* Alle Dateien haben Namen der Form `B18_..._Erklaerung.tex` (und die passende `*.pdf`) oder `B18_Gesamt_Hierarchische_Formeln.*`.
* Die Praeambel wird weiterhin ueber `\input{../../../T0_preamble_shared-ebook_De}` aus dem Projektwurzelverzeichnis eingebunden.
* Aeltere, nummerierte TEX-Kapitel (z.B. `006_T0_Teilchenmassen_De.tex`) verbleiben im Verzeichnis `de_standalone` und bilden zusammen mit diesen B18-Dokumenten die vollstaendige Dokumentation.

## Zuordnung Python-Skripte → B18-TEX

- `B18_Weltformel_Erklaerung.tex`: `Weltformel_B18.py`, `Weltformel_B18_FINAL.py`, `WELTFORMEL_B18_COMPLETION.py`
- `B18_Leptonen_Grundlagen_Erklaerung.tex`: `elektron.py`, `myon.py`, `massen-check.py`, `B18_myon_masse_check.py`
- `B18_Lepton_Genesis_Erklaerung.tex`: `B18_Mass_Geometry_Ratio.py`, `B18_Lepton_Final_Genesis.py`
- `B18_Tau_und_Neutrino_Torsion_Erklaerung.tex`: `g-2-tau-berechnug.py`, `g-2-neutrino.py`
- `B18_myon_lebensdauer_Erklaerung.tex`: `B18_myon_lebensdauer.py`
- `B18_Lepton_C_Unified_Erklaerung.tex`: `B18_C_Lepton_Unified.py`, `B18_Tau_Pure_Ratio.py`, `tau-lepton.py`
- `B18_g2_Pure_Geometry_Erklaerung.tex`: `B18_g2_Pure_Geometry.py`
- `B18_g2_T0_Korrektur_Erklaerung.tex`: `calc_g2_T0_full.py`
- `B18_g2_Anomalie_Erklaerung.tex`: `g-2-Anomalie.py`
- `B18_g2_Torsions_Resonanz_Erklaerung.tex`: `g-2-test.py`, `g-2-test2.py`, `g-2-berechnug.py`, `g-2-berchnug.py`, `g-2-Anomalie-check.py`
- `B18_g2_Holographic_Delta_Erklaerung.tex`: `B18_g2_Holographic_Delta.py`
- `B18_g2_Kristall_Erklaerung.tex`: `B18_g2_Elektron_Muon_Vergleich.py`
- `B18_g2_Chiral_Crystal_Erklaerung.tex`: `B18_g2_Chiral_Crystal.py`
- `B18_Quarks_und_Baryonen_Erklaerung.tex`: `up-down.py`, `B18_Strange_Quark_Resonance.py`, `B18_Charm_Quark_Genesis.py`, `B18_Bottom_Quark_Logic.py`, `top-quark.py`, `B18_Top_Quark_Interference.py`, `proton.py`, `neutrino-torsion.py`, `B18_neutrino_torsion.py`
- `B18_Higgs_und_Bosonen_Erklaerung.tex`: `B18_Higgs_Lattice_Stiffness.py`, `Higgs-Kondensat.py`, `Higgs-Kondensat1.py`, `Higgs-Kondensat2.py`, `B18_W_Boson_Torsion.py`, `w-boson.py`, `B18_Z_Boson_Torsion.py`, `z-boson.py`
- `B18_Gravitation_und_Kosmos_Erklaerung.tex`: `B18_Gravitation_Check.py`, `gravitation-check.py`, `dunkle-energie.py`, `torsions-kleber.py`, `torsions-licht.py`
- `B18_Gravity_Pressure_Erklaerung.tex`: `B18_Gravity_Pressure.py`
- `B18_Torsion_und_Licht_Erklaerung.tex`: `torsions-licht.py`, `torsos-temperatur.py`, `Zeitdilatation-check.py`, `Groesse-dieser-Flecken.py`/`Größe-dieser-Flecken.py`, `Universal-Skript.py`
- `B18_Torsion_und_Galaxien_Erklaerung.tex`: `torsions-kleber.py`, `Ladungs-Resonanz.py`, `Klebe-Effekt.py`, `liniendichte.py`, `zellen.py`, `Groesse-dieser-Flecken.py`/`Größe-dieser-Flecken.py`
- `B18_SubPlanck_Skala_Erklaerung.tex`: `B18_Planck_Verifikation.py`, `b18_c_final.py`, `kopplungsanalyse_t0.py`, `torsions_resonanz_scan.py`
- `B18_Bell_und_Verschraenkung_Erklaerung.tex`: `torsions-verschränkung.py`, `bell_73qubit_FIXED.py`, `alfa-check.py`, `C-frac.py`
- `B18_T0_Quantum_Computer_Erklaerung.tex`: `t0_shor_production.py`, `t0_shor_complete.py`, `t0_cosmic_qubit_simulator.py`, `t0_cosmic_error_correction.py`, `t0_cosmic_data_analyzer.py`
- `B18_Event_Horizon_Erklaerung.tex`: `B18_Event_Horizon_Final.py`
- `B18_FFGFT_Torsion_Erklaerung.tex`: `ffgft_torsion.py`, `FFGFT_Fractal_Correction.py`, `ffgft_constants.py`
- `B18_FFGFT_Master_Validator_Erklaerung.tex`: `ffgft_constants.py`, `ffgft_torsion.py`, `031_master.py`, `system_bias.py`
- `B18_Gesamt_Hierarchische_Formeln.tex`: fasst alle oben genannten Bereiche (Weltformel, Leptonen, g-2, Quarks, Gravitation/Kosmos, FFGFT, Bell/T0-Qubit) hierarchisch zusammen, ohne neue eigene Python-Skripte einzufuehren.
