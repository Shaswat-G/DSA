# Binary Heap

## What is a heap?

Heap is a complete binary tree that satisfies the heap property (max or min). The heap property states that for a max-heap, the value of each node is greater than or equal to (=> duplicates allowed, this is not BST) the values of its children, and for a min-heap, the value of each node is less than or equal to the values of its children.

A complete binary tree is a binary tree in which every level, except possibly the last, is completely filled, and all nodes are as far left as possible. This means that all nodes are filled from left to right, and there are no gaps in the tree - in the array representation, there are no empty slots in the array. => height will always be log(n) (base 2), where n is the number of nodes in the tree.

Elements in a binary tree are stored according to the following rules:

1. The root node is at index 1.
2. For any node at index i:
   - The left child is at index 2i.
   - The right child is at index 2i + 1.
   - The parent is at index floor(i/2).

Heap is not used for searching, as it does not maintain a sorted order like a binary search tree (BST). Instead, it is used for efficient access to the maximum or minimum element.

## Insert in a heap:

To insert a new element into a heap, we follow these steps:

1. Add the element to the next space in the array (maintaining the complete binary tree property).
2. Perform an "up-heap" or "bubble-up" operation to restore the heap property. This involves comparing the newly added element with its parent and swapping them if the heap property is violated. Repeat this process until the heap property is restored.

Clearly, it takes at most log(n) time to insert an element into a heap, where n is the number of elements in the heap. This is because we may need to traverse from the newly added element up to the root, which is at most log(n) levels deep in a complete binary tree.

We can also create a heap in place by inserting each element one by one, which will take O(n log n) time in total. However, there is a more efficient way to build a heap from an array in O(n) time using the "heapify" process.

## Delete in a heap:

From heap you can only delete the root element (maximum in max-heap, minimum in min-heap). Deleting any other element would violate the heap property, as it would not be possible to maintain the complete binary tree structure while ensuring the heap property.
To delete the root element (maximum or minimum) from a heap, we follow these steps:

1. Replace the root element with the last element in the heap.
2. Remove the last element.
3. Perform a "down-heap" or "bubble-down" operation to restore the heap property. This involves comparing the new root with its children and swapping it with the larger (or smaller) child if the heap property is violated. Repeat this process until the heap property is restored.

## Heap Sort:

Heap sort is a comparison-based sorting algorithm that uses a binary heap data structure. The basic idea is to build a max-heap (or min-heap) from the input data, and then repeatedly extract the maximum (or minimum) element from the heap and rebuild the heap until all elements are sorted. This is basically deleting the root element repeatedly. For ascending order, we can use a max-heap, and for descending order, we can use a min-heap.
Heap sort has a time complexity of O(n log n) in the worst case, where n is the number of elements to be sorted. This is because building the heap takes O(n) time, and each extraction takes O(log n) time, and we perform this extraction n times.

## Heapify:

Heapify is the process of converting a binary tree into a heap. This can be done in two ways:

1. Bottom-up approach: Start from the last non-leaf node and perform a "down-heap" operation on each node until the entire tree satisfies the heap property.
2. Top-down approach: Insert each element into the heap one by one, performing "up-heap" operations as necessary.

## Priority Queue:

A priority queue is an abstract data type that supports the following operations:

1. Insert: Add an element to the queue with a given priority.
2. Extract-Max (or Extract-Min): Remove and return the element with the highest (or lowest) priority.
3. Peek: Return the element with the highest (or lowest) priority without removing it.

Priority queues can be implemented using binary heaps, which provide efficient insertion and extraction operations.

## Recognizing and Applying Binary Heaps: Problem Patterns & Use Cases

### 1. Classic Problems Solvable with Binary Heaps

**1. Priority Queue Operations**  
_Essential Idea:_ Maintain a dynamic set where you can efficiently insert, remove, and get the highest/lowest priority element.  
_Heap Use:_ Binary heap provides O(log n) insert and extract-min/max, and O(1) peek.

**2. Heap Sort**  
_Essential Idea:_ Sort an array by repeatedly extracting the max/min.  
_Heap Use:_ Build a heap (O(n)), then extract n times (O(log n) each) for O(n log n) total.

**3. Find K Largest/Smallest Elements**  
_Essential Idea:_ Maintain a running set of the k largest/smallest elements seen so far.  
_Heap Use:_ Use a min-heap of size k for k largest (or max-heap for k smallest). Insert new elements and pop if heap exceeds size k.

**4. Merge K Sorted Lists/Arrays**  
_Essential Idea:_ Always pick the smallest/largest next element among k sources.  
_Heap Use:_ Push the first element of each list into a min-heap. Pop the smallest, push its successor, repeat. O(N log k) time.

**5. Running Median/Median of Data Stream**  
_Essential Idea:_ Maintain the median as numbers arrive.  
_Heap Use:_ Use two heaps: max-heap for lower half, min-heap for upper half. Balance sizes to get median in O(1), insert in O(log n).

**6. Top K Frequent Elements/Words**  
_Essential Idea:_ Find the k most frequent items.  
_Heap Use:_ Count frequencies, then use a min-heap of size k to keep top k frequent items.

**7. Scheduling/Task Management (CPU, Meeting Rooms, etc.)**  
_Essential Idea:_ Always process the next available task/resource.  
_Heap Use:_ Use a min-heap to track earliest end times or next available resources.

