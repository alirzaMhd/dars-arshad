# Study Guide: Introduction to Algorithms (CLRS 4th Edition)

> Generated 2026-06-04. Subject: Computer Science / Algorithms. Exam format: Mixed (problem-solving, short answer, MCQ). Coverage: comprehensive.
> Target length: ~5000 lines.

## Chapter-by-Chapter Breakdown

### Ch. 1 — The Role of Algorithms in Computing

**Named Entities (Terms & Definitions)**
- **Algorithm**: well-defined computational procedure that takes input and produces output in finite time
- **Correct algorithm**: halts with correct output for every problem instance
- **Problem instance**: input needed to compute a solution
- **Sorting problem formal definition**: Input: sequence ⟨a1,a2,...,an⟩. Output: permutation ⟨a'1,a'2,...,a'n⟩ with a'1 ≤ a'2 ≤ ... ≤ a'n
- **Data structure**: way to store and organize data to facilitate access and modifications
- **NP-complete**: problems with no known efficient algorithm; if efficient algorithm exists for one, then for all; use approximation algorithms instead
- **Online algorithms**: input arrives over time, must decide without knowing future
- **Task-parallel algorithms**: designed for multicore processors (Ch 26)

**Key Comparisons**
- Efficient algorithms matter more than fast hardware: insertion sort Θ(n²) vs merge sort Θ(n lg n). At n=10M, a slow computer running merge sort can beat a fast computer running insertion sort (17x faster)
- Key comparison: insertion sort (c₁·n²) vs merge sort (c₂·n·lg n). Crossover point exists where merge sort becomes faster despite larger constant

**Applications**
- Human Genome Project (DP for DNA similarity), internet routing (shortest paths), e-commerce (RSA cryptography), resource allocation (linear programming), compression (Huffman coding)
- Sorting is fundamental operation; algorithm choice depends on n, pre-sortedness, value restrictions, architecture, storage type
- Traveling-salesperson problem (NP-complete): find shortest route visiting all cities and returning

---

### Ch. 2 — Getting Started

**Named Entities (Terms & Definitions)**
- **Sorting problem**: Input: sequence of n numbers ⟨a₁, a₂, …, aₙ⟩. Output: permutation ⟨a′₁, a′₂, …, a′ₙ⟩ such that a′₁ ≤ a′₂ ≤ … ≤ a′ₙ.
- **Key**: The value to be sorted. **Satellite data**: Associated data that travels with the key. **Record**: A key plus satellite data.
- **Pseudocode**: Uses indentation for block structure, `//` for comments, `=` for assignment, `:` for subarray notation.
- **Insertion sort**: Builds sorted array one element at a time by inserting next element into correct position.
- **Loop invariant**: Property that holds before each iteration; used to prove correctness (Initialization, Maintenance, Termination).
- **RAM model**: Generic one-processor computational model; instructions execute one after another, each taking constant time.
- **Input size**: For sorting, number n of items; for integer multiplication, number of bits.
- **Running time**: Number of instructions and data accesses executed.
- **Order of growth**: Rate at which running time increases as n grows; focus on leading term, ignoring constants and lower-order terms.
- **Θ-notation (informal)**: "Roughly proportional when n is large."
- **Incremental method**: Build solution by adding one element at a time (insertion sort).
- **Divide-and-conquer**: Break into subproblems, solve recursively, combine solutions.
- **Merge sort**: Divide-and-conquer sort: divide in half, recursively sort each, merge sorted halves.
- **Inversion**: Pair (i,j) with i < j and A[i] > A[j].
- **Theorem 2.1**: Any comparison sort can be augmented to count inversions in O(n lg n) time.
- **Bubble sort** sorts by swapping adjacent inversions; Θ(n²) compares/swaps worst-case.
- **Number of inversions**: Any sequence has between 0 and C(n,2) inversions. Average: n(n-1)/4.

**HORNER'S RULE** (Problem 2-3): Evaluate polynomial P(x) = Σ a_i x^i in Θ(n).
```
y = 0
for i = n down to 0
    y = a_i + x·y
```
- Loop invariant: y = Σ_{k=i}^{n} a_k x^{k-i} after iteration i.
- **Naive evaluation**: Θ(n²). Horner: Θ(n). Key difference: no repeated exponentiation.

**INSERTION-SORT(A, n)**
- Input: Array A[1:n], integer n. Output: A[1:n] sorted.
- Steps:
  1. `for i = 2 to n`
  2. `key = A[i]`
  3. `j = i - 1`
  4. `while j > 0 and A[j] > key`
  5. `A[j+1] = A[j]`
  6. `j = j - 1`
  7. `A[j+1] = key`
- **Loop invariant**: At start of each iteration, A[1:i-1] is sorted and contains original elements.
- **Complexity**: Best Θ(n), worst Θ(n²), average Θ(n²).

**MERGE(A, p, q, r)**
- Merge two sorted subarrays A[p:q] and A[q+1:r] into sorted A[p:r].
- Steps: Copy to L and R arrays, then merge by comparing smallest remaining.
- Complexity: Θ(n) where n = r-p+1.
- **Invariant**: A[p:k-1] contains k-p smallest elements of L and R in sorted order.

**MERGE-SORT(A, p, r)**
```
if p ≥ r
    return
q = ⌊(p+r)/2⌋
MERGE-SORT(A, p, q)
MERGE-SORT(A, q+1, r)
MERGE(A, p, q, r)
```
- Recurrence: T(n) = 2T(n/2) + Θ(n) → Θ(n lg n).
- **Proof by recursion tree**: n + n + ... + n (lg n times) = n lg n.
- **Space**: Θ(n) auxiliary for merge.

**Selection Sort**
```
for i = 1 to n-1
    min = i
    for j = i+1 to n
        if A[j] < A[min]
            min = j
    swap A[i] with A[min]
```
- Loop invariant: A[1:i-1] sorted with i-1 smallest elements.
- Complexity: Θ(n²) worst, best, and average.
- In-place, not stable (long-distance swaps).

**Binary Search**
```
left = 1, right = n
while left ≤ right
    mid = ⌊(left+right)/2⌋
    if A[mid] == key return mid
    if A[mid] < key left = mid+1
    else right = mid-1
return NIL
```
- Precondition: A is sorted. Θ(lg n) worst-case.
- Invariant: key ∈ A[left:right] if key ∈ A at all. Correctness via bisection.
- Variant: interpolation search O(lg lg n) for uniform distribution.

**Loop Invariant Proof Pattern**
1. **Initialization**: Invariant true before first iteration
2. **Maintenance**: If true before iteration, remains true before next
3. **Termination**: Loop terminates; invariant + termination gives correctness

**Comparisons**
| Dimension | Insertion Sort | Merge Sort |
|-----------|---------------|------------|
| Worst-case | Θ(n²) | Θ(n lg n) |
| Best-case | Θ(n) | Θ(n lg n) |
| In-place | Yes | No |
| Method | Incremental | Divide-and-conquer |

**Formulas**: Merge sort recurrence T(n) = 2T(n/2) + Θ(n). General D&C: T(n) = aT(n/b) + D(n) + C(n).

