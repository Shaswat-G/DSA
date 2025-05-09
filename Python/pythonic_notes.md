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

## Python Dictionaries (Hashmaps): Key-Value Powerhouses

Dictionaries, often called hashmaps in other languages, are fundamental data structures in Python. They store data as collections of key-value pairs. Each key must be unique and immutable (e.g., strings, numbers, tuples), while values can be of any data type and can be duplicated. Dictionaries are unordered in Python versions before 3.7, but are insertion-ordered by default from Python 3.7 onwards.

### Creating Dictionaries

```python
# Empty dictionary
empty_dict = {}
empty_dict_alt = dict()

# Dictionary with initial key-value pairs
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Creating a dictionary using the dict() constructor
# From a list of key-value tuples
dict_from_tuples = dict([('a', 1), ('b', 2), ('c', 3)]) # {'a': 1, 'b': 2, 'c': 3}

# From keyword arguments (keys must be valid identifiers)
dict_from_kwargs = dict(name="Bob", age=25) # {'name': 'Bob', 'age': 25}

# Using zip to combine keys and values lists
keys = ['fruit', 'color', 'quantity']
values = ['apple', 'red', 5]
dict_from_zip = dict(zip(keys, values)) # {'fruit': 'apple', 'color': 'red', 'quantity': 5}
```

### Accessing Values

Values are accessed using their corresponding keys.

```python
my_dict = {"name": "Alice", "age": 30}

# Using square bracket notation
name = my_dict["name"]  # Alice
# If key doesn't exist, it raises a KeyError
# city = my_dict["city"] # Raises KeyError

# Using the get() method
age = my_dict.get("age")      # 30
city = my_dict.get("city")    # None (returns None if key is not found)
country = my_dict.get("country", "Unknown") # Unknown (returns default value if key not found)
```

Using `get()` is often safer as it avoids `KeyError` exceptions for missing keys.

### Adding and Updating Key-Value Pairs

```python
my_dict = {"name": "Alice"}

# Adding a new key-value pair
my_dict["age"] = 30            # my_dict is now {'name': 'Alice', 'age': 30}

# Updating an existing key's value
my_dict["name"] = "Alicia"     # my_dict is now {'name': 'Alicia', 'age': 30}

# Using the update() method
# Can add multiple pairs or update existing ones
my_dict.update({"city": "London", "age": 31})
# my_dict is now {'name': 'Alicia', 'age': 31, 'city': 'London'}

# update() can also take another dictionary or an iterable of key-value pairs
another_dict = {"occupation": "Engineer"}
my_dict.update(another_dict)
# my_dict is now {'name': 'Alicia', 'age': 31, 'city': 'London', 'occupation': 'Engineer'}
```

### Removing Key-Value Pairs

```python
my_dict = {"name": "Alice", "age": 30, "city": "New York"}

# Using the del keyword
del my_dict["city"]
# my_dict is now {'name': 'Alice', 'age': 30}
# del my_dict["country"] # Raises KeyError if key doesn't exist

# Using the pop() method
# Removes the key and returns its value
age = my_dict.pop("age") # age is 30, my_dict is now {'name': 'Alice'}
# city = my_dict.pop("city") # Raises KeyError if key doesn't exist

# pop() with a default value to avoid KeyError
country = my_dict.pop("country", "Not Found") # country is "Not Found", my_dict is unchanged if "country" wasn't there

# Using popitem()
# Removes and returns an arbitrary (key, value) pair (LIFO since Python 3.7)
# Useful for iterating through and consuming dictionary items
my_dict = {"a": 1, "b": 2, "c": 3}
item = my_dict.popitem() # item might be ('c', 3), my_dict is now {'a': 1, 'b': 2}

# Using clear()
# Removes all items from the dictionary
my_dict.clear() # my_dict is now {}
```

### Checking for Key Existence (Lookup)

```python
my_dict = {"name": "Alice", "age": 30}

# Using the 'in' operator (preferred)
is_name_present = "name" in my_dict  # True
is_city_present = "city" in my_dict  # False

# Using 'not in'
is_country_absent = "country" not in my_dict # True
```

### Iterating Through Dictionaries

