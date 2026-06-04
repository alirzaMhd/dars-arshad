# CLRS 4e — Comprehensive Study Notes: Chapters 26–35

---

## Chapter 26: Parallel Algorithms

### Fork-Join Model
- **spawn**: a subroutine may execute in parallel with the caller — do not wait for it to finish
- **sync**: wait for all spawned children to complete
- **parallel for (pfor)**: all iterations run in parallel; implemented via recursive spawning (divide-and-conquer)
- The computation is a **dag** (directed acyclic graph) of **strands** (sequential instruction sequences)

### Work and Span
- **Work T₁(n)**: total number of operations (time on 1 processor)
- **Span T∞(n)**: length of the longest path in the dag (critical path, time on infinite processors)
- **Tₚ(n)** = time on P processors
- **Work Law**: Tₚ ≥ T₁ / P
- **Span Law**: Tₚ ≥ T∞
- **Speedup**: T₁ / Tₚ — **linear speedup** = Θ(P), **perfect linear speedup** = P
- **Parallelism**: T₁ / T∞ — maximum possible speedup

### Greedy Scheduling
- A **greedy scheduler** never leaves a processor idle when work is available
- **Theorem (Graham–Brent)**: Tₚ ≤ T₁ / P + T∞
- Corollary: Tₚ = O(T₁ / P + T∞)
- **Linear speedup** when T₁ / T∞ = Ω(P) i.e. parallelism ≥ P

### Key Parallel Algorithms
- **P-MERGE(A₁, A₂, B)**: merge two sorted arrays in parallel
  - Pick median of larger array, binary search in other, recurse on two independent subproblems
  - Work: Θ(n), Span: Θ(lg² n), Parallelism: Θ(n / lg² n)
- **P-MATRIX-MULTIPLY(A, B)**: parallel divide-and-conquer matrix multiply
  - Partition 2×2 block, spawn 8 sub-multiplies, then sum
  - Work: Θ(n³), Span: Θ(lg n), Parallelism: Θ(n³ / lg n)
- **P-SAMPLE-SORT**: parallel sorting via random sampling
  - Work: Θ(n lg n), Span: Θ(lg² n) with high probability
- **Parallel Fibonacci**: spawn recursive calls, work Θ(φⁿ), span Θ(n) — terrible parallelism
- **Parallel loops (pfor)**: implemented via binary splitting / divide-and-conquer

### Scheduling Theory Formulas
- Tₚ ≥ max(T₁ / P, T∞)
- T₁ / T∞ ≥ P ⇒ greedy gives linear speedup
- **Brent's Theorem**: Tₚ ≤ T₁ / P + T∞

---

## Chapter 27: Online Algorithms

### Key Concepts
- **Offline algorithm**: knows entire input sequence in advance
- **Online algorithm**: processes input sequentially, makes irrevocable decisions without future knowledge
- **Competitive analysis**: compare online algorithm's cost to optimal offline algorithm's cost
- **Competitive ratio ρ**: for all inputs, C_ONLINE ≤ ρ · C_OPT + α (or strictly C_ONLINE ≤ ρ · C_OPT)

### Wait-for-Elevator Problem (Ski-Rental)
- **Problem**: rent skis at $1/day or buy for $B; don't know how many days you'll ski
- **Deterministic**: rent for B-1 days, buy on day B → competitive ratio 2 − 1/B
- **Randomized**: mixed strategy → competitive ratio e/(e−1) ≈ 1.582 (optimal)
- **Key insight**: deterministic ratio approaches 2, randomized gives better

### List Accessing / Move-to-Front (MTF)
- **Problem**: maintain a linked list, pay access cost = position of accessed element, can reorder after each access
- **Deterministic MTF**: after accessing an element, move it to front
- **Competitive ratio**: MTF is 2-competitive against optimal offline (with transpositions cost 1)
- **Other heuristics**: Frequency Count (FC), Transpose — not competitive

