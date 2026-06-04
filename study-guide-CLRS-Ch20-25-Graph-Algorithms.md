# Study Guide: CLRS 4e — Part VI: Graph Algorithms (Chapters 20–25)

> Generated 2026-06-04. Subject: Computer Science (Graph Algorithms). Exam format: Mixed (MCQ, short answer, problem-solving). Coverage: Comprehensive — every examinable primitive extracted.

---

## Ch. 20 — Elementary Graph Algorithms

### Named Entities (Terms & Definitions)

| Term | Definition |
|------|-----------|
| **Graph** | G = (V, E), where V is vertex set, E is edge set |
| **Directed graph (digraph)** | Edges have direction (u→v) |
| **Undirected graph** | Edges have no direction |
| **Sparse graph** | \|E\| ≪ \|V\|² |
| **Dense graph** | \|E\| ≈ \|V\|² |
| **Adjacency-list representation** | Array Adj[\|V\|] of lists; each list Adj[u] contains v for each edge (u,v) ∈ E |
| **Adjacency-matrix representation** | \|V\|×\|V\| matrix A where aᵢⱼ = 1 if (i,j) ∈ E, 0 otherwise |
| **Weighted graph** | Each edge has weight w: E → ℝ |
| **Weight function** | w: E → ℝ mapping edges to real numbers |
| **Source vertex** | Distinguished start vertex s |
| **Distance (unweighted)** | Minimum number of edges from s to v, denoted δ(s,v) |
| **Shortest-path distance** | δ(s,v) = min number of edges on any path from s to v (∞ if unreachable) |
| **Breadth-first tree** | Predecessor subgraph Gπ from BFS; rooted at s, contains unique shortest path to each reachable vertex |
| **Depth-first forest** | Predecessor subgraph Gπ from DFS; may contain multiple trees |
| **Depth-first tree** | A single tree in the depth-first forest |
| **Timestamp** | DFS assigns discovery time v.d and finish time v.f to each vertex |
| **Parenthesis structure** | Discovery/finish intervals are properly nested |
| **Tree edge** | Edge in the DFS forest (v discovered via this edge) |
| **Back edge** | Edge (u,v) connecting u to an ancestor v in a DFS tree (includes self-loops) |
| **Forward edge** | Nontree edge (u,v) connecting u to a proper descendant v |
| **Cross edge** | All other edges (between non-ancestor-related vertices or different trees) |
| **Topological sort** | Linear ordering of DAG vertices such that if (u,v) ∈ E, u appears before v |
| **Directed acyclic graph (dag)** | Directed graph with no cycles |
| **Strongly connected component (SCC)** | Maximal set C ⊆ V such that ∀u,v ∈ C, u ⇝ v and v ⇝ u |
| **Transpose graph** | Gᵀ = (V, Eᵀ) where Eᵀ = {(v,u) : (u,v) ∈ E} |
| **Component graph** | Gˢᶜᶜ = (Vˢᶜᶜ, Eˢᶜᶜ); one vertex per SCC; edge between components if any edge between them exists |
| **Predecessor subgraph** | Gπ = (Vπ, Eπ) where Vπ = {v ∈ V : v.π ≠ NIL} ∪ {s}, Eπ = {(v.π, v)} |
| **Universal sink** | Vertex with in-degree \|V\|−1 and out-degree 0 |
| **Incidence matrix** | \|V\|×\|E\| matrix B where bᵢⱼ = 1 if edge j leaves i, −1 if enters i, 0 otherwise |
| **Articulation point** | Vertex whose removal disconnects the graph |
| **Bridge** | Edge whose removal disconnects the graph |
| **Biconnected component** | Maximal set of edges where any two lie on a common simple cycle |

### Processes / Algorithms

#### BFS (Breadth-First Search)
- **Type**: Graph search algorithm
- **Goal**: Find shortest path (in number of edges) from source s to all reachable vertices; build breadth-first tree
- **Input**: Graph G = (V,E), source vertex s
- **Output**: For each v: v.d = δ(s,v), v.π = predecessor on shortest path
- **Data structures**: FIFO queue Q, color attributes (WHITE/GRAY/BLACK)

**Pseudocode**:
```
BFS(G, s)
1  for each vertex u ∈ G.V – {s}
2     u.color = WHITE
3     u.d = ∞
4     u.π = NIL
5  s.color = GRAY
6  s.d = 0
7  s.π = NIL
8  Q = Ø
9  ENQUEUE(Q, s)
10 while Q ≠ Ø
11    u = DEQUEUE(Q)
12    for each vertex v in G.Adj[u]
13       if v.color == WHITE
14          v.color = GRAY
15          v.d = u.d + 1
16          v.π = u
17          ENQUEUE(Q, v)
18    u.color = BLACK
```

**Steps**:
1. Initialize all vertices white, ∞ distance, NIL parent
2. Color source gray, set s.d = 0, enqueue s
3. Loop: dequeue u, examine all neighbors v
4. If v is white: set v.d = u.d+1, v.π = u, enqueue v
5. After all neighbors examined, color u black
6. Continue until queue empty

**Loop invariant**: Queue Q consists of exactly the gray vertices.

**Complexity**: O(V + E) time, O(V) space (queue + colors). Linear in graph size.

**Proof of correctness** (Theorem 20.5): BFS discovers every reachable vertex, and v.d = δ(s,v) for all v. Proof by contradiction: let v be vertex with minimum δ(s,v) where v.d > δ(s,v). Show each color (white/gray/black) gives contradiction.

**Properties**:
- v.d ≥ δ(s,v) always (Lemma 20.2)
- Queue contains vertices with d values in nondecreasing order, at most two distinct values k and k+1 (Lemma 20.3)
- Corollary 20.4: enqueued d values monotonically increase

#### PRINT-PATH
```
PRINT-PATH(G, s, v)
1  if v == s
2     print s
3  elseif v.π == NIL
4     print "no path from" s "to" v "exists"
5  else  PRINT-PATH(G, s, v.π)
6     print v
```
- **Complexity**: O(length of path)

#### DFS (Depth-First Search)
- **Type**: Graph search algorithm
- **Goal**: Explore graph deeply; assign discovery/finish timestamps; classify edges
- **Input**: Graph G = (V,E)
- **Output**: Discovery time v.d, finish time v.f, predecessor v.π, edge classifications
- **Data structures**: Global time counter, color attributes

**Pseudocode** (recursive with timestamps):
```
DFS(G)
1  for each vertex u ∈ G.V
2     u.color = WHITE
3     u.π = NIL
4  time = 0
5  for each vertex u ∈ G.V
6     if u.color == WHITE
7        DFS-VISIT(G, u)

DFS-VISIT(G, u)
1  time = time + 1
2  u.d = time
3  u.color = GRAY
4  for each vertex v in G.Adj[u]
5     if v.color == WHITE
6        v.π = u
7        DFS-VISIT(G, v)
8  time = time + 1
9  u.f = time
10 u.color = BLACK
```

**Steps**:
1. Initialize all vertices white, π = NIL
2. For each white vertex, call DFS-VISIT (each call starts a new tree root)
3. DFS-VISIT: increment time, set discovery time, color gray
4. Recursively visit all white neighbors
5. After all edges explored, increment time, set finish time, color black

**Complexity**: Θ(V + E), same as BFS.

**Properties**:
- Vertex u is WHITE before u.d, GRAY between u.d and u.f, BLACK after u.f
- u.d < u.f for all u
- Discovery and finish timestamps: 1 to 2|V|
- **Parenthesis theorem** (Theorem 20.7): For any two vertices u,v, exactly one holds: (a) intervals disjoint, neither is descendant of other; (b) [u.d,u.f] ⊆ [v.d,v.f], u descendant of v; (c) [v.d,v.f] ⊆ [u.d,u.f], v descendant of u
- **Corollary 20.8**: v is proper descendant of u ⇔ u.d < v.d < v.f < u.f
- **White-path theorem** (Theorem 20.9): v is descendant of u in DFS forest ⇔ at time u.d, there exists a path from u to v consisting entirely of white vertices

**Edge classification** (by color when edge first explored):
| Color of v | Edge type |
|-----------|-----------|
| WHITE | Tree edge |
| GRAY | Back edge |
| BLACK | Forward or cross edge |

Forward: u.d < v.d. Cross: u.d > v.d. (Exercise 20.3-5)
- **Theorem 20.10**: In DFS of undirected graph, every edge is either tree or back edge (no forward/cross edges)

#### TOPOLOGICAL-SORT
- **Type**: DAG linear ordering algorithm
- **Goal**: Produce linear ordering of DAG vertices respecting edge direction
- **Input**: Directed acyclic graph G
- **Output**: Linked list of vertices in topologically sorted order
- **Complexity**: Θ(V + E)

**Pseudocode**:
```
TOPOLOGICAL-SORT(G)
1  call DFS(G) to compute finish times v.f for each vertex v
2  as each vertex is finished, insert it onto the front of a linked list
3  return the linked list of vertices
```

**Correctness** (Theorem 20.12): For any edge (u,v) in DAG, v.f < u.f. Thus vertices in decreasing finish time give topological order.

**Lemma 20.11**: DAG ⇔ DFS yields no back edges.

**Alternative method**: Repeatedly find vertex of in-degree 0, output it, remove it and outgoing edges. Runs in O(V+E).

#### STRONGLY-CONNECTED-COMPONENTS (Kosaraju's Algorithm)
- **Type**: SCC decomposition algorithm
- **Goal**: Find all SCCs of a directed graph
- **Input**: Directed graph G = (V,E)
- **Output**: Sets of vertices forming SCCs
- **Complexity**: Θ(V + E)

**Pseudocode**:
```
STRONGLY-CONNECTED-COMPONENTS(G)
1  call DFS(G) to compute finish times u.f for each vertex u
2  create Gᵀ
3  call DFS(Gᵀ), but in main loop, consider vertices in order of decreasing u.f
4  output the vertices of each tree in depth-first forest of Gᵀ as a separate SCC
```

