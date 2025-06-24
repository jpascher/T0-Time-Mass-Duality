import os
import re

# Verzeichnisse definieren
target_dir_de = "tex\\Deutsch"
target_dir_en = "tex\\English"

# Dictionary mit den Zuordnungen: alter Name (mit .tex) -> neuer Name (ohne Endung)
name_mapping = {
    "Analyse der Messdifferenzen zwischen dem T0-Modell und dem Standardmodell.tex": "MessdifferenzenT0Standard",
    "Analyse der Messdifferenzen zwischen dem T0-Modell und dem Standardmodell_en.tex": "MessdifferenzenT0StandardEn",
    "Anpassung von Temperatureinheiten in natürlichen Einheiten und CMB-Messungen.tex": "TempEinheitenCMB",
    "Anpassung von Temperatureinheiten in natuerlichen Einheiten und CMB-Messungen_en.tex": "TempEinheitenCMBEn",
    "Bridging Quantum Mechanics and Relativity through Time-Mass Duality Part I Theoretical Foundations.tex": "QMRelTimeMassPart1",
    "Bridging Quantum Mechanics and Relativity through Time-Mass Duality Part I Theoretical Foundations_en.tex": "QMRelTimeMassPart1En",
    "Bridging Quantum Mechanics and Relativity through Time-Mass Duality Part I Theoretical Foundations__z_en.tex": "QMRelTimeMassPart1ZEn",
    "Bridging Quantum Mechanics and Relativity through Time-Mass Duality Part II Theoretical Foundations.tex": "QMRelTimeMassPart2",
    "Bridging Quantum Mechanics and Relativity through Time-Mass Duality Part II Theoretical Foundations_en.tex": "QMRelTimeMassPart2CosmoEn",
    "Bridging Quantum Mechanics and Relativity through Time-Mass Duality Part II Theoretical Foundations__z_en.tex": "QMRelTimeMassPart2ZEn",
    "Die Konsistenz von alpha = 1 und beta = 1.tex": "Alpha1Beta1Konsistenz",
    "Die Konsistenz von alpha = 1 und beta = 1_en.tex": "Alpha1Beta1KonsistenzEn",
    "Die Notwendigkeit einer Erweiterung der Standard-Quantenmechanik und Quantenfeldtheorie.tex": "NotwendigkeitQMErweiterung",
    "Die Notwendigkeit einer Erweiterung der Standard-Quantenmechanik und Quantenfeldtheorie_en.tex": "NotwendigkeitQMErweiterungEn",
    "Dynamische Masse von Photonen und ihre Implikationen für Nichtlokalitaet.tex": "DynMassePhotonenNichtlokal",
    "Dynamische Masse von Photonen und ihre Implikationen für Nichtlokalitaet_en.tex": "DynMassePhotonenNichtlokalEn",
    "Eine mathematische Analyse der Energiedynamik.tex": "MathEnergiedynamik",
    "Eine mathematische Analyse der Energiedynamik_en.tex": "MathEnergiedynamikEn",
    "Eine neue Perspektive auf Zeit und Raum Johann Paschers revolutionaere Ideen.tex": "ZeitRaumPascher",
    "Eine neue Perspektive auf Zeit und Raum Johann Paschers revolutionaere Ideen_en.tex": "ZeitRaumPascherEn",
    "Emergente Gravitation im T0-Modell Eine formale Herleitung.tex": "EmergentGravT0",
    "Emergente Gravitation im T0-Modell Eine formale Herleitung_en.tex": "EmergentGravT0En",
    "Feldtheorie und Quantenkorrelationen.tex": "FeldtheorieQuanten",
    "Feldtheorie und Quantenkorrelationen_en.tex": "FeldtheorieQuantenEn",
    "Jenseits der Planck-Skala.tex": "JenseitsPlanck",
    "Jenseits der Planck-Skala_en.tex": "JenseitsPlanckEn",
    "Kurzgefasst - Komplementärer Dualismus in der Physik - Von Welle-Teilchen zum Zeit-Masse-Konzept.tex": "KurzKomplementDualPhysik",
    "Kurzgefasst - Komplementärer Dualismus in der Physik - Von Welle-Teilchen zum Zeit-Masse-Konzept_en.tex": "KurzKomplementDualPhysikEn",
    "Massenvariation in Galaxien.tex": "MassVarGalaxien",
    "Massenvariation in Galaxien_en.tex": "MassVarGalaxienEn",
    "Mathematische Formulierung des Higgs-Mechanismus in der Zeit-Masse-Dualitaet.tex": "MathHiggsZeitMasse",
    "Mathematische Formulierung des Higgs-Mechanismus in der Zeit-Masse-Dualitaet_en.tex": "MathHiggsZeitMasseEn",
    "Mathematische Formulierungen der Zeit-Masse-Dualitaetstheorie mit Lagrange.tex": "MathZeitMasseLagrange",
    "Mathematische Formulierungen der Zeit-Masse-Dualitaetstheorie mit Lagrange_en.tex": "MathZeitMasseLagrangeEn",
    "Natürliche Einheiten mit Feinstrukturkonstante alpha = 1.tex": "NatEinheitenAlpha1",
    "Natürliche Einheiten mit Feinstrukturkonstante alpha = 1_en.tex": "NatEinheitenAlpha1En",
    "Quantenfeldtheoretische Behandlung des intrinsischen Zeitfelds im T0-Modell.tex": "QFTIntrinsischesZeitT0",
    "Quantenfeldtheoretische Behandlung des intrinsischen Zeitfelds im T0-Modell_en.tex": "QFTIntrinsischesZeitT0En",
    "Vereinfachte Beschreibung der vier Grundkraefte mit Zeit-Masse-Dualitaet.tex": "VierKraefteZeitMasse",
    "Vereinfachte Beschreibung der vier Grundkraefte mit Zeit-Masse-Dualitaet_en.tex": "VierKraefteZeitMasseEn",
    "Vereinheitlichung des T0-Modells Grundlagen - Dunkle Energie und Galaxiendynamik.tex": "T0VereinheitlichungDEGal",
    "Vereinheitlichung des T0-Modells Grundlagen - Dunkle Energie und Galaxiendynamik_en.tex": "T0VereinheitlichungDEGalEn",
    "Wesentliche mathematische Formalismen der Zeit-Masse-Dualitaetstheorie mit Lagrange-Dichten.tex": "MathZeitMasseLagrangeDicht",
    "Wesentliche mathematische Formalismen der Zeit-Masse-Dualitaetstheorie mit Lagrange-Dichten_en.tex": "MathZeitMasseLagrangeDichtEn",
    "Zeit als emergente Eigenschaft in der Quantenmechanik.tex": "ZeitEmergentQM",
    "Zeit als emergente Eigenschaft in der Quantenmechanik_en.tex": "ZeitEmergentQMEn",
    "Zeit und Masse Ein neuer Blick auf alte Formeln – und die Befreiung von traditionellen Fesseln.tex": "ZeitMasseNeuerBlick",
    "Zeit und Masse Ein neuer Blick auf alte Formeln – und die Befreiung von traditionellen Fesseln_en.tex": "ZeitMasseNeuerBlickEn",
    "Zeit-Masse-Dualitaetstheorie (T0-Modell) Herleitung der Parameter kappa, alpha und beta.tex": "ZeitMasseT0Params",
    "Zeit-Masse-Dualitaetstheorie (T0-Modell) Herleitung der Parameter kappa, alpha und beta_en.tex": "ZeitMasseT0ParamsEn",
    "Zusammenfassung - Fundamentale Konstanten.tex": "ZusammenfassungKonstanten",
    "Zusammenfassung - Fundamentale Konstanten_en.tex": "ZusammenfassungKonstantenEn"
}

