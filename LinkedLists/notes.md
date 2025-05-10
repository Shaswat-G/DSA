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
