# Complete Extraction: Chapters 19–22 of AIMA (Russell & Norvig)

---

## CHAPTER 19: LEARNING FROM EXAMPLES

### 1. NAMED ENTITIES (Concepts, Terms, Algorithms)

- **Machine Learning**: A computer observes data, builds a model from data, and uses the model as both a hypothesis about the world and a piece of software that can solve problems.
- **Induction**: Going from a specific set of observations to a general rule (may be incorrect, unlike deduction).
- **Classification**: Learning problem where output is one of a finite set of values.
- **Regression**: Learning problem where output is a number (integer or real).
- **Supervised Learning**: Agent observes input-output pairs and learns a function mapping input to output.
- **Unsupervised Learning**: Agent learns patterns in input without explicit feedback; most common task is clustering.
- **Reinforcement Learning**: Agent learns from a series of reinforcements (rewards and punishments).
- **Label**: Output value in supervised learning accompanying each input.
- **Training set**: Set of N example input–output pairs.
- **Hypothesis space (H)**: Set of possible functions the hypothesis h is drawn from.
- **Model class / Function class**: Alternative names for hypothesis space.
- **Ground truth**: The true answer the model is asked to predict.
- **Exploratory data analysis**: Examining data with statistical tests and visualizations.
- **Consistent hypothesis**: h such that h(xi) = yi for each xi in the training set.
- **Test set**: Second sample of (xi, yi) pairs to evaluate generalization.
- **Generalization**: How well h predicts outputs for the test set.
- **Bias**: Tendency of a predictive hypothesis to deviate from expected value when averaged over different training sets.
- **Variance**: Amount of change in hypothesis due to fluctuation in training data.
- **Underfitting**: When hypothesis fails to find a pattern in the data.
- **Overfitting**: When hypothesis pays too much attention to the particular data set it is trained on.
- **Bias–variance tradeoff**: Choice between complex low-bias hypotheses that fit training data well and simpler low-variance hypotheses that generalize better.
- **Ockham's Razor**: "Plurality [of entities] should not be posited without necessity" — choose simplest hypothesis matching data.
- **Decision tree**: Representation of a function mapping a vector of attribute values to a single output value via sequence of tests.
- **Positive example / Negative example**: Boolean classification outputs true/false.
- **Noise**: Errors or nondeterminism in data causing conflicting classifications for same description.
- **Entropy (H(V))**: Measure of uncertainty of a random variable. H(V) = -Σ_k P(v_k) log₂ P(v_k).
- **Information gain**: Expected reduction in entropy from an attribute test.
- **Decision tree pruning**: Eliminating nodes that are not clearly relevant to combat overfitting.
- **χ² pruning**: Statistical significance test to decide if attribute is irrelevant and should be pruned.
- **Null hypothesis**: Assumption that there is no underlying pattern.
- **Early stopping**: Stopping tree generation when there is no good attribute to split on (problematic because it misses XOR-like patterns).
- **Split point**: Inequality test on a continuous attribute value (e.g., Weight > 160).
- **Regression tree**: Decision tree with a linear function at each leaf for numerical output.
- **CART**: Classification And Regression Trees.
- **Unstable**: Decision trees are unstable — adding one example can change the root.
- **Stationarity assumption**: Future examples will be like the past; each example has same prior probability distribution.
- **I.i.d.**: Independent and identically distributed.
- **Error rate**: Proportion of times h(x) ≠ y for an (x, y) example.
- **Hyperparameters**: Parameters of the model class, not of the individual model.
- **Validation set / Development set / Dev set**: Set to evaluate candidate models and choose the best one.
- **k-fold cross-validation**: Split data into k equal subsets; each round 1/k held out as validation, rest as training.
- **LOOCV (Leave-One-Out Cross-Validation)**: k = n, extreme case of cross-validation.
- **Model selection**: Choosing a good hypothesis space.
- **Optimization (Training)**: Finding the best hypothesis within that space.
- **Loss function**: Specifies how bad each error is (generalization of error rate).
- **L₁ regularization / L₂ regularization**: Penalty terms added to loss to prevent overfitting.
- **Regularization**: Adding a penalty for model complexity to the loss function.
- **Linear regression**: Model where output is a linear function of inputs.
- **Closed-form solution / Normal equations**: Direct formula for optimal weights without iterative search.
- **Gradient descent**: Iterative method to minimize loss by moving in direction of negative gradient.
- **Convex function**: Function with one global minimum; gradient descent guaranteed to reach it.
- **Batching / Full batch**: Gradient descent using all training examples per step.
- **Minibatch / Stochastic gradient descent (SGD)**: Gradient descent using small random subsets per step.
- **Learning rate**: Step size in gradient descent.
- **Logistic function / Sigmoid**: σ(x) = 1/(1 + e^{-x}), maps any input to (0, 1).
- **Logistic regression**: Linear classifier with soft threshold defined by logistic function.
- **Perceptron**: Linear classifier with hard threshold.
- **Perceptron convergence theorem**: If data are linearly separable, the perceptron algorithm will find a separating hyperplane.
- **Nonparametric models**: Models that use all data to make each prediction; don't summarize data with few parameters.
- **Nearest neighbors / k-nearest neighbors (kNN)**: Query point classified by majority vote of k nearest neighbors in training set.
- **Locality-sensitive hashing (LSH)**: Hashes input points so nearby points map to same bucket with high probability.
- **Locally weighted regression**: Nonparametric regression; weights training points by distance to query.
- **Kernel function / Kernelization**: Implicitly map input to high-dimensional space where a linear separator exists.
- **Kernel trick**: Using kernels without explicit high-dimensional mapping.
- **Support vector machine (SVM)**: Finds linear separators with maximum margin.
- **Soft margin classifier**: Allows some misclassifications in SVM for noisy data.
- **Ensemble learning**: Combining multiple learning algorithms.
- **Bagging (Bootstrap aggregating)**: Generate K distinct training sets by sampling with replacement, train K hypotheses, aggregate by vote/average.
- **Random forest**: Decision tree bagging plus random attribute selection at each split.
- **Extremely randomized trees (ExtraTrees)**: Random sampling of split point values in addition to random attribute selection.
- **Out-of-bag error**: Mean error on each example using only trees whose training set didn't include that example.
- **Stacked generalization (Stacking)**: Combine multiple base models from different model classes.
- **Boosting**: Sequential ensemble method reweighting training examples.
- **Weighted training set**: Each example has associated weight w_j ≥ 0.
- **Weak learning algorithm**: Always returns hypothesis with accuracy slightly better than random guessing.
- **Decision stump**: Decision tree with just one test (root).
- **AdaBoost**: Popular boosting algorithm; boosts weak learner.
- **Gradient boosting / GBM / GBRT**: Boosting using gradient descent.
- **XGBoost**: Popular gradient boosting package.
- **Online learning**: Agent receives inputs sequentially, predicts, is told correct answer; data may not be i.i.d.
- **Randomized weighted majority algorithm**: Pool predictions from experts weighted by past performance.
- **Regret**: Number of additional mistakes compared to best expert in hindsight.
- **No-regret learning**: Average regret per trial tends to 0 as trials increase.
- **Semisupervised learning**: Few labeled examples used to mine information from large collection of unlabeled examples.
- **Weakly supervised learning**: Using labels that are noisy, imprecise, or supplied by non-experts.
- **ImageNet**: Freely available image data set with over 14 million photos with ~20,000 labels.
- **Data provenance**: Knowing exact definition, source, possible values, and history for each column.
- **Data augmentation**: Creating multiple versions of each image by rotation, translation, cropping, scaling, etc.
- **Unbalanced classes**: Some classes have many more examples than others.
- **Undersampling / Oversampling**: Techniques to handle unbalanced classes.
- **Outlier**: Data point far from other points.
- **One-hot encoding**: Transforming categorical attribute into separate Boolean attributes.
- **t-distributed stochastic neighbor embedding (t-SNE)**: Dimensionality reduction for visualization.
- **False positive / False negative**: Classification errors.
- **ROC curve (Receiver Operating Characteristic)**: Plots false positives vs true positives for different hyperparameter values.
- **AUC**: Area Under the ROC Curve, single-number summary.
- **Confusion matrix**: Two-dimensional table of misclassification counts.
- **Interpretability**: Ability to inspect model and understand why it got a particular answer.
- **Explainability**: Ability of a separate process to summarize what the model does.
- **LIME (Local Interpretable Model-agnostic Explanations)**: Builds interpretable linear model approximating the black-box model.
- **Long tail**: In popular systems, inputs that were never tested before.
- **Monitoring**: Tracking statistics on live data.
- **Nonstationarity**: World changes over time; spam evolves.
- **Learning curve (Happy graph)**: Plot of prediction accuracy vs training set size.
- **Kolmogorov complexity / Algorithmic complexity**: Length of shortest program for a universal Turing machine reproducing observed data.
- **PAC learning (Probably Approximately Correct)**: Theoretical framework for sample complexity (Valiant, 1984).
- **VC dimension**: Measure of capacity of a function class (Vapnik-Chervonenkis).
- **No free lunch theorem**: If a learning algorithm performs well on a certain set of problems, it performs poorly on a different set.
- **Automated machine learning (AutoML) / Metalearning**: Applying ML to the task of solving ML problems.

### 2. SEQUENTIAL PROCESSES (Algorithms & Procedures)

#### LEARN-DECISION-TREE Algorithm (Figure 19.5)
1. If examples is empty, return PLURALITY-VALUE(parent_examples).
2. Else if all examples have same classification, return that classification.
3. Else if attributes is empty, return PLURALITY-VALUE(examples).
4. Else:
   a. A ← argmax_{a in attributes} IMPORTANCE(a, examples)
   b. Tree ← new decision tree with root test A
   c. For each value v of A:
      - exs ← {e: e in examples and e.A = v}
      - subtree ← LEARN-DECISION-TREE(exs, attributes - A, examples)
      - Add branch (A = v) with subtree
   d. Return tree

#### Maximum-Likelihood Parameter Learning Method (3 steps)
1. Write down expression for likelihood of data as function of parameter(s).
2. Write down derivative of log likelihood with respect to each parameter.
3. Find parameter values such that derivatives are zero.

#### AdaBoost Algorithm (Figure 19.25)
1. Initialize weights w_j = 1/N for all N examples.
2. For k = 1 to K:
   a. h[k] ← L(examples, w) // train on weighted examples
   b. error ← 0; for j=1..N: if h[k](x_j) ≠ y_j then error += w[j]
   c. If error > 1/2, break
   d. error ← min(error, 1-ε)
   e. For j=1..N: if h[k](x_j)=y_j then w[j] ← w[j]·error/(1-error)
   f. Normalize w
   g. z[k] ← ½ log((1-error)/error) // hypothesis weight
3. Return h(x) = Σ z_i h_i(x)

#### Randomized Weighted Majority Algorithm (Online Learning)
1. Initialize weights {w₁,...,w_K} all to 1.
2. For each problem:
   a. Receive predictions {ŷ₁,...,ŷ_K} from experts.
   b. Randomly choose expert k* in proportion to its weight: P(k) = w_k.
   c. Yield ŷ_{k*} as the answer.
   d. Receive correct answer y.
   e. For each expert k where ŷ_k ≠ y, update w_k ← β w_k.
   f. Normalize weights.

#### Model Selection Algorithm (Figure 19.8)
1. Split examples into training set and test set.
2. For size = 1 to ∞:
   a. err[size] ← CROSS-VALIDATION(Learner, size, training set, k)
   b. If err is starting to increase significantly, stop.
3. best_size ← value with minimum err[size].
4. h ← Learner(best_size, training set).
5. Return h, ERROR-RATE(h, testset).

#### CROSS-VALIDATION function:
1. N ← number of examples. errs ← 0.
2. For i = 1 to k:
   a. validation_set ← examples[(i-1)×N/k : i×N/k]
   b. training_set ← examples - validation_set
   c. h ← Learner(size, training_set)
   d. errs ← errs + ERROR-RATE(h, validation_set)
3. Return errs/k.

### 3. HIERARCHIES / CLASSIFICATIONS

**Forms of Learning** (based on feedback):
- Supervised Learning (input-output pairs)
- Unsupervised Learning (patterns without feedback)
- Reinforcement Learning (rewards/punishments)