### Caching (Paging)
- **Problem**: two-level memory (cache + main), cache holds k pages; on miss (fault), fetch page into cache, evict one
- **Deterministic algorithms**: LRU, FIFO, LIFO, Random, Marking
- **LRU**: evict least-recently used page
- **FIFO**: evict page brought in earliest
- **LIFO**: evict most recently brought in — not competitive (can be arbitrarily bad)
- **Marking algorithm**: mark pages when referenced; on fault, evict unmarked page; if all marked, unmark all and continue
- **Competitive ratio of deterministic algorithms**: k-competitive (LRU, FIFO, Marking); no deterministic can do better than k
- **LIFO**: unbounded competitive ratio

### Randomized Caching
- **Random Marking**: each unmarked page equally likely to be evicted
- **Competitive ratio**: O(lg k) with high probability; 2H_k-competitive (H_k = harmonic number)
- **Lower bound**: any randomized algorithm has Ω(lg k) competitive ratio

### Markov Chains (for predictably-requested paging)
- States = reference pattern states; transition matrix P
- **Markov chain on a cycle**: sequence of requested pages correlated
- **Competitive ratio against Markov adversary**: LRU is O(lg k) for certain Markov chains

### Key Results
- No deterministic online paging algorithm can have competitive ratio < k
- Randomized paging can achieve Θ(lg k) competitive ratio
- MTF gives constant (2) competitive ratio for list accessing
- Ski-rental randomized bound e/(e−1) is optimal

---

## Chapter 28: Matrix Operations

### LUP Decomposition
- **LUP decomposition**: PA = LU where L = unit lower-triangular, U = upper-triangular, P = permutation matrix
- Solves Ax = b in Θ(n²) after decomposition
- **LUP-SOLVE(A, b)**: forward substitution (Ly = Pb), then back substitution (Ux = y)
- **LUP-DECOMPOSITION(A)**: Gaussian elimination with partial pivoting; Θ(n³)
- Pivoting ensures numerical stability

### Matrix Inversion
- Computing A⁻¹ via LUP decomposition: solve A · X = I (n systems) → Θ(n³)
- **Strassen-based inversion**: also Θ(n^lg7) ≈ Θ(n^2.81) using divide-and-conquer

### Positive-Definite Matrices
- **Definition**: A is positive-definite if xᵀAx > 0 for all x ≠ 0
- Equivalent: all eigenvalues > 0, all leading principal minors > 0
- **Cholesky decomposition**: A = LLᵀ (L = lower-triangular with positive diagonal)
- Faster than LU: half the work → Θ(n³/3) vs Θ(2n³/3)

### Least-Squares Approximation
- **Problem**: minimize ||Ax − b||₂ for overdetermined system (m > n)
- **Normal equations**: AᵀAx = Aᵀb
- Solve via LUP of AᵀA (cost Θ(n²m)) or Cholesky of AᵀA (if AᵀA positive-definite)
- **Alternative**: QR decomposition (Householder reflections) — more numerically stable

### Key Formulas
- Forward substitution: O(n²)
- Back substitution: O(n²)
- LUP decomposition: O(n³)
- Matrix multiplication: O(n³) (naive), O(n^lg7) (Strassen)

---

## Chapter 29: Linear Programming

### LP Formulation
- **Objective**: maximize/minimize cᵀx subject to Ax ≤ b, x ≥ 0
- **Standard form**: maximize cᵀx, Ax ≤ b, x ≥ 0
- **Slack form**: equality constraints + slack variables
- Convert inequality to equality: add slack variable s = b − Ax ≥ 0
- **Basic solution**: set nonbasic variables = 0, basic variables from equality

### Duality
- **Primal (max)**: maximize cᵀx, Ax ≤ b, x ≥ 0
- **Dual (min)**: minimize bᵀy, Aᵀy ≥ c, y ≥ 0
- **Weak duality**: cᵀx ≤ bᵀy for all feasible x, y
- **Strong duality**: if primal has optimal x*, dual has optimal y* with cᵀx* = bᵀy*
- **Complementary slackness**: for optimal x*, y*:
  - xⱼ > 0 ⇒ Σᵢ aᵢⱼyᵢ* = cⱼ
  - yᵢ > 0 ⇒ Σⱼ aᵢⱼxⱼ* = bᵢ

