# example of closure using lambda function


def make_y(a: float, b: float, c: float):
    # values of variables a, b, c are saved
    # inside returned lambda function

    return lambda x: a * (x**2) + b * x + c


y = make_y(7, -2, 3)

# quadratic function
# y == 7*(x**2) -2*x + 3

# y(0) == 7*0 - 2*0 + 3 == 3
# y(1) == 7*1 - 2*1 + 3 == 8

z = make_y(0, 2, -1)

# linear function
# z == 2x -1
