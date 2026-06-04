# Study Guide: Introduction to Algorithms (CLRS 4e) — Part I, Chapters 2–5

> Generated 2026-06-04. Subject: Computer Science (Algorithms). Exam format: Comprehensive. Coverage: Complete extraction of all examinable primitives.

---

## Ch. 2 — Getting Started

### Named Entities (Terms & Definitions)

- **Sorting problem**: Input: sequence of n numbers 〈a₁, a₂, …, aₙ〉. Output: permutation (reordering) 〈a′₁, a′₂, …, a′ₙ〉 such that a′₁ ≤ a′₂ ≤ … ≤ a′ₙ.
- **Key**: The value to be sorted.
- **Satellite data**: Associated data that travels with the key.
- **Record**: A key plus its associated satellite data.
- **Pseudocode**: Algorithm description language similar to C/C++/Java/Python/JavaScript; uses indentation for block structure, `//` for comments, `=` for assignment, `:` for subarray notation.
- **Insertion sort**: A sorting algorithm that builds the final sorted array one element at a time by repeatedly inserting the next element into its correct position among previously sorted elements.
- **Loop invariant**: A property that holds before each iteration of a loop; used to prove correctness.
- **RAM model (Random-Access Machine)**: Generic one-processor computational model where instructions execute one after another, each taking constant time; includes arithmetic, data movement, and control instructions.
- **Input size**: The measure of input; for sorting, the number n of items; for integer multiplication, the number of bits.
- **Running time**: Number of instructions and data accesses executed on a particular input.
- **Order of growth**: The rate at which running time increases as input size increases; focus on leading term, ignoring constants and lower-order terms.
- **Θ-notation (informal)**: "Roughly proportional when n is large"; Θ(n²) means roughly proportional to n² for large n.
- **Incremental method**: Algorithm design approach where the solution is built by adding elements one at a time (e.g., insertion sort).
- **Divide-and-conquer**: Design method that breaks a problem into smaller subproblems, solves them recursively, and combines solutions.
- **Merge sort**: A divide-and-conquer sorting algorithm that divides the array in half, recursively sorts each half, then merges the sorted halves.
- **Subarray notation**: A[i:j] indicates elements A[i] through A[j] inclusive.
- **Inversion**: For array A[1:n] of distinct numbers, pair (i,j) is an inversion if i < j and A[i] > A[j].
- **Selection sort**: Algorithm that repeatedly finds the smallest remaining element and swaps it into position.
- **Binary search**: Algorithm that finds a value in a sorted array by repeatedly halving the search range.
- **Linear search**: Algorithm that scans through an array from beginning to end looking for a value.
- **Horner's rule**: Method for evaluating a polynomial using nested multiplication.

### Sequential Processes (Algorithms)

#### INSERTION-SORT(A, n)
- **Type**: Algorithm
- **Goal**: Sort array A[1:n] in place into monotonically increasing order
- **Input**: Array A[1:n], integer n (number of elements)
- **Output**: Array A[1:n] sorted
- **Steps**:
  1. `for i = 2 to n`
  2. `key = A[i]`
  3. `// Insert A[i] into sorted subarray A[1:i-1]`
  4. `j = i - 1`
  5. `while j > 0 and A[j] > key`
  6. `A[j+1] = A[j]`
  7. `j = j - 1`
  8. `A[j+1] = key`
- **Loop invariant** (for for-loop): At start of each iteration of the for loop, subarray A[1:i-1] consists of elements originally in A[1:i-1], but in sorted order.
- **Proof of correctness**:
  - *Initialization*: i=2, A[1] is trivially sorted
  - *Maintenance*: while loop shifts elements right to make room for key, then inserts key in correct position
  - *Termination*: i = n+1, A[1:n] is sorted
- **Complexity**:
  - Best case (already sorted): Θ(n)
  - Worst case (reverse sorted): Θ(n²)
  - Average case: Θ(n²)
- **Analysis detail**: Let tᵢ = number of times while loop test executes for a given i.
  - Best case: tᵢ = 1 for all i → T(n) = c₁n + c₂(n-1) + c₄(n-1) + c₅(n-1) + c₈(n-1) = an + b = Θ(n)
  - Worst case: tᵢ = i for all i → T(n) = c₁n + c₂(n-1) + c₄(n-1) + c₅Σtᵢ + c₆Σ(tᵢ-1) + c₇Σ(tᵢ-1) + c₈(n-1) = an² + bn + c = Θ(n²)

#### MERGE(A, p, q, r)
- **Type**: Algorithm (subroutine)
- **Goal**: Merge two adjacent sorted subarrays A[p:q] and A[q+1:r] into sorted A[p:r]
- **Input**: Array A, indices p,q,r with p ≤ q < r; subarrays A[p:q] and A[q+1:r] are sorted
- **Output**: A[p:r] sorted
- **Steps**:
  1. `nL = q - p + 1` (length of A[p:q])
  2. `nR = r - q` (length of A[q+1:r])
  3. Create L[0:nL-1] and R[0:nR-1]
  4. `for i = 0 to nL-1: L[i] = A[p+i]` (copy left half)
  5. `for j = 0 to nR-1: R[j] = A[q+j+1]` (copy right half)
  6. `i = 0; j = 0; k = p`
  7. `while i < nL and j < nR` (merge loop):
     - `if L[i] ≤ R[j]: A[k] = L[i]; i++`
     - `else: A[k] = R[j]; j++`
     - `k++`
  8. `while i < nL: A[k] = L[i]; i++; k++` (copy remaining L)
  9. `while j < nR: A[k] = R[j]; j++; k++` (copy remaining R)
- **Complexity**: Θ(n) where n = r-p+1
- **Invariant** (merge loop): At start of each iteration, A[p:k-1] contains the k-p smallest elements of L[0:nL-1] and R[0:nR-1], in sorted order; L[i] and R[j] are the smallest remaining elements of each array.

