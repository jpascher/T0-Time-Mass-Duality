import os
import re

# Pfad zum tex-Verzeichnis
tex_dir = '2/tex'
output_file = 'T0_Book_En.tex'

# Header für das Buch
book_header = r"""\documentclass[11pt,a4paper]{book}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{amsmath,amssymb}
\usepackage{biblatex}
\addbibresource{T0_Bibliography_En.bib}
\usepackage{graphicx}
\usepackage{hyperref}

\title{T0 Time-Mass Duality: Complete English Edition}
\author{Johann Pascher}
\date{\today}

\begin{document}

\maketitle
\tableofcontents
\newpage

\chapter{Introduction}
This book compiles all English LaTeX documents from the T0-Time-Mass-Duality repository, maintaining all untruncated content for a comprehensive publication.

"""

book_footer = r"""

\printbibliography

\end{document}
"""

def extract_content(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Finde \begin{document} und \end{document}
    start_match = re.search(r'\\begin\{document\}', content)
    end_match = re.search(r'\\end\{document\}', content)
    
    if start_match and end_match:
        start = start_match.end()
        end = end_match.start()
        return content[start:end].strip()
    else:
        # Fallback: Wenn keine document-Umgebung, nimm den ganzen Inhalt
        return content

def main():
    if not os.path.exists(tex_dir):
        print(f"Verzeichnis {tex_dir} nicht gefunden.")
        return
    
    english_files = [f for f in os.listdir(tex_dir) if f.endswith('_En.tex')]
    english_files.sort()  # Sortiere alphabetisch
    
    with open(output_file, 'w', encoding='utf-8') as out:
        out.write(book_header)
        
        for filename in english_files:
            chapter_title = filename.replace('_En.tex', '').replace('_', ' ')
            out.write(f"\chapter{{{chapter_title}}}\n")
            content = extract_content(os.path.join(tex_dir, filename))
            out.write(content + "\n\n")
        
        out.write(book_footer)
    
    print(f"Buch erstellt: {output_file}")

if __name__ == "__main__":
    main()