### Simplex Algorithm (Conceptual)
- Start at a basic feasible solution
- Repeatedly pivot: swap a nonbasic variable into basis to increase objective
- **Entering variable**: nonbasic with positive coefficient in objective
- **Leaving variable**: basic that hits zero first (minimum ratio test)
- Exponential worst-case (Klee–Minty cube), but polynomial smoothed complexity
- **Pivot rules**: Bland's rule avoids cycling, largest-coefficient, steepest-edge

### Ellipsoid Method
- First polynomial-time LP algorithm (Khachiyan)
- Theoretical O(n⁶) — not practical
- Works by shrinking an ellipsoid around the feasible region

### Interior-Point Methods
- Practical polynomial-time (Karmarkar)
- Move through interior of feasible region, not along edges
- O(n³) per iteration, O(√n) iterations

### Network Simplex
- Specialized simplex for min-cost flow / max flow
- Tree-based basis representation
- Much faster than general simplex for network problems

### Key Exam Points
- Standard vs slack form conversion
- Dual construction
- Complementary slackness for checking optimality
- Minimum ratio test for leaving variable
- Cycling & Bland's rule

---

## Chapter 30: Polynomials and FFT

### Polynomial Representations
- **Coefficient form**: A(x) = Σ aⱼ xʲ | evaluation: Θ(n), multiplication: Θ(n²)
- **Point-value form**: {(x₀, y₀), ..., (x_{n-1}, y_{n-1})} | multiplication: Θ(n), interpolation: Θ(n²)

### DFT and FFT
- **nth roots of unity**: ωₙ = e^{2πi/n}
- **Principal root**: ωₙ; all roots = ωₙ⁰, ωₙ¹, ..., ωₙ^{n-1}
- **Properties**: ωₙⁿ = 1, ωₙ^{k+n/2} = −ωₙ^{k} (cancellation), (ωₙ^{k})² = ω_{n/2}^{k}
- **DFT**: evaluate at n roots of unity → Yⱼ = A(ωₙʲ)
- **FFT (Cooley–Tukey)**:
  - Divide: A⁰(x) = a₀ + a₂x + ... (even), A¹(x) = a₁ + a₃x + ... (odd)
  - A(ωₙᵏ) = A⁰(ω_{n/2}ᵏ) + ωₙᵏ A¹(ω_{n/2}ᵏ)
  - A(ωₙ^{k+n/2}) = A⁰(ω_{n/2}ᵏ) − ωₙᵏ A¹(ω_{n/2}ᵏ)
  - Recursive: T(n) = 2T(n/2) + Θ(n) → Θ(n lg n)
- **Iterative FFT (bit-reversal permutation)**: avoids recursion overhead

### Convolution
- Polynomial multiplication = convolution of coefficient vectors
- Compute via: coefficient → FFT → pointwise multiply → inverse FFT → Θ(n lg n)
- **Inverse DFT**: use ωₙ^{-1}, divide by n

### Schonhage–Strassen Algorithm
- Multiplication of large integers via FFT
- Recursive: multiply n-bit numbers → O(n lg n lg lg n)
- Uses modular arithmetic with roots of unity over finite rings

### Key Formulas
- A(x) · B(x) = C(x) where cₖ = Σᵢ₊ⱼ₌ₖ aᵢ bⱼ
- DFT matrix: F_{jk} = ωₙ^{jk} / √n (normalized unitary)
- ωₙ ⋅ ω̅ₙ = 1
- **Bluestein's algorithm**: FFT for arbitrary-length sequences

---

## Chapter 31: Number-Theoretic Algorithms

### Divisibility and GCD
- **a | b**: ∃ integer k, b = ak
- **Properties**: if a|b and a|c then a|(b+c), a|(bc)
- **Theorem**: a|b and b|a ⇒ a = ±b

### Euclid's Algorithm
- EUCLID(a, b): while b ≠ 0, (a, b) = (b, a mod b)
- Running time: O(lg b) divisions (worst-case: consecutive Fibonacci numbers)
- Proof uses **Lamé's theorem**: if a > b ≥ 1, number of divisions ≤ lg_φ(b) + 1

### Extended Euclid
- EXTENDED-EUCLID(a, b): returns (d, x, y) where d = gcd(a, b) = ax + by
- Used to compute modular inverses

