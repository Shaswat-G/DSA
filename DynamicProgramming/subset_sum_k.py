"""
Subset Sum Equals Target

Problem Statement:
Given an array `arr` of `n` integers and an integer `target`, determine if there is a subset of the given array with a sum equal to the given `target`.

You will implement three approaches (choose any or all when solving):
1. Simple recursion (exponential)
2. Memoization (top-down DP)
3. Tabulation (bottom-up DP) / bitset optimization

Do NOT implement these functions now — this is a template for you to fill in.

Examples:
- arr = [1, 2, 7, 3], target = 6 -> True  (subset 1+2+3)
- arr = [2, 3, 5], target = 6 -> False
- arr = [7, 54, 4, 12, 15, 5], target = 9 -> ??? (left for you to determine)

Constraints:
- 1 <= n <= 100
- -10^3 <= arr[i] <= 10^3 (note: negative values may require special handling)
- 0 <= target <= 10^4
"""

from typing import List


def subset_sum_recursive(arr: List[int], target: int) -> bool:
    """
    Determine if a subset sums to target using simple recursion.

    :param arr: List[int] - input array
    :param target: int - target sum
    :return: bool - True if a subset exists with sum == target, else False
    """

    # Edge Cases
    if not arr or target < 0:
        return False

    # Book keeping
    n = len(arr)

    def rec_helper(idx, cur_sum) -> bool:

        # Base case
        if idx == n:
            if cur_sum == target:
                return True
            return False

        if cur_sum > target:
            return False

        # Recursive Case
        if rec_helper(idx + 1, cur_sum + arr[idx]):
            return True

        if rec_helper(idx + 1, cur_sum):
            return True

        return False

    return rec_helper(0, 0)


def subset_sum_memo(arr: List[int], target: int) -> bool:
    """
    Determine if a subset sums to target using memoization (top-down DP).

    :param arr: List[int] - input array
    :param target: int - target sum
    :return: bool - True if a subset exists with sum == target, else False
    """

    # Edge Cases
    if target < 0:
        return False

    # Book keeping
    n = len(arr)

    # Quick answers
    if target == 0:
        return True
    if n == 0:
        return False

    # To keep memo small we clamp target to non-negative and reasonable value
    max_possible = sum(x for x in arr if x > 0)
    if target > max_possible:
        return False

    # Memo table: use -1 = unknown, 0 = False, 1 = True
    # dimensions: n x (target+1) for idx from 0..n-1 and cur_sum from 0..target
    memo = [[-1] * (target + 1) for _ in range(n)]

    def rec_helper(idx: int, cur_sum: int) -> bool:
        # if we've reached target
        if cur_sum == target:
            return True

        # if idx out of bounds or cur_sum exceeds target
        if idx >= n or cur_sum > target:
            return False

        if memo[idx][cur_sum] != -1:
            return bool(memo[idx][cur_sum])

        # choose current element
        take = False
        # only take if it doesn't immediately exceed target
        if cur_sum + arr[idx] <= target:
            take = rec_helper(idx + 1, cur_sum + arr[idx])

        # skip current element
        not_take = rec_helper(idx + 1, cur_sum)

        res = take or not_take
        memo[idx][cur_sum] = 1 if res else 0
        return res

    return rec_helper(0, 0)


def subset_sum_tabulation(arr: List[int], target: int) -> bool:
    """
    Determine if a subset sums to target using tabulation (bottom-up DP) or bitset optimization.

    :param arr: List[int] - input array
    :param target: int - target sum
    :return: bool - True if a subset exists with sum == target, else False
    """

    # Edge Cases

    if not (0 <= target <= sum(arr)):
        return False

    if target == 0:
        return True

    if not arr:
        return False

    # Book Keeping
    n = len(arr)

    # Init DP table of rows, cols = n, target+1
    dp = [[-1 for _ in range(target + 1)] for _ in range(n)]

    for idx in range(
        n
    ):  # Can construct a target of 0 by taking a null subset, valid for any index
        dp[idx][0] = 1

    for col in range(1, target + 1):
        dp[0][col] = 0

    if arr[0] <= target:
        dp[0][
            arr[0]
        ] = 1  # Can construct a target of arr[0] by taking the first 1 elements.

    # Iterate in topological order

    for row in range(1, n):
        for col in range(1, target + 1):

            include = False
            exclude = False

            if dp[row - 1][col] == 1:
                exclude = True

            if (col - arr[row] >= 0) and (dp[row - 1][col - arr[row]] == 1):
                include = True

            dp[row][col] = 1 if (include or exclude) else 0

    return True if dp[n - 1][target] == 1 else False


if __name__ == "__main__":
    # Test cases you can use while implementing — expected outputs are provided where obvious
    tests = [
        ("Example 1", [1, 2, 7, 3], 6, True),
        ("Example 2", [2, 3, 5], 6, False),
        ("Example 3", [7, 54, 4, 12, 15, 5], 9, False),
        ("Edge - empty", [], 0, True),
        ("Single equals", [5], 5, True),
        ("Single not equals", [5], 3, False),
        ("Zeros", [0, 0, 0], 0, True),
    ]

    for name, arr, target, expected in tests:
        print(f"{name}: arr={arr}, target={target}")
        print("  recursive ->", subset_sum_recursive(arr, target))
        print("  memo      ->", "Not run (template)")
        print("  tabulation->", subset_sum_tabulation(arr, target))
        print(f"  expected  -> {expected}\n")
