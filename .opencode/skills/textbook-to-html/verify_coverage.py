#!/usr/bin/env python3
"""
Coverage verifier for textbook-to-html skill.
Checks if all topics, formulas, and algorithms are covered.
"""

import os
import re
import sys
from pathlib import Path

def count_formulas_in_html(filepath):
    """Count formula sections in HTML file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            # Count formula divs
            formula_count = len(re.findall(r'class="formula"', content))
            # Count code blocks (algorithms)
            algorithm_count = len(re.findall(r'class="code"', content))
            # Count examples
            example_count = len(re.findall(r'class="example"', content))
            return formula_count, algorithm_count, example_count
    except:
        return 0, 0, 0

def verify_coverage(coverage_file, html_dir):
    """Verify coverage against coverage.txt tracker."""
    
    if not os.path.exists(coverage_file):
        print(f"ERROR: {coverage_file} not found!")
        print("Run textbook-to-html skill first to create coverage tracker.")
        return False
    
    with open(coverage_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Parse topics from coverage file
    topics = re.findall(r'TOPIC: (.+?)(?:\n|$)', content)
    files = re.findall(r'FILE: (.+?)(?:\n|$)', content)
    
    print("=" * 60)
    print("COVERAGE VERIFICATION REPORT")
    print("=" * 60)
    print()
    
    total_formulas = 0
    total_algorithms = 0
    total_examples = 0
    all_covered = True
    
    for i, (topic, filename) in enumerate(zip(topics, files)):
        filepath = os.path.join(html_dir, filename)
        
        if os.path.exists(filepath):
            formulas, algorithms, examples = count_formulas_in_html(filepath)
            total_formulas += formulas
            total_algorithms += algorithms
            total_examples += examples
            
            status = "✓" if formulas > 0 and examples >= 3 else "✗"
            if status == "✗":
                all_covered = False
            
            print(f"[{status}] {topic}")
            print(f"    File: {filename}")
            print(f"    Formulas: {formulas}, Algorithms: {algorithms}, Examples: {examples}")
        else:
            print(f"[✗] {topic}")
            print(f"    File: {filename} - NOT FOUND!")
            all_covered = False
        print()
    
    print("=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Topics: {len(topics)}")
    print(f"Total Formulas: {total_formulas}")
    print(f"Total Algorithms: {total_algorithms}")
    print(f"Total Examples: {total_examples}")
    print()
    
    if all_covered:
        print("STATUS: ✓ ALL TOPICS COVERED")
    else:
        print("STATUS: ✗ GAPS FOUND - Update HTML files!")
    
    return all_covered

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 verify_coverage.py coverage.txt /path/to/html/files")
        sys.exit(1)
    
    coverage_file = sys.argv[1]
    html_dir = sys.argv[2]
    
    success = verify_coverage(coverage_file, html_dir)
    sys.exit(0 if success else 1)
