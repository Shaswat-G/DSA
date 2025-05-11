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

---

**Tip:** Practice implementing queues both with arrays and linked lists, and understand their applications in BFS and real-world systems.