**8. Interval Problems (Meeting Rooms, Minimum Platforms, etc.)**  
_Essential Idea:_ Track overlapping intervals efficiently.  
_Heap Use:_ Use a min-heap to keep track of current end times; pop when an interval ends.

**9. Dijkstra’s Shortest Path / Prim’s MST**  
_Essential Idea:_ Always expand the node/edge with the smallest cost.  
_Heap Use:_ Use a min-heap (priority queue) to pick the next node/edge with minimum distance/weight.

**10. Sort Nearly Sorted (K-Sorted) Array**  
_Essential Idea:_ Each element is at most k away from its sorted position.  
_Heap Use:_ Use a min-heap of size k+1 to efficiently sort in O(n log k).

**11. Online Order Statistics (Kth Largest/Smallest in Stream)**  
_Essential Idea:_ Maintain the kth largest/smallest as new elements arrive.  
_Heap Use:_ Min-heap of size k for kth largest; max-heap for kth smallest.

**12. Huffman Coding (Optimal Prefix Codes)**  
_Essential Idea:_ Always combine the two lowest-frequency nodes.  
_Heap Use:_ Use a min-heap to repeatedly extract and merge the two smallest nodes.

**13. Minimum/Maximum Cost to Connect Ropes/Files**  
_Essential Idea:_ Always combine the two smallest ropes/files to minimize total cost.  
_Heap Use:_ Use a min-heap to repeatedly combine the two smallest elements.

**14. Water Trapping (Rain Water Trapping II, Trapping Water in 2D)**  
_Essential Idea:_ Always process the lowest boundary first.  
_Heap Use:_ Use a min-heap to expand from the lowest boundary cells.

**15. Event Simulation (Next Event Processing)**  
_Essential Idea:_ Always process the next event in time order.  
_Heap Use:_ Use a min-heap to keep events sorted by time.

**16. A\* Search (Best-First Search)**  
_Essential Idea:_ Always expand the node with the lowest estimated total cost.  
_Heap Use:_ Use a min-heap as a priority queue for nodes.

**17. Online Merging of Streams**  
_Essential Idea:_ Merge multiple sorted streams in real time.  
_Heap Use:_ Min-heap to always get the next smallest element.

**18. Load Balancing (Assigning Jobs to Machines)**  
_Essential Idea:_ Always assign the next job to the least loaded machine.  
_Heap Use:_ Min-heap to track current loads.

**19. Dynamic Range Queries (Sliding Window Maximum/Minimum)**  
_Essential Idea:_ Maintain the max/min in a moving window.  
_Heap Use:_ Max-heap/min-heap (with lazy deletion or index tracking).

**20. K Closest Points/Elements**  
_Essential Idea:_ Find k points closest to a target.  
_Heap Use:_ Max-heap of size k for closest points (by distance).

### 2. Real-World & Interview/LeetCode Heap Problems

- **Kth Largest Element in an Array** (LeetCode 215): Min-heap of size k.
- **Kth Smallest Element in a Sorted Matrix** (LeetCode 378): Min-heap to merge rows/columns.
- **Find Median from Data Stream** (LeetCode 295): Two heaps (max/min) for running median.
- **Top K Frequent Elements** (LeetCode 347): Min-heap for top k frequencies.
- **Merge k Sorted Lists** (LeetCode 23): Min-heap to merge heads of lists.
- **Meeting Rooms II** (LeetCode 253): Min-heap for end times.
- **Task Scheduler** (LeetCode 621): Max-heap for task frequencies.
- **Sliding Window Maximum** (LeetCode 239): Max-heap (with index tracking).
- **Find K Closest Elements** (LeetCode 658): Max-heap for closest k.
- **Minimum Cost to Connect Sticks** (LeetCode 1167): Min-heap for combining smallest sticks.
- **Trapping Rain Water II** (LeetCode 407): Min-heap for boundary expansion.
- **Dijkstra’s Algorithm** (LeetCode 743, 787): Min-heap for shortest path.
- **Prim’s Minimum Spanning Tree** (LeetCode 1135): Min-heap for edge selection.
- **Sort Characters By Frequency** (LeetCode 451): Max-heap for frequency sorting.
- **Reorganize String** (LeetCode 767): Max-heap for greedy placement.
- **IPO (Initial Public Offering)** (LeetCode 502): Two heaps for capital/profit selection.
- **Kth Smallest Prime Fraction** (LeetCode 786): Min-heap for fraction merging.
- **Smallest Range Covering Elements from K Lists** (LeetCode 632): Min-heap for range tracking.
- **Kth Largest Element in a Stream** (LeetCode 703): Min-heap of size k.
- **Find the Celebrity** (LeetCode 277): Heap not required, but can be adapted for priority.
- **Huffman Encoding** (classic): Min-heap for tree construction.
- **Minimum Number of Refueling Stops** (LeetCode 871): Max-heap for fuel selection.
- **Last Stone Weight** (LeetCode 1046): Max-heap for largest stones.
- **Find Median in a Large File** (external sort): Two heaps for median.

_This list covers nearly all classic and modern heap-based problems. If a problem requires efficiently getting/removing the largest/smallest, or maintaining a dynamic set of top-k, or merging sorted sources, think of heaps!_
