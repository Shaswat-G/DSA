from typing import List

# Recursion means a function calls itself again (with slightly different parameters) -> calls are made from root to leaf (base case), called downprop.
# results are returned from leaf to root (called up-prop). Stack fills up as function call wait, and then the stack shrinks vertically downwards.

# State tracking via function paramters, no global variable system required.

# Space Complexity - Usually measured by size of the recursion stack or tree. This is not externally used array in the program, but internal to the computer (auxiliary space)


#### --- Single Recursionn ----- ####


def print_name(i: int, num: int) -> None:
    # Base Case
    if i == num:
        return None

    # Recursive Case
    print_name(i + 1, num)
    print(f"Name_{i}")
    return None


# -- Parameterised REcursion -> we track the state by a parameter in the function


def sum_to_n(i: int, sum: int) -> int:
    # Base Case:
    if i == 0:
        return sum

    # Recusive Case:
    return sum_to_n(i - 1, sum + i)


def factorial_parameterised(i: int, product: int) -> int:
    if i == 1:
        return product

    return factorial_parameterised(i - 1, product * i)


def rec_reverse_array(left: int, right: int, array: List) -> List:
    # Base Case:
    if left > right:
        return array

    # Recursive Case:
    array[left], array[right] = array[right], array[left]
    return rec_reverse_array(left + 1, right - 1, array)


def rec_palindrome(s: str, left: int) -> bool:
    # Base Case:
    if left > len(s) / 2:
        return True

    # Recursive Case:
    if s[left] == s[len(s) - left - 1]:
        return rec_palindrome(s, left + 1)

    return False


# -- Mathematical Recursion (follow the math formula) -> the sum is tracked in the return of the function and not a parameter of the function
def sum_n(n: int) -> int:
    if n <= 1:
        return n

    return n + sum_n(n - 1)


def factorial(n: int) -> int:

    if n < 2:
        return 1

    return n * factorial(n - 1)


#### --- Multiple Recursion ---- ####


def print_fibonacci(n: int) -> None:
    # Base Case:
    if n < 3:
        return 1

    # Recursive Case:
    return print_fibonacci(n - 1) + print_fibonacci(n - 2)


### --- All about subsequences, permutation, path sums ---- ###


def print_all_subs(array: List[int]) -> List[List[int]]:

    def rec_subs(
        current_subs: List[int],
        index: int,
        array: List[int],
        collection: List[List[int]],
    ) -> None:
        # Base Case:
        if index == len(array):
            collection.append(current_subs.copy())
            return None

        # Recursive case with Backtracking

        # Include
        current_subs.append(array[index])
        rec_subs(current_subs, index + 1, array, collection)

        # Exclude
        current_subs.pop()
        rec_subs(current_subs, index + 1, array, collection)

        return None

    collection = []
    rec_subs([], 0, array, collection)
    return collection


def all_subs_with_sum_k(array: List[int], target: int) -> List[List[int]]:

    def rec_subs(
        current_subs: List[int],
        current_sum: int,
        target: int,
        index: int,
        array: List[int],
        all_subs: List[List[int]],
    ):

        # Base Case:
        if current_sum == target and index == len(array):
            all_subs.append(current_subs.copy())
            return None

        if index == len(array):
            return None

        # Recursive Case:

        # Include
        current_subs.append(array[index])
        rec_subs(
            current_subs, current_sum + array[index], target, index + 1, array, all_subs
        )

        # Exclude
        current_subs.pop()
        rec_subs(current_subs, current_sum, target, index + 1, array, all_subs)

        return None

    all_subs = []
    rec_subs([], 0, target, 0, array, all_subs)

    return all_subs


# To print only one, we have to remember this pattern. The return type is to be bool.
# Why does this work? As soon as condition is met in the base case, return True.
# This trigger early termincation is it send a true up the stack and avoids any further recursive calls.
def one_subs_with_sum_k(array: List[int], target: int) -> List[List[int]]:

    def rec(current_subs, index, current_sum, target, array) -> bool:

        # Base Case
        if index == len(array):
            if current_sum == target:
                return True
            return False

        # Recursive Case with backtracking
        current_subs.append(array[index])
        if rec(current_subs, index + 1, current_sum + array[index], target, array):
            return True
        current_subs.pop()
        if rec(current_subs, index + 1, current_sum, target, array):
            return True

        return False

    current_subs = []
    rec(current_subs, 0, 0, target, array)
    return current_subs


def count_subs_with_sum_k(array: List[int], target: int) -> List[List[int]]:

    def rec(current_subs, current_sum, index, target, array, count):

        if index == len(array):
            if current_sum == target:
                return 1
            else:
                return 0

        current_subs.append(array[index])
        incl_count = rec(
            current_subs, current_sum + array[index], index + 1, target, array, count
        )
        current_subs.pop()
        excl_count = rec(current_subs, current_sum, index + 1, target, array, count)

        return incl_count + excl_count

    count = rec([], 0, 0, target, array, 0)

    return count


