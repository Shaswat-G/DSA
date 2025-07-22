When we have overlapping subproblems, we can use memoization to store the results of subproblems to avoid redundant calculations. This is particularly useful in dynamic programming.
Store the value in a table or dictionary after computing it for the first time, and check this table before performing the computation again.

### What is Memoization?

Memoization is a technique used to optimize recursive algos by storing the results of intermediate computations. It avoids the need to recompute results for the same inputs, thus improving efficiency.

### What is tabulation?

Tabulation is a bottom-up approach to dynamic programming where we solve smaller subproblems first and use their results to build up solutions to larger problems. It typically involves filling up a table iteratively.
This is different from memoization, which is a top-down approach that uses recursion and stores results in a cache.

---

## Grid-Based Dynamic Programming: Complete Problem-Solving Framework

This comprehensive guide analyzes all problems from `dp_on_grids.py`, providing exact recipes for recognizing patterns, implementing solutions, and optimizing them progressively from recursion to space-optimized tabulation.

### Problem Analysis & Pattern Recognition

#### 1. **Unique Paths in Grid** (Foundation Problem)

- **Problem Type:** Combinatorial counting with movement constraints
- **Movement:** Right, Down only
- **Goal:** Count all possible paths from top-left to bottom-right

#### 2. **Unique Paths with Obstacles**

- **Problem Type:** Combinatorial counting with blocked cells
- **Movement:** Right, Down only (but avoid obstacles)
- **Goal:** Count valid paths avoiding obstacles (-1 cells)

#### 3. **Minimum Path Sum in Grid**

- **Problem Type:** Path optimization with costs
- **Movement:** Right, Down only
- **Goal:** Find path with minimum sum of cell values

#### 4. **Minimum Path Sum in Triangle**

- **Problem Type:** Path optimization in triangular structure
- **Movement:** Down, Down-right (triangle constraints)
- **Goal:** Find minimum sum path from top to any bottom cell

#### 5. **Maximum Path Sum (First to Last Row)**

- **Problem Type:** Path optimization with multi-directional movement
- **Movement:** Down, Down-left, Down-right
- **Goal:** Find maximum sum path from any first-row cell to any last-row cell

---

## Abstract Recipe Framework

### Phase 1: Problem Recognition & Setup

#### **When to Use Recursion?**

1. **Question hints:** "all possible paths", "find optimal path", "count ways"
2. **Multiple choices:** At each step, you have multiple movement options
3. **Optimal substructure:** Best solution depends on best solutions to subproblems
4. **Overlapping subproblems:** Same cell visited via different paths

#### **Why Greedy Fails?**

- Greedy only considers immediate best choice (local optimum)
- Grid problems require considering all future consequences
- Example: In min path sum, taking smallest immediate step might lead to larger future costs

#### **Time Complexity Intuition:**

- **Recursive (no memo):** O(choices^cells) = O(2^(m\*n)) for most grid problems
- **With memoization:** O(number of unique states) = O(m\*n) typically
- **Space complexity:** O(m\*n) for memo table + O(m+n) for recursion stack

---

### Phase 2: Recursive Solution Recipe

#### **Step 1: Define Recursive Function Signature**

```python
def helper(row, col, grid, additional_params):
    # Returns: count/min_sum/max_sum/boolean based on problem type
```

#### **Step 2: Write Base Cases**

```python
# Pattern A: Out of bounds
if row < 0 or col < 0 or row >= rows or col >= cols:
    return 0 (for counting) / float('inf') (for min) / float('-inf') (for max)

# Pattern B: Destination reached
if row == target_row and col == target_col:
    return 1 (for counting) / grid[row][col] (for sum problems)

# Pattern C: Invalid state (obstacles)
if grid[row][col] == obstacle_marker:
    return 0 (for counting) / float('inf') (for min)
```

#### **Step 3: Write Recursive Case**

```python
# For counting problems:
result = sum(helper(new_row, new_col, grid, params) for each valid move)

# For optimization problems (min/max):
choices = [helper(new_row, new_col, grid, params) for each valid move]
result = grid[row][col] + min/max(choices)
```

#### **Step 4: What Should Function Return?**

- **Counting problems:** Integer (number of paths)
- **Min/Max sum problems:** Integer/Float (optimal sum value)
- **Existence problems:** Boolean (True if path exists)
- **Path reconstruction:** List/Tuple (actual path)

---

### Phase 3: Memoization Conversion Recipe

#### **Step 1: Add Memoization Structure**

```python
# For 2D grid problems:
memo = [[-1 for _ in range(cols)] for _ in range(rows)]

# For triangle problems:
memo = [[-1 for _ in range(i+1)] for i in range(rows)]

# Initialize known values:
memo[start_row][start_col] = base_value
```

#### **Step 2: Add Memoization Checks**

```python
def helper(row, col, grid, memo):
    # Check if already computed
    if memo[row][col] != -1:
        return memo[row][col]

    # ... base cases ...

    # Compute result
    result = compute_recursive_result()

    # Store and return
    memo[row][col] = result
    return result
```

