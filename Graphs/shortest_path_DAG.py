"""
Shortest Path in a Directed Acyclic Graph (DAG)

Problem Statement:
Given a weighted Directed Acyclic Graph (DAG) and a source vertex, find the shortest path from the source to all other vertices.

Intuition:
- A DAG does not contain cycles, so we can use topological sorting to process vertices in a linear order.
- By relaxing edges in topological order, we ensure that each vertex is processed only after all its dependencies have been processed.

Input:
- n: int - The number of vertices in the graph.
- edges: List[Tuple[int, int, int]] - A list of edges where each edge is represented as a tuple (u, v, w) indicating a directed edge from vertex u to vertex v with weight w.
- source: int - The source vertex.

Output:
- List[int] - A list where the i-th element represents the shortest distance from the source vertex to vertex i. If a vertex is unreachable, the distance is float('inf').

Example:
Input: n = 6, edges = [(0, 1, 2), (0, 2, 4), (1, 2, 1), (1, 3, 7), (2, 4, 3), (3, 5, 1), (4, 5, 5)]
       source = 0
Output: [0, 2, 3, 9, 6, 10]

Constraints:
- 1 <= n <= 10^5
- 0 <= len(edges) <= 2 * 10^5
- 0 <= source < n
"""

from typing import List, Tuple
from collections import defaultdict, deque


def shortest_path_dag(
    n: int, edges: List[Tuple[int, int, int]], source: int
) -> List[float]:
    """
    Find the shortest path from the source vertex to all other vertices in a weighted DAG.

    :param n: int - The number of vertices in the graph.
    :param edges: List[Tuple[int, int, int]] - The list of edges in the graph.
    :param source: int - The source vertex.
    :return: List[float] - The shortest distances from the source to all vertices.
    """
    # TODO: Step 1 - Construct the adjacency list representation of the graph
    # Create a dictionary where each vertex maps to a list of (neighbor, weight) pairs.
    adj_list = {node: [] for node in range(n)}

    for edge in edges:
        u, v, w = edge
        adj_list[u].append((v, w))

    # TODO: Step 2 - Perform topological sorting
    # Use Kahn's algorithm or DFS-based approach to find a valid topological order.
    stack = deque()
    visited = [False] * n

    def dfs_util(node):
        visited[node] = True
        for oe in adj_list[node]:
            nn, w = oe
            if not visited[nn]:
                dfs_util(nn)
        stack.append(node)

    for node in range(n):
        if not visited[node]:
            dfs_util(node)

    topo_order = [stack.pop() for _ in range(n)]

    # TODO: Step 3 - Initialize the distance array
    # Set the distance to the source vertex as 0 and all other vertices as float('inf').
    distances = [float("inf")] * n
    distances[source] = 0

    # TODO: Step 4 - Relax edges in topological order
    # For each vertex in topological order, update the distance of its neighbors.
    for node in topo_order:
        for oe in adj_list[node]:
            nn, w = oe
            distances[nn] = min(distances[nn], distances[node] + w)

    # TODO: Step 5 - Return the distance array
    return distances


# Example test cases
if __name__ == "__main__":
    # Test case 1: Simple DAG
    n1 = 6
    edges1 = [
        (0, 1, 2),
        (0, 2, 4),
        (1, 2, 1),
        (1, 3, 7),
        (2, 4, 3),
        (3, 5, 1),
        (4, 5, 5),
    ]
    source1 = 0
    print(
        "Test Case 1 - Expected: [0, 2, 3, 9, 6, 10], Got:",
        shortest_path_dag(n1, edges1, source1),
    )

    # Test case 2: Disconnected DAG
    n2 = 4
    edges2 = [(0, 1, 1), (2, 3, 2)]
    source2 = 0
    print(
        "Test Case 2 - Expected: [0, 1, inf, inf], Got:",
        shortest_path_dag(n2, edges2, source2),
    )

    # Test case 3: Single node
    n3 = 1
    edges3 = []
    source3 = 0
    print("Test Case 3 - Expected: [0], Got:", shortest_path_dag(n3, edges3, source3))

    # Test case 4: No edges
    n4 = 5
    edges4 = []
    source4 = 0
    print(
        "Test Case 4 - Expected: [0, inf, inf, inf, inf], Got:",
        shortest_path_dag(n4, edges4, source4),
    )
