# Study Notes: Artificial Intelligence — A Modern Approach (Chapters 5–7)

---

## Chapter 5: Adversarial Search and Games

### 1. Named Entities (Terms, Concepts, Algorithms)

| Term | Definition |
|------|-----------|
| **Adversarial search** | Search in competitive environments where two or more agents have conflicting goals |
| **Perfect information** | Synonym for "fully observable"; players know the entire state |
| **Zero-sum game** | What is good for one player is equally bad for the other; no win-win outcome |
| **Move** | Synonym for "action" in games |
| **Position** | Synonym for "state" in games |
| **MAX / MIN** | The two players; MAX maximizes utility, MIN minimizes |
| **Initial state (S₀)** | How the game is set up at the start |
| **TO-MOVE(s)** | The player whose turn it is in state s |
| **ACTIONS(s)** | Set of legal moves in state s |
| **RESULT(s,a)** | Transition model; defines the resulting state |
| **IS-TERMINAL(s)** | Terminal test; true when game is over |
| **Terminal state** | State where game has ended |
| **Utility function / Payoff function** | Final numeric value to player p at terminal state s |
| **State space graph** | Vertices = states, edges = moves |
| **Search tree** | Superimposed over part of state space graph |
| **Game tree** | Complete search tree following every sequence to terminal states |
| **Ply** | One move by one player (one level deeper in game tree) |
| **Minimax value** | Utility for MAX assuming both play optimally |
| **Minimax decision** | Optimal choice at root (maximizing minimax value) |
| **Pruning** | Ignoring portions of search tree that don't affect the optimal move |
| **Alpha–beta pruning** | Technique to eliminate subtrees that make no difference to outcome |
| **α (alpha)** | Best (highest-value) choice found so far along path for MAX ("at least") |
| **β (beta)** | Best (lowest-value) choice found so far along path for MIN ("at most") |
| **Killer moves** | Best moves found previously; tried first |
| **Killer move heuristic** | Strategy of trying killer moves first |
| **Transposition** | Different move permutations leading to same position |
| **Transposition table** | Cache storing heuristic value of states |
| **Type A strategy** | Consider all moves to a fixed depth, use evaluation function |
| **Type B strategy** | Ignore bad moves, follow promising lines deep |
| **Heuristic evaluation function (EVAL)** | Estimates utility of a state |
| **Cutoff test** | Replaces terminal test; decides when to cut off search |
| **Features** | Calculated properties of a state (e.g., piece counts) |
| **Equivalence classes** | States with same feature values |
| **Expected value** | Proportion-weighted average of outcomes |
| **Weighted linear function** | EVAL(s) = Σ wᵢ fᵢ(s) |
| **Material value** | Approximate worth of pieces (pawn=1, knight/bishop=3, rook=5, queen=9) |
| **Quiescence** | Position with no pending wild swings in evaluation |
| **Quiescence search** | Extra search on nonquiescent positions until quiescence reached |
| **Horizon effect** | Unavoidable damage pushed beyond search horizon via delaying tactics |
| **Singular extension** | Clearly-better moves that extend search beyond cutoff |
| **Forward pruning** | Pruning moves that appear poor but might be good |
| **PROBCUT / Probabilistic cut** | Forward-pruning using statistics from prior experience |
| **Late move reduction** | Reduce search depth for later (likely worse) moves |
| **Pure Monte Carlo search** | N simulations from current state; track win percentages |
| **Monte Carlo tree search (MCTS)** | Simulates complete games, uses selection/expansion/simulation/backpropagation |
| **Simulation / Playout / Rollout** | Complete game played to terminal from a state |
| **Playout policy** | Biases moves toward good ones during playout |
| **Selection policy** | Focuses computation on important parts of game tree |
| **Exploration** | Try states with few playouts |
| **Exploitation** | Focus on states that have done well |
| **UCT (Upper Confidence Bounds applied to Trees)** | Selection policy ranking moves by UCB1 formula |
| **UCB1** | UCB1(n) = U(n)/N(n) + C × √(log N(PARENT(n)) / N(n)) |
| **Stochastic game** | Includes random element (dice, shuffled cards) |
| **Chance nodes** | Nodes representing random events (e.g., dice rolls) |
| **Expectiminimax value** | Generalization of minimax for games with chance nodes |
| **Guaranteed checkmate** | Strategy that leads to checkmate for every board state in belief state |
| **Probabilistic checkmate** | Works in every board state; probabilistic w.r.t. player's randomization |
| **Accidental checkmate** | Checkmate achieved without knowing it would be checkmate |
| **Bluff** | Betting as if one's hand is good when it's not |
| **Averaging over clairvoyance** | Treat start as chance node with every deal; assumes full observability after |
| **Metareasoning** | Reasoning about which computations are worth doing |
| **Retrograde minimax search** | Solve endgames by working backwards from terminal states |
| **Null move heuristic** | Good lower bound via shallow search where opponent moves twice |
| **Futility pruning** | Predict in advance which moves cause beta cutoff |
| **Kriegspiel** | Partially observable variant of chess |
| **Early playout termination** | Stop long playouts, evaluate heuristically or declare draw |

### 2. Processes / Algorithms / Pathways

#### MINIMAX-SEARCH (Fig 5.3)
```
MINIMAX-SEARCH(game, state) returns an action:
  player ← game.TO-MOVE(state)
  value, move ← MAX-VALUE(game, state)
  return move

MAX-VALUE(game, state) returns (utility, move):
  if IS-TERMINAL(state) then return UTILITY(state, player), null
  v ← -∞
  for each a in ACTIONS(state):
    v2, a2 ← MIN-VALUE(game, RESULT(state, a))
    if v2 > v then v, move ← v2, a
  return v, move

MIN-VALUE(game, state) returns (utility, move):
  if IS-TERMINAL(state) then return UTILITY(state, player), null
  v ← +∞
  for each a in ACTIONS(state):
    v2, a2 ← MAX-VALUE(game, RESULT(state, a))
    if v2 < v then v, move ← v2, a
  return v, move
```
- Time: O(b^m) where b = branching factor, m = maximum depth
- Space: O(bm) (all actions at once) or O(m) (one at a time)

#### ALPHA-BETA-SEARCH (Fig 5.7)
```
ALPHA-BETA-SEARCH(game, state) returns an action:
  player ← game.TO-MOVE(state)
  value, move ← MAX-VALUE(game, state, -∞, +∞)
  return move

MAX-VALUE(game, state, α, β) returns (utility, move):
  if IS-TERMINAL(state) then return UTILITY(state, player), null
  v ← -∞
  for each a in ACTIONS(state):
    v2, a2 ← MIN-VALUE(game, RESULT(state, a), α, β)
    if v2 > v then v, move ← v2, a
    α ← MAX(α, v)
    if v ≥ β then return v, move    // prune
  return v, move

MIN-VALUE(game, state, α, β) returns (utility, move):
  if IS-TERMINAL(state) then return UTILITY(state, player), null
  v ← +∞
  for each a in ACTIONS(state):
    v2, a2 ← MAX-VALUE(game, RESULT(state, a), α, β)
    if v2 < v then v, move ← v2, a
    β ← MIN(β, v)
    if v ≤ α then return v, move    // prune
  return v, move
```
- With perfect move ordering: O(b^(m/2))
- With random ordering: O(b^(3m/4))

#### Monte Carlo Tree Search (Fig 5.11)
```
MONTE-CARLO-TREE-SEARCH(state) returns an action:
  tree ← NODE(state)
  while IS-TIME-REMAINING():
    leaf ← SELECT(tree)
    child ← EXPAND(leaf)
    result ← SIMULATE(child)
    BACK-PROPAGATE(result, child)
  return move in ACTIONS(state) whose node has highest playouts
```
Four steps (Fig 5.10):
1. **Selection**: Starting at root, choose moves guided by selection policy down to leaf
2. **Expansion**: Generate a new child of selected node
3. **Simulation**: Playout from child node, choosing moves per playout policy (not recorded in tree)
4. **Back-propagation**: Update all nodes on path to root with result

#### Expectiminimax Algorithm
```
EXPECTIMINIMAX(s):
  if IS-TERMINAL(s): return UTILITY(s, MAX)
  if TO-MOVE(s) = MAX:  max_a EXPECTIMINIMAX(RESULT(s,a))
  if TO-MOVE(s) = MIN:  min_a EXPECTIMINIMAX(RESULT(s,a))
  if TO-MOVE(s) = CHANCE: Σ_r P(r) EXPECTIMINIMAX(RESULT(s,r))
```
- Complexity: O(b^m n^m) where n = number of distinct rolls
- For backgammon: b ≈ 20, n = 21, doubles raise b to 4000

### 3. Hierarchies / Classifications

**Game Hierarchy:**
- Deterministic / Stochastic
- Perfect information / Imperfect information (partial observability)
- Zero-sum / Non-zero-sum
- Two-player / Multiplayer
- Turn-taking / Simultaneous

**Search Algorithm Spectrum:**
1. Minimax (exact, full tree) → O(b^m)
2. Alpha–Beta (exact, pruned) → O(b^(m/2)) best case
3. Heuristic Alpha–Beta (approximate, cutoff)
4. Monte Carlo Tree Search (approximate, simulation-based)
5. Expectiminimax (for stochastic games)

**Search Strategies (Shannon):**
- Type A: Wide but shallow (all moves to fixed depth + evaluation)
- Type B: Deep but narrow (follow promising lines)

### 4. Comparisons / Trade-offs

| Criterion | Alpha–Beta | Monte Carlo Tree Search |
|-----------|-----------|------------------------|
| Evaluation | Uses heuristic EVAL function | Uses average of playout outcomes |
| Branching factor | Works well when b is small | Works well when b is high |
| Error vulnerability | Single node miscalculation can mislead | Aggregate of many playouts; less vulnerable |
| Evaluation function quality | Needs accurate EVAL | Can work without expert knowledge |
| Game type | Chess (low b, good EVAL) | Go (high b, hard EVAL) |
| New games | Requires hand-crafted EVAL | Only needs rules |
| Risk | May miss vital line due to pruning | Stochastic nature may fail to consider key move |
| Depth reached (chess) | ~14 ply with transposition table | 10 million playouts vs 6-ply minimax |

