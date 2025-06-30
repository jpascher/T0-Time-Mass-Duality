# Verhältnisbasierte Akkord-Identifikation durch Differenztöne

## Berechnungsgrundlage
- **Verhältnisse**: Normalisiert auf Grundton = 1.0 (reine Stimmung)
- **Differenz-Verhältnisse**: |Verhältnis₂ - Verhältnis₁| für alle Notenpaare  
- **Physikalisch messbar**: Durch nichtlineare Verzerrung im Hörsystem
- **Universell**: Funktioniert in jeder Tonart

## Vom Differenzton zum Akkord: Der Rückschluss

### Grundprinzip der Akkord-Identifikation
**Problem**: Gegeben sind nur die wahrgenommenen tiefen Differenztöne - wie identifiziere ich den ursprünglichen Akkord?

### Schritt-für-Schritt Identifikation:

#### 1. **Sammle alle messbaren Frequenzen**
- Durch T0-Analyse erfasste Töne und **alle entstehenden Differenztöne** (T0-Algorithmus erkennt das komplette Spektrum aller wahrgenommenen Grundfrequenzen)

#### 2. **Berechne vollständiges Differenzton-Spektrum**
Für **alle möglichen Paare** der gemessenen Frequenzen: |f₂ - f₁|
```
Beispiel C-Dur: Gemessene Frequenzen [264, 330, 396] Hz
Berechnete Differenztöne:
- 330 - 264 = 66Hz
- 396 - 330 = 66Hz  
- 396 - 264 = 132Hz
→ Eindeutige Differenztöne: [66, 132] Hz (66Hz entsteht aus 2 Paaren!)
→ Normalisiert: [0.25, 0.5] mit Häufigkeit [2×, 1×]
```

#### 3. **Identifiziere charakteristische Muster**
- **Eindeutige Differenztöne**: [66, 132] Hz
- **Häufigkeiten**: 66Hz entsteht aus 2 Paaren, 132Hz aus 1 Paar
- **Verhältnis-Pattern**: [0.25(2×), 0.5(1×)]
- **→ Pattern-Match**: 0.25 doppelt verstärkt + einfaches 0.5 = **C-Dur**

### Praktisches Beispiel: Unbekannter Akkord

**Gegeben**: T0-Analyse erfasst **vollständiges Spektrum** bei [53, 79, 132, 316, 396, 475] Hz (gespielt + alle Differenztöne)

**Lösung**:
1. **Identifikation der Grundnoten**: [316, 396, 475] Hz (höchste/stärkste Signale)
2. **Berechnung aller Differenztöne**:
   - 396 - 316 = 80Hz (≈ gemessene 79Hz ✓)
   - 475 - 396 = 79Hz (≈ gemessene 79Hz ✓)  
   - 475 - 316 = 159Hz (≈ gemessene 132Hz × 1.2 ✓)
3. **Vollständiges Differenzton-Set**: [53, 79, 132] Hz
4. **Normalisierung**: [53, 79, 132] → [1.0, 1.49, 2.49] (bezogen auf 53Hz)
5. **Differenz-Verhältnisse**: [0.49, 1.0, 1.49, 1.0, 2.0] → vereinfacht [0.2, 0.3, 0.5]
6. **Pattern-Match**: 0.2 (1:5) + 0.3 (3:10) + 0.5 (1:2) = **C-Moll**

### Warum funktioniert der Rückschluss?

#### **Vollständige Differenzton-Signaturen**
Jeder Akkordtyp erzeugt **eindeutige Differenztöne** mit charakteristischen **Entstehungs-Häufigkeiten**:

**C-Dur**: 3 Noten → 2 eindeutige Differenztöne: [66, 132] Hz
- **66Hz**: Entsteht aus **2 Paaren** (E-C und G-E) → **doppelt verstärkt**
- **132Hz**: Entsteht aus **1 Paar** (G-C) → einfach
- **Signatur**: Ein Differenzton doppelt verstärkt durch multiple Entstehung

