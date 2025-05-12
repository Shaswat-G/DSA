class InsertionSort:
    def __init__(self, array : list):
        self.array = array
        self.size = len(array)

    def sort(self, descending = False) -> None:
        # Assume element at 0 is sorted

        for index in range(1, self.size):
            element = self.array[index]
            cmp_pointer = index -1
            while (element < self.array[cmp_pointer]) and (cmp_pointer >= 0):
                self.array[cmp_pointer + 1] = self.array[cmp_pointer]
                cmp_pointer -= 1
            self.array[cmp_pointer+1] = element
        return None

    def __len__(self):
        return len(self.size)

    def __str__(self):
        return " | ".join([str(i) for i in self.array])


def main():
    array = [12,4,7,1,0,2]
    obj = InsertionSort(array)
    print(obj)
    obj.sort()
    print(obj)

main()
