# We will use lists as arrays in python to represent heaps
# since the root node is at 0, the left child is at 2*i+1 and right child is at 2*i+2
# this means that all the odd indices are left children and all the even indices are right children
# To get the parent, subtract one and floor divide by 2

class Heap:
    def __init__(self) -> None:
        self.size = 0
        self.array = []

    # helper methods
    def is_valid_index(self, index : int) -> bool:
        return 0 <= index < self.size

    def left(self, index : int) -> int:
        assert self.is_valid_index(index)
        left_child = 2*index + 1
        return left_child

    def right(self, index : int) -> int:
        assert self.is_valid_index(index)
        right_child = 2 * index + 2
        return right_child

    def parent(self, index : int) -> int:
        assert self.is_valid_index(index)
        parent = (index -1) // 2
        return parent

    def push(self, value : int) -> None:

        self.array.append(value)
        self.size += 1

        index = self.size-1
        parent_index = self.parent(index)
        while (self.array[parent_index] < self.array[index]) and (self.is_valid_index(parent_index)):
            self.array[parent_index], self.array[index] = self.array[index], self.array[parent_index]
            index = parent_index
            parent_index = self.parent(index)

        return

    # Pythonic methods
