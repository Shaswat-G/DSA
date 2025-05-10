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

            prev_node = self._node_at(index - 1)
            current = prev_node.next

            new_node = Node(value, current)
            prev_node.next = new_node
            self.size += 1

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
            self.tail = self._node_at(self.size - 2)
            self.tail.next = None

        self.size -= 1

    def delete_at(self, index):
        assert self._is_valid_index(index)

        if index == 0:
            self.delete_first()
        elif index == (self.size - 1):
            self.delete_last()
        else:
            prev_node = self._node_at(index - 1)
            current_node = prev_node.next
            prev_node.next = current_node.next
            self.size -= 1

    def find(self, value) -> int:
        index = -1
        current_node = self.head
        for idx in range(self.size):
            if current_node.value == value:
                index = idx
                break
            current_node = current_node.next
        return index

    # -- reverse, merge sorted linked lists
    def reverse(self):
        if self._is_empty():
            raise ValueError("Cannot reverse an empty linked list.")
        elif self.size == 1:
            pass
        else:
            prev_node = self.head
            current_node = prev_node.next

            while current_node:
                next_node = current_node.next
                current_node.next = prev_node
                prev_node = current_node
                current_node = next_node

            self.head.next = None
            self.tail = self.head
            self.head = prev_node

    @staticmethod
    def merge_sorted(l1, l2):
        """
        Merge two sorted LinkedList instances and return a new sorted LinkedList.
        You need to implement this logic!
        """
        # TODO: Implement merge logic here
        merged = LinkedList()
        node_1 = l1.head
        node_2 = l2.head
        for index in range(l1.size + l2.size):
            if (not node_1) and (not node_2):
                break
            elif (not node_1) and (node_2):
                merged.append(node_2.value)
                node_2 = node_2.next
            elif (node_1) and (not node_2):
                merged.append(node_1.value)
                node_1 = node_1.next
            else:
                if node_1.value <= node_2.value:
                    merged.append(node_1.value)
                    node_1 = node_1.next
                else:
                    merged.append(node_2.value)
                    node_2 = node_2.next
        return merged

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
    ll.insert_at(100, 2)
    print(ll)
    ll.reverse()
    print(ll)

    ll1 = LinkedList()
    ll2 = LinkedList()
    # Example sorted lists
    for v in [1, 3, 5]:
        ll1.append(v)
    for v in [2, 4, 6]:
        ll2.append(v)
    print("List 1:", ll1)
    print("List 2:", ll2)
    merged = LinkedList.merge_sorted(ll1, ll2)
    print("Merged:", merged)


main()
