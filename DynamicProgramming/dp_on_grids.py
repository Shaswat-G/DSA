from typing import List, Dict


# Problem 1: Count All Unique Paths in a Grid
# Given an m x n grid, count the number of unique ways to reach the bottom-right cell from the top-left cell.
# Movement is restricted to only right or down at each step.
# This is a classic combinatorial DP problem, foundational for understanding grid-based dynamic programming.


def count_unique_paths_memo(m: int, n: int) -> int:
    """
    Returns the number of unique paths from (0,0) to (m-1,n-1) in an m x n grid,
    moving only right or down.
    Uses recursion with memoization (top-down DP) to avoid redundant subproblem computation.
    Each cell (row, col) stores the number of unique ways to reach it from the origin.
    """

    def uniq_pths_from_origin(row, col, path_grid):
        # Base Case: If at the starting cell, there is exactly one way (do nothing).
        if row == 0 and col == 0:
            return 1

        # Out of bounds: No way to reach from outside the grid.
        if row < 0 or col < 0:
            return 0

        # If already computed, return cached value (memoization).
        if path_grid[row][col]:
            return path_grid[row][col]

        # Recursive Case:
        # The number of unique paths to (row, col) is the sum of unique paths
        # to the cell directly above (row-1, col) and the cell to the left (row, col-1).
        above_paths = uniq_pths_from_origin(row - 1, col, path_grid)
        left_paths = uniq_pths_from_origin(row, col - 1, path_grid)
        path_grid[row][col] = above_paths + left_paths

        return path_grid[row][col]

    path_grid = [[0 for _ in range(n)] for _ in range(m)]
    return uniq_pths_from_origin(m - 1, n - 1, path_grid)


# More efficient: Space-optimized Tabulation for Unique Paths
def count_unique_paths_tab_so(m: int, n: int) -> int:
    """
    Space-optimized tabulation (bottom-up DP) for unique paths in an m x n grid.
    Instead of a full 2D DP table, uses only O(n) space by keeping just the previous row.
    At each step, the number of ways to reach a cell depends only on the left and above cells.
    """
    prev = [1] * n
    for row in range(1, m):
        curr = [0] * n
        for col in range(n):
            left = curr[col - 1] if col > 0 else 0
            curr[col] = prev[col] + left
        prev = curr
    return prev[-1]


# Time Complexity (TC) for recursion is exponential: O(2^(m*n)).
# Memoization reduces TC to O(m*n) and space to O(m*n) for the DP grid, plus O(m+n) for the call stack.
# Tabulation (bottom-up) starts from (0,0) and fills the DP table iteratively.
# To convert memoization to tabulation: 1) Set base case, 2) Iterate over all states, 3) Apply recurrence relation.
# Space optimization: For each cell, only the previous row and current row are needed, so we can use two arrays (or one, with careful updates) for O(n) space.


