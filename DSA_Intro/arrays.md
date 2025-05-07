# Introduction to Data Structures and Algorithms

## RAM

**RAM (Random Access Memory):**  
Volatile memory for temporary storage of data and instructions needed by the CPU. Allows fast, uniform (random) access to any memory location.

- **Storage:** Variables and instructions are loaded from storage (HDD/SSD) into RAM, each at a unique address.
- **Access:** CPU uses memory addresses to fetch/store data. Access time is constant, regardless of location.
- **Types:**
  - **DRAM:** Main memory, slower, needs refreshing.
  - **SRAM:** Faster, used for caches, no refresh needed.
- **Cache Hierarchy:**
  - **L1:** 16–128 KB/core, ~1–4 cycles, fastest, per core.
  - **L2:** 128 KB–1 MB/core, ~4–12 cycles, per core.
  - **L3:** 2–64 MB (shared), ~10–40 cycles, shared.
- **Buses:**
  - **Data Bus:** Bidirectional, data transfer.
  - **Address Bus:** Unidirectional, address transfer.
  - **Control Bus:** Bidirectional, control signals.
- **Memory Units:**  
  Bit (0/1), Byte (8 bits), KB (1,024 B), MB (1,024 KB), GB (1,024 MB), KiB/MiB/GiB (binary multiples).
- **Address Space:**  
  Continuous block, each byte has a unique address.

## CPU Cycle

- **Fetch:** Get instruction from memory.
- **Decode:** Interpret instruction.
- **Execute:** Perform operation.
- **Clock Cycle:** Smallest unit of CPU time, set by clock frequency (Hz/GHz).
- **Performance:** Higher frequency = more cycles/sec, but real speed depends on architecture and memory access.

---

## Arrays

**Array:**  
Fixed-size, contiguous, homogeneous data structure. Each element is stored at a specific memory address.

- **Types:**
  - **Static Array:** Fixed size, set at compile time.
  - **Dynamic Array:** Resizable, allocated at runtime.
  - **Multidimensional:** Arrays of arrays (e.g., 2D matrix).
  - **Sparse Array:** Mostly empty, stored efficiently.
  - **Associative Array:** Key-value pairs (hash table/dictionary).

**Address Calculation:**  
`address = base_address + (index * size_of_element)`

- **Base Address:** Address of first element.
- **Index:** 0-based position.
- **Size of Element:** In bytes (e.g., int = 4B).

**Complexity:**

- **Access:** O(1)
- **Search:** O(n)
- **Insert/Delete (end):** O(1)
- **Insert/Delete (middle):** O(n)
- **Space:** O(n)

**Advantages:**  
Fast access, simple, efficient for static data.

**Traversal Examples:**

- For loop: `for (int i = 0; i < n; i++) arr[i];`
- For-each: `for (int x : arr) x;`
- While: `int i=0; while(i<n) arr[i++];`
- Pointer: `int* p=arr; for(int i=0;i<n;i++) *(p+i);`

---

## Static Arrays: Key Points

- Fixed size, type-safe, fast O(1) access.
- Insertion/deletion at end: O(1); at middle: O(n).
- Used when size is known and fixed.

---

## Suggested Problems

| Problem                             | Difficulty |
| ----------------------------------- | ---------- |
| Remove Duplicates From Sorted Array | Easy       |
| Remove Element                      | Easy       |

---
