# file: rocketapp.py

from fastapi import FastAPI, HTTPException
import asyncio
import random
import time

app = FastAPI(title="Asynchronous Rocket Launcher")

# เก็บ task ของจรวด (optional)
rockets = []

async def launch_rocket(student_id: str, delay: float):
    """
    จำลองเวลาจรวดด้วย delay ที่กำหนด
    และพิมพ์ log ว่า rocket launched และ reached destination
    """
    print(f"Rocket {student_id} launched! ETA: {delay:.2f} seconds")
    start = time.monotonic()
    await asyncio.sleep(delay)
    elapsed = time.monotonic() - start
    print(f"Rocket {student_id} reached destination after {elapsed:.2f} seconds")

@app.get("/fire/{student_id}")
async def fire_rocket(student_id: str):
    """
    - ตรวจสอบ student_id ต้องเป็น 10 หลัก
    - สร้าง background task ยิง rocket
    - ใช้ delay เดียวกับ response
    - return JSON {"message": ..., "time_to_target": ...}
    """
    # ตรวจสอบ student_id
    if not student_id.isdigit() or len(student_id) != 10:
        raise HTTPException(status_code=400, detail="student ID ต้องเป็นตัวเลข 10 หลัก")

    # สุ่ม delay 1–2 วินาที
    delay = random.uniform(1, 2)

    # สร้าง background task ใช้ delay เดียวกัน
    task = asyncio.create_task(launch_rocket(student_id, delay))
    rockets.append(task)

    # คืนค่า response ใช้ delay เดียวกัน
    return {
        "message": f"Rocket {student_id} fired!",
        "time_to_target": round(delay, 2)
    }
