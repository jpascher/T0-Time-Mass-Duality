# COMPILATION INSTRUCTIONS

**For:** Xi-Narrative Complete Project (Reordered)  
**Compiler:** LuaLaTeX (REQUIRED!)

---

## 🎯 QUICK START

```bash
# In project directory:
lualatex Xi_Narrative_Master_De_REORDERED.tex
lualatex Xi_Narrative_Master_De_REORDERED.tex  # 2× for references
```

**Done!** → `Xi_Narrative_Master_De_REORDERED.pdf`

---

## 📋 PREREQUISITES

### **1. LaTeX Distribution**

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install texlive-full
```

**macOS:**
```bash
brew install --cask mactex
```

**Windows:**
- Download: https://www.tug.org/texlive/
- Install TeX Live (Full)

### **2. Fonts**

**Linux:**
```bash
sudo apt install fonts-inter fonts-jetbrains-mono fonts-libertinus
```

**macOS:**
```bash
brew tap homebrew/cask-fonts
brew install --cask font-inter font-jetbrains-mono
```

**Windows:**
- Download manually:
  - Inter: https://fonts.google.com/specimen/Inter
  - JetBrains Mono: https://www.jetbrains.com/lp/mono/
  - Libertinus Math: https://github.com/libertinus-fonts/libertinus

### **3. Editor (Optional)**

**TeXstudio (recommended):**
```bash
sudo apt install texstudio           # Linux
brew install --cask texstudio        # macOS
```

**In TeXstudio:**
- Options → Configure TeXstudio → Build
- Default Compiler → **LuaLaTeX**

---

## 🚀 COMPILATION

### **Method 1: Command Line**

```bash
# Simple
lualatex Xi_Narrative_Master_De_REORDERED.tex

# With cross-references
lualatex Xi_Narrative_Master_De_REORDERED.tex
lualatex Xi_Narrative_Master_De_REORDERED.tex

# With bibliography (if present)
lualatex Xi_Narrative_Master_De_REORDERED.tex
bibtex Xi_Narrative_Master_De_REORDERED
lualatex Xi_Narrative_Master_De_REORDERED.tex
lualatex Xi_Narrative_Master_De_REORDERED.tex
```

### **Method 2: TeXstudio**

1. Open `Xi_Narrative_Master_De_REORDERED.tex`
2. Press `F5` (or Tools → Build & View)
3. Done!

### **Method 3: Makefile**

Create `Makefile`:
```makefile
.PHONY: all clean

all:
	lualatex Xi_Narrative_Master_De_REORDERED.tex
	lualatex Xi_Narrative_Master_De_REORDERED.tex

clean:
	rm -f *.aux *.log *.toc *.out *.pdf
```

Then:
```bash
make        # Compile
make clean  # Clean up
```

---

## ✅ EXPECTED OUTPUT

### **Successful Compilation:**

```
...
Output written on Xi_Narrative_Master_De_REORDERED.pdf (XXX pages)
Transcript written on Xi_Narrative_Master_De_REORDERED.log.
```

### **PDF Properties:**

```
Filename:    Xi_Narrative_Master_De_REORDERED.pdf
Pages:       ~150-200 (depending on formatting)
Format:      6" × 9" (book format)
File size:   ~500 KB - 1 MB
```

---

## ⚠️ COMMON ERRORS

### **Error 1: "I can't find file T0_preamble_shared_De.tex"**

**Problem:** Preamble not found

**Solution:**
```bash
# Check preamble exists in same directory:
ls T0_preamble_shared_De.tex

# If not present:
# Copy from project archive
```

### **Error 2: "Font 'Inter' not found"**

**Problem:** Fonts not installed

**Solution:**
```bash
# Linux:
sudo apt install fonts-inter

# macOS:
brew install --cask font-inter

# Windows:
# Download & install manually
```

### **Error 3: "Undefined control sequence \xipar"**

**Problem:** Preamble not loaded

**Solution:**
- Ensure `\input{T0_preamble_shared_De}` is in master file
- Check preamble file exists

### **Error 4: "Package inputenc Error"**

**Problem:** Wrong compiler

**Solution:**
```bash
# DON'T use pdflatex!
# Use:
lualatex Xi_Narrative_Master_De_REORDERED.tex
```

---

## 📊 WARNINGS (NOT CRITICAL)

### **Overfull hbox:**

```
Overfull \hbox (10.5pt too wide) in paragraph at lines 123--125
```

**Meaning:** Text slightly exceeds margin  
**Status:** ⚠️ Cosmetic (not critical)  
**Action:** Can be ignored (PDF still correct)

### **Underfull hbox:**

```
Underfull \hbox (badness 1852) in paragraph at lines 200--202
```

**Meaning:** Line is too empty  
**Status:** ⚠️ Cosmetic  
**Action:** Can be ignored

### **Label may have changed:**

```
LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.
```

**Meaning:** Cross-references need update  
**Action:** **Simply compile again:**
```bash
lualatex Xi_Narrative_Master_De_REORDERED.tex
```

---

## 🔍 TESTING INDIVIDUAL CHAPTERS

### **Compile only Chapter 10:**

```bash
cat > test_ch10.tex << 'EOF'
\documentclass[12pt]{book}
\input{T0_preamble_shared_De}
\begin{document}
\input{Kapitel_10_Xi_Narrative_De_REBUILD}
\end{document}
