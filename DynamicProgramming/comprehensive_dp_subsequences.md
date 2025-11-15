# Comprehensive Guide to Dynamic Programming on Subsequences

## Overview

DP on subsequences (also called DP on sequences or "DP with choice") is a class of problems where we decide whether to include or exclude each element. The core pattern is:

**State Definition**: `dp[i][j]` = result considering elements 0..i-1 with some constraint/target j

**Exploration Direction**: For each element at index i, we have two choices:
1. **Include** the element (if valid)
2. **Exclude** the element

**Recurrence**: Combine results from both choices (via AND, OR, MAX, MIN, COUNT, etc. depending on the problem)

## Roadmap — Important DP Topics

Below are the high-level, MECE (mutually exclusive, collectively exhaustive) categories you should be comfortable with when studying DP:

- DP on grids (2D walks, matrix path sums, DP for obstacles)
- DP on subsequences (include/exclude problems like subset sums and knapsack)
- Knapsack and variations (0/1, unbounded, bounded with weights/values)
- Coin change problems (min coins, count ways, combinations vs permutations)
- Partitioning problems (equal partition, min partition difference)
- Palindromic problems (palindrome partitioning, longest palindromic subsequence)

## Quick definitions — subsequence, subarray, subset

- Subsequence: derived from another sequence by deleting some elements without changing the order of the remaining elements.
- Subarray (or substring): contiguous elements from the sequence.
- Subset: a combinatorial selection of elements without regard to order (order doesn't matter).

## Quick steps for DP on subsequences

1. Express the subproblem state clearly, e.g., (index, remaining/target) or (index, capacity).
2. For each element (index) consider two actions: include or exclude. Convert those choices into a recurrence.
3. Identify base cases: end of array, target reached, or capacity exhausted.
4. Decide data shape: boolean decision, integer count, or min/max optimization — and choose combining operator accordingly.


---

## Problem 1: Subset Sum (Decision)

**Problem Statement**: 
Given an array and a target sum, determine if there exists a subset with sum equal to target.

**State**: `dp[i][j]` = True if we can form sum `j` using elements from first `i` elements

**Base Cases**:
- `dp[i][0] = True` for all i (empty subset always sums to 0)
- `dp[0][j] = False` for j > 0 (cannot form positive sum with zero elements)

**Recurrence**:
```
dp[i][j] = dp[i-1][j]  (exclude element i-1)
           OR
           dp[i-1][j - arr[i-1]]  (include element i-1, if j >= arr[i-1])
```

**Conceptual Notes**:
- Boolean decision problem (True/False)
- Indexing: dimensions are (n+1) × (target+1)
- Space optimization: rolling array reduces to O(target)

**Implementation Pattern**:
```python
def subset_sum(arr, target):
    n = len(arr)
    dp = [[False] * (target + 1) for _ in range(n + 1)]
    # Base: dp[i][0] = True
    for i in range(n + 1):
        dp[i][0] = True
    
    for i in range(1, n + 1):
        for j in range(1, target + 1):
            dp[i][j] = dp[i-1][j]  # exclude
            if j >= arr[i-1]:
                dp[i][j] = dp[i][j] or dp[i-1][j - arr[i-1]]  # include
    
    return dp[n][target]

**Note**: The last row `dp[n]` of the DP table contains, for each `j` in `0..target`, whether sum `j` is reachable using all array elements. This is very useful:
- For partition/closest-sum problems: check reachable sums near `total_sum / 2`.
- For counting problems: store integer counts instead of booleans in the same 2D table and the last row will give the count of subsets that form each sum.
```

---

## Problem 2: Count Subsets with Sum K

**Problem Statement**: 
Given an array, count the number of subsets with sum equal to target.

**Conceptual Change from Subset Sum**:
- Instead of boolean (True/False), we track **count** (integer)
- Recurrence combines counts via addition instead of OR

**State**: `dp[i][j]` = number of subsets using first i elements that sum to j

**Base Cases**:
- `dp[i][0] = 1` for all i (one way to make 0: empty subset)
- `dp[0][j] = 0` for j > 0

**Recurrence**:
```
dp[i][j] = dp[i-1][j]  (exclude element i-1)
           +
           dp[i-1][j - arr[i-1]]  (include element i-1, if j >= arr[i-1])
```

**Implementation Change**:
- Change data type from bool to int
- Combine counts via `+` instead of `or`

**Implementation Pattern**:
```python
def count_subsets_sum(arr, target):
    n = len(arr)
    dp = [[0] * (target + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = 1  # one way to make 0
    
    for i in range(1, n + 1):
        for j in range(1, target + 1):
            dp[i][j] = dp[i-1][j]  # exclude
            if j >= arr[i-1]:
                dp[i][j] += dp[i-1][j - arr[i-1]]  # include
    
    return dp[n][target]
```

---

## Problem 3: Partition Equal Subset Sum

**Problem Statement**: 
Given an array, determine if it can be partitioned into two subsets with equal sum.

**Conceptual Insight**:
- If array sum is odd, return False (cannot partition into equal halves)
- Otherwise, check if a subset with sum = total_sum / 2 exists
- **Reduces to Subset Sum problem with target = total_sum / 2**

**Implementation Pattern**:
```python
def partition_equal_subset_sum(arr):
    total_sum = sum(arr)
    if total_sum % 2 != 0:
        return False
    target = total_sum // 2
    return subset_sum(arr, target)
```

**Key Change**: 
- Problem type is different (partition vs. subset sum) but reduces to subset sum
- No new DP logic; reuse existing subset sum code

---

## Problem 4: Minimum Partition Difference

**Problem Statement**: 
Given an array, partition it into two subsets such that the absolute difference of their sums is minimized.

**Conceptual Insight**:
- Total sum = S
- If we partition into two subsets with sums s1 and s2, then s1 + s2 = S and we want to minimize |s1 - s2|
- If s1 = S/2 + x, then s2 = S/2 - x, so |s1 - s2| = 2|x|
- Minimize |s1 - s2| ⟺ find s1 as close to S/2 as possible
- Use subset sum DP to find all reachable sums, then pick the one closest to S/2

**Implementation Pattern**:
```python
def min_partition_diff(arr):
    total_sum = sum(arr)
    n = len(arr)
    # Build DP table for subset sum (all possible sums)
    dp = [[False] * (total_sum + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = True
    
    for i in range(1, n + 1):
        for j in range(total_sum + 1):
            dp[i][j] = dp[i-1][j]
            if j >= arr[i-1]:
                dp[i][j] = dp[i][j] or dp[i-1][j - arr[i-1]]
    
    # Find sum closest to total_sum // 2
    min_diff = float('inf')
    for j in range(total_sum // 2 + 1):
        if dp[n][j]:
            s1 = j
            s2 = total_sum - j
            min_diff = min(min_diff, abs(s1 - s2))
    
    return min_diff
```

**Key Change**:
- Not a boolean decision; extract all reachable sums from DP table
- Post-process: find the sum closest to the target half-sum

---

## Problem 5: Target Sum (Coin Change Variant)

**Problem Statement**: 
Given an array of positive integers, assign +/- sign to each to reach a target sum. Count or find all ways.

**Conceptual Insight**:
- Assign signs: arr becomes +/- arr
- If positive subset sums to P and negative subset sums to N, then P - N = target
- Also, P + N = total_sum (all elements used)
- Solving: P - N = target and P + N = S → P = (S + target) / 2
- Problem reduces to: count subsets with sum = (S + target) / 2

**Implementation Pattern**:
```python
def target_sum(arr, target):
    total_sum = sum(arr)
    # Check feasibility
    if (total_sum + target) % 2 != 0 or total_sum < abs(target):
        return 0
    subset_target = (total_sum + target) // 2
    return count_subsets_sum(arr, subset_target)
```

**Key Changes**:
- Problem interpretation is different (signs vs. inclusion)
- DP logic is count_subsets_sum (reused from Problem 2)
- Preprocessing transforms the problem

---

## Problem 6: Coin Change – Minimum Coins

**Problem Statement**: 
Given coin denominations and a target amount, find the minimum number of coins needed.

**Key Difference from Subset Sum**:
- **Unbounded knapsack**: each coin can be used unlimited times (not just 0 or 1)
- **Optimization**: minimize the count of coins, not a boolean decision

**State**: `dp[j]` = minimum coins needed to make amount j

**Base Cases**:
- `dp[0] = 0` (zero coins for amount 0)
- `dp[j] = ∞` for j > 0 initially

**Recurrence** (1D rolling array, unbounded):
```
for each coin in coins:
    for each amount from coin to target:
        dp[amount] = min(dp[amount], dp[amount - coin] + 1)
```

Why unbounded? When we process amount j after updating amounts < j, the cell dp[amount - coin] might already include the current coin.

**Implementation Pattern**:
```python
def coin_change_min(coins, target):
    dp = [float('inf')] * (target + 1)
    dp[0] = 0
    
    for amount in range(1, target + 1):
        for coin in coins:
            if coin <= amount:
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)
    
    return dp[target] if dp[target] != float('inf') else -1
```

**Conceptual Changes from Subset Sum**:
1. Unbounded (each element reusable)
2. Minimization instead of boolean decision
3. Base case: dp[0] = 0, others = ∞
4. Recurrence: min() instead of or
5. Loop order: amount (outer), coin (inner) for 1D DP

---

## Problem 7: Coin Change – Maximum Ways / Count Combinations

**Problem Statement**: 
Count the number of ways to make an amount using given coins (each coin unlimited).

**Key Difference**:
- Instead of minimizing count, count the number of distinct ways
- Still unbounded knapsack
- Recurrence combines via addition (not min or or)

**State**: `dp[j]` = number of ways to make amount j

**Base Cases**:
- `dp[0] = 1` (one way: use no coins)
- `dp[j] = 0` for j > 0 initially

**Recurrence** (1D, unbounded):
```
for each coin in coins:
    for each amount from coin to target:
        dp[amount] += dp[amount - coin]
```

**Why this order?**
- We iterate coins in outer loop to count **combinations** (not permutations)
- E.g., [1, 2] with target 3: [1+2] is one way, not counted twice as [2+1]

**Implementation Pattern**:
```python
def coin_change_ways(coins, target):
    dp = [0] * (target + 1)
    dp[0] = 1
    
    for coin in coins:
        for amount in range(coin, target + 1):
            dp[amount] += dp[amount - coin]
    
    return dp[target]
```

**Conceptual Changes from Minimum Coins (Problem 6)**:
1. Goal: count ways, not minimize coins
2. Recurrence: `+=` instead of `min()`
3. Loop order: **coin (outer), amount (inner)** for combinations
4. Base case: dp[0] = 1 (same)

---

## Problem 8: 0/1 Knapsack – Maximum Value

**Problem Statement**: 
Given items with weights and values, and a knapsack of capacity W, select items to maximize value without exceeding weight capacity.

**Key Difference from Subset Sum**:
- Each item has a weight AND a value
- Goal: maximize value subject to weight constraint
- Each item used at most once (0/1, not unbounded)

**State**: `dp[i][w]` = maximum value using first i items with weight limit w

**Base Cases**:
- `dp[0][w] = 0` for all w (no items → zero value)
- `dp[i][0] = 0` for all i (no capacity → zero value)

**Recurrence**:
```
dp[i][w] = dp[i-1][w]  (exclude item i-1)
           OR
           value[i-1] + dp[i-1][w - weight[i-1]]  (include item i-1, if w >= weight[i-1])
```
Take the maximum of the two options.

**Implementation Pattern**:
```python
def knapsack_0_1(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            dp[i][w] = dp[i-1][w]  # exclude
            if w >= weights[i-1]:
                dp[i][w] = max(dp[i][w], values[i-1] + dp[i-1][w - weights[i-1]])
    
    return dp[n][capacity]
```

**Conceptual Changes from Subset Sum**:
1. Dimensions: (n+1) × (capacity+1) same, but semantics differ
2. Goal: maximize value, not boolean/count
3. Each item has two attributes (weight, value), not just sum
4. Recurrence: max() instead of or
5. Base cases: all zeros (no items, no value)

---

## Problem 9: Unbounded Knapsack – Maximum Value

**Problem Statement**: 
Same as 0/1 knapsack, but each item can be used unlimited times.

**Key Difference from 0/1 Knapsack**:
- Bounded vs. unbounded (each item reusable)
- DP loop order changes
- Same recurrence structure, but applied differently

**State**: `dp[w]` = maximum value with weight limit w (rolling array, since unbounded)

**Base Cases**:
- `dp[0] = 0`
- `dp[w] = 0` for w > 0 initially

**Recurrence** (1D, unbounded):
```
for each item:
    for each weight from item.weight to capacity:
        dp[weight] = max(dp[weight], item.value + dp[weight - item.weight])
```

**Implementation Pattern**:
```python
def knapsack_unbounded(weights, values, capacity):
    dp = [0] * (capacity + 1)
    
    for i in range(len(weights)):
        for w in range(weights[i], capacity + 1):
            dp[w] = max(dp[w], values[i] + dp[w - weights[i]])
    
    return dp[capacity]
```

**Conceptual Changes from 0/1 Knapsack**:
1. Loop order: item (outer), weight (inner) — allows reuse
2. 1D DP vs. 2D — space optimization
3. Recurrence structure same, but applied in different order
4. Key insight: when we update dp[w], if w - weight[i] ≤ w, the updated dp[w - weight[i]] may already include item i

---

## Problem 10: Rod Cutting

**Problem Statement**: 
Given a rod of length n and a price table (length → price), cut the rod into pieces to maximize profit.

**Relationship to Knapsack**:
- Rod length is like knapsack capacity
- Each cut is like an item (length, price)
- Cuts can be repeated (unbounded)
- Goal: maximize price subject to length constraint

**State**: `dp[len]` = maximum price for rod of length len

**Base Cases**:
- `dp[0] = 0` (length 0 → no profit)

**Recurrence**:
```
dp[len] = max(dp[len], price[cut_len] + dp[len - cut_len])
          for each cut_len ≤ len
```

**Implementation Pattern**:
```python
def rod_cutting(n, prices):
    # prices[i] = price for length i+1
    dp = [0] * (n + 1)
    
    for length in range(1, n + 1):
        for cut_len in range(1, length + 1):
            dp[length] = max(dp[length], prices[cut_len - 1] + dp[length - cut_len])
    
    return dp[n]
```

**Conceptual Notes**:
- Functionally identical to unbounded knapsack
- Different problem context (rod vs. items)
- All cuts are available and reusable
- 1D DP sufficient (rolling array style)

---

## Problem 11: Coin Change – Maximum Coins (Minimize Coins Greedy Fails)

**Problem Statement**: 
Given coin denominations, find the **maximum number of coins** to make a target amount.

**Conceptual Insight**:
- Opposite of "minimum coins"
- Each coin reusable (unbounded)
- Maximize the count

**State**: `dp[amount]` = maximum coins to make amount (or -1 if impossible)

**Base Cases**:
- `dp[0] = 0`
- `dp[amount] = -1` initially

**Recurrence**:
```
for each amount from 1 to target:
    for each coin:
        if coin <= amount and dp[amount - coin] != -1:
            dp[amount] = max(dp[amount], dp[amount - coin] + 1)
```

**Implementation Pattern**:
```python
def coin_change_max(coins, target):
    dp = [-1] * (target + 1)
    dp[0] = 0
    
    for amount in range(1, target + 1):
        for coin in coins:
            if coin <= amount and dp[amount - coin] != -1:
                dp[amount] = max(dp[amount], dp[amount - coin] + 1)
    
    return dp[target]
```

**Conceptual Changes from Minimum Coins**:
1. Goal: maximize instead of minimize
2. Base case: -1 for unreachable (not ∞), 0 for target 0
3. Recurrence: max() instead of min()
4. Check for unreachable states (-1) explicitly

---

## Problem 12: Subsequence Sum (Sum of Subsequence, not Subset)

**Problem Statement**: 
Find the sum of the longest increasing subsequence (LIS) of values, or similar.

**Note**: This overlaps with string/array subsequence problems, which are often solved with different DP (like LCS, LIS) rather than the "include/exclude" pattern.

**Key Difference**:
- Order matters (subsequence preserves order, subset doesn't)
- May involve additional constraints (increasing, decreasing, etc.)
- State often includes position and last chosen value

**State Example (LIS by value sum)**:
`dp[i]` = maximum sum of increasing subsequence ending at index i

**Base Case**:
`dp[i] = arr[i]` (single element)

**Recurrence**:
```
dp[i] = arr[i] + max(dp[j] for all j < i where arr[j] < arr[i])
        or just arr[i] if no such j exists
```

**Implementation Pattern (Simplified)**:
```python
def lis_sum(arr):
    n = len(arr)
    dp = arr[:]  # each element is at least its own value
    
    for i in range(n):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], arr[i] + dp[j])
    
    return max(dp)
```

**Conceptual Notes**:
- Different from subset/partition problems
- Preserves order; not independent choices
- Often O(n²) for 1D DP; O(n log n) with advanced structures (binary search)

---

## Problem 13: Palindrome Partitioning – Minimum Cuts

**Problem Statement**: 
Given a string, partition it into minimum number of palindromic substrings.

**Conceptual Insight**:
- Use 2D DP to precompute palindrome ranges: `isPalin[i][j]` = is s[i..j] a palindrome?
- Use 1D DP for partitioning: `dp[i]` = minimum cuts for s[0..i-1]

**State**: 
- `isPalin[i][j]` = True if s[i..j] is palindrome
- `dp[i]` = minimum cuts for first i characters

**Base Cases**:
- `isPalin[i][i] = True` (single char)
- `dp[0] = 0` (zero cuts needed for empty string)
- `dp[i] = i - 1` (worst: each char is separate)

**Recurrence**:
```
isPalin[i][j] = (s[i] == s[j]) and isPalin[i+1][j-1]

dp[i] = min(dp[j] + 1 for all j < i where isPalin[j][i-1])
```

**Implementation Pattern**:
```python
def palindrome_partitions(s):
    n = len(s)
    isPalin = [[False] * n for _ in range(n)]
    
    # Compute palindromes
    for i in range(n):
        isPalin[i][i] = True
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                isPalin[i][j] = (length == 2) or isPalin[i+1][j-1]
    
    # Compute minimum cuts
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        for j in range(i):
            if isPalin[j][i-1]:
                dp[i] = min(dp[i], dp[j] + 1)
    
    return dp[n] - 1  # cuts = partitions - 1
```

**Conceptual Notes**:
- 2D DP for range queries (palindromes)
- 1D DP for optimization (minimum cuts)
- Bottom-up on ranges, not elements
- Different from simple subsequence problems

---

## Problem 14: House Robber (Variant on Subsequence DP)

**Problem Statement**: 
Rob houses in a line to maximize value. Cannot rob adjacent houses.

**Conceptual Insight**:
- Similar to subset sum but with a constraint: no two adjacent elements
- State depends on including/excluding current element AND the constraint
- 1D DP sufficient with two choices per position

**State**: `dp[i]` = maximum value robbing up to house i

**Base Cases**:
- `dp[0] = houses[0]`
- `dp[1] = max(houses[0], houses[1])`

**Recurrence**:
```
dp[i] = max(dp[i-1],              # skip house i
            houses[i] + dp[i-2])   # rob house i, skip house i-1
```

**Implementation Pattern**:
```python
def house_robber(houses):
    if not houses:
        return 0
    if len(houses) == 1:
        return houses[0]
    
    dp = [0] * len(houses)
    dp[0] = houses[0]
    dp[1] = max(houses[0], houses[1])
    
    for i in range(2, len(houses)):
        dp[i] = max(dp[i-1], houses[i] + dp[i-2])
    
    return dp[-1]
```

**Conceptual Changes from Basic Subset Sum**:
1. Constraint: not two adjacent elements
2. State simplifies to 1D (position only)
3. Recurrence: depend on both i-1 and i-2
4. No explicit "include/exclude" logic; instead combine choices directly

---

## Summary Table: Conceptual and Implementation Changes

| Problem | Goal | Bounded? | State Dim | Recurrence Op | Loop Order | Key Changes |
|---------|------|----------|-----------|---------------|-----------|-------------|
| Subset Sum | Boolean (exists?) | 1 use | 2D (i, sum) | OR | row, col | Boolean decision |
| Count Subsets Sum | Count ways | 1 use | 2D (i, sum) | + (addition) | row, col | Integer counting |
| Partition Equal | Boolean (exists?) | 1 use | 1D (sum) | OR | derived from subset sum | Reduces to subset sum |
| Min Partition Diff | Minimize diff | 1 use | 2D (i, sum) | OR + post-process | row, col | Extract min from results |
| Target Sum | Count ways | 1 use | 1D (sum) | + (addition) | derived | Transform to count subsets |
| Coin Change Min | Minimize count | Unbounded | 1D (amount) | min() | amount, coin | ∞ base case, min() op |
| Coin Change Ways | Count ways | Unbounded | 1D (amount) | + (addition) | **coin, amount** | coin outer loop for combinations |
| 0/1 Knapsack | Maximize value | 1 use | 2D (i, cap) | max() | row, col | Two attributes (weight, value) |
| Unbounded Knapsack | Maximize value | Unbounded | 1D (cap) | max() | item, weight | Reuse allowed, 1D DP |
| Rod Cutting | Maximize price | Unbounded | 1D (len) | max() | length, cut | Similar to unbounded knapsack |
| Coin Change Max | Maximize count | Unbounded | 1D (amount) | max() | amount, coin | max() instead of min() |
| LIS Sum | Maximize sum | Order-dependent | 1D (pos) | max() with constraint | i, j (quadratic) | Preserve order, additional condition |
| Palindrome Parts | Minimize cuts | Range-based | 2D + 1D | min() | range length, position | Two-phase: ranges, then cuts |
| House Robber | Maximize value | Constraint (no adjacent) | 1D (pos) | max() | forward | Non-adjacent constraint |

---

## Key Insights

1. **0/1 vs. Unbounded**:
   - 0/1 (each element once): 2D DP, iterate element then constraint; or 1D DP with full rollback
   - Unbounded (each element reusable): 1D DP, inner loop order matters for combinations vs. permutations

2. **Boolean vs. Count vs. Optimize**:
   - Boolean: use OR, base = True/False
   - Count: use +, base = 1 or 0
   - Minimize/Maximize: use min/max, base = 0 or ∞

3. **Loop Order Matters**:
   - 0/1 Knapsack: item (outer), capacity (inner) → ensures each item used ≤1 time
   - Unbounded Knapsack: same structure, but inner loop updates current item
   - Coin Change Combinations: coin (outer), amount (inner) → counts unordered combinations
   - Coin Change Permutations: amount (outer), coin (inner) → counts ordered sequences

4. **Constraint Encoding**:
   - Many problems add constraints (weight ≤ capacity, no adjacent, order preservation) by modifying the recurrence
   - Base cases and loop bounds are critical

5. **Dimensionality Reduction**:
   - Many 2D problems reduce to 1D with appropriate loop order
   - 1D DP uses less memory and is often faster

---

## Template for New Problems

When facing a new DP subsequence problem:

1. **Identify the goal**: Boolean? Count? Optimize?
2. **Define state**: What parameters uniquely identify a subproblem?
3. **Set base cases**: What are trivial/boundary conditions?
4. **Write recurrence**: For current element, what are the options?
5. **Choose DP format**: 2D or 1D? Loop order?
6. **Implement and test**: Start with simple cases.

"""