**Perfect ordering vs random ordering:**
- Perfect ordering: b^(m/2) nodes
- Random ordering: ~b^(3m/4) nodes (for moderate b)

**Type A vs Type B:**
- Type A: wider, shallower; used most historically for chess
- Type B: deeper, narrower; used for Go; more human-like

### 5. Formulas & Equations

**Minimax definition:**
```
MINIMAX(s) = UTILITY(s, MAX)                                if TERMINAL(s)
           = max_{a∈Actions(s)} MINIMAX(RESULT(s,a))       if TO-MOVE = MAX
           = min_{a∈Actions(s)} MINIMAX(RESULT(s,a))       if TO-MOVE = MIN
```

**Heuristic minimax:**
```
H-MINIMAX(s,d) = EVAL(s,MAX)                                    if IS-CUTOFF(s,d)
               = max_{a} H-MINIMAX(RESULT(s,a), d+1)            if TO-MOVE = MAX
               = min_{a} H-MINIMAX(RESULT(s,a), d+1)            if TO-MOVE = MIN
```

**Weighted linear evaluation function:**
```
EVAL(s) = w₁f₁(s) + w₂f₂(s) + ... + wₙfₙ(s) = Σ_{i=1}^{n} wᵢ fᵢ(s)
```

**Minimax complexity:** O(b^m) time, O(bm) or O(m) space
- Chess: b ≈ 35, m ≈ 80 → 35^80 ≈ 10^123 states

**Alpha–Beta complexity:**
- Best case (perfect ordering): O(b^(m/2)) → effective branching factor ≈ √b
- Random ordering: O(b^(3m/4))
- Chess effective b with perfect ordering: ~6 instead of 35

**UCB1 formula:**
```
UCB1(n) = U(n)/N(n) + C × √(log N(PARENT(n)) / N(n))
```
- U(n) = total utility of playouts through n
- N(n) = number of playouts through n
- C = exploration/exploitation balance constant (theoretical: √2)
- First term = exploitation (avg utility); second = exploration

**Expectiminimax complexity:** O(b^m n^m) where n = distinct chance outcomes

**Retrograde analysis table sizes:**
- 7-piece table: 400 trillion positions (140 TB)
- 8-piece table: 40 quadrillion positions

### 6. Rules, Laws & Theorems

**Optimal play assumption:** Minimax optimal play assumes MIN also plays optimally. If MIN does not, MAX does at least as well (possibly better).

**Alpha–Beta correctness:** Alpha–beta computes the same optimal move as minimax — it is provably correct.

**Zermelo's theorem (1912):** Minimax algorithm — the first formalization traced to Ernst Zermelo.

**Asymptotic optimality of alpha–beta (Pearl, 1982b):** Alpha–beta is asymptotically optimal among all fixed-depth game-tree search algorithms.

**Checkers solved (Schaeffer et al., 2007):** Checkers is a draw with perfect play.

### 7. Data Structures & Types

**Game formal definition elements:**
- Initial state (S₀)
- TO-MOVE(s)
- ACTIONS(s)
- RESULT(s,a) — transition model
- IS-TERMINAL(s) — terminal test
- UTILITY(s,p) — utility function

**Game tree:** nodes = states, edges = moves, leaves = terminal states with utility values

**Transposition table:** Hash table caching evaluated state values; in chess, doubles reachable search depth

**Multiplayer game value representation:** Vector ⟨v_A, v_B, v_C⟩ for each node (one value per player)

**Belief state (Kriegspiel):** Set of all logically possible board states consistent with percept history

### 8. Visual Patterns (Diagram Descriptions)

**Fig 5.1 — Tic-tac-toe game tree:** Partial tree from initial state (empty board), MAX (X) moves first, MIN (O) responds, alternating until terminal states with utilities -1, 0, +1 at leaves.

**Fig 5.2 — Two-ply game tree:** Root MAX node → three MIN nodes (B,C,D) → leaves with utilities 2-14. Root labels: △ = MAX, ▽ = MIN. Optimal path: a₁ → b₁ → utility 3.

**Fig 5.3 — Minimax algorithm pseudocode**

**Fig 5.5 — Alpha–beta stages (6 panels):** (a) First leaf B=3, B ≤ 3. (b) Second leaf B=12, B ≤ 3. (c) Third leaf 8, B = 3, root ≥ 3. (d) First leaf C=2, C ≤ 2, prune C rest. (e) First leaf D=14, D ≤ 14. (f) Second D=5, third D=2, D=2.

**Fig 5.7 — Alpha–beta search algorithm pseudocode**

**Fig 5.8 — Chess positions:** (a) Black advantage (knight+2 pawns). (b) White captures queen. Shows difference material advantage makes.

**Fig 5.9 — Horizon effect chess:** Black bishop doomed; pawn sacrifices push capture beyond horizon.

**Fig 5.10 — MCTS iteration:** (a) Selection down tree to 27/35 leaf. (b) Expansion + simulation (Black wins). (c) Back-propagation: update all nodes to root.

**Fig 5.12 — Backgammon position:** Board numbered 0-25. Black rolls 6-5, four legal moves shown.

**Fig 5.13 — Backgammon game tree:** Chance nodes (circles) for dice rolls between MAX and MIN nodes.

**Fig 5.14 — Order-preserving transformation:** Different leaf values cause different best moves even though preference order preserved.

**Fig 5.15 — KRK guaranteed checkmate belief states:** Black king in 3 possible locations; probing narrows to one.

**Fig 5.16 — Two-ply error example:** Minimax picks right branch (100>99); but with σ=5 error, left branch better 71% of time.

### 9. Edge Cases / Exceptions / Traps

- **Suboptimal opponent**: Minimax optimal move may not be best vs suboptimal opponent (risky move with 9/10 win chance better than certain draw)
- **Horizon effect**: Unavoidable damage pushed beyond search depth by delaying tactics (pawns checking king to delay bishop capture)
- **Non-quiescent position**: Evaluation function inaccurate when pending captures exist; needs quiescence search
- **Transpositions**: Different move sequences leading to same state; handled by transposition table
- **Infinite game tree**: If state space is unbounded or rules allow infinite repeating positions
- **Alpha–beta with random move ordering**: Far less pruning; only O(b^(3m/4)) vs O(b^(m/2))
- **Stochastic games evaluation**: Must be positive linear transform of win probability; order-preserving transforms can change best move
- **Monte Carlo disadvantage**: Might fail to consider vital line; "obviously" winning states still need many playout moves
- **Alliances in multiplayer games**: Emerge from selfish behavior; can be broken
- **Averaging over clairvoyance fails**: Doesn't consider belief state after acting; never gathers information, never bluffs

### 10. Empirical Evidence

- Chess branching factor: ~35; average depth ~80 ply
- Alpha–beta with ordering: ~14 ply depth (vs 6-ply minimax) in same time
- Chess with quiescence + ordering + transposition: expert level (~14 ply)
- Top chess programs (Stockfish): depth 30+, exceed human ability
- PROBCUT: beat regular version 64% of time, even when regular given 2× time
- Checkers: 18 CPU-years to solve; endgame table for 10 pieces: 39 trillion entries
- KBNK solved for all 7-piece endgames: 400 trillion positions, 140 TB
- AlphaZero defeated Stockfish: 155 wins, 6 losses in 1000-game trial
- AlphaZero at 1/10th time still won decisively
- Libratus: 25 million CPU hours; defeated top poker players
- MCTS with 10 million playouts vs minimax 6-ply vs alpha–beta 12-ply
- Go branching factor: 361 initially

### 11. Cross-Chapter Dependencies

- Uses AND–OR search from Chapter 4 (Fig 4.11) as basis
- Iterative deepening (Ch 3, p80) used for depth control
- Beam search (Ch 3, p115) mentioned for forward pruning
- Reinforcement learning (Ch 22) for MCTS and playout policy learning
- Machine learning (Ch 19, 22) for evaluation function weights
- Neural networks (Ch 21) for AlphaGo/AlphaZero
- Game theory (Ch 17, 18) for equilibrium solutions
- Planning (Ch 11) for hierarchical reasoning in games
- Uncertainty/Probability (Ch 12, 16) for evaluation function requirements
- Search algorithms from Chapter 3 for proof sequence finding

### 12. Dates & People

| Person | Contribution |
|--------|-------------|
| **Charles Babbage** (1846) | Discussed feasibility of computer chess |
| **Leonardo Torres y Quevedo** (~1890) | First game-playing machine (KRK endgame) |
| **Ernst Zermelo** (1912) | Minimax algorithm |
| **Claude Shannon** (1950) | Programming a Computer for Playing Chess; Type A/B strategies |
| **John McCarthy** (1956) | Conceived alpha–beta pruning |
| **Alan Turing** (1953) | Chess programming |
| **Donald Knuth & Moore** (1975) | Proved alpha–beta correctness, analyzed complexity |
| **Judea Pearl** (1982b) | Asymptotic optimality of alpha–beta |
| **Metropolis & Ulam** (1949) | Monte Carlo simulation (atomic bomb) |
| **Abramson** (1987) | Introduced MCTS |
| **Kocsis & Szepesvári** (2006) | UCT selection mechanism |
| **David Silver et al.** (2016, 2018) | AlphaGo, AlphaZero |
| **Garry Kasparov** (1997) | Defeated by Deep Blue |
| **Lee Sedol** (2015) | Defeated by AlphaGo |
| **Ke Jie** (2016) | Defeated by AlphaGo |
| **Arthur Samuel** (1959, 1967) | Checkers learning program |
| **Jonathan Schaeffer** (2007) | Solved checkers |
| **Berliner** (1979) | B* algorithm |
| **Bruce Ballard** (1983) | Alpha–beta for chance nodes |
| **Brown & Sandholm** (2017, 2019) | Libratus, Pluribus (poker) |
| **Moravčík et al.** (2017) | DeepStack (poker) |
| **Schrittwieser et al.** (2019) | MuZero (learns rules) |

### 13. Proof & Argument Patterns

