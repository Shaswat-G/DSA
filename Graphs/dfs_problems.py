# ---------------------------
# Connected Components / Island Problems
# ---------------------------
from collections import deque


def num_connected_components_dfs(graph):
    """
    Given an undirected graph (adjacency list), return the number of connected components using DFS.
    :param graph: Dict[int, List[int]]
    :return: int
    """

    def dfs(vertex, graph, visited):
        """Recursiveley visits unvisited neighbors of this vertex"""
        neighbors = graph[vertex]
        unvisited_neighbors = [neighbor for neighbor in neighbors if not visited[neighbor]]

        for unvisited_neighbor in unvisited_neighbors:
            visited[unvisited_neighbor] = True
            dfs(unvisited_neighbor, graph, visited)

    vertices = list(graph.keys())
    visited = {vertex: False for vertex in vertices}

    num_counts = 0

    for vertex in vertices:
        if not visited[vertex]:  # new component found
            num_counts += 1
            visited[vertex] = True
            dfs(vertex, graph, visited)

    return num_counts


def num_connected_components_bfs(graph):
    """
    Given an undirected graph (adjacency list), return the number of connected components using BFS.
    :param graph: Dict[int, List[int]]
    :return: int
    """

    # Multi-source bfs on unvisited vertices.
    vertices = list(graph.keys())
    visited = {vertex: False for vertex in vertices}

    num_counts = 0

    for vertex in vertices:
        if not visited[vertex]:
            num_counts += 1
            q = deque([vertex])
            visited[vertex] = True

            while q:
                cur_vertex = q.popleft()
                next_vertices = graph[cur_vertex]
                for next_vertex in next_vertices:
                    if not visited[next_vertex]:
                        visited[next_vertex] = True
                        q.append(next_vertex)

    return num_counts


def num_islands_dfs(grid):
    """
    Given a 2D grid of '1's (land) and '0's (water), return the number of islands using DFS.
    :param grid: List[List[str]]
    :return: int
    """

    def get_valid_cells(current_cell, grid, visited):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        valid_cells = []
        for direction in directions:
            new_cell = current_cell[0] + direction[0], current_cell[1] + direction[1]
            if (
                (0 <= new_cell[0] < len(grid))
                and (0 <= new_cell[1] < len(grid[0]))
                and (not visited[new_cell[0]][new_cell[1]])
                and (grid[new_cell[0]][new_cell[1]] == "1")
            ):
                valid_cells.append(new_cell)

        return valid_cells

    def dfs(current_cell, grid, visited):
        """Recursively visistes unvisited neighbors of current_cell"""
        unvisited_neighbors = get_valid_cells(current_cell, grid, visited)
        for unvisited_neighbor in unvisited_neighbors:
            visited[unvisited_neighbor[0]][unvisited_neighbor[1]] = True
            dfs(unvisited_neighbor, grid, visited)

    # ...implement DFS approach...
    rows, cols = len(grid) - 1, len(grid[0]) - 1
    visited = [[False for _ in range(cols + 1)] for _ in range(rows + 1)]
    num_islands = 0

    for row_idx, row in enumerate(grid):
        for col_idx, cell in enumerate(row):
            if cell == "0":
                pass
            else:
                if not visited[row_idx][col_idx]:
                    num_islands += 1
                    visited[row_idx][col_idx] = True
                    dfs((row_idx, col_idx), grid, visited)
                else:
                    pass

    return num_islands


def num_islands_bfs(grid):
    """
    Given a 2D grid of '1's (land) and '0's (water), return the number of islands using BFS.
    :param grid: List[List[str]]
    :return: int
    """

    # ...implement BFS approach...
    def get_valid_cells(current_cell, grid, visited):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        valid_cells = []
        for direction in directions:
            new_cell = current_cell[0] + direction[0], current_cell[1] + direction[1]
            if (
                (0 <= new_cell[0] < len(grid))
                and (0 <= new_cell[1] < len(grid[0]))
                and (not visited[new_cell[0]][new_cell[1]])
                and (grid[new_cell[0]][new_cell[1]] == "1")
            ):
                valid_cells.append(new_cell)

        return valid_cells

        # ...implement BFS approach...

    rows, cols = len(grid) - 1, len(grid[0]) - 1
    visited = [[False for _ in range(cols + 1)] for _ in range(rows + 1)]
    num_islands = 0

    for row_idx, row in enumerate(grid):
        for col_idx, cell in enumerate(row):
            current_cell = (row_idx, col_idx)
            if (grid[row_idx][col_idx] == "1") and (not visited[row_idx][col_idx]):
                num_islands += 1
                visited[row_idx][col_idx] = True
                q = deque([current_cell])

                while q:
                    this_cell = q.popleft()
                    for unvisited_neighbor in get_valid_cells(this_cell, grid, visited):
                        visited[unvisited_neighbor[0]][unvisited_neighbor[1]] = True
                        q.append(unvisited_neighbor)

    return num_islands


