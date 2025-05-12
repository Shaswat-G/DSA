# Sorting:
Sorting algos are compared based on:
1. **Time Complexity**: How fast the algorithm runs.
2. **Space Complexity**: How much memory the algorithm uses.
3. Number of passes: How many times the algorithm goes through the data.
4. Number of comparisons: How many times the algorithm compares elements - decides time complexity.
5. Number of swaps: How many times the algorithm swaps elements.
6. Stability: Whether the algorithm maintains the relative order of equal elements. (preserving order of duplicates)
7. Adaptivity: Whether the algorithm performs better on partially sorted data.
8. Extra space: Whether the algorithm uses extra space for sorting.

## Classification of Sorting Algorithms
Comparision Based Sorting:
- **O(n²)**: Bubble Sort, Selection Sort, Insertion Sort
- O(n ^ 3/2): Shell Sort
- **O(n log n)**: Merge Sort, Heap Sort, Quick Sort, Tree Sort
- O(n) : Counting Sort, Radix Sort, Bucket Sort - But they use extra space.

## Bubble Sort:
Imagine a bubble rising to the surface. The largest element "bubbles" to the end of the array. Lighter elements rise, while heavier elements sink. This is based on consecutive comparisons and swaps. In each pass, the largest unsorted element is moved to its correct position.


### Analysis

- **Passes:** n-1 (one for each element except the last)
- **Comparisons:** Worst case O(n²), as each element may be compared with all previous elements. (Sigma n-1 = n(n-1)/2)
- **Swaps/Shifts:** Worst case O(n²), as elements may need to be shifted for each insertion. (Sigma n-1 = n(n-1)/2)
- **Time Complexity:**
  - Best: O(n) (already sorted)
  - Average/Worst: O(n²)
- **Space Complexity:** O(1) (in-place)
- **Stability:** Stable (does not change the relative order of equal elements)
- **Adaptivity:** It is not adaptive by nature. Only if we add a flag to check if any swaps were made in a pass, it can be made adaptive. (if no swaps were made, the array is sorted and we can stop)

## Insertion Sort

### What is Insertion?

Insertion refers to placing a new element at its correct position in a sorted array. This involves traversing from the end of the sorted portion, shifting elements right until the correct spot is found, and inserting the element there.

- In arrays, insertion is an O(n) operation due to shifting.
- In linked lists, insertion at head/tail is O(1), but inserting at a specific position is O(n) due to traversal (no shifting required). Thus, insertion is more suited to linked lists.

### Algorithm

1. Consider the first element as sorted.
2. For each subsequent element, compare it with elements in the sorted subarray.
3. Shift larger elements to the right. (not equal, this gives stability)
4. Insert the current element at its correct position.
5. Repeat for all elements.

### Analysis

- **Passes:** n-1 (one for each element after the first)
- **Comparisons:** Worst case O(n²), as each element may be compared with all previous elements. (Sigma n-1 = n(n-1)/2)
- **Swaps/Shifts:** Worst case O(n²), as elements may need to be shifted for each insertion. (Sigma n-1 = n(n-1)/2)
- **Time Complexity:**
  - Best: O(n) (already sorted)
  - Average/Worst: O(n²)
- **Space Complexity:** O(1) (in-place)
- **Stability:** Stable (does not change the relative order of equal elements)
- **Adaptivity:** Adaptive by nature (performs better on partially sorted data)

### Reflections

- Insertion sort is especially efficient for small or nearly sorted datasets.
- It is simple, in-place, stable, and adaptive.
- Not a divide-and-conquer or greedy algorithm.
- Intermediate arrays do not necessarily contain the smallest or largest elements in order.
