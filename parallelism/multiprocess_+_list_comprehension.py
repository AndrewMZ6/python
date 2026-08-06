import time
import random
import concurrent.futures as cf


def generate_list_numbers(m):
    return [random.randint(1, 100_000) for _ in range(m)]


# without multiprocessing
# end goal is a list containing 10_000_000 of random numbers in range 1 to 100_000

py_start_time = time.perf_counter()
numlist = generate_list_numbers(10_000_000)
py_end_time = time.perf_counter()
print(
    f"lc exec time:{py_end_time - py_start_time:.5f}. len: {len(numlist)}, elems: {numlist[10000:10014]}"
)

# OUTPUT:
# lc exec time:6.78383. len: 10000000, elems: [99783, 12865, 34949, 4263, 76420, 50553, 54357, 56172, 65817, 5027, 65242, 52721, 6347, 34642]


# with multiprocessing, 10 processes
if __name__ == "__main__":
    mp_start_time = time.perf_counter()

    with cf.ProcessPoolExecutor() as executor:
        procs = [executor.submit(generate_list_numbers, 1_000_000) for _ in range(10)]
        l = []
        asc = cf.as_completed(procs)
        for process in asc:
            l.extend(process.result())

    mp_end_time = time.perf_counter()

    print(
        f"multi exec time:{mp_end_time - mp_start_time:.5f}. len: {len(l)}, elems: {l[10000:10014]}"
    )


# OUTPUT
# multi exec time:2.86173. len: 10000000, elems: [99539, 43419, 53584, 96622, 77050, 94317, 54246, 99545, 6726, 46120, 93583, 65628, 71087, 88166]
