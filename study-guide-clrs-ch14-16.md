# Study Guide: CLRS 4e — Part IV: Advanced Design and Analysis Techniques (Ch 14–16)

> Generated 2026-06-04. Subject: Computer Science (Algorithms). Exam format: Problem-solving / Short answer / Trace. Coverage: comprehensive.

---

## Ch. 14 — Dynamic Programming

### Named Entities (Terms & Definitions)

- **Dynamic Programming**: A method for solving problems by combining solutions to overlapping subproblems, solving each subproblem only once and storing its answer in a table.
- **Optimal Substructure**: An optimal solution to a problem contains within it optimal solutions to subproblems.
- **Overlapping Subproblems**: The space of subproblems is small such that a recursive algorithm solves the same subproblems repeatedly.
- **Memoization**: A top-down technique that saves the result of each subproblem (usually in an array or hash table) on first computation; subsequent calls simply look up the saved value.
- **Bottom-Up Method**: Solves subproblems in size order, smallest first, storing solutions as they are computed.
- **Subproblem Graph**: A directed graph where each vertex is a distinct subproblem, and edges indicate dependencies (solving subproblem x requires solution to subproblem y).
- **Rod-Cutting Problem**: Given a rod of length n and a price table pi for i=1,...,n, determine the maximum revenue rn obtainable by cutting up the rod and selling pieces.
- **Matrix-Chain Multiplication Problem**: Given a chain of n matrices with dimensions pi−1 × pi, fully parenthesize the product to minimize scalar multiplications.
- **Longest Common Subsequence (LCS) Problem**: Given two sequences X and Y, find a maximum-length common subsequence.
- **Optimal Binary Search Tree (OBST)**: Given keys k1<...<kn with probabilities pi (successful search) and dummy keys d0,...,dn with probabilities qi (unsuccessful search), construct a BST minimizing expected search cost.
- **Prefix**: Xi = ⟨x1, x2, ..., xi⟩, the first i elements of sequence X; X0 is empty.
- **Fully Parenthesized**: A product of matrices is fully parenthesized if it is either a single matrix or the product of two fully parenthesized matrix products, surrounded by parentheses.
- **Catalan Numbers**: The number of ways to parenthesize n matrices is the Catalan number, growing as Ω(4^n / n^(3/2)).
- **tD/eD Classification**: A dynamic-programming algorithm is called tD/eD if its table size is O(n^t) and each entry depends on O(n^e) other entries (e.g., matrix-chain is 2D/1D, LCS is 2D/0D).
- **Cut-and-Paste Argument**: Proof technique: assume a subproblem solution is not optimal, cut it out and paste in a better one to derive a contradiction with the optimality of the original solution.

### Processes / Algorithms / Pseudocode

#### CUT-ROD (naive recursive)
```
CUT-ROD(p, n)
1 if n == 0
2     return 0
3 q = -∞
4 for i = 1 to n
5     q = max{q, p[i] + CUT-ROD(p, n - i)}
6 return q
```
- **Goal**: Compute max revenue for rod length n
- **Complexity**: T(0)=1, T(n)=1 + Σ_{j=0}^{n-1} T(j) ⇒ T(n)=2^n — exponential
- **Why slow**: Solves same subproblems repeatedly (recursion tree has 2^n nodes, 2^(n−1) leaves)

#### MEMOIZED-CUT-ROD (top-down DP)
```
MEMOIZED-CUT-ROD(p, n)
1 let r[0:n] be a new array
2 for i = 0 to n
3     r[i] = -∞
4 return MEMOIZED-CUT-ROD-AUX(p, n, r)

MEMOIZED-CUT-ROD-AUX(p, n, r)
1 if r[n] ≥ 0
2     return r[n]
3 if n == 0
4     q = 0
5 else q = -∞
6 for i = 1 to n
7     q = max{q, p[i] + MEMOIZED-CUT-ROD-AUX(p, n - i, r)}
8 r[n] = q
9 return q
```
- **Complexity**: Θ(n^2) — solves each of n+1 subproblems once, each takes O(n) iterations

#### BOTTOM-UP-CUT-ROD (bottom-up DP)
```
BOTTOM-UP-CUT-ROD(p, n)
1 let r[0:n] be a new array
2 r[0] = 0
3 for j = 1 to n
4     q = -∞
5     for i = 1 to j
6         q = max{q, p[i] + r[j - i]}
7     r[j] = q
8 return r[n]
```
- **Complexity**: Θ(n^2) — doubly nested loop forming arithmetic series

#### EXTENDED-BOTTOM-UP-CUT-ROD (reconstructs solution)
```
EXTENDED-BOTTOM-UP-CUT-ROD(p, n)
1 let r[0:n] and s[1:n] be new arrays
2 r[0] = 0
3 for j = 1 to n
4     q = -∞
5     for i = 1 to j
6         if q < p[i] + r[j - i]
7             q = p[i] + r[j - i]
8             s[j] = i
9     r[j] = q
10 return r and s

PRINT-CUT-ROD-SOLUTION(p, n)
1 (r, s) = EXTENDED-BOTTOM-UP-CUT-ROD(p, n)
2 while n > 0
3     print s[n]
4     n = n - s[n]
```
- **s[j]** stores optimal size of first piece to cut off for rod length j

#### RECTANGULAR-MATRIX-MULTIPLY
```
RECTANGULAR-MATRIX-MULTIPLY(A, B, C, p, q, r)
1 for i = 1 to p
2     for j = 1 to r
3         for k = 1 to q
4             cij = cij + aik · bkj
```
- **Cost**: pqr scalar multiplications
- A is p×q, B is q×r, C is p×r

