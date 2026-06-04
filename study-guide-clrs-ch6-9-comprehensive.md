# Study Guide: Introduction to Algorithms (CLRS 4e) — Part II: Sorting and Order Statistics

> Generated 2026-06-04. Subject: Computer Science (Algorithms). Exam format: Mixed (MCQ / short answer / problem-solving). Coverage: Comprehensive — Chapters 6–9.

## Chapter-by-Chapter Breakdown

---

## Ch. 6 — Heapsort

### Named Entities (Terms & Definitions)

- **Heap**: A data structure that is an array object viewed as a nearly complete binary tree. Completely filled on all levels except possibly the lowest, which is filled from left to right.
- **Binary heap**: The standard heap implementation; supports max-heaps and min-heaps.
- **Max-heap**: A binary heap satisfying the max-heap property: for every node i other than the root, `A[PARENT(i)] ≥ A[i]`. The largest element is at the root.
- **Min-heap**: A binary heap satisfying the min-heap property: for every node i other than the root, `A[PARENT(i)] ≤ A[i]`. The smallest element is at the root.
- **Max-heap property**: The value of a node is at most the value of its parent.
- **Min-heap property**: The value of a node is at least the value of its parent.
- **Height of a node in a heap**: The number of edges on the longest simple downward path from the node to a leaf.
- **Height of the heap**: The height of its root (Θ(lg n) for an n-element heap).
- **Heap size**: Attribute `A.heap-size` — how many elements in the heap are stored within array A. `0 ≤ A.heap-size ≤ n`.
- **Priority queue**: A data structure for maintaining a set S of elements, each with an associated value called a key.
- **Max-priority queue**: Supports INSERT, MAXIMUM, EXTRACT-MAX, INCREASE-KEY.
- **Min-priority queue**: Supports INSERT, MINIMUM, EXTRACT-MIN, DECREASE-KEY.
- **Handles**: Additional information stored in objects and heap elements to map between application objects and array indices.
- **d-ary heap**: A generalization where nonleaf nodes have d children instead of two.
- **Young tableau**: An m × n matrix with rows sorted left-to-right and columns sorted top-to-bottom.
- **Strict Fibonacci heaps**: Support INSERT and DECREASE-KEY in O(1) worst-case time.
- **Fibonacci heaps**: Support INSERT and DECREASE-KEY in O(1) amortized time.
- **Radix heap**: A data structure for monotone priority queues with integer keys in range 1..C, supporting EXTRACT-MIN and INSERT in O(lg C) amortized time and DECREASE-KEY in O(1) time.

### Processes / Algorithms

#### PARENT, LEFT, RIGHT
- **Goal**: Compute parent, left child, and right child indices in a heap represented as an array.
- **Steps**:
  1. `PARENT(i)`: return ⌊i/2⌋
  2. `LEFT(i)`: return 2i
  3. `RIGHT(i)`: return 2i + 1
- **Implementation**: Can be implemented as macros or inline procedures. LEFT = shift left by 1 bit. RIGHT = shift left by 1 bit and add 1. PARENT = shift right by 1 bit.

#### MAX-HEAPIFY (A, i)
- **Type**: Algorithm — key subroutine for maintaining the max-heap property.
- **Goal**: Maintain the max-heap property. Assumes binary trees rooted at LEFT(i) and RIGHT(i) are max-heaps, but A[i] might be smaller than its children.
- **Input**: Array A (with heap-size attribute), index i.
- **Output**: Subtree rooted at i obeys max-heap property.
- **Steps**:
  1. `l = LEFT(i)`
  2. `r = RIGHT(i)`
  3. If `l ≤ A.heap-size` and `A[l] > A[i]`: `largest = l`
  4. Else: `largest = i`
  5. If `r ≤ A.heap-size` and `A[r] > A[largest]`: `largest = r`
  6. If `largest ≠ i`: exchange `A[i]` with `A[largest]`, then recursively call `MAX-HEAPIFY(A, largest)`
