import asyncio
import random
import time

async def save_to_db(sensor_id, value):
    await asyncio.sleep(random.uniform(0.5,1.5))
    if value > 80:
        raise ValueError(f"Sensor {sensor_id}: value to high!")
    print(f"{time.ctime()} Saved {sensor_id} = {value}")

def task_done_callback(task: asyncio.Task):
    try:
        result = task.result()
        print(f"{time.ctime()} Task completed: {result}")
    except Exception as e:
        print(f"{time.ctime()} Task failed:{e}")

async def handle_sensor(sensor_id):
    value = random.randint(50,100)
    print(f"{time.ctime()} Sensor {sensor_id} got value: {value}")

    task = asyncio.create_task(save_to_db(sensor_id, value))
    task.add_done_callback(task_done_callback)

async def main():
    for i in range(5):
        await handle_sensor(i)
    await asyncio.sleep(2)

asyncio.run(main())