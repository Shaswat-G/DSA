class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.next = next
        self.prev = prev

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # -- helper functions

    def _is_empty(self) -> bool:
        return self.size == 0

    def _is_valid_index(self, index: int) -> bool:
        return (0 <= index < self.size)

    def _node_at(self, index : int) -> Node:
        if self._is_empty():
            return None
        elif self._is_valid_index(index):
            if index <= self.size/2: # closer from head
                current_node = self.head
                for _ in range(index):
                    current_node = current_node.next
                return current_node
            else: # closer from tail
                current_node = self.tail
                for _ in range(self.size - index -1):
                    current_node = current_node.prev
                return current_node
        else:
            return None
        
    # -- CRUD operations
    
