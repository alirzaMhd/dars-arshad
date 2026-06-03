# CLRS Chapters 17–19: Comprehensive Study Guide

---

## Chapter 17: Augmenting Data Structures

### 1. NAMED ENTITIES — Every Term with Definition

| Term | Definition |
|------|-----------|
| **Augmenting a data structure** | Storing additional information in a textbook data structure to support new operations without creating an entirely new type |
| **Order-statistic tree** | A red-black tree augmented with a `size` attribute in each node; supports fast order-statistic queries (OS-SELECT, OS-RANK) |
| **`x.size`** | The number of internal nodes in the subtree rooted at `x` (including `x` itself, excluding sentinels); sentinel `T.nil.size = 0` |
| **Rank of an element** | The position at which it would be printed in an inorder walk of the tree |
| **Interval trichotomy** | For any two intervals `i` and `i'`, exactly one holds: (a) they overlap, (b) `i` is left of `i'` (`i.high < i'.low`), (c) `i` is right of `i'` (`i'.high < i.low`) |
| **Interval tree** | A red-black tree augmented such that each node `x` contains an interval `x.int` and a `x.max` value; supports INTERVAL-SEARCH |
| **`x.max`** | Maximum value of any interval endpoint in the subtree rooted at `x` |
| **Point of maximum overlap** | A point with the largest number of intervals in the set that overlap it (Problem 17-1) |
| **Josephus permutation** | The order in which people are removed from a circle when every m-th person is removed (Problem 17-2) |

### 2. PROCESSES/ALGORITHMS

#### OS-SELECT(x, i) — Find i-th smallest element
**Input:** Node `x` (root of subtree), integer `i` (1-indexed rank)
**Output:** Pointer to node containing i-th smallest key in subtree
**Steps:**
1. `r = x.left.size + 1`  (rank of x within its subtree)
2. If `i == r`: return `x`
3. If `i < r`: return `OS-SELECT(x.left, i)`
4. Else (`i > r`): return `OS-SELECT(x.right, i - r)`
**Complexity:** O(lg n) — height of red-black tree
**Example** (Fig 17.1, searching 17th smallest):
- Root (key 26): left.size=12 → rank=13 → i=17 > 13 → go right with i=4
- Node (key 41): left.size=5 → rank=6 → i=4 < 6 → go left with i=4
- Node (key 30): left.size=1 → rank=2 → i=4 > 2 → go right with i=2
- Node (key 38): left.size=1 → rank=2 → i=2 == r → return key 38

#### OS-RANK(T, x) — Determine rank of element x
**Input:** Tree `T`, node `x`
**Output:** Rank of `x` in inorder walk of `T`
**Steps:**
1. `r = x.left.size + 1`; `y = x`
2. While `y ≠ T.root`:
   - If `y == y.p.right`: `r = r + y.p.left.size + 1`
   - `y = y.p`
3. Return `r`
**Loop invariant:** At start of each iteration, `r` is rank of `x.key` in subtree rooted at `y`
**Complexity:** O(lg n)
**Example** (key 38 in Fig 17.1): y.key/r sequence: 38/2 → 30/4 → 41/4 → 26/17 → returns 17

#### Four-Step Method for Augmenting a Data Structure
1. **Choose** an underlying data structure
2. **Determine** additional information to maintain
3. **Verify** that the additional information can be maintained efficiently by the basic modifying operations
4. **Develop** new operations

#### INTERVAL-SEARCH(T, i) — Find overlapping interval
**Input:** Interval tree `T`, interval `i`
**Output:** Pointer to node with interval overlapping `i`, or `T.nil` if none exists
**Steps:**
1. `x = T.root`
2. While `x ≠ T.nil` and `i` does not overlap `x.int`:
   - If `x.left ≠ T.nil` and `x.left.max ≥ i.low`: `x = x.left`
   - Else: `x = x.right`
3. Return `x`
**Correctness (Theorem 17.2):** If search goes right: left subtree has no overlapping interval. If search goes left: left subtree has an overlap OR right subtree has no overlap.
**Complexity:** O(lg n)

### 3. THEOREMS

**Theorem 17.1 (Augmenting a Red-Black Tree)**
- If attribute `f` at node `x` depends only on `x`, `x.left`, `x.right` (including `x.left.f`, `x.right.f`) and can be computed in O(1) time, then insertion and deletion can maintain `f` without asymptotically affecting O(lg n) time.
- **Key insight:** A change to `x.f` propagates only to ancestors; height is O(lg n); rotations are constant per insertion/deletion.

