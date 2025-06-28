# Complete Sliding Window Mastery Guide

## 🎯 What is Sliding Window?

Sliding window is an optimization technique that transforms nested loops (often O(n²)) into a single pass solution (O(n)). Instead of recalculating everything from scratch for each position, we maintain a "window" of elements and slide it across the array, updating our result incrementally.

**Key Insight**: We're looking for contiguous subarrays/substrings that satisfy certain conditions.

## 🧠 Core Intuition

Think of sliding window like looking through a window while riding a train:
- You see a portion of the landscape (current window)
- As you move forward, new scenery enters your view (expand window)
- Old scenery disappears (shrink window)
- You're always maintaining some property about what you can see

## 📊 Problem Categories & Templates

### 1. Fixed Size Window

**When to use**: Window size is given or can be determined upfront.

**Template**:
```python
def fixed_window_template(arr, k):
    if len(arr) < k:
        return []
    
    # Initialize window
    window_sum = sum(arr[:k])
    result = [window_sum]
    
    # Slide the window
    for i in range(k, len(arr)):
        # Remove leftmost element, add rightmost element
        window_sum = window_sum - arr[i - k] + arr[i]
        result.append(window_sum)
    
    return result
```

**Example Problems**:
- Maximum sum subarray of size K
- Average of all subarrays of size K
- Maximum/minimum in sliding window

### 2. Variable Size Window (Most Common in Interviews)

**When to use**: Need to find optimal window size based on conditions.

**Template**:
```python
def variable_window_template(arr, condition):
    left = 0
    result = 0  # or float('inf') for minimum problems
    window_state = {}  # track window properties
    
    for right in range(len(arr)):
        # Expand window - add arr[right]
        # Update window_state
        
        # Contract window while condition is violated
        while window_violates_condition(window_state):
            # Remove arr[left] from window
            # Update window_state
            left += 1
        
        # Update result with current valid window
        result = max(result, right - left + 1)  # or min for minimum problems
    
    return result
```

### 3. Sliding Window with HashMap/Counter

**When to use**: Problems involving character/element frequency, anagrams, permutations.

**Template**:
```python
from collections import defaultdict

def sliding_window_with_map(s, pattern):
    if len(s) < len(pattern):
        return False
    
    pattern_count = defaultdict(int)
    for char in pattern:
        pattern_count[char] += 1
    
    window_count = defaultdict(int)
    left = 0
    matched = 0  # number of characters matched
    
    for right in range(len(s)):
        # Expand window
        right_char = s[right]
        window_count[right_char] += 1
        
        if window_count[right_char] == pattern_count[right_char]:
            matched += 1
        
        # Contract window when size exceeds pattern length
        if right - left + 1 > len(pattern):
            left_char = s[left]
            if window_count[left_char] == pattern_count[left_char]:
                matched -= 1
            window_count[left_char] -= 1
            left += 1
        
        # Check if we found a match
        if matched == len(pattern_count):
            return True
    
    return False
```

## 🔍 Key Patterns & When to Use Them

### Pattern 1: "Find Maximum/Minimum Subarray"
- **Clue**: "longest", "maximum", "minimum" subarray with condition
- **Approach**: Variable window, expand greedily, contract when needed
- **Examples**: Longest substring without repeating characters, Maximum sum subarray

### Pattern 2: "Find All Subarrays"
- **Clue**: "all subarrays", "count of subarrays"
- **Approach**: For each valid window, count all possible subarrays
- **Examples**: Count subarrays with sum K, All anagrams in string

### Pattern 3: "Check if Pattern Exists"
- **Clue**: "contains", "permutation", "anagram"
- **Approach**: Fixed or variable window with frequency matching
- **Examples**: Check if string contains permutation, Find anagrams

### Pattern 4: "Two Pointers Variation"
- **Clue**: Two conditions to track simultaneously
- **Approach**: Maintain two different properties in window
- **Examples**: Fruits into baskets, Longest substring with at most K distinct chars

## 💡 Problem-Solving Framework

### Step 1: Identify if it's a Sliding Window Problem
Ask yourself:
- Am I looking for contiguous elements?
- Can I avoid recalculating everything from scratch?
- Is there a way to incrementally update my answer?

### Step 2: Choose the Right Template
- **Fixed size**: Window size is given
- **Variable size**: Need to find optimal window
- **With HashMap**: Frequency/character problems

### Step 3: Define Window Properties
- What am I tracking in the window?
- How do I expand the window?
- When do I contract the window?
- How do I update the result?

