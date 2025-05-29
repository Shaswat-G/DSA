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
## Applications of Heaps:
1. **Priority Queues**: Heaps are commonly used to implement priority queues, where elements are processed based on their priority rather than their order of insertion.
2. **Heap Sort**: Heaps can be used to sort elements efficiently by repeatedly extracting the maximum (or minimum) element from the heap.
3. **Graph Algorithms**: Heaps are used in various graph algorithms, such as Dijkstra's shortest path algorithm and Prim's minimum spanning tree algorithm, to efficiently retrieve the next vertex to process.