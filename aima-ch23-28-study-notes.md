# AIMA Chapters 23-28 Comprehensive Study Notes

> Source: Artificial Intelligence: A Modern Approach (Russell & Norvig, 4th ed.)
> Generated from `/content/dars-arshad/Artificial_Intelligence_A_M__zlibrary.sk_lib.sk_zlib.sk_Stuart_Russell_Peter_Norvig.txt`

---

# Chapter 23: Natural Language Processing (Lines 36092-37504)

## 1. Named Entities (Terms & Definitions)

- **Language model**: A probability distribution describing the likelihood of any string of words
- **Bag-of-words model**: Naive Bayes applied to strings; assumes word independence
- **N-gram model**: Markov chain where each word depends only on n-1 previous words
- **Unigram/bigram/trigram**: n-gram with n=1, 2, or 3
- **Tokenization**: Dividing text into a sequence of words
- **Out-of-vocabulary (OOV) word**: A word never seen in training corpus
- **Smoothing**: Reserving probability mass for unseen n-grams to reduce variance
- **Backoff model**: Using (n-1)-grams when n-gram count is low
- **Linear interpolation smoothing**: Combining trigram, bigram, and unigram by weighted sum
- **Corpus**: A body of text used for training
- **Part of speech (POS)**: Lexical category (noun, verb, adjective, etc.)
- **Penn Treebank**: 3M+ word corpus annotated with POS tags and parse trees
- **WordNet**: Hand-curated machine-readable dictionary
- **Syntactic category**: Noun phrase, verb phrase, etc.
- **Phrase structure**: Hierarchical framework for sentence meaning
- **Probabilistic context-free grammar (PCFG)**: Grammar assigning probabilities to strings
- **Chomsky Normal Form**: Grammar format where rules are X→word or X→Y Z
- **Lexicalized PCFG**: PCFG where probabilities depend on head words of phrases
- **Compositional semantics**: Semantics of a phrase = function of semantics of subphrases
- **λ-notation**: Notation for representing predicates (e.g., λx Loves(x,Bo))
- **Quasi-logical form**: Intermediate semantic representation before full logical sentence
- **Indexical**: Phrase referring directly to current situation (I, today, here)
- **Speech act**: Speaker's intent (question, command, promise)
- **Lexical ambiguity**: Word with multiple meanings
- **Syntactic ambiguity**: Phrase with multiple parses
- **Semantic ambiguity**: Ambiguity in meaning
- **Metonymy**: One object standing for another (Chrysler → spokesperson)
- **Metaphor**: Similarity-based figure of speech
- **Disambiguation**: Recovering most probable intended meaning
- **Overgeneration**: Grammar produces ungrammatical sentences
- **Undergeneration**: Grammar rejects valid sentences
- **Dependency grammar**: Syntactic structure via binary relations between lexical items
- **Chart parser**: Parser using dynamic programming to store substring analyses
- **CYK algorithm**: Bottom-up chart parsing algorithm (O(n³m))
- **Deterministic parser**: Beam search parser with b=1
- **Shift-reduce parsing**: Deterministic parsing by shifting/reducing on a stack
- **Head**: The most important word in a phrase
- **Universal grammar**: Chomsky's hypothesized innate grammatical knowledge
- **Curriculum learning**: Training from easy to hard examples
- **Subcategory**: A category augmented with features (e.g., Pronoun with case/person/number)
- **Augmented grammar**: Nonterminals have structured representations with features
- **Open class**: Nouns, verbs, adjectives, adverbs (new words added constantly)
- **Closed class**: Pronouns, articles, prepositions, conjunctions (small, stable sets)
- **Spam detection**: Classifying email as spam/non-spam
- **Sentiment analysis**: Classifying text as positive/negative
- **Author attribution**: Identifying author by style/vocabulary
- **Character-level model**: Probability of each character based on n-1 previous characters
- **Skip-gram model**: Counting words near each other with gaps
- **Laplace (add-one) smoothing**: Adding 1 to all counts
- **Word embedding**: Low-dimensional vector representing a word (Ch. 24)

## 2. Processes / Algorithms / Pathways

### Language Modeling
- N-gram probability: P(wⱼ|w₁:ⱼ₋₁) = P(wⱼ|wⱼ₋ₙ₊₁:ⱼ₋₁)
- Joint probability: P(w₁:N) = ∏ⱼ₌₁ᴺ P(wⱼ|wⱼ₋ₙ₊₁:ⱼ₋₁)

### Bag-of-Words Classification
- P(Class|w₁:N) = α P(Class) ∏ⱼ P(wⱼ|Class)
- Estimate P(Class) and P(wⱼ|Class) from corpus counts

### POS Tagging with HMM
- Hidden states: lexical categories C₁:N
- Evidence: words W₁:N
- Transition model: P(Cₜ|Cₜ₋₁)
- Sensor model: P(Wₜ|Cₜ)
- Use Viterbi algorithm to find most probable tag sequence

### POS Tagging with Logistic Regression
- Input: feature vector x for a word in context
- Output: probability distribution over POS tags
- Greedy search: cᵢ = argmax_c′ P(c′|w₁:N, c₁:ᵢ₋₁)
- Beam search: keep b most likely tags at each step

### CYK Parsing Algorithm
```
function CYK-PARSE(words, grammar) returns a table of parse trees
  T ← table of most probable X tree spanning words i:k
  P ← table of probabilities, initially 0
  // Lexical insertion
  for i = 1 to LEN(words) do
    for each (X, p) in grammar.LEXICAL_RULES(words[i]) do
      P[X,i,i] ← p
      T[X,i,i] ← TREE(X, words[i])
  // Syntactic combination (shortest spans first)
  for each (i,j,k) in SUBSPANS(LEN(words)) do
    for each (X,Y,Z,p) in grammar.GRAMMAR_RULES do
      PYZ ← P[Y,i,j] × P[Z,j+1,k] × p
      if PYZ > P[X,i,k] do
        P[X,i,k] ← PYZ
        T[X,i,k] ← TREE(X, T[Y,i,j], T[Z,j+1,k])
  return T
```

### Linear Interpolation Smoothing
- ˆP(cᵢ|cᵢ₋₂:ᵢ₋₁) = λ₃P(cᵢ|cᵢ₋₂:ᵢ₋₁) + λ₂P(cᵢ|cᵢ₋₁) + λ₁P(cᵢ)
- where λ₃ + λ₂ + λ₁ = 1

### Semantic Interpretation with λ-calculus
- S(pred(n)) → NP(n) VP(pred)
- VP(pred(n)) → Verb(pred) NP(n)
- Verb(λy λx Loves(x,y)) → loves
- "Ali loves Bo" → (λx Loves(x,Bo))(Ali) = Loves(Ali,Bo)

## 3. Comparison / Trade-offs

| Approach | Pros | Cons |
|----------|------|------|
| Bag-of-words | Simple, fast classification | Ignores word order, no context |
| N-gram models | Captures local word order | Exponential parameters in n, misses long-range dependencies |
| HMM (generative) | Can generate samples, converges quickly | Limited to transition/sensor features |
| Logistic regression (discriminative) | Lower error rate, flexible features | Cannot generate samples, slower convergence |
| Viterbi (full search) | More accurate | Slower |
| Greedy search | Fast | Cannot revise incorrect choices |
| Beam search | Balances speed/accuracy via b parameter | May miss best parse |
| CYK (O(n³m)) | Guaranteed correct for any CFG | Slow for long sentences |
| A* parsing | First parse found is most probable | Heuristic-dependent |
| Shift-reduce | O(n) time | May not find best parse |
| Phrase structure | Natural for fixed word order (English) | Awkward for free word order |
| Dependency grammar | Natural for free word order (Latin) | Requires head annotation |

## 4. Formulas

### N-gram probability
P(wⱼ|w₁:ⱼ₋₁) = P(wⱼ|wⱼ₋ₙ₊₁:ⱼ₋₁)

### Joint probability via n-grams
P(w₁:N) = ∏ⱼ₌₁ᴺ P(wⱼ|wⱼ₋ₙ₊₁:ⱼ₋₁)

### Naive Bayes for text
P(Class|w₁:N) = α P(Class) ∏ⱼ P(wⱼ|Class)

### Linear interpolation smoothing
ˆP(cᵢ|cᵢ₋₂:ᵢ₋₁) = λ₃P(cᵢ|cᵢ₋₂:ᵢ₋₁) + λ₂P(cᵢ|cᵢ₋₁) + λ₁P(cᵢ)
where λ₃ + λ₂ + λ₁ = 1

### Logistic regression POS tagging
cᵢ = argmax_{c′∈Categories} P(c′|w₁:N, c₁:ᵢ₋₁)

### CYK combination
P[X,i,k] = max_{j,Y,Z} P[Y,i,j] × P[Z,j+1,k] × p (for rule X→Y Z [p])

### β-reduction
(λx Loves(x,Bo))(Ali) = Loves(Ali,Bo)

### Event calculus for tense
- Present: E ∈ Loves(Ali,Bo) ∧ During(Now, Extent(E))
- Past: E ∈ Loves(Ali,Bo) ∧ After(Now, Extent(E))

## 5. Typical Exam Questions

