"""
Minimum Effort Path

Problem Statement:
You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of the cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.

A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

Input:
- heights: List[List[int]] - A 2D array representing the heights of the grid cells.

Output:
- int - The minimum effort required to travel from the top-left to the bottom-right cell.

Examples:
Example 1:
Input:
heights = [[1,2,2],[3,8,2],[5,3,5]]
Output: 2
Explanation:
The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells. This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.

Example 2:
Input:
heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
Output: 0
Explanation:
The route of [1,1,1,1,1,1,1,1,1,1,1,1,1,1] has a maximum absolute difference of 0 in consecutive cells. This is better than the route of [1,1,1,1,1,1,2,1], where the maximum absolute difference is 1.

Constraints:
- rows == heights.length
- columns == heights[i].length
- 1 <= rows, columns <= 100
- 1 <= heights[i][j] <= 10^6
"""

from typing import List
from collections import deque
import heapq


def minimum_effort_path(heights: List[List[int]]) -> int:
    """
    Find the minimum effort required to travel from the top-left to the bottom-right cell.

    :param heights: List[List[int]] - The heights of the grid cells.
    :return: int - The minimum effort required.
    """

    # Filter Invalid Inputs
    if not heights or not heights[0]:
        raise ValueError("Empty Heights Input")

    # Book-keeping
    rows, cols = len(heights), len(heights[0])

    # Init effort
    effort = [[float("inf") for _ in range(cols)] for _ in range(rows)]
    effort[0][0] = 0
    priority_q = []
    heapq.heappush(priority_q, (0, (0, 0)))  # (effort, (row, col))

    while priority_q:
        cur_eff, cur_cell = heapq.heappop(priority_q)
        cr, cc = cur_cell

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = cr + dr, cc + dc
            if (0 <= nr < rows) and (0 <= nc < cols):
                delta_eff = abs(heights[nr][nc] - heights[cr][cc])
                new_eff = max(cur_eff, delta_eff)
                if max_eff < effort[nr][nc]:
                    effort[nr][nc] = new_eff
                    heapq.heappush(priority_q, (new_eff, (nr, nc)))

    return effort[rows - 1][cols - 1]


# Example test cases
if __name__ == "__main__":
    # Test case 1
    heights1 = [[1, 2, 2], [3, 8, 2], [5, 3, 5]]
    print("Test Case 1 - Expected: 2, Got:", minimum_effort_path(heights1))

    # Test case 2
    heights2 = [[1, 2, 1, 1, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 1, 1, 2, 1]]
    print("Test Case 2 - Expected: 0, Got:", minimum_effort_path(heights2))

    # Test case 3: Single cell
    heights3 = [[1]]
    print("Test Case 3 - Expected: 0, Got:", minimum_effort_path(heights3))

    # Test case 4: Flat grid
    heights4 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    print("Test Case 4 - Expected: 0, Got:", minimum_effort_path(heights4))
