# Queue Data Structure

## What is a Queue?

A **queue** is a linear data structure that follows the **First-In-First-Out (FIFO)** principle. The first element added is the first one to be removed.

## Basic Operations

- **Enqueue:** Add an element to the end (tail) of the queue.
- **Dequeue:** Remove and return the element from the front (head) of the queue.
- **Peek/Front:** View the element at the front without removing it.
- **is_empty:** Check if the queue is empty.
- **Size:** Get the number of elements in the queue.

## Implementation

### Using Linked List (Recommended for dynamic size)

- Each node contains a value and a reference to the next node.
- Maintain pointers to both the head (front) and tail (rear) for O(1) enqueue and dequeue.

### Using Array/List (Fixed or dynamic size)

- Use a list with two pointers (front and rear).
- May require shifting elements or using a circular buffer for efficiency.

## Example (Linked List Implementation)

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.head = self.tail = None
        self.size = 0

    def enqueue(self, value):
        new_node = Node(value)
        if not self.tail:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def dequeue(self):
        if not self.head:
            return None
        value = self.head.value
        self.head = self.head.next
        if not self.head:
            self.tail = None
        self.size -= 1
        return value

    def peek(self):
        return self.head.value if self.head else None

    def is_empty(self):
        return self.size == 0
```

## Use Cases

- **Task scheduling** (e.g., printer queue, CPU task scheduling)
- **Breadth-First Search (BFS)** in graphs/trees
- **Buffer management** (e.g., IO Buffers, streaming data)
- **Order processing** (e.g., customer service, ticketing systems)

## Time and Space Complexity

| Operation | Time Complexity | Space Complexity |
| --------- | --------------- | ---------------- |
| Enqueue   | O(1)            | O(n)             |
| Dequeue   | O(1)            | O(n)             |
| Peek      | O(1)            | O(n)             |
| is_empty  | O(1)            | O(n)             |

_n = number of elements in the queue._

## Popular LeetCode Problems

- [232. Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/)
- [933. Number of Recent Calls](https://leetcode.com/problems/number-of-recent-calls/)
- [346. Moving Average from Data Stream](https://leetcode.com/problems/moving-average-from-data-stream/)
- [621. Task Scheduler](https://leetcode.com/problems/task-scheduler/)
- [207. Course Schedule (uses BFS)](https://leetcode.com/problems/course-schedule/)
- [102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)

## Recognizing and Applying Queues: Problem Patterns & Use Cases

### 1. Classic Problems Solvable with Queues

**1. Breadth-First Search (BFS) in Graphs/Trees**  
_Essential Idea:_ Explore nodes level by level or shortest path in unweighted graphs.  
_Queue Use:_ Queue maintains the frontier of nodes to visit next, ensuring FIFO order for level-wise traversal.

**2. Level Order Traversal (Binary Trees/Graphs)**  
_Essential Idea:_ Visit all nodes at each depth before moving to the next.  
_Queue Use:_ Enqueue children as you visit nodes, process all nodes at current level before next.

**3. Shortest Path in Unweighted Graphs**  
_Essential Idea:_ Find the minimum number of steps from source to target.  
_Queue Use:_ BFS with queue ensures shortest path is found first.

**4. Sliding Window Problems**  
_Essential Idea:_ Maintain a window of recent elements (e.g., max/min/average in last k elements).  
_Queue Use:_ Queue (or deque) efficiently tracks elements in the window.

**5. Task Scheduling/Order Processing**  
_Essential Idea:_ Process tasks in the order they arrive (FIFO).  
_Queue Use:_ Enqueue tasks as they arrive, dequeue to process.

**6. Rate Limiting/Recent Requests**  
_Essential Idea:_ Track requests/events in a recent time window.  
_Queue Use:_ Enqueue timestamps, dequeue old ones to maintain window.

**7. Producer-Consumer/Buffer Management**  
_Essential Idea:_ Decouple producers and consumers, buffer data between them.  
_Queue Use:_ Queue stores items produced until consumed.

**8. Implementing Stacks with Queues (and vice versa)**  
_Essential Idea:_ Simulate one data structure using another.  
_Queue Use:_ Use two queues to implement stack operations.

**9. Multi-source BFS / Flood Fill**  
_Essential Idea:_ Start BFS from multiple sources simultaneously.  
_Queue Use:_ Enqueue all sources at start, process in FIFO order.

**10. Topological Sort (Kahn’s Algorithm)**  
_Essential Idea:_ Order tasks given dependencies.  
_Queue Use:_ Enqueue nodes with zero in-degree, process and update neighbors.

**11. Simulating Real-World Queues**  
_Essential Idea:_ Model real-life waiting lines (printer, customer service, etc.).  
_Queue Use:_ Enqueue arrivals, dequeue for service.

**12. Zigzag/Spiral Level Order Traversal**  
_Essential Idea:_ Alternate direction at each level in tree traversal.  
_Queue Use:_ Queue (sometimes with stack/deque) to manage order.

**13. Rotting Oranges/Spread Problems**  
_Essential Idea:_ Model spread of infection/rot/fire in grid.  
_Queue Use:_ Multi-source BFS with queue for time steps.

**14. Jump Game/Minimum Moves**  
_Essential Idea:_ Find minimum jumps/moves to reach target.  
_Queue Use:_ BFS with queue for shortest path in state space.

**15. Simulating Circular Buffers**  
_Essential Idea:_ Fixed-size buffer with wrap-around.  
_Queue Use:_ Circular queue/array for efficient space use.

**16. Windowed Aggregation (Moving Average, etc.)**  
_Essential Idea:_ Compute aggregate over recent k elements.  
_Queue Use:_ Queue maintains current window.

**17. Interleaving/Weaving Queues**  
_Essential Idea:_ Merge or alternate elements from multiple queues.  
_Queue Use:_ Enqueue/dequeue from multiple sources.

**18. Simulating Delays/Timeouts**  
_Essential Idea:_ Model delays in processing (e.g., network, IO).  
_Queue Use:_ Queue holds items until ready for processing.

### 2. Real-World & Interview/LeetCode Queue Problems

- **Implement Queue using Stacks** (LeetCode 232): Simulate queue with two stacks.
- **Number of Recent Calls** (LeetCode 933): Queue for recent timestamps.
- **Moving Average from Data Stream** (LeetCode 346): Queue for sliding window.
- **Task Scheduler** (LeetCode 621): Queue for task order and cooldown.
- **Course Schedule (BFS)** (LeetCode 207): Queue for topological sort.
- **Binary Tree Level Order Traversal** (LeetCode 102): Queue for level-wise traversal.
- **Rotting Oranges** (LeetCode 994): Multi-source BFS with queue.
- **Open the Lock** (LeetCode 752): BFS with queue for shortest path.
- **Perfect Squares** (LeetCode 279): BFS with queue for minimum steps.
- **Sliding Window Maximum** (LeetCode 239): Deque for window max.
- **Walls and Gates** (LeetCode 286): Multi-source BFS with queue.
- **Shortest Path in Binary Matrix** (LeetCode 1091): BFS with queue.
- **Minimum Genetic Mutation** (LeetCode 433): BFS with queue.
- **Jump Game IV** (LeetCode 1345): BFS with queue for minimum jumps.
- **Design Circular Queue** (LeetCode 622): Circular buffer implementation.
- **Design Hit Counter** (LeetCode 362): Queue for recent hits.
- **Sliding Window Median** (LeetCode 480): Queue/deque for window.
- **Snakes and Ladders** (LeetCode 909): BFS with queue for minimum moves.
- **Clone Graph** (LeetCode 133): BFS with queue for traversal.
- **Minimum Time to Collect All Apples in a Tree** (LeetCode 1443): BFS with queue.

_This list covers all classic and modern queue-based problems. If a problem involves processing items in FIFO order, level-wise traversal, sliding windows, or buffering, think of queues!_

---

**Tip:** Practice implementing queues both with arrays and linked lists, and understand their applications in BFS and real-world systems.