**Steps**:
1. First DFS on G: compute finish times
2. Compute transpose Gᵀ
3. Second DFS on Gᵀ: process vertices in decreasing order of finish times from step 1
4. Each tree in DFS forest of Gᵀ = one SCC

**Key property** (Lemma 20.13): If C and C' are distinct SCCs and there's a path from C to C', there cannot be a path from C' to C. Thus component graph is a DAG.

**Lemma 20.14**: If edge (u,v) ∈ E with u ∈ C', v ∈ C, then f(C') > f(C).

**Corollary 20.15**: If f(C) > f(C'), then Eᵀ contains no edge from C to C'.

**Theorem 20.16**: Algorithm correctly computes SCCs (proof by induction on DFS trees of Gᵀ).

### Data Structures & Representations

| Representation | Memory | Edge lookup | Edge iteration | Best for |
|---------------|--------|-------------|----------------|----------|
| Adjacency list | Θ(V + E) | O(degree(u)) worst-case | Θ(V + E) | Sparse graphs |
| Adjacency matrix | Θ(V²) | O(1) | Θ(V²) | Dense graphs; quick edge existence check |

- Adjacency list: sum of lengths = \|E\| (directed), 2\|E\| (undirected)
- Adjacency matrix for undirected: A = Aᵀ (symmetric)
- Weighted graphs: store weight alongside vertex in adjacency list; store weight in matrix cell
- One-bit-per-entry possible for unweighted adjacency matrix
- Transpose of adjacency list: Θ(V + E) time; of adjacency matrix: Θ(V²) time

### Comparisons & Trade-offs

| Dimension | BFS | DFS |
|-----------|-----|-----|
| Strategy | Level by level (breadth) | Deep first (depth) |
| Data structure | Queue (FIFO) | Stack (implicit via recursion) |
| Single/multi source | Single source | Multiple sources |
| Shortest paths (unweighted) | Yes | No |
| Edge classification | 3 types (no forward) | 4 types |
| Applications | Shortest path, Prim, Dijkstra | Topological sort, SCC, articulation points |
| Complexity | O(V+E) | Θ(V+E) |

### Proof & Argument Patterns

- **BFS correctness**: Two lemmas (bound, queue property) + contradiction proof (Theorem 20.5)
- **Parenthesis theorem**: Case analysis based on u.d < v.d or v.d < u.d
- **White-path theorem**: Forward (descendant ⇒ white path) trivial by Corollary 20.8; backward uses proof by contradiction with closest violating vertex
- **Topological sort correctness**: Edge (u,v) explored → v cannot be gray (no back edges in DAG) → v is white or black → v.f < u.f
- **SCC correctness**: Induction on number of DFS trees of Gᵀ; uses Lemma 20.14, Corollary 20.15, white-path theorem

### Edge Cases & Pitfalls
- BFS tree can vary with adjacency list order, but distances d do not (Exercise 20.2-5)
- DFS results can vary with vertex and adjacency list order
- Self-loops are back edges in directed graphs
- DAG required for topological sort; cycles make it impossible
- Isolated vertices with incoming/outgoing edges can form single-vertex DFS tree (Exercise 20.3-10)
- Multiple-source BFS possible but not standard convention

### End-of-Chapter Material
- **Problems**: Edge classification by BFS (20-1), Articulation points/bridges/biconnected components (20-2), Euler tour (20-3), Reachability (20-4), Planar graph insertion (20-5)
- **Key exercises**: 20.2-3 (color bit sufficiency), 20.2-7 (wrestler bipartite testing = 2-coloring / bipartite graph test via BFS), 20.3-5 (edge classification by timestamps), 20.3-6 (iterative DFS with stack), 20.4-2 (count paths in DAG), 20.4-5 (Kahn's algorithm), 20.5-3 (Bacon's incorrect modification)

---

## Ch. 21 — Minimum Spanning Trees

### Named Entities (Terms & Definitions)

| Term | Definition |
|------|-----------|
| **Spanning tree** | Acyclic subset T ⊆ E connecting all vertices; has exactly \|V\|−1 edges |
| **Minimum spanning tree (MST)** | Spanning tree minimizing total weight w(T) = Σ_{(u,v)∈T} w(u,v) |
| **Cut** | Partition (S, V−S) of V |
| **Edge crosses cut** | One endpoint in S, other in V−S |
| **Cut respects A** | No edge of A crosses the cut |
| **Light edge** | Edge crossing a cut with minimum weight (ties possible) |
| **Safe edge** | An edge (u,v) such that A ∪ {(u,v)} is still subset of some MST |
| **Cut-and-paste technique** | MST proof method: swap edges to show optimality |
| **Greedy algorithm** | Makes locally optimal choice at each step; MST greedy works due to cut property |
| **Disjoint-set forest** | Data structure for union-by-rank + path compression; nearly O(1) per operation |
| **Weight function** | w: E → ℝ |
| **Bottleneck spanning tree** | Spanning tree minimizing maximum edge weight |
| **Second-best MST** | Spanning tree with second smallest total weight |
| **Borůvka's algorithm** | Earliest MST algorithm; O(lg V) phases of edge contraction |

### Processes / Algorithms

#### GENERIC-MST
- **Type**: Greedy MST framework
- **Goal**: Grow MST by repeatedly adding safe edges
- **Input**: Connected, undirected G = (V,E) with weight function w
- **Output**: Minimum spanning tree A

**Pseudocode**:
```
GENERIC-MST(G, w)
1  A = Ø
2  while A does not form a spanning tree
3     find an edge (u,v) that is safe for A
4     A = A ∪ {(u,v)}
5  return A
```

**Loop invariant**: Prior to each iteration, A is subset of some MST.
- Initialization: A=Ø trivially satisfies
- Maintenance: only safe edges added
- Termination: A must be MST (contains exactly \|V\|−1 edges)

#### Theorem 21.1 (Cut Property)
- **Statement**: Let A ⊆ some MST. Let (S, V−S) be any cut respecting A. Let (u,v) be a light edge crossing (S, V−S). Then (u,v) is safe for A.
- **Proof**: Cut-and-paste: Let T be MST containing A. If (u,v) ∈ T, done. Else, (u,v) forms cycle with path in T. Edge (x,y) on that path crosses cut. Remove (x,y), add (u,v) → T' = T − {(x,y)} ∪ {(u,v)}. Since w(u,v) ≤ w(x,y), w(T') ≤ w(T), so T' is MST. Since (x,y) ∉ A (cut respects A), A ⊆ T'.

#### Corollary 21.2
- **Statement**: Let C be a connected component in forest GA = (V, A). If (u,v) is a light edge connecting C to another component, then (u,v) is safe for A.
- **Proof**: Cut (V_C, V−V_C) respects A; (u,v) is light for this cut.

#### MST-KRUSKAL
- **Type**: Greedy MST algorithm (edge-based)
- **Goal**: Build MST by adding smallest-weight edges that don't create cycles
- **Input**: Connected, undirected G = (V,E), weight w
- **Output**: Minimum spanning tree A
- **Data structure**: Disjoint-set forest (MAKE-SET, FIND-SET, UNION)
- **Complexity**: O(E lg V)

**Pseudocode**:
```
MST-KRUSKAL(G, w)
1  A = Ø
2  for each vertex v ∈ G.V
3     MAKE-SET(v)
4  create a single list of the edges in G.E
5  sort the list of edges into monotonically increasing order by weight w
6  for each edge (u,v) taken from the sorted list in order
7     if FIND-SET(u) ≠ FIND-SET(v)
8        A = A ∪ {(u,v)}
9        UNION(u,v)
10 return A
```

**Steps**:
1. Create \|V\| singleton sets
2. Sort edges in nondecreasing order
3. For each edge (u,v) in sorted order:
   - If u and v in different sets: add to A, union their sets
4. Return A

**Complexity details**:
- Sorting: O(E lg E) = O(E lg V)
- Disjoint-set operations: O((V+E) α(V)) ≈ O(E α(V))
- Total: O(E lg V)

#### MST-PRIM
- **Type**: Greedy MST algorithm (vertex-based)
- **Goal**: Grow a single tree by adding minimum-weight edge connecting tree to isolated vertex
- **Input**: Connected, undirected G = (V,E), weight w, root r
- **Output**: Minimum spanning tree A = {(v, v.π) : v ∈ V − {r}}
- **Data structure**: Min-priority queue Q keyed by v.key

**Pseudocode**:
```
MST-PRIM(G, w, r)
1  for each vertex u ∈ G.V
2     u.key = ∞
3     u.π = NIL
4  r.key = 0
5  Q = Ø
6  for each vertex u ∈ G.V
7     INSERT(Q, u)
8  while Q ≠ Ø
9     u = EXTRACT-MIN(Q)
10    for each vertex v in G.Adj[u]
11       if v ∈ Q and w(u,v) < v.key
12          v.π = u
13          v.key = w(u,v)
14          DECREASE-KEY(Q, v, w(u,v))
```

**Loop invariant** (three-part):
1. A = {(v, v.π) : v ∈ V − {r} − Q}
2. Vertices in MST = V − Q
3. ∀ v ∈ Q: if v.π ≠ NIL, v.key < ∞ is weight of light edge connecting v to V−Q

**Complexity**:
| Priority Queue | EXTRACT-MIN | DECREASE-KEY | Total |
|----------------|-------------|--------------|-------|
| Binary heap | O(V lg V) | O(E lg V) | O(E lg V) |
| Fibonacci heap | O(lg V) amortized | O(1) amortized | O(E + V lg V) |
| Array (dense) | O(V) each | O(1) | O(V²) |

For dense graphs (|E| = Θ(V²)), array implementation yields O(V²).

### Comparisons & Trade-offs