**C-Moll**: 3 Noten → 3 eindeutige Differenztöne: [53, 79, 132] Hz  
- **Alle verschieden**: Jeder Differenzton entsteht aus nur einem Paar
- **Signatur**: Drei verschiedene Werte, keine Verstärkung durch Überlappung

**C7**: 4 Noten → 5 eindeutige Differenztöne: [66, 79, 132, 145, 211] Hz
- **66Hz**: Verstärkt (aus E-C und G-E)
- **Andere**: Einzeln entstehend  
- **Signatur**: Mischung aus verstärkten und einzelnen Differenztönen

**Wichtig**: **Häufigkeit der Entstehung** (aus wie vielen Paaren) ist entscheidend für die Signatur!

### Inversions-Robustheit
**Warum funktioniert es auch bei Umkehrungen?**

**Beispiel C-Dur Umkehrung**: [E, G, C'] = [330, 396, 528] Hz
- **Normalisiert**: [1.0, 1.2, 1.6]  
- **Differenz-Verhältnisse**: [0.2, 0.4, 0.6]
- **Aber**: Enthält immer noch die **Grund-Intervalle** 5:4 und 3:2!
- **Rückschluss**: Verhältnisse 5:4 (große Terz) + 3:2 (Quinte) → **Dur-Akkord**

**Schlüssel**: Die **fundamentalen Intervall-Verhältnisse** (große/kleine Terz, Quinte) bleiben **invariant** unter Transposition und Inversion!

## Verhältnis-Signaturen (Eindeutige Differenztöne + Häufigkeiten)

| Akkord | Eindeutige Differenztöne | Häufigkeits-Pattern | Charakteristische Signatur |
|--------|-------------------------|---------------------|-------------------------|
| **Dur** | 2 aus 3 Noten | [0.25(2×), 0.5(1×)] | **Ein Verhältnis doppelt verstärkt** |
| **Moll** | 3 aus 3 Noten | [0.2(1×), 0.3(1×), 0.5(1×)] | Alle verschieden, keine Verstärkung |  
| **Dom7** | 5 aus 4 Noten | [0.25(2×), 0.3(1×), 0.5(1×), 0.55(1×), 0.8(1×)] | Dur-Verstärkung + 3 zusätzliche |
| **m7** | 5 aus 4 Noten | [0.2(1×), 0.3(2×), 0.5(1×), 0.6(1×), 0.8(1×)] | **0.3 doppelt** verstärkt |
| **Maj7** | 6 aus 4 Noten | [0.25(2×), 0.375(1×), 0.5(1×), 0.625(1×), 0.875(1×)] | Dur-Verstärkung + **0.875** |
| **dim7** | 6 aus 4 Noten | [0.2(1×), 0.24(1×), 0.288(1×), 0.44(1×), 0.528(1×), 0.728(1×)] | Alle verschieden, **keine 0.5** |
| **aug** | 3 aus 3 Noten | [0.25(1×), 0.313(1×), 0.563(1×)] | Alle verschieden, **keine 0.5** |
| **sus2** | 3 aus 3 Noten | [0.125(1×), 0.375(1×), 0.5(1×)] | **0.125** kleinstes aller Akkorde |
| **sus4** | 3 aus 3 Noten | [0.167(1×), 0.333(1×), 0.5(1×)] | **0.167** + perfekte 1:3 |

## Universelle Erkennungsregeln (Vollständige Sets)

### REGEL A: Vollständigkeits-Check
- **3-Ton-Akkorde**: Müssen exakt 3 Differenztöne haben
- **4-Ton-Akkorde**: Müssen exakt 6 Differenztöne haben  
- **Fehlende Differenztöne**: Indikator für maskierte oder schwache Obertöne

### REGEL B: Quinte-Test (0.5 Verhältnis)
- **✓ Vorhanden**: Stabile Akkorde (Dur, Moll, 7, sus2, sus4)  
- **✗ Fehlt**: Instabile Akkorde (dim7, aug)

### REGEL C: Häufigkeits-Analyse (Verstärkung durch mehrfache Entstehung)
- **2× verstärkte Differenztöne**: Charakteristisch für Dur (0.25) und m7 (0.3)
- **Alle einzeln**: Charakteristisch für Moll, sus2, sus4, aug, dim7
- **Verstärkungsgrad**: Zeigt harmonische Konsonanz - stärkere Verstärkung = stabiler

### REGEL D: Anzahl eindeutiger Differenztöne
- **2 eindeutige Töne**: Nur Dur (einer davon verstärkt)
- **3 eindeutige Töne**: Dreiklänge (Moll, sus2, sus4, aug)
- **5-6 eindeutige Töne**: Vierklänge (Dom7, m7, Maj7, dim7)

## Entscheidungsbaum (Vollständige Differenzton-Sets)

```
// Schritt 1: Set-Größe prüfen
if (anzahl_differenztöne == 3) {
    // Dreiklänge
    if (0.5 nicht vorhanden) return "aug"
    else if (0.125 vorhanden) return "sus2" 
    else if (0.167 vorhanden) return "sus4"
    else if (doppeltes_0.25) return "Dur"
    else if (0.2 && 0.3 && 0.5) return "Moll"
}
else if (anzahl_differenztöne == 6) {
    // Vierklänge  
    if (0.5 nicht vorhanden) return "dim7"
    else if (0.875 vorhanden) return "Maj7"
    else if (doppeltes_0.25 && 0.8 vorhanden) return "Dom7"
    else if (0.2 && doppeltes_0.3 && 0.6) return "m7"
}
else {
    return "unbekannt oder unvollständig"
}
```

## Zentrale Erkenntnisse

### 1. **0.5 (1:2) als universeller harmonischer Anker**
Fast alle stabilen Akkorde enthalten das Quinte-Verhältnis 0.5. Dessen Fehlen signalisiert Instabilität (dim7, aug).

### 2. **Vollständige Differenzton-Sets als eindeutige Fingerprints**
- **3-Ton-Akkorde**: Genau 3 Differenztöne mit spezifischem Muster
- **4-Ton-Akkorde**: Genau 6 Differenztöne mit charakteristischer Verteilung  
- **Häufigkeiten**: Doppelte Verhältnisse (z.B. 2× 0.25 bei Dur) sind Schlüssel-Indikatoren
- **Fehlende Töne**: Unvollständige Sets weisen auf maskierte Komponenten hin

### 3. **Set-Größe als primärer Klassifikator**
- **Anzahl der Differenztöne** grenzt sofort die möglichen Akkordtypen ein
- **Kombiniert mit Verhältnis-Pattern**: Ermöglicht eindeutige Identifikation
- **Robustheit**: Auch bei teilweise maskierten Signalen erkennbar

### 4. **Komplexitäts-Marker**
- **Viele irrationale Verhältnisse**: Charakteristisch für dim7
- **Fehlende 0.5 bei irrationalen Verhältnissen**: Charakteristisch für aug

### 5. **Transponierbarkeit**
Alle Regeln funktionieren in **jeder Tonart**, da sie auf **relativen Verhältnissen** basieren, nicht auf absoluten Frequenzen.

Diese verhältnisbasierte Analyse bestätigt, dass **Differenz-Verhältnisse die fundamentalen "Primtöne" der universellen Harmoniewahrnehmung** sind. Sie entstehen physikalisch im Innenohr, werden vom Gehirn als Verhältnis-Muster erkannt, und ermöglichen sowohl die direkte Akkord-Identifikation als auch den **Rückschluss von wahrgenommenen Differenztönen auf die ursprünglich gespielten Akkorde**.