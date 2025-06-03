from collections import deque


class GridBFS:
    """
    Comprehensive class for different types of grid BFS problems.
    Each method demonstrates a common variation you'll encounter.
    """

    def __init__(self):
        self.directions_4 = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        self.directions_8 = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]

    def multi_source_bfs(self, grid, sources, target_value):
        """
        BFS from multiple starting points simultaneously.
        Common in: "Rotting Oranges", "01 Matrix", "Walls and Gates"

        Find minimum distance from any source to each cell.
        """
        if not grid or not grid[0]:
            return []

        rows, cols = len(grid), len(grid[0])
        distances = [[-1] * cols for _ in range(rows)]
        queue = deque()

        # Initialize queue with all sources
        for r, c in sources:
            if 0 <= r < rows and 0 <= c < cols:
                distances[r][c] = 0
                queue.append((r, c, 0))

        while queue:
            r, c, dist = queue.popleft()

            for dr, dc in self.directions_4:
                nr, nc = r + dr, c + dc

                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and distances[nr][nc] == -1  # Not visited
                    and grid[nr][nc] == target_value
                ):

                    distances[nr][nc] = dist + 1
                    queue.append((nr, nc, dist + 1))

        return distances

    def level_order_bfs(self, grid, start, obstacle_value=0):
        """
        Process BFS level by level (useful for counting steps/levels).
        Common in: Problems asking "minimum steps to reach all cells"
        """
        if not grid or not grid[0]:
            return []

        rows, cols = len(grid), len(grid[0])
        visited = set()
        queue = deque([start])
        visited.add(start)

        levels = []
        level = 0

        while queue:
            level_size = len(queue)
            current_level = []

            for _ in range(level_size):
                r, c = queue.popleft()
                current_level.append((r, c))

                for dr, dc in self.directions_4:
                    nr, nc = r + dr, c + dc

                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and (nr, nc) not in visited
                        and grid[nr][nc] != obstacle_value
                    ):

                        visited.add((nr, nc))
                        queue.append((nr, nc))

            levels.append((level, current_level))
            level += 1

        return levels

    def conditional_bfs(self, grid, start, end, condition_func):
        """
        BFS with custom conditions for movement.
        Common in: Problems with special movement rules

        Args:
            condition_func: Function that takes (current_cell, next_cell) and returns bool
        """
        if not grid or not grid[0]:
            return -1

        rows, cols = len(grid), len(grid[0])
        queue = deque([(start[0], start[1], 0)])
        visited = set([start])

        while queue:
            r, c, dist = queue.popleft()

            if (r, c) == end:
                return dist

            for dr, dc in self.directions_4:
                nr, nc = r + dr, c + dc

                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and (nr, nc) not in visited
                    and condition_func(grid[r][c], grid[nr][nc])
                ):

                    visited.add((nr, nc))
                    queue.append((nr, nc, dist + 1))

        return -1

    def bfs_with_state(self, grid, start, end, initial_state=None):
        """
        BFS where each node has additional state information.
        Common in: Problems with keys/doors, different movement modes, etc.

        State could be: collected keys, remaining jumps, current direction, etc.
        """
        if not grid or not grid[0]:
            return -1

        rows, cols = len(grid), len(grid[0])
        # visited now includes state: (row, col, state)
        visited = set()
        queue = deque([(start[0], start[1], 0, initial_state)])
        visited.add((start[0], start[1], initial_state))

        while queue:
            r, c, dist, state = queue.popleft()

            if (r, c) == end:
                return dist

            for dr, dc in self.directions_4:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    # Calculate new state based on the cell we're moving to
                    new_state = self._update_state(state, grid[nr][nc])

                    if (nr, nc, new_state) not in visited:
                        visited.add((nr, nc, new_state))
                        queue.append((nr, nc, dist + 1, new_state))

        return -1

    def _update_state(self, current_state, cell_value):
        """Helper method to update state based on cell value"""
        # This is problem-specific. Examples:
        # - Collecting keys: add key to collected set
        # - Jump count: decrement remaining jumps
        # - Direction tracking: update current direction
        return current_state

    def shortest_path_with_obstacles_elimination(
        self, grid, start, end, max_eliminations
    ):
        """
        BFS where you can eliminate up to k obstacles.
        State includes: (row, col, eliminations_used)

        Common in: "Shortest Path in a Grid with Obstacles Elimination"
        """
        if not grid or not grid[0]:
            return -1

        rows, cols = len(grid), len(grid[0])
        # State: (row, col, eliminations_used)
        visited = set()
        queue = deque([(start[0], start[1], 0, 0)])  # r, c, dist, eliminations
        visited.add((start[0], start[1], 0))

        while queue:
            r, c, dist, eliminations = queue.popleft()

            if (r, c) == end:
                return dist

            for dr, dc in self.directions_4:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    new_eliminations = eliminations

                    # If it's an obstacle
                    if grid[nr][nc] == 1:
                        if eliminations < max_eliminations:
                            new_eliminations = eliminations + 1
                        else:
                            continue  # Can't eliminate more obstacles

                    state_key = (nr, nc, new_eliminations)
                    if state_key not in visited:
                        visited.add(state_key)
                        queue.append((nr, nc, dist + 1, new_eliminations))

        return -1


