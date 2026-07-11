# Dok. 304 — Skripte

Verifikationsskripte zu Dok. 304 *Der Gedächtnis-Reflex*, Abschnitt
„Der Messschnitt: der bezuglose Ausschnitt und der Linearisierungs-Reflex".

## `ffgft_304_linearisierungsfehler_probe.py`

Prüfskript (kein Beweis), deterministisch, nur Standardbibliothek (`math`).

Rechnet den Linearisierungsfehler eines Messausschnitts der Zeit-Windung
exakt aus der Rekursion `xi_{n+1} = xi_n (1 - 100 xi_n)`, `xi_0 = 4/30000`,
und zeigt:

- Der Fehler je `2·pi` ist der Fehler im akkumulierten Präzessionswinkel
  `beta = 2·pi·D(k)`:
  `e(k,w) = w·d_k − (D(k+w) − D(k)) = x − ln(1+x)`, mit `x = w·100·xi_k = w/(k+75)`.
- Drei Regime: kleines Fenster `~ x²/2`; skaleninvariantes Fenster `x=1 → 1−ln2`
  (asymptotisch); makroskopischer Grenzfall `e → 0 ~ (1/2)(w/(k+75))²`.
- Ehrliche Buchung: `1−ln2` und der Vorfaktor `1/2` sind im makroskopischen
  Grenzfall exakt, mit einer Korrektur `O(1/k)` bei endlicher Position (die
  geschlossene Form `ln(1+k/75)` trägt einen beschränkten, γ-artigen Versatz
  gegenüber der exakten Summe). Der **exakte Koeffizient** dieser Korrektur
  bleibt offen (Euler–Maclaurin von `D(k)`).
- Eingerollt vs. ausgerollt (Abschnitt [6]): eingefrorenes `xi` gibt `d=1/75`
  konstant → Schließung nach genau 75 **kongruenten** Teilen (`Z/75`, exakt);
  der Skalenlauf macht daraus die log-Spirale, Selbstähnlichkeit `exp(2·pi·a) ≈ e`
  (nur **asymptotisch** exakt). Daher gilt Bezuglosigkeit strikt nur ausgerollt;
  eingerollt bleibt ein periodischer Bezug (Ort mod 75). Was beides überlebt:
  die **Ordnung** (U1).

Ausführen:

```
python3 ffgft_304_linearisierungsfehler_probe.py
```

Referenzen: Dok. 295 (Log-Spirale, `D(k)`, Akkumulation gegen beschränkten Kern),
Dok. 296 (`D(k)` als messbare Zeit), Dok. 301 (drei Ebenen, Wort-Reflex),
Dok. 257 (Windungsquant als Bit-Grenze).
