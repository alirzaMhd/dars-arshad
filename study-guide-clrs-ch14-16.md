# Study Guide: Introduction to Algorithms (CLRS 4e) — Part IV: Advanced Design and Analysis Techniques

> Generated 2026-06-05. Subject: Computer Science / Algorithms. Coverage: Chapters 14–16 (Ch 14: Dynamic Programming, Ch 15: Greedy Algorithms, Ch 16: Amortized Analysis). Target: ~500 lines.

---

### Ch. 14 — Dynamic Programming

#### Named Entities (Terms & Definitions)
- **Dynamic Programming (DP)**: method for solving problems by combining solutions to overlapping subproblems; solves each subproblem once and stores result in a table; applies to optimization problems with optimal substructure and overlapping subproblems.
- **Memoization**: top-down DP technique that saves results of subproblems in an array/table upon first computation; subsequent calls look up the saved value.
- **Optimal substructure**: property where an optimal solution to a problem contains optimal solutions to its subproblems.
- **Overlapping subproblems**: property where a recursive algorithm revisits the same subproblem repeatedly; total distinct subproblems is polynomial.
- **Subproblem graph**: directed graph with one vertex per distinct subproblem; edge (x,y) if solving x requires solving y.
- **Rod-cutting problem**: given rod length n and price table pi for i=1..n, maximize revenue by cutting rod into integer-length pieces.
- **Matrix-chain multiplication**: given chain of n matrices with dimensions p0×p1, p1×p2, ..., pn−1×pn, fully parenthesize product to minimize scalar multiplications.
- **Longest common subsequence (LCS)**: given two sequences X, Y, find maximum-length subsequence common to both.
- **Optimal binary search tree (OBST)**: given keys k1..kn with probabilities pi and dummy keys d0..dn with probabilities qi, build BST minimizing expected search cost.

#### Processes / Algorithms / Pathways
##### Four-Step DP Method
- **Type**: Design paradigm
- **Steps**: (1) Characterize structure of optimal solution (optimal substructure). (2) Recursively define value of optimal solution. (3) Compute value bottom-up (or top-down with memoization). (4) Construct optimal solution from computed info.

##### CUT-ROD (naive recursive)
- **Goal**: compute max revenue for rod length n
- **Steps**: (1) if n=0 return 0. (2) q = -∞. (3) for i=1..n: q = max(q, p[i] + CUT-ROD(p, n-i)). (4) return q.
- **Complexity**: T(n) = 2^n (exponential); recurrence: T(n) = 1 + Σ_{j=0}^{n-1} T(j), T(0)=1

##### MEMOIZED-CUT-ROD
- **Goal**: compute max revenue with memoization
- **Steps**: (1) initialize r[0..n] = -∞. (2) call MEMOIZED-CUT-ROD-AUX(p,n,r).
- **Complexity**: Θ(n²)

##### BOTTOM-UP-CUT-ROD
- **Goal**: compute max revenue bottom-up
- **Steps**: (1) r[0] = 0. (2) for j=1..n: q = -∞; for i=1..j: q = max(q, p[i] + r[j-i]); r[j] = q. (3) return r[n].
- **Complexity**: Time Θ(n²), Space Θ(n)
- **Example**: For n=4, prices p=[1,5,8,9], r[1]=1, r[2]=5, r[3]=8, r[4]=10 (cut as 2+2)

##### MATRIX-CHAIN-ORDER
- **Goal**: compute min scalar multiplications for matrix chain A1..An
- **Steps**: (1) for i=1..n: m[i,i]=0. (2) for l=2..n (chain length): for i=1..n-l+1: j=i+l-1; m[i,j]=∞; for k=i..j-1: q = m[i,k]+m[k+1,j]+p_{i-1}·p_k·p_j; if q<m[i,j]: m[i,j]=q, s[i,j]=k.
- **Complexity**: Time Θ(n³), Space Θ(n²)
- **Example**: Dimensions: A1(30×35), A2(35×15), A3(15×5), A4(5×10), A5(10×20), A6(20×25). m[1,6]=15,125. Optimal parenthesization: ((A1(A2A3))((A4A5)A6))

