# Study Guide: CLRS Part III — Data Structures (Chapters 10–13)

> Generated 2026-06-04. Subject: Computer Science (Algorithms & Data Structures). Exam format: Mixed (MCQ, short answer, problem-solving). Coverage: comprehensive — every examinable primitive from Ch.10–13 of CLRS 4e.

---

## Ch. 10 — Elementary Data Structures

### Named Entities (Terms & Definitions)

- **Array**: Contiguous sequence of bytes in memory. Constant-time access via base + offset formula.
- **Row-major order**: Matrix stored row by row in a single array. Index: `s + n(i − s) + (j − s)` for 1-origin: `n(i−1) + j`.
- **Column-major order**: Matrix stored column by column. Index: `s + m(j − s) + (i − s)`. For 0-origin: `i + mj`.
- **Block representation**: Matrix divided into blocks, each stored contiguously.
- **Multiple-array representation**: Separate array per row (or column), plus a pointer array.
- **Stack**: LIFO (last-in, first-out) data structure. Operations: PUSH (insert), POP (delete).
- **Queue**: FIFO (first-in, first-out) data structure. Operations: ENQUEUE (insert), DEQUEUE (delete).
- **Stack underflow**: Attempt to POP from an empty stack.
- **Stack overflow**: PUSH onto a full stack.
- **Queue underflow**: Attempt to DEQUEUE from an empty queue.
- **Queue overflow**: ENQUEUE onto a full queue.
- **Deque** (double-ended queue): Insertion/deletion at both ends.
- **Linked list**: Linear ordering determined by pointers in each object.
- **Doubly linked list**: Each element has `next` and `prev` pointers.
- **Singly linked list**: Each element has only a `next` pointer.
- **Sorted list**: Linear order corresponds to key order.
- **Unsorted list**: Elements in arbitrary order.
- **Circular list**: `prev` of head points to tail; `next` of tail points to head.
- **Sentinel**: Dummy object (e.g., `L.nil`) that simplifies boundary conditions.
- **Compact list**: Singly linked list stored in `key[1..n]` and `next[1..n]` arrays.
- **Left-child, right-sibling representation**: Each node has `left-child` pointer to first child and `right-sibling` pointer to next sibling.
- **Binary tree representation**: Nodes with `p`, `left`, `right` attributes.
- **Mergeable heap**: Supports MAKE-HEAP, INSERT, MINIMUM, EXTRACT-MIN, UNION.
- **Search list**: A linked list whose elements contain searchable keys.

### Processes / Algorithms / Pseudocode

#### STACK-EMPTY(S)
```
1 if S.top == 0
2     return TRUE
3 else return FALSE
```
- **Complexity**: O(1)
- **Condition**: Returns TRUE if stack is empty

#### PUSH(S, x)
```
1 if S.top == S.size
2     error "overflow"
3 else S.top = S.top + 1
4     S[S.top] = x
```
- **Input**: Stack S, element x
- **Complexity**: O(1)
- **Edge case**: overflow when S.top equals S.size

#### POP(S)
```
1 if STACK-EMPTY(S)
2     error "underflow"
3 else S.top = S.top − 1
4     return S[S.top + 1]
```
- **Input**: Stack S (no element argument needed)
- **Complexity**: O(1)
- **Edge case**: underflow when stack is empty

#### ENQUEUE(Q, x)
```
1 Q[Q.tail] = x
2 if Q.tail == Q.size
3     Q.tail = 1
4 else Q.tail = Q.tail + 1
```
- **Input**: Queue Q, element x
- **Complexity**: O(1)
- **Note**: Wraps around circularly; no overflow check shown

#### DEQUEUE(Q)
```
1 x = Q[Q.head]
2 if Q.head == Q.size
3     Q.head = 1
4 else Q.head = Q.head + 1
5 return x
```
- **Complexity**: O(1)
- **Note**: No underflow check shown

#### LIST-SEARCH(L, k)
```
1 x = L.head
2 while x ≠ NIL and x.key ≠ k
3     x = x.next
4 return x
```
- **Input**: List L, key k
- **Output**: Pointer to first element with key k, or NIL
- **Complexity**: Θ(n) worst-case

#### LIST-PREPEND(L, x)
```
1 x.next = L.head
2 x.prev = NIL
3 if L.head ≠ NIL
4     L.head.prev = x
5 L.head = x
```
- **Complexity**: O(1)
- **Effect**: Inserts x at front of list

#### LIST-INSERT(x, y)
```
1 x.next = y.next
2 x.prev = y
3 if y.next ≠ NIL
4     y.next.prev = x
5 y.next = x
```
- **Complexity**: O(1)
- **Effect**: Inserts x immediately after y

#### LIST-DELETE(L, x)
```
1 if x.prev ≠ NIL
2     x.prev.next = x.next
3 else L.head = x.next
4 if x.next ≠ NIL
5     x.next.prev = x.prev
```
- **Complexity**: O(1) (excluding search for x)
- **Note**: Must have pointer to element x to delete

#### LIST-DELETE'(x) — with sentinel
```
1 x.prev.next = x.next
2 x.next.prev = x.prev
```
- **Complexity**: O(1)
- **Note**: No boundary checks needed; sentinel eliminates special cases

#### LIST-INSERT'(x, y) — with sentinel
```
1 x.next = y.next
2 x.prev = y
3 y.next.prev = x
4 y.next = x
```
- **Complexity**: O(1)
- **Note**: To insert at head, let y = L.nil; to insert at tail, let y = L.nil.prev

#### LIST-SEARCH'(L, k) — with sentinel optimization
```
1 L.nil.key = k           // store key in sentinel to guarantee it's in list
2 x = L.nil.next           // start at head
3 while x.key ≠ k
4     x = x.next
5 if x == L.nil             // found k in sentinel
6     return NIL
7 else return x
```
- **Complexity**: Θ(n) worst-case, but with smaller constant factor (one comparison per iteration instead of two)

#### Left-Child, Right-Sibling Representation
- Node attributes: `p` (parent), `left-child` (first child), `right-sibling` (next sibling)
- Space: O(n) for n-node arbitrary rooted tree

### Comparisons & Trade-offs

| Dimension | Array | Doubly Linked List |
|-----------|-------|---------------------|
| Access k-th element | O(1) | Θ(k) |
| Insert/delete first | Θ(n) (must shift) | O(1) |
| Search | Θ(n) | Θ(n) |
| Space per element | Key + satellite | Key + 2 pointers + satellite |
| Memory locality | High | Low |

