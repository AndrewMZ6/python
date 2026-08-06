# Testing execution time of generating 1x10000000 size list
# of random int numbers in range 1 to 100000 using:
#   1. Initially empty list, append in for loop
#   2. List comprehention
#   3. Numpy array
#

import time
import numpy as np
import random

# for loop ----------
py_forloop_start_time = time.time()

forlist = []
for num in range(10000000):
    forlist.append(random.randint(1, 100000))

form = max(forlist)

py_forloop_end_time = time.time()

# list comprehension ----------
py_start_time = time.time()

numlist = [random.randint(1, 100000) for num in range(10000000)]
m = max(numlist)
py_end_time = time.time()


# numpy ---------
np_start_time = time.time()
nplist = np.random.randint(low=1, high=100001, size=10000000)
npm = np.max(nplist)

np_end_time = time.time()


print(
    f"for loop exec time:{py_forloop_end_time - py_forloop_start_time:.2f}. Max is {form}"
)
print(f"list comprehension exec time:{py_end_time - py_start_time:.2f}. Max is {m}")
print(f"numpy exec time:{np_end_time - np_start_time:.2f}. Max is {npm}")


# OUTPUT:
#
# for loop exec time:16.61. Max is 100000
# list comprehension exec time:15.06. Max is 100000
# numpy exec time:0.18. Max is 100000
#
# 15/0.2 = 75
