#!/bin/bash
# ============================================================
# T0 LaTeX Translation Script - German to English
# Verwendet Microsoft Azure Translator API
# ============================================================

# === KONFIGURATION ===
KEY="5OfPzHviDzSPW4inYDJ3uokfadGiGTo1hQustQAnopshEU1zRW0mJQQJ99BLAC5RqLJXJ3w3AAAbACOGl4nH"
ENDPOINT="https://api.cognitive.microsofttranslator.com"
REGION="global"

# Wechsle ins Verzeichnis mit den LaTeX-Dateien
cd "$(dirname "$0")"

echo "============================================================"
echo "T0 LaTeX Übersetzung: Deutsch -> Englisch"
echo "============================================================"
echo ""

# Zähler
count=0
success=0
failed=0

# Erstelle Ausgabeverzeichnis
mkdir -p translated

# Durchlaufe alle deutschen LaTeX-Dateien
for f in *_De.tex; do
    [ -f "$f" ] || continue
    
    ((count++))
    basename="${f%_De.tex}"
    
    echo "[$count] Übersetze: $f"
    
    # 1. Text extrahieren mit pandoc (LaTeX -> Plain Text)
    TEXT=$(pandoc "$f" -t plain 2>/dev/null)
    
    if [ -z "$TEXT" ]; then
        echo "    FEHLER: Konnte Text nicht extrahieren"
        ((failed++))
        continue
    fi
    
    # 2. Text für JSON escapen
    TEXT_ESCAPED=$(echo "$TEXT" | jq -Rs '.')
    
    # 3. API-Aufruf mit curl
    RESPONSE=$(curl -s -X POST "$ENDPOINT/translate?api-version=3.0&from=de&to=en" \
        -H "Ocp-Apim-Subscription-Key: $KEY" \
        -H "Ocp-Apim-Subscription-Region: $REGION" \
        -H "Content-Type: application/json; charset=UTF-8" \
        -d "[{\"Text\":$TEXT_ESCAPED}]")
    
    # 4. Übersetzung extrahieren
    TRANSLATED=$(echo "$RESPONSE" | jq -r '.[0].translations[0].text' 2>/dev/null)
    
    if [ "$TRANSLATED" = "null" ] || [ -z "$TRANSLATED" ]; then
        echo "    FEHLER: Übersetzung fehlgeschlagen"
        echo "    Response: $RESPONSE"
        ((failed++))
        continue
    fi
    
    # 5. Speichern
    echo "$TRANSLATED" > "translated/${basename}_En_translated.txt"
    echo "    OK: translated/${basename}_En_translated.txt"
    ((success++))
    
    # Kurze Pause um API-Limits zu respektieren
    sleep 0.5
done

echo ""
echo "============================================================"
echo "Fertig!"
echo "Gesamt: $count Dateien"
echo "Erfolgreich: $success"
echo "Fehlgeschlagen: $failed"
echo ""
echo "Übersetzte Texte in: translated/"
echo "============================================================"
