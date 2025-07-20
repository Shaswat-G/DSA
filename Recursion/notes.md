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

---

## 9 Recursion & Brute-Force Patterns: DSA Problem Templates, Arguments, and Complexity Analysis

This section abstracts the core patterns, function templates, argument design, and mathematical reasoning behind the problems in `practice.py` and `practice_2.py`. It is designed to coach you through rigorous, step-by-step thinking for recursion and brute-force approaches, including time and space complexity analysis.

### A. Problem Types & Patterns

#### 1. Parameterized Recursion

**Pattern:** Track state via function arguments (e.g., sum, product, index).
**Examples:**

- Sum of first N numbers: `sum_to_n(i, sum)`
- Factorial: `factorial_parameterised(i, product)`
- Reverse array: `rec_reverse_array(left, right, array)`

**Template:**

```python
def func(param1, param2, ...):
    if base_case:
        return result
    # update parameters
    return func(updated_param1, updated_param2, ...)
```

**Complexity:**

- Time: O(N) for linear problems (sum, factorial, reverse)
- Space: O(N) due to recursion stack

#### 2. Mathematical Recursion

**Pattern:** Return value is built from recursive calls, not tracked in parameters.
**Examples:**

- Factorial: `factorial(n)`
- Fibonacci: `print_fibonacci(n)`
- Sum of array: `sum_n(n)`

**Template:**

```python
def func(n):
    if base_case:
        return result
    return combine(func(smaller_n), ...)
```

**Complexity:**

- Time: O(2^N) for naive Fibonacci (exponential), O(N) for linear problems
- Space: O(N) stack depth

#### 3. Multiple Recursion (Branching)

**Pattern:** Each call makes multiple recursive calls (e.g., include/exclude, left/right).
**Examples:**

- Fibonacci: two calls per node
- Subsequence generation: include/exclude each element

**Template:**

```python
def func(index):
    if base_case:
        return result
    result1 = func(index + 1)
    result2 = func(index + 1)
    return combine(result1, result2)
```

**Complexity:**

- Time: O(2^N) for subsequences, O(2^N) for naive Fibonacci
- Space: O(N) stack depth

#### 4. Backtracking & Combinatorial Generation

**Pattern:** Explore all configurations, undo choices (backtrack), use mutable lists for state.
**Examples:**

- Subsets: `print_all_subs`, `all_unique_subsets`
- Permutations: `all_permutations`
- Combination sum: `combination_sum`, `combination_sum_unique`

**Template:**

```python
def backtrack(current, index, ...):
    if base_case:
        collect(current)
        return
    # Include
    current.append(choice)
    backtrack(current, index + 1, ...)
    current.pop()
    # Exclude or skip duplicates
    backtrack(current, next_index, ...)
```

**Complexity:**

- Time: O(2^N) for subsets, O(N!) for permutations, O(2^N) to O(N^2) for combinations (depends on pruning)
- Space: O(N) stack depth, plus output size

#### 5. Early Termination & Counting

**Pattern:** Use return values (bool/int) to stop recursion early or count solutions.
**Examples:**

- Find one subset with sum k: `one_subs_with_sum_k`
- Count subsets with sum k: `count_subs_with_sum_k`

**Template:**

```python
def rec(...):
    if base_case:
        if condition:
            return True/1
        return False/0
    if rec(...):
        return True
    return False
```

**Complexity:**

- Time: O(2^N) worst case, but may terminate early
- Space: O(N)

#### 6. Unique Solutions with Duplicates

**Pattern:** Sort input, skip duplicates at each recursion level.
**Examples:**

- Unique subsets: `all_unique_subsets`
- Unique permutations: `all_permutations` (with duplicate handling)
- Unique combinations: `combination_sum_unique`

**Template:**

```python
def rec(index, ...):
    # Include
    ...
    # Exclude and skip duplicates
    while index < len(array) and array[index] == array[prev]:
        index += 1
    rec(index, ...)
```

**Complexity:**

- Time: O(2^N) for subsets, O(N!) for permutations, but output is unique
- Space: O(N)

### B. Function Template Design & Arguments

1. **State Tracking:** Use parameters to track current state (index, sum, product, current subset/permutation).
2. **Mutable Collections:** Pass lists to collect results (subsets, permutations, combinations).
3. **Visited/Used Arrays:** For permutations, use boolean arrays to track used elements.
4. **Sorting for Uniqueness:** Always sort input before recursion to handle duplicates efficiently.
5. **Early Exit:** Use return values to terminate recursion early when a solution is found.
6. **Backtracking:** Always undo changes to mutable state after recursive calls.

### C. Mathematical Reasoning & Complexity Analysis

#### 1. Brute Force vs Recursion

- **Brute Force:** Enumerate all possibilities using loops or recursion. Time complexity is exponential for combinatorial problems.
- **Recursion:** Elegant, but may be inefficient without pruning or memoization. Stack depth is a key space cost.