### Modular Arithmetic
- ℤₙ = {0, 1, ..., n−1} with +, × mod n
- **Multiplicative inverse**: a⁻¹ mod n exists iff gcd(a, n) = 1
- ℤₙ* = set of units (invertible elements)
- φ(n) = Euler's totient = |ℤₙ*| = n ∏_{p|n} (1−1/p)

### Modular Exponentiation
- MODULAR-EXPONENTIATION(a, b, n): computes a^b mod n in Θ(lg b) time
- Method: square-and-multiply (right-to-left binary exponentiation)
- **Important**: never compute a^b then mod — exponential intermediate values

### RSA Cryptosystem
- **Key generation**:
  - Pick large primes p, q
  - n = pq
  - Choose e such that gcd(e, φ(n)) = 1 (typically 65537)
  - d ≡ e⁻¹ (mod φ(n))
  - Public key: (n, e); Private key: d
- **Encryption**: c = m^e mod n
- **Decryption**: m = c^d mod n
- **Correctness**: m^{ed} ≡ m (mod n) by Euler's theorem (if gcd(m,n)=1)
- **Signing**: s = m^d mod n; verify: s^e mod n = m
- **Security**: factoring n = pq is hard

### Primality Testing
- **Fermat test**: a^{n−1} ≡ 1 (mod n) — Carmichael numbers fool it
- **Miller–Rabin**:
  - Write n−1 = 2^s · d (d odd)
  - Test: compute a^d mod n, repeatedly square
  - Check for nontrivial square roots of 1
  - Probability of false positive ≤ 1/4 per iteration
  - Run k iterations → error ≤ 4^{−k}
- **AKS test**: first deterministic polynomial-time primality test (Agrawal–Kayal–Saxena)
  - Õ(log¹⁰·⁵ n) originally, improved to Õ(log⁶ n)

### Chinese Remainder Theorem
- System x ≡ aᵢ (mod nᵢ) for pairwise coprime nᵢ has unique solution mod N = ∏ nᵢ
- Solution: x = Σ aᵢ · Nᵢ · yᵢ where Nᵢ = N/nᵢ, yᵢ = Nᵢ⁻¹ (mod nᵢ)

### Fermat and Euler Theorems
- **Fermat's Little Theorem**: a^{p−1} ≡ 1 (mod p) for prime p, a not divisible by p
- **Euler's Theorem**: a^{φ(n)} ≡ 1 (mod n) for gcd(a, n) = 1

### Discrete Logarithms
- Problem: find x such that g^x ≡ h (mod p)
- **Hard** for large primes — basis of Diffie–Hellman
- **Baby-step giant-step**: time O(√n), space O(√n)
- **Pohlig–Hellman**: exploits smooth order

### Factoring Algorithms
- **Pollard's rho**: O(√p) for smallest prime factor p; uses Floyd's cycle detection
- **Fermat factorization**: n = x² − y² = (x−y)(x+y), effective when factors close
- Pollard's p−1, Quadratic sieve, GNFS (for RSA-sized numbers)

### Key Formulas
- gcd(a,b) · lcm(a,b) = |ab|
- a ≡ b (mod n) ⇒ n | (a−b)
- ordₙ(g) = smallest k > 0 s.t. g^k ≡ 1 (mod n)
- Primitive root: g with ord = φ(n) (exists iff n = 2, 4, p^k, 2p^k)

---

## Chapter 32: String Matching

### Notation
- Text T[1..n], pattern P[1..m], alphabet Σ
- Shift s: valid if T[s+1..s+m] = P[1..m]

### Naive String Matcher
- Check each shift s = 0..n−m → O((n−m+1)m)
- Worst case: T=aaaa...a, P=aaa → Θ(nm)

### Rabin–Karp
- Compute hash of pattern and each text window
- Hash: base-d integer modulo q
- Rolling hash: t_{s+1} = (d(t_s − T[s+1]·d^{m−1}) + T[s+m+1]) mod q
- Checks characters only when hash matches
- Expected O(n+m) (hash collisions rare with good hash)
- Worst case O(nm) (many collisions)
- **Key formula**: hash(P) = (P[1]·d^{m−1} + P[2]·d^{m−2} + ... + P[m]) mod q

