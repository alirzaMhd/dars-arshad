# Chapters 8-11 Study Notes: First-Order Logic, Inference, Knowledge Representation & Automated Planning

---

## CHAPTER 8: FIRST-ORDER LOGIC
*Lines 11196-12399*

---

### 1. NAMED ENTITIES & DEFINITIONS

| Term | Definition |
|------|------------|
| **First-Order Logic (FOL)** | Also called first-order predicate calculus (FOPC). A logic that assumes the world consists of objects with relations among them. Concise, structured representation. |
| **Compositionality** | The meaning of a sentence is a function of the meaning of its parts (e.g., meaning of S₁₄ ∧ S₁₂ is a function of S₁₄ and S₁₂). |
| **Factored representation** | Propositional logic is factored — treats each atomic fact as indivisible. Lacks power to describe multiple objects concisely. |
| **Structured representation** | Representation like FOL or English that can describe objects and relations (e.g., "Squares adjacent to pits are breezy" = one sentence vs. many propositional ones). |
| **Object** | A thing in the world (people, houses, numbers, theories, colors, wars, centuries...). |
| **Relation** | A link among objects. Unary = property (red, round); n-ary = brother of, bigger than, inside, owns... |
| **Function** | A relation with exactly one value for a given input (father of, best friend, one more than...). |
| **Ontological commitment** | What a language assumes exists in reality. Propositional logic: facts. FOL: facts, objects, and relations. Temporal logic: adds times. |
| **Epistemological commitment** | Possible states of knowledge about a fact. FOL/propositional: true/false/unknown. Probability: degree of belief ∈ [0,1]. |
| **Domain** | The set of objects (domain elements) in a model. Must be nonempty. |
| **Tuple** | A collection of objects arranged in fixed order, written ⟨objects⟩. |
| **Property** | A unary relation (e.g., red, round, king). |
| **Total functions** | In FOL models, functions must have a value for every input tuple. |
| **Constant symbol** | A symbol that stands for an object (e.g., Richard, John). |
| **Predicate symbol** | A symbol that stands for a relation (e.g., Brother, OnHead, King). |
| **Function symbol** | A symbol that stands for a function (e.g., LeftLeg). |
| **Arity** | The number of arguments a predicate or function symbol takes. |
| **Interpretation** | Maps constant symbols → objects, function symbols → functions, predicate symbols → relations. |
| **Intended interpretation** | The interpretation a knowledge engineer "intends" (e.g., Richard → Richard the Lionheart). |
| **Term** | A logical expression that refers to an object. Constant symbols, variables, and complex terms (function applied to terms). |
| **Ground term** | A term with no variables. |
| **Atomic sentence (atom)** | A predicate symbol optionally followed by a parenthesized list of terms (e.g., Brother(Richard, John)). |
| **Quantifier** | ∀ (universal) and ∃ (existential). Express properties of collections of objects. |
| **Universal quantifier (∀)** | "For all." ∀x P means P is true for every object x. |
| **Existential quantifier (∃)** | "There exists." ∃x P means P is true for at least one object x. |
| **Variable** | Lowercase letter (x, y, z) used with quantifiers. A term by itself. |
| **Extended interpretation** | Interpretation that assigns a domain element to a quantifier variable. |
| **Equality symbol (=)** | Signifies two terms refer to the same object. |
| **Unique-names assumption** | Every constant symbol refers to a distinct object. |
| **Closed-world assumption** | Atomic sentences not known to be true are false. |
| **Domain closure** | No more domain elements than those named by constant symbols. |
| **Database semantics** | Semantics with unique-names + closed-world + domain closure. |
| **Assertion** | A sentence added to a knowledge base via TELL. |
| **Query / Goal** | A question asked with ASK. |
| **Substitution / Binding list** | Answer from ASKVARS, e.g., {x/John, x/Richard}. |
| **Domain** | Some part of the world about which we express knowledge. |
| **Axiom** | A sentence that is part of the basic factual knowledge of a domain. |
| **Theorem** | A sentence entailed by the axioms. |
| **Definition** | An axiom of the form ∀x,y P(x,y) ⇔ ... . |
| **Peano axioms** | Define natural numbers recursively: NatNum(0); ∀n NatNum(n) ⇒ NatNum(S(n)). |
| **Infix** | Binary operator placed between arguments (e.g., m+0). |
| **Prefix** | Operator placed before arguments (standard FOL notation). |
| **Syntactic sugar** | Extensions to standard syntax that don't change semantics (infix, square brackets, collapsed quantifiers). |
| **Set** | Mathematical entity: empty set {}, member ∈, subset ⊆, union ∪, intersection ∩. |
| **List** | Ordered, can have duplicate elements. Uses Cons, Append, First, Rest, Nil. |
| **Percept** | A sentence storing sensor input with time: Percept([Stench,Breeze,Glitter,None,None],5). |
| **Knowledge engineering** | The process of constructing a knowledge base: identify questions → assemble knowledge → decide vocabulary → encode axioms → encode instances → pose queries → debug. |
| **Knowledge acquisition** | Extracting knowledge from human experts. |
| **Ontology** | The vocabulary of predicates, functions, and constants for a domain. Determines what kinds of things exist. |
| **Truth value** | In FOL, a sentence is true/false relative to a model. |

### 2. ONTOLOGICAL VS. EPISTEMOLOGICAL COMMITMENTS TABLE

| Language | Ontological Commitment | Epistemological Commitment |
|----------|----------------------|--------------------------|
| Propositional logic | facts | true/false/unknown |
| First-order logic | facts, objects, relations | true/false/unknown |
| Temporal logic | facts, objects, relations, times | true/false/unknown |
| Probability theory | facts | degree of belief ∈ [0,1] |
| Fuzzy logic | facts with degree of truth ∈ [0,1] | known interval value |

### 3. FOL SYNTAX (BNF GRAMMAR)

```
Sentence → AtomicSentence | ComplexSentence
AtomicSentence → Predicate | Predicate(Term, ...) | Term = Term
ComplexSentence → (Sentence) | ¬ Sentence | Sentence ∧ Sentence | Sentence ∨ Sentence
                 | Sentence ⇒ Sentence | Sentence ⇔ Sentence | Quantifier Variable,... Sentence
Term → Function(Term, ...) | Constant | Variable
Quantifier → ∀ | ∃
Operator Precedence (highest to lowest): ¬, =, ∧, ∨, ⇒, ⇔
```

### 4. QUANTIFIER RULES

**De Morgan's Laws for Quantifiers:**

| Quantifier Rule | Propositional Analog |
|----------------|---------------------|
| ¬∃x P ≡ ∀x ¬P | ¬(P ∨ Q) ≡ ¬P ∧ ¬Q |
| ¬∀x P ≡ ∃x ¬P | ¬(P ∧ Q) ≡ ¬P ∨ ¬Q |
| ∀x P ≡ ¬∃x ¬P | P ∧ Q ≡ ¬(¬P ∨ ¬Q) |
| ∃x P ≡ ¬∀x ¬P | P ∨ Q ≡ ¬(¬P ∧ ¬Q) |

**Key patterns:**
- ∀ is natural with ⇒: ∀x (King(x) ⇒ Person(x))
- ∃ is natural with ∧: ∃x (Crown(x) ∧ OnHead(x, John))
- Common mistake: ∀x (King(x) ∧ Person(x)) means EVERYTHING is both a king and person

