# Study Guide: Introduction to Algorithms (CLRS 4th Edition)

> Generated 2026-06-03. Subject: Computer Science / Algorithms. Exam format: Mixed (MCQ, short answer, problem-solving, essay). Coverage: comprehensive.

> Target length: ~5000 lines.

---

## Chapter 6: Heapsort

### 6.1 Named Entities & Definitions

- **Heap**: An array object viewed as a nearly complete binary tree. Completely filled on all levels except possibly the lowest, which is filled from left to right.
- **Max-heap property**: For every node `i` other than the root, `A[PARENT(i)] ≥ A[i]` — the largest element is at the root.
- **Min-heap property**: For every node `i` other than the root, `A[PARENT(i)] ≤ A[i]` — the smallest element is at the root.
- **Height of a node**: Number of edges on the longest simple downward path from the node to a leaf.
- **Height of heap**: Height of its root = `Θ(lg n)`.
- **A.heap-size**: number of heap elements stored in array A[1:n].
- **Empty heap**: when `A.heap-size = 0`.

### 6.2 Data Structure: Binary Heap

**Array representation** (1-indexed):
```
PARENT(i) = ⌊i/2⌋
LEFT(i)   = 2i
RIGHT(i)  = 2i + 1
```
- Leaves: indices `⌊n/2⌋ + 1, ⌊n/2⌋ + 2, ..., n`
- Height of n-element heap: `⌊lg n⌋`

**Properties**:
| Property | Value |
|---|---|
| Height | Θ(lg n) |
| Min elements in height h | 2^h |
| Max elements in height h | 2^{h+1} - 1 |
| Nodes of height h | at most ⌈n/2^{h+1}⌉ |
| Leaves count | ⌈n/2⌉ |

### 6.3 Processes & Algorithms

#### MAX-HEAPIFY(A, i)
- **Input**: Array A with heap-size, index i; assumes subtrees at LEFT(i) and RIGHT(i) are max-heaps.
- **Output**: subtree at i is a max-heap.
- **Steps**:
  1. `l = LEFT(i)`, `r = RIGHT(i)`
  2. `largest = i`
  3. if `l ≤ A.heap-size` and `A[l] > A[i]`: `largest = l`
  4. if `r ≤ A.heap-size` and `A[r] > A[largest]`: `largest = r`
  5. if `largest ≠ i`: swap A[i] ↔ A[largest]; recurse on `MAX-HEAPIFY(A, largest)`
- **Time**: O(lg n). Recurrence: `T(n) ≤ T(2n/3) + Θ(1)`. Solved via case 2 of Master Theorem → O(lg n).
- **Worst case**: Ω(lg n) — when the leaf is far and values force recursive calls on every node along a path from root to leaf.

**Concrete example**: `A = [27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0]`, call MAX-HEAPIFY(A, 3):
- Values: A[3]=3, LEFT=10 (A[6]), RIGHT=1 (A[7])
- largest = 6 (value 10), swap A[3]↔A[6] → A=[27,17,10,16,13,3,1,5,7,12,4,8,9,0]
- Recurse MAX-HEAPIFY(A,6): A[6]=3, LEFT=8 (A[12]), RIGHT=9 (A[13])
- largest=12 (value 8), swap A[6]↔A[12] → A=[27,17,10,16,13,8,1,5,7,12,4,3,9,0]
- Recurse MAX-HEAPIFY(A,12): A[12]=3, LEFT=24 > hs, RIGHT=25 > hs → done

#### BUILD-MAX-HEAP(A, n)
- **Input**: unordered array A[1:n]
- **Output**: A is a max-heap
- **Steps**:
  1. `A.heap-size = n`
  2. `for i = ⌊n/2⌋ down to 1: MAX-HEAPIFY(A, i)`
- **Loop invariant**: at start of each iteration, each node i+1, i+2, ..., n is root of a max-heap.
- **Time**: O(n) (tight). Proof: cost at height h = O(h), nodes at height h ≤ n/2^{h+1}, sum_{h=0}^{⌊lg n⌋} n/2^{h+1} · O(h) = O(n).

**Concrete example**: `A = [5, 3, 17, 10, 84, 19, 6, 22, 9]`, n=9:
- Leaves start at ⌊9/2⌋+1 = 5 (indices 5..9)
- i=4: MAX-HEAPIFY(A,4): A[4]=10, LEFT=22(A[8]), RIGHT=9(A[9]) → swap 10↔22
- i=3: MAX-HEAPIFY(A,3): A[3]=17, LEFT=19(A[6]), RIGHT=6(A[7]) → swap 17↔19
- i=2: MAX-HEAPIFY(A,2): A[2]=3, LEFT=84(A[5]), RIGHT=10(A[4]) → swap 3↔84; recurse → swap 3↔22
- i=1: MAX-HEAPIFY(A,1): A[1]=5, LEFT=84(A[2]), RIGHT=19(A[3]) → swap 5↔84; recurse → swap 5↔17
- Final heap: [84, 22, 19, 10, 3, 17, 6, 5, 9]

#### HEAPSORT(A, n)
- **Steps**:
  1. `BUILD-MAX-HEAP(A, n)`  — O(n)
  2. `for i = n down to 2`:
     - exchange A[1] ↔ A[i]
     - `A.heap-size = A.heap-size - 1`
     - `MAX-HEAPIFY(A, 1)`  — O(lg n) each
- **Time**: O(n lg n) overall.
- **Loop invariant**: subarray A[1:i] is a max-heap containing the i smallest elements of A[1:n]; subarray A[i+1:n] contains the n-i largest elements, sorted.
- **Best case**: Ω(n lg n) even when all elements are distinct.
- **Sorted increasing order input**: still Θ(n lg n) (no advantage).
- **Sorted decreasing order input**: BUILD-MAX-HEAP is O(n), then n-1 MAX-HEAPIFY calls O(n lg n).

**Concrete example**: `A = [5, 13, 2, 25, 7, 17, 20, 8, 4]`:
- BUILD-MAX-HEAP → [25, 13, 20, 8, 7, 17, 2, 5, 4]
- i=9: swap 25↔4, heap-size=8, MAX-HEAPIFY(A,1) → [20, 13, 17, 8, 7, 4, 2, 5 | 25]
- i=8: swap 20↔5 → [5,13,17,8,7,4,2 | 20,25]; MAX-HEAPIFY → [17,13,5,8,7,4,2 | 20,25]
- i=7: swap 17↔2 → [2,13,5,8,7,4 | 17,20,25]; MAX-HEAPIFY → [13,8,5,2,7,4 | 17,20,25]
- i=6: swap 13↔4 → [4,8,5,2,7 | 13,17,20,25]; MAX-HEAPIFY → [8,7,5,2,4 | 13,17,20,25]
- i=5: swap 8↔4 → [4,7,5,2 | 8,13,17,20,25]; MAX-HEAPIFY → [7,4,5,2 | 8,13,17,20,25]
- i=4: swap 7↔2 → [2,4,5 | 7,8,13,17,20,25]; MAX-HEAPIFY → [5,4,2 | 7,8,13,17,20,25]
- i=3: swap 5↔2 → [2,4 | 5,7,8,13,17,20,25]; MAX-HEAPIFY → [4,2 | ...]
- i=2: swap 4↔2 → [2,4,5,7,8,13,17,20,25]

### 6.4 Priority Queues

| Operation | Procedure | Time |
|---|---|---|
| MAXIMUM(S) | MAX-HEAP-MAXIMUM(A): return A[1] | Θ(1) |
| EXTRACT-MAX(S) | MAX-HEAP-EXTRACT-MAX(A): save max, replace root with last, heapify, return max | O(lg n) |
| INCREASE-KEY(S,x,k) | MAX-HEAP-INCREASE-KEY(A,x,k): verify k ≥ current, set key, sift up | O(lg n) |
| INSERT(S,x,k) | MAX-HEAP-INSERT(A,x,n): extend heap with key=-∞, then INCREASE-KEY | O(lg n) |

```
```

```
```

```
```

- At start of each while iteration:
  - a. If PARENT(i) and LEFT(i) exist, A[PARENT(i)].key ≥ A[LEFT(i)].key
  - b. If PARENT(i) and RIGHT(i) exist, A[PARENT(i)].key ≥ A[RIGHT(i)].key
  - c. Subarray A[1:A.heap-size] satisfies max-heap property except possibly one violation: A[i].key > A[PARENT(i)].key

### 6.5 Edge Cases
- **Heap with distinct elements**: smallest element resides at a leaf.
- **kth largest element in max-heap**: for 2 ≤ k ≤ ⌊n/2⌋, resides at levels 1 through k-1.
- **Sorted increasing array as min-heap**: Yes.
- **MAX-HEAPIFY on > heap-size/2**: does nothing (node is a leaf, both children are beyond heap-size).
- **Calling MAX-HEAPIFY when A[i] ≥ children**: no effect, already max-heap.

### 6.6 Comparisons
| Property | Heapsort | Merge Sort | Insertion Sort | Quicksort |
|---|---|---|---|---|
| Worst-case time | O(n lg n) | O(n lg n) | O(n²) | O(n²) |
| Best-case time | Ω(n lg n) | Ω(n lg n) | O(n) | Ω(n lg n) |
| In-place | Yes | No | Yes | Yes |
| Stable | No | Yes | Yes | No |
| Extra space | O(1) | O(n) | O(1) | O(lg n) stack |

### 6.7 Visual Patterns
- **Fig 6.1**: Max-heap binary tree ↔ array, parent-child arrows, height=3, node at index 4 has height 1.
- **Fig 6.2**: MAX-HEAPIFY(A,2) on 10-element heap — blue node violates property, floats down through 3 levels.
- **Fig 6.3**: BUILD-MAX-HEAP on 10 elements — nodes 5→4→3→2→1 are processed bottom-up.
- **Fig 6.4**: HEAPSORT — tan region = sorted suffix, blue = remaining heap. After each swap + heapify.

### 6.8 Cross-Chapter Dependencies
- Priority queues used in **Ch 15** (amortized analysis), **Ch 21** (minimum spanning trees), **Ch 22** (shortest paths) with min-heaps.
- Fibonacci heaps (**Ch 16**) improve INSERT and DECREASE-KEY to O(1) amortized.
- Van Emde Boas trees (**Ch 20**) support O(lg lg n) operations.

### 6.9 People & Dates
- **Williams (1964)**: invented heapsort algorithm and heap-based priority queues.
- **Floyd (1964)**: suggested BUILD-MAX-HEAP (linear-time bottom-up construction).
- **Schaffer & Sedgewick**: best-case ~(n/2)lg n moves, average ~n lg n moves.

### 6.10 Proof Patterns
- **Loop invariant for BUILD-MAX-HEAP**: nodes i+1..n are roots of max-heaps.
- **Master Theorem case 2**: `T(n) = T(2n/3) + Θ(1)` → T(n) = O(lg n).
- **Height-based bound**: sum_{h=0}^{⌊lg n⌋} ⌈n/2^{h+1}⌉ · O(h) = O(n).

### 6.11 Problems
- **6-1 Building a heap using insertion**: BUILD-MAX-HEAP′ (insertion-based) vs standard. Counterexample shows they differ. Worst-case Θ(n lg n) for insertion method.
- **6-2 d-ary heaps**: height = ⌈log_d(n(d-1)+1)⌉ - 1 or Θ(log_d n). EXTRACT-MAX: O(d log_d n). INCREASE-KEY: O(log_d n). INSERT: O(log_d n).
- **6-3 Young tableaus**: m×n matrix with rows/cols sorted. EXTRACT-MIN in O(m+n). Insert in O(m+n). Sort n² numbers in O(n³). Search in O(m+n).

---

## Chapter 7: Quicksort

### 7.1 Named Entities & Definitions
- **Pivot**: element selected to partition the array.
- **Low side**: elements ≤ pivot, in A[p:q-1].
- **High side**: elements ≥ pivot, in A[q+1:r].
- **Tail recursion elimination**: replacing the second recursive call with iteration to reduce stack depth.

### 7.2 Algorithm: QUICKSORT
```
QUICKSORT(A, p, r)
1 if p < r
2     q = PARTITION(A, p, r)
3     QUICKSORT(A, p, q-1)
4     QUICKSORT(A, q+1, r)
```

### 7.3 Algorithm: PARTITION (Lomuto)
```
PARTITION(A, p, r)
1 x = A[r]          // pivot
2 i = p - 1
3 for j = p to r-1
4     if A[j] ≤ x
5         i = i + 1
6         exchange A[i] ↔ A[j]
7 exchange A[i+1] ↔ A[r]
8 return i + 1
```
- **Time**: Θ(n) for subarray of size n.
- **Loop invariant** (for any index k):
  1. if p ≤ k ≤ i: A[k] ≤ x
  2. if i+1 ≤ k ≤ j-1: A[k] > x
  3. if k = r: A[k] = x

**Concrete example**: `A = [13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11]`, p=1, r=12, pivot=11:
- i=0, j=1: A[1]=13>11 → do nothing, j=2
- j=2: A[2]=19>11 → j=3
- j=3: A[3]=9≤11 → i=1, swap A[1]↔A[3] → [9,19,13,5,...], j=4
- j=4: A[4]=5≤11 → i=2, swap A[2]↔A[4] → [9,5,13,19,...], j=5
- j=5: A[5]=12>11 → j=6
- j=6: A[6]=8≤11 → i=3, swap A[3]↔A[6] → [9,5,8,19,12,13,7,...], j=7
- j=7: A[7]=7≤11 → i=4, swap A[4]↔A[7] → [9,5,8,7,12,13,19,4,...], j=8
- j=8: A[8]=4≤11 → i=5, swap A[5]↔A[8] → [9,5,8,7,4,13,19,12,21,2,6,11], j=9
- j=9: A[9]=21>11 → j=10
- j=10: A[10]=2≤11 → i=6, swap A[6]↔A[10] → [9,5,8,7,4,2,19,12,21,13,6,11], j=11
- j=11: A[11]=6≤11 → i=7, swap A[7]↔A[11] → [9,5,8,7,4,2,6,12,21,13,19,11]
- j=12: loop ends. Swap A[8]↔A[12] → [9,5,8,7,4,2,6,11,21,13,19,12]
- return q=8

### 7.4 Randomized Version
```
RANDOMIZED-PARTITION(A, p, r)
1 i = RANDOM(p, r)
2 exchange A[r] ↔ A[i]
3 return PARTITION(A, p, r)

RANDOMIZED-QUICKSORT(A, p, r)
1 if p < r
2     q = RANDOMIZED-PARTITION(A, p, r)
3     RANDOMIZED-QUICKSORT(A, p, q-1)
4     RANDOMIZED-QUICKSORT(A, q+1, r)
```

### 7.5 Performance Analysis

#### Worst-case (deterministic or randomized)
- Recurrence: `T(n) = T(n-1) + Θ(n) = Θ(n²)`
- Occurs when partition produces one subproblem of size n-1 and one of size 0.
- Examples: already sorted ascending (with last-element pivot), sorted descending.

#### Best-case
- Recurrence: `T(n) = 2T(n/2) + Θ(n) = Θ(n lg n)`
- Even split: both subproblems ≤ n/2.

#### Balanced partitioning (constant proportion)
- 9-to-1 split: `T(n) = T(9n/10) + T(n/10) + Θ(n)`
- Recursion tree depth: log_{10/9} n = Θ(lg n), each level cost ≤ n.
- Running time: O(n lg n) for any split of constant proportionality.

#### Average-case (randomized, distinct elements)
- Expected time: O(n lg n), using indicator random variables.
- **Key lemma**: For z_i < z_j, Pr[z_i compared with z_j] = 2/(j-i+1).
- **Indicator variables**: X_{ij} = I{z_i compared with z_j}
- Expected comparisons: E[X] = Σ_{i=1}^{n-1} Σ_{j=i+1}^{n} 2/(j-i+1) = O(n lg n)
  - Let k = j-i: Σ_{i=1}^{n-1} Σ_{k=1}^{n-i} 2/(k+1) < Σ_{i=1}^{n-1} 2·H_n = O(n lg n)
- **Theorem 7.4**: Expected running time of RANDOMIZED-QUICKSORT = O(n lg n).

#### Lemma 7.1
- Running time of QUICKSORT = O(n + X) where X = number of element comparisons.
- At most n calls to PARTITION, each comparison is in the for loop.

#### Lemma 7.2
- z_i and z_j are compared iff the first pivot chosen from Z_{ij} = {z_i,...,z_j} is either z_i or z_j.
- No pair is compared twice.

#### Lemma 7.3
- Pr[z_i compared with z_j] = 2/(j-i+1).

### 7.6 Edge Cases
- **All elements equal**: PARTITION returns q = r (with standard code). QUICKSORT degrades to Θ(n²).
- **All elements distinct, sorted**: worst-case Θ(n²) for deterministic last-element pivot.
- **All elements distinct, reverse sorted**: worst-case Θ(n²).
- **Almost-sorted**: insertion sort beats quicksort (Exercise 7.2-4).
- **Modifying PARTITION for equal values**: Problem 7-2 introduces PARTITION′ returning two indices (q,t) where A[q:t] are all equal.

### 7.7 Classifications
| Sort Type | Worst Case | Average Case | Best Case | In-Place | Stable |
|---|---|---|---|---|---|
| Deterministic Quicksort | Θ(n²) | Θ(n lg n) | Θ(n lg n) | Yes | No |
| Randomized Quicksort | Θ(n²) | Θ(n lg n) | Θ(n lg n) | Yes | No |
| Merge Sort | Θ(n lg n) | Θ(n lg n) | Θ(n lg n) | No | Yes |
| Heapsort | Θ(n lg n) | Θ(n lg n) | Θ(n lg n) | Yes | No |
| Insertion Sort | Θ(n²) | Θ(n²) | O(n) | Yes | Yes |

### 7.8 Visual Patterns
- **Fig 7.1**: PARTITION on 8-element array — 4 regions (tan ≤ x, blue > x, white unknown, yellow pivot). Shows swapping process.
- **Fig 7.2**: Four regions maintained by PARTITION: A[p:i] ≤ x (tan), A[i+1:j-1] > x (blue), A[j:r-1] unknown (white), A[r] = x (yellow).
- **Fig 7.3**: Two cases per iteration: (a) A[j] > x → increment j; (b) A[j] ≤ x → increment i, swap A[i]↔A[j], increment j.
- **Fig 7.4**: Recursion tree for 9-to-1 split — per-level costs = n, depth = Θ(lg n).
- **Fig 7.5**: Bad split then good split — combining costs yields same asymptotic as good split alone.

### 7.9 Hoare Partition (Problem 7-1)
```
```
- Returns j where p ≤ j < r.
- Every element in A[p:j] ≤ every element in A[j+1:r].
- Pivot may end up in either partition (unlike Lomuto where pivot is isolated).
- Advantage: fewer swaps when many equal elements.

### 7.10 Problems
- **7-1 Hoare partition correctness**: indices stay in bounds; p ≤ j < r; partition property holds.
- **7-2 Quicksort with equal elements**: partition into < = > regions. Expected time O(n lg n) even with equal values.
- **7-3 Alternative analysis**: E[T(n)] = (1/n) Σ_{q=0}^{n-1} (E[T(q)] + E[T(n-q-1)]) + Θ(n); solves to O(n lg n).
- **7-4 Stooge sort**: T(n) = 3T(2n/3) + Θ(1) → Θ(n^{log_{3/2} 3}) ≈ Θ(n^{2.71}). Worse than all practical sorts.
- **7-5 Stack depth**: TRE-QUICKSORT can have Θ(n) stack depth. Fix: sort smaller side recursively, larger iteratively → Θ(lg n) depth.
- **7-6 Median-of-3 partition**: p_i = (i-1)(n-i) / C(n,3). Improves probability of good split.
- **7-7 Fuzzy sorting**: handles overlapping intervals; Θ(n lg n) general, Θ(n) when all overlap.

### 7.11 People & Dates
- **C.A.R. Hoare (1962)**: invented quicksort.
- **N. Lomuto**: Lomuto partition (used in Section 7.1).
- **Bentley & McIlroy**: engineering quicksort, killer adversary.

---

## Chapter 8: Sorting in Linear Time

### 8.1 Lower Bounds for Sorting

#### Decision Tree Model
- Full binary tree representing comparisons of a sorting algorithm on n elements.
- Each internal node labeled `i:j` (compare a_i vs a_j).
- Each leaf labeled with permutation 〈π(1),π(2),...,π(n)〉.
- Path from root to leaf = execution of the sort.
- n! permutations → at least n! reachable leaves.

#### Theorem 8.1: Comparison Sort Lower Bound
- **Statement**: Any comparison sort requires Ω(n lg n) comparisons in the worst case.
- **Proof**: Height h of decision tree. n! ≤ l ≤ 2^h → h ≥ lg(n!) = Ω(n lg n).
- Uses Stirling: lg(n!) = n lg n - n lg e + Θ(lg n).

#### Corollary 8.2
- Heapsort and merge sort are asymptotically optimal comparison sorts.

#### Lemma: lg(n!) bounds
- **Lower**: lg(n!) ≥ (n/2) lg(n/2) = Ω(n lg n) (first n/2 terms ≥ n/2).
- **Upper**: lg(n!) ≤ n lg n (each term ≤ n).

### 8.2 Counting Sort

**Assumption**: Input integers in range 0 to k.
**Time**: Θ(n + k). When k = O(n), time = Θ(n).

```
COUNTING-SORT(A, n, k)
1 let B[1:n] and C[0:k] be new arrays
2 for i = 0 to k
3     C[i] = 0
4 for j = 1 to n
5     C[A[j]] = C[A[j]] + 1
6 // C[i] now = count of elements equal to i
7 for i = 1 to k
8     C[i] = C[i] + C[i-1]
9 // C[i] now = count of elements ≤ i
10 for j = n down to 1
11     B[C[A[j]]] = A[j]
12     C[A[j]] = C[A[j]] - 1
13 return B
```

**Stable**: elements with same value appear in output in the same order as input. Critical for radix sort.

**Concrete example**: A = [2,5,3,0,2,3,0,3], n=8, k=5:
- After line 5: C = [2,0,2,3,0,1] (counts of 0,1,2,3,4,5)
- After line 8: C = [2,2,4,7,7,8] (cumulative ≤)
- Process j=8→1:
  - j=8: A[8]=3, C[3]=7 → B[7]=3, C[3]=6
  - j=7: A[7]=0, C[0]=2 → B[2]=0, C[0]=1
  - j=6: A[6]=3, C[3]=6 → B[6]=3, C[3]=5
  - j=5: A[5]=2, C[2]=4 → B[4]=2, C[2]=3
  - j=4: A[4]=0, C[0]=1 → B[1]=0, C[0]=0
  - j=3: A[3]=3, C[3]=5 → B[5]=3, C[3]=4
  - j=2: A[2]=5, C[5]=8 → B[8]=5, C[5]=7
  - j=1: A[1]=2, C[2]=3 → B[3]=2, C[2]=2
- B = [0,0,2,2,3,3,3,5]

### 8.3 Radix Sort

**Assumption**: Numbers have d digits, each in range 0..k-1.
**Method**: Sort on least significant digit first, using a stable sort.

```
RADIX-SORT(A, n, d)
1 for i = 1 to d
2     use a stable sort to sort array A on digit i
```

#### Lemma 8.3
- **Statement**: Given n d-digit numbers with each digit ≤ k possible values, RADIX-SORT correctly sorts in Θ(d(n+k)) time (if stable sort uses Θ(n+k) time).
- **Proof**: By induction on digit position. Induction needs stable sort to preserve previous digit ordering.

#### Lemma 8.4
- **Given n b-bit numbers, choose r ≤ b**: view as d = ⌈b/r⌉ digits of r bits each.
- Running time: Θ((b/r)(n + 2^r)).
- If b < ⌊lg n⌋: choose r = b → Θ(n).
- If b ≥ ⌊lg n⌋: choose r = ⌊lg n⌋ → Θ(bn/lg n).

**Concrete example**: 7 three-digit numbers:
- Input: [329, 457, 657, 839, 436, 720, 355]
- Sort on digit 1 (units): [720, 355, 436, 457, 657, 329, 839]
- Sort on digit 2 (tens): [720, 329, 436, 839, 355, 457, 657]
- Sort on digit 3 (hundreds): [329, 355, 436, 457, 657, 720, 839] ✓

#### Radix sort vs Quicksort
- When b = O(lg n), radix sort is Θ(n) vs quicksort Θ(n lg n).
- Radix sort has higher constant factors, not in-place, worse cache behavior.
- Choice depends on implementation, machine, and data characteristics.

### 8.4 Bucket Sort


```
```

- Let n_i = number of elements in bucket i.
- Running time: T(n) = Θ(n) + Σ_{i=0}^{n-1} O(n_i²)
- E[T(n)] = Θ(n) + Σ O(E[n_i²]) = Θ(n) + n·O(2-1/n) = Θ(n)
- Proof: n_i ~ Binomial(n, 1/n), so E[n_i] = 1, Var[n_i] = 1-1/n, E[n_i²] = 2-1/n.


- Bucket 0: [.12] (.12)
- Bucket 1: [.17] (.17)
- Bucket 2: [.21, .23, .26] → sorted: [.21, .23, .26]
- Bucket 3: [.39] (.39)
- Bucket 4: empty
- Bucket 5: empty
- Bucket 6: [.68] (.68)
- Bucket 7: [.72, .78] → sorted: [.72, .78]
- Bucket 8: empty
- Bucket 9: [.94] (.94)
- Concatenated: [.12, .17, .21, .23, .26, .39, .68, .72, .78, .94]

#### Edge case: non-uniform distribution
- Bucket sort still linear if Σ n_i² = O(n).

### 8.5 Visual Patterns
- **Fig 8.1**: Decision tree for Insertion Sort on 3 elements. Height=3, leaves=6 (=3!). Traced path for input [6,8,5].
- **Fig 8.2**: COUNTING-SORT on 8 elements, k=5. Shows C[] at each stage; reverse pass produces stable output.
- **Fig 8.3**: Radix sort on 7 three-digit numbers — 3 passes, stable sort each pass.
- **Fig 8.4**: Bucket sort on 10 elements — 10 buckets, each bucket sorted individually.

### 8.6 Theorems & Lemmas Summary
| # | Statement |
|---|---|
| Theorem 8.1 | Any comparison sort requires Ω(n lg n) comparisons in worst case |
| Corollary 8.2 | Heapsort and merge sort are asymptotically optimal comparison sorts |
| Lemma 8.3 | Radix sort runs in Θ(d(n+k)) with stable sort |
| Lemma 8.4 | Radix sort on b-bit numbers with r-bit digits: Θ((b/r)(n+2^r)) |

### 8.7 Key Properties
- **Stable sort**: equal keys retain input order. Stable: insertion, merge, counting, bucket (if stable sub-sort). Unstable: heapsort, quicksort.
- **Making any comparison sort stable**: store original index as secondary key, compare index on tie. Adds O(n) space, O(1) extra time per comparison.
- **0-1 sorting lemma (Problem 8-7)**: If an oblivious compare-exchange algorithm sorts all 0-1 sequences, it sorts all sequences.

### 8.8 Problems
- **8-1 Probabilistic lower bound**: External path length D(T) minimized when tree is balanced; average-case = Ω(n lg n).
- **8-2 Sorting in place in linear time**: (a) stable O(n): counting sort. (b) in-place O(n): partition. (c) in-place stable O(n): tricky, use cyclic rotations. (d) in-place for radix: need key-indexed counting.
- **8-3 Variable-length items**: sort by length first (bucket), then stable sort per bucket using counting sort on most significant position.
- **8-4 Water jugs**: pairing problem. Deterministic Θ(n²), lower bound Ω(n lg n), randomized O(n lg n) using quicksort-like partitioning.
- **8-5 Average sorting (k-sorted)**: A[i] ≤ A[i+k]. k-sort in O(n lg(n/k)). Sort k-sorted in O(n lg k).
- **8-6 Lower bound on merging sorted lists**: 2n-1 comparisons needed in worst case. If two elements are consecutive in sorted order and from different lists, they must be compared.
- **8-7 0-1 sorting lemma and columnsort**: 8 steps, r ≥ 2s², r even, s divides r. Column-major order.

### 8.9 People & Dates
- **H.H. Seward (1954)**: invented counting sort + combining with radix sort.
- **L.J. Comrie (1929)**: first published reference to LSD radix sort.
- **Isaac & Singleton (1956)**: bucket sort.
- **Leighton**: columnsort algorithm (Problem 8-7).

---

## Chapter 9: Medians and Order Statistics

### 9.1 Named Entities & Definitions
- **i-th order statistic**: the i-th smallest element.
- **Minimum**: 1st order statistic.
- **Maximum**: nth order statistic.
- **Median**: lower median = ⌊(n+1)/2⌋, upper median = ⌈(n+1)/2⌉.
- **Selection problem**: Input: set A of n distinct numbers, integer i (1≤i≤n). Output: element x ∈ A larger than exactly i-1 others.
- **Weighted median**: element x_k such that sum of weights of elements < x_k < 1/2 and sum of weights > x_k ≤ 1/2.

### 9.2 Minimum and Maximum

#### Finding minimum: n-1 comparisons
```
MINIMUM(A, n)
1 min = A[1]
2 for i = 2 to n
3     if min > A[i]
4         min = A[i]
5 return min
```
- **Lower bound**: n-1 comparisons (each non-winner must lose at least once).

#### Simultaneous min & max: 3⌊n/2⌋ comparisons
- Process elements in pairs.
- Compare the 2 elements in each pair (1 comparison), then compare smaller with current min and larger with current max (2 comparisons) = 3 per 2 elements.
- If n odd: initialize min=max=first, process rest in pairs → 3⌊n/2⌋ comparisons.
- If n even: 1 comparison on first 2 to set min/max, then 3(n-2)/2 comparisons → total 3n/2-2.

### 9.3 Randomized Selection (Expected Linear)

```
RANDOMIZED-SELECT(A, p, r, i)
1 if p == r
2     return A[p]
3 q = RANDOMIZED-PARTITION(A, p, r)
4 k = q - p + 1
5 if i == k
6     return A[q]
7 elseif i < k
8     return RANDOMIZED-SELECT(A, p, q-1, i)
9 else
10    return RANDOMIZED-SELECT(A, q+1, r, i-k)
```

#### Theorem 9.2: Expected running time = Θ(n)
- **Proof using generations**:
  - Define "helpful" partitioning if |A(j)| ≤ (3/4)|A(j-1)|.
  - Lemma 9.1: partitioning is helpful with Pr ≥ 1/2.
  - Break into generations, each starting with a helpful partition.
  - Let X_k = number of sets in generation k. E[X_k] ≤ 2 (geometric distribution).
  - Total comparisons < Σ_k n_k · X_k where n_k ≤ (3/4)^k n_0.
  - E[comparisons] < n_0 Σ (3/4)^k · 2 = 2n_0 · 1/(1-3/4) = 8n_0.

#### Lemma 9.1
- A partitioning is helpful with probability at least 1/2.
- "Middle half" = all elements except first ⌈n/4⌉-1 and last ⌈n/4⌉-1.
- Pivot in middle half → at least ⌈n/4⌉ elements removed.
- Pr[not in middle half] ≤ 2(⌈n/4⌉-1)/n < 1/2.

#### Worst-case: Θ(n²)
- Extremely unlucky: always partition around largest remaining element.

### 9.4 Deterministic Selection (Worst-Case Linear) — SELECT

#### Algorithm (median of medians)
```
SELECT(A, p, r, i)
1 while (r-p+1) mod 5 ≠ 0
2     for j = p+1 to r
3         if A[p] > A[j]: exchange A[p] ↔ A[j]
4     if i == 1: return A[p]
5     p = p + 1; i = i - 1
6 g = (r-p+1)/5
7 for j = p to p+g-1
8     sort group 〈A[j], A[j+g], A[j+2g], A[j+3g], A[j+4g]〉 in place
9 // Group medians now in A[p+2g : p+3g-1]
10 x = SELECT(A, p+2g, p+3g-1, ⌈g/2⌉)   // median of medians
11 q = PARTITION-AROUND(A, p, r, x)
12 k = q - p + 1
13 if i == k: return A[q]
14 elseif i < k: return SELECT(A, p, q-1, i)
15 else: return SELECT(A, q+1, r, i-k)
```

#### Key ideas
- Groups of 5 elements → g = n/5 groups.
- Find median of each group → Θ(1) per group, Θ(n) total.
- Recursively find median of the g medians → T(n/5).
- Pivot (median of medians) guarantees at least 3g/2 elements ≤ pivot and ≥ 3g/2 elements ≥ pivot.
- Each recursive call on at most n - 3g/2 = n - 3n/10 = 7n/10 elements.

#### Recurrence and Theorem 9.3
- T(n) ≤ T(n/5) + T(7n/10) + Θ(n)
- Solve by substitution: assume T(n) ≤ cn for all smaller values.
- T(n) ≤ c(n/5) + c(7n/10) + Θ(n) = 9cn/10 + Θ(n) = cn - cn/10 + Θ(n) ≤ cn for sufficiently large c.

#### Visual Pattern (Fig 9.3)
- g columns of 5 elements each, sorted vertically (bottom = min, top = max).
- Group medians in red, arranged left to right by median value.
- Pivot x = median of medians (center red element).
- Blue background: ≤ x (includes 3 group medians from left groups plus their 2 lower elements each).
- Yellow background: ≥ x (includes 3 group medians from right groups plus their 2 upper elements each).
- White background: ambiguous elements.
- At least 3g/2 elements guaranteed on each side of partition.

### 9.5 Classifications
| Algorithm | Worst-case | Expected | Type |
|---|---|---|---|
| MINIMUM | Θ(n) | — | Deterministic |
| MIN+MAX | Θ(n) | — | Deterministic |
| RANDOMIZED-SELECT | Θ(n²) | Θ(n) | Randomized |
| SELECT (median-of-medians) | Θ(n) | — | Deterministic |

### 9.6 Edge Cases
- **Worst-case RANDOMIZED-SELECT sequence**: A=[2,3,0,5,7,9,1,8,6,4], selecting min: if pivots are always the largest remaining (2,3,4,5,6,7,8,9), each step removes 1 element.
- **Base case correctness**: RANDOMIZED-SELECT never recurses on 0-length array (Exercise 9.2-1).
- **SELECT with groups of 3**: does NOT yield linear time — recurrence T(n) = T(n/3) + T(2n/3) + Θ(n) → T(n) = O(n lg n).

### 9.7 SELECT with groups of 7
- Works in linear time: groups of size 7 → at least 4g/2 = 4⌊g/2⌋ elements eliminated per side.
- General: groups of odd size > 3 → linear.

### 9.8 Comparisons
| Aspect | Sorting then indexing | RANDOMIZED-SELECT | SELECT (median-of-medians) |
|---|---|---|---|
| Time | O(n lg n) | Θ(n) expected | Θ(n) worst-case |
| In-place | No (merge) or yes (heap) | Yes (in-place partition) | Yes |
| Practicality | Good | Very good (small constants) | Poor (large constants, mostly theoretical) |
| Randomization | Not needed | Yes | No |

### 9.9 Connected problems
- **Post-office location problem (9-7)**: minimize Σ w_i·|x_i - p| → optimal p = weighted median.
- **k-th quantiles**: find k-1 order statistics dividing set into k equal parts. O(n lg k) time.
- **k numbers closest to median**: find median (SELECT), then find k nearest using SELECT on absolute differences.
- **Median of two sorted arrays**: O(lg n) using binary search on indices.

### 9.10 Key Formulas
| Formula | Description |
|---|---|
| E[X] = Σ_{i<j} 2/(j-i+1) ≤ 2n·H_n = O(n lg n) | Expected comparisons in randomized quicksort |
| E[SELECT] = Θ(n) | Expected running time of randomized selection |
| T_SELECT(n) ≤ T(n/5) + T(7n/10) + Θ(n) | Worst-case recurrence for SELECT |
| 3⌊n/2⌋ | Comparisons for simultaneous min & max |
| n + ⌈lg n⌉ - 2 | Comparisons to find 2nd smallest |

### 9.11 Problems
- **9-1 Largest i numbers in sorted order**: (a) sort O(n lg n); (b) max-priority queue O(n + i lg n); (c) SELECT + sort O(n + i lg i).
- **9-2 Simplified randomized selection**: may not terminate in worst case (pivot = q, infinite loop). Expected time still O(n).
- **9-3 Weighted median**: generalizes median. Compute in O(n) using SELECT. Weighted median solves 1D post-office location.
- **9-4 Small order statistics**: when i is small, U_i(n) = n + O(S(2i) lg(n/i)).
- **9-5 Alternative analysis using indicator variables**: E[X_{ijk}] depends on relative ordering of i, j, k. Total E[X_i] ≤ 4n.
- **9-6 SELECT with groups of 3**: O(n lg n) upper bound. SELECT3 with nested medians (groups of 3, then subgroups of 3) achieves O(n).

### 9.12 People & Dates
- **Blum, Floyd, Pratt, Rivest, Tarjan (1973)**: worst-case linear-time median algorithm.
- **Hoare (1961)**: RANDOMIZED-SELECT (also quicksort inventor).
- **Floyd & Rivest**: improved randomized selection.
- **Dor & Zwick**: upper bound ≈2.95n, lower bound (2+ε)n comparisons for median.
- **Bent & John**: lower bound 2n comparisons for median.
- **Schönhage, Paterson, Pippenger**: upper bound 3n comparisons for median.

---

## Cross-Chapter Summary

| Concept | Ch 6 | Ch 7 | Ch 8 | Ch 9 |
|---|---|---|---|---|
| Sorting algorithm | Heapsort | Quicksort | Counting/Radix/Bucket | — |
| Time (worst) | Θ(n lg n) | Θ(n²) | Θ(n) linear | — |
| Time (avg) | Θ(n lg n) | Θ(n lg n) | Θ(n) | — |
| In-place | Yes | Yes | No (most) | N/A |
| Comparison-based | Yes | Yes | No | N/A |
| Key technique | Heap data structure | Divide & conquer, randomization | Non-comparison, stable sub-sort | Median-of-medians |
| Selection algorithm | Priority queue | — | — | SELECT |
| Extra space | O(1) | O(lg n) stack | O(k) or O(n) | O(1) |

---

*End of CLRS Chapters 6–9 Comprehensive Study Guide*

# CLRS 4th Ed — Comprehensive Study Guide: Chapters 10–13

---

## Ch. 10 — Elementary Data Structures

### Named Entities

- **Array**: contiguous sequence of bytes; i-th element at address `a + b(i - s)` (s=1-origin) or `a + bi` (s=0); O(1) access via RAM model
- **Row-major order**: matrix stored row by row; index `s + n(i - s) + (j - s)` for s-origin; s=1: `n(i-1)+j`; s=0: `ni+j`
- **Column-major order**: matrix stored column by column; index `s + m(j - s) + (i - s)` for s-origin; s=1: `i+m(j-1)`; s=0: `i+mj`
- **Block representation**: matrix divided into blocks, each stored contiguously
- **Stack**: LIFO policy; INSERT=PUSH, DELETE=POP
- **Queue**: FIFO policy; INSERT=ENQUEUE, DELETE=DEQUEUE
- **Deque**: double-ended queue; insert/delete at both ends
- **Linked list**: linear order via pointers (not indices)
- **Singly linked list**: each element has `next` pointer only
- **Doubly linked list**: each element has `next` and `prev` pointers
- **Circular list**: `prev` of head points to tail, `next` of tail points to head
- **Sorted list**: linear order matches key order
- **Unsorted list**: elements in any order
- **Sentinel (L.nil)**: dummy object eliminating boundary conditions; circular, doubly linked list with sentinel uses only one pointer-type object for all NIL references
- **Rooted tree**: nodes with parent/child pointers
- **Binary tree**: each node has `p`, `left`, `right`
- **Left-child, right-sibling representation**: for arbitrary branching; each node has `left-child` (first child) and `right-sibling` (next sibling)
- **Compact list**: singly linked list stored in arrays `key[1..n]` and `next[1..n]`, only first n positions used

### Processes/Algorithms

#### STACK-EMPTY(S)
```
1 if S.top == 0
2     return TRUE
3 else return FALSE
```
Time: O(1)

#### PUSH(S, x)
```
1 if S.top == S.size
2     error "overflow"
3 else S.top = S.top + 1
4     S[S.top] = x
```
Time: O(1)

#### POP(S)
```
1 if STACK-EMPTY(S)
2     error "underflow"
3 else S.top = S.top - 1
4     return S[S.top + 1]
```
Time: O(1)

**Example**: Stack S[1:6], initially empty. Sequence: PUSH(S,4), PUSH(S,1), PUSH(S,3), POP(S), PUSH(S,8), POP(S).
- Start: top=0
- push 4: top=1, S[1]=4
- push 1: top=2, S[2]=1
- push 3: top=3, S[3]=3
- pop: returns 3, top=2
- push 8: top=3, S[3]=8
- pop: returns 8, top=2
Final stack: bottom [4, 1] top

#### ENQUEUE(Q, x)
```
1 Q[Q.tail] = x
2 if Q.tail == Q.size
3     Q.tail = 1
4 else Q.tail = Q.tail + 1
```
Time: O(1)

#### DEQUEUE(Q)
```
1 x = Q[Q.head]
2 if Q.head == Q.size
3     Q.head = 1
4 else Q.head = Q.head + 1
5 return x
```
Time: O(1)

**Example**: Queue Q[1:6], initially empty (head=tail=1). Sequence: ENQUEUE(Q,4), ENQUEUE(Q,1), ENQUEUE(Q,3), DEQUEUE(Q), ENQUEUE(Q,8), DEQUEUE(Q).
- enq 4: Q[1]=4, tail=2
- enq 1: Q[2]=1, tail=3
- enq 3: Q[3]=3, tail=4
- deq: returns 4, head=2
- enq 8: Q[4]=8, tail=5
- deq: returns 1, head=3
Final queue: head→[1,3,8]←tail (positions 3,4,5)

#### LIST-SEARCH(L, k)
```
1 x = L.head
2 while x ≠ NIL and x.key ≠ k
3     x = x.next
4 return x
```
Time: Θ(n) worst case

#### LIST-PREPEND(L, x)
```
1 x.next = L.head
2 x.prev = NIL
3 if L.head ≠ NIL
4     L.head.prev = x
5 L.head = x
```
Time: O(1)

#### LIST-INSERT(x, y) — insert x after y
```
1 x.next = y.next
2 x.prev = y
3 if y.next ≠ NIL
4     y.next.prev = x
5 y.next = x
```
Time: O(1)

#### LIST-DELETE(L, x)
```
1 if x.prev ≠ NIL
2     x.prev.next = x.next
3 else L.head = x.next
4 if x.next ≠ NIL
5     x.next.prev = x.prev
```
Time: O(1) (given pointer to x); Θ(n) if searching by key first

#### LIST-DELETE'(x) — with sentinel
```
1 x.prev.next = x.next
2 x.next.prev = x.prev
```
No boundary checks needed.

#### LIST-INSERT'(x, y) — with sentinel
```
1 x.next = y.next
2 x.prev = y
3 y.next.prev = x
4 y.next = x
```

#### LIST-SEARCH'(L, k) — sentinel-optimized
```
1 L.nil.key = k          // store key in sentinel (guarantees it's in list)
2 x = L.nil.next         // start at head
3 while x.key ≠ k
4     x = x.next
5 if x == L.nil
6     return NIL          // k was not in list
7 else return x           // found k
```
One comparison per iteration instead of two. Time: Θ(n) worst case, but lower constants.

#### COMPACT-LIST-SEARCH (probabilistic skip)
```
COMPACT-LIST-SEARCH(key, next, head, n, k)
1 i = head
2 while i ≠ NIL and key[i] < k
3     j = RANDOM(1, n)
4     if key[i] < key[j] and key[j] ≤ k
5         i = j
6     if key[i] == k
7         return i
8     i = next[i]
9 if i == NIL or key[i] > k
10     return NIL
11 else return i
```
Expected running time: O(√n)

### Data Structures — Operations Table

| Structure | SEARCH | INSERT | DELETE | SUCCESSOR/PRED | MIN/MAX | Space |
|-----------|--------|--------|--------|----------------|---------|-------|
| Array (direct access) | O(1) by index | — | — | — | — | O(n) |
| Stack (array) | — | O(1) PUSH | O(1) POP | — | — | O(n) |
| Queue (array) | — | O(1) ENQUEUE | O(1) DEQUEUE | — | — | O(n) |
| Unsorted singly linked list | Θ(n) | O(1) at head | Θ(n) (need prev) | Θ(n) | Θ(n) | O(n) |
| Sorted singly linked list | Θ(n) | O(n) | Θ(n) | O(1) if right ptr | O(1) min | O(n) |
| Unsorted doubly linked list | Θ(n) | O(1) | O(1) given ptr | O(1) from ptr | Θ(n) | O(n) |
| Sorted doubly linked list | Θ(n) | O(n) | O(1) given ptr | O(1) from ptr | O(1) min | O(n) |
| Circular doubly linked list w/ sentinel | Θ(n) | O(1) | O(1) | O(1) from ptr | Θ(n) | O(n) |

### Comparisons

| Dimension | Array | Linked List |
|-----------|-------|-------------|
| Linear order | Implicit (indices) | Explicit (pointers) |
| Access k-th element | O(1) | Θ(k) |
| Insert at beginning | Θ(n) (shift all) | O(1) |
| Delete first element | Θ(n) | O(1) |
| Memory per element | Element data only | Element + pointers (1 or 2) |
| Cache behavior | Good (contiguous) | Poor (scattered) |

| Dimension | Stack (Array) | Queue (Array) |
|-----------|---------------|---------------|
| Policy | LIFO | FIFO |
| Insert/Delete ends | Same end (top) | Different ends (head/tail) |
| Overflow condition | top == size | head == tail+1 (mod size) |
| Underflow condition | top == 0 | head == tail |
| Implementation | Single pointer top | Two pointers head, tail |

### Edge Cases

- **Stack overflow**: pushing onto full stack
- **Stack underflow**: popping from empty stack
- **Queue overflow**: enqueueing into full queue (size-1 elements max)
- **Queue underflow**: dequeueing from empty queue
- **Linked list**: deleting head/tail requires special cases; sentinel eliminates them
- **Sentinel memory waste**: for many small lists, sentinels waste significant space
- **Compact list**: assumes distinct keys; random skips do not help with repeated keys
- **Sentinel search edge**: if sentinel's key attribute must be NIL, store key before searching

### End-of-Chapter Material

**Exercises 10.1-1** through **10.1-8** on lines 9035-9074 cover:
- Binary representation of block-matrix indexing
- Stack operations sequence tracing
- Two stacks in one array
- Queue operations sequence tracing
- ENQUEUE/DEQUEUE with overflow/underflow checks
- Deque implementation with O(1) operations
- Queue with two stacks
- Stack with two queues

**Exercises 10.2-1** through **10.2-6** on lines 9247-9276 cover:
- Singly-linked DELETE is Θ(n), INSERT is O(1)
- Stack via singly linked list
- Queue via singly linked list
- UNION in O(1) via circular list
- Reverse singly linked list in Θ(n) with O(1) extra space
- XOR doubly linked list (space-saving, reversible in O(1))

**Exercises 10.3-1** through **10.3-6** on lines 9326-9364 cover:
- Drawing binary tree from attributes table
- Recursive print of binary tree O(n)
- Non-recursive print with stack O(n)
- Print arbitrary rooted tree (left-child right-sibling) O(n)
- Print binary tree non-recursively, O(1) extra space
- Two-pointer + boolean representation for parent/child access

**Problems** (lines 9365-9474):
- **10-1**: Comparisons among 4 list types (unsorted/sorted singly/doubly linked) — table of SEARCH, INSERT, DELETE, SUCCESSOR, PREDECESSOR, MINIMUM, MAXIMUM
- **10-2**: Mergeable heaps using linked lists (sorted, unsorted, disjoint)
- **10-3**: Searching a sorted compact list — COMPACT-LIST-SEARCH analysis proving O(√n) expected time

---

## Ch. 11 — Hash Tables

### Named Entities

- **Direct-address table**: array T[0..m-1] where slot k points to element with key k; O(1) operations
- **Hash table**: array of size m with hash function h: U → {0,...,m-1}
- **Hash function h**: maps universe U to slots; deterministic
- **Hash value h(k)**: slot where key k is stored
- **Collision**: two distinct keys hash to same slot
- **Independent uniform hashing (random oracle)**: each key maps to uniformly random independent slot
- **Load factor α**: α = n/m (n = #elements, m = #slots)
- **Chaining**: each slot points to linked list of colliding elements
- **Universal hashing**: family H where for any distinct k1,k2, Pr[h(k1)=h(k2)] ≤ 1/m
- **ε-universal**: collision probability ≤ ε
- **Uniform family**: for any key k, any slot q, Pr[h(k)=q] = 1/m
- **d-independent**: for any d distinct keys, hash values independent
- **Static hashing**: single fixed hash function (division or multiplication method)
- **Division method**: h(k) = k mod m
- **Multiplication method**: h(k) = ⌊m(kA mod 1)⌋ where 0<A<1
- **Multiply-shift method**: h_a(k) = (ka mod 2^w) ⋙ (w-ℓ); m=2^ℓ
- **Random hashing**: pick hash function randomly from family at runtime
- **Open addressing**: all elements stored in table itself; probe sequences
- **Probe sequence**: sequence of slots examined for insertion/search; permutation of {0,...,m-1}
- **Independent uniform permutation hashing**: each probe sequence equally likely any permutation
- **Double hashing**: h(k,i) = (h₁(k) + i·h₂(k)) mod m
- **Linear probing**: h(k,i) = (h₁(k) + i) mod m; special case of double hashing with h₂(k)=1
- **Primary clustering**: long runs of occupied slots in linear probing
- **Cryptographic hash function**: e.g., SHA-256; pseudorandom, fixed-length output
- **Wee hash function**: f_a(k) = swap((2k²+ak) mod 2^w); iterated r rounds; efficient in registers
- **Free list**: linked list of unused hash-table slots

### Processes/Algorithms

#### DIRECT-ADDRESS-SEARCH(T, k): return T[k] — O(1)
#### DIRECT-ADDRESS-INSERT(T, x): T[x.key] = x — O(1)
#### DIRECT-ADDRESS-DELETE(T, x): T[x.key] = NIL — O(1)

#### CHAINED-HASH-INSERT(T, x)
```
1 LIST-PREPEND(T[h(x.key)], x)
```
Time: O(1) worst case

#### CHAINED-HASH-SEARCH(T, k)
```
1 return LIST-SEARCH(T[h(k)], k)
```
Time: O(1+α) average under independent uniform hashing; Θ(n) worst case

#### CHAINED-HASH-DELETE(T, x)
```
1 LIST-DELETE(T[h(x.key)], x)
```
Time: O(1) if doubly linked (given element pointer, not key)

#### HASH-INSERT(T, k) — open addressing
```
1 i = 0
2 repeat
3     q = h(k, i)
4     if T[q] == NIL
5         T[q] = k
6         return q
7     else i = i + 1
8 until i == m
9 error "hash table overflow"
```

#### HASH-SEARCH(T, k) — open addressing
```
1 i = 0
2 repeat
3     q = h(k, i)
4     if T[q] == k
5         return q
6     i = i + 1
7 until T[q] == NIL or i == m
8 return NIL
```

#### LINEAR-PROBING-HASH-DELETE(T, q) — delete key at slot q
```
1 while TRUE
2     T[q] = NIL                           // make slot empty
3     q' = q                               // starting point for search
4     repeat
5         q' = (q' + 1) mod m
6         k' = T[q']
7         if k' == NIL
8             return                        // done
9     until g(k', q) < g(k', q')           // was empty slot q probed before q'?
10    T[q] = k'                             // move k' into slot q
11    q = q'                                 // free up slot q'
```
Uses inverse: g(k, q) = (q - h₁(k)) mod m

#### WEE hash function computation
```
ha,b,t,r(k) = WEE(k, a, b, t, r, m)

WEE(k, a, b, t, r, m)
1 u = ⌈t/w⌉
2 〈k₁, k₂, ..., kᵤ〉 = chop(k)
3 q = b
4 for i = 1 to u
5     q = f_a^(r)(q + k_i)
6 return q mod m
```
where f_a(k) = swap((2k² + ak) mod 2^w), and f_a^(r) means r iterations. One-to-one for odd a, any r≥0.

### Classifications

**Hash Functions:**
1. **Static hashing** (fixed function):
   - Division method: h(k) = k mod m (m prime, not near power of 2)
   - Multiplication method: h(k) = ⌊m(kA mod 1)⌋
   - Multiply-shift: h_a(k) = (ka mod 2^w) ⋙ (w-ℓ)

2. **Random hashing** (randomly chosen from family):
   - Universal: Pr[collision] ≤ 1/m
   - ε-universal: Pr[collision] ≤ ε
   - d-independent: hash of d distinct keys fully independent
   - Cryptographic: SHA-256; salt-based families h_a(k) = SHA-256(a‖k) mod m

3. **Wee hash**: register-only; 4 rounds recommended; extendable to variable-length

**Collision Resolution:**
1. **Chaining**: linked list per slot; α can be >1; pointers required
2. **Open addressing**: all in table; α ≤ 1; no pointers
   - Linear probing: h(k,i) = (h₁(k)+i) mod m; primary clustering; cache-friendly
   - Double hashing: h(k,i) = (h₁(k)+i·h₂(k)) mod m; Θ(m²) probe sequences

### Comparisons

| Dimension | Direct-Address | Chaining | Open Addressing |
|-----------|---------------|----------|-----------------|
| Table size | m = |U| | m ≈ n | m ≥ n |
| Load factor | n ≤ m | α = n/m any | α ≤ 1 |
| Worst-case search | O(1) | Θ(n) (all same slot) | O(m) |
| Avg unsuccessful search | O(1) | Θ(1+α) | ≤ 1/(1-α) |
| Avg successful search | O(1) | Θ(1+α) | ≤ (1/α) ln(1/(1-α)) |
| Deletion | O(1) | O(1) with doubly linked | Complex (DELETED marker) |
| Storage | O(|U|) | O(n+m) | O(m) |
| α = 0.5 unsucc search | — | Θ(1.5) | ≤ 2 probes |
| α = 0.5 succ search | — | Θ(1.5) | < 1.387 probes |
| α = 0.9 unsucc search | — | Θ(1.9) | ≤ 10 probes |
| α = 0.9 succ search | — | Θ(1.9) | < 2.559 probes |

### Data Structures — Operations Table

| Structure | SEARCH | INSERT | DELETE | Space |
|-----------|--------|--------|--------|-------|
| Direct-address table | O(1) | O(1) | O(1) | O(|U|) |
| Hash table (chaining, avg) | Θ(1+α) | O(1) | O(1)* | O(n+m) |
| Hash table (chaining, worst) | Θ(n) | O(1) | O(1)* | O(n+m) |
| Open addressing (avg, α<1) | ≤ 1/(1-α) | ≤ 1/(1-α) | varies | O(m) |
| * if doubly linked and given element pointer | | | | |

### Formulas

- **Array addressing** (s-origin): element i at `a + b(i-s)` through `a + b(i-s+1)-1`
- **Row-major index** (s=0): `ni + j`
- **Column-major index** (s=0): `i + mj`
- **Hash table load factor**: α = n/m
- **Division method**: h(k) = k mod m
- **Multiplication method**: h(k) = ⌊m(kA mod 1)⌋, where kA mod 1 = kA - ⌊kA⌋
- **Multiply-shift** (m=2^ℓ): h_a(k) = (ka mod 2^w) ⋙ (w-ℓ)
- **Double hashing**: h(k,i) = (h₁(k) + i·h₂(k)) mod m, with gcd(h₂(k), m)=1
- **Linear probing**: h(k,i) = (h₁(k) + i) mod m
- **Inverse for linear probing**: g(k, q) = (q - h₁(k)) mod m
- **Universal family (number theory)**: h_{ab}(k) = ((ak+b) mod p) mod m, a∈ℤ_p^*, b∈ℤ_p
- **Expected probes, unsuccessful search (open addressing)**: ≤ 1/(1-α)
- **Expected probes, successful search (open addressing)**: ≤ (1/α) ln(1/(1-α))
- **Wee hash**: f_a(k) = swap((2k²+ak) mod 2^w); f_a^(r) means r rounds
- **Wee hash for short input**: h_{a,b,t,r}(k) = f_a^(r)(k+b+2^t) mod m

### Rules/Laws/Theorems

**Theorem 11.1** — Unsuccessful search, chaining: Θ(1+α) average under independent uniform hashing.

**Theorem 11.2** — Successful search, chaining: Θ(1+α) average under independent uniform hashing.

**Corollary 11.3** — Universal hashing + chaining: sequence of s ops with n=O(m) inserts takes Θ(s) expected time.

**Theorem 11.4** — H_pm family (h_{ab}(k) = ((ak+b) mod p) mod m) is universal. Proof: r₁≠r₂ mod p (since a(k₁-k₂)≠0 mod p); one-to-one between (a,b) pairs and (r₁,r₂) pairs; collision probability ≤ 1/m.

**Theorem 11.5** — Multiply-shift family (odd a) is 2/m-universal.

**Theorem 11.6** — Unsuccessful search, open addressing: expected probes ≤ 1/(1-α) under independent uniform permutation hashing, no deletions, α<1.

**Corollary 11.7** — Insertion into open addressing: ≤ 1/(1-α) probes average, α<1.

**Theorem 11.8** — Successful search, open addressing: expected probes ≤ (1/α) ln(1/(1-α)) under independent uniform permutation hashing, no deletions, α<1.

**Theorem 11.9** — Linear probing: if h₁ is 5-independent and α ≤ 2/3, expected constant time per operation.

### Edge Cases

- **All keys hash to same slot**: Θ(n) search; worst-case for chaining
- **Hash table overflow**: open addressing when table full
- **Deletion in open addressing**: cannot just set to NIL; must use DELETED marker, or special algorithm for linear probing
- **Primary clustering**: linear probing builds long runs; avg search time increases
- **gcd(h₂(k), m) > 1**: double hashing only examines 1/d of table before repeating
- **Variable-length inputs**: need hash functions handling arbitrary length (wee hash, SHA-256)
- **Equal keys in compact list**: COMPACT-LIST-SEARCH analysis fails; random skips don't help asymptotically

### End-of-Chapter Material

**Exercises 11.1-1** through **11.1-4** (lines 9564-9593):
- 11.1-1: Find max in direct-address table; Θ(m) worst-case
- 11.1-2: Bit vector for dynamic set; O(1) operations
- 11.1-3: Direct-address with non-distinct keys; use linked list at each slot
- 11.1-4: Huge array with O(1) init; use additional stack array to track valid entries

**Exercises 11.2-1** through **11.2-6** (lines 9799-9832):
- 11.2-1: Expected collisions = C(n,2)/m under independent uniform hashing
- 11.2-2: Insert 5,28,19,15,20,33,12,17,10 with h(k)=k mod 9, chaining
- 11.2-3: Sorted chains: unsucc search Θ(1+α), succ search also; insert O(α); delete O(1+α)
- 11.2-4: Free list implementation; singly linked suffices
- 11.2-5: If |U| > (n-1)m, ∃ n keys all same hash ⇒ Θ(n) worst-case
- 11.2-6: Select random key in expected time O(L·(1+1/α))

**Exercises 11.3-1** through **11.3-6** (lines 10186-10218):
- 11.3-1: Use hash values to compare before full string comparison
- 11.3-2: Horner's rule for radix-128 division hash
- 11.3-3: h(k) = k mod (2^p-1) ⇒ string permutations hash to same value
- 11.3-4: Multiplication method with A=(√5-1)/2, m=1000; compute locations for 61-65
- 11.3-5: ε ≥ 1/|Q| - 1/|U| for any ε-universal family
- 11.3-6: H = {h_b : h_b(〈a₀,...,a_{d-1}〉) = Σ a_i·b^i mod p} is (d-1)/p-universal

**Exercises 11.4-1** through **11.4-6** (lines 10474-10503):
- 11.4-1: Insert 10,22,31,4,15,28,17,88,59 with m=11; linear probing vs double hashing
- 11.4-2: HASH-DELETE with DELETED marker; modify INSERT/Search
- 11.4-3: α=3/4: unsucc ≤ 4, succ ≤ (4/3)ln4≈1.848; α=7/8: unsucc ≤ 8, succ ≤ (8/7)ln8≈2.376
- 11.4-4: α=1 (n=m): expected successful probes = H_m (harmonic number)
- 11.4-5: If gcd(m, h₂(k)) = d, double hashing examines m/d slots before cycle
- 11.4-6: Solve 1/(1-α) = 2·(1/α)·ln(1/(1-α)) for α ≈ 0.715

**Exercises 11.5-1** through **11.5-3** (lines 10732-10751):
- 11.5-1: f_a is one-to-one modulo 2^w because 2k²+ak = k(2k+a) and odd a ensures invertibility
- 11.5-2: Random oracle is 5-independent by definition
- 11.5-3: r=3 needed (since f_a mixes bits, after 3 rounds any single input bit can affect any output bit)

**Problems** (lines 10753-10833):
- **11-1**: Longest-probe bound — for open addressing, n≤m/2: Pr[i-th insertion needs >p probes] ≤ 2^{-p}; E[max probes] = O(lg n)
- **11-2**: Searching a static set — binary search O(lg n); open addressing needs m-n = Θ(n) extra to match
- **11-3**: Slot-size bound for chaining — E[M] = O(lg n / lg lg n) using Stirling and Chernoff-style bounds
- **11-4**: Hashing and authentication — 2-independent ⇒ universal; polynomial-based family is universal but not 2-independent; adding random b makes it 2-independent; authentication tag: adversary succeeds with prob ≤ 1/p

---

## Ch. 12 — Binary Search Trees

### Named Entities

- **Binary search tree (BST)**: binary tree satisfying BST property
- **Binary-search-tree property**: for node x, all keys in left subtree ≤ x.key; all keys in right subtree ≥ x.key
- **Inorder tree walk**: visit left, then root, then right; prints keys in sorted order
- **Preorder tree walk**: visit root, then left, then right
- **Postorder tree walk**: visit left, then right, then root
- **Successor**: next node visited in inorder walk (smallest key greater than x.key, or next in order if duplicates)
- **Predecessor**: previous node visited in inorder walk
- **Trailing pointer**: variable y maintaining parent of current node x during traversal
- **TRANSPLANT**: replaces subtree at u with subtree at v (updates parent pointers)
- **Randomly built BST**: insert n keys in random order (any permutation equally likely); expected height O(lg n)
- **Radix tree (trie)**: tree storing bit strings; go left if bit=0, right if bit=1; lexicographic sort in Θ(n) total string length
- **Catalan number**: b_n = (1/(n+1))(2n choose n) = number of different binary trees with n nodes
- **Total path length P(T)**: sum of depths of all nodes in T

### Processes/Algorithms

#### INORDER-TREE-WALK(x)
```
1 if x ≠ NIL
2     INORDER-TREE-WALK(x.left)
3     print x.key
4     INORDER-TREE-WALK(x.right)
```
Time: Θ(n) for n-node tree (Theorem 12.1 proves by substitution: T(n) ≤ (c+d)n + c)

**Example**: Tree with keys [2,5,5,6,7,8] (Figure 12.1a):
```
    6
   / \
  5   7
 / \   \
2   5   8
```
Inorder walk: 2, 5, 5, 6, 7, 8

#### TREE-SEARCH(x, k)
```
1 if x == NIL or k == x.key
2     return x
3 if k < x.key
4     return TREE-SEARCH(x.left, k)
5 else return TREE-SEARCH(x.right, k)
```
Time: O(h) where h = height

#### ITERATIVE-TREE-SEARCH(x, k)
```
1 while x ≠ NIL and k ≠ x.key
2     if k < x.key
3         x = x.left
4     else x = x.right
5 return x
```
Time: O(h)

**Example**: Search for 13 in Figure 12.2: 15 → 6 → 7 → 13 (found)

#### TREE-MINIMUM(x)
```
1 while x.left ≠ NIL
2     x = x.left
3 return x
```
Time: O(h)

#### TREE-MAXIMUM(x)
```
1 while x.right ≠ NIL
2     x = x.right
3 return x
```
Time: O(h)

**Example**: Min in Figure 12.2: 15 → 6 → 2 (found). Max: 15 → 20 (found)

#### TREE-SUCCESSOR(x)
```
1 if x.right ≠ NIL
2     return TREE-MINIMUM(x.right)     // leftmost in right subtree
3 else
4     y = x.p
5     while y ≠ NIL and x == y.right
6         x = y
7         y = y.p
8     return y
```
Time: O(h)

Cases:
- x has right child: successor = minimum of right subtree
- x has no right child: go up until finding ancestor whose left child is also ancestor

**Example** (Figure 12.2c): successor of 15 = minimum of {17,20} = 17
**Example** (Figure 12.2d): successor of 13 (no right child): go up 13→7 (is right child?), 7→6 (is left child!) ⇒ successor = 6's parent? No, 13→7 (right child), 7→6 (left child) ⇒ successor = 15

#### TREE-PREDECESSOR — symmetric to SUCCESSOR

#### TREE-INSERT(T, z)
```
 1 x = T.root          // node being compared
 2 y = NIL             // trailing pointer (parent of z)
 3 while x ≠ NIL
 4     y = x
 5     if z.key < x.key
 6         x = x.left
 7     else x = x.right
 8 z.p = y
 9 if y == NIL
10     T.root = z      // tree was empty
11 elseif z.key < y.key
12     y.left = z
13 else y.right = z
```
Time: O(h)

**Example** (Figure 12.3): Insert key 13 into:
```
    12
   /  \
  5   18
 /   / \
2   15  19
```
- x=12, y=NIL; 13>12: x=18, y=12
- x=18, y=12; 13<18: x=15, y=18
- x=15, y=18; 13<15: x=15.left=NIL, y=15
- x=NIL, exit; z.p=15; 13<15: 15.left=13
Result: 13 becomes left child of 15

#### TRANSPLANT(T, u, v) — replace subtree u with subtree v
```
1 if u.p == NIL
2     T.root = v
3 elseif u == u.p.left
4     u.p.left = v
5 else u.p.right = v
6 if v ≠ NIL
7     v.p = u.p
```

#### TREE-DELETE(T, z)
```
 1 if z.left == NIL
 2     TRANSPLANT(T, z, z.right)        // case (a): no left child
 3 elseif z.right == NIL
 4     TRANSPLANT(T, z, z.left)         // case (b): no right child
 5 else y = TREE-MINIMUM(z.right)       // y = successor
 6     if y ≠ z.right                    // case (d): y not right child
 7         TRANSPLANT(T, y, y.right)
 8         y.right = z.right
 9         y.right.p = y
10     TRANSPLANT(T, z, y)             // case (c)/(d): replace z by y
11     y.left = z.left
12     y.left.p = y
```
Time: O(h)

Cases (Figure 12.4):
- **(a)** z has no left child: replace z by right child r
- **(b)** z has left child but no right child: replace z by left child l
- **(c)** z has two children, successor y is z's right child: replace z by y, y's left = z's left
- **(d)** z has two children, successor y ≠ z.right: first replace y by y.right, then replace z by y, giving y z's left and right children

**Example**: Delete node with key 13 from:
```
      15
     /  \
    6   17
   /   /  \
  7   13  20
```
- z.left=7 (non-NIL), z.right=17 (non-NIL) ⇒ two children
- y = TREE-MINIMUM(17) = 13
- y ≠ z.right: TRANSPLANT(T, 13, 13.right=NIL); 13.right = 17; 17.p = 13
- TRANSPLANT(T, 15, 13): 13.left=6; 6.p=13
Result:
```
    13
   /  \
  6   17
   \    \
    7   20
```

### Data Structures — Operations Table

| Operation | Running Time (BST height h) | Running Time (balanced, h = Θ(lg n)) |
|-----------|---------------------------|--------------------------------------|
| SEARCH | O(h) | O(lg n) |
| MINIMUM | O(h) | O(lg n) |
| MAXIMUM | O(h) | O(lg n) |
| SUCCESSOR | O(h) | O(lg n) |
| PREDECESSOR | O(h) | O(lg n) |
| INSERT | O(h) | O(lg n) |
| DELETE | O(h) | O(lg n) |
| INORDER-TREE-WALK | Θ(n) | Θ(n) |

### Comparisons

| Dimension | BST (unbalanced) | BST (balanced/RBT) | Sorted Array | Linked List |
|-----------|------------------|---------------------|--------------|-------------|
| SEARCH | O(n) worst | O(lg n) | O(lg n) binary | Θ(n) |
| INSERT | O(n) worst | O(lg n) | Θ(n) shift | O(1) at head |
| DELETE | O(n) worst | O(lg n) | Θ(n) shift | O(1) given ptr |
| MIN/MAX | O(n) worst | O(lg n) | O(1) | O(1) for ends |
| SUCCESSOR | O(n) worst | O(lg n) | O(1) with ptr | Θ(n) |
| Intermediate | Node-based | Node-based | Implicit order | Pointer-based |

### Formula

- **Theorem 12.1**: INORDER-TREE-WALK on n-node subtree takes Θ(n) time
- **Theorem 12.2**: SEARCH, MINIMUM, MAXIMUM, SUCCESSOR, PREDECESSOR run in O(h) time on BST of height h
- **Theorem 12.3**: INSERT and DELETE run in O(h) time on BST of height h
- **Catalan numbers**: b₀=1, bₙ = Σ_{k=0}^{n-1} b_k·b_{n-1-k} = (1/(n+1))(2n choose n)
- **Total path length**: P(T) = P(T_L) + P(T_R) + n - 1
- **Average depth in random BST**: E[P(n)] = O(n lg n)
- **k successive SUCCESSOR calls**: O(k + h) time (Exercise 12.2-8)

### Edge Cases

- **Degenerate BST**: linear chain of n nodes; all operations Θ(n)
- **Insert node with equal keys**: can go left or right — affects performance
- **Deletion with two children**: successor is guaranteed to have no left child
- **Deletion with TRANSPLANT**: TRANSPLANT does not update v.left and v.right; caller's responsibility
- **Search on empty tree**: TREE-SEARCH returns NIL
- **Insert into empty tree**: T.root set to z
- **Successor of maximum**: returns NIL
- **Zigzag deletion path**: when successor is not immediate right child, need extra transplant

### End-of-Chapter Material

**Exercises 12.1-1** through **12.1-5** (lines 10966-10988):
- 12.1-1: Draw BSTs of heights 2,3,4,5,6 for set {1,4,5,10,16,17,21}
- 12.1-2: BST vs min-heap property; heap cannot print sorted in O(n)
- 12.1-3: Nonrecursive inorder tree walk (stack-based)
- 12.1-4: Preorder and postorder walks
- 12.1-5: Any comparison-based BST construction takes Ω(n lg n) worst-case

**Exercises 12.2-1** through **12.2-9** (lines 11101-11144):
- 12.2-1: Identify valid search path sequences (c and e are invalid)
- 12.2-2: Recursive TREE-MINIMUM and TREE-MAXIMUM
- 12.2-3: TREE-PREDECESSOR procedure
- 12.2-4: Counterexample to Kilmer's claim: keys on path, left, right may violate a≤b≤c
- 12.2-5: If node has two children, successor has no left child, predecessor no right child
- 12.2-6: When right subtree empty, successor is lowest ancestor whose left child is also ancestor
- 12.2-7: MINIMUM + n-1 SUCCESSOR calls take Θ(n) total
- 12.2-8: k successive SUCCESSOR calls take O(k+h)
- 12.2-9: If x is leaf and y its parent, y.key is smallest larger or largest smaller than x.key

**Exercises 12.3-1** through **12.3-7** (lines 11299-11336):
- 12.3-1: Recursive TREE-INSERT
- 12.3-2: Search examines 1 more node than insertion examined
- 12.3-3: BST sort: worst-case Θ(n²), best-case Θ(n lg n)
- 12.3-4: TRANSPLANT can receive v=NIL when z has at most one child
- 12.3-5: Delete is not commutative (counterexample)
- 12.3-6: BST with succ pointers instead of parent; need parent-finding subroutine
- 12.3-7: Alternative: use predecessor instead of successor; fair strategy alternates

**Problems** (lines 11336-11423):
- **12-1**: BST with equal keys — 4 strategies: (a) flag to alternate left/right (b) list at node (c) random choice (d) standard; analyze insertion of n identical keys
- **12-2**: Radix trees (trie) — sort bit strings lexicographically in Θ(total length) time
- **12-3**: Average depth of random BST — prove P(n) = O(n lg n) via recurrence P(n) = P(k) + P(n-k-1) + n-1; relates to RANDOMIZED-QUICKSORT
- **12-4**: Number of different binary trees — Catalan numbers b_n = (1/(n+1))(2n choose n) ∼ 4^n/(n^{3/2}√π)

---

## Ch. 13 — Red-Black Trees

### Named Entities

- **Red-black tree**: BST with color bit (RED/BLACK) per node; approximately balanced (height ≤ 2 lg(n+1))
- **Red-black properties**:
  1. Every node is red or black
  2. Root is black
  3. Every leaf (NIL) is black
  4. If a node is red, both children are black (no two reds in a row)
  5. For each node, all simple paths to descendant leaves contain same number of black nodes
- **Black-height bh(x)**: number of black nodes on any simple path from x (exclusive) down to leaf
- **Sentinel T.nil**: single black object representing all NILs; simplifies boundary conditions
- **Rotation**: local pointer restructuring preserving BST property; left/right rotation; O(1) time
- **Left rotation**: node x has right child y; y becomes new subtree root, x becomes y's left child, β (y's left) becomes x's right
- **Right rotation**: inverse of left rotation
- **Uncle**: sibling of a node's parent
- **Double black / red-and-black**: extra blackness carried by x during DELETE-FIXUP
- **Relaxed red-black tree**: satisfies properties 1,3,4,5 but root may be red
- **AVL tree**: binary search tree with height balance (|left.h - right.h| ≤ 1 for all nodes)
- **Persistent data structure**: maintains past versions; copy path from root to modified node (O(lg n) per operation)
- **Join operation**: combine two RBTs and one element where all keys in S₁ ≤ x ≤ all keys in S₂
- **Tango tree**: competitive binary search tree; O(lg lg n) per operation competitive ratio
- **Skip list**: probabilistic alternative to balanced trees; O(lg n) expected time

### Processes/Algorithms

#### LEFT-ROTATE(T, x)
```
 1 y = x.right                    // set y
 2 x.right = y.left               // turn y's left subtree into x's right
 3 if y.left ≠ T.nil
 4     y.left.p = x
 5 y.p = x.p                      // link x's parent to y
 6 if x.p == T.nil
 7     T.root = y
 8 elseif x == x.p.left
 9     x.p.left = y
10 else x.p.right = y
11 y.left = x                     // put x on y's left
12 x.p = y
```
Time: O(1). Preserves BST property.

**Visual Pattern** (Figure 13.2):
```
Before LEFT-ROTATE(T,x):        After LEFT-ROTATE(T,x):
       x                               y
      / \                             / \
     α   y                           x   γ
        / \                         / \
       β   γ                       α   β
```
BST order: α < x.key < β < y.key < γ (preserved)

#### RIGHT-ROTATE(T, y) — symmetric to LEFT-ROTATE

**Example** (Figure 13.3): LEFT-ROTATE on x=7:
```
Before:         After:
    11              11
   /                /
  7                18
 / \              / \
3  18            7  19
   / \          / \
  15  19       3  15
```

#### RB-INSERT(T, z)
```
 1 x = T.root
 2 y = T.nil
 3 while x ≠ T.nil            // standard BST insert
 4     y = x
 5     if z.key < x.key
 6         x = x.left
 7     else x = x.right
 8 z.p = y
 9 if y == T.nil
10     T.root = z
11 elseif z.key < y.key
12     y.left = z
13 else y.right = z
14 z.left = T.nil
15 z.right = T.nil
16 z.color = RED               // new node always red
17 RB-INSERT-FIXUP(T, z)
```
Time: O(lg n). Only modification differences from TREE-INSERT: T.nil replaces NIL; set children to T.nil; color red; call FIXUP.

#### RB-INSERT-FIXUP(T, z)
```
 1 while z.p.color == RED
 2     if z.p == z.p.p.left                    // parent is left child
 3         y = z.p.p.right                     // uncle
 4         if y.color == RED                   // Case 1: uncle red
 5             z.p.color = BLACK
 6             y.color = BLACK
 7             z.p.p.color = RED
 8             z = z.p.p
 9         else                                // Cases 2 & 3: uncle black
10             if z == z.p.right               // Case 2: z is right child
11                 z = z.p
12                 LEFT-ROTATE(T, z)
13             z.p.color = BLACK               // Case 3: z is left child
14             z.p.p.color = RED
15             RIGHT-ROTATE(T, z.p.p)
16     else                                    // symmetric (parent is right child)
17         y = z.p.p.left                      // uncle
18         if y.color == RED                   // Case 1'
19             z.p.color = BLACK
20             y.color = BLACK
21             z.p.p.color = RED
22             z = z.p.p
23         else
24             if z == z.p.left                // Case 2'
25                 z = z.p
26                 RIGHT-ROTATE(T, z)
27             z.p.color = BLACK               // Case 3'
28             z.p.p.color = RED
29             LEFT-ROTATE(T, z.p.p)
30 T.root.color = BLACK
```

**Loop invariant** (start of each iteration):
(1) z is red
(2) If z.p is root, then z.p is black
(3) At most one violation: either property 2 (z red root) or property 4 (z and z.p both red)

**Three Cases** (when parent is left child):

| Case | Uncle Color | z position | Action | Outcome |
|------|------------|------------|--------|---------|
| 1 | RED | any | Recolor parent, uncle, grandparent; z moves up 2 levels | May continue loop |
| 2 | BLACK | right child | Left rotate at parent | Becomes Case 3 |
| 3 | BLACK | left child | Recolor parent black, grandparent red; right rotate at grandparent | Loop terminates |

**Example** (Figure 13.4):
Insert key 4 into:
```
     11(B)
    /  \
   2(R) 14(B)
  / \    \
 1(B) 7(B) 15(R)
```
After BST insert, z=4(R), parent=7(R) ⇒ violation property 4.
- z.p=7 is left child of z.p.p=11. Uncle=14(R) → Case 1:
  - parent 7→Black, uncle 14→Black, grandparent 11→Red, z=11
- z=11(R), parent 2(B) → loop exits (parent black)
- Root 11 colored black by line 30

**Maximum rotations per insertion**: ≤ 2

#### RB-TRANSPLANT(T, u, v) — for red-black tree
```
1 if u.p == T.nil
2     T.root = v
3 elseif u == u.p.left
4     u.p.left = v
5 else u.p.right = v
6 v.p = u.p
```
Difference from TRANSPLANT: T.nil instead of NIL; line 6 unconditional (assigns v.p even if v=T.nil)

#### RB-DELETE(T, z)
```
 1 y = z
 2 y-original-color = y.color
 3 if z.left == T.nil
 4     x = z.right
 5     RB-TRANSPLANT(T, z, z.right)
 6 elseif z.right == T.nil
 7     x = z.left
 8     RB-TRANSPLANT(T, z, z.left)
 9 else y = TREE-MINIMUM(z.right)
10     y-original-color = y.color
11     x = y.right
12     if y ≠ z.right
13         RB-TRANSPLANT(T, y, y.right)
14         y.right = z.right
15         y.right.p = y
16     else x.p = y
17     RB-TRANSPLANT(T, z, y)
18     y.left = z.left
19     y.left.p = y
20     y.color = z.color
21 if y-original-color == BLACK
22     RB-DELETE-FIXUP(T, x)
```
Time: O(lg n).

Key: y is the node actually removed/moved. x is y's child that takes y's place. If y was black, fixup needed.

#### RB-DELETE-FIXUP(T, x)
```
 1 while x ≠ T.root and x.color == BLACK
 2     if x == x.p.left                        // x is left child
 3         w = x.p.right                       // sibling
 4         if w.color == RED                   // Case 1: sibling red
 5             w.color = BLACK
 6             x.p.color = RED
 7             LEFT-ROTATE(T, x.p)
```



| Case | w(sibling) | w.left | w.right | Action | Loop continues? |
|------|-----------|--------|---------|--------|-----------------|
| 1 | RED | — | — | Recolor w black, x.p red; left rotate x.p; reset w | No (falls to 2/3/4) |
| 2 | BLACK | BLACK | BLACK | Set w red; x = x.p | Yes (if x.p black) |
| 3 | BLACK | RED | BLACK | Set w.left black, w red; right rotate w; reset w | No (becomes case 4) |
| 4 | BLACK | any | RED | Set w = x.p.color; x.p black; w.right black; left rotate x.p; x = root | Terminates |


### Data Structures — Operations Table

| Operation | BST (height h) | RBT (n nodes) | RBT guarantee |
|-----------|---------------|---------------|---------------|
| SEARCH | O(h) | O(lg n) | O(lg n) worst-case |
| MINIMUM | O(h) | O(lg n) | O(lg n) worst-case |
| MAXIMUM | O(h) | O(lg n) | O(lg n) worst-case |
| SUCCESSOR | O(h) | O(lg n) | O(lg n) worst-case |
| PREDECESSOR | O(h) | O(lg n) | O(lg n) worst-case |
| INSERT | O(h) | O(lg n) | O(lg n), ≤2 rotations |
| DELETE | O(h) | O(lg n) | O(lg n), ≤3 rotations |

### Formulas

- **Height bound**: h ≤ 2 lg(n+1) where n = number of internal nodes
- **Black-height bound**: n ≥ 2^{bh(root)} - 1 ⇒ bh(root) ≤ lg(n+1)
- **Path ratio**: longest path ≤ 2 × shortest path (property 4 and 5)
- **Maximum internal nodes for black-height k**: 2^{2k} - 1 (perfect RBT with alternating red/black)
- **Minimum internal nodes for black-height k**: 2^k - 1 (all black)
- **Largest ratio red:black**: 2:1 (alternating every other level starting with red root's children)
- **Smallest ratio red:black**: 0 (all black tree)

### Rules/Laws/Theorems





### Visual Patterns

```
```
- Inorder: α, x, β, y, γ preserved
- x.right must be non-nil

```
```

```


```

```



```

### Edge Cases

- **Root red**: violates property 2; RB-INSERT-FIXUP line 30 always colors root black
- **Sentinel T.nil**: all NIL replacements; color BLACK; used as child of newly inserted node; its parent may be written unconditionally
- **Inserting into empty tree**: z becomes root, z.color=RED, then line 30 fixes to BLACK
- **Case 1 causing property 2 violation**: if z moves to root (red), line 30 fixes
- **Case 2/3 only execute after Case 1 is impossible** (uncle becomes black)
- **Delete: y was red** → no fixup needed (no black-height change, no adjacent reds)
- **Delete: y was black** → three possible violations: (1) red child becomes root (prop 2), (2) x and x.p both red (prop 4), (3) path missing one black (prop 5)
- **x is T.nil in RB-DELETE**: x.p is explicitly set (line 16 or via RB-TRANSPLANT) because FIXUP references x.p
- **Sibling w is never T.nil** when x is doubly black (otherwise black-heights would differ)
- **Case 2 can repeat** O(lg n) times; no rotations in case 2
- **Sentinel T.nil.color never set to RED** (professor's concern unfounded)
- **Left-leaning RBT**: only left children can be red; simpler code but non-constant rotations

### End-of-Chapter Material

- 13.1-1: Complete BST of height 3 on {1..15}; color for black-heights 2,3,4
- 13.1-2: Insert 36 into Figure 13.1; red violates property 4; black violates property 5
- 13.1-3: Relaxed RBT with red root; changing root to black yields valid RBT
- 13.1-4: Black node absorbing red children: degree 2,3,4; leaves at same depth
- 13.1-5: Longest path ≤ 2 × shortest path from any node x
- 13.1-6: Max internal nodes for black-height k = 2^{2k}-1; min = 2^k-1
- 13.1-7: Largest red:black ratio = 2:1; smallest = 0 (all black)
- 13.1-8: Red node cannot have exactly one non-NIL child

- 13.2-1: RIGHT-ROTATE pseudocode (symmetric to LEFT-ROTATE)
- 13.2-2: Exactly n-1 possible rotations in n-node BST
- 13.2-3: Depth changes after left rotation on x
- 13.2-4: Any n-node BST transforms to any other with O(n) rotations
- 13.2-5: Right-conversion needs O(n²) rotations at worst

- 13.3-1: New node colored red to avoid property 5 violation
- 13.3-2: Successively insert 41,38,31,12,19,8 into empty RBT
- 13.3-3: Label black-heights in Figures 13.5 and 13.6
- 13.3-4: RB-INSERT-FIXUP never sets T.nil.color to RED
- 13.3-5: If n>1, at least one red node (otherwise properties would be violated)
- 13.3-6: RB-INSERT without parent pointers: maintain path stack

- 13.4-1: If y is red in RB-DELETE, no black-heights change
- 13.4-2: After RB-DELETE-FIXUP, root is black
- 13.4-3: If x and x.p both red, property 4 restored by fixup
- 13.4-4: Delete 8,12,19,31,38,41 from tree built in 13.3-2
- 13.4-5: Which lines of RB-DELETE-FIXUP touch T.nil
- 13.4-6: Count black nodes in each case of Figure 13.7 before/after
- 13.4-7: At start of case 1, x.p must be black
- 13.4-8: Insert then immediately delete same node — tree may differ
- 13.4-9: RB-ENUMERATE — output keys in [a,b] in Θ(m+lg n)

- **13-1**: Persistent dynamic sets — binary search tree with root per version; copy O(h) nodes per insert; parent pointers force Ω(n) copies; with RBT, O(lg n) per operation
- **13-2**: Join operation on RBT — use black-height attribute; find node y in taller tree at same black-height as shorter tree; attach in O(1); fixup in O(lg n)
- **13-3**: AVL trees — height O(lg n) with Fibonacci numbers; BALANCE(x) with rotations; AVL-INSERT uses recursion for O(lg n); O(lg n) rotations possible (unlike RBT's ≤2)

---

### Cross-Chapter Dependencies

| Chapter | Depends On | Used In |
|---------|-----------|---------|
| 10 (Linked lists) | — | 11 (chaining), 12 (BST nodes), 13 (RBT nodes) |
| 11 (Hash tables) | 10 (chaining lists) | — |
| 12 (BST) | 10 (tree representation) | 13 (RBT basis), 14 (optimal BST) |
| 13 (RBT) | 12 (BST operations) | 17 (amortized analysis), 18 (B-trees) |

- **Ch.10 → Ch.11**: Linked lists from §10.2 implement chaining in §11.2
- **Ch.10 → Ch.12**: Binary tree representation (§10.3) used for BST nodes
- **Ch.12 → Ch.13**: BST INSERT/DELETE operations (§12.3) form the basis of RB-INSERT and RB-DELETE
- **Ch.12 → Ch.14**: Optimal BST construction (§14.5) builds on BST concepts
- **Ch.13 → Ch.17**: Constant rotation bounds matter for amortized analysis of data structures
- **Randomized quicksort (Ch.7)** shares analysis with random BST (Problem 12-3)
- **Number theory (Ch.31)** used in universal hash family proof (§11.3.4)
- **Harmonic numbers (Appendix A)** used in open addressing analysis

### Dates & People

| Person | Contribution | Year | Ref |
|--------|-------------|------|-----|
| A.M. Turing | Stacks for subroutine linkage | 1947 | §10 notes |
| G.M. Hopper | A-1 language algebraic formula trees | 1951 | §10 notes |
| A. Newell, J.C. Shaw, H.A. Simon | IPL-II pointers, IPL-III stacks | 1956-7 | §10 notes |
| H.P. Luhn | Invented hash tables + chaining | 1953 | §11 notes |
| G.M. Amdahl | Open addressing | ~1953 | §11 notes |
| Carter & Wegman | Universal families of hash functions | 1979 | §11 notes |
| Dietzfelbinger et al. | Multiply-shift hash function | — | §11 notes |
| Fredman, Komlós, Szemerédi | Perfect hashing | — | §11 notes |
| Thorup | Linear probing with 5-independent hashing | — | §11 notes |
| Adel'son-Vel'skiĭ & Landis | AVL trees | 1962 | §13 notes |
| J.E. Hopcroft | 2-3 trees (unpublished) | 1970 | §13 notes |
| Bayer & McCreight | B-trees | — | §13 notes |
| Bayer | "Symmetric binary B-trees" (red-black) | — | §13 notes |
| Guibas & Sedgewick | Red/black color convention | — | §13 notes |
| Seidel & Aragon | Treaps | — | §13 notes |
| Sleator & Tarjan | Splay trees | — | §13 notes |
| Pugh | Skip lists | — | §13 notes |

### Design Paradigms

1. **Sentinel pattern** (§10.2, §13.1): dummy object eliminates boundary condition checks; simplifies code at cost of constant extra memory
2. **Divide-and-conquer via hashing** (§11.2): chaining divides n elements randomly into m subsets of approximate size n/m
3. **Randomization as algorithmic tool** (§11.3.2, §7, §12): randomly choose hash function from universal family to defeat adversary; random BST height O(lg n) expected
4. **Rolling hash / Horner's method** (Exercise 11.3-2): process string incrementally for division-method hashing
5. **Trailing pointer** (§12.3): maintain y as parent of current x during BST tree traversal for insert
6. **TRANSPLANT subroutine** (§12.3, §13.4): generic subtree replacement; simplifies DELETE
7. **Loop invariant for repair** (§13.3-13.4): maintain at most one violation of red-black properties during fixup
8. **"Extra black" abstraction** (§13.4): treat removed black node's blackness as transferred to the replacing node; simplifies analysis
9. **Persistent data structures** (Problem 13-1): copy path from root to modified node; share unmodified subtrees
10. **Join operation** (Problem 13-2): leverage black-height to balance two trees in O(lg n)


---

## Ch. 14 — Dynamic Programming

### Named Entities

| Term | Definition |
|------|------------|
| **Optimal substructure** | An optimal solution to a problem contains within it optimal solutions to subproblems |
| **Overlapping subproblems** | The space of subproblems is small; a recursive algorithm solves the same subproblems repeatedly |
| **Memoization** | Top-down DP: solve recursively, save each result, look up on subsequent encounters |
| **Bottom-up method** | Solve subproblems in increasing size order, smallest first |
| **Subproblem graph** | Directed graph: one vertex per distinct subproblem, edge from x to y if solving x requires solving y |
| **Rod-cutting problem** | Given rod length n and prices p_i, maximize revenue by cutting |
| **Matrix-chain multiplication** | Given chain of matrices, find parenthesization minimizing scalar multiplications |
| **Longest common subsequence (LCS)** | Find max-length common subsequence of two sequences |
| **Optimal binary search tree (OBST)** | BST minimizing expected search cost given key/dummy probabilities |
| **Load factor (table)** | num items / table size |

### Processes/Algorithms — Full Steps, Examples

#### Four-step DP method

---

#### Rod Cutting


- r_n = max_{1 ≤ i ≤ n} (p_i + r_{n-i}), with r_0 = 0
- Alternative: r_n = max(p_n, max_{1 ≤ i ≤ n-1} (r_i + r_{n-i}))

```
```

```

```

```
```
- Complexity: Θ(n²)
- Reconstruction uses s[j] to record optimal first-cut size


| i | r[i] | s[i] | Decomposition |
|---|------|------|---------------|
| 0 | 0 | — | — |
| 1 | 1 | 1 | 1 |
| 2 | 5 | 2 | 2 |
| 3 | 8 | 3 | 3 |
| 4 | 10 | 2 | 2+2 |


---

#### Matrix-Chain Multiplication


- m[i,i] = 0
- m[i,j] = min_{i ≤ k < j} { m[i,k] + m[k+1,j] + p_{i-1}·p_k·p_j }

```
```
- Complexity: Θ(n³) time, Θ(n²) space

- m[1,6] = 15,125
- Optimal parenthesization: ((A₁(A₂A₃))((A₄A₅)A₆))

```
```


---

#### Longest Common Subsequence (LCS)


- If xₘ = yₙ → LCS(X,Y) = LCS(X_{m-1}, Y_{n-1}) + xₘ
- If xₘ ≠ yₙ → LCS(X,Y) = longer of LCS(X_{m-1}, Y) and LCS(X, Y_{n-1})

- c[i,j] = 0 if i=0 or j=0
- c[i,j] = c[i-1,j-1] + 1 if x_i = y_j
- c[i,j] = max(c[i-1,j], c[i,j-1]) if x_i ≠ y_j

```
```
- Complexity: Θ(mn) time, Θ(mn) space

```
```

- LCS length = 4
- LCS = ⟨B,C,B,A⟩ (also ⟨B,D,A,B⟩)


---

#### Optimal Binary Search Tree (OBST)


- e[i,i-1] = q_{i-1} (dummy-only subtree)
- w[i,i-1] = q_{i-1}
- e[i,j] = min_{i≤r≤j} { e[i,r-1] + e[r+1,j] + w[i,j] }
- w[i,j] = w[i,j-1] + p_j + q_j

```
```
- Complexity: O(n³) time, O(n²) space
- Knuth optimization: root[i,j-1] ≤ root[i,j] ≤ root[i+1,j] → Θ(n²)


### Comparisons — DP vs Greedy

| Property | Dynamic Programming | Greedy Algorithms |
|----------|-------------------|-------------------|
| Choice basis | Depends on subproblem solutions | Looks best at moment |
| Direction | Bottom-up (or top-down memoized) | Top-down |
| Subproblems | Many overlapping | One remaining after greedy choice |
| When applicable | Optimal substructure + overlapping subproblems | Optimal substructure + greedy-choice property |
| Complexity | Often polynomial (n², n³) | Often linear or O(n log n) |
| Example | 0-1 knapsack | Fractional knapsack |

### Comparisons — Memoization vs Bottom-up

| Aspect | Top-down Memoized | Bottom-up |
|--------|------------------|-----------|
| Approach | Recursive with saved results | Iterative, increasing size |
| Overhead | Recursion + table check | Lower constant factors |
| Subproblem solving | Only those needed | All subproblems |
| When preferable | Sparse subproblem space | Dense subproblem space |

### Formulas/Recurrences

| Problem | Recurrence | Variables |
|---------|-----------|-----------|
| Rod cutting | r_n = max_{1≤i≤n} (p_i + r_{n-i}) | r_n = max revenue, p_i = price of length i |
| Matrix-chain | m[i,j] = min_{i≤k<j} (m[i,k] + m[k+1,j] + p_{i-1}p_kp_j) | m[i,j] = min mults, p_i = dimensions |
| LCS | c[i,j] = c[i-1,j-1]+1 if x_i=y_j else max(c[i-1,j], c[i,j-1]) | c[i,j] = LCS length of prefixes |
| OBST | e[i,j] = min_{i≤r≤j} (e[i,r-1] + e[r+1,j] + w[i,j]) | e[i,j] = expected cost, w[i,j] = sum of probabilities |
| OBST weight | w[i,j] = w[i,j-1] + p_j + q_j | p_j = key prob, q_j = dummy prob |

### Rules/Laws




### Proof Patterns

1. **Cut-and-paste proof of optimal substructure:** Assume subproblem solution is not optimal; cut it out and paste in a better one → contradiction to optimality of original
2. **Contradiction via augmentation** (LCS Theorem 14.1): If last chars match and LCS doesn't use it, append it for longer LCS
3. **Subproblem graph argument:** Running time = Σ(degree of vertices) = O(|V| + |E|)

### Design Paradigms

- **Top-down with memoization:** Write recursive algorithm, save each result, check before recomputing
- **Bottom-up:** Order subproblems by size, solve smallest first
- **DP vs divide-and-conquer:** DP when subproblems overlap; D&C when disjoint
- **Key question for DP:** Can you define subproblems with optimal substructure? Are subproblems overlapping?

### Case Studies

| Problem | Subproblems | Choices | Complexity |
|---------|-------------|---------|------------|
| Rod cutting | n (one per length) | n (first cut) | Θ(n²) |
| Matrix-chain | Θ(n²) (pairs i,j) | O(n) (split k) | Θ(n³) |
| LCS | Θ(mn) (prefix pairs) | 2-3 (match or skip) | Θ(mn) |
| OBST | Θ(n²) (key ranges) | O(n) (root r) | O(n³) |

### Data Structures

- Tables (arrays) for storing subproblem solutions
- s[i,j] table for reconstruction of optimal choices
- Subproblem graph (directed)

### Edge Cases

- **Rod cutting:** n=0 → revenue 0; no cut may be optimal
- **Matrix-chain:** n=1 → no multiplication needed
- **LCS:** empty prefix → length 0; no common subsequence
- **OBST:** j = i-1 → dummy-only subtree; empty subtree conventions

### Cross-Chapter Dependencies

- **Divide-and-conquer (Ch 2,4):** DP differs by overlapping subproblems
- **Greedy algorithms (Ch 15):** Greedy is special case where one choice suffices
- **Shortest paths (Ch 22,23):** Optimal substructure
- **NP-completeness (Ch 34):** Longest simple path is NP-complete, lacks optimal substructure
- **Catalan numbers (Problem 12-4):** Count parenthesizations

### Dates & People

| Name | Contribution |
|------|-------------|
| Richard Bellman (1955, 1957) | Systematic study of DP; coined term |
| Muraoka & Kuck | Matrix-chain algorithm |
| Hu & Shing | O(n log n) matrix-chain algorithm |
| Knuth | OBST algorithms, optimal-subtree root monotonicity |
| Hu & Tucker | OBST when p_i=0 |
| Gilbert & Moore | Early OBST work |
| Avidan & Shamir | Seam carving (Problem 14-8) |

### End-of-Chapter Material

#### Exercises 14.1

#### Exercises 14.2

#### Exercises 14.3

#### Exercises 14.4

#### Exercises 14.5

#### Problems 14

---

## Ch. 15 — Greedy Algorithms

### Named Entities

| Term | Definition |
|------|------------|
| **Greedy-choice property** | A globally optimal solution can be assembled by making locally optimal (greedy) choices |
| **Optimal substructure** | Same as in DP: optimal solution contains optimal solutions to subproblems |
| **Activity-selection problem** | Select max-size set of mutually compatible activities |
| **Fractional knapsack** | Items divisible; greedy by value/weight works |
| **0-1 knapsack** | Items indivisible; greedy fails, DP needed |
| **Huffman code** | Optimal prefix-free binary code using greedy merging |
| **Prefix-free code** | No codeword is prefix of another |
| **Full binary tree** | Every nonleaf node has two children (for optimal prefix-free codes) |
| **Offline caching** | Know entire request sequence; minimize cache misses |
| **Furthest-in-future** | Evict block whose next access is furthest in the future |
| **Compulsory miss** | Miss during first filling of cache |

### Processes/Algorithms — Full Steps, Examples

#### Greedy Algorithm Design (simplified)

#### Activity Selection



```
```

```
```
- Complexity: Θ(n) (after sorting O(n lg n))

- Greedy selects: a₁, a₄, a₈, a₁₁ (4 activities)
- Also optimal: {a₂, a₄, a₉, a₁₁}

---

#### Huffman Codes



```
```
- Complexity: O(n lg n) with binary min-heap

- Code: a=0, b=101, c=100, d=111, e=1101, f=1100
- Total bits: 224,000 (vs 300,000 fixed-length)

- Lemma 15.2 (Greedy-choice): Lowest-freq characters x,y have codewords of same length, differ only in last bit
- Lemma 15.3 (Optimal substructure): Merging x,y into z with z.freq = x.freq + y.freq preserves optimality
- Theorem 15.4: HUFFMAN produces optimal prefix-free code


---

#### Offline Caching (Furthest-in-Future)




- miss(C,i) = 0 if block b_i ∈ C (hit)
- miss(C,i) = min_{C' ∈ R_{C,i}} (1 + miss(C', i+1)) if miss

### Comparisons — Tables

#### DP vs Greedy

| Aspect | Dynamic Programming | Greedy |
|--------|-------------------|--------|
| Choice depends on | Subproblem solutions | Local optimum only |
| Approach | Bottom-up (or top-down memoized) | Top-down |
| Subproblems remaining | Many | One |
| Proof technique | Cut-and-paste | Greedy stays ahead / exchange argument |
| When it works | Optimal substructure + overlapping | Optimal substructure + greedy-choice |
| Example that fails | — | 0-1 knapsack (greedy fails) |

#### Fractional vs 0-1 Knapsack

| Aspect | Fractional | 0-1 |
|--------|-----------|-----|
| Items divisible | Yes | No |
| Greedy works | Yes (by value/weight) | No |
| Solution method | Greedy O(n log n) | DP O(nW) |
| Optimal substructure | Yes | Yes |
| Greedy-choice property | Yes | No |

### Formulas/Recurrences

| Problem | Formula | Variables |
|---------|---------|-----------|
| Activity DP | c[i,j] = max_{a_k∈S_{ij}} (c[i,k] + c[k,j] + 1) | c[i,j] = max activities between a_i, a_j |
| Huffman cost | B(T) = Σ_{c∈C} c.freq · d_T(c) | d_T(c) = depth of leaf for c |
| Huffman cost (alt) | B(T) = Σ_{internal} freq(z) | sum of merged frequencies |
| Offline caching | miss(C,i) = 0 if b_i∈C else min over evictions | miss = min cache misses from state C at position i |

### Rules/Laws



### Proof Patterns

1. **Exchange argument (greedy stays ahead):** Show greedy choice is at least as good as any other choice; transform any optimal solution to use greedy choice without worsening it (Theorem 15.1, 15.5)
2. **Greedy-choice proof by substitution:** Take optimal solution, replace first element with greedy choice, show result is still optimal
3. **Optimal substructure with greedy:** After making greedy choice, show remaining subproblem has optimal solution; combine with greedy choice
4. **Huffman two-step (Lemmas 15.2, 15.3):** (1) Greedy merge at first step doesn't hurt, (2) merging creates smaller instance
5. **Contradiction via swapping** (Huffman): Swap deep siblings with lowest-frequency nodes without increasing cost

### Design Paradigms

- **Greedy algorithm development (detailed):**
- **Simplified greedy design:**
- **When greedy works:** matroids (see literature), greedy-choice property + optimal substructure
- **Greedy vs DP trade-off:** Greedy requires fewer choices examined, but not always applicable

### Case Studies

| Problem | Greedy Choice | Complexity | Proof method |
|---------|---------------|------------|--------------|
| Activity selection | Earliest finish time | Θ(n) sorted | Exchange argument |
| Huffman coding | Merge two smallest frequencies | O(n log n) | Greedy choice + optimal substructure |
| Offline caching | Furthest-in-future | Depends on implementation | Exchange argument |
| Fractional knapsack | Highest value/weight | O(n log n) | Greedy-choice property |

### Data Structures

- **Min-priority queue** for Huffman algorithm
- **Binary tree** for representing prefix-free codes
- **Array** for activity start/finish times

### Visual Patterns

- **Huffman tree:** Full binary tree, leaves = characters, internal nodes = merged frequencies, edges labeled 0/1
- **Activity selection:** Time-line with intervals; selected activities are non-overlapping

### Edge Cases

- **Activity selection:** Empty set → return ∅; multiple activities with same finish time → any works
- **Huffman:** Single character → no merging needed; equal frequencies → balanced tree
- **Fractional knapsack:** Weight limit W may be less than smallest item
- **0-1 knapsack:** W and w_i may be large; O(nW) may be pseudo-polynomial
- **Offline caching:** Cache initially empty → compulsory misses; block never accessed again → evict it

### Cross-Chapter Dependencies

- **DP (Ch 14):** Greedy algorithms often have DP underpinnings; activity selection DP solution is possible but inefficient
- **Minimum spanning tree (Ch 21):** Classic greedy (Kruskal, Prim)
- **Dijkstra's algorithm (Section 22.3):** Greedy shortest paths
- **Set cover (Section 35.3):** Greedy heuristic for NP-hard problem
- **Huffman:** Compress data; used in file formats

### Dates & People

| Name | Contribution |
|------|-------------|
| David A. Huffman (1952) | Huffman coding |
| Belady (1966) | Furthest-in-future (Belady's algorithm) |
| Edmonds (1971) | First greedy algorithm in combinatorial optimization lit |
| Gavril | Activity-selection proof |
| Lelewer & Hirschberg | Survey of data compression (1987) |
| Lawler, Papadimitriou & Steiglitz | Greedy algorithm references |

### End-of-Chapter Material

#### Exercises 15.1

#### Exercises 15.2

#### Exercises 15.3

#### Exercises 15.4

#### Problems 15

---

## Ch. 16 — Amortized Analysis

### Named Entities

| Term | Definition |
|------|------------|
| **Amortized analysis** | Average time per operation over a sequence, worst-case guarantee |
| **Aggregate analysis** | Show total T(n) for n operations; amortized = T(n)/n |
| **Accounting method** | Assign differing amortized costs; overcharge early → credit pays for later undercharges |
| **Potential method** | Prepaid work as "potential energy" of data structure as a whole |
| **Potential function Φ** | Maps data structure to real number; amortized cost = actual + ΔΦ |
| **Credit** | Difference between amortized and actual cost (accounting method) |
| **Load factor α(T)** | num items / table size (defined as 1 for empty table) |
| **Table expansion** | Double size when full (load factor ≥ 1/2 guarantee) |
| **Table contraction** | Halve size when load factor < 1/4 (avoids thrashing) |

### Processes/Algorithms — Full Steps, Examples

#### Stack with MULTIPOP



- PUSH: amortized cost 2 (pay $1 for push, deposit $1 on the plate)
- POP: amortized cost 0 (use deposited $1)
- MULTIPOP: amortized cost 0 (uses deposits on plates)
- Credit never negative since each plate has $1

- Φ(stack) = number of objects in stack
- PUSH: ĉ = 1 + 1 = 2
- POP: ĉ = 1 + (-1) = 0
- MULTIPOP(k): ĉ = k' + (-k') = 0 (k' = min(s,k))

---

#### Binary Counter


```
```


- Setting 0→1 costs $2 ($1 for actual, $1 deposit for future reset)
- Setting 1→0 costs $0 (paid by deposit)
- At most one 0→1 per INCREMENT → amortized cost = $2

- Φ(counter) = number of 1-bits
- ĉ_i ≤ (t_i + 1) + (1 - t_i) = 2
- If counter starts at b₀ 1-bits: total actual ≤ 2n + b₀ - b_n

---

#### Dynamic Tables



```
```


- Charge $3 per insertion
- $1 pays for this insertion
- $1 stored on the new item
- $1 stored on an existing item
- When expansion occurs, each of m items has $1 → pays for all m moves

- Φ = 2·num - size
- Φ = 0 immediately after expansion (num = size/2)
- Insert without expansion: ΔΦ = 2, ĉ = 1 + 2 = 3
- Insert with expansion: ΔΦ = 2 - (i-1) = 3-i, ĉ = i + (3-i) = 3


- Φ = 2·num - size if α ≥ 1/2
- Φ = size/2 - num if 1/4 ≤ α < 1/2
- All operations have O(1) amortized cost

### Comparisons — Tables

#### Three Amortized Analysis Methods

| Aspect | Aggregate | Accounting | Potential |
|--------|-----------|------------|-----------|
| Approach | Sum total cost, divide by n | Assign per-op amortized cost, track credit | Define potential function Φ |
| Amortized costs | Same for all operations | May differ per operation | Computed via ΔΦ |
| Key invariant | T(n)/n bound | Total credit ≥ 0 always | Φ(D_i) ≥ Φ(D₀) for all i |
| Proof technique | Summation | Credit invariant | Potential difference |
| Granularity | Coarse | Per-object credit | Data structure as whole |
| Stack MULTIPOP | O(1) all | PUSH=2, POP=0, MULTIPOP=0 | Ĉ_PUSH=2, Ĉ_POP=0, Ĉ_MULTIPOP=0 |
| Binary counter | O(1) per INCREMENT | $2 per INCREMENT | Ĉ ≤ 2 per INCREMENT |
| Table insertion | $3 per insert | $3 per insert | Ĉ = 3 per insert |

### Formulas/Recurrences

| Method | Formula | Variables |
|--------|---------|-----------|
| Accounting | Σ ĉ_i ≥ Σ c_i with credit ≥ 0 always | ĉ_i = amortized, c_i = actual cost |
| Potential | ĉ_i = c_i + Φ(D_i) - Φ(D_{i-1}) | Φ = potential function |
| Aggregate | Total amortized = Σ ĉ_i = O(T(n)) | T(n) = total actual cost |

### Rules/Laws




### Proof Patterns

1. **Aggregate counting** (binary counter): Count how many times each bit flips → geometric series → O(n)
2. **Accounting credit assignment** (stack): Overcharge PUSH, credit stored on each object covers future POP
3. **Potential function design** (table expansion): Φ = 2·num - size gives Φ=0 at half-full, builds to size before full
4. **Telescoping sum** (potential): Σ ĉ_i = Σ c_i + Φ(D_n) - Φ(D_0)
5. **Amortized cost bound via potential difference**: ĉ_i = c_i + ΔΦ_i ≤ bound
6. **Contraction thrashing prevention**: Halve at 1/4 not 1/2; otherwise O(n) amortized from repeated expansion/contraction

### Design Paradigms

- **Aggregate analysis:** Simplest; find total cost by summation
- **Accounting method:** Assign per-operation amortized costs, prove credit never negative
- **Potential method:** Choose Φ that starts at 0, stays nonnegative, gives desired amortized bounds
- **Table load factor boundary:** Use α = 1/2 as equilibrium; deviations build potential
- **Binary counter trick:** Each 0→1 carries $1 for its eventual reset

### Data Structures

- **Stack** with MULTIPOP
- **Binary counter** (bit array)
- **Dynamic table** (resizable array)

### Visual Patterns

- **Figure 16.2:** Binary counter bit flips — each column is one INCREMENT, shaded bits flip
- **Figure 16.3:** Accounting for table — $3 per insert distributed; at expansion each item has $1
- **Figure 16.4:** Plot of num_i, size_i, Φ_i — potential peaks just before expansion, drops to 0 after
- **Figure 16.5:** Potential function behavior for α ≥ 1/2 and α < 1/2
- **Figure 16.6:** Full sequence of inserts/deletes with potential

### Edge Cases

- **Empty stack:** MULTIPOP on empty → no pops, cost 0
- **Counter overflow:** When k bits are 1, INCREMENT resets all to 0 (mod 2^k)
- **Empty table:** T.num = T.size = 0 initially; define α(empty) = 1
- **Table at size 0:** First insertion allocates 1 slot
- **Counter doesn't start at 0:** amortized bound still O(n) if n = Ω(k)
- **Stack starts with s₀ objects:** total cost = O(n) + s₀ - s_n

### Cross-Chapter Dependencies

- **Red-black tree modifications (Ch 13, Problem 16-4):** Structural modifications amortized O(1)
- **Fibonacci heaps (Part V ref):** O(1) amortized for DECREASE-KEY
- **Disjoint-set forests (Ch 19):** Aggregate analysis for union-find
- **Splay trees (Part V ref):** O(log n) amortized per operation
- **Binary heaps (Ch 6):** Used for priority queue in amortized contexts

### Dates & People

| Name | Contribution |
|------|-------------|
| D.D. Sleator & R.E. Tarjan | Coined "amortized"; accounting & potential methods |
| M.R. Brown, R.E. Tarjan, S. Huddleston, K. Mehlhorn | Accounting method attribution |
| Aho, Hopcroft, Ullman | Aggregate analysis for disjoint-set forest |
| Belady | Furthest-in-future cache strategy (Ch 15 link) |
| Floyd | Potential functions for I/O lower bounds |
| Cormen, Sundquist, Wisniewski | I/O complexity potential functions |
| Krumme, Cybenko, Venkataraman | Lower bounds on gossiping via potential |

### End-of-Chapter Material

#### Exercises 16.1

#### Exercises 16.2

#### Exercises 16.3

#### Exercises 16.4

#### Problems 16

## Chapter 17: Augmenting Data Structures

### 1. Named Entities

| Term | Definition |
|------|-----------|
| **Augmenting** | Storing additional information in a textbook data structure to support new operations |
| **Order-statistic tree** | Red-black tree augmented with `size` attribute in each node (subtree node count) |
| **size attribute** | `x.size` = number of internal nodes in subtree rooted at x (including x, excluding sentinel) |
| **Interval tree** | Red-black tree where each node x contains an interval `x.int` and a `x.max` value |
| **Interval trichotomy** | For any two intervals i, i': exactly one holds — (a) overlap, (b) i left of i', (c) i right of i' |
| **low endpoint** | `i.low` = t1 for interval [t1, t2] |
| **high endpoint** | `i.high` = t2 for interval [t1, t2] |
| **Overlap** | i ∩ i' ≠ ∅ ⇔ i.low ≤ i'.high AND i'.low ≤ i.high |
| **Point of maximum overlap** | A point with the largest number of intervals that overlap it (Problem 17-1) |
| **Josephus permutation** | Order of removal when every m-th person is removed from a circle of n people (Problem 17-2) |

### 2. Algorithms — FULL Steps

#### OS-SELECT(x, i)
- **Input**: node x (root of subtree), integer i (1 ≤ i ≤ size of subtree)
- **Output**: pointer to node containing i-th smallest key in subtree
- **Time**: O(lg n)

```
OS-SELECT(x, i)
1  r = x.left.size + 1          // rank of x within its subtree
2  if i == r
3      return x
4  elseif i < r
5      return OS-SELECT(x.left, i)
6  else
7      return OS-SELECT(x.right, i - r)
```

**Concrete Example** (Figure 17.1 tree): Search for 17th smallest element
- Root (key 26): left.size = 12 → rank = 13. Since 17 > 13, recurse right with i = 17-13 = 4
- Node (key 41): left.size = 5 → rank = 6. Since 4 < 6, recurse left with i = 4
- Node (key 30): left.size = 1 → rank = 2. Since 4 > 2, recurse right with i = 4-2 = 2
- Node (key 38): left.size = 1 → rank = 2. Since i == 2, return node with key 38 ✓

#### OS-RANK(T, x)
- **Input**: order-statistic tree T, pointer to node x
- **Output**: rank of x.key in the inorder walk of T
- **Time**: O(lg n)

```
OS-RANK(T, x)
1  r = x.left.size + 1
2  y = x
3  while y ≠ T.root
4      if y == y.p.right
5          r = r + y.p.left.size + 1
6      y = y.p
7  return r
```

**Concrete Example** (Figure 17.1, key 38):
- Start: y=38, r=2
- y=30 (left child): no addition → r=2
- y=41 (right child): r = 2 + (30.left.size=1) + 1 = 4
- y=26 (right child): r = 4 + (26.left.size=12) + 1 = 17
- Return 17 ✓

#### LEFT-ROTATE with size update (for order-statistic tree)
```
// After standard LEFT-ROTATE(T, x) lines:
13  y.size = x.size
14  x.size = x.left.size + x.right.size + 1
```

#### INTERVAL-SEARCH(T, i)
- **Input**: interval tree T, interval i
- **Output**: pointer to node whose interval overlaps i, or T.nil if none
- **Time**: O(lg n)

```
INTERVAL-SEARCH(T, i)
1  x = T.root
2  while x ≠ T.nil and i does not overlap x.int
3      if x.left ≠ T.nil and x.left.max ≥ i.low
4          x = x.left
5      else
6          x = x.right
7  return x
```

**Concrete Example** (Figure 17.4 tree):
- **Successful** (i=[22,25]): root [16,21] no overlap, left.max=23 ≥ 22 → go left → [8,9] no overlap, left.max=10 < 22 → go right → [15,23] overlaps → return it ✓
- **Unsuccessful** (i=[11,14]): root [16,21] no overlap, left.max=23 ≥ 11 → go left → [8,9] no overlap, left.max=10 < 11 → go right → [15,23] no overlap, left child nil → go right → return T.nil ✓

### 3. Classifications

| Classification | Description |
|---------------|-------------|
| Order-statistic tree | Augmented RBT with `size` |
| Interval tree | Augmented RBT with `max` |

### 4. Comparisons

| Dimension | RBT | Order-Statistic Tree | Interval Tree |
|-----------|-----|---------------------|---------------|
| Extra attribute | none | `x.size` | `x.int`, `x.max` |
| SEARCH | O(lg n) | O(lg n) | O(lg n) |
| INSERT | O(lg n) | O(lg n) | O(lg n) |
| DELETE | O(lg n) | O(lg n) | O(lg n) |
| New ops | — | OS-SELECT, OS-RANK | INTERVAL-SEARCH |
| Rotations to fix size/max | — | O(1) per rotation | O(1) per rotation |

| Dimension | Augmentation Theorem (17.1) | Manual (size) |
|-----------|---------------------------|---------------|
| Update cost per rotation | O(lg n) worst-case | O(1) |
| Propagates to | all ancestors (O(lg n)) | only 2 nodes |

### 5. Formulas

- **Subtree size identity**: `x.size = x.left.size + x.right.size + 1`
- **Sentinel size**: `T.nil.size = 0`
- **max computation**: `x.max = max{ x.int.high, x.left.max, x.right.max }`

### 6. Rules/Laws/Theorems

**Theorem 17.1 (Augmenting a red-black tree)**
> Let f be an attribute that augments a red-black tree T of n nodes. Suppose the value of f for each node x depends only on information in nodes x, x.left, and x.right (possibly including x.left.f and x.right.f), and that x.f can be computed in O(1) time. Then INSERT and DELETE can maintain f in all nodes without asymptotically affecting the O(lg n) running time.

*Proof sketch*: A change to x.f propagates only to ancestors (O(lg n) nodes). Insertion: first phase computes x.f in O(1), propagates up O(lg n); second phase (rotations) at most 2 rotations, each O(lg n) to propagate. Deletion similarly O(lg n) per rotation, ≤3 rotations.

**Theorem 17.2**
> INTERVAL-SEARCH(T,i) either returns a node whose interval overlaps i, or returns T.nil and T contains no node whose interval overlaps i.

*Proof*: Interval trichotomy ensures search always goes in safe direction. If search goes right: left.max < i.low ⇒ no overlap in left subtree. If search goes left: either left subtree has overlap, or right subtree has no overlap (since i.high < i'.low ≤ x.int.low ≤ i''.low for any i'' in right subtree).

### 7. Data Structures — Complete Operations Tables

**Order-Statistic Tree** (augmented RBT + `size`)

| Operation | Time | Notes |
|-----------|------|-------|
| OS-SELECT | O(lg n) | Find i-th smallest |
| OS-RANK | O(lg n) | Find rank of element |
| INSERT | O(lg n) | + O(lg n) to maintain size |
| DELETE | O(lg n) | + O(lg n) to maintain size |
| SEARCH | O(lg n) | Standard RBT search |
| MINIMUM/MAXIMUM | O(lg n) | O(1) with pointers (Ex 17.2-1) |
| SUCCESSOR/PREDECESSOR | O(lg n) | O(1) with pointers (Ex 17.2-1) |

**Interval Tree** (augmented RBT + `int` + `max`)

| Operation | Time | Notes |
|-----------|------|-------|
| INTERVAL-INSERT | O(lg n) | Uses RBT INSERT + maintain max |
| INTERVAL-DELETE | O(lg n) | Uses RBT DELETE + maintain max |
| INTERVAL-SEARCH | O(lg n) | Find one overlapping interval |
| List all overlapping | O(min{n, k lg n}) | k = output size (Ex 17.3-3) |

### 8. Visual Patterns

**Figure 17.1** — Order-statistic tree: standard RBT with `size` shown to right of each node. Root 26 (size 20), left subtree 12 nodes, right subtree 7 nodes. Has duplicate keys 14 and 21.

**Figure 17.2** — Rotation update: LEFT-ROTATE updates `size` for x and y only. y gets x's old size, x recomputes from left+right sizes.

**Figure 17.4** — Interval tree: 10 intervals sorted by low endpoint. Each node shows interval (above dashed line) and `max` (below dashed line). The `max` propagates the maximum interval endpoint in the subtree.

### 9. Edge Cases

- **Duplicate keys**: rank defined by inorder walk position (two keys = 14, ranks 5 and 6)
- **Sentinel size**: T.nil.size = 0
- **Empty interval search**: returns T.nil
- **FIND-POM** (Problem 17-1): point of maximum overlap is always an endpoint of some interval

### 10. Empirical Evidence

None presented.

### 11. Cross-Chapter Dependencies

- **Chapter 13 (RBT)**: INSERT phases (Section 13.3), DELETE phases (Section 13.4), LEFT-ROTATE/RIGHT-ROTATE
- **Chapter 12 (BST)**: TREE-SEARCH, inorder tree walk
- **Chapter 9 (Order Statistics)**: Definition of order statistics, O(n) selection from unordered set
- **Problem 2-4 (Inversions)**: Referenced in Ex 17.1-7

### 12. Dates & People

- **H. Edelsbrunner** (1980): interval tree work
- **E. M. McCreight** (1981): interval tree work
- Preparata and Shamos [364]: described interval trees in their book

### 13. Proof Patterns

- **Augmentation Theorem**: Change to attribute at node x → propagate to ancestors only → O(lg n) total. Follow same pattern as size maintenance.
- **Interval correctness (Theorem 17.2)**: uses interval trichotomy + max attribute to prove search direction is safe
- Abstract 4-step design method: (1) choose data structure, (2) determine additional info, (3) verify maintainable, (4) develop new ops

### 14. Design Paradigms

- **Augmentation framework**: 4-step method (Section 17.2)
- **Key insight**: Store subtree aggregate (size/max) rather than per-node rank to limit update propagation to O(lg n)
- **Rotation-friendly attribute**: must be locally recomputable from children's values

### 15. Case Studies



### 16. Ethics


### 17. End-of-Chapter Material

#### Exercises 17.1

- Root 26: left.size=12, rank=13. 10 < 13 → recurse left
- Node 14 (left of 26): left.size=2, rank=3. 10 > 3 → recurse right with i=10-3=7
- Node 21 (right of 14): left.size=2, rank=3. 7 > 3 → recurse right with i=7-3=4
- Node 21 (right of 21): left.size=1, rank=2. 4 > 2 → recurse right with i=4-2=2
- Node 26 (right of 21): left.size=1, rank=2. i=2 == rank → return node with key 26

- Start: x=35, r=35.left.size+1 = 0+1 = 1, y=35
- y.p = 30 (y is right child): r = 1 + 30.left.size + 1 = 1+1+1=3
- y.p = 41 (y is left child): no addition, r=3
- y.p = 26 (y is right child): r = 3 + 26.left.size + 1 = 3+12+1=16
- Return 16

```
```

```
```

- Find rank r = OS-RANK(T, x)
- Return OS-SELECT(T.root, r + i)
- Both O(lg n) → total O(lg n)

- Maintain `x.r` = rank of x within its subtree
- After insertion: must update all nodes on path from new node to root; also rotation invalidates ranks in two subtrees (O(n) worst-case). **Impractical** — this is why size is used instead.

```
```

- Sort endpoints by polar angle around circle
- Process endpoints in order; when encountering second endpoint of a chord, count how many open chords have one endpoint before and one after → use order-statistic tree
- O(n lg n)

#### Exercises 17.2



- After rotation: x.f = (x.left's inorder ⊗) ⊗ x.a ⊗ (x.right's inorder ⊗) = x.left.f ⊗ x.a ⊗ x.right.f (by associativity)
- Recompute in O(1) from children
- For size: x.size = x.left.size + x.right.size + 1 (associative with +)

#### Exercises 17.3

```
```

- Perform standard search but track minimum-low overlapping interval found
- Or: use order-statistic property — find leftmost interval that overlaps i by checking left subtree first

```
```
- Simple: O(k lg n) with k modifications
- Without modification: use successor queries O(k lg n)

- Key = i.low; search tree for key; then check if x.int.high == i.high
- If match, return x; else T.nil
- O(lg n)

- Maintain red-black tree of numbers with augmented attribute `min-gap` at each node = min(|x.key - y.key|) in subtree
- Compute: x.min-gap = min{ x.left.min-gap, x.right.min-gap, |x.key - x.left.max-key|, |x.right.min-key - x.key| }
- Also maintain `min-key`, `max-key` in each subtree
- INSERT, DELETE, SEARCH: O(lg n); MIN-GAP: O(1)

- Sweep line: sort x-coordinates of all left/right edges
- Maintain interval tree of active rectangles (by y-interval)
- When processing left edge, check INTERVAL-SEARCH for overlap; if found, return true; else INSERT y-interval
- When processing right edge, DELETE y-interval
- O(n lg n)

#### Problems

- (a) Max overlap occurs at an endpoint: consider left-to-right sweep; overlap count changes only at endpoints
- (b) RBT augmented with `sum` (cumulative count), `max-overlap` (max prefix sum), store ±1 at each endpoint; FIND-POM = node with max prefix sum

- (a) m constant: use circular linked list, O(m * n) = O(n) since m constant
- (b) m not constant: use order-statistic tree with n nodes; repeatedly find (current_pos + m - 1) % size-th element; O(n lg n)

#### Chapter Notes
- Preparata & Shamos [364]: interval trees, cite Edelsbrunner (1980) and McCreight (1981)
- Static interval tree: enumerate k overlapping intervals in O(k + lg n)

---

## Chapter 18: B-Trees

### 1. Named Entities

| Term | Definition |
|------|-----------|
| **B-tree** | Balanced search tree with high branching factor, optimized for disk |
| **Minimum degree t** | t ≥ 2; every node (except root) has at least t-1 keys; at most 2t-1 keys |
| **Full node** | Node with exactly 2t-1 keys |
| **B+-tree** | Variant: satellite info in leaves, only keys in internal nodes |
| **B*-tree** | Variant: internal nodes at least 2/3 full |
| **2-3-4 tree** | B-tree with t=2 (nodes have 2, 3, or 4 children) |
| **2-3 tree** | Precursor to B-trees (Hopcroft 1970); nodes have 2 or 3 children |
| **Disk block** | Unit of disk I/O; B-tree node = one disk block |
| **Disk access** | DISK-READ and DISK-WRITE operations |
| **Platter** | Rotating magnetic disk surface |
| **Track** | Surface passing under stationary head |
| **Latency** | Time waiting for mechanical movement (rotation + arm movement) |
| **Split** | Dividing a full node (2t-1 keys) into two nodes of t-1 keys each, median moves to parent |
| **Merge** | Combining two sibling nodes (case 2c, 3b in deletion) |

### 2. Algorithms — FULL Steps

#### B-TREE-SEARCH(x, k)
- **Input**: node x (root of subtree), key k
- **Output**: (y, i) where y.keyi = k, or NIL
- **Time**: O(t logt n) CPU, O(logt n) disk accesses

```
B-TREE-SEARCH(x, k)
1  i = 1
2  while i ≤ x.n and k > x.keyi
3      i = i + 1
4  if i ≤ x.n and k == x.keyi
5      return (x, i)
6  elseif x.leaf
7      return NIL
8  else
9      DISK-READ(x.ci)
10     return B-TREE-SEARCH(x.ci, k)
```

**Concrete Example** (Figure 18.1): Search for R
- Start at root (contains 1 key roughly mid-alphabet)
- Compare: R > key → go to rightmost child
- At internal node with keys ~P, T, etc.: R > P but R < T → go to middle child
- At leaf or internal: find R → return (node, index) ✓

#### B-TREE-CREATE(T)
- **Time**: O(1) disk ops, O(1) CPU

```
B-TREE-CREATE(T)
1  x = ALLOCATE-NODE()
2  x.leaf = TRUE
3  x.n = 0
4  DISK-WRITE(x)
5  T.root = x
```

#### B-TREE-SPLIT-CHILD(x, i)
- **Input**: nonfull internal node x, index i where x.ci is a full child
- **Output**: splits x.ci into two nodes, adds median to x
- **Time**: Θ(t) CPU, O(1) disk ops

```
B-TREE-SPLIT-CHILD(x, i)
 1  y = x.ci                       // full node to split
 2  z = ALLOCATE-NODE()            // z takes larger half
 3  z.leaf = y.leaf
 4  z.n = t - 1
 5  for j = 1 to t - 1
 6      z.keyj = y.keyj+t
 7  if not y.leaf
 8      for j = 1 to t
 9          z.cj = y.cj+t
10  y.n = t - 1
11  for j = x.n + 1 downto i + 1
12      x.cj+1 = x.cj
13  x.ci+1 = z
14  for j = x.n downto i
15      x.keyj+1 = x.keyj
16  x.keyi = y.keyt
17  x.n = x.n + 1
18  DISK-WRITE(y)
19  DISK-WRITE(z)
20  DISK-WRITE(x)
```

**Concrete Example** (Figure 18.5, t=4):
- y = x.ci has 2t-1 = 7 keys (A, B, C, D, E, F, G? No — the figure shows letters)
- y has keys: A B C D E F G (median = D at keyt = key4)
- z gets keys E F G (t-1 = 3 keys)
- If internal: z also gets last t = 4 children of y
- y keeps keys A B C (t-1 = 3)
- D moves up to x at position i
- x now has one more child and one more key

#### B-TREE-SPLIT-ROOT(T)
- **Time**: O(1) disk ops, Θ(t) CPU

```
B-TREE-SPLIT-ROOT(T)
1  s = ALLOCATE-NODE()
2  s.leaf = FALSE
3  s.n = 0
4  s.c1 = T.root
5  T.root = s
6  B-TREE-SPLIT-CHILD(s, 1)
7  return s
```

#### B-TREE-INSERT(T, k)
- **Input**: B-tree T, key k
- **Time**: O(t logt n) CPU, O(logt n) disk accesses

```
B-TREE-INSERT(T, k)
1  r = T.root
2  if r.n == 2t - 1
3      s = B-TREE-SPLIT-ROOT(T)
4      B-TREE-INSERT-NONFULL(s, k)
5  else
6      B-TREE-INSERT-NONFULL(r, k)
```

#### B-TREE-INSERT-NONFULL(x, k)
- **Time**: O(t logt n) CPU, O(logt n) disk accesses

```
B-TREE-INSERT-NONFULL(x, k)
 1  i = x.n
 2  if x.leaf
 3      while i ≥ 1 and k < x.keyi
 4          x.keyi+1 = x.keyi
 5          i = i - 1
 6      x.keyi+1 = k
 7      x.n = x.n + 1
 8      DISK-WRITE(x)
 9  else
10      while i ≥ 1 and k < x.keyi
11          i = i - 1
12      i = i + 1
13      DISK-READ(x.ci)
14      if x.ci.n == 2t - 1
15          B-TREE-SPLIT-CHILD(x, i)
16          if k > x.keyi
17              i = i + 1
18      B-TREE-INSERT-NONFULL(x.ci, k)
```

**Concrete Example** (Figure 18.7, t=3):
- (a) Initial tree: root has keys P, children: (A C D E G H J K L M N O?) ... Let's trace insertion of B, Q, L, F:
- (b) Insert B: leaf ABCDE not full → insert B in sorted order → ABCDE becomes ABCDE... wait, B would go between A and C: A B C D E
- (c) Insert Q: path encounters full node RSTUV → split: median T moves to root, RS and UV become children. Then Q inserted into RS node → Q goes between P and R? Q > P → right subtree, RS → Q > R? Q < S → insert into first position: Q R S
- (d) Insert L: root P is full (has keys P T) → root splits → new root with T. Then L goes to leaf with J K → J K L
- (e) Insert F: leaf ABCDE is full → split before descent → median C moves to parent, AB and DE become children. Then F > D → goes into DE → D E F

#### B-TREE-DELETE(T, k) — All Cases

**Guarantee**: Node x has at least t keys (except root) when recursion enters it.

**Case 1 (Leaf)**: x is leaf, contains k → delete k from x. If k not in x → not in tree.

**Case 2 (Internal node x contains k = x.keyi)**:

| Subcase | Condition | Action |
|---------|-----------|--------|
| **2a** | x.ci has ≥ t keys | Find predecessor k' in subtree rooted at x.ci, recursively delete k' from x.ci, replace k by k' in x |
| **2b** | x.ci has t-1 keys AND x.ci+1 has ≥ t keys | Symmetric to 2a: find successor k' in x.ci+1 subtree, delete k', replace k by k' |
| **2c** | Both x.ci and x.ci+1 have t-1 keys | Merge k and x.ci+1 into x.ci (2t-1 keys total), free x.ci+1, recursively delete k from x.ci |

**Case 3 (Internal node x does NOT contain k)**:
- Determine child x.ci that would contain k
- If x.ci has t-1 keys, ensure it gets ≥ t keys before recursing:

| Subcase | Condition | Action |
|---------|-----------|--------|
| **3a** | x.ci has t-1 keys AND a sibling has ≥ t keys | Move key from x down into x.ci, move key from sibling up into x, move appropriate child pointer from sibling into x.ci |
| **3b** | x.ci and both siblings (if exist) have t-1 keys | Merge x.ci with one sibling: move key from x down to become median of new merged node. If x becomes empty (root case), delete x, child becomes new root |

**Edge Cases in Deletion**:
- Cases 2c and 3b: if x is root and ends up with 0 keys → delete x, x.c1 becomes new root → height decreases by 1
- Predecessor/successor finding: can be done in same downward pass; return to x only takes O(1) pointer access

**Concrete Example** (Figure 18.8, t=3):
- (a) Initial tree after all insertions
- (b) Delete F (Case 1): leaf ABCDEF... F found in leaf, just delete it
- (c) Delete M (Case 2a): M at internal node; find predecessor L in left subtree, delete L, replace M with L
- (d) Delete G (Case 2c): G at internal node; both children (DE and JK) have t-1=2 keys; merge G down → node DEGJK with 5 keys, then delete G from leaf (Case 1)
- (e) Delete D → (Case 3b at root): CL has 2 keys (< t=3), its siblings have t-1 → merge CL, P, TX → CLPTX; then delete D from leaf (Case 1)
- (e0) After deletion, root has 0 keys → delete root → height shrinks by 1
- (f) Delete B (Case 3a): CL has 2 keys, sibling has ≥3 → C moves up to replace B, E moves down into CL

### 3. Classifications

| B-tree type | t | Node key range | Children range |
|-------------|---|----------------|----------------|
| 2-3-4 tree | 2 | 1–3 keys | 2–4 children |
| General B-tree | t ≥ 2 | t-1 to 2t-1 keys | t to 2t children |
| B*-tree | t | ≥ 2/3 full | — |
| B+-tree | — | internal: keys only | leaves: satellite data |

### 4. Comparisons

| Dimension | BST | RBT | B-tree |
|-----------|-----|-----|--------|
| Branching factor | 2 | 2 | t to 2t (large) |
| Height | O(n) worst | O(lg n) | O(logt n) |
| Disk accesses | O(n) worst | O(lg n) | O(logt n) |
| Node size | 2 children | 2 children | 1 disk block |
| Self-balancing | No | Yes (color) | Yes (splits/merges) |
| Increase height | At leaves | At leaves | At root (split) |

### 5. Formulas

- **h ≤ logt ((n+1)/2)**
- Derived from: n ≥ 1 + (t-1)(2 + 2t + 2t² + … + 2t^(h-1)) = 1 + 2(t-1)(t^h - 1)/(t - 1) = 2t^h - 1 ⇒ n ≥ 2t^h - 1 ⇒ t^h ≤ (n+1)/2 ⇒ h ≤ logt ((n+1)/2)

### 6. Rules/Laws/Theorems



### 7. Data Structures — Operations Table

| Operation | Disk Accesses | CPU Time |
|-----------|--------------|----------|
| B-TREE-SEARCH | O(logt n) | O(t logt n) |
| B-TREE-CREATE | O(1) | O(1) |
| B-TREE-INSERT | O(logt n) | O(t logt n) |
| B-TREE-DELETE | O(logt n) | O(t logt n) |
| B-TREE-SPLIT-CHILD | O(1) | Θ(t) |

### 8. Visual Patterns






- (a)→(b): Insert B into leaf (simple)
- (b)→(c): Insert Q, split full node RSTUV → root gains T
- (c)→(d): Insert L, root full → split, height grows
- (d)→(e): Insert F, split full node ABCDE before descent

- (a)→(b): Delete F from leaf (Case 1)
- (b)→(c): Delete M from internal node, predecessor L replaces it (Case 2a)
- (c)→(d): Delete G, merge children (Case 2c)
- (d)→(e): Delete D, merge with sibling (Case 3b)
- (e)→(e0): Empty root deleted, height shrinks
- (e0)→(f): Delete B, borrow from sibling (Case 3a)

### 9. Edge Cases

- **t = 1 not allowed**: would allow 0 keys in non-root nodes, violating B-tree structure
- **Root split** (only way height increases): root full → create new empty root, split old root
- **Empty root after merge** (cases 2c, 3b): delete root, height decreases
- **Underflow prevention**: always ensure t keys (not t-1) before descending; root exception
- **Duplicate keys**: key ordering uses ≤ (x.key1 ≤ x.key2 ≤ ...)
- **Sentinel keys**: not used in B-tree (sentinels are disk-level)
- **B-TREE-SEARCH linear vs binary**: linear O(t logt n) per node; binary search within node reduces CPU to O(lg n) independent of t

### 10. Empirical Evidence

- Disk specs: 5400-15000 RPM; one rotation = 4-8.33ms; main memory access ~50ns (5 orders of magnitude faster)
- SSD vs magnetic: SSDs faster but magnetic cheaper per TB
- Typical branching factors: 50-2000 depending on key/block size ratio
- With root cached in memory, height-2 B-tree (1001 branching factor) needs at most 2 disk accesses for any key

### 11. Cross-Chapter Dependencies

- **Chapter 13 (RBT)**: B-trees contrasted with red-black trees
- **Chapter 12 (BST)**: TREE-SEARCH generalized; BST insertion/deletion concepts
- **Chapter notes reference**: Knuth [261], Aho-Hopcroft-Ullman [5], Sedgewick-Wayne [402], Comer [99], Guibas-Sedgewick [202]

### 12. Dates & People

- **J. E. Hopcroft** (1970): invented 2-3 trees (precursor)
- **Bayer and McCreight** (1972): introduced B-trees; no explanation of name
- **Comer** [99]: comprehensive survey of B-trees
- **Bender, Demaine, Farach-Colton** [47]: cache-oblivious B-trees

### 13. Proof Patterns

- **Height bound proof**: Minimum keys in each level; geometric series; double-counting
- **Single-pass guarantee**: Split full nodes on way down (insert) / ensure t keys on way down (delete) to avoid backing up
- **One-pass argument**: While going down the tree, if child full (insert) or child underfull (delete), fix immediately so next recursion level is safe

### 14. Design Paradigms

- **Disk-aware design**: Node size = disk block; minimize disk accesses (dominant cost)
- **Top-down growth**: Height increases only at root (not at leaves like BST)
- **Preemptive splitting**: Split full nodes before descending to avoid back-up
- **Preemptive merging/borrowing**: Ensure enough keys before descending to avoid underflow
- **2-phase operations**: Phase 1 (tree modification) + Phase 2 (structural fix-up)

### 15. Case Studies


### 16. Ethics


### 17. End-of-Chapter Material

#### Exercises 18.1



- t=2: root can have 1-3 keys; non-root can have 1-3 keys
- Possible trees: (a) root [3], left [1,2], right [4,5]; (b) root [2,4], left [1], middle [3], right [5]; (c) root [1,2,3,4,5] (single node, height 0)

- Max per node: 2t-1
- Root max = 2t-1; each of its children max = 2t-1; total nodes = 1 + (2t) + (2t)² + ... + (2t)^h = (2t)^(h+1)-1)/(2t-1)
- Total max keys = (2t-1) * ((2t)^(h+1)-1)/(2t-1) = (2t)^(h+1) - 1


#### Exercises 18.2

- t=2: internal nodes 2-4 children, 1-3 keys
- Sequence of splits and inserts shown in text Figure 18.7 patterns.
- Key splits occur when a node reaches 3 keys (2t-1 = 3); median moves up.

- DISK-READ redundant when block already in memory (e.g., root always cached)
- DISK-WRITE redundant when writing block that hasn't changed (though typically only write modified blocks)






#### Exercises 18.3

- Delete C: leaf node, Case 1. 
- Delete P: internal node, Case 2a or 2b depending on children.
- Delete V: leaf or internal, appropriate case.

```
```

#### Problems

- (a) Simple stack: n pushes, n pops → O(n) disk accesses per operation worst-case
- (b) One block in memory: n pushes worst-case O(n/m) disk accesses
- (c) Same for mixed pushes/pops
- (d) Two blocks in memory: amortized O(1/m) disk accesses per operation

- (a) Maintain subtree height: `x.height = 1 + max(x.c1.height, ..., x.cx.n+1.height)`
- (b) Join: compare heights of roots; if equal → new root with key k; if different → insert k into taller tree at appropriate depth
- (c) Path p breaks into subtrees by going left/right at each node
- (d) Split: traverse path from root to k, collect subtrees, use join to assemble

#### Chapter Notes
- Hopcroft (1970): 2-3 trees
- Bayer & McCreight (1972): B-trees
- Knuth [261], Aho-Hopcroft-Ullman [5], Sedgewick-Wayne [402] for further reading
- Comer [99]: comprehensive survey
- Guibas-Sedgewick [202]: RBT ↔ 2-3-4 tree relationship
- Bender, Demaine, Farach-Colton [47]: cache-oblivious B-trees

---

## Chapter 19: Disjoint Sets

### 1. Named Entities

| Term | Definition |
|------|-----------|
| **Disjoint-set data structure** | Maintains collection of disjoint dynamic sets |
| **Representative** | Some member of a set; identifies the set |
| **Disjoint-set forest** | Tree-based representation; each set = rooted tree |
| **Union by rank** | Heuristic: root with smaller rank becomes child of root with larger rank |
| **Path compression** | Heuristic: during FIND-SET, make each node on find path point directly to root |
| **Find path** | Simple path from node up to root |
| **Rank** | Upper bound on node height (number of edges to deepest descendant leaf) |
| **Inverse Ackermann α(n)** | Lowest level k where Ak(1) ≥ n; ≤ 4 for all practical n |
| **Ackermann function Ak(j)** | Very fast-growing function used to bound disjoint-set complexity |
| **Level k** | Parameter of Ak(j) |
| **Functional iteration** | Notation: Aⁱ(j) = A applied i times |
| **Weighted-union heuristic** | Always append shorter list to longer (linked-list representation) |
| **Offline minimum problem** | Determine which key each EXTRACT-MIN returns given full sequence (Problem 19-1) |
| **LCA (lowest common ancestor)** | In a rooted tree, deepest ancestor of both u and v |
| **Tarjan's offline LCA** | Algorithm using disjoint-set forest to find LCA for all pairs |

### 2. Algorithms — FULL Steps

#### MAKE-SET(x)
- **Input**: element x (not already in a set)
- **Output**: creates new singleton set {x}
- **Time**: O(1)

```
MAKE-SET(x)
1  x.p = x
2  x.rank = 0
```

#### UNION(x, y)
- **Input**: elements x and y from different sets
- **Output**: unites their sets
- **Time**: O(α(n)) amortized

```
UNION(x, y)
1  LINK(FIND-SET(x), FIND-SET(y))
```

#### LINK(x, y)
- **Input**: roots x and y
- **Time**: O(1) actual

```
LINK(x, y)
1  if x.rank > y.rank
2      y.p = x
3  else
4      x.p = y
5      if x.rank == y.rank
6          y.rank = y.rank + 1
```

#### FIND-SET(x) — with path compression
- **Input**: element x
- **Output**: representative of x's set (root)
- **Time**: O(α(n)) amortized

```
FIND-SET(x)
1  if x ≠ x.p
2      x.p = FIND-SET(x.p)
3  return x.p
```

**Concrete Example** (Figure 19.5):
- Before: tree with root (no parent shown), node a at depth 3, nodes b,c,d on path
- FIND-SET(a): recurses up a → b → c → d → root, then unwinds setting a.p=root, b.p=root, c.p=root, d.p=root
- After: all nodes on find path point directly to root

#### CONNECTED-COMPONENTS(G)
```
CONNECTED-COMPONENTS(G)
1  for each vertex v ∈ G.V
2      MAKE-SET(v)
3  for each edge (u,v) ∈ G.E
4      if FIND-SET(u) ≠ FIND-SET(v)
5          UNION(u, v)
```

#### SAME-COMPONENT(u, v)
```
SAME-COMPONENT(u, v)
1  if FIND-SET(u) == FIND-SET(v)
2      return TRUE
3  else
4      return FALSE
```

#### Linked-list representation with weighted-union heuristic

```
MAKE-SET-LIST(x)
1  x.list = new list with x as only member
2  x.list.head = x
3  x.list.tail = x
4  x.list.size = 1
5  x.list.rep = x
6  x.next = NIL
7  x.set-ptr = x.list

FIND-SET-LIST(x)
1  return x.set-ptr.rep

UNION-LIST(x, y)
1  set_x = FIND-SET-LIST(x)
2  set_y = FIND-SET-LIST(y)
3  // assume set_x.size ≥ set_y.size (weighted-union)
4  set_x.tail.next = set_y.head
5  set_x.tail = set_y.tail
6  set_x.size = set_x.size + set_y.size
7  for each member z of set_y
8      z.set-ptr = set_x
9  set_x.rep = set_x.head.set-ptr.rep
```

### 3. Classifications

| Representation | MAKE-SET | FIND-SET | UNION (simple) | UNION (weighted) |
|---------------|----------|----------|----------------|------------------|
| Linked-list (simple) | O(1) | O(1) | O(n) worst | — |
| Linked-list (weighted) | O(1) | O(1) | O(lg n) amortized per op | O(m + n lg n) total |
| Forest (no heuristics) | O(1) | O(n) worst | O(1) basic | O(m n) worst |
| Forest (union by rank only) | O(1) | O(lg n) | O(1) link | O(m lg n) |
| Forest (path compression only) | O(1) | O(log_{2+f/n} n) | O(1) link | Θ(n + f·log_{2+f/n}n) |
| Forest (both heuristics) | O(1) | O(α(n)) amortized | O(α(n)) amortized | O(m α(n)) |

### 4. Comparisons

| Dimension | Linked-list (simple) | Linked-list (weighted) | Forest (both heuristics) |
|-----------|---------------------|----------------------|--------------------------|
| MAKE-SET | O(1) | O(1) | O(1) |
| FIND-SET | O(1) | O(1) | O(α(n)) amortized |
| UNION worst-case | O(n) | O(n) | O(α(n)) amortized |
| Sequence of m ops | O(m + n²) | O(m + n lg n) | O(m α(n)) |
| Space | O(n) | O(n) | O(n) |
| Implementation complexity | Low | Low | Medium |

### 5. Formulas

**Ak(j) (Ackermann-like function)**:
- A₀(j) = j + 1
- Aₖ(0) = Aₖ₋₁(1) for k ≥ 1
- Aₖ(j) = Aₖ₋₁^(j+1)(1) for k ≥ 1, j ≥ 1
  where Aₖ₋₁^(i)(1) = Aₖ₋₁(Aₖ₋₁(...(1)...)) iterated i times

**Closed forms**:
- A₁(j) = 2j + 1
- A₂(j) = 2^(j+1)(j+1) - 1

**Values**:
- A₀(1) = 2
- A₁(1) = 3
- A₂(1) = 7
- A₃(1) = 2047
- A₄(1) = A₃(2047) = 2²⁰⁵⁹ - 1 > 10⁸⁰ (atoms in observable universe)

**α(n) (inverse Ackermann)**:
- α(n) = min{k ≥ 0 : Aₖ(1) ≥ n}
- α(n) ≤ 4 for all practical n (n < A₄(1) ≈ huge)
- Only for astronomically large n does α(n) > 4

**Rank properties**:
- x.rank ≤ x.p.rank (strict if x not root)
- ranks are ≤ n-1 (weak bound); actually ≤ ⌊lg n⌋ (Exercise 19.4-2)
- rank increases only during LINK when roots have equal rank

### 6. Rules/Laws/Theorems

**Theorem 19.1 (Weighted-union linked-list)**:
> Using linked-list representation and weighted-union heuristic, a sequence of m MAKE-SET, UNION, FIND-SET operations (n of which are MAKE-SET) takes O(m + n lg n) time.

*Proof*: Each element's set-pointer is updated at most ⌈lg n⌉ times (doubling set size each time). UNION updates O(n lg n) total pointers. Each MAKE-SET/FIND-SET is O(1). Total: O(m + n lg n).

**Lemma 19.2**: A₁(j) = 2j + 1 for j ≥ 1.

**Lemma 19.3**: A₂(j) = 2^(j+1)(j+1) - 1 for j ≥ 1.

**Lemma 19.4 (Rank monotonicity)**:
> For all nodes x: x.rank ≤ x.p.rank, strict if x ≠ x.p. x.rank is initially 0, increases only while x is a root, and then never changes. x.p.rank monotonically increases.

**Corollary 19.5**: Ranks strictly increase along any simple path toward a root.

**Lemma 19.6**: Every node has rank ≤ n - 1.

**Lemma 19.7 (UNION → LINK conversion)**:
> Converting each UNION into 2 FIND-SET + 1 LINK preserves asymptotic bound (m ≤ 3m').

**Lemma 19.8 (Potential bounds)**:
> 0 ≤ ϕq(x) ≤ α(n)·x.rank for every node x after q operations.

**Corollary 19.9**:
> If x is not a root and x.rank > 0, then ϕq(x) < α(n)·x.rank.

**Lemma 19.10 (Potential monotonicity)**:
> If x is not a root and qth op is LINK or FIND-SET:
> - ϕq(x) ≤ ϕq₋₁(x) (potential never increases)
> - If x.rank ≥ 1 and level(x) or iter(x) changes, ϕq(x) ≤ ϕq₋₁(x) - 1

**Lemma 19.11**: Amortized cost of MAKE-SET = O(1).

**Lemma 19.12**: Amortized cost of LINK = O(α(n)).

**Lemma 19.13**: Amortized cost of FIND-SET = O(α(n)).

**Theorem 19.14 (Main result)**:
> A sequence of m MAKE-SET, UNION, FIND-SET operations (n of which are MAKE-SET) on a disjoint-set forest with union by rank and path compression runs in O(m α(n)) time.

### 7. Data Structures — Operations Table


| Operation | Actual Cost | Amortized Cost | Notes |
|-----------|-------------|----------------|-------|
| MAKE-SET | O(1) | O(1) | Creates singleton tree, rank=0 |
| FIND-SET | O(path length) | O(α(n)) | Two-pass: find root + compress path |
| LINK | O(1) | O(α(n)) | Union by rank (roots only) |
| UNION | O(α(n)) | O(α(n)) | = LINK(FIND-SET(x), FIND-SET(y)) |


| Operation | Time | Notes |
|-----------|------|-------|
| MAKE-SET | O(1) | |
| FIND-SET | O(1) | Via pointer to set object |
| UNION | O(size of smaller list) | Amortized O(lg n) per element |

### 8. Visual Patterns






### 9. Edge Cases

- **Self-parent**: root.p = root
- **Rank 0 singleton**: initial rank = 0
- **Equal rank UNION**: second root becomes child of first? Actually if x.rank == y.rank: x.p = y (y becomes parent); y.rank incremented by 1
- **Path compression on root**: FIND-SET(root) returns root without changes
- **α(n) ≤ 4**: for all practical purposes; the proof of O(mα(n)) uses α(n) as maximum level
- **Potential function edge cases**: if node is root → ϕ(x) = α(n)·x.rank; if x.rank=0 → ϕ(x)=0

### 10. Empirical Evidence

- Table of Ak(1) values: A₀(1)=2, A₁(1)=3, A₂(1)=7, A₃(1)=2047, A₄(1) > 10⁸⁰
- α(n) ≤ 4 for all n < A₄(1) (vastly larger than atoms in universe)

### 11. Cross-Chapter Dependencies

- **Section 16.3 (Potential method)**: Used for amortized analysis of disjoint-set forest
- **Section B.4 (Graph theory)**: Connected components definition
- **Section 20.3 (DFS)**: DFS can compute connected components faster for static graphs (Ex 19.1-1 reference to Ex 20.3-12)
- **Equation (3.30)**: Functional iteration notation

### 12. Dates & People

- **R. E. Tarjan** [427, 429]: first tight upper bound using inverse Ackermann
- **Hopcroft and Ullman** [5, 227]: proved O(m lg* n) bound earlier
- **Tarjan** [431]: later analysis adapted in Section 19.4
- **Kozen** [270]: basis for Tarjan's later analysis
- **Harfst and Reingold** [209]: potential-based version of Tarjan's bound
- **Tarjan and van Leeuwen** [432]: path-compression variants (one-pass methods)
- **Goel et al.** [182]: random linking yields same bound
- **Gabow and Tarjan** [166]: O(m) for certain applications
- **Tarjan** [428]: lower bound; generalized by **Fredman and Saks** [155]

### 13. Proof Patterns


- Define level(x) = max{k : Aₖ(x.rank) ≤ x.p.rank}
- Define iter(x) = max{i : A_level(x)^(i)(x.rank) ≤ x.p.rank}
- Potential: ϕ(x) = (α(n) - level(x))·x.rank - iter(x) (non-root, rank ≥ 1)
- ϕ(x) = α(n)·x.rank (root or rank 0)
- Show: non-root potential never increases; drops by ≥1 when level/iter changes


### 14. Design Paradigms

- **Amortized analysis via potential function**: Prepaid "potential" accounts for future path compression
- **Heuristic combination**: Union by rank (keep trees shallow) + path compression (make future finds cheaper)
- **Two-pass method**: FIND-SET: first pass finds root, second pass compresses
- **Representative choice**: For linked-list, head of list; for forest, tree root

### 15. Case Studies




### 16. Ethics


### 17. End-of-Chapter Material

#### Exercises 19.1

- After each edge, maintain sets. Final connected components can be determined by tracing UNION operations.



#### Exercises 19.2







#### Exercises 19.3


```
```

- Insert n elements, repeatedly UNION in worst-case order creating tall trees (height ∝ lg n), then FIND-SET on deepest elements. Each FIND-SET traverses Θ(lg n) nodes → Ω(m lg n).



#### Exercises 19.4








#### Problems

- (a) Sequence: 4, 8, E, 3, E, 9, 2, 6, E, E, E, 1, 7, E, 5
  - E1 (after 4,8): min of {4,8} = 4 → extracted[1]=4
  - E2 (after 3): min of {8,3} = 3 → extracted[2]=3
  - E3 (after 9,2,6): min of {8,9,2,6} = 2 → extracted[3]=2
  - E4: min of {8,9,6} = 6 → extracted[4]=6
  - E5: min of {8,9} = 8 → extracted[5]=8
  - E6 (after 1,7): min of {9,1,7} = 1 → extracted[6]=1
  - E7: min of {9,7} = 7 → extracted[7]=7
  - Remaining: 9,5 → but only m=7 E's total. Wait recount: 4,8,E,3,E,9,2,6,E,E,E,1,7,E,5 → E's at positions 3,5,10,11,12,14 → 6 E's, not 7. Let me recount:
  - 6 E's: extracted[1]=4, extracted[2]=3, extracted[3]=2, extracted[4]=6, extracted[5]=8, extracted[6]=1

- (b) Correctness: OFFLINE-MINIMUM assigns each key to the earliest EXTRACT-MIN that could return it; merging K_sets ensures future extractions see remaining keys.
- (c) Implementation: use disjoint-set where each E position is a set; for each key i in order, find which E's set it belongs to via FIND-SET(j); output to extracted[j]; UNION(j, j+1). O(n α(n)).

- (a) Without heuristics: could create chain of n nodes; FIND-DEPTH O(n) → Θ(m²)
- (b) MAKE-TREE(v): MAKE-SET(v), v.d = 0
- (c) FIND-DEPTH(v): FIND-SET(v) modified to compute sum of pseudodistances along path
  ```
  ```
- (d) GRAFT(r, v): UNION(r, v) but need to update pseudodistance of r's root to reflect depth in new tree
- (e) O(m α(n))

- (a) Line 10 executes once per pair: for each pair {u,v}, one node is visited first (WHITE then BLACK); when second is visited (BLACK), LCA printed.
- (b) At call LCA(u), number of sets = depth of u (each ancestor on stack is root of its own set).
- (c) Correctness: When v is BLACK and {u,v} ∈ P, FIND-SET(v) returns the set whose ancestor field is the LCA (the deepest ancestor that has been fully processed and whose subtree contains both u and v).
- (d) Running time: O((n + |P|) α(n)) for disjoint-set ops + O(n + |P|) for tree walk = O((n + |P|) α(n)).

#### Chapter Notes
- Tarjan [427, 429]: first tight O(m α(m,n)) bound
- Hopcroft & Ullman: O(m lg* n)
- Tarjan [431]: adapted analysis in Section 19.4
- Kozen [270]: basis for Tarjan's analysis
- Harfst & Reingold [209]: potential-based version
- Tarjan & van Leeuwen [432]: one-pass path compression variants
- Goel et al. [182]: random linking
- Gabow & Tarjan [166]: O(m) for special cases
- Tarjan [428]: lower bound (inverse Ackermann necessary)
- Fredman & Saks [155]: generalized lower bound

---

## Quick Reference Card

### Ch 17: Order-Statistic Tree
- `OS-SELECT(x,i)`: find i-th smallest, O(lg n)
- `OS-RANK(T,x)`: find rank of x, O(lg n)
- Maintain `x.size = x.left.size + x.right.size + 1`
- Rotations: O(1) to update size

### Ch 17: Interval Tree
- Key = `x.int.low`, extra attr `x.max = max(high, left.max, right.max)`
- `INTERVAL-SEARCH(T,i)`: find any overlapping interval, O(lg n)
- Correctness: interval trichotomy + safe direction Theorem 17.2

### Ch 18: B-Trees
- t = minimum degree; node: t-1 to 2t-1 keys
- Height: h ≤ log_t((n+1)/2)
- INSERT: split full nodes on way down (splits at root increase height)
- DELETE: 6 subcases (1, 2a, 2b, 2c, 3a, 3b); ensure t keys before descending

### Ch 19: Disjoint Sets
- **Union by rank**: smaller rank root → child of larger rank root
- **Path compression**: FIND-SET makes all nodes on path point to root
- **Potential function**: ϕ(x) = (α(n)-level(x))·x.rank - iter(x) [non-root, rank≥1]; α(n)·x.rank [root or rank=0]
- **Final bound**: O(m α(n)) for m ops, n MAKE-SETs
- **α(n)** ≤ 4 for all practical n

# CLRS 4th Edition — Chapters 20–25 Comprehensive Study Guide

---

### Ch. 20 — Elementary Graph Algorithms

#### Named Entities
- **Graph G = (V, E)**: set of vertices V and edges E
- **Adjacency-list representation**: array Adj of |V| lists; each edge stored once (directed) or twice (undirected); memory Θ(V+E)
- **Adjacency-matrix representation**: |V| × |V| matrix A = (aᵢⱼ); memory Θ(V²)
- **Weighted graph**: weight function w: E → ℝ
- **Source vertex s**: distinguished start vertex for BFS
- **Distance (BFS)**: smallest number of edges from s to v
- **Shortest-path distance δ(s,v)**: min #edges on any path s⇝v (∞ if unreachable)
- **Predecessor v.π**: parent of v in BFS/DFS tree
- **Breadth-first tree**: predecessor subgraph Gπ = (Vπ, Eπ) where Vπ = {v∈V: v.π≠NIL}∪{s}, Eπ = {(v.π, v): v∈Vπ−{s}}
- **Depth-first forest**: collection of depth-first trees; predecessor subgraph Gπ = (V, Eπ) where Eπ = {(v.π, v): v∈V and v.π≠NIL}
- **Timestamps**: v.d (discovery time), v.f (finish time), integers 1..2|V|
- **Parenthesis structure**: discovery/finish intervals are properly nested (Theorem 20.7)
- **Edge types (DFS)**: tree, back, forward, cross
- **Topological sort**: linear ordering of dag vertices where u before v if (u,v)∈E
- **Strongly connected component (SCC)**: maximal set C⊆V s.t. ∀u,v∈C: u⇝v and v⇝u
- **Transpose graph Gᵀ**: edges reversed
- **Component graph G_SCC**: one vertex per SCC, edges between SCCs
- **Semiconnected**: ∀u,v∈V, u⇝v or v⇝u

#### Processes/Algorithms

**BFS (Breadth-First Search)**
```
BFS(G, s)
1 for each vertex u ∈ G.V – {s}
2   u.color = WHITE
3   u.d = ∞
4   u.π = NIL
5 s.color = GRAY
6 s.d = 0
7 s.π = NIL
8 Q = ∅
9 ENQUEUE(Q, s)
10 while Q ≠ ∅
11   u = DEQUEUE(Q)
12   for each vertex v ∈ G.Adj[u]
13     if v.color == WHITE
14       v.color = GRAY
15       v.d = u.d + 1
16       v.π = u
17       ENQUEUE(Q, v)
18   u.color = BLACK
```
- **Input**: graph G (adjacency list), source vertex s
- **Output**: distances v.d, parent pointers v.π, breadth-first tree
- **Complexity**: O(V+E)
- **Example** (Figure 20.3): undirected graph, vertices explored wave-by-wave from source. Queue maintains frontier of gray vertices with d values of form k, k, ..., k, k+1, k+1, ..., k+1

**DFS (Depth-First Search)**
```
DFS(G)
1 for each vertex u ∈ G.V
2   u.color = WHITE
3   u.π = NIL
4 time = 0
5 for each vertex u ∈ G.V
6   if u.color == WHITE
7     DFS-VISIT(G, u)

DFS-VISIT(G, u)
1 time = time + 1
2 u.d = time
3 u.color = GRAY
4 for each vertex v ∈ G.Adj[u]
5   if v.color == WHITE
6     v.π = u
7     DFS-VISIT(G, v)
8 time = time + 1
9 u.f = time
10 u.color = BLACK
```
- **Input**: graph G (adjacency list)
- **Output**: timestamps u.d, u.f; parent pointers; depth-first forest
- **Complexity**: Θ(V+E)
- **Example** (Figure 20.4): directed graph, edges classified as T (tree), B (back), F (forward), C (cross). Timestamps shown inside vertices.

**Topological Sort**
```
TOPOLOGICAL-SORT(G)
1 call DFS(G) to compute finish times v.f for each vertex v
2 as each vertex is finished, insert it onto the front of a linked list
3 return the linked list of vertices
```
- **Input**: directed acyclic graph
- **Output**: topological ordering of vertices
- **Complexity**: Θ(V+E)
- **Correctness**: Lemma 20.11 — dag iff no back edges; Theorem 20.12 — if (u,v)∈E then v.f < u.f

**Strongly Connected Components**
```
STRONGLY-CONNECTED-COMPONENTS(G)
1 call DFS(G) to compute finish times u.f for each vertex u
2 create Gᵀ
3 call DFS(Gᵀ), but in the main loop of DFS, consider vertices in order of decreasing u.f
4 output the vertices of each tree in the depth-first forest formed in line 3 as a separate SCC
```
- **Input**: directed graph G
- **Output**: SCCs of G
- **Complexity**: Θ(V+E)
- **Key**: component graph G_SCC is acyclic (Lemma 20.13)

**Print Path**
```
PRINT-PATH(G, s, v)
1 if v == s
2   print s
3 elseif v.π == NIL
4   print "no path from" s "to" v "exists"
5 else PRINT-PATH(G, s, v.π)
6 print v
```
- **Complexity**: linear in path length

#### Classifications
- **Graph types**: directed, undirected, weighted, unweighted, sparse (|E| << |V|²), dense (|E| ≈ |V|²), dag, connected, strongly connected
- **Search types**: BFS (breadth-first), DFS (depth-first), single-source (BFS), multi-source (DFS)
- **Edge types (DFS)**: tree, back, forward, cross
- **Edge types (BFS on undirected)**: tree, cross only
- **Edge types (BFS on directed)**: tree, back, cross (no forward edges)

#### Comparisons
| Dimension | BFS | DFS |
|---|---|---|
| Data structure | Queue (FIFO) | Stack (implicit via recursion) |
| Vertex coloring | WHITE→GRAY→BLACK | WHITE→GRAY→BLACK |
| Distances | Shortest path by #edges | Not computed |
| Timestamps | None | Discovery u.d, finish u.f |
| Tree | Single BFS tree | DFS forest (multiple trees) |
| Edge classification | Tree, cross (undirected); tree, back, cross (directed) | Tree, back, forward, cross (directed); tree, back (undirected) |
| Complexity | O(V+E) | Θ(V+E) |
| Applications | Shortest paths in unweighted graphs, Prim's, Dijkstra's | Topological sort, SCC, articulation points |
| Revisiting | Once per vertex | Once per vertex |

| Dimension | Adjacency List | Adjacency Matrix |
|---|---|---|
| Memory | Θ(V+E) | Θ(V²) |
| Edge lookup | O(degree(u)) worst-case | O(1) |
| Find all edges | Θ(V+E) | Θ(V²) |
| Best for | Sparse graphs | Dense graphs |
| Weighted graphs | Yes (store weight with neighbor) | Yes (store weight in entry) |
| Symmetry (undirected) | Each edge stored twice | A = Aᵀ |

#### Formulas
- Sum of adjacency list lengths (directed): |E|
- Sum of adjacency list lengths (undirected): 2|E|
- Memory adjacency list: Θ(V+E)
- Memory adjacency matrix: Θ(V²)
- BFS distances: v.d = u.d + 1 (when v discovered from u)
- DFS timestamps: 1 ≤ u.d < u.f ≤ 2|V|
- δ(s,v) = min number of edges on path s⇝v
- δ(s,v) ≤ δ(s,u) + 1 for any edge (u,v) ∈ E (Lemma 20.1)

#### Rules/Laws/Theorems
- **Lemma 20.1**: δ(s,v) ≤ δ(s,u) + 1 for any edge (u,v) ∈ E
- **Lemma 20.2**: v.d ≥ δ(s,v) at all times (upper bound property for BFS)
- **Lemma 20.3**: Queue invariant: for queue 〈v₁,...,vᵣ〉, vᵣ.d ≤ v₁.d + 1 and vᵢ.d ≤ vᵢ₊₁.d
- **Corollary 20.4**: d values at enqueue time are monotonically nondecreasing
- **Theorem 20.5 (Correctness of BFS)**: BFS discovers all vertices reachable from s, v.d = δ(s,v) for all v∈V, and the path s⇝v.π→v is a shortest path
- **Lemma 20.6**: BFS produces a breadth-first tree
- **Theorem 20.7 (Parenthesis theorem)**: For any two vertices u,v, intervals [u.d,u.f] and [v.d,v.f] are either disjoint or one contains the other (nested)
- **Corollary 20.8**: v is a proper descendant of u iff u.d < v.d < v.f < u.f
- **Theorem 20.9 (White-path theorem)**: v is descendant of u iff at time u.d there is a path from u to v consisting entirely of white vertices
- **Theorem 20.10**: In DFS of undirected graph, every edge is either tree or back edge
- **Lemma 20.11**: Directed graph is acyclic iff DFS yields no back edges
- **Theorem 20.12**: TOPOLOGICAL-SORT produces a topological sort of a dag
- **Lemma 20.13**: Distinct SCCs: if there is a path from C to C', there cannot be a path from C' to C
- **Lemma 20.14**: If edge (u,v)∈E with u∈C', v∈C, then f(C') > f(C)
- **Corollary 20.15**: If f(C) > f(C'), then Gᵀ has no edge from C to C'
- **Theorem 20.16**: STRONGLY-CONNECTED-COMPONENTS correctly computes SCCs

#### Data Structures
- **Adjacency list**: Array of linked lists (or hash tables, Exercise 20.1-8)
- **Adjacency matrix**: |V| × |V| array
- **Queue (BFS)**: FIFO queue for frontier; contains gray vertices
- **Linked list (topological sort)**: stores vertices in reverse finish order
- **Vertex attributes**: color (WHITE/GRAY/BLACK), d (distance/timestamp), f (finish time), π (predecessor)

#### Edge Cases
- Disconnected graphs: BFS only reaches vertices reachable from s; DFS continues with new sources
- Self-loops: treated as back edges in DFS
- Graph with vertices unreachable: δ(s,v) = ∞
- BFS with multiple sources: not standard but possible (see depth-first search behavior)
- Directed graph with no source specified: DFS iterates over all vertices
- Complete binary tree representation (Exercise 20.1-2)

#### Proof Patterns
- **Induction on queue operations**: Lemma 20.2 (induction on ENQUEUE), Lemma 20.3 (induction on queue operations)
- **Contradiction / alternative-case**: Theorem 20.5 — assume v with minimal δ(s,v) has v.d > δ(s,v), consider cases (white/gray/black)
- **White-path theorem**: both directions — forward is trivial (via nested intervals), backward uses contrapositive-like reasoning
- **Parenthesis nesting**: Theorem 20.7 — case analysis based on discovery order

#### End-of-Chapter Material

**Exercises 20.1**:
1. Out-degree: O(V+E) scanning all adjacency lists; in-degree: O(V+E) with extra array
2. Adjacency list and matrix for complete binary tree on 7 vertices
3. Compute Gᵀ: adjacency list O(V+E), adjacency matrix O(V²)
4. Multigraph to simple graph O(V+E)
5. Square of graph G²: adjacency list O(V(V+E)), adjacency matrix O(V³)
6. Universal sink in O(V) using adjacency matrix
7. Incidence matrix B: BBᵀ entries
8. Hash tables for adjacency lists: expected O(1) edge lookup

**Exercises 20.2**:
1. BFS on directed graph with source vertex 3
2. BFS on undirected Figure 20.3 with source u (alphabetical order)
3. Single bit for color suffices; remove line 18 still works; eliminate colors using d values
4. BFS with adjacency matrix: O(V²)
5. d values independent of adjacency list order; tree depends on order
6. Example where BFS tree cannot be produced
7. Wrestler rivalry: O(n+r) using BFS (bipartite testing)
8. Tree diameter: efficient algorithm using two BFS runs

**Exercises 20.3**:
1. 3×3 color chart for directed and undirected DFS
2. DFS on Figure 20.6 with alphabetical order
3. Parenthesis structure of Figure 20.4
4. Single bit for color; remove line 10 still works
5. Edge classification using timestamps
6. Rewrite DFS iteratively using stack
7-8 Counterexamples for DFS conjectures
9. Print edge types in DFS
10. Vertex in depth-first tree containing only u
11. Maze traversal with pennies O(V+E)
12. Connected components labeling using DFS
13. Singly connected graph detection

**Exercises 20.4**:
1. Topological sort of Figure 20.8
2. Count simple paths in dag O(V+E)
3. Detect cycle in undirected graph O(V)
4. Does TOPOLOGICAL-SORT minimize "bad" edges?
5. In-degree-based topological sort O(V+E)

**Exercises 20.5**:
1. How SCC count changes with new edge
2. SCC on Figure 20.6
3. Professor Bacon's modification (incorrect)
4. ((Gᵀ)_SCC)ᵀ = G_SCC
5. Compute component graph O(V+E)
6. Minimize edges preserving SCC structure
7. Semiconnected graph algorithm
8. Maximum Δℓ(s,t) O(V+E)

**Problems**:
- 20-1: Edge classification by BFS
- 20-2: Articulation points, bridges, biconnected components
- 20-3: Euler tour
- 20-4: Reachability
- 20-5: Planar graph insertion and querying

---

### Ch. 21 — Minimum Spanning Trees

#### Named Entities
- **Minimum spanning tree (MST)**: acyclic subset T⊆E connecting all vertices minimizing total weight w(T) = Σ_{(u,v)∈T} w(u,v)
- **Safe edge**: edge that can be added to A while maintaining A ⊆ some MST
- **Cut (S, V−S)**: partition of V
- **Edge crosses cut**: one endpoint in S, other in V−S
- **Cut respects A**: no edge of A crosses the cut
- **Light edge crossing a cut**: edge with minimum weight among those crossing
- **Forest GA = (V, A)**: acyclic graph of selected edges (a forest of trees)
- **Kruskal's algorithm**: greedy MST algorithm using disjoint sets
- **Prim's algorithm**: greedy MST algorithm using priority queue
- **Borůvka's algorithm**: earliest MST algorithm (1926)

#### Processes/Algorithms

**Generic MST**
```
GENERIC-MST(G, w)
1 A = ∅
2 while A does not form a spanning tree
3   find an edge (u,v) that is safe for A
4   A = A ∪ {(u,v)}
5 return A
```
- **Loop invariant**: A is a subset of some minimum spanning tree
- Iterates |V|−1 times

**Kruskal's Algorithm**
```
MST-KRUSKAL(G, w)
1 A = ∅
2 for each vertex v ∈ G.V
3   MAKE-SET(v)
4 create a single list of the edges in G.E
5 sort the list of edges into monotonically increasing order by weight w
6 for each edge (u,v) taken from the sorted list in order
7   if FIND-SET(u) ≠ FIND-SET(v)
8     A = A ∪ {(u,v)}
9     UNION(u,v)
10 return A
```
- **Input**: connected, undirected graph G with weight function w
- **Output**: MST edges A
- **Complexity**: O(E lg V) using disjoint-set forest with union-by-rank and path compression
- **Example** (Figure 21.4): sorts edges, processes in ascending weight; adds edge if it connects two different trees

**Prim's Algorithm**
```
MST-PRIM(G, w, r)
1 for each vertex u ∈ G.V
2   u.key = ∞
3   u.π = NIL
4 r.key = 0
5 Q = ∅
6 for each vertex u ∈ G.V
7   INSERT(Q, u)
8 while Q ≠ ∅
9   u = EXTRACT-MIN(Q)
10  for each vertex v ∈ G.Adj[u]
11    if v ∈ Q and w(u,v) < v.key
12      v.π = u
13      v.key = w(u,v)
14      DECREASE-KEY(Q, v, w(u,v))
```
- **Input**: connected, undirected graph G, weight function w, root r
- **Output**: MST edges A = {(v, v.π) : v ∈ V – {r}}
- **Complexity**: O(E lg V) with binary heap; O(E + V lg V) with Fibonacci heap
- **Example** (Figure 21.5): starts from root a, grows tree by adding light edge crossing cut (V−Q, Q)

#### Classifications
- **Greedy algorithms**: Kruskal (edge-based, sorts edges), Prim (vertex-based, grows tree)
- **MST algorithms**: Generic, Kruskal, Prim, Borůvka, Chazelle's (O(E α(E,V)))
- **Graph types for MST**: connected, undirected, weighted

#### Comparisons
| Dimension | Kruskal | Prim |
|---|---|---|
| Approach | Edge-based (forest of trees) | Vertex-based (single growing tree) |
| Data structure | Disjoint sets (union-find) | Min-priority queue (binary/Fibonacci heap) |
| Edge selection | Global minimum-weight edge connecting two components | Minimum-weight edge connecting tree to nontree vertex |
| Complexity | O(E lg V) | O(E lg V) binary heap; O(E+V lg V) Fibonacci heap |
| Processing order | Sort edges by weight | Extract min from priority queue |
| Memory | O(V+E) | O(V+E) |
| Similar to | Connected-components algorithm | Dijkstra's algorithm |

#### Formulas
- Weight of tree T: w(T) = Σ_{(u,v)∈T} w(u,v)
- Number of edges in MST: |V| − 1
- Number of iterations of GENERIC-MST: |V| − 1
- Kruskal complexity: O(E lg E) = O(E lg V)
- Prim complexity (binary heap): O(V lg V + E lg V) = O(E lg V)
- Prim complexity (Fibonacci heap): O(E + V lg V)

#### Rules/Laws/Theorems
- **Theorem 21.1 (Cut property)**: If A ⊆ some MST, cut (S, V−S) respects A, and (u,v) is a light edge crossing the cut, then (u,v) is safe for A
  - **Proof sketch**: Let T be MST containing A. If T contains (u,v), done. Otherwise, (u,v) forms cycle with path p in T. Since u,v are on opposite sides of cut, some edge (x,y) on p crosses cut. Remove (x,y), add (u,v) to get T'. Since w(u,v) ≤ w(x,y), T' is also MST. A ⊆ T' because (x,y)∉A.
- **Corollary 21.2**: If C = (V_C, E_C) is a component in GA and (u,v) is a light edge connecting C to another component, then (u,v) is safe for A
- **Loop invariant (GENERIC-MST)**: A is subset of some MST
- **Loop invariant (Prim)**: 
  1. A = {(v, v.π) : v ∈ V−{r}−Q}
  2. Vertices in MST are V−Q
  3. For v∈Q with v.π≠NIL, v.key is weight of light edge (v, v.π) connecting v to MST
- **Distinct weights → unique MST** (not guaranteed for non-distinct; Exercise 21.1-6 gives characterization)

#### Data Structures
- **Disjoint-set forest** (Kruskal): union-by-rank + path compression; O(α(V)) per operation
- **Binary min-heap** (Prim): with vertex-to-heap mapping for DECREASE-KEY
- **Fibonacci heap** (Prim): O(1) amortized DECREASE-KEY and INSERT, O(lg V) EXTRACT-MIN

#### Edge Cases
- **Disconnected graph**: MST undefined; algorithms assume connected input
- **Equal-weight edges**: multiple MSTs possible; tie-breaking affects output
- **Negative edge weights**: algorithms still work; positive-weight assumption not needed for MST correctness
- **Single vertex graph**: no edges needed
- **Complete graph**: |E| = Θ(V²)
- **Sparse graph**: |E| = Θ(V); Kruskal O(E lg V) and Prim O(E lg V) similar
- **Nonpositive weights**: Exercise 21.1-7 — minimum-weight connected subgraph may not be a tree

#### Proof Patterns
- **Cut-and-paste**: Theorem 21.1 — remove (x,y), add (u,v); show w(T') ≤ w(T)
- **Loop invariant**: both GENERIC-MST and Prim use loop invariants for correctness
- **Corollary 21.2**: cut (V_C, V−V_C) respects A, light edge is safe
- **Exercise 21.1-3**: edge in MST is light edge crossing some cut

#### End-of-Chapter Material

**Exercises 21.1**:
1. Minimum-weight edge belongs to some MST
2. Converse of Theorem 21.1 is false (counterexample)
3. Edge in MST is light edge crossing some cut
4. Set of all light edges does not necessarily form MST
5. Maximum-weight edge on cycle not in some MST
6. Unique MST iff unique light edge per cut (converse false)
7. Positive weights → MST must be a tree
8. Sorted edge weight lists same for all MSTs
9. Induced subgraph of MST is MST of induced subgraph
10. Decrease weight of edge in T → T remains MST
11. Decrease weight of edge not in T → update MST

**Exercises 21.2**:
1. Kruskal can return any MST with appropriate tie-breaking
2. Prim O(V²) with adjacency matrix (simple array priority queue)
3. Sparse vs dense graph: Fibonacci heap faster only when E = o(V lg V)
4. Kruskal with integer weights 1..|V|: O(E) using counting sort
5. Prim with integer weights 1..|V|: comparably faster
6. Professor Borden's divide-and-conquer (may fail)
7. Uniform [0,1) weights: faster with Prim using van Emde Boas tree
8. Update MST after adding new vertex and edges

**Problems**:
- 21-1: Second-best MST
- 21-2: MST in sparse graphs (MST-REDUCE, preprocessing)
- 21-3: Alternative MST algorithms (MAYBE-MST-A, B, C)
- 21-4: Bottleneck spanning tree (linear time)

---

### Ch. 22 — Single-Source Shortest Paths

#### Named Entities
- **Shortest path problem**: find path of minimum total weight from s to each v∈V
- **Weight function w**: E → ℝ
- **Path weight w(p)**: sum of edge weights along path p
- **Shortest-path weight δ(u,v)**: min weight of any path u⇝v (∞ if none, −∞ if negative-weight cycle reachable)
- **Shortest path**: any path p with w(p) = δ(s,v)
- **Shortest-path estimate v.d**: upper bound on δ(s,v)
- **Predecessor v.π**: previous vertex on current candidate shortest path
- **Shortest-paths tree**: rooted tree where unique path from s to each reachable v is a shortest path
- **Relaxation**: testing whether u improves v's estimate
- **Triangle inequality**: δ(s,v) ≤ δ(s,u) + w(u,v)
- **Negative-weight cycle**: cycle with total weight < 0; makes shortest paths undefined (δ = −∞)
- **Constraint graph**: models difference constraints as graph
- **Difference constraints**: xⱼ − xᵢ ≤ bₖ
- **PERT chart**: program evaluation and review technique; critical path is longest path

#### Processes/Algorithms

**Initialize-Single-Source**
```
INITIALIZE-SINGLE-SOURCE(G, s)
1 for each vertex v ∈ G.V
2   v.d = ∞
3   v.π = NIL
4 s.d = 0
```
- **Complexity**: Θ(V)

**Relax**
```
RELAX(u, v, w)
1 if v.d > u.d + w(u,v)
2   v.d = u.d + w(u,v)
3   v.π = u
```
- **Complexity**: O(1)
- **Effect**: may decrease v.d (tighten upper bound)

**Bellman-Ford Algorithm**
```
BELLMAN-FORD(G, w, s)
1 INITIALIZE-SINGLE-SOURCE(G, s)
2 for i = 1 to |G.V| − 1
3   for each edge (u,v) ∈ G.E
4     RELAX(u, v, w)
5 for each edge (u,v) ∈ G.E
6   if v.d > u.d + w(u,v)
7     return FALSE
8 return TRUE
```
- **Input**: weighted, directed graph G, weight function w, source s
- **Output**: TRUE if no negative-weight cycles reachable from s; FALSE otherwise; v.d = δ(s,v) and v.π form shortest-paths tree
- **Complexity**: O(VE) (or O(V²+VE) with adjacency lists)
- **Example** (Figure 22.4): graph with 5 vertices, 4 passes over edges; after each pass, d values improve
- **Walkthrough**: Pass 1 relaxes all edges (s,t), (s,y), (t,x), (t,y), (t,z), (x,t), (y,x), (y,z), (z,x), (z,s). Final d: s=0, t=2, x=4, y=7, z=−2

**DAG Shortest Paths**
```
DAG-SHORTEST-PATHS(G, w, s)
1 topologically sort the vertices of G
2 INITIALIZE-SINGLE-SOURCE(G, s)
3 for each vertex u ∈ G.V, taken in topologically sorted order
4   for each vertex v ∈ G.Adj[u]
5     RELAX(u, v, w)
```
- **Input**: weighted dag G, source s
- **Output**: shortest-path weights and tree
- **Complexity**: Θ(V+E)
- **Example** (Figure 22.5): 6 vertices topologically sorted left to right; source s; edges relaxed in topological order

**Dijkstra's Algorithm**
```
DIJKSTRA(G, w, s)
1 INITIALIZE-SINGLE-SOURCE(G, s)
2 S = ∅
3 Q = ∅
4 for each vertex u ∈ G.V
5   INSERT(Q, u)
6 while Q ≠ ∅
7   u = EXTRACT-MIN(Q)
8   S = S ∪ {u}
9   for each vertex v ∈ G.Adj[u]
10    RELAX(u, v, w)
11    if the call of RELAX decreased v.d
12      DECREASE-KEY(Q, v, v.d)
```
- **Input**: weighted, directed graph G with nonnegative edge weights, source s
- **Output**: shortest-path weights and predecessor subgraph (shortest-paths tree)
- **Complexity**: O(V²) simple array; O((V+E) lg V) binary heap; O(V lg V + E) Fibonacci heap
- **Example** (Figure 22.6): 5 vertices; source s leftmost; each iteration extracts min-d vertex from Q and relaxes its outgoing edges

**Difference Constraints via Bellman-Ford**
- Construct constraint graph G = (V,E):
  - V = {v₀, v₁, ..., vₙ}
  - E = {(vᵢ, vⱼ) : xⱼ − xᵢ ≤ bₖ} ∪ {(v₀, vᵢ) : i=1..n} with w(v₀,vᵢ)=0
- Run Bellman-Ford on G with source v₀
- If no negative cycle: xᵢ = δ(v₀, vᵢ) is a feasible solution
- Complexity: O((n+1)(n+m)) = O(n²+nm)

#### Classifications
- **Single-source**: find shortest paths from s to all v
- **Single-destination**: find shortest paths from all v to t (reverse edges)
- **Single-pair**: find shortest path u⇝v
- **All-pairs**: find shortest paths for all pairs (Chapter 23)
- **Algorithm types**: Bellman-Ford (general), DAG-shortest (linear), Dijkstra (nonnegative weights), BFS (unit weights)

#### Comparisons
| Dimension | Bellman-Ford | DAG Shortest | Dijkstra |
|---|---|---|---|
| Input constraints | General weights | DAG | Nonnegative weights |
| Complexity | O(VE) | Θ(V+E) | O(V²) to O(V lg V + E) |
| Negative edges | Allowed | Allowed (no cycles) | Not allowed |
| Negative cycle detect | Yes (returns FALSE) | N/A (no cycles) | No |
| Relaxations per edge | |V|−1 | 1 | 1 (min-priority queue) |
| Strategy | Exhaustive | Topological order | Greedy (min-d extraction) |

| Dimension | Adjacency List | Adjacency Matrix |
|---|---|---|
| Bellman-Ford pass | O(V+E) to examine | O(V²) to examine |
| Edge weight access | With each adjacency entry | Matrix entry w[i][j] |

#### Formulas
- Path weight: w(p) = Σ_{k=1..ℓ} w(v_{k−1}, v_k)
- Shortest-path weight: δ(u,v) = min{w(p) : p is path u⇝v}
- Triangle inequality: δ(s,v) ≤ δ(s,u) + w(u,v) for all (u,v)∈E
- v.d relaxation: v.d ≥ δ(s,v) always (upper-bound property)
- After relaxation of (u,v): v.d ≤ u.d + w(u,v)
- Shortest path without cycles: at most |V|−1 edges
- Difference constraints: xⱼ − xᵢ ≤ bₖ
- Bellman-Ford passes needed: maximum edges in any shortest path ≤ |V|−1

#### Rules/Laws/Theorems
- **Lemma 22.1 (Optimal substructure)**: Subpaths of shortest paths are shortest paths
- **Properties of shortest paths and relaxation** (Section 22.5):
  - **Triangle inequality (Lemma 22.10)**: δ(s,v) ≤ δ(s,u) + w(u,v) for any edge (u,v)
  - **Upper-bound property (Lemma 22.11)**: v.d ≥ δ(s,v) always; once v.d = δ(s,v), it never changes
  - **No-path property (Corollary 22.12)**: If no path s⇝v, then v.d = δ(s,v) = ∞ forever
  - **Convergence property (Lemma 22.14)**: If s⇝u→v is a shortest path and u.d = δ(s,u) before relaxing (u,v), then v.d = δ(s,v) afterward
  - **Path-relaxation property (Lemma 22.15)**: If edges of shortest path p = 〈v₀,v₁,...,vₖ〉 are relaxed in order (v₀,v₁),...,(vₖ₋₁,vₖ), then vₖ.d = δ(s,vₖ)
  - **Predecessor-subgraph property (Lemma 22.17)**: Once v.d = δ(s,v) for all v, predecessor subgraph G_π is a shortest-paths tree rooted at s
- **Lemma 22.16**: G_π always forms a rooted tree with root s (acyclic, unique paths)
- **Theorem 22.4 (Correctness of Bellman-Ford)**: If no negative-weight cycles reachable from s, returns TRUE with v.d = δ(s,v) and G_π a shortest-paths tree; otherwise returns FALSE
- **Theorem 22.5 (Correctness of DAG-SHORTEST-PATHS)**: After termination, v.d = δ(s,v) and G_π is a shortest-paths tree
- **Theorem 22.6 (Correctness of Dijkstra)**: With nonnegative weights, terminates with u.d = δ(s,u) for all u∈V
- **Corollary 22.7**: Dijkstra produces shortest-paths tree
- **Lemma 22.8**: Adding constant to all variables preserves feasible solution for difference constraints
- **Theorem 22.9**: Constraint graph with no negative cycle → feasible solution xᵢ = δ(v₀,vᵢ); if negative cycle → no feasible solution

#### Data Structures
- **Predecessor subgraph G_π**: (V_π, E_π) where V_π = {v∈V: v.π≠NIL}∪{s}, E_π = {(v.π, v): v∈V_π−{s}}
- **Min-priority queue (Dijkstra)**: keyed by v.d; implementations: simple array, binary heap, Fibonacci heap
- **Constraint graph**: n+1 vertices, n+m edges

#### Edge Cases
- **Negative weights**: Bellman-Ford handles them; Dijkstra fails
- **Negative-weight cycles reachable from s**: δ(s,v) = −∞; Bellman-Ford returns FALSE
- **Zero-weight cycles**: can be removed without changing path weight
- **Positive-weight cycles**: never in shortest path (remove to get lighter path)
- **Unreachable vertices**: v.d = δ(s,v) = ∞
- **Source on negative-weight cycle**: δ(s,s) = −∞
- **Integer weights bounded by W**: faster implementations possible
- **Graph with edges entering source**: allowed in residual networks (Ch 24)

#### Proof Patterns
- **Path-relaxation property**: induction on edges relaxed along a shortest path
- **Convergence property**: from upper bound + edge relaxation
- **Dijkstra correctness (Theorem 22.6)**: induction on |S|; find first vertex y on shortest path to u not in S; by convergence property y.d = δ(s,y); by greediness u.d ≤ y.d; thus u.d = δ(s,u)
- **Bellman-Ford correctness**: Lemma 22.2 uses path-relaxation property on each vertex's shortest path (≤|V|−1 edges); Theorem 22.4 proves cycle detection by summing inequalities
- **Negative cycle detection**: sum inequalities around cycle gives 0 ≤ w(c) < 0 contradiction
- **Lemma 22.16**: G_π acyclic; if cycle existed, sum estimates around cycle yields negative weight, contradiction

#### End-of-Chapter Material

**Exercises 22.1**:
1. Bellman-Ford with source z on Figure 22.4; then change (z,x) to 4
2. Prove Corollary 22.3
3. Terminate in m+1 passes (m = max min edges in shortest path)
4. Modify Bellman-Ford to set v.d = −∞ for vertices on negative-weight cycle
5. O(VE) Bellman-Ford with adjacency lists
6. δ*(v) = min_u δ(u,v) in O(VE)
7. List vertices of negative-weight cycle

**Exercises 22.2**:
1. DAG-SHORTEST-PATHS with source r on Figure 22.5
2. Process only first |V|−1 vertices in topological order
3. Longest path in weighted-vertex dag
4. Count total paths in dag

**Exercises 22.3**:
1. Dijkstra with source s and source z on Figure 22.2
2. Example where negative edges cause Dijkstra to fail
3. While |Q| > 1 (is it correct?)
4. Q contains only reached vertices
5. Check correctness of Dijkstra output O(V+E)
6. Counterexample: Dijkstra doesn't relax edges in path order
7. Most reliable path (max product of probabilities → logarithms)
8. BFS on expanded graph matches Dijkstra order
9. O(WV+E) Dijkstra with integer 0..W weights
10. O((V+E) lg W) Dijkstra
11. Dijkstra correct if only edges leaving s can be negative
12. O(V+E) Dijkstra with edge weights in [C, 2C]

**Exercises 22.4**:
1. Feasible solution for 6-variable system
2. Feasible solution for 5-variable system
3. Can δ(v₀, vᵢ) be positive?


- 22-1: Yen's improvement to Bellman-Ford (⌈|V|/2⌉ passes)
- 22-2: Nesting boxes (transitive relation, longest chain)
- 22-3: Arbitrage (currency conversion, negative cycles in log graph)
- 22-4: Gabow's scaling algorithm O(E lg W)
- 22-5: Karp's minimum mean-weight cycle algorithm O(VE)
- 22-6: Bitonic shortest paths

---

### Ch. 23 — All-Pairs Shortest Paths

#### Named Entities
- **All-pairs shortest paths**: find δ(i,j) for all i,j ∈ V
- **Predecessor matrix Π = (πᵢⱼ)**: πᵢⱼ is predecessor of j on some shortest path from i
- **Adjacency matrix W = (wᵢⱼ)**: input; wᵢⱼ = 0 if i=j, w(i,j) if (i,j)∈E, ∞ otherwise
- **L^(r) = (ℓᵢⱼ^(r))**: min weight of path from i to j with at most r edges
- **D^(k) = (dᵢⱼ^(k))**: Floyd-Warshall; min weight of path from i to j with intermediate vertices in {1,...,k}
- **T^(k) = (tᵢⱼ^(k))**: transitive closure; 1 if path from i to j with intermediates in {1,...,k}
- **Repeated squaring**: compute L^(n−1) via ⌈lg(n−1)⌉ matrix multiplications
- **Reweighting**: compute ŵ(u,v) = w(u,v) + h(u) − h(v) to make all weights nonnegative
- **Tropical semiring**: min for ⊕, + for ⊗, ∞ for identity of ⊕, 0 for identity of ⊗

#### Processes/Algorithms

```
```
- **Complexity**: Θ(n³)
- **Analogous to matrix multiplication**: + → min, × → +

```
```

```
```
- Squares the matrix each iteration: L^(1), L^(2), L^(4), ..., L^(2^⌈lg(n−1)⌉)
- **Complexity**: Θ(n³ lg n)

```
```
- **Input**: n×n matrix W (edge weights)
- **Output**: D^(n) = (δ(i,j))
- **Complexity**: Θ(n³)
- **Space**: Θ(n²) with in-place update (Exercise 23.2-4)
- **Example** (Figure 23.4): sequence of matrices D^(k) and Π^(k) for graph from Figure 23.1

```
```
- Uses logical OR (∨) and AND (∧) instead of min and +
- **Complexity**: Θ(n³)

```
```
- **Reweighting**: h(v) = δ(s,v) via Bellman-Ford; ensures ŵ(u,v) ≥ 0
- **Complexity**: O(V² lg V + VE) with Fibonacci heap
- **Example** (Figure 23.6): graph G' with new vertex s, h values computed, then Dijkstra from each vertex

#### Classifications
- **DP algorithms**: matrix-multiplication based, Floyd-Warshall
- **Reweighting algorithm**: Johnson's
- **Transitive closure**: specialized boolean version

#### Comparisons
| Dimension | FASTER-APSP | Floyd-Warshall | Johnson |
|---|---|---|---|
| Complexity | Θ(n³ lg n) | Θ(n³) | O(V² lg V + VE) |
| Technique | Repeated squaring (matrix mult) | Dynamic programming (intermediate vertices) | Reweighting + Dijkstra |
| Graph representation | Adjacency matrix | Adjacency matrix | Adjacency lists |
| Negative edges | Allowed (no negative cycles) | Allowed (no negative cycles) | Allowed (no negative cycles) |
| Best for | Dense graphs | Dense graphs | Sparse graphs |
| Constant factor | Small | Small | Larger (uses multiple algorithms) |

#### Formulas
- L^(0): ℓᵢⱼ^(0) = 0 if i=j, ∞ otherwise
- L^(r): ℓᵢⱼ^(r) = min(ℓᵢⱼ^(r−1), minₖ{ℓᵢₖ^(r−1) + wₖⱼ}) = minₖ{ℓᵢₖ^(r−1) + wₖⱼ}
- L^(n−1) = shortest-path weights
- Floyd-Warshall: dᵢⱼ^(k) = min(dᵢⱼ^(k−1), dᵢₖ^(k−1) + dₖⱼ^(k−1))
- Base case dᵢⱼ^(0) = wᵢⱼ
- Transitive closure: tᵢⱼ^(0) = 1 if i=j or (i,j)∈E, else 0; tᵢⱼ^(k) = tᵢⱼ^(k−1) ∨ (tᵢₖ^(k−1) ∧ tₖⱼ^(k−1))
- Reweighting: ŵ(u,v) = w(u,v) + h(u) − h(v)
- Correct shortest path: δ(u,v) = δ̂(u,v) + h(v) − h(u)

#### Rules/Laws/Theorems
- **Lemma 22.1 (Subpaths of shortest paths are shortest paths)**: Used as DP optimal substructure
- **Equation (23.3)**: Recursive definition of ℓᵢⱼ^(r)
- **Equation (23.4)**: δ(i,j) = ℓᵢⱼ^(n−1) (since n−1 edges suffice for simple paths)
- **Associativity**: EXTEND-SHORTEST-PATHS is associative (Exercise 23.1-4)
- **Lemma 23.1 (Reweighting preserves shortest paths)**: ŵ(p) = w(p) + h(v₀) − h(vₖ); a path is shortest with w iff it is shortest with ŵ; negative-weight cycles preserved
- **Theorem 25.14** (used in Hungarian, not this chapter directly but related duality)

#### Data Structures
- **n×n matrix**: W (input), L^(r), D^(k), T^(k), Π (predecessor)
- **Adjacency list (Johnson)**: for Bellman-Ford and Dijkstra subroutines
- **Fibonacci heap (Johnson)**: for Dijkstra's min-priority queue

#### Edge Cases
- **Negative-weight cycles**: all algorithms (except transitive closure) handle via detection; Johnson uses Bellman-Ford to detect
- **No path between vertices**: δ(i,j) = ∞
- **Dense vs sparse graphs**: different algorithms preferred
- **Unweighted graph**: BFS from each vertex = O(V(V+E))
- **Graphs with large integer weights**: slower reweighting may not help
- **Zero-weight edges**: allowed

#### Proof Patterns
- **Dynamic programming recurrence**: Floyd-Warshall based on whether vertex k is intermediate
- **Reweighting**: Lemma 23.1 — ŵ(p) = w(p) + h(v₀) − h(vₖ); since h(v₀) and h(vₖ) independent of path, ordering preserved
- **Johnson correctness**: reweighted edges nonnegative; then Lemma 23.1 guarantees shortest paths preserved

#### End-of-Chapter Material




- 23-1: Transitive closure of dynamic graph (O(V²) per insertion)
- 23-2: Shortest paths in ϵ-dense graphs (d-ary heaps)

---

### Ch. 24 — Maximum Flow

#### Named Entities
- **Flow network G = (V, E)**: directed graph with source s, sink t, capacity c(u,v) ≥ 0
- **Flow f**: function V×V → ℝ satisfying capacity constraint (0 ≤ f(u,v) ≤ c(u,v)) and flow conservation (∀u∈V−{s,t}: Σ_v f(u,v) = Σ_v f(v,u))
- **Flow value |f|**: Σ_v f(s,v) − Σ_v f(v,s) (net flow out of source)
- **Residual network G_f = (V, E_f)**: edges with residual capacity c_f(u,v) = c(u,v) − f(u,v) if (u,v)∈E, or f(v,u) if (v,u)∈E; |E_f| ≤ 2|E|
- **Augmenting path**: simple path from s to t in G_f
- **Residual capacity of path p**: c_f(p) = min{c_f(u,v) : (u,v) in p}
- **Cut (S,T)**: partition V = S∪T with s∈S, t∈T
- **Net flow across cut**: f(S,T) = Σ_{u∈S} Σ_{v∈T} f(u,v) − Σ_{u∈S} Σ_{v∈T} f(v,u)
- **Capacity of cut**: c(S,T) = Σ_{u∈S} Σ_{v∈T} c(u,v)
- **Minimum cut**: cut with minimum capacity
- **Maximum flow**: flow with maximum |f|
- **Edmonds-Karp algorithm**: Ford-Fulkerson using BFS for augmenting paths; O(VE²)
- **Push-relabel algorithms**: alternative approach using preflows and heights
- **Antiparallel edges**: pair of edges (u,v) and (v,u); eliminated by vertex splitting
- **Supersource/supersink**: transform multiple sources/sinks to single source/sink
- **Integrality theorem**: integer capacities → integer maximum flow
- **Maximum bipartite matching**: via flow network with unit capacities
- **Corresponding flow network для matching**: V' = V∪{s,t}, E' from L to R + edges from s to L + edges from R to t, unit capacities

#### Processes/Algorithms

```
```

```
```
- **Input**: flow network G with source s, sink t
- **Output**: maximum flow f
- **Complexity**: O(E |f*|) with arbitrary path finding; O(VE²) with BFS (Edmonds-Karp)
- **Example** (Figure 24.6): 6 iterations on a network; each shows residual network G_f with augmenting path, then new flow
- **Bad example** (Figure 24.7): network where alternating bad choices require 2,000,000 augmentations

- Ford-Fulkerson with BFS (shortest path in residual network)
- **Lemma 24.7**: δ_f(s,v) increases monotonically with each flow augmentation
- **Theorem 24.8**: O(VE) augmentations
- **Complexity**: O(VE²)

#### Classifications
- **Flow types**: integer flow, feasible flow, maximum flow, preflow (push-relabel)
- **Network types**: single source/sink, multiple sources/sinks (reducible), vertex capacities (reducible), with antiparallel edges (reducible)
- **Algorithm types**: augmenting path (Ford-Fulkerson, Edmonds-Karp), push-relabel, scaling, continuous optimization
- **Application types**: bipartite matching, edge connectivity, escape problem, path cover, project selection

#### Comparisons
| Dimension | Ford-Fulkerson (arbitrary) | Edmonds-Karp (BFS) |
|---|---|---|
| Augmenting path selection | Any | Shortest (in edges) |
| Iterations | ≤ |f*| (integer capacities) | O(VE) |
| Per iteration | O(E) | O(E) |
| Total complexity | O(E |f*|) | O(VE²) |
| Edge capacity type | Integer (rational w/ scaling) | Any real |
| Termination | Always (integer); may not (irrational) | Always |

| Dimension | BFS (unweighted shortest path) | Dijkstra (weighted) |
|---|---|---|
| Edge weights | Unit | Nonnegative reals |
| Data structure | FIFO queue | Min-priority queue |
| Similarity to | Edmonds-Karp path finding | Used in Johnson reweighting |

#### Formulas
- Flow conservation: Σ_v f(u,v) = Σ_v f(v,u) for u∈V−{s,t}
- Flow value: |f| = Σ_v f(s,v) − Σ_v f(v,s)
- Residual capacity: c_f(u,v) = c(u,v) − f(u,v) if (u,v)∈E; = f(v,u) if (v,u)∈E; = 0 otherwise
- Augmented flow: (f↑f')(u,v) = f(u,v) + f'(u,v) − f'(v,u)
- Net flow across cut: f(S,T) = Σ_{u∈S} Σ_{v∈T} f(u,v) − Σ_{u∈S} Σ_{v∈T} f(v,u)
- Cut capacity: c(S,T) = Σ_{u∈S} Σ_{v∈T} c(u,v)
- |E_f| ≤ 2|E|
- Edmonds-Karp iterations: O(VE)

#### Rules/Laws/Theorems
- **Capacity constraint**: 0 ≤ f(u,v) ≤ c(u,v) for all u,v
- **Flow conservation**: ∀u∈V−{s,t}: Σ_v f(u,v) = Σ_v f(v,u)
- **Lemma 24.1**: If f is a flow in G and f' is a flow in G_f, then f↑f' is a flow in G with |f↑f'| = |f| + |f'|
- **Lemma 24.2**: f_p (augmenting path flow) is a flow in G_f with |f_p| = c_f(p) > 0
- **Corollary 24.3**: f↑f_p is a flow in G with |f↑f_p| = |f| + c_f(p) > |f|
- **Lemma 24.4**: For any cut (S,T), f(S,T) = |f|
- **Corollary 24.5**: |f| ≤ c(S,T) for any cut (S,T)
- **Theorem 24.6 (Max-flow min-cut theorem)**: For a flow f, TFAE:
  - **Proof sketch**: (1)⇒(2) via contradiction using augmenting path to increase flow. (2)⇒(3) define S = {v∈V : path s⇝v in G_f}, T = V−S. Show |f| = c(S,T). (3)⇒(1) by Corollary 24.5.
- **Lemma 24.7 (Monotonicity)**: δ_f(s,v) increases monotonically in Edmonds-Karp
- **Theorem 24.8**: Edmonds-Karp performs O(VE) augmentations
  - **Proof**: Each edge (u,v) can be critical at most |V|/2 times; each time distance to u increases by ≥2; ≤ |V|−2 edges max from s to u
- **Theorem 24.10 (Integrality theorem)**: If capacities are integer, Ford-Fulkerson produces integer-valued maximum flow
- **Lemma 24.9**: Matching M in bipartite G corresponds to integer-valued flow f in G' with |f| = |M|; conversely, integer-valued flow gives matching
- **Corollary 24.11**: Maximum matching cardinality = maximum flow value in corresponding network

#### Data Structures
- **Edge flow attribute**: (u,v).f
- **Residual network**: constructed implicitly by checking c_f(u,v) > 0
- **Adjacency lists**: edges with capacity and flow attributes
- **Modified graph G'**: includes both (u,v) and (v,u) for residual computation
- **BFS queue** (Edmonds-Karp): for finding shortest augmenting path

#### Edge Cases
- **Antiparallel edges**: eliminate by vertex splitting (Figure 24.2)
- **Multiple sources/sinks**: add supersource/supersink with infinite capacity (Figure 24.3)
- **Irrational capacities**: Ford-Fulkerson may not terminate
- **Zero-capacity edges**: not in residual network (c_f = 0)
- **Vertex capacities**: reduce to edge capacities by vertex splitting (Exercise 24.1-7)
- **Flow into source**: included in flow value definition; needed for residual networks
- **Edges entering source**: handled in residual computation

#### Proof Patterns
- **Max-flow min-cut**: (1)⇒(2): augmenting path increases flow; (2)⇒(3): define S as vertices reachable from s in G_f, show |f| = c(S,T); (3)⇒(1): flow ≤ cut capacity always
- **Monotonicity of distances (Lemma 24.7)**: assume a decrease, derive contradiction via edge (u,v) that was not in G_f before augmentation but is after; show δ_f'(s,v) ≥ δ_f(s,v)
- **Critical edge counting (Theorem 24.8)**: edge (u,v) critical when c_f(u,v) = c_f(p); disappears after augmentation; reappears only when (v,u) on augmenting path; distance to u increases by ≥2 each time; ≤|V|/2 times per edge
- **Integrality theorem**: induction on number of augmentations; each augmentation preserves integrality

#### End-of-Chapter Material




- 24-1: Escape problem (vertex capacities, grid)
- 24-2: Minimum path cover in dag
- 24-3: Hiring consulting experts (project selection via minimum cut)
- 24-4: Updating maximum flow (capacity increase/decrease by 1)
- 24-5: Maximum flow by scaling (O(E² lg C))
- 24-6: Widest augmenting path (≤|E| ln |f*| augmentations)
- 24-7: Global minimum cut (contraction algorithm, randomized)

---

### Ch. 25 — Matchings in Bipartite Graphs

#### Named Entities
- **Matching M**: subset of edges with at most one incident edge per vertex
- **Maximal matching**: cannot add another edge
- **Maximum matching**: matching of maximum cardinality
- **Perfect matching**: every vertex matched
- **M-alternating path**: path whose edges alternate ∈M, ∉M
- **M-augmenting path**: M-alternating path starting and ending with edges ∉M (odd length)
- **Symmetric difference**: X ⊕ Y = (X−Y) ∪ (Y−X)
- **d-regular graph**: every vertex has degree d
- **Hall's theorem**: perfect matching exists iff |A| ≤ |N(A)| for all A⊆L
- **Stable matching**: matching with no blocking pair
- **Blocking pair**: (w,m) both prefer each other to their current partners
- **Stable-marriage problem**: each vertex ranks all vertices of opposite side
- **Gale-Shapley algorithm**: finds stable matching (woman-oriented / man-oriented)
- **Assignment problem**: find perfect matching of maximum total weight in complete bipartite graph
- **Hungarian algorithm**: finds maximum-weight perfect matching via feasible vertex labeling and equality subgraph
- **Feasible vertex labeling h**: ℓ.h + r.h ≥ w(ℓ,r) for all ℓ∈L, r∈R
- **Equality subgraph G_h**: edges where ℓ.h + r.h = w(ℓ,r)
- **Directed equality subgraph G_{M,h}**: edges in E_h−M directed L→R, edges in M directed R→L

#### Processes/Algorithms

```
```
- **Complexity**: O(√V · E)
- **Phases for line 3**:
- **Lemma 25.5**: After updating M with maximal set of shortest M-augmenting paths, shortest M'-augmenting path is longer
- **Lemma 25.6**: If shortest M-augmenting path has q edges, |M*| ≤ |M| + |V|/(q+1)
- **Lemma 25.7**: repeat loop iterates O(√V) times

```
```
- **Complexity**: O(n²)
- **Properties**: always returns same stable matching; women get best possible partner; men get worst possible partner

```

```
- **Complexity**: O(n⁴) naive; O(n³) optimized
- **Theorem 25.14**: Perfect matching in equality subgraph = optimal solution to assignment problem
- **Example** (Figures 25.4–25.11): 7×7 weight matrix; starts with greedy matching; iteratively finds augmenting paths and updates labels until perfect matching found

```
```
- Returns matching at least half the size of maximum matching
- **Complexity**: O(E)

#### Classifications
- **Matching types**: maximal, maximum, perfect, maximum-weight, stable
- **Algorithm types**: augmenting path (Hopcroft-Karp), proposal/acceptance (Gale-Shapley), primal-dual (Hungarian), reduction to flow (Ch 24)
- **Graph types**: bipartite, complete bipartite, regular bipartite, general undirected

#### Comparisons
| Dimension | Hopcroft-Karp | Gale-Shapley | Hungarian | Flow-based (Ch 24) |
|---|---|---|---|---|
| Problem | Maximum cardinality | Stable matching | Maximum weight | Maximum cardinality |
| Complexity | O(√V · E) | O(n²) | O(n⁴) [O(n³) opt] | O(VE) |
| Technique | Augmenting paths (BFS+DFS) | Proposals/rejections | Vertex labeling + augment | Max flow on unit-capacity network |
| Graph needed | Bipartite | Complete bipartite | Complete bipartite | Bipartite |
| Edge weights | Unweighted | Rankings only | Weighted | Unweighted (unit capacities) |

| Dimension | Stable matching (woman-oriented) | Maximum matching |
|---|---|---|
| Optimal for women | Best possible partner in any stable matching | N/A |
| Optimal for men | Worst possible partner in any stable matching | N/A |
| Uniqueness | Produces same matching regardless of execution | Not unique |

#### Formulas
- |M'| = |M| + 1 (by augmenting path, Lemma 25.1)
- |M'| = |M| + k (by k vertex-disjoint augmenting paths, Corollary 25.2)
- |M*| ≤ |M| + |V|/(q+1) where q = shortest M-augmenting path length (Lemma 25.6)
- Hopcroft-Karp iterations: O(√V)
- Hopcroft-Karp complexity: O(√V · E)
- Gale-Shapley proposals: ≤ n²
- Feasible labeling: ℓ.h + r.h ≥ w(ℓ,r)
- Equality subgraph edges: ℓ.h + r.h = w(ℓ,r)
- Label update: ℓ.h' = ℓ.h − δ (for ℓ∈FL); r.h' = r.h + δ (for r∈FR)
- δ = min{ℓ.h + r.h − w(ℓ,r) : ℓ∈FL, r∈R−FR}
- Hungarian algorithm: O(n⁴) naive, O(n³) with σ-attribute optimization

#### Rules/Laws/Theorems
- **Lemma 25.1**: M-augmenting path P → M⊕P is a matching with |M|+1 edges
- **Corollary 25.2**: k vertex-disjoint M-augmenting paths → matching with |M|+k edges
- **Lemma 25.3**: M⊕M* is union of vertex-disjoint alternating paths and cycles; if |M*| > |M|, contains at least |M*|−|M| vertex-disjoint M-augmenting paths
- **Corollary 25.4 (Berge's theorem)**: M is maximum matching iff G contains no M-augmenting path
- **Lemma 25.5**: After adding maximal set of shortest augmenting paths, shortest augmenting path becomes longer
- **Lemma 25.6**: |M*| ≤ |M| + |V|/(q+1)
- **Lemma 25.7**: Hopcroft-Karp repeat loop iterates O(√V) times
- **Theorem 25.8**: Hopcroft-Karp runs in O(√V · E) time
- **Hall's theorem (Exercise 25.1-5)**: Perfect matching exists in bipartite G iff |A| ≤ |N(A)| for all A⊆L
- **Regular bipartite graphs**: d-regular bipartite graph has perfect matching (Exercise 25.1-6); has d disjoint perfect matchings
- **Theorem 25.9**: Gale-Shapley always terminates and returns a stable matching
- **Corollary 25.10**: Gale-Shapley O(n²) implementation
- **Theorem 25.11**: Gale-Shapley returns same stable matching regardless of woman choice; each woman gets best possible partner in any stable matching (woman-optimal)
- **Corollary 25.12**: Some stable matchings are not returned by Gale-Shapley
- **Corollary 25.13**: In Gale-Shapley output, each man has worst possible partner in any stable matching (man-pessimal)
- **Theorem 25.14**: Perfect matching in equality subgraph G_h is a maximum-weight perfect matching (optimal for assignment problem)
- **Lemma 25.15**: Updated labeling h' is feasible and ensures at least one new edge enters G_{M,h}; no edges from F or M leave

#### Data Structures
- **Predecessor π (breadth-first forest)**: in Hungarian algorithm, tracks augmenting path
- **Sets FL, FR**: vertices in breadth-first forest (L side and R side)
- **Queue Q**: BFS queue for augmenting path search
- **σ-attribute (Problem 25-2)**: r.σ = min{ℓ.h + r.h − w(ℓ,r) : ℓ∈FL}; speeds up δ computation to O(n)
- **Preference lists/rankings**: for Gale-Shapley
- **Engagement state**: free/engaged

#### Edge Cases
- **Empty matching**: valid starting point
- **Perfect matching not possible**: Hall's theorem characterizes when
- **|L| ≠ |R|**: Hungarian algorithm can be modified (Exercise 25.3-7)
- **Stable-roommates problem**: not always solvable (Exercise 25.2-5)
- **Incomplete bipartite graph**: maximum-weight matching via Hungarian with zero-weight edges for missing edges
- **General (non-bipartite) graphs**: matching harder; Edmonds' algorithm O(V⁴)
- **Non-complete preference lists**: National Resident Matching Program variant (Exercise 25.2-3)

#### Proof Patterns
- **Symmetric difference**: Lemma 25.3 shows M⊕M* contains vertex-disjoint alternating paths/cycles; if |M*| > |M|, at least |M*|−|M| are augmenting paths
- **Berge's theorem**: Corollary 25.4 — contrapositive both directions
- **Length increase (Lemma 25.5)**: two cases: path disjoint from augmenting paths set (must be longer b/c set is maximal), or intersecting (shares at least one edge → bound on |A| gives q < |P|)
- **Hall's theorem**: standard combinatorial proof (marriage theorem)
- **Gale-Shapley termination**: if some woman free, she proposes to all men; all men engaged → n men engaged → n women engaged → contradiction
- **Gale-Shapley stability**: woman w matched to m but prefers m' → she proposed to m' before; m' rejected her for someone he prefers; thus m' prefers current partner to w
- **Woman-optimality (Theorem 25.11)**: suppose woman w has better partner m' in another stable matching; trace first rejection in stable matching → contradiction
- **Hungarian correctness (Theorem 25.14)**: any perfect matching M in G: Σw(M) ≤ Σℓ.h + Σr.h = Σw(M*) for perfect M* in G_h

#### End-of-Chapter Material




- 25-1: Perfect matchings in regular bipartite graph via Euler tours; Θ(E lg d)
- 25-2: Reduce Hungarian to O(n³) via σ-attribute
- 25-3: Other matching problems (incomplete graph, zero/negative weights, cycle cover)
- 25-4: Fractional matchings (bipartite: max fractional matching = max matching; general: counterexample)
- 25-5: Computing vertex labels from maximum-weight perfect matching

### Chapter 26: Parallel Algorithms

#### 26.1 The Basics of Fork-Join Parallelism

**Fork-Join Model:** Task-parallel algorithms extend serial algorithms with three keywords: `spawn`, `sync`, `parallel`. Deleting these keywords yields the **serial projection** — ordinary serial pseudocode for the same problem.

**P-FIB (Parallel Fibonacci):**
```
P-FIB(n)
1 if n ≤ 1
2     return n
3 else x = spawn P-FIB(n-1)   // may run in parallel with parent
4     y = P-FIB(n-2)           // runs in parallel with spawned child
5     sync                      // wait for spawned children
6     return x + y
```
- Serial FIB runs in Θ(φⁿ) due to redundant recomputation.
- **Span analysis:** T∞(n) = max{T∞(n-1), T∞(n-2)} + Θ(1) = T∞(n-1) + Θ(1) = Θ(n).
- **Work:** T₁(n) = Θ(φⁿ). **Parallelism:** Θ(φⁿ/n) — grows dramatically.

**Trace Model:** Execution = DAG G = (V, E). Vertices = **strands** (maximal chains of instructions without parallel/procedural control). Edges = dependencies. Two strands are **in series** if a directed path connects them; **in parallel** if no path exists either way.

**Ideal Parallel Computer:** Set of processors with **sequentially consistent shared memory** — behaves as if instructions interleave in some global linear order respecting trace dependencies. Each processor has equal power; scheduling overhead ignored.

**Performance Metrics:**
| Term | Definition |
|------|-----------|
| **Work T₁** | Total time on 1 processor = sum of strand times |
| **Span T∞** | Time on unlimited processors = weight of critical path |
| **Speedup** | T₁/Tₚ (at most p by work law) |
| **Linear speedup** | T₁/Tₚ = Θ(p) |
| **Perfect linear speedup** | T₁/Tₚ = p |
| **Parallelism** | T₁/T∞ = average work per span step |
| **Parallel slackness** | (T₁/T∞)/p = T₁/(p·T∞) |

**Work Law:** Tₚ ≥ T₁/p (P processors do at most P work per step).
**Span Law:** Tₚ ≥ T∞ (cannot beat unlimited processors).

**Greedy Scheduler:**
- **Complete step:** ≥ p strands ready → assign any p.
- **Incomplete step:** < p strands ready → assign all ready strands.
- **Theorem 26.1:** Tₚ ≤ T₁/p + T∞.
- **Corollary 26.2:** Greedy is within factor 2 of optimal: Tₚ < 2T*ₚ.
- **Corollary 26.3:** If p ≪ T₁/T∞ (slackness ≫ 1), then Tₚ ≈ T₁/p (near-perfect linear speedup).
- Rule of thumb: slackness ≥ 10 suffices for good speedup.
- **Proof sketch:** Complete steps ≤ T₁/p (each does P work). Each incomplete step reduces remaining span by 1, so ≤ T∞ steps.

**Series-Parallel Composition:**
- Series: work adds, span adds.
- Parallel: work adds, span = max.

**Parallel Loops — P-MAT-VEC:**
```
P-MAT-VEC(A, x, y, n)
1 parallel for i = 1 to n
2     for j = 1 to n
3         yᵢ = yᵢ + aᵢⱼ·xⱼ
```
- Work T₁ = Θ(n²), Span T∞ = Θ(n) (inner serial loop) + Θ(lg n) (loop control) = Θ(n).
- Parallelism = Θ(n).

**Recursive Implementation (Compiled form):**
```
P-MAT-VEC-RECURSIVE(A, x, y, n, i, i′)
1 if i == i′
2     for j = 1 to n
3         yᵢ = yᵢ + aᵢⱼ·xⱼ
4 else mid = ⌊(i + i′)/2⌋
5     spawn P-MAT-VEC-RECURSIVE(A, x, y, n, i, mid)
6     P-MAT-VEC-RECURSIVE(A, x, y, n, mid+1, i′)
7     sync
```
Span formula: T∞(n) = Θ(lg n) + max{iter∞(i)}. Recursive spawning adds at most constant factor to work.

**Determinacy Races:**
- **Definition:** Two logically parallel instructions access same memory location, at least one modifies it.
- **RACE-EXAMPLE:** `x = 0; parallel for i=1 to 2: x = x+1; print x` — may print 1 instead of 2.
- Load-increment-store is not atomic: one update can be lost.
- **Mutually noninterfering strands:** Only read shared data, never modify.
- **P-MAT-VEC-WRONG:** Parallelizing inner loop creates races on yᵢ updates.
- **Benign races:** Possible (e.g., parallel hash tables) but avoided in this chapter.

**Chess Program Lesson (True Story):**
- Original: T₁=2048s, T∞=1s → T₃₂=65s, T₅₁₂=5s.
- "Optimized": T₁′=1024s, T∞′=8s → T₃₂′=40s, T₅₁₂′=10s.
- The "optimization" was slower on 512 processors because span became dominant. Work/span analysis predicted scaling failure where benchmarking on 32 processors did not.

#### 26.2 Parallel Matrix Multiplication

**P-MATRIX-MULTIPLY (Parallel Loops):**
```
P-MATRIX-MULTIPLY(A, B, C, n)
1 parallel for i = 1 to n
2     parallel for j = 1 to n
3         for k = 1 to n
4             cᵢⱼ = cᵢⱼ + aᵢₖ·bₖⱼ
```
- Work T₁ = Θ(n³), Span T∞ = Θ(lg n) + Θ(lg n) + Θ(n) = Θ(n).
- Parallelism = Θ(n²).

```
```
- **Work recurrence:** M₁(n) = 8M₁(n/2) + Θ(n²) = Θ(n³).
- **Span recurrence:** M∞(n) = M∞(n/2) + Θ(lg n) = Θ(lg² n).
- **Parallelism:** Θ(n³/lg² n) — huge.

- 7 parallel recursive multiplications of n/2 × n/2 matrices.
- **Work:** Θ(n^{lg 7}) ≈ Θ(n^{2.81}). **Span:** Θ(lg² n). **Parallelism:** Θ(n^{lg 7}/lg² n).

| Algorithm | Work T₁ | Span T∞ | Parallelism |
|-----------|---------|---------|-------------|
| P-MATRIX-MULTIPLY (loops) | Θ(n³) | Θ(n) | Θ(n²) |
| P-MATRIX-MULTIPLY-RECURSIVE | Θ(n³) | Θ(lg² n) | Θ(n³/lg² n) |
| Parallel Strassen | Θ(n^{lg 7}) | Θ(lg² n) | Θ(n^{lg 7}/lg² n) |

#### 26.3 Parallel Merge Sort

```
```



```
```
- **Work & Span:** Θ(lg n). Finds q such that A[p..q-1] ≤ x ≤ A[q..r].

```
```
- **Span:** T∞(n) = T∞(3n/4) + Θ(lg n) = Θ(lg² n) (master theorem, case 2, k=1).
- **Work:** T₁(n) = T₁(αn) + T₁((1-α)n) + Θ(lg n) with 1/4 ≤ α ≤ 3/4, solution T₁(n) = Θ(n).
- **Key property:** At most 3n/4 elements in any recursive call (since n₂ ≤ n₁ and median splits n₁ in half).

```
```

- Work: T₁(n) = 2T₁(n/2) + Θ(n) = Θ(n lg n).
- Span: T∞(n) = T∞(n/2) + Θ(lg² n) = Θ(lg³ n).
- Parallelism: Θ(n lg n / lg³ n) = Θ(n / lg² n) — much better than Θ(lg n) of naive version.

| Version | Work | Span | Parallelism |
|---------|------|------|-------------|
| Serial merge sort | Θ(n lg n) | Θ(n lg n) | 1 |
| P-NAIVE-MERGE-SORT | Θ(n lg n) | Θ(n) | Θ(lg n) |
| P-MERGE-SORT | Θ(n lg n) | Θ(lg³ n) | Θ(n/lg² n) |



---

### Chapter 27: Online Algorithms

#### 27.1 Waiting for an Elevator

**Problem Setup:** You want to go k floors up. Stairs: 1 min/floor = k min total. Elevator: ascends k floors in 1 min, but arrival time m is unknown (0 ≤ m ≤ B-1 minutes). You know k and B but not m.

**Offline Optimal (Seer):** If m ≤ k-1: wait for elevator (cost m+1). Else: take stairs (cost k). So OPT(m) = min{m+1, k}.

**Competitive Analysis Framework:**
- **Competitive ratio** = max_{I ∈ U} ALG(I)/OPT(I) for minimization problems.
- Algorithm is **c-competitive** if ratio ≤ c for all inputs.

**Three Strategies:**
| Strategy | Cost | Competitive Ratio | Worst-case scenario |
|----------|------|-------------------|-------------------|
| Always stairs | k | k | m=0 (elevator immediate) |
| Always elevator | m+1 | B/k | m=B-1 (elevator very late) |
| Hedge (wait k min, then stairs) | m+1 if m≤k, else 2k | **2** (independent of k,B) | any — balanced |

**Hedge Analysis:** h(m) = m+1 if m ≤ k, else 2k. Ratio = max{ (k+1)/1, 2k/k, 2k/(k+1), ..., (B)/(k) } = 2.
- **Key insight:** Wait k minutes guards against immediate arrival; taking stairs after k guards against long delay. Competitive ratio 2 is optimal.

**Exercises:** 27.1-1 (general wait time p), 27.1-2 (ski rental problem — rent/buy 2-competitive), 27.1-3 (concentration solitaire 2-competitive).

#### 27.2 Maintaining a Search List (Move-to-Front)

**Problem:** n-element doubly linked list. Search cost = position rL(x). After search, may swap adjacent elements (cost 1 per swap). Total cost = search cost + swap cost.

**Move-to-Front (MTF):** After searching x at position r, swap it forward r-1 times to front. Cost = r (search) + (r-1) (swaps) = 2r - 1.

**Optimal offline algorithm FORESEE:** Knows future requests, optimally rearranges list after each search.

**Inversion Count I(L, L′):** Number of element pairs (a,b) with a before b in L but b before a in L′.

**Notation for i-th search of element x:**
- **BB:** elements before x in both LMᵢ and LFᵢ
- **BA:** elements before x in LMᵢ, after x in LFᵢ
- **AB:** elements after x in LMᵢ, before x in LFᵢ

**Positions:** rLM(x) = |BB| + |BA| + 1; rLF(x) = |BB| + |AB| + 1.

**Costs:**
- MTF cost: cMᵢ = 2(|BB| + |BA| + 1) - 1 = 2|BB| + 2|BA| + 1.
- FORESEE cost: cFᵢ = rLF(x) + tᵢ = |BB| + |AB| + 1 + tᵢ (tᵢ = FORESEE's swaps).

**Inversion Count Change During MTF Swap:**
- Swapping with y ∈ BB: inversion count +1 (y was before x in both, now x before y in LM).
- Swapping with z ∈ BA: inversion count -1 (z before x in LM, x before z in LF; swap fixes it).
- Net change: Δ = |BB| - |BA|.

**Theorem 27.1:** MTF is **4-competitive**.
- **Proof:** Potential function Φᵢ = 2·I(LMᵢ, LFᵢ).
  - After MTF's i-th search: ΔΦ = 2(|BB| - |BA|).
  - After FORESEE's i-th search (tᵢ swaps): ΔΦ ≤ 2tᵢ (each swap changes by ±1).
  - Amortized cost: ĉMᵢ = cMᵢ + Φᵢ - Φᵢ₋₁
    = (2|BB|+2|BA|+1) + 2(|BB|-|BA|) + 2tᵢ
    = 4|BB| + 1 + 2tᵢ ≤ 4(|BB|+|AB|+1) + 2tᵢ = 4cFᵢ.
  - Summing: Σ cMᵢ ≤ 4Σ cFᵢ (since Φ₀=0, Φᵢ≥0).
- **Exercise 27.2-4:** With free moves (no swap cost), MTF is 2-competitive using Φᵢ = I(LM, LF).

| Algorithm | Competitive Ratio | Notes |
|-----------|-------------------|-------|
| MTF | 4 (or 2 with free moves) | Best known |
| Frequency count | Not O(1)-competitive | Can be fooled |
| Static (sorted by probability) | Optimal offline, not online | Needs distribution |

**Exercises:** 27.2-1 (static optimal ordering by probability), 27.2-2 (counterexample: FORESEE may cost more), 27.2-3 (frequency count not O(1)-competitive), 27.2-4 (free moves → 2-competitive).

#### 27.3 Online Caching

**Problem:** Cache holds k blocks. Sequence of n requests b₁,...,bₙ. On miss with full cache, evict one block. Goal: minimize misses. Cache starts empty (first k requests all misses).

**Deterministic Policies:**
| Policy | Eviction Rule | Competitive Ratio |
|--------|---------------|-------------------|
| FIFO | Longest-resident block | O(k) |
| LIFO | Most-recently-loaded block | Θ(n/k) — **unbounded** |
| LRU | Least-recently-used block | O(k) |
| LFU | Least-frequently-used block | Θ(n/k) — unbounded |

- **Lower bound:** k+1 blocks, request sequence: 1,2,...,k,k+1,k,k+1,k,... Alternating k and k+1. LIFO evicts on every request (n misses). OPT evicts once after first k+1 (k+1 misses). Ratio = n/(k+1) = Ω(n/k).
- **Upper bound:** Any algorithm has at most n misses, OPT at least k. Ratio = O(n/k).

- **Epoch analysis:** Epoch i begins upon (k+1)-st distinct request since start of epoch i-1.
- LRU: ≤ k misses per epoch (only first request of each distinct block causes miss; blocks stay in cache for rest of epoch).
- OPT: ≥ 1 miss per epoch (first request of each epoch is for a block not among k most recently used; OPT must have evicted it).
- Ratio ≤ k/1 = O(k). **Theorem 27.4:** Ω(k) lower bound for all deterministic algorithms.

- k+1 distinct blocks. Request 1,...,k (fill cache). Then repeatedly: request k+1 (online evicts some b₁), then request b₁ (online evicts b₂), then b₂, etc. Online: n misses.
- OPT (furthest-in-future): evicts block with next request furthest away. After k misses, incurs at most 1 miss per k requests. Total: ≤ k + n/k misses.
- Ratio ≥ n / (k + n/k) ≥ k/2 for n ≥ k². Thus Ω(k).

```
```
- **Deterministic MARKING:** Still Θ(k)-competitive.
- **Analysis by epochs:** New epoch starts after "unmark all." Each epoch has ≤ k distinct requests (usually exactly k).
  - **Old requests:** blocks requested in previous epoch.
  - **New requests:** blocks not in previous epoch (rᵢ ≥ 1 per epoch).
- **Expected misses in epoch i:** E[Xᵢ] = rᵢ + Σⱼ₌₁^{k-rᵢ} rᵢ/(k-j+1) = rᵢ H_k, where H_k = k-th harmonic number ≈ ln k + γ.


- **Proof:** Sum over epochs: E[X] ≤ Σ rᵢ H_k. For two consecutive epochs i-1 and i, there are k + rᵢ distinct requests. OPT incurs ≥ rᵢ misses across these two epochs (no cache can avoid miss on each new block). Summing: OPT ≥ (1/2) Σ rᵢ. So E[ALG]/OPT ≤ 2H_k = O(lg k).

- **Oblivious:** Knows algorithm but not random choices. Used for randomized analysis.
- **Nonoblivious:** Knows all random choices; randomness provides no benefit.

| Algorithm | Type | Competitive Ratio |
|-----------|------|-------------------|
| LIFO, LFU | Deterministic | Θ(n/k) unbounded |
| FIFO, LRU | Deterministic | Θ(k) |
| Deterministic lower bound | Any deterministic | Ω(k) |
| RANDOMIZED-MARKING | Randomized | O(lg k) |
| Lower bound (randomized) | Any randomized | Ω(lg k) |


- **MTF:** After search 5 (cost=9, move 5 to front): ⟨5,1,2,3,4⟩. Search 3 (cost=9): ⟨3,5,1,2,4⟩. Search 4 (cost=9): ⟨4,3,5,1,2⟩. Search 4 (cost=1, hit): total=28.
- **FORESEE:** After search 5 (cost=5, no swap): same list. After search 3, moves 4 to front (cost=5+3=8): ⟨4,1,2,3,5⟩. Search 4 (cost=1): hit. Search 4: cost=1. Total=15.
- MTF cost (28) is < 4× FORESEE (15×4=60), consistent with 4-competitive bound.

- **Static optimal ordering (Ex 27.2-1):** If probabilities p(xᵢ) known, sort descending by p. Expected cost = Σᵢ p(xᵢ)·r(xᵢ) minimized.
- **Frequency count heuristic:** Maintain count per element; re-sort by count after each access. Can be forced to have unbounded competitive ratio (Ex 27.2-3).
- **Free swaps (Ex 27.2-4):** If moving x to any earlier position costs 0 (only search costs matter), MTF is 2-competitive with Φ = I(LM, LF). Reason: each inversion costs 1 in future searches (element must pass over inverted elements), capped by actual future cost.


---

### Chapter 28: Matrix Operations

#### 28.1 Solving Systems of Linear Equations

**Problem:** Solve Ax = b for n equations in n unknowns, where A is nonsingular (invertible, full rank n).

**LUP Decomposition:** PA = LU where:
- **L:** unit lower-triangular (1s on diagonal, zeros above)
- **U:** upper-triangular (zeros below diagonal)
- **P:** permutation matrix (represents row swaps)

**Forward Substitution (Ly = Pb):**
```
y₁ = b_{π[1]}
yᵢ = b_{π[i]} - Σⱼ₌₁^{i-1} lᵢⱼ·yⱼ   for i = 2,...,n
```
- Time: Θ(n²). Uses permutation array π (not full matrix P).

**Back Substitution (Ux = y):**
```
xₙ = yₙ/u_{nn}
xᵢ = (yᵢ - Σⱼ₌ᵢ₊₁ⁿ uᵢⱼ·xⱼ)/u_{ii}   for i = n-1,...,1
```
- Time: Θ(n²). Works from bottom row up.

**LUP-SOLVE (Combined):**
```
LUP-SOLVE(L, U, π, b, n)
1 let x, y be new vectors of length n
2 for i = 1 to n
3     yᵢ = b_{π[i]} - Σⱼ₌₁^{i-1} lᵢⱼ·yⱼ
4 for i = n downto 1
5     xᵢ = (yᵢ - Σⱼ₌ᵢ₊₁ⁿ uᵢⱼ·xⱼ)/u_{ii}
6 return x
```
Total time: Θ(n²).

**Example (3×3 system):**
```
A = [[1, 2, 0], [3, 4, 4], [5, 6, 3]], b = [3, 7, 8]
LUP: P = [[0,1,0],[0,0,1],[1,0,0]] (π=[2,3,1])
     L = [[1,0,0],[0.2,1,0],[0.6,0.5,1]], U = [[5,6,3],[0,0.8,-0.6],[0,0,2.5]]
Forward: y = [7, 1.6, 5] → Backward: x = [1, 2, 2]
```

**LU Decomposition (Gaussian elimination, no pivoting):**
- Partition A = [[a₁₁, w^T], [v, A′]].
- Factor: A = [[1, 0], [v/a₁₁, I]] · [[a₁₁, w^T], [0, A′ - vw^T/a₁₁]].
- **Schur complement:** S = A′ - vw^T/a₁₁.
- Recursively factor S = L′U′. Then L = [[1,0],[v/a₁₁, L′]], U = [[a₁₁, w^T],[0, U′]].
- **Pivot:** a₁₁ (and subsequent diagonal entries). Division by 0 ⇒ failure.
- **Numerical stability:** Small pivots cause large roundoff errors. Mitigated by pivoting.

**LU-DECOMPOSITION (Iterative, in-place):**
```
LU-DECOMPOSITION(A, n)
1 let L, U be new n×n matrices
2 initialize U with 0s below diagonal, L with 1s on diagonal and 0s above
3 for k = 1 to n
4     u_{kk} = a_{kk}
5     for i = k+1 to n
6         l_{ik} = a_{ik}/a_{kk}
7         u_{ki} = a_{ki}
8     for i = k+1 to n           // compute Schur complement
9         for j = k+1 to n
10            a_{ij} = a_{ij} - l_{ik}·u_{kj}
11 return L, U
```
Time: Θ(n³). Can be done in-place (store L in lower triangle, U in upper triangle).

**LUP-DECOMPOSITION (with row pivoting):**
```
LUP-DECOMPOSITION(A, n)
1 let π[1:n] be new array; for i=1 to n: π[i] = i
2 for k = 1 to n
3     find k′ ≥ k with max |a_{ik}|                        // find pivot row
4     if |a_{k′k}| == 0: error "singular matrix"
5     exchange π[k] ↔ π[k′]
6     exchange rows k and k′ of A
7     for i = k+1 to n: a_{ik} = a_{ik}/a_{kk}             // form L column
8     for i = k+1 to n: for j = k+1 to n:
9         a_{ij} = a_{ij} - a_{ik}·a_{kj}                   // Schur complement
```
Time: Θ(n³). Stores L and U in-place in A (L below diagonal, U on and above diagonal).
- **Pivoting** ensures |l_{ik}| ≤ 1, improving numerical stability.

**Edge Cases:**
- **Underdetermined system** (rank < n): infinitely many or no solutions.
- **Overdetermined system** (more equations than unknowns): no exact solution generally.
- **Singular matrix:** determinant = 0, no unique solution.
- **Numerical instability:** Small pivots amplify roundoff errors; avoided by partial pivoting.

#### 28.2 Inverting Matrices

**Using LUP Decomposition:**
- Solve AX = I: for each column i, solve A·Xᵢ = eᵢ (eᵢ = i-th unit vector).
- Each solve: Θ(n²) using LUP-SOLVE. Total for n columns: Θ(n³).
- Combined with LUP decomposition (Θ(n³)): total Θ(n³).

- **Theorem 28.1 (Multiplication ≤ Inversion):** If I(n) = Ω(n²) and I(3n) = O(I(n)), then M(n) = O(I(n)).
  - Construct D = [[I, A, 0], [0, I, B], [0, 0, I]] (3n×3n). Then D⁻¹ = [[I, -A, AB], [0, I, -B], [0, 0, I]]. Extract AB from upper right.
  - D can be constructed in Θ(n²) time and inverted in O(I(3n)) = O(I(n)) time.

- **Theorem 28.2 (Inversion ≤ Multiplication):** If M(n) = Ω(n²) with M(n+k) = O(M(n)) and M(n/2) ≤ cM(n) for c<1/2, then I(n) = O(M(n)).
  - For symmetric positive-definite A: partition A = [[B, C^T], [C, D]].
  - Compute S = D - C·B⁻¹·C^T (Schur complement, via matrix multiplications).
  - Recurse: B⁻¹ and S⁻¹.
  - A⁻¹ = [[B⁻¹+B⁻¹C^T S⁻¹CB⁻¹, -B⁻¹C^T S⁻¹], [-S⁻¹CB⁻¹, S⁻¹]].
  - T(n) = 2T(n/2) + 4M(n/2) + O(n²) = O(M(n)) by master theorem.
  - For general nonsingular A: A⁻¹ = (A^T A)⁻¹ A^T, where A^T A is SPD.


#### 28.3 Symmetric Positive-Definite Matrices & Least Squares


| Lemma | Statement | Proof Sketch |
|-------|-----------|-------------|
| 28.3 | SPD ⇒ nonsingular | If singular, ∃ x≠0: Ax=0 ⇒ x^T A x = 0, contradiction |
| 28.4 | Leading submatrices of SPD are SPD | Let Aₖ be first k rows/cols. If xₖ≠0, extend with zeros to n-vector. x^T A x = xₖ^T Aₖ xₖ > 0 |
| 28.5 (Schur complement) | S = C - B^T Aₖ⁻¹ B is SPD | Complete the square: x^T A x = (y + Aₖ⁻¹ B^T z)^T Aₖ (y + Aₖ⁻¹ B^T z) + z^T S z. Choose y = -Aₖ⁻¹ B^T z ⇒ z^T S z > 0 |
| 28.6 | LU of SPD never divides by 0 | All pivots = det(Aₖ)/det(Aₖ₋₁) > 0 |

- All diagonal entries of SPD are positive.
- Maximum element lies on the diagonal.
- Determinants of all leading submatrices are positive.
- LU decomposition without pivoting is numerically safe for SPD matrices.

- **Given:** m data points (xᵢ, yᵢ) to fit with F(x) = Σⱼ₌₁ⁿ cⱼ fⱼ(x) (e.g., polynomial fⱼ(x) = x^{j-1}).
- **Matrix form:** Let A be m×n with a_{ij} = fⱼ(xᵢ). Want Ac ≈ y.
- **Error vector:** η = Ac - y. Minimize ||η||² = Σ ηᵢ².
- **Normal equation:** Differentiate ||η||²: (Ac - y)^T A = 0 ⇒ A^T A c = A^T y.
- **Solution:** c = (A^T A)⁻¹ A^T y = A⁺ y, where **A⁺** = (A^T A)⁻¹ A^T is the **pseudoinverse**.
- A^T A is SPD if A has full column rank (Theorem D.6).

```
```
- AA⁺A = A, A⁺AA⁺ = A⁺, (AA⁺)^T = AA⁺, (A⁺A)^T = A⁺A.

```
```
```
```
```
```
```
```

- **Singular matrix:** LUP-DECOMPOSITION reports "singular matrix" when all entries in a column are zero (line 10-11).
- **Numerical instability:** Even nonzero pivots can be very small, causing large roundoff errors. Partial pivoting (choosing max absolute value) mitigates this.
- **SPD guarantee:** For symmetric positive-definite matrices, all pivots > 0 (Corollary 28.6), so no pivoting needed.
- **Underdetermined/Overdetermined:** Underdetermined (rank < n) → infinitely many or no solutions. Overdetermined (more equations than unknowns) → least-squares approximation.
- **Non-power-of-2 sizes:** Matrix inversion algorithm (Thm 28.2) pads with identity to next power of 2.



---

### Chapter 29: Linear Programming

#### 29.1 Linear Programming Formulations and Algorithms

**Standard Form (maximization):**
```
maximize    c^T x
subject to  Ax ≤ b
            x ≥ 0
```
where A is m×n, c is n-vector, b is m-vector, x is n-vector of decision variables.

**Terminology:**
| Term | Definition |
|------|-----------|
| **Feasible solution** | x satisfying all constraints (Ax ≤ b, x ≥ 0) |
| **Feasible region** | Set of all feasible solutions (convex polyhedron) |
| **Optimal solution** | Feasible x with maximum c^T x |
| **Optimal objective value** | c^T x* for optimal x* |
| **Infeasible** | No feasible solution exists |
| **Unbounded** | Feasible region exists but objective can increase without bound |

**Converting to Standard Form:**
| Original | Conversion |
|----------|-----------|
| Minimize c^T x | Maximize -c^T x |
| a·x ≥ b | -a·x ≤ -b |
| a·x = b | a·x ≤ b and a·x ≥ b |
| Variable x unrestricted | Replace with x⁺ - x⁻, x⁺, x⁻ ≥ 0 |
| a·x ≤ b (want equality) | Add slack s ≥ 0: a·x + s = b |

**Example — Political Campaign LP:**
Variables: x₁ (zombie prep), x₂ (shark lasers), x₃ (flying car highways), x₄ (dolphin voting).
Minimize: x₁ + x₂ + x₃ + x₄
Subject to:
```
-2x₁ + 8x₂ + 0x₃ + 10x₄ ≥ 50    (urban votes)
 5x₁ + 2x₂ + 0x₃ +  0x₄ ≥ 100   (suburban votes)
 3x₁ - 5x₂ + 10x₃ - 2x₄ ≥ 25    (rural votes)
 x₁, x₂, x₃, x₄ ≥ 0
```
Solution: spend $33K (x₁=20, x₂=0, x₃=4, x₄=9) — not optimal; LP finds minimum.

**Algorithms Comparison:**
| Algorithm | Worst-case | Practice | Type |
|-----------|-----------|----------|------|
| **Simplex** (Dantzig 1947) | Exponential | Fast | Moves along exterior edges of feasible region |
| **Ellipsoid** (Khachian 1979) | Polynomial O(n⁶L²) | Slow | First polynomial-time LP algorithm |
| **Interior-point** (Karmarkar 1984) | Polynomial | Competitive with simplex | Moves through interior of feasible region |

**Integer Linear Programming:** Variables must be integers. **NP-hard** (feasibility alone is NP-complete, Exercise 34.5-3). No known polynomial algorithm.

**Two-Variable Geometric Solution:**
- Each constraint = half-plane. Feasible region = convex polygon (simplex).
- Objective function = line with slope -1 (for x₁ + x₂). Slide line outward until it exits feasible region.
- Optimal always at a **vertex** (corner point) or along an edge.
- For n variables: feasible region = intersection of half-spaces in ℝⁿ (a simplex).
- Simplex algorithm: walk from vertex to vertex along edges, increasing objective, until local=global optimum.

#### 29.2 Formulating Problems as Linear Programs

**Shortest Path (single-pair):**
```
maximize    d_t
subject to  d_v ≤ d_u + w(u,v)   ∀(u,v)∈E
            d_s = 0
```
- Variables: d_v for each vertex v (shortest-path weight from s).
- **Why maximize?** Minimizing would set all d_v = 0. Maximizing pushes each d_v to its largest value consistent with constraints, which is exactly min{d_u + w(u,v)}.
- Single-source version: maximize Σ d_v for all vertices reachable from s.

**Maximum Flow:**
```
maximize    Σ_v f_{sv} - Σ_v f_{vs}
subject to  0 ≤ f_{uv} ≤ c(u,v)           ∀u,v∈V
            Σ_u f_{uv} - Σ_u f_{vu} = 0   ∀v∈V\{s,t}  (flow conservation)
```
- Variables: f_{uv} for each ordered pair (u,v). Typically O(V²) variables.
- Can be reduced to O(V+E) constraints by omitting non-edges.

**Minimum-Cost Flow:**
```
minimize    Σ_{(u,v)∈E} a(u,v)·f_{uv}
subject to  0 ≤ f_{uv} ≤ c(u,v)
            flow conservation at all v∈V\{s,t}
            Σ_v f_{sv} - Σ_v f_{vs} = d   (demand = d units)
```
- **Cost a(u,v):** per-unit cost of flow on edge (u,v).
- Example (Fig 29.3): Send 4 units s→t. Edges with capacities & costs. Optimal: cost = 27.

**Multicommodity Flow:**
- k commodities Kᵢ = (sᵢ, tᵢ, dᵢ), each with own flow fᵢ_{uv}.
- **Aggregate flow:** f_{uv} = Σᵢ fᵢ_{uv} ≤ c(u,v).
- **No objective** — just feasibility (null objective). Only known polynomial algorithm is via LP.
- **Minimum-cost variant:** minimize Σ a(u,v)·f_{uv}.

#### 29.3 Duality

```
```
- Each primal constraint ↔ dual variable yᵢ.
- Each primal variable xⱼ ↔ dual constraint.
- Coefficients transpose: (c,b) ↔ (b,c), A ↔ A^T.

```
```


- Proof: c^T x ≤ (A^T y)^T x = y^T A x ≤ y^T b = b^T y.



- **Proof sketch:** Let μ = min b^T y (dual optimum). Augment primal with c^T x ≥ μ. Show augmented primal is feasible (using Farkas' lemma). Then Weak Duality gives c^T x ≤ μ = b^T y, and the augmented primal gives c^T x ≥ μ, so c^T x = μ.



- Max flow / min cut: Dual of max-flow LP is the min-cut problem (Theorem 24.6, Max-Flow Min-Cut Theorem).
- Shortest path: Dual of shortest-path LP gives a formulation related to potentials.


```
```

```
```

- **Infeasibility:** No solution exists (constraints contradict). Ex 29.1-3: max 3x₁-2x₂ s.t. x₁+x₂≤2, -2x₁-2x₂≤-10, x₁,x₂≥0 → infeasible (second constraint ⇒ x₁+x₂≥5, contradicts first).
- **Unboundedness:** Feasible region extends infinitely in direction of improving objective. Ex 29.1-4: max x₁-x₂ s.t. -2x₁+x₂≤-1, -x₁-2x₂≤-2, x₁,x₂≥0 → unbounded.
- **Finite optimum in unbounded region:** Ex 29.1-5: max -x₁ s.t. x₁≥0, x₂≥0, x₁+x₂≥0. Feasible region unbounded, but optimum = 0 at origin.
- **Integer LP (Problem 29-3):** Weak duality holds (IP ≤ ID), strong duality fails (IP < ID possible). Gap = P - IP = **integrality gap**.
- **Complementary Slackness (Problem 29-2):** At optimality, either a primal constraint is tight (equality) or the corresponding dual variable is zero. Similarly, either a dual constraint is tight or the corresponding primal variable is zero. Used to verify optimality and derive dual solutions.

- **29.1-1:** Minimize -2x₁+3x₂, x₁+x₂=7, x₁-2x₂≤4, x₁≥0. Feasible: (7,0)→-14, (4,3)→1, (0,7)→21.
- **29.1-2:** Nonpositivity constraint x₃≤0. Replace x₃ = -x₃′. Feasible: (7,24,-0)→182, (31,0,-24)→38, etc.
- **29.1-6:** Converting constraints between forms. (a) Equality a·x=b → a·x≤b and -a·x≤-b. (b) Inequality a·x≤b → a·x+s=b with slack s≥0.
- **29.1-8:** Political LP may predict winning more voters than exist. Adding constraints like "urban votes won ≤ 100,000" prevents this. But optimal solution won't exceed limits anyway (would waste money).



---

### Chapter 30: Polynomials and the FFT

#### 30.1 Representing Polynomials

**Polynomial:** A(x) = Σⱼ₌₀^{n-1} aⱼ xʲ over field F (typically ℂ). **Degree** = highest k with aₖ ≠ 0. **Degree-bound** n = any integer > degree.

**Two Representations:**
| Aspect | Coefficient | Point-Value |
|--------|-------------|-------------|
| Form | a = (a₀,...,a_{n-1}) | {(x₀,y₀),...,(x_{n-1},y_{n-1})}, yₖ=A(xₖ) |
| Evaluation | Θ(n) via Horner: A(x₀) = a₀ + x₀(a₁ + x₀(a₂ + ...)) | Already known at sample points |
| Addition | Θ(n): cⱼ = aⱼ + bⱼ | Θ(n): C(xₖ) = A(xₖ) + B(xₖ) |
| Multiplication | Θ(n²) naive: cⱼ = Σ aₖ·b_{j-k} | Θ(n) pointwise, but need 2n points |
| Interpolation | — | Θ(n²) via Lagrange, Θ(n³) via Vandermonde |

**Theorem 30.1 (Uniqueness):** n distinct point-value pairs uniquely determine a polynomial of degree-bound n.
- **Proof:** Vandermonde matrix V(x₀,...,x_{n-1}) with V_{kj} = xₖʲ is invertible (det ≠ 0) for distinct xₖ.

**Lagrange Interpolation Formula:**
A(x) = Σₖ yₖ · (Π_{j≠k} (x - xⱼ)) / (Π_{j≠k} (xₖ - xⱼ))
- Can compute coefficients in Θ(n²) time (Exercise 30.1-5).

**Polynomial Multiplication via FFT (Overall Strategy):**
```
1. Double degree-bound:   Pad A and B to 2n with zeros        Θ(n)
2. Evaluate:              Compute A(ω²ⁿₖ), B(ω²ⁿₖ) via FFT    Θ(n lg n)
3. Pointwise multiply:    C(ω²ⁿₖ) = A(ω²ⁿₖ)·B(ω²ⁿₖ)          Θ(n)
4. Interpolate:           Inverse FFT to get coefficients      Θ(n lg n)
```
**Theorem 30.2:** Two degree-bound n polynomials multiplyable in Θ(n lg n) time.

**Convolution:** c = a ⊗ b where cⱼ = Σₖ aₖ·b_{j-k}. Polynomial multiplication = convolution of coefficient vectors.

#### 30.2 The DFT and FFT

**Complex nth Roots of Unity:**
- ωₙ = e^{2πi/n} (principal nth root). All roots: ωₙᵏ for k=0,1,...,n-1.
- Form a multiplicative group isomorphic to (ℤₙ, +).
- Geometrically: equally spaced points on unit circle in complex plane.

**Key Lemmas:**
| Lemma | Statement | Use |
|-------|-----------|-----|
| **30.3 Cancellation** | ω_{dn}^{dk} = ωₙᵏ | Relates roots of different orders |
| **30.4 Corollary** | ωₙ^{n/2} = -1 (n even) | Gives negative values |
| **30.5 Halving** | (ωₙᵏ)² = ω_{n/2}ᵏ | Squares of nth roots = (n/2)th roots |
| **30.6 Summation** | Σ_{j=0}^{n-1} (ωₙᵏ)ʲ = 0 if n∤k | Orthogonality for inverse DFT |

**Discrete Fourier Transform (DFT):**
yₖ = Σ_{j=0}^{n-1} aⱼ ωₙ^{kj} for k = 0,...,n-1. y = Vₙ a where (Vₙ)_{kj} = ωₙ^{kj}.

**Fast Fourier Transform (FFT) — Divide & Conquer:**
```
FFT(a, n)
1 if n == 1
2     return a
3 ωₙ = e^{2πi/n}
4 ω = 1
5 a_even = (a₀, a₂, ..., a_{n-2})     // even-indexed coefficients
6 a_odd  = (a₁, a₃, ..., a_{n-1})     // odd-indexed coefficients
7 y_even = FFT(a_even, n/2)
8 y_odd  = FFT(a_odd, n/2)
9 for k = 0 to n/2 - 1
10    yₖ = y_evenₖ + ω·y_oddₖ
11    y_{k+n/2} = y_evenₖ - ω·y_oddₖ
12    ω = ω·ωₙ
13 return y
```
- **Recurrence:** T(n) = 2T(n/2) + Θ(n) = Θ(n lg n) (master theorem case 2).
- **Key optimization:** ω·y_oddₖ computed once (common subexpression) — the **butterfly operation**.
- **Twiddle factors:** ωₙᵏ for k=0,...,n/2-1.

**Example — DFT of (0, 1, 2, 3) with n=4:**
ω₄ = e^{2πi/4} = i. FFT computes:
- A(x) = 0 + 1·x + 2·x² + 3·x³.
- y₀ = A(1) = 6, y₁ = A(i) = -2+2i, y₂ = A(-1) = -2, y₃ = A(-i) = -2-2i.

**Why the Halving Lemma Enables Divide & Conquer:**
- A(x) = A_even(x²) + x·A_odd(x²).
- Evaluate at ωₙᵏ: A(ωₙᵏ) = A_even(ω_{n/2}ᵏ) + ωₙᵏ·A_odd(ω_{n/2}ᵏ).
- (ωₙᵏ)² = ω_{n/2}ᵏ, so both even and odd are polynomials of degree n/2 evaluated at (n/2)th roots.

- **Theorem 30.7:** Vₙ⁻¹ has entries ωₙ^{-kj}/n.
- Computed by same FFT algorithm with ωₙ replaced by ωₙ⁻¹ and each output divided by n.
- **Proof:** (Vₙ⁻¹ Vₙ)_{kk′} = (1/n) Σⱼ ωₙ^{-kj} ωₙ^{jk′} = (1/n) Σⱼ ωₙ^{j(k′-k)} = 1 if k′=k, else 0 (by summation lemma).


#### 30.3 FFT Circuits

```
```
- Named for butterfly-shaped wiring diagram.
- Each butterfly: 1 complex multiply, 1 add, 1 subtract.

- **lg n stages**, each stage has **n/2 butterflies** in parallel.
- **Stage s** (s=1,...,lg n): n/2s groups, 2^{s-1} butterflies per group. Twiddle factors: ωₘᵏ for m=2ˢ.
- **Base case:** n=1 — trivial (output = input). Smallest nontrivial: FFT₂ = single butterfly with ω₂ = e^{πi} = -1.
- **Depth:** Θ(lg n). **Total operations:** Θ(n lg n).

- Input aₖ goes to position rev(k) where rev(k) = reverse lg n bits of k.
- Example (n=8): input order 0,4,2,6,1,5,3,7.
- Binary: 000→000(0), 001→100(4), 010→010(2), 011→110(6), 100→001(1), etc.
- Reason: At each level, even-indexed (bit=0) go left subtree, odd-indexed (bit=1) go right. Stripping bits recursively produces bit-reversed order at leaves.


| Stage | Groups | Butterflies/Group | Twiddle Factors |
|-------|--------|-------------------|-----------------|
| 1 | n/2 | 1 | ω₂⁰ |
| 2 | n/4 | 2 | ω₄⁰, ω₄¹ |
| 3 | n/8 | 4 | ω₈⁰, ω₈¹, ω₈², ω₈³ |
| ... | ... | ... | ... |
| lg n | 1 | n/2 | ωₙ⁰,...,ωₙ^{n/2-1} |



- **n not a power of 2:** Pad with zeros to next power of 2 (at most doubles n). FFTW handles arbitrary sizes efficiently.
- **Numerical precision:** Complex arithmetic introduces roundoff errors. Modular arithmetic FFT (Problem 30-5) gives exact results for integer polynomials.
- **FFT using modular arithmetic (Problem 30-5):** Work in ℤₚ where p = kn+1 is prime and ω = gᵏ (g = generator of ℤₚ*). Avoids floating-point errors.
- **Chirp Transform (Ex 30.2-8):** Generalization of DFT: yₖ = Σ aⱼ z^{jk} for any complex z. Can be computed in O(n lg n) by rewriting as convolution using (jk) = (j² + k² - (k-j)²)/2.
- **Multidimensional FFT (Problem 30-2):** d-dimensional DFT computed by 1D FFTs along each dimension in sequence. Total: O(n lg n), independent of d.
- **Evaluating all derivatives (Problem 30-3):** Compute A^{(t)}(x₀) for t=0,...,n-1 in O(n lg n) by relating to convolution of coefficient sequences.
- **Multiple point evaluation (Problem 30-4):** Evaluate degree-bound n polynomial at n arbitrary points in O(n lg² n) using divide-and-conquer on remainder trees.



---

## Chapter 31: Number-Theoretic Algorithms

### 31.1 Elementary Number Theory

**Division theorem (31.1):** For integers a, n>0, ∃ unique q, r: a = qn + r, 0 ≤ r < n. r = a mod n.

**gcd properties:**
- gcd(a, b) = smallest positive linear combination ax + by (Theorem 31.2)
- gcd(an, bn) = n·gcd(a, b)
- If n|ab and gcd(a,n)=1 then n|b (Corollary 31.5)

**Relatively prime:** gcd(a,b) = 1. If gcd(a,p)=gcd(b,p)=1 then gcd(ab,p)=1 (Theorem 31.6).

**Theorem 31.7:** If prime p|ab then p|a or p|b.
**Theorem 31.8 (Unique prime factorization):** Every integer has unique factorization.

### 31.2 Greatest Common Divisor

**Theorem 31.9 (GCD recursion):** gcd(a, b) = gcd(b, a mod b)

**EUCLID:**
```
EUCLID(a, b)
1 if b == 0
2     return a
3 else return EUCLID(b, a mod b)
```

**Lamé's theorem (31.11):** If a > b ≥ 1 and b < F_{k+1}, then EUCLID(a,b) makes < k recursive calls.
Worst-case: EUCLID(F_{k+1}, F_k) makes exactly k-1 calls.
Running time: O(lg b) arithmetic operations, O(β³) bit operations (β = bit-length).

**EXTENDED-EUCLID:**
```
EXTENDED-EUCLID(a, b)
1 if b == 0
2     return (a, 1, 0)
3 else (d′, x′, y′) = EXTENDED-EUCLID(b, a mod b)
4     (d, x, y) = (d′, y′, x′ - ⌊a/b⌋·y′)
5     return (d, x, y)
```
Returns (d, x, y) with d = gcd(a,b) = ax + by.

### 31.3 Modular Arithmetic

**Group (S, ⊕):** closure, identity, associativity, inverses. Abelian: also commutative.

- **(ℤ_n, +_n):** additive group modulo n, size n, identity 0.
- **(ℤ_n^*, ·_n):** multiplicative group modulo n, elements = {a∈ℤ_n : gcd(a,n)=1}, size φ(n).

**Euler's phi function:** φ(n) = n·Π_{p|n} (1 - 1/p). If p prime, φ(p) = p-1, φ(p^e) = p^{e-1}(p-1).

**Theorem 31.14:** Nonempty closed subset of finite group is a subgroup.
**Theorem 31.15 (Lagrange):** |S′| divides |S| for any subgroup S′.
**Corollary 31.16:** Proper subgroup has size ≤ |S|/2.

**Order of a:** smallest t > 0 with a^{(t)} = e. ord(a) = |⟨a⟩|.
**Corollary 31.19:** a^{(|S|)} = e for any a in finite group S.

### 31.4 Solving Modular Linear Equations

**Equation:** ax ≡ b (mod n). Let d = gcd(a,n).

- **Corollary 31.21:** Solvable iff d|b
- **Corollary 31.22:** Either d distinct solutions modulo n or none
- **Theorem 31.23:** One solution: x₀ = x′(b/d) mod n (from EXTENDED-EUCLID)
- **Theorem 31.24:** All d solutions: xᵢ = x₀ + i(n/d) mod n for i=0,...,d-1

```
```


### 31.5 Chinese Remainder Theorem




### 31.6 Powers of an Element

```
```

### 31.7 RSA Public-Key Cryptosystem





### 31.8 Primality Testing

- Write n-1 = 2^t·u where u odd
- Pick random a ∈ [1, n-1]
- Compute x₀ = a^u mod n
- Square t times: xᵢ = x_{i-1}² mod n
- If x₀ ≠ 1 and for all i: xᵢ ≠ n-1, then n is composite
- Otherwise n is "probably prime"


---

## Chapter 32: String Matching

### Problem Statement

Text T[1:n], pattern P[1:m]. Find all shifts s (0 ≤ s ≤ n-m) where T[s+1:s+m] = P[1:m].

### Algorithm Summary

| Algorithm | Preprocessing | Matching |
|-----------|--------------|----------|
| Naive | 0 | O((n-m+1)m) |
| Rabin-Karp | Θ(m) | O((n-m+1)m) worst, O(n+m) expected |
| Finite Automaton | O(m|Σ|) | Θ(n) |
| KMP | Θ(m) | Θ(n) |
| Suffix Array | O(n lg n) | O(m lg n + km) |

### 32.1 Naive Algorithm

```
NAIVE-STRING-MATCHER(T, P, n, m)
1 for s = 0 to n - m
2     if P[1:m] == T[s+1:s+m]
3         print "Pattern occurs with shift" s
```
Worst-case: Θ((n-m+1)m) — e.g., P = a^m, T = a^n.

### 32.2 Rabin-Karp

**Idea:** View strings as numbers in base d (|Σ|). Compute numerical value of pattern and each m-length text window modulo prime q.

**Horner for p:** p = P[m] + d·(P[m-1] + d·(...P[1]...)) mod q

**Rolling hash:** t_{s+1} = (d·(t_s - T[s+1]·d^{m-1}) + T[s+m+1]) mod q

```
RABIN-KARP-MATCHER(T, P, n, m, d, q)
1 h = d^{m-1} mod q
2 p = 0; t₀ = 0
3 for i = 1 to m           // preprocessing
4     p = (d·p + P[i]) mod q
5     t₀ = (d·t₀ + T[i]) mod q
6 for s = 0 to n - m       // matching
7     if p == t_s          // hit (possibly spurious)
8         if P[1:m] == T[s+1:s+m]   // verify
9             print "Pattern occurs with shift" s
10    if s < n - m
11        t_{s+1} = (d·(t_s - T[s+1]·h) + T[s+m+1]) mod q
```

Expected time: O(n+m) with O(1) valid shifts and q > m. Worst: Θ((n-m+1)m).

### 32.3 Finite Automaton

**Suffix function σ(x):** length of longest prefix of P that is a suffix of x.

**Transition function:** δ(q, a) = σ(P[:q]·a)

**String-matching automaton:** Q = {0,...,m}, start = 0, accept = m.

```
FINITE-AUTOMATON-MATCHER(T, δ, n, m)
1 q = 0
2 for i = 1 to n
```



### 32.4 Knuth-Morris-Pratt (KMP)


```
```

```
```



### 32.5 Suffix Arrays






---

## Chapter 33: Machine-Learning Algorithms

### 33.1 Clustering

**k-means problem:** Given points S ⊂ ℝ^d, find k centers C = ⟨c^{(1)},...,c^{(k)}⟩ minimizing:
f(S, C) = Σ_{x∈S} min_{ℓ} ||x - c^{(ℓ)}||²

**Theorem 33.1:** Optimal center for cluster S^{(ℓ)} is centroid (mean): c^{(ℓ)} = (1/|S^{(ℓ)}|)·Σ_{x∈S^{(ℓ)}} x

**Theorem 33.2:** Given centers, optimal assignment is nearest-center rule.

**Lloyd's procedure:**
1. Initialize k centers randomly from S
2. Assign points to nearest center
3. If no change, stop
4. Recompute centers as centroids; go to 2

**Properties:** Always terminates (f strictly decreases each iteration except last). Finds local minimum. May not be optimal.

**Running time per iteration:** O(dkn) for assignment + O(dn) for centroid recomputation.

**Complications:** Data normalization, missing values, choice of k, empty clusters, tie-breaking.

### 33.2 Multiplicative Weights

**Problem:** n experts, T events. Each event t: experts predict p_i^{(t)} ∈ {0,1}, learner predicts p^{(t)}, outcome o^{(t)} revealed.

**Goal:** Minimize regret = m - m* where m = learner mistakes, m* = best expert mistakes.

**WEIGHTED-MAJORITY (parameter γ ≤ 1/2):**
1. Initialize all weights w_i = 1
2. For each event t:
   - upweight = Σ_{i: p_i^{(t)}=1} w_i
   - downweight = Σ_{i: p_i^{(t)}=0} w_i
   - Predict 1 if upweight ≥ downweight, else 0
   - For each expert i: if wrong, w_i ← w_i·(1-γ)

**Theorem 33.4:** For any expert i, after T′ ≤ T events:
m(T′) ≤ 2(1+γ)·m_i(T′) + (2 ln n)/γ

**Corollary 33.5:** m ≤ 2(1+γ)·m* + (2 ln n)/γ

**Analysis uses potential function W(t) = Σ w_i.** On mistakes: W(t+1) ≤ (1 - γ/2)·W(t). Combined with w_i(t) ≤ (1-γ)^{m_i(t)}.


### 33.3 Gradient Descent


```
```

- Every local minimum is global minimum
- Lies above tangent hyperplane: f(y) ≥ f(x) + ⟨(∇f)(x), y-x⟩


```
```


- Solving Ax = b by minimizing f(x) = ½||Ax - b||²
- Linear regression: minimize Σ (w·x^{(i)} - y^{(i)})²

---

## Chapter 34: NP-Completeness

### 34.1 Polynomial Time

**Class P:** Languages decidable in O(n^k) time.

**Abstract decision problem:** Maps instance set I to {0,1}.
**Concrete problem:** Instance set = {0,1}*.
**Encoding:** Maps abstract instances to binary strings.

**Lemma 34.1:** Polynomially related encodings preserve membership in P.

**Formal-language view:**
- P = {L ⊆ {0,1}* : ∃ algorithm A that decides L in polynomial time}
- **Theorem 34.2:** P = {L : L is accepted in polynomial time} (accepted = algorithm outputs 1 for x∈L, may run forever for x∉L — but can simulate with cutoff)

**Closure:** P closed under union, intersection, complement, concatenation, Kleene star.

### 34.2 Polynomial-Time Verification

**Class NP:** Languages verifiable in polynomial time.
L ∈ NP iff ∃ polynomial-time algorithm A and constant c such that:
L = {x : ∃ certificate y, |y| = O(|x|^c), A(x, y) = 1}

**HAM-CYCLE:** Graph has hamiltonian cycle? Certificate = sequence of vertices.

**co-NP:** {L : L ∈ NP}. Whether NP = co-NP is open.

**P ⊆ NP ⊆ EXP**, but P ≠ NP believed.

### 34.3 NP-Completeness and Reducibility

**Polynomial-time reduction:** L₁ ≤_P L₂ if ∃ polynomial-time f s.t. x∈L₁ ⇔ f(x)∈L₂.

**Lemma 34.3:** If L₁ ≤_P L₂ and L₂ ∈ P, then L₁ ∈ P.

**NP-complete:** L ∈ NPC if (1) L ∈ NP, (2) L′ ≤_P L for all L′ ∈ NP.
**NP-hard:** Satisfies (2) but not necessarily (1).

**Theorem 34.4:** If any NP-complete problem is in P, then P = NP.

**Cook-Levin Theorem:** CIRCUIT-SAT is NP-complete.
- Proof: Construct circuit that simulates Turing machine verifying certificate. Circuit has size polynomial in n^k.

### 34.4 NP-Completeness Proofs — Reductions

**CIRCUIT-SAT ≤_P SAT:**
- Convert circuit to boolean formula
- Each gate becomes a clause: e.g., AND gate z = x∧y becomes (z ↔ (x∧y)) ≡ (¬z∨x)∧(¬z∨y)∧(z∨¬x∨¬y)
- Output gate forced to 1

**SAT ≤_P 3-CNF-SAT:**
1. Parse formula into parse tree, introduce variable for each internal node

- Vertices in same clause
- Vertices representing contradictory literals (x and ¬x)






### 34.5 NP-Complete Problems Reference

- CIRCUIT-SAT (first — Cook-Levin)
- SAT (from CIRCUIT-SAT)
- 3-CNF-SAT (from SAT)
- CLIQUE (from 3-CNF-SAT)
- VERTEX-COVER (from CLIQUE)
- HAM-CYCLE (from VERTEX-COVER)
- TSP (from HAM-CYCLE)
- SUBSET-SUM (from 3-CNF-SAT)
- PARTITION (from SUBSET-SUM)
- BIN-PACKING (from PARTITION)
- SET-COVER (from VERTEX-COVER)
- KNAPSACK (from SUBSET-SUM, has pseudo-polynomial DP)

- **Strongly NP-complete:** remains NP-complete even when numbers are unary (e.g., SET-COVER)
- **Pseudo-polynomial:** polynomial in the numeric value but not bit-length (e.g., KNAPSACK DP is O(nt))
- **PSPACE:** problems solvable with polynomial space (containing NP)
- **#P:** counting versions of NP problems (#SAT: count satisfying assignments)

---

## Chapter 35: Approximation Algorithms

### Performance Ratios

**ρ(n)-approximation algorithm:** For all inputs of size n:
- Minimization: C/C* ≤ ρ(n)
- Maximization: C*/C ≤ ρ(n)

**Approximation scheme:** (1+ε)-approximation for any ε>0.
- **PTAS:** polynomial in n for fixed ε
- **FPTAS:** polynomial in n and 1/ε

### 35.1 Vertex Cover

**APPROX-VERTEX-COVER:**
```
APPROX-VERTEX-COVER(G)
1 C = ∅
2 E′ = G.E
3 while E′ ≠ ∅
4     let (u,v) be an arbitrary edge of E′
5     C = C ∪ {u, v}
6     remove from E′ edge (u,v) and edges incident on u or v
7 return C
```

**Theorem 35.1:** 2-approximation. Proof: Let A be selected edges. |A| ≤ |C*| (maximal matching lower bound). |C| = 2|A| ≤ 2|C*|.

### 35.2 Traveling Salesperson

**With triangle inequality (c(u,w) ≤ c(u,v) + c(v,w)):**

**APPROX-TSP-TOUR:**
```
APPROX-TSP-TOUR(G, c)
1 select root r ∈ V
2 compute MST T from r using MST-PRIM
3 H = preorder walk of T
4 return hamiltonian cycle H
```

**Theorem 35.2:** 2-approximation. Proof: c(T) ≤ c(H*) (MST lower bound). Full walk W has c(W) = 2c(T). Shortcutting (triangle inequality) gives c(H) ≤ c(W) = 2c(T) ≤ 2c(H*).

**Christofides algorithm:** 1.5-approximation (minimum spanning tree + minimum-weight perfect matching on odd-degree vertices + shortcut).

**Without triangle inequality:**
**Theorem 35.3:** No ρ-approximation for any ρ≥1 unless P=NP.
Proof: Transform HAM-CYCLE: edges in G cost 1, others cost ρ|V|+1. If ρ-approximation exists, it distinguishes hamiltonian from non-hamiltonian graphs.

### 35.3 Set Cover

**GREEDY-SET-COVER:**
```
GREEDY-SET-COVER(X, ℱ)
1 U₀ = X
2 C = ∅
3 i = 0
4 while Uᵢ ≠ ∅
5     select S ∈ ℱ maximizing |S ∩ Uᵢ|
6     U_{i+1} = Uᵢ - S
7     C = C ∪ {S}
8     i = i + 1
9 return C
```

**Theorem 35.4:** O(lg |X|)-approximation.
Proof: Let k = |C*|. |U_{i+1}| ≤ |Uᵢ|·(1 - 1/k). After ck iterations with c ≥ ln|X|, |U_i| < 1. |C| = c·|C*|·⌈ln|X|⌉.

### 35.4 Randomization and Linear Programming






### 35.5 Subset Sum — FPTAS

```
```



```
```



---

## Key Techniques Across Chapters

| Technique | Chapter | Application |
|-----------|---------|-------------|
| Work/span analysis | 26 | Parallel algorithm analysis |
| Competitive analysis | 27 | Online algorithm quality |
| LUP decomposition | 28 | Solving linear systems |
| LP duality | 29 | Proving optimality |
| FFT divide-and-conquer | 30 | Polynomial multiplication |
| Extended Euclid | 31 | Modular inverses, CRT |
| Prefix function (KMP) | 32 | Linear-time string matching |
| Gradient descent | 33 | Continuous optimization |
| Polynomial reduction | 34 | NP-completeness proofs |
| PTAS/FPTAS | 35 | Approximation schemes |

### Ch 31 Edge Cases
- **gcd(0,0)** = 0 (by definition).
- **gcd(0, n)** = n.
- **a < b in EUCLID**: swaps in first call.
- **Modular equation with no solutions**: d ∤ b.
- **RSA with M ≡ 0 mod p or q**: still works (0^ed ≡ 0 mod p).
- **Carmichael numbers**: satisfy Fermat but are composite; Miller-Rabin catches via nontrivial square root.

### Ch 32 Edge Cases
- **m = 0** (empty pattern): not allowed (m ≥ 1).
- **m = n**: only one possible shift (s = 0).
- **Pattern longer than text** (m > n): no valid shifts.
- **Empty text** (n = 0): no valid shifts.
- **All characters match** (P = a^m, T = a^n): worst case for naive and Rabin-Karp.
- **Spurious hits** in Rabin-Karp: ts ≡ p (mod q) but ts ≠ p.
- **Ties in nearest-center rule**: must break consistently, don't change unless strictly closer.
- **Empty clusters**: possible in k-means if many identical points.

### Ch 33 Edge Cases
- **k = 1** or **k = n**: trivial clusterings.
- **k = 0**: not defined.
- **Duplicate points**: frequent in vector quantization; use special initialization (Exercise 33.1-3).
- **Missing attribute values**: ignore or impute with median.
- **Step size too large**: can overshoot minimum, increase error.
- **Non-convex function**: gradient descent finds local, not global, minimum.
- **Projection for constrained GD**: if x' is already in K, projection is identity.

---

## All Exercises Listed

### Ch 31: 31.1-1 through 31.1-14, 31.2-1 through 31.2-9, 31.3-1 through 31.3-5, 31.4-1 through 31.4-4, 31.5-1 through 31.5-4, 31.6-1 through 31.6-5, 31.7-1 through 31.7-3, 31.8-1 through 31.8-3

### Ch 32: 32.1-1 through 32.1-4, 32.2-1 through 32.2-4, 32.3-1 through 32.3-6, 32.4-1 through 32.4-8, 32.5-1 through 32.5-4

### Ch 33: 33.1-1 through 33.1-4, 33.2-1 through 33.2-4, 33.3-1 through 33.3-7

**Starred (hard):** 31.1-11, 31.4-4, 31.7-3, 31.8-2, 32.3-5, 32.4-8, 32.5-4.

## Chapter 34: NP-Completeness

### 34.1 The Class P (Polynomial Time)

**Definition of P:**
P = { L ⊆ {0,1}* : there exists an algorithm A that decides L in polynomial time }.
Equivalently: L ∈ P if ∃ algorithm A and constant k such that for any input x of length n = |x|, A runs in O(n^k) time and correctly decides whether x ∈ L (outputs 1 if x ∈ L, 0 otherwise).

**Abstract Problems & Encodings:**
- An abstract problem Q is a binary relation on a set I of instances and a set S of solutions.
- Decision problems: Q maps I → {0,1} (yes/no).
- Encoding e: S → {0,1}* maps abstract objects to binary strings.
- A concrete problem has instance set = {0,1}*.
- Two encodings e₁, e₂ are polynomially related if there exist polynomial-time computable f₁₂, f₂₁ mapping between them.
- Lemma 34.1: If e₁, e₂ are polynomially related, then e₁(Q) ∈ P ⇔ e₂(Q) ∈ P.

**Formal Language Framework:**
- Alphabet Σ, language L ⊆ Σ*.
- L is decided by algorithm A if ∀x∈{0,1}*: A(x)=1 when x∈L, A(x)=0 when x∉L.
- L is accepted by A if A(x)=1 for x∈L (may loop forever on x∉L).
- Theorem 34.2: P = { L : L is accepted by a polynomial-time algorithm }.
  - Proof: If A accepts L in O(n^k), simulate cn^k steps; if accepted → 1 else → 0.
- P is closed under union, intersection, concatenation, complement, Kleene star.

### 34.2 The Class NP (Nondeterministic Polynomial Time)

**Verification Algorithms:**
- A verification algorithm A takes two arguments: input string x and certificate y.
- L = { x : ∃ y such that A(x,y) = 1 }.
- Certificate y must have length polynomial in |x|.

**Definition of NP:**
L ∈ NP if ∃ polynomial-time verification algorithm A and constant c such that:
- x ∈ L ⇔ ∃ certificate y with |y| = O(|x|^c) and A(x,y) accepts in O(|x|^k) time.

**Equivalent definition via NTM:**
L ∈ NP if there exists a nondeterministic Turing machine N that decides L in polynomial time. The NTM nondeterministically guesses the certificate and then verifies it deterministically.

**Key Examples in NP:**
- HAM-CYCLE: certificate = sequence of |V| vertices forming hamiltonian cycle. Verification: O(n²) checks that it's a permutation, each consecutive pair is an edge, and first/last are adjacent.
- 3-CNF-SAT: certificate = assignment of values to variables. Verification: evaluate formula in O(m) time where m is number of clauses.
- CLIQUE: certificate = set V' ⊆ V of vertices. Verification: check all (|V'| choose 2) pairs for edges.
- SUBSET-SUM: certificate = subset S'. Verification: sum elements and compare to target t.
- TSP: certificate = sequence of n vertices. Verification: sum edge costs, compare to k.

**Relationship:**
- P ⊆ NP (since a polynomial-time decider can ignore any certificate).
- The P ≠ NP question: is P a proper subset of NP? Most researchers believe yes.
- NP is closed under union, intersection, concatenation, Kleene star. Closure under complement is unknown.

**co-NP:**
- co-NP = { L : L ∈ NP }.
- Example: TAUTOLOGY = { boolean formulas that evaluate to 1 for all assignments } ∈ co-NP. (A certificate of non-satisfiability would be a counterexample assignment.)
- P ⊆ NP ∩ co-NP.
- The question NP = co-NP is also open. Most believe NP ≠ co-NP.

**Other Complexity Classes Mentioned:**
- PSPACE: problems solvable with polynomial space (even if exponential time).
- PSPACE-complete: QBF (Quantified Boolean Formulas), TQBF (True Quantified Boolean Formulas).
- #P: counting problems (e.g., #SAT = number of satisfying assignments). #P-complete problems are at least as hard as NP-complete problems.

### 34.3 NP-Completeness and Reducibility

**Polynomial-Time Reducibility:**
- L₁ ≤_P L₂ (L₁ is polynomial-time reducible to L₂) if ∃ polynomial-time computable function f: {0,1}* → {0,1}* such that: x ∈ L₁ ⇔ f(x) ∈ L₂ for all x.
- Lemma 34.3: If L₁ ≤_P L₂ and L₂ ∈ P, then L₁ ∈ P. (Proof: compute f(x), decide f(x) ∈ L₂.)
- ≤_P is transitive (Exercise 34.3-2).

**Definition of NP-Complete:**
L is NP-complete if:
1. L ∈ NP, and
2. L' ≤_P L for every L' ∈ NP (L is NP-hard).

If L satisfies property 2 but not necessarily 1, L is NP-hard.
NPC = class of NP-complete languages.

**Theorem 34.4:** If any NP-complete problem is polynomial-time solvable, then P = NP. Conversely, if P ≠ NP, then no NP-complete problem is polynomial-time solvable.

**The Cook-Levin Theorem (Circuit SAT is NP-complete):**

**Lemma 34.5 (CIRCUIT-SAT ∈ NP):**
Certificate = assignment of boolean values to every wire in the circuit. Verification algorithm: check each gate's output is correctly computed from its inputs; check circuit output = 1. Runs in polynomial (linear) time.

**Lemma 34.6 (CIRCUIT-SAT is NP-hard):**
Proof sketch: Let L ∈ NP with verification algorithm A running in T(n) = O(n^k) time. Represent computation of A on input x and certificate y as a sequence of T(n) configurations c₀, c₁, ..., c_{T(n)}. Each configuration includes: program for A, program counter, auxiliary machine state, input x, certificate y, working storage.
- A boolean combinational circuit M (the computer hardware) maps each configuration c_i to c_{i+1}.
- The reduction algorithm F constructs circuit C' by pasting together T(n) copies of M (output of copy i → input of copy i+1).
- F wires the program, program counter, input x, and initial memory to known constant values. The only remaining inputs correspond to certificate y.
- The output is the bit of c_{T(n)} corresponding to A's output.
- C is satisfiable ⇔ ∃ y such that A(x,y) = 1.
- C has size polynomial in n (each configuration is polynomial in size, T(n) copies).
- Construction is polynomial time.

**Theorem 34.7:** CIRCUIT-SAT is NP-complete (immediate from Lemmas 34.5 and 34.6).

### 34.4 NP-Completeness Proofs

**Lemma 34.8 (Reduction Methodology):**
If L' ∈ NPC and L' ≤_P L, then L is NP-hard. If also L ∈ NP, then L ∈ NPC.

**Proof Steps for NP-Completeness:**
1. Show L ∈ NP: describe certificate, show polynomial-time verification.
2. Show L is NP-hard: select known NP-complete L', give polynomial-time reduction f from L' to L, prove x ∈ L' ⇔ f(x) ∈ L.
3. Conclude L ∈ NPC.

#### CIRCUIT-SAT ≤_P SAT

**Construction:**
Given circuit C with wires x₁,...,x_k, create formula φ with:
- A variable for each wire in C.
- For each gate, a clause (↔) describing the gate's function.
  - NOT gate with input a, output b: (b ↔ ¬a)
  - AND gate with inputs a,b, output c: (c ↔ (a ∧ b))
  - OR gate with inputs a,b, output c: (c ↔ (a ∨ b))
- φ = (output variable) ∧ (conjunction of all gate clauses).

**Example from text (Figure 34.10):**
φ = x₁₀ ∧ (x₄ ↔ ¬x₃) ∧ (x₅ ↔ (x₁ ∨ x₂)) ∧ (x₆ ↔ ¬x₄) ∧ (x₇ ↔ (x₁ ∧ x₂ ∧ x₄)) ∧ (x₈ ↔ (x₅ ∨ x₆)) ∧ (x₉ ↔ (x₆ ∨ x₇)) ∧ (x₁₀ ↔ (x₇ ∧ x₈ ∧ x₉)).

**Correctness:**
- (⇒) If C has satisfying assignment, set each wire variable to its value. Each gate clause evaluates to 1; output variable = 1.
- (⇐) If φ is satisfiable, the assignment to input variables gives a satisfying assignment for C. The gate clauses enforce correct computation.

**Polynomial time:** φ has O(|C|) variables and O(|C|) clauses, each of constant size.

**Why naive reduction fails:** If we recursively substitute gate functions, shared subformulas (fan-out > 1) cause exponential blowup. The variable-per-wire method avoids this.

**Theorem 34.9:** SAT is NP-complete.

#### SAT ≤_P 3-CNF-SAT

**Three-step transformation:**

**Step 1 — Parse tree to formula with variable per node:**
- Build binary parse tree of φ (literals = leaves, connectives = internal nodes).
- Introduce variable y_i for each internal node.
- φ' = (root variable) ∧ (conjunction of clauses y_i ↔ (operation of node i)).
- Each clause has ≤ 3 variables.

**Step 2 — Convert each clause to CNF using truth table:**
- For each clause C_i = (y_i ↔ (···)) with ≤ 3 variables, build its truth table.
- For rows where C_i = 0, write DNF formula for ¬C_i (OR of ANDs).
- Negate and apply DeMorgan's laws to get CNF for C_i.
- Result: φ'' is CNF with each clause having ≤ 3 literals, and φ'' ≡ φ'.
- Each clause with v variables produces ≤ 2^v ≤ 8 CNF clauses.

**Step 3 — Make each clause have exactly 3 distinct literals:**
- If clause has 3 literals: keep as is.
- If clause has 2 literals (l₁ ∨ l₂): replace with (l₁ ∨ l₂ ∨ p) ∧ (l₁ ∨ l₂ ∨ ¬p). Both assignments of p make one clause ≡ (l₁ ∨ l₂) and the other ≡ 1.
- If clause has 1 literal l: replace with (l ∨ p ∨ q) ∧ (l ∨ p ∨ ¬q) ∧ (l ∨ ¬p ∨ q) ∧ (l ∨ ¬p ∨ ¬q). One clause ≡ l, others ≡ 1.

**Correctness:** Each step preserves satisfiability. φ''' is satisfiable ⇔ φ'' is satisfiable ⇔ φ' is satisfiable ⇔ φ is satisfiable.

**Polynomial time:** Step 1 adds O(|φ|) variables and clauses. Step 2 adds ≤ 8 clauses per original clause (each with ≤ 3 variables, truth table ≤ 8 rows). Step 3 multiplies clauses by ≤ 4. Total size O(|φ|).

**Theorem 34.10:** 3-CNF-SAT is NP-complete.

### 34.5 Key NP-Complete Problems & Reductions

#### 3-CNF-SAT ≤_P CLIQUE

- Create graph G with 3k vertices: for each clause C_r = (l₁^r ∨ l₂^r ∨ l₃^r), create vertices v₁^r, v₂^r, v₃^r.
- Add edge between v_i^r and v_j^s (r ≠ s) iff literals l_i^r and l_j^s are consistent (not negations of each other).

- (⇒) If φ satisfiable, pick one true literal from each clause. The corresponding k vertices form a clique: they're from different clauses (so edges exist) and are consistent (both true, so cannot be complements).
- (⇐) If G has k-clique V', since no edges within same triple, V' has exactly one vertex per clause. Set literals corresponding to clique vertices to 1. No conflicts (no complementary literals in clique). Each clause satisfied (has a true literal).



#### CLIQUE ≤_P VERTEX-COVER

- Compute complement graph Ḡ = (V, Ē) where Ē = {(u,v) : u≠v, (u,v)∉E}.
- Output 〈Ḡ, |V|-k〉 as VERTEX-COVER instance.

- (⇒) G has k-clique V' ⇒ every pair in V' is connected in G ⇒ no edge in Ḡ connects vertices in V'. So for any edge (u,v)∈Ē, at least one endpoint is in V\V'. Thus V\V' (size |V|-k) is a vertex cover of Ḡ.
- (⇐) Ḡ has vertex cover V'' of size |V|-k ⇒ V\V'' (size k) has no edges in Ḡ between its vertices ⇒ every pair in V\V'' is an edge in G ⇒ V\V'' is a k-clique in G.


#### VERTEX-COVER ≤_P HAM-CYCLE



- 12 vertices: [u,v,1]..[u,v,6] and [v,u,1]..[v,u,6].
- 14 internal edges as shown in Figure 34.16(a).
- Only [u,v,1], [u,v,6], [v,u,1], [v,u,6] connect to outside.
- Three traversal modes:
  - (b) Enter [u,v,1]→exit [u,v,6], visit all 12 vertices.
  - (c) Enter [u,v,1]→exit [u,v,6], visit only [u,v,1..6] (re-enter later for [v,u,1..6]).
  - (d) Same as (b) but from v side.




- (⇒) G has vertex cover V*={u₁,...,u_k}. Construct hamiltonian cycle: start at s₁, traverse path through u₁'s gadgets (using appropriate traversal mode based on whether neighbor is also in cover), go to s₂, repeat for u₂,...,u_k, return to s₁.
- (⇐) G' has hamiltonian cycle. Partition into k cover paths, each starting at selector sᵢ, traversing all gadgets of some vertex uᵢ. These uᵢ form a vertex cover of G (each gadget visited means its edge is covered).



#### HAM-CYCLE ≤_P TSP

- Create complete graph G'=(V,E') where E' = {(i,j): i,j∈V, i≠j}.
- Cost function: c(i,j) = 0 if (i,j)∈E, else c(i,j) = 1.
- Ask: does G' have tour of cost ≤ 0?

- (⇒) G has hamiltonian cycle H. Every edge of H is in E, so cost 0. Thus G' has tour with cost 0 (≤ 0).
- (⇐) G' has tour H' of cost ≤ 0. Costs are 0 or 1, so cost = 0 ⇒ every edge in H' has cost 0 ⇒ every edge is in E. Thus H' is a hamiltonian cycle in G.



#### 3-CNF-SAT ≤_P SUBSET-SUM

- Create numbers in base 10 (or any base ≥ 7 to prevent carries).
- Each number has n+k digits: most significant n digits for variables, least significant k digits for clauses.
- Target t: 1 in each variable digit, 4 in each clause digit.
- For each variable x_i: create v_i (has 1 in x_i digit, 1 in C_j digit if x_i ∈ C_j) and v̄_i (has 1 in x_i digit, 1 in C_j digit if ¬x_i ∈ C_j).
- For each clause C_j: create s_j (1 in C_j digit) and s̄_j (2 in C_j digit) — slack variables.

- (⇒) Satisfying assignment: include v_i if x_i=1, else v̄_i. Each variable digit sums to 1 (target). Each clause digit gets 1-3 from true literals. Add slack variables to reach 4.
- (⇐) Subset summing to t must include exactly one of v_i, v̄_i per variable (for variable digit to be 1). Set x_i=1 if v_i included. For each clause C_j, since slack contributes ≤ 3, a vi/v̄_i with 1 in C_j digit must be included, meaning clause is satisfied.



### Complete List of NP-Complete Problems in CLRS Ch 34

1. **CIRCUIT-SAT** — Circuit satisfiability (first NP-complete problem)
2. **SAT** — Boolean formula satisfiability
3. **3-CNF-SAT** — 3-conjunctive normal form satisfiability
4. **CLIQUE** — Does graph contain a clique of size k?
5. **VERTEX-COVER** — Does graph have a vertex cover of size k?
6. **HAM-CYCLE** — Does graph have a hamiltonian cycle?
7. **TSP** — Traveling-salesperson problem (tour cost ≤ k)
8. **SUBSET-SUM** — Does subset sum to target t?
9. **PARTITION** (Exercise 34.5-5) — Can numbers be partitioned into two equal-sum sets?
10. **HAMILTONIAN-PATH** (Exercise 34.5-6) — Does graph have hamiltonian path?
11. **0-1 INTEGER-PROGRAMMING** (Exercise 34.5-2)
12. **GRAPH-COLORING** / **3-COLOR** (Problem 34-3)
13. **SUBSET-ISOMORPHISM** (Exercise 34.5-1)
14. **LONGEST-SIMPLE-CYCLE** (Exercise 34.5-7)
15. **HALF-3-CNF-SAT** (Exercise 34.5-8)
16. **INDEPENDENT-SET** (Problem 34-1)
17. **SET-COVER** (mentioned in context)
18. **KNAPSACK** (mentioned in context)
19. **3-DIMENSIONAL-MATCHING** (mentioned in context)
20. **BIN-PACKING** (mentioned in context)

### Reduction Chain Summary

```
```

### NP-Completeness Proof Checklist (for exams)


1. **Prove L ∈ NP**: Give certificate (polynomial size), describe polynomial-time verifier.
2. **Prove L is NP-hard**: Choose known NP-complete L', define f: instances(L') → instances(L), prove:
   - f is polynomial-time computable
   - x ∈ L' ⇔ f(x) ∈ L (two directions: completeness and soundness)
3. **Conclude** L ∈ NPC.

### Complexity Class Hierarchy

- **P**: polynomial-time decidable
- **NP**: polynomial-time verifiable
- **co-NP**: complement of NP (e.g., TAUTOLOGY ∈ co-NP; TAUTOLOGY-complete = co-NP-complete)
- **NPC**: NP-complete (hardest in NP)
- **PSPACE**: polynomial-space decidable (TQBF is PSPACE-complete)
- **#P**: counting versions of NP problems (#SAT is #P-complete)

---

## Chapter 35: Approximation Algorithms

### 35.0 Performance Ratios and Core Definitions

**Why approximation algorithms?** Many important problems are NP-complete, but we need practical solutions. Three options: (1) exponential algorithm for small inputs, (2) polynomial for special cases, (3) approximation algorithms for near-optimal solutions.

**Definition of ρ(n)-approximation algorithm:**
For any input of size n, let C = cost of algorithm's solution, C* = cost of optimal solution.

- **Minimization problem** (0 < C* ≤ C): approximation ratio = C/C*. We require C/C* ≤ ρ(n).
- **Maximization problem** (0 < C ≤ C*): approximation ratio = C*/C. We require C*/C ≤ ρ(n).
- Unified: max(C/C*, C*/C) ≤ ρ(n).

Always ρ(n) ≥ 1. A 1-approximation algorithm produces an optimal solution.

**Approximation Scheme:**
- Takes input instance and ε > 0.
- For any fixed ε, it's a (1+ε)-approximation algorithm.

**PTAS (Polynomial-Time Approximation Scheme):**
- For any fixed ε > 0, runs in time polynomial in n (input size).
- Running time may depend badly on ε (e.g., O(n^{2/ε})).

**FPTAS (Fully Polynomial-Time Approximation Scheme):**
- Runs in time polynomial in both n and 1/ε.
- Example: O((1/ε)² n³).

**PTAS vs FPTAS vs Constant-Factor vs Logarithmic:**
- **Constant-factor**: ρ = O(1) independent of n (e.g., 2-approximation).
- **Logarithmic**: ρ = O(log n) (e.g., greedy SET-COVER).
- **PTAS**: can achieve (1+ε) for any ε > 0, but not necessarily polynomial in 1/ε.
- **FPTAS**: polynomial in n and 1/ε — the gold standard.

### 35.1 Vertex-Cover Problem

**Problem:** Given undirected G=(V,E), find minimum vertex cover (set of vertices covering all edges).

**Algorithm APPROX-VERTEX-COVER:**
```
C = ∅
E' = G.E
while E' ≠ ∅
    pick arbitrary (u,v) ∈ E'
    C = C ∪ {u,v}
    remove from E' all edges incident to u or v
return C
```
Running time: O(V+E).

**Theorem 35.1:** APPROX-VERTEX-COVER is a polynomial-time 2-approximation algorithm.

**Proof:**
- Clearly a vertex cover (loop removes all edges).
- Let A = set of edges picked in line 4. A is a **maximal matching**: no two edges in A share an endpoint (when (u,v) picked, all incident edges are removed). So edges in A are pairwise disjoint.
- Any vertex cover must contain at least one endpoint of each edge in A. Since edges in A are disjoint: |C*| ≥ |A|.
- The algorithm adds both endpoints of each edge in A: |C| = 2|A|.
- Therefore: |C| = 2|A| ≤ 2|C*|.

**Key insight:** We bound |C*| from below by |A| (the size of a maximal matching). This lower bound technique is fundamental: we don't know C*, but we know it's ≥ |A|.

**Note:** The maximal matching A is not necessarily a maximum matching. The bound |C*| ≥ |A| holds for any maximal matching. (In fact |C*| ≥ size of maximum matching, which is ≥ |A|.)

### 35.2 Traveling-Salesperson Problem (TSP)

**Problem:** Complete undirected graph G=(V,E) with nonnegative integer cost c(u,v) on each edge. Find minimum-cost hamiltonian cycle (tour).

**Triangle inequality:** c(u,w) ≤ c(u,v) + c(v,w) for all u,v,w. Holds for Euclidean distances and many natural cost functions.

#### 35.2.1 TSP with Triangle Inequality

**Algorithm APPROX-TSP-TOUR(G,c):**
```
select root r ∈ G.V
compute MST T for G from root r using MST-PRIM(G,c,r)
let H be list of vertices in preorder walk of T
return the hamiltonian cycle H
```
Running time: Θ(V²) with simple Prim implementation.

**Theorem 35.2:** When triangle inequality holds, APPROX-TSP-TOUR is a 2-approximation algorithm.

**Proof:**
- Let H* be optimal tour. Delete any edge from H* → spanning tree. Since edge costs ≥ 0: c(T) ≤ c(H*). (MST is minimum, so c(T) ≤ c(any spanning tree) ≤ c(H*).)
- Full walk W of T traverses each edge twice: c(W) = 2c(T) ≤ 2c(H*).
- W is not a tour (visits vertices multiple times). Apply triangle inequality to shortcut repeated vertices. Shortcutting never increases cost (direct path ≤ path through intermediate vertices by triangle inequality).
- Resulting preorder tour H has c(H) ≤ c(W) ≤ 2c(H*).

**Example:** Full walk a,b,c,b,h,b,a,d,e,f,e,g,e,d,a → shortcut to preorder a,b,c,h,d,e,f,g.

**Christofides Algorithm (1.5-approximation):**
- Compute MST T.
- Let O = set of odd-degree vertices in T. |O| is even.
- Compute minimum-weight perfect matching M on O.
- Add M to T: multigraph T∪M is Eulerian (all even degrees).
- Compute Eulerian tour, shortcut to hamiltonian cycle.
- Cost ≤ c(T) + c(M) ≤ c(H*) + ½c(H*) = 1.5c(H*).
  - c(T) ≤ c(H*) (same as before).
  - c(M) ≤ ½c(H*): shortcut optimal tour through O gives tour of cost ≤ c(H*), matching is at most half of this.

#### 35.2.2 General TSP (Without Triangle Inequality)

**Theorem 35.3:** If P ≠ NP, then for any constant ρ ≥ 1, there is no polynomial-time ρ-approximation algorithm for general TSP.

**Proof (by contradiction):**
- Suppose such an algorithm A exists with ratio ρ.
- Given instance G=(V,E) of HAM-CYCLE, construct TSP instance G' = complete graph on V with cost:
  - c(u,v) = 1 if (u,v)∈E
  - c(u,v) = ρ|V| + 1 if (u,v)∉E
- If G has hamiltonian cycle H: optimal TSP cost = |V| (use edges of cost 1). A must return tour of cost ≤ ρ·|V|.
- If G has no hamiltonian cycle: any TSP tour must use at least one edge ∉E, cost ≥ (ρ|V|+1)+(|V|-1) = ρ|V|+|V| > ρ|V|.
- So A returns tour of cost ≤ ρ|V| ⇔ G has hamiltonian cycle. Thus A solves HAM-CYCLE in polynomial time ⇒ P = NP. Contradiction.

**Implication:** Without triangle inequality, no constant-factor approximation exists unless P=NP. Even |V|^c approximation is impossible (Exercise 35.2-6).

### 35.3 Set-Cover Problem

**Problem:** Instance (X, ℱ) where X = finite set, ℱ = family of subsets of X covering X (∪_{S∈ℱ} S = X). Find minimum-size subfamily C ⊆ ℱ whose union = X.

**Greedy Algorithm GREEDY-SET-COVER(X, ℱ):**
```
U₀ = X
C = ∅
i = 0
while U_i ≠ ∅
    select S ∈ ℱ maximizing |S ∩ U_i|
    U_{i+1} = U_i \ S
    C = C ∪ {S}
    i = i + 1
return C
```

**Theorem 35.4:** GREEDY-SET-COVER is a polynomial-time O(log|X|)-approximation algorithm.

**Proof:**
- Let C* = optimal cover, k = |C*|.
- At each step, optimal cover (size k) covers remaining U_i. By pigeonhole, some set in C* covers ≥ |U_i|/k elements of U_i.
- The greedy choice covers at least this many: |U_i| - |U_{i+1}| ≥ |U_i|/k.
- So |U_{i+1}| ≤ |U_i|(1 - 1/k).
- By iteration: |U_i| ≤ |X|(1 - 1/k)^i.
- Using 1 - 1/k ≤ e^{-1/k}: |U_i| ≤ |X|·e^{-i/k}.
- Algorithm stops when |U_i| < 1. Solve |X|·e^{-i/k} < 1 ⇒ i > k·ln|X|.
- Therefore |C| = number of iterations ≤ k·⌈ln|X|⌉ = |C*|·⌈ln|X|⌉.

**Harmonic number bound:** More precisely, the approximation ratio is H(d) where d = max{|S|: S∈ℱ} and H(d) = 1 + 1/2 + ... + 1/d = ln d + O(1).

- Assign cost 1 to each chosen set, distribute equally among newly covered elements.
- When set S is chosen, each newly covered element gets cost 1/|S∩U_i|.
- Lemma: If an element e is first covered when |U_i| = m, its cost ≤ OPT/m.
- Total cost = sum of element costs ≤ OPT·(1 + 1/2 + ... + 1/n) = OPT·H_n.

### 35.4 Randomization and Linear Programming

#### 35.4.1 Randomized Algorithm for MAX-3-CNF-SAT




- For clause i with 3 distinct literals (no variable and its negation in same clause): literals are independent.
- Clause i is unsatisfied only if all 3 literals = 0. Pr[unsatisfied] = (1/2)³ = 1/8.
- Pr[satisfied] = 7/8.
- Let Y_i = I{clause i satisfied}, E[Y_i] = 7/8.
- Y = total satisfied clauses. E[Y] = Σ E[Y_i] = 7m/8.
- Since optimal ≤ m: E[Y] ≥ 7/8 · OPT. So E[C*]/E[C] = OPT/E[Y] ≤ m/(7m/8) = 8/7.


#### 35.4.2 Weighted Vertex Cover via Linear Programming




```
```


- LP can be solved in polynomial time.
- C is a vertex cover: for any edge (u,v), x(u)+x(v) ≥ 1 ⇒ at least one ≥ 1/2 ⇒ included.
- Weight bound: w(C) = Σ_{v: x(v)≥1/2} w(v) ≤ 2·Σ_{v: x(v)≥1/2} w(v)·x(v) ≤ 2·Σ_{all v} w(v)·x(v) = 2z*.
- Since z* ≤ w(C*) (LP relaxes integer program): w(C) ≤ 2z* ≤ 2w(C*).


### 35.5 Subset-Sum Problem — Exact Algorithm and FPTAS


#### Exact Exponential Algorithm EXACT-SUBSET-SUM

```
```
- L_i = sorted list of all subset sums of {x₁,...,x_i} that are ≤ t.
- |L_i| can be 2^i — exponential in worst case.

#### FPTAS: APPROX-SUBSET-SUM



```
```

```
```



- Let y* = optimal solution (maximum sum ≤ t in P_n).
- Claim: For every element y ∈ P_i with y ≤ t, there exists z ∈ L_i with z ≤ y and y/z ≤ (1+ε/2n)^i.
- Proof by induction: base i=0 trivial. Step: y is either in P_{i-1} or = y'+x_i where y'∈P_{i-1}. Apply IH, then use trimming property (z_trim ≥ z_merge/(1+δ)).
- So for y* ∈ P_n, ∃ z ∈ L_n with z ≤ y* and y*/z ≤ (1+ε/2n)^n.
- Since z* = max L_n, we have z ≤ z* ≤ y*.
- (1+ε/2n)^n ≤ e^{ε/2} ≤ 1 + ε/2 + (ε/2)² ≤ 1 + ε (for 0<ε<1).
- Therefore y*/z* ≤ 1 + ε. Equivalent to z* ≥ y*/(1+ε) ≥ (1-ε)y* (since 1/(1+ε) ≥ 1-ε).

- After trimming, successive elements differ by factor ≥ 1+δ.
- So |L_i| ≤ log_{1+δ}(t) + 2 ≤ (ln t)/δ + 2 = (2n ln t)/ε + 2.
- Input size: O(n + log t) bits.
- |L_i| = O(n·log t / ε) — polynomial in n, log t, and 1/ε.
- MERGE-LISTS runs in O(|L_{i-1}|) per iteration.
- Total time: O(n · |L_n|) = O(n²·log t / ε) = O(n³/ε) if we treat log t as O(n).


### Summary of Approximation Algorithms from CLRS Ch 35

| Problem | Algorithm | Ratio | Type |
|---------|-----------|-------|------|
| VERTEX-COVER | APPROX-VERTEX-COVER | 2 | Constant-factor |
| TSP (triangle inequality) | APPROX-TSP-TOUR (MST+preorder) | 2 | Constant-factor |
| TSP (triangle inequality) | Christofides | 1.5 | Constant-factor |
| TSP (general) | None (unless P=NP) | No constant | Impossibility |
| SET-COVER | GREEDY-SET-COVER | H(d) ≈ ln n | Logarithmic |
| MAX-3-CNF-SAT | Random assignment | 8/7 ≈ 1.143 | Randomized constant |
| WEIGHTED VERTEX-COVER | LP rounding | 2 | Constant-factor |
| SUBSET-SUM | APPROX-SUBSET-SUM | 1+ε | FPTAS |

---

## Cross-Cutting Topics

### Design Paradigms & Meta-Methods

**Incremental (Insertion Sort):** Build solution incrementally by inserting one element at a time. Used in Ch 2 (insertion sort), Ch 7 (PARTITION builds low side incrementally).

**Divide-and-Conquer (D&C):** Divide problem into independent subproblems; solve recursively; combine. Recurrence: T(n) = aT(n/b) + f(n). Solve via Master Theorem. Used in: Ch 2 (merge sort), Ch 4 (Strassen), Ch 7 (quicksort), Ch 9 (SELECT), Ch 30 (FFT). Key: subproblems must be disjoint (no overlap).

**Randomization:** Random choice of pivot/input avoids worst-case behavior. Used in: Ch 5 (RANDOMIZED-HIRE-ASSISTANT, RANDOMLY-PERMUTE), Ch 7 (RANDOMIZED-QUICKSORT), Ch 9 (RANDOMIZED-SELECT), Ch 31 (Miller-Rabin primality test).

**Dynamic Programming:** Optimal substructure + overlapping subproblems. Top-down with memoization or bottom-up table-filling. Used in: Ch 14 (rod cutting, matrix-chain, LCS, optimal BST).

**Greedy Strategy:** Greedy-choice property + optimal substructure. Always take locally optimal choice. Used in: Ch 15 (activity selection, Huffman codes, offline caching).

**Amortized Analysis:** Three methods: aggregate (total cost / n), accounting (banker's method, assign higher cost to cheap ops), potential (Phi(D_i) = prepaid work). Used in: Ch 16 (stack, counter, dynamic table).

**Augmentation:** Add extra fields to red-black tree nodes (size, max) to support new operations. Framework (Ch 17): (1) choose DS, (2) determine info, (3) verify maintainable, (4) develop new ops.

**Linear-Time Sorting:** Use key structure (not comparisons). Counting sort (range k), radix sort (d digits, stable sort per digit), bucket sort (uniform distribution). Ch 8.

**Fork-Join Parallelism (Ch 26):** spawn, sync, parallel keywords. Work = total ops (T_1), span = longest path (T_inf). Parallelism = T_1 / T_inf. Greedy scheduler: T_p <= T_1/p + T_inf.

**Online Algorithms (Ch 27):** Input arrives over time; must make irrevocable decisions. Competitive ratio: ALG <= alpha*OPT. Move-to-front is 2-competitive for search lists. LRU is k-competitive for caching.

**Reduction (Ch 34):** Transform instance of problem A to instance of problem B. Used for NP-completeness proofs (L' <=_P L). All reductions are polynomial-time.

**Approximation Algorithms (Ch 35):** For NP-hard problems, guarantee solution within factor rho of optimal. Vertex-cover: 2-approx. TSP (triangle inequality): 2-approx (MST), 1.5-approx (Christofides). Set-cover: O(ln n)-approx. Subset-sum: FPTAS.

### Proof & Argument Patterns

**Loop Invariants:** Initialization, Maintenance, Termination. Used for: INSERTION-SORT (Ch 2), PARTITION (Ch 7), BUILD-MAX-HEAP (Ch 6), HEAPSORT (Ch 6), RANDOMLY-PERMUTE (Ch 5).

**Mathematical Induction:** Base case + inductive step. Used for algorithm correctness proofs and recurrence solutions.

**Substitution Method (Ch 4):** Guess form of solution, prove by induction. Set up constants to satisfy base case and inductive step. Pitfall: O-notation on RHS loses constants. Fix: subtract lower-order term.

**Recursion-Tree Method (Ch 4):** Expand recurrence as tree, sum costs per level. Helps guess closed form for substitution proof.

**Master Theorem (Ch 4):** For T(n) = aT(n/b) + f(n). Three cases compare f(n) with n^(log_b a). Case 1: f(n) = O(n^(log_b a - epsilon)) => T(n) = Theta(n^(log_b a)). Case 2: f(n) = Theta(n^(log_b a) lg^k n) => T(n) = Theta(n^(log_b a) lg^(k+1) n). Case 3: f(n) = Omega(n^(log_b a + epsilon)) + regularity => T(n) = Theta(f(n)).

**Decision-Tree Lower Bound (Ch 8):** Any comparison sort requires Omega(n lg n) comparisons. Tree has n! leaves; height >= lg(n!) = Omega(n lg n).

**Median-of-Medians Guarantee (Ch 9):** Groups of 5 => pivot splits off at least 3g/2 elements => recursive subproblem <= 7n/10 => T(n) = T(n/5) + T(7n/10) + Theta(n) => Theta(n).

**Indicator Random Variables (Ch 5):** I{A} = 1 if A occurs, 0 otherwise. E[I{A}] = Pr{A}. Used with linearity of expectation for hire count, quicksort comparisons, birthday paradox, coupon collector.

**Exchange Argument (Ch 15):** Show that any optimal solution can be transformed to greedy solution without degrading quality. Used for activity selection, Huffman codes.

**Cut-and-Paste (Ch 14-16):** If subproblem solution is not optimal, can replace it with better one (cut it out, paste better in) => contradiction. Proves optimal substructure.

**Potential Method (Ch 16, 19):** Phi(D_0) = 0, Phi(D_i) >= 0. Amortized cost = actual cost + Delta(Phi). Used for dynamic tables, disjoint-set forests (inverse Ackermann bound).

**Relaxation (Ch 22, 23):** Relax edge (u,v): if v.d > u.d + w(u,v), update v.d = u.d + w(u,v). Repeated application converges to shortest-path distances.

**Max-Flow Min-Cut Theorem (Ch 24):** Three equivalent: f is max flow; residual network has no augmenting path; |f| = c(S,T) for some cut (S,T).

**Polynomial Reduction (Ch 34):** L_1 <=_P L_2: exists polynomial function f such that x in L_1 <=> f(x) in L_2. If L_2 in P then L_1 in P (contrapositive: if L_1 not in P then L_2 not in P). Transitive.

### People & Dates

| Person | Contribution | Chapter |
|--------|-------------|---------|
| C.A.R. Hoare | Quicksort (1962) | 7 |
| Robert Floyd | BUILD-MAX-HEAP, Floyd-Warshall | 6, 23 |
| J. Williams | Heapsort | 6 |
| Volker Strassen | Strassen's matrix multiplication (O(n^2.807)) | 4 |
| Akra & Bazzi | Akra-Bazzi recurrences | 4 |
| Ron Rivest, Adi Shamir, Len Adleman | RSA cryptosystem (1977) | 31 |
| R.E. Tarjan | Disjoint-set analysis, Augmented DS, SCC | 19, 20, 17 |
| John Hopcroft | B-trees, SCC algorithm | 18, 20 |
| Edsger Dijkstra | Dijkstra's shortest-path algorithm | 22 |
| Richard Bellman, Lester Ford | Bellman-Ford shortest paths | 22 |
| Robert W. Floyd | Floyd-Warshall all-pairs | 23 |
| Donald Knuth, Jim Morris, Vaughan Pratt | KMP string matching | 32 |
| Richard Karp | Karp's 21 NP-complete problems, Rabin-Karp | 32, 34 |
| Michael Rabin | Rabin-Karp, Miller-Rabin primality test | 31, 32 |
| Stephen Cook, Leonid Levin | Cook-Levin theorem: CIRCUIT-SAT is NP-complete | 34 |
| N. Christofides | 1.5-approximation for TSP | 35 |
| David Huffman | Huffman codes | 15 |
| Leslie Lamport | Parallel computing foundations | 26 |
| Harold Kuhn, James Munkres | Hungarian algorithm for assignment | 25 |
| D. Gale, L.S. Shapley | Stable-marriage problem (Gale-Shapley algorithm) | 25 |
| R. Bayer, E. McCreight | B-trees (1972) | 18 |
| H. Edelsbrunner, E.M. McCreight | Interval trees | 17 |
| Samuel, Tesauro (TD-Gammon) | Early ML success stories | 33 |
| L.J. Comrie | LSD radix sort (1929) | 8 |
| H.H. Seward | Counting sort (1954) | 8 |
| Blum, Floyd, Pratt, Rivest, Tarjan | Worst-case linear median (SELECT) | 9 |
| J.E. Hopcroft | 2-3 trees (B-tree precursor, 1970) | 18 |
| Bayer & McCreight | B-trees (1972) | 18 |
| Fredman & Tarjan | Fibonacci heaps | 16 |

### Mnemonics & Memory Aids

**Big-O Ordering (fastest to slowest):**
Theta(1) < Theta(lg n) < Theta(n) < Theta(n lg n) < Theta(n^2) < Theta(n^3) < Theta(2^n) < Theta(n!)
Mnemonic: "Oh Log No, N-Log-N Squared Cubed Exponential Factorial"

**Master Theorem Flowchart:**
1. Compute n^(log_b a) and compare to f(n)
2. If f(n) is polynomially smaller => Case 1: T(n) = Theta(n^(log_b a))
3. If f(n) ~ same size => Case 2: multiply by lg^(k+1) n
4. If f(n) is polynomially larger + regularity => Case 3: T(n) = Theta(f(n))
5. If none apply => Master Theorem doesn't apply (use Akra-Bazzi or substitution)

**Sorting Algorithm Quick Reference:**
| Algorithm | Worst | Avg | Best | Space | Stable | In-place |
|-----------|-------|-----|------|-------|--------|----------|
| Insertion | Theta(n^2) | Theta(n^2) | Theta(n) | O(1) | Yes | Yes |
| Merge | Theta(n lg n) | Theta(n lg n) | Theta(n lg n) | Theta(n) | Yes | No |
| Heap | Theta(n lg n) | Theta(n lg n) | Theta(n lg n) | O(1) | No | Yes |
| Quick | Theta(n^2) | Theta(n lg n) | Theta(n lg n) | O(lg n) | No | Yes |
| Counting | Theta(n+k) | Theta(n+k) | Theta(n+k) | Theta(k) | Yes | No |
| Radix | Theta(d(n+k)) | Theta(d(n+k)) | Theta(d(n+k)) | Theta(n+k) | Yes | No |

**Graph Algorithm Quick Reference:**
| Algorithm | Time | Problem |
|-----------|------|---------|
| BFS | O(V+E) | Shortest paths (unweighted) |
| DFS | O(V+E) | Topological sort, SCC |
| Kruskal | O(E lg V) | MST |
| Prim | O(E lg V) / O(E + V lg V) | MST |
| Bellman-Ford | O(VE) | Single-source (negative weights OK) |
| Dijkstra | O((V+E) lg V) | Single-source (nonnegative weights) |
| Floyd-Warshall | Theta(V^3) | All-pairs |
| Johnson | O(VE + V^2 lg V) | All-pairs (sparse) |
| Ford-Fulkerson | O(E|f*|) | Max flow |
| Edmonds-Karp | O(VE^2) | Max flow (BFS augmenting paths) |

**DP vs Greedy:** DP = subproblems overlap; Greedy = subproblems are independent + greedy choice property.

**NP-Completeness Reduction Chain:**
CIRCUIT-SAT -> SAT -> 3-CNF-SAT -> CLIQUE -> VERTEX-COVER -> HAM-CYCLE -> TSP -> SUBSET-SUM

---

## Exam Questions by Type

### MCQ

1. **Q:** What is the worst-case running time of quicksort?  **A:** Theta(n^2).  **Distractor:** Theta(n lg n) -- average-case.  **Distractor:** Theta(n) -- best-case for insertion sort.

2. **Q:** Which DS supports INSERT, EXTRACT-MAX, INCREASE-KEY in O(lg n)?  **A:** Max-heap.  **Distractor:** BST -- EXTRACT-MAX O(n).  **Distractor:** Hash table -- no EXTRACT-MAX.

3. **Q:** Master Theorem form?  **A:** T(n) = aT(n/b) + f(n), a>=1, b>1.  **Distractor:** T(n)=T(n-1)+f(n) -- linear.  **Distractor:** T(n)=aT(n-b)+f(n) -- not master.

4. **Q:** NOT NP-complete?  **A:** Shortest path (P).  **Distractor:** 3-CNF-SAT, VERTEX-COVER, HAM-CYCLE -- all NP-complete.

5. **Q:** Memoization?  **A:** Top-down storing subproblem results.  **Distractor:** Bottom-up -- tabular method.  **Distractor:** Avoids optimal substructure -- it requires it.

6. **Q:** Vertex-cover approximation ratio?  **A:** 2.  **Distractor:** 1 -- needs P=NP.  **Distractor:** O(ln n) -- set-cover.

7. **Q:** Floyd-Warshall paradigm?  **A:** DP (subproblems = paths via {1..k}).  **Distractor:** Greedy -- Dijkstra.  **Distractor:** D&C -- subproblems overlap.

8. **Q:** Dijkstra with negative weights?  **A:** May produce incorrect results.  **Distractor:** Works but slower -- wrong.  **Distractor:** Undefined -- runs but overestimates.

9. **Q:** Edmonds-Karp uses which augmenting path?  **A:** BFS, O(VE^2).  **Distractor:** DFS -- Ford-Fulkerson.  **Distractor:** O(E|f*|) -- generic bound.

10. **Q:** Greedy correctness requires?  **A:** Greedy-choice property + optimal substructure.  **Distractor:** Only overlapping subproblems -- DP.  **Distractor:** Only optimal substructure -- both needed.

### Short Answer

1. **Q:** State and prove the max-flow min-cut theorem.
   **Rubric:** (1) max flow = min cut capacity (1pt). (2) Three equivalent conditions (1pt). (3) Proof: |f|=c(S,T) => no augmenting path (1pt). (4) No augmenting path => define S as reachable, |f|=c(S,T) (1pt). (5) Thus max = min (1pt).

2. **Q:** Explain P, NP, NP-complete. What would P=NP imply?
   **Rubric:** (1) P = poly-time decidable (1pt). (2) NP = poly-time verifiable (1pt). (3) NPC = NP + every NP reduces to it (1pt). (4) P=NP => every verifiable problem solvable (1pt). (5) Collapses hierarchy, breaks crypto (1pt).

3. **Q:** Three amortized analysis methods; analyze dynamic table doubling.
   **Rubric:** (1) Aggregate: total/n (1pt). (2) Accounting: credit/debit (1pt). (3) Potential: Phi diff (1pt). (4) Total cost <= 3n (1pt). (5) Amortized = O(1) (1pt).

4. **Q:** D&C vs DP with examples.
   **Rubric:** (1) D&C: disjoint subproblems (1pt). (2) DP: overlapping (1pt). (3) D&C: merge sort (1pt). (4) DP: LCS (1pt). (5) Key: overlap (1pt).

5. **Q:** Bellman-Ford and negative cycles.
   **Rubric:** (1) |V|-1 relaxation passes (1pt). (2) Extra pass detects negative cycles (1pt). (3) Reports cycle, no distances if present (1pt). (4) O(VE) (1pt). (5) More general than Dijkstra (1pt).

### Trace / Apply

**T1:** INSERTION-SORT on A=[5,2,4,6,1,3]. Show array after each i iteration.
   **Expected:** i=2: [2,5,4,6,1,3]; i=3: [2,4,5,6,1,3]; i=4: [2,4,5,6,1,3]; i=5: [1,2,4,5,6,3]; i=6: [1,2,3,4,5,6].

**T2:** Bellman-Ford: V={s,a,b,c}, edges: (s,a,5), (s,b,3), (a,c,2), (b,a,1), (b,c,6), (c,b,2). Find shortest paths from s.
   **Expected:** 3 passes: s.d=0, a.d=4 (s->b->a), b.d=3 (s->b), c.d=6 (s->b->a->c). 4th pass: no changes.

**T3:** LCS of X=<A,B,C,B,D,A,B> and Y=<B,D,C,A,B,A> by DP table.
   **Expected:** length=4. LCS=<B,C,B,A> or <B,D,A,B>. c[7,6]=4.

### Essay / Long-Form

**E1:** Compare D&C and DP using merge sort, Strassen, matrix-chain, LCS. Explain why overlapping subproblems is the key distinction.
   **Points:** D&C disjoint; DP overlapping; both need optimal substructure; DP uses memoization/table.

**E2:** Max-flow min-cut theorem, Ford-Fulkerson, Edmonds-Karp advantage (O(VE^2) vs O(E|f*|)), applications (matching, connectivity).
   **Points:** Three equivalences; residual; augmenting path; integrality; BFS monotonic delta; applications.

**E3:** P vs NP, polynomial reduction, reduction chain CIRCUIT-SAT to VERTEX-COVER. Why NP-completeness guides algorithm design.
   **Points:** P poly-time; NP verifiable; reduction f poly x in L1 <=> f(x) in L2; each reduction construction + two-direction proof; seek approximations/heuristics.
