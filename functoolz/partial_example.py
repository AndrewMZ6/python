"""
Why does this module exist?
It's a collection of tolls - functions that 
"""

from functools import partial


def exponential_function(base: int, power: int):
    return base ** power



# two to the power of 1, 2, 3, 4
print(exponential_function(2, 1))
print(exponential_function(2, 2))
print(exponential_function(2, 3))
print(exponential_function(2, 4))


# OUTPUT:

# 2
# 4
# 8
# 16

two_base = partial(exponential_function, power=2)
# two_base = partial(exponential_function, base=2)        # TypeError: exponential_function() got multiple values for argument 'base'


# print the values of 1^2, 2^2, 3^2, 4^2
print(two_base(1))
print(two_base(2))
print(two_base(3))
print(two_base(4))



# OUTPUT:

# 2
# 4
# 8
# 16