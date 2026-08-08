"""
Experimenting with attribute lookup in python

obj.attr
   │
   ▼
type(obj).__getattribute__(obj, "attr")     ← always
   │
   ├─ (default implementation)
   │     ├─ data descriptor?
   │     ├─ instance.__dict__?
   │     ├─ non-data descriptor?
   │     └─ class attribute?
   │
   └─ if AttributeError → __getattr__ (if defined)

"""

from typing import Any


class MyDataDescriptor:
    """
    'self' is the instance of the descriptor. MyDataDescriptor()
    'instance' is the instance of the class the descriptor attached to. ClassUnderTesting()
    'cls' is the class the descriptor instance is attached to. ClassUnderTesting
    """

    def __get__(self, instance, cls):
        print("inside __get__ of MyDataDescriptor")
        try:
            return instance._hidden_value
        except AttributeError:
            return "This is the default value of the descriptor"

    def __set__(self, instance, value):
        print(f"inside __set__ of MyDataDescriptor, {value = }")
        instance._hidden_value = value


class ClassUnderTesting:
    class_attribute = "minecraft"
    my_descriptor = MyDataDescriptor()

    def __getattribute__(self, name: str) -> Any:
        print(f"a calling __getattribute__ with argument -> {name}")
        if name == "year_made":
            return 1976
        return super().__getattribute__(name)

    def __new__(cls):
        print(f"{cls.__name__} class calling __new__")
        return super().__new__(cls)

    def __getattr__(self, name) -> int:
        print(f"a calling __getattr__ with argument {name}")
        if name == "justice":
            return 7778
        raise AttributeError(f"a - has no attribute '{name}'")


if __name__ == "__main__":
    a = ClassUnderTesting()
    print(a.my_descriptor)
    a.my_descriptor = 54
    print(a.my_descriptor)
