# ======== PLAN ======================
# We are going to implement a hash table using chaining for collision resolution.
# Node class for linked list with key, value and next pointer.
# HashTable class with methods for inserting, searching, and deleting key-value pairs, and handling collisions, resizing.
# Methods: hash function, insert, search, delete, resize, disaply, contains, len
# data structure: array of linked lists, keep track of number of key-value pairs, loading factor and capacity (size of the array).
# ===================================

class Node:
    def __init__(self, key : int, value : int, next = None):
        self.key = key
        self.value = value
        self.next = next


class HashTable:
    def __init__(self, initial_size : int = 16, loading_factor_threshold : float = 0.5):
        self.size = 0    # Num K-V pairs
        self.capacity = initial_size
        self.table = [None] * initial_size
        self.loading_factor_threshold = loading_factor_threshold

    def hash(self, key : int) -> int:
        index = (key % self.capacity)
        return index

    def insert(self, key : int, value : int) -> None:
        index = self.hash(key)
        new_node = Node(key, value)
        head_node = self.table[index]

        # Cases: LL has 0 elements | has finite elements (key is already present | unique key)

        if not head_node:
            self.table[index] = new_node
            self.size += 1

        else:
            # Traverse the linked list from head, if key detected, replace, otw insert at tail
            prev_node =None
            current = head_node

            while current:
                if current.key == key:
                    # replace
                    current.value = value
                    break
                prev_node = current
                current = current.next
            if not current:
                # No key found
                prev_node.next = new_node
                self.size += 1

        if (self.size / self.capacity) > self.loading_factor_threshold:
            self.resize()
        return

    def get(self, key : int) -> int:
        index = self.hash(key)
        head = self.table[index]

        # cases : empty list (return -1) | finite list (traverse and find key return value)
        if not head:
            return -1

        else:
            current = head
            while current:
                if current.key == key:
                    return current.value
                current = current.next
            return -1

    def delete(self, key : int):
        # delete an empty list -> return -1
        # delete in a finite list -> Key found (delete and update size) [single element list -> reset to None] , Key not found (return -1)
        index = self.hash(key)
        head = self.table[index]

        if not head:
            return -1

        else:
            prev_node = None
            current = head
            while current:
                if current.key == key:
                    if not prev_node:
                        # current is head
                        self.table[index] = current.next
                    else:
                        prev_node.next = current.next
                    self.size -= 1
                    return
                prev_node = current
                current = current.next
            return -1

    def resize(self) -> None:
        # triggers a double resize -> rehash
        self.capacity = 2 * self.capacity
        
        nodes = []
        for head in self.table:
            if not head:
                pass
            else:
                current = head
                while current:
                    nodes.append(current)
                    current = current.next
        self.table = [None] * self.capacity
        self.size = 0
        for node in nodes:
            self.insert(node.key, node.value)
            

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def __len__(self) -> int:
        return self.size