**Order of quantifiers matters:**
- ∀x ∃y Loves(x,y): Everyone loves someone
- ∃y ∀x Loves(x,y): Someone is loved by everyone

### 5. FOL AXIOMS FOR KEY DOMAINS

**Kinship Domain:**
- Mother: ∀m,c Mother(c) = m ⇔ Female(m) ∧ Parent(m,c)
- Husband: ∀w,h Husband(h,w) ⇔ Male(h) ∧ Spouse(h,w)
- Parent-Child: ∀p,c Parent(p,c) ⇔ Child(c,p)
- Grandparent: ∀g,c Grandparent(g,c) ⇔ ∃p Parent(g,p) ∧ Parent(p,c)
- Sibling: ∀x,y Sibling(x,y) ⇔ x≠y ∧ ∃p Parent(p,x) ∧ Parent(p,y)

**Peano Axioms (Natural Numbers):**
- NatNum(0)
- ∀n NatNum(n) ⇒ NatNum(S(n))
- ∀n 0 ≠ S(n)
- ∀m,n m ≠ n ⇒ S(m) ≠ S(n)
- Addition: ∀m NatNum(m) ⇒ +(0,m) = m
- Addition: ∀m,n NatNum(m) ∧ NatNum(n) ⇒ +(S(m),n) = S(+(m,n))

**Set Theory Axioms:**
- ∀s Set(s) ⇔ (s = {}) ∨ (∃x,s₂ Set(s₂) ∧ s = Add(x,s₂))
- ¬∃x,s Add(x,s) = {}
- ∀x,s x∈s ⇔ s = Add(x,s)
- ∀x,s x∈s ⇔ ∃y,s₂ (s = Add(y,s₂) ∧ (x = y ∨ x ∈ s₂))
- ∀s₁,s₂ s₁ ⊆ s₂ ⇔ (∀x x∈s₁ ⇒ x∈s₂)
- ∀s₁,s₂ (s₁ = s₂) ⇔ (s₁ ⊆ s₂ ∧ s₂ ⊆ s₁)
- ∀x,s₁,s₂ x∈(s₁∩s₂) ⇔ (x∈s₁ ∧ x∈s₂)
- ∀x,s₁,s₂ x∈(s₁∪s₂) ⇔ (x∈s₁ ∨ x∈s₂)

**Wumpus World (FOL):**
- Percept handling: ∀t,s,g,w,c Percept([s,Breeze,g,w,c],t) ⇒ Breeze(t)
- Adjacent: ∀x,y,a,b Adjacent([x,y],[a,b]) ⇔ (x=a ∧ (y=b-1 ∨ y=b+1)) ∨ (y=b ∧ (x=a-1 ∨ x=a+1))
- Breezy: ∀s Breezy(s) ⇔ ∃r Adjacent(r,s) ∧ Pit(r)
- HaveArrow successor: ∀t HaveArrow(t+1) ⇔ (HaveArrow(t) ∧ ¬Action(Shoot,t))

### 6. KNOWLEDGE ENGINEERING PROCESS (7 Steps)

1. **Identify the questions** — Determine range of queries (PEAS-like)
2. **Assemble relevant knowledge** — Knowledge acquisition from experts
3. **Decide on vocabulary** — Choose predicates, functions, constants (the ontology)
4. **Encode general knowledge** — Write axioms for all vocabulary terms
5. **Encode problem instance** — Simple atomic sentences (from sensors or input)
6. **Pose queries** — Use inference to derive answers
7. **Debug and evaluate** — Missing axioms, false statements, test suite

### 7. KEY PEOPLE (Chapter 8)

- **Gottlob Frege (1879)** — Begriffschrift, introduced quantifiers, first FOL
- **Charles Sanders Peirce (1870, 1883)** — Logic of relations, independent development of FOL
- **Giuseppe Peano (1889)** — Present notation for FOL
- **Augustus De Morgan (1864)** — First systematic treatment of relations
- **Leopold Löwenheim (1915)** — Systematic model theory, equality symbol
- **Thoralf Skolem (1920)** — Extended Löwenheim's results
- **Alfred Tarski (1935)** — Definition of truth and model-theoretic satisfaction
- **John McCarthy (1958)** — Introduced FOL for building AI systems
- **John Alan Robinson (1965)** — Resolution, complete first-order inference
- **Sapir–Whorf hypothesis** — Language influences thought
- **Whorf (1956)** — Claimed understanding influenced by language

---

## CHAPTER 9: INFERENCE IN FIRST-ORDER LOGIC
*Lines 12400-13809*

---

### 1. NAMED ENTITIES & DEFINITIONS

