# Experimenting with changing list inbuilt functionality


class Mylist(list):
    def __init__(self, L: list):
        super().__init__(L)

    def __add__(self, other):
        try:
            return Mylist([i + j for i, j in zip(self, other, strict=True)])
        except ValueError:
            raise ValueError("Input Arguments must be the same length")

    def isunique(self):
        return len(set(self)) == len(self)


L2 = Mylist([7, 4, 11, 9, 3])
L1 = Mylist([3, 6, -1, 1, 7])
L3 = L1 + L2
print(L3)
print(L3.isunique())

# OUTPUT:
# [10, 10, 10, 10, 10]
# False

L2 = Mylist([7, 4, 11, 9, 3])
L1 = Mylist([-2, 23, 1, 21, -7])
L3 = L1 + L2
print(L3)
print(L3.isunique())

# OUTPUT:
# [5, 27, 12, 30, -4]
# True
