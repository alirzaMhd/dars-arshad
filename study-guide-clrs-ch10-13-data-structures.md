# Study Guide: Introduction to Algorithms (CLRS 4e) — Part III: Data Structures (Ch. 10–13)

> Generated 2026-06-05. Subject: Computer Science. Coverage: comprehensive for Ch. 10–13.

## Chapter-by-Chapter Breakdown

### Ch. 10 — Elementary Data Structures

#### Named Entities (Terms & Definitions)
- **Array**: contiguous sequence of bytes; element i at address a + b(i − s) for 1-origin (s=1) or a + bi for 0-origin (s=0); O(1) access
- **Matrix**: m × n grid; stored row-major or column-major in one or more arrays
- **Row-major order**: M[i,j] at index n(i−1)+j (1-origin); rows stored contiguously
- **Column-major order**: M[i,j] at index i + m(j−1) (1-origin); columns stored contiguously
- **Block representation**: matrix divided into blocks, each stored contiguously
- **Stack**: LIFO dynamic set; INSERT=PUSH, DELETE=POP; attribute S.top
- **Queue**: FIFO dynamic set; INSERT=ENQUEUE, DELETE=DEQUEUE; attributes Q.head, Q.tail; uses circular array
- **Deque**: double-ended queue; insertion/deletion at both ends
- **Linked list**: linear order determined by pointers (not array indices)
- **Doubly linked list**: each node has key, next, prev pointers
- **Singly linked list**: each node has next but no prev pointer
- **Circular list**: tail.next = head, head.prev = tail
- **Sentinel**: dummy node (L.nil) simplifying boundary conditions; replaces NIL references
- **Left-child, right-sibling representation**: each node has x.left-child (leftmost child) and x.right-sibling (next sibling); O(n) space for n-node tree

#### Processes / Algorithms / Pathways
##### STACK-EMPTY(S)
- **Type**: Algorithm
- **Steps**: (1) if S.top == 0 return TRUE (2) else return FALSE
- **Complexity**: O(1)

##### PUSH(S, x)
- **Type**: Algorithm
- **Goal**: Insert element x onto stack
- **Steps**: (1) if S.top == S.size → error "overflow" (2) S.top = S.top + 1 (3) S[S.top] = x
- **Complexity**: O(1)
- **Example**: Stack S = [1,4,9,16], S.top=4. PUSH(S,25): S.top=5, S[5]=25. Stack now [1,4,9,16,25].

##### POP(S)
- **Type**: Algorithm
- **Goal**: Remove and return top element
- **Steps**: (1) if STACK-EMPTY(S) → error "underflow" (2) S.top = S.top − 1 (3) return S[S.top + 1]
- **Complexity**: O(1)
- **Example**: POP from [1,4,9,16]: returns 16, S.top=3.

##### ENQUEUE(Q, x)
- **Type**: Algorithm
- **Steps**: (1) Q[Q.tail] = x (2) if Q.tail == Q.size → Q.tail = 1 else Q.tail = Q.tail + 1
- **Complexity**: O(1)
- **Example**: Q=[ _, _, _, 15, 6, 9, 8, 4], head=4, tail=1. ENQUEUE(Q,17): Q[1]=17, tail=2.

##### DEQUEUE(Q)
- **Type**: Algorithm
- **Steps**: (1) x = Q[Q.head] (2) if Q.head == Q.size → Q.head = 1 else Q.head = Q.head + 1 (3) return x
- **Complexity**: O(1)

##### LIST-SEARCH(L, k)
- **Steps**: (1) x = L.head (2) while x ≠ NIL and x.key ≠ k: x = x.next (3) return x
- **Complexity**: Θ(n) worst-case
- **Example**: List L = [9,16,4,1]. LIST-SEARCH(L,4) returns pointer to 3rd element. LIST-SEARCH(L,7) returns NIL.

##### LIST-PREPEND(L, x)
- **Steps**: (1) x.next = L.head (2) x.prev = NIL (3) if L.head ≠ NIL: L.head.prev = x (4) L.head = x
- **Complexity**: O(1)

##### LIST-INSERT(x, y)
- **Steps**: Insert x immediately after y: (1) x.next = y.next (2) x.prev = y (3) if y.next ≠ NIL: y.next.prev = x (4) y.next = x
- **Complexity**: O(1)

##### LIST-DELETE(L, x)
- **Steps**: (1) if x.prev ≠ NIL: x.prev.next = x.next else L.head = x.next (2) if x.next ≠ NIL: x.next.prev = x.prev
- **Complexity**: O(1) (plus Θ(n) to find the element via LIST-SEARCH)

##### LIST-SEARCH'(L, k) — sentinel version
- **Steps**: (1) L.nil.key = k (2) x = L.nil.next (3) while x.key ≠ k: x = x.next (4) if x == L.nil return NIL else return x
- **Complexity**: Θ(n); eliminates one comparison per iteration

#### Comparisons & Trade-offs
| Dimension | Array | Doubly Linked List |
|---|---|---|
| Access k-th element | O(1) | Θ(k) |
| Insert at front | Θ(n) (must shift) | O(1) (LIST-PREPEND) |
| Delete first element | Θ(n) | O(1) |
| Search | Θ(n) (unsorted) | Θ(n) |
| Space | n elements | n elements + 2n pointers |
| Sentinels benefit | N/A | Simplifies code, small constant speedup |

#### Formulas & Equations
##### Array element address (1-origin)
`address = a + b(i − 1)`
- a = base memory address [bytes]
- b = element size [bytes]
- i = 1-based index

