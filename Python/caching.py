class Node:
    """Doubly linked list node for LRU cache."""

    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    """
    LRU (Least Recently Used) Cache implementation.

    Uses a combination of:
    - Hash map for O(1) key lookups
    - Doubly linked list for O(1) insertion/deletion and LRU tracking

    Time Complexity: O(1) for both get and put operations
    Space Complexity: O(capacity)
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> node mapping

        # Create dummy head and tail nodes to simplify edge cases
        self.head = Node()  # Most recently used end
        self.tail = Node()  # Least recently used end
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node(self, node):
        """Add node right after head (most recently used position)."""
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        """Remove an existing node from the linked list."""
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    def _move_to_head(self, node):
        """Move node to head (mark as most recently used)."""
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self):
        """Remove and return least recently used node."""
        lru_node = self.tail.prev
        self._remove_node(lru_node)
        return lru_node

    def get(self, key: int) -> int:
        """
        Get value by key. Returns -1 if key doesn't exist.
        Moves accessed item to front (most recently used).
        """
        node = self.cache.get(key)

        if not node:
            return -1

        # Move accessed node to head (mark as recently used)
        self._move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        """
        Insert or update key-value pair.
        If at capacity, removes least recently used item.
        """
        node = self.cache.get(key)

        if not node:
            # Key doesn't exist, create new node
            new_node = Node(key, value)

            if len(self.cache) >= self.capacity:
                # Remove least recently used item
                lru_node = self._pop_tail()
                del self.cache[lru_node.key]

            # Add new node
            self.cache[key] = new_node
            self._add_node(new_node)
        else:
            # Key exists, update value and move to front
            node.value = value
            self._move_to_head(node)

    def display(self):
        """Display current cache state (for debugging)."""
        items = []
        current = self.head.next
        while current != self.tail:
            items.append(f"{current.key}:{current.value}")
            current = current.next
        print(f"Cache (MRU -> LRU): [{' -> '.join(items)}]")


# Alternative: Using Python's OrderedDict (simpler but less educational)
from collections import OrderedDict


class LRUCacheSimple:
    """LRU Cache using OrderedDict - much simpler implementation."""

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        # Move to end (most recently used)
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update existing key
            self.cache.move_to_end(key)
        elif len(self.cache) >= self.capacity:
            # Remove least recently used (first item)
            self.cache.popitem(last=False)

        self.cache[key] = value


# Using Python's built-in functools.lru_cache decorator
from functools import lru_cache


@lru_cache(maxsize=128)
def expensive_function(n):
    """Example of using built-in LRU cache for memoization."""
    print(f"Computing expensive_function({n})")
    # Simulate expensive computation
    result = sum(i * i for i in range(n))
    return result


# Example usage and testing
if __name__ == "__main__":
    print("=== Testing Custom LRU Cache ===")
    lru = LRUCache(3)

    # Test basic operations
    lru.put(1, "one")
    lru.put(2, "two")
    lru.put(3, "three")
    lru.display()  # Should show: 3:three -> 2:two -> 1:one

    print(f"Get 2: {lru.get(2)}")  # Should return "two" and move to front
    lru.display()  # Should show: 2:two -> 3:three -> 1:one

    lru.put(4, "four")  # Should evict 1 (LRU)
    lru.display()  # Should show: 4:four -> 2:two -> 3:three

    print(f"Get 1: {lru.get(1)}")  # Should return -1 (not found)

    print("\n=== Testing functools.lru_cache ===")
    print(expensive_function(100))  # Will compute
    print(expensive_function(100))  # Will use cache
    print(expensive_function(200))  # Will compute
    print(expensive_function.cache_info())  # Show cache statistics
