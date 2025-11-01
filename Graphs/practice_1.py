from collections import deque
from typing import List


class Graph:
    def __init__(self, num_vertices: int = 5):
        self.num_vertices = num_vertices
        self.adj_matrix = [
            [0 for _ in range(num_vertices)] for _ in range(num_vertices)
        ]

    def validate_vertex(self, v: int) -> bool:
        return not (v < 0 or v >= self.num_vertices)

    def add_edge(self, u: int, v: int):
        if not self.validate_vertex(u) or not self.validate_vertex(v):
            raise ValueError("Invalid Vertex")
        self.adj_matrix[u][v] = 1
        self.adj_matrix[v][u] = 1
        return None

    def BFS(self, starting_vertex: int) -> List[int]:
        if not self.validate_vertex(starting_vertex):
            raise ValueError("Invalid Vertex")

        result = []
        visited = [False for vertex in range(self.num_vertices)]
        q = deque([starting_vertex])
        visited[starting_vertex] = True
        result.append(starting_vertex)

        while q:
            current_vertex = q.popleft()
            for adj_vertex, edge in enumerate(self.adj_matrix[current_vertex]):
                if edge and not visited[adj_vertex]:
                    q.append(adj_vertex)
                    visited[adj_vertex] = True
                    result.append(adj_vertex)

        print(" ".join(map(str, result)))
        return None

    def DFS(self, starting_vertex: int) -> List[int]:
        if not self.validate_vertex(starting_vertex):
            raise ValueError("Invalid Vertex")

        visited = [False for vertex in range(self.num_vertices)]
        result = []

        def dfs(vertex: int):
            visited[vertex] = True
            result.append(vertex)
            for adj_vertex, edge in enumerate(self.adj_matrix[vertex]):
                if edge and not visited[adj_vertex]:
                    dfs(adj_vertex)

        dfs(starting_vertex)
        print(" ".join(map(str, result)))
        return result

    def __len__(self):
        return self.num_vertices

    def __str__(self):
        return "\n".join([" ".join(map(str, row)) for row in self.adj_matrix])


if __name__ == "__main__":

    graph = Graph(5)
    graph.add_edge(0, 2)
    graph.add_edge(1, 4)

    graph.add_edge(3, 2)

    graph.add_edge(4, 3)

    print(len(graph))
    print(graph)

    graph.BFS(2)
    graph.DFS(3)
