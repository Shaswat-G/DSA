"""
Ninja Training Problem

Problem Statement:
A Ninja has an ‘N’ Day training schedule. He has to perform one of these three activities (Running, Fighting Practice, or Learning New Moves) each day. There are merit points associated with performing an activity each day. The same activity can’t be performed on two consecutive days. We need to find the maximum merit points the ninja can attain in N Days.

We are given a 2D Array POINTS of size ‘N*3’ which tells us the merit point of specific activity on that particular day. Our task is to calculate the maximum number of merit points that the ninja can earn.

Constraints:
- 1 <= N <= 100
- 1 <= POINTS[i][j] <= 100

Example:
Input: N = 3, POINTS = [[10, 40, 70], [20, 50, 80], [30, 60, 90]]
Output: 210
Explanation: The ninja earns 70 merit points on the 1st day, 50 on the 2nd day, and 90 on the 3rd day.
"""

from typing import List


def ninja_training(n: int, points: List[List[int]]) -> int:
    """
    Calculate the maximum merit points the ninja can earn in N days.

    :param n: int - The number of days.
    :param points: List[List[int]] - A 2D list where points[i][j] represents the merit points for activity j on day i.
    :return: int - The maximum merit points the ninja can earn.
    """

    max_points = 0
    days, activities = len(points), len(points[0])
    mem = [[0 for _ in range(activities)] for _ in range(days)]

    for activity in activities:
        mem[0][activity] = points[0][activity]

    def rec_helper(day, last_activity, cur_sum):
        nonlocal max_points  # <---------------------------------------- Declare as non local variable.

        # Base Case
        if day == n:
            max_points = max(max_points, cur_sum)
            return None

        # Rec Case with BT
        for activity in range(activities):
            if activity == last_activity:
                continue
            rec_helper(day + 1, activity, cur_sum + points[day][activity])

    rec_helper(0, -1, 0)

    return max_points


if __name__ == "__main__":
    # Test cases
    points1 = [[10, 40, 70], [20, 50, 80], [30, 60, 90]]
    print("Test Case 1:", ninja_training(3, points1))  # Expected Output: 210

    points2 = [[18, 11, 19], [4, 13, 7], [1, 8, 13]]
    print("Test Case 2:", ninja_training(3, points2))  # Expected Output: 45

    points3 = [[1, 2, 5], [3, 1, 1], [3, 3, 3]]
    print("Test Case 3:", ninja_training(3, points3))  # Expected Output: 11
