"""
Cycle Detection in an Undirected Graph

Problem Statement:
You are given an undirected graph represented as an adjacency list. Write a function to determine if the graph contains a cycle.

A cycle in an undirected graph is a path of edges and vertices wherein a vertex is reachable from itself. The graph does not need to be connected, and it may contain multiple components.

Input:
- n: int - The number of vertices in the graph (0-indexed).
- edges: List[Tuple[int, int]] - A list of edges where each edge is represented as a tuple (u, v) indicating an undirected edge between vertex u and vertex v.

Output:
- bool - Return True if the graph contains a cycle, otherwise return False.

Example:
Input: n = 5, edges = [(0, 1), (1, 2), (2, 0), (3, 4)]
Output: True

Explanation: The graph contains a cycle (0 -> 1 -> 2 -> 0).

Constraints:
- 1 <= n <= 10^4
- 0 <= len(edges) <= 2 * 10^4
- The graph does not contain self-loops or multiple edges between the same pair of vertices.
"""

from typing import List, Tuple
from collections import deque


def has_cycle_bfs(n: int, edges: List[Tuple[int, int]]) -> bool:
    """
    Determine if the undirected graph contains a cycle.

    :param n: int - The number of vertices in the graph.
    :param edges: List[Tuple[int, int]] - The list of edges in the graph.
    :return: bool - True if the graph contains a cycle, False otherwise.
    """

    # convert to adjacency list:
    adj_list = {vertex: [] for vertex in range(n)}

    for edge in edges:
        adj_list[edge[0]].append(edge[1])
        adj_list[edge[1]].append(edge[0])  # undirected graph

    visited = [False] * n

    # iterate over all connected components
    for v in range(n):
        if not visited[v]:
            # Perform a BFS for each componenet with parent tracking
            source_v = v
            q = deque([(source_v, -1)])
            visited[source_v] = True

            while q:
                cur_v, par_v = q.popleft()
                for nv in adj_list[cur_v]:
                    if nv != par_v:
                        if visited[nv]:  # detected cycle!
                            return True
                        else:
                            q.append((nv, cur_v))
                            visited[nv] = True

    return False


def has_cycle_dfs(n: int, edges: List[Tuple[int, int]]) -> bool:
    """
    Determine if the undirected graph contains a cycle.

    :param n: int - The number of vertices in the graph.
    :param edges: List[Tuple[int, int]] - The list of edges in the graph.
    :return: bool - True if the graph contains a cycle, False otherwise.
    """

    # convert to adjacency list:
    adj_list = {vertex: [] for vertex in range(n)}

    for edge in edges:
        adj_list[edge[0]].append(edge[1])
        adj_list[edge[1]].append(edge[0])  # undirected graph

    visited = [False] * n

    # DFS utils:
    def dfs_utils(source, parent):
        for nv in adj_list[source]:
            if nv == parent:
                pass
            else:
                if not visited[nv]:
                    visited[nv] = True
                    return dfs_utils(nv, source)
                else:
                    return True
        return False

    # iterate over all connected components
    for v in range(n):
        if not visited[v]:
            # perform a DFS with parent tracking
            visited[v] = True
            if dfs_utils(v, -1):
                return True

    return False


# Example test cases
if __name__ == "__main__":
    # Test case 1: Graph with a cycle
    n1 = 5
    edges1 = [(0, 1), (1, 2), (2, 0), (3, 4)]
    print("Test Case 1 - Expected: True, Got:", has_cycle_dfs(n1, edges1))

    # Test case 2: Graph without a cycle
    n2 = 4
    edges2 = [(0, 1), (1, 2), (2, 3)]
    print("Test Case 2 - Expected: False, Got:", has_cycle_dfs(n2, edges2))

    # Test case 3: Empty graph
    n3 = 0
    edges3 = []
    print("Test Case 3 - Expected: False, Got:", has_cycle_dfs(n3, edges3))

    # Test case 4: Single node without edges
    n4 = 1
    edges4 = []
    print("Test Case 4 - Expected: False, Got:", has_cycle_dfs(n4, edges4))
