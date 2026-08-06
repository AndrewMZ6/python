"""
The file is dedicated to learning type hints in python
checking how ty by astral.sh works
"""

from collections.abc import Callable, Iterable

x: int = 1
y: float = 2.3
z: str = "Gradually"
w: bool = True
t: tuple[str, int] = ("Sarah", 43)
t2: tuple[str, ...] = ("ball", "kerl")
r: list[int] = [1, 2, 331]
d: dict[str, str] = {"Andrew": "dev", "Sarah": "QA"}
s: set[float] = {43.12, 5.1}
i: Iterable[int] = (1, 2, 3)  # [1, 2, 3] and {1, 2, 3} also work


class Dog: ...


u: Dog | int = Dog()


def func(x: int, /) -> str:
    return str(x)


def func2(x: str) -> str:
    return str(x)


q: Callable = func


def tres(f: Callable[[int], str]) -> None: ...


tres(func)


type Scores = dict[str, list[int]]  # type aliases
e: Scores = {"Knix": [4, 1, 9]}
