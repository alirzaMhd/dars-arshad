# Study Guide: Artificial Intelligence — A Modern Approach (Ch 12–14)

> Generated 2026-06-03. Subject: AI / Probabilistic Reasoning. Coverage: comprehensive.

---

## Ch. 12 — Quantifying Uncertainty

### Named Entities (Terms & Definitions)

- **Uncertainty**: arises from partial observability, nondeterminism, or adversaries; agent may never know for sure its current state or future outcomes.
- **Belief state**: representation of the set of all possible world states the agent might be in.
- **Qualification problem**: cannot deduce for sure that a plan succeeds because an almost unlimited list of qualifiers (car breaks down, accident, road closed, meteorite, etc.) can never be fully enumerated.
- **Degree of belief**: numerical measure between 0 (certainly false) and 1 (certainly true) of confidence in a sentence.
- **Probability theory**: main tool for dealing with degrees of belief; ontological commitment same as logic (facts that do or don't hold), but epistemological commitment allows numerical degrees.
- **Laziness**: too much work to list complete set of antecedents/consequents for exceptionless rules.
- **Theoretical ignorance**: medical science (and most domains) has no complete theory.
- **Practical ignorance**: even if rules known, might be uncertain about a particular case because not all tests can be run.
- **Preference**: agent's ordering among possible outcomes.
- **Outcome**: a completely specified state, including all relevant factors.
- **Utility theory**: represents preferences and reasons quantitatively with them; every state has a degree of usefulness (utility) to an agent.
- **Decision theory**: Decision theory = Probability theory + Utility theory.
- **Principle of Maximum Expected Utility (MEU)**: an agent is rational iff it chooses the action that yields the highest expected utility, averaged over all possible outcomes.
- **Sample space (Ω)**: the set of all possible worlds; mutually exclusive and exhaustive.
- **Probability model**: associates a numerical probability P(ω) with each possible world.
- **Event**: a set of possible worlds (in logic, corresponds to a proposition).
- **Unconditional (prior) probability**: degree of belief in a proposition in the absence of any other information; also called "priors."
- **Conditional (posterior) probability**: degree of belief given some evidence that has been revealed.
- **Random variable**: a function mapping from the domain of possible worlds Ω to some range; names begin with uppercase letter.
- **Range**: the set of possible values a random variable can take on.
- **Bernoulli distribution**: a Boolean random variable with range {0,1}.
- **Categorical distribution**: a probability distribution for a finite, discrete range.
- **Probability distribution**: assignment of a probability for each possible value of a random variable.
- **Probability density function (pdf)**: for continuous variables, a parameterized function defining probability that a variable takes on some value x; probabilities are unitless, densities have units (e.g., reciprocal degrees).
- **Joint probability distribution**: distribution on multiple variables; e.g., P(Weather,Cavity) is a 4×2 table.
- **Full joint probability distribution**: the joint distribution over all random variables in the domain.
- **Inclusion–exclusion principle**: P(a ∨ b) = P(a) + P(b) − P(a ∧ b).
- **Kolmogorov's axioms**: the axioms of probability (0 ≤ P(ω) ≤ 1, ∑P(ω)=1, and inclusion-exclusion).
- **Marginal probability**: obtained by summing out other variables from the joint distribution.
- **Marginalization (summing out)**: summing up probabilities for each possible value of other variables, thereby taking them out of the equation.
- **Conditioning**: using P(Y) = ∑_z P(Y|z)P(z).
- **Normalization constant (α)**: ensures conditional probabilities sum to 1.
- **Independence (absolute/marginal independence)**: P(a|b) = P(a) or P(a∧b) = P(a)P(b).
- **Bayes' rule (Bayes' law/Bayes' theorem)**: P(b|a) = P(a|b)P(b)/P(a).
- **Causal direction**: P(effect|cause); robust to changes in prior of cause.
- **Diagnostic direction**: P(cause|effect); fragile — changes when prior of cause changes.
- **Conditional independence**: P(X,Y|Z) = P(X|Z)P(Y|Z); X and Y are independent given Z.
- **Separation**: a variable Cavity separates Toothache and Catch when it is a direct cause of both.
- **Naive Bayes model**: P(Cause,Effect_1,...,Effect_n) = P(Cause)∏_i P(Effect_i|Cause); "naive" because assumes conditional independence of all effects given cause.
- **Text classification**: using naive Bayes to categorize documents based on word presence.
- **Frequentist**: probability comes only from experiments; fraction observed in limit of infinite samples.
- **Objectivist**: probabilities are real aspects of the universe (propensities).
- **Subjectivist**: probabilities characterize an agent's beliefs, not external physical significance.
- **Reference class problem**: to determine outcome probability, must place event in a reference class of "similar" experiments; but every event is unique.
- **Principle of indifference** (Principle of insufficient reason): assign equal probabilities when no knowledge distinguishes cases.

### Processes / Algorithms

#### Decision-Theoretic Agent
- **Type**: Algorithm
- **Goal**: select rational actions using decision theory
- **Steps**:
  1. Maintain belief state: probabilistic beliefs about current state of world
  2. Update belief state based on action and percept
  3. Calculate outcome probabilities for actions, given action descriptions and current belief state
  4. Select action with highest expected utility given probabilities of outcomes and utility information
  5. Return action
- **Input**: percept
- **Output**: action

#### Probabilistic Inference Using Full Joint Distribution
- **Type**: Algorithm (conceptual)
- **Goal**: compute P(X|e) from full joint distribution
- **Steps**:
  1. Identify query variable X, evidence variables E with observed values e, and unobserved variables Y
  2. Compute P(X|e) = α ∑_y P(X,e,y)
  3. Normalize by α = 1/P(e)
- **Complexity**: O(2^n) for n Boolean variables — impractical.

#### Applying Bayes' Rule with Normalization
- **Type**: Algorithm
- **Steps**:
  1. Write P(Y|X) = α P(X|Y) P(Y)
  2. Compute for each value y_i: P(X|y_i) × P(y_i)
  3. Normalize so entries sum to 1
- **Note**: avoids computing P(X) directly.

### Classifications & Hierarchies

- **Probabilistic vs Logical Agent**:
  | Dimension | Logical Agent | Probabilistic Agent |
  |---|---|---|
  | Belief | true/false or no opinion | numerical degree of belief 0–1 |
  | Ontology | facts holding or not | facts holding or not (same) |
  | Epistemology | binary | continuous [0,1] |
- **Prior vs Posterior**:
  | Prior | Posterior |
  |---|---|
  | No evidence | Given evidence |
  | Unconditional | Conditional |
- **Causal vs Diagnostic Knowledge**:
  | Causal (model-based) | Diagnostic |
  |---|---|
  | P(effect|cause) | P(cause|effect) |
  | Robust to change in priors | Fragile |
  | Easier for experts to provide | Harder to provide |
- **Frequentist vs Subjectivist vs Objectivist**: three interpretations of probability.

### Comparisons & Trade-offs

| Approach | Pros | Cons |
|---|---|---|
| Full joint distribution | Complete, theoretically sound | O(2^n) size, astronomical data required |
| Bayes' rule with causal knowledge | Robust, requires fewer numbers | Needs conditional probabilities in causal direction |
| Naive Bayes | Linear in #effects, often works well | Overconfident, assumes independence that may not hold |
| Logical (contingent) planning | Guaranteed if possible | Can't handle uncertainty; qualification problem |

### Formulas & Equations

#### Probability Axioms
`0 ≤ P(ω) ≤ 1 for every ω and ∑_{ω∈Ω} P(ω) = 1` (12.1)
- ω = possible world
- Ω = sample space (set of all possible worlds)

#### Probability of a Proposition
`P(φ) = ∑_{ω∈φ} P(ω)` (12.2)
- φ = proposition (set of possible worlds)

#### Conditional Probability
`P(a|b) = P(a∧b) / P(b)` for P(b) > 0 (12.3)
- a, b = propositions
- P(b) must be > 0

#### Product Rule
`P(a∧b) = P(a|b) P(b)` (12.4)

#### Inclusion–Exclusion (Disjunction)
`P(a∨b) = P(a) + P(b) − P(a∧b)` (12.5)

#### Marginalization
`P(Y) = ∑_z P(Y, Z=z)` (12.7)
- Y, Z = sets of random variables
- Sum over all combinations of values of Z

#### Conditioning
`P(Y) = ∑_z P(Y|z) P(z)` (12.8)

#### Bayes' Rule
`P(b|a) = P(a|b) P(b) / P(a)` (12.12)
- P(b|a) = posterior of b given a
- P(a|b) = likelihood of a given b
- P(b) = prior of b
- P(a) = evidence probability (can be normalized away)

#### Bayes' Rule with Background Evidence
`P(Y|X,e) = P(X|Y,e) P(Y|e) / P(X|e)` (12.13)

#### Bayes' Rule with Normalization
`P(Y|X) = α P(X|Y) P(Y)` (12.15)
- α = normalization constant = 1/P(X)

#### Naive Bayes Model
`P(Cause, Effect_1, ..., Effect_n) = P(Cause) ∏_i P(Effect_i | Cause)` (12.20)

#### Naive Bayes Inference
`P(Cause|e) = α P(Cause) ∏_j P(e_j | Cause)` (12.21)
- e = observed effects
- Unobserved effects disappear (sum to 1)

#### General Inference from Full Joint Distribution
`P(X|e) = α P(X, e) = α ∑_y P(X, e, y)` (12.9)
- X = query variable
- E = evidence variables, e = observed values
- Y = remaining unobserved variables
- α = 1/P(e)

### Rules, Laws & Theorems

##### Kolmogorov's Axioms (12.1, 12.5)
- **Statement**: (1) 0 ≤ P(ω) ≤ 1 for all ω ∈ Ω; (2) ∑_{ω∈Ω} P(ω) = 1; (3) P(a∨b) = P(a) + P(b) − P(a∧b)
- **Implications**: All of probability theory derives from these.
- **Proof sketch (de Finetti)**: If an agent violates these axioms, there exists a set of bets guaranteeing loss (Dutch book), so no rational agent can violate them.

##### Bayes' Rule (12.12)
- **Statement**: P(b|a) = P(a|b)P(b) / P(a)
- **Derivation**: From product rule P(a∧b) = P(a|b)P(b) = P(b|a)P(a); equate and divide by P(a).
- **Key insight**: Allows computing diagnostic probability from causal knowledge.
- **Why useful**: Causal knowledge (P(effect|cause)) is more robust and easier to obtain than diagnostic knowledge.

##### Chain Rule
- **Statement**: P(x_1, ..., x_n) = P(x_n|x_{n-1},...,x_1) P(x_{n-1}|x_{n-2},...,x_1) ... P(x_2|x_1) P(x_1) = ∏_{i=1}^n P(x_i|x_{i-1},...,x_1)
- **Holds for**: any set of random variables, in any order.

### Edge Cases & Common Pitfalls

- **Zero evidence probability**: P(b) must be > 0 for conditional probability definition.
- **Conditioning vs logical implication**: P(cavity|toothache)=0.6 does NOT mean "whenever toothache, conclude cavity with prob 0.6" — it means "when toothache and no further info."
- **Zero probability for unseen words in naive Bayes**: Must reserve probability for previously unseen words, else zero wipes out all other evidence.
- **Normalization shortcut**: Can normalize without computing P(e) by computing relative proportions then dividing by sum.
- **Probability vs density**: P(NoonTemp=20.18°C) has probability 0 (single point in continuous distribution); densities have units.

### Case Studies & Examples

##### Meningitis Example
- **What**: Doctor knows meningitis causes stiff neck 70% of time; prior meningitis is 1/50,000; prior stiff neck is 1%.
- **Method**: Bayes' rule: P(m|s) = P(s|m)P(m)/P(s) = 0.7 × 1/50000 / 0.01 = 0.0014.
- **Result**: Only 0.14% of stiff neck patients have meningitis.
- **Significance**: Even with strong causal link, posterior is tiny because prior of stiff neck is much higher than prior of meningitis.
- **Exam angle**: Illustrates why diagnostic knowledge must be updated when priors change (epidemic raises P(m)).

##### Wumpus World Probabilistic Reasoning
- **What**: Agent in wumpus world with 0.2 prior probability of pit per square; observed breeze in [1,2] and [2,1]; query P(P_1,3|known,b).
- **Method**: Uses conditional independence to reduce from 2^12 terms to 4 terms (Frontier variables).
- **Result**: P([1,3] has pit) ≈ 0.31; P([2,2] has pit) ≈ 0.86.
- **Significance**: Probabilistic agent distinguishes squares where logical agent sees only "unknown."

### End-of-Chapter Material

**Key Terms**: uncertainty, degree of belief, probability theory, decision theory, MEU, sample space, event, prior probability, posterior probability, random variable, probability distribution, joint distribution, full joint distribution, marginalization, conditioning, independence, Bayes' rule, conditional independence, naive Bayes.

**Summary points**:
- Uncertainty arises from laziness and ignorance; inescapable in complex/nondeterministic/partially observable environments.
- Probabilities express agent's inability to reach definite decision; summarize beliefs relative to evidence.
- Decision theory = probability theory + utility theory; best action maximizes expected utility.
- Axioms of probability constrain logically related propositions; violation leads to irrational behavior.
- Full joint distribution is theoretical foundation but impractical due to exponential size.
- Absolute independence allows factoring into smaller distributions.
- Bayes' rule computes unknown probabilities from known causal conditional probabilities.
- Conditional independence (via direct causal relationships) allows factoring into smaller conditional distributions.
- Naive Bayes assumes conditional independence of all effects given a single cause.

---

## Ch. 13 — Probabilistic Reasoning

### Named Entities (Terms & Definitions)

- **Bayesian network (Bayes net, belief network)**: a directed acyclic graph where each node is annotated with quantitative probability information; each node has a conditional distribution given its parents.
- **Causal network**: a Bayes net with additional constraints on arrow meaning (causal direction).
- **Graphical model**: broader class including Bayesian networks and other graph-based probability models.
- **Conditional probability table (CPT)**: local probability information for a node in a Bayes net; each row gives conditional probability for each node value given a conditioning case.
- **Conditioning case**: a possible combination of values for the parent nodes.
- **Parameter**: the finite number of values quantifying the effect of parents on a node.
- **Topological ordering**: an ordering of nodes consistent with the directed graph structure (parents before children).
- **Chain rule**: P(x_1,...,x_n) = ∏ P(x_i|x_{i-1},...,x_1) — holds for any set of random variables.
- **Locally structured (sparse) system**: each subcomponent interacts directly with only a bounded number of other components.
- **Descendant**: in a Bayes net, a node reachable by following arrows forward.
- **Markov blanket**: parents, children, and children's parents of a node; d-separates the node from all other nodes.
- **D-separation**: determines whether sets X and Y are conditionally independent given Z in a Bayes net; Z blocks all paths in the moralized ancestral subgraph.
- **Ancestral subgraph**: subgraph consisting of X, Y, Z, and their ancestors.
- **Moral graph**: add links between unlinked pairs sharing a common child, then make all links undirected.
- **Canonical distribution**: a standard pattern for conditional distributions (e.g., deterministic, noisy-OR, linear-Gaussian).
- **Deterministic nodes**: value specified exactly by parents with no uncertainty.
- **Context-specific independence (CSI)**: a variable is conditionally independent of some parents given certain values of others.
- **Noisy-OR**: generalization of logical OR; allows uncertainty about ability of each parent to cause child to be true; each parent may be inhibited.
- **Leak node**: in noisy-OR, captures "miscellaneous causes" not explicitly listed as parents.
- **Discretization**: dividing continuous variables into fixed intervals.
- **Nonparametric representation**: defining conditional distribution implicitly with collection of instances.
- **Hybrid Bayesian network**: network with both discrete and continuous variables.
- **Linear–Gaussian distribution**: child has Gaussian distribution whose mean varies linearly with parent value; P(c|h) = N(c; ah+b, σ²).
- **Conditional Gaussian (CG) distribution**: given any assignment to discrete variables, distribution over continuous variables is multivariate Gaussian.
- **Probit model**: P(buys|Cost=c) = 1 − Φ((c−μ)/σ); soft threshold function using integral of standard normal.
- **Expit (inverse logit) model**: uses logistic function 1/(1+e^{−x}) for soft threshold.
- **Logistic function**: 1/(1+e^{−x}); maps any x to (0,1).
- **Hidden variable**: a variable in a Bayes net that is neither input nor output but essential for sparsity.
- **Query variables**: variables whose posterior distribution we want.
- **Evidence variables**: variables with observed values.
- **Hidden (nonevidence, nonquery) variables**: Y in typical query formulation.
- **Event**: assignment of values to a set of evidence variables (in inference context).
- **Factor**: a matrix indexed by the values of its argument variables; used in variable elimination.
- **Pointwise product**: operation on factors yielding new factor with union of variables; h(X,Y,Z) = f(X,Y) × g(Y,Z).
- **Variable elimination**: exact inference algorithm that sums out variables from pointwise products of factors.
- **Singly connected network (polytree)**: at most one undirected path between any two nodes.
- **Multiply connected network**: network with more than one undirected path between nodes.
- **Reduction**: converting one problem (SAT) to another (Bayes net inference) to prove hardness.
- **Weighted model counting (WMC)**: sums total weight of satisfying assignments for a SAT expression; used for Bayes net inference.
- **Tree width**: bounds complexity of solving CSPs and Bayes nets.
- **Clustering algorithms (join tree algorithms)**: join nodes to form cluster nodes, creating a polytree; used for computing posteriors for all variables in O(n).
- **Meganode**: a node formed by clustering individual nodes, taking on all tuple values.
- **Monte Carlo algorithms**: randomized sampling algorithms for approximate inference.
- **Rejection sampling**: generate samples from prior, reject those inconsistent with evidence.
- **Consistent estimate**: estimated probability becomes exact in large-sample limit.
- **Importance sampling**: sample from distribution Q instead of P, apply correction factor (weight) P(x)/Q(x).
- **Likelihood weighting**: importance sampling for Bayes nets; fix evidence variables, sample nonevidence variables in topological order, weight = product of likelihoods of evidence given parents.
- **Markov chain Monte Carlo (MCMC)**: generate each sample by making random change to preceding sample.
- **Gibbs sampling**: MCMC algorithm for Bayes nets; sample each nonevidence variable conditioned on its Markov blanket.
- **Metropolis–Hastings (MH)**: general MCMC algorithm; propose new state from proposal distribution q(x'|x), accept with probability a(x'|x).
- **Proposal distribution**: q(x'|x) — distribution from which candidate next state is sampled.
- **Acceptance probability**: a(x'|x) = min(1, π(x')q(x|x')/(π(x)q(x'|x))).
- **Markov chain**: random process generating a sequence of states.
- **Transition kernel**: k(x→x') — probability of transition from state x to x'.
- **Stationary distribution**: π(x) — distribution that remains unchanged under the transition kernel; π(x') = ∑_x π(x) k(x→x').
- **Ergodic**: every state reachable from every other, no strictly periodic cycles.
- **Detailed balance**: π(x)k(x→x') = π(x')k(x'→x) for all x,x'.
- **Mixing rate**: how quickly Markov chain converges to stationary distribution.
- **Block sampling**: sampling multiple variables simultaneously to improve MCMC mixing.
- **Compiling approximate inference**: compiling Bayes net into model-specific inference code (2–3 orders faster).
- **Structural equation**: equation x_i = f_i(···) describing a stable causal mechanism invariant to local changes.
- **Do-calculus**: notation do(X_j = x_jk) for intervening to set a variable.
- **Adjustment formula**: P(X_i = x_i|do(X_j = x_jk)) = ∑_{parents(X_j)} P(x_i|x_jk, parents(X_j)) P(parents(X_j)).
- **Back-door criterion**: set Z that closes all back-door paths from X_j to X_i, allowing adjustment formula.
- **Unmodeled variables (error terms, disturbances)**: U-variables in structural equations representing exogenous noise.
- **Randomized controlled trial**: gold standard for causal inference; back-door criterion sometimes allows causal conclusions from observational data.

### Processes / Algorithms

#### Constructing a Bayesian Network
- **Type**: Algorithm (methodology)
- **Steps**:
  1. **Nodes**: Determine the set of variables required to model the domain. Order them {X_1,...,X_n} such that causes precede effects (for compactness).
  2. **Links**: For i = 1 to n:
     a. Choose a minimal set of parents for X_i from X_1,...,X_{i-1} such that P(X_i|X_{i-1},...,X_1) = P(X_i|Parents(X_i))
     b. Insert a link from each parent to X_i
  3. **CPTs**: Write down P(X_i|Parents(X_i)) for each node
- **Property**: No redundant probability values; impossible to create a Bayes net that violates axioms of probability.
- **Property**: Any ordering works but causal ordering yields more compact network.

#### Inference by Enumeration (ENUMERATION-ASK)
- **Type**: Algorithm (exact inference)
- **Goal**: Compute P(X|e) from Bayes net
- **Steps**:
  1. For each value x_i of X: Q(x_i) ← ENUMERATE-ALL(vars, e extended with X=x_i)
  2. Return NORMALIZE(Q(X))
- **ENUMERATE-ALL**(vars, e):
  1. If EMPTY?(vars), return 1.0
  2. V ← FIRST(vars)
  3. If V is evidence variable: return P(v|parents(V)) × ENUMERATE-ALL(REST(vars), e)
  4. Else: return ∑_v P(v|parents(V)) × ENUMERATE-ALL(REST(vars), e extended with V=v)
- **Complexity**: O(2^n) time, O(n) space (linear space)
- **Trick**: Move summations inward to reduce complexity.

#### Variable Elimination Algorithm
- **Type**: Algorithm (exact inference)
- **Goal**: Compute P(X|e) by eliminating repeated calculations
- **Input**: X (query), e (evidence), bn (Bayes net)
- **Steps**:
  1. factors ← []
  2. For each V in ORDER(vars):
     a. factors ← [MAKE-FACTOR(V, e)] + factors
     b. If V is hidden variable: factors ← SUM-OUT(V, factors)
  3. Return NORMALIZE(POINTWISE-PRODUCT(factors))
- **Key operations**:
  - **Pointwise product** f×g: new factor h with union of variables; h(···) = f(···) × g(···)
  - **Summing out**: ∑_x h(X,Y,Z) = h(x,Y,Z) + h(¬x,Y,Z); factors not depending on the summed variable can be moved outside
- **Optimization**: Remove irrelevant variables — leaf nodes that are not query or evidence variables can be removed; then any node that is not ancestor of query or evidence is irrelevant.
- **Complexity**: Linear in network size for polytrees; exponential for multiply connected networks.

#### Rejection Sampling
- **Type**: Algorithm (approximate inference)
- **Goal**: Estimate P(X|e)
- **Input**: X (query), e (evidence), bn, N (#samples)
- **Steps**:
  1. Initialize count vector C for each value of X to 0
  2. For j = 1 to N:
     a. x ← PRIOR-SAMPLE(bn)
     b. If x consistent with e: C[j] ← C[j] + 1
  3. Return NORMALIZE(C)
- **Complexity**: Depends on P(e) — fraction of accepted samples drops exponentially with #evidence variables.
- **Consistent**: converges to true probability as N → ∞.

#### Likelihood Weighting
- **Type**: Algorithm (approximate inference)
- **Goal**: Estimate P(X|e)
- **Input**: X (query), e (evidence), bn, N (#samples)
- **Steps**:
  1. Initialize weighted count vector W for each value of X to 0
  2. For j = 1 to N:
     a. (x, w) ← WEIGHTED-SAMPLE(bn, e)
     b. W[x_j] ← W[x_j] + w
  3. Return NORMALIZE(W)
- **WEIGHTED-SAMPLE**(bn, e):
  1. w ← 1; x ← event with values fixed from e
  2. For i = 1 to n:
     a. If X_i is evidence: w ← w × P(X_i = value | parents(X_i))
     b. Else: x[i] ← random sample from P(X_i | parents(X_i))
  3. Return (x, w)
- **Weight**: w = ∏_{evidence variables} P(e_i | parents(E_i)) — product of likelihoods of evidence
- **Complexity**: Much better than rejection; still degrades with many downstream evidence variables.

#### Gibbs Sampling
- **Type**: Algorithm (MCMC approximate inference)
- **Goal**: Estimate P(X|e)
- **Input**: X (query), e (evidence), bn, N (#samples)
- **Steps**:
  1. Initialize count vector C for each value of X
  2. Initialize current state x with random values for nonevidence variables Z, evidence fixed from e
  3. For k = 1 to N:
     a. Choose any variable Z_i from Z according to some distribution ρ(i)
     b. Set value of Z_i in x by sampling from P(Z_i | mb(Z_i))
     c. C[x_j] ← C[x_j] + 1
  4. Return NORMALIZE(C)
- **Markov blanket distribution**: P(x_i|mb(X_i)) = α P(x_i|parents(X_i)) ∏_{Y_j ∈ Children(X_i)} P(y_j|parents(Y_j))
- **Complexity**: Each step proportional to #children + range size of X_i — independent of network size.
- **Key property**: Stationary distribution = true posterior P(x|e).
- **Ergodicity requirement**: CPTs must not contain 0 or 1 probabilities.

#### Metropolis–Hastings Sampling
- **Type**: Algorithm (MCMC)
- **Goal**: Generate samples from target distribution π(x)
- **Steps** (per iteration):
  1. Sample x' from proposal distribution q(x'|x) given current state x
  2. Compute acceptance probability a(x'|x) = min(1, π(x')q(x|x')/(π(x)q(x'|x)))
  3. Accept x' with probability a(x'|x); if rejected, stay at x
- **Key property**: Converges to correct stationary distribution for any ergodic proposal distribution.
- **Useful trick**: π(x')/π(x) = P(x',e)/P(x,e) — full joint probabilities, many terms cancel for local changes.

#### Prior Sampling
- **Type**: Algorithm (basic building block)
- **Goal**: Generate sample from prior joint distribution of Bayes net
- **Steps**: For each variable X_i in topological order: sample x_i from P(X_i | parents(X_i))
- **Property**: S_PS(x_1,...,x_n) = P(x_1,...,x_n)

#### Compiling Approximate Inference
- **Type**: Algorithm optimization
- **Goal**: Speed up sampling by compiling Bayes net into model-specific code
- **Method**: Precompute Gibbs distributions for each variable given each combination of Markov blanket values; emit conditional code with precomputed thresholds.
- **Result**: 2–3 orders of magnitude faster.

### Classifications & Hierarchies

**Bayes Net Types by Connectivity**:
- **Singly connected (polytree)**: at most one undirected path between any two nodes; exact inference linear in network size.
- **Multiply connected**: multiple undirected paths; exact inference is NP-hard (exponential worst case).

**Inference Methods**:
| Exact | Approximate |
|---|---|
| Enumeration | Rejection sampling |
| Variable elimination | Likelihood weighting |
| Clustering (join tree) | Gibbs sampling |
| | Metropolis–Hastings |

**Conditional Distribution Types**:
- Full CPT: O(2^k) parameters for k parents
- Deterministic: exact function of parents (0 parameters beyond the function)
- Noisy-OR: O(k) parameters
- Linear–Gaussian: O(k) parameters (means linear in parents)
- Probit/Expit: O(k) parameters (weighted linear combination)
- Context-specific (CSI): if-then-else syntax

### Comparisons & Trade-offs

| Dimension | Exact Inference | Approximate Inference |
|---|---|---|
| Accuracy | Exact | Approximate (converges in limit) |
| Polytrees | Linear time | N/A |
| Multiply connected | Exponential (NP-hard) | Can be good approximation |
| Evidence amount | No inherent limitation | Degrades with more evidence |
| Deterministic CPTs | Handles naturally | Rejection/LW fine; Gibbs requires non-0/1 |

| Dimension | Rejection Sampling | Likelihood Weighting | Gibbs Sampling |
|---|---|---|---|
| Space | O(N) | O(N) | O(N) |
| Time per sample | O(n) | O(n) | O(range × #children) |
| Handles evidence | Poor (exponential rejection) | Better (but weight degrades) | Good (propagates) |
| Downstream evidence | Poor | Poor (hallucination) | Good |
| Deterministic CPTs | Fine | Fine | Can fail (non-ergodic) |

| Dimension | HMM | DBN | Kalman Filter |
|---|---|---|---|
| State variables | Single | Multiple | Continuous vector |
| State representation | Atomic | Factored | Gaussian |
| Complexity per step | O(S²) | O(n d^{n+k}) | O(n³) |
| Handles discrete | Yes | Yes | No (continuous only) |
| Handles nonlinear | Yes (with enough states) | Yes | No (linear–Gaussian required) |

### Formulas & Equations

#### Bayes Net Joint Distribution
`P(x_1, ..., x_n) = ∏_{i=1}^n θ(x_i | parents(X_i))` (13.1)
- θ(x_i|parents(X_i)) = local conditional distribution parameters

#### Bayes Net Joint Distribution (as conditional probabilities)
`P(x_1, ..., x_n) = ∏_{i=1}^n P(x_i | parents(X_i))` (13.2)
- Confirms that parameters equal conditional probabilities P(x_i|parents(X_i)).

#### Chain Rule for Bayes Nets
`P(x_1, ..., x_n) = ∏_{i=1}^n P(x_i | x_{i-1}, ..., x_1)` — holds for any ordering.

#### Conditional Independence in Bayes Nets
`P(X_i | X_{i-1}, ..., X_1) = P(X_i | Parents(X_i))` (13.3)
- Provided Parents(X_i) ⊆ {X_{i-1}, ..., X_1} (topological ordering).

#### Markov Blanket Distribution (Gibbs)
`P(x_i | mb(X_i)) = α P(x_i | parents(X_i)) ∏_{Y_j ∈ Children(X_i)} P(y_j | parents(Y_j))` (13.10)

#### Noisy-OR
`P(x_i | parents(X_i)) = 1 − ∏_{j: X_j = true} q_j` 
- q_j = P(¬x_i | all parents false except X_j = true) = inhibition probability of parent j
- Assumptions: all possible causes listed; inhibition independence

#### Linear–Gaussian (univariate example)
`P(c|h, subsidy) = N(c; a_t h + b_t, σ²_t)`
- c = cost, h = harvest
- a_t, b_t = linear coefficients for subsidy=true case
- σ²_t = variance for subsidy=true case

#### Probit Model
`P(buys|Cost=c) = 1 − Φ((c−μ)/σ)`
- Φ(x) = ∫_{-∞}^{x} N(s; 0, 1) ds = standard normal CDF
- μ = cost threshold
- σ = width of threshold region

#### Expit (Inverse Logit) Model
`P(buys|Cost=c) = 1 − 1/(1 + exp(−4/√(2π) · (c−μ)/σ))`

#### Gibbs Sampling Markov Blanket Distribution
`P(x_i | mb(X_i)) = α P(x_i | parents(X_i)) ∏_{Y_j ∈ Children(X_i)} P(y_j | parents(Y_j))` (13.10)

#### Variable Elimination Pointwise Product
`f(X_1...X_j, Y_1...Y_k) × g(Y_1...Y_k, Z_1...Z_ℓ) = h(X_1...X_j, Y_1...Y_k, Z_1...Z_ℓ)`
- Factor size: 2^{j+k+ℓ} (binary case)

#### Variable Elimination Summing Out
`h_2(Y,Z) = ∑_x h(X,Y,Z) = h(x,Y,Z) + h(¬x,Y,Z)`

#### Rejection Sampling Estimate
`P̂(X|e) = N_PS(X,e) / N_PS(e) = α N_PS(X,e)` — consistent estimate.

#### Likelihood Weighting Weight
`w(z) = ∏_{i=1}^m P(e_i | parents(E_i))` — product of likelihoods of evidence variables given their parents.

#### Stationary Distribution Condition
`π(x') = ∑_x π(x) k(x→x')` for all x' (13.11)

#### Detailed Balance Condition
`π(x) k(x→x') = π(x') k(x'→x)` for all x, x' (13.12)

#### MH Acceptance Probability
`a(x'|x) = min(1, π(x') q(x|x') / (π(x) q(x'|x)))`

#### Causal Network Joint
`P(x_1,...,x_n) = ∏_{i=1}^n P(x_i | parents(X_i))` (13.18)

#### After do(X_j = x_jk)
`P_{x_jk}(x_1,...,x_n) = ∏_{i ≠ j} P(x_i | parents(X_i))` if x_j = x_jk; 0 otherwise (13.19)

#### Adjustment Formula
`P(X_i = x_i | do(X_j = x_jk)) = ∑_{parents(X_j)} P(x_i | x_jk, parents(X_j)) P(parents(X_j))` (13.20)

#### Back-Door Criterion (Example)
`P(g | do(S=true)) = ∑_r P(g | S=true, r) P(r)` (13.21)
- Z = {Rain} closes the back-door path Sprinkler ← Cloudy → Rain → Grass

### Rules, Laws & Theorems

##### Chain Rule (for any set of variables)
- **Statement**: P(x_1,...,x_n) = ∏_{i=1}^n P(x_i | x_{i-1},...,x_1)
- **Holds for**: any ordering of any set of random variables.

##### Non-descendants Property
- **Statement**: Each variable is conditionally independent of its non-descendants, given its parents.
- **Implications**: Defines the conditional independence semantics of Bayes nets.

##### Markov Blanket Property
- **Statement**: A variable is conditionally independent of all other nodes in the network given its Markov blanket (parents, children, children's parents).
- **Implications**: Enables local Gibbs sampling.

##### D-separation
- **Statement**: If Z d-separates X and Y in the moralized ancestral subgraph, then X is conditionally independent of Y given Z.
- **Steps**:
  1. Consider ancestral subgraph of X, Y, Z
  2. Add links between unlinked pairs sharing a common child (moral graph)
  3. Replace directed links with undirected links
  4. If Z blocks all paths between X and Y, then Z d-separates X and Y

##### NP-hardness of Bayes Net Inference
- **Statement**: Computing marginals in Bayes nets is NP-hard (can be strengthened to #P-hard).
- **Proof sketch**: Encode 3-SAT as a Bayes net; P(S=true) > 0 iff satisfiable.

### Data Structures

#### Bayesian Network
- **Components**: DAG + CPTs
- **DAG**: Nodes = random variables; directed links = direct influence; no directed cycles.
- **CPT**: For each node X_i with parents, a table P(X_i | Parents(X_i)).
  - Boolean variable with k Boolean parents: 2^k independent entries.
  - Node with no parents: one row (prior).
- **Size**: For n Boolean variables, each with ≤ k parents: ≤ 2^k·n numbers (vs 2^n for full joint).

#### Factor (Variable Elimination)
- **Structure**: Matrix indexed by values of argument variables.
- **Operations**: Pointwise product (union of variables); summing out (marginalization).

#### Moral Graph
- **Construction**: Add links between unlinked parents sharing a child; replace directed with undirected links.

### Edge Cases & Common Pitfalls

- **Deterministic CPTs break Gibbs sampling**: If P(Cloudy) and P(Rain|Cloudy) are deterministic (0 or 1), Markov chain becomes non-ergodic; Gibbs never converges.
- **Nearly deterministic causes slow mixing**: Gibbs converges arbitrarily slowly when relationships are nearly deterministic.
- **Weighted model counting**: Bayes net inference via WMC is competitive for large tree width networks.
- **Compiled inference**: 2–3 orders faster than interpreted Gibbs sampling; code is ugly but fast.
- **Zero probabilities in CPTs**: Break ergodicity for Gibbs; rejection sampling is unaffected.
- **Zero CPT entries for evidence variables**: Can make likelihood weighting weight = 0 for all samples.
- **Leaf node removal**: Any leaf that is not a query or evidence variable can be pruned; repeated removal may eliminate more variables.
- **Weight underflow**: Likelihood weighting weights become very small for long evidence sequences.
- **Hidden variables for sparsity**: Essential for making Bayes nets compact (e.g., SocioEcon, RiskAversion in insurance net).

### Case Studies & Examples

##### Burglary Network (Pearl's example)
- **What**: Bayes net with Burglary, Earthquake, Alarm, JohnCalls, MaryCalls.
- **CPTs**: P(B)=0.001; P(E)=0.002; P(A|B,E): 0.95/0.94/0.29/0.001; P(J|A): 0.90/0.05; P(M|A): 0.70/0.01.
- **Query**: P(B|J=true, M=true) = α⟨0.00059224, 0.0014919⟩ ≈ ⟨0.284, 0.716⟩
- **Significance**: Classic example of causal structure in Bayes nets.

##### Car Insurance Network
- **What**: 27-variable Bayes net for evaluating car insurance applications.
- **Structure**: 3 types of claims (MedicalCost, LiabilityCost, PropertyCost); hidden variables (SocioEcon, RiskAversion, DrivingBehavior); input variables (Age, MakeModel, Mileage, etc.).
- **Hidden variables**: SocioEcon influences MakeModel, VehicleYear, ExtraCar, GoodStudent; RiskAversion influences Garaged, AntiTheft, SafetyFeatures.
- **Size**: Discrete version requires exact inference; continuous version would be learned from data.
- **Significance**: Demonstrates real-world Bayes net construction with hidden variables.

##### 3-SAT Reduction to Bayes Net
- **What**: Propositional variables as roots with P=0.5; clause nodes as deterministic disjunctions; S as conjunction.
- **Result**: P(S=true) > 0 iff 3-SAT formula is satisfiable; #satisfying assignments = P(S=true) / 2^{-n}.
- **Significance**: Proves Bayes net inference is #P-hard.

##### Mary's Lawn (Multiply Connected Network)
- **What**: Cloudy → Sprinkler, Cloudy → Rain, Sprinkler → WetGrass, Rain → WetGrass.
- **Multiply connected**: WetGrass has two causal pathways from Cloudy.
- **Clustering**: Merge Sprinkler+Rain into meganode with 4 values to make polytree.

##### Insurance Network Performance (Empirical)
- **Rejection sampling**: ~1/1000 to 1/10000 samples consistent with evidence.
- **Likelihood weighting**: ~1000x better than enumeration; 227M operations for typical query.
- **Gibbs sampling**: Outperforms likelihood weighting when evidence is downstream.

### End-of-Chapter Material

**Key Terms**: Bayesian network, conditional probability table, chain rule, topological ordering, locally structured, d-separation, Markov blanket, moral graph, polytree, variable elimination, factor, pointwise product, rejection sampling, importance sampling, likelihood weighting, Markov chain, Gibbs sampling, Metropolis–Hastings, detailed balance, stationary distribution, causal network, do-calculus, adjustment formula, back-door criterion.

**Summary points**:
- Bayes net = DAG with conditional distributions; provides compact representation of joint distribution.
- Size often exponentially smaller than full joint distribution.
- Many conditional distributions compactly representable via canonical families.
- Exact inference: variable elimination; linear for polytrees, NP-hard in general.
- Approximate inference: likelihood weighting and MCMC for larger networks.
- Causal networks capture causal relationships and predict effects of interventions.

---

## Ch. 14 — Probabilistic Reasoning over Time

### Named Entities (Terms & Definitions)

- **Discrete time**: world viewed as series of snapshots (time slices) at t=0,1,2,...
- **Time slice**: a snapshot of the world at a particular time.
- **State variables (X_t)**: unobservable variables describing the true state at time t.
- **Evidence variables (E_t)**: observable variables at time t.
- **Markov assumption**: current state depends on only a finite fixed number of previous states.
- **Markov process (Markov chain)**: a stochastic process satisfying the Markov assumption.
- **First-order Markov process**: current state depends only on previous state: P(X_t | X_{0:t-1}) = P(X_t | X_{t-1}).
- **Second-order Markov process**: current state depends on two previous states.
- **Time-homogeneous**: transition model is the same for all t.
- **Sensor Markov assumption**: P(E_t | X_{0:t}, E_{1:t-1}) = P(E_t | X_t).
- **Transition model**: P(X_t | X_{t-1}) — how the world evolves.
- **Sensor model (observation model)**: P(E_t | X_t) — how evidence is generated.
- **Filtering (state estimation)**: computing P(X_t | e_{1:t}) — posterior over most recent state.
- **Belief state**: P(X_t | e_{1:t}) — the posterior distribution over current state.
- **Prediction**: computing P(X_{t+k} | e_{1:t}) for k>0.
- **Smoothing**: computing P(X_k | e_{1:t}) for 0≤k<t.
- **Most likely explanation**: argmax_{x_{1:t}} P(x_{1:t} | e_{1:t}).
- **Recursive estimation**: update belief state using only previous estimate and new evidence, not full history.
- **Forward message (f_{1:t})**: P(X_t | e_{1:t}) — propagated forward in filtering.
- **Backward message (b_{k+1:t})**: P(e_{k+1:t} | X_k) — propagated backward in smoothing.
- **Forward–backward algorithm**: computes smoothed estimates for all time steps in O(t).
- **Fixed-lag smoothing**: computing smoothed estimate for time slice d steps behind current time.
- **Likelihood message (ℓ_{1:t})**: P(X_t, e_{1:t}) — identical calculation to filtering; summing out gives P(e_{1:t}).
- **Mixing time**: time taken for predicted distribution to reach stationary distribution.
- **Stationary distribution**: fixed point of Markov process prediction (independent of starting point).
- **Hidden Markov model (HMM)**: temporal model with single discrete state variable.
- **Observation matrix (O_t)**: S×S diagonal matrix with P(e_t | X_t = i) on diagonal.
- **Transition matrix (T)**: S×S matrix with T_{ij} = P(X_{t+1}=j | X_t=i).
- **Viterbi algorithm**: finds most likely sequence of states given observations; linear in t.
- **Kalman filter**: filters continuous state variables with linear–Gaussian transition/sensor models.
- **Kalman gain matrix (K_{t+1})**: determines how much to correct predicted state based on observation error.
- **Extended Kalman filter (EKF)**: handles nonlinear systems by local linearization at current mean.
- **Switching Kalman filter**: multiple Kalman filters in parallel for different system modes.
- **Nonlinear system**: transition model cannot be described as matrix multiplication of state vector.
- **Dynamic Bayesian network (DBN)**: Bayes net with replicated time slices; generalizes HMMs and Kalman filters.
- **Unrolling**: replicating DBN slices to accommodate observation sequence.
- **Sequential importance sampling (SIS)**: runs all N samples through DBN one slice at a time; approximated representation degrades exponentially.
- **Particle filtering**: SIS with resampling step; focus samples on high-probability regions.
- **Evidence reversal**: sample state at t+1 conditioned on both previous state and evidence at t+1.
- **Rao-Blackwellization**: exact inference for subset of variables conditioned on sampled values of others.
- **Rao-Blackwellized particle filter**: particle filter on location with exact HMM inference for each dirt square.
- **Transient failure**: sensor occasionally sends nonsense; handled by small probability of arbitrary reading.
- **Persistent failure model**: sensor stays broken once broken; requires additional state variable BMBroken.
- **Gaussian error model**: probability of sensor error drops off in Gaussian fashion.
- **Persistence arc**: arc linking BMBroken_t to BMBroken_{t+1} with CPT giving small failure probability.
- **Assumed-density filter**: assumes posterior belongs to a finitely parameterized family; projects back if needed.
- **Factored frontier algorithm**: approximates posterior as product of small factors.
- **Particle cascade algorithm**: removes synchronization requirement for parallel particle filtering.
- **Sequential Monte Carlo (SMC)**: general family of sequential sampling algorithms including particle filtering.
- **Simultaneous localization and mapping (SLAM)**: building a map while localizing within it.

### Processes / Algorithms

#### Filtering (State Estimation) — Recursive Formulation
- **Type**: Algorithm (general temporal model)
- **Goal**: Compute P(X_{t+1} | e_{1:t+1}) from P(X_t | e_{1:t}) and e_{t+1}
- **Formula**: P(X_{t+1}|e_{1:t+1}) = α P(e_{t+1}|X_{t+1}) ∑_{x_t} P(X_{t+1}|x_t) P(x_t|e_{1:t}) (14.5)
  - α = normalization constant
  - P(e_{t+1}|X_{t+1}) = sensor model
  - P(X_{t+1}|x_t) = transition model
  - P(x_t|e_{1:t}) = previous belief state
- **Two-part process**: (1) prediction: project forward via transition model; (2) update: condition on new evidence via sensor model
- **Complexity**: Constant time and space per update (for discrete state variables).

#### Prediction
- **Type**: Algorithm
- **Goal**: Compute P(X_{t+k+1} | e_{1:t})
- **Formula**: P(X_{t+k+1}|e_{1:t}) = ∑_{x_{t+k}} P(X_{t+k+1}|x_{t+k}) P(x_{t+k}|e_{1:t}) (14.6)
- **Note**: Only transition model, no sensor model; converges to stationary distribution.

#### Forward–Backward Algorithm (Smoothing)
- **Type**: Algorithm (O(t) for all smoothed estimates)
- **Goal**: Compute P(X_k | e_{1:t}) for all 0 ≤ k < t
- **Steps**:
  1. Forward pass: Compute fv[0] = P(X_0); for i=1 to t: fv[i] = FORWARD(fv[i-1], ev[i])
  2. Initialize backward message b = vector of 1s
  3. Backward pass: for i = t down to 1:
     a. sv[i] = NORMALIZE(fv[i] × b) — smoothed estimate at i
     b. b = BACKWARD(b, ev[i])
  4. Return sv
- **FORWARD**: Implements Equation (14.5)
- **BACKWARD**: Implements Equation (14.9)
- **Complexity**: O(t) time, O(|f|t) space (can be reduced to O(|f|log t))
- **Key equation**: P(X_k | e_{1:t}) = α f_{1:k} × b_{k+1:t} (14.8)

#### Backward Recursion
- **Formula**: P(e_{k+1:t}|X_k) = ∑_{x_{k+1}} P(e_{k+1}|x_{k+1}) P(e_{k+2:t}|x_{k+1}) P(x_{k+1}|X_k) (14.9)
- **Initialization**: b_{t+1:t} = P(empty | X_t) = 1 (vector of 1s)

#### Viterbi Algorithm (Most Likely Sequence)
- **Type**: Algorithm
- **Goal**: Find argmax_{x_{1:t}} P(x_{1:t} | e_{1:t})
- **Key insight**: Most likely path to state x_{t+1} = most likely path to some state at time t + transition.
- **Message**: m_{1:t} = max_{x_{1:t-1}} P(x_{1:t-1}, X_t, e_{1:t})
- **Recursion**: m_{1:t+1} = P(e_{t+1}|X_{t+1}) max_{x_t} [ P(X_{t+1}|x_t) × max_{x_{1:t-1}} P(x_{1:t-1}, x_t, e_{1:t}) ] (14.11)
  - Summation in filtering → maximization in Viterbi; no normalization constant.
- **Steps**:
  1. Start with m_{1:0} = P(X_0)
  2. For each t: compute m_{1:t+1} using (14.11); record best predecessor for each state
  3. At end, select state with max m; follow best predecessor pointers backward
- **Complexity**: O(t) time, O(t) space (must store pointers)
- **Numerical issues**: probabilities get very small; use log probabilities or normalize each step.

#### HMM Filtering (Matrix Form)
- **Forward**: f_{1:t+1} = α O_{t+1} T^T f_{1:t} (14.12)
- **Backward**: b_{k+1:t} = T O_{k+1} b_{k+2:t} (14.13)
- **Complexity**: O(S²t) time, O(St) space (S = number of states)
- **Transition matrix**: T_{ij} = P(X_{t+1}=j | X_t=i), S×S
- **Observation matrix**: O_t is S×S diagonal with P(e_t | X_t=i) on diagonal

#### HMM Fixed-Lag Smoothing
- **Type**: Algorithm (online, constant time per update)
- **Goal**: Compute P(X_{t-d} | e_{1:t}) for fixed lag d
- **Method**: Maintain forward message f and backward transformation matrix B = ∏_{i=t-d+1}^{t} T O_i
- **Update**: B_{t-d+2:t+1} = O^{-1}_{t-d+1} T^{-1} B_{t-d+1:t} T O_{t+1} (14.16)
- **Requirements**: Transition matrix invertible; sensor model has no zeroes.

#### Kalman Filter (Continuous State)
- **Type**: Algorithm
- **Goal**: Filtering with linear–Gaussian models
- **Model**: P(x_{t+1}|x_t) = N(x_{t+1}; F x_t, Σ_x); P(z_t|x_t) = N(z_t; H x_t, Σ_z)
  - F = transition matrix, Σ_x = transition noise covariance
  - H = sensor matrix, Σ_z = sensor noise covariance
- **Update equations**:
  - Prediction: µ_{t+1|t} = F µ_t; Σ_{t+1|t} = F Σ_t F^T + Σ_x
  - Update: K_{t+1} = Σ_{t+1|t} H^T (H Σ_{t+1|t} H^T + Σ_z)^{-1}
  - µ_{t+1} = µ_{t+1|t} + K_{t+1}(z_{t+1} − H µ_{t+1|t})
  - Σ_{t+1} = (I − K_{t+1} H) Σ_{t+1|t}
- **Properties**:
  - Gaussian prior → Gaussian posterior (closed under Bayesian updating)
  - Variance update independent of observations
  - Variance converges quickly to fixed value
  - K_{t+1} = Kalman gain matrix — how much to trust new observation vs prediction

#### Particle Filtering
- **Type**: Algorithm (approximate, DBN)
- **Goal**: Filtering with sample-based representation of belief
- **Steps** (each time step):
  1. **Propagate**: For each sample i: S[i] ← sample from P(X_{t+1} | X_t = S[i])
  2. **Weight**: W[i] ← P(e_{t+1} | X_{t+1} = S[i])
  3. **Resample**: S ← WEIGHTED-SAMPLE-WITH-REPLACEMENT(N, S, W)
- **Complexity**: O(N) time per update; constant space.
- **Consistency**: As N→∞, sample population correctly represents forward message.
- **Key property**: Focuses samples on high-probability regions via resampling.

#### Unrolling a DBN
- **Type**: Technique
- **Goal**: Convert DBN to standard Bayes net for inference
- **Method**: Replicate slices for each time step in observation sequence; add slices beyond last observation have no effect.
- **Problem**: O(t) space; need to re-run inference from scratch per update.
- **Solution**: Variable elimination in temporal order keeps only 2 slices in memory.

### Classifications & Hierarchies

**Temporal Models**:
```
Temporal Models
├── Hidden Markov Model (HMM)
│   ├── Single discrete state variable
│   ├── Matrix algorithms (O(S²) per step)
│   └── Atomic representation
├── Kalman Filter
│   ├── Continuous state vector
│   ├── Linear–Gaussian models
│   ├── Gaussian posterior (mean + covariance)
│   ├── O(n³) per step
│   └── Extended KF for nonlinear systems
└── Dynamic Bayesian Network (DBN)
    ├── Multiple state variables
    ├── Factored representation (linear in n, not exponential)
    ├── Generalizes HMM and KF
    ├── Exact inference: O(n d^{n+k}) per step
    └── Approximate inference: Particle filtering
```

**Inference Tasks in Temporal Models**:
1. **Filtering** (state estimation): P(X_t | e_{1:t}) — current state
2. **Prediction**: P(X_{t+k} | e_{1:t}) — future state
3. **Smoothing**: P(X_k | e_{1:t}) for k<t — past state (better estimate than filtering at that time)
4. **Most likely explanation**: argmax_{x_{1:t}} P(x_{1:t} | e_{1:t})
5. **Learning**: transition and sensor models from observations (via EM)

**Markov Order**:
- **First-order**: P(X_t | X_{0:t-1}) = P(X_t | X_{t-1})
- **Second-order**: P(X_t | X_{t-2}, X_{t-1})
- Higher order can be reformulated as first-order with more state variables.

**Failure Models for Sensors**:
- **Gaussian error model**: small errors with Gaussian distribution
- **Transient failure model**: small probability of arbitrary reading, regardless of true state
- **Persistent failure model**: sensor stays broken once broken; needs additional state variable

### Comparisons & Trade-offs

| Dimension | Filtering | Smoothing | Prediction |
|---|---|---|---|
| Time | t (current) | k < t (past) | t+k (future) |
| Evidence used | e_{1:t} | e_{1:t} | e_{1:t} |
| Accuracy | Good (less evidence) | Better (more evidence) | Degrades→stationary dist. |
| Use | Real-time decisions | Offline analysis | Planning |

| Dimension | HMM | DBN | Kalman Filter |
|---|---|---|---|
| State space | Single discrete var | Multiple variables | Continuous vector |
| Representation cost | O(S²) transition matrix | O(n d^k) per slice | O(n²) for mean+cov |
| Inference/step | O(S²) matrix ops | O(n d^{n+k}) exact | O(n³) matrix ops |
| Posterior | Discrete distribution | Arbitrary (factored) | Single Gaussian |
| Nonlinear models | Yes (many states) | Yes | No (linear required) |
| Deterministic variables | Yes | Yes (but breaks Gibbs) | No (noise required) |
| "Constant" per update | O(S²) | Exponential in n | O(n³) |

| Dimension | SIS (plain likelihood weighting) | Particle Filtering |
|---|---|---|
| Sample quality | Degrades exponentially with t | Maintains quality via resampling |
| Needs for accuracy | N exponential in t | N constant (bounded error) |
| Handles deterministic | Yes | Can collapse |
| Weakness | Downstream evidence | Static variables; deterministic transitions |

### Formulas & Equations

#### First-Order Markov Assumption
`P(X_t | X_{0:t-1}) = P(X_t | X_{t-1})` (14.1)

#### Sensor Markov Assumption
`P(E_t | X_{0:t}, E_{1:t-1}) = P(E_t | X_t)` (14.2)

#### Complete Joint for Temporal Model
`P(X_{0:t}, E_{1:t}) = P(X_0) ∏_{i=1}^{t} P(X_i | X_{i-1}) P(E_i | X_i)` (14.3)
- P(X_0) = initial state model
- P(X_i|X_{i-1}) = transition model
- P(E_i|X_i) = sensor model

#### Filtering Recursion
`P(X_{t+1} | e_{1:t+1}) = α P(e_{t+1} | X_{t+1}) ∑_{x_t} P(X_{t+1} | x_t) P(x_t | e_{1:t})` (14.5)
- α = normalization constant
- P(e_{t+1}|X_{t+1}) = sensor model
- P(X_{t+1}|x_t) = transition model
- P(x_t|e_{1:t}) = previous forward message

#### Prediction Recursion
`P(X_{t+k+1} | e_{1:t}) = ∑_{x_{t+k}} P(X_{t+k+1} | x_{t+k}) P(x_{t+k} | e_{1:t})` (14.6)

#### Likelihood of Evidence Sequence
`P(e_{1:t}) = ∑_{x_t} P(x_t, e_{1:t}) = ∑_{x_t} ℓ_{1:t}(x_t)` (14.7)
- ℓ_{1:t}(X_t) = P(X_t, e_{1:t}) — forward likelihood message

#### Smoothing
`P(X_k | e_{1:t}) = α f_{1:k} × b_{k+1:t}` (14.8)
- f_{1:k} = P(X_k | e_{1:k}) — forward message
- b_{k+1:t} = P(e_{k+1:t} | X_k) — backward message
- × = pointwise multiplication

#### Backward Recursion
`P(e_{k+1:t} | X_k) = ∑_{x_{k+1}} P(e_{k+1} | x_{k+1}) P(e_{k+2:t} | x_{k+1}) P(x_{k+1} | X_k)` (14.9)
- Initialization: b_{t+1:t} = 1 (vector of 1s)

#### Viterbi Recursion
`m_{1:t+1} = P(e_{t+1} | X_{t+1}) max_{x_t} [P(X_{t+1} | x_t) × max_{x_{1:t-1}} P(x_{1:t-1}, x_t, e_{1:t})]` (14.11)

#### HMM Forward (Matrix Form)
`f_{1:t+1} = α O_{t+1} T^T f_{1:t}` (14.12)
- T_{ij} = P(X_{t+1}=j | X_t=i), S×S transition matrix
- O_t = diag(P(e_t | X_t=i)), S×S observation matrix
- f = S-element column vector

#### HMM Backward (Matrix Form)
`b_{k+1:t} = T O_{k+1} b_{k+2:t}` (14.13)

#### HMM Fixed-Lag Smoothing Backward Update
`B_{t-d+2:t+1} = O^{-1}_{t-d+1} T^{-1} B_{t-d+1:t} T O_{t+1}` (14.16)
- B_{a:b} = ∏_{i=a}^{b} T O_i

#### Kalman Filter Model
`P(x_{t+1}|x_t) = N(x_{t+1}; F x_t, Σ_x)` — transition
`P(z_t|x_t) = N(z_t; H x_t, Σ_z)` — sensor (14.21)
- F = transition matrix (n×n)
- Σ_x = transition noise covariance (n×n)
- H = sensor matrix (m×n)
- Σ_z = sensor noise covariance (m×m)

#### Kalman Filter Update
`µ_{t+1} = F µ_t + K_{t+1}(z_{t+1} − H F µ_t)`
`Σ_{t+1} = (I − K_{t+1} H)(F Σ_t F^T + Σ_x)` (14.22)
- K_{t+1} = (F Σ_t F^T + Σ_x) H^T (H(F Σ_t F^T + Σ_x) H^T + Σ_z)^{-1}
  - Kalman gain matrix
- µ_t = mean at time t
- Σ_t = covariance at time t
- z_{t+1} = observation at time t+1
- I = identity matrix

#### Kalman Filter — Univariate Special Case
`µ_{t+1} = ((σ²_t + σ²_x) z_{t+1} + σ²_z µ_t) / (σ²_t + σ²_x + σ²_z)`
`σ²_{t+1} = (σ²_t + σ²_x) σ²_z / (σ²_t + σ²_x + σ²_z)` (14.20)
- µ_t = old mean, σ²_t = old variance
- σ²_x = transition noise variance
- σ²_z = sensor noise variance
- z_{t+1} = new observation

#### Stationary Distribution of Markov Process
`π(x') = ∑_x π(x) k(x→x')` for all x' — defining equation.
For umbrella example with P(R_t|R_{t-1}) = [0.7 0.3; 0.3 0.7], stationary distribution = ⟨0.5, 0.5⟩.

### Rules, Laws & Theorems

##### Markov Property (First-Order)
- **Statement**: P(X_t | X_{0:t-1}) = P(X_t | X_{t-1})
- **Meaning**: The state contains all information needed for predicting the future; future is independent of past given present.
- **Implication**: Transition model needs only P(X_t|X_{t-1}), not full history.

##### Time-Homogeneity
- **Statement**: The transition model P(X_t|X_{t-1}) and sensor model P(E_t|X_t) are the same for all t.
- **Implication**: Need specify only one CPT for transition and one for sensor; infinite sequence defined by finite specification.

##### Kalman Filter Optimality
- **Statement**: For linear–Gaussian systems, the Kalman filter provides the optimal (minimum mean squared error) state estimate.
- **Conditions**: Transition and sensor models are linear with additive Gaussian noise.

##### Gaussian Closedness Under Bayesian Updating
- **Statement**: If prior is Gaussian and transition + sensor are linear–Gaussian, the posterior is Gaussian.
- **Implication**: State distribution remains Gaussian forever; only mean and covariance need tracking.

##### Particle Filter Consistency
- **Statement**: As number of particles N → ∞, the particle filter estimate converges to the true posterior.
- **Proof sketch**: Each step (propagate, weight, resample) preserves the correct forward message in expectation.

### Edge Cases & Common Pitfalls

- **First-order Markov violation**: Battery-powered robot — battery drain violates Markov property unless Battery_t is included in state.
- **Particle filter collapse with static variables**: Deterministic dirt (p=1) causes particle collapse; initial guesses never updated.
- **Numerical underflow**: Viterbi and likelihood messages become extremely small; use log probabilities or normalize each step.
- **Transient failure vs persistent failure**: Simple Gaussian error model misdiagnoses transient sensor failure as real state change; needs explicit failure modeling.
- **Mixing time**: Prediction beyond mixing time converges to stationary distribution; long-term prediction is doomed.
- **HMM state explosion**: Adding dirt to 42 locations multiplies state space by 2^42; HMM becomes infeasible but DBN remains compact.
- **Kalman filter nonlinearity**: Bird flying toward tree — single Gaussian can't represent bifurcating evasive maneuvers.
- **SIS exponential degradation**: Even with 100,000 samples, SIS fails after ~20 steps for localization.
- **Zero sensor probability**: Fixed-lag smoothing requires sensor model with no zeroes (every observation possible in every state).

### Empirical Evidence

- **HMM Localization (Figure 14.8)**: With ǫ=0.20 (59% wrong readings), robot localizes to within 2 squares after 20 observations; with ǫ=0.40, robot is lost.
- **Particle Filter vs SIS (Figure 14.19)**: SIS with 100,000 samples fails after ~20 steps; PF with 1,000 samples maintains bounded error over 100 steps.
- **Gibbs vs LW on Insurance Net (Figure 13.22)**: Gibbs outperforms LW when evidence is downstream; LW better when evidence is upstream.
- **Rejection sampling vs LW (Figure 13.19)**: LW significantly outperforms rejection sampling on insurance net.
- **Rao-Blackwellized PF for SLAM (Figure 14.21)**: Standard PF fails with deterministic dirt (p=1); Rao-Blackwellized PF with 100 particles succeeds.

### Cross-Chapter Dependencies

- Ch 14 builds on Ch 12 (probability basics) and Ch 13 (Bayes nets).
- Ch 14's Markov chains are also used in Ch 13's Gibbs sampling and Ch 17's decision processes.
- Ch 14's DBN learning uses EM algorithm from Ch 20.
- Ch 14's SLAM connection is detailed in Ch 26.
- Ch 14's sensor models connect to Kalman filters in robotics (Ch 25).
- The belief-state concept links to Ch 4 (search) and Ch 7 (logical agents).

### People & Dates

- **Andrei Markov** (1856–1922): Markov processes, Markov assumption.
- **Rudolf Kalman** (1930–2016): Kalman filter (1960); also developed by Thiele (1880) and Stratonovich (1959).
- **Andrew Viterbi**: Viterbi algorithm (1967).
- **Judea Pearl**: Bayesian networks, causal networks, d-separation, do-calculus (1980s–2000).
- **Leonard Baum** and **Ted Petrie**: HMM and forward–backward algorithm (1966).
- **Leonard Savage**: Decision theory foundations.
- **C. F. Gauss** (1809): Least-squares estimation for orbits; precursor to Kalman filtering.
- **Bruno de Finetti**: Dutch book argument for probability axioms.
- **Andrei Kolmogorov**: Axiomatic probability theory (1933).
- **Thomas Bayes** (1702–1761): Bayes' rule (posthumous 1763).
- **Pierre-Simon Laplace**: Independently developed general Bayes' rule; principle of indifference.
- **Rauch, Tung, Striebel**: Kalman smoothing (1965).
- **Gordon, Salmond, Smith**: Particle filtering reintroduced in control theory (1993).
- **Baum–Welch** (EM for HMMs): precursor to general EM (Dempster, Laird, Rubin, 1977).
- **N. Metropolis et al.** (1953): MCMC origin (Metropolis algorithm).
- **Hastings** (1970): Metropolis–Hastings generalization.
- **Geman & Geman** (1984): Gibbs sampler for undirected Markov networks.
- **Pearl** (1987): Gibbs sampling applied to Bayes nets.
- **Doucet et al.** (2000): Rao-Blackwellized particle filter.
- **Murphy & Russell** (2001): Rao-Blackwellized PF for SLAM.

### End-of-Chapter Material

**Key Terms**: discrete time, Markov process, first-order Markov process, time-homogeneous, filter, prediction, smoothing, most likely explanation, forward–backward algorithm, HMM, Kalman filter, DBN, particle filtering, Rao-Blackwellization, sequential importance sampling.

**Summary points**:
- Changing state handled by random variables for each point in time.
- Markov property: future independent of past given present; time-homogeneity simplifies representation.
- Temporal model = transition model (state evolution) + sensor model (observation process).
- Inference tasks: filtering (state estimation), prediction, smoothing, most likely explanation — all solvable in O(t) time.
- Three families: HMMs, Kalman filters, DBNs (DBNs include other two as special cases).
- Exact inference with many state variables is intractable; particle filtering is an effective approximation.

---

## Cross-Cutting Topics

### Design Paradigms & Meta-Methods

- **Recursive estimation**: Update belief state from previous estimate + new evidence; constant time/space per step. Underlies filtering in all temporal models.
- **Dynamic programming**: Used in variable elimination (caching intermediate factors), forward–backward algorithm (storing forward messages), Viterbi (storing best predecessors).
- **Divide and conquer**: Constant-space smoothing uses divide-and-conquer to trade time for space (O(|f|log t) space, O(t log t) time).
- **Importance sampling**: Correct sampling from hard distribution P using easy distribution Q with weight = P/Q.
- **Markov chain Monte Carlo**: Sample by random walk through state space; stationary distribution = target.
- **Factorization**: Decompose joint distribution into product of conditional distributions (Bayes net, DBN).
- **Completing the square**: Technique for integrating products of Gaussians; used in Kalman filter derivation.
- **Mutilation (do-operator)**: To model intervention, delete incoming edges to intervened variable; joint distribution omits that variable's CPT.

### Proof & Argument Patterns

- **Dutch book argument** (de Finetti): If agent's beliefs violate probability axioms, opponent can construct set of bets guaranteeing loss; thus rational agents must obey axioms.
- **Reduction to 3-SAT**: Bayes net inference is NP-hard (and #P-hard) by encoding 3-SAT as a Bayes net where P(S=true)>0 iff satisfiable.
- **Detailed balance → stationarity**: Summing π(x)k(x→x') over x gives π(x') — proves Gibbs and MH converge to correct stationary distribution.
- **Closed-form Gaussian integration**: Products of Gaussian exponents are quadratic; completing the square yields closed-form posterior.

### Probability & Statistics Foundation

- **Bayes' rule**: P(cause|effect) ∝ P(effect|cause) × P(cause) — universally applied.
- **Conditional independence**: The key to scaling probabilistic models; allows factorization.
- **Law of total probability**: P(Y) = ∑_z P(Y|z)P(z) — conditioning.
- **Expectation**: Weighted average; MEU principle says choose action maximizing expected utility.
- **Gaussian distribution**: N(x; μ, σ²) = (1/σ√(2π)) e^{-½((x-μ)/σ)²}; closed under linear transformations and Bayesian updating.
- **Central limit theorem**: Sum of many independent random variables is approximately Gaussian (justifies Gaussian noise models).

### People & Dates Summary

| Person | Contribution | Year |
|---|---|---|
| Thomas Bayes | Bayes' rule | 1763 (posthumous) |
| Pierre Laplace | General Bayes rule, principle of indifference | 1816 |
| C.F. Gauss | Least-squares estimation | 1809 |
| A.A. Markov | Markov chains | 1913 |
| A. Kolmogorov | Axiomatic probability | 1933 |
| B. de Finetti | Dutch book argument | 1937 |
| L. Baum, T. Petrie | HMM, forward-backward | 1966 |
| A. Viterbi | Viterbi algorithm | 1967 |
| R. Kalman | Kalman filter | 1960 |
| N. Metropolis et al. | MCMC (Metropolis) | 1953 |
| W. Hastings | Metropolis-Hastings | 1970 |
| S. Geman, D. Geman | Gibbs sampler | 1984 |
| J. Pearl | Bayes nets, causal nets, do-calculus | 1982-2000 |
| N. Gordon et al. | Particle filtering | 1993 |
| A. Doucet et al. | Rao-Blackwellized PF | 2000 |

---

## Exam Questions by Type

### MCQ

1. **Q:** Bayes' rule allows computing P(cause|effect) from:
   a) P(effect), P(cause), P(effect|cause)
   b) P(cause), P(effect|cause), P(effect)
   c) P(cause|effect), P(cause), P(effect)
   d) P(effect|cause), P(cause), P(effect)
   **A:** d. **Distractor:** b is same as d but reordered; a is missing P(effect|cause).

2. **Q:** A Bayesian network with all Boolean variables has n nodes, each with at most k parents. How many numbers are needed for the CPTs?
   a) 2^n
   b) n × 2^k
   c) 2^{n+k}
   d) k × 2^n
   **A:** b. **Distractor:** a is full joint distribution size.