**Theorem 17.2 (Correctness of INTERVAL-SEARCH)**
- Any execution of INTERVAL-SEARCH returns a node whose interval overlaps `i`, or returns `T.nil` and the tree contains no overlapping interval.

### 4. FORMULAS & EQUATIONS

- `x.size = x.left.size + x.right.size + 1`
- `x.max = max{ x.int.high, x.left.max, x.right.max }`
- `r = x.left.size + 1` (rank of node x within its subtree)
- Interval overlap condition: `i.low ≤ i'.high` AND `i'.low ≤ i.high`

### 5. DATA STRUCTURES — Properties, Operations, Complexity

| Structure | Operations | Time |
|-----------|-----------|------|
| **Order-statistic tree** | OS-SELECT, OS-RANK | O(lg n) |
| | Insertion (with size maintenance) | O(lg n) |
| | Deletion (with size maintenance) | O(lg n) |
| **Interval tree** | INTERVAL-INSERT | O(lg n) |
| | INTERVAL-DELETE | O(lg n) |
| | INTERVAL-SEARCH | O(lg n) |

**Size maintenance during insertion:**
- Phase 1 (going down): increment `x.size` for each node on path from root to new node (O(lg n))
- Phase 2 (rotations): update sizes for the two nodes involved in each rotation (O(1) per rotation, ≤2 rotations)
- Deletion: traverse path from lowest moved node to root, decrementing sizes (O(lg n))

### 6. END-OF-CHAPTER EXERCISES (Summary)

**17.1-1:** Trace OS-SELECT(T.root, 10) on Figure 17.1
**17.1-2:** Trace OS-RANK(T, x) for node with key 35 on Figure 17.1
**17.1-3:** Write nonrecursive OS-SELECT
**17.1-4:** Write OS-KEY-RANK(T, k) — returns rank of key k
**17.1-5:** Find i-th successor of x in O(lg n) time
**17.1-6:** Maintain rank instead of size attribute during insertion/deletion/rotation
**17.1-7:** Count inversions using order-statistic tree O(n lg n)
**17.1-8:** Count intersecting chords on a circle O(n lg n)
**17.2-1:** Support MINIMUM, MAXIMUM, SUCCESSOR, PREDECESSOR in O(1) by adding pointers
**17.2-2:** Can maintain black-heights and depths using Theorem 17.1
**17.2-3:** Maintain associative aggregate over inorder listing; updates in O(1) per rotation
**17.3-1:** LEFT-ROTATE updating max in O(1)
**17.3-2:** Find overlapping interval with minimum low endpoint
**17.3-3:** List all overlapping intervals in O(min{n, k lg n})
**17.3-4:** INTERVAL-SEARCH-EXACTLY — search by both low and high O(lg n)
**17.3-5:** MIN-GAP — maintain set of numbers supporting closest-pair query
**17.3-6:** Rectangle overlap detection using sweep line O(n lg n)
**17-1 (Problem):** Point of maximum overlap — augment red-black tree with +1/-1 at endpoints
**17-2 (Problem):** Josephus permutation — O(n) for constant m, O(n lg n) for variable m using order-statistic tree

---

## Chapter 18: B-Trees

### 1. NAMED ENTITIES — Every Term with Definition

| Term | Definition |
|------|-----------|
| **B-tree** | A balanced search tree designed for disk storage; nodes may have many children (high branching factor); all leaves at same depth |
| **Minimum degree `t`** | Fixed integer `t ≥ 2` defining bounds on number of keys per node |
| **Full node** | A node containing exactly `2t - 1` keys (maximum capacity) |
| **2-3-4 tree** | B-tree with `t = 2`; each internal node has 2, 3, or 4 children |
| **B+ -tree** | Variant storing all satellite information in leaves; internal nodes contain only keys and child pointers (maximizes branching factor) |
| **B*-tree** | Variant requiring each internal node to be at least 2/3 full |
| **Block** | Unit of disk read/write; typical size 512–4096 bytes |
| **Latency** | Time spent waiting for mechanical movements (platter rotation + arm movement) |
| **Secondary storage** | Disk drives/SSDs; much slower than main memory but cheaper and higher capacity |
| **Cache-oblivious algorithms** | Algorithms that work efficiently without knowledge of memory hierarchy transfer sizes |
| **2-3 tree** | Precursor to B-trees; every internal node has 2 or 3 children (invented by J.E. Hopcroft, 1970) |