- **Complexity**: O(lg n) time. Recurrence: T(n) ≤ T(2n/3) + O(1). By case 2 of the master theorem, T(n) = O(lg n). Alternatively, O(h) where h is the height of the node.
- **Key insight**: Children's subtrees each have size at most 2n/3 (worst case when the last level is half-full).
- **Edge case**: If A[i] is larger than both children, no work is done (it is already a max-heap).
- **Edge case**: If i > A.heap-size/2, the node is a leaf, and MAX-HEAPIFY does nothing (it's already a max-heap).

#### BUILD-MAX-HEAP (A, n)
- **Type**: Algorithm — builds a max-heap from an unordered array.
- **Goal**: Convert array A[1:n] into a max-heap.
- **Input**: Unordered array A, size n.
- **Output**: Max-heap in A[1:n].
- **Steps**:
  1. `A.heap-size = n`
  2. For `i = ⌊n/2⌋` down to 1:
     - Call `MAX-HEAPIFY(A, i)`
- **Loop invariant**: At the start of each iteration of the for loop, each node i+1, i+2, ..., n is the root of a max-heap.
  - **Initialization**: Prior to first iteration, i = ⌊n/2⌋. Nodes ⌊n/2⌋+1...n are leaves, hence roots of trivial max-heaps.
  - **Maintenance**: Children of node i are numbered higher than i. By the invariant, both are roots of max-heaps. MAX-HEAPIFY makes node i a max-heap root.
  - **Termination**: i = 0. Each node 1...n is the root of a max-heap, particularly node 1.
- **Complexity**: O(n) tight bound (not O(n lg n)). Proof: there are at most ⌈n/2^(h+1)⌉ nodes of height h, each MAX-HEAPIFY at height h costs O(h). Sum over all nodes gives linear total.
- **To build a min-heap**: Use BUILD-MIN-HEAP, same algorithm but calls MIN-HEAPIFY.

#### HEAPSORT (A, n)
- **Type**: Sorting algorithm.
- **Goal**: Sort array A[1:n] in place in O(n lg n) time.
- **Input**: Array A[1:n].
- **Output**: Sorted array A[1:n] (increasing order).
- **Steps**:
  1. `BUILD-MAX-HEAP(A, n)`
  2. For `i = n` down to 2:
     - Exchange `A[1]` with `A[i]`
     - `A.heap-size = A.heap-size - 1`
     - `MAX-HEAPIFY(A, 1)`
- **Complexity**: O(n lg n). BUILD-MAX-HEAP takes O(n). n-1 calls to MAX-HEAPIFY each O(lg n).
- **Loop invariant**: At start of each iteration of the for loop (lines 2-5), subarray A[1:i] is a max-heap containing the i smallest elements of A[1:n], and subarray A[i+1:n] contains the n-i largest elements of A[1:n], sorted.
- **Best-case running time**: Ω(n lg n) when all elements are distinct.
- **Worst-case running time**: Ω(n lg n).

#### MAX-HEAP-MAXIMUM (A)
- **Type**: Priority queue operation.
- **Steps**:
  1. If `A.heap-size < 1`: error "heap underflow"
  2. Return `A[1]`
- **Complexity**: Θ(1)

#### MAX-HEAP-EXTRACT-MAX (A)
- **Type**: Priority queue operation.
- **Steps**:
  1. `max = MAX-HEAP-MAXIMUM(A)`
  2. `A[1] = A[A.heap-size]`
  3. `A.heap-size = A.heap-size - 1`
  4. `MAX-HEAPIFY(A, 1)`
  5. Return `max`
- **Complexity**: O(lg n)

#### MAX-HEAP-INCREASE-KEY (A, x, k)
- **Type**: Priority queue operation.
- **Goal**: Increase the key of object x to new value k (assumed ≥ current key).
- **Steps**:
  1. If `k < x.key`: error "new key is smaller than current key"
  2. `x.key = k`
  3. Find the index i in array A where object x occurs
  4. While `i > 1` and `A[PARENT(i)].key < A[i].key`:
     - Exchange `A[i]` with `A[PARENT(i)]`, updating mapping info
     - `i = PARENT(i)`
- **Complexity**: O(lg n)
- **Loop invariant**: At start of each iteration of the while loop:
  - (a) If both PARENT(i) and LEFT(i) exist: `A[PARENT(i)].key ≥ A[LEFT(i)].key`
  - (b) If both PARENT(i) and RIGHT(i) exist: `A[PARENT(i)].key ≥ A[RIGHT(i)].key`
  - (c) The subarray A[1:A.heap-size] satisfies the max-heap property, except that `A[i].key` may be greater than `A[PARENT(i)].key`.

#### MAX-HEAP-INSERT (A, x, n)
- **Type**: Priority queue operation.
- **Goal**: Insert new object x into max-heap A.
- **Steps**:
  1. If `A.heap-size == n`: error "heap overflow"
  2. `A.heap-size = A.heap-size + 1`
  3. `k = x.key`
  4. `x.key = -∞`
  5. `A[A.heap-size] = x`
  6. Map x to index heap-size in the array
  7. `MAX-HEAP-INCREASE-KEY(A, x, k)`
- **Complexity**: O(lg n)
- **Note**: The key is temporarily set to -∞, then INCREASE-KEY sets it to the real value, bubbling it up.

### Min-Priority Queue Operations (details from exercises)
- **MIN-HEAP-MINIMUM**: Returns A[1] — Θ(1)
- **MIN-HEAP-EXTRACT-MIN**: Extract A[1], replace with last element, call MIN-HEAPIFY — O(lg n)
- **MIN-HEAP-DECREASE-KEY**: Set key to smaller value, bubble up — O(lg n)
- **MIN-HEAP-INSERT**: Add element with key +∞, then DECREASE-KEY to desired value — O(lg n)

### Formulas & Equations

- **Height of n-element heap**: ⌊lg n⌋
- **Leaf indices in heap array**: ⌊n/2⌋ + 1, ⌊n/2⌋ + 2, …, n
- **MAX-HEAPIFY recurrence**: T(n) ≤ T(2n/3) + O(1), solved T(n) = O(lg n)
- **BUILD-MAX-HEAP total cost**: ∑_{h=0}^{⌊lg n⌋} ⌈n/2^(h+1)⌉ · O(h) = O(n)
- **Max nodes of height h**: ⌈n/2^(h+1)⌉
- **HEAPSORT complexity**: O(n lg n) (BUILD-MAX-HEAP O(n) + n-1 MAX-HEAPIFY calls each O(lg n))
- **d-ary heap height**: Θ(log_d n)

### Data Structures

#### Max-heap (as array)
- **Representation**: Array A[1:n] with attribute A.heap-size (≤ n).
- **Root**: A[1].
- **Parent/child indexing**: PARENT(i)=⌊i/2⌋, LEFT(i)=2i, RIGHT(i)=2i+1.
- **Property**: A[PARENT(i)] ≥ A[i] for all i ≠ root.
- **Operations**:
  | Operation | Time |
  |-----------|------|
  | MAX-HEAPIFY | O(lg n) |
  | BUILD-MAX-HEAP | O(n) |
  | HEAPSORT | O(n lg n) |
  | MAXIMUM | Θ(1) |
  | EXTRACT-MAX | O(lg n) |
  | INCREASE-KEY | O(lg n) |
  | INSERT | O(lg n) |

#### Min-heap
- **Property**: A[PARENT(i)] ≤ A[i] for all i ≠ root.
- Same structure as max-heap but with reversed comparisons.
- Used for min-priority queues.

### Comparisons & Trade-offs

| Dimension | Heapsort | Merge sort | Quicksort |
|-----------|----------|------------|-----------|
| Worst-case | O(n lg n) | O(n lg n) | Θ(n²) |
| Expected | O(n lg n) | O(n lg n) | Θ(n lg n) |
| In-place | Yes | No | Yes |
| Stable | No | Yes | No (Lomuto) |
| Constant factors | Moderate | Higher | Small |
| Practical speed | Slower than quicksort | Slower than quicksort | Fastest in practice |
| Asymptotically optimal? | Yes | Yes | No (worst-case) |

### Edge Cases & Pitfalls

- **Heap vs garbage-collected storage**: The term "heap" in this context refers to the data structure, not garbage-collected memory.
- **Heap overflow/underflow**: Priority queue operations must check bounds.
- **Already sorted array**: Heapsort still takes Ω(n lg n) even on sorted input.
- **Distinct vs non-distinct**: Analysis assumes distinct elements; handling duplicates requires care.
- **Heapify on leaf**: Calling MAX-HEAPIFY on a leaf (i > heap-size/2) does nothing.

### End-of-Chapter Material

**Key terms**: heap, max-heap, min-heap, max-heap property, min-heap property, height (of heap node), priority queue, max-priority queue, min-priority queue, key, handle.

**Key results**:
- A heap of n elements has height ⌊lg n⌋.
- Leaves in a heap array are at indices ⌊n/2⌋+1 through n.
- BUILD-MAX-HEAP runs in O(n) time.
- HEAPSORT sorts in place in O(n lg n) time.
- All priority queue operations run in O(lg n) time.
- Heapsort is asymptotically optimal among comparison sorts.

**Representative exercises**:
- 6.1-1: Min/max elements in heap of height h: min = 2^h, max = 2^(h+1) - 1.
- 6.1-2: n-element heap has height ⌊lg n⌋.
- 6.1-3: Root of any subtree contains the largest value in that subtree.
- 6.1-4: Smallest element in a max-heap is in a leaf.
- 6.2-2: Each child subtree size ≤ 2n/3. α = 2/3.
- 6.4-3: HEAPSORT on sorted array still takes Ω(n lg n).
- 6.5-9: Implement FIFO queue using priority queue (use increasing/decreasing keys as timestamps).
- 6.5-11: Merge k sorted lists in O(n lg k) using min-heap for k-way merging.

---

## Ch. 7 — Quicksort

### Named Entities (Terms & Definitions)

- **Quicksort**: A divide-and-conquer sorting algorithm that partitions an array around a pivot, recursively sorts each side. Worst-case Θ(n²), expected Θ(n lg n). Sorts in place.
- **Pivot**: The element around which the array is partitioned.
- **Low side**: Elements ≤ pivot (subarray A[p:q-1]).
- **High side**: Elements ≥ pivot (subarray A[q+1:r]).
- **Lomuto partition**: The PARTITION procedure in Section 7.1 (uses A[r] as pivot, attributed to N. Lomuto).
- **Hoare partition**: The original partition scheme by C.A.R. Hoare (uses A[p] as pivot, two pointers i and j moving from ends).
- **Randomized quicksort**: Quicksort where the pivot is chosen uniformly at random from the subarray, eliminating worst-case input dependence.
- **Tail-recursion elimination**: A compiler transformation that converts the second recursive call into a loop, reducing stack depth.
- **Median-of-3 method**: Improvement that chooses the pivot as the median of three randomly selected elements from the subarray.
- **Stooge sort**: A deceptively simple but very inefficient sorting algorithm (Θ(n^(lg 3 / lg 1.5)) ≈ Θ(n^2.71)).
- **Indicator random variable**: A random variable that is 1 if an event occurs, 0 otherwise. Used in quicksort expected time analysis.

### Processes / Algorithms

#### QUICKSORT (A, p, r)
- **Type**: Algorithm — divide-and-conquer sorting.
- **Goal**: Sort subarray A[p:r] in place.
- **Input**: Array A, indices p, r (p ≤ r).
- **Output**: Sorted subarray A[p:r].
- **Steps**:
  1. If `p < r`:
     - `q = PARTITION(A, p, r)`  // pivot ends up in A[q]
     - `QUICKSORT(A, p, q-1)`   // recursively sort low side
     - `QUICKSORT(A, q+1, r)`   // recursively sort high side
- **Divide**: Partition into low side (≤ pivot) and high side (≥ pivot).
- **Conquer**: Recursively sort both sides.
- **Combine**: Nothing to do — array is sorted after recursive calls.

#### PARTITION (A, p, r) — Lomuto partition
- **Type**: Algorithm — key subroutine of quicksort.
- **Goal**: Partition subarray A[p:r] around pivot A[r] (the last element). Returns the new index of the pivot.
- **Input**: Array A, indices p, r.
- **Output**: Index q such that A[p:q-1] ≤ A[q] and A[q+1:r] ≥ A[q].
- **Steps**:
  1. `x = A[r]`  // the pivot
  2. `i = p - 1`  // highest index into the low side
  3. For `j = p` to `r-1`:  // process each element other than pivot
     - If `A[j] ≤ x`:
       - `i = i + 1`
       - Exchange `A[i]` with `A[j]`
  4. Exchange `A[i+1]` with `A[r]`  // pivot goes just to the right of the low side
  5. Return `i + 1`  // new index of the pivot
- **Complexity**: Θ(n) where n = r-p+1.
- **Loop invariant**: At start of each iteration of the for loop (lines 3-6), for any array index k:
  1. If p ≤ k ≤ i: A[k] ≤ x (low side)
  2. If i+1 ≤ k ≤ j-1: A[k] > x (high side)
  3. If k = r: A[k] = x (pivot)
- **Initialization**: i = p-1, j = p. No elements between p and i, none between i+1 and j-1 — trivially satisfied.
- **Maintenance**: If A[j] > x, just increment j. If A[j] ≤ x, increment i, swap A[i] and A[j], increment j.
- **Termination**: j = r. Loop makes r-p iterations. Every element belongs to one of the three sets.

#### RANDOMIZED-PARTITION (A, p, r)
- **Type**: Algorithm — randomized version of PARTITION.
- **Goal**: Choose pivot uniformly at random, then partition.
- **Steps**:
  1. `i = RANDOM(p, r)`
  2. Exchange `A[r]` with `A[i]`
  3. Return `PARTITION(A, p, r)`

#### RANDOMIZED-QUICKSORT (A, p, r)
- **Type**: Randomized algorithm.
- **Goal**: Sort with expected Θ(n lg n) time regardless of input.
- **Steps**:
  1. If `p < r`:
     - `q = RANDOMIZED-PARTITION(A, p, r)`
     - `RANDOMIZED-QUICKSORT(A, p, q-1)`
     - `RANDOMIZED-QUICKSORT(A, q+1, r)`

#### HOARE-PARTITION (A, p, r) — Original partition by C.A.R. Hoare
- **Type**: Algorithm — alternative partitioning scheme.
- **Goal**: Partition using A[p] as pivot. Returns index j where p ≤ j < r.
- **Steps**:
  1. `x = A[p]`
  2. `i = p - 1`
  3. `j = r + 1`
  4. While TRUE:
     - Repeat `j = j - 1` until `A[j] ≤ x`
     - Repeat `i = i + 1` until `A[i] ≥ x`
     - If `i < j`: exchange `A[i]` with `A[j]`
     - Else return `j`
- **Properties**: 
  - Uses A[p] as pivot (not A[r]).
  - Always places pivot into one of the two partitions (neither partition is empty).
  - Every element of A[p:j] ≤ every element of A[j+1:r].
  - More efficient in practice when elements are equal.

### Formulas & Equations

#### Worst-case recurrence (unbalanced partition at every level)
- T(n) = T(n-1) + T(0) + Θ(n) = T(n-1) + Θ(n)
- **Solution**: Θ(n²) — arithmetic series.

#### Best-case recurrence (perfectly balanced partition at every level)
- T(n) = 2T(n/2) + Θ(n)
- **Solution**: Θ(n lg n) — by case 2 of master theorem.

#### Balanced partition (constant proportion α:β where α+β=1)
- T(n) = T(αn) + T(βn) + Θ(n)
- **Solution**: O(n lg n) regardless of constant proportion.
- Recursion tree depth: Θ(lg n). Cost per level: O(n).

#### Expected running time (RANDOMIZED-QUICKSORT)
- T(n) = O(n lg n) when elements are distinct.
- Formal proof uses indicator random variables:
  - Let z₁ < z₂ < ... < zₙ be elements in sorted order.
  - X = total number of element comparisons.
  - Xij = I{zi is compared with zj}.
  - E[X] = Σ_{i=1}^{n-1} Σ_{j=i+1}^{n} 2/(j-i+1)
  - = Σ_{i=1}^{n-1} Σ_{k=1}^{n-i} 2/(k+1)
  - < Σ_{i=1}^{n-1} 2·H_{n-i+1}
  - = O(n lg n)

#### Key probability in analysis (Lemma 7.3)
- Pr{zi is compared with zj} = 2/(j-i+1), for i < j.
- **Why**: Elements are compared iff one is chosen as pivot before any other element in Zij = {zi, ..., zj}. Since the first pivot from Zij is equally likely to be any of its j-i+1 elements, probability = 1/(j-i+1) + 1/(j-i+1) = 2/(j-i+1).

#### Lemma 7.1
- The running time of QUICKSORT on an n-element array is O(n + X), where X is the number of element comparisons performed.
- **Proof**: At most n calls to PARTITION. Each call takes O(1) + time proportional to number of comparisons in the for loop.

#### Lemma 7.2
- During execution of RANDOMIZED-QUICKSORT on distinct elements z₁ < z₂ < ... < zₙ, zi is compared with zj (i < j) if and only if one of them is chosen as a pivot before any other element in Zij. No two elements are ever compared twice.

### Comparisons & Trade-offs

| Dimension | Quicksort | Merge sort | Heapsort |
|-----------|-----------|------------|----------|
| Worst-case | Θ(n²) | Θ(n lg n) | Θ(n lg n) |
| Expected | Θ(n lg n) | Θ(n lg n) | Θ(n lg n) |
| In-place | Yes | No | Yes |
| Stable | No (Lomuto) | Yes | No |
| Space (stack) | Θ(n) worst, Θ(lg n) expected | Θ(n) | O(1) |
| Cache performance | Excellent | Poor for large n | Moderate |
| Practical speed | Fastest in practice | Slower | Slower |
| Asymptotically optimal? | No | Yes | Yes |

### Edge Cases & Pitfalls

- **Already sorted array (increasing order)**: Lomuto PARTITION always picks the last element as pivot, producing subproblems of size n-1 and 0 at every level. Θ(n²) running time.
- **Already sorted array (decreasing order)**: Same worst-case Θ(n²).
- **All elements equal**: Lomuto PARTITION returns q = r (all elements ≤ pivot). Produces worst-case behavior. Hoare partition handles this better.
- **Stack depth**: Worst-case recursion depth is Θ(n). Can be reduced to Θ(lg n) by tail-recursion elimination and always recursing on the smaller partition first.
- **Memory**: Not in-place by the strictest definition because recursion stack uses O(n) space in worst case.
- **Distinct element assumption**: Analysis requires distinct elements. Can enforce this by converting each A[i] to ordered pair (A[i], i) at cost Θ(n).

### End-of-Chapter Material

**Key terms**: quicksort, pivot, partition, low side, high side, randomized algorithm, tail recursion, median-of-3, indicator random variable.

**Key results**:
- The expected running time of RANDOMIZED-QUICKSORT is Θ(n lg n) for distinct elements.
- The worst-case running time is Θ(n²).
- Any split of constant proportionality yields O(n lg n) time.
- RANDOMIZED-PARTITION eliminates the dependence on input order.

**Theorems**:
- **Theorem 7.4**: The expected running time of RANDOMIZED-QUICKSORT on distinct elements is O(n lg n).

**Representative exercises**:
- 7.1-2: When all elements are equal, PARTITION returns q = r. Modify to return q = ⌊(p+r)/2⌋.
- 7.2-1: T(n) = T(n-1) + Θ(n) has solution Θ(n²) by substitution.
- 7.2-4: Insertion sort beats quicksort on almost-sorted input.
- 7.2-6: About 80% of the time, PARTITION produces a split at least as balanced as 9-to-1.
- 7.4-5: Coarsening (small subarrays use insertion sort) improves practical running time: O(nk + n lg(n/k)). Optimal k depends on implementation.
- 7-1: Hoare partition uses A[p] as pivot, two pointers i, j from opposite ends. Returns j where p ≤ j < r.
- 7-5: Tail-recursion elimination can reduce worst-case stack depth to Θ(lg n) by recursing on the smaller partition first.

---

## Ch. 8 — Sorting in Linear Time

### Named Entities (Terms & Definitions)

- **Comparison sort**: A sorting algorithm that determines order only by comparing elements (e.g., insertion sort, merge sort, heapsort, quicksort).
- **Decision tree**: A full binary tree representing comparisons performed by a comparison sort on an input of a given size. Each internal node is annotated i:j (compare ai vs aj). Each leaf is a permutation.
- **Ω(n lg n) lower bound**: Any comparison sort requires Ω(n lg n) comparisons in the worst case.
- **Counting sort**: A non-comparison sort that works when input elements are integers in range 0..k. Runs in Θ(n+k) time. Stable.
- **Radix sort**: A non-comparison sort that sorts digit by digit from least significant to most significant, requiring a stable sort for each digit.
- **Bucket sort**: A non-comparison sort that assumes uniform distribution over [0,1). Distributes elements into n buckets, sorts each with insertion sort.
- **Stable sort**: A sorting algorithm that preserves the relative order of elements with equal keys.
- **0-1 sorting lemma**: If an oblivious compare-exchange algorithm correctly sorts all inputs of 0s and 1s, then it correctly sorts all inputs with arbitrary values.
- **Oblivious compare-exchange algorithm**: An algorithm that operates by a prespecified sequence of compare-exchange operations; indices cannot depend on values or prior results.
- **Columnsort**: An oblivious compare-exchange algorithm for sorting rectangular arrays in 8 steps.
- **k-sorted array**: An array where A[i] ≤ A[i+k] for all i = 1, ..., n-k.
- **Fusion tree**: A data structure for sorting n integers in O(n lg n / lg lg n) time.

### Processes / Algorithms

#### Decision tree model
- Each internal node is a comparison i:j (compare ai ≤ aj).
- Left subtree: what happens if ai ≤ aj.
- Right subtree: what happens if ai > aj.
- Each leaf is a permutation ⟨π(1), ..., π(n)⟩.
- Height of decision tree = worst-case number of comparisons.
- Every permutation must appear as at least one reachable leaf.
- Number of leaves ≤ 2^h (for height h).

#### COUNTING-SORT (A, n, k)
- **Type**: Non-comparison sorting algorithm.
- **Goal**: Sort array A[1:n] where each element is an integer in [0, k].
- **Input**: Array A, size n, key range 0..k.
- **Output**: Sorted array B[1:n].
- **Steps**:
  1. Let B[1:n] and C[0:k] be new arrays
  2. For i = 0 to k: `C[i] = 0`
  3. For j = 1 to n: `C[A[j]] = C[A[j]] + 1`  // C[i] = count of elements equal to i
  4. For i = 1 to k: `C[i] = C[i] + C[i-1]`  // C[i] = count of elements ≤ i
  5. For j = n down to 1:
     - `B[C[A[j]]] = A[j]`
     - `C[A[j]] = C[A[j]] - 1`  // handle duplicates
  6. Return B
- **Complexity**: Θ(n + k). When k = O(n), runs in Θ(n) time.
- **Stability**: Stable — elements with the same value appear in the output in the same order as input.
- **Why it beats Ω(n lg n) bound**: Not a comparison sort. Uses actual values to index into an array.
- **Key detail**: Processing the input in reverse (line 11) is crucial for stability. Processing forward produces correct output but is not stable.
- **Loop invariant** (lines 11-13): At the start of each iteration, the last element in A with value i that has not yet been copied into B belongs in B[C[i]].

#### RADIX-SORT (A, n, d)
- **Type**: Non-comparison sorting algorithm.
- **Goal**: Sort n d-digit numbers.
- **Input**: Array A[1:n] with elements having d digits (digit 1 = least significant, digit d = most significant).
- **Steps**:
  1. For i = 1 to d:
     - Use a stable sort to sort array A on digit i
- **Complexity (Lemma 8.3)**: Θ(d(n + k)) if the stable sort takes Θ(n + k) time. With counting sort: Θ(d(n + k)).
- **Correctness**: By induction on the column being sorted (Exercise 8.3-3). Requires that the intermediate sort is stable.
- **Optimization (Lemma 8.4)**: For n b-bit numbers and r ≤ b:
  - View each key as d = ⌈b/r⌉ digits of r bits each.
  - Each digit in [0, 2^r - 1].
  - Running time: Θ((b/r)(n + 2^r)).
  - If b < ⌊lg n⌋: choose r = b, runtime = Θ(n).
  - If b ≥ ⌊lg n⌋: choose r = ⌊lg n⌋, runtime = Θ(bn/lg n).

#### BUCKET-SORT (A, n)
- **Type**: Non-comparison sorting algorithm.
- **Goal**: Sort n numbers uniformly distributed in [0, 1).
- **Input**: Array A[1:n] with 0 ≤ A[i] < 1.
- **Steps**:
  1. Let B[0:n-1] be a new array of empty lists
  2. For i = 1 to n:
     - Insert A[i] into list B[⌊n · A[i]⌋]
  3. For i = 0 to n-1:
     - Sort list B[i] with insertion sort
  4. Concatenate lists B[0], B[1], ..., B[n-1] together in order
  5. Return the concatenated lists
- **Complexity**: 
  - All lines except insertion sort: O(n)
  - Insertion sort: let ni be number of elements in bucket i. Total = ∑ O(ni²).
  - Expected: E[ni²] = 2 - 1/n, so E[total] = Θ(n) + n·O(2-1/n) = Θ(n).
  - Worst-case: Θ(n²) (when all elements go into one bucket).
- **Probability model**: Input uniformly distributed over [0,1). Each ni ∼ Binomial(n, 1/n). E[ni] = 1, Var[ni] = 1 - 1/n.
- **Improvement**: Replace insertion sort with O(n lg n) sort (e.g., merge sort) to make worst-case O(n lg n) while keeping average O(n).

### Formulas & Equations

#### Lower bound for comparison sorting
- n! ≤ l ≤ 2^h, where l = number of leaves, h = height of decision tree.
- h ≥ lg(n!) = Ω(n lg n).
- Using Stirling's approximation: lg(n!) = n lg n - n lg e + Θ(lg n).

**Theorem 8.1**: Any comparison sort requires Ω(n lg n) comparisons in the worst case.
**Corollary 8.2**: Heapsort and merge sort are asymptotically optimal comparison sorts.

#### Radix sort complexity
- **Lemma 8.3**: Θ(d(n + k)) time.
- **Lemma 8.4**: Θ((b/r)(n + 2^r)) time.
- Optimal r: if b < ⌊lg n⌋, r = b; if b ≥ ⌊lg n⌋, r = ⌊lg n⌋.

#### Bucket sort expected time
- E[total time] = Θ(n) + ∑_{i=0}^{n-1} O(E[ni²]) = Θ(n) + n·O(2-1/n) = Θ(n)
- E[ni] = 1, Var[ni] = 1 - 1/n, E[ni²] = 2 - 1/n

### Comparisons & Trade-offs

| Dimension | Counting sort | Radix sort | Bucket sort |
|-----------|---------------|------------|-------------|
| Input assumption | Integers in [0,k] | d-digit numbers (or b-bit) | Uniform [0,1) |
| Running time | Θ(n+k) | Θ(d(n+k)) or Θ((b/r)(n+2^r)) | Θ(n) expected |
| Worst-case | Θ(n+k) | Θ(d(n+k)) | Θ(n²) |
| In-place | No | No | No |
| Stable | Yes | Depends on digit sort | Depends on bucket sort |
| Space | Θ(k) out-place | Θ(n+k) per pass | Θ(n) |
| Practical use | Small k | b-bit keys, fast stable sort needed | Data known uniform |

**Radix sort vs quicksort**:
- If b = O(lg n) and r ≈ lg n, radix sort gives Θ(n) vs quicksort's Θ(n lg n).
- However, radix sort's constant factors are larger.
- Radix sort does not sort in place.
- Quicksort uses hardware caches more effectively.
- Choice depends on implementation, machine, and data characteristics.

**Stability of sorting algorithms**:
- Insertion sort: Stable
- Merge sort: Stable
- Heapsort: Not stable
- Quicksort (Lomuto): Not stable
- Counting sort: Stable
- Radix sort (with counting sort): Stable
- Making any comparison sort stable: Store original index as part of the key — costs O(n) additional space and some time.

### Proof & Argument Patterns

#### Lower bound proof (Theorem 8.1)
1. Model comparison sort as decision tree.
2. Each permutation must appear as at least one reachable leaf → n! ≤ l.
3. Binary tree of height h has at most 2^h leaves → l ≤ 2^h.
4. Therefore: n! ≤ 2^h → h ≥ lg(n!) = Ω(n lg n).
5. Stirling's approximation: n! = √(2πn)(n/e)^n(1+Θ(1/n)) → lg(n!) = n lg n - n lg e + Θ(lg n).

#### 0-1 Sorting Lemma
- If an oblivious compare-exchange algorithm correctly sorts all 0-1 inputs, then it correctly sorts all inputs with arbitrary values.
- Proof by contrapositive: if algorithm fails to sort some arbitrary input, it fails to sort some 0-1 input.
- Let A[p] be the smallest value in wrong location, A[q] the value that should be there. Set B[p] = 0, B[q] = 1.

### Edge Cases & Pitfalls

- **Counting sort**: Must handle k = O(n) to achieve linear time. Range must be small integers.
- **Counting sort without stability**: Processing forward (j = 1 to n) produces correct output but is not stable — important for radix sort.
- **Radix sort digit passes**: Must sort from least significant digit (LSD) first. Sorting MSD first creates many piles to manage.
- **Radix sort stability requirement**: Each digit sort must be stable for correctness.
- **Bucket sort worst-case**: If all elements fall into one bucket, time is Θ(n²).
- **Bucket sort non-uniform input**: Still linear as long as sum of squares of bucket sizes is O(n).
- **Comparison sort vs non-comparison**: Ω(n lg n) lower bound applies only to comparison sorts.

### End-of-Chapter Material

**Key terms**: comparison sort, decision tree, counting sort, stable sort, radix sort, bucket sort, 0-1 sorting lemma, oblivious compare-exchange algorithm.

**Key results**:
- **Theorem 8.1**: Any comparison sort requires Ω(n lg n) comparisons.
- **Corollary 8.2**: Heapsort and merge sort are asymptotically optimal.
- **Lemma 8.3**: Radix sort runs in Θ(d(n+k)).
- **Lemma 8.4**: Radix sort on b-bit numbers runs in Θ((b/r)(n+2^r)).
- Counting sort runs in Θ(n+k) time, Θ(n) when k = O(n).
- Bucket sort expected running time is Θ(n) for uniform input.
- Radix sort and bucket sort are not subject to the Ω(n lg n) lower bound because they use operations other than comparisons.

**Representative exercises**:
- 8.1-1: Smallest possible depth of a leaf in a decision tree is n-1 (for comparision sort).
- 8.2-3: Forward iteration in counting sort produces correct output but loses stability.
- 8.3-5: Sort n integers in range 0 to n³-1 in O(n) time using radix sort with base n.
- 8.4-2: Worst-case of bucket sort is Θ(n²); replace insertion sort with O(n lg n) sort to get O(n lg n) worst-case.

---

## Ch. 9 — Medians and Order Statistics

### Named Entities (Terms & Definitions)

- **Order statistic**: The i-th smallest element of a set of n elements.
- **Minimum**: The first order statistic (i = 1).
- **Maximum**: The n-th order statistic (i = n).
- **Median**: The "halfway point." Lower median at i = ⌊(n+1)/2⌋, upper median at i = ⌈(n+1)/2⌉. For odd n, median is unique at i = (n+1)/2.
- **Selection problem**: Given a set A of n distinct numbers and an integer i (1 ≤ i ≤ n), find the element x ∈ A that is larger than exactly i-1 other elements.
- **Randomized selection (RANDOMIZED-SELECT)**: A randomized divide-and-conquer algorithm for selection, modeled after quicksort. Expected Θ(n) time.
- **Deterministic selection (SELECT)**: A deterministic selection algorithm that runs in Θ(n) time in the worst case by choosing a provably good pivot.
- **Helpful partitioning**: A partitioning that reduces the number of elements in play to at most 3/4 of the previous size.
- **Middle half**: All but the smallest ⌈n/4⌉-1 and greatest ⌈n/4⌉-1 elements.
- **Generation**: In the analysis of RANDOMIZED-SELECT, the sequence of sets between consecutive helpful partitionings.
- **Weighted median**: An element xk satisfying sum of weights of elements < xk < 1/2 and sum of weights of elements > xk ≤ 1/2.
- **Post-office location problem**: Find point p minimizing ∑ w·d(a,b). In 1D with Manhattan distance, weighted median is optimal.
- **k-th quantiles**: The k-1 order statistics that divide a sorted set into k equal-sized sets.
- **BLUM-FLOYD-PRATT-RIVEST-TARJAN (SELECT)**: The worst-case linear-time median algorithm.

### Processes / Algorithms

#### MINIMUM (A, n)
- **Type**: Algorithm.
- **Goal**: Find the minimum of n elements.
- **Input**: Array A[1:n].
- **Output**: The minimum element.
- **Steps**:
  1. `min = A[1]`
  2. For `i = 2` to `n`:
     - If `min > A[i]`: `min = A[i]`
  3. Return `min`
- **Complexity**: n-1 comparisons — optimal (proven by tournament argument: every non-winner must lose at least one match).

#### Simultaneous minimum and maximum
- **Naive**: Find min and max independently — 2n-2 comparisons.
- **Optimized**: At most 3⌊n/2⌋ comparisons.
  - Process elements in pairs.
  - Compare pair elements with each other (1 comparison).
  - Compare smaller to current min, larger to current max (2 comparisons).
  - Total: 3 comparisons per 2 elements.
  - If n is odd: initialize min=max=A[1], then process rest in pairs.
  - If n is even: compare first two elements to initialize, then process rest in pairs.
- **Total comparisons**: If n is odd: 3⌊n/2⌋. If n is even: 3n/2 - 2.

#### RANDOMIZED-SELECT (A, p, r, i)
- **Type**: Randomized divide-and-conquer algorithm for selection.
- **Goal**: Return the i-th smallest element of A[p:r].
- **Input**: Array A, indices p, r, integer i (1 ≤ i ≤ r-p+1). Assumes distinct elements.
- **Output**: The i-th smallest element.
- **Steps**:
  1. If `p == r`: return `A[p]`  // base case, i must be 1
  2. `q = RANDOMIZED-PARTITION(A, p, r)`  // partition randomly
  3. `k = q - p + 1`  // number of elements in low side + pivot
  4. If `i == k`: return `A[q]`  // pivot is the answer
  5. Else if `i < k`: return `RANDOMIZED-SELECT(A, p, q-1, i)`  // recurse on low side
  6. Else: return `RANDOMIZED-SELECT(A, q+1, r, i-k)`  // recurse on high side (adjust i)
- **Complexity**: 
  - Worst-case: Θ(n²) (when always unlucky with pivot)
  - Expected: Θ(n)
- **Key difference from quicksort**: Recurses on only one side of the partition.
- **Intuition for linear expected time**: The pivot is equally likely to be any element. With probability ≥ 1/2, the pivot lies in the "middle half," removing ≥ 1/4 of elements from consideration.

#### SELECT (A, p, r, i) — Worst-case linear-time selection
- **Type**: Deterministic algorithm.
- **Goal**: Return the i-th smallest element in worst-case Θ(n) time.
- **Key idea**: Choose pivot provably well by taking median of group medians.
- **Steps**:
  1. (Lines 1-10) Reduce n until divisible by 5:
     - Loop 0-4 times: find min of A[p:r]; if i=1 return min; otherwise p++, i--.
  2. `g = (r-p+1)/5`  // number of 5-element groups
  3. For j = p to p+g-1: sort each 5-element group in place (e.g., insertion sort)
     - Groups: ⟨A[j], A[j+g], A[j+2g], A[j+3g], A[j+4g]⟩
  4. `x = SELECT(A, p+2g, p+3g-1, ⌈g/2⌉)`  // pivot = median of group medians (recursive)
  5. `q = PARTITION-AROUND(A, p, r, x)`  // partition around pivot x
  6. `k = q - p + 1`
  7. If `i == k`: return `A[q]`
  8. Else if `i < k`: return `SELECT(A, p, q-1, i)`
  9. Else: return `SELECT(A, q+1, r, i-k)`
- **Why groups of 5?**: Ensures the pivot is at least as large as 3g/2 elements and at most as large as 3g/2 elements, limiting the recursive subproblem size to ≤ 7n/10.
- **Recurrence**: T(n) ≤ T(n/5) + T(7n/10) + Θ(n)
- **Solution**: T(n) = Θ(n) (by substitution: assume T(n) ≤ cn; T(n) ≤ c(n/5) + c(7n/10) + Θ(n) = 9cn/10 + Θ(n) ≤ cn for c sufficiently large).
- **Note**: The algorithm is mostly of theoretical interest; RANDOMIZED-SELECT is more practical.

### Formulas & Equations

#### Selection recurrences

**RANDOMIZED-SELECT worst case**:
- T(n) = T(n-1) + Θ(n) = Θ(n²)

**RANDOMIZED-SELECT expected**:
- Intuition: with probability ≥ 1/2, at most 3/4 of elements remain.
- T(n) ≤ T(3n/4) + Θ(n) → Θ(n) by case 3 of master theorem.
- Expected number of helpful partitionings needed: ≤ 2 (geometric distribution).

**Lemma 9.1**: A partitioning is helpful with probability at least 1/2.
- **Proof**: If pivot falls in "middle half" (all but smallest ⌈n/4⌉-1 and greatest ⌈n/4⌉-1), at least ⌈n/4⌉ elements leave play. Probability of pivot in middle half ≥ 1 - (⌈n/4⌉-1)/n - (⌈n/4⌉-1)/n ≥ 1/2.

**Theorem 9.2**: RANDOMIZED-SELECT has expected running time Θ(n).
- **Proof sketch**: Bound number of helpful partitionings ≤ ⌈log_{4/3} n⌉. Expected number of sets in k-th generation: E[Xk] ≤ 2. Total comparisons < ∑ n·(3/4)^k·E[Xk] = O(n).

**SELECT recurrence**:
- T(n) ≤ T(⌈n/5⌉) + T(7n/10 + 6) + O(n)
- Simplified: T(n) ≤ T(n/5) + T(7n/10) + Θ(n)
- Solved: T(n) = Θ(n) by substitution (T(n) ≤ cn when c ≥ 10·Θ(n)).

**Lower bound for minimum**: n - 1 comparisons (each non-winner must lose at least once).

**Simultaneous min and max**: At most 3⌊n/2⌋ comparisons (process elements in pairs).

### Comparisons & Trade-offs

| Dimension | RANDOMIZED-SELECT | SELECT |
|-----------|-------------------|--------|
| Expected time | Θ(n) | Θ(n) |
| Worst-case time | Θ(n²) | Θ(n) |
| Pivot selection | Random | Median of group medians |
| Practical use | Yes, fast | Mostly theoretical |
| Constant factors | Low | High |
| In-place | Yes | Yes |

**Selection by sorting**: Trivial O(n lg n) solution — sort, then index. Randomized SELECT achieves Θ(n) expected, SELECT achieves Θ(n) worst-case, both beating the comparison model's lower bound for sorting because they do not sort all elements.

**Selection vs sorting lower bound**: The Ω(n lg n) lower bound for comparison sorting does NOT apply to selection. Selection can be done in linear time in the comparison model.

### Proof & Argument Patterns

#### Tournament argument for min lower bound
- Each comparison is a "match" where the smaller element wins.
- Every element except the ultimate winner must lose at least one match.
- Therefore at least n-1 comparisons are needed.

#### RANDOMIZED-SELECT expected time (Theorem 9.2)
1. Define A(j) as set of elements in play after j partitionings.
2. A "helpful" partitioning means |A(j)| ≤ (3/4)|A(j-1)|.
3. **Lemma 9.1**: P(helpful) ≥ 1/2 (pivot in middle half).
4. Maximum number of helpful partitionings: ⌈log_{4/3} n⌉.
5. Partitionings grouped into "generations" between helpful ones.
6. Xk = number of sets in generation k. E[Xk] ≤ 2.
7. Total comparisons < ∑_{k} n_k · Xk where n_k ≤ (3/4)^k n.
8. E[comparisons] < ∑ (3/4)^k n · 2 = 2n · ∑ (3/4)^k = O(n).

#### SELECT worst-case time (Theorem 9.3)
1. Show ≥ 3g/2 elements are known to be ≤ pivot and ≥ 3g/2 elements known to be ≥ pivot.
2. Thus the largest possible recursive call has at most 5g - 3g/2 = 7g/2 ≤ 7n/10 elements.
3. Recursive call to find pivot T(n/5).
4. T(n) ≤ T(n/5) + T(7n/10) + Θ(n).
5. Solve by substitution: T(n) ≤ cn requires c(n/5) + c(7n/10) + Θ(n) ≤ cn → c ≥ 10·Θ(n).

### Edge Cases & Pitfalls

- **RANDOMIZED-SELECT never recurses on 0-length array** (Exercise 9.2-1): If q is the pivot and i < k, then k ≥ 2 (since otherwise i < k would mean i < 1). So q-1 ≥ p. Similarly if i > k, q+1 ≤ r.
- **RANDOMIZED-SELECT worst-case**: Can be Θ(n²) if always unlucky (always picks max element as pivot), even to find the minimum.
- **SELECT on groups of 3**: If groups of size 3 are used, the recurrence becomes T(n) ≤ T(n/3) + T(2n/3) + Θ(n), which only gives O(n lg n) — not linear!
- **SELECT on groups of 7**: Works in linear time (Exercise 9.3-1), recurrence T(n) ≤ T(n/7) + T(5n/7 + O(1)) + Θ(n) still linear.
- **Distinct elements assumption**: Selection algorithms assume distinct elements for analysis. Can enforce by converting to ordered pairs at cost Θ(n).

### End-of-Chapter Material

**Key terms**: order statistic, minimum, maximum, median, lower median, upper median, selection problem, randomized selection, helpful partitioning, generation, worst-case linear-time selection, weighted median, post-office location problem, kth quantiles.

**Key results**:
- Minimum can be found in n-1 comparisons (optimal).
- Simultaneous min and max can be found in at most 3⌊n/2⌋ comparisons.
- **Theorem 9.2**: RANDOMIZED-SELECT has expected running time Θ(n).
- **Theorem 9.3**: SELECT runs in Θ(n) time in the worst case.
- The algorithm for worst-case linear-time selection was devised by Blum, Floyd, Pratt, Rivest, and Tarjan.
- The randomized version (RANDOMIZED-SELECT) is due to Hoare.
- Selection can be solved in O(n) expected time and O(n) worst-case time in the comparison model (without sorting all elements).
- The exact number of comparisons needed for median is still unknown: between (2+ε)n and 2.95n.

**Representative exercises**:
- 9.1-1: Second smallest can be found in n + ⌈lg n⌉ - 2 comparisons (find min using tournament, then the second smallest is among the ⌈lg n⌉ elements that lost to the min).
- 9.2-1: RANDOMIZED-SELECT never recurses on a 0-length array.
- 9.2-3: Worst-case sequence: always pick the maximum remaining element as pivot when selecting min.
- 9.3-1: SELECT works in linear time with groups of 7 (recurrence T(n) ≤ T(n/7) + T(5n/7 + O(1)) + Θ(n)).
- 9.3-3: Use SELECT to find a good pivot for quicksort (median), ensuring O(n lg n) worst-case.
- 9.3-7: Optimal pipeline location = median of y-coordinates.
- 9.3-10: Median of two sorted arrays in O(lg n) using binary search.

---

## Cross-Cutting Topics

### Design Paradigms & Meta-Methods

**Divide and Conquer**:
- **Heapsort**: Build-heap (build data structure) → repeatedly extract max. Not classic divide-and-conquer.
- **Quicksort**: Divide (partition) → Conquer (recurse on both sides) → Combine (nothing). The partitioning step does all the work.
- **Randomized Selection (RANDOMIZED-SELECT)**: Divide (randomized partition) → Conquer (recurse on ONE side). Unlike quicksort, only one recursive call.
- **Deterministic Selection (SELECT)**: Find a good pivot (recursively) → Partition → Recurse on one side. Two layers of divide-and-conquer.

**Using a Data Structure for Algorithm Design**:
- Heapsort demonstrates managing information with a heap data structure.
- Priority queues use heaps to efficiently manage dynamic sets with keys.

**Randomization**:
- RANDOMIZED-QUICKSORT: Random pivot eliminates worst-case input.
- RANDOMIZED-SELECT: Random pivot gives linear expected time.
- RANDOMIZED-PARTITION: Simple swap before partitioning.

**Recursion Tree Analysis**:
- Used for quicksort balanced partitioning.
- Used for SELECT recurrence.

### Proof & Argument Patterns

**Loop Invariants**:
- BUILD-MAX-HEAP: "Each node i+1, i+2, ..., n is the root of a max-heap."
- PARTITION (Lomuto): Three-region invariant (≤x, >x, unknown).
- HEAPSORT: "A[1:i] is max-heap of i smallest; A[i+1:n] contains n-i largest, sorted."
- MAX-HEAP-INCREASE-KEY: "Max-heap property holds except at i vs parent."

**Induction**:
- Radix sort correctness: by induction on digit position.
- HEAPSORT correctness through loop invariant (de facto induction).

**Decision Tree Model** (for lower bounds):
- Model comparison sort as a decision tree.
- Each permutation must be a reachable leaf → n! ≤ number of leaves ≤ 2^h.
- Therefore h ≥ lg(n!) = Ω(n lg n).
- The decision tree model abstracts away all aspects except comparisons.

**Contradiction / Contrapositive**:
- 0-1 sorting lemma proof uses the contrapositive.

**Substitution Method**:
- Quicksort worst-case: guess T(n) ≤ cn².
- SELECT: guess T(n) ≤ cn.

**Probabilistic Analysis**:
- Quicksort expected time: indicator random variables + linearity of expectation.
- Geometric distribution for helpful partitionings in RANDOMIZED-SELECT.
- Binomial distribution for bucket sizes in bucket sort.

### Probability & Statistics Foundation

**Indicator random variables** (Section 5.2):
- Xij = I{zi is compared with zj}.
- E[X] = Σ E[Xij] by linearity.
- Used in quicksort expected time analysis.

**Binomial distribution**:
- Bucket size in bucket sort: ni ∼ Binomial(n, 1/n).
- E[ni] = 1, Var[ni] = 1 - 1/n.

**Geometric distribution**:
- Number of trials until first successful partitioning: E[X] ≤ 2 since P(success) ≥ 1/2.

**Harmonic numbers**:
- H_n = 1 + 1/2 + 1/3 + ... + 1/n = ln n + O(1).
- Used in quicksort expected time summation.

**Uniform distribution**:
- Bucket sort assumes uniform [0,1) distribution.
- Random pivot selection assumes uniform distribution over elements.

### People & Dates

- **J. W. J. Williams (1964)**: Invented heapsort algorithm and priority queue with heap.
- **Robert W. Floyd (1964)**: Suggested BUILD-MAX-HEAP procedure.
- **C. A. R. Hoare (1962)**: Invented quicksort and its original partitioning algorithm (Hoare partition). Also invented RANDOMIZED-SELECT.
- **N. Lomuto**: The PARTITION procedure in Section 7.1 (Lomuto partition).
- **H. H. Seward (1954)**: Invented counting sort and the idea of combining counting sort with radix sort.
- **L. J. Comrie (1929)**: First published reference to LSD-first radix sort.
- **Blum, Floyd, Pratt, Rivest, Tarjan (1973)**: Devised the worst-case linear-time selection algorithm (SELECT).
- **M. D. McIlroy**: Shows how to engineer a "killer adversary" that forces quicksort to Θ(n²).
- **Fredman and Tarjan (1984)**: Developed Fibonacci heaps (O(1) amortized INSERT and DECREASE-KEY).
- **Fredman and Willard**: Fusion tree sorting O(n lg n / lg lg n).
- **Thorup**: Improved integer sorting bounds, strict Fibonacci heaps.
- **Bent and John**: Lower bound of 2n comparisons for median finding.
- **Schönhage, Paterson, Pippenger**: Upper bound of 3n comparisons for median finding.
- **Dor and Zwick**: Upper bound < 2.95n, lower bound (2+ε)n for median.

---

## Exam Questions by Type

### MCQ

1. **Q:** What is the worst-case running time of quicksort on an already-sorted array using Lomuto partition?
   **A:** Θ(n²)  
   **Distractor:** Θ(n lg n) — this is the expected or best-case time.

2. **Q:** Which of the following is NOT a stable sorting algorithm?
   **A:** Heapsort  
   **Distractor:** Counting sort, merge sort, insertion sort — all are stable.

3. **Q:** What is the running time of BUILD-MAX-HEAP on an array of n elements?
   **A:** O(n)  
   **Distractor:** O(n lg n) — this is the naive upper bound, but the tighter analysis shows linear.

4. **Q:** What is the probability that RANDOMIZED-SELECT compares zi and zj (i < j) on an input of n distinct elements?
   **A:** 2/(j-i+1)  
   **Distractor:** 1/n — wrong; the probability depends on the distance between the elements.

5. **Q:** Which sorting algorithm is NOT subject to the Ω(n lg n) lower bound for comparison sorts?
   **A:** Counting sort  
   **Distractor:** Heapsort — uses comparisons, thus subject to the bound.

6. **Q:** In SELECT (worst-case linear selection), what group size is used?
   **A:** 5  
   **Distractor:** 3 — groups of 3 yield O(n lg n) time.

7. **Q:** What is the worst-case stack depth of the basic QUICKSORT procedure?
   **A:** Θ(n)  
   **Distractor:** Θ(lg n) — this is achievable with tail-recursion optimization.

8. **Q:** How many comparisons are needed to simultaneously find min and max of n elements?
   **A:** At most 3⌊n/2⌋  
   **Distractor:** 2n-2 — the naive algorithm; the pair-processing method improves the constant.

### Short Answer

1. **Q:** Show that any comparison sort requires Ω(n lg n) comparisons.
   **Rubric:** (1) Model as decision tree. (2) Each permutation must be a leaf → n! ≤ l. (3) Binary tree of height h has ≤ 2^h leaves → l ≤ 2^h. (4) h ≥ lg(n!) = Ω(n lg n) by Stirling's approximation.

2. **Q:** Why is counting sort able to beat the Ω(n lg n) lower bound?
   **Rubric:** (1) Counting sort is not a comparison sort. (2) It uses actual values as array indices, not comparisons. (3) The Ω(n lg n) lower bound applies only to comparison sorts.

3. **Q:** Explain the difference between Lomuto and Hoare partitioning.
   **Rubric:** Lomuto: (1) Uses A[r] as pivot. (2) Single pass with i and j pointers. (3) Returns index of pivot. (4) Θ(n) time but more swaps. Hoare: (1) Uses A[p] as pivot. (2) Two pointers i, j from opposite ends moving toward each other. (3) Returns j where p ≤ j < r. (4) More efficient in practice, especially with equal elements.

### Trace / Apply

1. **Input:** A = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7], n = 10. **Apply BUILD-MAX-HEAP** → Show the array after each MAX-HEAPIFY call.
   **Expected output:** Initial: [4,1,3,2,16,9,10,14,8,7]. i=5: [4,1,3,2,16,9,10,14,8,7] (no change, 16 > children). i=4: [4,1,3,14,16,9,10,2,8,7]. i=3: [4,1,10,14,16,9,3,2,8,7]. i=2: [4,16,10,14,7,9,3,2,8,1]. i=1: [16,14,10,8,7,9,3,2,4,1].

