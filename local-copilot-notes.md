# local-copilot-notes

Kurze Merkhilfe, um den **lokalen GitHub Copilot CLI** zuverlässig zu verwenden – vor allem, wenn "nichts mehr geht".

---
## 1. Grundvoraussetzungen (nur prüfen, wenn Copilot gar nicht mehr startet)

- **Node & npm** (nur wichtig bei npm-Installation):
  - `node -v` → mindestens **v22**
  - `npm -v` → mindestens **v10**
- **Installation prüfen**:
  - `copilot --version` → wenn dieser Befehl einen Fehler liefert, ist Copilot nicht (mehr) installiert.
- **Neuinstallation (Windows, Alternativen)**:
  - Mit WinGet (empfohlen):
    ```powershell
    winget install GitHub.Copilot
    # oder Vorabversion
    winget install GitHub.Copilot.Prerelease
    ```
  - Mit npm:
    ```powershell
    npm install -g @github/copilot
    # oder Vorabversion
    npm install -g @github/copilot@prerelease
    ```

---
## 2. Standard-Start des lokalen Copilot

1. **PowerShell öffnen** (nicht cmd).
2. In das Projektverzeichnis wechseln (immer mit **Backslashes** auf Windows):
   ```powershell
   cd C:\Users\johann\B15
   ```
3. Copilot starten:
   ```powershell
   copilot
   ```
4. Du bist jetzt im interaktiven Copilot-CLI; hier kannst du einfach **auf Deutsch Fragen oder Befehle** tippen.

Nützlich: `/help` zeigt dir jederzeit die wichtigsten Befehle im CLI.

---
## 3. Anmelden / Login-Probleme

Wenn Copilot startet, aber meldet, dass du nicht eingeloggt bist, oder nichts mehr antwortet:

1. Im Copilot-CLI den Befehl ausführen:
   ```
   /login
   ```
   und den Anweisungen im Browser folgen.
2. Falls du mit **Personal Access Token (PAT)** arbeitest:
   - Einen PAT mit Berechtigung **"Copilot Requests"** auf https://github.com/settings/personal-access-tokens/new erstellen.
   - In PowerShell Umgebungsvariable setzen (Beispiel):
     ```powershell
     $env:GH_TOKEN = "DEIN_TOKEN_HIER"
     # oder
     $env:GITHUB_TOKEN = "DEIN_TOKEN_HIER"
     ```
   - Dann `copilot` neu starten und ggf. wieder `/login` ausführen.

---
## 4. Wenn Copilot läuft, aber nicht auf das Projekt zugreifen darf

- Prüfe im Copilot-CLI mit:
  ```
  /cwd
  ```
  ob der aktuelle Ordner tatsächlich `C:\Users\johann\B15` ist.
- Wenn Copilot meldet, dass er nicht in Verzeichnisse schauen darf:
  ```
  /add-dir .
  ```
  (damit erlaubst du den aktuellen Projektordner).
- Mit `/list-dirs` kannst du dir alle erlaubten Verzeichnisse anzeigen lassen.

---
## 5. Wichtige Shortcuts & Befehle im Copilot-CLI

- **Navigation & Basisbefehle**
  - `/help` – Übersicht aller Befehle.
  - `/exit` oder `/quit` – Copilot-CLI beenden.
  - `Ctrl+c` – aktuellen Vorgang abbrechen / Eingabezeile leeren.
  - `Ctrl+d` – Copilot-CLI sauber herunterfahren.
- **Kontext & Modelle**
  - `/model` – anderes Modell auswählen (z.B. Sonnet/GPT).
  - `/cwd <pfad>` – Arbeitsverzeichnis ändern, z.B. `/cwd C:\Users\johann\B15`.
- **Session & Teilen**
  - `/session` – Infos zur aktuellen Sitzung.
  - `/share file local-copilot-notes.md` – diese Notizen als Markdown-Datei exportieren (falls du im Copilot-CLI nicht im B15-Ordner bist).

---
## 6. Projekt-spezifische Hinweise für dieses Repository

- Dieses Repo hat eine Datei **`copilot-instructions.md`** im Root (B15-Verzeichnis),
  die beschreibt, wie Copilot mit den LaTeX-Tabellen/Overflow-Fixes umgehen soll.
- Wenn du nach längerer Zeit nicht mehr weißt, was der Plan war:
  - Einfach in PowerShell ansehen mit
    ```powershell
    type .\copilot-instructions.md
    ```
    oder im Editor öffnen.
- Copilot in dieser Umgebung berücksichtigt diese Datei bereits automatisch, also musst du die Regeln **nicht jedes Mal neu erklären**.

---
## 7. Typische Fehlerszenarien & schnelle Checks

1. **Copilot startet gar nicht ("Befehl nicht gefunden")**
   - `copilot --version` ausprobieren.
   - Falls Fehler → mit WinGet oder npm neu installieren (siehe Abschnitt 1).

2. **Copilot startet, aber kann nicht mit GitHub reden**
   - Internetverbindung prüfen.
   - Ggf. GitHub-Status checken (https://www.githubstatus.com/).
   - Im CLI `/login` noch einmal durchführen.

3. **Copilot reagiert extrem langsam oder gar nicht**
   - CLI einmal schließen (`Ctrl+c` oder `/exit`) und neu starten.
   - Notfalls PowerShell neu öffnen und `copilot` erneut starten.

4. **Du bist im falschen Ordner**
   - In PowerShell: `pwd` (oder `$PWD`) prüfen.
   - Sicherstellen, dass du im **B15-Ordner** bist, dann `copilot` aufrufen.

---
## 8. Mini-Cheatsheet (kurz & knapp)

- PowerShell:
  ```powershell
  cd C:\Users\johann\B15
  copilot
  ```
- Im Copilot-CLI bei Problemen nacheinander versuchen:
  ```
  /cwd
  /login
  /add-dir .
  /help
  ```
- Wenn gar nichts mehr hilft: Copilot neu installieren (WinGet) und danach wieder im B15-Ordner `copilot` starten.
