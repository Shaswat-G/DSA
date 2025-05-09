# Python Dictionaries: A Comprehensive Guide

# Dictionaries in Python are versatile, unordered (prior to Python 3.7) or ordered (Python 3.7+)
# collections of items. Each item in a dictionary is a key-value pair.
# Keys must be unique and immutable (e.g., strings, numbers, tuples).
# Values can be of any data type and can be duplicated.

print("--- 1. Creating Dictionaries ---")
# a. Empty dictionary
empty_dict = {}
print(f"Empty dictionary: {empty_dict}, type: {type(empty_dict)}")

# b. Dictionary with initial values
student = {"name": "Alice", "age": 25, "courses": ["Math", "Physics"]}
print(f"Student dictionary: {student}")

# c. Using the dict() constructor
person = dict(name="Bob", city="New York")
print(f"Person (from kwargs): {person}")

pairs = [("fruit", "apple"), ("color", "red")]
fruit_dict = dict(pairs)
print(f"Fruit (from list of tuples): {fruit_dict}")

print("\n--- 2. Accessing Elements ---")
print(f"Student's name: {student['name']}")
print(f"Student's age: {student.get('age')}")
print(f"Student's address (using get): {student.get('address')}")
print(
    f"Student's address (using get with default): {student.get('address', 'Not specified')}"
)

print("\n--- 3. Adding and Modifying Elements ---")
student["major"] = "Computer Science"
print(f"Student after adding major: {student}")
student["age"] = 26
print(f"Student after updating age: {student}")

print("\n--- 4. Removing Elements ---")
grades = {"Math": "A", "Physics": "B", "Chemistry": "C"}
print(f"Grades before del: {grades}")
del grades["Chemistry"]
print(f"Grades after del 'Chemistry': {grades}")
physics_grade = grades.pop("Physics")
print(f"Popped 'Physics' grade: {physics_grade}")
print(f"Grades after pop 'Physics': {grades}")
biology_grade = grades.pop("Biology", "Not Found")
print(f"Popped 'Biology' grade (with default): {biology_grade}")
print(f"Grades remain unchanged: {grades}")
grades["English"] = "A+"
grades["History"] = "B+"
print(f"Grades before popitem: {grades}")
last_item_added = grades.popitem()
print(f"Popped item (LIFO): {last_item_added}")
print(f"Grades after popitem: {grades}")
temp_dict = {"a": 1, "b": 2}
print(f"Temp dict before clear: {temp_dict}")
temp_dict.clear()
print(f"Temp dict after clear: {temp_dict}")

print("\n--- 5. Dictionary Membership ---")
print(f"'name' in student: {'name' in student}")
print(f"'address' in student: {'address' in student}")
print(f"'major' not in student: {'major' not in student}")
print(f"Is 'Alice' a value in student? {'Alice' in student.values()}")
print(f"Is 26 a value in student? {26 in student.values()}")
print(f"Is 'New York' a value in student? {'New York' in student.values()}")

print("\n--- 6. Iterating Through Dictionaries ---")
config = {"host": "localhost", "port": 8080, "debug_mode": True}
print(f"Config dictionary: {config}")
print("Keys:")
for key in config:
    print(f"  {key} -> {config[key]}")
print("Values:")
for value in config.values():
    print(f"  {value}")
print("Key-Value pairs:")
for key, value in config.items():
    print(f"  {key}: {value}")

print("\n--- 7. Dictionary Methods (More) ---")
keys_view = student.keys()
print(f"Keys view: {keys_view}")
student["phone"] = "555-1234"
print(f"Keys view (after adding 'phone' to student): {keys_view}")
values_view = student.values()
print(f"Values view: {values_view}")
items_view = student.items()
print(f"Items view: {items_view}")
user_profile = {"name": "Alice Smith", "city": "San Francisco"}
student.update(user_profile)
print(f"Student after update: {student}")
student.update([("status", "active"), ("id", 101)])
print(f"Student after update with iterable: {student}")
original_dict = {"a": 1, "b": [10, 20]}
copied_dict = original_dict.copy()
print(f"Original: {original_dict}, Copied: {copied_dict}")
copied_dict["a"] = 2
copied_dict["b"].append(30)
print(f"After modifying copied: Original: {original_dict}, Copied: {copied_dict}")
settings = {"theme": "dark"}
print(f"Theme: {settings.setdefault('theme', 'light')}")
print(f"Font size: {settings.setdefault('font_size', 12)}")
print(f"Settings after setdefault: {settings}")
seq = ("name", "age", "country")
default_value = "unknown"
new_user = dict.fromkeys(seq, default_value)
print(f"New user fromkeys: {new_user}")
new_user_no_value = dict.fromkeys(seq)
print(f"New user fromkeys (no value): {new_user_no_value}")

