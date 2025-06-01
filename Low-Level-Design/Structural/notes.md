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

### Common Use Cases:
1. API Simplification: Wrapping complex third-party libraries or APIs with simpler, domain-specific interfaces.
2. Legacy System Integration: Providing modern interfaces to old, complex systems without modifying the underlying code.
3. Microservice Communication: Creating unified interfaces that coordinate calls across multiple microservices.
4. Database Operations: Simplifying complex database operations involving multiple tables, transactions, and validation rules.
5. Framework Integration: Hiding the complexity of frameworks or libraries behind application-specific interfaces.
6. System Startup/Shutdown: Coordinating the initialization and cleanup of multiple interdependent components.


## Facade Pattern:
The facade pattern is a structural pattern that provides a very simple interface (high-level) to the client and internally orchestrates the complex interactions of internal subsystems. It hides this complexity from the client (demeter principle of least knowledge). It is similar to hotel concierge service, where the client interacts with a single point of contact (the facade) without needing to coordinate with housekeeping, maintenance, kitchen staff, and security.

### Common Use Cases
1. API Simplification: Wrapping complex third-party libraries or APIs with simpler, domain-specific interfaces.
2. Legacy System Integration: Providing modern interfaces to old, complex systems without modifying the underlying code.
3. Microservice Communication: Creating unified interfaces that coordinate calls across multiple microservices.
4. Database Operations: Simplifying complex database operations involving multiple tables, transactions, and validation rules.
5. Framework Integration: Hiding the complexity of frameworks or libraries behind application-specific interfaces.
6. System Startup/Shutdown: Coordinating the initialization and cleanup of multiple interdependent components.

### Approach:
1. Identify the Complex Subsystem: Analyze the existing classes and their interactions. Look for areas where clients need to coordinate multiple objects or perform complex initialization sequences.
2. Define Common Use Cases: Identify the most frequent scenarios where clients interact with the subsystem. These will become your facade methods.
3. Design the Facade Interface: Create methods that represent high-level operations from the client's perspective. Focus on what the client wants to accomplish, not how the subsystem works internally.
4. Implement Coordination Logic: In each facade method, implement the logic to coordinate calls across multiple subsystem objects. Handle the proper sequencing, error handling, and data transformation.
5. Maintain Flexibility: Don't hide everything behind the facade. Allow clients to access subsystem objects directly when they need fine-grained control.
6. Handle Errors Gracefully: Implement proper error handling and recovery mechanisms. The facade should present a unified error handling strategy.
7. Keep It Simple: Resist the temptation to add business logic to the facade. It should primarily coordinate existing functionality, not implement new features.


## Strategy Pattern:

The Strategy pattern is a behavioral design pattern that defines a family of algorithms, encapsulates each one, and makes them interchangeable. It allows you to select algorithms at runtime without altering the clients that use them.

### Core Concept and Reasoning

The Strategy pattern addresses the problem of having multiple ways to perform a task where the choice of algorithm depends on runtime conditions, user preferences, or different contexts. Instead of using conditional statements (if/else or switch) to select different algorithms, you encapsulate each algorithm in its own class and make them interchangeable.

The pattern follows the Open/Closed Principle - you can add new algorithms without modifying existing code. It also adheres to the Single Responsibility Principle by separating algorithm implementation from the context that uses them. This eliminates the need for large conditional blocks and makes the code more maintainable and testable.

Think of it like choosing different transportation methods to get to work - you might walk, drive, take public transit, or bike depending on weather, time constraints, or personal preference. Each method achieves the same goal but uses a different approach.

### How It Works

The Strategy pattern involves three key components:

**Strategy Interface**: Defines a common interface for all concrete strategies. This ensures all algorithms can be used interchangeably.

**Concrete Strategies**: Classes that implement different algorithms using the strategy interface. Each strategy encapsulates a specific algorithm or behavior.

**Context**: The class that uses a strategy. It maintains a reference to a strategy object and delegates algorithm execution to it. The context can switch strategies at runtime.

### Common Use Cases

**Payment Processing**: Different payment methods (credit card, PayPal, cryptocurrency) with the same interface.

**Sorting Algorithms**: Choosing between quicksort, mergesort, bubblesort based on data size or characteristics.

**Compression**: Different compression algorithms (ZIP, RAR, GZIP) based on file type or compression requirements.

**Pricing Strategies**: Different discount calculations (percentage, fixed amount, buy-one-get-one) in e-commerce systems.

**Authentication**: Multiple authentication methods (password, OAuth, biometric) that can be selected based on security requirements.

**Data Validation**: Different validation rules that can be applied based on context or user type.

**Navigation Systems**: Different route calculation algorithms (shortest distance, fastest time, avoid tolls).


### General Approach to Writing Strategy Patterns

**Identify Variable Algorithms**: Look for areas in your code where you have multiple ways to accomplish the same task, especially where you're using if/else or switch statements to choose between approaches.

**Define the Strategy Interface**: Create an interface or abstract class that defines the common method signature all strategies must implement. Keep it focused on the core algorithm.

**Implement Concrete Strategies**: Create separate classes for each algorithm, implementing the strategy interface. Each strategy should be self-contained and stateless when possible.

**Design the Context Class**: Create a class that uses strategies. It should maintain a reference to the current strategy and provide methods to switch strategies if needed.

**Consider Strategy Selection**: Decide how strategies will be chosen - through constructor parameters, setter methods, factory patterns, or configuration files.

**Handle Strategy-Specific Parameters**: If different strategies need different parameters, consider using strategy-specific configuration objects or builder patterns.

**Provide Strategy Metadata**: Consider adding methods to strategies that describe their characteristics (name, performance characteristics, suitable use cases).

## Strategy Pattern Variations

**Parameterized Strategies**: Strategies that accept configuration parameters to modify their behavior.

**Strategy Factories**: Factory classes that select appropriate strategies based on context or input characteristics.

**Strategy Chains**: Combining multiple strategies in sequence or applying fallback strategies.

**Template Method + Strategy**: Using template methods within strategies to provide common structure while allowing algorithmic variation.

## Benefits and Considerations

The Strategy pattern eliminates conditional statements and makes it easy to add new algorithms without modifying existing code. It promotes code reuse and makes testing easier since each algorithm can be tested in isolation. The pattern also makes it possible to switch algorithms at runtime based on changing conditions.

However, clients must be aware of different strategies and understand when to use each one. The pattern can increase the number of classes in your system, and if strategies are simple, the pattern might be overkill compared to simple function parameters.

The pattern works best when you have multiple algorithms for the same task, when algorithms change frequently, or when you want to avoid exposing complex, algorithm-specific data structures to clients. It's particularly valuable in systems where algorithm choice depends on runtime conditions, user preferences, or environmental factors.

The key is to identify true algorithmic variations rather than simple parameter differences - if behaviors differ only in values, consider parameterization instead of separate strategy classes.
