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
        while self.is_valid_index(parent_index) and self.array[parent_index] < self.array[index]:
            self.array[parent_index], self.array[index] = self.array[index], self.array[parent_index]
            index = parent_index
            parent_index = self.parent(index)

        return

    def delete(self) -> int:

        return_value = self.array[0]
        self.array[0] = self.array[self.size-1]
        self.size -=1
        self.array.pop() 

        index = 0

        while (self.is_valid_index(self.left(index))):
            
            if (self.is_valid_index(self.right(index))):
                right_child = self.array[self.right(index)]
                left_child = self.array[self.left(index)]
                
                if (right_child > left_child):
                    if self.array[index] < self.array[self.right(index)]:
                        self.array[self.right(index)], self.array[index] = self.array[index], self.array[self.right(index)]
                        index = self.right(index)
                    else:
                        break
                else:
                    if self.array[index] < self.array[self.left(index)]:
                        self.array[self.left(index)], self.array[index] = self.array[index], self.array[self.left(index)]
                        index = self.left(index)
                    else:
                        break
            else:
                if self.array[index] < self.array[self.left(index)]:
                        self.array[self.left(index)], self.array[index] = self.array[index], self.array[self.left(index)]
                        index = self.left(index)
                else:
                    break

        return return_value

    # Pythonic methods