```python
my_dict = {"name": "Alice", "age": 30, "city": "New York"}

# Iterating over keys (default iteration behavior)
print("Keys:")
for key in my_dict:
    print(key) # name, age, city

# Iterating over keys explicitly
print("\nKeys explicitly:")
for key in my_dict.keys():
    print(key) # name, age, city

# Iterating over values
print("\nValues:")
for value in my_dict.values():
    print(value) # Alice, 30, New York

# Iterating over key-value pairs (items)
print("\nKey-Value pairs:")
for key, value in my_dict.items():
    print(f"{key}: {value}") # name: Alice, age: 30, city: New York
```

### Common Dictionary Methods Overview

- `clear()`: Removes all items.
- `copy()`: Returns a shallow copy of the dictionary.
- `fromkeys(seq[, value])`: Creates a new dictionary with keys from `seq` and values set to `value` (defaults to `None`).
  ```python
  keys = ['a', 'b', 'c']
  new_dict = dict.fromkeys(keys, 0) # {'a': 0, 'b': 0, 'c': 0}
  ```
- `get(key[, default])`: Returns the value for `key` if `key` is in the dictionary, else `default`.
- `items()`: Returns a view object that displays a list of a dictionary's key-value tuple pairs.
- `keys()`: Returns a view object that displays a list of all the keys.
- `pop(key[, default])`: Removes `key` and returns its value. If `key` is not found, `default` is returned if given, otherwise `KeyError` is raised.
- `popitem()`: Removes and returns an arbitrary (key, value) pair.
- `setdefault(key[, default])`: If `key` is in the dictionary, returns its value. If not, inserts `key` with a value of `default` and returns `default` (defaults to `None`).
  ```python
  my_dict = {'a': 1}
  value_a = my_dict.setdefault('a', 0) # value_a is 1, my_dict is {'a': 1}
  value_b = my_dict.setdefault('b', 0) # value_b is 0, my_dict is {'a': 1, 'b': 0}
  ```
- `update([other])`: Updates the dictionary with the key/value pairs from `other`, overwriting existing keys.
- `values()`: Returns a view object that displays a list of all the values.

### Dictionary Comprehensions

Similar to list comprehensions, dictionary comprehensions provide a concise way to create dictionaries.
Syntax: `{key_expr: value_expr for item in iterable if condition}`

```python
# Create a dictionary of squares
squares_dict = {x: x**2 for x in range(5)}
# squares_dict: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# From existing lists
keys = ['name', 'age', 'city']
values = ['Bob', 25, 'Paris']
person_dict = {k: v for k, v in zip(keys, values)}
# person_dict: {'name': 'Bob', 'age': 25, 'city': 'Paris'}

# With a condition
original_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
even_values_dict = {k: v for k, v in original_dict.items() if v % 2 == 0}
# even_values_dict: {'b': 2, 'd': 4}

# Swapping keys and values (ensure values are unique and hashable if they become keys)
fruit_colors = {'apple': 'red', 'banana': 'yellow'}
color_fruits = {v: k for k, v in fruit_colors.items()}
# color_fruits: {'red': 'apple', 'yellow': 'banana'}
```

### Use Case Examples (from previous "Challenge")

1.  **Building a hash map from two lists:**

    ```python
    def build_hash_map(keys_list: list, values_list: list) -> dict:
        # Using zip and dict constructor is concise
        return dict(zip(keys_list, values_list))
        # Alternatively, using a dictionary comprehension:
        # return {keys_list[i]: values_list[i] for i in range(len(keys_list))}

    keys = ["apple", "banana", "cherry"]
    values = [0.5, 0.25, 0.75]
    price_map = build_hash_map(keys, values)
    print(price_map) # {'apple': 0.5, 'banana': 0.25, 'cherry': 0.75}
    ```

2.  **Getting values for a list of keys:**

    ```python
    def get_values_for_keys(hash_map: dict, keys_to_get: list) -> list:
        # Using a list comprehension
        return [hash_map[key] for key in keys_to_get]
        # Assuming all keys in keys_to_get exist in hash_map
        # If keys might be missing and you want a default:
        # return [hash_map.get(key, "N/A") for key in keys_to_get]

    fruit_prices = {'apple': 0.5, 'banana': 0.25, 'cherry': 0.75, 'date': 1.0}
    desired_fruits = ["banana", "date", "apple"]
    prices = get_values_for_keys(fruit_prices, desired_fruits)
    print(prices) # [0.25, 1.0, 0.5]
    ```

