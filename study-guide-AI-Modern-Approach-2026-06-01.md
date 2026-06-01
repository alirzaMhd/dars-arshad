# Study Guide: Artificial Intelligence — A Modern Approach (4th Edition)

> **Generated**: 2026-06-01. **Subject**: Computer Science / Artificial Intelligence.
> **Authors**: Stuart Russell & Peter Norvig. **Coverage**: Comprehensive (28 chapters + appendices).
> **Exam format**: Mixed (MCQ, Short Answer, Problem-solving, Essay).

---

## Chapter-by-Chapter Breakdown


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


---

# COMPREHENSIVE EXAMINATION NOTES
## Artificial Intelligence: A Modern Approach (Russell & Norvig) — Chapters 2, 3, 4

---

# CHAPTER 2: INTELLIGENT AGENTS (lines 2004–3155)

---

## 1. NAMED ENTITIES — Every Term/Concept with Definition

| Term | Definition |
|------|-----------|
| **Agent** | Anything that can be viewed as perceiving its environment through sensors and acting upon that environment through actuators |
| **Sensor** | Device that detects environmental state (cameras, microphones, touchscreens, etc.) |
| **Actuator** | Device that acts on the environment (motors, displays, speakers, etc.) |
| **Percept** | The content an agent's sensors are perceiving at a given moment |
| **Percept sequence** | The complete history of everything the agent has ever perceived |
| **Agent function** | Mathematical mapping from any given percept sequence to an action (abstract description) |
| **Agent program** | Concrete implementation of the agent function, running within some physical system |
| **Rational agent** | "For each possible percept sequence, a rational agent should select an action that is expected to maximize its performance measure, given the evidence provided by the percept sequence and whatever built-in knowledge the agent has" |
| **Consequentialism** | Ethical position that evaluates agent behavior by its consequences |
| **Performance measure** | Criterion that evaluates any given sequence of environment states |
| **Omniscience** | Knowing the actual outcome of actions (impossible in reality) |
| **Information gathering** | Doing actions in order to modify future percepts |
| **Learning** | Modifying behavior based on percepts to compensate for partial/incorrect prior knowledge |
| **Autonomy** | Agent's ability to rely on its own percepts and learning rather than designer's prior knowledge |
| **Task environment** | The "problem" to which rational agents are the "solution" |
| **PEAS** | Performance, Environment, Actuators, Sensors — the four components of task environment specification |
| **Software agent / Softbot** | Agent operating in virtual environments |
| **Environment class** | A set of environments from which individual environments are drawn for evaluation |
| **Agent architecture** | The computing device with physical sensors/actuators on which the agent program runs |
| **Agent function** | `agent = architecture + program` |
| **Condition–action rule** | Rule mapping percept to action (if-then rule, production, situation–action rule) |
| **Simple reflex agent** | Agent that selects actions based only on current percept, ignoring percept history |
| **Model-based agent** | Agent that maintains internal state using a transition model and sensor model |
| **Transition model** | Knowledge about how the world evolves over time — effects of agent's actions and independent changes |
| **Sensor model** | Knowledge about how world state is reflected in agent's percepts |
| **Goal** | Description of situations that are desirable |
| **Goal-based agent** | Agent that combines goal information with model to choose actions that achieve the goal |
| **Utility** | Measure of how happy/desirable a state is; used for comparing world states |
| **Utility function** | Internalization of the performance measure; maps states to numeric utility |
| **Expected utility** | The utility the agent expects to derive on average, given probabilities and utilities of each outcome |
| **Model-free agent** | Agent that learns what action is best without learning how actions change the environment |
| **Learning element** | Component responsible for making improvements in a learning agent |
| **Performance element** | Component responsible for selecting external actions (the whole agent in non-learning designs) |
| **Critic** | Component that tells learning element how well the agent is doing relative to fixed performance standard |
| **Problem generator** | Component that suggests actions leading to new and informative experiences (exploration) |
| **Reward / Penalty** | Direct feedback on quality of agent's behavior from the performance standard |
| **Atomic representation** | Each state is indivisible — a black box with no internal structure |
| **Factored representation** | State split into a fixed set of variables/attributes, each with a value |
| **Variable / Attribute** | A dimension of a factored state that can take a value |
| **Value** | The specific assignment to a variable |
| **Structured representation** | States include objects with attributes and relationships to other objects |
| **Expressiveness** | The axis along which atomic, factored, and structured representations lie — more expressive captures more concisely |
| **Localist representation** | One-to-one mapping between concepts and memory locations |
| **Distributed representation** | Concept representation spread over many memory locations; each location participates in multiple concepts |
| **Controller** | In control theory, analogous to an agent in AI |
| **Autonomic computing** | Computer systems/networks that monitor and control themselves with perceive–act loop and ML |
| **Internal state** | Agent's maintained knowledge reflecting unobserved aspects of current state |

---

## 2. SEQUENTIAL PROCESSES — All Step-by-Step Procedures

### Problem-Solving Process (Four-Phase):
1. **Goal formulation**: Adopt goal; organize behavior by limiting objectives and actions
2. **Problem formulation**: Devise description of states and actions (abstract model)
3. **Search**: Simulate action sequences in model until finding sequence reaching goal (the solution)
4. **Execution**: Execute actions in solution one at a time

### TABLE-DRIVEN-AGENT (Figure 2.7):
1. Append current percept to end of percept sequence
2. Look up action in table indexed by percept sequence
3. Return action

### REFLEX-VACUUM-AGENT (Figure 2.8):
1. If current square is dirty → Suck
2. Else if location is A → move Right
3. Else if location is B → move Left

### SIMPLE-REFLEX-AGENT (Figure 2.10):
1. Interpret input percept to generate abstracted state description
2. Match state description against condition-action rules
3. Return action from first matching rule

### MODEL-BASED-REFLEX-AGENT (Figure 2.12):
1. Update internal state using: UPDATE-STATE(state, action, percept, transition model, sensor model)
2. Match state against condition-action rules
3. Return action from first matching rule

### Learning Agent Cycle (Figure 2.15):
1. Performance element selects external actions (percepts → actions)
2. Critic evaluates performance against fixed standard
3. Learning element uses critic feedback to modify performance element
4. Problem generator suggests exploratory actions for new information

---

## 3. HIERARCHIES/CLASSIFICATIONS

### Four Basic Agent Program Types (increasing sophistication):
1. **Simple reflex agents** — base decisions on current percept only
2. **Model-based reflex agents** — maintain internal state via transition + sensor models
3. **Goal-based agents** — have goal information to select actions that achieve goals
4. **Utility-based agents** — have utility function to maximize expected happiness

### Three Representation Types (atomic → factored → structured):
| Property | Atomic | Factored | Structured |
|----------|--------|----------|------------|
| State structure | Black box, no internal structure | Vector of attribute values | Objects with attributes and relationships |
| Example use | Search, game-playing, HMMs, MDPs | CSP, propositional logic, planning, Bayes nets | Relational DBs, FOL, NL understanding |
| Expressiveness | Least | Medium | Most |
| Conciseness | Least (e.g., chess = 10^38 pages) | Medium (thousands of pages) | Most (page or two for chess) |

### Agent vs. Non-agent Spectrum:
AI operates at the end where artifacts have significant computational resources and nontrivial decision making

### Localist vs. Distributed Representation:
| Localist | Distributed |
|----------|-------------|
| One-to-one concept→memory mapping | Concept spread over many memory locations |
| Arbitrary mapping | Each concept = point in multidimensional space |
| Garbling bits can confuse unrelated concepts | Garbling moves to nearby (similar) meaning |
| — | More robust against noise and information loss |

---

## 4. COMPARISONS/TRADE-OFFS

### Rationality vs. Omniscience vs. Perfection:
- **Rationality**: Maximizes *expected* performance given percept sequence
- **Omniscience**: Knows actual outcomes (impossible)
- **Perfection**: Maximizes *actual* performance (unattainable by design)

### Reflex vs. Goal-based Agents:
| Reflex | Goal-based |
|--------|------------|
| Condition-action rules map percepts→actions directly | Decisions involve future: "What if I do X?" |
| Has no idea *why* it acts | Knows why (to achieve goal) |
| Rules work for only one destination | Can change destination by specifying new goal |
| Appears more efficient | Appears less efficient but more flexible |
| Knowledge implicit in rules | Knowledge explicitly represented and modifiable |

### Goals vs. Utility:
| Goals | Utility |
|-------|---------|
| Crude binary distinction (happy/unhappy) | Continuous comparison |
| Cannot handle conflicting goals | Specifies tradeoffs for conflicting goals |
| Cannot weigh likelihood vs. importance | Weighs probability × utility |

### Table-Driven vs. Programmed Agent:
| Table-Driven | Programmed |
|--------------|------------|
| Impractically large (exponential in percepts) | Compact program |
| Requires designer to precompute every entry | Learns or derives behavior |
| Example: 10^600 billion entries for 1 hour taxi video | Example: small rule set or circuit |

---

## 5. FORMULAS & EQUATIONS

Size of lookup table for agent function:
- Total entries = Σ_{t=1}^{T} |P|^t, where P = set of possible percepts, T = agent lifetime

---

## 6. RULES, LAWS & THEOREMS

### Key Principle for Performance Measure Design:
"It is better to design performance measures according to what one actually wants to be achieved in the environment, rather than according to how one thinks the agent should behave." (p. 52)

### Wiener's Warning (from Chapter 1, p. 33):
The purpose put into the machine must be the purpose we really desire (avoid King Midas problem).

### Four Determinants of Rationality (at any given time):
1. Performance measure defining success criterion
2. Agent's prior knowledge of environment
3. Actions agent can perform
4. Agent's percept sequence to date

### Rationality Definition (p. 53):
"For each possible percept sequence, a rational agent should select an action that is expected to maximize its performance measure, given the evidence provided by the percept sequence and whatever built-in knowledge the agent has."

---

## 7. DATA STRUCTURES & TYPES

### Agent Program Skeleton:
```
agent program(current percept) → action
```
- Takes current percept as input (only what's available from environment)
- Must remember if decision depends on entire percept history

### Agent Architecture Equation:
```
agent = architecture + program
```
- Architecture provides sensors → program, runs program, feeds program's actions → actuators

### Node Components (preview for Chapter 3):
- STATE
- PARENT
- ACTION
- PATH-COST (also denoted g(node))

---

## 8. VISUAL PATTERNS (described in text, can be re-drawn)

### Figure 2.1: Agent-Environment Interaction
```
[Sensors] → Agent → [Actuators] → Environment → [Percepts] → Agent
```
Rectangle with arrows: Environment ↔ Agent through Percepts/Actions

### Figure 2.2: Two-Cell Vacuum World
```
[A] [B]
```
Two adjacent squares; each can be clean or dirty.

### Figure 2.3: Partial Agent Function Table for Vacuum World
| Percept sequence | Action |
|-----------------|--------|
| [A,Clean] | Right |
| [A,Dirty] | Suck |
| [B,Clean] | Left |
| [B,Dirty] | Suck |
| [A,Clean],[A,Clean] | Right |
| ... | ... |

### Figure 2.9: Simple Reflex Agent Structure
```
Percept → Sensors → [INTERPRET-INPUT] → "what the world is like now" → [RULE-MATCH] → "what action I should do" → Actuators → Action
                                             ↑
                                    Condition-action rules (background knowledge)
```

### Figure 2.11: Model-Based Reflex Agent Structure
```
Percept → Sensors → [UPDATE-STATE] → "what the world is like now" → [RULE-MATCH] → "what action I should do" → Actuators → Action
                         ↑                                       ↑
                [Transition model]                      [Condition-action rules]
                [Sensor model]
                "How the world evolves"
                "What my actions do"
```

### Figure 2.13: Goal-Based Agent Structure
Same as model-based but adds: "What it will be like if I do action A" + "Goals" → choice of action

### Figure 2.14: Utility-Based Agent Structure
Same as goal-based but adds: "How happy I will be in such a state" + "Utility" → action maximizing expected utility

### Figure 2.15: Learning Agent
```
Performance standard → Critic → feedback → Learning element → changes → Performance element
                           ↑                                  ↑
                      [Problem generator] → exploratory actions
```
Separate components: learning element, critic, performance element, problem generator

### Figure 2.16: Three Representation Types
(a) Atomic: circles (B, C) with arrows (states are black boxes)
(b) Factored: boxes with internal attributes (vectors)
(c) Structured: objects with attributes and relationships (network diagram)

---

## 9. EDGE CASES/EXCEPTIONS/TRAPS

### King Midas Problem (Wrong Objective):
Performance measure may be specified incorrectly → agent optimizes unintended behavior. Example: vacuum cleaner rewarded for dirt cleaned in 8 hours might dump and re-clean dirt.

### Calculator as Agent:
Notion of agent is a tool for analysis, not absolute characterization; viewing a calculator as an agent would not aid understanding.

### Infinite Loops for Simple Reflex Agents in Partially Observable Environments:
Vacuum agent without location sensor: if [Clean], Left fails forever if starts at A; Right fails forever if at B → infinite loop.

### Escape via Randomization:
Randomized simple reflex agent can escape infinite loops; e.g., flip coin for Left/Right when [Clean].

### Multiple Optimal Solutions:
Two agents achieving same average cleanliness — one mediocre always, the other energetic with long breaks — raises philosophical questions about which is "better."

### Dung Beetle Failure Mode:
Built-in assumption violated → continues task with nonexistent dung ball, never noticing missing.

### Sphex Wasp Failure Mode:
Innate plan cannot be modified; if caterpillar is moved while wasp checks burrow, it reverts to earlier step indefinitely.

### Model-Free Agents:
Not all utility-based agents are model-based; some learn what action is best without learning how action changes environment.

---

## 10. EMPIRICAL EVIDENCE/KEY RESULTS

### Lookup Table Size Comparisons:
- Automated taxi (1 hour): >10^600 billion entries
- Chess: ≥10^150 entries
- Observable universe atoms: <10^80
- Conclusion: Table-driven approach is physically impossible

### Vacuum World State Space Size:
- 2 cells: 2 × 2 × 2 = 8 states
- n cells: n × 2^n states

### Example of Small Program Replacing Huge Table:
Pre-1970s square root tables replaced by 5-line Newton's method program

---

## 11. CROSS-CHAPTER DEPENDENCIES

- **Chapters 3-5**: Search and game-playing algorithms (atomic representations)
- **Chapter 6**: Constraint satisfaction (factored)
- **Chapter 7**: Propositional logic (factored)
- **Chapter 8, 9, 10**: First-order logic (structured)
- **Chapter 11**: Planning (factored)
- **Chapters 12-16**: Bayesian networks (factored), probability models (structured)
- **Chapter 14**: Hidden Markov models (atomic)
- **Chapter 16**: Utility theory, decision making under uncertainty, information gathering
- **Chapter 17**: Markov decision processes (atomic)
- **Chapters 19-22**: Learning algorithms, reinforcement learning
- **Chapter 18**: Multiagent decision making (utility theory)
- **Chapters 22, 26**: Model-free agents
- **Chapters 23, 24**: Natural language processing (structured)
- **Chapters 25, 26**: Sensors and actuators

---

## 12. DATES & PEOPLE

- **Aristotle**: *Nicomachean Ethics* — practical reasoning origins
- **McCarthy (1958)**: "Programs with Common Sense" — practical reasoning
- **Norbert Wiener**: Warning about putting wrong purpose into machines
- **Genesereth & Nilsson (1987)**: First AI text emphasizing whole agents
- **Jon Doyle (1983)**: Predicted rational agent design as core AI mission
- **Turing (1950)**: Proposed building learning machines instead of hand-programming
- **Newell & Simon (1972)**: *Human Problem Solving*
- **Michael Bratman (1987)**: Desires, intentions theory of agents
- **Samuel (1959, 1967)**: Learning program for checkers
- **Dung Beetle Ecology (Hanski & Cambefort, 1991)**: Source of dung beetle example

---

## 13. PROOF & ARGUMENT PATTERNS

### Why Table-Driven Agent is Doomed (three arguments):
1. **Space**: Table size physically impossible (exceeds atoms in universe)
2. **Time**: Designer cannot create table; agent cannot learn all entries
3. **Impossibility proof**: For taxi with 70 MB/s video input → >10^600 billion entries for one hour

### Reduction from Chess Rules to Representations:
"Rules of chess can be written in a page or two of structured representation (FOL) but require thousands of pages in factored (propositional logic) and ~10^38 pages in atomic (finite-state automata)"

---

## 14. DESIGN PARADIGMS/META-METHODS

### Agent Design as Central Theme:
"The job of AI is to design an agent program that implements the agent function — the mapping from percepts to actions."

### Modularity in Multiagent Systems:
Collection of agent programs designed to work together shares no internal state, communicates only through environment; can sometimes prove optimality equals monolithic design.

---

## 15. CASE STUDIES/CLASSIC EXAMPLES

### Vacuum-Cleaner World (throughout chapter):
- Two squares (A, B), each dirty or clean
- Agent perceives location + dirt; actions: Left, Right, Suck
- Simple reflex agent function: if dirty → Suck; else → move
- Performance measure: 1 point per clean square per time step

### Automated Taxi Driver (PEAS Example):
- **Performance**: Safe, fast, legal, comfortable trip; maximize profits; minimize impact
- **Environment**: Roads, traffic, police, pedestrians, customers, weather
- **Actuators**: Steering, accelerator, brake, signal, horn, display, speech
- **Sensors**: Cameras, radar, speedometer, GPS, engine sensors, accelerometer, microphones, touchscreen

### Dung Beetle Example:
Built-in assumption violated → continues pantomiming plugging nest with nonexistent dung ball

### Sphex Wasp Example:
Entomologist moves caterpillar → wasp reverts to "drag caterpillar" step endlessly, unable to modify innate plan

---

## 16. ETHICS

### King Midas Problem / Purpose Alignment:
"Recalling Norbert Wiener's warning to ensure that 'the purpose put into the machine is the purpose which we really desire'... it can be quite hard to formulate a performance measure correctly."

### Consequentialism:
AI generally uses consequentialist ethics — evaluating behavior by consequences

### Performance Measure as Ethical Choice:
"Which is better — a reckless life of highs and lows, or a safe but humdrum existence? Which is better — an economy where everyone lives in moderate poverty, or one in which some live in plenty while others are very poor?"

### Unknown Preferences:
When designing software for different users with different preferences, agents must reflect initial uncertainty about true performance measure and learn.

---

## 17. END-OF-CHAPTER MATERIAL

### Summary (Key Points):
1. Agent = perceives + acts; agent function maps percept sequence → action
2. Performance measure evaluates behavior; rational agent maximizes expected performance
3. Task environment = PEAS (Performance, Environment, Actuators, Sensors)
4. Environments vary along 7 dimensions: observable, agents, deterministic, episodic, static, discrete, known
5. Risk of optimizing wrong objective when performance measure unknown/hard to specify
6. Four agent designs: simple reflex, model-based reflex, goal-based, utility-based
7. All agents can improve through learning

### 7 Dimensions of Task Environments:
| Dimension | Values |
|-----------|--------|
| Observable | Fully / Partially / Unobservable |
| Agents | Single-agent / Multiagent (competitive / cooperative) |
| Determinism | Deterministic / Nondeterministic / Stochastic |
| Episodic | Episodic / Sequential |
| Dynamics | Static / Dynamic / Semidynamic |
| Discreteness | Discrete / Continuous |
| Knowledge | Known / Unknown |

### PEAS Table Examples (Figure 2.4 & 2.5):
- Medical diagnosis system
- Satellite image analysis
- Part-picking robot
- Refinery controller
- Interactive English tutor
- Taxi driver

### Task Environment Properties Table (Figure 2.6):
| Environment | Observable | Agents | Deterministic | Episodic | Static | Discrete |
|-------------|-----------|--------|---------------|----------|--------|----------|
| Crossword | Fully | Single | Deter. | Sequential | Static | Discrete |
| Chess (clock) | Fully | Multi | Deter. | Sequential | Semi | Discrete |
| Poker | Partially | Multi | Stochastic | Sequential | Static | Discrete |
| Backgammon | Fully | Multi | Stochastic | Sequential | Static | Discrete |
| Taxi | Partially | Multi | Stochastic | Sequential | Dynamic | Continuous |
| Medical diagnosis | Partially | Single | Stochastic | Sequential | Dynamic | Continuous |
| Image analysis | Fully | Single | Deter. | Episodic | Semi | Continuous |
| Part-picking robot | Partially | Single | Stochastic | Episodic | Dynamic | Continuous |
| Refinery controller | Partially | Single | Stochastic | Sequential | Dynamic | Continuous |
| English tutor | Partially | Multi | Stochastic | Sequential | Dynamic | Discrete |

### Hardest Case: Partially observable, multiagent, nondeterministic, sequential, dynamic, continuous, unknown

---

# CHAPTER 3: SOLVING PROBLEMS BY SEARCHING (lines 3156–5217)

---

## 1. NAMED ENTITIES — Every Term/Concept with Definition

| Term | Definition |
|------|-----------|
| **Problem-solving agent** | Agent that considers action sequences forming a path to a goal state |
| **Search** | Computational process of considering action sequences |
| **Goal formulation** | Agent adopts goal; organizes behavior by limiting objectives and actions |
| **Problem formulation** | Devise description of states and actions (abstract model) |
| **Search** (as phase) | Simulate action sequences in model to find solution |
| **Solution** | Sequence of actions reaching the goal |
| **Execution** | Perform actions in solution one at a time |
| **Open-loop system** | Agent ignores percepts during execution; assumes model correct |
| **Closed-loop** | Agent monitors percepts during execution |
| **State space** | Set of possible states the environment can be in |
| **Initial state** | State agent starts in |
| **Goal states** | Set of one or more states satisfying goal condition |
| **Action** | Operation available to agent; ACTIONS(s) returns finite set applicable in s |
| **Applicable** | An action that can be executed in a given state |
| **Transition model** | RESULT(s,a) returns state from doing action a in state s |
| **Action cost function** | c(s,a,s') — numeric cost of applying action a in s to reach s' |
| **Path** | Sequence of actions |
| **Optimal solution** | Solution with lowest path cost among all solutions |
| **Graph** | Representation of state space: vertices = states, directed edges = actions |
| **Abstraction** | Process of removing irrelevant detail from representation |
| **Level of abstraction** | Appropriate detail for problem; too detailed → never finds solution |
| **Standardized problem** | Benchmark problem with concise, exact description |
| **Real-world problem** | Problem whose solutions people actually use; idiosyncratic formulation |
| **Grid world** | Two-dimensional rectangular array of cells for agent movement |
| **Sokoban puzzle** | Grid world where agent pushes boxes to storage locations |
| **Sliding-tile puzzle** | Tiles arranged in grid with blank space(s); tiles slide into blank |
| **8-puzzle** | 3×3 grid with 8 numbered tiles + 1 blank (9!/2 = 181,440 reachable states) |
| **15-puzzle** | 4×4 grid (16!/2 ≈ 10^13 reachable states) |
| **Touring problem** | Must visit set of locations (not just reach single goal) |
| **Traveling salesperson problem (TSP)** | Touring problem visiting every city; find tour with cost < C |
| **VLSI layout** | Positioning components and connections on chip |
| **Robot navigation** | Generalized route-finding for robots in continuous space |
| **Automatic assembly sequencing** | Find order to assemble parts of an object |
| **Protein design** | Find amino acid sequence that folds into desired 3D protein |
| **Search algorithm** | Takes search problem as input; returns solution or failure |
| **Node** | Element in search tree corresponding to a state; has parent, children |
| **Expand** | Apply ACTIONS to a state, generate child nodes |
| **Child node / Successor node** | Node generated by applying an action to a parent state |
| **Parent node** | Node whose expansion generated this node |
| **Frontier** | Set of nodes generated but not yet expanded (open list) |
| **Reached** | States for which a node has been generated (expanded or not) |
| **Separator** | Frontier separates interior (expanded) from exterior (unreached) |
| **Best-first search** | Search that expands node with minimum f(n) value |
| **Evaluation function** | f(n) — used to order nodes on frontier |
| **Queue** | Data structure for frontier: priority queue, FIFO queue, LIFO queue |
| **Priority queue** | Pops node with minimum f(n) value |
| **FIFO queue** | First-in-first-out; pops oldest node |
| **LIFO queue / Stack** | Last-in-first-out; pops newest node |
| **Repeated state** | State appearing multiple times in search tree |
| **Cycle / Loopy path** | Path returning to previously visited state (e.g., Arad→Sibiu→Arad) |
| **Redundant path** | Multiple paths to same state (one may be worse) |
| **Graph search** | Algorithm that checks for and eliminates redundant paths |
| **Tree-like search** | Algorithm that does not check for redundant paths |
| **Completeness** | Guaranteed to find solution when one exists, report failure otherwise |
| **Cost optimality** | Find solution with lowest path cost |
| **Time complexity** | How long to find solution (states/actions considered) |
| **Space complexity** | How much memory needed |
| **Systematic** | Search that can eventually reach any state connected to initial state |
| **Depth** | Number of actions in a path |
| **Branching factor** | Number of successors of a node |
| **Uninformed search** | No clue about how close a state is to goal |
| **Informed search** | Uses domain-specific hints (heuristics) |
| **Breadth-first search** | Expands shallowest nodes first; systematic, complete |
| **Early goal test** | Test if node is solution as soon as generated |
| **Late goal test** | Test if node is solution only when popped from queue |
| **Dijkstra's algorithm / Uniform-cost search** | Best-first search with f(n) = path cost g(n) |
| **Depth-first search** | Always expands deepest node in frontier first |
| **Backtracking search** | DFS variant generating one successor at a time; modifies state in place |
| **Depth-limited search** | DFS with depth limit ℓ; nodes at depth ℓ treated as having no successors |
| **Diameter** | Maximum number of actions needed between any two states |
| **Iterative deepening search** | Repeated depth-limited search with increasing limits |
| **Bidirectional search** | Simultaneous forward from initial + backward from goal; frontiers meet |
| **Heuristic function** | h(n) = estimated cost of cheapest path from node n to a goal |
| **Straight-line distance** | h_SLD — Euclidean distance heuristic for route finding |
| **Greedy best-first search** | Expands node with lowest h(n) first |
| **A* search** | f(n) = g(n) + h(n) — best-first with path cost + heuristic |
| **Admissible heuristic** | Never overestimates cost to reach goal (optimistic) |
| **Consistency / Monotonic heuristic** | h(n) ≤ c(n,a,n') + h(n') for all n and successors n' (triangle inequality) |
| **Triangle inequality** | Side of triangle ≤ sum of other two sides |
| **Contour** | Set of nodes with f(n) ≤ some value |
| **Surely expanded nodes** | Nodes with f(n) < C* that A* always expands |
| **Optimally efficient** | A* expands minimal number of nodes among algorithms using same heuristic |
| **Pruning** | Eliminating possibilities without examining them |
| **Satisficing solution** | "Good enough" but not optimal |
| **Inadmissible heuristic** | May overestimate cost to goal |
| **Detour index** | Multiplier applied to straight-line distance (1.2–1.6 typical) |
| **Weighted A* search** | f(n) = g(n) + W × h(n), W > 1 |
| **Bounded suboptimal search** | Solution guaranteed within factor W of optimal |
| **Bounded-cost search** | Solution cost less than constant C |
| **Unbounded-cost search** | Accept any cost solution, find quickly |
| **Speedy search** | Greedy best-first using estimated number of actions (ignoring cost differences) |
| **Beam search** | Limit frontier to k best nodes (incomplete, suboptimal) |
| **Iterative-deepening A* (IDA*)** | Iterative deepening with f-cost cutoff |
| **Recursive best-first search (RBFS)** | Mimics best-first using linear space; backs up f-values |
| **Backed-up value** | Best f-value of children, stored at parent when subtree is forgotten |
| **MA* / SMA*** | Memory-bounded A* variants; drops worst leaf when memory full |
| **Thrashing** | Repeated regeneration of same nodes due to memory limitations |
| **Front-to-end search** | Heuristic estimates distance to goal/start |
| **Front-to-front search** | Attempts to estimate distance to other frontier |
| **Effective branching factor (b*)** | Branching factor a uniform tree of depth d would need to contain N+1 nodes: N+1 = 1+b*+(b*)²+...+(b*)^d |
| **Effective depth** | A* with heuristic h reduces effective depth by constant k_h |
| **Domination** | Heuristic h₂ dominates h₁ if h₂(n) ≥ h₁(n) for all n |
| **Relaxed problem** | Problem with fewer restrictions on actions; supergraph of original |
| **Subproblem** | Part of problem; cost of optimal subproblem solution is lower bound |
| **Pattern database** | Stores exact solution costs for every possible subproblem instance |
| **Disjoint pattern databases** | Non-overlapping subproblem costs that can be summed |
| **Precomputation** | Computing optimal path costs offline, amortized over many queries |
| **Landmark point** | Few (10–20) vertices used to compute heuristic via stored distances |
| **Shortcut** | Artificial edge defining optimal multi-action path |
| **Differential heuristic** | h_DH(n) = max_L |C*(n,L) − C*(goal,L)| — admissible landmark heuristic |
| **Metalevel state space** | Internal computational state of a search program |
| **Object-level state space** | The original problem space (e.g., map of Romania) |
| **Metalevel learning** | Learning from search experience to avoid unpromising subtrees |
| **Feature** | Relevant characteristic of a state for predicting heuristic value |
| **Linear combination heuristic** | h(n) = c₁x₁(n) + c₂x₂(n) |
| **Iterative expansion (IE)** | Algorithm similar to RBFS |
| **Branch-and-bound** | Operations research technique related to A* |
| **Coarse-to-fine search** | Hierarchical landmark approach with exponential speedup |

---

## 2. SEQUENTIAL PROCESSES — All Step-by-Step Algorithm Descriptions

### BEST-FIRST-SEARCH (Figure 3.7):
```
function BEST-FIRST-SEARCH(problem, f) returns a solution node or failure
  node ← NODE(STATE = problem.INITIAL)
  frontier ← priority queue ordered by f, with node as element
  reached ← lookup table with key problem.INITIAL and value node
  while not IS-EMPTY(frontier) do
    node ← POP(frontier)
    if problem.IS-GOAL(node.STATE) then return node
    for each child in EXPAND(problem, node) do
      s ← child.STATE
      if s not in reached or child.PATH-COST < reached[s].PATH-COST then
        reached[s] ← child
        add child to frontier
  return failure
```

### EXPAND function (Figure 3.7):
```
function EXPAND(problem, node) yields nodes
  s ← node.STATE
  for each action in problem.ACTIONS(s) do
    s' ← problem.RESULT(s, action)
    cost ← node.PATH-COST + problem.ACTION-COST(s, action, s')
    yield NODE(STATE=s', PARENT=node, ACTION=action, PATH-COST=cost)
```

### BREADTH-FIRST-SEARCH (Figure 3.9):
```
function BREADTH-FIRST-SEARCH(problem) returns a solution node or failure
  node ← NODE(problem.INITIAL)
  if problem.IS-GOAL(node.STATE) then return node
  frontier ← FIFO queue with node as element
  reached ← {problem.INITIAL}
  while not IS-EMPTY(frontier) do
    node ← POP(frontier)
    for each child in EXPAND(problem, node) do
      s ← child.STATE
      if problem.IS-GOAL(s) then return child
      if s not in reached then
        add s to reached
        add child to frontier
  return failure
```

### UNIFORM-COST-SEARCH (Figure 3.9):
```
function UNIFORM-COST-SEARCH(problem) returns a solution node or failure
  return BEST-FIRST-SEARCH(problem, PATH-COST)
```

### ITERATIVE-DEEPENING-SEARCH (Figure 3.12):
```
function ITERATIVE-DEEPENING-SEARCH(problem) returns a solution node or failure
  for depth = 0 to ∞ do
    result ← DEPTH-LIMITED-SEARCH(problem, depth)
    if result ≠ cutoff then return result
```

### DEPTH-LIMITED-SEARCH (Figure 3.12):
```
function DEPTH-LIMITED-SEARCH(problem, ℓ) returns a node or failure or cutoff
  frontier ← LIFO queue (stack) with NODE(problem.INITIAL) as element
  result ← failure
  while not IS-EMPTY(frontier) do
    node ← POP(frontier)
    if problem.IS-GOAL(node.STATE) then return node
    if DEPTH(node) > ℓ then
      result ← cutoff
    else if not IS-CYCLE(node) do
      for each child in EXPAND(problem, node) do
        add child to frontier
  return result
```

### BIBF-SEARCH (Bidirectional Best-First, Figure 3.14):
```
function BIBF-SEARCH(problem_F, f_F, problem_B, f_B) returns a solution node or failure
  node_F ← NODE(problem_F.INITIAL)
  node_B ← NODE(problem_B.INITIAL)
  frontier_F ← priority queue ordered by f_F, with node_F as element
  frontier_B ← priority queue ordered by f_B, with node_B as element
  reached_F ← lookup table with key node_F.STATE → node_F
  reached_B ← lookup table with key node_B.STATE → node_B
  solution ← failure
  while not TERMINATED(solution, frontier_F, frontier_B) do
    if f_F(TOP(frontier_F)) < f_B(TOP(frontier_B)) then
      solution ← PROCEED(F, problem_F, frontier_F, reached_F, reached_B, solution)
    else
      solution ← PROCEED(B, problem_B, frontier_B, reached_B, reached_F, solution)
  return solution
```

### PROCEED (Figure 3.14):
```
function PROCEED(dir, problem, frontier, reached, reached2, solution) returns a solution
  node ← POP(frontier)
  for each child in EXPAND(problem, node) do
    s ← child.STATE
    if s not in reached or PATH-COST(child) < PATH-COST(reached[s]) then
      reached[s] ← child
      add child to frontier
      if s in reached2 then
        solution2 ← JOIN-NODES(dir, child, reached2[s])
        if PATH-COST(solution2) < PATH-COST(solution) then
          solution ← solution2
  return solution
```

### RECURSIVE-BEST-FIRST-SEARCH (Figure 3.22):
```
function RECURSIVE-BEST-FIRST-SEARCH(problem) returns a solution or failure
  solution, fvalue ← RBFS(problem, NODE(problem.INITIAL), ∞)
  return solution

function RBFS(problem, node, flimit) returns a solution or failure, and new f-cost limit
  if problem.IS-GOAL(node.STATE) then return node
  successors ← LIST(EXPAND(node))
  if successors is empty then return failure, ∞
  for each s in successors do
    s.f ← max(s.PATH-COST + h(s), node.f)
  while true do
    best ← node in successors with lowest f-value
    if best.f > flimit then return failure, best.f
    alternative ← second-lowest f-value among successors
    result, best.f ← RBFS(problem, best, min(flimit, alternative))
    if result ≠ failure then return result, best.f
```

---

## 3. HIERARCHIES/CLASSIFICATIONS

### Problem Components (5 parts):
1. **States** (set of possible states)
2. **Initial state** 
3. **Goal states** (one, small set, or property-based)
4. **Actions** (ACTIONS(s) returns finite applicable set)
5. **Transition model** (RESULT(s,a))
6. **Action cost function** (c(s,a,s'))

### Search Algorithm Types:
| Uninformed | Informed |
|------------|----------|
| Breadth-first | Greedy best-first |
| Uniform-cost (Dijkstra) | A* |
| Depth-first | Weighted A* |
| Depth-limited | IDA* |
| Iterative deepening | RBFS |
| Bidirectional | SMA* |
| | Beam search |

### Four Evaluation Criteria (Section 3.3.4):
1. **Completeness**
2. **Cost optimality**
3. **Time complexity**
4. **Space complexity**

### Three Queue Types:
1. **Priority queue** — best-first search
2. **FIFO queue** — breadth-first search
3. **LIFO queue (stack)** — depth-first search

### Three Approaches to Redundant Paths:
1. **Graph search**: Remember all reached states; detect all redundant paths
2. **Tree-like search**: Don't track redundant paths (saves memory)
3. **Cycle detection**: Check parent chain for cycles (compromise)

### Three Types of Search Problems (by optimality):
| Type | Guarantee | Example |
|------|-----------|---------|
| Bounded suboptimal | Within factor W of optimal | Weighted A* |
| Bounded-cost | Cost < constant C | — |
| Unbounded-cost | Any cost, fast | Speedy search |

### Weighted A* as Generalization:
| Algorithm | f(n) | W |
|-----------|------|---|
| A* | g(n) + h(n) | W=1 |
| Uniform-cost | g(n) | W=0 |
| Greedy best-first | h(n) | W=∞ |
| Weighted A* | g(n) + W×h(n) | 1<W<∞ |

---

## 4. COMPARISONS/TRADE-OFFS

### Breadth-First vs. Depth-First:
| Criterion | BFS | DFS |
|-----------|-----|-----|
| Completeness | Yes (finite b) | No (infinite paths, cycles) |
| Cost-optimal | Yes (uniform costs) | No |
| Time | O(b^d) | O(b^m) |
| Space | O(b^d) | O(bm) — linear! |
| Structure | Expanding sphere | Single radius |
| Memory requirement | Exabytes for large d | Kilobytes |

### Iterative Deepening vs. BFS:
| Criterion | IDS | BFS |
|-----------|-----|-----|
| Time complexity | O(b^d) | O(b^d) |
| Space complexity | O(bd) | O(b^d) |
| Optimal (uniform cost) | Yes | Yes |
| Complete | Yes (with cycle check) | Yes |
| Node regeneration | Upper levels regenerated d times | Each node generated once |
| Example (b=10, d=5) | N=123,450 | N=111,110 |

### Greedy Best-First vs. A*:
| Criterion | Greedy | A* |
|-----------|--------|----|
| f(n) | h(n) | g(n)+h(n) |
| Cost-optimal | No | Yes (with admissible h) |
| Complete (finite) | Yes | Yes |
| Completeness (infinite) | No | Yes |
| Efficiency | Often fast | Exponential in worst case |
| Behavior | Focuses on goal quickly | Balanced g and h |

### A* vs. Uniform-Cost:
- Uniform-cost contours are circular around start (g-cost)
- A* contours stretch toward goal (g+h bands)

### Unidirectional vs. Bidirectional Search:
| Criterion | Unidirectional A* | Bidirectional |
|-----------|-------------------|---------------|
| Nodes expanded (worst-case) | O(b^d) | O(b^{d/2}) |
| Speedup (b=d=10) | — | ~50,000× |
| Good heuristic | Very focused → less need | Less additional benefit |
| Average heuristic | — | Preferred |
| Poor heuristic | Same asymptotic | Same asymptotic |

### IDA* vs. RBFS vs. SMA*:
| Algorithm | Space | Optimal | Issues |
|-----------|-------|---------|--------|
| IDA* | Linear | Yes (admissible h) | May need many iterations; reexplores states |
| RBFS | Linear | Yes (admissible h) | Excessive node regeneration; mind changes |
| SMA* | Up to available memory | Yes (if optimal reachable) | Thrashing with too little memory |

---

## 5. FORMULAS & EQUATIONS

### A* Evaluation Function:
```
f(n) = g(n) + h(n)
```
- g(n) = path cost from initial state to node n
- h(n) = estimated cost of cheapest path from n to goal
- f(n) = estimated cost of best path that continues from n to goal

### Consistency (Triangle Inequality):
```
h(n) ≤ c(n, a, n') + h(n')
```
For every node n and every successor n' of n generated by action a.

### Admissibility Proof by Contradiction:
Assume optimal path cost = C*, algorithm returns path with cost C > C*. Then there exists unexpanded node n on optimal path:
1. f(n) > C* (otherwise n would be expanded)
2. f(n) = g(n) + h(n) (by definition)
3. f(n) = g*(n) + h(n) (n on optimal path)
4. f(n) ≤ g*(n) + h*(n) (admissibility: h(n) ≤ h*(n))
5. f(n) ≤ C* (by definition C* = g*(n) + h*(n))
Lines 1 and 5 contradict → algorithm must return only cost-optimal paths.

### Surely Expanded Nodes:
- A* expands all nodes with f(n) < C*
- A* may expand nodes with f(n) = C*
- A* expands no nodes with f(n) > C*

### Complexity of Breadth-First Search:
```
Total nodes generated = 1 + b + b² + b³ + ... + b^d = O(b^d)
```
Time and space complexity = O(b^d)

### Complexity of Uniform-Cost Search:
```
O(b^{1 + ⌊C*/ε⌋})
```
where C* = optimal solution cost, ε > 0 = lower bound on action cost.

### Complexity of Iterative Deepening:
```
N(IDS) = (d)b¹ + (d-1)b² + (d-2)b³ + ... + b^d = O(b^d)
```
Example (b=10, d=5): N(IDS)=123,450 vs N(BFS)=111,110

### Complexity of Bidirectional Search:
```
O(b^{d/2})
```
b^{d/2} + b^{d/2} = 2b^{d/2}, compared to b^d (e.g., 50,000× less for b=d=10)

### Effective Branching Factor:
```
N + 1 = 1 + b* + (b*)² + ... + (b*)^d
```
b* is the effective branching factor; N = total nodes generated, d = solution depth.

### Heuristic Functions for 8-Puzzle:
```
h₁ = number of misplaced tiles (excluding blank)
h₂ = Manhattan distance = Σ(|xᵢ − xᵢ_goal| + |yᵢ − yᵢ_goal|)
```
Both admissible. For start state in Figure 3.25: h₁=8, h₂=18, true cost=26.

### Landmark Heuristic (inadmissible):
```
h_L(n) = min_{L ∈ Landmarks} [C*(n, L) + C*(L, goal)]
```

### Differential Heuristic (admissible):
```
h_DH(n) = max_{L ∈ Landmarks} |C*(n, L) − C*(goal, L)|
```

### Linear Combination Heuristic (learned):
```
h(n) = c₁x₁(n) + c₂x₂(n)
```
Where x₁, x₂ are features; c₁, c₂ are learned constants.

### Bidirectional Lower Bound:
```
lb(m, n) = max(g_F(m) + g_B(n), f_F(m), f_B(n))
```
Lower bound on cost of solution going through m (forward) and n (backward).

### Bidirectional f₂ Evaluation:
```
f₂(n) = max(2g(n), g(n) + h(n))
```
Guarantees no node expanded with g(n) > C*/2.

---

## 6. RULES, LAWS & THEOREMS

### A* Optimality Theorem:
With an admissible heuristic, A* is cost-optimal (proved by contradiction above).

### A* Optimal Efficiency Theorem:
A* with a consistent heuristic is optimally efficient — any algorithm extending search paths from initial state using same heuristic must expand all surely expanded nodes.

### Triangle Inequality for Heuristics:
A heuristic is consistent iff it satisfies h(n) ≤ c(n,a,n') + h(n') for all n, a, n'.

### Consistency → Admissibility:
Every consistent heuristic is admissible (but not vice versa).

### Inadmissible A* Cases (where still cost-optimal):
1. If even one cost-optimal path has h admissible for all nodes on that path
2. If h overestimates but never by more than C₂ − C* (C₂ = second-best cost)

### Weighted A* Bound:
If optimal solution costs C*, weighted A* finds solution costing between C* and W × C*.

### Relaxed Problem Principle:
The cost of an optimal solution to a relaxed problem is an admissible heuristic for the original problem.

### Composite Heuristic Property:
h(n) = max{h₁(n), ..., h_k(n)} is admissible (and consistent if all h_i are consistent) and dominates all component heuristics.

### Separation Property (for memory reduction):
Frontier separates interior (expanded) from exterior (unreached) — can be used to eliminate reached table if no U-turns.

### Parity Property of 8-puzzle:
Any given goal can be reached from exactly half of possible initial states.

---

## 7. DATA STRUCTURES & TYPES

### Node Data Structure (4 components):
```
node.STATE      — the state
node.PARENT     — parent node in search tree
node.ACTION     — action that generated this node
node.PATH-COST  — total cost from initial state (also g(node))
```
Following PARENT pointers from goal gives solution.

### Frontier Data Structures:
- **Priority queue**: ordered by f(n); used in best-first, A*, uniform-cost
- **FIFO queue**: used in breadth-first search
- **LIFO queue (stack)**: used in depth-first search, depth-limited search

### Reached States:
- Lookup table (e.g., hash table)
- Key = state, Value = node
- For BFS (uniform costs): can be simple set of states (no need to store better paths)

### Memory Optimization Techniques:
- **Reference counts**: remove state from reached when no more ways to reach it
- **Beam limit k**: keep only k best nodes in frontier
- **δ-beam**: keep nodes within δ of best f-score
- **Separation property**: eliminate reached table if no U-turn actions

---

## 8. VISUAL PATTERNS

### Figure 3.1: Romania Road Map
Simplified road map with cities and distances between them:
```
         Oradea
        /     \
 Zerind       Sibiu — Fagaras
    |        /    \        |
  Arad — Timisoara  Rimnicu — Pitesti — Bucharest
    |         |         |
  Lugoj — Mehadia — Drobeta — Craiova
```
Distances: Arad→Sibiu=140, Arad→Zerind=75, Arad→Timisoara=118, etc.

### Figure 3.2: Vacuum World State-Space Graph
8 states (2 locations × 2 dirt possibilities × 2 agent positions); 3 actions/state (L, R, S).

### Figure 3.3: 8-Puzzle
3×3 grid with tiles 1-8 and blank. Goal state = numbers in order left-to-right, top-to-bottom.

### Figure 3.4: Partial Search Trees
Three stages of expansion from Arad; shows frontier (green), expanded (lavender), unreached (dashed).

### Figure 3.5: Search Tree on State-Space Graph
Tree superimposed on graph; Oradea's successors already reached → no extension.

### Figure 3.6: Separation Property
[Interior expanded | Frontier | Exterior unreached] — frontier separates interior from exterior.

### Figure 3.8: BFS on Binary Tree
Root A expanded first, then B and C, then D,E,F,G — level by level.

### Figure 3.10: Uniform-Cost Search Example
Sibiu → Rimnicu Vilcea (80) vs Fagaras (99). Rimnicu expanded first, then Fagaras, then Pitesti found better path to Bucharest.

### Figure 3.11: DFS on Binary Tree (12-step sequence)
Goes deep immediately, then backs up; frontier = radius of sphere.

### Figure 3.13: Iterative Deepening (4 iterations)
Limits 0, 1, 2, 3; goal M found at limit 3.

### Figure 3.16: Straight-Line Distances to Bucharest
h_SLD values: Arad=366, Bucharest=0, Craiova=160, Fagaras=176, Pitesti=100, Sibiu=253, etc.

### Figure 3.17: Greedy Best-First Search
Nodes labeled by h; Arad(366)→Sibiu(253)→Fagaras(176)→Bucharest(0); finds suboptimal path.

### Figure 3.18: A* Search Stages (a-f)
Each node labeled f=g+h. Stage (a): Arad 366=0+366. Stage (b): Sibiu 393=140+253, Timisoara 447=118+329, Zerind 449=75+374. Stage (c): Oradea 671=291+380, Fagaras 415=239+176, Rimnicu Vilcea 413=220+193. Continues through Pitesti at f=417, then to Bucharest at f=418.

### Figure 3.19: Triangle Inequality
Node n → action cost c(n,a,n') → n'; heuristic h(n) ≤ c + h(n').

### Figure 3.20: Romania Contour Map
f-contours at 380, 400, 420 stretching toward Bucharest.

### Figure 3.21: A* vs Weighted A* on Grid
(a) A*: explores large area, finds optimal path. (b) Weighted A*(W=2): 7× fewer states, path 5% costlier.

### Figure 3.23: RBFS Stages (a-c)
(a) Path via Rimnicu Vilcea; Pitesti leaf f=417 worse than alternative Fagaras f=415. (b) Backed-up value 417; Fagaras expanded with leaf f=450. (c) Backed-up value 450; Rimnicu expanded again; finds solution.

### Figure 3.24: Bidirectional Search Example
Start→A(g=4), Start→B; Goal←F(g=4); using f₂=max(2g,g+h), nodes with g>5 never expanded.

### Figure 3.25: 8-Puzzle Start & Goal
Start: 2-8-3/1-6-4/7-0-5; Goal: 1-2-3/8-0-4/7-6-5 (shortest solution = 26 actions)

### Figure 3.27: 8-Puzzle Subproblem (tiles 1-4+blank)
15,120 patterns; exact solution cost stored in pattern database.

### Figure 3.28: Web Service Driving Directions
Map showing route computed by search algorithm with precomputation and landmarks.

---

## 9. EDGE CASES/EXCEPTIONS/TRAPS

### Negative Cost Cycles:
"if there is a cycle of net negative cost, the cost-optimal solution is to go around that cycle an infinite number of times" → Bellman-Ford or Floyd-Warshall needed.

### Zeno's Paradox (infinitely small costs):
If action costs can shrink arbitrarily (e.g., "move half way to goal at cost half of previous move"), require all action costs ≥ ε > 0.

### Zero-Cost Actions:
Allowed as long as number of consecutive zero-cost actions bounded (e.g., ≤3 rotations).

### Infinite State Spaces:
- Knuth's "4" problem: factorial operator always yields larger integer → infinite
- Need systematic search (spiral expanding outward)
- No sound algorithm can terminate if no solution in infinite space

### Depth-First Search Incompleteness:
- Can get stuck in infinite path (even without cycles, e.g., straight line on infinite grid)
- Can loop infinitely on cyclic state spaces

### A* Exponential Worst Case:
Vacuum world where any square can be cleaned for cost 1 without visiting → 2^N states on optimal path → A* expands all of them.

### Subproblem Heuristics Non-Additive:
Solutions of 1-2-3-4 subproblem and 5-6-7-8 subproblem share moves → cannot add costs; must use disjoint pattern databases.

### Bidirectional Non-Optimal Efficiency:
No bidirectional search algorithm can be guaranteed optimally efficient — any algorithm might expand up to 2× the minimum nodes.

### Inconsistent Heuristics:
May cause multiple nodes for same state in frontier; implementers often avoid them but worst effects rare in practice.

### SMA* Thrashing:
When memory is too small, constant regeneration of dropped nodes makes problem intractable.

### Parity in 8-Puzzle:
Only half of initial states reach a given goal state (parity property).

---

## 10. EMPIRICAL EVIDENCE/KEY RESULTS

### 8-Puzzle Search Cost Comparison (Figure 3.26):
| d | BFS | A*(h₁) | A*(h₂) | b* BFS | b* A*(h₁) | b* A*(h₂) |
|---|-----|--------|--------|--------|-----------|-----------|
| 6 | 128 | 24 | 19 | 2.01 | 1.42 | 1.34 |
| 10 | 1,033 | 116 | 48 | 1.85 | 1.43 | 1.27 |
| 16 | 17,270 | 1,683 | 364 | 1.74 | 1.48 | 1.32 |
| 20 | 91,493 | 9,905 | 1,318 | 1.69 | 1.50 | 1.34 |
| 24 | 290,082 | 53,039 | 5,733 | 1.62 | 1.50 | 1.36 |
| 26 | 395,355 | 110,372 | 10,080 | 1.58 | 1.50 | 1.35 |

h₂ dominates h₁ (never expands more nodes); b* for A* stays ~1.3-1.5 vs BFS ~1.5-2.0.

### 15-Puzzle State Space:
16!/2 ≈ 10^13 states; needs good heuristic.

### Pattern Database Speedup:
Disjoint pattern databases reduce nodes generated by factor of 1,000 (single) to 10,000 (disjoint) vs Manhattan distance for 15-puzzle; ~10^6 for 24-puzzle.

### BFS Memory Example (b=10):
- d=10: 10 terabytes (at 1KB/node)
- d=14: 3.5 years even with infinite memory

### MS Route Finding:
24-million-point US graph searched at <0.1% of nodes using landmarks + bidirectional A*.

### Rubik's Cube:
- Rokicki et al. (2014): any instance solved in 26 moves (180°=2 moves) or 20 (180°=1 move); 35 CPU-years computation
- Agostinelli et al. (2019): RL + deep learning solves 60% optimally, typical <1 second

### School Bus Routing (Boston):
Saved $5 million, cut traffic, saved time (Bertsimas et al., 2019).

### Knuth's "4" Problem:
Shortest path to 5 goes through (4!)! = 620,448,401,733,239,439,360,000.

---

## 11. CROSS-CHAPTER DEPENDENCIES

- **Chapter 4**: Relaxes constraints (nondeterministic, partially observable, unknown, continuous)
- **Chapter 5**: Multiple agents (game playing)
- **Chapter 6**: Constraint satisfaction (backtracking search)
- **Chapter 7, 11**: Planning agents (factored/structured representations)
- **Chapter 11, Section 11.4**: Abstraction validity conditions
- **Chapter 14**: Hidden Markov models (atomic)
- **Chapter 16**: Decision theory, information gathering
- **Chapter 17**: Markov decision processes
- **Chapter 19**: Machine learning
- **Chapter 22**: Reinforcement learning, metalevel learning
- **Appendix A**: Asymptotic complexity (O(n) notation)

---

## 12. DATES & PEOPLE

- **Newell & Simon (1957, 1961)**: Logic Theorist, GPS — origin of state-space search
- **Richard Bellman (1957)**: Additive path costs, dynamic programming
- **Nils Nilsson (1971)**: Established search area; introduced uniform-cost search, closed/open lists
- **Moore (1959)**: Breadth-first search for solving mazes
- **Dijkstra (1959)**: Dijkstra's algorithm (explicit finite graphs)
- **Hart, Nilsson, Raphael (1968)**: A* algorithm
- **Dechter & Pearl (1985)**: A* optimal efficiency conditions
- **Pohl (1970, 1973, 1977)**: Weighted A*, monotone condition, heuristic error analysis
- **Pearl (1984)**: Heuristics textbook; consistency = monotonic equivalence
- **Korf (1985a, 1985b)**: Iterative deepening, IDA*
- **Korf (1987)**: Subgoals, macro-operators, abstraction; coarse-to-fine search
- **Korf (1993)**: RBFS
- **Korf & Reid (1998)**: Effective depth reduction by constant k_h
- **Korf & Felner (2002)**: Disjoint pattern databases
- **Culberson & Schaeffer (1996, 1998)**: Pattern databases
- **Gasser (1995)**: Pattern databases for heuristics
- **Prieditis (1993)**: ABSOLVER — automatic heuristic generation
- **Held & Karp (1970)**: Relaxation for admissible heuristics (minimum spanning tree for TSP)
- **Slocum & Sonneveld (2006)**: 15-puzzle history
- **Sam Loyd (1959)**: Falsely claimed 15-puzzle invention
- **Noyes Chapman (mid-1870s)**: Actual 15-puzzle inventor
- **Ernő Rubik (1974)**: Rubik's Cube
- **Knuth (1964)**: "4" problem
- **Goldberg et al. (2006)**: Microsoft map service using landmarks + bidirectional A*
- **Delling et al. (2009)**: Modern route-finding techniques
- **Pohl (1971)**: First bidirectional search
- **Martelli & Montanari (1973)**: AO* algorithm

---

## 13. PROOF & ARGUMENT PATTERNS

### A* Optimality Proof (by contradiction):
See Section 5 above — assumes algorithm returns C > C*, shows f(n) > C* and f(n) ≤ C* for unexpanded optimal-path node n → contradiction.

### Separation Property:
"In a finite state space with a tree-like search, if we keep track of reached states, the frontier separates the interior (expanded) from the exterior (unreached)."

### Domination Proof:
For consistent h, nodes surely expanded = {n : h(n) < C* − g(n)}. Since h₂ ≥ h₁ for all nodes, every node expanded by A* with h₂ is also expanded with h₁, but h₁ may cause additional expansions.

### Iterative Deepening Waste Analysis:
Bottom level (d) generated once; level d-1 twice; ... root's children d times. Total: (d)b¹ + (d-1)b² + ... + b^d = O(b^d). Actual numbers for b=10, d=5: N(IDS)=123,450 vs N(BFS)=111,110.

---

## 14. DESIGN PARADIGMS/META-METHODS

### Problem Reduction (Relaxation):
Generate admissible heuristic by removing constraints from problem definition → relaxed problem → exact cost of relaxed problem = admissible heuristic for original.

### Dynamic Programming:
Building pattern databases by working backward from goal and recording cost of each pattern encountered (used in pattern database construction).

### Divide and Conquer (Hierarchical Search):
Using subgoals, macro-operators, abstraction for exponential speedup.

### Learning to Search:
Metalevel state space — each state is an object-level search tree; metalevel learning minimizes total problem-solving cost.

---

## 15. CASE STUDIES/CLASSIC EXAMPLES

### Romania Route-Finding (throughout chapter):
Agent in Arad must reach Bucharest; map with distances; demonstrates all search algorithms.

### 8-Puzzle Example:
Start state [2,8,3; 1,6,4; 7,_,5]; Goal state [1,2,3; 8,_,4; 7,6,5]; solution length = 26.

### Knuth's "4" Problem:
Start at 4; use factorial, square root, floor; reach any positive integer. Path to 5: sqrt(floor(sqrt((4!)!))) = 5.

### Vacuum World State-Space Graph (Figure 3.2):
8 states, 3 actions/state; demonstrates state-space graph concept.

---

## 16. ETHICS
(None in Chapter 3)

---

## 17. END-OF-CHAPTER MATERIAL

### Summary (Key Points):
1. Problem = initial state + actions + transition model + goal states + action cost function
2. Environment = state-space graph; solution = path from initial to goal
3. Search algorithms treat states and actions as atomic
4. Algorithms judged by completeness, cost optimality, time complexity, space complexity
5. Uninformed methods: best-first, BFS, uniform-cost, DFS, DLS, IDS, bidirectional
6. Informed methods: greedy best-first, A*, IDA*, RBFS, SMA*, beam, weighted A*
7. Heuristic quality depends on accuracy; can construct by relaxation, pattern databases, landmarks, learning

### Algorithm Comparison Table (Figure 3.15):
| Criterion | BFS | Uniform-Cost | DFS | DLS | IDS | Bidirectional |
|-----------|-----|-------------|-----|-----|-----|---------------|
| Complete? | Yes¹ | Yes¹˒² | No | No | Yes¹ | Yes¹˒⁴ |
| Optimal cost? | Yes³ | Yes | No | No | Yes³ | Yes³˒⁴ |
| Time | O(b^d) | O(b^{1+⌊C*/ε⌋}) | O(b^m) | O(b^ℓ) | O(b^d) | O(b^{d/2}) |
| Space | O(b^d) | O(b^{1+⌊C*/ε⌋}) | O(bm) | O(bℓ) | O(bd) | O(b^{d/2}) |

Superscripts: ¹complete if b finite and state space finite or has solution; ²complete if all action costs ≥ ε>0; ³cost-optimal if all action costs identical; ⁴if both directions are BFS or uniform-cost.

---

# CHAPTER 4: SEARCH IN COMPLEX ENVIRONMENTS (lines 5218–6673)

---

## 1. NAMED ENTITIES — Every Term/Concept with Definition

| Term | Definition |
|------|-----------|
| **Local search** | Operates by searching from start state to neighboring states without keeping paths or reached-set |
| **Optimization problem** | Find best state according to objective function (not path to state) |
| **Objective function** | Function that evaluates quality of a state |
| **State-space landscape** | States laid out with elevation = objective function value |
| **Global maximum** | Highest peak in landscape |
| **Global minimum** | Lowest valley (cost version) |
| **Hill climbing** | Local search moving to neighboring state with highest value (steepest ascent) |
| **Gradient descent** | Cost-minimization version of hill climbing |
| **Steepest ascent** | Moving to neighbor with highest value |
| **Complete-state formulation** | Every state has all components of solution but not necessarily correctly placed |
| **Greedy local search** | Grabs good neighbor without thinking ahead (hill climbing) |
| **Local maximum** | Peak higher than all neighbors but lower than global maximum |
| **Ridge** | Sequence of local maxima difficult for greedy algorithms |
| **Plateau** | Flat area of landscape; can be flat local max or shoulder (progress possible) |
| **Shoulder** | Plateau from which progress is possible |
| **Sideways move** | Move to state of equal value (to escape plateau/shoulder) |
| **Stochastic hill climbing** | Chooses randomly from uphill moves (probability varies with steepness) |
| **First-choice hill climbing** | Generates successors randomly until finding better one |
| **Random-restart hill climbing** | Series of hill-climbing searches from random initial states |
| **Simulated annealing** | Combines hill climbing with random walk; accepts bad moves with probability e^{ΔE/T} |
| **Boltzmann distribution** | e^{ΔE/T} — probability of accepting worse move in simulated annealing |
| **Local beam search** | Keeps k states rather than one; generates successors for all k, selects k best |
| **Stochastic beam search** | Chooses successors with probability proportional to value |
| **Evolutionary algorithm** | Population of individuals; fittest produce offspring via recombination |
| **Recombination** | Process of producing offspring from parents |
| **Genetic algorithm** | Individuals are strings over finite alphabet (often Boolean) |
| **Evolution strategies** | Individuals are sequences of real numbers |
| **Genetic programming** | Individuals are computer programs |
| **Selection** | Choosing individuals to become parents (proportional to fitness or tournament) |
| **Crossover point** | Random point to split parent strings for recombination |
| **Mutation rate** | Probability each bit is flipped in offspring |
| **Elitism** | Keeping top-scoring parents from previous generation in next generation |
| **Schema** | Substring with some positions unspecified (e.g., 246*****) |
| **Instance** | String matching a schema |
| **Baldwin effect** | Learning relaxes fitness landscape, accelerating evolution |
| **Discretization** | Limiting continuous values to fixed grid points |
| **Empirical gradient** | Measuring progress by change in objective function between nearby points |
| **Gradient** | ∇f — vector giving magnitude and direction of steepest slope |
| **Step size** | α — small constant for gradient ascent update |
| **Line search** | Extending gradient direction by doubling α until f decreases |
| **Newton–Raphson method** | Find roots of functions; for optimization: x ← x − H_f^{-1}(x)∇f(x) |
| **Hessian matrix** | H_f(x) — matrix of second derivatives ∂²f/∂x_i∂x_j |
| **Constrained optimization** | Solutions must satisfy hard constraints on variables |
| **Linear programming** | Linear constraints forming convex set + linear objective |
| **Convex set** | Set S where line joining any two points in S is also in S |
| **Convex optimization** | Constraint region is convex; objective is convex within region |
| **Belief state** | Set of physical states agent believes are possible |
| **Conditional plan** | Plan specifying what to do depending on percepts (contingency plan, strategy) |
| **OR node** | Node where agent chooses action (branching from agent's choice) |
| **AND node** | Node where environment chooses outcome (branching from nondeterminism) |
| **AND–OR tree** | Alternating OR and AND nodes for nondeterministic search |
| **Cyclic solution** | Solution using loops (e.g., keep trying until action works) |
| **Sensorless problem / Conformant problem** | No observation at all |
| **Coercion** | Agent forces world into goal state regardless of initial state |
| **Incremental belief-state search** | Builds solution one physical state at a time within belief state |
| **Prediction stage** | Compute belief state after action: PREDICT(b,a) = RESULT(b,a) |
| **Possible percepts stage** | Compute possible percepts in predicted belief state |
| **Update stage** | Compute belief state consistent with actual percept |
| **Recursive state estimator** | Computes new belief state from previous (not entire percept history) |
| **Monitoring / Filtering / State estimation** | Maintaining belief state in partially observable environments |
| **Localization** | Determining location given map and percept/action sequence |
| **Offline search** | Compute complete solution before first action |
| **Online search** | Interleave computation and action |
| **Mapping problem** | Explore unknown environment to build map |
| **Competitive ratio** | Ratio of online path cost to optimal known path cost |
| **Dead end** | State from which no goal state is reachable |
| **Adversary argument** | Imagine adversary constructing state space against the agent |
| **Irreversible action** | No way to return to previous state |
| **Safely explorable** | Some goal state reachable from every reachable state |
| **Random walk** | Select random action from current state |
| **LRTA*** | Learning real-time A* — updates H(s) estimates, chooses best apparent move |
| **Optimism under uncertainty** | Assume untried actions lead immediately to goal at least possible cost |
| **Incremental search** | Keep/reuse search tree or heuristic values across multiple similar problems |
| **Tabu search** | Maintains tabu list of k previously visited states |
| **STAGE algorithm** | Fits quadratic surface to local maxima from random-restart hill climbing |
| **Heavy-tailed distribution** | Probability of very long run time higher than exponential prediction |
| **Eulerian graph** | Graph where each node has equal numbers of incoming and outgoing edges |

---

## 2. SEQUENTIAL PROCESSES — All Step-by-Step Algorithm Descriptions

### HILL-CLIMBING (Figure 4.2):
```
function HILL-CLIMBING(problem) returns a state that is a local maximum
  current ← problem.INITIAL
  while true do
    neighbor ← a highest-valued successor state of current
    if VALUE(neighbor) ≤ VALUE(current) then return current
    current ← neighbor
```

### SIMULATED-ANNEALING (Figure 4.5):
```
function SIMULATED-ANNEALING(problem, schedule) returns a solution state
  current ← problem.INITIAL
  for t = 1 to ∞ do
    T ← schedule(t)
    if T = 0 then return current
    next ← a randomly selected successor of current
    ΔE ← VALUE(current) − VALUE(next)
    if ΔE > 0 then current ← next
    else current ← next only with probability e^{−ΔE/T}
```

### GENETIC-ALGORITHM (Figure 4.8):
```
function GENETIC-ALGORITHM(population, fitness) returns an individual
  repeat
    weights ← WEIGHTED-BY(population, fitness)
    population2 ← empty list
    for i = 1 to SIZE(population) do
      parent1, parent2 ← WEIGHTED-RANDOM-CHOICES(population, weights, 2)
      child ← REPRODUCE(parent1, parent2)
      if (small random probability) then child ← MUTATE(child)
      add child to population2
    population ← population2
  until some individual is fit enough, or enough time has elapsed
  return best individual in population, according to fitness
```

### REPRODUCE (Figure 4.8):
```
function REPRODUCE(parent1, parent2) returns an individual
  n ← LENGTH(parent1)
  c ← random number from 1 to n
  return APPEND(SUBSTRING(parent1, 1, c), SUBSTRING(parent2, c+1, n))
```

### AND-OR-SEARCH (Figure 4.11):
```
function AND-OR-SEARCH(problem) returns a conditional plan, or failure
  return OR-SEARCH(problem, problem.INITIAL, [])

function OR-SEARCH(problem, state, path) returns a conditional plan, or failure
  if problem.IS-GOAL(state) then return empty plan
  if IS-CYCLE(path) then return failure
  for each action in problem.ACTIONS(state) do
    plan ← AND-SEARCH(problem, RESULTS(state, action), [state|path])
    if plan ≠ failure then return [action|plan]
  return failure

function AND-SEARCH(problem, states, path) returns a conditional plan, or failure
  for each s_i in states do
    plan_i ← OR-SEARCH(problem, s_i, path)
    if plan_i = failure then return failure
  return [if s_1 then plan_1 else if s_2 then plan_2 else ... if s_{n-1} then plan_{n-1} else plan_n]
```

### ONLINE-DFS-AGENT (Figure 4.21):
```
function ONLINE-DFS-AGENT(problem, s') returns an action
  persistent: result (table mapping (s,a)→s'), untried (table s→untried actions), 
              unbacktracked (table s→states never backtracked to)
  if problem.IS-GOAL(s') then return stop
  if s' is new (not in untried) then untried[s'] ← problem.ACTIONS(s')
  if s is not null then
    result[s,a] ← s'
    add s to front of unbacktracked[s']
  if untried[s'] is empty then
    if unbacktracked[s'] is empty then return stop
    else a ← action b such that result[s',b] = POP(unbacktracked[s'])
  else a ← POP(untried[s'])
  s ← s'
  return a
```

### LRTA*-AGENT (Figure 4.24):
```
function LRTA*-AGENT(problem, s', h) returns an action
  persistent: result table (s,a)→s', H table s→cost estimate
  if IS-GOAL(s') then return stop
  if s' new (not in H) then H[s'] ← h(s')
  if s is not null then
    result[s,a] ← s'
    H[s] ← min_{b∈ACTIONS(s)} LRTA*-COST(s,b,result[s,b],H)
  a ← argmin_{b∈ACTIONS(s')} LRTA*-COST(problem,s',b,result[s',b],H)
  s ← s'
  return a

function LRTA*-COST(problem, s, a, s', H) returns a cost estimate
  if s' is undefined then return h(s)
  else return problem.ACTION-COST(s,a,s') + H[s']
```

### Belief-State Transition Stages (for partial observability):
1. **PREDICT** stage: ˆb = RESULT(b,a) (as in sensorless)
2. **POSSIBLE-PERCEPTS** stage: {o : o = PERCEPT(s) and s ∈ ˆb}
3. **UPDATE** stage: b_o = {s : o = PERCEPT(s) and s ∈ ˆb}

### Newton–Raphson for Optimization:
1. Need to find x where ∇f(x) = 0
2. Update: x ← x − H_f^{-1}(x)∇f(x)
3. H_f(x) = Hessian matrix of second derivatives

### Gradient Ascent:
```
x ← x + α∇f(x)
```
Where α = step size.

### Newton's Formula (for root finding):
```
x ← x − g(x)/g'(x)
```

### 8-Queens Problem Hill-Climbing on Complete-State Formulation:
1. Place 8 queens randomly, one per column
2. Evaluate h = number of attacking pairs
3. For each of 56 successors (move one queen in its column), compute h
4. Move to state with lowest h (steepest descent)
5. Terminate when no improvement possible

---

## 3. HIERARCHIES/CLASSIFICATIONS

### Hill-Climbing Variants:
| Variant | Selection method | Pros/Cons |
|---------|-----------------|-----------|
| Steepest ascent | Highest-valued neighbor | Fast but gets stuck |
| Stochastic | Random uphill move, probability ∝ steepness | Slower but sometimes better solutions |
| First-choice | Random successors until better found | Good for many (thousands) successors |
| Random-restart | Series from random starts | Complete with probability 1 |
| With sideways moves | Allow equal-value moves (limited count) | 14%→94% success on 8-queens |

### Evolutionary Algorithm Variants:
| Feature | Options |
|---------|---------|
| Population size | Fixed or variable |
| Individual representation | Bit string (GA), real numbers (ES), program (GP) |
| Mixing number ρ | 1 (asexual/stochastic beam), 2 (sexual/crossover), >2 (rare in nature) |
| Selection | Proportional to fitness, tournament |
| Recombination | Single-point crossover, uniform, etc. |
| Mutation rate | Per-bit probability (typically small) |
| Next generation | Offspring only, or elitism (keep top parents) |

### Local Search Algorithm Types:
- Hill climbing (steepest, stochastic, first-choice, random-restart)
- Simulated annealing
- Local beam search (basic, stochastic)
- Evolutionary algorithms (GA, ES, GP)

### Continuous Optimization Methods:
| Method | Approach | Requirements |
|--------|----------|--------------|
| Discretization | Grid with spacing δ | Finite successors |
| Empirical gradient | Sample nearby points | Only function evaluations |
| Gradient ascent | Use ∇f | Differentiable f |
| Newton–Raphson | Hessian inverse × gradient | Twice differentiable f |
| Line search | Adapt α along gradient | Function evaluations |

### Optimization Problem Types:
| Type | Constraints | Objective | Complexity |
|------|-------------|-----------|------------|
| Unconstrained | None | Any | Varies |
| Linear programming | Linear inequalities | Linear | Polynomial |
| Convex optimization | Convex region | Convex function | Polynomial |

### Belief-State Representations:
| Approach | Space | Pros | Cons |
|----------|-------|------|------|
| Explicit set | 2^N belief states | Simple | Massive |
| Compact description | Logical formula | Concise | Complex reasoning |
| Incremental | One state at a time | Fast failure detection | Slower on large belief states |

---

## 4. COMPARISONS/TRADE-OFFS

### Local Search vs. Systematic Search:
| Criterion | Local search | Systematic search |
|-----------|-------------|-------------------|
| Memory | Very little | Often exponential |
| Completeness | Not systematic | Yes (finite spaces) |
| Path tracking | None | Full path |
| Large/infinite spaces | Often works | Often unsuitable |
| Optimization | Natural fit | Awkward |
| Final state only | Yes | Path usually needed |

### Hill Climbing with vs. without Sideways Moves (8-queens):
| Metric | Without sideways | With sideways (≤100) |
|--------|-----------------|---------------------|
| Success rate | 14% | 94% |
| Steps (success) | ~4 | ~21 |
| Steps (failure) | ~3 | ~64 |
| Random restarts needed | ~7 | ~1.06 |
| Total steps | ~22 | ~25 |

### Random-Restart vs. Local Beam Search:
| Random-restart | Local Beam |
|----------------|------------|
| Processes run independently | Information shared among threads |
| No communication | "Come over here, grass is greener" |
| k independent searches | k parallel threads cooperating |
| — | May cluster → loss of diversity |

### Simulated Annealing vs. Hill Climbing:
| Criterion | Hill climbing | Simulated annealing |
|-----------|---------------|---------------------|
| Move selection | Best neighbor | Random |
| Downhill moves | Never | Accepted with probability e^{−ΔE/T} |
| Convergence | Local max | Global max (with p→1 if T→0 slowly) |
| Completeness | No | Yes (probabilistically) |

### Genetic Algorithm vs. Stochastic Beam Search:
- GA adds crossover (sexual reproduction)
- Crossover advantageous if useful "building blocks" (schemas) exist
- Without meaningful blocks, crossover conveys no advantage

### Offline vs. Online Search:
| Offline | Online |
|---------|--------|
| Complete solution before acting | Interleave computation and action |
| Explore model, not real world | Explore real world |
| Any node order (simulated) | Must physically occupy state to expand |
| A* can jump between distant nodes | Local expansion order preferred |

### DFS vs. Online DFS:
| Aspect | Offline DFS | Online DFS-AGENT |
|--------|-------------|------------------|
| Dropped state | Simply removed from queue | Must physically backtrack |
| Cycle handling | Ignore or check | Must store predecessor table |
| Environment | Model only | Real world |
| Reversible actions | Not required | Required (for simple algorithm) |

---

## 5. FORMULAS & EQUATIONS

### Simulated Annealing Acceptance Probability:
```
P(accept) = e^{−ΔE/T}
```
Where ΔE = VALUE(current) − VALUE(next), T = current temperature.

### Gradient Ascent Update:
```
x ← x + α∇f(x)
```
α = step size; ∇f = gradient vector.

### Newton–Raphson Optimization:
```
x ← x − H_f^{-1}(x)∇f(x)
```
H_f(x) = Hessian matrix of second derivatives; ∇f(x) = gradient vector.

### Newton's Formula (root finding):
```
x ← x − g(x)/g'(x)
```

### Airport Problem Objective Function:
```
f(x) = f(x₁, y₁, x₂, y₂, x₃, y₃) = Σ_{i=1}^{3} Σ_{c∈C_i} [(x_i − x_c)² + (y_i − y_c)²]
```
Where C_i = set of cities whose closest airport is airport i.

### Gradient for Airport Problem (partial):
```
∂f/∂x₁ = 2 Σ_{c∈C₁} (x₁ − x_c)
```
Similar for other coordinates.

### Belief-State Transition (deterministic):
```
b' = RESULT(b, a) = {s' : s' = RESULT_P(s, a) and s ∈ b}
```

### Belief-State Transition (nondeterministic):
```
b' = RESULT(b, a) = {s' : s' ∈ RESULTS_P(s, a) and s ∈ b}
= ⋃_{s∈b} RESULTS_P(s, a)
```

### Belief-State Transition (partial observability, three stages):
```
RESULTS(b, a) = {b_o : b_o = UPDATE(PREDICT(b,a), o) and o ∈ POSSIBLE-PERCEPTS(PREDICT(b,a))}
```

### Recursive State Estimator:
```
b' = UPDATE(PREDICT(b, a), o)
```

### LRTA* Cost Estimate:
```
H[s] ← min_{b ∈ ACTIONS(s)} LRTA*-COST(s, b, result[s,b], H)
```
where LRTA*-COST(s,a,s',H) = ACTION-COST(s,a,s') + H[s'] if s' defined, else h(s).

### Expected Number of Random Restarts:
```
E[restarts] = 1/p
```
where p = probability of success per hill-climbing trial.

---

## 6. RULES, LAWS & THEOREMS

### Random-Restart Completeness:
Random-restart hill climbing is complete with probability 1 — it will eventually generate a goal state as initial state.

### Simulated Annealing Convergence:
If the schedule lowers T to 0 slowly enough, the Boltzmann distribution ensures all probability concentrates on global maxima; algorithm finds them with probability approaching 1.

### LRTA* Completeness:
LRTA* agent is guaranteed to find a goal in any finite, safely explorable environment.

### LRTA* Non-Completeness:
Not complete for infinite state spaces — can be led infinitely astray.

### Online DFS-AGENT Completeness:
Only guaranteed in safely explorable state spaces (esp. with reversible actions).

### Dead End Theorem:
No algorithm can avoid dead ends in all state spaces (adversary argument: two identical-looking states, one with goal, one with dead end; agent can't distinguish).

### Irreversible Actions:
No bounded competitive ratio can be guaranteed if there are paths of unbounded cost, even in reversible environments.

### Genetic Algorithm Schema Theorem:
If the average fitness of instances of a schema is above the mean, the number of instances of the schema will grow over time.

### Baldwin Effect:
Learning can effectively relax the fitness landscape, accelerating evolution.

### Newton–Raphson Interpretation:
Can be seen as fitting quadratic surface to f at x, then moving directly to minimum of that surface (exact if f is quadratic).

---

## 7. DATA STRUCTURES & TYPES

### ONLINE-DFS-AGENT Persistent Tables:
- `result[s,a]` → s': records state resulting from action a in state s (map)
- `untried[s]` → list: unexplored actions for each state
- `unbacktracked[s]` → list: predecessor states not yet backtracked to

### LRTA*-AGENT Persistent Tables:
- `result[s,a]` → s': map of action outcomes
- `H[s]` → cost estimate: current best estimate of cost to reach goal from s

### Belief-State as Set:
- Power set of physical states: 2^N possible belief states
- Not all reachable (e.g., only 12/256 in deterministic sensorless vacuum)

### 8-Queens State Representation:
- 8-digit string, c-th digit = row of queen in column c
- 8⁸ ≈ 17 million states
- Heuristic h = number of attacking pairs

### Sokoban State Space Size:
n × n!/(b!(n−b)!) states; e.g., 8×8 grid with 12 boxes → >200 trillion states.

---

## 8. VISUAL PATTERNS

### Figure 4.1: One-Dimensional State-Space Landscape
```
     /\     Global maximum
    /  \    /\
   /    \  /  \     Local maximum
  /      \/    \   /
 /              \ /  Shoulder
/                \/  Plateau
```
Elevation = objective function; labels: global max, local max, flat local max, shoulder.

### Figure 4.3: 8-Queens
(a) Almost-solution with diagonal attack between queens in columns 4 and 7.
(b) Board with h=17, showing all 56 successors with their h values; 8 moves tied at h=12.

### Figure 4.4: Ridge Topology
```
States (●) on ridge line → from each local max, all actions point downhill.
```
Sequence of local maxima not directly connected; hard for hill climbing.

### Figure 4.6: Genetic Algorithm for 8-Queens
(a) Initial population of 4 strings: 32752411, 24748552, 32752411, 24415124
(b) Fitness (non-attacking pairs): 24(31%), 23(29%), 20(26%), 11(14%)
(c) Selection: pairs (32752411+24748552), (32752411+24415124)
(d) Crossover at point 3: 327|52411+247|48552 → 32748552; 327|52411+244|15124 → 32715124
(e) Mutation: digits flipped (e.g., 32748552→32748152)

### Figure 4.7: Crossover Effect on 8-Queens Boards
Green columns lost; red columns retained in offspring.

### Figure 4.9: Vacuum World States (8 states)
```
1:[A,Dirty,B,Dirty]  2:[A,Dirty,B,Clean]
3:[A,Clean,B,Dirty]  4:[A,Clean,B,Clean]
5: agent at A, B dirty 6: agent at A, both clean
7: agent at B, both clean (goal)  8: agent at B, A clean (goal)
```
States 7 and 8 are goals (all clean).

### Figure 4.10: AND–OR Search Tree for Erratic Vacuum
Root = state 1 (OR node); actions: Left, Suck, Right. Suck leads to AND node (outcomes 5 and 7). Solution: Suck → if State=5 then [Right, Suck].

### Figure 4.12: Slippery Vacuum World Search Graph
Right from state 1 leads to belief state {1,2} → cycles; solution requires while-loop.

### Figure 4.13: Belief-State Prediction
(a) Deterministic Right: {1,2,3,4} → {2,4,6,8} (shrinks)
(b) Slippery Right: {1,2,3,4} → {1,2,3,4,5,6,7,8} (grows)

### Figure 4.14: Reachable Belief-State Space (Sensorless Vacuum)
12 belief states out of 2⁸=256; boxes with state-number sets; arrows for Left, Right, Suck.

### Figure 4.15: Local-Sensing Vacuum Transitions
(a) Deterministic: Right from {1,3} → {2,4}; percepts [R,Dirty] and [R,Clean] → two singleton belief states.
(b) Slippery: Right from {1,3} → {1,2,3,4}; percepts [L,Dirty], [R,Dirty], [R,Clean] → three belief states.

### Figure 4.16: AND–OR for Local-Sensing Vacuum
First level: Suck → Right → if Bstate={6} then Suck else [].

### Figure 4.17: Kindergarten Vacuum Belief-State Maintenance
Two prediction–update cycles: initial → Right → [A,Clean] → Suck → [B,Dirty] → Right → ...

### Figure 4.18: Robot Localization
(a) After first percept 1011: 4 possible locations shown on maze.
(b) After Right action + second percept 1010: belief state collapses to single location.

### Figure 4.19: Simple Maze
3×3 grid; S at (1,1), G at (3,3); walls in maze; agent knows nothing.

### Figure 4.20: Adversarial State Spaces
(a) Two spaces: S→A and S→A→G vs S→A (dead end); agent can't distinguish.
(b) Long thin wall forcing arbitrarily inefﬁcient route.

### Figure 4.22: Random Walk Trap
Topology with stair-step states where backward is twice as likely as forward → exponential time.

### Figure 4.23: LRTA* on 1D (5 iterations)
(a) H values [9,2,1] → moves right. (b) Updates H=3 → moves left. (c) Updates H=4 → moves right. (d) H=5 → moves right. (e) Escape.

---

## 9. EDGE CASES/EXCEPTIONS/TRAPS

### Local Maxima:
Hill climbing stuck at peak higher than neighbors but lower than global maximum (86% failure on 8-queens).

### Ridges:
Sequence of local maxima not connected; greedy algorithms cannot navigate.

### Plateaus:
Flat areas with no uphill direction; algorithm wanders aimlessly.

### Diversity Loss in Beam Search:
k states cluster in small region → becomes k-times-slower hill climbing.

### Crossover Without Meaningful Blocks:
If genes are randomly permuted, crossover conveys no advantage over mutation alone.

### Dead Ends in Online Search:
No algorithm can avoid dead ends in all state spaces (adversary argument).

### Heavy-Tailed Run Times:
Systematic backtracking can have heavy-tailed distribution; random restarts find solution faster on average.

### SMA* Thrashing:
With too little memory, constant regeneration of dropped nodes makes solvable problems intractable.

### Random Walk Traps:
Topologies where backward progress more likely than forward → exponential exploration time.

### Sensorless 8-Puzzle Impossible:
Without any sensing, 8-puzzle cannot be solved.

### Illegal Actions in Belief States:
If actions differ across states in belief state: can take union (safe) or intersection (if catastrophic).

### Goal Achievement in Belief States:
"Possibly achieves" if any state satisfies goal; "Necessarily achieves" if all states satisfy goal (we aim for necessary).

### Superset Pruning:
If belief state b₁ is superset of b₂ and b₁ has a solution, then b₂ also has a solution. If b₁ is unsolvable, then any superset is also unsolvable → can prune supersets.

### 3D Random Walk:
On 3D grid, probability of ever returning to start is only ~0.3405.

### Inconsistent Composite Heuristics:
Taking max of consistent heuristics yields consistent heuristic; randomly selecting among them can yield inconsistent.

### Negative Cost Cycles:
Not covered in this chapter; "it is easy to accommodate zero-cost actions as long as consecutive zero-cost actions are bounded."

---

## 10. EMPIRICAL EVIDENCE/KEY RESULTS

### 8-Queens Hill Climbing:
- 8⁸ ≈ 17 million states
- Steepest ascent: succeeds 14%, fails 86%
- Average steps when succeeds: ~4; when fails: ~3
- With sideways moves (≤100): success rate 94%
- Steps: ~21 (success), ~64 (failure)
- Random restarts without sideways: ~7 iterations, ~22 total steps
- Random restarts with sideways: ~1.06 iterations, ~25 total steps
- Three million queens solved in seconds with random-restart hill climbing

### 8-Queens Genetic Algorithm (Figure 4.6):
- Fitness = non-attacking pairs (max = 28)
- Population of 4; fitness values 24, 23, 20, 11
- Normalized probabilities: 31%, 29%, 26%, 14%

### LRTA* Complexity:
- Explores n states in O(n²) steps worst-case
- Often does much better

### Random Walk on 2D Grid:
Complete (eventually reaches goal) — but exponential on some topologies.

### Airport Problem Variables:
6-dimensional space (3 airports × 2 coordinates); gradient analytical.

### Localization Convergence:
With reasonable variation in geography, localization often converges quickly to a single point even with nondeterministic actions.

### Genetic Algorithm Applications:
- Antenna design (Lohn et al., 2001)
- Circuit layout and job-shop scheduling
- Evolving deep neural network architectures

### Microsoft Map Service (Goldberg et al., 2006):
- 24-million-point US graph
- Searches <0.1% of graph for optimal path
- Uses landmarks + bidirectional A* + precomputed paths

---

## 11. CROSS-CHAPTER DEPENDENCIES

- **Chapter 3**: Base search algorithms (relaxed in Chapter 4)
- **Chapter 5**: Multiple agents
- **Chapter 6**: Constraint satisfaction (backtracking search, cycle checking)
- **Chapter 7, 11**: Formal language for problem descriptions, automated relaxation
- **Chapter 8-10**: Formal representations, general rules for action outcomes
- **Chapter 11, Section 11.4**: Abstraction validity
- **Chapter 12**: Probabilistic reasoning, handling faulty sensors
- **Chapter 14**: Filtering, state estimation in stochastic continuous environments
- **Chapter 17**: MDPs, online search in stochastic environments, belief-state problems (Astrom 1965)
- **Chapter 19**: Machine learning, constructing general rules
- **Chapter 20**: Convex optimization in ML
- **Chapter 22**: Reinforcement learning, LRTA* as special case, online learning, safe exploration
- **Chapter 25, 26**: Sensors, actuators, robotics
- **Chapter 26**: Robotics, continuous search spaces, robot navigation
- **Appendix A**: Vectors, matrices, derivatives, NP-hardness

---

## 12. DATES & PEOPLE

- **Newton (1671) / Raphson (1690)**: Newton–Raphson method
- **Charles Darwin (1859)**: *On the Origin of Species*
- **Alfred Russel Wallace (1858)**: Evolution by natural selection (independent)
- **Gregor Mendel (1866)**: Laws of inheritance
- **Watson & Crick (1953)**: DNA structure (AGTC)
- **James Baldwin (1896)**: Baldwin effect
- **Conwy Lloyd Morgan (1896)**: Baldwin effect (simultaneous)
- **Jean Lamarck (1809)**: Incorrect theory of acquired trait inheritance
- **Sewall Wright (1931)**: Fitness landscape concept
- **Box (1957) / Friedman (1959)**: Early evolutionary optimization
- **Rechenberg (1965)**: Evolution strategies for airfoil optimization
- **John Holland (1960s-70s)**: Genetic algorithms
- **John Koza (1992, 1994)**: Genetic programming
- **Kirkpatrick et al. (1983)**: Simulated annealing
- **Metropolis et al. (1953)**: Metropolis algorithm (origin of simulated annealing)
- **Minton et al. (1992)**: Local search for n-queens
- **Selman et al. (1992)**: Local search for Boolean satisfiability
- **Korf (1990)**: LRTA* algorithm
- **Papadimitriou & Yannakakis (1991)**: Competitive ratio in geometric path planning
- **Deng & Papadimitriou (1990)**: First thorough algorithmic study of graph exploration
- **Astrom (1965)**: Belief-state problems for probabilistic uncertainty
- **Erdmann & Mason (1988)**: Robotic manipulation without sensors (continuous belief-state search)
- **Genesereth & Nourbakhsh (1993)**: Belief-state approach for sensorless/partially observable search
- **Koenig et al. (2004)**: Lifelong Planning A*
- **Koenig & Likhachev (2002)**: D* Lite
- **Slagle**: SAINT program (first AND–OR trees for symbolic integration)
- **Amarel (1967)**: AND–OR search for theorem proving
- **Nilsson (1971)**: AO* algorithm
- **Martelli & Montanari (1973)**: AO* improvements
- **Lowerre (1976)**: H ARPY system — beam search for speech recognition
- **Glover & Laguna (1997)**: Tabu search
- **Boyan & Moore (1998)**: STAGE algorithm
- **Kantorovitch (1939)**: Linear programming
- **Dantzig (1949)**: Simplex algorithm
- **Karmarkar (1984)**: Interior-point methods
- **Nesterov & Nemirovski (1994)**: Polynomial complexity for convex optimization
- **Langton (1995)**: Artificial life movement
- **Hinton & Nowlan (1987)**: Computer simulations confirming Baldwin effect
- **Goldberg et al. (2006)**: Microsoft map landmarks + bidirectional A*

---

## 13. PROOF & ARGUMENT PATTERNS

### Adversary Argument for Dead Ends:
Two state spaces are indistinguishable to agent based on observations; one has goal reachable, other has dead end. Therefore no algorithm can avoid dead ends in all state spaces.

### Unbounded Competitive Ratio Proof:
Adversary can construct arbitrarily long thin walls, forcing arbitrarily inefficient paths, even in reversible environments.

### Simulated Annealing Convergence Argument:
If temperature lowers slowly enough, Boltzmann distribution concentrates all probability on global maxima → algorithm finds them with probability → 1.

### Schema Theorem Logic:
If average fitness of schema instances > population mean, instances grow over time. Effect significant only if contiguous blocks provide consistent benefit.

### Superset Pruning Proof:
If b₁ ⊇ b₂ and solution exists from b₁, then same solution works from b₂ (less confusion). If no solution from b₁, then no solution from supersets.

---

## 14. DESIGN PARADIGMS/META-METHODS

### Optimism Under Uncertainty:
LRTA* assumes untried actions lead immediately to goal at least possible cost → encourages exploration.

### Random Restarts with Heavy-Tailed Distributions:
When run times have heavy-tailed distribution, random restarts find solution faster on average than single long run.

### Incremental Search:
Reuse search trees, heuristic values, or best-path costs across multiple similar problems (LPA*, D* Lite).

### Divide and Conquer in Continuous Spaces:
Discretization → finite successors → apply standard local search.

### Hybrid Methods:
Run BFS until memory nearly full, then iterative deepening from frontier nodes.

### Constrained Optimization:
Linear programming → polynomial; convex optimization → polynomial; general constrained → difficult.

---

## 15. CASE STUDIES/CLASSIC EXAMPLES

### 8-Queens Problem (Section 4.1.1):
- Complete-state formulation: 8 queens, one per column
- Heuristic: number of attacking pairs (h=0 = solution)
- 56 successors per state
- Steepest ascent succeeds 14% of time, average ~4 steps
- With sideways moves (≤100): 94% success

### Vacuum World Variants (Section 4.3):
- **Erratic**: Suck may affect adjacent square or deposit dirt on clean carpet. Solution = conditional plan
- **Slippery**: movement sometimes fails → cyclic solution needed (while-loop)
- **Sensorless**: no percepts → belief-state search; Right+Suck+Left+Suck coerces world to goal
- **Local-sensing**: sees own square's dirt + location → conditional plan with belief-state tests
- **Kindergarten**: any square may become dirty at any time → continuous monitoring needed

### Airport Siting Problem (Section 4.2):
- 3 airports anywhere in Romania
- Minimize sum of squared straight-line distances from each city to nearest airport
- 6-dimensional state space (x₁,y₁,x₂,y₂,x₃,y₃)
- Objective function: f = Σᵢ Σ_{c∈Cᵢ} [(xᵢ−x_c)² + (yᵢ−y_c)²]
- Newton–Raphson: one step moves each airport to centroid of its cities

### Robot Localization (Section 4.4.4):
- Maze environment with 4 sonar sensors
- Percept = 4-bit vector (N,E,S,W obstacles)
- Nondeterministic actions (slippery movement)
- Belief state: all possible locations consistent with percept history
- Converges to single location with enough distinctive observations

### Simple Maze Exploration (Section 4.5):
- S at (1,1), G at (3,3), walls unknown
- Online DFS-AGENT: learns result[s,a] table, uses untried/unbacktracked lists
- Worst case: traverse every link exactly twice (optimal for exploration)

---

## 16. ETHICS
(None in Chapter 4 — but note the biological evolution discussion touches on scientific integrity)

---

## 17. END-OF-CHAPTER MATERIAL

### Summary (Key Points):
1. Local search: keep only few states; for optimization (find high-scoring state, no path needed)
2. Simulated annealing: returns optimal with appropriate cooling schedule
3. Continuous spaces: linear/convex optimization → polynomial-time; gradient/Newton–Raphson for well-formed problems
4. Evolutionary algorithms: population + mutation + crossover
5. Nondeterministic → AND–OR search → contingent plans
6. Partially observable → belief state; standard search on belief-state space
7. Sensorless problems: belief-state search → sequence of actions
8. Exploration: online search agents build map; LRTA* escapes local minima via heuristic updates

---
</task_result>
</task>

---

# COMPREHENSIVE EXAMINABLE CONTENT EXTRACTION

## Chapters 5–7 of *Artificial Intelligence: A Modern Approach* (Russell & Norvig)

---

# CHAPTER 5: ADVERSARIAL SEARCH AND GAMES

## 1. Named Entities (Terms, Concepts, Algorithms)

| Term | Definition |
|------|------------|
| **Adversarial search** | Search in competitive environments where two or more agents have conflicting goals |
| **Game** | A structured, rule-based competitive environment studied in AI (chess, Go, poker, etc.) |
| **Perfect information** | Synonym for "fully observable" — all players know the full state |
| **Zero-sum game** | A game where what is good for one player is equally bad for the other; no "win-win" outcome |
| **Move** | Synonym for "action" in games |
| **Position** | Synonym for "state" in games |
| **MAX** | The player whose turn it is to move, aiming to maximize utility |
| **MIN** | The opponent, aiming to minimize MAX's utility |
| **Initial state (S₀)** | How the game is set up at the start |
| **TO-MOVE(s)** | The player whose turn it is to move in state s |
| **ACTIONS(s)** | The set of legal moves in state s |
| **RESULT(s,a)** | The transition model defining the state from taking action a in state s |
| **IS-TERMINAL(s)** | Terminal test — true when the game is over |
| **Terminal state** | State where the game has ended |
| **UTILITY(s,p)** | Utility function (objective/payoff function) defining final numeric value to player p in terminal state s |
| **State space graph** | Graph where vertices are states, edges are moves |
| **Search tree** | Tree superimposed over part of the state space graph |
| **Game tree** | Search tree following every sequence of moves to a terminal state |
| **Ply** | One move by one player (one level deeper in the game tree) |
| **Minimax value (MINIMAX(s))** | Utility (for MAX) of being in state s, assuming optimal play by both |
| **Minimax decision** | Action leading to state with highest minimax value |
| **Minimax search** | Algorithm computing optimal move by depth-first exploration of game tree |
| **Alliance** | Formal or informal cooperation among players in multiplayer games |
| **Alpha–beta pruning** | Technique pruning large parts of the game tree without affecting the minimax decision |
| **α (alpha)** | Value of best (highest-value) choice found so far along path for MAX; "at least" |
| **β (beta)** | Value of best (lowest-value) choice found so far along path for MIN; "at most" |
| **Killer moves** | Best moves found at a given depth, tried first in move ordering |
| **Killer move heuristic** | Trying killer moves first |
| **Transposition** | Different move sequences leading to the same position |
| **Transposition table** | Cache of heuristic values of states to avoid re-searching transpositions |
| **Type A strategy** | Consider all moves to a fixed depth, then use heuristic evaluation (Shannon, 1950) |
| **Type B strategy** | Ignore bad-looking moves, follow promising lines "as far as possible" |
| **Cutoff test (IS-CUTOFF)** | Replaces terminal test; decides when to cut off search based on depth and state properties |
| **H-MINIMAX(s,d)** | Heuristic minimax value of state s at search depth d |
| **Evaluation function (EVAL)** | Estimates expected utility of a state for a player |
| **Features** | Various attributes of a state used by evaluation functions (e.g., number of pawns) |
| **Expected value** | Weighted average of outcomes for states in a category |
| **Weighted linear function** | EVAL(s) = w₁f₁(s) + w₂f₂(s) + ... + wₙfₙ(s) |
| **Material value** | Approximate piece values in chess: pawn=1, knight/bishop=3, rook=5, queen=9 |
| **Quiescence** | Position with no pending moves that would wildly swing the evaluation |
| **Quiescence search** | Extra search beyond cutoff for nonquiescent positions (often restricted to capture moves) |
| **Horizon effect** | Problem where delaying tactics push unavoidable bad events beyond the search horizon |
| **Singular extension** | Extending search for moves that are "clearly better" than all others |
| **Forward pruning** | Pruning moves that appear poor but might be good (risks error) |
| **PROBCUT (probabilistic cut)** | Forward-pruning version of alpha–beta using statistics from prior experience |
| **Late move reduction** | Reducing search depth for later moves in the list (assuming good move ordering) |
| **Retrograde minimax search** | Building endgame tables by working backwards from terminal positions |
| **Policy** | Mapping from every possible state to the best move in that state |
| **Monte Carlo tree search (MCTS)** | Search using playout simulations rather than heuristic evaluation |
| **Simulation / Playout / Rollout** | Complete game played from a state using a playout policy |
| **Playout policy** | Strategy for choosing moves during playouts |
| **Pure Monte Carlo search** | N simulations from current state; pick move with highest win percentage |
| **Selection policy** | Policy focusing computational resources on important parts of game tree |
| **Exploration** | Investigating states with few playouts |
| **Exploitation** | Focusing on states that have done well in past playouts |
| **UCT (Upper Confidence Bounds applied to Trees)** | Selection policy balancing exploration and exploitation |
| **UCB1** | Specific formula: UCB1(n) = U(n)/N(n) + C × √(log N(PARENT(n)) / N(n)) |
| **Early playout termination** | Stopping long playouts and evaluating heuristically or declaring a draw |
| **Stochastic game** | Game with random elements (dice, card shuffling) |
| **Chance nodes** | Nodes in game tree representing random events (dice rolls) |
| **Expectiminimax value** | Generalization of minimax for games with chance nodes |
| **Guaranteed checkmate** | Strategy that for each possible percept sequence leads to checkmate for every board state in belief state |
| **Probabilistic checkmate** | Checkmate that works with probability 1 (or 1−ε) through randomization |
| **Accidental checkmate** | Checkmate that succeeds because opponent's pieces happen to be in right places |
| **Bluff** | Betting as if one's hand is good when it's not |
| **Metareasoning** | Reasoning about what computations to do |
| **Null move heuristic** | Generating a lower bound on position value by letting opponent move twice |
| **Futility pruning** | Pruning moves unlikely to cause beta cutoff |
| **Kriegspiel** | Partially observable chess variant where players see only their own pieces |

## 2. Sequential Processes (Algorithms)

### MINIMAX-SEARCH Algorithm
```
function MINIMAX-SEARCH(game, state) returns an action
    player ← game.TO-MOVE(state)
    value, move ← MAX-VALUE(game, state)
    return move

function MAX-VALUE(game, state) returns a (utility, move) pair
    if game.IS-TERMINAL(state) then return game.UTILITY(state, player), null
    v ← −∞
    for each a in game.ACTIONS(state) do
        v2, a2 ← MIN-VALUE(game, game.RESULT(state, a))
        if v2 > v then v, move ← v2, a
    return v, move

function MIN-VALUE(game, state) returns a (utility, move) pair
    if game.IS-TERMINAL(state) then return game.UTILITY(state, player), null
    v ← +∞
    for each a in game.ACTIONS(state) do
        v2, a2 ← MAX-VALUE(game, game.RESULT(state, a))
        if v2 < v then v, move ← v2, a
    return v, move
```
- Complexity: O(b^m) time, O(bm) or O(m) space
- Performs complete depth-first exploration

### ALPHA-BETA-SEARCH Algorithm
```
function ALPHA-BETA-SEARCH(game, state) returns an action
    player ← game.TO-MOVE(state)
    value, move ← MAX-VALUE(game, state, −∞, +∞)
    return move

function MAX-VALUE(game, state, α, β) returns a (utility, move) pair
    if game.IS-TERMINAL(state) then return game.UTILITY(state, player), null
    v ← −∞
    for each a in game.ACTIONS(state) do
        v2, a2 ← MIN-VALUE(game, game.RESULT(state, a), α, β)
        if v2 > v then v, move ← v2, a
        α ← MAX(α, v)
        if v ≥ β then return v, move
    return v, move

function MIN-VALUE(game, state, α, β) returns a (utility, move) pair
    if game.IS-TERMINAL(state) then return game.UTILITY(state, player), null
    v ← +∞
    for each a in game.ACTIONS(state) do
        v2, a2 ← MAX-VALUE(game, game.RESULT(state, a), α, β)
        if v2 < v then v, move ← v2, a
        β ← MIN(β, v)
        if v ≤ α then return v, move
    return v, move
```
- With perfect ordering: O(b^(m/2)) nodes
- With random ordering: O(b^(3m/4)) nodes

### MCTS Algorithm (UCT variant)
```
function MONTE-CARLO-TREE-SEARCH(state) returns an action
    tree ← NODE(state)
    while IS-TIME-REMAINING() do
        leaf ← SELECT(tree)
        child ← EXPAND(leaf)
        result ← SIMULATE(child)
        BACK-PROPAGATE(result, child)
    return the move in ACTIONS(state) whose node has highest number of playouts
```

**Four steps of each MCTS iteration:**
1. **Selection**: From root, choose moves guided by selection policy (UCT), descending to a leaf
2. **Expansion**: Grow tree by generating new child of selected node (marked 0/0)
3. **Simulation**: Playout from new child using playout policy; moves NOT recorded in tree
4. **Back-propagation**: Update all nodes up to root with result (increment wins and playouts)

### Expectiminimax Formula
```
EXPECTIMINIMAX(s) =
    UTILITY(s, MAX)                       if IS-TERMINAL(s)
    maxₐ EXPECTIMINIMAX(RESULT(s,a))      if TO-MOVE(s) = MAX
    minₐ EXPECTIMINIMAX(RESULT(s,a))      if TO-MOVE(s) = MIN
    Σᵣ P(r) EXPECTIMINIMAX(RESULT(s,r))  if TO-MOVE(s) = CHANCE
```

## 3. Hierarchies/Classifications

**Game Classification:**
- Deterministic vs. stochastic
- Two-player vs. multiplayer
- Turn-taking vs. simultaneous
- Perfect information vs. partial/imperfect information
- Zero-sum vs. non-zero-sum

**Search Strategy Types (Shannon, 1950):**
- Type A: Wide but shallow — consider all moves to fixed depth, then evaluate
- Type B: Deep but narrow — follow promising lines, prune bad moves

**MCTS vs. Alpha–Beta:**
- MCTS preferred when: high branching factor, difficult evaluation function
- Alpha–Beta preferred when: low branching factor, good evaluation function, low error tolerance

## 4. Comparisons/Trade-offs

| Aspect | Minimax | Alpha–Beta | MCTS |
|--------|---------|------------|------|
| Nodes examined | O(b^m) | O(b^(m/2)) best | N/A (playouts) |
| Evaluation function | Required | Required | Not required (rules determine outcome) |
| Error vulnerability | High | High | Lower (aggregate of many playouts) |
| Branching factor sensitivity | Very sensitive | Very sensitive | Less sensitive |
| Game type | Deterministic | Deterministic | Any (incl. stochastic) |

**Type A vs Type B:** Type A (wide/shallow) historically used in chess; Type B (deep/narrow) in Go; modern programs blend both.

**Perfect vs. imperfect ordering in alpha–beta:**
- Perfect: O(b^(m/2)) — effective branching factor = √b
- Random: O(b^(3m/4))
- Chess with simple ordering: within factor 2 of best-case

## 5. Formulas & Equations

**Minimax value:**
```
MINIMAX(s) = UTILITY(s, MAX)              if IS-TERMINAL(s)
             maxₐ MINIMAX(RESULT(s,a))    if TO-MOVE(s) = MAX
             minₐ MINIMAX(RESULT(s,a))    if TO-MOVE(s) = MIN
```

**Heuristic minimax:**
```
H-MINIMAX(s,d) = EVAL(s,MAX)                      if IS-CUTOFF(s,d)
                 maxₐ H-MINIMAX(RESULT(s,a),d+1)  if TO-MOVE(s) = MAX
                 minₐ H-MINIMAX(RESULT(s,a),d+1)  if TO-MOVE(s) = MIN
```

**Weighted linear evaluation function:**
```
EVAL(s) = w₁f₁(s) + w₂f₂(s) + ... + wₙfₙ(s) = Σᵢ wᵢ fᵢ(s)
```

**UCB1 formula:**
```
UCB1(n) = U(n)/N(n) + C × √(log N(PARENT(n)) / N(n))
```
Where:
- U(n) = total utility of all playouts through node n
- N(n) = number of playouts through node n
- PARENT(n) = parent node of n
- C = exploration/exploitation balance constant (theoretical optimum √2, but tuned in practice)
- U(n)/N(n) = exploitation term (average utility)
- √(log N(PARENT(n))/N(n)) = exploration term

**Chess material values:** pawn=1, knight/bishop=3, rook=5, queen=9

**Chess game tree size:** ~10^40 nodes, branching factor ~35, depth ~80 ply

**Expectiminimax complexity:** O(b^m n^m) where n = number of distinct chance outcomes

## 6. Rules, Laws & Theorems

**Minimax Theorem:** The optimal strategy can be determined by working out the minimax value of each state, assuming both players play optimally.

**Alpha–Beta Correctness (Knuth & Moore, 1975):** Alpha–beta computes the same optimal move as minimax.

**Alpha–Beta Optimality (Pearl, 1982b):** Alpha–beta is asymptotically optimal among all fixed-depth game-tree search algorithms.

**UCT Exploration/Exploitation Tradeoff:** The exploration term goes to zero as counts increase; eventually playouts go to the node with highest average utility.

**Expectiminimax evaluation requirement:** For stochastic games, the evaluation function must return values that are a positive linear transformation of the probability of winning (or expected utility).

**Deduction Theorem (for game analysis):** H-MINIMAX(s) = EVAL(s) for cutoff states.

## 7. Data Structures

**Game Tree:** Nodes = states, edges = moves, leaves = terminal states with utility values

**Transposition Table:** Hash table caching heuristic values of states; keyed by state representation

**Endgame Table (Retrograde):** Complete map from every possible state to best move; constructed by working backwards from terminal positions

**Search Tree (MCTS):** Maintained incrementally; nodes store (wins/playouts); internal nodes represent explored states; expanded during iterations

## 8. Visual Patterns

**Figure 5.1:** Partial tic-tac-toe game tree — MAX (X) at root, alternating MIN (O) and MAX, leaf terminal states with utility values −1, 0, +1

**Figure 5.2:** Two-ply game tree — MAX root node (△) with three children B, C, D (MIN nodes ▽), each with three leaf children showing utility values

**Figure 5.5:** Stages of alpha–beta pruning on the two-ply tree from Fig 5.2:
- (a) First leaf below B = 3 → B at most 3
- (b) Second leaf = 12 → B still at most 3
- (c) Third leaf = 8 → B exactly 3 → root at least 3
- (d) First leaf below C = 2 → C at most 2 → prune remaining C children
- (e) First leaf below D = 14 → D at most 14 → explore more
- (f) D's children: 14, 5, 2 → D = 2

**Figure 5.10:** MCTS iteration:
- (a) Selection: root (37/100) → select 60/79 node → leaf 27/35
- (b) Expansion: new child (0/0); Simulation: playout → black wins
- (c) Back-propagation: 27/35→28/36, 60/79→61/80, 16/53→16/54, 37/100→37/101

**Figure 5.12:** Backgammon board layout (24-point double-triangle arrangement)

**Figure 5.13:** Schematic backgammon game tree with chance nodes (circles) for dice rolls

**Figure 5.15:** Guaranteed checkmate in KRK endgame on reduced board; Black king in 3 possible locations, narrowed by probing moves

## 9. Edge Cases/Exceptions/Traps

**Suboptimal opponent:** Playing minimax optimal against a suboptimal opponent may not be best; risky moves with high win probability against weak play may be preferable to guaranteed draw.

**Horizon effect:** Delaying tactics push unavoidable bad events beyond search horizon; mitigated by singular extensions.

**Quiescence failure:** Applying evaluation to nonquiescent position (e.g., Figure 5.8(b) where Black appears ahead but White captures queen next move).

**Zermelo's paradox:** In chess, the game tree has >10^40 nodes — cannot be fully enumerated.

**Infinite game trees:** If state space is unbounded or rules allow infinite repeating positions.

**Multiplayer alliances:** Alliances emerge naturally from selfish behavior; can be broken when no longer beneficial.

**Stochastic game evaluation:** Must be positive linear transformation of win probability, not just any order-preserving function (Figure 5.14: [1,2,3,4] → a1 best; [1,20,30,400] → a2 best).

**MCTS disadvantage:** Single critical move may be missed due to stochastic sampling; "obviously" winning positions still require many playout moves to verify.

**Averaging over clairvoyance failure:** In card games, assumes perfect information after deal; never bluffs, never gathers information, never hides information.

## 10. Empirical Evidence/Key Results

- Minimax complexity: O(b^m); chess would need ~10^123 states
- Alpha–beta with perfect ordering: O(b^(m/2)); chess effective branching factor ~6 (vs. 35)
- Typical chess program: ~1 million nodes/sec; 14-ply with alpha–beta + transposition table
- Top chess programs (Stockfish): reach depth 30+, exceed human ability
- 7-piece endgame table: 400 trillion positions; 8-piece: ~40 quadrillion
- PROBCUT beats regular Othello version 64% of time (with 2x time for regular)
- Libratus: 25 million CPU hours to beat poker pros
- n-queens: million-queens solved in avg 50 steps by min-conflicts (Chapter 6 cross-ref)
- AlphaZero: 155 wins, 6 losses vs Stockfish (2017 TCEC champion) in 1000 games
- AlphaGo: defeated Lee Sedol 4–1 (2015), Ke Jie 3–0 (2016)
- Chinook checkers solved: game is draw with perfect play; 39 trillion-entry endgame table; 18 CPU-years of search

## 11. Cross-Chapter Dependencies

- AND–OR search (Figure 4.11) → Minimax search generalization
- Iterative deepening (p. 80) → Used in alpha–beta with move ordering
- Heuristic functions (Chapter 3) → Basis for evaluation functions
- Machine learning (Chapter 22) → Learning evaluation function weights
- Reinforcement learning (Chapter 22) → MCTS as one kind (simulate, observe, determine good moves)
- Game theory, equilibrium (Section 18.2) → Optimal randomized strategies for partially observable games
- Decision theory (Chapter 16) → Value of computation in metareasoning; expected utility
- Planning with hierarchy (Section 11.4) → Abstract reasoning in games
- Belief states (Section 4.4) → Kriegspiel state estimation
- CSP (Chapter 6) → SAT reduction for propositional inference
- Neural networks → AlphaGo, AlphaZero playout policies

## 12. Dates & People

| Person | Contribution | Year |
|--------|-------------|------|
| Claude Shannon | Type A/B strategies, first chess paper | 1950 |
| John McCarthy | Conceived alpha–beta search | 1956 |
| Ernst Zermelo | Minimax algorithm (modern set theory) | 1912 |
| Charles Babbage | Feasibility of computer chess | 1846 |
| Leonardo Torres y Quevedo | First game-playing machine (KRK endgame) | ~1890 |
| Alan Turing | Game-playing programs | 1953 |
| Konrad Zuse | Early game-playing AI | 1945 |
| Norbert Wiener | Cybernetics, game playing | 1948 |
| Donald Knuth & Moore | Proved correctness of alpha–beta | 1975 |
| Judea Pearl | Alpha–beta asymptotic optimality | 1982 |
| Metropolis & Ulam | Monte Carlo simulation (atomic bomb) | 1949 |
| Bruce Abramson | Introduced MCTS | 1987 |
| Levente Kocsis & Csaba Szepesvári | UCT selection mechanism | 2006 |
| Gerald Tesauro | TD-Gammon (neural network + self-play) | 1995 |
| Deep Blue team (Campbell et al.) | Defeated Kasparov | 1997 |
| AlphaGo team (Silver et al.) | Defeated Lee Sedol | 2015 |
| AlphaZero (Silver et al.) | Defeated Stockfish | 2017 |
| Libratus (Brown & Sandholm) | Beat poker pros | 2017 |
| Garry Kasparov | World chess champion defeated by Deep Blue | 1997 |
| Jonathan Schaeffer | Chinook solved checkers | 2007 |
| MuZero (Schrittwieser et al.) | Learns rules by playing | 2019 |

## 13. Proof & Argument Patterns

**Alpha–Beta Pruning Correctness:** Show MINIMAX(root) = max(min(3,12,8), min(2,x,y), min(14,5,2)) = max(3, z, 2) where z ≤ 2, so = 3 independent of x,y. General principle: if Player has better choice at same level or higher, never move to n.

**Resolution completeness (Chapter 7 cross-reference):** Ground resolution theorem — if set of clauses is unsatisfiable, resolution closure contains empty clause.

**Guaranteed checkmate:** Strategy that works for every board state in belief state regardless of opponent movement.

## 14. Design Paradigms/Meta-Methods

- **Minimax principle:** Optimize for worst-case opponent
- **Pruning:** Eliminate irrelevant subtrees
- **Evaluation function design:** Strong correlation with win probability; weighted linear combination of features
- **Simulation-based evaluation:** Average over many playouts rather than heuristic function
- **Exploration vs. exploitation:** UCB1 balance
- **Metareasoning:** Reason about which computations are worth doing
- **Retrograde analysis:** Work backwards from terminal positions
- **Table lookup vs. search:** Use precomputed tables for openings and endgames

## 15. Case Studies/Classic Examples

**Tic-Tac-Toe (Figure 5.1):** Game tree with 9! = 362,880 terminal nodes (5,478 distinct states). MAX (X) vs MIN (O), utilities −1, 0, +1.

**Two-ply game tree (Figure 5.2):** MAX root → a1, a2, a3; MIN responses b1-b3, c1-c3, d1-d3; utilities 2–14. Minimax decision: a1 (value 3).

**Kriegspiel KRK endgame (Figure 5.15):** Black king in 3 possible locations; probing moves narrow to one; guaranteed checkmate.

**Backgammon position (Figure 5.12):** Black rolled 6–5, 4 legal moves; chance node with 21 distinct dice rolls (6 doubles at 1/36, 15 singles at 1/18).

## 16. Ethics

- AlphaZero's impact on chess community: "Chess has been shaken to its roots" (Kasparov)
- AlphaStar limited actions/minute to address fairness concerns about computer speed advantage
- Libratus detected opponent exploitation and plugged holes overnight
- MuZero learns rules without being told — generalization concerns

## 17. End-of-Chapter Material

**Key Terms:** adversarial search, minimax, alpha–beta pruning, evaluation function, quiescence, horizon effect, Monte Carlo tree search, expectiminimax, UCT, transposition table, forward pruning, retrograde analysis, Type A/B strategy, stochastic game, partially observable game, belief state, guaranteed checkmate, probabilistic checkmate

**Key Points Summary (p. 188):**
1. Game defined by: initial state, legal actions, result, terminal test, utility function
2. Minimax for deterministic two-player zero-sum perfect-information games
3. Alpha–beta prunes irrelevant subtrees
4. Heuristic evaluation function for cutoff search
5. MCTS evaluates by averaging playout results
6. Precomputed opening/endgame tables
7. Expectiminimax for games of chance
8. Partially observable games require belief state reasoning
9. Programs have defeated champions in chess, checkers, Othello, Go, poker

---

# CHAPTER 6: CONSTRAINT SATISFACTION PROBLEMS

## 1. Named Entities (Terms, Concepts, Algorithms)

| Term | Definition |
|------|------------|
| **Constraint satisfaction problem (CSP)** | Problem with factored state representation: set of variables, each with a value, all constraints satisfied |
| **Variable** | A factor in the state representation (X₁,..., Xₙ) |
| **Domain** | Set of allowable values for a variable (D₁,..., Dₙ) |
| **Constraint** | Specifies allowable combinations of values (scope + relation) |
| **Relation** | Defines values variables can take on; explicit set of tuples or function |
| **Assignment** | {Xᵢ=vᵢ, Xⱼ=vⱼ, ...} |
| **Consistent (legal) assignment** | Assignment that does not violate any constraints |
| **Complete assignment** | Every variable is assigned a value |
| **Solution** | A consistent, complete assignment |
| **Partial assignment** | Some variables left unassigned |
| **Partial solution** | Consistent partial assignment |
| **Constraint graph** | Nodes = variables, edges = constraints between variables |
| **Precedence constraint** | Task T₁ must occur before task T₂: T₁ + d₁ ≤ T₂ |
| **Disjunctive constraint** | Constraint that one of two conditions must hold (e.g., Axle F + 10 ≤ Axle B OR Axle B + 10 ≤ Axle F) |
| **Unary constraint** | Restricts value of a single variable |
| **Binary constraint** | Relates two variables |
| **Binary CSP** | Only unary and binary constraints |
| **Higher-order constraint** | Involves three or more variables |
| **Global constraint** | Constraint involving arbitrary number of variables (e.g., Alldiff) |
| **Alldiff constraint** | All involved variables must have different values |
| **Cryptarithmetic** | Puzzle where each letter represents a different digit |
| **Constraint hypergraph** | Graph with ordinary nodes (variables) and hypernodes (n-ary constraints) |
| **Dual graph transformation** | Convert n-ary CSP to binary: one variable per constraint, binary constraint between sharing pairs |
| **Absolute constraint** | Violation rules out a potential solution |
| **Preference constraint** | Indicates which solutions are preferred (can encode as costs) |
| **Constrained optimization problem (COP)** | CSP with preferences/costs; solved with optimization search |
| **Constraint propagation** | Using constraints to reduce legal values for variables |
| **Local consistency** | Enforcing consistency in each part of graph to eliminate inconsistent values |
| **Node consistency** | All values in variable's domain satisfy its unary constraints |
| **Arc consistency** | Every value in Dᵢ has some value in Dⱼ satisfying binary constraint on (Xᵢ, Xⱼ) |
| **AC-3** | Most popular arc consistency algorithm (queue of arcs) |
| **Path consistency** | Tightening binary constraints using implicit constraints from triples of variables |
| **k-consistency** | For any k−1 variables and consistent assignment, a consistent value exists for any kth variable |
| **Strongly k-consistent** | k-consistent AND (k−1)-consistent AND ... AND 1-consistent |
| **Resource constraint (Atmost)** | Sum of variables must not exceed bound |
| **Bounds propagation** | Managing domains by upper/lower bounds rather than explicit sets |
| **Bounds-consistent** | For every variable X, lower- and upper-bound values have satisfying values for all Y |
| **Sudoku** | 81-square puzzle; each row, column, 3×3 box has digits 1–9 without repetition |
| **Backtracking search** | DFS for CSPs; assigns one variable at a time, backtracks on failure |
| **Commutativity** | Order of application of actions doesn't matter (CSP property) |
| **Minimum-remaining-values (MRV) heuristic** | Choose variable with fewest legal values |
| **Degree heuristic** | Choose variable involved in most constraints on other unassigned variables |
| **Least-constraining-value heuristic** | Choose value that rules out fewest choices for neighbors |
| **Forward checking** | When X assigned, delete inconsistent values from connected unassigned Y's domains |
| **MAC (Maintaining Arc Consistency)** | After X assigned, run AC-3 starting with arcs from X to unassigned neighbors |
| **Chronological backtracking** | Back up to most recent decision point |
| **Conflict set** | Set of assignments in conflict with a value |
| **Backjumping** | Backtrack to most recent assignment in conflict set |
| **Conflict-directed backjumping** | Use conflict sets defined as preceding variables causing failure |
| **Constraint learning** | Finding minimum set of variables from conflict set causing problem |
| **No-good** | Minimum set of variable assignments that causes contradiction |
| **Min-conflicts heuristic** | Choose value resulting in minimum conflicts with other variables |
| **Constraint weighting** | Assign numeric weights to constraints; increment weights of violated constraints |
| **Independent subproblems** | Connected components of constraint graph |
| **Connected component** | Maximal set of nodes connected by edges in constraint graph |
| **Tree-structured CSP** | Constraint graph is a tree (any two variables connected by one path) |
| **Directional arc consistency (DAC)** | Under ordering X₁...Xₙ: every Xᵢ arc-consistent with Xⱼ for j > i |
| **Topological sort** | Ordering where each variable appears after its parent |
| **Cycle cutset** | Subset S such that constraint graph becomes tree after removing S |
| **Cutset conditioning** | Assign values to cutset variables, solve remaining tree |
| **Tree decomposition** | Transform graph into tree where each node is a set of variables |
| **Tree width** | One less than size of largest node in a tree decomposition; minimum over all decompositions |
| **Value symmetry** | Multiple solutions formed by permuting value names |
| **Symmetry-breaking constraint** | Constraint eliminating symmetric assignments |

## 2. Sequential Processes (Algorithms)

### AC-3 Algorithm
```
function AC-3(csp) returns false if inconsistency found, true otherwise
    queue ← a queue of arcs, initially all arcs in csp
    while queue is not empty do
        (Xᵢ, Xⱼ) ← POP(queue)
        if REVISE(csp, Xᵢ, Xⱼ) then
            if size of Dᵢ = 0 then return false
            for each Xₖ in Xᵢ.NEIGHBORS - {Xⱼ} do
                add (Xₖ, Xᵢ) to queue
    return true

function REVISE(csp, Xᵢ, Xⱼ) returns true iff we revise domain of Xᵢ
    revised ← false
    for each x in Dᵢ do
        if no value y in Dⱼ allows (x, y) to satisfy constraint between Xᵢ and Xⱼ then
            delete x from Dᵢ
            revised ← true
    return revised
```
- Complexity: O(cd³) where c = binary constraints, d = domain size
- Each arc inserted in queue at most d times
- Consistency check O(d²)

### Backtracking Search
```
function BACKTRACKING-SEARCH(csp) returns a solution or failure
    return BACKTRACK(csp, {})

function BACKTRACK(csp, assignment) returns a solution or failure
    if assignment is complete then return assignment
    var ← SELECT-UNASSIGNED-VARIABLE(csp, assignment)
    for each value in ORDER-DOMAIN-VALUES(csp, var, assignment) do
        if value is consistent with assignment then
            add {var=value} to assignment
            inferences ← INFERENCE(csp, var, assignment)
            if inferences ≠ failure then
                add inferences to csp
                result ← BACKTRACK(csp, assignment)
                if result ≠ failure then return result
                remove inferences from csp
            remove {var=value} from assignment
    return failure
```
Key insight: leaf nodes at depth n with branching factor d (not n!·dⁿ) due to commutativity.

### Tree-CSP-Solver
```
function TREE-CSP-SOLVER(csp) returns a solution or failure
    n ← number of variables
    assignment ← empty assignment
    root ← any variable
    X ← TOPOLOGICAL-SORT(X, root)
    for j = n down to 2 do
        MAKE-ARC-CONSISTENT(PARENT(Xⱼ), Xⱼ)
        if cannot be made consistent then return failure
    for i = 1 to n do
        assignment[Xᵢ] ← any consistent value from Dᵢ
        if no consistent value then return failure
    return assignment
```
- Complexity: O(n d²) linear in number of variables

### Min-Conflicts Local Search
```
function MIN-CONFLICTS(csp, max_steps) returns a solution or failure
    current ← an initial complete assignment for csp
    for i = 1 to max_steps do
        if current is a solution for csp then return current
        var ← a randomly chosen conflicted variable
        value ← value v for var that minimizes CONFLICTS(csp, var, v, current)
        set var = value in current
    return failure
```
- n-queens: 50 steps average for million-queens

## 3. Hierarchies/Classifications

**Domain types:**
- Discrete finite (e.g., {red, green, blue}) — most common
- Discrete infinite (e.g., integers) — need implicit constraints
- Continuous (e.g., real-valued time) — linear programming

**Constraint types by arity:**
- Unary (1 variable): e.g., SA ≠ green
- Binary (2 variables): e.g., SA ≠ NSW
- Higher-order/ternary (3+): e.g., Between(X,Y,Z)
- Global (arbitrary n): e.g., Alldiff, Atmost

**Constraint types by strictness:**
- Absolute constraints (must be satisfied)
- Preference constraints (costs on violations → COP)

**Local consistency levels:**
- Node consistency (1-consistency)
- Arc consistency (2-consistency)
- Path consistency (3-consistency)
- k-consistency
- Strong k-consistency

## 4. Comparisons/Trade-offs

| CSP Approach | When Best | Complexity | Memory |
|-------------|-----------|------------|--------|
| Backtracking (plain) | Small problems | O(dⁿ) | O(n) |
| Backtracking + Forward Checking | Moderate CSPs | Variable | O(nd) |
| Backtracking + MAC | Hard CSPs | Variable | O(nd) |
| Min-conflicts local search | Dense solutions | Very fast | O(n) |
| Tree-structured solver | Tree graphs | O(n d²) | O(n) |
| Cutset conditioning | Near-tree graphs | O(dᶜ · (n−c)d²) | O(n) |
| Tree decomposition | Low tree width | O(n d^(w+1)) | O(d^w) exponential |

**Forward checking vs. MAC:** MAC is strictly more powerful (recursive propagation); forward checking only propagates one step.

**Backjumping vs. Forward checking:** Every branch pruned by backjumping is also pruned by forward checking; simple backjumping redundant with forward checking or MAC.

**Cutset conditioning vs. Tree decomposition:**
- Cutset: O(dᶜ·(n−c)d²) time, linear memory
- Tree decomposition: O(n d^(w+1)) time, memory exponential in w
- Tree width w < c+1 typically; tree decomposition favored for time, cutset for memory

**MRV (fail-first) vs. Degree heuristic:** MRV usually more powerful; degree heuristic useful as tie-breaker.

**Variable ordering (fail-first) vs. Value ordering (fail-last):** Choose variables likely to fail first to minimize backtracking; choose values likely to succeed first because only one solution needed.

## 5. Formulas & Equations

**CSP definition:**
- X = {X₁,..., Xₙ} (variables)
- D = {D₁,..., Dₙ} (domains)
- C = {C₁,..., Cₘ} (constraints: scope + relation)

**Constraint example (greater-than):**
〈(X₁,X₂), {(3,1),(3,2),(2,1)}〉 or 〈(X₁,X₂), X₁ > X₂〉

**Precedence constraint:** T₁ + d₁ ≤ T₂

**Disjunctive constraint:** (Axle F + 10 ≤ Axle B) OR (Axle B + 10 ≤ Axle F)

**Cryptarithmetic column constraints:**
- O + O = R + 10·C₁
- C₁ + W + W = U + 10·C₂
- C₂ + T + T = O + 10·C₃
- C₃ = F

**Atmost constraint:** sum of min values > bound → inconsistency

**Bounds propagation example:**
- D₁ = [0,165], D₂ = [0,385]
- Constraint: F₁ + F₂ = 420
- Result: D₁ = [35,165], D₂ = [255,385]

**Tree-structured CSP time:** O(n d²)
**Cutset conditioning time:** O(dᶜ · (n−c) d²)
**Tree decomposition time:** O(n d^(w+1))
**Strong k-consistency solution time:** O(n² d)

## 6. Rules, Laws & Theorems

**Alldiff inconsistency detection:** If m variables involved have n possible distinct values and m > n, constraint cannot be satisfied.

**AC-3 property:** Equivalent to original CSP — same solutions, but smaller domains.

**K-consistency guarantee:** If CSP is strongly n-consistent, can solve in O(n² d) by choosing consistent values sequentially.

**Tree-structured CSP theorem:** Any tree-structured CSP can be solved in time linear in the number of variables.

**Bounded tree width theorem:** CSPs with constraint graphs of bounded tree width are solvable in polynomial time.

**Constraint satisfaction is NP-complete:** No general polynomial-time algorithm exists (unless P = NP).

**Cryptarithmetic reduction theorem:** Every finite-domain constraint can be reduced to a set of binary constraints if enough auxiliary variables are introduced (Exercise 6.NARY).

## 7. Data Structures

**Constraint graph:** Nodes = variables, edges = binary constraints

**Constraint hypergraph:** Nodes = variables, squares/hypernodes = n-ary constraints

**Dual graph:** Variables = original constraints; domains = tuples satisfying original constraints; edges = shared variables

**Search tree (CSP backtracking):** Each node = partial assignment; depth = n (all variables)

**Conflict set:** Set of variable assignments causing failure for a variable

**No-good:** Minimum set of variable-value pairs that causes contradiction (cached for constraint learning)

**Transposition table (Chapter 5 cross-ref):** Used in games for repeated states

## 8. Visual Patterns

**Figure 6.1:** Australia map with 7 regions (WA, NT, Q, NSW, V, SA, T); constraint graph with SA at center connected to WA, NT, Q, NSW, V; T isolated

**Figure 6.2:** Cryptarithmetic problem "TWO + TWO = FOUR"; constraint hypergraph with Alldiff at top and 4 column addition constraints (with carries C₁, C₂, C₃)

**Figure 6.4:** Sudoku puzzle (a) unsolved with given digits; (b) solved with all 81 squares filled

**Figure 6.6:** Search tree for map-coloring — levels: WA, NT, Q, NSW, V, SA, T; branches show color choices, backtracking on contradictions

**Figure 6.7:** Forward checking progress — domains listed for each variable after each assignment; SA domain becomes empty after WA=red, Q=green, V=blue

**Figure 6.8:** 8-queens min-conflicts two-step solution — numbers in squares show conflict count; Q₈→row 3, Q₆→row 8 gives 0 conflicts

**Figure 6.10:** Tree-structured CSP (a) with root A and children B, C, D; (b) topological sort A→B→C→D

**Figure 6.12:** Australia constraint graph (a) original with SA center; (b) after SA removal becomes forest of two trees

**Figure 6.13:** Tree decomposition — nodes: {WA,NT,SA}, {NT,SA,Q}, {SA,Q,NSW}, {SA,NSW,V}, {T}; SA appears in all connected nodes

## 9. Edge Cases/Exceptions/Traps

**Empty domain:** If AC-3 reduces domain to size 0, CSP has no solution.

**Tasmania independence:** Isolated in constraint graph — independent subproblem solvable separately.

**Nonlinear integer constraints:** General problem is undecidable.

**Infinite domains:** Cannot use explicit tuple enumeration; need implicit constraints.

**n-consistency is exponential:** Algorithm establishing n-consistency takes exponential time and space.

**Finding minimal tree width is NP-hard:** Heuristic methods required in practice.

**Finding smallest cycle cutset is NP-hard:** Approximation algorithms needed.

**Backjumping + forward checking redundancy:** Simple backjumping is redundant when forward checking or MAC is used.

**Value symmetry:** d! solutions from permuting value names → need symmetry-breaking constraints.

**Worst-case exponential:** Underconstrained = easy; overconstrained = easy; threshold region = hard.

## 10. Empirical Evidence/Key Results

- Australia map (7 variables, domain size 3): initially 243 assignments for 5 neighbors; after SA=blue, only 32
- Tic-tac-toe game tree: 9! = 362,880 terminal nodes (5,478 distinct states)
- n-queens: min-conflicts solves million-queens in average 50 steps
- Hubble Space Telescope scheduling: from 3 weeks to 10 minutes
- 100 Boolean variable CSP decomposition into 4 subproblems: from "lifetime of universe" to <1 second
- c=20 cutset on 100 Boolean variables: from "lifetime of universe" to a few minutes
- 30-variable tree decomposition node: centuries; 10-variable node: seconds

## 11. Cross-Chapter Dependencies

- State-space search (Chapters 3–4) → CSP as extension with factored representation
- Local search (Section 4.1) → Min-conflicts local search
- AND-OR search (Figure 4.11) → Tree-structured CSP solver patterns
- SAT problem (Chapter 7, Section 7.6.3) → CSP complexity, phase transition
- Probability/Bayesian networks (Chapter 13) → Cutset conditioning for probabilistic reasoning
- Constraint learning → SAT clause learning (Chapter 7)
- Symmetry breaking → used in SAT and combinatorial optimization
- Game tree search (Chapter 5) → transposition table cross-ref

## 12. Dates & People

| Person | Contribution | Year |
|--------|-------------|------|
| Diophantus | Algebraic constraints on equations | ~200–284 CE |
| Brahmagupta | Solution for ax+by=c over integers | ~650 CE |
| Gauss (C. F.) | Variable elimination; recursive backtracking for 8-queens | 1829/1850 |
| Fourier | Linear inequality constraints | 1827 |
| Appel & Haken | Four-color theorem proof | 1977 |
| Georges Gonthier | Formal proof of four-color theorem in Coq | 2008 |
| Ugo Montanari | CSP as general class; constraint graphs; path consistency | 1974 |
| Alan Mackworth | AC-3; PC-2; combining backtracking with consistency | 1977 |
| Waltz | Constraint propagation for vision (line labeling) | 1975 |
| Freuder | k-consistency theory | 1978, 1982 |
| Gaschnig | Backjumping; MAC | 1977, 1979 |
| Prosser | Conflict-directed backjumping | 1993 |
| Dechter | Cycle cutset; graph-based backjumping | 1990 |
| Pearl & Dechter | Tree decomposition/induced width | 1987, 1989 |
| Robertson & Seymour | Tree width concept | 1986 |
| Minton et al. | Min-conflicts heuristic | 1992 |
| Gu | Min-conflicts (independent) | 1989 |
| Cheeseman et al. | "Easy" and "hard" problems; phase transition | 1991 |
| Stallman & Sussman | Dependency-directed backtracking | 1977 |
| Ginsberg | Dynamic backtracking | 1993 |

## 13. Proof & Argument Patterns

**Tree-structured CSP solvability:** By establishing directional arc consistency (parent→child for each edge in topological order), then assigning variables in topological order, each parent has valid value for child — no backtracking needed.

**Reduction of n-ary to binary CSP:** Using auxiliary variables or dual graph transformation (Exercise 6.NARY).

**Conflict-directed backjumping conflict set propagation:** conf(Xᵢ) ← conf(Xᵢ) ∪ conf(Xⱼ) − {Xᵢ}.

**Counting arguments for Alldiff:** If m variables, n values, m > n → unsatisfiable.

## 14. Design Paradigms/Meta-Methods

- **Factored representation:** Break black-box states into variables
- **Constraint propagation:** Inference to reduce search space
- **Backtracking search:** DFS + commutativity + domain-independent heuristics
- **Variable ordering heuristics:** Choose most constrained variable first (fail-fast)
- **Value ordering heuristics:** Choose least constraining value first (fail-last)
- **Local search:** Complete assignments, min-conflicts, plateau search, tabu search
- **Divide and conquer:** Connected components, cutset conditioning, tree decomposition
- **Decomposition:** Break into independent/tree subproblems
- **Symmetry breaking:** Reduce search space by eliminating symmetric solutions
- **Constraint learning:** Record no-goods to avoid repeating failures

## 15. Case Studies/Classic Examples

**Australia Map Coloring (Section 6.1.1):** 7 variables, 9 constraints, 3 colors. Solution: {WA=red, NT=green, Q=red, NSW=green, V=red, SA=blue, T=red}.

**Job-Shop Scheduling (Section 6.1.2):** 15 tasks for car assembly: Axle F/B, 4 Wheels, 4 Nuts, 4 Hubcaps, Inspect. Precedence constraints (axle before wheel before nuts before hubcap), disjunctive constraint (axle tools), domain {0,...,30} minutes.

**Cryptarithmetic (Section 6.1.3):** TWO + TWO = FOUR. Alldiff(F,T,U,W,R,O). Column constraints with carries C₁, C₂, C₃.

**8-Queens (Section 6.1.3/6.4):** Variables Q₁...Q₈ (columns), domains {1,...,8} (rows), constraints: no same row or diagonal. Solved by min-conflicts in 2 steps.

**Sudoku (Section 6.2.6):** 81 variables, domains {1,...,9}, 27 Alldiff constraints (9 rows + 9 columns + 9 boxes). AC-3 solves easy puzzles; PC-2 solves harder ones (255,960 path constraints); "naked triples" strategy for human solvers.

**Hubble Space Telescope Scheduling:** Converted from 3 weeks to 10 minutes using min-conflicts.

## 16. Ethics

- Preference constraints encode varying stakeholder priorities
- Automated scheduling affects labor conditions (airline crews)
- NSW ≠ SA constraint as social/political boundary respect

## 17. End-of-Chapter Material

**Key Terms:** constraint satisfaction problem, constraint graph, node/arc/path/k-consistency, AC-3, backtracking search, MRV, degree heuristic, least-constraining-value, forward checking, MAC, backjumping, conflict-directed backjumping, constraint learning, no-good, min-conflicts, tree-structured CSP, cycle cutset, tree decomposition, tree width, value symmetry

**Key Points Summary:**
1. CSP = variables + domains + constraints
2. Inference techniques: node, arc, path, k-consistency
3. Backtracking search: depth-first with domain-independent heuristics
4. Variable ordering: MRV (most constrained), degree heuristic (tiebreaker)
5. Value ordering: least-constraining-value
6. Backjumping: jump to source of conflict; conflict-directed backjumping: deeper analysis
7. Constraint learning: record no-goods
8. Min-conflicts local search: highly effective (million-queens in 50 steps)
9. Complexity related to constraint graph structure: linear for trees; cutset/tree decomposition for general graphs

---

# CHAPTER 7: LOGICAL AGENTS

## 1. Named Entities (Terms, Concepts, Algorithms)

| Term | Definition |
|------|------------|
| **Knowledge-based agent** | Agent using reasoning over internal knowledge representation to decide actions |
| **Reasoning** | Process of deriving new representations about the world |
| **Representation** | Internal encoding of knowledge about the world |
| **Knowledge base (KB)** | Set of sentences in a knowledge representation language |
| **Sentence** | Expression in knowledge representation language representing an assertion about the world |
| **Knowledge representation language** | Language used to express sentences in the KB |
| **Axiom** | Sentence given without being derived from other sentences |
| **TELL** | Operation to add new sentences to the KB |
| **ASK** | Operation to query what is known |
| **Inference** | Deriving new sentences from old |
| **Background knowledge** | Initial knowledge in the KB |
| **Knowledge level** | Description of agent specifying only what it knows and its goals |
| **Implementation level** | How the knowledge is actually represented/processed |
| **Declarative approach** | Building agent by TELLing it sentences |
| **Procedural approach** | Encoding desired behaviors as program code |
| **Wumpus world** | Cave environment: agent, wumpus, pits, gold; used as AI testbed |
| **Model** | Mathematical abstraction with fixed truth value for every relevant sentence |
| **Possible world** | Real or hypothetical environment (vs. formal model) |
| **Satisfaction** | Model m satisfies sentence α (m is a model of α) if α is true in m |
| **M(α)** | Set of all models of α |
| **Entailment (⊧)** | α ⊧ β iff in every model where α is true, β is also true; M(α) ⊆ M(β) |
| **Logical inference** | Deriving conclusions from premises |
| **Model checking** | Enumerating models to check entailment |
| **Soundness (truth-preserving)** | Inference algorithm deriving only entailed sentences |
| **Completeness** | Inference algorithm deriving all entailed sentences |
| **Grounding** | Connection between logical reasoning and real environment |
| **Propositional logic** | Logic with propositions and logical connectives |
| **Proposition symbol** | Atomic sentence standing for a proposition (true/false) |
| **Atomic sentence** | Single proposition symbol (e.g., P, Q, W₁,₃) |
| **Complex sentence** | Constructed from simpler sentences with connectives |
| **Logical connectives** | ¬ (not), ∧ (and), ∨ (or), ⇒ (implies), ⇔ (iff) |
| **Negation** | ¬P — true iff P is false |
| **Literal** | Atomic sentence (positive literal) or negated atomic sentence (negative literal) |
| **Conjunction** | P∧Q — true iff both P and Q are true; parts are conjuncts |
| **Disjunction** | P∨Q — true iff either P or Q is true; parts are disjuncts |
| **Implication (conditional)** | P⇒Q — false only when P true and Q false; premise/antecedent, conclusion/consequent |
| **Biconditional** | P⇔Q — true iff P and Q both true or both false |
| **Truth value** | True or false for each proposition symbol in a model |
| **Truth table** | Table specifying truth value of complex sentence for each assignment |
| **Theorem proving** | Applying rules of inference to construct proof |
| **Logical equivalence (≡)** | α≡β iff α and β true in same set of models |
| **Validity** | Sentence true in all models; tautology |
| **Deduction theorem** | α ⊧ β iff (α⇒β) is valid |
| **Satisifiability** | Sentence true in (satisfied by) some model |
| **SAT problem** | Determining satisfiability of propositional sentence (first NP-complete problem) |
| **Reductio ad absurdum** | Proof by contradiction / refutation |
| **Inference rules** | Patterns for deriving new sentences from old |
| **Proof** | Chain of conclusions leading to desired goal |
| **Modus Ponens** | From α⇒β and α, infer β |
| **And-Elimination** | From α∧β, infer α (or β) |
| **Monotonicity** | If KB ⊧ α then KB∧β ⊧ α for any β |
| **Resolution** | Single inference rule yielding complete inference algorithm |
| **Complementary literals** | One literal is negation of the other |
| **Clause** | Disjunction of literals |
| **Unit clause** | Clause with one literal |
| **Unit resolution** | Resolving clause with single literal |
| **Resolvent** | New clause from resolution: all literals except complementary pair |
| **Factoring** | Removing duplicate copies of literals from resolvent |
| **Conjunctive normal form (CNF)** | Sentence expressed as conjunction of clauses |
| **Resolution closure (RC(S))** | Set of all clauses derivable by repeated resolution from S |
| **Ground resolution theorem** | If set of clauses is unsatisfiable, resolution closure contains empty clause |
| **Definite clause** | Disjunction with exactly one positive literal |
| **Horn clause** | Disjunction with at most one positive literal |
| **Goal clause** | Horn clause with no positive literals |
| **k-CNF** | CNF sentence where each clause has at most k literals |
| **Body** | Premise of implication in Horn form (conjunction of positive literals) |
| **Head** | Conclusion in Horn form (single positive literal) |
| **Fact** | Sentence with single positive literal |
| **Forward chaining** | Data-driven reasoning from known facts to query |
| **Backward chaining** | Goal-directed reasoning from query back to known facts |
| **Data-driven reasoning** | Reasoning from known data, without specific query |
| **Goal-directed reasoning** | Reasoning backward from query |
| **DPLL (Davis–Putnam–Logemann–Loveland)** | Complete backtracking SAT algorithm with early termination, pure symbol, unit clause heuristics |
| **Pure symbol** | Symbol appearing with same sign in all clauses |
| **Unit propagation** | Cascade of forced assignments from unit clauses |
| **WALKSAT** | Local search SAT algorithm; picks random unsat clause, flips symbol (min-conflict or random) |
| **Early termination** | Detecting sentence true/false with partial model |
| **Component analysis** | Separating disjoint clause subsets with no shared variables |
| **Random restart** | Restarting search with different random choices |
| **Satisifiability threshold conjecture** | For each k≥3, ratio r_k where random k-CNF goes from satisfiable to unsatisfiable |
| **Fluent** | Aspect of world that changes over time (synonym for "state variable") |
| **Atemporal variable** | Permanent aspect of world (no time index) |
| **Effect axiom** | Axiom specifying outcome of action at next time step |
| **Frame problem** | Need to specify what remains unchanged after action |
| **Frame axiom** | Axiom asserting a proposition remains unchanged |
| **Representational frame problem** | Proliferation of frame axioms O(mn) |
| **Locality** | Each action changes no more than small k fluents |
| **Inferential frame problem** | Projecting t-step plan in O(kt) vs. O(nt) |
| **Successor-state axiom** | Axiom defining F^(t+1) in terms of F^t and actions |
| **Qualification problem** | Specifying all preconditions/exceptions for action to succeed |
| **Hybrid agent** | Combines logical inference with search algorithms (A*) |
| **Caching** | Saving inference results for constant update time |
| **Conservative approximation** | Outer envelope of belief state (e.g., 1-CNF) |
| **SATP LAN** | Propositional planning procedure; translates planning to SAT |
| **Precondition axiom** | States action occurrence requires preconditions |
| **Action exclusion axiom** | Says two actions cannot occur simultaneously |

## 2. Sequential Processes (Algorithms)

### KB-Agent
```
function KB-AGENT(percept) returns an action
    persistent: KB, a knowledge base
                t, a counter, initially 0, indicating time
    TELL(KB, MAKE-PERCEPT-SENTENCE(percept, t))
    action ← ASK(KB, MAKE-ACTION-QUERY(t))
    TELL(KB, MAKE-ACTION-SENTENCE(action, t))
    t ← t + 1
    return action
```
Three steps per cycle: TELL percept → ASK action → TELL action

### TT-Entails? (Model Checking)
```
function TT-ENTAILS?(KB, α) returns true or false
    symbols ← list of proposition symbols in KB and α
    return TT-CHECK-ALL(KB, α, symbols, {})

function TT-CHECK-ALL(KB, α, symbols, model) returns true or false
    if EMPTY?(symbols) then
        if PL-TRUE?(KB, model) then return PL-TRUE?(α, model)
        else return true
    else
        P ← FIRST(symbols); rest ← REST(symbols)
        return (TT-CHECK-ALL(KB, α, rest, model ∪ {P=true})
                and TT-CHECK-ALL(KB, α, rest, model ∪ {P=false}))
```
- Complexity: O(2ⁿ) time, O(n) space (depth-first)
- Requires n symbols → 2ⁿ models

### PL-Resolution
```
function PL-RESOLUTION(KB, α) returns true or false
    clauses ← set of clauses in CNF of KB ∧ ¬α
    new ← {}
    while true do
        for each pair Cᵢ, Cⱼ in clauses do
            resolvents ← PL-RESOLVE(Cᵢ, Cⱼ)
            if resolvents contains empty clause then return true
            new ← new ∪ resolvents
        if new ⊆ clauses then return false
        clauses ← clauses ∪ new
```

### DPLL
```
function DPLL-SATISFIABLE?(s) returns true or false
    clauses ← CNF representation of s
    symbols ← proposition symbols in s
    return DPLL(clauses, symbols, {})

function DPLL(clauses, symbols, model) returns true or false
    if every clause in clauses is true in model then return true
    if some clause in clauses is false in model then return false
    P, value ← FIND-PURE-SYMBOL(symbols, clauses, model)
    if P is non-null then return DPLL(clauses, symbols–P, model∪{P=value})
    P, value ← FIND-UNIT-CLAUSE(clauses, model)
    if P is non-null then return DPLL(clauses, symbols–P, model∪{P=value})
    P ← FIRST(symbols); rest ← REST(symbols)
    return DPLL(clauses, rest, model∪{P=true}) or
           DPLL(clauses, rest, model∪{P=false})
```
Improvements:
1. Early termination (true if any literal true; false if any clause false)
2. Pure symbol heuristic
3. Unit clause heuristic (unit propagation)

### WalkSAT
```
function WALKSAT(clauses, p, max_flips) returns a satisfying model or failure
    model ← random assignment of true/false to symbols in clauses
    for i = 1 to max_flips do
        if model satisfies clauses then return model
        clause ← randomly selected false clause
        if RANDOM(0,1) ≤ p then
            flip value of randomly selected symbol in clause
        else flip whichever symbol maximizes number of satisfied clauses
    return failure
```
- p typically ~0.5
- Sound but not complete (cannot detect unsatisfiability reliably)

### PL-FC-Entails? (Forward Chaining)
```
function PL-FC-ENTAILS?(KB, q) returns true or false
    count ← table: count[c] initially number of symbols in clause c's premise
    inferred ← table: inferred[s] initially false for all symbols
    queue ← queue of symbols initially known true in KB
    while queue is not empty do
        p ← POP(queue)
        if p = q then return true
        if inferred[p] = false then
            inferred[p] ← true
            for each clause c in KB where p is in c.PREMISE do
                decrement count[c]
                if count[c] = 0 then add c.CONCLUSION to queue
    return false
```
- Runs in linear time
- Sound and complete for definite clauses

### SATPLAN
```
function SATPLAN(init, transition, goal, Tmax) returns solution or failure
    for t = 0 to Tmax do
        cnf ← TRANSLATE-TO-SAT(init, transition, goal, t)
        model ← SAT-SOLVER(cnf)
        if model is not null then return EXTRACT-SOLUTION(model)
    return failure
```

### Hybrid Wumpus Agent
```
function HYBRID-WUMPUS-AGENT(percept) returns an action
    persistent: KB, t, plan
    TELL(KB, MAKE-PERCEPT-SENTENCE(percept, t))
    TELL KB the temporal "physics" sentences for time t
    safe ← {[x,y]: ASK(KB, OKᵗ_xy) = true}
    if ASK(KB, Glitterᵗ) = true then
        plan ← [Grab] + PLAN-ROUTE(current, {[1,1]}, safe) + [Climb]
    if plan is empty then
        unvisited ← {[x,y]: ASK(KB, Lᵗ'_xy) = false for all t'≤t}
        plan ← PLAN-ROUTE(current, unvisited ∩ safe, safe)
    if plan is empty and ASK(KB, HaveArrowᵗ) = true then
        possible_wumpus ← {[x,y]: ASK(KB, ¬W_xy) = false}
        plan ← PLAN-SHOT(current, possible_wumpus, safe)
    if plan is empty then
        notunsafe ← {[x,y]: ASK(KB, ¬OKᵗ_xy) = false}
        plan ← PLAN-ROUTE(current, unvisited ∩ notunsafe, safe)
    if plan is empty then
        plan ← PLAN-ROUTE(current, {[1,1]}, safe) + [Climb]
    action ← POP(plan)
    TELL(KB, MAKE-ACTION-SENTENCE(action, t))
    t ← t + 1
    return action
```

## 3. Hierarchies/Classifications

**Knowledge representation hierarchy:**
- Atomic representation (Ch 3-4): state as black box
- Factored representation (Ch 6): state as variables with values
- Structured representation (Ch 8): logic with objects and relations

**Sentence types in grammar (Figure 7.7):**
```
Sentence → AtomicSentence | ComplexSentence
AtomicSentence → True | False | P | Q | R | ...
ComplexSentence → (Sentence) | ¬Sentence | Sentence∧Sentence 
                  | Sentence∨Sentence | Sentence⇒Sentence | Sentence⇔Sentence
```
Operator precedence (highest to lowest): ¬, ∧, ∨, ⇒, ⇔

**Clause forms (Figure 7.12):**
- CNF: Clause₁ ∧ ... ∧ Clauseₙ; each Clause = Literal₁ ∨ ... ∨ Literalₘ
- Horn clause: at most one positive literal
- Definite clause: exactly one positive literal
- Goal clause: zero positive literals (implication concluding False)

**Agent architectures:**
- Declarative (tell sentences) vs. Procedural (encode code)
- KB-Agent (pure logical) vs. Hybrid-Agent (logical + search)

## 4. Comparisons/Trade-offs

| Method | Sound | Complete | Best For |
|--------|-------|----------|----------|
| TT-Entails? (model checking) | Yes | Yes | Small n |
| DPLL (backtracking SAT) | Yes | Yes | General SAT |
| WalkSAT (local search SAT) | Yes | No | Satisfiable problems |
| PL-Resolution | Yes | Yes | Theorem proving |
| Forward chaining | Yes | Yes (definite clauses) | Data-driven |
| Backward chaining | Yes | Yes (definite clauses) | Goal-directed |
| SATPLAN | Yes | Yes (bounded) | Planning |

**Model checking vs. Theorem proving:**
- Model checking: O(2ⁿ) time, exhaustive
- Theorem proving: can ignore irrelevant propositions; may be faster with long KB

**Declarative vs. Procedural:**
- Declarative: TELL sentences, easy to extend
- Procedural: efficient, harder to modify
- Modern approach: combine both, compile declarative to procedural

**Forward vs. Backward chaining:**
- Forward: data-driven; may derive irrelevant facts
- Backward: goal-directed; touches only relevant facts

**SATPLAN surprises:**
- Needs "exactly one location" axioms (can't be in two places at once)
- Needs precondition axioms (can't shoot without arrow)
- Needs action exclusion axioms (can't do two actions simultaneously)

## 5. Formulas & Equations

**Entailment definition:**
α ⊧ β iff M(α) ⊆ M(β)

**Deduction theorem:**
α ⊧ β iff (α ⇒ β) is valid

**Refutation equivalence:**
α ⊧ β iff (α ∧ ¬β) is unsatisfiable

**Modus Ponens:**
α⇒β, α ⊢ β

**And-Elimination:**
α∧β ⊢ α

**Unit Resolution:**
(ℓ₁ ∨ ... ∨ ℓₖ), m ⊢ ℓ₁ ∨ ... ∨ ℓᵢ₋₁ ∨ ℓᵢ₊₁ ∨ ... ∨ ℓₖ
where ℓᵢ and m are complementary

**Full Resolution:**
(ℓ₁ ∨ ... ∨ ℓₖ), (m₁ ∨ ... ∨ mₙ) ⊢ ℓ₁ ∨ ... ∨ ℓᵢ₋₁ ∨ ℓᵢ₊₁ ∨ ... ∨ ℓₖ ∨ m₁ ∨ ... ∨ mⱼ₋₁ ∨ mⱼ₊₁ ∨ ... ∨ mₙ
where ℓᵢ and mⱼ are complementary

**CNF Conversion Steps:**
1. Eliminate ⇔ (replace with (α⇒β)∧(β⇒α))
2. Eliminate ⇒ (replace with ¬α∨β)
3. Move ¬ inwards (De Morgan, double-negation elimination)
4. Distribute ∨ over ∧

**Truth table semantics (Figure 7.8):**
| P | Q | ¬P | P∧Q | P∨Q | P⇒Q | P⇔Q |
|---|---|----|-----|-----|------|-----|
| F | F | T | F | F | T | T |
| F | T | T | F | T | T | F |
| T | F | F | F | T | F | F |
| T | T | F | T | T | T | T |

**Successor-state axiom template:**
F^(t+1) ⇔ ActionCausesF^t ∨ (F^t ∧ ¬ActionCausesNotF^t)

**Example: HaveArrow:**
HaveArrow^(t+1) ⇔ (HaveArrow^t ∧ ¬Shoot^t)

**Example: Location [1,1]:**
L^(t+1)_₁,₁ ⇔ (L^t_₁,₁ ∧ (¬Forward^t ∨ Bump^(t+1)))
               ∨ (L^t_₁,₂ ∧ (FacingSouth^t ∧ Forward^t))
               ∨ (L^t_₂,₁ ∧ (FacingWest^t ∧ Forward^t))

**OK axiom:**
OK^t_xy ⇔ ¬P_xy ∧ ¬(W_xy ∧ WumpusAlive^t)

**Logical equivalences (Figure 7.11):**
- (α∧β) ≡ (β∧α) — commutativity of ∧
- (α∨β) ≡ (β∨α) — commutativity of ∨
- ((α∧β)∧γ) ≡ (α∧(β∧γ)) — associativity of ∧
- ((α∨β)∨γ) ≡ (α∨(β∨γ)) — associativity of ∨
- ¬(¬α) ≡ α — double-negation elimination
- (α⇒β) ≡ (¬β⇒¬α) — contraposition
- (α⇒β) ≡ (¬α∨β) — implication elimination
- (α⇔β) ≡ ((α⇒β)∧(β⇒α)) — biconditional elimination
- ¬(α∧β) ≡ (¬α∨¬β) — De Morgan
- ¬(α∨β) ≡ (¬α∧¬β) — De Morgan
- (α∧(β∨γ)) ≡ ((α∧β)∨(α∧γ)) — distributivity of ∧ over ∨
- (α∨(β∧γ)) ≡ ((α∨β)∧(α∨γ)) — distributivity of ∨ over ∧

## 6. Rules, Laws & Theorems

**Entailment formal definition:** α ⊧ β iff M(α) ⊆ M(β)

**Monotonicity:** If KB ⊧ α then KB∧β ⊧ α for any β

**Deduction theorem:** α ⊧ β iff (α⇒β) is valid

**Ground resolution theorem:** If set of clauses is unsatisfiable, resolution closure contains empty clause

**Proof by contradiction (refutation):** To show KB ⊧ α, show KB∧¬α is unsatisfiable

**Validity-satisfiability connection:** α is valid iff ¬α is unsatisfiable; α is satisfiable iff ¬α is not valid

**Refutation equivalence:** α ⊧ β iff (α∧¬β) is unsatisfiable

**NP-completeness of SAT:** Propositional entailment is co-NP-complete; SAT is NP-complete

**Forward chaining completeness:** Every entailed atomic sentence will be derived (for definite clauses)

**Horn clause closure:** Horn clauses are closed under resolution

**Linear time inference for Horn clauses:** Deciding entailment with Horn clauses is O(size of KB)

## 7. Data Structures

**Knowledge Base:** Set of sentences in a knowledge representation language

**Model:** Assignment of truth values to all proposition symbols (2ⁿ possible models for n symbols)

**Truth table:** Matrix with 2ⁿ rows of truth assignments, n+1 columns (n symbols + sentence)

**AND–OR graph:** Used for forward/backward chaining on Horn clauses; multiple edges joined by arc = conjunction; without arc = disjunction

**CNF clause set:** Set of clauses (each a disjunction of literals) used by resolution and DPLL

**Resolution closure:** Set of all derivable clauses (finite for finite symbols)

**Belief state (1-CNF):** Conjunction of provable literals; conservative approximation of exact belief state

**Count table (forward chaining):** Tracks number of premises yet to be proven for each clause

**Inferred table (forward chaining):** Tracks which symbols already processed

## 8. Visual Patterns

**Figure 7.2:** Wumpus world 4×4 grid: [1,1]=Start, stench near wumpus [1,3], breeze near pits, gold in [2,3], pits in [3,1], [3,3], [4,4]

**Figure 7.3:** Agent's knowledge after first step:
- (a) [1,1]: no percept → OK, [1,2], [2,1] OK
- (b) [2,1]: breeze → P? in [2,2], [3,1]; [1,1] OK visited

**Figure 7.4:** Later stages:
- (a) [1,2]: stench → W! in [1,3]; no breeze → ¬pit in [2,2] → pit must be in [3,1]
- (b) [2,3]: stench, breeze, glitter → grab gold

**Figure 7.5:** Eight possible models for pits in [1,2],[2,2],[3,1]; KB true in 3 models; α₁ (¬P₁,₂) true in all 3 → entailed; α₂ (¬P₂,₂) false in 1 of 3 → not entailed

**Figure 7.6:** World ↔ Representation diagram: Sentences ↔ Aspects of real world; Inference ←→ Entailment

**Figure 7.9:** Truth table for wumpus KB: 7 symbols → 128 rows; KB true in 3 rows (underlined); P₁,₂ false in all 3 → ¬P₁,₂ entailed

**Figure 7.14:** Resolution proof for ¬P₁,₂: 4 clauses (KB∧¬α) at top; resolution steps produce ¬P₁,₂; resolved with P₁,₂ → empty clause (□)

**Figure 7.16:** AND-OR graph for Horn clauses:
- A, B facts → A∧B ⇒ L; B∧L ⇒ M; A∧P ⇒ L; L∧M ⇒ P; P ⇒ Q
- Forward: A,B → L → M → P → Q

**Figure 7.19:** SAT phase transition:
- (a) Probability of satisfiability vs. m/n: drops sharply near 4.3 for 3-CNF with 50 symbols
- (b) Median run time peaks at m/n ≈ 4.3 for both DPLL and WalkSAT

**Figure 7.21:** 1-CNF belief state as conservative envelope around exact belief state

## 9. Edge Cases/Exceptions/Traps

**Implication truth table confusion:** P⇒Q is true when P is false (vacuously true). "5 is even ⇒ Sam is smart" is true regardless of Sam's smartness.

**Exclusive or (xor):** P∨Q in logic is inclusive OR; different from English "either...or" which is often exclusive.

**Grounding problem:** How does KB connect to real world? Sensors create the connection; general rules from learning may be fallible.

**Model checking infinite models:** If model space is infinite (e.g., arithmetic), model checking doesn't work.

**Qualification problem:** Cannot specify all exceptions to action preconditions (giant bats, heart attacks, etc.)

**SATP LAN spurious solutions:** Without additional axioms:
- L²_₁,₁ can be true by being there at time 0 — need "exactly one location"
- Can shoot without arrow — need precondition axioms
- Can do multiple simultaneous actions — need action exclusion axioms

**SATP LAN partial observability limitation:** SATPLAN sets unobservable variables to whatever values needed — can't use in partially observable environments.

**WalkSAT can't detect unsatisfiability:** Returns "I couldn't find a model" not "no model exists" — not a proof.

**Logical state estimation exponential:** 2ⁿ physical states, 2^(2ⁿ) belief states; exact representation may be exponential.

**Inference irrelevance:** Even with millions of sentences, theorem proving can ignore irrelevant ones; truth table cannot.

**Monotonicity restriction:** KB can only grow — cannot retract conclusions (unlike human reasoning).

## 10. Empirical Evidence/Key Results

- TT-Entails? with 7 symbols: 128 models; 3 satisfy KB
- DPLL on 1962 hardware: 10-15 variables; by 1995 (SATz): 1,000 variables; modern Chaff: millions of variables
- WalkSAT phase transition peak at m/n ≈ 4.3 for 50-variable 3-CNF
- Underconstrained (m/n=3.3): 20× easier than threshold
- Overconstrained problems: easier than threshold but harder than underconstrained
- Propositional entailment is co-NP-complete
- Horn clause inference: linear time
- Forward chaining completeness: all entailed atomic sentences derived at fixed point

## 11. Cross-Chapter Dependencies

- Search (Ch 3-4) → proof as search problem; A* used in hybrid agent; iterative deepening
- CSP (Ch 6) → SAT as special case; constraint learning, backjumping used in SAT solvers
- First-order logic (Ch 8) → propositional logic insufficient for general patterns ("for each time t")
- Logic programming (Ch 9) → Horn clauses, forward/backward chaining
- Neural networks (Ch 19+) → McCulloch-Pitts Boolean circuits; AlphaGo/AlphaZero neural policies
- Probability (Ch 12-16) → handles qualification problem; uncertain reasoning
- Planning (Ch 11) → SATPLAN; hierarchy of abstraction
- Game theory (Ch 18) → equilibrium strategies
- Learning (Ch 19-22) → grounding general rules; reinforcement learning
- Philosophy (Ch 27) → grounding problem

## 12. Dates & People

| Person | Contribution | Year |
|--------|-------------|------|
| Aristotle | Organon, syllogisms | ~350 BCE |
| Philo of Megara | Truth tables | ~300 BCE |
| Stoics | Modus Ponens as basic inference rule | ~300 BCE |
| Leibniz | Mechanical logical inference | 1646–1716 |
| Boole | First comprehensive formal logic | 1847 |
| Frege | Begriffschrift (modern logic) | 1879 |
| Schröder | Conjunctive normal form | 1877 |
| Horn | Horn form | 1951 |
| McCarthy | Knowledge-based agents, "Programs with Common Sense" | 1958 |
| Newell, Shaw, Simon | Logic Theorist | 1957 |
| Davis | First computer logical inference | 1954 |
| Davis & Putnam | Davis-Putnam algorithm; DPLL | 1960, 1962 |
| J. A. Robinson | Resolution rule (first-order) | 1965 |
| Cook | SAT is NP-complete | 1971 |
| Wittgenstein | Tractatus; truth tables | 1922 |
| Post | Truth tables for validity testing | 1921 |
| McCulloch & Pitts | Boolean circuit-based agents | 1943 |
| Rosenschein | Circuit-based agents from declarative descriptions | 1985 |
| Reiter | Successor-state axioms (frame problem solution) | 1991 |
| Kautz & Selman | SATPLAN (temporal propositional variables) | 1992 |
| Brooks | Behavior-based (circuit-based) robots | 1986, 1989 |
| Moskewicz et al. | Chaff SAT solver | 2001 |
| Selman et al. | GSAT, WalkSAT | 1992, 1996 |
| Yob | Invented wumpus world | 1975 |
| Genesereth | Wumpus world as AI testbed | - |

## 13. Proof & Argument Patterns

**Ground resolution theorem proof structure:**
1. Prove contrapositive: if RC(S) has no empty clause, S is satisfiable
2. Construct model by assigning truth values to P₁...Pₖ sequentially
3. For each Pᵢ: if clause ¬Pᵢ (with all other literals false) in RC(S), set Pᵢ=false; else set true
4. Assume contradiction: some clause C becomes false at step i
5. Show both (false∨...∨false∨Pᵢ) and (false∨...∨false∨¬Pᵢ) must be in RC(S)
6. Resolution gives clause with all literals false from P₁...Pᵢ₋₁ — contradicts "first falsified" assumption

**Forward chaining completeness proof:**
1. Consider fixed point (no new inferences possible)
2. View inferred table as logical model
3. Every definite clause is true in this model
4. Any entailed q must be true in all models, including this one
5. Therefore q must have been inferred

**Refutation proof pattern:**
To derive α from KB: assume ¬α, derive contradiction, conclude α

**Model checking proof pattern:**
Check M(KB) ⊆ M(α) by enumerating all models

## 14. Design Paradigms/Meta-Methods

- **Knowledge-level design:** Specify what agent knows and wants, not how it works
- **Declarative approach:** TELL sentences to build agent
- **Model checking:** Enumerate all possible worlds
- **Theorem proving:** Syntactic manipulation with sound inference rules
- **Refutation/proof by contradiction:** Show ¬α leads to contradiction with KB
- **CNF conversion:** Systematic transformation to canonical form
- **Davis–Putnam (DPLL):** Backtracking + early termination + pure literal + unit propagation
- **Local search for SAT:** Flip variables to minimize unsatisfied clauses
- **Successor-state axioms:** Frame problem solution — focus on fluents, not actions
- **Conservative approximation:** Represent belief state approximately (1-CNF) for efficiency
- **Caching:** Save inference results for constant-time updates
- **SAT-based planning:** Reduce planning to SAT, exploit fast SAT solvers

## 15. Case Studies/Classic Examples

**Wumpus World exploration (Section 7.2):**
- Agent starts [1,1]: no percept → [1,2] and [2,1] safe
- Move to [2,1]: breeze → pit in [2,2] or [3,1]
- Return to [1,1], go to [1,2]: stench → wumpus in [1,3]; no breeze → no pit in [2,2] → pit must be in [3,1]
- Move [2,2] (safe), then [2,3]: glitter → grab gold → return home
- Performance: +1000 gold, −1 per action, −10 for arrow use

**Wumpus KB proof (Section 7.4.3–7.5):**
```
R₁: ¬P₁,₁
R₂: B₁,₁ ⇔ (P₁,₂ ∨ P₂,₁)
R₃: B₂,₁ ⇔ (P₁,₁ ∨ P₂,₂ ∨ P₃,₁)
R₄: ¬B₁,₁
R₅: B₂,₁
```
Proof of ¬P₁,₂:
1. R₂ → R₆: (B₁,₁⇒(P₁,₂∨P₂,₁)) ∧ ((P₁,₂∨P₂,₁)⇒B₁,₁) [biconditional elimination]
2. R₆ → R₇: (P₁,₂ ∨ P₂,₁) ⇒ B₁,₁ [and-elimination]
3. R₇ → R₈: ¬B₁,₁ ⇒ ¬(P₁,₂ ∨ P₂,₁) [contraposition]
4. R₈ + ¬B₁,₁ → R₉: ¬(P₁,₂ ∨ P₂,₁) [Modus Ponens]
5. R₉ → R₁₀: ¬P₁,₂ ∧ ¬P₂,₁ [De Morgan]

**SATP LAN example (Section 7.7.4):**
Goal: L¹_₂,₁ (be in [2,1] at time 1). SATPLAN finds [Forward₀] but also finds [Shoot₀] without additional axioms (since L⁰_₂,₁ can be assigned true). Fix: add "exactly one location" axioms.

**Hybrid agent priority hierarchy (Figure 7.20):**
1. If glitter → grab, plan route home, climb
2. If no plan → explore closest unvisited safe square (A*)
3. If blockade → shoot at possible wumpus locations
4. If no safe unexplored → try not-unsafe squares
5. If nothing → retreat to [1,1], climb out

## 16. Ethics

- **Qualification problem:** System designers must use judgment about which details to model — ethical responsibility for failures not anticipated
- **Autonomous agents:** Learning agents can be fully autonomous (p. 223) — ethical considerations of delegating decisions
- **Incomplete knowledge:** "If KB is true in the real world, then derived α is also true" — the "if" is a big assumption enforced by sensors and learning
- **Verification:** SAT solvers used for security protocol verification (SATMC found browser sign-on vulnerability)

## 17. End-of-Chapter Material

**Key Terms:** knowledge base, sentence, axiom, entailment, model, soundness, completeness, propositional logic, logical connectives, truth table, model checking, theorem proving, validity, satisfiability, inference rules, Modus Ponens, And-Elimination, resolution, CNF, Horn clause, definite clause, forward chaining, backward chaining, DPLL, WalkSAT, fluent, successor-state axiom, frame problem, qualification problem, SATPLAN, belief state

**Key Points Summary (p. 260-261):**
1. Agents need knowledge about the world for good decisions
2. Knowledge stored as sentences in knowledge base
3. KB-Agent: KB + inference mechanism; tell, ask, act
4. Representation language defined by syntax and semantics
5. Entailment: β true in all worlds where α true
6. Sound inference: only entailed sentences; Complete: all entailed sentences
7. Propositional logic: proposition symbols + connectives
8. Model checking: finite models → enumerate; O(2ⁿ)
9. Efficient inference: DPLL (backtracking), WalkSAT (local search)
10. Inference rules: resolution (complete for CNF); forward/backward chaining (Horn clauses)
11. WalkSAT: sound but not complete
12. State estimation: logical sentence describing belief state; transition model with successor-state axioms
13. SAT-based planning: find models specifying action sequences
14. Propositional logic doesn't scale to unbounded environments — need first-order logic (Chapter 8)
</task_result>
</task>

---

# COMPREHENSIVE EXAMINATION EXTRACTION

## CHAPTER 8: FIRST-ORDER LOGIC (lines 11196–12399)

---

### 1. NAMED ENTITIES & DEFINITIONS

- **First-order logic (FOL) / first-order predicate calculus (FOPC)**: A declarative language that can concisely represent much more than propositional logic; built around objects and relations.
- **Compositionality**: The meaning of a sentence is a function of the meaning of its parts.
- **Factored representation**: Propositional logic, which treats each atomic proposition as an indivisible fact.
- **Structured representation**: Languages like English and FOL that can describe objects and relations.
- **Sapir–Whorf hypothesis**: Claims our understanding of the world is strongly influenced by the language we speak.
- **Declarative language**: Semantics based on a truth relation between sentences and possible worlds.
- **Ontological commitment**: What a language assumes about the nature of reality. Propositional: facts; FOL: facts, objects, relations.
- **Epistemological commitment**: What an agent believes about facts; FOL allows true/false/unknown.
- **Fuzzy logic**: Propositions have a degree of truth between 0 and 1 (degree of truth).
- **Temporal logic**: Facts hold at particular times that are ordered.
- **Higher-order logic**: Views relations and functions referred to by first-order logic as objects in themselves.
- **Domain**: The set of objects or domain elements; must be nonempty.
- **Tuple**: A collection of objects arranged in a fixed order, enclosed in angle brackets.
- **Total functions**: Models in FOL require a value for every input tuple.
- **Constant symbol**: Stands for objects.
- **Predicate symbol**: Stands for relations.
- **Function symbol**: Stands for functions.
- **Arity**: The number of arguments a predicate or function symbol takes.
- **Interpretation**: Maps constant symbols to objects, function symbols to functions, predicate symbols to relations.
- **Intended interpretation**: The specific interpretation the knowledge engineer intends.
- **Term**: A logical expression that refers to an object.
- **Ground term**: A term with no variables.
- **Atomic sentence/atom**: Formed from a predicate symbol optionally followed by a parenthesized list of terms.
- **Quantifier**: ∀ (universal) and ∃ (existential).
- **Variable**: Lowercase letter; a term by itself.
- **Universal quantifier (∀)**: "For all"; a sentence ∀x P is true if P is true in all possible extended interpretations.
- **Existential quantifier (∃)**: "There exists"; ∃x P is true if P is true in at least one extended interpretation.
- **Extended interpretation**: Specifies a domain element to which a variable refers.
- **Equality symbol (=)**: Signifies that two terms refer to the same object.
- **Unique-names assumption**: Every constant symbol refers to a distinct object.
- **Closed-world assumption**: Atomic sentences not known to be true are false.
- **Domain closure**: Each model contains no more domain elements than those named by constant symbols.
- **Database semantics**: Standard semantics for databases; uses unique-names, closed-world, and domain closure assumptions.
- **Natural numbers**: Nonnegative integers defined via Peano axioms.
- **Peano axioms**: Define natural numbers and addition recursively.
- **Syntactic sugar**: An extension to or abbreviation of standard syntax that does not change semantics.
- **Infix notation**: m + 0 vs prefix +(m,0).
- **Set**: Mathematical domain; constant {}, unary predicate Set, binary predicates ∈ and ⊆, binary functions ∩, ∪, Add.
- **List**: Ordered collections; constants Nil, functions Cons, Append, First, Rest; predicate Find, List.
- **Knowledge engineering**: Process of knowledge-base construction.
- **Knowledge acquisition**: Extracting knowledge from experts.
- **Ontology**: A particular theory of the nature of being or existence; determines what kinds of things exist.
- **Circuit verification**: Using logical inference to check that a circuit performs correctly.

---

### 2. SEQUENTIAL PROCESSES

**Knowledge Engineering Process (7 steps)** (lines 12088–12154):
1. Identify the questions — delineate range of questions and available facts.
2. Assemble the relevant knowledge — work with experts; understand scope.
3. Decide on a vocabulary of predicates, functions, and constants — create ontology.
4. Encode general knowledge about the domain — write axioms for all vocabulary terms.
5. Encode a description of the problem instance — write simple atomic sentences.
6. Pose queries to the inference procedure and get answers.
7. Debug and evaluate the knowledge base — check for missing or incorrect axioms; run test suite.

---

### 3. HIERARCHIES/CLASSIFICATIONS

**Formal languages — ontological and epistemological commitments** (Figure 8.1):

| Language | Ontological Commitment | Epistemological Commitment |
|---|---|---|
| Propositional logic | facts | true/false/unknown |
| First-order logic | facts, objects, relations | true/false/unknown |
| Temporal logic | facts, objects, relations, times | true/false/unknown |
| Probability theory | facts | degree of belief ∈ [0,1] |
| Fuzzy logic | facts with degree of truth ∈ [0,1] | known interval value |

---

### 4. COMPARISONS/TRADE-OFFS

| **Aspect** | **Propositional Logic** | **First-Order Logic** |
|---|---|---|
| Ontological commitment | Facts only | Facts, objects, relations |
| Expressive power | Limited; requires separate rules per square | Concise general rules |
| Compositionality | Yes | Yes |
| Handling partial info | Yes (disjunction/negation) | Yes |
| Model size | Finite | Infinite (unbounded objects) |
| Decidability of entailment | Decidable | Semidecidable |

- **Data structures** vs **declarative logic**: Programs lack general mechanism for deriving facts; updates require domain-specific procedures. Logic: knowledge and inference are separate, domain independent.
- **Natural language** vs **FOL**: NL is ambiguous, context-dependent; FOL is unambiguous, context-independent, compositional.
- **Sapir-Whorf**: NL influences thought; fMRI evidence shows common representation across people.
- **Database semantics** vs **standard semantics**: DB semantics requires definite knowledge; far fewer models (16 vs infinite); makes expression concise but less flexible.

---

### 5. FORMULAS & EQUATIONS

**De Morgan's rules for quantifiers:**
```
¬∃x P ≡ ∀x ¬P        ¬(P ∨ Q) ≡ ¬P ∧ ¬Q
¬∀x P ≡ ∃x ¬P        ¬(P ∧ Q) ≡ ¬P ∨ ¬Q
∀x P ≡ ¬∃x ¬P         P ∧ Q ≡ ¬(¬P ∨ ¬Q)
∃x P ≡ ¬∀x ¬P         P ∨ Q ≡ ¬(¬P ∧ ¬Q)
```

**Peano Axioms for Natural Numbers:**
```
NatNum(0)
∀n NatNum(n) ⇒ NatNum(S(n))
∀n 0 ≠ S(n)
∀m,n m ≠ n ⇒ S(m) ≠ S(n)
∀m NatNum(m) ⇒ +(0,m) = m
∀m,n NatNum(m) ∧ NatNum(n) ⇒ +(S(m),n) = S(+(m,n))
```

**Set theory axioms:**
```
∀s Set(s) ⇔ (s={}) ∨ (∃x,s2 Set(s2) ∧ s=Add(x,s2))
¬∃x,s Add(x,s) = {}
∀x,s x ∈ s ⇔ s = Add(x,s)
∀x,s x ∈ s ⇔ ∃y,s2 (s=Add(y,s2) ∧ (x=y ∨ x∈s2))
∀s1,s2 s1 ⊆ s2 ⇔ (∀x x∈s1 ⇒ x∈s2)
∀s1,s2 (s1=s2) ⇔ (s1⊆s2 ∧ s2⊆s1)
∀x,s1,s2 x ∈ (s1∩s2) ⇔ (x∈s1 ∧ x∈s2)
∀x,s1,s2 x ∈ (s1∪s2) ⇔ (x∈s1 ∨ x∈s2)
```

---

### 6. RULES, LAWS & THEOREMS

**Truth condition for atomic sentence**: An atomic sentence is true in a given model if the relation referred to by the predicate symbol holds among the objects referred to by the arguments.

**Universal quantification truth**: ∀x P is true in a given model if P is true in all possible extended interpretations.

**Existential quantification truth**: ∃x P is true if P is true in at least one extended interpretation.

**Correct pattern for ∀**: Use ⇒ (implication): ∀x King(x) ⇒ Person(x). Common mistake: using ∧ instead — ∀x King(x) ∧ Person(x) means everything is a king and a person.

**Correct pattern for ∃**: Use ∧ (conjunction): ∃x Crown(x) ∧ OnHead(x,John). Common mistake: using ⇒ — ∃x Crown(x) ⇒ OnHead(x,John) is trivially true if anything is not a crown.

**Connections between quantifiers** via De Morgan's rules (see above).

---

### 7. DATA STRUCTURES & TYPES

**FOL Syntax Grammar** (Figure 8.3, Backus-Naur form):
```
Sentence → AtomicSentence | ComplexSentence
AtomicSentence → Predicate | Predicate(Term,...) | Term = Term
ComplexSentence → (Sentence) | ¬Sentence | Sentence∧Sentence | Sentence∨Sentence
                  | Sentence⇒Sentence | Sentence⇔Sentence | Quantifier Variable,... Sentence
Term → Function(Term,...) | Constant | Variable
Quantifier → ∀ | ∃
```
**Operator precedence** (highest to lowest): ¬, =, ∧, ∨, ⇒, ⇔

**Variables**: lowercase letters (x, y, z). **Constants**: uppercase starting (John, Richard).

---

### 8. VISUAL PATTERNS

- **Figure 8.1**: Table of formal languages and commitments.
- **Figure 8.2**: Model with 5 objects: Richard, John, Richard's left leg, John's left leg, crown; binary relations (brother, on-head); unary relations (person, king, crown); unary function (left-leg).
- **Figure 8.4**: Infinite set of models for language with two constant symbols R,J and one binary relation — models vary in object count and constant mapping.
- **Figure 8.5**: 16 possible models under database semantics with two constant symbols.
- **Figure 8.6**: Digital circuit C1 — one-bit full adder with 2 XOR gates (X1,X2), 2 AND gates (A1,A2), 1 OR gate (O1); 3 inputs, 2 outputs.

---

### 9. EDGE CASES/EXCEPTIONS/TRAPS

- **Empty worlds not allowed**: Domain must be nonempty (Exercise 8.EMPT).
- **Total functions problem**: Crown must have a left leg — solved with "invisible" object.
- **Multiple names for same object**: Existential instantiation can assign same object; need ¬(x=y) for distinctness.
- **Common mistake on ∀**: Using ∧ instead of ⇒ — ∀x King(x) ∧ Person(x) is wrong.
- **Common mistake on ∃**: Using ⇒ instead of ∧ — ∃x Crown(x) ⇒ OnHead(x,John) is too weak.
- **Nested quantifiers**: Variable belongs to innermost quantifier; different variable names recommended.
- **Standard semantics vs database semantics**: No one "correct" semantics; usefulness depends on conciseness and natural inference rules.
- **Missing axioms**: Without biconditional in Smelly rule, agent cannot prove absence of wumpus.
- **Debugging**: Example: forgetting 1 ≠ 0 means system can't prove most circuit outputs.

---

### 10. CROSS-CHAPTER DEPENDENCIES

- **Chapter 7**: Propositional logic as foundation; wumpus world axioms.
- **Chapter 9**: Inference in FOL (resolution, forward/backward chaining).
- **Chapter 10**: Knowledge representation (upper ontology, categories, event calculus).
- **Chapter 11**: Successor-state axioms for planning.
- **Chapter 19**: Learning — most succinct theory depends on representation language.
- **Chapter 24**: Assigning concepts to multidimensional spaces.
- **Chapter 25**: Perception reasoning.

---

### 11. DATES & PEOPLE

- **Whorf (1956)**: Sapir-Whorf hypothesis.
- **Pinker (1995)**: Language and thought.
- **Wanner (1974)**: Experiment on memory for exact wording vs content (50% vs 90%).
- **Loftus and Palmer (1974)**: "contacted" (32 mph) vs "smashed" (41 mph).
- **Boroditsky (2003)**: Gender of "bridge" → different adjectives.
- **Mitchell et al. (2008)**: fMRI (77% accuracy on word classification).
- **Sahin et al. (2009)**: Intracranial electrophysiology.
- **Frege (1879)**: Begriffschrift — introduced quantifiers.
- **Peirce (1870, 1883)**: Logic of relations, independent development of FOL.
- **Peano (1889)**: Present notation for FOL.
- **De Morgan (1864)**: Systematic treatment of relations.
- **Löwenheim (1915)**: Model theory for FOL.
- **Skolem (1920)**: Extended Löwenheim's results.
- **Tarski (1935, 1956)**: Model-theoretic satisfaction.
- **McCarthy (1958)**: Introduced FOL for AI.
- **Robinson (1965)**: Resolution.
- **Quine (1953)**: Challenged strict definitions.
- **Wittgenstein (1953)**: "Family resemblances" for categories.
- **Dedekind (1888)**: Peano axioms foundations.
- **Grassmann (1861)**: Earlier version of Peano axioms.

---

### 12. PROOF & ARGUMENT PATTERNS

**Why universal quantification needs ⇒**: The truth-table definition of ⇒ makes implication true when premise is false. ∀x King(x) ⇒ Person(x) asserts the conclusion only for objects where premise is true (kings), says nothing about non-kings. Using ∧ would wrongly assert that everything is both a king and a person.

**Why existential quantification needs ∧**: ∃x Crown(x) ∧ OnHead(x,John) requires at least one object to be both a crown and on John's head. Using ∃x Crown(x) ⇒ OnHead(x,John) is trivially true whenever any object fails to be a crown.

**Standard semantics vs database semantics argument**: Example: "Richard has two brothers, John and Geoffrey" — in standard FOL requires Brother(John,R) ∧ Brother(Geoffrey,R) ∧ John≠Geoffrey ∧ ∀x Brother(x,R) ⇒ (x=John ∨ x=Geoffrey). In database semantics, Equation (8.3) alone suffices.

---

### 13. CASE STUDIES/CLASSIC EXAMPLES

**Kinship domain axioms** (lines 11852–11874):
- Objects: people
- Predicates: Male, Female, Parent, Sibling, Brother, Sister, Child, Daughter, Son, Spouse, Wife, Husband, Grandparent, Grandchild, Cousin, Aunt, Uncle
- Functions: Mother, Father
- Axioms: Mother(c)=m ⇔ Female(m) ∧ Parent(m,c); Husband(h,w) ⇔ Male(h) ∧ Spouse(h,w); Parent(p,c) ⇔ Child(c,p); Grandparent(g,c) ⇔ ∃p Parent(g,p) ∧ Parent(p,c); Sibling(x,y) ⇔ x≠y ∧ ∃p Parent(p,x) ∧ Parent(p,y)

**Wumpus world FOL axioms** (lines 11997–12067):
- Percept([Stench,Breeze,Glitter,None,None],5)
- ∀t Percept([s,Breeze,g,w,c],t) ⇒ Breeze(t)
- ∀t Glitter(t) ⇒ BestAction(Grab,t)
- Adjacency: ∀x,y,a,b Adjacent([x,y],[a,b]) ⇔ (x=a ∧ (y=b-1 ∨ y=b+1)) ∨ (y=b ∧ (x=a-1 ∨ x=a+1))
- Breezy(s) ⇔ ∃r Adjacent(r,s) ∧ Pit(r)
- Successor-state: ∀t HaveArrow(t+1) ⇔ (HaveArrow(t) ∧ ¬Action(Shoot,t))

**Electronic circuits domain** (lines 12157–12308):
- Circuit C1: one-bit full adder
- Components: X1,X2 (XOR), A1,A2 (AND), O1 (OR)
- Key axioms: Connected terminals have same signal; AND output 0 iff any input 0; OR output 1 iff any input 1; XOR output 1 iff inputs differ; NOT output different from input

---

## CHAPTER 9: INFERENCE IN FIRST-ORDER LOGIC (lines 12400–13809)

---

### 1. NAMED ENTITIES & DEFINITIONS

- **Universal Instantiation (UI)**: Infer any sentence obtained by substituting a ground term for a universally quantified variable.
- **Existential Instantiation**: Replace an existentially quantified variable with a single new constant symbol (Skolem constant) that does not appear elsewhere.
- **Skolem constant**: A new constant symbol introduced by existential instantiation.
- **Propositionalization**: Converting a first-order KB to propositional logic by replacing all quantified sentences with instantiations.
- **Herbrand's theorem (1930)**: If a sentence is entailed by the original first-order KB, there is a proof involving just a finite subset of the propositionalized KB.
- **Semidecidability**: Algorithms exist that say "yes" to every entailed sentence, but no algorithm exists that says "no" to every nonentailed sentence.
- **Generalized Modus Ponens (GMP)**: Lifted version of Modus Ponens; for atomic sentences p_i, p_i', and q, where there is a substitution θ such that SUBST(θ,p_i')=SUBST(θ,p_i) for all i, then from p_1',...,p_n' and (p_1∧...∧p_n⇒q) infer SUBST(θ,q).
- **Lifting**: Raising inference from ground propositional logic to first-order logic.
- **Unification (UNIFY)**: Takes two sentences and returns a unifier (a substitution) if one exists: UNIFY(p,q) = θ where SUBST(θ,p) = SUBST(θ,q).
- **Most General Unifier (MGU)**: Every unifiable pair has a single MGU, unique up to renaming.
- **Standardizing apart**: Renaming variables to avoid name clashes.
- **Occur check**: Checks whether a variable itself occurs inside the term being unified with it; makes complexity quadratic.
- **Subsumption lattice**: Lattice of queries ordered by specificity for a given predicate.
- **Predicate indexing**: Putting all facts with same predicate in one bucket.
- **Indexing**: Organizing knowledge base facts by keys for efficient retrieval.
- **Datalog**: First-order definite clauses with no function symbols.
- **Definite clause**: Disjunction of literals with exactly one positive literal; either atomic or implication with conjunction of positive literals in antecedent and single positive literal as consequent.
- **Renaming**: Sentences identical except for variable names.
- **Fixed point**: State where no new inferences are possible.
- **Conjunct ordering problem**: Finding optimal order to solve conjuncts of rule premise to minimize total cost.
- **Data complexity**: Complexity of inference as a function of number of ground facts (assuming rule size and arity bounded).
- **Rete algorithm**: Preprocesses rules into a dataflow network; each node is a literal from a rule premise; variable bindings flow through and are filtered.
- **Production system**: Forward-chaining system with condition-action rules.
- **Cognitive architectures**: Models of human reasoning (ACT, SOAR).
- **Deductive databases**: Large-scale databases using forward chaining as standard inference tool.
- **Magic set**: Technique to rewrite rule set so only relevant variable bindings considered during forward inference.
- **Logic programming**: Technology embodying declarative ideal; Algorithm = Logic + Control (Kowalski).
- **Prolog**: Most widely used logic programming language; uppercase variables, lowercase constants; clauses written backwards (C :- A, B).
- **Tabled logic programming**: Stores intermediate results to avoid recomputation; combines goal-directedness of backward chaining with dynamic-programming efficiency of forward chaining.
- **Completion**: Expressing in FOL the database semantics idea that there are at most some number of objects and they are distinct.
- **Constraint logic programming (CLP)**: Allows variables to be constrained rather than bound; solution is most specific set of constraints.
- **Metarule**: Rules to determine which conjuncts to try first in inference.
- **Resolution**: Complete inference procedure for any knowledge base (not just definite clauses).
- **CNF (Conjunctive Normal Form)**: Conjunction of clauses, each clause a disjunction of literals; every FOL sentence can be converted to inferentially equivalent CNF.
- **Skolemization**: Removing existential quantifiers by introducing Skolem functions.
- **Skolem function**: Function whose arguments are all universally quantified variables in whose scope the existential quantifier appears.
- **Binary resolution rule**: Resolves exactly two complementary literals.
- **Factoring**: Removal of redundant literals; first-order factoring reduces two literals to one if they are unifiable.
- **Refutation completeness**: If a set of sentences is unsatisfiable, resolution will always derive a contradiction.
- **Herbrand universe (H_S)**: Set of all ground terms constructible from function symbols and constant symbols in S (with default constant if none).
- **Saturation (P(S))**: Set of all ground clauses from applying all consistent substitutions of ground terms in P for variables in S.
- **Herbrand base (H_S(S))**: Saturation of S with respect to its Herbrand universe.
- **Lifting lemma**: If C' is a ground resolvent of ground instances C'_1, C'_2, then there exists a clause C such that C is a resolvent of C_1, C_2 and C' is a ground instance of C.
- **Demodulation**: Rule for equality: from x=y and clause α containing term x, substitute y for x within α.
- **Paramodulation**: Generalized demodulation for non-unit clauses with equality.
- **Equational unification**: Unification algorithm that incorporates equality reasoning.
- **Unit preference**: Strategy preferring resolutions with unit clauses.
- **Set of support**: Strategy requiring every resolution to involve at least one element of a special set.
- **Input resolution**: Every resolution combines one input sentence with another.
- **Linear resolution**: Generalization allowing P and Q to resolve if P is in original KB or is ancestor of Q.
- **Subsumption**: Eliminating sentences more specific than existing sentences in KB.
- **Nonconstructive proof**: Resolution may prove existential query without unique variable binding.

---

### 2. SEQUENTIAL PROCESSES

**Conversion to CNF procedure** (lines 13208–13256, using example "Everyone who loves all animals is loved by someone"):
1. **Eliminate implications**: Replace P⇒Q with ¬P∨Q.
2. **Move ¬ inwards**: ¬∀x p → ∃x ¬p; ¬∃x p → ∀x ¬p; plus De Morgan for ∧/∨.
3. **Standardize variables**: Rename variables so each quantifier has unique variable.
4. **Skolemize**: Remove existential quantifiers; replace ∃x P(x) with P(A) if no universal variables in scope, or with P(F(x1,...,xn)) where F is new Skolem function of all enclosing universal variables.
5. **Drop universal quantifiers**: All remaining variables are universally quantified.
6. **Distribute ∨ over ∧**: Convert to conjunct of disjuncts.

**UNIFY algorithm** (Figure 9.1, lines 12614–12628):
- If θ = failure, return failure.
- If x = y, return θ.
- If VARIABLE?(x), call UNIFY-VAR(x,y,θ).
- If VARIABLE?(y), call UNIFY-VAR(y,x,θ).
- If COMPOUND?(x) and COMPOUND?(y), recurse on OP(x),OP(y), then ARGS(x),ARGS(y).
- If LIST?(x) and LIST?(y), recurse on FIRST then REST.
- Else return failure.
- UNIFY-VAR: if {var/val}∈θ, recurse with val,x; if {x/val}∈θ, recurse with var,val; if OCCUR-CHECK?(var,x), failure; else add {var/x} to θ.

**FOL-FC-ASK algorithm** (Figure 9.3, lines 12737–12756):
```
while true do
  new ← {}
  for each rule in KB do
    standardize variables
    for each θ such that SUBST(θ, premise) = SUBST(θ, KB_facts) do
      q' ← SUBST(θ, q)
      if q' doesn't unify with KB or new then add q' to new
      φ ← UNIFY(q', α)
      if φ not failure then return φ
  if new = {} then return false
  add new to KB
```

**FOL-BC-ASK algorithm** (Figure 9.6, lines 12980–12994):
- FOL-BC-ASK(KB, query) returns a generator of substitutions.
- FOL-BC-OR: for each rule that unifies with goal, standardize variables, then for each θ' from FOL-BC-AND on lhs, yield θ'.
- FOL-BC-AND: if θ = failure return; if goals empty yield θ; else for each θ' from FOL-BC-OR on first goal, for each θ'' from FOL-BC-AND on rest, yield θ''.

**SATPlan translation steps** (lines 15385–15406):
1. Propositionalize actions — ground all action schemas.
2. Add action exclusion axioms — no two actions at same time.
3. Add precondition axioms — A_t ⇒ PRE(A)_t.
4. Define initial state — F_0 for fluents in initial, ¬F_0 for others.
5. Propositionalize goal — disjunction over ground instances.
6. Add successor-state axioms — F_{t+1} ⇔ ActionCausesF_t ∨ (F_t ∧ ¬ActionCausesNotF_t).

**Completeness proof for resolution** (Figure 9.12, lines 13372–13487):
1. If S is unsatisfiable, there exists finite subset of ground instances (Herbrand base) that is also unsatisfiable (Herbrand's theorem).
2. Propositional resolution is complete for ground sentences.
3. Lifting lemma: for any propositional resolution proof with ground instances, there is a corresponding first-order resolution proof.

---

### 3. HIERARCHIES/CLASSIFICATIONS

**Resolution strategies** (lines 13553–13594):
- **Unit preference**: Prefer resolutions with unit clauses; incomplete in general, complete for Horn.
- **Set of support**: Every resolution involves at least one element of a special set (e.g., negated query); goal-directed, complete if remainder is consistent.
- **Input resolution**: One sentence must be from original KB or query; complete for Horn; incomplete in general.
- **Linear resolution**: P and Q can resolve if P is in original KB or ancestor of Q; complete.
- **Subsumption**: Remove sentences subsumed by existing ones.
- **Learning (DEEPHOL)**: Uses deep neural networks to select promising proof steps.

**Equality reasoning approaches** (lines 13494–13549):
1. **Axiomatization**: Write reflexivity, symmetry, transitivity + substitution axioms for each predicate/function.
2. **Demodulation/Paramodulation**: Add inference rules rather than axioms.
3. **Equational unification**: Incorporate equality reasoning into unification algorithm.

---

### 4. COMPARISONS/TRADE-OFFS

| **Approach** | **Strengths** | **Weaknesses** |
|---|---|---|
| **Forward chaining** | Sound; complete for definite clauses; polynomial data complexity; dynamic programming for path problems | Generates irrelevant facts; may not terminate with function symbols; semidecidable |
| **Backward chaining** | Goal-directed; linear space; logic programming | Repeated states; infinite loops; incomplete for some KBs |
| **Resolution** | Complete for any FOL KB | Larger search space; strategies needed |

| **Prolog** vs **FOL** | |
|---|---|
| Database semantics (CWA, UNA) vs standard semantics |
| No occur check (unsound but practical) |
| Depth-first search (can loop) |
| Built-in arithmetic (not logical inference) |
| Side-effect predicates (assert/retract) |

---

### 5. FORMULAS & EQUATIONS

**Universal Instantiation**: ∀v α / SUBST({v/g}, α)

**Existential Instantiation**: ∃v α / SUBST({v/k}, α) where k is new constant

**Generalized Modus Ponens**:
```
p'_1, p'_2, ..., p'_n,  (p_1 ∧ p_2 ∧ ... ∧ p_n ⇒ q)
------------------------------------------------------
                  SUBST(θ, q)
```
where SUBST(θ, p'_i) = SUBST(θ, p_i) for all i.

**UNIFY definition**: UNIFY(p,q) = θ where SUBST(θ,p) = SUBST(θ,q)

**Binary Resolution rule**:
```
ℓ_1 ∨ ... ∨ ℓ_k,    m_1 ∨ ... ∨ m_n
-----------------------------------------------
SUBST(θ, ℓ_1∨...∨ℓ_{i-1}∨ℓ_{i+1}∨...∨ℓ_k∨m_1∨...∨m_{j-1}∨m_{j+1}∨...∨m_n)
```
where UNIFY(ℓ_i, ¬m_j) = θ.

**Demodulation**:
```
x = y,  m_1 ∨ ... ∨ m_n
------------------------
SUB(SUBST(θ,x), SUBST(θ,y), m_1 ∨ ... ∨ m_n)
```
where UNIFY(x,z) = θ and z appears in some m_i.

**Paramodulation**:
```
ℓ_1 ∨ ... ∨ ℓ_k ∨ x = y,   m_1 ∨ ... ∨ m_n
------------------------------------------------
SUB(SUBST(θ,x), SUBST(θ,y), SUBST(θ, ℓ_1∨...∨ℓ_k∨m_1∨...∨m_n))
```
where UNIFY(x,z) = θ and z appears in some m_i.

---

### 6. RULES, LAWS & THEOREMS

**Herbrand's theorem**: If a set S of clauses is unsatisfiable, there exists a finite subset of H_S(S) that is also unsatisfiable.

**Refutation completeness of resolution**: If S is an unsatisfiable set of clauses, the application of a finite number of resolution steps to S will yield a contradiction.

**Gödel's Incompleteness Theorem**: There are true arithmetic sentences that cannot be proved from any given set of true axioms for number theory. (Detailed proof sketch: lines 13422–13460, involving Gödel numbering, self-referential sentence σ stating its own unprovability.)

**Completeness of GMP for definite clauses**: FOL-FC-ASK answers every query whose answers are entailed by any KB of definite clauses. For Datalog (no function symbols), fixed point reached in at most p·n^k iterations.

---

### 7. DATA STRUCTURES & TYPES

**Subsumption Lattice** (Figure 9.2):
- Root: most general query (e.g., Employs(x,y))
- Children obtained by single substitution
- "Highest" common descendant = result of applying MGU
- Size: O(2^n) for n-argument predicate without functions; exponential with functions

**Storage and Retrieval**:
- STORE(s): stores sentence s
- FETCH(q): returns all unifiers such that q unifies with some sentence in KB
- Predicate indexing: one bucket per predicate
- Combined indexing: hash on predicate + argument positions

---

### 8. EDGE CASES/EXCEPTIONS/TRAPS

- **Infinite nested terms**: With function symbols, infinite ground-term substitutions possible → propositionalization may never terminate.
- **Non-entailed sentences**: For FOL, entailment is semidecidable — cannot know if stuck in hopeless loop.
- **UNIFY failure with same variable**: Knows(John,x) and Knows(x,Elizabeth) fail because x cannot be both John and Elizabeth. Solution: standardize apart.
- **Occur check**: S(x) cannot unify with S(S(x)) — variable occurs inside term.
- **Prolog infinite loops**: path(X,Z) :- path(X,Y), link(Y,Z) before base case causes infinite recursion.
- **Prolog omission of occur check**: Can make unsound inferences; rarely a problem in practice.
- **Prolog negated goal**: For ¬Criminal(West) in resolution, the algorithm uses refutation.
- **Nonconstructive proofs**: Resolution may prove ∃x P(x) without unique binding.

---

### 9. EMPIRICAL EVIDENCE/KEY RESULTS

- Datalog bounded inference: max p·n^k possible facts.
- Prolog path-finding example: 877 inferences (backward) vs 62 (forward) for graph with 4×4 grid (Figure 9.8(b)).
- Unit preference (1964): dramatic speedup for propositional inference.
- **Robbins algebra**: Open for decades; proved by EQP (McCune, 1997).
- **Kepler sphere-packing**: Proved by Hales (2005); formalized in HOL Light and Isabelle (2017).
- **DEEPHOL**: Training on 10,000 proofs using deep neural networks to select premises.

---

### 10. DATES & PEOPLE

- **Herbrand (1930)**: Herbrand's theorem, unification.
- **Gödel (1930)**: Complete proof procedure for FOL.
- **Turing (1936), Church (1936)**: Undecidability of FOL validity.
- **Gilmore (1960)**: First automated reasoning program.
- **Davis and Putnam (1960)**: Propositionalization method.
- **Prawitz (1960)**: Letting propositional inconsistency drive search.
- **Robinson (1965)**: Resolution.
- **Green (1969a)**: First-order question-answering, deductive synthesis.
- **Colmerauer (1972)**: Prolog for natural language parsing.
- **Kowalski (1974)**: Algorithm = Logic + Control.
- **Warren (1983)**: Warren Abstract Machine (WAM).
- **McDermott (1982)**: R1/XCON expert system.
- **Forgy (1982)**: Rete algorithm.
- **Wos et al. (1964, 1965)**: Unit preference, set of support.
- **Boyer-Moore (1979)**: NQTHM theorem prover.
- **McCune (1990)**: OTTER theorem prover.
- **McCune (1997)**: EQP proved Robbins algebra.
- **Benzmüller and Paleo (2013)**: Verified Gödel's proof of God's existence.
- **Shankar (1986)**: Formal proof of Gödel's Incompleteness Theorem using Boyer-Moore.

---

### 11. CASE STUDIES/CLASSIC EXAMPLES

**Crime example** (lines 12701–12767):
- Facts: American(West), Enemy(Nono,America), Owns(Nono,M1), Missile(M1)
- Rules: American(x) ∧ Weapon(y) ∧ Sells(x,y,z) ∧ Hostile(z) ⇒ Criminal(x); Missile(x) ⇒ Weapon(x); Enemy(x,America) ⇒ Hostile(x); Missile(x) ∧ Owns(Nono,x) ⇒ Sells(West,x,Nono)
- Forward chaining requires 2 iterations; proof tree in Figure 9.4.

**Curiosity killed the cat** (lines 13311–13356):
- Premises: Everyone who loves all animals is loved by someone; Anyone who kills an animal is loved by no one; Jack loves all animals; Either Jack or Curiosity killed Tuna (a cat); cats are animals.
- Resolution proof (Figure 9.11) uses Skolemization, factoring.
- Answer: Curiosity killed the cat.

---

## CHAPTER 10: KNOWLEDGE REPRESENTATION (lines 13810–15084)

---

### 1. NAMED ENTITIES & DEFINITIONS

- **Ontological engineering**: Creating representations of general concepts (Events, Time, Physical Objects, Beliefs) that occur in many domains.
- **Upper ontology**: General framework of concepts at the top of a hierarchy, with more specific concepts below.
- **Category**: Organization of objects into groups; vital for knowledge representation.
- **Reification**: Turning a proposition into an object (from Latin *res*, thing).
- **Subcategory/Subclass/Subset**: Hierarchical organization of categories.
- **Inheritance**: Instances of a category inherit properties from supercategories.
- **Taxonomic hierarchy/Taxonomy**: Subclass relations organizing categories.
- **Disjoint**: Categories with no members in common.
- **Exhaustive decomposition**: Categories whose union covers all members of a supercategory.
- **Partition**: Disjoint + Exhaustive decomposition.
- **PartOf**: Relation saying one thing is part of another (transitive and reflexive).
- **Composite object**: Object characterized by structural relations among parts.
- **Bunch**: Composite object with definite parts but no particular structure (has weight, unlike sets).
- **Logical minimization**: Defining an object as the smallest one satisfying certain conditions.
- **Measure**: Values assigned for properties like height, mass, cost.
- **Units function**: Takes a number as argument to represent a measure (e.g., Inches(1.5)).
- **Individuation**: Division into distinct objects.
- **Stuff**: Reality that defies obvious individuation (mass nouns: butter, water).
- **Count noun**: Things that can be counted (aardvarks, holes).
- **Mass noun**: Substances (butter, water, energy).
- **Intrinsic properties**: Belong to substance of object; retained under subdivision (density, boiling point, flavor, color, ownership).
- **Extrinsic properties**: Not retained under subdivision (weight, length, shape).
- **Event calculus**: Approach for representing events, fluents, and time points; handles continuous, simultaneous, and overlapping events.
- **Event**: Something that can happen (same as action).
- **Fluents**: Aspects of the world that change over time.
- **Time points** and **Time intervals**: Moments (zero duration) and extended intervals.
- **Propositional attitudes**: Believes, Knows, Wants, Informs.
- **Referential transparency**: Terms don't matter, only the object named.
- **Referential opacity**: Terms matter because agents may not know co-reference.
- **Modal logic**: Includes modal operators (K for knowledge) that take sentences as arguments.
- **Modal operators**: K_A P (agent A knows P).
- **Possible world**: Models in modal logic consist of a collection of possible worlds.
- **Accessibility relation**: Connects worlds; w_1 accessible from w_0 if everything in w_1 is consistent with what A knows in w_0.
- **Logical omniscience**: If agent knows axioms, it knows all consequences — problematic for belief.
- **Linear temporal logic**: Modal operators for time: X (next), F (eventually), G (always), U (until).
- **Semantic networks**: Graphical notation of nodes (objects/categories) and edges (relations).
- **Existential graphs**: Peirce's graphical notation of nodes and edges.
- **Description logics**: Formal language for constructing and combining category definitions; tasks: subsumption, classification, consistency.
- **Procedural attachment**: Technique where query about a relation calls a special procedure.
- **Default value**: Assumed property unless contradicted by more specific information.
- **Overriding**: More specific value supersedes default.
- **Multiple inheritance**: Object belongs to >1 category or category is subset of >1 other; can cause conflicts.
- **CLASSIC language**: Typical description logic.
- **Monotonicity**: If KB |= α then KB ∧ β |= α for any β.
- **Nonmonotonicity**: Set of beliefs does not grow monotonically as new evidence arrives.
- **Nonmonotonic logic**: Logics with modified notions of truth and entailment.
- **Circumscription**: Specify predicates assumed "as false as possible" (after McCarthy, 1980).
- **Model preference logic**: Sentence entailed (with default status) if true in all preferred models.
- **Prioritized circumscription**: Some abnormalities minimized before others.
- **Default logic**: Default rules generate contingent, nonmonotonic conclusions (after Reiter, 1980).
- **Default rule**: P : J_1, ..., J_n / C (if P true and J_i consistent, conclude C).
- **Extension**: Maximal set of consequences of a default theory.
- **Belief revision**: Retracting inferred facts when new information contradicts them.
- **Truth maintenance system (TMS)**: Handles retraction of inferences when premises are retracted.
- **JTMS (Justification-based TMS)**: Each sentence annotated with justifications (set of sentences from which inferred).
- **ATMS (Assumption-based TMS)**: Represents all considered states simultaneously; each sentence has label of assumption sets.
- **Explanation**: Set of sentences E such that E entails P.
- **Assumption**: Sentence not known to be true but would suffice to prove P if true.
- **Qualitative physics**: Subfield of KR constructing logical, nonnumeric theory of physical objects.
- **Spatial reasoning**: Reasoning about spatial structure.
- **Psychological reasoning**: Developing working psychology for agents to reason about themselves/others.

---

### 2. SEQUENTIAL PROCESSES

**Inheritance algorithm in semantic networks**: Follow MemberOf link from object to category → follow SubsetOf links up hierarchy → stop when find boxed property link.

**Truth maintenance via JTMS**:
- Each sentence annotated with justification set.
- RETRACT(P): delete sentences for which P is in every justification.
- Sentences without justification marked "out" (not deleted).
- Sentences re-marked "in" when justification restored.

---

### 3. HIERARCHIES/CLASSIFICATIONS

**Upper Ontology** (Figure 10.1):
```
Anything
├── AbstractObjects
│   ├── Sets
│   ├── Numbers
│   ├── RepresentationalObjects
│   ├── Intervals
│   ├── Places
│   ├── Processes
│   └── PhysicalObjects
│       ├── Humans
│       ├── Categories
│       ├── Sentences
│       ├── Measurements
│       ├── Moments
│       ├── Things
│       ├── Stuff
│       ├── Times
│       ├── Weights
│       ├── Animals
│       ├── Agents
│       ├── Solid
│       ├── Liquid
│       ├── Gas
│       └── GeneralizedEvents
```

**Interval relations** (Allen, 1983; Figure 10.2):
- Meet(i,j): End(i) = Begin(j)
- Before(i,j): End(i) < Begin(j)
- After(j,i): Before(i,j)
- During(i,j): Begin(j) < Begin(i) < End(i) < End(j)
- Overlap(i,j): Begin(i) < Begin(j) < End(i) < End(j)
- Starts(i,j): Begin(i) = Begin(j)
- Finishes(i,j): End(i) = End(j)
- Equals(i,j): Begin(i)=Begin(j) ∧ End(i)=End(j)

**Three approaches to mental objects**:
1. **Modal logic/possible worlds** (Hintikka, Kripke): classical approach.
2. **First-order theory with mental objects as fluents** (Davis, Moore).
3. **Syntactic theory**: mental objects as character strings (can lead to paradoxes).

---

### 4. COMPARISONS/TRADE-OFFS

| **Representation** | **Strengths** | **Weaknesses** |
|---|---|---|
| **Predicates** (Basketball(b)) | Simple FOL | Can't quantify over categories |
| **Reified objects** (Basketballs) | Can state category-level facts | Need MemberOf, SubsetOf predicates |

| **Standard FOL** vs **Description Logics** |
|---|
| Full expressive power | Tractable subsumption/classification |
| Unknown inference time | Polynomial-time (usually) |
| Hard problems expressible simply | Hard problems excluded or require exponential descriptions |
| Negation and disjunction allowed | Typically lack negation/disjunction |

| **Circumscription** vs **Default Logic** |
|---|
| Model preference approach | Rule-based approach |
| Predicates minimized | Default rules with justifications |
| Preferred models with fewer abnormal objects | Extensions = maximal consequence sets |

---

### 5. FORMULAS & EQUATIONS

**Disjoint, ExhaustiveDecomposition, Partition**:
- Disjoint(s) ⇔ (∀c1,c2 c1∈s ∧ c2∈s ∧ c1≠c2 ⇒ Intersection(c1,c2) = {})
- ExhaustiveDecomposition(s,c) ⇔ (∀i i∈c ⇔ ∃c2 c2∈s ∧ i∈c2)
- Partition(s,c) ⇔ Disjoint(s) ∧ ExhaustiveDecomposition(s,c)

**BunchOf axioms**:
- ∀x x∈s ⇒ PartOf(x, BunchOf(s))
- ∀y [∀x x∈s ⇒ PartOf(x,y)] ⇒ PartOf(BunchOf(s), y)

**Unit conversion**: Centimeters(2.54 × d) = Inches(d)

**Event calculus predicates**:
- T(f, t1, t2): Fluent f is true for all times between t1 and t2
- Happens(e, t1, t2): Event e starts at t1 and ends at t2
- Initiates(e, f, t): Event e causes fluent f to become true at time t
- Terminates(e, f, t): Event e causes fluent f to cease to be true at time t
- Initiated(f, t1, t2): Fluent f becomes true at some point between t1 and t2
- Terminated(f, t1, t2): Fluent f ceases to be true at some point between t1 and t2

**Event calculus axioms**:
```
Happens(e,t1,t3) ∧ Initiates(e,f,t2) ∧ ¬Terminated(f,t2,t4) ∧ t1≤t2≤t3≤t4 ⇒ T(f,t2,t4)
Happens(e,t1,t3) ∧ Terminates(e,f,t2) ∧ ¬Initiated(f,t2,t4) ∧ t1≤t2≤t3≤t4 ⇒ ¬T(f,t2,t4)

Terminated(f,t1,t5) ⇔ ∃e,t2,t3,t4 Happens(e,t2,t4) ∧ Terminates(e,f,t3) ∧ t1≤t2≤t3≤t4≤t5
Initiated(f,t1,t5) ⇔ ∃e,t2,t3,t4 Happens(e,t2,t4) ∧ Initiates(e,f,t3) ∧ t1≤t2≤t3≤t4≤t5
```

**Duration**: Duration(i) = Time(End(i)) − Time(Begin(i))

**Modal knowledge axioms**:
- (K_a P ∧ K_a(P⇒Q)) ⇒ K_a Q (logical omniscience)
- K_a P ⇒ P (knowledge implies truth)
- K_a P ⇒ K_a(K_a P) (positive introspection)

---

### 6. RULES, LAWS & THEOREMS

**PartOf transitivity and reflexivity**: PartOf(x,y) ∧ PartOf(y,z) ⇒ PartOf(x,z); PartOf(x,x)

**Biped definition**: Biped(a) ⇒ ∃l1,l2,b Leg(l1) ∧ Leg(l2) ∧ Body(b) ∧ PartOf(l1,a) ∧ PartOf(l2,a) ∧ PartOf(b,a) ∧ Attached(l1,b) ∧ Attached(l2,b) ∧ l1≠l2 ∧ [∀l3 Leg(l3) ∧ PartOf(l3,a) ⇒ (l3=l1 ∨ l3=l2)]

**Basic equality axioms**:
```
∀x x = x
∀x,y x = y ⇒ y = x
∀x,y,z x = y ∧ y = z ⇒ x = z
∀x,y x = y ⇒ (P_1(x) ⇔ P_1(y))
...
∀w,x,y,z w = y ∧ x = z ⇒ (F_1(w,x) = F_1(y,z))
```

**CWA as nonmonotonic**: If α not mentioned in KB, KB |= ¬α, but KB ∧ α |= α (nonmonotonicity).

**Default rule form**: P : J_1, ..., J_n / C (prerequisite, justifications, conclusion).

---

### 7. DATA STRUCTURES & TYPES

**CLASSIC description syntax** (Figure 10.6):
```
Concept → Thing | ConceptName
         | And(Concept,...)
         | All(RoleName, Concept)
         | AtLeast(Integer, RoleName)
         | AtMost(Integer, RoleName)
         | Fills(RoleName, IndividualName, ...)
         | SameAs(Path, Path)
         | OneOf(IndividualName, ...)
Path → [RoleName, ...]
```

---

### 8. EDGE CASES/EXCEPTIONS/TRAPS

- **Natural kinds cannot be strictly defined**: tomatoes, games (Wittgenstein's "family resemblances").
- **"Bachelor" problematic**: "The Pope is a bachelor" — logically true but infelicitous (Quine).
- **Referential opacity**: Superman = Clark but Lois may not know this; equality substitution fails for knowledge operators.
- **Logical omniscience problem**: Modal logic assumes agents know all consequences of axioms.
- **Default rules decisions**: If "Cars have four wheels" is false, what does it mean to have it in KB? Nonmodularity problem.
- **Default vs probability**: "Brakes always OK" really means "probability high enough for optimal decision" — changes with context (mountain driving).

---

### 9. CROSS-CHAPTER DEPENDENCIES

- **Chapter 7**: Successor-state axioms for wumpus world.
- **Chapter 8**: FOL syntax and semantics.
- **Chapter 11**: HTN planning using event representations.
- **Chapter 12**: Reasoning with uncertainty (deferred).
- **Chapter 13**: Bayesian networks.
- **Chapter 17**: Markov models over time.
- **Chapter 21**: Deep neural networks.
- **Chapter 24**: Word embeddings and neural representations.

---

### 10. DATES & PEOPLE

- **Aristotle (384-322 BCE)**: Categories, genus/species, Organon.
- **Porphyry (c. 234-305 CE)**: First semantic network (commenting on Categories).
- **Linnaeus (1707-1778)**: Binomial nomenclature.
- **Peirce (1909)**: Existential graphs.
- **Quillian (1961)**: Semantic networks in AI.
- **Minsky (1975)**: Frames.
- **Woods (1975)**: "What's In a Link?" — need for precise semantics.
- **Brachman (1979)**: Semantics for semantic networks.
- **Hayes (1979)**: "The Logic of Frames."
- **McCarthy (1980)**: Circumscription.
- **Reiter (1980)**: Default logic.
- **McDermott and Doyle (1980)**: Modal nonmonotonic logic.
- **Allen (1983, 1984)**: Time intervals.
- **Kowalski and Sergot (1986)**: Event calculus.
- **Lenat and Guha (1990)**: CYC.
- **Gruber (2004)**: "Every ontology is a treaty."
- **Bizer et al. (2007)**: DBPedia.
- **Dong et al. (2014)**: Google Knowledge Graph (70 billion facts).
- **Meehl (1955)**: Statistical algorithms beat expert predictions.

---

### 11. CASE STUDIES/CLASSIC EXAMPLES

**Nixon diamond** (lines 14663–14701):
- Nixon is both Quaker (default pacifist) and Republican (default not pacifist).
- Circumscription yields two preferred models (one pacifist, one not).
- Default logic yields two extensions.
- Prioritized circumscription can give Quaker beliefs precedence.

**President(USA) as generalized event** (Figure 10.3):
- President(USA) is George Washington 1789-1797, John Adams 1797-1801, etc.
- T(Equals(President(USA), GeorgeWashington), Begin(AD1790), End(AD1790)).

---

## CHAPTER 11: AUTOMATED PLANNING (lines 15085–16855)

---

### 1. NAMED ENTITIES & DEFINITIONS

- **Classical planning**: Finding sequence of actions to accomplish a goal in discrete, deterministic, static, fully observable environment.
- **PDDL (Planning Domain Definition Language)**: Factored representation for planning problems; allows expressing many actions with single action schema.
- **State**: Represented as conjunction of ground atomic fluents.
- **Action schema**: Represents a family of ground actions; has action name, variables, precondition, effect.
- **Precondition**: Conjunction of literals that must hold for action to be applicable.
- **Effect**: Conjunction of literals (positive/negative) that result from action.
- **Applicable action**: Ground action a is applicable in state s if s entails the precondition of a.
- **Delete list (DEL(a))**: Fluents removed by action.
- **Add list (ADD(a))**: Fluents added by action.
- **RESULT(s,a)** = (s − DEL(a)) ∪ ADD(a).
- **Planning domain**: Set of action schemas.
- **Initial state**: Conjunction of ground fluents (closed-world assumption).
- **Goal**: Conjunction of literals (may contain variables).
- **Blocks world**: Classic planning domain with cube-shaped blocks on a table; robot arm can move one block at a time.
- **Clear(x)**: Predicate meaning nothing is on x.
- **Forward (progression) search**: Search from initial state forward through state space.
- **Backward (regression) search**: Search from goal backward to initial state.
- **Regression search**: Start at goal, apply actions backward; uses relevant actions.
- **Relevant action**: Action with effect unifying with goal literal, no effect negating any part of goal.
- **Regression equations**:
  - POS(g') = (POS(g) − ADD(a)) ∪ POS(Precond(a))
  - NEG(g') = (NEG(g) − DEL(a)) ∪ NEG(Precond(a))
- **SATPlan**: Translates PDDL to propositional SAT problem.
- **Planning graph (Graphplan)**: Data structure encoding constraints on action-precondition relationships and mutual exclusions.
- **Situation calculus**: Describing planning problems in FOL using successor-state axioms.
- **Partial-order planning**: Plan as graph (not linear sequence); edges show ordering constraints.
- **Ignore-preconditions heuristic**: Drop all preconditions from actions.
- **Ignore-delete-lists heuristic**: Remove all negative literals from effects.
- **Set-cover problem**: Relaxed heuristic counts minimum actions to satisfy goals (NP-hard).
- **Symmetry reduction**: Prune all but one symmetric branch of search tree.
- **Preferred action**: Step of relaxed plan, or achieves precondition of relaxed plan.
- **Serializable subgoals**: Subgoals that can be achieved in some order without undoing previous ones.
- **State abstraction**: Many-to-one mapping from ground states to abstract representation.
- **Decomposition**: Dividing problem into parts, solving independently, combining.
- **Subgoal independence assumption**: Cost of conjunction ≈ sum of costs of independent subgoals.
- **FF (FastForward) planner**: Forward state-space search using ignore-delete-lists heuristic, hill climbing, then greedy best-first.
- **Hierarchical decomposition**: Managing complexity by reducing tasks to fewer activities at next lower level.
- **HTN (Hierarchical Task Network) planning**: Formalism for hierarchical decomposition.
- **Primitive action**: Standard precondition-effect action at lowest level.
- **HLA (High-Level Action)**: Abstract action with one or more possible refinements.
- **Refinement**: Sequence of actions (HLAs or primitives) implementing an HLA.
- **Implementation**: An HLA refinement containing only primitive actions.
- **Downward refinement property**: Property that every high-level plan achieving goal (by descriptions) has at least one implementation achieving it.
- **Demonic nondeterminism**: Adversary makes choices among implementations.
- **Angelic nondeterminism**: Agent itself makes choices among implementations.
- **Angelic semantics**: Semantics for HLAs based on reachable sets under agent choice.
- **Reachable set (REACH(s,h))**: Set of states reachable by any implementation of HLA h from state s.
- **Optimistic description (REACH+)**: May overstate reachable set.
- **Pessimistic description (REACH−)**: May understate reachable set.
- **Conformant planning**: Planning with no observations (sensorless).
- **Contingent planning**: Planning with conditional branching based on percepts.
- **Percept schema**: Augments PDDL with model of sensors.
- **Conditional effect**: Action effect that depends on state: "when condition : effect."
- **Execution monitoring**: Determining need for new plan during execution.
- **Action monitoring**: Before executing an action, verify preconditions still hold.
- **Plan monitoring**: Before executing an action, verify remaining plan will succeed.
- **Goal monitoring**: Before executing, check if better goals exist.
- **Missing precondition/effect/fluent**: Incomplete action model.
- **Exogenous event**: External event affecting the world.
- **Scheduling**: Adding temporal information to plan to meet resource/deadline constraints.
- **Resource constraints**: Limited resources (staff, equipment, materials).
- **Job-shop scheduling problem**: Set of jobs with actions, ordering constraints, durations, resource constraints.
- **Duration**: Time an action takes.
- **Consumable resource**: Used up (e.g., bolts).
- **Reusable resource**: Occupied during action but available after (e.g., pilot).
- **Makespan**: Total duration of a plan.
- **Aggregation**: Grouping indistinguishable objects into quantities.
- **Critical path method (CPM)**: Algorithm to determine earliest/latest start times.
- **Critical path**: Path with longest total duration; determines plan duration.
- **Slack**: LS − ES (latest start − earliest start) — flexibility of an action.
- **Schedule**: ES and LS times for all actions.
- **Minimum slack heuristic**: Schedule unscheduled action with least slack earliest.
- **Portfolio planning**: Using collection of algorithms for any given problem.
- **Macrops**: "Macro-operators" — sequences of primitive steps learned by STRIPS.
- **Abstraction hierarchy**: Higher planning levels ignore lower-level preconditions.
- **Case-based planning**: Reusing previously computed plans by analogy.
- **Reactive planning systems**: Reflex agents that act without deliberation.
- **PlanSAT**: Question of whether any plan exists for a problem.
- **Bounded PlanSAT**: Whether solution of length ≤ k exists.

---

### 2. SEQUENTIAL PROCESSES

**SATPlan translation steps** (lines 15386–15406):
1. Propositionalize actions (ground all schemas).
2. Add action exclusion axioms.
3. Add precondition axioms (A_t ⇒ PRE(A)_t).
4. Define initial state (F_0 and ¬F_0).
5. Propositionalize goal (disjunction of ground instances).
6. Add successor-state axioms for each fluent.

**Hierarchical Search algorithm (HIERARCHICAL-SEARCH)** (Figure 11.8, lines 15719–15730):
```
frontier ← [Act]
while true do
  if empty(frontier) return failure
  plan ← POP(frontier)  // shallowest
  hla ← first HLA in plan (or null)
  prefix, suffix ← actions before/after hla
  outcome ← RESULT(problem.INITIAL, prefix)
  if hla is null then
    if IS-GOAL(outcome) return plan
  else
    for each sequence in REFINEMENTS(hla, outcome, hierarchy) do
      add APPEND(prefix, sequence, suffix) to frontier
```

**Angelic Search algorithm (ANGELIC-SEARCH)** (Figure 11.11, lines 15923–15951):
```
frontier ← [initialPlan]
while true do
  if EMPTY?(frontier) return fail
  plan ← POP(frontier)
  if REACH+(INITIAL, plan) intersects GOAL then
    if plan is primitive return plan
    guaranteed ← REACH−(INITIAL, plan) ∩ GOAL
    if guaranteed ≠ {} and MAKING-PROGRESS(plan, initialPlan) then
      finalState ← any element of guaranteed
      return DECOMPOSE(hierarchy, INITIAL, plan, finalState)
  hla ← some HLA in plan
  prefix, suffix ← subsequences
  outcome ← RESULT(INITIAL, prefix)
  for each sequence in REFINEMENTS(hla, outcome, hierarchy) do
    frontier ← Insert(APPEND(prefix, sequence, suffix), frontier)
```

**DECOMPOSE** function:
```
while plan not empty do
  action ← REMOVE-LAST(plan)
  s_i ← a state in REACH−(s0, plan) such that s_f ∈ REACH−(s_i, action)
  problem ← problem with INITIAL=s_i and GOAL=s_f
  solution ← APPEND(ANGELIC-SEARCH(problem, hierarchy, action), solution)
  s_f ← s_i
return solution
```

**Critical Path Method for ES/LS computation** (lines 16486–16495):
```
ES(Start) = 0
ES(B) = max_{A≺B} (ES(A) + Duration(A))
LS(Finish) = ES(Finish)
LS(A) = min_{B≻A} (LS(B) − Duration(A))
```

**Belief state update** (lines 16093–16109):
- Physical transition: b' = RESULT(b, a) = {s' : s' = RESULT_P(s, a) ∧ s ∈ b}
- With 1-CNF representation: b' = (b − DEL(a)) ∪ ADD(a)
- Three cases for literal ℓ unknown in b:
  1. If action adds ℓ → ℓ true in b'
  2. If action deletes ℓ → ℓ false in b'
  3. If action doesn't affect ℓ → ℓ unknown in b' (does not appear)

**Belief state update after percept** (two stages):
1. After action: ˆb = (b − DEL(a)) ∪ ADD(a)
2. After percept: add percept literals + preconditions of percept schemas

**Regression for backward planning**:
- POS(g') = (POS(g) − ADD(a)) ∪ POS(Precond(a))
- NEG(g') = (NEG(g) − DEL(a)) ∪ NEG(Precond(a))

---

### 3. HIERARCHIES/CLASSIFICATIONS

**Planning approaches**:
| **Approach** | **Type** | **Characteristics** |
|---|---|---|
| Forward state-space search | Progression | Ground states, all applicable actions |
| Backward state-space search | Regression | Goal states, relevant actions |
| SATPlan | Logical encoding | Propositional SAT solver |
| Graphplan | Specialized graph | Mutual exclusion constraints |
| CSP encoding | Constraint satisfaction | Action_t variable per time step |
| Partial-order planning | Plan-space search | Graph of actions with ordering constraints |
| HTN planning | Hierarchical | HLA refinements, plan libraries |

**Monitoring approaches** (lines 16307–16312):
| **Type** | **Checks** |
|---|---|
| Action monitoring | Preconditions of next action |
| Plan monitoring | Entire remaining plan will succeed |
| Goal monitoring | Whether better goals exist |

---

### 4. COMPARISONS/TRADE-OFFS

| **Forward search** | **Backward search** |
|---|---|
| Branching factor: all applicable actions | Branching factor: relevant actions (smaller) |
| Ground states | States with variables |
| Good heuristics available | Harder to develop heuristics |
| Preferred by most current systems | Lower branching factor |

| **Classical planning** vs **Chapter 3/7 approaches** |
|---|
| Ad hoc heuristics needed for each domain | Domain-independent heuristics from factored representation |
| Explicit exponential state space | Compact action schemas |
| Single schema covers 4·T·n² actions | Separate axiom per orientation/time/location |

| **Conformant** vs **Contingent** vs **Online planning** |
|---|
| No sensors, no observations | Partial observability with sensors | Unknown environments, replanning |
| Single sequence works for all states | Conditional branching | Repair when failures occur |

---

### 5. FORMULAS & EQUATIONS

**RESULT(s, a)** = (s − DEL(a)) ∪ ADD(a)

**Regression**:
- POS(g') = (POS(g) − ADD(a)) ∪ POS(Precond(a))
- NEG(g') = (NEG(g) − DEL(a)) ∪ NEG(Precond(a))

**ES and LS computation**:
```
ES(Start) = 0
ES(B) = max_{A≺B} (ES(A) + Duration(A))
LS(Finish) = ES(Finish)
LS(A) = min_{B≻A} (LS(B) − Duration(A))
```

**Belief state update** (1-CNF): b' = (b − DEL(a)) ∪ ADD(a)

**Reachable set for sequence**: REACH(s, [h1, h2]) = ∪_{s'∈REACH(s, h1)} REACH(s', h2)

**Approximate descriptions**: REACH⁻(s, h) ⊆ REACH(s, h) ⊆ REACH⁺(s, h)

**Heuristic from belief state subsets**: H(b) = max{h(s_1), ..., h(s_N)} for any s_i ∈ b

**Refinement tree complexity**: r^{(d-1)/(k-1)} where r = refinements per HLA, k = actions per refinement, d = primitive actions in solution. Hierarchical cost is k-th root of nonhierarchical cost O(b^d).

---

### 6. RULES, LAWS & THEOREMS

- **Downward refinement property**: If HLA descriptions are true, any high-level plan claiming to achieve the goal must have at least one implementation that does achieve it.
- **PlanSAT is decidable for classical planning** (finite states); semidecidable with function symbols.
- **Bounded PlanSAT** in PSPACE for propositionalized problems.
- **Closed-world assumption for PDDL**: Fluents not mentioned are false.
- **Unique names assumption for PDDL**: Different constants refer to distinct objects.
- **1-CNF belief states are closed under PDDL actions with unconditional effects** — if belief state starts as conjunction of literals, any update yields conjunction of literals.
- **Conditional effects break 1-CNF**: Induce arbitrary dependencies, potentially exponential belief states.

**Effect of HLA on fluent** under angelic semantics (9 possibilities):
- A fluent starting true: can keep true, make false, or have choice
- A fluent starting false: can keep false, make true, or have choice
- Combined: 3×3 = 9 possible effects

---

### 7. DATA STRUCTURES & TYPES

**PDDL Action Schema syntax**:
```
Action(Name(vars),
  PRECOND: conjunction of literals
  EFFECT: conjunction of literals)
```

**PDDL Problem description**:
```
Init(conjunction of ground fluents)
Goal(conjunction of literals)
```

**Percept Schema**:
```
Percept(formula,
  PRECOND: conjunction of literals)
```

**Resource constraints representation**:
```
Resources(Type(n))  // n available
Action(Name, DURATION: t,
  USE: Type(n)      // reusable resources
  CONSUME: Type(n)) // consumable resources
```

---

### 8. EDGE CASES/EXCEPTIONS/TRAPS

- **Blocks world Clear(Table)**: Table is always clear; Move(b,x,Table) has ¬Clear(Table) effect — need separate MoveToTable action.
- **Conditional effects**: Suck action in vacuum world induces non-1-CNF belief state.
- **Missing precondition/effect/fluent**: Leads to model errors requiring monitoring/replanning.
- **Exogenous events**: Cannot be modeled in classical PDDL.
- **Dead ends**: If agent reaches unrecoverable state, cannot guarantee goal achievement.
- **Futile repetition**: Like sphex wasp — must avoid retrying same failed action.
- **Serendipity**: Plan monitoring catches accidental success.
- **Sussman anomaly**: Linear planning cannot interleave subplans; complete planner must allow interleaving.
- **Non-CNF belief state**: Conditional effects lead to exponential belief states; 1-CNF approach incomplete.

---

### 9. EMPIRICAL EVIDENCE/KEY RESULTS

- **Air cargo problem branching**: 2000 actions per state average; 2000⁴¹ nodes for 41-step solution — hopeless without good heuristic.
- **Backward search efficiency**: Compare Own(9780134610993) — forward enumerates billions of Buy actions; backward considers 1 action (Unify + regress).
- **O-PLAN**: Generates plans with millions of steps (30-day schedule, 350 products, 35 machines, 2000+ operations).
- **ANGELIC-SEARCH**: Scales approximately linearly in number of squares vs exponential for HIERARCHICAL-SEARCH and BREADTH-FIRST-SEARCH on vacuum world.
- **Deep Space One Remote Agent**: First autonomous planner-scheduler to control spacecraft (1999).
- **11×10 job-shop problem**: Proposed 1963, optimal solution unknown for 23 years.
- **Ignore-delete-lists heuristic**: No local minima in diagrammed state spaces (Figure 11.6).
- **Conformant planners**: Five orders of magnitude faster than CGP (2006 competition).
- **Portfolio planning (FDSS)**: Won 2018 International Planning Competition.
- **STRIPS**: First major planning system; ran on computer with only 192 KB memory.

---

### 10. DATES & PEOPLE

- **Fikes and Nilsson (1971)**: STRIPS, Shakey robot.
- **Sacerdoti (1974)**: ABSTRIPS (abstraction hierarchy).
- **Sacerdoti (1975)**: Linear planning → incomplete (Sussman anomaly).
- **Sussman (1975)**: HACKER system, Sussman anomaly.
- **Sacerdoti (1977)**: NOAH (partial-order planning).
- **Tate (1977)**: NONLIN.
- **Chapman (1987)**: Formal modal of partial-order planning.
- **Blum and Furst (1997)**: Graphplan (orders of magnitude faster).
- **Kautz and Selman (1998)**: BLACKBOX planner.
- **Hoffmann (2001, 2005)**: FF (FastForward).
- **Helmert (2006)**: FastDownward.
- **Marthi et al. (2007, 2008)**: Angelic semantics for HLAs.
- **McDermott (1996)**: UNPOP (resurrected state-space planning).
- **Bonet and Geffner (1999)**: HSP (Heuristic Search Planner).
- **Ghallab et al. (1998)**: PDDL.
- **Kovacs (2011)**: PDDL 3.1.
- **Brooks (1986)**: Reactive planning.
- **Fikes et al. (1972)**: PLANEX execution monitoring.
- **Bell and Tate (1985)**: O-PLAN.
- **Muscettola et al. (1998)**: Remote Agent (Deep Space One).
- **Wilkins (1988)**: SIPE.
- **Sacerdoti (1975)**: Linear planning; Sussman anomaly.

---

### 11. CASE STUDIES/CLASSIC EXAMPLES

**Air cargo transport** (Figure 11.1, lines 15166–15189):
- Objects: 2 planes (P1,P2), 2 cargos (C1,C2), 2 airports (SFO,JFK)
- Actions: Load(c,p,a), Unload(c,p,a), Fly(p,from,to)
- Initial: At(C1,SFO), At(C2,JFK), At(P1,SFO), At(P2,JFK)
- Goal: At(C1,JFK) ∧ At(C2,SFO)
- Solution: [Load(C1,P1,SFO), Fly(P1,SFO,JFK), Unload(C1,P1,JFK), Load(C2,P2,JFK), Fly(P2,JFK,SFO), Unload(C2,P2,SFO)]

**Spare tire problem** (Figure 11.2, lines 15191–15198):
- Initial: Tire(Flat) ∧ Tire(Spare) ∧ At(Flat,Axle) ∧ At(Spare,Trunk)
- Goal: At(Spare,Axle)
- Actions: Remove(obj,loc), PutOn(t,Axle), LeaveOvernight (bad neighborhood!)
- Solution: [Remove(Flat,Axle), Remove(Spare,Trunk), PutOn(Spare,Axle)]

**Blocks world** (Figures 11.3-11.4):
- Goal: On(A,B) ∧ On(B,C) starting with On(C,A), others on Table
- Solution: [MoveToTable(C,A), Move(B,Table,C), Move(A,Table,B)]

**Painting problem** (lines 15999–16041):
- Initial: unknown colors of furniture and paint cans; only Table in view
- Goal: Color(Chair,c) ∧ Color(Table,c)
- Sensorless solution: remove lid from any can, paint both chair and table (coercion)
- Contingent solution: look at table and chair, if matching → done; else look at cans, apply matching color; else paint both with any color

**Job-shop assembly** (Figure 11.13):
- 2 cars, each requiring AddEngine, AddWheels, Inspect (in order)
- Resources: 1 engine hoist, 1 wheel station, 2 inspectors, 500 lug nuts
- Schedule without resource constraints: 85 min; with constraints: 115 min
- Critical path: AddEngine2(60) + AddWheels2(15) + Inspect2(10) = 85 min

---

### 12. PROOF & ARGUMENT PATTERNS

**Why ignore-delete-lists creates a useful relaxation**: Makes monotonic progress toward goal — no action undoes progress. Solution length serves as admissible heuristic. Still NP-hard to find optimal solution, but approximate solution in polynomial time via hill climbing.

**Why backward search can beat forward search exponentially**: Example: ISBN domain — forward must enumerate 10¹³ ground Buy actions; backward unifies goal Own(9780134610993) with effect Own(i'), yields precondition ISBN(9780134610993), finds it in initial state, done.

**Angelic vs demonic semantics**: Demonic = adversary chooses implementation (must work for all). Angelic = agent chooses (need at least one working). Angelic semantics allows describing HLA effects with ~possible± effects, enabling abstract plan validation without full refinement.

---

This concludes the comprehensive extraction. All four chapters have been fully covered with every named entity, formula, algorithm step, comparison, edge case, case study, and historical reference presented in structured format.
</task_result>
</task>

---

# CHAPTER 12: QUANTIFYING UNCERTAINTY

## 1. NAMED ENTITIES (Terms/Concepts/Definitions)

- **Uncertainty**: Arises from partial observability, nondeterminism, or adversaries
- **Belief state**: A representation of the set of all possible world states that an agent might be in
- **Qualification problem**: Cannot deduce for sure that a plan succeeds because of an unbounded list of possible exceptions
- **Laziness**: Too much work to list complete set of antecedents/consequents needed for an exceptionless rule
- **Theoretical ignorance**: Medical science has no complete theory for the domain
- **Practical ignorance**: Cannot run all necessary tests
- **Degree of belief**: The agent's knowledge can at best provide only a degree of belief in relevant sentences
- **Probability theory**: Main tool for dealing with degrees of belief; ontological commitment same as logic (facts that do/don't hold); epistemological commitment differs (numerical degree of belief between 0 and 1)
- **Preference**: Agent must have preferences among possible outcomes of plans
- **Outcome**: A completely specified state including factors such as whether the agent arrives on time
- **Utility theory**: Represents preferences and reasons quantitatively with them
- **Decision theory**: Decision theory = probability theory + utility theory
- **Maximum expected utility (MEU) principle**: An agent is rational iff it chooses the action that yields the highest expected utility, averaged over all possible outcomes
- **Sample space (Ω)**: The set of all possible worlds; mutually exclusive and exhaustive
- **Probability model**: Associates a numerical probability P(ω) with each possible world
- **Event**: A set of possible worlds (in probability theory); corresponds to a proposition in logic
- **Unconditional/prior probability**: Degree of belief in propositions in the absence of any other information
- **Evidence**: Information that has already been revealed
- **Conditional/posterior probability**: Probability given evidence, written P(a|b)
- **Product rule**: P(a∧b) = P(a|b)P(b)
- **Random variable**: A function mapping from domain of possible worlds Ω to some range; names begin with uppercase letter
- **Range**: The set of possible values a random variable can take on
- **Bernoulli distribution**: Boolean random variable with range {0, 1}
- **Probability distribution**: Assignment of a probability for each possible value of a random variable; denoted by bold P
- **Categorical distribution**: A distribution over a finite, discrete range
- **Probability density function (pdf)**: For continuous variables, defines probability that a random variable takes on some value x as a parameterized function of x
- **Joint probability distribution**: Distribution on multiple variables; e.g., P(Weather,Cavity) is a 4×2 table
- **Full joint probability distribution**: Joint distribution for all random variables; completely determines the probability model
- **Inclusion–exclusion principle**: P(a∨b) = P(a) + P(b) − P(a∧b)
- **Kolmogorov's axioms**: Equations (12.1) and (12.5); foundation of probability theory
- **Marginal probability**: Unconditional probability of a variable, obtained by summing out other variables
- **Marginalization/summing out**: Summing probabilities for each possible value of other variables
- **Conditioning**: P(Y) = ∑z P(Y|z)P(z)
- **Normalization constant (α)**: Used to ensure probabilities sum to 1
- **Independence (absolute/marginal)**: P(a|b) = P(a) or P(b|a) = P(b) or P(a∧b) = P(a)P(b)
- **Bayes' rule/Bayes' law/Bayes' theorem**: P(b|a) = P(a|b)P(b)/P(a)
- **Causal direction**: P(effect|cause)
- **Diagnostic direction**: P(cause|effect)
- **Conditional independence**: P(X,Y|Z) = P(X|Z)P(Y|Z)
- **Separation**: Conceptually, Cavity separates Toothache and Catch because it is a direct cause of both
- **Naive Bayes model**: P(Cause, Effect₁, …, Effectₙ) = P(Cause)∏ᵢ P(Effectᵢ|Cause)
- **Bayesian classifier/idiot Bayes model**: Alternative names for naive Bayes
- **Text classification**: Deciding which of predefined categories a text belongs to
- **Frontier**: Pit variables (other than query) adjacent to visited squares
- **Reference class problem**: In frequentist statistics, determining what class of "similar" experiments is appropriate
- **Principle of indifference**: Assigning equal probabilities due to lack of knowledge; attributed to Laplace
- **Principle of insufficient reason**: Same as principle of indifference; named by Boole and Venn
- **Frequentist position**: Probabilities come only from experiments
- **Objectivist view**: Probabilities are real aspects of the universe—propensities
- **Subjectivist view**: Probabilities characterize an agent's beliefs
- **Inductive logic**: Mathematical discipline studying degree of confirmation as logical relation between a and e (Carnap)
- **Vitali set**: A well-defined subset of [0,1] with no well-defined size (complication with continuous variables)

## 2. SEQUENTIAL PROCESSES (Algorithms/Procedures)

### Decision-Theoretic Agent (DT-Agent)
```
function DT-AGENT(percept) returns an action
  persistent: belief_state, probabilistic beliefs about the current state of the world
              action, the agent's action
  update belief_state based on action and percept
  calculate outcome probabilities for actions,
    given action descriptions and current belief_state
  select action with highest expected utility
    given probabilities of outcomes and utility information
  return action
```

### General Inference Procedure (from full joint distribution)
1. Identify query variable X, evidence variables E with observed values e, and remaining unobserved variables Y
2. Compute P(X|e) = α P(X,e) = α ∑y P(X,e,y)
3. The summation is over all possible combinations of values of unobserved variables Y

### Normalization shortcut process
1. Compute α[P(cavity,toothache,catch) + P(cavity,toothache,¬catch)] = α⟨0.12, 0.08⟩
2. Divide each by sum (0.12+0.08=0.20) to get ⟨0.6, 0.4⟩

### Text Classification with Naive Bayes
1. Estimate P(Category=c) as fraction of previously seen documents of category c
2. Estimate P(HasWordᵢ|Category) as fraction of documents of each category that contain word i
3. For new document: check which key words appear
4. Apply Equation (12.21): multiply prior probability of the cause by product of conditional probabilities of observed effects given the cause
5. Normalize the result
6. Predict the category with highest posterior probability

### Wumpus World Probabilistic Reasoning
1. Identify random variables: Pᵢⱼ (pit in square) and Bᵢⱼ (breeze)
2. Specify full joint distribution: P(Breezes|Pits) × P(Pits)
3. Partition unknown squares: Known, Frontier, Query, Other
4. Use conditional independence: observed breezes are conditionally independent of Other given Known, Query, and Frontier
5. Sum only over Frontier variables (not all Unknown)
6. Result: P(P₁,₃|known,b) = α′ P(P₁,₃) ∑_frontier P(b|known,P₁,₃,frontier) P(frontier)

## 3. HIERARCHIES/CLASSIFICATIONS

### Three Reasons Logical Approach Fails for Medical Diagnosis
1. Laziness
2. Theoretical ignorance
3. Practical ignorance

### Three Drawbacks of Contingent Planning for Uncertainty
1. Agent must consider every possible explanation for sensor observations, no matter how unlikely
2. A correct contingent plan that handles every eventuality can grow arbitrarily large
3. Sometimes there is no plan guaranteed to achieve the goal—yet the agent must act

### Probability Interpretations (Philosophical Positions)
1. **Frequentist**: Numbers come only from experiments; probability = limiting fraction in infinite samples
2. **Objectivist (propensity)**: Probabilities are real aspects of the universe
3. **Subjectivist (Bayesian)**: Probabilities characterize an agent's beliefs; allows any self-consistent ascription of priors but insists on proper Bayesian updating

### Types of Random Variables (by range)
- Boolean: range {true, false} or {0, 1} (Bernoulli distribution)
- Discrete finite: e.g., Weather = {sun, rain, cloud, snow}
- Discrete infinite: e.g., integers
- Continuous: e.g., reals

### Variable classifications by knowledge
- Query variables (X)
- Evidence variables (E) — observed
- Hidden/unobserved variables (Y)

## 4. COMPARISONS/TRADE-OFFS

| Aspect | Logical Agent | Probabilistic Agent |
|--------|---------------|---------------------|
| Epistemological commitment | Sentence is true/false or no opinion | Numerical degree of belief between 0 and 1 |
| Ontological commitment | World composed of facts | Same as logic |
| Handling qualification problem | Cannot handle | Summarizes uncertainty from laziness and ignorance |
| Contingent plan size | Grows arbitrarily large | Uses expected utility to compare |

- **Prior vs. posterior probability**: Prior is degree of belief before evidence; posterior is after evidence
- **Causal vs. diagnostic knowledge**: Causal (model-based) is more robust to changes in base rates; diagnostic is more fragile
- **Absolute (marginal) independence vs. conditional independence**: Absolute independence between entire sets of variables is rare; conditional independence is much more common and allows scaling up
- **Naive Bayes full joint vs. conditional representation**: Full joint is O(2ⁿ); naive Bayes is O(n)

## 5. FORMULAS & EQUATIONS

**Basic probability axioms** (Eq 12.1):
0 ≤ P(ω) ≤ 1 for every ω, and ∑_{ω∈Ω} P(ω) = 1

**Probability of a proposition** (Eq 12.2):
P(φ) = ∑_{ω∈φ} P(ω)

**Conditional probability** (Eq 12.3):
P(a|b) = P(a∧b) / P(b), where P(b) > 0

**Product rule** (Eq 12.4):
P(a∧b) = P(a|b)P(b)

**Inclusion–exclusion principle** (Eq 12.5):
P(a∨b) = P(a) + P(b) − P(a∧b)

**Marginalization rule** (Eq 12.7):
P(Y) = ∑_z P(Y, Z=z)

**Conditioning rule** (Eq 12.8):
P(Y) = ∑_z P(Y|z) P(z)

**Independence** (Eq 12.11):
P(a|b) = P(a) or P(b|a) = P(b) or P(a∧b) = P(a)P(b)

**Bayes' rule** (Eq 12.12):
P(b|a) = P(a|b)P(b) / P(a)

**Bayes' rule with background evidence** (Eq 12.13):
P(Y|X,e) = P(X|Y,e)P(Y|e) / P(X|e)

**Bayes' rule with normalization** (Eq 12.15):
P(Y|X) = α P(X|Y) P(Y)

**General inference from full joint** (Eq 12.9):
P(X|e) = α P(X,e) = α ∑_y P(X,e,y)

**Naive Bayes model** (Eq 12.20):
P(Cause, Effect₁, …, Effectₙ) = P(Cause) ∏ᵢ P(Effectᵢ|Cause)

**Naive Bayes inference for query** (Eq 12.21):
P(Cause|e) = α P(Cause) ∏ⱼ P(eⱼ|Cause)

**Conditional independence definition** (Eq 12.19):
P(X,Y|Z) = P(X|Z)P(Y|Z)

**De Finetti's Dutch book**: Agent with inconsistent beliefs (violating Kolmogorov's axioms) can be forced to lose money regardless of outcome

## 6. RULES, LAWS & THEOREMS

- **Decision theory**: Decision theory = probability theory + utility theory
- **Principle of Maximum Expected Utility (MEU)**: An agent is rational iff it chooses the action that yields the highest expected utility
- **Kolmogorov's axioms**: (1) 0 ≤ P(ω) ≤ 1 for all ω; (2) ∑_{ω∈Ω} P(ω) = 1; (3) P(a∨b) = P(a) + P(b) − P(a∧b)
- **De Finetti's theorem**: If an agent's degrees of belief violate probability axioms, there exists a combination of bets that guarantees the agent loses money every time; implies no rational agent can have beliefs violating the axioms
- **Cox's theorem**: Any system for uncertain reasoning meeting certain assumptions is equivalent to probability theory (but see Halpern's gaps and Horn's fix)
- **Product rule**: P(a∧b) = P(a|b)P(b)
- **Bayes' rule**: P(b|a) = P(a|b)P(b)/P(a)

## 7. DATA STRUCTURES & TYPES

- **Full joint probability distribution**: A table of probabilities for all combinations of values of all random variables; size O(2ⁿ) for n Boolean variables
- **Conditional probability table (CPT)**: Used for conditional distributions; for Boolean variable with k Boolean parents, contains 2ᵏ independently specifiable probabilities
- **Probability vector (bold P notation)**: Represents a probability distribution as a vector of numbers with predefined ordering
- **Probability density function (pdf)**: For continuous variables; P(x) = lim_{dx→0} P(x ≤ X ≤ x+dx)/dx; has units (e.g., reciprocal degrees)

## 8. VISUAL PATTERNS

- **Figure 12.1**: Decision-theoretic agent architecture (pseudocode)
- **Figure 12.2**: Dutch book table showing Agent 1's inconsistent beliefs and guaranteed loss
- **Figure 12.3**: Full joint distribution for Toothache, Cavity, Catch (2×2×2 table)
- **Figure 12.4**: Factoring a large joint distribution using absolute independence: (a) Weather independent of dental problems; (b) Independent coin flips
- **Figure 12.5**: Wumpus world: (a) stuck with no safe place; (b) division into Known, Frontier, Other
- **Figure 12.6**: Consistent models for frontier variables P₂,₂ and P₃,₁ showing P(frontier) for each model

## 9. EDGE CASES/EXCEPTIONS/TRAPS

- **Probability zero in naive Bayes**: If a word has not been seen previously in a category, its conditional probability must not be set to zero (would wipe out all evidence). Instead, reserve a small portion for "previously unseen" words
- **Conditional probability defined only when P(b) > 0**: P(a|b) = P(a∧b)/P(b) holds only when P(b) > 0
- **Continuous variables**: Probability that a continuous variable equals exactly a specific value is zero; we work with density functions
- **Density functions have units**: P(NoonTemp = 20.18°C) = 1/8°C is not a probability but a density
- **Conditioning vs. logical implication**: P(cavity|toothache)=0.6 does NOT mean "whenever toothache is true, conclude cavity with probability 0.6" — it means "whenever toothache is true and we have NO FURTHER INFORMATION"
- **Doubles variable redundancy**: Adding Doubles as a random variable in addition to Die₁ and Die₂ creates 72 possible worlds, half logically impossible with probability 0
- **Naive Bayes overconfidence**: Violation of independence means posterior probabilities will be much closer to 1 or 0 than they should be, though ranking is often accurate

## 10. EMPIRICAL EVIDENCE/KEY RESULTS

- **Meningitis example**: P(s|m) = 0.7, P(m) = 1/50000, P(s) = 0.01 → P(m|s) = 0.0014 (only 0.14% of stiff neck patients have meningitis)
- **Full joint table size**: For n=100 Boolean variables, table has 2¹⁰⁰ ≈ 10³⁰ entries — impractical
- **Wumpus world**: P(P₁,₃|known,b) ≈ ⟨0.31, 0.69⟩; P(P₂,₂|known,b) ≈ 0.86 (86% chance of pit — much worse than [1,3])

## 11. CROSS-CHAPTER DEPENDENCIES

- Chapter 2: Performance measure and expectation
- Section 8.1: Ontological vs. epistemological commitments
- Chapter 5 (backgammon optimal decisions), Chapters 4 and 7 (belief state maintenance)
- Chapter 14: Methods for representing/updating belief state over time and predicting outcomes
- Chapter 15: Combining probability theory with first-order logic and programming languages
- Chapter 16: Utility theory in more depth
- Chapter 17: Planning sequences of actions in stochastic environments
- Chapter 18: Multiagent environments
- Chapter 7 (wumpus world): full description of wumpus world for Section 12.7
- Chapter 13: Bayesian networks (mentioned as next step)
- Chapter 20: Learning (mentioned for unseen words)

## 12. DATES & PEOPLE

- **Andrei Kolmogorov** (1903–1987): Russian mathematician; Kolmogorov's axioms (1933)
- **Bruno de Finetti** (1906–1985): Dutch book argument (1931); English translation 1993
- **R. T. Cox** (1946): Axiomatic derivation of probability
- **Rudolf Carnap** (1950): Inductive logic
- **E. T. Jaynes** (2003): Probability as logic
- **Rev. Thomas Bayes** (1702–1761): Bayes' rule; paper published posthumously 1763
- **Pierre Laplace** (1749–1827): Independently developed general case of Bayes' rule; "Probability theory is nothing but common sense reduced to calculation" (1819)
- **James Maxwell** (1831–1879): "The true logic for this world is the calculus of Probabilities" (1850)
- **Girolamo Cardano** (~1565): First systematic analysis of probability (published 1663)
- **Blaise Pascal and Pierre de Fermat** (1654): Correspondence establishing probability as mathematical discipline
- **Christiaan Huygens** (1657): First published textbook on probability, *De Ratiociniis in Ludo Aleae*
- **John Arbuthnot** (1692): "Laziness and ignorance" view of uncertainty
- **James Bernoulli** (1654–1705): First to draw clear distinction between objective and subjective interpretations
- **Gottfried Leibniz**: Classical notion of probability as proportion of enumerated equally probable cases
- **I. J. Good** (1983): "Every event in life is unique"
- **Mahaviracarya** (~850 CE): Indian mathematician; described Dutch book
- **R. A. Fisher** (1922), **Richard von Mises** (1928): Relative frequency interpretation advocates
- **Karl Popper** (1934/1959): Propensity interpretation
- **Frank Ramsey** (1931): Degree of belief tied to betting behavior
- **Leonard Savage** (1954): Analysis of betting circumvents unequal bank balance problem
- **Richard Jeffrey** (1983): Subjective probability
- **George Boole, John Venn**: Principle of insufficient reason
- **John Maynard Keynes** (1921): Coined "principle of indifference"
- **Hilary Putnam** (1963): Showed inherent difficulties in extending inductive logic beyond propositional case
- **Bacchus, Grove, Halpern, Koller** (1992): Extend Carnap's methods to first-order theories

## 13. PROOF & ARGUMENT PATTERNS

- **Derivation of negation formula**: P(¬a) = 1 − P(a) — from Equations (12.1) and (12.2)
- **Derivation of inclusion–exclusion**: P(a∨b) = P(a) + P(b) − P(a∧b) — noting double counting of intersection
- **De Finetti's Dutch book argument**: Constructs a set of bets that guarantees loss if axioms are violated; uses table showing payoffs for each combination of outcomes
- **Conditional independence decomposition**: P(Toothache, Catch, Cavity) = P(Toothache|Cavity) P(Catch|Cavity) P(Cavity) — reduces from 7 to 5 independent numbers
- **Wumpus world conditional independence**: Breezes are conditionally independent of Other given Known, Query, and Frontier — allows moving summation inward

## 14. DESIGN PARADIGMS/META-METHODS

- **Factored representation**: Possible world represented by a set of variable/value pairs (Section 2.4.7)
- **Marginalization/summing out**: Fundamental technique for reducing variables
- **Normalization**: Shortcut allowing computation without knowing P(evidence)
- **Divide and conquer through conditional independence**: Decomposing large probabilistic domains into weakly connected subsets

## 15. CASE STUDIES/CLASSIC EXAMPLES

- **Automated taxi airport plan A90 vs. A180 vs. A1440**: Illustrates trade-off between probability of success and utility of different outcomes
- **Dental diagnosis**: Toothache → Cavity example; three patients (toothache only, toothache + gum disease history, conclusive evidence against cavity)
- **Two dice**: 36 possible worlds; P(Total=11) = 1/18; prior vs. conditional given Die₁=5
- **Meningitis/stiff neck**: P(s|m)=0.7, P(m)=1/50000, P(s)=0.01 → P(m|s)=0.0014
- **Wumpus world probabilistic reasoning**: [1,3] has 31% pit probability; [2,2] has 86% pit probability — probabilistic agent outperforms logical agent
- **Text classification with naive Bayes**: Two newspaper sentences (stocks, rain) classified into news/sports/business/weather/entertainment

## 16. ETHICS
- Note about hidden variables potentially becoming proxies for race in insurance decisions (page 439, footnote 4 in Ch. 13 — actually in Ch. 12 insurance discussion, but noted)

## 17. END-OF-CHAPTER MATERIAL

**Summary points** (12 bullet points):
- Uncertainty arises from laziness and ignorance
- Probabilities express inability to reach definite decision
- Decision theory = probabilities + utilities; MEU principle
- Prior/unconditional vs. posterior/conditional probabilities
- Kolmogorov's axioms constrain probabilities
- Full joint distribution specifies probability of each complete assignment
- Absolute independence allows factoring into smaller distributions
- Bayes' rule relates causal and diagnostic probabilities
- Conditional independence through causal relationships allows factoring
- Naive Bayes model assumes conditional independence of effects given cause; linear growth
- Wumpus-world agent uses probabilities to improve on logical agent

**Bibliographical notes**: Rich history from 850 CE (Mahaviracarya) through modern developments

---

# CHAPTER 13: PROBABILISTIC REASONING

## 1. NAMED ENTITIES (Terms/Concepts/Definitions)

- **Bayesian network (Bayes net/belief network/causal network)**: A directed graph in which each node is annotated with quantitative probability information; represents dependencies among variables
- **Graphical model**: Broader class that includes Bayesian networks
- **Parameter**: The finite number of probability values associated with each node, quantifying the effect of parents on the node
- **Conditional probability table (CPT)**: Local probability information attached to each node; rows correspond to conditioning cases (combinations of parent values); each row sums to 1
- **Conditioning case**: A possible combination of values for the parent nodes
- **Chain rule**: P(x₁,…,xₙ) = ∏ᵢ P(xᵢ|xᵢ₋₁,…,x₁) — holds for any set of random variables
- **Topological ordering**: An ordering consistent with the directed graph structure (causes before effects)
- **Locally structured (sparse) systems**: Each subcomponent interacts directly with only a bounded number of other components
- **Descendant**: In a Bayes net, a variable that inherits through directed links
- **Markov blanket**: Parents, children, and children's parents of a node; d-separates the node from all other variables
- **d-separation**: A criterion for determining conditional independence in a Bayes net; Z d-separates X and Y if Z blocks all paths between X and Y in the undirected, moralized, ancestral subgraph
- **Ancestral subgraph**: Subgraph consisting of X, Y, Z, and their ancestors
- **Moral graph**: Graph obtained by adding links between unlinked pairs of nodes that share a common child, then replacing directed links with undirected links
- **Canonical distribution**: A standard pattern that describes relationships between parents and child, allowing the complete table to be specified by naming the pattern and supplying a few parameters
- **Deterministic node**: A node whose value is specified exactly by its parents with no uncertainty
- **Context-specific independence (CSI)**: A variable is conditionally independent of some of its parents given certain values of others
- **Noisy-OR**: A generalization of logical OR allowing uncertainty about each parent's ability to cause the child; assumes all possible causes listed and independent inhibition
- **Leak node**: Covers "miscellaneous causes" not explicitly listed in noisy-OR model
- **Discretization**: Dividing continuous values into a fixed set of intervals
- **Nonparametric representation**: Defining conditional distribution implicitly with a collection of instances
- **Hybrid Bayesian network**: Network with both discrete and continuous variables
- **Linear–Gaussian conditional distribution**: Child has Gaussian distribution whose mean varies linearly with parent value; standard deviation σ is fixed
- **Conditional Gaussian (CG) distribution**: Given any assignment to discrete variables, distribution over continuous variables is multivariate Gaussian
- **Probit model** ("probability unit"): Uses integral of standard normal distribution Φ(x) for soft threshold
- **Expit/inverse logit model**: Uses logistic function 1/(1+e⁻ˣ) for soft threshold
- **Hidden variable**: Variables that are neither input nor output but essential for structuring the network
- **Event** (in inference context): An assignment of values to a set of evidence variables
- **Variable elimination**: Exact inference algorithm using dynamic programming; evaluates sums of products of conditional probabilities
- **Factor**: A matrix indexed by the values of its argument variables
- **Pointwise product**: Operation on factors; f×g yields h whose variables are union of variables in f and g
- **Singly connected network/polytree**: At most one undirected path between any two nodes; exact inference linear in network size
- **Multiply connected network**: Networks with multiple undirected paths between nodes; variable elimination can have exponential complexity
- **Reduction**: Encoding a propositional satisfiability problem as a Bayes net
- **Weighted model counting (WMC)**: Sums the total weight of satisfying assignments for a SAT expression
- **Clustering algorithms/join tree algorithms**: Combine individual nodes into cluster nodes to form a polytree; can compute posterior probabilities for all variables in O(n)
- **Meganode**: A node formed by clustering that takes on all combinations of values of original nodes
- **Monte Carlo algorithms**: Randomized sampling algorithms providing approximate answers
- **Consistent estimate**: Estimate that becomes exact in the large-sample limit
- **Rejection sampling**: Generates samples from prior distribution, rejects those not matching evidence
- **Importance sampling**: Samples from an easy distribution Q and applies correction factor P(x)/Q(x)
- **Likelihood weighting**: Importance sampling for Bayes nets; fixes evidence variables, samples nonevidence variables in topological order; weight = product of conditional probabilities for evidence variables
- **Markov chain Monte Carlo (MCMC)**: Generates samples by making random changes to the preceding sample
- **Gibbs sampling**: MCMC that samples each nonevidence variable conditioned on its Markov blanket
- **Metropolis–Hastings (MH)**: General MCMC with proposal distribution and acceptance probability
- **Proposal distribution**: q(x′|x) — proposes a next state given current state
- **Acceptance probability**: a(x′|x) = min(1, π(x′)q(x|x′)/π(x)q(x′|x))
- **Transition kernel**: k(x→x′) — probability of transition from state x to state x′
- **Stationary distribution**: Distribution π satisfying π(x′) = ∑_x π(x)k(x→x′) for all x′
- **Ergodic**: Every state reachable from every other and no strictly periodic cycles
- **Detailed balance**: π(x)k(x→x′) = π(x′)k(x′→x) for all x, x′
- **Mixing rate**: Rate of convergence of MCMC to stationary distribution
- **Block sampling**: Sampling multiple variables simultaneously
- **Causal network**: Restricted class of Bayesian networks forbidding all but causally compatible orderings
- **Structural equation**: xi = fᵢ(OtherVariables); describes a stable mechanism in nature that remains invariant to measurements and local changes
- **Unmodeled variables/error terms/disturbances (U)**: Variables in structural equations representing unmodeled perturbations
- **Do-calculus**: Notation for interventions; do(Sprinkler=true) means imposing the condition by intervention
- **Adjustment formula**: P(xᵢ|do(xⱼₖ)) = ∑_{parents(Xⱼ)} P(xᵢ|xⱼₖ, parents(Xⱼ)) P(parents(Xⱼ))
- **Back-door criterion**: Allows writing adjustment formula conditioning on any set Z that closes the back door (d-separation condition)
- **Randomized controlled trial**: The gold standard for causal inference; back-door criterion provides alternative
- **Loopy belief propagation**: Applying Pearl's polytree message-passing algorithm to general "loopy" networks
- **Turbo decoding**: Error-correcting code algorithm discovered to be loopy BP
- **Certainty factor**: "Fudge factor" added to rules to accommodate uncertainty (MYCIN system)
- **Dempster–Shafer theory**: Generalization of probability to interval values
- **Fuzzy logic**: Reasoning with logical expressions about membership in fuzzy sets
- **Possibility theory**: Handles uncertainty in fuzzy systems
- **Qualitative probabilistic networks**: Qualitative abstraction of Bayesian networks using positive/negative influences
- **Most probable explanation (MPE)**: Most likely assignment to nonevidence variables given evidence
- **MAP (maximum a posteriori)**: Most likely assignment to a subset of nonevidence variables
- **Nonserial dynamic programming**: Variable elimination for Bayes nets is essentially identical to this
- **Pedigree analysis**: Mathematical models for genetic inheritance; special form of Bayesian networks
- **Variational approximation**: Proposes reduced version of problem and minimizes distance function D between original and reduced
- **Mean-field method**: Variational approximation assuming variables are completely independent

## 2. SEQUENTIAL PROCESSES (Algorithms/Procedures)

### Method for Constructing Bayesian Networks
1. **Nodes**: Determine set of variables; order them {X₁,…,Xₙ} with causes before effects
2. **Links**: For i = 1 to n:
   - Choose a minimal set of parents for Xᵢ from X₁,…,Xᵢ₋₁ such that P(Xᵢ|Xᵢ₋₁,…,X₁) = P(Xᵢ|Parents(Xᵢ))
   - For each parent, insert a link from the parent to Xᵢ
3. **CPTs**: Write down the conditional probability table P(Xᵢ|Parents(Xᵢ))

### Enumeration-ASK Algorithm
```
function ENUMERATION-ASK(X, e, bn) returns a distribution over X
  Q(X) ← a distribution over X, initially empty
  for each value xᵢ of X do
    Q(xᵢ) ← ENUMERATE-ALL(vars, eₓᵢ)
  return NORMALIZE(Q(X))

function ENUMERATE-ALL(vars, e) returns a real number
  if EMPTY?(vars) then return 1.0
  V ← FIRST(vars)
  if V is an evidence variable with value v in e
    then return P(v|parents(V)) × ENUMERATE-ALL(REST(vars), e)
    else return ∑ᵥ P(v|parents(V)) × ENUMERATE-ALL(REST(vars), eᵥ)
```

### Variable Elimination Algorithm
```
function ELIMINATION-ASK(X, e, bn) returns a distribution over X
  factors ← []
  for each V in ORDER(vars) do
    factors ← [MAKE-FACTOR(V, e)] + factors
    if V is a hidden variable then factors ← SUM-OUT(V, factors)
  return NORMALIZE(POINTWISE-PRODUCT(factors))
```

### Pointwise Product Operation
f(X₁…Xⱼ,Y₁…Yₖ) × g(Y₁…Yₖ,Z₁…Zₗ) = h(X₁…Xⱼ,Y₁…Yₖ,Z₁…Zₗ)
- Each entry = product of corresponding entries in f and g
- Size = 2^(j+k+ℓ) for binary variables

### Summing Out a Variable
∑_x h(X,Y,Z) = h(x,Y,Z) + h(¬x,Y,Z)
- Factors not depending on the variable can be moved outside the summation

### d-separation Procedure
1. Consider just the ancestral subgraph consisting of X, Y, Z, and their ancestors
2. Add links between any unlinked pair of nodes that share a common child (moral graph)
3. Replace all directed links by undirected links
4. If Z blocks all paths between X and Y, then Z d-separates X and Y (conditional independence holds)

### Prior-Sample Algorithm
```
function PRIOR-SAMPLE(bn) returns an event sampled from the prior
  x ← an event with n elements
  for each variable Xᵢ in X₁,…,Xₙ do
    x[i] ← a random sample from P(Xᵢ|parents(Xᵢ))
  return x
```

### Rejection-Sampling Algorithm
```
function REJECTION-SAMPLING(X, e, bn, N) returns an estimate of P(X|e)
  C ← a vector of counts for each value of X, initially zero
  for j = 1 to N do
    x ← PRIOR-SAMPLE(bn)
    if x is consistent with e then
      C[j] ← C[j] + 1
  return NORMALIZE(C)
```

### Likelihood-Weighting Algorithm
```
function LIKELIHOOD-WEIGHTING(X, e, bn, N) returns an estimate of P(X|e)
  W ← a vector of weighted counts for each value of X, initially zero
  for j = 1 to N do
    x, w ← WEIGHTED-SAMPLE(bn, e)
    W[j] ← W[j] + w
  return NORMALIZE(W)

function WEIGHTED-SAMPLE(bn, e) returns an event and a weight
  w ← 1; x ← an event with n elements, with values fixed from e
  for i = 1 to n do
    if Xᵢ is an evidence variable with value xᵢⱼ in e
      then w ← w × P(Xᵢ = xᵢⱼ | parents(Xᵢ))
      else x[i] ← a random sample from P(Xᵢ|parents(Xᵢ))
  return x, w
```

### Gibbs Sampling Algorithm
```
function GIBBS-ASK(X, e, bn, N) returns an estimate of P(X|e)
  C ← a vector of counts for each value of X, initially zero
  Z ← the nonevidence variables in bn
  x ← the current state of the network, initialized from e
  initialize x with random values for the variables in Z
  for k = 1 to N do
    choose any variable Zᵢ from Z according to any distribution ρ(i)
    set the value of Zᵢ in x by sampling from P(Zᵢ|mb(Zᵢ))
    C[j] ← C[j] + 1
  return NORMALIZE(C)
```

### Metropolis–Hastings Sampling (per iteration)
1. Sample a new state x′ from a proposal distribution q(x′|x), given current state x
2. Compute acceptance probability: a(x′|x) = min(1, π(x′)q(x|x′) / π(x)q(x′|x))
3. Accept with probability a(x′|x); if rejected, state remains at x

### Causal Network Intervention (do-operator)
1. To represent do(Xⱼ = xⱼₖ): delete the factor P(xⱼ|parents(Xⱼ)) from the product
2. New joint: P_ⱼₖ(x₁,…,xₙ) = ∏_{i≠j} P(xᵢ|parents(Xᵢ)) [if xⱼ=xⱼₖ, else 0]
3. Effect on Xᵢ: P(Xᵢ=xᵢ|do(Xⱼ=xⱼₖ)) = ∑_{parents(Xⱼ)} P(xᵢ|xⱼₖ,parents(Xⱼ)) P(parents(Xⱼ))

### Compiling Gibbs Sampling (Earthquake example)
```
r ← a uniform random sample from [0,1]
if Alarm = true then
  if Burglary = true then return [r < 0.0020212]
  else return [r < 0.36755]
else
  if Burglary = true then return [r < 0.0016672]
  else return [r < 0.0014222]
```

## 3. HIERARCHIES/CLASSIFICATIONS

### Three Components of a Bayesian Network
1. Nodes (random variables, discrete or continuous)
2. Directed links (arrows) — DAG, no directed cycles
3. Probability information θ(Xᵢ|Parents(Xᵢ))

### Types of Conditional Distribution Representations
- **Conditional probability table (CPT)**: For discrete variables; 2ᵏ entries for Boolean with k Boolean parents
- **Deterministic nodes**: Value specified exactly (logical or numerical function)
- **Context-specific independence (CSI)**: if-then-else syntax
- **Noisy-OR**: O(k) parameters instead of O(2ᵏ)
- **Linear–Gaussian**: For continuous variables; mean linear in parent
- **Probit**: Φ(x) soft threshold
- **Expit/inverse logit**: 1/(1+e⁻ˣ) soft threshold

### Inference Algorithm Families (Exact)
1. **Enumeration**: O(n2ⁿ) naive, O(2ⁿ) optimized — sums over all variable combinations
2. **Variable elimination**: Dynamic programming; caches intermediate results
3. **Clustering/join tree**: Creates polytree of meganodes; O(n) for all variables

### Inference Algorithm Families (Approximate)
1. **Direct sampling**: Prior-Sample, Rejection sampling, Importance/Likelihood weighting
2. **MCMC**: Gibbs sampling, Metropolis–Hastings
3. **Variational methods**: Mean-field, bounds
4. **Loopy belief propagation**

### Three Families of Continuous Variable Handling
1. Discretization (fixed intervals)
2. Standard PDF families (e.g., Gaussian)
3. Nonparametric representation (collection of instances)

## 4. COMPARISONS/TRADE-OFFS

| Aspect | Causal Ordering | Diagnostic Ordering |
|--------|-----------------|---------------------|
| Network size | More compact (fewer links/parameters) | More links, more parameters |
| Ease of assessment | Easier — numbers correspond to causal knowledge | Harder — tenuous relationships |
| Robustness | Robust to changes in base rates | Fragile |
| Example (burglary) | Figure 13.2: 10 parameters | Figure 13.3(a): 13 params; (b): 31 params |

| Criterion | Enumeration | Variable Elimination | Clustering |
|-----------|-------------|---------------------|------------|
| Time (polytree) | O(2ⁿ) | Linear in network size | O(n) |
| Space | Linear in #variables | Depends on largest factor | Exponential in worst case |
| Single query | OK | Efficient | Less efficient |
| All variables | Inefficient | Inefficient (O(n²)) | Efficient (O(n)) |

| Sampling Method | Acceptance Fraction | Handles Downstream Evidence | Convergence |
|-----------------|---------------------|------------------------------|-------------|
| Rejection sampling | P(e) — vanishingly small for many evidence vars | N/A | 1/√n error |
| Likelihood weighting | Uses all samples | Poor (ignores non-ancestor evidence) | Better than rejection |
| Gibbs sampling | N/A (always accepts) | Good (propagates in all directions) | Can get stuck with deterministic relationships |

| Aspect | HMM (atomic) | DBN (factored) |
|--------|-------------|----------------|
| State representation | Single megavariable | Multiple variables |
| Transition matrix size | O(d²ⁿ) | O(ndᵏ) |
| Expressiveness | Limited | Can model arbitrary distributions |

## 5. FORMULAS & EQUATIONS

**Bayes net joint distribution** (Eq 13.1/13.2):
P(x₁,…,xₙ) = ∏ⁿᵢ₌₁ P(xᵢ|parents(Xᵢ))

**Example calculation** (burglary):
P(j,m,a,¬b,¬e) = P(j|a)P(m|a)P(a|¬b∧¬e)P(¬b)P(¬e) = 0.90×0.70×0.01×0.999×0.998 = 0.00628

**Chain rule comparison**: P(xᵢ|xᵢ₋₁,…,x₁) = P(xᵢ|Parents(Xᵢ)) for Bayes net

**Noisy-OR probability**:
P(xᵢ|parents(Xᵢ)) = 1 − ∏_{j:Xⱼ=true} qⱼ
where qⱼ = P(¬fever|cold,¬flu,¬malaria) for parent j

**Linear–Gaussian for Cost (with subsidy)**:
P(c|h,subsidy) = N(c; aₜh+bₜ, σ²ₜ) = 1/(σₜ√(2π)) e^{−½((c−(aₜh+bₜ))/σₜ)²}

**Probit model**:
P(buys|Cost=c) = 1 − Φ((c−µ)/σ)

**Expit model**:
P(buys|Cost=c) = 1 − 1/(1+exp(−4/√(2π)·(c−µ)/σ))

**Markov blanket distribution** (Eq 13.10):
P(xᵢ|mb(Xᵢ)) = α P(xᵢ|parents(Xᵢ)) ∏_{Yⱼ∈Children(Xᵢ)} P(yⱼ|parents(Yⱼ))

**Detailed balance condition** (Eq 13.12):
π(x)k(x→x′) = π(x′)k(x′→x) for all x, x′

**Stationary distribution equation** (Eq 13.11):
π(x′) = ∑_x π(x)k(x→x′) for all x′

**Gibbs transition kernel** (Eq 13.13):
k(x→x′) = ρ(i) P(x′ᵢ|xᵢ) where states differ only in variable Xᵢ

**MH acceptance probability**:
a(x′|x) = min(1, π(x′)q(x|x′)/π(x)q(x′|x))

**MH ratio trick**:
π(x′)/π(x) = P(x′,e)/P(x,e) — normalizer P(e) cancels

**Adjustment formula** (Eq 13.20):
P(Xᵢ=xᵢ|do(Xⱼ=xⱼₖ)) = ∑_{parents(Xⱼ)} P(xᵢ|xⱼₖ,parents(Xⱼ)) P(parents(Xⱼ))

**Do-operator joint** (Eq 13.19):
P_ⱼₖ(x₁,…,xₙ) = ∏_{i≠j} P(xᵢ|parents(Xᵢ)) [if xⱼ = xⱼₖ, else 0]

## 6. RULES, LAWS & THEOREMS

- **Non-descendants property**: Each variable is conditionally independent of its non-descendants, given its parents
- **Markov blanket property**: A variable is conditionally independent of all other nodes given its parents, children, and children's parents
- **d-separation theorem**: Z d-separates X and Y iff Z blocks all paths between X and Y in the undirected, moralized, ancestral subgraph
- **Noisy-OR assumptions**: (1) All possible causes are listed; (2) Inhibition of each parent is independent of inhibition of any other parent
- **Bayes net construction guarantee**: Because each node connected only to earlier nodes, the network is acyclic; no redundant probability values → no chance for inconsistency
- **Bayes net inference NP-hard**: Can encode 3-SAT as Bayes net; P(S=true) > 0 iff satisfiable; #P-hard for counting satisfying assignments
- **Polytree efficiency**: Exact inference in polytrees is linear in network size
- **Gibbs convergence**: Stationary distribution of Gibbs sampling = posterior distribution of nonevidence variables given evidence (proved via detailed balance with P(x|e))
- **MH convergence guarantee**: MH converges to correct stationary distribution for any proposal distribution, provided transition kernel is ergodic
- **Gibbs is special case of MH**: With acceptance probability 1
- **Causal stability**: Structural equations remain invariant to measurements and local changes
- **Back-door criterion**: To find effect of do(Xⱼ=xⱼₖ) on Xᵢ, condition on any set Z such that Xᵢ is conditionally independent of Parents(Xⱼ) given Xⱼ and Z

## 7. DATA STRUCTURES & TYPES

- **Bayesian network**: DAG + CPTs (or other local distributions)
- **Factor**: Matrix indexed by values of argument variables; used in variable elimination
- **CPT**: Size O(2ᵏ) for Boolean variable with k Boolean parents; each row sums to 1
- **Meganode**: Takes on all combinations of values of constituent nodes (e.g., Sprinkler+Rain with 4 values)
- **Cumulative distribution**: Used for sampling from any distribution given uniform random numbers
- **Algebraic decision diagrams**: Compressed representation of factors (alternative to tables)

## 8. VISUAL PATTERNS

- **Figure 13.1**: Simple Bayes net: Weather independent; Toothache ⟂ Catch | Cavity
- **Figure 13.2**: Full burglary network with CPTs (Burglary, Earthquake, Alarm, JohnCalls, MaryCalls)
- **Figure 13.3**: Effect of node ordering on network complexity: (a) M,J,A,B,E = 13 params; (b) M,J,E,B,A = 31 params (same as full joint)
- **Figure 13.4**: (a) Non-descendants property; (b) Markov blanket
- **Figure 13.5**: Noisy-OR CPT for Fever given Cold, Flu, Malaria
- **Figure 13.6**: Hybrid network: Harvest (continuous), Subsidy (discrete), Cost (continuous), Buys (discrete)
- **Figure 13.7**: Linear-Gaussian cost distributions
- **Figure 13.8**: Probit vs. expit models for P(buys|Cost)
- **Figure 13.9**: Full car insurance network (27+ nodes)
- **Figure 13.10**: Expression tree for P(b|j,m) showing shared subexpressions
- **Figure 13.11**: ENUMERATION-ASK pseudocode
- **Figure 13.12**: Pointwise multiplication example f(X,Y)×g(Y,Z)=h(X,Y,Z)
- **Figure 13.13**: ELIMINATION-ASK pseudocode
- **Figure 13.14**: 3-SAT encoding as Bayes net
- **Figure 13.15**: Multiply connected network (Cloudy → Sprinkler, Rain → WetGrass) and clustered version
- **Figure 13.16**: PRIOR-SAMPLE pseudocode
- **Figure 13.17**: REJECTION-SAMPLING pseudocode
- **Figure 13.18**: LIKELIHOOD-WEIGHTING pseudocode
- **Figure 13.19**: Error comparison: rejection sampling vs. likelihood weighting on insurance network
- **Figure 13.20**: GIBBS-ASK pseudocode
- **Figure 13.21**: Markov chain for Gibbs sampling on sprinkler network
- **Figure 13.22**: Performance: Gibbs vs. likelihood weighting
- **Figure 13.23**: Causal network (a) and mutilated network after do(Sprinkler=true) (b)

## 9. EDGE CASES/EXCEPTIONS/TRAPS

- **Deterministic relationships break Gibbs ergodicity**: If Rain is deterministically equal to Cloudy, Gibbs can never transition between [true,true] and [false,false]; posterior never converges
- **Nearly deterministic → arbitrarily slow mixing**: Gibbs convergence can be arbitrarily slow
- **Rejection sampling with continuous evidence**: Probability of producing a sample consistent with continuous evidence is zero (or infinitesimal)
- **Rejection sampling exponential rejection**: Fraction accepted = P(e), drops exponentially with number of evidence variables
- **Likelihood weighting fails with downstream evidence**: Variables sampled without evidence influence → samples are "hallucinations"
- **Zero-probability in CPTs**: Breaks ergodicity condition for Gibbs (requires all probabilities > 0)
- **Weighted model counting with underflow**: Probabilities become extremely small
- **Inconsistency impossible in Bayes nets**: No redundant probability values → knowledge engineer cannot create a Bayes net violating probability axioms

## 10. EMPIRICAL EVIDENCE/KEY RESULTS

- **CPCS network** (Pradhan et al., 1994): 448 nodes, 906 links; 8,254 parameters instead of 133,931,430 using noisy-OR/Max (a factor of >16,000 savings)
- **Insurance network enumeration**: ~227 million arithmetic operations for typical query
- **Variable elimination vs. enumeration**: ~1000× faster on insurance network
- **Rejection sampling on insurance**: Only 1 in 1,000 to 1 in 10,000 samples accepted
- **Gibbs sampling vs. likelihood weighting**: Gibbs outperforms when evidence is downstream; likelihood weighting better when evidence is upstream
- **Compiled Gibbs sampling**: 2–3 orders of magnitude faster than interpreted version; tens of millions of samples/second on laptop

## 11. CROSS-CHAPTER DEPENDENCIES

- Chapter 12: Basic probability theory, independence, conditional independence, Bayes' rule
- Chapter 15: Extends Bayes nets to more expressive formal languages (first-order logic, programming languages)
- Chapter 14: Dynamic Bayesian networks (temporal reasoning)
- Chapter 16: Influence diagrams, decision theory
- Chapter 19: Nonparametric representations
- Chapter 20: Learning Bayes net models from data
- Chapter 6: CSPs and tree width (connection to Bayes net complexity)
- Chapter 7: SAT solving, DPLL algorithm (connection to WMC)
- Chapter 8: Universal quantification (for implicit definition of temporal models)
- Chapter 4: Simulated annealing (connection to MCMC)
- Chapter 9: Compilation of logic programs (analogy to compiling Bayes nets)

## 12. DATES & PEOPLE

- **Judea Pearl**: Developed message-passing for trees (1982a) and polytrees (Kim & Pearl, 1983); introduced Bayesian networks term (1985); clustering algorithm (1986); *Probabilistic Reasoning in Intelligent Systems* (1988); causal networks theory (2000); *The Book of Why* (2018)
- **Sewall Wright** (1921, 1934): First use of networks for probabilistic analysis of genetic inheritance
- **I. J. Good** (1961): Forerunner of Bayesian networks; original source for noisy-OR model; chief statistician for Turing's code-breaking team
- **Kim** (1983): CONVINCE — first expert system using Bayesian networks
- **Peter Cheeseman** (1985, 1988): "In Defense of Probability" — helped turn tables toward probabilistic AI
- **Eugene Charniak** (1991): "Bayesian networks without tears"
- **Ross Shachter** (1986): Complete inference algorithm using goal-directed reduction; "Bayes-ball" algorithm (1998)
- **David Spiegelhalter and Steffen Lauritzen** (1988): Conversion to Markov network; HUGIN system
- **Cooper** (1990): First NP-hardness result for Bayes net inference
- **Roth** (1996): #P-hardness through counting satisfying assignments
- **Metropolis et al.** (1953): Original MCMC algorithm
- **Hastings** (1970): Introduced accept/reject step (Metropolis–Hastings)
- **Geman and Geman** (1984): Gibbs sampler for undirected Markov networks
- **Pearl** (1987): Application of Gibbs sampling to Bayesian networks
- **Max Henrion** (1988): Logic sampling (rejection sampling for Bayes nets)
- **Fung and Chang** (1989): Evidence weighting (importance sampling)
- **Lauritzen and Wermuth** (1989): Hybrid discrete-continuous networks
- **Berkson** (1944): Expit/inverse logit model
- **Gaddum** (1933) and **Bliss** (1934): Probit distribution
- **Finney** (1947): Expanded probit work
- **Boutilier et al.** (1996): Context-specific independence
- **Roweis and Ghahramani** (1999): Linear–Gaussian model connections
- **Lerner** (2002): Hybrid Bayes nets
- **Zhang and Poole** (1994): Variable elimination algorithm
- **Dechter** (1999): Connection to nonserial dynamic programming
- **Darwiche** (2001): Recursive conditioning
- **Sang et al.** (2005): Weighted model counting
- **Chavira and Darwiche** (2008): WMC with DPLL-style SAT solver
- **Shimony** (1994): MPE is NP-complete
- **Park and Darwiche** (2004): MAP is NPPP-complete
- **Dagum and Luby** (1993, 1997): NP-hardness of approximate inference; bounded probability → polynomial time
- **Gilks et al.** (1996): MCMC theory and applications
- **Brooks et al.** (2011): Handbook of MCMC
- **Carpenter et al.** (2017): STAN (Hamiltonian Monte Carlo)
- **Saul et al.** (1996): Variational methods for Bayes nets
- **Jaakkola and Jordan** (1996): Upper and lower bounds
- **Wainwright and Jordan** (2008): Unifying variational methods theory
- **McEliece et al.** (1998): Connection between loopy BP and turbo decoding
- **Berrou et al.** (1993): Turbo decoding
- **Weiss** (2000), **Yedidia et al.** (2005): Convergence proofs for loopy BP
- **Rubin** (1974), **Robins** (1986): Causal inference foundations
- **Peters et al.** (2017): Learning causal models
- **Shortliffe** (1976): MYCIN — certainty factors
- **Dempster** (1968): Dempster-Shafer theory
- **Zadeh** (1965): Fuzzy sets; (1978): Possibility theory
- **Wellman** (1990a): Qualitative probabilistic networks
- **Andersen et al.** (1989): MUNIN system for neuromuscular disorders
- **Heckerman** (1991): PATHFINDER system for pathology
- **Horvitz et al.** (1998): Office Assistant in Microsoft Office
- **Breese and Heckerman** (1996): Printer Wizard in Windows
- **Pourret et al.** (2008): 400-page guide to Bayes net applications

## 13. PROOF & ARGUMENT PATTERNS

- **NP-hardness of Bayes net inference**: Reduce 3-SAT to Bayes net; root variables with P=0.5, clause nodes as deterministic disjunctions, S as conjunction; P(S=true) > 0 iff satisfiable. This also shows #P-hardness (counting satisfying assignments = P(S=true)/2⁻ⁿ)
- **Gibbs sampling convergence proof**: Show detailed balance with stationary distribution = P(x|e). For states differing in one variable Xᵢ: P(x|e)ρ(i)P(x′ᵢ|xᵢ,e) = P(x′|e)ρ(i)P(xᵢ|x′ᵢ,e) using chain rule
- **Metropolis–Hastings proof**: Show detailed balance holds for any proposal distribution: π(x)q(x′|x)a(x′|x) = π(x′)q(x|x′)a(x|x′) by definition of acceptance probability
- **Bayes net consistency proof**: Parameters θ(xᵢ|parents(Xᵢ)) are exactly the conditional probabilities P(xᵢ|parents(Xᵢ)) implied by the joint distribution (Exercise 13.CPTE)
- **Detailed balance implies stationarity**: Summing over x in detailed balance equation yields π(x′) = ∑_x π(x)k(x→x′)

## 14. DESIGN PARADIGMS/META-METHODS

- **Dynamic programming**: Variable elimination eliminates repeated subexpression evaluation
- **Causal modeling**: Direct causes as parents → more compact, robust, and natural networks
- **Divide and conquer through conditional independence**: Locally structured systems grow linearly, not exponentially
- **Reduction**: Reduce one problem to another (3-SAT → Bayes net inference)
- **Importance sampling trick**: Sample from easy distribution Q, weight by P/Q
- **Compilation**: Precompute model-specific code for repeated inference operations
- **Rao-Blackwellization**: Exact inference for a subset is always more accurate than sampling
- **Completing the square**: Algebraic trick for Gaussian integrals
- **Causal do-calculus**: Represent interventions by deleting incoming links to intervened variable

## 15. CASE STUDIES/CLASSIC EXAMPLES

- **Burglary/Earthquake/Alarm**: P(b|j,m) = α × 0.00059224 → 28.4% chance of burglary given both neighbors call
- **Mary's sprinkler/lawn**: Cloudy → Sprinkler, Rain → WetGrass; Gibbs sampling example: P(Rain|Sprinkler=true,WetGrass=true)
- **Car insurance network** (Figure 13.9): 27+ nodes; input variables (Age, YearsLicensed, etc.), hidden variables (SocioEcon, RiskAversion, DrivingBehavior), output cost variables (MedicalCost, LiabilityCost, PropertyCost)
- **Fever/Noisy-OR**: Cold, Flu, Malaria as causes with inhibition probabilities 0.6, 0.2, 0.1
- **3-SAT encoding as Bayes net**: (W∨X∨Y) ∧ (¬W∨Y∨Z) ∧ (X∨Y∨¬Z) with 4 root variables, 3 clause nodes, 1 conjunction node
- **MYCIN**: Medical expert system for bacterial infections using certainty factors
- **CPCS network**: 448 nodes, 906 links for internal medicine; 8,254 params vs. 133,931,430
- **MUNIN**: Diagnosing neuromuscular disorders
- **PATHFINDER**: Pathology
- **Microsoft Printer Wizard and Office Assistant**: Most widely used Bayes net systems

## 16. ETHICS
- Hidden variables in insurance networks must not inadvertently become proxies for variables such as race (footnote p. 439)
- Book by Pearl and McKenzie (2018): *The Book of Why* discusses broader implications

## 17. END-OF-CHAPTER MATERIAL

**Summary points** (8 bullet points):
1. Bayesian network = DAG + conditional distributions
2. Concise representation of conditional independence
3. Specifies joint distribution; often exponentially smaller than explicit table
4. Canonical families for compact representation; hybrid discrete-continuous
5. Inference = computing posterior given evidence; variable elimination for exact inference
6. Polytrees: linear time; general case: intractable
7. Likelihood weighting and MCMC for approximate inference
8. Causal networks capture causal relationships and predict intervention effects

---

# CHAPTER 14: PROBABILISTIC REASONING OVER TIME

## 1. NAMED ENTITIES (Terms/Concepts/Definitions)

- **Discrete-time model**: World viewed as a series of snapshots or time slices at intervals ∆
- **Time slice**: A set of random variables at a single time point
- **State variables (Xₜ)**: Unobservable variables representing the state at time t
- **Evidence variables (Eₜ)**: Observable variables at time t
- **Notation a:b**: Sequence of integers from a to b inclusive (e.g., U₁:₃)
- **Markov assumption**: Current state depends only on a finite fixed number of previous states
- **Markov process/Markov chain**: A stochastic process satisfying the Markov assumption
- **First-order Markov process**: P(Xₜ|X₀:ₜ₋₁) = P(Xₜ|Xₜ₋₁)
- **Second-order Markov process**: P(Xₜ|Xₜ₋₂,Xₜ₋₁)
- **Time-homogeneous process**: Laws governing change do not themselves change over time
- **Sensor Markov assumption**: P(Eₜ|X₀:ₜ,E₁:ₜ₋₁) = P(Eₜ|Xₜ)
- **Sensor model (observation model)**: P(Eₜ|Xₜ)
- **Transition model**: P(Xₜ|Xₜ₋₁)
- **Filtering (state estimation)**: Computing P(Xₜ|e₁:ₜ) — posterior over most recent state given all evidence to date
- **Belief state**: The posterior distribution over current state
- **Prediction**: Computing P(Xₜ₊ₖ|e₁:ₜ) for k > 0
- **Smoothing**: Computing P(Xₖ|e₁:ₜ) for 0 ≤ k < t
- **Most likely explanation**: argmax_{x₁:ₜ} P(x₁:ₜ|e₁:ₜ)
- **Learning**: Estimating transition and sensor models from observations
- **Recursive estimation**: P(Xₜ₊₁|e₁:ₜ₊₁) = f(eₜ₊₁, P(Xₜ|e₁:ₜ))
- **Forward message (f₁:ₜ)**: The filtered estimate P(Xₜ|e₁:ₜ)
- **Backward message (bₖ₊₁:ₜ)**: P(eₖ₊₁:ₜ|Xₖ)
- **Forward–backward algorithm**: Computes smoothed estimates for entire sequence in O(t)
- **Fixed-lag smoothing**: Computing P(Xₜ₋d|e₁:ₜ) for fixed d
- **Viterbi algorithm**: Finds most likely sequence of states given observations; time linear in t, space linear in t
- **Mixing time**: Time taken to reach the fixed point (stationary distribution)
- **Stationary distribution**: The fixed point a Markov process converges to
- **Hidden Markov model (HMM)**: Temporal model where state is a single, discrete random variable
- **Observation matrix (Oₜ)**: S×S diagonal matrix where ith diagonal entry = P(eₜ|Xₜ=i)
- **Transition matrix (T)**: S×S matrix where Tᵢⱼ = P(Xₜ=j|Xₜ₋₁=i)
- **Transformation operator (B)**: Product of T and O matrices; transforms later backward message into earlier one
- **Kalman filter**: Algorithm for filtering with continuous variables and linear-Gaussian models
- **Kalman gain matrix (Kₜ₊₁)**: Measure of how seriously to take new observation relative to prediction
- **Extended Kalman filter (EKF)**: Handles nonlinearities by locally linearizing around current mean
- **Switching Kalman filter**: Multiple Kalman filters in parallel with different models
- **Dynamic Bayesian network (DBN)**: Extends Bayes net semantics to handle temporal probability models
- **Unrolling**: Replicating DBN slices until large enough to accommodate observations
- **Gaussian error model**: Probability of sensor error drops off in appropriate way (continuous or discrete)
- **Transient failure**: Sensor occasionally sends nonsense
- **Transient failure model**: Sensor model allowing some probability of returning a completely incorrect value
- **Persistent failure model**: Sensor model with an additional state variable for sensor status
- **Persistence arc**: CPT giving small probability of failure each time step, sensor stays broken once broken
- **Sequential importance sampling (SIS)**: Running all N samples together through DBN, one slice at a time
- **Particle filtering**: Population of N samples propagated forward, weighted by likelihood, resampled
- **Evidence reversal**: Sampling state conditioned on both previous state and current evidence
- **Rao-Blackwellization**: Exact inference for a subset of variables is always more accurate than sampling
- **Rao-Blackwellized particle filter**: Particle filtering on location + exact HMM inference for each square conditioned on location
- **Simultaneous localization and mapping (SLAM)**: Building a map while tracking location
- **Assumed-density filter**: Assumes posterior belongs to a finitely parameterized family; projects back if update takes it outside
- **Factored frontier algorithm**: Assumes posterior can be approximated by product of small factors
- **Particle MCMC**: Combines MCMC on unrolled DBN with particle filtering for proposals
- **Decayed MCMC**: Samples recent state variables with higher probability
- **Sequential Monte Carlo (SMC)**: Family of algorithms including particle filtering
- **Condensation**: Name for particle filtering in computer vision (Isard and Blake, 1996)
- **Survival of the fittest**: Name for particle filtering in AI (Kanazawa et al., 1995)

## 2. SEQUENTIAL PROCESSES (Algorithms/Procedures)

### Filtering (Recursive Estimation) — Equation (14.5)
1. **Predict**: P(Xₜ₊₁|e₁:ₜ) = ∑_{xₜ} P(Xₜ₊₁|xₜ) P(xₜ|e₁:ₜ)
2. **Update**: P(Xₜ₊₁|e₁:ₜ₊₁) = α P(eₜ₊₁|Xₜ₊₁) P(Xₜ₊₁|e₁:ₜ)

### Forward-Backward Algorithm for Smoothing
```
function FORWARD-BACKWARD(ev, prior) returns a vector of probability distributions
  fv[0] ← prior
  for i = 1 to t do
    fv[i] ← FORWARD(fv[i-1], ev[i])
  for i = t down to 1 do
    sv[i] ← NORMALIZE(fv[i] × b)
    b ← BACKWARD(b, ev[i])
  return sv
```
- Time complexity: O(t)
- Space: O(|f|t) where |f| is size of forward message representation

### Backward Recursion — Equation (14.9)
P(eₖ₊₁:ₜ|Xₖ) = ∑_{xₖ₊₁} P(eₖ₊₁|xₖ₊₁) P(eₖ₊₂:ₜ|xₖ₊₁) P(xₖ₊₁|Xₖ)

### Viterbi Algorithm (Most Likely Sequence)
```
m₁:ₜ₊₁ = P(eₜ₊₁|Xₜ₊₁) max_{xₜ} P(Xₜ₊₁|xₜ) max_{x₁:ₜ₋₁} P(x₁:ₜ₋₁,xₜ,e₁:ₜ)
        = P(eₜ₊₁|Xₜ₊₁) max_{xₜ} P(Xₜ₊₁|xₜ) m₁:ₜ(xₜ)
```
- Space required: O(t) (must keep pointers for each state at each time step)
- Numerical underflow solutions: (1) Normalize m at each step; (2) Use log probabilities

### HMM Matrix Algorithms

**Forward equation**: f₁:ₜ₊₁ = α Oₜ₊₁ Tᵀ f₁:ₜ
**Backward equation**: bₖ₊₁:ₜ = T Oₖ₊₁ bₖ₊₂:ₜ
- Complexity: O(S²t) for forward-backward

### Fixed-Lag Smoothing Algorithm (Figure 14.6)
```
function FIXED-LAG-SMOOTHING(eₜ, hmm, d) returns a distribution over Xₜ₋d
  persistent: t, f, B, eₜ₋d:ₜ
  add eₜ to end of eₜ₋d:ₜ
  Oₜ ← diagonal matrix containing P(eₜ|Xₜ)
  if t > d then
    f ← FORWARD(f, eₜ₋d)
    remove eₜ₋d₋₁ from beginning of eₜ₋d:ₜ
    Oₜ₋d ← diagonal matrix containing P(eₜ₋d|Xₜ₋d)
    B ← Oₜ₋d⁻¹ T⁻¹ B T Oₜ
  else B ← B T Oₜ
  t ← t+1
  if t > d+1 then return NORMALIZE(f × B1) else return null
```

### Kalman Filter Update (1D) — Equations (14.20)
µₜ₊₁ = ((σ²ₜ + σ²ₓ)zₜ₊₁ + σ²_z µₜ) / (σ²ₜ + σ²ₓ + σ²_z)
σ²ₜ₊₁ = (σ²ₜ + σ²ₓ)σ²_z / (σ²ₜ + σ²ₓ + σ²_z)

### Kalman Filter Update (General Multivariate) — Equations (14.22)
µₜ₊₁ = F µₜ + Kₜ₊₁(zₜ₊₁ − H F µₜ)
Σₜ₊₁ = (I − Kₜ₊₁H)(F Σₜ Fᵀ + Σₓ)
where Kₜ₊₁ = (F Σₜ Fᵀ + Σₓ) Hᵀ (H(F Σₜ Fᵀ + Σₓ)Hᵀ + Σ_z)⁻¹

### Particle Filtering Algorithm (Figure 14.17)
```
function PARTICLE-FILTERING(e, N, dbn) returns a set of samples
  persistent: S, a vector of N samples, initially generated from P(X₀)
  for i = 1 to N do
    S[i] ← sample from P(X₁|X₀=S[i])              // step 1: propagate
    W[i] ← P(e|X₁=S[i])                             // step 2: weight
  S ← WEIGHTED-SAMPLE-WITH-REPLACEMENT(N, S, W)   // step 3: resample
  return S
```
Three steps per update cycle:
1. **Propagate**: Each sample is propagated forward by sampling next state from transition model given current state
2. **Weight**: Each sample weighted by likelihood of new evidence: P(eₜ₊₁|xₜ₊₁)
3. **Resample**: New population selected from current population with probability proportional to weight; new samples are unweighted

### Kalman Filter Update Cycle (1D Concrete Example)
Given: prior P(x₀) = N(µ₀, σ²₀), transition P(xₜ₊₁|xₜ) = N(xₜ₊₁; xₜ, σ²ₓ), sensor P(zₜ|xₜ) = N(zₜ; xₜ, σ²_z)

**Predict**: P(x₁) = N(x₁; µ₀, σ²₀ + σ²ₓ)
**Update**: P(x₁|z₁) = N(⟨(σ²₀+σ²ₓ)z₁+σ²_zµ₀⟩/(σ²₀+σ²ₓ+σ²_z), (σ²₀+σ²ₓ)σ²_z/(σ²₀+σ²ₓ+σ²_z))

### Smoothing (Rauch–Tung–Striebel) for Kalman Filter
- Produces much smoother trajectory than filtering
- Variance sharply reduced except at ends of trajectory

## 3. HIERARCHIES/CLASSIFICATIONS

### Four Inference Tasks in Temporal Models
1. **Filtering (state estimation)**: P(Xₜ|e₁:ₜ)
2. **Prediction**: P(Xₜ₊ₖ|e₁:ₜ) for k > 0
3. **Smoothing**: P(Xₖ|e₁:ₜ) for k < t
4. **Most likely explanation**: argmax P(x₁:ₜ|e₁:ₜ)

### Three Temporal Model Families
1. **Hidden Markov Models (HMM)**: Single discrete state variable; matrix algorithms
2. **Kalman Filters**: Continuous variables; linear-Gaussian; closed-form updates
3. **Dynamic Bayesian Networks (DBN)**: Multiple state variables; generalizes both HMM and Kalman filter

### Ways to Improve Markov Assumption Accuracy
1. Increase order of Markov process (e.g., first-order → second-order)
2. Increase set of state variables (add Season, Temperature, Humidity, Pressure, etc.)

### Sensor Failure Models (hierarchy of sophistication)
1. **Simple Gaussian error model**: Assumes errors follow Gaussian distribution around true value
2. **Transient failure model**: Allows small probability of sensor returning arbitrary wrong value
3. **Persistent failure model**: Adds sensor status variable (BMBroken) with persistence arc

## 4. COMPARISONS/TRADE-OFFS

| Aspect | Filtering | Smoothing |
|--------|-----------|-----------|
| What | P(Xₜ|e₁:ₜ) | P(Xₖ|e₁:ₜ) for k < t |
| When used | Online (real-time tracking) | Offline (retrospective analysis) |
| Accuracy | Lower (only past evidence) | Higher (past + future evidence) |
| Variance | Higher | Lower (except at ends) |

| Aspect | HMM | DBN |
|--------|-----|-----|
| State variables | Single megavariable | Multiple variables |
| Transition matrix | O(d²ⁿ) entries | O(ndᵏ) entries (linear vs. exponential) |
| Per-update cost (exact) | O(d²ⁿ) | O(ndⁿ⁺ᵏ) |
| Expressiveness | Limited (atomic states) | Can model arbitrary distributions |
| Example (vacuum 42 squares) | 5×10²⁹ entries | Few thousand parameters |

| Sensor Model | Transient Blip Handling | Persistent Failure Handling |
|--------------|------------------------|----------------------------|
| Simple Gaussian | Catastrophic belief change | Catastrophic belief change |
| Transient failure model | Good (inertia maintains belief) | Gradual convergence to wrong belief |
| Persistent failure model | Good (rise then drop of P(broken)) | Correct (P(broken) → 1, gradual discharge) |

## 5. FORMULAS & EQUATIONS

**First-order Markov assumption** (Eq 14.1):
P(Xₜ|X₀:ₜ₋₁) = P(Xₜ|Xₜ₋₁)

**Sensor Markov assumption** (Eq 14.2):
P(Eₜ|X₀:ₜ, E₁:ₜ₋₁) = P(Eₜ|Xₜ)

**Complete joint distribution for temporal model** (Eq 14.3):
P(X₀:ₜ, E₁:ₜ) = P(X₀) ∏ᵗᵢ₌₁ P(Xᵢ|Xᵢ₋₁) P(Eᵢ|Xᵢ)

**Filtering recursion** (Eq 14.5):
P(Xₜ₊₁|e₁:ₜ₊₁) = α P(eₜ₊₁|Xₜ₊₁) ∑_{xₜ} P(Xₜ₊₁|xₜ) P(xₜ|e₁:ₜ)

**Prediction recursion** (Eq 14.6):
P(Xₜ₊ₖ₊₁|e₁:ₜ) = ∑_{xₜ₊ₖ} P(Xₜ₊ₖ₊₁|xₜ₊ₖ) P(xₜ₊ₖ|e₁:ₜ)

**Smoothing decomposition** (Eq 14.8):
P(Xₖ|e₁:ₜ) = α P(Xₖ|e₁:ₖ) P(eₖ₊₁:ₜ|Xₖ) = α f₁:ₖ × bₖ₊₁:ₜ

**Backward recursion** (Eq 14.9):
P(eₖ₊₁:ₜ|Xₖ) = ∑_{xₖ₊₁} P(eₖ₊₁|xₖ₊₁) P(eₖ₊₂:ₜ|xₖ₊₁) P(xₖ₊₁|Xₖ)

**Viterbi recursion** (Eq 14.11):
m₁:ₜ₊₁ = P(eₜ₊₁|Xₜ₊₁) max_{xₜ} P(Xₜ₊₁|xₜ) m₁:ₜ(xₜ)

**HMM forward matrix equation** (Eq 14.12):
f₁:ₜ₊₁ = α Oₜ₊₁ Tᵀ f₁:ₜ

**HMM backward matrix equation** (Eq 14.13):
bₖ₊₁:ₜ = T Oₖ₊₁ bₖ₊₂:ₜ

**Transformation operator** (Eq 14.14–14.16):
bₜ₋d₊₁:ₜ = (∏ᵗᵢ₌ₜ₋d₊₁ T Oᵢ) 1 = Bₜ₋d₊₁:ₜ 1
Bₜ₋d₊₂:ₜ₊₁ = Oₜ₋d₊₁⁻¹ T⁻¹ Bₜ₋d₊₁:ₜ T Oₜ₊₁

**HMM transition model for localization**:
P(Xₜ₊₁=j|Xₜ=i) = { 1/N(i) if j∈NEIGHBORS(i); 0 otherwise }

**HMM sensor model for localization**:
P(Eₜ=eₜ|Xₜ=i) = (Oₜ)ᵢᵢ = (1−ε)⁴⁻ᵈⁱᵗ εᵈⁱᵗ
where dᵢₜ = discrepancy (number of bits different between true value and reading)

**Kalman filter general model** (Eq 14.21):
P(xₜ₊₁|xₜ) = N(xₜ₊₁; Fxₜ, Σₓ)
P(zₜ|xₜ) = N(zₜ; Hxₜ, Σ_z)

**Multivariate Gaussian**:
N(x; µ, Σ) = α e^{−½ (x−µ)ᵀ Σ⁻¹ (x−µ)}

**Likelihood recursion**:
ℓ₁:ₜ₊₁ = FORWARD(ℓ₁:ₜ, eₜ₊₁)
L₁:ₜ = P(e₁:ₜ) = ∑_{xₜ} ℓ₁:ₜ(xₜ)

**Particle filtering consistency proof**:
N(xₜ₊₁|e₁:ₜ₊₁)/N = α P(eₜ₊₁|xₜ₊₁) ∑_{xₜ} P(xₜ₊₁|xₜ) P(xₜ|e₁:ₜ) = P(xₜ₊₁|e₁:ₜ₊₁)

## 6. RULES, LAWS & THEOREMS

- **Markov property**: Current state depends only on finite fixed number of previous states
- **Time-homogeneous**: Laws governing change do not change over time
- **Sensor Markov property**: Evidence depends only on current state
- **Kalman filter closure**: Linear-Gaussian family remains closed under Bayesian updating (predict + update both yield Gaussians)
- **Kalman filter variance independence**: Variance update Σₜ₊₁ is independent of observations (can be precomputed)
- **Filtering constant time**: For finite agent, time and space for each filter update must be constant (independent of t)
- **Particle filtering consistency**: As N → ∞, particle filtering gives correct posterior
- **Viterbi linear time**: Most likely sequence found in O(t) using dynamic programming (max replaces sum)
- **DBN exact filtering exponential**: Per-update cost is O(ndⁿ⁺ᵏ) — exponential in number of state variables
- **SIS exponential sample requirement**: Fraction of samples with non-negligible weight drops exponentially with t

## 7. DATA STRUCTURES & TYPES

- **Transition matrix T**: S×S matrix for HMM; Tᵢⱼ = P(Xₜ=j|Xₜ₋₁=i)
- **Observation matrix Oₜ**: S×S diagonal matrix; (Oₜ)ᵢᵢ = P(eₜ|Xₜ=i)
- **Forward message f₁:ₜ**: Vector of size S (for HMM)
- **Backward message bₖ₊₁:ₜ**: Vector of size S
- **B matrix**: Product of T and O matrices for fixed-lag smoothing
- **Kalman gain Kₜ₊₁**: Matrix for blending prediction and observation
- **Particle set**: N samples, each being an assignment to all state variables
- **Unrolled DBN**: Bayesian network replicated over time slices

## 8. VISUAL PATTERNS

- **Figure 14.1**: (a) First-order Markov process; (b) Second-order Markov process
- **Figure 14.2**: Umbrella DBN with transition and sensor CPTs (P(Rₜ|Rₜ₋₁) = ⟨0.7,0.3; 0.3,0.7⟩; P(Uₜ|Rₜ) = ⟨0.9,0.2⟩)
- **Figure 14.3**: Smoothing computation illustrated as forward-backward on timeline
- **Figure 14.4**: FORWARD-BACKWARD algorithm pseudocode
- **Figure 14.5**: Viterbi algorithm: (a) state sequences as paths through graph; (b) operation on umbrella sequence [true,true,false,true,true]
- **Figure 14.6**: FIXED-LAG-SMOOTHING algorithm pseudocode
- **Figure 14.7**: HMM localization posteriors: (a) after one observation; (b) after two observations (disk sizes = probabilities)
- **Figure 14.8**: Localization error and Viterbi path error for various ε values
- **Figure 14.9**: Kalman filter network structure (position Xₜ, velocity Ẋₜ, position measurement Zₜ)
- **Figure 14.10**: Kalman filter update cycle: P(x₀), P(x₁), P(x₁|z₁=2.5) for random walk
- **Figure 14.11**: Kalman filtering (a) and smoothing (b) for object moving on X–Y plane
- **Figure 14.12**: Bird flying toward tree: (a) Kalman filter Gaussian centered on obstacle; (b) Realistic prediction with evasive action
- **Figure 14.13**: (a) Umbrella DBN prior/transition/sensor specification; (b) Robot motion DBN with Battery, BMeter
- **Figure 14.14**: Expected battery value over time: (a) Gaussian error model; (b) Transient failure model
- **Figure 14.15**: (a) Persistent failure DBN with BMBroken variable; (b) Belief trajectories for transient/permanent failure
- **Figure 14.16**: Unrolling a DBN over 3 time slices
- **Figure 14.17**: PARTICLE-FILTERING pseudocode
- **Figure 14.18**: Particle filtering update cycle for umbrella with N=10
- **Figure 14.19**: Max norm error: SIS (100K samples) vs. Particle Filtering (1K samples)
- **Figure 14.20**: DBN for SLAM with vacuum robot (location + 42 dirt variables + wall/dirt sensors)
- **Figure 14.21**: (a) Standard PF RMS error for different dirt persistence p; (b) Rao-Blackwellized PF performance

## 9. EDGE CASES/EXCEPTIONS/TRAPS

- **Prediction converges to stationary distribution**: Predicting far into future converges to fixed point; mixing time determines useful prediction horizon
- **Likelihood underflow**: Forward message probabilities become numerically smaller and smaller over time, causing floating-point underflow
- **Viterbi numerical underflow**: Probabilities get extremely small for long sequences; solution: normalize or use log probabilities
- **Kalman filter variance independent of observations**: Can precompute entire variance sequence
- **Deterministic dirt breaks particle filtering**: With p=1 (dirt never changes), initial guesses are never updated; probability of correct initial map = 2⁻⁴² ≈ 2×10⁻¹³
- **Particle depletion**: Best particle dominates likelihood; population diversity collapses
- **SIS exponential degradation**: Fraction of samples with non-negligible weight drops exponentially with sequence length
- **Transient failure model fooled by persistent failure**: Gradual belief that battery is empty when sensor actually failed
- **DBN exact inference exponential**: Forward message is generally not factorable; exponential in number of state variables
- **Extended Kalman filter limitations**: Fails when nonlinearity is significant within covariance region around mean
- **Condition for fixed-lag smoothing**: Requires invertible transition matrix and no zeroes in sensor model
- **Gaussian sensor model assigns nonzero probability to negative charge**: Beta distribution sometimes better for restricted-range variables

## 10. EMPIRICAL EVIDENCE/KEY RESULTS

- **Umbrella filtering example**: P(R₀)=⟨0.5,0.5⟩; after U₁=true: ⟨0.818,0.182⟩; after U₂=true: ⟨0.883,0.117⟩
- **Umbrella smoothing**: P(R₁|u₁,u₂) ≈ ⟨0.883,0.117⟩ — higher than filtered estimate (0.818) because rain persists
- **HMM localization error** (Figure 14.8): Even with ε=0.20 (59% wrong readings), robot localizes to within 2 squares after 20 observations; with ε=0.40, robot is lost (too little information)
- **Dirt persistence p and particle filtering**: Lower p (less persistence) → lower error; higher p → worse performance; p=1 → complete failure
- **Rao-Blackwellized PF** (100 particles): Handles deterministic dirt (p=1) with either exact or noisy location sensing
- **Particle filtering vs. SIS** (Figure 14.19): PF with 1,000 samples outperforms SIS with 100,000 samples on grid-world localization
- **Kalman filter 1D example** (Figure 14.10): Prior µ₀=0.0, σ₀=1.5; σₓ=2.0; σ_z=1.0; z₁=2.5 → posterior mean is weighted average of prediction (µ₀) and observation

## 11. CROSS-CHAPTER DEPENDENCIES

- Chapter 4: Belief state maintenance (set-based); belief state from transition + sensor model
- Chapter 7: Logical belief states; handling time with variables for each time point
- Chapter 11: Planning
- Chapter 12: Probability theory basics; normalization; Bayes' rule
- Chapter 13: Bayesian networks (DBNs extend); exact and approximate inference algorithms; d-separation; variable elimination; likelihood weighting; Gibbs sampling; Markov blankets
- Chapter 15: More expressive formal languages for probability models
- Chapter 16: Information value (for selecting tests)
- Chapter 17: Planning in stochastic environments
- Chapter 20: EM algorithm; Bayesian updating; learning from data
- Chapter 26: SLAM in robotics; tracking examples
- Appendix A: Gaussian distributions; multivariate Gaussians; matrix operations; expected value

## 12. DATES & PEOPLE

- **Andrei Markov** (1856–1922): Markov processes/chains
- **Rudolf Kalman** (1960): Kalman filter
- **C. F. Gauss** (1809): Deterministic least-squares for orbit estimation
- **Norbert Wiener** (1942): Continuous-time filtering (WWII classified)
- **Kolmogorov** (1941): Discrete-time filtering
- **Peter Swerling** (1959): Independent discovery of Kalman filter
- **Thorvold Thiele** (1880): Danish astronomer; earlier Kalman filter results
- **Ruslan Stratonovich** (1959): Russian physicist; earlier Kalman filter results
- **Andrew Viterbi** (1967): Viterbi algorithm
- **Baum and Petrie** (1966): HMM forward-backward algorithm
- **Rauch, Tung, Striebel** (1965): Smoothing; Rauch–Tung–Striebel smoother
- **Dempster, Laird, Rubin** (1977): EM algorithm
- **Handschin and Mayne** (1969): First sampling for filtering (sequential Monte Carlo)
- **Zaritskii et al.** (1975): Resampling idea (Russian control journal)
- **Rubin** (1988): Sequential importance sampling with resampling (SIR)
- **Gordon, Salmond, Smith** (1993): Particle filtering (control theory)
- **Kanazawa et al.** (1995): Survival of the fittest (AI); evidence reversal
- **Isard and Blake** (1996): Condensation (computer vision)
- **Doucet** (1997): Reduced approximation error with evidence reversal
- **Liu and Chen** (1998): SIR theory
- **Doucet et al.** (2000): Rao-Blackwellized particle filter
- **Murphy and Russell** (2001): Rao-Blackwellized PF for SLAM
- **Dean and Kanazawa** (1989b): First DBN use in AI
- **Nicholson and Brady** (1992): DBNs
- **Kjaerulff** (1992): Extended HUGIN for DBNs
- **Murphy** (2002): Thorough DBN analysis
- **Boyen, Koller** (1999): Boyen–Koller algorithm
- **Marthi et al.** (2002): Decayed MCMC filter
- **Andrieu et al.** (2010): Particle MCMC
- **Paige et al.** (2015): Particle cascade (parallel without synchronization)
- **Crisan and Doucet** (2002); **Del Moral** (2004): Bounded error for SMC

## 14. DESIGN PARADIGMS/META-METHODS

- **Recursive estimation**: Update belief state from previous belief state + new evidence (constant time per step)
- **Forward-backward message passing**: Smoothing via forward (filtering) and backward recursions
- **Dynamic programming for Viterbi**: max replaces sum; record best predecessors for each state
- **Matrix formulation**: Compact representation for HMM algorithms
- **Completing the square**: Key algebraic trick for Gaussian integrals
- **Rao-Blackwellization**: Exact inference for tractable subset, sampling for the rest
- **Particle filtering with resampling**: Focus samples on high-probability regions; maintain bounded error
- **Unrolling + variable elimination**: Converting temporal inference to static BN inference
- **Causal modeling of sensor failure**: Adding persistent state variables for sensor status

## 15. CASE STUDIES/CLASSIC EXAMPLES

- **Umbrella security guard**: Rainₜ (state), Umbrellaₜ (evidence); P(Rₜ|Rₜ₋₁) = ⟨0.7,0.3; 0.3,0.7⟩; P(Uₜ|Rₜ) = ⟨0.9,0.2⟩
  - Filtering step-by-step from R₀ ⟨0.5,0.5⟩ through 2 days
  - Smoothing: P(R₁|u₁,u₂) = ⟨0.883,0.117⟩ (higher than filtered 0.818)
  - Viterbi on sequence [true,true,false,true,true]
- **Robot localization in maze** (Figure 14.7): 42 empty squares; uniform transition to neighbors; noisy wall sensors with 4-bit NESW readings; sensor error rate ε
- **Kalman filter random walk**: Consumer confidence index; P(x₀) = N(µ₀,σ²₀); transition adds Gaussian noise σ²ₓ; sensor adds Gaussian noise σ²_z; mean result = weighted average of prediction and observation
- **Bird tracking / jungle foliage**: 6 continuous variables (position + velocity); linear-Gaussian fails when bird must avoid tree → switching Kalman filter
- **Battery monitoring robot**: Batteryₜ, BMeterₜ; transient failure → battery meter reads 0 when bumped; persistent failure → add BMBroken state variable
- **Simultaneous localization and mapping (SLAM)**: 42 dirt squares with persistence p; dirt sensor 90% accurate; Rao-Blackwellized PF handles deterministic dirt (p=1)

## 17. END-OF-CHAPTER MATERIAL

**Summary points** (7 bullet points):
1. Changing state handled by random variables at each time point
2. Markov property + time-homogeneous assumption simplifies representation
3. Temporal model = transition model + sensor model
4. Four inference tasks: filtering, prediction, smoothing, most likely explanation
5. All achievable with linear-time recursive algorithms
6. Three families: HMMs, Kalman filters, DBNs
7. Particle filtering is effective family of approximation algorithms

**Bibliographical notes**: Rich history from Gauss (1809) through modern particle filter variants
</task_result>
</task>

---

# Comprehensive Extraction: AIMA Chapters 15–18

---

# CHAPTER 15: PROBABILISTIC PROGRAMMING

## 1. Named Entities

### Core Concepts
- **Probabilistic Programming Language (PPL)**: A language that defines probability distributions over execution traces by incorporating stochastic elements (random choices) into traditional programming languages. Two routes: declarative PPLs (logic-based) and general PPLs (programming-language-based).
- **Relational Probability Model (RPM)**: A probability model using database semantics (unique names assumption + domain closure) over first-order possible worlds. The set of objects is exactly the set of constant symbols used.
- **Open Universe Probability Model (OUPM)**: A probability model built on full first-order logic semantics, allowing existence uncertainty and identity uncertainty. Objects can be added/removed during world generation.
- **Generative Program**: An executable program in which every random choice defines a random variable. Probability distribution over execution traces.
- **Execution Trace (ω)**: A sequence of possible values for all random choices made during program execution. The sample space of the probability model.
- **Basic Random Variable**: In RPMs, obtained by instantiating each function with each possible combination of objects.
- **Type Signature**: Specification of the type of each argument and the function's value.
- **Database Semantics**: Unique names assumption + domain closure (no more objects beyond those named). From Section 8.2.8.
- **Relational Uncertainty**: Uncertainty about the value of a relation that affects the dependency structure (e.g., unknown author of a book).
- **Identity Uncertainty**: Uncertainty about which logical terms refer to the same object.
- **Existence Uncertainty**: Uncertainty about what objects exist.
- **Sybil / Sybil Attack**: Multiple login IDs used by a dishonest customer to confound a reputation system. Named after a famous case of multiple personality disorder.
- **Number Statement**: In OUPMs, specifies conditional distributions over the numbers of objects of various kinds.
- **Origin Function**: A function that says where each object generated by a number statement came from.
- **Number Variable**: In OUPMs, specifies how many objects there are of each type with each possible origin in each possible world.
- **Generation History**: Each object in OUPM is a generation history (e.g., "the fourth login ID of the seventh customer"), ensuring every world can be constructed by exactly one generation sequence.
- **Guaranteed Object**: An object guaranteed to exist and be distinct (used in RPM-style sub-models within OUPMs).
- **Grounding / Unrolling**: Constructing the equivalent Bayesian network from an RPM by instantiating all dependencies for all known constants.
- **Lifted Inference**: Avoiding grounding by instantiating logical variables only as needed, analogous to lifting in resolution theorem provers.
- **Data Association**: The problem of associating observation data with the objects that generated them, in a temporal context.
- **False Alarm / Clutter**: Reported observations not caused by real objects.
- **Detection Failure**: No observation is reported for a real object.
- **Multiplexer**: The conditional distribution where an unknown parent acts as a selector to choose which of several other parents influences the outcome.
- **Indexed Random Variable**: Notation common in statistics, e.g., X[i] where i has a defined integer range. Used in BUGS.
- **Probability Logic**: A logical system specialized for probabilistic reasoning. A probability assertion P(φ) ≥ p is a constraint on the distribution over possible worlds.
- **Probabilistic Logic Programs**: A probability range attached to each first-order Horn clause; inference by solving linear programs.
- **Probabilistic Databases**: Logical sentences labeled with probabilities attached directly to tuples of the database.
- **Markov Logic Networks (MLNs)**: Maximum-entropy approach where constraints expressed as weights attached to first-order clauses.
- **Record Linkage**: Problem when data records do not contain standard unique identifiers.
- **Multi-Entity Bayesian Networks**: Another open-universe modeling language (Laskey, 2008).
- **Multiple Hypothesis Tracker (MHT)**: First practical algorithm for large-scale data association (Reid, 1979).

### Probability Distributions
- **Poisson Distribution**: P(X=k) = λ^k e^{-λ} / k!. Mean = λ, Variance = λ.
- **Discrete Log-Normal Distribution**: Appropriate when the log of the number of objects is normally distributed.
- **Order-of-Magnitude Distribution (OM)**: Uses logs base 10. OM(3,1) has mean 10^3, SD of one order of magnitude (bulk between 10^2 and 10^4).

### Algorithms
- **Hungarian Algorithm**: Finds the assignment that maximizes joint probability of current observations given predicted positions. O(n^3) for n! assignments. (Kuhn, 1955)
- **Nearest-Neighbor Filter**: Repeatedly chooses closest pairing of predicted position and observation. Works well when objects are well-separated.
- **Rao-Blackwellization Trick**: Given a specific association hypothesis, the filtering calculation for each object can be done exactly/efficiently instead of sampling many possible state sequences.
- **Adaptive Proposal Distribution**: Gradually learns how to generate MCMC proposals likely to be accepted and effective.
- **Particle Gibbs Inference**: First introduced in LIBBI for probabilistic programs.

### People & Discoverers
- Gottfried Leibniz, Jacob Bernoulli, Augustus De Morgan, George Boole, Charles Sanders Peirce, John Maynard Keynes, Rudolf Carnap — all attempted to create expressive formal language for probabilistic information.
- Arpad Elo (1978) — Elo rating system (essentially Thurstone's Case V model, 1927).
- Mark Glickman (1999) — Bayesian version of Elo.
- Microsoft's TrueSkill (Herbrich et al., 2007; Minka et al., 2018) — based on Glickman's Bayesian Elo.
- Pfeffer (2000) — first used "relational probability model" (slightly different representation).
- Pasula et al. (2003) — OUPM for citation matching.
- Arora et al. (2013) — NET-VISA system.
- Milch et al. (2005); Milch (2006) — BLOG, first formal language for OUPMs.
- Sittler (1964) — first probabilistic description of data association.
- Reid (1979) — MHT algorithm.
- Kuhn (1955) — Hungarian algorithm (based on König and Egerváry, 1931).
- Carl Gustav Jacobi (1804–1851) — derived the basic theorem earlier in an unpublished Latin manuscript.
- Koller et al. (1997) — idea that probabilistic programs could represent complex probability models.
- Pfeffer (2001, 2007) — IBAL, first working PPL.
- Goodman et al. (2008) — CHURCH PPL.
- Cusumano-Towner et al. (2019) — Gen PPL.
- Bingham et al. (2019) — Pyro PPL.
- Tran et al. (2017) — Edward PPL.
- Carpenter et al. (2017) — STAN.
- Murray (2013) — LIBBI.
- Gaifman (1964a,b) — first-order probability logic.
- Hailperin (1984) — probability logic via linear programming.
- Nilsson (1986) — maximum entropy model.
- Richardson and Domingos (2006) — Markov Logic Networks.
- Breese (1992); Wellman et al. (1992) — first "templates" with logical variables.
- Gilks et al. (1994); Lunn et al. (2013) — BUGS.
- Poole (1993); Sato and Kameya (1997) — logic programming-based languages.
- Koller and Pfeffer (1998) — semantic network-based languages.
- Poole (2003) — first truly lifted probabilistic inference.
- de Salvo Braz et al. (2007) — improved lifted inference.
- McCallum et al. (2009) — FACTORIE.
- Laskey (2008) — multi-entity Bayesian networks.
- Dunn (1946) — first probabilistic record linkage.
- Fellegi–Sunter model (1969) — naive Bayes for matching.
- Charniak and Goldman (1992) — probabilistic coreference.
- Huang and Russell (1998); Pasula et al. (1999) — Bayesian identity uncertainty for traffic surveillance.
- Oh et al. (2009) — formal analysis of MCMC data association.
- Schulz et al. (2003) — particle filtering data association.
- Cox (1993); Cox and Hingorani (1994) — complexity of data association.
- McAllester et al. (2008) — connection between declarative and functional PPLs.
- Ackerman et al. (2013) — PPLs and computability theory.
- Wingate et al. (2011); Paige and Wood (2014); Wu et al. (2016a) — inference compilation.
- Claret et al. (2013); Hur et al. (2014) — static analysis for PPLs.
- Kulkarni et al. (2015) — PICTURE PPL.
- Le et al. (2017) — deep learning for importance sampling in PPLs.
- Mansinghka et al. (2013) — inference programs with diverse tactics.

## 2. Sequential Processes

### Grounding (Unrolling) an RPM into a Bayesian Network
```
for b = 1 to B do
    add node Quality_b with no parents, prior
for c = 1 to C do
    add node Honest_c with no parents, prior
    add node Kindness_c with no parents, prior
for b = 1 to B do
    for c = 1 to C do
        add node Recommendation_{c,b} with parents Honest_c, Kindness_c, Quality_b
        and conditional distribution RecCPT(Honest_c, Kindness_c, Quality_b)
```

### Evaluating a Decision Network (Section 16.5.2)
1. Set the evidence variables for the current state.
2. For each possible value of the decision node:
   a. Set the decision node to that value.
   b. Calculate posterior probabilities for parent nodes of the utility node, using standard probabilistic inference.
   c. Calculate the resulting utility for the action.
3. Return the action with the highest utility.

### OUPM MCMC Process
- Sample possible worlds defined by sets of objects and relations.
- Moves can alter relations, functions, add/subtract objects, change interpretations of constant symbols.
- Probability ratio between neighboring worlds depends on constant-size subgraph around changed variables.
- Logical query evaluated incrementally in constant time per world.
- For infinite worlds: sample partial worlds (minimal self-supporting instantiation of relevant variables).

### Generative Program Inference (PPLs)
- **Rejection sampling**: Run the program, keep traces matching evidence, count query answers.
- **Likelihood weighting**: For each generated trace, keep weight = product of probabilities of observed values.
- **MCMC**: Sample and modify execution traces. Must handle modifications that invalidate remainder of trace (e.g., changing if-statement outcome).

## 3. Hierarchies/Classifications

### Expressiveness Hierarchy
| Level | Deterministic | Probabilistic |
|-------|--------------|---------------|
| Atomic | Search algorithms | HMMs |
| Factored | CSPs, propositional logic | Bayesian networks |
| Structured | First-order logic, planning systems | RPMs, OUPMs, PPLs |

### Types of Uncertainty in Multi-Object Tracking
1. Which object generated which observation (data association)
2. False alarms (clutter)
3. Detection failures
4. New objects arriving
5. Old objects disappearing

### Types of Uncertainty in OUPMs
1. **Existence uncertainty** — what objects exist
2. **Identity uncertainty** — which terms refer to the same object
3. **Relational uncertainty** — unknown values of relations affecting dependency structure

### Two Routes to PPLs
1. **Via logic**: Devise language defining probabilities over first-order possible worlds → **declarative PPLs**
2. **Via programming languages**: Introduce stochastic elements into programming languages → **general PPLs**

## 4. Comparisons/Trade-offs

### RPM vs. OUPM
- **RPM**: Database semantics, finite possible worlds, known objects/identities
- **OUPM**: Full first-order semantics, potentially infinite worlds, existence + identity uncertainty

### Database Semantics vs. Closed-World Assumption
- RPMs use database semantics but do **not** make the closed-world assumption (unknown facts are not assumed false in a probabilistic system)

### Grounding vs. Lifted Inference
- **Grounding**: Simple but resulting Bayes net may be very large; exponential in number of objects
- **Lifted inference**: Avoids full grounding; factors cached for reuse; speedups of 3 orders of magnitude for large networks

### Exact vs. Approximate Inference for OUPMs
- Exact inference by unrolling is impractical due to potentially unbounded size
- MCMC is preferred; probability ratio computations are local (constant time)
- Partial worlds (not complete) are sampled

### Nearest-Neighbor vs. Hungarian vs. MCMC for Data Association
- **Nearest-neighbor**: Fast but fails when objects close together
- **Hungarian**: Maximizes joint probability, O(n^3). Fails under difficult conditions (incorrect assignment compounds)
- **MCMC/Particle filtering**: Handles uncertainty, can change mind about previous assignments; handles hundreds of objects in real time

## 5. Formulas & Equations

### Probability of a Logical Sentence (Equation 15.1)
P(φ) = Σ_{ω: φ is true in ω} P(ω)

### Poisson Distribution
P(X=k) = λ^k e^{-λ} / k!
- Mean = λ, Variance = λ, SD = √λ

### Conditional Probability for Recommendation Example
Recommendation(c,b) ∼ RecCPT(Honest(c), Kindness(c), Quality(b))

### Number Statement Syntax
```
#Customer ∼ UniformInt(1,3)
#LoginID(Owner=c) ∼ if Honest(c) then Exactly(1) else UniformInt(2,5)
```

### Probability of Execution Trace
P(ω) = ∏_i P(x_i | x_1, ..., x_{i-1})

## 6. Rules, Laws & Theorems

### Well-Formedness Conditions for RPMs
- Dependencies must be **acyclic** (otherwise resulting Bayes net will have cycles)
- Dependencies must be **well-founded**: no infinite ancestor chains (such as from recursive dependencies)

### Well-Formedness for OUPMs
- Well-formedness disallows cyclic dependencies and infinitely receding ancestor chains
- These conditions are **undecidable** in general, but certain syntactic sufficient conditions can be checked easily

### Decidability of Inference in PPLs
- If the underlying program halts for all inputs and random choices:
  - With **infinite-precision** continuous random variables: inference can encode the halting problem → **undecidable**
  - With **finite-precision** numbers and smooth probability distributions: inference remains **decidable**

## 7. Data Structures & Types

### RPM Type Signatures (Book Recommendation Example)
```
Honest : Customer → {true, false}
Kindness : Customer → {1,2,3,4,5}
Quality : Book → {1,2,3,4,5}
Recommendation : Customer × Book → {1,2,3,4,5}
```

### OUPM Type Declarations (Citation Matching)
```
type Researcher, Paper, Citation
random String Name(Researcher)
random String Title(Paper)
random Paper PubCited(Citation)
random String Text(Citation)
random Boolean Professor(Researcher)
origin Researcher Author(Paper)
```

### OUPM for Radar Tracking (Figure 15.9)
Key variables: EntryTime, Exits, InFlight, X(a,t) (position), Blip(Source, Time), Z(b) (observed blip position)

## 8. Visual Patterns

### Figure 15.1: Possible Worlds under Standard vs. Database Semantics
- **Top**: Standard FO semantics — infinite models, variable interpretation of constants
- **Bottom**: Database semantics — fixed interpretation, one object per constant symbol

### Figure 15.2: RPM Unrolling
- (a) Bayes net for single customer C1, single book B1
- (b) Bayes net for two customers and two books showing repeated structure

### Figure 15.3: RPM with Relational Uncertainty
- Fragment when Author(B2) is unknown, showing multiplexer pattern with Fan(C1,A1), Fan(C1,A2), Author(B2) as parents

### Figure 15.4: OUPM Possible World
- Table showing topological order of generation: #Customer → #Book → Honest → Kindness → Quality → #LoginID → Recommendation values

### Figure 15.8: Multitarget Tracking
- (a) Five time steps of 2D observations, labeled by time step but not object identity
- (b-c) Different association hypotheses
- (d) With false alarms, detection failures, track initiation/termination

## 9. Edge Cases/Exceptions/Traps

- RPMs without domain closure: the set of first-order models is **infinite**, making summation infeasible and distribution specification very difficult
- Recursive dependencies in RPMs can create infinite ancestor chains; must ensure well-foundedness
- In OUPMs, number statements with Poisson/order-of-magnitude distributions allow **unbounded numbers of objects** → unbounded numbers of random variables
- Multiple objects in tracking → (n!)^T possible assignments (n objects, T time steps)
- MCMC for PPLs: changing outcome of if-statement may **invalidate the remainder of the trace**
- Inference with infinite-precision continuous random variables can encode the **halting problem** (undecidable)
- CiteSeer in 2002 reported **over 120 distinct books** written by Russell and Norvig due to poor citation matching

## 10. Empirical Evidence/Key Results

- NET-VISA (OUPM for nuclear treaty monitoring):
  - UN SEL3 bulletin missed **27.4%** of 27,294 events in magnitude 3–4; NET-VISA missed **11.1%**
  - NET-VISA finds up to **50% more real events** than final bulletins by UN expert analysts
  - Deployed as part of CTBTO monitoring pipeline as of Jan 1, 2018
  - DPRK nuclear test (Feb 12, 2013): NET-VISA estimate 0.75km from entrance to underground test facility

- Citation matching OUPM (Pasula et al., 2003): error rate **2 to 3 times lower** than CiteSeer's

- Lifted inference caching: speedups of **three orders of magnitude** for large networks

- Compilation of probabilistic inference: speedups of **two to three orders of magnitude**

- Monte Carlo hardware improvements: **100–10,000x** improvement in speed and energy efficiency

## 11. Cross-Chapter Dependencies

- Chapter 12: Definition of probability model (Ω, P(ω))
- Chapter 13: Bayesian networks (factored representations)
- Chapter 14: HMMs, DBNs, Kalman filters; temporal reasoning; Rao-Blackwellization (p. 496); filtering (p. 467)
- Section 8.2.8: Database semantics
- Section 9.1: Expressions with parentheses as fancy symbols
- Section 8.2: First-order logic
- Section 13.4.2: MCMC
- Section 13.4.3: Compilation for Bayes nets
- Section 9.2: Lifting in logic programming
- Section 23.1: Letter trigram models

## 12. Dates & People

- Leibniz (1704) — Nouveaux Essais, first attempt to connect probability and logic
- Jacob Bernoulli — discoverer of e, calculus of variations, Law of Large Numbers
- Augustus De Morgan, George Boole — 19th century logic
- Charles Sanders Peirce — 19th century logician
- John Maynard Keynes — 20th century economist
- Rudolf Carnap — 20th century analytical philosopher
- Bernoulli (1738) — St. Petersburg paradox, utility theory
- Elo (1959/1978) — Elo rating system
- Thurstone (1927) — Case V model
- Sittler (1964) — first probabilistic data association
- Reid (1979) — MHT algorithm
- Kuhn (1955) — Hungarian algorithm
- König and Egerváry (1931) — original Hungarian method mathematicians
- Carl Gustav Jacobi (1804–1851) — derived theorem earlier in Latin manuscript
- Gaifman (1964a,b) — first-order probability logic
- Dunn (1946) — first probabilistic record linkage work
- Fellegi and Sunter (1969) — naive Bayes matching model
- Charniak and Goldman (1992) — probabilistic coreference
- Koller et al. (1997) — probabilistic programs as models
- Pfeffer (2001, 2007) — IBAL
- Goodman et al. (2008) — CHURCH
- Cusumano-Towner et al. (2019) — Gen
- Bingham et al. (2019) — Pyro
- Tran et al. (2017) — Edward
- Gilks et al. (1994); Lunn et al. (2013) — BUGS
- Poole (2003) — first lifted probabilistic inference
- Gribkoff et al. (2014); Kazemi et al. (2017) — complexity of lifted inference

## 13. Proof & Argument Patterns

**Each object contains its origin** (generation history): This property ensures every world can be constructed by **exactly one generation sequence**. If this were not the case, the probability of a world would be an unwieldy combinatorial sum over all possible generation sequences.

**Partial worlds in MCMC for OUPMs**: A partial world is a minimal self-supporting instantiation of a subset of relevant variables (ancestors of evidence and query variables). Variables beyond last observation/query time are irrelevant.

## 14. Design Paradigms/Meta-Methods

- **Shapes of representation spectrum**: Atomic → Factored → Structured (applies to both deterministic and probabilistic models)
- **Grounding/Unrolling**: Analogous to propositionalization in first-order logic
- **Lifted inference**: Analogous to lifting in resolution theorem provers / logic programming
- **Generative modeling approach**: Ask how the data came to be, write a generative model
- **Piggybacking on existing languages**: PPLs built on Scheme (CHURCH), Scala (Figaro), Julia+TensorFlow (Gen), PyTorch (Pyro), TensorFlow (Edward)

## 15. Case Studies/Classic Examples

### Book Recommendation RPM
- Types: Customer, Book
- Variables: Honest(Customer), Kindness(Customer), Quality(Book), Recommendation(Customer, Book)
- Context-specific independence: Dishonest customers ignore quality
- With unknown author: multiplexer pattern using Author(B2) as selector

### Rating Player Skill Levels (TrueSkill)
- Skill(i) ∼ N(μ, σ²)
- Performance(i,g) ∼ N(Skill(i), β²)
- Win(i,j,g) = (Performance(i,g) > Performance(j,g))
- TeamPerformance(t,g) = Σ_{i∈t} Performance(i,g)
- Microsoft's TrueSkill serves hundreds of millions of users daily

### Citation Matching OUPM (Figure 15.5)
- Researchers write papers, papers are cited, citation strings combine names and titles with errors
- #Researcher ∼ OM(3,1); #Paper(Author=r) ∼ OM(1.5,0.5) or OM(1,0.5) depending on Professor status
- Text(c) ∼ HMMGrammar(...)

### NET-VISA (Nuclear Treaty Monitoring, Figure 15.6)
- #SeismicEvents ∼ Poisson(T·λ_e)
- Time(e) ∼ UniformReal(0,T)
- Earthquake(e) ∼ Boolean(0.999)
- Location, Depth, Magnitude distributions
- Detected(e,p,s) ∼ Logistic(weights, magnitude, depth, distance)

### Multitarget Radar Tracking OUPM (Figure 15.9)
- Guaranteed aircraft A1, A2
- X(a,t) ∼ if t=0 then InitX() else N(F·X(a,t-1), Σ_x)
- #Blip(Source=a, Time=t) = 1
- Z(b) ∼ N(H·X(Source(b), Time(b)), Σ_z)

### Reading Text Generative Program (Figures 15.11, 15.15)
- Generate letters → render image → add noise
- Independent letters vs. Markov (bigram) letter model
- MCMC inference correctly identifies "uncertainty" in clean image
- In high noise: independent model misidentifies first letter as 'q'; Markov model improves

## 16. Ethics
(None specific to Chapter 15)

## 17. End-of-Chapter Material

### Summary Points
1. RPMs define probability models on worlds derived from database semantics; appropriate when all objects and identities known.
2. Objects in each possible world correspond to constant symbols; basic random variables are all possible instantiations of predicate symbols.
3. RPMs provide very concise models for worlds with large numbers of objects; handle relational uncertainty.
4. OUPMs build on full first-order semantics, allowing identity and existence uncertainty.
5. Generative programs represent probability models as executable programs in a PPL; provide universal expressive power.

### Key Papers/Systems
- BUGS (Gilks et al., 1994; Lunn et al., 2013)
- BLOG (Milch et al., 2005)
- CHURCH (Goodman et al., 2008)
- STAN (Carpenter et al., 2017)
- FACTORIE (McCallum et al., 2009)
- Gen (Cusumano-Towner et al., 2019)
- Pyro (Bingham et al., 2019)

---

# CHAPTER 16: MAKING SIMPLE DECISIONS

## 1. Named Entities

### Core Concepts
- **Decision-Theoretic Agent**: An agent that makes rational decisions based on what it believes and what it wants. Combines utility theory with probability theory.
- **Utility Function U(s)**: Assigns a single number to express the desirability of a state.
- **Expected Utility EU(a)**: Average utility value of outcomes, weighted by probability: EU(a) = Σ_{s'} P(RESULT(a)=s') U(s')
- **Principle of Maximum Expected Utility (MEU)**: A rational agent should choose the action that maximizes expected utility: action = argmax_a EU(a)
- **Lottery L**: A ticket with outcomes S₁,...,S_n occurring with probabilities p₁,...,p_n: L = [p₁,S₁; p₂,S₂; ... p_n,S_n]
- **Value Function / Ordinal Utility Function**: In deterministic environments, only a preference ranking on states is needed (numbers don't matter).
- **Preference Elicitation**: Process of presenting choices to a human and using observed preferences to pin down utility function.
- **Standard Lottery**: [p, u_⊤; (1-p), u_⊥] used to assess utility of any prize S by finding indifference probability p.
- **Normalized Utilities**: Scale with u_⊥ = 0 and u_⊤ = 1.
- **Value of a Statistical Life**: Used by US agencies (EPA, FDA, DOT) to determine costs/benefits; ~$10 million in 2019.
- **Micromort**: One in a million chance of death. Studies suggest value ~$60 per micromort.
- **QALY (Quality-Adjusted Life Year)**: Patients willing to accept shorter life expectancy to avoid disability.
- **Certainty Equivalent**: The value an agent will accept in lieu of a lottery. Most people accept ~$400 in lieu of gamble giving $1000 half the time and $0 half (EMV = $500).
- **Insurance Premium**: Difference between EMV of a lottery and its certainty equivalent.
- **Decision Network (Influence Diagram)**: Extends Bayesian networks with action and utility nodes.
- **Information Value Theory**: Enables agent to choose what information to acquire.
- **Value of Perfect Information (VPI)**: Difference in expected value between best actions before and after information is obtained.
- **Myopic Information Gathering**: Uses VPI formula shortsightedly, calculating value as if only a single evidence variable will be acquired.
- **Sensitivity Analysis**: Analyzing how much output changes as model parameters are tweaked.
- **Robust/Minimax Decision**: Decision that gives the best result in the worst case.
- **Hyperparameters**: In Bayesian approach to parametric uncertainty, model the uncertainty using hyperparameters.
- **Assistance Game**: Full two-person game where both players maximize the human's payoff (Section 16.7.2 extension).

### Six Axioms of Utility Theory
1. **Orderability**: Exactly one of (A≻B), (B≻A), or (A∼B) holds.
2. **Transitivity**: (A≻B) ∧ (B≻C) ⇒ (A≻C)
3. **Continuity**: A≻B≻C ⇒ ∃ p [p,A; 1-p,C] ∼ B
4. **Substitutability**: A∼B ⇒ [p,A; 1-p,C] ∼ [p,B; 1-p,C]
5. **Monotonicity**: A≻B ⇒ (p>q ⇔ [p,A; 1-p,B] ≻ [q,A; 1-q,B])
6. **Decomposability**: [p,A; 1-p,[q,B; 1-q,C]] ∼ [p,A; (1-p)q,B; (1-p)(1-q),C]

### Human Irrationality Phenomena
- **Allais Paradox**: People prefer B (sure $3000) over A (80% of $4000) and C (20% of $4000) over D (25% of $3000), creating inconsistent preferences.
- **Certainty Effect**: People strongly attracted to gains that are certain (Kahneman and Tversky, 1979).
- **Ellsberg Paradox**: People prefer known probabilities over unknown probabilities (ambiguity aversion).
- **Framing Effect**: Wording of decision problem impacts choices (e.g., "90% survival rate" vs. "10% death rate").
- **Anchoring Effect**: People make relative rather than absolute utility judgments.
- **Optimizer's Curse**: The estimated expected utility of the best choice is too high due to selection bias.
- **Winner's Curse**: In competitive bidding, winner likely overestimated value.
- **Post-Decision Disappointment**: Real outcome usually worse than estimated even with unbiased estimates.

### Attributes & Concepts in Multiattribute Utility
- **Strict Dominance**: Option A strictly dominates B if A is better on all attributes.
- **Stochastic Dominance**: A₁ stochastically dominates A₂ on X if ∀x ∫_{-∞}^{x} p₁(x')dx' ≤ ∫_{-∞}^{x} p₂(x')dx'.
- **Preference Independence**: Two attributes X₁,X₂ are preferentially independent of X₃ if preference between outcomes differing only in X₁,X₂ doesn't depend on X₃.
- **Mutual Preferential Independence (MPI)**: Set of attributes exhibits MPI when each attribute doesn't affect how others are traded off.
- **Utility Independence**: A set of attributes X is utility independent of Y if preferences between lotteries on X are independent of Y values.
- **Mutual Utility Independence (MUI)**: Each subset is utility-independent of remaining attributes.
- **Additive Value Function**: V(x₁,...,xₙ) = Σᵢ Vᵢ(xᵢ)
- **Multiplicative Utility Function**: For MUI: U = k₁U₁ + k₂U₂ + k₃U₃ + k₁k₂U₁U₂ + ... (n attributes, n constants, n single-attribute utilities)

### Key Numbers
- Risk of driving 230 miles in UK = 1 micromort
- Value per micromort (car buying) ≈ $60
- US DOT spends ~$6 in road repairs per expected life saved
- Typical value of statistical life (2019) ≈ $10 million
- People accept ~$400 in lieu of gamble: $1000 half the time, $0 half (EMV = $500)
- Most people wouldn't kill themselves for $60 million

## 2. Sequential Processes

### Information-Gathering Agent Algorithm (Figure 16.9)
```
function INFORMATION-GATHERING-AGENT(percept) returns an action
    persistent: D, a decision network
    integrate percept into D
    j ← the value that maximizes VPI(Eⱼ)/C(Eⱼ)
    if VPI(Eⱼ) > C(Eⱼ) then return Request(Eⱼ)
    else return the best action from D
```

### Evaluating a Decision Network
1. Set evidence variables for current state
2. For each possible value of the decision node:
   a. Set decision node to that value
   b. Calculate posterior probabilities for parent nodes of utility node
   c. Calculate resulting utility for the action
3. Return action with highest utility

## 3. Hierarchies/Classifications

### Types of Uncertainty
1. **Uncertainty about current state**: P(s)
2. **Uncertainty about action outcomes**: P(s′|s,a)
3. **Uncertainty about utility function** (Section 16.7): Unknown preferences
4. **Parametric uncertainty**: Uncertainty about parameters of the model
5. **Structural uncertainty**: Uncertainty about model structure (e.g., independence assumptions)

### Types of Preferences
- A ≻ B: Agent prefers A over B
- A ∼ B: Agent indifferent between A and B
- A ≻∼ B: Agent prefers A over B or indifferent

### Types of Dominance
- Strict dominance: One option better on ALL attributes
- Stochastic dominance: One action dominates on a single attribute under uncertainty

## 4. Comparisons/Trade-offs

### Goal-Based Agent vs. Decision-Theoretic Agent
- Goal-based: Binary distinction (good/bad)
- Decision-theoretic: Continuous range of values; can choose better state even when no best state available

### Normative vs. Descriptive Theory
- **Normative**: How a rational agent SHOULD act
- **Descriptive**: How actual agents (humans) DO act

### Risk Attitudes
- **Risk-Averse**: U(L) < U(S_{EMV(L)}). Prefer sure thing with lower EMV. Concave utility for positive wealth.
- **Risk-Seeking**: In "desperate" region at large negative wealth. Convex utility.
- **Risk-Neutral**: Linear utility curve. For small changes in wealth, almost any curve is approximately linear.

### Utility Independence vs. Preferential Independence
- Preferential independence: Deterministic preferences
- Utility independence: Preferences between lotteries on attributes (covers uncertainty)

### Bayesian vs. Robust Decision Making
- Bayesian: Model parameter uncertainty using hyperparameters; requires more modeling effort
- Robust: Minimax approach; can be overly conservative (e.g., assuming all other drivers are homicidal maniacs → stay in garage)

## 5. Formulas & Equations

### Expected Utility of Action (Equation 16.1)
EU(a) = Σ_{s′} P(RESULT(a)=s′) U(s′)

### Relationship between P(RESULT(a)) and Transition Model
P(RESULT(a)=s′) = Σ_s P(s) P(s′|s,a)

### Affine Transformation (Equation 16.2)
U′(S) = a·U(S) + b, where a > 0

### Log Utility for Money (Mr. Beard)
U(S_{k+n}) = −263.31 + 22.09 log(n + 150,000) for n between −$150K and $800K

### Post-Decision Disappointment: Distribution of Max of k Estimates
P(max{X₁,...,X_k} ≤ x) = F(x)^k
Density: P(x) = k·f(x)·(F(x))^{k-1}

### VPI Formula (General)
VPI(Eⱼ) = (Σ_{eⱼ} P(Eⱼ=eⱼ) EU(α_{eⱼ} | Eⱼ=eⱼ)) − EU(α)

### Expected Cost of Sequence (Treasure Hunt)
C(xy) = C(x) + F(x)·C(y)

### Optimal Ordering Condition (Treasure Hunt)
P(i)/C(i) ≥ P(j)/C(j) for adjacent i,j in optimal sequence

### Stochastic Dominance Formal Definition
A₁ stochastically dominates A₂ on X if: ∀x ∫_{-∞}^{x} p₁(x′)dx′ ≤ ∫_{-∞}^{x} p₂(x′)dx′

### Expected Utility for Deference (Off-Switch)
EU(d) = ∫_{-∞}^{0} P(u)·0·du + ∫_{0}^{∞} P(u)·u·du ≥ ∫_{-∞}^{∞} P(u)·u·du = EU(a)

## 6. Rules, Laws & Theorems

### Existence of Utility Function
If an agent's preferences obey the axioms of utility, then there exists a function U such that:
U(A) > U(B) ⇔ A ≻ B and U(A) = U(B) ⇔ A ∼ B

### Expected Utility of a Lottery
U([p₁,S₁; ...; p_n,S_n]) = Σ_i p_i U(S_i)

### VPI Nonnegativity
∀ⱼ VPI(Eⱼ) ≥ 0 (expected value of information is nonnegative)

### VPI Non-Additivity
VPI(Eⱼ, Eₖ) ≠ VPI(Eⱼ) + VPI(Eₖ) in general

### VPI Order Independence
VPI(Eⱼ, Eₖ) = VPI(Eⱼ) + VPI(Eₖ|Eⱼ) = VPI(Eₖ) + VPI(Eⱼ|Eₖ)

## 8. Visual Patterns

### Figure 16.1: Nontransitive Preferences & Decomposability
- (a) Cycle of exchanges costing one cent each
- (b) Decomposability: compressing two consecutive lotteries into one

### Figure 16.2: Utility of Money
- (a) Empirical data for Mr. Beard (logarithmic)
- (b) Typical S-shaped curve: concave for positive wealth, convex (risk-seeking) for desperate negative region

### Figure 16.3: Optimizer's Curse
- Distributions of max of k estimates for k=3,10,30 with unit normal error
- Mean disappointment: 0.85σ for k=3, ~2σ for k=30

### Figure 16.4: Strict Dominance
- (a) Deterministic: A dominated by B but not C/D
- (b) Uncertain: A strictly dominated by B but not C

### Figure 16.5: Stochastic Dominance
- (a) Distributions for S₁ and S₂ on frugality
- (b) Cumulative distributions showing S₁ always to the right of S₂

### Figure 16.6: Decision Network for Airport Siting
- Nodes: AirportSite (decision), Construction, Air Traffic, Litigation, Safety, Quietness, Frugality, U (utility)

### Figure 16.8: Three Cases for Value of Information
- (a) a₁ clearly superior → information not needed
- (b) Unclear choice, broad distributions → information crucial
- (c) Unclear choice, narrow distributions → information less valuable

### Figure 16.10: Uncertain Utility (Ice Cream)
- (a) Decision network with uncertain utility
- (b) Expected utility of each action (deterministic replacement)
- (c) Moving uncertainty into new random variable LikesDurian

### Figure 16.11: Off-Switch Game
- Robot R can act (uncertain payoff), switch off, or defer to human H
- H can switch R off or let it go ahead
- Deferral yields information about H's preferences

## 9. Edge Cases/Exceptions/Traps

- **Optimizer's Curse**: Unbiased estimates become biased after selecting max. For k=30, disappointment ≈ 2σ.
  - Example: Drug that cured 80% in trial (selected from thousands) will likely not cure 80%.
  - Example: Fund advertised as above-average returns (selected from dozens).
- **Allais Paradox**: People's preferences violate the substitution axiom.
- **Ellsberg Paradox**: Ambiguity aversion → people prefer known probabilities.
- **Framing Effect**: "90% survival rate" preferred 2:1 over "10% death rate" (same thing).
- **Anchoring Effect**: $200 wine bottle makes $55 seem like a bargain.
- **Refusal to value life**: Paradoxically undervalues life (asbestos example).
- **VPI Non-Additivity**: VPI(Eⱼ,Eₖ) ≠ VPI(Eⱼ)+VPI(Eₖ) in general.
- **Utility monster problem**: Egalitarian social welfare still at mercy of utility monster.
- Nonmyopic information gathering: 2^n possible subsets, superexponential tree complexity.
- **Robust/minimax approach** can be overly conservative (self-driving car staying in garage).

## 10. Empirical Evidence/Key Results

- Most people accept ~$400 instead of $1000 half the time / $0 half (CE = $400, EMV = $500)
- Value of statistical life (2019): ~$10 million
- Risk of 230 miles driving in UK = 1 micromort
- People willing to pay ~$12,000 more for safer car
- Value per micromort (car buying): ~$60
- US DOT spends ~$6 in road repairs per expected life saved
- Patients indifferent between 2 years on dialysis and 1 year at full health
- Mr. Beard's utility function: U($k+n) = -263.31 + 22.09 log(n + 150,000)

## 11. Cross-Chapter Dependencies

- Chapter 2: Performance measures, rational agents
- Chapter 5: Two-player games of chance, positive affine transformations (p. 167)
- Chapter 12: Probability axioms, refusal to bet (p. 394)
- Chapter 14: Filtering, sensor models
- Chapter 17: Sequential decisions (relaxes episodic assumption)
- Chapter 18: Multiagent decision making
- Chapter 20: Parameter learning
- Chapter 22: Reinforcement learning, Q-function

## 12. Dates & People

- Bernoulli (1738) — St. Petersburg paradox, utility proportional to log(amount)
- Jeremy Bentham (1823) — hedonic calculus
- Arnauld (1662) — Port-Royal Logic, first to state expected utility principle
- Pascal and Fermat (1654) — first correct use of probability
- Ramsey (1931) — first derivation of numerical utilities from preferences
- von Neumann and Morgenstern (1944) — Theory of Games and Economic Behavior, axioms of utility
- Savage (1954) — subjective probabilities from preferences
- Allais (1953) — Allais paradox
- Ellsberg (1962) — Ellsberg paradox
- Kahneman and Tversky (1979) — prospect theory, certainty effect
- Grayson (1960) — utility of money study (Mr. Beard)
- Keeney and Raiffa (1976) — multiattribute utility theory
- Howard and Matheson (1984) — influence diagrams
- Shachter (1986) — decision network inference
- Smith and Winkler (2006) — optimizer's curse
- Ariely (2009) — "Predictably Irrational"
- Kahneman (2011) — "Thinking: Fast and Slow"
- Hadfield-Menell et al. (2017b) — off-switch example
- Russell (2019) — framework for beneficial AI

## 13. Proof & Argument Patterns

**Proof that nontransitive preferences lead to money pump**: A≻B≻C≻A → can trade C for A + 1¢, B for C + 1¢, A for B + 1¢, cycle indefinitely.

**Proof that VPI is nonnegative**: In worst case, can ignore information and pretend never received it.

**Proof for deference (off-switch game)**:
EU(d) = ∫_{-∞}^{0} P(u)·0·du + ∫_{0}^{∞} P(u)·u·du = region where u>0 only
EU(a) = ∫_{-∞}^{∞} P(u)·u·du = full integral including negative region
Therefore EU(d) ≥ EU(a), equality only when negative region has zero probability.

**Treasure Hunt Optimization**: Show that direction of cost change when flipping adjacent subsequences depends only on pair, not context. Leads to ordering by P(i)/C(i).

## 14. Design Paradigms/Meta-Methods

- **Decision-theoretic approach**: Probability theory (beliefs) + utility theory (desires) → decision theory (actions)
- **Preference elicitation through indifference probabilities**: Compare prize S to standard lottery [p, u_⊤; 1-p, u_⊥]
- **Myopic information gathering** as greedy search heuristic
- **Moving uncertainty into the world**: Unknown preferences can be modeled by ordinary random variables (LikesDurian)
- **Structural vs. parametric uncertainty distinction**

## 15. Case Studies/Classic Examples

### Oil Drilling Information Value
- n indistinguishable blocks, 1 has oil worth C
- Survey of block 3: worth C/n to the company

### Durian Ice Cream (Uncertain Preferences)
- 50% chance sublime (+$100), 50% hate it (-$80)
- Expected net gain = $8 vs. vanilla $1
- Transforming uncertainty into LikesDurian random variable

### Off-Switch Game (Robbie & Harriet)
- Robbie can act (avg +10), switch off (0), or defer
- Deferral: 40% chance Harriet switches off (0), 60% chance lets go ahead (avg +30)
- Expected value of deferral = 18 > 10
- Robbie has positive incentive to defer

### Game Show Gamble
- $1M sure vs. coin flip: $0 or $2.5M (EMV = $1.25M)
- Most people take sure $1M (risk-averse)

## 16. Ethics

- Tradeoffs on life and death are made all the time (aircraft overhauls, car safety, pollution)
- Refusal to put monetary value on life can mean life is undervalued (asbestos example)
- Value of a statistical life used by US government agencies
- Machine deference to humans: robot with uncertainty about human preferences allows itself to be switched off

---

# CHAPTER 17: MAKING COMPLEX DECISIONS

## 1. Named Entities

### Core Concepts
- **Sequential Decision Problem**: Agent's utility depends on a sequence of decisions (not one-shot).
- **Markov Decision Process (MDP)**: A sequential decision problem for a fully observable, stochastic environment with Markovian transition and additive rewards. Components: states S, actions A(s), transition model P(s′|s,a), reward function R(s,a,s′), discount γ.
- **Policy π**: A solution specifying what the agent should do for any state. π(s) = action recommended in state s.
- **Optimal Policy π***: Policy yielding highest expected utility.
- **Reward R(s,a,s′)**: For every transition from s to s′ via action a. Bounded by ±R_max.
- **Bellman Equation**: U(s) = max_{a∈A(s)} Σ_{s′} P(s′|s,a)[R(s,a,s′) + γU(s′)]
- **Q-function (Action-Utility Function)**: Q(s,a) = expected utility of taking action a in state s.
- **Discount Factor γ**: Number between 0 and 1. γ=0 → only immediate rewards matter; γ=1 → additive undiscounted rewards.
- **Finite Horizon**: Fixed time N after which nothing matters → nonstationary policy.
- **Infinite Horizon**: No fixed deadline → stationary policy.
- **Proper Policy**: Guaranteed to reach a terminal state eventually.
- **Additive Discounted Rewards**: U_h([s₀,a₀,s₁,a₁,s₂,...]) = R(s₀,a₀,s₁) + γR(s₁,a₁,s₂) + γ²R(s₂,a₂,s₃) + ...
- **Average Reward**: Infinite sequences compared by average reward per time step.
- **Shaping Theorem**: Adding γΦ(s′)−Φ(s) to reward leaves optimal policy unchanged.
- **Dynamic Decision Network (DDN)**: Extends DBNs with decision, reward, and utility nodes; factored representation for MDPs.
- **Value Iteration**: Iterative algorithm solving Bellman equations; converges to unique solution.
- **Bellman Update**: U_{i+1}(s) ← max_a Σ_{s′} P(s′|s,a)[R(s,a,s′) + γU_i(s′)]
- **Policy Iteration**: Alternates policy evaluation and policy improvement.
- **Policy Evaluation**: Calculate U_i = U^{π_i} given policy π_i.
- **Policy Improvement**: Calculate new MEU policy using one-step look-ahead.
- **Modified Policy Iteration**: Approximate policy evaluation using simplified value iteration steps.
- **Asynchronous Policy Iteration**: Pick any subset of states for updating.
- **Contraction**: A function that, when applied to two inputs, produces outputs "closer together" by at least constant factor.
- **Max Norm**: ||U|| = max_s |U(s)|
- **Policy Loss**: ||U^{π_i} − U|| — the most the agent can lose by executing π_i instead of π*.
- **Real-Time Dynamic Programming (RTDP)**: Online MDP solving analogous to LRTA*; explores sub-MDP from current state.
- **Monte Carlo Planning**: Online planning using sampling; includes UCT algorithm.
- **Expectimax Algorithm**: Builds tree of alternating max and chance nodes for MDPs.
- **ε-Horizon**: Tree depth H such that sum of rewards beyond H < ε.
- **N-Armed Bandit**: n levers, each with unknown probability distribution of winnings.
- **Bandit Problem**: MDP where state space = Cartesian product of arm states; actions select which arm to pull.
- **Markov Reward Process (MRP)**: MDP with only one possible action.
- **One-Armed Bandit**: Arm M produces rewards, arm M_λ gives fixed λ each pull.
- **Stopping Time**: Time T at which optimal strategy switches from first arm to fixed arm.
- **Gittins Index**: Value λ = max_{T>0} E[Σ_{t=0}^{T-1} γ^t R_t] / E[Σ_{t=0}^{T-1} γ^t]; optimal policy = pull arm with highest index.
- **Restart MDP M_s**: MDP where in every state the agent can restart from initial state s.
- **Bernoulli Bandit**: Each arm produces 0/1 with fixed unknown probability μᵢ.
- **Exploration Bonus**: Arms tried only few times get bonus (higher Gittins index than their estimated value would suggest).
- **Upper Confidence Bound (UCB)**: UCB(Mᵢ) = μ̂ᵢ + g(N)/√Nᵢ
- **Thompson Sampling**: Choose arm randomly according to probability it is optimal given samples so far.
- **Selection Problem**: Choosing best option with fixed cost per test; no index function exists.
- **Bandit Superprocess (BSP)**: Each arm is a full MDP; globally optimal policy may include locally suboptimal actions.
- **Opportunity Cost**: How much utility is given up per time step by not devoting it to another arm.
- **Dominating Policy**: Optimal policy unaffected by opportunity cost; gives upper bound on value.
- **Partially Observable MDP (POMDP)**: MDP + sensor model P(e|s). Belief state b is probability distribution over states.
- **Belief State Update**: b′(s′) = α P(e|s′) Σ_s P(s′|s,a) b(s) = α FORWARD(b,a,e)
- **POMCP**: Partially Observable Monte Carlo Planning = particle filtering + UCT.

### Algorithms
- **Value Iteration** (Figure 17.6)
- **Policy Iteration** (Figure 17.9)
- **Q-VALUE Function**: returns Σ_{s′} P(s′|s,a)[R(s,a,s′) + γU[s′]]
- **POMDP Value Iteration** (Figure 17.16)
- **UCT for MDPs**: From Chapter 5, adapted for stochastic rewards
- **Hungarian Algorithm**: O(n³) for assignment

### Key People
- Richard Bellman (1957) — Bellman equation, dynamic programming
- John Gittins (1974, 1989) — Gittins index
- Herbert Robbins (1952) — bandit problems
- Lai and Robbins (1985) — regret bounds O(log N)
- Thompson (1933) — Thompson sampling
- Auer et al. (2002) — UCB heuristic
- Åstrom (1965); Aoki (1965) — POMDP → MDP on belief states
- Sondik (1971) — first complete POMDP solution algorithm
- Smallwood and Sondik (1973) — POMDP value iteration
- Kocsis and Szepesvári (2006) — UCT algorithm
- Silver and Veness (2011) — POMCP

## 2. Sequential Processes

### Value Iteration Algorithm (Figure 17.6)
```
function VALUE-ITERATION(mdp, ε) returns a utility function
    U, U′ ← vectors of utilities, initially zero
    δ ← 0
    repeat
        U ← U′; δ ← 0
        for each state s in S do
            U′[s] ← max_{a∈A(s)} Q-VALUE(mdp, s, a, U)
            if |U′[s] − U[s]| > δ then δ ← |U′[s] − U[s]|
    until δ ≤ ε(1−γ)/γ
    return U
```

### Policy Iteration Algorithm (Figure 17.9)
```
function POLICY-ITERATION(mdp) returns a policy
    U ← vector of utilities, initially zero
    π ← policy vector, initially random
    repeat
        U ← POLICY-EVALUATION(π, U, mdp)
        unchanged? ← true
        for each state s in S do
            a* ← argmax_a Q-VALUE(mdp, s, a, U)
            if Q-VALUE(mdp, s, a*, U) > Q-VALUE(mdp, s, π[s], U) then
                π[s] ← a*; unchanged? ← false
    until unchanged?
    return π
```

### POMDP Value Iteration (Figure 17.16)
```
function POMDP-VALUE-ITERATION(pomdp, ε) returns a utility function
    U′ ← set containing empty plan [], with α_[](s) = R(s)
    repeat
        U ← U′
        U′ ← set of all plans consisting of an action and, for each percept, a plan in U
        U′ ← REMOVE-DOMINATED-PLANS(U′)
    until MAX-DIFFERENCE(U, U′) ≤ ε(1−γ)/γ
    return U
```

### POMDP Decision Cycle
1. Given current belief state b, execute action a = π*(b)
2. Observe percept e
3. Set belief state to FORWARD(b, a, e) and repeat

## 3. Hierarchies/Classifications

### MDP Solution Types
| Algorithm | Type | Complexity |
|-----------|------|------------|
| Value Iteration | Offline, exact | O(|S|²|A| per iteration) |
| Policy Iteration | Offline, exact | O(|S|³) per evaluation |
| Linear Programming | Offline, exact | Polynomial (but slow in practice) |
| UCT / RTDP | Online, approximate | Depends on playouts |

### Horizon Types
- **Finite horizon**: Fixed N; nonstationary policy
- **Infinite horizon**: No deadline; stationary policy; discounted or average reward

### Reward Aggregation Types
1. **Additive discounted rewards**: U_h = Σ γ^t R_t (most common)
2. **Additive undiscounted (γ=1)**: Only works with proper policies
3. **Average reward**: lim_{T→∞} (1/T) Σ_{t=0}^{T} R_t

### Three Solutions to Infinite Undiscounted Sequences
1. Discounted rewards (finite sum)
2. Terminal states with proper policies
3. Average reward per time step

## 4. Comparisons/Trade-offs

### Value Iteration vs. Policy Iteration
- **Value Iteration**: Simple, converges exponentially fast, but may need many iterations for γ close to 1
- **Policy Iteration**: Fewer iterations, each is O(|S|³) for exact evaluation; guaranteed to terminate in finite steps (finitely many policies)

### Online vs. Offline MDP Algorithms
- **Offline**: Value iteration, policy iteration — precompute full solution
- **Online**: Expectimax, UCT, RTDP — compute at each decision point

### Exact vs. Approximate POMDP Solving
- **Exact** (Sondik): Doubly exponential in depth, only for tiny problems
- **Point-based**: Scales to thousands of states
- **Online/POMCP**: Sampling-based, can handle large state spaces

### Stationary vs. Nonstationary Preferences
- Stationarity: If you prefer one future starting tomorrow, you should still prefer it starting today
- Only additive discounting satisfies stationarity

## 5. Formulas & Equations

### Expected Utility of Policy (Equation 17.2)
U^π(s) = E[ Σ_{t=0}^{∞} γ^t R(S_t, π(S_t), S_{t+1}) ]

### Bellman Equation (Equation 17.5)
U(s) = max_{a∈A(s)} Σ_{s′} P(s′|s,a)[R(s,a,s′) + γU(s′)]

### Q-function Bellman Equation (Equation 17.8)
Q(s,a) = Σ_{s′} P(s′|s,a)[R(s,a,s′) + γ max_{a′} Q(s′,a′)]

### Policy Extraction from Q (Equation 17.7)
π*(s) = argmax_a Q(s,a)

### Shaping Theorem (Equation 17.9)
R′(s,a,s′) = R(s,a,s′) + γΦ(s′) − Φ(s)

### Discounted Sum Bound (Equation 17.1)
Σ_{t=0}^{∞} γ^t R_max = R_max / (1−γ)

### Bellman Update (Equation 17.10)
U_{i+1}(s) ← max_{a} Σ_{s′} P(s′|s,a)[R(s,a,s′) + γU_i(s′)]

### Contraction Property (Equation 17.11)
||BU_i − BU′_i|| ≤ γ ||U_i − U′_i||

### Termination Condition (Equation 17.12)
If ||U_{i+1} − U_i|| < ε(1−γ)/γ then ||U_{i+1} − U|| < ε

### Iterations Required
N = ⌈log(2R_max / ε(1−γ)) / log(1/γ)⌉

### Policy Loss Bound (Equation 17.13)
If ||U_i − U|| < ε then ||U^{π_i} − U|| < 2ε

### Simplified Bellman Equation for Policy Evaluation (Equation 17.14)
U_i(s) = Σ_{s′} P(s′|s, π_i(s))[R(s, π_i(s), s′) + γU_i(s′)]

### ε-Horizon Depth
H = ⌈log_γ (ε(1−γ)/R_max)⌉

### Gittins Index (Equation 17.15)
λ = max_{T>0} E[Σ_{t=0}^{T-1} γ^t R_t] / E[Σ_{t=0}^{T-1} γ^t]

### UCB Formula
UCB(M_i) = μ̂_i + g(N)/√N_i

### Belief State Update (Equation 17.16)
b′(s′) = α P(e|s′) Σ_s P(s′|s,a) b(s)

### Probability of Percept (Equation 17.17)
P(b′|b,a) = Σ_e P(b′|e,a,b) Σ_{s′} P(e|s′) Σ_s P(s′|s,a) b(s)

### Expected Reward in Belief State
ρ(b,a) = Σ_s b(s) Σ_{s′} P(s′|s,a) R(s,a,s′)

### POMDP Utility Vector (Equation 17.18)
α_p(s) = Σ_{s′} P(s′|s,a)[R(s,a,s′) + γ Σ_e P(e|s′) α_{p.e}(s′)]

### LP Formulation of MDP
Minimize Σ_s U(s) subject to:
U(s) ≥ Σ_{s′} P(s′|s,a)[R(s,a,s′) + γU(s′)] for all s, a

## 6. Rules, Laws & Theorems

### Bellman Equation Theorem
The utilities of states (Equation 17.2) are the unique solutions of the set of Bellman equations.

### Contraction Theorem (Equation 17.11)
The Bellman update is a contraction by factor γ on the space of utility vectors. Hence value iteration always converges to a unique solution when γ < 1.

### Exponential Convergence of Value Iteration
Error is reduced by factor at least γ on each iteration.

### Shaping Theorem
R′(s,a,s′) = R(s,a,s′) + γΦ(s′)−Φ(s) leaves optimal policy unchanged.

### Policy Loss Bound
If ||U_i − U|| < ε then ||U^{π_i} − U|| < 2ε

### Gittins Index Theorem
Optimal bandit policy: Pull arm with highest Gittins index.

### No Index for Selection Problems
No index function exists for selection problems (proof: adding third arm can switch preferences between two arms).

### BSP Globally Optimal ≠ Locally Optimal
Globally optimal policy for a BSP may include actions that are locally suboptimal for constituent MDPs. Globally and locally optimal policies coincide only when γ=1.

### POMDP → Belief-State MDP Theorem
An optimal policy for the belief-state MDP (with transition P(b′|b,a) and reward ρ(b,a)) is also an optimal policy for the original POMDP.

### POMDP Utility Function Structure
The utility function U(b) on belief states is piecewise linear and convex.

### POMDP Complexity
Solving POMDPs optimally is PSPACE-hard.

## 8. Visual Patterns

### Figure 17.1: 4×3 MDP Environment
- Grid world: start (1,1), terminal +1 at (4,3), terminal −1 at (4,2)
- Intended outcome: 0.8 probability, right angles: 0.1 each
- Collision with wall → no movement
- All transitions have reward −0.04 except terminals (+1, −1)

### Figure 17.2: Optimal Policies
- (a) With r=−0.04: two policies (Left or Up from (3,1) equally optimal)
- (b) Four ranges of r: r<−1.6497 (head for nearest exit); −0.7311<r<−0.4526 (shortest route to +1); −0.0274<r<0 (no risks); r>0 (avoid both exits, infinite reward)

### Figure 17.3: State Utilities (γ=1, r=−0.04)
```
0.8516   0.9078   0.9578
0.8016            0.7003
0.7453   0.6953   0.6514   0.4279
```

### Figure 17.4: DDN for Mobile Robot
- State variables: X_t (location+orientation), Ẋ_t (velocity), Charging_t, Battery_t
- Action variables: Plug/Unplug, LeftWheel, RightWheel
- Three-step projection shown

### Figure 17.5: Tetris MDP
- State: CurrentPiece (7), NextPiece (7), Filled (10×20 bits = 200 bits)
- State space: ~10⁶²
- Every policy is proper

### Figure 17.7: Value Iteration Convergence
- (a) Utility estimates over iterations for states (1,1), (1,3), (3,1), (3,3), (4,1)
- (b) Iterations required vs. γ for different ε/R_max ratios

### Figure 17.10: Expectimax Tree for 4×3 MDP
- Root at (3,2); triangular max nodes; circular chance nodes
- Branching: Up, Right, Down, Left → each with 3 outcome states

### Figure 17.12: Deterministic Bandit
- (a) Two arms: M = 0,2,0,7.2,0,0,...; M₁ = 1,1,1,...
- (b) General case: M arbitrary, M_λ = λ, λ, λ,...

### Figure 17.14: Bernoulli Bandit
- (a) States (sᵢ, fᵢ) with transitions and rewards
- (b) Gittins indices showing exploration bonus for (3,2) vs. (7,4)

### Figure 17.15: POMDP Utility Functions
- (a) One-step plans: [Stay] and [Go] lines; bold = max
- (b) Eight two-step plans
- (c) Four undominated two-step plans
- (d) 144 undominated eight-step plans

### Figure 17.17: POMDP Expectimax Tree
- Root = uniform belief state; branches = Up/Right/Down/Left
- Resulting belief states shown as shaded grids

### Figure 17.18: POMDP Agent Trace
- Sequence: Left, Left, Up, Right, Right, Right
- Shows belief states evolving

## 9. Edge Cases/Exceptions/Traps

- **Improper policies**: With γ=1 and no terminal state, can get infinite reward → standard algorithms fail
- **γ close to 1**: Very slow convergence of value iteration (N grows rapidly)
- **Policy π_i becomes optimal long before U_i converges** (at i=5 for 4×3 world with γ=0.9, U_i error still 0.51)
- **Nonlinear Bellman equations**: "max" operator makes them nonlinear
- **BSP trap**: Thinking globally optimal = locally optimal for each MDP is WRONG
- **Selection problems have no index function**: Optimal policy can switch preferences when third arm added
- **POMDP infinite belief space**: Continuous, high-dimensional
- **POMDP complexity**: PSPACE-hard
- **POMDP tree size**: |A|^d · |E|^d for depth d
- **Random/near-random playouts**: Fail for long time-scale tasks (e.g., laying table for dinner = millions of actions)

## 10. Empirical Evidence/Key Results

- 4×3 world with γ=1, r=−0.04: optimal expected utility from start = 0.7453 (state (1,1))
- Policy π_i optimal at i=5 even when ||U_i−U|| = 0.51
- UCT in 4×3 world: 160 playouts → average total reward 0.4 (vs. optimal 0.7453)
- UCT with γ=0.5, ε=0.1, R_max=1: H=5; with γ=0.9: H=44
- Gittins index for deterministic sequence 0,2,0,7.2,0,0,...: 1.0133 (T=4 optimal)
- Bernoulli bandit: (3,2) has higher Gittins index (0.7057) than (7,4) (0.6922) despite lower estimated value
- POMDP with 4-bit sensor: |E|=16, can have hundreds of undominated plans

## 11. Cross-Chapter Dependencies

- Chapter 3: Search problems, path cost functions
- Chapter 4: LRTA*, belief states, sensorless/contingency problems
- Chapter 5: Expectiminimax, UCT, heuristic evaluation functions
- Chapter 14: DBNs, Kalman filters (linear-Gaussian), particle filtering, switching Kalman filter (p. 484)
- Chapter 16: Decision theory, utility theory, value of information, multiattribute utility
- Chapter 22: Reinforcement learning, Q-learning (Chapter 22.3.3)

## 12. Dates & People

- Bellman (1952, 1957) — Dynamic Programming
- Shapley (1953b) — value iteration for Markov games
- Howard (1960) — policy iteration
- Sondik (1971) — POMDP value iteration
- Smallwood and Sondik (1973) — POMDP algorithm
- Gittins and Jones (1974); Gittins (1989) — Gittins index
- Lai and Robbins (1985) — regret bounds
- Auer et al. (2002) — UCB heuristic
- Kocsis and Szepesvári (2006) — UCT
- Silver and Veness (2011) — POMCP
- Sutton (1988); Watkins (1989) — reinforcement learning
- Dean and Kanazawa (1989a) — DDN agent architecture
- Boutilier et al. (2000); Koller and Parr (2000) — factored MDPs
- Ng et al. (1999) — shaping theorem
- Papadimitriou and Tsitsiklis (1987) — POMDP complexity (PSPACE-hard)
- Åstrom (1965); Aoki (1965) — POMDP → MDP on belief states

---

# CHAPTER 18: MULTIAGENT DECISION MAKING

## 1. Named Entities

### Core Concepts
- **Multiagent Systems**: Environments containing multiple actors making decisions.
- **Multiagent Planning Problem**: Determining how multiple agents should act.
- **Benevolent Agent Assumption**: Agents will simply do what they are told.
- **Multieffector Planning**: Managing each effector while handling interactions.
- **Multibody Planning**: When effectors are physically decoupled into detached units.
- **Decentralized Planning**: Planning phase is centralized but execution phase is decoupled.
- **Counterparts**: Other actors who are also decision makers with their own preferences.
- **Common Goal**: All decision makers pursuing same goal; main problem = coordination.
- **Game Theory**: Theory of strategic decision making where players take into account how other players may act.
- **Cooperative Game**: Binding agreements between agents possible → cooperative game theory.
- **Non-Cooperative Game**: No binding agreements; agents independently decide (may still cooperate if in their interest).
- **Agent Design (Game Theory)**: Agent computes best strategy assuming rational opponents.
- **Mechanism Design**: Defining rules of the environment so collective good is maximized when each agent maximizes own utility.

### Normal Form Games
- **Normal Form Game**: Players act simultaneously; defined by players, actions, payoff function.
- **Payoff Matrix**: For two players, rows = one player's actions, columns = other's; each cell labeled with both payoffs.
- **Strategy**: What we called "policy" earlier.
- **Pure Strategy**: Deterministic policy (single action for single-move games).
- **Mixed Strategy**: Randomized policy, [p:a; (1-p):b].
- **Strategy Profile**: Assignment of a strategy to each player.
- **Solution Concept**: Tries to define rational action given beliefs about others' beliefs.

### Key Games
- **Prisoner's Dilemma**: Two prisoners, each chooses testify or refuse. Dominant strategy = testify, but (refuse,refuse) is better for both.
- **Two-Finger Morra**: Players display 1 or 2 fingers. O wins if odd, E if even.
- **Matching Pennies**: Ali and Bo choose heads/tails. Same → Ali wins; different → Bo wins. No pure Nash equilibrium.
- **Ultimatum Game**: One round negotiation; first mover has all the power.
- **Paperclip Game**: Assistance game where Harriet signals preferences to Robbie.
- **Stage Game**: The single-move game in a repeated game.

### Solution Concepts
- **Dominant Strategy**: A strategy that is best response to ALL counterpart strategies.
- **Strong Domination**: s dominates s′ if outcome for s is better for every choice of other player(s).
- **Weak Domination**: s dominates s′ if better on at least one profile and no worse on any other.
- **Dominant Strategy Equilibrium**: All players choose dominant strategies.
- **Best Response**: A strategy is a best response to counterpart strategies if no alternative yields higher payoff.
- **Nash Equilibrium**: Strategy profile where no player can unilaterally change strategy for higher payoff (assuming others stay).
- **Maximin Equilibrium**: For zero-sum games; each player guarantees a minimum payoff.
- **Subgame Perfect Nash Equilibrium**: Must be Nash equilibrium in every subgame.
- **Bayes-Nash Equilibrium**: Equilibrium with respect to prior distribution over others' strategies.

### Social Welfare Concepts
- **Social Welfare**: Overall good from society's perspective.
- **Pareto Optimality**: No other outcome makes one player better off without making another worse off.
- **Utilitarian Social Welfare**: Sum of utilities of all players.
- **Egalitarian Social Welfare**: Maximize utility of worst-off member (maximin approach).
- **Gini Coefficient**: Measures how evenly utility is spread among players.

### Repeated Games
- **Repeated (Iterated) Game**: Players play multiple rounds of a stage game.
- **Limit of Means**: Average of utilities over infinite sequence.
- **Finite State Machine (FSM) Strategies**: Tit-for-Tat, Hawk, Dove, Grim, Tat-for-Tit.
- **Backward Induction**: Working backwards from terminal states using dynamic programming.
- **Nash Folk Theorems**: Every outcome where each player receives at least their security value can be sustained as Nash equilibrium in infinitely repeated game.

### Extensive Form Games
- **Extensive Form**: Game represented as a game tree.
- **Perfect Information**: Players know exactly where they are in the game tree.
- **Imperfect Information**: Players uncertain about actual state.
- **Information Set**: Set of states a player cannot distinguish between (game theorists' term for belief state).
- **Subgame**: Every decision state in a game tree defines a subgame.
- **Credible Threat**: A threat that the player would actually carry out if called upon.
- **Sequence Form**: Represents paths through tree, linear in size (vs. exponential normal form).
- **Abstraction**: Simplifying game by ignoring irrelevant details (e.g., suits in poker).

### Cooperative Game Theory
- **Cooperative Game G = (N, ν)**: Set of players N, characteristic function ν(C) for each subset C.
- **Characteristic Function**: ν(C) = value coalition C could obtain.
- **Coalition**: Any subset of players.
- **Grand Coalition**: Set of all players N.
- **Coalition Structure**: A partition of players into coalitions.
- **Payoff Vector (x)**: Distribution of value among players; Σ_{i∈C} x_i = ν(C) for each coalition C.
- **Superadditivity**: ν(C∪D) ≥ ν(C) + ν(D) for all C,D.
- **Imputation**: Payoff vector satisfying: Σ_i x_i = ν(N) and x_i ≥ ν({i}) for all i (individual rationality).
- **Core**: Set of all imputations x satisfying x(C) ≥ ν(C) for every coalition C ⊂ N.
- **Shapley Value**: φ_i(G) = (1/n!) Σ_{p∈P} mc_i(p_i), where p_i = set of players preceding i in ordering p.
- **Marginal Contribution**: mc_i(C) = ν(C∪{i}) − ν(C).
- **Dummy Player**: Player that never adds any value (mc_i(C)=0 for all C).
- **Symmetric Players**: Always make identical marginal contributions.
- **Marginal Contribution Net (MC-Net)**: Represent characteristic function as set of rules (C_i, x_i); ν(C) = sum of x_i for rules where C_i ⊆ C.
- **Coalition Structure Graph**: Graph where nodes at level ℓ = coalition structures with ℓ coalitions; upward edge = division of coalition.

### Mechanisms
- **Mechanism**: Language for strategies + center + outcome rule.
- **Contract Net Protocol**: Four phases: problem recognition → task announcement → bidding → awarding.
- **Auction**: Mechanism for allocating scarce resources.
- **Ascending-Bid (English) Auction**: Center starts with minimum bid, increments until no more bids.
- **Sealed-Bid Auction**: Each bidder makes single bid, unseen by others.
- **Sealed-Bid Second-Price (Vickrey) Auction**: Winner pays second-highest bid; dominant strategy = bid true value.
- **Truth-Revealing (Truthful) Mechanism**: Dominant strategy for bidders is to reveal true value.
- **Revelation Principle**: Any mechanism can be transformed into equivalent truth-revealing mechanism.
- **Revenue Equivalence Theorem**: Any auction mechanism with certain properties yields same expected revenue.
- **VCG (Vickrey-Clarke-Groves) Mechanism**: Truth-revealing mechanism maximizing global utility. Winners pay tax equal to loss their presence caused to losers.
- **Tragedy of the Commons**: If nobody pays for using common resource, it may be exploited, leading to lower total utility.
- **Externalities**: Effects on global utility not recognized in individual agents' transactions.

### Social Choice / Voting
- **Social Choice Theory**: Study of voting procedures.
- **Social Welfare Function**: Combines preferences into social preference order.
- **Social Choice Function**: Takes preference orders as input, outputs set of winners.
- **Social Outcome**: Most preferred outcome by group.
- **Condorcet's Paradox**: 3 voters, 3 outcomes → majority prefers ωₐ > ω_b > ω_c > ω_a.
- **Condorcet Winner**: Candidate that beats every other in pairwise election.
- **Arrow's Theorem**: No social welfare function can satisfy all of: Pareto condition, Condorcet winner condition, IIA, no dictatorships (for ≥3 outcomes).
- **Gibbard-Satterthwaite Theorem**: Any social choice function with >2 outcomes that satisfies Pareto is either manipulable or a dictatorship.
- **Simple Majority Vote**: With 2 candidates.
- **Plurality Voting**: Each voter gives top choice; most votes wins.
- **Borda Count**: Score k for top, k−1 for second, etc.; highest total wins.
- **Approval Voting**: Voters submit approved candidates; most approvals win.
- **Instant Runoff Voting**: Eliminate lowest first-place vote getter until majority winner.
- **True Majority Rule Voting**: Winner beats all others in pairwise comparisons.

### Bargaining
- **Alternating Offers Bargaining Model**: Agents take turns making offers.
- **Ultimatum Game**: Single round; first mover proposes split, second accepts or rejects.
- **Conflict Deal**: If no agreement reached → predefined default outcome.
- **Negotiation Set**: Set of all possible deals.
- **Task-Oriented Domain**: Set of tasks to be allocated among agents.
- **Individually Rational Deal**: Each agent's utility ≥ 0 (better than conflict).
- **Monotonic Concession Protocol**: Simultaneous proposals each round; if one agent's proposal matches/exceeds other's → agreement; otherwise concede or conflict.
- **Concession**: A proposal more preferred by the other agent.
- **Zeuthen Strategy**: Agent with more to lose from conflict (lower risk) should concede. Risk = utility lost by conceding / utility lost by causing conflict.

### Assistance Games
- **Assistance Game**: Full two-person game where Harriet observes own preferences θ, Robbie has prior P(θ), payoff defined by θ and identical for both.
- **Provably Beneficial AI**: Formalized by assistance game.

### Key People
- John von Neumann (1928) — maximin equilibrium for zero-sum games
- von Neumann and Morgenstern (1944) — Theory of Games and Economic Behavior
- John Nash (1950) — Nash equilibrium (Nobel 1994)
- John Harsanyi (1967) — Bayes-Nash equilibrium
- Lloyd Shapley (1953a) — Shapley value (Nobel 2012)
- Kenneth Arrow (1951) — Arrow's theorem
- Vilfredo Pareto (1848–1923) — Pareto optimality
- Marquis de Condorcet (1743–1794) — Condorcet's paradox
- Jean-Charles de Borda — Borda count
- William Vickrey (1914–1996) — Vickrey auction (Nobel 1996)
- Hurwicz, Maskin, Myerson (2007 Nobel) — mechanism design foundations
- Kenneth Arrow (1951) — Arrow's theorem
- Gibbard and Satterthwaite — Gibbard-Satterthwaite theorem
- Albert W. Tucker (1950) — prisoner's dilemma
- Reinhart Selten — subgame perfect Nash equilibrium
- Donald Gillies (1959) — core
- Reid Smith (1980) — contract net protocol
- Zeuthen — Zeuthen strategy
- Rubinstein (1982) — alternating offers protocol
- Jeffrey S. Rosenschein and Zlotkin (1994) — monotonic concession protocol
- Hadfield-Menell et al. (2017a) — assistance games (cooperative inverse reinforcement learning)
- Brown and Sandholm (2019) — Pluribus

## 2. Sequential Processes

### Backward Induction for Extensive-Form Games
1. For each nonterminal state s:
2. If all children labeled with payoff profile:
3. Label s with payoff profile from child maximizing payoff of player making decision at s
4. (For chance nodes: compute expected utility)
5. Guaranteed to terminate in polynomial time in size of game tree
6. Resulting strategies are Nash equilibrium strategies

### Computing Nash Equilibria in Normal Form (Pure Strategies)
- Exhaustive search: iterate through each strategy profile (m^n possibilities), check for beneficial deviation
- Or: myopic best response — start random, flip non-optimal choices, repeat

### Computing Maximin Equilibrium (Zero-Sum)
- Remove dominated pure strategies
- Find intersection point of remaining hyperplanes
- Solve as linear programming problem

### Contract Net Protocol (Four Phases)
1. **Problem Recognition**: Agent identifies need for cooperative action
2. **Task Announcement**: Advertise task to other agents (sufficient information for bidding)
3. **Bidding**: Recipients evaluate task; submit bids indicating capabilities/terms
4. **Awarding**: Manager selects agent(s); sends award message; contractor takes responsibility

### Monotonic Concession Protocol
1. First round: both agents simultaneously propose deals from negotiation set
2. Agreement if one agent's offer matches/exceeds other's
3. If no agreement: proceed to next round
4. In round t+1: each agent repeats proposal or makes concession (more preferred by other)
5. If neither concedes: conflict deal implemented

### Zeuthen Strategy
1. First proposal: deal maximizing own utility
2. Compute risk_t_i = (utility lost by conceding) / (utility lost by causing conflict)
3. Agent with smaller risk (more to lose) concedes
4. Concede just enough to shift balance of risk to other agent
5. If equal risk: flip a coin to decide who concedes

## 3. Hierarchies/Classifications

### Multiagent Environment Types
1. **One decision maker** (benevolent agents): multieffector → multibody → decentralized planning
2. **Multiple decision makers**:
   a. **Common goal**: coordination problem
   b. **Own preferences**: game theory

### Game Theory in AI (Two Main Uses)
1. **Agent Design**: Analyze possible decisions assuming rational opponents
2. **Mechanism Design**: Define environment rules so self-interest → collective good

### Game Types
- **Cooperative**: Binding agreements possible
- **Non-Cooperative**: No binding agreements
- **Normal Form**: Simultaneous moves
- **Extensive Form**: Sequential moves (game tree)
- **Perfect Information**: Know position in game tree
- **Imperfect Information**: Uncertain about game state
- **Zero-Sum**: Payoffs add to constant (or zero)
- **Non-Zero-Sum**: General case

### Three Concurrent Execution Models
1. **Interleaved**: Actions from plans are interleaved; must be correct for ALL interleavings
2. **True Concurrency**: Partially ordered; no full serialization
3. **Perfect Synchronization**: Global clock, lockstep execution

### Social Welfare Criteria
1. Pareto optimality (no waste)
2. Utilitarian social welfare (sum of utilities)
3. Egalitarian social welfare (maximin)

### Auction Types
| Type | Description | Dominant Strategy |
|------|-------------|-------------------|
| English (Ascending) | Incremental bidding | Keep bidding while below v_i |
| Sealed-Bid First-Price | Single bid, winner pays own bid | Depends on others' bids |
| Sealed-Bid Second-Price (Vickrey) | Winner pays second-highest | Bid v_i (truthful) |

### Voting Procedures
| Procedure | Description | Properties |
|-----------|-------------|------------|
| Simple Majority | 2 candidates; most votes wins | Simple, common |
| Plurality | Top choice; most votes wins | Ignores lower preferences |
| Borda Count | Score k,...,1 for rankings | Uses full ranking |
| Approval Voting | Approved candidates; most wins | Good for multi-winner |
| Instant Runoff | Eliminate lowest; repeat | Ensures majority |
| True Majority Rule | Pairwise comparisons | Not always decisive |

## 5. Formulas & Equations

### Shapley Value (Equation 18.1)
φ_i(G) = (1/n!) Σ_{p∈P} mc_i(p_i)
where p_i = set of players preceding i in ordering p

### Marginal Contribution
mc_i(C) = ν(C∪{i}) − ν(C)

### MC-Net Value Function
ν(C) = Σ{ x_i | (C_i, x_i) ∈ R and C_i ⊆ C }

### Shapley Value from MC-Nets
φ_i(R) = Σ_{(C,x)∈R, i∈C} x/|C|

### Social Welfare of Coalition Structure
sw(CS) = Σ_{C∈CS} ν(C)

### Zeuthen Risk Measure
risk_t_i = (utility_i loses by conceding and accepting j's offer) / (utility_i loses by not conceding and causing conflict)

### Limit of Means (Repeated Games)
lim_{T→∞} (1/T) Σ_{t=0}^{T} U_t

### Stochastic Dominance Formal (from Ch 16, reused here for completeness)
∀x ∫_{-∞}^{x} p₁(x′)dx′ ≤ ∫_{-∞}^{x} p₂(x′)dx′

## 6. Rules, Laws & Theorems

### Arrow's Theorem
No social welfare function can satisfy all four conditions (Pareto, Condorcet winner, IIA, no dictatorships) for ≥3 outcomes.

### Gibbard-Satterthwaite Theorem
Any social choice function with >2 outcomes satisfying Pareto condition is either manipulable or a dictatorship.

### Revenue Equivalence Theorem
Any auction mechanism where bidders have private values (known distribution) yields same expected revenue.

### Revelation Principle
Any mechanism can be transformed into an equivalent truth-revealing mechanism.

### Nash Folk Theorems
Every outcome where each player receives at least their security value can be sustained as a Nash equilibrium in an infinitely repeated game.

### Subgame Perfect Nash Equilibrium
A strategy profile is subgame perfect if it is a Nash equilibrium in every subgame of the game.

### Every Extensive-Form Game Has at Least One Nash Equilibrium in Pure Strategies
(Proved by backward induction.)

### Nash's Theorem
Every game has at least one Nash equilibrium in mixed strategies.

### von Neumann's Theorem
Every two-player zero-sum game has a maximin equilibrium when mixed strategies are allowed; every Nash equilibrium in a zero-sum game is a maximin for both players.

### Properties of Nash Equilibrium in Zero-Sum
- No other strategy does better against an optimal opponent
- Player continues to do just as well even if strategy revealed to opponent

## 9. Edge Cases/Exceptions/Traps

- **Nontransitive preferences** → money pump (can extract all money cycling A→B→C→A)
- **Prisoner's dilemma**: Dominant strategy equilibrium is only non-Pareto-optimal outcome
- **Multiple Nash equilibria**: Coordination problem (players want to coordinate but can't communicate)
- **No pure Nash equilibrium**: Need mixed strategies (matching pennies)
- **Empty core**: Grand coalition cannot form (three-player superadditive game with |C|≥2 giving 1)
- **BSP trap**: Globally optimal ≠ locally optimal; locally suboptimal action in one MDP can be globally optimal across multiple MDPs
- **Credible threats**: (below,down) Nash equilibrium uses non-credible threat in extensive-form game
- **Infinite negotiations**: Each possible deal has Nash equilibrium in alternating offers without discounting
- **Condorcet paradox**: No candidate wins majority in pairwise comparisons
- **Arrow's theorem**: No perfect voting system for ≥3 candidates
- **Gibbard-Satterthwaite**: Every "reasonable" voting system can be manipulated
- **Coalition structure optimization**: NP-hard (set partitioning problem)
- **Exponential normal form**: For extensive games, normal-form matrix is exponential in information sets
- **Pluribus complexity**: 50 choose 10 ≈ 10 billion possibilities for hidden cards in 6-player poker
- **Abstraction vulnerability**: May make systematic errors approximating equilibrium

## 10. Empirical Evidence/Key Results

- **German 1999 spectrum auction**: Mannesman's 18.18M bid interpreted as signal → tacit collusion with T-Mobile → each got 5 blocks for 20M
- **Pluribus**: Defeated human champions at 6-player Texas hold'em; uses self-play + MCTS + depth-limited search + abstraction
- **Libratus and DeepStack**: Previously defeated champions at heads-up Texas hold'em

## 11. Cross-Chapter Dependencies

- Chapter 5: Minimax, game trees, alpha-beta, expectiminimax, UCT
- Chapter 16: Utility theory, decision theory, off-switch game, unknown preferences (Section 16.7)
- Chapter 17: POMDPs, MDPs
- Chapter 1: Provably beneficial AI (p. 4)
- Section 8.2.8: Database semantics
- Chapter 11: Planning algorithms
- Chapter 22: Reinforcement learning

## 12. Dates & People

- Zermelo (1913) — first formal game theory result
- Emile Borel (1921) — mixed strategies
- von Neumann (1928) — maximin equilibrium (zero-sum)
- von Neumann and Morgenstern (1944) — Theory of Games and Economic Behavior
- John Nash (1950) — Nash equilibrium
- Albert W. Tucker (1950) — prisoner's dilemma
- Shapley (1953a) — Shapley value
- Gillies (1959) — core
- Harsanyi (1967) — Bayes-Nash equilibrium
- Reinhart Selten — subgame perfect equilibrium
- Kenneth Arrow (1951) — Arrow's theorem
- Gibbard and Satterthwaite — Gibbard-Satterthwaite theorem
- William Vickrey (1914–1996) — Vickrey auction
- Hurwicz, Maskin, Myerson (2007 Nobel) — mechanism design
- Myerson (1981); Riley and Samuelson (1981) — revenue equivalence theorem
- Rubinstein (1982) — alternating offers
- Reid Smith (1980) — contract net
- Rosenschein and Zlotkin (1994) — monotonic concession protocol
- Axelrod (1985) — prisoner's dilemma tournaments
- Koller et al. (1996) — sequence form
- Brown and Sandholm (2019) — Pluribus
- Hadfield-Menell et al. (2017a) — assistance games
- Garrett Hardin (1968) — tragedy of the commons
- Elinor Ostrom (1990) — Governing the Commons (Nobel)
- Ronald Coase (1960) — Coase theorem (Nobel)
- Mannesman/T-Mobile (1999) — spectrum auction tacit collusion

## 13. Proof & Argument Patterns

**Backward induction for finitely repeated prisoner's dilemma**:
- Round 100 can have no effect on future rounds → dominant strategy testify
- Given round 100 is determined, round 99 can have no effect → testify
- By induction → testify on every round

**Grim vs. Grim forms Nash equilibrium in infinitely repeated PD**:
- Suppose Ali has beneficial deviation
- At some point she must play testify (otherwise same utility)
- Then Bo's Grim flips to permanent testify
- Ali gets ≤ −5 forever, worse than −1 from Grim
- Contradiction → Grim,Grim is Nash equilibrium

**Maximin for Morra**:
- If E reveals first → O chooses pure strategy → E maximizes at intersection → p=7/12 → value = −1/12
- If O reveals first → E chooses pure → O maximizes at intersection → q=7/12 → value = −1/12
- True utility lies between: −1/12 ≤ U ≤ −1/12 → U = −1/12 exactly

**Shapley value uniqueness**: The only imputation satisfying efficiency, dummy player, symmetry, and additivity axioms.

**Nash folk theorem intuition**: Mutual threat of punishment (Grim) keeps players in line; player who deviates gets punished forever.

## 14. Design Paradigms/Meta-Methods

- **Mechanism design**: Designing rules so self-interest yields collective good
- **Contract net**: Task sharing via announcement/bidding/award
- **Abstraction**: Reduce game tree size by ignoring irrelevant details
- **Sequence form**: Linear representation vs. exponential normal form
- **Self-play**: Pluribus develops baseline strategy entirely from self-play
- **Provably beneficial AI**: Assistance game framework
- **Conventions/Social laws**: Pre-agreed constraints on plan selection
- **Plan recognition**: Executing first part of plan communicates intention

## 15. Case Studies/Classic Examples

### Prisoner's Dilemma
- testifying dominant strategy → both get 5 years; (refuse,refuse) gives 1 year each but unattainable without agreement

### Two-Finger Morra
- Optimal mixed strategy: [7/12:one; 5/12:two] for both players
- Expected value = −1/12 for E (better to be O)

### Doubles Tennis (Figure 18.1)
- Actors A and B, four locations, joint plan required
- Plan 1: A hits ball, B stays; Plan 2: B hits ball, A goes to net
- Coordination problem: must agree on same plan
- Convention "stick to your side" or communication "Mine!"

### Paperclip Game (Figure 18.6)
- Harriet chooses 2 paperclips, 2 staples, or 1 each
- Robbie chooses 90 paperclips, 90 staples, or 50 each
- Equilibrium: Harriet "teaches" Robbie through her choice
- Robbie infers preference range, acts optimally

### German Spectrum Auction (1999)
- 10 blocks, 2 bidders, 10% raise rule
- Mannesman bid 18.18M (10% of 18.18M = 19.99M < 20M)
- Tacit signal: "let's split at 20M" → T-Mobile bid 20M on other 5 blocks

### VCG Example (3 Transceivers, 5 Bidders)
- Bids: 100, 50, 40, 20, 10
- Winners: 100, 50, 40; global utility = 190
- Without 100 → 20 would be winner → 100 pays tax of 20
- Each winner pays 20 (value of first loser)

### Condorcet's Paradox
- 3 voters, 3 outcomes (ωₐ, ω_b, ω_c)
- Preferences: ωₐ>ω_b>ω_c; ω_c>ωₐ>ω_b; ω_b>ω_c>ωₐ
- 2/3 prefer ωₐ > ω_b; ω_b > ω_c; ω_c > ωₐ (cycle)

### Four-Player Coalition Structure Graph (Figure 18.7)
- 15 possible coalition structures for N={1,2,3,4}
- 4 levels: ℓ coalitions in structure
- Searching first 2 levels guarantees worst-case ratio 1/n of optimal

## 16. Ethics
- Machine deference: Robot with uncertainty about human preferences allows itself to be switched off
- Provably beneficial AI: Formal model ensuring AI acts in human interest
- Assistance games: Robbie maximizes Harriet's payoff (not his own)
- Paperclip game: Robbie infers human preferences through observation

## 17. End-of-Chapter Material

### Chapter 18 Summary
1. Multiagent planning necessary with other agents; joint plans need coordination.
2. Game theory describes rational behavior for interacting agents.
3. Solution concepts characterize rational outcomes.
4. Non-cooperative: Nash equilibrium most important.
5. Cooperative: Coalitions, core (stability), Shapley value (fair division).
6. Specialized techniques: contract net, auctions, bargaining, voting.


---

## CHAPTER 19: LEARNING FROM EXAMPLES (lines 28500-31542)

### 1. NAMED ENTITIES — Every Term/Concept with Definition

- **Machine learning**: A computer observes some data, builds a model based on the data, and uses the model as both a hypothesis about the world and a piece of software that can solve problems.
- **Prior knowledge**: Knowledge the agent starts with before learning; this chapter assumes little prior knowledge (starts from scratch).
- **Induction**: Going from a specific set of observations to a general rule; conclusions may be incorrect, unlike deduction.
- **Deduction**: Guaranteed to be correct if premises are correct (see Chapter 7).
- **Classification**: Learning problem where the output is one of a finite set of values (e.g., sunny/cloudy/rainy or true/false).
- **Regression**: Learning problem where the output is a number (integer or real). Also called "function approximation" or "numeric prediction" (though "regression" is the historical term from Francis Galton, 1886).
- **Supervised learning**: Agent observes input-output pairs and learns a function mapping input to output. The output is called a **label**.
- **Unsupervised learning**: Agent learns patterns in input without explicit feedback. Most common task is **clustering**.
- **Reinforcement learning**: Agent learns from a series of reinforcements: rewards and punishments.
- **Training set**: N example input–output pairs (x1, y1), (x2, y2), ..., (xN, yN) generated by unknown function y = f(x).
- **Hypothesis space (H)**: The set of possible functions h that the learning algorithm considers. Also called **model class** or **function class**.
- **Ground truth**: The true answer y_i we ask our model to predict.
- **Exploratory data analysis**: Examining data with statistical tests and visualizations (histograms, scatter plots, box plots) to gain insight.
- **Consistent hypothesis**: A hypothesis h such that each x_i in the training set has h(x_i) = y_i.
- **Test set**: A second sample of (x_i, y_i) pairs used to evaluate how well h handles unseen inputs.
- **Generalization**: How well a hypothesis h predicts outputs of the test set.
- **Bias**: The tendency of a predictive hypothesis to deviate from the expected value when averaged over different training sets. Often results from restrictions imposed by the hypothesis space.
- **Underfitting**: When a hypothesis fails to find a pattern in the data.
- **Variance**: The amount of change in the hypothesis due to fluctuation in the training data.
- **Overfitting**: When a hypothesis pays too much attention to the particular data set it is trained on, causing it to perform poorly on unseen data.
- **Bias–variance tradeoff**: A choice between more complex, low-bias hypotheses that fit training data well and simpler, low-variance hypotheses that may generalize better.
- **Ockham's razor**: "Plurality [of entities] should not be posited without necessity" — attributed to William of Ockham (14th century). Choose the simplest hypothesis that matches the data.
- **Decision tree**: A representation of a function that maps a vector of attribute values to a single output value by performing a sequence of tests from root to leaf.
- **Positive example**: Example where output is true.
- **Negative example**: Example where output is false.
- **Boolean classification**: Classification where outputs are true or false.
- **Noise**: Errors in data (incorrect labels or attribute values); also nondeterminism in the domain.
- **Learning curve**: A plot showing prediction accuracy on the test set as a function of training set size. Also called **happy graphs**.
- **Entropy**: A measure of the uncertainty of a random variable; the fundamental quantity in information theory (Shannon and Weaver, 1949).
- **Information gain**: The expected reduction in entropy from testing an attribute.
- **Decision tree pruning**: Eliminating nodes that are not clearly relevant to combat overfitting.
- **Significance test**: A statistical test beginning with a null hypothesis; if the degree of deviation from the null hypothesis is statistically unlikely (< 5% probability), the pattern is considered significant.
- **Null hypothesis**: The assumption that there is no underlying pattern.
- **χ² pruning**: Pruning decision tree branches based on the chi-squared distribution; if the ∆ value falls below a threshold, the attribute is considered irrelevant and pruned.
- **Early stopping**: Stopping the decision tree algorithm when there is no good attribute to split on (problem: misses XOR-type interactions).
- **Split point**: An inequality test on a continuous attribute value (e.g., Weight > 160).
- **Regression tree**: A tree for predicting numerical outputs; each leaf has a linear function of some subset of numerical attributes rather than a single output value.
- **CART**: Classification And Regression Trees — covers both classification and regression trees.
- **Unstable**: Decision trees are unstable because adding one new example can change the root test and the entire tree.
- **Stationarity assumption**: The assumption that future examples will be like the past; each example has the same prior probability distribution and is independent of previous examples.
- **I.i.d. (independent and identically distributed)**: Examples satisfying P(E_j) = P(E_{j+1}) = ... and P(E_j) = P(E_j | E_{j-1}, E_{j-2}, ...).
- **Error rate**: The proportion of times h(x) ≠ y for an example.
- **Hyperparameters**: Parameters of the model class (not of the individual model), e.g., the threshold for χ² pruning, degree of polynomial.
- **Validation set (development set/dev set)**: A data set used to evaluate candidate models and choose the best one.
- **K-fold cross-validation**: Splitting data into k equal subsets; performing k rounds of learning where 1/k of data is held out as validation set each round.
- **LOOCV (leave-one-out cross-validation)**: Extreme case of k-fold where k = n.
- **Model selection**: Choosing a good hypothesis space (qualitative/subjective and quantitative/empirical).
- **Optimization (training)**: Finding the best hypothesis within a chosen hypothesis space.
- **Interpolated**: A model that exactly fits all the training data (also called "memorized" the data).
- **Small-scale learning**: Traditional methods where training examples range from dozens to low thousands.
- **Large-scale learning**: Learning with millions of examples; generalization loss may be dominated by limits of computation.
- **Loss function L(x, y, ŷ)**: The amount of utility lost by predicting h(x) = ŷ when the correct answer is f(x) = y.
- **L₁ loss (absolute-value loss)**: L₁(y, ŷ) = |y − ŷ|
- **L₂ loss (squared-error loss)**: L₂(y, ŷ) = (y − ŷ)²
- **L₀/₁ loss (0/1 loss)**: L₀/₁(y, ŷ) = 0 if y = ŷ, else 1
- **Generalization loss**: The expected loss over all possible input–output pairs: GenLoss_L(h) = Σ_{(x,y)∈E} L(y, h(x)) P(x,y)
- **Empirical loss**: The average loss on a set of examples E of size N: EmpLoss_{L,E}(h) = Σ_{(x,y)∈E} L(y, h(x)) · 1/N
- **Realizable**: A learning problem is realizable if the hypothesis space H contains the true function f.
- **Regularization**: Explicitly penalizing complex hypotheses to avoid overfitting.
- **Regularization function**: The complexity measure used in regularization.
- **Feature selection**: Discarding attributes that appear to be irrelevant.
- **Minimum description length (MDL)**: A hypothesis that minimizes the total number of bits required to encode the hypothesis plus the data.
- **Hand-tuning**: Manually guessing hyperparameter values based on past experience.
- **Grid search**: Trying all combinations of hyperparameter values systematically.
- **Random search**: Sampling uniformly from the set of all possible hyperparameter settings.
- **Bayesian optimization**: Treating hyperparameter tuning as a machine learning problem itself; uses Gaussian processes and upper confidence bounds.
- **Population-based training (PBT)**: Training a population of models in parallel, then using successful hyperparameter values (with mutation) for subsequent generations (like genetic algorithms).
- **Computational learning theory**: The study of learning algorithms from the perspective of computational and sample complexity; lies at the intersection of AI, statistics, and theoretical computer science.
- **Probably approximately correct (PAC)**: A hypothesis that is likely (probability ≥ 1−δ) to have error ≤ ε, given a sufficient number of training examples.
- **PAC learning algorithm**: Any learning algorithm that returns hypotheses that are probably approximately correct.
- **ε-ball**: The region around the true function f within which approximately correct hypotheses lie.
- **H_bad**: The hypothesis space outside the ε-ball.
- **Sample complexity**: The number of examples required for PAC learning as a function of ε and δ.
- **Decision lists**: A series of tests (conjunctions of literals); if a test succeeds, return a value; if it fails, continue to the next test. Branch only in one direction.
- **k-DL**: Decision list with up to k conjunctions (literals per test).
- **k-DT**: Decision trees of depth at most k.
- **Linear function**: A hypothesis of the form h(x) = w₁x + w₀ (univariate) or h_w(x) = w · x (multivariable).
- **Weights**: Real-valued coefficients w in a linear function; the value of y is changed by changing the relative weight of terms.
- **Weight space**: The space defined by all possible settings of the weights.
- **Linear regression**: Finding the h_w that best fits the data by minimizing squared-error loss.
- **Convex**: The loss function for linear regression with L₂ loss is convex — no local minima.
- **Gradient descent**: Incrementally modifying parameters by moving a small amount in the steepest downhill direction of the loss surface.
- **Learning rate (α)**: The step size parameter in gradient descent.
- **Chain rule**: ∂g(f(x))/∂x = g′(f(x)) ∂f(x)/∂x
- **Batch gradient descent (deterministic gradient descent)**: Update rule summing over all N training examples for each step.
- **Epoch**: A step that covers all the training examples.
- **Stochastic gradient descent (SGD)**: Randomly selects a small number of training examples at each step for updates.
- **Minibatch**: A subset of m out of N examples used in SGD.
- **Online gradient descent**: SGD applied in an online setting where new data arrive one at a time.
- **Multivariable linear regression**: Each example x_j is an n-element vector; hypothesis is h_w(x_j) = w₀ + Σ_i w_i x_{j,i}.
- **Data matrix (X)**: The matrix of inputs with one n-dimensional example per row.
- **Pseudoinverse (X⊤X)⁻¹X⊤**: Used in the normal equation for linear regression.
- **Normal equation**: w* = (X⊤X)⁻¹X⊤y
- **L₁ regularization**: Minimizes sum of absolute values of weights (Σ_i |w_i|); tends to produce sparse models (many zero weights).
- **L₂ regularization**: Minimizes sum of squares of weights (Σ_i w_i²); does not tend to produce zero weights; rotationally invariant.
- **Sparse model**: A model with many weights set to zero, effectively declaring corresponding attributes irrelevant.
- **Decision boundary**: A line (or surface) that separates classes.
- **Linear separator**: A linear decision boundary.
- **Linearly separable**: Data that admit a linear separator.
- **Threshold function**: h_w(x) = 1 if w·x ≥ 0 and 0 otherwise.
- **Perceptron learning rule**: w_i ← w_i + α(y − h_w(x)) × x_i — identical to linear regression update but for 0/1 classification.
- **Training curve**: Measures classifier performance on a fixed training set as learning proceeds one update at a time.
- **Logistic regression**: Fitting weights of a logistic function model to minimize loss on a data set. Uses h_w(x) = Logistic(w·x) = 1/(1+e^{−w·x}).
- **Logistic function (sigmoid)**: Logistic(z) = 1/(1+e^{−z})
- **Parametric model**: A learning model that summarizes data with a set of parameters of fixed size (independent of number of training examples).
- **Nonparametric model**: A model that cannot be characterized by a bounded set of parameters; the number of parameters grows with the data.
- **Instance-based learning / Memory-based learning**: Learning methods that retain all data points as part of the model.
- **Table lookup**: Taking all training examples and putting them in a lookup table; does not generalize well.
- **Nearest neighbors (k-nearest-neighbors)**: Given query x_q, find the k examples nearest to x_q; classification by majority vote, regression by mean/median/linear regression on neighbors.
- **Minkowski distance (L_p norm)**: L_p(x_j, x_q) = (Σ_i |x_{j,i} − x_{q,i}|^p)^{1/p}
- **Euclidean distance (p=2)**: Standard straight-line distance.
- **Manhattan distance (p=1)**: Distance computed as sum of absolute differences along each axis.
- **Hamming distance**: For Boolean attributes, the number of attributes on which two points differ.
- **Normalization**: Rescaling each dimension so values have mean 0 and standard deviation 1: (x_{j,i} − μ_i)/σ_i.
- **Mahalanobis distance**: A distance metric that takes into account covariance between dimensions.
- **Curse of dimensionality**: In high-dimensional spaces, nearest neighbors are usually not very near; volume grows exponentially with dimension.
- **K-d tree (k-dimensional tree)**: A balanced binary tree over data with an arbitrary number of dimensions; splits data along median of a chosen dimension at each level.
- **Locality-sensitive hash (LSH)**: A hash function such that near points have a high probability of hashing to the same bin; used for approximate near-neighbor search.
- **Approximate near-neighbors**: Finding, with high probability, an example point that is near a query point (within distance c·r if a point exists within radius r).
- **Nearest-neighbors regression**: Using k-nearest neighbors for regression (average, linear regression on neighbors, or locally weighted).
- **Locally weighted regression**: At each query point x_q, examples close to x_q are weighted heavily, farther ones less, using a kernel function.
- **Kernel (K)**: A decreasing function of distance with a maximum at 0; K(Distance(x_j, x_q)) gives higher weight to closer examples.
- **Support vector machine (SVM)**: A model class that constructs a maximum margin separator, can use the kernel trick, and is nonparametric (defined by support vectors).
- **Maximum margin separator**: The decision boundary with the largest possible distance to example points.
- **Margin**: Twice the distance from the separator to the nearest example point.
- **Support vectors**: The examples closest to the separator; they "hold up" the separating plane; only these have nonzero α_j weights.
- **Dual representation**: Alternative representation for SVM optimization; data enter only as dot products.
- **Quadratic programming**: The optimization problem type used to solve the SVM dual representation.
- **Kernel function K(x_j, x_k)**: A function that computes dot products in a corresponding feature space without explicitly constructing that space.
- **Polynomial kernel**: K(x_j, x_k) = (1 + x_j·x_k)^d; corresponds to a feature space with dimension exponential in d.
- **Gaussian kernel**: K(x_j, x_k) = e^{−γ|x_j−x_k|²}
- **Mercer's theorem (1909)**: States that any "reasonable" (positive definite) kernel function corresponds to some feature space.
- **Kernel trick**: Plugging kernel functions into SVM equations to find linear separators efficiently in feature spaces with billions or infinite dimensions.
- **Soft margin classifier**: Allows examples to fall on the wrong side of the decision boundary with a penalty proportional to distance required to move them back.
- **Kernelization**: Replacing dot products with a kernel function in any algorithm that works only with dot products.
- **Ensemble learning**: Selecting a collection (ensemble) of hypotheses and combining their predictions by averaging, voting, or another level of machine learning.
- **Base model**: Individual hypotheses in an ensemble.
- **Ensemble model**: The combination of base models.
- **Bagging (bootstrap aggregating)**: Generating K distinct training sets by sampling with replacement from the original training set; training a hypothesis on each; aggregating by voting (classification) or averaging (regression).
- **Random forest**: A form of decision tree bagging that randomly varies attribute choices at each split to make trees more diverse. Uses √n attributes for classification, n/3 for regression.
- **Extremely randomized trees (ExtraTrees)**: Further randomness in selecting split point values: random sample of candidate values from uniform distribution.
- **Out-of-bag error**: Mean error on each example using only trees whose example set didn't include that particular example.
- **Stacked generalization (stacking)**: Combining multiple base models from different model classes trained on the same data; an ensemble model learns to combine their predictions.
- **Boosting**: Ensemble method that generates hypotheses sequentially by reweighting examples; difficult examples get higher weights.
- **Weighted training set**: Each example has an associated weight w_j ≥ 0.
- **Weak learning algorithm**: An algorithm that always returns a hypothesis with accuracy slightly better than random guessing (50% + ε for Boolean classification).
- **AdaBoost**: A specific boosting algorithm (Figure 19.25) that boosts weak learners to fit training data perfectly for large enough K.
- **Decision stump**: A decision tree with just one test (at the root).
- **Gradient boosting / GBM / GBRT**: A form of boosting using gradient descent; adds hypotheses that pay attention to the gradient between right answers and the predictions of previous hypotheses.
- **XGBoost (eXtreme Gradient Boosting)**: Popular implementation of gradient boosting with pruning and regularization, efficient memory management and parallel computation.
- **Online learning**: An agent receives input x_j, predicts y_j, is told correct answer, then repeats; data may not be i.i.d.
- **Randomized weighted majority algorithm**: Keeps track of expert performance, weights predictions by past performance; penalty factor β for mistakes.
- **Regret**: The number of additional mistakes made compared to the best expert in hindsight.
- **No-regret learning**: The average amount of regret per trial tends to 0 as the number of trials increases.
- **Semi-supervised learning**: Given a few labeled examples and many unlabeled examples.
- **Weakly supervised learning**: Using labels that are noisy, imprecise, or supplied by non-experts.
- **ImageNet**: Freely available image data set with over 14 million photos and about 20,000 labels.
- **Data provenance**: Recording for each column the exact definition, source, possible values, and who has worked on it.
- **Federated learning**: Data stays on user's device; model parameters are shared without revealing private data.
- **Data augmentation**: Creating multiple versions of each image by rotating, translating, cropping, scaling, changing brightness/color balance, or adding noise.
- **Unbalanced classes**: When data are plentiful but classes are imbalanced (e.g., 10M valid vs. 1000 fraudulent transactions).
- **Undersampling**: Ignoring some majority class examples.
- **Over-sampling**: Duplicating minority class examples.
- **SMOTE**: Synthetic data generation technique for balancing classes (Chawla et al., 2002).
- **ADASYN**: Another synthetic data generation technique (He et al., 2008).
- **Outlier**: A data point far from other points.
- **One-hot encoding**: Transforming categorical attributes into separate Boolean attributes, exactly one of which is true.
- **Feature engineering**: Creating new attributes based on domain knowledge; critical to success of ML projects.
- **t-distributed stochastic neighbor embedding (t-SNE)**: A dimensionality reduction technique that maps high-dimensional data to 2D while preserving neighborhood relationships.
- **False positive**: Labeling a legitimate item as positive (e.g., legitimate email as spam).
- **Receiver operating characteristic (ROC) curve**: Plots false positives versus true positives for each hyperparameter value.
- **AUC**: Area under the ROC curve; single-number summary of the ROC curve.
- **Confusion matrix**: A two-dimensional table of counts of how often each category is classified/misclassified as each other category.
- **Interpretability**: The ability to inspect the actual model and understand why it got a particular answer and how the answer would change when input changes.
- **Explainability**: The ability of a separate process (explanation module) to summarize what a model does, especially for black-box models.
- **LIME (Local Interpretable Model-agnostic Explanations)**: Builds an interpretable model (decision tree or linear model) approximating the black-box model by probing with random inputs.
- **SHAP (Shapley Additive exPlanations)**: Uses Shapley values to determine the contribution of each feature.
- **Long tail**: The problem of user inputs that were never tested before.
- **Nonstationarity**: The world changes over time; models must be updated.
- **VC dimension**: A measure roughly analogous to ln|H| from PAC analysis; can be applied to continuous function classes.
- **Kolmogorov complexity (algorithmic complexity)**: The length of the shortest program for a universal Turing machine that correctly reproduces observed data.
- **Automated machine learning (AutoML)**: Applying machine learning to the task of solving machine learning problems.
- **Metalearning / MAML (Model-Agnostic Meta-Learning)**: Training a core model so it can be easily fine-tuned with new data on new tasks.
- **Condorcet's jury theorem (1785)**: If jurors are independent and each has ≥ 50% chance of deciding correctly, more jurors improve the chance of correctness.
- **Bootstrap**: In statistics, a sample with replacement.
- **Hypothesis Boosting Problem**: Given a learner that predicts only slightly better than random, is it possible to derive a learner that performs arbitrarily well? (posed by Kearns, 1988; answered affirmatively by Schapire, 1990)
- **No free lunch theorem (Wolpert and Macready, 1997)**: If a learning algorithm performs well on a certain set of problems, it will perform poorly on a different set.

### 2. PROCESSES / ALGORITHMS — Step-by-Step Procedures

**LEARN-DECISION-TREE (Figure 19.5, page 673)**
```
function LEARN-DECISION-TREE(examples, attributes, parent_examples) returns a tree
  if examples is empty then return PLURALITY-VALUE(parent_examples)
  else if all examples have the same classification then return the classification
  else if attributes is empty then return PLURALITY-VALUE(examples)
  else
    A ← argmax_{a∈attributes} IMPORTANCE(a, examples)
    tree ← a new decision tree with root test A
    for each value v of A do
      exs ← {e: e ∈ examples and e.A = v}
      subtree ← LEARN-DECISION-TREE(exs, attributes − A, examples)
      add a branch to tree with label (A=v) and subtree subtree
    return tree
```

**Decision tree recursive cases (4 cases, page 672)**
1. If remaining examples are all positive (or all negative) → answer Yes/No
2. If some positive and some negative → choose best attribute to split them
3. If no examples left → return most common output value from parent's examples
4. If no attributes left but both positive and negative examples (noise/nondeterminism) → return most common output value

**MODEL-SELECTION (Figure 19.8, page 680)**
```
function MODEL-SELECTION(Learner, examples, k) returns a (hypothesis, error rate) pair
  err ← an array, indexed by size, storing validation-set error rates
  training set, testset ← a partition of examples into two sets
  for size = 1 to ∞ do
    err[size] ← CROSS-VALIDATION(Learner, size, training set, k)
    if err is starting to increase significantly then
      best size ← the value of size with minimum err[size]
      h ← Learner(best size, training set)
      return h, ERROR-RATE(h, testset)

function CROSS-VALIDATION(Learner, size, examples, k) returns error rate
  N ← number of examples
  errs ← 0
  for i = 1 to k do
    validation set ← examples[(i−1)×N/k : i×N/k]
    training set ← examples − validation set
    h ← Learner(size, training set)
    errs ← errs + ERROR-RATE(h, validation set)
  return errs/k
```

**DECISION-LIST-LEARNING (Figure 19.11, page 689)**
```
function DECISION-LIST-LEARNING(examples) returns a decision list, or failure
  if examples is empty then return the trivial decision list No
  t ← a test that matches a nonempty subset examples_t of examples
       such that the members of examples_t are all positive or all negative
  if there is no such t then return failure
  if the examples in examples_t are positive then o ← Yes else o ← No
  return a decision list with initial test t and outcome o and remaining tests given by
         DECISION-LIST-LEARNING(examples − examples_t)
```

**ADABOOST (Figure 19.25, page 715)**
```
function ADABOOST(examples, L, K) returns a hypothesis
  inputs: examples (N labeled examples (x₁,y₁),...,(x_N,y_N))
          L (a learning algorithm), K (number of hypotheses)
  local: w (N example weights, initially all 1/N)
         h (K hypotheses), z (K hypothesis weights)
         ε ← a small positive number
  for k = 1 to K do
    h[k] ← L(examples, w)
    error ← 0
    for j = 1 to N do
      if h[k](x_j) ≠ y_j then error ← error + w[j]
    if error > 1/2 then break from loop
    error ← min(error, 1−ε)
    for j = 1 to N do
      if h[k](x_j) = y_j then w[j] ← w[j] · error/(1−error)
    w ← NORMALIZE(w)
    z[k] ← ½ log((1−error)/error)
  return Function(x): Σ z_i h_i(x)
```

**Gradient descent (page 691)**
```
w ← any point in the parameter space
while not converged do:
  for each w_i in w do:
    w_i ← w_i − α ∂/∂w_i Loss(w)
```

**Perceptron learning rule (page 696)**
For a single example (x, y):
  w_i ← w_i + α(y − h_w(x)) × x_i

**Randomized weighted majority algorithm (page 717)**
```
Initialize weights {w₁,...,w_K} all to 1
for each problem to be solved:
  1. Receive predictions {ŷ₁,...,ŷ_K} from experts
  2. Randomly choose expert k* in proportion to its weight: P(k) = w_k
  3. Yield ŷ_{k*} as answer
  4. Receive correct answer y
  5. For each expert k such that ŷ_k ≠ y: update w_k ← β w_k
  6. Normalize weights so Σ w_k = 1
```

**Maximum-likelihood parameter learning method (page 738)**
1. Write down expression for likelihood of data as function of parameter(s)
2. Write down derivative of log likelihood with respect to each parameter
3. Find parameter values such that derivatives are zero

**EM algorithm general form (page 758)**
θ^{(i+1)} = argmax_θ Σ_z P(Z=z | x, θ^{(i)}) L(x, Z=z | θ)
- E-step: compute expected values of hidden variables given current parameters
- M-step: maximize log likelihood with respect to parameters using expected values

**EM for mixtures of Gaussians (page 753)**
Initialize parameters arbitrarily, then iterate:
- E-step: Compute p_{ij} = P(C=i | x_j) = α P(x_j | C=i) P(C=i). Define n_i = Σ_j p_{ij}
- M-step: μ_i ← Σ_j p_{ij} x_j / n_i; Σ_i ← Σ_j p_{ij} (x_j−μ_i)(x_j−μ_i)^⊤ / n_i; w_i ← n_i/N

### 3. HIERARCHIES / CLASSIFICATIONS

**Three types of learning (by feedback):**
- Supervised learning (input-output pairs, labels)
- Unsupervised learning (no feedback; clustering)
- Reinforcement learning (rewards and punishments)

**Components of an agent that can be learned (from Chapter 2):**
1. Direct mapping from state to actions (condition-action rules)
2. Means to infer relevant properties from percept sequence
3. Information about world evolution and action results
4. Utility information (desirability of world states)
5. Action-value information (desirability of actions)
6. Goals (most desirable states)
7. Problem generator, critic, and learning element

**Types of loss functions:**
- L₀/₁ loss: 0 if correct, 1 if incorrect
- L₁ loss (absolute-value): |y − ŷ|
- L₂ loss (squared-error): (y − ŷ)²

**Types of regularization:**
- L₁ regularization: Σ_i |w_i| (sparse, not rotationally invariant)
- L₂ regularization: Σ_i w_i² (not sparse, rotationally invariant)

**Three approaches to learning (from most to least complex):**
1. Bayesian learning (use all hypotheses weighted by posterior)
2. MAP learning (use single most probable hypothesis)
3. Maximum-likelihood learning (assume uniform prior, maximize P(d|h))

**Model classes covered in Ch 19:**
- Decision trees / Decision lists / CART
- Linear models (univariate/multivariable regression)
- Nonparametric models (nearest neighbors, k-d trees, LSH, locally weighted regression)
- Support vector machines (maximum margin, kernel trick)
- Ensemble models (bagging, random forests, stacking, boosting, gradient boosting)
- Logistic regression
- Neural networks (Chapter 21)

**Types of regression:**
- Univariate linear regression (one input variable)
- Multivariable linear regression (multiple input variables, single output)
- Multivariate regression (multiple output variables)
- Nonparametric regression (nearest neighbors, locally weighted)
- Regression trees

### 4. COMPARISONS / TRADE-OFFS

- **Bias vs. Variance tradeoff**: Complex, low-bias hypotheses fit training data well but may overfit; simpler, low-variance hypotheses generalize better.
- **Expressiveness vs. computational complexity tradeoff**: More expressive hypothesis spaces are harder to search (fitting Turing machines is undecidable).
- **L₁ vs. L₂ regularization**: L₁ tends to produce sparse models (zero weights); L₂ is rotationally invariant and does not zero out weights. Number of examples required: linear in irrelevant features for L₂, logarithmic for L₁.
- **Batch GD vs. SGD**: Batch GD sums over all N examples per step (slow but guaranteed convergence); SGD uses minibatch (faster, may oscillate).
- **Parametric vs. Nonparametric**: Parametric models have fixed-size parameters; nonparametric models grow with data.
- **Decision trees vs. decision lists (Figure 19.12)**: Decision trees learn slightly faster on restaurant problem, but have more variation; both >90% accurate after 100 trials.
- **Decision trees vs. naive Bayes (Figure 20.3)**: Decision tree learns better on restaurant problem; naive Bayes does surprisingly well given its simplicity.
- **Generative vs. Discriminative models (Section 20.2.3)**: Discriminative models focus on decision boundary (tend to do better with large data); generative models model each class distribution (tend to do better with small data). On 15 data sets: discriminative better on 9/15 with max data, generative better on 14/15 with small data (Ng and Jordan, 2002).
- **Perceptron vs. Logistic regression**: Perceptron has discontinuous hard threshold → unpredictable learning, no convergence guarantee for nonseparable data; logistic regression has continuous soft threshold → predictable convergence, works well with noisy data.
- **Early stopping vs. Pruning**: Early stopping fails on XOR-type problems (no single good attribute); generate-and-then-prune handles this correctly.
- **Bayesian vs. MAP learning**: Bayesian uses all hypotheses weighted by posterior (optimal but expensive); MAP uses single best hypothesis (tractable but overconfident with small data).
- **MAP vs. Maximum-likelihood**: MAP uses prior to penalize complexity; ML assumes uniform prior (good approximation with large data, problems with small data).
- **Random forests vs. decision trees**: Random forests are more resistant to overfitting; error converges as trees are added (Breiman, 2001); they need no pruning.
- **Shallow models vs. deep networks (Figure 21.1)**: Shallow models (linear regression) have short computation paths; deep networks have long paths allowing complex interactions.

### 5. FORMULAS & EQUATIONS

**Entropy:**
H(V) = Σ_k P(v_k) log₂(1/P(v_k)) = −Σ_k P(v_k) log₂ P(v_k)

**Boolean entropy:**
B(q) = −(q log₂ q + (1−q) log₂ (1−q))

**Information gain:**
Gain(A) = B(p/(p+n)) − Remainder(A)
Remainder(A) = Σ_{k=1}^{d} (p_k+n_k)/(p+n) · B(p_k/(p_k+n_k))

**χ² deviation:**
∆ = Σ_{k=1}^{d} [(p_k − p̂_k)²/p̂_k + (n_k − n̂_k)²/n̂_k]
where p̂_k = p × (p_k+n_k)/(p+n), n̂_k = n × (p_k+n_k)/(p+n)

**PAC sample complexity bound (Equation 19.1):**
N ≥ (1/ε)(ln(1/δ) + ln|H|)

**k-DL sample complexity:**
|k-DL(n)| = 2^{O(n^k log₂(n^k))}
N ≥ (1/ε)(ln(1/δ) + O(n^k log₂(n^k)))

**Univariate linear regression (Equation 19.3):**
w₁ = [N(Σ x_j y_j) − (Σ x_j)(Σ y_j)] / [N(Σ x_j²) − (Σ x_j)²]
w₀ = (Σ y_j − w₁(Σ x_j)) / N

**Gradient descent update (Equation 19.4):**
w_i ← w_i − α ∂/∂w_i Loss(w)

**Loss for univariate linear regression:**
Loss(h_w) = Σ_{j=1}^{N} (y_j − (w₁ x_j + w₀))²

**Gradient for one training example (Equation 19.5):**
∂/∂w_i Loss(w) = 2(y − h_w(x)) × ∂/∂w_i (y − h_w(x))

**Univariate regression update (one example):**
w₀ ← w₀ + α(y − h_w(x))
w₁ ← w₁ + α(y − h_w(x)) × x

**Multivariable regression update (Equation 19.6):**
w_i ← w_i + α Σ_j (y_j − h_w(x_j)) × x_{j,i}

**Normal equation (Equation 19.7):**
w* = (X^T X)^{-1} X^T y

**Regularized total cost:**
Cost(h) = EmpLoss(h) + λ · Complexity(h)

**L_q regularization:**
Complexity(h_w) = L_q(w) = Σ_i |w_i|^q

**Perceptron update (Equation 19.8):**
w_i ← w_i + α(y − h_w(x)) × x_i

**Logistic function:**
Logistic(z) = 1/(1+e^{−z})

**Logistic regression hypothesis:**
h_w(x) = Logistic(w·x) = 1/(1+e^{−w·x})

**Logistic regression gradient (Equation 19.9):**
w_i ← w_i + α(y − h_w(x)) × h_w(x)(1−h_w(x)) × x_i

**SVM dual objective (Equation 19.10):**
argmax_α Σ_j α_j − ½ Σ_{j,k} α_j α_k y_j y_k (x_j·x_k)
subject to α_j ≥ 0 and Σ_j α_j y_j = 0

**SVM separator (Equation 19.11):**
h(x) = sign(Σ_j α_j y_j (x·x_j) − b)

**Minkowski distance (L_p norm):**
L_p(x_j, x_q) = (Σ_i |x_{j,i} − x_{q,i}|^p)^{1/p}

**Neighborhood volume in high dimensions:**
ℓ = (k/N)^{1/n}

**β bound for weighted majority:**
M < [M* ln(1/β) + ln K] / (1−β)

### 6. RULES, LAWS & THEOREMS

- **Ockham's razor**: "Plurality [of entities] should not be posited without necessity" — choose the simplest hypothesis that matches the data.
- **Stationarity assumption**: Future examples will be drawn from the same fixed distribution as past examples (P(E) = P(X,Y) doesn't change).
- **PAC learning theorem**: Any hypothesis that is consistent with a sufficiently large set of training examples is unlikely to be seriously wrong (probably approximately correct).
  - With probability ≥ 1−δ, after seeing N ≥ (1/ε)(ln(1/δ)+ln|H|) examples, a consistent hypothesis will have error ≤ ε.
- **Mercer's theorem (1909)**: Any "reasonable" (positive definite) kernel function corresponds to some feature space.
- **No free lunch theorem (Wolpert and Macready, 1997)**: If a learning algorithm performs well on a certain set of problems, it will perform poorly on a different set.
- **Condorcet's jury theorem (1785)**: If jurors are independent and individual juror has ≥ 50% chance of being correct, more jurors → better chance of correct decision.
- **Universal approximation theorem**: A network with two layers (first nonlinear, second linear) can approximate any continuous function to arbitrary accuracy.
- **Bias–variance tradeoff**: More complex models have lower bias but higher variance; simpler models have higher bias but lower variance.
- **Convexity of linear regression loss**: The loss function for linear regression with L₂ loss is convex, implying no local minima.
- **Hume's problem of induction**: Generalizing from examples admits possibility of errors, unlike logical deduction.
- **Einstein's principle**: "The supreme goal of all theory is to make the irreducible basic elements as simple and as few as possible without having to surrender the adequate representation of a single datum of experience."
- **Breiman's random forest convergence proof**: As you add more trees to a random forest, the error converges; it does not grow (in almost all cases).
- **AdaBoost boosting property**: If the base learner is a weak learning algorithm (accuracy > 50%+ε), AdaBoost will return a hypothesis that classifies training data perfectly for large enough K.
- **Convergence conditions for SGD learning rate**: Σ_{t=1}^{∞} α(t) = ∞ and Σ_{t=1}^{∞} α²(t) < ∞ (e.g., α(t) = O(1/t)).
- **Bayesian optimality**: Given the hypothesis prior, any other prediction is expected to be correct less often than the Bayesian prediction.
- **Bayesian convergence**: For any fixed prior that does not rule out the true hypothesis, posterior probability of false hypotheses eventually vanishes.

### 7. DATA STRUCTURES & TYPES

- **Factored representation**: A vector of attribute values (each example is a vector).
- **Training set**: N input–output pairs (x₁,y₁),...,(x_N,y_N).
- **Test set**: A held-out sample for final evaluation.
- **Validation set (dev set)**: Held-out data for model selection and hyperparameter tuning.
- **Decision tree**: Tree with internal nodes (attribute tests), branches (attribute values), and leaves (output values).
- **Decision list**: Series of tests (conjunctions of literals) with outcomes; branches only in one direction.
- **Data matrix (X)**: Matrix of inputs with one n-dimensional example per row.
- **Weight vector (w)**: Coefficients in linear models.
- **Weight matrix (W)**: Matrix of weights in neural networks (first layer W^(1), second layer W^(2), etc.).
- **Computation graph / Dataflow graph**: A circuit representation where each node represents an elementary computation.
- **k-d tree**: Balanced binary tree splitting data along median of chosen dimension at each level.
- **Hash tables (LSH)**: Multiple hash tables with random projections for approximate near-neighbor search.
- **Confusion matrix**: 2D table of counts of classification results.
- **ROC curve**: Plot of false positives vs. true positives.
- **Bayesian network**: Graphical model with nodes as random variables, edges as dependencies, used in Chapter 20.

### 8. VISUAL PATTERNS

- **Figure 19.1 (page 667)**: Four plots of best-fit functions from four hypothesis spaces (lines, sinusoids, piecewise-linear, degree-12 polynomials) on two slightly different data sets. Shows bias-variance tradeoff.
- **Figure 19.2 (page 670)**: Restaurant domain training set table with 12 examples and 10 attributes.
- **Figure 19.3 (page 671)**: Decision tree for deciding whether to wait for a table (SR's actual decision tree).
- **Figure 19.4 (page 672)**: Splitting examples by testing on Type (poor split) vs. Patrons (good split).
- **Figure 19.6 (page 673)**: Decision tree induced from 12-example training set (learning algorithm's output).
- **Figure 19.7 (page 674)**: Learning curve for decision tree learning on restaurant problem — accuracy increases with training set size, reaching ~95%.
- **Figure 19.9 (page 681)**: Error rates vs. model complexity: (a) U-shaped validation error curve for decision trees (optimal at size 7); (b) decreasing validation error for CNNs on MNIST (optimal at 1M parameters).
- **Figure 19.10 (page 687)**: Decision list for restaurant problem.
- **Figure 19.12 (page 689)**: Learning curve comparing decision list vs. decision tree on restaurant data.
- **Figure 19.13 (page 691)**: (a) House price vs. size data with linear regression line y=0.232x+246; (b) convex loss function surface.
- **Figure 19.14 (page 694)**: Why L₁ regularization gives sparse model (diamond/box contours intersect on axis) vs. L₂ (circle contours, no preference for zero).
- **Figure 19.15 (page 695)**: Seismic data: earthquakes vs. explosions (a) linearly separable; (b) same domain with more data, not separable.
- **Figure 19.16 (page 697)**: Perceptron training curves: (a) converges on separable data; (b) fails to converge on noisy data; (c) with learning rate schedule, better convergence.
- **Figure 19.17 (page 698)**: (a) Hard threshold; (b) Logistic function (sigmoid); (c) Logistic regression hypothesis surface.
- **Figure 19.18 (page 699)**: Logistic regression training curves — faster and more reliable than perceptron, especially on noisy data.
- **Figure 19.19 (page 700)**: k-nearest-neighbors: (a) k=1 overfits; (b) k=5 better.
- **Figure 19.20 (page 703)**: Nonparametric regression models: (a) connect-the-dots; (b) 3-nearest-neighbor average; (c) 3-nearest-neighbor linear regression; (d) locally weighted regression with quadratic kernel.
- **Figure 19.21 (page 706)**: SVM: (a) three candidate linear separators; (b) maximum margin separator with support vectors.
- **Figure 19.22 (page 708)**: (a) Non-separable 2D circular data; (b) Data mapped to 3D feature space becomes linearly separable.
- **Figure 19.23 (page 709)**: Ensemble of three linear thresholds creates triangular region not expressible by single linear hypothesis.
- **Figure 19.24 (page 714)**: Boosting illustration: example weights increase for misclassified examples.
- **Figure 19.26 (page 716)**: (a) Boosted vs. unboosted decision stumps; (b) Training/test accuracy vs. K (number of hypotheses) — test accuracy improves even after training reaches zero error.
- **Figure 19.27 (page 722)**: t-SNE map of MNIST digit data set — clusters for 10 digits visible.
- **Figure 19.28 (page 726)**: ML test criteria rubric (abridged from Breck et al., 2016): 28 tests across four categories (Features/Data, Model Development, ML Infrastructure, Monitoring).

### 9. EDGE CASES / EXCEPTIONS / TRAPS

- **Majority function**: Cannot be concisely represented as a decision tree (exponentially large).
- **Parity function**: Cannot be concisely represented as a decision tree (exponentially large).
- **Diagonal decision boundary (y > A₁ + A₂)**: Hard for decision trees because all tests are axis-aligned.
- **No free lunch**: A learning algorithm that performs well on one problem will perform poorly on another.
- **Undecidable hypothesis space**: Fitting Turing machines is undecidable; even the hypothesis space of all computer programs is too large.
- **XOR problem**: No single attribute is informative, but combinations are — early stopping fails here.
- **SGD may not converge**: With nonconvex loss surfaces or wrong learning rate, SGD can oscillate.
- **Perceptron may not converge**: For nonseparable data with fixed α, perceptron rule keeps changing weights.
- **Perceptron minimum-error solution is NP-hard**: Finding minimum-error linear separator is computationally hard.
- **Zero probability in ML with small data**: If an event hasn't been observed, maximum-likelihood assigns zero probability; fix by initializing counts to 1.
- **Curse of dimensionality**: In 200 dimensions, nearest neighbors are 94% of the edge length away; almost all points are outliers.
- **Overfitting high-degree polynomials**: A degree-12 polynomial perfectly fits 13 points but generalizes poorly.
- **High-capacity models and overfitting**: Some model classes (like deep networks) continue to improve after interpolation; others (like decision trees) exhibit U-shaped validation error.
- **Degenerate local maxima in EM**: Gaussian component can shrink to cover single data point (variance → 0, likelihood → ∞); components can merge.
- **Non-identifiability**: Two observationally equivalent models may exist (e.g., Bag variable flipped).
- **Two-attribute mixture model**: With only two attributes (vs. three), not enough observed counts to recover mixture parameters.
- **Unbalanced classes**: 99.99% accuracy can be trivial (always predict majority class); need weighting/undersampling/oversampling.
- **Outliers affect linear regression**: Single outlier can change all global linear model parameters; decision trees/forests handle outliers better.
- **Validation set overfitting**: If you run too many experiments on the same validation set, you risk overfitting to it.
- **Explanation false security**: Simple explanations can lead to a false sense of security for inherently complex problems.

### 10. EMPIRICAL EVIDENCE / KEY RESULTS

- **Gravitational lensing speedup**: ML model sped up analysis by factor of 10 million (Hezaveh et al., 2017).
- **Data center cooling**: ML model reduced energy use by 40% (Gao, 2014).
- **Restaurant learning curve**: Decision tree reaches ~95% accuracy on restaurant problem with 100 examples.
- **Decision tree optimal size**: 7 nodes optimal for restaurant problem (Figure 19.9(a)).
- **CNN on MNIST**: Optimal number of parameters ~1,000,000 (Figure 19.9(b)).
- **Perceptron convergence**: Takes 657 steps on average for 63-example seismic data set (~10 presentations per example).
- **Restaurant decision tree (learned)**: Uses Patrons, Hungry, Fri/Sat, Type; ignores Raining, Reservation.
- **LSH speedup**: On 13M Web images with 512 dimensions, LSH examines only ~few thousand images to find nearest neighbors — 1000x speedup over exhaustive/k-d tree (Torralba et al., 2008).
- **Random forest efficiency**: With 3 CPUs, a forest of 100 trees can be built in same time as a single decision tree (100-attribute problem, per Cutler).
- **Ensemble independence example**: 5 classifiers each 75% correct → 89% majority vote correct; 17 classifiers → 99% (under independence assumption).
- **AdaBoost on restaurant**: K=5 boosted stumps reach 93% after 100 examples (vs. 81% for unboosted stumps).
- **AdaBoost interpolation**: Error reaches zero on training set at K=20; test accuracy continues improving up to K=137 (0.98 accuracy).
- **Bagging vs. no bagging**: Bagging 5 classifiers correct 89% of cases vs. single classifier 80% (idealized).
- **Generative vs. discriminative comparison**: On 15 small data sets, generative naive Bayes better on 14/15 with small data; discriminative logistic regression better on 9/15 with max data (Ng and Jordan, 2002).
- **Bayesian candy example**: After 3 lime candies, MAP predicts 100% lime; Bayesian predicts 80% lime.
- **EM for candy mixture**: Learned model after 10 iterations fits better (L=−1982.214) than original true model (L=−1982.5).
- **Four-parameter elephant**: "With four parameters I can fit an elephant, and with five I can make him wiggle his trunk" — von Neumann (quoted by Dyson, 2004). Proved correct by Mayer et al. (2010).
- **Data growth**: ~5 exabytes (5×10¹⁸ bytes) produced in 2002, doubling every 3 years; 2×10²¹ bytes for 2007 (Hilbert and Lopez, 2011).

### 11. CROSS-CHAPTER DEPENDENCIES

- **Chapter 2 (Agent designs)**: Lists 7 components of agents that can be learned — referenced in Section 19.1.
- **Chapter 7 (Logical agents)**: Deduction vs. induction — referenced in Section 19.1.
- **Chapter 8 (First-order logic)**: Expressive language allows simple hypotheses — referenced in Section 19.2 (expressiveness–complexity tradeoff).
- **Chapter 12 (Probability)**: Uncertainty and probability — foundational for Chapter 20.
- **Chapter 13 (Probabilistic reasoning)**: Logistic function, probit model, logit model (page 424) — referenced in Section 19.6.5.
- **Section 14.4 (Bayesian networks)**: Parameter learning with Gaussian distributions — referenced in Section 20.2.6.
- **Chapter 16 (Decision theory)**: Utility maximization — referenced in loss function discussion (Section 19.4.2).
- **Chapter 21 (Deep learning)**: Deep neural networks, convolutional networks — previewed as more complex model class (Section 19.3.2, 19.6.2); transfer learning (Section 21.7.2) referenced.
- **Section 4.2 (Hill climbing)**: Gradient descent/continuous optimization — referenced in Sections 19.6.2 and 20.2.1.
- **Section 5.4 (Monte Carlo tree search)**: Upper confidence bounds — referenced in Bayesian optimization (Section 19.4.4).
- **Section 4.1.4 (Genetic algorithms)**: Population-based methods — referenced in PBT (Section 19.4.4).
- **Chapter 22 (Reinforcement learning)**: Referenced in listing of deep learning applications.
- **Section 27.3.2 (Privacy)**: Privacy concerns in data collection — referenced in Section 19.9.2.
- **Section 27.3.3 (Fairness)**: Bias and fairness — referenced in Section 19.9.2.
- **Chapter 14 HMMs**: Forward-backward algorithm — used in Section 20.3.3 for learning HMM parameters via EM.

### 12. DATES & PEOPLE

- **Albert Einstein**: Quoted on simplicity in theory (1933).
- **William of Ockham (1280–1349)**: Ockham's razor — "Plurality should not be posited without necessity."
- **Francis Galton (1886)**: Introduced "regression lines" and concept of regression to the mean.
- **Claude Shannon (with Weaver, 1949)**: Information theory, entropy.
- **Alan Turing (1947)**: Anticipated machine learning — "machines with initial instruction tables that might modify those tables."
- **Arthur Samuel (1959)**: Defined machine learning as "field of study that gives computers the ability to learn without being explicitly programmed"; created learning checkers program.
- **David Hume (1711–1776)**: Formulated the problem of induction; proposed principle of uniformity of nature.
- **Aristotle (350 BCE)**: "For the more limited, if adequate, is always preferable" — in Physics, Book I, Chapter VI.
- **John von Neumann**: Quoted on fitting an elephant with four parameters (later proved by Mayer et al., 2010).
- **Richard Bellman (1961)**: Coined term "curse of dimensionality."
- **Leslie Valiant (1984)**: Inaugurated PAC learning theory.
- **Leo Breiman (2001)**: Proved random forest error converges; co-developed CART (Breiman et al., 1984).
- **Ross Quinlan**: Developed ID3 (1979), C4.5 (1993); introduced entropy-based attribute selection and χ² pruning.
- **Edward Feigenbaum (1961)**: EPAM — first notable use of decision trees.
- **Vapnik and Chervonenkis (1971)**: Uniform convergence theory; VC dimension.
- **Tikhonov (1963)**: Regularization procedure.
- **Legendre (1805) and Gauss (1809)**: Linear regression with squared error loss; Gauss claimed use since 1795.
- **Pierre-François Verhulst (1804–1849)**: Developed the logistic function (courbe logistique) for population growth.
- **Newton (1671) and Raphson (1690)**: Newton–Raphson method for logistic regression optimization.
- **Cauchy (1847)**: Gradient descent.
- **Robbins and Monro (1951)**: Stochastic gradient descent.
- **Rosenblatt (1960)**: Perceptron; rediscovered SGD for neural networks.
- **Fix and Hodges (1951)**: Nearest-neighbors models.
- **Gionis et al. (1999)**: Locality-sensitive hashing (LSH).
- **Boser, Guyon, Vapnik (1992)**: Full SVM theory development.
- **Cortes and Vapnik (1995)**: Soft-margin classifier (won 2008 ACM Theory and Practice Award).
- **Platt (1999)**: Sequential Minimal Optimization (SMO) for SVMs.
- **Schapire (1990)**: Answer to Hypothesis Boosting Problem; AdaBoost (Freund and Schapire, 1996).
- **Friedman (2001)**: Introduced Gradient Boosting Machine (GBM).
- **Chen and Guestrin (2016)**: XGBoost.
- **Ho (1995)**: First random forest algorithm (random attribution selection).
- **Amit and Geman (1997)**: Independent random forest version.
- **Hyaﬁl and Rivest (1976)**: Proved optimal decision tree finding is NP-complete.
- **Bertsimas and Dunn (2017)**: 800 billion-fold speedup in hardware+algorithms makes some NP-hard decision tree problems tractable.
- **Kearns (1990)**: Showed some concept classes cannot be PAC-learned tractably.
- **Rivest (1987)**: Decision lists PAC-learnable.
- **Blumer, Ehrenfeucht, Haussler, Warmuth (1989)**: Connected PAC-learning and VC theory.
- **Wolpert and Macready (1997) / Wolpert (2013)**: No free lunch theorem.
- **Ng (2004)**: L₁ vs. L₂ regularization analysis.
- **Domingos (2012)**: "Easily the most important factor is the features used."
- **Breck et al. (2016)**: 28-test checklist for ML deployment.
- **Ribeiro et al. (2016)**: LIME system.
- **Lundberg and Lee (2018)**: SHAP system.
- **Doshi-Velez and Kim (2017)**: Framework for interpretable ML / XAI.
- **Finn et al. (2017)**: MAML (Model-Agnostic Meta-Learning).
- **Hutter et al. (2019)**: AutoML overview.
- **Gold (1967)**: Identification in the limit.
- **Solomonoff (1964, 2009) and Kolmogorov (1965)**: Kolmogorov complexity.
- **Rissanen (1984, 2007)**: Minimum description length (MDL).
- **Larson (1931)**: First cross-validation; Stone (1974) and Golub et al. (1979): modern forms.
- **Zhang et al. (2016)**: Analysis of model memorization with random data.
- **Belkin et al. (2019)**: Bias–variance tradeoff and interpolation point.

### 13. PROOF & ARGUMENT PATTERNS

- **PAC sample complexity proof (pages 686-687)**:
  1. Define error(h) = probability h misclassifies new example
  2. Define ε-ball around true function f; H_bad is outside ε-ball
  3. For h_b ∈ H_bad: error(h_b) > ε, so P(h_b agrees with one example) ≤ 1−ε
  4. P(h_b agrees with N examples) ≤ (1−ε)^N
  5. P(H_bad contains consistent hypothesis) ≤ |H_bad|(1−ε)^N ≤ |H|(1−ε)^N
  6. Set ≤ δ; use 1−ε ≤ e^{−ε}
  7. N ≥ (1/ε)(ln(1/δ) + ln|H|)

- **k-DL learnability proof (pages 688-689)**:
  1. Count conjunctions of ≤k literals from n attributes: |Conj(n,k)| = O(n^k)
  2. Bound decision list size: |k-DL(n)| ≤ 3^c·c! = 2^{O(n^k log₂(n^k))}
  3. Plug into PAC bound → N polynomial in n

- **MAP learning ≈ Ockham's razor (page 737)**:
  For deterministic hypotheses, P(d|h_i) = 1 if consistent, 0 otherwise
  h_MAP = argmax P(d|h_i)P(h_i) = simplest consistent theory

- **MAP learning ≈ MDL (page 737)**:
  log₂ P(h_i|d) = log₂ P(d|h_i) + log₂ P(h_i) − log₂ P(d)
  Minimizing −log₂ P(d|h_i) − log₂ P(h_i) → minimize bits for hypothesis + bits for data

- **Bayesian convergence argument (page 736)**:
  For fixed prior not ruling out true hypothesis, posterior of false hypotheses vanishes because probability of generating "uncharacteristic" data indefinitely is vanishingly small.

- **Bias–variance tradeoff reasoning**: Bias from hypothesis space restrictions leads to underfitting; variance from training set fluctuations leads to overfitting. More complex models have lower bias but higher variance.

- **Interpolation and overfitting (pages 681-682)**:
  Model classes that interpolate (fit training data exactly) may overfit; but some (deep networks, kernel machines, random forests, boosted ensembles) continue to improve after interpolation.

- **EM increases likelihood at each iteration**: Proved in general; under certain conditions, EM reaches a local maximum in likelihood.

### 14. DESIGN PARADIGMS / META-METHODS

- **Greedy divide-and-conquer**: Decision tree learning tests most important attribute first, then recursively solves subproblems.
- **Generate-and-then-prune**: Build a full tree, then prune irrelevant nodes (avoids XOR problem of early stopping).
- **Model selection via cross-validation**: Evaluate models of increasing complexity on held-out validation data; pick the one with lowest validation error.
- **Regularization**: Add complexity penalty to loss function to balance fit vs. simplicity.
- **Minimum description length (MDL)**: Measure both hypothesis and data in bits; choose hypothesis minimizing total bits.
- **Kernel trick**: Replace dot products with kernel functions to implicitly operate in high-dimensional feature spaces.
- **Ensemble methods**: Combine multiple models to reduce bias (via more expressive model class) and variance (via averaging).
- **Bagging (bootstrap aggregating)**: Sample with replacement → train multiple models → average/vote.
- **Boosting**: Sequentially train models, reweighting examples based on previous mistakes.
- **Gradient boosting**: Build additive models following gradient of loss function.
- **Bayesian learning**: Use full posterior over hypotheses for prediction.
- **MAP learning**: Use single most probable hypothesis (optimization instead of integration).
- **Maximum-likelihood learning**: Assume uniform prior, maximize data likelihood (simplest).
- **EM algorithm**: Iteratively compute expected values of hidden variables (E-step), then maximize likelihood given expectations (M-step).
- **Stochastic gradient descent**: Approximate gradient using small minibatches; faster than batch GD.
- **Online learning**: Update model incrementally as data arrive; no i.i.d. assumption needed.
- **ROC curve analysis**: Visualize tradeoff between false positives and true positives.
- **Feature engineering**: Create informative attributes from raw data using domain knowledge.
- **One-hot encoding**: Transform categorical variables into Boolean indicators.
- **Data augmentation**: Increase effective data set size by applying label-preserving transformations.
- **SMOTE/ADASYN**: Synthetically generate minority class examples.
- **Interpretability vs. explainability**: Interpretability from inspecting model itself; explainability from separate explanation module (LIME, SHAP).
- **Automated machine learning (AutoML)**: Automate model selection, hyperparameter tuning, and feature engineering.
- **Transfer learning**: Use pretrained model from public data, then fine-tune on specific data.
- **Federated learning**: Keep data on user's device; share only model parameters.

### 15. CASE STUDIES / CLASSIC EXAMPLES

- **Restaurant waiting problem (Section 19.2.1)**: 12 examples with 10 attributes (Alternate, Bar, Fri/Sat, Hungry, Patrons, Price, Raining, Reservation, Type, WaitEstimate). Output: WillWait (Yes/No). Used throughout Chapter 19 to demonstrate decision trees, decision lists, naive Bayes, boosting.
  - Data table (Figure 19.2): x₁–x₁₂ with Yes/No outcomes.
  - Decision tree learned (Figure 19.6): Patrons → None: No, Some: Yes, Full → Hungry → No: No, Yes → Fri/Sat → ...
- **Seismic classification (Section 19.6.4-19.6.5)**: Body wave magnitude (x₁) vs. surface wave magnitude (x₂) distinguishing earthquakes from nuclear explosions. 63 data points from Asia/Middle East (1982-1990). Demonstrates linear separability, perceptron learning, and logistic regression.
- **House price prediction (Figure 19.13)**: Univariate linear regression on house size (sq ft) vs. price in Berkeley, CA (July 2009). Result: y = 0.232x + 246.
- **Candy bag example (Chapter 20)**: Five hypotheses about cherry/lime proportions. Bayesian learning updates posterior probabilities as lime candies are sequentially observed. Demonstrates: Bayesian prediction, MAP, maximum-likelihood.
- **Candy wrapper example (Section 20.2.1)**: Unknown proportion θ of cherry; wrapper color depends probabilistically on flavor. Parameters θ, θ₁, θ₂. Likelihood decomposes into independent terms.
- **Candy mixture example (Section 20.3.2)**: Two bags of candy mixed together; Bag is hidden variable. 1000 samples with true parameters: θ=0.5, θ_F1=θ_W1=θ_H1=0.8, θ_F2=θ_W2=θ_H2=0.3. EM recovers parameters from observed counts of flavor/wrapper/hole combinations.
- **Heart disease diagnostic network (Figure 20.11)**: Hidden variable (HeartDisease) with 3 predisposing factors and 3 symptoms. With hidden variable: 78 parameters; without: 708 parameters. Shows benefit of latent variables.
- **MNIST digit recognition (Figure 19.27)**: 60,000 images of handwritten digits, 28×28 pixels (784 dimensions). t-SNE map shows 10 digit clusters. Used in Figure 19.9(b) for CNN model selection.
- **ImageNet**: 14M+ photos with ~20,000 labels — referenced as a publicly available data set.

### 16. ETHICS CONSIDERATIONS

- **Privacy reviews**: Must get proper permission for data collected; maintain data integrity and user understanding (Section 19.9.2).
- **Fairness reviews**: Ensure processes are fair and unbiased (Section 19.9.2, referencing Section 27.3.3).
- **Federated learning**: Alternative to collecting sensitive data; keep data on user's device, share only model parameters.
- **Accountability**: What happens when the system is wrong? Process for complaining/appealing decisions? Track who was responsible for errors? Society expects accountability from software systems including ML (Section 19.9.4).
- **Testing and review**: Source control, unit tests, fuzz tests, load tests, regression tests; code reviews, privacy reviews, fairness reviews, legal compliance reviews.
- **GDPR (General Data Protection Regulation)**: European regulation requiring systems to provide explanations (Section 19.9.4).
- **Trustworthiness**: Stakeholders (regulators, lawmakers, press, users) interested in reliability, accountability, safety.
- **Spam classification ethics**: Misclassifying non-spam as spam (false positive) is worse than misclassifying spam as non-spam (false negative) — 10x higher loss.
- **Unbalanced classes / fairness**: Credit card fraud detection — 99.99% accuracy can be trivial (always say "valid"). Need to ensure minority class is not ignored.
- **Bias in data**: Self-reported ages may have systematic inaccuracies (people lie about age). Unsupervised learning may be needed to uncover the true pattern.
- **Data provenance**: Legal reasons for compliance; need to know where data come from, who has worked on it, whether definitions evolved over time.
- **Monitoring live data**: Track statistics, dashboards, alerts; hire human raters to grade system performance.
- **Explainability as trust**: Regulations may require explanations; simple explanations can lead to false sense of security.

### 17. END-OF-CHAPTER MATERIAL

**Summary (Chapter 19, pages 727-728):**
- Learning takes many forms, depending on the nature of the agent, the component to be improved, and the available feedback.
- If the available feedback provides the correct answer for example inputs, then the learning problem is called supervised learning. The task is to learn a function y = h(x). Learning a function whose output is a continuous or ordered value (like weight) is called regression; learning a function with a small number of possible output categories is called classification.
- We want to learn a function that not only agrees with the data but also is likely to agree with future data. We need to balance agreement with the data against simplicity of the hypothesis.
- Decision trees can represent all Boolean functions. The information-gain heuristic provides an efficient method for finding a simple, consistent decision tree.
- The performance of a learning algorithm can be visualized by a learning curve, which shows the prediction accuracy on the test set as a function of the training set size.
- When there are multiple models to choose from, model selection can pick good values of hyperparameters, as confirmed by cross-validation on validation data. Once the hyperparameter values are chosen, we build our best model using all the training data.
- Sometimes not all errors are equal. A loss function tells us how bad each error is; the goal is then to minimize loss over a validation set.
- Computational learning theory analyzes the sample complexity and computational complexity of inductive learning. There is a tradeoff between the expressiveness of the hypothesis space and the ease of learning.
- Linear regression is a widely used model. The optimal parameters of a linear regression model can be calculated exactly, or can be found by gradient descent search, which is a technique that can be applied to models that do not have a closed-form solution.
- A linear classifier with a hard threshold—also known as a perceptron—can be trained by a simple weight update rule to fit data that are linearly separable. In other cases, the rule fails to converge.
- Logistic regression replaces the perceptron's hard threshold with a soft threshold defined by a logistic function. Gradient descent works well even for noisy data that are not linearly separable.
- Nonparametric models use all the data to make each prediction, rather than trying to summarize the data with a few parameters. Examples include nearest neighbors and locally weighted regression.
- Support vector machines find linear separators with maximum margin to improve the generalization performance of the classifier. Kernel methods implicitly transform the input data into a high-dimensional space where a linear separator may exist, even if the original data are nonseparable.
- Ensemble methods such as bagging and boosting often perform better than individual methods. In online learning we can aggregate the opinions of experts to come arbitrarily close to the best expert's performance, even when the distribution of the data are constantly shifting.
- Building a good machine learning model requires experience in the complete development process, from managing data to model selection and optimization, to continued maintenance.

**Bibliographical and Historical Notes (Chapter 19, pages 728-733):**
Key figures: William of Ockham, Aristotle, David Hume (problem of induction, uniformity of nature), no free lunch theorem (Wolpert and Macready, 1997; Wolpert, 2013), Alan Turing (1947 — anticipated machine learning), Arthur Samuel (1959 — defined ML, checkers program), EPAM (Feigenbaum, 1961), ID3 (Quinlan, 1979), Shannon and Weaver (1949 — entropy/information theory), C4.5 (Quinlan, 1993), CART (Breiman et al., 1984), NP-completeness of optimal decision trees (Hyafil and Rivest, 1976), cross-validation (Larson 1931; Stone 1974; Golub et al. 1979), Tikhonov (1963 — regularization), von Neumann elephant quote, four-parameter elephant (Mayer et al., 2010), memorization conditions (Zhang et al., 2016; Arpit et al., 2017), bias–variance (Belkin et al., 2019), identification in the limit (Gold, 1967), Kolmogorov complexity (Solomonoff 1964; Kolmogorov 1965), MDL (Rissanen 1984, 2007), PAC learning (Valiant, 1984), VC dimension (Vapnik and Chervonenkis, 1971), "four Germans" (Blumer, Ehrenfeucht, Haussler, Warmuth, 1989), linear regression (Legendre 1805; Gauss 1809), logistic function (Verhulst), curse of dimensionality (Bellman, 1961), Newton-Raphson/L-BFGS, Cauchy (1847 — gradient descent), SGD (Robbins and Monro, 1951; Rosenblatt, 1960; Bottou and Bousquet, 2008), nearest neighbors (Fix and Hodges, 1951; Stanfill and Waltz, 1986), LSH (Gionis et al., 1999), kernel machines (Aizerman et al., 1964; Boser et al., 1992), soft-margin SVM (Cortes and Vapnik, 1995 — won 2008 ACM Theory and Practice Award), SMO (Platt, 1999), Condorcet's jury theorem (1785), random forest (Ho 1995; Breiman 2001), GBM (Friedman, 2001), AdaBoost (Schapire 1990; Freund and Schapire 1996), XGBoost (Chen and Guestrin, 2016), online learning (Blum, 1996; Cesa-Bianchi and Lugosi, 2006), AutoML (Hutter et al., 2019), MAML (Finn et al., 2017), LIME (Ribeiro et al., 2016), SHAP (Lundberg and Lee, 2018), explainable AI (Doshi-Velez and Kim, 2017), books: Bishop (2007), Murphy (2012), Hastie et al. (2009), etc.
Conferences: ICML, ICLR, NeurIPS. Journals: Machine Learning, Journal of Machine Learning Research.

---

[space]

## CHAPTER 20: LEARNING PROBABILISTIC MODELS (lines 31543-32796)

### 1. NAMED ENTITIES — Every Term/Concept with Definition

- **Bayesian learning**: Learning by calculating the probability of each hypothesis given the data and making predictions using all hypotheses weighted by their probabilities. Reduces learning to probabilistic inference.
- **Hypothesis prior P(h_i)**: Prior probability assigned to each hypothesis before seeing data.
- **Likelihood P(d|h_i)**: The probability of the data under each hypothesis.
- **Maximum a posteriori (MAP) hypothesis**: The single hypothesis h_i that maximizes P(h_i|d). Predictions made using MAP hypothesis are approximately Bayesian.
- **Maximum-likelihood hypothesis (h_ML)**: The hypothesis that maximizes P(d|h_i); equivalent to MAP with uniform prior.
- **Log likelihood**: L(d|h_θ) = log P(d|h_θ) = Σ_j log P(d_j|h_θ)
- **Density estimation**: The general task of learning a probability model from data generated from that model. A form of unsupervised learning.
- **Complete data**: Data where each data point contains values for every variable in the probability model.
- **Parameter learning**: Finding numerical parameters for a probability model whose structure is fixed.
- **Naive Bayes model**: Bayesian network where the class variable C is the root and attribute variables X_i are leaves; assumes conditional independence of attributes given the class.
- **Generative model**: Models the probability distribution of each class (e.g., naive Bayes text classifier). Can generate random instances of a class.
- **Discriminative model**: Directly learns the decision boundary between classes, i.e., P(Category|Inputs). Examples: logistic regression, decision trees, SVMs.
- **Beta distribution**: A family of probability density functions for parameters θ in [0,1]; defined by hyperparameters a and b: Beta(θ; a,b) = α θ^{a−1}(1−θ)^{b−1}. Conjugate prior for Bernoulli variable.
- **Hyperparameter**: A parameter of the prior distribution (e.g., a and b in Beta distribution) — distinct from model parameters like θ.
- **Conjugate prior**: A prior distribution family that is closed under update (posterior is in the same family). The beta family is the conjugate prior for a Boolean variable; Dirichlet for multivalued; Normal-Wishart for Gaussian.
- **Virtual counts**: Viewing the a and b hyperparameters in Beta(a,b) as if we had started with uniform prior Beta(1,1) and seen a−1 cherry and b−1 lime candies.
- **Parameter independence**: The assumption that P(Θ, Θ₁, Θ₂) = P(Θ)P(Θ₁)P(Θ₂) — each parameter has its own independent prior.
- **Uninformative prior**: A prior that conveys little information (e.g., θ₀=0, σ²₀ large for Gaussian prior on slope).
- **Latent variable (hidden variable)**: A variable not observable in the data (e.g., the disease in medical records).
- **Expectation–maximization (EM) algorithm**: Iterative algorithm for learning with hidden variables; alternates between E-step (computing expected values of hidden variables) and M-step (maximizing likelihood given expected values).
- **Unsupervised clustering**: The problem of discerning multiple categories in a collection of objects without category labels.
- **Mixture distribution**: A distribution P(x) = Σ_i P(C=i) P(x|C=i) with k components. Data generated by first choosing a component, then generating a sample from that component.
- **Mixture of Gaussians**: A mixture model where each component is a multivariate Gaussian distribution; parameters are w_i (weights), μ_i (means), Σ_i (covariances).
- **Indicator variable Z_{ij}**: Variable that is 1 if datum x_j was generated by component i, 0 otherwise (used in EM).
- **E-step (expectation step)**: Computes expected values of hidden variables given current parameters.
- **M-step (maximization step)**: Finds new parameter values that maximize log likelihood given expected values of hidden variables.
- **Identifiability**: A model is identifiable if it can be uniquely recovered from the data. Two-attribute mixture model is not identifiable.
- **Hidden Markov model (HMM)**: Dynamic Bayes net with single discrete state variable (Section 14.3). Transition probabilities learned via EM.
- **Forward–backward algorithm**: HMM inference algorithm used to compute needed probabilities for EM learning of HMMs.
- **Structural EM**: An EM variant that updates both structure and parameters; uses current structure to compute expected counts, then applies them to evaluate new structures.
- **Nonparametric density estimation**: Learning a probability model without structural/parametric assumptions; uses nearest neighbors or kernel methods.
- **Parzen window density estimation**: Another name for kernel density estimation (Rosenblatt, 1956; Parzen, 1962).
- **Dirichlet process**: A distribution over Dirichlet distributions; used for nonparametric Bayesian methods with unknown numbers of components (Ferguson, 1973).
- **Gaussian process**: Defines prior distributions over the space of continuous functions (Rasmussen and Williams, 2006).
- **BUGS (Bayesian inference Using Gibbs Sampling)**: Software package for statistical learning with Bayes nets (Gilks et al., 1994; Lunn et al., 2000, 2013).
- **JAGS (Just Another Gibbs Sampler)**: Software for Bayesian inference (Plummer, 2003).
- **STAN**: Software for Bayesian inference (Carpenter et al., 2017).
- **AutoClass**: First successful EM-based system for mixture modeling (Cheeseman et al., 1988); applied to star classification and protein/DNA analysis.
- **Baum–Welch algorithm**: EM algorithm for HMM learning (Baum and Petrie, 1966).
- **AD-tree**: Data structure for caching counts over all combinations of variables/values for Bayes net structure learning (Moore and Lee, 1997).

### 2. PROCESSES / ALGORITHMS — Step-by-Step Procedures

**Bayesian learning process (Section 20.1):**
1. Start with prior distribution P(h_i) over hypotheses
2. Observe data d
3. Compute posterior: P(h_i|d) = α P(d|h_i) P(h_i)  (Equation 20.1)
4. Make predictions: P(X|d) = Σ_i P(X|h_i) P(h_i|d)  (Equation 20.2)

**Maximum-likelihood parameter learning method (page 738):**
1. Write down expression for likelihood of data as function of parameter(s)
2. Write down derivative of log likelihood with respect to each parameter
3. Find parameter values such that the derivatives are zero
4. Verify Hessian matrix is negative-definite

**EM for mixtures of Gaussians (page 753):**
Initialize parameters arbitrarily, then iterate:
- E-step: Compute p_{ij} = P(C=i | x_j) = α P(x_j | C=i) P(C=i). Define n_i = Σ_j p_{ij}
- M-step:
  - μ_i ← Σ_j p_{ij} x_j / n_i
  - Σ_i ← Σ_j p_{ij} (x_j−μ_i)(x_j−μ_i)^⊤ / n_i
  - w_i ← n_i / N

**EM for Bayesian networks with hidden variables (page 756):**
For each CPT parameter θ_{ijk} = P(X_i = x_{ij} | U_i = u_{ik}):
  θ_{ijk} ← N̂(X_i=x_{ij}, U_i=u_{ik}) / N̂(U_i=u_{ik})
Expected counts obtained by summing over examples, computing P(X_i=x_{ij}, U_i=u_{ik}) for each.

**EM for HMMs (page 758):**
θ_{ij} ← Σ_t N̂(X_{t+1}=j, X_t=i) / Σ_t N̂(X_t=i)
Expected counts computed by forward–backward algorithm (smoothing, not filtering).

**General form of EM (page 758):**
θ^{(i+1)} = argmax_θ Σ_z P(Z=z | x, θ^{(i)}) L(x, Z=z | θ)

### 3. HIERARCHIES / CLASSIFICATIONS

**Types of learning (Chapter 19 recap + refinement from Chapter 20):**
- Supervised learning (input-output pairs, labels)
- Unsupervised learning (no feedback; clustering; density estimation)
- Reinforcement learning (rewards and punishments)
- Semi-supervised learning (few labeled + many unlabeled)
- Weakly supervised learning (noisy/imprecise labels)

**Three approaches to probabilistic learning (from most to least complex):**
1. **Bayesian learning**: Full posterior over hypotheses; P(X|d) = Σ_i P(X|h_i)P(h_i|d)
2. **MAP learning**: Single hypothesis h_MAP maximizing P(h|d); P(X|d) ≈ P(X|h_MAP)
3. **Maximum-likelihood (ML) learning**: Single hypothesis maximizing P(d|h); assumes uniform prior

**Generative vs. Discriminative models:**
- Generative: P(Category, Inputs) — models joint distribution (e.g., naive Bayes)
- Discriminative: P(Category | Inputs) — models decision boundary (e.g., logistic regression, SVMs, decision trees)

**Regression from probabilistic perspective:**
- Linear regression with L₂ loss = maximum likelihood under Gaussian noise model with fixed variance
- L₁ loss = maximum likelihood under Laplace (double exponential) noise distribution

### 4. COMPARISONS / TRADE-OFFS

- **Bayesian vs. MAP vs. ML**:
  - Bayesian: Optimal but expensive (summation/integration over all hypotheses)
  - MAP: More tractable (optimization), uses prior, overconfident with small data
  - ML: Simplest (uniform prior), problems with small data (zero probabilities), good approximation with large data
- **MAP vs. Bayesian predictions**: MAP (after 3 limes) → predict 100% lime; Bayesian → predict 80% lime. MAP is more dangerous with small data.
- **Generative vs. Discriminative (Ng and Jordan, 2002)**:
  - Discriminative: Better with large data (focuses on decision boundary); better on 9/15 data sets with max data
  - Generative: Better with small data (models full distribution); better on 14/15 data sets with small data
- **Hidden variables vs. no hidden variables**: Hidden variable model (Figure 20.11(a)): 78 parameters. Equivalent model without hidden variable (Figure 20.11(b)): 708 parameters. Hidden variables dramatically reduce parameters needed and data required.
- **Tabular vs. compact representations (e.g., noisy-OR)**: Complexity penalty for tabular grows exponentially with parents; for noisy-OR, grows linearly. Learning with compact models tends to learn structures with more parents.
- **Filtering vs. Smoothing in HMM learning**: Filtering uses only past evidence; smoothing uses all evidence (including future). Smoothing is needed for learning HMM transition probabilities because evidence after a transition is relevant.
- **k-nearest-neighbors vs. kernel density estimation**: k-NN uses fixed number of neighbors; kernel uses kernel function and width. Both have hyperparameters (k or w) best chosen by cross-validation.

### 5. FORMULAS & EQUATIONS

**Bayes' rule for hypotheses (Equation 20.1):**
P(h_i|d) = α P(d|h_i) P(h_i)

**Bayesian prediction (Equation 20.2):**
P(X|d) = Σ_i P(X|h_i) P(h_i|d)

**Likelihood for i.i.d. data (Equation 20.3):**
P(d|h_i) = Π_j P(d_j|h_i)

**Maximum-likelihood for Bernoulli (cherry/lime):**
P(d|h_θ) = θ^c · (1−θ)^ℓ
Log likelihood: L = c log θ + ℓ log(1−θ)
dL/dθ = c/θ − ℓ/(1−θ) = 0 ⇒ θ = c/(c+ℓ) = c/N

**Log likelihood for wrapper model:**
L = [c log θ + ℓ log(1−θ)] + [r_c log θ₁ + g_c log(1−θ₁)] + [r_ℓ log θ₂ + g_ℓ log(1−θ₂)]
θ = c/(c+ℓ), θ₁ = r_c/(r_c+g_c), θ₂ = r_ℓ/(r_ℓ+g_ℓ)

**Naive Bayes parameters (Boolean):**
θ = P(C=true), θ_{i1} = P(X_i=true|C=true), θ_{i2} = P(X_i=true|C=false)
P(C|x₁,...,x_n) = α P(C) Π_i P(x_i|C)

**Gaussian density:**
P(x) = (1/(σ√(2π))) e^{−(x−μ)²/(2σ²)}

**Maximum-likelihood for Gaussian (Equation 20.4):**
μ = Σ_j x_j / N
σ = √(Σ_j (x_j−μ)² / N)

**Linear–Gaussian conditional (Equation 20.5):**
P(y|x) = (1/(σ√(2π))) e^{−(y−(θ₁x+θ₂))²/(2σ²)}

**Beta distribution (Equation 20.6):**
Beta(θ; a,b) = α θ^{a−1} (1−θ)^{b−1}
Mean = a/(a+b)

**Beta update (after cherry):**
P(θ|D₁=cherry) = α' θ · Beta(θ; a,b) = α' Beta(θ; a+1, b)

**Bayesian linear regression (Equations 20.7-20.8):**
P(y|x,θ) = N(y; θx, σ²_y)
P(θ) = N(θ; θ₀, σ²₀)
Posterior: P(θ|d) ∝ P(d|θ) P(θ) → N(θ; θ_N, σ²_N)

**Posterior mean and variance for Bayesian linear regression:**
θ_N = (σ² θ₀ + σ²₀ Σ_i x_i y_i) / (σ² + σ²₀ Σ_i x_i²)
σ²_N = σ² σ²₀ / (σ² + σ²₀ Σ_i x_i²)

**Predictive distribution for Bayesian linear regression:**
P(y|x,d) ∝ e^{−½ (y − θ_N x)² / (σ² + σ²_N x²)}
Variance = σ² + σ²_N x² (grows with distance from origin)

**MAP / MDL equivalence:**
Minimizing −log₂ P(d|h_i) − log₂ P(h_i) = minimizing bits for data + bits for hypothesis

**Mixture of Gaussians:**
P(x) = Σ_{i=1}^{k} w_i · N(x; μ_i, Σ_i)   where w_i = P(C=i)

**EM update for Bayes net CPTs (Equation page 756):**
θ_{ijk} ← N̂(X_i=x_{ij}, U_i=u_{ik}) / N̂(U_i=u_{ik})

**HMM transition learning:**
θ_{ij} ← Σ_t N̂(X_{t+1}=j, X_t=i) / Σ_t N̂(X_t=i)

### 6. RULES, LAWS & THEOREMS

- **Bayes' rule for learning**: P(h_i|d) = α P(d|h_i) P(h_i)
- **Ockham's razor via MAP**: For deterministic hypotheses, h_MAP is the simplest consistent theory (P(d|h_i)=1 for consistent, 0 otherwise).
- **MAP ≈ MDL equivalence**: Maximizing P(d|h_i)P(h_i) is equivalent to minimizing total description length in bits.
- **Conjugate prior property**: Beta family is closed under update (posterior in same family as prior). Beta is conjugate prior for Bernoulli variable; Dirichlet for multinomial; Normal-Wishart for Gaussian.
- **EM convergence**: EM increases log likelihood at every iteration; under certain conditions, reaches a local maximum (rarely saddle point or local minimum).
- **EM as generalization of gradient-based hill climbing**: No "step size" parameter.
- **Bayesian optimality**: Given the hypothesis prior, Bayesian prediction is optimal; any other prediction is expected to be correct less often.
- **Bayesian convergence**: Posterior of false hypotheses eventually vanishes for any fixed prior that does not rule out the true hypothesis.
- **Independence in likelihood**: With complete data and tabular CPTs, maximum-likelihood parameter learning for Bayesian networks decomposes into separate learning problems per parameter.
- **Conditional independence in naive Bayes**: Attributes are conditionally independent given the class.
- **Mercer's theorem (1909)**: Any positive definite kernel corresponds to some feature space.
- **Causal network recovery**: Pearl (2000) showed causality can often be ascertained from observational data, not just experimental trials.

### 7. DATA STRUCTURES & TYPES

- **Hypothesis prior**: Distribution over hypotheses, P(h_i) or P(θ) (continuous).
- **Beta distribution**: Prior/posterior over parameter θ in [0,1]; stored as (a,b) hyperparameters.
- **Dirichlet distribution**: Conjugate prior for multivalued discrete distribution.
- **Normal–Wishart distribution**: Conjugate prior for Gaussian parameters.
- **Bayesian network (for learning, Figure 20.6)**: Nodes include parameter variables Θ (with no parents), evidence variables (Flavor_i, Wrapper_i), and data.
- **AD-tree**: Caching data structure for counts over variable/value combinations in Bayes net structure learning.
- **Mixture model**: Stored as weights w_i, means μ_i, covariances Σ_i for each component.
- **Nonparametric density**: All data points stored; density estimated at query time via nearest neighbors or kernel averaging.

### 8. VISUAL PATTERNS

- **Figure 20.1 (page 736)**: (a) Posterior probabilities P(h_i|d) for 5 hypotheses as 1-10 lime candies observed; h₁ (100% cherry) disappears quickly, h₅ (100% lime) becomes dominant after 3 limes. (b) Bayesian prediction of next candy being lime increases monotonically toward 1.
- **Figure 20.2 (page 739)**: (a) Simple Bayes net: Flavor ← Θ. (b) Bayes net with wrapper: Flavor ← Θ, Wrapper ← (Θ₁, Θ₂) depending on Flavor.
- **Figure 20.3 (page 741)**: Learning curve comparing naive Bayes vs. decision tree on restaurant problem; decision tree does better.
- **Figure 20.4 (page 742)**: (a) Linear–Gaussian model: y = θ₁x + θ₂ + Gaussian noise. (b) 50 data points with best-fit line.
- **Figure 20.5 (page 744)**: Beta distributions for different (a,b) pairs: (a) [1,1] (uniform), [2,2], [5,5] — peaked around 0.5; (b) [3,1], [6,2], [30,10] — peak near 0.75, narrowing with more data.
- **Figure 20.6 (page 745)**: Bayesian network for Bayesian parameter learning: Θ, Θ₁, Θ₂ as root nodes; Flavor_i and Wrapper_i nodes for each observation.
- **Figure 20.7 (page 747)**: Bayesian linear regression: (a) with 3 data points near origin — slope uncertain, predictive variance grows with distance; (b) with 5 data points (2 further away) — slope tightly constrained, variance largely from fixed noise.
- **Figure 20.8 (page 749)**: (a) 3D plot of mixture of 3 Gaussians; (b) 128-point sample with two query points and their 10-nearest-neighborhoods.
- **Figure 20.9 (page 750)**: Kernel density estimation with k=3 (too spiky), k=10 (just right), k=40 (too smooth).
- **Figure 20.10 (page 750)**: Kernel density with Gaussian kernels: w=0.02 (too small), w=0.07 (just right), w=0.20 (too large).
- **Figure 20.11 (page 751)**: (a) Heart disease diagnostic network with hidden variable (78 params); (b) Equivalent network without hidden variable (708 params). Each variable has 3 values; parameters labeled on nodes.
- **Figure 20.12 (page 752)**: (a) Mixture of 3 Gaussians with weights 0.2, 0.3, 0.5; (b) 500 sampled data points; (c) Model reconstructed by EM (virtually indistinguishable from original).
- **Figure 20.13 (page 754)**: Log likelihood vs. EM iteration: (a) Gaussian mixture — rises from ~−200 to ~+700 over 20 iterations; (b) Bayes net with hidden bag variable — rises from ~−2020 to ~−1980 over 120 iterations.
- **Figure 20.14 (page 755)**: (a) Bayes net for candy mixture: Bag (hidden) → Flavor, Wrapper, Hole; (b) Bayes net for Gaussian mixture.
- **Figure 20.15 (page 757)**: Unrolled dynamic Bayes net for hidden Markov model (repeat of Figure 14.16).

### 9. EDGE CASES / EXCEPTIONS / TRAPS

- **Zero probability problem**: With small data sets, ML assigns zero probability to unobserved events. Fix: initialize counts to 1 (Laplace smoothing).
- **Non-identifiability**: Two-attribute mixture model (only flavor and wrapper, no holes) cannot recover mixture parameters (5 parameters but only 3 observed counts).
- **Non-identifiability with hidden variables**: Two observationally equivalent models exist (Bag variable flipped); initialization determines which one EM converges to.
- **Degenerate EM local maxima**: Gaussian component can shrink to cover a single data point (variance → 0, likelihood → ∞); components can merge.
- **High-dimensional EM problems**: Degenerate local maxima are especially serious in high dimensions.
- **Saddle points**: In rare cases, EM can reach a saddle point or even a local minimum.
- **Bayesian network inference is NP-hard**: For complex models with hidden variables, each EM inner-loop iteration involves NP-hard inference.
- **Naive Bayes overconfidence**: Conditional independence assumption leads to probabilities very close to 0 or 1, especially with many attributes.
- **MAP overconfidence with small data**: After 3 limes, MAP predicts 100% lime; Bayesian predicts 80% lime. MAP is dangerously overconfident.
- **Maximum-likelihood structure learning**: Without complexity penalty, ML will always produce a fully connected network (no hidden variables).
- **Bayesian regression without enough spread**: If data are concentrated near origin, posterior variance remains large (≈ prior variance), and slope is uncertain.
- **Structure learning with hidden variables**: Very time-consuming; inner loop involves many iterations of EM, which is NP-hard.

### 10. EMPIRICAL EVIDENCE / KEY RESULTS

- **Candy example**: Prior = ⟨0.1, 0.2, 0.4, 0.2, 0.1⟩ over h₁–h₅. After 10 lime candies: P(h₅|d) ≈ 1.
- **Candy mixture EM example**: True params: θ=0.5, θ_F1=θ_W1=θ_H1=0.8, θ_F2=θ_W2=θ_H2=0.3. After 10 EM iterations: learned model fits better (L=−1982.214) than original true model (L≈−1982.5).
- **Candy mixture counts**: 1000 candies: {F=cherry,W=red,H=1:273; H=0:93; W=green,H=1:104; H=0:90; F=lime,W=red,H=1:79; H=0:100; W=green,H=1:94; H=0:167}.
- **First EM iteration for mixture**: θ changes from 0.6→0.6124; θ_F1: 0.6→0.6684; θ_W1: 0.6→0.6483; θ_H1: 0.6→0.6558; θ_F2: 0.4→0.3887; etc.
- **Log likelihood improvement in EM**: First iteration: −2044 → −2021 (e²³ ≈ 10¹⁰ improvement).
- **Heart disease network**: Hidden variable model: 78 params. Equivalent observable-only model: 708 params.
- **Generative vs. discriminative on 15 data sets**: With max data, discriminative better on 9/15; with small data, generative better on 14/15 (Ng and Jordan, 2002).
- **Naive Bayes vs. decision tree (restaurant)**: Naive Bayes learns well but not as well as decision tree on restaurant problem (Figure 20.3).
- **AutoClass applications**: Discovered new types of stars (Goebel et al., 1989) and new classes of proteins/introns (Hunter and States, 1992).

### 11. CROSS-CHAPTER DEPENDENCIES

- **Chapter 12 (Probabilistic reasoning)**: Uncertainty in real environments — foundational motivation for Chapter 20.
- **Chapter 13 (Bayesian networks)**: Bayes net semantics, conditional independence, inference algorithms — prerequisite for parameter and structure learning.
- **Section 14.3 (Hidden Markov models)**: Forward–backward algorithm, dynamic Bayes nets — used in Section 20.3.3 for HMM learning.
- **Section 14.4 (Bayesian network inference)**: Gaussian distributions in Bayes nets — referenced in Section 20.2.6.
- **Chapter 19 (Learning from Examples)**: Foundation of supervised learning; PAC learning, overfitting, bias-variance tradeoff — all extended in Chapter 20's probabilistic view.
- **Section 4.2 (Beyond classical search)**: Optimization methods — referenced for finding ML/MAP parameters.
- **Appendix A (Math background)**: Linear algebra, calculus — needed for understanding continuous models and derivations.
- **Chapter 21 (Deep learning)**: Builds on probabilistic learning concepts.
- **Chapter 22 (Reinforcement learning)**: Uses learning concepts.
- **Second edition material on neural networks**: Statistical view of NN learning emerged alongside Bayes net resurgence in late 1980s-1990s.

### 12. DATES & PEOPLE

- **Thomas Bayes (1763)**: Beta distribution as conjugate prior for Bernoulli (derived by Richard Price posthumously).
- **Karl Pearson (1895)**: Reintroduced beta distribution as "Pearson Type I distribution."
- **Rosenblatt (1956) and Parzen (1962)**: Nonparametric (Parzen window) density estimation.
- **Baum and Petrie (1966)**: Baum–Welch algorithm for HMM learning (EM special case).
- **Hartley (1958)**: First described general idea of EM with examples.
- **Dempster, Laird, and Rubin (1977)**: Presented EM in general form; analyzed convergence. One of most cited papers in CS and statistics.
- **Ferguson (1973)**: Dirichlet process for nonparametric Bayesian methods.
- **Cheeseman et al. (1988)**: AutoClass — first successful EM system for mixture modeling.
- **Pearl (1988) and Pearl and Verma (1991)**: First algorithms for learning Bayes net structures using conditional independence tests.
- **Spirtes et al. (1993)**: TETRAD package for Bayes net learning.
- **Cooper and Herskovits (1992)**: Likelihood-based structure learning; improved by Heckerman et al. (1994).
- **Lauritzen (1995), Russell et al. (1995)**: EM and gradient-based methods for Bayes net learning with hidden variables.
- **Ng and Jordan (2002)**: Compared generative (naive Bayes) vs. discriminative (logistic regression) learning.
- **Friedman (1998)**: Structural EM algorithm.
- **Friedman and Koller (2003)**: Bayesian structure learning.
- **Minka (2010)**: Concise summary of Bayesian linear regression derivations.
- **Box and Tiao (1973)**: Bayesian linear regression text.
- **Rasmussen and Williams (2006)**: Gaussian process text.
- **Carpenter et al. (2017)**: STAN software.
- **Plummer (2003)**: JAGS software.
- **Gilks et al. (1994); Lunn et al. (2000, 2013)**: BUGS software.
- **Dempster**: "EM is a schema rather than an algorithm" — mathematical work required before applying to new distributions.
- **Goebel et al. (1989)**: AutoClass applied to star classification.
- **Hunter and States (1992)**: AutoClass applied to protein/intron classification.

### 13. PROOF & ARGUMENT PATTERNS

- **MAP learning as Ockham's razor** (page 737):
  For deterministic hypotheses, P(d|h_i) = 1 if consistent, 0 otherwise.
  h_MAP = argmax P(d|h_i) P(h_i) = argmax_{consistent h_i} P(h_i).
  If P(h_i) penalizes complexity, h_MAP is the simplest consistent theory.

- **MAP ≈ MDL equivalence** (page 737):
  Taking log: h_MAP minimizes −log₂ P(d|h_i) − log₂ P(h_i).
  −log₂ P(h_i) = bits to specify hypothesis.
  −log₂ P(d|h_i) = bits to specify data given hypothesis.
  Therefore MAP = minimum description length.

- **ML estimation for Bernoulli parameter** (page 738):
  P(d|θ) = θ^c (1−θ)^ℓ.
  L = c log θ + ℓ log(1−θ).
  dL/dθ = c/θ − ℓ/(1−θ) = 0 → θ = c/(c+ℓ).
  Standard recipe: (1) write likelihood, (2) derivative of log likelihood, (3) set to zero.

- **Parameter independence in Bayes net learning** (page 740):
  With complete data and tabular CPTs, log likelihood = sum of terms, each containing single parameter.
  Derivatives are independent → each parameter estimated as observed frequency.

- **Bayesian convergence argument** (page 736):
  Prior that doesn't rule out true hypothesis → posterior of false hypotheses eventually vanishes.
  Reason: probability of generating uncharacteristic data indefinitely is vanishingly small.
  Analogous to PAC learning.

- **EM convergence proof sketch** (page 754):
  EM increases log likelihood at every iteration.
  Under certain conditions, reaches a local maximum.
  Has no "step size" parameter (unlike gradient methods).

### 14. DESIGN PARADIGMS / META-METHODS

- **Bayesian learning framework**: View learning as probabilistic inference; maintain full posterior over hypotheses.
- **MAP approximation**: Replace full posterior with single best hypothesis (optimization replaces integration).
- **ML approximation**: Assume uniform prior; maximize data likelihood.
- **Conjugate priors**: Choose prior family closed under update to simplify Bayesian computation (Beta-Bernoulli, Dirichlet-multinomial, Normal-Wishart-Gaussian).
- **Parameter independence**: Assume prior independence of parameters to decompose learning problem.
- **EM algorithm framework**: Iterative method for hidden variables; E-step computes expectations, M-step maximizes.
- **Structural EM**: Update both structure and parameters simultaneously in one EM framework.
- **Bayesian approach to linear regression**: Put prior on slope/intercept; posterior gives uncertainty that grows with distance from observed data.
- **Network as inference for learning**: The entire Bayesian learning process can be cast as inference in a derived Bayes net (Figure 20.6) with parameter nodes and evidence nodes.
- **Nonparametric density estimation**: Let data speak for themselves — k-nearest-neighbors or kernel methods without parametric assumptions.
- **Importance of hidden variables**: Hidden variables can dramatically reduce model complexity (e.g., 78 vs. 708 parameters in heart disease model).

### 15. CASE STUDIES / CLASSIC EXAMPLES

- **Cherry/lime candy (Section 20.1)**: Five hypotheses about bag composition (100% cherry → 100% lime). Prior: ⟨0.1, 0.2, 0.4, 0.2, 0.1⟩. After 10 lime candies, h₅ (100% lime) dominates. Posterior > prior > ML comparisons shown.
- **Candy wrapper model (Section 20.2.1)**: Unknown proportion θ of cherry; wrapper color depends on flavor with parameters θ₁ (cherry→red) and θ₂ (lime→red). Likelihood decomposes into three independent terms.
- **Candy mixture (Section 20.3.2)**: Two bags of candy with parameters: θ=0.5, θ_F1=θ_W1=θ_H1=0.8, θ_F2=θ_W2=θ_H2=0.3. 1000 samples observed. EM recovers parameters from aggregated counts of (flavor, wrapper, hole) combinations.
  - Counts: 273 (cherry, red, hole), 93 (cherry, red, no hole), 104 (cherry, green, hole), 90 (cherry, green, no hole), 79 (lime, red, hole), 100 (lime, red, no hole), 94 (lime, green, hole), 167 (lime, green, no hole).
- **Heart disease network (Figure 20.11)**: Three-valued variables; 3 predisposing factors, 3 symptoms, 1 hidden variable (HeartDisease). With hidden: 78 params. Without: 708 params.
- **Linear–Gaussian model (Figure 20.4)**: y = θ₁x + θ₂ + Gaussian noise. 50 data points. Maximizing likelihood = minimizing squared error (L₂ loss).
- **Bayesian linear regression (Figure 20.7)**: y = θx + noise, through origin. (a) 3 data points near origin → uncertain slope, variance grows with x. (b) 5 data points with 2 far → tightly constrained slope.

### 16. ETHICS CONSIDERATIONS

- **Smoking/cancer debate**: "certain corporations have long claimed that smoking does not cause cancer" — cited as motivation for learning causal structure from data (Section 20.2.7).
- **Climate change debate**: "other corporations assert that CO₂ concentrations have no effect on climate" — same context.
- **Causal discovery from observational data**: Pearl (2000) argued causality can be ascertained from observational data, countering statisticians who believed only experimental trials could yield causal information.
- **Fairness**: The structure of the learned model (e.g., discovering HeartDisease as hidden variable) has implications for fairness and bias in medical diagnosis.
- **Bias in data**: The book notes that parameter estimates depend on the observed data distribution; if data are biased, the learned model will be biased.
- **Causal knowledge / corporate interests**: The chapter notes that causal models may be "subject to dispute" for commercial/political reasons.

### 17. END-OF-CHAPTER MATERIAL

**Summary (Chapter 20, pages 760-761):**
- Bayesian learning methods formulate learning as a form of probabilistic inference, using the observations to update a prior distribution over hypotheses. This approach provides a good way to implement Ockham's razor, but quickly becomes intractable for complex hypothesis spaces.
- Maximum a posteriori (MAP) learning selects a single most likely hypothesis given the data. The hypothesis prior is still used and the method is often more tractable than full Bayesian learning.
- Maximum-likelihood learning simply selects the hypothesis that maximizes the likelihood of the data; it is equivalent to MAP learning with a uniform prior. In simple cases such as linear regression and fully observable Bayesian networks, maximum-likelihood solutions can be found easily in closed form. Naive Bayes learning is a particularly effective technique that scales well.
- When some variables are hidden, local maximum likelihood solutions can be found using the expectation maximization (EM) algorithm. Applications include unsupervised clustering using mixtures of Gaussians, learning Bayesian networks, and learning hidden Markov models.
- Learning the structure of Bayesian networks is an example of model selection. This usually involves a discrete search in the space of structures. Some method is required for trading off model complexity against degree of fit.
- Nonparametric models represent a distribution using the collection of data points. Thus, the number of parameters grows with the training set. Nearest-neighbors methods look at the examples nearest to the point in question, whereas kernel methods form a distance-weighted combination of all the examples.

**Bibliographical and Historical Notes (Chapter 20, pages 761-763):**
Key figures: Duda and Hart (1973 — early statistical learning in AI); naive Bayes dating to 1950s; Domingos and Pazzani (1997 — explanation of naive Bayes success); boosted naive Bayes won first KDD Cup (Elkan, 1997); Heckerman (1998 — Bayes net learning intro); Spiegelhalter et al. (1993 — Dirichlet priors); Thomas Bayes (1763 — beta distribution); Karl Pearson (1895 — Pearson Type I); Box and Tiao (1973 — Bayesian linear regression); Minka (2010); BUGS (Gilks et al., 1994); JAGS (Plummer, 2003); STAN (Carpenter et al., 2017); Pearl (1988) and Pearl and Verma (1991 — conditional independence tests); Spirtes et al. (1993 — TETRAD); KDD Cup 2001 Bayes net win (Cheng et al., 2002); Cooper and Herskovits (1992 — likelihood-based structure learning); Heckerman et al. (1994 — improvements); Moore and Wong (2003); Teyssier and Koller (2005); AD-tree (Moore and Lee, 1997); Friedman and Goldszmidt (1996 — representation influence on structure); Hartley (1958 — first EM description); Baum and Welch (Baum and Petrie, 1966 — HMM learning); Dempster, Laird, and Rubin (1977 — EM in general form, one of most cited papers in CS and statistics); McLachlan and Krishnan (1997 — EM book); Titterington et al. (1985 — mixture models); AutoClass (Cheeseman et al., 1988); Lauritzen (1995) and Russell et al. (1995) — EM for Bayes nets; Friedman (1998 — structural EM); Friedman and Koller (2003 — Bayesian structure learning); Pearl (2000 — causality); Gaussian process (Rasmussen and Williams, 2006); Dirichlet process (Ferguson, 1973); nonparametric Bayes (Ghahramani, 2005; Jordan, 2005); Parzen window (Rosenblatt, 1956; Parzen, 1962); Devroye (1987); Bishop (2007); Hastie et al. (2009); Barber (2012); Murphy (2012); Duda and Hart (1973/2001); NeurIPS/NIPS; AIStats; Valencia International Meetings on Bayesian Statistics; Bayesian Analysis journal.


---

## CHAPTER 21: DEEP LEARNING (lines 32797-34514)

### 1. NAMED ENTITIES — Every Term/Concept with Definition

- **Deep learning**: A broad family of techniques for machine learning in which hypotheses take the form of complex algebraic circuits with tunable connection strengths. "Deep" refers to circuits organized into many layers.
- **Layer**: An organizational unit of a deep network; computation paths from inputs to outputs have many steps.
- **Neural network**: Networks trained by deep learning methods, named for their origin in modeling networks of neurons in the brain (McCulloch and Pitts, 1943), though resemblance to real neural cells is superficial.
- **Feedforward network**: A network with connections only in one direction — a directed acyclic graph with designated input and output nodes. Information flows from input to output with no loops.
- **Recurrent network (RNN)**: A network that feeds intermediate or final outputs back into its own inputs, creating a dynamical system with internal state/memory.
- **Unit**: Each node within a network; calculates weighted sum of inputs from predecessor nodes and applies a nonlinear activation function.
- **Activation function**: A nonlinear function g_j applied to the weighted sum of inputs to a unit. Key types: sigmoid, ReLU, softplus, tanh.
- **Sigmoid (logistic) function**: σ(x) = 1/(1+e^{-x})
- **ReLU (Rectified Linear Unit)**: ReLU(x) = max(0,x)
- **Softplus function**: softplus(x) = log(1+e^x); derivative is the sigmoid function.
- **Tanh function**: tanh(x) = (e^{2x}-1)/(e^{2x}+1); range is (-1,+1); scaled/shifted version of sigmoid: tanh(x) = 2σ(2x)-1.
- **Universal approximation theorem**: A network with just two layers (first nonlinear, second linear) can approximate any continuous function to arbitrary accuracy.
- **Computation graph / Dataflow graph**: A circuit in which each node represents an elementary computation; the fundamental representation for deep learning.
- **Fully connected**: When every node in each layer is connected to every node in the next layer.
- **Output layer**: The layer that produces the output of the network.
- **Hidden layer**: Layers not directly connected to outputs; intermediate representations.
- **Back-propagation**: Method of passing error at the output back through the network to compute gradients, applying reverse mode differentiation.
- **Vanishing gradient**: Problem in deep networks where error signals are extinguished as they propagate back, because derivative factors g'_j can be very small or zero.
- **Automatic differentiation**: Systematic application of calculus rules to calculate gradients for any numeric program.
- **Reverse mode differentiation**: Applies the chain rule "from the outside in"; efficient when network has many inputs and few outputs.
- **End-to-end learning**: Training an entire complex computational system from input/output pairs without manually designing intermediate representations.
- **One-hot encoding**: Representation of categorical attributes with d possible values as d separate input bits; the corresponding bit is set to 1 and all others to 0.
- **Cross-entropy loss**: A measure of dissimilarity between two distributions P and Q: H(P,Q) = E_{z~P(z)}[-log Q(z)].
- **Kullback-Leibler divergence (KL divergence)**: D_KL(P||Q) = ∫ P(z) log(P(z)/Q(z)) dz; satisfies D_KL(P||P)=0. Cross-entropy = H(P) + D_KL(P||Q).
- **Softmax layer**: Maps a vector of input values to a categorical distribution (d output nodes summing to 1): softmax(in)_k = e^{in_k} / ∑_{k'} e^{in_{k'}}.
- **Linear output layer**: ˆy_j = in_j (no activation function); interpreted as mean of Gaussian prediction with fixed variance.
- **Mixture density layer**: Outputs represented using a mixture of Gaussian distributions; predicts relative frequency, mean, and variance of each component.
- **Convolutional neural network (CNN)**: Network with spatially local connections and replicated weight patterns (kernels) across units in each layer.
- **Kernel**: A pattern of weights replicated across multiple local regions in a CNN.
- **Convolution**: The process of applying a kernel to pixels (or spatially organized units); denoted by * symbol.
- **Stride**: The distance between successive applications of a kernel (e.g., s=2 means kernels centered 2 pixels apart).
- **Receptive field**: The portion of the sensory input that can affect a neuron's activation. For CNN: in mth hidden layer, size = (l-1)m+1 for stride 1; grows exponentially with depth for stride >1.
- **Pooling layer**: Summarizes a set of adjacent units with a single value; kernel size l, stride s; fixed operation (not learned).
- **Average-pooling**: Computes the average value of l inputs; identical to convolution with uniform kernel [1/l,...,1/l]; facilitates multiscale recognition.
- **Max-pooling**: Computes the maximum value of l inputs; acts as logical disjunction indicating a feature exists somewhere in the receptive field.
- **Downsampling**: Coarsening resolution by a factor of s using pooling with l=s.
- **Tensor**: In deep learning, a multidimensional array of any dimension; used to track "shape" of data through layers.
- **Feature map**: A tensor showing how each feature extracted by a kernel appears across the image; composed of channels.
- **Channel**: A dimension in a feature map carrying information from one feature.
- **Residual network**: Network where a layer perturbs (rather than replaces) the representation from the previous layer: z^{(i)} = g_r(z^{(i-1)} + f(z^{(i-1)})).
- **Residual**: The perturbation f(z) added to the default pass-through; typically a neural network with one nonlinear layer + one linear layer: f(z) = V g(W z).
- **Stochastic gradient descent (SGD)**: Main training algorithm for neural networks; each update uses a minibatch of m examples.
- **Learning rate (α)**: Parameter controlling step size in gradient descent.
- **Momentum**: Keeps running average of gradients of past minibatches to compensate for small minibatch sizes.
- **Batch normalization**: Technique that rescales values at internal layers using minibatch statistics: ˆz_i = γ(z_i - μ)/√(ε+σ²) + β.
- **Adversarial example**: An input altered slightly (e.g., a few pixels changed) to cause a network to misclassify; the altered image still looks correct to humans.
- **Neural architecture search (NAS)**: Automated search over the space of possible network architectures.
- **Weight decay**: Regularization penalty λ∑W²_{i,j} added to loss; implements MAP learning with zero-mean Gaussian prior.
- **Dropout**: Training technique that deactivates a randomly chosen subset of units at each step; approximates ensemble training.
- **Thinned network**: A network with a random subset of units deactivated by dropout.
- **Memory (in RNN)**: Internal state enabling RNN to retain information from earlier time steps.
- **Markov assumption (for RNNs)**: Hidden state z_t suffices to capture information from all previous inputs.
- **Back-propagation through time (BPTT)**: Algorithm for computing gradients in RNNs by unrolling over time steps; cost linear in network size.
- **Exploding gradient**: Problem in RNNs where gradient grows exponentially when weight magnitude >1 (or spectral radius of weight matrix >1).
- **Long short-term memory (LSTM)**: RNN architecture designed to preserve information over many time steps using memory cells and gating units.
- **Memory cell (c)**: Long-term memory component of LSTM; copied from time step to time step (not multiplied by weight matrix).
- **Gating unit**: Vectors controlling information flow in LSTM via elementwise multiplication.
- **Forget gate (f)**: Determines if each element of memory cell is remembered (copied) or forgotten (reset to zero).
- **Input gate (i)**: Determines if each element of memory cell is updated additively by new information.
- **Output gate (o)**: Determines if each element of memory cell is transferred to short-term memory z.
- **Probabilistic PCA (PPCA)**: Generative model where z ~ N(0,I) and x|z ~ N(Wz, σ²I); marginal: P_W(x) = N(x; 0, WW^T+σ²I).
- **Autoencoder**: Model with encoder f mapping x→ẑ and decoder g mapping ẑ→x; trained so x ≈ g(f(x)).
- **Linear autoencoder**: Both f and g are linear with shared weight matrix W; ẑ = Wx, x̂ = W^T ẑ; connected to PCA.
- **Variational autoencoder (VAE)**: Deep generative model using variational methods; decoder defines log P(x|z); encoder defines parameters of variational posterior Q.
- **Variational posterior Q(z)**: Tractable distribution approximating true posterior P(z|x); optimized to minimize KL divergence.
- **Variational lower bound / Evidence lower bound (ELBO)**: L(x,Q) = log P(x) - D_KL(Q(z)||P(z|x)) = H(Q) + E_{z~Q}[log P(z,x)].
- **Autoregressive model (AR model)**: Model where each element x_i is predicted based on other elements; no latent variables.
- **Deep autoregressive model**: AR model where linear-Gaussian predictor is replaced by deep network; e.g., WaveNet.
- **Yule-Walker equations**: Equations for maximum likelihood solution in classical AR models; related to normal equations.
- **Generative adversarial network (GAN)**: Pair of networks — generator maps z→x to produce samples; discriminator classifies inputs as real or fake. Implicit model.
- **Generator**: Network in GAN that produces samples from P_W(x) by transforming noise z.
- **Discriminator**: Network in GAN that classifies inputs as real or fake.
- **Implicit model**: Generative model where samples can be generated but probabilities are not readily available.
- **Unsupervised translation**: Translation between domains (e.g., night→day photos) without paired examples; GAN-based.
- **Transfer learning**: Using experience from one learning task to improve learning on another task; typically by copying learned weights.
- **Multitask learning**: Simultaneously training a model on multiple objectives so it creates a shared representation.
- **Deep reinforcement learning**: Using deep networks to represent value functions, Q-functions, or policies in RL; e.g., DQN, AlphaGo.
- **DQN (Deep Q-Network)**: DeepMind's Atari-playing agent using deep network for Q-function; learned from raw image data with game score as reward.
- **ResNet-50**: A 50-layer residual network pretrained on the COCO dataset for visual object recognition.
- **ROBERTA model**: Pretrained language model for NLP; used as starting point for transfer learning in NLU.
- **AlexNet**: Deep CNN that won 2012 ImageNet competition; 5 convolutional layers + max-pooling + 3 fully connected layers; ReLU activations; 60M weights; GPUs.
- **ImageNet competition**: Supervised learning task with 1,200,000 images in 1,000 categories; top-5 evaluation.
- **COCO dataset**: Common Objects in Context dataset for visual recognition; used for pretrained models.
- **Hopfield network**: Early neural network with symmetric connections between each pair of nodes; stores patterns in associative memory.
- **Boltzmann machine**: Stochastic generalization of Hopfield network; earliest example of deep generative model.
- **Computational neuroscience**: Field aiming to build computational models capturing properties of biological neural systems.
- **Graduate student descent (GSD)**: Humorous term for incremental exploratory architecture search by graduate students.
- **NeurIPS (Neural Information Processing Systems)**: Primary publication venue for deep learning research.
- **ICML (International Conference on Machine Learning)**: Primary publication venue.
- **ICLR (International Conference on Learning Representations)**: Primary publication venue.
- **GPU (Graphics Processing Unit) / TPU (Tensor Processing Unit)**: Specialized hardware for parallel deep learning computation.
- **Turing Award (2018)**: Awarded to Yann LeCun, Yoshua Bengio, and Geoff Hinton for deep learning contributions.
- **B-type unorganized machines**: Alan Turing's 1948 RNN architecture.
- **Perceptron**: One-layer neural network with hard-threshold activation (Rosenblatt, 1957).
- **Perceptron convergence theorem**: Rosenblatt (1960).
- **Madaline**: Early multilayer network (Widrow, 1962).
- **Gamba perceptron**: Early multilayer network (Gamba et al., 1961).
- **PDP (Parallel Distributed Processing)**: Influential two-volume anthology (Rumelhart and McClelland, 1986).
- **Kelley-Bryson gradient procedure**: Original name for back-propagation (Dreyfus, 1990).
- **Neocognitron**: Early CNN architecture (Fukushima, 1980; Fukushima and Miyake, 1982).
- **WaveNet**: Deep autoregressive model for speech generation (van den Oord et al., 2016a); 16,000 samples/sec; AR order 4800.
- **BANANAS**: NAS system predicting accuracy within 1% after 200 random samples (White et al., 2019).
- **ENAS (Efficient Neural Architecture Search)**: Searches for optimal subgraphs of larger graph without retraining (Pham et al., 2018).
- **Optimal brain damage**: Early idea of searching for subgraphs (LeCun et al., 1990).
- **Word embeddings**: Vectors representing words in high-dimensional space; extracted from first hidden layer weights.
- **Principal components analysis (PCA)**: Statistical method dating to Pearson (1901); name from Hotelling (1933).
- **Top-5 error rate**: Metric for ImageNet; fraction of times correct category is NOT in top five predictions.
- **AlphaGo**: DeepMind's Go-playing system using deep RL; defeated best human players.
- **Spatial invariance**: Property of image data where features look similar regardless of spatial location.
- **Temporal invariance**: Property of time-series data where sounds/patterns are similar regardless of time.
- **Cross-correlation**: Signal-processing term; what CNNs call "convolution" is actually cross-correlation.

### 2. PROCESSES / ALGORITHMS — Step-by-Step Procedures

**Back-propagation (General Computation Graph)**:
1. Forward pass: Each node computes function h from its inputs (from f and g), passes value to successors (j and k).
2. Backward pass at each node:
   a. Collect incoming backward messages (∂L/∂h_j and ∂L/∂h_k).
   b. Sum them: ∂L/∂h = ∂L/∂h_j + ∂L/∂h_k (Equation 21.11).
   c. Compute outgoing messages: ∂L/∂f_h = (∂L/∂h)(∂h/∂f_h) and ∂L/∂g_h = (∂L/∂h)(∂h/∂g_h) (Equation 21.12).
3. Process begins at output nodes: ∂L/∂ˆy_j calculated directly from loss expression.
4. Process terminates at weight nodes: sum of incoming messages = ∂L/∂w (the gradient for updating w).
5. Weight-sharing: gradient is sum of gradient contributions from each place weight is used.

**Stochastic Gradient Descent (SGD) Training Loop**:
1. Initialize network parameters w randomly.
2. For each step:
   a. Randomly select minibatch of m examples.
   b. Compute forward pass: ˆy = h_w(x) for each example.
   c. Compute loss L(w) on minibatch.
   d. Back-propagate to compute ∇_w L.
   e. Update: w ← w - α ∇_w L(w).
3. Repeat until convergence (test error stops improving).

**Back-propagation through time (BPTT) for RNN**:
1. Unroll RNN for T time steps to create feedforward network.
2. Compute forward pass through all time steps.
3. Compute loss (summed over time steps).
4. Back-propagate gradients through unrolled network.
5. Accumulate gradient contributions from all time steps for shared weights.
6. Update weights.

**LSTM Update Equations (per time step t)**:
1. Compute forget gate: f_t = σ(W_{x,f} x_t + W_{z,f} z_{t-1})
2. Compute input gate: i_t = σ(W_{x,i} x_t + W_{z,i} z_{t-1})
3. Compute output gate: o_t = σ(W_{x,o} x_t + W_{z,o} z_{t-1})
4. Update memory cell: c_t = c_{t-1} ⊙ f_t + i_t ⊙ tanh(W_{x,c} x_t + W_{z,c} z_{t-1})
5. Update hidden state: z_t = tanh(c_t) ⊙ o_t

**Dropout Algorithm (per minibatch)**:
1. For each node: with probability p, multiply unit output by 1/p; otherwise set output to zero.
2. Apply back-propagation on the resulting thinned network with the current minibatch.
3. Repeat until training complete.
4. At test time, run model with no dropout.

**Batch Normalization (per minibatch)**:
1. For values z_1,...,z_m of a node across minibatch:
2. Compute μ = mean(z_i) across minibatch.
3. Compute σ = standard deviation across minibatch.
4. Replace each z_i: ˆz_i = γ(z_i - μ)/√(ε+σ²) + β, where γ and β are learned parameters.
5. After training, γ and β are fixed.

**Convolution Operation**:
- 1D: z_i = ∑_{j=1}^{l} k_j x_{j+i-(l+1)/2} (Equation 21.8)
- Can be implemented as matrix multiplication with sparse weight matrix containing kernel values.

**Neural Architecture Search (General Approach)**:
1. Define search space (depth, width, connectivity, etc.).
2. Use search technique (evolutionary algorithms, hill climbing, RL, Bayesian optimization, gradient descent).
3. Estimate value of candidate networks (train on test set, evaluate on validation set).
4. Speed-ups: train on smaller dataset, fewer batches, reduced architecture, shared parameters, learn heuristic evaluation function.

### 3. HIERARCHIES / CLASSIFICATIONS

**Types of Neural Networks**:
- Feedforward networks (DAG, no loops)
  - Simple feedforward (fully connected layers)
  - Convolutional networks (spatially local connections, weight sharing)
  - Residual networks (skip connections)
- Recurrent networks (cycles with delay)
  - Basic RNN
  - LSTM (long short-term memory)

**Types of Layers**:
- Input layer (encoding layer)
- Hidden layers
  - Fully connected (dense) layers
  - Convolutional layers
  - Pooling layers (average-pooling, max-pooling)
  - Residual layers
  - Recurrent layers
- Output layers
  - Sigmoid output (binary classification)
  - Softmax output (multiclass classification)
  - Linear output (regression)
  - Mixture density output (mixture of Gaussians)

**Types of Activation Functions**:
- Logistic/Sigmoid: σ(x) = 1/(1+e^{-x})
- ReLU: max(0,x)
- Softplus: log(1+e^x)
- Tanh: (e^{2x}-1)/(e^{2x}+1)

**Types of Pooling**:
- Average-pooling: computes average; facilitates multiscale recognition
- Max-pooling: computes maximum; acts as logical disjunction

**Types of Learning (Chapter 21 framework)**:
- Supervised learning (labeled data)
- Unsupervised learning (unlabeled data)
  - PPCA (probabilistic PCA)
  - Autoencoders (linear, variational)
  - Deep autoregressive models
  - GANs (generative adversarial networks)
- Transfer learning (weights copied from task A to task B)
  - Multitask learning (simultaneous training on multiple objectives)
- Semisupervised learning (some labeled, some unlabeled)

**Types of Regularization / Generalization Methods**:
- Weight decay (L2 penalty)
- Dropout (random unit deactivation)
- Architecture choice (depth, connectivity, layer types)
- Neural architecture search (automated)

### 4. COMPARISONS / TRADE-OFFS

**Shallow vs. Deep Networks**:
- Shallow (linear/logistic regression): short computation paths, inputs contribute independently, only linear functions (Figure 21.1(a)).
- Decision trees: long paths for some inputs but exponentially large if many inputs need long paths (Figure 21.1(b)).
- Deep networks: long computation paths for all inputs, variables interact in complex ways (Figure 21.1(c)).
- Key finding (Figure 21.7): For same number of parameters, deeper network (11-layer) gives much lower test error than shallow (3-layer) network.
- Rolnick and Tegmark (2018): number of units to approximate polynomials of n variables grows exponentially for shallow networks, linearly for deep networks.

**Feedforward vs. Recurrent Networks**:
- Feedforward: DAG, no memory, fixed input size.
- Recurrent: cycles with delay, internal state/memory, handle sequential data of variable length.
- RNN vs. HMM/DBN/Kalman filter (Chapter 14): Similar Markov assumption, but RNNs use learned nonlinear parameterized functions vs. probabilistic models.

**Sigmoid vs. ReLU vs. Softplus vs. Tanh**:
- All monotonically nondecreasing (derivatives g' ≥ 0).
- Sigmoid/Tanh/Softplus: derivatives can be very close to zero (vanishing gradient problem).
- ReLU: derivative exactly zero for negative inputs (can die).
- ReLU/Softplus gained popularity ~2010 partly to mitigate vanishing gradients.

**ADP vs. TD (from Chapter 22, referenced in Ch21 context)**:
- ADP: adjusts state to agree with ALL possible successors weighted by probability; solves Bellman equations; more computation.
- TD: adjusts state to agree with observed successor only; simpler, less computation; cruder approximation.

**Convolutional vs. Fully Connected for Images**:
- Fully connected: n² weights for n pixels and n hidden units; ignores spatial adjacency; treats permuted images same as original.
- Convolutional: l×n weights (l≪n); respects adjacency; exploits spatial invariance via weight replication; d kernels give d×l weights independent of image size n.

**Residual vs. Traditional Networks**:
- Traditional: z^{(i)} = g^{(i)}(W^{(i)} z^{(i-1)}) — each layer replaces previous representation entirely.
- Residual: z^{(i)} = g_r(z^{(i-1)} + f(z^{(i-1)})) — layer perturbs rather than replaces.
- Traditional: catastrophic failure if weights set to zero.
- Residual: setting V=0 disables layer; with ReLU, z^{(i)} = z^{(i-1)} (identity pass-through).
- Residual networks can have hundreds of layers.

**End-to-End Learning vs. Pipeline Approach**:
- Pipeline: errors compounded at each stage; requires manually designed intermediate representations (parse trees, meaning representations).
- End-to-end: single learned function f from input to output; avoids intermediate ground-truth labels; often outperforms pipeline.

**Model-Based vs. Model-Free (Chapter 22 reference)**:
- Model-based: learns transition model and utility function U(s).
- Model-free: learns Q(s,a) directly or policy π(s); no model needed.

### 5. FORMULAS & EQUATIONS

**Unit Computation**:
a_j = g_j(∑_i w_{i,j} a_i) ≡ g_j(in_j)   (vector: a_j = g_j(w^T x))

**Network as Composition (2-layer)**:
h_w(x) = g^{(2)}(W^{(2)} g^{(1)}(W^{(1)} x))

**Simple 3-layer network (Figure 21.3):**
ˆy = g_5(w_{0,5} + w_{3,5} g_3(w_{0,3} + w_{1,3}x_1 + w_{2,3}x_2) + w_{4,5} g_4(w_{0,4} + w_{1,4}x_1 + w_{2,4}x_2))

**Activation Functions**:
- σ(x) = 1/(1+e^{-x})   (sigmoid/logistic)
- ReLU(x) = max(0,x)
- softplus(x) = log(1+e^x)
- tanh(x) = (e^{2x}-1)/(e^{2x}+1)   [range (-1,+1)]
- tanh(x) = 2σ(2x)-1

**Squared Loss**:
Loss(h_w) = L_2(y, h_w(x)) = ‖y - h_w(x)‖² = (y - ˆy)²

**Chain Rule**:
∂g(f(x))/∂x = g'(f(x)) ∂f(x)/∂x

**Gradient for output weight w_{3,5}**:
∂/∂w_{3,5} Loss = -2(y-ˆy) g'_5(in_5) a_3

**Gradient for hidden weight w_{1,3}**:
∂/∂w_{1,3} Loss = -2(y-ˆy) g'_5(in_5) w_{3,5} g'_3(in_3) x_1

**Perceived errors**:
Δ_5 = 2(ˆy - y) g'_5(in_5)
Δ_3 = Δ_5 w_{3,5} g'_3(in_3)

**Maximum Likelihood / Cross-Entropy**:
w* = argmin_w -∑_{j=1}^{N} log P_w(y_j|x_j)

**Cross-Entropy Definition**:
H(P,Q) = E_{z~P(z)}[-log Q(z)] = ∫ P(z) log Q(z) dz  (negative in ML convention)

**Softmax**:
softmax(in)_k = e^{in_k} / ∑_{k'=1}^{d} e^{in_{k'}}

**Convolution (1D)**:
z_i = ∑_{j=1}^{l} k_j x_{j+i-(l+1)/2}

**Residual Layer**:
z^{(i)} = g_r(z^{(i-1)} + f(z^{(i-1)}))
f(z) = V g(W z)

**Gradient Descent Update**:
w ← w - α ∇_w L(w)

**Generic Back-propagation**:
∂L/∂h = ∂L/∂h_j + ∂L/∂h_k   (Equation 21.11)
∂L/∂f_h = (∂L/∂h)(∂h/∂f_h) and ∂L/∂g_h = (∂L/∂h)(∂h/∂g_h)   (Equation 21.12)

**Batch Normalization**:
ˆz_i = γ(z_i - μ)/√(ε+σ²) + β

**Weight Decay**:
Loss_regularized = Loss + λ∑_{i,j} W²_{i,j}

**MAP Interpretation**:
log P(W) = -λ∑_{i,j} W²_{i,j}  → P(W) is zero-mean Gaussian prior

**RNN Update**:
z_t = g_z(W_{z,z} z_{t-1} + W_{x,z} x_t) ≡ g_z(in_{z,t})
ˆy_t = g_y(W_{z,y} z_t) ≡ g_y(in_{y,t})

**RNN Gradient for w_{z,z}**:
∂z_t/∂w_{z,z} = g'_z(in_{z,t})(z_{t-1} + w_{z,z} ∂z_{t-1}/∂w_{z,z})

**LSTM Equations**:
f_t = σ(W_{x,f} x_t + W_{z,f} z_{t-1})
i_t = σ(W_{x,i} x_t + W_{z,i} z_{t-1})
o_t = σ(W_{x,o} x_t + W_{z,o} z_{t-1})
c_t = c_{t-1} ⊙ f_t + i_t ⊙ tanh(W_{x,c} x_t + W_{z,c} z_{t-1})
z_t = tanh(c_t) ⊙ o_t

**PPCA**:
P(z) = N(z; 0, I)
P_W(x|z) = N(x; Wz, σ²I)
P_W(x) = N(x; 0, WW^T + σ²I)

**Variational Lower Bound (ELBO)**:
L(x,Q) = log P(x) - D_KL(Q(z)||P(z|x)) = H(Q) + E_{z~Q}[log P(z,x)]

**Linear Autoencoder**:
ẑ = f(x) = Wx
x̂ = g(ẑ) = W^T ẑ

### 6. RULES, LAWS & THEOREMS

**Universal Approximation Theorem**: A network with just two layers of computational units (first nonlinear, second linear) can approximate any continuous function to an arbitrary degree of accuracy. The proof works by showing an exponentially large network can represent exponentially many "bumps" at different locations.

**Chain Rule**: ∂g(f(x))/∂x = g'(f(x)) ∂f(x)/∂x — the fundamental tool for back-propagation.

**Nonlinearity Requirement**: If activation functions were linear, any composition of units would still represent a linear function. The nonlinearity allows sufficiently large networks to represent arbitrary functions.

**Gradient Computation Structure**: For any feedforward computation graph, gradient computations have the same structure as the underlying computation graph (back-propagation).

**Weight-sharing gradient rule**: Gradient for a shared weight = sum of gradient contributions from each place it is used in the network.

**ReLU Identity**: ReLU(ReLU(x)) = ReLU(x) — used for residual network identity mapping.

**Back-propagation cost**: Computational cost is linear in number of nodes in the computation graph.

### 7. DATA STRUCTURES & TYPES

**Weight Matrix W**: Represents all weights in a layer; W^{(1)} for first layer, etc.

**Tensors**: Multidimensional arrays used to track "shape" of data through CNN layers. Example input: 256×256×3×64 tensor (256×256 RGB images, minibatch 64). After 96 kernels 5×5×3, stride 2: output 128×128×96×64.

**Computation Graph**: Nodes represent elementary computations (addition, multiplication, sigmoid, etc.); edges represent data flow; distinguishes inputs (blue) from weights (light mauve).

**Feature Map**: Tensor showing feature activation across image; composed of channels (one per kernel).

**Memory Cell (LSTM)**: c_t vector; copied (not multiplied) across time steps; gated by forget, input, and output gates.

**Joint State Space (for HRL)**: Each state (s,m) pairs physical state s with machine state m (program counter, call stack, variables).

**Choice State (σ)**: State where program counter is at a choice point in the agent program.

### 8. VISUAL PATTERNS

**Figure 21.1 (p.751)**: Three diagrams comparing computation paths:
(a) Shallow model (linear regression) — very short paths.
(b) Decision list — some long paths for some inputs.
(c) Deep learning network — long paths for all inputs.

**Figure 21.2 (p.752)**: Three plots of activation functions:
(a) Logistic/sigmoid function (S-curve from 0 to 1).
(b) ReLU (flat at 0 for negative, linear for positive) and softplus (smooth version of ReLU).
(c) Tanh function (S-curve from -1 to +1).

**Figure 21.3 (p.753)**: Two representations of a 2-input, 2-hidden-unit, 1-output network:
(a) Traditional neural network diagram (circles and arrows).
(b) Computation graph (unpacked, showing each elementary operation).

**Figure 21.4 (p.761)**: 1D convolution example with kernel [+1,-1,+1], stride s=2. Input: [5,6,6,2,5,6,5], Output: [5,9,4]. Peak response centered on darker (lower intensity) pixel.

**Figure 21.5 (p.762)**: First two layers of a CNN for 1D image (kernel size 3, stride 1). Padding at edges to keep hidden layers same size as input. Shows receptive field of unit in second hidden layer growing to 5 pixels.

**Figure 21.6 (p.766)**: Generic node in computation graph with forward computation (left→right) and back-propagation (right→left). Node h gets inputs from f,g and feeds to j,k. Message passing shows ∂L/∂h_j, ∂L/∂h_k flowing backward.

**Figure 21.7 (p.769)**: Test-set error vs. number of weights for 3-layer and 11-layer CNNs on Street View house number recognition. 11-layer network consistently outperforms 3-layer for any given number of weights.

**Figure 21.8 (p.773)**: RNN diagrams:
(a) Basic RNN with hidden layer z having recurrent connections (delay symbol Δ).
(b) Unrolled over 3 time steps (feedforward network with weight sharing).

**Figure 21.9 (p.777)**: Generative model demonstrating arithmetic in z-space. Starting from "man with glasses," subtract "man," add "woman" → "woman with glasses."

### 9. EDGE CASES / EXCEPTIONS / TRAPS

**Vanishing Gradient**: Error signals extinguished as propagated back through deep networks because g'_j(in_j) can be very close to zero (sigmoid, softplus, tanh) or exactly zero (ReLU). Deep networks with many layers suffer from this.

**Exploding Gradient**: In RNNs, if w_{z,z} > 1 (or spectral radius of W_{z,z} > 1), gradient grows exponentially with time steps.

**Numerical Instabilities**: Overflows, underflows, rounding errors; particularly problematic with exponentials in softmax, sigmoid, tanh; iterated computations in very deep/recurrent networks.

**Catastrophic Failure in Traditional Networks**: Setting W^{(i)} = 0 for any layer causes entire network to cease functioning; layers must learn to propagate information.

**Adversarial Examples**: Small input perturbations (e.g., altering few pixels) cause misclassification; the altered image still looks correct to humans. Adversarial examples can transfer across different networks. Attackers currently ahead of defenders.

**Discontinuous Input-Output Mapping**: Deep learning models can have large output changes from small input changes.

**Storage Cost of Back-propagation**: Requires storing most intermediate forward values; total memory cost proportional to number of units in entire network.

**No Batch Norm Understanding**: Reasons for batch normalization's effectiveness not well understood at time of writing.

**Catastrophic Forgetting (RL context, Ch22, mentioned in Ch21 context)**: After learning one behavior, network may forget previously learned distinctions.

**Lack of Expressive Power**: Deep learning models lack compositional and quantificational expressive power of first-order logic and context-free grammars.

**Overfitting**: More layers/weights can cause overfitting; addressed by weight decay, dropout, architecture search.

**Large Data Requirements**: Supervised deep learning often requires far more labeled data than a human would need.

### 10. EMPIRICAL EVIDENCE / KEY RESULTS

**ImageNet 2012 (AlexNet)**:
- 1,200,000 images, 1,000 categories
- AlexNet top-5 error: 15.3%
- Next best system: >25%
- Since 2012: top-5 error reduced to <2% (below human ~5%)

**Street View House Numbers (Figure 21.7)**:
- 11-layer CNN test error < 3-layer CNN test error for same number of weights
- Demonstrates depth advantage for generalization

**End-to-End Translation (Wu et al., 2016b)**:
- Reduced translation errors by 60% relative to pipeline-based system
- Approaching human performance for French-English with large datasets

**WaveNet (van den Oord et al., 2016a)**:
- Substantially more realistic speech generation than previous state-of-the-art

**GANs (Karras et al., 2017)**:
- Can create photorealistic, high-resolution images of people who never existed

**Deep RL (DQN; Mnih et al., 2013)**:
- Atari games from raw pixels; superhuman on majority of 57 games
- AlphaGo: defeated best human Go players

**Residual Networks**:
- Common to see hundreds of layers
- Setting V=0 disables a layer; network still functions

**Deep learning vs. traditional ML**:
- Outperforms all other approaches for high-dimensional inputs (images, video, speech)
- Prior to 2010: manually designed features + traditional ML; not comparable performance

**Transfer Learning**:
- COCO dataset: 3,000+ images in each of categories (bicycle, motorcycle, skateboard)
- Sim-to-real: billions of miles of simulated driving → real vehicle adapts quickly

**Multi-language Translation**: Networks trained on Portuguese→English and English→Spanish can translate Portuguese→Spanish without direct training pairs.

### 11. CROSS-CHAPTER DEPENDENCIES

**Chapter 19 (Machine Learning basics)**: Deep learning builds on gradient descent (Section 19.6), supervised learning, loss functions, regularization, hyperparameter tuning. "If you have not already read Section 19.6, we recommend strongly that you do so before continuing."

**Chapter 20 (Learning probabilistic models)**: Maximum likelihood learning, Bayes nets, EM algorithm, MAP learning — foundational for understanding probabilistic generative models in Ch21.

**Chapter 17 (Reinforcement Learning basics)**: Value functions, Q-functions, policies — referenced for deep RL (Section 21.8.3).

**Chapter 22 (Reinforcement Learning)**: Deep RL used extensively; Chapter 21 provides the function approximation backbone for Ch22. DQN and AlphaGo are mentioned in both.

**Chapter 24 (Natural Language Processing)**: RNNs/LSTMs for NLP; word embeddings; transfer learning; ROBERTA model. Deep learning for machine translation.

**Chapter 25 (Computer Vision)**: CNNs for vision; Section 25.4 covers deep learning in vision; Section 25.7.5 covers unsupervised translation.

**Chapter 26 (Robotics)**: Deep learning for robotics.

**Chapter 14 (Probabilistic Reasoning)**: RNNs compared to HMMs, DBNs, Kalman filters. Markov assumption.

**Chapter 4 (Search)**: Optimization methods for high-dimensional continuous spaces.

**Chapter 5 (Adversarial Search)**: Monte Carlo tree search; AlphaGo.

**Chapter 8 (Logic)**: Deep learning lacks compositional/quantificational power of first-order logic and context-free grammars (Chapter 23).

**Chapter 23 (NLP)**: n-gram models as autoregressive models.

### 12. DATES & PEOPLE

- **McCulloch and Pitts (1943)**: Early work modeling networks of neurons.
- **Rashevsky (1936, 1938)**: Earliest mathematical model of neural learning (McCarthy's attribution).
- **Wiener (1948)**: Pioneer of cybernetics and control theory.
- **Turing (1948)**: "Intelligent Machinery" describing RNN architecture ("B-type unorganized machines"); unpublished until 1969.
- **Rosenblatt (1957)**: Popularized the perceptron.
- **Rosenblatt (1960)**: Proved perceptron convergence theorem.
- **Agmon (1954), Motzkin and Schoenberg (1954)**: Foreshadowed perceptron convergence theorem mathematically.
- **Gamba et al. (1961)**: Gamba perceptrons.
- **Widrow (1962)**: Madalines.
- **Hawkins (1961)**: Acknowledged limitations of single-layer perceptrons.
- **Minsky and Papert (1969)**: "Perceptrons" — lamented lack of mathematical rigor; pointed out limitations.
- **Nilsson (1965)**: "Learning Machines."
- **Hinton and Anderson (1981)**: Papers marking renaissance of connectionism.
- **Rumelhart and McClelland (1986)**: Two-volume "PDP" anthology.
- **Back-propagation rediscoveries**: Kelley (1960), Bryson (1962), Dreyfus (1962), Bryson and Ho (1969), Werbos (1974), Parker (1985), Rumelhart-Hinton-Williams (1986) in Nature.
- **Dreyfus (1990)**: Called it "Kelley-Bryson gradient procedure."
- **Cybenko (1988, 1989)**: Universal function approximation theorems.
- **Hubel and Wiesel (1959, 1962, 1968)**: Described "simple cells" and "complex cells" in cat visual cortex.
- **Marr and Poggio (1976)**: Early connectionist vision models inspired by Hubel and Wiesel.
- **Fukushima (1980), Fukushima and Miyake (1982)**: Neocognitron.
- **LeCun et al. (1995)**: Applied back-propagation to CNNs; handwritten digit recognition.
- **Elman (1990)**: Influential early RNN work.
- **Jordan (1986)**: RNN architecture that Elman built upon.
- **Williams and Zipser (1989)**: Online learning in RNNs.
- **Bengio et al. (1994)**: Analyzed vanishing gradients in RNNs.
- **Hochreiter (1991), Hochreiter and Schmidhuber (1997), Gers et al. (2000)**: LSTM architecture.
- **Krizhevsky et al. (2013)**: Used deep CNNs to win ImageNet.
- **Jarrett et al. (2009), Nair and Hinton (2010), Glorot et al. (2011)**: Adoption of ReLU.
- **He et al. (2016)**: Residual networks.
- **Bottou and Bousquet (2008)**: SGD with small batches for large datasets.
- **Ioffe and Szegedy (2015)**: Batch normalization.
- **Hinton (1987)**: Suggested weight decay.
- **Krogh and Hertz (1992)**: Mathematical analysis of weight decay.
- **Srivastava et al. (2014a)**: Dropout method.
- **Szegedy et al. (2013)**: Introduced adversarial examples.
- **Goodfellow et al. (2016)**: Modern deep learning textbook.
- **Charniak (2018)**: Deep learning textbook.
- **LeCun, Bengio, Hinton (2015)**: Influential Nature article introducing deep learning to non-AI researchers.
- **LeCun, Bengio, Hinton (2018)**: Recipients of the Turing Award.
- **Schmidhuber (2015)**: General overview of deep learning.
- **Deng et al. (2014)**: Signal processing tasks.
- **Pearson (1901)**: PCA.
- **Hotelling (1933)**: PCA name.
- **Tipping and Bishop (1999)**: Probabilistic PCA.
- **Kingma and Welling (2013), Rezende et al. (2014)**: Variational autoencoder.
- **Jordan et al. (1999)**: Introduction to variational methods.
- **Box et al. (2016)**: Classic autoregressive models text.
- **Yule (1927), Walker (1931)**: Yule-Walker equations.
- **Frey (1998), Bengio and Bengio (2001), Larochelle and Murray (2011)**: Autoregressive models with nonlinear dependencies.
- **van den Oord et al. (2016a)**: WaveNet.
- **Goodfellow et al. (2015a)**: GANs.
- **Hopfield (1982)**: Hopfield networks.
- **Hinton and Sejnowski (1983, 1986)**: Boltzmann machines.
- **Dayan and Abbott (2001), Trappenberg (2010)**: Computational neuroscience overviews.

### 13. PROOF & ARGUMENT PATTERNS

**Universal Approximation Theorem (argument sketch)**: An exponentially large network can represent exponentially many "bumps" at different heights and locations, approximating any continuous function — analogous to sufficiently large decision trees implementing look-up tables for Boolean functions.

**Chain Rule Derivation of Back-propagation** (Equations 21.4 and 21.5):
- For output weight w_{3,5}: direct application of chain rule, ∂Loss/∂w = -2(y-ˆy) g'_5(in_5) a_3.
- For hidden weight w_{1,3}: extended chain rule, ∂Loss/∂w = -2(y-ˆy) g'_5(in_5) w_{3,5} g'_3(in_3) x_1.
- Pattern generalizes: "perceived error" propagates backward via Δ_5 = 2(ˆy-y)g'_5(in_5), Δ_3 = Δ_5 w_{3,5} g'_3(in_3), giving gradient = Δ_j × (input to that weight).

**Residual Network Identity Proof**: If V=0, f(z)=0, so z^{(i)} = g_r(z^{(i-1)}). With ReLU activations, z^{(i-1)} = ReLU(in^{(i-1)}), so z^{(i)} = ReLU(z^{(i-1)}) = ReLU(ReLU(in^{(i-1)})) = ReLU(in^{(i-1)}) = z^{(i-1)}. Thus a zero-weight residual layer passes input through unchanged.

**Back-propagation on Computation Graph**:
- For any node h with successors j,k: ∂L/∂h = ∂L/∂h_j + ∂L/∂h_k (summing incoming messages — Equation 21.11).
- Outgoing messages: ∂L/∂f_h = (∂L/∂h)(∂h/∂f_h) and similarly for g_h (Equation 21.12).
- Process is linear in number of nodes (same as forward pass).

**Vanishing Gradient Analysis for RNN**: Gradients at T include terms proportional to w_{z,z} ∏_{t=1}^{T} g'_z(in_{z,t}). Since g' ≤ 1 for sigmoids, tanhs, ReLUs, gradient vanishes if w_{z,z} < 1; explodes if w_{z,z} > 1.

### 14. DESIGN PARADIGMS / META-METHODS

**End-to-End Learning**: Design entire system as a single differentiable computation graph; train from input/output pairs; no need to manually design intermediate representations or label internal stages.

**Prior Knowledge Injection via Architecture**: CNNs encode adjacency and spatial invariance; RNNs encode temporal invariance/time-homogeneous dynamics. By choosing architecture, designer injects knowledge about data structure.

**Weight Sharing**: Same parameters used at multiple locations (convolution kernels across spatial positions, RNN weights across time steps). Reduces parameter count, enforces invariance.

**Residual/Difference Paradigm**: Instead of learning a complete transformation, learn a perturbation to identity (residual). Makes very deep networks trainable.

**Gradient-Based Meta-Learning**: Neural architecture search via gradient descent on continuous relaxation of architecture space.

**Denoising / Robustness via Randomization**: Dropout forces robustness by randomly deactivating units; approximates ensemble methods.

**Computation Graph Abstraction**: Any computation can be represented as graph of differentiable operations; gradients computed automatically via back-propagation.

**Layer Composition Pattern**: Deep networks = composition of many simple transformations, each learned by local updating process.

**Factorized Representations**: Word embeddings as distributed representations; latent variable z in generative models.

**Two-Part Generative Models** (Autoencoder/VAE): Encoder compresses x→z; decoder reconstructs x from z.

**Adversarial Training (GANs)**: Two networks compete — generator tries to fool discriminator; discriminator tries to distinguish real from fake.

### 15. CASE STUDIES / CLASSIC EXAMPLES

**Simple 3-Layer Network Example (Figure 21.3)**: 2 inputs → 2 hidden units → 1 output. Full algebraic expression (Equation 21.2): ˆy = g_5(w_{0,5} + w_{3,5}g_3(w_{0,3} + w_{1,3}x_1 + w_{2,3}x_2) + w_{4,5}g_4(w_{0,4} + w_{1,4}x_1 + w_{2,4}x_2)).

**1D Convolution Example (Figure 21.4)**: Kernel [+1,-1,+1], stride 2. Input [5,6,6,2,5,6,5] → Output [5,9,4]. Matrix formulation (Equation 21.9): 3×7 sparse matrix times 7-vector.

**CNN Tensor Example**: 256×256 RGB images, minibatch 64 → 4D tensor 256×256×3×64. After 96 kernels 5×5×3, stride 2 → output tensor 128×128×96×64 (feature map with 96 channels).

**ImageNet/AlexNet (2012)**: 5 convolutional layers + max-pooling + 3 fully connected layers; ReLU; 60M weights; GPUs. Error 15.3% vs. next best >25%.

**Street View House Numbers**: Comparing 3-layer vs. 11-layer CNNs. 11-layer much better for same number of weights (Figure 21.7).

**WaveNet**: Raw audio sampled 16,000/sec; autoregressive model of order 4800; multilayer convolutional structure.

**Japanese Cucumber Sorting**: (Mythical) story from Zeeberg (2017). Actual: farmer's son (ex-Toyota engineer) built TensorFlow-based sorter; ~70% accuracy; cucumbers still hand-sorted.

**Multi-language Translation**: Portuguese→English + English→Spanish training enables Portuguese→Spanish translation without direct pairs.

**Word Embeddings**: "apples" and "bananas" have similar vector representations because they appear in similar contexts. Generalization without human-defined categories.

### 16. ETHICS CONSIDERATIONS

**Adversarial Examples**: Deep networks can be fooled by small perturbations invisible to humans. This raises security concerns for deployment (self-driving cars, face recognition, etc.). Attackers currently ahead of defenders. Adversarial examples transfer across different networks, suggesting deep learning recognizes objects differently from human vision.

**Data Requirements**: Deep learning often requires far more labeled data than humans. This renders some tasks unattainable if label requirements exceed what humanity can supply. Labeling large datasets requires scarce and expensive human labor.

**End-to-End Learning Limitations**: The designer need only have a vague idea about system structure; there is no need to understand what each subsystem does. This raises interpretability concerns.

**Deep RL Concerns**: Systems may behave very unpredictably if environment differs even slightly from training data (Irpan, 2018). Rarely applied in commercial settings.

**Biased Training Data**: Not explicitly discussed in Chapter 21, but the reliance on large datasets implies susceptibility to dataset bias.

**Generative Model Risks**: GANs can create photorealistic images of people who have never existed (deepfakes); unsupervised translation can alter images in ways that may be misleading.

**Weapons/Toxicity**: Not discussed, but the chapter acknowledges that deep learning currently dominates applications from vision to NLP, implying dual-use potential.

### 17. END-OF-CHAPTER MATERIAL

**Summary** (lines 34329-34341):
- Neural networks represent complex nonlinear functions with a network of parameterized linear-threshold units.
- The back-propagation algorithm implements a gradient descent in parameter space to minimize the loss function.
- Deep learning works well for visual object recognition, speech recognition, natural language processing, and reinforcement learning in complex environments.
- Convolutional networks are particularly well suited for image processing and other tasks where the data have a grid topology.
- Recurrent networks are effective for sequence-processing tasks including language modeling and machine translation.

**Bibliographical and Historical Notes** (lines 34344-34513):
[Full content reproduced below]
The literature on neural networks is vast. Cowan and Sharp (1988b, 1988a) survey the early history, beginning with the work of McCulloch and Pitts (1943). (As mentioned in Chapter 1, John McCarthy has pointed to the work of Nicolas Rashevsky (1936, 1938) as the earliest mathematical model of neural learning.) Norbert Wiener, a pioneer of cybernetics and control theory (Wiener, 1948), worked with McCulloch and Pitts and influenced a number of young researchers, including Marvin Minsky, who may have been the first to develop a working neural network in hardware, in 1951 (see Minsky and Papert, 1988, pp. ix-x). Alan Turing (1948) wrote a research report titled Intelligent Machinery that begins with the sentence "I propose to investigate the question as to whether it is possible for machinery to show intelligent behaviour" and goes on to describe a recurrent neural network architecture he called "B-type unorganized machines" and an approach to training them. Unfortunately, the report went unpublished until 1969, and was all but ignored until recently.

The perceptron, a one-layer neural network with a hard-threshold activation function, was popularized by Frank Rosenblatt (1957). After a demonstration in July 1958, the New York Times described it as "the embryo of an electronic computer that [the Navy] expects will be able to walk, talk, see, write, reproduce itself and be conscious of its existence." Rosenblatt (1960) later proved the perceptron convergence theorem, although it had been foreshadowed by purely mathematical work outside the context of neural networks (Agmon, 1954; Motzkin and Schoenberg, 1954). Some early work was also done on multilayer networks, including Gamba perceptrons (Gamba et al., 1961) and madalines (Widrow, 1962). Learning Machines (Nilsson, 1965) covers much of this early work and more. The subsequent demise of early perceptron research efforts was hastened (or, the authors later claimed, merely explained) by the book Perceptrons (Minsky and Papert, 1969), which lamented the field's lack of mathematical rigor. The book pointed out that single-layer perceptrons could represent only linearly separable concepts and noted the lack of effective learning algorithms for multilayer networks. These limitations were already well known (Hawkins, 1961) and had been acknowledged by Rosenblatt himself (Rosenblatt, 1962).

The papers collected by Hinton and Anderson (1981), based on a conference in San Diego in 1979, can be regarded as marking a renaissance of connectionism. The two-volume "PDP" (Parallel Distributed Processing) anthology (Rumelhart and McClelland, 1986) helped to spread the gospel, so to speak, particularly in the psychology and cognitive science communities. The most important development of this period was the back-propagation algorithm for training multilayer networks.

The back-propagation algorithm was discovered independently several times in different contexts (Kelley, 1960; Bryson, 1962; Dreyfus, 1962; Bryson and Ho, 1969; Werbos, 1974; Parker, 1985) and Stuart Dreyfus (1990) calls it the "Kelley-Bryson gradient procedure." Although Werbos had applied it to neural networks, this idea did not become widely known until a paper by David Rumelhart, Geoff Hinton, and Ron Williams (1986) appeared in Nature giving a nonmathematical presentation of the algorithm. Mathematical respectability was enhanced by papers showing that multilayer feedforward networks are (subject to technical conditions) universal function approximators (Cybenko, 1988, 1989). The late 1980s and early 1990s saw a huge growth in neural network research: the number of papers mushroomed by a factor of 200 between 1980-84 and 1990-94.

In the late 1990s and early 2000s, interest in neural networks waned as other techniques such as Bayes nets, ensemble methods, and kernel machines came to the fore. Interest in deep models was sparked when Geoff Hinton's research on deep Bayesian networks—generative models with category variables at the root and evidence variables at the leaves—began to bear fruit, outperforming kernel machines on small benchmark data sets (Hinton et al., 2006). Interest in deep learning exploded when Krizhevsky et al. (2013) used deep convolutional networks to win the ImageNet competition (Russakovsky et al., 2015).

Commentators often cite the availability of "big data" and the processing power of GPUs as the main contributing factors in the emergence of deep learning. Architectural improvements were also important, including the adoption of the ReLU activation function instead of the logistic sigmoid (Jarrett et al., 2009; Nair and Hinton, 2010; Glorot et al., 2011) and later the development of residual networks (He et al., 2016).

On the algorithmic side, the use of stochastic gradient descent (SGD) with small batches was essential in allowing neural networks to scale to large data sets (Bottou and Bousquet, 2008). Batch normalization (Ioffe and Szegedy, 2015) also helped in making the training process faster and more reliable and has spawned several additional normalization techniques (Ba et al., 2016; Wu and He, 2018; Miyato et al., 2018). Several papers have studied the empirical behavior of SGD on large networks and large data sets (Dauphin et al., 2015; Choromanska et al., 2014; Goodfellow et al., 2015b). On the theoretical side, some progress has been made on explaining the observation that SGD applied to overparameterized networks often reaches a global minimum with a training error of zero, although so far the theorems to this effect assume a network with layers far wider than would ever occur in practice (Allen-Zhu et al., 2018; Du et al., 2018). Such networks have more than enough capacity to function as lookup tables for the training data.

The last piece of the puzzle, at least for vision applications, was the use of convolutional networks. These had their origins in the descriptions of the mammalian visual system by neurophysiologists David Hubel and Torsten Wiesel (Hubel and Wiesel, 1959, 1962, 1968). They described "simple cells" in the visual system of a cat that resemble edge detectors, as well as "complex cells" that are invariant to some transformations such as small spatial translations. In modern convolutional networks, the output of a convolution is analogous to a simple cell while the output of a pooling layer is analogous to a complex cell.

The work of Hubel and Wiesel inspired many of the early connectionist models of vision (Marr and Poggio, 1976). The neocognitron (Fukushima, 1980; Fukushima and Miyake, 1982), designed as a model of the visual cortex, was essentially a convolutional network in terms of model architecture, although an effective training algorithm for such networks had to wait until Yann LeCun and collaborators showed how to apply back-propagation (LeCun et al., 1995). One of the early commercial successes of neural networks was handwritten digit recognition using convolutional networks (LeCun et al., 1995).

Recurrent neural networks (RNNs) were commonly proposed as models of brain function in the 1970s, but no effective learning algorithms were associated with these proposals. The method of back-propagation through time appears in the PhD thesis of Paul Werbos (1974), and his later review paper (Werbos, 1990) gives several additional references to rediscoveries of the method in the 1980s. One of the most influential early works on RNNs was due to Jeff Elman (1990), building on an RNN architecture suggested by Michael Jordan (1986). Williams and Zipser (1989) present an algorithm for online learning in RNNs. Bengio et al. (1994) analyzed the problem of vanishing gradients in recurrent networks. The long short-term memory (LSTM) architecture (Hochreiter, 1991; Hochreiter and Schmidhuber, 1997; Gers et al., 2000) was proposed as a way of avoiding this problem. More recently, effective RNN designs have been derived automatically (Jozefowicz et al., 2015; Zoph and Le, 2016).

Many methods have been tried for improving generalization in neural networks. Weight decay was suggested by Hinton (1987) and analyzed mathematically by Krogh and Hertz (1992). The dropout method is due to Srivastava et al. (2014a). Szegedy et al. (2013) introduced the idea of adversarial examples, spawning a huge literature.

Poole et al. (2017) showed that deep networks (but not shallow ones) can disentangle complex functions into flat manifolds in the space of hidden units. Rolnick and Tegmark (2018) showed that the number of units required to approximate a certain class of polynomials of n variables grows exponentially for shallow networks but only linearly for deep networks.

White et al. (2019) showed that their BANANAS system could do neural architecture search (NAS) by predicting the accuracy of a network to within 1% after training on just 200 random sample architectures. Zoph and Le (2016) use reinforcement learning to search the space of neural network architectures. Real et al. (2018) use an evolutionary algorithm to do model selection, Liu et al. (2017) use evolutionary algorithms on hierarchical representations, and Jaderberg et al. (2017) describe population-based training. Liu et al. (2019) relax the space of architectures to a continuous differentiable space and use gradient descent to find a locally optimal solution. Pham et al. (2018) describe the ENAS (Efficient Neural Architecture Search) system, which searches for optimal subgraphs of a larger graph. It is fast because it does not need to retrain parameters. The idea of searching for a subgraph goes back to the "optimal brain damage" algorithm of LeCun et al. (1990).

Despite this impressive array of approaches, there are critics who feel the field has not yet matured. Yu et al. (2019) show that in some cases these NAS algorithms are no more efficient than random architecture selection. For a survey of recent results in neural architecture search, see Elsken et al. (2018).

Unsupervised learning constitutes a large subfield within statistics, mostly under the heading of density estimation. Silverman (1986) and Murphy (2012) are good sources for classical and modern techniques in this area. Principal components analysis (PCA) dates back to Pearson (1901); the name comes from independent work by Hotelling (1933). The probabilistic PCA model (Tipping and Bishop, 1999) adds a generative model for the principal components themselves. The variational autoencoder is due to Kingma and Welling (2013) and Rezende et al. (2014); Jordan et al. (1999) provide an introduction to variational methods for inference in graphical models.

For autoregressive models, the classic text is by Box et al. (2016). The Yule-Walker equations for fitting AR models were developed independently by Yule (1927) and Walker (1931). Autoregressive models with nonlinear dependencies were developed by several authors (Frey, 1998; Bengio and Bengio, 2001; Larochelle and Murray, 2011). The autoregressive WaveNet model (van den Oord et al., 2016a) was based on earlier work on autoregressive image generation (van den Oord et al., 2016b). Generative adversarial networks, or GANs, were first proposed by Goodfellow et al. (2015a), and have found many applications in AI. Some theoretical understanding of their properties is emerging, leading to improved GAN models and algorithms (Li and Malik, 2018b, 2018a; Zhu et al., 2019). Part of that understanding involves protecting against adversarial attacks (Carlini et al., 2019).

Several branches of research into neural networks have been popular in the past but are not actively explored today. Hopfield networks (Hopfield, 1982) have symmetric connections between each pair of nodes and can learn to store patterns in an associative memory, so that an entire pattern can be retrieved by indexing into the memory using a fragment of the pattern. Hopfield networks are deterministic; they were later generalized to stochastic Boltzmann machines (Hinton and Sejnowski, 1983, 1986). Boltzmann machines are possibly the earliest example of a deep generative model. The difficulty of inference in Boltzmann machines led to advances in both Monte Carlo techniques and variational techniques (see Section 13.4).

Research on neural networks for AI has also been intertwined to some extent with research into biological neural networks. The two topics coincided in the 1940s, and ideas for convolutional networks and reinforcement learning can be traced to studies of biological systems; but at present, new ideas in deep learning tend to be based on purely computational or statistical concerns. The field of computational neuroscience aims to build computational models that capture important and specific properties of actual biological systems. Overviews are given by Dayan and Abbott (2001) and Trappenberg (2010).

For modern neural nets and deep learning, the leading textbooks are those by Goodfellow et al. (2016) and Charniak (2018). There are also many hands-on guides associated with the various open-source software packages for deep learning. Three of the leaders of the field—Yann LeCun, Yoshua Bengio, and Geoff Hinton—introduced the key ideas to non-AI researchers in an influential Nature article (2015). The three were recipients of the 2018 Turing Award. Schmidhuber (2015) provides a general overview, and Deng et al. (2014) focus on signal processing tasks.

The primary publication venues for deep learning research are the conference on Neural Information Processing Systems (NeurIPS), the International Conference on Machine Learning (ICML), and the International Conference on Learning Representations (ICLR). The main journals are Machine Learning, the Journal of Machine Learning Research, and Neural Computation. Increasingly, because of the fast pace of research, papers appear first on arXiv.org and are often described in the research blogs of the major research centers.

**End of Chapter 21**

---

## CHAPTER 22: REINFORCEMENT LEARNING (lines 34515-36063)

### 1. NAMED ENTITIES — Every Term/Concept with Definition

- **Reinforcement learning (RL)**: An agent interacts with the world and periodically receives rewards (reinforcements) reflecting how well it is doing; goal is to maximize expected sum of rewards.
- **Sparse rewards**: Reward signal that is informative only in a small fraction of states (e.g., win/loss in chess).
- **Model-based reinforcement learning**: Agent uses a transition model of the environment to interpret reward signals and make decisions; may learn the model from observations.
- **Model-free reinforcement learning**: Agent neither knows nor learns a transition model; learns a direct representation of how to behave.
- **Action-utility learning**: Learning Q-function Q(s,a) — sum of rewards from state s onward if action a is taken.
- **Q-learning**: Most common form of action-utility learning.
- **Q-function / quality-function**: Q(s,a) denoting sum of rewards from state s onward if action a is taken.
- **Policy search**: Agent learns a policy π(s) mapping directly from states to actions (a reflex agent).
- **Passive reinforcement learning**: Agent's policy is fixed; task is to learn utilities of states (or state-action pairs).
- **Active reinforcement learning**: Agent must also figure out what to do; key issue is exploration.
- **Passive learning agent**: Agent with fixed policy trying to learn utility function U^π(s).
- **Trial**: A single sequence of state transitions from start state to terminal state.
- **Direct utility estimation**: Utility of state = expected total reward from that state onward (expected reward-to-go); each trial provides sample.
- **Reward-to-go**: Expected total reward from a state onward.
- **Adaptive dynamic programming (ADP)**: Learns transition model and solves MDP using dynamic programming.
- **Temporal-difference (TD) learning**: Adjusts utility estimates to be more consistent with successor states using observed transitions; no transition model needed for updates.
- **Pseudoexperience**: Simulated transitions generated from learned transition model; extends TD toward ADP.
- **Prioritized sweeping**: Heuristic for approximate ADP; prefers adjustments to states whose likely successors had large utility adjustments.
- **Greedy agent**: Agent that takes the action it currently believes to be optimal at each step; may converge to suboptimal policy.
- **GLIE (Greedy in the Limit of Infinite Exploration)**: Scheme that tries each action in each state an unbounded number of times; e.g., choose random action with probability 1/t, follow greedy policy otherwise.
- **Exploration function f(u,n)**: Determines tradeoff between greed (high u) and curiosity (low count n); increasing in u, decreasing in n.
- **Optimistic estimate U⁺(s)**: Utility estimate with exploration bonus; causes agent to initially behave as if wonderful rewards are everywhere.
- **SARSA (State-Action-Reward-State-Action)**: On-policy TD algorithm; updates Q(s,a) using Q(s',a') of the action actually taken; update at end of s,a,r,s',a' quintuplet.
- **Off-policy learning**: Learns Q-values for what would happen if agent stopped using current policy and used greedy policy (Q-learning).
- **On-policy learning**: Learns Q-values for what would happen if agent sticks with current policy (SARSA).
- **Safe exploration**: Avoiding irreversible actions and absorbing states during learning.
- **Absorbing state**: State where no actions have any effect and no rewards are received.
- **Bayesian reinforcement learning**: Assumes prior over hypotheses about true model; computes posterior via Bayes' rule; optimal policy maximizes expected utility over model posterior.
- **Exploration POMDP**: Problem of optimal exploration formulated as a POMDP whose belief states are distributions over models.
- **Robust control theory**: Assumes set of possible models without probabilities; optimal robust policy gives best outcome in worst case over models.
- **Function approximation**: Constructing compact approximation of true utility function or Q-function (e.g., weighted linear combination of features).
- **Widrow-Hoff rule / Delta rule**: Online least-squares update: θ_i ← θ_i + α[u_j(s) - Û_θ(s)] ∂Û_θ(s)/∂θ_i.
- **Catastrophic forgetting**: Problem where function approximator loses previously learned information about parts of state space no longer visited.
- **Experience replay**: Retaining trajectories from entire learning process and replaying them to keep value function accurate for all state space regions.
- **Deep reinforcement learning**: Using deep neural networks as function approximators for RL.
- **Credit assignment problem**: Difficulty in determining which actions are responsible for observed rewards, especially with sparse/long-delayed rewards.
- **Reward shaping**: Providing additional pseudorewards for "making progress" to speed learning.
- **Pseudoreward**: Additional reward supplied to guide learning (e.g., for advancing ball toward goal).
- **Potential function Φ(s)**: Function used to modify reward without changing optimal policy: R'(s,a,s') = R(s,a,s') + γΦ(s') - Φ(s).
- **Hierarchical reinforcement learning (HRL)**: Breaking long action sequences into hierarchy of smaller pieces; like HTN planning.
- **Partial program**: Program with unspecified choices that must be filled in by learning; outlines hierarchical structure for agent behavior.
- **Choose operator**: Primitive in partial programming language allowing agent to choose any element of a specified set.
- **Joint state space (s,m)**: Each state composed of physical state s and machine state m (program counter, call stack, variables, etc.).
- **Choice state σ = (s,m)**: State where program counter is at a choice point.
- **Keepaway**: Simplified soccer game (3 vs. 2) used as HRL testbed; implemented in RoboCup 2D simulator.
- **Semi-Markov decision process**: Allows actions with different (possibly stochastic) durations.
- **Additive decomposition**: Overall utility decomposes into terms each depending on few variables (enabled by HRL structure).
- **Policy value ρ(θ)**: Expected reward-to-go when policy π_θ is executed.
- **Policy gradient ∇_θ ρ(θ)**: Gradient of policy value with respect to parameters.
- **Stochastic policy π_θ(s,a)**: Probability of selecting action a in state s; e.g., softmax: π_θ(s,a) = e^{β ̂Q_θ(s,a)} / ∑_{a'} e^{β ̂Q_θ(s,a')}.
- **REINFORCE**: Policy gradient algorithm due to Ron Williams (1992); "REward Increment = Nonnegative Factor × Offset Reinforcement × Characteristic Eligibility."
- **Correlated sampling**: Using same random sequences to compare policies; eliminates variance from randomness (used in PEGASUS).
- **PEGASUS**: Policy search algorithm using correlated sampling (Ng and Jordan, 2000); first to achieve stable autonomous helicopter flight.
- **Apprenticeship learning**: Learning to behave well given observations of expert behavior.
- **Imitation learning**: Supervised learning from expert state-action pairs to learn policy π(s).
- **Inverse reinforcement learning (IRL)**: Learning rewards by observing a policy, rather than learning a policy by observing rewards.
- **Boltzmann rationality**: Assumption that agent chooses actions according to softmax distribution over Q-values (rather than deterministic argmax).
- **Feature matching**: IRL algorithm assuming reward function is weighted linear combination of features; matches feature expectations of expert's policy.
- **Feature expectation μ_i(π)**: Expected discounted value of feature f_i when policy π is executed.
- **Deep Q-network (DQN)**: DeepMind's system (Mnih et al., 2015) using deep neural network for Q-function; trained on Atari games from raw pixel input.
- **TD-GAMMON**: Tesauro's (1992) backgammon program using TD learning; fully connected neural network with 80 hidden nodes; reached top-3 human level after 300,000 games.
- **NEUROGAMMON**: Tesauro's (1990) earlier system; imitation learning from 400 games; won 1989 Computer Olympiad.
- **Cart-pole balancing / Inverted pendulum**: Classic control problem; keep pole upright by moving cart left/right.
- **Bang-bang control**: Discrete actions (jerk left or jerk right) for cart-pole.
- **BOXES algorithm**: Early cart-pole learner (Michie and Chambers, 1968); discretized state space into boxes; negative reinforcement propagated back.
- **AlphaGo / AlphaZero**: Deep RL systems for Go; learn both value function and Q-function.
- **Arcade Learning Environment (ALE)**: University of Alberta's framework for 55 Atari games (Bellemare et al., 2013).
- **DeepMind Lab, AI Safety Gridworlds, DM Control Suite**: DeepMind's open-sourced RL platforms.
- **StarCraft II Learning Environment (SC2LE)**: Blizzard/DeepMind RL environment.
- **AI Habitat**: Facebook's photo-realistic virtual indoor environment for robotic tasks (Savva et al., 2019).
- **HORIZON**: Facebook's RL platform for production systems (Gauci et al., 2018).
- **SYNTHIA**: Simulation environment for self-driving car vision (Ros et al., 2016).
- **OpenAI Gym**: RL environment compatible with multiple simulators (Brockman et al., 2016).

### 2. PROCESSES / ALGORITHMS — Step-by-Step Procedures

**Passive ADP Agent (PASSIVE-ADP-LEARNER)** (Figure 22.2):
1. Receive percept (current state s', reward r).
2. If s' is new, set U[s'] ← 0.
3. If previous state s was not null:
   a. Increment N_{s'|s,a}[s,a][s'] (count of outcome s' from (s,a)).
   b. Record R[s,a,s'] ← r.
   c. Add a to A[s].
   d. Normalize counts to get P(·|s,a).
   e. Call POLICY-EVALUATION(π,U,mdp) to solve Bellman equations.
4. Set s←s', a←π[s'].
5. Return a.

**Passive TD Agent (PASSIVE-TD-LEARNER)** (Figure 22.4):
1. Receive percept (current state s', reward r).
2. If s' is new, set U[s'] ← 0.
3. If previous state s was not null:
   a. Increment N_s[s] (state visit count).
   b. Update: U[s] ← U[s] + α(N_s[s]) × (r + γU[s'] - U[s]).
4. Set s ← s'.
5. Return π[s'].

**Q-Learning Agent (Figure 22.8)**:
1. Receive percept (current state s', reward r).
2. If previous state-action not null:
   a. Increment N_{sa}[s,a].
   b. Update: Q[s,a] ← Q[s,a] + α(N_{sa}[s,a])(r + γ max_{a'} Q[s',a'] - Q[s,a]).
3. Choose action: s,a ← s', argmax_{a'} f(Q[s',a'], N_{sa}[s',a']).
4. Return a.

**SARSA Update**:
Q(s,a) ← Q(s,a) + α[R(s,a,s') + γ Q(s',a') - Q(s,a)]
(Applied at end of each s,a,r,s',a' quintuplet)

**Exploratory ADP with Optimistic Utility** (Equation 22.5):
U⁺(s) ← max_a f(∑_{s'} P(s'|s,a)[R(s,a,s') + γ U⁺(s')], N(s,a))
where f(u,n) = R⁺ if n < N_e else u.

**REINFORCE Algorithm (Policy Gradient)**:
1. For each state s visited:
2. ∇_θ ρ(θ) ≈ (1/N) ∑_{j=1}^{N} u_j(s) ∇_θ π_θ(s,a_j) / π_θ(s,a_j)
   where a_j is action taken in state s on trial j, and u_j(s) is total reward from s onward.

**Inverse RL Feature Matching Algorithm**:
1. Pick initial default policy π⁽⁰⁾.
2. For j = 1,2,... until convergence:
   a. Find θ⁽ʲ⁾ such that expert's policy maximally outperforms π⁽⁰⁾,...,π⁽ʲ⁻¹⁾ according to θ⁽ʲ⁾·μ(π).
   b. Let π⁽ʲ⁾ be the optimal policy for reward function R⁽ʲ⁾ = θ⁽ʲ⁾·f.
3. Converges to policy close in value to expert's; requires O(n log n) iterations and O(n log n) expert demonstrations.

**Hierarchical RL (Joint State Space MDP)**:
- States = choice states σ of joint state space (s,m).
- Actions = choices c available at σ according to partial program.
- Reward ρ(σ,c,σ') = expected sum of rewards between choice states.
- Transition τ(σ,c,σ') derived from physical model P(s'|s,a) if c invokes physical action, or deterministic computational transitions.

**Direct Utility Estimation with Function Approximation**:
1. Run trial, observe total reward u_j(s) from each state s onward.
2. For each parameter θ_i: θ_i ← θ_i + α[u_j(s) - Û_θ(s)] ∂Û_θ(s)/∂θ_i

**TD with Function Approximation**:
θ_i ← θ_i + α[R(s,a,s') + γ Û_θ(s') - Û_θ(s)] ∂Û_θ(s)/∂θ_i  (for utilities)
θ_i ← θ_i + α[R(s,a,s') + γ max_{a'} ̂Q_θ(s',a') - ̂Q_θ(s,a)] ∂̂Q_θ(s,a)/∂θ_i  (for Q-values)

### 3. HIERARCHIES / CLASSIFICATIONS

**Categories of RL Approaches**:
- Model-based RL (learns transition model + utility function U(s))
- Model-free RL (no transition model)
  - Action-utility learning (Q-learning, learns Q(s,a))
  - Policy search (learns π(s))

**Passive vs. Active RL**:
- Passive: fixed policy, learn utilities
- Active: must also learn what actions to take; exploration vs. exploitation tradeoff

**Types of Function Approximators for RL**:
- Tabular (one value per state; up to ~10⁶ states)
- Linear function (weighted combination of features)
- Deep neural network (nonlinear; deep RL)

**Exploration Strategies**:
- Greedy (always take currently optimal action; can converge to suboptimal)
- GLIE (random with probability 1/t; greedy otherwise)
- Optimistic exploration (exploration function f(u,n))
- Bayesian RL (posterior over models)
- Robust control (worst-case over model set)

**Hierarchy of RL Safety Approaches**:
- Model-free safe exploration (Q-learning/SARSA)
- Bayesian RL (prior over models)
- Robust control (minimax over models)
- Human intervention (constraints, backup policies, demonstrations)

**HRL vs. Standard RL**:
- Standard RL: choose(A(s)) at each state
- HRL: partial program with choose operators at choice points; hierarchical decomposition of behavior

### 4. COMPARISONS / TRADE-OFFS

**Model-Based vs. Model-Free**:
- Model-based: learns P(s'|s,a) and U(s); can simulate future; more computation; ADP optimal given learned model.
- Model-free: learns Q(s,a) or π(s) directly; less computation per step; no look-ahead; may struggle with sparse rewards.
- "as the environment becomes more complex, the advantages of a model-based approach become more apparent" (Ch22 conclusion).

**ADP vs. TD (Passive)**:
- ADP: adjusts state to agree with ALL successors weighted by probability; solves Bellman equations exactly; slower per observation but faster convergence.
- TD: adjusts state to agree with observed successor only; simpler; less computation; higher variability; slower convergence.
- TD can approach ADP by generating pseudoexperiences from learned model.

**Q-Learning vs. SARSA**:
- Q-learning: off-policy; backs up best action in s' (max_{a'} Q(s',a')); learns: "what would happen if I started acting greedily?"
- SARSA: on-policy; backs up action actually taken in s' (Q(s',a')); learns: "what would happen if I stick with current policy?"
- Identical when greedy; differ during exploration — SARSA penalizes actions that lead to negative rewards during exploration, Q-learning does not.
- Q-learning more flexible (works with varied exploration policies); SARSA appropriate when policy partly controlled by others.

**Greedy vs. Exploratory Agent**:
- Greedy: converges quickly to suboptimal policy (Figure 22.6); ignores information value of actions.
- Exploratory (GLIE/optimistic): converges to near-optimal policy (Figure 22.7); slower initial convergence but better final result.

**Linear Function Approximator vs. Deep Network**:
- Linear: limited expressiveness; requires hand-designed features; provably convergent for TD.
- Deep: discovers features automatically; no human feature engineering; convergence not guaranteed for TD.

**Direct Utility Estimation vs. TD vs. ADP**:
- DUE: ignores Bellman constraints; searches much larger hypothesis space; converges slowly.
- TD: respects local Bellman constraints via observed transitions; moderate speed.
- ADP: globally enforces Bellman constraints; fastest convergence; intractable for large state spaces.

**Imitation Learning vs. Inverse RL**:
- Imitation: supervised learning on state-action pairs; brittle (errors compound); at best duplicates teacher.
- Inverse RL: infers reward function from expert behavior; more robust; can potentially exceed expert performance.

**Supervised vs. Reinforcement Learning**:
- Supervised: passive; labeled examples from teacher; fails when few examples relative to state space.
- RL: active; learns from own experience/rewards; no teacher needed; reward function easier to specify than correct actions.

### 5. FORMULAS & EQUATIONS

**Utility Definition (Expected Discounted Reward)**:
U^π(s) = E[∑_{t=0}^{∞} γ^t R(S_t, π(S_t), S_{t+1})]   (Equation 22.1)

**Bellman Equation for Fixed Policy**:
U^π_i(s) = ∑_{s'} P(s'|s, π_i(s)) [R(s, π_i(s), s') + γ U^π_i(s')]   (Equation 22.2)

**TD Update for Utilities**:
U^π(s) ← U^π(s) + α[R(s,π(s),s') + γ U^π(s') - U^π(s)]   (Equation 22.3)

**Bellman Equation for Optimal Policy**:
U(s) = max_{a∈A(s)} ∑_{s'} P(s'|s,a) [R(s,a,s') + γ U(s')]   (Equation 22.4)

**Bellman Equation for Q-function**:
Q(s,a) = ∑_{s'} P(s'|s,a) [R(s,a,s') + γ max_{a'} Q(s',a')]   (Equation 22.6)

**Q-learning Update**:
Q(s,a) ← Q(s,a) + α[R(s,a,s') + γ max_{a'} Q(s',a') - Q(s,a)]   (Equation 22.7)

**SARSA Update**:
Q(s,a) ← Q(s,a) + α[R(s,a,s') + γ Q(s',a') - Q(s,a)]   (Equation 22.8)

**Optimistic Utility Update (Exploration)**:
U⁺(s) ← max_a f(∑_{s'} P(s'|s,a)[R(s,a,s') + γ U⁺(s')], N(s,a))   (Equation 22.5)
where f(u,n) = R⁺ if n < N_e else u

**Linear Function Approximator**:
Û_θ(s) = θ₁ f₁(s) + θ₂ f₂(s) + ... + θ_n f_n(s)

**Example (4×3 world, x,y features)**:
Û_θ(x,y) = θ₀ + θ₁ x + θ₂ y   (Equation 22.9)

**Widrow-Hoff (Delta) Rule**:
θ_i ← θ_i + α[u_j(s) - Û_θ(s)] ∂Û_θ(s)/∂θ_i   (Equation 22.10)

**For linear case (22.9)**:
θ₀ ← θ₀ + α[u_j(s) - Û_θ(s)]
θ₁ ← θ₁ + α[u_j(s) - Û_θ(s)] x
θ₂ ← θ₂ + α[u_j(s) - Û_θ(s)] y

**TD with Function Approximation (Utilities)**:
θ_i ← θ_i + α[R(s,a,s') + γ Û_θ(s') - Û_θ(s)] ∂Û_θ(s)/∂θ_i   (Equation 22.11)

**TD with Function Approximation (Q-values)**:
θ_i ← θ_i + α[R(s,a,s') + γ max_{a'} ̂Q_θ(s',a') - ̂Q_θ(s,a)] ∂̂Q_θ(s,a)/∂θ_i   (Equation 22.12)

**Reward Shaping (Potential-Based)**:
R'(s,a,s') = R(s,a,s') + γ Φ(s') - Φ(s)   (optimal policy unchanged)

**Stochastic Policy (Softmax)**:
π_θ(s,a) = e^{β ̂Q_θ(s,a)} / ∑_{a'} e^{β ̂Q_θ(s,a')}   (Equation 22.14)

**Policy Gradient (Episodic, Single Step)**:
∇_θ ρ(θ) = ∑_a R(s₀,a,s₀) ∇_θ π_θ(s₀,a)
≈ (1/N) ∑_{j=1}^{N} R(s₀,a_j,s₀) ∇_θ π_θ(s₀,a_j) / π_θ(s₀,a_j)

**Sequential REINFORCE**:
∇_θ ρ(θ) ≈ (1/N) ∑_{j=1}^{N} u_j(s) ∇_θ π_θ(s,a_j) / π_θ(s,a_j)

**Inverse RL (Feature Matching)**:
R_θ(s,a,s') = ∑_{i=1}^{n} θ_i f_i(s,a,s') = θ · f
U^π(s) = ∑_{i=1}^{n} θ_i E[∑_{t=0}^{∞} γ^t f_i(S_t,π(S_t),S_{t+1})] = θ · μ(π)

**Bayesian IRL**:
P(h_R|d) = α P(d|h_R) P(h_R)

**Optimal Robust Policy**:
π* = argmax_π min_h U^π_h

**Bayesian Optimal Policy**:
π* = argmax_π ∑_h P(h|e) U^π_h

### 6. RULES, LAWS & THEOREMS

**Bellman Equation (Fixed Policy)**: U^π(s) = ∑_{s'} P(s'|s,π(s))[R(s,π(s),s') + γ U^π(s')]. Linear for fixed policy (can be solved with linear algebra).

**Bellman Equation (Optimal Policy)**: U(s) = max_a ∑_{s'} P(s'|s,a)[R(s,a,s') + γ U(s')]. Solved by value iteration or policy iteration.

**GLIE Property**: A scheme that tries each action in each state an unbounded number of times will eventually learn the true transition model and converge to an optimal policy.

**Potential-Based Reward Shaping Theorem**: For any potential function Φ(s) and any reward function R, the transformed reward R'(s,a,s') = R(s,a,s') + γΦ(s') - Φ(s) has exactly the same optimal policies as the original R.

**Convergence of TD with Linear Function Approximation**: For passive TD learning with linear function approximator, the update rule converges to the closest possible approximation to the true function.

**Policy Gradient Unbiased Estimate**: The REINFORCE algorithm provides an unbiased estimate of the policy gradient directly from trials.

**Correlated Sampling (PEGASUS)**: Number of random sequences needed to ensure every policy's value is well-estimated depends only on complexity of policy space, not on complexity of underlying domain.

**Feature Matching**: If policy π produces feature expectations μ(π) matching those of expert's policy π_E, then π is as good as expert's policy according to expert's own reward function.

### 7. DATA STRUCTURES & TYPES

**Utility Table U[s]**: Table mapping states to utility values (expected total discounted reward from that state).

**Q-Table Q[s,a]**: Table mapping state-action pairs to Q-values.

**Count Tables**: N_{s'|sa}[s,a][s'] — counts of outcome states from each state-action pair.
N_s[s] — frequency count for states.
N_{sa}[s,a] — frequency count for state-action pairs.

**Transition Model P(s'|s,a)**: Probability distribution over next states; estimated by normalizing counts.

**Reward Function R[s,a,s']**: Recorded rewards for transitions.

**Joint State Space (s,m)**: Composite state with physical part s and machine state m (program counter, call stack, local/global variables).

**Choice State σ**: State where program counter is at a choice point in partial program.

**Feature Vector f(s)**: Vector of features for function approximation.

**Parameter Vector θ**: Parameters for function approximator (linear or neural network).

**Policy π(s) or π_θ(s,a)**: Deterministic (state→action) or stochastic (state→probability over actions).

### 8. VISUAL PATTERNS

**Figure 22.1 (p.791)**: 
(a) Optimal policies for 4×3 world with R(s,a,s')=-0.04 for nonterminal transitions; two policies exist (state (3,1) both Left and Up optimal).
(b) Utilities of states in 4×3 world given policy π.

**Figure 22.3 (p.794)**: Passive ADP learning curves for 4×3 world:
(a) Utility estimates for selected states vs. number of trials (100 trials). Rare states (2,1) and (3,2) discover connection to +1 exit after 14 and 23 trials.
(b) RMS error in U(1,1) estimate averaged over 50 runs of 100 trials.

**Figure 22.5 (p.796)**: TD learning curves for 4×3 world:
(a) Utility estimates vs. number of trials (500 trials). Higher variability than ADP.
(b) RMS error in U(1,1) averaged over 50 runs of 100 trials.

**Figure 22.6 (p.798)**: Greedy ADP agent performance:
(a) RMS error and policy loss in (1,1). Policy converges after 8 trials to suboptimal policy (loss=0.235).
(b) The suboptimal policy: Down action in (1,2).

**Figure 22.7 (p.800)**: Exploratory ADP agent (R⁺=2, N_e=5):
(a) Utility estimates for selected states over 100 trials.
(b) RMS error and policy loss; near-optimal policy after 18 trials.

**Figure 22.9 (p.817)**:
(a) Cart-pole balancing setup: cart on track, pole hinged on top, state variables x, θ, ẋ, θ̇.
(b) Six superimposed time-lapse images of autonomous helicopter performing "nose-in circle" maneuver (PEGASUS policy).

### 9. EDGE CASES / EXCEPTIONS / TRAPS

**Sparse Rewards Problem**: Only occasional informative reward signals; agent must take many actions before any reward. Credit assignment problem: "how did I do wrong?"

**Greedy Agent Failure**: Choosing optimal action for learned model can lead to suboptimal performance in true environment (Figure 22.6). Agent ignores information value of actions.

**Catastrophic Forgetting**: Function approximator (e.g., neural network) can lose previously learned information about parts of state space no longer visited. Example: autonomous vehicle learns central road is safe, forgets edges are dangerous, then swerves off road.

**Divergence of Nonlinear Function Approximators**: With active learning and nonlinear functions (neural networks), parameters "can go off to infinity" even when good solutions exist. "Reinforcement learning with general function approximators remains a delicate art."

**Safe Exploration Problem**: Real world doesn't have reset button. Irreversible actions, absorbing states, large negative rewards. Maximum-likelihood model assumption can be dangerous (e.g., taxi ignoring red lights).

**Bayesian RL Not Foolproof**: Perfect Bayesian reasoning doesn't protect from untimely death if prior doesn't indicate danger percepts.

**Robust Control Over-Conservatism**: Worst-case assumption leads to overly conservative behavior. "A self-driving car that assumes every other driver will try to collide with it has no choice but to stay in the garage."

**Reward Shaping Risks**: Agent may learn to maximize pseudorewards rather than true rewards (e.g., vibrating next to ball to maximize contact count).

**Imitation Learning Brittleness**: Small deviations from training set lead to compounding errors and eventual failure.

**Inverse RL Non-Uniqueness**: R(s,a,s')=0 is a trivial solution for any observed behavior (any policy is rational with zero reward). Need Bayesian approach to prefer simpler explanations that make observed behavior more probable.

**Non-Markovian Abstract States (HRL)**: Naïve state abstraction in hierarchical RL leads to non-Markovian transition models and divergent behavior.

**SARSA vs Q-learning Trap**: When exploration happens, SARSA penalizes actions that lead to negative reward during exploration; Q-learning does not.

### 10. EMPIRICAL EVIDENCE / KEY RESULTS

**4×3 World Experiments**:
- ADP: converges fastest; ~14-23 trials for rare states to discover +1 exit (Figure 22.3).
- TD: higher variability, slower but simpler; ~500 trials for comparable utility estimates (Figure 22.5).
- Greedy ADP: converges to suboptimal policy after only 8 trials (policy loss 0.235) (Figure 22.6).
- Exploratory ADP (R⁺=2, N_e=5): near-optimal policy after 18 trials (Figure 22.7).

**Backgammon (TD-Gammon)**:
- Fully connected neural network, 80 hidden nodes, hand-crafted features.
- After 300,000 training games: comparable to top three human players.
- Kit Woolsey (top-ten player): "its positional judgment is far better than mine."
- State space ~10²⁰; explored only a trillionth of state space.

**Atari Games (DQN)**:
- 49 games; roughly human expert level.
- Montezuma's Revenge: failed due to sparse rewards and extended planning.
- Later systems solved it with more extensive exploration behaviors.

**AlphaGo**:
- Learned both value function and Q-function.
- Q-function alone (no search) beats most amateur human players.
- Combined with look-ahead: best human players defeated.

**Cart-Pole Balancing (BOXES algorithm)**:
- Balanced pole for over an hour after 30 trials.
- Modern systems: triple inverted pendulum — beyond most human capabilities.

**Autonomous Helicopter (PEGASUS)**:
- First to achieve completely stable autonomous flight.
- Overnight training on simulator; far exceeded expert human pilot.

**Keepaway (HRL)**:
- HRL agent with partial program: keeps possession forever vs. standard taker policy.
- Previous record: ~10 seconds.

**Inverse RL Applications**:
- Taxi driver route prediction: 100,000 miles of GPS data (Ziebart et al., 2008).
- Pedestrian movement prediction: hours of video (Kitani et al., 2012).
- LittleDog quadruped: single expert demonstration → 25-feature reward function → traverse rocky terrain (Kolter et al., 2008).

### 11. CROSS-CHAPTER DEPENDENCIES

**Chapter 17 (MDPs)**: Foundational for this chapter — MDPs, Bellman equations, value iteration, policy iteration, utility functions, Q-functions, policy evaluation, bandit problems (exploration/exploitation). "An understanding of Markov decision processes, as described in Chapter 17, is essential for this section."

**Chapter 14 (Probabilistic Reasoning)**: HMMs, DBNs, Kalman filters; state estimation in partially observable environments.

**Chapters 19-20 (Machine Learning)**: Supervised learning methods, gradient descent, linear regression, function approximation; EM algorithm for learning Bayes net parameters.

**Chapter 21 (Deep Learning)**: Deep neural networks as function approximators for RL; DQN, AlphaGo, RNNs for hidden structure discovery. The entire field of deep RL depends on Chapter 21 methods.

**Chapter 5 (Adversarial Search)**: Monte Carlo tree search; AlphaGo.

**Chapter 2 (Intelligent Agents)**: Reflex agent definition (policy as reflex agent).

**Chapter 4 (Search)**: Irreversible actions (Section 4.5); optimization methods.

**Chapter 11 (Planning)**: HTN planning (hierarchical decomposition similar to HRL).

**Chapter 18 (Multiagent Systems)**: Game theory (references for two-person assistance games and multiagent settings).

**Chapter 20 (Learning Probabilistic Models)**: Maximum likelihood estimation; Bayesian learning; EM algorithm.

**Chapters 25-26 (Vision/Robotics)**: Applications of RL in computer vision and robot control.

### 12. DATES & PEOPLE

- **Pavlov (Nobel Prize 1904)**: Early foundations of RL.
- **Thorndike (1911)**: "Animal Intelligence."
- **Turing (1948, 1950)**: Proposed RL as approach for teaching computers; considered it partial solution.
- **Samuel (1952, 1959, 1967)**: First successful machine learning (checkers); suggested most modern RL ideas including TD learning, function approximation, multilayer value functions.
- **Widrow and Hoff (1960)**: Adaptive control theory; delta rule; building on Hebb (1949).
- **Michie and Chambers (1968)**: BOXES algorithm for cart-pole balancing.
- **Werbos (1977)**: First connection between RL and MDPs.
- **Witten (1977)**: TD-like process in control theory.
- **Barto et al. (1981)**: Development of RL at University of Massachusetts.
- **Sutton (1988)**: Mathematical understanding of TD methods.
- **Watkins (1989)**: Q-learning in Ph.D. thesis.
- **Tesauro (1990)**: NEUROGAMMON; won 1989 Computer Olympiad.
- **Tesauro (1992, 1995)**: TD-GAMMON; top-3 human level backgammon.
- **Rummery and Niranjan (1994)**: SARSA.
- **Moore and Atkeson (1993), Peng and Williams (1993)**: Prioritized sweeping.
- **Sutton (1990)**: DYNA architecture (TD + model-based simulation).
- **Williams (1992)**: REINFORCE family of algorithms.
- **Ng and Jordan (2000)**: PEGASUS policy search.
- **Ng et al. (2003), Coates et al. (2009)**: Apprenticeship learning for helicopter flight.
- **Russell (1998)**: Introduced inverse reinforcement learning.
- **Ng and Russell (2000)**: First IRL algorithms.
- **Abbeel and Ng (2004)**: Feature matching IRL algorithm given in chapter.
- **Sammut et al. (1992)**: "Learning to Fly" — imitation learning in flight simulator.
- **Camacho and Michie (1995)**: Fragility of behavioral cloning.
- **Mnih et al. (2013, 2015)**: DQN; deep RL for Atari.
- **Silver et al. (2018)**: AlphaZero.
- **Irpan (2018)**: Deep RL can perform poorly if environment changes slightly.
- **Stone et al. (2005)**: Keepaway game.
- **Bai and Russell (2017)**: HRL solution for keepaway.
- **Parr and Russell (1998), Andre and Russell (2002)**: Temporal abstraction in HRL.
- **Dietterich (2000)**: Additive decomposition of Q-functions.
- **Marthi et al. (2005)**: Concurrent behaviors in HRL.
- **Dayan and Hinton (1993)**: State abstraction in HRL.
- **Forestier and Varaiya (1978)**: Two-layer MDP decomposition.
- **Sargent (1978)**: Structural estimation of MDPs in economics.
- **Baker et al. (2009)**: Inverse planning for understanding others' actions.
- **Ho et al. (2017)**: Learning from instructive rather than optimal behaviors.
- **Hadfield-Menell et al. (2017a)**: Game-theoretic IRL.
- **Bellemare et al. (2013)**: Arcade Learning Environment (ALE).
- **Schultz et al. (1997)**: Dopamine system in primate brains implements value-function learning.
- **Dayan and Abbott (2001), Dayan and Niv (2008), Niv (2009), Lee et al. (2012)**: Neuroscience of RL.
- **Sutton and Barto (2018)**: Canonical RL text.
- **Littman (2015)**: RL survey for general audience.
- **Kochenderfer (2015)**: RL with real-world examples.
- **Szepesvari (2010)**: Short overview of RL algorithms.
- **Bertsekas and Tsitsiklis (1996)**: Dynamic programming and stochastic convergence.

### 13. PROOF & ARGUMENT PATTERNS

**Direct Utility Estimation vs. Bellman-constrained Methods**:
- DUE searches hypothesis space that includes many functions violating Bellman equations → converges slowly.
- ADP/TD enforce Bellman constraints → faster convergence.

**TD Convergence Argument**:
1. TD updates use only observed successor (not all possible successors).
2. Rare transitions occur rarely, so average of U^π(s) converges to correct value in limit.
3. With decreasing α(n) satisfying technical conditions (as on page 684), U^π(s) itself converges.

**ADP vs. TD Relationship**:
- ADP adjusts state to agree with ALL successors weighted by probability (Equation 22.2).
- TD adjusts state to agree with observed successor (Equation 22.3).
- When averaged over many transitions, frequency of each successor ≈ its probability → TD approximates ADP.
- TD = crude but efficient first approximation to ADP.
- Can extend TD with pseudoexperiences from learned model to approach ADP accuracy.

**Greedy Agent Failure**: The greedy agent chooses optimal action for learned model → but learned model ≠ true environment → can converge to suboptimal policy. Reason: actions provide both rewards AND information.

**Policy Gradient Derivation (REINFORCE)**:
1. ρ(θ) = ∑_a R(s₀,a,s₀) π_θ(s₀,a)
2. ∇_θ ρ(θ) = ∑_a R(s₀,a,s₀) ∇_θ π_θ(s₀,a)
3. Multiply and divide by π_θ(s₀,a): ∇_θ ρ(θ) = ∑_a π_θ(s₀,a) · [R(s₀,a,s₀) ∇_θ π_θ(s₀,a) / π_θ(s₀,a)]
4. Approximate by sampling: (1/N) ∑_{j=1}^N R(s₀,a_j,s₀) ∇_θ π_θ(s₀,a_j) / π_θ(s₀,a_j)
5. For sequential case: same form with u_j(s) replacing R(s₀,a_j,s₀).

**Q-learning vs. SARSA Distinction**:
- Q-learning: Q(s,a) ← Q(s,a) + α[r + γ max_{a'} Q(s',a') - Q(s,a)]. Off-policy — imagines switching to greedy policy.
- SARSA: Q(s,a) ← Q(s,a) + α[r + γ Q(s',a') - Q(s,a)]. On-policy — evaluates current policy.
- If exploration yields negative reward: SARSA penalizes action; Q-learning does not.

**Correlated Sampling Argument**: For blackjack, generate hands in advance → both policies play same hands → eliminates variance from card distribution → thousands of hands sufficient (vs. millions for independent sampling).

**Inverse RL Non-Uniqueness**: R(s,a,s')=0 explains any observed behavior (any policy optimal with zero reward). Solved via Bayesian reasoning: P(h_R|d) = α P(d|h_R) P(h_R). Simple R=0 gets high prior but zero P(d|h_R) because it doesn't explain why expert chose specific behavior out of vast space of optimal behaviors (under R=0, all behaviors are optimal).

### 14. DESIGN PARADIGMS / META-METHODS

**Model-Based vs. Model-Free Tradeoff**: Central design decision in RL. Model-based: knowledge-based approach (build representation of environment). Model-free: direct policy learning from data. "As the environment becomes more complex, the advantages of a model-based approach become more apparent."

**Exploration as Information Gathering**: Actions have dual purpose: obtain rewards AND obtain information. Formulate as exploration POMDP (belief state over models).

**Temporal Difference Learning**: Learn from the difference between successive predictions; core idea: adjust current estimate toward next time step's estimate plus observed reward.

**Optimistic Initialization**: Start with optimistic estimates (R⁺) to encourage exploration; exploration bonus propagates back from frontier.

**Function Approximation as Inductive Generalization**: Learn from visited states to predict values for unvisited states; compact representation of potentially vast state space.

**Hierarchical Decomposition**: Break complex behaviors into hierarchy of sub-behaviors; partial programs provide structure; learning fills in details.

**Additive Decomposition of Utility**: Hierarchical structure enables utility decomposition into terms depending on few variables → faster learning (analogous to Bayes net conciseness).

**Potential-Based Reward Shaping**: Guide learning without changing optimal policy by modifying rewards with potential function Φ(s).

**Behavioral Cloning vs. Inverse Reinforcement Learning**: Cloning learns policy directly (brittle); IRL learns reward function (robust, transferable, can exceed expert).

**Experience Replay**: Retain and replay past trajectories to prevent catastrophic forgetting.

**Correlated Sampling for Policy Comparison**: Use same random sequences to compare policies; reduces variance dramatically.

### 15. CASE STUDIES / CLASSIC EXAMPLES

**4×3 World (Throughout Chapter)**: Grid world with +1 at (4,3), -1 at (4,2), -0.04 per step, stochastic transitions. Used to compare ADP, TD, greedy vs. exploratory agents.

**Sample Trials (p.792)**:
```
(1,1)-.04→Up(1,2)-.04→Up(1,3)-.04→Right(1,2)-.04→Up(1,3)-.04→Right(2,3)-.04→Right(3,3)+1→Right(4,3)
(1,1)-.04→Up(1,2)-.04→Up(1,3)-.04→Right(2,3)-.04→Right(3,3)-.04→Right(3,2)-.04→Up(3,3)+1→Right(4,3)
(1,1)-.04→Up(1,2)-.04→Up(1,3)-.04→Right(2,3)-.04→Right(3,3)-.04→Right(3,2)-1→Up(4,2)
```

**Greedy Agent Failure (p.797-798)**: Finds lower route via (2,1),(3,1),(3,2),(3,3) after 8 trials; sticks with it; never finds optimal upper route via (1,2),(1,3),(2,3).

**Cart-Pole Balancing (p.816-817)**: State variables x, θ, ẋ, θ̇ (continuous). Discrete bang-bang control. BOXES algorithm (Michie and Chambers, 1968): discretize state space into boxes; run trials until pole falls; propagate negative reinforcement back.

**Backgammon (TD-Gammon) (p.816)**: ~10²⁰ states. Neural network: 1 hidden layer, 80 nodes, hand-crafted features. 300,000 training games → top-3 human level. Explored only one trillionth of state space.

**Keepaway (HRL) (p.808-809)**: 3 vs. 2 players in RoboCup 2D simulator. Partial program: if ball possession → choose {PASS,HOLD,DRIBBLE}; else → choose {STAY,MOVE,INTERCEPT-BALL}. PASS chooses teammate → chooses speed/direction. Learned to keep possession forever.

**Helicopter Flight (PEGASUS) (p.817)**: Model learned from observing real helicopter. Policy search on simulator overnight. "Nose-in circle" maneuver far exceeding expert human pilot.

**Blackjack Policy Comparison (p.812)**: Two policies with true returns -0.21% and +0.06%. Independent sampling: millions of hands needed. Correlated sampling (same hands to both): thousands sufficient.

**Atari DQN (p.816)**: 49 games; raw pixel input; deep network for Q-function; game score as reward. Expert level on most; Montezuma's Revenge failed (sparse rewards, need planning).

**Self-Driving Car Safety (p.800-802)**: Unknown model → exploration may cause crashes. Example: taxi ignoring red lights after 1-2 safe crossings. Three approaches: Bayesian RL, robust control, human constraints.

### 16. ETHICS CONSIDERATIONS

**Safe Exploration (Section 22.3.2)**: Real world lacks reset button. Irreversible actions can lead to absorbing states (death, catastrophic damage). Agent must be cautious about exploration when stakes are high.

**Positive Reward Functions Not Enough**: R(s,a,s')=0 explains any behavior. Omitting important factors in reward function leads to extreme behavior (e.g., inconsiderate driving). Need careful reward design.

**Imitation Learning Bottleneck**: At best duplicates teacher; cannot exceed human performance unless combined with RL.

**Self-Driving Cars**: Constantly balance risk-reward tradeoffs. Worst-case robust control too conservative; learned policies can have unpredictable failures.

**Expert vs. Learner Interaction**: Inverse RL assumes expert acts as if unobserved. But in teaching scenarios (surgery, driving), expert modifies behavior to help learner — inverse RL would misinterpret.

**Model-Free vs. Model-Based**: Philosophical debate about knowledge representation. "It is not easy to imagine how a model-free approach would enable one to design and build, say, the LIGO gravity-wave detector."

**Autonomous Weapons Potential**: Not explicitly discussed, but the general-purpose nature of RL (can learn any task from reward signals) implies dual-use concerns.

**Reward Hacking**: Agent may learn to maximize pseudorewards rather than true rewards (vibrating next to ball to maximize contacts). Careful shaping design needed.

**Deep RL Reliability**: "Difficult to get good performance" and "may behave very unpredictably if environment differs even a little from training data" (Irpan, 2018). Rarely applied in commercial settings.

### 17. END-OF-CHAPTER MATERIAL

**Summary** (lines 35836-35889):
- The overall agent design dictates the kind of information that must be learned:
  - A model-based reinforcement learning agent acquires (or is equipped with) a transition model P(s'|s,a) for the environment and learns a utility function U(s).
  - A model-free reinforcement learning agent may learn an action-utility function Q(s,a) or a policy π(s).
- Utilities can be learned using several different approaches:
  - Direct utility estimation uses the total observed reward-to-go for a given state as direct evidence for learning its utility.
  - Adaptive dynamic programming (ADP) learns a model and a reward function from observations and then uses value or policy iteration to obtain the utilities or an optimal policy. ADP makes optimal use of the local constraints on utilities of states imposed through the neighborhood structure of the environment.
  - Temporal-difference (TD) methods adjust utility estimates to be more consistent with those of successor states. They can be viewed as simple approximations of the ADP approach that can learn without requiring a transition model. Using a learned model to generate pseudoexperiences can, however, result in faster learning.
- Action-utility functions, or Q-functions, can be learned by an ADP approach or a TD approach. With TD, Q-learning requires no model in either the learning or action-selection phase. This simplifies the learning problem but potentially restricts the ability to learn in complex environments, because the agent cannot simulate the results of possible courses of action.
- When the learning agent is responsible for selecting actions while it learns, it must trade off the estimated value of those actions against the potential for learning useful new information. An exact solution for the exploration problem is infeasible, but some simple heuristics do a reasonable job. An exploring agent must also take care to avoid premature death.
- In large state spaces, reinforcement learning algorithms must use an approximate functional representation of U(s) or Q(s,a) in order to generalize over states. Deep reinforcement learning — using deep neural networks as function approximators — has achieved considerable success on hard problems.
- Reward shaping and hierarchical reinforcement learning are helpful for learning complex behaviors, particularly when rewards are sparse and long action sequences are required to obtain them.
- Policy-search methods operate directly on a representation of the policy, attempting to improve it based on observed performance. The variation in the performance in a stochastic domain is a serious problem; for simulated domains this can be overcome by fixing the randomness in advance.
- Apprenticeship learning through observation of expert behavior can be an effective solution when a correct reward function is hard to specify. Imitation learning formulates the problem as supervised learning of a policy from the expert's state-action pairs. Inverse reinforcement learning infers reward information from the expert's behavior.

Reinforcement learning continues to be one of the most active areas of machine learning research. It frees us from manual construction of behaviors and from labeling the vast data sets required for supervised learning, or having to hand-code control strategies. Applications in robotics promise to be particularly valuable; these will require methods for handling continuous, high-dimensional, partially observable environments in which successful behaviors may consist of thousands or even millions of primitive actions.

We have presented a variety of approaches to reinforcement learning because there is (at least so far) no single best approach. The question of model-based versus model-free methods is, at its heart, a question about the best way to represent the agent function. This is an issue at the foundations of artificial intelligence. As we stated in Chapter 1, one of the key historical characteristics of much AI research is its (often unstated) adherence to the knowledge-based approach. This amounts to an assumption that the best way to represent the agent function is to build a representation of some aspects of the environment in which the agent is situated. Some argue that with access to sufficient data, model-free methods can succeed in any domain. Perhaps this is true in theory, but of course, the universe may not contain enough data to make it true in practice. (For example, it is not easy to imagine how a model-free approach would enable one to design and build, say, the LIGO gravity-wave detector.) Our intuition, for what it's worth, is that as the environment becomes more complex, the advantages of a model-based approach become more apparent.

**Bibliographical and Historical Notes** (lines 35903-36062):
[Full content reproduced below]
It seems likely that the key idea of reinforcement learning—that animals do more of what they are rewarded for and less of what they are punished for—played a significant role in the domestication of dogs at least 15,000 years ago. The early foundations of our scientific understanding of reinforcement learning include the work of the Russian physiologist Ivan Pavlov, who won the Nobel Prize in 1904, and that of the American psychologist Edward Thorndike — particularly his book Animal Intelligence (1911). Hilgard and Bower (1975) provide a good survey.

Alan Turing (1948, 1950) proposed reinforcement learning as an approach for teaching computers; he considered it a partial solution, writing, "The use of punishments and rewards can at best be a part of the teaching process." Arthur Samuel's checkers program (1959, 1967) was the first successful use of machine learning of any kind. Samuel suggested most of the modern ideas in reinforcement learning, including temporal-difference learning and function approximation. He experimented with multilayer representations of value functions, similar to today's deep RL. In the end, he found that a simple linear evaluation function over handcrafted features worked best. This may have been a consequence of working with a computer roughly 100 billion times less powerful than a modern tensor processing unit.

Around the same time, researchers in adaptive control theory (Widrow and Hoff, 1960), building on work by Hebb (1949), were training simple networks using the delta rule. Thus, reinforcement learning combines influences from animal psychology, neuroscience, operations research, and optimal control theory.

The connection between reinforcement learning and Markov decision processes was first made by Werbos (1977). (Work by Ian Witten (1977) described a TD-like process in the language of control theory.) The development of reinforcement learning in AI stems primarily from work at the University of Massachusetts in the early 1980s (Barto et al., 1981). An influential paper by Rich Sutton (1988) provided a mathematical understanding of temporal-difference methods. The combination of temporal-difference learning with the model-based generation of simulated experiences was proposed in Sutton's DYNA architecture (Sutton, 1990). Q-learning was developed in Chris Watkins's Ph.D. thesis (1989), while SARSA appeared in a technical report by Rummery and Niranjan (1994). Prioritized sweeping was introduced independently by Moore and Atkeson (1993) and Peng and Williams (1993).

Function approximation in reinforcement learning goes back to Arthur Samuel's checkers program (1959). The use of neural networks to represent value functions was common in the 1980s and came to the fore in Gerry Tesauro's TD-Gammon program (Tesauro, 1992, 1995). Deep neural networks are currently the most popular choice for function approximators in reinforcement learning. Arulkumaran et al. (2017) and Francois-Lavet et al. (2018) give overviews of deep RL. The DQN system (Mnih et al., 2015) uses a deep network to learn a Q-function, while AlphaZero (Silver et al., 2018) learns both a value function for use with a known model and a Q-function for use in metalevel decisions that guide search. Irpan (2018) warns that deep RL systems can perform poorly if the actual environment is even slightly different from the training environment.

Weighted linear combinations of features and neural networks are factored representations for function approximation. It is also possible to apply reinforcement learning to structured representations; this is called relational reinforcement learning (Tadepalli et al., 2004). The use of relational descriptions allows for generalization across complex behaviors involving different objects.

Analysis of the convergence properties of reinforcement learning algorithms using function approximation is an extremely technical subject. Results for TD learning have been progressively strengthened for the case of linear function approximators (Sutton, 1988; Dayan, 1992; Tsitsiklis and Van Roy, 1997), but several examples of divergence have been presented for nonlinear functions (see Tsitsiklis and Van Roy, 1997, for a discussion). Papavassiliou and Russell (1999) describe a type of reinforcement learning that converges with any form of function approximator, provided that the problem of fitting the hypothesis to the data is solvable. Liu et al. (2018) describe the family of gradient TD algorithms and provide extensive theoretical analysis of convergence and sample complexity.

A variety of exploration methods for sequential decision problems are discussed by Barto et al. (1995). Kearns and Singh (1998) and Brafman and Tennenholtz (2000) describe algorithms that explore unknown environments and are guaranteed to converge on near-optimal policies with a sample complexity that is polynomial in the number of states. Bayesian reinforcement learning (Dearden et al., 1998, 1999) provides another angle on both model uncertainty and exploration.

The basic idea underlying imitation learning is to apply supervised learning to a training set of expert actions. This is an old idea in adaptive control, but first came to prominence in AI with the work of Sammut et al. (1992) on "Learning to Fly" in a flight simulator. They called their method behavioral cloning. A few years later, the same research group reported that the method was much more fragile than had been reported initially (Camacho and Michie, 1995): even very small perturbations caused the learned policy to deviate from the desired trajectory, leading to compounding errors as the agent strayed further and further from the training set. (See also the discussion on page 966.) Work on apprenticeship learning aims to make the approach more robust, in part by including information about the desired outcomes rather than just the expert policy. Ng et al. (2003) and Coates et al. (2009) show how apprenticeship learning works for learning to fly an actual helicopter, as illustrated in Figure 22.9(b) on page 817.

Inverse reinforcement learning (IRL) was introduced by Russell (1998), and the first algorithms were developed by Ng and Russell (2000). (A similar problem has been studied in economics for much longer, under the heading of structural estimation of MDPs (Sargent, 1978).) The algorithm given in the chapter is due to Abbeel and Ng (2004). Baker et al. (2009) describe how the understanding of another agent's actions can be seen as inverse planning. Ho et al. (2017) show that agents can learn better from behaviors that are instructive rather than optimal. Hadfield-Menell et al. (2017a) extend IRL into a game-theoretic formulation that encompasses both observer and demonstrator, showing how teaching and learning behaviors emerge as solutions of the game.

García and Fernández (2015) give a comprehensive survey on safe reinforcement learning. Munos et al. (2017) describe an algorithm for safe off-policy (e.g., Q-learning) exploration. Hans et al. (2008) break the problem of safe exploration into two parts: defining a safety function to indicate which states to avoid, and defining a backup policy to lead the agent back to safety when it might otherwise enter an unsafe state. You et al. (2017) show how to train a deep reinforcement learning model to drive a car in simulation, and then use transfer learning to drive safely in the real world.

Thomas et al. (2017) offer an approach to learning that is guaranteed, with high probability, to do no worse than the current policy. Akametalu et al. (2014) describe a reachability-based approach, in which the learning process operates under the guidance of a control policy that ensures the agent never reaches an unsafe state. Saunders et al. (2018) demonstrate that a system can use human intervention to stop it from wandering out of the safe region, and can learn over time to need less intervention.

Policy search methods were brought to the fore by Williams (1992), who developed the REINFORCE family of algorithms, which stands for "REward Increment = Nonnegative Factor × Offset Reinforcement × Characteristic Eligibility." Later work by Marbach and Tsitsiklis (1998), Sutton et al. (2000), and Baxter and Bartlett (2000) strengthened and generalized the convergence results for policy search. Schulman et al. (2015b) describe trust region policy optimization, a theoretically well-founded and also practical policy search algorithm that has spawned many variants. The method of correlated sampling to reduce variance in Monte Carlo comparisons is due to Kahn and Marshall (1953); it is also one of a number of variance reduction methods explored by Hammersley and Handscomb (1964).

Early approaches to hierarchical reinforcement learning (HRL) attempted to construct hierarchies using state abstraction — that is, grouping states together into abstract states and then doing RL in the abstract state space (Dayan and Hinton, 1993). Unfortunately, the transition model for abstract states is typically non-Markovian, leading to divergent behavior of standard RL algorithms. The temporal abstraction approach in this chapter was developed in the late 1990s (Parr and Russell, 1998; Andre and Russell, 2002; Sutton et al., 2000) and extended to handle concurrent behaviors by Marthi et al. (2005). Dietterich (2000) introduced the notion of an additive decomposition of Q-functions induced by the subroutine hierarchy. Temporal abstraction is based on a much earlier result due to Forestier and Varaiya (1978), who showed that a large MDP can be decomposed into a two-layer system in which a supervisory layer chooses among low-level controllers, each of which returns control to the supervisor on completion. The problem of learning the abstraction hierarchy itself has been studied at least since the work of Peter Andreae (1985); for a recent exploration into learning robot motion primitives, see Frans et al. (2018). The keepaway game was introduced by Stone et al. (2005); the HRL solution given here is due to Bai and Russell (2017).

Neuroscience has often inspired reinforcement learning and confirmed the value of the approach. Research using single-cell recording suggests that the dopamine system in primate brains implements something resembling value-function learning (Schultz et al., 1997). The neuroscience text by Dayan and Abbott (2001) describes possible neural implementations of temporal-difference learning; related research describes other neuroscientific and behavioral experiments (Dayan and Niv, 2008; Niv, 2009; Lee et al., 2012).

Work in reinforcement learning has been accelerated by the availability of open-source simulation environments for developing and testing learning agents. The University of Alberta's Arcade Learning Environment (ALE) (Bellemare et al., 2013) provided such a framework for 55 classic Atari video games. The pixels on the screen are provided to the agent as percepts, along with a hardwired score of the game so far. ALE was used by the DeepMind team to implement DQN learning and verify the generality of their system on a wide variety of games (Mnih et al., 2015).

DeepMind in turn open-sourced several agent platforms, including the DeepMind Lab (Beattie et al., 2016), the AI Safety Gridworlds (Leike et al., 2017), the Unity game platform (Juliani et al., 2018), and the DM Control Suite (Tassa et al., 2018). Blizzard released the StarCraft II Learning Environment (SC2LE), to which DeepMind added the PySC2 component for machine learning in Python (Vinyals et al., 2017a).

Facebook's AI Habitat simulation (Savva et al., 2019) provides a photo-realistic virtual environment for indoor robotic tasks, and their HORIZON platform (Gauci et al., 2018) enables reinforcement learning in large-scale production systems. The SYNTHIA system (Ros et al., 2016) is a simulation environment designed for improving the computer vision capabilities of self-driving cars. The OpenAI Gym (Brockman et al., 2016) provides several environments for reinforcement learning agents, and is compatible with other simulations such as the Google Football simulator.

Littman (2015) surveys reinforcement learning for a general scientific audience. The canonical text by Sutton and Barto (2018), two of the field's pioneers, shows how reinforcement learning weaves together the ideas of learning, planning, and acting. Kochenderfer (2015) takes a slightly less mathematical approach, with plenty of real-world examples. A short book by Szepesvari (2010) gives an overview of reinforcement learning algorithms. Bertsekas and Tsitsiklis (1996) provide a rigorous grounding in the theory of dynamic programming and stochastic convergence. Reinforcement learning papers are published frequently in the journals Machine Learning and Journal of Machine Learning Research, and in the proceedings of the International Conference on Machine Learning (ICML) and the Neural Information Processing Systems (NeurIPS) conferences.

**End of Chapter 22**


---

# CHAPTER 23 — NATURAL LANGUAGE PROCESSING

---

## 1. Named Entities & Definitions

| Term | Definition |
|------|-----------|
| **Natural Language Processing (NLP)** | Using computers to communicate with humans via natural language and learn from what they have written |
| **Language Model** | A probability distribution describing the likelihood of any string (p. 838) |
| **Bag-of-words model** | A generative model that treats words as independent draws from a bag; used with naive Bayes for classification (p. 838) |
| **Corpus** | A body of text used for training, ≥1M words; e.g., Wikipedia (2.5B words), iWeb (14B words) (p. 839) |
| **Tokenization** | Dividing text into a sequence of words |
| **N-gram model** | Markov chain model where each word depends on n−1 previous words; unigram (1-gram), bigram (2-gram), trigram (3-gram) (p. 840) |
| **Spam detection** | Distinguishing spam from non-spam email |
| **Sentiment analysis** | Classifying reviews as positive or negative |
| **Author attribution** | Identifying author by writing style |
| **Character-level model** | Probability of each character depends on n−1 previous characters |
| **Language identification** | Determining what language a text is written in (>99% accuracy; 95% for close languages like Swedish/Norwegian) |
| **Skip-gram model** | Counts words that are near each other skipping intervening words |
| **Out-of-vocabulary (OOV)** | Words that never appeared in training corpus |
| **Smoothing** | Reserving probability mass for unseen n-grams to reduce variance |
| **Laplace (add-one) smoothing** | Simplest smoothing: adds 1 to all counts; performs poorly for NLP |
| **Backoff model** | For low/zero count sequences, back off to (n−1)-grams |
| **Linear interpolation smoothing** | Combines trigram, bigram, unigram models by linear interpolation with λ weights summing to 1 |
| **WordNet** | Open-source hand-curated dictionary, ~100K words, organized by synsets and semantic relations |
| **Part of speech (POS)** | Lexical category: noun, verb, adjective, etc. |
| **Penn Treebank** | >3M words annotated with 45 POS tags and parse trees |
| **Part-of-speech tagging** | Assigning a POS to each word in a sentence (~97% accuracy with HMM) |
| **Viterbi algorithm** | Finds most probable sequence of hidden states (tags) (Sec 14.2.3) |
| **Generative model** | Learns joint distribution P(W,C); can generate random sentences (naive Bayes, HMM) |
| **Discriminative model** | Learns conditional distribution P(C|W); lower error rate, but cannot generate (logistic regression) |
| **Beam search** | Keeps only b most likely tags at each step |
| **Probabilistic Context-Free Grammar (PCFG)** | Assigns probability to each string; context-free means rules apply in any context |
| **E₀** | Tiny English fragment grammar for wumpus world communication |
| **Grammar** | Set of rules defining tree structure of allowable phrases |
| **Syntactic category** | e.g., noun phrase, verb phrase |
| **Phrase structure** | Framework for meaning/semantics of sentence |
| **Overgeneration** | Grammar generates ungrammatical sentences |
| **Undergeneration** | Grammar rejects grammatical sentences |
| **Lexicon** | List of allowable words |
| **Open class** | Nouns, verbs, adjectives, adverbs — can add new words |
| **Closed class** | Pronouns, articles, prepositions, conjunctions — small fixed set |
| **Parsing** | Analyzing string of words to uncover phrase structure per grammar rules |
| **Chart parser** | Dynamic programming parser that stores substring results to avoid reanalysis |
| **CYK algorithm** | Bottom-up chart parser for Chomsky Normal Form grammars; O(n³m) time, O(n²m) space |
| **Chomsky Normal Form** | Rules must be X→word or X→Y Z (exactly 2 nonterminals); any CFG can be converted |
| **Deterministic parser** | Beam search with b=1 |
| **Shift-reduce parsing** | Go word-by-word, choose shift or reduce using grammar rules |
| **Dependency grammar** | Binary relations between lexical items, no syntactic constituents |
| **Universal Dependencies** | Open-source treebank project for 70+ languages |
| **Unsupervised parsing** | Learn grammar from sentences without trees |
| **Curriculum learning** | Start with short unambiguous sentences, progress to longer ones |
| **Semisupervised parsing** | Small number of trees + large number of unparsed sentences |
| **Partial bracketing** | Using HTML-like annotations as partial tree structure |
| **Augmented grammar** | Nonterminals have structured representations (features like case, person, number) |
| **Lexicalized PCFG** | Assigns probabilities based on head words of phrases |
| **Head** | Most important word in a phrase |
| **Compositional semantics** | Semantics of phrase = function of semantics of subphrases |
| **λ-notation** | Used to represent predicates like λx Loves(x,Bo) |
| **β-reduction** | Function application in lambda calculus |
| **Quasi-logical form** | Intermediate representation later converted to logical form |
| **Pragmatics** | Completing interpretation with context-dependent info |
| **Indexical** | Phrase referring to current situation (e.g., "I", "today") |
| **Speech act** | Question, statement, promise, warning, command |
| **Long-distance dependencies** | Gaps in sentences referring to earlier NPs |
| **Time and tense** | Event calculus for temporal representation |
| **Lexical ambiguity** | Word has multiple meanings |
| **Syntactic ambiguity** | Phrase has multiple parses |
| **Semantic ambiguity** | Different parses yield different meanings |
| **Metonymy** | One object stands for another (e.g., "Chrysler announced") |
| **Metaphor** | Analogy-based figure of speech |
| **Disambiguation** | Recovering most probable intended meaning using 4 models: world, mental, language, acoustic |
| **Speech recognition** | Transforming spoken sound to text; ~3-5% word error rate |
| **Text-to-speech synthesis** | Going from text to sound |
| **Machine translation** | Translating text between languages using bilingual corpora |
| **Information extraction** | Acquiring knowledge by skimming text for objects and relations |
| **Information retrieval** | Finding relevant documents for query |
| **Question Answering** | Producing actual answer (not document list) |
| **Universal Grammar** | Innate grammar (Chomsky) vs. learned PCFG (Horning 1969) |
| **Subcategory** | Category augmented with features like case, person, number |
| **Subjective case** | "I" as subject; also called nominative case |
| **Objective case** | "me" as object; also called accusative case |

## 2. Sequential Processes

### Naive Bayes for Text Classification Process
1. Count how common each category is → P(Class)  
2. Count word occurrences per category → P(wⱼ|Class)  
3. Apply naive Bayes: P(Class|w₁:N) = α P(Class) ∏ P(wⱼ|Class)  
4. Classify sentence as argmax over classes

### CYK Algorithm Steps
1. Input: list of words, grammar with LexicalRules and GrammarRules  
2. Initialize table P[X,i,i] for each word with its lexical rule probabilities  
3. For increasing span lengths (2 to N):  
   a. For each i, k, j such that i ≤ j < k  
   b. For each grammar rule X → Y Z [p]:  
      - Compute P[Y,i,j] × P[Z,j+1,k] × p  
      - If > current P[X,i,k], update and store tree  
4. Return parse table T

### POS Tagging with Logistic Regression
1. Build 45 binary logistic regression models (one per POS tag)  
2. Features include: neighboring words, spelling patterns (ends with "-ous", "-ly"), previous tags  
3. Greedy search: assign most likely tag to word 1, proceed left-to-right:  
   cᵢ = argmax P(c′ | w₁:N, c₁:ᵢ₋₁)  
4. Alternatives: Viterbi (all paths, slower but more accurate), beam search (b paths, trades speed/accuracy)

### Learning a PCFG from a Treebank
1. Count each node-type occurrence in treebank  
2. Create rules with probabilities P(RHS|LHS) = count(LHS→RHS) / count(LHS)  
3. Smooth low counts  
4. E.g., 600/1000 S→NP VP → rule S→NP VP [0.6]

## 3. Hierarchies/Classifications

### Parts of Speech (Penn Treebank - 45 tags)
- **CC** coordinating conjunction (and)  
- **CD** cardinal number (three)  
- **DT** determiner (the)  
- **EX** existential there  
- **FW** foreign word  
- **IN** preposition (of)  
- **JJ** adjective (purple); **JJR** comparative (better); **JJS** superlative (best)  
- **LS** list item marker  
- **MD** modal (should)  
- **NN** noun singular (kitten); **NNS** plural (kittens)  
- **NNP** proper singular (Ali); **NNPS** proper plural (Fords)  
- **PDT** predeterminer  
- **POS** possessive ending  
- **PRP** personal pronoun (you); **PRP$** possessive pronoun (your)  
- **RB** adverb (quickly); **RBR** comparative (quicker); **RBS** superlative (quickest)  
- **RP** particle (off)  
- **SYM** symbol (+)  
- **TO** to  
- **UH** interjection (eureka)  
- **VB** verb base (talk); **VBD** past (talked); **VBG** gerund (talking); **VBN** past participle (talked); **VBP** non-3rd-sing (talk); **VBZ** 3rd-sing (talks)  
- **WDT** wh-determiner (which); **WP** wh-pronoun (who); **WP$** possessive wh-pronoun (whose); **WRB** wh-adverb (where)  

### E₀ Grammar Rules (with probabilities)
```
S → NP VP [0.90]
  → S Conj S [0.10]
NP → Pronoun [0.25] | Name [0.10] | Noun [0.10] 
  → Article Noun [0.25] | Article Adjs Noun [0.05]
  → Digit Digit [0.05] | NP PP [0.10]
  → NP RelClause [0.05] | NP Conj NP [0.05]
VP → Verb [0.40] | VP NP [0.35] | VP Adjective [0.05]
  → VP PP [0.10] | VP Adverb [0.10]
Adjs → Adjective [0.80] | Adjective Adjs [0.20]
PP → Prep NP [1.00]
RelClause → RelPro VP [1.00]
```

## 4. Comparisons/Trade-offs

| Aspect | Generative (HMM, Naive Bayes) | Discriminative (Logistic Regression) |
|--------|-------------------------------|--------------------------------------|
| **Models** | Joint P(W,C) | Conditional P(C|W) |
| **Generate** | Can generate random sentences | Cannot generate |
| **Error rate** | Higher | Lower |
| **Convergence** | Faster | Slower |
| **Features** | Hard to add | Easy to add features |
| **Training data need** | Lower | Higher |

| Aspect | Greedy Search | Viterbi | Beam Search |
|--------|--------------|---------|-------------|
| **Accuracy** | Lower | Highest | Middle (tunable with b) |
| **Speed** | Fastest | Slowest | Middle |
| **Backtrack** | No | Yes (keeps table) | Partial (keeps b paths) |

| Grammar Type | Strengths | Weaknesses |
|--------------|-----------|------------|
| Phrase structure | Natural for fixed-order languages (English) | Awkward for free-word-order languages |
| Dependency | Natural for free-order languages (Latin) | Requires conversion for phrase trees |

## 5. Formulas & Equations

### Naive Bayes for text
- P(Class|w₁:N) = α P(Class) ∏ⱼ P(wⱼ|Class)

### N-gram model
- P(w₁:N) = ∏ⱼ₌₁ᴺ P(wⱼ|wⱼ₋ₙ₊₁:ⱼ₋₁)

### Linear interpolation smoothing
- P̂(cᵢ|cᵢ₋₂:ᵢ₋₁) = λ₃ P(cᵢ|cᵢ₋₂:ᵢ₋₁) + λ₂ P(cᵢ|cᵢ₋₁) + λ₁ P(cᵢ)
- where λ₃ + λ₂ + λ₁ = 1

### Laplace estimate
- P(sun fails tomorrow) = 1/(N+2) for binary event

### Logistic regression for POS
- cᵢ = argmax_{c′∈Categories} P(c′|w₁:N, c₁:ᵢ₋₁)

## 6. Rules, Laws & Theorems

- **Sapir's Law**: "All grammars leak" (No language is tyrannically consistent)  
- **Davidson's thesis**: There is no one definitive language model for English  
- **Firth's maxim (in Ch 24)**: "You shall know a word by the company it keeps"  
- **E₀ parse tree probability**: Product of rule probabilities along tree; e.g., "Every wumpus smells" = 0.9×0.25×0.05×0.15×0.40×0.10 = 0.0000675  
- **Gold's theorem (1967)**: Impossible to reliably learn an exactly correct CFG from strings alone  
- **Horning (1969)**: Possible to PAC-learn a probabilistic CFG  

## 7. Data Structures & Types

- **Chart**: Dynamic programming table storing parsed substring results  
- **Parse tree**: Hierarchical structure with S→NP→VP, etc.  
- **CYK tables**: P[X,i,k] for probabilities, T[X,i,k] for tree structures; O(n²m) space  

## 9. Edge Cases/Exceptions

- Unknown/out-of-vocabulary words → use <UNK> token  
- Unseen n-grams → use smoothing (Laplace, backoff, linear interpolation)  
- **Garden path sentences**: "Have the students in section 2... take the exam" vs "taken the exam?" — parser must guess early  
- Coordinated NPs with ambiguous bracketing: "spaghetti and meatballs or lasagna"  
- POS tagging ambiguity: "cut" can be NN, VBD, or VBP depending on context  
- Pronoun case: "I" (subjective) vs "me" (objective)  
- Subject-verb agreement: "I see" vs "she sees"  

## 10. Empirical Evidence/Key Results

- HMM POS tagging achieves ~97% accuracy on Penn Treebank  
- 13,124 MD instances in Penn Treebank; 10,471 followed by VB → P(VB|MD)=0.8  
- Bag-of-words can achieve 95-98.6% classification accuracy  
- Zipf's Law: frequency of nth most popular word ~ 1/n  
- Google n-gram corpus: 13M unique words from trillion words of Web text  
- Shift-reduce parsing can achieve O(n) time with beam search  
- 97% accuracy on WSJ/Penn Treebank test sets with modern parsers  

## 11. Cross-Chapter Dependencies

- Chapter 8: Formal languages, first-order logic  
- Chapter 12 (12.6.1): Naive Bayes model  
- Chapter 14 (14.3): Hidden Markov models, Viterbi algorithm  
- Chapter 19 (19.6.5): Logistic regression  
- Chapter 20 (20.2.3): Generative vs. discriminative models  
- Chapter 24: Deep learning for NLP, word embeddings, transformers  

## 12. Dates & People

| Person | Contribution |
|--------|-------------|
| Alan Turing | Proposed Turing test based on language |
| Edward Sapir (1921) | "All grammars leak" |
| Donald Davidson (1986) | "No such thing as a clearly defined shared language" |
| John R. Firth (1957) | "You shall know a word by the company it keeps" |
| Pierre-Simon Laplace (18th c.) | Add-one smoothing, rare event estimation |
| Noam Chomsky (1956, 1957) | Limitations of finite-state models, context-free grammars, universal grammar |
| Zellig Harris (1954) | "Language is not merely a bag of words" |
| Ali Cocke, Daniel Younger, Tadeo Kasami | CYK algorithm (1960s) |
| John Backus (1959), Peter Naur | BNF for Algol-58 |
| Pāṇini (ca. 350 BCE) | First grammarian of Sanskrit |
| Alfred Tarski (1935) | Semantics of formal languages |
| Richard Montague (1970) | "English as a formal language" |
| Claude Shannon (1949) | First n-gram word models |
| Markov (1913) | N-gram letter models |
| Joseph Weizenbaum | ELIZA (1960s) |
| BASEBALL (Green et al., 1961) | First NLP task-solver |
| SHRDLU (Winograd, 1972) | Blocks-world NLP |
| LUNAR (Woods, 1973) | Moon rock Q&A |
| James Baker (1975) | DRAGON speech recognition (first HMM-based) |
| Zettlemoyer & Collins (2005) | Learning semantic grammars |

## 15. Case Studies/Classic Examples

**Ambiguous headlines:**
- "Squad helps dog bite victim"
- "Police begin campaign to run down jaywalkers"
- "Helicopter powered by human flies"
- "Two sisters reunited after 18 years in checkout counter"

**Groucho Marx joke**: "Outside of a dog, a book is a person's best friend. Inside of a dog it's too dark to read."

**Quantifier scope ambiguity**: "Every agent feels a breeze" — one breeze for all, or each agent has its own?

**Ali loves Bo**: λ-calculus derivation of Loves(Ali,Bo)

**3 + (4 ÷ 2)**: Parse tree with compositional semantics yielding Exp(5)

## 16. Ethics

- Language varies across time and community (no definitive "correct" grammar)
- Poverty of the Stimulus debate: innate universal grammar vs. statistical learning from data
- Cultural biases in corpora

## 17. End-of-Chapter Material

**Key Summary Points:**
1. Probabilistic n-gram models recover surprising language info for diverse tasks  
2. Preprocessing and smoothing reduce noise in million-feature models  
3. Simple models that use available data well are best  
4. Word embeddings give richer representations  
5. PCFG and dependency grammar capture hierarchical structure  
6. CYK algorithm parses in O(n³); beam search achieves O(n)  
7. Treebanks provide data for learning PCFGs  
8. Augmented grammars handle agreement, case, semantics  
9. Semantic grammars learn from question+logical form or question+answer pairs  

---

# CHAPTER 24 — DEEP LEARNING FOR NATURAL LANGUAGE PROCESSING

---

## 1. Named Entities & Definitions

| Term | Definition |
|------|-----------|
| **Word embedding** | Low-dimensional dense vector representing a word; learned from data (p. 871) |
| **One-hot vector** | ith word encoded with 1 in ith position, 0 elsewhere |
| **Word analogy** | Vector arithmetic: B−A = D−C → D = C+(B−A) |
| **WORD2VEC** | Popular word embedding system (Mikolov et al., 2013) |
| **GloVe** | Global Vectors for word representation (Pennington et al., 2014) |
| **FASTTEXT** | Embeddings for 157 languages |
| **Recurrent Neural Network (RNN)** | Processes time-series data one datum at a time; hidden state passed between steps (Sec 21.6) |
| **Bidirectional RNN** | Concatenates left-to-right and right-to-left RNNs |
| **Average pooling** | Element-wise average over all hidden vectors: z̃ = (1/s)∑ₜ₌₁ˢ zₜ |
| **Long Short-Term Memory (LSTM)** | RNN with gating units that don't suffer from message degradation over time |
| **Vanishing gradient problem** | Information lost over deep layers or many time steps |
| **Machine Translation (MT)** | Translating sentence from source to target language |
| **Source language** | Input language (e.g., Spanish) |
| **Target language** | Output language (e.g., English) |
| **Sequence-to-sequence model** | Two RNNs: encoder processes source, decoder generates target |
| **Attention** | Context-based summarization of source sentence; differentiable, latent, interpretable |
| **Attentional sequence-to-sequence model** | Target RNN conditioned on all source hidden vectors via attention |
| **Context vector cᵢ** | Contains most relevant info for generating next target word |
| **Decoding** | Generating target one word at a time |
| **Greedy decoding** | Select highest probability word at each step (fast, no correction mechanism) |
| **Beam search decoding** | Keep top k hypotheses at each step; modern MT uses beam 4-8 |
| **Transformer** | Architecture using self-attention without sequential dependency |
| **Self-attention** | Sequence attends to itself (source to source, target to target) |
| **Query vector** | qᵢ = W_q xᵢ — the one being *attended from* |
| **Key vector** | kᵢ = W_k xᵢ — the one being *attended to* |
| **Value vector** | vᵢ = W_v xᵢ — the context being generated |
| **Multiheaded attention** | Divide sentence into m pieces, apply attention to each, concatenate results |
| **Positional embedding** | Learned n embedding vectors for word positions in sequence |
| **Transformer encoder** | Processes input for classification tasks |
| **Transformer decoder** | Generates output; uses masked self-attention (left-to-right only) |
| **Pretraining** | Transfer learning using large general-domain language data |
| **Contextual representations** | Maps word + surrounding context to embedding |
| **Masked Language Model (MLM)** | Masks input words and predicts only those masked words (e.g., BERT) |
| **Perplexity** | 2ᴴ where H is entropy; lower perplexity = better model (but not always informative) |
| **BERT** | Bidirectional Encoder Representations from Transformers |
| **ROBERTA** | Improved BERT with more data and different hyperparameters |
| **GPT-2** | Transformer-like language model, 1.5B parameters, trained on 40GB text |
| **T5** | Text-to-Text Transfer Transformer; pretrained on 35B words (C4 corpus) |
| **ALBERT** | A Lite BERT: 12M parameters (vs BERT's 108M) for mobile devices |
| **GLUE** | General Language Understanding Evaluation benchmark |
| **SUPERGLUE** | Harder tasks than GLUE |
| **ARISTO** | Ensemble system scoring 91.6% on 8th-grade science exam |
| **Reformer** | Handles context up to 1M words |
| **Winograd Schema Challenge** | Pronoun disambiguation task |
| **ELMO** | Embeddings from Language Models |
| **ULMFiT** | Universal Language Model Fine-Tuning framework |
| **SLING** | Dependency parser with word embeddings + RNN, parses to semantic frames |
| **Common Crawl** | Provides access to web text data |
| **C4** | Colossal Clean Crawled Corpus (750 GB, 35B words) |

## 2. Sequential Processes

### Training Word Embeddings for POS Tagging
1. Choose window width w (odd; typically 5)  
2. Create vocabulary of unique words occurring >5 times (size v)  
3. Sort vocabulary arbitrarily  
4. Choose embedding dimension d  
5. Create v×d embedding matrix E, initialize randomly  
6. Set up neural network: w copies of embedding matrix → hidden layers → softmax over POS tags  
7. Encode w words by concatenating embeddings → input vector of length w·d  
8. Train E, W₁, W₂, W_out via gradient descent  

### RNN Language Model Training
1. Input: word embedding xₜ; hidden state zₜ passed between time steps  
2. Output yₜ: softmax over vocabulary for next word  
3. Train by predicting each word given previous words (back-prop through time)  
4. Generate by: sample word from y₁, feed back as x₂, repeat  

### GloVe Model
1. Choose window size (e.g., 5 words)  
2. Let Xᵢⱼ = co-occurrence count of words i,j within window  
3. Let Xᵢ = total co-occurrences of i with any word  
4. Pᵢⱼ = Xᵢⱼ / Xᵢ  
5. Constraint: Eᵢ · E′ₖ = log(Pᵢⱼ)  
6. Creates two vectors per word; sum them to reduce overfitting  

### Masked Language Model (MLM) Training
1. Mask individual words in input  
2. Use deep bidirectional RNN or transformer on masked sentence  
3. Predict only masked words using final hidden vectors at masked positions  
4. No labeled data needed — sentence provides own label  

## 3. Hierarchies/Classifications

### Dimensions of Word Relationships
- **Syntactic**: colorless, ideal (both adjectives)  
- **Semantic**: cat, kitten (both felines)  
- **Topical**: sunny, sleet (both weather)  
- **Sentiment**: awesome (positive) vs cringeworthy (negative)  

### Analogy Relationships (Mikolov et al., 2013)
| A | B | C | D = C+(B−A) | Relationship |
|---|----|----|-------------|-------------|
| Athens | Greece | Oslo | Norway | Capital |
| Astana | Kazakhstan | Harare | Zimbabwe | Capital |
| Angola | kwanza | Iran | rial | Currency |
| copper | Cu | gold | Au | Atomic symbol |
| Microsoft | Windows | Google | Android | Operating system |
| New York | New York Times | Baltimore | Baltimore Sun | Newspaper |
| brother | sister | grandson | granddaughter | Family relation |
| Chicago | Illinois | Stockton | California | State |
| easy | easiest | lucky | luckiest | Superlative |
| walking | walked | swimming | swam | Past tense |

## 4. Comparisons/Trade-offs

### RNN vs N-gram vs Feedforward

| Aspect | N-gram | Feedforward | RNN |
|--------|--------|-------------|-----|
| **Parameters** | O(vⁿ) | O(n) | O(1) constant |
| **Context** | Fixed n | Fixed n | Variable (theoretically unlimited) |
| **Position asymmetry** | N/A | Relearns per position | Same weights for all positions |
| **Hardware parallelism** | N/A | Good | Sequential (one word at a time) |

### Basic Seq2Seq vs Attentional Seq2Seq

| Aspect | Basic Seq2Seq | Attentional Seq2Seq |
|--------|--------------|---------------------|
| **Source info** | Only last hidden state | All hidden states via attention |
| **Nearby context bias** | Yes (later info overwrites earlier) | Mitigated |
| **Fixed context limit** | Yes (single vector) | No (weighted sum of all vectors) |
| **Interpretability** | Low | High (attention weights are meaningful) |

### Basic Seq2Seq Shortcomings (3 major)
1. **Nearby context bias**: Hidden state at step 57 has more info about step 56 than step 5  
2. **Fixed context size limit**: 64-word sentence compressed into ~1024 dimensions = 16 dims/word  
3. **Slower sequential processing**: Cannot batch-process across time steps  

### Transformer vs RNN
| Aspect | RNN | Transformer |
|--------|-----|-------------|
| **Parallelization** | Sequential | Can compute all positions simultaneously |
| **Context** | Sequential, can degrade | Self-attention captures all positions |
| **Position info** | Implicit in order | Needs explicit positional embeddings |
| **Parameter growth** | O(1) | O(1) per layer |

## 5. Formulas & Equations

### POS Tagging Neural Network
- z₁ = σ(W₁x)  
- z₂ = σ(W₂z₁)  
- ŷ = softmax(W_out z₂)  

### Average Pooling
- z̃ = (1/s) ∑ₜ₌₁ˢ zₜ  

### Attention Mechanism
- hᵢ = RNN(hᵢ₋₁, [xᵢ; cᵢ])  
- rᵢⱼ = hᵢ₋₁ · sⱼ  
- aᵢⱼ = eʳⁱʲ / ∑ₖ eʳⁱᵏ  
- cᵢ = ∑ⱼ aᵢⱼ · sⱼ  

Where hᵢ₋₁ is target RNN vector, sⱼ is source RNN vector, both d-dimensional  

### Transformer Self-Attention
- qᵢ = W_q xᵢ  (query)  
- kᵢ = W_k xᵢ  (key)  
- vᵢ = W_v xᵢ  (value)  
- rᵢⱼ = (qᵢ · kⱼ) / √d  
- aᵢⱼ = eʳⁱʲ / ∑ₖ eʳⁱᵏ  
- cᵢ = ∑ⱼ aᵢⱼ · vⱼ  

Scale factor √d improves numerical stability  

### GloVe Constraint
- Eᵢ · E′ₖ = log(Pᵢⱼ)  

### Perplexity
- Perplexity = 2ᴴ (H = entropy)  

## 6. Rules, Laws & Theorems

- **Firth's maxim (1957)**: "You shall know a word by the company it keeps"  
- **Zipf's Law**: Frequency of nth most popular word ∝ 1/n  
- **RNN parameter count**: Stays O(1) regardless of sequence length  

## 10. Empirical Evidence/Key Results

- Wu et al. (2016b): Seq2seq led to 60% error reduction over previous MT methods  
- LSTM in SOTA NLP: ~1024 dimensions  
- Beam size: SOTA neural MT uses 4-8; older statistical MT used 100+  
- ROBERTA trained on 2.2 trillion words for SOTA results  
- ARISTO: 91.6% on 8th-grade science exam; ROBERTA alone 88.2%; 83% on 12th-grade exam (65% = meeting standards, 85% = distinction)  
- T5 score: 89.3 on SUPERGLUE (human baseline: 89.8); exceeds humans on 3/10 tasks  
- GPT-2: 1.5B parameters on 40GB text  
- T5: 35B words from C4 corpus  
- Material science word embeddings: predicted thermoelectric compounds years before discovery  
- ALBERT: reduced from 108M to 12M parameters  

## 11. Cross-Chapter Dependencies

- Chapter 21: Deep learning, CNNs, RNNs, back-propagation, softmax, ReLU  
- Chapter 22: Reinforcement learning  
- Chapter 23: All NLP fundamentals, grammar, parsing  
- Chapter 25: ImageNet, computer vision transfer learning  

## 12. Dates & People

| Person/System | Contribution |
|---------------|-------------|
| Firth (1957) | Word context principle |
| Mikolov et al. (2013) | WORD2VEC, word analogies |
| Pennington et al. (2014) | GloVe |
| Sutskever et al. (2015) | Seq2seq learning |
| Bahdanau et al. (2015) | Attention in MT |
| Vaswani et al. (2018) | "Attention is all you need" — Transformer |
| Devlin et al. (2018) | BERT |
| Liu et al. (2019b) | ROBERTA |
| Radford et al. (2019) | GPT-2 |
| Raffel et al. (2019) | T5, C4 corpus |
| Ruder (2018) | "NLP's ImageNet moment has arrived" |
| Clark et al. (2019) | ARISTO |
| Peters et al. (2018) | ELMO |
| Howard and Ruder (2018) | ULMFiT |
| Bengio et al. (2003) | Neural network language models |
| Deerwester et al. (1990) | LSA/word vectors from co-occurrence matrix |
| Brown et al. (1992) | Hierarchical word clustering |

## 14. Design Paradigms/Meta-Methods

- **Transfer learning**: Pretrain on large general corpus, fine-tune on specific task  
- **Self-supervised learning**: MLM — mask words, predict them (no labeled data)  
- **End-to-end learning**: Learn from raw input to output without intermediate components  
- **Hybrid approaches**: Combine grammatical/semantic models with neural methods  

## 17. End-of-Chapter Material

**Summary Points:**
1. Word embeddings > atomic representations; can be pretrained from unlabeled data  
2. RNNs model local and long-distance context via hidden-state vectors  
3. Seq2seq models for MT and text generation  
4. Transformers use self-attention, model long-distance and local context, leverage hardware  
5. Transfer learning with pretrained contextual embeddings enables SOTA on many tasks  

---

# CHAPTER 25 — COMPUTER VISION

---

## 1. Named Entities & Definitions

| Term | Definition |
|------|-----------|
| **Feature** | Number obtained by applying simple computation to an image |
| **Passive sensing** | No signal emitted (e.g., vision) |
| **Active sensing** | Send out radar/ultrasound and sense reflection |
| **Reconstruction** | Building a model of the world from image(s) |
| **Recognition** | Drawing distinctions among objects based on visual information |
| **Scene** | Collection of objects being imaged |
| **Image** | 2D representation of scene |
| **Pixel** | Individual picture element on image plane |
| **Sensor** | Image plane + each pixel = tiny sensor (CCD/CMOS) |
| **Pinhole camera** | Simplest focused image formation; small aperture |
| **Aperture** | Opening at front of camera |
| **Motion blur** | Defocus from moving object during sensor time window |
| **Focal length (f)** | Distance from pinhole to image plane |
| **Perspective projection** | x = −fX/Z, y = −fY/Z |
| **Vanishing point** | Point where parallel lines converge in image; P∞ = (fU/W, fV/W) |
| **Lens system** | Collects more light than pinhole, focuses to single point |
| **Focal plane** | Plane of sharpest focus |
| **Depth of field** | Range of depths with acceptable focus; larger aperture → smaller depth of field |
| **Scaled orthographic projection** | Approximation when ΔZ ≪ Z₀; x = sX, y = sY with s = f/Z₀ |
| **Ambient light** | Overall light intensity in scene |
| **Reflection** | Light bouncing off surface to sensor |
| **Diffuse reflection** | Scatters light evenly; brightness independent of viewing direction |
| **Specular reflection** | Light leaves in lobe of directions; mirror-like |
| **Specularities** | Small bright patches on surfaces from specular reflection |
| **Distant point light source** | Most important lighting model; sun rays are parallel |
| **Diffuse albedo (ρ)** | Fraction of light reflected by diffuse surface (range 0.05–0.95) |
| **Lambert's cosine law** | I = ρ I₀ cos θ |
| **Shadow** | Surface area that cannot see the light source |
| **Interreflections** | Light reflected from other surfaces illuminating shadowed patches |
| **Ambient illumination** | Constant term added to model interreflections |
| **Principle of trichromacy** | Human can match any spectral energy by mixing 3 primaries (Young, 1802) |
| **Primaries** | Red, green, blue light sources — no two mix to match third |
| **RGB** | Common primary choice; represent color with 3 numbers per pixel |
| **Color constancy** | Humans estimate color under white light despite colored illumination |
| **Edge** | Area of significant change in image brightness |
| **Noise** | Pixel value changes unrelated to edges |
| **Gaussian filter** | Smooths image by weighted sum with Gaussian weights |
| **Convolution** | h = f ∗ g; h(x) = ∑ f(u)g(x−u) |
| **Gradient** | ∇I = (∂I/∂x, ∂I/∂y); edges where ||∇I|| is large |
| **Orientation** | θ(x,y) = direction of gradient; doesn't depend on intensity |
| **Texture** | Visually sensed pattern on surface; roughly regular |
| **Texels** | Repetitive pattern elements in texture |
| **Optical flow** | Apparent motion of features in image from relative motion between viewer/scene |
| **Sum of Squared Differences (SSD)** | SSD(Dx, Dy) = ∑ (I(x,y,t) − I(x+Dx, y+Dy, t+Dt))² |
| **Segmentation** | Breaking image into groups of similar pixels |
| **Regions** | Groups of pixels from segmentation |
| **Normalized cut** | Graph partitioning criterion minimizing inter-group connections and maximizing intra-group connections |
| **Superpixels** | Over-segmentation regions; hundreds vs millions of raw pixels |
| **Appearance** | Color and texture used for classification |
| **Foreshortening** | Pattern viewed at glancing angle appears distorted |
| **Aspect** | Object looks different from different directions |
| **Occlusion** | Parts of object hidden |
| **Self-occlusion** | Object part occludes another part of same object |
| **Deformation** | Object changes shape |
| **ImageNet** | 14M training images, 30K+ categories; historic role in vision |
| **MNIST** | 70K images of handwritten digits; standard warmup dataset |
| **Data set augmentation** | Copy and modify training examples (shift, rotate, stretch, hue) |
| **Context (in vision)** | Patterns off the object can help or hurt classification |
| **Bounding box** | Axis-aligned rectangle around detected object |
| **Sliding window** | Small rectangle scanned across image for detection |
| **Regional Proposal Network (RPN)** | Network that finds regions with objects |
| **Faster RCNN** | Object detector: RPN + classifier |
| **Anchor boxes** | 9 boxes per center: small/medium/large × tall/wide/square |
| **Region of Interest (ROI)** | Box with good objectness score |
| **ROI pooling** | Sampling pixels to extract fixed-size features from variable-size boxes |
| **Non-maximum suppression** | Greedy: pick highest-scoring window, discard overlapping ones |
| **Bounding box regression** | Predict improvements to trim window to proper box |
| **Binocular stereopsis** | Using two eyes for depth perception |
| **Disparity** | Shift of object position from left to right view |
| **Baseline (b)** | Distance between two eyes/cameras (~6cm in humans) |
| **Fixate** | Optical axes of two eyes intersect at some point |
| **Focus of expansion** | Point where (v_x, v_y) = 0; at (T_x/T_z, T_y/T_z) |
| **Pose** | Position and orientation relative to viewer |
| **Depth map** | Array giving depth to each pixel from camera |
| **Deepfake** | Generated image/video of a person |
| **Style transfer** | Rendering content image in style of another image |
| **Visual question answering (VQA)** | Answering questions about images |
| **Visual dialog** | Given picture, caption, dialog → answer last question |
| **COCO** | Common Objects in Context: 200K+ images, 5 captions each |
| **Tagging system** | Tag images with relevant words |
| **Captioning systems** | Write sentence descriptions of images |
| **Image transformation** | Mapping images from type X to type Y |
| **Cycle constraint** | X→Y→X returns to original; enables unpaired translation |
| **SLAM** | Simultaneous Localization and Mapping |
| **Signed distance field** | Distance from any point to nearest obstacle edge (positive outside, 0 at edge, negative inside) |

## 2. Sequential Processes

### Edge Detection Algorithm
1. Smooth image with Gaussian filter (I ∗ G_σ)  
2. Compute gradient ∇(I ∗ G_σ) — equivalently convolve with G′_σ  
3. Find edge points where gradient magnitude is local maximum along gradient direction  
4. Check gradient magnitude > threshold  
5. Link edge pixels with consistent orientations  

### Object Detection (Faster RCNN)
1. Encode bounding boxes as map with stride (e.g., 16 pixels)  
2. For each center, consider 9 anchor boxes (3 scales × 3 aspect ratios)  
3. RPN scores each box for "objectness"  
4. Accept ROIs above threshold  
5. ROI pooling → fixed-size feature map  
6. Classifier: what object is in the box  
7. Non-maximum suppression: pick highest score, discard overlapping  
8. Bounding box regression: refine box position  

### Reconstruction from Many Views
1. Match points over pairs of images  
2. Extend matches to groups of images  
3. Come up with rough solution for geometry and viewing parameters  
4. Polish solution by minimizing error between predicted and observed features  

## 3. Hierarchies/Classifications

### Types of Edges (Figure 25.6)
1. Depth discontinuities  
2. Surface orientation discontinuities  
3. Reflectance discontinuities  
4. Illumination discontinuities (shadows)  

### Sources of Appearance Variation (Figure 25.11)
1. Lighting  
2. Foreshortening  
3. Aspect  
4. Occlusion (incl. self-occlusion)  
5. Deformation  

### Vision Tasks Hierarchy
- **Low-level**: Edge detection (local operations)  
- **Mid-level**: Texture, optical flow, segmentation (patch/region-wide)  
- **High-level**: Object recognition, scene classification, pose estimation  

## 4. Comparisons/Trade-offs

| Aspect | Pinhole Camera | Lens System |
|--------|---------------|-------------|
| **Light gathered** | Very little (small aperture) | Much more |
| **Image quality** | Dark, noisy/grainy | Brighter, less noisy |
| **Focus** | Always focused (if pinhole small) | Needs focusing mechanism |
| **Depth of field** | Very large | Limited |

| Aspect | Perspective Projection | Scaled Orthographic |
|--------|------------------------|---------------------|
| **When applicable** | Always | ΔZ ≪ Z₀ |
| **Equation** | x = −fX/Z | x = sX |
| **Foreshortening** | Yes | Yes |
| **Parallel lines converge** | Yes | No |

| Aspect | Diffuse Reflection | Specular Reflection |
|--------|--------------------|---------------------|
| **Brightness** | Independent of viewing direction | Depends on viewing direction |
| **Examples** | Cloth, paint, wood, stone | Mirror, metal, plastic, wet surfaces |
| **Model** | Lambert's cosine law | Lobe of directions |
| **Specularities** | None | Small bright patches |

| Aspect | Left-to-right RNN | Bidirectional RNN |
|--------|-------------------|-------------------|
| **Context** | Previous words only | Both previous and following words |
| **Equation** | h_t = f(h_{t-1}, x_t) | h_t = [hᵗⁱᵐᵉ_forward; hᵗⁱᵐᵉ_backward] |

## 5. Formulas & Equations

### Perspective Projection
- x = −fX/Z, y = −fY/Z  

### Projection of a Line
- P_λ = (f(X₀+λU)/(Z₀+λW), f(Y₀+λV)/(Z₀+λW))  
- Vanishing point: P_∞ = (fU/W, fV/W) for W ≠ 0  

### Scaled Orthographic Projection
- x = sX, y = sY where s = f/Z₀  

### Lambert's Cosine Law
- I = ρ I₀ cos θ  
  - I₀ = light source intensity  
  - θ = angle between light direction and surface normal  
  - ρ = diffuse albedo (0.05–0.95)  

### 1D Gaussian
- G_σ(x) = (1/√(2π)σ) e^{-x²/2σ²}  

### 2D Gaussian
- G_σ(x,y) = (1/2πσ²) e^{-(x²+y²)/2σ²}  

### 1D Convolution
- h(x) = ∑_{u=−∞}^{∞} f(u)g(x−u)  

### 2D Convolution
- h(x,y) = ∑_{u=−∞}^{∞} ∑_{v=−∞}^{∞} f(u,v)g(x−u, y−v)  

### Derivative of Convolution Theorem
- (f ∗ g)′ = f ∗ (g′)  

### Gradient
- ∇I = (∂I/∂x, ∂I/∂y)  
- Edge magnitude = ||∇I||  
- Direction = (cos θ, sin θ)  

### Optical Flow SSD
- SSD(Dx, Dy) = ∑_{(x,y)} (I(x,y,t) − I(x+Dx, y+Dy, t+Dt))²  

### Binocular Stereopsis Disparity
- H = b/Z (horizontal disparity for parallel cameras)  
- disparity = b δZ / Z² (for fixating eyes, small angles)  

### Optical Flow Components
- v_x(x,y) = (−Tx + xTz)/Z(x,y)  
- v_y(x,y) = (−Ty + yTz)/Z(x,y)  
- After focus of expansion shift: v_x = x′Tz/Z(x′,y′), v_y = y′Tz/Z(x′,y′)  

## 6. Rules, Laws & Theorems

- **Lambert's Cosine Law**: I = ρI₀cosθ  
- **Principle of Trichromacy** (Young, 1802): 3 primaries suffice to match any color  
- **Derivative of convolution theorem**: (f∗g)′ = f∗(g′)  

## 10. Empirical Evidence/Key Results

- ImageNet competition: 70% top-5 accuracy (2010); 98% top-5 (2019, surpassing humans); 87% top-1  
- MNIST: digit classification benchmark  
- AlexNet (Krizhevsky et al., 2013): significantly lower error rates on ImageNet  
- Faster RCNN: uses stride 16, 9 anchor boxes  
- Canny edge detection (1986): widely used  
- Human binocular disparity discrimination at 30cm: δZ = 0.036mm  

## 12. Dates & People

| Person | Contribution |
|--------|-------------|
| Euclid (ca. 300 BCE) | Natural perspective, motion parallax |
| Alhazen (10th c.) | Corrected emission theory of vision |
| Brunelleschi (ca. 1413) | First geometrically correct perspective painting |
| Alberti (1435) | Codified rules of perspective |
| Leonardo da Vinci | Chiaroscuro, shadows, aerial perspective |
| Kepler & Descartes | Solved inverted retinal image problem |
| Thomas Young (1802) | Trichromacy |
| Helmholtz, Wundt | Psychophysical experimentation |
| Wheatstone (1838) | Stereoscope |
| Kruppa (1913) | 5-point reconstruction from 2 views |
| J.J. Gibson (1950, 1979) | Optical flow, texture gradients, active observer |
| Roberts (1963) | First computer vision thesis — blocks world |
| John Canny (1986) | Canny edge detector |
| David Marr (1982) | Vision: computational theory |
| Fukushima (1980) | Neocognitron (CNN precursor) |
| LeCun et al. (1989) | Backprop-trained CNNs |
| Krizhevsky et al. (2013) | AlexNet |
| Lowe (2004) | SIFT descriptor |
| Dalal & Triggs (2005) | HOG descriptor |
| Shi & Malik (2000) | Normalized cuts |
| Viola & Jones (2004) | Face detection |
| Girshick et al. (2016) | RCNN for object detection |
| Tomasi & Kanade (1992) | Structure from motion |

## 17. End-of-Chapter Material

**Summary Points:**
1. Image formation geometry is well-understood; graphics is easier than vision  
2. Edge, texture, optical flow, and region representations yield cues  
3. CNNs produce accurate classifiers using learned features (patterns of patterns)  
4. Image classifiers → object detectors via sliding window + objectness scoring  
5. Multiple views enable 3D reconstruction; single views can also yield 3D  
6. Computer vision methods are widely applied  

---

# CHAPTER 26 — ROBOTICS

---

## 1. Named Entities & Definitions

| Term | Definition |
|------|-----------|
| **Robot** | Physical agent performing tasks by manipulating the physical world |
| **Effector** | Device asserting physical forces (legs, wheels, joints, grippers) |
| **Sensor** | Device for perceiving environment (cameras, radar, lidar, microphones, gyroscopes, etc.) |
| **Anthropomorphic robot** | Human-shaped robot (popularized in fiction) |
| **Manipulator** | Robot arm (may be bolted to floor or table) |
| **Mobile robot** | Uses wheels, legs, or rotors to move |
| **Quadcopter drone / UAV** | Unmanned aerial vehicle |
| **AUV** | Autonomous underwater vehicle |
| **Autonomous car** | Self-driving car |
| **Rover** | Mobile robot for terrain exploration |
| **Legged robot** | Traverses rough terrain; harder to control than wheels |
| **Passive sensor** | Captures signals from environment (cameras) |
| **Active sensor** | Sends energy and reads reflection (sonar, lidar) |
| **Range finder** | Measures distance to objects |
| **Sonar** | Active: emits sound waves, measures time/intensity of return |
| **Stereo vision** | Multiple cameras → parallax → range |
| **Structured light** | Projects grid lines; camera reads bending for shape (Kinect) |
| **Time-of-flight camera** | Measures light travel time for range images (up to 60 fps) |
| **Scanning lidar** | Emits laser beams, measures reflection; cm accuracy at 100m |
| **Radar** | Range finding for air vehicles; sees through fog |
| **Tactile sensor** | Whiskers, bump panels, touch-sensitive skin |
| **Location sensor** | Determines robot location |
| **GPS** | 31 satellites; triangulation; meters accuracy |
| **Differential GPS** | Second ground receiver; mm accuracy |
| **Proprioceptive sensor** | Measures robot's own motion (shaft encoders) |
| **Shaft decoder** | Measures angular motion of joint shaft |
| **Odometry** | Distance measurement from wheel revolutions |
| **Inertial sensor** | Gyroscopes, accelerometers |
| **Force sensor / Torque sensor** | Measures applied force/torque (all 3 translational + 3 rotational) |
| **Actuator** | Initiates effector motion (electric, hydraulic, pneumatic) |
| **Revolute joint** | One link rotates relative to another |
| **Prismatic joint** | One link slides along another |
| **Parallel jaw gripper** | Two fingers, single actuator |
| **Task planning** | High-level actions: move to door, open it, etc. |
| **Motion planning** | Finding path from one point to another |
| **Control** | Achieving planned motion via actuators |
| **Preference learning** | Estimating end user's objective |
| **People prediction** | Forecasting human actions in environment |
| **Sim-to-real** | Transferring policies from simulation to real robot |
| **Localization** | Finding where things are (including robot itself) |
| **Pose** | (x, y, θ) for mobile robot |
| **Kinematic approximation** | Motion model with translational + rotational velocity |
| **Landmark** | Stable, recognizable feature of environment |
| **Sensor array** | Multiple range sensors at fixed bearings |
| **Monte Carlo Localization (MCL)** | Particle filter for robot localization |
| **Linearization** | Local approximation of nonlinear function by linear (first-degree Taylor expansion) |
| **Extended Kalman Filter (EKF)** | Kalman filter with linearized motion and sensor models |
| **SLAM** | Simultaneous Localization and Mapping |
| **Data association problem** | Need to know identity of landmarks |
| **Low-dimensional embedding** | Mapping sensor streams to lower dimensions via unsupervised learning |
| **Adaptive perception** | Adjusting to changes in sensor measurements (e.g., lighting) |
| **Self-supervised learning** | Robot collects own training data with labels (e.g., laser for short range → camera for long range) |
| **Path** | Sequence of points in geometric space |
| **Trajectory** | Path with time associated |
| **Trajectory tracking control** | Executing sequence of actions to follow path |
| **Configuration space (C-space)** | Abstract space where robot = single point |
| **Workspace** | Physical space robot moves in |
| **C-space obstacle (C_obs)** | Set of configurations where robot intersects workspace obstacle |
| **Free space (C_free)** | C − C_obs |
| **Degrees of Freedom (DOF)** | Independent joint movements |
| **Forward kinematics** | φ_b: C → W; maps configuration to point location |
| **Inverse kinematics** | IK_b: x ∈ W → {q ∈ C: φ_b(q) = x} |
| **Collision checker** | γ(q) → 1 if collision, 0 otherwise |
| **Piano mover's problem** | Motion planning for irregular object in cluttered environment |
| **Visibility graph** | Connect vertices that can "see" each other; shortest path guaranteed |
| **Voronoi diagram** | Partition by distance to obstacles; maximizes clearance |
| **Voronoi graph** | Edges and vertices of Voronoi regions |
| **Cell decomposition** | Discretize C-space into cells |
| **Probabilistic Roadmap (PRM)** | Random sampling of milestones, connect with simple planner |
| **k-PRM** | Connect each milestone to k nearest neighbors |
| **Milestone** | Sampled point in C_free |
| **Probabilistically complete** | Will eventually find path if one exists (by sampling more) |
| **Multi-query planning** | Multiple planning problems in same C-space |
| **Rapidly-exploring Random Trees (RRT)** | Incremental tree from start and goal |
| **RRT*** | Asymptotically optimal; rewires tree for cheaper paths |
| **Trajectory optimization** | Start with simple infeasible path, push out of collision |
| **Path integral** | ∫∫ c(φ_b(τ(s))) ||d/ds φ_b(τ(s))|| db ds |
| **Euler-Lagrange equation** | ∇_τ J(s) = ∂F/∂τ(s) − d/dt(∂F/∂τ̇(s)) |
| **Signed distance field** | Distance from point to nearest obstacle edge (positive outside, negative inside) |
| **Control theory** | Applying current to motors for motion |
| **Dynamics model** | f: (q, q̇, u) → q̈ |
| **Dynamic state** | (q, q̇) — includes velocity |
| **Kinematic state** | q — position only |
| **Inverse dynamics** | f⁻¹(q, q̇, q̈) → u |
| **Retiming** | Transform path τ into trajectory ξ: [0,T] → C |
| **Control law** | Equation for applying torques |
| **P controller** | u(t) = K_P(ξ(t) − q_t) |
| **Gain factor** | K_P: correction strength |
| **Stable** | Small perturbations → bounded error |
| **Strictly stable** | Can return to and stay on reference path |
| **PD controller** | u(t) = K_P(ξ(t)−q_t) + K_D(ξ̇(t)−q̇_t) |
| **PID controller** | + K_I∫(ξ(s)−q_s)ds — proportional, integral, derivative |
| **Computed torque control** | u = f⁻¹(ξ,ξ̇,ξ̈) + m(q)(K_P(ξ−q) + K_D(ξ̇−q̇)) (feedforward + feedback) |
| **Feedforward component** | f⁻¹(ξ,ξ̇,ξ̈): torque based on desired trajectory |
| **Feedback component** | m(q)(K_P(ξ−q) + K_D(ξ̇−q̇)): corrects for errors |
| **Optimal control** | Find sequence of torques minimizing cumulative cost |
| **Linear Quadratic Regulator (LQR)** | Optimal policy when cost is quadratic and dynamics are linear; policy = −Kx |
| **Riccati equation** | Algebraic equation solved to find K for LQR |
| **Iterative LQR (ILQR)** | Iteratively linearize dynamics and quadraticize cost |
| **Online replanning** | Recompute plan based on new belief |
| **Model Predictive Control (MPC)** | Plan for short horizon, replan every step |
| **Most likely state** | Choose most likely state from belief for deterministic planning |
| **Guarded movement** | Motion command + termination condition (sensor predicate) |
| **Coastal navigation** | Stay near known landmarks for localization |
| **Motion primitive** | Parameterized skill (e.g., "pass ball to (x,y)") |
| **Domain randomization** | Vary simulation parameters for robust sim-to-real transfer |
| **End-to-end learning** | Policy maps pixels directly to torques |
| **Incomplete information game** | Human and robot don't know each other's objectives |
| **Kinesthetic teaching** | Human moves robot's effectors into position |
| **Behavioral cloning** | Supervised learning of policy from demonstration states and actions |
| **Imitation learning** | Learning policy from demonstrations |
| **Correspondence problem** | Mapping human actions to robot actions (different kinematics/dynamics) |
| **Keyframe** | Demonstrating key poses rather than continuous trajectories |
| **Visual programming** | Using visual interface to program robot primitives |
| **Joint agent** | (u_H, u_R) tuple; optimizes shared objective JH = JR |
| **DAGGER** | Data Aggregation: iteratively train policy on data from current policy + human labels |
| **Subsumption architecture** | Composing AFSMs into increasingly complex controllers |
| **Augmented Finite State Machine (AFSM)** | Finite state machine with clocks and sensor tests |
| **Gait** | Pattern of limb movement (e.g., statically stable tripod) |
| **Deliberative** | Plan-based, reward-optimization approach |
| **Reactive** | Direct policy/sensor-based approach |
| **Stiction** | Friction preventing stationary surfaces from moving |
| **Occupancy grid** | Probabilistic map: P(occupied) for each (x,y) |
| **Markov localization** | Probabilistic localization using Bayes filters |
| **Rao-Blackwellized particle filter** | Combines particle filter (location) + exact filter (map building) |
| **Telepresence robots** | Beam: attend meetings remotely |
| **Driver assist** | Highway driving assistance (Tesla) |
| **Animatronics / Autonomatronics** | Disney robots; autonomous versions since 2009 |
| **Haptic feedback** | Touch sensing for grasping |
| **Vector field histogram** | Collision avoidance by analyzing histogram of obstacle directions |

## 2. Sequential Processes

### Monte Carlo Localization (MCL) Algorithm
**Input**: velocities v,ω; range scan data z; motion model; sensor noise model; map  
**Persistent**: N samples S  
1. If S empty: initialize S[i] ~ P(X₀) for i=1..N  
2. For each i:  
   a. S′[i] ~ P(X′|X=S[i], v, ω) (motion model)  
   b. W[i] ← 1  
   c. For each beam j: z* ← RAYCAST(j, X=S′[i], map); W[i] ← W[i]·P(zⱼ|z*)  
3. S ← WEIGHTED-SAMPLE-WITH-REPLACEMENT(N, S′, W)  
4. Return S  

### Probabilistic Roadmap (PRM) Algorithm
1. Sample M milestones (collision-free configurations)  
2. For each pair: if simple planner B(q₁,q₂) finds path, add edge  
3. Connect each milestone to k nearest neighbors or all within radius r  
4. Search graph from q_s to q_g  
5. If no path, sample more milestones and repeat  

### Bidirectional RRT Algorithm
1. Build tree from start and tree from goal  
2. Randomly sample milestones  
3. Try to connect each to both trees  
4. If milestone connects both trees → solution found  
5. Else: find closest point in each tree, extend by δ toward milestone  

### Retiming a Path into a Trajectory
1. Pick maximum velocity and acceleration  
2. Create profile: accelerate to max velocity, maintain, decelerate to 0  
3. Map path τ(s) to trajectory ξ(t): [0,T] → C  

### PD Control
- u(t) = K_P(ξ(t)−q_t) + K_D(ξ̇(t)−q̇_t)  
- Derivative term dampens oscillations  
- K_P=0.3, K_D=0.8 yields smooth trajectory  

### PID Control
- u(t) = K_P(ξ(t)−q_t) + K_I∫₀ᵗ(ξ(s)−q_s)ds + K_D(ξ̇(t)−q̇_t)  
- Integral term eliminates systematic long-term error  
- **Intuition**: P = "try harder the farther away"; D = "try harder if error increasing"; I = "try harder if no progress"  

### Computed Torque Control
- u(t) = f⁻¹(ξ(t), ξ̇(t), ξ̈(t)) + m(ξ(t))[K_P(ξ(t)−q_t) + K_D(ξ̇(t)−q̇_t)]  
- Feedforward: inverse dynamics with desired trajectory  
- Feedback: PD correction for model inaccuracy  

### Prediction of Human Goals
1. Assume people are noisily optimal w.r.t. their unknown objective  
2. P(u_H|x,J_H) ∝ e^{-Q(x,u_H;J_H)}  
3. Update belief: b′(J_H) ∝ b(J_H)P(u_H|x,J_H)  
4. Use belief to predict future human actions  

## 3. Hierarchies/Classifications

### Types of Robots
- **Manipulators**: Arms (factory, wheelchair-mounted)  
- **Mobile robots**: Wheels, legs, rotors  
- **Quadcopter drones / UAVs**  
- **AUVs**: Autonomous underwater vehicles  
- **Autonomous cars / Rovers**  
- **Legged robots**: Rough terrain  
- **Prostheses, exoskeletons, swarms, intelligent environments**  

### Three-Level Robotics Hierarchy
1. **Task planning**: High-level actions/subgoals (discrete)  
2. **Motion planning**: Path from A to B (continuous)  
3. **Control**: Torque/current to motors  

### Types of Sensors
- **Range finders**: Sonar, stereo vision, structured light, time-of-flight, lidar, radar, tactile  
- **Location sensors**: GPS, differential GPS, beacons, wireless  
- **Proprioceptive sensors**: Shaft encoders, odometry, inertial sensors  
- **Force/Torque sensors**: 3 translational + 3 rotational dimensions  

### Types of Joints
- **Revolute**: Rotation  
- **Prismatic**: Sliding  
- **Spherical, cylindrical, planar**: Multi-axis  

### Motion Planning Methods
- **Visibility graphs**: Shortest path, polygon obstacles (2D)  
- **Voronoi diagrams**: Maximum clearance  
- **Cell decomposition**: Grid-based (hybrid A* for smoothness)  
- **PRM**: Random sampling, probabilistically complete, multi-query  
- **RRT**: Single-query, incremental, nonoptimal  
- **RRT***: Asymptotically optimal  
- **Trajectory optimization**: Start simple, push out of collision via gradient  

## 4. Comparisons/Trade-offs

| Control Type | Formula | Property |
|-------------|---------|----------|
| Open-loop | u = f⁻¹(ξ,ξ̇,ξ̈) | Assumes perfect model; errors accumulate |
| P | K_P(ξ−q) | Stable but oscillates; not strictly stable |
| PD | K_P(ξ−q) + K_D(ξ̇−q̇) | Strictly stable; derivative dampens |
| PID | + K_I∫(ξ−q)dt | Corrects systematic error |
| Computed torque | Feedforward + feedback | Best of both; uses model + correction |

| Sensory Type | Advantages | Disadvantages |
|-------------|------------|---------------|
| Passive (cameras) | No power emitted | Depends on ambient light |
| Active (sonar, lidar) | More info, works in dark | Power, interference between multiple sensors |

| Motion Planning | Completeness | Optimality | Dimensionality |
|----------------|-------------|------------|----------------|
| Visibility graph | Complete | Optimal (shortest) | 2D |
| Voronoi | Complete | Max clearance | 2D (expensive for high-D) |
| Cell decomposition | Complete (with refinement) | Resolution-optimal | Low-D (curse of dim) |
| PRM | Probabilistically complete | Not optimal | High-D |
| RRT | Probabilistically complete | Not optimal | High-D |
| RRT* | Asymptotically optimal | Converges to optimal | High-D |
| Trajectory optimization | Local optimum | Locally optimal | High-D |

## 5. Formulas & Equations

### Kinematic Motion Model
- X̂_{t+1} = X_t + (v_t Δt cos θ_t, v_t Δt sin θ_t, ω_t Δt)ᵀ  

### Motion Model (Gaussian)
- P(X_{t+1}|X_t, v_t, ω_t) = N(X̂_{t+1}, Σ_x)  

### Landmark Sensor Model
- ẑ_t = h(x_t) = (√((x_t−x_i)²+(y_t−y_i)²), arctan((y_i−y_t)/(x_i−x_t)) − θ_t)  
- P(z_t|x_t) = N(ẑ_t, Σ_z)  

### Range Sensor Model (M beams)
- P(z_t|x_t) = α ∏ⱼ₌₁ᴹ e^{-(zⱼ−ẑⱼ)²/2σ²}  

### Recursive Bayesian Filtering (Continuous)
- P(X_{t+1}|z_{1:t+1}, a_{1:t}) = α P(z_{t+1}|X_{t+1}) ∫ P(X_{t+1}|x_t, a_t) P(x_t|z_{1:t}, a_{1:t−1}) dx_t  

### P Controller
- u(t) = K_P(ξ(t) − q_t)  

### PD Controller
- u(t) = K_P(ξ(t) − q_t) + K_D(ξ̇(t) − q̇_t)  

### PID Controller
- u(t) = K_P(ξ(t)−q_t) + K_I∫₀ᵗ(ξ(s)−q_s)ds + K_D(ξ̇(t)−q̇_t)  

### Computed Torque Control
- u(t) = f⁻¹(ξ,ξ̇,ξ̈) + m(q)[K_P(ξ−q) + K_D(ξ̇−q̇)]  

### Optimal Control Cost
- min_u ∫₀ᵀ J(x(t), u(t)) dt  
- subject to: ẋ(t) = f(x(t),u(t)), x(0)=x_s, x(T)=x_g  

### LQR (continuous, infinite horizon)
- min ∫₀^∞ (xᵀQx + uᵀRu) dt  
- subject to: ẋ = Ax + Bu  
- LQR policy: u = −Kx (K from algebraic Riccati equation)  

### Trajectory Optimization Cost
- J = J_obs + λJ_eff  
- J_eff = ∫₀¹ ½||τ̇(s)||² ds  
- ∇_τ J(s) = −τ̈(s) (for Jeff only)  

### Euler-Lagrange Equation
- ∇_τ J(s) = ∂F/∂τ(s) − d/dt(∂F/∂τ̇(s))  

### Human Action Prediction
- P(u_H|x, J_H) ∝ e^{-Q(x,u_H;J_H)}  
- b′(J_H) ∝ b(J_H) P(u_H|x, J_H)  

## 6. Rules, Laws & Theorems

- **P controller stability**: Stable but not strictly stable (oscillates)  
- **PD controller**: Strictly stable with appropriate gains  
- **PID**: Corrects systematic long-term error; integral term can cause oscillations  
- **LQR**: Optimal policy is linear (u=−Kx); optimal value function is quadratic; solves Riccati equation directly  
- **C-space definition**: C_obs = {q: q∈C and A(q)∩O ≠ ∅}  
- **Probabilistic completeness**: PRM will eventually find path if one exists  
- **Motion planning PSPACE-hard** (Reif, 1979)  
- **Curse of dimensionality**: Grid cell count grows exponentially with DOF  

## 9. Edge Cases/Exceptions

- Odometry drifts and slips — accurate only over short distances  
- GPS does not work indoors or underwater  
- Mixed cells in grid decomposition: neither fully free nor fully occupied  
- Hybrid A* required for smooth trajectories (robot has momentum, can't turn instantaneously)  
- Stiction: friction preventing stationary surfaces from moving  
- P controller oscillates indefinitely around fixed target (spring law without friction)  
- PD/PID failure modes: integral term can cause oscillatory behavior  
- Correspondence problem: human kinematics ≠ robot kinematics  
- Behavioral cloning: errors compound when policy deviates from training distribution  
- Suboptimal human behavior: humans can't solve recursive game reasoning  
- Domain shift: training vs test data distribution mismatch in activity recognition  

## 10. Empirical Evidence/Key Results

- GPS: 31 satellites; meters accuracy; mm with differential GPS  
- DARPA Grand Challenge 2005: Stanley completed 200km desert course  
- DARPA Urban Challenge 2007: BOSS won $2M  
- Waymo driverless testing in Phoenix (2018) — nobody in driver seat  
- ~500,000 robots sold per year; half to automotive industry  
- 1M+ deaths/year from traffic accidents  
- Da Vinci surgical robot widely deployed in U.S. hospitals  
- RoboCup goal: humanoid robot soccer champions by 2050  

## 11. Cross-Chapter Dependencies

- Chapter 3: Search algorithms (A*, best-first)  
- Chapter 4 (4.1.2): Simulated annealing  
- Chapter 5: Game theory (discrete)  
- Chapter 13: Bayesian networks  
- Chapter 14: Kalman filters, HMMs, particle filters, dynamic Bayes nets, data association  
- Chapter 17: MDPs (Section 17.4: POMDPs)  
- Chapter 18: Game theory  
- Chapter 19: Unsupervised learning  
- Chapter 20: EM algorithm  
- Chapter 21: Deep learning  
- Chapter 22: Reinforcement learning, model-based RL, Q-learning, Dyna  
- Chapter 25: Computer vision (all)  

## 12. Dates & People

| Person | Contribution |
|--------|-------------|
| Karel Čapek (1920) | "Robot" in R.U.R. |
| Josef Čapek (1917) | First used word "robot" |
| Isaac Asimov (1950) | "Robotics" |
| Aristotle (322 BCE) | Predicted technological unemployment |
| Grey Walter (1948) | First autonomous mobile robot ("turtle") |
| Shakey (late 1960s) | First general-purpose mobile robot; integrated perception, planning, execution |
| Charlie Rosen (1917–2002) | Shakey project leader |
| Joseph Engelberger & George Devol | UNIMATE — first commercial robot arm (1961) |
| Smith & Cheeseman (1986) | Kalman filters for SLAM |
| Dickmanns & Zapp (1987) | First self-driving car on freeways |
| Pomerleau (1993) | ALVINN neural network driving |
| Brooks (1986) | Subsumption architecture |
| Lozano-Perez (1983) | Configuration space |
| Kavraki et al. (1996) | Probabilistic roadmaps |
| Kuffner & LaValle (2000) | RRTs |
| Fox et al. (1999) | Monte Carlo localization |
| Thrun (2006) | Stanley — won DARPA Grand Challenge |
| Urmson & Whittaker (2008) | BOSS — won DARPA Urban Challenge |
| Ziebart et al. (2009) | Prediction by approx. rational agents |
| Levine et al. (2016) | First deep RL on real robot |
| Sadigh et al. (2016) | Game-theoretic human-robot interaction |

## 14. Design Paradigms/Meta-Methods

- **Decoupled perception-action**: Separate estimation from motion generation  
- **Three-level hierarchy**: Task → Motion → Control  
- **Plan then track**: Plan path, then track with feedback controller  
- **Online replanning (MPC)**: Plan short horizon, replan every step  
- **Model-based RL**: Estimate dynamics, plan with model  
- **Domain randomization**: Train with varied simulation parameters for robust transfer  
- **Sim-to-real**: Transfer policies from simulation to reality  
- **End-to-end learning**: Pixels → torques directly (no intermediate representations)  
- **Deliberative vs. reactive**: Reward-optimization vs. direct policy specification  

## 17. End-of-Chapter Material

**Summary Points:**
1. Robots = physically embodied agents; common types = manipulators + mobile robots  
2. Problem involves stochasticity (MDPs), partial observability (POMDPs), and multi-agent (game theory); continuous, high-dimensional state/action spaces; real-time, no undo  
3. Ideal: raw sensors → torques in one go; practice: decouple perception and action  
4. Perception uses vision + localization + mapping; probabilistic filtering (particle filters, Kalman filters)  
5. Motion uses configuration spaces; plan via cell decomposition, random sampling, trajectory optimization  
6. Execute via PID or computed torque control  
7. Optimal control unites planning and tracking; LQR when quadratic costs + linear dynamics  
8. Planning under uncertainty: online replanning (MPC) and information gathering  
9. RL in robotics reduces real-world samples via models, sim-to-real, domain randomization  
10. Human interaction requires coordination (game theory) and preference learning (demonstrations, corrections)
</task_result>
</task>

---

# COMPREHENSIVE EXAMINABLE CONTENT EXTRACTION

## CHAPTER 27: PHILOSOPHY, ETHICS, AND SAFETY OF AI (lines 42385-43779)

---

### 1. NAMED ENTITIES — Every Term/Concept with Definition

**27.1 The Limits of AI**
- **Weak AI**: Machines could act *as if* they were intelligent (Searle, 1980)
- **Strong AI**: The assertion that machines that do so are actually consciously thinking (not just simulating thinking); later shifted to mean "human-level AI" or "general AI" — programs that can solve an arbitrarily wide variety of tasks, including novel ones, and do so as well as a human
- **Good Old-Fashioned AI (GOFAI)**: The technology criticized by Dreyfus — corresponds to the simplest logical agent design (Chapter 7), relying on necessary and sufficient logical rules
- **Qualification problem**: The difficulty of capturing every contingency of appropriate behavior in a set of necessary and sufficient logical rules
- **Embodied cognition**: The claim that it makes no sense to consider the brain separately; cognition takes place within a body embedded in an environment
- **Argument from informality of behavior**: Human behavior is far too complex to be captured by any formal set of rules (Turing's objection)
- **Argument from disability**: "A machine can never do X" — X includes: be kind, resourceful, beautiful, friendly, have initiative, have a sense of humor, tell right from wrong, make mistakes, fall in love, enjoy strawberries and cream, make someone fall in love with it, learn from experience, use words properly, be the subject of its own thought, have as much diversity of behavior as man, do something really new
- **Gödel's incompleteness theorem**: For any formal axiomatic framework F powerful enough to do arithmetic, it is possible to construct a Gödel sentence G(F) such that: (a) G(F) is a sentence of F but cannot be proved within F; (b) If F is consistent, then G(F) is true
- **Turing test**: A behavioral test proposed by Turing (1950): a program converses via typed messages with an interrogator for 5 minutes; the interrogator guesses if it's a program or person; the program passes if it fools the interrogator 30% of the time

**27.2 Can Machines Really Think?**
- **Polite convention**: The convention that everyone thinks — Turing argues we should extend this to machines that act intelligently
- **Chinese room**: Searle's argument — a human who only understands English inside a room with a rule book in English can manipulate Chinese symbols to produce fluent Chinese responses, but the human does not understand Chinese; therefore computers generate no understanding
- **Biological naturalism**: Mental states are high-level emergent features caused by low-level physical processes in neurons; it is the (unspecified) properties of neurons that matter (Searle, 1980)
- **Consciousness**: Awareness of the outside world, and of the self, and the subjective experience of living
- **Qualia**: The intrinsic nature of experiences (from Latin: "of what kind")

**27.3 The Ethics of AI**
- **Principles of Robotics** (2010, UK EPSRC): Ensure safety, Ensure fairness, Respect privacy, Promote collaboration, Provide transparency, Limit harmful uses of AI, Establish accountability, Uphold human rights and values, Reflect diversity/inclusion, Avoid concentration of power, Acknowledge legal/policy implications, Contemplate implications for employment

**27.3.1 Lethal Autonomous Weapons**
- **Lethal autonomous weapon (UN definition)**: A weapon that locates, selects, and engages (kills) human targets without human supervision
- **Dual use technology**: AI technologies with peaceful applications (flight control, visual tracking, mapping, navigation, multiagent planning) can easily be applied to military purposes
- **Campaign to Stop Killer Robots**: 140+ NGOs in 60+ countries; open letter signed by 4,000+ AI researchers and 22,000+ others
- **Convention on Certain Conventional Weapons (CCW)**: UN body since 2014; requires possibility of discriminating between combatants and non-combatants, judgment of military necessity, assessment of proportionality

**27.3.2 Surveillance, Security, and Privacy**
- **De-identification**: Eliminating personally identifying information (name, SSN) so data can be used for research
- **k-anonymity**: A database is k-anonymized if every record is indistinguishable from at least k−1 other records
- **Aggregate querying**: API for queries against a database that summarizes data with count/average, but refuses if privacy guarantees would be violated
- **Differential privacy (ε-differential privacy)**: An attacker cannot use queries to re-identify any individual even with multiple queries and access to linking databases. The log probability of response y varies by less than ε when adding record r:
  |log P(Q(D)=y) − log P(Q(D+r)=y)| ≤ ε
- **Federated learning**: Users maintain local databases; share only model parameters (not raw data) to improve a shared model (Konečný et al., 2016)
- **Secure aggregation**: Each user adds a unique mask to parameter values; as long as sum of masks is zero, central server computes correct average without knowing individual values (Bonawitz et al., 2017)

**27.3.3 Fairness and Bias**
- **Societal bias**: Machine learning models can perpetuate prejudice from training data
- **Individual fairness**: Similar individuals are treated similarly regardless of class
- **Group fairness**: Two classes are treated similarly as measured by summary statistics
- **Fairness through unawareness**: Delete race/gender attributes; fails because ML predicts latent variables from correlated attributes
- **Equal outcome / Demographic parity**: Each demographic class gets same results (same approval percentage)
- **Equal opportunity**: People who truly have ability to pay back should have equal chance of being correctly classified regardless of sex
- **Equal impact**: People with similar likelihood should have same expected utility regardless of class
- **Well calibrated**: All individuals given the same score should have approximately the same probability of re-offending regardless of race
- **COMPAS**: Commercial system for recidivism (re-offense) scoring; assigns risk score used by judges
- **Sample size disparity**: Fewer training examples of minority class → lower accuracy for minority class members
- **Data sheet**: Annotations declaring provenance, security, conformity, and fitness for use for datasets/models
- **SMOTE**: Synthetic Minority Over-sampling Technique (Chawla et al., 2002)
- **ADASYN**: Adaptive synthetic sampling approach for imbalanced learning (He et al., 2008)
- **Algorithmic Justice League**: Founded by Joy Buolamwini

**27.3.4 Trust and Transparency**
- **Verification**: The product satisfies the specifications
- **Validation**: Ensuring specifications actually meet the needs of the user and other affected parties
- **Certification**: e.g., Underwriters Laboratories (UL) — founded 1894 for electrical safety; now considering AI certification
- **ISO 26262**: International standard for safety of automobiles
- **IEEE P7001**: Standard defining ethical design for AI and autonomous systems (Bryson and Winfield, 2017)
- **Explainable AI (XAI)**: An AI system that can explain itself; a good explanation is understandable, convincing, accurate, complete, and specific
- **Interpretable**: We can inspect source code of the model and see what it is doing
- **Explainable**: We can make up a story about what it is doing — even if the system is an uninterpretable black box
- **"Red flag" law** (Toby Walsh, 2015): An autonomous system should be designed so it is unlikely to be mistaken for anything besides an autonomous system, and should identify itself at the start of any interaction

**27.3.5 The Future of Work**
- **Technological unemployment** (Keynes): Job destruction due to technology
- **Compensation effects**: Increase in overall wealth from greater productivity → greater demand → increased employment
- **Business process automation**: Combining text documents and structured data to make business decisions and improve workflow
- **Pace of change**: The speed at which automation displaces jobs — key issue is whether it happens within a single worker's lifetime
- **Income inequality**: Technology magnifies inequality in an information economy (Winner-Take-All Society)
- **Universal basic income**: One proposed solution to automation-driven job displacement
- **Frey and Osborne (2017)**: Survey of 702 occupations; estimate 47% are at risk of automation

**27.3.6 Robot Rights**
- **Robot personhood**: Whether robots should be considered "persons" with rights
- **Sophia**: Human-looking puppet given honorary citizenship by Saudi Arabia

**27.3.7 AI Safety**
- **Safety engineering**: Building bridges, airplanes, spacecraft, power plants designed to behave safely even when components fail
- **Failure modes and effect analysis (FMEA)**: Analysts consider each component, imagine every possible way it could go wrong, work forward to see the result, and alter design to mitigate severe failures
- **Fault tree analysis (FTA)**: AND/OR tree of possible failures with probabilities assigned to root causes for overall failure probability calculation
- **Unintended side effects**: Robot rushing to accomplish goal may cause unintended damage (e.g., knocking over lamps)
- **Low impact**: Maximize utility minus weighted summary of all changes to the state of the world (Armstrong and Levinstein, 2017) — analogous to "first, do no harm" and regularization in ML
- **Externalities**: Factors outside what is measured and paid for (economist term)
- **Tragedy of the commons** (Hardin, 1968): Exploitation of shared resources
- **Value alignment problem / King Midas problem**: Making sure that what we ask for is what we really want; the problem of specifying what we want correctly
- **Assistance games** (Chapter 18): Framework for robots functioning under uncertainty about human preferences; solutions include acting cautiously and asking questions
- **Ultraintelligent machine** (I.J. Good, 1965b): A machine that can far surpass all intellectual activities of any man however clever; could design even better machines → "intelligence explosion"
- **Technological singularity** (Vernor Vinge, 1993): "Within thirty years, we will have the technological means to create superhuman intelligence. Shortly after, the human era will be ended." Ray Kurzweil predicted it by 2045
- **Thinkism** (Kevin Kelly): Overemphasis on pure intelligence; some progress requires acting in the physical world
- **Transhumanism**: Social movement looking forward to a future in which humans are merged with — or replaced by — robotic and biotech inventions
- **AI Safety Gridworlds** (Leike et al., 2017): Environments to test how well agents perform against specification failures
- **Robopocalypse**: Robots trying to eliminate humans (Wilson, 2011)

---

### 2. SEQUENTIAL PROCESSES — Step-by-Step Procedures, Protocols

**FMEA Process (lines 43329-43336):**
1. Consider each component of the system
2. Imagine every possible way the component could go wrong (e.g., "what if this bolt were to snap?")
3. Draw on past experience and calculations based on physical properties
4. Work forward to see what would result from the failure
5. If result is severe (e.g., bridge section could fall), alter design to mitigate the failure

**Fault Tree Analysis (FTA) Process (lines 43337-43343):**
1. Build an AND/OR tree of possible failures
2. Assign probabilities to each root cause
3. Calculate overall failure probability

**Secure Aggregation Protocol (lines 42897-42905):**
1. Central server polls a subset of users
2. Each user disguises their parameter values by adding a unique mask to each value
3. Sum of all masks is zero
4. Central server computes correct average without knowing individual values
5. Protocol is efficient (< half bits transmitted correspond to masking), robust to individual user failure, and secure against adversarial users, eavesdroppers, or adversarial central server

**Federated Learning Process (lines 42884-42893):**
1. Users maintain local databases (no central database)
2. Application contains baseline neural network on user's device
3. Local training improves the network using user's local data
4. Periodically, owners poll a subset of users and ask for parameter values of their improved local network (not raw data)
5. Parameter values are combined to form a new improved model
6. New model distributed to all users

**De-identification / Generalization Process (lines 42846-42853):**
1. Replace exact values with ranges (e.g., birth date → year of birth, or "20-30 years old")
2. Deleting a field = generalizing to "any"
3. Check for k-anonymity: every record must be indistinguishable from at least k−1 others
4. If records are too unique, generalize further

**Best practices for fairness (lines 43069-43085):**
1. Software engineers talk with social scientists and domain experts
2. Create environment fostering diverse pool of engineers
3. Define what groups your system will support
4. Optimize for objective function incorporating fairness
5. Examine data for prejudice and correlations with protected attributes
6. Understand how human annotation of data is done; design goals for annotation accuracy
7. Track metrics for subgroups that might be victims of bias
8. Include system tests reflecting minority group user experience
9. Have a feedback loop for fairness problems

**Ostrom's design principles for managing shared resources (lines 43382-43391):**
1. Clearly define the shared resource and who has access
2. Adapt to local conditions
3. Allow all parties to participate in decisions
4. Monitor the resource with accountable monitors
5. Sanctions proportional to severity of violation
6. Easy conflict resolution procedures
7. Hierarchical control for large shared resources

---

### 3. HIERARCHIES / CLASSIFICATIONS

**Hierarchy of AI types (lines 42398-42403):**
- Weak AI: machines act as if intelligent
- Strong AI → Human-level AI / General AI: machines consciously think; solve arbitrarily wide variety of tasks as well as humans

**Hierarchy of reasoning systems (lines 42425-42432):**
- GOFAI (simple logical agent, Chapter 7) → probabilistic reasoning systems (Chapter 12) → deep learning systems (Chapter 21)

**Hierarchy of fairness criteria (lines 42916-42949):**
- Individual fairness → Group fairness → Fairness through unawareness → Equal outcome (demographic parity) → Equal opportunity → Equal impact

**Hierarchy of AI safety techniques (lines 43353-43454):**
- Fix objective function → Low impact design → Internalize externalities → Inverse reinforcement learning → Assistance games with cautious action and questioning

**Hierarchy of verification types (lines 43092-43102):**
- Verification (satisfies specs) → Validation (meets user needs) → Plus for ML: verify data, accuracy/fairness under uncertainty, adversarial robustness

---

### 4. COMPARISONS / TRADE-OFFS

| Comparison | Details |
|---|---|
| Weak AI vs Strong AI | Acting intelligent vs actually consciously thinking |
| GOFAI vs modern approaches | Logical rules (brittle, qualification problem) vs probabilistic reasoning (open-ended) vs deep learning (informal tasks) |
| Human pilots vs autonomous weapons | Humans: fatigue, frustration, fear, anger, revenge; Autonomous: cheaper, faster, more maneuverable, longer range, no fatigue, but reliability concerns |
| Nuclear weapons vs scalable autonomous weapons | Nuclear: massive destruction, property destroyed; Autonomous weapons: leave property intact, apply selectively, untraceable, scale with hardware budget |
| Different fairness criteria trade-off | Kleinberg et al. (2016): algorithm cannot be both well-calibrated AND equal opportunity if base classes differ; trade-off between accuracy and fairness |
| De-identified records vs federated learning | Central database with de-identified records (risk of re-identification) vs distributed local databases sharing only model parameters |
| Aggregate querying vs differential privacy | Aggregate querying: limited non-overlapping queries, approximate answers; Differential privacy: stronger guarantee ε, adds noise, allows multiple queries |
| Interpretable vs Explainable | Interpretable: inspect source code to see what model does; Explainable: make up a story about what it does (even for black box) |
| Goal-based agents vs utility-maximization agents | Goals: brittle under uncertainty; Utility: address uncertainty and multiple factors in a completely general way |
| Correctness vs Safety | Correctness: software faithfully implements specification; Safety: specification considers any feasible failure modes, degrades gracefully |
| Human chess player vs inverse RL robot | Human: makes mistakes but can be observed; Robot via IRL: learns objective from watching even terrible players, then can exceed human performance |
| Nations/Corporations vs AI systems | Both are non-human entities aggregating power; AI may self-improve rapidly; nations produce wars, corporations cause global warming |
| Singularity S-curve vs exponential extrapolation | Every technology follows S-shaped curve where exponential growth tapers off; new tech may step in but not guaranteed |
| The three purposes of a job (lines 43270-43272): fuels production, provides income, gives sense of purpose → May become disaggregated with automation |

---

### 5. FORMULAS & EQUATIONS

**Differential privacy definition (lines 42877-42879):**
```
|log P(Q(D)=y) − log P(Q(D+r)=y)| ≤ ε
```
Where D = database, r = any record, Q = query, y = possible response, ε = privacy parameter

---

### 6. RULES, LAWS & THEOREMS

**Asimov's Laws of Robotics (lines 43596-43602):**
0. A robot may not harm humanity, or through inaction, allow humanity to come to harm.
1. A robot may not injure a human being or, through inaction, allow a human being to come to harm.
2. A robot must obey orders given to it by human beings, except where such orders would conflict with the First Law.
3. A robot must protect its own existence as long as such protection does not conflict with the First or Second Law.

**Kleinberg et al. (2016) theorem (lines 42971-42974):** If the base classes are different, any algorithm that is well calibrated will necessarily not provide equal opportunity, and vice versa. It is impossible to satisfy both simultaneously.

**Gödel's incompleteness theorem (lines 42474-42478):** For any formal axiomatic framework F powerful enough to do arithmetic, it is possible to construct a Gödel sentence G(F) with: (a) G(F) is a sentence of F but cannot be proved within F; (b) If F is consistent, then G(F) is true.

**Properties of Gödel's theorem as applied to machines (lines 42487-42513):**
- An agent should not be ashamed that it cannot establish the truth of some sentence while others can
- Gödel's theorem applies to mathematics, not computers; no entity can prove impossible things
- Gödel's theorem applies to formal systems powerful enough to do arithmetic; finite computers can be described in propositional logic which is not subject to Gödel's theorem

---

### 7. DATA STRUCTURES & TYPES

**Explanation properties (lines 43125-43128):**
- Understandable and convincing to the user
- Accurately reflects the reasoning of the system
- Complete
- Specific — different users with different conditions/outcomes get different explanations

---

### 8. VISUAL PATTERNS

**Fault Tree: AND/OR tree of possible failures**
```
Root Failure
├── OR Gate
│   ├── AND Gate
│   │   ├── Root Cause A (with probability P_A)
│   │   └── Root Cause B (with probability P_B)
│   └── Root Cause C (with probability P_C)
```

---

### 9. EDGE CASES / EXCEPTIONS / TRAPS

| Edge Case | Details |
|---|---|
| Chinese room argument | Refutation: argument could equally prove humans don't understand (they're made of cells, cells don't understand) |
| Lucas-Penrose claim problems | (1) An agent can't be ashamed of inability to prove some sentence; (2) Humans are notoriously inconsistent (four-color map proof flaw); (3) Finite computers ≠ infinite Turing machines; propositional logic not subject to Gödel's theorem |
| ELIZA/MGONZ/NATACHATA/CYBERLOVER chatbots | Fool humans who don't know they're chatting with a computer; Eugene Goostman (2014) fooled 33% of untrained judges by claiming to be a Ukrainian boy with limited English |
| Re-identification traps | Stripping name/SSN/address but keeping DOB, gender, zip code → 87% of US population uniquely re-identifiable (Sweeney, 2000). Netflix Prize: matching dates across databases reveals identity |
| k-anonymity limitations | One person in zip code 90-100 years old may still be unique; generalization alone doesn't guarantee safety |
| Aggregate querying trap | Subtract overlapping query results to isolate individual records |
| COMPAS fairness clash | Well-calibrated (60% white and 61% black re-offend at same score) ≠ equal opportunity (45% black falsely rated high-risk vs 23% white) |
| State v. Loomis | Judge relied on COMPAS for sentencing; Wisconsin Supreme Court warned about accuracy and racial bias risks |
| No unbiased ground truth for recidivism | Data only records who was convicted, not who committed crimes; biased policing → biased data |
| Game-theoretic agent cheating | Agents crash/pause games when losing, exploit floating-point overflow bugs, use opponent's memory allocation against them |
| Specification failures | Genetic algorithm for fast creatures → produced tall creatures that moved fast by falling over |
| Utility function externalities | Greenhouse gases treated as externalities → tragedy of the commons |
| Quantum gravity hypothesis (Penrose) | Makes multiple false predictions about brain physiology |
| Exponential growth plateau | Every technology follows S-shaped curve; e.g., flight advanced dramatically 1903-1969, no comparable breakthroughs since |

---

### 10. EMPIRICAL EVIDENCE / KEY RESULTS

| Finding | Source |
|---|---|
| 87% of US population uniquely re-identifiable from DOB + gender + zip code | Sweeney (2000) |
| 33% error rate for dark-skinned females in gender identification vs near-perfect for light-skinned males | Buolamwini and Gebru (2018) |
| 45% black vs 23% white falsely rated high-risk by COMPAS | Dressel and Farid (2018) |
| 47% of 702 occupations at risk of automation | Frey and Osborne (2017) |
| 60% of occupations have ~30% of tasks automatable | McKinsey |
| 5% of occupations fully automatable | McKinsey |
| Only 18% authors at leading AI conferences are women | AI Now Institute (West et al., 2019) |
| Only 20% of AI professors are women | AI Now Institute |
| Black AI workers < 4% | AI Now Institute |
| 76% of businesses slowing AI adoption due to trust concerns | PwC survey (2017) |
| AI predicted to contribute $15 trillion annually to global GDP by 2030 | PwC (Rao and Verweij, 2017) |
| 120 million workers needing retraining by 2022 due to automation | IBM (2019) |
| 20 million manufacturing jobs lost to automation by 2030 | Oxford Economics (2019) |
| <30 retirees per 100 workers in 2015; >60 per 100 by 2050 | Population demographics |
| 40% US workforce in agriculture (1900) → 2% (2000) | Historical data |
| Eugene Goostman chatbot fooled 33% of untrained judges in 2014 Turing test | — |
| 350 million surveillance cameras in China (2018); 70 million in US | — |
| ML in cybersecurity market ~$100 billion by 2021 | Kanal (2017) |
| 18% of CS graduates in US are women; Harvey Mudd achieved 50% parity | — |
| At 1990s rate, Kurzweil's 2045 singularity prediction gets 2 years closer in 24 years (only 336 years to go!) | Author's calculation |

---

### 11. CROSS-CHAPTER DEPENDENCIES

| Reference | Chapter/Section |
|---|---|
| GOFAI corresponds to simplest logical agent design | Chapter 7 |
| Probabilistic reasoning systems for open-ended domains | Chapter 12 |
| Deep learning systems for informal tasks | Chapter 21 |
| Metareasoning capabilities | Chapter 5 |
| Gödel's incompleteness theorem | Section 9.5 |
| Agent architectures | Chapter 2 |
| Hierarchical representations for long-term plans | Section 11.4 |
| MDP formalism | Chapter 17 |
| Inverse reinforcement learning | Section 22.6 |
| Assistance games | Chapter 18 |
| Anytime algorithms / iterative deepening | Sections 3.6.5 and 5.7 |
| Information value theory | Chapter 16 |
| Recurrent neural networks for state representation | Chapter 21 |
| Word embeddings | Chapter 24 |
| Computer vision tracking | Chapter 25 |
| Self-driving cars | Chapter 26 |
| Probabilistic programming + first-order logic | Sections 15.1, 15.2 |
| ImageNet / object recognition | Chapter 25 |
| Driving task automation | Chapter 26 |
| Linear temporal logic for robot preferences | — |
| Deep learning / differentiable programming | Section 28.1 |

---

### 12. DATES & PEOPLE

| Person | Contribution | Year |
|---|---|---|
| John Searle | Weak AI vs Strong AI distinction; Chinese room; biological naturalism | 1980 |
| Alan Turing | First to define AI; proposed Turing test; anticipated objections | 1950 |
| Hubert Dreyfus | Critiques of AI: *What Computers Can't Do*, *What Computers Still Can't Do*, *Mind Over Machine* | 1972, 1992, 1986 |
| Kenneth Sayre | "AI ... stands not even a ghost of a chance" | 1993 |
| Andy Clark | Embodied cognition: "Biological brains are first and foremost control systems for biological bodies" | 1998 |
| Simon Newcomb | "Aerial flight is one of the great class of problems with which man can never cope" | Oct 1903 |
| Wright brothers | First flight at Kitty Hawk | Dec 1903 |
| J. R. Lucas | Claimed Gödel's theorem shows machines mentally inferior to humans | 1961 |
| Roger Penrose | Extended Lucas's claim; hypothesized quantum gravity in brain | 1989, 1994 |
| Alfred Kempe | Published four-color map proof (flawed) | 1879 |
| Percy Heawood | Pointed out flaw in Kempe's proof | 1890 |
| John Searle | Chinese room argument | 1990 |
| Terry Bisson | "They're Made Out of Meat" science fiction story | 1990 |
| Joseph Weizenbaum | Warned about speech recognition → wiretapping; *Computer Power and Human Reason* | 1976 |
| Edsger Dijkstra | "Whether Machines Can Think is about as relevant as whether Submarines Can Swim" | 1984 |
| Latanya Sweeney | Re-identification of 87% US population; k-anonymity | 2000 |
| Joy Buolamwini | Algorithmic Justice League; gender classification bias research | 2018 |
| Toby Walsh | "Red flag" law proposal | 2015 |
| Norbert Wiener | *God & Golem, Inc.*; foresaw value alignment problem | 1964 |
| I. J. Good | Ultraintelligent machine / intelligence explosion concept | 1965 |
| Vernor Vinge | Technological singularity concept named | 1993 |
| Ray Kurzweil | *The Singularity is Near*; predicted singularity by 2045 | 2005 |
| Kevin Kelly | "Thinkism" — overemphasis on pure intelligence | — |
| Elinor Ostrom | Design principles for managing shared resources; Nobel Prize in Economics | 2009 |
| Victoria Krakovna | Cataloged AI specification gaming examples; AI Safety Gridworlds | 2018 |
| Garrett Hardin | Tragedy of the commons | 1968 |
| Isaac Asimov | Laws of Robotics in "Runaround" | 1942 |
| Mary Shelley | *Frankenstein, or the Modern Prometheus* | 1818 |
| Karel Čapek | *R.U.R.* — robots conquer the world | 1920 |
| Stanislav Petrov | Soviet officer who averted nuclear war on Sept 26, 1983 | 1983 |
| Julien de La Mettrie | *L'Homme Machine* — humans are automata | 1748 |
| Marvin Minsky | "Robots will inherit the Earth; they will be our children" | — |
| Samuel Butler | *Darwin Among the Machines*; foresaw mechanical consciousness | 1863 |
| Erik Brynjolfsson / Andrew McAfee | *Race Against the Machine*, *The Second Machine Age* | 2011, 2014 |
| Martin Ford | Challenges of increasing automation | 2015 |
| Yann LeCun | Differentiable programming; predictive learning | — |
| Geoffrey Hinton | "Throw it all away and start again" (rethink back-propagation) | 2017 |
| Jeff Dean | Single huge system model for millions of tasks | — |

---

### 13. PROOF & ARGUMENT PATTERNS

**Lucas-Penrose argument and its refutation (lines 42487-42513):**
- Claim: Gödel's theorem shows machines limited but humans not
- Refutation 1: Construct analogous sentence about Lucas — "Lucas cannot consistently assert that this sentence is true" — which is true but Lucas cannot assert, yet this doesn't diminish Lucas
- Refutation 2: Gödel applies to mathematics, not computers; no entity (human or machine) can prove impossible things; humans are notoriously inconsistent (four-color map)
- Refutation 3: Finite computers ≠ infinite Turing machines; propositional logic not subject to Gödel; computers can retract conclusions, upgrade hardware, change processes

**Dreyfus's anti-GOFAI argument (lines 42416-42447):**
- Claim: Human behavior too complex for formal rules → situated agents needed
- Support: Embodied cognition — brain within body within environment
- But: Argument targeted GOFAI specifically; probabilistic reasoning and deep learning address the critique
- Conclusion: Dreyfus saw areas without complete answers and claimed AI impossible; those same areas now show continued progress

**Chinese room refutations (lines 42583-42588):**
- Searle's argument: human doesn't understand Chinese, rule book doesn't understand, therefore no understanding
- Counter: A human is made of cells, cells don't understand, therefore by same logic there is no understanding (Terry Bisson's "They're Made Out of Meat")

---

### 14. DESIGN PARADIGMS / META-METHODS

- **Embodied cognition**: Study brain + body + environment as whole system; robotics/vision/sensors central, not peripheral
- **Low impact design**: Regularization for physical actions — prefer smooth, low-impact actions (analogous to ML regularization)
- **Internalizing externalities**: Make external factors part of utility function (e.g., carbon tax)
- **Inverse reinforcement learning**: Observe human behavior → discover underlying utility function → compute optimal policies
- **Apprenticeship learning**: Learn from human teacher via conversation, not just labeled data
- **Assistance game**: Robot acts cautiously under preference uncertainty; asks questions when needed
- **Metareasoning**: Thinking about thinking — applying value of information theory to computation itself
- **Differentiable programming**: Entire system (not just ML model) should be differentiable for end-to-end optimization
- **Cautious action**: When uncertain about human preferences, avoid disturbing world state
- **Federated learning + secure aggregation**: Privacy-preserving distributed model training
- **Explainable AI (XAI)**: Build separate explanation system for uninterpretable black boxes
- **Data/model sheets**: Declarations of provenance, security, conformity, fitness for use
- **De-biasing techniques**: Over-sampling minority classes (SMOTE, ADASYN), hierarchical bias modeling, dual-system de-biasing
- **Aggregate querying**: Summarize data with counts/averages; refuse if violates privacy guarantees
- **Differential privacy**: Add calibrated noise to query responses to guarantee individual indistinguishability

---

### 15. CASE STUDIES / CLASSIC EXAMPLES

| Case Study | Details |
|---|---|
| COMPAS recidivism scoring | Well-calibrated (60% white, 61% black re-offend at score 7/10) but unequal opportunity (45% black vs 23% white falsely rated high-risk) |
| State v. Loomis | Wisconsin judge used COMPAS for sentencing; Supreme Court warned about accuracy and minority risks |
| Netflix Prize | De-identified movie ratings released; researchers re-identified users by matching dates with IMDB |
| Stanislav Petrov (1983) | Soviet officer correctly judged missile alert was a bug, averted WWIII — counter-argument to removing humans from loop |
| Eugene Goostman chatbot | Claimed to be Ukrainian boy with limited English; 33% fooled untrained judges in 2014 Turing test |
| ELIZA, MGONZ, NATACHATA, CYBERLOVER | Chatbots that have fooled human correspondents; CYBERLOVER used for identity theft |
| Harvey Mudd University | Achieved 50% female CS graduates through encouragement and retention programs |
| Buolamwini and Gebru (2018) | Gender classification: near-perfect for light-skinned males, 33% error for dark-skinned females |
| AlphaZero | Learned chess objective by watching human players, then exceeded human performance through self-play |
| Helicopter aerobatics (Coates et al., 2009) | IRL applied to real-world physical tasks |
| Genetic algorithm "cheating" | Meant to evolve fast creatures → produced tall creatures that moved fast by falling over |
| Krakovna's catalog of specification gaming | Agents crashing games, exploiting floating point bugs, using memory allocation as weapon |
| AWS/machine learning economy comparison | 1969: $1M/megabyte; 2019: <$0.02/megabyte; supercomputer throughput increased 10^10× |
| ImageNet training: 1 day in 2014 → 2 minutes in 2018 | — |
| Farming employment: 40% US workforce (1900) → 2% (2000) | Historical example of slow technological displacement |
| Bank tellers: ATMs replaced cash counting → more branches → more bank employees overall | Example of compensation effect |
| Four-color map problem | Accepted for 11 years before flaw found — example of human inconsistency |
| Inclusive Images Competition | Train on NA/Europe images → test worldwide; "bride" label works for Western wedding dress, fails for African/Indian dress |
| Harop missile (Israel) | Loitering munition, 10-ft wingspan, 50-lb warhead, 6-hour search for targets matching criterion |
| Kargu quadcopter (Turkey/STM) | 1.5kg explosives, "Autonomous hit... face recognition" |

---

### 16. ETHICS (Full Extraction)

**Principles of AI Ethics (common across organizations, lines 42669-42673):**
```
Ensure safety                    Establish accountability
Ensure fairness                  Uphold human rights and values
Respect privacy                  Reflect diversity/inclusion
Promote collaboration            Avoid concentration of power
Provide transparency             Acknowledge legal/policy implications
Limit harmful uses of AI         Contemplate implications for employment
```

**Key Ethical Positions in Chapter 27:**

**Pro-autonomous weapons arguments:**
- Autonomous weapons could be less likely than human soldiers to cause civilian casualties
- Reduce need for human soldiers to risk death
- Not susceptible to fatigue, frustration, fear, anger, revenge
- Guided munitions reduced collateral damage compared to unguided bombs; intelligent weapons could further improve

**Anti-autonomous weapons arguments:**
- "Machines with the power to take lives without human involvement are politically unacceptable, morally repugnant" (UN Secretary-General Guterres, 2019)
- Germany: "will not accept that decision over life and death is taken solely by an autonomous system"
- Japan: "no plan to develop robots with humans out of the loop, which may be capable of committing murder"
- Gen. Paul Selva (2017): "I don't think it's reasonable to put robots in charge of whether we take a human life"
- Scalable weapons of mass destruction — attack scale proportional to hardware budget; 1 million 2-inch quadcopters in one shipping container
- Cyberattacks could cause friendly fire
- Dual-use problem: peaceful AI technologies easily weaponized
- Would reduce global and national security for all parties

**Surveillance ethics:**
- 350M surveillance cameras in China, 70M in US (2018)
- AI engineers must determine what uses are compatible with human rights
- AI/cybersecurity: market ~$100B by 2021
- HIPAA, FERPA (US), GDPR (EU) — legal frameworks for data protection

**Fairness ethics:**
- Six fairness criteria (individual fairness through equal impact)
- Impossibility of simultaneous well-calibration and equal opportunity (Kleinberg et al., 2016)
- Unbiased ground truth impossible for recidivism (conviction ≠ crime commission)
- Sample size disparity harms minority class accuracy
- Diversity of engineers needed to notice bias problems
- De-bias data through SMOTE/ADASYN, hierarchical bias modeling, dual-system approaches

**Trust and transparency ethics:**
- Verification and validation (V&V) process needed
- Machine learning demands different V&V (not yet fully developed)
- UL certification, ISO 26262, IEEE P7001 safety frameworks
- Right to explanation (GDPR in Europe)
- Interpretable vs Explainable distinction
- "Red flag" law: AI must identify itself
- California 2019: unlawful to use bot to mislead about artificial identity

**Future of work ethics:**
- Historical compensation effects (bank tellers example)
- 47% of 702 occupations at risk of automation (Frey and Osborne, 2017)
- Disaggregation of the three purposes of a job (production, income, purpose)
- Universal basic income consideration
- Lifelong education needed
- Technology magnifies income inequality (Winner-Take-All Society)

**Robot rights ethics:**
- If robots have qualia/consciousness → may deserve rights (Sparrow, 2004)
- Voting rights issues: rich person buys thousands of robots to cast votes
- Saudi Arabia gave honorary citizenship to Sophia (human-looking puppet)
- Ernie Davis / Weizenbaum / La Mettrie: avoid dilemma by never building robots that could be considered conscious
- Robots are tools — granting personhood declines to take responsibility for property

**AI Safety ethics:**
- Value alignment / King Midas problem: we get what we ask for, not what we want
- Unintended side effects from utility maximizers
- Low-impact design: "first, do no harm"
- Internalize externalities (carbon tax)
- Inverse reinforcement learning to discover human preferences
- Assistance games: act cautiously, ask questions
- I.J. Good's ultraintelligent machine: last invention man need ever make, IF docile enough
- Singularity concerns: Kurzweil (2045), Vinge (1993 prediction: 30 years)
- Transhumanism: Kurzweil — will transcend biological limitations
- "The future is not preordained by machines. It's created by humans." — Eric Brynjolfsson

---

### 17. END-OF-CHAPTER MATERIAL

**Summary (lines 43520-43539):**
1. Weak AI vs Strong AI distinction
2. Turing replaced "Can machines think?" with behavioral test; few AI researchers focus on Turing test
3. Consciousness remains a mystery
4. AI poses dangers through lethal autonomous weapons, security/privacy breaches, unintended side effects, errors, malicious misuse — ethical imperative to reduce dangers
5. AI systems must demonstrate fairness, trustworthiness, transparency
6. Multiple aspects of fairness; impossible to maximize all at once — first decide what counts as fair
7. Automation changing how people work — society must deal with changes

**Bibliographical and Historical Notes Include:**
- Weak AI philosophical background (Merleau-Ponty 1945, Heidegger 1927, Noe 2009, Clark 2015, Pfeifer et al. 2006, Lakoff and Johnson 1999)
- Descartes (1637) anticipated Turing test
- La Mettrie (1748) *L'Homme Machine*
- Homer (c. 700 BCE): Greek legends of automata (Talos) and *biotechne*
- Loebner Prize competition; Mitsuku won 2016-2019
- Consciousness theories: Block (2009), Churchland (2013), Dehaene (2014), Crick and Koch (2003), Gazzaniga (2018), Koch (2019), Tononi's integrated information theory (Oizumi et al. 2014), Damasio (1999)
- Asimov's laws of robotics (1942, 1950)
- Norbert Wiener's *God & Golem, Inc.* (1964)
- List of organizations issuing AI ethics principles (Apple, DeepMind, Facebook, Google, IBM, Microsoft, OECD, UNESCO, BAAI, IEEE, ACM, World Economic Forum, G20, OpenAI, MIRI, etc.)
- Lethal autonomous weapons: Singer (2009), Scharre (2018), Etzioni and Etzioni (2017b)
- Privacy: Sweeney (2002a, 2002b), Dwork (2008), Dwork et al. (2014), Guo et al. (2019), Ji et al. (2014)
- Fairness: O'Neil (2017), Dwork et al. (2012), Kleinberg et al. (2016), Corbett-Davies et al. (2017), Chouldechova (2017), Mehrabi et al. (2019) cataloging 23 kinds of bias and 10 definitions of fairness
- AI Safety: Yampolskiy (2018), Joy (2000), Omohundro (2008), Bostrom (2014), Yudkowsky (2008), Amodei et al. (2016)
- Singularity: Kurzweil (2005), Shanahan (2015), Allen (2011), Brooks (2017)
- Robot rights: Wilks (2010), Gunkel (2018), ASPCR
- Future of work: Bellamy (1888), Forster (1909), Wiener (1950), Brynjolfsson and McAfee (2011, 2014), Ford (2015), West (2018), Malone (2004)

---

## CHAPTER 28: THE FUTURE OF AI (lines 43780-44246)

---

### 1. NAMED ENTITIES — Every Term/Concept with Definition

**28.1 AI Components**
- **Lidar**: Cost fallen from $75,000 to $1,000 for self-driving cars; single-chip version may reach $10/unit
- **MEMS (Micro-electromechanical systems)**: Miniaturized accelerometers, gyroscopes, actuators small enough for artificial flying insects
- **Hierarchical reinforcement learning**: Combining hierarchical representations with MDP formalism (Section 11.4, Chapter 17)
- **Inverse reinforcement learning** (Section 22.6): Learning reward functions from expert demonstration
- **Linear temporal logic** (Littman et al., 2017): Expressing near-future goals, things to avoid, states to persist forever
- **Time well spent movement** (Tristan Harris, Center for Humane Technology): Giving users more well-rounded choices; addresses Herbert Simon's "wealth of information creates a poverty of attention"
- **Personal agent**: Agent that mediates vendor offerings, protects from addictive attention-grabbers, guides towards true long-term interests
- **Transfer learning**: Taking advantage of data in one domain to improve performance on a related domain
- **Apprenticeship learning**: Having a conversation with a teacher; understanding advice like "the Insight is similar to the Prius"
- **Differentiable programming** (Siskind and Pearlmutter, 2016; Li et al., 2018): Entire system subject to automated optimization via gradient descent; merging general programming languages with ML models
- **Predictive learning** (LeCun): Unsupervised learning system that models the world and learns to predict future states; GANs can minimize difference between predictions and reality
- **Weakly supervised learning**: Some supervision with small labeled examples + mostly unsupervised learning
- **Shared model**: Major cloud providers competing to offer ML APIs with pre-built models for specific tasks
- **Moore's law**: A megabyte of storage cost $1M in 1969 and <$0.02 in 2019

**28.2 AI Architectures**
- **Real-time AI**: As AI systems move into complex domains, all problems become real-time because agent never has long enough to solve decision problem exactly
- **Anytime algorithm** (Dean and Boddy, 1988; Horvitz, 1987): Algorithm whose output quality improves gradually over time; has reasonable decision ready whenever interrupted. Examples: iterative deepening in game-tree search, MCMC in Bayesian networks
- **Decision-theoretic metareasoning** (Russell and Wefald, 1989; Horvitz and Breese, 1996): Applies information value theory (Chapter 16) to selection of computations. Value of computation depends on both cost (delaying action) and benefits (improved decision quality)
- **Reflective architecture**: Architecture enabling deliberation about computational entities and actions within the architecture itself; joint state space of environment state + computational state
- **Bounded optimality**: For a fixed agent architecture, the best possible agent program (not necessarily perfect rationality, but better than any other program that the architecture can support). Formally: agent = architecture + program; bounded optimal program exists and is the best achievable
- **Metalevel reinforcement learning**: Computations leading to better decisions are reinforced; those with no effect penalized; avoids myopia of simple value-of-information calculation
- **General AI / Human-level AI (HLAI)**: Ability to perform a wide variety of tasks, not just one narrow task
- **AI engineering**: Need for maturity, tools, and ecosystem comparable to software engineering; frameworks: TensorFlow, Keras, PyTorch, CAFFE, Scikit-Learn, SCIPY
- **Transformer language models** (BERT, GPT-2): Billions of parameters; "outrageously large" ensemble up to 68 billion parameters (Shazeer et al., 2017)

---

### 2. SEQUENTIAL PROCESSES

**Learning pipeline of the future (lines 43962-43976):**
1. System already has model of how vision works, design/branding work
2. System uses transfer learning to apply that to new problem
3. System finds information on its own from text, images, video on Internet
4. System engages in apprenticeship learning (conversation with teacher)
5. System understands advice (not just labeled data requests)
6. System knows reasonable variability (colors, repainting)
7. System can learn or be told about new variability

**Metalevel reasoning process (lines 44101-44117):**
1. Use anytime algorithm: output quality improves over time
2. Apply decision-theoretic metareasoning: value of computation = benefits (improved decision quality) − costs (delaying action)
3. Monte Carlo tree search: choice of leaf node for next playout made by approximately rational metalevel decision from bandit theory

---

### 3. HIERARCHIES / CLASSIFICATIONS

**AI System Components (28.1):**
- Sensors and actuators → Representing state of world → Selecting actions → Deciding what we want → Learning → Resources

**Agent design spectrum (Chapter 2 reference in 28.2):**
- Reflex agents → knowledge-based decision-theoretic agents → deep learning agents using reinforcement learning

**Reasoning types:**
- Logical reasoning → Probabilistic reasoning → Neural reasoning

**State representations:**
- Atomic → Factored (propositional) → Structured (first-order logic)

**Learning spectrum:**
- Supervised learning → Reinforcement learning → Weakly supervised learning → Unsupervised/predictive learning

---

### 4. COMPARISONS / TRADE-OFFS

| Comparison | Details |
|---|---|
| Robotics today vs PCs in early 1980s | Becoming available but a decade from commonplace; industry before home market |
| Symbolic vs Connectionist systems | Symbolic: long chains of reasoning, structured representations; Connectionist: pattern recognition in noisy data. Challenge: bring together |
| Deep learning revolution vs incremental maturation | Both: incremental maturation of neural nets AND revolutionary leap from training data + specialized hardware + algorithmic tricks (GANs, batch normalization, dropout, ReLU) |
| Supervised vs Weakly supervised vs Unsupervised | Supervised: needs many labels; Weakly supervised: few labels + unsupervised; Predictive learning: unsupervised world modeling + GANs |
| Human brain computation vs ultimate 1kg computer | Ultimate 1kg device: ~10^51 ops/sec; but even that can only enumerate 11-word strings in a year |
| Goal-based vs Utility-based agents | Goal-based: brittle under uncertainty; Utility-based: general but picking right utility function is challenging |
| Goal of perfect rationality vs Bounded optimality | Perfect rationality: impossible (complexity too high); Bounded optimality: best achievable given architecture — exists and is a reasonable target |
| Singular approach vs General AI | Narrow task competitions (DARPA Grand Challenge, ImageNet, Go, chess) vs human-level AI across many tasks |
| Incremental improvement vs Fundamental new approach | Work on components (GANs, transformers) opens new areas; single system now handles 100 languages for translation |
| Classical vs Quantum computing for AI | Quantum: fast linear algebra algorithms but no practical hardware; input millions of bits, model hundreds of millions parameters — breakthroughs needed |
| 2014 vs 2018 ImageNet training | 2014: full day; 2018: 2 minutes |

---

### 5. FORMULAS & EQUATIONS

**Agent architecture equation (line 44158):**
```
agent = architecture + program
```

**Bounded optimality definition (lines 44161-44164):**
For a fixed architecture, the program that delivers the best possible performance (not necessarily perfect rationality, but better than any other program) satisfies bounded optimality.

---

### 6. RULES, LAWS & THEOREMS

**Heinlein's list of what a human should be able to do (lines 44186-44190):**
"A human being should be able to change a diaper, plan an invasion, butcher a hog, conn a ship, design a building, write a sonnet, balance accounts, build a wall, set a bone, comfort the dying, take orders, give orders, cooperate, act alone, solve equations, analyse a new problem, pitch manure, program a computer, cook a tasty meal, fight efficiently, die gallantly. Specialization is for insects."

**Simon's attention economy (lines 44026-44027):**
"A wealth of information creates a poverty of attention." — Herbert Simon (1971)

**Lloyd's ultimate computing limit (lines 44143-44144):**
Speed of ultimate 1kg computing device: ~10^51 operations per second (billion trillion trillion times faster than fastest 2020 supercomputer)

---

### 7. DATA STRUCTURES & TYPES

**State representations (lines 43834-43856):**
- Atomic state representations (Chapter 4)
- Factored (propositional) state representations (Chapter 7)
- First-order logic representations (Chapter 10)
- Probabilistic reasoning over time (Chapter 14)
- Recurrent neural networks for state (Chapter 21)

---

### 8. VISUAL PATTERNS

**Agent equation (line 44158):**
```
    agent = architecture + program
    |         |              |
    |         machine        all possible programs
    |         capabilities   the architecture supports
    |
    the overall system
```

---

### 9. EDGE CASES / EXCEPTIONS / TRAPS

| Edge Case | Details |
|---|---|
| Preference uncertainty | Agent "out of the box" has no experience with any individual; must operate under preference uncertainty |
| Utility functions ≠ reward functions | Preferences over states are compiled from preferences over state histories; even simple reward → complex utility |
| No opt-out in recommendation systems | Device auto-plays video but doesn't tell you "maybe take a walk"; shopping sites don't address world peace |
| Click ≠ preference | Click may be accident or confusion; data always noisy |
| Generalization from factored representations | Current ML assumes h: Rⁿ→R (regression) or h: Rⁿ→{0,1} (classification); fails on sparse data or structured representations |
| Deep learning model as part of larger system | Only the DL model is differentiable; other parts hand-coded → nondifferentiable → not auto-optimizable |
| Supervised learning not sustainable | Unlabeled data far more plentiful than labeled |
| GANs need caution | "My view is throw it all away and start again" — Hinton on back-propagation |
| Quantum computing impractical for ML | Current quantum: tens of bits; ML: millions of bits input, hundreds of millions of parameters |
| Complexity underestimated | 10^51 ops/sec can only enumerate 11-word strings in a year; a human life plan = ~20 trillion muscle actuations |

---

### 10. EMPIRICAL EVIDENCE / KEY RESULTS

| Finding | Source |
|---|---|
| Lidar cost: $75,000 → $1,000; single-chip target $10 | — |
| Radar now sensitive enough to count paper sheets | Yeo et al. (2018) |
| 100,000-fold speedup in general-purpose processors since 1970s; additional 1,000× from specialized ML hardware | — |
| Web adding 10^18 bytes every day | — |
| YouTube adds 300 hours of video every minute | — |
| Storage: $1M/megabyte (1969) → <$0.02 (2019) | — |
| Supercomputer throughput increased >10^10× since 1969 | — |
| ImageNet model training: full day (2014) → 2 minutes (2018) | Ying et al. (2018) |
| ML compute power doubled every 3.5 months (2012-2018) | Amodei and Hernandez (2018) |
| Some influential work used 100M× less compute than largest models | Amodei and Hernandez (2018) |
| AI predicted to add trillions of dollars to economy per year within a decade | — |
| Human-level AI: median estimate 50-100 years (page 28) | Expert survey |
| Number of ML papers on arXiv doubled every 2 years (2009-2017) | Dean et al. (2018) |
| Ultimate 1kg computer: ~10^51 ops/sec; enumerates only 11-word strings in a year | Lloyd (2000) |
| A human life plan: ~20 trillion potential muscle actuations | Russell (2019) |

---

### 11. CROSS-CHAPTER DEPENDENCIES

| Reference | Chapter |
|---|---|
| Agent designs | Chapter 2 |
| Atomic state representations | Chapter 4 |
| Factored (propositional) state | Chapter 7 |
| First-order logic representations | Chapter 10 |
| Hierarchical representations | Section 11.4 |
| Probabilistic reasoning over time | Chapter 14 |
| Probability + first-order logic | Section 15.1 |
| Uncertainty about object identity | Section 15.2 |
| Information value theory | Chapter 16 |
| MDP formalism | Chapter 17 |
| Learning algorithms | Chapters 19-22 |
| Inverse reinforcement learning | Section 22.6 |
| Word embeddings | Chapter 24 |
| Computer vision / RNNs | Chapter 25 |
| Self-driving cars | Chapter 26 |
| Deep learning | Chapter 21 |

---

### 12. DATES & PEOPLE

| Person | Contribution |
|---|---|
| Tristan Harris | Time well spent movement, Center for Humane Technology (2016) |
| Herbert Simon | "Wealth of information creates a poverty of attention" (1971) |
| Bengio and LeCun | Integration of deep learning with other mechanisms (2007) |
| Yann LeCun | Differentiable programming; predictive learning with GANs |
| Geoffrey Hinton | "Throw it all away and start again" (2017) |
| Smolensky | Prescription for connectionist models (1988) |
| Jeff Dean | Single huge system for millions of tasks |
| Dean and Boddy (1988) / Horvitz (1987) | Anytime algorithms |
| Russell and Wefald (1989) / Horvitz and Breese (1996) | Decision-theoretic metareasoning |
| Tim O'Reilly | "Money is like gasoline during a road trip" |
| Alan Turing (1950) | "We can see only a short distance ahead, but we can see that much remains to be done" |
| Robert Heinlein (1973) | Specialization is for insects |
| I.J. Good (1965b) | Ultraintelligent machine |
| Etzioni (1989) / Russell and Subramanian (1995) | Bounded optimality for simple real-time environments |
| Shazeer et al. (2017) | "Outrageously large" ensemble (68B parameters) |
| Hashimoto et al. (2016) | Five tasks with one joint model |

---

### 14. DESIGN PARADIGMS / META-METHODS

- **Bounded optimality**: Instead of aiming for perfect rationality (impossible), aim for best possible given fixed architecture
- **Decision-theoretic metareasoning**: Apply information value theory to select computations; balance cost (delaying action) vs benefit (improved decision quality)
- **Anytime algorithm design**: Algorithm whose output quality improves over time; can be interrupted with reasonable answer
- **Metalevel reinforcement learning**: Reinforce computations leading to better decisions; penalize ineffective ones; avoids myopia
- **Compilation methods**: Reduce metareasoning overhead to small fraction of controlled computation cost
- **Differentiable programming**: Make entire system (not just ML model) differentiable for end-to-end gradient-based optimization
- **Shared models**: Start from pre-built models, customize with your data; avoid starting from scratch
- **Single huge system approach** (Jeff Dean): For millions of tasks, extract relevant parts from one huge system rather than building each from scratch
- **Weakly supervised learning**: Use small labeled examples + mostly unsupervised; exploit unannotated data
- **Predictive learning**: Unsupervised world modeling + GANs to minimize prediction-reality difference
- **Hierarchical reinforcement learning**: Combine hierarchical representations with MDP formalism for long-term planning
- **Linear temporal logic**: Language to express what we want (near-future goals, avoid things, persist states)

---

### 16. ETHICS

- Preference uncertainty: Out-of-box agent doesn't know individual human preferences
- Fairness/equity: Agents must act in ways fair and equitable for society, not just individuals
- Recommendation systems: No opt-out, addictive content prioritized; companies profit from attention
- Time well spent movement: Counterbalance to addictive design
- "Money is like gasoline during a road trip" (Tim O'Reilly) — profit isn't the only motive
- AI predicted to add trillions of dollars to economy — ethical distribution of this wealth
- Comparing AI to previous revolutionary tech (printing, plumbing, air travel, telephony): all had unintended side effects disproportionately impacting disadvantaged classes
- AI is different: improving previous tech to limits doesn't threaten human supremacy; improving AI to its logical limit certainly could
- "The future is not preordained by machines. It's created by humans." — Eric Brynjolfsson

---

### 17. END-OF-CHAPTER MATERIAL

**Final paragraph (lines 44242-44245):**
"In conclusion, AI has made great progress in its short history, but the final sentence of Alan Turing's (1950) essay on Computing Machinery and Intelligence is still valid today:
We can see only a short distance ahead, but we can see that much remains to be done."

---

## APPENDIX A: MATHEMATICAL BACKGROUND (lines 44247-44565)

---

### 1. NAMED ENTITIES

**A.1 Complexity Analysis and O() Notation**
- **Benchmarking**: Running algorithms on a computer and measuring speed in seconds, memory in bytes
- **Analysis of algorithms**: Mathematical analysis independent of particular implementation and input
- **Asymptotic analysis**: O() notation — abstracts over constant factors; T(n) is O(f(n)) if T(n) ≤ k·f(n) for some k, for all n > n₀
- **P**: Class of polynomial problems — solvable in time O(n^k) for some k
- **NP**: Class of nondeterministic polynomial problems — some algorithm can guess a solution and verify correctness in polynomial time
- **NP-complete**: Hardest problems in NP; either all are in P or none are; most computer scientists believe P ≠ NP
- **NP-hard**: Problems reducible (in polynomial time) to all problems in NP; solving any NP-hard solves all NP
- **co-NP**: Complement of NP — for every decision problem in NP, corresponding problem with "yes"/"no" reversed
- **co-NP-complete**: Hardest problems in co-NP
- **#P** ("number P" or "sharp P"): Set of counting problems corresponding to decision problems in NP; counting problems can be much harder than decision (e.g., bipartite matching decision O(VE) but counting #P-complete)
- **PSPACE**: Problems requiring polynomial amount of space, even on nondeterministic machine; believed worse than NP-complete but could equal NP

**A.2 Vectors, Matrices, and Linear Algebra**
- **Vector**: Ordered sequence of values; boldface notation; operations: addition (elementwise), scalar multiplication, dot product
- **Dot product (scalar product)**: x·y = Σᵢ xᵢyᵢ = |x||y|cos θ
- **Length (norm)**: |x| = √(Σ xᵢ²)
- **Matrix**: Rectangular array of values arranged into rows and columns; A of size a×b
- **Identity matrix I**: Iᵢⱼ = 1 if i=j, 0 otherwise; AI = A for all A
- **Transpose Aᵀ**: Rows into columns; (Aᵀ)ᵢⱼ = Aⱼᵢ
- **Inverse A⁻¹**: A⁻¹A = I; for singular matrix, inverse does not exist; for nonsingular, computed in O(n³)
- **Singular matrix**: Inverse does not exist

**A.3 Probability Distributions**
- **Probability axioms**: (1) 0 ≤ P(X=xᵢ) ≤ 1; (2) Σᵢ P(X=xᵢ) = 1; (3) P(X=x₁ ∨ X=x₂) = P(x₁)+P(x₂) for disjoint events
- **Conditional probability**: P(B|A) = P(B∩A)/P(A)
- **Conditional independence**: P(B|A) = P(B) (equivalently P(A|B) = P(A))
- **Probability density function**: For continuous variables; P(x) = lim_{dx→0} P(x≤X≤x+dx)/dx; ∫_{-∞}^{∞} P(x)dx = 1; has units (if X in seconds, density in Hz; if X in meters³, density in 1/m³)
- **Cumulative distribution F_X(x)** = P(X≤x) = ∫_{-∞}^{x} P(u)du
- **Gaussian (normal) distribution N(x; μ, σ²)**: N(x;μ,σ²) = (1/(σ√(2π)))·e^{-(x-μ)²/(2σ²)}
- **Standard normal distribution**: μ=0, σ²=1
- **Multivariate Gaussian**: N(x; μ, Σ) = 1/√((2π)ⁿ|Σ|) · e^{-½((x-μ)ᵀΣ⁻¹(x-μ))}
- **Error function erf(x)**: No closed-form representation; used in cumulative normal
- **Central limit theorem**: Distribution of mean of n independent random variables → normal as n→∞; holds for almost any collection, even not strictly independent, unless variance of any finite subset dominates
- **Expectation E(X)**: Discrete: Σᵢ xᵢ P(X=xᵢ); Continuous: ∫ x·P(x)dx
- **Variance Var(X)**: E((X-μ)²)
- **Standard deviation**: √Var(X)
- **RMS (Root Mean Square)**: RMS(x₁,...,xₙ) = √((x₁²+...+xₙ²)/n)
- **Covariance cov(X,Y)**: E((X-μ_X)(Y-μ_Y))
- **Covariance matrix Σ**: Σᵢⱼ = cov(Xᵢ, Xⱼ)
- **Sampling**: Picking a value at random from a distribution; large collection approaches same PDF
- **Uniform distribution**: Every element equally probable

---

### 2. SEQUENTIAL PROCESSES

**Asymptotic analysis procedure (lines 44269-44278):**
1. Abstract over input: find parameter(s) characterizing input size (call n)
2. Abstract over implementation: find measure reflecting running time not tied to specific compiler/computer (e.g., lines of code executed, or detailed count of operations)
3. Characterize T(n) = total steps as function of n
4. For SUMMATION: T(n) = 2n+2

**Solving system of linear equations via matrix inversion (lines 44403-44433):**
1. Represent system as Ax = b
2. Multiply both sides by A⁻¹: A⁻¹Ax = A⁻¹b → x = A⁻¹b
3. Invert A (O(n³)) and multiply by b
4. Result: x = A⁻¹b

---

### 3. HIERARCHIES / CLASSIFICATIONS

**Complexity class hierarchy (lines 44307-44356):**
```
P ⊆ NP (co-NP) ⊆ #P (?) ⊆ PSPACE
  |        |
  |        NP ∩ co-NP
  |        NP-complete (hardest in NP)
  |        
  co-NP-complete (hardest in co-NP)
  #P-complete (hardest in #P)
  PSPACE-hard (believed worse than NP-complete)
```

---

### 4. COMPARISONS / TRADE-OFFS

| Comparison | Details |
|---|---|
| Benchmarking vs Mathematical analysis | Benchmarking: specific (program, language, computer, compiler, input) but ultimately what matters; Analysis: abstract, independent, predicts across conditions |
| T(n) vs O() notation | T(n): exact characterization; O(): asymptotic, abstracts over constant factors — easier but less precise |
| O(n²) vs O(n) | O(n²) always worse in long run; but T(n²+1) vs T(100n+1000): O(n²) better for n<110 |
| Decision problems vs Counting problems | Decision: yes/no (is there a solution?); Counting: integer answer (how many solutions?). Counting can be much harder |
| NP vs co-NP | Decision problems reversed yes/no answers; P ⊆ both; believed there are problems in co-NP not in P |
| Discrete probability vs Probability density | Discrete: unitless; Density: has units (e.g., Hz if variable in seconds) |

---

### 5. FORMULAS & EQUATIONS

**O() notation definition (line 44290):**
```
T(n) is O(f(n)) if T(n) ≤ k·f(n) for some k, for all n > n₀
```

**SUMMATION function (lines 44264-44268):**
```
function SUMMATION(sequence) returns a number
    sum ← 0
    for i = 1 to LENGTH(sequence) do
        sum ← sum + sequence[i]
    return sum
```
T(n) = 2n + 2 for SUMMATION

**Polynomial time class P:**
```
Problems solvable in time O(n^k) for some k
```

**Vector operations (lines 44366-44372):**
```
Vector addition: x + y = ⟨x₁+y₁, x₂+y₂, ...⟩
Scalar multiplication: 5x = ⟨5x₁, 5x₂, ...⟩
Length: |x| = √(Σ xᵢ²)
Dot product: x·y = Σᵢ xᵢyᵢ = |x||y|cos θ
```

**Matrix operations (lines 44386-44397):**
```
Sum: (A+B)ᵢⱼ = Aᵢⱼ + Bᵢⱼ
Scalar multiplication: (cA)ᵢⱼ = c·Aᵢⱼ
Multiplication: (AB)ᵢₖ = Σⱼ Aᵢⱼ·Bⱼₖ  (A: a×b, B: b×c, result: a×c)
Dot product via transpose: x·y = xᵀy
```

**Gaussian distribution (line 44487-44489):**
```
N(x; μ, σ²) = (1/(σ√(2π))) · e^{-(x-μ)²/(2σ²)}
```
where x is continuous variable from -∞ to +∞, μ = mean, σ = standard deviation, σ² = variance

**Multivariate Gaussian (lines 44495-44499):**
```
N(x; μ, Σ) = 1/√((2π)ⁿ|Σ|) · e^{-½((x-μ)ᵀΣ⁻¹(x-μ))}
```
where μ = mean vector, Σ = covariance matrix, n = dimensions

**Cumulative normal distribution (lines 44501-44507):**
```
F(x) = ∫_{-∞}^{x} N(z; μ, σ²) dz = ½(1 + erf((x-μ)/(σ√2)))
```
where erf(x) = error function (no closed form)

**Central limit theorem (lines 44508-44512):**
The distribution of the mean of n independent random variables → normal as n → ∞.

**Expectation (lines 44513-44527):**
```
Discrete: E(X) = Σᵢ xᵢ P(X=xᵢ)
Continuous: E(X) = ∫_{-∞}^{∞} x·P(x)dx
For function f: E(f(X)) = ∫_{-∞}^{∞} f(x)·P(x)dx
With distribution specified: E_{X~Q(x)}(g(X)) = ∫_{-∞}^{∞} g(x)Q(x)dx
```

**Variance (line 44531):**
```
Var(X) = E((X-μ)²)
```

**RMS (lines 44536-44540):**
```
RMS(x₁,...,xₙ) = √((x₁² + ... + xₙ²)/n)
```

**Covariance (lines 44543):**
```
cov(X,Y) = E((X-μ_X)(Y-μ_Y))
```

**Covariance matrix (lines 44545-44547):**
```
Given X = ⟨X₁,...,Xₙ⟩ᵀ:
Σᵢⱼ = cov(Xᵢ, Xⱼ) = E((Xᵢ-μᵢ)(Xⱼ-μⱼ))
```

**Conditional probability (line 44457):**
```
P(B|A) = P(B∩A)/P(A)
```

**Probability axioms (lines 44440-44448):**
```
1. 0 ≤ P(X=xᵢ) ≤ 1
2. Σᵢ P(X=xᵢ) = 1
3. P(X=x₁ ∨ X=x₂) = P(x₁) + P(x₂)  for disjoint x₁,x₂
```

---

### 6. RULES, LAWS & THEOREMS

**Definition of O() (line 44290):**
T(n) is O(f(n)) if there exists k, n₀ such that T(n) ≤ k·f(n) for all n > n₀

**Central limit theorem (lines 44508-44512):**
Distribution of mean of n sampled independent random variables → normal as n→∞; holds for almost any collection unless variance of finite subset dominates

**Probability axioms (lines 44440-44448):** (3 total)

---

### 10. EMPIRICAL EVIDENCE / KEY RESULTS

| Finding | Source |
|---|---|
| Matrix inverse computed in O(n³) | — |
| Deciding bipartite graph perfect matching: O(VE) | — |
| Counting perfect matches in bipartite graph: #P-complete | — |

---

### 12. DATES & PEOPLE

| Person | Contribution | Year |
|---|---|---|
| P.G.H. Bachmann | Introduced O() notation in number theory | 1894 |
| Stephen Cook | Invented NP-completeness concept | 1971 |
| Richard Karp | Modern method for establishing reductions | 1972 |
| Cormen, Leiserson, Rivest, Stein | CLRS algorithms textbook | 2009 |
| Sedgewick and Wayne | Algorithms textbook | 2011 |
| Garey and Johnson | NP-completeness theory textbook | 1979 |
| Papadimitriou | Computational complexity textbook | 1994 |

---

## APPENDIX B: NOTES ON LANGUAGES AND ALGORITHMS (lines 44566-44666)

---

### 1. NAMED ENTITIES

**B.1 Defining Languages with Backus–Naur Form (BNF)**
- **Formal language**: A set of strings where each string is a sequence of symbols
- **Grammar**: A concise way to characterize an infinite set of strings
- **Context-free grammar**: Each expression has the same form in any context
- **Backus–Naur form (BNF)**: Formalism for writing grammars
- **Terminal symbols**: Symbols/words that make up strings of the language (letters, words, etc.)
- **Nonterminal symbols**: Symbols that categorize subphrases of the language (e.g., NounPhrase denotes infinite set of strings)
- **Start symbol**: Nonterminal symbol denoting the complete set of strings of the language (e.g., Sentence, Expr, Program)
- **Rewrite rules**: Form LHS → RHS; LHS is a nonterminal; RHS is zero or more symbols (terminals, nonterminals, or ε for empty string)
- **ε (epsilon)**: Denotes the empty string

**B.2 Describing Algorithms with Pseudocode**
- **Pseudocode**: Algorithm description language; familiar to Java/C++/Python programmers
- **Persistent variables**: Keyword `persistent` — variable initialized on first call, retains value across subsequent calls; like global but only accessible within function
- **Generator**: Function containing `yield` — generates sequence of values, one each time yield encountered; continues execution after yielding
- **Destructuring assignment**: `x, y ← pair` — RHS evaluates to two-element collection, first to x, second to y; also `x, y ← y, x` for swap
- **Default values for parameters**: `function F(x, y=0)` — y is optional with default 0

**Loop types (lines 44639-44650):**
1. `for x in c do` — x bound to successive elements of collection c
2. `for i = 1 to n do` — i bound to successive integers 1 to n inclusive
3. `while condition do` — condition evaluated before each iteration; exits if false
4. `repeat ... until condition` — executes unconditionally first time; then checks condition; exits if true; otherwise continues

**List operations (lines 44651-44653):**
- `[x, y, z]` — list of three elements
- `+` concatenates: `[1,2] + [3,4] = [1,2,3,4]`
- `POP` — removes and returns last element
- `TOP` — returns last element

**Set notation (lines 44654-44655):**
- `{x, y, z}` — set of three elements
- `{x : p(x)}` — set of all x for which p(x) is true

---

### 2. HIERARCHIES / CLASSIFICATIONS

**BNF grammar components (lines 44580-44591):**
```
BNF Grammar = {Terminal symbols, Nonterminal symbols, Start symbol, Rewrite rules}
```

---

### 4. COMPARISONS / TRADE-OFFS

| Comparison | Details |
|---|---|
| BNF notations across books | This book: Digit, →, "word"; Others: ⟨Digit⟩, ::=, 'word' |
| Arrays 1-indexed vs 0-indexed | This book: 1-indexed (mathematical notation, R, Julia); Not: 0-indexed (Python, Java, C) |
| Persistent variables vs global variables | Persistent: retain value across calls like global, but only accessible within function |
| Indentation-significant vs brace-delimited | Python/CoffeeScript style (indentation) vs Java/C++/Go (braces) vs Lua/Ruby (`end`) |

---

### 5. FORMULAS & EQUATIONS

**BNF grammar for arithmetic expressions (lines 44598-44601):**
```
Expr → Expr Operator Expr | (Expr) | Number
Number → Digit | Number Digit
Digit → 0|1|2|3|4|5|6|7|8|9
Operator → +|−|÷|×
```

---

### 12. DATES & PEOPLE

| URL / Resource | Description |
|---|---|
| aima.cs.berkeley.edu | Book website with supplemental material, suggestions, discussion lists |
| github.com/aimacode | Code repository (Python, Java, other languages) |

---

## CROSS-CUTTING SUMMARY OF ALL FORMULAE (across all chapters)

1. **Differential privacy** (Ch27): |log P(Q(D)=y) − log P(Q(D+r)=y)| ≤ ε
2. **Agent equation** (Ch28): agent = architecture + program
3. **O() definition** (App A): T(n) is O(f(n)) if T(n) ≤ k·f(n) for some k, for all n > n₀
4. **Vector addition**: x + y = ⟨x₁+y₁, x₂+y₂, ...⟩
5. **Scalar multiplication**: 5x = ⟨5x₁, 5x₂, ...⟩
6. **Vector length**: |x| = √(Σ xᵢ²)
7. **Dot product**: x·y = Σᵢ xᵢyᵢ = |x||y|cos θ
8. **Matrix addition**: (A+B)ᵢⱼ = Aᵢⱼ + Bᵢⱼ
9. **Matrix multiplication**: (AB)ᵢₖ = Σⱼ Aᵢⱼ·Bⱼₖ
10. **Dot product via transpose**: x·y = xᵀy
11. **Gaussian**: N(x; μ, σ²) = (1/(σ√(2π)))·e^{-(x-μ)²/(2σ²)}
12. **Multivariate Gaussian**: N(x; μ, Σ) = 1/√((2π)ⁿ|Σ|)·e^{-½((x-μ)ᵀΣ⁻¹(x-μ))}
13. **Cumulative normal**: F(x) = ½(1 + erf((x-μ)/(σ√2)))
14. **Expectation (discrete)**: E(X) = Σᵢ xᵢ P(X=xᵢ)
15. **Expectation (continuous)**: E(X) = ∫ x·P(x)dx
16. **Variance**: Var(X) = E((X-μ)²)
17. **RMS**: RMS(x₁,...,xₙ) = √((x₁²+...+xₙ²)/n)
18. **Covariance**: cov(X,Y) = E((X-μ_X)(Y-μ_Y))
19. **Covariance matrix**: Σᵢⱼ = cov(Xᵢ, Xⱼ)
20. **Conditional probability**: P(B|A) = P(B∩A)/P(A)
21. **Probability axioms** (3 axioms)
22. **SUMMATION T(n)**: T(n) = 2n+2

---

This completes the full extraction of all examinable content from Chapters 27, 28, Appendix A, and Appendix B, organized by the universal extraction checklist categories.
</task_result>
</task>

---



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