| Term | Definition |
|------|------------|
| **Universal Instantiation (UI)** | From ∀v α, infer SUBST({v/g}, α) for any ground term g. |
| **Existential Instantiation (EI)** | From ∃v α, infer SUBST({v/k}, α) where k is a new constant symbol not appearing elsewhere. |
| **Skolem constant** | A new constant symbol introduced by Existential Instantiation to name an existentially quantified object. |
| **Propositionalization** | Converting FOL KB to propositional logic by instantiating all quantified sentences. |
| **Generalized Modus Ponens (GMP)** | Lifted Modus Ponens: from p₁',...,pₙ' and (p₁∧...∧pₙ ⇒ q) where SUBST(θ,pᵢ') = SUBST(θ,pᵢ), infer SUBST(θ,q). |
| **Lifting** | Raising inference rules from ground propositional to FOL using unification. |
| **Unification** | Finding a substitution θ that makes two logical expressions identical: UNIFY(p,q) = θ where SUBST(θ,p) = SUBST(θ,q). |
| **Unifier** | The substitution returned by UNIFY. |
| **Most General Unifier (MGU)** | The unifier that places fewest restrictions on variables; unique up to renaming. |
| **Standardizing apart** | Renaming variables to avoid name clashes before unification. |
| **Occur check** | Check whether a variable occurs inside a term before unifying; prevents infinite recursion (e.g., S(x) with S(S(x))). |
| **Subsumption lattice** | A lattice organizing all possible queries that unify with a fact. |
| **Datalog** | First-order definite clauses with no function symbols. |
| **Renaming** | A sentence identical to another except for variable names. |
| **Fixed point** | State where no new inferences can be added. |
| **Conjunct ordering** | Finding optimal order to solve conjuncts in a rule premise (NP-hard in general). |
| **Data complexity** | Complexity of inference as function of number of ground facts (holding rule size constant). |
| **Rete algorithm** | Efficient forward-chaining algorithm using a dataflow network; preprocesses rules. |
| **Production system** | Condition-action rule system; forward-chaining with working memory. |
| **Cognitive architecture** | Model of human reasoning (ACT, SOAR). |
| **Deductive databases** | Large-scale databases using forward chaining like relational databases with inference. |
| **Magic set** | Technique rewriting rule sets using goal information so only relevant bindings considered. |
| **Logic programming** | Declarative systems built by expressing knowledge in formal language; Algorithm = Logic + Control (Kowalski). |
| **Prolog** | Most widely used logic programming language. Uppercase = variables, lowercase = constants. C :- A, B means A∧B⇒C. |
| **Tabled logic programming** | Backward chaining with memoization; combines goal-directedness of backward chaining with dynamic-programming efficiency. |
| **Completion** | Expressing database semantics in FOL: Course(d,n) ⇔ (d=CS∧n=101) ∨ ... (exactly the courses known). |
| **Constraint logic programming (CLP)** | Allows variables to be constrained rather than bound; returns most specific set of constraints. |
| **Metarule** | Rule that determines which conjuncts to try first. |
| **Resolution** | Complete inference procedure for any FOL knowledge base (not just definite clauses). Works by refutation: prove KB∧¬α is unsatisfiable. |
| **Binary resolution** | Resolves exactly two complementary literals after unification. |
| **Factoring** | Removing redundant literals by unification; combination with binary resolution is complete. |
| **Refutation completeness** | If a set of sentences is unsatisfiable, resolution will derive a contradiction. |
| **Skolem function** | Function introduced during Skolemization whose arguments are all universally quantified variables in scope. |
| **Skolemization** | Removing existential quantifiers by replacing with Skolem functions/constants. |
| **Herbrand universe** | Set of all ground terms constructible from function symbols and constant symbols in S. |
| **Saturation** | Set of all ground clauses from applying substitutions from ground terms to variables. |
| **Herbrand base** | Saturation of S w.r.t. its Herbrand universe. |
| **Herbrand's theorem** | If S is unsatisfiable, there exists a finite subset of its Herbrand base that is also unsatisfiable. |
| **Lifting lemma** | If ground instance resolutions exist, corresponding FOL resolutions exist. |
| **Demodulation** | Equality inference: from x=y and clause α containing term x, substitute y for x in α (directional: x→y). |
| **Paramodulation** | Equality inference for non-unit clauses: resolve with equality literal then substitute. |
| **Equational unification** | Extends unification to allow equality reasoning (commutativity, associativity, etc.). |
| **Unit preference** | Prefer resolutions involving a unit clause (single literal). |
| **Set of support** | Every resolution step must involve at least one clause from a special set (e.g., negated query). |
| **Input resolution** | Every resolution combines one input sentence with another. |
| **Linear resolution** | Resolution where resolved clauses are either original or ancestors. |
| **Subsumption** | Eliminate sentences more specific than existing ones (e.g., don't add P(A) if P(x) exists). |
| **Nonconstructive proof** | Resolution proves existential goal without unique binding for variable. |

### 2. SUBSTITUTION NOTATION

SUBST(θ, α) = result of applying substitution θ to sentence α.
- θ = {v/g} means replace variable v with ground term g
- Example: SUBST({x/John}, King(x) ⇒ Person(x)) = King(John) ⇒ Person(John)

### 3. UNIFICATION ALGORITHM

```
function UNIFY(x, y, θ=empty) returns a substitution or failure
    if θ = failure then return failure
    else if x = y then return θ
    else if VARIABLE?(x) then return UNIFY-VAR(x, y, θ)
    else if VARIABLE?(y) then return UNIFY-VAR(y, x, θ)
    else if COMPOUND?(x) and COMPOUND?(y) then
        return UNIFY(ARGS(x), ARGS(y), UNIFY(OP(x), OP(y), θ))
    else if LIST?(x) and LIST?(y) then
        return UNIFY(REST(x), REST(y), UNIFY(FIRST(x), FIRST(y), θ))
    else return failure

function UNIFY-VAR(var, x, θ) returns a substitution
    if {var/val} ∈ θ for some val then return UNIFY(val, x, θ)
    else if {x/val} ∈ θ for some val then return UNIFY(var, val, θ)
    else if OCCUR-CHECK?(var, x) then return failure
    else return add {var/x} to θ
```

### 4. GENERALIZED MODUS PONENS

```
p₁', p₂', ..., pₙ',  (p₁ ∧ p₂ ∧ ... ∧ pₙ ⇒ q)
────────────────────────────────────────────
                SUBST(θ, q)
```
where SUBST(θ, pᵢ') = SUBST(θ, pᵢ) for all i.

Sound because: (1) p |= SUBST(θ,p) by UI; (2) from p₁'...pₙ' infer SUBST(θ,p₁')∧...∧SUBST(θ,pₙ'); (3) from implication infer SUBST(θ,p₁)∧...∧SUBST(θ,pₙ) ⇒ SUBST(θ,q); (4) by condition, these match, so by Modus Ponens, SUBST(θ,q) follows.

### 5. UNIFICATION EXAMPLES

| Expression 1 | Expression 2 | Result |
|-------------|-------------|--------|
| Knows(John, x) | Knows(John, Jane) | {x/Jane} |
| Knows(John, x) | Knows(y, Bill) | {x/Bill, y/John} |
| Knows(John, x) | Knows(y, Mother(y)) | {y/John, x/Mother(John)} |
| Knows(John, x) | Knows(x, Elizabeth) | FAILURE (x can't be both John and Elizabeth) |
| Knows(John, x) | Knows(x₁₇, Elizabeth) | {x/Elizabeth, x₁₇/John} (after standardizing apart) |
| Knows(John, x) | Knows(y, z) | {y/John, x/z} (MGU) |

### 6. FORWARD CHAINING (FOL-FC-ASK)

```
function FOL-FC-ASK(KB, α) returns a substitution or false
    inputs: KB (definite clauses), α (atomic sentence query)
    
    while true do
        new ← {}
        for each rule in KB do
            (p₁∧...∧pₙ ⇒ q) ← STANDARDIZE-VARIABLES(rule)
            for each θ such that SUBST(θ, p₁∧...∧pₙ) = SUBST(θ, p₁'∧...∧pₙ')
                for some p₁',...,pₙ' in KB
                q' ← SUBST(θ, q)
                if q' does not unify with any sentence in KB or new then
                    add q' to new
                    φ ← UNIFY(q', α)
                    if φ is not failure then return φ
        if new = {} then return false
        add new to KB
```

**Properties:**
- Sound (GMP is sound)
- Complete for definite clause KBs
- For Datalog: terminates in ≤ p·n^k iterations (p predicates, n constants, k max arity)
- For general definite clauses with functions: semidecidable (may loop infinitely, e.g., Peano axioms generating NatNum(S(0)), NatNum(S(S(0))), ...)

### 7. BACKWARD CHAINING (FOL-BC-ASK)

```
function FOL-BC-ASK(KB, query) returns a generator of substitutions
    return FOL-BC-OR(KB, query, {})

function FOL-BC-OR(KB, goal, θ) returns a substitution
    for each rule in FETCH-RULES-FOR-GOAL(KB, goal) do
        (lhs ⇒ rhs) ← STANDARDIZE-VARIABLES(rule)
        for each θ' in FOL-BC-AND(KB, lhs, UNIFY(rhs, goal, θ)) do
            yield θ'

function FOL-BC-AND(KB, goals, θ) returns a substitution
    if θ = failure then return
    else if LENGTH(goals) = 0 then yield θ
    else
        first, rest ← FIRST(goals), REST(goals)
        for each θ' in FOL-BC-OR(KB, SUBST(θ, first), θ) do
            for each θ'' in FOL-BC-AND(KB, rest, θ') do
                yield θ''
```

**Properties:**
- Depth-first search → linear space
- Suffers from repeated states and incompleteness
- AND/OR search: OR because goal proved by any rule; AND because all conjuncts must be proved

### 8. CRIME EXAMPLE (Definite Clauses)

```
American(x) ∧ Weapon(y) ∧ Sells(x,y,z) ∧ Hostile(z) ⇒ Criminal(x)
Owns(Nono, M1)
Missile(M1)
Missile(x) ∧ Owns(Nono, x) ⇒ Sells(West, x, Nono)
Missile(x) ⇒ Weapon(x)
Enemy(x, America) ⇒ Hostile(x)
American(West)
Enemy(Nono, America)
```

### 9. CONVERSION TO CNF (Algorithm)

1. **Eliminate implications**: P⇒Q → ¬P∨Q
2. **Move ¬ inwards**: ¬∀x P → ∃x ¬P; ¬∃x P → ∀x ¬P
3. **Standardize variables**: rename duplicate variables
4. **Skolemize**: replace ∃x P with P(A) (constant) or P(F(x₁,...,xₙ)) (Skolem function)
5. **Drop universal quantifiers**: all remaining variables are universally quantified
6. **Distribute ∨ over ∧**: convert to conjunction of clauses

### 10. RESOLUTION RULE

```
ℓ₁ ∨ ... ∨ ℓₖ,   m₁ ∨ ... ∨ mₙ
──────────────────────────────────
SUBST(θ, ℓ₁∨...∨ℓᵢ₋₁∨ℓᵢ₊₁∨...∨ℓₖ ∨ m₁∨...∨mⱼ₋₁∨mⱼ₊₁∨...∨mₙ)
```
where UNIFY(ℓᵢ, ¬mⱼ) = θ.

**Completeness proof structure:**
1. If S unsatisfiable → finite subset of Herbrand base is unsatisfiable (Herbrand's theorem)
2. Propositional resolution complete for ground sentences (ground resolution theorem)
3. Lifting lemma: ground proof → corresponding first-order proof

### 11. EQUALITY AXIOMS

```
∀x x = x                              (reflexivity)
∀x,y x = y ⇒ y = x                    (symmetry)
∀x,y,z x = y ∧ y = z ⇒ x = z         (transitivity)
∀x,y x = y ⇒ (P₁(x) ⇔ P₁(y))         (substitution for each predicate)
∀w,x,y,z w = y ∧ x = z ⇒ (F₁(w,x) = F₁(y,z))  (substitution for each function)
```

**Demodulation rule:**
```
x = y,   m₁ ∨ ... ∨ mₙ
────────────────────────
SUB(SUBST(θ,x), SUBST(θ,y), m₁ ∨ ... ∨ mₙ)
```
where UNIFY(x, z) = θ and z appears somewhere in some mᵢ.

**Paramodulation rule:**
```
ℓ₁ ∨ ... ∨ ℓₖ ∨ x = y,   m₁ ∨ ... ∨ mₙ
──────────────────────────────────────────
SUB(SUBST(θ,x), SUBST(θ,y), SUBST(θ, ℓ₁∨...∨ℓₖ ∨ m₁∨...∨mₙ))
```

### 12. RESOLUTION STRATEGIES

| Strategy | Description | Completeness |
|----------|-------------|-------------|
| Unit preference | Prefer resolution with unit clause | Complete for Horn; incomplete general |
| Set of support | Every step involves set-of-support clause | Complete if remainder is satisfiable |
| Input resolution | Always combine with input sentence | Complete for Horn; incomplete general |
| Linear resolution | Resolve with original or ancestor | Complete |
| Subsumption | Eliminate redundant sentences | Preserves completeness |

### 13. COMPARISON: FORWARD vs BACKWARD CHAINING

| Aspect | Forward Chaining | Backward Chaining |
|--------|-----------------|-------------------|
| Direction | Data-driven (facts → conclusions) | Goal-driven (query → facts) |
| Search | Breadth-first, complete | Depth-first, potentially incomplete |
| Space | Generates all consequences | Only explores relevant paths |
| Redundancy | May generate irrelevant facts | May get infinite loops |
| Efficiency | Good for many rules, few facts | Good for many facts, few rules |
| Uses | Deductive databases, production systems | Logic programming (Prolog) |

### 14. PROLOG FEATURES VS STANDARD LOGIC

- Uses database semantics (UNA + CWA), not standard FOL
- Built-in arithmetic (X is 4+3 succeeds; 5 is X+Y fails)
- Side-effect predicates (assert/retract) — no logical counterpart
- Occurs check omitted (unsound but rarely problematic)
- Depth-first search with no infinite recursion check
- Negation as failure: if goal can't be proved, it's false

### 15. KEY PEOPLE (Chapter 9)

- **Jacques Herbrand (1930)** — Herbrand's theorem, Herbrand universe, unification
- **Alan Turing (1936)** — Undecidability of first-order validity
- **Alonzo Church (1936)** — Undecidability of first-order validity
- **Kurt Gödel (1930, 1931)** — Complete proof procedure for FOL; Incompleteness Theorem
- **John Alan Robinson (1965)** — Resolution
- **Robert Kowalski** — Algorithm = Logic + Control; logic programming foundations
- **Alain Colmerauer (1972)** — Prolog developer
- **David H.D. Warren** — Warren Abstract Machine (WAM)
- **Cordell Green (1969)** — First question-answering FOL system (QA3)
- **Charles Forgy (1982)** — Rete algorithm
- **John McCarthy (1980)** — Circumscription
- **Raymond Reiter (1980)** — Default logic

### 16. GÖDEL'S INCOMPLETENESS THEOREM

- For any consistent, recursively enumerable set A of true arithmetic sentences, there exist true sentences not provable from A.
- Proof: construct sentence σ that states its own unprovability from A. If σ provable → false (contradiction). So σ is unprovable, hence true.
- Implication: We can never prove all theorems of mathematics within any fixed system of axioms.
- Debate about significance for AI (taken up in Chapter 27).

### 17. INFERENCE COMPLEXITY TABLE

| Knowledge Base Type | Entailment Problem | Decidable? |
|--------------------|-------------------|-----------|
| Propositional logic | SAT | Decidable (NP-complete) |
| FOL (general) | Validity | Semidecidable |
| Datalog (function-free definite clauses) | Entailment | Decidable (polynomial) |
| Definite clauses with functions | Entailment | Semidecidable |

---

## CHAPTER 10: KNOWLEDGE REPRESENTATION
*Lines 13810-15084*

---

### 1. NAMED ENTITIES & DEFINITIONS

| Term | Definition |
|------|------------|
| **Ontological engineering** | Creating representations for general concepts like Events, Time, Physical Objects, Beliefs. |
| **Upper ontology** | General framework of concepts at the "top" of the hierarchy (e.g., Anything → AbstractObjects, PhysicalObjects, etc.). |
| **Category** | Organization of objects into classes. Reasoning occurs at category level. |
| **Reification** | Turning a proposition into an object (from Latin *res* = thing). |
| **Subcategory / Subclass / Subset** | A category contained within another (Basketballs ⊂ Balls). |
| **Inheritance** | Properties of a superclass are inherited by all members of subclasses. |
| **Taxonomic hierarchy / Taxonomy** | Subclass relations organizing categories. |
| **Disjoint** | Categories with no members in common. |
| **Exhaustive decomposition** | A set of subcategories that covers all members of a parent category. |
| **Partition** | Disjoint + Exhaustive decomposition. |
| **PartOf** | Transitive, reflexive relation: one object is part of another. |
| **Composite object** | An object characterized by structural relations among parts. |
| **Bunch** | A composite object consisting of parts (not elements); has weight, unlike sets. BunchOf({Apple₁, Apple₂, Apple₃}). |
| **Logical minimization** | Defining an object as the smallest one satisfying certain conditions. |
| **Measure** | Values assigned to properties like height, mass, cost. Abstract measure objects. |
| **Units function** | Function like Inches(1.5), Centimeters(3.81). |
| **Qualitative physics** | AI subfield reasoning about physical systems without detailed equations. |
| **Individuation** | Division into distinct objects. Some stuff defies individuation. |
| **Stuff** | Substances like butter, water, energy — no obvious individuation. |
| **Count noun** | Things that can be counted (aardvarks, holes, theorems). |
| **Mass noun** | Substances without countable units (butter, water, energy). |
| **Intrinsic properties** | Belong to substance itself (density, boiling point, color) — retained under subdivision. |
| **Extrinsic properties** | Depend on object as whole (weight, length, shape) — not retained under subdivision. |
| **Event calculus** | Formal representation of events, fluents, and time points. |
| **Fluent** | An aspect of the world that changes over time; reified as an object. |
| **Modal logic** | Logic with modal operators (K for knowledge, □ for necessity, ◇ for possibility). |
| **Modal operators** | Operators taking sentences as arguments: K_A P (agent A knows P). |
| **Possible world** | A complete consistent state of affairs; models in modal logic are collections of possible worlds. |
| **Accessibility relation** | Links worlds w.r.t. a modal operator; w₁ accessible from w₀ if all in w₁ consistent with A's knowledge in w₀. |
| **Knowledge atom** | K_A P is true in w if P true in every world accessible from w. |
| **Referential transparency** | Meaning depends on object referred to, not term used. Normal in FOL. |
| **Referential opacity** | Terms matter because not all agents know which terms are co-referential. Needed for knowledge/belief. |
| **Logical omniscience** | If agent knows axioms, it knows all consequences. Problematic property of modal logic. |
| **Linear temporal logic** | Adds modal operators: □X (next), □F (finally/eventually), □G (globally/always), □U (until). |
| **Semantic networks** | Graphical notation with nodes (objects/categories) and labeled links (relations). |
| **Description logics** | Formal language for constructing and combining category definitions; emphasis on tractable subsumption. |
| **Existential graphs** | Peirce's graphical notation of nodes and edges; "logic of the future." |
| **Procedural attachment** | Technique where query about a relation calls a special procedure instead of general inference. |
| **Default value** | Assumed property unless contradicted by more specific information (e.g., persons have 2 legs). |
| **Overriding** | More specific information overrides default value. |
| **Multiple inheritance** | Object belongs to multiple categories; can lead to conflicting property values. |
| **Subsumption (description logic)** | Checking if one category is a subset of another by comparing definitions. |
| **Classification (description logic)** | Checking if an object belongs to a category. |
| **Monotonicity** | If KB ⊨ α then KB ∧ β ⊨ α (entailed sentences remain entailed after adding new sentences). |
| **Nonmonotonicity** | Beliefs do not grow monotonically; new evidence can retract conclusions. |
| **Nonmonotonic logic** | Logic with modified notions of truth and entailment to capture default reasoning. |
| **Circumscription** | Assume specified predicates are false for all objects except those known to be true. Model preference: fewer abnormal objects = preferred. |
| **Model preference logic** | Sentence entailed if true in all *preferred* models (not all models). |
| **Prioritized circumscription** | Give some abnormality predicates higher priority than others for minimization. |
| **Default logic** | Default rules of form P:J₁,...,Jₙ / C (if P true and Jᵢ consistent with KB, conclude C). |
| **Default rule** | P:J₁,...,Jₙ / C where P = prerequisite, C = conclusion, Jᵢ = justifications. |
| **Extension (default logic)** | Maximal set of consequences of a default theory. |
| **Belief revision** | Process of retracting incorrect inferences when new information arrives. |
| **Belief update** | Revising KB to reflect change in the world (vs. new info about fixed world). |
| **Truth maintenance system (TMS)** | System handling retraction of inferences, maintaining consistency. |
| **Justification-based TMS (JTMS)** | Each sentence annotated with justifications; retraction cascades based on justification dependencies. |
| **Justification** | Set of sentences from which a sentence was inferred. |
| **Assumption-based TMS (ATMS)** | Represents all hypothetical states simultaneously; each sentence has label of assumption sets. |
| **Explanation** | Set of sentences E such that E ⊨ P (can include assumptions). |
| **Assumption** | Sentence not known true, but would suffice to prove P if true. |

### 2. UPPER ONTOLOGY HIERARCHY

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
│       └── Stuff
│           ├── Times
│           ├── Weights
│           ├── Animals
│           ├── Agents
│           ├── Solid
│           ├── Liquid
│           └── Gas
└── GeneralizedEvents
```

### 3. EVENT CALCULUS PREDICATES

| Predicate | Meaning |
|-----------|---------|
| T(f, t₁, t₂) | Fluent f is true for all times between t₁ and t₂ |
| Happens(e, t₁, t₂) | Event e starts at t₁ and ends at t₂ |
| Initiates(e, f, t) | Event e causes fluent f to become true at time t |
| Terminates(e, f, t) | Event e causes fluent f to cease to be true at time t |
| Initiated(f, t₁, t₂) | Fluent f became true at some point between t₁ and t₂ |
| Terminated(f, t₁, t₂) | Fluent f ceased to be true at some point between t₁ and t₂ |
| t₁ < t₂ | Time point t₁ occurs before time t₂ |

**Event calculus axioms:**
```
Happens(e, t₁, t₃) ∧ Initiates(e, f, t₂) ∧ ¬Terminated(f, t₂, t₄) ∧ t₁ ≤ t₂ ≤ t₃ ≤ t₄ ⇒ T(f, t₂, t₄)
Happens(e, t₁, t₃) ∧ Terminates(e, f, t₂) ∧ ¬Initiated(f, t₂, t₄) ∧ t₁ ≤ t₂ ≤ t₃ ≤ t₄ ⇒ ¬T(f, t₂, t₄)
```

### 4. TIME INTERVAL RELATIONS (Allen, 1983)

| Relation | Definition |
|----------|-----------|
| Meet(i, j) | End(i) = Begin(j) |
| Before(i, j) | End(i) < Begin(j) |
| After(j, i) | Before(i, j) |
| During(i, j) | Begin(j) < Begin(i) < End(i) < End(j) |
| Overlap(i, j) | Begin(i) < Begin(j) < End(i) < End(j) |
| Starts(i, j) | Begin(i) = Begin(j) |
| Finishes(i, j) | End(i) = End(j) |
| Equals(i, j) | Begin(i) = Begin(j) ∧ End(i) = End(j) |

### 5. MODAL KNOWLEDGE AXIOMS

| Axiom | Meaning |
|-------|---------|
| (K_A P ∧ K_A(P ⇒ Q)) ⇒ K_A Q | Agents draw conclusions |
| K_A(P ∨ ¬P) | Tautology (every agent knows law of excluded middle) |
| (K_A P) ∨ (K_A ¬P) | NOT a tautology (agents often don't know) |
| K_A P ⇒ P | Knowledge implies truth (Plato: justified true belief) |
| K_A P ⇒ K_A(K_A P) | Positive introspection |

### 6. NATURAL KINDS VS DEFINED CATEGORIES

**Defined categories:** Strict definitions possible (triangle = polygon with three sides).

**Natural kinds:** No clear-cut definition (tomatoes, games). Use Typical(c) function:
- Typical(c) ⊆ c
- x ∈ Typical(Tomatoes) ⇒ Red(x) ∧ Round(x)
- Wittgenstein (1953): "family resemblances" not necessary/sufficient characteristics
- Quine (1953): even "bachelor" definition is suspect ("Pope is a bachelor" infelicitous)

### 7. SEMANTIC NETWORK vs DESCRIPTION LOGIC

| Aspect | Semantic Networks | Description Logics |
|--------|------------------|-------------------|
| Focus | Graphical visualization, efficient inheritance | Formal definitions, tractable subsumption |
| Expressiveness | Limited (binary relations, defaults) | Limited (no full negation/disjunction) |
| Inference | Inheritance reasoning | Subsumption, classification, consistency |
| Tractability | Simple, transparent | Designed for polynomial-time |
| Issues | Ambiguous semantics (IS-A links) | Limited constructs |

### 8. CLASSIC Description Logic Syntax

```
Concept → Thing | ConceptName
         | And(Concept, ...)
         | All(RoleName, Concept)
         | AtLeast(Integer, RoleName)
         | AtMost(Integer, RoleName)
         | Fills(RoleName, IndividualName, ...)
         | SameAs(Path, Path)
         | OneOf(IndividualName, ...)
Path → [RoleName, ...]
```

Example: `Bachelor = And(Unmarried, Adult, Male)`

### 9. NONMONOTONIC LOGICS COMPARISON

| Logic | Mechanism | Multiple extensions? |
|-------|-----------|---------------------|
| **Circumscription** | Minimize abnormal predicates; prefer models with fewer abnormal objects | Single minimal model (or multiple if tied) |
| **Prioritized circumscription** | Give precedence to certain predicates | Single |
| **Default logic** | Default rules: P:J₁,...,Jₙ / C | Yes (e.g., Nixon diamond) |
| **Closed-world assumption** | Assume false if not provable | Single |

**Nixon Diamond Example:**
- Nixon is both Quaker and Republican
- Default: Quakers are pacifists
- Default: Republicans are not pacifists
- Result: Two extensions (pacifist or not) — properly agnostic

### 10. TRUTH MAINTENANCE SYSTEMS COMPARISON

| Aspect | Simple (Retract & Reassert) | JTMS | ATMS |
|--------|---------------------------|------|------|
| Mechanism | Number sentences, undo to point | Annotate with justifications | Track assumption sets per sentence |
| Retraction cost | O(n) sentences to redo | O(# derived from P) | Fast context switching |
| State representation | One at a time | One at a time (in/out) | All states simultaneously |
| Use case | Simple databases | Interactive reasoning | Hypothetical reasoning |

### 11. SEVEN KNOWLEDGE ENGINEERING STEPS (same as Ch8)

(See Chapter 8 §6 above)

### 12. KEY PEOPLE (Chapter 10)

- **Aristotle (384-322 BCE)** — Categories, genus/species, Metaphysics
- **Charles S. Peirce (1909)** — Existential graphs
- **Ross Quillian (1961)** — First AI semantic networks
- **Marvin Minsky (1975)** — Frames
- **Bill Woods (1975)** — "What's In a Link?" (semantic network semantics)
- **Ron Brachman (1979)** — Precise semantics for KR formalisms
- **Patrick Hayes (1979, 1985)** — "Logic of Frames"; Naive Physics
- **Drew McDermott (1978, 1987)** — "Tarskian Semantics"; critique of pure reason
- **Robert Kowalski & Marek Sergot (1986)** — Event calculus
- **James Allen (1983, 1984)** — Time intervals
- **John McCarthy (1980)** — Circumscription
- **Raymond Reiter (1980)** — Default logic
- **Jon Doyle (1979)** — TMS
- **Lenat & Guha (1990)** — CYC project
- **Wittgenstein (1953)** — Family resemblances, natural kinds
- **Quine (1953)** — Critique of strict definitions
- **Tom Gruber (2004)** — "Every ontology is a treaty"

---

## CHAPTER 11: AUTOMATED PLANNING
*Lines 15085-16855*

---

### 1. NAMED ENTITIES & DEFINITIONS

| Term | Definition |
|------|------------|
| **Classical planning** | Finding sequence of actions to accomplish goal in discrete, deterministic, static, fully observable environment. |
| **PDDL (Planning Domain Definition Language)** | Family of languages for factored representation in planning. |
| **State** | Conjunction of ground atomic fluents (closed-world: unmentioned are false; unique names assumption). |
| **Action schema** | Template for a family of ground actions; has name, variables, precondition, effect. |
| **Precondition** | Conjunction of literals that must be true for action to be applicable. |
| **Effect** | Conjunction of literals (positive and negative) describing action's result. |
| **Applicable action** | Ground action a is applicable in state s if s ⊨ Precond(a). |
| **RESULT(s, a)** | (s - DEL(a)) ∪ ADD(a). |
| **Delete list (DEL(a))** | Negative literals in action's effects (removed from state). |
| **Add list (ADD(a))** | Positive literals in action's effects (added to state). |
| **Planning domain** | Set of action schemas. |
| **Initial state** | Conjunction of ground fluents (closed-world). |
| **Goal** | Conjunction of literals (may contain variables). |
| **Datalog knowledge base** | FOL definite clauses with no function symbols. |
| **Regression search** | Backward search from goal to initial state using relevant actions. |
| **Relevant action** | Action with effect that unifies with goal literal but no effect negates any part of goal. |
| **Regression formulas:** | POS(g') = (POS(g) - ADD(a)) ∪ POS(Precond(a)); NEG(g') = (NEG(g) - DEL(a)) ∪ NEG(Precond(a)). |
| **SATPLAN** | Translates PDDL to propositional SAT: propositionalize actions + exclusion axioms + precondition axioms + initial state + goal + successor-state axioms. |
| **Planning graph** | Specialized data structure encoding constraints on actions, preconditions, effects, and mutual exclusions. |
| **Situation calculus** | FOL approach using successor-state axioms. |
| **Partial-order planning** | Plan represented as graph (actions = nodes, edges = ordering constraints). |
| **Ignore-preconditions heuristic** | Drops all preconditions from actions. |
| **Ignore-delete-lists heuristic** | Removes all negative literals from effects (monotonic progress). |
| **Set-cover problem** | Minimum number of actions whose effects satisfy goal (NP-hard). |
| **Symmetry reduction** | Prune all but one symmetric branch of search tree. |
| **Preferred action** | Action that is a step of, or achieves precondition of, a relaxed plan. |
| **Serializable subgoals** | Subgoals can be achieved in order without undoing previous ones. |
| **State abstraction** | Many-to-one mapping from ground states to abstract representation (e.g., ignore some fluents). |
| **Decomposition** | Dividing problem into parts, solving independently, combining. |
| **Subgoal independence assumption** | Cost of conjunction ≈ sum of costs of each subgoal independently. |
| **Hierarchical decomposition** | Managing complexity through levels of abstraction. |
| **Hierarchical Task Network (HTN) planning** | Planning with high-level actions (HLAs) that have refinements into lower-level actions. |
| **Primitive action** | Standard precondition-effect action (lowest level). |
| **High-level action (HLA)** | Action with one or more possible refinements into sequences of (possibly high-level) actions. |
| **Refinement** | A sequence of actions implementing an HLA. |
| **Implementation (of HLA)** | A refinement containing only primitive actions. |
| **Downward refinement property** | Every high-level plan that claims to achieve goal has at least one implementation that does. |
| **Demonic nondeterminism** | Adversary chooses implementation (must work for all). |
| **Angelic nondeterminism** | Agent chooses implementation (must work for at least one). |
| **Angelic semantics** | Reachable set = union of states reachable by any implementation. Plan achieves goal if reachable set intersects goal set. |
| **Reachable set** | REACH(s, h) = set of states reachable by any implementation of HLA h from state s. |
| **Optimistic description** | REACH⁺(s, h) — may overstate reachable set. |
| **Pessimistic description** | REACH⁻(s, h) — may understate reachable set. |
| **Percept schema** | PDDL extension: Percept(p, PRECOND: c) — describes sensor model. |
| **Conditional effect** | "when condition : effect" — action effect depends on state. |
| **Conformant planning** | Sensorless planning — no percepts; agent acts without knowing exact state. |
| **Contingent planning** | Conditional branching based on percepts. |
| **Action monitoring** | Before executing action, verify all preconditions still hold. |
| **Plan monitoring** | Before executing action, verify remaining plan will succeed. |
| **Goal monitoring** | Before executing action, check if better goals exist. |
| **Execution monitoring** | Determining when replanning is needed during execution. |
| **Replanning** | Generating new plan when current plan fails due to unexpected events. |
| **Missing precondition** | Action model lacks a necessary precondition. |
| **Missing effect** | Action model lacks an effect. |
| **Missing fluent** | Fluent absent from representation. |
| **Exogenous event** | Event outside agent's control affecting the world. |
| **Scheduling** | Determining when actions occur (adding temporal info). |
| **Resource constraint** | Limited resources (staff, money, materials, time). |
| **Job-shop scheduling problem** | Set of jobs with ordered actions; each action has duration and resource requirements. |
| **Duration** | Time an action takes. |
| **Consumable resource** | Used up by action (e.g., bolts). |
| **Reusable resource** | Occupied during action but available after (e.g., pilot). |
| **Makespan** | Total duration of the plan (solution cost). |
| **Critical path method (CPM)** | Find earliest/latest start times for actions given ordering constraints. |
| **Critical path** | Path with longest total duration; determines plan duration. |
| **Slack** | LS - ES (latest start - earliest start). |
| **Schedule** | ES and LS times for all actions. |
| **Minimum slack heuristic** | Greedy scheduling: pick action with least slack whose predecessors are scheduled. |
| **Aggregation** | Grouping identical individual objects into quantities. |
| **Portfolio planning** | Using collection of algorithms; run selectively, in parallel, or interleaved. |

### 2. PDDL ACTION SCHEMA FORMAT

```
Action(ActionName(var₁, ..., varₙ),
    PRECOND: conjunction of literals,
    EFFECT: conjunction of literals)
```

**Variable rule:** Any variable in EFFECT must also appear in PRECOND.

### 3. PDDL EXAMPLE DOMAINS

**Air Cargo Transport:**
```
Action(Load(c, p, a),
    PRECOND: At(c, a) ∧ At(p, a) ∧ Cargo(c) ∧ Plane(p) ∧ Airport(a)
    EFFECT: ¬At(c, a) ∧ In(c, p))

Action(Unload(c, p, a),
    PRECOND: In(c, p) ∧ At(p, a) ∧ Cargo(c) ∧ Plane(p) ∧ Airport(a)
    EFFECT: At(c, a) ∧ ¬In(c, p))

Action(Fly(p, from, to),
    PRECOND: At(p, from) ∧ Plane(p) ∧ Airport(from) ∧ Airport(to)
    EFFECT: ¬At(p, from) ∧ At(p, to))
```

**Blocks World:**
```
Action(Move(b, x, y),
    PRECOND: On(b, x) ∧ Clear(b) ∧ Clear(y) ∧ Block(b) ∧ Block(y)
             ∧ (b≠x) ∧ (b≠y) ∧ (x≠y)
    EFFECT: On(b, y) ∧ Clear(x) ∧ ¬On(b, x) ∧ ¬Clear(y))

Action(MoveToTable(b, x),
    PRECOND: On(b, x) ∧ Clear(b) ∧ Block(b) ∧ Block(x)
    EFFECT: On(b, Table) ∧ Clear(x) ∧ ¬On(b, x))
```

**Spare Tire:**
```
Action(Remove(obj, loc),
    PRECOND: At(obj, loc)
    EFFECT: ¬At(obj, loc) ∧ At(obj, Ground))

Action(PutOn(t, Axle),
    PRECOND: Tire(t) ∧ At(t, Ground) ∧ ¬At(Flat, Axle) ∧ ¬At(Spare, Axle)
    EFFECT: ¬At(t, Ground) ∧ At(t, Axle))

Action(LeaveOvernight,
    PRECOND: (none)
    EFFECT: ¬At(Spare, Ground) ∧ ¬At(Spare, Axle) ∧ ¬At(Spare, Trunk)
            ∧ ¬At(Flat, Ground) ∧ ¬At(Flat, Axle) ∧ ¬At(Flat, Trunk))
```

### 4. FORWARD vs BACKWARD SEARCH IN PLANNING

| Aspect | Forward (Progression) | Backward (Regression) |
|--------|----------------------|----------------------|
| Start | Initial state | Goal |
| Direction | Forward through actions | Backward through relevant actions |
| States | Ground (variable-free) | May contain variables |
| Branching factor | All applicable actions | Only relevant actions (usually smaller) |
| Heuristics | Easier to compute | Harder to compute |
| Dominance | Preferred by most current systems | Lower branching but harder heuristics |

### 5. REGRESSION FORMULAS

Given goal g and action a:
```
POS(g') = (POS(g) - ADD(a)) ∪ POS(Precond(a))
NEG(g') = (NEG(g) - DEL(a)) ∪ NEG(Precond(a))
```

**Relevant action definition:** Action A is relevant toward goal g if:
1. A has effect e'ⱼ where Unify(gᵢ, e'ⱼ) = θ
2. There is no effect in A' = SUBST(θ, A) that negates a literal in g

### 6. SATPLAN TRANSLATION STEPS

1. **Propositionalize actions** — ground all action schemas for each time step t
2. **Action exclusion axioms** — ¬(Actionᵢᵗ ∧ Actionⱼᵗ) for i≠j (no two actions at same time)
3. **Precondition axioms** — Actionᵗ ⇒ PRE(Action)ᵗ
4. **Initial state** — assert F⁰ for each fluent in init; ¬F⁰ for others
5. **Goal** — disjunction over all ground instances
6. **Successor-state axioms** — Fᵗ⁺¹ ⇔ ActionCausesFᵗ ∨ (Fᵗ ∧ ¬ActionCausesNotFᵗ)

### 7. PLANNING APPROACHES COMPARISON

| Approach | Mechanism | Strength | Weakness |
|----------|-----------|----------|----------|
| Forward state-space search | Progress from initial state | Good heuristics possible | Large branching factor |
| Backward regression search | Regress from goal | Lower branching factor | Harder heuristics |
| SATPLAN | Encode as SAT, use SAT solver | Powerful with modern SAT | Large propositional encoding |
| Graphplan | Planning graph | Efficient mutual exclusion | Memory for large problems |
| CSP | Encode as constraint satisfaction | Single Actionᵗ variable | May not scale |
| Partial-order | Search plan space | Human-readable; good for scheduling | Not competitive on classical problems |

### 8. PLANNING HEURISTICS TABLE

| Heuristic | Method | Admissible? | Issues |
|-----------|--------|-------------|--------|
| Ignore-preconditions | Drop all preconditions | Usually not | Too optimistic |
| Ignore-delete-lists | Remove all negative effects | Usually not | NP-hard to compute optimal |
| Set cover | Count min actions covering goal | No (greedy) | NP-hard exact |
| State abstraction | Ignore some fluents | Admissible if abstraction safe | Must choose abstraction wisely |
| Subgoal independence max | maxᵢ COST(Pᵢ) | Admissible | May be too low |
| Subgoal independence sum | Σᵢ COST(Pᵢ) | Admissible only if independent | Often inadmissible |

### 9. HTN PLANNING: KEY FORMULAS

**Refinement tree cost (idealized):**
- d = number of primitive actions
- r = refinements per nonprimitive action
- k = actions at next lower level per refinement
- Number of levels = logₖ d
- Internal refinement nodes = (d-1)/(k-1)
- Total decomposition trees = r^(d-1)/(k-1)

**Key insight:** Small r and large k = huge savings (take k-th root of nonhierarchical cost).

### 10. ANGELIC SEMANTICS FORMULAS

**Reachable set of a plan:**
```
REACH(s, [h₁, h₂]) = ⋃_{s' ∈ REACH(s, h₁)} REACH(s', h₂)
```

**Goal achievement (angelic):** Plan achieves goal if REACH(s, plan) ∩ Goal ≠ ∅

**Approximate descriptions:**
```
REACH⁻(s, h) ⊆ REACH(s, h) ⊆ REACH⁺(s, h)
```

**Decision logic:**
- If REACH⁺(s, plan) ∩ Goal = ∅ → plan DEFINITELY DOESN'T WORK
- If REACH⁻(s, plan) ∩ Goal ≠ ∅ → plan DEFINITELY WORKS
- If REACH⁺ intersects but REACH⁻ doesn't → UNCERTAIN (refine further)

**HLA effect notation:** ⁓A = possibly add A, ⁓⁻A = possibly delete A, ⁓±A = possibly add or delete A.

### 11. BELIEF STATE UPDATE (Sensorless)

```
b' = RESULT(b, a) = (b - DEL(a)) ∪ ADD(a)
```

**Three cases for literal ℓ:**
1. Action adds ℓ → ℓ true in b' regardless
2. Action deletes ℓ → ℓ false in b' regardless
3. Action doesn't affect ℓ → ℓ retains unknown value

**Critical insight:** 1-CNF (conjunction of literals) is closed under updates for actions with unconditional effects. Conditional effects break 1-CNF.

### 12. CONTINGENT vs SENSORLESS vs ONLINE PLANNING

| Aspect | Sensorless (Conformant) | Contingent | Online |
|--------|------------------------|------------|--------|
| Sensors | None | Available during execution | Available during execution |
| Planning | Plan without sensing | Plan with conditional branches | Plan, then execute & replan |
| Belief state | Compact (1-CNF possible) | May need full representation | Maintain during execution |
| Guarantee | Must work for all possible worlds | Branch covers possibilities | May get stuck |
| Example | Paint both pieces with same can | Check colors, branch accordingly | Try paint, replan if fails |

### 13. CRITICAL PATH METHOD (SCHEDULING)

```
ES(Start) = 0
ES(B) = max_{A ≺ B} ES(A) + Duration(A)
LS(Finish) = ES(Finish)
LS(A) = min_{B ≻ A} LS(B) - Duration(A)
```

**Slack:** LS - ES (zero for actions on critical path)
**Complexity:** O(N·b) where N = actions, b = max branching factor

### 14. RESOURCE TYPES

| Type | Behavior | Example |
|------|----------|---------|
| Consumable | Used up entirely | LugNuts, fuel, money |
| Reusable | Occupied then released | EngineHoist, inspector, pilot |

### 15. COMPLEXITY OF PLANNING

| Problem | Complexity |
|---------|-----------|
| PlanSAT (classical) | Decidable (finite state space) |
| PlanSAT (with function symbols) | Semidecidable (infinite state space) |
| Bounded PlanSAT (length ≤ k) | PSPACE-complete (propositionalized) |
| Matching definite clause (NP-hard) | Yes (equivalent to 3-SAT) |

### 16. KEY PEOPLE (Chapter 11)

- **Fikes & Nilsson (1971)** — STRIPS, Shakey robot
- **Sacerdoti (1974, 1975, 1977)** — ABSTRIPS, NOAH, hierarchical planning
- **Sussman (1975)** — HACKER, Sussman anomaly
- **Chapman (1987)** — Formal model of partial-order planning
- **McDermott (1996)** — UNPOP (revived state-space planning)
- **Blum & Furst (1997)** — Graphplan
- **Kautz & Selman (1998)** — SATPLAN, BLACKBOX
- **Bonet & Geffner (1999)** — HSP (Heuristic Search Planner)
- **Hoffmann (2001, 2005)** — FF (Fast Forward) planner
- **Helmert (2006)** — Fast Downward
- **Ghallab et al. (1998)** — PDDL
- **Marthi et al. (2007, 2008)** — Angelic semantics for HLAs
- **Bell & Tate (1985)** — O-PLAN (HTN + scheduling)
- **Muscettola et al. (1998)** — Remote Agent (Deep Space One)
- **Erol, Hendler, Nau (1994, 1996)** — Complete hierarchical decomposition planner

---

## CROSS-CHAPTER DEPENDENCIES

| From | To | Concept |
|------|----|---------|
| Ch 8 (FOL) | Ch 9 (Inference) | Definite clauses, substitutions, FOL syntax all used by inference algorithms |
| Ch 8 (FOL) | Ch 10 (KR) | FOL is representation language for categories, events, time |
| Ch 8 (FOL) | Ch 11 (Planning) | Successor-state axioms (Ch8 wumpus) → planning (Ch11) |
| Ch 7 (Propositional) | Ch 8 (FOL) | Propositional logic is subset of FOL; resolution extended |
| Ch 7 (Propositional) | Ch 9 (Inference) | Propositional forward/backward chaining extended to FOL |
| Ch 7 (Propositional) | Ch 11 (Planning) | SATPLAN propositionalizes planning problems |
| Ch 3 (Search) | Ch 11 (Planning) | State-space search heuristics (A*, hill-climbing) |
| Ch 6 (CSP) | Ch 11 (Planning) | Conjunct ordering = CSP variable ordering; CSP encodings |
| Ch 4 (Beyond Classical) | Ch 11 (Planning) | Sensorless/contingent/online search → planning |
| Ch 9 (Inference) | Ch 10 (KR) | Resolution used in description logic subsumption |
| Ch 9 (Inference) | Ch 10 (KR) | Closed-world assumption (Prolog) → nonmonotonic reasoning |
| Ch 10 (KR) | Ch 11 (Planning) | Event calculus → planning with time and change |