| Sentinel vs No Sentinel | Sentinel | No Sentinel |
|-------------------------|----------|-------------|
| Code simplicity | Cleaner (no boundary checks) | More conditionals |
| Space | +1 node per list | None |
| Asymptotic time | Same | Same |
| Constant factors | Slightly better for search | Standard |

### Formulas & Equations

#### Array Address Calculation
- 1-origin: element i occupies bytes `a + b(i − 1)` through `a + bi − 1`
- 0-origin: element i occupies bytes `a + bi` through `a + b(i + 1) − 1`
- `a` = base address, `b` = bytes per element, `s` = starting index

#### Matrix Index in Single Array
- Row-major, 1-origin: `M[i,j]` at index `n(i − 1) + j`
- Column-major, 1-origin: `M[i,j]` at index `i + m(j − 1)`
- Row-major, 0-origin: `M[i,j]` at index `ni + j`
- Column-major, 0-origin: `M[i,j]` at index `i + mj`

### Edge Cases & Common Pitfalls

- **Stack underflow**: POP on empty stack — error
- **Stack overflow**: PUSH on full stack — error
- **Queue underflow**: DEQUEUE on empty queue — error
- **Queue overflow**: ENQUEUE on full queue — error
- **Circular wrap-around**: Must wrap indices modulo array size
- **Deleting from singly linked list**: Requires Θ(n) time because need predecessor
- **Sentinels waste space**: For many small lists, sentinel overhead is significant
- **Sentinel deletion**: Never delete sentinel unless deleting entire list
- **Multiple-array matrices**: Slower due to extra indirection vs single array

### End-of-Chapter Material

**Key terms**: Array, row-major order, column-major order, stack, LIFO, queue, FIFO, deque, linked list, singly linked, doubly linked, sorted list, unsorted list, circular list, sentinel, compact list, left-child/right-sibling representation.

**Key results**: Stack/queue operations O(1); LIST-SEARCH Θ(n); LIST-PREPEND, LIST-INSERT, LIST-DELETE O(1) with pointer; array element access O(1).

---

## Ch. 11 — Hash Tables

### Named Entities (Terms & Definitions)

- **Direct-address table**: Array T[0..m−1] where slot k points to element with key k.
- **Hash table**: Generalization of array using hash function to compute slot from key.
- **Hash function** `h`: Maps universe U to slots {0,1,…,m−1}.
- **Hash value**: `h(k)`, the slot computed for key k.
- **Collision**: Two distinct keys hash to the same slot.
- **Chaining**: Collision resolution where each slot points to a linked list of elements.
- **Load factor** `α = n/m`: Average number of elements per chain.
- **Independent uniform hashing**: Each key equally likely to hash to any of m slots, independently.
- **Random oracle**: Ideal hash function giving independent uniform output per input.
- **Division method**: `h(k) = k mod m`.
- **Multiplication method**: `h(k) = ⌊m(kA mod 1)⌋`, with 0<A<1.
- **Multiply-shift method**: For m = 2^ℓ, `h_a(k) = (k·a mod 2^w) ⋙ (w−ℓ)`.
- **Static hashing**: Single fixed hash function.
- **Random hashing**: Hash function chosen randomly from a family.
- **Universal hashing**: Family H such that for any distinct k1,k2, Pr[h(k1)=h(k2)] ≤ 1/m.
- **ϵ-universal**: Pr[h(k1)=h(k2)] ≤ ϵ.
- **Uniform family**: For any key k, Pr[h(k)=q] = 1/m for all q.
- **d-independent family**: For any distinct keys k1..kd, Pr[h(ki)=qi ∀i] = 1/m^d.
- **Open addressing**: All elements stored in hash table itself (no pointers outside).
- **Probe**: Examination of a slot during open addressing insertion/search.
- **Probe sequence**: Permutation of {0,…,m−1} for a given key.
- **Double hashing**: `h(k,i) = (h1(k) + i·h2(k)) mod m`.
- **Linear probing**: `h(k,i) = (h1(k) + i) mod m` (special case of double hashing with h2(k)=1).
- **Primary clustering**: Long runs of occupied slots in linear probing.
- **Independent uniform permutation hashing**: Each key's probe sequence is equally likely any permutation of {0,…,m−1}.
- **Cryptographic hash function**: Complex pseudorandom function (e.g., SHA-256) usable for hash tables.
- **Wee hash function**: Fast register-based hash using `f_a(k) = swap((2k² + ak) mod 2^w)` iterated r rounds.
- **Bit vector**: Array of bits representing presence of keys.
- **Perfect hashing**: Scheme where all collisions are avoided.
- **Random oracle**: Ideal independent uniform hash function.

### Processes / Algorithms / Pseudocode

#### DIRECT-ADDRESS-SEARCH(T, k)
```
1 return T[k]
```
- **Complexity**: O(1) worst-case

#### DIRECT-ADDRESS-INSERT(T, x)
```
1 T[x.key] = x
```
- **Complexity**: O(1) worst-case

#### DIRECT-ADDRESS-DELETE(T, x)
```
1 T[x.key] = NIL
```
- **Complexity**: O(1) worst-case

#### CHAINED-HASH-INSERT(T, x)
```
1 LIST-PREPEND(T[h(x.key)], x)
```
- **Complexity**: O(1) worst-case (assumes no duplicate check)
- **Note**: Uses LIST-PREPEND from Ch.10; elements added at front of chain

#### CHAINED-HASH-SEARCH(T, k)
```
1 return LIST-SEARCH(T[h(k)], k)
```
- **Complexity**: Average O(1+α); worst-case Θ(n)
- **Note**: Searches linked list at slot h(k)

#### CHAINED-HASH-DELETE(T, x)
```
1 LIST-DELETE(T[h(x.key)], x)
```
- **Complexity**: O(1) if doubly linked lists (element x known, not key)
- **Note**: Requires doubly linked lists for O(1) deletion

#### HASH-INSERT(T, k) — Open addressing
```
1 i = 0
2 repeat
3     q = h(k, i)
4     if T[q] == NIL
5         T[q] = k
6         return q
7     else i = i + 1
8 until i == m
9 error "hash table overflow"
```
- **Complexity**: Average O(1/(1−α)) probes; worst-case O(m)
- **Input**: Table T, key k (assumed not already present)

