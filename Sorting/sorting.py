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
    
    
    # -- helper for quick sort
    
    def _partition(self, low : int, high : int) -> int:
        '''Select a pivot and return the index of the pivot (for partitioning)'''
        pivot_element = self.array[low]
        left_pointer = low + 1
        right_pointer = high
        
        while True:
            # Move the left pointer to the right wherever the element is less than the pivot
            while (left_pointer <= right_pointer) and (self.array[left_pointer] < pivot_element):
                left_pointer += 1
            # Move the right pointer to the left wherever the element is greater than the pivot
            while (left_pointer <= right_pointer) and (self.array[right_pointer] > pivot_element):
                right_pointer -= 1
            
            if left_pointer < right_pointer:
                self.array[left_pointer], self.array[right_pointer] = self.array[right_pointer], self.array[left_pointer]
            else:
                # We have found the partition index
                break
        # Swap the pivot element with the right pointer
        self.array[low], self.array[right_pointer] = self.array[right_pointer], self.array[low]
                
        return right_pointer

    def quick_sort(self, low : int, high : int) -> None:
        ''' Sort the array using quick sort and partition function'''
        if low < high:
            partition_index = self._partition(low, high)
            self.quick_sort(low, partition_index - 1)
            self.quick_sort(partition_index + 1, high)
        return None 

    def __len__(self):
        return self.size

    def __str__(self):
        return " | ".join([str(i) for i in self.array])


def merge_arrays(array1 : list, array2 : list) -> list:
    ''' Merge two sorted arrays into one sorted array'''
    merged_array = []
    index1 = 0
    index2 = 0

    while (index1 < len(array1)) and (index2 < len(array2)):
        if array1[index1] < array2[index2]:
            merged_array.append(array1[index1])
            index1 +=1
        else:
            merged_array.append(array2[index2])
            index2 += 1

    if index1 == len(array1):
        merged_array.extend(array2[index2:])
    else:
        merged_array.extend(array1[index1:])
        
    return merged_array


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

    array = [12, 4, 7, 1, 0, 2]
    obj = Sorter(array)
    print(f"Gonna do quick sort on {obj}")
    obj.quick_sort(0, len(obj.array) - 1)
    print(obj)

    a = [1, 3, 5]
    b = [2, 4, 6]
    print(f"Print the new array {Sorter(merge_arrays(a, b))}")


main()
