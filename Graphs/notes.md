# Graphs: Comprehensive DSA Notes

## 1. Graph Terminologies

- **Graph (G):** A set of vertices (V) and edges (E), G = (V, E).
- **Vertex (Node):** Fundamental unit (V).
- **Edge:** Connection between two vertices (E).
- **Directed Graph (Digraph):** Edges have direction (u → v).
- **Undirected Graph:** Edges have no direction (u—v).
- **Weighted Graph:** Edges have weights/costs.
- **Unweighted Graph:** All edges are equal.
- **Connected Graph:** There is a path between every pair of vertices.
- **Disconnected Graph:** Not all vertices are reachable from each other.
- **Strongly Connected (Directed):** Every vertex is reachable from every other vertex.
- **Weakly Connected (Directed):** Underlying undirected graph is connected.
- **Articulation Point:** Vertex whose removal increases the number of connected components.
- **Bridge (Cut Edge):** Edge whose removal increases the number of connected components.
- **Cycle:** Path that starts and ends at the same vertex, with all edges/vertices distinct (except start/end).
- **Parallel Edges:** Multiple edges between the same pair of vertices.
- **Self Loop:** Edge from a vertex to itself.
- **In-degree:** Number of incoming edges to a vertex (for directed graphs).
- **Out-degree:** Number of outgoing edges from a vertex (for directed graphs).
- **Directed Acyclic Graph (DAG):** Directed graph with no cycles.
- **Topological Ordering:** Linear ordering of vertices in a DAG such that for every edge u→v, u comes before v.

## 2. Graph Representations

- **Adjacency Matrix:**
  - 2D array (V x V), entry [i][j] = 1 if edge exists, else 0 (or weight for weighted graphs).
  - Space: O(V²). Fast edge lookup, slow for sparse graphs.
- **Adjacency List:**
  - Array/list of lists. Each vertex stores a list of adjacent vertices.
  - Space: O(V + E). Efficient for sparse graphs.
- **Compact List:**
  - Flattened adjacency list for memory efficiency (used in competitive programming).

## 3. Graph Traversal Algorithms

### Breadth-First Search (BFS)

- Explores neighbors level by level using a queue.
- Finds shortest path in unweighted graphs.
- Time: O(V + E)
- Used for: Shortest path, connected components, bipartite check, level order, etc.

**BFS Pseudocode:**

```
BFS(G, start):
    visited = [False] * V
    queue = [start]
    visited[start] = True
    while queue:
        v = queue.pop(0)
        for u in G.adj[v]:
            if not visited[u]:
                visited[u] = True
                queue.append(u)
```

### Depth-First Search (DFS)

- Explores as far as possible along each branch before backtracking (uses stack or recursion).
- Used for: Cycle detection, topological sort, connected components, articulation points, etc.
- Time: O(V + E)

**DFS Pseudocode:**

```
DFS(G, v):
    visited[v] = True
    for u in G.adj[v]:
        if not visited[u]:
            DFS(G, u)
```

## 4. Key Formulas and MCQ Tips

- **Number of edges in complete graph:**
  - Undirected: E = V(V-1)/2
  - Directed: E = V(V-1)
- **Sum of degrees (undirected):** 2E
- **Sum of in-degrees = sum of out-degrees = E (directed)**
- **Max edges in undirected graph:** V(V-1)/2
- **Max edges in directed graph:** V(V-1)
- **Tree:** Connected acyclic undirected graph with V vertices and V-1 edges.
- **Bipartite Graph:** Can be colored with 2 colors (no odd cycles).
- **DAG:** No cycles, can be topologically sorted.

## 5. DSA Implementations (Python)

### Adjacency Matrix

```python
class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = [[0]*V for _ in range(V)]
    def add_edge(self, u, v):
        self.adj[u][v] = 1
        self.adj[v][u] = 1  # Remove for directed
```

### Adjacency List

```python
class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for _ in range(V)]
    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)  # Remove for directed
```

### BFS (Adjacency List)

```python
from collections import deque

def bfs(graph, start):
    visited = [False] * len(graph.adj)
    q = deque([start])
    visited[start] = True
    while q:
        v = q.popleft()
        print(v)
        for u in graph.adj[v]:
            if not visited[u]:
                visited[u] = True
                q.append(u)
```

### DFS (Adjacency List)

```python
def dfs(graph, v, visited=None):
    if visited is None:
        visited = [False] * len(graph.adj)
    visited[v] = True
    print(v)
    for u in graph.adj[v]:
        if not visited[u]:
            dfs(graph, u, visited)
```

### Path Existence (BFS)