# Example problems and their solutions
def rotting_oranges_example():
    """
    Example: Rotting Oranges problem using multi-source BFS
    """

    def oranges_rotting(grid):
        bfs = GridBFS()
        rows, cols = len(grid), len(grid[0])

        # Find all initially rotten oranges (sources)
        rotten_sources = []
        fresh_count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:  # Rotten
                    rotten_sources.append((r, c))
                elif grid[r][c] == 1:  # Fresh
                    fresh_count += 1

        if fresh_count == 0:
            return 0  # No fresh oranges

        # Multi-source BFS
        queue = deque([(r, c, 0) for r, c in rotten_sources])
        visited = set(rotten_sources)
        max_time = 0
        rotted_count = 0

        while queue:
            r, c, time = queue.popleft()
            max_time = max(max_time, time)

            for dr, dc in bfs.directions_4:
                nr, nc = r + dr, c + dc

                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and (nr, nc) not in visited
                    and grid[nr][nc] == 1
                ):

                    visited.add((nr, nc))
                    queue.append((nr, nc, time + 1))
                    rotted_count += 1

        return max_time if rotted_count == fresh_count else -1

    # Test case
    test_grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]

    result = oranges_rotting(test_grid)
    print(f"Rotting Oranges - Time to rot all: {result}")


def walls_and_gates_example():
    """
    Example: Walls and Gates using multi-source BFS
    """

    def walls_and_gates(rooms):
        bfs = GridBFS()
        INF = 2147483647

        # Find all gates (sources)
        gates = []
        for r in range(len(rooms)):
            for c in range(len(rooms[0])):
                if rooms[r][c] == 0:
                    gates.append((r, c))

        # Multi-source BFS from all gates
        queue = deque([(r, c, 0) for r, c in gates])

        while queue:
            r, c, dist = queue.popleft()

            for dr, dc in bfs.directions_4:
                nr, nc = r + dr, c + dc

                if (
                    0 <= nr < len(rooms)
                    and 0 <= nc < len(rooms[0])
                    and rooms[nr][nc] == INF
                ):  # Empty room not yet visited

                    rooms[nr][nc] = dist + 1
                    queue.append((nr, nc, dist + 1))

    # Test case
    INF = 2147483647
    test_rooms = [
        [INF, -1, 0, INF],
        [INF, INF, INF, -1],
        [INF, -1, INF, -1],
        [0, -1, INF, INF],
    ]

    walls_and_gates(test_rooms)
    print("Walls and Gates result:")
    for row in test_rooms:
        print(row)


if __name__ == "__main__":
    rotting_oranges_example()
    print()
    walls_and_gates_example()
