#!/usr/bin/env python3
"""
Analyze all .tex files to collect package usage and custom commands.
"""

import os
import re
from pathlib import Path
from collections import defaultdict

def extract_packages_and_commands(tex_file):
    """Extract usepackage commands and custom definitions from a tex file."""
    packages = []
    commands = []
    
    with open(tex_file, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
        
    # Extract \usepackage commands
    package_pattern = r'\\usepackage(?:\[[^\]]*\])?\{([^}]+)\}'
    packages = re.findall(package_pattern, content)
    
    # Extract custom command definitions
    command_patterns = [
        r'\\newcommand\{([^}]+)\}',
        r'\\renewcommand\{([^}]+)\}',
        r'\\newtheorem\{([^}]+)\}',
        r'\\definecolor\{([^}]+)\}',
        r'\\DeclareMathOperator\{([^}]+)\}',
    ]
    
    for pattern in command_patterns:
        commands.extend(re.findall(pattern, content))
    
    return packages, commands

# Process files
tex_dir = Path("2/tex")
all_packages = defaultdict(int)
all_commands = defaultdict(int)

for tex_file in tex_dir.glob("*.tex"):
    packages, commands = extract_packages_and_commands(tex_file)
    for pkg in packages:
        all_packages[pkg] += 1
    for cmd in commands:
        all_commands[cmd] += 1

# Output results
print("=" * 60)
print("MOST COMMON PACKAGES:")
print("=" * 60)
sorted_packages = sorted(all_packages.items(), key=lambda x: x[1], reverse=True)
for pkg, count in sorted_packages[:30]:
    print(f"{pkg:40} used in {count} files")

print("\n" + "=" * 60)
print("CUSTOM COMMANDS:")
print("=" * 60)
sorted_commands = sorted(all_commands.items(), key=lambda x: x[1], reverse=True)
for cmd, count in sorted_commands[:20]:
    print(f"{cmd:40} used in {count} files")

print(f"\nTotal unique packages: {len(all_packages)}")
print(f"Total unique custom commands: {len(all_commands)}")
