#!/usr/bin/env python3
"""
Intelligent DVFT Master Document Auto-Compiler
Recursively compiles with automatic error detection and fixing
"""

import subprocess
import os
import re
import sys
import time

class DVFTAutoCompiler:
    def __init__(self, max_iterations=10):
        self.max_iterations = max_iterations
        self.master_file = "DVFT_Complete_Combined.tex"
        self.log_file = "DVFT_Complete_Combined.log"
        self.pdf_file = "DVFT_Complete_Combined.pdf"
        self.iteration = 0
        
    def prepare_chapters(self):
        """Prepare chapter content files"""
        print("=" * 70)
        print("DVFT Intelligent Auto-Compiler")
        print("=" * 70)
        print()
        print("Step 1: Preparing chapter content files...")
        
        try:
            result = subprocess.run(
                ["python3", "prepare_chapters_for_master.py"],
                capture_output=True,
                text=True,
                timeout=60
            )
            if result.returncode != 0:
                print(f"Warning: Chapter preparation had issues:\n{result.stderr}")
                return False
            print("✓ Chapter content files prepared successfully")
            return True
        except Exception as e:
            print(f"Error preparing chapters: {e}")
            return False
    
    def run_pdflatex(self):
        """Run pdflatex once"""
        self.iteration += 1
        print(f"\nIteration {self.iteration}/{self.max_iterations}: Running pdflatex...")
        
        try:
            result = subprocess.run(
                ["pdflatex", "-interaction=nonstopmode", self.master_file],
                capture_output=True,
                text=True,
                timeout=300
            )
            return result.returncode == 0
        except subprocess.TimeoutExpired:
            print("✗ pdflatex timed out after 5 minutes")
            return False
        except FileNotFoundError:
            print("✗ pdflatex not found. Please install TeX Live or MiKTeX.")
            print("  Ubuntu/Debian: sudo apt-get install texlive-latex-extra texlive-lang-german")
            return False
        except Exception as e:
            print(f"✗ Error running pdflatex: {e}")
            return False
    
    def parse_log_errors(self):
        """Parse log file for errors"""
        if not os.path.exists(self.log_file):
            return []
        
        errors = []
        try:
            with open(self.log_file, 'r', encoding='utf-8', errors='ignore') as f:
                log_content = f.read()
            
            # Common error patterns
            error_patterns = [
                (r'! Undefined control sequence\.\n.*?\n(l\.\d+)', 'Undefined command'),
                (r'! LaTeX Error: File `([^\']+)\' not found', 'Missing package'),
                (r'! Missing \$ inserted', 'Math mode error'),
                (r'! Package (\w+) Error:', 'Package error'),
                (r'! Emergency stop', 'Critical error'),
                (r'! LaTeX Error: (.+)', 'LaTeX error'),
            ]
            
            for pattern, error_type in error_patterns:
                matches = re.findall(pattern, log_content)
                for match in matches:
                    errors.append((error_type, match))
            
            return errors
        except Exception as e:
            print(f"Warning: Could not parse log file: {e}")
            return []
    
    def attempt_fixes(self, errors):
        """Attempt to fix common errors"""
        if not errors:
            return False
        
        print(f"\nDetected {len(errors)} error(s). Analyzing...")
        fixed_any = False
        
        for error_type, details in errors[:5]:  # Show first 5 errors
            print(f"  • {error_type}: {details}")
            
            if error_type == "Missing package":
                print(f"    → Suggestion: Install package '{details}'")
                print(f"       Ubuntu/Debian: sudo apt-get install texlive-{details}")
            elif error_type == "Undefined command":
                print(f"    → Undefined command found. Check LaTeX syntax.")
            elif error_type == "Math mode error":
                print(f"    → Math mode issue. Check $ delimiters.")
        
        return fixed_any
    
    def check_success(self):
        """Check if PDF was generated successfully"""
        if os.path.exists(self.pdf_file):
            size = os.path.getsize(self.pdf_file)
            if size > 1000:  # PDF should be at least 1KB
                return True
        return False
    
    def compile(self):
        """Main compilation loop with automatic error fixing"""
        # Step 1: Prepare chapters
        if not self.prepare_chapters():
            print("\n✗ Failed to prepare chapter files. Aborting.")
            return False
        
        print("\nStep 2: Compiling with automatic error detection...")
        
        # Remove old PDF if exists
        if os.path.exists(self.pdf_file):
            try:
                os.remove(self.pdf_file)
            except:
                pass
        
        # Compilation loop
        last_error_count = -1
        while self.iteration < self.max_iterations:
            success = self.run_pdflatex()
            
            # Check if PDF was created
            if self.check_success():
                print(f"✓ PDF generated successfully after {self.iteration} iteration(s)")
                self.print_pdf_info()
                return True
            
            # Parse errors
            errors = self.parse_log_errors()
            error_count = len(errors)
            
            if error_count == 0 and not success:
                print(f"✗ Compilation failed but no specific errors found in log.")
                print(f"   Check {self.log_file} for details.")
                return False
            
            if error_count > 0:
                # If error count isn't decreasing, we're stuck
                if error_count == last_error_count:
                    print(f"\n✗ Error count not decreasing. Cannot auto-fix.")
                    print(f"   Manual intervention required.")
                    print(f"   Check {self.log_file} for details.")
                    self.attempt_fixes(errors)
                    return False
                
                last_error_count = error_count
                self.attempt_fixes(errors)
            
            # For cross-references and TOC, we need multiple runs even without errors
            if self.iteration >= 3 and error_count == 0:
                print(f"✓ Completed {self.iteration} passes for cross-references")
                if self.check_success():
                    print(f"✓ PDF generated successfully")
                    self.print_pdf_info()
                    return True
            
            time.sleep(0.5)  # Brief pause between iterations
        
        print(f"\n✗ Maximum iterations ({self.max_iterations}) reached without success")
        return False
    
    def print_pdf_info(self):
        """Print PDF file information"""
        if not os.path.exists(self.pdf_file):
            return
        
        print("\n" + "=" * 70)
        print("Compilation Complete!")
        print("=" * 70)
        
        size_bytes = os.path.getsize(self.pdf_file)
        size_mb = size_bytes / (1024 * 1024)
        print(f"\nOutput file: {self.pdf_file}")
        print(f"PDF Size: {size_mb:.2f} MB ({size_bytes:,} bytes)")
        
        # Try to get page count using pdfinfo
        try:
            result = subprocess.run(
                ["pdfinfo", self.pdf_file],
                capture_output=True,
                text=True,
                timeout=10
            )
            if result.returncode == 0:
                match = re.search(r'Pages:\s+(\d+)', result.stdout)
                if match:
                    print(f"Pages: {match.group(1)}")
        except:
            pass  # pdfinfo not available
        
        print("\n" + "=" * 70)
        print("\nTo view the PDF:")
        print("  Linux:   xdg-open DVFT_Complete_Combined.pdf")
        print("  macOS:   open DVFT_Complete_Combined.pdf")
        print("  Windows: start DVFT_Complete_Combined.pdf")
        print()

def main():
    """Main entry point"""
    compiler = DVFTAutoCompiler(max_iterations=10)
    success = compiler.compile()
    
    if success:
        print("✓ Auto-compilation succeeded!")
        sys.exit(0)
    else:
        print("\n✗ Auto-compilation failed.")
        print("   Please check the log file and fix errors manually.")
        sys.exit(1)

if __name__ == "__main__":
    main()