### Step 4: Handle Edge Cases
- Empty array/string
- Window size larger than array
- All elements satisfy/violate condition

## 🚨 Common Pitfalls & How to Avoid Them

### 1. Off-by-One Errors
**Problem**: Incorrect window size calculation
**Solution**: Always use `right - left + 1` for window size

### 2. Forgetting to Update Window State
**Problem**: Not updating HashMap/counters when expanding/contracting
**Solution**: Always pair element addition with state update

### 3. Incorrect Contraction Logic
**Problem**: Contracting too much or too little
**Solution**: Use `while` loop for contraction, not `if`

### 4. Not Handling Empty Windows
**Problem**: Accessing elements when window is empty
**Solution**: Check window size before accessing elements

### 5. Frequency Count Errors
**Problem**: Negative counts or incorrect matching logic
**Solution**: Use `defaultdict(int)` and careful increment/decrement

## 🏆 Advanced Techniques

### Technique 1: At Most K Pattern
```python
def at_most_k_distinct(s, k):
    count = defaultdict(int)
    left = 0
    result = 0
    
    for right in range(len(s)):
        count[s[right]] += 1
        
        while len(count) > k:
            count[s[left]] -= 1
            if count[s[left]] == 0:
                del count[s[left]]
            left += 1
        
        result += right - left + 1  # Add all subarrays ending at right
    
    return result

# To find "exactly K", use: at_most_k(s, k) - at_most_k(s, k-1)
```

### Technique 2: Multiple Conditions
```python
def sliding_window_multiple_conditions(arr, condition1, condition2):
    left = 0
    state1, state2 = 0, 0
    result = 0
    
    for right in range(len(arr)):
        # Update both conditions
        state1 += arr[right]
        state2 = max(state2, arr[right])
        
        # Contract while either condition is violated
        while state1 > condition1 or state2 > condition2:
            state1 -= arr[left]
            # Recalculate state2 if needed (might require additional data structure)
            left += 1
        
        result = max(result, right - left + 1)
    
    return result
```

## 📝 Practice Problems by Category

### Beginner Level
1. **Maximum Sum Subarray of Size K** (Fixed window)
2. **Find Average of All Subarrays of Size K** (Fixed window)
3. **Longest Subarray with Sum K** (Variable window)

### Intermediate Level
4. **Longest Substring Without Repeating Characters** (Variable + HashMap)
5. **Find All Anagrams in a String** (Fixed + HashMap)
6. **Longest Substring with At Most K Distinct Characters** (Variable + HashMap)
7. **Minimum Window Substring** (Variable + HashMap)

### Advanced Level
8. **Sliding Window Maximum** (Deque optimization)
9. **Longest Substring with At Most K Zeros** (Variable with condition)
10. **Count Subarrays with K Different Integers** (At most K pattern)

## 🎯 Interview Tips

### Before Coding:
1. **Clarify the problem**: What exactly are we optimizing for?
2. **Identify the pattern**: Fixed vs variable window?
3. **Choose data structures**: Do we need HashMap, Set, or just variables?
4. **Discuss edge cases**: Empty input, single element, etc.

### While Coding:
1. **Start with brute force**: Explain O(n²) approach first
2. **Optimize step by step**: Show how sliding window improves it
3. **Think out loud**: Explain your expand/contract logic
4. **Test with examples**: Walk through your code with sample input

### After Coding:
1. **Trace through edge cases**: Empty array, single element
2. **Analyze complexity**: Time O(n), Space O(k) where k is window size
3. **Discuss variations**: How would you modify for different constraints?

## 🧪 Debugging Checklist

When your sliding window solution isn't working:

- [ ] Are you updating the window state correctly on both expand and contract?
- [ ] Is your contraction condition correct?
- [ ] Are you calculating window size correctly (`right - left + 1`)?
- [ ] Are you handling the case when window becomes empty?
- [ ] For HashMap problems, are you handling zero counts properly?
- [ ] Are you updating the result at the right time?
- [ ] Have you considered all edge cases?

## 🎪 Pro Tips for Mastery

1. **Practice the templates**: Memorize the basic patterns
2. **Visualize the window**: Draw it out for complex problems
3. **Start simple**: Begin with fixed window, then move to variable
4. **Think incrementally**: What changes when we add/remove one element?
5. **Use meaningful variable names**: `left`, `right`, `window_sum`, etc.
6. **Comment your code**: Especially the expand/contract logic

Remember: Sliding window is about maintaining an invariant while efficiently updating your answer. Master the templates, understand the patterns, and you'll recognize these problems instantly in interviews!