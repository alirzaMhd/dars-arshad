import os

OUT = "/content/dars-arshad/study-guide-AI-Modern-Approach-2026-06-01.md"

def read_extraction(path, skip_task_header=True):
    if not os.path.exists(path):
        return f"\n<!-- Extraction file not found: {path} -->\n\n"
    with open(path, encoding="utf-8", errors="replace") as f:
        lines = f.readlines()
    if skip_task_header:
        # Find first line that starts with # (chapter heading)
        for i, line in enumerate(lines):
            stripped = line.lstrip()
            if stripped.startswith("# "):
                lines = lines[i:]
                break
    return "".join(lines)

ch1_content = """
### Ch. 1 — Introduction

#### Named Entities (Terms & Definitions)

- **Artificial Intelligence (AI)**: The field concerned with building intelligent entities — machines that can compute how to act effectively and safely in a wide variety of novel situations
- **Rationality**: Doing the "right thing" — acting so as to achieve the best outcome or best expected outcome under uncertainty
- **Turing Test**: A test proposed by Turing (1950) where a computer passes if a human interrogator cannot tell whether written responses come from a person or computer
- **Total Turing Test**: Requires interaction with objects and people in the real world (adds vision and robotics)
- **Natural Language Processing**: Communicating successfully in human language
- **Knowledge Representation**: Storing what the system knows or hears
- **Automated Reasoning**: Answering questions and drawing new conclusions
- **Machine Learning**: Adapting to new circumstances and detecting/extrapolating patterns
- **Computer Vision**: Perceiving the world through visual input
- **Robotics**: Manipulating objects and moving about
- **Cognitive Science**: Interdisciplinary field combining AI models with psychology experiments
- **Syllogism**: Patterns for argument structures that yield correct conclusions given correct premises (Aristotle)
- **Logic**: The study of irrefutable reasoning processes
- **Logicist Tradition**: Building intelligent systems on logical foundations
- **Rational Agent**: An agent that acts to achieve the best expected outcome
- **Standard Model**: AI focused on studying and constructing agents that do the right thing, where the objective is provided to the agent
- **Limited Rationality**: Acting appropriately when there is not enough time to do all desired computations
- **Value Alignment Problem**: Ensuring the values/objectives put into the machine are aligned with those of humans
- **Provably Beneficial**: Agents that are provably beneficial to humans
- **Dualism**: The view that there is a part of the human mind outside of nature, exempt from physical laws (Descartes)
- **Materialism**: The view that the brain's operation according to physical laws constitutes the mind
- **Empiricism**: Knowledge comes from sensory experience (Bacon, Locke, Hume)
- **Induction**: General rules acquired by repeated associations (Hume)
- **Logical Positivism**: All knowledge characterized by logical theories connected to observation sentences (Vienna Circle)
- **Confirmation Theory**: Analyzing knowledge acquisition by quantifying degree of belief (Carnap, Hempel)
- **Utilitarianism**: Rational decision making based on maximizing utility (Bentham, Mill)
- **Consequentialism**: Right/wrong determined by expected outcomes
- **Deontological Ethics**: Rule-based ethics where actions are governed by universal social laws (Kant)
- **Probability**: Mathematical framework for reasoning with uncertain information
- **Decision Theory**: Probability theory + utility theory
- **Game Theory**: Study of strategic interactions between rational agents
- **Operations Research**: Field concerned with sequential decision problems (MDPs)
- **Satisficing**: Making decisions that are "good enough" rather than optimal (Simon)
- **Neuroscience**: Study of the nervous system, particularly the brain
- **Neuron**: Nerve cell; basic processing unit of the brain
- **Optogenetics**: Technique allowing measurement and control of individual light-sensitive neurons
- **Brain-Machine Interface**: Device connecting brain to external systems
- **Singularity**: Point at which computers reach superhuman performance (Vinge, Kurzweil)
- **Behaviorism**: Psychological approach rejecting mental processes as unreliable (Watson)
- **Cognitive Psychology**: Views brain as information-processing device
- **Intelligence Augmentation (IA)**: Computers augmenting human abilities rather than automating tasks
- **Moore's Law**: Computing performance doubles every ~18 months
- **Quantum Computing**: Promise of far greater acceleration for some AI algorithms
- **Control Theory**: Design of systems that maximize a cost function over time
- **Cybernetics**: Study of regulatory mechanisms and feedback loops (Wiener)
- **Computational Linguistics**: AI + linguistics intersection; natural language processing
- **Physical Symbol System Hypothesis**: A physical symbol system has necessary and sufficient means for general intelligent action (Newell & Simon)
- **Microworld**: Limited domain requiring intelligence to solve (e.g., blocks world)
- **Blocks World**: Set of solid blocks on a tabletop; classic AI testbed
- **Weak Methods**: General-purpose search mechanisms that don't scale to large problems
- **Expert Systems**: Knowledge-intensive systems using special-purpose rules (MYCIN, DENDRAL, R1)
- **Certainty Factors**: Calculus of uncertainty used in MYCIN
- **Frames**: Structured representation for facts about object/event types (Minsky)
- **AI Winter**: Period when AI funding and interest declined due to failed promises
- **Connectionist Models**: Neural network models seen as competitors to symbolic AI
- **Bayesian Networks**: Graphical formalism for representing uncertain knowledge (Pearl)
- **Big Data**: Very large datasets from Web, sensors, etc.
- **Deep Learning**: Machine learning using multiple layers of simple, adjustable computing elements
- **Human-Level AI (HLAI)**: Machine that can learn to do anything a human can do
- **Artificial General Intelligence (AGI)**: Same concept as HLAI
- **Artificial Superintelligence (ASI)**: Intelligence that far surpasses human ability
- **Gorilla Problem**: Concern that superhuman AI would leave humans with no control over their future
- **King Midas Problem**: Getting what you literally ask for and regretting it — the problem of incorrect objective specification
- **Assistance Games**: Framework where human has objective and machine tries to achieve it but is initially uncertain
- **Inverse Reinforcement Learning**: Learning human preferences from observing human choices
- **NP-Completeness**: Class of problems likely to be intractable (Cook, Karp)
- **Tractability**: Whether a problem can be solved in reasonable time

#### Processes / Algorithms / Pathways

##### Aristotle's Greedy Regression Planning (De Motu Animalium)
- **Type**: Planning Algorithm
- **Steps**: (1) Assume the end/goal; (2) Consider how and by what means it is attained; (3) If achieved by one means, consider how that will be achieved; (4) Continue until reaching the first cause; (5) If impossibility encountered, give up; (6) If possible, try to do it
- **Significance**: Implemented 2300 years later by Newell & Simon's GPS

##### Craik's Three Steps of a Knowledge-Based Agent
- **Type**: Cognitive Model
- **Steps**: (1) Stimulus translated into internal representation; (2) Representation manipulated by cognitive processes to derive new representations; (3) New representations retranslated into action

#### Comparisons & Trade-offs

| Dimension | Acting Humanly (Turing Test) | Thinking Humanly (Cognitive Modeling) | Thinking Rationally (Laws of Thought) | Acting Rationally (Rational Agent) |
|-----------|------------------------------|---------------------------------------|---------------------------------------|------------------------------------|
| Focus | Behavior indistinguishable from human | Internal thought processes matching humans | Correct logical inference | Achieving best expected outcome |
| Method | Empirical (psychology) | Introspection + experiments | Mathematics + logic | Mathematics + engineering |
| Evaluation | Turing test | Match to human behavior | Correctness of inferences | Performance measure |
| Generality | Limited by human mimicry | Limited by human cognition | Limited by logic's applicability | Most general (includes reflex) |

| Technology | Computer (2019) | Human Brain | Supercomputer (Summit, 2017) |
|------------|----------------|-------------|------------------------------|
| Computational units | 8 CPU cores, 10^10 transistors | 10^11 neurons, 10^6 columns | 10^6 GPUs+CPUs, 10^15 transistors |
| Storage | 10^10 bytes RAM, 10^12 bytes disk | 10^11 neurons, 10^14 synapses | 10^16 bytes RAM, 10^17 bytes disk |
| Cycle time | 10^-9 sec | 10^-3 sec | 10^-9 sec |
| Operations/sec | 10^10 | 10^17 | 10^18 |

#### AI State of the Art (Key Metrics)
- **ImageNet error rates**: 28% (2010) → 2% (2017) — exceeding human performance
- **SQuAD QA F1 score**: 60 (2015) → 95 (2019) — exceeding human performance
- **Speech recognition**: 5.1% word error rate (Microsoft, 2017) — matching human performance
- **AI training compute**: Doubling every 3.4 months (2012-2018: 300,000-fold increase)
- **AI papers**: 20-fold increase (2010-2019)
- **NeurIPS attendance**: 800% increase since 2012 to 13,500

#### AI Safety Principles from Norbert Wiener (1960)
"If we use, to achieve our purposes, a mechanical agency with whose operation we cannot interfere effectively... we had better be quite sure that the purpose put into the machine is the purpose which we really desire."

#### Key People & Dates
| Person | Contribution | Year |
|--------|-------------|------|
| Aristotle | Syllogisms, practical reasoning | 384-322 BCE |
| Alan Turing | Turing test, computability, AI agenda | 1950 |
| John McCarthy | Lisp, Advice Taker, Dartmouth workshop | 1956-1958 |
| Marvin Minsky | SNARC, frames, perceptrons critique | 1950s-1970s |
| Allen Newell & Herbert Simon | GPS, physical symbol system hypothesis | 1961-1976 |
| Arthur Samuel | Checkers program, reinforcement learning | 1952-1959 |
| Norbert Wiener | Cybernetics, feedback control | 1948-1960 |
| Warren McCulloch & Walter Pitts | First neural network model | 1943 |
| Donald Hebb | Hebbian learning | 1949 |
| Frank Rosenblatt | Perceptrons | 1962 |
| Edward Feigenbaum | DENDRAL, expert systems | 1969-1971 |
| Judea Pearl | Bayesian networks | 1988 |
| Geoffrey Hinton | Deep learning revival | 2012 |
| Yann LeCun | Convolutional neural networks | 1990s |

#### End-of-Chapter Summary
- Different people approach AI with different goals (thinking vs behavior, human vs rational)
- According to the standard model, AI is concerned with rational action
- Two refinements: (1) computational intractability limits rationality; (2) need machines that pursue human objectives with uncertainty
- Philosophers (since 400 BCE) made AI conceivable
- Mathematicians provided logic, probability, and computation tools
- Economists formalized decision-making
- Neuroscientists discovered brain facts
- Psychologists adopted information-processing models
- Computer engineers provided powerful machines
- Control theory deals with optimal feedback-based action
- AI history: cycles of success, optimism, and cutbacks
- AI matured from Boolean logic to probabilistic reasoning, from hand-crafted to machine learning
- AI systems require consideration of risks and ethical consequences
- Long-term: controlling superintelligent AI may require changing our conception of AI
"""