#### MATRIX-CHAIN-ORDER (bottom-up DP)
```
MATRIX-CHAIN-ORDER(p, n)
1 let m[1:n, 1:n] and s[1:n-1, 2:n] be new tables
2 for i = 1 to n
3     m[i, i] = 0
4 for l = 2 to n          // l is chain length
5     for i = 1 to n - l + 1
6         j = i + l - 1
7         m[i, j] = ∞
8         for k = i to j - 1
9             q = m[i, k] + m[k+1, j] + p[i-1]*p[k]*p[j]
10            if q < m[i, j]
11                m[i, j] = q
12                s[i, j] = k
13 return m and s
```
- **Input**: sequence p = ⟨p0, p1, ..., pn⟩ of matrix dimensions
- **Output**: m[1,n] = minimum scalar multiplications; s[i,j] = optimal split point k
- **Complexity**: Time Θ(n^3), Space Θ(n^2) (for both m and s)
- **Fill order**: by increasing chain length l = 2, 3, ..., n
- **Subproblem size**: chain length j−i+1

#### PRINT-OPTIMAL-PARENS
```
PRINT-OPTIMAL-PARENS(s, i, j)
1 if i == j
2     print "A" i
3 else print "("
4     PRINT-OPTIMAL-PARENS(s, i, s[i, j])
5     PRINT-OPTIMAL-PARENS(s, s[i, j] + 1, j)
6     print ")"
```
- Initial call: PRINT-OPTIMAL-PARENS(s, 1, n)

#### RECURSIVE-MATRIX-CHAIN (naive, exponential)
```
RECURSIVE-MATRIX-CHAIN(p, i, j)
1 if i == j
2     return 0
3 m[i, j] = ∞
4 for k = i to j - 1
5     q = RECURSIVE-MATRIX-CHAIN(p, i, k)
6       + RECURSIVE-MATRIX-CHAIN(p, k+1, j)
7       + p[i-1]*p[k]*p[j]
8     if q < m[i, j]
9         m[i, j] = q
10 return m[i, j]
```
- **Complexity**: T(1)≥1, T(n)=1+Σ_{k=1}^{n-1}(T(k)+T(n−k)+1) ⇒ T(n)=Ω(2^n)

#### MEMOIZED-MATRIX-CHAIN (top-down DP)
```
MEMOIZED-MATRIX-CHAIN(p, n)
1 let m[1:n, 1:n] be a new table
2 for i = 1 to n
3     for j = i to n
4         m[i, j] = ∞
5 return LOOKUP-CHAIN(m, p, 1, n)

LOOKUP-CHAIN(m, p, i, j)
1 if m[i, j] < ∞
2     return m[i, j]
3 if i == j
4     m[i, j] = 0
5 else for k = i to j - 1
6     q = LOOKUP-CHAIN(m, p, i, k)
7       + LOOKUP-CHAIN(m, p, k+1, j) + p[i-1]*p[k]*p[j]
8     if q < m[i, j]
9         m[i, j] = q
10 return m[i, j]
```
- **Complexity**: O(n^3) — Θ(n^2) calls of first type, each makes O(n) recursive calls

#### LCS-LENGTH
```
LCS-LENGTH(X, Y, m, n)
1 let b[1:m, 1:n] and c[0:m, 0:n] be new tables
2 for i = 1 to m
3     c[i, 0] = 0
4 for j = 0 to n
5     c[0, j] = 0
6 for i = 1 to m
7     for j = 1 to n
8         if x_i == y_j
9             c[i, j] = c[i-1, j-1] + 1
10            b[i, j] = "↖"
11        elseif c[i-1, j] ≥ c[i, j-1]
12            c[i, j] = c[i-1, j]
13            b[i, j] = "↑"
14        else
15            c[i, j] = c[i, j-1]
16            b[i, j] = "←"
17 return c and b
```
- **Complexity**: Θ(mn) time, Θ(mn) space
- **Fill order**: row-major (top to bottom, left to right)
- **c[i,j]** = length of LCS of Xi and Yj

#### PRINT-LCS
```
PRINT-LCS(b, X, i, j)
1 if i == 0 or j == 0
2     return
3 if b[i, j] == "↖"
4     PRINT-LCS(b, X, i-1, j-1)
5     print x_i
6 elseif b[i, j] == "↑"
7     PRINT-LCS(b, X, i-1, j)
8 else
9     PRINT-LCS(b, X, i, j-1)
```
- Initial call: PRINT-LCS(b, X, m, n)
- **Complexity**: O(m+n)
- **Space optimization**: Can eliminate b table by checking which of the three neighbors gave c[i,j] — reconstruct in O(m+n) time from c alone

#### OPTIMAL-BST
```
OPTIMAL-BST(p, q, n)
1 let e[1:n+1, 0:n], w[1:n+1, 0:n], and root[1:n, 1:n] be new tables
2 for i = 1 to n+1
3     e[i, i-1] = q[i-1]
4     w[i, i-1] = q[i-1]
5 for l = 1 to n
6     for i = 1 to n - l + 1
7         j = i + l - 1
8         e[i, j] = ∞
9         w[i, j] = w[i, j-1] + p[j] + q[j]
10        for r = i to j
11            t = e[i, r-1] + e[r+1, j] + w[i, j]
12            if t < e[i, j]
13                e[i, j] = t
14                root[i, j] = r
15 return e and root
```
- **Goal**: Compute e[1,n] = expected search cost of optimal BST
- **Complexity**: Θ(n^3) time, Θ(n^2) space
- Knuth optimization: root[i, j-1] ≤ root[i, j] ≤ root[i+1, j] ⇒ reduces to Θ(n^2) time

### Formulas & Equations

#### Rod Cutting

**Number of cut patterns**: 2^(n−1) possible ways to cut a rod of length n (each of n−1 cut positions chosen independently)

**Revenue recurrence (two-subproblem formulation)**:
```
r_n = max_{1 ≤ i ≤ n} (p_i + r_{n-i})
```
where r_0 = 0.

**Revenue recurrence (first-piece formulation)**:
```
r_n = max_{1 ≤ i ≤ n} (p_i + r_{n-i})
```
with r_0 = 0.

**Running time of naive CUT-ROD**:
```
T(0) = 1
T(n) = 1 + Σ_{j=0}^{n-1} T(j)
```
Solution: T(n) = 2^n.

#### Matrix-Chain Multiplication

**Recurrence for m[i,j] (min scalar multiplications for Ai..j)**:
```
m[i, j] = 0                                          if i = j
m[i, j] = min_{i ≤ k < j} {m[i, k] + m[k+1, j] + p_{i-1} p_k p_j}   if i < j
```

