"""
Why is it needed?

To reduce coupling between creation of objects and their concrete classes.
Wiki article https://en.wikipedia.org/wiki/Factory_method_pattern
"""

from abc import ABC, abstractmethod


# In this example "Creator" creates "Product"


class Product(ABC):
    """
    This is the interface for factory items that will be created by Factories
    """

    @abstractmethod
    def product_method(self): ...


class Creator(ABC):
    """
    This is the inteface for Factories
    """

    @abstractmethod
    def create_product(self) -> Product:
        """
        Factories have a method that creates and returns items with interface "Product"

        For example:
        >>> product = factory_instance.create_product()
        >>> isinstance(product, Product)
        True
        """

    def operation(self):
        # ...
        product = self.create_product()
        product.product_method()
        # ...


class ProductWithRedRibbon(Product):
    """
    Concrete implementation of interface "Product"
    """

    def product_method(self):
        print("I'm a product with red ribbon. It's red, not blue")


class CreatorOfProductsWithRedRibbon(Creator):
    """
    Concrete implementation of a Factory class
    """

    def create_product(self):
        red_ribboned_product = ProductWithRedRibbon()
        return red_ribboned_product


# ---------------------- Logistics example ------------------


"""
Good example of the usage of the "Factory" design pattern is shown on https://refactoring.guru/design-patterns/factory-method

The idea is having Logistics class that is responsible for logistics in general
and then had various implementations of Logistics depending on the road chosen - 
by land, by sea, on rails, etc.
"""


class Transport(ABC):
    """
    Interface for all transport object to have
    """

    @abstractmethod
    def deliver(self):
        """
        Describes how to deliver cargo from one place to another
        """


class Logistics(ABC):
    """
    Factory blueprint
    """

    @abstractmethod
    def create_transport(self) -> Transport: ...

    def plan_delivery(self, t: Transport):
        self.process(t)


class Ship(Transport):
    """
    Implementation of sea transport. It is guaranteed to have 'deliver' method
    """

    def deliver(self):
        return "A guide how to deliver cargo by sea"


class Truck(Transport):
    """
    Implementation of road transport.
    """

    def deliver(self):
        return "A GPS list of points of the road"


class SeaLogistics(Logistics):
    """
    Implementation of Factory for sea transport
    """

    def create_transport(self):
        return Ship()


class RoadLogistics(Logistics):
    """
    Implementation of Factory for road transport
    """

    def create_transport(self):
        return Truck()


if __name__ == "__main__":
    red_ribbon_factory = CreatorOfProductsWithRedRibbon()
    red_ribbon_factory.operation()

    road_factory = RoadLogistics()
    t = road_factory.create_transport()
    print(t.deliver())

    sea_factory = SeaLogistics()
    s = sea_factory.create_transport()
    print(s.deliver())
