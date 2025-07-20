When we have overlapping subproblems, we can use memoization to store the results of subproblems to avoid redundant calculations. This is particularly useful in dynamic programming.
Store the value in a table or dictionary after computing it for the first time, and check this table before performing the computation again.


### What is Memoization?
Memoization is a technique used to optimize recursive algos by storing the results of intermediate computations. It avoids the need to recompute results for the same inputs, thus improving efficiency.

### What is tabulation?
Tabulation is a bottom-up approach to dynamic programming where we solve smaller subproblems first and use their results to build up solutions to larger problems. It typically involves filling up a table iteratively.
This is different from memoization, which is a top-down approach that uses recursion and stores results in a cache.


For 1D DP, the first step is to convert the problem into an index with a recursive relation. Then, we can use either memoization (for time complexity) or tabulation (for space complexity) to solve it. In other words, **define what the state is and how to transition between states.**