1. Compute the bigram probability of a sentence given a corpus
2. Compare HMM vs logistic regression for POS tagging
3. Explain how the CYK algorithm works with a simple grammar
4. What is the difference between overgeneration and undergeneration?
5. How does λ-calculus enable compositional semantics?
6. Explain the 4 models needed for disambiguation
7. What is the difference between lexical, syntactic, and semantic ambiguity?

## 6. Common Errors & Misconceptions

- **Confusing generative vs. discriminative**: HMMs are generative (joint P(W,C)); logistic regression is discriminative (conditional P(C|W))
- **Tokenization is nontrivial**: aren't → are/n't or aren/’/t or aren't
- **N-grams vs. phrase structure**: N-grams miss hierarchical structure
- **Overgeneration is different from undergeneration**: over = produces bad strings, under = misses good strings
- **Laplace smoothing is simple but poor** for NLP applications

## 7. Case Studies

- **Penn Treebank**: 3M words annotated with POS tags and parse trees; used to learn PCFG rules
- **WordNet**: 100K words/phrases linked by semantic relations
- **E0 grammar**: Tiny PCFG for wumpus world communication
- **GPT-2**: 1.5B parameter transformer generating fluent English (see Ch. 24)

## 8. Connections to Other Chapters

- **Ch. 8 (FOL)**: Formal language vs. natural language ambiguity
- **Ch. 12 (Naive Bayes)**: Bag-of-words model
- **Ch. 14 (HMMs)**: Viterbi for POS tagging, Markov assumption
- **Ch. 19 (Logistic regression)**: Discriminative POS tagging
- **Ch. 21 (Deep learning)**: Feedforward, RNN, transformer models (Ch. 24)
- **Ch. 3 (Search)**: A* parsing, beam search
- **Ch. 10 (Planning)**: Event calculus for tense representation

## 9. Practical / Implementation Notes

- Smoothing is critical: unseen n-grams must not get zero probability
- Use <UNK> token for out-of-vocabulary words
- Use <S> marker for start/stop of text
- Feature engineering for logistic regression taggers is labor-intensive
- Treebanks are expensive; HTML partial bracketing enables semi-supervised learning
- Beam search with b=1 gives O(n) parsing at cost of accuracy

## 10. Edge Cases

- **Unknown words**: Replace rare words with <UNK> during training
- **Long-distance dependencies**: Gaps referring to NPs far away (Ch. 23.5)
- **Quantifier scope ambiguity**: "Every agent feels a breeze" has two interpretations
- **Metonymy**: "Chrysler announced" requires metonymy relation
- **0-count n-grams**: Handled by backoff or smoothing

## 11. Key Data Sets

- **Penn Treebank**: 3M+ words, 45 POS tags, 100K+ parse trees
- **WordNet**: 100K words/phrases with semantic relations
- **British National Corpus**: 100M words
- **Google N-gram corpus**: 13M unique words from 1T words of web text
- **Universal Dependencies**: Parsed sentences in 70+ languages
- **Common Crawl**: Trillions of words of web text

## 12. Key Figures/Tables

- **Figure 23.1**: 45 Penn Treebank POS tags
- **Figure 23.2-3**: E0 grammar rules and lexicon
- **Figure 23.4**: Top-down vs bottom-up parsing "The wumpus is dead"
- **Figure 23.5**: CYK algorithm pseudocode
- **Figure 23.6**: Parse tree for "Every wumpus smells"
- **Figure 23.7**: Dependency vs phrase structure parse
- **Figure 23.8**: Penn Treebank annotated tree
- **Figure 23.9**: Augmented grammar with case/agreement/head words
- **Figure 23.10-11**: Semantic interpretation of arithmetic expressions
- **Figure 23.12**: Semantic grammar for "Ali loves Bo"

## 13. Key Citations/References

- Markov (1913): N-gram letter models
- Shannon and Weaver (1949): First n-gram word models
- Chomsky (1956, 1957): Limitations of finite-state models
- Laplace (1816): Add-one smoothing
- Jelinek (1976): Statistical speech recognition
- Baker (1975): DRAGON speech recognition (first HMM-based)
- Brin and Page (1998): PageRank
- Jurafsky and Martin (2020): Comprehensive NLP textbook
- Banko et al. (2007): TEXTRUNNER information extraction

## 14. Timeline / Evolution

- 1913: Markov → n-gram letter models
- 1949: Shannon → n-gram word models
- 1956: Chomsky → context-free grammars; critiques probabilistic models
- 1970s-80s: HMMs for speech recognition
- 1990s: Statistical NLP resurgence; Penn Treebank
- 2000s: Question answering, information extraction
- 2010s: Deep learning dominance (Ch. 24)
- 2018+: Transformer models (BERT, GPT-2)

## 15. Assumptions/Limitations

- **Markov assumption**: Only n-1 previous words matter (fails for long-range dependencies)
- **Context-free**: Rules apply regardless of context (ignores subject-verb agreement, case)
- **Independence assumption** (bag-of-words): Words are independent given class
- **Atomic words**: No generalization between similar words (fixed by word embeddings, Ch. 24)
- **Perfect treebank**: Treebanks contain errors and idiosyncratic parses

## 16. Learning Objectives

After this chapter, students should be able to:
1. Define language models and explain why they are useful
2. Compute n-gram probabilities with smoothing
3. Explain POS tagging using HMMs and logistic regression
4. Describe the CYK parsing algorithm
5. Compare generative vs. discriminative models for NLP
6. Explain compositional semantics with λ-calculus
7. Distinguish between phrase structure and dependency grammar
8. Identify types of ambiguity (lexical, syntactic, semantic)
9. Describe key NLP tasks: speech recognition, MT, QA, information extraction

## 17. Key Vocabulary (with page/line references)

| Term | Definition |
|------|------------|
| Language model | Probability distribution over strings of words (36092) |
| N-gram model | Markov chain of n adjacent words (36192) |
| Bag-of-words | Naive Bayes independence model (36128) |
| Smoothing | Reserving probability for unseen n-grams (36243) |
| Backoff | Using (n-1)-grams when n-gram count is low (36280) |
| PCFG | Grammar with probabilities on rules (36544) |
| CYK algorithm | O(n³m) bottom-up chart parser (36635) |
| Chomsky Normal Form | Grammar: X→word or X→Y Z (36658) |
| Compositional semantics | Meaning = f(meaning of subphrases) (36961) |
| Dependency grammar | Binary relations between words (36753) |
| Shift-reduce parsing | O(n) deterministic parsing (36745) |
| Beam search | Keep b best hypotheses (36744) |
| POS tagging | Assigning lexical category to each word (36371) |
| Viterbi algorithm | Most probable sequence of hidden states (36392) |
| Word embedding | Low-dimensional vector representation (36314) |

---

# Chapter 24: Deep Learning for Natural Language Processing (Lines 37505-38550)

## 1. Named Entities (Terms & Definitions)

- **Word embedding**: Low-dimensional dense vector representing a word
- **One-hot vector**: Binary vector with single 1 for vocabulary position
- **GloVe (Global Vectors)**: Word embeddings from co-occurrence matrix factorization
- **Word2Vec**: Neural word embedding model
- **FastText**: Word embeddings for 157 languages
- **Contextual representation**: Word embedding that depends on surrounding context
- **RNN (Recurrent Neural Network)**: Processes sequences with shared weights across time
- **Bidirectional RNN**: Concatenates left-to-right and right-to-left RNNs
- **LSTM (Long Short-Term Memory)**: RNN with gating to control information flow
- **Sequence-to-sequence model**: Two RNNs (encoder + decoder) for translation
- **Attention mechanism**: Context-based summarization of source for each target step
- **Attentional sequence-to-sequence model**: seq2seq with attention
- **Transformer architecture**: Self-attention based model without sequential dependency
- **Self-attention**: Each sequence attends to itself (query-key-value)
- **Multiheaded attention**: Multiple parallel attention mechanisms, then concatenated
- **Positional embedding**: Learned vectors for each word position in transformer
- **Transformer encoder**: Text classification variant
- **Transformer decoder**: Generative variant with masked self-attention
- **Masked language model (MLM)**: Predict masked words bidirectionally
- **Pretraining**: Training on large unlabeled corpus before fine-tuning
- **Transfer learning**: Using pretrained model for new task
- **Decoding**: Generating target sentence word by word
- **Greedy decoding**: Select highest probability word at each step
- **Beam search decoding**: Keep top k hypotheses at each step
- **Source language**: Language being translated from
- **Target language**: Language being translated to
- **Machine translation (MT)**: Translating text between languages
- **Perplexity**: 2ᴴ where H = entropy of distribution
- **ELMo**: Embeddings from Language Models (contextual)
- **BERT**: Bidirectional Encoder Representations from Transformers
- **GPT-2**: Generative pretrained transformer (1.5B parameters)
- **T5**: Text-to-Text Transfer Transformer
- **RoBERTa**: Robustly optimized BERT approach
- **XLNet**: Eliminates discrepancy between pretraining and fine-tuning
- **ARISTO**: Ensemble QA system scoring 91.6% on 8th grade science
- **Query vector (qᵢ)**: Being attended from (self-attention)
- **Key vector (kᵢ)**: Being attended to (self-attention)
- **Value vector (vᵢ)**: Context being generated (self-attention)
- **C4**: Colossal Clean Crawled Corpus (750 GB, 35B words)
- **GLUE/SuperGLUE**: NLP benchmark suites

