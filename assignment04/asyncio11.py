# task name
import asyncio

async def simple_task():
    await asyncio.sleep(1)

def on_done(task):
    print("Callback:", task.result())

async def main():
    task = asyncio.create_task(simple_task(), name="load data")
    print("Task Name:", task.get_name())
    await task

asyncio.run(main())