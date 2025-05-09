box_dimensions = (2, 3, 4)
length, width, height = box_dimensions # unpacking
volume = length * width * height
print("Volume of the box:", volume)

# Demonstrate unpacking with a list
coordinates = [10, 20, 30]
x, y, z = coordinates # unpacking
print("Coordinates:", x, y, z)
# Demonstrate unpacking with a dictionary
person = {"name": "Alice", "age": 30, "city": "New York"}
name, age, city = person.values() # unpacking
print("Person:", name, age, city)
# Demonstrate unpacking with a set
numbers = {1, 2, 3}
a, b, c = numbers # unpacking
print("Numbers:", a, b, c)
# Demonstrate unpacking with a string
text = "Hello"
a, b, c, d, e = text # unpacking
print("Text:", a, b, c, d, e)


# enumberate is used for getting index and element in the iterable
# it packages the index and the element into a tuple
# we unpack it in the main loop
names = ["Alice", "Bob", "Charlie"]
for index, name in enumerate(names):
    print(f"Index: {index}, Name: {name}")
    