#### HASH-SEARCH(T, k) — Open addressing
```
1 i = 0
2 repeat
3     q = h(k, i)
4     if T[q] == k
5         return q
6     i = i + 1
7 until T[q] == NIL or i == m
8 return NIL
```
- **Complexity**: Average O(1/(1−α)) probes; worst-case O(m)
- **Note**: Terminates at empty slot (since insertion would have placed k there)

#### LINEAR-PROBING-HASH-DELETE(T, q)
```
 1 while TRUE
 2     T[q] = NIL
 3     q' = q
 4     repeat
 5         q' = (q' + 1) mod m
 6         k' = T[q']
 7         if k' == NIL
 8             return
 9     until g(k', q) < g(k', q')
10     T[q] = k'
11     q = q'
```
- **Purpose**: Delete key at slot q from a linear probing hash table without using DELETED marker
- **Key insight**: If `g(k', q) < g(k', q')` then slot q was probed before q' during insertion — must move k' up

#### WEE(k, a, b, t, r, m) — Variable-length input hash
```
1 u = ⌈t/w⌉
2 〈k₁, k₂, …, k_u〉 = chop(k)
3 q = b
4 for i = 1 to u
5     q = f_a^{(r)}(q + k_i)
6 return q mod m
```

#### Hash function family based on number theory (universal)
- Choose prime p > all keys, m = table size
- `h_{ab}(k) = ((ak + b) mod p) mod m` where a∈{1,…,p−1}, b∈{0,…,p−1}
- Family size: p(p−1) functions

#### Multiply-shift universal family (2/m-universal)
- `h_a(k) = ((k·a) mod 2^w) ⋙ (w−ℓ)` where a is odd
- Implemented with 3 machine instructions: multiply, no carry, right shift

### Hash Functions (Formulas & Equations)

#### Division Method
`h(k) = k mod m`
- **Constraints**: Avoid powers of 2 for m; prime not too close to power of 2 works well
- **Speed**: Fast (single division)
- **Pitfall**: m constrains hash-table sizes to primes; no randomness guarantee

#### Multiplication Method
`h(k) = ⌊m(kA mod 1)⌋`
- `kA mod 1` = fractional part of kA = kA − ⌊kA⌋
- `0 < A < 1` (constant)
- **Advantage**: m not critical; can choose independently of A

#### Multiply-Shift Method (m = 2^ℓ, ℓ ≤ w)
`h_a(k) = (k·a mod 2^w) ⋙ (w−ℓ)`
- a is a w-bit odd integer
- `⋙` = logical right shift (zero-fill)
- Implemented in 3 instructions: multiply, no carry, right shift
- Example: k=123456, ℓ=14, w=32, a=2654435769 → h_a(k)=67

#### Universal Hash (Number Theory)
`h_{ab}(k) = ((ak + b) mod p) mod m`
- a ∈ {1,…,p−1}, b ∈ {0,…,p−1}, p prime, p > all keys

#### Double Hashing
`h(k, i) = (h₁(k) + i·h₂(k)) mod m`
- h₁, h₂ are auxiliary hash functions
- h₂(k) must be relatively prime to m for full coverage
- Θ(m²) distinct probe sequences when m is prime or power of 2

#### Linear Probing
`h(k, i) = (h₁(k) + i) mod m`
- Simplest open addressing; only m distinct probe sequences
- Suffers from primary clustering

#### Wee Hash Function (short input, ≤ w bits)
`h_{a,b,t,r}(k) = (f_a^{(r)}(k + b) + 2^t) mod m`
- `f_a(k) = swap((2k² + ak) mod 2^w)`
- `swap(x)` swaps high and low w/2-bit halves
- r = 4 rounds recommended; a odd

### Rules, Laws & Theorems

#### Theorem 11.1 (Unsuccessful Search — Chaining)
In a hash table with chaining, under independent uniform hashing, an unsuccessful search takes **Θ(1 + α)** expected time.

#### Theorem 11.2 (Successful Search — Chaining)
In a hash table with chaining, under independent uniform hashing, a successful search takes **Θ(1 + α)** expected time.

#### Corollary 11.3 (Universal Hashing Performance)
Using universal hashing and chaining in an initially empty table with m slots, any sequence of s INSERT, SEARCH, DELETE operations containing n = O(m) INSERT operations takes **Θ(s)** expected time.

#### Theorem 11.4 (Universal Family H_{pm})
The family `H_{pm} = {h_{ab} : a∈ℤ_p^*, b∈ℤ_p}` with `h_{ab}(k) = ((ak+b) mod p) mod m` is universal.

#### Theorem 11.5 (Multiply-Shift 2/m-Universal)
The family of multiply-shift hash functions with odd constants a is 2/m-universal. Probability of collision ≤ 2/m.

#### Theorem 11.6 (Unsuccessful Search — Open Addressing)
Given an open-address hash table with load factor α < 1, under independent uniform permutation hashing and no deletions, the expected number of probes in an unsuccessful search is at most **1/(1 − α)**.

#### Corollary 11.7 (Insertion — Open Addressing)
Inserting into an open-address hash table with α < 1 requires at most **1/(1 − α)** probes on average.

#### Theorem 11.8 (Successful Search — Open Addressing)
Given an open-address hash table with α < 1, under independent uniform permutation hashing with no deletions, expected probes for successful search is at most **(1/α) ln(1/(1−α))**.

#### Theorem 11.9 (Linear Probing Constant Time)
If h₁ is 5-independent and α ≤ 2/3, then search, insert, or delete in a linear probing hash table takes expected constant time.

### Data Structures & Supported Operations

| Structure | Operations | Time (average) | Time (worst) |
|-----------|-----------|----------------|--------------|
| Direct-address table | SEARCH, INSERT, DELETE | O(1) | O(1) |
| Hash table (chaining) | INSERT | O(1) | O(1) |
| | SEARCH | Θ(1+α) | Θ(n) |
| | DELETE | O(1) (doubly linked) | O(1) |
| Hash table (open addressing) | INSERT | O(1/(1−α)) probes avg | O(m) |
| | SEARCH | O(1/(1−α)) probes avg | O(m) |
| | DELETE | Tricky (needs DELETED marker or linear probing method) | — |

### Comparisons & Trade-offs