**Components of Agents That Can Be Learned** (7 components):
1. Direct mapping from conditions to actions
2. Means to infer relevant properties from percept sequence
3. Information about world evolution and action results
4. Utility information (desirability of states)
5. Action-value information (desirability of actions)
6. Goals (most desirable states)
7. Problem generator, critic, and learning element

**Types of Model Classes Covered**:
- Decision Trees (19.3)
- Linear Models (19.6)
- Nonparametric Models (kNN, locally weighted regression) (19.7)
- Ensemble Models (random forests, bagging, boosting) (19.8)
- Neural Networks/Deep Learning (Chapter 21)

**Ensemble Methods Taxonomy**:
- Bagging: same model class, different data (parallel)
- Random Forests: bagging + random attribute selection (parallel)
- Stacking: different model classes, same data
- Boosting: sequential reweighting (AdaBoost, Gradient Boosting)

### 4. COMPARISONS / TRADE-OFFS

- **Bias vs Variance**: Simple models → high bias, low variance; complex models → low bias, high variance. Trade-off: choose complex enough to fit patterns but simple enough to generalize.
- **Expressiveness vs Computational Complexity**: More expressive hypothesis spaces require more computation to find good hypothesis; e.g., linear fit is easy, Turing machines are undecidable.
- **ADP vs TD**: ADP uses full transition model and Bellman equations (better but expensive); TD uses single observed successor (simpler, less computation).
- **Bagging vs Boosting**: Bagging is parallel (independent hypotheses) and reduces variance; boosting is sequential, focuses on hard examples.
- **Deep vs Shallow Networks**: Deep (many layers) with relatively narrow vs shallow and wide. Deep often generalizes better for similar total weight count.
- **Decision Trees vs Neural Networks**: Trees are interpretable but less accurate with greedy search; NNs can represent complex functions but are not interpretable.
- **Generative vs Discriminative Models**: Generative models learn P(X,Y) and can generate samples; discriminative models learn P(Y|X) and focus on decision boundary.
- **Batch vs Stochastic Gradient Descent**: Batch is exact but slow for large datasets; SGD is fast and stochasticity helps escape local minima.

### 5. FORMULAS & EQUATIONS

**Entropy of a random variable V**:
H(V) = -Σ_k P(v_k) log₂ P(v_k)

**Boolean entropy function B(q)**:
B(q) = -(q log₂ q + (1-q) log₂ (1-q))

**Remainder after attribute test A**:
Remainder(A) = Σ_{k=1}^{d} (p_k + n_k)/(p+n) · B(p_k/(p_k+n_k))

**Information gain**:
Gain(A) = B(p/(p+n)) - Remainder(A)

**Chi-squared deviation**:
Δ = Σ_{k=1}^{d} [(p_k - p̂_k)² / p̂_k + (n_k - n̂_k)² / n̂_k]
where p̂_k = p × (p_k+n_k)/(p+n), n̂_k = n × (p_k+n_k)/(p+n)

**Linear regression hypothesis**:
h_w(x) = w·x = Σ_{i=0}^{n} w_i x_i

**Squared error loss**:
Loss(h_w) = ½ Σ_j (y_j - h_w(x_j))²

**Gradient descent update**:
w ← w - α ∇_w Loss(h_w)

**Gradient of squared error** (for linear regression):
∂Loss/∂w_i = Σ_j (h_w(x_j) - y_j) x_j_i

**Logistic function**:
σ(x) = 1/(1 + e^{-x})

**Logistic regression form**:
P(y=1|x) = σ(w·x)
P(y=0|x) = 1 - σ(w·x)

**Logistic regression derivative**:
∂Loss/∂w_i = Σ_j (σ(w·x_j) - y_j) x_j_i

**L₂ regularization term**:
Loss = original loss + (λ/2) Σ_i w_i²

**L₁ regularization term**:
Loss = original loss + λ Σ_i |w_i|

**SVM maximum margin separator**: maximize margin = 2/||w||, subject to y_j(w·x_j + b) ≥ 1 for all j.

**Soft margin**: allow slack variables ξ_j ≥ 0, minimize (1/2)||w||² + C Σ_j ξ_j.

**Bagging prediction (regression)**:
h(x) = (1/K) Σ_{i=1}^{K} h_i(x)

**AdaBoost hypothesis weight**:
z[k] = ½ log((1-error)/error)

**Regret bound for weighted majority**:
M < (M* ln(1/β) + ln K) / (1-β)

### 6. RULES, LAWS & THEOREMS

- **Ockham's Razor**: "Plurality [of entities] should not be posited without necessity" — prefer simpler hypotheses.
- **Einstein's principle**: "The supreme goal of all theory is to make the irreducible basic elements as simple and as few as possible without having to surrender the adequate representation of a single datum of experience."
- **Perceptron Convergence Theorem**: If data are linearly separable, the perceptron algorithm will find a separating hyperplane in a finite number of steps.
- **Universal Approximation Theorem**: A network with just two layers (first nonlinear, second linear) can approximate any continuous function to arbitrary accuracy (Cybenko 1988, 1989).
- **No Free Lunch Theorem** (Wolpert & Macready): If a learning algorithm performs well on a certain set of problems, it must perform poorly on a different set.
- **Stationarity assumption** (Uniformity of Nature): Future examples will be like the past; P(E_j) = P(E_{j+1}) = P(E_{j+2}) = ... and P(E_j) = P(E_j | E_{j-1}, E_{j-2}, ...).
- **Condorcet's Jury Theorem** (1785): If jurors are independent and each has >50% chance of being correct, more jurors improve the chance of correct decision.
- **No-regret property**: For weighted majority, average regret per trial tends to 0 as number of trials increases.

### 7. DATA STRUCTURES & TYPES

- **Decision tree**: Internal nodes test attributes; branches labeled with values; leaves specify output value. Efficient for Boolean classification.
- **Weight vector w** for linear models: dimensionality = number of input features + 1 (bias).
- **Distance metrics** for kNN: Euclidean (standard), Manhattan, Minkowski, Mahalanobis.
- **LSH (Locality-Sensitive Hashing)**: Maps points to buckets; nearby points map to same bucket with high probability.
- **Kernel matrices**: Symmetric positive semidefinite; Gram matrix K_ij = K(x_i, x_j).

### 8. VISUAL PATTERNS

- **Figure 19.1**: Four columns of best-fit functions from different hypothesis spaces (line, sinusoidal, piecewise linear, degree-12 polynomial) on two slightly different data sets. Shows bias and variance differences.
- **Figure 19.2**: Restaurant domain example table — 12 examples with 10 attributes (Alternate, Bar, Fri/Sat, Hungry, Patrons, Price, Raining, Reservation, Type, WaitEstimate) and output WillWait.
- **Figure 19.3**: A decision tree for deciding whether to wait at a restaurant.
- **Figure 19.4**: Splitting examples by Type (poor — no separation) vs Patrons (good — separates positive/negative).
- **Figure 19.7**: Learning curve (happy graph) — proportion correct on test set vs training set size.
- **Figure 19.9**: Model selection curves — training set error decreases monotonically; validation set error decreases then increases (U-shaped) for overfitting-prone models, or decreases monotonically to asymptote for robust models (like random forests).
- **Figure 19.23**: An ensemble of three linear classifiers can represent a triangular region.
- **Figure 19.24**: Boosting illustration: shaded rectangles for examples, height = weight; checks/crosses = correct/wrong.
- **Figure 19.26**: Boosted decision stumps vs unboosted; test accuracy continues improving even after training error hits zero.
- **Figure 19.27**: t-SNE map of MNIST digit data set; 10 clear clusters with some confusions.

### 9. EDGE CASES / EXCEPTIONS / TRAPS

- **Decision trees and XOR**: No single attribute is informative for XOR; early stopping fails; generate-and-then-prune handles it.
- **Majority function**: Requires exponentially large decision tree.
- **Parity function**: Requires exponentially large decision tree.
- **Diagonal decision boundary** (e.g., y > A₁ + A₂): Hard to represent with axis-aligned decision tree tests.
- **Small data sets**: Maximum-likelihood assigns zero probability to unseen events (mitigating by initializing counts to 1).
- **Unbalanced classes**: 99.99% accuracy trivial if one class dominates; need undersampling, oversampling, or weighted loss.
- **Outliers in linear regression**: Single outlier can significantly affect all parameters.
- **Missing data**: Classification with missing test attribute values; information gain with partially unknown attributes.
- **Continuous attributes**: Information gain highest for values with many distinct values (fix: split point tests, information gain ratio).
- **Early stopping problem**: Prevents recognizing XOR-like patterns where no single attribute is good.
- **Decision tree instability**: Adding one new example can change the test at the root, changing entire tree.
- **Gradient descent on non-convex functions**: Can converge to local minimum (not guaranteed global).
- **ε-insensitive in SVM**: Training error below ε is tolerated; points inside margin "cost" proportional to distance from boundary.
- **Boosting and overfitting**: Test accuracy continues to improve after training error reaches 0 (contradicts Ockham).
- **Deep unpruned random forests**: Resistant to overfitting (error converges as trees added, but may not go to zero).

### 10. EMPIRICAL EVIDENCE / KEY RESULTS

- **Hezaveh et al. (2017)**: ML model sped up gravitational lensing image analysis by factor of 10 million.
- **Gao (2014)**: ML model reduced data center cooling energy use by 40%.
- **Dean et al. (2018)**: Declared "Golden Age" for computer architecture due to ML.
- **Restaurant learning curve**: 95% accuracy reached; curve may continue increasing with more data.
- **Random forests in Kaggle**: Most popular approach of winning teams 2011–2014.
- **Kaggle 2015**: Every team in top 10 of KDD Cup used XGBoost.
- **Boosting decision stumps performance**: Unboosted: 81%; boosted (K=5): 93% on restaurant data.
- **Boosting test accuracy**: Continues increasing long after training error reaches 0 (at K=20 test performance 0.95, increases to 0.98 at K=137).
- **Regret bound example**: With K=10 experts, β=1/2 → mistakes bounded by 1.39M* + 4.6; β=3/4 → 1.15M* + 9.2.

### 11. CROSS-CHAPTER DEPENDENCIES

- Cross-ref to **Chapter 7** (deduction vs induction; wumpus world agent)
- Cross-ref to **Chapter 2** (agent designs)
- Cross-ref to **Chapter 8** (first-order logic expressiveness)
- Cross-ref to **Chapter 16** (utility of money is logarithmic)
- Cross-ref to **Chapter 20** (Bayesian learning)
- Cross-ref to **Chapter 21** (deep learning; transfer learning)
- Cross-ref to **Section 27.3.2** (privacy), **Section 27.3.3** (fairness)

### 12. DATES & PEOPLE

- **Albert Einstein** (1933): "supreme goal of all theory is to make the irreducible basic elements as simple and as few as possible"
- **William of Ockham** (1280–1349): Ockham's Razor
- **Francis Galton** (1886): "regression to the mean"
- **Claude Shannon & Warren Weaver** (1949): information theory
- **Alan Turing** (1947): anticipated machine learning
- **Arthur Samuel** (1959): defined "machine learning"; checkers program
- **Edward Feigenbaum** (1961): EPAM decision tree system
- **Ross Quinlan** (1979): ID3 with maximum entropy attribute selection; later C4.5
- **Leo Breiman et al.** (1984): CART; later Random Forests (2001)
- **Leslie Valiant** (1984): PAC learning
- **Vapnik & Chervonenkis** (1971): VC dimension
- **Legendre** (1805) & **Gauss** (1809): linear regression
- **Pierre-François Verhulst** (1804–1849): logistic function
- **Richard Bellman** (1961): "curse of dimensionality"
- **Cauchy** (1847): gradient descent
- **Robbins & Monro** (1951): stochastic gradient descent
- **Frank Rosenblatt** (1957, 1960): perceptron; perceptron convergence theorem
- **Freund & Schapire** (1996): AdaBoost
- **Friedman** (2001): Gradient Boosting Machine
- **Breck et al.** (2016): ML testing rubric
- **Domingos** (2012): "most important factor is the features used"
- **John Tukey** (1977): exploratory data analysis (EDA)
- **David Hume** (1711–1776): problem of induction; uniformity of nature principle
- **Pierre-Simon Laplace**: Laplace smoothing

### 13. PROOF & ARGUMENT PATTERNS

**Expressiveness of decision trees**: Any Boolean function can be expressed as a decision tree (DNF form) because output ⇔ (Path₁ ∨ Path₂ ∨ ...) where each Path is a conjunction of attribute tests.

