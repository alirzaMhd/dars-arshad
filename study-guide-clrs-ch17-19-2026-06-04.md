# Study Guide: Introduction to Algorithms (CLRS 4e) — Part V: Advanced Data Structures

> Generated 2026-06-04. Subject: Computer Science (Algorithms & Data Structures). Exam format: Mixed (MCQ / Problem-solving / Trace). Coverage: comprehensive.
> Target length: Comprehensive (no limit).

## Chapter-by-Chapter Breakdown

---

### Ch. 17 — Augmenting Data Structures

#### Named Entities (Terms & Definitions)

- **Augmenting a data structure**: Storing additional information in a textbook data structure to support new operations, while maintaining the efficiency of the basic modifying operations.
- **Order-statistic tree**: A red-black tree augmented with a `size` attribute in each node, supporting fast order-statistic queries.
- **Order statistic**: The *i*th smallest key in a set (i ∈ {1, 2, …, n}).
- **Rank**: The position of an element in the linear order of the set (as determined by an inorder walk).
- **Interval trichotomy**: For any two closed intervals *i* and *i'*, exactly one holds: (a) they overlap, (b) *i* is left of *i'* (*i.high < i'.low*), or (c) *i* is right of *i'* (*i'.high < i.low*).
- **Interval tree**: A red-black tree augmented with a `max` attribute, maintaining a dynamic set of intervals and supporting overlap queries.
- **Low endpoint**: The left endpoint of an interval (*i.low*).
- **High endpoint**: The right endpoint of an interval (*i.high*).
- **Overlap**: Two intervals *i* and *i'* overlap iff *i* ∩ *i'* ≠ ∅, i.e., *i.low ≤ i'.high* and *i'.low ≤ i.high*.
- **Josephus problem**: A circle of *n* people, every *m*th person removed; the removal order is the Josephus permutation.
- **Point of maximum overlap**: A point with the largest number of intervals that overlap it (always an endpoint of some interval).

#### Processes / Algorithms

##### OS-SELECT (x, i)
- **Type**: Algorithm
- **Goal**: Return pointer to node containing the *i*th smallest key in the subtree rooted at *x*.
- **Input**: Node pointer *x*, integer *i* (1-indexed rank). **Output**: Node pointer.
- **Steps**:
  1. *r* = *x.left.size* + 1   (rank of *x* within its subtree)
  2. If *i* == *r*: return *x*
  3. Elseif *i* < *r*: return OS-SELECT(*x.left*, *i*)
  4. Else: return OS-SELECT(*x.right*, *i − r*)
- **Complexity**: O(lg *n*) — one path from root to leaf, height O(lg *n*).
- **Example**: Find 17th smallest in Fig 17.1:
  - root=26, left.size=12 → rank 13 → i=17-13=4 → go right to 41
  - 41.left.size=5 → rank 6 → i=4 < 6 → go left to 30
  - 30 left.size=1 → rank 2 → i=4-2=2 → go right to 38
  - 38 left.size=1 → rank 2 → i=2 → return 38

##### OS-RANK (T, x)
- **Type**: Algorithm
- **Goal**: Return the rank (position in inorder) of node *x* in order-statistic tree *T*.
- **Input**: Tree *T*, node pointer *x*. **Output**: integer rank.
- **Steps**:
  1. *r* = *x.left.size* + 1
  2. *y* = *x*
  3. While *y* ≠ *T.root*:
     - If *y* == *y.p.right*: *r* = *r* + *y.p.left.size* + 1
     - *y* = *y.p*
  4. Return *r*
- **Loop invariant**: At start of each while iteration, *r* is rank of *x.key* in subtree rooted at *y*.
- **Complexity**: O(lg *n*).
- **Example**: Rank of node with key 38 in Fig 17.1:
  - y=38, r=2; y=30, r=4; y=41, r=4; y=26, r=17 → return 17.

##### Maintaining `size` During Insertion
- **Phase 1 (tree descent)**: Increment `x.size` for each node on path from root to insertion point. New node gets `size=1`. Cost: O(lg *n*).
- **Phase 2 (rotations, ≤2)**: After LEFT-ROTATE(T,x), add:
  - `y.size = x.size`
  - `x.size = x.left.size + x.right.size + 1`
  - Cost per rotation: O(1).

##### Maintaining `size` During Deletion
- **Phase 1**: Traverse path from lowest moved node to root, decrementing `size`. Cost: O(lg *n*).
- **Phase 2** (≤3 rotations): Same as insertion rotation handling. Cost: O(1).

##### Generic 4-Step Method for Augmenting a Data Structure
1. **Choose underlying data structure** (e.g., red-black tree).
2. **Determine additional information** to maintain (e.g., `size`, `max`).
3. **Verify maintainability** — basic modifying ops (insert/delete) can update info efficiently.
4. **Develop new operations** (e.g., OS-SELECT, OS-RANK, INTERVAL-SEARCH).

##### INTERVAL-SEARCH (T, i)
- **Type**: Algorithm
- **Goal**: Return pointer to a node in interval tree *T* whose interval overlaps *i*, or *T.nil* if none.
- **Input**: Interval tree *T*, interval *i*. **Output**: Node pointer.
- **Steps**:
  1. *x* = *T.root*
  2. While *x* ≠ *T.nil* and *i* does not overlap *x.int*:
     - If *x.left* ≠ *T.nil* and *x.left.max ≥ i.low*: *x* = *x.left*
     - Else: *x* = *x.right*
  3. Return *x*
- **Complexity**: O(lg *n)* — single path, each step O(1).
- **Correctness** (Theorem 17.2): The search always heads toward an overlapping interval if one exists. If it goes left, either the left subtree has an overlap or the right subtree has none. If it goes right, the left subtree definitely has no overlap.

##### LEFT-ROTATE for Interval Trees
- After standard rotation, update `max`:
  - `y.max = x.max`
  - `x.max = max(x.int.high, x.left.max, x.right.max)`
- Symmetric for RIGHT-ROTATE.

#### Formulas & Equations

- **Size identity**: `x.size = x.left.size + x.right.size + 1` (with *T.nil.size* = 0)
- **Max identity**: `x.max = max(x.int.high, x.left.max, x.right.max)`
- **Overlap condition**: *i* and *i'* overlap iff *i.low ≤ i'.high* and *i'.low ≤ i.high*.

#### Rules, Laws & Theorems

##### Theorem 17.1 (Augmenting a Red-Black Tree)
- **Statement**: Let *f* be an attribute augmenting an RB tree of *n* nodes. If *x.f* depends only on info in *x*, *x.left*, *x.right* (possibly including *x.left.f*, *x.right.f*) and can be computed in O(1) time, then insertion and deletion can maintain *f* in all nodes without asymptotically affecting the O(lg *n*) running time.
- **Proof sketch**: Changes to *x.f* propagate only up ancestors (O(lg *n*) path). Insertion Phase 1: compute *x.f* O(1), propagate up O(lg *n*). Phase 2: each rotation requires O(lg *n*) propagation, ≤2 rotations. Deletion: similar with ≤3 rotations.
- **Key insight**: Constant number of rotations is critical. If rotations could be Θ(lg *n*), each requiring O(lg *n*) propagation, total would be Θ(lg²*n*).

##### Theorem 17.2 (Correctness of INTERVAL-SEARCH)
- **Statement**: INTERVAL-SEARCH(T,i) either returns a node whose interval overlaps *i*, or returns *T.nil* and *T* contains no such node.
- **Proof**: Two-part invariant on search direction:
  1. Search goes left → left subtree has overlap or right subtree has none.
  2. Search goes right → left subtree has no overlap.
  Uses interval trichotomy and `max` attribute.

#### Data Structures

##### Order-Statistic Tree
- **Base**: Red-black tree.
- **Augmentation**: Each node *x* has attribute `x.size` = number of internal nodes in subtree rooted at *x* (including *x*, excluding sentinel).
- **Supported ops**: OS-SELECT (O(lg *n*)), OS-RANK (O(lg *n*)), plus all standard dynamic-set ops.
- **Maintenance**: Insert/delete still O(lg *n*). Updates propagate up ancestors. Rotations update O(1) local changes.
- **Equal keys**: Rank defined by inorder walk position.
- **Applications**: Counting inversions (Problem 2-4), chord intersection counting.

##### Interval Tree
- **Base**: Red-black tree keyed by low endpoint (*x.int.low*).
- **Augmentation**: Each node *x* has `x.max` = max value of any interval endpoint in subtree rooted at *x*.
- **Supported ops**: INTERVAL-INSERT (O(lg *n*)), INTERVAL-DELETE (O(lg *n*)), INTERVAL-SEARCH (O(lg *n*)).
- **Maintenance**: `max` computable in O(1) from children's `max` and own `high`, so Theorem 17.1 applies.

#### Edge Cases & Common Pitfalls

- **Equal keys in order-statistic trees**: Rank definition becomes ambiguous. CLRS resolves by defining rank as position in inorder walk.
- **Rotation propagation in Theorem 17.1**: If attribute *f* requires O(lg *n*) propagation per rotation (rather than O(1)), the constant number of rotations (≤2 for insert, ≤3 for delete) is essential to keep total O(lg *n*).
- **INTERVAL-SEARCH only finds one overlapping interval**: To list all *k* overlapping intervals, use O(min{n, k lg n}) algorithm (Exercise 17.3-3).
- **Interval trichotomy**: Only holds when comparing *i* and *i'* pairwise. The overlap relation is not transitive.

#### End-of-Chapter Material

**Key terms**: order-statistic tree, size attribute, rank, interval tree, interval trichotomy, max attribute, point of maximum overlap, Josephus permutation.

**Review Exercises (selected)**:
- 17.1-1: Trace OS-SELECT(T.root, 10) on Fig 17.1.
- 17.1-2: Trace OS-RANK(T, x) for x.key=35 on Fig 17.1.
- 17.1-3: Write nonrecursive OS-SELECT.
- 17.1-7: Count inversions in O(n lg n) using order-statistic tree.
- 17.2-2: Can you maintain black-heights? Depths? Yes (they propagate up), yes (but expensive).
- 17.2-3: Associative operator ⊗ over inorder: *x.f* = *x₁.a ⊗ x₂.a ⊗ … ⊗ xₘ.a* can be updated in O(1) after rotation.
- 17.3-2: Find interval overlapping *i* with minimum low endpoint.
- 17.3-3: List all overlapping intervals in O(min{n, k lg n}).

**Problems**:
- **17-1 Point of maximum overlap**: Augment RB tree with +1/−1 endpoint values; track max prefix sum.
- **17-2 Josephus permutation**: Constant *m* → O(n). Variable *m* → O(n lg n) using order-statistic tree.

---

### Ch. 18 — B-Trees

#### Named Entities (Terms & Definitions)

- **B-tree**: A balanced search tree designed for disk storage, with nodes having many children (high branching factor). Generalizes BSTs: internal node with *n* keys has *n+1* children.
- **Minimum degree *t*** (t ≥ 2): Controls how many keys a node can hold. Every node (except root) has at least *t−1* keys; at most *2t−1* keys.
- **Full node**: A node containing exactly *2t−1* keys.
- **B+-tree**: Variant storing all satellite info in leaves, only keys and child pointers in internal nodes (maximizes branching factor).
- **B*-tree**: Variant requiring internal nodes to be at least 2/3 full (vs. 1/2 for B-tree).
- **2-3-4 tree**: B-tree with *t=2*. Internal nodes have 2, 3, or 4 children.
- **2-3 tree**: Precursor to B-trees (Hopcroft, 1970). Internal nodes have 2 or 3 children.
- **Disk block**: Unit of disk I/O. B-tree node size = one disk block.
- **Latency**: Time spent waiting for mechanical movements (platter rotation + arm movement).
- **Track**: Surface passing under a read/write head when stationary.
- **Platter**: Rotating disk coated with magnetizable material.
- **DISK-READ(x)**: Reads block containing *x* from disk into main memory.
- **DISK-WRITE(x)**: Writes block containing *x* from main memory to disk.

#### Disk Access Motivation

- Main memory access: ~50 ns. Disk rotation (7200 RPM): 8.33 ms/rotation. Ratio: >100,000×.
- B-trees minimize disk accesses by using large nodes (one disk block) and high branching factor.
- Two principal costs: (1) number of disk accesses, (2) CPU time.
- A typical B-tree application keeps only a constant number of blocks in main memory.
- Root is always kept in main memory → no DISK-READ on root needed.
- With branching factor 1001, height 2 tree stores >1 billion keys (only 2 disk accesses to find any key if root is cached).

#### B-Tree Properties

1. Every node *x* has: *x.n* (number of keys), keys *x.key₁ ≤ x.key₂ ≤ … ≤ x.keyₓ.ₙ*, *x.leaf* (boolean).
2. Internal nodes have *x.n+1* child pointers *x.c₁, …, x.cₓ.ₙ₊₁*. Leaves have no children.
3. Keys separate subtree ranges: *k₁ ≤ x.key₁ ≤ k₂ ≤ x.key₂ ≤ … ≤ x.keyₓ.ₙ ≤ kₓ.ₙ₊₁*.
4. All leaves have same depth (= tree height *h*).
5. Bounds (minimum degree *t* ≥ 2):
   - Every node except root: at least *t−1* keys (internal nodes: ≥ *t* children).
   - Every node: at most *2t−1* keys (internal: ≤ *2t* children).
   - Nonempty root: at least 1 key.

#### Formulas & Equations

##### Theorem 18.1 (Height of a B-tree)
- **Statement**: If *n ≥ 1*, then for any *n*-key B-tree of height *h* and minimum degree *t ≥ 2*:

  > *h ≤ logₜ ((n+1)/2)*

- **Proof**: Root has ≥1 key. All other nodes have ≥ *t−1* keys. Minimum nodes at depth *d*: ≥ *2tᵈ⁻¹*. Therefore:
  - *n ≥ 1 + (t−1)·2·(1 + t + t² + … + tʰ⁻¹)*
  - *n ≥ 1 + 2(t−1)·(tʰ − 1)/(t − 1) = 2tʰ − 1*
  - *n ≥ 2tʰ − 1* → *tʰ ≤ (n+1)/2* → *h ≤ logₜ ((n+1)/2)*
- **Comparison with RB trees**: Both O(lg *n*), but B-tree's log base *t* is larger → shallower tree → fewer disk accesses (factor of lg *t* fewer).
- **Example**: *t=1001, n=10⁹ → h ≤ log₁₀₀₁(10⁹/2) ≈ 3* (actually height 2 suffices with branching factor 1001).

#### Processes / Algorithms

##### B-TREE-SEARCH (x, k)
- **Type**: Algorithm
- **Goal**: Search for key *k* in subtree rooted at *x*.
- **Input**: Node *x*, key *k*. **Output**: Pair (*y, i*) where *y.keyᵢ = k*, or NIL.
- **Steps**:
  1. *i* = 1
  2. While *i ≤ x.n* and *k > x.keyᵢ*: *i = i + 1*
  3. If *i ≤ x.n* and *k == x.keyᵢ*: return (*x, i*)
  4. Elseif *x.leaf*: return NIL
  5. Else: DISK-READ(*x.cᵢ*); return B-TREE-SEARCH(*x.cᵢ, k*)
- **Complexity**: O(*h*) = O(logₜ *n*) disk accesses; O(*t h*) = O(*t* logₜ *n*) CPU time (linear search within node; binary search would give O(lg *n*) CPU, Exercise 18.2-6).

##### B-TREE-CREATE (T)
- **Type**: Algorithm
- **Goal**: Create an empty B-tree.
- **Steps**:
  1. *x* = ALLOCATE-NODE()
  2. *x.leaf* = TRUE
  3. *x.n* = 0
  4. DISK-WRITE(*x*)
  5. *T.root* = *x*
- **Cost**: O(1) disk operations, O(1) CPU.

##### B-TREE-SPLIT-CHILD (x, i)
- **Type**: Algorithm
- **Goal**: Split the full child *y = x.cᵢ* (with 2*t−1* keys) into two nodes of *t−1* keys each; median key moves up to *x*.
- **Precondition**: *x* is nonfull, *y* is full (resides in main memory).
- **Steps**:
  1. *y = x.cᵢ*
  2. *z* = ALLOCATE-NODE()
  3. *z.leaf = y.leaf*
  4. *z.n = t − 1*
  5. For *j = 1* to *t−1*: *z.keyⱼ = y.keyⱼ₊ₜ*   (copy largest *t−1* keys to *z*)
  6. If not *y.leaf*: for *j = 1* to *t*: *z.cⱼ = y.cⱼ₊ₜ*   (copy corresponding children)
  7. *y.n = t − 1*
  8. Shift *x*'s children right from *i+1* to make room for *z*
  9. *x.cᵢ₊₁ = z*
  10. Shift *x*'s keys right from *i*
  11. *x.keyᵢ = y.keyₜ*   (move median key up)
  12. *x.n = x.n + 1*
  13. DISK-WRITE(*y*); DISK-WRITE(*z*); DISK-WRITE(*x*)
- **Complexity**: CPU Θ(*t*); O(1) disk ops.
- **Key point**: Splitting is the **only** way the B-tree grows in height.

##### B-TREE-SPLIT-ROOT (T)
- **Type**: Algorithm (auxiliary)
- **Goal**: Split the root (if full) into a new root with two children.
- **Steps**:
  1. *s* = ALLOCATE-NODE()
  2. *s.leaf* = FALSE
  3. *s.n* = 0
  4. *s.c₁ = T.root*
  5. *T.root = s*
  6. B-TREE-SPLIT-CHILD(*s, 1*)
  7. Return *s*

##### B-TREE-INSERT (T, k)
- **Type**: Algorithm
- **Goal**: Insert key *k* into B-tree *T* in a single pass.
- **Steps**:
  1. *r = T.root*
  2. If *r.n == 2t − 1* (root is full):
     - *s* = B-TREE-SPLIT-ROOT(*T*)
     - B-TREE-INSERT-NONFULL(*s, k*)
  3. Else: B-TREE-INSERT-NONFULL(*r, k*)
- **Key insight**: Split every full node **as you go down**, guaranteeing parent is never full when you need to split a child.
- **Complexity**: O(*h*) disk accesses; O(*t h*) = O(*t* logₜ *n*) CPU.

##### B-TREE-INSERT-NONFULL (x, k)
- **Type**: Algorithm (auxiliary, tail-recursive)
- **Precondition**: *x* is nonfull.
- **Steps**:
  1. *i = x.n*
  2. If *x.leaf* (insert into leaf):
     - Shift keys in *x* right to make room for *k*
     - *x.keyᵢ₊₁ = k*
     - *x.n = x.n + 1*
     - DISK-WRITE(*x*)
  3. Else (find child to descend to):
     - Find *i* where *k* belongs (*k < x.keyᵢ*)
     - DISK-READ(*x.cᵢ*)
     - If *x.cᵢ.n == 2t − 1* (child full):
       - B-TREE-SPLIT-CHILD(*x, i*)
       - If *k > x.keyᵢ*: *i = i + 1*
     - B-TREE-INSERT-NONFULL(*x.cᵢ, k*)

##### B-TREE-DELETE (T, k)
- **Type**: Algorithm (conceptual, combined search + delete)
- **Goal**: Delete key *k* from B-tree *T* in one downward pass, maintaining invariant that every visited node has ≥ *t* keys (1 more than minimum).
- **Cases** (Figure 18.8):

  **Case 1 — Leaf contains *k***:
  - Simply delete *k* from leaf *x*.
  - If *k* not in leaf → key not in tree.

  **Case 2 — Internal node *x* contains *k = x.keyᵢ***:
  - **Case 2a (left child has ≥ *t* keys)**: Find predecessor *k'* of *k* in left subtree. Recursively delete *k'*, replace *k* with *k'*.
  - **Case 2b (right child has ≥ *t* keys)**: Symmetric. Find successor *k'* in right subtree. Recursively delete *k'*, replace *k* with *k'*.
  - **Case 2c (both children have *t−1* keys)**: Merge *k* and *x.cᵢ₊₁* into *x.cᵢ*. Now *x.cᵢ* has *2t−1* keys. Free *x.cᵢ₊₁*. Recursively delete *k* from *x.cᵢ*.

  **Case 3 — Internal node *x* does NOT contain *k***:
  - Determine child *x.cᵢ* that would contain *k*.
  - If *x.cᵢ* has only *t−1* keys, ensure it gets an extra key before descending:
    - **Case 3a (sibling has ≥ *t* keys)**: Rotate key from sibling through *x* into *x.cᵢ*.
    - **Case 3b (both siblings have *t−1*)**: Merge *x.cᵢ* with a sibling, moving a key from *x* down as median.
  - Recursively delete from appropriate child.

  **Special case (root emptied)**: If merging (cases 2c, 3b) empties the root, delete root and make its only child the new root → tree height decreases by 1.
- **Complexity**: O(*h*) disk ops; O(*t h*) CPU.
- **Key insight**: Guarantees each visited node (except root) has ≥ *t* keys, preventing underflow during recursion.

#### Comparisons & Trade-offs

| Dimension | B-Tree | Red-Black Tree |
|-----------|--------|----------------|
| Branching factor | Large (50–2000) | 2 (binary) |
| Height | logₜ *n* (small base) | lg *n* |
| Disk accesses | O(logₜ *n*) — few | O(lg *n*) — more |
| Node size | One disk block | Small (fits in cache line) |
| Primary use | Disk-based storage (databases) | In-memory data structures |
| Growth direction | Top (root splits increase height) | Bottom |
| Node fullness | ≥ 50% (except root) | Always 1 key per node |

| Variant | Key feature |
|---------|-------------|
| **B-tree** (standard) | All nodes store keys + satellite info |
| **B+-tree** | Internal nodes: keys only; leaves: all satellite info |
| **B*-tree** | Internal nodes ≥ 2/3 full |
| **2-3-4 tree** | B-tree with *t=2* |

#### Edge Cases & Common Pitfalls

- **t = 1 not allowed**: Minimum degree *t* must be ≥ 2. Reason: with *t=1*, nodes would have 0 or 1 keys, which collapses to a binary tree with the B-tree overhead.
- **Root is special**: Can have as few as 1 key (even when *t > 2*). No other node can fall below *t−1*.
- **Splitting the root is the only height increase**: Unlike BSTs, B-trees grow at the top.
- **Deletion merges can cascade**: Cases 2c and 3b merge nodes, potentially emptying the root and decreasing height.
- **Deletion case 2a/2b may require two passes**: One pass down to find predecessor/successor, then back up to replace the key. But no full backtracking needed — just a pointer to the original node.
- **Redundant DISK-READ**: May occur if a block is already in memory. Exercise 18.2-2 explores this.
- **Binary search within nodes**: Using binary search instead of linear search (Exercise 18.2-6) makes CPU time O(lg *n*), independent of *t*.

#### End-of-Chapter Material

**Key terms**: B-tree, minimum degree, full node, B+-tree, B*-tree, 2-3-4 tree, disk block, DISK-READ, DISK-WRITE, split, merge, join, cache-oblivious.

**Review Exercises (selected)**:
- 18.1-1: Why is *t=1* not allowed? (Would give 0 keys minimum → degenerate.)
- 18.1-2: What *t* values make Fig 18.1 legal? (Each node has 1–3 keys, so *t=2* or *t=3*.)
- 18.1-3: All legal B-trees with *t=2* for keys {1,2,3,4,5}.
- 18.1-4: Max keys in B-tree height *h*, min degree *t*: *2tʰ⁺¹ − 1*.
- 18.2-1: Trace insert of F,S,Q,K,... into B-tree with *t=2*.
- 18.2-4: Number of nodes after inserting {1,…,n} into empty B-tree with *t=2*.
- 18.3-1: Delete C, P, V from Fig 18.8(f).
- 18.3-2: Write pseudocode for B-TREE-DELETE.

**Problems**:
- **18-1 Stacks on secondary storage**: Analyzing disk accesses for stack operations with one or two memory-resident blocks.
- **18-2 Joining and splitting 2-3-4 trees**: Implementing join (O(1+|h′−h″|)) and split (O(lg n)) for 2-3-4 trees.

---

### Ch. 19 — Data Structures for Disjoint Sets

#### Named Entities (Terms & Definitions)

- **Disjoint-set data structure**: Maintains a collection of disjoint dynamic sets. Supports MAKE-SET, UNION, FIND-SET.
- **Representative**: Some member of a set used to identify the set. Can be any member (idempotent: returns same value between modifications).
- **Connected components**: The equivalence classes of vertices in an undirected graph under the "reachable" relation.
- **Weighted-union heuristic**: When unioning two linked lists, always append the shorter list to the longer one.
- **Disjoint-set forest**: A rooted-tree representation where each tree represents one set, each node points to its parent, and the root is the representative.
- **Union by rank**: Heuristic making the root with smaller rank point to the root with larger rank. Rank is an upper bound on node height.
- **Path compression**: FIND-SET makes every node on the find path point directly to the root. Two-pass method: first pass up to find root, second pass down to update pointers.
- **Find path**: The simple path from a node to the root of its tree.
- **Ackermann-like function *Aₖ(j)***: A very quickly growing function used to define the inverse Ackermann.
- **Inverse Ackermann *α(n)***: The lowest level *k* for which *Aₖ(1) ≥ n*. Grows extremely slowly: *α(n) ≤ 4* for all practical values.
- **Level (of a nonroot node)**: The greatest *k* such that *Aₖ(x.rank) ≤ x.p.rank*.
- **iter(x)**: The largest number of times *Aₗₑᵥₑₗ₍ₓ₎* can be iteratively applied to *x.rank* without exceeding *x.p.rank*.
- **Offline minimum problem**: Given a sequence of INSERT and EXTRACT-MIN calls, determine which key each EXTRACT-MIN returns.
- **Depth-determination problem**: Maintain a forest of rooted trees with MAKE-TREE, FIND-DEPTH, and GRAFT operations.
- **Lowest common ancestor (LCA)**: The deepest node that is an ancestor of both *u* and *v* in a rooted tree.

#### Processes / Algorithms

##### CONNECTED-COMPONENTS (G)
- **Type**: Algorithm
- **Goal**: Compute connected components of an undirected graph using disjoint-set operations.
- **Steps**:
  1. For each vertex *v ∈ G.V*: MAKE-SET(*v*)
  2. For each edge (*u, v*) ∈ *G.E*:
     - If FIND-SET(*u*) ≠ FIND-SET(*v*): UNION(*u, v*)
- **Analysis**: FIND-SET called 2|E| times; UNION called ≤ |V|−1 times.

##### SAME-COMPONENT (u, v)
- **Type**: Query
- **Steps**: Return TRUE if FIND-SET(*u*) == FIND-SET(*v*), else FALSE.

##### Linked-List MAKE-SET (x)
- Steps: Create new linked list with single object *x*. Set *head = tail = x*. Set *x*'s set pointer to set object.
- **Cost**: O(1).

##### Linked-List FIND-SET (x)
- Steps: Follow pointer from *x* to set object, return *head* member.
- **Cost**: O(1).

##### Linked-List UNION (x, y) — Simple
- Steps: Append *y*'s list to end of *x*'s list. Use *tail* pointer of *x*'s list for O(1) append. Update set pointer for each element originally in *y*'s list.
- **Cost**: O(length of *y*'s list) — linear.
- **Worst-case sequence**: Θ(*n²*) for *n* MAKE-SET + (*n−1*) UNION (arithmetic series: 1+2+...+(n−1) = Θ(n²)).

##### Linked-List UNION with Weighted-Union Heuristic
- Steps: Always append the **shorter** list to the **longer** list (break ties arbitrarily). Maintain list length as attribute.
- **Cost per UNION**: O(length of shorter list).
- **Sequence bound** (Theorem 19.1): O(*m + n* lg *n*) for *m* operations, *n* MAKE-SET.
- **Proof intuition**: Each element's set-pointer is updated at most ⌈lg *n*⌉ times (doubling argument: each update moves it to a set at least twice as large).

##### Disjoint-Set Forest MAKE-SET (x)
- Steps:
  1. *x.p = x*
  2. *x.rank = 0*
- **Cost**: O(1).

##### Disjoint-Set Forest UNION (x, y)
- Steps: LINK(FIND-SET(*x*), FIND-SET(*y*)).
- Actual work is in FIND-SET calls + LINK.

##### LINK (x, y) (union by rank)
- **Precondition**: *x, y* are roots.
- Steps:
  1. If *x.rank > y.rank*: *y.p = x*
  2. Else: *x.p = y*
  3. If *x.rank == y.rank*: *y.rank = y.rank + 1*
- **Key point**: Only the root's rank can increase (by at most 1 per LINK). Ranks never decrease. Only roots have their rank incremented.

##### FIND-SET (x) with Path Compression
- **Type**: Two-pass algorithm (recursive)
- Steps:
  1. If *x ≠ x.p* (not root):
     - *x.p = FIND-SET(x.p)*   (recursive, compresses path on unwinding)
  2. Return *x.p*
- **Iterative version**: First pass to find root, second pass to redirect all nodes on path to root (Exercise 19.3-2).
- **Cost**: Linear in length of find path (amortized O(α(n))).

#### Disjoint-Set Forest (Union by Rank + Path Compression) — Complete Pseudocode

```
MAKE-SET(x)
    x.p = x
    x.rank = 0

UNION(x, y)
    LINK(FIND-SET(x), FIND-SET(y))

LINK(x, y)
    if x.rank > y.rank
        y.p = x
    else
        x.p = y
        if x.rank == y.rank
            y.rank = y.rank + 1

FIND-SET(x)
    if x ≠ x.p
        x.p = FIND-SET(x.p)
    return x.p
```

#### Formulas & Equations

##### The Ackermann-like Function *Aₖ(j)*
For integers *j, k ≥ 0*:

```
Aₖ(j) = |  j + 1                  if k = 0
        |  Aₖ₋₁⁽ʲ⁺¹⁾(j)           if k ≥ 1
```

Where *Aₖ₋₁⁽ⁱ⁾(j)* is functional iteration: *Aₖ₋₁⁽⁰⁾(j) = j*, *Aₖ₋₁⁽ⁱ⁾(j) = Aₖ₋₁(Aₖ₋₁⁽ⁱ⁻¹⁾(j))* for *i ≥ 1*.

**Closed forms**:
- *A₀(j) = j + 1*
- *A₁(j) = 2j + 1* (Lemma 19.2)
- *A₂(j) = 2ʲ⁺¹(j + 1) − 1* (Lemma 19.3)

**Key values of Aₖ(1)**:
- *A₀(1) = 2*
- *A₁(1) = 3*
- *A₂(1) = 7*
- *A₃(1) = 2047*
- *A₄(1) = 2²⁰⁵⁹ − 1 ≫ 10⁸⁰* (atoms in observable universe)

##### The Inverse Ackermann *α(n)*

> *α(n) = min { k : Aₖ(1) ≥ n }*

**Values**:
- *α(n) = 0* for *0 ≤ n ≤ 2*
- *α(n) = 1* for *3 ≤ n ≤ 3*
- *α(n) = 2* for *4 ≤ n ≤ 7*
- *α(n) = 3* for *8 ≤ n ≤ 2047*
- *α(n) = 4* for *2048 ≤ n ≤ A₄(1)* (essentially all practical *n*)

##### Disjoint-Set Complexity

| Implementation | Sequence of *m* ops, *n* MAKE-SET |
|---------------|--------------------------------------|
| Linked-list (simple UNION) | Θ(*n²*) worst case (amortized Θ(*n*) per op) |
| Linked-list (weighted union) | O(*m + n* lg *n*) |
| Forest (union by rank only) | O(*m* lg *n*) |
| Forest (path compression only) | Θ(*n + f*·(1+log₂₊*f/n* *n*)) |
| Forest (union by rank + path compression) | O(*m α(n)*) — asymptotically optimal |

#### Rules, Laws & Theorems

##### Theorem 19.1 (Weighted-Union Heuristic for Linked-List)
- **Statement**: Using linked-list representation with weighted-union heuristic, a sequence of *m* MAKE-SET, UNION, FIND-SET operations (*n* MAKE-SET) takes O(*m + n* lg *n*) time.
- **Proof**: Each element's pointer updated at most ⌈lg *n*⌉ times (doubling argument). Total UNION cost: O(*n* lg *n*). Each MAKE-SET/FIND-SET: O(1).

##### Lemma 19.2
- *A₁(j) = 2j + 1*
- Proof: Induction on *i* showing *A₀⁽ⁱ⁾(j) = j + i*, then *A₁(j) = A₀⁽ʲ⁺¹⁾(j) = j + (j+1) = 2j+1*.

##### Lemma 19.3
- *A₂(j) = 2ʲ⁺¹(j + 1) − 1*
- Proof: Induction on *i* showing *A₁⁽ⁱ⁾(j) = 2ⁱ(j + 1) − 1*, then *A₂(j) = A₁⁽ʲ⁺¹⁾(j) = 2ʲ⁺¹(j + 1) − 1*.

##### Lemma 19.4 (Rank Properties)
- For all nodes *x*: *x.rank ≤ x.p.rank*, strict if *x* is not a root.
- *x.rank* starts at 0, increases until *x* becomes a nonroot, then never changes.
- *x.p.rank* monotonically increases.

##### Corollary 19.5
- On the simple path from any node to a root, ranks strictly increase.

##### Lemma 19.6
- Every node has rank at most *n − 1* (weak bound; actually ≤ ⌊lg *n*⌋ per Exercise 19.4-2).

##### Lemma 19.7 (Conversion Lemma)
- Converting each UNION into 2 FIND-SET + 1 LINK changes *m'* → *m* where *m = Θ(m')*. Proving O(*m α(n)*) for converted sequence implies O(*m' α(n)*) for original.

##### Lemma 19.8
- For every node *x* and operation count *q*: 0 ≤ *ϕₚ(x)* ≤ *α(n) · x.rank*.

##### Corollary 19.9
- If *x* is not a root and *x.rank > 0*: *ϕₚ(x) < α(n) · x.rank*.

##### Lemma 19.10 (Potential Change)
- For nonroot *x* during LINK or FIND-SET: *ϕₚ(x) ≤ ϕₚ₋₁(x)*. If *x.rank ≥ 1* and level(*x*) or iter(*x*) changes, potential drops by ≥ 1.

##### Lemma 19.11
- Amortized cost of MAKE-SET: O(1).

##### Lemma 19.12
- Amortized cost of LINK: O(*α(n)*).

##### Lemma 19.13
- Amortized cost of FIND-SET: O(*α(n)*).
- Proof: Actual cost O(*s*) (find path length). At least *s − (α(n) + 2)* nodes have potential drop ≥ 1. Amortized = O(*s*) − (*s* − *α(n)* − 2) = O(*α(n)*).

##### Theorem 19.14 (Final Bound)
- A sequence of *m* MAKE-SET, UNION, FIND-SET operations (*n* MAKE-SET) on a disjoint-set forest with union by rank and path compression runs in O(*m α(n)*) time.

#### Potential Function (for Amortized Analysis)

**Node potential** *ϕₚ(x)* after *q* operations:
- If *x* is a root or *x.rank = 0*: *ϕₚ(x) = α(n) · x.rank*
- If *x* is not a root and *x.rank ≥ 1*:

  > *ϕₚ(x) = (α(n) − level(x)) · x.rank − iter(x)*

**Auxiliary functions**:
- *level(x) = max {k : Aₖ(x.rank) ≤ x.p.rank}*
  - Bounds: 0 ≤ *level(x) < α(n)*
- *iter(x) = max {i : Aₗₑᵥₑₗ₍ₓ₎⁽ⁱ⁾(x.rank) ≤ x.p.rank}*
  - Bounds: 1 ≤ *iter(x) ≤ x.rank*

**Total potential**: *Φₚ = Σₓ ϕₚ(x)*, with *Φ₀ = 0*. No potential is ever negative.

#### Data Structures

##### Linked-List Representation
- **Structure**: Each set = singly linked list. Set object has *head* and *tail*. Each element has pointer to set object + next pointer.
- **Representative**: First element in list.
- **Costs**: MAKE-SET O(1), FIND-SET O(1), UNION O(length of appended list).
- **Weighted-union**: Append shorter list to longer. Maintain length attribute. Sequence cost: O(*m + n* lg *n*).

##### Disjoint-Set Forest
- **Structure**: Rooted trees. Each node has *parent* pointer and *rank*. Root = representative (parent of itself).
- **Heuristics**: Union by rank (shorter tree → taller); Path compression (FIND-SET flattens).
- **Costs**: MAKE-SET O(1), UNION O(α(n)) amortized, FIND-SET O(α(n)) amortized.
- **Overall**: O(*m α(n)*) for *m* operations.

#### Comparisons & Trade-offs

| Dimension | Linked-List (Weighted) | Forest (Union by Rank + PC) |
|-----------|----------------------|------------------------------|
| MAKE-SET | O(1) | O(1) |
| FIND-SET | O(1) | O(α(n)) amortized |
| UNION | O(lg n) amortized | O(α(n)) amortized |
| Sequence of m ops | O(m + n lg n) | O(m α(n)) |
| Space per element | 2 pointers (set + next) | 2 fields (parent + rank) |
| Practical speed | Simple, good for small n | Best asymptotic; α(n) ≤ 4 |
| Central operation | Pointer updates on union | Path compression on find |

#### Proof & Argument Patterns

- **Doubling argument (weighted union)**: Each time an element's pointer updates, its set size at least doubles → ≤ ⌈lg *n*⌉ updates per element.
- **Inverse Ackermann bound**: Complex amortized analysis using potential function with level(*x*) and iter(*x*). Only nodes where level/iter change contribute potential drop. At most *α(n)* nodes per find path don't have such a change.
- **Rank monotonicity**: Ranks strictly increase along any rootward path (Corollary 19.5).
- **Conversion lemma**: UNION → 2 FIND-SET + 1 LINK preserves asymptotic complexity.

#### Edge Cases & Common Pitfalls

- **Make-set assumes element not already in a set**: Precondition of MAKE-SET(*x*) is that *x* does not belong to any other set.
- **Union destroys old sets**: After UNION, the two original sets no longer exist as separate entities.
- **Maximum UNIONS**: At most *n−1* UNION operations (each reduces set count by 1).
- **Union by rank vs. union by size**: CLRS uses union by rank (easier analysis), but union by size (actual subtree size) works similarly.
- **Path compression doesn't change ranks**: Ranks are upper bounds on height, not exact heights. After path compression, actual height may be much less than rank.
- **Rank only increases during LINK**: FIND-SET (even with path compression) never changes ranks.
- **α(n) > 4 for astronomically large n**: Practical *n* always has *α(n) ≤ 4*. The O(*m α(n)*) bound is essentially linear.
- **One-pass path compression**: There exist variants that sometimes have better constant factors (Tarjan–van Leeuwen).

#### Case Studies & Examples

##### Connected Components
- **Input**: Graph *G = (V, E)*. **Output**: Component membership.
- **Process**: MAKE-SET for each vertex; for each edge (*u,v*), union if in different sets.
- **Complexity**: O((|V|+|E|) α(|V|)) using forest.
- **Alternative**: DFS is faster for static graphs (O(|V|+|E|)). Disjoint-set excels when edges are added dynamically.

##### Offline Minimum (Problem 19-1)
- **Problem**: Sequence of INSERT and EXTRACT-MIN calls; each key in {1,…,n} inserted exactly once. Determine which key each EXTRACT-MIN returns.
- **Algorithm (OFFLINE-MINIMUM)**:
  - Partition sequence: *I₁, E, I₂, E, …, Iₘ, E, Iₘ₊₁* where each *Iⱼ* is (possibly empty) sequence of INSERTs.
  - Place keys of *Iⱼ* into set *Kⱼ*.
  - For *i = 1* to *n*: find *j* with *i ∈ Kⱼ*; if *j ≤ m*, set *extracted[j] = i*; merge *Kⱼ* into *Kₗ* where *l* = smallest > *j* with nonempty set.
  - Implement efficiently with disjoint-set data structure.

##### Tarjan's Offline LCA (Problem 19-3)
- **Problem**: Given rooted tree *T* and set of unordered pairs *P*, find LCA of each pair.
- **Algorithm (LCA)**: Tree walk. MAKE-SET for each node when first visited. UNION with parent after processing children. When a node turns BLACK, answer queries: for each *v* where {*u, v*} ∈ *P* and *v* is BLACK, LCA = FIND-SET(*v*).ancestor.
- **Complexity**: O((|T| + |P|) α(|T|)) with disjoint-set forest.

#### End-of-Chapter Material

**Key terms**: disjoint-set data structure, representative, MAKE-SET, UNION, FIND-SET, connected components, weighted-union heuristic, disjoint-set forest, union by rank, path compression, find path, Ackermann's function, inverse Ackermann, level, iter, offline minimum, depth-determination, lowest common ancestor.

**Review Exercises (selected)**:
- 19.1-1: Trace CONNECTED-COMPONENTS on given graph.
- 19.1-3: FIND-SET called 2|E| times; UNION called |V| − *k* (*k* = number of connected components).
- 19.2-1: Write pseudocode for linked-list MAKE-SET, FIND-SET, UNION with weighted-union heuristic.
- 19.2-4: Tight bound for Fig 19.3 with weighted union: O(*n* lg *n*).
- 19.3-1: Trace disjoint-set forest with union by rank + path compression.
- 19.3-2: Write nonrecursive FIND-SET with path compression.
- 19.3-4: Add a "next" pointer in each node to allow linear-time PRINT-SET.
- 19.4-1: Prove Lemma 19.4 (rank properties).
- 19.4-2: Prove max rank ≤ ⌊lg *n*⌋.
- 19.4-3: ⌊lg *n*⌋ bits needed to store rank.
- 19.4-6: Scale potential function by constant *c* to dominate O(*s*) term.

**Problems**:
- **19-1 Offline minimum**: Implement with disjoint-set; nearly linear.
- **19-2 Depth determination**: Maintain pseudodistance *v.d* such that sum along find path = depth. Implement FIND-DEPTH using modified FIND-SET, GRAFT using modified UNION/LINK. Total: O(*m α(n)*).
- **19-3 Tarjan's offline LCA**: Elegant O((|T|+|P|) α(|T|)) algorithm using disjoint sets.

---

## Cross-Cutting Topics

### Design Paradigms & Meta-Methods

- **Augmentation (Ch 17)**: Generic 4-step method: choose base structure → decide extra info → verify maintainability → develop new ops. Theorem 17.1 guarantees RB tree augmentation works if *x.f* depends only on O(1)-computable info from *x*, *x.left*, *x.right*.
- **Preemptive splitting (Ch 18)**: Split full nodes on the way down during insertion → no need to backtrack. One-pass algorithm.
- **Preemptive merging/borrowing (Ch 18)**: During deletion, ensure each visited node has ≥ *t* keys on the way down → no backtracking.
- **Inverse Ackermann trick (Ch 19)**: Use extremely slow-growing function to prove essentially linear time. The potential function uses node ranks and "levels" defined via *Aₖ*.

### Proof & Argument Patterns

- **Augmentation correctness (Theorem 17.1)**: Local changes propagate up ancestors only. Constant rotations keep total O(lg *n*).
- **B-tree height bound (Theorem 18.1)**: Minimum number of nodes at each depth → lower bound on *n* → *h* ≤ logₜ((*n*+1)/2).
- **Doubling argument (Theorem 19.1)**: Each pointer update doubles the size of the set containing the element → ≤ lg *n* updates per element.
- **Potential method (Ch 19.4)**: Complex potential function using level(*x*) and iter(*x*). Amortized cost = actual + ΔΦ. FIND-SET O(α(n)) by charging potential drops against work.
- **Interval search correctness (Theorem 17.2)**: Show both search directions are safe using interval trichotomy + max attribute.

### People & Dates

- **J. E. Hopcroft (1970)**: Invented 2-3 trees, precursor to B-trees.
- **Bayer and McCreight (1972)**: Introduced B-trees. Origin of the name is unexplained.
- **R. E. Tarjan**: Pioneered disjoint-set analysis. First tight upper bound using inverse Ackermann. Also developed offline LCA algorithm.
- **Hopcroft and Ullman**: Proved O(*m* lg* n*) bound for disjoint sets (before Tarjan's tighter bound).
- **H. Edelsbrunner (1980), E. M. McCreight (1981)**: Pioneering work on interval trees.
- **Kozen**: Alternative analysis of disjoint-set forests.
- **Tarjan and van Leeuwen**: One-pass path compression variants.
- **Fredman and Saks**: Lower bound on disjoint-set data structures.

---

## Exam Questions by Type

### MCQ

1. **Q:** What is the running time of OS-SELECT on an order-statistic tree of *n* nodes?
   - **A:** O(lg *n*)
   - **Distractor:** O(*n*) — confuses with unsorted array selection (Chapter 9).
   - **Distractor:** O(*n* lg *n*) — confuses with sorting.

2. **Q:** What is the minimum number of keys in a B-tree node (except the root) with minimum degree *t*?
   - **A:** *t − 1*
   - **Distractor:** *t* — confuses with minimum children count for internal nodes.
   - **Distractor:** *2t − 1* — that's the maximum (full node).

3. **Q:** Which operation is the ONLY way a B-tree increases in height?
   - **A:** Splitting the root.
   - **Distractor:** Inserting into a leaf — BST growth model, incorrect for B-trees.
   - **Distractor:** Merging during deletion — that decreases height.

4. **Q:** What is α(10¹⁰⁰) (the inverse Ackermann function)?
   - **A:** 4 (since *A₄(1)* ≥ 10¹⁰⁰)
   - **Distractor:** 3 — *A₃(1)* = 2047, too small.
   - **Distractor:** 5 — *A₄(1)* already exceeds any practical *n*.

5. **Q:** In a disjoint-set forest with union by rank and path compression, what is the amortized time per operation?
   - **A:** O(α(n))
   - **Distractor:** O(lg *n*) — that's without path compression.
   - **Distractor:** O(1) — close in practice but not theoretically for all cases.

6. **Q:** What starts at 0, increases until a node becomes a nonroot, then never changes?
   - **A:** The node's *rank*.
   - **Distractor:** The node's *level* — level can change even for nonroots.
   - **Distractor:** The node's *iter* — iter can change even for nonroots.

7. **Q:** If *x* is a root or *x.rank = 0*, then *ϕₚ(x)* in the disjoint-set potential function equals what?
   - **A:** *α(n) · x.rank*
   - **Distractor:** *(α(n) − level(x)) · x.rank − iter(x)* — that's for nonroot nodes with rank ≥ 1.
   - **Distractor:** *x.rank* — missing the *α(n)* factor.

8. **Q:** What is the maximum number of rotations that can occur during a single insertion into a red-black tree (and thus in an order-statistic tree or interval tree)?
   - **A:** 2
   - **Distractor:** 3 — that's the limit for deletion.
   - **Distractor:** O(lg *n*) — confuses with other balanced tree schemes.

### Short Answer

1. **Q:** State the 4 steps for augmenting a data structure.
   - **Rubric:** (1) Choose underlying data structure. (2) Determine additional info to maintain. (3) Verify maintainability. (4) Develop new operations.

2. **Q:** State the interval trichotomy.
   - **Rubric:** For any two closed intervals *i*, *i'*, exactly one holds: (a) they overlap; (b) *i* is to the left of *i'* (*i.high < i'.low*); (c) *i* is to the right of *i'* (*i'.high < i.low*).

3. **Q:** State the 5 properties of a B-tree.
   - **Rubric:** (1) Each node has *n* keys, monotonic, plus *leaf* flag. (2) Internal nodes have *n+1* children. (3) Keys separate subtree key ranges. (4) All leaves at same depth. (5) Node bounds: ≥ *t−1* keys (except root), ≤ *2t−1* keys.

4. **Q:** In B-TREE-DELETE, what invariant is maintained for every visited node (except possibly the root)?
   - **Rubric:** The node must have at least *t* keys (one more than the minimum *t−1*), to prevent underflow during recursion.

5. **Q:** Compare linked-list vs. forest implementations of disjoint sets: give the asymptotic bound for a sequence of *m* operations (*n* MAKE-SET).
   - **Rubric:** Weighted linked-list: O(*m + n* lg *n*). Forest with union by rank + path compression: O(*m α(n)*).

### Trace / Apply

1. **Input:** Order-statistic tree from Fig 17.1. Apply OS-SELECT(T.root, 17). **Expected output:** Node with key 38. **Why:** Trace as shown in chapter.

2. **Input:** B-tree with *t=2*, sequence of keys: F, S, Q, K, C, L, H, T, V, W, M, R, N, P, A, B, X, Y, D, Z, E. Apply B-TREE-INSERT in order. **Expected output:** Final B-tree configuration from Exercise 18.2-1.

3. **Input:** Linked-list disjoint set with weighted union, sequence from Exercise 19.2-2. Show data structure after each operation. **Expected output:** Final FIND-SET(x₂) returns representative of set containing x₁.

4. **Input:** Graph with edges (d,i), (f,k), (g,i), etc., from Exercise 19.1-1. Apply CONNECTED-COMPONENTS. **Expected output:** List vertices in each component after each edge.

### Essay / Long-Form

1. **Q:** Prove Theorem 18.1 (B-tree height bound). **Key points:** Tree with minimum nodes, root has ≥1 key, other nodes have ≥ *t−1* keys, count nodes per depth (≥ 2 at depth 1, ≥ 2*t* at depth 2, etc.), sum geometric series, derive *n ≥ 2tʰ − 1*, rearrange to *h ≤ logₜ((n+1)/2)*.

2. **Q:** Explain the amortized analysis of FIND-SET with path compression and union by rank, proving O(*α(n)*) amortized time. **Key points:** Potential function with level(*x*), iter(*x*), Lemma 19.10 (potential does not increase for nonroots, drops by ≥1 when level/iter changes), at most *α(n)+2* nodes on find path without potential drop, amortized cost = O(*s*) − (*s* − *α(n)* − 2) = O(*α(n)*).

3. **Q:** Describe the B-TREE-DELETE procedure with all cases. **Key points:** Case 1 (leaf), Case 2a (predecessor), Case 2b (successor), Case 2c (merge), Case 3a (borrow from sibling), Case 3b (merge with sibling), root emptying, single downward pass invariant (≥ *t* keys in visited nodes).

4. **Q:** Prove Theorem 19.1 (weighted-union heuristic for linked-list disjoint sets). **Key points:** Each element's set-pointer updated ≤ ⌈lg *n*⌉ times (doubling: each update moves to set ≥ 2× previous size), *n* elements → O(*n* lg *n*) total pointer updates, plus O(1) per MAKE-SET and FIND-SET, O(1) per UNION for tail/length updates → O(*m* + *n* lg *n*).