##### LCS-LENGTH
- **Goal**: compute length of LCS of X[1..m], Y[1..n]
- **Steps**: (1) initialize c[i,0]=0, c[0,j]=0. (2) for i=1..m: for j=1..n: if xi=yj: c[i,j]=c[i-1,j-1]+1, b[i,j]="↖"; else if c[i-1,j]≥c[i,j-1]: c[i,j]=c[i-1,j], b[i,j]="↑"; else: c[i,j]=c[i,j-1], b[i,j]="←".
- **Complexity**: Time Θ(mn), Space Θ(mn)
- **Example**: X=<A,B,C,B,D,A,B>, Y=<B,D,C,A,B,A>. LCS length=4, LCS = <B,C,B,A>

##### OPTIMAL-BST
- **Goal**: compute min expected search cost for BST with keys k1..kn
- **Steps**: (1) for i=1..n+1: e[i,i-1]=q_{i-1}, w[i,i-1]=q_{i-1}. (2) for l=1..n: for i=1..n-l+1: j=i+l-1; w[i,j]=w[i,j-1]+pj+qj; e[i,j]=∞; for r=i..j: t=e[i,r-1]+e[r+1,j]+w[i,j]; if t<e[i,j]: e[i,j]=t, root[i,j]=r.
- **Complexity**: Time Θ(n³); can be improved to Θ(n²) using Knuth's inequality (root[i,j-1] ≤ root[i,j] ≤ root[i+1,j])
- **Example**: 5 keys with given probabilities; e[1,5]=2.75; root k2

#### Classifications & Hierarchies
- **DP implementation approaches**:
  - Top-down with memoization: recursive + table; solves only needed subproblems; higher constant factors
  - Bottom-up: iterative, smallest subproblems first; lower constant factors; solves all subproblems
- **DP problem classification (tD/eD)**:
  - 2D/1D: matrix-chain (Θ(n³) time, Θ(n²) subproblems, each depends on O(n) others)
  - 2D/0D: LCS (Θ(mn) time, each entry depends on O(1) others)

#### Comparisons & Trade-offs
| Dimension | Top-down (Memoization) | Bottom-up |
|---|---|---|
| Strategy | Recursive + save results | Iterative, smallest first |
| Solves all subproblems? | Only those needed | All |
| Overhead | Recursion + table maintenance | Lower constant factors |
| When preferred | Not all subproblems needed | All subproblems must be solved |

| Dimension | DP | Divide-and-Conquer |
|---|---|---|
| Subproblems | Overlapping | Disjoint |
| Efficiency | Solves each once | May recompute |
| Example | Rod cutting, LCS | Merge sort |

#### Formulas & Equations
##### Rod-cutting recurrence
`rn = max(pn, max_{1≤i≤n-1}(ri + r_{n-i}))`  
Simpler: `rn = max_{1≤i≤n}(pi + r_{n-i})`, r0=0

##### Matrix-chain recurrence
`m[i,j] = min_{i≤k<j}(m[i,k] + m[k+1,j] + p_{i-1}·pk·pj)`  
Base: m[i,i]=0

##### LCS recurrence
`c[i,j] = 0` if i=0 or j=0  
`c[i,j] = c[i-1,j-1] + 1` if xi=yj  
`c[i,j] = max(c[i-1,j], c[i,j-1])` if xi≠yj

##### OBST recurrence
`e[i,j] = qi-1` if j=i-1  
`e[i,j] = min_{i≤r≤j}(e[i,r-1] + e[r+1,j] + w[i,j])` if j≥i  
where `w[i,j] = w[i,j-1] + pj + qj`