3. **Q:** What is the stationary distribution of a first-order Markov process?
   a) The distribution after one time step
   b) The fixed point of the transition kernel: π(x') = ∑_x π(x) k(x→x')
   c) The prior P(X_0)
   d) The posterior after filtering
   **A:** b. **Distractor:** a is the one-step prediction, not stationary.

4. **Q:** In a polytree Bayes net, exact inference takes time:
   a) Exponential in the number of nodes
   b) Linear in the size of the network
   c) O(n log n)
   d) Quadratic in the number of CPT entries
   **A:** b. **Distractor:** a applies to multiply connected networks.

5. **Q:** The Viterbi algorithm differs from filtering in that:
   a) It sums instead of maximizing
   b) It maximizes instead of summing, and has no normalization constant
   c) It uses only the sensor model
   d) It requires a Gaussian distribution
   **A:** b. **Distractor:** a is the opposite; c is false (uses both models).

### Short Answer

1. **Q:** State Bayes' rule and explain why causal knowledge is more robust than diagnostic knowledge.
   **Rubric:** P(b|a) = P(a|b)P(b)/P(a). Causal knowledge P(effect|cause) reflects underlying mechanisms unaffected by changes in prior of cause. Diagnostic knowledge P(cause|effect) must be re-estimated when priors change (e.g., epidemic).

