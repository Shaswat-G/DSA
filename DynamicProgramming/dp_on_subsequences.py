from typing import List


def subset_sum_exists(array: List[int], target: int) -> bool:

    # Approach : We can use recusion with paramters (index, current_sum) to track all possible subset sums and
    # check if a subset will actually sum to target. We can then optimize TC from exponential to polynomial with memoization

    # Edge Cases:
    if target == 0:
        return True

    if not array:
        return False

    dp = {}

    def rec(index: int, current_sum: int) -> bool:
        # Whether its possible to get a target if you're at index with current_sum.

        # Base Case:
        # 1. state out of bounds cases
        # 2. condition fulfilled case

        if current_sum == target:
            return True
        if index == len(array) or current_sum > target:
            return False
        if (index, current_sum) in dp:
            return dp[(index, current_sum)]

        # Recursive Case:
        include = rec(index + 1, current_sum + array[index])
        exclude = rec(index + 1, current_sum)
        dp[(index, current_sum)] = include or exclude
        return dp[(index, current_sum)]

    return rec(0, 0)


def subset_sum_exists_tabulation(array: List[int], target: int) -> bool:

    # What are our states? S = (Index, Sum) : Is it possible to generate Sum using the first Index elements (0-based)?
    n = len(array)
    dp = [[False for _ in range(target + 1)] for _ in range(n + 1)]

    # Base case: sum 0 is always possible (by picking nothing)
    for i in range(n + 1):
        dp[i][0] = True

    # Fill the DP table
    for i in range(1, n + 1):
        for j in range(1, target + 1):
            # Exclude the current element (don't pick array[i-1])
            if dp[i - 1][j]:
                dp[i][j] = True
            # Include the current element (pick array[i-1] if possible)
            elif j >= array[i - 1] and dp[i - 1][j - array[i - 1]]:
                dp[i][j] = True
    return dp[n][target]


if __name__ == "__main__":
    # Test array (changed for new test)
    test_array = [2, 7, 11, 15, 20]
    target_sum = 22
    result = subset_sum_exists(test_array, target_sum)
    result = subset_sum_exists_tabulation(test_array, target_sum)

    print(f"Subset with sum {target_sum} exists: {result}")
    
    
    
# One great realization is that filling the dp table uptill target will give you the possibilities for 
# all possible subset sums from 0 to k included. (0 is always true).
# So if you run dp for target = sum(array) then you know all possible subset sums.