#### Rules, Laws & Theorems
##### Theorem 14.1 (Optimal substructure of LCS)
- **Statement**: Let X=<x1..xm>, Y=<y1..yn>, Z any LCS. (1) If xm=yn then zk=xm=yn and Z_{k-1} is LCS of X_{m-1} and Y_{n-1}. (2) If xm≠yn and zk≠xm then Z is LCS of X_{m-1} and Y. (3) If xm≠yn and zk≠yn then Z is LCS of X and Y_{n-1}.

#### Edge Cases & Common Pitfalls
- **Longest simple path lacks optimal substructure** (subproblems not independent — sharing vertices makes combination non-simple); while shortest path has it
- **OBST is not necessarily the tree with smallest height**; highest-probability key may not be root
- **Cut-and-paste proof**: must show subproblems are independent (no shared resources)
- **Greedy ≠ DP**: rod cutting greedy by density fails (Exercise 14.1-2)

#### Case Studies & Examples
##### Rod Cutting (n=4)
- Prices: p1=$1, p2=$5, p3=$8, p4=$9
- Options: 1+1+1+1=$4, 2+2=$10 (optimal), 3+1=$9, 4=$9
- Optimal: cut into two 2-inch pieces, revenue $10

##### Matrix Chain (n=3)
- A1(10×100), A2(100×5), A3(5×50)
- ((A1A2)A3): 10·100·5 + 10·5·50 = 5000+2500=7500
- (A1(A2A3)): 100·5·50 + 10·100·50 = 25000+50000=75000
- Ratio: 10x difference

#### Diagrams & Visuals
```
Rod-cutting recursion tree (n=4):
          4
     /   |   |   \
    3    2    1    0
   /|\   |\   |
  2 1 0  1 0  0
 /|\ |   |
1 0 0   0  ...
|
0

Subproblem graph: collapses repeated nodes
Vertices: {0,1,2,3,4}
Edges: i → j for j < i
```

#### End-of-Chapter Material
- **Key terms**: optimal substructure, overlapping subproblems, memoization, bottom-up, subproblem graph, Catalan numbers, prefix, dummy key
- **Exercises**: 14.1-1 (T(n) recurrence), 14.1-2 (greedy counterexample), 14.2-1 (optimal parenthesization for <5,10,3,12,5,50,6>), 14.4-1 (LCS of binary sequences), 14.5-1 (construct OBST from root table)

#### Cross-Chapter Links
- **Requires knowledge of**: Ch 2 (divide-and-conquer), Ch 4 (recurrences), Ch 12 (BSTs)
- **Referenced in later chapters**: Ch 15 (greedy vs DP), Ch 34 (NP-completeness)

---

### Ch. 15 — Greedy Algorithms

#### Named Entities (Terms & Definitions)
- **Greedy algorithm**: makes locally optimal choice at each step, hoping for globally optimal solution.
- **Greedy-choice property**: globally optimal solution can be assembled by making locally optimal (greedy) choices.
- **Activity-selection problem**: given n activities with start/finish times, select maximum-size set of mutually compatible activities.
- **Compatible activities**: activities whose intervals [si, fi) do not overlap.
- **Huffman code**: optimal prefix-free code constructed by repeatedly merging two least-frequent characters.
- **Prefix-free code**: no codeword is a prefix of any other codeword; decoding is unambiguous.
- **Full binary tree**: every nonleaf node has two children; optimal prefix-free codes correspond to full trees.
- **0-1 knapsack problem**: thief can take or leave each item (binary choice); requires DP.
- **Fractional knapsack problem**: thief can take fractions of items; solvable by greedy.
- **Offline caching**: know entire request sequence in advance; optimal strategy is furthest-in-future.
- **Furthest-in-future**: evict the block in cache whose next access is furthest in the future.

#### Processes / Algorithms / Pathways
##### Greedy Algorithm Design Steps
- **Type**: Design paradigm
- **Steps**: (1) Cast problem as making a choice, leaving one subproblem. (2) Prove greedy choice is always safe. (3) Demonstrate optimal substructure: greedy choice + optimal solution to subproblem = optimal solution to original.

