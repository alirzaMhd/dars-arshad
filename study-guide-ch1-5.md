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