### 2. B-TREE PROPERTIES

**Node attributes:**
- `x.n` — number of keys currently stored
- `x.key₁, x.key₂, …, x.key_{x.n}` — keys in monotonically increasing order
- `x.leaf` — TRUE if leaf, FALSE if internal node
- `x.c₁, x.c₂, …, x.c_{x.n+1}` — pointers to children (internal nodes only)

**Structural properties:**
1. Keys separate subtree key ranges: `k₁ ≤ key₁ ≤ k₂ ≤ key₂ ≤ … ≤ key_{x.n} ≤ k_{x.n+1}`
2. All leaves at same depth (height `h`)
3. **Every node (except root)** has at least `t - 1` keys (at least `t` children if internal)
4. **Root** has at least 1 key (if nonempty)
5. **Every node** has at most `2t - 1` keys (at most `2t` children if internal)

### 3. PROCESSES/ALGORITHMS

#### B-TREE-SEARCH(x, k) — Search for key k
**Input:** Node `x`, key `k`
**Output:** `(y, i)` where `y.keyᵢ = k`, or NIL
**Steps:**
1. `i = 1`
2. While `i ≤ x.n` and `k > x.keyᵢ`: `i = i + 1`
3. If `i ≤ x.n` and `k == x.keyᵢ`: return `(x, i)`
4. Else if `x.leaf`: return NIL
5. Else: `DISK-READ(x.cᵢ)`; return `B-TREE-SEARCH(x.cᵢ, k)`
**Complexity:**
- Disk accesses: O(logₜ n) = O(h)
- CPU time: O(t h) = O(t logₜ n)
- With binary search within node: O(lg n) independent of t

#### B-TREE-CREATE(T) — Create empty B-tree
1. `x = ALLOCATE-NODE()`
2. `x.leaf = TRUE`; `x.n = 0`
3. `DISK-WRITE(x)`
4. `T.root = x`
**Complexity:** O(1) disk operations, O(1) CPU

#### B-TREE-SPLIT-CHILD(x, i) — Split a full child
**Input:** Nonfull internal node `x`, index `i` such that `x.cᵢ` (a full child) is in main memory
**Effect:** Splits full child `y = x.cᵢ` into `y` and `z`; median key moves up to `x`
**Steps:**
1. `y = x.cᵢ` (full node to split)
2. `z = ALLOCATE-NODE()`
3. `z.leaf = y.leaf`; `z.n = t - 1`
4. Copy largest `t-1` keys from `y` to `z` (lines 5-6)
5. If not leaf, copy corresponding `t` children (lines 7-9)
6. `y.n = t - 1`
7. Shift `x`'s children right; insert `z` as `x.c_{i+1}` (lines 11-13)
8. Shift `x`'s keys right; insert `y.keyₜ` as `x.keyᵢ` (lines 14-16)
9. `x.n = x.n + 1`
10. `DISK-WRITE(y)`, `DISK-WRITE(z)`, `DISK-WRITE(x)`
**Complexity:** CPU: Θ(t); Disk operations: O(1)
**Key point:** Splitting is the **only way** the tree grows taller (height increases at the top, not the bottom)

#### B-TREE-SPLIT-ROOT(T) — Split the root
1. `s = ALLOCATE-NODE()`; `s.leaf = FALSE`; `s.n = 0`
2. `s.c₁ = T.root`; `T.root = s`
3. `B-TREE-SPLIT-CHILD(s, 1)`
4. Return `s`

#### B-TREE-INSERT(T, k) — Insert key k into B-tree
1. `r = T.root`
2. If `r.n == 2t - 1` (root is full):
   - `s = B-TREE-SPLIT-ROOT(T)` (new root with 0 keys, r as child)
   - `B-TREE-INSERT-NONFULL(s, k)`
3. Else: `B-TREE-INSERT-NONFULL(r, k)`

#### B-TREE-INSERT-NONFULL(x, k) — Insert into nonfull node
**Key invariant:** Node `x` is nonfull when called
**Steps:**
1. `i = x.n`
2. If `x.leaf`:
   - Shift keys right to make room; insert `k`
   - `x.n = x.n + 1`; `DISK-WRITE(x)`
