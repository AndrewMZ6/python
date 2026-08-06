"""
Experimenting with attribute lookup in python
"""


from typing import Any


class A:
    def __getattribute__(self, name: str) -> Any:
        if name == 'flare':
            return 46
        return super().__getattribute__(name)


a = A()
print(a.t)