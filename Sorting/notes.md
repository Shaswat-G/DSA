## Insertion Sort:

### What is an Inssertion?

Inserting refers to inserting a new element at the correct posiiton in the sorted array. This means traversing the array from the end whil shifting the elements to the right until the correct posiiton is foind and isnetting the element at that position.

Therefore inserting is a O(n) operation.

FOr linked lists, we can insert at the head or tail in O(1) time. But if we want to insert at a specific position, we need to traverse the list to find that position. This is O(n) operation. Although no shifting is required. => Insertion is more suited to linked lists.

### The algo:
1. Start from the first element and consider it as sorted. This is the first pass, and the subarray of the first element is already sorted.
2. Take the next element and compare it with the elements in the sorted subarray.
3. Shift the elements in the sorted subarray to the right until you find the correct position for the new element.
4. Insert the new element at the correct position.
5. Repeat steps 2-4 for all elements in the array.

### Analysis:
1. Number of passes: n-1 (one for each element after the first)
2. Number of comparisions: For every element "n" there will be "n-1" comparisions in the worst case. So the total number of comparisions is n(n-1)/2 = O(n^2)
3. Number of swaps: For every element "n" there will be "n-1" swaps in the worst case. So the total number of swaps is n(n-1)/2 = O(n^2)
4. Therefore the time complexity is O(n^2) in the worst case.
5. Best Case: Already sorted O(n) - no swaps, only comparisions.
6. Worst Case: Reverse sorted O(n^2) - all swaps, all comparisions.
7. Average Case: O(n^2) - all swaps, all comparisions.


### Reflections:
Insertion sort is designed for linked lists, since we do not need to shift elements.
5. In Place: The algorithm is in-place because we are not using any extra space. => space complexity is O(1) 
6. Stable: The algorithm is stable because we are not changing the relative order of equal elements.
7. Adaptive: By nature and by design, the algorithm is adaptive because it takes advantage of the existing order in the array. If the array is already sorted, the time complexity is O(n) since we do n-1 comparisins and 0 swaps.
8. Simple iterative, neither greedy nor divide and conquer : The intermediate array is not sorted. The algorithm is not a divide and conquer algorithm. It is a simple iterative algorithm. The intermediate array does not contain any useful informtaion - no smallest or largest element.