2. **Input:** A = [13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11]. **Apply PARTITION(A, 1, 12)** with pivot = A[12] = 11.
   **Expected output:** After partitioning: [9, 5, 8, 7, 4, 2, 6, 11, 21, 12, 19, 13] and return index 8 (q=8).

3. **Input:** A = [3, 2, 1, 5, 4], i = 3 (find median). **Apply RANDOMIZED-SELECT** with lucky pivots (always pick median).
   **Expected output:** Partition 1: pivot at q=3, k=3, i=k=3, return A[3]=3.

### Essay / Long-Form

1. **Q:** Compare and contrast quicksort, heapsort, and merge sort in terms of asymptotic complexity, in-place property, stability, and practical performance.
   **Key points:** (1) Heapsort: O(n lg n) worst-case, in-place, not stable, moderate constants. (2) Merge sort: O(n lg n) worst-case, not in-place (Θ(n) extra space), stable, higher constants. (3) Quicksort: Θ(n²) worst-case but Θ(n lg n) expected/typical, in-place, not stable (Lomuto), smallest constants. (4) Practical: quicksort usually fastest; heapsort useful when worst-case guarantees needed; merge sort used when stability and guaranteed performance needed.

2. **Q:** Prove that the expected running time of RANDOMIZED-QUICKSORT is O(n lg n).
   **Key points:** (1) Lemma 7.1: running time = O(n+X) where X = number of comparisons. (2) Lemma 7.2: zi compared with zj iff first pivot from Zij is zi or zj. (3) Lemma 7.3: Pr[zi compared with zj] = 2/(j-i+1). (4) E[X] = Σ_{i=1}^{n-1} Σ_{j=i+1}^{n} 2/(j-i+1) = Σ_{i=1}^{n-1} O(H_{n-i}) = O(n lg n). (5) Therefore expected time = O(n + n lg n) = O(n lg n).

3. **Q:** Explain how SELECT achieves worst-case linear time for selection.
   **Key points:** (1) Groups of 5 ensure pivot is provably good. (2) Median of group medians guarantees at least 3n/10 elements are ≤ pivot and 3n/10 ≥ pivot. (3) Recurrence: T(n) ≤ T(n/5) + T(7n/10) + Θ(n). (4) Solve by substitution: assume T(n) ≤ cn, show T(n) ≤ 9cn/10 + Θ(n) ≤ cn for c large enough. (5) Why not groups of 3: recurrence T(n) ≤ T(n/3) + T(2n/3) + Θ(n) only yields O(n lg n).

### Diagram Label

1. **Diagram:** Max-heap as a nearly complete binary tree with values [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]. **Label:** root, leaves, height, parent-child relationships.
2. **Diagram:** Decision tree for comparison sort on 3 elements. **Label:** internal nodes (comparisons), leaves (permutations), path for input ⟨6,8,5⟩.