| Dimension | Chaining | Open Addressing |
|-----------|----------|-----------------|
| Memory | Extra pointers per chain | No extra pointers; more slots for same memory |
| Load factor | α can be > 1 | α ≤ 1 (table can fill up) |
| Deletion | Easy (list deletion) | Hard (need DELETED or special procedure) |
| Cache performance | Poor (pointers to scattered nodes) | Better (probe sequences local) |
| Implementation | Simple (uses linked lists) | More complex (probe sequences) |
| Performance degrades | Gracefully (longer chains) | Sharply (as α → 1) |

| Dimension | Linear Probing | Double Hashing |
|-----------|---------------|----------------|
| Distinct probe sequences | m | Θ(m²) |
| Cache performance | Excellent (sequential) | Poor (random access) |
| Primary clustering | Yes | No |
| Deletion | Possible (special algorithm) | Requires DELETED marker |
| When to use | Hierarchical memory, α ≤ 2/3 | RAM model, general case |

| Dimension | Division Method | Multiplication Method | Universal Hashing |
|-----------|----------------|----------------------|-------------------|
| Speed | Fast | Fast | Moderate |
| Randomness guarantee | None | None | Yes (provable) |
| Adversary resistance | No | No | Yes |
| Practical use | Legacy | Legacy | Recommended |

### Proof & Argument Patterns

**Chaining expected search time** (Theorem 11.1, 11.2):
1. Define indicator variables for collisions
2. Show E[n_j] = α = n/m
3. Unsuccessful: search to end of list → expected length α
4. Successful: element equally likely; expected elements before = sum of probabilities of later insertions into same slot → (α/2 − α/(2n))
5. Total: Θ(1+α)

**Open addressing expected probes** (Theorem 11.6):
1. Define event A_i = i-th probe occurs and is to occupied slot
2. Pr{A₁} = n/m; Pr{Aⱼ | first j−1 occupied} = (n−j+1)/(m−j+1) ≤ n/m
3. Pr{X ≥ i} ≤ (n/m)^{i−1}
4. E[X] = Σ Pr{X ≥ i} ≤ Σ (n/m)^{i−1} = 1/(1−α)

**Universal family proof** (Theorem 11.4):
1. For distinct k₁,k₂, let r₁ = (ak₁+b) mod p, r₂ = (ak₂+b) mod p
2. Since p prime and a ≠ 0: r₁ ≠ r₂
3. r₁,r₂ uniformly distributed among distinct pairs modulo p
4. Collision probability = Pr{r₁ ≡ r₂ (mod m)} ≤ 1/m

### Edge Cases & Common Pitfalls

- **Worst-case chaining**: All n keys hash to same slot → Θ(n) search (mitigated by universal hashing)
- **Deletion in open addressing**: Cannot simply store NIL; breaks search for subsequent keys → use DELETED marker (which degrades performance) or special linear probing method
- **Primary clustering** (linear probing): Long runs build up; empty slot preceded by i full slots gets filled with probability (i+1)/m
- **Load factor too high in open addressing**: As α → 1, probes → ∞; at α = 1, unsuccessful search probes all m slots
- **m must be prime for double hashing** when h₂(k) = 1 + (k mod m′) to ensure full coverage
- **Division method with power-of-2 m**: Certain key patterns collide frequently
- **Sentinel in chaining**: Not typically used; list operations from Ch.10 handle NIL
- **Distinct keys**: Analysis assumes distinct keys; repeated keys break search assumptions

### End-of-Chapter Material

**Key terms**: Direct-address table, hash table, hash function, collision, chaining, load factor, independent uniform hashing, division method, multiplication method, multiply-shift method, universal hashing, ϵ-universal, d-independent, open addressing, probe sequence, double hashing, linear probing, primary clustering, cryptographic hash function, random oracle, wee hash.

**Key results**:
- Chaining: Θ(1+α) average search time
- Open addressing: 1/(1−α) average unsuccessful probes
- Universal hashing: O(1) expected time per operation for any input
- Linear probing: Expected O(1) with 5-independent hash and α ≤ 2/3

**Historical milestones**:
- Hash tables invented by H.P. Luhn (1953)
- Open addressing by G.M. Amdahl (c. 1953)
- Universal hashing introduced by Carter & Wegman (1979)
- Multiply-shift by Dietzfelbinger et al.

---

## Ch. 12 — Binary Search Trees

### Named Entities (Terms & Definitions)

- **Binary search tree**: Binary tree satisfying the binary-search-tree property.
- **Binary-search-tree property**: For any node x, all keys in left subtree ≤ x.key ≤ all keys in right subtree.
- **Inorder tree walk**: Visit left subtree, then root, then right subtree — prints keys in sorted order.
- **Preorder tree walk**: Visit root, then left subtree, then right subtree.
- **Postorder tree walk**: Visit left subtree, then right subtree, then root.
- **Successor**: Next node visited in inorder tree walk (smallest key > x.key if distinct).
- **Predecessor**: Previous node visited in inorder tree walk.
- **Tree height** (h): Length of longest path from root to leaf.
- **Randomly built BST**: BST created by inserting keys in random order (each of n! permutations equally likely); expected height O(lg n).
- **Radix tree** (trie): Tree storing bit strings where left=0, right=1 at each node.
- **Catalan number**: Number of distinct binary trees with n nodes is `b_n = (1/(n+1))·C(2n, n)`.
- **Total path length** P(T): Sum of depths of all nodes in tree T.
- **Trailing pointer**: Pointer `y` maintained as parent of current node `x` during tree traversal.

### Processes / Algorithms / Pseudocode

#### INORDER-TREE-WALK(x)
```
1 if x ≠ NIL
2     INORDER-TREE-WALK(x.left)
3     print x.key
4     INORDER-TREE-WALK(x.right)
```
- **Complexity**: Θ(n) for n-node subtree
- **Output**: Keys in sorted (non-decreasing) order
- **Proof**: Substitution method with T(n) ≤ (c+d)n + c

#### TREE-SEARCH(x, k)
```
1 if x == NIL or k == x.key
2     return x
3 if k < x.key
4     return TREE-SEARCH(x.left, k)
5 else return TREE-SEARCH(x.right, k)
```
- **Complexity**: O(h), where h = tree height
- **Recursive**: Traces simple path from root downward

#### ITERATIVE-TREE-SEARCH(x, k)
```
1 while x ≠ NIL and k ≠ x.key
2     if k < x.key
3         x = x.left
4     else x = x.right
5 return x
```
- **Complexity**: O(h)
- **Note**: More efficient on most computers (no recursion overhead)

