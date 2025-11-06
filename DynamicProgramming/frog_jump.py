"""
Frog Jump Problem

Problem Statement:
Given a number of stairs and a frog, the frog wants to climb from the 0th stair to the (N-1)th stair. At a time, the frog can climb either one or two steps. A `height[N]` array is also given.
The frog can jump from any step either one or two steps, provided it exists.
Whenever the frog jumps from a stair `i` to stair `j`, the energy consumed in the jump is `abs(height[i] - height[j])`, where `abs()` means the absolute difference.
We need to return the minimum energy that can be used by the frog to jump from stair 0 to stair N-1.

Approaches to Implement:
1. Recursion
2. Memoization
3. Tabulation

Example:
Input: N = 4, height = [10, 20, 30, 10]
Output: 20
Explanation: The frog can jump from 0 -> 1 -> 3 with a total energy cost of |10-20| + |20-10| = 10 + 10 = 20.

Constraints:
- 2 <= N <= 10^5
- 0 <= height[i] <= 10^4
"""


def frog_jump_recursive(n: int, height: list[int]) -> int:
    """
    Solve the problem using recursion.

    :param n: int - The number of stairs.
    :param height: list[int] - The heights of the stairs.
    :return: int - The minimum energy required to reach the (N-1)th stair.
    """
    # n is the number of stairs; target index is n-1
    if n <= 0:
        return 0
    if n == 1:
        # already at stair 0, no energy needed
        return 0
    if n == 2:
        # only one possible jump: 0 -> 1
        return abs(height[1] - height[0])

    # recursive solution: to reach index n-1 we can come from n-2 (one step)
    # or from n-3 (two steps)
    cost_from_one = frog_jump_recursive(n - 1, height) + abs(
        height[n - 1] - height[n - 2]
    )
    cost_from_two = frog_jump_recursive(n - 2, height) + abs(
        height[n - 1] - height[n - 3]
    )
    return min(cost_from_one, cost_from_two)


def frog_jump_memoization(n: int, height: list[int]) -> int:
    """
    Solve the problem using memoization.

    :param n: int - The number of stairs.
    :param height: list[int] - The heights of the stairs.
    :return: int - The minimum energy required to reach the (N-1)th stair.
    """
    if n <= 0:
        return 0

    energy = [-1] * n
    energy[0] = 0
    if n >= 2:
        energy[1] = abs(height[1] - height[0])

    def rec_helper(k: int) -> int:
        if energy[k] != -1:
            return energy[k]
        one = rec_helper(k - 1) + abs(height[k] - height[k - 1])
        two = float("inf")
        if k - 2 >= 0:
            two = rec_helper(k - 2) + abs(height[k] - height[k - 2])
        energy[k] = min(one, two)
        return energy[k]

    return rec_helper(n - 1)


def frog_jump_tabulation(n: int, height: list[int]) -> int:
    """
    Solve the problem using tabulation.

    :param n: int - The number of stairs.
    :param height: list[int] - The heights of the stairs.
    :return: int - The minimum energy required to reach the (N-1)th stair.
    """
    # TODO: Implement the tabulation solution
    pass


if __name__ == "__main__":
    # Test cases
    height = [10, 20, 30, 10]
    n = len(height)

    print("Recursive Solution:", frog_jump_recursive(n, height))
    print("Memoization Solution:", frog_jump_memoization(n, height))
    # print("Tabulation Solution:", frog_jump_tabulation(n, height))
