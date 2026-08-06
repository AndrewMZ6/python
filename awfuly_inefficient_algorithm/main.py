# awfuly inefficitent algorithm takes almost 10 seconds to generate 100 fake emails!

from func_module import my_gen

L = []
for i in my_gen(100):
    L.append(i)

# output:
# [Finished in 9.4s]
