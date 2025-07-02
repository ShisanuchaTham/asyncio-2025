# example of waiting for all tasks to be completed with a timeout
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
    return f"task {arg} done with {value}"

# main coroutine
async def main():
    # create many tasks
    task = [asyncio.create_task(task_coro(i)) for i in range(10)]
    # wait for all tasks complete
    done,pending = await asyncio.wait(task, timeout=0.5)

    print(f"Done, {len(done)} task complete in time")

asyncio.run(main()) 

