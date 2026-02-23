# copy_wrappers.ps1
# Kopiert alle Wrapper-Dateien, die zu den geänderten _ch-Dateien gehören,
# in das Verzeichnis .\wp
#
# Verwendung: Im Verzeichnis ausfuehren, das die Wrapper-Dateien enthält
#             (also das tex-Verzeichnis, NICHT das ch-Verzeichnis)
#
# Struktur:   .\018_T0_Anomale-g2-12_De.tex      (Wrapper)
#             .\ch\018_T0_Anomale-g2-12_De_ch.tex (Content)

$ErrorActionPreference = "Stop"

# Zielverzeichnis
$wpDir = ".\wp"
if (-not (Test-Path $wpDir)) {
    New-Item -ItemType Directory -Path $wpDir | Out-Null
    Write-Host "Verzeichnis $wpDir erstellt." -ForegroundColor Green
}

# Liste der geaenderten ch-Dateien (ohne _ch.tex Suffix = Wrapper-Name)
$changedFiles = @(
    "000_Einleitung_Teil1_De"
    "003_T0_Grundlagen_v1_En"
    "006_T0_Teilchenmassen_De"
    "006_T0_Teilchenmassen_En"
    "008_T0_xi-und-e_De"
    "008_T0_xi-und-e_En"
    "011_T0_Feinstruktur_En"
    "012_T0_Gravitationskonstante_De"
    "012_T0_Gravitationskonstante_En"
    "018_T0_Anomale-g2-10_De"
    "018_T0_Anomale-g2-10_En"
    "018_T0_Anomale-g2-11_De"
    "018_T0_Anomale-g2-11_En"
    "018_T0_Anomale-g2-12_De"
    "018_T0_Anomale-g2-12_En"
    "025_T0_Kosmologie_En"
    "026_T0_Geometrische_Kosmologie_De"
    "026_T0_Geometrische_Kosmologie_En"
    "030_T0_penrose_De"
    "030_T0_penrose_En"
    "033_T0-Theory-vs-Synergetics_De"
    "033_T0-Theory-vs-Synergetics_En"
    "038_Markov_De"
    "038_Markov_En"
    "041_parameterherleitung_De"
    "041_parameterherleitung_En"
    "049_LagrandianVergleich_De"
    "060_Musik_T0_Parallelen_De"
    "060_Musik_T0_Parallelen_En"
    "070_Mathematische_struktur_De"
    "070_Mathematische_struktur_En"
    "073_QM-testen_De"
    "073_QM-testen_En"
    "086_T0_Dokumentenuebersicht_De"
    "086_T0_Dokumentenuebersicht_En"
    "089_Amper_Low_De"
    "089_Amper_Low_En"
    "124_Unit_Charge_En"
    "131_scheinbar_instantan_De"
    "131_scheinbar_instantan_En"
    "133_Fraktale_Korrektur_Herleitung_De"
    "133_Fraktale_Korrektur_Herleitung_En"
    "137_De"
    "137_En"
    "141_Renormierung_De"
    "141_Renormierung_En"
    "146_turing_De"
    "150_kompatiblitaet_En"
    "157_Zeitpfeil_De"
    "157_Zeitpfeil_En"
    "158_T0_Koide-zu-g2-1_De"
    "158_T0_Koide-zu-g2-1_En"
    "159_T0_Harmonische-Struktur-Torus-1_De"
    "159_T0_Harmonische-Struktur-Torus-1_En"
    "160_T0_Lepton-Lebensdauer-Verh_De"
    "160_T0_Lepton-Lebensdauer-Verh_En"
    "1_T0_Introduction_En"
)

$copied = 0
$missing = 0

foreach ($name in $changedFiles) {
    $wrapper = ".\$name.tex"
    if (Test-Path $wrapper) {
        Copy-Item $wrapper -Destination $wpDir
        Write-Host "  OK  $name.tex" -ForegroundColor Green
        $copied++
    } else {
        Write-Host "  --  $name.tex nicht gefunden" -ForegroundColor Yellow
        $missing++
    }
}

Write-Host ""
Write-Host "Fertig: $copied kopiert, $missing nicht gefunden." -ForegroundColor Cyan
Write-Host "Wrapper-Dateien liegen in: $wpDir" -ForegroundColor Cyan
