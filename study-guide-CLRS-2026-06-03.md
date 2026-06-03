# Study Guide: Introduction to Algorithms (CLRS, 4th Edition)

> Generated 2026-06-03. Subject: Computer Science. Exam format: Mixed. Coverage: comprehensive. Target length: no limit.

## Chapter-by-Chapter Breakdown

# CLRS Introduction to Algorithms (4th Ed.) — Comprehensive Study Guide: Chapters 1–5

---

## Ch. 1 — The Role of Algorithms in Computing

### Named Entities (Terms & Definitions)

- **algorithm**: A well-defined computational procedure that takes some value(s) as input and produces some value(s) as output in a finite amount of time; a sequence of computational steps that transform input into output.
- **computational problem**: A specification of the desired input/output relationship for problem instances, typically of arbitrarily large size.
- **instance**: A particular input to a problem (satisfying the problem's constraints).
- **correct algorithm**: One that halts with the correct output for every problem instance.
- **incorrect algorithm**: Might not halt on some inputs or might produce incorrect answers; can still be useful if error rate is controllable.
- **data structure**: A way to store and organize data to facilitate access and modifications.
- **NP-complete**: A class of problems for which no efficient algorithm is known, but if an efficient algorithm exists for one, it exists for all.
- **approximation algorithm**: An algorithm that gives a good, but not necessarily optimal, solution (used for NP-complete problems).
- **online algorithm**: An algorithm that receives input over time rather than all at once.
- **parallel computer / multicore**: Computers with multiple processing cores requiring parallel algorithms.
- **keys**: The values being sorted.
- **satellite data**: Associated data that moves with the key during sorting.
- **record**: A key plus its associated satellite data.

### Processes / Algorithms / Pathways

#### Sorting Problem Definition
- **Input**: A sequence of n numbers ⟨a₁, a₂, …, a_n⟩
- **Output**: A permutation (reordering) ⟨a'₁, a'₂, …, a'_n⟩ such that a'₁ ≤ a'₂ ≤ … ≤ a'_n

#### Insertion Sort (informal)
- Works like sorting a hand of playing cards
- Start with empty left hand, cards on table
- One at a time, take a card from the pile and insert it into correct position in left hand
- At all times, cards in left hand are sorted
- **Complexity**: Θ(n²) worst-case, Θ(n) best-case

#### Merge Sort (informal)
- **Complexity**: Θ(n lg n) worst-case
- Uses divide-and-conquer (detailed in Ch. 2)

### Comparisons & Trade-offs

| Dim | Insertion Sort | Merge Sort |
|-----|---------------|------------|
| Time (rough) | c₁·n² | c₂·n lg n |
| Constant factor | Smaller (c₁ < c₂) | Larger |
| n=1000 | n factor | lg n ≈ 10 |
| n=1,000,000 | n factor | lg n ≈ 20 |
| Cross-over | Faster for small n | Faster once n large enough |

### Formulas & Equations

**Running time comparison (concrete example)**
- Computer A (10 billion instr/sec) runs insertion sort: 2n² instructions
- Computer B (10 million instr/sec) runs merge sort: 50 n lg n instructions
- For n=10,000,000:
  - Computer A: 2·(10⁷)² / 10¹⁰ = 20,000 sec ≈ 5.56 hours
  - Computer B: 50·10⁷·lg(10⁷) / 10⁷ ≈ 50·23.25 ≈ 1163 sec ≈ 0.32 hours
- Computer B (slower!) runs 17× faster than Computer A

### Case Studies / Classic Examples

1. **Human Genome Project**: Identifying genes, sequencing DNA base pairs, storing/analyzing data — all require sophisticated algorithms (dynamic programming Ch. 14)
2. **Internet**: Finding routes (shortest path, Ch. 22), search engines (Ch. 11, 32)
3. **Electronic commerce**: Public-key cryptography, digital signatures (Ch. 31)
4. **Manufacturing/commerce**: Linear programming for resource allocation (Ch. 29)
5. **Shortest path in road maps**: Model as graph, find shortest path (Ch. 22)
6. **Topological sorting**: Order parts so each appears before parts that use it (Ch. 20)
7. **Clustering for cancer diagnosis**: Identify tumors by similarity (Ch. 33)
8. **Data compression**: Huffman coding (Ch. 15), LZW compression
9. **Discrete Fourier Transform (FFT)**: Signal processing, data compression, multiplying polynomials (Ch. 30)
10. **Traveling-salesperson problem**: NP-complete; approximation algorithms (Ch. 35)

### End-of-Chapter Material

**1.1-1** Real-world examples: sorting (organizing files by date); shortest distance (GPS navigation).

**1.1-2** Other efficiency measures: memory usage, power consumption, communication bandwidth.

**1.1-3** Example: array — strength: O(1) random access; limitation: O(n) insert/delete.

**1.1-4** Shortest-path and traveling-salesperson are similar: both find optimal routes through a graph. Different: shortest-path can be solved efficiently (O(E lg V)); traveling-salesperson is NP-complete (no known efficient algorithm).

**1.1-5** Only best will do: air traffic control landing schedules. Approximately best is good enough: recommendation systems.

**1.1-6** Entire input available: sorting a list of known items. Input arriving over time: stock market trading algorithms.

**1.2-1** Navigation app: uses shortest-path algorithms (Dijkstra/A*), map rendering algorithms, address interpolation.

**1.2-2** Insertion sort beats merge sort when 8n² < 64n lg n → n < 8 lg n → n ≤ 43. (Solve: 8n² < 64n lg n → n < 8 lg n → n/8 < lg n → n ≤ 43.)

**1.2-3** 100n² < 2ⁿ → smallest n = 15. (Check: 100·225 = 22500 vs 2¹⁵ = 32768; n=14: 100·196=19600 vs 16384 — insertion wins, so n=15.)

**Problem 1-1**: For each function f(n) and time t, find largest n solvable. Key approach: solve f(n) = t × 10⁶ (since 1 microsecond). Functions: lg n, √n, n, n lg n, n², n³, 2ⁿ, n!.

---

## Ch. 2 — Getting Started

### Named Entities (Terms & Definitions)

- **keys**: The values being sorted.
- **satellite data**: Associated data carried with the key.
- **record**: A key plus its satellite data.
- **pseudocode**: Algorithm description similar to C/C++/Java/Python/JavaScript but using clear/concise expressions.
- **loop invariant**: A property that holds before each iteration of a loop, used to prove correctness.
- **subarray**: A contiguous portion of an array, denoted A[i:j].
- **RAM (random-access machine) model**: Computation model with one processor, sequential instructions, constant-time per instruction/data access.
- **input size**: The number of items in the input (for sorting) or total bits (for integer multiplication).
- **running time**: Number of instructions and data accesses executed.
- **order of growth**: The rate of growth of running time; considers only leading term without constant coefficient.
- **Θ-notation**: Informal in Ch. 2, formalized in Ch. 3. "Roughly proportional when n is large."
- **incremental method**: Algorithm design where elements are processed one by one, inserting each into its proper place.
- **divide-and-conquer**: Algorithm design that breaks problem into subproblems, solves recursively, combines solutions.
- **recursive algorithm**: An algorithm that calls itself on smaller subproblems.
- **base case**: Smallest instance solved directly without recursion.
- **recursive case**: Case that requires recursive calls.
- **recurrence (recurrence equation)**: Equation describing running time in terms of smaller inputs.

### Processes / Algorithms / Pathways

##### INSERTION-SORT (A, n)
- **Goal**: Sort array A[1:n] in monotonically increasing order.
- **Input**: Array A[1:n] of n numbers.
- **Output**: A[1:n] sorted.
- **Steps**:
  1. for i = 2 to n
  2.     key = A[i]
  3.     // Insert A[i] into sorted subarray A[1:i-1]
  4.     j = i - 1
  5.     while j > 0 and A[j] > key
  6.         A[j+1] = A[j]
  7.         j = j - 1
  8.     A[j+1] = key
- **Pseudocode**: See above.
- **Complexity**: Best-case Θ(n) (already sorted), worst-case Θ(n²) (reverse sorted), average-case Θ(n²).
- **Correctness proof**: Loop invariant — at start of each for loop iteration, subarray A[1:i-1] contains elements originally in A[1:i-1] but in sorted order.
  - **Initialization**: i=2, A[1:1] is trivially sorted.
  - **Maintenance**: Inner while loop shifts elements right to make room; after insertion, A[1:i] is sorted. Incrementing i preserves invariant.
  - **Termination**: i=n+1, so A[1:n] is sorted.

##### Linear Search (Exercise 2.1-4)
- **Goal**: Find value x in array A[1:n].
- **Steps**: Scan from beginning to end, compare each element to x.
- **Loop invariant**: At start of each iteration, x is not in A[1:i-1].

##### MERGE (A, p, q, r)
- **Goal**: Merge two adjacent sorted subarrays A[p:q] and A[q+1:r] into sorted A[p:r].
- **Input**: Array A, indices p ≤ q < r, subarrays A[p:q] and A[q+1:r] sorted.
- **Output**: A[p:r] sorted.
- **Steps**:
  1. nL = q - p + 1; nR = r - q
  2. Create L[0:nL-1] and R[0:nR-1]
  3. Copy A[p:q] into L, A[q+1:r] into R
  4. i=0; j=0; k=p
  5. while i < nL and j < nR:
  6.     if L[i] ≤ R[j]: A[k]=L[i]; i++
  7.     else: A[k]=R[j]; j++
  8.     k++
  9. Copy remainder of L or R into A
- **Complexity**: Θ(n) where n = r-p+1

##### MERGE-SORT (A, p, r)
- **Goal**: Sort subarray A[p:r].
- **Steps**:
  1. if p ≥ r: return
  2. q = ⌊(p+r)/2⌋
  3. MERGE-SORT(A, p, q)
  4. MERGE-SORT(A, q+1, r)
  5. MERGE(A, p, q, r)
- **Pseudocode**: See above.
- **Complexity**: Θ(n lg n) worst-case
- **Initial call**: MERGE-SORT(A, 1, n)

##### BUBBLESORT (Problem 2-2)
- Repeatedly swap adjacent out-of-order elements.
- Worst-case: Θ(n²)

##### Selection Sort (Exercise 2.2-2)
- Repeatedly find smallest element in remaining unsorted portion and swap into position.
- Worst-case: Θ(n²), best-case: Θ(n²) (no improvement).

##### Binary Search (Exercise 2.3-6)
- On sorted array, repeatedly compare to midpoint and eliminate half.
- Worst-case: Θ(lg n)

##### Horner's Rule (Problem 2-3)
- Evaluate polynomial P(x) = ∑ᵢ₌₀ⁿ aᵢxⁱ using: P(x) = a₀ + x(a₁ + x(a₂ + ... + x(a_{n-1} + xa_n)...))
- Θ(n) time vs naive Θ(n²)

### Formulas & Equations

**Running time of INSERTION-SORT**:
- Best case: T(n) = c₁n + (c₂ + c₄ + c₅ + c₈)(n-1) = an + b = Θ(n)
- Worst case: T(n) = (c₅/2 + c₆/2 + c₇/2)n² + (c₁ + c₂ + c₄ + c₅/2 - c₆/2 - c₇/2 + c₈)n - (c₂ + c₄ + c₅ + c₈) = an² + bn + c = Θ(n²)

**Merge sort recurrence**:
- T(n) = Θ(1) if n = 1
- T(n) = 2T(n/2) + Θ(n) if n > 1
- Solution: T(n) = Θ(n lg n)
- (With detailed form: T(n) = 2T(n/2) + c₂n, base T(1) = c₁)
- Recursion tree: lg n + 1 levels; each level costs c₂n; leaf level costs c₁n; total = c₂n lg n + c₁n = Θ(n lg n)

**General divide-and-conquer recurrence**:
- T(n) = Θ(1) if n < n₀ (base case)
- T(n) = aT(n/b) + D(n) + C(n) if n ≥ n₀
- Where a = number of subproblems, n/b = size of each, D(n) = divide time, C(n) = combine time

**Factorial**: n! = n × (n-1) × (n-2) × ... × 1

### Comparisons & Trade-offs

| Dim | Insertion Sort | Merge Sort |
|-----|---------------|------------|
| Worst-case | Θ(n²) | Θ(n lg n) |
| Best-case | Θ(n) | Θ(n lg n) |
| In-place | Yes | No (uses extra arrays) |
| Method | Incremental | Divide-and-conquer |
| Small inputs | Faster (lower constants) | Slower |

### Design Paradigms

- **Incremental method**: Insertion sort — process elements one at a time, maintaining sorted prefix.
- **Divide-and-conquer**: Merge sort — divide into subproblems, solve recursively, combine.

### Edge Cases / Traps

- **Already sorted array**: Insertion sort runs in Θ(n) (best case); merge sort still runs in Θ(n lg n).
- **Reverse sorted array**: Insertion sort worst-case Θ(n²).
- **Single element**: Already sorted; base case of recursion.
- **Empty subarray**: If p > r, subarray is empty — MERGE-SORT test "if p ≥ r" handles this.
- **Off-by-one**: In MERGE, subarray A[p:q] has length q-p+1; A[q+1:r] has length r-q.

### End-of-Chapter Material

**2.1-1** Insertion sort on ⟨31, 41, 59, 26, 41, 58⟩:
- i=2: key=41, compare 31≤41 → ⟨31,41,59,26,41,58⟩
- i=3: key=59, compare 41≤59 → ⟨31,41,59,26,41,58⟩
- i=4: key=26, shift 59,41,31 → ⟨26,31,41,59,41,58⟩
- i=5: key=41, shift 59 → ⟨26,31,41,41,59,58⟩
- i=6: key=58, shift 59 → ⟨26,31,41,41,58,59⟩

**2.1-2** SUM-ARRAY: Loop invariant — at start of each iteration i, sum = sum of A[1:i-1]. Initialization: sum=0, i=1, A[1:0] empty sum=0 ✓. Maintenance: sum += A[i]. Termination: i=n+1, sum = sum of all elements.

**2.1-3** Decreasing insertion sort: change line 5 to `while j > 0 and A[j] < key`.

**2.1-4** Linear search pseudocode:
```
LINEAR-SEARCH(A, n, x)
1 for i = 1 to n
2     if A[i] == x
3         return i
4 return NIL
```
Loop invariant: A[1:i-1] does not contain x.

**2.1-5** Binary addition:
```
ADD-BINARY-INTEGERS(A, B, n)
1 carry = 0
2 for i = 0 to n-1
3     sum = A[i] + B[i] + carry
4     C[i] = sum mod 2
5     carry = sum div 2
6 C[n] = carry
7 return C
```

**2.2-1** n³/1000 + 100n² - 100n + 3 = Θ(n³)

**2.2-2** Selection sort:
```
SELECTION-SORT(A, n)
1 for i = 1 to n-1
2     min = i
3     for j = i+1 to n
4         if A[j] < A[min]
5             min = j
6     swap A[i] with A[min]
```
Only n-1 elements needed because after placing first n-1, the last element is in correct position. Worst-case Θ(n²). Best-case Θ(n²) — no improvement.

**2.2-3** Linear search: average-case: (n+1)/2 elements checked = Θ(n). Worst-case: n elements = Θ(n).

**2.2-4** Check if already sorted at start; if so, output immediately (Θ(n) best-case).

**2.3-1** Merge sort on ⟨3,41,52,26,38,57,9,49⟩:
- Divide: [3,41,52,26] [38,57,9,49]
- Divide: [3,41] [52,26] [38,57] [9,49]
- Divide: [3][41] [52][26] [38][57] [9][49]
- Merge: [3,41] [26,52] [38,57] [9,49]
- Merge: [3,26,41,52] [9,38,49,57]
- Merge: [3,9,26,38,41,49,52,57]

**2.3-2** Test "if p ≥ r" vs "if p ≠ r": If called initially with n≥1, p starts at 1, r=n. Since q=⌊(p+r)/2⌋, we have p≤q<r, so recursive calls have p≤q and q+1≤r. The subarrays always have at least one element, so p>r never occurs.

**2.3-3** Loop invariant for MERGE while loop (lines 12-18): At start of each iteration, subarray A[p:k-1] contains the k-p smallest elements of L[0:nL-1] and R[0:nR-1] in sorted order, and L[i] and R[j] are the smallest elements of their respective arrays not yet copied back.

**2.3-4** Prove T(n) = n lg n for recurrence T(n)=2T(n/2)+n, T(1)=0 (or Θ(1)). Base: n=1, T(1)=0=1·lg1. Inductive step: T(2n)=2T(n)+2n=2(n lg n)+2n=2n(lg n+1)=2n lg(2n). (If using constant base c₁, show T(n)=c₁n + c₂n lg n.)

**2.3-5** Recursive insertion sort:
```
RECURSIVE-INSERTION-SORT(A, n)
1 if n > 1
2     RECURSIVE-INSERTION-SORT(A, n-1)
3     key = A[n]
4     j = n-1
5     while j > 0 and A[j] > key
6         A[j+1] = A[j]
7         j = j-1
8     A[j+1] = key
```
Recurrence: T(n) = T(n-1) + Θ(n) → T(n) = Θ(n²)

**2.3-6** Binary search:
```
BINARY-SEARCH(A, n, v)
1 lo = 1; hi = n
2 while lo ≤ hi
3     mid = ⌊(lo+hi)/2⌋
4     if A[mid] == v: return mid
5     if A[mid] < v: lo = mid+1
6     else: hi = mid-1
7 return NIL
```
Worst-case: Θ(lg n). Using binary search in insertion sort does NOT improve to Θ(n lg n) because shifting elements still takes Θ(n) per element.

**2.3-7** Two-sum algorithm:
```
TWO-SUM(S, n, x)
1 MERGE-SORT(S, n) // Θ(n lg n)
2 for i = 1 to n
3     if BINARY-SEARCH(S, n, x-S[i]) returns index j where j ≠ i
4         return (i, j)
5 return NIL
```
Total: Θ(n lg n).

**Problem 2-1 (Insertion sort on small arrays in merge sort)**:
a. Insertion sort on n/k lists of size k: each list Θ(k²), n/k lists → Θ(nk).
b. Merging n/k lists: merge tree has lg(n/k) levels, each level Θ(n) → Θ(n lg(n/k)).
c. For same running time as standard merge sort: Θ(nk + n lg(n/k)) = Θ(n lg n) → k = O(lg n).
d. In practice, choose k where insertion sort outperforms merge sort on small arrays (typically 10-50).

**Problem 2-2 (Bubblesort)**:
a. BUBBLESORT terminates with A'[1] ≤ A'[2] ≤ ... ≤ A'[n]. Need to prove A' is a permutation of original A.
b. Inner loop invariant: After inner loop iteration j, A[j] is the minimum of A[j:n] (for descending j).
c. Outer loop invariant: After i-1 iterations, A[1:i-1] contains the i-1 smallest elements in sorted order.
d. Worst-case: Θ(n²). Comparable to insertion sort but with more swaps on average.

**Problem 2-3 (Horner's rule)**:
a. Θ(n).
b. Naive: for i=0..n, compute term = a_i; for j=1..i, term *= x; sum += term. Θ(n²).
c. Loop invariant: At start of iteration i, p = ∑_{k=0}^{n-(i+1)} a_{k+i+1}·x^{k}. At termination i=-1 (or i=0 before loop), p = ∑_{k=0}^{n} a_k·x^k = P(x).

**Problem 2-4 (Inversions)**:
a. Inversions in ⟨2,3,8,6,1⟩: (1,5), (2,5), (3,4), (3,5), (4,5) — 5 inversions.
b. Array ⟨n, n-1, ..., 1⟩ has most inversions: n(n-1)/2.
c. Running time of insertion sort = Θ(n + d) where d = number of inversions. Each swap eliminates one inversion.
d. Count inversions by modifying merge sort: during merge, when R[j] < L[i], add (nL - i) inversions. Θ(n lg n).

---

## Ch. 3 — Characterizing Running Times

### Named Entities (Terms & Definitions)

- **asymptotic efficiency**: How running time increases with input size in the limit as input size grows without bound.
- **O-notation (big-oh)**: Asymptotic upper bound. f(n) = O(g(n)) means f(n) grows no faster than g(n) (to within constant factor).
- **Ω-notation (big-omega)**: Asymptotic lower bound. f(n) grows at least as fast as g(n).
- **Θ-notation (theta)**: Asymptotically tight bound. f(n) grows at exactly the rate of g(n) (to within constant factors).
- **o-notation (little-oh)**: Upper bound that is NOT asymptotically tight.
- **ω-notation (little-omega)**: Lower bound that is NOT asymptotically tight.
- **asymptotically nonnegative**: f(n) ≥ 0 for all sufficiently large n.
- **asymptotically positive**: f(n) > 0 for all sufficiently large n.
- **asymptotically smaller/larger**: f is asymptotically smaller than g if f = o(g); larger if f = ω(g).
- **monotonically increasing**: m ≤ n ⇒ f(m) ≤ f(n).
- **monotonically decreasing**: m ≤ n ⇒ f(m) ≥ f(n).
- **strictly increasing**: m < n ⇒ f(m) < f(n).
- **floor (⌊x⌋)**: Greatest integer ≤ x.
- **ceiling (⌈x⌉)**: Least integer ≥ x.
- **modular arithmetic**: a mod n = remainder of a/n; a ≡ b (mod n) if (a mod n) = (b mod n).
- **polynomial**: p(n) = ∑ᵢ₌₀ᵈ aᵢnⁱ, with a_d ≠ 0; asymptotically positive if a_d > 0.
- **polynomially bounded**: f(n) = O(n^k) for some constant k.
- **polylogarithmically bounded**: f(n) = O(lg^k n) for some constant k.
- **exponential**: Function of form aⁿ with a > 1.
- **factorial (n!)**: n! = 1·2·3·...·n.
- **iterated logarithm (lg* n)**: Number of times lg must be applied to reduce n to ≤ 1.
- **Fibonacci numbers**: F₀=0, F₁=1, F_i = F_{i-1} + F_{i-2} for i ≥ 2.
- **golden ratio (ϕ)**: ϕ = (1+√5)/2 ≈ 1.618; ϕ̂ = (1-√5)/2 ≈ -0.618.
- **Stirling's approximation**: n! = √(2πn)(n/e)ⁿ(1+Θ(1/n)).
- **watershed function**: n^{log_b a} in master theorem.

### Formulas & Equations

##### O-notation (formal)
O(g(n)) = {f(n): ∃ positive constants c, n₀ such that 0 ≤ f(n) ≤ c·g(n) for all n ≥ n₀}

##### Ω-notation (formal)
Ω(g(n)) = {f(n): ∃ positive constants c, n₀ such that 0 ≤ c·g(n) ≤ f(n) for all n ≥ n₀}

##### Θ-notation (formal)
Θ(g(n)) = {f(n): ∃ positive constants c₁, c₂, n₀ such that 0 ≤ c₁·g(n) ≤ f(n) ≤ c₂·g(n) for all n ≥ n₀}

##### o-notation (formal)
o(g(n)) = {f(n): ∀ positive constants c > 0, ∃ n₀ > 0 such that 0 ≤ f(n) < c·g(n) for all n ≥ n₀}

##### ω-notation (formal)
ω(g(n)) = {f(n): ∀ positive constants c > 0, ∃ n₀ > 0 such that 0 ≤ c·g(n) < f(n) for all n ≥ n₀}

##### Theorem 3.1
f(n) = Θ(g(n)) iff f(n) = O(g(n)) and f(n) = Ω(g(n))

##### Limit characterizations
- f(n) = o(g(n)) iff lim_{n→∞} f(n)/g(n) = 0
- f(n) = ω(g(n)) iff lim_{n→∞} f(n)/g(n) = ∞

##### Transitivity
- f = Θ(g) and g = Θ(h) ⇒ f = Θ(h)
- f = O(g) and g = O(h) ⇒ f = O(h)
- f = Ω(g) and g = Ω(h) ⇒ f = Ω(h)

##### Reflexivity
f = Θ(f), f = O(f), f = Ω(f)

##### Symmetry
f = Θ(g) iff g = Θ(f)

##### Transpose symmetry
- f = O(g) iff g = Ω(f)
- f = o(g) iff g = ω(f)

##### Floor/ceiling properties
- ⌈x⌉ - 1 < x ≤ ⌈x⌉ ≤ x + 1
- ⌊x⌋ - 1 < x ≤ ⌊x⌋ ≤ x + 1
- ⌊n/2⌋ + ⌈n/2⌉ = n for integer n
- For real x ≥ 0 and integers a,b > 0: ⌈⌈x/a⌉/b⌉ = ⌈x/(ab)⌉ and ⌊⌊x/a⌋/b⌋ = ⌊x/(ab)⌋

##### Polynomials
- p(n) = ∑ᵢ₌₀ᵈ aᵢnⁱ with a_d > 0 ⇒ p(n) = Θ(n^d)

##### Exponentials
- a⁰ = 1, a¹ = a, a⁻¹ = 1/a
- (a^m)^n = a^{mn}
- a^m a^n = a^{m+n}
- For a > 1, b: lim_{n→∞} n^b / a^n = 0 (exponential dominates polynomial)
- e = 2.71828...; e^x = ∑_{k=0}^∞ x^k/k! ≥ 1+x (equality only at x=0)
- For |x| ≤ 1: 1 + x ≤ e^x ≤ 1 + x + x²
- As x → 0: e^x = 1 + x + Θ(x²)

##### Logarithms
- lg n = log₂ n (binary), ln n = log_e n (natural)
- lg^k n = (lg n)^k, lg lg n = lg(lg n)
- log_b n undefined for n ≤ 0; strictly increasing for n > 0
- a = b^{log_b a}, log_c(ab) = log_c a + log_c b
- log_b a^n = n log_b a
- log_b a = log_c a / log_c b (change of base)
- log_b(1/a) = -log_b a
- a^{log_b c} = c^{log_b a}
- For x > -1: x/(1+x) ≤ ln(1+x) ≤ x (equality only at x=0)
- ln(1+x) = x - x²/2 + x³/3 - x⁴/4 + ...
- For any constants a>0, b: lim_{n→∞} lg^b n / n^a = 0 (polynomial dominates polylogarithm)

##### Factorial
- n! = 1·2·3·...·n, with 0! = 1
- n! ≤ nⁿ (weak bound)
- Stirling's approximation: n! = √(2πn)(n/e)ⁿ(1 + Θ(1/n))
- n! = o(nⁿ), n! = ω(2ⁿ), lg(n!) = Θ(n lg n)

##### Iterated logarithm (lg* n)
- lg* n = min{i ≥ 0: lg^(i) n ≤ 1}
- lg* 2 = 1, lg* 4 = 2, lg* 16 = 3, lg* 65536 = 4, lg* 2⁶⁵⁵³⁶ = 5
- Extremely slow-growing; rarely exceeds 5 for practical inputs.

##### Fibonacci numbers
- F₀ = 0, F₁ = 1, F_i = F_{i-1} + F_{i-2} for i ≥ 2
- ϕ² = ϕ + 1 (golden ratio equation)
- ϕ = (1+√5)/2, ϕ̂ = (1-√5)/2
- F_i = (ϕⁱ - ϕ̂ⁱ)/√5
- F_i = ⌊ϕⁱ/√5 + 1/2⌋ (nearest integer to ϕⁱ/√5)
- Fibonacci numbers grow exponentially.

### Comparisons (Analogy with Real Numbers)

| Asymptotic | Real Numbers |
|-----------|-------------|
| f = O(g) | a ≤ b |
| f = Ω(g) | a ≥ b |
| f = Θ(g) | a = b |
| f = o(g) | a < b |
| f = ω(g) | a > b |

**Note**: Trichotomy does NOT hold for asymptotic notation — not all functions are asymptotically comparable (e.g., n vs n^{1+sin n}).

### Edge Cases / Traps

- **Θ(n²) ≠ O(n²)**: Θ is tight bound; O is only upper bound. "Insertion sort runs in Θ(n²)" is wrong as blanket statement (best case is Θ(n)).
- **Asymptotically nonnegative**: Required for all notations; O(g(n)) is empty if g negative.
- **o vs O**: o is strictly looser bound than O. 2n = O(n²) but also 2n = o(n²); 2n² ≠ o(n²).
- **Gap between cases**: Master theorem has gaps (e.g., f(n) = n/lg n falls in gap between cases 1 and 2).
- **Anonymous functions**: In 2n² + Θ(n) = Θ(n²), the Θ(n) on LHS and Θ(n²) on RHS represent (possibly different) anonymous functions.
- **Constants hidden**: When using substitution method, must use explicit constants, not asymptotic notation in inductive hypothesis.

### End-of-Chapter Material

**3.1-1** Modify lower bound for non-multiple-of-3: use ⌊n/3⌋ largest values in first ⌊n/3⌋ positions. The middle ⌈n/3⌉ positions are passed through by at least ⌊n/3⌋ values, giving Ω(n²).

**3.1-2** Selection sort: Θ(n²) — doubly nested loops, each roughly n iterations.

**3.1-3** Generalization with α: αn largest values start in first αn positions. Each must pass through middle (1-2α)n positions. Need α < 1/2 for middle to be non-empty. The number of passes = α(1-2α)n². Maximized when α = 1/4.

**3.2-1** max(f,g) ≤ f+g, so max(f,g) = O(f+g). Also max(f,g) ≥ (f+g)/2 (since both nonnegative), so max(f,g) = Ω(f+g). Thus max(f,g) = Θ(f+g).

**3.2-2** "Running time is at least O(n²)" is meaningless because O is an upper bound, not lower. "At least" suggests a lower bound, conflicting with O's upper bound meaning.

**3.2-3** 2^{n+1} = 2·2ⁿ = O(2ⁿ). 2^{2n} = (2ⁿ)² ≠ O(2ⁿ) since ratio is 2ⁿ which is unbounded.

**3.2-4** Proof of Theorem 3.1: (⇒) If f=Θ(g), then ∃c₁,c₂,n₀: c₁g≤f≤c₂g. Then f≤c₂g so f=O(g); c₁g≤f so f=Ω(g). (⇐) If f=O(g) and f=Ω(g), then ∃c₂,n₂: f≤c₂g for n≥n₂ and ∃c₁,n₁: c₁g≤f for n≥n₁. Let n₀=max(n₁,n₂). Then c₁g≤f≤c₂g, so f=Θ(g).

**3.2-5** Running time is Θ(g(n)) iff worst-case = O(g(n)) and best-case = Ω(g(n)). Proof: T_worst(n) = max_{input of size n} T(n), T_best(n) = min_{input of size n} T(n). If T(n)=Θ(g(n)) then ∀inputs: c₁g≤T≤c₂g, so T_worst=O(g), T_best=Ω(g). Conversely, if T_worst=O(g) and T_best=Ω(g), then ∃c₁,c₂: T_best≥c₁g and T_worst≤c₂g, so c₁g≤T_best≤T(n)≤T_worst≤c₂g, hence T(n)=Θ(g(n)).

**3.2-6** o(g) ∩ ω(g) = ∅. If f∈o(g), then lim f/g = 0. If f∈ω(g), then lim f/g = ∞. Both cannot hold simultaneously.

**3.2-7** Ω(g(n,m)) = {f(n,m): ∃c,n₀,m₀: 0 ≤ c·g(n,m) ≤ f(n,m) for all n≥n₀ or m≥m₀}. Θ(g(n,m)) = {f(n,m): ∃c₁,c₂,n₀,m₀: 0 ≤ c₁·g(n,m) ≤ f(n,m) ≤ c₂·g(n,m) for all n≥n₀ or m≥m₀}.

**3.3-1** If f,g monotonically increasing: (f+g)(m) = f(m)+g(m) ≤ f(n)+g(n) = (f+g)(n). (f∘g)(m) = f(g(m)) ≤ f(g(n)) = (f∘g)(n). If nonnegative: (f·g)(m) ≤ (f·g)(n).

**3.3-2** ⌊αn⌋ + ⌈(1-α)n⌉ = n. Let αn = ⌊αn⌋ + r where 0≤r<1. Then (1-α)n = n - αn = n - ⌊αn⌋ - r. So ⌈(1-α)n⌉ = n - ⌊αn⌋ (since -r makes it ceiling up). Sum = n.

**3.3-3** (n+o(n))^k = n^k + k·n^{k-1}·o(n) + ... = n^k + o(n^k) = Θ(n^k). Hence ⌈n⌉^k = Θ(n^k) and ⌊n⌋^k = Θ(n^k).

**3.3-4** Equation (3.21): a^{log_b c} = c^{log_b a}. Take logs: log_b(a^{log_b c}) = log_b c·log_b a; log_b(c^{log_b a}) = log_b a·log_b c. Equal.
Equations (3.26)-(3.28): Stirling: n! = √(2πn)(n/e)^n(1+Θ(1/n)). lg(n!) = Θ(n lg n).

**3.3-5** ⌈lg n⌉! is NOT polynomially bounded (grows faster than any polynomial). ⌈lg lg n⌉! IS polynomially bounded (it's O(lg n) which is O(n^ε) for any ε>0).

**3.3-6** lg(lg* n) and lg*(lg n): Let m = lg n. Then lg*(lg n) = lg* m. And lg(lg* n) = lg(lg* 2^m). Since lg* 2^m = lg* m + 1, we have lg(lg* n) = lg(lg* m + 1) ≈ lg(lg* m). Compare: lg(lg* n) grows as lg(lg* n) while lg*(lg n) grows as lg* m. lg* grows much faster than lg, so lg*(lg n) = lg* m is asymptotically larger than lg(lg* n) ≈ lg(lg* m).

**3.3-7** ϕ = (1+√5)/2 and ϕ̂ = (1-√5)/2: ϕ² = (3+√5)/2 = (1+√5)/2 + 1 = ϕ + 1. Similarly ϕ̂² = ϕ̂ + 1.

**3.3-8** F_i = (ϕⁱ - ϕ̂ⁱ)/√5. Base: i=0: (1-1)/√5=0✓; i=1: (ϕ-ϕ̂)/√5 = (√5)/√5 = 1✓. Inductive: assume for i-1,i. F_{i+1}=F_i+F_{i-1} = (ϕⁱ-ϕ̂ⁱ+ϕ^{i-1}-ϕ̂^{i-1})/√5 = (ϕ^{i-1}(ϕ+1)-ϕ̂^{i-1}(ϕ̂+1))/√5 = (ϕ^{i-1}ϕ²-ϕ̂^{i-1}ϕ̂²)/√5 = (ϕ^{i+1}-ϕ̂^{i+1})/√5.

**3.3-9** k lg k = Θ(n) implies k = Θ(n/lg n). Suppose k = cn/lg n for some c. Then k lg k = (cn/lg n)·lg(cn/lg n) = (cn/lg n)(lg n + lg c - lg lg n) = cn(1 + o(1)) = Θ(n). So n = Θ(k lg k) ⇒ k = Θ(n/lg n).

---

## Ch. 4 — Divide-and-Conquer

### Named Entities (Terms & Definitions)

- **recurrence**: An equation describing a function in terms of its value on smaller arguments.
- **algorithmic recurrence**: A recurrence where for all n < n₀, T(n) = Θ(1), and every recursion path terminates in finite steps.
- **substitution method**: Guess form of solution, prove by induction.
- **recursion-tree method**: Model recurrence as tree, sum costs per level.
- **master method**: Cookbook method for recurrences of form T(n) = aT(n/b) + f(n).
- **Akra-Bazzi method**: General method for recurrences with differently-sized subproblems.
- **driving function (f(n))**: The non-recursive part of a master recurrence.
- **watershed function (n^{log_b a})**: The function compared against f(n) in master theorem.
- **regularity condition**: af(n/b) ≤ cf(n) for some c < 1 (required for master theorem case 3).
- **polynomial-growth condition**: f(Θ(n)) = Θ(f(n)) in a strong sense; required for ignoring floors/ceilings in Akra-Bazzi recurrences.
- **Monge array**: Array where A[i,j] + A[k,l] ≤ A[i,l] + A[k,j] for all i<k, j<l.
- **dense matrix**: Matrix where most entries are nonzero.
- **sparse matrix**: Matrix where most entries are zero.

### Processes / Algorithms / Pathways

##### MATRIX-MULTIPLY (A, B, C, n) — naive
```
MATRIX-MULTIPLY(A, B, C, n)
1 for i = 1 to n
2     for j = 1 to n
3         for k = 1 to n
4             c_ij = c_ij + a_ik · b_kj
```
- **Complexity**: Θ(n³)

##### MATRIX-MULTIPLY-RECURSIVE (A, B, C, n)
```
MATRIX-MULTIPLY-RECURSIVE(A, B, C, n)
1 if n == 1
2     c₁₁ = c₁₁ + a₁₁ · b₁₁
3     return
4 partition A, B, C into n/2×n/2 submatrices
5 MATRIX-MULTIPLY-RECURSIVE(A₁₁, B₁₁, C₁₁, n/2)
6 MATRIX-MULTIPLY-RECURSIVE(A₁₁, B₁₂, C₁₂, n/2)
7 MATRIX-MULTIPLY-RECURSIVE(A₂₁, B₁₁, C₂₁, n/2)
8 MATRIX-MULTIPLY-RECURSIVE(A₂₁, B₁₂, C₂₂, n/2)
9 MATRIX-MULTIPLY-RECURSIVE(A₁₂, B₂₁, C₁₁, n/2)
10 MATRIX-MULTIPLY-RECURSIVE(A₁₂, B₂₂, C₁₂, n/2)
11 MATRIX-MULTIPLY-RECURSIVE(A₂₂, B₂₁, C₂₁, n/2)
12 MATRIX-MULTIPLY-RECURSIVE(A₂₂, B₂₂, C₂₂, n/2)
```
- **Recurrence**: T(n) = 8T(n/2) + Θ(1)
- **Solution**: T(n) = Θ(n³) (by master theorem case 1)
- Note: The partitioning equations are:
  - C₁₁ = A₁₁·B₁₁ + A₁₂·B₂₁
  - C₁₂ = A₁₁·B₁₂ + A₁₂·B₂₂
  - C₂₁ = A₂₁·B₁₁ + A₂₂·B₂₁
  - C₂₂ = A₂₁·B₁₂ + A₂₂·B₂₂

##### Strassen's Algorithm
- **Goal**: Multiply n×n matrices in o(n³) time.
- **Key insight**: Only 7 recursive multiplications instead of 8, at cost of 18 matrix additions/subtractions.

**Step 1**: Partition into n/2×n/2 submatrices (Θ(1) using index calculations).

**Step 2**: Create 10 sum/difference matrices S₁,...,S₁₀ (Θ(n²)):
- S₁ = B₁₂ − B₂₂
- S₂ = A₁₁ + A₁₂
- S₃ = A₂₁ + A₂₂
- S₄ = B₂₁ − B₁₁
- S₅ = A₁₁ + A₂₂
- S₆ = B₁₁ + B₂₂
- S₇ = A₁₂ − A₂₂
- S₈ = B₂₁ + B₂₂
- S₉ = A₁₁ − A₂₁
- S₁₀ = B₁₁ + B₁₂

**Step 3**: Recursively compute 7 products P₁,...,P₇ (7T(n/2)):
- P₁ = A₁₁·S₁ = A₁₁·B₁₂ − A₁₁·B₂₂
- P₂ = S₂·B₂₂ = A₁₁·B₂₂ + A₁₂·B₂₂
- P₃ = S₃·B₁₁ = A₂₁·B₁₁ + A₂₂·B₁₁
- P₄ = A₂₂·S₄ = A₂₂·B₂₁ − A₂₂·B₁₁
- P₅ = S₅·S₆ = A₁₁·B₁₁ + A₁₁·B₂₂ + A₂₂·B₁₁ + A₂₂·B₂₂
- P₆ = S₇·S₈ = A₁₂·B₂₁ + A₁₂·B₂₂ − A₂₂·B₂₁ − A₂₂·B₂₂
- P₇ = S₉·S₁₀ = A₁₁·B₁₁ + A₁₁·B₁₂ − A₂₁·B₁₁ − A₂₁·B₁₂

**Step 4**: Combine results (Θ(n²) with 12 matrix additions/subtractions):
- C₁₁ = C₁₁ + P₅ + P₄ − P₂ + P₆
- C₁₂ = C₁₂ + P₁ + P₂
- C₂₁ = C₂₁ + P₃ + P₄
- C₂₂ = C₂₂ + P₅ + P₁ − P₃ − P₇

- **Recurrence**: T(n) = 7T(n/2) + Θ(n²)
- **Solution**: T(n) = Θ(n^{lg 7}) = O(n^{2.81}) (by master theorem case 1)

### Formulas & Equations

##### General divide-and-conquer recurrence
T(n) = aT(n/b) + f(n)

##### Master Theorem (Theorem 4.1)
Let a > 0, b > 1 constants; f(n) driving function. T(n) = aT(n/b) + f(n) (with implicit floors/ceilings).

- **Case 1**: if ∃ε>0: f(n) = O(n^{log_b a - ε}) ⇒ T(n) = Θ(n^{log_b a})
- **Case 2**: if ∃k≥0: f(n) = Θ(n^{log_b a} lg^k n) ⇒ T(n) = Θ(n^{log_b a} lg^{k+1} n)
- **Case 3**: if ∃ε>0: f(n) = Ω(n^{log_b a + ε}) AND regularity condition af(n/b) ≤ cf(n) for some c<1 ⇒ T(n) = Θ(f(n))

##### Akra-Bazzi method
For T(n) = ∑ᵢ₌₁ᵏ aᵢT(n/bᵢ) + f(n):
Find p such that ∑ aᵢbᵢ^{-p} = 1.
Then T(n) = Θ(n^p(1 + ∫₁ⁿ f(u)/u^{p+1} du))

##### Example recurrences and solutions
| Recurrence | a | b | f(n) | n^{log_b a} | Case | Solution |
|-----------|----|----|-----|-------------|------|----------|
| Merge sort: T(n) = 2T(n/2) + n | 2 | 2 | n | n | 2 (k=0) | Θ(n lg n) |
| Matrix recursive: T(n) = 8T(n/2) + 1 | 8 | 2 | Θ(1) | n³ | 1 | Θ(n³) |
| Strassen: T(n) = 7T(n/2) + n² | 7 | 2 | n² | n^{lg7}≈n^{2.81} | 1 | Θ(n^{lg7}) |
| T(n) = 9T(n/3) + n | 9 | 3 | n | n² | 1 | Θ(n²) |
| T(n) = T(2n/3) + 1 | 1 | 3/2 | 1 | n^0=1 | 2 | Θ(lg n) |
| T(n) = 3T(n/4) + n lg n | 3 | 4 | n lg n | n^{log₄3}≈n^{0.79} | 3 | Θ(n lg n) |
| T(n) = 2T(n/2) + n lg n | 2 | 2 | n lg n | n | 2 (k=1) | Θ(n lg² n) |

##### Akra-Bazzi example
T(n) = T(n/5) + T(7n/10) + n (from selection algorithm, Ch. 9)
Find p: (1/5)^p + (7/10)^p = 1. Since p ∈ (0,1), solution T(n) = Θ(n).

### Comparisons & Trade-offs

| Algorithm | Recursions | Combine cost | Recurrence | Solution |
|-----------|-----------|-------------|------------|----------|
| Naive multiply | 8 subproblems | Θ(1) | 8T(n/2)+Θ(1) | Θ(n³) |
| Strassen | 7 subproblems | Θ(n²) | 7T(n/2)+Θ(n²) | Θ(n^{lg7}) = O(n^{2.81}) |

### Edge Cases / Traps

- **Master theorem gaps**: f(n) = n/lg n falls between cases 1 and 2 (not polynomially slower than n). f(n) = n lg n falls between cases 2 and 3 when comparing with n^{log_b a} if lg n is in the gap — actually case 2 does cover it with k=1.
- **Regularity condition**: Must hold for case 3. Counterexample: f(n) = 2^{⌈lg n⌉} satisfies f(n) = Ω(n^{log_b a + ε}) but fails regularity.
- **Floors and ceilings**: Can generally be ignored for master recurrences and for Akra-Bazzi recurrences whose driving function satisfies the polynomial-growth condition.
- **Algorithmic recurrence convention**: Base cases T(n) = Θ(1) for n < n₀ are implicit; asymptotic solution doesn't depend on choice of n₀.
- **Inequality recurrences**: T(n) ≤ 2T(n/2) + n ⇒ O(n lg n); T(n) ≥ 2T(n/2) + n ⇒ Ω(n lg n).

### End-of-Chapter Material

**4.1-1** Generalize for non-power-of-2: use ceil/floor for n/2. Recurrence: T(n) = T(⌈n/2⌉) + T(⌊n/2⌋) + ... Still Θ(n³) by master theorem with n/2 as approximation.

**4.1-2** k×n × n×k: each product is k×k; there are n²/k² such products? Actually: Multiply (kn × n) by (n × kn). The result is kn × kn. Using recursive algorithm, each half-sized problem is (kn/2 × n/2) × (n/2 × kn/2). Running time T(kn) = 8T(kn/2) + Θ(1) → Θ((kn)³) = Θ(k³n³). Similarly for n×kn × kn×n: also Θ(k³n³). Same asymptotic.

**4.1-3** If copying instead of index calculation: each partition copies Θ(n²) elements. Recurrence: T(n) = 8T(n/2) + Θ(n²). Master theorem case 1: n^{log₂8}=n³, f(n)=n²=O(n^{3-ε}) → Θ(n³). Same solution.

**4.1-4** Matrix addition:
```
MATRIX-ADD-RECURSIVE(A, B, C, n)
1 if n == 1
2     c₁₁ = a₁₁ + b₁₁
3 else partition into n/2×n/2 submatrices
4     MATRIX-ADD-RECURSIVE(A₁₁, B₁₁, C₁₁, n/2)
5     MATRIX-ADD-RECURSIVE(A₁₂, B₁₂, C₁₂, n/2)
6     MATRIX-ADD-RECURSIVE(A₂₁, B₂₁, C₂₁, n/2)
7     MATRIX-ADD-RECURSIVE(A₂₂, B₂₂, C₂₂, n/2)
```
Recurrence: T(n) = 4T(n/2) + Θ(1) → master case 1: n^{log₂4}=n², Θ(1)=O(n^{2-ε}) → Θ(n²). With Θ(n²) copying: T(n) = 4T(n/2) + Θ(n²) → master case 2: f(n)=Θ(n²)=Θ(n^{log₂4}) → Θ(n² lg n).

**4.2-1** Strassen: compute product of 2×2 matrices. Show S₁,...,S₁₀, then P₁,...,P₇, then combine.

**4.2-2** Pseudocode for Strassen: Follow the 4-step outline.

**4.2-3** Largest k for 3×3 multiplication: Need a such that T(n) = aT(n/3) + Θ(n²). Strassen gives n^{lg7} ≈ n^{2.81}. We need n^{log₃ a} < n^{lg7}. So log₃ a < lg 7 → a < 3^{lg7} = 7^{lg3} ≈ 7^{1.585} ≈ 22.85. So a ≤ 22. Running time: Θ(n^{log₃ a}). Since a > 3² = 9 (or thereabouts), we get various exponents.

**4.2-4** Pan's methods: 68×68 with 132464 mults → exponent = log_68(132464) ≈ 2.795. 70×70 with 143640 → log_70(143640) ≈ 2.794. 72×72 with 155424 → log_72(155424) ≈ 2.794. All slightly better than Strassen's 2.807.

**4.2-5** Complex multiplication: compute P₁=(a+b)(c+d)=ac+ad+bc+bd, P₂=ac, P₃=bd. Then ac-bd = P₂-P₃, ad+bc = P₁-P₂-P₃. Only 3 real multiplications.

**4.2-6** Squaring to multiplication: Use identity (A+B)² = A² + AB + BA + B². Compute (A+B)², A², B². Then AB = ((A+B)² - A² - B²)/2. Since squaring is Θ(n^α), multiplication is also Θ(n^α).

**4.3-1**
a. T(n) = T(n-1) + n: Guess T(n) = O(n²). Inductive: T(n) ≤ c(n-1)² + n = cn² - 2cn + c + n ≤ cn² for c ≥ 1, n large enough.
b. T(n) = T(n/2) + Θ(1): Guess O(lg n). T(n) ≤ c lg(n/2) + d = c lg n - c + d ≤ c lg n for c ≥ d.
c. T(n) = 2T(n/2) + n: Guess Θ(n lg n). Upper bound: T(n) ≤ 2c(n/2)lg(n/2) + n = cn lg n - cn + n ≤ cn lg n for c ≥ 1. Lower bound: similarly.
d. T(n) = 2T(n/2+17)+n: Guess O(n lg n). When n large, n/2+17 is close to n/2. T(n) ≤ 2c(n/2+17)lg(n/2+17)+n ≤ 2c·(n/2+17)lg(3n/4)+n for large n. Can show ≤ cn lg n for appropriate c.
e. T(n) = 2T(n/3) + Θ(n): Master case 3: n^{log₃2} ≈ n^{0.63}, f(n)=n = Ω(n^{0.63+ε}). Regularity: 2·(n/3)=2n/3 ≤ c·n for c=3/4. So Θ(n).
f. T(n) = 4T(n/2) + Θ(n): Master case 1: n^{log₂4}=n², f(n)=n=O(n^{2-ε}). So Θ(n²).

**4.3-2** T(n) = 4T(n/2) + n. Guess Θ(n²). Substitution T(n) ≤ cn²: T(n) ≤ 4c(n/2)² + n = cn² + n, which doesn't imply ≤ cn². Subtracting lower-order term: T(n) ≤ cn² - dn. Then T(n) ≤ 4(c(n/2)² - d(n/2)) + n = cn² - 2dn + n = cn² - dn - (dn - n) ≤ cn² - dn for d ≥ 1.

**4.3-3** T(n) = 2T(n-1) + 1. Guess O(2ⁿ). T(n) ≤ 2·c·2^{n-1} + 1 = c·2ⁿ + 1, doesn't close. Subtract: T(n) ≤ c·2ⁿ - d. Then T(n) ≤ 2(c·2^{n-1} - d) + 1 = c·2ⁿ - 2d + 1 ≤ c·2ⁿ - d when d ≥ 1.

**4.4-1**
a. T(n) = T(n/2) + n³: Tree height lg n. Root cost n³, then (n/2)³, (n/4)³... Sum = n³(1 + 1/8 + 1/64 + ...) = Θ(n³). Verify substitution: T(n) ≤ c(n/2)³ + n³ = (c/8+1)n³ ≤ cn³ for c ≥ 8/7.
b. T(n) = 4T(n/3) + n: Watershed n^{log₃4} ≈ n^{1.26}. Case 1: n = O(n^{1.26-ε}) → Θ(n^{log₃4}).
c. T(n) = 4T(n/2) + n: Watershed n^{log₂4}=n². Case 1: n = O(n^{2-ε}) → Θ(n²).
d. T(n) = 3T(n-1) + 1: Tree height n, each level has 3× nodes, leaf level has 3^{n-1} nodes, total = Θ(3ⁿ).

**4.4-2** L(n) = L(n/3) + L(2n/3), base L(n)=1 for n<n₀. Lower bound: L(n) ≥ c·n. L(n) ≥ c·n/3 + c·2n/3 = c·n. Base: c=1 works. So L(n)=Ω(n). With upper bound L(n)=O(n) shown in text, L(n)=Θ(n).

**4.4-3** T(n) = T(n/3) + T(2n/3) + cn. Prove T(n) = Ω(n lg n). T(n) ≥ c·n + c·n/3·lg(n/3) + c·2n/3·lg(2n/3) = ... ≥ d·n lg n for some d. Combined with upper bound O(n lg n) → Θ(n lg n).

**4.4-4** T(n) = T(αn) + T((1-α)n) + Θ(n). By symmetry, guess Θ(n lg n). Recursion tree has longest path from root through (1-α) splits.

**4.5-1**
a. T(n) = 2T(n/4) + 1: n^{log₄2}=n^{0.5}. Case 1: 1=O(n^{0.5-ε}) → Θ(√n).
b. T(n) = 2T(n/4) + √n: n^{0.5}. Case 2 (k=0): Θ(√n lg n).
c. T(n) = 2T(n/4) + n^{0.51}: n^{0.5}, f(n)=n^{0.51}=Ω(n^{0.5+ε}). Regularity: 2·(n/4)^{0.51} = 2·n^{0.51}/4^{0.51} = 2·n^{0.51}/2^{1.02} = n^{0.51}/2^{0.02} ≈ 0.986·n^{0.51} ≤ c·n^{0.51} for c=0.986<1. Case 3: Θ(n^{0.51}).
d. T(n) = 2T(n/4) + n: n^{0.5}. f(n)=n = Ω(n^{0.5+ε}). Regularity: 2·(n/4)=n/2 ≤ c·n for c=1/2. Case 3: Θ(n).
e. T(n) = 2T(n/4) + n²: n^{0.5}. f(n)=n²=Ω(n^{0.5+ε}). Regularity: 2·(n/4)²=n²/8 ≤ c·n² for c=1/8. Case 3: Θ(n²).

**4.5-2** Professor Caesar: each matrix divided into n/4 × n/4 submatrices. Watershed: n^{log₄ a}. Strassen: n^{lg7} ≈ n^{2.807}. Need n^{log₄ a} < n^{lg7} → log₄ a < lg7 → a < 4^{lg7} = 7^{lg4} = 7² = 49. So largest integer a ≤ 48. (Since log₄ 49 ≈ 2.807.)

**4.5-3** Binary search: T(n) = T(n/2) + Θ(1). Watershed: n^{log₂1}=n⁰=1. Case 2 (k=0): Θ(lg n).

**4.5-4** f(n)=lg n. Regularity: af(n/b) ≤ cf(n) with a=1, b=2: lg(n/2) ≤ c lg n → lg n - 1 ≤ c lg n → 1 - 1/lg n ≤ c. For n large, 1 - 1/lg n → 1, so no c < 1 works. For case 3 condition: f(n)=Ω(n^{log_b a+ε})=Ω(n^ε). But lg n ≠ Ω(n^ε) for any ε>0.

**4.5-5** f(n) = 2^{⌈lg n⌉}. For any n, f(n) ≈ n (varies by factor 2). Show fails regularity: af(n/b) ≤ cf(n). With a,b chosen: 2^{⌈lg n/b⌉} ≤ c·2^{⌈lg n⌉}. The jumps at powers of 2 violate this.

**4.6-1** Show ∑_{j=0}^{⌊log_b n⌋} a^j lg^k(n/b^j) = Θ(n^{log_b a} lg^{k+1} n).

**4.6-2** Case 3 condition f(n) = Ω(n^{log_b a + ε}) is implied by the regularity condition. Proof: If af(n/b) ≤ cf(n), then f(n) ≥ (a/c)f(n/b) ≥ ... ≥ (a/c)^j f(n/b^j). Setting n/b^j = n₀ gives f(n) ≥ (a/c)^{log_b(n/n₀)}·Θ(1) = Θ(n^{log_b(a/c)}) = Ω(n^{log_b a + δ}) where δ = -log_b c > 0 since c < 1.

**4.6-3** For f(n) = n/lg n with a=2,b=2: Show ∑ a^j f(n/b^j) = Θ(n lg lg n). Then T(n) = Θ(n) + Θ(n lg lg n) = Θ(n lg lg n).

**4.7-1** If T satisfies T(n) = ∑ aᵢT(n/bᵢ) + f(n), then T'(n) = cT(n) satisfies T'(n) = ∑ aᵢT'(n/bᵢ) + c·f(n). So any constant factor on f can be absorbed by scaling initial conditions.

**4.7-2** f(n)=n² satisfies polynomial-growth: for any ϕ≥1, f(ψn)/f(n) = ψ², and 1≤ψ≤ϕ means 1≤ψ²≤ϕ², so d can be ϕ². f(n)=2ⁿ fails: f(ψn)/f(n) = 2^{(ψ-1)n} which is unbounded for fixed ψ>1 as n→∞.

**4.7-3** f satisfies polynomial-growth: for any ϕ≥1, f(ψn) ≥ f(n)/d. Take ϕ=1, ψ=1, we get f(n) ≥ f(n)/d. For large n, f(n) positive since d>1 and f(n) nonnegative.

**4.7-4** Example: f(n) = n^{1+sin n}. Then f(Θ(n)) can be Θ(f(n)) because the oscillation is scale-invariant, but polynomial-growth fails because near sin n = -1, f(ψn) can be much larger relative to f(n).

**4.7-5** Akra-Bazzi solutions:
a. T(n)=T(n/2)+T(n/3)+T(n/6)+n lg n: (1/2)^p+(1/3)^p+(1/6)^p=1 → p=1. ∫₁ⁿ (u lg u)/u² du = Θ(lg² n). T(n)=Θ(n) + Θ(n lg² n)=Θ(n lg² n).
b. T(n)=3T(n/3)+8T(n/4)+n²/lg n: 3·(1/3)^p+8·(1/4)^p=1 → p≈1. etc.
c-g: Similar approach.

---

## Ch. 5 — Probabilistic Analysis and Randomized Algorithms

### Named Entities (Terms & Definitions)

- **probabilistic analysis**: Using probability theory to analyze problems/algorithms, computing expected behavior under assumed input distribution.
- **average-case running time**: Expected running time over a distribution of inputs.
- **randomized algorithm**: Algorithm whose behavior depends on both input and values produced by a random-number generator.
- **expected running time**: Running time expectation over the algorithm's own random choices (contrast with average-case).
- **indicator random variable**: I{A} = 1 if event A occurs, 0 otherwise. E[I{A}] = Pr{A}.
- **uniform random permutation**: A permutation of n elements where each of the n! permutations is equally likely.
- **random-number generator RANDOM(a,b)**: Returns integer between a and b inclusive, each equally likely, independent of previous calls.
- **birthday paradox**: With only 23 people in a room, probability ≥ 1/2 that two share a birthday.
- **coupon collector's problem**: Expected number of randomly obtained coupons to collect all b types is b·ln b + O(b).
- **k-permutation**: A sequence containing k of n elements without repetitions.
- **inversion**: Pair (i,j) where i<j and A[i] > A[j].
- **hat-check problem**: Expected number of customers getting own hat back when hats returned randomly = 1.

### Processes / Algorithms / Pathways

##### HIRE-ASSISTANT (n)
```
HIRE-ASSISTANT(n)
1 best = 0   // dummy least-qualified candidate
2 for i = 1 to n
3     interview candidate i
4     if candidate i is better than candidate best
5         best = i
6         hire candidate i
```
- **Cost**: Interview cost = O(c_i·n). Hiring cost = O(c_h·m) where m = number hired.
- **Worst-case**: Candidates in increasing order → hire all n → O(c_h·n).
- **Average-case** (random order): Expected hires = H_n = ln n + Θ(1) → O(c_h·ln n).

##### RANDOMIZED-HIRE-ASSISTANT (n)
```
RANDOMIZED-HIRE-ASSISTANT(n)
1 randomly permute the list of candidates
2 HIRE-ASSISTANT(n)
```
- **Expected hiring cost**: O(c_h·ln n) for ANY input.

##### RANDOMLY-PERMUTE (A, n)
```
RANDOMLY-PERMUTE(A, n)
1 for i = 1 to n
2     swap A[i] with A[RANDOM(i, n)]
```
- **Goal**: Generate uniform random permutation.
- **Complexity**: Θ(n), in-place.
- **Correctness**: Loop invariant — after i-1 iterations, each (i-1)-permutation appears with probability (n-i+1)!/n!. At end (i=n+1), each n-permutation has probability 1/n!.

##### ONLINE-MAXIMUM (k, n)
```
ONLINE-MAXIMUM(k, n)
1 best-score = -∞
2 for i = 1 to k
3     if score(i) > best-score
4         best-score = score(i)
5 for i = k+1 to n
6     if score(i) > best-score
7         return i
8 return n
```
- **Strategy**: Reject first k, then hire first candidate better than all seen.
- **Success probability**: Pr{S} = (k/n)(ln n - ln k) ± O(1/n)
- **Optimal k**: k = n/e ≈ 0.368n, success probability ≥ 1/e ≈ 0.368.

##### RANDOM-SAMPLE (m, n)
```
RANDOM-SAMPLE(m, n)
1 S = ∅
2 for k = n-m+1 to n
3     i = RANDOM(1, k)
4     if i ∈ S
5         S = S ∪ {k}
6     else S = S ∪ {i}
7 return S
```
- **Goal**: Generate random m-subset of {1,...,n} using only m calls to RANDOM.

### Formulas & Equations

##### Indicator random variable
I{A} = { 1 if A occurs; 0 otherwise }
E[I{A}] = Pr{A}  (Lemma 5.1)

##### Linearity of expectation
E[∑ᵢ Xᵢ] = ∑ᵢ E[Xᵢ] (holds even for dependent variables)

##### Expected hires in HIRE-ASSISTANT
- Pr{candidate i is hired} = 1/i
- E[number of hires] = ∑ᵢ₌₁ⁿ 1/i = H_n = ln n + γ + O(1/n) ≈ ln n

##### Birthday paradox
- Pr{k people all have different birthdays} = ∏ᵢ₌₁^{k-1} (1 - i/n)
- Using 1+x ≤ e^x: Pr{different} ≤ e^{-k(k-1)/(2n)}
- Pr{same} ≥ 1/2 when k ≥ (1+√(1+8n ln 2))/2. For n=365: k ≈ 23.
- Expected number of matching pairs: C(k,2)/n ≈ k²/(2n). For k=28, ≈ 1.04.

##### Balls and bins (coupon collector)
- Expected tosses until every bin has a ball: b·H_b = b ln b + O(b)
- Per-stage expectation: E[n_i] = b/(b-i+1)
- Total: ∑ᵢ₌₁^b b/(b-i+1) = b·H_b

##### Streaks of consecutive heads
- Expected longest streak in n fair coin flips: Θ(lg n)
- Upper bound: Pr{streak ≥ 2⌈lg n⌉} ≤ 1/n
- Lower bound: Pr{streak ≥ ⌊(lg n)/2⌋} ≥ 1 - O(1/n)

##### Online hiring success probability
Pr{S} = (k/n)(H_{n-1} - H_{k-1}) ≈ (k/n)(ln n - ln k)
Optimal k = n/e, success probability ≈ 1/e

### Comparisons

| | Probabilistic Analysis | Randomized Algorithm |
|---|---|---|
| **Input assumption** | Input distribution known | No assumption (imposes randomness) |
| **Running time** | Average-case over inputs | Expected over algorithm's random choices |
| **Example** | HIRE-ASSISTANT with random order | RANDOMIZED-HIRE-ASSISTANT |
| **Guarantee** | For typical inputs | For every input |

### Edge Cases / Traps

- **Pairwise independence insufficient** for birthday paradox analysis (Exercise 5.4-4) — need full independence for exact probability, but linearity of expectation with indicator variables requires only pairwise independence for expectation.
- **PERMUTE-WITH-ALL vs RANDOMLY-PERMUTE**: Swapping with any element (PERMUTE-WITH-ALL) does NOT produce uniform random permutation — it produces only nⁿ equally likely outcomes, and n! does not divide nⁿ.
- **PERMUTE-WITHOUT-IDENTITY**: Professor Kelp's procedure (RANDOM(i+1,n)) never produces identity permutation but doesn't produce all other permutations uniformly.
- **PERMUTE-BY-CYCLE**: Each element has 1/n probability in any position, but permutations are not uniformly random (only n possible outcomes, not n!).
- **Average-case ≠ expected**: Average-case is over input distribution; expected is over algorithm's random choices.
- **Worst-case input for randomized algorithm**: No single input elicits worst-case behavior; unlucky random choices do.

### End-of-Chapter Material

**5.1-1** Being able to determine which candidate is best means you have a total order: for any two candidates, you can decide which is better. The ranking provides a total order since ranks are unique.

**5.1-2** Implement RANDOM(a,b) using RANDOM(0,1):
```
RANDOM(a,b)
1 range = b-a+1
2 bits = ⌈lg range⌉
3 do
4     result = 0
5     for i = 0 to bits-1
6         result = 2*result + RANDOM(0,1)
7 while result ≥ range
8 return a + result
```
Expected calls to RANDOM(0,1): at most 2·⌈lg(b-a+1)⌉ (due to rejection sampling).

**5.1-3** Unbiased from biased:
```
UNBIASED
1 do
2     x = BIASED-RANDOM()
3     y = BIASED-RANDOM()
4 while x == y
5 return x
```
Probability of (0,1) followed by (1,0) = p(1-p). Each equally likely. Expected iterations: 1/(2p(1-p)).

**5.2-1** Hire exactly once: first candidate is best → 1/n. Hire exactly n times: candidates in increasing order → 1/n!.

**5.2-2** Hire exactly twice: first candidate is not best. Let best be at position i>1. No one before best except first is hired. First must be best among first i-1, and second is overall best. Pr = ∑ᵢ₌₂ⁿ (1/(i-1))·(1/n) = (1/n)·H_{n-1}. Approximately (ln n)/n.

**5.2-3** Sum of n dice: E[X] = ∑ᵢ₌₁ⁿ E[X_i] = n·3.5 = 3.5n.

**5.2-4** Independent dice: sum expectation = 3.5+3.5=7. Second die = first: sum expectation = 3.5+3.5=7. Second = 7-first: E[sum] = E[first + (7-first)] = 7. Linearity holds.

**5.2-5** Hat-check problem: X_i = I{person i gets own hat}. Pr{X_i=1}=1/n. E[X] = ∑ᵢ₌₁ⁿ 1/n = 1.

**5.2-6** Expected inversions: For each pair (i,j), Pr{A[i]>A[j]} = 1/2. E[#inversions] = C(n,2)·1/2 = n(n-1)/4.

**5.3-1** Rewrite RANDOMLY-PERMUTE to start with i=0 and treat A[1:0] as nonempty by starting with i=1... Could initialize with A[1] fixed and loop from i=2.

**5.3-2** PERMUTE-WITHOUT-IDENTITY: Fails — for n=3, produces permutations (2,1,3), (3,1,2), (2,3,1), (3,2,1) each with probability 1/4, never identity (1,2,3) nor (1,3,2). Not uniform over non-identity.

**5.3-3** PERMUTE-WITH-ALL: Swap each A[i] with A[RANDOM(1,n)]. Produces nⁿ possible sequences, each equally likely. Since n! does not divide nⁿ in general (e.g., n=3: 3⁹=27, 3!=6, 27/6 not integer), permutations cannot be equally likely.

**5.3-4** PERMUTE-BY-CYCLE: Each element has 1/n chance for any position (due to offset uniform from 1..n). But only n possible permutations (one per offset value). Not uniform unless n=1.

**5.3-5** RANDOM-SAMPLE: Proven by induction that each m-subset is equally likely. At step k, element i is added to S with prob i/k or something... Produces uniform random m-subset in m calls.

**5.4-1** Someone has same birthday as you: Pr{someone matches} = 1 - (364/365)^{k-1}. Need k such that 1-(364/365)^{k-1} ≥ 1/2 → k ≥ 1 + ln(1/2)/ln(364/365) ≈ 254. (Approximately 253.)
Two people born on July 4: Use Poisson approx. Expected number = C(k,2)/365. Need ≈ 1 → k ≈ √730 ≈ 27.

**5.4-2** Need k such that Pr{different} ≤ 0.01. e^{-k(k-1)/(2·365)} ≤ 0.01 → k(k-1) ≥ 2·365·ln 100 ≈ 3361 → k ≥ 58. (Actually ~57.) Expected pairs = C(57,2)/365 ≈ 4.37.

**5.4-3** Birthday paradox variant: Expected tosses until bin has 2 balls ≈ √(πb/2). This is the expected number of tosses until a collision in hashing. More precisely, E[T] ≈ √(πb/2) where T is the first time a bin gets a second ball.

**5.4-4** Mutual independence NOT required for the indicator variable method (only linearity of expectation which needs no independence). For exact probability calculation, pairwise independence is not sufficient for the product formula (need full independence). But indicator approach using linearity of expectation only needs pairwise expectations, which only need pairwise independence or even just marginal probabilities.

**5.4-5** Three people with same birthday: Use Poisson. Expected number of triples = C(k,3)/365². Need ≈ 1 → k³ ≈ 6·365² ≈ 799,350 → k ≈ 93.

**5.4-6** Probability a k-string over alphabet size n forms a k-permutation: P = n!/((n-k)!·n^k). This is exactly the birthday paradox event: all k items distinct.

**5.4-7** n balls into n bins:
- Expected empty bins: E[#empty] = ∑ᵢ Pr{bin i empty} = n·(1-1/n)^n → n·(1/e) = n/e.
- Expected bins with exactly one ball: n·C(n,1)·(1/n)·(1-1/n)^{n-1} = n·(1-1/n)^{n-1} → n/e.

**5.4-8** Show Pr{streak ≥ lg n - 2 lg lg n} ≥ 1 - 1/n. Partition into n/(lg n - 2 lg lg n) groups. Each group all-heads prob = (1/2)^{s}. Expected number of such streaks ≈ n/2^s = n/2^{lg n - 2 lg lg n} = n/(n/(lg n)²) = (lg n)².

---

*End of Chapters 1–5 Study Guide*




### Ch. 6 — Heapsort

#### Named Entities (Terms & Definitions)
- **Heap (Binary)**: Array object viewed as nearly complete binary tree; completely filled on all levels except possibly the lowest, which fills from left.
- **Max-heap**: For every node i ≠ root: A[PARENT(i)] ≥ A[i] — largest element at root.
- **Min-heap**: For every node i ≠ root: A[PARENT(i)] ≤ A[i] — smallest element at root.
- **Heap property**: The condition (max or min) that values in nodes satisfy.
- **Height of a node**: Number of edges on longest simple downward path to a leaf.
- **Height of a heap**: Height of its root = Θ(lg n).
- **Priority queue**: Data structure maintaining a set S of elements, each with an associated key.
- **Max-priority queue**: Supports INSERT, MAXIMUM, EXTRACT-MAX, INCREASE-KEY.
- **Min-priority queue**: Supports INSERT, MINIMUM, EXTRACT-MIN, DECREASE-KEY.
- **Handle**: Additional info stored to map between application objects and array indices.

#### Processes / Algorithms / Pathways

##### PARENT / LEFT / RIGHT
```
PARENT(i) = ⌊i/2⌋    // shift right 1 bit
LEFT(i) = 2i          // shift left 1 bit
RIGHT(i) = 2i + 1     // shift left 1 bit + 1
```

##### MAX-HEAPIFY(A, i)
- **Goal**: Correct a single violation at node i, assuming children are max-heaps.
- **Input**: Array A with heap-size, index i.
- **Output**: Subtree at i obeys max-heap property.
- **Steps**: (1) Find largest among A[i], A[LEFT(i)], A[RIGHT(i)]; (2) If A[i] not largest, swap A[i] with A[largest]; (3) Recursively MAX-HEAPIFY on largest.
- **Complexity**: O(lg n) = O(h). Recurrence: T(n) ≤ T(2n/3) + Θ(1) → O(lg n).
- **Edge Cases**: Leaf (i > A.heap-size/2) → no effect; already largest → no swaps.

##### BUILD-MAX-HEAP(A, n)
```
BUILD-MAX-HEAP(A, n)
1 A.heap-size = n
2 for i = ⌊n/2⌋ downto 1
3     MAX-HEAPIFY(A, i)
```
- **Loop invariant**: Nodes i+1, i+2, ..., n are roots of max-heaps.
- **Complexity**: O(n). Tight bound: ∑_{h=0}^{⌊lg n⌋} ⌈n/2^{h+1}⌉·O(h) = O(n).
- **Correctness**: Leaves (indices ⌊n/2⌋+1..n) are trivial max-heaps; process bottom-up.

##### HEAPSORT(A, n)
```
HEAPSORT(A, n)
1 BUILD-MAX-HEAP(A, n)
2 for i = n downto 2
3     exchange A[1] with A[i]
4     A.heap-size = A.heap-size - 1
5     MAX-HEAPIFY(A, 1)
```
- **Loop invariant**: A[1:i] is max-heap of i smallest elements; A[i+1:n] contains n-i largest elements, sorted.
- **Complexity**: O(n lg n). BUILD-MAX-HEAP O(n) + (n-1)·MAX-HEAPIFY O(lg n) each.
- **In-place**: Yes. **Stable**: No.

##### Priority Queue Operations
- **MAXIMUM**: Θ(1) — return A[1].
- **EXTRACT-MAX**: O(lg n) — replace root with last, shrink heap, MAX-HEAPIFY.
- **INCREASE-KEY**: O(lg n) — set key, bubble up while parent is smaller.
- **INSERT**: O(lg n) — add leaf with -∞, then INCREASE-KEY to target.

#### Data Structures & Types
- **Heap**: Nearly complete binary tree in array A[1:n]. Height = ⌊lg n⌋.
- **Operations table**:

| Operation | Time |
|-----------|------|
| MAX-HEAPIFY | O(lg n) |
| BUILD-MAX-HEAP | O(n) |
| HEAPSORT | O(n lg n) |
| MAXIMUM | Θ(1) |
| EXTRACT-MAX | O(lg n) |
| INCREASE-KEY | O(lg n) |
| INSERT | O(lg n) |

#### Comparisons & Trade-offs
| Property | Heapsort | Mergesort | Quicksort |
|----------|----------|-----------|-----------|
| Time | O(n lg n) | O(n lg n) | Θ(n²) worst, Θ(n lg n) avg |
| In-place | Yes | No | Yes |
| Stable | No | Yes | No |
| Constant factors | Larger than quicksort | Larger | Small |

#### Formulas & Equations
- Parent: PARENT(i) = ⌊i/2⌋
- Left child: LEFT(i) = 2i
- Right child: RIGHT(i) = 2i + 1
- Leaves: indices ⌊n/2⌋+1 through n
- Nodes at height h: ≤ ⌈n/2^{h+1}⌉
- Heap height: ⌊lg n⌋
- BUILD-MAX-HEAP cost: ∑_{h=0}^{⌊lg n⌋} ⌈n/2^{h+1}⌉·O(h) = O(n)

#### Visual Patterns
- **Figure 6.1**: Max-heap as (a) binary tree with values, (b) array with parent-child lines.
- **Figure 6.2**: MAX-HEAPIFY(A,2) — violator floats down.
- **Figure 6.4**: HEAPSORT — tan = sorted largest values; blue = remaining heap.

#### Edge Cases & Common Pitfalls
- Empty heap: A.heap-size = 0.
- All elements equal: still O(n lg n) for heapsort.
- MAX-HEAPIFY on leaf: no effect.
- Sorted array as min-heap: ascending order satisfies min-heap property.

#### Proof & Argument Patterns
- **Loop invariant for BUILD-MAX-HEAP**: nodes i+1...n are roots of max-heaps.
- **Loop invariant for HEAPSORT**: A[1:i] is max-heap of i smallest; A[i+1:n] has n-i largest sorted.
- **MAX-HEAPIFY correctness**: structural induction on subtree height.


### Ch. 7 — Quicksort

#### Named Entities (Terms & Definitions)
- **Pivot**: Element selected as the partition point.
- **Low side**: Elements ≤ pivot. **High side**: Elements ≥ pivot.
- **Hoare partition**: Original partition scheme; two pointers from ends.
- **Tail-recursion elimination**: Convert one recursive call to iterative to reduce stack depth.

#### Processes / Algorithms / Pathways

##### PARTITION(A, p, r)
```
PARTITION(A, p, r)
1 x = A[r]          // pivot
2 i = p - 1
3 for j = p to r-1
4     if A[j] ≤ x
5         i = i + 1
6         exchange A[i] with A[j]
7 exchange A[i+1] with A[r]
8 return i + 1
```
- **Loop invariant**: For any k: (1) p ≤ k ≤ i → A[k] ≤ x; (2) i+1 ≤ k ≤ j-1 → A[k] > x; (3) k = r → A[k] = x.
- **Complexity**: Θ(n) for subarray of size n.

##### QUICKSORT(A, p, r)
- **Steps**: (1) Partition around pivot; (2) Recursively sort left subarray; (3) Recursively sort right subarray.
- **Worst case**: T(n) = T(n-1) + Θ(n) → Θ(n²) — happens when already sorted or reverse sorted.
- **Best case**: T(n) = 2T(n/2) + Θ(n) → Θ(n lg n) — balanced partition.
- **Any constant split**: T(n) = T(αn) + T((1-α)n) + Θ(n) → Θ(n lg n).
- **In-place**: Yes. **Stable**: No.

##### Randomized Quicksort
- RANDOMIZED-PARTITION picks random pivot; RANDOMIZED-QUICKSORT uses it.
- **Expected time**: Θ(n lg n) on n distinct elements.
- **Key Lemma 7.2**: z_i compared with z_j (i < j) iff one is chosen as pivot before any other in Z_{ij} = {z_i,...,z_j}.
- **Key Lemma 7.3**: Pr{z_i compared with z_j} = 2/(j-i+1).
- **Expected comparisons**: E[X] = ∑_{i=1}^{n-1} ∑_{j=i+1}^{n} 2/(j-i+1) < 2n ln n = O(n lg n).

#### Comparisons & Trade-offs
| Algorithm | Best | Average | Worst | In-place | Stable |
|-----------|------|---------|-------|----------|--------|
| Quicksort | Θ(n lg n) | Θ(n lg n) | Θ(n²) | Yes | No |
| Mergesort | Θ(n lg n) | Θ(n lg n) | Θ(n lg n) | No | Yes |
| Heapsort | Θ(n lg n) | Θ(n lg n) | Θ(n lg n) | Yes | No |
| Insertion | Θ(n) | Θ(n²) | Θ(n²) | Yes | Yes |

#### Edge Cases & Common Pitfalls
- **All elements equal**: PARTITION returns r → Θ(n²) worst-case.
- **Already sorted**: Θ(n²) if always pick last element as pivot (Lomuto).
- **Killer adversary** (McIlroy): can force Θ(n²) on virtually any implementation.

#### Dates & People
- C. A. R. Hoare: invented quicksort (1960/1962).
- N. Lomuto: Lomuto partition.
- McIlroy: "killer adversary" for quicksort.

### Ch. 8 — Sorting in Linear Time

#### Named Entities (Terms & Definitions)
- **Comparison sort**: Determines order only by comparing elements. Lower bound: Ω(n lg n).
- **Decision tree**: Full binary tree representing comparisons performed by a comparison sort.
- **Counting sort**: Sorts integers in range 0..k in Θ(n+k) time; not a comparison sort.
- **Stable sort**: Equal values appear in output in same order as input.
- **Radix sort**: Sorts digit by digit, LSB first, using stable sort.
- **Bucket sort**: Assumes uniform distribution over [0,1); divides into buckets, sorts each.

#### Processes / Algorithms / Pathways

##### COUNTING-SORT(A, n, k)
```
COUNTING-SORT(A, n, k)
1 let B[1:n] and C[0:k] be new arrays
2 for i = 0 to k: C[i] = 0
3 for j = 1 to n: C[A[j]] = C[A[j]] + 1
4 // C[i] now = count of elements equal to i
5 for i = 1 to k: C[i] = C[i] + C[i-1]
6 // C[i] now = count of elements ≤ i
7 for j = n down to 1:
8     B[C[A[j]]] = A[j]
9     C[A[j]] = C[A[j]] - 1
10 return B
```
- **Complexity**: Θ(n + k) = Θ(n) when k = O(n).
- **Stable**: Yes (processing from n down to 1 preserves order).
- **Not in-place**: Uses two additional arrays.

##### RADIX-SORT(A, n, d)
```
RADIX-SORT(A, n, d)
1 for i = 1 to d
2     use stable sort to sort on digit i
```
- **Complexity**: Θ(d(n + k)) where k = range of digits.
- **Optimal r** (bits per digit): if b < ⌊lg n⌋, choose r = b → Θ(n); if b ≥ ⌊lg n⌋, choose r = ⌊lg n⌋ → Θ(bn/lg n).

##### BUCKET-SORT(A, n)
```
BUCKET-SORT(A, n)
1 let B[0:n-1] be new array of empty lists
2 for i = 1 to n: insert A[i] into B[⌊n·A[i]⌋]
3 for i = 0 to n-1: sort list B[i] with insertion sort
4 concatenate lists B[0], B[1], ..., B[n-1]
```
- **Assumption**: Input uniformly distributed over [0,1).
- **Average case**: Θ(n). **Worst case**: Θ(n²) (all in one bucket).

#### Rules, Laws & Theorems
**Theorem 8.1** (Lower bound): Any comparison sort requires Ω(n lg n) comparisons in worst case.
- Proof: n! ≤ l ≤ 2^h → h ≥ lg(n!) = Ω(n lg n).
**Corollary 8.2**: Heapsort and mergesort are asymptotically optimal comparison sorts.

#### Formulas & Equations
- Decision tree: n! ≤ l ≤ 2^h → h ≥ lg(n!) = Ω(n lg n)
- Stirling: lg(n!) = n lg n − n lg e + Θ(lg n) ≈ n lg n − 1.44n
- Counting sort: Θ(n + k)
- Radix sort: Θ((b/r)(n + 2^r))

#### Edge Cases & Common Pitfalls
- Bucket sort with skewed distribution: worst-case Θ(n²).
- Counting sort with large k: Θ(n + k) becomes Θ(k) which may dominate.

### Ch. 9 — Medians and Order Statistics

#### Named Entities
- **i-th order statistic**: i-th smallest element.
- **Median**: Lower median ⌊(n+1)/2⌋, upper median ⌈(n+1)/2⌉.
- **Selection problem**: Find i-th smallest from n distinct numbers.

#### Processes / Algorithms / Pathways

##### MINIMUM / MAXIMUM
- Minimum: n−1 comparisons (each non-winner loses at least once).
- Simultaneous min & max: ≤ 3⌊n/2⌋ comparisons (pairwise method).

##### RANDOMIZED-SELECT(A, p, r, i)
```
RANDOMIZED-SELECT(A, p, r, i)
1 if p == r: return A[p]
2 q = RANDOMIZED-PARTITION(A, p, r)
3 k = q - p + 1
4 if i == k: return A[q]
5 elseif i < k: return RANDOMIZED-SELECT(A, p, q-1, i)
6 else: return RANDOMIZED-SELECT(A, q+1, r, i-k)
```
- **Key difference from quicksort**: Only recurses on one side.
- **Expected time**: Θ(n) (with probability ≥ 1/2, pivot falls in middle half).
- **Worst case**: Θ(n²) (unlucky partitions).

##### SELECT — Deterministic Linear-Time Selection
- Group n/5 groups of 5; find median of each group.
- Recursively find median of the ⌈n/5⌉ group medians → pivot.
- Partition around pivot; recurse on appropriate side.
- **Pivot guarantee**: Each side ≤ 7n/10.
- **Recurrence**: T(n) ≤ T(n/5) + T(7n/10) + Θ(n) → T(n) = Θ(n).
- **Theorem 9.3**: SELECT runs in Θ(n) worst-case time.

#### Comparisons & Trade-offs
| Algorithm | Strategy | Worst-case | Expected | Practical? |
|-----------|----------|-----------|----------|-----------|
| MINIMUM | Sequential | Θ(n) | — | Yes |
| MIN+MAX pair | Pairwise | ⌈3n/2⌉−2 | — | Yes |
| RANDOMIZED-SELECT | Randomized D&C | Θ(n²) | Θ(n) | Yes |
| SELECT (median-of-medians) | Deterministic D&C | Θ(n) | Θ(n) | No (high constant) |

#### Edge Cases & Common Pitfalls
- n not divisible by 5: preprocessing loop handles it.
- All elements equal: works correctly despite analysis assumption.
- i = 1 (minimum): SELECT returns after preprocessing.


### Ch. 10 — Elementary Data Structures

#### Named Entities (Terms & Definitions)
- **Stack**: LIFO (last-in, first-out). Operations: PUSH, POP, STACK-EMPTY.
- **Queue**: FIFO (first-in, first-out). Operations: ENQUEUE, DEQUEUE.
- **Doubly linked list**: Each node has key, prev, next pointers.
- **Singly linked list**: Only next pointer.
- **Circular list**: tail→head, head→tail.
- **Sentinel**: Dummy object L.nil representing NIL; simplifies boundary checks.
- **Row-major order**: index = n(i-1) + j for 1-origin.

#### Processes / Algorithms / Pathways
- **PUSH(S, x)**: O(1). Increment top, store x. Error on overflow.
- **POP(S)**: O(1). Return top, decrement. Error on underflow.
- **ENQUEUE(Q, x)**: O(1). Insert at tail, wrap around circularly.
- **DEQUEUE(Q)**: O(1). Remove from head, wrap around.
- **LIST-SEARCH(L, k)**: Θ(n) worst. Linear scan.
- **LIST-PREPEND(L, x)**: O(1). Insert at front.
- **LIST-DELETE(L, x)**: O(1) given pointer to x (doubly linked).
- **Sentinel benefits**: Simplifies LIST-DELETE (no boundary checks); eliminates end-of-list check in search.

#### Comparisons & Trade-offs
| Operation | Array | Doubly Linked List |
|-----------|-------|-------------------|
| Access k-th | O(1) | Θ(k) |
| Insert/delete at front | Θ(n) | O(1) |
| Search | Θ(n) | Θ(n) |

#### Edge Cases & Common Pitfalls
- Stack/queue underflow/overflow.
- Empty list operations.
- Singly linked delete = Θ(n) (must find predecessor).
- Sentinel: never delete sentinel.

### Ch. 11 — Hash Tables

#### Named Entities (Terms & Definitions)
- **Hash function** h: U → {0,...,m-1} maps keys to slots.
- **Collision**: Two keys hash to same slot.
- **Load factor**: α = n/m (average elements per slot).
- **Independent uniform hashing**: Each key's hash independent and uniform.
- **Chaining**: Each slot points to linked list of colliding keys.
- **Open addressing**: All elements stored in table itself; probes.
- **Universal hashing**: Family H is universal if Pr[h(k₁)=h(k₂)] ≤ 1/m for distinct k₁,k₂.
- **Perfect hashing**: Static keys, O(1) worst-case search.

#### Processes / Algorithms / Pathways

##### Hashing with Chaining
- INSERT: O(1) — prepend to chain.
- SEARCH: average Θ(1+α) under independent uniform hashing.
- DELETE: O(1) if doubly linked chain.
- **Theorem 11.1**: Unsuccessful search averages Θ(1+α).
- **Theorem 11.2**: Successful search averages Θ(1+α).

##### Open Addressing
```
HASH-INSERT(T, k)
1 i = 0
2 repeat
3     q = h(k, i)
4     if T[q] == NIL: T[q] = k; return q
5     else i = i + 1
6 until i == m
7 error "hash table overflow"
```
- α ≤ 1 (table can fill up).
- **Double hashing**: h(k,i) = (h₁(k) + i·h₂(k)) mod m. Best for avoiding clustering.
- **Linear probing**: h(k,i) = (h₁(k) + i) mod m. Primary clustering; good cache locality.

##### Hashing Analysis
| Operation | Expected probes (open addressing) |
|-----------|----------------------------------|
| Unsuccessful search | ≤ 1/(1-α) |
| Successful search | ≤ (1/α) ln(1/(1-α)) |

##### Universal Hash Family H_pm
- Choose prime p > m, h_{ab}(k) = ((ak + b) mod p) mod m.
- Theorem 11.4: H_pm is universal.

#### Edge Cases & Common Pitfalls
- All keys hash to same slot → Θ(n) search (chaining).
- Open addressing table full → overflow.
- Deletion in open addressing: need DELETED marker or special method.
- Double hashing with gcd(m, h₂(k)) > 1 → only 1/d of table examined.

#### Dates & People
- H.P. Luhn (1953): hash tables with chaining.
- Carter & Wegman (1979): universal hashing.
- Thorup: 5-independence for linear probing analysis.

### Ch. 12 — Binary Search Trees

#### Named Entities
- **BST property**: For node x, all keys in left subtree ≤ x.key ≤ all keys in right subtree.
- **Inorder tree walk**: left → root → right → produces sorted order.

#### Processes / Algorithms / Pathways

##### TREE-SEARCH(x, k): O(h). Recursive or iterative.
##### TREE-MINIMUM(x): O(h). Follow left child until NIL.
##### TREE-MAXIMUM(x): O(h). Follow right child until NIL.
##### TREE-SUCCESSOR(x): O(h).
- If x.right ≠ NIL: return TREE-MINIMUM(x.right).
- Else: go up until finding node that is left child of its parent.
##### TREE-INSERT(T, z): O(h). Trailing pointer y tracks parent.
##### TREE-DELETE(T, z): O(h). Three cases:
1. No left child: replace by right child.
2. No right child but has left: replace by left child.
3. Two children: find successor y = TREE-MINIMUM(z.right); replace z by y.

#### Formulas & Equations
- Inorder walk: T(n) = T(k) + T(n-k-1) + d → Θ(n) (Theorem 12.1).

#### Edge Cases & Common Pitfalls
- Linear chain: BST degenerates → Θ(n) for all operations.
- All keys equal: depends on tie-breaking strategy.
- Insert into empty tree: trailing pointer y = NIL → set T.root = z.

### Ch. 13 — Red-Black Trees

#### Named Entities (Terms & Definitions)
- **Red-black tree**: BST with one extra bit per node: color = RED or BLACK.
- **Black-height bh(x)**: Number of black nodes on path from x (excluding x) to leaf.
- **Sentinel T.nil**: All NIL pointers replaced by single black T.nil.

#### Properties
1. Every node is RED or BLACK.
2. Root is BLACK.
3. Every leaf (T.nil) is BLACK.
4. RED node's children are both BLACK (no two reds in a row).
5. Equal black count on all paths from node to leaves.

**Lemma 13.1**: RB-tree with n internal nodes has height ≤ 2 lg(n+1).
- Proof: Subtree at x has ≥ 2^{bh(x)} - 1 nodes. bh(root) ≥ h/2 → n ≥ 2^{h/2} - 1.
- Corollary: SEARCH, MINIMUM, MAXIMUM, SUCCESSOR, PREDECESSOR all O(lg n).

#### Processes / Algorithms / Pathways

##### LEFT-ROTATE(T, x): O(1). Makes x.right become new root of subtree. Preserves BST property.

##### RB-INSERT(T, z): O(lg n)
1. BST-insert z, color it RED.
2. RB-INSERT-FIXUP: three cases while z.p is RED:
   - **Case 1**: Uncle RED → recolor parent, uncle, grandparent; move z up 2.
   - **Case 2**: Uncle BLACK, z is right child → left-rotate parent → Case 3.
   - **Case 3**: Uncle BLACK, z is left child → recolor parent BLACK, grandparent RED; right-rotate grandparent.
   - Root always BLACK.

##### RB-DELETE(T, z): O(lg n)
- Based on TREE-DELETE with RB-TRANSPLANT.
- Tracks y = node removed/moved and y-original-color.
- If y was BLACK: RB-DELETE-FIXUP(x) where x replaces y.
- **Four fixup cases** (x is left child):
  1. Sibling RED → recolor, left-rotate → becomes case 2/3/4.
  2. Sibling BLACK, both nephews BLACK → set sibling RED, move x up.
  3. Sibling BLACK, left nephew RED, right BLACK → recolor, right-rotate → case 4.
  4. Sibling BLACK, right nephew RED → recolor, left-rotate, done.

#### Formulas & Equations
- Height: ≤ 2 lg(n+1).
- All operations: O(lg n).
- Rotations per INSERT: at most 2. Rotations per DELETE: at most 3.

#### Visual Patterns
- **Rotations** (Fig 13.2): x → y transform via constant pointer changes.
- **Insert cases** (Fig 13.4-13.6): case 1 = recolor+move up; case 2→3 via rotation.

#### Dates & People
- Bayer (1972): "symmetric binary B-trees".
- Guibas & Sedgewick: named red-black trees.
- AVL trees: Adel'son-Vel'skiĭ & Landis (1962).
- Splay trees: Sleator & Tarjan.


### Ch. 14 — Dynamic Programming

#### Named Entities (Terms & Definitions)
- **Dynamic Programming**: Solves problems by combining solutions to overlapping subproblems. "Programming" refers to tabular method.
- **Optimal substructure**: Optimal solution contains within it optimal solutions to subproblems.
- **Overlapping subproblems**: Space of subproblems is small; same subproblems solved repeatedly.
- **Memoization**: Top-down recursive approach that saves results in a table.
- **Cut-and-paste technique**: Proof method: assume suboptimal subproblem, cut it out, paste optimal one → contradiction.
- **Independent subproblems**: Solution to one subproblem does not affect another.

#### Processes / Algorithms / Pathways

##### Four-Step DP Method
1. Characterize structure of optimal solution.
2. Recursively define value of optimal solution.
3. Compute value (typically bottom-up).
4. Construct optimal solution from computed info.

##### Rod Cutting
- **Problem**: Given rod length n and price table p_i, maximize revenue r_n by cutting rod.
- **Recurrence**: r_n = max_{1≤i≤n} (p_i + r_{n-i}), r_0 = 0.
- **Naive CUT-ROD**: T(n) = 2^n (exponential).
- **BOTTOM-UP-CUT-ROD**: Θ(n²).
- **Number of ways to cut**: 2^{n-1}.

##### Matrix-Chain Multiplication
- **Problem**: Fully parenthesize chain 〈A₁...A_n⟩ to minimize scalar multiplications.
- **Dimensions**: p_{i-1}×p_i for A_i.
- **Cost recurrence**: m[i,i] = 0; m[i,j] = min_{i≤k<j} {m[i,k] + m[k+1,j] + p_{i-1}·p_k·p_j}.
- **MATRIX-CHAIN-ORDER**: O(n³) time, Θ(n²) space.
- **Number of parenthesizations**: Catalan numbers P(n) = Ω(4^n/n^{3/2}).

##### Longest Common Subsequence (LCS)
- **Problem**: Find maximum-length subsequence common to X = 〈x₁...x_m⟩, Y = 〈y₁...y_n⟩.
- **Recurrence**: c[i,j] = 0 if i=0 or j=0; c[i-1,j-1] + 1 if x_i = y_j; max(c[i-1,j], c[i,j-1]) if x_i ≠ y_j.
- **LCS-LENGTH**: Θ(mn) time, Θ(mn) space.

##### Optimal Binary Search Tree (OBST)
- **Problem**: BST minimizing expected search cost given p_i (key k_i) and q_i (dummy keys).
- **Cost recurrence**: e[i,i-1] = q_{i-1}; e[i,j] = min_{i≤r≤j} {e[i,r-1] + e[r+1,j] + w(i,j)}.
- **OPTIMAL-BST**: Θ(n³). Knuth optimization reduces to Θ(n²).

#### Rules, Laws & Theorems
**Theorem 14.1 (Optimal substructure of LCS)**: If x_m = y_n, then z_k = x_m = y_n and Z_{k-1} is LCS of X_{m-1}, Y_{n-1}. If x_m ≠ y_n, then Z is LCS of X_{m-1}, Y or X, Y_{n-1}.

#### Comparisons & Trade-offs
| Aspect | Top-Down (Memoization) | Bottom-Up |
|--------|----------------------|-----------|
| Control | Recursive | Iterative |
| Subproblems solved | Only required | All |
| Overhead | More | Less |
| Asymptotic | Same | Same |

**DP vs Divide-and-Conquer**: DP has overlapping subproblems, D&C has disjoint.

**DP vs Greedy**: DP solves subproblems first then chooses; greedy chooses first then solves one subproblem.

### Ch. 15 — Greedy Algorithms

#### Named Entities
- **Greedy algorithm**: Makes locally optimal choice hoping it leads to globally optimal solution.
- **Greedy-choice property**: Globally optimal solution can be assembled by making locally optimal choices.
- **Prefix-free code**: No codeword is prefix of any other.
- **Huffman code**: Optimal prefix-free code built by merging least-frequent characters.

#### Processes / Algorithms / Pathways

##### Activity Selection
- **Problem**: Select max-size set of mutually compatible activities (s_i start, f_i finish).
- **Greedy choice**: Pick activity with earliest finish time.
- **RECURSIVE-ACTIVITY-SELECTOR**: Θ(n) (sorted by finish).
- **GREEDY-ACTIVITY-SELECTOR**: Θ(n) iterative.

##### Huffman Codes
```
HUFFMAN(C)
1 Q = C
2 for i = 1 to |C|-1
3     allocate new node z
4     x = EXTRACT-MIN(Q); y = EXTRACT-MIN(Q)
5     z.left = x; z.right = y
6     z.freq = x.freq + y.freq
7     INSERT(Q, z)
8 return EXTRACT-MIN(Q)
```
- **Time**: O(n lg n) with binary min-heap.
- **Lemma 15.2**: Two lowest-frequency characters can be deepest siblings in optimal code.
- **Lemma 15.3**: Optimal substructure for Huffman codes.

##### Fractional vs 0-1 Knapsack
- **Fractional**: Greedy by value/weight works. O(n lg n).
- **0-1**: Greedy fails. DP O(nW).

##### Offline Caching (Furthest-in-Future)
- Evict block whose next access is furthest in future.
- Theorem 15.5: Furthest-in-future optimal for caching with full future knowledge.

#### Rules, Laws & Theorems
**Theorem 15.1 (Greedy choice for activity selection)**: Earliest-finish activity is included in some optimal solution.

**Theorem 15.4**: HUFFMAN produces optimal prefix-free code.

#### Comparisons & Trade-offs
| Aspect | Greedy | DP |
|--------|--------|-----|
| Approach | Top-down: choose first | Bottom-up: solve subproblems first |
| Subproblems | One remains | Many possible |
| Hallmarks | Greedy-choice + optimal substructure | Optimal substructure + overlapping |
| Example | Fractional knapsack | 0-1 knapsack |

### Ch. 16 — Amortized Analysis

#### Named Entities
- **Amortized analysis**: Averages time over sequence of operations; guarantees average per-operation worst-case.
- **Aggregate analysis**: Total cost T(n) / n = amortized cost per op.
- **Accounting method**: Overcharge some ops early, store credit, use for later undercharged ops.
- **Potential method**: Φ: data structure → ℝ. ĉ_i = c_i + Φ(D_i) − Φ(D_{i-1}).
- **Load factor**: α(T) = num/size.

#### Processes / Algorithms / Pathways

##### MULTIPOP(S, k): min(s, k) actual cost.
##### Binary Counter INCREMENT: flips t_i + 1 bits (t_i = trailing 1s).
##### Dynamic Table: TABLE-INSERT expands by factor of 2 when full; TABLE-DELETE contracts at α < 1/4.

#### Comparisons & Trade-offs
| Method | Key concept | Amortized cost |
|--------|------------|---------------|
| Aggregate | Total cost / n | Same for all ops |
| Accounting | Credit on objects | Differs per type |
| Potential | Φ(D_i) − Φ(D_{i-1}) | Differs per type |

#### Formulas & Equations
- **Accounting constraint**: ∑ĉ_i ≥ ∑c_i (credit never negative).
- **Potential**: ĉ_i = c_i + Φ(D_i) − Φ(D_{i-1}); ∑ĉ_i = ∑c_i + Φ(D_n) − Φ(D_0).
- **Binary counter flips**: ∑_{i=0}^{k-1} ⌊n/2^i⌋ < 2n.
- **Dynamic table (insert only)**: Φ = 2·num − size. Amortized cost = 3 per insertion.
- **Dynamic table (insert+delete)**: Φ = 2·num − size if α ≥ 1/2; Φ = size/2 − num if α < 1/2.
- **TABLE-INSERT aggregate**: ≤ 3n total for n insertions.

#### Edge Cases & Common Pitfalls
- Empty stack MULTIPOP: while condition prevents errors.
- Counter not starting at 0: total ≤ 2n + b₀ − b_n.
- Contraction thrashing: halving at 1/2 causes Θ(n²); solution: contract at 1/4.


### Ch. 17 — Augmenting Data Structures

#### Named Entities (Terms & Definitions)
- **Augment a data structure**: Add new fields and maintain invariants to support new operations.
- **Order-statistic tree**: Red-black tree augmented with x.size = x.left.size + x.right.size + 1.
- **Interval tree**: Red-black tree with intervals as keys, augmented with x.max = max(x.int.high, x.left.max, x.right.max).

#### Processes / Algorithms / Pathways

##### Dynamic Order Statistics
- **OS-SELECT(x, i)**: O(lg n). Find i-th order statistic recursively by checking x.left.size.
- **OS-RANK(T, x)**: O(lg n). Compute rank by walking up from x to root.
- **Maintaining size**: On INSERT, increment size along path (O(lg n)). On rotation, update size of rotated nodes (O(1)).

##### Interval Trees
- **INTERVAL-SEARCH(T, i)**: O(lg n). Find any interval in T that overlaps i.
- **Key**: At each node, go left if x.left.max ≥ i.low; else go right.
- **Theorem 17.2**: INTERVAL-SEARCH returns an overlapping interval if one exists.

#### Rules, Laws & Theorems
**Theorem 17.1 (Choosing augmentation)**: Can augment red-black trees with field f if: (1) f can be computed from node's own data, left.f, right.f in O(1); (2) f is updated during rotations in O(1). Then all RB operations remain O(lg n).

### Ch. 18 — B-Trees

#### Named Entities
- **B-tree**: Balanced search tree optimized for disk storage. Nodes have high branching factor.
- **Minimum degree t**: Each node (except root) has t-1 ≤ keys ≤ 2t-1. Internal nodes have degree t..2t.
- **B-tree height**: h ≤ log_t ((n+1)/2) (Theorem 18.1).

#### Processes / Algorithms / Pathways

##### B-TREE-SEARCH(x, k): O(t log_t n). Linear search within node, then recurse.
##### B-TREE-SPLIT-CHILD(x, i): Splits full child y of x into two (median key moves up to x). O(t).
##### B-TREE-INSERT(T, k): O(t log_t n). Split root if full; insert-nonfull recursively.
##### B-TREE-DELETE: Three main cases with subcases. O(t log_t n).

#### Visual Patterns
- B-tree of height 2 with minimum degree 3: internal nodes have 2-5 keys, children 3-6.

#### Comparisons & Trade-offs
- B-trees vs RB-trees: B-trees minimize disk accesses (high branching factor).
- B+ trees: all data in leaves, internal nodes just keys.
- B* trees: internal nodes at least 2/3 full (not 1/2).

### Ch. 19 — Data Structures for Disjoint Sets

#### Named Entities
- **Disjoint-set data structure**: Maintains collection of disjoint dynamic sets.
- **Union by rank**: Root of shorter tree points to taller. Rank = upper bound on height.
- **Path compression**: During FIND-SET, make each node on path point directly to root.

#### Processes / Algorithms / Pathways

##### Operations
- **MAKE-SET(x)**: O(1). Create singleton set.
- **FIND-SET(x)**: O(α(n)) amortized. Follow parent pointers to root with path compression.
- **UNION(x, y)**: O(α(n)) amortized. FIND both roots; attach shorter to taller.

##### Linked-List Representation
- Each set: linked list with head/tail pointers; each node has pointer to set object.
- **Union naïve**: O(n²) total for n unions.
- **Weighted-union heuristic**: O(m + n lg n) for m ops, n of which are MAKE-SET.
- **Theorem 19.1**: Weighted-union gives O(m + n lg n) total time.

##### Disjoint-Set Forests
- Tree representation with union by rank + path compression.
- **Theorem 19.14**: O(m α(n)) total time for m operations, where α(n) is inverse Ackermann function — grows extremely slowly (α(n) ≤ 4 for n ≤ 2^65536).

#### Formulas & Equations
- α(n) = min{k : A_k(1) ≥ n} where A_k(j) is Ackermann-like function.
- Rank properties: rank(p[x]) ≥ rank(x) + 1; rank increases only on path compression.


### Ch. 20 — Elementary Graph Algorithms

#### Named Entities (Terms & Definitions)
- **Graph G = (V, E)**: Vertices V and edges E.
- **Adjacency-list representation**: Array Adj of |V| lists. Memory: Θ(V+E).
- **Adjacency-matrix representation**: |V|×|V| matrix. Memory: Θ(V²).
- **Sparse graph**: |E| << |V|². **Dense**: |E| close to |V|².
- **Breadth-first tree**: Predecessor subgraph with unique shortest path from s.
- **Depth-first forest**: DFS predecessor subgraph with timestamps.
- **Topological sort**: Linear ordering of DAG vertices where (u,v) implies u before v.
- **Strongly connected component (SCC)**: Maximal C ⊆ V where every pair mutually reachable.
- **Component graph G_SCC**: Contracted SCC graph — always a DAG.

#### Processes / Algorithms / Pathways

##### BFS(G, s): O(V+E)
- Queue of gray vertices. Discover vertices by distance.
- v.d = shortest-path distance δ(s,v) (number of edges).
- Produces breadth-first tree.

##### DFS(G): Θ(V+E)
- Discovery timestamps u.d, finish times u.f (1 ≤ u.d < u.f ≤ 2|V|).
- Edge types: tree (white), back (gray), forward (black, descendant), cross (black, nondescendant).
- In undirected graphs: only tree and back edges.

##### TOPOLOGICAL-SORT(G): Θ(V+E)
- Run DFS; output vertices in reverse order of finish times.
- Correct iff graph is acyclic.

##### STRONGLY-CONNECTED-COMPONENTS(G): Θ(V+E)
1. DFS(G) to compute finish times.
2. Create G^T (transpose).
3. DFS(G^T) in order of decreasing u.f.
4. Output each DFS tree as SCC.

#### Rules, Laws & Theorems
- **Lemma 20.1**: δ(s,v) ≤ δ(s,u) + 1 for any edge (u,v).
- **Theorem 20.5**: BFS correctly computes shortest-path distances.
- **Theorem 20.7 (Parenthesis theorem)**: DFS discovery/finish intervals are either disjoint or nested.
- **Theorem 20.9 (White-path theorem)**: v is descendant of u iff at time u.d there's white path from u to v.
- **Lemma 20.11**: Digraph is acyclic iff DFS has no back edges.
- **Theorem 20.16**: SCC algorithm correctly computes SCCs.

#### Visual Patterns
- BFS: waves emanating from source.
- DFS: depth-first forest with parentheses nesting structure.
- SCC: component graph G_SCC is acyclic; second DFS visits in topologically sorted order.

### Ch. 21 — Minimum Spanning Trees

#### Named Entities
- **Spanning tree**: Acyclic subset T ⊆ E connecting all vertices; |V|-1 edges.
- **Minimum spanning tree (MST)**: Spanning tree with minimum total weight.
- **Cut (S, V−S)**: Partition of V.
- **Light edge**: Minimum-weight edge crossing a cut.
- **Safe edge**: Edge that can be added to A while A ⊆ some MST.

#### Processes / Algorithms / Pathways

##### GENERIC-MST: Add safe edges greedily until spanning tree.

##### Kruskal's Algorithm: O(E lg V)
- Sort edges by weight. Process smallest first. If edge connects different components (FIND-SET), add it (UNION).
- Uses disjoint-set data structure.
- Edge-based approach.

##### Prim's Algorithm: O(E lg V) with binary heap; O(E + V lg V) with Fibonacci heap
- Grow single tree from root. Use priority queue keyed by min edge weight to tree.
- Vertex-based approach.

#### Rules, Laws & Theorems
**Theorem 21.1 (Cut property)**: If A ⊆ some MST, cut (S,V−S) respects A, (u,v) is light edge crossing cut → (u,v) is safe for A.
**Cycle property**: Maximum-weight edge on any cycle is not in any MST.

#### Comparisons & Trade-offs
| Algorithm | Data Structure | Time |
|-----------|---------------|------|
| Kruskal | Disjoint-set forest | O(E lg V) |
| Prim (binary heap) | Binary min-heap | O(E lg V) |
| Prim (Fibonacci heap) | Fibonacci heap | O(E + V lg V) |

### Ch. 22 — Single-Source Shortest Paths

#### Named Entities
- **Shortest-path weight δ(u,v)**: Min weight over all paths; ∞ if no path; −∞ if negative cycle reachable.
- **Relaxation**: If v.d > u.d + w(u,v), update v.d = u.d + w(u,v), v.π = u.
- **Negative-weight cycle**: Makes shortest paths undefined for reachable vertices.

#### Processes / Algorithms / Pathways

##### Bellman-Ford Algorithm: O(VE)
- Initialize; relax all edges |V|-1 times; check for negative cycles.
- Returns FALSE if negative-weight cycle reachable.
- Works with negative weights.

##### DAG-Shortest-Paths: Θ(V+E)
- Topological sort, then relax edges in topological order.
- Linear time! Works with negative weights. No cycles.

##### Dijkstra's Algorithm: O(V²) array, O(E lg V) binary heap, O(V lg V + E) Fibonacci heap
- Requires nonnegative edge weights.
- Greedy: always selects vertex with smallest estimate from V−S.

#### Rules, Laws & Theorems
- **Lemma 22.1 (Optimal substructure)**: Subpaths of shortest paths are shortest paths.
- **Lemma 22.10 (Triangle inequality)**: δ(s,v) ≤ δ(s,u) + w(u,v).
- **Lemma 22.11 (Upper-bound property)**: v.d ≥ δ(s,v) always; once equal, never changes.
- **Lemma 22.14 (Convergence property)**: If s→...→u→v is shortest path and u.d = δ(s,u) before relaxing (u,v), then v.d = δ(s,v) after.
- **Lemma 22.15 (Path-relaxation property)**: If edges of shortest path relaxed in order, v_k.d = δ(s,v_k) afterward.

#### Comparisons & Trade-offs
| Algorithm | Negative weights? | Time |
|-----------|------------------|------|
| BFS | Unweighted | O(V+E) |
| DAG-Shortest-Paths | Yes (no cycles) | Θ(V+E) |
| Dijkstra | No | O(V lg V + E) (Fibonacci) |
| Bellman-Ford | Yes | O(VE) |

### Ch. 23 — All-Pairs Shortest Paths

#### Named Entities
- **Predecessor matrix Π**: π_{ij} = predecessor of j on shortest path from i.
- **W = (w_{ij})**: Input adjacency matrix.

#### Processes / Algorithms / Pathways

##### Floyd-Warshall Algorithm: Θ(V³)
- D^{(k)} = shortest paths using intermediate vertices only from {1,...,k}.
- Recurrence: d^{(k)}_{ij} = min(d^{(k-1)}_{ij}, d^{(k-1)}_{ik} + d^{(k-1)}_{kj}).
- Space-optimized: single matrix D overwritten in place.

##### Johnson's Algorithm: O(V² lg V + VE)
- For sparse graphs. Reweight edges using Bellman-Ford (h(v) = δ(s,v)).
- Run Dijkstra from each vertex.
- Reweighting: ŵ(u,v) = w(u,v) + h(u) − h(v) preserves shortest paths.

#### Comparisons & Trade-offs
| Algorithm | Time | Notes |
|-----------|------|-------|
| Floyd-Warshall | Θ(V³) | Simple, dense graphs |
| Johnson | O(V² lg V + VE) | Best for sparse |
| Run Dijkstra |V| times | O(V·E lg V) | Needs nonnegative weights |

### Ch. 24 — Maximum Flow

#### Named Entities
- **Flow network**: Directed graph (V,E) with source s, sink t, capacity c(u,v) ≥ 0.
- **Flow f**: Capacity constraint (0 ≤ f(u,v) ≤ c(u,v)); flow conservation (∀u≠s,t: in = out).
- **Flow value |f|**: ∑_v f(s,v) − ∑_v f(v,s).
- **Residual network G_f**: Edges with c_f(u,v) > 0.
- **Augmenting path**: s→t path in G_f.
- **Cut (S,T)**: Partition with s∈S, t∈T. Capacity = ∑_{u∈S}∑_{v∈T} c(u,v).

#### Processes / Algorithms / Pathways

##### Ford-Fulkerson Method
- While augmenting path exists in G_f, augment flow by min residual capacity on path.
- **Time**: O(E·|f*|) with integer capacities. May not terminate with irrational capacities.

##### Edmonds-Karp: O(VE²)
- Ford-Fulkerson where augmenting path found via BFS.
- Each edge becomes critical ≤ |V|/2 times → O(VE) augmentations × O(E) per BFS.

##### Maximum Bipartite Matching via Flow
- Construct flow network: s→L (cap 1), L→R (cap 1), R→t (cap 1).
- Max flow = max matching cardinality.
- **Integrality theorem**: Ford-Fulkerson with integer capacities produces integer flow.

#### Rules, Laws & Theorems
**Theorem 24.6 (Max-flow min-cut theorem)**: TFAE: (1) f is max flow; (2) G_f has no augmenting path; (3) |f| = c(S,T) for some cut (S,T).
**Lemma 24.4**: Net flow across any cut equals |f|.
**Corollary 24.5**: |f| ≤ c(S,T) for any cut.

### Ch. 25 — Matchings in Bipartite Graphs

#### Named Entities
- **Matching**: Subset M ⊆ E with at most one incident edge per vertex.
- **Perfect matching**: Every vertex matched.
- **M-alternating path**: Edges alternate between M and E−M.
- **M-augmenting path**: Alternating path with both endpoints unmatched.
- **Stable matching**: No blocking pair (two people who prefer each other to current partners).
- **Assignment problem**: Find max-weight perfect matching in complete bipartite graph.

#### Processes / Algorithms / Pathways

##### Hopcroft-Karp: O(√V·E)
- Find maximal set of vertex-disjoint shortest augmenting paths per phase.
- Each phase: BFS + DFS on directed graph.
- O(√V) phases.

##### Gale-Shapley (Stable Marriage): O(n²)
- Women propose to men in order of preference. Men accept if free or prefer her.
- Returns women-optimal, men-pessimal stable matching.
- Multiple stable matchings can exist.

##### Hungarian Algorithm (Assignment Problem): O(n⁴) → O(n³)
- Maintain feasible labeling: l.h + r.h ≥ w(l,r).
- Equality subgraph G_h: edges where l.h + r.h = w(l,r).
- While no perfect matching: find augmenting path; if blocked, update labels.

#### Rules, Laws & Theorems
- **Lemma 25.1**: M⊕P is a matching with |M|+1 edges for M-augmenting path P.
- **Corollary 25.4 (Berge)**: M is maximum iff no augmenting path exists.
- **Theorem 25.8**: Hopcroft-Karp runs in O(√V·E).
- **Theorem 25.9**: Gale-Shapley always terminates with stable matching.
- **Theorem 25.11**: Proposing side gets best possible partners; other side gets worst.
- **Theorem 25.14**: G_h with perfect matching gives optimal assignment.


### Ch. 26 — Parallel Algorithms

#### Named Entities (Terms & Definitions)
- **Fork-join parallelism**: spawn and sync keywords; parallel for.
- **Work T₁**: Total time on one processor.
- **Span T∞**: Fastest time on unlimited processors (critical path length).
- **Work law**: T_p ≥ T₁/P.
- **Span law**: T_p ≥ T∞.
- **Parallelism**: T₁/T∞ (maximum possible speedup).
- **Greedy scheduler**: Assigns as many ready strands as possible each step.
- **Determinacy race**: Two parallel instructions access same memory, at least one writes.

#### Processes / Algorithms / Pathways

##### P-FIB(n): spawn P-FIB(n-1); P-FIB(n-2); sync.
- Work: Θ(φ^n) (exponential). Span: Θ(n). Parallelism: Θ(φ^n/n).

##### P-MERGE-SORT
- Spawn two recursive calls in parallel; use P-MERGE.
- Work: Θ(n lg n). Span: Θ(lg³ n). Parallelism: Θ(n/lg² n).

##### P-MERGE-AUX (parallel merge)
- Divide-and-conquer: pick median of larger subarray, binary search split point in smaller, place, recurse.
- Work: Θ(n). Span: Θ(lg² n).

#### Formulas & Equations
- Work law: T_p ≥ T₁/P
- Span law: T_p ≥ T∞
- Speedup: T₁/T_p ≤ P
- Parallelism: T₁/T∞
- **Theorem 26.1**: Greedy scheduler: T_p ≤ T₁/P + T∞
- **Corollary 26.2**: Greedy scheduler within factor 2 of optimal

#### Algorithm Parallelism Table
| Algorithm | Work | Span | Parallelism |
|-----------|------|------|-------------|
| P-FIB | Θ(φⁿ) | Θ(n) | Θ(φⁿ/n) |
| P-MAT-VEC | Θ(n²) | Θ(n) | Θ(n) |
| P-MATRIX-MULTIPLY | Θ(n³) | Θ(n) | Θ(n²) |
| P-MERGE-SORT | Θ(n lg n) | Θ(lg³ n) | Θ(n/lg² n) |

### Ch. 27 — Online Algorithms

#### Named Entities
- **Online algorithm**: Receives input over time; decisions without knowing future.
- **Competitive ratio**: max{A(I)/F(I) : I ∈ U} (minimization); c-competitive if ratio ≤ c.
- **Seer / optimal offline**: Knows entire future; benchmark.
- **Move-to-Front (MTF)**: After search, move element to front.
- **Potential function**: Φ_i = 2·I(L^{MTF}_i, L^{OPT}_i) for MTF analysis.

#### Processes / Algorithms / Pathways

##### Elevator vs Stairs Problem
- **Hedge strategy**: Wait k minutes then take stairs. Competitive ratio = 2 (optimal).

##### Move-to-Front (MTF)
- Cost per operation: 2r(x) − 1 (position r, search + swaps).
- **Theorem 27.1**: MTF competitive ratio = 4.
- Proof via potential function (2·inversions).

##### Caching Algorithms
- **LRU**: O(k) competitive ratio.
- **FIFO**: O(k) competitive ratio.
- **LIFO**: Θ(n/k) — unbounded.
- **Any deterministic**: Ω(k) lower bound.
- **RANDOMIZED-MARKING**: O(lg k) expected competitive ratio.

#### Comparisons & Trade-offs
| Algorithm | Competitive Ratio | Notes |
|-----------|------------------|-------|
| Always stairs | k | — |
| Always elevator | B/k | — |
| Hedge (wait k) | 2 | Optimal |
| MTF | 4 | List maintenance |
| LRU | O(k) | Caching |
| RANDOMIZED-MARKING | O(lg k) | Best known |

### Ch. 28 — Matrix Operations

#### Named Entities
- **LUP decomposition**: PA = LU (P = permutation, L = unit lower-triangular, U = upper-triangular).
- **Forward substitution**: Solve Ly = Pb (Θ(n²)).
- **Back substitution**: Solve Ux = y (Θ(n²)).
- **Schur complement**: A' − vw^T/a_{11} (for LU step).
- **Symmetric positive-definite (SPD)**: A = A^T and x^T A x > 0 for all x ≠ 0.
- **Least-squares approximation**: Minimize ||η||² = ||Ac − y||².

#### Processes / Algorithms / Pathways

##### LU-DECOMPOSITION(A, n): Θ(n³). Fails if pivot = 0.
##### LUP-DECOMPOSITION(A, n): Θ(n³). Pivoting for numerical stability.
- Find row with largest |a_{ik}|, swap rows.

##### Matrix Inversion via LUP: Θ(n³)
- Solve AX_i = e_i for each column i.

##### Strassen-based Inversion: O(M(n)) where M(n) = matrix multiplication time.
- Recursively invert SPD submatrices; Schur complement.

##### Least-Squares via Normal Equation: c = (A^T A)^{-1} A^T y

#### Rules, Laws & Theorems
**Theorem 28.1**: Matrix multiplication ≤ Inversion (if inversion takes I(n), multiplication takes O(I(n))).
**Theorem 28.2**: Inversion ≤ Multiplication (if multiplication takes M(n), inversion takes O(M(n))).
**Lemma 28.5 (Schur complement)**: Schur complement of SPD matrix is SPD.
**Corollary 28.6**: LU of SPD has all pivots > 0.

### Ch. 29 — Linear Programming

#### Named Entities
- **Linear programming**: Optimize linear objective subject to linear constraints.
- **Standard form**: max c^T x s.t. Ax ≤ b, x ≥ 0.
- **Feasible solution**: Satisfies all constraints.
- **Unbounded LP**: Feasible region unbounded; no finite optimal.
- **Dual LP**: min b^T y s.t. A^T y ≥ c, y ≥ 0 (for max primal).
- **Weak duality**: c^T x ≤ b^T y for any feasible primal x and dual y.
- **Strong duality**: c^T x* = b^T y* at optimality.

#### Processes / Algorithms / Pathways
- **Simplex algorithm**: Moves along edges of feasible region. Exponential worst-case, fast in practice.
- **Ellipsoid algorithm**: First polynomial-time (Khachian 1979). O(n⁶L). Slow in practice.
- **Interior-point methods**: Polynomial-time, practical (Karmarkar 1984).

#### LP Formulation Examples
- **Shortest paths**: maximize d_t subject to d_s = 0, d_v ≤ d_u + w(u,v).
- **Max flow**: maximize ∑_v f_{sv} − ∑_v f_{vs} subject to capacity + conservation.
- **Minimum-cost flow**: minimize ∑ a(u,v)·f_{uv} subject to flow constraints.

#### Rules, Laws & Theorems
**Lemma 29.1 (Weak duality)**: c^T x ≤ b^T y for all feasible x,y.
**Corollary 29.2**: If c^T x = b^T y, then x,y are optimal.
**Theorem 29.4 (Strong duality)**: If primal and dual are feasible and bounded, c^T x* = b^T y*.
**Theorem 29.5**: Any LP in standard form has finite optimal, is infeasible, or is unbounded.

#### People & Dates
- Dantzig (1947): Simplex.
- Khachian (1979): Ellipsoid.
- Karmarkar (1984): Interior-point.
- Klee & Minty: exponential-time example for simplex.

### Ch. 30 — Polynomials and the FFT

#### Named Entities
- **Polynomial**: A(x) = ∑_{j=0}^{n-1} a_j x^j. Degree-bound n.
- **Coefficient representation**: Vector a = (a₀, a₁, ..., a_{n-1}).
- **Point-value representation**: n pairs {(x_k, y_k)}.
- **DFT (Discrete Fourier Transform)**: y_k = A(ω_n^k) where ω_n = e^{2πi/n}.
- **FFT (Fast Fourier Transform)**: Θ(n lg n) algorithm for DFT.
- **Convolution**: (a ⊗ b)_j = ∑_k a_k·b_{j-k}.

#### Processes / Algorithms / Pathways

##### FFT (Cooley-Tukey)
```
FFT(a, n):
1 if n == 1: return a
2 ω_n = e^{2πi/n}; ω = 1
3 a_even = (a₀, a₂, ..., a_{n-2})
4 a_odd = (a₁, a₃, ..., a_{n-1})
5 y_even = FFT(a_even, n/2)
6 y_odd = FFT(a_odd, n/2)
7 for k = 0 to n/2-1:
8     y_k = y_even_k + ω·y_odd_k
9     y_{k+n/2} = y_even_k − ω·y_odd_k
10    ω = ω·ω_n
11 return y
```
- **Recurrence**: T(n) = 2T(n/2) + Θ(n) → Θ(n lg n).
- Butterfly operation: y_k = even + ω·odd; y_{k+n/2} = even − ω·odd.

##### Polynomial Multiplication via FFT (4 steps)
1. Double degree-bound (add n zero coefficients).
2. Compute DFT (FFT) of order 2n on each polynomial.
3. Pointwise multiply: C(ω_{2n}^k) = A(ω_{2n}^k)·B(ω_{2n}^k).
4. Apply inverse FFT. → Θ(n lg n).

#### Rules, Laws & Theorems
- **Lemma 30.3 (Cancellation lemma)**: ω_{dn}^{dk} = ω_n^k.
- **Lemma 30.5 (Halving lemma)**: Squares of n-th roots = (n/2)-th roots.
- **Lemma 30.6 (Summation lemma)**: ∑_{j=0}^{n-1} (ω_n^k)^j = 0 for k not divisible by n.
- **Theorem 30.8 (Convolution theorem)**: DFT_{2n}(a⊗b) = DFT_{2n}(a)·DFT_{2n}(b).

#### Representations Comparison
| Representation | Evaluation | Addition | Multiplication |
|---------------|-----------|----------|---------------|
| Coefficient | Θ(n) (Horner) | Θ(n) | Θ(n²) naive; Θ(n lg n) via FFT |
| Point-value | Interpolation needed | Θ(n) | Θ(n) |

#### Dates & People
- Cooley & Tukey (1965): FFT. Gauss (1805): earliest known.
- Frigo & Johnson: FFTW library.


### Ch. 31 — Number-Theoretic Algorithms

#### Named Entities (Terms & Definitions)
- **GCD**: Greatest common divisor of a and b (gcd(a,b)).
- **Modular arithmetic**: a ≡ b (mod n) if n | (a−b).
- **Multiplicative inverse**: a⁻¹ mod n exists iff gcd(a,n) = 1.
- **Group Z_n^***: {a ∈ Z_n : gcd(a,n) = 1}; multiplicative group modulo n.
- **Euler's totient φ(n)**: |Z_n^*|.
- **Primitive root**: Generator of Z_n^*.
- **RSA**: Rivest-Shamir-Adleman public-key cryptosystem.
- **Chinese Remainder Theorem**: System of congruences with pairwise coprime moduli.

#### Processes / Algorithms / Pathways

##### EUCLID(a, b) — GCD: O(lg b)
```
EUCLID(a, b)
1 if b == 0: return a
2 else return EUCLID(b, a mod b)
```
- Lame's theorem: EUCLID takes O(lg b) divisions.

##### EXTENDED-EUCLID(a, b) — GCD + Bézout coefficients: O(lg b)
```
EXTENDED-EUCLID(a, b)
1 if b == 0: return (a, 1, 0)
2 else (d, x, y) = EXTENDED-EUCLID(b, a mod b)
3      return (d, y, x − ⌊a/b⌋·y)
```
- Returns (d, x, y) such that d = gcd(a,b) = ax + by.

##### Modular Linear Equations
- Solve ax ≡ b (mod n). Solutions exist iff d = gcd(a,n) divides b. Then d solutions: x_0 + t(n/d) for t = 0,1,...,d−1.

##### Chinese Remainder Theorem
- n = n₁·n₂·...·n_k where n_i pairwise coprime.
- System x ≡ a_i (mod n_i) has unique solution modulo n.
- x = ∑ a_i·c_i·\hat{n}_i where \hat{n}_i = n/n_i, c_i = \hat{n}_i^{-1} (mod n_i).

##### RSA Public-Key Cryptosystem
1. Choose large primes p,q. Compute n = pq, φ(n) = (p−1)(q−1).
2. Choose e with gcd(e, φ(n)) = 1. Compute d = e⁻¹ mod φ(n).
3. Public key: (e, n). Private key: d.
4. Encrypt: c = m^e mod n. Decrypt: m = c^d mod n.
5. Security relies on difficulty of factoring n.

##### PRIMALITY TESTING (Miller-Rabin)
- Probabilistic test. Uses witness a: if a^{n−1} ≠ 1 (mod n) or finds nontrivial square root of 1, n is composite.
- For odd n > 2: write n−1 = 2^s·t (t odd). Check a^t, a^{2t}, a^{4t}, ..., a^{2^{s−1}t} mod n.
- If n is composite, at least 3/4 of a ∈ Z_n^* are witnesses.
- Error probability < 4^{−k} after k independent trials.

#### Formulas & Equations
- gcd(a,b) = gcd(b, a mod b)
- Bézout: ∃x,y: ax + by = gcd(a,b)
- Fermat: a^{p−1} ≡ 1 (mod p) for prime p ∤ a
- Euler: a^{φ(n)} ≡ 1 (mod n) for gcd(a,n) = 1
- RSA: m^{ed} ≡ m (mod n) where ed ≡ 1 (mod φ(n))

### Ch. 32 — String Matching

#### Named Entities
- **Pattern P**: Length m, text T: length n. Find all occurrences of P in T.
- **Suffix**: T[i..j] where j = n. **Prefix**: T[1..i].
- **Suffix array**: Lexicographically sorted suffixes of T.
- **LCP array**: Longest common prefix between consecutive suffixes in suffix array.

#### Processes / Algorithms / Pathways

##### Naive String Matching: O((n−m+1)m)
- Slide pattern over text, compare character by character.

##### Rabin-Karp: O(n) average, O(nm) worst
- Hash pattern. Compute rolling hash for each text substring.
- Hash collision resolved by checking equality.
- Rolling hash: h(T[s+1..s+m]) = (d·(h(T[s..s+m−1]) − T[s+1]·d^{m−1}) + T[s+m+1]) mod q.

##### String Matching with Finite Automata: O(n + m|Σ|)
- Build transition function δ(q, a) for pattern.
- Preprocessing: O(m|Σ|). Matching: Θ(n).

##### KMP (Knuth-Morris-Pratt): O(n + m)
- Compute prefix function π for pattern: length of longest proper prefix that is also suffix.
- Matching: shift pattern using π without backing up text pointer.
- Never re-compares characters matched earlier.

##### Suffix Arrays: O(n) construction
- SA: array of start indices of all suffixes of T in lexicographic order.
- LCP: longest common prefix between SA[i] and SA[i−1].
- Pattern search: binary search on SA using LCP to accelerate → O(m + lg n).

#### Comparisons & Trade-offs
| Algorithm | Preprocessing | Matching | Space |
|-----------|--------------|----------|-------|
| Naive | None | O((n−m+1)m) | O(1) |
| Rabin-Karp | Θ(m) | O(n) avg, O(nm) worst | O(1) |
| Finite automaton | O(m|Σ|) | Θ(n) | O(m|Σ|) |
| KMP | Θ(m) | Θ(n) | Θ(m) |

### Ch. 33 — Machine-Learning Algorithms

#### Named Entities
- **Clustering**: Partition points into groups by similarity.
- **k-median**: Minimize sum of distances from points to nearest cluster center.
- **k-means**: Minimize sum of squared distances.
- **k-means++**: Improved initialization for k-means.
- **Multiplicative weights**: Weighted majority / Hedge algorithm.
- **Gradient descent**: Iteratively move in direction of steepest descent (negative gradient).
- **Loss function**: Measures error of current parameters.

#### Processes / Algorithms / Pathways

##### k-means Clustering
- Initialize k centers. Repeat: assign each point to nearest center; recompute centers as mean of assigned points.
- Hill-climbing: converges to local optimum.
- k-means++: pick first center uniformly; subsequent centers with probability ∝ distance².

##### Multiplicative Weights (Weighted Majority)
- Maintain weights on experts. Predict by weighted majority vote.
- Update: decrease weight of wrong experts by factor (1−ε).
- **Theorem**: Number of mistakes ≤ (1+ε)·(best expert mistakes) + O(log(n)/ε).

##### Gradient Descent
- θ_{t+1} = θ_t − η·∇L(θ_t) where η = learning rate.
- Works for convex loss functions (guaranteed global min).
- Stochastic gradient descent (SGD): use single sample's gradient estimate.

### Ch. 34 — NP-Completeness

#### Named Entities
- **P**: Problems solvable in polynomial time.
- **NP**: Problems verifiable in polynomial time (certificate).
- **NP-complete (NPC)**: NP-hard and in NP.
- **NP-hard**: All NP problems reduce to it.
- **Polynomial-time reduction**: f such that x ∈ A iff f(x) ∈ B; f computable in poly time.
- **Certificate**: Proof that answer is YES, verifiable in poly time.

#### Processes / Algorithms / Pathways
- To prove problem B is NP-complete:
  1. Show B ∈ NP (polynomial-time verifiable).
  2. Reduce known NP-complete problem A to B (A ≤_P B).
  3. Show reduction is polynomial time.

##### Standard NP-Complete Problems (reduction chain)
- **CIRCUIT-SAT** → SAT → 3-CNF-SAT → CLIQUE → VERTEX-COVER → HAM-CYCLE → TSP
- SAT → SUBSET-SUM

##### Well-known NP-Complete Problems
- **SAT**: Boolean formula satisfiability.
- **3-CNF-SAT**: Conjunctive normal form, each clause exactly 3 literals.
- **CLIQUE**: Does graph contain clique of size k?
- **VERTEX-COVER**: Does graph have vertex cover of size k?
- **HAM-CYCLE**: Does graph have Hamiltonian cycle?
- **TSP**: Traveling salesperson with total distance ≤ D.
- **SUBSET-SUM**: Does subset sum to target t?

#### Rules, Laws & Theorems
**Cook-Levin Theorem (1971)**: CIRCUIT-SAT is NP-complete. First NP-complete problem.
If any NP-complete problem has polynomial-time algorithm, then P = NP.

#### Edge Cases & Common Pitfalls
- Some problems seem NP-complete but are in P for restricted inputs (e.g., 2-CNF-SAT).
- Proving NP-completeness via wrong direction: must reduce FROM known NPC TO new problem.
- NP ≠ "not polynomial" — it's nondeterministic polynomial.

### Ch. 35 — Approximation Algorithms

#### Named Entities
- **Approximation algorithm**: Guarantees solution within factor ρ of optimal.
- **ρ-approximation algorithm**: |SOL| ≤ ρ·|OPT| for minimization (SOL/OPT ≤ ρ).
- **PTAS (Polynomial-Time Approximation Scheme)**: (1+ε)-approximation for any ε > 0.
- **FPTAS (Fully PTAS)**: Time polynomial in n and 1/ε.

#### Processes / Algorithms / Pathways

##### Vertex-Cover Approximation (2-approximation)
- Take edge (u,v), add both u,v to cover, remove all incident edges. Repeat.

##### TSP Approximation
- **With triangle inequality**: MST-based (double-tree) gives 2-approx; Christofides gives 1.5-approx.
- **Without triangle inequality**: No polynomial-time ρ-approximation for any ρ (unless P=NP).

##### Set-Cover Approximation (greedy)
- Repeatedly pick set that covers most uncovered elements.
- H(d)-approximation where d = max set size. H(d) = 1 + 1/2 + ... + 1/d = ln d + O(1).

##### Subset-Sum (FPTAS)
- Dynamic programming with scaling: discard low-order bits to get polynomial time.
- O(n²/ε) time; produces solution ≥ (1−ε)·OPT.

#### Comparisons & Trade-offs
| Problem | Approximation | Method |
|---------|-------------|--------|
| Vertex cover | 2-approximation | Maximal matching |
| TSP (triangle inequality) | 1.5-approximation (Christofides) | MST + perfect matching |
| Set cover | H(d)-approximation | Greedy |
| Subset-sum | FPTAS (1−ε) | Scaled DP |
| Max clique | No constant factor (unless P=NP) | — |


### Appendix A — Summations

#### Named Entities
- **Arithmetic series**: Σ_{k=1}^n k = n(n+1)/2.
- **Geometric series**: Σ_{k=0}^n x^k = (x^{n+1}−1)/(x−1) for x ≠ 1.
- **Infinite decreasing geometric series**: Σ_{k=0}∞ x^k = 1/(1−x) for |x| < 1.
- **Harmonic series**: H_n = Σ_{k=1}^n 1/k = ln n + γ + O(1/n). γ ≈ 0.57721 (Euler's constant).
- **Telescoping series**: Σ_{k=1}^n (a_k − a_{k-1}) = a_n − a_0.

#### Formulas & Equations
- Σ k = n(n+1)/2
- Σ k² = n(n+1)(2n+1)/6
- Σ k³ = n²(n+1)²/4
- Σ_{k=0}∞ k x^k = x/(1−x)² for |x| < 1
- Σ_{k=0}∞ k² x^k = x(1+x)/(1−x)³

#### Bounding Techniques
1. **Induction**: Prove base, assume for n, prove n+1. Must use same constant for all n.
2. **Bounding terms**: Σ a_k ≤ n·a_max. Ratio method if a_{k+1}/a_k ≤ r < 1.
3. **Splitting sums**: Partition range into pieces; bound each.
4. **Integral approximation**: ∫_{0}^{n} f(x)dx ≤ Σ_{k=1}^n f(k) ≤ ∫_{1}^{n+1} f(x)dx for monotone increasing f. Reverse for decreasing f.

### Appendix B — Sets, Etc.

#### Sets
- **Operations**: ∪ (union), ∩ (intersection), − (difference), complement.
- **DeMorgan's laws**: A∩B = Ā∪B̄, A∪B = Ā∩B̄.
- **Principle of inclusion-exclusion**: |∪A_i| = Σ|A_i| − Σ|A_i∩A_j| + Σ|A_i∩A_j∩A_k| − ... + (−1)^{n−1}|∩A_i|.

#### Relations
- **Equivalence relation**: Reflexive + Symmetric + Transitive. Equivalence classes form partition.
- **Partial order**: Reflexive + Antisymmetric + Transitive.
- **Total order**: Partial order that is total.

#### Functions
- **Injection (one-to-one)**: a≠a' ⇒ f(a)≠f(a').
- **Surjection (onto)**: Range = Codomain.
- **Bijection**: Both injective and surjective.

#### Graphs (see also Ch 20)
- **Connected**: Every vertex reachable from all others.
- **Free tree**: Connected + acyclic + |E| = |V| − 1.
- **Theorem B.2**: Six equivalent definitions of free tree.

#### Trees
- **Rooted tree**: Distinguished root. Parent, child, ancestor, descendant.
- **Binary tree**: Left/right children (position matters).
- **Full binary tree**: Every node has 0 or 2 children.
- **Complete k-ary tree**: Leaves at same depth; internal nodes have k children.
- **Kraft inequality**: Σ_{leaves} 2^{−depth} ≤ 1.

### Appendix C — Counting and Probability

#### Counting
- k-strings over n-set: n^k
- Permutations: n!
- k-permutations: n!/(n−k)!
- k-combinations: C(n,k) = n!/(k!(n−k)!)
- **Binomial theorem**: (x+y)^n = Σ_{k=0}^n C(n,k) x^k y^{n−k}
- **Stirling upper bound**: C(n,k) ≤ (en/k)^k

#### Probability Axioms
1. Pr{A} ≥ 0
2. Pr{S} = 1
3. Pr{∪A_i} = Σ Pr{A_i} for disjoint events

#### Random Variables
- **Expectation**: E[X] = Σ x·Pr{X=x}. Linearity: E[X+Y] = E[X] + E[Y].
- **Variance**: Var[X] = E[(X−μ)²] = E[X²] − E²[X].
- **Markov's inequality**: Pr{X ≥ t} ≤ E[X]/t.
- **Jensen's inequality**: f(E[X]) ≤ E[f(X)] for convex f.

#### Distributions
- **Geometric**: Pr{X=k} = (1−p)^{k−1}p. E[X] = 1/p. Var = (1−p)/p².
- **Binomial**: b(k;n,p) = C(n,k) p^k (1−p)^{n−k}. E[X] = np. Var = np(1−p).
- **Chernoff bound**: Pr{X ≥ r} < (np/r)^r e^{r−np} for r > np.

### Appendix D — Matrices

#### Named Entities
- **Matrix**: Rectangular array A = (a_{ij}) ∈ ℝ^{m×n}.
- **Transpose**: (A^T)_{ij} = a_{ji}.
- **Square matrix types**: diagonal, identity, tridiagonal, upper/lower-triangular, permutation, symmetric.
- **Determinant**: det(A) = Σ a_{ij}·(−1)^{i+j}·det(A[ij]).
- **Rank**: Maximum number of linearly independent rows/columns.
- **Positive-definite**: x^T A x > 0 for all x ≠ 0.

#### Matrix Operations
- **Addition**: C = A + B (c_{ij} = a_{ij} + b_{ij}).
- **Multiplication**: (AB)_{ij} = Σ_k a_{ik}b_{kj}. NOT commutative.
- **Inner product**: ⟨x,y⟩ = x^T y = Σ x_i y_i.
- **Outer product**: (xy^T)_{ij} = x_i y_j.

#### Properties
- **Theorem D.1**: Square matrix has full rank ⇔ nonsingular (inverse exists).
- **Theorem D.4**: det(AB) = det(A)·det(B). Row swap flips sign.
- **Theorem D.5**: A is singular ⇔ det(A) = 0.
- **Theorem D.6**: A^T A is positive-definite if A has full column rank.



---

## Cross-Cutting Topics

### Design Paradigms & Meta-Methods

1. **Divide and Conquer** — (Ch 2, 4) Split problem into independent subproblems, solve recursively, combine. Examples: merge sort, Strassen, FFT. Recurrence: T(n) = aT(n/b) + f(n). Master theorem solves in 3 cases.

2. **Dynamic Programming** — (Ch 14) Overlapping subproblems + optimal substructure. Two implementations: top-down with memoization (recursion + table) and bottom-up (iterative, all subproblems). Four-step method: (1) characterize structure, (2) define recursively, (3) compute value, (4) construct solution. Examples: rod cutting (Θ(n²)), matrix-chain (O(n³)), LCS (Θ(mn)), OBST (Θ(n³)).

3. **Greedy Algorithms** — (Ch 15) Greedy-choice property + optimal substructure. Make locally optimal choice first, leaving one subproblem. Examples: activity selection (Θ(n)), Huffman codes (O(n lg n)), fractional knapsack, offline caching. Proves optimality via exchange argument.

4. **Amortized Analysis** — (Ch 16) Average per-operation cost over worst-case sequence. Three methods: aggregate (T(n)/n), accounting (charge + credit), potential (Φ function). Examples: MULTIPOP, binary counter (O(1) amortized per INCREMENT), dynamic tables (O(1) amortized per INSERT).

5. **Randomization** — (Ch 5, 7, 9) Uses random number generator in algorithm. Benefits: no worst-case input (randomized quicksort), expected linear time (RANDOMIZED-SELECT), probabilistic primality testing. Analysis uses indicator random variables + linearity of expectation.

6. **Fork-Join Parallelism** — (Ch 26) spawn/sync keywords. Work T₁ (sequential), span T∞ (critical path). Greedy scheduling: T_p ≤ T₁/P + T∞. Parallelism = T₁/T∞.

7. **Online Algorithms** — (Ch 27) Input arrives over time. Competitive analysis vs optimal offline. Examples: MTF (competitive ratio 4), LRU (O(k)), RANDOMIZED-MARKING (O(lg k)).

8. **Augmenting Data Structures** — (Ch 17) Add fields, maintain invariants, implement new operations. Theorem 17.1: if field computable from children in O(1) and rotation-maintainable in O(1), RB operations stay O(lg n). Examples: order-statistic trees (size), interval trees (max).

### Proof & Argument Patterns

1. **Loop Invariants** — Used for iterative algorithm correctness. Three parts: (a) Initialization: invariant holds before first iteration; (b) Maintenance: if holds before iteration, holds after; (c) Termination: invariant + loop condition gives correctness. Classic: INSERTION-SORT, PARTITION, HEAPSORT, BUILD-MAX-HEAP.

2. **Induction** — For recursive algorithms and structural properties. Base case + inductive step. Uses: BST inorder walk (Θ(n)), red-black tree height bound (Lemma 13.1), free tree properties (Theorem B.2).

3. **Substitution Method** — For solving recurrences. (1) Guess form; (2) verify by induction; (3) solve for constants. Example: T(n) = 2T(n/2) + n, guess T(n) ≤ cn lg n.

4. **Recursion Tree Method** — Draw tree where each node = cost of subproblem. Sum costs per level, total across levels. Useful for guessing form for substitution method.

5. **Cut-and-Paste** — For optimal substructure. Assume subproblem solution is not optimal; cut it out and paste in optimal one; derive contradiction with optimality of original solution. Used in DP (rod cutting, LCS).

6. **Exchange Argument** — For greedy correctness. Take any optimal solution; swap non-greedy element with greedy element without worsening solution; iteratively transform to greedy solution. Used in activity selection (Theorem 15.1), Huffman codes (Lemma 15.2).

7. **Cut Property** — MST correctness: any light edge crossing cut that respects A is safe for A (Theorem 21.1). Used to prove Kruskal and Prim.

8. **Max-Flow Min-Cut Theorem** (24.6): Three equivalent statements — f is max flow; G_f has no augmenting path; |f| = c(S,T) for some cut. Foundation of flow theory.

9. **Potential Method** — For amortized analysis. Φ maps data structures to reals. ĉ_i = c_i + Φ(D_i) − Φ(D_{i-1}). Total cost = ∑c_i + Φ(D_n) − Φ(D_0). Example: dynamic table with Φ = 2·num − size.

10. **Reduction** — For NP-completeness. Given known NP-complete A, reduce A ≤_P B to show B is NP-complete. Must reduce FROM known NPC TO new problem.

11. **Parenthesis Theorem** (20.7) — DFS intervals: for any u,v, intervals are either disjoint or one contains the other. White-path theorem (20.9): v is descendant of u iff white-path exists at u.d.

12. **Pigeonhole Principle** — Used in: hashing collisions, comparison sort lower bound, Hall's theorem.

### Probability & Statistics Foundation

(from Appendix C, Ch 5)

- **Indicator random variables**: E[I{A}] = Pr{A}. Sum of indicators → expected count.
- **Linearity of expectation**: E[X+Y] = E[X] + E[Y]. Holds even if X,Y dependent. Critical for analyzing randomized algorithms.
- **Variance**: Var[X] = E[X²] − E²[X]. Standard deviation σ = √Var.
- **Bernoulli trial**: Single success/failure experiment. E[X] = p, Var[X] = p(1−p).
- **Binomial distribution**: b(k;n,p) = C(n,k) p^k (1−p)^{n−k}. k successes in n independent Bernoulli trials. E[X] = np. Var[X] = np(1−p).
- **Geometric distribution**: Pr{X=k} = (1−p)^{k−1}p. Number of trials until first success. E[X] = 1/p. Var[X] = (1−p)/p².
- **Markov's inequality**: Pr{X ≥ t} ≤ E[X]/t for nonnegative X. Weak but general.
- **Chernoff bound**: Pr{X ≥ r} < (np/r)^r e^{r−np} for r > np (binomial). Strong exponential tail bound.
- **Union bound (Boole's inequality)**: Pr{∪A_i} ≤ Σ Pr{A_i}. Used in: hashing analysis, randomized algorithm error bounds.
- **Bayes' theorem**: Pr{A|B} = Pr{A}·Pr{B|A} / Pr{B}. Updated beliefs given evidence.
- **Conditional probability**: Pr{A|B} = Pr{A∩B}/Pr{B}.
- **Jensen's inequality**: f(E[X]) ≤ E[f(X)] for convex f. Used for lower bounds.

### Mnemonics & Memory Aids

- **Big-O ordering**: "1 < lg n < n < n lg n < n² < n³ < 2ⁿ < n!" (constant-log-linear-linearithmic-quadratic-cubic-exponential-factorial)
- **Master Theorem Cases**: Compare f(n) with n^{log_b a}. f(n) is smaller → case 1 (Θ(n^{log_b a})). f(n) is equal → case 2 (Θ(n^{log_b a} lg n)). f(n) is larger and regular → case 3 (Θ(f(n))).
- **DFS Edge Colors**: "White → Tree, Gray → Back, Black → Forward/Cross"
- **Red-Black Properties**: "Root-Black, Leaves-Black, No-Red-Red, Equal-Black-Count" (RB-5: root-black, leaf-black, red-no-red-children, equal-black-paths)
- **DP Steps**: "Characterize, Define, Compute, Construct" (4-step method)
- **Greedy Requirements**: "Greedy Choice + Optimal Substructure" (both required)
- **Amortized Methods**: "Aggregate (total/n), Accounting (charge + credit), Potential (Φ function)"
- **Graph Algorithm Times**: BFS=O(V+E), DFS=Θ(V+E), TopSort=Θ(V+E), SCC=Θ(V+E), Dijkstra=O(E lg V), Bellman-Ford=O(VE), Prim=O(E lg V), Kruskal=O(E lg V), Floyd-Warshall=Θ(V³)
- **NP-Completeness Chain**: "CIRCUIT-SAT → SAT → 3-CNF-SAT → CLIQUE → VERTEX-COVER → HAM-CYCLE → TSP" and "SAT → SUBSET-SUM"
- **Flow Conservation**: "Flow In = Flow Out" (for all nodes except source/sink)
- **Five Sorting Algorithms**: "Insertion O(n²), Merge O(n lg n), Heap O(n lg n), Quick Θ(n²) worst Θ(n lg n) avg, Counting Θ(n+k)" — know which are comparison-based, stable, in-place

### People & Dates

- **C.A.R. Hoare** (1960/1962): Quicksort
- **John von Neumann**: Mergesort
- **Edsger Dijkstra** (1959): Dijkstra's algorithm
- **Robert Floyd**: Floyd-Warshall (1962)
- **J.B.J. Fourier / Cooley & Tukey** (1965): FFT; Gauss found it first (1805)
- **Rivest, Shamir, Adleman** (1977): RSA cryptosystem
- **Dantzig** (1947): Simplex algorithm for LP
- **Khachian** (1979): Ellipsoid algorithm (first poly-time LP)
- **Karmarkar** (1984): Interior-point method for LP
- **Cook, Karp, Levin** (1971-1972): NP-completeness theory
- **Cook** (1971): Cook-Levin theorem (SAT is NP-complete)
- **Hopcroft & Karp** (1973): O(√V·E) bipartite matching
- **Gale & Shapley** (1962): Stable marriage algorithm
- **Sleator & Tarjan**: Amortized analysis, splay trees, competitive analysis (MTF)
- **Bayer & McCreight**: B-trees
- **Kruskal** (1956): MST algorithm
- **Prim / Jarník** (~1930/1957): MST algorithm
- **Bellman & Ford** (1958): Bellman-Ford shortest paths
- **Knuth, Morris, Pratt** (1977): KMP string matching
- **Carter & Wegman** (1979): Universal hashing
- **Huffman** (1952): Huffman coding
- **Strassen** (1969): O(n^lg7) matrix multiplication
- **Thorup**: O(V+E) undirected shortest paths (integer weights)
- **Cormen, Leiserson, Rivest, Stein**: CLRS textbook authors

---

## Exam Questions by Type

### MCQ

1. **Q:** What is the worst-case running time of quicksort?  
   **A:** Θ(n²).  
   **Distractor:** Θ(n lg n) — that's average-case.  
   **Distractor:** Θ(n) — only if input already sorted in best-case for some variants.

2. **Q:** Which data structure gives O(1) amortized insert and O(lg n) extract-max?  
   **A:** Binary heap.  
   **Distractor:** BST — O(h) where h can be O(n) in worst case.

3. **Q:** The Floyd-Warshall algorithm solves which problem?  
   **A:** All-pairs shortest paths.  
   **Distractor:** Single-source shortest paths — that's Dijkstra.  
   **Distractor:** Minimum spanning tree — that's Prim/Kruskal.

4. **Q:** A red-black tree with n internal nodes has height at most:  
   **A:** 2 lg(n+1).  
   **Distractor:** lg(n+1) — that's the height bound for AVL trees.  
   **Distractor:** n — a red-black tree never degenerates to linear chain.

5. **Q:** Which of the following is NOT a comparison sort?  
   **A:** Counting sort.  
   **Distractor:** Heapsort, mergesort, quicksort — all are comparison sorts.

6. **Q:** The master theorem case 2 applies when f(n) = Θ(n^{log_b a} lg^k n). What is the solution?  
   **A:** T(n) = Θ(n^{log_b a} lg^{k+1} n).  
   **Distractor:** T(n) = Θ(n^{log_b a} lg^k n) — missing +1 in the lg exponent.

7. **Q:** In a flow network, the max flow value equals:  
   **A:** The capacity of the minimum cut.  
   **Distractor:** The capacity of the maximum cut — opposite of min cut.

8. **Q:** What is the competitive ratio of LRU caching?  
   **A:** O(k).  
   **Distractor:** O(lg k) — that's RANDOMIZED-MARKING.  
   **Distractor:** Θ(n/k) — that's LIFO.

9. **Q:** Which property must a relation satisfy to be a partial order?  
   **A:** Reflexive + Antisymmetric + Transitive.  
   **Distractor:** Reflexive + Symmetric + Transitive — that's equivalence relation.

10. **Q:** What is the amortized cost of TABLE-INSERT using the accounting method?  
    **A:** 3.  
    **Distractor:** 1 — that's the actual cost of a non-expanding insert.  
    **Distractor:** 2 — doesn't account for reinsertion of existing items.

### Short Answer

1. **Q:** State the three properties a relation must satisfy to be an equivalence relation.  
   **Rubric:** Reflexive (1pt): a R a for all a. Symmetric (1pt): a R b ⇒ b R a. Transitive (1pt): a R b ∧ b R c ⇒ a R c.

2. **Q:** What is the difference between DP and divide-and-conquer?  
   **Rubric:** DP has overlapping subproblems (2pt); D&C has disjoint subproblems (2pt). Both require optimal substructure (1pt). DP saves results in table; D&C recomputes.

3. **Q:** Define the greedy-choice property.  
   **Rubric:** A globally optimal solution can be assembled by making locally optimal choices (3pt). Must prove greedy choice is part of some optimal solution (2pt).

4. **Q:** What does it mean for a problem to be NP-complete?  
   **Rubric:** (1) Problem is in NP — verifiable in polynomial time (2pt). (2) Problem is NP-hard — all NP problems reduce to it in polynomial time (3pt).

5. **Q:** Explain the three methods of amortized analysis.  
   **Rubric:** Aggregate — compute total cost T(n), divide by n (2pt). Accounting — assign differing amortized costs, maintain nonnegative credit (2pt). Potential — Φ function; ĉ_i = c_i + ΔΦ (1pt).

6. **Q:** When can a hash table use open addressing?  
   **Rubric:** Load factor α ≤ 1 (1pt). Deletion requires care — use DELETED marker or special linear probing delete (2pt). Must guarantee probe sequence covers all slots (2pt).

### Trace / Apply

1. **Input:** A = 〈5, 2, 4, 6, 1, 3〉. Apply INSERTION-SORT step by step.  
   **Expected output:** 〈1, 2, 3, 4, 5, 6〉.  
   **Key invariant:** After processing A[j], A[1..j] is sorted.

2. **Input:** Graph edges (s,a,10), (s,b,5), (a,b,2), (a,t,1), (b,a,3), (b,t,9). Run Dijkstra from s.  
   **Expected:** s.d=0, b.d=5, a.d=7 (via s→b→a), t.d=8 (via s→b→a→t).  
   **Why:** b relaxes first (extract-min b=5). Then (b,a) relaxes a.d from 10→7. Then (a,t) relaxes t.d from 9→8.

3. **Input:** X=〈ABCBDAB〉, Y=〈BDCABA〉. Find LCS.  
   **Expected:** "BCBA", "BDAB", or "BCAB" — all length 4.  
   **Method:** Fill LCS table c[1..m,1..n]; trace back via arrows.

4. **Input:** Items (w,v): (10,60), (20,100), (30,120). Capacity W=50. Solve fractional knapsack.  
   **Expected:** Item 1 (10/60) all, item 2 (20/100) all, item 3 (20/80) 2/3. Total = 240.  
   **Why:** Sort by v/w: item1=6, item2=5, item3=4. Take greedily.

5. **Trace HEAPSORT on** A = 〈5, 13, 2, 25, 7, 17, 20, 8, 4〉.  
   **Expected after BUILD-MAX-HEAP:** 〈25, 13, 20, 8, 7, 17, 2, 5, 4〉.  
   **Final sorted:** 〈2, 4, 5, 7, 8, 13, 17, 20, 25〉.

6. **Trace PARTITION on** A = 〈13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11〉.  
   **Expected output:** pivot at position 8 with value 11.  
   **Low side:** 〈9, 5, 8, 7, 4, 2, 6〉. **High side:** 〈21, 13, 19, 12〉.

### Diagram Label

1. **Diagram:** Complete red-black tree. **Label:** Root (black), red nodes (2 children black), NIL leaves (black), black-height. Show that longest path (alternating red-black) ≤ 2× shortest (all black).

2. **Diagram:** Flow network with source s, sink t. **Label:** Capacity, flow, residual edges, augmenting path, cut (S,T). Show max-flow = min-cut.

3. **Diagram:** Decision tree for comparison sort on 3 elements. **Label:** Internal node = comparison, leaf = permutation. Show 3! = 6 leaves, height ≥ lg(3!) = Ω(lg 6) = Ω(3 lg 3).

4. **Diagram:** BFS tree. **Label:** Source s, distances d, queue Q with gray vertices. Show waves of discovery.

5. **Diagram:** Red-black tree insertion. **Label:** Cases 1, 2, 3. Show rotation and recoloring steps.

### Essay / Long-Form

1. **Q:** Compare and contrast dynamic programming and greedy algorithms. When would you use each?  
   **Key points:** Both require optimal substructure. DP has overlapping subproblems (solved once, cached); greedy makes locally optimal choice leaving one subproblem. DP: bottom-up or top-down memoization. Greedy: prove greedy-choice property via exchange argument. Examples: 0-1 knapsack (DP) vs fractional knapsack (greedy). DP generally O(n²) or O(n³); greedy O(n) or O(n lg n). Choose DP when overlapping subproblems and no greedy choice exists.

2. **Q:** Explain NP-completeness and its implications for algorithm design.  
   **Key points:** P = poly-time decidable; NP = poly-time verifiable; NPC = NP-hard + NP. Cook-Levin: SAT is first NPC problem. Reductions chain NPC problems together. P=NP? is open problem. Implications: for NPC problems, design approximation algorithms (TSP: Christofides 1.5-approx), heuristics (simulated annealing, genetic), FPTAS (subset-sum), or exact exponential for small n. Always prove NPC before concluding no efficient algorithm exists.

3. **Q:** Describe how max flow can be used to solve bipartite matching.  
   **Key points:** Construct flow network: source→L_i (capacity 1), L_i→R_j (capacity 1 if edge exists), R_j→sink (capacity 1). Integrality theorem ensures integer flow values. Max-flow = max-cardinality matching. Time: O(VE) via Ford-Fulkerson (each augmenting path adds 1 to matching). Hopcroft-Karp improves to O(√V·E). Weighted bipartite matching → min-cost flow or Hungarian algorithm.

4. **Q:** Explain the fork-join parallelism model. What is the significance of work and span?  
   **Key points:** spawn = potential parallelism; sync = barrier. Work T₁ = sequential time; Span T∞ = critical path. Work law: T_p ≥ T₁/P. Span law: T_p ≥ T∞. Parallelism = T₁/T∞ (max speedup). Greedy scheduling achieves T_p ≤ T₁/P + T∞. Applications: parallel merge sort (parallelism Θ(n/lg² n)), parallel matrix multiplication. Determinacy races occur when parallel code shares writable data.

5. **Q:** Analyze the performance of hash tables. Compare chaining vs open addressing.  
   **Key points:** Chaining: α = n/m. Expected search Θ(1+α). Simple, handles α > 1. Open addressing: α ≤ 1. Expected probes: ≤ 1/(1−α) for unsuccessful search. Linear probing: primary clustering, good cache locality. Double hashing: Θ(m²) probe sequences, avoids clustering. Universal hashing: guarantees Pr[collision] ≤ 1/m. Practical: choose simple hash function (multiply-shift) and consider memory hierarchy.

