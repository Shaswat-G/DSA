# Introduction to Data Structures and Algorithms

## RAM:

**RAM (Random Access Memory)** is a type of volatile memory used by computers to temporarily store data and instructions that the CPU needs while performing tasks. It allows data to be read or written in almost the same amount of time irrespective of the physical location of data inside the memory.

### How are variables and instructions stored?

- When a program runs, variables and instructions are loaded from storage (like HDD/SSD) into RAM.
- Each variable or instruction occupies a specific location in RAM, identified by a unique address.
- The CPU accesses these addresses directly to read or write data.

### How are they accessed?

- The CPU uses memory addresses to access data in RAM.
- Access time is uniform (random access), unlike sequential access in storage devices like tapes.
- Instructions and variables are fetched from RAM as needed during program execution.

### Types of RAM

- **DRAM (Dynamic RAM):** Needs to be refreshed thousands of times per second. Used as main memory.
- **SRAM (Static RAM):** Faster and more expensive, does not need to be refreshed. Used for cache memory.

### Cache Hierarchy

- **L1 Cache:** Closest to the CPU core, very fast, small size. Often split into L1i (instruction) and L1d (data) caches.
  - **Typical Size:** 16 KB – 128 KB per core
  - **Latency:** ~1–4 CPU cycles
- **L2 Cache:** Larger and a bit slower than L1, shared by one or more cores.
  - **Typical Size:** 128 KB – 1 MB per core
  - **Latency:** ~4–12 CPU cycles
- **L3 Cache:** Even larger, slower, shared across all CPU cores.
  - **Typical Size:** 2 MB – 64 MB (shared)
  - **Latency:** ~10–40 CPU cycles
- Caches store frequently accessed data to speed up processing.

### Buses and Directionality

- **Buses** are communication systems that transfer data between components (CPU, RAM, storage, etc.).
- **Data Bus:** Carries data between CPU and memory (bidirectional).
- **Address Bus:** Carries memory addresses from CPU to memory (unidirectional).
- **Control Bus:** Carries control signals (bidirectional).
- The width of the bus (number of lines) determines how much data can be transferred at once.

### Continuous Memory Space and Address Space

- RAM is organized as a continuous block of memory, each byte having a unique address.
- The **address space** is the range of memory addresses that can be used to access RAM.
- Programs use pointers or references to access specific memory addresses.

### Memory Units

- **Bit:** Smallest unit of data (0 or 1).
- **Byte:** 8 bits.
- **Kilobyte (KB):** 1,024 bytes.
- **Megabyte (MB):** 1,024 KB.
- **Gigabyte (GB):** 1,024 MB.
- **Kibibyte (KiB):** 1,024 bytes (binary prefix).
- **Mebibyte (MiB):** 1,024 KiB.
- **Gibibyte (GiB):** 1,024 MiB.

> Note: GB, MB, KB are decimal (base 10) units, while GiB, MiB, KiB are binary (base 2) units.

---

### CPU Fetch-Decode-Execute Cycle

- The CPU operates in cycles, repeatedly performing three main steps:
  1. **Fetch:** Retrieve the next instruction from memory (RAM or cache).
  2. **Decode:** Interpret the instruction to determine required actions.
  3. **Execute:** Perform the operation (e.g., arithmetic, memory access).
- Each instruction may take one or more **clock cycles** to complete, depending on complexity and memory access.
- **Clock Cycle:** The smallest unit of time in a CPU, determined by the clock frequency.
- **Clock Frequency:** Number of cycles per second, measured in Hertz (Hz). Modern CPUs operate in GHz (billions of cycles per second).
- Higher frequency generally means more instructions can be processed per second, but actual performance depends on many factors (pipeline depth, cache hits/misses, etc.).
