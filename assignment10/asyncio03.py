import asyncio
import time
from random import random

async def producer(queue):
    print(f"{time.ctime()} Producer: Running")
    for i in range(10):
        value = random()
        await asyncio.sleep(value)
        await queue.put(value)
    print(f"{time.ctime()} Producer: Done")

async def consumer(queue):
    print(f"{time.ctime()} Consumer: Running")
    while True:
        item = await queue.get()
        print(f"{time.ctime()} >got {item}")
        if item:
            await asyncio.sleep(item)
        queue.task_done()

async def main():
    queue = asyncio.Queue()
    consumer_task = asyncio.create_task(consumer(queue))
    await asyncio.create_task(producer(queue))
    await queue.join()

asyncio.run(main())