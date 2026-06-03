# Chapters 15-18 Comprehensive Study Notes: Probabilistic Programming, Decision Making & Multiagent Systems

---

# CHAPTER 15: PROBABILISTIC PROGRAMMING

## 1. Named Entities

| Term | Definition |
|------|------------|
| **Probabilistic Programming Language (PPL)** | A language that defines probability distributions over execution traces by incorporating stochastic elements (random choices) into programming languages. Universal in the sense that Turing machines are universal. |
| **Relational Probability Model (RPM)** | A probability model using database semantics (unique names assumption + domain closure) to define a finite set of possible worlds from first-order logic structures with typed constant, function, and predicate symbols. |
| **Open-Universe Probability Model (OUPM)** | A probability model based on full first-order logic semantics allowing existence uncertainty and identity uncertainty; objects can be added/removed across worlds. |
| **Database Semantics** | Assumes unique names assumption and domain closure; guarantees finite possible worlds. |
| **Unique Names Assumption** | Each constant symbol refers to a distinct object. |
| **Domain Closure** | No objects exist beyond those named by constant symbols. |
| **Basic Random Variable** | In an RPM, obtained by instantiating each function with each possible combination of objects. |
| **Type Signature** | Specification of the type of each argument and the function's value, eliminating spurious possible worlds. |
| **Grounding / Unrolling** | Constructing the equivalent Bayesian network from an RPM given known constant symbols. |
| **Relational Uncertainty** | Uncertainty about the dependency structure (e.g., unknown author of a book). |
| **Multiplexer** | A conditional distribution where a selector variable chooses which parent influences the child. |
| **Sybil / Sybil Attack** | Multiple fake identities used to confound a reputation system. |
| **Existence Uncertainty** | Uncertainty about what objects exist. |
| **Identity Uncertainty** | Uncertainty about which logical terms refer to the same object. |
| **Number Statement** | In OUPMs, specifies conditional distributions over the numbers of objects of various kinds. |
| **Origin Function** | A function that records where each generated object came from (e.g., Owner of a LoginID). |
| **Poisson Distribution** | Distribution over nonnegative integers: P(X=k) = λ^k e^(-λ) / k!; mean = λ, variance = λ. |
| **Discrete Log-Normal Distribution** | Distribution where the log of the number of objects is normally distributed. |
| **Order-of-Magnitude Distribution** | OM(μ,σ) uses logs base 10; mean 10^μ, std dev one order of magnitude. |
| **Number Variable** | In OUPM, specifies how many objects of each type with each origin exist in a world. |
| **Generation History** | Each object in an OUPM is identified by its origin trace (e.g., "the third login of the second customer"). |
| **Data Association Problem** | The problem of associating observation data with the objects that generated them; arises in multitarget tracking. |
| **Guaranteed Object** | Objects guaranteed to exist and be distinct (used in RPM-style semantics within larger OUPMs). |
| **False Alarm / Clutter** | Reported observations not caused by real objects. |
| **Detection Failure** | No observation reported for a real object. |
| **Nearest-Neighbor Filter** | Repeatedly chooses the closest pairing of predicted position and observation. |
| **Hungarian Algorithm** | Algorithm that finds the assignment maximizing joint probability of current observations given predicted positions; O(n³) for n! assignments. |
| **Rao-Blackwellization** | Trick: given a specific association hypothesis, filter exactly/efficiently per object instead of sampling state sequences. |
| **Generative Program** | Executable code where every random choice defines a random variable; world = execution trace. |
| **Execution Trace** | A sequence of possible values for the random choices made during program execution. |
| **Adaptive Proposal Distribution** | Gradually learns how to generate MCMC proposals likely to be accepted and effective at exploring the probability landscape. |
| **Indexed Random Variable** | Notation common in statistics (e.g., X[i]), used in BUGS language. |
| **Record Linkage** | Determining when data records refer to the same entity despite lacking unique identifiers. |
| **Markov Logic Network (MLN)** | Maximum-entropy probabilistic logic with constraints as weights on first-order clauses. |
| **Probability Logic** | A logical system where P(φ) ≥ p constrains the distribution over possible worlds. |
| **Probabilistic Database** | Logical sentences labeled with probabilities attached directly to database tuples. |

## 2. Processes/Algorithms

### RPM Inference via Grounding
```
for b = 1 to B do
    add node Quality_b with no parents, prior
for c = 1 to C do
    add node Honest_c with no parents, prior
    add node Kindness_c with no parents, prior
for b = 1 to B do
    add node Recommendation_{c,b} with parents Honest_c, Kindness_c, Quality_b
    and conditional distribution RecCPT(Honest_c, Kindness_c, Quality_b)
```

### MCMC for RPMs with Relational Uncertainty
- Sample complete possible worlds
- In each state relational structure is completely known
- Relational uncertainty causes no increase in network complexity for MCMC
- MCMC includes transitions that change the relational structure

### OUPM Inference (MCMC)
- Explore space of possible worlds (sets of objects + relations)
- Moves alter relations, add/subtract objects, change constant interpretations
- Probability ratio between neighboring worlds depends on constant-size subgraph
- Logical query evaluated incrementally in each world (constant time)
- Samples partial worlds (not complete) when infinite-sized worlds possible

### Generative Program Inference
- **Rejection sampling**: run program, keep traces matching evidence
- **Likelihood weighting**: track weight by multiplying probabilities of observed values
- **MCMC**: sample and modify execution traces; careful about changes (e.g., if-statement outcomes) that invalidate remainder of trace

## 3. Hierarchies/Classifications

### Representation Spectrum
```
Atomic → Factored → Structured
(Search)   (CSPs,     (First-order logic,
            Bayes nets)  planning)
```

### Probability Model Hierarchy
- **Atomic**: HMMs
- **Factored**: Bayesian networks, DBNs, Kalman filters
- **Structured**: RPMs, OUPMs, PPLs (declarative and general)

### Two Routes to Expressive Probability Models
1. **Logical route**: Probabilities over first-order possible worlds (RPMs, OUPMs)
2. **Programming language route**: Stochastic elements in programming languages (PPLs)

### PPL Types
- **Declarative PPLs**: Like logic programming (e.g., BLOG)
- **General PPLs**: Built on general programming languages (e.g., Church on Scheme, Pyro on PyTorch)

## 4. Comparisons/Trade-offs

| Aspect | RPM | OUPM | Generative Program |
|--------|-----|------|-------------------|
| Semantics | Database semantics (finite) | Full first-order (possibly infinite) | Execution traces |
| Object uncertainty | None (known objects) | Existence + identity uncertainty | Depends on program |
| Inference | Grounding + variable elimination / MCMC | MCMC (partial worlds) | Rejection sampling / MCMC |
| Expressiveness | Bounded | Universal (Turing complete) | Universal |

### Inference Approaches for RPMs
| Method | Advantage | Disadvantage |
|--------|-----------|--------------|
| Grounding (full) | Exact | Very large networks |
| Relevant variable grounding | Smaller network | Still limited |
| Cached factors | 1000x speedup for large networks | Requires repeated structure |
| Lifted inference | Avoids grounding entirely | Complex implementation |
| MCMC | Handles relational uncertainty well | Approximate |

## 5. Formulas & Equations

### Probability of a Logical Sentence
```
P(φ) = Σ_{ω: φ is true in ω} P(ω)      (15.1)
```

### Poisson Distribution
```
P(X = k) = λ^k e^(-λ) / k!
```
Mean = λ, Variance = λ, StdDev = √λ

### Generative Program Trace Probability
```
P(ω) = ∏_i P(x_i | x_1, ..., x_{i-1})
```

### Elo/TrueSkill Rating Model
```
Skill(i) ~ N(μ, σ²)
Performance(i, g) ~ N(Skill(i), β²)
Win(i, j, g) = if Game(g, i, j) then (Performance(i, g) > Performance(j, g))
```
For teams: `TeamPerformance(t, g) = Σ_{i ∈ t} Performance(i, g)`

## 6. Rules, Laws & Theorems

- **Well-formedness conditions for RPMs**: Dependencies must be acyclic; must be well-founded (no infinite ancestor chains)
- **Undecidability**: Well-formedness conditions for OUPMs (cyclic dependencies and infinite ancestor chains) are undecidable in general, but syntactic sufficient conditions can be checked
- **Inference undecidability for PPLs**: With infinite-precision continuous random variables, inference encodes the halting problem. With finite-precision, inference remains decidable.

