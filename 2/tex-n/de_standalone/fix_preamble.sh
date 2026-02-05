#!/bin/bash
# Fix the @ifundefined line in preamble

# Create temporary file with fix
cat > temp_preamble.tex << 'ENDPRE'
% === KAPITEL 1: GRUNDLEGENDE PAKETE (müssen ZUERST kommen) ===
\RequirePackage{fontspec}
\RequirePackage{unicode-math}
\usepackage{chngcntr}
\setcounter{secnumdepth}{1}  % Nur Sections nummerieren (nicht subsections)
\setcounter{tocdepth}{1}     % Nur Sections im TOC (nicht subsections)

% Chapter counter check - needs makeatletter for standalone article documents
\makeatletter
\@ifundefined{c@chapter}{}{\counterwithout{section}{chapter}}  % Falls Kapitel existieren
\makeatother

\counterwithout{subsection}{section}  % Löse Verknüpfung
ENDPRE

# Replace lines 17-24 in the file
head -16 T0_preamble_standalone_De.tex > new_preamble.tex
cat temp_preamble.tex >> new_preamble.tex
tail -n +25 T0_preamble_standalone_De.tex >> new_preamble.tex
mv new_preamble.tex T0_preamble_standalone_De.tex
rm temp_preamble.tex

echo "Preamble fixed!"