##### Row-major index (1-origin)
`index = n(i − 1) + j`
- n = number of columns
- i = row index, j = column index

##### Column-major index (1-origin)
`index = i + m(j − 1)`
- m = number of rows

#### Edge Cases & Common Pitfalls
- **Stack underflow**: POP from empty stack (S.top = 0)
- **Stack overflow**: PUSH to full stack (S.top = S.size)
- **Queue underflow**: DEQUEUE from empty queue (Q.head = Q.tail)
- **Queue overflow**: ENQUEUE to full queue (Q.head = Q.tail + 1 in circular sense)
- **Singly linked list deletion**: O(n) worst-case because predecessor must be found
- **Sentinel overuse**: wastes memory on many small lists
- **Deletion with sentinel**: never delete the sentinel itself

#### Diagrams & Visuals
```
Array implementation of stack S[1:n]:
  bottom → [e1][e2][e3][e4][ ]...[ ]
                    ↑ S.top

Circular queue Q[1:n]:
  head → [ ][ ][ ][15][6][9][8][4] ← tail
         ↑              ↑
       tail=1         head=4

Doubly linked list with sentinel:
  L.nil ⇄ head-node ⇄ ... ⇄ tail-node ⇄ L.nil

Binary tree representation:
    T.root → [p,left,right]
              /       \
          [p,l,r]   [p,l,r]

Left-child, right-sibling:
  parent → left-child → right-sibling → right-sibling → NIL
```

#### End-of-Chapter Material
- **Key terms**: array, matrix, row-major, column-major, block representation, stack (LIFO), queue (FIFO), deque, linked list, doubly/singly linked, circular list, sentinel, left-child right-sibling representation
- **Exercises 10.1**: implement two stacks in one array; implement queue using two stacks; implement stack using two queues
- **Exercises 10.2**: implement stack/queue with singly linked list; reverse singly linked list in Θ(n) with constant space; XOR doubly linked list (x.np = x.next XOR x.prev)
- **Problems 10-1**: comparison of list types (unsorted/sorted, singly/doubly) for SEARCH, INSERT, DELETE, SUCCESSOR, PREDECESSOR, MINIMUM, MAXIMUM
- **Problems 10-3**: Compact list search with randomization — expected O(√n) time

#### Cross-Chapter Links
- **Requires**: Ch. 2 (RAM model, Big-O notation), Appendix B (tree math)
- **Referenced in**: Ch. 6 (heaps as arrays), Ch. 11 (chaining uses linked lists), Ch. 12 (BST uses binary tree representation), Ch. 13 (red-black trees use sentinel)

---

### Ch. 11 — Hash Tables

#### Named Entities (Terms & Definitions)
- **Direct-address table**: array T[0:m−1] where slot k stores element with key k; O(1) dictionary operations
- **Hash table**: array T[0:m−1] where element with key k stored in slot h(k); size m ≪ |U|
- **Hash function h**: U → {0,1,…,m−1}; maps keys to slots
- **Collision**: two distinct keys hash to same slot
- **Load factor α**: α = n/m (n elements, m slots); for chaining α can be >1; for open addressing α ≤ 1
- **Chaining**: each slot points to linked list of keys hashing to that slot
- **Independent uniform hashing**: h(k) uniformly random from {0,…,m−1}, independent across keys
- **Universal hashing**: family H where for any distinct k₁,k₂, Pr[h(k₁)=h(k₂)] ≤ 1/m
- **ϵ-universal**: collision probability ≤ ϵ
- **d-independent**: for any d distinct keys, Pr[h(kᵢ)=qᵢ ∀i] = 1/mᵈ
- **Division method**: h(k) = k mod m (m prime, not near power of 2)
- **Multiplication method**: h(k) = ⌊m(kA mod 1)⌋, 0<A<1
- **Multiply-shift**: hₐ(k) = (ka mod 2ʷ) ⋙ (w−ℓ); for m=2ℓ, w-bit words
- **Open addressing**: all elements in table; no external storage; α ≤ 1
- **Probe sequence**: 〈h(k,0), h(k,1), …, h(k,m−1)〉 — must be permutation of 〈0,…,m−1〉
- **Double hashing**: h(k,i) = (h₁(k) + i·h₂(k)) mod m; requires h₂(k) relatively prime to m
- **Linear probing**: h(k,i) = (h₁(k) + i) mod m; suffers primary clustering
- **Independent uniform permutation hashing**: probe sequence of each key equally likely any permutation
- **Primary clustering**: long runs of occupied slots in linear probing; empty slot preceded by i full slots filled with probability (i+1)/m
- **Cryptographic hash function**: SHA-256 produces 256-bit output; usable as hash via h(k) = SHA-256(k) mod m
- **Wee hash function**: fₐ(k) = swap((2k² + ak) mod 2ʷ); then iterate r rounds with CBC-style chaining for variable-length inputs

#### Processes / Algorithms / Pathways
##### DIRECT-ADDRESS-SEARCH(T, k)
- **Steps**: return T[k]
- **Complexity**: O(1)

##### CHAINED-HASH-INSERT(T, x)
- **Steps**: LIST-PREPEND(T[h(x.key)], x)
- **Complexity**: O(1) worst-case
- **Example**: T size 9, h(k)=k mod 9. Insert keys 5,28,19,15,20,33,12,17,10. h(5)=5, h(28)=1, h(19)=1 (collision → chain at slot 1: 19→28), h(15)=6, h(20)=2, h(33)=6 (chain: 33→15), h(12)=3, h(17)=8, h(10)=1 (chain: 10→19→28)