There are 2^{2^n} different Boolean functions with n Boolean attributes, so no representation can be efficient for all functions using a small number of bits.

**χ² pruning logic**: Null hypothesis → attribute irrelevant → information gain would be zero for infinite sample. Compute expected counts under null; compare actual deviation to χ² distribution with d-1 degrees of freedom.

**Bootstrapping/Bagging variance reduction**: Ensemble of 5 independent classifiers each correct 75% individually → majority vote correct 89% (assuming independence). With 17 classifiers → 99%.

**AdaBoost weak learner property**: If L always returns hypothesis with accuracy > 50% + ε on training set, AdaBoost will classify training data perfectly for large enough K. Proof in Freund & Schapire (1996).

**No-regret bound for weighted majority**: M < (M* ln(1/β) + ln K)/(1-β) holds for any sequence of examples, even adversarial.

### 14. DESIGN PARADIGMS / META-METHODS

- **Greedy divide-and-conquer**: Decision tree learning (test most important attribute first, solve subproblems recursively).
- **Gradient descent in parameter space**: Linear/logistic regression, neural networks.
- **Stochastic approximation**: SGD updates on minibatches.
- **Bootstrap aggregation (Bagging)**: Reduce variance by resampling and averaging.
- **Boosting**: Sequential reweighting to focus on hard examples.
- **Occam's Razor** (parsimony): Simpler hypotheses preferred.
- **Kernel trick**: Implicit high-dimensional mapping without explicit computation.
- **Cross-validation**: Reuse limited data for model selection.
- **End-to-end learning** (Chapter 21): Complex system trained from input/output pairs without manual subsystem design.

### 15. CASE STUDIES / CLASSIC EXAMPLES

**Restaurant waiting problem** (running example throughout chapter):
- 10 attributes, 12 training examples, 9,216 possible input combinations.
- Decision tree learning on this data yields tree with Patrons at root, then Hungry, Fri/Sat, Type.
- Learning curve reaches ~95% accuracy.

**Spam email classification**: 
- False positive vs false negative tradeoff; ROC curve.
- As spam evolves, models become stale (nonstationarity).

**Photo identification project**:
- ImageNet (14M photos, 20,000 labels).
- One-hot encoding for categorical attributes.
- Data augmentation (rotate, translate, crop, scale, change brightness/color).
- Transfer learning with pretrained models.

### 16. ETHICS

- **Privacy**: Federated learning approach where data stays on user's device; review with privacy experts; proper permission for data collection.
- **Fairness**: Ensure processes are fair and unbiased; fairness reviews; inclusion testing.
- **Accountability**: What happens when system is wrong? Process for complaining/appealing decisions; tracking responsibility.
- **GDPR (General Data Protection Regulation)**: Requires systems to provide explanations.
- **Trust**: Build trust with source control, testing, review, monitoring, accountability.
- **Explainability vs Interpretability**: Regulations require explanations; but explanations can lead to false sense of security.

### 17. END-OF-CHAPTER MATERIAL

**Summary Key Points**:
- Learning takes many forms depending on agent component to improve and available feedback.
- Supervised learning: learn y = h(x). Regression (continuous output), classification (discrete).
- Need to balance agreement with data vs simplicity (generalization).
- Decision trees represent all Boolean functions; information gain heuristic.
- Learning curve shows prediction accuracy vs training set size.
- Model selection via cross-validation; hyperparameters on validation set.
- Loss function specifies how bad each error is.
- Computational learning theory: sample complexity vs expressiveness tradeoff.
- Linear regression: closed form or gradient descent.
- Perceptron: hard threshold; converges for linearly separable data.
- Logistic regression: soft threshold; gradient descent works for noisy/nonseparable data.
- Nonparametric models: kNN, locally weighted regression.
- SVMs: maximum margin separators; kernel trick.
- Ensemble methods: bagging, boosting.
- Building ML systems: data management, model selection, testing, monitoring.

---

## CHAPTER 20: LEARNING PROBABILISTIC MODELS

### 1. NAMED ENTITIES

- **Bayesian learning**: Calculates probability of each hypothesis given data; predictions use all hypotheses weighted by probabilities.
- **Hypothesis prior P(h_i)**: Prior probability of each hypothesis before seeing data.
- **Likelihood P(d|h_i)**: Probability of data under each hypothesis.
- **Maximum a posteriori (MAP)**: Single most probable hypothesis maximizing P(h_i|d).
- **Maximum-likelihood (ML) hypothesis h_ML**: Hypothesis maximizing P(d|h_i); equivalent to MAP with uniform prior.
- **Minimum description length (MDL)**: Learning method counting bits in binary encoding of hypotheses and data.
- **Density estimation**: General task of learning a probability model from data assumed to be generated from that model.
- **Complete data**: Each data point contains values for every variable in the model.
- **Parameter learning**: Finding numerical parameters for a probability model with fixed structure.
- **Log likelihood**: L(d|h_θ) = log P(d|h_θ) = Σ_j log P(d_j|h_θ), easier to maximize than raw likelihood.
- **Naive Bayes model**: "Class" variable is root; "attribute" variables are leaves; attributes conditionally independent given class.
- **Generative model**: Models probability distribution of each class (e.g., naive Bayes).
- **Discriminative model**: Learns decision boundary P(Category|Inputs) (e.g., logistic regression, decision trees, SVM).
- **Beta distribution**: Beta(θ; a, b) = α θ^{a-1} (1-θ)^{b-1} for θ∈[0,1]; conjugate prior for Bernoulli variable.
- **Hyperparameter**: Parameters a and b of beta distribution parameterize distribution over θ.
- **Conjugate prior**: Prior such that posterior is in same family as prior (Beta is conjugate for Bernoulli).
- **Virtual counts**: a and b hyperparameters behave as if seen a-1 cherry and b-1 lime candies.
- **Parameter independence**: P(Θ, Θ₁, Θ₂) = P(Θ)P(Θ₁)P(Θ₂).
- **Uninformative prior**: Prior that expresses ignorance (e.g., zero mean, large variance Gaussian).
- **Nonparametric density estimation**: Learning probability model without assumptions about its structure/parameterization.
- **Latent variable (Hidden variable)**: Variable not observable in data.
- **Expectation-maximization (EM)**: Algorithm for learning with hidden variables.
- **Unsupervised clustering**: Discerning multiple categories in collection of objects (no labels).
- **Mixture distribution**: P(x) = Σ_{i=1}^{k} P(C=i) P(x|C=i).
- **Component**: Each distribution in a mixture.
- **Mixture of Gaussians**: Each component is a multivariate Gaussian.
- **Indicator variable Z_ij**: 1 if datum x_j generated by component i, 0 otherwise.
- **Identifiability**: Whether parameters can be uniquely recovered from data.
- **Dirichlet process**: Distribution over Dirichlet distributions for nonparametric Bayes.
- **Gaussian process**: Defines prior distributions over space of continuous functions.
- **Structural EM**: EM algorithm that updates structure as well as parameters.
- **Kernel density estimation (Parzen window)**: P(x) = (1/N) Σ_j K(x, x_j).

### 2. SEQUENTIAL PROCESSES

**Bayesian Learning (Conceptual Process)**:
1. Start with hypothesis prior P(h_i).
2. Observe data d.
3. Compute posterior P(h_i|d) = α P(d|h_i) P(h_i) by Bayes' rule.
4. For prediction: P(X|d) = Σ_i P(X|h_i) P(h_i|d).

**Maximum-Likelihood Parameter Learning Method** (3 Steps):
1. Write likelihood expression as function of parameters.
2. Write derivative of log likelihood with respect to each parameter.
3. Find parameter values setting derivatives to zero.

**EM Algorithm for Mixture of Gaussians**:
1. Initialize mixture-model parameters arbitrarily.
2. Iterate:
   a. **E-step**: Compute p_ij = P(C=i|x_j) by Bayes' rule. Compute n_i = Σ_j p_ij.
   b. **M-step**: 
      μ_i ← Σ_j p_ij x_j / n_i
      Σ_i ← Σ_j p_ij (x_j - μ_i)(x_j - μ_i)^⊤ / n_i
      w_i ← n_i / N

**Computation of Bayes Net Parameters with EM**:
θ_ijk ← N̂(X_i=x_ij, U_i=u_ik) / N̂(U_i=u_ik)
where expected counts are obtained by summing over examples.

**Bayes Net Structure Learning Approaches**:
1. **Conditional independence testing**: Check if independence assertions hold in data.
2. **Likelihood-based**: Penalize model complexity (MAP/MDL).

### 3. HIERARCHIES / CLASSIFICATIONS

**Learning Paradigms (Statistical)**:
- **Bayesian learning**: All hypotheses weighted by posterior.
- **MAP learning**: Single most probable hypothesis (maximizes P(h|d)).
- **ML learning**: Maximizes P(d|h) (uniform prior on hypotheses).

**Model Types for Learning**:
- **Parametric models**: Fixed number of parameters (e.g., Gaussian, linear regression).
- **Nonparametric models**: Parameters grow with data (kNN, kernel density estimation).

**Learning with Data Completeness**:
- **Complete data**: All variables observed.
- **Incomplete data**: Some variables hidden → EM algorithm.

**Generative vs Discriminative**:
| Aspect | Generative | Discriminative |
|--------|-----------|---------------|
| What it models | P(X,Y) joint | P(Y|X) conditional |
| Can generate samples? | Yes | No |
| Better with limited data? | Often yes | No |
| Better asymptotically? | No | Often yes |
| Examples | Naive Bayes, HMM | Logistic regression, SVM, decision trees |

### 4. COMPARISONS / TRADE-OFFS