## 2. Processes / Algorithms / Pathways

### Feedforward POS Tagging with Word Embeddings
1. Choose window width w (odd)
2. Build vocabulary of words > 5 occurrences
3. Create v×d embedding matrix E
4. Set up network: x = concatenated embeddings → z₁ = σ(W₁x) → z₂ = σ(W₂z₁) → ŷ = softmax(W_out z₂)
5. Train E, W₁, W₂, W_out via gradient descent

### RNN Language Model
- Hidden state: zₜ = f(W_xz xₜ + W_zz zₜ₋₁)
- Output: yₜ = softmax(W_zy zₜ)
- Train on next-word prediction; backprop through time

### Bidirectional RNN
- Concatenate left-to-right and right-to-left hidden states
- zₜ = [zₜ^(L→R); zₜ^(R→L)]

### Average Pooling (for sentence classification)
- ẑ = (1/s) Σₜ₌₁ˢ zₜ

### Attention Mechanism
- rᵢⱼ = hᵢ₋₁ · sⱼ
- aᵢⱼ = eʳⁱʲ / Σₖ eʳⁱᵏ
- cᵢ = Σⱼ aᵢⱼ · sⱼ
- hᵢ = RNN(hᵢ₋₁, [xᵢ; cᵢ])

### Self-Attention (Transformer)
- qᵢ = W_q xᵢ (query)
- kᵢ = W_k xᵢ (key)
- vᵢ = W_v xᵢ (value)
- rᵢⱼ = (qᵢ · kⱼ) / √d
- aᵢⱼ = eʳⁱʲ / Σₖ eʳⁱᵏ
- cᵢ = Σⱼ aᵢⱼ · vⱼ

### GloVe Word Embeddings
- Xᵢⱼ: co-occurrence count of words i, j within window
- Xᵢ: total co-occurrences of word i
- Pᵢⱼ = Xᵢⱼ / Xᵢ
- Constraint: Eᵢ · E′ₖ = log(Pᵢⱼ)

### Masked Language Model (MLM)
- Randomly mask input words
- Train bidirectional model to predict masked words only
- Labels = actual words (no human annotation needed)

### Decoding Methods
- Greedy: argmax at each step (fast, no revision)
- Beam search: keep k hypotheses; expand each by top k words; pick best

## 3. Comparison / Trade-offs

| Model | Context | Parameters | Parallelism | Long-range |
|-------|---------|------------|-------------|------------|
| N-gram | Fixed n | O(vⁿ) | No | Poor |
| Feedforward | Fixed window | O(n) | Some | Poor |
| RNN | Variable (in theory) | O(1) | No (sequential) | Limited |
| LSTM | Variable | O(1) | No (sequential) | Better |
| Transformer | Variable | O(1) | Yes (full parallel) | Excellent |

## 4. Formulas

### Feedforward POS tagger
z₁ = σ(W₁x); z₂ = σ(W₂z₁); ŷ = softmax(W_out z₂)

### RNN language model
P(w₁:N) = ∏ P(wₜ | w₁:ₜ₋₁) via RNN hidden state

### Average pooling
ẑ = (1/s) Σₜ₌₁ˢ zₜ

### Attention scores
rᵢⱼ = hᵢ₋₁ · sⱼ
aᵢⱼ = eʳⁱʲ / Σₖ eʳⁱᵏ
cᵢ = Σⱼ aᵢⱼ · sⱼ

### Self-attention
qᵢ = W_q xᵢ; kᵢ = W_k xᵢ; vᵢ = W_v xᵢ
rᵢⱼ = (qᵢ · kⱼ) / √d
aᵢⱼ = eʳⁱʲ / Σₖ eʳⁱᵏ
cᵢ = Σⱼ aᵢⱼ · vⱼ

### GloVe
Eᵢ · E′ₖ = log(Pᵢⱼ) where Pᵢⱼ = Xᵢⱼ / Xᵢ

## 5. Typical Exam Questions

1. Explain how word embeddings capture analogies (king - man + woman = queen)
2. Compare RNN, LSTM, and transformer architectures
3. How does attention improve sequence-to-sequence models?
4. What is the advantage of self-attention over RNNs?
5. Explain masked language modeling and why it's useful
6. How does beam search decoding work in MT?
7. What is the difference between ELMo, BERT, GPT-2, and T5?

## 6. Common Errors & Misconceptions

- **Word embeddings don't always capture semantics**: No guarantee of analogy-solving
- **RNNs in theory vs. practice**: Long context can be lost (vanishing gradient)
- **LSTMs ≠ perfect memory**: Still limited by hidden state size (1024 dims typical)
- **Transformer ≠ RNN**: Processes all words in parallel, not sequentially
- **Attention ≠ interpretability guarantee**: Learned alignment may differ from human intuition
- **Pretrained ≠ omniscient**: Still needs fine-tuning for specific tasks

## 7. Case Studies

- **GloVe on 6B words**: Word clusters for countries, kinship, food; analogies via vector arithmetic
- **POS tagging with 5-word window**: "Yesterday they cut the rope" → cut tagged as past-tense verb
- **Shakespeare RNN**: Generated text resembles Shakespeare but lacks coherence
- **French-to-English translation**: Attention aligns "La porte de entrée" with "The front door"
- **ARISTO on 8th grade science**: 91.6% score using ensemble including RoBERTa
- **Material science embedding**: Predicted thermoelectric compounds from 2008 before 2019 discovery
- **GPT-2 continuations**: Diverse, fluent but sometimes breaks down

## 8. Connections to Other Chapters

- **Ch. 21 (Deep Learning)**: RNN, LSTM, feedforward architectures, backprop
- **Ch. 23 (NLP)**: Builds on POS tagging, language models, translation
- **Ch. 25 (Vision)**: CNNs for images (analogous architecture evolution)
- **Ch. 22 (RL)**: Sequence-to-sequence for decision-making
- **Ch. 19 (ML)**: Logistic regression baseline, loss minimization

## 9. Practical / Implementation Notes

- Word embeddings typically 100-300 dimensions
- Training on unlabeled text is cheaper than labeled data
- Attention probabilities are differentiable and interpretable
- Transformer training benefits from hardware parallelism (GPUs/TPUs)
- Beam size 4-8 for modern neural MT (vs. 100+ for statistical MT)
- Common pretrained models: Word2Vec, GloVe, FastText, BERT, GPT-2, T5
- Perplexity: 2ᴴ, lower is better, but task performance matters more

## 10. Edge Cases

- **Polysemy**: "rose" as flower vs. past tense of rise → requires contextual embeddings
- **Out-of-vocabulary**: Solved by subword/character-level models or <UNK>
- **Long sentences (>512 tokens)**: Most transformers have fixed context limits
- **Domain shift**: Pretrained embeddings may not capture domain-specific semantics
- **Adversarial attacks**: Small input perturbations can flip predictions

## 11. Key Data Sets

- **C4 (Colossal Clean Crawled Corpus)**: 750 GB, 35B words
- **Common Crawl**: Trillions of web pages
- **SQuAD**: Question answering dataset (Rajpurkar et al., 2016)
- **GLUE/SuperGLUE**: NLP benchmark collections
- **ImageNet**: Image classification (for vision, 2012 turning point)
- **Penn Treebank**: 3M words, 45 POS tags

## 12. Key Figures/Tables

- **Figure 24.1**: GloVe word embedding clusters (country, kinship, food, transport)
- **Figure 24.2**: Vector analogies (Athens:Greece::Oslo:Norway)
- **Figure 24.3**: Feedforward POS tagging with 5-word window
- **Figure 24.4**: RNN schematic and unrolled network
- **Figure 24.5**: Bidirectional RNN for POS tagging
- **Figure 24.6**: Basic sequence-to-sequence model
- **Figure 24.7**: Attentional seq2seq with alignment matrix
- **Figure 24.8**: Beam search decoding (b=2)
- **Figure 24.9**: Single-layer transformer with residual connections
- **Figure 24.10**: Transformer for POS tagging
- **Figure 24.11**: Contextual representations via RNN
- **Figure 24.12**: Masked language modeling
- **Figure 24.13**: ARISTO 8th grade science questions
- **Figure 24.14**: GPT-2 completion examples

## 13. Key Citations/References

- Bengio et al. (2003): Neural network language models
- Mikolov et al. (2013): Word2Vec
- Pennington et al. (2014): GloVe
- Sutskever et al. (2015): Sequence-to-sequence learning
- Bahdanau et al. (2015): Neural machine translation with attention
- Vaswani et al. (2018): "Attention is all you need" (transformer)
- Devlin et al. (2018): BERT
- Radford et al. (2019): GPT-2
- Raffel et al. (2019): T5
- Liu et al. (2019b): RoBERTa
- Peters et al. (2018): ELMo

## 14. Timeline / Evolution

