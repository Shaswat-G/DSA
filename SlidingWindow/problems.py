"""
SLIDING WINDOW PROBLEMS WITH DETAILED SOLUTIONS
============================================

This file contains 10 carefully selected problems that cover all sliding window patterns.
Each solution includes:
- Problem statement
- Intuition and approach
- Step-by-step solution
- Time/Space complexity
- Common pitfalls
"""

from collections import defaultdict, deque
from typing import List

# =============================================================================
# PROBLEM 1: MAXIMUM SUM SUBARRAY OF SIZE K (Fixed Window - Beginner)
# =============================================================================


def max_sum_subarray_size_k(arr: List[int], k: int) -> int:
    """
    Find maximum sum of any contiguous subarray of size k.

    Intuition: Instead of calculating sum for each subarray from scratch,
    slide the window by removing first element and adding next element.

    Example: arr = [2, 1, 5, 1, 3, 2], k = 3
    Windows: [2,1,5]=8, [1,5,1]=7, [5,1,3]=9, [1,3,2]=6
    Answer: 9
    """
    if len(arr) < k:
        return 0

    # Calculate sum of first window
    window_sum = sum(arr[:k])
    max_sum = window_sum

    # Slide the window: remove arr[i-k], add arr[i]
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i - k] + arr[i]
        max_sum = max(max_sum, window_sum)

    return max_sum


# Time: O(n), Space: O(1)
# Pitfall: Don't recalculate sum from scratch each time

# =============================================================================
# PROBLEM 2: LONGEST SUBSTRING WITHOUT REPEATING CHARACTERS (Variable Window)
# =============================================================================


def longest_substring_without_repeating(s: str) -> int:
    """
    Find length of longest substring without repeating characters.

    Intuition: Expand window until we see a duplicate, then contract
    from left until the duplicate is removed.

    Example: s = "abcabcbb"
    Process: a(1) -> ab(2) -> abc(3) -> abca(contract to bca=3) -> bcab(contract to cab=3)...
    Answer: 3 ("abc")
    """
    char_index = {}  # char -> last seen index
    left = 0
    max_len = 0

    for right in range(len(s)):
        char = s[right]

        # If char seen before and is in current window
        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1

        char_index[char] = right
        max_len = max(max_len, right - left + 1)

    return max_len


# Time: O(n), Space: O(min(m,n)) where m is charset size
# Pitfall: Check if duplicate is within current window

# =============================================================================
# PROBLEM 3: MINIMUM WINDOW SUBSTRING (Variable Window + HashMap)
# =============================================================================


def min_window_substring(s: str, t: str) -> str:
    """
    Find minimum window in s that contains all characters of t.

    Intuition: Expand until all chars of t are covered, then contract
    while maintaining coverage to find minimum window.

    Example: s = "ADOBECODEBANC", t = "ABC"
    Answer: "BANC"
    """
    if len(s) < len(t):
        return ""

    # Count characters in t
    t_count = defaultdict(int)
    for char in t:
        t_count[char] += 1

    required = len(t_count)  # unique chars in t
    formed = 0  # chars with desired frequency in current window

    window_count = defaultdict(int)
    left = 0
    min_len = float("inf")
    min_left = 0

    for right in range(len(s)):
        # Expand window
        char = s[right]
        window_count[char] += 1

        if char in t_count and window_count[char] == t_count[char]:
            formed += 1

        # Contract window
        while formed == required:
            # Update minimum window
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_left = left

            # Remove from left
            left_char = s[left]
            window_count[left_char] -= 1
            if left_char in t_count and window_count[left_char] < t_count[left_char]:
                formed -= 1
            left += 1

    return "" if min_len == float("inf") else s[min_left : min_left + min_len]


# Time: O(|s| + |t|), Space: O(|s| + |t|)
# Pitfall: Track 'formed' carefully, not just character counts

# =============================================================================
# PROBLEM 4: LONGEST SUBSTRING WITH AT MOST K DISTINCT CHARACTERS
# =============================================================================


def longest_substring_k_distinct(s: str, k: int) -> int:
    """
    Find longest substring with at most k distinct characters.

    Intuition: Expand window while distinct chars <= k,
    contract when distinct chars > k.

    Example: s = "eceba", k = 2
    Answer: 3 ("ece")
    """
    if k == 0:
        return 0

    char_count = defaultdict(int)
    left = 0
    max_len = 0

    for right in range(len(s)):
        # Expand window
        char_count[s[right]] += 1

        # Contract while distinct chars > k
        while len(char_count) > k:
            left_char = s[left]
            char_count[left_char] -= 1
            if char_count[left_char] == 0:
                del char_count[left_char]
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len


