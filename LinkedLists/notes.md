# Linked Lists: Comprehensive Notes

## 1. Why Linked Lists?

- **Arrays** offer O(1) random access, but O(n) insertion/deletion (due to shifting).
- **Linked Lists** trade O(1) access for O(1) insertion/deletion (at known positions), enabling dynamic resizing without pre-allocation or costly resizing.
- **Key Insight:** Use linked lists when frequent insertions/deletions are needed, especially at the start/middle.

---

## 2. What is a Linked List?

A dynamic, linear data structure of nodes, where each node contains:

- **Data** (the value)
- **Reference(s)** to next (and possibly previous) node(s)

**Types:**

- **Singly Linked List (SLL):** Each node points to next node.
- **Doubly Linked List (DLL):** Each node points to both next and previous nodes.
- **Circular Linked List:** Last node points back to head (can be singly or doubly).

---

## 3. Helper Functions

- **is_empty:** Check if list is empty.
- **node_at(index):** Retrieve node at a given index (O(n)).
- **is_valid_index(index):** Bounds checking.

**Nugget:** Helper functions encapsulate common checks, reducing bugs and code repetition.

---

## 4. CRUD Operations

| Operation       | SLL Avg | DLL Avg | Array Avg |
| --------------- | ------- | ------- | --------- |
| Access          | O(n)    | O(n)    | O(1)      |
| Insert/Delete\* | O(1)    | O(1)    | O(n)      |
| Search          | O(n)    | O(n)    | O(n)      |

\*At head/tail or with node reference. Arbitrary position requires traversal.

- **Prepend:** Insert at head (O(1))
- **Append:** Insert at tail (O(1) if tail pointer maintained)
- **Insert at index:** O(n) (need to traverse)
- **Delete first/last/at index:** O(1) with pointers, O(n) otherwise

**Nugget:** Maintaining tail pointer in SLL enables O(1) append.

---

## 5. Classification & Tradeoffs

### Singly vs Doubly Linked

- **SLL:** Less memory, simpler, but no backward traversal.
- **DLL:** Bidirectional traversal, easier deletion (given node), but uses more memory.

### Circular vs Non-Circular

- **Circular:** Useful for round-robin, avoids null checks at ends.
- **Non-Circular:** Simpler, more intuitive for most use-cases.

**Nugget:** DLLs are preferred when frequent backward traversal or deletion (not at head) is needed.

---

## 6. Special Operations

### a. Reversal

- **SLL:** Iteratively reverse pointers (O(n)), careful with next/prev tracking.
- **DLL:** Swap next/prev for each node, then swap head/tail.

**Insight:** Always update head/tail after reversal.

### b. Merging Sorted Lists

- Traverse both lists, always append smaller node to result.
- O(n + m) time, O(1) extra space if done in-place.

**Nugget:** Merging is easier if you can manipulate node pointers directly.

### c. Loop Detection

- **Floyd’s Cycle Detection (Tortoise & Hare):** Use two pointers at different speeds.
- If they meet, a loop exists. O(n) time, O(1) space.

### d. Duplicate Removal

- **Unsorted:** Use a hash set to track seen values (O(n) time, O(n) space).
- **Sorted:** Compare current and next, skip duplicates (O(n) time, O(1) space).

### e. Other Useful Operations

- **Find Kth from End:** Use two pointers, k apart.
- **Split/Partition:** Useful for algorithms like quicksort on lists.

---

## 7. Implementation Nuances

- Always handle edge cases: empty list, single node, head/tail updates.
- For deletion, ensure no memory leaks (in languages without GC).
- For circular lists, be careful with traversal to avoid infinite loops.

---

## 8. Pros & Cons

**Pros:**

- Dynamic size, efficient insert/delete at ends.
- No need for contiguous memory.

**Cons:**

- No O(1) random access.
- Extra memory for pointers.
- More complex than arrays for some operations.

---

## 9. When to Use Linked Lists

- When frequent insertions/deletions are required.
- When memory allocation patterns are unpredictable.
- When implementing advanced data structures (queues, stacks, adjacency lists, etc).

---

## 10. Key Takeaways

- Choose the right type (SLL/DLL, circular/non-circular) for your use-case.
- Use helper functions for clarity and safety.
- Always consider time/space tradeoffs.
- Understand the nuances of pointer manipulation to avoid bugs.

---

## 11. Recognizing and Applying Linked Lists: Problem Patterns & Use Cases

### 1. Classic Problems Solvable with Linked Lists

**1. Dynamic Insertion/Deletion (at Head/Tail/Middle)**  
_Essential Idea:_ When you need to insert or delete elements frequently, especially at the start or middle, without shifting elements.  
_Linked List Use:_ O(1) insert/delete at head/tail (with pointers), O(n) at arbitrary position (after traversal).

**2. Implementing Stacks and Queues**  
_Essential Idea:_ Need for dynamic, efficient push/pop (stack) or enqueue/dequeue (queue) operations.  
_Linked List Use:_ SLL for stack (push/pop at head), SLL/DLL for queue (enqueue at tail, dequeue at head).

**3. LRU Cache / MRU Cache**  
_Essential Idea:_ Need to move elements to front/back on access and remove least/most recently used efficiently.  
_Linked List Use:_ DLL with hashmap for O(1) access, insert, and delete.