### Finite Automaton Matcher
- Build transition function δ(q, a) for q = 0..m, a ∈ Σ
- δ(q, a) = length of longest prefix of P that is suffix of P_q + a
- Match: O(n + m|Σ|) preprocess + O(n) scan
- Automaton is DFA: states 0..m, state m = accepting

### Knuth–Morris–Pratt (KMP)
- **Prefix function π**: π[q] = length of longest proper prefix of P that is suffix of P[1..q]
- **COMPUTE-PREFIX-FUNCTION**: O(m) — matches against itself
- **KMP-MATCHER**: scans T with pointer q tracking longest prefix matched
- On mismatch: q = π[q] (no backtracking in T)
- Time: O(n + m)
- Key property: π is computed incrementally; π[q] ≤ π[q−1] + 1

### Suffix Arrays
- Suffix array SA[i] = starting index of i-th lexicographically smallest suffix
- Built in O(n) via SA-IS / induced sorting, or O(n lg n) via doubling
- Used with LCP array (longest common prefix between adjacent suffixes)
- LCP construction: Kasai's algorithm O(n)
- Applications: pattern matching in O(m lg n) (binary search SA) or O(m + lg n) (LCP-augmented)

### Key Comparisons
| Algorithm | Preprocessing | Matching | Space |
|-----------|:---:|:---:|:---:|
| Naive | 0 | O(nm) | 0 |
| Rabin–Karp | O(m) | O(n+m) avg | O(1) |
| Finite Automaton | O(m|Σ|) | O(n) | O(m|Σ|) |
| KMP | O(m) | O(n) | O(m) |
| Suffix Array | O(n) | O(m lg n) | O(n) |

---

## Chapter 33: Machine-Learning Algorithms

### Clustering & Lloyd's (k-Means) Procedure
- **Input**: set S of n points in ℝ^d, integer k
- **k-means problem**: find k centers C = 〈c^(1),...,c^(k)〉 minimizing f(S,C) = Σ_x min_j Δ(x, c^(j))
- Δ(x,y) = squared Euclidean distance ||x−y||²
- **Centroid** of cluster = pointwise mean of points in that cluster

#### Lloyd's Procedure
1. Initialize k centers (pick random points from S)
2. Assign each point to nearest center (nearest-center rule)
3. If no changes, stop
4. Recompute centers as centroids of clusters; go to 2

**Guarantees**: converges to local minimum; each iteration strictly decreases f
**Running time**: O(T d k n) per iteration
**Properties**: centroid gives optimal center for given cluster (Theorem 33.1); nearest-center rule optimal for given centers (Theorem 33.2)

### Multiplicative-Weight Algorithms
- **Problem**: online prediction with n experts; each round t, each expert predicts 0/1, learner predicts, outcome revealed
- **Goal**: minimize mistakes relative to best expert (regret = m − m*)
- **Weighted-Majority algorithm**:
  - Maintain weight w_i^(t) for each expert
  - Predict: majority vote weighted by w_i
  - On error: multiply wrong experts' weights by (1−γ), 0 < γ ≤ 1/2
- **Theorem 33.4**: m ≤ 2(1+γ) m* + (2 ln n)/γ
- **Corollary 33.5**: m ≤ 2m* + O(ln n) with γ = 1/2
- **Lemma 33.3**: If one perfect expert exists, algorithm makes ≤ ⌈lg n⌉ mistakes
- **Randomized variant**: expected regret (1+ε)m* + (ln n)/ε — better by factor ~2

### Gradient Descent
- **Goal**: minimize convex function f : ℝ^n → ℝ
- **Gradient ∇f**: vector of partial derivatives; points direction of steepest ascent
- **Update**: x^(t+1) = x^(t) − γ · (∇f)(x^(t)) (γ = step size)
- **Return**: x-avg = average of all iterates

#### Key Theorems
- **Lemma 33.6** (convex functions lie above tangent): f(x) ≥ f(y) + ⟨∇f(y), x−y⟩
- **Theorem 33.8**: f(x-avg) − f(x*) ≤ RL/√T where R = ||x⁰−x*||, L = max ||∇f||
- Number of iterations for error ε: T = R²L²/ε²

