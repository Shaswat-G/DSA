from typing import List
from collections import deque


def count_connected_components_in_matrix(matrix: List[List[int]]) -> int:
    # TODO: Implement the function to count connected components in a matrix

    if not matrix or not matrix[0]:
        raise ValueError("Matrix is Empty")

    # book-keeping:
    rows, cols = len(matrix), len(matrix[0])

    # visited matrix:
    visited = [[False for _ in range(cols)] for _ in range(rows)]

    num_comps = 0
    for r, row in enumerate(matrix):
        for c, cell_value in enumerate(row):
            if cell_value == 1 and not visited[r][c]:
                # Implement traversal
                q = deque([(r, c)])
                visited[r][c] = True

                while q:
                    cr, cc = q.popleft()
                    for nr, nc in generate_valid_nn(cr, cc, matrix):
                        if not visited[nr][nc]:
                            q.append((nr, nc))
                            visited[nr][nc] = True

                num_comps += 1

    return num_comps


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
    matrix1 = [[1, 1, 0, 0], [1, 0, 0, 1], [0, 0, 1, 1], [0, 1, 1, 0]]

    print("Test Case 1:", count_connected_components_in_matrix(matrix1))  # Expected: 2

    matrix2 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

    print("Test Case 2:", count_connected_components_in_matrix(matrix2))  # Expected: 3

    matrix3 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    print("Test Case 3:", count_connected_components_in_matrix(matrix3))  # Expected: 0

    matrix4 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    print("Test Case 4:", count_connected_components_in_matrix(matrix4))  # Expected: 1
