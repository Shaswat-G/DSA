### --------------- Parameterised function for recursion ---------------------- ###
# The recursion tree goes from 3,0 -> 2,3 -> 1,5 -> 0,6 then return values are propogated upwards. -> parameters in the function can be used to track recursion state.
from typing import List


def recursive_n_sum(num: int, sum: int) -> int:

    if num == 0:  # base case
        return sum

    else:  # recursive case
        return recursive_n_sum(num - 1, sum + num)


def recursive_facotrial(num: int) -> int:

    if num == 0:
        # Base Case
        return 1

    else:
        # recursive case
        return num * recursive_facotrial(num - 1)


def recursive_reverse_array(array: List) -> None:

    def swap(left, right, array):

        if left >= right:
            return None
        else:
            array[left], array[right] = array[right], array[left]
            swap(left + 1, right - 1, array)
            return None

    swap(0, len(array) - 1, array)

    return None


### --------------- Multiple Recursion Calls ---------------------- ###

# Down-Prop : The recursive case makes the tree to grow and propoagate outwards till you reach the base case which is a leaf node.
# Up-Prop : The leaf nodes return back the calculated value upwards to their parents until it reaches the root.


def fibonacci(n: int) -> int:
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:  # recursive case
        return fibonacci(n - 1) + fibonacci(n - 2)


### -- Print all possible Subsequences ---###
def get_subs(array: List[int]) -> List[List[int]]:

    def rec_subs(array: List[int], current_subs, all_subs, index: int = 0):

        if index == len(array):
            all_subs.append(current_subs.copy())
            return None

        current_subs.append(array[index])
        rec_subs(array, current_subs, all_subs, index + 1)
        current_subs.pop()
        rec_subs(array, current_subs, all_subs, index + 1)

        return all_subs

    all_subs = []
    rec_subs(array, [], all_subs, 0)
    return all_subs


def get_subs_with_sum(sample_array: List[int], target_sum: int) -> List[List[int]]:

    def rec_subs(current_subs, all_subs, array, target_sum, current_sum, index):

        if index == len(array):
            return

        if current_sum == target_sum:
            all_subs.append(current_subs.copy())

        # include
        current_subs.append(array[index])
        rec_subs(
            current_subs,
            all_subs,
            array,
            target_sum,
            current_sum + array[index],
            index + 1,
        )
        # exclude
        current_subs.pop()
        rec_subs(current_subs, all_subs, array, target_sum, current_sum, index + 1)

    all_subs = []
    rec_subs([], all_subs, sample_array, target_sum, 0, 0)

    return all_subs


def get_any_subs_with_sum(sample_array: List[int], target_sum: int) -> List[List[int]]:

    def rec_subs(current_subs, array, target_sum, current_sum, index):

        # base case:
        if index == len(array):
            return False

        if current_sum == target_sum:
            print(current_subs)
            return True

        # Include
        current_subs.append(array[index])
        if rec_subs(
            current_subs, array, target_sum, current_sum + array[index], index + 1
        ):
            return True

        # Exclude
        current_subs.pop()
        if rec_subs(current_subs, array, target_sum, current_sum, index + 1):
            return True

        return False

    rec_subs([], sample_array, target_sum, 0, 0)
    return None


def count_subs_with_sum(sample_array: List[int], target_sum: int) -> int:

    def rec_count_subs(current_subs, array, index, target_sum, current_sum):

        if index == len(array):
            return 0

        count = 0
        if current_sum == target_sum:
            count += 1

        current_subs.append(array[index])
        incl_count = rec_count_subs(
            current_subs, array, index + 1, target_sum, current_sum + array[index]
        )
        current_subs.pop()
        excl_count = rec_count_subs(
            current_subs, array, index + 1, target_sum, current_sum
        )

        return incl_count + excl_count + count

    return rec_count_subs([], sample_array, 0, target_sum, 0)


# Clearly, the learning is we can include and exclude a given index and generate all possible subsequences and collect them in pass-by-references ds like a mutable list.
# Return type of the recursive function will be none.
# For printing any one subs, we can use a bool return type to stop the recursion calls as soon as you encounter a sum(subs) = k.
# For counting, we can use an int return type to return the sum of recursion calls. It follows post order, root (1,0), left then right.