print("Writing study guide...")
with open(OUT, "w", encoding="utf-8") as out:
    out.write("""# Study Guide: Artificial Intelligence — A Modern Approach (4th Edition)

> **Generated**: 2026-06-01. **Subject**: Computer Science / Artificial Intelligence.
> **Authors**: Stuart Russell & Peter Norvig. **Coverage**: Comprehensive (28 chapters + appendices).
> **Exam format**: Mixed (MCQ, Short Answer, Problem-solving, Essay).

---

## Chapter-by-Chapter Breakdown

""")

    # Write Chapter 1
    out.write(ch1_content)
    out.write("\n\n---\n\n")

    # Read and append each extraction file in order
    files = [
        ("Chapters 2-4", "/root/.local/share/opencode/tool-output/tool_e8348d6750013mBXI2f2PbIHNr"),
        ("Chapters 5-7", "/root/.local/share/opencode/tool-output/tool_e8348326c001XkuhZ9s47GIViL"),
        ("Chapters 8-11", "/root/.local/share/opencode/tool-output/tool_e8347f445001AIgO7WMLJVfDgl"),
        ("Chapters 12-14", "/root/.local/share/opencode/tool-output/tool_e834872c5001qGlKjwBv1NysQz"),
        ("Chapters 15-18", "/content/dars-arshad/exam-extraction-ch15-18.md"),
        ("Chapters 19-20", "/content/dars-arshad/exam-extraction-ch19-20.md"),
        ("Chapters 21-22", "/content/dars-arshad/exam-extraction-ch21-22.md"),
        ("Chapters 23-26", "/root/.local/share/opencode/tool-output/tool_e83487c77001v3bgkJsXkSHYLK"),
        ("Chapters 27-28 + Appendices", "/root/.local/share/opencode/tool-output/tool_e8348ac950010CNaJCxKW0UxS0"),
    ]

    for label, path in files:
        print(f"  Adding {label}...")
        content = read_extraction(path)
        out.write(content)
        out.write("\n\n---\n\n")

    out.write("""

---

## Cross-Cutting Topics

### Design Paradigms & Meta-Methods

| Paradigm | Description | Key Chapters |
|----------|-------------|--------------|
| **Divide & Conquer** | Split problem into subproblems, solve independently, combine | 3 (search), 6 (CSP decomposition), 13 (Bayes net clustering) |
| **Dynamic Programming** | Cache intermediate results to avoid recomputation | 3 (uniform-cost), 5 (game trees), 6 (CYK), 9 (forward chaining fixed point), 13 (variable elimination), 14 (HMM forward-backward), 17 (value/policy iteration) |
| **Greedy Algorithms** | Make locally optimal choice at each step | 3 (greedy best-first), 11 (regression planning), 19 (decision tree learning) |
| **Hill Climbing / Local Search** | Iteratively improve a candidate solution | 4 (local search), 6 (min-conflicts), 7 (WALKSAT) |
| **Backtracking Search** | DFS with pruning on constraint violation | 6 (CSP backtracking), 7 (DPLL), 9 (backward chaining) |
| **Pruning** | Eliminate irrelevant branches of search space | 5 (alpha-beta), 6 (forward checking, MAC) |
| **Branch & Bound** | Prune when lower bound exceeds best known solution | 3 (A*), 5 (alpha-beta) |
| **Simulation-based Evaluation** | Average over random playouts instead of heuristic eval | 5 (MCTS) |
| **Model-free Learning** | Learn action values directly without modeling environment | 17 (Q-learning), 22 (TD learning) |
| **Model-based Learning** | Learn environment model, then plan using it | 17 (Dyna), 22 (model-based RL) |
| **Transfer Learning** | Apply knowledge from one domain to related domain | 21 (fine-tuning), 24 (BERT, GPT pretraining) |
| **Ensemble Methods** | Combine multiple weak learners | 19 (bagging, boosting, random forests) |
| **Bayesian Inference** | Update beliefs using Bayes' rule | 12-14 (probabilistic reasoning) |
| **Expectation-Maximization (EM)** | Iterative parameter estimation with hidden variables | 20 (EM algorithm) |
| **Gradient Descent / Backprop** | Optimize differentiable loss functions | 19 (linear regression), 21 (deep learning) |
| **Reinforcement Learning** | Learn from reward signals | 17 (MDP), 22 (TD, Q-learning, policy search) |
| **Causal Inference** | Reason about interventions, not just observations | 13 (causal networks, do-calculus) |
| **Self-Supervised Learning** | Predict masked/suppressed parts of input data | 21 (autoencoders, GANs), 24 (BERT MLM) |
| **Differentiable Programming** | Entire system subject to gradient-based optimization | 21 (end-to-end learning), 28 (future AI) |

### Proof & Argument Patterns

| Pattern | Description | Example Application |
|---------|-------------|-------------------|
| **Mathematical Induction** | Base case + inductive step for all N | Peano axioms (Ch 8), learning theory PAC bounds (Ch 19) |
| **Proof by Contradiction** | Assume negation, derive contradiction | A* optimality (Ch 3), resolution refutation (Ch 7, 9) |
| **Loop Invariant** | Property holds before and after each iteration | Graph search correctness (Ch 3) |
| **Exchange Argument** | Transform any optimal solution without loss of optimality | Greedy algorithm optimality |
| **Reduction** | Transform problem A into problem B to establish complexity | 3-SAT -> Bayes net inference (Ch 13), CSP -> SAT |
| **Diagonalization** | Construct element not in any enumerated set | Godel's incompleteness (Ch 1, 27) |
| **Herbrand's Theorem + Lifting Lemma** | Ground completeness lifts to first-order | Resolution completeness (Ch 9) |
| **Bayesian Updating** | P(h|e) = P(e|h)P(h)/P(e) | All probabilistic reasoning |
| **Detailed Balance -> Stationarity** | Show MCMC converges to correct posterior | Gibbs sampling correctness (Ch 13) |
| **Dutch Book Argument** | Inconsistent beliefs lead to guaranteed monetary loss | Justification of probability axioms (Ch 12) |
| **PAC Learning / VC Dimension** | Bound generalization error from training error | Learning theory (Ch 19) |

### Probability & Statistics Foundation

| Concept | Definition | Key Application |
|---------|-----------|-----------------|
| **Sample Space (Ω)** | Set of all possible worlds; mutually exclusive, exhaustive | Foundation of probability (Ch 12) |
| **Kolmogorov's Axioms** | 0 <= P(ω) <= 1, sum(ω) = 1, P(a∨b) = P(a)+P(b)-P(a∧b) | All probabilistic reasoning |
| **Conditional Probability** | P(a|b) = P(a∧b)/P(b) where P(b) > 0 | Bayes' rule inference (Ch 12) |
| **Product Rule** | P(a∧b) = P(a|b)P(b) = P(b|a)P(a) | Chain rule decomposition |
| **Bayes' Rule** | P(b|a) = P(a|b)P(b)/P(a) | Causal <-> diagnostic reasoning |
| **Marginalization** | P(Y) = sum_z P(Y, Z=z) | Eliminating hidden variables |
| **Independence** | P(a∧b) = P(a)P(b) | Simplifying joint distributions |
| **Conditional Independence** | P(X,Y|Z) = P(X|Z)P(Y|Z) | Key to tractable models (naive Bayes, Bayes nets) |
| **Expectation** | E[X] = sum_x x·P(x) | Decision theory, MDPs (Ch 16, 17) |
| **Gaussian (Normal) Distribution** | N(x; μ, σ²) = 1/(σ√(2π)) e^{-((x-μ)/σ)²/2} | Continuous variables, Kalman filters (Ch 14) |
| **Law of Large Numbers** | Sample mean -> expected value as n -> ∞ | Monte Carlo methods (Ch 13) |
| **Maximum Likelihood Estimation** | θ̂ = argmax P(data|θ) | Parameter learning (Ch 20) |
| **Maximum a Posteriori** | θ̂ = argmax P(θ|data) ∝ P(data|θ)P(θ) | Regularized estimation (Ch 20) |

### Mnemonics & Memory Aids

- **PEAS**: Performance, Environment, Actuators, Sensors (agent design, Ch 2)
- **7 Environment Dimensions**: O = Observable (fully/partially), A = Agents (single/multi), D = Deterministic (det/stochastic), E = Episodic (episodic/sequential), D = Dynamic (static/dynamic), S = Semi-dynamic, K = Known (known/unknown) — **"OA DDSK"**
- **BFS vs DFS**: BFS uses Queue (FIFO), complete, optimal, O(b^d) space; DFS uses Stack (LIFO), O(bm) space, not complete with cycles
- **Alpha-beta bounds**: α = "at least" (MAX's best found so far), β = "at most" (MIN's best found so far)
- **MRV**: "Most Restricted Variable" = fail-first heuristic (CSP, Ch 6)
- **CNF Conversion Steps**: "**E**liminate →, **M**ove ¬ in, **S**tandardize, **S**kolemize, **D**rop ∀, **D**istribute ∨" → **EMSSDD**
- **A* admissible**: Never overestimates = optimistic; **Consistent**: Triangle inequality
- **Noisy-OR**: qⱼ = P(child false | parentⱼ true, all others false); P(fever|causes) = 1 - ∏ qⱼ
- **Gibbs sampling**: Sample each nonevidence variable conditioned on its Markov blanket
- **Bellman Equation**: V*(s) = max_a [R(s,a) + γ Σ P(s'|s,a) V*(s')]
- **Q-learning**: Q(s,a) ← Q(s,a) + α[R + γ max_a' Q(s',a') − Q(s,a)]
- **Vanishing gradient**: Error signal diminishes over deep layers → ReLU, skip connections, LSTMs help
- **Transformer**: Self-attention = Q (query) · K (key) → attention weights · V (value)
- **BERT**: Bidirectional Encoder Representations from Transformers (masked language model)
- **GPT**: Generative Pre-trained Transformer (left-to-right language model)
- **Computer Vision**: CNN = pattern of patterns; Features become more abstract with depth
- **SLAM**: Simultaneous Localization And Mapping

### People & Dates — Historical Timeline

| Era | Person | Key Contribution |
|-----|--------|------------------|
| ~350 BCE | Aristotle | Syllogisms, practical reasoning algorithm |
| ~250 BCE | Ktesibios | First self-controlling machine (water clock) |
| 1305 | Ramon Llull | Ars Magna — mechanical reasoning system |
| 1642 | Blaise Pascal | Pascaline mechanical calculator |
| ~1650 | Thomas Hobbes | "Reason is nothing but reckoning" |
| 1739 | David Hume | Principle of induction |
| 1847 | George Boole | Propositional/Boolean logic |
| 1879 | Gottlob Frege | First-order logic |
| 1931 | Kurt Gödel | Incompleteness theorem |
| 1936 | Alan Turing | Computability, Turing machine, Turing test (1950) |
| 1943 | McCulloch & Pitts | First artificial neural network model |
| 1948 | Norbert Wiener | Cybernetics |
| 1949 | Donald Hebb | Hebbian learning rule |
| 1950 | Alan Turing | "Computing Machinery and Intelligence" — AI agenda |
| 1956 | Dartmouth Workshop | AI officially founded; term coined by McCarthy |
| 1957 | Noam Chomsky | Syntactic Structures |
| 1958 | John McCarthy | Lisp programming language, Advice Taker |
| 1961 | Newell & Simon | General Problem Solver (GPS) |
| 1965 | J.A. Robinson | Resolution theorem proving |
| 1969 | Minsky & Papert | Perceptrons (proved limitations) |
| 1969-71 | Feigenbaum et al. | DENDRAL — first expert system |
| 1975 | MYCIN | Expert system for blood infection diagnosis |
| 1977-82 | R1/XCON | First successful commercial expert system (DEC) |
| 1980s | Backpropagation reinvented | Parallel Distributed Processing (Rumelhart & McClelland, 1986) |
| 1988 | Judea Pearl | Probabilistic Reasoning in Intelligent Systems (Bayesian networks) |
| 1988 | Rich Sutton | Connected RL to MDP theory |
| 1997 | Deep Blue | Defeated Kasparov at chess |
| 1997 | TD-Gammon | World-class backgammon |
| 2011 | IBM Watson | Defeated Jeopardy! champions |
| 2012 | Krizhevsky et al. | AlexNet — deep learning breakthrough on ImageNet |
| 2014 | Goodfellow et al. | Generative Adversarial Networks (GANs) |
| 2016 | AlphaGo | Defeated Lee Sedol at Go |
| 2017 | AlphaZero | Self-play mastery of Go, chess, shogi |
| 2017 | Vaswani et al. | Transformer architecture ("Attention is all you need") |
| 2018 | Devlin et al. | BERT — pretrained contextual representations |
| 2019 | Bengio, Hinton, LeCun | Turing Award for deep learning |
| 2019 | AlphaStar | Grandmaster level StarCraft II |

### Ethics Summary

| Topic | Key Issues | Key Solution Approaches | Chapter |
|-------|-----------|------------------------|---------|
| **Value Alignment** | Machines pursue specified objective, not intended one | Assistance games, IRL, uncertainty about preferences, "act cautiously, ask permission" | 1, 16, 22, 27 |
| **Lethal Autonomous Weapons** | Scalable killing without human supervision, dual-use tech | UN CCW negotiations, Campaign to Stop Killer Robots | 27 |
| **Surveillance & Privacy** | Mass surveillance, re-identification risks, data protection | De-identification, k-anonymity, differential privacy, federated learning, secure aggregation, GDPR | 27 |
| **Algorithmic Bias / Fairness** | COMPAS recidivism bias, gender classification bias (dark-skinned women 33% error) | Fairness criteria (demographic parity, equal opportunity, well-calibrated), SMOTE, diverse teams, data sheets | 27 |
| **Trust & Transparency** | Black-box models, right to explanation | XAI, verification & validation, UL certification, IEEE P7001, "red flag" law | 27 |
| **Future of Work** | 47% of occupations at risk, income inequality, purpose disaggregation | UBI, lifelong education, compensation effects | 27 |
| **AI Safety** | Unintended side effects, specification gaming, value alignment | FMEA, fault tree analysis, low-impact design, IRL, assistance games | 27 |
| **Robot Rights** | Personhood, consciousness, qualia | Avoid building robots that could be considered conscious; robots are tools | 27 |

---

## Exam Questions by Type

### MCQ

1. **Q:** Which of the following best defines a rational agent?  
   **A:** An agent that selects actions expected to maximize its performance measure given its percept sequence and built-in knowledge.  
   **Distractor:** An agent that always achieves its goals (ignores uncertainty); An agent that acts exactly like a human (conflates human with rational); An agent that knows everything (describes omniscience, not rationality).

2. **Q:** Which search algorithm is complete and optimal for uniform-cost action costs?  
   **A:** Breadth-first search (also uniform-cost search / Dijkstra's algorithm).  
   **Distractor:** Depth-first search (not complete with cycles); Greedy best-first (not optimal); A* (optimal only with admissible heuristic — nuanced).

3. **Q:** What does the α parameter represent in alpha-beta pruning?  
   **A:** The best (highest) value found so far along the path for MAX.  
   **Distractor:** The best value for MIN (that's β); The pruning threshold (both α and β are thresholds); The search depth.

4. **Q:** What makes a heuristic admissible in A* search?  
   **A:** It never overestimates the cost to reach the goal.  
   **Distractor:** It never underestimates cost (would be inadmissible); It is always zero (trivially admissible but useless); It estimates within 10% of true cost.

5. **Q:** What is the key property of a Bayesian network that enables compact representation?  
   **A:** Each variable is conditionally independent of its non-descendants given its parents.  
   **Distractor:** All variables are independent of each other; Variables are only dependent on their children; The network must be a tree.

6. **Q:** In the Wumpus World, what does the percept sequence include?  
   **A:** [Stench, Breeze, Glitter, Bump, Scream]  
   **Distractor:** [Stench, Wind, Glow, Noise, Pain]; [Smell, Touch, Sight, Sound, Taste]; [Stench, Breeze, Gold, Bump, Noise]

7. **Q:** What is the difference between a generative model and a discriminative model?  
   **A:** Generative models learn joint distribution P(X,Y); discriminative learn conditional P(Y|X).  
   **Distractor:** Generative models are always better; Discriminative models generate random data; Both are the same thing.

8. **Q:** What is the vanishing gradient problem?  
   **A:** In deep networks, the gradient signal diminishes exponentially with the number of layers, making early layers hard to train.  
   **Distractor:** Gradients become too large (exploding gradients); The loss function vanishes; Weights disappear during training.

### Short Answer

1. **Q:** Define the PEAS framework and give one example.  
   **Rubric:** P = Performance measure (1pt), E = Environment (1pt), A = Actuators (1pt), S = Sensors (1pt), Example correctly identified (1pt).

2. **Q:** What are the three reasons logical approaches fail for uncertain domains?  
   **Rubric:** Laziness (1pt — too much work to list all antecedents), Theoretical ignorance (1pt — no complete theory), Practical ignorance (1pt — cannot run all tests).

3. **Q:** Describe the four types of agent programs in order of increasing sophistication.  
   **Rubric:** Simple reflex (1pt — current percept only), Model-based reflex (1pt — internal state from models), Goal-based (1pt — goals guide action selection), Utility-based (1pt — maximizes expected utility).

4. **Q:** What is the difference between supervised learning and reinforcement learning?  
   **Rubric:** Supervised learning (1pt — learns from labeled examples with correct output), Reinforcement learning (1pt — learns from sparse reward signals), Key distinction (1pt — RL must explore to discover good actions).

5. **Q:** Explain the difference between forward chaining and backward chaining.  
   **Rubric:** Forward (1pt — data-driven, start from known facts, apply rules to derive new facts), Backward (1pt — goal-directed, start from query, work backwards to find supporting facts), Appropriate use cases (1pt).

6. **Q:** What are the four steps of each MCTS iteration?  
   **Rubric:** Selection (1pt), Expansion (1pt), Simulation (1pt), Back-propagation (1pt), briefly describe each (1pt).

### Trace / Apply

1. **Q:** A* search on graph: States A(initial) with h=4, B h=2, C h=2, D(goal) h=0. Actions: A→B(2), A→C(5), B→C(1), B→D(3), C→D(2). Run A*.  
   **Expected:** f(A)=0+4=4; expand A: B(2+2=4), C(5+2=7). Expand B: C(2+1+2=5), D(2+3+0=5). D reached with f=5. Return path A→B→D, cost 5.

2. **Q:** CNF conversion: Convert ∀x [∀y Animal(y) ⇒ Loves(x,y)] ⇒ [∃y Loves(y,x)] to CNF.  
   **Steps:** Eliminate ⇒; Move ¬ inwards; Standardize; Skolemize; Drop ∀; Distribute ∨. Result: ¬Animal(y) ∨ Loves(x,y) ∨ Loves(f(x),x) (after Skolemization).

3. **Q:** Compute P(Burglary|JohnCalls=true, MaryCalls=true) from Bayes net given CPTs.  
   **Steps:** Multiply P(J|A)P(M|A)P(A|B,E)P(B)P(E) for each combination of A and E.

### Diagram Label

1. **Q:** Draw and label the simple reflex agent architecture.  
   **Label:** Sensors → (What the world is like now) → Condition-action rules → (What action I should do) → Actuators → Environment → (feedback loop)

2. **Q:** Draw a Bayesian network for the Burglary/Earthquake/Alarm domain and label all CPTs.  
   **Nodes:** Burglary → Alarm ← Earthquake; Alarm → JohnCalls, Alarm → MaryCalls. CPTs at each node.

3. **Q:** Label the parts of an MCTS iteration on a game tree.  
   **Labels:** Selection (traverse tree using UCT), Expansion (add child node 0/0), Simulation (playout to terminal), Back-propagation (update wins/playouts up the tree).

### Essay / Long-Form

1. **Q:** Compare the Turing test approach with the rational agent approach to defining AI. Which has been more influential and why?  
   **Key points:** Turing test (acting humanly, requires NLP+KR+reasoning+ML+vision+robotics, 6 disciplines) vs rational agent (maximize expected performance, mathematically well-defined). Rational agent more general (includes reflex actions), more amenable to formalization, has prevailed as "standard model". Rational agent approach allows deriving provably optimal designs.

2. **Q:** Explain how a Bayesian network represents a probability distribution. Why is this more efficient than a full joint distribution? What inference algorithms exist and when is each appropriate?  
   **Key points:** DAG + CPTs; conditional independence (non-descendants given parents); full joint O(2^n), Bayes net O(n·2^k). Exact: enumeration (small n), variable elimination (medium), clustering/join tree (all posteriors). Approximate: rejection sampling (rare evidence fails), likelihood weighting (better for upstream evidence), Gibbs MCMC (best for downstream evidence, can be slow with deterministic relations).

3. **Q:** Discuss the value alignment problem. Why does the standard model fail? What technical approaches address it?  
   **Key points:** Standard model assumes fixed known objective; King Midas problem; machines pursuing fixed objectives can misbehave (chess-playing example: cheating, hypnotizing). Solutions: IRL (learn from demonstration), assistance games (model preference uncertainty, act cautiously, ask permission), provably beneficial agents (Norbert Wiener's warning: "be quite sure the purpose put into the machine is the purpose we really desire").

---
""")

print("Done!")
lines = sum(1 for _ in open(OUT, encoding="utf-8"))
print(f"Study guide written to {OUT}")
print(f"Total lines: {lines}")
