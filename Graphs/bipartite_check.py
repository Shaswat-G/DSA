"""
Bipartite Graph Check

Problem Statement:
A graph is bipartite if it is possible to divide its set of vertices into two independent subsets such that no two vertices within the same subset are adjacent. Given an undirected graph, determine if it is bipartite.

Intuition:
- A graph is bipartite if we can color its vertices using two colors such that no two adjacent vertices share the same color.
- This can be achieved by performing a graph traversal (BFS or DFS) and attempting to color the graph.
- If we encounter a situation where two adjacent vertices have the same color, the graph is not bipartite.

Input:
- n: int - The number of vertices in the graph.
- edges: List[Tuple[int, int]] - A list of edges where each edge is represented as a tuple (u, v) indicating an undirected edge between vertex u and vertex v.

Output:
- bool - Return True if the graph is bipartite, otherwise return False.

Example:
Input: n = 4, edges = [(0, 1), (1, 2), (2, 3), (3, 0)]
Output: True

Input: n = 3, edges = [(0, 1), (1, 2), (2, 0)]
Output: False

Constraints:
- 1 <= n <= 10^5
- 0 <= len(edges) <= 2 * 10^5
"""

from typing import List, Tuple
from collections import deque


def is_bipartite_bfs(n: int, edges: List[Tuple[int, int]]) -> bool:
    """
    Check if the graph is bipartite using BFS.

    :param n: int - The number of vertices in the graph.
    :param edges: List[Tuple[int, int]] - The list of edges in the graph.
    :return: bool - True if the graph is bipartite, False otherwise.
    """

    # construct adj list
    adj_list = {node: [] for node in range(n)}
    for edge in edges:
        adj_list[edge[0]].append(edge[1])
        adj_list[edge[1]].append(edge[0])

    visited = [
        0 for _ in range(n)
    ]  # 0 : unvisited, -1 : visited and black, 1 : visited and white

    starting_node = 0
    q = deque([(starting_node, -1)])
    visited[0] = -1

    while q:
        cur_n, color = q.popleft()
        for nn in adj_list[cur_n]:
            if visited[nn] == 0:
                q.append((nn, -color))
                visited[nn] = -color
            elif visited[nn] == -color:
                pass
            else:
                return False

    return True


def is_bipartite_dfs(n: int, edges: List[Tuple[int, int]]) -> bool:
    """
    Check if the graph is bipartite using DFS.

    :param n: int - The number of vertices in the graph.
    :param edges: List[Tuple[int, int]] - The list of edges in the graph.
    :return: bool - True if the graph is bipartite, False otherwise.
    """
    pass


# Example test cases
if __name__ == "__main__":
    # Test case 1: Bipartite graph
    n1 = 4
    edges1 = [(0, 1), (1, 2), (2, 3), (3, 0)]
    print("Test Case 1 - Expected: True, Got:", is_bipartite_bfs(n1, edges1))
    # print("Test Case 1 - Expected: True, Got:", is_bipartite_dfs(n1, edges1))

    # Test case 2: Non-bipartite graph
    n2 = 3
    edges2 = [(0, 1), (1, 2), (2, 0)]
    print("Test Case 2 - Expected: False, Got:", is_bipartite_bfs(n2, edges2))
    # print("Test Case 2 - Expected: False, Got:", is_bipartite_dfs(n2, edges2))

    # Test case 3: Empty graph
    n3 = 0
    edges3 = []
    # print("Test Case 3 - Expected: True, Got:", is_bipartite_bfs(n3, edges3))
    # print("Test Case 3 - Expected: True, Got:", is_bipartite_dfs(n3, edges3))

    # Test case 4: Single node without edges
    n4 = 1
    edges4 = []
    print("Test Case 4 - Expected: True, Got:", is_bipartite_bfs(n4, edges4))
    # print("Test Case 4 - Expected: True, Got:", is_bipartite_dfs(n4, edges4))