3. Else (internal node):
   - Find child `x.cᵢ` where `k` belongs (lines 9-11)
   - `DISK-READ(x.cᵢ)`
   - If `x.cᵢ` is full: `B-TREE-SPLIT-CHILD(x, i)`; adjust `i` if `k > x.keyᵢ`
   - Recurse: `B-TREE-INSERT-NONFULL(x.cᵢ, k)`
**Complexity:** O(h) disk accesses; O(t h) CPU = O(t logₜ n)
**Design:** Single pass down the tree — split full nodes preemptively to avoid backing up

#### B-TREE-DELETE(T, k) — Delete key k from B-tree
**Design principle:** Single downward pass; ensures each visited node (except possibly root) has at least `t` keys before recursing (one more than minimum `t-1`)

**Case 1** — Arrive at **leaf** `x`:
- If `x` contains `k`: delete it
- If not: `k` not in tree

**Case 2** — Arrive at **internal node** `x` containing `k = x.keyᵢ`:
- **Case 2a:** `x.cᵢ` (preceding child) has ≥ `t` keys
  - Find predecessor `k'` in subtree of `x.cᵢ`; recursively delete `k'`; replace `k` with `k'`
- **Case 2b:** `x.cᵢ` has `t-1` keys, `x.c_{i+1}` (succeeding child) has ≥ `t` keys
  - Symmetric: find successor `k'` in subtree of `x.c_{i+1}`; replace `k` with `k'`
- **Case 2c:** Both `x.cᵢ` and `x.c_{i+1}` have `t-1` keys
  - Merge `k` and `x.c_{i+1}` into `x.cᵢ` (now `2t-1` keys); free `x.c_{i+1}`; recursively delete `k` from `x.cᵢ`

**Case 3** — Arrive at internal node `x` **not containing** `k`:
- Determine child `x.cᵢ` that should contain `k`
- If `x.cᵢ` has only `t-1` keys, apply Case 3a or 3b:
  - **Case 3a:** `x.cᵢ` has an immediate sibling with ≥ `t` keys → rotate a key through `x`
  - **Case 3b:** Both siblings have `t-1` keys → merge `x.cᵢ` with a sibling, moving a key from `x` down
- Recurse on appropriate child

**Root underflow:** If root ends up with zero keys (Cases 2c, 3b), delete root and make its only child the new root → height decreases by 1

**Complexity:** O(h) disk accesses; O(t h) CPU time

### 4. THEOREMS

**Theorem 18.1 (Height of B-tree)**
If `n ≥ 1`, then for any n-key B-tree of height `h` and minimum degree `t ≥ 2`:
```
h ≤ logₜ ((n+1)/2)
```
**Proof:** Root has ≥1 key; other nodes have ≥ t-1 keys. At depth 1: ≥2 nodes; depth 2: ≥2t nodes; depth 3: ≥2t² nodes; ... depth h: ≥2t^{h-1} nodes. So: `n ≥ 1 + (t-1) · Σ_{i=0}^{h-1} 2t^i = 1 + 2(t-1)(t^h - 1)/(t - 1) = 2t^h - 1`. Thus `t^h ≤ (n+1)/2`.

**Implication:** B-tree height is O(logₜ n); base of logarithm is much larger than 2 for red-black trees. Saves factor of ~lg t in nodes examined.

### 5. COMPARISONS & TRADE-OFFS

| Aspect | B-trees vs Red-black trees |
|--------|--------------------------|
| Branching factor | Large (50–2000 typical); red-black: 2 |
| Height | O(logₜ n) vs O(lg n); much shorter for large t |
| Disk accesses | O(logₜ n) — significantly fewer |
| Node size | As large as a disk block |
| Height growth | At the top (root splits) vs at the bottom |
| Main memory | Root kept permanently in memory; only constant blocks needed |

### 6. DISK STORAGE CONCEPTS

| Concept | Detail |
|---------|--------|
| Platter | Rotating magnetic surface |
| Track | Surface under stationary head |
| Block | Unit of disk I/O (512–4096 bytes) |
| Latency | ~4 ms average access; one rotation: 5.5–11 ms (5400–15000 RPM) |
| Main memory access | ~50 ns — 5 orders of magnitude faster |
| B-tree node size | Typically one full disk block |
| Typical branching factors | 50–2000 (depends on key size relative to block size) |

### 7. END-OF-CHAPTER EXERCISES (Summary)

