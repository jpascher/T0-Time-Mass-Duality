# Prüfskripte zu Dok. 075, 076, 176 (Periodenfindung und Faktorisierung)

Reine Standardbibliothek, Sollwerte als Assertions, Seed 20780458.

| Skript | Inhalt | Status |
|---|---|---|
| `s1_periodensuche.py` | Korrektheit der Periodenfindung; Skalierung über die mittlere multiplikative Ordnung; Primfaktorzerlegung der σ-Nenner; Vergleich mit Probeteilung und Pollard ρ | [K] |
| `s3_thermik_zustandsraum.py` | Thermische Besetzung nach Trägerfrequenz; Kühlkosten nach Carnot; Dimensionsvergleich der Zustandsräume; Gottesman-Knill | [K] |
| `s2_grenzen.py` | Weyl-Obstruktion gegen äquidistantes Register; Abgrenzung von Shors Aufgabe; Ressourcenabschätzung; Windungszahl-Probe | [K] |

## Kernbefunde

**s1:** Periodenfindung liefert korrekt die Faktoren (sieben Semiprimzahlen geprüft).
Die mittlere multiplikative Ordnung wächst mit **Exponent 0,95** in N — praktisch
exakt O(N), nicht polylogarithmisch. Die Behauptung O((log N)³) für das klassische
Verfahren ist damit widerlegt; sie gilt nur für Shors Quantenverfahren.
Alle σ-Nenner sind zusammengesetzt (42 = 2·3·7, 100 = 2²·5², 1000 = 2³·5³,
100000 = 2⁵·5⁵) und können nach dem Bikohärenzbefund keine Resonanzlinien erzeugen.

**s2:** Zwei Grenzen verschiedener Natur werden getrennt.
*Strukturell (Weyl):* Ein kompakter Zustandsraum kann ein unendliches
arithmetisches Spektrum der Dichte T·ln T nicht tragen — der Faktor wächst
unbeschränkt wie ln(T)/2π.
*Ressource (Shor):* Die Faktorisierung einer konkreten Zahl ist endlich; ein
Register mit 2n+3 Qubits reicht. Shor scheitert bei großen N an der Gatterzahl
(n³) und am Fehlerkorrektur-Overhead — **nicht** an der Weyl-Obstruktion.
Die Weyl-Grenze gegen Shor anzuführen wäre eine Überdehnung.

**s3:** Der thermische Vorteil optischer Verfahren folgt aus hν/(k_BT):
bei 600 nm und 300 K ist die Besetzung 1,8·10⁻³⁵, bei 5 GHz dagegen 1250 —
supraleitende Systeme brauchen T < 52 mK, optische nichts. Er betrifft
Infrastruktur, nicht Rechenmächtigkeit. Die exponentielle Dimension kommt aus
der Tensorproduktstruktur, nicht aus dem Medium (ein Photon in n Moden: Dimension
n wie eine klassische Welle; 25 Photonen in 50 Moden: 3,5·10¹⁹). Verschränkung
allein trägt den Rechenvorteil nicht — Gottesman-Knill zeigt maximal
verschränkte Clifford-Schaltkreise als klassisch simulierbar. Der eigentliche
Träger ist offen.

## Ausführen

    python3 s1_periodensuche.py
    python3 s2_grenzen.py
    python3 s3_thermik_zustandsraum.py
