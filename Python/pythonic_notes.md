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

## Python Lists: Powerful and Versatile

Lists are ordered, mutable collections of items. They are one of Python's most versatile built-in data types.

### Creating Lists

```python
# Empty list
empty_list = []
empty_list_alt = list()

# List with initial elements
my_list = [1, 2, 3, "hello", 3.14]

# List from an iterable (e.g., string, tuple, range)
list_from_string = list("python")  # ['p', 'y', 't', 'h', 'o', 'n']
list_from_range = list(range(5))   # [0, 1, 2, 3, 4]
```

### Accessing and Slicing Elements

Elements are accessed by their index (0-based). Slicing extracts a portion of the list.

```python
my_list = [10, 20, 30, 40, 50]
first_element = my_list[0]   # 10
second_element = my_list[1]  # 20
last_element = my_list[-1]   # 50

# Slicing: list[start:stop:step]
sub_list = my_list[1:4]    # [20, 30, 40] (elements at index 1, 2, 3)
from_start = my_list[:3]   # [10, 20, 30]
to_end = my_list[2:]       # [30, 40, 50]
every_other = my_list[::2] # [10, 30, 50]
reversed_list = my_list[::-1]# [50, 40, 30, 20, 10] (creates a new reversed list)
```

### Modifying Lists

#### Adding Elements

- `append(x)`: Adds item `x` to the end of the list.
- `insert(i, x)`: Inserts item `x` at a given position `i`.
- `extend(iterable)`: Extends the list by appending all items from the iterable.

```python
numbers = [1, 2, 3]
numbers.append(4)          # numbers is now [1, 2, 3, 4]
numbers.insert(1, 99)      # numbers is now [1, 99, 2, 3, 4]
numbers.extend([5, 6])     # numbers is now [1, 99, 2, 3, 4, 5, 6]
```

#### Removing Elements

- `remove(x)`: Removes the first item from the list whose value is equal to `x`. Raises `ValueError` if `x` is not found.
- `pop([i])`: Removes the item at the given position `i` in the list and returns it. If no index is specified, `pop()` removes and returns the last item.
- `clear()`: Removes all items from the list (equivalent to `del a[:]`).

```python
items = [10, 20, 30, 20, 40]
items.remove(20)           # items is now [10, 30, 20, 40] (first 20 removed)
popped_item = items.pop(1) # popped_item is 30, items is now [10, 20, 40]
last_item = items.pop()    # last_item is 40, items is now [10, 20]
items.clear()              # items is now []
```

### Other Common List Methods

- `index(x[, start[, end]])`: Returns the zero-based index in the list of the first item whose value is `x`. Raises `ValueError` if `x` is not found.
  Optional `start` and `end` arguments limit the search to a subsequence.
- `count(x)`: Returns the number of times `x` appears in the list.
- `sort(key=None, reverse=False)`: Sorts the items of the list in place. `key` and `reverse` are customization options.
- `reverse()`: Reverses the elements of the list in place.
- `copy()`: Returns a shallow copy of the list (equivalent to `a[:]`).

```python
data = [5, 2, 7, 1, 0, 12, 5, 3]
print(f"Index of 7: {data.index(7)}")      # Output: Index of 7: 2
print(f"Count of 5: {data.count(5)}")      # Output: Count of 5: 2

data_copy = data.copy()
print(f"Original data: {data}")
print(f"Copied data: {data_copy}")

data.sort()
print(f"Sorted data: {data}")            # Output: Sorted data: [0, 1, 2, 3, 5, 5, 7, 12]
data.sort(reverse=True)
print(f"Reverse sorted data: {data}")    # Output: Reverse sorted data: [12, 7, 5, 5, 3, 2, 1, 0]

data.reverse()
print(f"Reversed data: {data}")          # Output: Reversed data: [0, 1, 2, 3, 5, 5, 7, 12] (reversed from previous state)
```

**Note on `sort()` vs `sorted()`**: `list.sort()` sorts the list in-place (modifies the original list and returns `None`). The built-in function `sorted(iterable)` returns a new sorted list, leaving the original iterable unchanged.

### List Comprehensions: Concise List Creation

List comprehensions provide a compact way to create lists. The general syntax is: `[expression for item in iterable if condition]`

#### Basic Comprehension

```python
# Squares of numbers from 0 to 9
squares = [x**2 for x in range(10)]
# squares: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

#### Comprehension with a Condition

```python
# Even numbers from 0 to 9
evens = [x for x in range(10) if x % 2 == 0]
# evens: [0, 2, 4, 6, 8]
```

#### Comprehension with Function Calls

```python
def to_uppercase(s):
    return s.upper()

words = ["hello", "world"]
uppercase_words = [to_uppercase(word) for word in words]
# uppercase_words: ['HELLO', 'WORLD']

# Using lambda functions
numbers = [1, 2, 3, 4]
doubled = [(lambda x: x * 2)(num) for num in numbers] # Or more simply: [num * 2 for num in numbers]
# doubled: [2, 4, 6, 8]
```

#### Nested List Comprehensions

For creating lists of lists or iterating over multiple iterables.

```python
# Create a 3x3 matrix (list of lists)
matrix = [[(row, col) for col in range(3)] for row in range(3)]
# matrix: [[(0,0), (0,1), (0,2)], [(1,0), (1,1), (1,2)], [(2,0), (2,1), (2,2)]]

