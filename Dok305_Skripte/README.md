# FFGFT Krümmungstreue-Probe (Dok. 304 / Dok. 295)

**Prüfskript, kein Beweis.** Deterministisch, nur Standardbibliothek (`math`).

## Was es zeigt

Die FFGFT-seitige These aus Dok. 304: Die trennende Achse zwischen einem
**krümmungstreuen** (log-Spiral-) Akkumulator und einem **gleichförmigen**
(archimedischen) Akkumulator ist **nicht die Reichweite, sondern die Krümmungstreue**.

Der Prüfstand stellt beide Akkumulatoren mit **gleicher Reichweite** gegenüber
(gleiche Gesamtakkumulation D(N)) und zeigt:

- **Reichweiten-Test** — beide unbeschränkten Akkumulatoren behalten einen
  beliebig alten Impuls; ein endlicher Kern verliert ihn. Reichweite trennt
  {Akkumulatoren} von {endlichem Kern}, **nicht** krümmungstreu von gleichförmig.
- **Krümmungstreue-Test (e-Kriterium, Dok. 295)** — drei Signaturen trennen sauber:
  - Selbstähnlichkeit: D(2k) − D(k) → **ln 2** (skaleninvariant) vs. wächst linear mit k;
  - Ganghöhen-Zerfall: d_n ~ n^(−p) mit **p ≈ 1** (1/n) vs. p = 0 (konstant);
  - Skalen-Ratio: k-Faktor pro Einheits-Zuwachs von D → **e** vs. 1.

Die Konvergenz ist asymptotisch exakt (O(1/k)-Rest, konsistent mit Dok. 304 §Kongruenz).

## Claim-state

- Das **e-Kriterium und die Trennung** sind FFGFT-intern aus ξ / der Rekursion
  ξ_{n+1} = ξ_n(1 − 100 ξ_n) ableitbar — **proven** (Dok. 295).
- Der Prüfstand etabliert **keine** Spezifität irgendeines kognitiven M_B. Ob die
  Krümmungstreue ein operationales, funktional definiertes M_B trennt, bleibt die
  **restricted-Brücke (Kategorie B)** und verlangt einen eigenen, **unabhängigen,
  gemeinsam versiegelten** Benchmark — keine FFGFT-interne Rechnung.

## Ausführen

```
python3 ffgft_kruemmungstreue_probe.py
```

Kein Zufall, keine externen Abhängigkeiten, reproduzierbar.
