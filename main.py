def main():
    def f(a: int, /, b: int) -> str:
        return f"{a=}, {b=}"

    s = f(1, 2)
    assert type(s) is str


if __name__ == "__main__":
    main()