## 9. Edge Cases

- **Relational uncertainty**: When Author(B2) is unknown, system reasons about all possible authors; the Author variable acts as a multiplexer selector
- **Unknown object existence**: Vision systems, text understanding, intelligence analysis all involve uncertainty about what exists
- **Infinite possible worlds**: First-order logic gives infinite possible worlds; database semantics avoids this
- **Unbounded objects**: Poisson distributions allow unbounded objects → unbounded random variables
- **Recursive dependencies**: OUPMs can have recursive dependencies; must be well-founded
- **Infinite sequences**: In multitarget tracking, variables X(a, t) for unbounded t → infinite; MCMC samples partial worlds

## 10. Empirical Evidence

- **Citation matching**: OUPM produces error rate 2-3× lower than CiteSeer (Pasula et al., 2003)
- **NET-VISA**: Missed 11.1% vs UN SEL3's 27.4% for magnitude 3-4 events; finds up to 50% more real events than UN expert analysts; deployed Jan 1, 2018
- **TrueSkill**: Microsoft's engine serves hundreds of millions of users daily
- **PPL speedups**: Compilation yields 2-3 orders of magnitude; Monte Carlo hardware gives 100-10,000×

## 11. Cross-Chapter Dependencies

- Builds on Ch 13-14 (Bayesian networks, inference algorithms: variable elimination, MCMC, Kalman filters)
- Ch 9 (Logic programming) for declarative PPL analogy
- Ch 8 (First-order logic) for semantics
- Ch 14 (DBNs, HMMs, Kalman filters) for temporal models
- Ch 18 (Game theory) references: dishonest customer acts like game theorist
- Ch 21-22 (Deep learning, RL): PPLs built on PyTorch/TensorFlow; adaptive proposals use deep learning

## 14. Design Paradigms

- **Generative modeling approach**: Model the process that generates observations (e.g., researchers → papers → citations)
- **Modular model improvement**: PPLs allow easy model refinement (e.g., adding Markov letter bigram model)

---

# CHAPTER 16: MAKING SIMPLE DECISIONS

## 1. Named Entities

