import asyncio
import time
import random
from random import sample

# รายการสินค้าของแต่ละลูกค้า
item_pool = ["Apple", "Banana", "Milk", "Bread", "Cheese", "Eggs", "Juice", "Butter"]

# ฟังก์ชันสร้างรายการสินค้าสุ่มสำหรับลูกค้า
def generate_random_order(item_pool, min_items=1, max_items=4):
    num_items = random.randint(min_items, max_items)
    return sample(item_pool, num_items)

async def customer(name, order, queue):
    print(f"[{time.ctime()}] {name} เริ่มซื้อสินค้า: {order}")
    await queue.put((name, order))

async def cashier(name, processing_time, queue):
    while True:
        try:
            customer_name, order = await queue.get()
            # คิดเงินตามเวลาที่กำหนด (1 หรือ 2 วินาที ต่อสินค้า)
            print(f"[{time.ctime()}] {name} ทำรายการให้ {customer_name} ")
            for item in order:
                await asyncio.sleep(processing_time)
            print(f"[{time.ctime()}] {name} ทำรายการให้ {customer_name} เรียบร้อยแล้ว")
            queue.task_done()
        except asyncio.CancelledError:
            # เมื่อปิดระบบ
            break

async def main():
    queue = asyncio.Queue(maxsize=5)

    # เริ่มต้น Cashiers  คน
    cashier_tasks = [
        asyncio.create_task(cashier(f"cashier-{i}", i, queue))
        for i in range(1, 3)
    ]

    # เริ่มต้น Customer  คน
    customer_tasks = [
        asyncio.create_task(customer(f"customer-{i}", generate_random_order(item_pool), queue))
        for i in range(1, 11)
    ]

    # รอให้ลูกค้าทำงานส่งไปยังคิวครบทั้งหมด
    await asyncio.gather(*customer_tasks)

    # รอให้แคชเชียร์จัดการงานทั้งหมด
    await queue.join()

    # ยกเลิกแคชเชียร์เพื่อปิดระบบอย่างปลอดภัย
    for task in cashier_tasks:
        task.cancel()


    print("ร้านปิดแล้ว. ทุกงานเสร็จสิ้น.")

# รันโปรแกรม
asyncio.run(main())