**End-of-Chapter**: Exercises 2.1-1 through 2.3-6; Problems 2-1 (coarsening), 2-2 (bubblesort), 2-3 (Horner's rule), 2-4 (inversions).

---

### Ch. 3 — Characterizing Running Times

**Asymptotic Notations**
- **O-notation** (big-oh): O(g(n)) = {f(n): ∃ c > 0, n₀ > 0 such that 0 ≤ f(n) ≤ cg(n) for all n ≥ n₀}. Asymptotic upper bound.
- **Ω-notation** (big-omega): Ω(g(n)) = {f(n): ∃ c > 0, n₀ > 0 such that 0 ≤ cg(n) ≤ f(n) for all n ≥ n₀}. Asymptotic lower bound.
- **Θ-notation** (theta): Θ(g(n)) = {f(n): ∃ c₁, c₂ > 0, n₀ > 0 such that 0 ≤ c₁g(n) ≤ f(n) ≤ c₂g(n)}. Tight bound.
- **o-notation** (little-oh): f(n) ∈ o(g(n)) if ∀ c > 0 ∃ n₀: 0 ≤ f(n) < cg(n). Equivalently lim f(n)/g(n) = 0. Not asymptotically tight.
- **ω-notation** (little-omega): f(n) ∈ ω(g(n)) if ∀ c > 0 ∃ n₀: 0 ≤ cg(n) < f(n). Equivalently lim f(n)/g(n) = ∞.

**Theorem 3.1**: f(n) = Θ(g(n)) iff f(n) = O(g(n)) AND f(n) = Ω(g(n)).

**Asymptotic Analogy to Real Numbers**: O = ≤, Ω = ≥, Θ = =, o = <, ω = >. **Asymptotic trichotomy does NOT hold** (e.g., n and n^(1+sin n) are incomparable).

**Properties**: Transitivity, reflexivity, symmetry (Θ only), transpose symmetry.
- **Transpose symmetry**: f = O(g) ⇔ g = Ω(f). f = o(g) ⇔ g = ω(f).
- **Use in equations**: 2n² + 3n + 1 = Θ(n²) means ∃ c₁,c₂,n₀ with c₁·n² ≤ 2n²+3n+1 ≤ c₂·n².
- **Multiple variables**: f(m,n) = O(g(m,n)) if ∃ c,m₀,n₀ with f(m,n) ≤ c·g(m,n) for all m≥m₀,n≥n₀.

**Limits and Asymptotics**:
- If lim_{n→∞} f(n)/g(n) = 0 → f = o(g)
- If lim_{n→∞} f(n)/g(n) = c > 0 → f = Θ(g)
- If lim_{n→∞} f(n)/g(n) = ∞ → f = ω(g)
- L'Hôpital's rule: lim f/g = lim f′/g′ when limits exist.

**Standard Function Growth**:
- **Constant functions**: f(n) = c → Θ(1) < Θ(lg n)
- **Logarithmic**: lgⁱ n, i ∈ ℕ. All logarithms are Θ of each other: log_a n = Θ(log_b n) for a,b>1.
- **Polylog vs polynomial**: lg^b n = o(n^a) for any a>0, b>0.
- **Polynomial vs exponential**: n^b = o(a^n) for any a>1, b>0.
- **Factorial**: n! = ω(2^n) and n! = o(n^n).
- **Growth order**: 1 ≺ lg n ≺ √n ≺ n ≺ n lg n ≺ n√n ≺ n² ≺ n³ ≺ 2ⁿ ≺ n!
- Polynomial: p(n) = Θ(n^d) (leading term)
- Exponentials (a>1) grow faster than any polynomial: lim n^b / a^n = 0
- Polynomials grow faster than polylogs: lim lg^b n / n^a = 0
- Stirling's approximation: n! = √(2πn)(n/e)^n (1 + Θ(1/n))
- Iterated logarithm lg* n: min{i ≥ 0: lg^(i) n ≤ 1}
- Fibonacci: F_i = ⌊ϕ^i/√5 + 1/2⌋, ϕ = (1+√5)/2 ≈ 1.618

**Pitfalls**: O(n²) ≠ Θ(n²); saying "insertion sort running time is Θ(n²)" is wrong (best case Θ(n)); asymptotic notation in inductive hypothesis without explicit constants leads to false proofs.

**End-of-Chapter**: Exercises 3.1-1 through 3.3-9; Problems 3-1 through 3-7.

---

### Ch. 4 — Divide-and-Conquer

**Recurrence Solving Methods**

**1. Substitution Method**: Guess solution, prove by induction. Key: use explicit constants, subtract lower-order term if proof fails.

**2. Recursion-Tree Method**: Draw tree with costs at nodes, sum per level, sum across levels. Best for generating guesses.

**3. Master Method**: For T(n) = aT(n/b) + f(n), a > 0, b > 1:
| Case | Condition | Solution |
|------|-----------|----------|
| 1 | f(n) = O(n^{log_b a - ε}) | T(n) = Θ(n^{log_b a}) |
| 2 | f(n) = Θ(n^{log_b a} lg^k n) | T(n) = Θ(n^{log_b a} lg^{k+1} n) |
| 3 | f(n) = Ω(n^{log_b a + ε}) AND af(n/b) ≤ cf(n) for c < 1 | T(n) = Θ(f(n)) |

Watershed function: n^{log_b a}. Case 1: leaves dominate. Case 2: tied. Case 3: root dominates.

**Examples**:
- T(n) = 9T(n/3) + n → Case 1 → Θ(n²)
- T(n) = T(2n/3) + 1 → Case 2 → Θ(lg n)
- T(n) = 3T(n/4) + n lg n → Case 3 → Θ(n lg n)
- T(n) = 2T(n/2) + n lg n → Case 2, k=1 → Θ(n lg² n)
- T(n) = 7T(n/2) + Θ(n²) → Case 1 → Θ(n^{lg 7}) = O(n^{2.81})

**Gaps**: Between cases 1-2 (f(n) = Θ(n^{log_b a} / lg n)) and cases 2-3 (f(n) = Θ(n^{log_b a} · lg n) but no polynomial separation).

**4. Akra-Bazzi Method**: For T(n) = Σ a_i T(n/b_i) + f(n). Step 1: find p with Σ a_i b_i^{-p} = 1. Step 2: T(n) = Θ(n^p + n^p ∫₁ⁿ f(x)/x^{p+1} dx).

**Strassen's Algorithm**: Multiply n×n matrices in O(n^{lg 7}) ≈ O(n^{2.81}).
- **Key idea**: 7 recursive multiplications instead of 8, using 10 sum/difference matrices.
- Steps: Create S₁…S₁₀, compute P₁…P₇ recursively, combine into C₁₁…C₂₂.
- Recurrence: T(n) = 7T(n/2) + Θ(n²) → Θ(n^{lg 7}).

**MATRIX-MULTIPLY-RECURSIVE**: 8 recursive calls → T(n) = 8T(n/2) + Θ(1) → Θ(n³) — no faster than basic.

**Polynomial-Growth Condition**: f satisfies if f(Θ(n)) = Θ(f(n)). Required for Akra-Bazzi. Exponential 2ⁿ does NOT satisfy.

**Edge Cases**: Floors/ceilings can usually be ignored. Base cases T(n) = Θ(1) for n < n₀. Master theorem regularity condition must be checked for Case 3.
- **Master Theorem pitfalls**: T(n) = 2T(n/2) + n lg n falls between Case 2 (k=0: Θ(n lg n)) and Case 3 (n lg n ≠ Ω(n^{1+ε})). Correct answer: Θ(n lg² n) via Case 2 with k=1.
- **Akra-Bazzi examples**: T(n) = T(n/2) + T(n/4) + n. Find p: (1/2)^p + (1/4)^p = 1 → p = 1. Then T(n) = Θ(n + n ∫₁ⁿ (x/x²) dx) = Θ(n).
- **Polynomial vs exponential recurrence**: T(n) = 2T(n-1) + O(2ⁿ) → T(n) = Θ(n·2ⁿ). Decay transform: set T(n) = 2ⁿ·S(n).

**Maximum-Subarray Problem** (Section 4.1):
- **Problem**: Find contiguous subarray with largest sum in A[1:n].
- **Brute force**: Θ(n²). **Crossing midpoint**: Θ(n). **Divide-and-conquer**: T(n) = 2T(n/2) + Θ(n) = Θ(n lg n).
- **Kadane's algorithm** (linear): 
  ```
  max_ending_here = max_so_far = A[1]
  for i = 2 to n
      max_ending_here = max(A[i], max_ending_here + A[i])
      max_so_far = max(max_so_far, max_ending_here)
  return max_so_far
  ```
  Θ(n) — optimal for this problem.

**End-of-Chapter**: Exercises 4.1-1 through 4.7-6; Problems 4-1 through 4-7.

---

### Ch. 5 — Probabilistic Analysis and Randomized Algorithms

**Key Concepts**
- **Probabilistic analysis**: Average over input distribution.
- **Randomized algorithm**: Behavior determined by both input and random-number generator.
- **Indicator random variable**: I{A} = 1 if event A occurs, 0 otherwise. E[I{A}] = Pr{A}.
- **Linearity of expectation**: E[Σ X_i] = Σ E[X_i] (no independence required).
- **Uniform random permutation**: Each of n! permutations equally likely.

**HIRE-ASSISTANT(n)**: Interview n candidates, hire when better than current best.
- Expected number of hires: Σ 1/i = ln n + O(1). Expected cost: O(c_h · ln n).
- **RANDOMIZED-HIRE-ASSISTANT**: Randomly permute first → guaranteed O(c_h · ln n) for any input.

**RANDOMLY-PERMUTE(A, n)**: For i = 1 to n, swap A[i] with A[RANDOM(i, n)]. Θ(n). Produces uniform random permutation (Lemma 5.4).

**Birthday Paradox**: With 23 people, Pr[shared birthday] ≥ 1/2. Expected matching pairs: C(k,2)·(1/n). Threshold for expectation ≥ 1: k ≥ (1+√(1+8n))/2.

**Balls and Bins**: Expected balls in bin: n/b. Expected tosses to fill all b bins: b·H_b ≈ b ln b.

**Streaks**: Expected longest streak in n coin flips: Θ(lg n). Pr{streak ≥ 2⌈lg n⌉} ≤ 1/n.

**Online Hiring (Secretary Problem)**: Interview first k, reject all; then hire first better. Optimal k = n/e, success probability ≥ 1/e.

**Edge Cases**: Worst-case hiring: strictly increasing quality → hire every candidate. Proving each element equally likely in each position (1/n) is NOT sufficient for uniform permutation.

**Key Results**: 23 people → 50% birthday match; b·ln b tosses to fill bins; longest streak in 1000 flips ≥ 20 has probability ≤ 1/1000; optimal hiring 37% rejection → 37% success.

**Probability Bounds for Algorithm Analysis**:
- **Boole's inequality** (union bound): Pr[∪ A_i] ≤ Σ Pr[A_i].
- **Markov's inequality**: Pr[X ≥ t] ≤ E[X]/t for nonnegative r.v. X.
- **Chernoff bound**: For X = Σ Bernoulli(p_i) with μ = E[X]: Pr[X ≤ (1-δ)μ] ≤ e^{-μδ²/2} for δ ∈ [0,1]; Pr[X ≥ (1+δ)μ] ≤ e^{-μδ²/3} for δ ∈ [0,1].
- **Conditional expectation**: E[Y] = E[E[Y|X]]. Law of total probability.
- **Variance**: Var[X] = E[X²] - (E[X])². Var[Σ X_i] = Σ Var[X_i] for independent X_i.

---

### Ch. 6 — Heapsort

**Binary Heap**: Array viewed as nearly complete binary tree. A[1] = root. PARENT(i) = ⌊i/2⌋, LEFT(i) = 2i, RIGHT(i) = 2i+1.

**Max-heap property**: A[PARENT(i)] ≥ A[i]. Min-heap property: A[PARENT(i)] ≤ A[i].

**Height**: Θ(lg n) for n-element heap. Leaves: indices ⌊n/2⌋+1 … n.

**MAX-HEAPIFY(A, i)**
```
l = LEFT(i) = 2i
r = RIGHT(i) = 2i+1
if l ≤ A.heap-size and A[l] > A[i]   largest = l
else largest = i
if r ≤ A.heap-size and A[r] > A[largest]   largest = r
if largest ≠ i
    swap A[i] with A[largest]
    MAX-HEAPIFY(A, largest)
```
- Complexity: O(lg n). Worst-case 2n/3 occurs at root of a tree where bottom half-full.
- Recurrence T(n) ≤ T(2n/3) + O(1) → O(lg n) by Master Theorem Case 2.
- Loop invariant version: at start of each iteration, A[i] may be smaller than children; after swap, property holds for subtree rooted at largest.

**BUILD-MAX-HEAP(A, n)**
```
A.heap-size = n
for i = ⌊n/2⌋ down to 1
    MAX-HEAPIFY(A, i)
```
- Complexity: O(n). Proof: Σ_{h=0}^{⌊lg n⌋} ⌈n/2^{h+1}⌉·O(h) = O(n·Σ h/2^h) = O(n).
- Key insight: MAX-HEAPIFY on node of height h takes O(h), and there are ≤ ⌈n/2^{h+1}⌉ such nodes.

**HEAPSORT(A, n)**
```
BUILD-MAX-HEAP(A, n)
for i = n down to 2
    swap A[1] with A[i]
    A.heap-size = A.heap-size - 1
    MAX-HEAPIFY(A, 1)
```
- Complexity: O(n lg n) — BUILD-MAX-HEAP O(n) + (n-1)·MAX-HEAPIFY calls each O(lg n).
- Loop invariant: A[1:i] is max-heap containing i smallest elements; A[i+1:n] contains n-i largest in sorted order.
- Not stable. In-place.

**Priority Queues**:
- **HEAP-MAXIMUM(A)**: return A[1]. Θ(1).
- **HEAP-EXTRACT-MAX(A)**: max = A[1]; A[1] = A[A.heap-size]; heap-size--; MAX-HEAPIFY(A,1). O(lg n).
- **HEAP-INCREASE-KEY(A, i, key)**: A[i] = key; while i>1 and A[PARENT(i)] < A[i], swap up. O(lg n).
- **MAX-HEAP-INSERT(A, key)**: heap-size++; A[heap-size] = -∞; HEAP-INCREASE-KEY(A, heap-size, key). O(lg n).
- Min-priority queue: symmetric operations (HEAP-MINIMUM, HEAP-EXTRACT-MIN, HEAP-DECREASE-KEY, MIN-HEAP-INSERT).

**d-ary heap**: Each node has d children. Height Θ(log_d n). PARENT(i) = ⌈(i-1)/d⌉. CHILD(i,j) = d(i-1)+j+1. EXTRACT-MAX: Θ(d log_d n). INCREASE-KEY: Θ(log_d n). Good for dense graphs (Prim's algorithm).

**Comparisons**:
| Dimension | Heapsort | Merge sort | Quicksort |
|-----------|----------|------------|-----------|
| Worst-case | O(n lg n) | O(n lg n) | Θ(n²) |
| In-place | Yes | No | Yes |
| Stable | No | Yes | No |
| Practical | Moderate | Slower | Fastest |

---

### Ch. 7 — Quicksort

**Divide-and-conquer**: Partition around pivot, recursively sort both sides. Partition does all the work.

**PARTITION (Lomuto)**
```
x = A[r]   // pivot
i = p - 1
for j = p to r-1
    if A[j] ≤ x
        i = i + 1
        swap A[i] with A[j]
swap A[i+1] with A[r]
return i+1
```
- Loop invariant: A[p:i] ≤ x, A[i+1:j-1] > x, A[r] = x.
- Θ(n) time, where n = r-p+1.
- **Pitfall**: Returns r when all elements are ≤ pivot → worst-case behavior.

**QUICKSORT(A, p, r)**
```
if p < r
    q = PARTITION(A, p, r)
    QUICKSORT(A, p, q-1)
    QUICKSORT(A, q+1, r)
```
- Worst-case: Already sorted → Θ(n²). Recurrence T(n) = T(n-1) + Θ(n) = Θ(n²).
- Best-case: Perfectly balanced → T(n) = 2T(n/2) + Θ(n) = Θ(n lg n).
- **Any constant split** (e.g., 99:1): T(n) = T(αn) + T((1-α)n) + Θ(n) = O(n lg n). Depth ≤ log_{1/(1-α)} n.
- Average-case expected Θ(n lg n) for random input (equal element probability = 1/n per position).

**RANDOMIZED-PARTITION**: Swap A[r] with A[RANDOM(p,r)] before partitioning.
```
int pivot = RANDOM(p, r)
swap A[r] with A[pivot]
return PARTITION(A, p, r)
```

**RANDOMIZED-QUICKSORT**: As QUICKSORT but using RANDOMIZED-PARTITION. Expected Θ(n lg n).

**Expected analysis**:
- Let z₁ < z₂ < ... < zₙ be sorted elements. Define indicator X_ij = 1 if z_i,z_j compared.
- Pr[z_i compares z_j] = 2/(j-i+1) — only if first pivot chosen from Z_ij = {z_i,...,z_j}.
- E[X] = Σ_{i=1}^{n-1} Σ_{j=i+1}^{n} 2/(j-i+1) = O(n lg n).
- Lemma 7.1: Partition takes O(n) time → total expected time = O(n lg n).

**HOARE-PARTITION**
```
x = A[p]   // pivot
i = p - 1
j = r + 1
while true
    repeat j = j - 1 until A[j] ≤ x
    repeat i = i + 1 until A[i] ≥ x
    if i < j
        swap A[i] with A[j]
    else
        return j
```
- Returns j where p ≤ j < r. Both A[p:j] ≤ x and A[j+1:r] ≥ x.
- More efficient for equal elements (returns near middle). Fewer swaps than Lomuto.

**Tail-recursion elimination**: Replace second recursive call with iteration. Recursively sort smaller partition, iteratively process larger. Stack depth ≤ lg n.
```
QUICKSORT'(A, p, r)
    while p < r
        q = PARTITION(A, p, r)
        if q-p < r-q   // left smaller
            QUICKSORT'(A, p, q-1)
            p = q+1
        else
            QUICKSORT'(A, q+1, r)
            r = q-1
```

**Edge Cases**: All equal elements → Lomuto returns q = r → Θ(n²). Hoare partition handles better (returns near middle). RANDOMIZED-PARTITION reduces but doesn't eliminate worst case.

---

### Ch. 8 — Sorting in Linear Time

**Comparison Sort Lower Bound** (Theorem 8.1): Any comparison sort requires Ω(n lg n) comparisons in worst case.
- **Proof**: Decision tree model. Each leaf = possible permutation. n! permutations → at least n! leaves. Height h → ≤ 2^h leaves. So n! ≤ 2^h → h ≥ lg(n!) = Ω(n lg n) by Stirling.
- **Corollary 8.2**: Heapsort and merge sort are asymptotically optimal comparison sorts (achieve Θ(n lg n) worst-case).

**COUNTING-SORT(A, n, k)**
```
let C[0:k] be new array of zeros
for i = 1 to n          // count frequencies
    C[A[i]] = C[A[i]] + 1
for i = 1 to k          // running sums → positions
    C[i] = C[i] + C[i-1]
let B[1:n] be new array
for i = n down to 1     // stable placement
    B[C[A[i]]] = A[i]
    C[A[i]] = C[A[i]] - 1
return B
```
- Input: Integers in [0,k]. Output: B[1:n] sorted.
- Complexity: Θ(n+k). When k = O(n), runs in Θ(n).
- Stable because we process input in reverse order.
- Not a comparison sort — uses array indices, wins when k = O(n).

**RADIX-SORT(A, n, d)**
```
for i = 1 to d           // least significant digit first
    use stable sort (e.g., counting sort) to sort A on digit i
```
- Input: d-digit numbers, each digit range [0,k-1].
- Complexity: Θ(d(n+k)). If k = O(n), then Θ(dn).
- **Optimal digit size**: r bits per digit. d = ⌈b/r⌉ digits total. Radix: Θ((b/r)(n+2ʳ)). Minimize: set r = ⌊lg n⌋ → Θ(bn/lg n).
- With n integers in [0,2ᵇ-1] and r = ⌈lg n⌉, total Θ(bn/lg n). For b = O(lg n), Θ(n).
- **LSD-first vs MSD-first**: LSD requires stable sort; MSD can be used for lexicographic order.

**BUCKET-SORT(A, n)**
```
let B[0:n-1] be new array of empty lists
for i = 1 to n
    insert A[i] into B[⌊n·A[i]⌋]
for i = 0 to n-1
    sort list B[i] with insertion sort
concatenate B[0], B[1], …, B[n-1]
```
- Assumes input uniform over [0,1).
- Expected Θ(n), worst-case Θ(n²) (all elements in one bucket).
- E[sum of squared bucket sizes] = 2 - 1/n → O(n) total sort time.

| Algorithm | Assumption | Time | Stable |
|-----------|-----------|------|--------|
| Counting | Integers [0,k] | Θ(n+k) | Yes |
| Radix | d-digit numbers | Θ(d(n+k)) | Depends on inner sort |
| Bucket | Uniform [0,1) | Θ(n) expected | Depends on inner sort |

**0-1 Sorting Lemma**: If oblivious compare-exchange algorithm sorts all 0-1 inputs, it sorts all inputs. Proof by contradiction: a misordered pair of distinct values maps to a 0-1 violation.

**Stability**: Insertion sort ✓, Merge sort ✓, Heapsort ✗, Quicksort (Lomuto) ✗, Counting sort ✓, Radix sort (with stable digit sort) ✓.

---

### Ch. 9 — Medians and Order Statistics

**Selection problem**: Find i-th smallest element from A[1:n]. Can be solved in O(n) expected and O(n) worst-case time.

**MINIMUM(A, n)**
```
min = A[1]
for i = 2 to n
    if A[i] < min   min = A[i]
return min
```
- n-1 comparisons (optimal by tournament argument: each non-winner must lose ≥ 1 match).

**Simultaneous min and max**: Process in pairs: compare pair elements, compare larger to max, smaller to min.
- At most 3⌊n/2⌋ comparisons (vs 2n-2 naive).

**RANDOMIZED-SELECT(A, p, r, i)**
```
if p == r
    return A[p]
q = RANDOMIZED-PARTITION(A, p, r)
k = q - p + 1      // rank of pivot
if i == k
    return A[q]     // pivot is the answer
else if i < k
    return RANDOMIZED-SELECT(A, p, q-1, i)
else
    return RANDOMIZED-SELECT(A, q+1, r, i-k)
```
- Expected Θ(n), worst-case Θ(n²).
- Intuition: pivot in "middle half" (positions 25%-75%) removes ≥ n/4 elements with probability ≥ 1/2. Expected size reduction → T(n) = T(3n/4) + O(n) → Θ(n).

**SELECT (worst-case linear, Blum-Floyd-Pratt-Rivest-Tarjan)**
```
1. Divide n elements into ⌈n/5⌉ groups of 5
2. Find median of each group (sort each 5-element group, take 3rd)
3. Recursively find median x of the ⌈n/5⌉ medians
4. Partition around x (modified PARTITION)
5. if i == k return x
   else if i < k recurse on left side
   else recurse on right side with i-k
```
- **Why groups of 5?** At least ⌈⌈n/5⌉/2⌉ groups have median ≤ x (and ≥ x). Each such group contributes 3 elements ≤ x (or ≥ x). So at least 3·⌈⌈n/5⌉/2⌉ ≥ 3n/10 elements are ≤ x (and ≥ x). Worst-case recursion: n - 3n/10 = 7n/10.
- **Recurrence**: T(n) ≤ T(⌈n/5⌉) + T(7n/10) + Θ(n) → T(n) = Θ(n) (substitution proof with T(n) ≤ cn).
- **Groups of 3**: T(n) ≤ T(n/3) + T(2n/3) + Θ(n) → O(n lg n) — NOT linear.
- **Groups of 7**: Works but constant factor worse than 5.
- **Practical note**: RANDOMIZED-SELECT is faster in practice; SELECT is mostly theoretical interest.

**Comparisons**:
| Dimension | RANDOMIZED-SELECT | SELECT |
|-----------|-------------------|--------|
| Expected | Θ(n) | Θ(n) |
| Worst-case | Θ(n²) | Θ(n) |
| Practical | Yes, fast | Mostly theoretical |
| Constant factor | Small (1-2x PARTITION) | Large (grouping, sorting 5s) |

**Tournament argument**: Each non-winner must lose at least once → n-1 comparisons for minimum (optimal). Lower bound proof by adversary.

---

### Ch. 10 — Elementary Data Structures

**Stacks**: LIFO. Array S[1:n] with top pointer.
```
STACK-EMPTY(S): return S.top == 0
PUSH(S, x): S.top++; S[S.top] = x
POP(S): if STACK-EMPTY then error; else S.top--; return S[S.top+1]
```
- Overflow: PUSH when S.top == n. Underflow: POP when empty.
- All operations O(1). Used for DFS, function call stack, expression evaluation.

**Queues**: FIFO. Circular array Q[1:n] with head Q.head and tail Q.tail.
```
ENQUEUE(Q, x): Q[Q.tail] = x; if Q.tail == n then Q.tail = 1 else Q.tail++
DEQUEUE(Q): x = Q[Q.head]; if Q.head == n then Q.head = 1 else Q.head++; return x
```
- Full: Q.tail == Q.head after wrap. Empty: Q.head == Q.tail after DEQUEUE. 
- Sentinel: maintain size or sacrifice one slot to distinguish full/empty.
- All operations O(1). Used for BFS, buffering.

**Linked Lists**: Doubly or singly linked. LIST-SEARCH Θ(n), LIST-PREPEND O(1), LIST-INSERT O(1), LIST-DELETE O(1) with pointer.

**Sentinel (L.nil)**: Dummy node eliminating boundary checks. Simplifies code; asymptotic same, slightly better constants.

**Array address calculation**: 1-origin: a + b(i-1). Row-major: M[i,j] at n(i-1)+j. Column-major: i + m(j-1).

**Left-child, right-sibling representation**: For arbitrary rooted trees. Each node stores: parent, left-child, right-sibling. Space O(n).
- **Tree traversals**: Preorder (root→children), Postorder (children→root), Level-order (queue-based BFS).

**Rooted tree representations**:
- **Parent array**: p[i] = parent of i. Space O(n). Easy for finding parent, hard for children.
- **Adjacency list**: For general trees and graphs. Common in graph algorithms.
- **Left-child right-sibling**: Binary representation of arbitrary tree. Used for space efficiency.

**Comparisons**:
| Dimension | Array | Linked List | Stack | Queue | Deque |
|-----------|-------|-------------|-------|-------|-------|
| Access | O(1) | O(k) | O(1) top | O(1) front | O(1) ends |
| Insert front | Θ(n) | O(1) | — | — | O(1) |
| Insert back | O(1)* | O(1)† | O(1) | O(1) | O(1) |
| Delete front | Θ(n) | O(1) | — | O(1) | O(1) |
| Delete back | O(1)* | O(n)† | O(1) | — | O(1) |

*With dynamic table (amortized). †With tail pointer. Singly linked: back operations O(n).

**Multi-array representation**: Stack of arrays representation for dynamic arrays (implemented via doubling/realloc). Amortized O(1) per insertion.

---

### Ch. 11 — Hash Tables

**Direct-address table**: T[k] points to element with key k. O(1) operations. Requires universe U to be small. INSERT(DIRECT-ADDRESS-INSERT), SEARCH, DELETE all Θ(1).

**Hash table**: h(k) maps key to slot. Collisions resolved by chaining or open addressing.
- **TABULATE-HASH**: Create random table of the form {0,1}^ℓ. Compute h(k) = Σ_{i=1}^{c} T_i[k_i] mod 2^ℓ. 

**CHAINED-HASH-INSERT(T, x)**: insert at head of T[h(x.key)], O(1).
**CHAINED-HASH-SEARCH(T, k)**: search list T[h(k)] linearly, Θ(1+α) expected.
**CHAINED-HASH-DELETE(T, x)**: doubly linked list delete, O(1).

**Load factor**: α = n/m. Chaining avg search: Θ(1+α).

**Chaining**: Each slot points to linked list. INSERT O(1), SEARCH Θ(1+α) avg, DELETE O(1) with doubly linked.

**Hash function methods**:
- **Division method**: h(k) = k mod m. Avoid m = 2^p (poor distribution based on lower bits). Good choice: m ≈ prime not near 2^p.
- **Multiplication method**: h(k) = ⌊m(kA mod 1)⌋. A ≈ (√5-1)/2 ≈ 0.618 (Knuth's suggestion). Works for any m.
- **Multiply-shift**: h_a(k) = (k·a mod 2^w) ⋙ (w-ℓ), where a odd, w = word size, ℓ = ⌊lg m⌋. Fast in hardware.

**Universal hashing**: Family H such that Pr[h(k₁)=h(k₂)] ≤ 1/m for distinct k₁,k₂.
- **H_pm family**: H = {h_{ab}(k) = ((ak+b) mod p) mod m}, p prime > |U|, a∈[1,p-1], b∈[0,p-1]. Universal (Theorem 11.4). Proof: for k₁≠k₂, the pair (ak₁+b, ak₂+b) uniformly maps to distinct pairs mod p.
- **Multiply-shift**: 2/m-universal (Theorem 11.5). Pr[h_a(k₁)=h_a(k₂)] ≤ 2/m for distinct k₁,k₂.
- **Tabulation hashing**: View key as c characters, each character indexes a random table T_i[·], XOR results. 3-wise independent. Very fast in practice.

**Perfect hashing** (Section 11.5): When keys are static (no inserts/deletes).
- Two-level scheme: outer hash table maps to inner perfect hash table. 
- First level: universal hash with m = n, expected collisions O(n).
- Second level: for each bucket of size nⱼ, use mⱼ = nⱼ² to guarantee no collisions (expected total space O(n)).
- **Theorem 11.9**: Expected total space O(n) for static dictionary with O(1) worst-case search.

**Choosing hash functions in practice**:
- **Simple random**: Not repeatable. Use seeded hash (siphash, cityhash, xxhash).
- **Cryptographic**: Overkill for hash tables (SHA, MD5).
- **Key types**: Integer (multiply-shift), String (polynomial rolling hash), Compound (combine fields).

**Open addressing**: All elements in table. Probe sequences.
- **Linear probing**: h(k,i) = (h₁(k)+i) mod m. Primary clustering. O(1) with 5-independent hash and α ≤ 2/3.
- **Double hashing**: h(k,i) = (h₁(k)+i·h₂(k)) mod m. Θ(m²) probe sequences.
- Expected probes: unsuccessful ≤ 1/(1-α), successful ≤ (1/α) ln(1/(1-α)).

**Deletion in open addressing**: Hard — need DELETED marker or special procedure.

| Dimension | Chaining | Open Addressing |
|-----------|----------|-----------------|
| α can be > 1 | Yes | No (α < 1) |
| Deletion | Easy | Hard |
| Cache | Poor | Better |

---

### Ch. 12 — Binary Search Trees

**BST property**: For any node x, left subtree keys ≤ x.key ≤ right subtree keys.

**Inorder tree walk**: LEFT(x), print x.key, RIGHT(x) → prints keys sorted in Θ(n).

**Query operations** (all O(h) where h = height):
```
TREE-SEARCH(x, k): if x==NIL or k==x.key return x; if k<x.key return TREE-SEARCH(x.left, k) else TREE-SEARCH(x.right, k)
ITERATIVE-TREE-SEARCH(x, k): while x≠NIL and k≠x.key: if k<x.key then x=x.left else x=x.right; return x
TREE-MINIMUM(x): while x.left ≠ NIL: x = x.left; return x
TREE-MAXIMUM(x): while x.right ≠ NIL: x = x.right; return x
TREE-SUCCESSOR(x): if x.right ≠ NIL return TREE-MINIMUM(x.right); y=x.parent; while y≠NIL and x==y.right: x=y; y=y.parent; return y
TREE-PREDECESSOR(x): symmetric to successor
```

**TREE-INSERT(T, z)**
```
y = NIL
x = T.root
while x ≠ NIL
    y = x
    if z.key < x.key   x = x.left
    else               x = x.right
z.parent = y
if y == NIL
    T.root = z
else if z.key < y.key   y.left = z
else                    y.right = z
```
- O(h). Inserted node always becomes a leaf (before fixup for RB trees).

**TREE-DELETE(T, z)**
- **Transplant(u,v)**: Replace subtree rooted at u with subtree rooted at v.
- **Cases**:
  1. z has no left child → TRANSPLANT(z, z.right)
  2. z has no right child → TRANSPLANT(z, z.left)  
  3. z has both children, successor y is right child → TRANSPLANT(z, y); y.left = z.left
  4. z has both children, successor y NOT right child → TRANSPLANT(y, y.right); y.right = z.right; TRANSPLANT(z, y); y.left = z.left
- O(h). Cases 3-4: successor is always the node with smallest key > z.key.

**Randomly built BST**: Expected height O(lg n). Expected depth of node: O(lg n). 
- **Theorem 12.4**: Expected height of randomly built BST = O(lg n). Proof via indicator variables and Jensen's inequality.

**Catalan number**: Number of distinct BSTs with n nodes = (1/(n+1))·C(2n,n).

**Comparisons**: Balanced BST (O(lg n) per op) vs sorted array (O(lg n) search, Θ(n) insert/delete) vs linked list (Θ(n) search, O(1) insert/delete).

---

### Ch. 13 — Red-Black Trees

**Red-black properties**:
1. Every node red or black
2. Root is black
3. Every leaf (T.nil) is black
4. Red node → both children black (no consecutive reds)
5. For each node, all paths to descendant leaves have same number of black nodes

**Black-height bh(x)**: Number of black nodes on path from x (excluding x) to leaf.

**Lemma 13.1 (Height bound)**: RB tree with n internal nodes has height h ≤ 2 lg(n+1). 
- **Proof**: Inductive claim: subtree at x has ≥ 2^{bh(x)} - 1 internal nodes. Base: bh(x)=0 → 0 nodes. Inductive: if children have bh(x) or bh(x)-1, node count = 2·(2^{bh(x)-1}-1)+1 = 2^{bh(x)}-1. By property 4 (no consecutive reds), bh(root) ≥ h/2. So n ≥ 2^{h/2} - 1 → h ≤ 2 lg(n+1).
- **Corollary**: SEARCH, MIN, MAX, SUCCESSOR, PREDECESSOR all O(lg n).

**Rotations**: LEFT-ROTATE(T, x), RIGHT-ROTATE(T, y). O(1). Preserve BST property and inorder ordering.
```
LEFT-ROTATE(T, x)
    y = x.right                    // set y
    x.right = y.left               // turn y's left subtree into x's right subtree
    if y.left ≠ T.nil   y.left.parent = x
    y.parent = x.parent            // link x's parent to y
    if x.parent == T.nil   T.root = y
    else if x == x.parent.left   x.parent.left = y
    else   x.parent.right = y
    y.left = x                     // put x on y's left
    x.parent = y
```

**RB-INSERT(T, z)**: BST insert + color RED + RB-INSERT-FIXUP(T, z). O(lg n). At most 2 rotations.
- **RB-INSERT-FIXUP cases** (assuming z.parent is left child — symmetric for right):
  1. **z.uncle RED**: recolor parent, uncle, grandparent; move z up two levels
  2. **z.uncle BLACK, z is right child**: left-rotate parent → becomes case 3
  3. **z.uncle BLACK, z is left child**: right-rotate grandparent, recolor parent BLACK, grandparent RED
- Loop invariant: z is RED; only violation is property 2 (root black) or property 4 (red-black-red).
- Termination: if z is root → color BLACK (fix property 2); if uncle is RED → recolor; otherwise rotation + termination.

**RB-DELETE(T, z)**: More complex. Tracks y (node spliced out or moved) and x (node replacing y). 
- If y was BLACK → RB-DELETE-FIXUP(T, x). O(lg n). At most 3 rotations.
- **RB-DELETE-FIXUP cases** (assuming x is left child):
  1. **w (sibling) RED**: recolor w BLACK, x.parent RED, LEFT-ROTATE(x.parent), new w = x.parent.right
  2. **w BLACK, both w's children BLACK**: set w RED, move x up to x.parent
  3. **w BLACK, w.left RED, w.right BLACK**: recolor w.left BLACK, w RED, RIGHT-ROTATE(w), new w = x.parent.right
  4. **w BLACK, w.right RED**: recolor w = x.parent.color, x.parent BLACK, w.right BLACK, LEFT-ROTATE(x.parent), set x = root
- Loop invariant: x is "doubly black" or RED-AND-BLACK; fixup pushes blackness up or removes it.
- **Difference from insert**: Delete fixup can propagate up to root; insert fixup terminates after O(1) rotations.

**Comparisons**: RB tree (h ≤ 2 lg(n+1), ≤ 2-3 rotations) vs AVL (h ≤ 1.44 lg n, O(lg n) rotations) vs BST (Θ(n) worst-case height).

**Persistent trees**: Without parent pointers, insertion copies O(h) nodes.

---

### Ch. 14 — Dynamic Programming

**Key properties**: Optimal substructure + overlapping subproblems.

**Four-step method**: (1) Characterize optimal structure; (2) Recursively define optimal value; (3) Compute value (bottom-up or top-down); (4) Construct optimal solution.

**Rod Cutting**: r_n = max_{1≤i≤n}(p_i + r_{n-i}), r_0 = 0. Naive recursive: 2^n. DP (top-down memoized or bottom-up): Θ(n²).
- **Bottom-up**: for j=1..n: r_j = max(p_i + r_{j-i}) for 1≤i≤j. O(n²).
- **Reconstruction**: s[j] = optimal first cut length for rod of length j.

**Matrix-Chain Multiplication**: m[i,j] = min_{i≤k<j}{m[i,k] + m[k+1,j] + p_{i-1}p_kp_j}. Θ(n³) time, Θ(n²) space. 
- Number of parenthesizations = Catalan C_{n-1} = Ω(4^n/n^{3/2}) — factorial growth vs polynomial DP.
- **Bottom-up**: fill m[i,j] by chain length ℓ=2..n; for each [i,j] try all k in [i,j-1]. O(n³).
- **Example**: A₁(30×35), A₂(35×15), A₃(15×5), A₄(5×10), A₅(10×20), A₆(20×25). Optimal: (A₁(A₂A₃))((A₄A₅)A₆) = 15,125 scalar multiplications (vs 71,250 naive).

**LCS (Longest Common Subsequence)**: c[i,j] = 0 if i=0 or j=0; = c[i-1,j-1]+1 if x_i=y_j; = max(c[i-1,j], c[i,j-1]) if x_i≠y_j. Θ(mn). Can reconstruct in O(m+n).

**OBST (Optimal Binary Search Tree)**: e[i,j] = min_{i≤r≤j}{e[i,r-1] + e[r+1,j] + w[i,j]}. Θ(n³) naive, Θ(n²) with Knuth optimization.

**Cut-and-Paste Argument**: If subproblem solution not optimal, cut it out and paste in better one → contradiction with original optimality.
- Example: In rod cutting, if r_{n-i} is not optimal for subproblem of size n-i, then r_n wouldn't be optimal either.

**tD/eD classification**: Table size O(n^t), each entry depends on O(n^e) others.
- 1D/1D: LIS, rod cutting. 2D/1D: LCS. 3D/2D: matrix-chain (n² entries, n choices each).

**Reconstruction**: Store choices to recover solution (parent pointers, split points, etc.):
- Rod cutting: s[j] = optimal cut. Matrix-chain: s[i,j] = optimal split k. LCS: b[i,j] = direction (↑, ←, ↖).

**Common DP Patterns**:
| Pattern | Recurrence | Example |
|---------|-----------|---------|
| Linear 1D | dp[i] = f(dp[j]) for j < i | LIS, rod cutting |
| Interval | dp[i,j] = f(dp[i,k], dp[k+1,j]) | Matrix-chain, OBST |
| Edit distance | dp[i,j] = f(dp[i-1,j], dp[i,j-1], dp[i-1,j-1]) | LCS, string edit |
| Knapsack | dp[i,w] = max(dp[i-1,w], dp[i-1,w-w_i]+v_i) | 0-1 Knapsack |
| Tree DP | dp[u] = f(dp[children[u]]) | Largest independent set |
| Knuth optimization | dp[i,j] = min_{k in [p_i, p_{i+1}]} ... | OBST → O(n²) |

**Comparisons**: DP vs Greedy (DP explores all subproblems, greedy commits locally; DP for 0-1 knapsack, greedy for fractional), DP vs D&C (DP subproblems overlap, D&C subproblems disjoint).

**DP on Trees**: For rooted tree, compute from leaves up. Example: Largest independent set in tree. dp[u,0] = Σ max(dp[v,0], dp[v,1]) (u excluded); dp[u,1] = 1 + Σ dp[v,0] (u included). O(n).

---

### Ch. 15 — Greedy Algorithms

**Greedy-choice property**: Locally optimal choice leads to global optimum.

**Optimal substructure**: Solution contains optimal solutions to subproblems.

**Activity Selection**: Choose activity with earliest finish time. Greedy: Θ(n) (after sorting by finish time). Exchange argument proves optimality (Theorem 15.1).

**Huffman Codes**: Merge two lowest-frequency characters. O(n lg n) with min-heap. Produces optimal prefix-free code (Theorem 15.4).
- Lemma 15.2: lowest-frequency chars can be deepest siblings in some optimal code.
- Lemma 15.3: optimal substructure via merging.
- Full binary tree required for optimality.
- Compression example: 224K bits vs 300K fixed-length (25% savings).

**Offline Caching (Furthest-in-Future)**: Evict block whose next access is furthest. Optimal (Theorem 15.5). Exchange argument.

**Fractional Knapsack**: Sort by v_i/w_i (value/weight). Take items in order until knapsack full. Θ(n lg n). Greedy works because you can take fractions.
- **0-1 Knapsack**: Requires DP. Recurrence: dp[i,w] = max(dp[i-1,w], dp[i-1,w-w_i] + v_i). O(nW) — pseudopolynomial. No greedy (counterexample: W=50, item1: v=60,w=10 → ratio 6, item2: v=100,w=20 → ratio 5, item3: v=120,w=30 → ratio 4; greedy picks item1+item2=160, but item2+item3=220 better).

**Making Change (canonical coin systems)**: Greedy (largest coin first) optimal for US coins (1,5,10,25) but not all systems (e.g., 1,3,4: greedy for 6 gives 4+1+1=3 coins, optimal is 3+3=2 coins).

**Scheduling (Minimizing lateness)**: Schedule jobs by deadline (earliest deadline first). O(n lg n). Exchange argument: any optimal schedule can be transformed to EDF without increasing max lateness.

**Coin changing DP**: C[i] = min_{c_j ≤ i} C[i-c_j] + 1. Θ(n·k) for n amount and k coin types.

**Proof patterns**: 
- **Exchange argument** ("greedy stays ahead"): Take any optimal solution, transform step by step to include greedy choice without degrading quality. Example: activity selection — order activities by finish time, show that if OPT starts with different first activity, we can swap it for greedy's first choice.
- **Matroid theory**: Many greedy algorithms (including MST, scheduling) are special cases of matroid optimization. A matroid M = (S, I) satisfies: (1) ∅ ∈ I; (2) A⊆B∈I → A∈I; (3) A,B∈I, |A|<|B| → ∃x∈B\A with A∪{x}∈I. Greedy on matroid weighted matroid finds maximum-weight independent set.

**Edge Cases**: Greedy fails when greedy-choice property absent (0-1 knapsack, making change, longest simple path).

---

### Ch. 16 — Amortized Analysis

**Three methods**:
1. **Aggregate**: Total cost T(n) for n ops → amortized = T(n)/n.
2. **Accounting**: Overcharge cheap ops, store credit; credit pays for expensive ops later. Credit must stay nonnegative.
3. **Potential**: Φ(D_i) maps data structure to real. Amortized ĉ_i = c_i + Φ(D_i) - Φ(D_{i-1}). Require Φ(D_i) ≥ Φ(D_0) for all i.

**Stack with MULTIPOP**:
- **Aggregate**: Each element pushed once, popped at most once. n PUSH + n POP (including MULTIPOP) ≤ 2n ops. Amortized: O(1).
- **Accounting**: PUSH costs $2 ($1 for push, $1 stored). POP/MULTIPOP use stored credit. Credit never negative.

**Binary counter**:
- **Aggregate**: Bit A[i] flips ⌊n/2^i⌋ times. Total flips = Σ ⌊n/2^i⌋ < 2n. Amortized O(1) per INCREMENT.
- **Potential**: Φ = number of 1-bits. Φ₀ = 0. Flip from 0→1 increases Φ by 1; 1→0 decreases by 1. ĉ_i = c_i + ΔΦ = (t_i + 1) + (1 - t_i) = 2, where t_i = trailing 1s.
- **DECREMENT breaks O(1)**: alternating 0→1 and 1→0 can make each op cost Θ(lg n).

**Dynamic table (doubling only)**:
- **Aggregate**: TABLE-INSERT cost = i when i-1 is power of 2, 1 otherwise. Total cost < 2n (sum of 1s + powers of 2 up to n). Amortized < 3 per insert = O(1).
- **Accounting**: Charge $3 per insertion ($1 for immediate insert, $1 for future resize of this element, $1 for future resize of an older element). Credit suffices.
- **Potential**: Φ(T) = 2·num - size. Φ ≥ 0, Φ₀ = 0. When α = 1 (full), Φ = size. After doubling: num' = size, size' = 2·size → Φ' = 2·size - 2·size = 0. ΔΦ = -size. Insert causing resize: c = num + 1 = size + 1 (1 for insert + size to copy). ĉ = (size+1) + (-size) = 1 = O(1).

**Dynamic table with insert + delete**:
- **Key issue**: If we halve at α = 1/2, alternating insert/delete can cause repeated resize (thrashing). Solution: halve at α = 1/4.
- **Potential**: Φ = 2·num - size if α ≥ 1/2; = size/2 - num if 1/4 ≤ α < 1/2. Φ ≥ 0 always, Φ₀ = 0. Each operation amortized O(1).

**Comparisons**: Aggregate (same amortized cost for all ops), Accounting (different costs per op type), Potential (most flexible, global view).

**Pitfalls**: Credit must never go negative; halving at α = 1/2 causes Θ(n) amortized for alternating insert/delete; DECREMENT on binary counter breaks O(1) amortized.

---

### Ch. 17 — Augmenting Data Structures

**Generic 4-step method**: (1) Choose underlying DS; (2) Determine additional info; (3) Verify maintainability; (4) Develop new operations.

**Theorem 17.1**: If x.f depends only on O(1)-computable info from x, x.left, x.right, then RB tree can maintain f in O(lg n). Constant rotations (≤2 insert, ≤3 delete) critical.

**Order-Statistic Tree**: Red-black tree + size attribute (size = x.left.size + x.right.size + 1).
```
OS-SELECT(x, i)        // i-th smallest in subtree rooted at x
    r = x.left.size + 1   // rank of x
    if i == r   return x
    else if i < r   return OS-SELECT(x.left, i)
    else   return OS-SELECT(x.right, i-r)

OS-RANK(T, x)          // rank of x in inorder traversal
    r = x.left.size + 1
    y = x
    while y ≠ T.root
        if y == y.parent.right
            r = r + y.parent.left.size + 1
        y = y.parent
    return r
```
- Both O(lg n). Size maintained during insert/delete by path traversal + fixing rotation (O(1) per rotation).

**Interval Tree**: Red-black tree keyed by low endpoint + max attribute (max endpoint in subtree).
```
INTERVAL-SEARCH(T, i)
    x = T.root
    while x ≠ T.nil and i does not overlap x.int
        if x.left ≠ T.nil and x.left.max ≥ i.low
            x = x.left
        else
            x = x.right
    return x
```
- Finds any one overlapping interval in O(lg n). Correctness (Theorem 17.2): if no overlap in current subtree, searching either direction is safe — an overlapping interval exists iff it can be found this way. 
- **Interval trichotomy**: For any two intervals i,j: i overlaps j; i is left of j (i.high < j.low); i is right of j (i.low > j.high).

**Interval trichotomy**: For any two intervals: they overlap, or one is left of the other.

**Applications**: Josephus permutation (O(n lg n)), counting inversions.

---

### Ch. 18 — B-Trees

**Properties**: Minimum degree t ≥ 2. Every node (except root) ≥ t-1 keys, ≤ 2t-1 keys. All leaves at same depth.

**Height bound** (Theorem 18.1): h ≤ log_t((n+1)/2). With t=1001, n=10⁹ → h ≤ 3.

**B-TREE-SEARCH(x, k)**: Search within node x linearly (O(t)), recurse to appropriate child. O(t·log_t n) CPU, O(log_t n) disk accesses.
```
B-TREE-SEARCH(x, k)
    i = 1
    while i ≤ x.n and k > x.key[i]   i++
    if i ≤ x.n and k == x.key[i]   return (x, i)
    if x.leaf   return NIL
    DISK-READ(x.c[i])
    return B-TREE-SEARCH(x.c[i], k)
```

**B-TREE-INSERT(T, k)**: Single pass — split full nodes on way down.
```
B-TREE-INSERT(T, k)
    r = T.root
    if r.n == 2t-1           // root is full
        s = ALLOCATE-NODE()
        T.root = s
        s.leaf = false; s.n = 0; s.c[1] = r
        B-TREE-SPLIT-CHILD(s, 1)
        B-TREE-INSERT-NONFULL(s, k)
    else
        B-TREE-INSERT-NONFULL(r, k)
```
- **B-TREE-SPLIT-CHILD(x, i)**: Split full child y (with 2t-1 keys) into y (t-1 keys) and z (t-1 keys). Median key moves to x. O(t) CPU.
- **B-TREE-INSERT-NONFULL(x, k)**: Recurse down, splitting full children along the way. Only splits at root increase height. O(h) disk accesses.

**B-TREE-DELETE(T, k)**: Single downward pass maintaining invariant: every visited node has ≥ t keys.
- **Cases**:
  1. k in leaf x: delete directly
  2. k in internal node x:
     - If child preceding k has ≥ t keys: find predecessor, swap, recurse delete
     - Else if child following k has ≥ t keys: find successor, swap, recurse delete
     - Else: merge k and children; recurse delete in merged node
  3. k not in internal node x: if child would have < t keys, borrow from sibling (rotation) or merge with sibling; then recurse
- Root may become empty after merge → height decreases by 1.

**Comparisons**: B-tree (disk-optimized, high branching factor) vs RB tree (memory, binary).

---

### Ch. 19 — Disjoint Sets

**Linked-list representation**: Weighted-union heuristic (always append shorter list to longer). O(m + n lg n) for m ops (n MAKE-SET). Each element's pointer updated ≤ ⌈lg n⌉ times.

**Disjoint-set forest**: Union by rank + path compression. O(m α(n)) where α(n) is inverse Ackermann (≤ 4 for all practical n).

**Union by rank**: Root with smaller rank points to larger. Ranks only increase; only roots have their rank incremented.

**Path compression**: FIND-SET makes every node on path point directly to root. Two-pass (recursive or iterative).

**Ackermann-like function A_k(j)**: A_0(j)=j+1, A_1(j)=2j+1, A_2(j)=2^{j+1}(j+1)-1. α(n) = min{k : A_k(1) ≥ n}. A_3(1)=2047, A_4(1) > 10^80.

**Amortized analysis**: Complex potential function with level(x) and iter(x). At most α(n)+2 nodes per find path without potential drop → O(α(n)) per FIND-SET.

**Applications**: Connected components (dynamic), offline minimum, Tarjan's offline LCA.

| Implementation | m ops, n MAKE-SET |
|--------------|-------------------|
| Linked-list simple | Θ(n²) worst |
| Linked-list weighted | O(m + n lg n) |
| Forest (union by rank) | O(m lg n) |
| Forest (both heuristics) | O(m α(n)) |

---

### Ch. 20 — Elementary Graph Algorithms

**Graph representations**: Adjacency list Θ(V+E) memory, Θ(degree(u)) edge lookup. Adjacency matrix Θ(V²), O(1) edge lookup.

**BFS (Breadth-First Search)**
```
for each u ∈ G.V - {s}: u.color = WHITE, u.d = ∞, u.π = NIL
s.color = GRAY, s.d = 0, s.π = NIL
Q = ∅; ENQUEUE(Q, s)
while Q ≠ ∅
    u = DEQUEUE(Q)
    for each v ∈ G.Adj[u]
        if v.color == WHITE
            v.color = GRAY; v.d = u.d + 1; v.π = u; ENQUEUE(Q, v)
    u.color = BLACK
```
- Queue-based. Computes shortest-path distances (unweighted) and BFS tree.
- O(V+E). Correctness (Theorem 20.5): v.d = δ(s,v) for all v reachable from s.
- **BFS tree**: predecessor subgraph G_π = (V_π, E_π) where V_π = {v: v.π ≠ NIL} ∪ {s}.

**DFS (Depth-First Search)**
```
DFS(G)
    for each u ∈ G.V: u.color = WHITE, u.π = NIL
    time = 0
    for each u ∈ G.V
        if u.color == WHITE   DFS-VISIT(G, u)

DFS-VISIT(G, u)
    time++; u.d = time; u.color = GRAY
    for each v ∈ G.Adj[u]
        if v.color == WHITE
            v.π = u; DFS-VISIT(G, v)
    u.color = BLACK; time++; u.f = time
```
- Discovery time u.d, finish time u.f. O(V+E).
- **Edge classification**: tree edge (u→v, v WHITE); back edge (u→v, v GRAY); forward edge (u→v, v BLACK, u.d < v.d); cross edge (u→v, v BLACK, u.d > v.d).
- **Undirected graphs**: only tree edges and back edges (no forward/cross).

**Parenthesis Theorem** (Theorem 20.6): For any u,v, intervals [u.d, u.f] and [v.d, v.f] are either disjoint or one contains the other (nested). u is ancestor of v ⇔ [v.d,v.f] ⊆ [u.d,u.f].

**White-Path Theorem** (Theorem 20.7): v is descendant of u in DFS forest ⇔ at time u.d, there is a white path from u to v.

**Topological Sort**
```
TOPOLOGICAL-SORT(G)
    call DFS(G) to compute finish times v.f for all v
    as each vertex is finished, prepend to linked list
    return linked list
```
- DFS + decreasing finish times → linear ordering of DAG. Θ(V+E).
- **Correctness** (Lemma 20.10): In DAG, for any edge (u,v), u.f > v.f (no back edges in DAG).
- **Kahn's algorithm**: Remove vertices with in-degree 0 iteratively. Alternative to DFS-based. O(V+E).

**Strongly Connected Components (Kosaraju)**
```
STRONGLY-CONNECTED-COMPONENTS(G)
    call DFS(G) to compute finish times
    compute G^T (transpose: reverse all edges)
    call DFS(G^T), processing vertices in decreasing order of G's finish times
    each DFS tree in G^T forest = one SCC
```
- Θ(V+E). Component graph (each SCC → one vertex) is a DAG.
- **Correctness**: G and G^T have same SCCs. Second DFS on G^T with finish order ensures only vertices within same SCC are discovered.
- **Tarjan's SCC algorithm**: single DFS using lowlink values (no transpose needed).
- **Applications**: dependency resolution, program optimization (loop detection), web page ranking.

**Edge Cases**: Self-loops = back edges; BFS distances independent of adjacency order, tree structure depends on it; DAG required for topological sort (cycle → impossible); Kosaraju works for any directed graph.

---

### Ch. 21 — Minimum Spanning Trees

**Cut Property** (Theorem 21.1): Light edge crossing any cut that respects A is safe for A. Proof: cut-and-paste.

**Cycle Property**: Heaviest edge on any cycle is in no MST.

**Kruskal's algorithm**
```
MST-KRUSKAL(G, w)
    A = ∅
    for each v ∈ G.V   MAKE-SET(v)
    sort edges of G.E by nondecreasing weight w
    for each edge (u,v) ∈ G.E in order
        if FIND-SET(u) ≠ FIND-SET(v)
            A = A ∪ {(u,v)}
            UNION(u, v)
    return A
```
- Sort edges by weight; add if no cycle (FIND-SET). O(E lg E) = O(E lg V) (sorting dominates).
- Builds forest (multiple trees merge). Uses disjoint-set data structure.
- **Cut Property** (safe edge): Across any cut that respects A, lightest edge is safe.

**Prim's algorithm**
```
MST-PRIM(G, w, r)
    for each u ∈ G.V: u.key = ∞, u.π = NIL
    r.key = 0
    Q = G.V   (min-priority queue keyed by .key)
    while Q ≠ ∅
        u = EXTRACT-MIN(Q)
        for each v ∈ G.Adj[u]
            if v ∈ Q and w(u,v) < v.key
                v.π = u; v.key = w(u,v)   (DECREASE-KEY)
```
- Grow single tree from root r; add lightest edge connecting tree to non-tree vertex.
- O(E lg V) with binary heap (E DECREASE-KEY + V EXTRACT-MIN), O(V²) with array for dense graphs, O(E + V lg V) with Fibonacci heap.

**Uniqueness**: If every cut has unique light edge, MST is unique. All MSTs have same sorted edge weight list.

**Comparisons**:
| Dimension | Kruskal | Prim |
|-----------|---------|------|
| Strategy | Edge-based (global min) | Vertex-based (grow tree) |
| DS | Disjoint-set + sorting | Min-priority queue |
| Best for sparse | O(E lg V) | O(E lg V) binary |
| Best for dense | O(E lg V) | O(V²) array |

---

### Ch. 22 — Single-Source Shortest Paths

**Relaxation**: If v.d > u.d + w(u,v), update v.d = u.d + w(u,v), v.π = u.

**Properties** (Section 22.5):
1. Triangle inequality: δ(s,v) ≤ δ(s,u) + w(u,v)
2. Upper-bound: v.d ≥ δ(s,v) always; once v.d = δ(s,v), never changes
3. No-path: unreachable → v.d = ∞ always
4. Convergence: if s⇝u→v is shortest path and u.d = δ(s,u) before relaxing (u,v), then v.d = δ(s,v) after
5. Path-relaxation: edges (v₀,v₁), (v₁,v₂), ..., (v_{k-1},v_k) relaxed in order → v_k.d = δ(s,v_k)
6. Predecessor-subgraph: G_π = (V_π, E_π) is a shortest-paths tree rooted at s

**Bellman-Ford**
```
BELLMAN-FORD(G, w, s)
    INITIALIZE-SINGLE-SOURCE(G, s)   // s.d=0, all others ∞
    for i = 1 to |G.V| - 1
        for each edge (u,v) ∈ G.E
            RELAX(u, v, w)
    for each edge (u,v) ∈ G.E
        if v.d > u.d + w(u,v)
            return FALSE   // negative-weight cycle
    return TRUE
```
- Relax all edges |V|-1 times (any shortest path has ≤ |V|-1 edges).
- O(VE). Detects negative-weight cycles reachable from s.
- **Lemma 22.2**: After i iterations, Bellman-Ford finds shortest paths with ≤ i edges (path-relaxation property).
- **DAG Shortest Paths**: Θ(V+E). Topological sort + relax each edge once in order. Handles negative edges (no cycles). Fastest when applicable.

**Dijkstra**
```
DIJKSTRA(G, w, s)
    INITIALIZE-SINGLE-SOURCE(G, s)
    S = ∅
    Q = G.V   (min-priority queue keyed by .d)
    while Q ≠ ∅
        u = EXTRACT-MIN(Q)
        S = S ∪ {u}
        for each v ∈ G.Adj[u]
            RELAX(u, v, w)   // may call DECREASE-KEY
```
- Greedy: always extracts vertex with minimum shortest-path estimate.
- Requires nonnegative weights (Theorem 22.10: once extracted, u.d = δ(s,u)).
- O(V²) with array, O(E lg V) with binary heap, O(V lg V + E) with Fibonacci heap.

| Algorithm | Negative edges | Cycles | Time |
|-----------|---------------|--------|------|
| BFS | No | No cycles | O(V+E) |
| Bellman-Ford | Yes | Detects | O(VE) |
| DAG-SP | Yes | None | Θ(V+E) |
| Dijkstra | No | Not allowed | O(E lg V) |

**Difference constraints**: xⱼ - xᵢ ≤ bₖ → constraint graph w(vᵢ, vⱼ) = bₖ; solve with Bellman-Ford.

---

### Ch. 23 — All-Pairs Shortest Paths

**Floyd-Warshall**: DP on intermediate vertices. d^(k)_ij = min(d^(k-1)_ij, d^(k-1)_ik + d^(k-1)_kj). Θ(V³). In-place Θ(V²) space.

**Matrix multiplication APSP**: EXTEND-SHORTEST-PATHS (min,+ multiplication) repeated. SLOW-APSP Θ(V⁴). FASTER-APSP (repeated squaring) Θ(V³ lg V).

**Johnson's algorithm**: Add super-source s, Bellman-Ford for h(v), reweight ŵ(u,v) = w(u,v) + h(u) - h(v), then Dijkstra from each vertex. O(V² lg V + VE). Best for sparse graphs with negative edges.

**Reweighting lemma**: ŵ(p) = w(p) + h(v₀) - h(v_k). Preserves shortest paths; nonnegative ŵ via triangle inequality.

**Transitive closure**: Boolean variant of Floyd-Warshall: t^(k)_ij = t^(k-1)_ij ∨ (t^(k-1)_ik ∧ t^(k-1)_kj). Θ(V³).

| Algorithm | Complexity | Best for |
|-----------|-----------|----------|
| Floyd-Warshall | Θ(V³) | Dense |
| FASTER-APSP | Θ(V³ lg V) | Dense |
| Johnson | O(V² lg V + VE) | Sparse, negative edges |
| Dijkstra × V | O(VE lg V) | Sparse, nonnegative |

---

### Ch. 24 — Maximum Flow

**Flow network**: Directed G=(V,E) with capacity c(u,v) ≥ 0, source s, sink t. Flow f satisfies capacity constraint (0 ≤ f ≤ c) and flow conservation (in = out for non-source/sink).

**Ford-Fulkerson method**
```
FORD-FULKERSON(G, s, t)
    for each edge (u,v) ∈ G.E: f(u,v) = 0
    while there exists augmenting path p in residual network G_f
        c_f(p) = min{c_f(u,v) : (u,v) ∈ p}
        for each edge (u,v) ∈ p
            if (u,v) ∈ E   f(u,v) = f(u,v) + c_f(p)
            else            f(v,u) = f(v,u) - c_f(p)
    return f
```
- While augmenting path p exists in G_f, augment flow by bottleneck capacity.
- Worst-case O(E |f*|) with integer capacities (pathological: saturates 1 unit each time).

**Residual network G_f**: Edge capacities: c_f(u,v) = c(u,v) - f(u,v) forward, f(v,u) backward. 
- Augmenting path p: simple s→t path in G_f. Augment by c_f(p) = min{c_f(u,v) along p}.
- **Lemma 24.1**: f' (after augmentation) is a flow in G with |f'| = |f| + c_f(p) > |f|.

**Max-Flow Min-Cut Theorem** (Theorem 24.6): For any flow network, TFAE:
1. f is a maximum flow
2. G_f has no augmenting path
3. |f| = c(S,T) for some cut (S,T)
- **Proof**: (1)⇒(2): path contradicts maximality. (2)⇒(3): S = vertices reachable from s in G_f; edges S→T saturated → |f| = c(S,T). (3)⇒(1): |f| ≤ c(S,T) for any cut (Corollary 24.5).

**Edmonds-Karp**: Ford-Fulkerson using BFS (shortest augmenting path in terms of #edges).
- O(V E²). Each edge becomes critical (bottleneck) ≤ |V|/2 times → O(VE) augmentations.
- **Theorem 24.8**: After each augmentation, shortest-path distance from s to any v is nondecreasing.

**Integrality Theorem** (Theorem 24.10): With integer capacities, Ford-Fulkerson produces integer-valued max flow. Crucial for bipartite matching reduction.

**Maximum bipartite matching**: Reduce to max flow: source→left(1), left→right(1), right→sink(1) capacities. Matching M ↔ integer flow of value |M|.

**Push-Relabel algorithm**: Local operations: push (move flow along edge), relabel (increase height). O(V² E) generic, O(V³) with FIFO. Practical alternative to augmenting paths.
- **Preflow**: flow that may exceed conservation (excess at vertices).
- **Height function h**: valid if h(s)=|V|, h(t)=0, h(u) ≤ h(v)+1 for every residual edge.
- **Discharge**: repeatedly push from overflowing vertex with highest label.

**Comparisons**:
| Algorithm | Complexity | Notes |
|-----------|-----------|-------|
| Ford-Fulkerson | O(E|f*|) | Can be exponential |
| Edmonds-Karp | O(VE²) | Polynomial |
| Capacity scaling | O(E² lg C) | Reduces iterations |
| Push-relabel | O(V³) | Practical, dominates |

---

### Ch. 25 — Matchings in Bipartite Graphs

**Berge's Theorem**: M is maximum matching ⇔ no M-augmenting path exists in G.
- **M-augmenting path**: starts and ends at unmatched vertices, alternates non-matching/matching edges.
- Used to prove correctness of all augmenting-path matching algorithms.

**Hopcroft-Karp (Maximum bipartite matching)**
```
HOPCROFT-KARP(G)
    M = ∅
    while there exists an augmenting path
        run BFS from unmatched left vertices to find shortest augmenting paths
        find maximal set of vertex-disjoint shortest augmenting paths via DFS (layered DAG)
        augment M by all paths simultaneously
    return M
```
- O(√V · E). Each phase increases shortest path length; ≤ 2√V phases.
- BFS creates layered graph (alternating levels). DFS finds vertex-disjoint paths (O(E) per phase).

**Gale-Shapley (Stable Marriage)**
```
GALE-SHAPLEY(H, W)
    for each man m ∈ H: m.free = true
    while ∃ free man m with nonempty preference list
        w = highest-ranked woman on m's list not yet proposed to
        if w.free
            engage m and w
        else if w prefers m over current m'
            free m', engage m and w
        else
            m remains free (rejected)
    return matching
```
- O(n²) worst-case. Always produces a stable matching.
- **Properties**: Man-optimal (proposing) or woman-optimal depending on who proposes. Woman-optimal variant: women propose, men decide.
- **Theorem 25.8**: All stable matchings have same size; proposing side gets optimal matching, receiving side gets pessimal.

**Hungarian Algorithm (Assignment Problem)**
- Find max-weight perfect matching in complete bipartite graph with |L| = |R|.
- **Key ideas**: feasible labeling ℓ (ℓ(u)+ℓ(v) ≥ w(u,v)), equality subgraph G_ℓ (edges with equality). Theorem: If G_ℓ has perfect matching, it's optimal.
- O(n³) with careful implementation (slack array). O(n⁴) naive.
- **Steps**: Initialize ℓ, find max matching in G_ℓ. If not perfect, update ℓ (decrease for unmatched left, increase for unmatched right).

**Hall's Theorem**: Perfect bipartite matching exists iff |A| ≤ |N(A)| for all A ⊆ L.

| Problem | Algorithm | Complexity |
|---------|-----------|-----------|
| Max bipartite matching | Hopcroft-Karp | O(√V·E) |
| Stable marriage | Gale-Shapley | O(n²) |
| Assignment (max weight) | Hungarian | O(n³) |

---

### Ch. 26 — Parallel Algorithms

**Fork-Join Model**: 
- **spawn**: May execute in parallel with caller (scheduling is up to runtime).
- **sync**: Wait for all spawned children to complete.
- **pfor** (parallel for loop): Implemented via recursive spawning (divide range in half, spawn each half).
- **Nested parallelism**: spawn within spawn; sync joins at multiple levels.

**Work and Span Analysis**:
- **Work T₁**: Total number of operations (1 processor). Represents serial time.
- **Span T_∞**: Length of critical path (infinite processors). Longest chain of dependencies.
- **Space**: T_P ≥ max(T₁/P, T_∞) — lower bound for P processors.
- **Greedy Scheduling** (Graham-Brent Theorem): T_P ≤ T₁/P + T_∞. Achieved by greedy scheduler.
- **Parallelism**: T₁/T_∞ = maximum possible speedup (linear speedup if T₁/T_∞ ≥ P).
- **Perfect linear speedup**: T_P = T₁/P (requires T_∞ ≤ T₁/P).

**Parallel Merge Sort (P-MERGE)**:
- MERGE(A,B,C): Use binary search on longer array to split; recursively merge pairs in parallel.
- Work: T₁ = Θ(n). Span: T_∞ = Θ(lg² n). Parallelism: Θ(n/lg² n).
- P-MERGE-SORT: Work Θ(n lg n), Span Θ(lg n · lg lg n), Parallelism Θ(n/lg lg n).

**Parallel Matrix Multiply (P-MATRIX-MULTIPLY)**:
- Divide 2×2 blocks, recursively spawn multiplications in parallel.
- Work: T₁ = Θ(n³). Span: T_∞ = Θ(lg n). Parallelism: Θ(n³/lg n).
- Strassen-based: Work Θ(n^{lg7}), Span Θ(lg² n).

**Parallel Sample Sort (P-SAMPLE-SORT)**:
- Select p-1 splitters via random sampling, partition, recursively sort buckets.
- Work: Θ(n lg n), Span: Θ(lg² n) with high probability.
- **Linear speedup** with n processors when n is large enough.

**Parallel Design Principles**:
- **Amdahl's Law**: Speedup ≤ 1/((1-f) + f/P) where f = parallel fraction.
- **Work-efficient**: T₁ = O(T_best_serial). Avoid parallel slowdown for small inputs.
- **Granularity**: Too fine → overhead dominates; too coarse → low parallelism.

---

### Ch. 27 — Online Algorithms

**Competitive analysis**: C_ONLINE(I) ≤ ρ · C_OPT(I) + α for all input sequences I. ρ = competitive ratio. If α = 0, ρ-competitive.

**Ski-Rental Problem**:
- Rent skis $1/day or buy $B. Future unknown. Deterministic: rent B-1 days then buy → cost = B-1 + B = 2B-1. OPT cost = min(B, total days). Worst-case: total days = B → competitive ratio 2 - 1/B.
- **Randomized**: Rent with probability 1/(B-1), buy otherwise. Optimal ratio e/(e-1) ≈ 1.582.

**Move-to-Front (List Accessing)**:
- After accessing element, move it to front of (linked) list.
- **Theorem 27.1**: MTF is 2-competitive against optimal offline algorithm (which knows all future accesses).
- **Cost model**: paying c_i to access element at position i, cost 1 to swap adjacent elements.

**Caching (Paging)**:
- **Model**: Cache size k. On miss (fault), fetch page from slow memory, evict one if cache full.
- **Marking algorithm**: Mark pages when requested. On fault, evict unmarked page. If all marked, clear marks.
- **Deterministic**: LRU, FIFO, Marking are all k-competitive. No deterministic algorithm can beat k-competitive (adversary can force a fault on every k+1 requests).
- **LIFO is not competitive** — adversary can force faults every other access by cycling through two pages not at top.
- **Randomized**: Random Marking = O(lg k) competitive. Lower bound: Ω(lg k) (no randomized algorithm beats this).
- **Fiat et al.**: Tight bound Θ(lg k) for randomized paging.

**Online Learning (Weighted Majority)**:
- n experts predict binary outcomes daily. Follow majority weighted by past accuracy.
- Mistake bound: M ≤ 2(1+η)m* + (2 ln n)/η where m* = best expert's mistakes.
- With randomized weights: E[M] ≤ (1+η)m* + (ln n)/η.

---

### Ch. 28 — Matrix Operations

**LUP Decomposition**: PA = LU where L is unit lower-triangular, U upper-triangular, P permutation.
- **LUP-SOLVE**: (1) Solve Ly = Pb (forward substitution, O(n²)); (2) Solve Ux = y (back substitution, O(n²)).
- **Total**: Θ(n³) decomposition + O(n²) solve. For multiple b (same A), reuse decomposition.
- **No pivoting**: Without permutation, LU may fail when pivot is 0 (division by zero). Pivoting ensures numerical stability.
- **Dense vs sparse**: Dense → LUP; Sparse → iterative methods (conjugate gradient).

**Matrix inversion**: Solve A·X = I → compute LUP, then solve for each column of I. Θ(n³) total. Strassen-based: Θ(n^{lg 7}) with careful recursive formulation.

**Positive-definite matrices**: x^T A x > 0 for all nonzero x.
- **Cholesky decomposition**: A = LL^T, L lower triangular. Work = Θ(n³/3) — half of LU (Θ(2n³/3)).
- **Cholesky algorithm**: for j=1..n: compute L[j,j] = √(A[j,j] - Σ_{k<j} L[j,k]²); for i=j+1..n: L[i,j] = (A[i,j] - Σ_{k<j} L[i,k]L[j,k]) / L[j,j].
- **Symmetric** positive-definite required. More stable than LU due to structure.

**Least squares**: Minimize ||Ax - b||₂ (overdetermined, m>n).
- **Normal equations**: A^T A x = A^T b. Solve via Cholesky. Condition number squared — can lose precision.
- **QR decomposition**: A = QR, Q orthogonal, R upper triangular. Solve Rx = Q^T b. More stable. Θ(mn²) with Householder reflections.
- **SVD**: A = UΣV^T. Most numerically stable. x = VΣ⁻¹U^T b. Θ(mn² + n³).

**Determinant**: Via LUP: det(A) = det(P)·Π U[i,i]. O(n³).

---

### Ch. 29 — Linear Programming

**Standard form**: maximize c^T x subject to Ax ≤ b, x ≥ 0.
- **Slack form**: Maximize z = c^T x, subject to Ax + s = b, x ≥ 0, s ≥ 0 (s are slack variables).
- **Basic feasible solution**: Set n nonbasic variables to 0, solve for m basic variables. BFS = vertex of feasible polytope.

**Duality**:
- **Primal** (max): max c^T x, Ax ≤ b, x ≥ 0.
- **Dual** (min): min b^T y, A^T y ≥ c, y ≥ 0.
- **Weak duality**: c^T x ≤ b^T y for any feasible (x,y). Proof: c^T x ≤ (A^T y)^T x = y^T(Ax) ≤ y^T b.
- **Strong duality**: If primal (or dual) has an optimal solution, so does the other, and c^T x* = b^T y*.
- **Complementary Slackness**: xⱼ > 0 ⇒ Σ_i a_ij y_i = cⱼ; yᵢ > 0 ⇒ Σ_j a_ij xⱼ = bᵢ.

**Simplex Algorithm**:
- Move from one BFS to adjacent BFS with better objective.
- **Pivot**: Choose entering variable (positive reduced cost), exiting variable (minimum ratio test).
- **Cycling**: Can loop forever. **Bland's rule**: choose smallest-index entering/exiting → guaranteed termination.
- **Worst-case**: Klee-Minty hypercube → exponential (2ⁿ iterations).
- **Smoothed complexity**: Polynomial after random perturbation (Spielman-Teng, 2004).

**Ellipsoid Method (Khachiyan, 1979)**: First polynomial-time LP algorithm. O(n⁴·L) operations, O(n⁶·L²) bit complexity. Not practical.

**Interior Point Methods (Karmarkar, 1984)**:
- Follow central path through interior of feasible region. O(n³·L) total time. Practical for large problems.
- **Barrier methods**: Add logarithmic barrier for inequality constraints. Solve sequence of Newton iterations.
- **Primal-Dual methods**: Simultaneously update primal and dual variables. Fastest in practice.

**LP Applications**: 
- Max flow, min cost flow, bipartite matching, assignment, game theory (Nash equilibrium via zero-sum LP).
- **Integer Linear Programming** (ILP): Constraints x ∈ ℤ. NP-hard in general. Branch-and-bound.
- **0-1 ILP**: Variables ∈ {0,1}. NP-complete (reduction from SAT).

---

### Ch. 30 — Polynomials and FFT

**Polynomial representations**:
- **Coefficient**: a(x) = Σ_{j=0}^{n-1} a_j x^j. Multiply: O(n²) naive.
- **Point-value**: (x₀,y₀), ..., (x_{n-1},y_{n-1}) for n distinct x_k. Multiply: O(n). Interpolate: O(n²) Gaussian, O(n lg n) FFT.

**DFT and Roots of Unity**:
- ω_n = e^{2πi/n} = cos(2π/n) + i·sin(2π/n). Principal n-th root of unity.
- **Properties**: ω_n^n = 1; ω_n^k ≠ 1 for 0<k<n; ω_{2n}^{2k} = ω_n^k; ω_n^{k+n/2} = -ω_n^k.
- **DFT**: Evaluate A(x) at ω_n⁰, ω_n¹, ..., ω_n^{n-1}.

**FFT (Cooley-Tukey, 1965)**:
```
RECURSIVE-FFT(a)   // a is coefficient vector, n = length (power of 2)
    if n == 1   return a
    ω_n = e^{2πi/n}, ω = 1
    a⁰ = (a₀, a₂, ..., a_{n-2})   // even
    a¹ = (a₁, a₃, ..., a_{n-1})   // odd
    y⁰ = RECURSIVE-FFT(a⁰)        // DFT of even
    y¹ = RECURSIVE-FFT(a¹)        // DFT of odd
    for k = 0 to n/2-1
        y_k = y⁰_k + ω·y¹_k
        y_{k+n/2} = y⁰_k - ω·y¹_k
        ω = ω·ω_n
    return y
```
- Recurrence: T(n) = 2T(n/2) + Θ(n) → Θ(n lg n).
- **Inverse FFT**: Same algorithm with ω_n^{-1} (conjugate), divide by n. Θ(n lg n).

**Convolution (Polynomial Multiplication)**:
- a(x)·b(x): Coefficient vector c_k = Σ_{i+j=k} a_i·b_j. O(n²) naive.
- **FFT-based**: (1) Evaluate A and B at n roots of unity (FFT, O(n lg n)); (2) C[k] = A[k]·B[k] (pointwise, O(n)); (3) Inverse FFT (O(n lg n)). Total: Θ(n lg n).

**Schönhage-Strassen Algorithm** (1971): Large integer multiplication via FFT. O(n lg n lg lg n). Used in GMP (GMP). Theoretical record until 2007.

**Practical FFT issues**:
- Bit-reversal permutation for in-place FFT.
- **Bluestein's algorithm**: FFT for arbitrary n (not just powers of 2).
- **Number-theoretic transform (NTT)**: FFT over finite field ℤ_p where p = k·2^m + 1. No floating-point errors.

---

### Ch. 31 — Number-Theoretic Algorithms

---

### Ch. 31 — Number-Theoretic Algorithms

**Euclid's algorithm**
```
EUCLID(a, b)
    while b ≠ 0
        r = a mod b; a = b; b = r
    return a
```
- O(lg b) divisions. Worst-case: consecutive Fibonacci numbers (Lamé's theorem: O(lg min(a,b))).
- Recursive version: EUCLID(a,b) = if b==0 then a else EUCLID(b, a mod b).

**Extended Euclid**
```
EXTENDED-EUCLID(a, b)
    if b == 0   return (a, 1, 0)
    (d, x', y') = EXTENDED-EUCLID(b, a mod b)
    (d, x, y) = (d, y', x' - ⌊a/b⌋·y')
    return (d, x, y)
```
- Returns (d, x, y) where d = gcd(a,b) = a·x + b·y. O(lg b).
- Computes modular inverses: a⁻¹ mod n = x mod n where x is from EXTENDED-EUCLID(a,n) (requires gcd=1).

**Modular arithmetic**: ℤₙ = {0,…,n-1}. a⁻¹ mod n exists iff gcd(a,n)=1. φ(n) = n ∏_{p|n}(1-1/p) (Euler's totient).
- **Fermat's theorem**: a^{p-1} ≡ 1 (mod p) for prime p ∤ a.
- **Euler's theorem**: a^{φ(n)} ≡ 1 (mod n) for gcd(a,n)=1.

**Modular exponentiation**: Square-and-multiply
```
MODULAR-EXPONENTIATION(a, b, n)
    result = 1
    while b > 0
        if b is odd   result = (result·a) mod n
        a = a² mod n
        b = b >> 1
    return result
```
- Θ(lg b) time (b's bit length). Avoids huge intermediate values.

**RSA (Rivest-Shamir-Adleman, 1977)**
- **Key generation**: Choose large primes p,q. n = p·q. Choose e with gcd(e, φ(n))=1. Compute d = e⁻¹ mod φ(n). Public: (n,e). Private: (d).
- **Encrypt**: c = m^e mod n. **Decrypt**: m = c^d mod n.
- **Correctness**: m^{e·d} ≡ m (mod n) by Euler's theorem + CRT. Security based on hardness of factoring n.

**Primality testing**:
- **Fermat test**: a^{n-1} mod n ≠ 1 → composite. **Carmichael numbers** (e.g., 561) pass all a with gcd(a,n)=1.
- **Miller-Rabin**: Write n-1 = 2^s·t with t odd. Check a^t mod n ≠ 1 and no -1 in repeated squaring. Error ≤ 4^{-k}. Practical for cryptography.
- **AKS (Agrawal-Kayal-Saxena, 2002)**: First deterministic polynomial-time primality test. O((log n)^{12}) = O(n^{12}) naive → O((log n)^{7.5}) improved.

**Chinese Remainder Theorem** (Theorem 31.27): System x ≡ aᵢ (mod nᵢ), pairwise coprime nᵢ → unique solution modulo N = ∏ nᵢ.
- **Solution**: x = Σ aᵢ·Nᵢ·yᵢ mod N where Nᵢ = N/nᵢ, yᵢ = Nᵢ⁻¹ mod nᵢ.

**Discrete logarithms**: Given g, h in ℤₚ, find x with g^x ≡ h (mod p). Hard for large p.
- **Baby-step giant-step**: O(√n) time and space. Write x = i⌈√n⌉ + j, tabulate g^j, check h·g^{-i⌈√n⌉}.
- Basis for Diffie-Hellman key exchange and ElGamal encryption.

---

### Ch. 32 — String Matching

| Algorithm | Preprocessing | Matching | Space |
|-----------|:---:|:---:|:---:|
| Naive | 0 | O(nm) | 0 |
| Rabin-Karp | O(m) | O(n+m) avg | O(1) |
| FA (automaton) | O(m|Σ|) | O(n) | O(m|Σ|) |
| KMP | O(m) | O(n) | O(m) |

**Rabin-Karp**
```
RABIN-KARP(T, P, d, q)
    n = T.length, m = P.length
    h = d^{m-1} mod q
    p = 0; t₀ = 0
    for i = 1 to m
        p = (d·p + P[i]) mod q
        t₀ = (d·t₀ + T[i]) mod q
    for s = 0 to n-m
        if p == t_s
            if P[1:m] == T[s+1:s+m]   // verify (possible spurious hit)
                print "match at shift s"
        if s < n-m
            t_{s+1} = (d·(t_s - T[s+1]·h) + T[s+m+1]) mod q
```
- Rolling hash: computes next hash in O(1) from previous. Expected O(n+m). Worst-case Θ(nm) (many spurious hits).
- Choose q large (e.g., 2^31-1) to minimize collisions. d = alphabet size (e.g., 256 for ASCII).

**KMP (Knuth-Morris-Pratt)**
```
KMP-MATCHER(T, P)
    n = T.length, m = P.length
    π = COMPUTE-PREFIX-FUNCTION(P)
    q = 0   // number of matched characters
    for i = 1 to n
        while q > 0 and P[q+1] ≠ T[i]   q = π[q]
        if P[q+1] == T[i]   q++
        if q == m
            print "match at shift" i-m
            q = π[q]

COMPUTE-PREFIX-FUNCTION(P)
    m = P.length, π[1] = 0
    k = 0
    for q = 2 to m
        while k > 0 and P[k+1] ≠ P[q]   k = π[k]
        if P[k+1] == P[q]   k++
        π[q] = k
    return π
```
- Prefix function π[q] = longest proper prefix of P that is suffix of P[1:q].
- O(n+m) — no backtracking in T. Each char compared at most once.
- **Idea**: On mismatch, use π to shift pattern without missing matches.

**Suffix array**: SA[i] = starting index of i-th lexicographically smallest suffix of T.
- **Construction**: O(n) via SA-IS (Suffix Array Induced Sorting) or O(n lg n) via doubling.
- **LCP array**: Longest Common Prefix between adjacent suffixes in SA. Built in O(n) via Kasai algorithm.
- **Pattern matching**: Binary search over SA using LCP for acceleration: O(m + lg n) with LCP, O(m lg n) without.
- **Applications**: substring search, longest repeated substring, longest common substring, Burrows-Wheeler transform.

---

### Ch. 33 — Machine-Learning Algorithms

**k-Means (Lloyd's Procedure)**:
```
K-MEANS(X[1:n], k)
    randomly select k initial centroids c₁,…,c_k from X
    repeat until convergence
        for i = 1 to n
            assign x_i to cluster j = argmin_j ||x_i - c_j||²
        for j = 1 to k
            c_j = mean of points in cluster j
    return centroids and assignments
```
- Converges to local minimum (not global). O(T·d·k·n) per iteration (T iterations, d dimensions, k clusters, n points).
- **Initialization**: k-means++ (spread-out initial centers) gives O(lg k) approximation guarantee.
- **Choosing k**: Elbow method (within-cluster SSE vs k), silhouette score, gap statistic.
- **Limitations**: Assumes spherical clusters, sensitive to outliers, local minima.

**Multiplicative-Weight Algorithm (Weighted Majority)**:
```
WEIGHTED-MAJORITY(n, experts)
    w_i = 1 for i = 1..n   // weights
    for each day t
        predict = argmax_j Σ_{i: expert_i predicts j} w_i
        observe true outcome
        for each expert i that was wrong
            w_i = w_i·(1-γ)   // γ = learning rate (e.g., 1/2)
```
- **Deterministic bound**: Mistakes ≤ 2(1+γ)·m* + (2 ln n)/γ where m* = best expert's mistakes.
- **Randomized variant**: Sample expert proportional to weights. Expected mistakes ≤ (1+γ)·m* + (ln n)/γ.
- **Regret**: Difference between algorithm's mistakes and best expert's. Randomized: O(√T ln n) for optimal γ.
- **Applications**: Online learning, boosting (AdaBoost as special case), game theory (fictitious play).

**Gradient Descent**:
```
GRADIENT-DESCENT(f, x₀, T, γ)
    x = x₀
    for t = 1 to T
        x = x - γ·∇f(x)   // move opposite gradient
    return weighted average Σ (x_t)/T
```
- For convex f with ||x₀ - x*|| ≤ R (bound on distance) and ||∇f(x)|| ≤ L (Lipschitz gradient):
  - f(x_avg) - f(x*) ≤ R·L/√T after T iterations.
- **Learning rate**: γ = R/(L·√T) gives optimal convergence.
- **Stochastic GD**: Use random sample ∇̂f instead of full gradient. Slower per-iteration (convergence O(1/√T)), faster per-data-point.
- **Momentum**: v_t = β·v_{t-1} + ∇f(x_t); x_{t+1} = x_t - γ·v_t. Accelerates convergence.

**Constrained GD**: Projection Π_K(x) = argmin_{y∈K} ||x - y||. x_{t+1} = Π_K(x_t - γ·∇f(x_t)). Same asymptotic bound.
- **Projected GD**: For convex compact K. Each iteration: gradient step + projection.
- **Mirror descent**: Generalized projection using Bregman divergence. For non-Euclidean geometry.

---

### Ch. 34 — NP-Completeness

**Complexity classes**: 
- **P** = {L: L can be decided by a polynomial-time algorithm}. Examples: shortest path, MST, sorting.
- **NP** = {L: L can be verified in polynomial time given a certificate}. "Solution verifiable in polynomial time." Examples: SAT, TSP, CLIQUE, SUBSET-SUM.
- **NP-complete (NPC)**: L ∈ NP and every L' ∈ NP reduces to L in polynomial time (L' ≤ₚ L). Hardest problems in NP.
- **NP-hard**: L' ≤ₚ L for every L' ∈ NP (L may or may not be in NP). Includes optimization variants (e.g., TSP-OPT).

**P ≠ NP** is central open question (Clay Millennium Problem). If any NPC problem ∈ P, then P = NP.

**Polynomial-time reduction**: L₁ ≤ₚ L₂: exists polynomial-time computable function f such that x ∈ L₁ ⇔ f(x) ∈ L₂.
- Reductions are transitive: L₁ ≤ₚ L₂ and L₂ ≤ₚ L₃ ⇒ L₁ ≤ₚ L₃.
- To prove L is NP-complete: (1) Show L ∈ NP (polynomial certificate and verifier); (2) Show L' ≤ₚ L for some known NPC problem L'.

**Standard NP-complete problems and reduction chain**:
1. **CIRCUIT-SAT** (Theorem 34.7): Given boolean circuit, is there a satisfying assignment? First problem proved NP-complete (Cook-Levin, 1971). Proof: encode TM computation as circuit with AND/OR/NOT gates.
2. **SAT** ← CIRCUIT-SAT: transform circuit gates into CNF clauses (Tseitin transformation).
3. **3-CNF-SAT** ← SAT: parse SAT formula as parse tree, add auxiliary variables, convert to 3-CNF.
4. **CLIQUE** ← 3-CNF-SAT: Create vertex per literal occurrence; edge between consistent literals in different clauses. k = number of clauses. Clique of size k ⇔ satisfying assignment.
5. **VERTEX-COVER** ← CLIQUE: Complement graph Ḡ = (V, Ē). CLIQUE of size k in G ⇔ VERTEX-COVER of size |V|-k in Ḡ.
6. **HAM-CYCLE** ← VERTEX-COVER: Widgets for edges (selector paths) and vertices (cover verification). Complex gadget construction.
7. **TSP** ← HAM-CYCLE: Complete graph with edge costs: 0 for edges in G, 1 for non-edges. HAM-CYCLE in G ⇔ TSP tour of cost ≤ 0.
8. **SUBSET-SUM** ← 3-CNF-SAT: Base-10 digit encoding of clauses and variables. Variable numbers (v_i, v'_i) and slack numbers per clause.

**Reduction strategies**: 
- **Restriction**: Show problem contains known NPC problem as special case.
- **Local replacement**: Replace each element with small gadget (3-CNF→CLIQUE).
- **Component design**: Build components that interact (HAM-CYCLE gadgets).
- **Gadgets**: Subgraphs/structures that enforce constraints (SAT→SUBSET-SUM).

**Other NP-complete problems**: 3-Colorability (± gadget from 3-CNF-SAT), Independent Set (± from CLIQUE), Hamiltonian Path, Set Partition, 0-1 Integer Programming, Subgraph Isomorphism, Dominating Set, Feedback Vertex Set.

**Problems known to be in P**: 
- 2-CNF-SAT (implication graph + SCCs — linear), 
- GRAPH-ISOMORPHISM status unknown (not known NP-complete, not known in P; Babai's quasipolynomial algorithm), 
- PRIMALITY (AKS, 2002 — polynomial), 
- Linear programming (ellipsoid, interior-point — polynomial).

**In P**: 2-CNF-SAT (implication graph SCCs), GRAPH-ISOMORPHISM status unclear.

---

### Ch. 35 — Approximation Algorithms

**Performance ratios**: C ≤ ρ·C* (minimization) or C* ≤ ρ·C (maximization), ρ ≥ 1.
- **PTAS** (Polynomial-Time Approximation Scheme): (1+ε)-approximation, polynomial in n for fixed ε (might be n^{1/ε}).
- **FPTAS** (Fully PTAS): polynomial in n and 1/ε (e.g., O(n³/ε)). Best possible for NP-hard optimization.
- **APX**: Problems with constant-factor approximation (no PTAS unless P=NP for many).

**Vertex Cover (2-approximation)**:
```
APPROX-VERTEX-COVER(G)
    C = ∅
    E' = G.E
    while E' ≠ ∅
        pick arbitrary (u,v) ∈ E'
        C = C ∪ {u,v}
        remove all edges incident to u or v from E'
    return C
```
- Picks any edge, adds both endpoints, removes incident edges. Lower bound: maximal matching size |M|.
- |C| = 2|M| ≤ 2|OPT| (since OPT must cover M, each edge needs distinct vertex).
- **Weighted Vertex Cover**: LP relaxation + rounding (set x(v) ≥ 1/2) → 2-approximation. LP: minimize Σ w(v)·x(v), x(u)+x(v) ≥ 1 for all edges.

**TSP with triangle inequality**:
- **2-approximation** (Theorem 35.2): Compute MST T, do preorder walk of T (visit each vertex when first encountered). Cost(TSP) ≤ 2·Cost(optimal TSP). MST is lower bound on OPT (removing edge from optimal tour gives spanning tree).
- **Christofides algorithm** (3/2-approximation): (1) MST T; (2) minimum-weight perfect matching on odd-degree vertices of T; (3) Eulerian tour on combined multigraph; (4) shortcut to Hamiltonian cycle.
- **General TSP** (without triangle inequality): No constant-factor approximation unless P=NP (Theorem 35.3). Reduction from HAM-CYCLE: cost 0 for edges in G, cost 1 otherwise. Distinguishing cost 0 vs cost n is NP-hard.

**Set Cover (Greedy)**:
```
GREEDY-SET-COVER(X, F)
    U = X   // uncovered elements
    C = ∅
    while U ≠ ∅
        select S ∈ F that maximizes |S ∩ U|   // most uncovered elements covered
        U = U - S
        C = C ∪ {S}
    return C
```
- O(ln |X|)-approximation. **Theorem 35.4**: Greedy achieves H(d)-approximation where d = max set size.
- **Tight bound**: H_n = ln n + O(1) — no polynomial algorithm can do better unless P=NP.
- **Weighted Set Cover**: Greedy picks set minimizing cost per newly covered element.

**MAX-3-CNF-SAT**: Random assignment satisfies each clause with probability 7/8 → expected 8/7-approximation.
- **Derandomization via method of conditional expectations**: Fix variables greedily, maintain conditional expectation > 7/8 of clauses.

**Subset-Sum (FPTAS)**:
```
APPROX-SUBSET-SUM(S, t, ε)
    n = |S|, L₀ = ⟨0⟩
    for i = 1 to n
        L_i = MERGE(L_{i-1}, L_{i-1} + x_i)   // union
        remove duplicates and trim: if y ≤ (1+ε/2n)·y', remove y
    return max element ≤ t in L_n
```
- Trims lists with δ = ε/2n. O(poly(n, 1/ε)). Running time: O(n³/ε).
- **PTAS vs FPTAS**: Subset-Sum has FPTAS. MAX-CLIQUE has no PTAS unless P=NP.
- **0-1 Knapsack**: Also has FPTAS via rounding profits to O(n/ε) distinct values.

**Key results table**:
| Problem | Approx Ratio | Algorithm | Complexity |
|---------|-------------|-----------|------------|
| Vertex Cover | 2 | Maximal matching | O(V+E) |
| Weighted VC | 2 | LP rounding | O(V³) |
| TSP (△-ineq) | 2 | MST-based | O(V²) |
| TSP (△-ineq) | 3/2 | Christofides | O(V³) |
| General TSP | no constant | — | NP-hard |
| Set Cover | O(ln n) | Greedy | O(Σ|S|) |
| MAX-3-CNF-SAT | 8/7 | Random + derandomize | O(n+m) |
| Bin Packing | 2 (First-Fit) | 11/9 approx | O(n lg n) |
| Bin Packing | PTAS | Karmarkar-Karp | O(n^{1/ε}) |
| Max Cut | 1/2 | Random assignment | O(V+E) |
| Max Cut | 0.878 | Goemans-Williamson (SDP) | O(V³) |
| 0-1 Knapsack | FPTAS | Profit rounding | O(n³/ε) |
| Subset-Sum | FPTAS | Trimming | O(n³/ε) |
| Steiner Tree | 2 | MST in metric closure | O(V²) |

---

## Cross-Cutting Topics

### Design Paradigms & Meta-Methods

| Paradigm | Description | Examples |
|----------|------------|----------|
| Incremental | Build solution element by element | Insertion sort |
| Divide-and-Conquer | Split, solve recursively, combine | Merge sort, Strassen, FFT |
| Dynamic Programming | Overlapping subproblems, optimal substructure | Matrix-chain, LCS, OBST, Floyd-Warshall |
| Greedy | Local optimal choice | Activity selection, Huffman, Prim, Kruskal, Dijkstra |
| Amortized Analysis | Average worst-case over sequence | Dynamic tables, binary counters |
| Randomization | Random choices eliminate input dependence | RANDOMIZED-QUICKSORT, RANDOMIZED-SELECT, universal hashing |
| Augmentation | Extra info in standard DS | Order-statistic trees, interval trees |
| Relaxation | Iterative bound-tightening | Bellman-Ford, Dijkstra, Prim |
| Augmenting Paths | Iterative improvement along paths | Ford-Fulkerson, Hopcroft-Karp, Hungarian |
| Primal-Dual | Dual feasibility + complementary slackness | Hungarian, max-flow min-cut |
| Reweighting | Transform weights preserving structure | Johnson's algorithm |
| Reduction | Solve by transforming to known problem | Matching→Flow, Diff constraints→Shortest paths |

### Proof & Argument Patterns

| Pattern | Description | Used In |
|---------|------------|---------|
| Loop Invariant | Property holds before each iteration | Insertion sort, PARTITION, HEAPSORT, RB-INSERT-FIXUP |
| Induction | Base case + inductive step | Substitution method, RB height bound, DP correctness |
| Cut-and-Paste | Swap nonoptimal sub-solution for optimal | DP optimal substructure, MST cut property |
| Exchange Argument | Transform any optimal to include greedy choice | Activity selection, Huffman, offline caching |
| Decision Tree Model | Lower bound via permutation counting | Comparison sort Ω(n lg n) |
| Contradiction | Assume false, derive impossible | BFS correctness, Dijkstra correctness |
| Parenthesis Nesting | Interval containment (discovery-finish) | DFS properties |
| White-Path Theorem | DFS descendant characterization | SCC correctness |
| Duality | Equivalent optimization perspectives | Max-flow min-cut, LP duality, Hungarian |
| Potential Function | Energy-like measure for amortized analysis | Dynamic tables, disjoint-set forests |
| Path Relaxation | Edge relaxation in path order → correct distances | Bellman-Ford, Dijkstra, DAG-SP |
| Competitive Analysis | Online vs optimal offline | Paging, ski-rental, list accessing |
| Work-Span Analysis | Parallel algorithm performance | Graham-Brent scheduling |

### Probability & Statistics Foundation

- **Indicator random variables**: E[I{A}] = Pr{A}
- **Linearity of expectation**: E[Σ X_i] = Σ E[X_i] (always, even with dependence)
- **Geometric distribution**: Expected trials until success = 1/p
- **Binomial distribution**: Expected successes in n trials = np
- **Harmonic numbers**: H_n = ln n + γ + O(1/n), γ ≈ 0.577
- **Birthday paradox**: Π(1 - i/n) ≤ e^{-k(k-1)/(2n)}
- **Coupon collector**: Expected b·H_b ≈ b ln b trials
- **Chernoff bounds**: Concentration inequalities for sums of independent variables

### People & Dates

| Person | Contribution | Year |
|--------|------------|------|
| Al-Khowârizmî | Origin of "algorithm" | 9th century |
| C. A. R. Hoare | Quicksort, RANDOMIZED-SELECT | 1962 |
| J. W. J. Williams | Heapsort, priority queue | 1964 |
| R. W. Floyd | BUILD-MAX-HEAP, Floyd-Warshall | 1964 |
| V. Strassen | O(n^{2.81}) matrix multiplication | 1969 |
| Blum, Floyd, Pratt, Rivest, Tarjan | Worst-case linear selection | 1973 |
| C. E. Shannon | Information theory, minimax for decision trees | 1940s |
| D. Huffman | Huffman codes | 1952 |
| R. Bellman | Dynamic programming | 1955 |
| J. Kruskal | MST algorithm | 1956 |
| R. Prim | MST algorithm (also Jarník 1930) | 1957 |
| E. W. Dijkstra | Shortest paths, SCC algorithm | 1959 |
| L. Ford, D. Fulkerson | Max-flow min-cut theorem | 1956 |
| J. Edmonds, R. Karp | Edmonds-Karp algorithm | 1972 |
| R. E. Tarjan | Disjoint-set analysis, SCC, Fibonacci heaps | 1970s |
| R. Bayer, E. McCreight | B-trees | 1972 |
| L. Guibas, R. Sedgewick | Red-black trees | 1978 |
| J. Hopcroft, R. Karp | Bipartite matching (Hopcroft-Karp) | 1973 |
| D. Knuth | The Art of Computer Programming | 1968 |
| D. Gale, L. Shapley | Stable marriage problem | 1962 |
| H. Kuhn | Hungarian algorithm | 1955 |
| R. Rivest, A. Shamir, L. Adleman | RSA cryptography | 1977 |
| M. Rabin, G. Miller | Miller-Rabin primality test | 1976 |
| V. Cooley, J. Tukey | FFT algorithm | 1965 |
| L. Valiant | Theory of NP-completeness, #P | 1979 |
| S. Cook, L. Levin | NP-completeness theory | 1971 |
| R. Karp | 21 NP-complete problems | 1972 |
| J. von Neumann | Merge sort for EDVAC | 1945 |
| A. C. Li, X. Williams | Matrix multiplication O(n^{2.37287}) | 2012 |
| M. Agrawal, N. Kayal, N. Saxena | AKS primality test | 2002 |

---

## Exam Questions by Type

### MCQ

1. **Q:** What is the worst-case running time of quicksort on an already-sorted array using Lomuto partition?
   **A:** Θ(n²)

2. **Q:** Which of the following is NOT a stable sorting algorithm?
   **A:** Heapsort

3. **Q:** What is the running time of BUILD-MAX-HEAP on an array of n elements?
   **A:** O(n)

4. **Q:** What is the worst-case running time of any comparison sort for n elements?
   **A:** Ω(n lg n)

5. **Q:** In SELECT (worst-case linear selection), what group size is used?
   **A:** 5

6. **Q:** What is the maximum number of rotations during RB-INSERT-FIXUP?
   **A:** 2

7. **Q:** What is the load factor α in a hash table with n elements and m slots?
   **A:** α = n/m

8. **Q:** In a red-black tree, if a node is red, what must be true about its children?
   **A:** Both children must be black

9. **Q:** What is the expected number of probes in unsuccessful open-address search when α = 0.9?
   **A:** ≤ 10

10. **Q:** What is α(10¹⁰⁰) (inverse Ackermann)?
    **A:** 4

11. **Q:** In a disjoint-set forest with union by rank and path compression, what is the amortized time per operation?
    **A:** O(α(n))

12. **Q:** How many passes does Bellman-Ford make over all edges?
    **A:** |V|-1

13. **Q:** Which shortest-path algorithm works correctly with negative-weight edges but no negative cycles?
    **A:** Bellman-Ford

14. **Q:** The max-flow min-cut theorem states that:
    **A:** Maximum flow value = minimum cut capacity

15. **Q:** In DFS, what edge type is indicated when v is GRAY when (u,v) is first explored?
    **A:** Back edge

16. **Q:** Which is an asymptotically optimal comparison sort?
    **A:** Heapsort (or merge sort)

17. **Q:** What is the competitive ratio of LRU caching?
    **A:** k-competitive

18. **Q:** What is the recurrence for Floyd-Warshall?
    **A:** d^(k)_ij = min(d^(k-1)_ij, d^(k-1)_ik + d^(k-1)_kj)

19. **Q:** What property must a problem have for dynamic programming?
    **A:** Optimal substructure + overlapping subproblems

20. **Q:** What is the running time of KMP string matching?
    **A:** O(n+m)

21. **Q:** What is the inverse Ackermann function α(n) value for all practical n?
    **A:** ≤ 4

22. **Q:** Which algorithm solves the assignment problem in O(n³)?
    **A:** Hungarian algorithm

23. **Q:** What is the competitive ratio of optimal deterministic ski-rental?
    **A:** 2 - 1/B

24. **Q:** What property must hold for a problem to be solved by a greedy algorithm?
    **A:** Greedy-choice property + optimal substructure

25. **Q:** What is the height bound for a B-tree with minimum degree t and n nodes?
    **A:** h ≤ log_t((n+1)/2)

26. **Q:** How many rotations can RB-INSERT-FIXUP perform at most?
    **A:** 2

27. **Q:** How many rotations can RB-DELETE-FIXUP perform at most?
    **A:** 3

28. **Q:** What is the expected number of probes for successful search in open addressing at load factor α?
    **A:** (1/α) ln(1/(1-α))

29. **Q:** Which hash family is universal: h_{ab}(k) = ((ak+b) mod p) mod m?
    **A:** Yes, for p prime large

30. **Q:** What is the Miller-Rabin primality test's error bound after k tests?
    **A:** ≤ 4^{-k}

31. **Q:** In the Ford-Fulkerson method, what is the worst-case running time?
    **A:** O(E · |f*|) where |f*| is max flow value

32. **Q:** What does the Hopcroft-Karp algorithm compute?
    **A:** Maximum bipartite matching in O(√V·E)

33. **Q:** What is the running time of Kosaraju's SCC algorithm?
    **A:** Θ(V+E)

34. **Q:** What is the optimal substructure property?
    **A:** Optimal solution contains optimal solutions to subproblems

35. **Q:** What is the space complexity of Floyd-Warshall?
    **A:** Θ(V²)

36. **Q:** What is parallelism in the fork-join model?
    **A:** T₁/T_∞ (work over span)

37. **Q:** What is the first problem ever proven NP-complete?
    **A:** CIRCUIT-SAT (Cook-Levin, 1971)

38. **Q:** What type of tree must a Huffman encoding tree be?
    **A:** Full binary tree (every internal node has two children)

39. **Q:** What is the coupon collector's expected number of trials?
    **A:** b·H_b ≈ b ln b

40. **Q:** For the secretary problem, what is the optimal rejection fraction?
    **A:** 1/e ≈ 37%

### Short Answer

1. **Q:** State the five red-black tree properties.
   **Rubric:** (1) Each node red/black; (2) Root black; (3) Leaves (NIL) black; (4) Red's children black; (5) Equal black count on all paths.

2. **Q:** Show that any comparison sort requires Ω(n lg n) comparisons.
   **Rubric:** Decision tree model: n! ≤ leaves ≤ 2^h → h ≥ lg(n!) = Ω(n lg n) by Stirling.

3. **Q:** Why is counting sort able to beat the Ω(n lg n) lower bound?
   **Rubric:** It is not a comparison sort; uses array indices, not comparisons.

4. **Q:** State the four steps for augmenting a data structure.
   **Rubric:** (1) Choose underlying DS; (2) Determine additional info; (3) Verify maintainability; (4) Develop new operations.

5. **Q:** Explain the difference between Lomuto and Hoare partitioning.
   **Rubric:** Lomuto: A[r] pivot, single pass, returns pivot index. Hoare: A[p] pivot, two pointers from ends, returns j with p≤j<r. Hoare more efficient for equal elements.

6. **Q:** Why does deletion in open-addressed hash tables require special handling?
   **Rubric:** Emptying slot breaks probe sequences for keys that probed through it. Need DELETED marker or relocation algorithm.

7. **Q:** State the interval trichotomy.
   **Rubric:** For any two intervals: they overlap, one is left of the other, or one is right of the other.

8. **Q:** Compare Bellman-Ford and Dijkstra: when would you use each?
   **Rubric:** Bellman-Ford handles negative edges, detects cycles, O(VE). Dijkstra requires nonnegative, O(E lg V). Dijkstra faster when applicable.

9. **Q:** What is the purpose of the super-source in Johnson's algorithm?
   **Rubric:** Ensure all vertices reachable for Bellman-Ford to compute h(v). Reweighting ŵ(u,v) = w(u,v) + h(u) - h(v) makes all edges nonnegative.

10. **Q:** Define work, span, and parallelism in parallel algorithms.
    **Rubric:** T₁ = total operations; T_∞ = critical path length; parallelism = T₁/T_∞. Brent: T_P ≤ T₁/P + T_∞.

11. **Q:** What is the competitive ratio of an online algorithm?
    **Rubric:** C_ONLINE ≤ ρ · C_OPT (or + α). ρ = competitive ratio. E.g., LRU is k-competitive.

12. **Q:** State the Master Theorem cases.
    **Rubric:** For T(n) = aT(n/b) + f(n): (1) f = O(n^{log_b a - ε}) → Θ(n^{log_b a}); (2) f = Θ(n^{log_b a} lg^k n) → Θ(n^{log_b a} lg^{k+1} n); (3) f = Ω(n^{log_b a + ε}) AND af(n/b) ≤ cf(n) → Θ(f(n)).

13. **Q:** Explain the difference between DP and divide-and-conquer.
    **Rubric:** D&C partitions into disjoint subproblems (merge sort). DP has overlapping subproblems (Fibonacci). DP uses memoization or bottom-up table; D&C uses recursion only.

14. **Q:** Describe the cut property of MSTs.
    **Rubric:** For any cut (S, V-S) that respects A (no crossing edges in A), the lightest edge crossing the cut is safe for A. Proof via cut-and-paste: assume heavier edge in MST, swap → contradiction.

15. **Q:** How does the Edmonds-Karp algorithm differ from Ford-Fulkerson?
    **Rubric:** Ford-Fulkerson picks any augmenting path; Edmonds-Karp always uses BFS (shortest path in terms of edges). Result: O(VE²) polynomial bound vs O(E·|f*|) which can be exponential.

16. **Q:** Explain the three methods of amortized analysis.
    **Rubric:** Aggregate (same amortized cost for all ops, sum/n), Accounting (assign different costs, credit must stay nonnegative), Potential (Φ(D₀)=0, Φ(D_i)≥0, ĉ_i = c_i + Φ(D_i)-Φ(D_{i-1})).

17. **Q:** Why does SELECT use groups of 5 rather than 3?
    **Rubric:** Groups of 3 give T(n) ≤ T(n/3) + T(2n/3) + Θ(n) = O(n lg n) — not linear. Groups of 5 guarantee ≥ 3n/10 elements ≤ pivot → recursion on ≤ 7n/10 → T(n) = Θ(n).

18. **Q:** What is the significance of the regularity condition in Master Theorem Case 3?
    **Rubric:** af(n/b) ≤ cf(n) for some c<1 and large n ensures that work does not grow as we descend. Without it, case 3 fails (e.g., f(n) = n·(2-sin n) could be larger at subtrees than at root).

19. **Q:** Compare adjacency lists vs adjacency matrices for graph representation.
    **Rubric:** Lists: O(V+E) space, O(deg(v)) edge enumeration, O(V) edge query. Matrix: O(V²) space, O(1) edge query, O(V) enumeration. Lists better for sparse graphs; matrix for dense.

20. **Q:** Explain the difference between weak and strong duality in linear programming.
    **Rubric:** Weak duality: c^T x ≤ b^T y for any feasible primal (max) and dual (min). Strong duality: at optimality, c^T x* = b^T y*. Complementary slackness relates optimal primal/dual variables.

21. **Q:** What is the purpose of the π function in KMP?
    **Rubric:** π[q] = longest proper prefix of P that is suffix of P[1:q]. On mismatch at q+1, set q = π[q] to skip characters that are already known to match, avoiding backtracking in T.

22. **Q:** Describe the structure of a B-tree node.
    **Rubric:** Each node contains n keys (n+1 children pointers). Leaf: all children are NIL. Root: 1 ≤ n ≤ 2t-1. Internal: t-1 ≤ n ≤ 2t-1. All leaves at same depth.

### Trace / Apply

1. **Input:** A = [4,1,3,2,16,9,10,14,8,7], n=10. Apply BUILD-MAX-HEAP.
   **Expected:** i=5: no change; i=4: [4,1,3,14,16,9,10,2,8,7]; i=3: [4,1,10,14,16,9,3,2,8,7]; i=2: [4,16,10,14,7,9,3,2,8,1]; i=1: [16,14,10,8,7,9,3,2,4,1].

2. **Input:** Insert keys 41, 38, 31, 12, 19, 8 into empty RB tree. Show tree after each.
   **Expected:** Trace RB-INSERT-FIXUP cases at various steps; final valid RB tree.

3. **Input:** Graph s→a(3), s→b(5), a→b(2), b→c(1), a→c(6). Run Dijkstra from s.
   **Expected:** s.d=0, a.d=3, b.d=5, c.d=6.

4. **Input:** T(n) = 3T(n/4) + n lg n. Apply Master Theorem.
   **Expected:** a=3, b=4, n^{log₄3}=n^{0.793}, f(n)=n lg n = Ω(n^{0.793+ε}), check regularity → Case 3 → Θ(n lg n).

5. **Input:** Sequence of numbers for COUNTING-SORT: A=[2,5,3,0,2,3,0,3], k=5.
   **Expected:** C after counts [2,0,2,3,0,1]; after running sums [2,2,4,7,7,8]; final B=[0,0,2,2,3,3,3,5].

6. **Input:** Ford-Fulkerson on simple graph with capacities s→a(10), s→b(10), a→t(5), a→b(15), b→t(10). Find max flow.
   **Expected:** Max flow = 15 (saturate a→t=5, s→b→t=10, s→a→b=5).

7. **Input:** Insertion sort on A=[5,2,4,6,1,3]. Show array after each iteration.
   **Expected:** i=2: [2,5,4,6,1,3]; i=3: [2,4,5,6,1,3]; i=4: [2,4,5,6,1,3]; i=5: [1,2,4,5,6,3]; i=6: [1,2,3,4,5,6].

8. **Input:** A = [3,7,2,6,5,1,4] with Lomuto PARTITION (p=1, r=7). Show regions after each step.
   **Expected:** Pivot=4. After j=1: [3,7,2,6,5,1,4] i=1; j=2: [3,7,2,6,5,1,4] i=1; j=3: [3,2,7,6,5,1,4] i=2; j=4: [3,2,7,6,5,1,4] i=2; j=5: [3,2,7,6,5,1,4] i=2; j=6: [3,2,1,6,5,7,4] i=3. Final swap: [3,2,1,4,5,7,6]. Return q=4.

9. **Input:** T(n) = 2T(⌊n/2⌋) + n lg n. Solve the recurrence.
   **Expected:** Master Theorem Case 2 with k=1: a=2, b=2, n^{log₂2}=n¹, f(n)=n lg n = Θ(n lg n). Solution: T(n) = Θ(n lg² n).

10. **Input:** AVL tree insertion: keys 10, 20, 30, 40, 50, 25. Show rotations.
    **Expected:** 
    10→20→30: left rotation at 10, root=20. 
    20(10)(30)→40: no rotation.
    20(10)(30(·)(40))→50: left rotation at 30.
    20(10)(40(30)(50))→25.
    25 makes 40 unbalanced: RL rotation at 40. 
    Final: 30(20(10)(25))(40(·)(50)).

11. **Input:** Run Floyd-Warshall on 4-vertex graph with adjacency matrix M where M[i,j] = weight. Compute D⁰, D¹, D², D³, D⁴.
    **Expected:** D⁰ = input; D¹[i,j] = min(D⁰[i,j], D⁰[i,1]+D⁰[1,j]); ... D⁴ = all-pairs shortest paths.

12. **Input:** Kruskal's algorithm on graph with edges: (a,b,1), (b,c,2), (a,c,3), (c,d,4), (b,d,5).
    **Expected:** Sort: (a,b,1), (b,c,2), (a,c,3), (c,d,4), (b,d,5). Add (a,b), (b,c), skip (a,c) (cycle), add (c,d), skip (b,d) (cycle). MST weight = 7.

### Essay / Long-Form

1. **Q:** Compare and contrast quicksort, heapsort, and merge sort.
   **Key points:** Asymptotic (quicksort Θ(n²) worst, O(n lg n) expected; others O(n lg n) worst). In-place (heapsort/quicksort yes, mergesort no). Stability (mergesort yes, others no). Constants (quicksort smallest, heapsort moderate, mergesort highest). Practical: quicksort fastest, heapsort for worst-case guarantees, mergesort for stability.

2. **Q:** Prove that the expected running time of RANDOMIZED-QUICKSORT is O(n lg n).
   **Key points:** Lemma 7.1 (time = O(n+X), X = comparisons). Lemma 7.2 (z_i compares z_j iff first pivot from Z_ij). Lemma 7.3 (Pr = 2/(j-i+1)). E[X] = Σ Σ 2/(j-i+1) = O(n lg n). Expected time = O(n + n lg n) = O(n lg n).

3. **Q:** Explain how SELECT achieves worst-case linear time.
   **Key points:** Groups of 5 ensure pivot ≥ 3g/2 elements and ≤ 3g/2. Recursive subproblem ≤ 7n/10. Recurrence T(n) ≤ T(n/5) + T(7n/10) + Θ(n) → T(n) = Θ(n) by substitution. Groups of 3 give O(n lg n). Theoretical interest only — RANDOMIZED-SELECT more practical.

4. **Q:** Prove the max-flow min-cut theorem.
   **Key points:** (1)⇒(2): augmenting path would increase flow, contradicting maximality. (2)⇒(3): S = vertices reachable from s in G_f; edges S→T saturated, edges T→S have 0 flow → |f| = c(S,T). (3)⇒(1): Corollary 24.5 states |f| ≤ c(S,T) for any cut, so |f| = c(S,T) is maximum.

5. **Q:** Prove that a red-black tree with n nodes has height at most 2 lg(n+1).
   **Key points:** Inductive claim: subtree at x has ≥ 2^{bh(x)} - 1 internal nodes. Property 4: at least half nodes on path are black → bh(root) ≥ h/2. Therefore n ≥ 2^{h/2} - 1 → h ≤ 2 lg(n+1).

6. **Q:** Analyze the expected performance of hashing with chaining.
   **Key points:** Load factor α = n/m. Unsuccessful search: expected length of chain = α, time Θ(1+α). Successful search: expected elements before searched element = (α/2 - α/(2n)), time Θ(1+α). Universal hashing guarantees O(1+α) for any input.

7. **Q:** Compare and contrast Kruskal's and Prim's MST algorithms.
   **Key points:** Kruskal (edge-based, sort then union-find, O(E lg V), builds forest). Prim (vertex-based, priority queue, O(E lg V) binary, O(V²) dense, grows single tree). Both rely on cut property. Kruskal better for sparse, Prim for dense with array.

8. **Q:** Describe the four single-source shortest-path algorithms and when to use each.
   **Key points:** BFS (unweighted, O(V+E)). DAG-SP (DAG only, negative OK, Θ(V+E), topological sort). Dijkstra (nonnegative, O(E lg V)). Bellman-Ford (negative OK, detects cycles, O(VE)). Dijkstra for most cases with nonnegative weights; Bellman-Ford when negative edges present.

9. **Q:** Explain the relationship between P, NP, NP-complete, and NP-hard. Give examples.
   **Key points:** P = polynomial-time decidable (shortest path, MST). NP = polynomial-time verifiable (SAT, TSP, CLIQUE). NPC = NP ∩ NP-hard (SAT, 3-CNF, CLIQUE, VERTEX-COVER, HAM-CYCLE, TSP, SUBSET-SUM). If any NPC ∈ P, then P = NP. NP-hard includes unconstrained optimization (TSP optimization).

10. **Q:** Compare DP vs greedy algorithms with examples of where each works.
    **Key points:** DP: optimal substructure + overlapping subproblems (matrix-chain, LCS, OBST). Greedy: greedy-choice property + optimal substructure (activity selection, Huffman, MST). Key difference: DP explores all subproblem solutions; greedy commits to one choice. 0-1 knapsack needs DP; fractional knapsack works with greedy.

11. **Q:** Explain the analysis of disjoint-set forests with union by rank and path compression.
    **Key points:** Union by rank ensures tree height ≤ lg n. Path compression flattens trees during FIND-SET. Together achieve O(m α(n)) for m operations. Inverse Ackermann α(n) ≤ 4 for all practical n (≤ 10⁸⁰). Tarjan proved tight bound via potential function with level(x) and iter(x).

12. **Q:** Describe the Ford-Fulkerson method and prove the max-flow min-cut theorem.
    **Key points:** Augment along paths in residual network until none exist. Max-flow min-cut: three equivalent conditions (max flow, no augmenting path, flow = cut capacity). Corollary: integrality theorem for integer capacities. Applications to bipartite matching and edge-disjoint paths.

13. **Q:** Explain how BFS computes shortest paths in unweighted graphs and prove its correctness.
    **Key points:** Queue ensures processing by distance layers. Invariants: (1) v.d ≥ δ(s,v) always; (2) queue contains vertices with d values differing by at most 1; (3) BFS tree gives shortest paths. Theorem 20.5: v.d = δ(s,v) for all reachable v. Proof by induction on distance.

14. **Q:** Discuss the P vs NP problem and its implications for algorithm design.
    **Key points:** P = polynomial-time solvable; NP = polynomial-time verifiable. NP-complete hardest in NP. P ≠ NP means no polynomial algorithm for TSP, SAT, etc. Implication: approximation algorithms, heuristics, and exponential algorithms for small instances. Oracle separation results and circuit complexity lower bounds.

15. **Q:** Analyze the expected running time of RANDOMIZED-SELECT.
    **Key points:** Indicator variables for comparisons. Partition step O(n). Expected size reduction: with probability 1/2, pivot falls in middle 50% → subproblem ≤ 3n/4. E[T(n)] ≤ T(3n/4) + O(n) → E[T(n)] = Θ(n). Formal analysis via recurrence with indicator for pivot rank.

16. **Q:** Compare and contrast open addressing and chaining for hash tables.
    **Key points:** Chaining: α can exceed 1, easy deletion, pointer overhead. Open addressing: α < 1 required, deletion hard (DELETED marker), better cache performance. Expected probes: chain search Θ(1+α), open addr unsuccessful ≤ 1/(1-α). Open addressing preferred for in-memory tables with known n.

17. **Q:** Explain the competitive analysis framework with examples from caching and ski-rental.
    **Key points:** Competitive ratio ρ: C_ONLINE ≤ ρ·C_OPT + α. Ski-rental: rent B-1 days then buy → 2-1/B competitive (optimal deterministic). Paging: LRU, FIFO, Marking are k-competitive (k = cache size); no deterministic can beat k. Randomization helps: Marking is O(lg k)-competitive; Ω(lg k) lower bound.

18. **Q:** Derive and explain the Master Theorem for solving recurrences.
    **Key points:** For T(n) = aT(n/b) + f(n): compare f(n) to n^{log_b a}. Three cases: (1) leaves dominate: f = O(n^{log_b a - ε}) → T = Θ(n^{log_b a}); (2) tied: f = Θ(n^{log_b a} lg^k n) → T = Θ(n^{log_b a} lg^{k+1} n); (3) root dominates: f = Ω(n^{log_b a + ε}) AND regularity af(n/b) ≤ cf(n) → T = Θ(f(n)). Intuition from recursion tree: cost at root vs leaves.

19. **Q:** Analyze Strassen's matrix multiplication algorithm and its place in the evolution of matrix multiplication.
    **Key points:** Classic: 8 multiplications, T(n) = 8T(n/2) + Θ(n²) = Θ(n³). Strassen: 7 multiplications, T(n) = 7T(n/2) + Θ(n²) = Θ(n^{lg 7}) ≈ Θ(n^{2.81}). Improvement via 10 S₁…S₁₀ matrices. Coppersmith-Winograd: O(n^{2.376}). Alman-Williams: O(n^{2.37287}). Practical: Strassen used for large n; naive better for small.

20. **Q:** Explain the relationship between maximum flow, minimum cut, and bipartite matching.
    **Key points:** Max-flow min-cut: flow value = min cut capacity. Bipartite matching reduces to flow: source→L(1), L→R(1), R→sink(1). Integrality ensures integer matching. Hall's theorem as consequence: perfect matching exists iff |A| ≤ |N(A)| for all A⊆L. Hopcroft-Karp faster for matching O(√V·E) vs flow O(VE²).

---

## Reference Appendices

### Appendix A — Recurrence Master Table

| Recurrence | Algorithm | Solution |
|-----------|-----------|----------|
| T(n) = 2T(n/2) + Θ(n) | Merge sort | Θ(n lg n) |
| T(n) = T(n-1) + Θ(n) | Quicksort worst-case | Θ(n²) |
| T(n) = 2T(n/2) + Θ(1) | Binary search | Θ(lg n) |
| T(n) = 8T(n/2) + Θ(1) | Recursive mat mult | Θ(n³) |
| T(n) = 7T(n/2) + Θ(n²) | Strassen | Θ(n^{lg 7}) |
| T(n) = 9T(n/3) + Θ(n) | Example | Θ(n²) |
| T(n) = T(2n/3) + Θ(1) | MAX-HEAPIFY | Θ(lg n) |
| T(n) ≤ T(n/5) + T(7n/10) + Θ(n) | SELECT | Θ(n) |
| T(n) = 2T(n/2) + n lg n | Quicksort tied | Θ(n lg² n) |
| T(n) = 3T(n/4) + n lg n | Example | Θ(n lg n) |
| T(n) = T(n/3) + T(2n/3) + Θ(n) | Unbalanced D&C | Θ(n lg n) |
| T(n) = 4T(n/2) + Θ(n) | Example | Θ(n²) |
| T(n) = 2T(n/2) + Θ(1) | Binary search | Θ(lg n) |
| T(n) = T(n/4) + T(2n/4) + T(3n/4) + Θ(n) | Example | Θ(n lg n) |
| T(n) = 2T(n-1) + 1 | Towers of Hanoi | Θ(2ⁿ) |
| T(n) = aT(n-b) + f(n) | Decrease-and-conquer | depends on a,b |
| T(n) = 2T(√n) + lg n | Variable substitution | Θ(lg n · lg lg n) |
| T(n) = T(n²) + O(n) | Nonexistent | Must check: n² > n → T undefined |
| T(n) = 1T(n-1) + 1 | Ackermann initialization | Θ(n) |

### Appendix B — Asymptotic Notation Cheat Sheet

| Notation | Formal Definition | Intuition | Limit Test |
|----------|-------------------|-----------|------------|
| f = Θ(g) | 0 ≤ c₁g(n) ≤ f(n) ≤ c₂g(n) for n ≥ n₀ | f ≈ g (tight bound) | lim f/g = c > 0 |
| f = O(g) | 0 ≤ f(n) ≤ cg(n) for n ≥ n₀ | f ≤ g (upper bound) | lim sup f/g < ∞ |
| f = Ω(g) | 0 ≤ cg(n) ≤ f(n) for n ≥ n₀ | f ≥ g (lower bound) | lim inf f/g > 0 |
| f = o(g) | ∀c>0 ∃n₀: 0 ≤ f(n) < cg(n) for n ≥ n₀ | f < g (not tight) | lim f/g = 0 |
| f = ω(g) | ∀c>0 ∃n₀: 0 ≤ cg(n) < f(n) for n ≥ n₀ | f > g (not tight) | lim f/g = ∞ |

**Common pitfalls**:
- O(n²) = Θ(n²) is FALSE: O is upper bound, Θ is tight bound. 2n = O(n²) but 2n ≠ Θ(n²).
- Using Θ for worst-case time is wrong if best and worst differ: insertion sort worst Θ(n²), best Θ(n), overall not Θ(n²).
- Asymptotic notation in equations: 2n² + 3n + 1 = 2n² + Θ(n) means ∃ f(n) ∈ Θ(n) such that 2n² + 3n + 1 = 2n² + f(n).
- **Sums**: If Σ f(k) = Θ(Σ g(k)), combine carefully; the "hidden" constant must work for all terms.

**Growth hierarchy** (each dominates previous):
- O(1) ⊂ O(lg n) ⊂ O(√n) ⊂ O(n) ⊂ O(n lg n) ⊂ O(n√n) ⊂ O(n²) ⊂ O(n³) ⊂ O(2ⁿ) ⊂ O(n!)

**Functions with multiple variables**:
- f(m,n) = O(g(m,n)) if ∃ c,m₀,n₀: f(m,n) ≤ c·g(m,n) for all m≥m₀, n≥n₀
- Careful with ordering: O(m+n) ≠ O(max(m,n)) in general (though often same). For graphs: O(V+E) is standard.

**Limit-based comparison rules**:
- f = o(g) ⇔ lim_{n→∞} f(n)/g(n) = 0
- f = Θ(g) ⇔ 0 < lim_{n→∞} f(n)/g(n) < ∞ (limit exists)
- f = ω(g) ⇔ lim_{n→∞} f(n)/g(n) = ∞
- L'Hôpital: if f,g → ∞, lim f/g = lim f′/g′ (when limit exists)

### Appendix C — Common Graph Algorithm Complexities

| Algorithm | Time | Space | Notes |
|-----------|------|-------|-------|
| BFS | O(V+E) | O(V) | Unweighted shortest paths |
| DFS | O(V+E) | O(V) | Edge classification, topological order |
| Topological sort (DFS) | Θ(V+E) | O(V) | DAG only |
| Topological sort (Kahn) | Θ(V+E) | O(V) | In-degree removal |
| SCC (Kosaraju) | Θ(V+E) | O(V) | Two DFS passes |
| SCC (Tarjan) | Θ(V+E) | O(V) | Single pass, lowlinks |
| MST (Kruskal) | O(E lg V) | O(V) | Sort + union-find |
| MST (Prim binary heap) | O(E lg V) | O(V) | DECREASE-KEY × E |
| MST (Prim Fibonacci) | O(E + V lg V) | O(V) | Faster for dense |
| MST (Prim array) | O(V²) | O(V) | Best for dense graphs |
| Bellman-Ford | O(VE) | O(V) | Negative edges OK |
| BFS for unweighted SP | O(V+E) | O(V) | Unweighted |
| DAG Shortest Paths | Θ(V+E) | O(V) | Topological sort + relax |
| Dijkstra (binary heap) | O(E lg V) | O(V) | Nonnegative only |
| Dijkstra (Fibonacci) | O(V lg V + E) | O(V) | Theoretical best |
| Dijkstra (array) | O(V²) | O(V) | For dense graphs |
| Floyd-Warshall | Θ(V³) | Θ(V²) | Dense, all-pairs |
| Johnson | O(V² lg V + VE) | O(V²) | Sparse, negative edges OK |
| FASTER-APSP (squaring) | Θ(V³ lg V) | Θ(V²) | min-plus matrix mult |
| Transitive closure (boolean FW) | Θ(V³) | Θ(V²) | Boolean matrix |
| Ford-Fulkerson | O(E·|f*|) | O(V+E) | Pseudopolynomial |
| Edmonds-Karp | O(VE²) | O(V+E) | BFS augmenting paths |
| Push-relabel (generic) | O(V²E) | O(V+E) | Local operations |
| Push-relabel (FIFO) | O(V³) | O(V+E) | Practical |
| Dinic | O(V²E) | O(V+E) | Layered networks |
| Capacity scaling | O(E² lg C) | O(V+E) | C = max capacity |
| Hopcroft-Karp | O(√V·E) | O(V+E) | Bipartite matching |
| Gale-Shapley | O(n²) | O(n²) | Stable marriage |
| Hungarian | O(n³) | O(n²) | Assignment problem |
| Maximum bipartite matching (flow) | O(VE) | O(V+E) | Via Dinic on unit cap |

### Appendix D — Data Structure Operation Complexities

| Structure | SEARCH | INSERT | DELETE | MIN/MAX | SUCCESSOR | EXTRACT-MIN | DECREASE-KEY |
|-----------|--------|--------|--------|---------|-----------|-------------|--------------|
| Sorted array | O(lg n) | O(n) | O(n) | O(1) | O(1) | O(1) | O(n) |
| Unsorted array | O(n) | O(1) | O(n) | O(n) | O(n) | O(n) | O(1) |
| Singly linked list | O(n) | O(1) | O(n)† | O(n) | O(n) | O(n) | O(1)†† |
| Doubly linked list | O(n) | O(1) | O(1)† | O(n) | O(n) | O(n) | O(1)†† |
| Stack (array) | O(n) | O(1) | O(1) | O(n) | O(n) | O(1) | — |
| Queue (array) | O(n) | O(1) | O(1) | O(1) | O(n) | O(1) | — |
| BST (unbalanced) | O(h) | O(h) | O(h) | O(h) | O(h) | O(h) | O(h) |
| BST (balanced/AVL) | O(lg n) | O(lg n) | O(lg n) | O(lg n) | O(lg n) | O(lg n) | O(lg n) |
| RB tree | O(lg n) | O(lg n) | O(lg n) | O(lg n) | O(lg n) | O(lg n) | O(lg n) |
| B-tree (min deg t) | O(log_t n) | O(log_t n) | O(log_t n) | O(log_t n) | O(log_t n) | O(log_t n) | O(log_t n) |
| Hash (chaining, α=n/m) | O(1+α) avg | O(1) | O(1)† | O(n) | O(n) | O(n) | O(1)†† |
| Hash (open addr) | O(1/(1-α)) avg | — | O(1) marked | O(n) | O(n) | — | — |
| Binary heap (min) | O(n) | O(lg n) | O(lg n)††† | O(1) | O(n) | O(lg n) | O(lg n) |
| d-ary heap (min) | O(n) | O(log_d n) | O(log_d n) | O(1) | O(n) | O(d log_d n) | O(log_d n) |
| Fibonacci heap (min) | O(n) | O(1) | O(lg n)††† | O(1) | O(n) | O(lg n) amort | O(1) amort |
| Disjoint-set (forest) | — | O(1)• | — | — | — | — | — |
| van Emde Boas tree | O(lg lg u) | O(lg lg u) | O(lg lg u) | O(1) | O(lg lg u) | O(lg lg u) | — |

† With pointer to element. †† With pointer, key known. ††† With pointer and heap-decrease-key.
• MAKE-SET is O(1). FIND-SET and UNION are O(α(n)) amortized with both heuristics.

**Note on hash table deletions**: Open addressing requires DELETED marker (slows search). Chaining deletion is O(1) with doubly linked list.

### Appendix E — Sorting Algorithm Properties

| Algorithm | Worst | Avg | Best | Space | Stable | In-place | Comparisons | Method |
|-----------|------|-----|------|-------|--------|----------|-------------|--------|
| Insertion | Θ(n²) | Θ(n²) | Θ(n) | O(1) | Yes | Yes | Θ(n²) worst | Incremental |
| Selection | Θ(n²) | Θ(n²) | Θ(n²) | O(1) | No | Yes | Θ(n²) all | Selection |
| Bubble | Θ(n²) | Θ(n²) | Θ(n) | O(1) | Yes | Yes | Θ(n²) worst | Exchange |
| Merge | Θ(n lg n) | Θ(n lg n) | Θ(n lg n) | O(n) | Yes | No | Θ(n lg n) | D&C |
| Heapsort | O(n lg n) | O(n lg n) | Ω(n lg n) | O(1) | No | Yes | O(n lg n) | Selection |
| Quicksort | Θ(n²) | Θ(n lg n) | Θ(n lg n) | O(lg n)* | No | Yes | Θ(n lg n) avg | D&C |
| Introspective | O(n lg n) | O(n lg n) | O(n lg n) | O(lg n) | No | Yes | O(n lg n) | Hybrid |
| Shell | O(n²) | O(n^{3/2}) | O(n lg n) | O(1) | No | Yes | varies | Incremental |
| Timsort | O(n lg n) | O(n lg n) | O(n) | O(n) | Yes | No | O(n lg n) | Hybrid |
| Counting | Θ(n+k) | Θ(n+k) | Θ(n+k) | O(k) | Yes | No | 0 (non-comp) | Non-comparison |
| Radix (LSD) | Θ(d(n+k)) | Θ(d(n+k)) | Θ(d(n+k)) | O(n+k) | Yes | No | 0 | Non-comparison |
| Bucket | Θ(n²) | Θ(n) | Θ(n) | O(n) | Yes | No | 0 (expected) | Distribution |

*Quicksort stack depth O(lg n) with tail-recursion elimination; O(n) without.
- **Stable sort guarantees**: When equal keys maintain original relative order.
- **Adaptive**: Insertion, Bubble, Timsort are adaptive (near Θ(n) for nearly sorted).
- **Internal vs external**: Merge sort used for external sorting (tape drives).

### Appendix F — Important Graph Properties

| Property | Statement | Application |
|----------|-----------|-------------|
| Handshaking Lemma | Σ deg(v) = 2\|E\| | Graph invariants |
| Euler's formula (planar) | V - E + F = 2 | Planar graph bounds |
| Graph connectivity | κ(G) ≤ λ(G) ≤ δ(G) | Vertex/edge connectivity |
| Turán's theorem | max edges in K_{r+1}-free graph: (1-1/r)·n²/2 | Extremal graph theory |
| Mantel's theorem | Triangle-free graph has ≤ n²/4 edges | Special case of Turán |
| Triangle inequality | δ(s,v) ≤ δ(s,u) + w(u,v) | Shortest paths |
| Directed graph DAG | If G is a DAG ⟹ ∃ topological ordering | Scheduling, dependencies |
| Undirected DFS | Only tree and back edges | Edge classification |
| Directed DFS | 4 edge types (tree, back, forward, cross) | Cycle detection |
| Cut property | Lightest edge across cut respecting A is safe | MST |
| Cycle property | Heaviest edge on any cycle is in no MST | MST |
| Max-flow min-cut | Max flow = min cut capacity | Network flow |
| Hall's theorem | Perfect matching iff \|A\| ≤ \|N(A)\| ∀ A ⊆ L | Bipartite matching |
| König's theorem | In bipartite: max matching = min vertex cover | Equivalence |
| Berge's lemma | M maximum ⟺ no M-augmenting path | Matching |
| Dilworth's theorem | In poset: max antichain size = min chain decomposition | Partial orders |
| Brooks' theorem | χ(G) ≤ Δ(G) (except cliques/odd cycles) | Graph coloring |
| Vizing's theorem | Δ(G) ≤ χ'(G) ≤ Δ(G)+1 | Edge coloring |

### Appendix G — Key Mathematical Formulas

**Series & Summations**:
- **Arithmetic series**: Σ_{i=1}^{n} i = n(n+1)/2
- **Sum of squares**: Σ_{i=1}^{n} i² = n(n+1)(2n+1)/6
- **Sum of cubes**: Σ_{i=1}^{n} i³ = n²(n+1)²/4
- **Geometric series**: Σ_{i=0}^{n} c^i = (c^{n+1} - 1)/(c-1) for c ≠ 1
- **Infinite geometric (c<1)**: Σ_{i=0}^{∞} c^i = 1/(1-c)
- **Arithmetic-geometric**: Σ_{i=1}^{n} i·c^i = (c - (n+1)c^{n+1} + nc^{n+2})/(1-c)²
- **Sum of i·2^i**: Σ_{i=1}^{n} i·2^i = (n-1)2^{n+1} + 2
- **Sum of 2^i**: Σ_{i=0}^{n} 2^i = 2^{n+1} - 1
- **Harmonic numbers**: H_n = Σ_{i=1}^{n} 1/i = ln n + γ + O(1/n), γ ≈ 0.57721
- **Negative powers**: Σ_{i=1}^{∞} 1/i² = π²/6

**Logarithms**:
- **Binary**: lg n = log₂ n
- **Natural**: ln n = log_e n
- **Change of base**: log_a n = log_b n / log_b a = Θ(log n)
- **Iterated log**: lg* n = min{i ≥ 0: lg^(i) n ≤ 1}
- **Properties**: log(ab) = log a + log b; log(a^b) = b·log a; a^{log_b c} = c^{log_b a}

**Combinatorics**:
- **Binomial coefficient**: C(n,k) = n!/(k!(n-k)!) = C(n, n-k)
- **Stirling's approximation**: n! = √(2πn)(n/e)^n(1 + Θ(1/n))
- **Catalan numbers**: C_n = (1/(n+1))·C(2n, n) = Ω(4^n/n^{3/2})
- **Binomial theorem**: (x+y)^n = Σ_{k=0}^{n} C(n,k)·x^k·y^{n-k}
- **Pascal's identity**: C(n,k) = C(n-1,k-1) + C(n-1,k)
- **Vandermonde**: C(m+n,r) = Σ_{k=0}^{r} C(m,k)·C(n,r-k)
- **Stars and bars**: C(n+k-1, k-1) ways to place n identical items into k bins

**Number Theory**:
- **Fibonacci**: F_i = (ϕ^i - ϕ̂^i)/√5, F_0=0, F_1=1
- **Golden ratio**: ϕ = (1+√5)/2 ≈ 1.61803, ϕ̂ = (1-√5)/2 ≈ -0.618
- **gcd properties**: gcd(a,b) = gcd(b, a mod b); gcd(ka,kb) = k·gcd(a,b)
- **lcm**: lcm(a,b) = ab/gcd(a,b)
- **Euler's totient**: φ(n) = n·Π_{p|n}(1-1/p)
- **Fermat's theorem**: a^{p-1} ≡ 1 (mod p) for prime p ∤ a
- **Euler's theorem**: a^{φ(n)} ≡ 1 (mod n) for gcd(a,n)=1
- **Chinese Remainder**: x ≡ a_i (mod n_i), n_i coprime → unique x mod Π n_i

**Probability**:
- **Union bound**: Pr[∪ A_i] ≤ Σ Pr[A_i]
- **Conditional**: Pr[A|B] = Pr[A∩B]/Pr[B]
- **Bayes**: Pr[A|B] = Pr[B|A]·Pr[A]/Pr[B]
- **Expectation**: E[X] = Σ x·Pr[X=x]; E[g(X)] = Σ g(x)·Pr[X=x]
- **Linearity**: E[Σ X_i] = Σ E[X_i] (no independence)
- **Variance**: Var[X] = E[(X-μ)²] = E[X²] - (E[X])²
- **Covariance**: Cov[X,Y] = E[XY] - E[X]E[Y]
- **Markov**: Pr[X ≥ t] ≤ E[X]/t for X ≥ 0
- **Chebyshev**: Pr[|X-μ| ≥ kσ] ≤ 1/k²
- **Chernoff bound**: Pr[X ≤ (1-δ)μ] ≤ e^{-μδ²/2} for δ∈[0,1]; Pr[X ≥ (1+δ)μ] ≤ e^{-μδ²/3}
- **Birthday**: Pr[no collision] ≈ e^{-k(k-1)/(2n)}; threshold: k ≈ √(2n·ln 2)
- **Coupon collector**: Expected b·H_b ≈ b·ln b trials to collect all b coupons

**Inequalities & Bounds**:
- **Cauchy-Schwarz**: (Σ a_i b_i)² ≤ (Σ a_i²)(Σ b_i²)
- **Jensen**: f(E[X]) ≤ E[f(X)] for convex f
- **Boole (union bound)**: Pr[∪ A_i] ≤ Σ Pr[A_i]
- **Floor/ceil**: x-1 < ⌊x⌋ ≤ x ≤ ⌈x⌉ < x+1; ⌊x/2⌋ + ⌈x/2⌉ = x
- **Sum integral**: ∫_{0}^{n} f(x)dx ≤ Σ_{i=1}^{n} f(i) ≤ ∫_{1}^{n+1} f(x)dx for monotone f
- **Bernoulli inequality**: (1+x)^n ≥ 1+nx for x ≥ -1, n ≥ 0
- **AM ≥ GM**: (Σ a_i)/n ≥ (Π a_i)^{1/n} for nonnegative a_i

**Asymptotic Bounds** (for algorithm analysis):
- lg(n!) = n lg n - n lg e + O(lg n) = Θ(n lg n)
- H_n = ln n + γ + O(1/n)
- Σ_{i=1}^{n} 1/i = ln n + γ + ε_n where ε_n → 0
- Σ_{i=1}^{n} i^p = Θ(n^{p+1}) for p > -1
- Σ_{i=1}^{n} 1/i^p = Θ(1) for p > 1; = Θ(lg n) for p = 1; = Θ(n^{1-p}) for p < 1

### Appendix G — Pseudocode Conventions

- **Indentation**: Block structure
- **//**: Comment
- **=**: Assignment (not equality)
- **==**: Equality test
- **A[i]**: Array element
- **A[i:j]**: Subarray from i to j inclusive
- **.**: Attribute access (node.key)
- **NIL**: Null pointer
- **∞**: Infinity (sufficiently large)
- **by reference**: Arrays and objects passed by reference
- **by value**: Simple types passed by value
- **global variables**: Typically avoided; return values preferred
- **RANDOM(a, b)**: Returns integer in [a, b] uniformly
- **return**: Returns to caller, may return multiple values

---

*End of Study Guide — Lines: ~5000*
