# Python Collections and Typing Libraries - Complete Guide

## 📚 Overview

These two libraries are fundamental for writing clean, efficient Python code, especially in competitive programming and technical interviews.

- **`typing`**: Provides type hints for better code documentation and IDE support
- **`collections`**: Provides specialized container datatypes beyond built-in lists, dicts, sets

## 🎯 The `typing` Module

### What is Type Hinting?

Type hints are annotations that specify what type of data a variable, parameter, or return value should be. They don't affect runtime behavior but provide:

- **Better IDE support** (autocomplete, error detection)
- **Code documentation** (makes intent clear)
- **Static analysis** (tools like mypy can catch type errors)
- **Interview clarity** (shows you write professional code)

### Common Type Hints in DSA

```python
from typing import List, Dict, Set, Tuple, Optional, Union

# Basic types
def process_number(x: int) -> int:
    return x * 2

def process_string(s: str) -> str:
    return s.upper()

def check_condition(flag: bool) -> bool:
    return not flag

# Collection types
def process_array(arr: List[int]) -> List[int]:
    return [x * 2 for x in arr]

def count_chars(s: str) -> Dict[str, int]:
    return {char: s.count(char) for char in set(s)}

def unique_elements(arr: List[int]) -> Set[int]:
    return set(arr)

def get_coordinates() -> Tuple[int, int]:
    return (0, 0)

# Optional types (can be None)
def find_element(arr: List[int], target: int) -> Optional[int]:
    try:
        return arr.index(target)
    except ValueError:
        return None

# Union types (multiple possible types)
def process_input(data: Union[int, str]) -> str:
    return str(data)

# Complex nested types
def create_matrix(rows: int, cols: int) -> List[List[int]]:
    return [[0] * cols for _ in range(rows)]

def build_graph() -> Dict[int, List[int]]:
    return {1: [2, 3], 2: [1, 4], 3: [1], 4: [2]}

def group_by_length(words: List[str]) -> Dict[int, List[str]]:
    result = {}
    for word in words:
        length = len(word)
        if length not in result:
            result[length] = []
        result[length].append(word)
    return result
```

### When to Use Type Hints in DSA/Interviews

**Always use for:**
- Function parameters and return types
- Complex data structures (List[List[int]], Dict[str, List[int]])
- When the type isn't obvious from context

**Example in Sliding Window:**
```python
def longest_substring_k_distinct(s: str, k: int) -> int:
    char_count: Dict[str, int] = {}
    left: int = 0
    max_len: int = 0
    # ... rest of implementation
```

## 🗂️ The `collections` Module

### What is collections?

The `collections` module provides specialized container datatypes that extend Python's built-in containers (dict, list, set, tuple) with additional functionality.

### Key Collections for DSA

#### 1. `defaultdict` - Dictionary with Default Values

**Problem it solves**: Eliminates KeyError when accessing missing keys.

```python
from collections import defaultdict

# Without defaultdict (verbose and error-prone)
def count_chars_verbose(s: str) -> Dict[str, int]:
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

# With defaultdict (clean and concise)
def count_chars_clean(s: str) -> Dict[str, int]:
    char_count = defaultdict(int)  # default value is 0
    for char in s:
        char_count[char] += 1
    return char_count

# Common defaultdict patterns in DSA
def build_adjacency_list(edges: List[Tuple[int, int]]) -> Dict[int, List[int]]:
    graph = defaultdict(list)  # default value is empty list
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    return graph

def group_anagrams(words: List[str]) -> Dict[str, List[str]]:
    groups = defaultdict(list)
    for word in words:
        key = ''.join(sorted(word))
        groups[key].append(word)
    return groups
```

**Common defaultdict types:**
- `defaultdict(int)` → default value 0
- `defaultdict(list)` → default value []
- `defaultdict(set)` → default value set()
- `defaultdict(lambda: float('inf'))` → custom default

#### 2. `deque` - Double-Ended Queue

**Problem it solves**: Efficient insertion/deletion from both ends (O(1) vs O(n) for lists).

```python
from collections import deque

# Sliding Window Maximum (classic deque usage)
def sliding_window_maximum(nums: List[int], k: int) -> List[int]:
    dq = deque()  # stores indices
    result = []
    
    for i in range(len(nums)):
        # Remove elements outside window
        while dq and dq[0] <= i - k:
            dq.popleft()  # O(1) operation
        
        # Maintain decreasing order
        while dq and nums[dq[-1]] <= nums[i]:
            dq.pop()  # O(1) operation
        
        dq.append(i)
        
        if i >= k - 1:
            result.append(nums[dq[0]])
    
    return result

# BFS traversal
def bfs(graph: Dict[int, List[int]], start: int) -> List[int]:
    visited = set()
    queue = deque([start])
    result = []
    
    while queue:
        node = queue.popleft()  # O(1) vs list.pop(0) which is O(n)
        if node not in visited:
            visited.add(node)
            result.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
    
    return result

# Moving window problems
def moving_average(nums: List[int], k: int) -> List[float]:
    window = deque()
    window_sum = 0
    result = []
    
    for num in nums:
        window.append(num)
        window_sum += num
        
        if len(window) > k:
            removed = window.popleft()
            window_sum -= removed
        
        if len(window) == k:
            result.append(window_sum / k)
    
    return result
```

