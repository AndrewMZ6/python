import asyncio
import time

"""
In this file I wanted to check how the first coroutine will behave if it's scheduled to execute a
3 second long NON-BLOCKING operation before a second coroutine with a 4 seconds long
BLOCKING operation. Despite me understanding how event loop works, for some reason I thought that 
after 3 seconds the first coroutine will just interrupt the second's coroutine blocking flow
of execution.

It did not
"""

start = time.time()


async def non_blocking_func():
    start = time.time()
    print("non_blocking_func begins execution")
    await asyncio.sleep(3)
    end = time.time()
    print(f"non_blocking_func finished its execution in {end - start} seconds")


async def blocking_func():
    print("blocking_func begins execution")
    await asyncio.to_thread(time.sleep, 4)
    print("blocking_func finished its execution")


async def main():
    task1 = asyncio.create_task(non_blocking_func())
    task2 = asyncio.create_task(blocking_func())

    print("tasks created and now will be awaited")
    await asyncio.gather(task1, task2)
    print("both tasks are finished")


asyncio.run(main())
end = time.time()

print(f"The program ended in {end - start} seconds")


# tasks created and now will be awaited
# non_blocking_func begins execution
# blocking_func begins execution
# blocking_func finished its execution
# non_blocking_func finished its execution in 4.001134872436523 seconds
# both tasks are finished
# The program ended in 4.002854108810425 seconds




# AFTER ADDING asincio.to_thread

# tasks created and now will be awaited
# non_blocking_func begins execution
# blocking_func begins execution
# non_blocking_func finished its execution in 3.004077196121216 seconds
# blocking_func finished its execution
# both tasks are finished
# The program ended in 4.018345832824707 seconds