#!/bin/bash
# Extract content from LaTeX chapters for inclusion in master documents

for lang in De En; do
    for i in $(seq -w 1 44); do
        input_file="Kapitel_${i}_Narrative_${lang}.tex"
        output_file="Kapitel_${i}_Narrative_${lang}_content.tex"
        
        if [ -f "$input_file" ]; then
            # Extract content between \begin{document} and \end{document}
            sed -n '/\\begin{document}/,/\\end{document}/p' "$input_file" | \
            sed '1d;$d' > "$output_file"
            echo "Extracted content from $input_file to $output_file"
        fi
    done
done