def count_unique_paths_tabl(m: int, n: int) -> int:
    """
    Tabulation (bottom-up DP) for unique paths in an m x n grid.
    Fills a 2D DP table where each cell contains the number of unique ways to reach it from the origin.
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
    Space-optimized tabulation for unique paths in an m x n grid.
    Uses only two 1D arrays to keep track of the current and previous row, reducing space to O(n).
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


def count_paths_with_obstacles(grid: List[List[int]]) -> int:

    # Edge Case: Empty grid or no columns means no paths.
    if not grid or not grid[0]:
        return 0

    # Housekeeping: Get grid dimensions.
    rows = len(grid)
    cols = len(grid[0])

    # Recursive solution with memoization to avoid redundant recomputation.
    # For each cell (x, y), the number of unique paths is the sum of paths from above and left,
    # unless the cell is an obstacle (-1), in which case there are 0 paths.

    def rec_paths_from_origin_to(
        row: int, col: int, grid: List[List[int]], path_grid: List[List[int]]
    ) -> int:
        # Base Case: Start cell (0,0) has one way to reach it.
        if row == 0 and col == 0:
            return 1

        # Out of bounds: No way to reach from outside the grid.
        if row < 0 or col < 0:
            return 0

        # Obstacle cell: No way to pass through.
        if grid[row][col] == -1:
            return 0

        # Return cached value if already computed.
        if path_grid[row][col] != -1:
            return path_grid[row][col]

        # Recursive Case: Sum of paths from above and left, if not obstacles.
        above_paths = (
            rec_paths_from_origin_to(row - 1, col, grid, path_grid) if (row > 0) else 0
        )
        left_paths = (
            rec_paths_from_origin_to(row, col - 1, grid, path_grid) if (col > 0) else 0
        )
        path_grid[row][col] = above_paths + left_paths
        return path_grid[row][col]

    path_grid = [[-1 for _ in range(cols)] for _ in range(rows)]
    return rec_paths_from_origin_to(rows - 1, cols - 1, grid, path_grid)


# 3. Min Path Sum
def min_path_sum(grid: List[List[int]]) -> int:

    # Edge Case: Empty grid or no columns means no path exists.
    if not grid or not grid[0]:
        return 0

    # Housekeeping: Get grid dimensions.
    rows, cols = len(grid), len(grid[0])

    # Approach: Recursively try all possible paths from (0,0) to (rows-1, cols-1),
    # keeping track of the minimum sum. Memoization avoids recomputation of subproblems.

    def rec_path_sum_from_origin_to(
        row: int, col: int, grid: List[List[int]], min_cost_grid: List[List[int]]
    ) -> int:
        # Base Case: Out of bounds means an invalid path (infinite cost).
        if row < 0 or col < 0:
            return float("inf")

        # Return cached value if already computed.
        if min_cost_grid[row][col] != -1:
            return min_cost_grid[row][col]

        # Recursive Case: Minimum path sum to (row, col) is its value plus
        # the minimum of the path sums from above and from the left.
        above_path = (
            rec_path_sum_from_origin_to(row - 1, col, grid, min_cost_grid)
            if (row > 0)
            else float("inf")
        )
        left_path = (
            rec_path_sum_from_origin_to(row, col - 1, grid, min_cost_grid)
            if (col > 0)
            else float("inf")
        )
        min_cost_grid[row][col] = grid[row][col] + min(above_path, left_path)
        return min_cost_grid[row][col]

    min_cost_grid = [[-1 for _ in range(cols)] for _ in range(rows)]
    min_cost_grid[0][0] = grid[0][0]
    return rec_path_sum_from_origin_to(rows - 1, cols - 1, grid, min_cost_grid)


# More efficient: Tabulation (bottom-up DP) for Min Path Sum
def min_path_sum_tab(grid: List[List[int]]) -> int:
    """
    Tabulation (bottom-up DP) for minimum path sum in a grid.
    Fills a 2D DP table where each cell contains the minimum sum to reach that cell from the origin.
    """
    if not grid or not grid[0]:
        return 0
    rows, cols = len(grid), len(grid[0])
    dp = [[0] * cols for _ in range(rows)]
    for row in range(rows):
        for col in range(cols):
            if row == 0 and col == 0:
                dp[row][col] = grid[row][col]
            else:
                up = dp[row - 1][col] if row > 0 else float("inf")
                left = dp[row][col - 1] if col > 0 else float("inf")
                dp[row][col] = grid[row][col] + min(up, left)
    return dp[-1][-1]


# Space-optimized version for Min Path Sum
def min_path_sum_tab_so(grid: List[List[int]]) -> int:
    """
    Space-optimized tabulation for minimum path sum in a grid (O(n) space).
    Uses only two 1D arrays to keep track of the current and previous row, reducing space usage.
    """
    if not grid or not grid[0]:
        return 0
    rows, cols = len(grid), len(grid[0])
    prev = [float("inf")] * cols
    for row in range(rows):
        curr = [float("inf")] * cols
        for col in range(cols):
            if row == 0 and col == 0:
                curr[col] = grid[row][col]
            else:
                up = prev[col] if row > 0 else float("inf")
                left = curr[col - 1] if col > 0 else float("inf")
                curr[col] = grid[row][col] + min(up, left)
        prev = curr
    return prev[-1]


# 4. Max path sum with condition

# 5. Triangle


def min_path_sum_in_triangle_grid(grid: List[List[int]]) -> int:

    # Edge Case: Empty triangle or no rows means no path exists.
    if not grid or not grid[0]:
        return -1

    # Housekeeping: Number of rows in the triangle.
    rows = len(grid)
    # Each row i has i+1 columns (triangle structure).

    # Approach: Recursively try all possible paths from the top to the bottom row,
    # keeping track of the minimum sum. Memoization avoids recomputation of subproblems.

    def rec_path_sum_from_vertex_to(
        row: int, col: int, grid: List[List[int]], path_grid: List[List[int]]
    ) -> int:
        # Base Case: Out of bounds means an invalid path (infinite cost).
        if row < 0 or col < 0:
            return float("inf")

        # Return cached value if already computed.
        if path_grid[row][col] != -1:
            return path_grid[row][col]

        # Recursive Case: Minimum path sum to (row, col) is its value plus
        # the minimum of the path sums from above (same col) and above-left (col-1).
        above_path_cost = (
            rec_path_sum_from_vertex_to(row - 1, col, grid, path_grid)
            if (row > 0 and col < row)
            else float("inf")
        )
        diag_path_cost = (
            rec_path_sum_from_vertex_to(row - 1, col - 1, grid, path_grid)
            if (row > 0 and col > 0)
            else float("inf")
        )
        path_grid[row][col] = grid[row][col] + min(above_path_cost, diag_path_cost)
        return path_grid[row][col]

    path_grid = []
    for row in range(rows):
        path_grid.append([-1 for _ in range(row + 1)])
    path_grid[0][0] = grid[0][0]

    for i in range(len(path_grid[-1])):
        rec_path_sum_from_vertex_to(rows - 1, rows - 1 - i, grid, path_grid)
    return min(path_grid[-1])


# More efficient: Bottom-up Tabulation for Triangle Min Path Sum
def min_path_sum_in_triangle_grid_tab(grid: List[List[int]]) -> int:
    """
    Bottom-up tabulation for minimum path sum in a triangle grid.
    Uses a single 1D array (O(n) space) to iteratively compute the minimum path sum from bottom to top.
    At each step, dp[col] holds the minimum path sum to reach the bottom from (row, col).
    """
    if not grid or not grid[0]:
        return -1
    n = len(grid)
    dp = grid[-1][:]
    for row in range(n - 2, -1, -1):
        for col in range(row + 1):
            dp[col] = grid[row][col] + min(dp[col], dp[col + 1])
    return dp[0]


# 6. Maximum path sum from first row to last row (Recursive + Memoization)
def max_path_sum(grid: List[List[int]]) -> int:
    """
    Recursive + memoized solution for maximum path sum from any cell in the first row to any cell in the last row.
    At each step, you can move down, down-left, or down-right.
    """
    if not grid or not grid[0]:
        return 0
    rows, cols = len(grid), len(grid[0])

    def rec_max_path_sum_from_to(
        origin_col: int,
        row: int,
        col: int,
        grid: List[List[int]],
        max_dict: Dict[int, List[List[int]]],
    ) -> int:
        # Base Case: reached the origin cell in the first row
        if row == 0 and col == origin_col:
            return max_dict[origin_col][row][col]
        if row < 0 or col < 0 or col > cols - 1:
            return 0
        if max_dict[origin_col][row][col] != -1:
            return max_dict[origin_col][row][col]
        # Recursive Case: try all three possible moves from above
        above_path = (
            rec_max_path_sum_from_to(origin_col, row - 1, col, grid, max_dict)
            if row > 0
            else 0
        )
        left_diag_path = (
            rec_max_path_sum_from_to(origin_col, row - 1, col + 1, grid, max_dict)
            if (row > 0 and col < cols - 1)
            else 0
        )
        right_diag_path = (
            rec_max_path_sum_from_to(origin_col, row - 1, col - 1, grid, max_dict)
            if (row > 0 and col > 0)
            else 0
        )
        max_dict[origin_col][row][col] = grid[row][col] + max(
            above_path, left_diag_path, right_diag_path
        )
        return max_dict[origin_col][row][col]

    max_sum = 0
    max_dict = {}
    for origin_col in range(cols):
        max_dict[origin_col] = [[-1 for _ in range(cols)] for _ in range(rows)]
        max_dict[origin_col][0][origin_col] = grid[0][origin_col]
        for dest_col in range(cols):
            rec_max_path_sum_from_to(origin_col, rows - 1, dest_col, grid, max_dict)
        max_sum = max(max_sum, max(max_dict[origin_col][rows - 1]))
        del max_dict[origin_col]
    return max_sum


# 6b. Maximum path sum from first row to last row (Tabulation, Bottom-Up)
def max_path_sum_tab(grid: List[List[int]]) -> int:
    """
    Tabulation (bottom-up DP) solution for maximum path sum from any cell in the first row to any cell in the last row.
    At each step, you can move down, down-left, or down-right.
    """
    if not grid or not grid[0]:
        return 0
    rows, cols = len(grid), len(grid[0])
    # dp[row][col] = max path sum to (row, col)
    dp = [row[:] for row in grid]  # Copy grid for DP
    # Build up the DP table from the second row to the last
    for row in range(1, rows):
        for col in range(cols):
            up = dp[row - 1][col]
            left_diag = dp[row - 1][col - 1] if col > 0 else float("-inf")
            right_diag = dp[row - 1][col + 1] if col < cols - 1 else float("-inf")
            dp[row][col] += max(up, left_diag, right_diag)
    # The answer is the max value in the last row
    return max(dp[-1])


# 7. 3D state space DP with simultaneous agent tracking:


def cherry_pickup_ninja_friends(grid: List[List[int]]) -> int:
    # Edge Case:
    if not grid or not grid[0]:
        return 0

    # House Keeping:
    rows, cols = len(grid), len(grid[0])

    # Approach: If it were a simpler problem -> 1 agent, fixed origin, fixed destination -> recursive solution with overlapping subproblems -> optimized by memoization -> tabulation.
    # Add complexity: Multiple desitnations -> maximize across last row cells -> Find the max sum across maximum path sums of last row cells as destinations, fill dp grid only once.
    # Add complexity: 2 agents -> move simultaneously -> track both agents -> row will be the same, col can be different -> 3 parameter state representation -> (row, col1, col2)

    def rec_max_path_sum(
        row: int,
        col1: int,
        col2: int,
        directions: List[int],
        grid: List[List[int]],
        max_grid: Dict[int, List[List[int]]],
    ) -> int:
        # Base Case:
        # 1) Out of bounds
        if row < 0 or col1 < 0 or col1 >= cols or col2 < 0 or col2 >= cols:
            return float("-inf")

        # 2) If at the starting row (row 0), return the initial values
        if row == 0:
            if col1 == 0 and col2 == cols - 1:
                return grid[0][0] + grid[0][cols - 1]
            else:
                return float("-inf")  # Invalid starting position

        # 3) Check memoization
        if max_grid[row][col1][col2] != -1:
            return max_grid[row][col1][col2]

        # Recursive Case:
        max_from_above = float("-inf")
        for delta1 in directions:
            for delta2 in directions:
                max_from_above = max(
                    max_from_above,
                    rec_max_path_sum(
                        row - 1,
                        col1 + delta1,
                        col2 + delta2,
                        directions,
                        grid,
                        max_grid,
                    ),
                )

        # Add current cell values (avoid double counting if same position)
        if col1 == col2:
            max_grid[row][col1][col2] = grid[row][col1] + max_from_above
        else:
            max_grid[row][col1][col2] = (
                grid[row][col1] + grid[row][col2] + max_from_above
            )

        return max_grid[row][col1][col2]

    # Init max_sum DP grid -> 3D states: max_grid[row][col1][col2]
    directions = [-1, 0, 1]

    max_grid = {}
    for row in range(rows):
        max_grid[row] = [[-1 for _ in range(cols)] for _ in range(cols)]

    # We need to try ALL possible ending positions in the last row
    # and find the maximum among them
    max_cherries = 0
    for end_col1 in range(cols):
        for end_col2 in range(cols):
            cherries = rec_max_path_sum(
                rows - 1, end_col1, end_col2, directions, grid, max_grid
            )
            max_cherries = max(max_cherries, cherries)

    return max_cherries


def cherry_pickup_ninja_friends_tab(grid: List[List[int]]) -> int:
    # Edge Case:
    if not grid or not grid[0]:
        return 0

    # House Keeping:
    rows, cols = len(grid), len(grid[0])

    # Approach: Convert the recursive solution to tabulation (bottom-up DP)
    # Key insight: Fill the 3D DP table from row 0 to row (rows-1)
    # For each row, consider all possible (col1, col2) combinations

    # TODO: Initialize 3D DP table
    # dp[row][col1][col2] = max cherries from (0,0)+(0,cols-1) to (row,col1)+(row,col2)
    # Hint: Use a 3D array or dict structure similar to memoization version
    dp = {}
    for row in range(rows):
        dp[row] = [[float("-inf") for _ in range(cols)] for _ in range(cols)]

    # TODO: Base case - fill row 0
    # Only dp[0][0][cols-1] should have the initial value (grid[0][0] + grid[0][cols-1])
    # All other dp[0][col1][col2] combinations should be -infinity (invalid starting positions)
    dp[0][0][cols - 1] = grid[0][0] + grid[0][cols - 1]

    # TODO: Fill remaining rows using tabulation
    # For row = 1 to rows-1:
    #   For each col1 in range(cols):
    #     For each col2 in range(cols):
    #       Try all 9 combinations of previous moves (delta1, delta2 in [-1,0,1])
    #       dp[row][col1][col2] = current_cherries + max(dp[row-1][prev_col1][prev_col2])
    #       Remember: current_cherries = grid[row][col1] + grid[row][col2] if col1 != col2
    #                                 = grid[row][col1] if col1 == col2 (avoid double counting)

    directions = [-1, 0, 1]
    for row in range(1, rows, 1):  # because the starting position is fixed
        for col1 in range(cols):
            for col2 in range(cols):
                maxi = float("-inf")
                for delta1 in directions:
                    for delta2 in directions:
                        prev_col1 = col1 + delta1
                        prev_col2 = col2 + delta2
                        if (0 <= prev_col1 < cols) and (0 <= prev_col2 < cols):
                            maxi = max(maxi, dp[row - 1][prev_col1][prev_col2])
                if col1 == col2:
                    dp[row][col1][col2] = grid[row][col1] + maxi
                else:
                    dp[row][col1][col2] = grid[row][col1] + grid[row][col2] + maxi

    # TODO: Find the answer
    # Answer = max value among all dp[rows-1][col1][col2] for all valid col1, col2
    # This represents the maximum cherries for any ending position in the last row

    return max(dp[rows - 1][c1][c2] for c1 in range(cols) for c2 in range(cols))  # Replace with your implementation


if __name__ == "__main__":
    # Example: 3x3 grid
    m, n = 3, 3
    print(f"Unique paths in a {m}x{n} grid: {count_unique_paths_memo(m, n)}")
    print(f"Unique paths in a {m}x{n} grid: {count_unique_paths_tabl(m, n)}")
    print(f"Unique paths in a {m}x{n} grid: {count_unique_paths_tabl_with_so(m, n)}")
    print(
        f"Unique paths in a {m}x{n} grid: {count_paths_with_obstacles([[1,1,1],[1,-1,1],[1,1,1]])}"
    )

    min_path_grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    print(f"Min path sum in grid: {min_path_sum(min_path_grid)}")
    print(f"Max path sum in grid: {max_path_sum(min_path_grid)}")
    triangle_grid = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    print(
        f"Min path sum for Triangle grid: {min_path_sum_in_triangle_grid(triangle_grid)}"
    )

    # Cherry pickup example
    cherry_grid = [[3, 1, 1], [2, 5, 1], [1, 5, 5], [2, 1, 1]]
    print(
        f"Cherry pickup (Ninja and Friends) memoization: {cherry_pickup_ninja_friends(cherry_grid)}"
    )
    print(
        f"Cherry pickup (Ninja and Friends) tabulation: {cherry_pickup_ninja_friends_tab(cherry_grid)}"
    )

    # Another example with more cherries
    cherry_grid2 = [
        [1, 0, 0, 0, 0, 0, 1],
        [2, 0, 0, 0, 0, 3, 0],
        [2, 0, 9, 0, 0, 0, 0],
        [0, 3, 0, 5, 4, 0, 0],
        [1, 0, 2, 3, 0, 0, 6],
    ]
    print(f"Cherry pickup large grid: {cherry_pickup_ninja_friends(cherry_grid2)}")