def combination_sum(array: List[int], target: int) -> List[List[int]]:

    def rec(current_subs, index, current_sum, target, array, all_combinations):

        # Base Case
        if index == len(array):
            if current_sum == target:
                all_combinations.append(current_subs.copy())
            return None

        if current_sum > target:
            return None

        # Recursive Case with Backtrack
        current_subs.append(array[index])
        rec(
            current_subs,
            index,
            current_sum + array[index],
            target,
            array,
            all_combinations,
        )
        current_subs.pop()
        rec(
            current_subs,
            index + 1,
            current_sum,
            target,
            array,
            all_combinations,
        )

        return None

    array.sort()
    all_combinations = []
    rec([], 0, 0, target, array, all_combinations)
    return all_combinations


def combination_sum_unique(array: List[int], target: int) -> List[List[int]]:

    def rec(current_subs, index, current_sum, target, array, all_unique_combs):
        # Base Case
        if index == len(array):
            if current_sum == target:
                all_unique_combs.append(current_subs.copy())
            return None

        if current_sum > target:
            return None

        # Recursive Case with Backtracking

        # Include
        current_element = array[index]
        current_subs.append(current_element)
        rec(
            current_subs,
            index + 1,
            current_sum + current_element,
            target,
            array,
            all_unique_combs,
        )

        # Exclude
        current_subs.pop()

        incrementer = 0
        new_index = index + incrementer
        while new_index < len(array) and current_element == array[new_index]:
            incrementer += 1
            new_index = index + incrementer

        rec(
            current_subs,
            index + incrementer,
            current_sum,
            target,
            array,
            all_unique_combs,
        )

    array.sort()  # Sorting is requires so you can linearly traverse till you find the next unique element in the exclude case.
    all_unique_combs = []
    rec([], 0, 0, target, array, all_unique_combs)

    return all_unique_combs


def all_subset_sums(array: List[int]) -> List[int]:
    # power set algorithm first then use recursion

    def rec(current_sum, index, array, all_sums):

        if index == len(array):
            all_sums.add(current_sum)
            return None

        rec(current_sum + array[index], index + 1, array, all_sums)
        rec(current_sum, index + 1, array, all_sums)

        return None

    all_sums = set()
    rec(0, 0, array, all_sums)
    return list(all_sums)


def all_unique_subsets(array: int) -> List[List[int]]:

    def rec(current_subs, index, array, all_subs):

        if index == len(array):
            all_subs.append(current_subs.copy())
            return None

        current_subs.append(array[index])
        rec(current_subs, index + 1, array, all_subs)

        current_subs.pop()
        new_index = index
        while new_index < len(array) and array[new_index] == array[index]:
            new_index += 1

        rec(current_subs, new_index, array, all_subs)

        return None

    all_subs = []
    array.sort()
    rec([], 0, array, all_subs)
    return all_subs


def all_permutations(array: List[int]) -> List[List[int]]:

    def rec(curr_permutation, visited, array, all_permutations):
        # Base Case
        if len(curr_permutation) == len(array):
            all_permutations.append(curr_permutation.copy())
            return

        for i in range(len(array)):
            if visited[i]:
                continue
            # Skip duplicates: only use the first unused occurrence
            if i > 0 and array[i] == array[i - 1] and not visited[i - 1]:
                continue
            visited[i] = True
            curr_permutation.append(array[i])
            rec(curr_permutation, visited, array, all_permutations)
            curr_permutation.pop()
            visited[i] = False

    all_permutations = []
    array.sort()
    visited = [False] * len(array)
    rec([], visited, array, all_permutations)
    return all_permutations


if __name__ == "__main__":
    # print_name(0, num=5)
    # print(sum_to_n(10, 0))
    # print(sum_n(10))

    # print(factorial_parameterised(5, 1))
    # print(factorial(5))

    # print(rec_reverse_array(0, 5, array=[1,2,3,4,5,6]))
    # print(rec_palindrome("race6car", 0))
    # print(print_fibonacci(5))

    sample_array = [3, 7, 8, 1, 2, 10]
    # print(print_all_subs(sample_array))
    # print(all_subs_with_sum_k(sample_array, 10))
    # print(one_subs_with_sum_k(sample_array, 10))
    # print(count_subs_with_sum_k(sample_array, 10))

    # print(combination_sum([2, 3, 5], 8))
    # print(combination_sum_unique([10, 1, 2, 7, 6, 1, 5], 8))

    # print(all_subset_sums(sample_array))
    # print(all_unique_subsets([1, 2, 2]))
    print(all_permutations([1, 2, 3]))