- **Minimax correctness**: Mutual recursion defines optimal values; MAX chooses max, MIN chooses min; definition ensures optimal play against optimal opponent
- **Alpha–beta soundness**: α and β maintain bounds; if value known to be worse than current best for the player, prune (branch cannot affect root decision)
- **Alpha–beta with perfect ordering**: Proved to examine O(b^(m/2)) nodes — halves exponent
- **Probability-based move choice**: Left branch better 71% of time given σ=5 error; shows evaluation function error accumulation
- **Expectiminimax evaluation requirement**: Must be positive linear transform of win probability to avoid order-preserving paradox (Fig 5.14)
- **Retrograde analysis completeness**: Working backwards from all terminal states guarantees solution for all positions with those pieces

### 14. Design Paradigms

- **Game-as-search-tree**: State space + utility function + terminal test
- **Depth-first game tree search**: MINIMAX as DFS with backup values
- **Pruning paradigm**: Eliminate irrelevant subtrees via bounds (α–β)
- **Heuristic cutoff**: Replace utility with evaluation at depth limit
- **Simulation-based evaluation**: Instead of heuristic function, average many playouts
- **Four-phase MCTS loop**: Select → Expand → Simulate → Back-propagate
- **Belief-state search**: Maintain set of possible states for partial observability
- **Endgame lookup table**: Precompute policy for all states with few pieces
- **Opening book**: Human expert moves stored for early game
- **Explore vs Exploit tradeoff**: UCB1 balances exploration of uncertain nodes vs exploitation of known good nodes

### 15. Case Studies

**Tic-tac-toe (noughts and crosses):**
- Game tree: < 9! = 362,880 terminal nodes (5,478 distinct states)
- MAX = X, MIN = O
- Utilities: win +1, loss -1, draw 0

**Chess:**
- b ≈ 35, m ≈ 80 → 35^80 ≈ 10^123 states
- Type A search dominant historically
- Material values: pawn=1, knight/bishop=3, rook=5, queen=9
- AlphaZero defeated Stockfish (world champion chess program) using MCTS + neural networks

**Go:**
- Branching factor starts at 361
- No good material-based evaluation function
- AlphaGo defeated Lee Sedol 4-1 (2015), Ke Jie 3-0 (2016)
- AlphaZero surpassed AlphaGo, also beat top chess and shogi programs

**Backgammon:**
- n = 21 distinct dice rolls
- Becomes O(b^m n^m) with expectiminimax
- TD-Gammon learned by self-play; reached world champion level

**Kriegspiel (partially observable chess):**
- Referee adjudicates, announces captures/checks
- Belief state tracking via state estimation
- Guaranteed checkmate: works for all belief states
- Probabilistic checkmate: works with probability 1 (or 1-ε)

**Poker:**
- Stochastic partial observability
- Libratus used abstraction + overnight hole-plugging
- Pluribus defeated 6-player pros

### 16. Ethics

- AlphaZero's success raises concerns: "Hidebound disciplines like education and medicine will also be shaken" (Kasparov)
- 21% of wumpus worlds are "utterly unfair" (gold in/behind pit)
- Game-playing programs raise questions about human obsolescence in strategic domains
- Metareasoning about computational resource allocation

### 17. End-of-Chapter Material (Summary)

1. Game = initial state, legal actions, result, terminal test, utility function
2. Two-player perfect-information zero-sum games: minimax = optimal moves
3. Alpha–beta: same as minimax, more efficient via pruning
4. Heuristic evaluation function for cutoff when full tree infeasible
5. MCTS: evaluates via playout averages rather than heuristic function
6. Opening/endgame tables for lookup
7. Expectiminimax for games of chance
8. Imperfect information: belief state reasoning
9. Programs have defeated champions at chess, checkers, Othello, Go, poker

---

## Chapter 6: Constraint Satisfaction Problems

### 1. Named Entities (Terms, Concepts, Algorithms)

| Term | Definition |
|------|-----------|
| **Constraint satisfaction problem (CSP)** | Problem with variables, domains, constraints |
| **Variables (X)** | Set {X₁,...,Xₙ} |
| **Domains (D)** | Set {D₁,...,Dₙ} of allowable values per variable |
| **Constraints (C)** | Specify allowable combinations of values; each = ⟨scope, rel⟩ |
| **Scope** | Tuple of variables participating in a constraint |
| **Relation (rel)** | Defines values variables can take (explicit tuples or function) |
| **Assignment** | {Xᵢ=vᵢ, Xⱼ=vⱼ, ...} |
| **Consistent/Legal assignment** | Does not violate any constraints |
| **Complete assignment** | Every variable assigned |
| **Solution** | Consistent, complete assignment |
| **Partial assignment** | Some variables unassigned |
| **Partial solution** | Consistent partial assignment |
| **Constraint graph** | Nodes = variables, edges = binary constraints |
| **Unary constraint** | Restricts value of single variable |
| **Binary constraint** | Relates two variables |
| **Binary CSP** | Only unary and binary constraints |
| **Global constraint** | Involves arbitrary number of variables (e.g., Alldiff) |
| **Alldiff constraint** | All involved variables must have different values |
| **Atmost constraint (resource constraint)** | Sum of variables ≤ bound |
| **Cryptarithmetic** | Letters represent distinct digits; addition constraints |
| **Constraint hypergraph** | Nodes = variables, hypernodes (squares) = n-ary constraints |
| **Dual graph transformation** | Create variable per constraint, binary constraint per shared-variable pair |
| **Preference constraints** | Indicate which solutions are preferred (not absolute) |
| **Constrained optimization problem (COP)** | CSP with preference constraints as costs |
| **Constraint propagation** | Using constraints to reduce legal values for variables |
| **Local consistency** | Enforcing consistency in each part of the graph |
| **Node consistency** | All values in domain satisfy unary constraints |
| **Arc consistency** | For every X in domain Dᵢ, ∃ value in Dⱼ satisfying binary constraint |
| **Path consistency** | Tightens binary constraints using implicit constraints from triples |
| **K-consistency** | For any set of k-1 variables and consistent assignment, ∃ consistent value for kth |
| **Strongly k-consistent** | k-consistent, (k-1)-consistent, ..., 1-consistent |
| **Directional arc consistency (DAC)** | Each Xᵢ arc-consistent with each Xⱼ for j > i |
| **Backtracking search** | DFS with partial assignments; exploits commutativity |
| **Commutativity** | Order of variable assignment doesn't matter |
| **Minimum-remaining-values (MRV) heuristic** | Choose variable with fewest legal values |
| **Degree heuristic** | Choose variable with most constraints on unassigned variables |
| **Least-constraining-value heuristic** | Choose value that rules out fewest choices for neighbors |
| **Forward checking** | After assignment, establish arc consistency for assigned variable |
| **Maintaining Arc Consistency (MAC)** | After assignment, run AC-3 on neighboring arcs |
| **Chronological backtracking** | Back up to most recent decision point on failure |
| **Conflict set** | Assignments that conflict with value for a variable |
| **Backjumping** | Backtrack to most recent assignment in conflict set |
| **Conflict-directed backjumping** | Uses deeper conflict sets (preceding variables causing subproblem failure) |
| **Constraint learning** | Record minimal conflict subset as no-good |
| **No-good** | Set of variables and values causing failure |
| **Min-conflicts heuristic** | Choose value that minimizes conflicts with other variables |
| **Tabu search** | Small list of recent states; forbids returning to them |
| **Constraint weighting** | Assign numeric weights to constraints; increment when violated |
| **Connected component** | Independent subproblem in constraint graph |
| **Tree-structured CSP** | Any two variables connected by only one path |
| **Topological sort** | Ordering where each variable appears after its parent |
| **Bounds propagation** | Manage domains by upper/lower bounds rather than explicit sets |
| **Bounds-consistent** | For every X, both lower/upper bounds have satisfying values for all Y |
| **Cycle cutset** | Subset whose removal makes graph a tree |
| **Cutset conditioning** | Assign values to cutset, solve remaining tree |
| **Tree decomposition** | Transform graph into tree where each node = set of variables |
| **Tree width** | (Size of largest node) - 1; minimum width over all decompositions |
| **Value symmetry** | Permuting value names yields other solutions |
| **Symmetry-breaking constraint** | Imposes ordering to eliminate symmetric solutions |
| **Sudoku** | 81 variables (A1-I9), domains {1-9}, 27 Alldiff constraints |
| **Dependency-directed backtracking** | Backjumping + no-good learning |
| **Backmarking** | Save consistent/inconsistent pairwise assignments |

### 2. Processes / Algorithms / Pathways

#### AC-3 (Arc Consistency) (Fig 6.3)
```
AC-3(csp) returns false if inconsistency found, true otherwise:
  queue ← all arcs in csp
  while queue not empty:
    (Xᵢ, Xⱼ) ← POP(queue)
    if REVISE(csp, Xᵢ, Xⱼ):
      if size of Dᵢ = 0: return false
      for each Xₖ in Xᵢ.NEIGHBORS - {Xⱼ}:
        add (Xₖ, Xᵢ) to queue
  return true

REVISE(csp, Xᵢ, Xⱼ) returns true iff domain of Xᵢ revised:
  revised ← false
  for each x in Dᵢ:
    if no y in Dⱼ allows (x,y) to satisfy constraint:
      delete x from Dᵢ
      revised ← true
  return revised
```
- Complexity: O(c d³) where c = binary constraints, d = max domain size
- Each arc inserted at most d times; each check O(d²)

#### BACKTRACKING-SEARCH (Fig 6.5)
```
BACKTRACKING-SEARCH(csp) returns solution or failure:
  return BACKTRACK(csp, {})

BACKTRACK(csp, assignment) returns solution or failure:
  if assignment is complete: return assignment
  var ← SELECT-UNASSIGNED-VARIABLE(csp, assignment)
  for each value in ORDER-DOMAIN-VALUES(csp, var, assignment):
    if value is consistent with assignment:
      add {var=value} to assignment
      inferences ← INFERENCE(csp, var, assignment)
      if inferences ≠ failure:
        add inferences to csp
        result ← BACKTRACK(csp, assignment)
        if result ≠ failure: return result
        remove inferences from csp
      remove {var=value} from assignment
  return failure
```

#### TREE-CSP-SOLVER (Fig 6.11)
```
TREE-CSP-SOLVER(csp) returns solution or failure:
  n ← number of variables
  assignment ← empty
  root ← any variable
  X ← TOPOLOGICAL SORT(X, root)
  for j = n down to 2:
    MAKE-ARC-CONSISTENT(PARENT(Xⱼ), Xⱼ)
    if cannot be made consistent: return failure
  for i = 1 to n:
    assignment[Xᵢ] ← any consistent value from Dᵢ
    if no consistent value: return failure
  return assignment
```
- Complexity: O(n d²) — linear in number of variables

