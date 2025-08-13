import asyncio, time
async def worker_ok():
    print(f"{time.ctime()} [worker_ok] Start")
    await asyncio.sleep(1)
    print(f"{time.ctime()} [worker_ok] Done")

async def main():
    asyncio.create_task(worker_ok())
    await asyncio.sleep(2)

asyncio.run(main())