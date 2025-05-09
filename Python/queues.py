from collections import deque

# Python Queues: FIFO, LIFO, and More
# -----------------------------------
# Queues are data structures that follow specific orderings for adding and removing elements.
# The most common are FIFO (First-In, First-Out) and LIFO (Last-In, First-Out, i.e., stack).
# Python provides several ways to implement queues:
# - collections.deque (double-ended queue): Fast, thread-safe, supports FIFO and LIFO.
# - queue.Queue: Thread-safe, for multi-threaded programming.
# - Simple lists: Not efficient for queue operations (O(n) pops from front).

print("--- 1. FIFO Queue with deque ---")
fifo = deque()
fifo.append("a")
fifo.append("b")
fifo.append("c")
print(f"Queue after enqueues: {list(fifo)}")  # ['a', 'b', 'c']

# Dequeue (FIFO)
print(f"Dequeued: {fifo.popleft()}")  # 'a'
print(f"Queue after dequeue: {list(fifo)}")  # ['b', 'c']

# Peek at front
print(f"Front element: {fifo[0]}")  # 'b'

print("\n--- 2. LIFO Queue (Stack) with deque ---")
lifo = deque()
lifo.append(1)
lifo.append(2)
lifo.append(3)
print(f"Stack after pushes: {list(lifo)}")  # [1, 2, 3]

# Pop (LIFO)
print(f"Popped: {lifo.pop()}")  # 3
print(f"Stack after pop: {list(lifo)}")  # [1, 2]

# Peek at top
print(f"Top element: {lifo[-1]}")  # 2

print("\n--- 3. Double-Ended Queue Operations ---")
d = deque([10, 20, 30])
d.appendleft(5)
print(f"After appendleft: {list(d)}")  # [5, 10, 20, 30]
print(f"Popped from right: {d.pop()}")  # 30
print(f"Popped from left: {d.popleft()}")  # 5
print(f"Deque now: {list(d)}")  # [10, 20]

print("\n--- 4. Limiting Queue Size with deque(maxlen) ---")
limited = deque(maxlen=3)
for i in range(5):
    limited.append(i)
    print(f"After appending {i}: {list(limited)}")
# Only last 3 elements are kept

print("\n--- 5. Rotating a deque ---")
rot = deque([1, 2, 3, 4, 5])
rot.rotate(2)
print(f"Rotated right by 2: {list(rot)}")  # [4, 5, 1, 2, 3]
rot.rotate(-3)
print(f"Rotated left by 3: {list(rot)}")  # [2, 3, 4, 5, 1]

print("\n--- 6. queue.Queue for Thread-Safe Queues ---")
import queue

q = queue.Queue()
q.put("task1")
q.put("task2")
print(f"Queue size: {q.qsize()}")
print(f"Is queue empty? {q.empty()}")
print(f"Dequeued: {q.get()}")
print(f"Queue size after get: {q.qsize()}")

print("\n--- 7. PriorityQueue Example ---")
pq = queue.PriorityQueue()
pq.put((2, "low priority"))
pq.put((1, "high priority"))
pq.put((3, "lowest priority"))
while not pq.empty():
    priority, task = pq.get()
    print(f"Priority: {priority}, Task: {task}")

print("\n--- 8. Use Cases ---")


# 1. BFS (Breadth-First Search) uses a queue
def bfs(graph, start):
    visited = set()
    q = deque([start])
    while q:
        node = q.popleft()
        if node not in visited:
            print(f"Visited: {node}")
            visited.add(node)
            q.extend(graph.get(node, []))


graph = {"A": ["B", "C"], "B": ["D"], "C": [], "D": []}
print("BFS traversal:")
bfs(graph, "A")


# 2. Sliding Window Maximum/Minimum
def sliding_window_max(nums, k):
    dq = deque()
    result = []
    for i, num in enumerate(nums):
        while dq and dq[0] <= i - k:
            dq.popleft()
        while dq and nums[dq[-1]] < num:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            result.append(nums[dq[0]])
    return result


nums = [1, 3, -1, -3, 5, 3, 6, 7]
print(f"Sliding window max (k=3): {sliding_window_max(nums, 3)}")

print("\n--- End of Queue Demo ---")
print("Queues are fundamental for scheduling, buffering, and breadth-first algorithms!")
