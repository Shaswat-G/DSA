# Creational Design Patterns: Elegant Reference Guide

This guide covers the three most essential creational design patterns in object-oriented programming: **Factory Method**, **Singleton**, and **Builder**. Each pattern is explained with its intent, use cases, benefits, drawbacks, and Python examples.

---

## Factory Method Pattern

**Intent:**

> Define an interface for creating an object, but let subclasses decide which class to instantiate. Factory Method lets a class defer instantiation to subclasses.

**When to Use:**

- You need to create objects, but the exact type may not be known until runtime.
- You want to centralize and decouple object creation logic from business logic.
- You have a family of related objects (e.g., different UI elements, payment processors).
- You are building frameworks or plugin architectures.

**Benefits:**

- Flexible and extensible: add new product types without changing client code.
- Decouples client code from concrete classes.
- Follows the Open/Closed Principle.

**Example:**

```python
class VehicleFactory:
    def create_vehicle(self, vehicle_type):
        if vehicle_type == 'car':
            return Car()
        elif vehicle_type == 'bike':
            return Bike()
        else:
            raise ValueError('Unknown vehicle type')

# Usage
factory = VehicleFactory()
vehicle = factory.create_vehicle('car')
```

---

## Singleton Pattern

**Intent:**

> Ensure a class has only one instance and provide a global point of access to it.

**When to Use:**

- Managing shared resources (database connections, configuration, logging).
- Coordinating actions across the system (device managers, print spoolers).
- When a single instance is required for correctness.

**Benefits:**

- Controlled access to sole instance.
- Lazy initialization possible.
- Saves memory by avoiding duplicate instances.

**Drawbacks:**

- Can introduce global state and hidden dependencies.
- Harder to test and maintain.
- Requires care in multi-threaded environments.

**Python Example:**

```python
class Singleton:
    _instance = None
    _initialized = False
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    def __init__(self):
        if not self._initialized:
            self.data = "Singleton instance"
            Singleton._initialized = True

# Usage
s1 = Singleton()
s2 = Singleton()
assert s1 is s2
```

---

## Builder Pattern

**Intent:**

> Separate the construction of a complex object from its representation, allowing the same construction process to create different representations.

**When to Use:**

- Constructing complex objects step by step.
- Objects with many optional parameters or configurations.
- When you want to separate construction logic from the object itself.

**Benefits:**

- Fluent, readable object creation (method chaining).
- Easy to add new optional parameters.
- Can validate or enforce invariants before building.
- Supports immutability and complex construction logic.

**Drawbacks:**

- Overkill for simple objects with few parameters.
- Adds extra classes and complexity.

**Python Example:**

```python
class Product:
    def __init__(self):
        self.parts = []
    def add_part(self, part):
        self.parts.append(part)
    def show(self):
        return f"Product parts: {', '.join(self.parts)}"

class Builder:
    def __init__(self):
        self.product = Product()
    def add_engine(self, engine_type):
        self.product.add_part(f"Engine: {engine_type}")
        return self
    def add_wheels(self, wheel_count):
        self.product.add_part(f"Wheels: {wheel_count}")
        return self
    def add_color(self, color):
        self.product.add_part(f"Color: {color}")
        return self
    def build(self):
        return self.product

# Usage
car = (Builder()
       .add_engine("V8")
       .add_wheels(4)
       .add_color("Red")
       .build())
print(car.show())
```

---

**Summary Table**

| Pattern   | Intent                                      | When to Use                                | Key Benefit               |
| --------- | ------------------------------------------- | ------------------------------------------ | ------------------------- |
| Factory   | Delegate object creation to subclasses      | Type not known until runtime, decoupling   | Flexible, decoupled code  |
| Singleton | Only one instance, global access            | Shared resources, global state             | Controlled, single access |
| Builder   | Step-by-step construction of complex object | Many optional params, complex construction | Readable, flexible build  |

---

This guide is designed for quick reference and practical application. For each pattern, remember to weigh the benefits and drawbacks in the context of your project.


