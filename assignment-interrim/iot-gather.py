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
    results = await asyncio.gather(get_temperature(),get_humidity(),get_weather_api())
    for i in results:
        print(i)
    end = time.time()
    print(f"took {end-start:.2f}s")
asyncio.run(main())