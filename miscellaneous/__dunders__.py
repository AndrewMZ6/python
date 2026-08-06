# experimenting with classes' dunder methods


class myclass:
    """
    This class is one of the foremost classes that's everseen. Pog?
    """

    __name__ = "SPARTA"

    def __init__(self, value: str) -> object:
        self.value = value
        self.dic: dict = {}

    def __eq__(self, other: object) -> bool:

        try:
            assert hasattr(other, "value") == True and type(other.value) == str
            return len(self.value) == len(other.value)
        except AssertionError:
            return "LOL"

    def __hash__(self):
        return 91231

    def __getitem__(self, key):
        return self.dic[key]

    def __setitem__(self, key, value):
        self.dic[key] = value

    def __call__(self):
        pass
        print("Ooooooooopsie")


m = myclass("word")
n = myclass("word")
z = myclass(54)

print(m == n)
# True

print(m == z)
# LOL

print(hash(m))
# 91231

m[0] = 51
m[9] = "hello"

print(m.dic)
# {0: 51, 9: 'hello'}
