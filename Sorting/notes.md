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

### Bubble Sort Implementation Details

#### Algorithm Steps

1. Start from the beginning of the array.
2. Compare each pair of adjacent elements.
3. If the elements are in the wrong order, swap them.
4. After each pass, the largest unsorted element "bubbles" to its correct position at the end.
5. Repeat for all elements, reducing the unsorted portion by one each time.

#### Purpose of Loops

- **Outer loop:** Controls the number of passes (n-1 passes for n elements).
- **Inner loop:** Iterates through the unsorted portion, comparing and swapping adjacent elements.

#### Indices and Termination

- The inner loop runs from index 0 to `size - count - 1` (where `count` is the current pass).
- After each pass, the last `count` elements are sorted and do not need to be checked again.

#### Edge Cases

- If no swaps occur during a pass, the array is already sorted (adaptive optimization).
- Works for arrays of any size, including empty or single-element arrays.

#### Key Idea / Philosophy

- Simple, intuitive, and easy to implement.
- Not efficient for large datasets.
- Each pass guarantees that the next largest element is placed in its correct position.
- Can be made adaptive by checking for swaps.

---

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

### Insertion Sort Implementation Details

#### Algorithm Steps

1. Assume the first element is sorted.
2. For each subsequent element, store it as the "key".
3. Compare the key with elements in the sorted portion (to its left).
4. Shift larger elements to the right to make space.
5. Insert the key at its correct position.
6. Repeat for all elements.

#### Purpose of Loops

- **Outer loop:** Iterates from the second element to the end (index 1 to n-1).
- **Inner loop:** Moves leftward through the sorted portion, shifting elements as needed.

#### Indices and Termination

- The outer loop index marks the current element to insert.
- The inner loop index moves left from the current position, stopping when the correct spot is found or the start of the array is reached.

#### Edge Cases

- Already sorted arrays: minimal shifts, best-case O(n).
- Empty or single-element arrays: no action needed.
- Stable by design (equal elements are not swapped).

#### Key Idea / Philosophy

- Mimics the way people sort playing cards.
- Efficient for small or nearly sorted datasets.
- In-place, stable, and adaptive.
- Not divide-and-conquer; does not guarantee smallest/largest elements are in place after each pass.

---

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

### Selection Sort Implementation Details

#### Algorithm Steps

1. Start with the first element as the minimum.
2. Scan the unsorted portion to find the smallest element.
3. Swap the smallest element with the first unsorted element.
4. Move the boundary of the sorted portion one step forward.
5. Repeat until the array is sorted.

#### Purpose of Loops

- **Outer loop:** Marks the boundary between sorted and unsorted portions (from 0 to n-2).
- **Inner loop:** Scans the unsorted portion to find the minimum element.

#### Indices and Termination

- The outer loop index marks the current position to fill with the minimum.
- The inner loop index scans from `count+1` to the end.
- After each pass, the sorted portion grows by one.

#### Edge Cases

- Works for arrays of any size.
- Not stable: swapping can change the order of equal elements.
- Not adaptive: always scans the entire unsorted portion.

#### Key Idea / Philosophy

- Minimizes the number of swaps (at most n-1).
- Simple and in-place.
- Useful when swap cost is high.
- After k passes, the first k elements are the k smallest, sorted.

---

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

### Quick Sort Implementation Details

#### Algorithm Steps

1. Choose a pivot element (commonly first, last, middle, or random).
2. Partition the array so that elements less than the pivot are on the left, and elements greater than the pivot are on the right.
3. Place the pivot in its correct sorted position.
4. Recursively apply the same process to the left and right subarrays.
5. Base case: subarrays of size 0 or 1 are already sorted.

#### Purpose of Loops

- **Partitioning loop:** Moves pointers inward, swapping elements to ensure partitioning around the pivot.
- **Recursive calls:** Divide the array into subproblems (left and right of the pivot).

#### Indices and Termination

- Partitioning uses two pointers: left (starts at low+1) and right (starts at high).
- The partitioning loop continues until the pointers cross.
- After partitioning, the pivot is placed at its correct index.
- Recursion terminates when subarray size is 0 or 1 (`low >= high`).

#### Edge Cases

