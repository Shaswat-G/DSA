class Hashing:

    # Constructor
    def __init__(self, size: int) -> None:
        self.size = size
        self.array = [None for _ in range(self.size)]

    # Helper functions
    def is_valid_index(self, index: int) -> bool:
        return 0 <= index < self.size

    def check_if_empty_at(self, index: int) -> bool:
        assert self.is_valid_index(index)
        return self.array[index] is None

    def check_if_full(self) -> bool:
        return all(slot is not None for slot in self.array)

    # Main operations
    def hash(self, value: int) -> int:
        index = value % self.size
        start_index = index
        while self.array[index] is not None:
            index = (index + 1) % self.size
            if index == start_index:
                raise Exception("Hash table is full")

        return index

    def insert(self, value: int) -> None:
        assert not self.check_if_full()
        self.array[self.hash(value)] = value
        return

    def search(self, value: int) -> int:
        start_index = value % self.size
        index = start_index
        while self.array[index] is not None:
            if self.array[index] == value:
                return index
            index = (index + 1) % self.size
            if index == start_index:
                break
        return -1

    # Pythonic Methsods
    def __len__(self) -> int:
        return self.size

    def __iter__(self):
        for value in self.array:
            yield value

    def __str__(self) -> str:
        return ", ".join([str(value) for value in self.array])


def main():
    print("Linear Probing Hash Table Demo")
    h = Hashing(10)
    # Insert some values
    for value in [15, 25, 35, 5, 7, 18, 28, 38, 48, 58]:
        h.insert(value)
    print("Hash Table:")
    print(h)
    # Search for a few values
    for search_val in [25, 7, 100]:
        idx = h.search(search_val)
        if idx != -1:
            print(f"Value {search_val} found at index {idx}")
        else:
            print(f"Value {search_val} not found in the table.")


if __name__ == "__main__":
    main()