| Dimension | Kruskal | Prim |
|-----------|---------|------|
| Strategy | Add globally minimum edge not creating cycle | Grow tree from root, add lightest connection |
| Data structure | Disjoint-set forest + Sorting | Min-priority queue |
| Builds | Forest (multiple trees merge) | Single tree |
| Complexity | O(E lg V) | O(E lg V) binary; O(E + V lg V) Fibonacci |
| Dense graph best | O(E lg V) | O(V²) array |
| Sparse graph best | O(E lg V) | O(E + V lg V) Fibonacci |
| Edge processing | Sorted once | Per-vertex adjacency scan |
| Origin | Kruskal (1956) | Jarník (1930) / Prim (1957) |

### Formulas & Equations
- Tree weight: w(T) = Σ_{(u,v)∈T} w(u,v)
- A spanning tree has exactly \|V\| − 1 edges (Theorem B.2)

### Rules, Laws & Theorems
- **Theorem 21.1 (Cut property)**: Light edge crossing any cut that respects A is safe for A
- **Corollary 21.2**: Light edge connecting a component of GA to another is safe
- **Theorem 21.3 (Cycle property)**: If (u,v) is the heaviest edge on a cycle, it cannot be in any MST (Problem 21.1-5)
- **Uniqueness**: If every cut has unique light edge, MST is unique (Exercise 21.1-6). Converse false
- **Sorted edge weights**: All MSTs of same graph have same sorted edge weight list (Exercise 21.1-8)

### Proof & Argument Patterns
- **Cut-and-paste**: Swap a non-light edge for a light edge on a cycle to get lighter (or equal) tree; standard for MST correctness
- **Cycle property**: Maximum-weight edge on any cycle is not in any MST
- **Corollary 21.2 proof**: Set S = V_C; cut respects A; light edge = safe
- **Loop invariant proof** for Prim: three-part invariant maintained

### Edge Cases & Pitfalls
- MST not unique when multiple edges have same weight
- Positive weights ensure minimum-weight connected subgraph is a tree (nonpositive weights allow cycles)
- Disconnected graph: MST-KRUSKAL produces minimum spanning forest
- Edge weights must be real numbers; comparisons-based operations
- Bottleneck spanning tree ≠ MST, but every MST is bottleneck spanning tree

### End-of-Chapter Material
- **Problems**: Second-best MST (21-1), MST in sparse graphs / MST-REDUCE (21-2), Alternative MST algorithms (21-3), Bottleneck spanning tree (21-4)
- **Key exercises**: 21.1-1 (minimum-weight edge belongs to some MST), 21.1-2 (converse of cut property false), 21.2-1 (tie-breaking produces any MST), 21.2-2 (O(V²) Prim with adjacency matrix), 21.2-4 (fast Kruskal with integer weights using counting sort)
- **Historical**: Borůvka (1926), Kruskal (1956), Prim/Jarník (1930/1957), Fredman-Tarjan (O(E lg* V)), Chazelle (O(E α(E,V)))

---

## Ch. 22 — Single-Source Shortest Paths

### Named Entities (Terms & Definitions)

| Term | Definition |
|------|-----------|
| **Shortest-path problem** | Find path minimizing sum of edge weights from source to destination |
| **Shortest-path weight** | δ(u,v) = min{w(p) : p is path u⇝v}, ∞ if no path, −∞ if negative-weight cycle reachable |
| **Shortest path** | Path p with w(p) = δ(u,v) |
| **Single-source shortest-paths** | Find shortest paths from s to all v ∈ V |
| **Single-destination shortest-paths** | Find shortest paths to t from all v ∈ V (reversible) |
| **Single-pair shortest-path** | Shortest path from u to v for given pair |
| **All-pairs shortest-paths** | Shortest paths between all pairs (Chapter 23) |
| **Negative-weight edge** | Edge with w(u,v) < 0 |
| **Negative-weight cycle** | Cycle with total weight < 0; makes shortest paths undefined (δ = −∞) |
| **Zero-weight cycle** | Cycle with total weight 0; can be removed without changing path weight |
| **Relaxation** | Operation testing if u improves path to v: if v.d > u.d + w(u,v), update |
| **Shortest-path estimate** | v.d: current upper bound on δ(s,v) |
| **Predecessor subgraph** | Gπ = (Vπ, Eπ); at termination, shortest-paths tree rooted at s |
| **Shortest-paths tree** | Rooted tree s.t. unique path from s to v is shortest path in G |
| **Triangle inequality** | δ(s,v) ≤ δ(s,u) + w(u,v) for all edges (u,v) |
| **Difference constraint** | Inequality of form xⱼ − xᵢ ≤ bₖ |
| **Constraint graph** | Weighted directed graph encoding difference constraints |
| **Feasible solution** | Vector x satisfying Ax ≤ b |
| **Linear programming** | Maximize cᵀx subject to Ax ≤ b |
| **Critical path** | Longest path in a DAG (PERT chart analysis) |
| **Scaling algorithm** | Algorithm working on progressively more significant bits of edge weights |
| **Arbitrage** | Currency conversion cycle yielding profit (>1 product of exchange rates) |
| **Mean weight of cycle** | μ(c) = (1/k) Σ w(eᵢ) |

### Processes / Algorithms

#### INITIALIZE-SINGLE-SOURCE
```
INITIALIZE-SINGLE-SOURCE(G, s)
1  for each vertex v ∈ G.V
2     v.d = ∞
3     v.π = NIL
4  s.d = 0
```
- **Complexity**: Θ(V)

#### RELAX
```
RELAX(u, v, w)
1  if v.d > u.d + w(u,v)
2     v.d = u.d + w(u,v)
3     v.π = u
```
- **Complexity**: O(1)
- **Effect**: Decreases v.d to u.d + w(u,v) if improvement possible

#### BELLMAN-FORD
- **Type**: Dynamic programming / relaxation-based shortest paths
- **Goal**: Find shortest paths from s, handle negative edges, detect negative cycles
- **Input**: Weighted directed graph G = (V,E), source s, weight w
- **Output**: TRUE if no negative-weight cycle reachable from s, FALSE otherwise; v.d = δ(s,v) if TRUE
- **Complexity**: O(VE)

**Pseudocode**:
```
BELLMAN-FORD(G, w, s)
1  INITIALIZE-SINGLE-SOURCE(G, s)
2  for i = 1 to |G.V| − 1
3     for each edge (u,v) ∈ G.E
4        RELAX(u, v, w)
5  for each edge (u,v) ∈ G.E
6     if v.d > u.d + w(u,v)
7        return FALSE
8  return TRUE
```

**Correctness** (Theorem 22.4):
- After \|V\|−1 passes, v.d = δ(s,v) for all reachable vertices (path relaxation property on any shortest path with ≤ \|V\|−1 edges)
- If no negative-weight cycle reachable: check passes (triangle inequality implies v.d ≤ u.d + w(u,v) for all edges) → returns TRUE
- If negative-weight cycle reachable: summing inequalities around cycle gives 0 ≤ w(c) < 0 contradiction → returns FALSE

**Lemma 22.2**: After \|V\|−1 iterations, v.d = δ(s,v) for all reachable v (if no negative cycles).

**Corollary 22.3**: v.d < ∞ at termination ⇔ there exists a path from s to v.