##### RECURSIVE-ACTIVITY-SELECTOR(s, f, k, n)
- **Goal**: select max-size set of compatible activities from Sk
- **Steps**: (1) m = k+1. (2) while m≤n and s[m]<f[k]: m++. (3) if m≤n: return {am} ∪ RECURSIVE-ACTIVITY-SELECTOR(s,f,m,n). (4) else return ∅.
- **Complexity**: Θ(n) (each activity examined once across all recursive calls)

##### GREEDY-ACTIVITY-SELECTOR(s, f, n)
- **Goal**: iterative greedy activity selection
- **Steps**: (1) A={a1}, k=1. (2) for m=2..n: if s[m]≥f[k]: A=A∪{am}, k=m. (3) return A.
- **Complexity**: Θ(n) (after sorting by finish time O(n lg n))
- **Example**: Activities (sorted by finish): a1(1,4), a2(3,5), a3(0,6), a4(5,7), a5(3,9), a6(5,9), a7(6,10), a8(8,11), a9(8,12), a10(2,14), a11(12,16). Selected: {a1, a4, a8, a11}

##### HUFFMAN(C)
- **Goal**: construct optimal prefix-free code for alphabet C with frequencies
- **Steps**: (1) Q = C (min-priority queue keyed by freq). (2) for i=1 to |C|-1: allocate new node z; x = EXTRACT-MIN(Q); y = EXTRACT-MIN(Q); z.left=x; z.right=y; z.freq=x.freq+y.freq; INSERT(Q,z). (3) return EXTRACT-MIN(Q) (root).
- **Complexity**: O(n lg n) with binary heap
- **Example**: Frequencies: a:45, b:13, c:12, d:16, e:9, f:5 (×1000). Code: a=0 (1 bit), b=101 (3), c=100 (3), d=111 (3), e=1101 (4), f=1100 (4). Total bits: 224,000 vs 300,000 fixed-length.

#### Classifications & Hierarchies
- **Greedy vs DP**: both require optimal substructure; greedy adds greedy-choice property; greedy makes choice before solving subproblems; DP solves subproblems before making choice.
- **Knapsack variants**:
  - 0-1 knapsack: each item taken or left (DP, O(nW))
  - Fractional knapsack: take fractions (greedy by value/weight, O(n lg n))

#### Comparisons & Trade-offs
| Dimension | Greedy | Dynamic Programming |
|---|---|---|
| Choice timing | Before solving subproblems | After solving subproblems |
| Subproblems | One remains after choice | Multiple considered |
| Direction | Top-down | Usually bottom-up |
| Efficiency | Typically faster | More general |
| When applies | Greedy-choice + optimal substructure | Optimal substructure + overlapping subproblems |

| Dimension | 0-1 Knapsack | Fractional Knapsack |
|---|---|---|
| Items | Take or leave | Take fractions |
| Solution | DP (O(nW)) | Greedy by value/weight |
| Greedy works? | No | Yes |

#### Formulas & Equations
##### Huffman tree cost
`B(T) = Σ_{c∈C} c.freq · dT(c)`  
where dT(c) = depth of leaf for character c (also codeword length)

##### Huffman cost = sum of merge costs
`B(T) = Σ_{internal nodes} (freq(left child) + freq(right child))`
- Each merge adds combined frequency to total cost

#### Rules, Laws & Theorems
##### Theorem 15.1 (Greedy choice — activity selection)
- **Statement**: For any nonempty subproblem Sk, let am be activity with earliest finish time. Then am is included in some maximum-size subset of mutually compatible activities of Sk.
- **Proof**: Take optimal solution Ak; let aj be earliest-finish activity in Ak. If aj≠am, substitute am for aj; compatibility preserved, same size.

##### Lemma 15.2 (Greedy choice — Huffman)
- **Statement**: Let x,y be two characters with lowest frequencies. There exists an optimal prefix-free code where codewords for x,y have same length and differ only in last bit.
- **Proof**: Swap deepest siblings a,b with x,y; cost does not increase.

