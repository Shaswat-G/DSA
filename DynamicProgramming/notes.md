When we have overlapping subproblems, we can use memoization to store the results of subproblems to avoid redundant calculations. This is particularly useful in dynamic programming.
Store the value in a table or dictionary after computing it for the first time, and check this table before performing the computation again.

### What is Memoization?

Memoization is a technique used to optimize recursive algos by storing the results of intermediate computations. It avoids the need to recompute results for the same inputs, thus improving efficiency.

### What is tabulation?

Tabulation is a bottom-up approach to dynamic programming where we solve smaller subproblems first and use their results to build up solutions to larger problems. It typically involves filling up a table iteratively.
This is different from memoization, which is a top-down approach that uses recursion and stores results in a cache.

---

## Dynamic Programming: Insights, Intuition, and Problem-Solving Patterns

This section distills the key strategies, mental models, and step-by-step approaches from the problems in `practice_dp.py`. Use it as a guide for tackling DP problems rigorously and efficiently.

### 1. Recognizing DP Problems

- **Overlapping Subproblems:** The same subproblem is solved multiple times (e.g., Fibonacci, grid paths).
- **Optimal Substructure:** The optimal solution can be constructed from optimal solutions to subproblems.
- **State Definition:** Identify what uniquely describes a subproblem (e.g., index, previous choice).

### 2. General DP Problem-Solving Pattern

1. **Define the State:** What parameters uniquely describe a subproblem? (e.g., `i`, `prev_activity`)
2. **Write the Recurrence:** Express the solution in terms of smaller states.
3. **Base Case:** Specify the simplest input and its direct answer.
4. **Implement Recursion:** Write a function that solves the problem recursively.
5. **Memoize:** Store results of subproblems to avoid recomputation.
6. **Tabulate (Optional):** Convert recursion to iteration for space/time efficiency.

### 3. Example Patterns from practice_dp.py

#### A. Fibonacci (Classic DP)

- **State:** `n` (the term to compute)
- **Recurrence:** `fib(n) = fib(n-1) + fib(n-2)`
- **Base Case:** `fib(0) = 0`, `fib(1) = 1`
- **Memoization:** Store results in a dictionary.
- **Tabulation:** Build up from base cases iteratively.

#### B. Frog Jump (Min Energy)

- **State:** `stair` (current stair)
- **Recurrence:**
  - `dp[i] = min(dp[i-1] + abs(H[i] - H[i-1]), dp[i-2] + abs(H[i] - H[i-2]))`
- **Base Case:** `dp[0] = 0`, `dp[1] = abs(H[1] - H[0])`
- **Pattern:** Use two variables for O(1) space, or a DP array for clarity.

#### C. Max Non-Adjacent Sum (House Robber)

- **State:** `i` (current index)
- **Recurrence:**
  - `dp[i] = max(dp[i-1], dp[i-2] + array[i])`
- **Base Case:** `dp[0] = array[0]`, `dp[1] = max(array[0], array[1])`
- **Pattern:** Rolling window for O(1) space.

#### D. Ninja Training (2D DP)

- **State:** `(day, prev_activity)`
- **Recurrence:**
  - For each activity not equal to `prev_activity`,
    `dp[day][prev_activity] = max(grid[day][activity] + dp[day+1][activity])`
- **Base Case:** When `day == days`, return 0.
- **Pattern:** Use a 2D DP table to memoize results for each (day, prev_activity).

### 4. Intuition and Mental Models

- **State Transition:** Always ask: "What choices do I have at this step? How does my state change?"
- **Recursive Tree:** Visualize the recursion tree. Memoization prunes repeated branches.
- **Tabulation:** Imagine filling a table from the smallest subproblems up.
- **Space Optimization:** If only previous states are needed, use rolling variables.

### 5. Complexity Analysis

| Problem               | State Space         | Time Complexity       | Space Complexity    |
| --------------------- | ------------------- | --------------------- | ------------------- |
| Fibonacci (memo)      | O(N)                | O(N)                  | O(N)                |
| Fibonacci (tab)       | O(N)                | O(N)                  | O(1)                |
| Frog Jump             | O(N)                | O(N)                  | O(1) or O(N)        |
| Max Non-Adj Sum       | O(N)                | O(N)                  | O(1)                |
| Ninja Training (memo) | O(days\*activities) | O(days\*activities^2) | O(days\*activities) |

### 6. Instructional Steps for DP Problems

1. **Identify the state:** What parameters change as you progress?
2. **Write the recurrence:** How does the answer depend on smaller states?
3. **Implement recursion:** Write a function for the subproblem.
4. **Add memoization:** Store results in a table or dict.
5. **Convert to tabulation:** (Optional) Build the solution bottom-up.
6. **Optimize space:** Use rolling variables if possible.
7. **Test edge cases:** Empty input, single element, etc.

### 7. Coaching Tips

- Always start by defining the state and recurrence.
- Use memoization for overlapping subproblems.
- Tabulate for space/time efficiency when possible.
- Visualize the DP table and transitions.
- Practice converting recursion to tabulation.
- Analyze time and space complexity for every approach.

---