#### MIN-CONFLICTS (Fig 6.9)
```
MIN-CONFLICTS(csp, max_steps) returns solution or failure:
  current ← initial complete assignment
  for i = 1 to max_steps:
    if current is a solution: return current
    var ← randomly chosen conflicted variable
    value ← value v for var minimizing CONFLICTS(csp, var, v, current)
    set var = value in current
  return failure
```

**Cutset conditioning algorithm:**
1. Choose subset S (cycle cutset) such that removing S makes graph a tree
2. For each assignment to S satisfying S's constraints:
   - Remove inconsistent values from remaining variable domains
   - Solve remaining tree CSP
   - If solution found, return it with S assignment
- Complexity: O(d^c · (n-c) d²) where c = cutset size

**Tree decomposition algorithm:**
- Transform graph to tree where each node = set of variables
- Each edge enforces equality of shared variables
- Apply TREE-CSP-SOLVER: O(n d²) where d = size of largest domain (tuples)
- Domain per node = Cartesian product of constituent variable domains
- Complexity: O(n d^(w+1)) where w = tree width

#### Cutset Conditioning (general):
1. Choose cycle cutset S (NP-hard to find minimal)
2. For each assignment to S:
   - Remove inconsistent domain values
   - Solve remaining tree (O((n-c)d²))
   - Return solution if found
- Complexity: O(d^c · (n-c)d²)

#### Conflict-directed backjumping:
```
When variable Xⱼ fails (domain empty):
  conf(Xⱼ) = conflict set of Xⱼ
  backjump to most recent Xᵢ in conf(Xⱼ)
  recompute: conf(Xᵢ) ← conf(Xᵢ) ∪ conf(Xⱼ) - {Xᵢ}
```

### 3. Hierarchies / Classifications

**Domain types:**
- Discrete finite (map coloring: {red,green,blue})
- Discrete infinite (integers, strings)
- Continuous (Hubble telescope timing; linear programming)

**Constraint types:**
| Type | Arity | Example |
|------|-------|---------|
| Unary | 1 | SA ≠ green |
| Binary | 2 | SA ≠ NSW |
| Higher-order | 3+ | Between(X,Y,Z) |
| Global | n | Alldiff(F,T,U,W,R,O) |

**Consistency hierarchy:**
- 1-consistency = Node consistency
- 2-consistency = Arc consistency
- 3-consistency = Path consistency (for binary constraint graphs)
- k-consistency = General form
- Strongly k-consistent = k, k-1, ..., 1 all consistent

**CSP vs atomic state-space search:**
| Property | Atomic search | CSP |
|----------|--------------|-----|
| State | Black box | Factored (variables) |
| Heuristics | Domain-specific | Domain-independent |
| Pruning | Only by goal test | Constraint propagation |
| Branching factor | n·d (any var × any val) | d (single variable) |
| Order matters | Yes | No (commutative) |

### 4. Comparisons / Trade-offs

| Technique | Benefit | Drawback |
|-----------|---------|----------|
| **Node consistency** | Eliminates unary violations | Doesn't propagate |
| **Arc consistency (AC-3)** | Propagates across binary constraints | Can't detect all inconsistencies (e.g., 2-color Australia) |
| **Path consistency (PC-2)** | Detects 3-variable inconsistencies | More expensive |
| **k-consistency** | Guarantees solution for strongly n-consistent | Exponential time & space in n |
| **Forward checking** | Fast incremental arc consistency | Doesn't look ahead far enough |
| **MAC (Maintaining Arc Consistency)** | Full propagation after assignment | More expensive per node |
| **MRV heuristic** | Fail-first; prunes early | Needs tie-breaker initially |
| **Degree heuristic** | Reduces future branching | Less powerful than MRV generally |
| **Least-constraining-value** | Fail-last; leaves flexibility | Only useful for first solution |

| Approach | Complexity | Memory |
|----------|-----------|--------|
| Cutset conditioning | O(d^c · (n-c)d²) | Linear |
| Tree decomposition | O(n d^(w+1)) | Exponential in w |
| Backtracking search (plain) | O(d^n) | O(n) |
| Tree-structured CSP | O(n d²) | O(n) |

### 5. Formulas & Equations

**CSP formal components:**
- X = {X₁, ..., Xₙ}
- D = {D₁, ..., Dₙ} where Dᵢ = {v₁, ..., vₖ}
- C = {⟨scope, rel⟩, ...}

**AC-3 complexity:** O(c d³)
- n variables, max domain size d, c binary constraints
- Each arc inserted at most d times
- Each consistency check: O(d²)

**Tree-structured CSP:** O(n d²)
- n-1 edges; each edge: O(d²)

**Cutset conditioning complexity:** O(d^c · (n-c) d²)
- c = cutset size

**Tree decomposition complexity:** O(n d^(w+1))
- w = tree width = (largest node size) - 1

**Strong n-consistent solution time:** O(n² d)
- Choose value for each Xᵢ from d options, consistent with previous

**Job-shop precedence constraint:**
```
T₁ + d₁ ≤ T₂
```
Example: `Axle F + 10 ≤ Wheel RF`

**Cryptarithmetic constraints (TWO + TWO = FOUR):**
```
O + O = R + 10·C₁
C₁ + W + W = U + 10·C₂
C₂ + T + T = O + 10·C₃
C₃ = F
```

**Disjunctive constraint:**
```
(Axle F + 10 ≤ Axle B) OR (Axle B + 10 ≤ Axle F)
```

**Bounds propagation:**
```
F₁ + F₂ = 420, D₁ = [0,165], D₂ = [0,385]
→ D₁ = [35,165], D₂ = [255,385]
```

### 6. Rules, Laws & Theorems

- **CSP = NP-complete** in general
- **Strong n-consistency → O(n² d) solution**: choose consistent values sequentially with no backtracking
- **No free lunch**: establishing n-consistency is exponential in n
- **Every finite-domain CSP can be reduced to binary CSPs** via auxiliary variables (Exercise 6.NARY)
- **Tree-structured CSPs solvable in linear time** (O(n d²))
- **Graphs with bounded tree width solvable in polynomial time**
- **Four-color theorem** (Appel & Haken, 1977): any planar graph 4-colorable
- **Sudoku on n²×n² board is NP-hard**
- **Hypertree width subsumes all previous width measures** (Gottlob et al., 1999)

### 7. Data Structures & Types

**Constraint graph:** nodes = variables, edges = binary constraints
**Constraint hypergraph:** nodes = variables, squares = n-ary constraints
**Dual graph:** nodes = original constraints, edges = shared variables between constraints

**No-good:** Recorded set of conflicting variable assignments (added as constraint or cache)

**Tree decomposition requirements:**
1. Every variable appears in ≥1 tree node
2. Connected variables appear together in ≥1 node
3. If variable appears in 2 nodes, it appears in every node on path between them

### 8. Visual Patterns (Diagram Descriptions)

**Fig 6.1 — Australia map and constraint graph:**
- (a) 7 regions: WA, NT, Q, NSW, V, SA, T
- (b) Constraint graph: edges connect neighboring regions; SA central with degree 5

**Fig 6.2 — Cryptarithmetic puzzle (TWO+TWO=FOUR):**
- (a) Letter representation
- (b) Hypergraph: top Alldiff constraint box; 4 column addition boxes; variables C₁, C₂, C₃

**Fig 6.6 — Australia search tree:** WA=red → NT=green → Q=...; branches showing value assignment order

**Fig 6.7 — Forward checking progress:** Table with columns WA, NT, Q, NSW, V, SA, T showing domain reductions after each assignment:
- Initial: all {R,G,B}
- After WA=red: NT, SA remove red
- After Q=green: NT, SA, NSW remove green
- After V=blue: SA empty → backtrack

**Fig 6.8 — Min-conflicts 8-queens:** 3 boards showing Q8 → row 3 (1 conflict), then Q6 → row 8 (0 conflicts = solution)

**Fig 6.10 — Tree-structured CSP:** (a) Tree graph with nodes A-G. (b) Topological sort: A as root, B-G in order consistent with tree

**Fig 6.12 — Australia graph with/without SA:**
- (a) Full constraint graph with SA central
- (b) After removing SA: two separate trees (forest)

**Fig 6.13 — Tree decomposition:** WA-NT-SA node → SA-NT-Q → SA-Q-NSW → SA-NSW-V + T (independent)

### 9. Edge Cases / Exceptions / Traps

- **Forward checking misses** some inconsistencies (e.g., NT and SA both forced to blue)
- **Chronological backtracking is silly**: Recoloring Tasmania won't fix South Australia
- **Backjumping redundant with forward checking**: FC prunes same branches
- **Dual graphs can be exponential**: transforming n-ary to binary via auxiliary variables
- **Infinite domains require implicit constraints** (e.g., T₁+d₁ ≤ T₂) — no explicit tuple enumeration
- **Nonlinear constraints on integers**: undecidable
- **Value symmetry**: d! solutions from one — must add symmetry-breaking constraints
- **Sudoku hardest puzzles**: AC-3 insufficient; need path consistency or higher strategies
- **Finding minimal cycle cutset is NP-hard**
- **Finding minimal tree width decomposition is NP-hard**
- **Strong n-consistency requires exponential time & space**
- **n-queens is underconstrained**: solutions densely distributed; min-conflicts solves million-queens in ~50 steps
- **Hard random SAT problems**: only at critical clause/variable ratio (~4.3 for 3-CNF)

### 10. Empirical Evidence

- **Australia map**: 5 neighbors of SA → 3^5=243 assignments reduced to 2^5=32 (87% reduction)
- **n-queens**: min-conflicts solves million-queens in ~50 steps (independent of problem size)
- **Hubble scheduling**: reduced from 3 weeks to ~10 minutes
- **8-queens**: min-conflicts finds solution in 2 steps (Fig 6.8)
- **Sudoku**: AC-3 solves easiest puzzles; PC-2 handles harder (255,960 path constraints)
- **100 Boolean CSP**: subproblem decomposition → from lifetime of universe to < 1 second
- **100 Boolean CSP with cutset c=20**: from lifetime to minutes

