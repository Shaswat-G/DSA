# Pythonic Code: Elegant and Readable Patterns

## Unpacking and Packing

- **Unpacking:** Assign multiple variables at once from iterables.
  ```python
  a, b, c = (1, 2, 3)
  x, *rest = [10, 20, 30, 40]  # x=10, rest=[20,30,40]
  first, *_, last = [1, 2, 3, 4]  # first=1, last=4
  ```
- **Packing:** Use \*args and \*\*kwargs to collect positional and keyword arguments in functions.
  ```python
  def func(*args, **kwargs):
    pass
  ```

## Enumerate for Readability

- Use `enumerate()` to get both index and value when looping.
  ```python
  for idx, value in enumerate(my_list):
      print(idx, value)
  ```
- Improves clarity and avoids manual index tracking.

## Zip for Parallel Iteration

- Use `zip()` to iterate over multiple iterables in parallel.
  ```python
  for a, b in zip(list1, list2):
      print(a, b)
  ```
- Useful for combining, comparing, or processing paired data.

## Chained Comparisons

- Python allows concise chained comparisons:
  ```python
  if 0 < x < 10:
      ...
  ```

## Min/Max Shortcuts

- Use `min()` and `max()` to constrain values elegantly:
  ```python
  transactions = max(0, transactions)  # Never negative
  transactions = min(100, transactions)  # Never above 100
  ```
- Prefer these over verbose if-statements for bounds checking.

## General Tips

- Prefer list comprehensions for concise transformations.
- Use generator expressions for memory efficiency with large data.
- Leverage built-in functions (`any`, `all`, `sum`, `sorted`, etc.) for clarity and performance.
- Write expressive, readable code—avoid unnecessary loops and manual bookkeeping.



## Lists:
# demonstrate append, pop, romove, insert, sort, reverse, extend, clear, index, count, copy
my_list = [5, 2, 7, 1, 0, 12, 5, 3, 4, 6, 8, 9, 10, 11]
print("Original list:", my_list)
# Append
my_list.append(13)
print("After append:", my_list)
# Pop
popped_value = my_list.pop()
print("Popped value:", popped_value)
print("After pop:", my_list)

# Remove
my_list.remove(5)
print("After remove:", my_list)
# Insert
my_list.insert(0, 99)
print("After insert:", my_list)
# Sort
my_list.sort()
print("After sort:", my_list)
# Reverse
my_list.reverse()
print("After reverse:", my_list)
# Extend
my_list.extend([14, 15])
print("After extend:", my_list)
# Clear
my_list.clear()
print("After clear:", my_list)
# Index
my_list = [5, 2, 7, 1, 0, 12, 5, 3, 4, 6, 8, 9, 10, 11]
index_of_7 = my_list.index(7)
print("Index of 7:", index_of_7)
# Count
count_of_5 = my_list.count(5)
print("Count of 5:", count_of_5)
# Copy
my_list_copy = my_list.copy()
print("Copied list:", my_list_copy)
# List Comprehensions
squares = [x**2 for x in range(10)]
print("Squares:", squares)
# Nested List Comprehensions
nested_list = [[x for x in range(3)] for y in range(3)]
print("Nested list:", nested_list)
# List Comprehensions with Conditions
evens = [x for x in range(10) if x % 2 == 0]
print("Evens:", evens)
# List Comprehensions with Functions
def square(x):
    return x**2
squared_list = [square(x) for x in range(10)]
print("Squared list:", squared_list)
# List Comprehensions with Multiple Iterables
pairs = [(x, y) for x in range(3) for y in range(3)]
print("Pairs:", pairs)
# List Comprehensions with Enumerate
enumerated_list = [(index, value) for index, value in enumerate(my_list)]
print("Enumerated list:", enumerated_list)
# List Comprehensions with Zip
zipped_list = [(x, y) for x, y in zip(range(3), range(3, 6))]
print("Zipped list:", zipped_list)
# List Comprehensions with Set
set_comprehension = {x**2 for x in range(10)}
print("Set comprehension:", set_comprehension)
# List Comprehensions with Dictionary
dict_comprehension = {x: x**2 for x in range(10)}
print("Dictionary comprehension:", dict_comprehension)
# List Comprehensions with String
string_comprehension = [char for char in "Hello"]
print("String comprehension:", string_comprehension)
# List Comprehensions with Filter
filtered_list = [x for x in range(10) if x > 5]
print("Filtered list:", filtered_list)
# List Comprehensions with Map
mapped_list = [x**2 for x in map(int, range(10))]
print("Mapped list:", mapped_list)
# List Comprehensions with Reduce
from functools import reduce
reduced_value = reduce(lambda x, y: x + y, range(10))
print("Reduced value:", reduced_value)
# List Comprehensions with Lambda
lambda_list = [(lambda x: x**2)(x) for x in range(10)]
print("Lambda list:", lambda_list)
# List Comprehensions with Filter and Map
filtered_mapped_list = [x**2 for x in filter(lambda x: x > 5, range(10))]
print("Filtered and mapped list:", filtered_mapped_list)
# List Comprehensions with Nested Loops
nested_loop_list = [(x, y) for x in range(3) for y in range(3)]
