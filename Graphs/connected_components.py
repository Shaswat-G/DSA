from typing import List
from collections import deque


def count_components(n: int, edges: List[List[int]]) -> int:

    # construct adjacency list
    adj_list = {i: [] for i in range(n)}

    for edge in edges:
        adj_list[edge[0]].append(edge[1])
        adj_list[edge[1]].append(edge[0])

    num_comps = 0
    visited = [False] * n

    for v in range(n):
        if not visited[v]:
            num_comps += 1

            # perform traversal (BFS)
            visited[v] = True
            q = deque([v])

            while q:
                u = q.popleft()

                for adj_u in adj_list[u]:
                    if not visited[adj_u]:
                        q.append(adj_u)
                        visited[adj_u] = True

    return num_comps


if __name__ == "__main__":
    # Test cases
    n1 = 5
    edges1 = [[0, 1], [1, 2], [3, 4]]
    print("Test Case 1:", count_components(n1, edges1))  # Expected: 2

    n2 = 6
    edges2 = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]]
    print("Test Case 2:", count_components(n2, edges2))  # Expected: 1

    n3 = 4
    edges3 = []
    print("Test Case 3:", count_components(n3, edges3))  # Expected: 4

    n4 = 7
    edges4 = [[0, 1], [2, 3], [4, 5], [5, 6]]
    print("Test Case 4:", count_components(n4, edges4))  # Expected: 4
