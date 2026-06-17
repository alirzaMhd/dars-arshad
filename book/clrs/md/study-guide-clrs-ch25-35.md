# Study Guide: Introduction to Algorithms (CLRS 4e) — Part VII: Selected Topics (Ch 25–35)

> Generated 2026-06-05. Subject: Algorithms. Coverage: Chapters 25–35, examinable content.

## Chapter-by-Chapter Breakdown

### Ch. 25 — Matchings in Bipartite Graphs

#### Named Entities (Terms & Definitions)
- **Matching**: subset M ⊆ E s.t. each vertex has ≤1 incident edge in M
- **Maximum matching**: matching of maximum cardinality
- **M-augmenting path**: alternating path starting & ending with edges in E−M, containing one more edge in E−M than M
- **M-alternating path**: simple path whose edges alternate between M and E−M
- **Stable matching**: matching with no blocking pair
- **Blocking pair**: unmatched pair who each prefer the other over current partner
- **Assignment problem**: find perfect matching maximizing total weight
- **Feasible vertex labeling**: l.h + r.h ≥ w(l,r) for all l∈L, r∈R
- **Equality subgraph**: Gh = (V, Eh) where Eh = {(l,r): l.h + r.h = w(l,r)}

#### Processes / Algorithms / Pathways
##### Hopcroft-Karp (Maximum Bipartite Matching)
- **Type**: Algorithm
- **Goal**: Find maximum matching in O(√V·E) time
- **Steps**: (1) Start with M = ∅. (2) Find maximal set of vertex-disjoint shortest M-augmenting paths. (3) M = M ⊕ {paths}. (4) Repeat until no augmenting paths exist.
- **Complexity**: O(√V · E) time
- **Key Phases per iteration**: (a) Direct edges to form GM (L→R for E−M, R→L for M). (b) BFS to build DAG H of shortest paths. (c) DFS on transpose HT to find maximal vertex-disjoint paths.
- **Example**: Graph L={l1..l7}, R={r1..r8}, matching M of size 4. Found two augmenting paths: (r1,l3,l3,r3,r3,l1) and (r4,l5,l5,r7,r7,l6).

##### Gale-Shapley (Stable Marriage)
- **Type**: Algorithm
- **Goal**: Find a stable matching in complete bipartite graph with rankings
- **Steps**: (1) All free. (2) While ∃ free woman w: w proposes to next man m on her list. (3) If m free → engage. (4) If m prefers w to current fianceé → break engagement, engage with w. (5) Else → reject. (6) Return engaged pairs.
- **Complexity**: O(n²) time
- **Theorem**: Women-optimal, men-pessimal. Always terminates with stable matching.
- **Example**: 4 women (Wanda,Emma,Lacey,Karen) and 4 men (Oscar,Davis,Brent,Hank) → stable matching: (Lacey,Brent), (Wanda,Hank), (Karen,Davis), (Emma,Oscar)

##### Hungarian Algorithm (Assignment Problem)
- **Type**: Algorithm
- **Goal**: Maximum-weight perfect matching in complete bipartite graph
- **Complexity**: O(n⁴) (can be improved to O(n³))
- **Steps**: (1) Initialize feasible vertex labeling h. (2) Build equality subgraph Gh. (3) Find max matching in Gh. (4) If not perfect, update labels and repeat. (5) Perfect matching in Gh is optimal.

#### Classifications & Hierarchies
- Matching types: maximal ⊇ maximum ⊇ perfect
- Stable matching variants: woman-oriented vs man-oriented Gale-Shapley

#### Comparisons & Trade-offs
| Dimension | Hopcroft-Karp | Hungarian |
|---|---|---|
| Problem | Unweighted max matching | Max-weight perfect matching |
| Graph | Bipartite (general) | Complete bipartite |
| Time | O(√V·E) | O(n⁴) |
| Technique | Augmenting paths | Vertex labeling |

#### Formulas & Equations
##### Symmetric difference
`M' = M ⊕ P = (M − P) ∪ (P − M)`
- |M'| = |M| + 1 if P is M-augmenting

##### Maximum matching bound
`|M*| ≤ |M| + |V|/(q+1)`
- q = length of shortest M-augmenting path

#### Rules, Laws & Theorems
##### Hall's Theorem
- **Statement**: Bipartite graph G=(L∪R,E) has perfect matching iff |A| ≤ |N(A)| for all A⊆L
- **Conditions**: |L| = |R|

##### Lemma 25.1
- M ⊕ P where P is M-augmenting gives |M'| = |M|+1

##### Corollary 25.4
- M is maximum iff no M-augmenting path exists

##### Theorem 25.14
- Perfect matching in equality subgraph = optimal solution to assignment problem

#### Edge Cases & Common Pitfalls
- Stable-roommates problem (non-bipartite) may have no stable matching
- Maximal ≠ maximum (e.g., maximal set of augmenting paths may not be maximum)
- Hungarian: zero-weight edges may need careful tie-breaking

#### Diagrams & Visuals
```
Hopcroft-Karp BFS layers:
Layer 0: L unmatched vertices
Layer 1: R neighbors via E−M
Layer 2: L neighbors via M
... alternating until R unmatched found
```

#### End-of-Chapter Material
- **Key terms**: matching, M-augmenting path, stable matching, blocking pair, equality subgraph, feasible labeling
- **Exercises**: 25.1-1 (Hopcroft-Karp on Fig 25.1), 25.2-1 (O(n²) Gale-Shapley impl), 25.3-2 (greedy matching ≥ ½ max)

#### Cross-Chapter Links
- Ch 24 (max flow → max matching via flow network)
- Ch 34 (NP-completeness of general matching variants)
- Ch 27 (online algorithms, competitive analysis)

---

### Ch. 26 — Parallel Algorithms

