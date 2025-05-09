# Python List Sorting: `sort()` and `sorted()`

## `list.sort()` Method

```python
def sort(*, key=None, reverse=False) -> None: ...
```

- Sorts the list in ascending order by default.
- Modifies the list in place and returns `None`.
- The sort is **stable**: equal elements retain their original order.
- Accepts an optional `key` function to determine the sorting criteria.
- The `reverse` flag sorts in descending order if set to `True`.

### Examples

```python
my_list = [5, 2, 7, 1, 0, 12, 5, 3, 4, 6, 8, 9, 10, 11]

my_list.sort()  # Ascending
print(my_list)

my_list.sort(reverse=True)  # Descending
print(my_list)

my_list.sort(key=lambda x: x % 10)  # By last digit
print(my_list)
```

### Common Use Cases

- **Sort by absolute value:**
  ```python
  numbers.sort(key=abs)
  ```
- **Sort strings by length:**
  ```python
  words.sort(key=len)
  ```
- **Sort objects by attribute:**
  ```python
  students.sort(key=lambda s: s.grade)
  ```

### Time and Space Complexity

- **Time Complexity:** O(n log n), where n is the number of elements.
- **Space Complexity:** O(n).
- **Algorithm:** Python uses Timsort, a hybrid of merge sort and insertion sort.

### Limitations

- Only works on mutable, ordered collections (e.g., lists).
- Does not work on tuples or strings (immutable), or on sets and dictionaries (unordered).

---

## `sorted()` Function

```python
sorted(iterable, *, key=None, reverse=False)
```

- Returns a new sorted list from any iterable (list, tuple, set, dictionary, etc.).
- Does **not** modify the original object.

### Example

```python
my_set = {3, -2, 5, 1}
result = sorted(my_set, key=abs, reverse=True)
print(result)  # [5, 3, -2, 1]
```

---

## Additional Concepts

### Sorting Custom Objects

To sort objects, provide a `key` function that extracts a sortable attribute.

```python
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

students = [Student("Alice", 90), Student("Bob", 85)]
students.sort(key=lambda s: s.grade)
```

### Sorting Dictionaries

To sort dictionary items by value:

```python
d = {'a': 3, 'b': 1, 'c': 2}
sorted_items = sorted(d.items(), key=lambda item: item[1])
```

### Sorting with Multiple Criteria

Use a tuple as the key for multi-level sorting:

```python
people = [('Alice', 25), ('Bob', 20), ('Charlie', 25)]
people.sort(key=lambda x: (x[1], x[0]))  # Sort by age, then name
```

---

## Summary Table

| Method        | In-place | Returns New List | Works on | Key Function | Reverse | Stable |
| ------------- | -------- | ---------------- | -------- | ------------ | ------- | ------ |
| `list.sort()` | Yes      | No               | List     | Yes          | Yes     | Yes    |
| `sorted()`    | No       | Yes              | Any      | Yes          | Yes     | Yes    |

---

## Key Points

- Use `list.sort()` for in-place sorting of lists.
- Use `sorted()` for sorting any iterable without modifying the original.
- Both support custom sorting via the `key` parameter and reverse order.
- Sorting is stable and efficient due to Timsort.
