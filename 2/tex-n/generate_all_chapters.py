#!/usr/bin/env python3
"""
Generate all missing DVFT chapters with T0 Theory adaptations
Extracts chapters from DVFT.txt and creates bilingual LaTeX files
"""

import re
import os
from pathlib import Path

# Repository base path
BASE_DIR = Path("/home/runner/work/T0-Time-Mass-Duality/T0-Time-Mass-Duality/2/tex-n")
DVFT_FILE = BASE_DIR / "DVFT.txt"
EN_DIR = BASE_DIR / "en_standalone"
DE_DIR = BASE_DIR / "de_standalone"

# Read DVFT.txt
with open(DVFT_FILE, 'r', encoding='utf-8') as f:
    dvft_content = f.read()

# Find all chapter boundaries
chapter_pattern = r'^CHAPTER (\d+):\s*(.+?)$'
chapters = []

lines = dvft_content.split('\n')
current_chapter = None
current_content = []

for i, line in enumerate(lines):
    match = re.match(chapter_pattern, line)
    if match:
        # Save previous chapter
        if current_chapter:
            chapters.append({
                'num': current_chapter['num'],
                'title': current_chapter['title'],
                'content': '\n'.join(current_content)
            })
        
        # Start new chapter
        current_chapter = {
            'num': int(match.group(1)),
            'title': match.group(2).strip()
        }
        current_content = [line]
    elif current_chapter:
        current_content.append(line)

# Add last chapter
if current_chapter:
    chapters.append({
        'num': current_chapter['num'],
        'title': current_chapter['title'],
        'content': '\n'.join(current_content)
    })

print(f"Found {len(chapters)} chapters in DVFT.txt")

# Check which chapters exist
existing_en = set()
for f in EN_DIR.glob("Chapter_*.tex"):
    match = re.search(r'Chapter_(\d+)_', f.name)
    if match:
        existing_en.add(int(match.group(1)))

print(f"Existing English chapters: {sorted(existing_en)}")
print(f"Total to create: {len(chapters) - len(existing_en)} English + German chapters")

# List missing chapters
missing = [ch['num'] for ch in chapters if ch['num'] not in existing_en]
print(f"Missing chapters: {missing}")
