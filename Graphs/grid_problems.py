from collections import deque
from typing import Tuple, List

def bfs_shortest_path(start, end, grid, obstacle_value = 100) -> Tuple[int, List[Tuple[int, int]]]:

    # We keep track of (row, col, distance) in queue.
    # We keep track of parents in a dictionary (row, col) : (parent_row, parent_col)
    # We use a set to keep track of visisted grid-squares (row, col)
    # We terminate as soon as we reach the end -> in this case we reconstrcuct the path backwards and return  dist, path_list.

    # 1. Handle Edge Cases: Invalid grid, start or end points. Start == End.

    rows, cols = len(grid), len(grid[0])
    start_row, start_col = start
    end_row, end_col = end

    if not grid or not grid[0]:
        return -1, []

    if not is_valid_gridsquare(start_row, start_col, grid, obstacle_value) or not is_valid_gridsquare(end_row, end_col, grid, obstacle_value):
        return -1, []

    if start == end:
        return 0, [start]

    # 2. BFS setups - valid directions, tracking visited, q, parent dictionary
    visited = set()
    parent = {}

    q = deque([(start_row, start_col, 0)])
    visited.add((start_row, start_col))
    parent[(start_row, start_col)] = None

    while q:
        cur_row, cur_col, dist = q.popleft()

        # Reached End -> reconstruct and return path
        if (cur_row, cur_col) == (end_row, end_col):
            path = []
            current = (cur_row, cur_col)
            while current:
                path.append(current)
                current = parent[current]

            return dist, path[::-1] # reverse path

        # Did not reach End
        for new_row, new_col in get_valid_neighbors(cur_row, cur_col, grid):
            if (new_row, new_col) not in visited:
                q.append((new_row, new_col, dist+1))
                visited.add((new_row, new_col))
                parent[(new_row, new_col)] = (cur_row, cur_col)

    return -1, [] # No path was found


def level_order_bfs(grid, start):
    rows, cols = len(grid), len(grid[0])

    visited = set()
    q = deque([start])
    visited.add(start)
    
    levels = []
    level = 0
    
    while q:
        level_size = len(q)
        current_level = []
        
        for _ in range(level_size):
            current = q.popleft()
            current_level.append(current)
            
            for nn in get_valid_neighbors(current[0], current[1], grid):
                if nn not in visited:
                    q.append(nn)
                    visited.add(nn)
                    
        levels.append((level, current_level))
        level+=1


# Neighbor generation helper functions

def get_valid_neighbors(row : int, col : int, grid : List[List[int]], include_diagonals : bool = False) -> List[Tuple[int,int]]:
    neighbors = []
    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    if include_diagonals:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1,1), (-1,1), (1,-1), (-1,-1)]
        
    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if is_valid_gridsquare(new_row, new_col, grid):
            neighbors.append((new_row, new_col))
        
    return neighbors

def is_valid_gridsquare(row : int, col : int, grid : List[List[int]], obstacle_value : int = 100) -> bool:
    rows, cols = len(grid), len(grid[0])
    is_valid = (0<= row < rows) and (0<= col < cols) and (grid[row][col]!=obstacle_value)
    
    return is_valid


def main():
    grid = [
        [1, 0, 1], 
        [1, 1, 0], 
        [0, 1, 1]
            ]

    print("4-way neighbors of (1,1):", get_valid_neighbors(1, 1, grid))
    print(
        "8-way neighbors of (1,1):",
        get_valid_neighbors(1, 1, grid, include_diagonals=True),
    )


if __name__ == "__main__":
    main()