def combination_sum(sample_array: List[int], target_sum: int) -> List[List[int]]:

    def rec_comb(
        current_subs: List,
        array,
        target_sum,
        current_sum,
        all_combinations: List,
        index,
    ):

        if index == len(array) or current_sum > target_sum:
            return None

        if current_sum == target_sum:
            all_combinations.append(current_subs.copy())
            return None

        # Inclusion
        current_element = array[index]
        current_subs.append(current_element)
        rec_comb(
            current_subs,
            array,
            target_sum,
            current_sum + current_element,
            all_combinations,
            index,
        )
        current_subs.pop()
        rec_comb(
            current_subs, array, target_sum, current_sum, all_combinations, index + 1
        )

        return None

    all_combinations = []
    rec_comb([], sample_array, target_sum, 0, all_combinations, 0)
    return all_combinations


def combination_sum_2(candidates: List[int], target_sum: int) -> List[List[int]]:
    candidates.sort()

    def backtrack(
        current_subs: List,
        all_subs: List[List[int]],
        array,
        index,
        current_sum,
        target_sum,
    ):

        # Base Case
        if index == len(array) or current_sum > target_sum:
            return None

        if current_sum == target_sum:
            all_subs.append(current_subs.copy())
            return None

        # Recursive Case

        current_subs.append(array[index])
        backtrack(
            current_subs,
            all_subs,
            array,
            index + 1,
            current_sum + array[index],
            target_sum,
        )
        current_subs.pop()

        while index + 1 < len(array) and array[index] == array[index + 1]:
            index += 1

        backtrack(
            current_subs,
            all_subs,
            array,
            index + 1,
            current_sum,
            target_sum,
        )

        return None

    all_subs = []
    backtrack([], all_subs, candidates, 0, 0, target_sum)
    return all_subs


def all_subset_sums(sample_array: List[int]) -> List[int]:

    def backtrack(current_subs: List, all_sums: List, array: List, index, current_sum):

        # Base Case
        if index == len(array):
            all_sums.append(current_sum)
            return None

        # Recursive Case

        # Include current element
        current_subs.append(array[index])
        backtrack(current_subs, all_sums, array, index + 1, current_sum + array[index])

        # Exclude and Backtrack
        current_subs.pop()
        backtrack(current_subs, all_sums, array, index + 1, current_sum)

        return None

    all_sums = []
    backtrack([], all_sums, sample_array, 0, 0)
    all_sums.sort()
    return all_sums


def all_unique_subsets(sample_array: List[int]) -> List[int]:

    def backtrack(current_subs: List, all_subs: List, array: List, index):

        # Base Case
        if index == len(array):
            all_subs.append(current_subs.copy())
            return None

        # Recusrsive Case
        # Use inclusion and exclusion while ensuring unique elements

        # Inclusion
        current_element = array[index]
        current_subs.append(current_element)
        backtrack(current_subs, all_subs, array, index + 1)

        # Exclusion
        current_subs.pop()
        # Get to the next unique element

        while index < len(array) and array[index] == current_element:
            index += 1

        backtrack(current_subs, all_subs, array, index)

        return None

    sample_array.sort()
    all_subs = []
    backtrack([], all_subs, sample_array, 0)

    return all_subs


def all_permutations(sample_array: List[int]) -> List[List[int]]:

    def backtrack(current_subs, all_perms, used, array):

        if len(current_subs) == len(sample_array) or sum(used) == len(sample_array):
            all_perms.append(current_subs.copy())
            return None

        # Recursive Case
        for index, is_used in enumerate(used):
            if not is_used:
                current_subs.append(array[index])
                used[index] = 1
                backtrack(current_subs, all_perms, used, array)
                used[index] = 0
                current_subs.pop()

    used = [0] * len(sample_array)
    all_perms = []
    backtrack([], all_perms, used, sample_array)
    return all_perms


if __name__ == "__main__":
    # print(recursive_facotrial(5))
    # sample_array = list(range(10))
    # recursive_reverse_array(sample_array)
    # print(sample_array)

    # sample_array = [5, 7, 1, 4]
    # print(get_subs(sample_array))

    sample_array = [1, 2, 3, 4, 5, 6, 7]
    target_sum = 9
    # print(get_subs_with_sum(sample_array, target_sum))

    # get_any_subs_with_sum(sample_array, target_sum)
    # print(count_subs_with_sum(sample_array, target_sum))

    sample_array = [2, 3, 6, 7]
    target_sum = 7
    # print(combination_sum(sample_array, target_sum))

    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    # print(combination_sum_2(candidates, target))

    # print(all_subset_sums(sample_array))

    # print(all_unique_subsets([1, 2, 2, 4]))

    print(all_permutations([1, 2, 3]))

    # print(fibonacci(5))