#### **Critical Memoization Cautions:**

1. **Initialization value:** Use -1 for impossible values, 0 might be valid result
2. **Origin point handling:** Initialize start position correctly
3. **Multiple origins:** Some problems need separate memo tables for each starting point
4. **Bounds checking:** Always validate indices before accessing memo

---

### Phase 4: Tabulation Conversion Recipe

#### **Step 1: Identify Dependencies**

- Analyze recursive calls to understand which cells depend on which
- Common patterns: current cell depends on cells above, left, or diagonally above

#### **Step 2: Determine Iteration Order**

```python
# For top-left to bottom-right dependency:
for row in range(rows):
    for col in range(cols):
        # Fill dp[row][col]

# For bottom-up (triangle problems):
for row in range(rows-1, -1, -1):
    for col in range(row+1):
        # Fill dp[row][col]
```

#### **Step 3: Convert Recursive Logic**

```python
# Memoization pattern:
if base_case:
    return base_value
result = combine(helper(dependencies))
memo[row][col] = result

# Tabulation equivalent:
if base_case:
    dp[row][col] = base_value
else:
    dp[row][col] = combine(dp[dependency_positions])
```

#### **Step 4: Handle Base Cases in Loop**

```python
for row in range(rows):
    for col in range(cols):
        if row == 0 and col == 0:  # Start position
            dp[row][col] = initial_value
        else:
            # Regular recurrence
            up = dp[row-1][col] if row > 0 else invalid_value
            left = dp[row][col-1] if col > 0 else invalid_value
            dp[row][col] = grid[row][col] + min/max(up, left)
```

---

### Phase 5: Space Optimization Recipe

#### **When Can We Space Optimize?**

- Current row only depends on previous row(s)
- We don't need the entire DP table for final answer
- Common in linear scans (left-to-right, top-to-bottom)

#### **Step 1: Identify Required Previous States**

```python
# If only previous row needed:
prev_row = [initial_values]

# If only two previous rows needed:
prev_prev = [...]
prev = [...]
```

#### **Step 2: Rolling Array Pattern**

```python
for row in range(rows):
    curr = [0] * cols  # Current row
    for col in range(cols):
        if base_case:
            curr[col] = base_value
        else:
            # Use prev_row[col], curr[col-1], etc.
            curr[col] = combine(prev_row[col], curr[col-1])
    prev_row = curr  # Roll forward
```

#### **Step 3: Single Array Optimization (Advanced)**

```python
# When updates can be done in-place:
dp = [initial_values]
for row in range(1, rows):
    for col in range(cols):
        # Update dp[col] using dp[col] (previous row) and dp[col-1] (current row)
        dp[col] = combine(dp[col], dp[col-1])
```

---

### Complexity Analysis Framework

| Approach        | Time Complexity | Space Complexity      | Implementation Difficulty |
| --------------- | --------------- | --------------------- | ------------------------- |
| Recursion       | O(2^(m×n))      | O(m+n) stack          | Easy                      |
| Memoization     | O(m×n)          | O(m×n) + O(m+n) stack | Medium                    |
| Tabulation      | O(m×n)          | O(m×n)                | Medium                    |
| Space-Optimized | O(m×n)          | O(n)                  | Hard                      |

---

### Problem-Specific Patterns

#### **Pattern 1: Basic Grid Navigation (Unique Paths)**

- **Movement:** Right, Down only
- **Recurrence:** `dp[i][j] = dp[i-1][j] + dp[i][j-1]`
- **Base:** `dp[0][0] = 1`
- **Space optimization:** Only need previous row

#### **Pattern 2: Grid with Obstacles**

- **Additional check:** Skip cells with obstacles
- **Recurrence:** Same as Pattern 1, but `dp[i][j] = 0` if obstacle
- **Initialization:** Handle obstacle at start position

#### **Pattern 3: Path Cost Optimization**

- **Goal:** Find min/max sum instead of counting
- **Recurrence:** `dp[i][j] = grid[i][j] + min/max(dp[i-1][j], dp[i][j-1])`
- **Base:** `dp[0][0] = grid[0][0]`

#### **Pattern 4: Triangle Structure**

- **Special constraint:** Row i has i+1 columns
- **Movement:** Down or down-right
- **Bottom-up optimization:** Start from last row, work upward

#### **Pattern 5: Multi-directional Movement**

- **Movement:** Down, down-left, down-right
- **Recurrence:** Consider all three previous positions
- **Boundary handling:** Check column bounds for diagonal moves

---

### Concrete Implementation Examples

#### **Example 1: Unique Paths (Complete Progression)**

**Recursive Solution:**

```python
def count_paths_recursive(m, n):
    def helper(row, col):
        # Base cases
        if row == 0 and col == 0:
            return 1
        if row < 0 or col < 0:
            return 0

        # Recursive case
        return helper(row-1, col) + helper(row, col-1)

    return helper(m-1, n-1)
```

**Memoization Conversion:**

