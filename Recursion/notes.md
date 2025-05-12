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

Happy recursing!
