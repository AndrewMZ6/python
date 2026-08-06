# decorator that limits the amount oof letters in string


def limiter(n=10):
    def ponchik(func):
        def decorator(s):
            try:
                assert len(s) <= n
                m = func(s)
                return m
            except AssertionError:
                print(f"The input string length cannot be more than {n} letters")

        return decorator

    return ponchik


@limiter(n=62)
def func(s: str) -> str:

    counter = 1
    m = ""

    try:
        for i in range(len(s)):
            if s[i] == s[i + 1]:
                counter += 1
            else:
                m = m + str(s[i]) + str(counter)
                counter = 1

    except IndexError:
        m = m + s[i] + str(counter)

    return m


p = func("aacbbbttbc asssssssdas")
print(p)
# output
# a2c1b3t2b1c1 1a1s7d1a1s1
