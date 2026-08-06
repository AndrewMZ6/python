# https://www.codewars.com/kata/57b06f90e298a7b53d000a86/train/python
# solving codewars kata using asyncio

import asyncio
import time


def queue_time(customers, n):
    start = time.time()
    x = 0

    async def coro():
        nonlocal customers
        nonlocal x
        x += 1
        y = x
        while customers:
            print(f"coroutine number: {y}")
            print(f"customers list: {customers}")
            t = customers.pop(0)
            print(f"poped value from customers: {t}")
            await asyncio.sleep(t)

    tasks = (coro() for _ in range(n))

    async def main():
        await asyncio.gather(*tasks)

    asyncio.run(main())

    stop = time.time()
    x = 0
    return int(stop - start)


print("case: queue_time([], 1)")
print(f"resut: {queue_time([], 1)}", end="\n\n")  # expected 0
print("case: queue_time([5], 1)")
print(f"resut: {queue_time([5], 1)}", end="\n\n")  # expected 5
print("case: queue_time([2], 5)")
print(f"resut: {queue_time([2], 5)}", end="\n\n")  # expected 2
print("case: queue_time([1,2,3,4,5], 1)")
print(f"resut: {queue_time([1, 2, 3, 4, 5], 1)}", end="\n\n")  # expected 15
print("case: queue_time([1,2,3,4,5], 100)")
print(f"resut: {queue_time([1, 2, 3, 4, 5], 100)}", end="\n\n")  # expected 5
print("case: queue_time([2,2,3,3,4,4], 2)")
print(f"resut: {queue_time([2, 2, 3, 3, 4, 4], 2)}", end="\n\n")  # expected 9

# OUTPUT:
# case: queue_time([], 1)
# resut: 0

# case: queue_time([5], 1)
# coroutine number: 1
# customers list: [5]
# poped value from customers: 5
# resut: 5

# case: queue_time([2], 5)
# coroutine number: 1
# customers list: [2]
# poped value from customers: 2
# resut: 2

# case: queue_time([1,2,3,4,5], 1)
# coroutine number: 1
# customers list: [1, 2, 3, 4, 5]
# poped value from customers: 1
# coroutine number: 1
# customers list: [2, 3, 4, 5]
# poped value from customers: 2
# coroutine number: 1
# customers list: [3, 4, 5]
# poped value from customers: 3
# coroutine number: 1
# customers list: [4, 5]
# poped value from customers: 4
# coroutine number: 1
# customers list: [5]
# poped value from customers: 5
# resut: 15

# case: queue_time([1,2,3,4,5], 100)
# coroutine number: 1
# customers list: [1, 2, 3, 4, 5]
# poped value from customers: 1
# coroutine number: 2
# customers list: [2, 3, 4, 5]
# poped value from customers: 2
# coroutine number: 3
# customers list: [3, 4, 5]
# poped value from customers: 3
# coroutine number: 4
# customers list: [4, 5]
# poped value from customers: 4
# coroutine number: 5
# customers list: [5]
# poped value from customers: 5
# resut: 5

# case: queue_time([2,2,3,3,4,4], 2)
# coroutine number: 1
# customers list: [2, 2, 3, 3, 4, 4]
# poped value from customers: 2
# coroutine number: 2
# customers list: [2, 3, 3, 4, 4]
# poped value from customers: 2
# coroutine number: 1
# customers list: [3, 3, 4, 4]
# poped value from customers: 3
# coroutine number: 2
# customers list: [3, 4, 4]
# poped value from customers: 3
# coroutine number: 1
# customers list: [4, 4]
# poped value from customers: 4
# coroutine number: 2
# customers list: [4]
# poped value from customers: 4
# resut: 9

# [Finished in 36.3s]
