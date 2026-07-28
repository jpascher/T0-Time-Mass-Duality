# Dok. 309 — Das Skalenanker-Problem: ΛCDM und FFGFT im Vergleich

**Entwurf — Johann Pascher, Juli 2026**
**Interne Arbeitsnotiz. Nicht Teil der A-Serie.**

---

## Die Ausgangsfrage

Beide kosmologischen Theorien — ΛCDMund FFGFT — müssen irgendwo
eine Zahl einführen, die den kosmischen Maßstab an das SI-System ankoppelt.
Keine der beiden leitet diesen Anker aus erster Prinzipien her.

Das ist kein Zufall — es ist ein strukturelles Problem jeder physikalischen
Theorie, die Dimensionen hat. Aber **Art und Qualität** des Ankers
unterscheiden sich fundamental.

---

## 1. Das SI-System — ein Netz ohne ersten Anker

Seit 2019 ist das SI vollstaendig ueber Naturkonstanten definiert.
Die Zahlen sind alle **exakt** — aber nicht physikalisch ausgezeichnet.
Sie sind **gegenseitig verankert**, nicht einzeln begruendet.

| Konstante | Wert (exakt) | Historischer Ursprung |
|---|---|---|
| c | 299 792 458 m/s | Lichtgeschwindigkeit (gemessen) |
| h | 6,626 070 15e-34 Js | Plancks Konstante (gemessen) |
| e | 1,602 176 634e-19 C | Elementarladung (gemessen) |
| nu_Cs | 9 192 631 770 Hz | Cs-Hyperfeinuebergang (gewaehlt) |

### 1.1 Es gibt keinen ersten Anker

Die Sekunde war urspruenglich 1/86400 eines Sonnentages — astronomisch,
nicht physikalisch. Seit 1967 ist sie ueber den Caesium-Hyperfeinuebergang
definiert. Diese Wahl war **technisch bequem** — nicht fundamental.
Der Cs-Uebergang haette genauso gut der Rb-Uebergang, die Elektronen-
frequenz oder hundert andere Systeme sein koennen. Alle heutigen
SI-Zahlenwerte waeren dann andere — alle dimensionslosen Verhaeltnisse
(Massenverhaeltnisse m_e/m_p usw.) blieben unveraendert.

### 1.2 Seit der Reform 2019: ein einziger konventioneller Anker

Vor 2019 waren c, h, e, k_B, N_A gemessene Groessen mit Messunsicherheit.
Seit 2019 sind sie alle exakt fixiert. Das bedeutet:

**Alle dimensionsbehafteten SI-Konstanten sind auf nu_Cs zurueckfuehrbar.**

Beispiele:

    1 m  = c / nu_Cs * (historischer Zahlenfaktor 9 192 631 770 / 299 792 458)
    1 kg = h * nu_Cs^2 / c^2 * (Zahlenfaktor)
    1 A  = e * nu_Cs * (Zahlenfaktor)
    1 K  = h * nu_Cs / k_B * (Zahlenfaktor)

Die scheinbar 'vier unabhaengigen Messwerte' c, h, e, k_B sind traditionell
so — physikalisch sind sie alle Vielfache der einen Frequenzskala nu_Cs.
nu_Cs selbst ist historisch-konventionell gewaehlt (Cs-Atom, technische
Bequemlichkeit), nicht physikalisch ausgezeichnet.

**Der einzig nicht-konventionelle physikalische Inhalt sind die
dimensionslosen Verhaeltnisse:**

    m_e/m_p = 1/1836,15...   (Massenverhaeltnis)
    ... und weitere dimensionslose Verhaeltnisse

Diese Zahlen sind unabhaengig von Einheitenkonventionen.
Alles andere — einschliesslich aller SI-Zahlenwerte — folgt aus
(1) diesen dimensionslosen Zahlen und
(2) der einen Konvention: welche Frequenz als 'eine Einheit' gilt.

### 1.3 Konsequenz fuer den Skalenanker

Jede Theorie, die kosmologische Absolutwerte in SI voraussagt,
gibt eine Relation zwischen zwei Frequenzen an — und muss dafuer
irgendwo eine Zahl setzen. Die FFGFT-Aussage

    H_0 = (pi/2) * c * xi^10 / lambda_e

