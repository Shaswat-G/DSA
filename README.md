# DSA: Data Structures & Algorithms Reference

A practical, code-driven guide to mastering Data Structures and Algorithms for interviews, competitive programming, and real-world engineering. This repository features clean Python implementations, concise notes, and curated problem patterns for each topic.

---

## Repository Structure

- `DSA_Intro/` — Foundations, arrays, and core concepts
- `Arrays/`, `LinkedLists/`, `Queues/`, `Trees/`, `Heaps/`, `Hashing/`, `Sorting/`, `Recursion/`, `Graphs/` — Each topic contains:
  - `notes.md`: Theory, patterns, and interview tips
  - `*.py`: Idiomatic Python implementations and sample problems
- `Low-Level-Design/` — OOP and design patterns for system design interviews
- `Python/` — Pythonic DSA idioms and best practices
- `assets/` — Visuals and diagrams

---

## Folder Guide

- `DSA_Intro/` — Quickstart and foundational DSA concepts.
- `Arrays/` — Array operations, patterns, and interview problems.
- `LinkedLists/` — Singly, doubly, and circular linked list implementations and tricks.
- `Queues/` — Queue types, patterns, and real-world use cases.
- `Trees/` — Binary trees, BSTs, traversals, and tree algorithms.
- `Heaps/` — Min/max heaps, heap operations, and heap-based problems.
- `Hashing/` — Hash tables, collision resolution, and hashing patterns.
- `Sorting/` — Classic sorting algorithms and searching techniques.
- `Recursion/` — Recursion patterns, backtracking, and practice problems.
- `Graphs/` — Graph representations, BFS/DFS, and graph algorithms.
- `Low-Level-Design/` — OOP and design patterns for system design interviews.
- `Python/` — Pythonic DSA idioms, tips, and best practices.
- `assets/` — Visual diagrams and supporting images.

---

## Getting Started

1. Clone the repository:

   ```sh
   git clone https://github.com/yourusername/DSA.git
   cd DSA
   ```

2. Explore by topic:

   - Read `notes.md` in each folder for theory and interview patterns
   - Run and modify `*.py` files for hands-on practice

3. Use the curated LeetCode/interview problem lists in each notes file for targeted practice.

---

## Sample Usage

```python
from Heaps.heaps import MinHeap
h = MinHeap()
h.insert(5)
h.insert(2)
h.insert(8)
print(h.extract_min())  # 2

from Graphs.graphs import Graph
G = Graph(5)
G.add_edge(0, 1)
G.add_edge(1, 2)
print(G.bfs(0))
```

---

## Navigation

- Start with `notes.md` for theory and patterns
- Dive into Python files for implementation details
- Use problem lists for focused LeetCode prep
- See `Low-Level-Design/` for design/system rounds
- See `Python/pythonic_notes.md` for Python-specific tips

---

## Topics Covered

- Arrays, Linked Lists, Stacks, Queues, Trees, BSTs, Heaps, Hashing, Sorting, Graphs, Recursion, LLD, and more
- Each topic: Clean code, edge cases, patterns, and real-world applications

---

## Contributing

Pull requests and suggestions are welcome. Open an issue or submit a PR.

---

## License

MIT

---

Ace your interviews. Master the patterns. Write clean code.
