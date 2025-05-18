class Search:
    def __init__(self, array : list[int]):
        self.array = array
        self.size = len(array)
        
    def linear_search(self, target : int) -> int:
        for index in range(self.size):
            if self.array[index] == target:
                return index
        return -1
    
    # Improved linear search
    def linear_search_improved(self, target : int) -> int:
        for index in range(self.size):
            if self.array[index] == target:
                # move the found element to the front
                if index != 0:
                    self.array[index], self.array[0] = self.array[0], self.array[index]
                return index
        return -1
    
    def better_linear_search(self, target : int) -> int:
        # moves the targer one step to the front
        
        for index in range(self.size):
            if self.array[index] == target:
                # move the found element to the front
                if index >= 1:
                    self.array[index], self.array[index - 1] = self.array[index - 1], self.array[index]
                return index
            
        return -1