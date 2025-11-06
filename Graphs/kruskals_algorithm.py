"""
Kruskal's Algorithm for Minimum Spanning Tree (MST)

Problem Statement:
Kruskal's algorithm is a greedy algorithm used to find the Minimum Spanning Tree (MST) of a connected, undirected graph. It works by sorting all edges in the graph by their weights and adding them one by one to the MST, ensuring no cycles are formed.

Steps:
1. Sort all edges in non-decreasing order of their weights.
2. Initialize an empty MST.
3. Iterate through the sorted edges and add an edge to the MST if it doesn't form a cycle (using a Disjoint Set to check).
4. Stop when the MST contains exactly (V-1) edges, where V is the number of vertices.

Applications:
- Network design (e.g., designing least-cost networks).
- Approximation algorithms for NP-hard problems.

Time Complexity:
- Sorting edges: O(E log E)
- Union-Find operations: O(E * \u03b1(V)), where \u03b1 is the inverse Ackermann function.
- Overall: O(E log E), as E log E dominates for sparse graphs.

"""


class DisjointSet:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n
        return None

    def find(self, x: int) -> int:
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            rank_x = self.size[root_x]
            rank_y = self.size[root_y]

            if rank_x >= rank_y:
                self.parent[root_y] = root_x
                self.size[root_x] += self.size[root_y]
            else:
                self.parent[root_x] = root_y
                self.size[root_y] += self.size[root_x]

        return None

    def is_connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


class Edge:
    def __init__(self, u: int, v: int, weight: int):
        self.u = u  # One vertex of the edge
        self.v = v  # Other vertex of the edge
        self.weight = weight  # Weight of the edge

    def __lt__(self, other):
        return self.weight < other.weight


class KruskalMST:
    def __init__(self, vertices: int):
        """
        Initialize the Kruskal's MST algorithm.

        :param vertices: int - The number of vertices in the graph.
        """
        self.vertices = vertices
        self.edges = []  # List to store all edges
        self.uf = DisjointSet(self.vertices)

    def add_edge(self, u: int, v: int, weight: int):
        """
        Add an edge to the graph.

        :param u: int - One vertex of the edge.
        :param v: int - Other vertex of the edge.
        :param weight: int - Weight of the edge.
        """
        self.edges.append(Edge(u, v, weight))

    def find_mst(self):
        """
        Find the Minimum Spanning Tree (MST) using Kruskal's algorithm.

        :return: List[Tuple[int, int, int]] - The edges in the MST.
        """
        # TODO: Sort edges by weight
        self.edges.sort(key=lambda x: x.weight)

        # TODO: Iterate through edges and add to MST if no cycle is formed
        mst = []
        cost = 0
        for edge in self.edges:
            if not self.uf.is_connected(edge.u, edge.v):
                self.uf.union(edge.u, edge.v)
                mst.append(edge)
                cost += edge.weight

        # TODO: Return the edges in the MST
        return mst


# Example Usage
if __name__ == "__main__":
    # TODO: Initialize Kruskal's MST with the number of vertices
    kruskal = KruskalMST(5)

    # TODO: Add edges to the graph
    kruskal.add_edge(0, 1, 10)
    kruskal.add_edge(0, 2, 6)
    kruskal.add_edge(0, 3, 5)
    kruskal.add_edge(1, 3, 15)
    kruskal.add_edge(2, 3, 4)

    # TODO: Find the MST
    mst = kruskal.find_mst()

    # TODO: Print the edges in the MST
    print("Edges in the MST:")
    for edge in mst:
        print(f"{edge.u} -- {edge.v} == {edge.weight}")