#### TREE-MINIMUM(x)
```
1 while x.left ≠ NIL
2     x = x.left
3 return x
```
- **Complexity**: O(h)
- **Correctness**: Binary-search-tree property guarantees min is leftmost node

#### TREE-MAXIMUM(x)
```
1 while x.right ≠ NIL
2     x = x.right
3 return x
```
- **Complexity**: O(h)

#### TREE-SUCCESSOR(x)
```
1 if x.right ≠ NIL
2     return TREE-MINIMUM(x.right)     // leftmost node in right subtree
3 else
4     y = x.p
5     while y ≠ NIL and x == y.right
6         x = y
7         y = y.p
8     return y
```
- **Complexity**: O(h)
- **Two cases**: (1) right subtree nonempty → min of right subtree; (2) right subtree empty → go up until finding ancestor whose left child is also ancestor

#### TREE-PREDECESSOR(x)
- Symmetric to TREE-SUCCESSOR
- Complexity: O(h)

#### TREE-INSERT(T, z)
```
 1 x = T.root
 2 y = NIL
 3 while x ≠ NIL
 4     y = x
 5     if z.key < x.key
 6         x = x.left
 7     else x = x.right
 8 z.p = y
 9 if y == NIL
10     T.root = z
11 elseif z.key < y.key
12     y.left = z
13 else y.right = z
```
- **Complexity**: O(h)
- **Input**: Tree T, node z with z.key set, z.left = z.right = NIL
- **Strategy**: Traverse to leaf position, insert as child

#### TRANSPLANT(T, u, v)
```
1 if u.p == NIL
2     T.root = v
3 elseif u == u.p.left
4     u.p.left = v
5 else u.p.right = v
6 if v ≠ NIL
7     v.p = u.p
```
- **Complexity**: O(1)
- **Purpose**: Replaces subtree rooted at u with subtree rooted at v
- **Note**: Does NOT update v.left or v.right — caller's responsibility

#### TREE-DELETE(T, z)
```
 1 if z.left == NIL
 2     TRANSPLANT(T, z, z.right)
 3 elseif z.right == NIL
 4     TRANSPLANT(T, z, z.left)
 5 else y = TREE-MINIMUM(z.right)
 6     if y ≠ z.right
 7         TRANSPLANT(T, y, y.right)
 8         y.right = z.right
 9         y.right.p = y
10     TRANSPLANT(T, z, y)
11     y.left = z.left
12     y.left.p = y
```
- **Complexity**: O(h)
- **Four cases**:
  1. z has no left child → replace by right child (handles no children and only right child)
  2. z has left but no right child → replace by left child
  3. z has two children, successor y = z.right → replace z by y, straight
  4. z has two children, successor y ≠ z.right → transplant y by its right child, then replace z by y

### Rules, Laws & Theorems

#### BST Property
For any node x: all keys in left subtree ≤ x.key ≤ all keys in right subtree.

#### Theorem 12.1 (Inorder Walk Linearity)
If x is root of n-node subtree, INORDER-TREE-WALK(x) takes Θ(n) time.

#### Theorem 12.2 (Query Operations)
SEARCH, MINIMUM, MAXIMUM, SUCCESSOR, PREDECESSOR run in O(h) time on BST of height h.

#### Theorem 12.3 (Modify Operations)
INSERT and DELETE run in O(h) time on BST of height h.

#### Property of BST Deletion
If a node has two children, its successor has no left child (and its predecessor has no right child). (Exercise 12.2-5)

#### Comparison Model Lower Bound
Building a BST from n arbitrary elements takes Ω(n lg n) worst-case comparisons (Exercise 12.1-5).

### Data Structures

| Operation | Time (balanced) | Time (worst-case chain) |
|-----------|----------------|------------------------|
| SEARCH | O(lg n) | Θ(n) |
| MINIMUM | O(lg n) | Θ(n) |
| MAXIMUM | O(lg n) | Θ(n) |
| SUCCESSOR | O(lg n) | Θ(n) |
| PREDECESSOR | O(lg n) | Θ(n) |
| INSERT | O(lg n) | Θ(n) |
| DELETE | O(lg n) | Θ(n) |
| INORDER-WALK | Θ(n) | Θ(n) |

### Comparisons & Trade-offs

| Dimension | BST (balanced) | Sorted Array | Linked List |
|-----------|---------------|--------------|-------------|
| SEARCH | O(lg n) | O(lg n) (binary search) | Θ(n) |
| INSERT | O(lg n) | Θ(n) (shift) | O(1) (with pointer) |
| DELETE | O(lg n) | Θ(n) (shift) | O(1) (doubly linked) |
| Successor/Predecessor | O(lg n) | O(1) (adjacent) | Θ(n) |
| Memory | 3 pointers/node | n slots | 1-2 pointers/node |

### Edge Cases & Common Pitfalls

- **Unbalanced BST**: Worst-case height Θ(n) when keys inserted in sorted order → BST becomes linear chain
- **Deleting node with two children**: Must carefully handle case where successor is not right child (requires secondary transplant)
- **Equal keys**: BST property uses ≤ / ≥ on both sides; implementation must decide left vs right for equal keys
- **Successor of node with empty right subtree**: Must traverse up; confusing to implement correctly
- **TRANSPLANT does not update children**: Caller must handle left/right updates
- **Root deletion**: TREE-DELETE handles via TRANSPLANT which checks for nil parent

### End-of-Chapter Material

**Key terms**: Binary search tree, binary-search-tree property, inorder tree walk, preorder tree walk, postorder tree walk, successor, predecessor, tree height, randomly built BST, radix tree (trie), Catalan number, total path length.

**Key results**:
- BST operations O(h) where h = height
- Worst-case h = Θ(n) (degenerate), best-case h = Θ(lg n)
- Inorder walk prints sorted order in Θ(n)
- Random BST has expected height O(lg n)
- Catalan number C_n = number of distinct BSTs with n nodes

---

## Ch. 13 — Red-Black Trees

### Named Entities (Terms & Definitions)

- **Red-black tree**: Self-balancing BST with one extra bit (color: RED or BLACK) per node.
- **Red-black properties**:
  1. Every node is either red or black.
  2. The root is black.
  3. Every leaf (NIL) is black.
  4. If a node is red, then both its children are black. (No two reds in a row.)
  5. For each node, all simple paths from the node to descendant leaves contain the same number of black nodes.