# Liste für Änderungen
changes = []

# Funktion zum Ersetzen der URLs
def replace_urls(file_path, mapping):
    print(f"Verarbeite Datei: {file_path}")
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
    except Exception as e:
        print(f"Fehler beim Öffnen der Datei {file_path}: {e}")
        return

    updated = False
    for old_name, new_name in mapping.items():
        # Sprache bestimmen
        lang_dir = "English" if old_name.endswith("_en.tex") else "Deutsch"
        
        # Alte URL mit verschiedenen Kodierungen
        old_name_pdf = old_name.replace(".tex", ".pdf")
        old_url_variants = [
            f"https://github.com/jpascher/T0-Time-Mass-Duality/tree/main/2/pdf/{lang_dir}/{old_name_pdf.replace(' ', '%20')}",
            f"https://github.com/jpascher/T0-Time-Mass-Duality/tree/main/2/pdf/{lang_dir}/{old_name_pdf.replace(' ', '\\%20')}",
            f"https://github.com/jpascher/T0-Time-Mass-Duality/tree/main/2/pdf/{lang_dir}/{old_name_pdf.replace(' ', '%20').replace('ä', '%C3%A4').replace('ö', '%C3%B6').replace('ü', '%C3%BC')}",
            f"https://github.com/jpascher/T0-Time-Mass-Duality/tree/main/2/pdf/{lang_dir}/{old_name_pdf.replace(' ', '%20').replace('ä', 'ae').replace('ö', 'oe').replace('ü', 'ue')}",
            f"https://github.com/jpascher/T0-Time-Mass-Duality/tree/main/2/pdf/{lang_dir}/{old_name_pdf}"
        ]
        
        # Neue URL
        new_url = f"https://github.com/jpascher/T0-Time-Mass-Duality/tree/main/2/pdf/{lang_dir}/{new_name}.pdf"
        
        # URLs ersetzen
        for old_url in old_url_variants:
            if old_url in content:
                content = content.replace(old_url, new_url)
                changes.append(f"In {file_path}: '{old_url}' -> '{new_url}'")
                updated = True

    # Datei überschreiben, wenn Änderungen vorgenommen wurden
    if updated:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"URLs in {file_path} aktualisiert.")
    else:
        print(f"Keine Änderungen in {file_path} erforderlich.")

# URLs in allen .tex-Dateien aktualisieren
print("Starte Aktualisierung der URLs...")
for target_dir in [target_dir_de, target_dir_en]:
    if not os.path.exists(target_dir):
        print(f"Verzeichnis {target_dir} existiert nicht.")
        continue
    for filename in os.listdir(target_dir):
        if filename.endswith(".tex"):
            file_path = os.path.join(target_dir, filename)
            replace_urls(file_path, name_mapping)

# Änderungen ausgeben
print("\nListe der vorgenommenen Änderungen:")
if changes:
    for change in changes:
        print(change)
else:
    print("Keine Änderungen vorgenommen.")

print("\nFertig!")