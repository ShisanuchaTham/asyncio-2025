import asyncio, time, random

async def get_temperature():
    await asyncio.sleep(random.uniform(0.5,2.0))
    return f"{time.ctime()} Temp: 30C"

async def get_humidity():
    await asyncio.sleep(random.uniform(0.5,2.0))
    return f"{time.ctime()} Humidity: 60%"

async def get_weather_api():
    await asyncio.sleep(random.uniform(0.5,2.0))
    return f"{time.ctime()} Weather: Sunny"

async def main():
    start = time.time()
    tasks = {asyncio.create_task(get_temperature()),
             asyncio.create_task(get_humidity()),
             asyncio.create_task(get_weather_api())}
    while tasks:
        done, tasks = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
        for task in done:
            result = task.result()
            print(f"{time.ctime()} -> {result}")
    end = time.time()
    print(f"took {end-start:.2f}s")
asyncio.run(main())