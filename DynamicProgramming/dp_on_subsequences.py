from typing import List


def subset_sum_exists(array, target):

    # Memoization for DP optimization
    memo = {}

    def rec(index: int, current_sum: int) -> bool:
        # Base Cases:
        if current_sum == target:
            return True

        if index == len(array) or current_sum > target:
            return False

        # Check memo
        if (index, current_sum) in memo:
            return memo[(index, current_sum)]

        # Recursive Cases:
        # Include current element
        include = rec(index + 1, current_sum + array[index])

        # Exclude current element
        exclude = rec(index + 1, current_sum)

        # Store result in memo
        memo[(index, current_sum)] = include or exclude
        return memo[(index, current_sum)]

    return rec(0, 0)


def subset_sum_exists_tabulation(array, target):
    """
    Tabulation (bottom-up DP) approach for subset sum.
    Returns True if a subset with sum == target exists, else False.
    """
    n = len(array)
    # TODO: Initialize a 2D DP table of size (n+1) x (target+1) with all False
    # dp[i][j] means: is it possible to get sum j using first i elements?
    dp = [[False] * (target + 1) for _ in range(n + 1)]

    # TODO: Base case - sum 0 is always possible (by picking nothing)
    for i in range(n + 1):
        dp[i][0] = True

    # TODO: Fill the DP table
    # For each element (1 to n)
    for i in range(1, n + 1):
        # For each possible sum (1 to target)
        for j in range(1, target + 1):
            # Exclude the current element: can we make sum j without array[i-1]?
            if dp[i - 1][j]:
                dp[i][j] = True
            # Include the current element: can we make sum j by including array[i-1]?
            elif j >= array[i - 1] and dp[i - 1][j - array[i - 1]]:
                dp[i][j] = True
            # Otherwise, dp[i][j] stays False

    # TODO: The answer is whether we can make 'target' using all n elements
    return dp[n][target]


if __name__ == "__main__":
    # Test array
    test_array = [3, 34, 4, 12, 5, 2]
    target_sum = 9
    result = subset_sum_exists(test_array, target_sum)
    print(f"Subset with sum {target_sum} exists: {result}")