- **Bayesian vs MAP**: Bayesian uses all hypotheses (optimal), MAP uses one (approximate, but easier computationally).
- **MAP vs ML**: MAP includes prior (Ockham's razor); ML assumes uniform prior (good with large data where prior is swamped).
- **Bayesian vs Frequentist**: Bayesian uses subjective priors; frequentist/ML avoids them.
- **Complexity vs Degree of Fit**: More complex hypotheses fit training data better but generalize worse; prior/complexity penalty balances tradeoff.
- **Maximum-likelihood with small vs large data**: Small data can give zero probabilities for unseen events; large data swamps the prior.
- **Generative vs Discriminative (Ng & Jordan 2002)**: With maximum data, discriminative better on 9/15 data sets; with limited data, generative better on 14/15.
- **Tabular vs Noisy-OR complexity penalty**: Tabular grows exponentially with number of parents; noisy-OR grows linearly → learning produces different structures.
- **Complete data vs Hidden variables parameter learning**: Complete data → closed-form frequency counts; hidden variables → iterative EM or gradient methods.

### 5. FORMULAS & EQUATIONS

**Bayes' rule for hypotheses**:
P(h_i|d) = α P(d|h_i) P(h_i)   (20.1)

**Bayesian prediction**:
P(X|d) = Σ_i P(X|h_i) P(h_i|d)   (20.2)

**Likelihood for i.i.d. data**:
P(d|h_i) = ∏_j P(d_j|h_i)   (20.3)

**Maximum-likelihood for Bernoulli (cherry/lime)**:
θ = c/(c + ℓ) = c/N

**Log likelihood for Bernoulli**:
L(d|h_θ) = c log θ + ℓ log (1-θ)

**Maximum-likelihood for wrapper+flavor model**:
θ = c/(c+ℓ), θ₁ = r_c/(r_c+g_c), θ₂ = r_ℓ/(r_ℓ+g_ℓ)

**Naive Bayes parameters**:
θ = P(C=true), θ_{i1} = P(X_i=true|C=true), θ_{i2} = P(X_i=true|C=false)

**Naive Bayes classification**:
P(C|x₁,...,x_n) = α P(C) ∏_i P(x_i|C)

**Gaussian density**:
P(x) = (1/(σ√(2π))) e^{-(x-μ)²/(2σ²)}

**Maximum-likelihood for Gaussian**:
μ = (Σ_j x_j)/N
σ = √(Σ_j (x_j-μ)² / N)   (20.4)

**Linear-Gaussian conditional**:
P(y|x) = (1/(σ√(2π))) e^{-(y-(θ₁x+θ₂))²/(2σ²)}   (20.5)

**Beta distribution**:
Beta(θ; a, b) = α θ^{a-1} (1-θ)^{b-1}   (20.6)
Mean = a/(a+b)

**Bayesian linear regression posterior**:
P(θ|d) ∝ e^{-½((θ-θ₀)²/σ₀² + Σ_i((y_i-θx_i)²/σ²))}
θ_N = (σ²θ₀ + σ₀² Σ_i x_i y_i) / (σ² + σ₀² Σ_i x_i²)
σ_N² = σ²σ₀² / (σ² + σ₀² Σ_i x_i²)

**Bayesian linear regression predictive**:
P(y|x,d) ∝ e^{-½((y-θ_N x)²/(σ²+σ_N² x²))}

**Kernel density estimation**:
P(x) = (1/N) Σ_j K(x, x_j)
where K(x,x_j) = 1/(w²√(2π))^d e^{-D(x,x_j)²/(2w²)}

**Mixture distribution**:
P(x) = Σ_{i=1}^{k} P(C=i) P(x|C=i)

**General EM algorithm**:
θ^{(i+1)} = argmax_θ Σ_z P(Z=z|x,θ^{(i)}) L(x, Z=z|θ)

### 6. RULES, LAWS & THEOREMS

- **Ockham's Razor via MAP**: MAP chooses simplest logical theory consistent with data — natural embodiment of Ockham's razor.
- **MAP = Minimum Description Length**: Choosing h_MAP minimizes -log₂ P(d|h_i) - log₂ P(h_i), which equals total bits to encode hypothesis + data.
- **Bayesian prediction optimality**: Given hypothesis prior, any other prediction is expected to be correct less often.
- **Bayesian convergence**: Posterior probability of false hypotheses eventually vanishes for fixed prior that does not rule out true hypothesis.
- **Complete data decomposition**: ML parameter learning for Bayesian network decomposes into separate learning problems for each parameter.
- **Beta is conjugate prior for Bernoulli**: Beta(a,b) prior → Beta(a+1,b) after cherry, Beta(a,b+1) after lime.
- **EM monotonically increases log likelihood**: EM increases log likelihood at every iteration; under certain conditions reaches local maximum.
- **Identifiability**: A model with two attributes and five parameters from three observed counts is not identifiable.

### 7. DATA STRUCTURES & TYPES

- **Beta(a,b)**: Distribution over θ ∈ [0,1]; mean = a/(a+b); peaks as a+b increases.
- **Bayesian network for learning**: Derived network where data and parameters become nodes; one learning algorithm = inference algorithm for Bayesian networks.
- **AD-tree**: Efficient data structure for caching counts over all variable/value combinations.
- **Gaussian mixture model**: Parameters: w_i (weights), μ_i (means), Σ_i (covariances).

### 8. VISUAL PATTERNS

- **Figure 20.1**: Posterior probabilities of 5 hypotheses change as 10 lime candies observed; h₃ starts most likely, h₅ becomes most likely after 3 limes. Prediction probability of next lime increases monotonically toward 1.
- **Figure 20.2**: (a) Simple BN for candy with unknown θ (cherry proportion). (b) BN with wrapper color depending probabilistically on flavor (θ, θ₁, θ₂).
- **Figure 20.3**: Learning curve for naive Bayes on restaurant problem; decision tree learning curve shown for comparison — decision tree does better.
- **Figure 20.4**: Linear-Gaussian model y = θ₁x + θ₂ + Gaussian noise; 50 data points and best-fit line.
- **Figure 20.5**: Beta(a,b) distributions for different (a,b): Beta(1,1) uniform; Beta(2,2) peaked at 0.5; Beta(3,1) skewed toward 1.
- **Figure 20.6**: Bayesian network for Bayesian learning: parameter nodes Θ, Θ₁, Θ₂; evidence nodes Flavor_i, Wrapper_i.
- **Figure 20.7**: Bayesian linear regression constrained to origin. (a) 3 points near origin → slope uncertain, σ_N²≈0.3861; uncertainty grows with distance. (b) 5 points spread out → slope tightly constrained, σ_N²≈0.0286.
- **Figure 20.8**: (a) 3D plot of mixture of 3 Gaussians. (b) 128 sample points with 10-nearest-neighborhood circles.
- **Figure 20.9**: kNN density estimation: k=3 (too spiky), k=10 (just right), k=40 (too smooth).
- **Figure 20.10**: Kernel density estimation: w=0.02 (too small), w=0.07 (just right), w=0.20 (too large).
- **Figure 20.11**: Heart disease diagnostic network: hidden variable with 78 parameters. Removing hidden variable → 708 parameters.
- **Figure 20.12**: GMM with 3 components (weights 0.2, 0.3, 0.5); 500 sample points; model reconstructed by EM (virtually indistinguishable).
- **Figure 20.13**: Log likelihood increases with EM iterations: (a) GMM — reaches slightly above true model; (b) BN mixture — increases from -2044 to -2021 after one iteration.
- **Figure 20.14**: (a) Mixture model for candy: bag is hidden; features Flavor, Wrapper, Holes. (b) BN for Gaussian mixture.

### 9. EDGE CASES / EXCEPTIONS / TRAPS

- **Zero probability problem**: With small data, ML assigns zero probability to unseen events. Fix: initialize counts to 1.
- **Non-identifiability**: With 2 attributes and 5 parameters from 3 counts, cannot recover mixture weight.
- **Observationally equivalent models**: Flipping Bag variable yields same likelihood; EM converges to either.
- **Degenerate local maxima in EM**: Gaussian component covering single data point → variance → 0, likelihood → ∞.
- **Component merging in EM**: Two components acquire identical means and variances.
- **Saddle points in EM**: Rare cases where EM reaches saddle point or local minimum.
- **Overfitting with maximum likelihood**: Fully connected network always highest likelihood → need complexity penalty.
- **NN structure search superexponential**: Far too many structures to sum over for Bayesian approach.
- **Inner loop NP-hard**: With hidden variables, inner loop involves posterior computation in Bayes nets, which is NP-hard.

### 10. EMPIRICAL EVIDENCE / KEY RESULTS

- Naive Bayes achieves decision tree-like performance on restaurant problem but slightly worse.
- Ng & Jordan (2002): Naive Bayes beats logistic regression on 14/15 small data sets; logistic regression beats naive Bayes on 9/15 with full data.
- EM on Bayes net mixture: log likelihood improves from -2044 to -2021 after 1st iteration (factor ~10¹⁰). By 10th iteration, better than true model (L = -1982.214).
- Removing hidden variable from heart disease network increases parameters from 78 to 708.
- Mixture of Gaussians EM: final model virtually indistinguishable from original model.
- Heart disease example: latent variables reduce parameters from 708 to 78.

### 11. CROSS-CHAPTER DEPENDENCIES

- **Chapter 12**: Uncertainty; naive Bayes text classifier.
- **Chapter 13**: Bayesian networks; inference.
- **Chapter 14**: HMMs; filtering vs smoothing.
- **Chapter 19**: PAC learning; supervised learning; regression.
- **Section 4.2**: Optimization techniques.
- **Section 13.4**: MCMC.
- **Section 19.6**: Linear regression.
- **Section 19.7**: Nonparametric methods.
- **Appendix A**: Continuous probability.

### 12. DATES & PEOPLE

- **Thomas Bayes** (1763): Beta distribution as conjugate prior
- **Karl Pearson** (1895): Beta distribution as "Pearson Type I"
- **Ronald Fisher**: Maximum likelihood
- **Hartley** (1958): General idea of EM
- **Baum & Petrie** (1966): Baum-Welch algorithm for HMM (special case of EM)
- **Dempster, Laird & Rubin** (1977): EM algorithm in general form; one of most cited papers in CS and statistics
- **Judea Pearl** (1988): Bayes net learning algorithms via independence tests
- **Cooper & Herskovits** (1992): Likelihood-based structure learning
- **Lauritzen** (1995): EM for Bayes nets with hidden variables
- **Russell et al.** (1995): Gradient methods for Bayes nets with hidden variables
- **Friedman** (1998): Structural EM algorithm
- **Rosenblatt** (1956) & **Parzen** (1962): Kernel density estimation
- **Ferguson** (1973): Dirichlet process

### 13. PROOF & ARGUMENT PATTERNS

**Bayesian optimality argument**: Since all predictions are weighted averages over hypotheses, any other prediction is expected to be correct less often given the hypothesis prior.

**MAP = MDL equivalence**: -log₂ P(h_i) = bits to specify hypothesis; -log₂ P(d|h_i) = bits to specify data given hypothesis. MAP minimizes sum = total encoding length = MDL.

**EM likelihood monotonicity**: EM increases log likelihood at every iteration (provable in general). Under certain conditions, reaches local maximum (rarely saddle or local minimum).

**Identifiability argument**: With 2 attributes (e.g., flavor + wrapper, no holes), we have 5 parameters but only 3 observed counts → model is not identifiable. With 3 attributes, 7 parameters and 7 counts → identifiable (up to label flipping of bag).

### 14. DESIGN PARADIGMS / META-METHODS

- **Bayesian learning as inference**: Learning = probabilistic inference over hypothesis space.
- **Conjugate priors**: Choose prior that is closed under update (Beta for Bernoulli, Dirichlet for multinomial, Normal-Wishart for Gaussian).
- **Parameter independence**: Assumption that parameter distributions are independent simplifies Bayesian learning.
- **EM algorithm**: Iterative "chicken-and-egg" method: complete hidden variables (E-step), then maximize parameters (M-step).
- **MAP/MDL complexity penalty**: Penalize model complexity to avoid overfitting.

### 15. CASE STUDIES / CLASSIC EXAMPLES

**Cherry/Lime Candy Problem** (running example):
- 5 bag types h₁-h₅ (100% cherry to 100% lime).
- Priors: ⟨0.1, 0.2, 0.4, 0.2, 0.1⟩.
- After 1 lime: h₃ most likely; after 2 limes: h₄; after 3+: h₅ most likely.
- Bayesian prediction converges to true hypothesis.
- MAP after 3 limes predicts probability 1.0 for next lime; Bayesian predicts 0.8.

**Wrapper + Flavor Model**:
- Three parameters: θ (cherry proportion), θ₁ (red wrapper given cherry), θ₂ (red wrapper given lime).
- ML solutions are observed frequencies (comforting, commonsense results).

**Bayes Net for Heart Disease** (hidden variable):
- Smoking, Diet, Exercise → HeartDisease → Symptoms.
- 78 parameters with hidden variable; 708 without.
- Shows power of latent variables.

**Candy Mixture (two bags mixed)**:
- True parameters: θ=0.5, θ_F1=θ_W1=θ_H1=0.8, θ_F2=θ_W2=θ_H2=0.3.
- EM iteration: θ^(0)=0.6 → θ^(1)=0.6124; likelihood from -2044 to -2021.
- Log likelihood of learned model exceeds original true model after 10 iterations.

### 16. ETHICS

- Causal models subject to corporate dispute: "corporations have long claimed that smoking does not cause cancer and other corporations assert that CO₂ concentrations have no effect on climate" — showing importance of learning correct causal structure.

### 17. END-OF-CHAPTER MATERIAL

**Summary Key Points**:
- Bayesian learning: probabilistic inference; observations update prior over hypotheses; implements Ockham's razor.
- MAP learning: single most likely hypothesis; prior still used; more tractable than full Bayesian.
- ML learning: uniform prior; closed form for simple cases like linear regression and fully observable BNs.
- Naive Bayes: scales well, effective technique.
- Hidden variables: EM algorithm for local ML solutions.
- Structure learning: discrete search; trade off complexity vs fit.
- Nonparametric models: nearest-neighbors, kernel methods.

---

## CHAPTER 21: DEEP LEARNING

### 1. NAMED ENTITIES

- **Deep learning**: Family of ML techniques where hypotheses are complex algebraic circuits with tunable connection strengths; organized into many layers.
- **Layer**: A stage of computation in a deep network; computation paths from inputs to outputs have many steps.
- **Neural network**: Networks trained by deep learning methods; originally inspired by McCulloch-Pitts neuron model.
- **Feedforward network**: Connections only in one direction (DAG); no loops.
- **Recurrent network**: Feeds intermediate/final outputs back into own inputs (has internal state/memory).
- **Unit**: Each node within a network; computes weighted sum of inputs and applies nonlinear activation function.
- **Activation function**: Nonlinear function applied to weighted sum at each unit.
- **Sigmoid (logistic)**: σ(x) = 1/(1+e^{-x}); range (0,1).
- **ReLU (Rectified Linear Unit)**: ReLU(x) = max(0,x).
- **Softplus**: softplus(x) = log(1+e^x); derivative is sigmoid.
- **Tanh**: tanh(x) = (e^{2x}-1)/(e^{2x}+1); range (-1,+1).
- **Computation graph / Dataflow graph**: Circuit representation where each node is an elementary computation.
- **Fully connected**: Every node in each layer connected to every node in next layer.
- **Output layer**: Units producing output of network.
- **Hidden layer**: Layers not directly connected to outputs.
- **Back-propagation**: Passing error from output back through network to compute gradients.
- **Vanishing gradient**: Error signals extinguished as propagated back through many layers.
- **Automatic differentiation**: Systematic calculus to calculate gradients for any numeric program.
- **Reverse mode differentiation**: Applies chain rule "from outside in" (same as back-propagation).
- **End-to-end learning**: Complex system trained from input/output pairs without manual subsystem design.
- **One-hot encoding**: Categorical attribute with d values represented as d separate bits (one 1, rest 0).
- **Cross-entropy loss**: H(P,Q) = E_{z~P(z)}[-log Q(z)]; measures dissimilarity between distributions.
- **Softmax layer**: softmax(in)_k = e^{in_k} / Σ_{k'} e^{in_{k'}}; outputs probability distribution over d categories.
- **Mixture density layer**: Outputs mixture of Gaussians (weights, means, variances).
- **Convolutional neural network (CNN)**: Spatially local connections with replicated weight patterns.
- **Kernel**: Pattern of weights replicated across multiple local regions.
- **Convolution**: Applying kernel to input; z_i = Σ_{j=1}^{l} k_j x_{i+j-(l+1)/2}.
- **Stride**: Distance between kernel application positions (s).
- **Feature map**: Output tensor showing how each feature appears across image.
- **Channel**: One feature's information in a feature map (e.g., 96 channels from 96 kernels).
- **Receptive field**: Portion of sensory input that can affect a neuron's activation.
- **Pooling**: Summarizing adjacent units with single value (average-pooling or max-pooling).
- **Downsampling**: Coarsening resolution by pooling (e.g., average-pooling with l=s).
- **Tensor**: Multidimensional array; keeps track of "shape" of data as it progresses through layers.
- **GPU / TPU**: Graphics processing units / Tensor processing units for parallel deep learning.
- **Residual network**: Layer perturbs rather than replaces previous representation; z^{(i)} = g_r(z^{(i-1)} + f(z^{(i-1)})).
- **Residual**: f(z) = V g(W z); the learned perturbation.
- **Momentum**: Running average of past gradients to compensate for small minibatches.
- **Batch normalization**: Rescales values at internal layers within each minibatch; standardizes mean and variance using learned β, γ.
- **Weight decay**: L₂ penalty λ Σ W² added to loss; form of MAP learning with zero-mean Gaussian prior.
- **Dropout**: Deactivates randomly chosen units at each training step; approximates ensemble of thinned networks.
- **Adversarial example**: Small change to input causes large change in output (e.g., altered image misclassified).
- **Neural architecture search (NAS)**: Automated architecture selection via search (evolution, RL, gradient, Bayesian optimization).
- **Long short-term memory (LSTM)**: Specialized RNN with memory cell and gating units (forget, input, output gates).
- **Memory cell (c)**: Long-term memory in LSTM, copied from time step to time step.
- **Gating unit**: Vector controlling information flow via elementwise multiplication.
- **Forget gate (f)**: Determines if memory cell elements are remembered or forgotten.
- **Input gate (i)**: Determines if memory cell is updated by new information.
- **Output gate (o)**: Determines if memory cell is transferred to short-term memory.
- **Back-propagation through time (BPTT)**: Gradient computation for RNNs; linear in network size.
- **Exploding gradient**: Gradient grows exponentially when W_{z,z} > 1 in RNN.
- **Probabilistic PCA (PPCA)**: P(z)=N(z;0,I); P_W(x|z)=N(x;Wz,σ²I); learns linear mapping from latent to observed.
- **Autoencoder**: Encoder maps x→ẑ; decoder maps ẑ→x; trained so x ≈ g(f(x)).
- **Variational autoencoder (VAE)**: Uses variational lower bound (ELBO) for training deep generative model.
- **Variational posterior Q(z)**: Tractable approximation to true posterior P(z|x); optimized to be close via KL divergence.
- **ELBO / Variational lower bound**: L(x,Q) = log P(x) - D_KL(Q(z)||P(z|x)) = H(Q) + E_{z~Q} log P(z,x).
- **Autoregressive model (AR model)**: Each element x_i predicted based on other elements; no latent variables.
- **Deep autoregressive model**: AR model where conditional distribution is a deep network.
- **WaveNet**: DeepMind's AR model for speech generation (order 4800, multilayer convolutional).
- **Generative adversarial network (GAN)**: Generator + Discriminator trained simultaneously in game-theoretic competition.
- **Generator**: Produces samples from P_W(x) (maps z→x).
- **Discriminator**: Classifies inputs as real or fake.
- **Implicit model**: Samples can be generated but probabilities not readily available.
- **Unsupervised translation**: Translating x→y without paired (x,y) examples (using GANs).
- **Transfer learning**: Experience with one task helps learn another; copy weights from task A to task B.
- **Multitask learning**: Simultaneously train on multiple objectives.
- **Word embeddings**: Words represented as vectors in high-dimensional space; similar words close together.
- **Deep reinforcement learning**: Deep learning + RL for value/Q/policy functions.
- **Hopfield network**: Symmetric connections; associative memory.
- **Boltzmann machine**: Stochastic Hopfield network; early deep generative model.
- **Computational neuroscience**: Building computational models that capture biological neural system properties.

