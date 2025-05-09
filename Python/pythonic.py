# Pythonic Idioms Demo Script

# --- Unpacking Examples ---
box_dimensions = (2, 3, 4)
length, width, height = box_dimensions
volume = length * width * height
print("Box dimensions:", box_dimensions)
print("Volume of the box:", volume)

coordinates = [10, 20, 30]
x, y, z = coordinates
print("Coordinates:", x, y, z)

person = {"name": "Alice", "age": 30, "city": "New York"}
name, age, city = person.values()
print("Person details:", name, age, city)

numbers = {1, 2, 3}
a, b, c = numbers
print("Numbers from set:", a, b, c)

text = "Hello"
a, b, c, d, e = text
print("Characters in text:", a, b, c, d, e)

# --- Enumerate Example ---
names = ["Alice", "Bob", "Charlie"]
print("\nEnumerate demo:")
for index, name in enumerate(names):
    print(f"Index: {index}, Name: {name}")

# --- Zip Example ---
ages = [25, 30, 35]
print("\nZip demo:")
for name, age in zip(names, ages):
    print(f"Name: {name}, Age: {age}")

# --- Chained Comparison Example ---
x = 5
if 0 < x < 10:
    print("\nChained comparison: x is between 0 and 10")

# --- Min/Max Shortcut Example ---
transactions = -2
transactions = max(0, transactions)
print("\nTransactions after min check:", transactions)

transactions = 101
transactions = min(100, transactions)
print("Transactions after max check:", transactions)
