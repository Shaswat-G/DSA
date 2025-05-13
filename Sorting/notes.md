# Sorting

Sorting algorithms are evaluated based on:

1. **Time Complexity:** Speed of execution.
2. **Space Complexity:** Memory usage.
3. **Passes:** Number of full traversals over the data.
4. **Comparisons:** Number of element comparisons (drives time complexity).
5. **Swaps:** Number of element swaps.
6. **Stability:** Preserves the relative order of equal elements.
7. **Adaptivity:** Performs better on partially sorted data.
8. **Extra Space:** Uses additional memory for sorting.

## Classification of Sorting Algorithms

- **O(n²):** Bubble Sort, Selection Sort, Insertion Sort
- **O(n^{3/2}):** Shell Sort
- **O(n log n):** Merge Sort, Heap Sort, Quick Sort, Tree Sort
- **O(n):** Counting Sort, Radix Sort, Bucket Sort (require extra space)

## Bubble Sort

Bubble Sort repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. With each pass, the largest unsorted element "bubbles" to its correct position at the end.

### Bubble Sort Analysis

- **Passes:** n-1
- **Comparisons:** O(n²) worst case (n(n-1)/2)
- **Swaps:** O(n²) worst case (n(n-1)/2)
- **Time Complexity:**
  - Best: O(n) (already sorted, with early exit)
  - Average/Worst: O(n²)
- **Space Complexity:** O(1) (in-place)
- **Stability:** Stable
- **Adaptivity:** Not adaptive by default, but can be made adaptive by adding a flag to stop if no swaps occur in a pass.

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

## Comparing Bubble Sort and Insertion Sort

Both have similar properties in that they are stable, in-place, adaptive and have O(n²) time complexity in the worst case.

Including merge-sort these are the only stable sorting algorithms. Of which insertion and bubble are adaptive.

Bubble is suited for arrays since every intermediate pass gives a sorted array. Insertion is suited for linked lists since it does not require shifting elements, only traversal.

## Selection Sort

Selection Sort repeatedly selects the smallest remaining element and swaps it into its correct position. With each pass, the next smallest element is placed at the start of the unsorted portion.

### Selection Sort Algorithm

1. Start with the first element as the minimum.
2. Iterate through the array to find the smallest element.
3. Swap the smallest element with the first element.
4. Repeat for the rest of the array.

### Selection Sort Analysis

- **Passes:** n-1
- **Comparisons:** O(n²) (n(n-1)/2)
- **Swaps:** O(n) (one swap per pass) — a key advantage over Bubble and Insertion Sort, which can have O(n²) swaps.
- **Time Complexity:**
  - Best: O(n²)
  - Average/Worst: O(n²)
  - No improvement in best case, as the entire array is always scanned.
- **Space Complexity:** O(1) (in-place)
- **Stability:** Not stable (may change the relative order of equal elements)
- **Adaptivity:** Not adaptive (performs the same regardless of initial order)

### Selection Sort Reflections

- Simple and in-place, but not stable or adaptive.
- Useful when minimizing swaps is important.
- After k passes, the first k elements are the k smallest, sorted.


## Quick Sort
Quick Sort is a divide-and-conquer algorithm that sorts an array by selecting a "pivot" element and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. The sub-arrays are then sorted recursively.

### Quick Sort Algorithm
1. Choose a pivot element from the array. (frist, last, middle or random)
2. Partition the array into two sub-arrays:
   - Elements less than the pivot
   - Elements greater than the pivot
   - The pivot itself
3. Recursively apply the same process to the sub-arrays.
4. Combine the sorted sub-arrays and the pivot to get the final sorted array.

### Quick Sort Analysis
- **Passes:** n-1 (for n elements)
- **Comparisons:** O(n log n) average case, O(n²) worst case (when the pivot is the smallest or largest element)
- **Swaps:** O(n log n) average case, O(n²) worst case
- **Time Complexity:**
  - Best: O(n log n) (balanced partitioning) - when the pivot divides the array into two equal halves
  - Average: O(n log n)
  - Worst: O(n²) (unbalanced partitioning)

Clearly, best and worst cases are not simply array configurations. To decide best and worst casse we need to consider whether or not the combination of the pivot and array config result in a balanced partitioning.