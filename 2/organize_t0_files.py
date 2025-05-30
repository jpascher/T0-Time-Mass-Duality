#!/usr/bin/env python3
"""
T0-Model File Organization Script
=================================

This script organizes T0-Model LaTeX files by language:
- Moves files ending with 'De.tex' to 'de/' subdirectory (German)
- Moves files ending with 'En.tex' to 'en/' subdirectory (English)
- Creates subdirectories if they don't exist
- Provides detailed logging of all operations

Author: T0-Model Project
Date: 2025
"""

import os
import shutil
import sys
from pathlib import Path


def create_directories(base_path):
    """Create language subdirectories if they don't exist."""
    de_dir = base_path / "de"
    en_dir = base_path / "en"
    
    de_dir.mkdir(exist_ok=True)
    en_dir.mkdir(exist_ok=True)
    
    print(f"✓ Created/verified directory: {de_dir}")
    print(f"✓ Created/verified directory: {en_dir}")
    
    return de_dir, en_dir


def find_tex_files(base_path):
    """Find all .tex files with De/En endings."""
    de_files = list(base_path.glob("*De.tex"))
    en_files = list(base_path.glob("*En.tex"))
    
    return de_files, en_files


def move_files(files, target_dir, language):
    """Move files to target directory with error handling."""
    moved_count = 0
    
    for file_path in files:
        try:
            target_path = target_dir / file_path.name
            
            # Check if target already exists
            if target_path.exists():
                print(f"⚠️  Target exists, overwriting: {target_path}")
            
            shutil.move(str(file_path), str(target_path))
            print(f"✓ Moved ({language}): {file_path.name} → {target_dir.name}/")
            moved_count += 1
            
        except Exception as e:
            print(f"❌ Error moving {file_path.name}: {e}")
    
    return moved_count


def find_file_pairs(de_files, en_files):
    """Find and display paired files (same base name)."""
    de_bases = {file.stem[:-2] for file in de_files}  # Remove 'De' suffix
    en_bases = {file.stem[:-2] for file in en_files}  # Remove 'En' suffix
    
    paired = de_bases & en_bases
    de_only = de_bases - en_bases
    en_only = en_bases - de_bases
    
    return paired, de_only, en_only


def print_summary(paired, de_only, en_only, de_moved, en_moved):
    """Print detailed summary of operations."""
    print("\n" + "="*60)
    print("📊 T0-MODEL FILE ORGANIZATION SUMMARY")
    print("="*60)
    
    print(f"\n📁 Files moved:")
    print(f"   German (De): {de_moved} files")
    print(f"   English (En): {en_moved} files")
    print(f"   Total: {de_moved + en_moved} files")
    
    if paired:
        print(f"\n🔗 Paired files (De + En): {len(paired)}")
        for base in sorted(paired):
            print(f"   • {base}De.tex ↔ {base}En.tex")
    
    if de_only:
        print(f"\n🇩🇪 German-only files: {len(de_only)}")
        for base in sorted(de_only):
            print(f"   • {base}De.tex")
    
    if en_only:
        print(f"\n🇬🇧 English-only files: {len(en_only)}")
        for base in sorted(en_only):
            print(f"   • {base}En.tex")


def find_english_files_with_german_pairs(base_path):
    """Find English files that have corresponding German files."""
    de_files = list(base_path.glob("*De.tex"))
    en_files = list(base_path.glob("*En.tex"))
    
    # Create mapping of base names to files
    de_bases = {file.stem[:-2]: file for file in de_files}  # Remove 'De' suffix
    en_bases = {file.stem[:-2]: file for file in en_files}  # Remove 'En' suffix
    
    # Find English files that have German counterparts
    paired_en_files = []
    for base_name in de_bases.keys():
        if base_name in en_bases:
            paired_en_files.append(en_bases[base_name])
    
    return paired_en_files, de_files, en_files


def main():
    """Main function to move English files to 'en' directory only if German version exists."""
    print("🚀 T0-Model English File Organization Script")
    print("=" * 50)
    print("📝 Only moves English files (*En.tex) to 'en/' if German version (*De.tex) exists")
    
    # Get current directory
    base_path = Path.cwd()
    print(f"📂 Working directory: {base_path}")
    
    try:
        # Create en subdirectory only
        en_dir = base_path / "en"
        en_dir.mkdir(exist_ok=True)
        print(f"✓ Created/verified directory: {en_dir}")
        
        # Find files
        print("\n🔍 Scanning for T0-Model LaTeX files...")
        paired_en_files, de_files, en_files = find_english_files_with_german_pairs(base_path)
        
        print(f"   Found {len(de_files)} German files (*De.tex)")
        print(f"   Found {len(en_files)} English files (*En.tex)")
        print(f"   Found {len(paired_en_files)} English files with German counterparts")
        
        if not paired_en_files:
            print("\n⚠️  No English files with German counterparts found!")
            print("    Looking for pairs like: SomeNameDe.tex + SomeNameEn.tex")
            return
        
        # Show which files will be moved
        print(f"\n📋 English files to be moved (have German counterpart):")
        for en_file in paired_en_files:
            base_name = en_file.stem[:-2]  # Remove 'En' suffix
            de_file = f"{base_name}De.tex"
            print(f"   • {en_file.name} → en/ (German: {de_file})")
        
        # Move only English files that have German counterparts
        print(f"\n📦 Moving {len(paired_en_files)} English files to 'en/' directory...")
        en_moved = move_files(paired_en_files, en_dir, "English")
        
        print("\n" + "="*60)
        print("📊 SUMMARY")
        print("="*60)
        print(f"✅ Moved {en_moved} English files to 'en/' directory")
        print(f"📁 German files remain in current directory")
        print(f"📁 English files now in: {en_dir}")
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Operation cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()