# Database Chapters 7 & 8 — Normalization & Functional Dependency

## Overview
Add two new chapters to the `book/db/` directory following the existing pattern.

## Chapter Structure
Each chapter has:
- `index.html` — card grid linking to subtopic pages (same dark terminal theme)
- Multiple `*-comprehensive.html` pages — each a full tabbed topic page with the same CSS/JS style as ch. 6

## Chapter 7 — نرمالسازی (Normalization) — 10 subtopics
1. `normalization-intro-comprehensive.html` — Redundancy, Insert/Update/Delete Anomalies
2. `first-normal-form-comprehensive.html` — 1NF (Atomicity, Repeating Groups)
3. `second-normal-form-comprehensive.html` — 2NF (Partial Dependency)
4. `third-normal-form-comprehensive.html` — 3NF (Transitive Dependency)
5. `bcnf-comprehensive.html` — BCNF (Strictest of 3NF family)
6. `fourth-normal-form-comprehensive.html` — 4NF (Multi-valued Dependency)
7. `fifth-normal-form-comprehensive.html` — 5NF (Join Dependency)
8. `normalization-process-comprehensive.html` — Step-by-step process with examples
9. `denormalization-comprehensive.html` — Trade-offs, performance considerations
10. `normal-forms-comparison-comprehensive.html` — Side-by-side comparison table

## Chapter 8 — وابستگی تابعی (Functional Dependency) — 8 subtopics
1. `fd-intro-comprehensive.html` — Definition, notation, types
2. `armstrong-axioms-comprehensive.html` — Reflexivity, Augmentation, Transitivity
3. `attribute-closure-comprehensive.html` — Closure algorithm, uses
4. `fd-closure-comprehensive.html` — Closure of FD set, equivalence
5. `canonical-cover-comprehensive.html` — Minimal cover, algorithm
6. `lossless-decomposition-comprehensive.html` — Lossless join, dependency preservation
7. `key-computation-comprehensive.html` — Computing keys from FDs
8. `candidate-keys-comprehensive.html` — Superkeys vs candidate keys

## Style & Format
- Same dark theme (`#0f172a` background, `#22c55e` green accent, `#f97316` orange headings)
- Tab-based navigation within each page
- `.section`, `.formula`, `.example`, `.code`, `.table`, `.warning` classes as in ch. 6
- English content (consistent with existing db pages)
- RTL-friendly for Persian titles