- **Black-height** `bh(x)`: Number of black nodes on any simple path from (but not including) node x down to a leaf.
- **Sentinel `T.nil`**: Single sentinel representing all NIL leaves; color BLACK.
- **Rotation**: Local pointer restructuring preserving BST property; O(1) time.
- **Left rotation**: Transforms x-y structure so y becomes new root of subtree, x becomes left child.
- **Right rotation**: Inverse of left rotation.
- **Uncle**: Sibling of a node's parent (used in RB-INSERT-FIXUP and RB-DELETE-FIXUP).
- **Internal node**: Key-bearing node (non-NIL).
- **Doubly black**: Extra black on a node during RB-DELETE-FIXUP (violation of property 1).
- **Red-and-black**: Node with extra black that is originally red.
- **Persistent data structure**: Maintains past versions; copying only part of tree.
- **AVL tree**: BST where heights of left/right subtrees differ by at most 1 (Problem 13-3).
- **Treap**: Hybrid of BST and heap; randomized dictionary.
- **Splay tree**: Self-adjusting BST with amortized O(lg n) per operation.
- **AA-tree**: Red-black variant where left children cannot be red.
- **Left-leaning red-black tree**: Red-black tree where only left children can be red.
- **Join operation**: Combine two red-black trees and a separating key.

### Processes / Algorithms / Pseudocode

#### LEFT-ROTATE(T, x)
```
 1 y = x.right
 2 x.right = y.left          // turn y's left subtree into x's right subtree
 3 if y.left ≠ T.nil
 4     y.left.p = x
 5 y.p = x.p                 // x's parent becomes y's parent
 6 if x.p == T.nil
 7     T.root = y
 8 elseif x == x.p.left
 9     x.p.left = y
10 else x.p.right = y
11 y.left = x                // make x become y's left child
12 x.p = y
```
- **Complexity**: O(1)
- **Precondition**: x.right ≠ T.nil
- **Preserves**: BST property and inorder ordering

#### RIGHT-ROTATE(T, y)
Symmetric to LEFT-ROTATE. Formally:
```
1 x = y.left
2 y.left = x.right
3 if x.right ≠ T.nil
4     x.right.p = y
5 x.p = y.p
6 if y.p == T.nil
7     T.root = x
8 elseif y == y.p.right
9     y.p.right = x
10 else y.p.left = x
11 x.right = y
12 y.p = x
```
- Complexity: O(1)

#### RB-INSERT(T, z)
```
 1 x = T.root
 2 y = T.nil
 3 while x ≠ T.nil
 4     y = x
 5     if z.key < x.key
 6         x = x.left
 7     else x = x.right
 8 z.p = y
 9 if y == T.nil
10     T.root = z
11 elseif z.key < y.key
12     y.left = z
13 else y.right = z
14 z.left = T.nil
15 z.right = T.nil
16 z.color = RED
17 RB-INSERT-FIXUP(T, z)
```
- **Complexity**: O(lg n) [O(lg n) for BST insert + O(lg n) for fixup]
- **Differences from TREE-INSERT**: (1) NIL → T.nil; (2) sets z.left = z.right = T.nil; (3) colors z RED; (4) calls RB-INSERT-FIXUP

#### RB-INSERT-FIXUP(T, z)
```
 1 while z.p.color == RED
 2     if z.p == z.p.p.left            // parent is left child
 3         y = z.p.p.right               // uncle
 4         if y.color == RED              // CASE 1: uncle red
 5             z.p.color = BLACK
 6             y.color = BLACK
 7             z.p.p.color = RED
 8             z = z.p.p
 9         else                           // uncle black: cases 2 & 3
10             if z == z.p.right           // CASE 2: z is right child
11                 z = z.p
12                 LEFT-ROTATE(T, z)
13             z.p.color = BLACK           // CASE 3: z is left child
14             z.p.p.color = RED
15             RIGHT-ROTATE(T, z.p.p)
16     else                                // symmetric (parent is right child)
17         y = z.p.p.left
18         if y.color == RED
19             z.p.color = BLACK
20             y.color = BLACK
21             z.p.p.color = RED
22             z = z.p.p
23         else
24             if z == z.p.left
25                 z = z.p
26                 RIGHT-ROTATE(T, z)
27             z.p.color = BLACK
28             z.p.p.color = RED
29             LEFT-ROTATE(T, z.p.p)
30 T.root.color = BLACK
```
- **Complexity**: O(lg n); at most 2 rotations performed
- **Loop invariant**:
  - (a) z is red
  - (b) If z.p is root, it is black
  - (c) At most one violation: property 2 (z red root) or property 4 (z and z.p both red)

**Three cases** (when parent is left child):
- **Case 1** (uncle red): Recolor parent, uncle, grandparent; move z up two levels
- **Case 2** (uncle black, z is right child): Left rotation → becomes Case 3
- **Case 3** (uncle black, z is left child): Recolor + right rotation; loop terminates

#### RB-TRANSPLANT(T, u, v)
```
1 if u.p == T.nil
2     T.root = v
3 elseif u == u.p.left
4     u.p.left = v
5 else u.p.right = v
6 v.p = u.p
```
- **Differences from TRANSPLANT**: NIL → T.nil; v.p assigned unconditionally (even if v = T.nil)

#### RB-DELETE(T, z)
```
 1 y = z
 2 y-original-color = y.color
 3 if z.left == T.nil
 4     x = z.right
 5     RB-TRANSPLANT(T, z, z.right)
 6 elseif z.right == T.nil
 7     x = z.left
 8     RB-TRANSPLANT(T, z, z.left)
 9 else y = TREE-MINIMUM(z.right)
10     y-original-color = y.color
11     x = y.right
12     if y ≠ z.right
13         RB-TRANSPLANT(T, y, y.right)
14         y.right = z.right
15         y.right.p = y
16     else x.p = y
17     RB-TRANSPLANT(T, z, y)
18     y.left = z.left
19     y.left.p = y
20     y.color = z.color
21 if y-original-color == BLACK
22     RB-DELETE-FIXUP(T, x)
```
- **Complexity**: O(lg n)
- **Key idea**: `y` = node actually removed or moved; `x` = node that takes y's original position
- If y was originally BLACK → violations possible → call RB-DELETE-FIXUP
- If y was originally RED → no violations (black-heights unchanged, no adjacent reds, root stays black)

