class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # -- helper: _node_at(index), _is_empty, _is_valid_index(index)
    def _is_valid_index(self, index) -> bool:
        return 0 <= index < self.size

    def _node_at(self, index):
        assert self._is_valid_index(index)

        current = self.head
        for _ in range(index):
            current = current.next

        return current

    def _is_empty(self):
        return self.size == 0

    # -- define CRUD operations: prepend, append, insert_at, delete_first, delete_last, delete_at, find
    def prepend(self, value):
        new_node = Node(value, self.head)
        self.head = new_node

        if self._is_empty():
            self.tail = new_node

        self.size += 1

    def append(self, value):
        new_node = Node(value, None)
        if self._is_empty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1

    def insert_at(self, value, index):
        if index == 0:
            self.prepend(value)
        elif index == self.size:
            self.append(value)
        else:
            assert self._is_valid_index(index)
        
            prev_node = self._node_at(index-1)
            current = prev_node.next
            
            new_node = Node(value, current)
            prev_node.next = new_node
            self.size +=1
            
    def delete_first(self):
        if self._is_empty():
            return -1
        
        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            
        self.size -= 1
        
    def delete_last(self):
        if self._is_empty():
            return -1
        
        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self._node_at(self.size-2)
            self.tail.next = None
            
        self.size -= 1
        
    def delete_at(self, index):
        assert self._is_valid_index(index)
        
        if index == 0:
            self.delete_first()
        elif index == (self.size -1):
            self.delete_last()
        else:
            prev_node = self._node_at(index-1)
            current_node = prev_node.next
            prev_node.next = current_node.next
            self.size -=1
            
    def find(self, value) -> int:
        index = -1
        current_node = self.head
        for idx in range(self.size):
            if (current_node.value == value):
                index = idx
                break
            current_node = current_node.next
        return index
    # -- reverse, merge sorted linked lists

    # -- syntactic sugar : __len__, __iter__, __str__

    def __len__(self) -> int:
        return self.size

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next

    def __str__(self) -> str:
        values = []
        current = self.head
        while current:
            values.append(str(current.value))
            current = current.next

        string = " --> ".join(values)
        return string


def main():
    ll = LinkedList()
    ll.prepend(1)
    ll.append(5)
    ll.append(10)
    ll.prepend(2)
    print(ll)
    ll.insert_at(100,2)
    print(ll)


main()