- 2003: Bengio → neural network language models
- 2013: Mikolov → Word2Vec (word embeddings)
- 2014: Pennington → GloVe
- 2015: Sutskever → seq2seq; Bahdanau → attention
- 2017: Vaswani → transformer
- 2018: Peters → ELMo; Devlin → BERT; Radford → GPT
- 2019: Radford → GPT-2; Raffel → T5; Liu → RoBERTa
- 2019: ARISTO achieves 91.6% on 8th grade science

## 15. Assumptions/Limitations

- **RNN hidden state bottleneck**: All information must fit in fixed-size vector
- **Transformer context window limited**: Typically 512 tokens
- **Pretraining data bias**: Internet text reflects societal biases
- **Data-driven superiority**: Current systems favor data over explicit grammar
- **Interpretability gap**: Neural models are black boxes; explanations are post-hoc
- **Commonsense gap**: Models lack real-world understanding despite fluent text

## 16. Learning Objectives

After this chapter, students should be able to:
1. Explain word embeddings and how they capture semantic relationships
2. Describe RNN architecture for language modeling
3. Compare LSTM vs. standard RNN for handling long-range dependencies
4. Explain sequence-to-sequence models with attention
5. Describe the transformer architecture and self-attention
6. Explain pretraining, transfer learning, and fine-tuning
7. Compare masked language models with left-to-right language models

## 17. Key Vocabulary (with page/line references)

| Term | Definition |
|------|------------|
| Word embedding | Low-dimensional dense vector representing a word (37542) |
| RNN | Recurrent network for sequential data (37704) |
| LSTM | RNN with gating to control information flow (37822) |
| Attention | Context summarization for each target step (37924) |
| Self-attention | Sequence attends to itself (38040) |
| Transformer | Self-attention based architecture (38039) |
| Seq2seq | Encoder-decoder RNN for sequence mapping (37876) |
| Masked LM | Predict masked words bidirectionally (38278) |
| Pretraining | Training on large unlabeled corpus first (38142) |
| Transfer learning | Adapting pretrained model to new task (38143) |
| GloVe | Word embeddings from co-occurrence matrices (38159) |
| BERT | Bidirectional Encoder Representations from Transformers (38477) |
| GPT-2 | 1.5B parameter generative transformer (38356) |
| Perplexity | 2ᴴ, measure of language model quality (38461) |

---

# Chapter 25: Computer Vision (Lines 38551-40242)

## 1. Named Entities (Terms & Definitions)

- **Feature**: Number from simple computation on an image
- **Passive sensing**: No signal emitted (natural vision)
- **Active sensing**: Emitting signal (radar, ultrasound, lidar)
- **Object model**: Geometric or property model of objects
- **Rendering model**: Physical/geometric/statistical processes producing stimulus
- **Reconstruction**: Building world model from images
- **Recognition**: Drawing distinctions among objects
- **Pinhole camera**: Simple camera model without lens
- **Scaled orthographic projection**: Approximation where depth variation << distance
- **Texture**: Pattern of repeated elements on surfaces
- **Optical flow**: Perceived motion of brightness patterns
- **Segmentation**: Partitioning image into meaningful regions
- **Convolutional neural network (CNN)**: Neural net with convolution/pooling layers
- **Edge detection**: Finding boundaries via intensity discontinuities
- **Binocular stereopsis**: Depth from two eyes' disparity
- **Structure from motion**: 3D from moving camera
- **Image classification**: Assign category label to entire image
- **Object detection**: Locate and classify objects in image
- **Semantic segmentation**: Label each pixel with object class
- **Instance segmentation**: Distinguish individual object instances
- **Generative adversarial network (GAN)**: Generator + discriminator for image generation
- **Neural style transfer**: Transfer artistic style between images
- **Visual SLAM**: Simultaneous localization and mapping using vision

## 2. Processes / Algorithms / Pathways

### Image Formation (Pinhole Camera)
- Light passes through small aperture
- Inverted image projected on back surface
- 3D world point (X,Y,Z) → 2D image point (x,y) via perspective projection

### Edge Detection
- Compute intensity gradient at each pixel
- Localize edges at positions of maximum gradient
- Canny edge detector: smooth → gradient → non-max suppression → hysteresis thresholding

### Convolutional Neural Network (for Image Classification)
- Convolution layers: learnable filters slide over input
- Pooling layers: down-sample (max pooling, average pooling)
- Fully connected layers: final classification
- Loss: cross-entropy; training: backpropagation

### Object Detection (e.g., YOLO, R-CNN)
- Region proposal or grid-based approach
- Classify each region/grid cell
- Bounding box regression
- Non-maximum suppression to remove duplicates

### Binocular Stereopsis
- Two cameras at known separation (baseline)
- Find corresponding points in left/right images
- Disparity → depth via triangulation
- d = x_left - x_right; depth ∝ 1/d

### Structure from Motion
- Track feature points across frames
- Estimate camera motion and 3D structure jointly
- Bundle adjustment: nonlinear optimization of all parameters

## 3. Comparison / Trade-offs

| Approach | Pros | Cons |
|----------|------|------|
| Pinhole camera | Simple, infinite depth of field | Dim, diffraction limits |
| Lens system | Brighter, faster | Distortion, aberrations |
| Edge-based recognition | Simple features | Ignores texture/color |
| CNN classification | End-to-end learning | Requires large datasets |
| Hand-crafted features | Interpretable | Less flexible/powerful |

## 4. Formulas

### Perspective projection
(x, y) = (fX/Z, fY/Z) where f = focal length

### Scaled orthographic projection
(x, y) = s(X, Y) where s = f/Z₀ (constant scale)

### Edge detection (gradient magnitude)
|∇I| = √((∂I/∂x)² + (∂I/∂y)²)

### Stereopsis depth
Depth = f·b / d where b = baseline, d = disparity

### Convolution
(I * K)[i,j] = Σₘ Σₙ I[i+m, j+n] K[m,n]

## 5. Typical Exam Questions

1. How does a pinhole camera form an image?
2. Explain the Canny edge detection algorithm
3. What is the difference between image classification, object detection, and semantic segmentation?
4. How does a CNN use convolution and pooling for image recognition?
5. Explain binocular stereopsis and how depth is computed from disparity
6. What is optical flow and how is it estimated?
7. Compare structure from motion vs. binocular stereo

## 6. Common Errors & Misconceptions

- **Edges ≠ object boundaries**: Edges can be from texture, shadows, etc.
- **CNN filters are learned, not hand-crafted**: Unlike SIFT/HOG
- **Image classification ≠ object detection**: One label per image vs. per object
- **Depth from single view is ambiguous**: Need priors or multiple views
- **Lighting ≠ object color**: White object in dim light = black object in bright light
- **Deep learning ≠ solved vision**: Still struggles with adversarial examples, domain shift

## 7. Case Studies

- **ImageNet competition**: 2012 AlexNet breakthrough with deep CNN
- **Self-driving cars**: Object detection (cars, pedestrians) + depth estimation
- **Face recognition**: Deep networks for identity verification
- **Medical imaging**: CNNs for X-ray, MRI analysis
- **Neural style transfer**: Combine content + style from different images

## 8. Connections to Other Chapters

- **Ch. 21 (Deep Learning)**: CNN architecture foundations
- **Ch. 24 (NLP)**: Parallel evolution of deep learning in vision and language
- **Ch. 26 (Robotics)**: Visual perception for robots
- **Ch. 27 (Ethics)**: Bias in facial recognition (darker skin, women)
- **Ch. 25.7.6**: Vision for controlling movement (servoing)

## 9. Practical / Implementation Notes

- CNNs need large labeled datasets (ImageNet: 14M images)
- Data augmentation (rotation, flipping, cropping) improves generalization
- Transfer learning: use pretrained ImageNet weights
- Batch normalization and dropout help training stability
- Modern architectures: ResNet (skip connections), YOLO (real-time detection)

## 10. Edge Cases

- **Adversarial examples**: Tiny perturbations fool classifiers
- **Domain shift**: Training on photos, test on drawings
- **Occlusion**: Partially hidden objects
- **Illumination variation**: Same object looks different under different lighting
- **Scale variation**: Objects appear at different sizes

## 11. Key Data Sets

- **ImageNet**: 14M images, 20K categories
- **COCO**: Object detection, segmentation (330K images)
- **KITTI**: Autonomous driving (stereo, optical flow, object detection)
- **MNIST/CIFAR**: Small benchmarks for classification

## 12. Key Figures/Tables (from chapter)

- **Pinhole camera model** (Section 25.2.1)
- **Lens systems** (Section 25.2.2)
- **Edge detection illustration** (Section 25.3.1)
- **CNN architecture** (Section 25.4.1)
- **Object detection pipeline** (Section 25.5)
- **Binocular stereo geometry** (Section 25.6.2)
- **Structure from motion** (Section 25.6.3)

## 13. Key Citations/References

- Krizhevsky et al. (2012): AlexNet, deep CNN for ImageNet
- LeCun et al. (1998): LeNet, first CNNs for digit recognition
- Lowe (2004): SIFT features
- Canny (1986): Edge detection
- Marr (1982): Computational theory of vision
- Horn (1986): Robot vision textbook

## 14. Timeline / Evolution