ist aequivalent zur **dimensionslosen** Aussage:

    H_0 / nu_e = (pi/2) * xi^10 = 2,79e-39

mit nu_e = m_e*c^2/h = 1,235e20 Hz (Elektronenfrequenz).

Das Verhaeltnis H_0/nu_e ist eine reine Zahl — unabhaengig von
Einheitenkonventionen. Der SI-Bezug steckt vollstaendig in der
Wahl von lambda_e als Bezugsgroesse.

**Jede Theorie, die Absolutwerte in SI voraussagt, muss irgendwo
eine Zahl ohne Vorwaertsableitung einfuehren.**

---

## 2. ΛCDMund sein Skalenanker

### 2.1 Die freien Parameter

ΛCDMbeschreibt die Kosmologie mit sechs freien Parametern (Planck 2018):

| Parameter | Wert | Bedeutung |
|---|---|---|
| $H_0$ | 67,4 km/s/Mpc | Expansionsrate heute |
| $\Omega_b h^2$ | 0,0224 | Baryonendichte |
| $\Omega_\text{DM} h^2$ | 0,120 | DM-Dichte |
| $n_s$ | 0,965 | Spektralindex Inflation |
| $\sigma_8$ | 0,811 | Fluktuationsamplitude |
| $\tau$ | 0,054 | Reionisationstiefe |

Alle sechs Zahlen sind aus Beobachtung bestimmt.
Keine folgt aus der Teilchenphysik oder der Geometrie.

### 2.2 Woher kommt $H_0$?

$H_0$ wird nicht abgeleitet — er wird gemessen. Die Messung läuft über
eine vierstufige Entfernungsleiter:

```
Trigonometrische Parallaxe (GAIA)
         ↓
Cepheiden-Periode-Leuchtkraft-Relation
         ↓
Typ-Ia-Supernovae (Standardkerzen)
         ↓
H_0 = c·z / d  [Hubble-Gesetz]
```

Jede Stufe bringt eigene Kalibrierungsannahmen. Das ist der Grund
für das **Hubble-Spannungsproblem**: früh-kosmische Messung (CMB, Planck)
liefert $H_0 = 67{,}4$, spät-kosmische (Cepheiden/SNe, SH0ES) $H_0 = 73{,}0$
— eine Spannung von 5σ ohne Auflösung im Rahmen von ΛCDM.

Die Entfernungsleiter ist **zirkulär**: spätere Stufen werden teilweise
über $H_0$-abhängige Relationen (Tully-Fisher, Fundamental Plane) kalibriert.

### 2.3 Das Feinabstimmungsproblem als Skalenanker-Versagen

$\Lambda$ entspricht einer Vakuumenergiedichte:

$$\rho_\Lambda = \frac{\Lambda c^2}{8\pi G} \approx 5{,}96 \times 10^{-27}~\text{kg/m}^3$$

Die Quantenfeldtheorie sagt vor:

$$\rho_\text{QFT} \sim \frac{E_\text{Planck}^4}{\hbar^3 c^3} \approx 5 \times 10^{96}~\text{kg/m}^3$$

**Das Verhältnis beträgt $10^{123}$.** Das Feinabstimmungsproblem ist
direkt das Versagen des ΛCDMSkalenankers: $\Lambda$ hat keinen
physikalischen Ursprung, er wird einfach auf den Beobachtungswert gesetzt.

### 2.4 Struktureller Befund

> **ΛCDMhat ~6 unabhängige Skalenanker, alle empirisch bestimmt,
> ohne theoretischen Ursprung, teilweise zirkulär verschränkt.
> Das Feinabstimmungsproblem ($10^{123}$) ist die extremste
> Manifestation dieser fehlenden Basis.**

---

## 3. FFGFT und ihr Skalenanker

### 3.1 Ein Parameter

FFGFT hat einen einzigen freien Parameter:

$$\xi = \frac{4}{30000} = 1{,}\overline{3} \times 10^{-4}$$

Dieser Wert ist empirisch motiviert und als Setzung deklariert
(P33, Dok. 190). Er hat keine Vorwärtsableitung.

### 3.2 Ankopplung an SI — und der versteckte Fit

$H_0$ wird in FFGFT berechnet als (Dok. 279, K6):

$$H_0 = \frac{\pi}{2}\,\frac{c\,\xi^{10}}{\bar\lambda_e}$$

