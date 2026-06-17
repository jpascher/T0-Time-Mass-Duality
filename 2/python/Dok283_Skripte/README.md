# Dok283_Skripte — FFGFT ↔ HLV: die Brücke und die Gabelung

Begleitskript zu **Dok. 283**. Prüft die FFGFT↔HLV-Verbindung streng nach dem
Drei-Teile-Kriterium: (1) dasselbe strukturelle Objekt aus der eigenen Geometrie
jedes Modells, (2) explizite Abbildung, (3) Divergenzpunkt (kein Stufe-0-Gerüst).
numpy-only.

## ffgft_hlv_c3_bridge_probe.py
Sechs Checks. HLV ist ein ikosaedrischer 6D→3D-Cut-and-Project-Quasikristall
(Krügers exakter Projektor, τ=φ parallel, τ=−1/φ senkrecht). Die zyklische
Koordinaten-Abbildung (x,y,z)→(z,x,y) ist eine C₃-Achse der Ikosaedergruppe und
zerlegt die sechs Spalten in zwei 3-Zyklen.

- **Check 1** — Gram eines C₃-Orbits = exakter reeller Z₃-Zirkulant circ(1,1/√5,1/√5),
  r=2/√5≈0,894, θ=0, Koide 7/15 (Kriterien 1+2 erfüllt: FFGFTs Objekttyp lebt in
  HLVs Geometrie, Abbildung = C₃-Achseneinbettung).
- **Check 2** — alle 6×6-Skalarprodukte sind ±1/√5 (5-Zähligkeit verbietet √2 rigide).
- **Check 3** — r(τ)=2τ/(1+τ²)≤1 für alle τ ⇒ FFGFTs r=√2>1 ist mit keinem
  Cut-and-Project-Parameter erreichbar.
- **Check 4** — √2 nur in 3-zähliger Geometrie; FFGFTs Gram circ(1,1/√2,1/√2) PSD-gültig.
- **Check 5** — geschützt vs. generisch: tausende projizierte Punkte treffen auch
  1/√2, aber ungeschützt; nur die sechs geschützten Generatoren geben ±1/√5.
- **Check 6** — kompaktifiziertes HLV (rationaler Fibonacci-Approximant τ=p/q →
  periodischer Kristall auf T³): r(τ_n)→2/√5, Koide→7/15; die Gabelung übersteht den
  fairen kompakt-gegen-kompakt-Vergleich.

Befund: genuine Verbindung (gemeinsamer Z₃-Zirkulant + C₃-Abbildung) mit fundamentaler
Gabelung — 5-zählig (φ, 1/√5) gegen 3-zählig (√2, Koide 2/3). Was substanziell von
HLV bleibt, ist nicht die Geometrie, sondern die Spiral-Time (Phase R, χ-Gedächtnis),
die FFGFTs nicht-Markovschen Kern aus Dok. 282 trifft (§8/§9 des Dokuments).
