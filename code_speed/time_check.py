import time


def measure_time(func):
    def wrapper(*args):
        t_start = time.time_ns()
        print(*args)
        func(*args)
        t_stop = time.time_ns()
        print(
            f"elapsed time: {(t_stop - t_start) / 1e3} mcs, or {(t_stop - t_start) / 1e6} ms"
        )

    return wrapper


@measure_time
def func1():
    L = []
    for i in range(100000):
        if i % 2 == 0 and i % 3 == 0 and i % 7 == 0:
            L.append(i)
    print(len(L))


@measure_time
def func2():
    L = []
    for i in range(100000):
        if i % 2 == 0 and i % 3 == 0 and i % 7 == 0:
            L = L + [i]
    print(len(L))


func1()
func2()

## output:
#
# 2381
# elapsed time: 15588.8 mcs, or 15.5888 ms
#
# 2381
# elapsed time: 15660.9 mcs, or 15.6609 ms
