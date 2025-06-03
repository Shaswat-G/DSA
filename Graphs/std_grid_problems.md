# Complete Strategy Guide for Grid Problems

- **Grids are implicit graphs**: You don't need to build an adjacency list. Each cell is a node, and you generate neighbors on-demand.
- **BFS properties**: Guarantees shortest path in unweighted graphs because it explores level by level (like ripples in water).
- **Space-time tradeoff**: BFS uses O(V) space for the queue and visited set, but gives you shortest paths. DFS uses O(h) space (height of tree) but doesn't guarantee shortest paths.

### **Python Object Insights**
- **`deque` vs `list`**: `deque.popleft()` is O(1), while `list.pop(0)` is O(n). Always use `deque` for BFS.
- **`set` for visited**: O(1) average lookup time vs O(n) for lists. Critical for performance.
- **Tuple hashing**: `(row, col)` tuples are hashable and work great as dictionary keys and set elements.
- **Generator expressions**: `(nr, nc) for dr, dc in directions for nr, nc in [r+dr, c+dc] if is_valid(nr, nc)]` can be memory efficient.

### **Advanced DSA Concepts**
- **Bidirectional search**: Reduces search space from O(b^d) to O(b^(d/2)) where b is branching factor and d is depth.
- **A* heuristic**: Manhattan distance `|x1-x2| + |y1-y2|` is admissible (never overestimates) for grid problems.
- **State space search**: When problems have additional state (keys, remaining moves), your visited set becomes `(position, state)` tuples.

### **Memory Management Tips**
- For very large grids, consider using bitwise operations for visited tracking
- Use `collections.defaultdict` when you need to initialize complex data structures
- Consider iterative deepening for memory-constrained environments

### **Problem Recognition Patterns**
- **Multi-source BFS**: "All X spread to adjacent cells simultaneously"
- **Level-order BFS**: "Minimum time/steps for all cells to be affected"
- **State-based BFS**: "Collect items", "limited moves", "conditional movement"
- **Component counting**: "Number of islands/regions/connected areas"

The beauty of grid problems is that they're concrete visualizations of abstract graph concepts. Once you master the patterns I've shown you, you'll recognize that most "complex" grid problems are just variations of these fundamental templates with different movement rules or state tracking.

**Practice Strategy**: Start with the basic BFS template, then gradually add complexity (multi-source, state tracking, optimizations). The patterns will become second nature, and you'll be able to adapt them to any grid problem you encounter.

## Step 1: Problem Analysis and Classification

### 1.1 Identify the Problem Type
- **Single Source Shortest Path**: BFS from one starting point
- **Multi-Source**: BFS from multiple starting points (rotting oranges, walls and gates)
- **All Pairs Shortest Path**: Floyd-Warshall or run BFS from each cell
- **Connected Components**: Count islands, flood fill
- **Path with Constraints**: Keys and doors, obstacle elimination
- **Optimization Problems**: Minimum cost path, collect all items

### 1.2 Key Questions to Ask
1. **What represents nodes and edges?**
   - Nodes: Usually cells in the grid
   - Edges: Adjacent cells (4-directional or 8-directional)

2. **What are the movement rules?**
   - Can move diagonally?
   - Are there special movement patterns?
   - Any restrictions based on cell values?

3. **What defines a valid path?**
   - Which cells can be visited?
   - Are there obstacles?
   - Any state-dependent restrictions?

4. **What's the goal?**
   - Find shortest distance?
   - Find actual path?
   - Count something?
   - Transform the grid?

## Step 2: Choose the Right Algorithm

### 2.1 Algorithm Selection Matrix

| Problem Characteristics | Best Algorithm | Time Complexity |
|------------------------|----------------|-----------------|
| Unweighted, single target | BFS | O(V + E) = O(mn) |
| Unweighted, multiple sources | Multi-source BFS | O(mn) |
| Weighted edges | Dijkstra's | O(mn log(mn)) |
| With heuristic to target | A* | O(mn log(mn)) |
| Large grid, distant target | Bidirectional BFS | O(b^(d/2)) |
| Connected components | BFS/DFS | O(mn) |

### 2.2 BFS Variations Quick Reference

```python
# Standard BFS Template
def bfs_template(grid, start, target_condition):
    queue = deque([start])
    visited = set([start])
    
    while queue:
        current = queue.popleft()
        
        if target_condition(current):
            return True  # or distance, path, etc.
        
        for neighbor in get_valid_neighbors(current, grid):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return False

# Level-by-level BFS (when you need to track levels/steps)
def level_bfs_template(grid, start):
    queue = deque([start])
    visited = set([start])
    level = 0
    
    while queue:
        level_size = len(queue)
        
        for _ in range(level_size):
            current = queue.popleft()
            # Process current node
            
            for neighbor in get_valid_neighbors(current, grid):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        level += 1
    
    return level

# Multi-source BFS
def multi_source_bfs_template(grid, sources):
    queue = deque(sources)
    visited = set(sources)
    
    while queue:
        current = queue.popleft()
        
        for neighbor in get_valid_neighbors(current, grid):
            if neighbor not in visited and is_valid(neighbor, grid):
                visited.add(neighbor)
                queue.append(neighbor)

# BFS with state (for complex problems)
def bfs_with_state_template(grid, start, initial_state):
    queue = deque([(start, initial_state)])
    visited = set([(start, initial_state)])
    
    while queue:
        current_pos, current_state = queue.popleft()
        
        for neighbor in get_valid_neighbors(current_pos, grid):
            new_state = update_state(current_state, neighbor, grid)
            
            if (neighbor, new_state) not in visited:
                visited.add((neighbor, new_state))
                queue.append((neighbor, new_state))
```