#### MERGE-SORT(A, p, r)
- **Type**: Algorithm
- **Goal**: Sort subarray A[p:r] using divide-and-conquer
- **Input**: Array A, indices p,r
- **Output**: A[p:r] sorted
- **Steps**:
  1. `if p ≥ r: return` (base case: 0 or 1 element)
  2. `q = ⌊(p+r)/2⌋` (midpoint)
  3. `MERGE-SORT(A, p, q)` (recursively sort left half)
  4. `MERGE-SORT(A, q+1, r)` (recursively sort right half)
  5. `MERGE(A, p, q, r)` (merge sorted halves)
- **Complexity**: T(n) = 2T(n/2) + Θ(n) → T(n) = Θ(n lg n)
- **Edge case**: When n is not a power of 2, subarray sizes differ by at most 1; merge still takes Θ(n) time.

#### Selection Sort (Exercise 2.2-2)
- **Idea**: Find smallest element in A[1:n], swap with A[1]; find smallest in A[2:n], swap with A[2]; continue for first n-1 elements.
- **Loop invariant**: After i iterations, A[1:i] contains the i smallest elements in sorted order.
- **Complexity**: Θ(n²) both best and worst case.

#### Binary Search (Exercise 2.3-6)
- **Idea**: Check midpoint of sorted subarray against value v; eliminate half; repeat.
- **Complexity**: Θ(lg n) worst-case.

### Loop Invariant Proof Pattern

- Three required properties:
  1. **Initialization**: Invariant true before first iteration
  2. **Maintenance**: If true before an iteration, remains true before next iteration
  3. **Termination**: Loop terminates; invariant + termination condition gives useful property showing correctness
- Loop invariant proof is a form of mathematical induction (base case = initialization, inductive step = maintenance).

### Classifications

- **Design paradigms for sorting**:
  - Incremental (insertion sort)
  - Divide-and-conquer (merge sort)

### Comparisons & Trade-offs

| Dimension | Insertion Sort | Merge Sort |
|---|---|---|
| Worst-case time | Θ(n²) | Θ(n lg n) |
| Best-case time | Θ(n) | Θ(n lg n) |
| In-place? | Yes | No (uses auxiliary arrays) |
| Small n | Fast due to tight constants | Slower due to overhead |
| Large n | Much slower | Much faster |
| Method | Incremental | Divide-and-conquer |

### Formulas & Equations

#### Merge sort recurrence
`T(n) = 2T(n/2) + Θ(n)`

#### General divide-and-conquer recurrence
`T(n) = aT(n/b) + D(n) + C(n)`
- a = number of subproblems
- n/b = size of each subproblem
- D(n) = cost to divide
- C(n) = cost to combine

#### Merge sort recursion tree
- Each level cost: c₂n (for internal nodes), c₁n (leaves)
- Number of levels: lg n + 1
- Total: c₂n lg n + c₁n = Θ(n lg n)

### End-of-Chapter Material

**Key exercises:**
- 2.1-1: Trace INSERTION-SORT on 〈31, 41, 59, 26, 41, 58〉
- 2.1-3: Rewrite INSERTION-SORT for monotonically decreasing order
- 2.1-4: Write LINEAR-SEARCH with loop invariant proof
- 2.2-2: Analyze SELECTION-SORT
- 2.3-4: Prove by induction that solution of merge sort recurrence is T(n) = n lg n for powers of 2
- 2.3-6: Write BINARY-SEARCH, show Θ(lg n) worst-case

**Problems:**
- 2-1: Insertion sort on small arrays in merge sort (coarsening)
- 2-2: Correctness of bubblesort
- 2-3: Correctness of Horner's rule
- 2-4: Inversions — relationship between insertion sort time and number of inversions; Θ(n lg n) inversion-counting via merge sort

---

## Ch. 3 — Characterizing Running Times

### Named Entities (Terms & Definitions)

- **Asymptotic efficiency**: How running time increases with input size in the limit, as input size increases without bound.
- **O-notation (big-oh)**: Asymptotic upper bound; function grows no faster than a certain rate.
- **Ω-notation (big-omega)**: Asymptotic lower bound; function grows at least as fast as a certain rate.
- **Θ-notation (theta)**: Asymptotically tight bound; function grows precisely at a certain rate within constant factors.
- **o-notation (little-oh)**: Upper bound that is NOT asymptotically tight; f(n) becomes insignificant relative to g(n).
- **ω-notation (little-omega)**: Lower bound that is NOT asymptotically tight; f(n) becomes arbitrarily large relative to g(n).
- **Asymptotically nonnegative**: f(n) ≥ 0 for all sufficiently large n.
- **Asymptotically positive**: f(n) > 0 for all sufficiently large n.
- **Leading term**: The term with the highest order of growth in a polynomial expression.
- **Watershed function** (Chapter 4 context): Function n^(log_b a) in the master theorem.
- **Driving function**: The f(n) term in a recurrence.
- **Polynomial**: Function p(n) = Σ a_d n^d of degree d.
- **Exponential**: Function a^n for a > 1.
- **Logarithm**: lg n = log₂ n (binary), ln n = log_e n (natural).
- **Polylogarithmically bounded**: f(n) = O(lg^k n) for some constant k.
- **Polynomially bounded**: f(n) = O(n^k) for some constant k.
- **Stirling's approximation**: n! = √(2πn) (n/e)^n (1 + Θ(1/n)).
- **Iterated logarithm**: lg* n = min{i ≥ 0: lg⁽ⁱ⁾ n ≤ 1}.
- **Fibonacci numbers**: F₀ = 0, F₁ = 1, F_i = F_{i-1} + F_{i-2} for i ≥ 2.
- **Golden ratio**: ϕ = (1 + √5)/2 ≈ 1.618; ϕ̂ = (1 - √5)/2 ≈ -0.618.
- **Monotonically increasing**: m ≤ n ⇒ f(m) ≤ f(n).
- **Monotonically decreasing**: m ≤ n ⇒ f(m) ≥ f(n).
- **Strictly increasing**: m < n ⇒ f(m) < f(n).
- **Strictly decreasing**: m < n ⇒ f(m) > f(n).
- **Floor**: ⌊x⌋ = greatest integer ≤ x.
- **Ceiling**: ⌈x⌉ = least integer ≥ x.
- **Modular arithmetic**: a mod n = remainder when a divided by n.
- **Equivalence modulo n**: a ≡ b (mod n) if (a mod n) = (b mod n).