**18.1-1:** Why `t = 1` not allowed? (A node could have 0 keys, 1 child — degenerate)
**18.1-2:** What `t` values make Figure 18.1 legal?
**18.1-3:** All legal B-trees of `t=2` storing keys {1,2,3,4,5}
**18.1-4:** Max keys in B-tree of height h: `n_max = 2t^h - 1` (when root has 2t-1, others have 2t-1, all nodes full)
**18.1-5:** Red-black tree with black nodes absorbing red children = 2-3-4 tree representation
**18.2-1:** Insert sequence into t=2 B-tree; draw before splits and final
**18.2-2:** Redundant DISK-READ/DISK-WRITE in B-TREE-INSERT
**18.2-3:** B-TREE-INSERT does not always produce minimum height (proof for t=2, keys 1..15)
**18.2-4:** Number of nodes after inserting 1..n into empty t=2 B-tree
**18.2-5:** Different t for leaves vs internal nodes (modify CREATE and INSERT)
**18.2-6:** Binary search within node → O(lg n) CPU time independent of t
**18.2-7:** Choose t to minimize search time with disk read time a + bt; optimal for a=5ms, b=10μs
**18.3-1:** Delete C, P, V from Figure 18.8(f)
**18.3-2:** Write pseudocode for B-TREE-DELETE
**18-1 (Problem):** Stack on secondary storage — disk access analysis
**18-2 (Problem):** Join and split operations on 2-3-4 trees using height attribute

### 8. DATES & PEOPLE

- **1970:** J.E. Hopcroft invents **2-3 trees**
- **1972:** Bayer and McCreight introduce **B-trees** (origin of name unexplained)
- **B-tree notes:** Comer [99] — comprehensive survey; Guibas & Sedgewick [202] — relationships among balanced-tree schemes; Bender, Demaine, Farach-Colton [47] — cache-oblivious B-trees

---

## Chapter 19: Data Structures for Disjoint Sets

### 1. NAMED ENTITIES — Every Term with Definition

| Term | Definition |
|------|-----------|
| **Disjoint-set data structure** | Maintains a collection `𝒮 = {S₁, S₂, …, Sₖ}` of disjoint dynamic sets |
| **Representative** | Some member of a set used to identify the set; must be consistent across queries without intervening modifications |
| **MAKE-SET(x)** | Creates new singleton set `{x}` where `x` is its own representative |
| **UNION(x, y)** | Unites sets containing `x` and `y`; destroys the two original sets |
| **FIND-SET(x)** | Returns pointer to representative of set containing `x` |
| **Weighted-union heuristic** | Always append shorter list to longer list (for linked-list representation) |
| **Disjoint-set forest** | Rooted-tree representation where each node points to its parent; root is representative |
| **Union by rank** | Heuristic: make root with smaller rank (height upper bound) point to root with larger rank |
| **Path compression** | Heuristic: during FIND-SET, make each node on find path point directly to root (two-pass method) |
| **Find path** | The simple path from a node to the root of its tree |
| **Rank** | Upper bound on the height of a node (number of edges in longest path from descendant leaf to node) |
| **Level (of node)** | `level(x) = max{ k : A_k(x.rank) ≤ x.p.rank }` |
| **iter(x)** | `iter(x) = max{ i : A_{level(x)}^{(i)}(x.rank) ≤ x.p.rank }` |

### 2. PROCESSES/ALGORITHMS

#### MAKE-SET(x)
1. `x.p = x`
2. `x.rank = 0`
**Complexity:** O(1)

#### UNION(x, y)
1. `LINK(FIND-SET(x), FIND-SET(y))`
**Complexity:** dominated by two FIND-SET calls + O(1)

#### LINK(x, y) — union by rank
**Input:** Two roots `x`, `y`
1. If `x.rank > y.rank`: `y.p = x`
2. Else: `x.p = y`; if `x.rank == y.rank`: `y.rank = y.rank + 1`

#### FIND-SET(x) — with path compression (recursive, two-pass)
1. If `x ≠ x.p`: `x.p = FIND-SET(x.p)`
2. Return `x.p`
**Two-pass:** First pass up to find root; second pass (during unwind) updates each node to point directly to root
**Nonrecursive alternative:** Exercise 19.3-2

#### CONNECTED-COMPONENTS(G) — Application
```
for each vertex v ∈ G.V:
    MAKE-SET(v)
for each edge (u,v) ∈ G.E:
    if FIND-SET(u) ≠ FIND-SET(v):
        UNION(u,v)
```