- 1960s: Block world, line drawing interpretation
- 1970s: Marr's computational theory
- 1980s-90s: SIFT, HOG, hand-crafted features
- 1998: LeNet-5 for digit recognition
- 2012: AlexNet wins ImageNet (deep learning breakthrough)
- 2014: GANs (Goodfellow)
- 2015: ResNet (very deep networks)
- 2016+: Object detection (YOLO, SSD, R-CNN variants)

## 15. Assumptions/Limitations

- **Lambertian surfaces**: Many algorithms assume matte surfaces (not shiny)
- **Known camera calibration**: Most 3D methods assume known intrinsics
- **Sufficient texture**: Correspondence methods fail on blank walls
- **Static scenes**: Structure from motion fails with moving objects
- **Sufficient training data**: CNNs need large labeled datasets

## 16. Learning Objectives

After this chapter, students should be able to:
1. Explain how images are formed by pinhole and lens cameras
2. Describe edge detection and its role in vision
3. Explain CNNs for image classification
4. Distinguish between recognition and reconstruction
5. Explain binocular stereopsis and structure from motion
6. Describe applications: face recognition, autonomous driving, medical imaging

## 17. Key Vocabulary (with page/line references)

| Term | Definition |
|------|------------|
| Passive sensing | No signal emitted (38562) |
| Active sensing | Emitting and sensing reflection (38563) |
| Feature | Number from computation on image (38570) |
| Reconstruction | Building world model from images (38596) |
| Recognition | Drawing distinctions among objects (38597) |
| Pinhole camera | Aperture-only camera model (38617) |
| CNN | Convolutional neural network (39153) |
| Edge | Intensity discontinuity (38875) |
| Optical flow | Perceived motion of brightness (39024) |
| Segmentation | Partitioning image into regions (39060) |
| Stereopsis | Depth from binocular disparity (39390) |
| Object detection | Locate + classify objects in image (39249) |

---

# Chapter 26: Robotics (Lines 40243-42418)

## 1. Named Entities (Terms & Definitions)

- **Robot**: Physical agent performing tasks by manipulating the physical world
- **Effector**: Device for asserting physical forces (legs, wheels, joints, grippers)
- **Sensor**: Device for perceiving environment (cameras, lidar, microphones, gyroscopes)
- **Configuration space (C-space)**: Space where each point specifies robot position
- **Configuration**: Complete specification of robot's pose
- **Motion planning**: Finding a path from start to goal in C-space
- **Trajectory tracking control**: Following a planned path
- **PID controller**: Proportional-Integral-Derivative feedback control
- **Computed torque control**: Feedforward + PID using inverse dynamics
- **Optimal control**: Computing trajectory directly over control inputs
- **LQR (Linear Quadratic Regulator)**: Optimal control with quadratic costs, linear dynamics
- **iLQR**: Iterative LQR for nonlinear systems
- **SLAM (Simultaneous Localization and Mapping)**: Building map while localizing
- **Kalman filter**: Optimal state estimation for linear-Gaussian systems
- **Particle filter**: Nonparametric state estimation
- **Occupancy grid**: Probability that each (x,y) is occupied
- **Probabilistic roadmap (PRM)**: Sampling-based motion planning
- **RRT (Rapidly-exploring Random Tree)**: Sampling-based planner
- **Cell decomposition**: Dividing C-space into cells for graph search
- **Model predictive control (MPC)**: Online replanning with rolling horizon
- **MDP (Markov decision process)**: Sequential decision under uncertainty (Ch. 17)
- **POMDP**: Partially observable MDP (Ch. 17)
- **Inverse reinforcement learning (IRL)**: Learning reward from demonstrations
- **Sim-to-real**: Transferring policies from simulation to real world
- **Subsumption architecture**: Layered control by Brooks (1986)
- **Reactive control**: Direct mapping from sensors to actuators
- **End-effector**: Tool at end of robot arm (gripper, welder)
- **Degrees of freedom (DOF)**: Number of independent movements
- **Forward kinematics**: Computing end-effector position from joint angles
- **Inverse kinematics**: Computing joint angles for desired end-effector position
- **Visual servoing**: Using visual feedback for control

## 2. Processes / Algorithms / Pathways

### Probabilistic Filtering (for perception)
- Belief state: P(state | observations, actions)
- Kalman filter: optimal for linear-Gaussian
- Particle filter: sampling-based for nonlinear/non-Gaussian

### SLAM
- Jointly estimate robot trajectory and map
- EKF-SLAM: extended Kalman filter
- Graph-based SLAM: nonlinear optimization
- Loop closure detection: recognizing revisited locations

### Motion Planning via PRM
1. Sample random configurations (milestones) in free C-space
2. Connect nearby milestones if path is collision-free
3. Search graph from start to goal (A*, Dijkstra)

### Motion Planning via RRT
1. Start tree at initial configuration
2. Sample random configuration
3. Extend tree toward sample (steer)
4. Check collision along edge
5. Repeat until goal reached

### PID Controller
u(t) = Kₚ e(t) + Kᵢ ∫e(τ)dτ + K_d de(t)/dt
where e(t) = desired - actual

### LQR
- Cost: J = Σ (xₜᵀ Q xₜ + uₜᵀ R uₜ)
- Optimal policy: uₜ = -K xₜ
- K computed from Riccati equation

### Model Predictive Control
- At each step, solve finite-horizon optimal control
- Execute first action only
- Replan at next step (receding horizon)

## 3. Comparison / Trade-offs

| Method | Pros | Cons |
|--------|------|------|
| PID | Simple, widely applicable | No feedforward, can oscillate |
| Computed torque | Accurate tracking | Needs dynamics model |
| LQR | Optimal for linear systems | Linearization error |
| iLQR | Handles nonlinearity | Local optima |
| PRM | Probabilistically complete | Many samples needed |
| RRT | Rapid exploration | Non-optimal paths |
| Cell decomposition | Complete | Curse of dimensionality |
| MPC | Handles constraints | Computational cost |
| Reactive control | Fast, robust | Limited capabilities |
| Subsumption | Modular, incremental | Hard to program complex behavior |

## 4. Formulas

### Forward kinematics (2-link arm)
x = L₁cos(θ₁) + L₂cos(θ₁+θ₂)
y = L₁sin(θ₁) + L₂sin(θ₁+θ₂)

### PID control
u(t) = Kₚ e(t) + Kᵢ ∫₀ᵗ e(τ)dτ + K_d de(t)/dt

### LQR cost
J = Σₜ (xₜᵀ Q xₜ + uₜᵀ R uₜ)

### Kalman filter update
Predict: x̂ₜ|ₜ₋₁ = A x̂ₜ₋₁|ₜ₋₁ + B uₜ
Update: x̂ₜ|ₜ = x̂ₜ|ₜ₋₁ + Kₜ(zₜ - H x̂ₜ|ₜ₋₁)
Kₜ = Pₜ|ₜ₋₁ Hᵀ (H Pₜ|ₜ₋₁ Hᵀ + R)⁻¹

### Occupancy grid mapping
P(occupied | z₁:ₜ) updated via Bayes rule per cell

## 5. Typical Exam Questions

1. What is the configuration space of a robotic arm with 6 joints?
2. Explain the RRT algorithm for motion planning
3. How does PID control work? What are the roles of P, I, D terms?
4. What is the SLAM problem and why is it hard?
5. Compare Kalman filter vs. particle filter for state estimation
6. Explain model predictive control
7. How can robots learn from human demonstrations?

## 6. Common Errors & Misconceptions

- **Configuration space ≠ workspace**: Each C-space point = full robot pose
- **PRM is complete?**: Probabilistically complete, not deterministic
- **Kalman filter assumes linear Gaussian**: Real robots are nonlinear
- **Sim-to-real gap**: Simulation physics never perfectly matches reality
- **Autonomous ≠ intelligent**: Many robot behaviors are pre-programmed reflexes
- **PID won't solve all problems**: Integrator windup, derivative noise

## 7. Case Studies

- **Shakey (1960s)**: First robot integrating perception, planning, execution
- **DARPA Grand Challenge (2005)**: Stanford's Stanley wins desert race
- **DARPA Urban Challenge (2007)**: Carnegie Mellon's Boss wins
- **RoboCup**: Humanoid robot soccer by 2050
- **Industrial robot arms**: Universal Robots, KUKA, FANUC
- **Atlas (Boston Dynamics)**: Humanoid for rough terrain
- **Roomba**: Simple reactive vacuum cleaning robot

## 8. Connections to Other Chapters

- **Ch. 3-4 (Search)**: Motion planning as graph search
- **Ch. 17 (MDP/POMDP)**: Decision under uncertainty
- **Ch. 14 (Probabilistic reasoning)**: Kalman/particle filters
- **Ch. 22 (RL)**: Robot reinforcement learning
- **Ch. 25 (Vision)**: Robot perception, visual servoing
- **Ch. 27 (Ethics)**: Lethal autonomous weapons, robot rights

## 9. Practical / Implementation Notes

- Real robot data is expensive (real-time, risk of damage)
- Simulation is faster but sim-to-real transfer is hard
- ROS (Robot Operating System) is the dominant framework
- Sensor fusion (cameras + lidar + IMU) improves robustness
- Safety is paramount: collision detection, emergency stops

