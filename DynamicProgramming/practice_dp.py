from typing import List, Tuple


def fibonacci_memo(n: int) -> int:
    # overlapping subproblems -> Memoization

    fib_map = {}

    def fib(n: int) -> int:
        # Base Case
        if n <= 1:
            return n

        # Recursive Case
        if n in fib_map:
            return fib_map[n]

        else:
            fib_map[n] = fib(n - 1) + fib(n - 2)
            return fib_map[n]

    return fib(n)


def fibonacci_tabl(n: int) -> int:
    # Iterative solution built from the base case upwards

    if n <= 1:
        return n

    first_prev = 1
    second_prev = 0
    for term_num in range(2, n + 1, 1):
        current_term = first_prev + second_prev
        second_prev = first_prev
        first_prev = current_term

    return current_term


def count_distinct_steps_to(n: int) -> int:
    # Clearly, this is a recursive problem. Why? count_distinct_steps_to(n) = 1*count_distinct_steps_to(n-2) + 1*count_distinct_steps_to(n-1)
    # => this is fibonacci
    return fibonacci_tabl(n)


### ---- General Pattern Learned ---- ###
# 1. Realize that there is a recursive strcucture to the problem -> write down the state and state transition possibilities.
# 2. Convinve yourself that this is not a greedy minimization problem -> If you need ALL possible ways -> Recursion
# 3. Write the recursive relation, perform the computation once and recurse.
# 4. Optimize with memoization or tabulation.


def frog_jump_min_energy(num_stairs: int, heights: List[int]) -> int:
    # Height[i-1] represents the heigt of the ith stair
    # Energy from i to j = abs_value(H[i-1] - H[j-1])
    # Frog can either jump 1 step or 2 steps
    # Find min possible energy.

    # Clearly this question asks for all possible solution -> use recursion and optimize with dp (memo/tabl).
    # We can also generalize this to k step jumps rather than just 2 steps.

    # Convert to direct indexing by H[0] = 0
    heights.insert(0, 0)

    # Base
    if num_stairs <= 1:
        return heights[num_stairs]

    # Recursive Case

    first_prev = heights[1]  # min energy to reach step 1 which is H[1] - H[0] = H[1]
    second_prev = heights[0]  # min energy to reach step 0 which is 0.
    for stair in range(2, num_stairs + 1, 1):

        # can convert the following in a for loop and track the minimum
        one_jump_energy = first_prev + abs(heights[stair] - heights[stair - 1])
        two_jump_energy = second_prev + abs(heights[stair] - heights[stair - 2])
        min_energy = min(one_jump_energy, two_jump_energy)
        second_prev = first_prev
        first_prev = min_energy

    return min_energy


def max_non_adj_sum(array: List[int]) -> int:

    # Base Cases
    if not array:
        return -1
    if len(array) == 1:
        return array[0]
    if len(array) == 2:
        return max(array[0], array[1])

    # Recursive Cases
    second_prev = array[0]
    first_prev = max(array[0], array[1])
    for index in range(2, len(array), 1):
        pick_cur_index = second_prev + array[index]
        not_pick_cur_index = first_prev
        max_sum_at_index = max(pick_cur_index, not_pick_cur_index)
        second_prev = first_prev
        first_prev = max_sum_at_index

    return max_sum_at_index


def ninja_training(grid: List[List[int]]) -> int:
    # Clearly, we need to evaluate all possible paths and select the maximum. Additionally, I can also return the training schedule :p
    # Makes me think of recursion on paramters -> Day and prev_activity (2D recursion)
    # Can optimize it with memoization -> 2D DP

    # Edge Cases:
    if not grid or not grid[0]:
        return 0

    # House Keeping
    days = len(grid)
    activities = len(grid[0])

    # Define recurisve function to return max training points given a day and previous activity:

    def rec_max_tp(day: int, prev_activity: int, tp: List[int]) -> int:
        # Base Case
        if day == len(grid):
            return 0

        # Memoization
        if tp[day][prev_activity] != -1:
            return tp[day][prev_activity]

        # Recursive Case
        max_tp = 0
        for activity in range(activities):
            if activity != prev_activity:
                points = grid[day][activity] + rec_max_tp(day + 1, activity, tp)
                max_tp = max(max_tp, points)

        tp[day][prev_activity] = max_tp
        return tp[day][prev_activity]

    # 2D Hash-map to deal with repeating recursive calls
    tp = [[-1 for _ in range(activities + 1)] for _ in range(days + 1)]
    max_tp = rec_max_tp(0, activities, tp)
    return max_tp


if __name__ == "__main__":
    # print(fibonacci_memo(10))  # 55
    # print(fibonacci_tabl(10))  # 55

    # print(frog_jump_min_energy(4, [10, 20, 30, 10]))
    # print(max_non_adj_sum([2, 4, 1, 9, 7, 3]))
    print(ninja_training([[10, 50, 1], [5, 100, 11], [20, 50, 10], [15, 35, 70]]))