##### Lemma 15.3 (Optimal substructure — Huffman)
- **Statement**: If T' is optimal for C' = (C-{x,y})∪{z} with z.freq = x.freq+y.freq, then replacing leaf z with internal node having children x,y gives optimal tree T for C.

##### Theorem 15.4
- **Statement**: HUFFMAN produces an optimal prefix-free code.

##### Theorem 15.5 (Greedy choice — offline caching)
- **Statement**: When cache is full and miss occurs, evicting the block whose next access is furthest in the future is included in some optimal solution.

#### Edge Cases & Common Pitfalls
- **Not all greedy strategies work**: activity selection by shortest duration, fewest overlaps, or earliest start time all fail (Exercise 15.1-3)
- **0-1 knapsack greedy fails**: item1=10lbs/$60 ($6/lb), item2=20lbs/$100 ($5/lb), item3=30lbs/$120 ($4/lb); greedy picks item1 then can't fill 50lb → suboptimal; optimal is items2+3=$220
- **Huffman with nearly-uniform frequencies**: no better than fixed-length code (Exercise 15.3-7)
- **Compression cannot guarantee compression for all inputs**: pigeonhole principle (Exercise 15.3-8)

#### Diagrams & Visuals
```
Huffman tree for {a:45, b:13, c:12, d:16, e:9, f:5}:
          [100]
        0/    \1
        a     [55]
        0/       \1
       [25]      [30]
      0/  \1    0/  \1
    [14]   c   d   [14]
    0/ \1       0/ \1
    f   e       b  [13] (cont.)
                   0/ \1
                   ?   ?
      
Fixed-length vs Huffman:
Fixed: a=000,b=001,c=010,d=011,e=100,f=101 → 300,000 bits
Huffman: a=0,b=101,c=100,d=111,e=1101,f=1100 → 224,000 bits (25% savings)
```

```
Activity selection diagram:
a1: ████      selected
a2:  ███
a3: ██████
a4:     ███   selected
a5:    ██████
a6:    ████
a7:      ████
a8:        ███ selected
a9:        ████
a10: ████████████
a11:           ████ selected
```

#### End-of-Chapter Material
- **Key terms**: greedy algorithm, greedy-choice property, optimal substructure, activity selection, compatible, prefix-free code, Huffman code, full binary tree, offline caching, furthest-in-future
- **Exercises**: 15.1-1 (DP for activity selection), 15.1-3 (counterexamples for wrong greedy strategies), 15.2-1 (prove greedy-choice for fractional knapsack), 15.2-2 (DP for 0-1 knapsack O(nW)), 15.3-1 (Huffman proof case), 15.3-3 (Huffman for Fibonacci frequencies), 15.4-2 (LRU not optimal example)

#### Cross-Chapter Links
- **Requires knowledge of**: Ch 14 (DP, optimal substructure), Ch 6 (heaps for Huffman)
- **Referenced in later chapters**: Ch 21 (MST — Kruskal, Prim), Ch 22 (Dijkstra), Ch 35 (greedy set-covering heuristic)

---

### Ch. 16 — Amortized Analysis

#### Named Entities (Terms & Definitions)
- **Amortized analysis**: averaging time over a sequence of operations; guarantees average per-operation cost in the worst case.
- **Aggregate analysis**: total cost T(n) for n operations; amortized cost = T(n)/n (same for all operations).
- **Accounting method**: assign differing amortized costs; overcharge early operations, store credit on specific objects, use credit to pay for undercharged later operations.
- **Potential method**: assign potential Φ(Di) to data structure; amortized cost ĉi = ci + Φ(Di) − Φ(Di-1); prepaid work as "potential energy" of whole structure.
- **Load factor α(T)**: num_items / size (number of slots).
- **Table expansion**: when table fills, allocate new table of double size, copy items.
- **Table contraction**: when load factor drops below 1/4, halve table size.
- **MULTIPOP(S,k)**: pops up to k objects from stack.
- **INCREMENT**: increments k-bit binary counter; flips bits from rightmost 0.

