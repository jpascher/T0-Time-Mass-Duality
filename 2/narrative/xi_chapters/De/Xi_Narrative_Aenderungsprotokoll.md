# Änderungsprotokoll: Xi-Narrative Kapitel

## Durchgeführte Korrekturen

### 1. K_frak einheitlich (in v absorbiert)
- **Kap 01:** `\Kfrak = 0.986` als separate Gleichung entfernt → erklärt als "in v=246 GeV absorbiert"
- **Kap 06:** G_SI-Formel ohne `\Kfrak`, mit Remark zur historischen Erklärung
- **Kap 07:** G_SI-Formel ohne `\Kfrak`, K_frak-Herleitung beibehalten als historische Note, Remark zur numerischen Präzision

### 2. Geometrische α-Herleitung ergänzt (Kap 02)
- Remark eingefügt: α⁻¹ = π⁴·√2 = 137.757 (geometrischer Idealwert aus Ref 149)
- Erklärt: 0.5% Differenz durch pentagonale Symmetriebrechung
- Verbindung zum E₀-basierten Weg hergestellt

### 3. f-basierte Massenformeln ergänzt (Kap 02)
- Remark mit SET A (Ref 149): m_e = v/(f·(2π³+3))·1000 etc.
- Erklärt: Komplementäre Darstellung zum (r,p)-Formalismus
- Genauigkeitsvergleich: 1-4% für beide Sets

### 4. G-Formel Brücke erklärt (Kap 06, 07)
- Remark in Kap 06 und 07: G = ξ/2 (Torsionskristall) ↔ G = ξ²/(4m_e)
- Erklärt: Verschiedene Referenzmassen (ξ/2 vs m_e) in verschiedenen Einheitensystemen
- Beide führen zum identischen SI-Wert

### 5. Kap 09 erweitert (73 → 145 Zeilen)
- ξ_eff = ξ/2 für kosmologische Skalen eingeführt (konsistent mit Ref 201)
- H₀-Diskrepanz erklärt (Remark mit Verweis auf Vakuumdynamik)
- Kosmologische Vakuumdichte ρ₀^cosmo = 4/ξ² ergänzt
- CMB als Vakuumfeld-Gleichgewicht erklärt
- Statisches Universum: definitiv formuliert (konsistent mit Ref 201)

### 6. Kap 06/07 Überschneidung gelöst
- Kap 06: Verweis auf Kap 07 für ausführliche G-Herleitung

### 7. T(x) → T(x,t) (Kap 01)
- Konsistent mit Ref 201 (DVFT): raumzeitabhängig

### 8. ξ = 4/30000 und Torsionskristall-Konzepte
- Kap 01: Remark zu ξ = 4/30000, f = 7500, ξ·f = 1
- Kap 02: Geometrische α-Herleitung referenziert Torsionsgitter

### 9. LaTeX-Korrekturen
- Kap 01: "Kapitel 1:" aus \chapter-Titel entfernt
- Kap 16: `\sloppy` entfernt (Preamble hat bereits `\emergencystretch`)
- Kap 17: Windows-Zeilenenden konvertiert
- Alle: Restliche `\r` bereinigt

## Nicht geändert (kein Handlungsbedarf oder Autor-Entscheidung)
- **Kap 10:** Bleibt auskommentiert im Master (29 Zeilen Platzhalter)
- **Kap 02a:** K_frak-Sektion beibehalten (erklärt den historischen Übergang)
- **Kap 15:** section* beibehalten (Literaturverzeichnis typischerweise unnummeriert)
