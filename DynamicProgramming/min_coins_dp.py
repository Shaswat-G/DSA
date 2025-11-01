from typing import List
from math import ceil


def min_coins_memo(coins: List[int], amount: int) -> int:
    # Edge Cases
    if amount == 0:
        return 0

    if not coins:
        return 0

    # Core Implementation
    # Overlapping Recursive Problems
    dp = {}

    def rec(index: int, current_sum: int) -> int:
        # Base Case
        if index == len(coins):
            if current_sum == amount:
                return 0
            return float("inf")

        if current_sum > amount:
            return float("inf")

        if (index, current_sum) in dp:
            return dp[(index, current_sum)]

        # Recursive Case
        include = 1 + rec(index, current_sum + coins[index])
        exclude = rec(index + 1, current_sum)
        dp[(index, current_sum)] = min(include, exclude)
        return dp[(index, current_sum)]

    return rec(0, 0)


def min_coins_tabl(coins: List[int], amount: int) -> int:

    # Edge Cases:
    if amount < 0:
        return -1
    if amount == 0:
        return 0
    if not coins:
        return 0

    # State : (index, sum) -> Min number of coins from the first "i" coins that total sum.
    rows = len(coins) + 1
    cols = amount + 1
    dp = [[float("inf") for col in range(cols)] for row in range(rows)]

    for row in range(rows):
        dp[row][0] = 0

    # Iterate over states starting from base case

    for row in range(1, rows):
        for col in range(1, cols):
            min_coins = min(dp[row - 1][col], 1 + dp[row][col - coins[row - 1]])
            dp[row][col] = min_coins

    return dp[len(coins)][amount]


if __name__ == "__main__":
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    amount = 487
    print(min_coins_memo(coins, amount))
    print(min_coins_tabl(coins, amount))

    # The greedy approach can work for some cases, but not always,
    # Use all possible combinations -> Recursion -> optimize from exponential to polynomial with memoization -> iteration -> space optimization.
    # State? Index, include a coin as many times as you want, track the current_sum as a parameter, and return min coins
    # Recursive Relation: Min_coins
    # return dp[(len(coins), amount)]
    
    
    # The learning is that in an unbounded case (as opposed to 0/1 case),
    # you model that by remaining in the same row! not the previous row!