#### Processes / Algorithms / Pathways
##### MULTIPOP(S,k)
- **Goal**: pop min(s, k) objects from stack
- **Steps**: while not STACK-EMPTY(S) and k>0: POP(S); k--.
- **Cost**: min(s, k) where s = stack size

##### INCREMENT(A,k)
- **Goal**: add 1 to k-bit binary counter
- **Steps**: i=0; while i<k and A[i]==1: A[i]=0; i++; if i<k: A[i]=1.
- **Cost**: number of bits flipped (ti + 1, where ti = # of trailing 1s)

##### TABLE-INSERT(T,x)
- **Goal**: insert item into dynamic table, expanding if full
- **Steps**: (1) if T.size==0: allocate with 1 slot. (2) if T.num==T.size: allocate new table with 2·T.size slots; copy all items; free old; T.table=new; T.size=2·T.size. (3) insert x; T.num++.
- **Cost**: 1 (no expansion) or i (expansion at i-th insertion)

#### Classifications & Hierarchies
- **Three amortized analysis methods**:
  - Aggregate: T(n)/n, same for all operations, simplest
  - Accounting: per-operation amortized costs, credit on objects, flexible
  - Potential: Φ function on data structure, most general

#### Comparisons & Trade-offs
| Dimension | Aggregate | Accounting | Potential |
|---|---|---|---|
| Amortized cost | Same for all ops | May differ per op type | May differ per op type |
| Credit storage | None | On specific objects | Data structure as whole |
| Difficulty | Simplest | Medium | Most flexible |
| Key concept | Total cost / n | Overcharge → credit | Φ function |

#### Formulas & Equations
##### Potential method definition
`ĉi = ci + Φ(Di) − Φ(Di-1)`  
Total: `Σ ĉi = Σ ci + Φ(Dn) − Φ(D0)`  
If Φ(Di) ≥ Φ(D0) for all i, total amortized cost ≥ total actual cost.

##### Accounting method invariant
`Σ_{i=1}^n ĉi ≥ Σ_{i=1}^n ci` for all n (credit never negative)

##### Stack — amortized costs (accounting/potential)
Actual: PUSH=1, POP=1, MULTIPOP=min(s,k)  
Amortized: PUSH=2, POP=0, MULTIPOP=0  
Potential Φ = number of objects in stack

##### Binary counter — amortized cost (aggregate)
Total flips in n INCREMENT ops: `Σ_{i=0}^{k-1} ⌊n/2^i⌋ < 2n`  
Amortized: O(1) per operation

##### Binary counter — amortized (accounting)
Setting 0→1 costs $2 ($1 to set, $1 stored as credit).  
Resetting 1→0 costs $0 (paid by stored credit).  
Each INCREMENT sets at most one 0→1 → amortized cost ≤ $2.

##### Binary counter — potential method
Φ = number of 1-bits in counter  
If operation resets ti bits: ci ≤ ti+1, Φ(Di)−Φ(Di-1) ≤ 1−ti  
ĉi ≤ (ti+1)+(1−ti) = 2

##### Dynamic table — aggregate
Cost of i-th insertion: ci = i if i−1 is power of 2, else ci = 1  
Total: `Σ ci ≤ n + Σ_{j=0}^{⌊lg n⌋} 2^j = n + (2n−1) < 3n`  
Amortized: < 3 per insertion

##### Dynamic table — potential
`Φ = 2·num − size` for α ≥ 1/2  
`Φ = size/2 − num` for α < 1/2  
Amortized cost: insert=3 (with/without expansion), delete=1 (with contraction) or 2 (without contraction crossing α=1/2) or 0 (insert crossing up to α=1/2)

##### Dynamic table — expansion/contraction strategy
- Expand: double size when full (α=1)
- Contract: halve size when α < 1/4 (NOT 1/2 — avoids thrashing)

#### Rules, Laws & Theorems
##### Key invariant for aggregate analysis (stack)
- **Statement**: Number of POP operations (including within MULTIPOP) ≤ number of PUSH operations ≤ n.
- **Implication**: Total cost of n PUSH, POP, MULTIPOP operations = O(n).

##### Key insight for binary counter
- **Statement**: Bit A[i] flips ⌊n/2^i⌋ times in sequence of n INCREMENT operations from 0.
- **Implication**: Total flips < 2n, so amortized O(1).

#### Edge Cases & Common Pitfalls
- **Naive bound O(n²) for stack is not tight**: aggregate analysis shows O(n).
- **Naive bound O(nk) for binary counter is not tight**: aggregate analysis shows O(n).
- **Thrashing**: contracting at load factor 1/2 causes Θ(n²) total cost for alternating insert/delete pattern. Solution: contract at α < 1/4, not α < 1/2.
- **Potential function choice**: different Φ give different amortized costs; must ensure Φ(Di) ≥ Φ(D0).
- **DECREMENT in binary counter breaks amortized O(1)**: n ops can cost Θ(nk) (Exercise 16.1-2).

#### Case Studies & Examples
##### Stack aggregate analysis
Sequence of n operations: PUSH, PUSH, MULTIPOP(S,2), POP, PUSH, MULTIPOP(S,3)  
Naive worst-case: each MULTIPOP O(n) → O(n²)  
Actual: each pop corresponds to a previous push → at most n pops total → O(n)

##### Binary counter flips (n=16, k=8)
| Value | Bits (A7..A0) | Flips |
|-------|--------------|-------|
| 0 | 00000000 | — |
| 1 | 00000001 | 1 |
| 2 | 00000010 | 2 |
| 3 | 00000011 | 1 |
| 4 | 00000100 | 3 |
| ... | ... | ... |
| 16 | 00010000 | 1 |
Total flips = 31 < 2·16 = 32

##### Dynamic table expansion sequence
Insert ops 1..16: costs = 1,2,1,4,1,1,1,8,1,1,1,1,1,1,1,16  
Total = 1+2+1+4+1+1+1+8+1+1+1+1+1+1+1+16 = 1+2+4+8+16 = 31 < 3·16 = 48  
Amortized cost per op = 31/16 < 2

#### Diagrams & Visuals
```
Stack with MULTIPOP:
Initial: [A,B,C,D] (A=top)
MULTIPOP(3): pops A,B,C → [D]
Cost: 3 pops = 3 units

Binary counter flips pattern:
Bit A0: flips every time (n times)
Bit A1: flips every 2nd time (n/2)
Bit A2: flips every 4th time (n/4)
...

Dynamic table potential:
  Φ = 2·num − size (when α ≥ ½)
  Φ = size/2 − num (when α < ½)
  
  After expansion (α=½): Φ=0
  As insertions fill table: Φ increases linearly
  At full (α=1): Φ = size (pays for next expansion)
```

#### End-of-Chapter Material
- **Key terms**: amortized analysis, aggregate analysis, accounting method, potential method, credit, potential function, load factor, table expansion, contraction, MULTIPOP
- **Exercises**: 16.1-1 (MULTIPUSH impact), 16.1-2 (DECREMENT breaks amortized), 16.1-3 (powers of 2 cost sequence), 16.2-1 (stack with backups), 16.3-1 (re-zeroing potential), 16.3-5 (queue with two stacks), 16.4-1 (first insertion potential), 16.4-3 (accounting for both insert/delete)

#### Cross-Chapter Links
- **Requires knowledge of**: Ch 10 (stacks), Ch 6 (binary heaps), Ch 11 (hash tables, load factor)
- **Referenced in later chapters**: Ch 17 (augmenting data structures), Ch 19 (disjoint-set forests), Ch 13 (red-black tree amortized analysis)