#### RB-DELETE-FIXUP(T, x)
```
 1 while x ≠ T.root and x.color == BLACK
 2     if x == x.p.left                        // x is left child
 3         w = x.p.right                         // sibling
 4         if w.color == RED                     // CASE 1: sibling red
 5             w.color = BLACK
 6             x.p.color = RED
 7             LEFT-ROTATE(T, x.p)
 8             w = x.p.right
 9         if w.left.color == BLACK and w.right.color == BLACK  // CASE 2
10             w.color = RED
11             x = x.p
12         else
13             if w.right.color == BLACK         // CASE 3
14                 w.left.color = BLACK
15                 w.color = RED
16                 RIGHT-ROTATE(T, w)
17                 w = x.p.right
18             w.color = x.p.color               // CASE 4
19             x.p.color = BLACK
20             w.right.color = BLACK
21             LEFT-ROTATE(T, x.p)
22             x = T.root
23     else                                      // symmetric (x is right child)
24         w = x.p.left
25         if w.color == RED
26             w.color = BLACK
27             x.p.color = RED
28             RIGHT-ROTATE(T, x.p)
29             w = x.p.left
30         if w.right.color == BLACK and w.left.color == BLACK
31             w.color = RED
32             x = x.p
33         else
34             if w.left.color == BLACK
35                 w.right.color = BLACK
36                 w.color = RED
37                 LEFT-ROTATE(T, w)
38                 w = x.p.left
39             w.color = x.p.color
40             x.p.color = BLACK
41             w.left.color = BLACK
42             RIGHT-ROTATE(T, x.p)
43             x = T.root
44 x.color = BLACK
```
- **Complexity**: O(lg n); at most 3 rotations (cases 1,3,4 terminate; case 2 may repeat)
- **Node `x`**: "doubly black" or "red-and-black" — carries extra black from y's removal