#### Constrained Gradient Descent
- **Projection**: Π_K(x) = point in K closest to x
- **Lemma 33.10**: projection cannot increase distance to any point in K
- **Theorem 33.11**: same asymptotic bound as unconstrained

#### Applications
- **Linear regression**: minimize ||Aw−b||² → w = A⁻¹b (or approximate via GD)
- **Hessian**: ∇²f matrix of second derivatives; convex iff positive-semidefinite
- **α-strongly convex**: gradient descent achieves linear convergence O(L²/(αT))
- **β-smooth**: alternative convergence bounds

### Key Definitions
- **Convex function**: f(λx + (1−λ)y) ≤ λf(x) + (1−λ)f(y)
- **Loss function**: L(w) = Σ (f(x^(i)) − y^(i))² (least-squares)
- **Regularization**: add penalty ||w||² to avoid overfitting

---

## Chapter 34: NP-Completeness

### Complexity Classes
- **P**: languages decidable in polynomial time O(n^k)
- **NP**: languages verifiable in polynomial time (certificate-based)
- **co-NP**: languages L where complement L ∈ NP
- **NPC**: NP-complete — hardest in NP (NP ∩ NP-hard)
- **P ≠ NP** is the central open question (most believe true)
- P ⊆ NP, P ⊆ co-NP
- If any NPC problem ∈ P, then P = NP

### Decision vs Optimization Problems
- Decision problem: answer yes/no
- Optimization → decision by adding bound k
- If decision is easy, optimization is easy (converse for hardness)
- Example: SHORTEST-PATH → PATH(G, u, v, k)

### Polynomial-Time Reductions
- **L₁ ≤ₚ L₂**: exists polynomial-time computable f s.t. x ∈ L₁ ⇔ f(x) ∈ L₂
- **Lemma 34.3**: L₁ ≤ₚ L₂ and L₂ ∈ P ⇒ L₁ ∈ P
- Reductions preserve polynomial-time solvability
- **Transitive**: if L₁ ≤ₚ L₂ and L₂ ≤ₚ L₃ then L₁ ≤ₚ L₃

### Circuit Satisfiability (CIRCUIT-SAT)
- **Instance**: boolean combinational circuit (AND/OR/NOT gates, no cycles)
- **Question**: does there exist an assignment making output = 1?
- **Theorem 34.7**: CIRCUIT-SAT is NP-complete
- **Lemma 34.5**: CIRCUIT-SAT ∈ NP (certificate = wire values)
- **Lemma 34.6**: CIRCUIT-SAT is NP-hard (encode any NP computation as circuit)

### Formula Satisfiability (SAT)
- **Instance**: boolean formula with variables, connectives (∧, ∨, ¬, →, ↔)
- **Theorem 34.9**: SAT is NP-complete
- **Reduction from CIRCUIT-SAT**: introduce variable for each wire, clause per gate

### 3-CNF Satisfiability (3-CNF-SAT)
- **k-CNF**: AND of clauses, each clause = OR of exactly k literals (variable or ¬variable)
- **Theorem 34.10**: 3-CNF-SAT is NP-complete
- **Reduction from SAT**:
  1. Parse formula → parse tree with variables for internal nodes
  2. Convert each clause to CNF via truth table + DeMorgan
  3. Convert to exactly 3 literals per clause using auxiliary variables p, q

### CLIQUE
- **Instance**: graph G, integer k
- **Question**: does G contain a complete subgraph (clique) of size k?
- **Theorem 34.11**: CLIQUE is NP-complete
- **Reduction from 3-CNF-SAT**: vertex per literal occurrence, edges between consistent literals in different clauses
- Size-k clique ⇔ satisfying assignment

### Vertex Cover (VERTEX-COVER)
- **Instance**: graph G, integer k
- **Question**: does G have a vertex set of size k covering all edges?
- **Theorem 34.12**: VERTEX-COVER is NP-complete
- **Reduction from CLIQUE via complement graph**: G has k-clique ⇔ G (complement) has |V|−k vertex cover