2. **Q:** Define d-separation and explain how to determine if X is conditionally independent of Y given Z.
   **Rubric:** Consider ancestral subgraph of X,Y,Z; moralize (add links between unpaired parents sharing child); replace directed links with undirected. If Z blocks all paths between X and Y, then Z d-separates X and Y and conditional independence holds.

3. **Q:** Describe the three inference tasks in temporal models and give the formula for filtering.
   **Rubric:** Filtering (state estimation): P(X_t|e_{1:t}); Prediction: P(X_{t+k}|e_{1:t}); Smoothing: P(X_k|e_{1:t}) for k<t. Filtering: P(X_{t+1}|e_{1:t+1}) = α P(e_{t+1}|X_{t+1}) ∑_{x_t} P(X_{t+1}|x_t) P(x_t|e_{1:t}).

### Trace / Apply

1. **Input:** Umbrella DBN: P(R_0)=⟨0.5,0.5⟩; P(R_t|R_{t-1}): 0.7/0.3; P(U_t|R_t): 0.9/0.2. Observe U_1=true, U_2=true. **Apply filtering** to compute P(R_2|u_1,u_2).
   **Expected output:** Step 1: P(R_1) = 0.5×⟨0.7,0.3⟩+0.5×⟨0.3,0.7⟩ = ⟨0.5,0.5⟩. Step 2: P(R_1|u_1) = α⟨0.9,0.2⟩×⟨0.5,0.5⟩ = α⟨0.45,0.1⟩ = ⟨0.818,0.182⟩. Step 3: P(R_2|u_1) = 0.818×⟨0.7,0.3⟩+0.182×⟨0.3,0.7⟩ = ⟨0.627,0.373⟩. Step 4: P(R_2|u_1,u_2) = α⟨0.9,0.2⟩×⟨0.627,0.373⟩ = α⟨0.565,0.075⟩ = ⟨0.883,0.117⟩.