**Four cases** (when x is left child):
- **Case 1** (sibling w red): Swap colors of w and x.p; left-rotate x.p → converts to case 2/3/4
- **Case 2** (w black, both w's children black): Remove one black from x and w; add extra black to x.p; move x up
- **Case 3** (w black, w's left red, w's right black): Swap colors of w and w.left; right-rotate w → becomes case 4
- **Case 4** (w black, w's right red): Recolor w to x.p's color, x.p black, w.right black; left-rotate x.p; x = T.root → loop terminates

### Rules, Laws & Theorems

#### Lemma 13.1 (Height Bound)
A red-black tree with n internal nodes has height **h ≤ 2 lg(n + 1)**. Therefore, h = O(lg n).

**Proof sketch**:
1. Show by induction: subtree at x contains ≥ 2^{bh(x)} − 1 internal nodes
2. Property 4: at least half the nodes on any root-to-leaf path are black → bh(root) ≥ h/2
3. n ≥ 2^{h/2} − 1 → h ≤ 2 lg(n + 1)

#### Red-Black Properties Summary
1. Every node RED or BLACK
2. Root BLACK
3. Every leaf (NIL) BLACK
4. Red node → children BLACK (no consecutive reds)
5. Equal black nodes on every simple path from any node to descendant leaves

#### Black-Height Property
The black-height of a red node is the same as the black-height of its parent (since red doesn't count).
A black child has black-height = bh(parent) − 1; a red child has black-height = bh(parent).

#### Maximum Rotations
- RB-INSERT-FIXUP: at most 2 rotations
- RB-DELETE-FIXUP: at most 3 rotations

### Comparisons & Trade-offs

| Dimension | BST (unbalanced) | Red-Black Tree |
|-----------|-----------------|----------------|
| Height | Θ(n) worst-case | ≤ 2 lg(n+1) |
| SEARCH/INSERT/DELETE | O(n) worst-case | O(lg n) worst-case |
| Rotations per modification | 0 | ≤ 3 |
| Space overhead | 3 pointers | 3 pointers + color bit |
| Implementation complexity | Simple | Complex (6 insertion cases, 8 deletion cases) |

| Dimension | Red-Black Tree | AVL Tree |
|-----------|---------------|----------|
| Balance condition | Color-based, height ≤ 2 lg(n+1) | Height difference ≤ 1 |
| Height bound | ≤ 2 lg(n+1) | ≤ 1.44 lg n (tighter) |
| Insert rotations | ≤ 2 | O(lg n) |
| Delete rotations | ≤ 3 | O(lg n) |
| Use case | General purpose, frequent inserts/deletes | Search-heavy workloads |

### Proof & Argument Patterns

**Height bound proof** (Lemma 13.1):
1. Inductive claim: subtree at x has ≥ 2^{bh(x)} − 1 internal nodes
2. Base: height 0 (leaf) → 0 internal nodes = 2^0 − 1
3. Inductive step: children have bh = bh(x) or bh(x)−1 → each has ≥ 2^{bh(x)−1} − 1 nodes → total ≥ (2^{bh−1}−1)+(2^{bh−1}−1)+1 = 2^{bh} − 1
4. Root bh ≥ h/2 (at least half nodes on any path are black) → n ≥ 2^{h/2} − 1 → h ≤ 2 lg(n+1)

**RB-INSERT-FIXUP loop invariant proof**:
- Initialization: holds after RB-INSERT (z red, z.p black if root, only property 2 or 4 possibly violated)
- Maintenance: Cases 1-3 shown to maintain invariant (z remains red, violation moves up or resolves)
- Termination: z.p becomes black (property 4 restored) or z reaches root; line 30 colors root black (property 2)

**RB-DELETE-FIXUP extra-black idea**:
- When black node y is removed/moved, its blackness transfers to x (the node taking y's place)
- x becomes "doubly black" or "red-and-black" (violates property 1)
- Cases 1-4 move the extra black up or eliminate it while preserving other properties

### Edge Cases & Common Pitfalls

- **Root red after fixup**: RB-INSERT-FIXUP line 30 ensures root always black
- **Sentinel T.nil**: Must be treated as ordinary node with parent pointer; RB-TRANSPLANT assigns v.p unconditionally even for sentinel
- **RB-DELETE-FIXUP Case 2**: Only case that repeats loop; can propagate up O(lg n) times
- **RB-DELETE y-original-color**: Must track y's original color before any changes; only call fixup if y was BLACK
- **x.p must be set correctly**: Even when x = T.nil, x.p must be correct (RB-DELETE ensures this)
- **Red node cannot have exactly one non-NIL child** (Exercise 13.1-8): would violate property 4 and 5 simultaneously
- **Succssor has no left child**: Critical property for both BST and RB deletion
- **Persistent trees**: Without parent pointers, insertion copies O(h) nodes; with parent pointers, O(n) copying needed

### End-of-Chapter Material

**Key terms**: Red-black tree, red-black properties, black-height, rotation, left rotation, right rotation, uncle, sentinel, double black, red-and-black, persistent data structure, AVL tree, join, treap, splay tree, AA-tree, left-leaning red-black tree.

**Key results**:
- h ≤ 2 lg(n+1) → O(lg n) for all operations
- RB-INSERT: O(lg n), ≤ 2 rotations
- RB-DELETE: O(lg n), ≤ 3 rotations
- Fixed number of rotations per modify operation (important for amortized analysis in Ch.17)

---

## Cross-Cutting Topics

### Design Paradigms

- **Divide-and-conquer (hashing as nonrecursive form)**: Chaining divides n elements randomly into m subsets of ≈ n/m each; each subset managed independently as a list.
- **Randomization**: Universal hashing, randomly built BSTs, randomized skip-ahead in compact list search.
- **Trade-off engineering**: Memory vs time (direct-address vs hash table), pointer overhead vs faster operations (singly vs doubly linked), LIFO/FIFO vs arbitrary access.

### Proof Patterns

1. **Indicator random variables**: Used in chaining analysis to compute expected search time (sum over collisions).
2. **Loop invariants**: RB-INSERT-FIXUP and RB-DELETE-FIXUP proven correct with invariant + termination + postcondition.
3. **Induction**: Height bound of red-black trees (Lemma 13.1); inorder walk linear time (Theorem 12.1).
4. **Amortized counting**: Expected probes = Pr{≥1} + Pr{≥2} + Pr{≥3} + ... = Σ Pr{X ≥ i}.
5. **One-to-one correspondence**: Universal family proof shows injection from (a,b) to (r₁,r₂) pairs.

### Mnemonics

- **BST Property**: "Left ≤ Node ≤ Right" (for any node)
- **RB Properties**: "Root Black, Leaves Black, No Red-Red, Same Black-Count"
- **RB-INSERT Cases**: "Uncle red → recolor up; Uncle black, zig-zag → rotate then recolor; Uncle black, straight → recolor and rotate"
- **RB-DELETE Cases**: "Sibling red → rotate; Sibling black + kids black → push black up; Sibling black + far kid black → rotate sibling; Sibling black + far kid red → recolor and rotate"
- **Inorder walk order**: "Left, Print, Right"

### People & Dates

- **Stacks/queues**: A.M. Turing (1947, stack for subroutine linkage); IPL languages (Newell, Shaw, Simon, 1956-57)
- **Hash tables**: H.P. Luhn (1953, invention + chaining); G.M. Amdahl (c. 1953, open addressing)
- **Universal hashing**: Carter & Wegman (1979)
- **Red-black trees**: R. Bayer (1972, "symmetric binary B-trees"); Guibas & Sedgewick (1978, red/black color convention)
- **AVL trees**: Adel'son-Vel'skiĭ & Landis (1962)
- **B-trees**: Bayer & McCreight (1972)
- **Treaps**: Seidel & Aragon (1996)

---

## Exam Questions by Type

### MCQ

1. **Q:** What is the worst-case time for SEARCH in a hash table with chaining under independent uniform hashing?
   **A:** Θ(1 + α) on average; Θ(n) worst-case
   **Distractor:** Θ(1) — this is average-case, not worst-case

2. **Q:** How many rotations can RB-INSERT-FIXUP perform at most?
   **A:** 2
   **Distractor:** O(lg n) — that's the number of color changes in case 1, but rotations ≤ 2

3. **Q:** In a red-black tree, if a node is red, what can be said about its children?
   **A:** Both children must be black (property 4)
   **Distractor:** At least one child is black — doesn't guarantee both are black

4. **Q:** What is the expected number of probes in an unsuccessful open-address search when α = 0.9?
   **A:** ≤ 1/(1−0.9) = 10
   **Distractor:** 2.559 — that's for a successful search

### Short Answer

1. **Q:** State the five red-black tree properties.
   **Rubric:** (1) Each node red or black (2) Root black (3) Leaves (NIL) black (4) Red's children black (5) Equal black count on all paths

2. **Q:** What is the load factor α in a hash table, and why does it matter?
   **Rubric:** α = n/m. For chaining: search time Θ(1+α). For open addressing: probes ∼ 1/(1−α). Higher α → worse performance.

3. **Q:** Why does deletion in open-addressed hash tables require special handling?
   **Rubric:** Simply setting slot to NIL breaks the probe sequence for subsequent keys (they may have probed this occupied slot). Must use DELETED marker or relocate keys.

### Trace / Apply

1. **Input:** Insert keys 41, 38, 31, 12, 19, 8 into an empty red-black tree. Show the tree after each step.
   **Expected:** Final tree should be a valid red-black tree (follow RB-INSERT-FIXUP cases). The sequence traces cases 1, 2, 3 at various steps.

2. **Input:** Hash table size m=11, h₁(k)=k mod 11, h₂(k)=1+(k mod 10). Insert 10,22,31,4,15,28,17,88,59 using double hashing.
   **Expected:** Trace probe sequences for each key until empty slot found.

3. **Input:** Delete nodes 8, 12, 19, 31, 38, 41 from the red-black tree built above. Show tree after each deletion.
   **Expected:** Trace RB-DELETE cases.

### Essay / Long-Form

1. **Q:** Compare and contrast chaining and open addressing for collision resolution in hash tables.
   **Key points to include:** Memory usage, load factor constraints, deletion difficulty, cache performance, probe sequence generation, expected search times.

2. **Q:** Prove that a red-black tree with n internal nodes has height at most 2 lg(n + 1).
   **Key points to include:** Inductive proof on black-height, property 4 guarantees bh(root) ≥ h/2, algebraic manipulation.

3. **Q:** Analyze the expected performance of hashing with chaining under independent uniform hashing. Include both successful and unsuccessful search.
   **Key points to include:** Definition of α, indicator random variables, E[n_j] = α, Θ(1+α) bound, universal hashing as practical substitute.