**s[i,j]**: value of k achieving the minimum for m[i,j].

**Number of distinct subproblems**: Θ(n^2) = n + C(n,2) = n(n+1)/2.

**Number of parenthesizations P(n)**:
```
P(1) = 1
P(n) = Σ_{k=1}^{n-1} P(k) P(n-k)    for n ≥ 2
```
This is the Catalan number: P(n) = C_{n-1} = (1/n) * C(2n-2, n-1) = Ω(4^n / n^(3/2)).

**T(n) for recursive matrix-chain**:
```
T(1) ≥ 1
T(n) ≥ 1 + Σ_{k=1}^{n-1} (T(k) + T(n-k) + 1)
```
Solution: T(n) = Ω(2^n).

#### Longest Common Subsequence

**Recurrence for c[i,j] (length of LCS of Xi and Yj)**:
```
c[i, j] = 0                                          if i=0 or j=0
c[i, j] = c[i-1, j-1] + 1                            if i,j>0 and x_i = y_j
c[i, j] = max(c[i-1, j], c[i, j-1])                  if i,j>0 and x_i ≠ y_j
```

**Number of distinct subproblems**: Θ(mn).

#### Optimal Binary Search Tree

**Sum of probabilities in subtree**:
```
w[i, j] = Σ_{l=i}^{j} p_l + Σ_{l=i-1}^{j} q_l
```

**Recurrence for e[i,j] (expected search cost)**:
```
e[i, j] = q_{i-1}                                    if j = i-1 (dummy key only)
e[i, j] = min_{i ≤ r ≤ j} {e[i, r-1] + e[r+1, j] + w[i, j]}   if i ≤ j
```
where w(i,j) = w(i,j-1) + p_j + q_j.

**e[1,n]** = minimum expected search cost for all keys.

**root[i,j]**: index r of the root key in optimal BST for keys ki..kj.

### Rules, Laws & Theorems

**Theorem 14.1 (Optimal substructure of an LCS)**: Let X=⟨x1...xm⟩, Y=⟨y1...yn⟩, and let Z=⟨z1...zk⟩ be any LCS of X and Y.

1. If xm = yn, then zk = xm = yn and Z_{k-1} is an LCS of X_{m-1} and Y_{n-1}.
2. If xm ≠ yn and zk ≠ xm, then Z is an LCS of X_{m-1} and Y.
3. If xm ≠ yn and zk ≠ yn, then Z is an LCS of X and Y_{n-1}.

**Four-step DP method**:
1. Characterize the structure of an optimal solution.
2. Recursively define the value of an optimal solution.
3. Compute the value of an optimal solution (typically bottom-up).
4. Construct an optimal solution from computed information.

### Comparisons & Trade-offs

| Dimension | Dynamic Programming | Greedy Algorithms |
|---|---|---|
| Choice depends on | Solutions to subproblems | Only local information |
| Direction | Bottom-up or top-down with memoization | Usually top-down |
| Subproblems | Considers all possible subproblems | Solves one remaining subproblem |
| When to use | Overlapping subproblems + optimal substructure | Greedy-choice property + optimal substructure |
| Example | 0-1 knapsack, matrix-chain | Activity selection, fractional knapsack |

| Dimension | Top-down (Memoization) | Bottom-up |
|---|---|---|
| Approach | Recursive, saves results | Iterative, solves smallest first |
| Overhead | Recursion + table maintenance | Lower constant factors |
| Subproblems solved | Only those needed | All relevant ones |
| When preferred | Some subproblems may not be needed | All subproblems must be solved |

| Dimension | DP | Divide-and-Conquer |
|---|---|---|
| Subproblems | Overlapping (share subsubproblems) | Disjoint |
| Efficiency concern | Repeated work | Recursion overhead |
| Example | Matrix-chain multiplication | Merge sort |

| Dimension | 0-1 Knapsack | Fractional Knapsack |
|---|---|---|
| Item choice | Take or leave whole item | Take fractions allowed |
| Solvable by greedy? | No | Yes (value per pound) |
| DP solvable? | Yes (O(nW)) | N/A |

### Edge Cases & Common Pitfalls

- **Optimal substructure does NOT hold for longest simple path** in an unweighted directed graph — subproblems are not independent (share vertices)
- **DP vs greedy confusion**: Not all problems with optimal substructure work with greedy; the greedy-choice property must also hold
- **Rod cutting exponential**: Naive recursive CUT-ROD is 2^n, not polynomial — only DP makes it Θ(n^2)
- **OBST ≠ minimum height tree**: An optimal BST does not necessarily have minimal height or the highest-probability key at root
- **Matrix-chain**: The optimal split k may not minimize the immediate cost p_{i-1}p_kp_j — greedy split fails
- **LCS with equal keys**: When equal keys exist, rank in an order-statistic tree is defined by inorder walk position
- **Subproblem independence**: For DP to work, subproblems must be independent (no shared resources)

### Proof & Argument Patterns

**Cut-and-Paste (Optimal Substructure Proof Template)**:
1. Suppose an optimal solution to a problem contains a choice that leads to subproblems.
2. Assume for contradiction that one subproblem solution used in the optimal solution is NOT optimal.
3. "Cut out" the nonoptimal subproblem solution.
4. "Paste in" the optimal solution to that subproblem.
5. Show this yields a better solution to the original problem, contradicting optimality.

**Example: Rod cutting** — If an optimal solution for rod length n cuts off a first piece of length i, the remaining piece of length n−i must be cut optimally.

**Example: Matrix-chain** — If optimal parenthesization of Ai..j splits at k, then the parenthesizations of Ai..k and A(k+1)..j must be optimal.

**Example: Shortest path** — If p is a shortest path from u to v with intermediate vertex w, then subpaths u→w and w→v are shortest paths (cut-and-paste works because subpaths are independent — they share no vertices other than w).

**Example: Longest simple path** — CUT-AND-PASTE FAILS because subpaths may share vertices, violating independence.

### Design Paradigms

