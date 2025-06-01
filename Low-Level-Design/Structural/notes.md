# Structural Design Patterns
Structural design patterns  explore how classes and objects can be composed to form larger structures. They help ensure that if one part of a system changes, the entire system doesn't need to do the same.

# Key Concepts:
1. **Composition over Inheritance**: Favor composition to achieve flexibility and reusability.
2.  **Encapsulation**: Hide the complexities of the system and expose only what is necessary.
3.   **Decoupling**: Reduce dependencies between components to enhance maintainability.


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