```python
def count_paths_memo(m, n):
    memo = [[-1 for _ in range(n)] for _ in range(m)]

    def helper(row, col):
        if row == 0 and col == 0:
            return 1
        if row < 0 or col < 0:
            return 0

        if memo[row][col] != -1:  # Check memo
            return memo[row][col]

        result = helper(row-1, col) + helper(row, col-1)
        memo[row][col] = result  # Store result
        return result

    return helper(m-1, n-1)
```

**Tabulation Conversion:**

```python
def count_paths_tab(m, n):
    dp = [[0 for _ in range(n)] for _ in range(m)]

    # Fill table bottom-up
    for row in range(m):
        for col in range(n):
            if row == 0 and col == 0:
                dp[row][col] = 1
            else:
                up = dp[row-1][col] if row > 0 else 0
                left = dp[row][col-1] if col > 0 else 0
                dp[row][col] = up + left

    return dp[m-1][n-1]
```

**Space Optimization:**

```python
def count_paths_optimized(m, n):
    prev = [1] * n  # Previous row, all 1s for first row

    for row in range(1, m):
        curr = [0] * n
        for col in range(n):
            left = curr[col-1] if col > 0 else 0
            curr[col] = prev[col] + left
        prev = curr

    return prev[n-1]
```

---

#### **Example 2: Minimum Path Sum (Key Differences)**

**Recursive with Path Cost:**

```python
def min_path_sum_recursive(grid):
    rows, cols = len(grid), len(grid[0])

    def helper(row, col):
        # Base cases
        if row < 0 or col < 0:
            return float('inf')  # Invalid path
        if row == 0 and col == 0:
            return grid[0][0]

        # Recursive case with cost
        up_cost = helper(row-1, col)
        left_cost = helper(row, col-1)
        return grid[row][col] + min(up_cost, left_cost)

    return helper(rows-1, cols-1)
```

**Key Tabulation Pattern:**

```python
def min_path_sum_tab(grid):
    rows, cols = len(grid), len(grid[0])
    dp = [[0] * cols for _ in range(rows)]

    for row in range(rows):
        for col in range(cols):
            if row == 0 and col == 0:
                dp[row][col] = grid[row][col]
            else:
                up = dp[row-1][col] if row > 0 else float('inf')
                left = dp[row][col-1] if col > 0 else float('inf')
                dp[row][col] = grid[row][col] + min(up, left)

    return dp[rows-1][cols-1]
```

---

### Debugging and Common Pitfalls

#### **Memoization Pitfalls:**

1. **Wrong initialization:** Using 0 instead of -1 when 0 is a valid result
2. **Index errors:** Not checking bounds before accessing memo table
3. **Multiple starting points:** Need separate memo tables or reset between calls

#### **Tabulation Pitfalls:**

1. **Wrong iteration order:** Dependencies must be computed before current cell
2. **Base case handling:** Forgetting to handle starting position specially
3. **Boundary conditions:** Not checking row > 0, col > 0 before accessing dp[row-1][col]

#### **Space Optimization Pitfalls:**

1. **Overwriting needed values:** Updating in wrong order
2. **Array size mismatch:** Using wrong dimensions for rolling arrays
3. **Lost state:** Forgetting to save curr to prev after each iteration

---

### Master Template for Any Grid DP Problem

```python
def solve_grid_dp(grid, problem_type):
    """
    Master template for grid DP problems
    problem_type: 'count', 'min_sum', 'max_sum', 'exists'
    """
    if not grid or not grid[0]:
        return 0 if problem_type == 'count' else float('inf')

    rows, cols = len(grid), len(grid[0])

    # Step 1: Choose return values for each problem type
    if problem_type == 'count':
        invalid_value = 0
        initial_value = 1
        combine_func = lambda x, y: x + y
    elif problem_type == 'min_sum':
        invalid_value = float('inf')
        initial_value = grid[0][0]
        combine_func = lambda x, y: min(x, y)
    elif problem_type == 'max_sum':
        invalid_value = float('-inf')
        initial_value = grid[0][0]
        combine_func = lambda x, y: max(x, y)

    # Step 2: Initialize DP table
    dp = [[invalid_value] * cols for _ in range(rows)]
    dp[0][0] = initial_value

    # Step 3: Fill table with problem-specific logic
    for row in range(rows):
        for col in range(cols):
            if row == 0 and col == 0:
                continue

            # Handle obstacles if needed
            if hasattr(grid[row][col], '__eq__') and grid[row][col] == -1:
                dp[row][col] = invalid_value
                continue

            # Collect valid transitions
            transitions = []
            if row > 0:
                transitions.append(dp[row-1][col])
            if col > 0:
                transitions.append(dp[row][col-1])

            # Apply problem-specific combination
            if transitions:
                if problem_type in ['min_sum', 'max_sum']:
                    dp[row][col] = grid[row][col] + combine_func(*transitions)
                else:
                    dp[row][col] = sum(transitions)

    return dp[rows-1][cols-1]
```

---

---

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
