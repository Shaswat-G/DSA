"""
Recursion Problems

This file contains a collection of recursion problems with their problem statements, function templates, and test cases.

Problem 1: Print Name N Times
Print a given name N times using recursion.

Problem 2: Sum of First N Numbers
Calculate the sum of the first N natural numbers using recursion.

Problem 3: Factorial of a Number
Calculate the factorial of a given number using recursion.

Problem 4: Reverse an Array
Reverse a given array using recursion.

Problem 5: Check Palindrome
Check if a given string is a palindrome using recursion.

Problem 6: Fibonacci Number
Calculate the Nth Fibonacci number using recursion.

Problem 7: Print All Subsequences
Print all subsequences of a given array using recursion.

Problem 8: Subsequence with Sum K
Find all subsequences of a given array whose sum is K using recursion.

Problem 9: Count Subsequences with Sum K
Count the number of subsequences of a given array whose sum is K using recursion.

Problem 10: Combination Sum
Find all unique combinations in an array where the numbers sum to a target.

Problem 11: All Permutations
Generate all permutations of a given array using recursion.

"""

from typing import List


def print_name_n_times(n: int, name: str) -> None:
    """
    Print a given name N times using recursion.

    :param n: int - The number of times to print the name.
    :param name: str - The name to print.
    """
    # TODO: Implement the function
    pass


def sum_of_first_n(n: int) -> int:
    """
    Calculate the sum of the first N natural numbers using recursion.

    :param n: int - The number up to which the sum is calculated.
    :return: int - The sum of the first N natural numbers.
    """
    # TODO: Implement the function
    pass


def factorial(n: int) -> int:
    """
    Calculate the factorial of a given number using recursion.

    :param n: int - The number to calculate the factorial for.
    :return: int - The factorial of the number.
    """
    # TODO: Implement the function
    pass


def reverse_array(array: List[int]) -> List[int]:
    """
    Reverse a given array using recursion.

    :param array: List[int] - The array to reverse.
    :return: List[int] - The reversed array.
    """
    # TODO: Implement the function
    pass


def is_palindrome(s: str) -> bool:
    """
    Check if a given string is a palindrome using recursion.

    :param s: str - The string to check.
    :return: bool - True if the string is a palindrome, False otherwise.
    """
    # TODO: Implement the function
    pass


def fibonacci(n: int) -> int:
    """
    Calculate the Nth Fibonacci number using recursion.

    :param n: int - The position of the Fibonacci number to calculate.
    :return: int - The Nth Fibonacci number.
    """
    # TODO: Implement the function
    pass


def print_all_subsequences(array: List[int]) -> List[List[int]]:
    """
    Print all subsequences of a given array using recursion.

    :param array: List[int] - The input array.
    :return: List[List[int]] - A list of all subsequences.
    """
    # TODO: Implement the function
    pass


def subsequences_with_sum_k(array: List[int], k: int) -> List[List[int]]:
    """
    Find all subsequences of a given array whose sum is K using recursion.

    :param array: List[int] - The input array.
    :param k: int - The target sum.
    :return: List[List[int]] - A list of subsequences whose sum is K.
    """
    # TODO: Implement the function
    pass


def count_subsequences_with_sum_k(array: List[int], k: int) -> int:
    """
    Count the number of subsequences of a given array whose sum is K using recursion.

    :param array: List[int] - The input array.
    :param k: int - The target sum.
    :return: int - The count of subsequences whose sum is K.
    """
    # TODO: Implement the function
    pass


def combination_sum(array: List[int], target: int) -> List[List[int]]:
    """
    Find all unique combinations in an array where the numbers sum to a target.

    :param array: List[int] - The input array.
    :param target: int - The target sum.
    :return: List[List[int]] - A list of unique combinations.
    """
    # TODO: Implement the function
    pass


def all_permutations(array: List[int]) -> List[List[int]]:
    """
    Generate all permutations of a given array using recursion.

    :param array: List[int] - The input array.
    :return: List[List[int]] - A list of all permutations.
    """
    # TODO: Implement the function
    pass


if __name__ == "__main__":
    # Test cases
    print("Test cases for recursion problems")

    # Problem 1: Print Name N Times
    print_name_n_times(5, "Alice")

    # Problem 2: Sum of First N Numbers
    print("Sum of first 5 numbers:", sum_of_first_n(5))

    # Problem 3: Factorial of a Number
    print("Factorial of 5:", factorial(5))

    # Problem 4: Reverse an Array
    print("Reversed array:", reverse_array([1, 2, 3, 4, 5]))

    # Problem 5: Check Palindrome
    print("Is 'racecar' a palindrome?", is_palindrome("racecar"))

    # Problem 6: Fibonacci Number
    print("5th Fibonacci number:", fibonacci(5))

    # Problem 7: Print All Subsequences
    print("All subsequences:", print_all_subsequences([1, 2, 3]))

    # Problem 8: Subsequence with Sum K
    print("Subsequences with sum 5:", subsequences_with_sum_k([1, 2, 3, 4], 5))

    # Problem 9: Count Subsequences with Sum K
    print(
        "Count of subsequences with sum 5:",
        count_subsequences_with_sum_k([1, 2, 3, 4], 5),
    )

    # Problem 10: Combination Sum
    print("Combination sum:", combination_sum([2, 3, 6, 7], 7))

    # Problem 11: All Permutations
    print("All permutations:", all_permutations([1, 2, 3]))
