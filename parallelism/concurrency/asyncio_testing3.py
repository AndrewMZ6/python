import asyncio
import time


# nonblocking function can ceeds workflow
# to event loop even if it's not finished
async def nonbocking():
    print("nonblocking staring")
    await asyncio.sleep(1)
    print("nonblocking finished")


# blocking function doesn't let workflow
# go anywhere untill it's finished
async def blocking():
    print("blocking staring")
    for i in range(5):
        print(f"bl -> {i}")
        time.sleep(1)
    print("blocking finished")


async def main():
    await asyncio.gather(nonbocking(), blocking())


if __name__ == "__main__":
    asyncio.run(main())


# output:
# nonblocking staring
# blocking staring
# bl -> 0
# bl -> 1
# bl -> 2
# bl -> 3
# bl -> 4
# blocking finished
# nonblocking finished
# [Finished in 5.3s]