### 2. SEQUENTIAL PROCESSES

**Back-propagation Gradient Computation (for the simple 2-layer network)**:
1. Forward pass: compute unit outputs a_j via g_j(in_j).
2. For output weight w₃,₅: ∂Loss/∂w₃,₅ = -2(y-ŷ) g'₅(in₅) a₃.
3. For hidden weight w₁,₃: ∂Loss/∂w₁,₃ = -2(y-ŷ) g'₅(in₅) w₃,₅ g'₃(in₃) x₁.
4. Define Δ₅ = 2(ŷ-y) g'₅(in₅); Δ₃ = Δ₅ w₃,₅ g'₃(in₃).
5. Gradient for output weights = Δ₅ a₃; for hidden weights = Δ₃ x₁.

**General Back-Propagation in Computation Graphs**:
1. Forward pass: compute node outputs left to right.
2. Backward pass: begin at output nodes with ∂L/∂ŷ derived from loss.
3. At each internal node h: ∂L/∂h = Σ_{outgoing} ∂L/∂h_j (sum incoming messages).
4. Compute outgoing messages: ∂L/∂f_h = (∂L/∂h)(∂h/∂f_h); ∂L/∂g_h = (∂L/∂h)(∂h/∂g_h).
5. Continue to nodes representing weights — sum of incoming messages = ∂L/∂w.

**SGD Training Process**:
1. w ← w - α ∇_w L(w) where L is over minibatch.
2. Use decreasing learning rate schedule.
3. Optionally use momentum.
4. Optionally apply batch normalization.
5. Optionally apply weight decay (L₂ penalty).
6. Optionally apply dropout (randomly deactivate units per minibatch).

**Dropout Process**:
1. For each minibatch: with probability p, multiply unit output by 1/p; with probability 1-p, set to 0.
2. Apply back-propagation to thinned network.
3. At test time, run with no dropout.

**LSTM Update Equations**:
f_t = σ(W_{x,f} x_t + W_{z,f} z_{t-1})
i_t = σ(W_{x,i} x_t + W_{z,i} z_{t-1})
o_t = σ(W_{x,o} x_t + W_{z,o} z_{t-1})
c_t = c_{t-1} ⊙ f_t + i_t ⊙ tanh(W_{x,c} x_t + W_{z,c} z_{t-1})
z_t = tanh(c_t) ⊙ o_t

### 3. HIERARCHIES / CLASSIFICATIONS

**Network Types**:
- Feedforward (DAG) vs Recurrent (cycles with delay)
- Supervised (input-output pairs), Unsupervised (unlabeled inputs), Semisupervised (some labeled)
- Convolutional (images), Recurrent (sequences), Residual (very deep), LSTM (long sequences)

**Activation Functions**:
| Function | Formula | Range | Derivative |
|----------|---------|-------|------------|
| Sigmoid | σ(x)=1/(1+e^{-x}) | (0,1) | σ(x)(1-σ(x)) |
| ReLU | max(0,x) | [0,∞) | 0 if x≤0, 1 if x>0 |
| Softplus | log(1+e^x) | (0,∞) | σ(x) |
| Tanh | (e^{2x}-1)/(e^{2x}+1) | (-1,1) | 1 - tanh²(x) |

**Output Layer Types**:
- Sigmoid: Boolean probability
- Softmax: Multiclass probability distribution (sums to 1)
- Linear: Real-valued regression
- Mixture density: Gaussian mixture parameters

**Unsupervised Learning Models**:
- Probabilistic PCA (PPCA): linear mapping from latent Gaussian
- Autoencoders: encoder/decoder trained for reconstruction
- Variational autoencoders: variational inference with deep encoder/decoder
- Deep autoregressive models (e.g., WaveNet): sequential prediction
- Generative adversarial networks (GANs): generator + discriminator competition

### 4. COMPARISONS / TRADE-OFFS

- **Shallow vs Deep**: Shallow (linear/logistic regression) — short computation paths, limited expressiveness. Deep — long paths, complex interactions possible.
- **Decision trees vs Deep networks**: Trees have long paths for few inputs; need exponential size for many long paths. Deep networks have all-variable interaction.
- **Three-layer vs Eleven-layer**: For similar total weight count, deeper gives better generalization (Figure 21.7).
- **Sigmoid vs ReLU**: Sigmoid suffers vanishing gradient near extremes; ReLU avoids vanishing gradient but can have "dead" units.
- **Fully connected vs Convolutional**: Fully connected ignores adjacency and has n² weights. CNN + locality + weight sharing = dl weights (independent of image size).
- **Vanilla RNN vs LSTM**: RNN has multiplicative gradient accumulation → vanishing/exploding. LSTM copies memory cell (additive) → avoids vanishing gradient.
- **Q-learning vs Policy search**: Q-learning finds ˆQ close to Q*; policy search finds ˆQ that gives good performance (doesn't need to be close to Q*).
- **Forward pass vs Backward pass memory**: Back-propagation requires storing forward intermediate values → total memory proportional to number of units in network.

### 5. FORMULAS & EQUATIONS

**Unit computation**:
a_j = g_j(Σ_i w_{i,j} a_i) ≡ g_j(in_j)

**Unit in vector form**:
a_j = g_j(w^⊤ x)   (21.1)

**Network in matrix form**:
h_w(x) = g^{(2)}(W^{(2)} g^{(1)}(W^{(1)} x))   (21.3)

**Gradient for output weight w₃,₅**:
∂Loss/∂w₃,₅ = -2(y-ŷ) g'₅(in₅) a₃   (21.4)

**Gradient for hidden weight w₁,₃**:
∂Loss/∂w₁,₃ = -2(y-ŷ) g'₅(in₅) w₃,₅ g'₃(in₃) x₁   (21.5)

**Negative log likelihood objective**:
w* = argmin_w -Σ_{j=1}^{N} log P_w(y_j|x_j)   (21.6)

**Cross-entropy loss**:
H(P,Q) = E_{z~P(z)}[-log Q(z)]   (21.7)

**Softmax**:
softmax(in)_k = e^{in_k} / Σ_{k'=1}^{d} e^{in_{k'}}

**Convolution**:
z_i = Σ_{j=1}^{l} k_j x_{i+j-(l+1)/2}   (21.8)

**Receptive field size** (stride=1): (l-1)m + 1 for mth hidden layer.
**Receptive field growth** (stride>1): O(l s^m) — exponential with depth.

**Residual network**:
z^{(i)} = g_r(z^{(i-1)} + f(z^{(i-1)}))   (21.10)
where f(z) = V g(W z)

**SGD update**:
w ← w - α ∇_w L(w)

**Batch normalization**:
ẑ_i = γ(z_i - μ)/√(ε+σ²) + β

**Weight decay loss**:
Loss + λ Σ_{i,j} W_{i,j}²

