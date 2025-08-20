from random import random
import asyncio

async def task_coro(arg):
    value = random() * 10
    await asyncio.sleep(value)
    print(f'>Task {arg} done with {value}')

async def main():
    tasks = [asyncio.create_task(task_coro(i)) for i in range(10)]
    done, pending = await asyncio.wait(tasks, timeout=5)
    print(f"Done: {len(done)} tasks completed in time")
    print(f"Pending: {len(pending)} tasks")

asyncio.run(main())