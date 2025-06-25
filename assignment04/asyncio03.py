# Create 2 Tasks with High-Level API
import asyncio

async def download_image(name, delay):
    print(f"{name} loading")
    await asyncio.sleep(delay)
    print(f"{name} loading comple")

async def main():
    # create 2 task in 1 time
    task1 = asyncio.create_task(download_image("image1",2))
    task2 = asyncio.create_task(download_image("image2",4))

    await task1
    await task2

asyncio.run(main())