```python
def has_path(graph, src, dest):
    visited = [False] * len(graph.adj)
    q = deque([src])
    visited[src] = True
    while q:
        v = q.popleft()
        if v == dest:
            return True
        for u in graph.adj[v]:
            if not visited[u]:
                visited[u] = True
                q.append(u)
    return False
```
## Grid problems:
Problems like "Number of Islands" can be solved using BFS/DFS on a grid by treating each cell as a vertex and adjacent cells as edges. Shortest path on unweighted grids can also be solved using BFS.




## 6. Common MCQ/Interview Points

- **Self-loop:** Counts as 1 edge, degree +2 (undirected).
- **Parallel edges:** Allowed in multigraphs, not in simple graphs.
- **Acyclic:** No cycles.
- **Tree:** Connected, acyclic, V-1 edges.
- **Bipartite:** No odd cycles. The vertex set is partionable into two disjoint sets, where no two graph vertices within the same set are adjacent.
- **DAG:** Topological sort possible.
- **Articulation point/bridge:** Removal increases #components.
- **Eulerian Path/Circuit:** All vertices even degree (circuit), exactly two odd (path).
- **Hamiltonian Path/Circuit:** Visits each vertex once (NP-complete).

## 7. Classic Problems Solved with BFS/DFS (and Their Variants)

### A. Traversal & Search

- **Connected Components**
  - _Idea:_ Each traversal visits all nodes in that connected components. Use BFS/DFS to mark all nodes in a component. Repeat for all unvisited nodes. The number of times you start a new traversal is the number of connected components. To count distinct islands keep track of the BFS sequence in a set
  - and compare a new BFS sequence with the set to check if it's a new island or not.
  - _When to use:_ Find number of islands, clusters, or groups.
- **Path Existence**
  - _Idea:_ Use BFS/DFS to check if a path exists between two nodes.
  - _When to use:_ "Is there a route between X and Y?"
- **Shortest Path in Unweighted Graph**
  - _Idea:_ BFS finds shortest path (fewest edges) from source to target.
  - _When to use:_ Maze solving, minimum moves, word ladder.
- **Cycle Detection**
  - _Idea:_ DFS with parent tracking (undirected), or color/recursion stack (directed).
  - _When to use:_ Check if a graph is a tree, detect deadlocks, validate course schedules.