**MAP interpretation of weight decay**:
h_MAP = argmin_w [-log P(y|X,W) - log P(W)]
If log P(W) = -λ Σ W² → P(W) is zero-mean Gaussian prior.

**LSTM equations**:
f_t = σ(W_{x,f} x_t + W_{z,f} z_{t-1})
i_t = σ(W_{x,i} x_t + W_{z,i} z_{t-1})
o_t = σ(W_{x,o} x_t + W_{z,o} z_{t-1})
c_t = c_{t-1} ⊙ f_t + i_t ⊙ tanh(W_{x,c} x_t + W_{z,c} z_{t-1})
z_t = tanh(c_t) ⊙ o_t

**PPCA generative model**:
P(z) = N(z; 0, I)
P_W(x|z) = N(x; Wz, σ²I)
P_W(x) = ∫ P_W(x,z) dz = N(x; 0, WW^⊤ + σ²I)   (21.16)

**Variational lower bound (ELBO)**:
L(x,Q) = log P(x) - D_KL(Q(z)||P(z|x))   (21.17)
        = H(Q) + E_{z~Q} log P(z,x)

### 6. RULES, LAWS & THEOREMS

- **Universal Approximation Theorem**: Network with 2 layers (1st nonlinear, 2nd linear) can approximate any continuous function to arbitrary accuracy (Cybenko 1988, 1989).
- **Back-propagation gradient structure**: Gradient computations for any feedforward computation graph have same structure as underlying graph.
- **Weight decay = MAP**: L₂ penalty corresponds to zero-mean Gaussian prior on weights.
- **Dropout approximation**: Dropout approximates training large ensemble of thinned networks (verified analytically for linear models).
- **ReLU identity**: ReLU(ReLU(x)) = ReLU(x) — key for residual network identity propagation.
- **Bayesian learning = inference**: Under the BN formulation with parameter nodes, learning is just inference.
- **Residual network property**: With zero weights, z^{(i)} = g_r(z^{(i-1)}). With ReLU, this becomes z^{(i)} = z^{(i-1)} (pass-through).
- **SGD global minimum for overparameterized networks**: Theorems show SGD often reaches global minimum with zero training error for sufficiently wide networks (Allen-Zhu et al. 2018; Du et al. 2018).

### 7. DATA STRUCTURES & TYPES

- **Tensor**: Multidimensional array (0D=scalar, 1D=vector, 2D=matrix, 3D+=tensor). Used to track data shape through CNN layers.
- **Weight matrix W^{(ℓ)}**: For layer ℓ; dimensions depend on layer sizes.
- **Computation graph**: DAG of elementary operations; each node knows its own derivative for autodiff.
- **Feature map**: 3D tensor (height × width × channels) from convolution.
- **Kernel**: Small pattern of weights (e.g., 5×5×3) replicated across image.

### 8. VISUAL PATTERNS

- **Figure 21.1**: (a) Shallow model — short paths, each input independent. (b) Decision list — some long paths for some inputs. (c) Deep network — all variables interact via long paths.
- **Figure 21.2**: Activation functions: sigmoid (S-curve 0 to 1), ReLU (0 for x<0, linear for x≥0) with softplus smooth version, tanh (S-curve -1 to 1).
- **Figure 21.3**: (a) 2-input, 2-hidden-unit, 1-output network. (b) Unpacked computation graph with inputs (blue) and weights (mauve).
- **Figure 21.4**: 1D convolution: kernel [+1,-1,+1] applied with stride 2 to 7-pixel input → 3 outputs [5, 9, 4]; peak at darker pixel.
- **Figure 21.5**: First 2 layers of CNN with kernel 3, stride 1; padding keeps layers same size. Receptive field of 2nd-layer unit covers 5 pixels.
- **Figure 21.6**: Back-propagation at generic node h: receives ∂L/∂h_j and ∂L/∂h_k from successors, sums them to get ∂L/∂h, then computes ∂L/∂f_h and ∂L/∂g_h for predecessors.
- **Figure 21.7**: Test error vs number of weights for 3-layer vs 11-layer CNNs (Street View addresses). 11-layer always better for any fixed weight count.
- **Figure 21.8**: (a) Basic RNN with recurrent hidden layer z and delay ∆. (b) Unrolled over 3 time steps creating feedforward network with shared weights.
- **Figure 21.9**: Arithmetic in z-space of generative model: "man with glasses" - "man" + "woman" = "woman with glasses."

### 9. EDGE CASES / EXCEPTIONS / TRAPS

- **Vanishing gradient**: In deep networks with sigmoid/tanh, g' near 0 in flat regions; error signals extinguished. ReLU reduces problem but can have dead units.
- **Exploding gradient**: In RNNs when W_{z,z} > 1, gradient grows exponentially.
- **Dead ReLU units**: If all inputs are negative, ReLU outputs 0 and gradient is 0; unit never recovers.
- **Adversarial examples**: Small pixel changes → completely different classification. Usually imperceptible to humans. Transferable across networks.
- **Catastrophic forgetting**: In RL with function approximation, learning too well → forgetting dangerous regions → sudden failure.
- **Numerical instability**: Exponentials in softmax/sigmoid/tanh can cause overflow; iterated computations in deep/recurrent networks cause vanishing/exploding activations.
- **Memory cost of back-propagation**: Need to store forward intermediate values; total memory proportional to total units.
- **Insufficient labeled data**: Current supervised DL may require more labeled data than the universe can supply for some tasks.

### 10. EMPIRICAL EVIDENCE / KEY RESULTS

- **AlexNet (2012 ImageNet)**: 15.3% top-5 error vs >25% for next best. 5 conv layers + max-pooling + 3 fully connected; 60M weights; ReLU; GPU training.
- **ImageNet progress (since 2012)**: Top-5 error reduced to <2%, below trained human (~5%).
- **11-layer vs 3-layer networks**: For any fixed number of weights, deeper network gives lower test-set error (Google Street View address transcription — Goodfellow et al. 2014).
- **ResNet-50**: Available pretrained on COCO (3000+ images each for bicycle, motorcycle, skateboard categories).
- **WaveNet**: Order 4800 AR model with multilayer convolutional structure; substantially more realistic speech than previous state-of-the-art.
- **GANs**: Can create photorealistic, high-resolution images of people who have never existed.
- **Machine translation**: End-to-end DL reduced translation errors by 60% relative to pipeline-based system (Wu et al. 2016b).
- **2018 Turing Award**: Yann LeCun, Yoshua Bengio, Geoff Hinton.

### 11. CROSS-CHAPTER DEPENDENCIES

- **Chapter 19**: Linear/logistic regression; gradient descent; supervised learning basics; Ockham's razor.
- **Chapter 20**: Maximum likelihood learning; Bayes nets; variational inference; cross-entropy; KL divergence.
- **Chapter 22**: Deep reinforcement learning (DQN, AlphaGo).
- **Chapter 23**: Grammars; n-grams.
- **Chapter 24**: Natural language; word embeddings; transformers; RNNs.
- **Chapter 25**: Computer vision (CNNs).
- **Chapter 26**: Robotics.

### 12. DATES & PEOPLE

- **McCulloch & Pitts** (1943): Mathematical model of neuron
- **Frank Rosenblatt** (1957): Perceptron; perceiveon convergence theorem (1960)
- **Kelley (1960), Bryson (1962), Werbos (1974)**: Back-propagation
- **Rumelhart, Hinton & Williams** (1986): Back-propagation in Nature
- **David Hubel & Torsten Wiesel** (1959, 1962, 1968): Simple/complex cells in visual cortex → CNNs
- **Kunihiko Fukushima** (1980): Neocognitron (early CNN)
- **Yann LeCun** (1995): Convolutional networks with back-propagation; hand-written digit recognition
- **Geoff Hinton** (2006): Deep belief networks breakthrough
- **Alex Krizhevsky** (2012): AlexNet wins ImageNet
- **Hochreiter & Schmidhuber** (1997): LSTM
- **Goodfellow et al.** (2015a): GANs
- **Kingma & Welling** (2013): Variational autoencoders
- **He et al.** (2016): Residual networks
- **LeCun, Bengio, Hinton** (2015): Nature article introducing deep learning to non-AI researchers
- **2018 Turing Award**: LeCun, Bengio, Hinton

### 13. PROOF & ARGUMENT PATTERNS

**Universal approximation theorem proof sketch**: Exponentially large network can represent exponentially many "bumps" of different heights at different locations → approximate any continuous function (lookup table for continuous functions).

**Back-propagation linearity in graph size**: Each node's backward messages are sum of outgoing derivatives → each node processes once → total cost linear in number of nodes.

**Residual network identity propagation**: If V=0, then f(z)=0, so z^{(i)} = g_r(z^{(i-1)}). With ReLU: ReLU(ReLU(x)) = ReLU(x) → identity. Thus disabling a layer doesn't break network → robust to depth.

**KL divergence nonnegativity**: D_KL(Q||P) ≥ 0 with equality iff Q=P. Used to derive ELBO.

### 14. DESIGN PARADIGMS / META-METHODS

- **Computation graph abstraction**: Unifies all deep learning models; nodes are elementary computations; weights are tunable parameters.
- **Feature hierarchy**: Deep networks learn increasingly abstract representations (edges → parts → objects).
- **Weight sharing**: Same weights reused across space (CNN) or time (RNN) → fewer parameters + inductive bias.
- **Residual learning**: Each layer should perturb rather than replace; enables very deep networks.
- **End-to-end learning**: Let the network learn the entire pipeline from raw inputs to outputs.
- **Unsupervised pretraining + supervised fine-tuning**: Transfer learning paradigm.
- **Game-theoretic training**: Generator vs discriminator in GANs.

### 15. CASE STUDIES / CLASSIC EXAMPLES

**Simple 2-layer network** (Section 21.1.1):
- Input x = [x₁, x₂]; hidden units a₃, a₄; output ŷ.
- Full expression: ŷ = g₅(w₀,₅ + w₃,₅ g₃(w₀,₃ + w₁,₃ x₁ + w₂,₃ x₂) + w₄,₅ g₄(w₀,₄ + w₁,₄ x₁ + w₂,₄ x₂)).

**CNN 1D convolution example** (Figure 21.4):
- Input: [5, 6, 6, 2, 5, 6, 5]; kernel: [+1, -1, +1]; stride: 2.
- Output: [5, 9, 4] — peak at dark pixel.

**ResNet pass-through with ReLU**: If V=0, all weights zero, then f(z)=0; ReLU(ReLU(x)) = ReLU(x) if previous layer used ReLU → identity.

**WaveNet**: AR model of order 4800 with multilayer convolutional structure; trained on raw audio at 16,000 samples/sec.

**ImageNet AlexNet** (2012): 5 conv + max-pooling + 3 fully connected; 60M weights; ReLU; GPU; 15.3% top-5 error (next best >25%).

**Style transfer / generative model arithmetic**: "man with glasses" - "man" + "woman" = "woman with glasses" in z-space.

### 16. ETHICS

- **Adversarial attacks and defenses**: Attackers seem ahead of defenders; robust adversarial examples fool multiple networks with different architectures.
- **Data requirements**: "Labeling large data sets usually requires scarce and expensive human labor."
- **Explainable AI (XAI)**: Regulations like GDPR require explanations; LIME, SHAP provide explanations.

### 17. END-OF-CHAPTER MATERIAL

**Summary Key Points**:
- Neural networks represent complex nonlinear functions with parameterized linear-threshold units.
- Back-propagation algorithm implements gradient descent to minimize loss.
- Deep learning works well for visual object recognition, speech, NLP, and RL.
- Convolutional networks (spatial locality + weight sharing) excel at image tasks.
- Recurrent networks (cycles with delay) excel at sequential tasks.
- Residual networks, batch normalization, dropout, weight decay improve training and generalization.
- Unsupervised learning: VAEs, GANs, autoregressive models.
- Transfer learning: pretrained models fine-tuned for new tasks.

---

## CHAPTER 22: REINFORCEMENT LEARNING

### 1. NAMED ENTITIES

