"""
Rat in a Maze Problem

Problem Statement:
Given a grid of dimensions n x n. A rat is placed at coordinates (0, 0) and wants to reach coordinates (n-1, n-1). Find all possible paths that the rat can take to travel from (0, 0) to (n-1, n-1). The directions in which the rat can move are 'U' (up), 'D' (down), 'L' (left), 'R' (right).

The value 0 in the grid denotes that the cell is blocked and the rat cannot use that cell for travelling, whereas value 1 represents that the rat can travel through the cell. If the cell (0, 0) has a value of 0, then the rat cannot move to any other cell.

Constraints:
- 2 <= n <= 10
- grid[i][j] is either 0 or 1

Example:
Input: n = 4, grid = [[1, 0, 0, 0], [1, 1, 0, 1], [0, 1, 0, 0], [1, 1, 1, 1]]
Output: ["DDRDRR", "DRDDRR"]
Explanation: The rat can take two paths to reach the destination.
"""

from typing import List


def find_paths(grid: List[List[int]]) -> List[str]:
    """
    Find all possible paths for the rat to travel from (0, 0) to (n-1, n-1).

    :param grid: List[List[int]] - The input grid where 0 represents blocked cells and 1 represents open cells.
    :return: List[str] - A list of all possible paths represented as strings of directions.
    """

    if not grid:
        raise ValueError("Empty List")

    n = len(grid)
    directions = {"D": (1, 0), "R": (0, 1)}

    def valid_next_cells(cell):
        valid_cells = []

        cr, cc = cell
        for d in directions.keys():
            dr, dc = directions[d]
            nr, nc = cr + dr, cc + dc
            if (nr < n) and (nc < n) and not (grid[nr][nc] == 0):
                valid_cells.append((nr, nc, d))

        return valid_cells

    # Seems like a DFS problem with path collection

    policies = []

    def rec_helper(cell, path, actions):

        # Base Case
        if cell == (n - 1, n - 1):
            policies.append("".join(actions.copy()))
            return None

        # Recurse and Backtrack over possible states
        for r, c, d in valid_next_cells(cell):
            # it should not be a visited cell
            next_cell = (r, c)
            if next_cell in path:
                continue

            actions.append(d)
            path.add(next_cell)
            rec_helper(next_cell, path, actions)

            actions.pop()
            path.remove(next_cell)

        return None

    rec_helper((0, 0), set([]), [])
    return policies


if __name__ == "__main__":
    # Test cases
    grid1 = [[1, 0, 0, 0], [1, 1, 0, 1], [0, 1, 0, 0], [1, 1, 1, 1]]
    print("Test Case 1:", find_paths(grid1))

    grid2 = [[1, 0], [1, 1]]
    print("Test Case 2:", find_paths(grid2))

    grid3 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    print("Test Case 3:", find_paths(grid3))
