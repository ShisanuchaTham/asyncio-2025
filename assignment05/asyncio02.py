# example of waiting for the first task to complete

from random import random
import asyncio

# coroutine to execute in a new task
async def task_coro(arg):
    #generate a random value between 0 and 1
    value = random()
    # block for a moment
    await asyncio.sleep(value)
    # report the value
    print(f'>task {arg} done with {value}')

# main coroutine
async def main():
    # create many tasks
    task = [asyncio.create_task(task_coro(i)) for i in range(10)]
    done,pending = await asyncio.wait(task, return_when=asyncio.FIRST_COMPLETED)
    print("done")
    first = done.pop()
    print(first)

asyncio.run(main()) 
