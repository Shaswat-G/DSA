class Sorter:
    def __init__(self, array : list):
        self.array = array
        self.size = len(array)

    def insertion_sort(self, descending = False) -> None:
        # Assume element at 0 is sorted

        for index in range(1, self.size):
            element = self.array[index]
            cmp_pointer = index -1
            while (element < self.array[cmp_pointer]) and (cmp_pointer >= 0):
                self.array[cmp_pointer + 1] = self.array[cmp_pointer]
                cmp_pointer -= 1
            self.array[cmp_pointer+1] = element
        return None

    def bubble_sort(self, descending = False) -> None:
        for count in range(1, self.size):
            swap_flag = False
            for index in range(0,self.size - count):
                if self.array[index] > self.array[index+1]:
                    temp = self.array[index+1]
                    self.array[index + 1] = self.array[index]
                    self.array[index] = temp
                    swap_flag = True
                
            if not swap_flag:
                break
        return None
    
    def selection_sort(self, descending=False) -> None:
        for count in range(0, self.size-1):
            min_index_yet = count
            for index in range(count+1 ,self.size):
                if self.array[index] < self.array[min_index_yet]:
                    min_index_yet = index
            temp = self.array[count]
            self.array[count] = self.array[min_index_yet]
            self.array[min_index_yet] = temp
        return None
            

    def __len__(self):
        return len(self.size)

    def __str__(self):
        return " | ".join([str(i) for i in self.array])
    
    


def main():
    array = [12,4,7,1,0,2]
    obj = Sorter(array)
    print(f"Gonna do Insertion sort on {obj}")
    obj.insertion_sort()
    print(obj)

    array = [12, 4, 7, 1, 0, 2]
    obj = Sorter(array)
    print(f"Gonna do Bubble sort on {obj}")
    obj.bubble_sort()
    print(obj)
    
    array = [12, 4, 7, 1, 0, 2]
    obj = Sorter(array)
    print(f"Gonna do Selection sort on {obj}")
    obj.selection_sort()
    print(obj)
    
    
    

main()
