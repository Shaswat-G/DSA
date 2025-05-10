class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def append(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node  # Points to itself
        else:
            new_node.next = self.head
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.tail.next = new_node
            self.head = new_node
        self.size += 1

    def delete_first(self):
        if self.is_empty():
            return None
        removed_value = self.head.value
        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head
        self.size -= 1
        return removed_value

    def delete_last(self):
        if self.is_empty():
            return None
        removed_value = self.tail.value
        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            current = self.head
            while current.next != self.tail:
                current = current.next
            current.next = self.head
            self.tail = current
        self.size -= 1
        return removed_value

    def __len__(self):
        return self.size

    def __iter__(self):
        if self.is_empty():
            return
        current = self.head
        for _ in range(self.size):
            yield current.value
            current = current.next

    def __str__(self):
        if self.is_empty():
            return ""
        values = []
        current = self.head
        for _ in range(self.size):
            values.append(str(current.value))
            current = current.next
        return " -> ".join(values) + " (circular)"


def main():
    cll = CircularLinkedList()
    for i in range(5):
        cll.append(i)
    print("Appended:", cll)
    cll.prepend(100)
    print("Prepended 100:", cll)
    cll.delete_first()
    print("After delete_first:", cll)
    cll.delete_last()
    print("After delete_last:", cll)
    print("Iterate:", list(cll))


main()
