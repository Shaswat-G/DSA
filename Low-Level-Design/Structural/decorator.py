from abc import ABC, abstractmethod


# Component interface
class Coffee(ABC):
    @abstractmethod
    def cost(self):
        pass

    @abstractmethod
    def description(self):
        pass


# Concrete component
class SimpleCoffee(Coffee):
    def cost(self):
        return 2.00

    def description(self):
        return "Simple coffee"


# Base decorator
class CoffeeDecorator(Coffee):
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost()

    def description(self):
        return self._coffee.description()


# Concrete decorators
class MilkDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 0.50

    def description(self):
        return self._coffee.description() + ", milk"


class SugarDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 0.25

    def description(self):
        return self._coffee.description() + ", sugar"


class WhipCreamDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 0.75

    def description(self):
        return self._coffee.description() + ", whip cream"


class ExtraShotDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 1.00

    def description(self):
        return self._coffee.description() + ", extra shot"


# Usage - decorators can be combined in any order
coffee = SimpleCoffee()
print(f"{coffee.description()}: ${coffee.cost():.2f}")

# Add milk
coffee = MilkDecorator(coffee)
print(f"{coffee.description()}: ${coffee.cost():.2f}")

# Add sugar
coffee = SugarDecorator(coffee)
print(f"{coffee.description()}: ${coffee.cost():.2f}")

# Add whip cream and extra shot
coffee = WhipCreamDecorator(ExtraShotDecorator(coffee))
print(f"{coffee.description()}: ${coffee.cost():.2f}")

# Create a different combination
fancy_coffee = WhipCreamDecorator(SugarDecorator(MilkDecorator(ExtraShotDecorator(SimpleCoffee()))))
print(f"{fancy_coffee.description()}: ${fancy_coffee.cost():.2f}")