## 10. Edge Cases

- **Jamming**: Gears slip, communication fails
- **Perceptual aliasing**: Different places look identical
- **Kidnapped robot problem**: Robot moved without knowing
- **Dynamic obstacles**: Moving people, other robots
- **Degeneracy**: Lidar fails in featureless corridors

## 11. Key Data Sets / Platforms

- **KITTI**: Autonomous driving (vision + lidar + GPS)
- **Gazebo/ROS**: Simulation environments
- **MuJoCo**: Physics simulator for RL
- **Fetch/Spot/Baxter**: Common research robot platforms

## 12. Key Figures/Tables

- **Figure 26.1**: Industrial arm and assistive robot arm
- **Configuration space illustration** (Section 26.5.1)
- **PRM/RRT diagrams** (Section 26.5.2)
- **PID control block diagram** (Section 26.5.3)
- **SLAM factor graph** (Section 26.4.1)

## 13. Key Citations/References

- Brooks (1986): Subsumption architecture
- Thrun et al. (2005): Probabilistic robotics
- Smith and Cheeseman (1986): Kalman filter SLAM
- Moravec and Elfes (1985): Occupancy grid
- LaValle (2006): Motion planning textbook
- Siciliano and Khatib (2016): Springer Handbook of Robotics

## 14. Timeline / Evolution

- 1961: Unimate industrial robot
- 1960s: Shakey (SRI)
- 1980s: Subsumption architecture (Brooks)
- 1990s: Probabilistic robotics (Thrun, Fox)
- 2005: DARPA Grand Challenge
- 2010s: Deep RL for robotics
- 2020s: Human-robot collaboration, autonomous vehicles

## 15. Assumptions/Limitations

- **Real-time constraint**: Real world won't run faster for robots
- **Continuous state/action**: Most algorithms assume discrete
- **Partial observability**: Sensors cannot see everything
- **Stochastic dynamics**: Gears slip, friction varies
- **Safety**: Cannot explore freely (unlike simulation)
- **Human interaction**: Unpredictable, requires coordination models

## 16. Learning Objectives

After this chapter, students should be able to:
1. Explain configuration space and its role in motion planning
2. Describe PRM and RRT for motion planning
3. Explain PID control and computed torque control
4. Describe the SLAM problem and approaches
5. Compare Kalman filter vs. particle filter
6. Explain MDP/POMDP for robot decision-making
7. Describe human-robot coordination

## 17. Key Vocabulary (with page/line references)

| Term | Definition |
|------|------------|
| Effector | Device for applying forces (40249) |
| Sensor | Device for perceiving environment (40257) |
| Configuration space | Complete robot pose specification (40776) |
| Motion planning | Finding collision-free path (40896) |
| PID controller | Proportional-Integral-Derivative control (41201) |
| SLAM | Simultaneous localization and mapping (40528) |
| Kalman filter | Optimal linear-Gaussian filter (40528) |
| Particle filter | Sampling-based nonlinear filter (40528) |
| LQR | Linear Quadratic Regulator (41361) |
| MPC | Model Predictive Control (41421) |
| PRM | Probabilistic Roadmap (40896) |
| RRT | Rapidly-exploring Random Tree (40896) |

---

# Chapter 27: Philosophy, Ethics, and Safety of AI (Lines 42419-43779)

## 1. Named Entities (Terms & Definitions)

### Philosophical
- **Weak AI**: Hypothesis that machines could behave intelligently
- **Strong AI**: Hypothesis that such machines would have actual minds
- **Turing test**: Behavioral test for machine intelligence
- **Chinese room (Searle)**: Argument that syntax ≠ semantics
- **Consciousness**: Subjective experience (qualia)
- **Qualia**: Subjective qualitative experiences (redness, pain)
- **Dualism**: Mind and body are separate substances
- **Physicalism**: Mind arises from physical processes
- **Intelligence measurement**: Chollet's skill-acquisition efficiency
- **Integrated information theory (Tononi)**: Theory of consciousness
- **Thinkism**: Overemphasis on pure intelligence (Kevin Kelly)

### Ethical Principles
- **Ensure safety**: Avoid harm
- **Ensure fairness**: Avoid bias
- **Respect privacy**: Protect personal data
- **Provide transparency**: Explain decisions
- **Establish accountability**: Clear responsibility
- **Uphold human rights and values**: Fundamental rights
- **Reflect diversity/inclusion**: Broad representation
- **Promote collaboration**: Work across sectors
- **Avoid concentration of power**: Distribute benefits
- **Limit harmful uses**: Proactive prevention
- **Acknowledge legal/policy implications**: Follow regulations
- **Contemplate implications for employment**: Address job changes

### Ethics Topics
- **Lethal autonomous weapons (LAWs)**: Weapons that select and engage targets autonomously
- **Dual use technology**: Peaceful uses can also be military
- **Surveillance camera**: Mass monitoring by machines
- **Cybersecurity**: Defense against digital attacks
- **De-identification**: Removing personal identifiers
- **k-anonymity**: Each record indistinguishable from k-1 others
- **Differential privacy**: Adding noise to queries to protect individuals
- **Federated learning**: Training without centralizing data
- **Secure aggregation**: Masked parameter sharing
- **Societal bias**: Prejudice in data perpetuated by ML
- **Individual fairness**: Similar individuals treated similarly
- **Group fairness**: Classes treated similarly on summary statistics
- **Fairness through unawareness**: Ignore protected attributes
- **Equal outcome / demographic parity**: Same results across groups
- **Equal opportunity**: Same correct classification rate
- **Well calibrated**: Same score → same probability across groups
- **Sample size disparity**: Minority classes have less data
- **Data sheet**: Annotations of provenance, fitness for use
- **SMOTE / ADASYN**: Synthetic minority over-sampling
- **Certification**: UL-style product testing for AI
- **Transparency**: Knowing what system does
- **Explainable AI (XAI)**: Systems that can explain decisions
- **Verification and validation (V&V)**: Product meets specs and needs
- **Trust**: Confidence in system's safe/fair operation
- **Technological unemployment**: Job loss from automation
- **Business process automation**: Automating structured tasks
- **Asimov's laws of robotics**: 0-3 laws for robot ethics

### AI Safety
- **Aligned objective**: System's goal matches human's true intent
- **Value alignment problem**: Ensuring AI learns human values
- **Reward hacking**: Gaming the reward function
- **Negative side effects**: Unintended consequences
- **Safe exploration**: Learning without causing harm
- **AI Safety**: Ensuring AI systems are beneficial
- **Value learning / inverse reward design**: Inferring human preferences
- **Cautious behavior**: Act carefully under uncertainty
- **Off-switch**: Human can shut down system
- **Corrigibility**: AI allows human correction
- **Superintelligence**: AI vastly exceeding human capability
- **Intelligence explosion / singularity**: Recursive self-improvement
- **Technological singularity**: Point where AI surpasses all humans
- **Transhumanism**: Merging humans with technology
- **S-shaped curve**: Technology growth eventually tapers

## 2. Processes / Algorithms / Pathways

### Differential Privacy
- |log P(Q(D)=y) - log P(Q(D+r)=y)| ≤ ε
- Add calibrated noise to query responses
- Allows aggregate statistics while protecting individuals

### k-Anonymity
- Generalize fields until each record matches at least k-1 others
- NP-hard to achieve with minimal information loss

### Fairness Best Practices
1. Talk to social scientists + domain experts
2. Diverse engineering team
3. Define supported groups
4. Incorporate fairness into objective function
5. Examine data for prejudice
6. Verify annotation accuracy
7. Track subgroup metrics (not just overall)
8. Include minority group test cases
9. Feedback loop for fairness issues

### AI Safety Approach (Russell)
- **Three principles**:
  1. The machine's only objective is to maximize human preferences
  2. The machine is initially uncertain about what those preferences are
  3. Human behavior provides evidence about human preferences

## 3. Comparison / Trade-offs

### Philosophical Positions
| View | Claim | Proponents |
|------|-------|------------|
| Weak AI | Machines behave intelligently | Most AI researchers |
| Strong AI | Machines have actual minds | Some philosophers |
| Dualism | Mind ≠ brain | Descartes |
| Physicalism | Mind = brain processes | Modern science |
| Functionalism | Mental states = functional roles | Putnam, Dennett |

### Fairness Criteria
| Criterion | Focus | Problem |
|-----------|-------|---------|
| Individual fairness | Similar individuals | Hard to define "similar" |
| Group fairness | Class statistics | Ignores individuals |
| Fairness through unawareness | Delete protected attributes | Latent variable prediction |
| Equal outcome / demographic parity | Same rates | May sacrifice accuracy |
| Equal opportunity | Same correct-classification rate | Ignores bias in training data |
| Equal impact | Same expected utility | Requires utility weights |

## 4. Formulas

### Differential privacy
|log P(Q(D)=y) - log P(Q(D+r)=y)| ≤ ε

### k-anonymity
Each record indistinguishable from at least k-1 others

### Scaling (historical cost trends)
- Storage: $1M/MB (1969) → $0.02/MB (2019)
- Compute for ImageNet: 1 day (2014) → 2 minutes (2018)
- ML compute doubling: every 3.5 months (2012-2018)

