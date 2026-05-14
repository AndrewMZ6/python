from abc import ABC, abstractmethod

"""
From wikipedia:

In object-oriented design, the dependency inversion principle is a specific methodology
for loosely coupled software modules. When following this principle, 
the conventional dependency relationships established from high-level, 
policy-setting modules to low-level, dependency modules are reversed, 
thus rendering high-level modules independent of the low-level module 
implementation details. The principle states:

1. High-level modules should not import anything from low-level modules. Both should depend on abstractions (e.g., interfaces).
2. Abstractions should not depend on details. Details (concrete implementations) should depend on abstractions.
By dictating that both high-level and low-level objects must depend on the same abstraction, this design principle inverts the way some people may think about
 object-oriented programming.
"""


# ------------------ Conventional dependency relationships ---------------------------


# Conventional dependency relationships (before applying Dependency Inversion)
# mean that high-level modules directly depend on low-level modules. For example


class UserService:  # this is high-level module
    def __init__(self):
        self.db = PostgresDatabase()  # this is low-level details

    def get_user(self, user_id):
        user = self.db.query(f"SELECT * FROM users WHERE id={user_id}")
        return user


# 1. "UserService" owns / knows about "PostgresDatabase"
# 2. Switching from Postgres to MySQL database or MongoDB requires changing "UserService" class
# 3. Can't use mocks for testing


# ------------------------------- And now enter DI! -----------------------------------


class UserRepository(ABC):  # interface
    @abstractmethod
    def get_user(self, user_id): ...


class PostgreSqlUserRepository(UserRepository):  # low-level depends on the interface
    def get_user(self, user_id):
        "PostgreSQL query code"
        pass


class UserService:
    def __init__(self, repo: UserRepository):  # depends on abstraction / interface
        self.repo = repo

    def get_user(self, user_id):
        return self.db.get_user(user_id)


# High-level module "UserService" depends on abtraction "UserRepository"
# Low-level module "PostgreSqlUserRepository" ALSO depends on abtraction "UserRepository"
# Adding another low-level module, e.g. "MySqlUserRepository" is now easier


class MySqlUserRepository(UserRepository):
    def get_user(self, user_id):
        "MySQL query code"
        pass


# ------------------------------- another example --------------------------------------
#                           Lightbulb and FairyLights(гирлянда)


class Switchable(ABC):
    """
    Interface for dependency object
    """

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
    def __init__(
        self, l: Switchable
    ) -> None:  # depends on the interface, not implementation
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


"""
Without dependency injection - direct dependency
"""


class BadPowerSwitcher:
    def __init__(self) -> None:
        self.turned_on = False

    def switch(self) -> None:
        # Direct depencency, BadPowerSwitcher class is tightly coupled to
        # Lightbulb class
        l = Lightbulb()
        if self.turned_on:
            l.turn_off()
            self.turned_on = False
        else:
            l.turn_on()
            self.turned_on = True


bps = BadPowerSwitcher()
bps.switch()
bps.switch()


# OUTPUT:

# the FairyLights is turned on
# the FairyLights is turned off
# the Lightbulb is turned on
# the Lightbulb is turned off
# the Lightbulb is turned on
# the Lightbulb is turned off




"""
I've confused dependency injection (DI) and dependency inversion principle (DIP). They are different in the sense of
area:
    DIP is a principle, recomendation on how to depouple modules while 
    DI is a technique implementing the principle
"""