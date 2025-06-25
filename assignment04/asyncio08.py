# get Exception
import asyncio

async def error_task():
    await asyncio.sleep(1)
    raise ValueError("ERROR")

async def main():
    task = asyncio.create_task(error_task())
    try:
        await task
    except Exception:
        print("Exception found:", task.exception())

asyncio.run(main())

