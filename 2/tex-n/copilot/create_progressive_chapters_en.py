#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Progressive Narrative Chapter Generator for FFGFT - English Version
Creates chapters 14-44 with progressive narrative style in English
"""

import os
import re

def get_progressive_intro_en(chapter_num):
  """Generate progressive introductions in English that build on previous chapters"""
  
  intros = {
    14: """\\subsection*{Progressive Narrative Introduction}

In the preceding thirteen chapters, we have learned the fundamental principles of FFGFT: the Time-Mass Duality, the fractal geometry with parameter $\\xi = \\frac{4}{3} \\times 10^{-4}$, and the cosmic brain as our central metaphor. We now understand that the universe does not expand in the conventional sense, but develops through increasing fractal folding at constant volume – similar to how a maturing brain forms more complex convolutions.

This chapter builds directly on these insights and examines one of the most radical consequences of the theory: \\textbf{space itself is not fundamental}. What we perceive as the "expansion of the universe" is actually the propagation of a fractal amplitude front through the vacuum – a process that creates physical space where there was none before.

Imagine observing the development of a neural network in time-lapse: neurons don't simply fire in a pre-given space, but neural activity \\textit{defines} the functional space in which information can be processed. Analogously, in the cosmic brain, the propagation of the vacuum amplitude $\\rho(\\vec{x},t)$ defines physical space itself.
""",
    15: """\\subsection*{Progressive Narrative Introduction}

Having seen in Chapter 14 how space emerges from the fractal amplitude front, we now turn to an even more fundamental aspect: the geometric structure of this emergence. The Time-Mass Duality, which we know from the first chapters, manifests here in a specific mathematical form that we will now examine in detail.

Let us recall: In the cosmic brain, space creation corresponds to the propagation of neural activity. In this chapter, we explore the precise geometric language in which this process is described – a language built on the fractal parameter $\\xi$ and the already established duality relationship.
""",
    16: """\\subsection*{Progressive Narrative Introduction}

The preceding chapters have shown us how space emerges (Chapter 14) and what geometric structure underlies this process (Chapter 15). Now we examine the dynamic consequences of this geometry: How does matter behave in a space that is itself an emergent phenomenon?

This question leads us to one of the most elegant predictions of FFGFT. In a universe that develops like a maturing brain, we expect specific signatures in the movement of galaxies and the distribution of matter. This chapter builds on our insights about the fractal dimension $D_f = 3 - \\xi$ and shows how it manifests in observable phenomena.
""",
    17: """\\subsection*{Progressive Narrative Introduction}

We have now understood the fundamentals of space emergence (Chapter 14), its geometric description (Chapter 15), and the dynamic consequences for matter (Chapter 16). This chapter brings these insights together and examines how they affect cosmological scales.

The Time-Mass Duality, which we have known since the first chapters, shows its full power here: It connects local phenomena (such as the movement of individual galaxies) with global cosmic structures. In the image of the cosmic brain, this corresponds to the connection between individual neuronal firing events and emergent consciousness phenomena.
""",
  }
  
  # Default progressive intro for chapters not specifically defined
  default = f"""\\subsection*{{Progressive Narrative Introduction}}

This chapter builds on the preceding insights. In the first {chapter_num-1} chapters, we have learned the fundamental principles of FFGFT: the Time-Mass Duality, the fractal geometry with parameter $\\xi = \\frac{{4}}{{3}} \\times 10^{{-4}}$, the emergence of space, and numerous applications of these principles.

In this chapter, we expand our understanding with further aspects that follow from the established principles. We will see how the already known concepts enable new insights and how the image of the cosmic brain continues to be refined.

The results presented here assume understanding of the previous chapters and systematically advance the argumentation.
"""
  
  return intros.get(chapter_num, default)

def get_progressive_conclusion_en(chapter_num):
  """Generate progressive conclusions in English that link to future chapters"""
  
  return f"""
\\subsection*{{Progressive Narrative Summary}}

This chapter has expanded our journey through FFGFT with important aspects. The concepts developed here build directly on the insights from chapters 1-{chapter_num-1} and prepare the ground for the following investigations.

In the cosmic brain, each new chapter corresponds to a deeper layer of understanding – similar to how in a neural network, higher processing levels build on the activations of lower levels. The mathematical structures presented here are not isolated, but an integral part of the overall picture that unfolds through all 44 chapters.

In the coming chapters, we will see how these insights find further applications and how the unified picture of FFGFT continues to be completed. Each step brings us closer to a comprehensive understanding of the universe as a self-organizing, fractally structured system – a cosmic brain that creates and maintains its own structure through the Time-Mass Duality at every moment.
"""

def create_narrative_chapter_en(chapter_num, source_dir, target_dir):
  """Create a single English narrative chapter with progressive style"""
  
  source_file = os.path.join(source_dir, f"kapitel_{chapter_num}a_En.tex")
  target_file = os.path.join(target_dir, f"Kapitel_{chapter_num:02d}_Narrative_En.tex")
  
  if not os.path.exists(source_file):
    print(f"Warning: Source file {source_file} not found")
    return False
  
  try:
    # Read source file
    with open(source_file, 'r', encoding='utf-8') as f:
      content = f.read()
    
    # Update headheight in geometry
    if 'headheight' not in content and 'geometry' in content:
      content = re.sub(r'(\\geometry\{[^}]+)\}', 
              r'\1}\n\\setlength{\\headheight}{30pt}', content)
    
    # Find the main section and insert progressive intro after it
    section_pattern = r'(\\section\{[^}]+\}\s*)'
    progressive_intro = get_progressive_intro_en(chapter_num)
    
    # Insert progressive intro after section title
    content = re.sub(section_pattern, 
            lambda m: m.group(1) + '\n' + progressive_intro + '\n\\subsection*{The Mathematical Framework}\n\n',
            content, count=1)
    
    # Add progressive conclusion before \end{document}
    progressive_conclusion = get_progressive_conclusion_en(chapter_num)
    content = content.replace('\\end{document}', 
                progressive_conclusion + '\n\\end{document}')
    
    # Write target file
    with open(target_file, 'w', encoding='utf-8') as f:
      f.write(content)
    
    print(f"Created: {target_file}")
    return True
    
  except Exception as e:
    print(f"Error processing chapter {chapter_num}: {e}")
    return False

def main():
  """Generate all English narrative chapters 14-44"""
  
  repo_root = "/home/runner/work/T0-Time-Mass-Duality/T0-Time-Mass-Duality"
  source_dir = os.path.join(repo_root, "2/tex-n/en_FFGFT/tex_kapitel")
  target_dir = os.path.join(repo_root, "2/narrative")
  
  # Process chapters 14-44
  success_count = 0
  for chapter_num in range(14, 45):
    if create_narrative_chapter_en(chapter_num, source_dir, target_dir):
      success_count += 1
  
  print(f"\nCompleted: {success_count}/31 English chapters created")
  
  return 0 if success_count == 31 else 1

if __name__ == "__main__":
  import sys
  sys.exit(main())

