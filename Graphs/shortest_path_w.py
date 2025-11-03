"""
Shortest Path in a Weighted Graph (Dijkstra's Algorithm)

Problem Statement:
Given a weighted graph and a source vertex, find the shortest path from the source to all other vertices.

Intuition:
- Dijkstra's algorithm uses a priority queue to greedily select the vertex with the smallest known distance.
- It relaxes the edges of the selected vertex, updating the shortest distances to its neighbors.
- This process continues until all vertices are processed or the priority queue is empty.

Input:
- n: int - The number of vertices in the graph.
- edges: List[Tuple[int, int, int]] - A list of edges where each edge is represented as a tuple (u, v, w) indicating an edge from vertex u to vertex v with weight w.
- source: int - The source vertex.

Output:
- List[float] - A list where the i-th element represents the shortest distance from the source vertex to vertex i. If a vertex is unreachable, the distance is float('inf').

Example:
Input: n = 5, edges = [(0, 1, 2), (0, 2, 4), (1, 2, 1), (1, 3, 7), (2, 4, 3), (3, 4, 1)]
       source = 0
Output: [0, 2, 3, 9, 6]

Constraints:
- 1 <= n <= 10^5
- 0 <= len(edges) <= 2 * 10^5
- 0 <= source < n

Detailed Explanation:
Use heapq as a min-heap of (priority, item) tuples. Push with heapq.heappush(heap, (priority, item)) and pop the smallest with heapq.heappop(heap). In Dijkstra you store (distance, vertex), ignore stale entries when popped, and relax neighbors.

Key points

Use tuples (distance, vertex) so the heap orders by distance.
When you pop (dist, u) and dist > distances[u], it's a stale entry — skip it.
Dijkstra requires non-negative weights.

Time complexity:
O((V+E)logV).
Gotchas

Do not try to remove arbitrary items from heapq — instead push a new entry and skip stale ones.
If your graph is undirected, add both (u->v) and (v->u) edges.
Ties in distance are broken by the second tuple element (vertex id).
"""

from typing import List, Tuple
import heapq


def dijkstra(n: int, edges: List[Tuple[int, int, int]], source: int) -> List[float]:
    """
    Find the shortest path from the source vertex to all other vertices in a weighted graph.

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
        adj_list[v].append((u, w))  # for undirected graph

    # TODO: Step 2 - Initialize the distance array and priority queue
    # Set the distance to the source vertex as 0 and all other vertices as float('inf').
    # Add the source vertex to the priority queue with distance 0.
    distances = [float("inf")] * n
    distances[source] = 0
    priority_queue = [(0, source)]  # (distance, vertex)

    # TODO: Step 3 - Process the priority queue
    # While the priority queue is not empty, extract the vertex with the smallest distance.
    # Relax the edges of the extracted vertex, updating the distances to its neighbors.

    while priority_queue:
        cur_dist, cur_node = heapq.heappop(priority_queue)

        for oe in adj_list[cur_node]:
            nn, w = oe
            if distances[nn] > cur_dist + w:
                distances[nn] = cur_dist + w
                heapq.heappush(priority_queue, (distances[nn], nn))

    # TODO: Step 4 - Return the distance array
    return distances


# Example test cases
if __name__ == "__main__":
    # Test case 1: Simple graph
    n1 = 5
    edges1 = [(0, 1, 2), (0, 2, 4), (1, 2, 1), (1, 3, 7), (2, 4, 3), (3, 4, 1)]
    source1 = 0
    print(
        "Test Case 1 - Expected: [0, 2, 3, 9, 6], Got:", dijkstra(n1, edges1, source1)
    )

    # Test case 2: Disconnected graph
    n2 = 4
    edges2 = [(0, 1, 1), (2, 3, 2)]
    source2 = 0
    print(
        "Test Case 2 - Expected: [0, 1, inf, inf], Got:", dijkstra(n2, edges2, source2)
    )

    # Test case 3: Single node
    n3 = 1
    edges3 = []
    source3 = 0
    print("Test Case 3 - Expected: [0], Got:", dijkstra(n3, edges3, source3))

    # Test case 4: No edges
    n4 = 5
    edges4 = []
    source4 = 0
    print(
        "Test Case 4 - Expected: [0, inf, inf, inf, inf], Got:",
        dijkstra(n4, edges4, source4),
    )