| Term | Definition |
|------|------------|
| **Decision Theory** | Combination of probability theory + utility theory; basis for rational decision-making under uncertainty. |
| **Utility Function U(s)** | A function assigning a single number to express the desirability of a state. |
| **Expected Utility EU(a)** | Average utility value of outcomes weighted by probability: EU(a) = Σ_{s'} P(RESULT(a)=s') U(s') |
| **Principle of Maximum Expected Utility (MEU)** | A rational agent should choose the action maximizing expected utility: action = argmax_a EU(a) |
| **Lottery** | A probabilistic outcome: L = [p₁, S₁; p₂, S₂; ...; pₙ, Sₙ] |
| **Value Function / Ordinal Utility Function** | In deterministic environments, only a preference ranking on states is needed. |
| **Preference Elicitation** | Process of presenting choices to a human to determine their utility function. |
| **Normalized Utilities** | Scale with u⊥ = 0 and u⊤ = 1. |
| **Standard Lottery** | [p, u⊤; (1-p), u⊥] used to assess utility of any prize S by finding p where agent is indifferent. |
| **Micromort** | A one in a million chance of death. |
| **QALY (Quality-Adjusted Life Year)** | Measure where patients accept shorter life expectancy to avoid disability. |
| **Monotonic Preference** | Preferring more money to less, all else equal. |
| **Expected Monetary Value (EMV)** | The expected dollar value of a lottery. |
| **Risk-Averse** | Prefers a sure thing with payoff less than EMV of a gamble (concave utility). |
| **Risk-Seeking** | Prefers gamble over sure thing of equal EMV (convex utility). |
| **Risk-Neutral** | Linear utility curve; indifferent between gamble and its EMV. |
| **Certainty Equivalent** | The value an agent will accept in lieu of a lottery. |
| **Insurance Premium** | Difference between EMV of a lottery and its certainty equivalent. |
| **Order Statistic** | Distribution of any particular ranked element of a sample; used to compute optimizer's curse. |
| **Optimizer's Curse** | Tendency for estimated expected utility of the best choice to be too high due to selection bias. |
| **Winner's Curse** | In auctions, winner likely overestimated the value. |
| **Normative Theory** | Describes how a rational agent should act. |
| **Descriptive Theory** | Describes how actual agents (humans) do act. |
| **Certainty Effect** | People strongly attracted to gains that are certain (Kahneman & Tversky). |
| **Ambiguity Aversion** | People prefer known probabilities over unknown unknowns. |
| **Framing Effect** | Wording of decision problem affects choices (e.g., "90% survival" vs "10% death"). |
| **Anchoring Effect** | A high reference price skews perception of other prices. |
| **Evolutionary Psychology** | Humans are rational in evolutionarily appropriate contexts, not in word problems. |
| **Multiattribute Utility Theory** | Theory of comparing apples to oranges; outcomes characterized by two or more attributes. |
| **Strict Dominance** | Option A strictly dominates B if A is better on all attributes. |
| **Stochastic Dominance** | A₁ stochastically dominates A₂ on X if ∀x ∫_{-∞}^{x} p₁(x')dx' ≤ ∫_{-∞}^{x} p₂(x')dx'; then for any monotonically nondecreasing U, EU(A₁) ≥ EU(A₂). |
| **Preference Independence** | X₁ and X₂ are preferentially independent of X₃ if preference between outcomes differing in X₁, X₂ does not depend on X₃'s value. |
| **Mutual Preferential Independence (MPI)** | Each attribute does not affect how one trades off other attributes. |
| **Additive Value Function** | V(x₁,...,xₙ) = Σᵢ Vᵢ(xᵢ); valid under MPI. |
| **Utility Independence** | Set X is utility independent of Y if preferences between lotteries on X are independent of the particular values of Y. |
| **Mutual Utility Independence (MUI)** | Each subset is utility-independent of the remaining attributes. |
| **Multiplicative Utility Function** | For n attributes with MUI: U = Σ kᵢUᵢ + Σ kᵢkⱼUᵢUⱼ + ... (n single-attribute utilities + n constants). |
| **Decision Network / Influence Diagram** | Bayesian network extended with action (decision) nodes and utility nodes. |
| **Chance Node** | Oval; represents random variables with conditional distributions. |
| **Decision Node** | Rectangle; point where decision maker chooses an action. |
| **Utility Node** | Diamond; represents agent's utility function as a function of parent attributes. |
| **Action-Utility Function / Q-Function** | Expected utility associated with each action (used in simplified decision networks). |
| **Information Value Theory** | Enables agent to choose what information to acquire before making a decision. |
| **Value of Perfect Information (VPI)** | Expected improvement in utility from learning the exact value of a random variable. |
| **Myopic Information Gathering** | Uses VPI formula shortsightedly, as if only a single evidence will be acquired. |
| **Sensitivity Analysis** | Analyzing how output changes as model parameters are tweaked. |
| **Robust / Minimax Decision** | Decision giving best result in worst case: a* = argmax_a min_θ EU(a; θ) |
| **Hedonic Calculus** | Jeremy Bentham's proposal to weigh "pleasures" and "pains" for all decisions. |

## 2. Processes/Algorithms

### Decision Network Evaluation Algorithm
```
1. Set evidence variables for current state.
2. For each possible value of the decision node:
   a. Set decision node to that value.
   b. Calculate posterior probabilities for parent nodes of utility node.
   c. Calculate resulting utility for the action.
3. Return action with highest utility.
```

### Information-Gathering Agent Algorithm
```
function INFORMATION-GATHERING-AGENT(percept) returns an action
    persistent: D, a decision network
    integrate percept into D
    j ← the value that maximizes VPI(Eⱼ) / C(Eⱼ)
    if VPI(Eⱼ) > C(Eⱼ) then return Request(Eⱼ)
    else return the best action from D
```

### Treasure Hunt Optimal Order
- Sort locations by success probability per unit cost: P(i)/C(i) ≥ P(j)/C(j)
- This is the optimal sequence for independent tests with stopping on success.

## 3. Hierarchies/Classifications

### Rational Preference Axioms (von Neumann-Morgenstern)
1. **Orderability**: Exactly one of (A ≻ B), (B ≻ A), (A ∼ B)
2. **Transitivity**: (A ≻ B) ∧ (B ≻ C) ⇒ (A ≻ C)
3. **Continuity**: A ≻ B ≻ C ⇒ ∃p [p, A; 1-p, C] ∼ B
4. **Substitutability**: A ∼ B ⇒ [p, A; 1-p, C] ∼ [p, B; 1-p, C]
5. **Monotonicity**: A ≻ B ⇒ (p > q ⇔ [p, A; 1-p, B] ≻ [q, A; 1-q, B])
6. **Decomposability**: [p, A; 1-p, [q, B; 1-q, C]] ∼ [p, A; (1-p)q, B; (1-p)(1-q), C]

### Risk Attitude Classification
| Attitude | Utility Curve Shape | Behavior |
|----------|-------------------|----------|
| Risk-Averse | Concave | Prefers sure thing < EMV |
| Risk-Neutral | Linear | Indifferent at EMV |
| Risk-Seeking | Convex (in desperate region) | Prefers gamble |

### Human Irrationality Phenomena
- Allais paradox
- Ellsberg paradox (ambiguity aversion)
- Framing effects
- Anchoring effects
- Certainty effect

## 5. Formulas & Equations

### Expected Utility of Action
```
EU(a) = Σ_{s'} P(RESULT(a) = s') U(s')          (16.1)
```
where P(RESULT(a)=s') = Σ_s P(s) P(s'|s,a)

### MEU Principle
```
action = argmax_a EU(a)
```

### Positive Affine Transformation
```
U'(S) = a·U(S) + b,   where a > 0              (16.2)
```

### Lottery Utility
```
U([p₁, S₁; ...; pₙ, Sₙ]) = Σᵢ pᵢ U(Sᵢ)
```

### Optimizer's Curse (Order Statistics)
For k estimates Xᵢ with density f(x) and CDF F(x):
```
P(max{X₁, ..., Xₖ} ≤ x) = F(x)^k
P(x) = d/dx[F(x)^k] = k·f(x)·(F(x))^(k-1)
```

### Stochastic Dominance Condition
A₁ stochastically dominates A₂ on X if:
```
∀x: ∫_{-∞}^{x} p₁(x')dx' ≤ ∫_{-∞}^{x} p₂(x')dx'
```
Then for any monotonically nondecreasing U: EU(A₁) ≥ EU(A₂)

### Additive Value Function (under MPI)
```
V(x₁, ..., xₙ) = Σᵢ Vᵢ(xᵢ)
```

### Multiplicative Utility Function (under MUI)
For 3 attributes: U = k₁U₁ + k₂U₂ + k₃U₃ + k₁k₂U₁U₂ + k₂k₃U₂U₃ + k₃k₁U₃U₁ + k₁k₂k₃U₁U₂U₃

### Value of Perfect Information (VPI)
```
VPI(Eⱼ) = [Σ_{eⱼ} P(Eⱼ=eⱼ) · EU(α_{eⱼ} | Eⱼ=eⱼ)] - EU(α)
```

### VPI Properties
- Nonnegative: VPI(Eⱼ) ≥ 0
- Not additive: VPI(Eⱼ, Eₖ) ≠ VPI(Eⱼ) + VPI(Eₖ) in general
- Order-independent: VPI(Eⱼ, Eₖ) = VPI(Eⱼ) + VPI(Eₖ|Eⱼ) = VPI(Eₖ, Eⱼ)

### Treasure Hunt Expected Cost
```
C(xy) = C(x) + F(x)·C(y)                         (16.3)
```
where F(x) = 1 - P(x) is probability of failure.

Optimal ordering condition: `P(i)/C(i) ≥ P(j)/C(j)`

### Robust Decision
```
a* = argmax_a min_θ EU(a; θ)
```

## 6. Rules, Laws & Theorems

- **Existence of Utility Function**: If preferences obey axioms, there exists U s.t. U(A) > U(B) ⇔ A ≻ B and U(A) = U(B) ⇔ A ∼ B.
- **Expected Utility of a Lottery**: U([p₁,S₁;...;pₙ,Sₙ]) = Σᵢ pᵢ U(Sᵢ)
- **VPI Nonnegativity Theorem**: VPI(Eⱼ) ≥ 0 (expected value, not actual)
- **Deference Theorem**: If machine is uncertain about human's utility for proposed action a, EU(defer) ≥ EU(a). Equality only when negative region has zero probability.
- **Revelation Principle**: Any mechanism can be transformed into an equivalent truth-revealing mechanism.
- **Revenue Equivalence Theorem**: Any auction mechanism where bidders have private values (known distribution) yields same expected revenue.

## 7. Data Structures

### Decision Network Nodes
- **Chance nodes** (ovals): Random variables with conditional distributions
- **Decision nodes** (rectangles): Choice points for actions
- **Utility nodes** (diamonds): Agent's utility function; has parents describing outcomes that directly affect utility

## 10. Empirical Evidence

- **Mr. Beard's utility curve**: U(S_{k+n}) = -263.31 + 22.09 log(n + 150,000) for -$150K ≤ n ≤ $800K (Grayson, 1960)
- **Micromort values**: UK drivers ~$60/micromort (car-buying behavior); US DOT ~$6/micromort (road repairs)
- **Value of statistical life**: ~$10 million (US government agencies, 2019)
- **QALY**: Kidney patients indifferent between 2 years on dialysis and 1 year full health
- **Certainty equivalent**: Most people accept ~$400 instead of [$1000 (0.5); $0 (0.5)] (EMV = $500)

## 11. Cross-Chapter Dependencies

- Ch 12-14: Bayesian networks for probabilistic inference
- Ch 13.4: Variable elimination, MCMC
- Ch 17: Sequential decisions (MDPs, POMDPs) extend one-shot decisions
- Ch 18: Multiagent decision making, game theory
- Ch 22: Reinforcement learning (Q-functions)
- Ch 5: Game playing (minimax, α-β)

## 13. Proof & Argument Patterns

### Proof that Rational Preferences → Utility Function
- From the axioms of utility, can prove existence of U and expected utility property (von Neumann & Morgenstern, 1944)
- Proof sketch: use continuity axiom to establish utility scale, then monotonicity and substitutability to maintain consistency

### Deference Proof
```
EU(a) = ∫_{-∞}^{∞} P(u)·u du = ∫_{-∞}^{0} P(u)·u du + ∫_{0}^{∞} P(u)·u du
EU(d) = ∫_{-∞}^{0} P(u)·0 du + ∫_{0}^{∞} P(u)·u du = ∫_{0}^{∞} P(u)·u du
∴ EU(d) ≥ EU(a) (equality only if P(u<0) = 0)
```

---

# CHAPTER 17: MAKING COMPLEX DECISIONS

## 1. Named Entities

| Term | Definition |
|------|------------|
| **Sequential Decision Problem** | Agent's utility depends on a sequence of decisions over time. |
| **Markov Decision Process (MDP)** | Sequential decision problem with: set of states S, actions A(s), transition model P(s'|s,a), reward function R(s,a,s'), discount factor γ. Markovian transitions. |
| **Policy π** | A solution specifying what action the agent should take in any state it might reach. |
| **Optimal Policy π*** | Policy yielding highest expected utility. |
| **Reward R(s,a,s')** | Numeric reward received for each transition; bounded by ±R_max. |
| **Discount Factor γ** | Number between 0 and 1 describing preference for current vs. future rewards. |
| **Bellman Equation** | U(s) = max_{a∈A(s)} Σ_{s'} P(s'|s,a)[R(s,a,s') + γU(s')] |
| **Q-Function Q(s,a)** | Expected utility of taking action a in state s: Q(s,a) = Σ_{s'} P(s'|s,a)[R(s,a,s') + γ max_{a'} Q(s',a')] |
| **Dynamic Programming** | Simplifying a problem by recursively breaking it into smaller pieces and remembering optimal solutions. |
| **Finite Horizon** | Fixed time N after which nothing matters; leads to nonstationary policies. |
| **Infinite Horizon** | No fixed deadline; optimal policy is stationary. |
| **Stationary Preference** | If you prefer one future to another starting tomorrow, you should still prefer it starting today. |
| **Additive Discounted Reward** | U_h([s₀,a₀,s₁,a₁,...]) = R(s₀,a₀,s₁) + γR(s₁,a₁,s₂) + γ²R(s₂,a₂,s₃) + ... |
| **Proper Policy** | Policy guaranteed to reach a terminal state eventually. |
| **Average Reward** | Alternative criterion comparing infinite sequences by average reward per time step. |
| **Shaping Theorem** | R'(s,a,s') = R(s,a,s') + γΦ(s') - Φ(s) leaves optimal policy unchanged for any potential function Φ. |
| **Potential Φ(s)** | Function analogous to electrical potential; gradient γΦ(s') - Φ(s) leads agent "uphill." |
| **Dynamic Decision Network (DDN)** | DBN extended with decision, reward, and utility nodes; factored MDP representation. |
| **Value Iteration** | Iterative algorithm solving Bellman equations; converges to unique utilities. |
| **Bellman Update** | U_{i+1}(s) ← max_a Σ_{s'} P(s'|s,a)[R(s,a,s') + γU_i(s')] |
| **Contraction** | A function where outputs are "closer together" than inputs; Bellman update contracts by factor γ. |
| **Max Norm** | ||U|| = max_s |U(s)| |
| **Policy Loss** | ||U^{π_i} - U||, the most the agent can lose by executing π_i instead of π*. |
| **Policy Iteration** | Alternates between policy evaluation and policy improvement until convergence. |
| **Policy Evaluation** | Calculate U_i = U^{π_i} given policy π_i. |
| **Policy Improvement** | Calculate new MEU policy using one-step look-ahead based on U_i. |
| **Modified Policy Iteration** | Use simplified value iteration steps (with fixed policy) to approximate utilities. |
| **Asynchronous Policy Iteration** | Apply updates to any subset of states on each iteration. |
| **Linear Programming (for MDPs)** | Formulate MDP as LP: minimize U(s) subject to U(s) ≥ Σ_{s'} P(s'|s,a)[R(s,a,s') + γU(s')] for all s, a. |
| **Expectimax Algorithm** | Builds tree of alternating max and chance nodes for online MDP solving. |
| **Real-Time Dynamic Programming (RTDP)** | Online MDP algorithm; explores state space and solves sub-MDPs. |
| **ǫ-Horizon** | Tree depth H such that sum of rewards beyond leaf at depth H is < ǫ. H = ⌈log_γ ǫ(1-γ)/R_max⌉ |
| **N-Armed Bandit** | n levers (arms), each with fixed but unknown reward distribution; balance exploration vs. exploitation. |
| **Markov Reward Process (MRP)** | MDP with only one possible action (no choice); defines distribution over reward sequences. |
| **One-Armed Bandit** | First arm M yields arbitrary sequence; second arm M_λ yields constant λ. |
| **Stopping Time** | T = number of pulls before switching to the constant arm. |
| **Gittins Index** | Value λ for arm M: max_{T>0} [E(Σ_{t=0}^{T-1} γ^t R_t) / E(Σ_{t=0}^{T-1} γ^t)]; optimal policy = pull highest index. |
| **Restart MDP M_s** | MDP where quitting returns to initial state s; Gittins index = (1-γ) × value of optimal policy for M_s. |
| **Bernoulli Bandit** | Each arm produces 0/1 rewards with fixed but unknown probability μ_i. |
| **Exploration Bonus** | Arms tried fewer times have higher index; encourages exploration. |
| **Upper Confidence Bound (UCB)** | UCB(M_i) = μ̂_i + g(N)/√N_i; pick highest UCB. |
| **Thompson Sampling** | Choose arm randomly according to probability it is optimal given samples. |
| **Selection Problem** | Choose best option with fixed test costs; no index function exists. |
| **Bandit Superprocess (BSP)** | Each arm is a full MDP; arms independent, only one worked on at a time. |
| **Opportunity Cost** | Utility given up per time step by not attending to another arm. |
| **Dominating Policy** | Optimal policy for an arm unaffected by opportunity cost. |
| **Partially Observable MDP (POMDP)** | MDP + sensor model P(e|s); agent doesn't know its state. |
| **Belief State b** | Probability distribution over all possible states; b(s) = P(actual state = s). |
| **Belief State Update (Filtering)** | b'(s') = α P(e|s') Σ_s P(s'|s,a) b(s) |
| **Forward Operator** | b' = α FORWARD(b, a, e) |
| **Point-Based Value Iteration** | Generate conditional plans and α-vectors for finite set of belief states. |
| **POMCP** | Partially Observable Monte Carlo Planning; combines particle filtering + UCT. |
| **Hyperbolic Reward** | Alternative to exponential discounting; dips more steeply in near term. |

## 2. Processes/Algorithms

### Value Iteration Algorithm
```
function VALUE-ITERATION(mdp, ε) returns a utility function
    inputs: mdp with S, A(s), P(s'|s,a), R(s,a,s'), γ
            ε, maximum error allowed
    local: U, U' (vectors of utilities, initially zero)
           δ (maximum relative change)
    repeat
        U ← U'; δ ← 0
        for each state s in S do
            U'[s] ← max_{a∈A(s)} Q-VALUE(mdp, s, a, U)
            if |U'[s] - U[s]| > δ then δ ← |U'[s] - U[s]|
    until δ ≤ ε(1-γ)/γ
    return U
```

### Convergence Properties of Value Iteration
- Bellman update is a contraction by factor γ on the space of utility vectors:
  `||BU_i - BU'_i|| ≤ γ ||U_i - U'_i||` (17.11)
- Therefore value iteration always converges to unique solution when γ < 1
- Error reduced by factor ≥ γ each iteration
- Iterations needed: N = ⌈log(2R_max/ε(1-γ)) / log(1/γ)⌉
- Termination condition: if `||U_{i+1} - U_i|| < ε(1-γ)/γ` then `||U_{i+1} - U|| < ε` (17.12)
- Policy loss bound: if `||U_i - U|| < ε` then `||U^{π_i} - U|| < 2ε` (17.13)

### Policy Iteration Algorithm
```
function POLICY-ITERATION(mdp) returns a policy
    local: U (utilities, initially zero), π (policy, initially random)
    repeat
        U ← POLICY-EVALUATION(π, U, mdp)
        unchanged? ← true
        for each state s in S do
            a* ← argmax_{a∈A(s)} Q-VALUE(mdp, s, a, U)
            if Q-VALUE(mdp, s, a*, U) > Q-VALUE(mdp, s, π[s], U) then
                π[s] ← a*; unchanged? ← false
    until unchanged?
    return π
```

### Policy Evaluation (for fixed policy π)
```
U_i(s) = Σ_{s'} P(s'|s, π_i(s)) [R(s, π_i(s), s') + γ U_i(s')]    (17.14)
```
These are linear equations (no "max" operator); solvable in O(n³).

### Expectimax (Online MDP)
- Build tree of alternating max (decision) and chance nodes
- Evaluation function applied to nonterminal leaves
- Back up: average at chance nodes, maximum at decision nodes
- ǫ-horizon depth: H = ⌈log_γ ε(1-γ)/R_max⌉

### Gittins Index Calculation
```
λ = max_{T>0} E(Σ_{t=0}^{T-1} γ^t R_t) / E(Σ_{t=0}^{T-1} γ^t)    (17.15)
```
- Solve restart MDP M_s (add action to restart from initial state in every state)
- Gittins index = (1-γ) × value of optimal policy for M_s

### POMDP Belief State Update
```
b'(s') = α P(e|s') Σ_s P(s'|s,a) b(s)                            (17.16)
b' = α FORWARD(b, a, e)
```

### POMDP Belief-State Transition
```
P(b'|b,a) = Σ_e P(b'|e,a,b) Σ_{s'} P(e|s') Σ_s P(s'|s,a) b(s)   (17.17)
```
where P(b'|e,a,b) = 1 if b' = FORWARD(b,a,e) else 0.

### POMDP Belief Reward
```
ρ(b,a) = Σ_s b(s) Σ_{s'} P(s'|s,a) R(s,a,s')                    (17.18)
```

### POMDP Value Iteration (Conditional Plans)
```
α_p(s) = Σ_{s'} P(s'|s,a)[R(s,a,s') + γ Σ_e P(e|s') α_{p.e}(s')]  (17.19)
```
where p is depth-d plan with initial action a and subplan p.e for percept e.

### POMDP Expectimax Search
- Decision nodes: belief states
- Chance nodes: branches for possible observations E
- Transition probabilities from Equation (17.17)
- Complexity: O(|A|^d · |E|^d)

### UCT for MDPs
- Adaptation of Monte Carlo tree search to MDPs
- Handles stochastic nature (opponent = nature)
- Uses random playout policy
- Performance: ~160 playouts for 4×3 world to reach 0.4 reward (optimal = 0.7453)

## 3. Hierarchies/Classifications

### MDP Solution Algorithm Comparison
| Algorithm | Type | Complexity | Notes |
|-----------|------|------------|-------|
| Value Iteration | Offline, exact | O(|S|²|A| per iteration) | Converges exponentially; contraction factor γ |
| Policy Iteration | Offline, exact | O(|S|³) per evaluation | Usually fewer iterations; exact for small spaces |
| Linear Programming | Offline, exact | Polynomial in |S|·|A| | Less efficient than DP in practice |
| Expectimax | Online, approximate | O(|A|^d · branching) | Uses tree search |
| RTDP | Online, approximate | Sub-MDP | Similar to LRTA* |
| UCT (MCTS) | Online, approximate | Varies | Uses random playouts |

### Horizon Comparison
| Horizon Type | Policy | Key Property |
|-------------|--------|--------------|
| Finite | Nonstationary | Optimal action depends on time remaining |
| Infinite (discounted) | Stationary | Optimal action depends only on current state |
| Infinite (absorbing) | Possibly stationary | Proper policies reach terminal states |
| Average reward | Stationary | Maximizes per-step reward |

### Utility over Time Approaches
1. **Additive discounted rewards**: U_t = Σ γ^t R_t; finite for γ < 1; empirically valid
2. **Additive undiscounted** (γ=1): Works with proper policies; improper policies yield ∞
3. **Average reward**: lim_{T→∞} (1/T) Σ_{t=0}^{T} R_t; complex analysis

### Bandit Problem Types
| Problem | Structure | Solution |
|---------|-----------|----------|
| One-armed bandit | M + fixed M_λ | Gittins index |
| Bernoulli bandit | Each arm: Bernoulli(μ_i) | Gittins index (approximate), UCB, Thompson sampling |
| Selection problem | Fixed test cost | No index exists |
| Bandit superprocess | Each arm = MDP | Opportunity cost, dominating policies |
| Metalevel decisions | Selection problem (computation cost same regardless) | UCB heuristic may explore too much |

## 5. Formulas & Equations

### Principle of Maximum Expected Utility (MDP)
```
π*(s) = argmax_{a∈A(s)} Σ_{s'} P(s'|s,a)[R(s,a,s') + γU(s')]    (17.4)
```

### Bellman Equation
```
U(s) = max_{a∈A(s)} Σ_{s'} P(s'|s,a)[R(s,a,s') + γU(s')]        (17.5)
```

### Q-Function Definition
```
Q(s,a) = Σ_{s'} P(s'|s,a)[R(s,a,s') + γ max_{a'} Q(s',a')]      (17.8)
U(s) = max_a Q(s,a)                                              (17.6)
π*(s) = argmax_a Q(s,a)                                          (17.7)
```

### Q-VALUE Subroutine
```
function Q-VALUE(mdp, s, a, U) returns a utility value
    return Σ_{s'} P(s'|s,a)[R(s,a,s') + γU[s']]
```

### Infinite Horizon Discounted Sum Bound
```
Σ_{t=0}^{∞} γ^t R(s_t, a_t, s_{t+1}) ≤ R_max / (1-γ)            (17.1)
```

### Expected Utility of Policy π
```
U^π(s) = E[ Σ_{t=0}^{∞} γ^t R(S_t, π(S_t), S_{t+1}) ]           (17.2)
```

### Optimal Policy
```
π*_s = argmax_π U^π(s)                                           (17.3)
```
Remarkable: for discounted infinite horizon, optimal policy independent of starting state.

### Shaping Theorem Transformation
```
R'(s,a,s') = R(s,a,s') + γΦ(s') - Φ(s)                          (17.9)
```
Proof: Let Q'(s,a) = Q(s,a) - Φ(s). Then Q' satisfies Bellman equation for M', and π*_M'(s) = argmax_a Q'(s,a) = argmax_a Q(s,a) - Φ(s) = argmax_a Q(s,a) = π*_M(s).

### Gittins Index Equation
```
λ = max_{T>0} E(Σ_{t=0}^{T-1} γ^t R_t) / E(Σ_{t=0}^{T-1} γ^t)  (17.15)
```

### UCB Formula
```
UCB(M_i) = μ̂_i + g(N)/√N_i
```
where g(N) = (2 log(1 + N log² N))^{1/2} for optimal regret O(log N).

### POMDP Belief State Update
```
b'(s') = α P(e|s') Σ_s P(s'|s,a) b(s)
```

### POMDP Belief MDP Reward
```
ρ(b,a) = Σ_s b(s) Σ_{s'} P(s'|s,a) R(s,a,s')
```

### Conditional Plan Utility (POMDP)
```
α_p(s) = Σ_{s'} P(s'|s,a)[R(s,a,s') + γ Σ_e P(e|s') α_{p.e}(s')]
```

## 6. Rules, Laws & Theorems

- **Bellman Equation**: Foundation of MDP solution via dynamic programming (Bellman, 1957)
- **Contraction Property**: Bellman update contracts by γ; guarantees convergence of value iteration
- **Shaping Theorem**: Adding potential-based reward γΦ(s') - Φ(s) doesn't change optimal policy
- **Gittins Index Theorem**: Optimal policy for bandit = pull arm with highest Gittins index; decision O(n) for first, O(1) thereafter
- **Regret Lower Bound (Lai & Robbins, 1985)**: No algorithm can have regret growing slower than O(log N) for undiscounted case
- **Selection Problem Impossibility**: No index function exists for selection problems
- **POMDP Reduction**: Solving a POMDP on physical state space = solving MDP on belief-state space
- **POMDP Complexity**: PSPACE-hard (very hard indeed)
- **POMDP Utility Convexity**: U(b) as max of hyperplanes → piecewise linear and convex

## 8. Visual Patterns

### 4×3 World MDP (Figure 17.1)
- Grid: 4 columns × 3 rows
- Start: (1,1); Goal: (4,3) (+1) and (4,2) (-1)
- Actions: Up, Down, Left, Right (each with 0.8 intended, 0.1 each right angle)
- Walls block movement
- Reward: -0.04 per nonterminal transition; +1 or -1 at terminal states

### Dynamic Decision Network (Figure 17.4)
- State variables: X_t (location), Ẋ_t (velocity), Charging_t, Battery_t
- Action variables: Plug/Unplug, LeftWheel, RightWheel
- Reward depends on X_t and Charging_t
- Projected 3 steps into future; U for t+3 represents all future rewards

## 10. Empirical Evidence

- **4×3 World**: Optimal utility from start = 0.7453 with γ=1, r=-0.04
- **Policy optimal at i=5** even when max error in U_i = 0.51 (Figure 17.8)
- **Value iteration convergence**: For γ=0.5, ε=0.1, H=5; for γ=0.9, H=44
- **UCT in 4×3 world**: ~160 playouts for reward 0.4 (optimal 0.7453)
- **Tetris MDP**: ~10^62 states; every policy proper
- **ACAS X**: POMDP-based collision avoidance system; significant safety improvement over legacy TCAS

## 11. Cross-Chapter Dependencies

- Ch 16: Utility theory, one-shot decisions → sequential decisions in MDPs
- Ch 14: DBNs → DDNs for factored MDPs; Kalman filters → linear-Gaussian models
- Ch 5: Game trees, expectimax, UCT → MCTS for MDPs
- Ch 4: LRTA* → RTDP
- Ch 3: Search problems as deterministic special case of MDPs
- Ch 22: Reinforcement learning (Q-learning, model-free methods)
- Ch 18: Multiagent MDPs, Markov games

## 12. Dates & People

- **Richard Bellman** (1957): Dynamic Programming, Bellman equation, value iteration
- **John Gittins** (1974, 1989): Gittins index for bandit problems
- **Herbert Robbins** (1952): Bandit problems prominence
- **William Thompson** (1933): Thompson sampling
- **Lai & Robbins** (1985): Asymptotic regret lower bound O(log N)
- **Edward Sondik** (1971): First POMDP value iteration
- **Kearns et al.** (2002): Depth-bounded expectimax with sampling
- **Kocsis & Szepesvári** (2006): UCT algorithm
- **Astrom** (1965): POMDP → belief-space MDP transformation
- **Silver & Veness** (2011): POMCP

---

# CHAPTER 18: MULTIAGENT DECISION MAKING

## 1. Named Entities

| Term | Definition |
|------|------------|
| **Multiagent System** | Environment containing multiple actors that make decisions. |
| **Multiagent Planning Problem** | Planning problem in an environment with multiple agents. |
| **Benevolent Agent Assumption** | Assumption that agents will do what they are told. |
| **Multieffector Planning** | Managing each effector while handling positive/negative interactions. |
| **Multibody Planning** | Planning for physically decoupled units. |
| **Decentralized Planning** | Centralized planning with partially decoupled execution; subplans may include communicative actions. |
| **Counterparts** | Other actors in the environment who are also decision makers with their own preferences. |
| **Coordination Problem** | Ensuring agents pull in same direction without fouling each other's plans. |
| **Game Theory** | Theory of strategic decision making; theoretical foundation for multiagent AI. |
| **Agent Design (Game Theory use)** | Agent analyzes decisions assuming others act rationally. |
| **Mechanism Design** | Defining game rules so collective good is maximized when each agent maximizes its own utility. |
| **Cooperative Game** | Binding agreements possible between agents (e.g., legal contracts). |
| **Non-Cooperative Game** | No central binding agreement; agents may still cooperate if in their interest. |
| **Incentive** | Payment (salary/bonuses) aligning goals in multiagent systems. |
| **Concurrency** | Plans of each agent executed simultaneously. |
| **Interleaved Execution** | Actions atomic; order within each plan preserved; all interleavings must be correct. |
| **True Concurrency** | Actions partially ordered; no full serialization. |
| **Synchronization** | Global clock; all actions same duration; simultaneous lockstep execution. |
| **Joint Action** | ⟨a₁, ..., aₙ⟩ where aᵢ is action taken by ith actor. |
| **Joint Plan** | Specification of what each actor does at each step. |
| **Concurrent Action Constraint** | Specifies which actions must/must not be executed concurrently. |
| **Convention** | Any constraint on selection of joint plans (e.g., "drive on right"). |
| **Social Law** | Widespread convention (e.g., language). |
| **Plan Recognition** | Inferring joint plan from a single action (or short sequence). |
| **Normal Form Game** | All players act simultaneously; defined by players, actions, payoff function. |
| **Payoff Function** | Utility to each player for each combination of actions. |
| **Payoff Matrix** | Combined matrix for two-player games, each cell labeled with both payoffs. |
| **Player** | Decision maker in a game (capitalized names like Ali, Bo). |
| **Row Player / Column Player** | In two-player matrix, row player = one player, column player = the other. |
| **Solution Concept** | Precise notion of rational outcome in game theory. |
| **Strategy** | What game theory calls a policy. |
| **Pure Strategy** | Deterministic policy; for single-move game = single action. |
| **Mixed Strategy** | Randomized policy selecting actions according to a probability distribution (e.g., [0.5:one; 0.5:two]). |
| **Strategy Profile** | Assignment of a strategy to each player. |
| **Prisoner's Dilemma** | Famous game where dominant strategy leads to worse outcome for both. |
| **Dominant Strategy** | A strategy that dominates all others (better regardless of what others do). |
| **Strong Domination** | s strongly dominates s' if outcome is better for every choice of others. |
| **Weak Domination** | s weakly dominates s' if better on at least one profile and no worse on any. |
| **Dominant Strategy Equilibrium** | All players choose a dominant strategy. |
| **Best Response** | A strategy that maximizes payoff given the strategies of others. |
| **Nash Equilibrium** | Strategy profile where no player could unilaterally change to receive higher payoff (each playing best response). |
| **Focal Point** | An outcome that "obviously" stands out for coordination. |
| **Matching Pennies** | Game with no pure-strategy Nash equilibrium. |
| **Social Welfare** | Measure of overall outcome quality for society. |
| **Pareto Optimality** | Outcome where no other outcome would make one player better off without making another worse off. |
| **Utilitarian Social Welfare** | Sum of utilities given to all players. |
| **Egalitarian Social Welfare** | Concerned with distribution; e.g., maximin (maximize worst-off member's utility). |
| **Gini Coefficient** | Summarizes how evenly utility is spread among players. |
| **Myopic Best Response / Iterated Best Response** | Start with random strategy profile; flip non-optimal choices; repeat. |
| **Zero-Sum Game** | Payoffs always add to zero (or constant); one player's gain = another's loss. |
| **Maximin Technique** | von Neumann's method for two-player zero-sum games: first player chooses mixed strategy, second responds with pure strategy. |
| **Maximin Equilibrium** | Mixed strategy Nash equilibrium for zero-sum games. |
| **Repeated Game / Iterated Game** | Players repeatedly play rounds of a stage game. |
| **Stage Game** | The single-move game repeated in a repeated game. |
| **Backward Induction** | Dynamic programming from terminal states backward to compute equilibrium. |
| **Tit-for-Tat** | FSM strategy: start with refuse, then copy opponent's previous move. |
| **GRIM** | FSM strategy: start with refuse; if opponent ever testifies, testify forever. |
| **HAWK** | Always testify. |
| **DOVE** | Always refuse. |
| **Limit of Means** | Average of utilities over infinite sequence: lim_{T→∞} (1/T) Σ_{t=0}^{T} U_t |
| **Nash Folk Theorems** | Every outcome where each player receives at least their security value can be sustained as Nash equilibrium in infinitely repeated game. |
| **Security Value** | Best payoff a player could guarantee to obtain. |
| **Extensive Form** | Game tree representation of sequential games. |
| **Perfect Information** | Players know exactly where they are in the game tree (no uncertainty about history). |
| **Subgame Perfect Nash Equilibrium** | Strategy profile that is Nash equilibrium in every subgame. |
| **Subgame** | Every decision state in game tree defines a subgame. |
| **Credible Threat** | A threat that a rational player would actually carry out if called upon. |
| **Imperfect Information** | Players uncertain about actual state of the game (partial observability). |
| **Information Set** | Game theory term for belief state; nodes where player cannot distinguish which actual state. |
| **Perfect Recall** | Players always remember all their own previous actions. |
| **Sequence Form** | Representation of extensive games linear in tree size (not exponential). |
| **Abstraction** | Simplifying game by grouping states/actions to reduce tree size. |
| **Bayes-Nash Equilibrium** | Equilibrium with respect to a player's prior over other players' strategies. |
| **Assistance Game** | Two-person game where Harriet observes own preferences θ, Robbie has prior P(θ), payoff = θ for both. |
| **Paperclip Game** | Example assistance game: Harriet signals preferences via production choice, Robbie interprets and acts. |
| **Cooperative Game (formal)** | G = (N, ν) where N = players, ν = characteristic function. |
| **Characteristic Function ν(C)** | Value a coalition C can obtain by working together. |
| **Coalition** | Any subset of players C ⊆ N. |
| **Grand Coalition** | Set of all players N. |
| **Coalition Structure** | A partition of N into coalitions. |
| **Payoff Vector** | x = (x₁, ..., xₙ) where xᵢ = value to player i. |
| **Superadditivity** | ν(C ∪ D) ≥ ν(C) + ν(D) for all C, D ⊆ N. |
| **Imputation** | Payoff vector Σ xᵢ = ν(N) and xᵢ ≥ ν({i}) for all i (individual rationality). |
| **Individual Rationality** | Each player at least as well off as working alone: xᵢ ≥ ν({i}). |
| **Core** | Set of imputations x where x(C) ≥ ν(C) for all C ⊂ N (no coalition can do better alone). |
| **Shapley Value** | φᵢ(G) = (1/n!) Σ_{p∈P} mcᵢ(pᵢ) where pᵢ = players preceding i in ordering p; average marginal contribution over all orderings. |
| **Marginal Contribution** | mcᵢ(C) = ν(C ∪ {i}) - ν(C). |
| **Dummy Player** | Player who never adds value: mcᵢ(C) = 0 for all C. |
| **Symmetric Players** | mcᵢ(C) = mcⱼ(C) for all C; should receive same payoff. |
| **Marginal Contribution Net (MC-Net)** | Represents cooperative game as set of rules (Cᵢ, xᵢ); ν(C) = Σ{xᵢ | (Cᵢ,xᵢ) ∈ R and Cᵢ ⊆ C}. |
| **Coalition Structure Graph** | Graph organizing coalition structures by number of coalitions; upward edges = division of a coalition. |
| **Set Partitioning Problem** | Finding socially optimal coalition structure (NP-hard). |
| **Mechanism** | Language for strategies + center + outcome rule. |
| **Center** | Distinguished agent collecting reports and determining payoffs. |
| **Contract Net Protocol** | Task allocation: problem recognition → task announcement → bidding → awarding. |
| **Manager** | Agent advertising a task in contract net. |
| **Bid** | Response to task announcement indicating capability and desire. |
| **Auction** | Mechanism for allocating scarce resources. |
| **Bidder** | Agent with utility vᵢ for an item. |
| **Ascending-Bid / English Auction** | Center starts at reserve price, raises incrementally; last bidder wins at bid price. |
| **Efficient Auction** | Goods go to agent who values them most. |
| **Collusion** | Unfair agreement to manipulate prices. |
| **Strategy-Proof Mechanism** | Agents have a dominant strategy. |
| **Truth-Revealing / Truthful / Incentive Compatible** | Dominant strategy involves revealing true value vᵢ. |
| **Revelation Principle** | Any mechanism can be transformed into equivalent truth-revealing mechanism. |
| **Sealed-Bid Auction** | Each bidder makes single bid unseen by others. |
| **Vickrey Auction / Sealed-Bid Second-Price** | Winner pays second-highest bid; truth-revealing (dominant strategy = bid vᵢ). |
| **Revenue Equivalence Theorem** | Any private-value auction mechanism yields same expected revenue. |
| **Tragedy of the Commons** | Shared resource exploited to lower total utility; similar to prisoner's dilemma. |
| **Externalities** | Effects on global utility not recognized in individual agents' transactions. |
| **VCG Mechanism (Vickrey-Clarke-Groves)** | Truth-revealing mechanism maximizing global utility; winners pay tax equal to loss their presence caused to losers. |
| **Social Choice Theory** | Study of voting procedures for aggregating preferences. |
| **Social Welfare Function** | Combines individual preferences into social preference order. |
| **Social Outcome** | Most preferred outcome by group as a whole. |
| **Social Choice Function** | Takes preference orders and outputs set of winners. |
| **Condorcet's Paradox** | Majority preferences can be cyclic: ωₐ ≻ ω_b ≻ ω_c ≻ ω_a. |
| **Condorcet Winner** | Candidate that beats every other in pairwise election. |
| **Arrow's Theorem** | No social welfare function for ≥3 outcomes satisfies all: Pareto, Condorcet winner, IIA, No dictatorship. |
| **Gibbard-Satterthwaite Theorem** | Any reasonable social choice function with >2 outcomes is either manipulable or a dictatorship. |
| **Borda Count** | Score k to top-ranked, k-1 to second, etc.; sum determines winner. |
| **Plurality Voting** | Each voter picks top choice; most votes wins. |
| **Approval Voting** | Voters submit approved subset; most approvals win. |
| **Instant Runoff Voting** | Eliminate lowest first-place votes iteratively until majority. |
| **True Majority Rule** | Candidate beats all others in pairwise comparisons. |
| **Alternating Offers Bargaining Model** | Agents take turns making offers; can accept or reject. |
| **Conflict Deal** | Outcome if negotiation never terminates. |
| **Negotiation Set** | Space of possible deals (e.g., {(x, 1-x): 0 ≤ x ≤ 1} for pie division). |
| **Ultimatum Game** | Single round: A₁ proposes, A₂ accepts or conflict. First mover has all power. |
| **Task-Oriented Domain** | Set of tasks initially allocated; agents negotiate to reallocate. |
| **Monotonic Concession Protocol** | Simultaneous proposals each round; agreement if one matches/exceeds other; concession or conflict. |
| **Zeuthen Strategy** | Concession based on willingness to risk conflict: riskᵢ = (utility lost by conceding) / (utility lost by causing conflict). |

## 2. Processes/Algorithms

### Joint Plan Construction
- Define action schemas with CONCURRENT constraints
- For concurrent exclusion: `∀b b≠actor ⇒ ¬Hit(b, Ball)`
- For concurrent requirement: `∃b b≠actor ∧ Carry(b, cooler, here, there)`
- Adapt existing planning algorithms with minor modifications

### Computing Nash Equilibria (Pure Strategies)
1. **Exhaustive search**: Iterate through each possible strategy profile; check for beneficial deviations. Complexity: mⁿ (infeasible for large n).
2. **Myopic best response** (iterated best response): Start random; flip suboptimal choices; repeat until convergence.

### Computing Mixed-Strategy Equilibria (Zero-Sum)
1. **Maximin technique** (von Neumann):
   - Let first player choose mixed strategy [p₁: a₁; ...; pₙ: aₙ]
   - Second player responds with pure strategy (since linear combination ≤ best pure)
   - Find intersection point of payoff lines
   - Solve linear programming problem

### Backward Induction (Extensive Form)
```
For each nonterminal state s (bottom-up from terminal states):
    if all children of s labeled with payoff profiles:
        label s with payoff profile from child maximizing
        the payoff of the player who moves at s
        (if chance node: compute expected utility)
```
Guaranteed to terminate; runs in polynomial time in tree size.

### Computing Subgame Perfect Equilibrium
- Same as backward induction
- Strategies computed are subgame perfect Nash equilibria

### Sequence Form for Extensive Games
- Represent paths (not strategies); linear in tree size
- Solve with linear programming
- Applied to poker: 25,000 states solvable in minutes (Koller et al., 1996)
- Abstraction further reduces 10¹⁸ states to ~10⁷

### Contract Net Protocol Phases
1. **Problem recognition**: Agent identifies need for cooperative action
2. **Task announcement**: Advertise task to other agents with sufficient info
3. **Bidding**: Recipients evaluate and submit bids indicating capabilities
4. **Awarding**: Manager selects best agent(s), sends award message

### VCG Mechanism
1. Center asks each agent to report value vᵢ
2. Allocate goods to winners W to maximize Σ_{i∈W} vᵢ
3. For each winner, calculate loss their presence caused to losers (who could have gotten vⱼ)
4. Each winner pays tax equal to this loss

### Shapley Value Computation
```
φᵢ(G) = (1/n!) Σ_{p∈P} mcᵢ(pᵢ)                                 (18.1)
```
where pᵢ = set of players preceding i in ordering p.

### MC-Net Shapley Value
```
φᵢ(R) = Σ_{(C,x)∈R} [x/|C| if i∈C, 0 otherwise]
```

### Zeuthen Strategy for Bargaining
1. First proposal: maximize own utility in negotiation set
2. Risk calculation: riskᵢ = (U_i(conceding) - U_i(conflict)) / (U_i(not conceding) - U_i(conflict))
3. Agent with smaller risk should concede
4. Concede just enough to shift risk balance to other agent
5. If equal risk, flip coin to decide who concedes

## 3. Hierarchies/Classifications

### Multiagent Environment Types
```
Single Decision Maker
├── Multieffector (one agent, multiple effectors)
├── Multibody (detached units, pooled sensor info)
└── Decentralized (centralized planning, decoupled execution)
Multiple Decision Makers
├── Common Goal (coordination problem)
└── Personal Preferences (game theory)
    ├── Cooperative (binding agreements)
    └── Non-cooperative (no binding agreements)
```

### Concurrent Action Models
| Model | Description | Pros | Cons |
|-------|-------------|------|------|
| Interleaved | Actions atomic; order within plans preserved | Simple, CPU model | Exponential interleavings, no true simultaneity |
| True Concurrency | Partially ordered actions | Theoretically satisfying | Less adopted in practice |
| Synchronous | Global clock, lockstep | Simple semantics | Unrealistic |

### Game Theory in AI
1. **Agent Design**: Analyze possible decisions assuming rational counterparts
2. **Mechanism Design**: Define rules so collective good is maximized under individual optimization

### Solution Concept Hierarchy
| Concept | Strength | Guaranteed? | Complexity |
|---------|----------|-------------|------------|
| Dominant Strategy Equilibrium | Strongest | Rare | Check each strategy |
| Nash Equilibrium (pure) | Medium | Not always (e.g., matching pennies) | mⁿ exhaustive |
| Nash Equilibrium (mixed) | Weakest | Always (Nash's theorem) | Via LP (zero-sum) |

### Cooperative Game Solution Concepts
| Concept | Purpose | Property |
|---------|---------|----------|
| Core | Stability of grand coalition | May be empty |
| Shapley Value | Fair distribution | Unique, axiomatic |
| Imputation | Individual rationality | Condition for core |
| Marginal Contribution | Player's added value | Basis for Shapley value |

### Voting Procedures
| Method | Description | Issue |
|--------|-------------|-------|
| Simple majority | Two candidates; most votes wins | Only for 2 candidates |
| Plurality | Top choice wins | Ignores lower preferences |
| Borda count | Rank all; weighted scores | Voters must rank all |
| Approval voting | Approve subset; most approvals | Binary approval |
| Instant runoff | Eliminate lowest iteratively | Complex process |
| True majority rule | Pairwise comparisons | May have no winner |

## 4. Comparisons/Trade-offs

| Aspect | Decision Theory | Game Theory |
|--------|----------------|-------------|
| Agents | Single | Multiple |
| Environment | Nature (stochastic) | Other strategic agents |
| Optimization | Maximize EU given P(states) | Nash equilibrium / best response |
| Key concept | MEU | Nash equilibrium |

| Aspect | Normal Form | Extensive Form |
|--------|-------------|----------------|
| Timing | Simultaneous moves | Sequential moves |
| Representation | Payoff matrix | Game tree |
| Perfect info | Assumed | Can represent imperfect info |
| Solution | Mixed strategies via LP | Backward induction / sequence form |

| Aspect | Cooperative | Non-Cooperative |
|--------|-------------|-----------------|
| Agreements | Binding possible | Not possible |
| Focus | Coalition formation, fair division | Strategic interaction |
| Solution | Core, Shapley value | Nash equilibrium |
| Key paper | von Neumann & Morgenstern (1944) | Nash (1950) |

## 5. Formulas & Equations

### Shapley Value
```
φᵢ(G) = (1/n!) Σ_{p∈P} mcᵢ(pᵢ)                                 (18.1)
```

### Marginal Contribution
```
mcᵢ(C) = ν(C ∪ {i}) - ν(C)
```

### Core Inequalities
```
xᵢ ≥ ν({i}) for all i ∈ N
Σ_{i∈N} xᵢ = ν(N)
Σ_{i∈C} xᵢ ≥ ν(C) for all C ⊆ N
```

### MC-Net Characteristic Function
```
ν(C) = Σ{xᵢ | (Cᵢ, xᵢ) ∈ R and Cᵢ ⊆ C}
```

### Social Welfare of Coalition Structure
```
sw(CS) = Σ_{C∈CS} ν(C)
```

### Negotiation Outcome (Alternating Offers, Infinite Horizon)
```
A₁ gets: (1 - γ₂) / (1 - γ₁γ₂)
A₂ gets: remainder
```

### Utility in Task-Oriented Domain
```
Uᵢ((T₁,T₂)) = c(Tᵢ) - c(Tᵢ⁰)
```

### Zeuthen Risk
```
riskᵢ = (Uᵢ(conceding) - Uᵢ(conflict)) / (Uᵢ(not conceding) - Uᵢ(conflict))
```

### Vickrey Auction Utility
```
Uᵢ = { (vᵢ - bₒ) if bᵢ > bₒ, 0 otherwise }
```

## 6. Rules, Laws & Theorems

- **Nash's Theorem** (1950): Every game has at least one Nash equilibrium in mixed strategies.
- **von Neumann's Theorem** (1928): Every two-player zero-sum game has a maximin equilibrium in mixed strategies.
- **Nash Folk Theorems**: Every outcome where each player receives at least their security value can be sustained as Nash equilibrium in infinitely repeated game (via GRIM strategies).
- **Arrow's Theorem**: No social welfare function for ≥3 outcomes can satisfy all: Pareto condition, Condorcet winner condition, IIA, and no dictatorship simultaneously.
- **Gibbard-Satterthwaite Theorem**: Any "reasonable" social choice function with >2 outcomes is either manipulable or a dictatorship.
- **Revelation Principle**: Any mechanism can be transformed into an equivalent truth-revealing mechanism.
- **Revenue Equivalence Theorem**: Private-value auction mechanisms yield the same expected revenue.
- **Shapley Value Axioms**: Efficiency, Dummy Player, Symmetry, Additivity → unique fair distribution.
- **Superadditivity**: ν(C ∪ D) ≥ ν(C) + ν(D) for all C, D ⊆ N.
- **Pareto Optimality**: No player can be made better off without making another worse off.

## 10. Empirical Evidence

- **Poker solving**: Sequence form solves 25,000-state variants (Koller et al., 1996); abstraction → 10¹⁷→10⁷ states
- **Libratus & DeepStack**: Defeated human champions at heads-up Texas hold 'em
- **Pluribus**: Defeated human champions at 6-player poker; 50 choose 10 ≈ 10 billion opponent card possibilities
- **German spectrum auction (1999)**: Two bidders used 10% raise rule to signal collusion; government got less than expected
- **Internet ad auctions**: Trillions of Vickrey-style auctions per year; $100B/year in goods

## 11. Cross-Chapter Dependencies

- Ch 5: Minimax, game trees, utility in games → zero-sum games, expectimax for chance nodes
- Ch 16: Utility theory, decision networks → payoff functions, expected utility in games
- Ch 17: MDPs, POMDPs → Markov games, assistance games as POMDPs
- Ch 22: Reinforcement learning → multiagent RL, Markov games
- Ch 4: Belief states → information sets
- Ch 9: Logic programming, STRIPS → joint plans with concurrent action constraints
- Ch 1: Provably beneficial AI → assistance games

## 12. Dates & People

- **John von Neumann** (1928, 1944): Maximin equilibrium for zero-sum games; Theory of Games and Economic Behavior (with Morgenstern)
- **John Forbes Nash, Jr.** (1950): Nash equilibrium (Nobel 1994); BSPs (1973)
- **Kenneth Arrow** (1951): Arrow's impossibility theorem (Nobel 1972)
- **Lloyd Shapley** (1953a): Shapley value (Nobel 2012)
- **Reinhard Selten**: Subgame perfect equilibrium (Nobel 1994)
- **John Harsanyi**: Bayes-Nash equilibrium (Nobel 1994)
- **William Vickrey** (1961): Vickrey auction (Nobel 1996)
- **Vilfredo Pareto** (1848-1923): Pareto optimality
- **Marquis de Condorcet** (1743-1794): Condorcet's paradox
- **Jean-Charles de Borda**: Borda count
- **Zermelo** (1913): First formal game theory results
- **Emile Borel** (1921): Mixed strategies
- **Lloyd Shapley** (1953a): Shapley value
- **Donald Gillies** (1959): Core
- **Koller et al.** (1996): Sequence form
- **Smith** (1980): Contract net protocol
- **Reid Smith**: Contract net protocol (PhD, late 1970s)
- **Myerson** (1981, 1986): Revelation principle, revenue equivalence (Nobel 2007)
- **Rubinstein** (1982): Alternating offers bargaining
- **Rosenschein & Zlotkin** (1994): Monotonic concession protocol
- **Hadfield-Menell et al.** (2017a): Assistance games / cooperative inverse reinforcement learning

## 16. Ethics

- **Value alignment**: Machines must operate under uncertainty about human's true objectives
- **Off-switch problem**: Robot with uncertainty about human preferences will defer and allow itself to be switched off; proof that EU(defer) ≥ EU(act)
- **Assistance games**: Formal model of provably beneficial AI; Harriet and Robbie both maximize Harriet's payoff
- **Paperclip game**: Harriet signals preferences via production; Robbie interprets and acts; language emerges from equilibrium analysis
- **Tragedy of the commons**: Without mechanism design, shared resources exploited; need to make externalities explicit

## 18. End-of-Chapter Summary

- Multiagent planning requires joint plans with coordination mechanisms (conventions, communication, plan recognition)
- Game theory is to multiagent decision making as decision theory is to single-agent decision making
- Non-cooperative: Nash equilibrium is the most important solution concept
- Cooperative: Core (stability) and Shapley value (fairness)
- Specialized techniques: contract net (task sharing), auctions (resource allocation), bargaining (agreements), voting (preference aggregation)