### Hamiltonian Cycle (HAM-CYCLE)
- **Instance**: undirected graph G
- **Question**: does G have a simple cycle visiting each vertex exactly once?
- **Theorem 34.13**: HAM-CYCLE is NP-complete
- **Reduction from VERTEX-COVER**: construct gadget Γ_uv per edge + selector vertices
- Gadget enforces: cycle traverses each edge's gadget in one of 3 patterns

### Traveling Salesperson (TSP)
- **Instance**: complete graph G, cost function c, integer k
- **Question**: does G have a tour (hamiltonian cycle) of total cost ≤ k?
- **Theorem 34.14**: TSP is NP-complete
- **Reduction from HAM-CYCLE**: cost 0 for existing edges, 1 for non-edges

### Subset-Sum (SUBSET-SUM)
- **Instance**: set S of positive integers, target t
- **Question**: does there exist subset S' ⊆ S summing to exactly t?
- **Theorem 34.15**: SUBSET-SUM is NP-complete
- **Reduction from 3-CNF-SAT**: base-10 digits, variable numbers v_i/¬v_i, slack variables s_j/s'_j, target = n variable-digits of 1 + k clause-digits of 4

### Reduction Strategies
- ✗ Common pitfall: reducing to rather than from a known NP-complete problem
- **General → specific**: restrict output (not input)
- **Use structure of source problem** (e.g., 3-CNF over arbitrary formulas)
- **Special cases**: X NP-hard + special case of Y ⇒ Y NP-hard
- **Domain matching**: graph → graph is easier; cross-domain (SAT → CLIQUE) works too
- **Rewards and penalties**: low cost for desired edges, high for undesired
- **Gadgets**: enforce structural constraints in the target problem

### Key Results
- 2-CNF-SAT ∈ P (reduce to strongly connected components of implication graph)
- GRAPH-ISOMORPHISM ∈ NP (certificate = permutation)
- TAUTOLOGY ∈ co-NP
- Set-Partition is NP-complete (special case of Subset-Sum)
- Hamiltonian-Path is NP-complete (similar to HAM-CYCLE)
- 3-Colorability is NP-complete
- Independent Set is NP-complete (complement of vertex cover)
- 0-1 Integer Programming is NP-complete

---

## Chapter 35: Approximation Algorithms

### Performance Ratios
- **ρ(n)-approximation algorithm**: C ≤ ρ(n) · C* (minimization) or C* ≤ ρ(n) · C (maximization)
- ρ(n) ≥ 1 always
- 1-approximation = exact algorithm
- **Polynomial-time approximation scheme (PTAS)**: for any ε > 0, (1+ε)-approximation in time polynomial in n (may have factor like n^{1/ε})
- **Fully PTAS (FPTAS)**: polynomial in both n and 1/ε

### Vertex Cover (2-Approximation)
- **APPROX-VERTEX-COVER**: pick any edge (u,v), add both to C, remove all incident edges; repeat
- **Theorem 35.1**: O(V+E) time, 2-approximation
- Proof: edges picked = maximal matching A; |C*| ≥ |A|; |C| = 2|A| ≤ 2|C*|
- Weighted version: LP relaxation + rounding (APPROX-MIN-WEIGHT-VC)

