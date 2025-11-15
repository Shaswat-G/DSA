"""
Distance of Nearest Cell

Problem Statement:
Given a binary grid of size N*M, find the distance of the nearest 1 in the grid for each cell.

The distance is calculated as |i1 - i2| + |j1 - j2|, where i1, j1 are the row number and column number of the current cell, and i2, j2 are the row number and column number of the nearest cell having value 1.

Input:
- grid: List[List[int]] - A binary grid of size N*M where each cell contains either 0 or 1.

Output:
- List[List[int]] - A grid of the same size where each cell contains the distance to the nearest cell with value 1.

Example:
Input: grid = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[1,0,1],[0,1,0],[1,0,1]]

Constraints:
- 1 <= N, M <= 1000
- grid[i][j] is either 0 or 1.
"""

from typing import List
from collections import deque


def nearest_cell_distance(grid: List[List[int]]) -> List[List[int]]:
    """
    Find the distance of the nearest 1 in the grid for each cell.

    :param grid: List[List[int]] - The binary grid of size N*M.
    :return: List[List[int]] - A grid of the same size with distances to the nearest 1.
    """

    if not grid or not grid[0]:
        raise ValueError("Empty Grid")

    rows, cols = len(grid), len(grid[0])
    q = deque()
    visited = [[False for _ in range(cols)] for _ in range(rows)]

    # Init : First pass to get all the ones in the grid
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                q.append((r, c, 0))
                visited[r][c] = True
                grid[r][c] = 0

    # Multi-source BFS on all ones simultaneously

    while q:
        cr, cc, distance = q.popleft()
        for nr, nc in generate_valid_nn(cr, cc, grid):
            if not visited[nr][nc]:
                q.append((nr, nc, distance + 1))
                visited[nr][nc] = True
                grid[nr][nc] = distance + 1

    return grid


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


def is_valid_cell(row: int, col: int, matrix: List[List[int]]) -> bool:
    rows, cols = len(matrix), len(matrix[0])
    is_valid = (0 <= row < rows) and (0 <= col < cols)
    return is_valid


# Example test cases
if __name__ == "__main__":
    # Test case 1
    grid1 = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    print(
        "Test Case 1 - Expected: [[2, 1, 2], [1, 0, 1], [2, 1, 2]], Got:",
        nearest_cell_distance(grid1),
    )

    # Test case 2
    grid2 = [[1, 0, 0], [0, 0, 0], [0, 0, 1]]
    print(
        "Test Case 2 - Expected: [[0, 1, 2], [1, 2, 1], [2, 1, 0]], Got:",
        nearest_cell_distance(grid2),
    )

    # Test case 3
    grid3 = [[1]]
    print("Test Case 3 - Expected: [[0]], Got:", nearest_cell_distance(grid3))

    # Test case 4
    grid4 = [[0]]
    print("Test Case 4 - Expected: [[-1]], Got:", nearest_cell_distance(grid4))
