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
def min_path_sum(grid : List[List[int]]) -> int:

    # Edge Case:
    if not grid or not grid[0]:
        return 0

    # House Keeeping:
    rows, cols = len(grid), len(grid[0])

    # Approach : Recursively try all possible paths and keep track of the minimum.
    # Optimize for time by using memoization (avoiding recomputes)

    def rec_path_sum_from_origin_to(row: int, col: int, grid: List[List[int]], min_cost_grid : List[List[int]]) -> int:
        # Base Case:
        if row < 0 or col < 0:
            return float("inf")

        if min_cost_grid[row][col] != -1:
            return min_cost_grid[row][col]

        # Recursive Case:
        above_path = rec_path_sum_from_origin_to(row-1, col, grid, min_cost_grid) if (row>0) else float("inf")
        left_path = rec_path_sum_from_origin_to(row, col-1, grid, min_cost_grid) if (col>0) else float("inf")
        min_cost_grid[row][col] = grid[row][col] + min(above_path, left_path)
        return min_cost_grid[row][col]

    min_cost_grid = [[-1 for _ in range(cols)] for _ in range(rows)]
    min_cost_grid[0][0] = grid[0][0]
    return rec_path_sum_from_origin_to(rows - 1, cols - 1, grid, min_cost_grid)

# 4. Max path sum with condition

# 5. Triangle

def min_path_sum_in_triangle_grid(grid : List[List[int]]) -> int:

    # Edge Case:
    if not grid or not grid[0]:
        return -1

    # House Keeping
    rows = len(grid)
    # cols in the ith row (0-indexing) = i+1

    # Approach: Recursion to try out all possible paths and track minimum sum to bottom.
    # Memoization for optimizing time complexity from exponential to linear by avoiding recomputations.

    def rec_path_sum_from_vertex_to(row : int, col : int, grid : List[List[int]], path_grid: List[List[int]]) -> int:
        # Base Case
        if row < 0 or col <0:
            return float("inf")

        if path_grid[row][col] != -1:
            return path_grid[row][col]

        # Recursive Case
        above_path_cost = rec_path_sum_from_vertex_to(row-1,col,grid,path_grid) if (row > 0 and col<row) else float("inf")
        diag_path_cost = rec_path_sum_from_vertex_to(row-1,col-1,grid,path_grid) if (row > 0 and col>0) else float("inf")
        path_grid[row][col] = grid[row][col] + min(above_path_cost, diag_path_cost)
        return path_grid[row][col]

    path_grid = []
    for row in range(rows):
        path_grid.append([-1 for _ in range(row+1)])
    path_grid[0][0] = grid[0][0]

    rec_path_sum_from_vertex_to(rows - 1, rows - 1, grid, path_grid)
    return min(path_grid[-1])

# 6. Multiple Start points


if __name__ == "__main__":
    # Example: 3x3 grid
    m, n = 3, 3
    print(f"Unique paths in a {m}x{n} grid: {count_unique_paths_memo(m, n)}")
    print(f"Unique paths in a {m}x{n} grid: {count_unique_paths_tabl(m, n)}")
    print(f"Unique paths in a {m}x{n} grid: {count_unique_paths_tabl_with_so(m, n)}")
    print(f"Unique paths in a {m}x{n} grid: {count_paths_with_obstacles([[1,1,1],[1,-1,1],[1,1,1]])}")

    min_path_grid = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    print(f"Min path sum in grid: {min_path_sum(min_path_grid)}")
    triangle_grid = [
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]
    print(f"Min path sum for Triangle grid: {min_path_sum_in_triangle_grid(triangle_grid)}")