### Formulas & Definitions

#### Formal definitions

**O-notation**: O(g(n)) = {f(n): ∃ c > 0, n₀ > 0 such that 0 ≤ f(n) ≤ cg(n) for all n ≥ n₀}

**Ω-notation**: Ω(g(n)) = {f(n): ∃ c > 0, n₀ > 0 such that 0 ≤ cg(n) ≤ f(n) for all n ≥ n₀}

**Θ-notation**: Θ(g(n)) = {f(n): ∃ c₁, c₂ > 0, n₀ > 0 such that 0 ≤ c₁g(n) ≤ f(n) ≤ c₂g(n) for all n ≥ n₀}

**o-notation**: o(g(n)) = {f(n): ∀ c > 0 ∃ n₀ > 0 such that 0 ≤ f(n) < cg(n) for all n ≥ n₀}; equivalently lim_{n→∞} f(n)/g(n) = 0

**ω-notation**: ω(g(n)) = {f(n): ∀ c > 0 ∃ n₀ > 0 such that 0 ≤ cg(n) < f(n) for all n ≥ n₀}; equivalently lim_{n→∞} f(n)/g(n) = ∞

### Theorem 3.1
- **Statement**: For any two functions f(n) and g(n), f(n) = Θ(g(n)) iff f(n) = O(g(n)) AND f(n) = Ω(g(n)).
- **Implications**: Proving both an upper bound and a lower bound gives a tight bound.

### Rules, Laws & Theorem Analogies

#### Comparison of asymptotic notations to real numbers
| Notation | Analogy |
|---|---|
| f(n) = O(g(n)) | a ≤ b |
| f(n) = Ω(g(n)) | a ≥ b |
| f(n) = Θ(g(n)) | a = b |
| f(n) = o(g(n)) | a < b |
| f(n) = ω(g(n)) | a > b |

**Asymptotic trichotomy does NOT hold** — not all functions are asymptotically comparable (e.g., n and n^(1+sin n)).

#### Transitivity
- f = Θ(g) and g = Θ(h) ⇒ f = Θ(h)
- f = O(g) and g = O(h) ⇒ f = O(h)
- f = Ω(g) and g = Ω(h) ⇒ f = Ω(h)
- f = o(g) and g = o(h) ⇒ f = o(h)
- f = ω(g) and g = ω(h) ⇒ f = ω(h)

#### Reflexivity
- f = Θ(f), f = O(f), f = Ω(f)

#### Symmetry
- f = Θ(g) iff g = Θ(f)

#### Transpose symmetry
- f = O(g) iff g = Ω(f)
- f = o(g) iff g = ω(f)

### Standard Functions & Growth Rates

**Polynomial**: p(n) = Σ_{i=0}^d a_i n^i with a_d > 0 ⇒ p(n) = Θ(n^d)

**Exponential vs Polynomial**: For all a > 1 and b, lim_{n→∞} n^b / a^n = 0. Any exponential with base > 1 grows faster than any polynomial.

**Logarithm base-change**: log_a n = log_b n / log_b a. Changing base changes value by constant factor.

**Polynomial vs Polylogarithm**: For all a > 0 and b, lim_{n→∞} lg^b n / n^a = 0. Any positive polynomial grows faster than any polylogarithmic function.

**Stirling's approximation**: n! = √(2πn)(n/e)^n (1 + Θ(1/n))

**Iterated logarithm growth**:
- lg* 2 = 1
- lg* 4 = 2
- lg* 16 = 3
- lg* 65536 = 4
- lg* 2⁶⁵⁵³⁶ = 5

**Fibonacci numbers**: F_i = ⌊ϕ^i / √5 + 1/2⌋ = (ϕ^i - ϕ̂^i) / √5; F_i grows exponentially.

### Edge Cases & Pitfalls

- Using O(n²) when Θ(n²) is meant — O-notation is only an upper bound, not necessarily tight.
- Saying "insertion sort's running time is Θ(n²)" is WRONG (overstates; best case is Θ(n)).
- Using asymptotic notation in inductive hypothesis without explicit constants can lead to false proofs (constants change across steps).
- Asymptotic notation in equations: O(g(n)) on RHS means "some anonymous function f(n) ∈ O(g(n))."
- O(1) for n < 3 is technically meaningless by formal definition (only constrains n ≥ n₀), but conventionally means bounded by constant.
- Some functions are not asymptotically comparable (e.g., n and n^(1+sin n)).
- The master theorem has gaps between cases; not all recurrences fit.

### End-of-Chapter Material

**Exercises:**
- 3.1-1: Modify insertion sort lower bound for non-multiples of 3
- 3.1-2: Analyze selection sort running time
- 3.2-1: Prove max{f(n),g(n)} = Θ(f(n)+g(n))
- 3.2-3: Is 2^(n+1) = O(2^n)? Is 2^(2n) = O(2^n)?
- 3.2-4: Prove Theorem 3.1
- 3.2-5: Prove T(n) = Θ(g(n)) iff worst-case O(g(n)) and best-case Ω(g(n))
- 3.3-1 through 3.3-9: Various properties of monotonicity, floors/ceilings, factorial, Fibonacci