#### 2. Time Complexity Table

| Problem Type        | Time Complexity (Brute/Recursion) | Space Complexity |
| ------------------- | --------------------------------- | ---------------- |
| Sum/Factorial       | O(N)                              | O(N)             |
| Fibonacci (naive)   | O(2^N)                            | O(N)             |
| Subsets/Power Set   | O(2^N)                            | O(N) + output    |
| Permutations        | O(N!)                             | O(N) + output    |
| Combination Sum     | O(2^N) to O(N^2)                  | O(N) + output    |
| Unique Subsets      | O(2^N)                            | O(N) + output    |
| Unique Permutations | O(N!)                             | O(N) + output    |
| Counting Solutions  | O(2^N)                            | O(N)             |

#### 3. Space Complexity

- **Recursion Stack:** O(N) for problems with depth N (subsets, permutations, sum, factorial).
- **Output Storage:** Additional space for storing all solutions (subsets, permutations, combinations).

#### 4. Pruning & Optimization

- **Early Termination:** Reduces unnecessary calls (e.g., stop when sum exceeds target).
- **Memoization:** For overlapping subproblems (e.g., Fibonacci, DP), use caching to reduce time to O(N).
- **Sorting & Skipping:** For uniqueness, sort and skip duplicates to avoid repeated work.

### D. Instructional Guidance: How to Approach Recursion Problems

1. **Identify the Problem Type:** Is it combinatorial, mathematical, or state-tracking?
2. **Define the Base Case:** What is the smallest input with a direct answer?
3. **Design Arguments:** What state needs to be tracked? Use parameters for index, sum, product, current solution.
4. **Write the Recursive Case:** How does the problem reduce? What choices are made at each step?
5. **Handle Duplicates:** Sort input and skip repeated values for unique solutions.
6. **Backtrack Properly:** Always undo changes to mutable state after recursion.
7. **Analyze Complexity:** Estimate time and space costs. For combinatorial problems, expect exponential time.
8. **Test Small Inputs:** Validate logic with minimal cases before scaling up.
9. **Optimize:** Use memoization or pruning where possible.

### E. Example: Permutations with Duplicates

```python
def all_permutations(array: List[int]) -> List[List[int]]:
    def rec(curr_permutation, visited, array, all_permutations):
        if len(curr_permutation) == len(array):
            all_permutations.append(curr_permutation.copy())
            return
        for i in range(len(array)):
            if visited[i]:
                continue
            if i > 0 and array[i] == array[i-1] and not visited[i-1]:
                continue
            visited[i] = True
            curr_permutation.append(array[i])
            rec(curr_permutation, visited, array, all_permutations)
            curr_permutation.pop()
            visited[i] = False
    all_permutations = []
    array.sort()
    visited = [False] * len(array)
    rec([], visited, array, all_permutations)
    return all_permutations
```

**Time Complexity:** O(N!)
**Space Complexity:** O(N) stack + output

### F. Example: Unique Subsets with Duplicates

```python
def all_unique_subsets(array: List[int]) -> List[List[int]]:
    def rec(current_subs, index, array, all_subs):
        if index == len(array):
            all_subs.append(current_subs.copy())
            return
        current_subs.append(array[index])
        rec(current_subs, index + 1, array, all_subs)
        current_subs.pop()
        new_index = index
        while new_index < len(array) and array[new_index] == array[index]:
            new_index += 1
        rec(current_subs, new_index, array, all_subs)
    all_subs = []
    array.sort()
    rec([], 0, array, all_subs)
    return all_subs
```

**Time Complexity:** O(2^N)
**Space Complexity:** O(N) stack + output

---

## Summary Table: Recursion Patterns & Complexity

| Pattern                 | Example Function          | Time Complexity | Space Complexity |
| ----------------------- | ------------------------- | --------------- | ---------------- |
| Parameterized Recursion | sum_to_n, factorial_param | O(N)            | O(N)             |
| Mathematical Recursion  | factorial, sum_n          | O(N)            | O(N)             |
| Multiple Recursion      | print_fibonacci, subsets  | O(2^N)          | O(N)             |
| Backtracking            | all_permutations, subsets | O(N!), O(2^N)   | O(N) + output    |
| Unique Solutions        | all_unique_subsets        | O(2^N)          | O(N) + output    |
| Counting/Early Exit     | count_subs_with_sum_k     | O(2^N)          | O(N)             |

---

## Coaching Tips

- Always start with the base case and recursive case.
- Use parameters to track all necessary state.
- For combinatorial problems, expect exponential time unless you prune or memoize.
- Sort input and skip duplicates for unique results.
- Backtrack by undoing changes to mutable state.
- Analyze both time and space complexity rigorously.
- Practice with small inputs and trace the call stack.

---

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