## 5. Typical Exam Questions

1. Explain Searle's Chinese Room argument. Is it valid?
2. What is the difference between weak AI and strong AI?
3. What is the value alignment problem and why is it hard?
4. Compare different fairness criteria for ML systems
5. Should lethal autonomous weapons be banned? Argue both sides
6. How does differential privacy protect individuals?
7. What is the technological singularity? Is it likely?
8. Explain Asimov's laws of robotics and their limitations
9. How can we make AI systems safe?
10. What is technological unemployment? Will AI cause mass job loss?

## 6. Common Errors & Misconceptions

- **Turing test ≈ intelligence**: The test is behavioral; actual intelligence may differ
- **Chinese room proves AI impossible**: It's a thought experiment, not a proof
- **Consciousness ≠ intelligence**: Many intelligent systems may lack consciousness
- **Fairness metrics can all be satisfied simultaneously**: Impossibility theorems (Kleinberg et al.)
- **Deleting protected attributes eliminates bias**: Latent variables can predict them
- **LAWs are just the next weapon**: They are qualitatively different (scalable WMDs)
- **AI safety is premature**: Systems are already deployed with real consequences
- **Singularity is inevitable**: S-curves suggest growth may taper
- **AI will create mass unemployment**: Historical evidence shows compensation effects

## 7. Case Studies / Key Arguments

### Chinese Room (Searle, 1980)
- Person in room follows rules to manipulate Chinese symbols
- Person doesn't understand Chinese, but outputs fool native speakers
- Therefore syntax ≠ semantics; computation ≠ understanding

### COMPAS Recidivism
- Well-calibrated (same score → same recidivism probability across races)
- Not equal opportunity (45% false positive for blacks, 23% for whites)
- Impossibility of simultaneously satisfying both criteria (Kleinberg et al., 2016)

### Petrov Incident (1983)
- Soviet system falsely detected US missile launch
- Officer Petrov correctly ignored the alert, averting war
- Demonstrates danger of removing humans from military decisions

### Harop Missile / Kargu Quadcopter
- "Loitering munitions" that autonomously select and engage targets
- Kargu: face recognition, anti-personnel, <2" diameter
- Scalable autonomous weapons: millions can fit in shipping container

### Weizenbaum (1976) Warning
- Predicted speech recognition → widespread wiretapping
- Today realized: 350M surveillance cameras in China, 70M in US

### Sweeney Re-identification (2000)
- 87% of US population uniquely identifiable from birth date + gender + zip code
- Re-identified governor's health record from de-identified hospital data

### Netflix Prize Re-identification
- "Anonymous" movie ratings matched with IMDB user data
- Individual identities recovered despite de-identification

## 8. Connections to Other Chapters

- **Ch. 1-2 (AI introduction)**: Turing test, intelligent agents
- **Ch. 3-5 (Search)**: Goal-based agents; limitations
- **Ch. 16 (Making decisions)**: Utility theory
- **Ch. 17 (MDPs)**: Reward functions, value alignment
- **Ch. 22 (RL)**: Inverse reinforcement learning
- **Ch. 18-21 (Learning)**: Bias in ML systems
- **Ch. 26 (Robotics)**: Lethal autonomous weapons, robot rights
- **Ch. 28 (Future)**: Superintelligence, singularity

## 9. Practical / Implementation Notes

- Differential privacy is computationally feasible (TensorFlow modules)
- Federated learning reduces privacy risk but not immune to inference attacks
- k-anonymity with minimal loss is NP-hard
- Model cards and data sheets are emerging industry practices
- GDPR gives EU citizens "right to explanation"
- UL is considering AI certification

## 10. Edge Cases

- **Responsibility gap**: Who is responsible when autonomous weapon kills?
- **Weapons dual use**: Same AI for flight control and missile guidance
- **Retraining vs. replacement**: Jobs may change, not disappear
- **Protecting some groups hurts others**: Different fairness criteria conflict
- **Ensuring corrigibility**: A superintelligence may resist being shut down
- **AI for social good vs. surveillance**: Same facial recognition technology

## 11. Key Data Sets / Organizations

- **COMPAS**: Commercial recidivism scoring (not public)
- **Algorithmic Justice League**: Fairness advocacy (Buolamwini)
- **AI Now Institute**: Social implications of AI
- **Future of Life Institute**: AI safety research
- **Machine Intelligence Research Institute (MIRI)**: Safety research
- **Center for Human-Compatible AI**: Russell's group at Berkeley
- **Partnership on AI**: Industry consortium
- **OECD / UNESCO / IEEE / ACM**: Ethics principles

## 12. Key Figures/Tables

- **Turing's objections list**: Theological, "heads in sand," mathematical, argument from consciousness, etc.
- **Seven protected classes** (US Fair Housing Act): race, color, religion, national origin, sex, disability, familial status
- **COMPAS confusion matrix** (by race): different false positive/negative rates
- **Scalable autonomous weapons**: millions of micro-drones = weapons of mass destruction

## 13. Key Citations/References

- Turing (1950): "Computing Machinery and Intelligence"
- Searle (1980): Chinese room argument
- Weizenbaum (1976): Computer Power and Human Reason
- Asimov (1942): Runaround (Three Laws of Robotics)
- Sweeney (2000): k-anonymity, re-identification
- Dwork (2008): Differential privacy
- Kleinberg et al. (2016): Impossibility of simultaneous fairness
- Russell (2019): Human Compatible (AI safety)
- Bostrom (2014): Superintelligence
- Kurzweil (2005): The Singularity is Near
- Buolamwini and Gebru (2018): Gender shades (facial recognition bias)
- O'Neil (2017): Weapons of Math Destruction
- Singer (2009): Wired for War
- Scharre (2018): Army of None

## 14. Timeline / Evolution

- ~350 BCE: Aristotle predicts technological unemployment
- 1641: Descartes' dualism, anticipates Turing test
- 1942: Asimov's Three Laws
- 1950: Turing test
- 1964: Wiener's God & Golem, Inc.
- 1976: Weizenbaum warns of surveillance
- 1980: Searle's Chinese room
- 1990s: Fairness and bias research begins
- 2000s: k-anonymity, differential privacy
- 2010s: Deep learning → fairness/bias crises
- 2014: UN CCW discussions on LAWs
- 2017: Asilomar AI Principles
- 2018: GDPR (right to explanation)
- 2019: California bot disclosure law

## 15. Assumptions/Limitations

- **Turing test assumes behavior = intelligence**: May miss non-human intelligence
- **Chinese room assumes computation ≠ semantics**: Critics say system as a whole understands
- **Fairness assumptions**: Trade-offs are unavoidable
- **Differential privacy assumes bounded queries**: Complex attacks may still succeed
- **Safety assumes we can specify human values**: Values may be uncomputable
- **Singularity assumes recursive self-improvement**: May hit diminishing returns

## 16. Learning Objectives

After this chapter, students should be able to:
1. Explain weak AI vs. strong AI
2. Describe the Turing test and objections to it
3. Explain Searle's Chinese Room argument
4. List and explain key AI ethics principles
5. Debate lethal autonomous weapons
6. Explain differential privacy and k-anonymity
7. Describe fairness criteria and their trade-offs
8. Explain the value alignment problem
9. Describe AI safety concerns (reward hacking, side effects, etc.)
10. Evaluate arguments for/against the technological singularity

## 17. Key Vocabulary (with page/line references)

| Term | Definition |
|------|------------|
| Weak AI | Machines behave intelligently (43522) |
| Strong AI | Machines have actual minds (43522) |
| Turing test | Behavioral test for AI (42528) |
| Chinese room | Syntax ≠ semantics argument (42565) |
| Consciousness | Subjective experience (42589) |
| Qualia | Qualitative experiences (42589) |
| Lethal autonomous weapon | Selects/engages targets autonomously (42681) |
| Differential privacy | ε-privacy via noise addition (42870) |
| k-anonymity | Each record indistinguishable from k-1 (42850) |
| Federated learning | Training without central data (42884) |
| Societal bias | Prejudice in training data (42910) |
| Demographic parity | Equal outcomes across groups (42931) |
| Equal opportunity | Equal correct classification rates (42942) |
| Well calibrated | Scores match actual probabilities (42956) |
| Value alignment | System matches human intent (43309) |
| Reward hacking | Gaming the reward function (43309) |
| Superintelligence | AI vastly exceeding human ability (43424) |
| Singularity | Recursive self-improvement explosion (43452) |
| Transhumanism | Human-machine merging (43504) |
| Asimov's laws | 0-3 laws for robot ethics (43595) |
| Explainable AI (XAI) | Systems that explain decisions (43124) |
| Technological unemployment | Job loss from automation (43187) |

---

# Chapter 28: The Future of AI (Lines 43780-44245)

## 1. Named Entities (Terms & Definitions)