- **Reinforcement learning (RL)**: Agent interacts with world and periodically receives rewards reflecting how well it is doing; maximizes expected sum of rewards.
- **Markov decision process (MDP)**: Formal framework for sequential decision problems (Ch. 17).
- **Sparse rewards**: Rewards given only in a small fraction of states (e.g., win/loss in chess).
- **Model-based reinforcement learning**: Agent uses/learns transition model of environment; often learns utility function U(s).
- **Model-free reinforcement learning**: Agent neither knows nor learns transition model; learns direct representation of how to behave.
- **Action-utility learning (Q-learning)**: Learns Q-function Q(s,a) = sum of rewards from state s onward if action a is taken.
- **Policy search**: Learns policy π(s) mapping directly from states to actions (reflex agent).
- **Q-function (Quality-function)**: Q(s,a) denoting sum of rewards from state s onward if action a is taken.
- **Passive reinforcement learning**: Agent's policy is fixed; task is to learn utilities of states.
- **Active reinforcement learning**: Agent must also figure out what to do; issue of exploration.
- **Passive learning agent**: Agent with fixed policy that tries to learn utility function U^π(s).
- **Trial**: Sequence of state transitions from start state to terminal state.
- **Reward-to-go**: Expected total reward from a state onward.
- **Direct utility estimation**: Utility of state = expected total reward from that state onward; each trial provides sample.
- **Adaptive dynamic programming (ADP)**: Learns transition model and solves MDP using DP.
- **Temporal-difference (TD) learning**: Adjusts utility estimates using observed transitions; uses error signal R + γU(s') - U(s).
- **Pseudoexperience**: Simulated transitions from current model used by TD agent.
- **Prioritized sweeping**: Heuristic to adjust states whose likely successors just had large adjustments.
- **Greedy agent**: Always takes action currently believed optimal; can get stuck in suboptimal policy.
- **GLIE (Greedy in the Limit of Infinite Exploration)**: Scheme trying each action unlimited times; e.g., choose random action with probability 1/t.
- **Exploration function**: f(u,n) trading off greed (high u) vs curiosity (low count n). Example: f(u,n) = R⁺ if n < N_e else u.
- **Bayesian reinforcement learning**: Prior over hypotheses; posterior obtained by Bayes' rule; optimal policy maximizes expected utility over models.
- **Exploration POMDP**: Problem of finding optimal exploration strategy is a POMDP over belief states (distribution over models).
- **Robust control theory**: Set of possible models H without probabilities; optimal robust policy = best outcome in worst case over H.
- **SARSA**: On-policy TD update: Q(s,a) ← Q(s,a) + α[R + γQ(s',a') - Q(s,a)].
- **Off-policy learning**: Learns Q for best action regardless of current policy (Q-learning).
- **On-policy learning**: Learns Q for actual policy being followed (SARSA).
- **Function approximation**: Compact approximation of utility/Q-function using features (e.g., linear combination).
- **Widrow-Hoff rule (Delta rule)**: θ_i ← θ_i + α[u_j(s) - Û_θ(s)] ∂Û_θ(s)/∂θ_i.
- **Catastrophic forgetting**: Learning too well → forgetting dangerous regions → sudden failure.
- **Experience replay**: Retaining and replaying trajectories from entire learning process to maintain value function accuracy.
- **Deep reinforcement learning**: RL with deep neural network as function approximator.
- **Credit assignment problem**: Determining which actions were responsible for a delayed reward/punishment.
- **Reward shaping**: Providing additional pseudorewards for "making progress."
- **Pseudoreward**: Additional reward for subgoal achievement to speed up learning.
- **Potential function Φ(s)**: Transforms reward without changing optimal policy: R'(s,a,s') = R(s,a,s') + γΦ(s') - Φ(s).
- **Hierarchical reinforcement learning (HRL)**: Breaking long action sequences into hierarchy of smaller pieces.
- **Partial program**: Program with unspecified choices that must be filled by learning.
- **Joint state space**: (s, m) composed of physical state s and machine state m (program counter, arguments, variable values).
- **Choice state**: State where program counter is at a choice point.
- **Semi-Markov decision process**: Allows actions of different durations.
- **Keepaway**: Simplified soccer game where team of 3 tries to keep possession; 2 opponents try to take possession.
- **Additive decomposition**: Overall utility decomposes into terms each depending on few variables (due to hierarchical structure).
- **Policy search**: Keep twiddling policy while its performance improves.
- **Policy value ρ(θ)**: Expected reward-to-go when π_θ is executed.
- **Policy gradient ∇_θ ρ(θ)**: Gradient of policy value with respect to parameters.
- **Stochastic policy π_θ(s,a)**: Probability of selecting action a in state s (e.g., softmax).
- **REINFORCE**: Algorithm estimating policy gradient from samples: ∇_θ ρ(θ) ≈ (1/N) Σ_j u_j(s) ∇_θ π_θ(s,a_j) / π_θ(s,a_j).
- **Correlated sampling**: Same random sequences used for comparing different policies to reduce variance (PEGASUS algorithm).
- **Apprenticeship learning**: Learning how to behave well given observations of expert behavior.
- **Imitation learning**: Supervised learning from observed state-action pairs to learn policy π(s).
- **Inverse reinforcement learning (IRL)**: Learning rewards by observing a policy (rather than policy from rewards).
- **Boltzmann rationality**: Agent chooses actions according to softmax distribution over Q-values.
- **Feature matching**: IRL assuming reward is linear combination of features; finds θ such that feature expectations match expert's.
- **Feature expectation μ_i(π)**: Expected discounted value of feature f_i when policy π is executed.
- **Deep Q-network (DQN)**: Deep neural network representing Q-function for Atari games.
- **Cart-pole (Inverted pendulum)**: Classic control problem; keep pole upright by moving cart.
- **Bang-bang control**: Discrete actions (jerk left or right).
- **BOXES algorithm**: Discretizes state space into boxes; first RL for cart-pole (Michie & Chambers 1968).
- **TD-Gammon**: Tesauro's backgammon system using TD learning; reached top-3 human level after 300,000 games.
- **AlphaGo / AlphaZero**: Deep RL + search for Go; learned value function + Q-function.

### 2. SEQUENTIAL PROCESSES