**Variation** (Yen's improvement, Problem 22-1): Partition edges into forward (i<j) and backward (i>j); alternate passes; only ⌈\|V\|/2⌉ passes needed.

#### DAG-SHORTEST-PATHS
- **Type**: Shortest paths in DAGs
- **Goal**: Compute shortest paths from s in a DAG (handles negative edges, no cycles)
- **Input**: Weighted DAG G, source s
- **Output**: Shortest-path weights and tree
- **Complexity**: Θ(V + E)

**Pseudocode**:
```
DAG-SHORTEST-PATHS(G, w, s)
1  topologically sort the vertices of G
2  INITIALIZE-SINGLE-SOURCE(G, s)
3  for each vertex u ∈ G.V, taken in topologically sorted order
4     for each vertex v in G.Adj[u]
5        RELAX(u, v, w)
```

**Correctness** (Theorem 22.5): Topological order ensures edges of any shortest path are relaxed in order → path-relaxation property applies.

**Application**: Critical path in PERT charts (longest path = negate weights or replace ∞ with −∞ and > with <).

#### DIJKSTRA
- **Type**: Greedy shortest-paths algorithm
- **Goal**: Find shortest paths from s (nonnegative weights only)
- **Input**: Weighted directed graph G = (V,E), source s, w(u,v) ≥ 0 for all edges
- **Output**: Shortest-path weights and tree
- **Data structure**: Min-priority queue Q, keyed by v.d
- **Complexity**: O(V²) array, O(E lg V) binary heap, O(V lg V + E) Fibonacci heap

**Pseudocode**:
```
DIJKSTRA(G, w, s)
1  INITIALIZE-SINGLE-SOURCE(G, s)
2  S = Ø
3  Q = Ø
4  for each vertex u ∈ G.V
5     INSERT(Q, u)
6  while Q ≠ Ø
7     u = EXTRACT-MIN(Q)
8     S = S ∪ {u}
9     for each vertex v in G.Adj[u]
10       RELAX(u, v, w)
11       if the call of RELAX decreased v.d
12          DECREASE-KEY(Q, v, v.d)
```

**Invariant**: Q = V − S at start of each iteration. Vertices in S have final shortest-path weights.

**Correctness** (Theorem 22.6): Induction on |S|. Show u.d = δ(s,u) when u extracted. Uses convergence property: first vertex y on shortest path not in S must have y.d = δ(s,y). Since u has minimum d in V−S, u.d ≤ y.d, and δ(s,y) ≤ δ(s,u) ≤ u.d, forcing equality.

**Corollary 22.7**: Gπ is shortest-paths tree rooted at s.

### Properties of Shortest Paths and Relaxation (Section 22.5)

| # | Property | Lemma | Statement |
|---|----------|-------|-----------|
| 1 | **Triangle inequality** | 22.10 | δ(s,v) ≤ δ(s,u) + w(u,v) for all (u,v) ∈ E |
| 2 | **Upper-bound property** | 22.11 | v.d ≥ δ(s,v) always; once v.d = δ(s,v), it never changes |
| 3 | **No-path property** | 22.12 | No path s⇝v ⇒ v.d = δ(s,v) = ∞ always |
| 4 | **Convergence property** | 22.14 | If s⇝u→v is shortest path and u.d = δ(s,u) before relaxing (u,v), then v.d = δ(s,v) after |
| 5 | **Path-relaxation property** | 22.15 | If edges of shortest path p = 〈v₀,v₁,…,vₖ〉 relaxed in order, then vₖ.d = δ(s,vₖ) |
| 6 | **Predecessor-subgraph property** | 22.17 | Once v.d = δ(s,v) for all v, Gπ is shortest-paths tree |

**Lemma 22.13**: After relaxing (u,v), v.d ≤ u.d + w(u,v).

**Lemma 22.16**: Gπ always forms a rooted tree with root s (no cycles).

### Comparisons & Trade-offs

| Algorithm | Negative edges | Cycles | Time | Strategy |
|-----------|---------------|--------|------|----------|
| BFS | No (unweighted) | No cycles in paths | O(V+E) | Queue-based |
| Bellman-Ford | Yes | Detects neg cycles | O(VE) | Relax all edges \|V\|−1 times |
| DAG-SP | Yes | No cycles possible | Θ(V+E) | Topological order + relax |
| Dijkstra | No | Not allowed | O(V²) or O(E lg V) | Greedy + min-priority queue |

### Formulas & Equations
- Path weight: w(p) = Σ_{i=1}^{k} w(v_{i−1}, v_i)
- Shortest-path weight: δ(u,v) = min{w(p) : p is path u⇝v}
- Relaxation: if v.d > u.d + w(u,v) then v.d = u.d + w(u,v)
- Triangle inequality: δ(s,v) ≤ δ(s,u) + w(u,v)
- Reweighting (Ch 23): ŵ(u,v) = w(u,v) + h(u) − h(v) preserves shortest paths
- Difference constraint: xⱼ − xᵢ ≤ bₖ
- Constraint graph: w(vᵢ, vⱼ) = bₖ for constraint xⱼ − xᵢ ≤ bₖ

### Edge Cases & Pitfalls
- **Negative-weight cycles**: δ(s,v) = −∞ for vertices reachable from such cycles
- **Disconnected**: δ(s,v) = ∞; no-path property maintains v.d = ∞
- **Dijkstra on negative edges**: fails because extracted vertex may later be reachable via shorter path
- **Zero-weight cycles**: can be removed; shortest paths assumed simple (≤ |V|−1 edges)
- **Infinite arithmetic**: a + ∞ = ∞; a + (−∞) = −∞; these conventions needed for correctness proofs

### Proof & Argument Patterns
- **Path-relaxation proof**: Induction on edge position in shortest path; convergence property at each step
- **Upper-bound proof**: Induction on number of relaxations; triangle inequality at each step
- **Bellman-Ford negative cycle detection**: Sum inequalities around cycle → 0 ≤ w(c) < 0 contradiction
- **Dijkstra correctness**: Induction on |S|; uses convergence property + nonnegative weights
- **Triangle inequality**: Shortest path to v cannot be longer than shortest path to u plus edge (u,v)

### End-of-Chapter Material
- **Problems**: Yen's improvement (22-1), Nesting boxes / longest chain in partial order (22-2), Arbitrage detection (22-3), Gabow's scaling (22-4), Karp's minimum mean-weight cycle (22-5), Bitonic shortest paths (22-6)
- **Key exercises**: 22.1-3 (m+1 pass termination), 22.1-4 (set v.d = −∞ for negative-cycle reachable vertices), 22.2-4 (count all paths in DAG), 22.3-2 (Dijkstra fails with negative edges), 22.3-11 (Dijkstra OK if only source-outgoing edges negative), 22.4-5 (O(nm) Bellman-Ford for difference constraints)

---

## Ch. 23 — All-Pairs Shortest Paths

### Named Entities (Terms & Definitions)

| Term | Definition |
|------|-----------|
| **All-pairs shortest paths** | Find δ(i,j) for all vertex pairs i,j |
| **Predecessor matrix** | Π = (πᵢⱼ): πᵢⱼ = predecessor of j on shortest path from i |
| **Matrix multiplication view** | Shortest-path extension analogous to (min,+) matrix multiplication |
| **Repeated squaring** | Compute L^(n−1) = W^(n−1) by squaring powers: Θ(n³ lg n) |
| **Floyd-Warshall algorithm** | Dynamic programming on intermediate vertices; Θ(V³) |
| **Intermediate vertex** | Any vertex on path other than endpoints |
| **Transitive closure** | G* = (V, E*): edge (i,j) in E* iff path exists from i to j in G |
| **Johnson's algorithm** | Reweighting + Dijkstra from each vertex; O(V² lg V + VE) |
| **Reweighting** | ŵ(u,v) = w(u,v) + h(u) − h(v) makes all edges nonnegative |
| **Closed semiring** | Algebraic structure for path problems (tropical semiring: min, +, ∞, 0) |
| **ϵ-dense graph** | \|E\| = Θ(V^{1+ϵ}) |

### Processes / Algorithms

#### EXTEND-SHORTEST-PATHS
- **Type**: Matrix multiplication (min,+) variant
- **Goal**: Extend path lengths by one edge
- **Input**: L^(r−1) (path weights with ≤ r−1 edges), W (edge weight matrix)
- **Output**: L^(r) (path weights with ≤ r edges)
- **Complexity**: Θ(n³)

**Pseudocode**:
```
EXTEND-SHORTEST-PATHS(L^(r−1), W, L^(r), n)
1  // Assume L^(r) initialized to ∞
2  for i = 1 to n
3     for j = 1 to n
4        for k = 1 to n
5           l^(r)ᵢⱼ = min(l^(r)ᵢⱼ, l^(r−1)ᵢₖ + wₖⱼ)
```

**Analogous to matrix multiplication**: Replace + with min, × with +.

#### SLOW-APSP
- **Type**: Dynamic programming with matrix multiplication
- **Goal**: Compute L^(n−1) = shortest-path weights
- **Complexity**: Θ(n⁴)

```
SLOW-APSP(W, L^(0), n)
1  let L = (lᵢⱼ) and M = (mᵢⱼ) be new n×n matrices
2  L = L^(0)
3  for r = 1 to n−1
4     M = ∞
5     EXTEND-SHORTEST-PATHS(L, W, M, n)
6     L = M
7  return L
```

#### FASTER-APSP (Repeated Squaring)
- **Type**: Improved DP using exponentiation by squaring
- **Goal**: Compute L^(n−1) in O(n³ lg n)
- **Complexity**: Θ(n³ lg n)

```
FASTER-APSP(W, n)
1  let L and M be new n×n matrices
2  L = W
3  r = 1
4  while r < n−1
5     M = ∞
6     EXTEND-SHORTEST-PATHS(L, L, M, n)  // compute M = L²
7     r = 2r
8     L = M
9  return L
```

**Key**: L^(n−1) = W^(n−1); compute by squaring: L^(2r) = (L^(r))². Only ⌈lg(n−1)⌉ matrix multiplications needed.

#### FLOYD-WARSHALL
- **Type**: Dynamic programming on intermediate vertices
- **Goal**: Compute all-pairs shortest-path weights
- **Input**: n×n matrix W (edge weights)
- **Output**: D^(n) = (δ(i,j))
- **Complexity**: Θ(n³)

**Recurrence**:
- d^(k)ᵢⱼ = weight of shortest path from i to j with intermediate vertices in {1,2,…,k}
- d^(0)ᵢⱼ = wᵢⱼ (0 if i=j, ∞ if no edge)
- d^(k)ᵢⱼ = min(d^(k−1)ᵢⱼ, d^(k−1)ᵢₖ + d^(k−1)ₖⱼ)

**Pseudocode**:
```
FLOYD-WARSHALL(W, n)
1  D^(0) = W
2  for k = 1 to n
3     let D^(k) be a new n×n matrix
4     for i = 1 to n
5        for j = 1 to n
6           d^(k)ᵢⱼ = min(d^(k−1)ᵢⱼ, d^(k−1)ᵢₖ + d^(k−1)ₖⱼ)
7  return D^(n)
```

**Space optimization** (Floyd-Warshall′): Can compute in-place; only Θ(n²) space needed.

**Predecessor matrix Π**: 
- π⁽⁰⁾ᵢⱼ = i if i≠j and wᵢⱼ < ∞, NIL otherwise
- π⁽ᵏ⁾ᵢⱼ = π⁽ᵏ⁻¹⁾ₖⱼ if d^(k−1)ᵢₖ + d^(k−1)ₖⱼ < d^(k−1)ᵢⱼ, else π⁽ᵏ⁻¹⁾ᵢⱼ

#### TRANSITIVE-CLOSURE
- **Type**: Boolean variant of Floyd-Warshall
- **Goal**: Compute G* = (V, E*) where (i,j) ∈ E* iff path i⇝j exists
- **Complexity**: Θ(n³)
- **Recurrence**: t^(k)ᵢⱼ = t^(k−1)ᵢⱼ ∨ (t^(k−1)ᵢₖ ∧ t^(k−1)ₖⱼ)
- Replace (min,+) with (∨, ∧)

#### JOHNSON
- **Type**: Reweighting + Dijkstra
- **Goal**: All-pairs shortest paths, efficient for sparse graphs
- **Input**: Weighted directed graph G = (V,E)
- **Output**: D = (dᵢⱼ) = δ(i,j) or report negative-weight cycle
- **Complexity**: O(V² lg V + VE)

**Pseudocode**:
```
JOHNSON(G, w)
1  compute G′ where G′.V = G.V ∪ {s}, G′.E = G.E ∪ {(s,v) : v ∈ G.V}, w(s,v) = 0
2  if BELLMAN-FORD(G′, w, s) == FALSE
3     print "negative-weight cycle"
4  else
5     for each vertex v ∈ G′.V
6        h(v) = δ(s,v)  (from Bellman-Ford)
7     for each edge (u,v) ∈ G′.E
8        ŵ(u,v) = w(u,v) + h(u) − h(v)
9     let D = (dᵤᵥ) be new n×n matrix
10    for each vertex u ∈ G.V
11       run DIJKSTRA(G, ŵ, u) to compute δ̂(u,v) for all v
12       for each vertex v ∈ G.V
13          dᵤᵥ = δ̂(u,v) + h(v) − h(u)
14    return D
```

**Steps**:
1. Add super-source s with 0-weight edges to all vertices
2. Run Bellman-Ford to compute h(v) = δ(s,v)
3. Reweight: ŵ(u,v) = w(u,v) + h(u) − h(v) (all nonnegative)
4. Run Dijkstra from each vertex u with ŵ
5. Convert back: δ(u,v) = δ̂(u,v) + h(v) − h(u)

**Lemma 23.1 (Reweighting)**: ŵ(p) = w(p) + h(v₀) − h(vₖ). Reweighting preserves shortest paths and does not change which cycles are negative.

### Formulas & Equations
- **Recurrence for matrix multiplication approach**: l^(r)ᵢⱼ = min_{1≤k≤n} (l^(r−1)ᵢₖ + wₖⱼ)
- **Floyd-Warshall recurrence**: d^(k)ᵢⱼ = min(d^(k−1)ᵢⱼ, d^(k−1)ᵢₖ + d^(k−1)ₖⱼ)
- **Reweighting**: ŵ(u,v) = w(u,v) + h(u) − h(v)
- **Reweighted path**: ŵ(p) = w(p) + h(v₀) − h(vₖ)
- **Conversion back**: δ(u,v) = δ̂(u,v) + h(v) − h(u)
- **Transitive closure**: t^(k)ᵢⱼ = t^(k−1)ᵢⱼ ∨ (t^(k−1)ᵢₖ ∧ t^(k−1)ₖⱼ)

### Comparisons & Trade-offs

| Algorithm | Complexity | Best for | Technique |
|-----------|-----------|----------|-----------|
| Run Dijkstra \|V\| times (binary heap) | O(VE lg V) | Sparse, nonnegative | Greedy |
| Run Dijkstra \|V\| times (Fibonacci) | O(V² lg V + VE) | Sparse, nonnegative | Greedy + Fibonacci |
| Run Bellman-Ford \|V\| times | O(V²E) = O(V⁴ dense) | Dense, negative edges | Relaxation |
| SLOW-APSP | Θ(V⁴) | — | DP (matrix multiply) |
| FASTER-APSP | Θ(V³ lg V) | Dense | Repeated squaring |
| Floyd-Warshall | Θ(V³) | Dense | DP (intermediate vertices) |
| Johnson | O(V² lg V + VE) | Sparse, negative edges OK | Reweighting + Dijkstra |

### Edge Cases & Pitfalls
- **Negative-weight cycles**: Floyd-Warshall detects them (d^(n)ᵢᵢ < 0); Johnson detects via Bellman-Ford
- **Dense vs sparse**: Floyd-Warshall better for dense (V³ constant small); Johnson better for sparse
- **Space**: Floyd-Warshall Θ(V³) naive, Θ(V²) with in-place optimization
- **Zero-weight cycles**: handled correctly (no effect on shortest paths)
- **Disconnected**: δ(i,j) = ∞ for unreachable pairs
- **Reweighting requires h from Bellman-Ford**: without super-source, may get h(v) = ∞ for unreachable vertices
- **Integer weights**: matrix multiplication approach can exploit faster matrix multiplication (Zwick, Williams)

### Proof & Argument Patterns
- **Optimal substructure**: Subpaths of shortest paths are shortest paths (Lemma 22.1)
- **Floyd-Warshall recurrence**: Case analysis on whether k is intermediate vertex
- **Reweighting preservation**: ŵ(p) = w(p) + h(v₀) − h(vₖ); path weights shift by constant independent of path → order preserved
- **Nonnegativity of ŵ**: h(v) ≤ h(u) + w(u,v) by triangle inequality → ŵ(u,v) = w(u,v) + h(u) − h(v) ≥ 0

### End-of-Chapter Material
- **Problems**: Transitive closure dynamic maintenance (23-1), Shortest paths in ϵ-dense graphs (23-2)
- **Key exercises**: 23.1-4 (associativity of min,+ multiplication), 23.1-9 (detect negative cycles in FASTER-APSP), 23.2-4 (Floyd-Warshall in-place Θ(n²) space), 23.2-6 (negative cycle detection via dᵢᵢ < 0), 23.2-8 (O(VE) transitive closure using BFS from each vertex), 23.3-4 (simple subtraction fails for reweighting)

---

## Ch. 24 — Maximum Flow

### Named Entities (Terms & Definitions)

| Term | Definition |
|------|-----------|
| **Flow network** | Directed graph G = (V,E) with source s, sink t, capacity c(u,v) ≥ 0 for each edge |
| **Capacity** | c(u,v): maximum flow that can pass through edge (u,v) |
| **Flow** | Function f: V×V → ℝ satisfying capacity constraint and flow conservation |
| **Capacity constraint** | 0 ≤ f(u,v) ≤ c(u,v) for all u,v |
| **Flow conservation** | Σ_v f(u,v) = Σ_v f(v,u) for all u ∈ V − {s,t} |
| **Flow value** | \|f\| = Σ_v f(s,v) − Σ_v f(v,s) (total flow out of source) |
| **Maximum-flow problem** | Find flow of maximum value from s to t |
| **Residual network** | G_f = (V, E_f): edges with capacity c_f(u,v) = c(u,v) − f(u,v) (forward) or f(v,u) (backward) |
| **Residual capacity** | c_f(u,v) = c(u,v) − f(u,v) if (u,v) ∈ E; = f(v,u) if (v,u) ∈ E; = 0 otherwise |
| **Augmenting path** | Simple path from s to t in residual network |
| **Augmentation** | f ↑ f′: adding flow from residual network to original flow |
| **Cancellation** | Sending flow on reverse edge in residual network (decreases flow on original edge) |
| **Cut (of flow network)** | Partition (S,T) with s ∈ S, t ∈ T |
| **Net flow across cut** | f(S,T) = Σ_{u∈S} Σ_{v∈T} f(u,v) − Σ_{u∈S} Σ_{v∈T} f(v,u) |
| **Capacity of cut** | c(S,T) = Σ_{u∈S} Σ_{v∈T} c(u,v) |
| **Minimum cut** | Cut with minimum capacity |
| **Max-flow min-cut theorem** | Maximum flow value = minimum cut capacity |
| **Antiparallel edges** |Both (u,v) and (v,u) exist (not allowed in flow network definition) |
| **Supersource / Supersink** | Artificial source/sink for multiple-source/sink problems (∞ capacity edges) |
| **Integer-valued flow** | f(u,v) integer for all (u,v) |
| **Integrality theorem** | Ford-Fulkerson with integer capacities produces integer flow |
| **Edmonds-Karp algorithm** | Ford-Fulkerson using BFS to find augmenting paths; O(VE²) |
| **Critical edge** | Edge on augmenting path with minimum residual capacity |
| **Push-relabel algorithm** | Alternative max-flow approach using preflows and heights |
| **Preflow** | Flow that may violate conservation (excess at some vertices) |
| **Edge connectivity** | Min edges to remove to disconnect graph |
| **Maximum bipartite matching** | Max cardinality matching in bipartite graph (via flow) |
| **Corresponding flow network** | Directed G′ with unit capacities for bipartite matching |

### Processes / Algorithms

#### FORD-FULKERSON-METHOD
- **Type**: Iterative augmenting-path framework
- **Goal**: Find maximum flow
- **Complexity**: O(E |f*|) worst-case (integer capacities)

```
FORD-FULKERSON-METHOD(G, s, t)
1  initialize flow f to 0
2  while there exists an augmenting path p in residual network G_f
3     augment flow f along p
4  return f
```

#### FORD-FULKERSON (concrete implementation)
```
FORD-FULKERSON(G, s, t)
1  for each edge (u,v) ∈ G.E
2     (u,v).f = 0
3  while there exists a path p from s to t in the residual network G_f
4     c_f(p) = min { c_f(u,v) : (u,v) is in p }
5     for each edge (u,v) in p
6        if (u,v) ∈ G.E
7           (u,v).f = (u,v).f + c_f(p)
8        else  (v,u).f = (v,u).f − c_f(p)
9  return f
```

#### EDMONDS-KARP
- **Type**: BFS-based augmenting path selection (shortest path in residual network)
- **Goal**: Polynomial-time max flow
- **Complexity**: O(V E²)

**Key lemmas**:
- **Lemma 24.7**: δ_f(s,v) increases monotonically with each augmentation
- **Theorem 24.8**: Each edge becomes critical at most \|V\|/2 times; O(VE) augmentations

**Proof of O(VE) augmentations**:
1. Edge (u,v) critical on augmenting path ⇒ δ_f(s,v) = δ_f(s,u) + 1
2. After augmentation, (u,v) disappears from residual network
3. To reappear, (v,u) must be on some later augmenting path ⇒ δ_f'(s,u) = δ_f'(s,v) + 1
4. By monotonicity: δ_f'(s,u) ≥ δ_f(s,u) + 2
5. Each time edge becomes critical, u's distance increases by ≥2; max distance ≤ \|V\|−2
6. Each edge critical ≤ \|V\|/2 times; total O(VE) critical edges → O(VE) augmentations

### Formulas & Equations
- **Flow conservation**: Σ_v f(u,v) = Σ_v f(v,u) for all u ∈ V − {s,t}
- **Flow value**: \|f\| = Σ_v f(s,v) − Σ_v f(v,s)
- **Residual capacity**: c_f(u,v) = c(u,v) − f(u,v) if (u,v) ∈ E; = f(v,u) if (v,u) ∈ E; = 0 otherwise
- **Net flow across cut**: f(S,T) = Σ_{u∈S} Σ_{v∈T} f(u,v) − Σ_{u∈S} Σ_{v∈T} f(v,u)
- **Cut capacity**: c(S,T) = Σ_{u∈S} Σ_{v∈T} c(u,v)
- **Augmentation**: (f ↑ f′)(u,v) = f(u,v) + f′(u,v) − f′(v,u)
- **Residual capacity of path**: c_f(p) = min {c_f(u,v) : (u,v) ∈ p}
- **Lemma 24.1**: |f ↑ f′| = |f| + |f′|

### Rules, Laws & Theorems

#### Lemma 24.1 and 24.2
- **Lemma 24.1**: Augmenting flow f in G by flow f′ in G_f yields flow in G with value |f| + |f′|
- **Lemma 24.2**: The function f_p (sending c_f(p) along each edge of augmenting path p) is flow in G_f with value c_f(p) > 0
- **Corollary 24.3**: f ↑ f_p is flow in G with value |f| + c_f(p) > |f|

#### Lemma 24.4 (Net flow across any cut equals flow value)
- **Statement**: For any cut (S,T), f(S,T) = |f|
- **Proof**: Sum flow conservation equations for vertices in S−{s}

#### Corollary 24.5
- **Statement**: |f| ≤ c(S,T) for any cut (S,T)
- **Implication**: Maximum flow value ≤ minimum cut capacity

#### Theorem 24.6 (Max-Flow Min-Cut Theorem)
- **Statement**: For any flow f, TFAE: (1) f is maximum flow; (2) G_f has no augmenting paths; (3) |f| = c(S,T) for some cut (S,T)
- **Proof**: (1)⇒(2): augmenting path would increase flow. (2)⇒(3): S = {v reachable from s in G_f}, T = V−S; edges from S to T saturated, edges from T to S have zero flow → |f| = c(S,T). (3)⇒(1): by Corollary 24.5

#### Theorem 24.10 (Integrality Theorem)
- **Statement**: If all capacities are integers, Ford-Fulkerson produces integer-valued maximum flow
- **Proof**: Induction on iterations; each augmentation increases flow by integer amount

#### Corollary 24.11
- **Statement**: Cardinality of maximum matching in bipartite G = value of maximum flow in corresponding flow network G′
- **Proof**: Using Lemma 24.9 and integrality theorem

### Residual Networks — Detailed Example
Given f on edge (u,v) = 11 with c(u,v) = 16:
- c_f(u,v) = 5 (can send 5 more forward)
- c_f(v,u) = 11 (can cancel up to 11 flow by sending back)

### Data Structures & Representations
- **BFS** for Edmonds-Karp (shortest augmenting path)
- **DFS** for basic Ford-Fulkerson (any augmenting path)
- **Vertex splitting** for vertex capacities (Problem 24-1)
- **Unit-capacity edges** for bipartite matching

### Comparisons & Trade-offs

| Algorithm | Method | Complexity | Notes |
|-----------|--------|-----------|-------|
| Ford-Fulkerson (arbitrary path) | DFS for any augmenting path | O(E |f*|) | Depends on max flow value; can be exponential |
| Edmonds-Karp (BFS) | Shortest augmenting path | O(V E²) | Polynomial, independent of flow value |
| Capacity scaling | Find augmenting paths with capacity ≥ K | O(E² lg C) | Reduces iterations |
| Push-relabel | Preflow + heights | O(V³) or O(V E lg(V²/E+2)) | Practical; dominates in benchmarks |
| Dinic (blocking flow) | Layered network + blocking flow | O(V²E) | First polynomial improvement |

### Edge Cases & Pitfalls
- **Antiparallel edges**: Must eliminate by splitting one edge with intermediate vertex
- **Multiple sources/sinks**: Add supersource + supersink with ∞ capacity edges
- **Vertex capacities**: Split each vertex v into v_in → v_out with capacity l(v)
- **Irrational capacities**: Ford-Fulkerson may never terminate (pathological case)
- **Integer capacities**: Ford-Fulkerson terminates in at most |f*| iterations
- **Worst-case example** (Fig 24.7): Alternating paths s→u→v→t and s→v→u→t cause 2,000,000 iterations if capacities are 1,000,000
- **Edges entering source**: can exist; flow value formula accounts for this

### Proof & Argument Patterns
- **Augmentation**: Show f↑f′ satisfies capacity constraint and flow conservation via careful algebra
- **Net flow = cut flow**: Summation of conservation equations over S
- **Max-flow min-cut**: Construct S as reachable vertices in G_f; edges from S to T must be saturated
- **Monotonicity of distances** (Edmonds-Karp): Contradiction proof assuming distance decreases
- **Critical edge bound**: Each edge becomes critical at most |V|/2 times; distance increases by ≥2 between occurrences

### End-of-Chapter Material
- **Problems**: Escape problem (24-1), Minimum path cover (24-2), Hiring experts (24-3), Updating max flow (24-4), Max flow by scaling (24-5), Widest augmenting path (24-6), Global minimum cut (24-7)
- **Key exercises**: 24.1-7 (vertex capacity reduction), 24.2-3 (Edmonds-Karp execution), 24.2-7 (prove Lemma 24.2), 24.2-11 (edge connectivity via max flow), 24.3-1 (Ford-Fulkerson on bipartite matching), 24.3-2 (prove integrality theorem)

---

## Ch. 25 — Matchings in Bipartite Graphs

### Named Entities (Terms & Definitions)

| Term | Definition |
|------|-----------|
| **Matching** | Subset M ⊆ E such that each vertex incident on at most one edge in M |
| **Maximum matching** | Matching of maximum cardinality |
| **Perfect matching** | Matching matching every vertex (requires |L| = |R| for bipartite) |
| **Maximal matching** | Matching to which no edge can be added (always smaller or equal to maximum) |
| **Matched vertex** | Vertex incident on an edge in M |
| **Unmatched vertex** | Vertex with no incident edge in M |
| **M-alternating path** | Simple path whose edges alternate between M and E−M |
| **M-augmenting path** | M-alternating path starting and ending with edges in E−M (odd length, endpoints unmatched) |
| **Symmetric difference** | X ⊕ Y = (X−Y) ∪ (Y−X); commutative, associative, X⊕X = Ø |
| **Vertex-disjoint paths** | Paths sharing no vertices |
| **Maximal set of vertex-disjoint shortest M-augmenting paths** | Set used by Hopcroft-Karp to maximize matching growth per iteration |
| **Stable matching** | Matching with no blocking pair |
| **Blocking pair** | Unmatched pair (w,m) where w prefers m to her partner and m prefers w to his partner |
| **Stable-marriage problem** | Find stable matching given preference lists of n women and n men |
| **Gale-Shapley algorithm** | Propose-and-reject algorithm finding stable matching; O(n²) |
| **Woman-oriented / Man-oriented** | Variants of Gale-Shapley depending on who proposes |
| **Weak Pareto optimality** | No matching (stable or unstable) gives every woman a better partner than Gale-Shapley result |
| **Stable-roommates problem** | Stable matching on complete non-bipartite graph; may have no solution |
| **Assignment problem** | Find perfect matching maximizing total weight in complete bipartite graph |
| **Feasible vertex labeling** | Function h: V → ℝ s.t. l.h + r.h ≥ w(l,r) for all l∈L, r∈R |
| **Equality subgraph** | G_h = (V, E_h) where E_h = {(l,r) : l.h + r.h = w(l,r)} |
| **Hungarian algorithm** | Algorithm for assignment problem using equality subgraphs and augmenting paths |
| **δ (Hungarian)** | Minimum slack: min{l.h + r.h − w(l,r) : l∈F_L, r∈R−F_R} |
| **Hall's theorem** | Perfect matching in bipartite G exists iff |A| ≤ |N(A)| for all A ⊆ L |
| **d-regular graph** | Every vertex has degree d |
| **Fractional matching** | Function x: E → [0,1] s.t. Σ_{(u,v)∈E} x(u,v) ≤ 1 per vertex |

### Processes / Algorithms

#### Augmenting Path Theorem
**Corollary 25.4** (Berge's Theorem): M is maximum matching ⇔ no M-augmenting path exists.

**Lemma 25.1**: If P is M-augmenting path, then M′ = M ⊕ P is matching with |M′| = |M| + 1.

**Corollary 25.2**: If P₁,…,Pₖ are vertex-disjoint M-augmenting paths, then M′ = M ⊕ (P₁∪…∪Pₖ) has |M′| = |M| + k.

**Lemma 25.3**: M⊕M* consists of disjoint paths/cycles alternating between M and M*. If |M*| > |M|, contains ≥ |M*|−|M| vertex-disjoint M-augmenting paths.

#### HOPCROFT-KARP
- **Type**: Maximum cardinality bipartite matching via augmenting paths
- **Goal**: Maximum matching in bipartite graph
- **Input**: Undirected bipartite graph G = (V,E)
- **Output**: Maximum matching M
- **Complexity**: O(√V · E) = O(V^{1/2} E)

```
HOPCROFT-KARP(G)
1  M = Ø
2  repeat
3     let P = {P₁, P₂, …, Pₖ} be a maximal set of vertex-disjoint shortest M-augmenting paths
4     M = M ⊕ (P₁ ∪ P₂ ∪ … ∪ Pₖ)
5  until P == Ø
6  return M
```

**Three phases to find maximal set of shortest M-augmenting paths**:

**Phase 1**: Create directed graph G_M from undirected G:
- Edges L→R for edges in E−M
- Edges R→L for edges in M

**Phase 2**: BFS from all unmatched vertices in L to create DAG H:
- Each layer alternates L/R
- q = shortest distance to unmatched vertex in R
- Include only vertices with distance ≤ q
- Only edges between consecutive layers

**Phase 3**: DFS on transpose Hᵀ from unmatched vertices in R:
- Start from each unmatched vertex in layer q
- Search backward to layer 0
- Once vertex discovered, not searched again
- Produces maximal (not necessarily maximum) set of vertex-disjoint shortest M-augmenting paths

**Number of iterations** (Lemma 25.7): O(√V)
- Lemma 25.5: After each iteration, shortest augmenting path length increases
- Lemma 25.6: If shortest M-augmenting path has q edges, |M*| ≤ |M| + |V|/(q+1)
- After √V iterations, q ≥ √V, then at most √V more iterations needed

#### GALE-SHAPLEY (Stable Marriage)
- **Type**: Stable matching algorithm
- **Goal**: Find stable matching with women-proposing (or men-proposing)
- **Input**: n women, n men, preference rankings
- **Output**: Stable matching
- **Complexity**: O(n²)

**Pseudocode** (woman-oriented):
```
GALE-SHAPLEY(men, women, rankings)
1  assign each woman and man as free
2  while some woman w is free
3     let m be the first man on w's ranked list to whom she has not proposed
4     if m is free
5        w and m become engaged (and not free)
6     elseif m ranks w higher than the woman w′ he is currently engaged to
7        m breaks engagement to w′, who becomes free
8        w and m become engaged (and not free)
9     else  m rejects w, with w remaining free
10 return the stable matching consisting of the engaged pairs
```

**Properties**:
- Always terminates (each woman proposes at most n times; ≤ n² iterations)
- Always returns stable matching (Theorem 25.9)
- Returns same result regardless of free woman choice order (Theorem 25.11)
- **Woman-optimal, man-pessimal**: Each woman gets best possible partner in any stable matching; each man gets worst possible (Theorem 25.11, Corollary 25.13)
- **Corollary 25.12**: Some stable matchings may never be returned by Gale-Shapley

#### HUNGARIAN ALGORITHM (Assignment Problem)
- **Type**: Primal-dual algorithm for maximum-weight perfect matching
- **Goal**: Find perfect matching M* with maximum total weight
- **Input**: Complete bipartite graph G = (V,E), V = L ∪ R, |L| = |R| = n, weights w(l,r)
- **Output**: Maximum-weight perfect matching
- **Complexity**: O(n⁴) naive; O(n³) with optimization

**Key idea** (Theorem 25.14): For feasible labeling h (l.h + r.h ≥ w(l,r)), if equality subgraph G_h contains a perfect matching M*, then M* is optimal (max-weight perfect matching).

**Proof of optimality**:
- Σ_{(l,r)∈M*} w(l,r) = Σ_{v} v.h (since M* ⊆ G_h)
- For any other perfect matching M: Σ_{(l,r)∈M} w(l,r) ≤ Σ_{v} v.h (by feasibility)
- Hence M* is optimal

**Initial labeling**: l.h = max_r w(l,r), r.h = 0 (default feasible labeling)

**Greedy maximal matching**:
```
GREEDY-BIPARTITE-MATCHING(G)
1  M = Ø
2  for each vertex l ∈ L
3     if l has an unmatched neighbor in R
4        choose any such unmatched neighbor r ∈ R
5        M = M ∪ {(l,r)}
6  return M
```
- At least half the size of maximum matching (Exercise 25.3-2)

**Finding augmenting path in G_h**:
1. Create directed equality subgraph G_{M,h}: L→R for E_h−M; R→L for M
2. BFS from all unmatched vertices in L
3. Stop when unmatched vertex in R discovered → M-augmenting path found
4. If queue empties before finding augmenting path → need to update labeling

**Label update when search fails**:
- F_L = L ∩ VF (discovered L vertices), F_R = R ∩ VF (discovered R vertices)
- δ = min{l.h + r.h − w(l,r) : l ∈ F_L, r ∈ R − F_R}
- New labels: l.h = l.h − δ for l ∈ F_L; r.h = r.h + δ for r ∈ F_R
- At least one new edge enters equality subgraph (l ∈ F_L, r ∈ R−F_R with slack = δ)
- No edge in F or M leaves equality subgraph (Lemma 25.15)

**Pseudocode**:
```
HUNGARIAN(G)
1  for each vertex l ∈ L
2     l.h = max { w(l,r) : r ∈ R }
3  for each vertex r ∈ R
4     r.h = 0
5  let M be any matching in G_h
6  form G_h and G_{M,h}
7  while M is not a perfect matching in G_h
8     P = FIND-AUGMENTING-PATH(G_{M,h})
9     M = M ⊕ P
10    update G_h and G_{M,h}
11 return M

FIND-AUGMENTING-PATH(G_{M,h})
   // BFS from unmatched L vertices, with label updates if needed
   // Returns M-augmenting path P
```

### Formulas & Equations
- **Symmetric difference**: X ⊕ Y = (X−Y) ∪ (Y−X)
- **Size after augmentation**: |M ⊕ P| = |M| + 1
- **Berge's theorem**: M is maximum ⇔ no M-augmenting path exists
- **Hall's condition**: Perfect matching exists ⇔ |A| ≤ |N(A)| for all A ⊆ L
- **Feasible labeling**: l.h + r.h ≥ w(l,r) for all l∈L, r∈R
- **Equality subgraph**: G_h = {(l,r) : l.h + r.h = w(l,r)}
- **Optimality**: max_{perfect M} w(M) = min_{feasible h} Σ_v v.h (duality)
- **Label update δ**: min{l.h + r.h − w(l,r) : l∈F_L, r∈R−F_R}
- **Hopcroft-Karp bound**: |M*| ≤ |M| + |V|/(q+1) (Lemma 25.6)

### Comparisons & Trade-offs

| Problem | Algorithm | Complexity | Notes |
|---------|-----------|-----------|-------|
| Max bipartite matching (via flow) | Ford-Fulkerson | O(VE) | Simple reduction |
| Max bipartite matching | Hopcroft-Karp | O(√V · E) | Faster for sparse |
| Max general matching | Edmonds ("blossom") | O(V⁴) → O(V³) | Polynomial but complex |
| Stable marriage | Gale-Shapley | O(n²) | Optimal for proposing side |
| Assignment (max weight) | Hungarian | O(n⁴) → O(n³) | Primal-dual |
| Weighted matching | Hungarian variant | O(n³) | Integer weights 0..W: O(√nW) |

### Edge Cases & Pitfalls
- **Stable roommate**: May have no stable matching (Exercise 25.2-5); stable marriage always does
- **Unstable matching always exists** in trivial cases (2 women, 2 men with same preferences → Exercise 25.2-2)
- **Non-bipartite matching**: maximum matching ≠ fractional matching optimum (Problem 25-4)
- **Hungarian with |L| ≠ |R|**: Add dummy vertices with 0-weight edges (Exercise 25.3-7)
- **Minimization instead of maximization**: Negate weights and run Hungarian (Exercise 25.3-6)
- **Non-complete bipartite graphs**: Add edges with weight 0 or −∞ as appropriate (Problem 25-3)
- **Maximal ≠ maximum** for augmenting path set in Hopcroft-Karp; maximal is sufficient
- **Multiple stable matchings** may exist; Gale-Shapley returns only woman-optimal one
- **National Resident Matching**: Hospitals can take multiple students; modification of Gale-Shapley (Exercise 25.2-3)

### Proof & Argument Patterns
- **Berge's theorem**: Forward (augmenting path ⇒ not maximum) via Lemma 25.1; backward (not maximum ⇒ augmenting path) via Lemma 25.3 and symmetric difference
- **Hall's theorem**: Perfect matching ⇔ |A| ≤ |N(A)| for all A ⊆ L
- **Hopcroft-Karp correctness**: Corollary 25.4 (Berge) → terminates at max matching
- **Hopcroft-Karp iteration bound**: Lemma 25.5 (path length increases) + Lemma 25.6 (size bound via q) → O(√V) iterations
- **Gale-Shapley stability proof**: Show any blocking pair cannot exist by examining proposal history
- **Hungarian optimality**: Sum of labels = upper bound on matching weight; equality attained when perfect matching in G_h
- **Label update validity** (Lemma 25.15): Feasibility preserved; edges in F or M stay in G_h; at least one new edge enters

### End-of-Chapter Material
- **Problems**: Perfect matchings in regular bipartite graphs (25-1), Reducing Hungarian to O(n³) (25-2), Other matching problems via Hungarian (25-3), Fractional matchings (25-4), Computing vertex labels from matching (25-5)
- **Key exercises**: 25.1-4 (bound iterations by 2⌈√(|V|)⌉+1), 25.1-5 (prove Hall's theorem), 25.1-6 (d-regular bipartite has perfect matching, in fact d disjoint), 25.2-5 (stable roommate counterexample with no stable matching), 25.3-2 (greedy matching at least half of maximum), 25.3-7 (unbalanced assignment problem)

---

## Cross-Cutting Topics

### Design Paradigms & Meta-Methods

| Paradigm | Where Used |
|----------|-----------|
| **Greedy** | MST (Kruskal, Prim), Dijkstra, Gale-Shapley, greedy maximal matching |
| **Dynamic programming** | Bellman-Ford (all-pairs interpretation), Floyd-Warshall, matrix-multiplication APSP, SLOW/FASTER-APSP |
| **Divide and Conquer** | Not central in these chapters (but MST-REDUCE uses contraction) |
| **Graph search (BFS/DFS)** | Foundations for all graph algorithms; BFS for Edmonds-Karp and Hopcroft-Karp |
| **Relaxation** | Universal technique for shortest paths; iterative bound-tightening |
| **Augmenting paths** | Ford-Fulkerson (flow), Hopcroft-Karp (matching), Hungarian (matching) |
| **Primal-dual** | Hungarian algorithm; maximize matching weight = minimize label sum |
| **Cut-and-paste** | MST proofs (cut property, cycle property) |
| **Reweighting** | Johnson's algorithm; preserves shortest paths while making weights nonnegative |
| **Scaling** | Gabow's shortest-path scaling; max-flow-by-scaling |
| **Contraction** | MST-REDUCE (Borůvka), global min-cut (randomized contraction) |
| **Reduction** | Maximum matching → maximum flow; difference constraints → shortest paths; maximum flow → linear programming |

### Proof & Argument Patterns

| Pattern | Example |
|---------|---------|
| **Induction on operations** | BFS queue invariant (Lemma 20.3), DFS correctness |
| **Contradiction with minimum counterexample** | BFS correctness (Theorem 20.5), Dijkstra correctness |
| **White-path theorem** | DFS descendant characterization |
| **Parenthesis nesting** | DFS interval containment |
| **Cut-and-paste** | Cut property for MST, cycle property |
| **Path-relaxation property** | Bellman-Ford, Dijkstra, DAG-SP correctness |
| **Summation around cycle** | Negative cycle detection (Bellman-Ford, difference constraints) |
| **Loop invariant** | GENERIC-MST, Prim's algorithm |
| **Symmetric difference** | Matching augmentation (Lemma 25.1, Lemma 25.3) |
| **Induction on iterations** | Ford-Fulkerson integrality |
| **Monotonicity + distance bound** | Edmonds-Karp O(VE) bound |
| **Duality** | Max-flow min-cut, Hungarian algorithm (label sum = matching weight) |
| **Scaling / doubling** | FASTER-APSP (repeated squaring), capacity scaling |

### People & Dates

| Person | Contribution |
|--------|------------|
| **E. W. Dijkstra** | Single-source shortest paths (1959); SCC via cycle contraction |
| **R. Bellman, L. Ford** | Bellman-Ford algorithm |
| **E. F. Moore** | BFS (finding paths through mazes) |
| **J. Hopcroft, R. Tarjan** | Adjacency-list advocacy, DFS importance; Hopcroft-Karp matching |
| **R. E. Tarjan** | Linear-time SCC algorithm; MST verification |
| **S. R. Kosaraju** | SCC algorithm (unpublished) |
| **D. E. Knuth** | First linear-time topological sort |
| **J. B. Kruskal** | Kruskal's MST algorithm (1956) |
| **R. C. Prim** | Prim's MST algorithm (1957); also V. Jarník (1930) |
| **O. Borůvka** | First MST algorithm (1926) |
| **R. W. Floyd** | Floyd-Warshall algorithm |
| **S. Warshall** | Transitive closure of boolean matrices |
| **D. Johnson** | Johnson's algorithm for all-pairs shortest paths |
| **L. R. Ford, D. R. Fulkerson** | Ford-Fulkerson method; max-flow min-cut theorem |
| **J. Edmonds, R. M. Karp** | Edmonds-Karp algorithm (BFS augmentations); matching in general graphs |
| **E. A. Dinic** | Blocking flow algorithm |
| **H. W. Kuhn, J. Munkres** | Hungarian algorithm for assignment problem |
| **D. König, J. Egerváry** | Hungarian mathematicians (algorithm named after) |
| **D. Gale, L. S. Shapley** | Stable marriage problem (Gale-Shapley algorithm) |
| **C. Berge** | Berge's theorem (augmenting path ↔ max matching) |
| **P. Hall** | Hall's marriage theorem |

### Mnemonics & Memory Aids

**Edge classification by color (DFS)**:
- "While → Tree, Gray → Back, Black → Forward/Cross"
- Mnemonic: **W**hite = **T**ree, **G**ray = **B**ack, **B**lack = **F**orward/**C**ross

**Bellman-Ford steps**: "Init + (V−1) passes + 1 check" → I, (V−1)×E, check cycles

**Dijkstra vs Prim**:
- Both use min-priority queue
- Prim: key = min edge weight to tree; Dijkstra: key = min path distance from source
- Prim: stop when queue empty; Dijkstra: stop when queue empty (all vertices processed)

**Edge relaxation comparison**:
- Prim: `if v ∈ Q and w(u,v) < v.key`
- Dijkstra: `if v.d > u.d + w(u,v)` (same as RELAX)

**Floyd-Warshall**: "k is the intermediate vertex" — for k=1..n, for i=1..n, for j=1..n

**Max-flow min-cut**: "S = vertices reachable from s in G_f"

---

## Exam Questions by Type

### MCQ

1. **Q**: In a DFS of a directed graph, which edge type is indicated when vertex v is GRAY when edge (u,v) is first explored?  
   **A**: Back edge. **Distractor**: Tree edge (WHITE indicates tree edge)

2. **Q**: What is the running time of TOPOLOGICAL-SORT on a DAG with V vertices and E edges?  
   **A**: Θ(V + E). **Distractor**: O(V lg V + E) (no sorting needed)

3. **Q**: Which shortest-path algorithm works correctly when the graph has negative-weight edges but no negative-weight cycles?  
   **A**: Bellman-Ford. **Distractor**: Dijkstra (fails with negative edges)

4. **Q**: What is the recurrence for the Floyd-Warshall algorithm?  
   **A**: d^(k)ᵢⱼ = min(d^(k−1)ᵢⱼ, d^(k−1)ᵢₖ + d^(k−1)ₖⱼ). **Distractor**: l^(r)ᵢⱼ = min_k(l^(r−1)ᵢₖ + wₖⱼ) (that's matrix multiplication APSP)

5. **Q**: The max-flow min-cut theorem states that:  
   **A**: The value of a maximum flow equals the capacity of a minimum cut. **Distractor**: The value of a maximum flow equals the net flow across any cut

6. **Q**: Which property of shortest paths guarantees that Dijkstra's algorithm works?  
   **A**: Nonnegative edge weights. **Distractor**: No negative-weight cycles (what Bellman-Ford requires)

7. **Q**: In the Gale-Shapley stable marriage algorithm (woman-oriented), what is true about the resulting matching?  
   **A**: Every woman gets her best possible partner in any stable matching. **Distractor**: Every man gets his best possible partner (they get worst)

### Short Answer

1. **Q**: State the white-path theorem and explain why it is important.  
   **Rubric**: (1) In DFS, v is descendant of u iff at time u.d, there is a path of white vertices from u to v. (2) Used to prove DFS edge classification, SCC component graph acyclicity, and Lemma 20.11.

2. **Q**: Explain why Bellman-Ford runs for exactly |V|−1 passes.  
   **Rubric**: (1) Any shortest path is simple, hence has at most |V|−1 edges. (2) Path-relaxation property: after i passes, edges of any shortest path with i edges have been relaxed in order. (3) After |V|−1 passes, all shortest paths correctly computed.

3. **Q**: Why does the cut property (Theorem 21.1) hold for MSTs?  
   **Rubric**: (1) Cut-and-paste: swap edges on cycle. (2) Light edge (u,v) crossing cut plus tree T with A ⊆ T. (3) If (u,v) not in T, cycle formed; edge (x,y) crossing cut can be removed and (u,v) added. (4) w(u,v) ≤ w(x,y) → new tree no heavier → MST.

4. **Q**: What is the purpose of the super-source in Johnson's algorithm?  
   **Rubric**: (1) Need h(v) = δ(s,v) computed by Bellman-Ford. (2) Without super-source, some vertices may be unreachable. (3) Super-source s with 0-weight edges to all vertices ensures reachability. (4) After reweighting, all ŵ(u,v) ≥ 0 by triangle inequality.

### Trace / Apply

1. **Input**: Graph with vertices s,a,b,c; edges s→a(3), s→b(5), a→b(2), b→c(1), a→c(6). Run Dijkstra from s.  
   **Expected output**: s.d=0, a.d=3, b.d=5, c.d=6. **Why**: Extract s→a(3) then relax a→b(5) no change, then extract b(5) relax b→c(6).

2. **Input**: Ford-Fulkerson on a simple graph with capacities s→a(10), s→b(10), a→t(5), a→b(15), b→t(10). Find max flow.  
   **Expected output**: 15. **Why**: Saturate a→t(5), send 10 through b→t(10), flow through a→b can be 5.

### Essay / Long-Form

1. **Q**: Compare and contrast the four single-source shortest-path algorithms: BFS, Bellman-Ford, DAG-SP, and Dijkstra. When would you use each?  
   **Key points**: (1) BFS: unweighted only, O(V+E). (2) Bellman-Ford: handles negative edges, detects cycles, O(VE). (3) DAG-SP: fastest, handles negative, requires DAG, O(V+E). (4) Dijkstra: nonnegative only, O(V²) or O(E lg V). Include correctness conditions, edge cases, trade-offs.

2. **Q**: Explain the relationship between matchings and flows. How does the Hopcroft-Karp algorithm improve on the Ford-Fulkerson approach for bipartite matching?  
   **Key points**: (1) Flow reduction: bipartite graph → unit-capacity flow network. (2) Matching ↔ integer flow (Lemma 24.9). (3) Hopcroft-Karp finds multiple vertex-disjoint augmenting paths per iteration using BFS+DFS. (4) O(√V) iterations vs O(V) for basic augmenting path approach. (5) Each iteration O(E) → O(√V·E) total.

3. **Q**: Prove the max-flow min-cut theorem.  
   **Key points**: (1) (1)⇒(2): augmenting path would increase flow. (2)⇒(3): S = vertices reachable from s in G_f; T = V−S; capacity argument shows |f| = c(S,T). (3)⇒(1): by Corollary 24.5, no flow exceeds cut capacity.