### TSP — Triangle Inequality (2-Approximation)
- **APPROX-TSP-TOUR**:
  - Compute MST (Prim's)
  - Return vertices in preorder of MST walk
- **Theorem 35.2**: 2-approximation when c satisfies triangle inequality
- Proof: c(T) ≤ c(H*) (MST lower bound); full walk = 2c(T); shortcutting preserves ≤2c(H*)

### General TSP — No Constant Approximation
- **Theorem 35.3**: If P ≠ NP, no polynomial-time ρ-approximation for general TSP for any ρ ≥ 1
- Proof: create cost 1 for edges in G, cost (ρ|V|+1) for others
- Gap: Hamiltonian cycle ⇔ tour cost ≤ |V| vs ≥ ρ|V|+|V|

### Set Cover (Greedy)
- **GREEDY-SET-COVER**: at each step, pick set covering most remaining uncovered elements
- **Theorem 35.4**: O(lg |X|)-approximation
- Proof: |U_i| ≤ |X|(1−1/k)^i; solve for i when |U_i| < 1 → i ≤ k · ⌈ln |X|⌉

### MAX-3-CNF Satisfiability (Randomized 8/7)
- **Theorem 35.5**: random assignment (each var 1 with prob 1/2) gives expected 7/8 of maximum satisfiable clauses
- Approximation ratio: m / (7m/8) = 8/7
- Analysis: each clause independent, P(satisfied) = 7/8, linearity of expectation

### Weighted Vertex Cover via LP
- **APPROX-MIN-WEIGHT-VC**:
  - Solve LP relaxation: min Σ w(v)x(v) s.t. x(u)+x(v) ≥ 1, 0 ≤ x(v) ≤ 1
  - Round: include v iff x(v) ≥ 1/2
- **Theorem 35.6**: 2-approximation
- Proof: z* ≤ w(C*) (LP lower bound); w(C) ≤ 2 Σ v w(v)·x(v) = 2z* ≤ 2w(C*)

### Subset-Sum (FPTAS)
- **EXACT-SUBSET-SUM**: compute all reachable sums ≤ t via merge; O(2^n) worst-case
- **APPROX-SUBSET-SUM**: trim each list L_i with δ = ε/2n before merging
  - **TRIM(L, δ)**: keep only values where y_i > last·(1+δ)
- **Theorem 35.7**: FPTAS — running time polynomial in n and 1/ε
- After trimming: list length ≤ ⌊log_{1+δ} t⌋ + 2 = O((lg t)/δ) = O(n lg t / ε)
- y*/z* ≤ 1+ε where y* = optimal, z* = returned value

### Key Results
- Maximum matching via greedy: 2-approximation, O(E) time
- Bin packing first-fit: 2-approximation
- Parallel machine scheduling (greedy list): 2-approximation
- 0-1 Knapsack: 2-approximation via fractional knapsack rounding
- Christofides for TSP with triangle inequality: 3/2-approximation

---

## Cross-Chapter Dependencies

| Chapter | Depends On | Used In |
|---------|-----------|---------|
| 26 (Parallel) | Recurrences (Ch 4), Sorting (Ch 2-8, 17) | — |
| 27 (Online) | Probability (App C) | — |
| 28 (Matrices) | Matrices (App D), Divide-and-Conquer (Ch 4) | 33 (Gradient descent) |
| 29 (LP) | Matrices (App D) | 35 (Weighted VC via LP) |
| 30 (FFT) | Complex numbers (App C), Divide-and-Conquer (Ch 4) | — |
| 31 (Number Theory) | Modular arithmetic, Induction | 34 (RSA example) |
| 32 (String Matching) | Finite automata, DP (Ch 15) | — |
| 33 (ML) | Vectors (App D), Probability (App C), Convexity (App C), LP (Ch 29) | — |
| 34 (NP-Completeness) | Graphs (App B), Formulas, Reductions | 35 (Approximation) |
| 35 (Approximation) | 34 (NP-completeness), 29 (LP), Greedy (Ch 16) | — |

## High-Weight Exam Topics

1. **NP-completeness reductions** (Ch 34) — knowing the standard reduction patterns (SAT → 3-CNF → CLIQUE → VERTEX-COVER → HAM-CYCLE → TSP, and 3-CNF → SUBSET-SUM)
2. **Work/span analysis** (Ch 26) — computing T₁, T∞, parallelism, applying Brent's theorem
3. **Competitive analysis** (Ch 27) — proving/predicting competitive ratios for paging (LRU, FIFO, marking) and ski-rental
4. **Gradient descent convergence** (Ch 33) — Theorem 33.8, potential function analysis, constrained vs unconstrained
5. **Approximation algorithm proof methods** (Ch 35) — lower bounding C* (matching, MST, LP relaxation), relating C to the bound
6. **FFT** (Ch 30) — polynomial multiplication via convolution, recursive and iterative FFT
7. **RSA** (Ch 31) — key generation, encryption/decryption, modular exponentiation, Euler's theorem
8. **LUP decomposition** (Ch 28) — forward/back substitution, solving systems, least-squares
9. **LP duality** (Ch 29) — weak/strong duality, complementary slackness
10. **String matching** (Ch 32) — KMP prefix function, Rabin–Karp rolling hash