### Time Complexity of Basic Dictionary Operations

For Python's `dict` implementation (which uses a hash table):

- **Insertion**: Average `O(1)`, Worst case `O(n)` (due to hash collisions or resizing)
- **Access/Lookup**: Average `O(1)`, Worst case `O(n)`
- **Deletion**: Average `O(1)`, Worst case `O(n)`

The `O(n)` worst-case scenarios are rare in practice with good hash functions. For most practical purposes, dictionary operations are considered `O(1)`.

## Python Heaps (Priority Queues) with `heapq`

Heaps are a specialized tree-based data structure that satisfy the heap property. In Python, the `heapq` module provides an implementation of the heap queue algorithm, also known as the priority queue algorithm. Heaps are binary trees for which every parent node has a value less than or equal to any of its children (min-heap). Python's `heapq` module implements a min-heap, meaning the smallest element is always at the root (`heap[0]`).

Heaps are implemented as Python lists, but it's crucial to use only the functions from the `heapq` module to maintain the heap property.

```python
import heapq
```

### Core Heap Operations

#### 1. Pushing Elements: `heapq.heappush(heap, item)`

Adds `item` to the `heap`, maintaining the heap invariant.

```python
heap = []
heapq.heappush(heap, 30) # heap is now [30]
heapq.heappush(heap, 10) # heap is now [10, 30]
heapq.heappush(heap, 20) # heap is now [10, 30, 20] (internal list representation)
heapq.heappush(heap, 5)  # heap is now [5, 10, 20, 30]
print(heap) # Output: [5, 10, 20, 30] (actual internal order might vary but heap[0] is smallest)
```

- **Time Complexity**: `O(log n)`, where `n` is the number of elements in the heap.
- **Space Complexity**: `O(1)` for the operation itself (heap storage is `O(n)`).

**Use Case (Challenge: Heap Push):**
Implement a function that pushes a value onto a min-heap and returns the smallest element.

```python
def heap_push_and_get_min(heap: list, value: int) -> int:
    heapq.heappush(heap, value)
    return heap[0] # Smallest element is always at index 0

my_heap = [10, 20]
heapq.heapify(my_heap) # Ensure it's a valid heap first if starting with existing list
min_val = heap_push_and_get_min(my_heap, 5)
print(f"Heap after push: {my_heap}, Min value: {min_val}") # Heap: [5, 20, 10], Min: 5
```

#### 2. Popping Elements: `heapq.heappop(heap)`

Pops and returns the smallest item from the `heap`, maintaining the heap invariant. Raises `IndexError` if the heap is empty.

```python
heap = [5, 10, 20, 30] # Assume this is a valid heap
heapq.heapify(heap) # Or ensure it's heapified

smallest = heapq.heappop(heap) # smallest is 5, heap is now [10, 30, 20]
print(f"Popped: {smallest}, Heap after pop: {heap}")

next_smallest = heapq.heappop(heap) # next_smallest is 10, heap is now [20, 30]
print(f"Popped: {next_smallest}, Heap after pop: {heap}")
```

- **Time Complexity**: `O(log n)`.
- **Space Complexity**: `O(1)`.

**Use Case (Challenge: Heap Pop):**
Implement a function that pops all elements from a min-heap and returns them in the order they were popped (ascending order).

```python
def pop_all_from_heap(heap: list) -> list:
    popped_elements = []
    # Ensure the input list is a heap if it's not already
    # If it's guaranteed to be a heap, heapify might not be needed here
    # but it's safer if the source is an arbitrary list.
    # heapq.heapify(heap) # Uncomment if 'heap' might not be a heap initially
    while heap:
        popped_elements.append(heapq.heappop(heap))
    return popped_elements

data_to_heap = [40, 10, 50, 20, 30]
heapq.heapify(data_to_heap) # Make it a heap first
sorted_data = pop_all_from_heap(data_to_heap) # data_to_heap will be empty
print(f"Sorted data by popping: {sorted_data}") # [10, 20, 30, 40, 50]
```

