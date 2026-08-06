import asyncio
import threading as td


async def func1():
    print(f"function 1 starts working on thread {td.current_thread()}")
    await asyncio.sleep(1)
    print(f"function 1 finished working on thread {td.current_thread()}")


async def func2():
    print(f"function 2 starts working on thread {td.current_thread()}")
    await asyncio.sleep(1)
    print(f"function 2 finished working on thread {td.current_thread()}")


async def main():
    await asyncio.gather(func1(), func2())


asyncio.run(main())

## Output
# function 1 starts working on thread <_MainThread(MainThread, started 16440)>
# function 2 starts working on thread <_MainThread(MainThread, started 16440)>
# function 1 finished working on thread <_MainThread(MainThread, started 16440)>
# function 2 finished working on thread <_MainThread(MainThread, started 16440)>
