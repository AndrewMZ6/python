import random
import asyncio
from faker import Faker


# asynchronous fake email generator
async def email_gen(x):
    print("-> email_gen first line")
    emails = Faker()
    while x:
        x -= 1
        yield emails.email()


# asynchronous random number [0.0, 1.0) generator
async def num_gen(x):
    print("-> num_gen first line")
    while x:
        x -= 1
        yield random.random()


# prints random numbers in async for loop
async def numbers(x):
    print("-> numbers function first line")
    async for i in num_gen(x):
        print(i)
        await asyncio.sleep(1)


# prints emails in async for loop
async def emails(x):
    print("-> emails function first line")
    async for j in email_gen(x):
        print(j)
        await asyncio.sleep(1)


# main coroutine
async def main():
    await asyncio.gather(numbers(4), emails(3))


# creates eventloop and runs the main coroutine
if __name__ == "__main__":
    asyncio.run(main())

# output:
#
# -> f() first line
# -> mygen first line
# 0.007900825453143523
# -> h() first line
# -> email_gen first line
# julie81@example.net
# 0.9710039284381164
# kelly89@example.net
# 0.5811082916136737
# ojones@example.org
# 0.2650784122835159
# [Finished in 4.5s]