#### 3. Accessing the Smallest Element (Peeking)

The smallest element of a min-heap is always at index 0.

```python
heap = [5, 10, 20] # Assume valid heap
smallest_element = heap[0] # 5
```

- **Time Complexity**: `O(1)`.

### Building a Heap

#### `heapq.heapify(x)`

Transforms list `x` into a heap, in-place, in linear time.

```python
my_list = [4, 2, 5, 3, 1, 9, 6]
heapq.heapify(my_list)
print(f"Heapified list: {my_list}") # e.g., [1, 2, 5, 3, 4, 9, 6] (heap[0] is smallest)
# The exact internal order can vary but it satisfies the heap property.
```

- **Time Complexity**: `O(n)`, where `n` is the number of elements in the list. This is more efficient than pushing elements one by one (`O(n log n)`).
- **Space Complexity**: `O(1)` (in-place).

**Use Cases (Challenge: Heapify):**

1.  **Heapify Strings:**

    ```python
    def heapify_strings(strings: list[str]) -> list[str]:
        heapq.heapify(strings)
        return strings

    str_list = ["banana", "apple", "kiwi", "date"]
    heapified_str_list = heapify_strings(str_list)
    print(f"Heapified strings: {heapified_str_list}") # e.g., ['apple', 'banana', 'kiwi', 'date']
    ```

2.  **Heapify Integers:** (Same as the general example above)
    ```python
    def heapify_integers(integers: list[int]) -> list[int]:
        heapq.heapify(integers)
        return integers
    ```
3.  **Heap Sort:**
    A common application of heaps is heap sort.

    ```python
    def heap_sort(nums: list[int]) -> list[int]:
        heapq.heapify(nums) # Transform list into a min-heap
        sorted_list = []
        while nums:
            sorted_list.append(heapq.heappop(nums)) # Repeatedly pop the smallest element
        return sorted_list

    unsorted_nums = [4, 2, 5, 3, 1, 9, 6]
    sorted_nums = heap_sort(unsorted_nums)
    print(f"Heap sorted numbers: {sorted_nums}") # [1, 2, 3, 4, 5, 6, 9]
    ```

### Advanced Heap Techniques

#### 1. Simulating a Max-Heap

Python's `heapq` only provides a min-heap. To simulate a max-heap, store negated values (for numbers) or use custom objects/tuples where the comparison logic is inverted. For numbers, negate them when pushing and negate again when popping.

```python
nums = [4, 2, 3, 5, 1]
max_heap = []
for num in nums:
    heapq.heappush(max_heap, -num) # Push negated value

print("Max-heap elements (popped and re-negated):")
while max_heap:
    largest = -heapq.heappop(max_heap) # Pop and negate back
    print(largest, end=" ") # Output: 5 4 3 2 1
print()
```

**Use Case (Challenge: Max Heap - Get Reverse Sorted):**

```python
def get_reverse_sorted(nums: list[int]) -> list[int]:
    max_heap_sim = []
    for num in nums:
        heapq.heappush(max_heap_sim, -num)

    reverse_sorted_list = []
    while max_heap_sim:
        reverse_sorted_list.append(-heapq.heappop(max_heap_sim))
    return reverse_sorted_list

numbers = [4, 2, 3, 5, 1, 9]
print(f"Reverse sorted: {get_reverse_sorted(numbers)}") # [9, 5, 4, 3, 2, 1]
```

#### 2. Heaps with Custom Priorities (Tuples)

If you need to prioritize based on a custom key or store complex objects, use tuples `(priority, item)` or custom objects that implement rich comparison methods. Python's heap compares tuples element by element.

```python
# Example: Min-heap of (priority, task_name)
tasks = []
heapq.heappush(tasks, (5, "Write code"))
heapq.heappush(tasks, (1, "Fix critical bug"))
heapq.heappush(tasks, (3, "Attend meeting"))

print("Tasks by priority (popped):")
while tasks:
    priority, task_name = heapq.heappop(tasks)
    print(f"Priority: {priority}, Task: {task_name}")
# Output:
# Priority: 1, Task: Fix critical bug
# Priority: 3, Task: Attend meeting
# Priority: 5, Task: Write code
```