**Passive ADP Learning Algorithm** (Figure 22.2):
1. If s' is new, U[s'] ← 0.
2. If s is not null:
   a. Increment N_{s'|s,a}[s,a][s'].
   b. R[s,a,s'] ← r.
   c. Add a to A[s].
   d. P(·|s,a) ← NORMALIZE(N_{s'|s,a}[s,a]).
   e. U ← POLICY-EVALUATION(π, U, mdp).
3. s,a ← s', π[s'].
4. Return a.

**Passive TD Learning Algorithm** (Figure 22.4):
1. If s' is new, U[s'] ← 0.
2. If s is not null:
   a. Increment N_s[s].
   b. U[s] ← U[s] + α(N_s[s]) × (r + γU[s'] - U[s]).
3. s ← s'.
4. Return π[s'].

**Exploratory Q-Learning Algorithm** (Figure 22.8):
1. If s is not null:
   a. Increment N_sa[s,a].
   b. Q[s,a] ← Q[s,a] + α(N_sa[s,a])(r + γ max_{a'} Q[s',a'] - Q[s,a]).
2. s,a ← s', argmax_{a'} f(Q[s',a'], N_sa[s',a']).
3. Return a.

**SARSA Update**:
Q(s,a) ← Q(s,a) + α[R(s,a,s') + γ Q(s',a') - Q(s,a)]   (22.8)
(Applied at end of each s,a,r,s',a' quintuplet.)

**Gradient-based Policy Search (REINFORCE)** for sequential case:
∇_θ ρ(θ) ≈ (1/N) Σ_{j=1}^{N} u_j(s) ∇_θ π_θ(s,a_j) / π_θ(s,a_j)
where a_j is action in state s on trial j and u_j(s) is total reward from s onward.

**Feature Matching (IRL) Algorithm**:
1. Pick initial default policy π^(0).
2. For j = 1, 2, ... until convergence:
   a. Find θ^(j) such that expert's policy maximally outperforms π^(0)...π^(j-1) according to θ·μ(π).
   b. Let π^(j) be optimal policy for R^(j) = θ^(j)·f.

**Reward shaping potential function**:
R'(s,a,s') = R(s,a,s') + γΦ(s') - Φ(s)
Does not change optimal policy.

### 3. HIERARCHIES / CLASSIFICATIONS

**RL Approaches Taxonomy**:
- **Model-based**: learns/uses P(s'|s,a); learns U(s).
- **Model-free**:
  - Action-utility learning: learns Q(s,a) (e.g., Q-learning, SARSA).
  - Policy search: learns π(s) directly.

**RL Agent Types**:
| Aspect | Passive | Active |
|--------|---------|--------|
| Policy | Fixed | Must choose |
| Learns | U^π(s) or Q^π(s,a) | Optimal U(s) or Q(s,a) |
| Issue | Evaluating policy | Exploration vs exploitation |

**TD Learning Variants**:
| Algorithm | Type | Update target | Model needed? |
|-----------|------|---------------|---------------|
| TD(utility) | Passive | r + γU(s') | No |
| Q-learning | Off-policy | r + γ max_{a'} Q(s',a') | No |
| SARSA | On-policy | r + γ Q(s',a') | No |

**Exploration Approaches**:
- GLIE: random action with prob 1/t.
- Exploration function: f(u,n) with optimism.
- Bayesian RL: posterior over models.
- Robust control: worst-case over model set.

**RL + Function Approximation Levels**:
| Level | Approximator | Complexity |
|-------|-------------|------------|
| Tabular | Exact table | Up to ~10⁶ states |
| Linear | Û_θ = θ·f | Simple features |
| Nonlinear (deep) | Deep neural network | Learns features automatically |

### 4. COMPARISONS / TRADE-OFFS

- **Supervised Learning vs RL**: SL needs labeled (state,action) pairs from teacher; RL needs only reward signal (easier to specify but harder to learn from).
- **Model-based vs Model-free**: MB uses model → better sample efficiency, can simulate; MF simpler, no model needed.
- **Q-learning vs SARSA**: Q-learning (off-policy) backs up best Q-value; SARSA (on-policy) backs up actual action's Q-value. Q-learning more flexible; SARSA appropriate when policy partly controlled by others.
- **Q-learning vs Policy search**: Q-learning tries to approximate Q*; policy search tries to find θ giving good performance (may not need Q close to Q*).
- **ADP vs TD**: ADP adjusts state to agree with ALL successors (requires model) → accurate but expensive; TD adjusts to observed successor only → efficient but approximate.
- **Direct utility estimation vs ADP vs TD**: DUE ignores Bellman constraints (slow); ADP uses full model (fast but expensive); TD uses observed transitions (cheap, moderately fast).
- **Greedy vs Exploratory ADP**: Greedy gets stuck in suboptimal policy (Figure 22.6). Exploratory (with U+) finds near-optimal policy in 18 trials.
- **Bayesian vs Robust control**: Bayesian uses probabilities over models; robust uses worst-case (conservative but safe).

### 5. FORMULAS & EQUATIONS

**Utility definition**:
U^π(s) = E[ Σ_{t=0}^{∞} γ^t R(S_t, π(S_t), S_{t+1}) ]   (22.1)

**Bellman equation for fixed policy**:
U^π(s) = Σ_{s'} P(s'|s,π(s)) [R(s,π(s),s') + γ U^π(s')]   (22.2)

**Bellman equation for optimal policy**:
U(s) = max_{a∈A(s)} Σ_{s'} P(s'|s,a) [R(s,a,s') + γ U(s')]   (22.4)

**TD update for utilities**:
U^π(s) ← U^π(s) + α [R(s,π(s),s') + γ U^π(s') - U^π(s)]   (22.3)

**Q-learning TD update**:
Q(s,a) ← Q(s,a) + α [R(s,a,s') + γ max_{a'} Q(s',a') - Q(s,a)]   (22.7)

**SARSA update**:
Q(s,a) ← Q(s,a) + α [R(s,a,s') + γ Q(s',a') - Q(s,a)]   (22.8)

**Exploration function update**:
U⁺(s) ← max_a f( Σ_{s'} P(s'|s,a)[R(s,a,s') + γ U⁺(s')], N(s,a) )   (22.5)

**Linear function approximator for utilities**:
Û_θ(s) = θ₁ f₁(s) + θ₂ f₂(s) + ... + θ_n f_n(s)

**Delta rule (Widrow-Hoff) for linear function**:
θ_i ← θ_i + α [u_j(s) - Û_θ(s)] ∂Û_θ(s)/∂θ_i   (22.10)

**TD with function approximation**:
θ_i ← θ_i + α [R(s,a,s') + γ Û_θ(s') - Û_θ(s)] ∂Û_θ(s)/∂θ_i   (22.11)

**Q-learning with function approximation**:
θ_i ← θ_i + α [R(s,a,s') + γ max_{a'} Q̂_θ(s',a') - Q̂_θ(s,a)] ∂Q̂_θ(s,a)/∂θ_i   (22.12)

**Reward shaping**:
R'(s,a,s') = R(s,a,s') + γΦ(s') - Φ(s)   (doesn't change optimal policy)

**Softmax stochastic policy**:
π_θ(s,a) = e^{β Q̂_θ(s,a)} / Σ_{a'} e^{β Q̂_θ(s',a')}   (22.14)

**REINFORCE gradient estimate**:
∇_θ ρ(θ) ≈ (1/N) Σ_{j=1}^{N} u_j(s) ∇_θ π_θ(s,a_j) / π_θ(s,a_j)

**Feature matching**: If μ_i(π) = μ_i(π_E) for all i, then π is as good as expert's policy according to expert's own reward function.

### 6. RULES, LAWS & THEOREMS

- **Bellman equation**: Utility of state = sum of rewards + discounted utility of successor states, weighted by transition probabilities.
- **Bellman optimality equation**: U(s) = max_a Σ_{s'} P(s'|s,a)[R(s,a,s') + γU(s')].
- **GLIE property**: If every action tried unboundedly in each state, and policy becomes greedy in limit, agent converges to optimal policy.
- **Reward shaping invariance**: Adding γΦ(s') - Φ(s) to reward does not change optimal policy (from Chapter 17).
- **Convergence of TD with linear function approx**: Passive TD with linear function approximator converges to closest possible approximation to true function.
- **Convergence of Q-learning**: Q-learning converges to optimal Q-values as visits → ∞, provided all actions tried in all states.
- **Feature matching convergence**: Requires O(n log n) iterations and O(n log n) expert demonstrations.
- **Condorcet Jury Theorem parallel**: Ensemble of 5 independent classifiers correct 75% each → majority correct 89%. 17 classifiers → 99% (if independent).

### 7. DATA STRUCTURES & TYPES

- **U**: Table of utilities indexed by state.
- **Q**: Table of action values indexed by state and action.
- **N_{s'|s,a}**: Table of outcome count vectors indexed by (state, action) → resulting state counts.
- **N_s**: Frequency table for state visit counts.
- **Policy π(s)**: Mapping from states to actions (table or parameterized function).
- **Transition model P(s'|s,a)**: Table or learned function.

### 8. VISUAL PATTERNS

- **Figure 22.1**: (a) Optimal policies for 4×3 world with R=-0.04 for nonterminal transitions. (b) Utilities of states given policy π.
- **Figure 22.3**: Passive ADP learning curves — utility estimates for selected states over 100 trials. States (2,1) and (3,2) need 14 and 23 trials to "discover" connection to +1 exit.
- **Figure 22.5**: TD learning curves — slower than ADP, higher variability. RMS error comparison.
- **Figure 22.6**: Greedy ADP agent converges to suboptimal policy (Down in (1,2)) after just 8 trials; policy loss of 0.235.
- **Figure 22.7**: Exploratory ADP with R⁺=2, N_e=5 discovers near-optimal policy after 18 trials.
- **Figure 22.9**: (a) Cart-pole balancing setup — cart position x, pole angle θ. (b) Helicopter autonomous "nose-in circle" maneuver — 6 time-lapse images.

### 9. EDGE CASES / EXCEPTIONS / TRAPS

- **Sparse rewards**: In many real-world environments, most actions yield no reward; credit assignment problem.
- **Greedy agent gets suboptimal policy**: Because learned model ≠ true environment; agent never learns about unexplored better states.
- **Catastrophic forgetting**: After learning to avoid edges, car forgets why edges are dangerous → drifts off road.
- **Irreversible actions**: Some actions lead to absorbing states (death); exploration must be safe.
- **Exploration and premature death**: Bayesian approach doesn't protect against taking actions leading to absorbing states.
- **Nonlinear function approximation divergence**: Simple cases where parameters go to infinity even though good solutions exist.
- **Robust control conservatism**: Worst-case assumption → overly conservative (e.g., car stays in garage assuming all drivers try to collide).
- **Policy search variance**: Total reward varies widely between trials; hard to compare policies via hill climbing.
- **IRL identifiability problem**: R(s,a,s') = 0 explains any observed behavior; need prior that rewards are not trivial.

### 10. EMPIRICAL EVIDENCE / KEY RESULTS

- **Passive ADP (4×3 world)**: RMS error near 0 after ~100 trials.
- **Passive TD (4×3 world)**: RMS error ~0.1 after 100 trials; varies more than ADP; takes ~500 trials.
- **Greedy ADP**: Converges to suboptimal policy after ~8 trials (policy loss 0.235).
- **Exploratory ADP (R⁺=2, N_e=5)**: Near-optimal policy after ~18 trials.
- **TD-Gammon**: After 300,000 training games, reached level of top-3 human players.
- **DQN (Atari)**: Roughly human expert level on 49 Atari games; Montezuma's Revenge too hard.
- **AlphaGo**: Uses value function + Q-function + search; beats best human players.
- **PEGASUS helicopter**: Autonomous nose-in circle maneuver exceeding expert human pilot performance.
- **Keepaway HRL**: Policy that keeps possession forever (vs ~10 sec previous record).
- **Feature matching IRL**: Requires O(n log n) iterations and demonstrations.

### 11. CROSS-CHAPTER DEPENDENCIES

- **Chapter 2**: Agent designs; reflex agent.
- **Chapter 4**: Online search; irreversible actions.
- **Chapter 5**: Game playing; Monte Carlo tree search; evaluation functions.
- **Chapter 7**: Wumpus world agent (robust control example).
- **Chapter 11**: HTN planning (HRL connection).
- **Chapter 14**: HMMs; state estimation.
- **Chapter 17**: MDPs; Bellman equations; value/policy iteration; exploration (bandit problems); reward shaping.
- **Chapters 19–21**: Supervised learning; function approximation; deep learning.

### 12. DATES & PEOPLE

- **Ivan Pavlov** (Nobel 1904): Classical conditioning
- **Edward Thorndike** (1911): Animal Intelligence; law of effect
- **Alan Turing** (1948, 1950): Proposed RL; "punishments and rewards can at best be part of the teaching process"
- **Arthur Samuel** (1959, 1967): First successful ML (checkers); pioneered TD learning, function approximation
- **Widrow & Hoff** (1960): Delta rule
- **Donald Hebb** (1949): Hebbian learning
- **Michie & Chambers** (1968): BOXES algorithm for cart-pole
- **Chris Watkins** (1989): Q-learning (PhD thesis)
- **Rich Sutton** (1988): Mathematical understanding of TD methods; DYNA architecture (1990)
- **Gerry Tesauro** (1992, 1995): TD-Gammon; Neurogammon (1990)
- **Ron Williams** (1992): REINFORCE algorithm
- **Barto, Sutton, etc.** (1980s): RL development at UMass
- **Stuart Russell** (1998): Inverse RL
- **Pieter Abbeel & Andrew Ng** (2004): Feature matching IRL
- **DeepMind (Mnih et al.)** (2013, 2015): DQN for Atari
- **AlphaGo** (Silver et al., 2016, 2018): Deep RL + search for Go
- **Sutton & Barto** (2018): Canonical RL textbook
- **Royall Society**: Open-source simulation environments: ALE (Bellemare et al. 2013), DeepMind Lab, OpenAI Gym

### 13. PROOF & ARGUMENT PATTERNS

**Regret bound for weighted majority**: M < (M* ln(1/β) + ln K)/(1-β) holds for any sequence, even adversarial.

**REINFORCE unbiased gradient estimate**: True gradient ∇_θ ρ(θ) = Σ_a R(s₀,a,s₀) ∇_θ π_θ(s₀,a). By multiplying and dividing by π_θ(s₀,a), we get Σ_a π_θ(s₀,a) · R(s₀,a,s₀) ∇_θ π_θ(s₀,a)/π_θ(s₀,a) ≈ (1/N) Σ_j R(s₀,a_j,s₀) ∇_θ π_θ(s₀,a_j)/π_θ(s₀,a_j). This is unbiased because a_j sampled from π_θ.

**Correlated sampling argument**: Using same random number sequences for comparing two policies eliminates measurement error due to environment stochasticity. Need only enough trials to distinguish policies, not to get absolute values.

**Feature matching argument**: If policy π produces feature expectations μ_i(π) that match expert's μ_i(π_E), then π is as good as expert's policy according to expert's own reward function (since utility = θ·μ(π)).

**IRL identifiability argument**: If R(s,a,s') = 0, any policy is rational. But P(d|h_R) for R=0 is infinitesimal (explains nothing about why expert chose that particular behavior over vast space of alternatives optimal under R=0). Simple priors penalize R=0 less, but likelihood term dominates.

### 14. DESIGN PARADIGMS / META-METHODS

- **Learning = solving MDP without knowing model/reward**: Key RL insight.
- **Temporal abstraction (HRL)**: Decompose long sequences into hierarchy; choose higher-level actions → concrete lower-level sequences.
- **Experience replay**: Retain and replay old trajectories to prevent catastrophic forgetting.
- **Correlated sampling**: Same random seeds to compare policies fairly.
- **Reward shaping**: Guide learning with pseudorewards without changing optimal policy (if potential function is used).
- **Inverse RL**: Observe actions → infer reward → derive policy (more robust than direct imitation).

### 15. CASE STUDIES / CLASSIC EXAMPLES

**4×3 World (running example)**:
- States: grid with +1 at (4,3), -1 at (4,2), -0.04 for nonterminal transitions.
- Policy: shown in Figure 22.1(a); two optimal actions in (3,1).
- Three sample trials shown (page 792): sequence of state-action-reward transitions.
- Direct utility estimation: first trial gives total reward 0.76 for (1,1), 0.80 and 0.88 for (1,2), etc.
- ADP: learns transition model from counts (e.g., Right from (3,3) → (3,2) 2 times, (4,3) 2 times → each 0.5).
- TD: starts with U(1,3)=0.88, U(2,3)=0.96; transition from (1,3) suggests U(1,3) should be -0.04+0.96=0.92; current estimate 0.84 → increase.

**Chess as RL**:
- Supervised learning approach fails: 10⁸ examples vs 10⁴⁰ positions.
- RL approach: reward = 1 win, 0 lose, ½ draw.
- Sparse rewards: only at end of game.

**Cart-Pole (Inverted Pendulum)** (Figure 22.9(a)):
- State: x, θ, ẋ, θ̇ (continuous).
- Actions: jerk left or right (bang-bang).
- BOXES algorithm: discretize state space into boxes; ~30 trials to balance for hour.

**Helicopter Flight** (Figure 22.9(b)):
- PEGASUS policy search with correlation sampling; from overnight simulation.
- Autonomous "nose-in circle" exceeding human expert.

**Keepaway Soccer**:
- 3 keepers vs 2 takers; HRL partial program with choices: PASS/HOLD/DRIBBLE if have ball; STAY/MOVE/INTERCEPT-BALL otherwise.
- HRL policy learns to keep possession forever vs ~10 sec previous record.

**Atari DQN**: Deep Q-network; learns from raw pixels; reward = game score; expert-level on 49/57 games.

### 16. ETHICS

- **Safe exploration**: Irreversible actions, absorbing states; need to avoid premature death in real-world learning (e.g., car crashes).
- **Reward modeling risk**: Agent may learn to maximize pseudorewards rather than true rewards (e.g., vibrating next to ball to maximize contacts).
- **Accountability**: Need to define what happens when system is wrong; process for appealing decisions.
- **Monitoring and maintenance**: Nonstationarity; models become stale; need to update.

### 17. END-OF-CHAPTER MATERIAL

**Summary Key Points**:
- Model-based RL: learns transition model + utility function.
- Model-free RL: learns Q(s,a) or policy π(s).
- Utilities learned via: direct utility estimation, ADP (model + DP), TD methods.
- Q-learning: model-free TD for action-utility.
- Active learning: exploration vs exploitation tradeoff; GLIE schemes; safe exploration.
- Large state spaces: function approximation; deep RL.
- Reward shaping and HRL for complex behaviors.
- Policy search: directly optimize policy.
- Apprenticeship learning: imitation learning or inverse RL.
