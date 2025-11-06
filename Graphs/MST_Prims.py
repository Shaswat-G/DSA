"""
Prim's Algorithm for Minimum Spanning Tree (MST)

Problem Statement:
Given a connected, undirected graph with weights on its edges, find the Minimum Spanning Tree (MST). The MST is a subset of edges that connects all vertices with the minimum possible total edge weight and without forming any cycles.

Theory:
- Prim's algorithm is a greedy algorithm that builds the MST incrementally.
- It starts with an arbitrary vertex and grows the MST by adding the smallest edge that connects a vertex in the MST to a vertex outside the MST.
- The algorithm ensures that locally optimal decisions (choosing the smallest edge) lead to a globally optimal solution (the MST).

Key Points:
1. **Greedy Choice**: At each step, choose the smallest edge that connects the MST to a new vertex.
2. **Priority Queue**: A priority queue (min-heap) is used to efficiently fetch the smallest edge.
3. **Uniqueness**: If all edge weights are distinct, the MST is unique. Otherwise, multiple MSTs may exist.
4. **Time Complexity**: O((V + E) log V), where V is the number of vertices and E is the number of edges.
5. **Space Complexity**: O(V + E) for the adjacency list and priority queue.

Input:
- n: int - The number of vertices in the graph.
- edges: List[Tuple[int, int, int]] - A list of edges where each edge is represented as a tuple (u, v, w) indicating an undirected edge between vertex u and vertex v with weight w.

Output:
- Tuple[int, List[Tuple[int, int, int]]] - The total weight of the MST and the list of edges in the MST.

Example:
Input: n = 5, edges = [(0, 1, 2), (0, 3, 6), (1, 3, 8), (1, 2, 3), (1, 4, 5), (2, 4, 7)]
Output: (16, [(0, 1, 2), (0, 3, 6), (1, 2, 3), (1, 4, 5)])
Explanation: The MST includes edges (0, 1), (0, 3), (1, 2), and (1, 4) with a total weight of 16.

Constraints:
- 1 <= n <= 1000
- 0 <= len(edges) <= 10^5
- 0 <= u, v < n
- 1 <= w <= 10^6
"""

from typing import List, Tuple
import heapq
from random import randint


def prims_algorithm(
    n: int, edges: List[Tuple[int, int, int]]
) -> Tuple[int, List[Tuple[int, int, int]]]:
    """
    Find the total weight of the Minimum Spanning Tree (MST) and its edges using Prim's algorithm.

    :param n: int - The number of vertices in the graph.
    :param edges: List[Tuple[int, int, int]] - The list of edges in the graph.
    :return: Tuple[int, List[Tuple[int, int, int]]] - The total weight of the MST and the list of edges in the MST.
    """
    # TODO: Step 1 - Construct the adjacency list representation of the graph
    # Create a dictionary where each vertex maps to a list of (neighbor, weight) pairs.
    adj_list = {node: [] for node in range(n)}
    for edge in edges:
        u, v, w = edge
        adj_list[u].append((v, w))
        adj_list[v].append((u, w))  # undirected graph

    # TODO: Step 2 - Initialize the priority queue and visited set
    # Start with an arbitrary vertex (e.g., vertex 0) and add its edges to the priority queue.
    mst = []
    cost = 0
    pq = []
    starting_node = randint(0, n - 1)
    for edge in adj_list[starting_node]:
        nn, ew = edge
        heapq.heappush(pq, (ew, nn, starting_node))

    visited = [False] * n
    visited[starting_node] = True

    # TODO: Step 3 - Process the priority queue
    # While the priority queue is not empty, extract the smallest edge.
    # If the edge connects to an unvisited vertex, add it to the MST and update the total weight.
    while pq:
        candidate_edge = heapq.heappop(pq)
        ew, node, parent = candidate_edge
        if not visited[node]:
            mst.append((parent, node, ew))
            cost += ew
            for edge in adj_list[node]:
                nn, ew = edge
                if not visited[nn]:
                    heapq.heappush(pq, (ew, nn, node))

        visited[node] = True

    # TODO: Step 4 - Return the total weight of the MST and the list of edges
    return cost, mst


# Example test cases
if __name__ == "__main__":
    # Test case 1: Simple graph
    n1 = 5
    edges1 = [(0, 1, 2), (0, 3, 6), (1, 3, 8), (1, 2, 3), (1, 4, 5), (2, 4, 7)]
    mst_weight1, mst_edges1 = prims_algorithm(n1, edges1)
    print("Test Case 1 - Expected: 16, Got:", mst_weight1)
    print("MST Edges:", mst_edges1)

    # Test case 2: Single vertex
    n2 = 1
    edges2 = []
    mst_weight2, mst_edges2 = prims_algorithm(n2, edges2)
    print("Test Case 2 - Expected: 0, Got:", mst_weight2)
    print("MST Edges:", mst_edges2)

    # Test case 3: Disconnected graph (invalid input for MST)
    n3 = 4
    edges3 = [(0, 1, 1), (2, 3, 2)]
    mst_weight3, mst_edges3 = prims_algorithm(n3, edges3)
    print("Test Case 3 - Expected: Error or invalid, Got:", mst_weight3)
    print("MST Edges:", mst_edges3)

    # Test case 4: Large graph
    n4 = 6
    edges4 = [
        (0, 1, 1),
        (0, 2, 2),
        (1, 2, 2),
        (1, 3, 3),
        (2, 4, 4),
        (3, 4, 5),
        (3, 5, 6),
    ]
    mst_weight4, mst_edges4 = prims_algorithm(n4, edges4)
    print("Test Case 4 - Expected: 15, Got:", mst_weight4)
    print("MST Edges:", mst_edges4)
