import random
import time
from typing import List, Callable


class SortingStrategy(ABC):
    @abstractmethod
    def sort(self, data: List[int]) -> List[int]:
        pass

    @abstractmethod
    def get_name(self) -> str:
        pass


class BubbleSortStrategy(SortingStrategy):
    def sort(self, data: List[int]) -> List[int]:
        arr = data.copy()
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

    def get_name(self) -> str:
        return "Bubble Sort"


class QuickSortStrategy(SortingStrategy):
    def sort(self, data: List[int]) -> List[int]:
        arr = data.copy()
        self._quick_sort(arr, 0, len(arr) - 1)
        return arr

    def _quick_sort(self, arr, low, high):
        if low < high:
            pivot = self._partition(arr, low, high)
            self._quick_sort(arr, low, pivot - 1)
            self._quick_sort(arr, pivot + 1, high)

    def _partition(self, arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def get_name(self) -> str:
        return "Quick Sort"


class MergeSortStrategy(SortingStrategy):
    def sort(self, data: List[int]) -> List[int]:
        arr = data.copy()
        self._merge_sort(arr, 0, len(arr) - 1)
        return arr

    def _merge_sort(self, arr, left, right):
        if left < right:
            mid = (left + right) // 2
            self._merge_sort(arr, left, mid)
            self._merge_sort(arr, mid + 1, right)
            self._merge(arr, left, mid, right)

    def _merge(self, arr, left, mid, right):
        left_arr = arr[left : mid + 1]
        right_arr = arr[mid + 1 : right + 1]

        i = j = 0
        k = left

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] <= right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

    def get_name(self) -> str:
        return "Merge Sort"


class PythonSortStrategy(SortingStrategy):
    def sort(self, data: List[int]) -> List[int]:
        return sorted(data)

    def get_name(self) -> str:
        return "Python Built-in Sort"


# Context class
class DataSorter:
    def __init__(self, strategy: SortingStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: SortingStrategy):
        self.strategy = strategy

    def sort_data(self, data: List[int]) -> dict:
        start_time = time.time()
        sorted_data = self.strategy.sort(data)
        end_time = time.time()

        return {
            "sorted_data": sorted_data,
            "algorithm": self.strategy.get_name(),
            "execution_time": end_time - start_time,
            "original_size": len(data),
        }


# Demonstration
def demonstrate_sorting_strategies():
    print("=== Sorting Strategies Comparison ===\n")

    # Create different datasets
    datasets = {
        "Small Random": [random.randint(1, 100) for _ in range(20)],
        "Medium Random": [random.randint(1, 1000) for _ in range(100)],
        "Already Sorted": list(range(1, 101)),
        "Reverse Sorted": list(range(100, 0, -1)),
    }

    strategies = [
        BubbleSortStrategy(),
        QuickSortStrategy(),
        MergeSortStrategy(),
        PythonSortStrategy(),
    ]

    sorter = DataSorter(BubbleSortStrategy())

    for dataset_name, data in datasets.items():
        print(f"--- {dataset_name} Dataset ({len(data)} elements) ---")

        for strategy in strategies:
            sorter.set_strategy(strategy)
            result = sorter.sort_data(data)

            print(f"{result['algorithm']}: {result['execution_time']:.6f} seconds")

        print()


demonstrate_sorting_strategies()
