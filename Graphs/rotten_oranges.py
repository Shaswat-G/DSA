"""
Problem Statement: Rotten Oranges

You are given an m x n grid where each cell can have one of three values:
- 0 representing an empty cell,
- 1 representing a fresh orange, or
- 2 representing a rotten orange.

Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

Constraints:
1. m == grid.length
2. n == grid[i].length
3. 1 <= m, n <= 10
4. grid[i][j] is 0, 1, or 2

Example:
Input: grid = [
    [2, 1, 1],
    [1, 1, 0],
    [0, 1, 1]
]
Output: 4

Input: grid = [
    [2, 1, 1],
    [0, 1, 1],
    [1, 0, 1]
]
Output: -1

Input: grid = [
    [0, 2]
]
Output: 0
"""

from typing import List
from collections import deque


def oranges_rotting(grid: List[List[int]]) -> int:
    # TODO: Implement the function to calculate the minimum time to rot all oranges

    if not grid or not grid[0]:
        raise ValueError("Empty Grid")

    rows, cols = len(grid), len(grid[0])

    # Init: First pass to get locations of rotten oranges and total fresh oranges at t=0
    orange_count = 0
    rotten_oranges = deque()

    for r, row in enumerate(grid):
        for c, cell_value in enumerate(row):
            if cell_value == 1:
                orange_count += 1
            elif cell_value == 2:
                rotten_oranges.append((r, c, 0))
                orange_count += 1
            else:
                pass

    max_time = 0
    num_rotten = 0
    while rotten_oranges:
        cr, cc, t = rotten_oranges.popleft()
        num_rotten += 1
        max_time = max(max_time, t)
        for nr, nc in generate_valid_nn(
            cr, cc, grid
        ):  # iterate over all neighboring fresh oranges
            rotten_oranges.append((nr, nc, t + 1))
            grid[nr][nc] = 2

    if num_rotten == orange_count:
        return max_time

    return -1


def generate_valid_nn(
    row: int, col: int, matrix: List[List[int]], diagonals_allowed: bool = False
) -> List[tuple[int, int]]:
    # ensure that this function is only called from a valid cell.

    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    if diagonals_allowed:
        directions.extend([(1, 1), (-1, -1), (-1, 1), (1, -1)])

    nn = []
    for dr, dc in directions:
        nr, nc = row + dr, col + dc
        if is_valid_cell(nr, nc, matrix):
            nn.append((nr, nc))

    return nn


def is_valid_cell(
    row: int, col: int, matrix: List[List[int]], land_value: int = 1
) -> bool:
    rows, cols = len(matrix), len(matrix[0])
    is_valid = (
        (0 <= row < rows) and (0 <= col < cols) and (matrix[row][col] == land_value)
    )
    return is_valid


if __name__ == "__main__":
    # Test cases
    grid1 = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    print("Test Case 1:", oranges_rotting(grid1))  # Expected: 4

    grid2 = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
    print("Test Case 2:", oranges_rotting(grid2))  # Expected: -1

    grid3 = [[0, 2]]
    print("Test Case 3:", oranges_rotting(grid3))  # Expected: 0

    grid4 = [[0]]
    print("Test Case 4:", oranges_rotting(grid4))  # Expected: 0
