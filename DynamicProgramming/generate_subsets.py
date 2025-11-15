"""
Generate All Subsets

Problem Statement:
Given an array of distinct integers, return all possible subsets (the power set).

The solution set must not contain duplicate subsets, and the subsets can be returned in any order.

Approaches to Implement:
1. Recursive Backtracking
2. Iterative Approach

Example:
Input: nums = [1, 2, 3]
Output: [[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]

Constraints:
- 1 <= nums.length <= 10
- -10 <= nums[i] <= 10
"""

from typing import List, Tuple, Dict


def generate_subsets_recursive(nums: list[int]) -> list[list[int]]:
    """
    Generate all subsets using recursive backtracking.

    :param nums: list[int] - The input array of distinct integers.
    :return: list[list[int]] - A list of all possible subsets.
    """
    collection = []

    def rec_helper(index: int, current_subs: List[int]) -> None:

        # base case
        if index >= len(nums):
            collection.append(current_subs.copy())
            return

        # Rec case
        candidate_element = nums[index]

        # Include
        current_subs.append(candidate_element)
        rec_helper(index + 1, current_subs)

        # Exclude
        current_subs.pop()
        rec_helper(index + 1, current_subs)

        return None

    rec_helper(0, [])

    return collection


def generate_subsets_iterative(nums: list[int]) -> list[list[int]]:
    """
    Generate all subsets using an iterative approach.

    :param nums: list[int] - The input array of distinct integers.
    :return: list[list[int]] - A list of all possible subsets.
    """
    # TODO: Implement the iterative solution
    pass


if __name__ == "__main__":
    # Test cases
    nums = [1, 2, 3]

    print("Recursive Solution:", generate_subsets_recursive(nums))
    # print("Iterative Solution:", generate_subsets_iterative(nums))
