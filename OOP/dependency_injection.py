from abc import ABC, abstractmethod


class Switchable(ABC):
    
    @abstractmethod
    def turn_on(self):
        '''Turns on the Switchable object'''

    @abstractmethod
    def turn_off(self):
        '''Turns off the Switchable object'''


class Lightbulb(Switchable):

    def turn_on(self)  -> None:
        print(f"the {self.__class__.__name__} is turned on")

    def turn_off(self)  -> None:
        print(f"the {self.__class__.__name__} is turned off")


class FairyLights(Switchable):
    def turn_on(self)  -> None:
        print(f"the {self.__class__.__name__} is turned on")

    def turn_off(self)  -> None:
        print(f"the {self.__class__.__name__} is turned off")


class PowerSwitcher:

    def __init__(self, l:Switchable) -> None:
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