**Problems:**
- 3-1: Asymptotic behavior of polynomials
- 3-2: Relative asymptotic growths (table of O/o/Ω/ω/Θ relationships)
- 3-3: Ordering by asymptotic growth rates (30 functions to rank)
- 3-4: Asymptotic notation properties (prove or disprove 8 conjectures)
- 3-5: Manipulating asymptotic notation
- 3-6: Variations on O and Ω (Ω_∞, O′, Õ)
- 3-7: Iterated functions

---

## Ch. 4 — Divide-and-Conquer

### Named Entities (Terms & Definitions)

- **Divide-and-conquer method**: Algorithm design paradigm: (1) Divide problem into subproblems, (2) Conquer subproblems recursively, (3) Combine subproblem solutions.
- **Recurrence**: Equation describing a function in terms of its value on smaller arguments.
- **Algorithmic recurrence**: Recurrence T(n) where (1) for all n < n₀, T(n) = Θ(1), and (2) every recursion path terminates in finite steps.
- **Base case**: Non-recursive case in a recurrence (small enough to solve directly).
- **Recursive case**: Case involving recursive invocation(s).
- **Substitution method**: Solve recurrence by guessing form of solution and proving by induction.
- **Recursion-tree method**: Model recurrence as tree with costs at nodes; sum costs per level.
- **Master method**: Cookbook method for recurrences of form T(n) = aT(n/b) + f(n).
- **Master theorem** (Theorem 4.1): Provides asymptotic bounds for master recurrences.
- **Continuous master theorem** (Theorem 4.4): Variant with domain over reals.
- **Akra-Bazzi method**: General method for divide-and-conquer recurrences with different-sized subproblems.
- **Akra-Bazzi recurrence**: T(n) = Σ_{i=1}^k a_i T(n/b_i) + f(n).
- **Driving function**: The f(n) term in a recurrence.
- **Watershed function**: n^{log_b a} (used in master theorem comparisons).
- **Regularity condition**: af(n/b) ≤ cf(n) for some c < 1 and all sufficiently large n (needed for Master Theorem case 3).
- **Polynomial-growth condition**: Condition on f(n) that allows ignoring floors/ceilings: for every φ ≥ 1, ∃ d > 1 such that f(n)/d ≤ f(ψn) ≤ d f(n) for all 1 ≤ ψ ≤ φ and sufficiently large n.
- **Matrix multiplication**: C = A·B where c_{ij} = Σ_{k=1}^n a_{ik}·b_{kj}.
- **Dense matrix**: Most entries are non-zero.
- **Sparse matrix**: Most entries are zero.
- **Strassen's algorithm**: O(n^{lg 7}) ≈ O(n^{2.81}) matrix multiplication algorithm using 7 recursive multiplications.
- **Karatsuba's algorithm**: Referenced as early divide-and-conquer (1962).
- **Monge array**: Array where for all i<k, j<l: A[i,j] + A[k,l] ≤ A[i,l] + A[k,j].

### Sequential Processes (Algorithms)

#### MATRIX-MULTIPLY(A, B, C, n)
- **Type**: Algorithm
- **Goal**: Compute C = C + A·B for n×n matrices
- **Steps**:
  1. `for i = 1 to n`
  2. `for j = 1 to n`
  3. `for k = 1 to n`
  4. `c_{ij} = c_{ij} + a_{ik} · b_{kj}`
- **Complexity**: Θ(n³) (triply nested loops)

#### MATRIX-MULTIPLY-RECURSIVE(A, B, C, n)
- **Type**: Algorithm (divide-and-conquer)
- **Goal**: Compute C = C + A·B recursively
- **Assumption**: n is exact power of 2
- **Steps**:
  1. `if n == 1: c₁₁ = c₁₁ + a₁₁·b₁₁; return`
  2. Partition A, B, C into n/2 × n/2 submatrices
  3. Eight recursive calls:
     - `MM-REC(A₁₁, B₁₁, C₁₁, n/2)`
     - `MM-REC(A₁₁, B₁₂, C₁₂, n/2)`
     - `MM-REC(A₂₁, B₁₁, C₂₁, n/2)`
     - `MM-REC(A₂₁, B₁₂, C₂₂, n/2)`
     - `MM-REC(A₁₂, B₂₁, C₁₁, n/2)`
     - `MM-REC(A₁₂, B₂₂, C₁₂, n/2)`
     - `MM-REC(A₂₂, B₂₁, C₂₁, n/2)`
     - `MM-REC(A₂₂, B₂₂, C₂₂, n/2)`
- **Recurrence**: T(n) = 8T(n/2) + Θ(1) → T(n) = Θ(n³)
- **Key insight**: No faster than basic Θ(n³) algorithm.

