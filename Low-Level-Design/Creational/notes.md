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