**Use Case (Challenge: Custom Heap - Absolute Value Priority):**
Sort numbers based on their absolute value (smallest absolute value first), then by their original value if absolute values are tied.

```python
nums_custom = [4, -2, 3, -5, 2] # -2 and 2 have same abs value
custom_heap = []
for num in nums_custom:
    # (abs_value, original_value) for tie-breaking
    heapq.heappush(custom_heap, (abs(num), num))

print("Sorted by absolute value (then original value):")
while custom_heap:
    abs_val, original_num = heapq.heappop(custom_heap)
    print(original_num, end=" ") # Output: -2 2 3 4 -5 (or similar based on tie-breaking)
print()
```

### Utility Functions for N Smallest/Largest

#### 1. `heapq.nsmallest(n, iterable, key=None)`

Returns a list with the `n` smallest items from `iterable`. If `key` is provided, it's a function of one argument that is used to extract a comparison key from each element in iterable.

```python
my_array = [1, 6, 3, 5, 7, 9, 8, 10, 2, 12]
print(f"3 smallest: {heapq.nsmallest(3, my_array)}")  # [1, 2, 3]
print(f"5 smallest: {heapq.nsmallest(5, my_array)}")  # [1, 2, 3, 5, 6]

# With a key
data_dicts = [{'name': 'A', 'val': 10}, {'name': 'B', 'val': 5}, {'name': 'C', 'val': 15}]
print(f"2 smallest by 'val': {heapq.nsmallest(2, data_dicts, key=lambda x: x['val'])}")
# Output: [{'name': 'B', 'val': 5}, {'name': 'A', 'val': 10}]
```

- **Time Complexity**: `O(m log n)` where `m` is the size of the iterable and `n` is the number of items to find. If `n` is 1, it's `O(m)`. If `n` is close to `m`, it's closer to `O(m log m)`.

**Use Cases (Challenge: Heap N Smallest):**

```python
def get_min_element(arr: list[int]) -> int:
    return heapq.nsmallest(1, arr)[0]

def get_min_4_elements_increasing(arr: list[int]) -> list[int]:
    return heapq.nsmallest(4, arr) # nsmallest returns them sorted

def get_min_2_elements_decreasing(arr: list[int]) -> list[int]:
    two_smallest = heapq.nsmallest(2, arr)
    return sorted(two_smallest, reverse=True) # nsmallest sorts ascending, so re-sort

test_arr = [10, 1, 30, 2, 40, 5]
print(f"Min element: {get_min_element(test_arr)}") # 1
print(f"Min 4 increasing: {get_min_4_elements_increasing(test_arr)}") # [1, 2, 5, 10]
print(f"Min 2 decreasing: {get_min_2_elements_decreasing(test_arr)}") # [2, 1]
```

#### 2. `heapq.nlargest(n, iterable, key=None)`

Returns a list with the `n` largest items from `iterable`. Similar to `nsmallest` in behavior and complexity.

```python
my_array = [1, 6, 3, 5, 7, 9, 8, 10, 2, 12]
print(f"3 largest: {heapq.nlargest(3, my_array)}")  # [12, 10, 9]
print(f"5 largest: {heapq.nlargest(5, my_array)}")  # [12, 10, 9, 8, 7]
```

- **Time Complexity**: `O(m log n)`.

**Use Cases (Challenge: Heap N Largest):**

```python
def get_max_element(arr: list[int]) -> int:
    return heapq.nlargest(1, arr)[0]

def get_max_4_elements_decreasing(arr: list[int]) -> list[int]:
    return heapq.nlargest(4, arr) # nlargest returns them sorted descending

def get_max_2_elements_increasing(arr: list[int]) -> list[int]:
    two_largest = heapq.nlargest(2, arr)
    return sorted(two_largest) # nlargest sorts descending, so re-sort

test_arr = [10, 1, 30, 2, 40, 5]
print(f"Max element: {get_max_element(test_arr)}") # 40
print(f"Max 4 decreasing: {get_max_4_elements_decreasing(test_arr)}") # [40, 30, 10, 5]
print(f"Max 2 increasing: {get_max_2_elements_increasing(test_arr)}") # [30, 40]
```

This concludes the refined section on Python Heaps / Priority Queues.