# ---------------------------
# Cycle Detection
# ---------------------------


def has_cycle_undirected(graph):
    """
    Detect cycle in an undirected graph using DFS.
    :param graph: Dict[int, List[int]]
    :return: bool
    """

    # ...implement cycle detection for undirected graph...
    def dfs(node, parent, visited):
        visited[node] = True
        for adj_node in graph[node]:
            if not visited[adj_node]:
                return dfs(adj_node, node, visited)
            else:
                if adj_node != parent:
                    return True
        return False

    vertices = list(graph.keys())
    visited = {vertex: False for vertex in vertices}

    for vertex in vertices:
        if not visited[vertex]:
            if dfs(vertex, -1, visited):
                return True

    return False


def has_cycle_directed(graph):
    """
    Detect cycle in a directed graph using DFS.
    :param graph: Dict[int, List[int]]
    :return: bool
    """
    # ...implement cycle detection for directed graph...
    pass


# ---------------------------
# Path Sum / Tree Problems
# ---------------------------


def has_path_sum(root, target_sum):
    """
    Given a binary tree root and a target sum, return True if the tree has a root-to-leaf path with the given sum.
    :param root: TreeNode
    :param target_sum: int
    :return: bool
    """

    if not root:
        return False

    if not root.left and not root.right:
        if root.val == target_sum:
            return True

    left_has_path = has_path_sum(root.left, target_sum - root.val)
    right_has_path = has_path_sum(root.right, target_sum - root.val)

    return left_has_path or right_has_path


def all_paths_sum(root, target_sum):
    """
    Given a binary tree root and a target sum, return all root-to-leaf paths where the sum equals target_sum.
    :param root: TreeNode
    :param target_sum: int
    :return: List[List[int]]
    """
    result = []

    def dfs(node, current_path, remaining_sum):
        if not node:
            return
        current_path.append(node.val)
        # If it's a leaf and the sum matches, add a copy of the path
        if not node.left and not node.right and node.val == remaining_sum:
            result.append(list(current_path))
        else:
            dfs(node.left, current_path, remaining_sum - node.val)
            dfs(node.right, current_path, remaining_sum - node.val)
        current_path.pop()

    dfs(root, [], target_sum)
    return result


# ---------------------------
# Helper Classes (Optional)
# ---------------------------


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ...add more helper functions/classes as needed...
def test():
    # Test for has_path_sum and all_paths_sum
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.left = TreeNode(5)
    root.right.right.right = TreeNode(1)
    target_sum = 22
    print("Has Path Sum:", has_path_sum(root, target_sum))  # Expected: True


def main():
    # Test for num_connected_components_dfs and num_connected_components_bfs
    graph = {0: [1], 1: [0, 2], 2: [1], 3: [4], 4: [3]}
    print(
        "Connected Components (DFS):", num_connected_components_dfs(graph)
    )  # Expected: 2
    print(
        "Connected Components (BFS):", num_connected_components_bfs(graph)
    )  # Expected: 2

    # Test for num_islands_dfs and num_islands_bfs
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    print("Number of Islands (DFS):", num_islands_dfs(grid))  # Expected: 3
    print("Number of Islands (BFS):", num_islands_bfs(grid))  # Expected: 3

    # Test for has_cycle_undirected
    cycle_graph = {0: [1], 1: [0, 2], 2: [1, 3], 3: [2, 0]}
    print(
        "Has Cycle (Undirected):", has_cycle_undirected(cycle_graph)
    )  # Expected: True

    # Test for has_cycle_directed
    directed_graph = {0: [1], 1: [2], 2: [0]}
    print("Has Cycle (Directed):", has_cycle_directed(directed_graph))  # Expected: True

    # Test for has_path_sum and all_paths_sum
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.left = TreeNode(5)
    root.right.right.right = TreeNode(1)
    target_sum = 22
    print("Has Path Sum:", has_path_sum(root, target_sum))  # Expected: True
    print(
        "All Paths Sum:", all_paths_sum(root, target_sum)
    )  # Expected: [[5,4,11,2],[5,8,4,5]]


if __name__ == "__main__":
    test()
