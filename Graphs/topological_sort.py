"""
Topological Sort

Problem Statement:
Given a directed acyclic graph (DAG), perform a topological sort of its vertices. A topological sort is a linear ordering of vertices such that for every directed edge (u, v), vertex u comes before vertex v in the ordering.

Intuition:
- Topological sorting is only possible for Directed Acyclic Graphs (DAGs).
- It can be achieved using:
  1. Depth-First Search (DFS) with a stack.
  2. Kahn's Algorithm (BFS-based approach using in-degrees).

Input:
- n: int - The number of vertices in the graph.
- edges: List[Tuple[int, int]] - A list of directed edges where each edge is represented as a tuple (u, v) indicating a directed edge from vertex u to vertex v.

Output:
- List[int] - A list representing the topological order of vertices. If the graph is not a DAG, return an empty list.

Example:
Input: n = 6, edges = [(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)]
Output: [5, 4, 2, 3, 1, 0]

Constraints:
- 1 <= n <= 10^5
- 0 <= len(edges) <= 2 * 10^5
"""

from typing import List, Tuple
from collections import deque


def topological_sort_dfs(n: int, edges: List[Tuple[int, int]]) -> List[int]:
    """
    Perform topological sort using DFS.

    :param n: int - The number of vertices in the graph.
    :param edges: List[Tuple[int, int]] - The list of directed edges in the graph.
    :return: List[int] - The topological order of vertices, or an empty list if the graph is not a DAG.
    """
    # TODO: Step 1 - Construct the adjacency list representation of the graph
    # Create a dictionary where each vertex maps to a list of its neighbors.
    # Example: {0: [1, 2], 1: [3], 2: [3], 3: []}
    adj_list = {node: [] for node in range(n)}
    for edge in edges:
        adj_list[edge[0]].append(edge[1])

    # TODO: Step 2 - Initialize a visited set and a stack
    # The visited set will keep track of nodes that have been processed.
    # The stack will store the topological order in reverse.
    visited = [False] * n
    stack = deque()

    # TODO: Step 3 - Define a recursive DFS function
    # The function should:
    # - Mark the current node as visited.
    # - Recursively visit all unvisited neighbors.
    # - Push the current node onto the stack after processing all its neighbors.
    def dfs_util(node: int):
        visited[node] = True
        for nn in adj_list[node]:
            if not visited[nn]:
                dfs_util(nn)
        stack.append(
            node
        )  # It is critical to add to the stack after all its dependencies are completed!
        return None

    # TODO: Step 4 - Perform DFS for all unvisited nodes
    # Iterate through all vertices and call the DFS function for unvisited nodes.
    for node in range(n):
        if not visited[node]:
            dfs_util(node)

    # TODO: Step 5 - Return the topological order
    # Reverse the stack to get the correct topological order.
    order = [stack.pop() for _ in range(n)]
    return order


def topological_sort_kahn(n: int, edges: List[Tuple[int, int]]) -> List[int]:
    """
    Perform topological sort using Kahn's Algorithm (BFS-based approach).

    :param n: int - The number of vertices in the graph.
    :param edges: List[Tuple[int, int]] - The list of directed edges in the graph.
    :return: List[int] - The topological order of vertices, or an empty list if the graph is not a DAG.
    """
    # TODO: Step 1 - Construct the adjacency list and calculate in-degrees
    # Create a dictionary where each vertex maps to a list of its neighbors.
    # Also, maintain an array to store the in-degree of each vertex.
    adj_list = {node: [] for node in range(n)}
    in_degree = [0] * n
    for edge in edges:
        adj_list[edge[0]].append(edge[1])
        in_degree[edge[1]] += 1

    # TODO: Step 2 - Initialize a queue with all vertices having in-degree 0
    # These vertices have no dependencies and can be processed first.
    q = deque()
    for node, in_deg in enumerate(in_degree):
        if in_deg == 0:
            q.append(node)

    # TODO: Step 3 - Perform BFS
    # While the queue is not empty:
    # - Remove a vertex from the queue and add it to the topological order.
    # - Decrease the in-degree of its neighbors.
    # - If any neighbor's in-degree becomes 0, add it to the queue.
    order = []

    while q:
        cur_n = q.popleft()
        order.append(cur_n)
        for nn in adj_list[cur_n]:
            in_degree[nn] -= 1
            if in_degree[nn] == 0:
                q.append(nn)

    # TODO: Step 4 - Check for cycles
    # If the topological order does not contain all vertices, the graph is not a DAG.
    if len(order) != n:
        return []

    # TODO: Step 5 - Return the topological order
    return order


# Example test cases
if __name__ == "__main__":
    # Test case 1: DAG
    n1 = 6
    edges1 = [(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)]
    print(
        "Test Case 1 - Expected: [5, 4, 2, 3, 1, 0], Got:",
        topological_sort_dfs(n1, edges1),
    )
    print(
        "Test Case 1 - Expected: [5, 4, 2, 3, 1, 0], Got:",
        topological_sort_kahn(n1, edges1),
    )

    # Test case 2: Graph with a cycle
    n2 = 3
    edges2 = [(0, 1), (1, 2), (2, 0)]
    print("Test Case 2 - Expected: [], Got:", topological_sort_dfs(n2, edges2))
    print("Test Case 2 - Expected: [], Got:", topological_sort_kahn(n2, edges2))

    # Test case 3: Empty graph
    n3 = 0
    edges3 = []
    print("Test Case 3 - Expected: [], Got:", topological_sort_dfs(n3, edges3))
    print("Test Case 3 - Expected: [], Got:", topological_sort_kahn(n3, edges3))

    # Test case 4: Single node without edges
    n4 = 1
    edges4 = []
    print("Test Case 4 - Expected: [0], Got:", topological_sort_dfs(n4, edges4))
    print("Test Case 4 - Expected: [0], Got:", topological_sort_kahn(n4, edges4))
