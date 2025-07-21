from typing import List


# Problem 1: Count All Unique Paths in a Grid
# Given an m x n grid, count the number of unique ways to reach the bottom-right cell from the top-left cell.
# You can only move either right or down at any point in time.


def count_unique_paths_memo(m: int, n: int) -> int:
    """
    Returns the number of unique paths from (0,0) to (m-1,n-1) in an m x n grid,
    moving only right or down.
    """

    def uniq_pths_from_origin(row, col, path_grid):
        # Base Case:
        if row == 0 and col == 0:
            return 1

        if row < 0 or col < 0:
            return 0

        if path_grid[row][col]:
            return path_grid[row][col]

        # Rec Case:
        # Uniq paths to row, col = 1* uniq paths to row-1, col + 1* uniq paths from to row, col -1
        above_paths = uniq_pths_from_origin(row - 1, col, path_grid)
        left_paths = uniq_pths_from_origin(row, col - 1, path_grid)
        path_grid[row][col] = above_paths + left_paths

        return path_grid[row][col]

    path_grid = [[0 for _ in range(n)] for _ in range(m)]
    return uniq_pths_from_origin(m - 1, n - 1, path_grid)


# Initial TC was 2^(m*n) -> exponential
# New TC = O(n*M) for dp grid + O(m+n) for path length.
# Clearly recursion as well as space-optimized recursion (memoization) is top-down.
# But, can we do tabulation (bottom up?) we can start from 0,0 and go upwards?
# How to Convert Memoization to Tabulation? 1. Declare Base Case, 2. Express all states in iteration, 3. Perform recurrence.
# Now TC is O(N*M) since nested for loop and SC (N*M) for path grid. Can we space optimize?
# Notice that the for loop runs from left to right for each row from top to bottom. (book reading style).
# Notice that for every cell, we just need a value from its upward cell and leftward cell!
# we can store the previous row and the current row and replace them. TC: O(m*n) and TC O(n)


def count_unique_paths_tabl(m: int, n: int) -> int:
    """
    Returns the number of unique paths from (0,0) to (m-1,n-1) in an m x n grid,
    moving only right or down.
    """
    path_grid = [[0 for _ in range(n)] for _ in range(m)]

    for row in range(m):
        for col in range(n):
            if row == 0 and col == 0:
                path_grid[row][col] = 1
            else:
                path_grid[row][col] = path_grid[row - 1][col] + path_grid[row][col - 1]

    return path_grid


def count_unique_paths_tabl_with_so(m: int, n: int) -> int:
    """
    Returns the number of unique paths from (0,0) to (m-1,n-1) in an m x n grid,
    moving only right or down.
    """
    prev_row = [0 for _ in range(n)]

    for row in range(m):
        row_array = [0 for _ in range(n)]
        for col in range(n):
            if row == 0 and col == 0:
                row_array[col] = 1
            else:
                row_array[col] = prev_row[col] + row_array[col - 1]

        prev_row = row_array

    return prev_row[-1]


# 2. Count paths with obstacles

def count_paths_with_obstacles(grid : List[List[int]]) -> int:

    # Edge Cases:
    if not grid or not grid[0]:
        return 0

    # House-keeping:
    rows = len(grid)
    cols = len(grid[0])

    # Recursive Solution with memoization to avoid redundant recomputations.
    # Approach : Uniq paths to x,y = 1*uniq paths to x-1, y + 1* uniq_paths to x, y-1, except when the sources are obstacles.

    def rec_paths_from_origin_to(row : int, col : int, grid : List[List[int]], path_grid : List[List[int]]) -> int:
        # Base Case:
        if row == 0 and col == 0:
            return 1

        if row < 0 or col < 0:
            return 0
        
        if grid[row][col] == -1:
            return 0

        if path_grid[row][col] != -1:
            return path_grid[row][col]

        # Recursive Case:
        above_paths = rec_paths_from_origin_to(row-1,col, grid, path_grid) if (row > 0) else 0
        left_paths = rec_paths_from_origin_to(row,col-1, grid, path_grid) if (col > 0) else 0
        path_grid[row][col] = above_paths + left_paths
        return path_grid[row][col]

    path_grid = [[-1 for _ in range(cols)] for _ in range(rows)]
    return rec_paths_from_origin_to(rows-1, cols-1, grid, path_grid)

# 3. Min Path Sum

# 4. Max path sum with condition

# 5. Triangle

# 6. Multiple Start points


if __name__ == "__main__":
    # Example: 3x3 grid
    m, n = 3, 3
    print(f"Unique paths in a {m}x{n} grid: {count_unique_paths_memo(m, n)}")
    print(f"Unique paths in a {m}x{n} grid: {count_unique_paths_tabl(m, n)}")
    print(f"Unique paths in a {m}x{n} grid: {count_unique_paths_tabl_with_so(m, n)}")
    print(f"Unique paths in a {m}x{n} grid: {count_paths_with_obstacles([[1,1,1],[1,-1,1],[1,1,1]])}")