2. **Input:** Burglary net. Query P(B|j,m). **Apply variable elimination** to compute P(B|j,m).
   **Expected output:** Show f_4(A)=⟨0.90,0.05⟩, f_5(A)=⟨0.70,0.01⟩, f_3(A,B,E)=CPT. Sum out A: f_6(B,E). Sum out E: f_7(B). Multiply with f_1(B)=⟨0.001,0.999⟩. Normalize → ⟨0.284,0.716⟩.

### Essay / Long-Form

1. **Q:** Compare and contrast HMMs, Kalman filters, and DBNs for temporal probabilistic reasoning. Discuss representation, inference complexity, and when each is appropriate.
   **Key points:** HMM: single discrete state, O(S²) per step, atomic state representation; good for speech, bioinformatics. Kalman: continuous vector, linear-Gaussian, O(n³) per step, Gaussian posterior; good for tracking. DBN: multiple variables, factored representation (linear in n), exact inference exponential in n; generalizes both. DBN preferred for complex systems with many interacting variables; particle filtering makes DBN inference practical. HMMs suffer state explosion; Kalman fails with nonlinearity.

2. **Q:** Explain the role of conditional independence in scaling probabilistic inference. Discuss with examples from Bayes nets and the naive Bayes model.
   **Key points:** Full joint distribution O(2^n); conditional independence allows factorization into O(n2^k). Bayes net: each variable independent of non-descendants given parents. Naive Bayes: all effects independent given cause. Wumpus world: frontier variables separate query from irrelevant variables. Without conditional independence, probabilistic AI would be infeasible.