##### CHAINED-HASH-SEARCH(T, k)
- **Steps**: return LIST-SEARCH(T[h(k)], k)
- **Complexity**: Θ(1+α) average under independent uniform hashing; Θ(n) worst-case

##### CHAINED-HASH-DELETE(T, x)
- **Steps**: LIST-DELETE(T[h(x.key)], x)
- **Complexity**: O(1) if doubly linked list

##### HASH-INSERT(T, k) — open addressing
- **Steps**: (1) i=0 (2) repeat: q = h(k,i); if T[q] == NIL: T[q]=k, return q; else i=i+1 (3) until i==m (4) error "hash table overflow"
- **Complexity**: Expected O(1/(1−α)) probes under independent uniform permutation hashing

##### HASH-SEARCH(T, k) — open addressing
- **Steps**: (1) i=0 (2) repeat: q = h(k,i); if T[q]==k return q; i=i+1 (3) until T[q]==NIL or i==m (4) return NIL

##### LINEAR-PROBING-HASH-DELETE(T, q)
- **Steps**: (1) T[q]=NIL (2) search forward; for each key k' found, compute g(k',q) = (q − h₁(k')) mod m; if g(k',q) < g(k',q'), move k' to vacated slot; continue until empty slot found
- **Complexity**: proportional to distance from h₁(k) to next empty slot

#### Classifications & Hierarchies
- **Hash function families by strength**:
  - Uniform: Pr[h(k)=q] = 1/m for any key k
  - Universal: Pr[h(k₁)=h(k₂)] ≤ 1/m for distinct keys
  - ϵ-universal: collision prob ≤ ϵ
  - d-independent: d-wise joint distribution uniform
- **Collision resolution**:
  - Chaining (uses external lists)
  - Open addressing (all in table): linear probing, double hashing
- **Hash function construction**:
  - Static: division; multiplication; multiply-shift (fixed h)
  - Random: universal family Hₚₘ = {hₐb(k) = ((ak+b) mod p) mod m}; multiply-shift with random odd a
  - Cryptographic: SHA-256 + salt; wee hash (RC6-based)

#### Comparisons & Trade-offs
| Dimension | Chaining | Open Addressing |
|---|---|---|
| Load factor α | Can exceed 1 | ≤ 1 |
| Storage | table + pointers | table only (no pointers) |
| Deletion | Trivial (O(1) doubly linked) | Tricky; needs DELETED marker or linear-probing delete |
| Search avg (α=.5) | Θ(1+α) ≈ 1.5 probes | 1/(1−α) ≈ 2 probes (unsuccessful) |
| Cache behavior | Poor (list traversal) | Better (linear probing sequential) |
| Worst-case | Θ(n) (all same slot) | Θ(n) (table full, must probe all) |

| Dimension | Linear Probing | Double Hashing |
|---|---|---|
| Probe sequences | m distinct | Θ(m²) distinct |
| Primary clustering | Yes | No |
| Cache locality | Excellent | Poor |
| Deletion w/o DELETED | Yes (L-P delete) | No |

| Dimension | Division Method | Multiply-Shift | Universal Family Hₚₘ |
|---|---|---|---|
| Speed | Very fast | 3 instructions | Moderate (needs mod p) |
| m constraint | Prime preferred, not near 2ᵏ | Power of 2 (m=2ℓ) | Arbitrary |
| Guarantee | None (static) | None (static) | Universal (≤1/m collision) |

#### Formulas & Equations
##### Load factor
`α = n / m`
- n = number of elements
- m = number of slots
- For open addressing: α < 1 strictly (at least one empty slot)

##### Expected unsuccessful search — chaining
`Θ(1 + α)`
- Theorem 11.1: under independent uniform hashing

##### Expected successful search — chaining
`Θ(1 + α)`
- Theorem 11.2: under independent uniform hashing

##### Expected probes unsuccessful search — open addressing
`≤ 1 / (1 − α)`
- Theorem 11.6: under independent uniform permutation hashing, α < 1, no deletions

##### Expected probes successful search — open addressing
`≤ (1/α) ln(1/(1−α))`
- Theorem 11.8: under independent uniform permutation hashing

##### Universal hash family Hₚₘ
`hₐb(k) = ((ak + b) mod p) mod m`
- a ∈ {1,…,p−1}, b ∈ {0,…,p−1}
- p prime, p > m
- |Hₚₘ| = p(p−1)

##### Multiply-shift hash
`hₐ(k) = (ka mod 2ʷ) ⋙ (w−ℓ)`
- m = 2ℓ, w-bit words
- a = odd w-bit constant
- 2/m-universal (Theorem 11.5)

##### Double hashing
`h(k,i) = (h₁(k) + i·h₂(k)) mod m`
- h₂(k) must be relatively prime to m
- Common: m prime, h₂(k) = 1 + (k mod m′), m′ slightly < m

##### Linear probing hash
`h(k,i) = (h₁(k) + i) mod m`

#### Edge Cases & Common Pitfalls
- **Worst-case chaining**: all keys hash to same slot → Θ(n) per operation
- **m power of 2 with division**: h(k) = k mod 2ℓ uses only low-order ℓ bits — bad if keys are patterned
- **m near power of 2 with division**: bad distribution
- **Open addressing deletion**: setting slot to NIL breaks search; use DELETED marker instead (but then α no longer bounds search time)
- **Double hashing non-relatively-prime**: if gcd(h₂(k), m) = d > 1, only 1/d of table probed
- **Linear probing primary clustering**: empty slot preceded by i full slots filled with probability (i+1)/m
- **α → 1 in open addressing**: probes → ∞; unsuccessful search at α=1 probes all m slots
- **Static hash function**: adversary can choose n keys all same slot

#### Diagrams & Visuals
```
Direct-address table:
  Keys U={0,...,9}  K={2,3,5,8}
  T: [NIL][NIL][●→e₂][●→e₃][NIL][●→e₅][NIL][NIL][●→e₈][NIL]
       0     1    2     3    4    5    6    7    8    9

Chaining:
  T: [NIL]→[●→k₁→k₄]→[●→k₂→k₅→k₇]→[NIL]→...
       0        1             2           3

Open addressing — double hashing:
  h₁(k)=k mod 13, h₂(k)=1+(k mod 11)
  Key 14: h₁(14)=1 (occupied) → probe 1+5=6 (occupied) → probe 6+5=11 (occupied) → probe 11+5=16 mod 13 = 3 (occupied) → probe 3+5=8 (occupied) → probe 8+5=13 mod 13=0 (occupied) → probe 0+5=5 (occupied) → probe 5+5=10 (occupied) → probe 10+5=15 mod 13=2 (occupied) → probe 2+5=7 (occupied) → probe 7+5=12 (occupied) → probe 12+5=17 mod 13=4 (occupied) → probe 4+5=9 (empty!) insert at 9
  (modified from text: 14 inserted at slot 9 after probing slots 1,5)

Multiply-shift:
  k (w bits) → × a (w bits) → [r₁ (high w) | r₀ (low w)] → take ℓ MSB of r₀
```

#### End-of-Chapter Material
- **Key terms**: direct-address table, hash table, hash function, collision, chaining, load factor, independent uniform hashing, universal hashing, ϵ-universal, d-independent, division method, multiplication method, multiply-shift, open addressing, probe sequence, double hashing, linear probing, primary clustering, cryptographic hash, wee hash, random oracle
- **Theorem 11.1–11.2**: chaining search Θ(1+α) average
- **Theorem 11.4**: Hₚₘ is universal
- **Theorem 11.5**: multiply-shift is 2/m-universal
- **Theorem 11.6**: open addressing unsuccessful search ≤ 1/(1−α)
- **Theorem 11.8**: open addressing successful search ≤ (1/α) ln(1/(1−α))
- **Theorem 11.9**: linear probing with 5-independent h₁ and α ≤ 2/3 takes expected constant time
- **Problem 11-3**: max chain length E[M] = O(lg n / lg lg n) for n keys, n slots

#### Cross-Chapter Links
- **Requires**: Ch. 10 (linked lists for chaining), Ch. 5 (indicator random variables, expectation), Ch. 31 (modular arithmetic for universal hashing)
- **Referenced in**: Ch. 17 (amortized analysis of hash tables), Ch. 22 (graph representations)

---

### Ch. 12 — Binary Search Trees

#### Named Entities (Terms & Definitions)
- **Binary search tree (BST)**: binary tree with BST property: for any node x, all keys in left subtree ≤ x.key ≤ all keys in right subtree
- **BST property**: if y in left subtree of x then y.key ≤ x.key; if y in right subtree then y.key ≥ x.key
- **Inorder tree walk**: recursively visit left, print root, visit right; prints keys in sorted order in Θ(n) time
- **Preorder tree walk**: print root, visit left, visit right
- **Postorder tree walk**: visit left, visit right, print root
- **Successor**: next node visited in inorder walk; if right subtree exists → minimum of right subtree; else lowest ancestor whose left child is also ancestor
- **Predecessor**: symmetric to successor; last node visited before x in inorder walk
- **Radix tree (trie)**: tree on bit strings; go left if bit=0, right if bit=1; sorts strings in Θ(total length) time
- **Randomly built BST**: insert n keys in random order (all n! permutations equally likely); expected height O(lg n)
- **Catalan number**: bₙ = (1/(n+1))C(2n,n); number of distinct binary trees with n nodes

#### Processes / Algorithms / Pathways
##### INORDER-TREE-WALK(x)
- **Type**: Algorithm
- **Goal**: Print keys of BST in sorted order
- **Steps**: (1) if x ≠ NIL: (2) INORDER-TREE-WALK(x.left) (3) print x.key (4) INORDER-TREE-WALK(x.right)
- **Complexity**: Θ(n) (Theorem 12.1)
- **Example**: Tree root=6, left child=5 (with left=2, right=5), right child=7 (with right=8). Output: 2,5,5,6,7,8

##### TREE-SEARCH(x, k)
- **Type**: Algorithm
- **Goal**: Find node with key k in subtree rooted at x
- **Steps**: (1) if x == NIL or k == x.key: return x (2) if k < x.key: return TREE-SEARCH(x.left, k) (3) else: return TREE-SEARCH(x.right, k)
- **Complexity**: O(h) where h = tree height
- **Example**: Search key 13 in tree [15,6,7,13, ...]: path 15 → 6 → 7 → 13; returns node with key 13

##### ITERATIVE-TREE-SEARCH(x, k)
- **Type**: Algorithm
- **Steps**: (1) while x ≠ NIL and k ≠ x.key: (2) if k < x.key: x = x.left (3) else: x = x.right (4) return x
- **Complexity**: Same, more efficient in practice

##### TREE-MINIMUM(x)
- **Type**: Algorithm
- **Goal**: Find minimum key in subtree
- **Steps**: (1) while x.left ≠ NIL: x = x.left (2) return x
- **Complexity**: O(h)
- **Example**: From root 15: 15→6→3→2 → returns 2

##### TREE-MAXIMUM(x)
- **Type**: Algorithm
- **Goal**: Find maximum key in subtree
- **Steps**: (1) while x.right ≠ NIL: x = x.right (2) return x
- **Complexity**: O(h)

##### TREE-SUCCESSOR(x)
- **Type**: Algorithm
- **Goal**: Find next node in inorder traversal
- **Steps**: (1) if x.right ≠ NIL: return TREE-MINIMUM(x.right) (2) y = x.p (3) while y ≠ NIL and x == y.right: x = y; y = y.p (4) return y
- **Complexity**: O(h)
- **Example**: Node with key 13 (no right child): go up to parent 7 (13 is right child of 7); go up to parent 6 (7 is right child of 6); go up to 15 (6 is left child of 15) → successor is 15

##### TREE-INSERT(T, z)
- **Type**: Algorithm
- **Goal**: Insert node z into BST T (z.key set, children NIL)
- **Steps**: (1) x = T.root; y = NIL (2) while x ≠ NIL: y = x; if z.key < x.key: x = x.left else x = x.right (3) z.p = y (4) if y == NIL: T.root = z (5) elseif z.key < y.key: y.left = z (6) else: y.right = z
- **Complexity**: O(h)
- **Example**: Insert key 13 into tree with root 15, left=6, right=20. Path: 15→6→7→NIL (right of 7). Insert as right child of 7.

##### TRANSPLANT(T, u, v)
- **Type**: Subroutine
- **Goal**: Replace subtree rooted at u with subtree rooted at v
- **Steps**: (1) if u.p == NIL: T.root = v (2) elseif u == u.p.left: u.p.left = v (3) else: u.p.right = v (4) if v ≠ NIL: v.p = u.p

##### TREE-DELETE(T, z)
- **Type**: Algorithm
- **Goal**: Delete node z from BST T
- **Steps**: Cases: (a) z no left child → TRANSPLANT(z, z.right) (b) z no right child → TRANSPLANT(z, z.left) (c) z has two children: y = TREE-MINIMUM(z.right); if y ≠ z.right: TRANSPLANT(y, y.right); y.right = z.right; TRANSPLANT(z, y); y.left = z.left
- **Complexity**: O(h)
- **Example**: Delete root 15 (has children 6 and 20). y = TREE-MINIMUM(z.right) = 17. If 17 is not right child of 15: splice 17 out, make 17's right child (say 19) replace 17, set 17.right = 20, TRANSPLANT(15,17), set 17.left = 6.

#### Classifications & Hierarchies
- **BST variants**:
  - Basic BST (Ch. 12): O(h) operations, h could be n
  - Red-black tree (Ch. 13): h ≤ 2 lg(n+1)
  - AVL tree (Problem 13-3): |left.h − right.h| ≤ 1
  - Radix tree / trie (Problem 12-2): bit-based keys
  - Optimal BST (Ch. 14): known search frequencies
- **Tree walks**: inorder (sorted), preorder (root first), postorder (root last)

#### Comparisons & Trade-offs
| Dimension | Unsorted Array | Sorted Array | BST (height h) | Red-Black Tree |
|---|---|---|---|---|
| SEARCH | Θ(n) | O(log n) | O(h) | O(log n) |
| INSERT | O(1) | Θ(n) (shift) | O(h) | O(log n) |
| DELETE | Θ(n) (search+shift) | Θ(n) | O(h) | O(log n) |
| MIN/MAX | Θ(n) | O(1) | O(h) | O(log n) |
| SUCCESSOR | N/A | O(1) if index given | O(h) | O(log n) |
| Sorted output | Θ(n log n) sort | Θ(n) walk | Θ(n) inorder | Θ(n) inorder |

#### Formulas & Equations
##### BST height bound (random)
`E[height] = O(log n)`
- Random BST from random insertion order

##### Number of distinct binary trees (Catalan)
`bₙ = (1/(n+1)) · C(2n, n) = Ω(4ⁿ / n^(3/2))`
- b₀ = 1; recurrence: bₙ = Σ_{k=0}^{n-1} bₖ·b_{n-1-k}

#### Rules, Laws & Theorems
##### Theorem 12.1
- **Statement**: INORDER-TREE-WALK on n-node subtree takes Θ(n) time
- **Proof**: T(n) ≤ T(k) + T(n−k−1) + d; by substitution T(n) ≤ (c+d)n + c

##### Theorem 12.2
- **Statement**: SEARCH, MINIMUM, MAXIMUM, SUCCESSOR, PREDECESSOR each run in O(h) on BST of height h

##### Theorem 12.3
- **Statement**: INSERT and DELETE run in O(h) on BST of height h

#### Edge Cases & Common Pitfalls
- **Degenerate BST**: inserting sorted keys yields h = n (linked list); operations Θ(n)
- **Equal keys**: need convention about ≤ vs < in BST property; Problem 12-1 explores strategies
- **Deleting node with two children**: successor y may be z's immediate right child (case c) or deeper (case d); two distinct subcases
- **STACK-EMPTY check not needed**: TREE-INSERT accesses NIL child attributes, must stop at NIL
- **TRANSPLANT does not update children of v**: caller's responsibility (TREE-DELETE handles this)
- **Successor when right subtree empty**: must go up tree until finding a node that is a left child

#### Diagrams & Visuals
```
Binary search tree (h=2):
        6
       / \
      5   7
     / \   \
    2   5   8

Inorder: 2,5,5,6,7,8

Search path for k=13:
    15 → 6 → 7 → 13
    (go left at 15, right at 6, right at 7, found)

Successor of node 13 (no right child):
    13 → parent 7 (13 is right child) → parent 6 (7 is right child) → parent 15 (6 is left child) → successor = 15

Delete cases (z=blue, replacement=orange):
  (a) z no left child: z.right replaces z
  (b) z no right child: z.left replaces z
  (c) z two children, y=successor is z.right: y replaces z
  (d) z two children, y deeper: splice y out first, then y replaces z

Radix tree (trie) for strings {0,011,10,100,1011}:
        root
       /    \
      0      1
      |     / \
      0    0   0
      |    |   |
      1    0   1
          /    |
         0     1
              /
             1
```

#### End-of-Chapter Material
- **Key terms**: binary search tree, BST property, inorder/preorder/postorder tree walk, successor, predecessor, TRANSPLANT, radix tree (trie), Catalan number, randomly built BST
- **Exercises 12.1**: draw BSTs of various heights; compare BST property to min-heap property; nonrecursive inorder walk
- **Exercises 12.2**: search path validity; recursive MIN/MAX; successor has no left child; Θ(n) inorder via MINIMUM + n−1 SUCCESSOR calls
- **Exercises 12.3**: BST sort (worst Θ(n²), best Θ(n log n)); deletion not commutative; successor-only representation
- **Problem 12-3**: average node depth in randomly built BST is O(log n); links to quicksort
- **Problem 12-4**: Catalan numbers count distinct binary trees

#### Cross-Chapter Links
- **Requires**: Ch. 10 (binary tree representation, linked lists), Appendix B (tree math)
- **Referenced in**: Ch. 13 (red-black trees), Ch. 14 (optimal BST), Ch. 18 (B-trees), Ch. 19 (Fibonacci heaps)

---

### Ch. 13 — Red-Black Trees

#### Named Entities (Terms & Definitions)
- **Red-black tree**: BST with 1 extra bit per node (color: RED or BLACK); approximately balanced; height ≤ 2 lg(n+1)
- **Red-black properties**: (1) every node red or black (2) root is black (3) every leaf (NIL) is black (4) red node → both children black (5) all paths from node to descendant leaves have same #black nodes
- **Black-height bh(x)**: number of black nodes on path from x (excluding x) down to a leaf
- **Sentinel T.nil**: single object representing all NIL leaves; color BLACK
- **Rotation**: local pointer rearrangement preserving BST property; left rotation and right rotation; O(1) time
- **Left rotation**: x.right = y becomes new root of subtree; x becomes y's left child; y's left child becomes x's right child
- **Right rotation**: symmetric
- **Uncle**: sibling of a node's parent
- **Doubly black / red-and-black**: conceptual extra black on node x after deletion of black y; x is doubly black if x.color = BLACK, red-and-black if x.color = RED
- **AVL tree**: height-balanced BST; |left.h − right.h| ≤ 1 for all nodes; height O(log n)
- **Persistent data structure**: maintains past versions; copying only affected path nodes (O(log n) per op)
- **Join operation (RB-JOIN)**: merge two red-black trees S₁, S₂ and element x where all keys in S₁ ≤ x.key ≤ all keys in S₂; O(log n)

#### Processes / Algorithms / Pathways
##### LEFT-ROTATE(T, x)
- **Type**: Algorithm
- **Goal**: Perform left rotation on node x (x.right ≠ T.nil)
- **Steps**: (1) y = x.right (2) x.right = y.left (3) if y.left ≠ T.nil: y.left.p = x (4) y.p = x.p (5) if x.p == T.nil: T.root = y (6) elseif x == x.p.left: x.p.left = y (7) else: x.p.right = y (8) y.left = x (9) x.p = y
- **Complexity**: O(1)
- **Example**: Left rotation on x with right child y: before: x→(α, y→(β,γ)); after: y→(x→(α,β), γ). BST order α < x < β < y < γ preserved.

##### RIGHT-ROTATE(T, y)
- **Type**: Algorithm (symmetric to LEFT-ROTATE)
- **Complexity**: O(1)

##### RB-INSERT(T, z)
- **Type**: Algorithm
- **Goal**: Insert node z into red-black tree T maintaining red-black properties
- **Steps**: (1) Same as TREE-INSERT but with T.nil sentinel (2) set z.left = z.right = T.nil (3) z.color = RED (4) call RB-INSERT-FIXUP(T, z)
- **Complexity**: O(log n); at most 2 rotations
- **Example**: Insert 38 into empty tree → root=38, black. Insert 31: root=38(black), left=31(red). Insert 12: 38(black)→31(red)→12(red) → violation (two reds). Uncle=NIL(black). Case 2/3: rotate right on 31, recolor → 31(black), left=12(red), right=38(red).

##### RB-INSERT-FIXUP(T, z)
- **Type**: Algorithm
- **Goal**: Restore red-black properties after insertion
- **Invariant**: (a) z is red (b) if z.p is root, z.p is black (c) at most one violation (property 2 or 4, not both)
- **Cases** (z.p is left child of z.p.p):
  - **Case 1** (uncle y red): recolor: z.p=BLACK, y=BLACK, z.p.p=RED; z moves up two levels
  - **Case 2** (uncle black, z is right child): left rotation on z.p; falls through to Case 3
  - **Case 3** (uncle black, z is left child): recolor z.p=BLACK, z.p.p=RED; right rotation on z.p.p
- **Termination**: when z.p is black; line 30 colors root black
- **Complexity**: O(log n); ≤ 2 rotations

##### RB-TRANSPLANT(T, u, v)
- **Type**: Subroutine
- **Steps**: (1) if u.p == T.nil: T.root = v (2) elseif u == u.p.left: u.p.left = v (3) else: u.p.right = v (4) v.p = u.p (unconditional)
- **Difference from TRANSPLANT**: uses T.nil, unconditional v.p assignment

##### RB-DELETE(T, z)
- **Type**: Algorithm
- **Goal**: Delete node z from red-black tree
- **Steps**: (1) y = z; y-original-color = y.color (2) if z has ≤1 child: set x = child, RB-TRANSPLANT(z, child) (3) else: y = TREE-MINIMUM(z.right); y-original-color = y.color; x = y.right; splice y out if not z.right; RB-TRANSPLANT(z, y); y.color = z.color (4) if y-original-color == BLACK: call RB-DELETE-FIXUP(T, x)
- **Complexity**: O(log n); at most 3 rotations

##### RB-DELETE-FIXUP(T, x)
- **Type**: Algorithm
- **Goal**: Fix red-black properties after deletion of a black node
- **Idea**: x is "doubly black"; push extra black up tree
- **Cases** (x is left child):
  - **Case 1** (sibling w red): w=BLACK, x.p=RED, left-rotate on x.p; new w = x.p.right (black); falls into 2/3/4
  - **Case 2** (w black, both w's children black): remove one black from x and w (w=RED); move extra black up to x.p; x = x.p
  - **Case 3** (w black, w.left red, w.right black): w.left=BLACK, w=RED, right-rotate on w; new w = x.p.right (black with red right child); falls into Case 4
  - **Case 4** (w black, w.right red): w.color = x.p.color; x.p=BLACK; w.right=BLACK; left-rotate on x.p; x = T.root (terminates)
- **Termination**: x = root (extra black vanishes) or x red-and-black (color x black); line 44 colors x black
- **Complexity**: O(log n); only Case 2 repeats; at most 3 rotations

#### Classifications & Hierarchies
- **Balanced BSTs**: red-black (Ch. 13), AVL (Problem 13-3), AA-trees, treaps, splay trees, scapegoat trees, weight-balanced trees
- **Red-black variants**: left-leaning red-black trees (Sedgewick); all red nodes are left children

#### Comparisons & Trade-offs
| Dimension | Red-Black Tree | AVL Tree |
|---|---|---|
| Height bound | ≤ 2 lg(n+1) | ≤ 1.44 lg n (stricter) |
| Insert rotations | ≤ 2 | O(log n) |
| Delete rotations | ≤ 3 | O(log n) |
| Lookup speed | O(log n) | Slightly faster (tighter balance) |
| Implementation | More complex | Simpler (no color; just height) |

| Dimension | BST (Ch. 12) | Red-Black Tree |
|---|---|---|
| Worst-case height | Θ(n) (degenerate) | O(log n) |
| SEARCH, INSERT, DELETE | O(h) | O(log n) |
| Space | n nodes + 3 pointers | n nodes + 3 ptrs + 1 color bit |
| Sentinel | Optional | Required (T.nil) |

#### Formulas & Equations
##### Height bound
`h ≤ 2 lg(n + 1)`
- Lemma 13.1: red-black tree with n internal nodes has height at most 2 lg(n+1)
- Proof: (1) subtree at x contains ≥ 2^bh(x) − 1 internal nodes (induction) (2) root black-height ≥ h/2 (by property 4, ≥ half nodes on path are black) (3) n ≥ 2^(h/2) − 1 → h ≤ 2 lg(n+1)

##### Black-height bounds
`⌈h/2⌉ ≤ bh(root) ≤ h`
- min black-height = ⌈h/2⌉ (alternating red-black from root)
- max black-height = h (all nodes black)

#### Rules, Laws & Theorems
##### Lemma 13.1
- Red-black tree with n internal nodes has height ≤ 2 lg(n+1)
- Implies O(log n) for all BST operations

##### Property 4 consequence
- A red node cannot have exactly one non-NIL child (Exercise 13.1-8)
- Proof: if red node had one child, that child's black-height would differ from NIL leaf's black-height

#### Edge Cases & Common Pitfalls
- **Inserting black instead of red**: would violate property 5 (extra black on paths through new node)
- **Deleting red node**: no problem — properties preserved
- **Deleting black root with red child**: new root (x) is red — property 2 violated; fix by coloring root black (line 44)
- **T.nil sentinel**: must never be colored RED; RB-INSERT-FIXUP never sets T.nil.color = RED (Exercise 13.3-4)
- **Case 2 entering from Case 1**: new x (x.p) will be red-and-black → loop terminates next iteration
- **Doubly black**: not a real color attribute; conceptual; x.color attribute stays RED or BLACK
- **x.p must be set in RB-DELETE** even when x = T.nil (line 16), needed by RB-DELETE-FIXUP
- **RB-INSERT vs TREE-INSERT**: uses T.nil instead of NIL; sets children to T.nil; colors RED; calls FIXUP

#### Diagrams & Visuals
```
Red-black tree structure:
     (7) BLACK
     /        \
  (3)RED    (18)RED
   /  \      /    \
(2)B (4)B (11)B (22)B — NIL leaves not shown

Black-heights: nil=0, 2=bh1, 4=bh1, 3=bh1, 11=bh1, 22=bh1, 18=bh1, 7=bh2

Left rotation:
  BEFORE:        AFTER:
     x              y
    / \            / \
   α   y    →     x   γ
      / \        / \
     β   γ      α   β

  BST order preserved: α < x < β < y < γ

RB-INSERT-FIXUP cases:
  Case 1: z.p and uncle both red → recolor, move z up 2
  Case 2: z.p red, uncle black, z right child → left rotate → Case 3
  Case 3: z.p red, uncle black, z left child → recolor + right rotate → done

RB-DELETE-FIXUP cases (x is left child):
  Case 1: w red → recolor + left rotate → Case 2/3/4
  Case 2: w black, both children black → push black up
  Case 3: w black, w.left red, w.right black → right rotate → Case 4
  Case 4: w black, w.right red → recolor + left rotate → done
```

#### End-of-Chapter Material
- **Key terms**: red-black tree, red-black properties, black-height, sentinel T.nil, rotation (left/right), RB-INSERT, RB-INSERT-FIXUP, RB-DELETE, RB-DELETE-FIXUP, doubly black, red-and-black, uncle, AVL tree, persistent set, join
- **Lemma 13.1**: h ≤ 2 lg(n+1)
- **Exercises 13.1**: draw RB tree; red node cannot have exactly one child; largest/smallest internal nodes for given black-height
- **Exercises 13.2**: any BST can be transformed to any other using O(n) rotations; right-conversion O(n²); exactly n−1 possible rotations in n-node BST
- **Exercises 13.3**: tracing insertions 41,38,31,12,19,8 into empty RB tree; black-height labeling
- **Exercises 13.4**: tracing deletions from previous tree; sentinel interactions
- **Problem 13-1**: persistent BST — copy O(h) nodes per insert; parent pointers make it Ω(n)
- **Problem 13-2**: RB-JOIN — O(log n) by grafting at nodes of matching black-height
- **Problem 13-3**: AVL trees — height O(log n), at least F_h nodes; BALANCE procedure using rotations; AVL-INSERT O(log n) with O(log n) rotations

#### Cross-Chapter Links
- **Requires**: Ch. 12 (BST operations, TREE-INSERT, TREE-DELETE), Ch. 10 (binary tree representation, sentinel)
- **Referenced in**: Ch. 14 (optimal BST), Ch. 17 (amortized analysis — constant rotations per op matters), Ch. 18 (B-trees), Ch. 19 (mergeable heaps)

---

## Cross-Cutting Topics

### Design Paradigms & Meta-Methods
- **Divide-and-conquer in hashing**: chaining divides n elements into m random subsets (Ch. 11)
- **Randomization for average-case**: universal hashing (Ch. 11), randomly built BSTs (Ch. 12), randomized skip-ahead search (Problem 10-3)
- **Balancing via local transformations**: rotations in red-black trees (Ch. 13); preserves BST property while rebalancing in O(1)
- **Sentinel pattern**: dummy node to eliminate boundary checks — used in linked lists (Ch. 10), red-black trees (Ch. 13)

### Proof & Argument Patterns
- **Indicator random variables**: analysis of chaining (Theorem 11.2), Pr{collision} = 1/m²
- **Induction on tree height**: Lemma 13.1 (subtree size ≥ 2^bh(x) − 1)
- **Substitution method**: Theorem 12.1 (inorder walk takes Θ(n))
- **Loop invariant**: RB-INSERT-FIXUP three-part invariant (z red; if root then black; at most one violation of prop 2 or 4)
- **Amortization intuition**: RB-INSERT-FIXUP case 1 moves z up; O(log n) total; only case 2 repeats in RB-DELETE-FIXUP

### Mnemonics & Memory Aids
- **ROYGBIV for RB properties**: (1) Red-or-black every node (2) Only root is black (3) Yellow/NIL is black → skip (4) Green/Go: red's children black (5) Black numbers same on every path
- **Left rotation = "lift the right child"**: x.right (y) becomes new parent; x drops to left; y's left becomes x's right
- **Chaining α = "average chain length"**: α = n/m; search Θ(1+α)
- **Open addressing probes**: unsuccessful = 1/(1−α) (geometric series!)
- **BST delete 3 cases**: 0 children (leaf) → snip; 1 child → replace; 2 children → find successor, splice, replace
- **RB-INSERT-FIXUP cases**: Uncle red → just recolor (case 1); uncle black, zig-zag → rotate once (case 2); uncle black, zig-zig → rotate + recolor (case 3)

### People & Dates
- **A. M. Turing** (1947): stacks for subroutine linkage
- **G. M. Hopper** (1951): algebraic formulas as binary trees in A-1 language
- **A. Newell, J. C. Shaw, H. A. Simon** (1956–57): IPL-II/IPL-III — pointers and stack operations
- **H. P. Luhn** (1953): invented hash tables and chaining
- **G. M. Amdahl**: originated open addressing
- **Carter & Wegman** (1979): universal families of hash functions
- **Dietzfelbinger et al.**: multiply-shift hash; Theorem 11.5 proof
- **Thorup**: 5-independent hashing for linear probing (Theorem 11.9)
- **Adel'son-Vel'skiĭ & Landis** (1962): AVL trees
- **Bayer** (1972): red-black trees ("symmetric binary B-trees")
- **Guibas & Sedgewick**: red/black color convention
- **Sleator & Tarjan**: splay trees (self-adjusting)
