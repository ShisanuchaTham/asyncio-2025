# Asynchronous breakfast
import asyncio
from time import sleep, time


async def make_coffee(start):  # 1
    print(f"coffee: prepare ingridients in {time()-start:.3f} secs.")
    sleep(1)
    print(f"coffee: waiting...")
    await asyncio.sleep(5)  # 2: pause, another tasks can be run
    print(f"coffee: ready in {time()-start:.3f} secs.")

async def fry_eggs(start):  # 1
    print(f"eggs: prepare ingridients in {time()-start:.3f} secs.")
    sleep(1)
    print(f"eggs: frying...")
    await asyncio.sleep(3)  # 2: pause, another tasks can be run
    print(f"eggs: ready in {time()-start:.3f} secs.")

async def main():  # 1
    start = time()
    t1 = asyncio.create_task(make_coffee(start))
    t2 = asyncio.create_task(fry_eggs(start))

    await t1  # run task with await
    await t2
    print(f"breakfast is ready in {time()-start:.3f} secs.")


asyncio.run(main())  # run top-level function concurrently