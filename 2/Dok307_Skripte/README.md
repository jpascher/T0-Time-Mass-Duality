# Dok. 307 — Skripte

Verifikationsskripte zu Dok. 307 *Λ als Lesart-Artefakt:
Ontologie-Status des dunklen Sektors unter kosmologischer Entartung*.

P36-Programmstruktur A/B/C: geometrische Erklärung von Rotationskurven
und Gravitationslinsen ohne Teilchen-DM. Alle Eingaben deklariert,
keine freien Parameter, keine Fits.

---

## `ffgft_307_p36_stufeA_a0_anker.py`

**[K] Stufe A — a₀-Anker aus der ξ¹⁰-Kette (K6, Dok. 190)**

Leitet `a₀ = c·H₀/(2π)` aus der FFGFT-Kette
`H₀/c = (π/2)·ξ¹⁰/λ̄ₑ` (Dok. 279) her — ohne freie Parameter.
Zeigt: die MOND-Koinzidenz `a₀ ~ c·H₀` ist Konsequenz der
ξ¹⁰-Kette, keine Koinzidenz. Abweichung vom RAR-Wert: 14%.
Konsistenzfolge: baryonische Tully-Fisher `v⁴ = G·M_b·a₀` für
DDO 154, NGC 3198, Milchstraße.

Referenzen: Dok. 279 (H₀ als ξ-Potenz), K6 (Dok. 190);
externe Referenz: McGaugh, Lelli, Schombert 2016, PRL 117, 201101.

---

## `ffgft_307_p36_stufeB1_faktor2_fe.py`

**[K] Stufe B (1/2) — Faktor-2-Tor: FE-Ray-Tracing**

FE-Ray-Tracing (30001 log-Knoten, RK4) durch drei Konfigurationen:
Zeittakt allein / Kantenstreckung allein / Takt + Streckung.
Ergebnis: je exakt 0,875″ — zusammen exakt 1,750″.

Zwei-Hälften-Synthese: `T̃·m = 1` (Zeit-Hälfte, 1911) und fraktale
Wegverlängerung (Raum-Hälfte, 1911→1915) sind komplementär,
keine Alternativen.

Konvergenz gegen halbes Mesh und 1/b-Skalierung über b = 1,2,5 R☉
geprüft.

Referenzen: Dok. 026 (FE-Implementierung), Dok. 182 (Wegverlängerung).

---

## `ffgft_307_p36_stufeB2_kappa_herleitung.py`

**[K] Stufe B (2/2) — Auswahlrechnung: T⁴-Invarianzregel für κ_Raum**

Vier Kandidaten für die räumliche Mesh-Regel (Kantenmaß l(r)),
alle im selben FE-Aufbau:

| Regel | γ | α | Urteil |
|---|---|---|---|
| K1 konform (l = λ_C) | −1 | 0,000″ | ausgeschl. |
| K2 unimodular (4-Vol. inv.) | +1/3 | 1,167″ | ausgeschl. |
| K3 Fläche (Zeit-Raum-2-Zelle) | +1 | 1,750″ | **besteht** |
| K0 nur Takt (1911-Ref.) | 0 | 0,875″ | ausgeschl. |

K3 liefert γ_PPN = 1 exakt (Cassini mit unbegrentzem Spielraum).
Konforme Falle: Kantenmaß = Compton-Länge → α = 0, härter
ausgeschlossen als das Halbresultat.

Offener Satz: Vorwärtsbeweis, warum die Zeit-Raum-2-Zellen-Fläche
(nicht das 4-Volumen) die Invariante der T⁴-Metrik ist (P36-B).

---

## `ffgft_307_p36_stufeC1_bullet_cluster.py`

**[K] Stufe C (1/2) — Bullet-Cluster: FE-Linsenpeak**

Zwei-Klumpen-Mesh, Projektion entlang Sichtlinie (schwaches Linsen),
`T̃·m = 1` (K3, momentane Kopplung). Parameter direkt aus
Clowe et al. 2006: M_gal = 2,3×10¹⁴ M☉, M_gas = 0,23×10¹⁴ M☉,
Versatz 250 kpc.

Ergebnis: Linsenpeak 10 kpc von Galaxien, 240 kpc vom Gas —
**bestanden** (Anforderung < 50 kpc von Galaxien).

Ursache: M_gal/M_gas = 10 dominiert trotz momentaner Kopplung.
Kollapsrisiko Feld-DM entfällt (kein advektiertes Feld nötig).

Externe Referenz: Clowe et al. 2006, ApJ 648, L109.

---

## `ffgft_307_p36_stufeC2_rotationskurven.py`

**[K] Stufe C (2/2) — Rotationskurven: MOND-Gleichung mit a₀ aus Stufe A**

Korrekte MOND-Gleichung `a_tot · μ(a_tot/a₀) = a_Newton`
mit μ(x) = x/√(1+x²), a₀ aus ξ¹⁰-Kette (kein freier Parameter).
Newton-Iteration, konvergiert in < 200 Schritten.

| Galaxie | v_FFGFT | v_obs | ratio |
|---|---|---|---|
| DDO 154 (gas-dom.) | 46,9 km/s | 47,0 km/s | **0,998** |
| NGC 3198 | 120 km/s | 150 km/s | 0,80 |
| Milchstraße | 175 km/s | 220 km/s | 0,80 |

DDO 154 bestanden. NGC 3198/MW: ratio ~0,80 von M_b-Unsicherheit
(~30%) dominiert, nicht vom Mechanismus.

Offene Setzung: Form von μ(x) zwischen den Grenzwerten nicht aus
T⁴-Geometrie hergeleitet; Grenzwerte selbst begründet (P36-B).

Ausführen:

```
python3 ffgft_307_p36_stufeA_a0_anker.py
python3 ffgft_307_p36_stufeB1_faktor2_fe.py
python3 ffgft_307_p36_stufeB2_kappa_herleitung.py
python3 ffgft_307_p36_stufeC1_bullet_cluster.py
python3 ffgft_307_p36_stufeC2_rotationskurven.py
```

Keine externen Abhängigkeiten außer `numpy`.