#### Strassen's Algorithm
- **Type**: Algorithm (divide-and-conquer)
- **Goal**: Multiply n×n matrices in O(n^{lg 7}) time
- **Assumption**: n is exact power of 2
- **Four steps**:
  1. **Base case** (n=1): single scalar multiplication
  2. **Create 10 sum/difference matrices** S₁,…,S₁₀ (Θ(n²) time):
     - S₁ = B₁₂ - B₂₂
     - S₂ = A₁₁ + A₁₂
     - S₃ = A₂₁ + A₂₂
     - S₄ = B₂₁ - B₁₁
     - S₅ = A₁₁ + A₂₂
     - S₆ = B₁₁ + B₂₂
     - S₇ = A₁₂ - A₂₂
     - S₈ = B₂₁ + B₂₂
     - S₉ = A₁₁ - A₂₁
     - S₁₀ = B₁₁ + B₁₂
  3. **Recursively compute 7 products** P₁,…,P₇:
     - P₁ = A₁₁ · S₁ = A₁₁·B₁₂ - A₁₁·B₂₂
     - P₂ = S₂ · B₂₂ = A₁₁·B₂₂ + A₁₂·B₂₂
     - P₃ = S₃ · B₁₁ = A₂₁·B₁₁ + A₂₂·B₁₁
     - P₄ = A₂₂ · S₄ = A₂₂·B₂₁ - A₂₂·B₁₁
     - P₅ = S₅ · S₆ = A₁₁·B₁₁ + A₁₁·B₂₂ + A₂₂·B₁₁ + A₂₂·B₂₂
     - P₆ = S₇ · S₈ = A₁₂·B₂₁ + A₁₂·B₂₂ - A₂₂·B₂₁ - A₂₂·B₂₂
     - P₇ = S₉ · S₁₀ = A₁₁·B₁₁ + A₁₁·B₁₂ - A₂₁·B₁₁ - A₂₁·B₁₂
  4. **Combine results** into C₁₁, C₁₂, C₂₁, C₂₂ (Θ(n²) time):
     - C₁₁ = C₁₁ + P₅ + P₄ - P₂ + P₆
     - C₁₂ = C₁₂ + P₁ + P₂
     - C₂₁ = C₂₁ + P₃ + P₄
     - C₂₂ = C₂₂ + P₅ + P₁ - P₃ - P₇
- **Recurrence**: T(n) = 7T(n/2) + Θ(n²) → T(n) = Θ(n^{lg 7}) = O(n^{2.81})
- **Trade-off**: 7 multiplications instead of 8, at cost of 18 additions instead of 4.

### Recurrence-Solving Methods

#### 1. Substitution Method (Section 4.3)
- **Steps**:
  1. Guess form of solution (using symbolic constants)
  2. Use mathematical induction to prove guess works and find constants
- **Key techniques**:
  - Prove O-bound and Ω-bound separately, then combine for Θ-bound
  - Use explicit constants, NOT asymptotic notation in inductive hypothesis
  - **Subtract a lower-order term** if proof doesn't go through (e.g., guess cn - d instead of cn)
- **Example** (T(n) = 2T(⌊n/2⌋) + Θ(n)):
  - Guess: T(n) ≤ cn lg n
  - Assume for m < n: T(⌊n/2⌋) ≤ c⌊n/2⌋ lg(⌊n/2⌋)
  - T(n) ≤ 2(c(n/2) lg(n/2)) + Θ(n) = cn lg n - cn + Θ(n) ≤ cn lg n (for sufficiently large c,n₀)
- **Subtracting lower-order term example** (T(n) = 2T(n/2) + Θ(1)):
  - Guess T(n) ≤ cn - d (not just cn, which fails)
  - Then T(n) ≤ 2(c(n/2) - d) + Θ(1) = cn - 2d + Θ(1) ≤ cn - d

#### 2. Recursion-Tree Method (Section 4.4)
- **Steps**:
  1. Draw tree with root = cost of top-level call
  2. Each node's children = subproblem costs
  3. Sum costs per level
  4. Sum across levels for total cost
- **Use**: Best for generating guesses; verify with substitution method
- **Example**: T(n) = 3T(n/4) + cn²
  - Levels: depth i has 3ⁱ nodes, each cost c(n/4ⁱ)²
  - Per level cost: (3/16)ⁱ cn²
  - Leaf depth: log₄ n
  - Total: Σ (3/16)ⁱ cn² from i=0 to log₄ n-1 + Θ(n^{log₄ 3})
  - This is a decreasing geometric series → dominated by root cost → Θ(n²)
- **Irregular example**: T(n) = T(n/3) + T(2n/3) + cn
  - Tree height: Θ(lg n)
  - Each level cost ≤ cn
  - Total internal cost: O(n lg n)
  - Number of leaves: L(n) = L(n/3) + L(2n/3) → L(n) = Θ(n)
  - Leaf cost: Θ(n)
  - Total: Θ(n lg n)

#### 3. Master Method (Section 4.5)
- **Prerequisite**: Recurrence of form T(n) = aT(n/b) + f(n) where a > 0, b > 1
- **Three cases**:

| Case | Condition | Solution |
|---|---|---|
| 1 | f(n) = O(n^{log_b a - ε}) for some ε > 0 | T(n) = Θ(n^{log_b a}) |
| 2 | f(n) = Θ(n^{log_b a} lg^k n) for k ≥ 0 | T(n) = Θ(n^{log_b a} lg^{k+1} n) |
| 3 | f(n) = Ω(n^{log_b a + ε}) for ε > 0, AND af(n/b) ≤ cf(n) for c < 1 | T(n) = Θ(f(n)) |

- **Watershed function**: n^{log_b a}
- **Case 1 intuition**: Watershed grows polynomially faster → leaf cost dominates
- **Case 2 intuition**: Equal growth rates → all levels cost same → multiply by lg n
- **Case 3 intuition**: Driving function grows polynomially faster → root cost dominates
- **Examples**:
  - T(n) = 9T(n/3) + n: a=9, b=3, n^{log₃9}=n², f(n)=n=O(n^{2-ε}) → Case 1 → Θ(n²)
  - T(n) = T(2n/3) + 1: a=1, b=3/2, n^{log_{3/2}1}=n⁰=1, f(n)=1=Θ(1) → Case 2 → Θ(lg n)
  - T(n) = 3T(n/4) + n lg n: a=3, b=4, n^{log₄3}=n^{0.793}, f(n)=n lg n=Ω(n^{0.793+ε}) → Case 3 → Θ(n lg n)
  - T(n) = 2T(n/2) + n lg n: a=2, b=2, n^{log₂2}=n, f(n)=n lg n=Θ(n lg¹ n) → Case 2 with k=1 → Θ(n lg² n)
  - T(n) = 2T(n/2) + Θ(n): a=2, b=2, f(n)=Θ(n) → Case 2 with k=0 → Θ(n lg n)
  - T(n) = 8T(n/2) + Θ(1): a=8, b=2, n^{log₂8}=n³, f(n)=Θ(1)=O(n^{3-ε}) → Case 1 → Θ(n³)
  - T(n) = 7T(n/2) + Θ(n²): a=7, b=2, n^{lg7}=n^{2.807}, f(n)=n²=O(n^{lg7-ε}) → Case 1 → Θ(n^{lg7})