print("\n--- 8. Dictionary Comprehensions ---")
numbers = [1, 2, 3, 4, 5]
squared_dict = {x: x**2 for x in numbers}
print(f"Squared numbers dict: {squared_dict}")
keys_list = ["a", "b", "c"]
values_list = [10, 20, 30]
combined_dict = {k: v for k, v in zip(keys_list, values_list)}
print(f"Combined dict from lists: {combined_dict}")
even_squared_dict = {x: x**2 for x in numbers if x % 2 == 0}
print(f"Even squared numbers dict: {even_squared_dict}")

print("\n--- 9. Nested Dictionaries ---")
employees = {
    "emp1": {"name": "John Doe", "position": "Developer", "salary": 70000},
    "emp2": {
        "name": "Jane Smith",
        "position": "Manager",
        "salary": 90000,
        "team": {"team_name": "Alpha", "members": 5},
    },
    "emp3": {"name": "Peter Jones", "position": "Designer", "salary": 65000},
}
print(f"Employees: {employees}")
print(f"Employee 1's name: {employees['emp1']['name']}")
print(f"Employee 2's position: {employees['emp2']['position']}")
print(f"Employee 2's team name: {employees['emp2']['team']['team_name']}")
employees["emp1"]["salary"] = 75000
print(f"Employee 1's updated salary: {employees['emp1']['salary']}")
employees["emp2"]["team"]["project"] = "New Platform"
print(f"Employee 2's team details: {employees['emp2']['team']}")

print("\n--- 10. Common Use Cases ---")
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
word_counts = {}
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1
print(f"Word counts (manual): {word_counts}")
word_counts_get = {}
for word in words:
    word_counts_get[word] = word_counts_get.get(word, 0) + 1
print(f"Word counts (using get): {word_counts_get}")
app_config = {
    "database": {
        "type": "PostgreSQL",
        "host": "db.example.com",
        "port": 5432,
        "user": "admin",
    },
    "api_keys": {"google_maps": "YOUR_API_KEY_HERE"},
    "logging_level": "INFO",
}
print(f"App config database type: {app_config['database']['type']}")
memo = {}


def fibonacci(n):
    if n in memo:
        return memo[n]
    if n <= 1:
        result = n
    else:
        result = fibonacci(n - 1) + fibonacci(n - 2)
    memo[n] = result
    return result


print(f"Fibonacci(10): {fibonacci(10)}")
print(f"Fibonacci memoization cache: {memo}")
data_points = [
    {"category": "A", "value": 10},
    {"category": "B", "value": 20},
    {"category": "A", "value": 15},
    {"category": "C", "value": 5},
    {"category": "B", "value": 25},
]
grouped_data = {}
for item in data_points:
    category = item["category"]
    if category not in grouped_data:
        grouped_data[category] = []
    grouped_data[category].append(item["value"])
print(f"Grouped data: {grouped_data}")

print("\n--- 11. Advanced Concepts & Related Collections ---")
from collections import defaultdict

grouped_data_defaultdict = defaultdict(list)
for item in data_points:
    grouped_data_defaultdict[item["category"]].append(item["value"])
print(f"Grouped data (using defaultdict): {dict(grouped_data_defaultdict)}")
word_counts_defaultdict = defaultdict(int)
for word in words:
    word_counts_defaultdict[word] += 1
print(f"Word counts (using defaultdict): {dict(word_counts_defaultdict)}")
from collections import Counter

word_counts_counter = Counter(words)
print(f"Word counts (using Counter): {word_counts_counter}")
print(f"Most common words: {word_counts_counter.most_common(2)}")
hashable_key_dict = {}
hashable_key_dict[10] = "integer key"
hashable_key_dict["text"] = "string key"
hashable_key_dict[(1, 2)] = "tuple key"
print(f"Dictionary with various hashable keys: {hashable_key_dict}")
ordered_example = {}
ordered_example["first"] = 1
ordered_example["second"] = 2
ordered_example["third"] = 3
print("Iteration order (Python 3.7+):")
for k, v in ordered_example.items():
    print(f"  {k}: {v}")

print("\n--- End of Dictionary Demo ---")
print("Dictionaries are a fundamental and powerful data structure in Python!")
