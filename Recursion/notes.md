### 1 Understanding Recursion

| Concept            | Summary                                                                   |
| ------------------ | ------------------------------------------------------------------------- |
| **Self-reference** | A function calls itself with a smaller or simpler input.                  |
| **Base case**      | The simplest input for which the answer is known directly.                |
| **Recursive case** | The rule that reduces the problem to a smaller instance of itself.        |
| **Call stack**     | Each call has its own context; results are returned as calls complete.    |
| **Termination**    | Each call must progress toward the base case to avoid infinite recursion. |

Recursion solves problems by breaking them into smaller, similar subproblems, solving each recursively, and combining results.

---

### 2 Identifying Recursive Problems

1. **Self-similarity:** The problem can be defined in terms of smaller instances of itself.  
   _Example:_ A tree node defined by its subtrees.
2. **Divide-and-conquer:** The input can be split into independent parts whose solutions combine.  
   _Example:_ Merge sort, quick sort.
3. **Incremental reduction:** The problem can be simplified by removing one element at a time.  
   _Example:_ Summing an array, reversing a string.
4. **Combinatorial enumeration:** Counting or generating all possible ways or paths.  
   _Example:_ Generating subsets, counting paths in a grid.

If a problem can be expressed as “solution(n) = f(solution(smaller n))”, recursion is often suitable.

---

### 3 Steps to Write a Recursive Function

1. **Define** the function clearly.
2. **Identify the base case(s):** Specify the simplest input and its direct answer.
3. **Formulate the recursive case:** Express the solution in terms of smaller inputs.
4. **Ensure progress:** Each call must move closer to the base case.
5. **Combine results:** Use the results of recursive calls to build the final answer.

> **Tip:** Always verify that each recursive path reduces the problem size and reaches the base case.

---

### 4 Walk-through Examples

| Problem            | Recurrence Formula                | Base Case            |
| ------------------ | --------------------------------- | -------------------- |
| **Factorial**      | `fact(n) = n × fact(n-1)`         | `fact(0)=1`          |
| **Fibonacci**      | `fib(n) = fib(n-1)+fib(n-2)`      | `fib(0)=0, fib(1)=1` |
| **Sum of array**   | `sum(i,j) = a[i] + sum(i+1,j)`    | Single element       |
| **Reverse string** | `rev(s) = rev(s[1:]) + s[0]`      | Length ≤ 1           |
| **Binary search**  | Halve the array each call         | Empty sub-array      |
| **Height of tree** | `h(node)=1+max(h(left),h(right))` | Node is None         |

Each example demonstrates how the input size is reduced in every recursive step.

---

### 5 Intuition Boosters

- **Visualize the call tree:** Draw boxes for calls and arrows for returns to identify patterns.
- **Trace small inputs:** Test with minimal cases to validate logic.
- **Focus on child calls:** Determine what information is needed from recursive calls.
- **Use memoization:** Optimize repeated subproblems (e.g., Fibonacci, dynamic programming).
- **Convert to iteration:** Once the recursive logic is clear, practice iterative solutions.

---

### 6 Beginner Practice Set (Ordered by Difficulty)

| #   | Problem & Hint                 | Goals                                               |
| --- | ------------------------------ | --------------------------------------------------- |
| 1   | **Print 1 … n**                | Base case `n==0`, then print `n`, recurse on `n-1`. |
| 2   | **Factorial**                  | Direct mathematical recurrence.                     |
| 3   | **Nth Fibonacci (plain)**      | Observe inefficiency → learn memoization.           |
| 4   | **Count digits of an integer** | Remove last digit each call.                        |
| 5   | **Sum of digits**              | Same pattern, return sum.                           |
| 6   | **Reverse a string**           | Build result while unwinding recursion.             |
| 7   | **Power(x, n)**                | Use `pow(x,n)=pow(x,n//2)^2` (divide & conquer).    |
| 8   | **Find minimum in array**      | Compare first element with min of rest.             |
| 9   | **Check palindrome string**    | Compare ends, recurse on inner slice.               |
| 10  | **Binary search**              | Classical divide-and-conquer.                       |

#### Suggested Routine

1. **Write** the function stub and base case.
2. **Add** debug prints to observe shrinking input.
3. **Test** with small inputs (e.g., n=1,2).
4. **Remove debug prints and test larger cases.**
5. **Analyze** time and space complexity (call-stack depth ≈ input size unless halved per step).

---

### 7 Key Takeaways

- Recursion relies on solving smaller instances of the problem.
- Two essentials: **base case** and **progress toward it**.
- Recognize recursive problems by their self-similar structure.
- Practice with small, focused problems before tackling complex ones.

---

### 8 Recognizing and Applying Recursion: Problem Patterns & Use Cases

#### 1. Classic Problems Solvable with Recursion

**1. Divide and Conquer Algorithms**  
_Essential Idea:_ Break the problem into smaller subproblems, solve each recursively, and combine results.  
_Recursion Use:_ Each call works on a smaller part (e.g., merge sort, quick sort, binary search).

**2. Tree and Graph Traversals**  
_Essential Idea:_ Visit all nodes in a hierarchical or connected structure.  
_Recursion Use:_ Each call processes a node and recurses on its children or neighbors (e.g., preorder, inorder, postorder, DFS).

**3. Backtracking/Combinatorial Generation**  
_Essential Idea:_ Explore all possible configurations/choices, undoing choices as needed.  
_Recursion Use:_ Each call makes a choice, recurses, and backtracks (e.g., permutations, combinations, N-Queens, Sudoku).

