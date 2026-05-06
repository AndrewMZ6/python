"""
Why is it needed?

To reduce coupling between creation of objects and their concrete classes.
Wiki article https://en.wikipedia.org/wiki/Factory_method_pattern
"""
from abc import ABC, abstractmethod




class Product(ABC):
    """
    This is the interface for factory items that will be created by Factories
    """
    @abstractmethod
    def interface_method(self): ...



class Creator(ABC):
    """
    This is the inteface for Factories
    """
    @abstractmethod
    def factory_method(self) -> Product:
        """
        Factories have a method that creates and returns items with interface Product
        """

    def operation(self):
        # other stuff ...
        product = self.factoryMethod()

        # do something with product...
        return product


class Creator1(Creator):
    """
    Concrete implementation of a Factory
    """
    
