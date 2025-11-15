"""
Climbing Stairs Problem

Problem Statement:
Given a number of stairs, starting from the 0th stair, we need to climb to the Nth stair. At a time, we can climb either one or two steps. We need to return the total number of distinct ways to reach from the 0th to the Nth stair.

Approaches to Implement:
1. Recursion
2. Memoization
3. Tabulation

Example:
Input: N = 3
Output: 3
Explanation: There are three ways to climb to the 3rd stair:
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Constraints:
- 0 <= N <= 45
"""


def climb_stairs_recursive(n: int) -> int:
    """
    Solve the problem using recursion.

    :param n: int - The number of stairs.
    :return: int - The total number of distinct ways to climb to the Nth stair.
    """

    if n <= 1:
        return 1
    else:
        return climb_stairs_recursive(n - 2) + climb_stairs_recursive(n - 1)


def climb_stairs_memoization(n: int) -> int:
    """
    Solve the problem using memoization.

    :param n: int - The number of stairs.
    :return: int - The total number of distinct ways to climb to the Nth stair.
    """
    # TODO: Implement the memoization solution
    memo_table = [-1] * (n + 1)
    memo_table[0] = 1
    memo_table[1] = 1

    def rec_helper(n: int) -> int:
        if memo_table[n] == -1:
            memo_table[n] = rec_helper(n - 1) + rec_helper(n - 2)

        return memo_table[n]

    return rec_helper(n)


def climb_stairs_tabulation(n: int) -> int:
    """
    Solve the problem using tabulation.

    :param n: int - The number of stairs.
    :return: int - The total number of distinct ways to climb to the Nth stair.
    """

    if n <= 1:
        return 1

    prev2 = 0
    prev1 = 1

    for some_index in range(1, n):
        cur = prev2 + prev1
        prev2 = prev1
        prev1 = cur

    return cur


if __name__ == "__main__":
    n = int(input("Enter the number of stairs: "))
    print("Recursive Solution:", climb_stairs_recursive(n))
    print("Memoization Solution:", climb_stairs_memoization(n))
    print("Tabulation Solution:", climb_stairs_tabulation(n))