## Prototype Pattern:
Creation pattern that allows cloning of existing objects without depending on their classes. Useful when object creation is expensive or complex.
Following is a deep copy that ensures complete independence of the cloned object from the original, even for complex nested structures.
```Python
import copy
from abc import ABC, abstractmethod

class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass

class ConcretePrototype(Prototype):
    def __init__(self, name, data):
        self.name = name
        self.data = data
        self.complex_object = {"nested": "value", "list": [1, 2, 3]}
    
    def clone(self):
        # Deep copy to ensure complete independence
        return copy.deepcopy(self)
    
    def __str__(self):
        return f"ConcretePrototype(name={self.name}, data={self.data})"

# Usage
original = ConcretePrototype("Original", "original_data")
cloned = original.clone()

cloned.name = "Cloned"
cloned.data = "cloned_data"
cloned.complex_object["nested"] = "modified"

print(f"Original: {original}")
print(f"Cloned: {cloned}")
print(f"Original complex_object: {original.complex_object}")
print(f"Cloned complex_object: {cloned.complex_object}")

```

However, you can also create shallow copies that modifies the original object, which is useful when you want to share some properties between the original and cloned objects.
```Python
import copy

class Document:
    def __init__(self, title, content, metadata):
        self.title = title
        self.content = content
        self.metadata = metadata  # This is a mutable object
    
    def shallow_clone(self):
        return copy.copy(self)
    
    def deep_clone(self):
        return copy.deepcopy(self)
    
    def __str__(self):
        return f"Document(title={self.title}, metadata={self.metadata})"

# Original document
original = Document("Report", "Content here", {"author": "John", "tags": ["work", "important"]})

# Shallow copy - shares references to mutable objects
shallow = original.shallow_clone()
shallow.title = "Report Copy"
shallow.metadata["author"] = "Jane"  # This modifies original too!

# Deep copy - completely independent
deep = original.deep_clone()
deep.title = "Deep Report Copy"
deep.metadata["author"] = "Bob"  # This doesn't affect original

print(f"Original: {original}")
print(f"Shallow: {shallow}")
print(f"Deep: {deep}")
```


When Should Prototype Ring a Bell?
1. Expensive Object Creation

Objects that require database queries to initialize
Objects with complex computational setup
Objects that load large amounts of data

2. Similar Objects with Variations

Game characters with different names but same class
Documents with similar structure but different content
Configuration objects with minor differences

3. Dynamic Object Creation

When object types are determined at runtime
Plugin systems where object types are loaded dynamically
Template systems

4. Performance Optimization

When object creation is a bottleneck
When you need many similar objects
When initialization is more expensive than copying

Real-World Use Cases
Configuration Management:
pythonclass DatabaseConfig:
    def __init__(self):
        self.host = "localhost"
        self.port = 5432
        self.database = "myapp"
        self.connection_pool_size = 10
        self.timeout = 30
        self.ssl_config = {"enabled": False, "cert_path": None}
    
    def clone(self):
        return copy.deepcopy(self)

# Base configurations
base_config = DatabaseConfig()

# Production config (clone and modify)
prod_config = base_config.clone()
prod_config.host = "prod-db.company.com"
prod_config.ssl_config["enabled"] = True
prod_config.connection_pool_size = 50

# Testing config
test_config = base_config.clone()
test_config.database = "test_myapp"
test_config.port = 5433
UI Component Templates:
pythonclass UIComponent:
    def __init__(self, component_type):
        self.type = component_type
        self.properties = {}
        self.styles = {}
        self.event_handlers = {}
    
    def clone(self):
        return copy.deepcopy(self)

# Create base button template
base_button = UIComponent("button")
base_button.properties = {"text": "Click Me", "enabled": True}
base_button.styles = {"width": "100px", "height": "30px"}

# Create specialized buttons
primary_button = base_button.clone()
primary_button.styles.update({"background": "blue", "color": "white"})

secondary_button = base_button.clone()
secondary_button.styles.update({"background": "gray", "color": "black"})
Benefits of Prototype Pattern
Performance: Faster than creating objects from scratch when initialization is expensive
Flexibility: Easy to create variations of existing objects
Reduced Subclassing: Avoid creating many subclasses for similar objects
Runtime Configuration: Object types can be determined and cloned at runtime
Complex Object Management: Simplifies creation of objects with complex internal state
When NOT to Use Prototype
Simple Objects: When object creation is already fast and simple
Deep Copy Complexity: When objects contain circular references or complex nested structures
Memory Constraints: When storing many prototype instances uses too much memory
Unique Objects: When each object needs to be completely unique
The Prototype pattern is particularly valuable in scenarios where you have template objects that serve as starting points for creating customized instances. It's commonly used in game development, document generation systems, and configuration management where you need many similar objects with slight variations.RetryClaude can make mistakes. Please double-check responses.