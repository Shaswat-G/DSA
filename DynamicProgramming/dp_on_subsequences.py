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


def count_subset_sums_memo(array: List[int], target: int) -> int:

    # Approach : Use recursion to generate all possible subsets and count susbets that sum to target.
    # Can optimize using memoization and then tabulation
    # What should be the state? state should be (Index, CurrentSum) to track current sum
    # (Index, CurrentSum) -> Counts of all subs that can be fromed with the first i elements that sum to CurrentSum

    # Edge Case:
    if not array or target < 0:
        return 0

    dp = {}

    def rec(index: int, current_sum: int) -> int:
        # Base Case:
        if index == len(array) and current_sum == target:
            return 1

        if index == len(array):
            return 0

        if current_sum > target:
            return 0

        if (index, current_sum) in dp:
            return dp[(index, current_sum)]

        # Recursive Case:
        # Include
        include = rec(index + 1, current_sum + array[index])

        # Exclude
        exclude = rec(index + 1, current_sum)

        dp[(index, current_sum)] = include + exclude

        return dp[(index, current_sum)]

    return rec(0, 0)


def count_subset_sums_tabulation(array: List[int], target: int) -> int:

    # State : (i, Target_Sum) : If we take the first i elements, how many subsets sum to target_sum?

    rows = len(array) + 1
    cols = sum(array) + 1

    dp = [[0 for _ in range(cols)] for _ in range(rows)]

    for row in range(rows):
        dp[row][0] = 1

    for row in range(1, rows):
        for col in range(1, cols):
            dp[row][col] += dp[row - 1][col]
            if col >=   array[row - 1]:
                dp[row][col] += dp[row - 1][col - array[row - 1]]

    return dp[len(array)][target]


if __name__ == "__main__":
    # Test array for counting subset sums (larger example)
    test_array = [2, 3, 5, 6, 8, 10, 12, 15, 18, 20]
    target_sum = 20

    # Function calls for counting subset sums (implementations to be written by you)
    result_count_memo = count_subset_sums_memo(test_array, target_sum)
    result_count_tab = count_subset_sums_tabulation(test_array, target_sum)

    print(f"Number of subsets with sum {target_sum} (memo): {result_count_memo}")
    print(f"Number of subsets with sum {target_sum} (tabulation): {result_count_tab}")


# One great realization is that filling the dp table uptill target will give you the possibilities for
# all possible subset sums from 0 to k included. (0 is always true).
# So if you run dp for target = sum(array) then you know all possible subset sums.