- **Gaps where master theorem doesn't apply**:
  - Between Case 1 and 2: f(n) = Θ(n^{log_b a} / lg n) [slower than watershed but not polynomially slower]
  - Between Case 2 and 3: f(n) = Θ(n^{log_b a} · lg n) but no polynomial separation
  - Regularity condition fails in Case 3

#### 4. Akra-Bazzi Method (Section 4.7)
- **For recurrences**: T(n) = Σ_{i=1}^{k} a_i T(n/b_i) + f(n)
- **Step 1**: Find unique real p such that Σ_{i=1}^{k} a_i b_i^{-p} = 1
- **Step 2**: Solution is T(n) = Θ(n^p + n^p ∫_{1}^{n} f(x)/x^{p+1} dx)
- **Example**: T(n) = T(n/5) + T(7n/10) + n
  - Find p: (1/5)^p + (7/10)^p = 1 → p ≈ 0.83978
  - T(n) = Θ(n^p + n^p ∫_{1}^{n} x·x^{-p-1} dx) = Θ(n^p + n^p ∫ x^{-p} dx) = Θ(n^p + n^p · n^{1-p}) = Θ(n)
- **Prerequisite**: f(n) must satisfy polynomial-growth condition for ignoring floors/ceilings.

### Theorem 4.5 (Floors and Ceilings)
- If f(n) satisfies polynomial-growth condition, replacing T(n/bᵢ) with T(⌈n/bᵢ⌉) or T(⌊n/bᵢ⌋) doesn't change asymptotic solution.

### Polynomial-Growth Condition
- ∃ e₀ ≥ 0 such that ∀ φ ≥ 1, ∃ d > 1 (depending on φ) such that f(n)/d ≤ f(ψn) ≤ d f(n) for all 1 ≤ ψ ≤ φ and sufficiently large n.
- Roughly: f(Θ(n)) = Θ(f(n))
- Examples: n^α lg^β n lg lg^γ n satisfy it; exponentials 2^n do not.

### Edge Cases & Pitfalls