## Step 3: Implementation Checklist

### 3.1 Before Coding
- [ ] Understand what each cell value represents
- [ ] Identify valid movements (4 or 8 directional)
- [ ] Determine what constitutes a valid neighbor
- [ ] Plan your state representation
- [ ] Consider edge cases (empty grid, single cell, no solution)

### 3.2 During Implementation
- [ ] Handle boundary checking properly
- [ ] Use appropriate data structures:
  - `deque` for BFS queue
  - `set` for visited tracking (O(1) lookup)
  - `dict` for parent tracking (path reconstruction)
- [ ] Implement neighbor generation efficiently
- [ ] Handle obstacle/invalid cell checking
- [ ] Consider memory optimization for large grids

### 3.3 Common Pitfalls to Avoid
- **Off-by-one errors**: Check boundary conditions carefully
- **Infinite loops**: Ensure visited set is working correctly
- **Memory issues**: For large grids, consider memory-efficient approaches
- **State representation**: In complex problems, ensure state is properly defined
- **Direction arrays**: Double-check direction vectors

## Step 4: Problem-Specific Patterns

### 4.1 Shortest Path Problems
```python
def shortest_path_pattern(grid, start, end):
    if start == end:
        return 0
    
    queue = deque([(start[0], start[1], 0)])
    visited = set([start])
    
    while queue:
        r, c, dist = queue.popleft()
        
        for nr, nc in get_neighbors(r, c, grid):
            if (nr, nc) == end:
                return dist + 1
            
            if (nr, nc) not in visited and is_valid(nr, nc, grid):
                visited.add((nr, nc))
                queue.append((nr, nc, dist + 1))
    
    return -1
```

### 4.2 Flood Fill Pattern
```python
def flood_fill_pattern(grid, start_r, start_c, new_value):
    original = grid[start_r][start_c]
    if original == new_value:
        return
    
    queue = deque([(start_r, start_c)])
    
    while queue:
        r, c = queue.popleft()
        if grid[r][c] != original:
            continue
        
        grid[r][c] = new_value
        
        for nr, nc in get_neighbors(r, c, grid):
            if grid[nr][nc] == original:
                queue.append((nr, nc))
```

### 4.3 Count Components Pattern
```python
def count_components_pattern(grid):
    visited = set()
    count = 0
    
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if (r, c) not in visited and grid[r][c] == 1:
                bfs_explore_component(grid, r, c, visited)
                count += 1
    
    return count
```

## Step 5: Optimization Strategies

### 5.1 When to Use Each Optimization
- **Bidirectional BFS**: Single source-target, large grid
- **A* Search**: When you have a good heuristic (Manhattan distance for grids)
- **Multi-source BFS**: Multiple starting points
- **Early termination**: When you don't need to explore the entire grid
- **Memory optimization**: Very large grids

### 5.2 Space-Time Tradeoffs
- **More memory, less time**: Store distances/paths in arrays
- **Less memory, more time**: Recompute neighbors, use generators
- **Balanced approach**: Use visited sets, compute neighbors on-demand

## Step 6: Testing Strategy

### 6.1 Test Cases to Always Include
1. **Empty grid or single cell**
2. **No solution exists**
3. **Start equals end**
4. **Grid with all obstacles**
5. **Grid with no obstacles**
6. **Boundary conditions**
7. **Large grids (performance testing)**

### 6.2 Debugging Tips
1. **Visualize the grid**: Print intermediate states
2. **Track visited cells**: Ensure no infinite loops
3. **Verify neighbors**: Print neighbor lists for debugging
4. **Step through BFS**: Print queue contents at each step
5. **Check edge cases**: Test with minimal examples

## Step 7: Common LeetCode/Interview Patterns

### 7.1 Must-Know Problems
1. **Number of Islands** (Basic BFS/DFS)
2. **Rotting Oranges** (Multi-source BFS)
3. **Walls and Gates** (Multi-source BFS)
4. **Shortest Path in Binary Matrix** (BFS with path)
5. **Word Search** (DFS with backtracking)
6. **Pacific Atlantic Water Flow** (Multi-source BFS from edges)
7. **01 Matrix** (Multi-source BFS)

### 7.2 Advanced Patterns
1. **Shortest Path with Obstacle Elimination** (BFS with state)
2. **Word Ladder** (BFS on word graph)
3. **Jump Game** (BFS with variable steps)
4. **Robot Room Cleaner** (DFS with unknown grid)

## Quick Reference Code Snippets

### Essential Helper Functions
```python
def get_neighbors(r, c, grid):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    neighbors = []
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
            neighbors.append((nr, nc))
    return neighbors

def is_valid(r, c, grid, obstacle_value=0):
    return (0 <= r < len(grid) and 0 <= c < len(grid[0]) and 
            grid[r][c] != obstacle_value)
```

### Time and Space Complexity Quick Reference
- **BFS on grid**: O(mn) time, O(mn) space
- **Multi-source BFS**: O(mn) time, O(mn) space  
- **Bidirectional BFS**: O(b^(d/2)) time, O(b^(d/2)) space
- **A* Search**: O(mn log(mn)) time, O(mn) space

Remember: The key to mastering grid problems is recognizing patterns and practicing the fundamental BFS template with different variations. Start with simple problems and gradually work your way up to more complex state-based problems.