**4. Reversal of List**  
_Essential Idea:_ Reverse the order of elements in-place.  
_Linked List Use:_ Iterative or recursive pointer manipulation.

**5. Merging Two Sorted Lists**  
_Essential Idea:_ Merge two sorted sequences into one, in-place.  
_Linked List Use:_ Traverse both, relink nodes without extra space.

**6. Detecting and Removing Cycles**  
_Essential Idea:_ Check if a loop exists and remove it.  
_Linked List Use:_ Floyd’s Tortoise & Hare for detection, pointer manipulation for removal.

**7. Finding Intersection/Loop Start**  
_Essential Idea:_ Find the node where two lists intersect or where a cycle begins.  
_Linked List Use:_ Two-pointer techniques, length difference, or cycle detection.

**8. Kth Node from End**  
_Essential Idea:_ Find the kth last element efficiently.  
_Linked List Use:_ Two pointers, k apart.

**9. Partitioning/Splitting Lists**  
_Essential Idea:_ Divide a list into parts (e.g., odd/even, less/greater than x).  
_Linked List Use:_ Relink nodes to new lists without extra space.

**10. Removing Duplicates**  
_Essential Idea:_ Remove repeated elements.  
_Linked List Use:_ Hash set for unsorted, pointer skip for sorted.

**11. Palindrome Check**  
_Essential Idea:_ Check if list reads the same forward and backward.  
_Linked List Use:_ Find middle, reverse second half, compare.

**12. Add Two Numbers (as Lists)**  
_Essential Idea:_ Add numbers where each digit is a node.  
_Linked List Use:_ Traverse both, handle carry, build result.

**13. Rotate/Shift List**  
_Essential Idea:_ Move last k nodes to front.  
_Linked List Use:_ Find new head/tail, relink.

**14. Flattening Nested Lists**  
_Essential Idea:_ Convert multi-level list to single-level.  
_Linked List Use:_ Recursively relink child lists.

**15. Copy List with Random Pointer**  
_Essential Idea:_ Deep copy a list where nodes have extra random pointers.  
_Linked List Use:_ Interleave nodes, then split.

**16. Remove Nth Node from End**  
_Essential Idea:_ Remove the nth last node in one pass.  
_Linked List Use:_ Two pointers, n apart.

**17. Grouping/Segregating Nodes**  
_Essential Idea:_ Group nodes by value (e.g., odd/even, 0/1/2).  
_Linked List Use:_ Multiple pointers, relink nodes.

**18. Circular Buffer/Linked List**  
_Essential Idea:_ Implement round-robin or continuous traversal.  
_Linked List Use:_ Circular SLL/DLL.

**19. Implementing Adjacency Lists (Graphs)**  
_Essential Idea:_ Store variable-length neighbor lists.  
_Linked List Use:_ Each vertex’s neighbors as a linked list.

**20. Skip Lists**  
_Essential Idea:_ Fast search in sorted linked structure.  
_Linked List Use:_ Multi-level linked lists for O(log n) search.

### 2. Real-World & Interview/LeetCode Linked List Problems

- **Reverse Linked List** (LeetCode 206): Reverse pointers.
- **Merge Two Sorted Lists** (LeetCode 21): Merge by relinking.
- **Remove Nth Node From End** (LeetCode 19): Two pointers.
- **Linked List Cycle** (LeetCode 141): Floyd’s cycle detection.
- **Linked List Cycle II** (LeetCode 142): Find cycle start.
- **Intersection of Two Linked Lists** (LeetCode 160): Two pointers, length diff.
- **Palindrome Linked List** (LeetCode 234): Find middle, reverse, compare.
- **Add Two Numbers** (LeetCode 2): Traverse, add, carry.
- **Copy List with Random Pointer** (LeetCode 138): Interleave, split.
- **Rotate List** (LeetCode 61): Find new head/tail, relink.
- **Remove Duplicates from Sorted List** (LeetCode 83, 82): Skip duplicates.
- **Partition List** (LeetCode 86): Relink nodes by value.
- **Odd Even Linked List** (LeetCode 328): Group odd/even indices.
- **Flatten a Multilevel Doubly Linked List** (LeetCode 430): Recursively flatten.
- **LRU Cache** (LeetCode 146): DLL + hashmap.
- **Design Browser History** (LeetCode 1472): DLL for back/forward.
- **Swap Nodes in Pairs** (LeetCode 24): Relink pairs.
- **Reverse Nodes in k-Group** (LeetCode 25): Reverse k at a time.
- **Remove Linked List Elements** (LeetCode 203): Skip nodes by value.
- **Split Linked List in Parts** (LeetCode 725): Partition into k parts.
- **Delete Node in a Linked List** (LeetCode 237): Overwrite and skip.
- **Sort List** (LeetCode 148): Merge sort on list.
- **Insertion Sort List** (LeetCode 147): Insertion sort by relinking.
- **Reorder List** (LeetCode 143): Find middle, reverse, merge.
- **Next Greater Node in Linked List** (LeetCode 1019): Stack + traversal.
- **Swap Nodes in Linked List** (LeetCode 1721): Find and swap.
- **Remove Zero Sum Consecutive Nodes** (LeetCode 1171): Prefix sum + hashmap.

_This list covers all classic and modern linked list problems. If a problem involves dynamic insertion/deletion, pointer manipulation, or sequential node access, think of linked lists!_
