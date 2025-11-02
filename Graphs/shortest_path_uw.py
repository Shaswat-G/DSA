"""
Shortest Path in an Undirected Graph with Unit Weights

Problem Statement:
Given an undirected graph with unit weights, find the shortest path from a source vertex to all other vertices.

Intuition:
- Since all edges have the same weight (1), the shortest path can be determined using Breadth-First Search (BFS).
- BFS explores all vertices at the current distance before moving to the next level, ensuring the shortest path is found.

Input:
- n: int - The number of vertices in the graph.
- edges: List[Tuple[int, int]] - A list of edges where each edge is represented as a tuple (u, v) indicating an undirected edge between vertex u and vertex v.
- source: int - The source vertex.

Output:
- List[int] - A list where the i-th element represents the shortest distance from the source vertex to vertex i. If a vertex is unreachable, the distance is -1.

Example:
Input: n = 6, edges = [(0, 1), (0, 2), (1, 3), (2, 4), (3, 5)]
       source = 0
Output: [0, 1, 1, 2, 2, 3]

Constraints:
- 1 <= n <= 10^5
- 0 <= len(edges) <= 2 * 10^5
- 0 <= source < n
"""

from typing import List, Tuple
from collections import deque


def shortest_path_undirected_unit_weights(
    n: int, edges: List[Tuple[int, int]], source: int
) -> List[int]:
    """
    Find the shortest path from the source vertex to all other vertices in an undirected graph with unit weights.

    :param n: int - The number of vertices in the graph.
    :param edges: List[Tuple[int, int]] - The list of edges in the graph.
    :param source: int - The source vertex.
    :return: List[int] - The shortest distances from the source to all vertices.
    """
    # convert to adj_list
    adj_list = {node: [] for node in range(n)}
    for edge in edges:
        adj_list[edge[0]].append(edge[1])
        adj_list[edge[1]].append(edge[0])

    # Init
    distances = [-1] * n
    distances[source] = 0
    q = deque([(source, 0)])

    while q:
        cur_n, cur_dist = q.popleft()
        for nn in adj_list[cur_n]:
            if distances[nn] == -1:  # unvisited
                distances[nn] = cur_dist + 1
                q.append((nn, cur_dist + 1))

            else:  # visited but updating distance
                distances[nn] = min(distances[nn], cur_dist + 1)

    return distances


# Example test cases
if __name__ == "__main__":
    # Test case 1: Simple graph
    n1 = 6
    edges1 = [(0, 1), (0, 2), (1, 3), (2, 4), (3, 5)]
    source1 = 0
    print(
        "Test Case 1 - Expected: [0, 1, 1, 2, 2, 3], Got:",
        shortest_path_undirected_unit_weights(n1, edges1, source1),
    )

    # Test case 2: Disconnected graph
    n2 = 4
    edges2 = [(0, 1), (2, 3)]
    source2 = 0
    print(
        "Test Case 2 - Expected: [0, 1, -1, -1], Got:",
        shortest_path_undirected_unit_weights(n2, edges2, source2),
    )

    # Test case 3: Single node
    n3 = 1
    edges3 = []
    source3 = 0
    print(
        "Test Case 3 - Expected: [0], Got:",
        shortest_path_undirected_unit_weights(n3, edges3, source3),
    )

    # Test case 4: No edges
    n4 = 5
    edges4 = []
    source4 = 0
    print(
        "Test Case 4 - Expected: [0, -1, -1, -1, -1], Got:",
        shortest_path_undirected_unit_weights(n4, edges4, source4),
    )