### 11. Cross-Chapter Dependencies

- State-space search (Ch 3-4) as foundation
- Heuristic functions (Ch 3) → min-conflicts evaluation
- Local search (Ch 4.1) → hill climbing, simulated annealing for CSPs
- AND-OR search algorithms (Ch 6.5.4) apply to CSPs and probabilistic reasoning
- SAT → Chapter 7 propositional satisfiability
- Belief networks / probabilistic reasoning (Ch 13) use cutset conditioning
- Constraint logic programming
- Operations research / linear programming (continuous-domain CSPs)
- Machine learning (Ch 22) for learning heuristic weights

### 12. Dates & People

| Person | Contribution |
|--------|-------------|
| **Diophantus** (c. 200-284) | Algebraic constraint equations |
| **Brahmagupta** (c. 650) | General integer solution ax+by=c |
| **Gauss** (1829) | Variable elimination for linear equations |
| **Fourier** (1827) | Linear inequality constraints |
| **Francis Guthrie** (1852) | Four-color conjecture |
| **Appel & Haken** (1977) | Four-color theorem proof (computer-assisted) |
| **Georges Gonthier** (2008) | Formal Coq proof of four-color theorem |
| **Ugo Montanari** (1974) | CSP as general class; constraint graphs, path consistency |
| **Alan Mackworth** (1977) | AC-3 algorithm; combining backtracking + consistency |
| **Waltz** (1975) | Constraint propagation for computer vision |
| **David Waltz** | Polyhedral line-labeling |
| **Mohr & Henderson** (1986) | AC-4 algorithm O(c d²) |
| **Freuder** (1978, 1982, 1985) | k-consistency; tree-structured CSPs |
| **Dechter** (1990a,b) | Cycle-cutset; constraint learning; graph-based backjumping |
| **Dechter & Pearl** (1987, 1989) | Induced width / tree decomposition |
| **Robertson & Seymour** (1986) | Tree width |
| **Gaschnig** (1977, 1979) | Backjumping; backmarking |
| **Prosser** (1993) | Conflict-directed backjumping |
| **Gu** (1989) | Min-conflicts heuristic |
| **Minton et al.** (1992) | Developed min-conflicts independently |
| **Stallman & Sussman** (1977) | Dependency-directed backtracking |
| **Doyle** (1979) | Truth maintenance systems |
| **Kirkpatrick et al.** (1983) | Simulated annealing |
| **Cheeseman et al.** (1991) | Easy/hard problem phase transition |
| **Gottlob et al.** (1999) | Hypertree width |
| **Regin** (1994) | Alldiff constraint |
| **Simonis** (2005) | Sudoku as CSP |
| **Golomb & Baumert** (1965) | MRV heuristic |
| **Brelaz** (1979) | Degree heuristic as MRV tiebreaker |

### 13. Proof & Argument Patterns

- **Reduction by constraint**: Once SA=blue, 5 neighbors can't be blue; 243→32 assignments (87% reduction)
- **Commutativity proof**: Order of assignment doesn't matter → single variable per node, branching factor d (not n·d)
- **AC-3 correctness**: Equivalent CSP; same solutions but smaller domains
- **Tree-structured CSP linear time**: DAC + topological sort = no backtracking needed
- **Cutset conditioning correctness**: Removing cutset makes tree; for each cutset assignment, solve tree; combine
- **Tree decomposition correctness**: Requirements ensure each variable has same value across connected nodes
- **Min-conflicts effectiveness**: Solutions densely distributed for n-queens → independent of problem size
- **No free lunch (k-consistency)**: Exponential cost for full n-consistency
- **Bounds consistency proof**: Min-sum detection of Atmost inconsistency

### 14. Design Paradigms

- **Factored representation**: State = variable assignments, not black box
- **Constraint propagation as inference**: Reduce domains before/during search
- **Backtracking + inference interleaving**: MRV → assign → propagate → recurse
- **Fail-first principle**: Choose most constrained variable first (MRV)
- **Fail-last principle**: Try least constraining value first
- **Local consistency as preprocessing**: Node → Arc → Path → k-consistency
- **Cutset conditioning**: Remove nodes to get tree; iterate over removed values
- **Tree decomposition**: Collapse variable sets into tree nodes
- **Constraint learning**: Cache no-goods to avoid repeated failure
- **Complete → local search duality**: Both approaches useful for different problem types

### 15. Case Studies

**Map coloring (Australia):** 7 variables {WA,NT,Q,NSW,V,SA,T}, domains {R,G,B}, 9 inequality constraints. Solved with backtracking + MRV + forward checking.

**Job-shop scheduling (car assembly):** 15 variables (axles, wheels, nuts, caps, inspect). Precedence constraints (Axle F + 10 ≤ Wheel RF), disjunctive constraints, deadline domain {0,...,30}.

**Cryptarithmetic (TWO+TWO=FOUR):** Alldiff on {F,T,U,W,R,O, C₁,C₂,C₃}. Column constraints with carries. Aim: find digit substitution making sum correct.

**8-queens CSP:**
- Variables Q₁...Q₈ (column positions)
- Dᵢ = {1,...,8} (row positions)
- Constraints: no two same row (Qᵢ≠Qⱼ), no same diagonal (|i-j| ≠ |Qᵢ-Qⱼ|)
- Solved by min-conflicts in ~2 steps

**Sudoku:** 81 vars (A1-I9), domain {1-9}, 27 Alldiff constraints (9 rows + 9 cols + 9 boxes). AC-3 solves easiest; PC-2 handles harder (255,960 path constraints). Hardest need "naked triples" strategy.

**Hubble Space Telescope:** Continuous-domain CSP. Scheduling observations with temporal, precedence, power constraints. Solved via min-conflicts in 10 minutes (previously 3 weeks).

### 16. Ethics

- CSP techniques reduce human scheduling effort (Hubble: 3 weeks → 10 minutes)
- Airline scheduling repair via local search: minimize changes from infeasible schedule

### 17. End-of-Chapter Material (Summary)

1. CSP represents state as variable/value pairs; constraints on variables
2. Inference techniques: node, arc, path, k-consistency
3. Backtracking search (DFS) commonly used; inference interwoven with search
4. MRV, degree heuristics for variable selection; least-constraining-value for values
5. Conflict-directed backjumping; constraint learning records no-goods
6. Min-conflicts local search highly effective
7. Complexity related to constraint graph structure
8. Tree-structured CSPs: linear time
9. Cutset conditioning: reduces general to tree; linear memory
10. Tree decomposition: exponential in tree width but faster

---

## Chapter 7: Logical Agents

### 1. Named Entities (Terms, Concepts, Algorithms)

| Term | Definition |
|------|-----------|
| **Knowledge-based agent** | Uses reasoning over internal knowledge representation to decide actions |
| **Knowledge base (KB)** | Set of sentences |
| **Sentence** | Expression in knowledge representation language |
| **Knowledge representation language** | Language for expressing assertions |
| **Axiom** | Sentence taken as given without derivation |
| **TELL** | Operation to add sentence to KB |
| **ASK** | Operation to query KB |
| **Inference** | Deriving new sentences from old |
| **Background knowledge** | Initial knowledge in KB |
| **Knowledge level** | Abstract description of what agent knows and its goals |
| **Implementation level** | Physical realization of knowledge and reasoning |
| **Declarative approach** | Building agent by TELLing it what it needs to know |
| **Procedural approach** | Encoding desired behaviors as program code |
| **Wumpus world** | Cave + rooms + wumpus + pits + gold; agent testbed |
| **PEAS description** | Performance, Environment, Actuators, Sensors |
| **Syntax** | Structure of well-formed sentences |
| **Semantics** | Meaning/truth of sentences w.r.t. possible worlds |
| **Truth** | Property of sentence in a possible world |
| **Possible world** | Complete state of affairs in which sentences are true/false |
| **Model** | Mathematical abstraction with fixed truth values (synonym for possible world) |
| **Satisfaction** | Model m satisfies sentence α (m is model of α): m(α) = true |
| **Entailment (⊧)** | α ⊧ β iff in every model where α true, β also true; M(α) ⊆ M(β) |
| **Logical inference** | Deriving conclusions via entailment |
| **Model checking** | Enumerating all models to check if α true in all KB models |
| **Soundness / Truth-preserving** | Derives only entailed sentences |
| **Completeness** | Can derive any entailed sentence |
| **Grounding** | Connection between logical reasoning and real environment |
| **Propositional logic** | Logic with proposition symbols and connectives |
| **Proposition symbol** | Atomic sentence representing a proposition (e.g., P, Q, W₁,₃) |
| **Atomic sentence** | Single proposition symbol |
| **Complex sentence** | Constructed from simpler sentences using connectives |
| **Logical connectives** | ¬ (not), ∧ (and), ∨ (or), ⇒ (implies), ⇔ (iff) |
| **Negation (¬)** | "Not" — highest precedence |
| **Literal** | Atomic sentence (positive) or negated atomic sentence (negative) |
| **Conjunction (∧)** | "And" — parts are conjuncts |
| **Disjunction (∨)** | "Or" — parts are disjuncts |
| **Implication (⇒)** | "Implies" — premise/antecedent, conclusion/consequent |
| **Biconditional (⇔)** | "If and only if" |
| **Truth value** | true or false |
| **Truth table** | Specifies truth value for each assignment |
| **Validity** | Sentence true in all models (tautology) |
| **Deduction theorem** | α ⊧ β iff (α⇒β) is valid |
| **Satisfiability** | Sentence true in some model |
| **SAT problem** | Determining satisfiability of propositional sentence (first NP-complete problem) |
| **Theorem proving** | Applying inference rules to construct proof |
| **Logical equivalence (≡)** | α and β true in same set of models |
| **Inference rules** | Patterns of sound inference |
| **Proof** | Chain of conclusions leading to goal |
| **Modus Ponens** | From α⇒β and α, infer β |
| **And-Elimination** | From α∧β, infer α (or β) |
| **Monotonicity** | Entailed set only increases as info added; if KB ⊧ α then KB∧β ⊧ α |
| **Resolution** | Single sound inference rule yielding complete algorithm |
| **Resolvent** | Clause produced by resolving two clauses |
| **Unit resolution** | ℓ₁∨...∨ℓₖ, m / ℓ₁∨...∨ℓᵢ₋₁∨ℓᵢ₊₁∨...∨ℓₖ (ℓᵢ and m complementary) |
| **Complementary literals** | One is negation of the other |
| **Clause** | Disjunction of literals |
| **Unit clause** | Clause with one literal |
| **Full resolution** | ℓ₁∨...∨ℓₖ, m₁∨...∨mₙ → resolve complementary pair |
| **Factoring** | Removing duplicate literals from clause |
| **Conjunctive normal form (CNF)** | Conjunction of clauses |
| **Horn clause** | Disjunction with at most one positive literal |
| **Definite clause** | Disjunction with exactly one positive literal |
| **Goal clause** | Horn clause with no positive literals |
| **Body** | Premise of definite clause in implication form |
| **Head** | Conclusion of definite clause in implication form |
| **Fact** | Single positive literal sentence |
| **Forward chaining** | Data-driven reasoning from known facts |
| **Backward chaining** | Goal-directed reasoning from query |
| **Data-driven reasoning** | Starting from known data |
| **Goal-directed reasoning** | Starting from query |
| **Davis–Putnam (DPLL) algorithm** | Complete backtracking SAT algorithm |
| **Early termination** | Detect sentence true/false with partial model |
| **Pure symbol** | Symbol always same sign in all clauses |
| **Unit clause heuristic** | Assign unit clause's literal before branching |
| **Unit propagation** | Cascade of forced assignments from unit clauses |
| **WALKSAT** | Local search SAT algorithm, random + greedy flips |
| **Underconstrained problem** | Few clauses; many models; easy |
| **Overconstrained problem** | Many clauses; likely unsolvable; easy |
| **CNF_k(m,n)** | k-CNF with m clauses, n symbols |
| **Satisfiability threshold conjecture** | For each k≥3, threshold ratio rₖ for phase transition |
| **Fluent** | Changing aspect of world (state variable indexed by time) |
| **Atemporal variable** | Permanent aspect; no time index |
| **Effect axiom** | Specifies outcome of action at next time step |
| **Frame problem** | Need to specify what stays unchanged after action |
| **Frame axiom** | Explicitly asserts propositions that remain same |
| **Representational frame problem** | O(mn) frame axioms needed |
| **Inferential frame problem** | O(nt) projection vs O(kt) |
| **Locality** | Each action changes small k of n fluents |
| **Successor-state axiom** | Defines Fᵗ⁺¹ in terms of Fᵗ and actions |
| **Qualification problem** | Specifying all preconditions for action to work |
| **Hybrid agent** | Combines logical inference + problem-solving search |
| **Caching** | Saving inference results for constant update time |
| **Belief state** | Set of possible current states |
| **State estimation** | Updating belief state with new percepts |
| **Conservative approximation** | Outer envelope around exact belief state (1-CNF) |
| **SATP LAN** | Planning by propositional SAT solving |
| **Precondition axioms** | Action occurrence requires preconditions satisfied |
| **Action exclusion axioms** | Prevents multiple simultaneous actions |
| **Watched literal indexing** | Efficient unit propagation |
| **Survey propagation** | Algorithm for near-threshold random SAT |

