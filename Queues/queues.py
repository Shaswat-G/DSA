class Node:
    """Defines the data and attributes of a node in the queue."""

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Queue:
    """Defines the behaviour of the Queue"""

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # -- Helper Functions

    def is_empty(self) -> bool:
        return self.size == 0

    # -- CRUD Operations: enqueue(value), dequeue(), peek

    def peek(self):
        if self.is_empty():
            return None
        return self.head.value

    def enqueue(self, value) -> None:
        new_node = Node(value, None)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1
        return None

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            value = self.head.value
            self.head = self.head.next

        if self.head is None:
            self.tail = None

        self.size -= 1
        return value

    # -- Pythonic Fucntionality
    def __len__(self):
        return self.size

    def __str__(self):
        result = []
        current_node = self.head
        while current_node:
            result.append(str(current_node.value))
            current_node = current_node.next
        return " -- ".join(result)


# -----------------------------------------
def main():
    q = Queue()
    print("Initial queue (should be empty):", q)
    print("Is empty?", q.is_empty())
    print("Enqueue 10, 20, 30")
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    print("Queue after enqueues:", q)
    print("Peek:", q.peek())
    print("Dequeue:", q.dequeue())
    print("Queue after one dequeue:", q)
    print("Peek:", q.peek())
    print("Dequeue:", q.dequeue())
    print("Dequeue:", q.dequeue())
    print("Queue after all dequeues (should be empty):", q)
    print("Is empty?", q.is_empty())
    print("Peek on empty queue:", q.peek())
    print("Dequeue on empty queue:", q.dequeue())


# -----------------------------------------


main()