# Time: O(n), Space: O(k)
# Pitfall: Delete character from map when count becomes 0

# =============================================================================
# PROBLEM 5: SLIDING WINDOW MAXIMUM (Advanced - Deque)
# =============================================================================


def sliding_window_maximum(nums: List[int], k: int) -> List[int]:
    """
    Find maximum in each sliding window of size k.

    Intuition: Use deque to maintain potential maximums in decreasing order.
    Front of deque always contains current window's maximum.

    Example: nums = [1,3,-1,-3,5,3,6,7], k = 3
    Answer: [3,3,5,5,6,7]
    """
    if not nums or k == 0:
        return []

    dq = deque()  # stores indices
    result = []

    for i in range(len(nums)):
        # Remove indices outside current window
        while dq and dq[0] <= i - k:
            dq.popleft()

        # Remove indices of smaller elements (they can't be maximum)
        while dq and nums[dq[-1]] <= nums[i]:
            dq.pop()

        dq.append(i)

        # Add maximum of current window to result
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result


# Time: O(n), Space: O(k)
# Pitfall: Deque stores indices, not values

# =============================================================================
# PROBLEM 6: PERMUTATION IN STRING (Fixed Window + HashMap)
# =============================================================================


def check_inclusion(s1: str, s2: str) -> bool:
    """
    Check if s2 contains any permutation of s1.

    Intuition: Sliding window of size len(s1), check if character
    frequencies match at each position.

    Example: s1 = "ab", s2 = "eidbaooo"
    Answer: True (substring "ba" is permutation of "ab")
    """
    if len(s1) > len(s2):
        return False

    s1_count = defaultdict(int)
    for char in s1:
        s1_count[char] += 1

    window_count = defaultdict(int)
    left = 0
    matched = 0

    for right in range(len(s2)):
        # Expand window
        right_char = s2[right]
        window_count[right_char] += 1
        if window_count[right_char] == s1_count[right_char]:
            matched += 1

        # Maintain window size
        if right - left + 1 > len(s1):
            left_char = s2[left]
            if window_count[left_char] == s1_count[left_char]:
                matched -= 1
            window_count[left_char] -= 1
            left += 1

        # Check if permutation found
        if matched == len(s1_count):
            return True

    return False


# Time: O(|s1| + |s2|), Space: O(|s1|)
# Pitfall: Track matched characters, not just counts

# =============================================================================
# PROBLEM 7: LONGEST REPEATING CHARACTER REPLACEMENT
# =============================================================================


def character_replacement(s: str, k: int) -> int:
    """
    Find longest substring with same character after at most k replacements.

    Intuition: For each window, if (window_size - max_frequency) <= k,
    then we can make all characters same with k replacements.

    Example: s = "ABAB", k = 2
    Answer: 4 (replace both B's with A's)
    """
    char_count = defaultdict(int)
    left = 0
    max_len = 0
    max_freq = 0

    for right in range(len(s)):
        # Expand window
        char_count[s[right]] += 1
        max_freq = max(max_freq, char_count[s[right]])

        # Contract if replacements needed > k
        if right - left + 1 - max_freq > k:
            char_count[s[left]] -= 1
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len


# Time: O(n), Space: O(1) - at most 26 characters
# Pitfall: Don't recalculate max_freq on contraction (optimization)

# =============================================================================
# PROBLEM 8: SUBARRAY SUM EQUALS K (Prefix Sum + HashMap)
# =============================================================================


def subarray_sum_k(nums: List[int], k: int) -> int:
    """
    Count number of contiguous subarrays with sum = k.

    Intuition: Use prefix sum. If prefix_sum[j] - prefix_sum[i] = k,
    then subarray from i+1 to j has sum k.

    Example: nums = [1,1,1], k = 2
    Answer: 2 (subarrays [1,1] at positions 0-1 and 1-2)
    """
    prefix_sum = 0
    sum_count = defaultdict(int)
    sum_count[0] = 1  # empty subarray
    result = 0

    for num in nums:
        prefix_sum += num

        # Check if (prefix_sum - k) exists
        if prefix_sum - k in sum_count:
            result += sum_count[prefix_sum - k]

        sum_count[prefix_sum] += 1

    return result