### 2. Processes / Algorithms / Pathways

#### KB-AGENT (Fig 7.1)
```
KB-AGENT(percept) returns an action:
  persistent: KB, knowledge base; t, counter
  TELL(KB, MAKE-PERCEPT-SENTENCE(percept, t))
  action ← ASK(KB, MAKE-ACTION-QUERY(t))
  TELL(KB, MAKE-ACTION-SENTENCE(action, t))
  t ← t + 1
  return action
```

#### TT-ENTAILS? (Truth-table enumeration, Fig 7.10)
```
TT-ENTAILS?(KB, α) returns true or false:
  symbols ← list of proposition symbols in KB and α
  return TT-CHECK-ALL(KB, α, symbols, {})

TT-CHECK-ALL(KB, α, symbols, model) returns true or false:
  if EMPTY?(symbols):
    if PL-TRUE?(KB, model): return PL-TRUE?(α, model)
    else: return true
  else:
    P ← FIRST(symbols); rest ← REST(symbols)
    return (TT-CHECK-ALL(KB, α, rest, model∪{P=true})
            and TT-CHECK-ALL(KB, α, rest, model∪{P=false}))
```
- Complexity: O(2ⁿ) time, O(n) space
- Sound and complete for finite model spaces

#### PL-RESOLUTION (Fig 7.13)
```
PL-RESOLUTION(KB, α) returns true or false:
  clauses ← CNF representation of KB ∧ ¬α
  new ← {}
  while true:
    for each pair Cᵢ, Cⱼ in clauses:
      resolvents ← PL-RESOLVE(Cᵢ, Cⱼ)
      if resolvents contains empty clause: return true
      new ← new ∪ resolvents
    if new ⊆ clauses: return false
    clauses ← clauses ∪ new
```
- Resolution closure RC(S): all clauses derivable from S by repeated resolution
- Ground resolution theorem: if S unsatisifiable, RC(S) contains empty clause

#### CNF Conversion:
1. Eliminate ⇔: replace α⇔β with (α⇒β)∧(β⇒α)
2. Eliminate ⇒: replace α⇒β with ¬α∨β
3. Move ¬ inwards: double-negation elimination, De Morgan's laws
4. Distribute ∨ over ∧

#### PL-FC-ENTAILS? (Forward chaining, Fig 7.15)
```
PL-FC-ENTAILS?(KB, q) returns true or false:
  count[c] ← initial # symbols in premise of clause c
  inferred[s] ← false for all symbols
  queue ← symbols known true in KB
  while queue not empty:
    p ← POP(queue)
    if p = q: return true
    if inferred[p] = false:
      inferred[p] ← true
      for each clause c where p in c.PREMISE:
        decrement count[c]
        if count[c] = 0: add c.CONCLUSION to queue
  return false
```
- Linear time in size of KB
- Sound (Modus Ponens based)
- Complete (entailed atomic sentences derived)

#### DPLL (Fig 7.17)
```
DPLL-SATISFIABLE?(s) returns true or false:
  clauses ← CNF of s
  symbols ← proposition symbols in s
  return DPLL(clauses, symbols, {})

DPLL(clauses, symbols, model) returns true or false:
  if every clause true in model: return true
  if some clause false in model: return false
  P, value ← FIND-PURE-SYMBOL(symbols, clauses, model)
  if P non-null: return DPLL(clauses, symbols-P, model∪{P=value})
  P, value ← FIND-UNIT-CLAUSE(clauses, model)
  if P non-null: return DPLL(clauses, symbols-P, model∪{P=value})
  P ← FIRST(symbols); rest ← REST(symbols)
  return DPLL(clauses, rest, model∪{P=true}) or
         DPLL(clauses, rest, model∪{P=false})
```
Improvements over TT-ENTAILS?:
1. Early termination
2. Pure symbol heuristic
3. Unit clause heuristic → unit propagation

#### WALKSAT (Fig 7.18)
```
WALKSAT(clauses, p, max_flips) returns model or failure:
  model ← random assignment
  for i = 1 to max_flips:
    if model satisfies clauses: return model
    clause ← randomly selected false clause
    if RANDOM(0,1) ≤ p:
      flip random symbol in clause
    else:
      flip symbol maximizing satisfied clauses
  return failure
```
- p typically ~0.5
- Sound (if returns model, model valid)
- Not complete (cannot detect unsatisfiability)

#### SATPLAN (Fig 7.22)
```
SATPLAN(init, transition, goal, Tmax) returns solution or failure:
  for t = 0 to Tmax:
    cnf ← TRANSLATE-TO-SAT(init, transition, goal, t)
    model ← SAT-SOLVER(cnf)
    if model not null: return EXTRACT-SOLUTION(model)
  return failure
```
Requirements:
- Init₀: initial state assertions
- Transition₁...Transitionₜ: successor-state axioms
- Goal assertion: HaveGoldᵗ ∧ ClimbedOutᵗ
- Precondition axioms (e.g., Shootᵗ ⇒ HaveArrowᵗ)
- Action exclusion axioms (¬Aᵢᵗ ∨ ¬Aⱼᵗ)

#### HYBRID-WUMPUS-AGENT (Fig 7.20)
```
HYBRID-WUMPUS-AGENT(percept) returns action:
  TELL(KB, percept sentence, time t)
  TELL(KB, temporal physics axioms for time t)
  safe ← {[x,y]: ASK(KB, OKᵗ_xy) = true}
  if ASK(KB, Glitterᵗ) = true:
    plan ← [Grab] + PLAN-ROUTE(current, [1,1], safe) + [Climb]
  if plan empty:
    unvisited ← squares never visited
    plan ← PLAN-ROUTE(current, unvisited ∩ safe, safe)
  if plan empty and HaveArrowᵗ:
    plan ← PLAN-SHOT(current, possible wumpus locations, safe)
  if plan empty:
    plan ← PLAN-ROUTE(current, [1,1], safe) + [Climb]
  action ← POP(plan)
  TELL(KB, action sentence)
  t ← t+1
  return action
```

#### Logical State Estimation (1-CNF belief state):
- For each symbol Xᵗ, try to prove Xᵗ and ¬Xᵗ from previous belief state
- Conjunction of provable literals = new belief state (1-CNF)
- Conservative approximation: includes all possible states (outer envelope)
- May lose information (disjunctions not representable)

### 3. Hierarchies / Classifications

**Logic hierarchy used:**
- Propositional logic (Ch 7) — factored representation
- First-order logic (Ch 8) — structured representation

**Sentence types in propositional logic (BNF, Fig 7.7):**
```
Sentence → AtomicSentence | ComplexSentence
AtomicSentence → True | False | P | Q | R | ...
ComplexSentence → (Sentence) | ¬Sentence | Sentence∧Sentence
                 | Sentence∨Sentence | Sentence⇒Sentence | Sentence⇔Sentence
```
Operator precedence (high to low): ¬, ∧, ∨, ⇒, ⇔

**Clause types (Fig 7.12):**
| Type | Positive literals | Example |
|------|-----------------|---------|
| Definite clause | Exactly one | ¬A ∨ ¬B ∨ C ≡ A∧B ⇒ C |
| Horn clause | At most one | ¬A ∨ ¬B ∨ C or ¬A ∨ ¬B |
| Goal clause | None | ¬A ∨ ¬B ≡ A∧B ⇒ False |
| Unit clause | One literal | P |

