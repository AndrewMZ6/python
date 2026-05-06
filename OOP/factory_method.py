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


if __name__ == "__main__":
    red_ribbon_factory = CreatorOfProductsWithRedRibbon()
    red_ribbon_factory.operation()