- Worst case occurs when the pivot is always the smallest or largest element (unbalanced partitioning).
- Can be improved by randomizing the pivot or using median-of-three.
- Handles arrays of any size, including empty or single-element arrays.

#### Key Idea / Philosophy

- Divide-and-conquer: partitions the array into smaller subproblems.
- In-place and efficient on average (O(n log n)), but not stable.
- Performance depends on pivot choice and partitioning balance.
- Recursion forms a binary tree of subproblems.

---

## Merge Sort

Merge Sort is a classic **divide-and-conquer** algorithm that sorts an array by recursively dividing it into halves, sorting each half, and then merging the sorted halves back together.

### Divide and Conquer

- **Divide:** Split the array into two halves.
- **Conquer:** Recursively sort each half.
- **Combine:** Merge the two sorted halves into a single sorted array.

This approach breaks a problem into smaller subproblems, solves them independently, and combines their results.

### Top-Down vs Bottom-Up

- **Top-Down (Recursive Merge Sort):** The array is recursively divided into halves until each subarray has one element (base case). Sorting is performed during the merging phase as recursion unwinds.
- **Bottom-Up (Iterative Merge Sort):** The array is viewed as n sorted subarrays of size 1. Adjacent subarrays are merged in pairs, doubling the subarray size each pass, until the whole array is merged.

---

### Recursive Merge Sort (Top-Down)

#### Implementation Steps

1. **Base Case:** If the subarray has one element (`low == high`), it is already sorted.
2. **Divide:** Find the middle index (`mid = (low + high) // 2`).
3. **Recursive Calls:** Recursively sort the left (`low` to `mid`) and right (`mid+1` to `high`) halves.
4. **Merge:** Merge the two sorted halves using a helper function.

#### Indices and Termination

- `low`: Start index of the subarray.
- `high`: End index of the subarray.
- **Termination:** When `low >= high`. If `low > high`, it's an invalid range (edge case).

#### Recursion Tree Example

For array `[5, 2, 4, 7]`:

```
merge_sort(0,3)
├─ merge_sort(0,1)
│  ├─ merge_sort(0,0)
│  └─ merge_sort(1,1)
├─ merge_sort(2,3)
│  ├─ merge_sort(2,2)
│  └─ merge_sort(3,3)
```

Each call splits the array, forming a binary tree of recursive calls.

---

### Iterative Merge Sort (Bottom-Up)

#### Implementation Steps

1. **Initialize subarray size:** Start with `sub_array_size = 1` (each element is a sorted subarray).
2. **Merge Passes:** For each pass, merge adjacent subarrays of size `sub_array_size`.
   - For each pair, calculate:
     - `low`: Start index of the first subarray.
     - `mid`: End index of the first subarray (`low + sub_array_size - 1`).
     - `high`: End index of the second subarray (`low + 2*sub_array_size - 1` or array end).
   - Merge the two subarrays if `mid < high`.
3. **Double subarray size:** After each pass, set `sub_array_size *= 2`.
4. **Terminate:** When `sub_array_size` exceeds array length.

#### Loop Purposes

- **Outer loop:** Controls the size of subarrays to merge.
- **Inner loop:** Iterates over the array, merging adjacent subarrays.

#### Edge Cases

- When the array size is not a power of two, the last subarray may be smaller.
- Ensure indices do not exceed array bounds using `min()`.

---

### Helper Functions

Before implementing merge sort, it's instrumental to implement:

- **Merge Function:** Merges two sorted subarrays into a single sorted array (or merges in place).
- **Index Calculations:** For iterative merge sort, carefully calculate `low`, `mid`, and `high` for each merge.

---

### Summary Table

| Implementation | Approach  | Recursion | Subarray Division | Merge Direction | Space Complexity |
| -------------- | --------- | --------- | ----------------- | --------------- | ---------------- |
| Recursive      | Top-Down  | Yes       | Halves            | Bottom-Up       | O(n)             |
| Iterative      | Bottom-Up | No        | Fixed-size pairs  | Top-Down        | O(n)             |

---

### Example: Merge Sort Steps

Given `[8, 4, 5, 7, 1, 3, 6, 2]`:

**Recursive:**

