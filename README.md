# 📘 Data Structures Lab README (Experiments 1–13)

---

## ---- EXPERIMENT 1 — Stack ADT ----

**Q1. What is an Abstract Data Type (ADT)?**  
An Abstract Data Type (ADT) is a logical description of a data structure that defines operations and their behavior without specifying implementation. It focuses on what operations do, not how they are done.  
Example: Stack ADT defines push, pop, and peek.

**Q2. Why are push and pop operations O(1)?**  
Push and pop operate only on the top element and do not require traversal or shifting. Hence they take constant time → O(1).

**Q3. Give one real-world use of stack.**  
Function call management (call stack) in programming languages.

---

## ---- EXPERIMENT 2 — Complexity Analysis ----

**Q1. Difference between Big-O and Big-Theta?**  
Big-O → upper bound (worst case)  
Big-Theta → exact bound (tight bound)

**Q2. What is worst-case complexity?**  
Maximum number of operations for input size n.

**Q3. Why is complexity important?**  
- Choose efficient algorithms  
- Predict performance  
- Build scalable systems  

---

## ---- EXPERIMENT 3 — Recursive Factorial ----

**Q1. What is recursion depth?**  
Maximum number of recursive calls in stack at once.

**Q2. Why recursion uses stack memory?**  
Each call stores parameters, variables, and return address.

**Q3. When is iteration preferred?**  
- Large recursion depth  
- Limited memory  
- Avoid overhead  

---

## ---- EXPERIMENT 4 — Fibonacci ----

**Q1. Why naive recursion is inefficient?**  
Repeats calculations → exponential time.

**Q2. Memoization relation to DP?**  
Stores results of subproblems → avoids recomputation.

**Q3. Space impact?**  
Extra memory used → O(n)

---

## ---- EXPERIMENT 5 — Tower of Hanoi ----

**Q1. Why moves = 2ⁿ − 1?**  
T(n) = 2T(n−1) + 1 → solution = 2ⁿ − 1

**Q2. What is recursion tree?**  
Tree representation of recursive calls.

**Q3. Risk of exponential algorithms?**  
Very slow for large inputs.

---

## ---- EXPERIMENT 6 — Recursive Binary Search ----

**Q1. Why must data be sorted?**  
To eliminate half using comparisons.

**Q2. Complexities?**  
Best: O(1)  
Average: O(log n)  
Worst: O(log n)

**Q3. What is divide and conquer?**  
Divide problem → solve → combine results.

---

## ---- EXPERIMENT 7 — Arrays 1D ----

**Q1. Why index access is O(1)?**  
Direct address calculation.

**Q2. Why insertion at start is O(n)?**  
Requires shifting all elements.

**Q3. Static vs Dynamic arrays?**  
Static = fixed size  
Dynamic = resizable

---

## ---- EXPERIMENT 8 — Arrays 2D ----

**Q1. Complexity of scanning matrix?**  
O(n × m)

**Q2. Real-world use?**  
Images, spreadsheets, games

**Q3. Memory layout?**  
Row-major order

---

## ---- EXPERIMENT 9 — Dynamic Array ----

**Q1. What is amortized complexity?**  
Average cost over many operations.

**Q2. Why doubling helps?**  
Reduces number of resizes.

**Q3. Why pop is O(1)?**  
Just decreases size.

---

## ---- EXPERIMENT 10 — Singly Linked List ----

**Q1. Why search is O(n)?**  
Traverse node by node.

**Q2. Why insert at head is O(1)?**  
No traversal needed.

**Q3. Node structure?**  
Data + next pointer

---

## ---- EXPERIMENT 11 — Doubly Linked List ----

**Q1. Advantage over SLL?**  
Bidirectional traversal.

**Q2. Browser history?**  
Back/forward navigation.

**Q3. Deletion ease?**  
Access to previous node.

---

## ---- EXPERIMENT 12 — Stack + Parentheses Checker ----

**Q1. Why stack?**  
Follows LIFO for matching brackets.

**Q2. Why "([)]" fails?**  
Incorrect order.

**Q3. Underflow?**  
Pop from empty stack.

---

## ---- EXPERIMENT 13 — Queue using SLL ----

**Q1. Why BFS uses queue?**  
Processes level by level.

**Q2. FIFO meaning?**  
First In First Out.

**Q3. Scheduling example?**  
CPU scheduling, printer queue.

---
