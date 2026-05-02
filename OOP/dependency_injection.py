from abc import ABC, abstractmethod

"""
From wikipedia:

In object-oriented design, the dependency inversion principle is a specific methodology for loosely coupled software modules. When following this principle, 
the conventional dependency relationships established from high-level, policy-setting modules to low-level, dependency modules are reversed, 
thus rendering high-level modules independent of the low-level module implementation details. The principle states:

1. High-level modules should not import anything from low-level modules. Both should depend on abstractions (e.g., interfaces).
2. Abstractions should not depend on details. Details (concrete implementations) should depend on abstractions.
By dictating that both high-level and low-level objects must depend on the same abstraction, this design principle inverts the way some people may think about
 object-oriented programming.
"""


class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        """Turns on the Switchable object"""

    @abstractmethod
    def turn_off(self):
        """Turns off the Switchable object"""


class Lightbulb(Switchable):
    def turn_on(self) -> None:
        print(f"the {self.__class__.__name__} is turned on")

    def turn_off(self) -> None:
        print(f"the {self.__class__.__name__} is turned off")


class FairyLights(Switchable):
    def turn_on(self) -> None:
        print(f"the {self.__class__.__name__} is turned on")

    def turn_off(self) -> None:
        print(f"the {self.__class__.__name__} is turned off")


class PowerSwitcher:
    def __init__(self, l: Switchable) -> None:
        self.l = l
        self.turned_on = False

    def switch(self) -> None:
        if self.turned_on:
            self.l.turn_off()
            self.turned_on = False
        else:
            self.l.turn_on()
            self.turned_on = True


f = FairyLights()
p = PowerSwitcher(f)
p.switch()
p.switch()


l = Lightbulb()
p = PowerSwitcher(l)
p.switch()
p.switch()


# OUTPUT:

# the FairyLights is turned on
# the FairyLights is turned off
# the Lightbulb is turned on
# the Lightbulb is turned off