1. Split into `[8,4,5,7]` and `[1,3,6,2]`
2. Further split until single elements.
3. Merge pairs: `[8,4]` → `[4,8]`, `[5,7]` → `[5,7]`, etc.
4. Merge larger sorted subarrays: `[4,8,5,7]` → `[4,5,7,8]`, etc.
5. Final merge: `[1,2,3,4,5,6,7,8]`

**Iterative:**

1. Merge pairs of size 1: `[8,4]` → `[4,8]`, `[5,7]` → `[5,7]`, etc.
2. Merge pairs of size 2: `[4,8,5,7]` → `[4,5,7,8]`, etc.
3. Continue doubling subarray size until the whole array is merged.

---

### Key Points

- **Merge step** requires O(n) extra space.
- **Recursive merge sort** forms a binary recursion tree.
- **Iterative merge sort** uses nested loops to merge subarrays of increasing size.
- **Helper functions** (like merging two sorted arrays) are essential for both approaches.
- Handles all array sizes, including non-powers of two, via careful index calculations.

---

## Counting Sort

Counting Sort is a non-comparative integer sorting algorithm that sorts elements by counting the number of occurrences of each unique value. It is efficient for sorting integers within a known, limited range.

### Counting Sort Analysis

- **Time Complexity:**
  - Best: O(n + k)
  - Average: O(n + k)
  - Worst: O(n + k)
  - Where n = number of elements, k = range of input (max value)
- **Space Complexity:** O(n + k) (requires extra space for the count array and output array)
- **Stability:** Stable (if implemented with output array)
- **Adaptivity:** Not adaptive (performance does not improve for partially sorted data)
- **Extra Space:** Requires O(k) extra space for the count array

### Counting Sort Implementation Details

#### Algorithm Steps

1. Find the maximum value in the array to determine the range (k).
2. Initialize a count array of size k+1 to zero.
3. Count the occurrences of each element in the input array.
4. (Optional for stable sort) Compute prefix sums in the count array to determine positions.
5. Place each element in its correct position in the output array.
6. Copy the output array back to the original array.

#### Caveats, Sacrifices, and Tradeoffs

- Only works for non-negative integers (or must be adapted for negatives).
- Not suitable for large ranges (large k), as space and time grow with k.
- Very fast for small ranges, but impractical for large or sparse data.
- Not a comparison sort; does not work for arbitrary objects or floating-point numbers.

#### Key Idea / Philosophy

- Sacrifices generality for speed: extremely fast for small integer ranges, but not universal.
- Trades extra space for linear time.

---

## Radix Sort

Radix Sort is a non-comparative sorting algorithm that sorts numbers by processing individual digits. It processes digits from least significant to most significant (LSD) or vice versa (MSD), using a stable sub-sorting algorithm (often counting sort) at each digit position.

### Radix Sort Analysis

- **Time Complexity:**
  - Best: O(d·(n + k))
  - Average: O(d·(n + k))
  - Worst: O(d·(n + k))
  - Where n = number of elements, k = range of digits (e.g., 0-9), d = number of digits in the largest number
- **Space Complexity:** O(n + k) (for buckets or count arrays at each digit pass)
- **Stability:** Stable (if the sub-sorting algorithm is stable)
- **Adaptivity:** Not adaptive
- **Extra Space:** Requires O(n + k) extra space per digit pass

### Radix Sort Implementation Details

#### Algorithm Steps

1. Find the maximum number to determine the number of digits (d).
2. For each digit position (from least significant to most significant):
   - Use a stable sort (like counting sort) to sort the array based on the current digit.
3. After processing all digit positions, the array is sorted.

#### Caveats, Sacrifices, and Tradeoffs

- Only works for integers (or fixed-length strings); not suitable for floating-point numbers or arbitrary objects.
- Performance depends on the number of digits (d) and the range of each digit (k).
- Requires extra space for buckets or count arrays at each digit pass.
- Not comparison-based; can outperform O(n log n) sorts for large n and small d.
- Not adaptive; does not benefit from partially sorted data.

#### Key Idea / Philosophy

- Sacrifices generality for speed: extremely fast for large lists of integers with limited digit length.
- Trades extra space and multiple passes for linear time in practice for many cases.

---
