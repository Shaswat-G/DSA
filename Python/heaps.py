import heapq
from typing import List, Tuple

# Python Heaps (Priority Queues) with heapq
# -----------------------------------------
# Heaps are specialized tree-based data structures that satisfy the heap property.
# In Python, the heapq module provides a min-heap implementation using lists.
# The smallest element is always at index 0.

print("--- 1. Creating and Using a Min-Heap ---")
# Create an empty heap
min_heap = []
heapq.heappush(min_heap, 30)
heapq.heappush(min_heap, 10)
heapq.heappush(min_heap, 20)
heapq.heappush(min_heap, 5)
print(f"Min-heap after pushes: {min_heap}")  # [5, 10, 20, 30]

# Access the smallest element (peek)
print(f"Smallest element (peek): {min_heap[0]}")

# Pop elements (always pops the smallest)
print("Popping all elements (ascending order):")
while min_heap:
    print(heapq.heappop(min_heap), end=" ")
print()

print("\n--- 2. Heapify: Transform List into Heap ---")
nums = [4, 2, 5, 3, 1, 9, 6]
heapq.heapify(nums)
print(f"Heapified list: {nums}")  # heap[0] is smallest

print("\n--- 3. Heap Sort Example ---")


def heap_sort(arr: List[int]) -> List[int]:
    heapq.heapify(arr)
    sorted_list = []
    while arr:
        sorted_list.append(heapq.heappop(arr))
    return sorted_list


unsorted = [7, 2, 5, 3, 1]
print(f"Heap sorted: {heap_sort(unsorted[:])}")  # [1, 2, 3, 5, 7]

print("\n--- 4. Simulating a Max-Heap ---")
# Python's heapq is a min-heap. To simulate a max-heap, push negated values.
max_heap = []
for n in [4, 2, 7, 1, 5]:
    heapq.heappush(max_heap, -n)
print(f"Max-heap (internal, negated): {max_heap}")
print("Popping all elements (descending order):")
while max_heap:
    print(-heapq.heappop(max_heap), end=" ")
print()

print("\n--- 5. Heaps with Tuples (Custom Priority) ---")
# Use (priority, value) tuples for custom sorting
tasks = []
heapq.heappush(tasks, (5, "Write code"))
heapq.heappush(tasks, (1, "Fix bug"))
heapq.heappush(tasks, (3, "Attend meeting"))
print("Tasks by priority (lowest number = highest priority):")
while tasks:
    priority, task = heapq.heappop(tasks)
    print(f"Priority: {priority}, Task: {task}")

print("\n--- 6. Absolute Value Heap Example ---")
nums = [4, -2, 3, -5, 2]
abs_heap = []
for n in nums:
    heapq.heappush(abs_heap, (abs(n), n))
print("Numbers sorted by absolute value (then original value):")
while abs_heap:
    print(heapq.heappop(abs_heap)[1], end=" ")
print()

print("\n--- 7. nsmallest and nlargest Utility Functions ---")
arr = [10, 1, 30, 2, 40, 5]
print(f"3 smallest: {heapq.nsmallest(3, arr)}")  # [1, 2, 5]
print(f"2 largest: {heapq.nlargest(2, arr)}")  # [40, 30]

# With key argument
data = [{"name": "A", "val": 10}, {"name": "B", "val": 5}, {"name": "C", "val": 15}]
print("2 smallest by 'val':", heapq.nsmallest(2, data, key=lambda x: x["val"]))

print("\n--- 8. Heapify Strings ---")
strs = ["banana", "apple", "kiwi", "date"]
heapq.heapify(strs)
print(f"Heapified strings: {strs}")

print("\n--- 9. Heap Use Cases as Functions ---")


def heap_push_and_get_min(heap: List[int], value: int) -> int:
    heapq.heappush(heap, value)
    return heap[0]


def pop_all_from_heap(heap: List[int]) -> List[int]:
    result = []
    while heap:
        result.append(heapq.heappop(heap))
    return result


def get_reverse_sorted(nums: List[int]) -> List[int]:
    max_heap = []
    for n in nums:
        heapq.heappush(max_heap, -n)
    return [-heapq.heappop(max_heap) for _ in range(len(max_heap))]


print(f"Push 3 to [2, 5], min is: {heap_push_and_get_min([2, 5], 3)}")
print(f"Pop all from [4, 1, 3]: {pop_all_from_heap([1, 3, 4])}")
print(f"Reverse sorted [4, 2, 7, 1, 5]: {get_reverse_sorted([4, 2, 7, 1, 5])}")

print("\n--- End of Heap Demo ---")
print("Heaps are essential for efficient priority queue operations in Python!")
