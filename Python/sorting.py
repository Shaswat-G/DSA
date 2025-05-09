# Demo: Python Sorting Methods

# Original list
my_list = [5, 2, 7, 1, 0, 12, 5, 3, 4, 6, 8, 9, 10, 11]
print("Original list:", my_list)

# In-place ascending sort
my_list.sort()
print("Sorted ascending:", my_list)

# In-place descending sort
my_list.sort(reverse=True)
print("Sorted descending:", my_list)

# In-place sort by last digit
my_list.sort(key=lambda x: x % 10)
print("Sorted by last digit:", my_list)

# Demonstrate sorted() on a set (returns a new list)
my_set = {5, 2, 7, 1, 0, 12, 5, 3, 4, 6, 8, 9, 10, 11}
sorted_set = sorted(my_set)
print("Set sorted ascending:", sorted_set)

# Sorted by square value
sorted_by_square = sorted(my_set, key=lambda x: x**2)
print("Set sorted by square:", sorted_by_square)

# Sort list of strings by length
words = ["apple", "banana", "kiwi", "grape"]
words.sort(key=len)
print("Words sorted by length:", words)

# Sort list of tuples by second element
pairs = [(1, 3), (2, 2), (3, 1)]
pairs.sort(key=lambda x: x[1])
print("Tuples sorted by second element:", pairs)

# Use sorted() to preserve original list
original = [3, 1, 4, 1, 5]
sorted_original = sorted(original)
print("Original:", original)
print("Sorted copy:", sorted_original)