# Time: O(n), Space: O(n)
# Pitfall: Initialize sum_count[0] = 1 for empty prefix

# =============================================================================
# PROBLEM 9: FRUIT INTO BASKETS (At Most 2 Distinct)
# =============================================================================


def total_fruit(fruits: List[int]) -> int:
    """
    Pick maximum fruits with at most 2 types.

    Intuition: Longest subarray with at most 2 distinct elements.
    Same as "Longest Substring with At Most K Distinct Characters" where k=2.

    Example: fruits = [1,2,1]
    Answer: 3 (pick all fruits)
    """
    fruit_count = defaultdict(int)
    left = 0
    max_fruits = 0

    for right in range(len(fruits)):
        # Expand window
        fruit_count[fruits[right]] += 1

        # Contract while more than 2 types
        while len(fruit_count) > 2:
            fruit_count[fruits[left]] -= 1
            if fruit_count[fruits[left]] == 0:
                del fruit_count[fruits[left]]
            left += 1

        max_fruits = max(max_fruits, right - left + 1)

    return max_fruits


# Time: O(n), Space: O(1) - at most 2 fruit types
# Same as longest_substring_k_distinct with k=2

# =============================================================================
# PROBLEM 10: COUNT SUBARRAYS WITH K DIFFERENT INTEGERS (At Most Pattern)
# =============================================================================


def subarrays_with_k_distinct(nums: List[int], k: int) -> int:
    """
    Count subarrays with exactly k distinct integers.

    Intuition: exactly_k = at_most_k - at_most_(k-1)

    Example: nums = [1,2,1,2,3], k = 2
    Answer: 7
    """

    def at_most_k_distinct(nums: List[int], k: int) -> int:
        if k == 0:
            return 0

        count = defaultdict(int)
        left = 0
        result = 0

        for right in range(len(nums)):
            count[nums[right]] += 1

            while len(count) > k:
                count[nums[left]] -= 1
                if count[nums[left]] == 0:
                    del count[nums[left]]
                left += 1

            # All subarrays ending at right
            result += right - left + 1

        return result

    return at_most_k_distinct(nums, k) - at_most_k_distinct(nums, k - 1)


# Time: O(n), Space: O(k)
# Key insight: Use "at most" pattern for "exactly" problems

# =============================================================================
# TESTING FUNCTIONS
# =============================================================================


def test_sliding_window_problems():
    """Test all sliding window problems with sample inputs."""

    print("Testing Sliding Window Problems...")
    print("=" * 50)

    # Test 1: Maximum Sum Subarray
    print("1. Maximum Sum Subarray of Size K:")
    arr1 = [2, 1, 5, 1, 3, 2]
    k1 = 3
    result1 = max_sum_subarray_size_k(arr1, k1)
    print(f"   Input: {arr1}, k={k1}")
    print(f"   Output: {result1} (Expected: 9)")

    # Test 2: Longest Substring Without Repeating
    print("\n2. Longest Substring Without Repeating:")
    s2 = "abcabcbb"
    result2 = longest_substring_without_repeating(s2)
    print(f"   Input: '{s2}'")
    print(f"   Output: {result2} (Expected: 3)")

    # Test 3: Minimum Window Substring
    print("\n3. Minimum Window Substring:")
    s3, t3 = "ADOBECODEBANC", "ABC"
    result3 = min_window_substring(s3, t3)
    print(f"   Input: s='{s3}', t='{t3}'")
    print(f"   Output: '{result3}' (Expected: 'BANC')")

    # Test 4: Longest Substring K Distinct
    print("\n4. Longest Substring with At Most K Distinct:")
    s4, k4 = "eceba", 2
    result4 = longest_substring_k_distinct(s4, k4)
    print(f"   Input: '{s4}', k={k4}")
    print(f"   Output: {result4} (Expected: 3)")

    # Test 5: Sliding Window Maximum
    print("\n5. Sliding Window Maximum:")
    nums5, k5 = [1, 3, -1, -3, 5, 3, 6, 7], 3
    result5 = sliding_window_maximum(nums5, k5)
    print(f"   Input: {nums5}, k={k5}")
    print(f"   Output: {result5}")
    print(f"   Expected: [3, 3, 5, 5, 6, 7]")

    print("\n" + "=" * 50)
    print("All tests completed!")


if __name__ == "__main__":
    test_sliding_window_problems()