**Dynamic Programming: Two implementation approaches**:
1. **Top-down with memoization**: Write recursive procedure, save results in array/hash table; check before computing.
2. **Bottom-up method**: Determine "size" ordering of subproblems; solve smallest first, storing results; look up when needed.

**When DP applies**:
- **Optimal substructure** ✓ (optimal solution built from optimal sub-solutions)
- **Overlapping subproblems** ✓ (same subproblems recur; small number of distinct subproblems — polynomial in input size)

**Running time heuristic**: O(#subproblems × #choices per subproblem). More precisely, running time is linear in size of subproblem graph (vertices + edges).

**Subproblem graph interpretation**:
- Bottom-up = reverse topological sort of subproblem graph
- Top-down with memoization = depth-first search of subproblem graph

### End-of-Chapter Material

#### Key terms
dynamic programming, optimal substructure, overlapping subproblems, memoization, bottom-up method, subproblem graph, rod-cutting problem, matrix-chain multiplication, longest common subsequence, optimal binary search tree, prefix, Catalan numbers, cut-and-paste argument

#### Selected Exercises
- **14.1-2**: Show greedy by density (max pi/i) fails for rod cutting (counterexample)
- **14.1-3**: Modify rod cutting: each cut costs c — DP algorithm
- **14.1-4**: Optimize CUT-ROD loops to ⌊n/2⌋
- **14.1-6**: DP for Fibonacci in O(n) time; subproblem graph has n+1 vertices, 2n edges
- **14.2-3**: Show P(n)=Ω(2^n) by substitution
- **14.2-4**: Subproblem graph for matrix-chain: Θ(n^2) vertices, O(n^3) edges
- **14.3-1**: Recursive-Matrix-Chain vs enumeration — both exponential, same asymptotic
- **14.3-2**: Memoization fails for MergeSort because subproblems are disjoint, not overlapping
- **14.3-4**: Counterexample where greedy split by pi−1 pk pj is suboptimal
- **14.3-5**: Rod cutting with li limits loses optimal substructure
- **14.4-2**: Reconstruct LCS from c table (no b table) in O(m+n)
- **14.4-5**: O(n^2) algorithm for longest monotonically increasing subsequence
- **14.4-6**: O(n lg n) algorithm for LIS (patience sorting)
- **14.5-1**: CONSTRUCT-OPTIMAL-BST from root table
- **14.5-4**: Knuth optimization → Θ(n^2) time for OBST

#### Key Problems
- **14-1**: Longest simple path in DAG (DP on topological order)
- **14-2**: Longest palindrome subsequence (LCS variant: LCS of string and its reverse)
- **14-3**: Bitonic Euclidean TSP (O(n^2) DP)
- **14-4**: Printing neatly (DP minimizing sum of cubes of extra spaces)
- **14-5**: Edit distance (6 operations: copy, replace, delete, insert, twiddle, kill)
- **14-6**: Company party planning (tree DP — employee/supervisor cannot both attend)
- **14-7**: Viterbi algorithm (DP on graph for most probable path matching a sound sequence)
- **14-8**: Image compression by seam carving (DP for min-disruption seam)
- **14-9**: Breaking a string (optimal break order — similar to matrix-chain)
- **14-10**: Investment strategy (DP, optimal substructure breaks with max investment limit)
- **14-11**: Inventory planning (DP, polynomial in n and D)
- **14-12**: Free-agent signing (knapsack-like DP with WAR metric)

---

## Ch. 15 — Greedy Algorithms

### Named Entities (Terms & Definitions)

- **Greedy Algorithm**: Makes the choice that looks best at the moment — a locally optimal choice in hope of global optimality.
- **Greedy-Choice Property**: A globally optimal solution can be assembled by making locally optimal (greedy) choices.
- **Activity-Selection Problem**: Given n activities with start times si and finish times fi, select a maximum-size subset of mutually compatible activities.
- **Compatible Activities**: Activities ai and aj are compatible if their intervals [si, fi) and [sj, fj) do not overlap (si ≥ fj or sj ≥ fi).
- **Huffman Code**: An optimal prefix-free code produced by Huffman's greedy algorithm.
- **Prefix-Free Code**: No codeword is a prefix of any other codeword.
- **Fixed-Length Code**: Each character encoded with ⌈lg n⌉ bits.
- **Variable-Length Code**: Frequent characters get short codewords, infrequent get long codewords.
- **Full Binary Tree**: Every nonleaf node has two children; optimal prefix-free codes always correspond to full binary trees.
- **Offline Caching**: Caching problem where the entire request sequence is known in advance; optimal strategy is furthest-in-future.
- **Cache Hit/Miss**: Hit = requested block already in cache; Miss = block not in cache.
- **Compulsory Miss**: Cache miss that occurs while the cache is still filling up.
- **Furthest-in-Future**: Greedy eviction strategy — evict the block whose next access is furthest in the future.
- **0-1 Knapsack Problem**: Each item taken or left (0/1); maximize value subject to weight limit W. Requires DP.
- **Fractional Knapsack Problem**: Can take fractions of items; solvable by greedy (value per pound).
- **Interval-Graph Coloring Problem**: Schedule all activities in minimum number of lecture halls = find chromatic number of interval graph.

### Processes / Algorithms / Pseudocode

#### RECURSIVE-ACTIVITY-SELECTOR
```
RECURSIVE-ACTIVITY-SELECTOR(s, f, k, n)
1 m = k + 1
2 while m ≤ n and s[m] < f[k]
3     m = m + 1
4 if m ≤ n
5     return {a_m} ∪ RECURSIVE-ACTIVITY-SELECTOR(s, f, m, n)
6 else return ∅
```
- **Input**: arrays s[1:n], f[1:n] (sorted by increasing finish time), index k defining subproblem Sk, size n
- **Initial call**: RECURSIVE-ACTIVITY-SELECTOR(s, f, 0, n) with fictitious a0 having f0=0
- **Output**: maximum-size set of mutually compatible activities in Sk
- **Complexity**: Θ(n) — each activity examined once across all recursive calls

#### GREEDY-ACTIVITY-SELECTOR (iterative)
```
GREEDY-ACTIVITY-SELECTOR(s, f, n)
1 A = {a1}
2 k = 1
3 for m = 2 to n
4     if s[m] ≥ f[k]
5         A = A ∪ {a_m}
6         k = m
7 return A
```
- **Complexity**: Θ(n) assuming activities sorted by finish time; O(n lg n) otherwise (for sorting)
- **Invariant**: fk = max finish time of any activity in A

#### HUFFMAN
```
HUFFMAN(C)
1 n = |C|
2 Q = C
3 for i = 1 to n - 1
4     allocate a new node z
5     x = EXTRACT-MIN(Q)
6     y = EXTRACT-MIN(Q)
7     z.left = x
8     z.right = y
9     z.freq = x.freq + y.freq
10    INSERT(Q, z)
11 return EXTRACT-MIN(Q)    // root of the tree
```
- **Input**: set C of n characters with freq attribute
- **Output**: root of optimal prefix-free code tree
- **Data structure**: min-priority queue Q keyed on freq (binary min-heap)
- **Complexity**: O(n lg n) — BUILD-MIN-HEAP O(n), loop n-1 times with O(lg n) heap operations

#### FURTHEST-IN-FUTURE (offline caching strategy)
- On a cache miss when cache is full, evict the block whose next access is furthest in the future.
- If a block in cache will never be accessed again, treat it as "furthest in future."
- **Optimal**: Theorem 15.5 — this greedy choice is part of some optimal solution.

### Formulas & Equations

**Expected bits for Huffman encoding**:
```
B(T) = Σ_{c∈C} c.freq · d_T(c)
```
where d_T(c) is depth of c's leaf (codeword length).

**Total cost as sum of internal node frequencies**:
```
B(T) = Σ_{internal nodes} (left_child.freq + right_child.freq)
```

**Huffman code compression example** (Figure 15.4): 6 chars a:45, b:13, c:12, d:16, e:9, f:5 (thousands)
- Fixed-length (3 bits): 300,000 bits
- Variable-length optimal: 224,000 bits (25% savings)

### Rules, Laws & Theorems

**Theorem 15.1 (Greedy choice for activity selection)**: Consider any nonempty subproblem Sk, and let am be the activity in Sk with earliest finish time. Then am is included in some maximum-size subset of mutually compatible activities of Sk.

**Proof**: Exchange argument — take any optimal solution, replace its earliest-finishing activity aj with am (fm ≤ fj maintains compatibility, same cardinality).

**Lemma 15.2 (Greedy-choice property for Huffman)**: Let x and y be two characters in C with lowest frequencies. Then there exists an optimal prefix-free code for C in which the codewords for x and y have the same length and differ only in the last bit.

**Proof**: Take optimal tree T, find deepest sibling leaves a,b. Swap x with a, y with b. Each swap does not increase cost. Result: x and y are deepest siblings.

**Lemma 15.3 (Optimal substructure for Huffman)**: Let C' = (C − {x,y}) ∪ {z} where z.freq = x.freq + y.freq. If T' is an optimal prefix-free code for C', then T (replace leaf z with internal node having children x,y) is optimal for C.

**Proof**: B(T) = B(T') + x.freq + y.freq. Contradiction if T not optimal.

**Theorem 15.4**: Procedure HUFFMAN produces an optimal prefix-free code.

**Theorem 15.5 (Greedy-choice property for offline caching)**: When cache is full and a miss occurs, evicting the block whose next access is furthest in the future is included in some optimal solution.

**Proof**: Exchange argument — transform optimal solution that evicts some other block x into one that evicts z (furthest-in-future) without increasing misses.

### Comparisons & Trade-offs

| Dimension | Greedy | Dynamic Programming |
|---|---|---|
| Choice | Locally optimal, doesn't depend on subproblem solutions | Depends on subproblem solutions |
| Direction | Top-down (make choice, then solve subproblem) | Bottom-up (solve subproblems, then make choice) |
| Subproblem space | Single remaining subproblem | Many subproblems |
| Proof | Greedy-choice property + optimal substructure | Optimal substructure + overlapping subproblems |
| Efficiency | Usually faster, simpler | May be overkill |
| Example | Activity selection, fractional knapsack | 0-1 knapsack, matrix-chain |

| Dimension | Huffman Coding | Fixed-Length Coding |
|---|---|---|
| Bit usage | Variable length; optimal | Fixed ⌈lg n⌉ bits per char |
| Savings | 20-90% typical | None |
| Decoding | Requires prefix-free property | Simple |
| Best for | Skewed frequency distributions | Uniform/ near-uniform distributions |

| Dimension | 0-1 Knapsack | Fractional Knapsack |
|---|---|---|
| Greedy works? | No | Yes |
| DP works? | Yes (O(nW)) | N/A |
| Item unit | Indivisible | Divisible |
| Optimal substructure? | Yes | Yes |
| Greedy-choice property? | No | Yes |

| Dimension | Furthest-in-Future (offline) | LRU (online) |
|---|---|---|
| Knows future? | Yes (optimal) | No (past only) |
| Performance | Optimal (min cache misses) | Can be suboptimal |

### Edge Cases & Common Pitfalls

- **Greedy fails when greedy-choice property absent**: 0-1 knapsack, making change with arbitrary denominations, longest simple path
- **Activity selection**: Selecting by least duration, fewest overlaps, or earliest start time all FAIL as greedy strategies
- **Huffman code**: Non-full binary trees cannot be optimal (must be full binary tree)
- **Huffman for uniform frequencies**: No better than fixed-length code when all frequencies are within factor 2 of each other
- **Offline caching**: The proof of Theorem 15.5 is intricate — the exchange argument must maintain that cache configurations differ by at most one block
- **Lossless compression cannot always compress**: No lossless scheme can guarantee shorter output for every input file (pigeonhole principle)

### Proof & Argument Patterns

**Exchange Argument (Greedy Stays Ahead)**:
1. Consider an optimal solution O.
2. Show that the greedy choice can replace some element of O without making O worse.
3. By induction, greedy's choices can be swapped in one-by-one, proving greedy is optimal.

**Example: Activity selection (Theorem 15.1)**:
- Let am = greedy choice (earliest finish in Sk)
- Let aj = earliest finish in optimal solution Ak
- If aj ≠ am, replace aj with am → set A'k = (Ak − {aj}) ∪ {am}
- A'k is compatible (since fm ≤ fj), has same size, contains am

**Example: Huffman (Lemma 15.2)**:
- Take optimal T, find deepest siblings a,b
- Swap x with a, y with b
- Cost difference: (a.freq−x.freq)(dT(a)−dT(x)) + (b.freq−y.freq)(dT(b)−dT(y)) ≤ 0
- Result: T'' is optimal with x,y as deepest siblings

**Example: Offline caching (Theorem 15.5)**:
- Let S evict x (not furthest-in-future)
- Construct S' that evicts z instead
- Show cache configurations differ by at most one block
- Show S' has ≤ cache misses as S (if S has a hit, S' has a hit; miss differences cancel)

### Design Paradigms

**Greedy Algorithm Development Process** (detailed, Section 15.1 style):
1. Determine optimal substructure
2. Develop recursive solution
3. Show greedy choice leaves one subproblem
4. Prove greedy choice is safe
5. Develop recursive greedy algorithm
6. Convert to iterative algorithm

**Greedy Algorithm Development Process** (streamlined, Section 15.2 style):
1. Cast as make-a-choice, one-subproblem-remains problem
2. Prove there is always an optimal solution making the greedy choice
3. Show optimal substructure: greedy choice + optimal subproblem solution = optimal original solution

**Key requirements for greedy**:
- **Greedy-choice property**: Local optimal choice leads to global optimum
- **Optimal substructure**: Solution contains optimal solutions to subproblems

### End-of-Chapter Material

#### Key terms
greedy algorithm, greedy-choice property, optimal substructure, activity-selection problem, Huffman code, prefix-free code, full binary tree, offline caching, furthest-in-future, 0-1 knapsack, fractional knapsack

#### Selected Exercises
- **15.1-1**: DP for activity selection based on recurrence c[i,j] — compare running time to greedy
- **15.1-3**: Counterexamples: least duration, fewest overlaps, earliest start all fail for activity selection
- **15.1-4**: Interval-graph coloring (minimum lecture halls) — greedy by earliest finish time
- **15.1-5**: Weighted activity selection (maximize total value) — DP, not greedy
- **15.2-1**: Prove fractional knapsack has greedy-choice property
- **15.2-2**: DP for 0-1 knapsack in O(nW) time
- **15.2-6**: Fractional knapsack in O(n) time (median-finding for value/pound)
- **15.2-7**: Maximize Π ai^bi — sort both arrays (rearrangement inequality)
- **15.3-3**: Huffman for Fibonacci frequencies 1,1,2,3,5,8,13,21 — related to Fibonacci coding
- **15.3-4**: Total cost of Huffman tree = sum of all internal node frequencies
- **15.3-7**: Huffman useless when max freq < 2× min freq (near-uniform)
- **15.3-8**: No lossless compression guarantees shorter output for every input
- **15.4-2**: LRU ≠ optimal — give counterexample sequence

#### Key Problems
- **15-1**: Coin changing — greedy optimal for US coins and powers of c; counterexample for arbitrary denominations; O(nk) DP
- **15-2**: Minimize average completion time — SPT (shortest processing time first); with release times and preemption → SRPT (shortest remaining processing time first)
- **15-4**: Offline caching proof

---

## Ch. 16 — Amortized Analysis

### Named Entities (Terms & Definitions)

- **Amortized Analysis**: Averaging the time required to perform a sequence of data-structure operations over all operations performed; guarantees worst-case average performance.
- **Aggregate Analysis**: Shows that a sequence of n operations takes T(n) worst-case time total; amortized cost per operation = T(n)/n.
- **Accounting Method**: Assign differing charges to operations; overcharge some early operations and store as credit; credit pays for later operations with undercharge.
- **Potential Method**: Prepaid work represented as "potential energy" of the data structure as a whole; amortized cost = actual cost + change in potential.
- **Credit**: The difference between total amortized cost and total actual cost; must remain nonnegative at all times.
- **Potential Function Φ**: Maps a data structure D to a real number Φ(D); amortized cost ĉi = ci + Φ(Di) − Φ(Di−1).
- **Load Factor α(T)**: For a table T, α(T) = num / size; for empty table, defined as 1.
- **Table Expansion**: When a dynamic table is full, allocate a new table with twice as many slots and copy all items.
- **Table Contraction**: When load factor drops below 1/4, allocate a new table half the size and copy items.
- **Elementary Insertion**: Inserting a single item into a table slot (cost 1).

### Processes / Algorithms / Pseudocode

#### MULTIPOP (stack with additional operation)
```
MULTIPOP(S, k)
1 while not STACK-EMPTY(S) and k > 0
2     POP(S)
3     k = k - 1
```
- **Actual cost**: min{s, k} where s is stack size
- **Amortized cost**: O(1) by aggregate/accounting/potential analysis

#### INCREMENT (binary counter)
```
INCREMENT(A, k)
1 i = 0
2 while i < k and A[i] == 1
3     A[i] = 0
4     i = i + 1
5 if i < k
6     A[i] = 1
```
- **Actual cost**: number of bits flipped (ti + 1, where ti = number of trailing 1s)
- **Amortized cost**: O(1) by aggregate/accounting/potential analysis

#### TABLE-INSERT (dynamic table)
```
TABLE-INSERT(T, x)
1 if T.size == 0
2     allocate T.table with 1 slot
3     T.size = 1
4 if T.num == T.size
5     allocate new-table with 2·T.size slots
6     insert all items in T.table into new-table
7     free T.table
8     T.table = new-table
9     T.size = 2·T.size
10 insert x into T.table
11 T.num = T.num + 1
```
- **Actual cost**: 1 if no expansion; i if expansion occurs (i−1 copies + 1 insert = i)
- **Expansion occurs when**: i−1 is an exact power of 2

#### TABLE-DELETE (dynamic table — conceptual)
- Analogous to TABLE-INSERT
- **Contraction policy**: Halve size when load factor drops below 1/4
- Contraction occurs after deletion, when num = (size/4) before deletion

### Formulas & Equations

**Stack analysis summary**:
| Operation | Actual cost | Accounting amortized | Potential amortized |
|---|---|---|---|
| PUSH | 1 | 2 | 2 |
| POP | 1 | 0 | 0 |
| MULTIPOP | min{s,k} | 0 | 0 |

**Potential function for stack**: Φ(D) = number of objects in stack.

**Binary counter analysis**:
- Bit A[i] flips ⌊n/2^i⌋ times in sequence of n INCREMENT operations
- Total flips: Σ_{i=0}^{k-1} ⌊n/2^i⌋ < 2n
- **Amortized cost per operation**: O(1)
- **Accounting method**: Charge $2 per bit set to 1; $1 pays for setting, $1 stored as credit for resetting to 0
- **Potential function**: Φ(D) = number of 1-bits in counter
- **Counter starting at b0**: Total actual cost ≤ 2n + bn − b0; if n = Ω(k), cost is O(n)

**Amortized cost of INCREMENT**:
```
ĉi = ci + Φ(Di) − Φ(Di−1)
   ≤ (ti + 1) + (1 − ti) = 2
```

**Dynamic table — aggregate analysis**:
```
ci = i  if i−1 is a power of 2
     1  otherwise
```
Total cost of n insertions:
```
Σ_{i=1}^{n} ci ≤ n + Σ_{j=0}^{⌊lg n⌋} 2^j = n + (2^{⌊lg n⌋+1} − 1) < 3n
```
Amortized cost per operation ≤ 3.

**Potential function for table insert only**:
```
Φ(T) = 2(T.num − T.size/2)
```
- Φ = 0 immediately after expansion (num = size/2)
- Φ = size when table is full (num = size)
- Each insertion without expansion: ΔΦ = 2, ĉ = 1+2 = 3
- Each insertion with expansion: c = i, ΔΦ = 2−(i−1)=3−i, ĉ = i+(3−i)=3

**Potential function for table insert + delete**:
```
Φ(T) = 2(T.num − T.size/2)    if α(T) ≥ 1/2
Φ(T) = T.size/2 − T.num       if 1/4 ≤ α(T) < 1/2
```
Equivalently: Φ(T) = |2(T.num − T.size/2)| for load factor between 1/4 and 1.

**Amortized costs for table with doubling/halving**:
| Operation | Condition | ĉ |
|---|---|---|
| Insert | α ≥ 1/2, no expansion | 3 |
| Insert | With expansion | 3 |
| Insert | α < 1/2 | 0 |
| Insert | α crosses from <1/2 to =1/2 | 0 |
| Delete | α ≥ 1/2 | −1 |
| Delete | With contraction | 1 |
| Delete | α < 1/2, no contraction | 2 |
| Delete | α crosses from =1/2 to <1/2 | 2 |

**Key identity for potential method**:
```
Σ ĉi = Σ ci + Φ(Dn) − Φ(D0)
```
If Φ(Dn) ≥ Φ(D0) for all n, then total amortized cost ≥ total actual cost.

### Rules, Laws & Theorems

**Amortized Analysis — Three methods**:
1. **Aggregate**: Compute T(n) total worst-case cost; amortized = T(n)/n
2. **Accounting**: Assign ĉi (amortized cost) per operation; ensure Σ ĉi ≥ Σ ci for all sequences; credit = Σ(ĉi − ci) ≥ 0 always
3. **Potential**: Define Φ(D); ĉi = ci + Φ(Di) − Φ(Di−1); require Φ(Di) ≥ Φ(D0) for all i

**Theorem 16.x (implicit)**: For a sequence of n operations on a data structure, amortized analysis provides a worst-case guarantee on average performance; no probabilistic assumptions needed.

### Comparisons & Trade-offs

| Dimension | Aggregate | Accounting | Potential |
|---|---|---|---|
| Amortized cost per op | Same for all ops | May differ by op type | May differ by op type |
| Key concept | Sum all costs, divide by n | Assign credits to objects | Potential function for DS |
| Credit/potential location | Implicit | On specific objects | Data structure as whole |
| Difficulty | Simplest | Intermediate | Most flexible |
| When useful | All ops similar | Different op types | Need global view |

| Dimension | Amortized Analysis | Average-Case Analysis |
|---|---|---|
| Guarantee | Worst-case bound on average | Average over probability distribution |
| Probability | None used | Required |
| Example | Stack: any n ops = O(n) | Separate chaining hash: expected O(1) per op |

### Edge Cases & Common Pitfalls

- **Credit must never go negative**: In accounting method, total credit Σ(ĉi − ci) must be ≥ 0 after every operation
- **Potential function bounds**: Need Φ(Di) ≥ Φ(D0) for all i (usually Φ(D0)=0, Φ(Di) ≥ 0)
- **Table contraction at 1/2 is pathological**: If you halve at load factor 1/2, alternating insert/delete causes Θ(n) amortized cost (thrashing)
- **MULTIPUSH breaks O(1) amortized**: If MULTIPUSH(S, k) can push k items, each with cost k, amortized bound may not hold
- **DECREMENT on binary counter**: If both INCREMENT and DECREMENT are supported, worst-case per op can be Θ(k)
- **Empty table**: Load factor defined as 1 for empty table (0/0 avoids division by zero)
- **Potential function choice matters**: Different Φ give different amortized costs but all valid upper bounds

### Design Paradigms

**Amortized Analysis** — three complementary techniques:
1. **Aggregate analysis**: Simpler; same amortized cost for all ops
2. **Accounting method**: Like a bank account; prepay expensive ops
3. **Potential method**: Most general; Φ changes capture "stored work"

**Dynamic table design principles**:
- Double size on overflow for insertions
- Halve size only when load factor drops to 1/4 (not 1/2) to avoid thrashing
- After expansion or contraction, load factor = 1/2 and potential = 0
- Potential builds linearly as load factor deviates from 1/2

### End-of-Chapter Material

#### Key terms
amortized analysis, aggregate analysis, accounting method, potential method, credit, potential function, load factor, dynamic table, table expansion, table contraction

#### Selected Exercises
- **16.1-1**: MULTIPUSH — O(1) amortized fails if MULTIPUSH(k) can push k items
- **16.1-2**: DECREMENT added to binary counter — Θ(nk) worst case possible
- **16.1-3**: Sequence where i-th op costs i if i is power of 2, else 1 — amortized O(1)
- **16.2-1**: Stack with backup copy every k operations — O(n) total with accounting
- **16.2-3**: Counter with RESET — O(n) total using pointer to high-order 1
- **16.3-1**: Φ(D0) ≠ 0 → define Φ'(D) = Φ(D) − Φ(D0)
- **16.3-3**: Binary min-heap potential function: amortized INSERT O(lg n), EXTRACT-MIN O(1)
- **16.3-5**: Queue with two stacks — O(1) amortized per ENQUEUE and DEQUEUE
- **16.3-6**: Dynamic multiset with DELETE-LARGER-HALF — O(m) total for m operations
- **16.4-2**: Open-address hash table with load factor threshold < 1 for insertion
- **16.4-4**: Contraction by ×2/3 at load factor 1/3 — potential Φ = |2(num − size/2)|

#### Key Problems
- **16-1**: Binary reflected Gray code — determine which bit flips from index i; generate in Θ(2^k)
- **16-2**: Making binary search dynamic — maintain k sorted arrays of lengths 2^i
- **16-3**: Amortized weight-balanced trees — α-balanced, rebuild when unbalanced, potential = c Σ Δ(x) / (x.size)
- **16-4**: Structural modifications in red-black trees — potential = number of red nodes; O(m) modifications for m operations

---

## Cross-Cutting Topics

### Design Paradigms

| Paradigm | Approach | Key Requirement | Running time (typical) |
|---|---|---|---|
| **Divide & Conquer** | Split into disjoint subproblems, solve recursively, combine | Subproblems independent | Recurrence solution |
| **Dynamic Programming** | Solve overlapping subproblems, store results | Optimal substructure + overlapping subproblems | O(#subproblems × #choices) |
| **Greedy** | Make locally optimal choice, solve remaining subproblem | Greedy-choice property + optimal substructure | Often O(n lg n) or better |
| **Amortized Analysis** | Average worst-case cost over sequence | None (analysis technique, not algorithm design) | O(1) amortized per op |

### Proof & Argument Patterns

1. **Cut-and-Paste (Optimal Substructure)**:
   - Show optimal solution contains optimal sub-solutions
   - If sub-solution not optimal, cut it out and paste in a better one → contradiction
   - Applied in: rod cutting, matrix-chain, LCS, OBST, activity selection, Huffman, offline caching

2. **Exchange Argument (Greedy Stays Ahead)**:
   - Take any optimal solution, show greedy choice can replace some element without degrading quality
   - Applied in: activity selection (Theorem 15.1), Huffman (Lemma 15.2), offline caching (Theorem 15.5)

3. **Induction on Subproblems**:
   - Greedy choice reduces problem size; assume optimal for smaller case; combine proves optimal for original
   - Underlies both DP and greedy correctness proofs

4. **Substitution Method**:
   - Prove lower/upper bound on recurrence (e.g., T(n) ≥ 2^{n−1} for recursive matrix-chain)

5. **Contradiction via Cost Comparison (Huffman Lemma 15.3)**:
   - Show B(T) = B(T') + x.freq + y.freq
   - If T not optimal, then T' not optimal (contradiction)

6. **Potential Function Lower Bounds**:
   - Φinit, Φfinal, ΔΦmax ⇒ steps ≥ |Φfinal−Φinit|/|ΔΦmax|
   - Used in I/O complexity, gossiping lower bounds

### Mnemonics & Memory Aids

- **DP 4 steps**: Char → Rec → Comp → Constr (Characterize, Recursively define, Compute, Construct)
- **Greedy 6 steps**: OST → Rec → Greedy → Proof → RecG → IterG (Optimal substructure, Recursive solution, Greedy choice, Prove, Recursive greedy, Iterative)
- **Amortized 3 methods**: AAA (Aggregate, Accounting, Add potential)
- **Dynamic table thresholds**: Insert double at 1, delete halve at 1/4 (not 1/2!) → "Double full, halve quarter"
- **Huffman invariant**: Merge two smallest frequencies; total cost = sum of all merged frequencies
- **Stack amortization**: "Push pays double — one to insert, one to pop"

### Self-Test Templates

**Template: DP recurrence setup**
```
Given problem P with subproblem parameter(s) ____:
1. Base case: P(0) = ____
2. Choices: for each ____ in ____:
3. Subproblem to solve: P(____)
4. Combine: opt(P) = ____ { ____ }
```

**Template: Greedy proof**
1. Greedy choice: always pick ____
2. Any optimal solution can be transformed to include greedy choice because ____
3. After greedy choice, remaining subproblem is ____
4. Optimal substructure: greedy choice + optimal solution to subproblem = optimal original solution

**Fill-in: Aggregate analysis for binary counter**
```
Bit A[0] flips every time = ⌊n/__⌋ times
Bit A[1] flips every __ time = ⌊n/__⌋ times
Bit A[i] flips ⌊n/__⌋ times
Total flips = Σ ____ < ____
Amortized cost per INCREMENT = ____
```
> Answers: 1, 2nd, 2, 2^i, Σ⌊n/2^i⌋ < 2n, O(1)

### People & Dates

- **Richard Bellman**: Began systematic study of dynamic programming in 1955, book in 1957
- **David A. Huffman**: Invented Huffman codes in 1952
- **L. A. Belady**: Proposed furthest-in-future strategy for virtual-memory systems
- **D. D. Sleator and R. E. Tarjan**: Coined term "amortized"; developed accounting and potential methods
- **Knuth**: O(n lg n) algorithm for OBST (pi=0 case); showed root[i,j-1] ≤ root[i,j] ≤ root[i+1,j] (Exercise 14.5-4)
- **Galil and Park**: Classified DP as tD/eD algorithms
- **Masek and Paterson**: O(mn/lg n) algorithm for LCS