#### Named Entities (Terms & Definitions)
- **Work (T₁)**: total time to execute on 1 processor (sum of strand times)
- **Span (T∞)**: fastest time on unlimited processors (critical path length)
- **Parallelism**: T₁/T∞ — average work per step along critical path
- **Speedup**: T₁/TP — factor faster on P processors
- **Linear speedup**: T₁/TP = Θ(P); Perfect: T₁/TP = P
- **Parallel slackness**: (T₁/T∞)/P
- **Determinacy race**: two logically parallel instructions access same location, ≥1 modifies it
- **Strand**: chain of instructions with no parallel/procedural control
- **Fork-join parallelism**: model using spawn, sync, parallel for

#### Processes / Algorithms / Pathways
##### Work/Span Analysis
- **Goal**: Bound running time on P processors
- **Steps**: (1) Compute work T₁ (serial projection). (2) Compute span T∞ (longest path in trace DAG). (3) TP ≥ max(T₁/P, T∞). (4) Greedy scheduler achieves TP ≤ T₁/P + T∞.
- **Theorem 26.1**: Greedy scheduling: TP ≤ T₁/P + T∞

##### Parallel Matrix-Vector Multiply (P-MAT-VEC)
- `parallel for i=1..n` outer loop, inner serial loop sums row
- Work: Θ(n²), Span: Θ(n), Parallelism: Θ(n)

#### Comparisons & Trade-offs
| Metric | Formula | Meaning |
|---|---|---|
| Work law | TP ≥ T₁/P | At most P work per step |
| Span law | TP ≥ T∞ | Cannot beat critical path |
| Speedup | S = T₁/TP | P in ideal case |
| Parallelism | T₁/T∞ | Upper bound on S |

#### Rules, Laws & Theorems
##### Corollary 26.2
- Greedy scheduler is within factor 2 of optimal

##### Corollary 26.3
- If P ≪ T₁/T∞ (slackness ≫ 1), then TP ≈ T₁/P (near-perfect speedup)

#### Edge Cases & Common Pitfalls
- Determinacy races cause nondeterministic behavior (e.g., Therac-25, 2003 blackout)
- Span analysis: series composition adds, parallel composition takes max
- High parallelism not always needed beyond 10× slackness

#### Diagrams & Visuals
```
Trace DAG for P-FIB(4):
17 strands total, 8 on critical path
Work = 17, Span = 8, Parallelism = 2.125
```

#### End-of-Chapter Material
- **Key terms**: work, span, parallelism, speedup, slackness, determinacy race, strand, fork-join
- **Exercises**: 26.1-7 (more parallelism in mat-vec)
- **Chess lesson**: Optimization reduced work 2048→1024 but increased span 1→8; on 512 processors, time went from 5s to 10s

#### Cross-Chapter Links
- Ch 2–4 (divide-and-conquer recurrences)
- Ch 27 (online algorithms for scheduling)

---

### Ch. 27 — Online Algorithms

