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


class A:
    class_attribute = "minecraft"

    def __getattribute__(self, name: str) -> Any:
        print(f"{self} calling __getattribute__ with argument -> {name}")
        if name == "flare":
            return 46
        return super().__getattribute__(name)

    def __new__(cls):
        print(f"{cls} class accessing __new__")
        return super().__new__(cls)

    def __getattr__(self, name) -> int:
        print(f"{self} accessing __getattr__ with argument {name}")
        if name == "justice":
            return 7778
        raise AttributeError(
            f"'{self.__class__.__name__}' object - has no attribute '{name}'"
        )
