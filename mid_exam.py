import asyncio
import time
async def download(file_name,size_mb,delay_sec):
    start = time.perf_counter()
    await asyncio.sleep(delay_sec)
    end = time.perf_counter()
    speed = size_mb / (end - start)
    print(f"{file_name} downloaded at {speed:.2f} MB/s")
async def main():
    tasks = [asyncio.create_task(download("File A",100,1)),
             asyncio.create_task(download("File B",200,2)),
             asyncio.create_task(download("File C",300,3))]
    await asyncio.gather(*tasks)
asyncio.run(main())