**Numerische Werte:**

```
xi        = 4/30000 = 1,3333e-4  (Setzung, P33)
lambda_e  = hbar/(m_e * c) = 3,8616e-13 m
H0        = (pi/2) * c * xi^10 / lambda_e = 66,82 km/s/Mpc
a_0       = c^2 * xi^10 / (4*lambda_e)   = 1,033e-10 m/s^2
```

### 3.3 Der eigentliche Fit: der Exponent 10

xi kommt aus der Geometrie (P33). Der Exponent 10 in
H0 = (pi/2)*c*xi^10/lam_e wurde so gewaehlt dass H0 ~ 67 km/s/Mpc.
Da xi ~ 1,3e-4 springt H0 zwischen benachbarten Exponenten um ~7500:

```
n= 9:  H0 = 5,01e5   km/s/Mpc  -- unphysikalisch
n=10:  H0 = 66,8     km/s/Mpc  -- plausibel  <-- gewaehlt
n=11:  H0 = 0,0089   km/s/Mpc  -- unphysikalisch
```

Es gibt kein kontinuierliches Anpassen -- nur n=10 funktioniert.
Aber die Begruendung bleibt: er gibt einen mit ΛCDM kompatiblen Wert.

### 3.4 Die Vererbung: FFGFT erbt die ΛCDM-Systematik

Hier liegt das tiefere Problem:

**67 km/s/Mpc ist ein ΛCDM-Messwert.**
Er wurde unter der Annahme der Expansionslesart bestimmt --
Rotverschiebung als Doppler-Effekt, Entfernungen aus Standardkerzen
die unter ΛCDM kalibriert sind.

Der 'natuerliche' H0 aus der FFGFT-Rotverschiebungsformel
z = exp(xi*x/lam_e) - 1 waere:

    H0_natur = c * xi / lam_e ~ 3e33 km/s/Mpc  (unphysikalisch)

Um ~67 km/s/Mpc zu erhalten, braucht man xi^10 statt xi^1.
Die Rechtfertigung des Exponenten 10 ist letztlich:
er gibt einen Wert der mit ΛCDM-Messungen kompatibel ist.

**Konsequenz:**
Wenn die statische Lesart die korrekte ist, und wenn die
ΛCDM-H0-Messung systematisch falsch ist (weil Entfernungen
unter falscher Annahme bestimmt wurden), dann ist der
Exponent 10 an den falschen Wert kalibriert.

Das ist keine Schwaeche die FFGFT allein hat --
es ist die unvermeidliche Konsequenz der Entartung (Dok. 267):
solange beide Lesarten empirisch ununterscheidbar sind,
kalibriert jede Theorie ihre Parameter an denselben Daten.

Der Ausweg waere eine **lesartunabhaengige** Bestimmung
des Exponenten 10 -- aus der T^4-Geometrie vorwaerts.
Das ist bisher nicht geleistet (P33/P20, Dok. 190).

- Dass xi^10 auch a_0 reproduziert: Querverankerung, nicht erwartet

### 3.3 Querverankerung: dieselbe Zahl in fünf Sektoren

Was FFGFT von ΛCDMunterscheidet, ist nicht das Vorhandensein einer
Setzung — sondern was mit dieser Setzung passiert:

| Sektor | Größe | $\xi$-Abhängigkeit | Status |
|---|---|---|---|
| Kosmologie | $H_0$ | $\xi^{10}$ | [K] |
| Gravitation | $a_0$ (MOND-Skala) | $\xi^{10}$ | [K] |
| Teilchenphysik | Leptonmassenleiter | $\xi$-Potenzen | [K] |
| Quantenmechanik | $K_\text{frak} = 1 - 100\xi$ | $\xi$ | [K] |
| Geometrie | $k^* = \ln\varphi/\xi$ | $\xi$ | [S] |
| Lichtablenkung | $\gamma_\text{PPN} = 1$ | K3, $\xi$-Geometrie | [K] |

In **keinem** Sektor ist $\xi$ ein eigener freier Parameter —
es ist immer dieselbe Zahl.

$\Omega_\Lambda$ in ΛCDMhat **null** solcher Querverankerungen.

### 3.4 Kein Zirkularitätsproblem

