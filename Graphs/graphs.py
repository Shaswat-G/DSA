from collections import deque


class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_matrix = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]

    def add_edge(self, u, v):
        self.adj_matrix[u][v] = 1
        self.adj_matrix[v][u] = 1  # For undirected graph; remove for directed

    def __str__(self):
        return "\n".join([" ".join(map(str, row)) for row in self.adj_matrix])

    def bfs(self, starting_vertex: int = 0) -> None:
        visited = [0] * self.num_vertices
        result = []

        q = deque([starting_vertex])
        while q:
            vertex = q.popleft()
            result.append(str(vertex))
            visited[vertex] = 1
            for adj_vertex, is_edge in enumerate(self.adj_matrix[vertex]):
                if is_edge and not visited[adj_vertex]:
                    visited[adj_vertex] = 1
                    q.append(adj_vertex)

        print(f'BFS : {" ".join(result)}')
        return None

    def dfs(self, starting_vertex: int = 0) -> None:
        visited = [0] * self.num_vertices
        result = []

        def dfs_util(v):
            visited[v] = 1
            result.append(str(v))
            for adj_vertex, is_edge in enumerate(self.adj_matrix[v]):
                if is_edge and not visited[adj_vertex]:
                    dfs_util(adj_vertex)

        dfs_util(starting_vertex)
        print(f'DFS : {" ".join(result)}')
        return None


# Example usage:
g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(3, 4)
g.add_edge(1, 3)
g.add_edge(0, 4)
print(g)

g.bfs()
g.dfs()
