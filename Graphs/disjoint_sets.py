"""
Disjoint Set Data Structure is also called (Union-Find)

Problem Statement:
The Disjoint Set data structure, also known as Union-Find, is used to efficiently manage a collection of non-overlapping sets. It supports two primary operations:
1. **Find**: Determine which set a particular element belongs to.
2. **Union**: Merge two sets into a single set.

Applications:
- Detecting cycles in an undirected graph.
- Kruskal's algorithm for Minimum Spanning Tree (MST).
- Connected components in a graph.
- Dynamic connectivity problems.

Key Features:
1. **Path Compression**: Optimizes the `find` operation by making nodes point directly to the root of their set, flattening the structure.
2. **Union by Rank/Size**: Optimizes the `union` operation by attaching the smaller tree under the larger tree, minimizing the height of the tree.

Time Complexity:
- Both `find` and `union` operations have an amortized time complexity of O(α(n)), where α(n) is the inverse Ackermann function, which grows very slowly and is nearly constant for practical inputs.

Implementation:
- The Disjoint Set is implemented as a class with methods for `find`, `union`, and utility functions.

"""


class DisjointSet:
    def __init__(self, n: int):
        """
        Initialize the Disjoint Set with `n` elements.

        :param n: int - The number of elements in the set.
        """
        # TODO: Initialize the parent array where each element is its own parent initially
        # TODO: Initialize the rank array to keep track of the rank (or size) of each set
        self.parent = list(range(n))
        self.size = [1] * n  # Size of each set

    def find(self, x: int) -> int:
        """
        Find the root of the set containing `x` with path compression.

        :param x: int - The element to find.
        :return: int - The root of the set containing `x`.
        """
        # TODO: Implement the find operation with path compression

        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> None:
        """
        Union the sets containing `x` and `y` using union by size.

        :param x: int - An element in the first set.
        :param y: int - An element in the second set.
        """
        # TODO: Find the roots of the sets containing `x` and `y`
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            # Union by size
            if self.size[root_x] >= self.size[root_y]:
                self.parent[root_y] = root_x
                self.size[root_x] += self.size[root_y]
            else:
                self.parent[root_x] = root_y
                self.size[root_y] += self.size[root_x]

    def connected(self, x: int, y: int) -> bool:
        """
        Check if `x` and `y` are in the same set.

        :param x: int - An element in the first set.
        :param y: int - An element in the second set.
        :return: bool - True if `x` and `y` are in the same set, False otherwise.
        """
        # TODO: Check if the roots of `x` and `y` are the same
        return self.find(x) == self.find(y)


# Example Usage
if __name__ == "__main__":
    # TODO: Initialize Disjoint Set with 5 elements (0 to 4)
    ds = DisjointSet(5)

    # TODO: Perform union operations
    ds.union(0, 1)
    ds.union(1, 2)
    ds.union(3, 4)

    # TODO: Perform find operations
    print("Find(0):", ds.find(0))  # Should print the root of the set containing 0
    print("Find(3):", ds.find(3))  # Should print the root of the set containing 3

    # TODO: Check connected components
    print(
        "Connected(0, 2):", ds.connected(0, 2)
    )  # True, as 0 and 2 are in the same set
    print(
        "Connected(0, 4):", ds.connected(0, 4)
    )  # False, as 0 and 4 are in different sets

    # TODO: Perform additional union operations and verify connectivity
    ds.union(2, 3)
    print(
        "Connected(0, 4):", ds.connected(0, 4)
    )  # True, as all elements are now connected