#### Named Entities (Terms & Definitions)
- **Online algorithm**: input arrives progressively; decisions made without future knowledge
- **Offline algorithm**: knows entire input in advance
- **Competitive ratio**: max over all inputs I of A(I)/F(I) where F is optimal offline
- **c-competitive**: competitive ratio = c
- **Inversion count**: I(L, L') = number of pairs whose order differs between lists
- **Cache miss/hit**: block not in cache / in cache
- **Adversary**: oblivious (doesn't know random choices) vs nonoblivious (knows them)

#### Processes / Algorithms / Pathways
##### Move-to-Front (List Maintenance)
- **Goal**: Maintain search list to minimize total access + swap cost
- **Steps**: After searching for element x, swap x forward until it reaches front
- **Cost**: 2r − 1 for element at position r
- **Competitive ratio**: 4 (Theorem 27.1)
- **Proof technique**: Potential function Φ = 2·I(LM, LF)

##### RANDOMIZED-MARKING (Caching)
- **Steps**: (1) On hit → mark block. (2) On miss: if all marked, unmark all. (3) Evict random unmarked block. (4) Load & mark new block.
- **Competitive ratio**: O(lg k) against oblivious adversary

##### LIFO/FIFO/LRU Caching Policies
- **LIFO**: evict newest block — competitive ratio Θ(n/k)
- **LRU**: evict least recently used — competitive ratio Θ(k)
- **Theorem 27.3**: LRU is O(k)-competitive
- **Theorem 27.4**: Any deterministic online caching algorithm is Ω(k)-competitive

#### Comparisons & Trade-offs
| Policy | Competitive Ratio | Strategy |
|---|---|---|
| LIFO | Θ(n/k) | Evict newest |
| LRU | Θ(k) | Evict least recently used |
| FIFO | Θ(k) | Evict longest in cache |
| Randomized-Marking | O(lg k) | Evict random unmarked |

#### Formulas & Equations
##### Competitive Ratio (minimization)
`CR = max_{I∈U} A(I)/F(I)`

##### Elevator Hedging Strategy
- Wait k minutes, then take stairs → competitive ratio = 2 (independent of k, B)

#### Edge Cases & Common Pitfalls
- LIFO can have unbounded competitive ratio (depends on n)
- LRU and FIFO have Θ(k) but k is constant w.r.t. input size
- Randomized algorithms need oblivious adversary for theoretical guarantees

#### End-of-Chapter Material
- **Key terms**: competitive ratio, online/offline, inversion, adversary, cache eviction
- **Exercises**: 27.1-2 (ski rental 2-competitive alg), 27.2-4 (Move-to-Front 2-competitive with free moves), 27.3-1 (LRU epoch analysis)

#### Cross-Chapter Links
- Ch 35 (approximation algorithms, similar ratio analysis)
- Ch 15 (caching, offline furthest-in-future)
- Ch 16 (amortized analysis, potential functions)

---

### Ch. 28 — Matrix Operations

#### Named Entities (Terms & Definitions)
- **LUP decomposition**: PA = LU where L = unit lower-triangular, U = upper-triangular, P = permutation
- **LU decomposition**: A = LU (no pivoting)
- **Schur complement**: A' − vw^T/a₁₁
- **Forward substitution**: solve Ly = Pb for y
- **Back substitution**: solve Ux = y for x
- **Symmetric positive-definite**: A = A^T and x^T A x > 0 for all x ≠ 0
- **Pivot**: diagonal entry used for elimination; pivoting = permuting rows for stability

#### Processes / Algorithms / Pathways
##### LUP-Solve
- **Goal**: Solve Ax = b given LUP decomposition
- **Steps**: (1) Forward substitution: Ly = Pb. (2) Back substitution: Ux = y.
- **Complexity**: Θ(n²)

##### LU-Decomposition
- **Steps**: For k=1..n: (1) u_kk = a_kk. (2) l_ik = a_ik/a_kk for i>k. (3) u_ki = a_ki for i>k. (4) Update Schur complement: a_ij = a_ij − l_ik·u_kj.
- **Complexity**: Θ(n³)

##### LUP-Decomposition (with pivoting)
- **Steps**: For k=1..n: (1) Find pivot row k' with max |a_ik| in column k. (2) Swap rows k and k'. (3) Update permutation π. (4) Compute multipliers and Schur complement.
- **Complexity**: Θ(n³)

#### Formulas & Equations
##### Forward substitution
`y_i = b_π[i] − Σ_{j=1}^{i-1} l_ij·y_j`
- Solves Ly = Pb

##### Back substitution
`x_i = (y_i − Σ_{j=i+1}^{n} u_ij·x_j) / u_ii`
- Solves Ux = y

##### Matrix inversion from LUP
- Solve AX_i = e_i for each column X_i → O(n³) total

##### Multiplication ⇔ Inversion (Theorem 28.1-28.2)
- M(n) = O(I(n)) and I(n) = O(M(n)) equivalence

#### Rules, Laws & Theorems
##### Lemma 28.3
- Positive-definite ⇒ nonsingular

##### Theorem 28.1
- Matrix inversion is no harder than multiplication (construct 3n×3n block matrix)

##### Theorem 28.2
- Matrix multiplication is no harder than inversion (for symmetric positive-definite via Schur complement recursion)

#### Edge Cases & Common Pitfalls
- LU fails when pivot = 0 → need pivoting
- Numerical stability: pivoting on max absolute value mitigates roundoff
- Symmetric positive-definite matrices require no pivoting

#### End-of-Chapter Material
- **Key terms**: LUP decomposition, forward/back substitution, Schur complement, pivoting, symmetric positive-definite
- **Exercises**: 28.1-2 (LU decomposition), 28.1-3 (LUP solve), 28.2-2 (LUP from mat-mul)

#### Cross-Chapter Links
- Ch 4 (Strassen's matrix multiplication, O(n^lg7))
- Ch 29 (linear programming)
- Appendix D (matrix basics)

---

### Ch. 29 — Linear Programming

#### Named Entities (Terms & Definitions)
- **Linear program**: optimize linear function subject to linear constraints
- **Standard form**: max c^T x s.t. Ax ≤ b, x ≥ 0
- **Objective function**: c^T x (linear function to optimize)
- **Feasible solution**: satisfies all constraints
- **Optimal solution**: feasible with max/min objective value
- **Feasible region**: set of all feasible solutions (convex polyhedron = simplex)
- **Dual**: minimization LP derived from primal max LP; optimal values equal
- **Simplex algorithm**: moves along edges of feasible region to reach optimum vertex
- **Integer linear program**: LP with x ∈ ℤ constraint — NP-hard

#### Processes / Algorithms / Pathways
##### Formulating an LP
- **Steps**: (1) Identify decision variables. (2) Specify linear constraints. (3) Define linear objective function. (4) Add nonnegativity constraints.
- **Example**: Political problem — minimize cost to win votes given effectiveness matrix

##### Simplex Algorithm (conceptual)
- **Steps**: (1) Start at feasible vertex. (2) Move along edge to neighbor with better objective. (3) Repeat until local (hence global) optimum reached.
- **Complexity**: Exponential worst-case, polynomial average-case

##### Ellipsoid & Interior-Point Methods
- Polynomial-time: ellipsoid (first polynomial LP algorithm), interior-point (practical)

#### Comparisons & Trade-offs
| Algorithm | Type | Time | Notes |
|---|---|---|---|
| Simplex | Vertex-following | Exp. worst-case | Most used in practice |
| Ellipsoid | Polynomial | O(n⁶L²) | Theoretical, slow in practice |
| Interior-point | Polynomial | O(n³L) | Moves through interior |

#### Formulas & Equations
##### Standard Form LP
`max c^T x`
`s.t. Ax ≤ b, x ≥ 0`
- x ∈ ℝⁿ, A ∈ ℝ^(m×n), b ∈ ℝ^m, c ∈ ℝⁿ

##### Dual LP (for max primal)
`min b^T y`
`s.t. A^T y ≥ c, y ≥ 0`

##### Shortest Path as LP
`max d_t`
`s.t. d_v ≤ d_u + w(u,v) for all (u,v)∈E, d_s = 0`

#### Rules, Laws & Theorems
##### Duality Theorem
- Optimal primal value = optimal dual value (if both feasible)
- **Weak duality**: c^T x ≤ b^T y for any feasible primal x, dual y
- **Strong duality**: equality at optimality

#### Edge Cases & Common Pitfalls
- Infeasible LP: no solution satisfying all constraints
- Unbounded LP: feasible but objective can increase without bound
- Integer LP is NP-hard; LP relaxation (drop integrality) gives bound

#### End-of-Chapter Material
- **Key terms**: objective function, constraints, feasible region, simplex, duality, primal/dual
- **Exercises**: 29.1-1 (feasible solutions), 29.2-1 (shortest path as LP)

#### Cross-Chapter Links
- Ch 22 (shortest paths as LP)
- Ch 24 (max flow as LP)
- Ch 34 (integer programming NP-complete)
- Ch 35 (LP for approximation algorithms)

---

### Ch. 30 — Polynomials and the FFT

#### Named Entities (Terms & Definitions)
- **Polynomial**: A(x) = Σ a_j x^j, degree bound n
- **Coefficient representation**: vector a = (a₀, a₁, …, a_{n−1})
- **Point-value representation**: {(x₀, y₀), …, (x_{n−1}, y_{n−1})} where y_k = A(x_k)
- **DFT (Discrete Fourier Transform)**: y_k = A(ω_n^k) for k=0..n−1, ω_n principal nth root of unity
- **FFT (Fast Fourier Transform)**: computes DFT in Θ(n lg n) time
- **Convolution**: c = a ⊗ b where c_j = Σ a_k·b_{j−k} — polynomial multiplication
- **Interpolation**: convert point-value → coefficients (inverse DFT)
- **Vandermonde matrix**: V_jk = ω_n^{jk}

#### Processes / Algorithms / Pathways
##### FFT (Cooley-Tukey)
- **Goal**: Compute polynomial evaluation at nth roots of unity in Θ(n lg n)
- **Steps**: (1) If n=1, return a. (2) Split into A_even(x) (even indices) and A_odd(x) (odd indices). (3) Recursively compute FFT on each (size n/2). (4) Combine: y_k = y_even_k + ω^k·y_odd_k; y_{k+n/2} = y_even_k − ω^k·y_odd_k.
- **Complexity**: T(n) = 2T(n/2) + Θ(n) = Θ(n lg n)
- **Example**: Multiply (6x³+7x²−10x+9)(−2x³+4x−5) via FFT: (1) pad to degree 8, (2) FFT both, (3) pointwise multiply, (4) inverse FFT

##### Efficient Polynomial Multiplication
- **Steps**: (1) Double degree-bound (add n zeros). (2) Evaluate at 2nth roots of unity (FFT). (3) Pointwise multiply. (4) Interpolate (inverse FFT).
- **Complexity**: Θ(n lg n)

#### Formulas & Equations
##### Complex nth Roots of Unity
`ω_n = e^{2πi/n}`
- ω_n^k for k=0..n−1 are all nth roots
- **Cancellation lemma**: ω_{dn}^{dk} = ω_n^k
- **Halving lemma**: (ω_n^k)^2 = ω_{n/2}^k for even n
- **Summation lemma**: Σ_{j=0}^{n−1} (ω_n^k)^j = 0 if n ∤ k

##### DFT Matrix
`y = V_n a` where V_n[jk] = ω_n^{jk}
- **Inverse**: V_n^{-1}[jk] = ω_n^{−jk}/n

##### Lagrange Interpolation
`A(x) = Σ y_k · Π_{j≠k} (x−x_j)/(x_k−x_j)`

#### Rules, Laws & Theorems
##### Theorem 30.1 (Uniqueness)
- n distinct point-value pairs determine unique degree-bound n polynomial

##### Theorem 30.2
- Polynomial multiplication in coefficient form in Θ(n lg n) time

##### Convolution Theorem
- a ⊗ b = IDFT(DFT(a) · DFT(b))

#### Edge Cases & Common Pitfalls
- FFT requires n to be a power of 2 (pad with zeros otherwise)
- Inverse DFT: replace ω_n by ω_n^{−1} and divide by n
- For non-power-of-2, use Bluestein's algorithm or zero-padding

#### Diagrams & Visuals
```
FFT butterfly:
    y_even_k ──⊕── y_k = y_even_k + ω^k·y_odd_k
               ╱
            ω^k
               ╲
    y_odd_k ───⊕── y_{k+n/2} = y_even_k − ω^k·y_odd_k
```

#### End-of-Chapter Material
- **Key terms**: DFT, FFT, convolution, roots of unity, butterfly operation, twiddle factors
- **Exercises**: 30.1-1 (polynomial multiplication), 30.2-2 (DFT of (0,1,2,3))

#### Cross-Chapter Links
- Ch 28 (Vandermonde matrix)
- Ch 31 (modular arithmetic, number-theoretic transform analogue)

---

### Ch. 31 — Number-Theoretic Algorithms

#### Named Entities (Terms & Definitions)
- **GCD**: greatest common divisor; gcd(a,b) = smallest positive linear combination ax+by
- **Relatively prime**: gcd(a,b) = 1
- **Modular equivalence**: a ≡ b (mod n) iff n | (a−b)
- **Group (S, ⊕)**: closed, associative, identity, inverses; abelian if commutative
- **ℤₙ**: integers modulo n under addition; ℤₙ*: multiplicative group (units mod n)
- **Euler's φ function**: φ(n) = |ℤₙ*| = n·Π_{p|n} (1−1/p)
- **Primitive root (generator)**: g such that ⟨g⟩ = ℤₙ*
- **Discrete logarithm**: ind_{n,g}(a) = z where g^z ≡ a (mod n)

#### Processes / Algorithms / Pathways
##### Euclid's Algorithm (GCD)
- **Goal**: Compute gcd(a,b) for a ≥ b ≥ 0
- **Steps**: (1) If b=0, return a. (2) Else return Euclid(b, a mod b).
- **Complexity**: O(lg b) recursive calls; O(β²) bit ops for β-bit numbers
- **Example**: Euclid(99,78) → Euclid(78,21) → Euclid(21,15) → Euclid(15,6) → Euclid(6,3) → Euclid(3,0) → 3

##### Extended-Euclid
- **Goal**: Find x,y such that d = gcd(a,b) = ax + by
- **Steps**: (1) If b=0, return (a,1,0). (2) Recursively get (d',x',y') for (b, a mod b). (3) Return (d', y', x' − ⌊a/b⌋·y').
- **Example**: Extended-Euclid(99,78) → (3, −11, 14) since 3 = 99·(−11) + 78·14

##### Modular Linear Equation Solver
- **Goal**: Solve ax ≡ b (mod n)
- **Steps**: (1) Compute d = gcd(a,n), x' from Extended-Euclid. (2) If d∤b → no solution. (3) x₀ = x'·(b/d) mod n. (4) Solutions: x_i = x₀ + i·(n/d) for i=0..d−1.

##### Repeated Squaring (Modular Exponentiation)
- **Goal**: Compute a^b mod n efficiently
- **Steps**: (1) If b=0 return 1. (2) If b even: (a^{b/2})² mod n. (3) If b odd: a·(a^{b−1}) mod n.
- **Complexity**: O(lg b) multiplications

#### Formulas & Equations
##### GCD Recursion Theorem
`gcd(a,b) = gcd(b, a mod b)`

##### Euler's Theorem
`a^{φ(n)} ≡ 1 (mod n)` for gcd(a,n)=1

##### Fermat's Theorem
`a^{p−1} ≡ 1 (mod p)` for prime p, a not divisible by p

##### Chinese Remainder Theorem
- n = n₁n₂…n_k, pairwise coprime
- a ↔ (a mod n₁, …, a mod n_k) is bijection
- a = Σ a_i · c_i (mod n), where c_i = m_i·(m_i^{−1} mod n_i), m_i = n/n_i

#### Rules, Laws & Theorems
##### Lamé's Theorem
- Euclid(a,b) makes < k recursive calls if b < F_{k+1} (Fibonacci)
- ⇒ O(lg b) calls

##### Lagrange's Theorem
- |subgroup| divides |group|

##### Unique Prime Factorization (Theorem 31.8)
- Every integer has unique prime factorization

#### Edge Cases & Common Pitfalls
- Modular inverse exists iff gcd(a,n)=1
- If n has nontrivial square roots of 1 → n is composite (Corollary 31.35)
- Working modulo prime vs composite: ℤₚ* is cyclic, ℤₙ* may not be

#### Diagrams & Visuals
```
Extended-Euclid recursion (99,78):
a b ⌊a/b⌋  d   x    y
99 78   1   3  −11  14
78 21   3   3   3  −11
21 15   1   3  −2   3
15 6    2   3   1  −2
 6 3    2   3   0   1
 3 0    —   3   1   0
```

#### End-of-Chapter Material
- **Key terms**: gcd, modular arithmetic, extended Euclid, CRT, φ(n), discrete log, repeated squaring
- **Exercises**: 31.1-2 (infinitely many primes), 31.2-2 (Extended-Euclid(899,493)), 31.4-1 (35x=10 mod 50)

#### Cross-Chapter Links
- Ch 30 (roots of unity in complex vs. finite fields)
- Ch 33 (machine learning, randomness)
- RSA cryptosystem (Sec 31.7)

---

### Ch. 32 — String Matching

#### Named Entities (Terms & Definitions)
- **String matching**: find all occurrences of pattern P[1:m] in text T[1:n]
- **Valid shift**: s where T[s+1:s+m] = P[1:m]
- **Prefix**: w ⊏ x if x = wy; **Suffix**: w ⊐ x if x = yw
- **Suffix function**: σ(x) = length of longest prefix of P that is suffix of x
- **Prefix function π**: π[q] = max{k < q : P[:k] ⊐ P[:q]}
- **Finite automaton**: 5-tuple (Q, q₀, A, Σ, δ) for string matching

#### Processes / Algorithms / Pathways
##### Naive String Matching
- **Steps**: For each shift s=0..n−m, check P[1:m] == T[s+1:s+m]
- **Complexity**: O((n−m+1)·m) worst-case
- **Example**: P=aaab, T=aaaaaaab → Θ((n−m+1)m)

##### Rabin-Karp (Rolling Hash)
- **Goal**: Average-case O(n+m) string matching
- **Steps**: (1) Compute p = P mod q. (2) Compute t₀ = T[1:m] mod q. (3) For each shift: if t_s = p (hit), verify equality. (4) Compute t_{s+1} = (d·(t_s − T[s+1]·h) + T[s+m+1]) mod q.
- **Complexity**: Θ(m) preprocessing, O((n−m+1)·m) worst-case, O(n+m) expected
- **Example**: P=31415, q=13, T=... (Fig 32.4). Window values mod 13; spurious hit at position 13

##### Finite Automaton Matcher
- **Steps**: (1) Precompute δ(q,a) = σ(P[:q]a). (2) For each T[i]: q = δ(q, T[i]); if q=m → match.
- **Complexity**: O(m|Σ|) preprocessing, Θ(n) matching

##### Knuth-Morris-Pratt (KMP)
- **Goal**: Θ(n) matching with Θ(m) preprocessing (no Σ factor)
- **Steps**: (1) Compute prefix function π[1:m]. (2) Scan T: while q>0 and P[q+1]≠T[i], q=π[q]; if match, q++. If q=m, found.
- **Complexity**: Θ(m) + Θ(n)
- **Key insight**: π[q] gives longest proper prefix of P[:q] that is also a suffix

#### Comparisons & Trade-offs
| Algorithm | Preprocessing | Matching | Space |
|---|---|---|---|
| Naive | 0 | O((n−m+1)m) | O(1) |
| Rabin-Karp | Θ(m) | O((n−m+1)m) / expected O(n+m) | O(1) |
| Finite Automaton | O(m|Σ|) | Θ(n) | O(m|Σ|) |
| KMP | Θ(m) | Θ(n) | Θ(m) |
| Suffix Array | O(n lg n) | O(m lg n + k·m) | O(n) |

#### Formulas & Equations
##### Rabin-Karp Rolling Hash
`t_{s+1} = (d·(t_s − T[s+1]·h) + T[s+m+1]) mod q`
- h = d^{m−1} mod q
- d = radix (e.g., 10 for decimal, 256 for ASCII)

##### Prefix Function
`π[q] = max{k < q : P[:k] ⊐ P[:q]}`

#### Rules, Laws & Theorems
##### Lemma 32.5 (Prefix iteration)
- π*[q] = {k < q : P[:k] ⊐ P[:q]}; iterating π generates all proper prefix-suffix matches

#### Edge Cases & Common Pitfalls
- Rabin-Karp: spurious hits when hash matches but strings differ (choose large prime q to minimize)
- Naive is O(n²) worst-case (e.g., P = a^m, T = a^n)
- KMP: after finding match at q=m, set q=π[m] to continue scanning

#### Diagrams & Visuals
```
KMP prefix function π for P=ababaca:
q:   1 2 3 4 5 6 7
π:   0 0 1 2 3 0 1

Finite automaton states:
0→a→1→b→2→a→3→b→4→a→5→c→6→a→7 (accept)
Back edges from each state on mismatch use prefix function
```

#### End-of-Chapter Material
- **Key terms**: valid shift, prefix/suffix, automaton, prefix function, rolling hash
- **Exercises**: 32.1-1 (naive comparisons), 32.2-1 (Rabin-Karp spurious hits), 32.4-1 (compute π)

#### Cross-Chapter Links
- Ch 31 (modular arithmetic for Rabin-Karp)
- Ch 12 (Trie, suffix tree)

---

### Ch. 33 — Machine-Learning Algorithms

#### Named Entities (Terms & Definitions)
- **Supervised learning**: training data has labels → learn hypothesis for prediction
- **Unsupervised learning**: no labels (e.g., clustering)
- **k-means clustering**: partition n points into k clusters minimizing sum of squared distances to centroids
- **Centroid (mean)**: d-dimensional point where each coordinate = mean of cluster values
- **Lloyd's procedure**: iterates assign-to-nearest-center + recompute-centroids
- **Dissimilarity**: squared Euclidean distance Δ(x,y) = Σ(x_a − y_a)²
- **Multiplicative weights**: maintain weights per expert, decrease on mistakes
- **Weighted majority**: predict based on weighted vote of experts
- **Gradient descent**: iterative optimization following negative gradient
- **Convex function**: f(λx + (1−λ)y) ≤ λf(x) + (1−λ)f(y)

#### Processes / Algorithms / Pathways
##### Lloyd's Procedure (k-means)
- **Goal**: Find locally optimal k-clustering
- **Steps**: (1) Choose k initial centers randomly. (2) Assign each point to nearest center. (3) If no change → stop. (4) Recompute centers as centroids. (5) Go to step 2.
- **Complexity**: O(T·d·k·n) where T = iterations
- **Example**: 49 US capitals → k=4 clusters after 11 iterations

##### Weighted-Majority (Multiplicative Weights)
- **Goal**: Limit mistakes vs best expert
- **Steps**: (1) Initialize all weights = 1. (2) For each event: (a) Sum weights predicting 1 vs 0. (b) Predict majority. (c) Multiply incorrect experts' weights by (1−γ).
- **Theorem 33.4**: m ≤ 2(1+γ)·m* + (2 ln n)/γ
- **Corollary 33.5**: m ≤ 2·m* + O(log n) when γ = 1/2

##### Gradient Descent
- **Goal**: Minimize convex function f : ℝⁿ → ℝ
- **Steps**: (1) Start at x(0). (2) For t=0..T−1: x(t+1) = x(t) − γ·∇f(x(t)). (3) Return avg of points.
- **Theorem 33.8**: f(x_avg) − f(x*) ≤ O(LR/T) where L bounds gradient, R bounds distance from start

#### Comparisons & Trade-offs
| Algorithm | Type | Guarantee | Complexity |
|---|---|---|---|
| Lloyd's k-means | Clustering | Local minimum | O(T·d·k·n) |
| Weighted-Majority | Online learning | 2·m* + O(log n) mistakes | O(n·T) |
| Gradient Descent | Optimization | f(x) − f(x*) ≤ ε | O(L²R²/ε²) |

#### Formulas & Equations
##### k-means Objective
`f(S,C) = Σ_{ℓ=1}^{k} Σ_{x∈S(ℓ)} Δ(x, c(ℓ))` = sum of squared distances to cluster centroids

##### Weighted-Majority Mistake Bound
`m ≤ 2(1+γ)·m* + (2 ln n)/γ`
- m = algorithm mistakes, m* = best expert mistakes, γ ∈ (0, ½]

#### Edge Cases & Common Pitfalls
- k-means: NP-hard to find global optimum (local minimum only)
- Gradient descent may converge to local minimum (not global) for non-convex functions
- Step size too large → overshoot; too small → slow convergence
- Weighted majority: weights may approach 0 for perpetually wrong experts

#### End-of-Chapter Material
- **Key terms**: clustering, centroid, Lloyd's procedure, multiplicative weights, gradient descent, convex function
- **Exercises**: 33.1-1 (alternative k-means objective), 33.2-2 (ln (1−x) bounds), 33.3-1 (convex function property)

#### Cross-Chapter Links
- Ch 27 (online algorithms, competitive analysis)
- Ch 29 (linear programming)
- Ch 34 (NP-hardness of k-means)

---

### Ch. 34 — NP-Completeness

#### Named Entities (Terms & Definitions)
- **P**: problems solvable in polynomial time
- **NP**: problems verifiable in polynomial time (certificate)
- **NPC (NP-complete)**: hardest problems in NP; all NP problems reduce to them
- **NP-hard**: at least as hard as all NP problems (may not be in NP)
- **Reduction**: polynomial-time transformation from problem A to problem B (A ≤_P B)
- **Decision problem**: yes/no answer (vs optimization problem)
- **Circuit-SAT**: given boolean circuit, is there satisfying assignment?
- **SAT**: boolean formula satisfiability
- **3-CNF-SAT**: SAT where formula is AND of ORs of 3 literals each
- **CLIQUE**: does graph contain complete subgraph of size k?
- **VERTEX-COVER**: does graph have vertex cover of size ≤ k?
- **HAM-CYCLE**: does graph have Hamiltonian cycle?
- **TSP**: traveling salesperson tour of cost ≤ k?
- **SUBSET-SUM**: does subset sum to target t?

#### Processes / Algorithms / Pathways
##### Reduction Methodology
- **Goal**: Prove problem B is NP-complete
- **Steps**: (1) Show B ∈ NP (certificate verifiable in polynomial time). (2) Reduce known NP-complete A to B. (3) Show reduction is polynomial time. (4) Show x ∈ A ⇔ f(x) ∈ B.

##### Cook-Levin Theorem (Circuit-SAT is NP-complete)
- Any NP problem can be reduced to CIRCUIT-SAT by encoding the verification algorithm as a circuit
- Key insight: configuration of Turing machine computation → boolean circuit

#### Classifications & Hierarchies
```
         NP
    ┌────┴────┐
    P        NPC
    (tractable)  (intractable if P≠NP)
```

#### Comparisons & Trade-offs
| Problem | Known Time | Status |
|---|---|---|
| Shortest path (unweighted) | O(V+E) | ∈ P |
| Longest simple path | ? | NP-complete |
| Euler tour | O(E) | ∈ P |
| Hamiltonian cycle | ? | NP-complete |
| 2-CNF SAT | O(m+n) | ∈ P |
| 3-CNF SAT | ? | NP-complete |
| Linear programming | polynomial | ∈ P |
| Integer linear programming | ? | NP-hard |

#### Formulas & Equations
##### Reduction for NP-Completeness Proof
`L₁ ≤_P L₂`: ∃ polynomial-time f s.t. x ∈ L₁ ⇔ f(x) ∈ L₂
- If L₂ ∈ P then L₁ ∈ P
- If L₁ ∈ NPC then L₂ ∈ NPC (when L₂ ∈ NP)

#### Rules, Laws & Theorems
##### Theorem 34.4
- If any NP-complete problem is polynomial-time solvable, then P = NP

##### Lemma 34.8
- If L' ∈ NPC and L' ≤_P L, then L is NP-hard; if L ∈ NP, then L ∈ NPC

##### Cook-Levin Theorem (34.7)
- CIRCUIT-SAT is NP-complete

#### Edge Cases & Common Pitfalls
- Optimization vs decision: show decision version hard → optimization version hard
- Encoding matters (unary vs binary can change complexity class)
- Reduction must be polynomial in instance size

#### Diagrams & Visuals
```
Reduction Chain (Section 34.4-34.5):
CIRCUIT-SAT → SAT → 3-CNF-SAT
                          ↓
                    SUBSET-SUM ← HAM-CYCLE → TSP
                         ↗
              CLIQUE ← VERTEX-COVER
```

#### End-of-Chapter Material
- **Key terms**: P, NP, NPC, reduction, certificate, Cook-Levin, 3-CNF-SAT, HAM-CYCLE, TSP, CLIQUE, VERTEX-COVER, SUBSET-SUM
- **Exercises**: 34.2-1 (graph isomorphism ∈ NP), 34.5-1 (CLIQUE reduction)

#### Cross-Chapter Links
- Ch 35 (approximation algorithms for NP-complete problems)
- Ch 29 (integer programming NP-hard)
- Ch 22 (shortest path ∈ P vs longest path NP-complete)

---

### Ch. 35 — Approximation Algorithms

#### Named Entities (Terms & Definitions)
- **Approximation ratio ρ(n)**: C/C* ≤ ρ(n) for minimization; C*/C ≤ ρ(n) for maximization
- **ρ(n)-approximation algorithm**: achieves ratio ρ(n)
- **Approximation scheme**: (1+ε)-approximation for any ε > 0
- **PTAS**: polynomial-time approximation scheme (time polynomial in n for fixed ε)
- **FPTAS**: fully polynomial-time (time polynomial in n and 1/ε)
- **Maximal matching**: matching where no more edges can be added

#### Processes / Algorithms / Pathways
##### APPROX-VERTEX-COVER (2-approximation)
- **Goal**: Find vertex cover within factor 2 of optimal
- **Steps**: (1) C = ∅, E' = G.E. (2) While E' ≠ ∅: pick any (u,v) ∈ E', add u,v to C, remove all edges incident on u or v. (3) Return C.
- **Complexity**: O(V+E)
- **Proof**: Let A = edges picked. |C*| ≥ |A| (each edge needs distinct vertex). |C| = 2|A| ≤ 2|C*|.

##### APPROX-TSP-TOUR (2-approx with triangle inequality)
- **Goal**: TSP tour within factor 2 of optimal (when triangle inequality holds)
- **Steps**: (1) Compute MST T. (2) Preorder walk of T gives tour H.
- **Complexity**: Θ(V²)
- **Proof**: c(T) ≤ c(H*); full walk W costs 2·c(T); triangle inequality gives c(H) ≤ c(W) ≤ 2·c(H*).

##### Greedy-Set-Cover (O(lg n)-approximation)
- **Goal**: Find subfamily C ⊆ ℱ covering all elements, near-minimum size
- **Steps**: (1) U₀ = X, C = ∅. (2) While U_i ≠ ∅: pick S ∈ ℱ maximizing |S ∩ U_i|; U_{i+1} = U_i − S; C = C ∪ {S}.
- **Complexity**: O(|X|·|ℱ|·(|X|+|ℱ|))
- **Theorem 35.4**: |C| ≤ |C*|·⌈ln |X|⌉

##### APPROX-MIN-WEIGHT-VC (LP-rounding, 2-approximation)
- **Steps**: (1) Form LP relaxation: min Σ w(v)·x(v) s.t. x(u)+x(v) ≥ 1, 0 ≤ x(v) ≤ 1. (2) Solve LP. (3) Include v iff x(v) ≥ ½.

##### Randomized MAX-3-CNF-SAT (8/7-approximation)
- **Steps**: Set each variable to 1 with prob ½, 0 with prob ½.
- **Guarantee**: Expected clauses satisfied = 7m/8, ratio ≤ 8/7.

##### APPROX-SUBSET-SUM (FPTAS)
- **Goal**: Subset sum within (1+ε) of optimal, time polynomial in n and 1/ε
- **Steps**: (1) Maintain sorted list of subset sums ≤ t. (2) After each merge, trim list δ = ε/(2n). (3) Return max in L_n.
- **Complexity**: O(n·log t / δ) = poly(n, 1/ε)

#### Comparisons & Trade-offs
| Problem | Algorithm | Ratio | Time | Type |
|---|---|---|---|---|
| Vertex Cover | APPROX-VC | 2 | O(V+E) | Deterministic |
| Weighted VC | LP-rounding | 2 | poly(n) | LP-based |
| TSP (triangle) | MST+preorder | 2 | Θ(V²) | Deterministic |
| TSP (general) | — | Any ρ ≥ 1 | — | Imposs. unless P=NP |
| Set Cover | Greedy | O(ln n) | O(|X|·|ℱ|·|X|+|ℱ|) | Greedy |
| Subset Sum | APPROX-SS | 1+ε | poly(n,1/ε) | FPTAS |
| MAX-3-CNF-SAT | Random | 8/7 | O(m) | Randomized |

#### Formulas & Equations
##### Approximation Ratio
`max(C/C*, C*/C) ≤ ρ(n)`

##### TSP lower bound via MST
`c(T) ≤ c(H*)` (deleting edge from tour gives spanning tree)

#### Rules, Laws & Theorems
##### Theorem 35.3 (TSP inapproximability)
- Unless P=NP, no constant-factor approximation for general TSP

##### Theorem 35.4 (Set cover)
- Greedy Set-Cover is O(ln |X|)-approximation

##### Theorem 35.6 (Weighted VC)
- LP-rounding gives 2-approximation

##### Theorem 35.7 (Subset Sum)
- APPROX-SUBSET-SUM is FPTAS

#### Edge Cases & Common Pitfalls
- General TSP has NO constant-factor approximation unless P=NP
- Vertex cover: 2-approximation, but vertex cover is NP-complete
- Set cover lower bound: cannot be approximated better than Ω(ln n) unless P=NP
- FPTAS exists only for some NP-complete problems (subset-sum yes, TSP no)

#### End-of-Chapter Material
- **Key terms**: approximation ratio, PTAS, FPTAS, vertex cover, TSP, set cover, subset sum, LP rounding
- **Exercises**: 35.1-1 (suboptimal vertex cover example), 35.2-3 (closest-point TSP heuristic), 35.3-1 (set cover tie-breaking)

#### Cross-Chapter Links
- Ch 34 (NP-completeness: all problems here are NP-hard)
- Ch 29 (linear programming for approximation)
- Ch 27 (competitive analysis analogous to approximation ratio)

---

## Cross-Cutting Topics

### Design Paradigms & Meta-Methods
- **Divide & Conquer**: FFT (Ch 30), Parallel matrix multiplication (Ch 26), LUP decomposition (Ch 28)
- **Greedy**: Maximum bipartite matching (Ch 25), Set cover approximation (Ch 35)
- **Dynamic Programming**: Subset-sum exact algorithm (Ch 35)
- **Linear Programming**: LP-rounding for vertex cover (Ch 35), Duality (Ch 29)
- **Fork-Join Parallelism**: Spawn/sync model (Ch 26)
- **Online / Competitive**: Elevator, Move-to-Front, Caching (Ch 27)
- **Reduction**: NP-completeness proofs via polynomial reduction (Ch 34)
- **Rounding (LP→IP)**: Fractional solution → integral via threshold (Ch 35)
- **Potential Function**: Move-to-Front analysis (Ch 27), Gradient descent (Ch 33)

### Proof & Argument Patterns
- **Loop Invariant**: Hopcroft-Karp (Ch 25), KMP (Ch 32)
- **Induction**: Euclid's algorithm analysis (Ch 31), prefix function correctness (Ch 32)
- **Contradiction**: Gale-Shapley correctness (Ch 25)
- **Reduction Proof**: NP-completeness (Ch 34)
- **Potential Function**: Move-to-Front competitive ratio (Ch 27), gradient descent (Ch 33)
- **Work/Span**: Parallel algorithms analysis (Ch 26)
- **Exchange Argument**: Augmenting paths (Ch 25)

### People & Dates
- **Gale-Shapley (1962)**: Stable marriage algorithm
- **Hopcroft-Karp (1973)**: Maximum bipartite matching
- **Kuhn (1955) / Munkres (1957)**: Hungarian algorithm
- **Cooley-Tukey (1965)**: FFT
- **Euclid (~300 BCE)**: GCD algorithm
- **Rabin-Karp (1987)**: String matching with rolling hash
- **Knuth-Morris-Pratt (1977)**: Linear-time string matching
- **Lloyd (1982)**: k-means clustering
- **Littlestone & Warmuth (1994)**: Weighted majority
- **Cook (1971)**: NP-completeness, Cook-Levin theorem
- **Karp (1972)**: 21 NP-complete problems

### Mnemonics & Memory Aids
- **FTT** (FFT pattern): Formulate (pad), Transform (FFT), Times (multiply), Transform back (inverse FFT)
- **RSA** requires: Repeated squaring, φ(n), Extended Euclid, CRT
- **KMP prefix**: π[q] = longest proper prefix of P[:q] that is also suffix
- **NP-complete reductions chain**: CIRCUIT-SAT → SAT → 3-SAT → CLIQUE → VERTEX-COVER → HAM-CYCLE → TSP, and 3-SAT → SUBSET-SUM
- **Online competitive ratios**: Move-to-Front (4), LRU (k), Randomized-Marking (lg k)
