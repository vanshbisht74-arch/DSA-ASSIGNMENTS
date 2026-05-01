# 📘 Data Structures Lab README (Experiments 1–28)

---

## ---- EXPERIMENT 1 — Stack ADT ----
Q1. What is an Abstract Data Type (ADT)?
An Abstract Data Type (ADT) defines operations and behavior without implementation details.

Q2. Why push/pop are O(1)?
They operate only on the top element.

Q3. Real-world use?
Function call stack.

---

## ---- EXPERIMENT 2 — Complexity Analysis ----
Q1. Big-O vs Big-Theta?
Big-O → worst case
Big-Theta → exact bound

Q2. Worst-case complexity?
Maximum operations for input size n.

Q3. Importance?
Efficient and scalable programs.

---

## ---- EXPERIMENT 3 — Recursive Factorial ----
Q1. Recursion depth?
Maximum active calls.

Q2. Why uses stack?
Stores function calls.

Q3. Iteration preferred?
When memory is limited.

---

## ---- EXPERIMENT 4 — Fibonacci ----
Q1. Why naive slow?
Repeats calculations.

Q2. Memoization relation?
Top-down DP.

Q3. Space impact?
O(n)

---

## ---- EXPERIMENT 5 — Tower of Hanoi ----
Q1. Moves formula?
2^n - 1

Q2. Recursion tree?
Visual representation of recursive calls.

Q3. Risk?
Exponential time.

---

## ---- EXPERIMENT 6 — Binary Search ----
Q1. Why sorted?
To eliminate half.

Q2. Complexity?
O(log n)

Q3. Divide & conquer?
Divide → solve → combine.

---

## ---- EXPERIMENT 7 — Arrays 1D ----
Q1. Index access O(1)?
Direct address calculation.

Q2. Insert at start O(n)?
Shifting required.

Q3. Static vs dynamic?
Static = fixed size
Dynamic = resizable

---

## ---- EXPERIMENT 8 — Arrays 2D ----
Q1. Scan complexity?
O(n × m)

Q2. Use?
Images, spreadsheets.

Q3. Memory layout?
Row-major order.

---

## ---- EXPERIMENT 9 — Dynamic Array ----
Q1. Amortized cost?
Average over operations.

Q2. Why doubling?
Reduces resizing.

Q3. Pop complexity?
O(1)

---

## ---- EXPERIMENT 10 — Singly Linked List ----
Q1. Search O(n)?
Sequential traversal.

Q2. Insert at head O(1)?
No traversal needed.

Q3. Node structure?
Data + next pointer.

---

## ---- EXPERIMENT 11 — Doubly Linked List ----
Q1. Advantage?
Bidirectional traversal.

Q2. Use?
Browser history.

Q3. Deletion ease?
Access to previous node.

---

## ---- EXPERIMENT 12 — Parentheses Checker ----
Q1. Why stack?
LIFO structure for matching.

Q2. Why "([)]" fails?
Incorrect order.

Q3. Underflow?
Pop from empty stack.

---

## ---- EXPERIMENT 13 — Queue ----
Q1. Why BFS uses queue?
Processes level by level.

Q2. FIFO?
First In First Out.

Q3. Use?
CPU scheduling, printer queue.

---

## ---- EXPERIMENT 14 — O(n²) Sort ----
Q1. O(n²)?
Quadratic growth.

Q2. Why slow?
Too many comparisons.

Q3. Stable?
Maintains order of equal elements.

---

## ---- EXPERIMENT 15 — Insertion Sort ----
Q1. Best case?
Nearly sorted array.

Q2. Worst case?
Reverse sorted.

Q3. Space?
O(1)

---

## ---- EXPERIMENT 16 — Merge Sort ----
Q1. Time?
O(n log n)

Q2. Stable?
Yes

Q3. Space?
O(n)

---

## ---- EXPERIMENT 17 — Quick Sort ----
Q1. Worst case?
O(n²)

Q2. Average?
O(n log n)

Q3. Stable?
No

---

## ---- EXPERIMENT 18 — Heap Sort ----
Q1. Stable?
No

Q2. Time?
O(n log n)

Q3. Use?
Priority queue.

---

## ---- EXPERIMENT 19 — Benchmarking ----
Q1. Why compare algorithms?
To evaluate performance.

Q2. Why copy input?
Fair comparison.

Q3. Worst case insertion?
Reverse array.

---

## ---- EXPERIMENT 20 — BST ----
Q1. Inorder sorted?
Yes

Q2. Worst case?
O(n)

Q3. Avg?
O(log n)

---

## ---- EXPERIMENT 21 — BST Delete ----
Q1. Successor?
Minimum in right subtree.

Q2. Why tricky?
Three cases.

Q3. Verify?
Inorder traversal sorted.

---

## ---- EXPERIMENT 22 — Heap ----
Q1. Why heap?
Efficient insert/delete.

Q2. Complexity?
O(log n)

Q3. Use?
Scheduling.

---

## ---- EXPERIMENT 23 — Graph ----
Q1. Adjacency list?
Space efficient.

Q2. Directed?
One-way edges.

Q3. Weighted?
Stores cost.

---

## ---- EXPERIMENT 24 — BFS ----
Q1. Why queue?
Level traversal.

Q2. Shortest path?
Yes (unweighted graph).

Q3. Complexity?
O(V + E)

---

## ---- EXPERIMENT 25 — DFS ----
Q1. DFS vs BFS?
Depth vs level.

Q2. Issue?
Stack overflow.

Q3. Use?
Path finding.

---

## ---- EXPERIMENT 26 — Hash Table ----
Q1. Collision?
Same index.

Q2. Chaining?
List in bucket.

Q3. Load factor?
n / size.

---

## ---- EXPERIMENT 27 — Trie ----
Q1. Use?
Prefix search.

Q2. Space?
More memory.

Q3. Advantage?
Fast lookup.

---

## ---- EXPERIMENT 28 — Bloom Filter ----
Q1. False negatives?
No

Q2. False positives?
Yes

Q3. Use?
Databases, caching.

---