- Floors and ceilings in recurrences can usually be ignored for asymptotic solutions.
- Base cases of recurrences are almost always T(n) = Θ(1) for n < n₀ and can be omitted.
- Recurrences can be inequalities (T(n) ≤ 2T(n/2) + Θ(n) → O-bound; ≥ → Ω-bound).
- The master theorem does NOT apply when f(n) is not polynomially comparable to n^{log_b a}.
- Regularity condition must be checked for Case 3.
- For Akra-Bazzi, f(n) MUST satisfy polynomial-growth condition to ignore floors/ceilings.
- Matrices need not be exact powers of 2 (padding works, doesn't change asymptotic).

### End-of-Chapter Material

**Exercises:**
- 4.1-1: Generalize MATRIX-MULTIPLY-RECURSIVE for any n
- 4.2-1: Trace Strassen's on concrete 2×2 matrices
- 4.2-2: Write pseudocode for Strassen's algorithm
- 4.3-1 through 4.3-3: Substitution method practice
- 4.4-1 through 4.4-4: Recursion-tree method practice
- 4.5-1: Master method on 5 recurrences
- 4.5-2: Professor Caesar's algorithm — max a to beat Strassen
- 4.5-4: Why f(n)=lg n fails regularity condition
- 4.7-1 through 4.7-6: Akra-Bazzi method practice

**Problems:**
- 4-1: Recurrence examples (8 recurrences)
- 4-2: Parameter-passing costs (pointer vs copy vs subrange)
- 4-3: Change of variables method for solving recurrences
- 4-4: More recurrence examples (10 recurrences)
- 4-5: Fibonacci numbers via generating functions
- 4-6: Chip testing (divide-and-conquer identification of good chips)
- 4-7: Monge arrays (divide-and-conquer algorithm for leftmost minima)

---

## Ch. 5 — Probabilistic Analysis and Randomized Algorithms

### Named Entities (Terms & Definitions)

- **Probabilistic analysis**: Use of probability in analyzing problems (average over input distribution).
- **Randomized algorithm**: Algorithm whose behavior is determined by both input and values from a random-number generator.
- **Expected running time**: Running time averaged over the random choices made by the algorithm.
- **Average-case running time**: Running time averaged over the distribution of inputs.
- **Random-number generator**: RANDOM(a,b) returns integer between a and b inclusive, each equally likely.
- **Indicator random variable**: I{A} = 1 if event A occurs, 0 otherwise. E[I{A}] = Pr{A}.
- **Linearity of expectation**: E[Σ X_i] = Σ E[X_i] (holds even with dependence).
- **Uniform random permutation**: Each of n! permutations equally likely (probability 1/n!).
- **Hiring problem**: Model for finding maximum/minimum in a sequence; interview n candidates, hire when better than current best.
- **Birthday paradox**: With only 23 people, probability ≥ 1/2 that two share a birthday.
- **Balls and bins**: Random tossing of balls into bins; used in hash analysis.
- **Coupon collector's problem**: Expected number of trials to collect all b coupons is approximately b ln b.
- **Streaks**: Consecutive heads in n coin flips; longest streak expected length Θ(lg n).
- **Online hiring problem (secretary problem)**: Strategy of rejecting first k candidates then hiring the first better one; optimal k = n/e with success probability ≥ 1/e.
- **k-permutation**: Sequence containing k of n elements, no repetitions.
- **Hat-check problem**: Expected number of customers who get their own hat back = 1.

### Sequential Processes (Algorithms)

#### HIRE-ASSISTANT(n)
- **Type**: Algorithm
- **Goal**: Hire the best-qualified office assistant
- **Input**: n candidates interviewed sequentially
- **Steps**:
  1. `best = 0` (dummy least-qualified candidate)
  2. `for i = 1 to n`
  3. `interview candidate i`
  4. `if candidate i is better than candidate best`
  5. `best = i`
  6. `hire candidate i`
- **Cost model**: Interview cost cᵢ, hiring cost cₕ; total = cᵢ·n + cₕ·m where m = number hired
- **Complexity**:
  - Worst-case: n hires, O(cₕ·n) (candidates in strictly increasing order)
  - Average-case (random order): O(cₕ·ln n) expected hiring cost

#### RANDOMIZED-HIRE-ASSISTANT(n)
- **Type**: Algorithm (randomized)
- **Goal**: Eliminate dependence on input order
- **Steps**:
  1. `randomly permute the list of candidates`
  2. `HIRE-ASSISTANT(n)`
- **Expected cost**: O(cₕ·ln n) for any input

#### RANDOMLY-PERMUTE(A, n)
- **Type**: Algorithm
- **Goal**: Generate uniform random permutation in place
- **Steps**:
  1. `for i = 1 to n`
  2. `swap A[i] with A[RANDOM(i, n)]`
- **Complexity**: Θ(n) time
- **Correctness proof** (Lemma 5.4): Loop invariant — just prior to i-th iteration, each (i-1)-permutation in A[1:i-1] has probability (n-i+1)!/n!

#### ONLINE-MAXIMUM(k, n)
- **Type**: Algorithm (online hiring)
- **Goal**: Hire the best candidate by interviewing first k (reject them all), then hire first better one
- **Steps**:
  1. `best-score = -∞`
  2. `for i = 1 to k: if score(i) > best-score: best-score = score(i)`
  3. `for i = k+1 to n: if score(i) > best-score: return i`
  4. `return n` (if no better candidate found after k)
- **Success probability**: Pr{S} = (k/n)(ln n - ln k) (approximate); max at k = n/e → Pr{S} ≥ 1/e

### Formulas & Equations

#### Expected value of indicator random variable
`E[I{A}] = Pr{A}` (Lemma 5.1)

#### Hiring problem — expected number of hires
- Xᵢ = I{candidate i is hired}
- Pr{candidate i is hired} = 1/i
- E[X] = Σ_{i=1}^n 1/i = ln n + O(1) ≈ ln n
- Expected hiring cost = O(cₕ·ln n)

#### Birthday paradox
- Probability k people have distinct birthdays: Π_{i=1}^{k-1} (1 - i/n) ≤ e^{-k(k-1)/(2n)}
- Threshold for Pr ≥ 1/2: k ≥ (1 + √(1 + 8n ln 2))/2 ≈ 23 for n=365
- Expected number of matching pairs: E[X] = C(k,2)·(1/n) = k(k-1)/(2n)
- Threshold for expectation ≥ 1: k ≥ (1 + √(1+8n))/2

#### Balls and bins
- Expected balls in given bin: n/b
- Expected tosses until given bin gets a ball: b
- Expected tosses until all bins have ≥1 ball: b·H_b = b·(ln b + O(1))

#### Streaks of heads
- Expected longest streak of heads in n coin flips: Θ(lg n)
- Pr{streak of length ≥ 2⌈lg n⌉} ≤ 1/n
- Pr{length ≥ r⌈lg n⌉} ≤ 1/n^{r-1}
- Lower bound: streak of length ≥ ⌊(lg n)/2⌋ occurs with probability ≥ 1 - O(1/n)

#### Online hiring
- Pr{success with k} = (k/n)(H_{n-1} - H_{k-1}) ≈ (k/n)(ln n - ln k)
- Optimal k = n/e, success probability ≥ 1/e ≈ 0.368

### Rules, Laws & Theorems

#### Lemma 5.1
- **Statement**: E[I{A}] = Pr{A} for any event A.
- **Proof**: E[I{A}] = 1·Pr{A} + 0·Pr{Ā} = Pr{A}.

#### Lemma 5.2
- **Statement**: HIRE-ASSISTANT has average-case total hiring cost O(cₕ ln n) assuming random input order.

#### Lemma 5.3
- **Statement**: RANDOMIZED-HIRE-ASSISTANT has expected hiring cost O(cₕ ln n) for ANY input.

#### Lemma 5.4
- **Statement**: RANDOMLY-PERMUTE computes a uniform random permutation.
- **Proof**: Loop invariant on (i-1)-permutations.

#### Linearity of Expectation
- E[Σ X_i] = Σ E[X_i] (no independence required)

### Classifications

| Type | Input/Algorithm | Running time characterization |
|---|---|---|
| Deterministic algorithm | Fixed input | Worst-case / best-case |
| Probabilistic analysis | Random input distribution | Average-case |
| Randomized algorithm | Algorithm makes random choices | Expected running time |

### Comparisons & Trade-offs

| Dimension | Deterministic HIRE-ASSISTANT | Randomized HIRE-ASSISTANT |
|---|---|---|
| Input assumption | Candidates in random order (may not hold) | None — algorithm creates randomness |
| Worst-case cost | O(cₕ·n) | O(cₕ·n) (if RNG produces bad permutation) |
| Expected cost | O(cₕ·ln n) (under assumption) | O(cₕ·ln n) (guaranteed) |
| Additional overhead | None | O(n) time to permute |

### Edge Cases & Pitfalls

- Worst-case input for hiring: strictly increasing quality order → hire every candidate.
- The event that empty subarray contains 0-permutation must have probability 1, not 0 (for RANDOMLY-PERMUTE loop invariant).
- Proving each element equally likely to end up in each position (probability 1/n) is NOT sufficient to prove uniform random permutation (Exercise 5.3-4).
- For the birthday paradox, both mutual independence and pairwise independence give the same result for expectation, but pairwise independence may not suffice for probability bounds (Exercise 5.4-4).
- The probability that longest streak ≥ s is NOT the same as the probability that some group of s consecutive flips is all heads (streaks can cross group boundaries).

### Key Results & Empirical Values

- 23 people: Pr{matching birthday} ≥ 1/2
- 28 people: expected matching pairs ≈ 1.036
- b·ln b tosses expected to fill all b bins
- Longest streak in 1000 flips: ≥ 20 heads has probability ≤ 1/1000
- Optimal online hiring: interview first 37% (n/e), then hire first better; success probability ≥ 37% (1/e)

### End-of-Chapter Material

**Exercises:**
- 5.1-1: Total order on candidates implied by ability to determine best
- 5.1-2: Implement RANDOM(a,b) using RANDOM(0,1)
- 5.1-3: Unbiased random from biased random
- 5.2-1 through 5.2-6: Indicator random variable practice (hiring probabilities, dice, hat-check, inversions)
- 5.3-1 through 5.3-5: Random permutation variants (with/without identity, with-all, by-cycle, random-sample)
- 5.4-1 through 5.4-8: Birthday paradox variations, balls/bins, streaks

**Problems:**
- 5-1: Probabilistic counting (Morris's algorithm)
- 5-2: Searching an unsorted array (random search vs deterministic vs scramble search)

---

## Cross-Cutting Topics

### Design Paradigms

1. **Incremental Method**: Build solution incrementally, adding one element at a time.
   - Example: Insertion sort — grows sorted portion by one element per iteration.

2. **Divide-and-Conquer**: (1) Divide into subproblems, (2) Conquer recursively, (3) Combine.
   - Examples: Merge sort, MATRIX-MULTIPLY-RECURSIVE, Strassen's algorithm
   - Recurrence form: T(n) = aT(n/b) + f(n)

3. **Randomization**: Use random choices to make algorithm performance independent of input distribution.
   - Examples: RANDOMIZED-HIRE-ASSISTANT, RANDOMLY-PERMUTE

### Proof & Argument Patterns

1. **Loop Invariant**: Show correctness of iterative algorithms via Initialization — Maintenance — Termination.
   - Used for: INSERTION-SORT, RANDOMLY-PERMUTE, MERGE

2. **Mathematical Induction**:
   - Used in: substitution method for recurrences, proof of correct sorting
   - Base case (n = 1 or small constant) → Induction step

3. **Substitution Method for Recurrences**:
   - Guess solution → Assume for smaller arguments → Prove for n → Find constants
   - Trick: subtract lower-order term if proof doesn't go through
   - Pitfall: avoid using asymptotic notation in inductive hypothesis

4. **Recursion-Tree Analysis**:
   - Sum costs level-by-level across a tree of recursive calls
   - Geometric series → dominated by root or leaves
   - Arithmetic series (equal cost per level) → multiply by lg n

5. **Probabilistic Analysis with Indicator Random Variables**:
   - Decompose quantity into sum of indicator variables
   - Apply linearity of expectation
   - E[I{A}] = Pr{A}

### Probability & Statistics Foundation (from Ch. 5)

- **Indicator random variables**: I{A} = 1 if A occurs, 0 otherwise; E[I{A}] = Pr{A}
- **Linearity of expectation**: E[Σ X_i] = Σ E[X_i] (always, even with dependence)
- **Geometric distribution**: Number of trials until first success; expected value = 1/p
- **Binomial distribution**: Number of successes in n independent trials; expected value = np
- **Birthday paradox**: Product bound Π(1 - i/n) ≤ e^{-i/n} ≤ e^{-k(k-1)/(2n)}
- **Harmonic numbers**: H_n = Σ_{i=1}^n 1/i = ln n + γ + O(1/n) where γ ≈ 0.577
- **Coupon collector**: Expected b·H_b ≈ b ln b trials to collect all b coupons

### Mnemonics & Memory Aids

- **Asymptotic notation analogy**: O = ≤, Ω = ≥, Θ = =, o = <, ω = >
- **Master theorem cases**:
  1. Leaves dominate (n^{log_b a} wins)
  2. Tied (all levels same cost) → add lg n
  3. Root dominates (f(n) wins)
- **Master theorem mnemonic**: Compare f(n) to n^{log_b a}; if f(n) is polynomially smaller → case 1; if same up to lg^k → case 2; if polynomially larger + regularity → case 3
- **Birthday paradox**: 23 people → 50% chance; 28 → expect a match
- **Optimal hiring**: 37% rejection → 37% success

### People & Dates

- **Al-Khowârizmî**: 9th-century Persian mathematician, origin of word "algorithm"
- **Knuth (1968)**: The Art of Computer Programming
- **Knuth**: Introduced Ω and Θ notations
- **Bachmann (1892)**: Origin of O-notation
- **Landau (1909)**: Invented o-notation
- **Strassen (1969)**: O(n^{2.81}) matrix multiplication
- **Coppersmith & Winograd (1987)**: O(n^{2.376}) matrix multiplication
- **Williams (2012)**: O(n^{2.37287}) matrix multiplication
- **Akra & Bazzi**: Generalized recurrence method
- **De Moivre**: Generating functions for Fibonacci
- **Fibonacci (1202)**: Fibonacci numbers
- **Fisher & Yates / Durstenfeld**: Random permutation algorithm
- **von Neumann (1945)**: First merge sort program for EDVAC
- **Leibnitz**: Loosely referenced in chapter notes context
