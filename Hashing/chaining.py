# First we create a linked list class
class Node:
    def __init__(self, value : int, next = None):
        self.value = value
        self.next = next


# Then we create a Linked list class

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # Implement helper funcitons

    def is_valid_index(self, index : int) -> bool:
        return 0 <= index < self.size

    def is_empty(self) -> bool:
        return self.size ==0

    def node_at(self, index : int) -> Node:
        assert not self.is_empty() and self.is_valid_index(index)
        current = self.head
        for counter in range(index):
            current = current.next
        return current

    # For hashing we will need insert in sorted LL, delete when found, and searching
    def insert_in_sorted(self, value : int) -> None:
        new_node = Node(value)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node

        else:
            prev_node = None
            current = self.head
            while current and current.value < value:
                prev_node = current
                current = current.next
                # either value is the largest yet and so current is None, prev is tail, or we found a place.
                if not current:
                    # prev_node is at tail
                    prev_node.next = new_node
                    self.tail = new_node
                elif not prev_node:
                    # current is at head
                    new_node.next = current
                    self.head = new_node
                else:
                    # insert in a standard way
                    new_node.next = current
                    prev_node.next = new_node
        self.size +=1
        return

    # Delete if found

    def search(self, value : int) -> int:
        # return index if value is found in sorted LL
        assert not self.is_empty()
        current = self.head

        index = 0
        while current and value > current.value:
            current = current.next
            index += 1

        # current is None
        if not current:
            return -1

        # value <= current
        else:
            if value == current.value:
                return index
            else:
                return -1

    def delete_if_found(self, value : int) -> None:
        assert self.size > 0

        index = self.search(value)
        if index == -1:
            return

        else:
            # deal with single element link lise
            if self.size == 1:
                if index == 0:
                    self.head = None
                    self.tail = None
                else:
                    return
            # deal with normal sized LL
            if index == 0:
                # Implement delete at head
                self.head = self.head.next
            elif index == self.size-1:
                # Implement delete at tail
                second_to_last_node = self.node_at(self.size-2)
                self.tail = second_to_last_node
                self.tail.next = None
            else:
                # Implement general delete
                second_to_search_node = self.node_at(index-1)
                second_to_search_node.next = second_to_search_node.next.next

        self.size -=1
        return

    # We implement python methods for ease

    def __len__(self):
        return self.size

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next

    def __str__(self):
        values = []
        current = self.head
        while current:
            values.append(str(current.value))
            current = current.next

        return "-->".join(values)
    
    
# Now we implement the Hashing class (chaining)
class Hashing:
    def __init__(self, size : int):
        self.size = size
        self.array = [LinkedList() for each_one in range(size)]
        
    def hash(self, key : int) -> int:
        return key % self.size
    
    def insert(self, value : int) -> None:
        return self.array[self.hash(value)].insert_in_sorted(value)
    
    # Implement python methods
    
    def __len__(self):
        return self.size
    
    def __iter__(self):
        for chain in self.array:
            yield chain
            
    def __str__(self):
        string_list = []
        for index, chain in enumerate(self.array):
            string_list.append(f"{index} : {str(chain)}")
            
        return "\n".join(string_list)
            
            
def main():
    hash_table = Hashing(size=10)
    
    for number in range(20):

        hash_table.insert(number)
        
    print(hash_table)


if __name__ == "__main__":
    main()