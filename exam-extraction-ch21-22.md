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