- **Topological Sort (DAGs)**
  - _Idea:_ DFS postorder or BFS with in-degree (Kahn's algorithm).
  - _When to use:_ Task scheduling, course prerequisites.
- **Bipartite Check**
  - _Idea:_ BFS/DFS with coloring. If a conflict occurs, not bipartite.
  - _When to use:_ Team assignments, graph coloring, matching problems.
- **Articulation Points & Bridges**
  - _Idea:_ DFS with discovery/low times (Tarjan's algorithm).
  - _When to use:_ Network reliability, critical connections.
- **Eulerian Path/Circuit**
  - _Idea:_ DFS to check degree conditions and connectivity.
  - _When to use:_ Route planning, circuit design.
- **Hamiltonian Path/Circuit**
  - _Idea:_ Backtracking DFS (NP-complete, not efficient for large graphs).
  - _When to use:_ Traveling Salesman, puzzle games.
- **Flood Fill / Region Growing**
  - _Idea:_ BFS/DFS to fill all connected cells of the same type.
  - _When to use:_ Image processing, coloring, "number of islands".
- **Clone Graph**
  - _Idea:_ BFS/DFS to copy nodes and edges, using a map to avoid cycles.
  - _When to use:_ Deep copy of data structures.
- **Counting Paths/Components**
  - _Idea:_ DFS/BFS to enumerate or count all possible paths/components.
  - _When to use:_ Counting unique routes, number of islands, etc.

### B. Essential Patterns/Modifications

- **Multi-source BFS**: Start BFS from multiple sources at once (e.g., rotten oranges, fire spread).
- **Level-order Traversal**: BFS naturally gives levels (distance from source).
- **Backtracking with DFS**: For all possible paths, permutations, or combinations.
- **Recursive DFS**: For tree/graph problems where state is naturally recursive.
- **Iterative DFS/BFS**: For stack/queue-based exploration, especially in large graphs.
- **State Compression**: Use BFS/DFS on state spaces (bitmask, tuple, etc.), not just nodes.

---

## 8. Real-World & LeetCode/Interview Problems That Are Graphs at Their Core

### A. Classic Graph Problems

- **Number of Islands** (LeetCode 200): Connected components in a grid (DFS/BFS).
- **Clone Graph** (LeetCode 133): Deep copy using BFS/DFS.
- **Course Schedule** (LeetCode 207): Cycle detection/topological sort in a DAG.
- **Word Ladder** (LeetCode 127): Shortest path in word graph (BFS).
- **Pacific Atlantic Water Flow** (LeetCode 417): Multi-source BFS/DFS from borders.
- **Rotting Oranges** (LeetCode 994): Multi-source BFS for minimum time.
- **Surrounded Regions** (LeetCode 130): Flood fill from border (DFS/BFS).
- **Minimum Genetic Mutation** (LeetCode 433): BFS in state space.
- **Friend Circles** (LeetCode 547): Connected components.
- **Accounts Merge** (LeetCode 721): Connected components with DFS.
- **Reconstruct Itinerary** (LeetCode 332): Hierholzer’s algorithm (DFS for Eulerian path).
- **All Paths From Source to Target** (LeetCode 797): Backtracking DFS for all paths.
- **Critical Connections in a Network** (LeetCode 1192): Tarjan’s algorithm for bridges.
- **Find Eventual Safe States** (LeetCode 802): DFS with cycle detection.
- **Evaluate Division** (LeetCode 399): BFS/DFS in weighted graph.
- **Sliding Puzzle** (LeetCode 773): BFS in state space.
- **Snakes and Ladders** (LeetCode 909): BFS for minimum moves.
- **Jump Game III** (LeetCode 1306): BFS/DFS for reachability.
- **Longest Consecutive Sequence** (LeetCode 128): Union-Find/DFS.
- **Connected Components in Undirected Graph** (LeetCode 323): DFS/BFS.
- **Find the Town Judge** (LeetCode 997): In-degree/out-degree analysis.

### B. Real-World Applications

- **Social Networks:** Friend suggestions, community detection (BFS/DFS, connected components).
- **Navigation/Maps:** Shortest path, reachability (BFS, Dijkstra, A\*).
- **Web Crawling:** BFS/DFS to traverse links.
- **Network Routing:** Path finding, cycle detection, reliability (BFS/DFS, articulation points).
- **Image Processing:** Flood fill, region labeling (BFS/DFS).
- **Scheduling/Dependency Resolution:** Topological sort (DFS/BFS).
- **Puzzle Solving:** State space search (BFS/DFS, e.g., sliding puzzles).
- **Recommendation Systems:** Graph traversal for similar items/users.

---

## 9. How to Recognize When to Use BFS/DFS

- **BFS:**
  - Shortest path in unweighted graphs
  - Level-order traversal (distance, minimum steps)
  - Multi-source propagation (spread, infection, fire)
  - When you need the "closest" solution
- **DFS:**
  - All possible paths, permutations, or combinations
  - Cycle detection, topological sort
  - Backtracking, recursion, tree/graph traversal
  - When you need to explore all options or states

**Key:** If the problem involves exploring neighbors, finding paths, counting regions, or simulating spread, think BFS/DFS. If the problem can be modeled as a graph (even if not explicit), try to represent it as such and apply these techniques.

---

This guide covers theory, formulas, and practical DSA implementations for graphs. Use it for MCQs, interviews, and coding!


**Toplogical Sort**
Producing a linear ordering of vertices for a DAG such that for every directed edge u → v, vertex u comes before v in the ordering. This ordering is not unique; multiple valid orderings may exist for a given DAG.

For connected components, we can run BFS/DFS from each unvisited node to ensure all components are checked.

**Eventual Safe States**
In a directed graph, a node is considered "safe" if every possible path starting from that node leads to a terminal node (a node with no outgoing edges). The goal is to find all such safe nodes in the graph. Can be done using DFS with cycle detection or reverse graph + topological sort.

# study cycle detection in directed graps using DFS and then BFS (Kahn's Algorithm). 


Shortest path in unweighted graph can be found using standard BFS.

shortest path in weighted graph can be found using Dijkstra's algorithm. (with or without cycles).

Shotest path in weighted DAG can be found using topological sort followed by edge relaxation.

## Shortest Path Problems in Graphs

Shortest path problems involve finding the minimum distance or cost to travel between two nodes in a graph. The choice of algorithm depends on the graph's properties, such as whether it is directed or undirected, weighted or unweighted, and whether it contains cycles. Below is a detailed breakdown of the variants and the algorithms used to solve them.

### 1. Unweighted Graphs

#### Directed and Undirected Graphs
- **Algorithm**: Breadth-First Search (BFS)
- **Why BFS?**
  - BFS explores all nodes at the current distance before moving to the next level.
  - In unweighted graphs, the shortest path is determined by the number of edges, making BFS optimal.
- **Key Intuition**:
  - BFS guarantees that the first time a node is visited, it is reached via the shortest path.
- **Complexity**: O(V + E), where V is the number of vertices and E is the number of edges.

### 2. Weighted Graphs

#### Without Negative Weights
- **Algorithm**: Dijkstra's Algorithm
- **Why Dijkstra's?**
  - Dijkstra's algorithm uses a priority queue to always expand the shortest known path first.
  - It works efficiently when all edge weights are non-negative.
- **Key Intuition**:
  - The algorithm maintains a "visited" set and a "distance" array. Once a node is processed, its shortest distance is finalized.
- **Complexity**: O((V + E) log V) with a priority queue.

#### With Negative Weights (No Negative Cycles)
- **Algorithm**: Bellman-Ford Algorithm
- **Why Bellman-Ford?**
  - Bellman-Ford relaxes all edges repeatedly, ensuring that even paths with negative weights are considered.
  - It can detect negative weight cycles.
- **Key Intuition**:
  - The algorithm iteratively improves the shortest path estimate for each edge.
- **Complexity**: O(VE)

#### With Negative Cycles
- **Algorithm**: Bellman-Ford (to detect negative cycles)
- **Why Not Dijkstra's?**
  - Dijkstra's algorithm fails with negative weights because it assumes that once a node is processed, its shortest distance is finalized, which is not true with negative cycles.
- **Key Intuition**:
  - Negative cycles allow infinite reductions in path cost, making the shortest path undefined.

### 3. Directed Acyclic Graphs (DAGs)

#### Weighted DAGs
- **Algorithm**: Topological Sort + Edge Relaxation
- **Why Topological Sort?**
  - In a DAG, topological sorting provides a linear order of vertices, ensuring that all edges are processed in the correct order.
  - This allows edge relaxation to be performed in a single pass.
- **Key Intuition**:
  - The absence of cycles ensures that once a node is processed, its shortest distance is finalized.
- **Complexity**: O(V + E)

### 4. Graphs with Cycles

#### Positive Weight Cycles
- **Algorithm**: Dijkstra's Algorithm (if no negative weights)
- **Why Dijkstra's?**
  - Positive weight cycles do not affect the correctness of Dijkstra's algorithm.

#### Negative Weight Cycles
- **Algorithm**: Bellman-Ford (to detect cycles)
- **Why Bellman-Ford?**
  - Negative weight cycles make the shortest path undefined, and Bellman-Ford can detect such cycles.

### 5. All-Pairs Shortest Path

#### Unweighted Graphs
- **Algorithm**: BFS for each node
- **Complexity**: O(V(V + E))

#### Weighted Graphs (No Negative Weights)
- **Algorithm**: Dijkstra's Algorithm for each node
- **Complexity**: O(V(V + E) log V)

#### Weighted Graphs (With Negative Weights)
- **Algorithm**: Floyd-Warshall Algorithm
- **Why Floyd-Warshall?**
  - Floyd-Warshall uses dynamic programming to compute shortest paths between all pairs of nodes.
  - It handles negative weights but not negative cycles.
- **Key Intuition**:
  - The algorithm iteratively considers whether a path through an intermediate node is shorter.
- **Complexity**: O(V³)

### 6. Special Cases

#### Single Source to All Nodes
- **Unweighted Graphs**: BFS
- **Weighted Graphs (No Negative Weights)**: Dijkstra's Algorithm
- **Weighted Graphs (With Negative Weights)**: Bellman-Ford Algorithm

#### Single Pair Shortest Path
- **Unweighted Graphs**: BFS
- **Weighted Graphs (No Negative Weights)**: Dijkstra's Algorithm
- **Weighted Graphs (With Negative Weights)**: Bellman-Ford Algorithm

#### Multi-Source Shortest Path
- **Algorithm**: Multi-Source BFS
- **Why Multi-Source BFS?**
  - BFS can be initialized with multiple sources, treating them as a single virtual source.

### Summary Table
| Graph Type                | Algorithm                  | Complexity       |
|---------------------------|----------------------------|------------------|
| Unweighted                | BFS                        | O(V + E)         |
| Weighted (No Negatives)   | Dijkstra's                | O((V + E) log V) |
| Weighted (With Negatives) | Bellman-Ford              | O(VE)            |
| Weighted DAG              | Topological Sort + Relax  | O(V + E)         |
| All-Pairs (No Negatives)  | Dijkstra's for each node  | O(V(V + E) log V)|
| All-Pairs (With Negatives)| Floyd-Warshall            | O(V³)            |

### Choosing the Right Algorithm
1. **Unweighted Graphs**:
   - Use BFS for its simplicity and efficiency.
2. **Weighted Graphs**:
   - Use Dijkstra's if all weights are non-negative.
   - Use Bellman-Ford if negative weights are present.
3. **DAGs**:
   - Use Topological Sort + Edge Relaxation for its linear complexity.
4. **All-Pairs Shortest Path**:
   - Use Floyd-Warshall for dense graphs or graphs with negative weights.
   - Use Dijkstra's for sparse graphs with non-negative weights.
5. **Graphs with Cycles**:
   - Use Bellman-Ford to detect negative cycles.

By understanding the properties of the graph and the requirements of the problem, you can select the most appropriate algorithm for finding the shortest path.



