# FFGFT Stage-10 BD17A — Ledger-Verdikt (3. Juli 2026)

## Verdikt: BLOCKED — unabhängig bestätigt

Marcels Stage-10-Lauf (Datei
`stage10_runN_BD17A_blind_dynamicCe_v1_1_fast_20260703T054020Z.zip`,
Zeitstempel 2026-07-03T05:40:20Z) meldet:

    STAGE10_BD17A_BLIND_DYNAMIC_CE_BLOCKED_OR_NOT_SEPARATED

Dieses Verdikt wurde von der FFGFT-Seite **unabhängig reproduziert**, indem
der VOR Dateneingang eingefrorene Verdikt-Harness (SHA256
99e11399f23377702c5878784d791f8fc90a350e7999f8c2906bf99221aab246,
UNVERAENDERT) auf Marcels Roh-Loop-Winkel
(`results/raw/loop_angle_samples_compact.csv`) angewendet wurde.

## Integritaets-Pruefung (alle bestanden)

- FFGFT-Harness-Hash unveraendert: 99e11399... (kein Lock-Bruch).
- Marcels Generator-Hash == versiegelter Wert: 8bd0f7ce1077c5ade851721089cee0ffbbf9f3ba4832b5526c9e07208d1b8fe0
  -> die verwendete Klasse WAR die vorregistrierte; Blindheit bestaetigt.
- Stage-9-CONFIG-Hash im Modul == versiegelt: 45020f82...c5f06c.
- theta_2_9_used_in_construction = False (blind), _in_scoring = True (vereinbart).
- scale_tuning_used = False, generator_tuning_used = False, wn_support_used = False.
- Generator-Selbsttest max abs diff 1.18e-16 (Maschinengenauigkeit).

## Zwei unabhaengige Methoden, identische Rangfolge

Marcels Kernel-Score (seine Methode):
  target median 0.01801 < best null edge_operator_shuffle 0.06171
  target minus best null = -0.04370;  target candidate fraction 0.0

FFGFT-Harness Orbit-Selektion (unsere Methode, pre-registriert):
  target-Orbit-Fraktionen: flat=0.7867, 1/9=0.1891, 2/9=0.0243, 4/9=0.0000
  -> 2/9 ist NICHT der Orbit-Modus des Targets (flach dominiert).
  Nulls mit hoeherer 2/9-Fraktion als Target:
     edge_operator_shuffle 0.0823, phase_randomized_edges 0.0783,
     random_skewadjoint_same_scale 0.0783
  -> DOPPELT blockiert: weder Orbit-Selektion von 2/9, noch Schlagen der Nulls.

Beide Methoden, voellig unabhaengig konstruiert, ergeben dieselbe Rangfolge
(edge_operator_shuffle staerkste, Target darunter) und dasselbe Verdikt.

## Gebuchtes Verdikt

BLOCKED. Die eingefrorene Stage-9-Klasse erzeugt keine Determinanten-Linien-
Holonomien, die 2/9 rad jenseits der harten Nulls selektieren. BD17A bleibt
fuer diese dynamische Nachfolger-Klasse blockiert.

## Was das NICHT bedeutet

- Kein Widerspruch zu Q=2/3 (geometrisch, magnitude-blind, unberuehrt).
- Kein Widerspruch zur θ=2/9-Struktur im FFGFT-Zirkulanten (andere Ebene:
  Massen-Spektrum, nicht HLV-Holonomie).
- Der No-Go war vorhergesagt: eine flache Z3-Holonomie kann 2/9 nicht als
  topologische Invariante tragen (Lindemann-Weierstrass, Dok 291); Stage 9
  lieferte nur eine ADMISSIBLE non-flache Klasse, keine 2/9-tragende. Dass
  auch die dynamische Klasse 2/9 nicht trifft, engt den Kandidatenraum ein.

## Konsequenz fuer die Siegel

Das Verdikt ist gebucht. Die drei Siegel koennen nun gemeinsam geoeffnet
werden:
  1. HLV Stage-9 generator/source 8bd0f7ce... (Marcel) — bestaetigt genutzt.
  2. FFGFT verdict harness 99e11399... — unveraendert angewandt.
  3. FFGFT reasoning master seal 858268... (Dok 291) — jetzt oeffenbar.
Die Blindheit war in beide Richtungen gewahrt: Marcels Klasse war vor jeder
2/9-Begruendung eingefroren, die FFGFT-Begruendung vor jedem Ergebnis.
Das Protokoll hat wie vorgesehen funktioniert — es hat ein echtes blindes
Verdikt erzeugt, und dieses ist negativ.