#### SAME-COMPONENT(u, v)
```
if FIND-SET(u) == FIND-SET(v): return TRUE
else: return FALSE
```

### 3. LINKED-LIST REPRESENTATION

**Structure:**
- Each set = linked list with `head` (first object = representative) and `tail`
- Each object: set member + pointer to next object + pointer back to set object

**Operation costs (simple):**
- `MAKE-SET`: O(1)
- `FIND-SET`: O(1) (follow pointer to set object, return member at head)
- `UNION`: O(length of appended list) — must update all pointers in smaller list

**Worst-case sequence:** `n` MAKE-SET + `n-1` UNIONs appending longer lists → Σ_{i=1}^{n-1} i = Θ(n²) total, Θ(n) amortized per operation

**Weighted-union heuristic (Theorem 19.1):**
- Always append **shorter** list to **longer** list
- Each object's pointer updated at most ⌈lg n⌉ times (set size at least doubles each time)
- Total time: O(m + n lg n) for m operations, n of which are MAKE-SET
- Amortized: O(1) for MAKE-SET/FIND-SET, O(lg n) for UNION

### 4. DISJOINT-SET FORESTS — Two Heuristics

| Heuristic | Description | Effect on running time |
|-----------|-------------|----------------------|
| **Union by rank** | Root with smaller rank points to root with larger rank; equal ranks → increment | Alone: O(m lg n) |
| **Path compression** | FIND-SET makes each node on find path point directly to root | Combined: O(m α(n)) |
| **Both** | Union by rank + path compression | O(m α(n)) — almost linear |

**Effect of heuristics alone:**
- Union by rank alone: O(m lg n) tight bound (Exercise 19.3-3)
- Path compression alone: Θ(n + f·(1 + log_{2+f/n} n)) where f = FIND-SET operations
- Both: O(m α(n))

### 5. THE ACKERMANN-LIKE FUNCTION AND ITS INVERSE

**Definition of Aₖ(j):**
```
Aₖ(j) = 
  j+1                if k = 0
  A_{k-1}^{(j+1)}(j)  if k ≥ 1
```
where `A^{(i)}(j)` denotes functional iteration: `A^{(1)}(j) = A(j)`, `A^{(i)}(j) = A(A^{(i-1)}(j))`

**Closed forms:**
- `A₀(j) = j + 1`
- `A₁(j) = 2j + 1` (Lemma 19.2)
- `A₂(j) = 2^{j+1}(j+1) - 1` (Lemma 19.3)

**Growth of Aₖ(1):**
- `A₀(1) = 2`
- `A₁(1) = 3`
- `A₂(1) = 7`
- `A₃(1) = 2047`
- `A₄(1) = 2^{2059} - 1 > 16^{514} >> 10^{80}` (atoms in observable universe)

**Definition of α(n):**
```
α(n) = min{ k ≥ 0 : Aₖ(1) ≥ n }
```
**Values:**
- `α(n) = 0` for `0 ≤ n ≤ 2`
- `α(n) = 1` for `n = 3`
- `α(n) = 2` for `4 ≤ n ≤ 7`
- `α(n) = 3` for `8 ≤ n ≤ 2047`
- `α(n) = 4` for `2048 ≤ n ≤ A₄(1)` (practically all n)
- In any conceivable application: **α(n) ≤ 4**

### 6. RANK PROPERTIES (Lemmas)

**Lemma 19.4:** `x.rank ≤ x.p.rank` (strict if x not root); rank is initially 0; increases until x becomes non-root, then never changes; `x.p.rank` monotonically increases.

**Corollary 19.5:** On path from any node to root, ranks strictly increase.

**Lemma 19.6:** Every node has rank at most `n - 1`.
- Tighter bound (Ex 19.4-2): `rank ≤ ⌊lg n⌋`

### 7. AMORTIZED ANALYSIS — Potential Method

**Parameters:** `n` = number of MAKE-SET operations; `m` = total operations
**Conversion:** Replace each UNION with 2 FIND-SET + 1 LINK (Lemma 19.7: preserves O(m α(n)))

**Potential function:**
```
Φ_q = Σ_x ϕ_q(x)

ϕ_q(x) = 
  α(n) · x.rank                                   if x is root or x.rank = 0
  (α(n) - level(x)) · x.rank - iter(x)            otherwise
```