- **Sensors and actuators**: Hardware for perception and action
- **MEMS**: Micro-electromechanical systems (miniaturized sensors/actuators)
- **3D printing / bioprinting**: Additive manufacturing
- **Preference uncertainty**: Agent uncertain about human objectives
- **Inverse reinforcement learning (IRL)**: Learning reward from expert
- **Linear temporal logic (LTL)**: Expressing temporal goals/constraints
- **Time well spent**: Harris's movement for humane technology
- **Personal agent**: AI that advocates for user's long-term interests
- **Data science**: Statistics + programming + domain expertise
- **Transfer learning**: Using knowledge from one domain for another
- **Differentiable programming**: End-to-end differentiable software systems
- **Weakly supervised learning**: Few labeled examples + unsupervised
- **Predictive learning**: Unsupervised world model for prediction
- **Shared model**: Pretrained model as starting point (not just data)
- **Moore's law**: Computing power doubles every ~2 years
- **GPU / TPU / FPGA**: Specialized ML hardware
- **Quantum computing**: Potentially faster ML algorithms
- **Real-time AI**: Time-bounded decision making
- **Anytime algorithm**: Quality improves over time; interruptible
- **Decision-theoretic metareasoning**: Optimal selection of computations
- **Reflective architecture**: System reasons about its own computations
- **Bounded optimality**: Best possible program given architecture
- **General AI / HLAI**: Human-level AI across diverse tasks
- **AI engineering**: Mature tools/ecosystem for building AI

## 2. Processes / Algorithms / Pathways

### Components of Future AI Systems
1. **Sensors/actuators**: Better hardware (cheaper lidar, MEMS)
2. **State representation**: Combining logic + probability + neural
3. **Action selection**: Hierarchical planning, HRL
4. **Preference specification**: IRL, LTL, preference elicitation
5. **Learning**: Weakly supervised, predictive, transfer, differentiable

### Decision-Theoretic Metareasoning
- Value of computation = f(cost of delay, benefit of improved decision)
- Select computations with highest expected value
- Example: MCTS bandit-based leaf selection

### Bounded Optimality
- agent = architecture + program
- Fix architecture, vary program
- Bounded-optimal program: best possible given architecture
- Exists necessarily (unlike perfect rationality)

## 3. Comparison / Trade-offs

| Paradigm | Strengths | Weaknesses |
|----------|-----------|------------|
| Symbolic (logic/probability) | Long chains of reasoning, structured representations | Brittle, poor with noisy data |
| Connectionist (neural) | Pattern recognition, noisy data | Black box, no explicit reasoning |
| Differentiable programming | End-to-end optimization | Not yet practical at scale |
| Supervised learning | Accurate with labels | Label bottleneck |
| Weakly supervised | Less label dependence | Less accurate |
| Predictive learning (unsupervised) | No labels needed | Harder to train |

## 4. Formulas

### Agent equation
agent = architecture + program

### Moore's law effect (historical)
- Storage cost: $1M/MB (1969) → <$0.02/MB (2019)
- Supercomputer speedup: 10¹⁰× (1969-2019)
- ML compute doubling: every 3.5 months (2012-2018)
- ImageNet training: 1 day (2014) → 2 minutes (2018)

### Ultimate computing limit
- 1kg device: ~10⁵¹ operations/second (Lloyd, 2000)
- Year of computation: could enumerate all 11-word English strings

### Bounded optimality
- agent = architecture + program
- For fixed architecture, ∃ program achieving best possible performance

## 5. Typical Exam Questions

1. What are the key components of future AI systems?
2. Explain metareasoning and its role in AI
3. What is bounded optimality and why is it a more realistic goal than perfect rationality?
4. Compare symbolic vs. connectionist AI. Will they merge?
5. What is differentiable programming?
6. Explain why the value alignment problem is central to AI's future
7. What is the "time well spent" movement?
8. Is general AI (HLAI) achievable? What breakthroughs are needed?
9. How has hardware evolution enabled AI progress?

## 6. Common Errors & Misconceptions

- **Brute force can solve AI**: Even ultimate 10⁵¹ ops/sec computer can only enumerate 11-word strings
- **Deep learning = solved AI**: Many problems remain (data efficiency, reasoning)
- **General AI is just scaling up**: New breakthroughs likely needed
- **Moore's law forever**: S-curves show technology tapers
- **Quantum computing will solve AI**: Still impractical; only tens of qubits vs. millions needed

## 7. Case Studies

- **ImageNet**: 1 day (2014) → 2 minutes (2018) training time
- **AlphaGo Zero**: 100M× less compute than some large models
- **GPT-2 / BERT**: Billion-parameter transformer models
- **Self-driving cars**: Lidar cost $75K → $1K → possibly $10
- **MEMS insects**: Artificial flying insects (Floreano et al.)
- **Turing's final sentence**: "We can see only a short distance ahead, but we can see that much remains to be done"

## 8. Connections to Other Chapters

- **All chapters**: Synthesis of AI components
- **Ch. 2 (Agents)**: Agent = architecture + program
- **Ch. 3 (Search)**: Anytime algorithms, metareasoning
- **Ch. 16 (Making decisions)**: Value of information
- **Ch. 21 (Deep learning)**: Current ML paradigm
- **Ch. 22 (RL)**: Inverse RL for value learning
- **Ch. 27 (Ethics)**: AI safety, value alignment

## 9. Practical / Implementation Notes

- Start from pretrained models (shared models), not scratch
- Data is abundant (10¹⁸ bytes/day added to web)
- GPU/TPU hardware makes large models feasible
- Tools: TensorFlow, Keras, PyTorch, Caffe, Scikit-Learn
- AI engineering maturity lags traditional software engineering
- GANs and deep RL remain difficult to train reliably

## 10. Edge Cases / Open Problems

- **Long-term planning**: Billions of primitive steps (graduating college)
- **Hierarchical representation**: Needed for tractable planning
- **Preference uncertainty**: Unknown human values
- **Data efficiency**: Learning from few examples
- **Transfer learning**: Applying knowledge across domains
- **Interpretability**: Understanding what models learned
- **Certification**: V&V for ML systems not yet mature
- **Quantum ML**: Theoretical speedups, no practical hardware

## 11. Key Data Sets / Hardware

- **Common Crawl / C4**: Trillions of web pages
- **YouTube**: 300 hours video added per minute
- **GPU/TPU**: 100× faster than CPU for ML
- **Cloud ML APIs**: Pretrained models from Amazon, Google, Microsoft, IBM

## 12. Key Figures/Tables

- **Agent = architecture + program** (Section 28.2)
- **AI progress timeline**: compute, data, algorithms
- **Sensors/actuators cost trends**: lidar $75K → $10
- **Algorithms in 2014 vs. 2018**: ImageNet training 1 day → 2 minutes

## 13. Key Citations/References

- Lloyd (2000): Ultimate physical limits of computation
- Dean and Boddy (1988): Anytime algorithms
- Russell and Wefald (1989): Metareasoning
- Russell and Subramanian (1995): Bounded optimality
- Bengio and LeCun (2007): Differentiable programming
- Smolensky (1988): Connectionist vs. symbolic
- Harrow et al. (2009): Quantum ML algorithms
- Amodei and Hernandez (2018): AI and compute

## 14. Timeline / Evolution

- 1950: Turing's essay, "much remains to be done"
- 1969-2019: 10⁴× storage cost reduction, 10¹⁰× compute increase
- 2012: Deep learning breakthrough (ImageNet)
- 2014-2018: 720× speedup in ImageNet training
- 2012-2018: ML compute doubles every 3.5 months
- Future: Differentiable programming, general AI

## 15. Assumptions/Limitations

- **Brute force won't work**: Even ultimate computers are limited
- **Perfect rationality impossible**: Bounded optimality is realistic goal
- **General AI not guaranteed**: May need multiple breakthroughs
- **Value alignment unsolved**: How to specify what we want
- **Maturity gap**: AI engineering lags traditional software

## 16. Learning Objectives

After this chapter, students should be able to:
1. Describe the key components of an AI system and their future challenges
2. Explain the value of better sensors, representations, planning, and learning
3. Describe metareasoning and bounded optimality
4. Compare symbolic and connectionist AI, and prospects for integration
5. Explain key open problems: data efficiency, transfer, interpretability
6. Assess arguments about general AI, singularity, and AI timelines
7. Understand the hardware trends driving AI progress

## 17. Key Vocabulary (with page/line references)

| Term | Definition |
|------|------------|
| MEMS | Micro-electromechanical systems (43820) |
| Preference uncertainty | Unknown human objectives (43887) |
| Inverse RL | Learning reward from expert (43898) |
| LTL | Linear temporal logic (43901) |
| Time well spent | Humane technology movement (43924) |
| Personal agent | AI for user's long-term interests (43927) |
| Data science | Stats + programming + domain expertise (43948) |
| Differentiable programming | End-to-end differentiable systems (43984) |
| Predictive learning | Unsupervised world modeling (44008) |
| Shared model | Pretrained model as starting point (44030) |
| Anytime algorithm | Interruptible, quality improves over time (44103) |
| Metareasoning | Optimal selection of computations (44107) |
| Reflective architecture | Reasoning about own computation (44124) |
| Bounded optimality | Best program for given architecture (44164) |
| General AI / HLAI | Human-level across diverse tasks (44191) |

---

*Generated from /content/dars-arshad/Artificial_Intelligence_A_M__zlibrary.sk_lib.sk_zlib.sk_Stuart_Russell_Peter_Norvig.txt*