#### 3. `Counter` - Counting Made Easy

**Problem it solves**: Simplified counting and frequency operations.

```python
from collections import Counter

# Character frequency
def most_common_char(s: str) -> str:
    counter = Counter(s)
    return counter.most_common(1)[0][0]

# Anagram detection
def are_anagrams(s1: str, s2: str) -> bool:
    return Counter(s1) == Counter(s2)

# Find elements appearing more than n/2 times
def majority_element(nums: List[int]) -> int:
    counter = Counter(nums)
    n = len(nums)
    for num, count in counter.items():
        if count > n // 2:
            return num

# Subtract counters (useful for sliding window)
def min_window_substring_counter(s: str, t: str) -> str:
    t_count = Counter(t)
    window_count = Counter()
    # ... implementation using counter arithmetic
```

#### 4. Other Useful Collections

```python
from collections import OrderedDict, namedtuple

# OrderedDict - maintains insertion order (less needed in Python 3.7+)
def lru_cache_simulation():
    cache = OrderedDict()
    # Move to end when accessed, pop from beginning when full

# namedtuple - lightweight object with named fields
Point = namedtuple('Point', ['x', 'y'])
def distance(p1: Point, p2: Point) -> float:
    return ((p1.x - p2.x)**2 + (p1.y - p2.y)**2)**0.5

# Usage
origin = Point(0, 0)
point = Point(3, 4)
print(distance(origin, point))  # 5.0
```

## 🎯 Common Patterns in DSA Problems

### Pattern 1: Frequency Counting
```python
from collections import defaultdict, Counter

# Using defaultdict
def top_k_frequent_defaultdict(nums: List[int], k: int) -> List[int]:
    count = defaultdict(int)
    for num in nums:
        count[num] += 1
    return sorted(count.keys(), key=lambda x: count[x], reverse=True)[:k]

# Using Counter (more concise)
def top_k_frequent_counter(nums: List[int], k: int) -> List[int]:
    count = Counter(nums)
    return [num for num, _ in count.most_common(k)]
```

### Pattern 2: Graph Building
```python
def build_graph(edges: List[List[int]]) -> Dict[int, List[int]]:
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)  # undirected graph
    return graph
```

### Pattern 3: Grouping
```python
def group_by_property(items: List[str]) -> Dict[int, List[str]]:
    groups = defaultdict(list)
    for item in items:
        key = len(item)  # or any property
        groups[key].append(item)
    return groups
```

### Pattern 4: Sliding Window with Deque
```python
def sliding_window_problem(arr: List[int], k: int) -> List[int]:
    dq = deque()
    result = []
    
    for i in range(len(arr)):
        # Remove elements outside window
        while dq and dq[0] <= i - k:
            dq.popleft()
        
        # Maintain some property (max, min, etc.)
        while dq and should_remove(arr, dq[-1], i):
            dq.pop()
        
        dq.append(i)
        
        if i >= k - 1:
            result.append(arr[dq[0]])
    
    return result
```

## 🚨 Common Pitfalls and Best Practices

### defaultdict Pitfalls
```python
# WRONG: Accessing creates entries
d = defaultdict(int)
if d['nonexistent']:  # This creates d['nonexistent'] = 0!
    pass

# RIGHT: Check membership first
if 'nonexistent' in d and d['nonexistent']:
    pass

# WRONG: Forgetting to handle deletion
d = defaultdict(list)
d['key'].append(1)
d['key'].remove(1)  # List is now empty but key still exists

# RIGHT: Clean up empty entries
if not d['key']:
    del d['key']
```

### deque Pitfalls
```python
# WRONG: Using list for queue operations
queue = []
queue.append(1)  # O(1)
first = queue.pop(0)  # O(n) - expensive!

# RIGHT: Use deque for queue operations
queue = deque()
queue.append(1)  # O(1)
first = queue.popleft()  # O(1) - efficient!
```

### Type Hints Best Practices
```python
# GOOD: Clear and specific
def process_matrix(matrix: List[List[int]]) -> List[List[int]]:
    pass

# BETTER: Use meaningful names
Matrix = List[List[int]]
def process_matrix(matrix: Matrix) -> Matrix:
    pass

# AVOID: Over-complicating simple cases
def add(a, b):  # Fine for simple functions
    return a + b
```

## 🎪 Interview Tips

1. **Import what you need**: `from collections import defaultdict, deque` shows you know the tools
2. **Use type hints for complex returns**: `-> List[List[int]]` makes your intent clear
3. **Explain your choice**: "I'm using defaultdict to avoid KeyError handling"
4. **Know the time complexity**: deque operations are O(1), list.pop(0) is O(n)
5. **Practice the patterns**: frequency counting, graph building, sliding window with deque

## 🏆 Summary

- **`typing`**: Makes your code self-documenting and IDE-friendly
- **`collections.defaultdict`**: Eliminates KeyError, perfect for counting/grouping
- **`collections.deque`**: Efficient double-ended operations, essential for BFS and sliding window
- **`collections.Counter`**: Simplified counting with powerful methods

These libraries are your best friends in technical interviews - they make your code cleaner, more efficient, and demonstrate professional Python knowledge!