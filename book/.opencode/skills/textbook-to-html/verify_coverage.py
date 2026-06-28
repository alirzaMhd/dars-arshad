#!/usr/bin/env python3
"""
Coverage verifier for textbook-to-html skill.
Checks if all topics, formulas, and algorithms are covered.
Also checks for English content (not copy-pasted from source).
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
            # Count formula divs (multiple class name patterns)
            formula_count = len(re.findall(r'class="formula(?:\s|")', content))
            formula_count += len(re.findall(r'class="formula-box"', content))
            # Count code blocks (algorithms) - multiple patterns
            algorithm_count = len(re.findall(r'class="code"', content))
            algorithm_count += len(re.findall(r'class="pseudo"', content))
            # Count examples - multiple patterns
            example_count = len(re.findall(r'class="example"', content))
            example_count += len(re.findall(r'class="card(?:\s|")', content))
            return formula_count, algorithm_count, example_count
    except:
        return 0, 0, 0

def check_english_content(filepath):
    """Check if file has English content (not just copied from source)."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
            # Check for English words (common words)
            english_words = ['the', 'is', 'are', 'was', 'and', 'or', 'not', 'in', 'on', 'at',
                           'to', 'for', 'of', 'with', 'by', 'from', 'as', 'into', 'through',
                           'Time', 'Space', 'Example', 'Formula', 'Algorithm', 'Complexity']
            
            english_count = sum(1 for word in english_words if word in content)
            
            # Check for Persian/Arabic characters (UTF-8 range)
            persian_chars = len(re.findall(r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF]', content))
            
            # Good if has English content and minimal Persian
            has_english = english_count >= 5
            has_persian = persian_chars > 10
            
            if has_english and not has_persian:
                return "✓ English"
            elif has_english and has_persian:
                return "⚠ Mixed"
            elif has_persian:
                return "✗ Persian"
            else:
                return "? Unknown"
    except:
        return "? Error"

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
            english_status = check_english_content(filepath)
            total_formulas += formulas
            total_algorithms += algorithms
            total_examples += examples
            
            # Check if topic is complete
            has_formulas = formulas > 0
            has_examples = examples >= 3
            has_english = "✓" in english_status
            
            status = "✓" if has_formulas and has_examples and has_english else "✗"
            if status == "✗":
                all_covered = False
            
            print(f"[{status}] {topic}")
            print(f"    File: {filename}")
            print(f"    Formulas: {formulas}, Algorithms: {algorithms}, Examples: {examples}")
            print(f"    Language: {english_status}")
            
            # Show specific issues
            issues = []
            if not has_formulas:
                issues.append("Missing formulas")
            if not has_examples:
                issues.append(f"Only {examples} examples (need 3+)")
            if not has_english:
                issues.append("Content not in English")
            if issues:
                print(f"    Issues: {', '.join(issues)}")
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
