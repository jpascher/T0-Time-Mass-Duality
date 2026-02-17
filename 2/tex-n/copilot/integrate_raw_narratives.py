#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Integration script for raw narrative chapters 13-44
Replaces existing narrative chapters with new raw versions
"""

import os
import shutil

def main():
  """Integrate raw narrative chapters into the narrative directory"""
  
  repo_root = "/home/runner/work/T0-Time-Mass-Duality/T0-Time-Mass-Duality"
  raw_dir = os.path.join(repo_root, "2/narrative/raw_narrative_chapters_13-44")
  narrative_dir = os.path.join(repo_root, "2/narrative")
  
  # Get list of raw narrative files
  raw_files = [f for f in os.listdir(raw_dir) if f.endswith('_De.tex')]
  
  print(f"Found {len(raw_files)} raw narrative files")
  
  # Process each raw file
  for raw_file in sorted(raw_files):
    # Extract chapter number from filename: Kapitel_XXa_Narrative_De.tex -> XX
    import re
    match = re.match(r'Kapitel_(\d+)a_Narrative_De\.tex', raw_file)
    if not match:
      print(f"Warning: Could not extract chapter number from {raw_file}")
      continue
    
    chapter_num = int(match.group(1))
    
    # Source and target paths
    source_path = os.path.join(raw_dir, raw_file)
    target_file = f"Kapitel_{chapter_num:02d}_Narrative_De.tex"
    target_path = os.path.join(narrative_dir, target_file)
    
    # Copy the raw file to replace the existing narrative file
    shutil.copy2(source_path, target_path)
    print(f"✓ Replaced {target_file} with raw narrative version")
  
  print(f"\nIntegration complete: {len(raw_files)} chapters replaced")
  
  # Check for missing chapters
  expected_chapters = list(range(13, 45))
  existing_chapters = [int(re.match(r'Kapitel_(\d+)a_Narrative_De\.tex', f).group(1)) 
            for f in raw_files]
  missing_chapters = [ch for ch in expected_chapters if ch not in existing_chapters]
  
  if missing_chapters:
    print(f"\nMissing chapters that need to be created: {missing_chapters}")
  
  return 0

if __name__ == "__main__":
  import sys
  sys.exit(main())