**Wumpus world symbol types:**
- Percept symbols: Stenchᵗ, Breezeᵗ, Glitterᵗ, Bumpᵗ, Screamᵗ
- Fluents: Lᵗ_xy, FacingEastᵗ, HaveArrowᵗ, WumpusAliveᵗ
- Atemporal: P_xy, W_xy, B_xy, S_xy

**Entailment verification approaches:**
1. Model checking (enumerate all models) → O(2ⁿ)
2. Theorem proving (inference rules) → proof length dependent
3. SAT solving (unsatisfiability of KB∧¬α)

### 4. Comparisons / Trade-offs

| Aspect | Model checking (TT-ENTAILS?) | Theorem proving (Resolution) | SAT solving (DPLL) |
|--------|-------------------------------|------------------------------|---------------------|
| Method | Enumerate all models | Apply inference rules | Search for satisfying assignment |
| Pros | Sound & complete | Can ignore irrelevant propositions | Very fast in practice |
| Cons | O(2ⁿ) always | Proof may be long | Exponential worst case |
| Best for | Small n | KB with many irrelevant facts | Large structured problems |

| Aspect | Forward chaining | Backward chaining |
|--------|-----------------|-------------------|
| Direction | Data-driven (facts → conclusions) | Goal-driven (query → facts) |
| Use case | Deriving from incoming percepts | Answering specific queries |
| Efficiency | Explores all derivable facts | Only touches relevant facts |
| Complexity | Linear in KB | Linear in KB (typically less) |

| Aspect | DPLL | WALKSAT |
|--------|------|---------|
| Type | Complete backtracking | Local search |
| Sound | Yes | Yes (if model found) |
| Complete | Yes | No (cannot detect unsatisfiability) |
| Best for | Deciding entailment | Finding solutions when they likely exist |
| Termination | Always | Needs max_flips limit |

**Underconstrained vs Overconstrained:**
| | Underconstrained | Overconstrained |
|--|-----------------|----------------|
| m/n ratio | Low | High |
| Solutions | Many | Few/none |
| Difficulty | Easy | Easy |
| Hard region | — | At threshold (~4.3 for 3-CNF) |

### 5. Formulas & Equations

**Entailment definition:**
```
α ⊧ β  iff  M(α) ⊆ M(β)  iff  every model of α is also model of β
```

**Key equivalences:**
```
α ⊧ β  iff  (α⇒β) is valid            (Deduction theorem)
α ⊧ β  iff  (α∧¬β) is unsatisfiable   (Refutation)
α ≡ β  iff  α ⊧ β and β ⊧ α
```

**Standard logical equivalences (Fig 7.11):**
- Commutativity: α∧β ≡ β∧α, α∨β ≡ β∨α
- Associativity: (α∧β)∧γ ≡ α∧(β∧γ), (α∨β)∨γ ≡ α∨(β∨γ)
- Double-negation elimination: ¬(¬α) ≡ α
- Contraposition: α⇒β ≡ ¬β⇒¬α
- Implication elimination: α⇒β ≡ ¬α∨β
- Biconditional elimination: α⇔β ≡ (α⇒β)∧(β⇒α)
- De Morgan: ¬(α∧β) ≡ ¬α∨¬β; ¬(α∨β) ≡ ¬α∧¬β
- Distributivity: α∧(β∨γ) ≡ (α∧β)∨(α∧γ); α∨(β∧γ) ≡ (α∨β)∧(α∨γ)

**Truth tables (Fig 7.8):**
| P | Q | ¬P | P∧Q | P∨Q | P⇒Q | P⇔Q |
|---|---|----|-----|-----|-----|-----|
| F | F | T | F | F | T | T |
| F | T | T | F | T | T | F |
| T | F | F | F | T | F | F |
| T | T | F | T | T | T | T |

**TT-ENTAILS? complexity:** O(2ⁿ) where n = # proposition symbols

**Resolution rule:**
```
ℓ₁∨...∨ℓₖ,   m₁∨...∨mₙ
───────────────────────────   (ℓᵢ and mⱼ complementary)
ℓ₁∨...∨ℓᵢ₋₁∨ℓᵢ₊₁∨...∨ℓₖ∨m₁∨...∨mⱼ₋₁∨mⱼ₊₁∨...∨mₙ
```

**Successor-state axiom template:**
```
Fᵗ⁺¹ ⇔ ActionCausesFᵗ ∨ (Fᵗ ∧ ¬ActionCausesNotFᵗ)
```

**Example: HaveArrow successor-state axiom:**
```
HaveArrowᵗ⁺¹ ⇔ (HaveArrowᵗ ∧ ¬Shootᵗ)
```

**Example: Location successor-state axiom (L₁,₁):**
```
Lᵗ⁺¹₁,₁ ⇔ (Lᵗ₁,₁ ∧ (¬Forwardᵗ ∨ Bumpᵗ⁺¹))
         ∨ (Lᵗ₁,₂ ∧ (FacingSouthᵗ ∧ Forwardᵗ))
         ∨ (Lᵗ₂,₁ ∧ (FacingWestᵗ ∧ Forwardᵗ))
```

**DPLL early termination:**
- Clause true if ANY literal true → whole sentence can be judged true early
- Sentence false if ANY clause has ALL literals false

### 6. Rules, Laws & Theorems

- **Modus Ponens**: From α⇒β and α, infer β
- **And-Elimination**: From α∧β, infer α (or β)
- **Monotonicity**: If KB ⊧ α then KB∧β ⊧ α (entailed set only grows)
- **Deduction theorem**: α ⊧ β iff (α⇒β) is valid
- **Refutation theorem**: α ⊧ β iff (α∧¬β) is unsatisfiable
- **Ground resolution theorem**: If S (set of clauses) unsatisfiable, then resolution closure RC(S) contains empty clause
- **Completeness of resolution**: Resolution can decide entailment for any α,β in propositional logic
- **SAT is NP-complete** (Cook, 1971)
- **Horn clause entailment is linear time** (polynomially solvable subset)
- **Forward chaining completeness**: Every entailed atomic sentence will be derived (fixed-point model proof)
- **DPLL with definite clauses replicates forward chaining**
- **Propositional entailment is co-NP-complete**
- **No algorithm can solve general nonlinear constraints on integers** (undecidable)

### 7. Data Structures & Types

**Knowledge base:** Set of sentences (implicitly conjoined)

**Model:** Assignment of truth values to all proposition symbols

**1-CNF belief state:** Conjunction of provable literals (outer envelope of exact belief state)
- Size: O(n)
- Conservative approximation: includes all possible states, may add extra states

**AND–OR graph (for Horn clauses, Fig 7.16):**
- Nodes = proposition symbols
- AND edges (arc joining multiple edges): all premises needed
- OR edges (no arc): any premise suffices
- Known facts = leaf nodes

**CNF grammar (Fig 7.12):**
```
CNFSentence → Clause₁ ∧ ... ∧ Clauseₙ
Clause → Literal₁ ∨ ... ∨ Literalₘ
Literal → Symbol | ¬Symbol
```

**Watched literal indexing:** Efficient data structure for unit propagation in SAT solvers

### 8. Visual Patterns (Diagram Descriptions)

**Fig 7.2 — Wumpus world:** 4×4 grid. Agent at [1,1] facing east. Wumpus at [1,3]. Pits at [3,1], [3,3], [4,4]. Gold at [2,3]. Stenches, breezes marked in adjacent squares.

**Fig 7.3 — Agent's first step:**
- (a) [1,1]: no percept → [1,2] and [2,1] marked OK
- (b) Move to [2,1]: breeze → P? in [2,2] and [3,1]

**Fig 7.4 — Agent's later steps:**
- (a) Move to [1,2]: stench → W! at [1,3]; no breeze → no pit in [2,2] → P! at [3,1]
- (b) Move to [2,3]: stench + breeze + glitter → grab gold

**Fig 7.5 — Models for pit inference:** 8 possible models (3 pits × 2²). KB true in 3 (no pit in [1,1], breeze in [2,1]). α₁ (no pit in [1,2]) true in all 3. α₂ (no pit in [2,2]) false in one.

**Fig 7.6 — World-to-representation correspondence:** Real world → aspects → semantics → sentences in agent; inference produces new sentences; semantics maps back to world aspects.

**Fig 7.7 — BNF grammar for propositional logic**

**Fig 7.8 — Truth tables for 5 connectives**

**Fig 7.9 — Truth table for wumpus KB:** 128 rows (7 symbols); 3 rows where KB true; P₁,₂ false in all 3

**Fig 7.11 — Standard logical equivalences table**

**Fig 7.14 — Resolution proof tree:** 4 initial clauses → intermediate resolvents → empty clause (⊥)

**Fig 7.16 — AND–OR graph for Horn clauses:**
- (a) KB: P⇒Q, L∧M⇒P, B∧L⇒M, A∧P⇒L, A∧B⇒L, A, B
- (b) Graph: A,B at bottom; Q at top; arcs show conjunctions

**Fig 7.19 — Random SAT landscape:**
- (a) P(satisfiable) vs m/n for 3-CNF, n=50: sharp drop at ~4.3
- (b) Run time vs m/n: peak at ~4.3 for both DPLL and WALKSAT

**Fig 7.20 — HYBRID-WUMPUS-AGENT pseudocode**

**Fig 7.21 — 1-CNF belief state:** Wiggly exact belief state (shaded) within bold-outlined conservative approximation (1-CNF). Circles = possible worlds.

### 9. Edge Cases / Exceptions / Traps

