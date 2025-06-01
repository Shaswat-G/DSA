# Structural Design Patterns
Structural design patterns  explore how classes and objects can be composed to form larger structures. They help ensure that if one part of a system changes, the entire system doesn't need to do the same.

# Key Concepts:
1. **Composition over Inheritance**: Favor composition to achieve flexibility and reusability.
2.  **Encapsulation**: Hide the complexities of the system and expose only what is necessary.
3.   **Decoupling**: Reduce dependencies between components to enhance maintainability.

ed
# Common Structural Patterns:

## Adapter Pattern:
The adapter pattern allows incompatible interfaces to work together.

Usually, we define an adapter class that inherits from a target interface that needs to be translated into. The adaptee object is passed to the adapter object, which then implements all the methods of the target interface by calling and processing the methods from the adaptee class. 

### Approach:
1. Identify/Define a target interface that the client expects.
2. Analyze the adaptee class and identify the methods that can be used to implement the target interface.
3.  Create an adapter class that inherits from the target interface and contains an instance of the adaptee class.
4.  Implement interface translation: For each method in the target interface, implement the logic to translate the call to the appropriate method(s) on the adaptee. This often involves: Parameter transformation (changing types, units, formats), Method name mapping, Return value conversion, Error handling translation.

### Use Cases:
- Integrating third-party libraries with different interfaces.
- Adapting legacy code to new systems.
- Data format conversion (e.g., XML to JSON).
- API standardization.

## Decorator Pattern:
The decorator pattern is a structural design pattern that allows you to add more functionality to an object dynamically (at run time) without subclassing / modifying the original class. It is often used to extend the behavior of classes in a flexible and reusable way.

Each decorator wraps an object and adds its own behavior while delegating the core functionality to the wrapped object.

### Key components:
1. Component Base Class: An abstract class that defines the interface components.
2. Concrete Component Class: A class that inherits from the component base class and implements the core functionality.
3. Decorator Base Class: An abstract class that also inherits from the component base class and contains a reference to a component object. It implements all the same functionality as the concrete component class.  It delegates all operations to the wrapped component by default.
4. Concrete Decorator Classes: Classes that inherit from the decorator base class and add additional functionality by overriding methods.

### Approach:
1. Define the Component Interface: Create an interface or abstract class that defines the operations that can be decorated. This should include all methods that decorators might need to intercept or modify.
2. Implement the Concrete Component: Create the base implementation that provides the core functionality without any decorations.
3. Create the Base Decorator: Implement an abstract decorator class that implements the component interface and holds a reference to a component. This class should delegate all operations to the wrapped component by default.
4. Implement Concrete Decorators: For each behavior you want to add, create a concrete decorator that extends the base decorator. Each decorator should:

   - Add its specific behavior before, after, or around the delegated call
   - Maintain the same interface as the component
   - Be composable with other decorators