**4. Dynamic Programming (Top-Down/Memoization)**  
_Essential Idea:_ Solve overlapping subproblems recursively, caching results.  
_Recursion Use:_ Each call solves a subproblem, stores result to avoid recomputation (e.g., Fibonacci, coin change, edit distance).

**5. Mathematical Recurrences**  
_Essential Idea:_ Problems defined by recurrence relations.  
_Recursion Use:_ Each call computes based on smaller values (e.g., factorial, Fibonacci, catalan numbers).

**6. String and Array Manipulation**  
_Essential Idea:_ Process or transform sequences by handling one element and recursing on the rest.  
_Recursion Use:_ Each call works on a smaller slice (e.g., reverse string, check palindrome, sum array).

**7. Path Finding and Counting**  
_Essential Idea:_ Count or enumerate all possible paths/ways to reach a goal.  
_Recursion Use:_ Each call explores a possible move (e.g., grid paths, climbing stairs, word break).

**8. Subset/Subset Sum/Power Set Problems**  
_Essential Idea:_ Generate all subsets or combinations.  
_Recursion Use:_ Each call includes/excludes an element (e.g., subsets, combination sum).

**9. Constructive Recursion (Building Structures)**  
_Essential Idea:_ Build complex structures recursively (e.g., binary trees, expression trees).  
_Recursion Use:_ Each call constructs a part and combines results.

**10. Game/Simulation Problems**  
_Essential Idea:_ Simulate all possible moves or outcomes.  
_Recursion Use:_ Each call represents a game state (e.g., minimax, tic-tac-toe, word ladder).

**11. Linked List Recursion**  
_Essential Idea:_ Process nodes recursively (e.g., reverse, merge, detect cycle).  
_Recursion Use:_ Each call processes a node and recurses on next.

**12. Expression Evaluation/Parsing**  
_Essential Idea:_ Parse or evaluate nested expressions.  
_Recursion Use:_ Each call processes a subexpression (e.g., arithmetic expression parser).

**13. Flood Fill/Connected Components**  
_Essential Idea:_ Fill or mark all connected regions.  
_Recursion Use:_ Each call marks a cell and recurses on neighbors.

**14. Recursion with Multiple Parameters/States**  
_Essential Idea:_ Track multiple changing variables (e.g., DP with i, j, k).  
_Recursion Use:_ Each call represents a unique state.

**15. Recursion with Pruning/Branch and Bound**  
_Essential Idea:_ Cut off unpromising branches early.  
_Recursion Use:_ Each call checks constraints before recursing (e.g., N-Queens, subset sum with early exit).

#### 2. Real-World & Interview/LeetCode Recursion Problems

- **Factorial** (classic): Direct recurrence.
- **Fibonacci Number** (LeetCode 509): Recurrence, memoization.
- **Climbing Stairs** (LeetCode 70): Count paths, DP.
- **Merge Sort/Quick Sort** (classic): Divide and conquer.
- **Binary Search** (classic): Halve array recursively.
- **Permutations/Combinations** (LeetCode 46, 77): Backtracking.
- **Subsets/Power Set** (LeetCode 78): Include/exclude recursion.
- **Generate Parentheses** (LeetCode 22): Backtracking.
- **N-Queens** (LeetCode 51): Backtracking with pruning.
- **Word Search** (LeetCode 79): DFS recursion.
- **Sudoku Solver** (LeetCode 37): Backtracking.
- **Letter Combinations of a Phone Number** (LeetCode 17): Backtracking.
- **Restore IP Addresses** (LeetCode 93): Backtracking.
- **Palindrome Partitioning** (LeetCode 131): Backtracking.
- **Reverse Linked List** (LeetCode 206): Recursive pointer manipulation.
- **Merge Two Sorted Lists** (LeetCode 21): Recursive merge.
- **Maximum Depth of Binary Tree** (LeetCode 104): Tree recursion.
- **Balanced Binary Tree** (LeetCode 110): Tree recursion.
- **Diameter of Binary Tree** (LeetCode 543): Tree recursion.
- **Same Tree/Symmetric Tree** (LeetCode 100, 101): Tree recursion.
- **Path Sum** (LeetCode 112): Tree recursion.
- **Flatten Binary Tree to Linked List** (LeetCode 114): Tree recursion.
- **Construct Binary Tree from Traversals** (LeetCode 105, 106): Recursive construction.
- **Word Break** (LeetCode 139): Recursion + memoization.
- **Coin Change** (LeetCode 322): Recursion + memoization.
- **Edit Distance** (LeetCode 72): Recursion + memoization.
- **Flood Fill** (LeetCode 733): DFS recursion.
- **Number of Islands** (LeetCode 200): DFS recursion.
- **Combination Sum** (LeetCode 39): Backtracking.
- **All Paths From Source to Target** (LeetCode 797): DFS recursion.
- **Unique Binary Search Trees** (LeetCode 96): Catalan recurrence.
- **Decode Ways** (LeetCode 91): Recursion + memoization.
- **House Robber** (LeetCode 198): Recursion + memoization.
- **Minimum Path Sum** (LeetCode 64): Recursion + memoization.
- **Scramble String** (LeetCode 87): Recursion + memoization.
- **Interleaving String** (LeetCode 97): Recursion + memoization.
- **Regular Expression Matching** (LeetCode 10): Recursion + memoization.
- **Wildcard Matching** (LeetCode 44): Recursion + memoization.

_This list covers all classic and modern recursion-based problems. If a problem can be defined in terms of smaller subproblems, involves exploring all possibilities, or has a natural divide-and-conquer structure, think of recursion!_

---
