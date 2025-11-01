from typing import List, Dict
from collections import defaultdict


# Understand that this is not count. In count we need to output 1 in the base case when index == len()
# since that represents a vlid path and things are summed and aggregated in upwards prop.
# However in summations, we are wondering whether from this state is there any future value addition.
def knapsack_01_memo(weights: List[int], values: List[int], capacity: int) -> int:
    if not weights or not values or capacity == 0:
        return 0

    dp = {}

    def rec(index: int, current_weight: int) -> int:
        if index == len(weights):
            return 0  # No more items to add, return accumulated value
        if current_weight > capacity:
            return 0  # Exceeded capacity, invalid path
        if (index, current_weight) in dp:
            return dp[(index, current_weight)]
        # Include current item if it doesn't exceed capacity
        include = 0
        if current_weight + weights[index] <= capacity:
            include = values[index] + rec(index + 1, current_weight + weights[index])
        exclude = rec(index + 1, current_weight)
        dp[(index, current_weight)] = max(include, exclude)
        return dp[(index, current_weight)]

    return rec(0, 0)


def knapsack_01_tabl(weights: List[int], values: List[int], capacity: int) -> int:
    rows = len(weights) + 1
    cols = capacity + 1
    dp = [[0 for _ in range(cols)] for _ in range(rows)]

    # dp[row][col]: max value using first 'row' items and capacity 'col'
    for row in range(1, rows):
        for col in range(1, cols):
            exclude = dp[row - 1][col]
            include = 0
            if weights[row - 1] <= col:
                include = values[row - 1] + dp[row - 1][col - weights[row - 1]]
            dp[row][col] = max(include, exclude)
    return dp[len(weights)][capacity]


if __name__ == "__main__":
    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 6]
    capacity = 5
    print(knapsack_01_memo(weights, values, capacity))
    values = [3, 4, 5, 6]
    capacity = 5
    print(knapsack_01_memo(weights, values, capacity))
    print(knapsack_01_tabl(weights, values, capacity))