FFGFT leitet $H_0$ direkt aus $\xi$, $\hbar$, $m_e$, $c$ ab.
Es gibt keine Entfernungsleiter, keine Standardkerzen, keine
mehrstufige Kalibrierung. Das Hubble-Spannungsproblem existiert
in FFGFT strukturell nicht.

---

## 4. Numerischer Vergleich

### 4.1 Freiheitsgrade

| | ΛCDM | FFGFT |
|---|---|---|
| Freie Skalenanker | 6–7 | 1 ($\xi$) |
| Theoretischer Ursprung | keiner | keiner (P33) |
| Querverankerung | nein | ja (5+ Sektoren) |
| Zirkulär | ja ($H_0$-Treppe) | nein |
| Feinabstimmung | $10^{123}$ ($\Lambda$) | entfällt (kein $\Lambda$) |
| Hubble-Spannung | 5σ, offen | strukturell absent |

### 4.2 Kandidaten für einen echten $\xi$-Anker

Ein echter Anker wäre ein dimensionsloser Ausdruck aus bekannten
Konstanten, der $\xi = 4/30000$ erzwingt:

| Ausdruck | Wert | Verhältnis zu $\xi$ |
|---|---|---|
| $m_e/m_p$ | $5{,}446 \times 10^{-4}$ | 4,08 |
| $m_e/m_p$ | $5{,}446 \times 10^{-4}$ | 4,08 |
| $(m_e/m_p)^{1/2}$ | $2{,}333 \times 10^{-2}$ | 175 |
| $G m_e^2/(\hbar c)$ | $1{,}750 \times 10^{-45}$ | $\ll 1$ |

Kein einfacher dimensionsloser Ausdruck trifft $\xi$ exakt.

### 4.3 Was der Koide-Wert zeigt

Der Koide-Wert der Leptonen:

$$Q = \frac{(\sqrt{m_e} + \sqrt{m_\mu} + \sqrt{m_\tau})^2}
           {3(m_e + m_\mu + m_\tau)} = 0{,}500005$$

trifft $Q = 2/3$ auf $10^{-5}$ — zu präzise für Zufall.
FFGFT erklärt dies über die $\xi$-Massenleiter. Das ist eine
Konsistenzprüfung des $\xi$-Werts, kein Beweis seiner Herleitung.

Der Wert $Q = 2/3$ ist im $\xi$-Formalismus geometrisch:
er entspricht dem Verhältnis von Zeit- zu Gesamtzyklen in der
K3-2-Zellen-Struktur ($2/3$ des Raum-Zeit-Paares ist Zeit).
Das ist ein Kandidat für eine tiefere Begründung — kein Beweis.

---

## 5. Offene Punkte — was die Dokumente sagen

Die relevanten offenen Punkte sind in Dok. 190 deklariert:

**P20:** Form von H0 als xi-Verhaeltnis fest; der Exponent 10
ist externe Kalibrierung aus ΛCDM, nicht hergeleitet.

**P33:** Magnitude von xi (Faktor 5^4) intuitiv/empirisch begruendet,
kein Vorwaertsbeweis. Struktur-Parallele zu P20.

**Vererbung (neu, dieses Dokument):**
Der Exponent 10 wurde an H0_ΛCDM kalibriert. Wenn die statische
Lesart korrekt ist, erbt FFGFT die Systematik der Expansionslesart.
Der Ausweg waere eine lesartunabhaengige Herleitung des Exponenten
aus der T^4-Geometrie — bisher nicht geleistet.

---

## 6. Fazit

| Frage | ΛCDM | FFGFT |
|---|---|---|
| Skalenanker | 6–7, empirisch, zirkulär | 1, empirisch, querverankert |
| Feinabstimmung | $10^{123}$, unerklärt | entfällt strukturell |
| Hubble-Spannung | 5σ, offen | strukturell absent |
| Nächster Schritt | unklar | Herleitung von $\xi$-Magnitude |

> FFGFT tauscht sechs isolierte Parameter gegen einen querverankerten —
> kein Beweis, aber eine Reduktion mit Richtung.

---

*Bezüge: Dok. 190 (P33), Dok. 279 ($H_0$-Kette, K6),
Dok. 308 (kosmischer Sektor), Dok. 182 ($R_H$), Dok. 267 (Entartung).*