**Properties of ϕ_q(x):**
- `0 ≤ ϕ_q(x) ≤ α(n) · x.rank` (Lemma 19.8)
- If x is non-root with positive rank: `ϕ_q(x) < α(n) · x.rank` (Corollary 19.9)
- Non-root potential never increases; decreases by ≥1 if level(x) or iter(x) changes (Lemma 19.10)

**Amortized costs:**
- **MAKE-SET:** O(1) (Lemma 19.11) — creates node with rank 0
- **LINK:** O(α(n)) (Lemma 19.12) — only y's potential can increase, by at most α(n)
- **FIND-SET:** O(α(n)) (Lemma 19.13) — at most α(n)+2 nodes on find path don't decrease potential; all other positive-rank nodes (followed by same-level node) decrease by ≥1

**Theorem 19.14:** Sequence of m MAKE-SET, UNION, FIND-SET operations on disjoint-set forest with union by rank and path compression runs in **O(m α(n))** time.

### 8. APPLICATIONS

| Application | Description |
|-------------|-------------|
| **Connected components** | CONNECTED-COMPONENTS + SAME-COMPONENT (Section 19.1) |
| **Offline minimum** (Problem 19-1) | Determine which key each EXTRACT-MIN returns using disjoint sets |
| **Depth determination** (Problem 19-2) | Maintain forest with FIND-DEPTH and GRAFT using pseudodistances |
| **Tarjan's offline LCA** (Problem 19-3) | Find lowest common ancestors of pairs in a rooted tree using tree walk + disjoint sets |

### 9. END-OF-CHAPTER EXERCISES (Summary)

**19.1-1:** Trace CONNECTED-COMPONENTS on given graph with 11 vertices
**19.1-2:** Prove: after processing all edges, two vertices in same component iff in same set
**19.1-3:** FIND-SET called 2|E| times; UNION called |V| - k times
**19.2-1:** Pseudocode for linked-list MAKE-SET, FIND-SET, UNION with weighted-union heuristic
**19.2-2:** Trace linked-list operations with weighted-union on 16 elements
**19.2-3:** Amortized bounds using aggregate analysis: O(1) MAKE/FIND, O(lg n) UNION
**19.2-4:** Tight bound for sequence in Figure 19.3 with weighted-union
**19.2-5:** Keep only head pointer (use tail as representative)
**19.2-6:** Remove tail by splicing lists (making first of one list point to first of other)
**19.3-1:** Redo 19.2-2 using forest with union by rank and path compression
**19.3-2:** Nonrecursive FIND-SET with path compression (iterative + stack)
**19.3-3:** Sequence achieving Ω(m lg n) with union by rank, no path compression
**19.3-4:** Add "next" attribute for PRINT-SET in linear time
**19.3-5:** All LINKs before FIND-SETs → O(m) time; path compression alone same?
**19.4-1:** Prove Lemma 19.4 (rank properties)
**19.4-2:** Prove rank ≤ ⌊lg n⌋
**19.4-3:** Bits needed for x.rank: ⌈lg lg n⌉ bits
**19.4-4:** Prove O(m lg n) with union by rank only using rank ≤ ⌊lg n⌋
**19.4-5:** Is professor correct that level(x) ≤ level(x.p)? (No — levels can decrease along path)
**19.4-6:** Scaling potential function constant in proof of Lemma 19.13
**19.4-7:** α'(n) with Aₖ(1) ≥ lg(n+1) — ≤ 3 for all practical n; proof with tighter bound
**19-1 (Problem):** Offline minimum — implement with disjoint sets
**19-2 (Problem):** Depth determination — maintain pseudodistances for FIND-DEPTH and GRAFT
**19-3 (Problem):** Tarjan's offline LCA — tree walk with disjoint sets and colors

### 10. DATES & PEOPLE

- **R.E. Tarjan** — first tight upper bound with inverse Ackermann function [427, 429]; lower bound [428]
- **Hopcroft and Ullman** — earlier O(m lg* n) bound [5, 227]
- **Fredman and Saks** — lower bound on word accesses [155]
- **Kozen** — analysis basis in Section 19.4 [270]
- **Harfst and Reingold** — potential-based version [209]
- **Tarjan and van Leeuwen** — one-pass path compression variants [432]
- **Goel et al.** — random linking yields same asymptotic bound [182]
- **Gabow and Tarjan** — O(m) for certain applications [166]