# Flatten a list of lists
list_of_lists = [[1, 2], [3, 4], [5, 6]]
flattened = [item for sublist in list_of_lists for item in sublist]
# flattened: [1, 2, 3, 4, 5, 6]

# Pairs from two lists (Cartesian product)
list1 = ['a', 'b']
list2 = [1, 2]
pairs = [(x, y) for x in list1 for y in list2]
# pairs: [('a', 1), ('a', 2), ('b', 1), ('b', 2)]
```

#### Comprehensions with `enumerate`

To get both index and value.

```python
my_items = ['apple', 'banana', 'cherry']
indexed_items = [(index, value) for index, value in enumerate(my_items)]
# indexed_items: [(0, 'apple'), (1, 'banana'), (2, 'cherry')]
```

#### Comprehensions with `zip`

To iterate over multiple iterables in parallel.

```python
names = ['Alice', 'Bob', 'Charlie']
ages = [30, 25, 35]
name_age_pairs = [(name, age) for name, age in zip(names, ages)]
# name_age_pairs: [('Alice', 30), ('Bob', 25), ('Charlie', 35)]
```

### Using Lists with `map()`, `filter()`, and `reduce()`

While list comprehensions are often more Pythonic for `map` and `filter` operations, these functions are still useful.

- **`map(function, iterable, ...)`**: Applies `function` to every item of `iterable` and returns an iterator of the results.

  ```python
  numbers = [1, 2, 3, 4]
  # Using map
  squared_map = list(map(lambda x: x**2, numbers)) # [1, 4, 9, 16]
  # Equivalent list comprehension
  squared_lc = [x**2 for x in numbers]
  ```

- **`filter(function, iterable)`**: Constructs an iterator from elements of `iterable` for which `function` returns true.

  ```python
  numbers = range(10)
  # Using filter
  evens_filter = list(filter(lambda x: x % 2 == 0, numbers)) # [0, 2, 4, 6, 8]
  # Equivalent list comprehension
  evens_lc = [x for x in numbers if x % 2 == 0]
  ```

- **`functools.reduce(function, iterable[, initializer])`**: Applies `function` of two arguments cumulatively to the items of `iterable`, from left to right, so as to reduce the iterable to a single value.
  ```python
  from functools import reduce
  numbers = [1, 2, 3, 4, 5]
  sum_of_numbers = reduce(lambda x, y: x + y, numbers) # 15
  # Using built-in sum() is more direct for this case: sum(numbers)
  ```

### Related Comprehension Types

Python also supports comprehensions for other data types:

- **Set Comprehensions**: ` {expression for item in iterable if condition}`
  ```python
  unique_squares = {x**2 for x in [1, 2, 2, 3, 3, 3, 4]}
  # unique_squares: {1, 4, 9, 16}
  ```
- **Dictionary Comprehensions**: `{key_expression: value_expression for item in iterable if condition}`
  ```python
  squared_dict = {x: x**2 for x in range(5)}
  # squared_dict: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
  ```

This concludes the refined section on Python lists.



# Hashmaps or Dictionaries in Python
Hash Map Basics
Behind lists, hash maps are the most commonly used data structure in Python. A hash map is a collection of key-value pairs. Each key is unique, and it maps to a specific value. Keys may be of any immutable type, such as integers, strings, or as we will see later, tuples.

In Python, hash maps are implemented using the dict class. The common operations on a hash map include:

Insertion: Insert a key-value pair into the hash map.

my_dict = {}

my_dict['a'] = 1 # {'a': 1}
Access: Access the value associated with a key.

my_dict = {'a': 1}

print(my_dict['a']) # 1
Deletion: Delete a key-value pair from the hash map.

my_dict = {'a': 1, 'b': 2}

del my_dict['a'] # {}

my_dict.pop('b') # {}

my_dict.pop('c') # KeyError: 'c'

my_dict.pop('c', 'default') # No error, returns 'default'
As shown above, there are two ways to delete a key-value pair from a hash map: using the del keyword or the pop() method. The only difference is that the pop() method returns the value associated with the key.
If the key does not exist, both pop() and del will raise a KeyError. To avoid this, you can pass a default value to the pop() method, which will be returned if the key does not exist.

Lookup: Check if a key exists in the hash map.

my_dict = {'a': 1}

does_a_exist = 'a' in my_dict # True
does_b_exist = 'b' in my_dict # False
For lookup operations, you can also use the in operator, similar to how you would check if an element is in a list.

Challenge
Implement the following functions:

build_hash_map(keys: List[str], values: List[int]) -> Dict[str, int]. It takes two lists, keys and values, and returns a hash map where the keys are the elements of the keys list and the values are the elements of the values list.
This may be a good opportunity to use the zip() function in Python.
get_values(hash_map: Dict[str, int], keys: List[str]) -> List[int]. It takes a hash map and a list of keys and returns a list of the values associated with those keys.
You may assume that all keys in the list exist in the hashmap
The order of the values in the output list should match the order of the keys in the input list.
Hint: If you don't recall how to loop through a dictionary, check out the Dict Looping lesson from the Python for Beginners course.

Time Complexity
Insertion: 
O
(
1
)
O(1)
Access: 
O
(
1
)
O(1)
Deletion: 
O
(
1
)
O(1)
Lookup: 
O
(
1
)
O(1)
The above time complexities are technically for the average case, but in most cases it's safe to assume that these hash map operations are 
O
(
1
)
O(1).