- **Implication truth table confusion**: P⇒Q is true when P false (vacuous truth)
- **Exclusive or vs inclusive or**: Propositional ∨ is inclusive (true when both true)
- **Propositional symbols atomic**: W₁,₃ — W, 1, 3 have no independent meaning
- **KB may not be true in real world**: Learning fallible (wumpuses bathe on leap day)
- **Model checking infinite models**: For arithmetic, infinite models → TT-ENTAILS? fails
- **WALKSAT cannot detect unsatisfiability**: Limits use for proving safety
- **SATPLAN spurious solutions**: Without unique-location, precondition, action-exclusion axioms, SATPLAN produces impossible plans
- **Representational frame problem**: O(mn) frame axioms needed without successor-state axioms
- **Inferential frame problem**: O(nt) projection without proper formulation
- **Qualification problem**: Cannot specify all exceptional preconditions
- **Belief state explosion**: 2ⁿ physical states → 2^(2ⁿ) belief states
- **1-CNF loses disjunctive information**: e.g., (P₃,₁ ∨ P₂,₂) not provable individually
- **Monotonicity means cannot retract conclusions**: Nonmonotonic logics needed for defeasible reasoning
- **SATP LAN in partially observable**: Would set unobservable variables to desired values

### 10. Empirical Evidence

- Wumpus world: 128 models for 7 symbols; KB true in 3
- 4×4 wumpus world: ~100×100 board × 1000 time steps → millions of sentences
- Propositional entailment: co-NP-complete; worst-case exponential
- DPLL (1962): solved 10-15 variables in 10 min; by 1995: ~1000 variables
- Modern SAT solvers (Chaff): millions of variables
- DPLL on 2019 laptop: ~30 variables
- 3-CNF threshold: m/n ≈ 4.26 (sharp peak in runtime)
- WALKSAT median iterations at threshold: ~2000 for n=50, 3-CNF
- Hybrid wumpus agent: few ms for small-to-medium worlds

### 11. Cross-Chapter Dependencies

- **Ch 2**: PEAS description, agent design, condition-action rules
- **Ch 3-4**: State-space search, AND–OR graph search (Fig 4.11), A* search
- **Ch 4**: Belief state (Section 4.4), state estimation
- **Ch 5**: Adversarial search (alternate inference paradigm)
- **Ch 6**: CSP → SAT connection; constraint learning → clause learning; easy/hard problem phase transition
- **Ch 8**: First-order logic (next — propositional logic foundation)
- **Ch 9**: Logic programming (Horn clauses, forward/backward chaining)
- **Ch 10**: Nonmonotonic logics (frame problem); truth maintenance systems
- **Ch 11**: Planning; hierarchical plans
- **Ch 12**: Probability theory for qualification problem
- **Ch 13**: Fuzzy logic (degrees of truth)
- **Ch 16**: Decision theory (evaluation function requirements)
- **Ch 19**: Learning — knowledge compilation
- **Ch 22**: Reinforcement learning (used by AlphaZero)
- **Ch 27**: Philosophy of AI (grounding)
- **Appendix A**: NP-completeness, co-NP-completeness

### 12. Dates & People

| Person | Contribution |
|--------|-------------|
| **McCarthy** (1958, 1968) | Declarative approach; "Programs with Common Sense" |
| **Allen Newell** (1982) | Knowledge level |
| **Aristotle** | Organon; syllogisms |
| **Philo of Megara** (5th c. BCE) | Truth tables |
| **Stoics** (5th c. BCE) | Modus Ponens, deduction theorem |
| **Leibniz** (1646-1716) | Mechanical logical inference |
| **George Boole** (1847) | Mathematical Analysis of Logic |
| **Schröder** (1877) | Conjunctive normal form |
| **Alfred Horn** (1951) | Horn form |
| **Gottlob Frege** (1879) | Begriffschrift; modern logic |
| **Martin Davis** (1954, 1960) | First proof program; DP algorithm |
| **Davis, Logemann, Loveland** (1962) | DPLL |
| **J.A. Robinson** (1965) | Resolution rule; completeness |
| **Cook** (1971) | SAT is NP-complete |
| **McCarthy & Hayes** (1969) | Frame problem |
| **Ray Reiter** (1991) | Successor-state axioms solution |
| **Kautz & Selman** (1992) | Temporal-indexed SAT planning |
| **Selman et al.** (1992, 1996) | GSAT, WALKSAT |
| **Moskewicz et al.** (2001) | Chaff solver (million variables) |
| **Zhang & Stickel** (1996) | Watched literal indexing |
| **Bayardo & Schrag** (1997) | Clause learning in SAT |
| **Amir & Russell** (2003) | Efficient state estimation classes |
| **Stan Rosenschein** (1985) | Circuit-based agents |
| **Rod Brooks** (1986, 1991) | Behavior-based robotics; anti-representation argument |
| **Wittgenstein** (1922) | Tractatus; truth tables |
| **McCulloch & Pitts** (1943) | Boolean circuit agents in brain |
| **Gregory Yob** (1975) | Wumpus world inventor |
| **Michael Genesereth** | Wumpus world as agent testbed |
| **Thielscher** (1999) | Inferential frame problem |

### 13. Proof & Argument Patterns

- **Model checking soundness**: Direct implementation of entailment definition → always correct
- **Model checking completeness**: Finite models → exhaustive enumeration terminates
- **Resolution completeness proof (ground resolution theorem)**:
  - Contrapositive: if RC(S) no empty clause → S satisfiable
  - Construct model by assigning P₁...Pₖ
  - At each step, if RC(S) has ¬Pᵢ with all others false, set Pᵢ=false; else true
  - Prove by contradiction: no clause can first become false at step i
  - Resolution would have created resolvent falsified earlier → contradiction
- **Forward chaining completeness proof**: Fixed-point model exists where all inferred atoms true; no undrawn entailed atom because it would be false in this model → contradiction
- **Monotonicity proof**: If all models of KB satisfy α, then all models of KB∧β also satisfy α (since KB∧β models are subset of KB models)
- **Deduction theorem**: α ⊧ β iff ⊧ (α⇒β) — follows from definition of ⊧ and ⇒ semantics

### 14. Design Paradigms

- **Knowledge-based agent architecture**: Percept → TELL → ASK → action → TELL action → repeat
- **Declarative approach**: TELL agent what it needs to know (vs procedural code)
- **Logic as representation language**: Syntax + semantics → sound inference
- **Model checking**: Direct semantic method for entailment
- **Theorem proving**: Syntactic method using inference rules
- **Refutation (proof by contradiction)**: Show KB∧¬α unsatisfiable
- **CNF representation**: Normal form enabling resolution
- **Horn clause specialization**: Restricted form → efficient forward/backward chaining
- **Data-driven reasoning**: Forward chaining from percepts
- **Goal-driven reasoning**: Backward chaining from queries
- **SAT solving as search**: Complete (DPLL) and incomplete (WALKSAT) approaches
- **Successor-state axioms**: Frame problem solution (fluent-centric, not action-centric)
- **Belief state as logical sentence**: Conservative approximation (1-CNF)
- **SATPLAN**: Planning as SAT; translate to SAT, extract plan from model
- **Hybrid agent**: Combine logical inference for state estimation + search algorithms for planning

### 15. Case Studies

**Wumpus World (detailed):**
- 4×4 grid, start [1,1] facing east
- Performance: +1000 (climb with gold), -1000 (pit/wumpus), -1/action, -10/arrow
- Percepts: Stench (adjacent wumpus), Breeze (adjacent pit), Glitter (gold), Bump (wall), Scream (wumpus dies)
- Actions: Forward, TurnLeft, TurnRight, Grab, Shoot, Climb
- Logical inference sequence (Section 7.2):
  1. [1,1] no percept → [1,2],[2,1] OK
  2. Forward to [2,1]: breeze → pit in [2,2]∨[3,1]
  3. Back to [1,1], forward to [1,2]: stench → wumpus in [1,3]; no breeze → pit in [3,1]
  4. [2,2] OK → move to [2,3]: glitter → grab gold
- Knowledge base: R₁:¬P₁,₁; R₂:B₁,₁⇔(P₁,₂∨P₂,₁); R₃:B₂,₁⇔(P₁,₁∨P₂,₂∨P₃,₁); R₄:¬B₁,₁; R₅:B₂,₁

**Propositional proof example (no pit in [1,2]):**
- R₂ ⇒ R₆ (biconditional elimination) ⇒ R₇ (And-Elimination) ⇒ R₈ (contrapositive) ⇒ R₉ (Modus Ponens with R₄) ⇒ R₁₀ (De Morgan): ¬P₁,₂∧¬P₂,₁

**Resolution proof (pit location):**
- From R₁₃:¬P₂,₂, R₁₅:P₁,₁∨P₂,₂∨P₃,₁ → R₁₆:P₁,₁∨P₃,₁
- From R₁:¬P₁,₁, R₁₆ → R₁₇:P₃,₁

**SATP LAN (Section 7.7.4):**
- Translate initial state, transition axioms, goal, preconditions, exclusions to CNF
- SAT solver finds model
- Extract action variables with true assignment → plan
- Must add unique-location, precondition, and action-exclusion axioms to avoid spurious solutions

**KRK endgame (Kriegspiel):** Guaranteed checkmate through belief-state narrowing; probabilistic checkmate in KBNK (probability 1) and KBBK (probability 1-ε)

### 16. Ethics

- **Grounding problem**: How do we know KB is true in real world? Perception creates connection, but learning is fallible.
- **Declarative vs procedural debate** (1970s-80s): Both approaches valid; successful agents combine both
- **Philosophical implications**: The frame problem cited by Dreyfus (1972) and Crockett (1994) as evidence AI will fail
- **Wittgenstein's Tractatus**: "The world is everything that is the case" — all sentences are either true or false

### 17. End-of-Chapter Material (Summary)

1. Intelligent agents need knowledge; stored as sentences in KB
2. KB agent: knowledge base + inference mechanism; percept → TELL → ASK → action
3. Syntax: sentence structure; Semantics: truth in possible worlds/models
4. Entailment: α ⊧ β iff β true in all α's models; equivalently: (α⇒β) valid, or (α∧¬β) unsatisfiable
5. Inference: sound (derives only entailed), complete (derives all entailed)
6. Propositional logic: proposition symbols + connectives; known true/false/unknown
7. Model checking: enumerate finite models; efficient algorithms: DPLL (backtracking), WALKSAT (local search)
8. Inference rules: resolution (complete for CNF); forward/backward chaining (for Horn clauses)
9. Local search (WALKSAT): sound but not complete
10. Logical state estimation: maintain belief state via transition model; successor-state axioms solve frame problem
11. SATPLAN: planning by SAT solving; needs precondition + action-exclusion axioms
12. Propositional logic: doesn't scale to unbounded environments — needs first-order logic (Ch 8)
