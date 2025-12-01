<#
.SYNOPSIS
  Generate markdown stubs, originals and mapping YAMLs from .tex sources (PowerShell variant).
.DESCRIPTION
  - Process the explicit list of 11 .tex files for Band1.
  - For each file produce:
      book1/Book1_T0_erklaert_de/chapters/01_<basename>.md
      book1/Book1_T0_erklaert_de/originals/<basename>.tex.raw
      book1/Book1_T0_erklaert_de/mappings/mapping_<basename>.yaml
  - Use the specified -Ref commit SHA (default: ce78d7b93bd940a3b3f12a2c3afd0d1c34d35a41) to build blob URLs.
  - Safe default: dry-run mode. Use -Apply to write files.
.PARAMETER Apply
  If present, actually write files. Otherwise only show preview.
.PARAMETER Ref
  The git ref (commit SHA) to use for blob URLs and file retrieval. Default: ce78d7b93bd940a3b3f12a2c3afd0d1c34d35a41
#>

param(
  [switch]$Apply,
  [string]$Ref = "ce78d7b93bd940a3b3f12a2c3afd0d1c34d35a41"
)

# Ensure running in repo root (should contain .git)
if (-not (Test-Path ".git")) {
  Write-Warning "No .git directory found in current folder. Please run this script from the repository root."
  Write-Host "Current path: $(Get-Location)"
  exit 1
}

$sha = $Ref

Write-Host "Using commit/ref: $sha"
Write-Host "Dry-run mode: $([bool](-not $Apply))"
Write-Host ""

# Explicit list of 11 .tex files for Band 1
$texFiles = @(
  "2/tex/T0_7-fragen-3_De.tex",
  "2/tex/T0_7-fragen-3_En.tex",
  "2/tex/T0_Grundlagen_De.tex",
  "2/tex/T0_Grundlagen_en.tex",
  "2/tex/T0_Introduction_En.tex",
  "2/tex/T0_Modell_Uebersicht_De.tex",
  "2/tex/T0_Modell_Uebersicht_En.tex",
  "2/tex/chapters_en/T0_7-fragen-3_En_ch.tex",
  "2/tex/chapters_en/T0_Grundlagen_En_ch.tex",
  "2/tex/chapters_en/T0_Introduction_En_ch.tex",
  "2/tex/chapters_en/T0_Modell_Uebersicht_En_ch.tex"
)

$outBase = "book1/Book1_T0_erklaert_de"
$chaptersDir = Join-Path $outBase "chapters"
$originalsDir = Join-Path $outBase "originals"
$mappingsDir = Join-Path $outBase "mappings"

if ($Apply) {
  New-Item -ItemType Directory -Path $chaptersDir -Force | Out-Null
  New-Item -ItemType Directory -Path $originalsDir -Force | Out-Null
  New-Item -ItemType Directory -Path $mappingsDir -Force | Out-Null
}

Write-Host "Files to process:"
$texFiles | ForEach-Object { Write-Host " - $_" }

foreach ($path in $texFiles) {
  $base = [System.IO.Path]::GetFileNameWithoutExtension($path)
  $mdOut = Join-Path $chaptersDir ("01_$base.md")
  $origOut = Join-Path $originalsDir ("$base.tex.raw")
  $mapOut = Join-Path $mappingsDir ("mapping_$base.yaml")
  $blobUrl = "https://github.com/jpascher/T0-Time-Mass-Duality/blob/$sha/$path"

  # Check if file exists at ref
  $gitArg = $sha + ':' + $path
  $testResult = & git cat-file -e $gitArg 2>&1
  if ($LASTEXITCODE -ne 0) {
    Write-Host "WARN: Could not find $path at ref $sha. Skipping."
    continue
  }

  Write-Host ""
  Write-Host "Processing: $path"
  Write-Host " -> md: $mdOut"
  Write-Host " -> orig: $origOut"
  Write-Host " -> map: $mapOut"
  Write-Host " -> blob URL: $blobUrl"

  # show snippet: first 30 lines from the commit snapshot
  Write-Host "---- snippet (first 30 lines) ----"
  & git show $gitArg 2>$null | Select-Object -First 30 | ForEach-Object { Write-Host "| $_" }
  Write-Host "---- end snippet ----"

  if ($Apply) {
    # write markdown stub
    $mdHeader = @"
---
source_tex: $blobUrl
original_ref: $sha
original_path: $path
mapping: $mapOut
---

# DRAFT: $($base -replace '_',' ')

(Platzhalter. Die Überarbeitung wird strikt auf Basis der Original-LaTeX erfolgen.
Die Original-LaTeX-Datei wird als Appendix angehängt. Siehe mapping: $mapOut)
"@

    # Write markdown file without trailing newline manipulation
    $mdHeader | Out-File -FilePath $mdOut -Encoding UTF8

    # write original snapshot: use git show to preserve tracked content at sha
    & git show $gitArg | Out-File -FilePath $origOut -Encoding UTF8

    # write mapping yaml
    $mappingYaml = @"
rewritten_file: $mdOut
original_file: $path
repo_blob_url: $blobUrl
original_ref: $sha
mappings: []
appendix:
  original_snapshot_file: $origOut
"@
    $mappingYaml | Out-File -FilePath $mapOut -Encoding UTF8

    Write-Host "WROTE files for $path"
  } else {
    Write-Host "(dry-run) would write md: $mdOut, orig: $origOut, map: $mapOut"
  }
}

Write-Host ""
Write-Host "Finished."
Write-Host "To actually write files re-run the script with -Apply."
Write-Host "To use a different ref: -Ref <sha> -Apply"
