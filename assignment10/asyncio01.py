# example of using an asyncio queue
from random import random
import asyncio

async def producer(queue):
    print("Producer: Running")
    for i in range(10):
        value = i
        await asyncio.sleep(random())
        print(f">Producer put {value}")
        await queue.put(value)
    await queue.put(None)  # send an all done signal
    print("Producer: Done")

async def consumer(queue):
    print("Consumer: Running")
    while True:
        item = await queue.get()
        if item is None:
            break
        print(f"\t<Consumer got {item}")
    print("Consumer: Done")

async def main():
    queue = asyncio.Queue()
    await asyncio.gather(producer(queue), consumer(queue))

asyncio.run(main())