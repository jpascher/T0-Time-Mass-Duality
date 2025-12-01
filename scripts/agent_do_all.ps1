# PowerShell script for T0 Book 1 automation
# This script automates the complete book generation workflow

param(
    [switch]$Build,
    [switch]$Validate,
    [switch]$GenerateMappings,
    [switch]$All
)

$ErrorActionPreference = "Stop"
$BookDir = "book1/Book1_T0_erklaert_de"

function Write-Header {
    param([string]$Message)
    Write-Host "`n=== $Message ===" -ForegroundColor Cyan
}

function Test-Prerequisites {
    Write-Header "Checking prerequisites"
    
    if (-not (Test-Path $BookDir)) {
        throw "Book directory not found: $BookDir"
    }
    
    Write-Host "✓ Book directory exists" -ForegroundColor Green
}

function Invoke-GenerateMappings {
    Write-Header "Generating mappings"
    
    $chapters = Get-ChildItem "$BookDir/chapters" -Filter "*.md"
    foreach ($chapter in $chapters) {
        $baseName = $chapter.BaseName -replace '^01_', ''
        $mappingFile = "$BookDir/mappings/mapping_$baseName.yaml"
        
        if (Test-Path $mappingFile) {
            Write-Host "✓ Mapping exists: $baseName" -ForegroundColor Green
        } else {
            Write-Host "⚠ Missing mapping: $baseName" -ForegroundColor Yellow
        }
    }
}

function Invoke-Validate {
    Write-Header "Validating structure"
    
    $requiredDirs = @("chapters", "mappings", "originals")
    foreach ($dir in $requiredDirs) {
        $path = "$BookDir/$dir"
        if (Test-Path $path) {
            $count = (Get-ChildItem $path -File).Count
            Write-Host "✓ $dir`: $count files" -ForegroundColor Green
        } else {
            Write-Host "✗ Missing: $dir" -ForegroundColor Red
        }
    }
}

function Invoke-Build {
    Write-Header "Building book"
    
    if (Test-Path "scripts/build_book.sh") {
        if ($IsLinux -or $IsMacOS) {
            & bash scripts/build_book.sh
        } else {
            Write-Host "Running bash script via WSL or Git Bash..."
            & bash scripts/build_book.sh
        }
    } else {
        Write-Host "Build script not found" -ForegroundColor Yellow
    }
}

# Main execution
try {
    Test-Prerequisites
    
    if ($All -or $GenerateMappings) { Invoke-GenerateMappings }
    if ($All -or $Validate) { Invoke-Validate }
    if ($All -or $Build) { Invoke-Build }
    
    if (-not ($All -or $Build -or $Validate -or $GenerateMappings)) {
        Write-Host "`nUsage: agent_do_all.ps1 [-Build] [-Validate] [-GenerateMappings] [-All]"
    }
    
    Write-Header "Complete"
}
catch {
    Write-Host "Error: $_" -ForegroundColor Red
    exit 1
}
