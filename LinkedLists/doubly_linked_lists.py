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
    def prepend(self, value : int) -> None:
        new_node = Node(value, None, self.head)
        if self._is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            self.head = new_node
            
        self.size += 1
        
    def append(self, value : int) -> None:
        new_node = Node(value, self.tail, None)
        if self._is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
         
        self.size +=1   
            
        
    # -- Pythonic methods
    def __len__(self):
        return self.size
    
    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node.value
            current_node = current_node.next
            
    def __str__(self):
        values = []
        current_node = self.head
        while current_node:
            values.append(str(current_node.value))
            current_node = current_node.next
        output = " <--> ".join(values)
        return output
           
        
def main():
    dll = LinkedList()
    for i in range(5):
        dll.prepend(i)
        dll.append(100-i**2)
    print(dll)
    
    
            
main()